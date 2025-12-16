---
authors:
- Ali Hosseinzadeh
doc_id: arxiv:2512.12054v1
family_id: arxiv:2512.12054
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Universal Dynamics of Financial Bubbles in Isolated Markets: Evidence from
  the Iranian Stock Market'
url_abs: http://arxiv.org/abs/2512.12054v1
url_html: https://arxiv.org/html/2512.12054v1
venue: arXiv q-fin
version: 1
year: 2025
---


Ali Hosseinzadeh
  
Department of Physics, Shahid Beheshti University
  
Evin, Tehran 1983969411, Iran
  
ali\_hosseinzadeh@sbu.ac.ir

###### Abstract

Speculative bubbles exhibit common statistical signatures across many financial markets, suggesting the presence of universal underlying mechanisms. We test this hypothesis in the Iranian stock market, an economy that is highly isolated, subject to capital controls, and largely inaccessible to foreign investors. Using the Log-Periodic Power Law Singularity (LPPLS) model, we analyze two major bubble episodes in 2020 and 2023. The estimated critical exponents (β≈0.46\beta\approx 0.46 and β≈0.20\beta\approx 0.20) fall within the empirical ranges documented for canonical historical bubbles such as the 1929 DJIA crash and the 2000 Nasdaq episode. The Tehran Stock Exchange displays clear LPPLS hallmarks: faster-than-exponential price acceleration, log-periodic corrections, and stable estimates of the critical time horizon. These results indicate that endogenous herding, imitation, and positive-feedback dynamics—rather than exogenous shocks—play a dominant role even in politically and economically isolated markets. By showing that an emerging and semi-closed financial system conforms to the same dynamical patterns observed in global markets, this paper provides new empirical support for the universality of bubble dynamics. To the best of our knowledge, it also presents the first systematic LPPLS analysis of bubbles in the Tehran Stock Exchange. The findings highlight the usefulness of LPPLS-based diagnostic tools for monitoring systemic risk in emerging or restricted economies.

## 1 Introduction

Speculative bubbles and market crashes are widely observed phenomena in financial systems around the world. Over the past two decades, numerous studies have suggested that such events may share common underlying dynamics, independent of geography, market structure, or regulatory environment. In particular, the Log-Periodic Power Law Singularity (LPPLS) model—rooted in statistical physics and complex systems theory—has been successfully applied to a range of financial bubbles, from the 1929 Wall Street crash to the 2000 Nasdaq collapse [[1](https://arxiv.org/html/2512.12054v1#bib.bib1), [3](https://arxiv.org/html/2512.12054v1#bib.bib3), [2](https://arxiv.org/html/2512.12054v1#bib.bib2)]. These studies have revealed recurring features such as faster-than-exponential growth, log-periodic oscillations, and identifiable precursors to critical transitions.

While the LPPLS model has been successfully applied to various well-integrated and highly liquid markets, its validity in structurally isolated or emerging financial systems remains underexplored. Most empirical studies have focused on bubbles in advanced economies, where data accessibility, institutional stability, and high-frequency trading behaviors support robust model calibration [[1](https://arxiv.org/html/2512.12054v1#bib.bib1), [4](https://arxiv.org/html/2512.12054v1#bib.bib4), [5](https://arxiv.org/html/2512.12054v1#bib.bib5)].

The Iranian stock market, in contrast, presents a unique opportunity to test whether the endogenous mechanisms captured by LPPLS—such as herding, reflexivity, and log-periodic behavior—still manifest in a market characterized by international sanctions, restricted capital flows, and limited foreign investor access [[8](https://arxiv.org/html/2512.12054v1#bib.bib8)].

This raises a broader theoretical question: To what extent are the dynamics of financial bubbles universal, and do they hold even in markets that are isolated from the global financial system?

While the LPPLS model has been extensively validated in well-integrated, liquid markets, its applicability in emerging or structurally isolated markets—such as Iran—remains an open empirical and theoretical question.
Prior studies have primarily focused on developed economies, where institutional maturity, transparency, and data availability support robust calibration [[1](https://arxiv.org/html/2512.12054v1#bib.bib1), [4](https://arxiv.org/html/2512.12054v1#bib.bib4), [9](https://arxiv.org/html/2512.12054v1#bib.bib9)]. In contrast, the Tehran Stock Exchange (TSE) operates under international sanctions, limited foreign participation, and a retail-driven structure—conditions rarely tested under the LPPLS framework.

Addressing this gap not only advances the empirical frontier of LPPLS applications but also contributes to a larger conversation in econophysics and complex systems theory: whether endogenous mechanisms like herding, positive feedback, and reflexivity exhibit universal behavior across financial systems regardless of geopolitical or structural isolation [[10](https://arxiv.org/html/2512.12054v1#bib.bib10), [11](https://arxiv.org/html/2512.12054v1#bib.bib11)].

This paper builds upon this body of work by investigating whether these universal features of bubble dynamics also appear in an economically and politically isolated market: the Tehran Stock Exchange (TSE). We propose that financial instabilities, such as those observed during the 2020 and 2023 crashes in Iran, conform to generalizable principles of collective behavior and criticality—even in the absence of global capital flows or mature institutional frameworks. This hypothesis aligns with recent perspectives in econophysics, which emphasize the role of endogenous feedback mechanisms like herding, imitation, and self-organization in driving speculative dynamics [[9](https://arxiv.org/html/2512.12054v1#bib.bib9), [10](https://arxiv.org/html/2512.12054v1#bib.bib10)].

In the podcast episode What’s Been Happening With the Iranian Stock Market by Bloomberg’s Odd Lots, Maciej Wojtal, a London-based fund manager specializing in Iranian stocks, describes the Tehran Stock Exchange as “one of the world’s most unfamiliar markets” [[8](https://arxiv.org/html/2512.12054v1#bib.bib8)]. This unfamiliarity arises primarily due to international sanctions that limit access to accurate information and restrict foreign investment in Iranian stocks. Despite Iran being a large middle-income country with significant economic potential, its stock market remains largely isolated from global financial systems, rendering it a niche area for specialized investors. The main contribution of this paper is to provide the first systematic application of the LPPLS model to speculative bubbles in the Tehran Stock Exchange. By analyzing two major episodes—the 2020 crash and the 2023 bubble—we show that the estimated LPPLS exponents fall within the empirical ranges reported for canonical bubbles in major international markets. This demonstrates that bubble dynamics in an isolated, sanction-constrained economy share the same universal signatures as those in more integrated systems. In addition, we complement the parametric LPPLS analysis with a non-parametric log-periodic detection procedure and contextual “stories” that link the bubble phases to macroeconomic conditions and policy interventions in Iran.

This paper aims to demystify the Tehran Stock Exchange by analyzing the bubble dynamics associated with the 2020 crash and the 2023 bubble. We utilize the Log-Periodic Power Law Singularity (LPPLS) model to demonstrate that, despite the market’s unfamiliarity, it exhibits patterns similar to other global stock markets. Our findings suggest that, using only data available before each crash, there was scope to anticipate these bubbles in the Tehran stock market, akin to the predictability documented in more familiar markets.

The 2020 crash had a profound impact on the Tehran Stock Exchange, with the total market index plummeting by approximately 42% (Figure 1). This event stands as the most significant crash in the market’s history. While some experts attribute the crash to political issues, our analysis indicates that positive feedback mechanisms were the primary drivers. For example, the Persian Gulf Petrochemical Industries Corporation (PGPIC), the largest company on the Tehran Stock Exchange, saw its valuation peak at $22.4 billion during the bubble, only to decline to around $10 billion currently. Similarly, the Social Security Investment Company (SSIC), also known by its Persian acronym SHASTA, experienced a peak valuation of approximately $24 billion, which has since decreased to around $3 billion.

In the following sections, we will present the results of our LPPLS analysis, shedding light on the bubble characteristics of the Tehran stock market during this period and reinforcing the potential for bubble predictability even in less familiar markets.

![Refer to caption](ndex_log.png)


Figure 1: The 2020 crash (red dashed line) and the 2023 bubble (green dashed line)

## 2 Review of the LPPLS Model and Positive Feedback Mechanisms

### 2.1 Overview of the LPPLS Model

The Log-Periodic Power Law Singularity (LPPLS) model is a mathematical framework used to describe and predict the behavior of asset prices during financial bubbles and crashes [[1](https://arxiv.org/html/2512.12054v1#bib.bib1), [12](https://arxiv.org/html/2512.12054v1#bib.bib12)]. Developed by Didier Sornette and his collaborators, the LPPLS model captures the characteristic super-exponential growth of asset prices leading up to a critical point, often followed by a market correction or crash. The model incorporates both the accelerating growth of prices and the oscillatory behavior caused by investor herding and positive feedback mechanisms.

### 2.2 Success and Applications of the LPPLS Model

The LPPLS has been successfully applied to a wide range of historical bubbles, including the 1929 Wall Street crash, the 1987 Black Monday, the 2000 dot-com bubble, the 2006–2008 housing market crash, and even recent phenomena such as the 2020 COVID-induced crash in the S&P 500 [[1](https://arxiv.org/html/2512.12054v1#bib.bib1), [3](https://arxiv.org/html/2512.12054v1#bib.bib3), [12](https://arxiv.org/html/2512.12054v1#bib.bib12), [7](https://arxiv.org/html/2512.12054v1#bib.bib7)].

The LPPLS model captures two key features of financial bubbles: faster-than-exponential price growth driven by positive feedback mechanisms (such as herding and momentum trading), and log-periodic oscillations that arise from discrete scale invariance and hierarchical structure in trader interactions. These oscillations often manifest as volatility clustering and can serve as early-warning signals of regime shifts. Numerous empirical studies have shown that the model not only fits historical data well, but also provides ex-ante predictive power when carefully calibrated [[4](https://arxiv.org/html/2512.12054v1#bib.bib4), [6](https://arxiv.org/html/2512.12054v1#bib.bib6)].

Its success lies in its capacity to model endogenous market dynamics using principles from statistical physics and complex systems, bridging economic theory with mathematical rigor. In the context of this study, applying the LPPLS model to the Iranian market provides a robust framework for comparing the universality of bubble dynamics across structurally different financial systems.

### 2.3 Mathematical Formulation

The LPPLS model posits that the logarithm of an asset’s price p​(t)p(t) can be described by a function that includes a power law term and a log-periodic oscillation term. The general form of the LPPLS equation is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ln⁡p​(t)=A+B​(tc−t)β+C​(tc−t)β​cos⁡[ω​ln⁡(tc−t)+ϕ],\ln p(t)=A+B(t\_{c}-t)^{\beta}+C(t\_{c}-t)^{\beta}\cos\left[\omega\ln(t\_{c}-t)+\phi\right], |  | (1) |

where:

* •

  ln⁡p​(t)\ln p(t) is the natural logarithm of the asset price at time tt.
* •

  AA is a constant representing the baseline level of ln⁡p​(t)\ln p(t).
* •

  BB and CC are amplitudes of the power law growth and the oscillatory terms, respectively.
* •

  tct\_{c} is the critical time at which the bubble is expected to burst or the market is expected to crash.
* •

  β\beta is the exponent of the power law term, typically constrained between 0 and 1 (0<β<10<\beta<1).
* •

  ω\omega is the angular frequency of the logarithmic periodic oscillations.
* •

  ϕ\phi is a phase shift that adjusts the starting point of the oscillations.

#### 2.3.1 Interpretation of the Parameters

* •

  Power Law Term (B​(tc−t)βB(t\_{c}-t)^{\beta}): This term captures the accelerating growth of prices as they approach the critical time tct\_{c}. The exponent β\beta determines the rate of this acceleration.
* •

  Log-Periodic Oscillation Term (C​(tc−t)β​cos⁡[ω​ln⁡(tc−t)+ϕ]C(t\_{c}-t)^{\beta}\cos\left[\omega\ln(t\_{c}-t)+\phi\right]): This term accounts for the oscillatory behavior observed in asset prices due to collective investor behaviors like herding. The frequency ω\omega and phase ϕ\phi characterize the pattern of these oscillations.

### 2.4 Positive Feedback and Bubble Formation

Positive feedback mechanisms are central to the formation and growth of financial bubbles [[1](https://arxiv.org/html/2512.12054v1#bib.bib1)]. In the context of the LPPLS model, positive feedback refers to the self-reinforcing process where rising asset prices attract more investors, further driving up prices. This phenomenon is often fueled by psychological factors such as:

* •

  Herding behavior refers to the tendency of investors to follow the actions of the majority—buying assets simply because others are buying, regardless of underlying fundamentals [[14](https://arxiv.org/html/2512.12054v1#bib.bib14), [16](https://arxiv.org/html/2512.12054v1#bib.bib16), [15](https://arxiv.org/html/2512.12054v1#bib.bib15)].
* •

  Expectation of Future Price Increases: The belief that prices will continue to rise motivates more buying, creating a feedback loop.
* •

  Speculative Investment: Investors purchase assets with the intent to sell at higher prices in the short term, contributing to price inflation.

As a result of positive feedback, asset prices deviate significantly from their intrinsic values, leading to unsustainable growth patterns that the LPPLS model aims to capture. The model’s ability to characterize the super-exponential growth and oscillatory behavior of prices makes it a valuable tool for predicting the timing of market corrections or crashes.

### 2.5 Application to the Tehran Stock Market

Applying the LPPLS model to the Tehran Stock Exchange allows for the analysis of bubble dynamics in an unfamiliar and largely isolated market. Despite the lack of widespread international engagement due to sanctions, the Tehran stock market exhibits patterns consistent with other global markets experiencing bubbles. The positive feedback mechanisms observed—such as rapid price increases attracting more investors—mirror those in more familiar markets.

By fitting the LPPLS model to the Tehran stock market data leading up to the 2020 crash and the 2023 bubble, we aim to demonstrate that:

* •

  The market experienced super-exponential growth indicative of a financial bubble.
* •

  When calibrated on data up to several weeks before the crash, the model can predict a critical time tct\_{c} that aligns closely with the eventual crash date.
* •

  Positive feedback mechanisms were significant contributors to the bubble’s formation and eventual burst.

In the next section, we will delve into the empirical results of our LPPLS analysis on the Tehran stock market, highlighting how the model’s parameters reflect the market’s dynamics during the bubble period.

## 3 Market Structure and Performance of the Tehran Stock Exchange

### 3.1 Market Structure of TSE

The Tehran Stock Exchange (TSE) comprises multiple segments catering to different financial instruments and investor types. The largest and most active segment is the Equities Market, where publicly traded companies issue and trade shares. This market consists of a primary segment for new stock issuance and a secondary segment for trading existing shares. Companies are listed on either the First Market (Main Board), which includes well-established firms meeting stringent listing requirements, or the Second Market, where smaller and less liquid companies operate.

Alongside equities, the Debt Market facilitates investment in government bonds, Sukuk (Islamic bonds), and corporate debt securities, providing stability for risk-averse investors. The Derivatives Market offers options and futures contracts, enabling investors to hedge against price fluctuations. Furthermore, Exchange-Traded Funds (ETFs) have gained prominence, with funds tracking both equity indices and fixed-income securities. Finally, the Professional Investment Market serves institutional investors and specialized financial products, including structured funds.

### 3.2 Trading System and Rules

TSE operates under a structured regulatory framework that dictates market behavior. Trading is conducted from Saturday to Wednesday, between 9:00 AM and 12:30 PM local time. To mitigate excessive volatility, daily price fluctuations are restricted to ±5%. When a stock reaches the upper limit and the demand for buying exceeds the available supply, a buy queue is formed. Conversely, when a stock hits the lower limit and selling pressure dominates, a sell queue emerges.

The fluctuation limit plays a crucial role in stabilizing prices by preventing excessive volatility within a single trading day, but it also directly contributes to the formation of these buy and sell queues, which can delay price discovery.
Additionally, transactions follow a T+2 settlement cycle, meaning trades are finalized two business days after execution. The T+2 settlement system refers solely to the cash and ownership transfer timing and does not impose a minimum holding period for stocks; investors can sell their shares at any time during the same day if market conditions allow.

### 3.3 Key Features and Challenges of TSE

TSE presents a mix of strengths and challenges. A key advantage is its diverse investment landscape, offering opportunities across equities, bonds, ETFs, and derivatives. Regulatory oversight by the Securities and Exchange Organization (SEO) further enhances market integrity and investor confidence. Additionally, market capitalization has expanded significantly in recent years, signaling the growing importance of TSE within the region.

Despite these strengths, challenges persist. Foreign investment remains restricted due to economic sanctions, limiting international capital inflows. Liquidity constraints affect certain stocks, making large-volume trades difficult. Moreover, the fixed daily price fluctuation limits can sometimes result in artificial pricing distortions and sharp market swings.

## 4 Tehran Stock Exchange (TSE) Market Overview in 2020

In order to analyze the Tehran Stock Exchange (TSE) around mid-2020 and detect potential bubble-like behavior, we extract key statistics from official reports111This section is based on official reports of the TSE, which can be found in [[17](https://arxiv.org/html/2512.12054v1#bib.bib17)].. Below is a comprehensive market overview for that period.

### 4.1 Number of Public Companies Traded

By the end of March 2021, the number of listed companies across different markets was:

* •

  Tehran Stock Exchange (TSE): 369 companies
* •

  Iran Fara Bourse (IFB): 141 companies
* •

  Base Market (OTC): 174 companies
* •

  Total listed companies: 684 entities

### 4.2 Market Capitalization

The total market capitalization of the Tehran Stock Exchange in March 2021 was 72,418,800 billion IRR (approx. 359 billion $), marking a 177% increase compared to the previous year.

Breakdown by financial instrument type:

| Financial Instrument | Market Share (%) |
| --- | --- |
| Equities (Stock Market) | 23 |
| Debt Market (Fixed-Income Securities) | 58 |
| ETFs | 8 |
| Physical Commodities & Energy Exchange | 11 |

Table 1: Market Capitalization Breakdown in 2020

### 4.3 Trading Frequency and Volume

For the Iranian fiscal year 1399 (20 March 2020–20 March 2021), official statistics from
the Securities and Exchange Organization (SEO) report that the total number of stock trades
across the Tehran Stock Exchange and Iran Fara Bourse reached 559,597,153 transactions.
Over the same period, aggregate trading volume amounted to 2,825,997,294 thousand
shares (roughly 2.83×10122.83\times 10^{12} shares), with a total traded value of 33,882,952 billion
IRR. The reported daily averages over 1399 were 27,251,350 trades, 138,499,921 thousand
shares (about 1.38×10111.38\times 10^{11} shares), and 1,642,621 billion IRR in trading value.222All
figures in this subsection are taken from the SEO’s end-of-year report for 1399.

### 4.4 Sectoral Breakdown & Key Industries

Top Traded Sectors by Market Share:

| Industry | Trading Value (Billion IRR) |
| --- | --- |
| Oil, Gas, and Petroleum Products | 203,985 |
| Basic Metals (Steel, Copper, Aluminum) | 139,466 |
| Banking and Financial Services | 103,004 |
| Chemical Products | 149,670 |

Table 2: Top Traded Sectors in 1399

### 4.5 Trading Statistics in August 2020

| Exchange | Stock Trading Value (Billion IRR) | MoM Change (%) | YoY Change (%) |
| --- | --- | --- | --- |
| TSE | 3,343,361 | -10.7 | +1561.5 |
| IFB | 1,106,645 | -19.1 | +735.2 |

Table 3: Trading Statistics in August 2020

Observations:

* •

  Stock trading value dropped 10.7% in TSE and 19.1% in IFB, confirming reduced liquidity.
* •

  Massive 1561% YoY increase before the crash suggests bubble-like conditions.

### 4.6 Bubble Genesis: The “Stories” Behind the 2020 Crashes

The 2020 Tehran Stock Exchange bubble was catalyzed by a multifaceted “story” built on fiscal desperation, state-led privatization, and a mass behavioral shift in investment practices.

Amid reimposed U.S. sanctions following the collapse of the Joint Comprehensive Plan of Action (JCPOA), the Iranian government actively encouraged investment in the stock market as a means of compensating for its fiscal deficits. A wave of state-owned enterprise IPOs—most notably including major players like Shasta—was promoted as a national wealth-building initiative. Retail investors, many of them first-time participants and explicitly incentivized by state messaging, entered the market en masse.

At the same time, concurrent hyperinflation and the severe devaluation of the Iranian rial positioned equities as a perceived hedge against inflation. These economic pressures, combined with speculative momentum and extensive government propaganda, pushed valuations far beyond economic fundamentals.

The TEDPIX index ultimately rallied over 190% during 2020, before the eventual crash reflected the unsustainability of this speculative boom in the face of deteriorating macroeconomic and geopolitical conditions. This combination of sanctions, inflationary pressure, and state-led promotion of equity investment created a fertile environment for strong positive feedback and herding into stocks, consistent with the LPPLS bubble regime identified in our empirical analysis.

### 4.7 Evidence of a Bubble Formation

The TSE saw an extraordinary bull run from late 2019 to mid-2020, followed by a sharp correction in the second half of 1399 (Iranian calendar).

Key signs of a bubble:

* •

  Massive market capitalization growth (177% YoY increase).
* •

  Exponential price increases across major indices.
* •

  P/E ratio surged above historical averages, indicating speculative investments.
* •

  Daily trade volumes skyrocketed, driven by retail participation.

This aligns with the LPPLS model criteria for bubble detection. Also, we plot [2](https://arxiv.org/html/2512.12054v1#S4.F2 "Figure 2 ‣ 4.7 Evidence of a Bubble Formation ‣ 4 Tehran Stock Exchange (TSE) Market Overview in 2020 ‣ Universal Dynamics of Financial Bubbles in Isolated Markets: Evidence from the Iranian Stock Market") which is Smoothed Returns Leading Up To The 2020-08-09 Crash. Both SMA and EMA show a rising trend in returns from late 2019 until the crash. This suggests super-exponential growth, which is a hallmark of speculative bubbles. In a normal market, returns fluctuate around a mean, but here, they increase progressively, meaning investors are driving up prices faster and faster.

![Refer to caption](output__10_.png)


Figure 2: Smoothed Returns Leading Up To The 2020-08-09 Crash

### 4.8 Conclusion

The TSE in mid-2020 exhibited strong indications of a speculative bubble, characterized by high market participation, extreme liquidity influx, and super-exponential price growth. This ultimately resulted in a major market correction.

## 5 Analysis of the 2020 Tehran Stock Market Crash: Black Sunday

In this section, we introduce the empirical framework used in this paper and apply it to the 2020 Tehran Stock Exchange bubble. We first present the data and LPPLS calibration scheme for the Tehran market, then explain how we scan over fitting windows to identify bubble inception dates using a Lagrange-regularized procedure. Finally, we outline the non-parametric Lomb–Scargle and (H, q)-derivative diagnostics used to validate log-periodic structures.

### 5.1 Data Collection and Preprocessing

The data used in this analysis comprises the Adjusted Close prices of the Tehran Stock Exchange (TSE) index from January 2017 to August 2020. Due to the unique characteristics of the TSE, including limited accessibility and less frequent trading days compared to other global markets, careful preprocessing was necessary. Non-trading days and public holidays were accounted for to ensure continuity in the time series data. The data was filtered to create multiple time windows for analysis, allowing us to assess the robustness and consistency of the LPPLS model predictions across different periods leading up to the 2020 crash.

### 5.2 LPPLS Model Fitting Procedure

To evaluate how well the 2020 Tehran stock market crash could be anticipated using only pre-crash data, we fitted the LPPLS model to the Adjusted Close price data over various time intervals.
The calibration of the LPPLS model was performed using the robust and stable two-step nonlinear estimation scheme proposed by Filimonov and Sornette [[30](https://arxiv.org/html/2512.12054v1#bib.bib30)]. In this method, the nonlinear parameters (tc,β,ω)(t\_{c},\beta,\omega) are explored over a defined grid, and for each candidate triplet, the corresponding linear parameters (A,B,C1,C2)(A,B,C\_{1},C\_{2}) are estimated via ordinary least squares. The optimal parameter set is selected as the one minimizing the root-mean-square error (RMSE) between the logarithmic observed prices and the LPPLS fit. This approach ensures robustness against noise and enhances convergence, especially in the presence of pronounced log-periodic components.
Constraints were applied to the parameters based on theoretical considerations:

* •

  The exponent β\beta was constrained within (0,1)(0,1) to ensure super-exponential growth.
* •

  The angular frequency ω\omega was set to be positive to capture the oscillatory behavior.
* •

  The critical time tct\_{c} was restricted to be after the last data point in each time window to prevent fitting past data with future events.

To evaluate the predictive power of the model, we fitted333See Appendix I. 
it over multiple time windows and examined how the estimated critical time tct\_{c} aligned with the actual crash date. However, this methodology lacks robustness. Therefore, in the following sections, we adopt the approaches proposed in [[18](https://arxiv.org/html/2512.12054v1#bib.bib18), [19](https://arxiv.org/html/2512.12054v1#bib.bib19)] to systematically identify the inception of financial bubbles, rather than relying on arbitrary time window selection. In our analysis, t1t\_{1} denotes the start date of the fitting window, representing a candidate point where the financial bubble may have begun, while t2t\_{2} is the end date, typically fixed at the known crash date or shifted earlier for robustness testing. The LPPLS model is calibrated over each window [t1,t2][t\_{1},t\_{2}] to evaluate which start date best captures the bubble dynamics. This [t1,t2][t\_{1},t\_{2}] notation is a common jargon in LPPLS analysis used to define the calibration window for bubble detection.

### 5.3 Different Windows with a Fixed t2t\_{2}

First of all, approximately one year before the crash, the LPPLS fitting tends to become more precise [[1](https://arxiv.org/html/2512.12054v1#bib.bib1)]. Moreover, we generally expect that the estimated critical time tct\_{c} will be close to, but systematically later than, the actual crash date [[1](https://arxiv.org/html/2512.12054v1#bib.bib1)].

Here, we fixed t2t\_{2} as the actual crash time to fit the LPPLS model, as shown in Figures [3](https://arxiv.org/html/2512.12054v1#S5.F3 "Figure 3 ‣ 5.3 Different Windows with a Fixed 𝑡₂ ‣ 5 Analysis of the 2020 Tehran Stock Market Crash: Black Sunday ‣ Universal Dynamics of Financial Bubbles in Isolated Markets: Evidence from the Iranian Stock Market") and Table [4](https://arxiv.org/html/2512.12054v1#S5.T4 "Table 4 ‣ 5.3 Different Windows with a Fixed 𝑡₂ ‣ 5 Analysis of the 2020 Tehran Stock Market Crash: Black Sunday ‣ Universal Dynamics of Financial Bubbles in Isolated Markets: Evidence from the Iranian Stock Market"). Nevertheless, we will show (in section 5.4) that plot 4 in Figure [3](https://arxiv.org/html/2512.12054v1#S5.F3 "Figure 3 ‣ 5.3 Different Windows with a Fixed 𝑡₂ ‣ 5 Analysis of the 2020 Tehran Stock Market Crash: Black Sunday ‣ Universal Dynamics of Financial Bubbles in Isolated Markets: Evidence from the Iranian Stock Market") represents the optimal choice 444This optimized choice is, of course, an approximation, as the parameters vary in a sensitive manner, leading to an uncertainty in the prediction of tct\_{c} by approximately several weeks.
, using Lagrange regularization to further justify this selection. In the next subsection, we also conduct a robustness test by shifting t2t\_{2} backward to evaluate the stability of the results.

Table 4: LPPLS Model Parameters for Plots 1–4 (2020 crash)

| Parameter | Plot 1 | Plot 2 | Plot 3 | Plot 4 |
| --- | --- | --- | --- | --- |
| AA | 22.8640 | 22.6180 | 22.9161 | 16.2747 |
| BB | -5.7278 | -5.5960 | -5.7556 | -0.2767 |
| CC | 0.0288 | 0.0515 | 0.0417 | 0.0077 |
| β\beta | 0.1 | 0.1 | 0.1 | 0.4556 |
| ω\omega | 10.6667 | 11.25 | 11.25 | 9.8889 |
| ϕ\phi | -0.8462 | 2.3792 | 2.1545 | 1.6631 |
| tct\_{c} (estimated) | 2020-09-07 | 2020-09-03 | 2020-09-07 | 2020-09-22 |
| tct\_{c} (days from start) | 646.39 | 976.39 | 1286.27 | 296.90 |

![Refer to caption](output__32_.png)


Figure 3: Results for LPPLS Model on different time frames (2020 bubble)

#### 5.3.1 Discussion of Results

These results support the hypothesis that the Tehran stock market bubble was driven by
positive feedback mechanisms, as captured by the LPPLS model. The ability of the model,
when calibrated solely on pre-crash data, to predict a critical time close to the realized crash reinforces its applicability even in less familiar markets like the TSE.

### 5.4 Methodology: Bubble Start Detection via Lagrange-Regularized LPPLS

To identify the inception of speculative bubbles preceding major financial crashes, we apply the Log-Periodic Power Law Singularity (LPPLS) model combined with a Lagrange-regularized calibration approach, following the methodology introduced by Sornette et al. [[18](https://arxiv.org/html/2512.12054v1#bib.bib18)] and Zhou & Sornette [[19](https://arxiv.org/html/2512.12054v1#bib.bib19)].

#### 5.4.1 LPPLS Model Framework

The LPPLS model captures the accelerating price dynamics during bubbles.
The empirical range for the log-periodic frequency parameter ω\omega is typically set within [6,13][6,13], based on numerous studies of financial bubbles [[13](https://arxiv.org/html/2512.12054v1#bib.bib13)],[[20](https://arxiv.org/html/2512.12054v1#bib.bib20)]. However, in practice, broader ranges such as [4,15][4,15] are often explored, especially when market dynamics are unusual or when the visibility of oscillations is affected by noise or structural shifts in the market [[13](https://arxiv.org/html/2512.12054v1#bib.bib13)].

#### 5.4.2 Window Scanning and Lagrange Regularization

To determine the most probable start date of the 2020 bubble (t1t\_{1}), we scanned backward over a series of candidate windows [t1,t2][t\_{1},t\_{2}] and fitted the LPPLS model to the log-price series within each window. For each fit, we computed the normalized sum of squared residuals:

|  |  |  |
| --- | --- | --- |
|  | χn​p2​(t1)=1N−k​∑i=1N(log⁡p​(ti)−f^​(ti))2\chi^{2}\_{np}(t\_{1})=\frac{1}{N-k}\sum\_{i=1}^{N}\left(\log p(t\_{i})-\hat{f}(t\_{i})\right)^{2} |  |

where kk is the number of free parameters in the model, and f^​(t)\hat{f}(t) is the fitted LPPLS function.

To correct for the tendency of short windows to overfit, we applied a Lagrange regularization term:

|  |  |  |
| --- | --- | --- |
|  | χλ2​(t1)=χn​p2​(t1)−λ​(t2−t1)\chi^{2}\_{\lambda}(t\_{1})=\chi^{2}\_{np}(t\_{1})-\lambda(t\_{2}-t\_{1}) |  |

The optimal bubble start time t1∗t\_{1}^{\*} is selected as the window start that minimizes χλ2​(t1)\chi^{2}\_{\lambda}(t\_{1}).
The regularization coefficient λ\lambda was estimated as the negative slope of a linear regression of χn​p2​(t1)\chi^{2}\_{np}(t\_{1}) versus window size. The optimal bubble start time t1∗t\_{1}^{\*} was defined as the window start that minimized χλ2​(t1)\chi^{2}\_{\lambda}(t\_{1}).

LPPLS fits were calculated using a grid-based search over nonlinear parameters (tc,β,ω)(t\_{c},\beta,\omega) and linear regression for (A,B,C1,C2)(A,B,C\_{1},C\_{2}). This semi-parametric method provided robustness to local minima and instability.

#### 5.4.3 Robustness Test by Shifting t2t\_{2}

To verify the stability of the estimated bubble inception time, we repeated the scanning process by shifting t2t\_{2} backward in increments of 15 to 60 trading days. For each new t2t\_{2}, we recalculated the Lagrange-regularized residual curve χλ2​(t1)\chi^{2}\_{\lambda}(t\_{1}).

The resulting curves were overlaid to visually assess whether the estimated bubble start remained consistent.

#### 5.4.4 Visualization

Two key figures support the detection of the 2020 bubble:

* •

  Figure 4: Bubble Start Detection (2020 Crash). This plot shows the evolution of χn​p2​(t1)\chi^{2}\_{np}(t\_{1}) and χλ2​(t1)\chi^{2}\_{\lambda}(t\_{1}) across candidate windows. The minimum of the regularized curve identifies the optimal start time.

  Interpretation: Although χn​p2\chi^{2}\_{np} tends to favor short windows—resulting in lower residual error but potential overfitting—χλ2\chi^{2}\_{\lambda} penalizes such windows and identifies the interval between 2019-12-01 and 2020-01-05 as the most plausible inception period for the bubble. This range corresponds to the onset of super-exponential growth and log-periodic oscillations that characterize the build-up to the 2020 crash. As previously claimed, Figure [3](https://arxiv.org/html/2512.12054v1#S5.F3 "Figure 3 ‣ 5.3 Different Windows with a Fixed 𝑡₂ ‣ 5 Analysis of the 2020 Tehran Stock Market Crash: Black Sunday ‣ Universal Dynamics of Financial Bubbles in Isolated Markets: Evidence from the Iranian Stock Market") (Plot 4) represents the optimal choice, and this section provides empirical support for that claim. Moreover, if we fix the bubble start at 2020-01-05, the estimated value of β\beta is approximately 0.5. Therefore, the β\beta parameter for the optimally chosen window of the 2020 crash lies in the range of approximately 0.45 to 0.5.
* •

  Figure 5: Robustness Test (2020 Crash). This figure overlays the χλ2​(t1)\chi^{2}\_{\lambda}(t\_{1}) curves for multiple shifted t2t\_{2} values. Despite the changes in end-date, all curves reach a minimum in the narrow range around early 2020.

  Interpretation: The clustering of minima near 2020-01 affirms the robustness of the Lagrange-regularized LPPLS approach. This indicates that the bubble start estimation is stable and does not significantly depend on the precise crash date definition.

![Refer to caption](m.png)


Figure 4: Bubble Start Detection Using Lagrange-Regularized LPPLS

![Refer to caption](m2.png)


Figure 5: Robustness Test Of Bubble Start Detection (Varying T2T\_{2})

### 5.5 Non-Parametric Validation of Log-Periodicity via Lomb Periodogram Analysis

To rigorously validate the presence of log-periodic structures in the price dynamics prior to the 2023 correction phase, we employed the non-parametric spectral methodology proposed by Zhou and Sornette [[21](https://arxiv.org/html/2512.12054v1#bib.bib21), [25](https://arxiv.org/html/2512.12054v1#bib.bib25)]. While the LPPLS model provides a parametric framework to fit financial bubbles, its sensitivity to parameter initialization and the potential for overfitting under noisy conditions necessitate an independent test of the log-periodicity hypothesis. The Lomb–Scargle periodogram offers a model-free approach to detect periodic structures in unevenly spaced or transformed time series, particularly suited to the LPPLS framework where oscillations occur in logarithmic time.

### Methodology

Let p​(t)p(t) denote the observed price series and tct\_{c} the estimated critical time. The first step involves transforming time into logarithmic space:

|  |  |  |
| --- | --- | --- |
|  | x=log⁡(tc−t),for ​t<tc.x=\log(t\_{c}-t),\quad\text{for }t<t\_{c}. |  |

Next, we fit and subtract the power-law trend from the log-price:

|  |  |  |
| --- | --- | --- |
|  | log⁡p​(t)≈A+B​(tc−t)β,\log p(t)\approx A+B(t\_{c}-t)^{\beta}, |  |

yielding the residuals:

|  |  |  |
| --- | --- | --- |
|  | r​(t)=log⁡p​(t)−[A+B​(tc−t)β],r(t)=\log p(t)-[A+B(t\_{c}-t)^{\beta}], |  |

which are expected to contain the log-periodic oscillations:

|  |  |  |
| --- | --- | --- |
|  | r​(t)≈C​(tc−t)β​cos⁡[ω​log⁡(tc−t)+ϕ].r(t)\approx C(t\_{c}-t)^{\beta}\cos[\omega\log(t\_{c}-t)+\phi]. |  |

To test for periodicity in x=log⁡(tc−t)x=\log(t\_{c}-t), we compute the Lomb–Scargle periodogram P​(ω)P(\omega) of the residuals:

|  |  |  |
| --- | --- | --- |
|  | P​(ω)=12​{[∑iri​cos⁡ω​(xi−τ)]2∑icos2⁡ω​(xi−τ)+[∑iri​sin⁡ω​(xi−τ)]2∑isin2⁡ω​(xi−τ)},P(\omega)=\frac{1}{2}\left\{\frac{\left[\sum\_{i}r\_{i}\cos\omega(x\_{i}-\tau)\right]^{2}}{\sum\_{i}\cos^{2}\omega(x\_{i}-\tau)}+\frac{\left[\sum\_{i}r\_{i}\sin\omega(x\_{i}-\tau)\right]^{2}}{\sum\_{i}\sin^{2}\omega(x\_{i}-\tau)}\right\}, |  |

where τ\tau is a phase offset that ensures time-shift invariance.

We then calculate the peak power and its corresponding frequency ω∗\omega^{\ast}, and compare this value against surrogate data generated from four null models:

* •

  (i) White Gaussian noise,
* •

  (ii) AR(1) short-memory processes,
* •

  (iii) Fractional Gaussian noise (fGn) with long memory (H=0.7H=0.7),
* •

  (iv) Lévy-stable noise with heavy tails (α=1.7\alpha=1.7).

The empirical p-value is computed as:

|  |  |  |
| --- | --- | --- |
|  | p=1N​∑j=1N𝕀​(Pjsurrogate≥Preal∗),p=\frac{1}{N}\sum\_{j=1}^{N}\mathbb{I}(P\_{j}^{\text{surrogate}}\geq P^{\ast}\_{\text{real}}), |  |

where 𝕀​(⋅)\mathbb{I}(\cdot) is the indicator function and NN is the number of surrogate realizations.

### Results for Two Detected Bubbles

We applied this procedure to both of the bubble windows identified in Section LABEL:sec:lppls\_results:

1. 1.

   Bubble 1: Jan 20, 2019 – Aug 9, 2020
2. 2.

   Bubble 2: Aug 1, 2022 – May 6, 2023

In addition to the Lomb periodogram, we also applied the (H,q)(H,q)-derivative technique [[25](https://arxiv.org/html/2512.12054v1#bib.bib25)] to both intervals. This operator enhances weak log-periodic signals by computing a local difference operator over logarithmic time, defined as:

|  |  |  |
| --- | --- | --- |
|  | Dt(H,q)​[log⁡p​(t)]=log⁡p​(t)−log⁡p​(q​t)[(1−q)​t]H.D^{(H,q)}\_{t}[\log p(t)]=\frac{\log p(t)-\log p(qt)}{[(1-q)t]^{H}}. |  |

Log-periodic oscillations manifest as regular waves in a plot of Dt(H,q)​[log⁡p​(t)]D^{(H,q)}\_{t}[\log p(t)] versus log⁡(tc−t)\log(t\_{c}-t).

##### Bubble 1 (2019–2020):

The (H,q)(H,q)-derivative exhibits mild and less pronounced oscillatory behavior, indicating weaker—but present—log-periodic structure. The Lomb periodogram reveals a peak at ω≈1.28\omega\approx 1.28 with spectral power of 0.062.

To assess the statistical significance of this log-periodicity, we generated 100 surrogate time series under each null model and computed the maximum spectral power. The observed peak was found statistically significant against white noise and fractional Gaussian noise (p = 0.01 and p = 0.02, respectively), but not against AR(1) (p = 0.27) or Lévy noise (p = 0.19). These results suggest that while the log-periodic signal in this bubble is weaker, it is unlikely to result from classical uncorrelated or long-memory noise alone, though autocorrelation and heavy-tailed effects remain plausible sources.

##### Bubble 2 (2022–2023):

555In the next section, we will analyze this bubble completely.

The (H,q)(H,q)-derivative exhibits sharper and cleaner oscillatory structure, suggesting stronger log-periodicity. The Lomb periodogram reveals a high peak at ω≈1.19\omega\approx 1.19 with spectral power of 0.144.

To evaluate statistical significance, we generated 100 surrogate time series under each null model and computed the maximum spectral power. The observed peak was found statistically significant against white noise and fGn (p = 0.00 for both), but not against AR(1) (p = 0.13) or Lévy noise (p = 0.16). This supports the hypothesis that the oscillations are not random artifacts of classical or long-memory Gaussian noise, but could still emerge from more complex dynamics.

##### 

Figure [6](https://arxiv.org/html/2512.12054v1#S5.F6 "Figure 6 ‣ Results for Two Detected Bubbles ‣ 5 Analysis of the 2020 Tehran Stock Market Crash: Black Sunday ‣ Universal Dynamics of Financial Bubbles in Isolated Markets: Evidence from the Iranian Stock Market") presents the four non-parametric diagnostic plots in a two-row format. The first row shows the (H,q)(H,q)-derivative and Lomb periodogram for Bubble 1, and the second row for Bubble 2. These visualizations strengthen the LPPLS results by independently confirming the presence of log-periodic oscillations.

![Refer to caption](fig6_combined.png)


Figure 6: Non-parametric diagnostics of log-periodicity in two bubble episodes.
The first row shows the (H,q)(H,q)-derivative and Lomb periodogram for Bubble 1 (2019–2020),
while the second row presents the same diagnostics for Bubble 2 (2022–2023).
The (H,q)(H,q)-derivative detects oscillatory structure in log-space, and the Lomb periodogram reveals the spectral power
at log-periodic frequencies. Bubble 2 shows cleaner oscillations and stronger spectral peak compared to Bubble 1.

Together, these results validate our LPPLS fitting approach and confirm the existence of critical log-periodic behavior in both historical bubbles of the Tehran Stock Exchange.

## 6 Analysis of the 2023 Tehran Stock Market Bubble

### 6.1 Overview of the 2023 Bubble

In addition to the 2020 crash, the Tehran Stock Exchange experienced another significant
bubble that burst in July 2023. From its local peak, the Tehran Price Index (TEPIX) lost
approximately 23% of its value, marking one of the most substantial short-term drawdowns
in the market’s history. This section extends our analysis by applying the LPPLS model to
this recent bubble, further exploring the model’s predictive capabilities in the context of the
Tehran stock market.

### 6.2 Bubble Genesis: The “Stories” Behind the 2023 Bubble

The 2023 bubble emerged in a markedly different, yet equally turbulent, environment. Following the prolonged downturn after the 2020 collapse, investor sentiment began to shift in mid-2022, fueled by multiple “optimism triggers”: the lifting of price ceilings by the Securities and Exchange Organization (SEO), aggressive state messaging around a Tehran Stock Exchange (TSE) revival, and falling interest rates.

Combined with persistent inflation and a lack of viable investment alternatives, these developments reignited speculative behavior. Critically, the dominant “story” in this bubble centered on hopeful narratives—perceived stabilization of geopolitical tensions and a post-COVID economic recovery.

As a result, the TEDPIX index rebounded sharply in late 2022, gaining more than 50% in less than a year before culminating in a crash in May 2023. Despite improvements in market infrastructure and increased digital access, the structural fragilities of the Iranian market persisted: lack of foreign institutional capital, vulnerability to insider manipulation, and an overreliance on retail liquidity.

As with the 2020 bubble, the market once again became disconnected from economic fundamentals, demonstrating a recurring pattern of hope-driven rallies followed by abrupt corrections. In this environment, macro and policy signals appear to have coordinated investors into a self-reinforcing buying phase, aligning with the LPPLS signatures of accelerating growth and log-periodic oscillations documented for the 2023 bubble window.

### 6.3 Data Collection and Preprocessing

The data for this analysis includes Adjusted Close prices of the TEPIX from September 2022 to June 2023. Similar to the previous analysis, the data was carefully preprocessed to account for non-trading days and ensure continuity. Multiple time windows were selected to assess the model’s performance over different periods leading up to the 2023 crash.

### 6.4 LPPLS Model Fitting and Results

We now apply the same procedure used in the previous section to the 2023 Tehran Stock Market bubble. Therefore, we do not go through the detailed steps again and instead focus on presenting the results. Figure [7](https://arxiv.org/html/2512.12054v1#S6.F7 "Figure 7 ‣ 6.4 LPPLS Model Fitting and Results ‣ 6 Analysis of the 2023 Tehran Stock Market Bubble ‣ Universal Dynamics of Financial Bubbles in Isolated Markets: Evidence from the Iranian Stock Market") shows different fits of the model. Figure [8](https://arxiv.org/html/2512.12054v1#S6.F8 "Figure 8 ‣ 6.4 LPPLS Model Fitting and Results ‣ 6 Analysis of the 2023 Tehran Stock Market Bubble ‣ Universal Dynamics of Financial Bubbles in Isolated Markets: Evidence from the Iranian Stock Market") demonstrates the stability of our fitting procedure and suggests that the
approximate inception date of the 2023 bubble lies between 2022-11-01 and
2023-01-05.

Note that Plot 4 in Figure [7](https://arxiv.org/html/2512.12054v1#S6.F7 "Figure 7 ‣ 6.4 LPPLS Model Fitting and Results ‣ 6 Analysis of the 2023 Tehran Stock Market Bubble ‣ Universal Dynamics of Financial Bubbles in Isolated Markets: Evidence from the Iranian Stock Market") is one of the optimal choices based on our analysis, and the β\beta value for the optimal interval of the 2023 bubble is approximately 0.2.
In the following discussion and results, we will use this optimal β\beta value along with the corresponding optimal value detected for the 2020 crash.

![Refer to caption](2023.png)


Figure 7: Results for LPPLS Model on different time frames (2023 bubble)




Table 5: LPPLS Model Parameters for Plots 1–4 (2023 Bubble)

| Parameter | Plot 1 | Plot 2 | Plot 3 | Plot 4 |
| --- | --- | --- | --- | --- |
| AA | 16.5308 | 16.6603 | 15.6006 | 15.7300 |
| BB | -1.3889 | -1.4758 | -0.5088 | -0.5890 |
| CC | 0.0444 | 0.0369 | 0.0175 | 0.0147 |
| β\beta | 0.1 | 0.1 | 0.2 | 0.189 |
| ω\omega | 7.8421 | 8.5789 | 8.9474 | 9.11 |
| ϕ\phi | -0.5240 | 2.1154 | 0.4143 | 3.02 |
| tct\_{c} (estimated) | 2023-05-16 | 2023-05-16 | 2023-05-16 | 2023-05-22 |
| tct\_{c} (days from start) | 318.0 | 288.0 | 255.0 | 240.0 |

![Refer to caption](Grid__2_.png)


Figure 8: LPPLS window scanning and Lagrange-regularized bubble-start detection for the
2023 TSE bubble and crash.

## 7 Interpretation and Analysis

The LPPLS model parameters extracted from the 2020 and 2023 bubbles in the Iranian stock market offer a basis for interpreting the speculative dynamics of each episode in light of comparable historical crashes in global markets.

### 7.1 Growth Exponent β\beta

The critical exponent β\beta characterizes the acceleration of price growth preceding a financial crash. In the 2020 Iranian bubble, our LPPLS model estimates β≈0.45\beta\approx 0.45–0.500.50, indicating a pronounced super-exponential increase in prices. This range aligns with those observed in mature financial markets—such as the 1929 DJIA crash (β≈0.44\beta\approx 0.44) and the Nasdaq bubble of 2000 (β≈0.62\beta\approx 0.62) [[3](https://arxiv.org/html/2512.12054v1#bib.bib3), [1](https://arxiv.org/html/2512.12054v1#bib.bib1)].

By contrast, the 2023 Iranian bubble yields a significantly lower exponent of β≈0.20\beta\approx 0.20, suggesting a more gradual escalation. Although such low values are rare, they have been documented in specific episodes, including the late-1990s Amazon bubble [[22](https://arxiv.org/html/2512.12054v1#bib.bib22)] and the 2015 Chinese equity boom [[23](https://arxiv.org/html/2512.12054v1#bib.bib23)]. This divergence in β\beta values highlights the variability in bubble dynamics across different market regimes.

### 7.2 Phase Parameter ϕ\phi and Characteristic Time Scale

In the LPPLS framework, the phase parameter ϕ\phi traditionally modulates the alignment of log-periodic oscillations along the time axis. However, following the interpretation proposed by Sornette, it is more meaningful to express ϕ\phi in terms of a characteristic time scale τ\tau, defined by the transformation:

|  |  |  |
| --- | --- | --- |
|  | ϕ=−ω​log⁡τ⇒τ=e−ϕ/ω.\phi=-\omega\log\tau\quad\Rightarrow\quad\tau=e^{-\phi/\omega}. |  |

This scale τ\tau represents the relative time to the critical point tct\_{c} at which the log-periodic oscillations effectively begin. In other words, it captures the onset of herding behavior and the emergence of oscillatory precursors during the bubble’s growth phase. A smaller τ\tau indicates an earlier emergence of oscillations, whereas values of τ\tau close to 1 imply a more abrupt and explosive buildup immediately before the critical transition.

For the 2020 bubble (Plot 4), we estimate τ≈0.845\tau\approx 0.845, indicating that the log-periodic structure became prominent around 15% before the crash date. For the 2023 bubble (Plot 3), we obtain τ≈0.955\tau\approx 0.955, suggesting the oscillatory dynamics emerged much later, within just 4.5% of the time interval to the crash. These values are consistent with visual observations: the 2023 event exhibited a sharper and more compressed instability phase compared to the more gradually evolving 2020 bubble. Framing ϕ\phi in terms of τ\tau thus provides a physically interpretable and comparative measure of the temporal localization of log-periodic behavior across distinct bubbles.

### 7.3 Summary of Dynamics

The 2020 bubble represents a high-intensity, high-oscillation regime, characterized by a sharp acceleration in prices (β≈0.46\beta\approx 0.46) and a dense pattern of log-periodic oscillations (ω≈9.89\omega\approx 9.89). These features suggest a speculative boom driven by strong herding dynamics, possibly amplified by macroeconomic shocks such as currency devaluation or inflationary expectations.

By contrast, the 2023 bubble unfolded more gradually, with a lower growth exponent (β≈0.20\beta\approx 0.20) but still a pronounced log-periodic structure (ω≈8.95\omega\approx 8.95). This behavior is consistent with a slower build-up of speculative pressure, possibly reflecting a more informed or cautious investor base, or greater regulatory or informational feedback mechanisms.

Together, these cases demonstrate that financial bubbles—regardless of market maturity or geographical context—exhibit endogenous signatures that conform to the LPPLS framework. The variation in dynamic parameters between the two episodes further underscores the model’s flexibility in capturing different modes of bubble formation and collapse.

## 8 Discussion

### Universality of Bubble Dynamics in the Iranian Market

The present analysis offers compelling evidence that the Iranian stock market, despite its
economic and geopolitical isolation, exhibits speculative bubble dynamics that align closely
with those of major global financial markets. Using the Log-Periodic Power Law Singularity
(LPPLS) model, we identified two significant bubbles in the Iranian market (2020 and 2023),
with critical exponents estimated around β∈[0.45,0.50]\beta\in[0.45,0.50] and β≈0.20\beta\approx 0.20,
respectively. As summarised in Sornette’s catalogue of historical bubbles [[3](https://arxiv.org/html/2512.12054v1#bib.bib3), [1](https://arxiv.org/html/2512.12054v1#bib.bib1), [2](https://arxiv.org/html/2512.12054v1#bib.bib2)], LPPL fits of major crashes such as the 1929 DJIA episode,
the Nasdaq dot-com bubble of 2000, and the 2007 Chinese stock market bubble typically yield
β\beta values in the range 0.20.2–0.40.4 and angular log-frequencies ω\omega in the range
66–99. Our estimates for the Tehran Stock Exchange therefore lie well within, or at the
lower edge of, this empirical window.

The qualitative narratives developed in Sections 4.6 and 6.2 highlight the macroeconomic and policy environment in which the 2020 and 2023 bubbles unfolded. In 2020, renewed U.S. sanctions, currency devaluation, and state-led privatization campaigns—framed as a national wealth-building strategy—encouraged households to shift savings into equities. In 2023, a different configuration of “optimism triggers,” including relaxed price ceilings, state messaging about a market revival, and falling interest rates, again drew retail investors into the market. These episodes suggest that macro and policy shocks acted primarily as catalysts that coordinated investor expectations and amplified speculative flows. The endogenous positive-feedback mechanisms captured by the LPPLS model—herding, imitation, and reflexivity—then governed the build-up of instability and the eventual critical transition.

These findings extend existing universality tests in the LPPLS literature by adding evidence
from a politically and financially isolated market, a setting that has been largely absent from
prior empirical studies. In the context of econophysics, our results align with universal
patterns and scaling ideas discussed by Farmer, Shubik, and Smith [[9](https://arxiv.org/html/2512.12054v1#bib.bib9)],
Yakovenko and Rosser [[10](https://arxiv.org/html/2512.12054v1#bib.bib10)], and Gabaix et al. [[11](https://arxiv.org/html/2512.12054v1#bib.bib11)], showing
that endogenous feedback mechanisms and heterogeneous-agent interactions can generate
similar critical behaviors even under restricted institutional and geopolitical conditions.
This interpretation is further consistent with Bouchaud’s self-organized criticality perspective
on economic and financial systems, in which fat tails, clustered volatility, and crisis avalanches
emerge from dynamics operating near critical points [[26](https://arxiv.org/html/2512.12054v1#bib.bib26)].

Table 6: Comparison of LPPLS parameters (β\beta, ω\omega) for major historical bubbles
and the two Tehran Stock Exchange bubbles analyzed in this study. Values for non-Iranian
markets are taken from the LPPLS literature (Sornette, 2003; Filimonov & Sornette, 2013;
Zhou & Sornette, 2003).

| Market / Bubble Episode | Estimated β\beta | Estimated ω\omega |
| --- | --- | --- |
| DJIA 1929 crash | 0.33±0.050.33\pm 0.05 | 7.0±0.57.0\pm 0.5 |
| Nasdaq 2000 dot-com bubble | 0.34±0.040.34\pm 0.04 | 8.9±0.78.9\pm 0.7 |
| Shanghai Composite 2007 | 0.28±0.060.28\pm 0.06 | 8.8±0.68.8\pm 0.6 |
| Shanghai Composite 2015 | 0.21±0.040.21\pm 0.04 | 7.9±0.47.9\pm 0.4 |
| Bitcoin 2017 bubble | 0.32±0.060.32\pm 0.06 | 8.3±0.58.3\pm 0.5 |
| TSE 2020 bubble (this study) | β∈[0.45, 0.50]\beta\in[0.45,\,0.50] | 9.99.9 |
| TSE 2023 bubble (this study) | β≈0.20\beta\approx 0.20 | 8.98.9 |

Our estimated parameters for the Tehran Stock Exchange bubbles fall within the broad range
documented for well-known global bubbles such as the 1929 crash, the Nasdaq 2000 episode,
and the 2015 Chinese market correction. To illustrate this universality more explicitly,
Table [6](https://arxiv.org/html/2512.12054v1#S8.T6 "Table 6 ‣ Universality of Bubble Dynamics in the Iranian Market ‣ 8 Discussion ‣ Universal Dynamics of Financial Bubbles in Isolated Markets: Evidence from the Iranian Stock Market") compares the critical exponents β\beta and ω\omega across
several major bubble episodes. In addition, the peak-to-trough drawdowns of the TSE 2020
and 2023 crashes (approximately 42%42\% and 23%23\%, respectively) are comparable to the
30–50% losses typically reported for major historical crashes in developed and emerging
markets [[1](https://arxiv.org/html/2512.12054v1#bib.bib1)].

A broader synthesis of the ranges of β\beta, ω\omega, and crash amplitudes across the
historical bubbles catalogued by Sornette [[1](https://arxiv.org/html/2512.12054v1#bib.bib1)], together with the two TSE
episodes analyzed here, is provided in Appendix II (Table [7](https://arxiv.org/html/2512.12054v1#Ax2.T7 "Table 7 ‣ Appendix II: Universality Ranges of LPPLS Exponents and Crash Amplitudes ‣ Universal Dynamics of Financial Bubbles in Isolated Markets: Evidence from the Iranian Stock Market")).

Interestingly, the β≈0.20\beta\approx 0.20 observed in the 2023 bubble corresponds to a particularly
sharp super-exponential acceleration toward the critical point. While such low values are
relatively rare, similar results have been reported in analyses of the Amazon stock bubble of
the late 1990s [[22](https://arxiv.org/html/2512.12054v1#bib.bib22)], the Chinese stock market crash of
2015 [[23](https://arxiv.org/html/2512.12054v1#bib.bib23)], and the South African equities surge of
2003–2006 [[24](https://arxiv.org/html/2512.12054v1#bib.bib24)]. These cases demonstrate that sharply accelerating
bubbles with β\beta values near 0.2 can arise even in very different economic contexts,
reinforcing the hypothesis of universality in bubble dynamics.

This finding suggests that the dynamics of financial bubbles—characterized by accelerating prices, log-periodic oscillations, and eventual crashes—may reflect universal properties of financial markets, irrespective of their degree of openness, regulation, or integration into global capital flows. While Didier Sornette and collaborators have emphasized that the LPPLS exponent β\beta should not be interpreted as a universal constant, its clustering within a bounded range across diverse market settings underscores the presence of common underlying mechanisms666In statistical physics, a *universal critical exponent* characterizes the behavior of observables (such as magnetization, correlation length, or susceptibility) near a critical point. These exponents are called *universal* because they depend only on general features like the system’s dimensionality and symmetry—not on microscopic details. For an accessible introduction, see [[27](https://arxiv.org/html/2512.12054v1#bib.bib27), [28](https://arxiv.org/html/2512.12054v1#bib.bib28), [29](https://arxiv.org/html/2512.12054v1#bib.bib29)].. In the strict sense of statistical physics [[2](https://arxiv.org/html/2512.12054v1#bib.bib2)], the recurring appearance of β\beta in a narrow range across diverse markets supports its interpretation as a robust, emergent property of collective financial behavior.

From the standpoint of complexity science, this result aligns with theories that treat financial markets as complex adaptive systems. As Farmer, Shubik, and Smith argue [[9](https://arxiv.org/html/2512.12054v1#bib.bib9)], the search for universality in economics—akin to that in physics—rests on identifying behavioral regularities that transcend institutional specifics. Our findings echo this philosophy: the Iranian market, dominated by retail investors, limited foreign access, and heavy regulatory influence, still converges to LPPLS dynamics observed in freer, more liquid markets. This implies that endogenous dynamics, such as herding, imitation, and reflexivity, are sufficient to produce bubble-like behaviors consistent with the LPPLS framework [[1](https://arxiv.org/html/2512.12054v1#bib.bib1), [9](https://arxiv.org/html/2512.12054v1#bib.bib9)].

Additionally, the results resonate with research by Yakovenko and Rosser [[10](https://arxiv.org/html/2512.12054v1#bib.bib10)], who demonstrate that income and wealth distributions across countries follow statistical forms analogous to those in statistical mechanics. Their work emphasizes how simple aggregate behaviors can emerge from heterogeneous agents, a principle also evident in our analysis: despite microstructural differences, the Iranian market’s macro-dynamics conform to globally observed critical behaviors.

Furthermore, the power-law regularities discussed by Gabaix et al. [[11](https://arxiv.org/html/2512.12054v1#bib.bib11)] support the notion that large market movements—regardless of geography—stem from statistically regular agent behaviors, particularly the impact of large traders and institutions. Although the Iranian market lacks substantial foreign institutional participation, it still exhibits power-law-like accelerations and oscillatory corrections that LPPLS captures, reinforcing the idea that universal scaling laws can arise endogenously.

In summary, our findings contribute to the growing body of evidence suggesting that speculative bubbles obey generalizable principles. They offer a rare empirical example from an isolated emerging market to support the hypothesis that financial instabilities exhibit signatures of criticality, as predicted by theories of complex systems. These insights not only validate the LPPLS model’s applicability across market contexts but also advance our understanding of universality in economic systems.

## Acknowledgment

I gratefully acknowledge Professor Didier Sornette for deep and constructive discussions and for his thoughtful reading of the manuscript, which significantly improved this work. I also thank my colleagues at the Physics Department & Center for Complex Networks and Data Science (CCNSD), Beheshti University, for their encouragement and feedback. I am furthermore grateful to Bahram Shakerin, Ali Vahedi, Amir Kargaran, and Mohammad Osoolian for their valuable comments and discussions.

## Data availability

The data used in this study were obtained from the official website of the Tehran Stock Exchange (TSE) at <https://www.tsetmc.com>. Due to restrictions on automated data extraction and limited accessibility from outside Iran, the full cleaned dataset used in this analysis is available from the corresponding author upon reasonable request.

## Code availability

The code used for the LPPLS calibration, window optimization, and Lomb–Scargle spectral analysis is available from the corresponding author upon reasonable request.

## Competing interests

The author declares no competing interests.

## Appendix I: Robust LPPLS Calibration Algorithm (Filimonov–Sornette Method)

The LPPLS (Log-Periodic Power Law Singularity) model fitting in this study follows the robust and stable estimation scheme introduced by Filimonov and Sornette [[30](https://arxiv.org/html/2512.12054v1#bib.bib30)]. Unlike direct nonlinear least squares, this method separates the estimation of nonlinear and linear parameters, enhancing numerical stability and convergence.

### Step 1: Preprocess Data

* •

  Convert dates to numerical format with t=0t=0 at the beginning of the window.
* •

  Compute the natural logarithm of prices: log⁡Pobs​(t)\log P\_{\text{obs}}(t).

### Step 2: Define the LPPLS Model

The LPPLS equation is rewritten to separate linear and nonlinear components:

|  |  |  |
| --- | --- | --- |
|  | log⁡PLPPLS​(t)=A+B​f​(t)+C1​f​(t)​cos⁡[ω​log⁡(tc−t)]+C2​f​(t)​sin⁡[ω​log⁡(tc−t)]\log P\_{\text{LPPLS}}(t)=A+Bf(t)+C\_{1}f(t)\cos[\omega\log(t\_{c}-t)]+C\_{2}f(t)\sin[\omega\log(t\_{c}-t)] |  |

with f​(t)=(tc−t)βf(t)=(t\_{c}-t)^{\beta}, and C1=C​cos⁡ϕC\_{1}=C\cos\phi, C2=−C​sin⁡ϕC\_{2}=-C\sin\phi.

### Step 3: Grid Search over Nonlinear Parameters

We construct a dense grid over:

* •

  tc∈[tmax+10,tmax+200]t\_{c}\in[t\_{\max}+10,t\_{\max}+200]
* •

  β∈[0.1,1.0]\beta\in[0.1,1.0]
* •

  ω∈[6,13]\omega\in[6,13]

### Step 4: Linear Regression for Each Grid Point

For each grid point (tc,β,ω)(t\_{c},\beta,\omega), compute:

* •

  f​(t)=(tc−t)βf(t)=(t\_{c}-t)^{\beta}
* •

  cos⁡[ω​log⁡(tc−t)]\cos[\omega\log(t\_{c}-t)], sin⁡[ω​log⁡(tc−t)]\sin[\omega\log(t\_{c}-t)]

Then solve the linear system:

|  |  |  |
| --- | --- | --- |
|  | log⁡Pobs​(t)=X⋅θ\log P\_{\text{obs}}(t)=X\cdot\theta |  |

where XX is the design matrix:

|  |  |  |
| --- | --- | --- |
|  | X=[𝟏,f​(t),f​(t)​cos⁡[ω​log⁡(tc−t)],f​(t)​sin⁡[ω​log⁡(tc−t)]]X=\left[\mathbf{1},f(t),f(t)\cos[\omega\log(t\_{c}-t)],f(t)\sin[\omega\log(t\_{c}-t)]\right] |  |

and θ=[A,B,C1,C2]T\theta=[A,B,C\_{1},C\_{2}]^{T} is estimated using Ordinary Least Squares.

### Step 5: Select the Best Fit

* •

  Compute the RMSE for each parameter set:

  |  |  |  |
  | --- | --- | --- |
  |  | RMSE=1N​∑i(log⁡Pobs​(ti)−log⁡PLPPLS​(ti))2\text{RMSE}=\sqrt{\frac{1}{N}\sum\_{i}\left(\log P\_{\text{obs}}(t\_{i})-\log P\_{\text{LPPLS}}(t\_{i})\right)^{2}} |  |
* •

  Choose the parameter set with the lowest RMSE as the best-fit model.

### Step 6: Recover Canonical LPPLS Parameters

* •

  C=C12+C22C=\sqrt{C\_{1}^{2}+C\_{2}^{2}}
* •

  ϕ=arctan⁡2​(−C2,C1)\phi=\arctan 2(-C\_{2},C\_{1})

### Advantages of This Method

* •

  Increased robustness to noise and poor initial guesses.
* •

  Avoids instability of traditional nonlinear optimizers.
* •

  Efficient and scalable across multiple detection windows.

## Appendix II: Universality Ranges of LPPLS Exponents and Crash Amplitudes

To place the Tehran Stock Exchange bubbles in a broader empirical context, we summarize in
Table [7](https://arxiv.org/html/2512.12054v1#Ax2.T7 "Table 7 ‣ Appendix II: Universality Ranges of LPPLS Exponents and Crash Amplitudes ‣ Universal Dynamics of Financial Bubbles in Isolated Markets: Evidence from the Iranian Stock Market") the typical ranges of the LPPLS power-law exponent
β\beta (reported as m2m\_{2} in Sornette [[1](https://arxiv.org/html/2512.12054v1#bib.bib1)]), the angular log-frequency
ω\omega, and the associated peak-to-trough crash amplitudes across several groups of
historical bubbles and antibubbles. The last two rows report the corresponding values for
the 2020 and 2023 TSE episodes documented in this study.

Table 7: Summary of universality patterns across major groups of historical bubbles, as documented in Sornette (2003), together with the two Tehran Stock Exchange bubbles analyzed in this study.

| Group / Episode Set | # Episodes | Typical β\beta | Typical ω\omega | Crash (%) |
| --- | --- | --- | --- | --- |
| Major crashes (DJIA 1929, 1987, 1997, Nasdaq 2000) | ∼9\sim 9 | 0.300.30–0.600.60 | 66–99 | 3030–5050 |
| Latin-American bubbles 1990s (Argentina, Brazil, Chile, Mexico, Peru, Venezuela) | 1010 | 0.250.25–0.700.70 | 44–99 | 2020–4040 |
| 1994 Western “antibubble” + Hong Kong | 88 | 0.200.20–0.500.50 | 22–88 | 2222–3131 |
| Other developed/emerging bubbles (Sornette Tables 7.2 & 8.x) | ∼10\sim 10 | 0.300.30–0.700.70 | 55–99 | 2020–4545 |
| TSE 2020 (this study) | 11 | [0.45,0.50][0.45,0.50] | ≈9.9\approx 9.9 | ≈42\approx 42 |
| TSE 2023 (this study) | 11 | ≈0.20\approx 0.20 | ≈8.9\approx 8.9 | ≈23\approx 23 |

## References

* [1]

  Didier Sornette.
  *Why Stock Markets Crash: Critical Events in Complex Financial Systems*.
  Princeton University Press, 2003.
* [2]

  Didier Sornette.
  “Physics and financial economics (1776–2014): puzzles, Ising and agent-based models.”
  *Reports on Progress in Physics*, vol. 77, no. 6, 2014, 062001.
  DOI: 10.1088/0034-4885/77/6/062001.
* [3]

  Anders Johansen and Didier Sornette.
  “Critical crashes.”
  *Risk*, 12(1):91–94, 1999.
* [4]

  Wei-Xing Zhou and Didier Sornette.
  “Is there a real-estate bubble in the US?”
  *Physica A: Statistical Mechanics and its Applications*, 361(1), 2006, pp. 297–308.
* [5]

  Qun Zhang, Qunzhi Zhang, and Didier Sornette.
  “Early warning signals of financial crises with multi-scale quantile regressions of log-periodic power law singularities.”
  *PLOS ONE*, 11(11):e0165819, 2016. <https://doi.org/10.1371/journal.pone.0165819>
* [6]

  Didier Sornette, Ryan Woodard, and Wei-Xing Zhou.
  “The 2006–2008 Oil Bubble: evidence of speculation, and prediction.”
  *Physica A: Statistical Mechanics and its Applications*, 388(8):1571–1576, 2009.
* [7]

  Joshua Nielsen, Didier Sornette, and Maziar Raissi.
  “Deep LPPLS: Forecasting of temporal critical points in natural, engineering and financial systems.”
  *Swiss Finance Institute Research Paper No. 24-33*, 2024. Available at: <https://ssrn.com/abstract=4839066>
* [8]

  Bloomberg’s Odd Lots Podcast.
  *What’s Been Happening With the Iranian Stock Market, Nov 10, 2023*.
  Available at: <https://www.bloomberg.com/oddlots>.
* [9]

  J. Doyne Farmer, Martin Shubik, and Eric Smith.
  “Is economics the next physical science?”
  *Physics Today*, vol. 58, no. 9, 2005, pp. 37–42.
* [10]

  Victor M. Yakovenko and J. Barkley Rosser.
  “Colloquium: Statistical mechanics of money, wealth, and income.”
  *Reviews of Modern Physics*, vol. 81, no. 4, 2009, pp. 1703–1725.
* [11]

  Xavier Gabaix, Parameswaran Gopikrishnan, Vasiliki Plerou, and H. Eugene Stanley.
  “A theory of power-law distributions in financial market fluctuations.”
  *Nature*, vol. 423, no. 6937, 2003, pp. 267–270.
* [12]

  Didier Sornette and Peter Cauwels.
  “Financial bubbles: mechanisms and diagnostics.”
  *Review of Behavioral Economics*, vol. 4, no. 3, 2017, pp. 245–253.
* [13]

  Didier Sornette.
  “Econophysics Approaches to Large-Scale Business Data and Financial Crisis,”
  in *Proceedings of APFA7 (Applications of Physics in Financial Analysis)*, Misako Takayasu, Tsutomu Watanabe, and Hideki Takayasu, eds., Springer (2010), pp. 101–148.
* [14]

  Sushil Bikhchandani, David Hirshleifer, and Ivo Welch.
  “A Theory of Fads, Fashion, Custom, and Cultural Change as Informational Cascades.”
  *Journal of Political Economy*, vol. 100, no. 5, 1992, pp. 992–1026.
* [15]

  Andrea Devenow and Ivo Welch.
  “Rational Herding in Financial Economics.”
  *European Economic Review*, vol. 40, no. 3–5, 1996, pp. 603–615.
* [16]

  Abhijit V. Banerjee.
  “A Simple Model of Herd Behavior.”
  *Quarterly Journal of Economics*, vol. 107, no. 3, 1992, pp. 797–817.
* [17]

  Securities and Exchange Organization of Iran.
  “Annual Reports.”
  *Securities and Exchange Organization (SEO)*,
  <https://rdis.seo.ir/fa/category/list/22/annual-reports>,
  Accessed: 2025-03-21.
* [18]

  Guilherme Demos and Didier Sornette.
  “Comparing nested data sets and objectively determining financial bubbles’ inceptions.”
  *Physica A: Statistical Mechanics and its Applications*, vol. 524, 2019, pp. 661–675.
* [19]

  Guilherme Demos and Didier Sornette.
  “Birth or burst of financial bubbles: which one is easier to diagnose?”
  *Quantitative Finance*, vol. 17, no. 5, 2017, pp. 657–675.
* [20]

  Wei-Xing Zhou and Didier Sornette.
  “2000–2003 real estate bubble in the UK but not in the USA.”
  *Physica A: Statistical Mechanics and its Applications*, vol. 329, no. 1–2, 2003, pp. 249–263.
* [21]

  Wei-Xing Zhou and Didier Sornette.
  “Statistical Significance of Periodicity and Log-Periodicity with Heavy-Tailed Correlated Noise,”
  in *International Journal of Modern Physics C*, Vol. 13, No. 2 (2002), pp. 137–170.
  <https://arxiv.org/abs/cond-mat/0110445>
* [22]

  Ritabrata Majumder and Debabrata Das.
  “Log-periodic power law modeling of the late-1990s Amazon stock bubble.”
  *Physica A: Statistical Mechanics and its Applications*, vol. 635, 2024, 129572.
* [23]

  Wei-Xing Zhou and Didier Sornette.
  “Analysis of the 2015 Chinese stock market crash using the LPPLS model.”
  *Chaos, Solitons & Fractals*, vol. 120, 2019, pp. 189–199.
* [24]

  Wei-Xing Zhou and Didier Sornette.
  “Self-fulfilling Ising model of financial markets: Evidence from the South African stock market.”
  *Physica A: Statistical Mechanics and its Applications*, vol. 383, no. 1, 2007, pp. 115–124.
* [25]

  Wei-Xing Zhou and Didier Sornette.
  “Non-Parametric Analyses of Log-Periodic Precursors to Financial Crashes,”
  in *International Journal of Modern Physics C*, Vol. 14, No. 8 (2003), pp. 1107–1126.
  <https://arxiv.org/abs/cond-mat/0205531>
* [26]

  Jean-Philippe Bouchaud.
  “The Self-Organized Criticality Paradigm in Economics & Finance.”
  *Working paper*, Capital Fund Management and Académie des Sciences, October 25, 2025. Available as an SSRN preprint.
* [27]

  Nigel Goldenfeld.
  *Lectures on Phase Transitions and the Renormalization Group*.
  Addison-Wesley, 1992.
* [28]

  John Cardy.
  *Scaling and Renormalization in Statistical Physics*.
  Cambridge University Press, 1996.
* [29]

  H. Eugene Stanley.
  “Scaling, universality, and renormalization: Three pillars of modern critical phenomena.”
  *Reviews of Modern Physics*, vol. 71, no. 2, 1999, pp. S358–S366.
* [30]

  Vladimir Filimonov and Didier Sornette.
  “A Stable and Robust Calibration Scheme of the Log-Periodic Power Law Model.”
  *Physica A: Statistical Mechanics and its Applications*, vol. 392, no. 17, 2013, pp. 3698–3707.