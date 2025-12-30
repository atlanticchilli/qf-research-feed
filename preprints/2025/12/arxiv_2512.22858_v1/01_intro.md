---
authors:
- Abdulrahman Qadi
- Akash Sharma
- Francesca Medda
doc_id: arxiv:2512.22858v1
family_id: arxiv:2512.22858
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing
  and Portfolio Design'
url_abs: http://arxiv.org/abs/2512.22858v1
url_html: https://arxiv.org/html/2512.22858v1
venue: arXiv q-fin
version: 1
year: 2025
---


Abdulrahman Qadi\inst1, Akash Sharma\inst1, Francesca Medda\inst1
  

Abdulrahman Qadi
Institute of Finance & Technology, University College London, London, U.K., WC1E 6BT. Email: abdulrahman.qadi.24@ucl.ac.uk
  
Akash Sharma
Institute of Finance & Technology, University College London, London, U.K., WC1E 6BT. Email: akash.sharma@ucl.ac.uk
  
Francesca Medda
Institute of Finance & Technology, University College London, London, U.K., WC1E 6BT. Email: f.medda@ucl.ac.uk

###### Abstract

Binary Shariah screens vary across standards and apply hard thresholds that create discontinuous classifications. We construct a Continuous Shariah Compliance Index (CSCI) in [0,1][0,1] by mapping standard screening ratios to smooth scores between conservative “comfort” bounds and permissive outer bounds, and aggregating them conservatively with a sectoral activity factor. Using CRSP–Compustat U.S. equities (1999–2024) with lagged accounting inputs and monthly rebalancing, we find that CSCI-based long-only portfolios have historical risk-adjusted performance similar to an emulated binary Islamic benchmark. Tightening the minimum compliance threshold reduces the investable universe and diversification and is associated with lower Sharpe ratios. The framework yields a practical compliance gradient that supports portfolio construction, constraint design, and cross-standard comparisons without reliance on pass/fail screening.

Keywords: Shariah Screening; Islamic Equity Indices; Continuous Compliance Score; Ethical Screening; Portfolio Constraints; Index Construction; Asset Pricing.

## 1 Introduction

Non-pecuniary constraints are now central to portfolio choice. One prominent and long-standing example is Islamic equity investing, where portfolios must satisfy Shariah criteria on both business activities and financial structure. In practice, these criteria are implemented almost exclusively as *binary* filters: a stock either passes a set of sector and ratio tests and is deemed “Shariah-compliant”, or it fails at least one test and is excluded from the investable universe. Major index providers such as S&P Dow Jones (Dow Jones Islamic Market indices), MSCI, and FTSE Russell construct Islamic indices by applying such pass/fail rules to conventional parent universes, and Islamic equity funds typically adopt the same architecture.111See, e.g., S&P Dow Jones Indices (“Dow Jones Islamic Market Indices Methodology”), MSCI (“MSCI Islamic Index Series Methodology”), and FTSE Russell (“FTSE Shariah Global Equity Index Series Ground Rules”).

Binary screening is easy to communicate and implement, but it is an extremely coarse representation of the underlying constraints. A firm with a debt ratio of 10% and one with 29.9% are treated identically as eligible, whereas a firm with a ratio of 30.1% is treated identically to a highly levered firm with an 80% ratio, both are ineligible. Similar discontinuities arise for cash, receivables, and non-permissible income. At the same time, Shariah standards differ across boards and institutions: AAOIFI, Dow Jones Islamic (DJIM), FTSE/Yasaar, MSCI, and various national Shariah boards use closely related but distinct thresholds and denominator definitions for the same quantities.(Accounting and Auditing Organization for Islamic Financial
Institutions,, [2024](https://arxiv.org/html/2512.22858v1#bib.bib1)) As a result, the same firm can be classified as compliant in one index family and non-compliant in another, without any change in fundamentals. This fragmentation raises basic questions: how should we compare portfolios constructed under different standards, how close is a given portfolio to alternative interpretations, and what are the consequences of tightening or relaxing the constraints?

A substantial empirical literature compares Islamic and conventional indices in terms of performance, risk, and diversification, and documents that Islamic indices differ systematically in sector composition, leverage, and crisis behavior. Many studies find that Islamic indices perform at least as well as their conventional counterparts, with lower volatility and better downside protection during episodes such as the global financial crisis and the Covid-19 shock, largely attributable to balance-sheet and sector tilts.(e.g. Hakim and Rashidian,, [2004](https://arxiv.org/html/2512.22858v1#bib.bib19); Ho et al.,, [2014](https://arxiv.org/html/2512.22858v1#bib.bib23); Jawadi et al.,, [2014](https://arxiv.org/html/2512.22858v1#bib.bib25); Ben Rejeb and Arfaoui,, [2019](https://arxiv.org/html/2512.22858v1#bib.bib8); Ashraf et al.,, [2022](https://arxiv.org/html/2512.22858v1#bib.bib5); Asutay and co authors,, [2022](https://arxiv.org/html/2512.22858v1#bib.bib6)) However, the *screening layer itself* is treated as a fixed black box: a stock is either in or out, and empirical analysis proceeds conditional on that binary universe. There is no standard way to quantify “how compliant” a firm or portfolio is, to reconcile multiple Shariah standards on a common scale, or to trace out a continuous trade-off between compliance stringency, diversification, and performance.

By contrast, the ESG and ethical-investing literature almost always works with *continuous* scores. Firms receive graded measures of environmental, social, and governance quality from commercial providers or bespoke constructions, and these scores are used as characteristics in cross-sectional asset-pricing tests and as tilt variables in portfolio optimisation. Meta-analyses such as Friede et al., ([2015](https://arxiv.org/html/2512.22858v1#bib.bib16)) find that roughly 90% of more than 2,000 studies report a non-negative relation between ESG and corporate financial performance. Subsequent work shows that performance on financially *material* ESG issues is associated with higher risk-adjusted returns, while immaterial ESG signals are not rewarded, highlighting the importance of how scores are constructed.(Khan et al.,, [2016](https://arxiv.org/html/2512.22858v1#bib.bib26)) More recent studies treat ESG as a factor or preference channel in asset pricing and examine whether ESG scores and “ESG momentum” help explain the cross-section of expected returns and volatility.(e.g. Pástor et al.,, [2021](https://arxiv.org/html/2512.22858v1#bib.bib31); Pedersen et al.,, [2021](https://arxiv.org/html/2512.22858v1#bib.bib32); Andersson et al.,, [2022](https://arxiv.org/html/2512.22858v1#bib.bib4); Escobar-Saldivar et al.,, [2025](https://arxiv.org/html/2512.22858v1#bib.bib14))

We turn heterogeneous, threshold-based screens into a single continuous characteristic usable in standard asset-pricing tests. We propose a *Continuous Shariah Compliance Index* (CSCI), a firm-level measure in [0,1][0,1] that aggregates business-activity and financial-ratio information into a single index of “how compliant” a firm is, rather than a yes/no label. The construction explicitly embeds multiple leading standards. For each key ratio, leverage, cash and interest-bearing assets, receivables, and impure income, we treat the strictest thresholds used by major standards (e.g. AAOIFI’s 30% limits on riba-bearing debt and riba-earning assets and 5% impure-income limit) as a *comfort zone* and more permissive limits used by index providers (e.g. 33–33.33% debt and cash, 33% receivables or 50% cash-plus-receivables, 5% impure income in DJIM, MSCI, and FTSE/Yasaar) as *outer bounds*.(e.g. Accounting and Auditing Organization for Islamic Financial
Institutions,, [2024](https://arxiv.org/html/2512.22858v1#bib.bib1); Sandwick,, [2019](https://arxiv.org/html/2512.22858v1#bib.bib36); S&P Dow Jones Indices,, [2024](https://arxiv.org/html/2512.22858v1#bib.bib39); MSCI,, [2024](https://arxiv.org/html/2512.22858v1#bib.bib28); FTSE Russell,, [2022](https://arxiv.org/html/2512.22858v1#bib.bib17)) Firms inside the comfort zone receive a score of one on that dimension; as a ratio moves towards the outer bound the score decays smoothly to zero, and breaching the outer bound yields zero. Sector and activity screens enter via a sectoral compliance factor that equals one for clearly permissible sectors, zero for clearly prohibited sectors (e.g. conventional banking, gambling), and declines with the share of revenue from non-permissible activities up to a tolerated margin.

We aggregate components multiplicatively so a severe violation cannot be offset by strength elsewhere. At the ratio level, we use a weighted geometric mean across the financial dimensions so that a severe weakness in any one ratio meaningfully drags down the overall financial compliance score and cannot be fully offset by strengths elsewhere. At the firm level, we combine the financial score and the sectoral factor multiplicatively. Firms in non-permissible core sectors therefore receive CSCI =0=0 regardless of balance-sheet quality, while firms in permissible sectors must maintain reasonably strong financial compliance on all ratios to attain an CSCI near one. Conceptually, CSCI is designed to match the way Shariah boards and index providers talk about screening in practice: what matters is not only whether a particular threshold is breached, but also the *distance to the boundary* and the buffer available under alternative interpretations.(e.g. El-Gari,, [2004](https://arxiv.org/html/2512.22858v1#bib.bib13); Haneef et al.,, [2015](https://arxiv.org/html/2512.22858v1#bib.bib21); Hasan,, [2010](https://arxiv.org/html/2512.22858v1#bib.bib22))

We apply this framework to U.S. equities from 1999 to 2024, using a survivorship-free CRSP–Compustat panel constructed with standard linking and timing conventions. First, we document the cross-sectional and time-series distribution of CSCI across firms and sectors, and show how widely used binary standards (AAOIFI-style rules, DJIM/FTSE-style rules) map into different regions of the CSCI scale. This provides a unified lens for comparing standards: we quantify how much they differ in terms of the number of firms and market capitalisation admitted, how close admitted firms lie to their ratio limits, and how many reclassifications would occur if one standard were replaced by another.

Second, we use CSCI to construct a family of Islamic equity portfolios that vary the *intensity* of compliance. We consider portfolios that impose different minimum CSCI thresholds (e.g. portfolios holding only firms with CSCI ≥τ\geq\tau for various τ\tau) and portfolios that *tilt* weights towards high-CSCI names while maintaining a broad universe. This allows us to trace out a *frontier* between Shariah stringency, diversification, and performance. At one end of this frontier, strict CSCI thresholds produce smaller universes, lower effective numbers of holdings, and more conservative financial profiles. At the other end, lower thresholds or CSCI tilts preserve diversification while raising average compliance relative to conventional and standard Islamic benchmarks. Existing binary index rules emerge as special cases along this continuum: they correspond to particular regions of the CSCI scale rather than uniquely defining what an “Islamic portfolio” must look like.

Third, we examine the asset-pricing implications of CSCI-based screening. We compare CSCI portfolios to conventional and Islamic benchmarks in terms of average returns, volatility, Sharpe ratios, drawdowns, and exposures to common risk factors (market, size, value, profitability, investment, and momentum). We then test whether CSCI has cross-sectional explanatory power for individual stock returns after controlling for standard characteristics, asking whether the market attaches a return premium or discount to more compliant firms, or whether CSCI primarily proxies for other characteristics such as leverage or quality.

The paper makes three main contributions. First, on the measurement side, we develop a transparent and flexible Continuous Shariah Compliance Index that unifies multiple screening standards within a single continuous scoring framework, explicitly grounded in existing index rules and Shariah board thresholds. Building on recent proposals for Shariah compliance indices and degree measures in single-country settings,(e.g. Hameed and Muneeza,, [2024](https://arxiv.org/html/2512.22858v1#bib.bib20); Parlak et al.,, [2024](https://arxiv.org/html/2512.22858v1#bib.bib30); Alnamlah et al.,, [2022](https://arxiv.org/html/2512.22858v1#bib.bib3)) our CSCI extends this idea to a global, multi-standard context. Second, on the portfolio side, we provide the first systematic analysis of how continuous Shariah screening affects the investable universe, portfolio structure, and diversification, and we characterise the resulting frontier between compliance intensity and risk-adjusted performance, with existing binary indices as interior points rather than endpoints. Third, on the asset-pricing side, we link the degree of Shariah compliance to returns and factor exposures, showing how CSCI-based portfolios behave relative to conventional and Islamic benchmarks and testing whether CSCI contains incremental information about expected returns.

More broadly, our analysis reframes Shariah screening from a discrete eligibility rule into a continuous state variable that can be incorporated into portfolio design and, in subsequent work, asset-pricing and machine-learning models. This provides Islamic asset managers and index providers with a quantitative tool for specifying and communicating different levels of compliance intensity, and offers Shariah boards a way to assess how close a portfolio sits to their preferred limits under alternative interpretations. In this paper, we focus on the screening layer itself: what changes when Islamic equity investing moves from rigid binary filters to continuous, degree-based measures of Shariah compliance?

## 2 Institutional Background and Related Literature

### 2.1 Shariah screening architecture and standards

Shariah equity investing relies on a two–stage screening architecture.
First, firms whose *core* activities fall in prohibited sectors, such as
conventional financial intermediation, alcohol, gambling, adult
entertainment, or pork-related products, are excluded outright.
Second, surviving firms are subjected to quantitative financial-ratio
screens intended to bound their exposure to interest-bearing debt,
interest-based assets, liquidity risk, and non-permissible income
streams.222See, among others,
Khatkhatay and Nisar, ([2007](https://arxiv.org/html/2512.22858v1#bib.bib27)), Ayedh et al., ([2019](https://arxiv.org/html/2512.22858v1#bib.bib7)),
and Nisar, ([2015](https://arxiv.org/html/2512.22858v1#bib.bib29)) for comparative overviews.
Table [1](https://arxiv.org/html/2512.22858v1#S2.T1 "Table 1 ‣ 2.1 Shariah screening architecture and standards ‣ 2 Institutional Background and Related Literature ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") summarises the main financial-ratio thresholds used by leading standards and index providers, highlighting both their commonalities and differences as well as the source of fragmentation our CSCI measure is designed to subsume.

Table 1: Overview of Major Shariah Financial-Ratio Screens

|  | Financial-ratio thresholds | | | |
| --- | --- | --- | --- | --- |
| Standard | Interest-bearing debt | Cash & interest-bearing assets | Accounts receivable / liquidity | Impure income |
| AAOIFI | ≤30%\leq 30\% of   Market Cap | ≤30%\leq 30\% of   Market Cap | – | ≤5%\leq 5\% of   Total Income |
| DJIM (Dow Jones/S&P) | ≤33%\leq 33\% of 24-month avg Market Cap | ≤33%\leq 33\% of 24-month avg Market Cap | ≤33%\leq 33\% of   24-month avg Market Cap | ≤5%\leq 5\% of   Total Revenue |
| FTSE Islamic | ≤33.33%\leq 33.33\% of   Total Assets | ≤33.33%\leq 33.33\% of   Total Assets | ≤50%\leq 50\% of   Total Assets | ≤5%\leq 5\% of   Total Revenue |
| MSCI Islamic | ≤33.33%\leq 33.33\% of   Total Assets | ≤33.33%\leq 33.33\% of   Total Assets | ≤33.33%\leq 33.33\% of   Total Assets | ≤5%\leq 5\% of   Total Revenue |
| S&P Shariah | ≤33%\leq 33\% of 36-month avg Market Cap | ≤33%\leq 33\% of 36-month avg Market Cap | ≤49%\leq 49\% of   36-month avg Market Cap | ≤5%\leq 5\% of   Total Revenue |
| Malaysia (SC) - KLSI | ≤33%\leq 33\% of   Total Assets | ≤33%\leq 33\% of   Total Assets | – | 5% for prohibited activities; 20% for mixed activities |

*Notes*: This table summarises the main financial-ratio screening thresholds used by selected global and national Shariah standards for equities. “Debt limit” and “Cash / interest” refer to upper bounds on riba-bearing debt and on cash and interest-bearing assets, respectively. “Receivables” refers to upper bounds on accounts receivable or joint thresholds on receivables plus cash. “Impure income” refers to the share of revenue from non-permissible activities. The denominators (market capitalisation or total assets) differ across standards.

Despite a shared objective, these standards are *far from
harmonised*. AAOIFI’s Shariah Standard No. 21 sets the canonical benchmark:
interest-bearing debt and interest-bearing deposits must each not exceed
30% of the firm’s market capitalisation, and income from non-permissible
activities must remain below 5% of total income.333AAOIFI,
Shariah Standard No. 21 (Financial Papers); see the synthesis in
Ayedh et al., ([2019](https://arxiv.org/html/2512.22858v1#bib.bib7)).
AAOIFI originally also imposed a minimum share of illiquid assets,
but this liquidity constraint was removed in the subsequent Standard 59,
so the current standard contains *no* explicit receivables or
liquidity ratio.444See Ayedh et al., ([2019](https://arxiv.org/html/2512.22858v1#bib.bib7)), Table 2.

Global index providers have translated these principles into implementable
rules using different numerators, denominators, and averaging
windows. The Dow Jones Islamic Market Indices (DJIM), now operated by
S&P Dow Jones Indices, use three financial ratios, each capped at 33% of
the trailing 24-month average market capitalisation:
(i) total debt,
(ii) cash plus interest-bearing securities,
and (iii) accounts receivable.555See S&P Dow Jones Indices,
“Dow Jones Islamic Market Indices Methodology”;
summarised in Ayedh et al., ([2019](https://arxiv.org/html/2512.22858v1#bib.bib7)) and Nisar, ([2015](https://arxiv.org/html/2512.22858v1#bib.bib29)).
Non-permissible income (excluding interest) must be below 5% of total
revenue. DJIM therefore implements the “one-third” benchmark entirely in
market-value terms, smoothing price volatility via a two-year averaging
window.
FTSE Russell’s Global Equity Shariah Index Series, advised by Yasaar
Limited, instead adopts a balance-sheet-based approach. The relevant
denominator is total assets, and three ratios must satisfy:
(i) debt/total assets <33.33%<33.33\%,
(ii) cash and interest-bearing items/total assets <33.33%<33.33\%,
and (iii) cash plus accounts receivable/total assets <50%<50\%.666See
FTSE Russell, “FTSE Shariah Global Equity Index Series Ground Rules”; see
also Zakri, ([2018](https://arxiv.org/html/2512.22858v1#bib.bib41)), Table 3.
Total interest and non-compliant income may not exceed 5% of total
revenue.
Relative to DJIM, FTSE replaces market capitalisation with total assets,
and applies a more generous (50%) ceiling to the combined liquidity ratio
(cash + receivables), reflecting a different view on how strictly to
limit balance-sheet liquidity.

MSCI’s Islamic Index Series also uses total assets as the denominator, but
imposes a uniform 33.33% cap across all three ratios:
(i) total debt/total assets,
(ii) cash plus interest-bearing securities/total assets,
and (iii) accounts receivable plus cash/total assets.777MSCI,
“MSCI Islamic Index Series Methodology”; see also
Ayedh et al., ([2019](https://arxiv.org/html/2512.22858v1#bib.bib7)) and the Albilad MSCI US Equity ETF prospectus.
As with FTSE and DJIM, non-permissible income is limited to 5% of total
revenue. MSCI therefore lies between AAOIFI and FTSE: it preserves the
one-third threshold but applies it symmetrically to leverage, cash, and
receivables.
S&P’s Shariah indices sit closer to DJIM but with a longer averaging
window and a differentiated receivables cap. Leverage is restricted by
requiring total debt to be less than 33% of the 36-month average market
value of equity; cash plus interest-bearing securities must likewise be
below 33% of the same denominator, while accounts receivable face a
looser 49% cap.888See S&P Dow Jones Indices, “S&P Shariah
Indices Methodology”; see also the S&P/OIC COMCEC Shariah presentation
for a concise summary.
Again, non-permissible income (other than interest) must be below 5% of
total revenue.999See slide 5 in S&P/OIC COMCEC Emerging Shariah
Index, “S&P Shariah Methodology – Accounting Screens”.

National Shariah boards introduce further variation. The Securities
Commission Malaysia (SC) applies a two-tier business-activity screen with
benchmarks of 5% for clearly prohibited activities and 20% for broader
mixed activities,101010See Securities Commission Malaysia,
“Revised Shariah Screening Methodology for Shariah-compliant Securities”:
Zainudin et al., ([2014](https://arxiv.org/html/2512.22858v1#bib.bib40)).
and only two financial ratios: total debt/total assets and cash plus
interest-bearing securities/total assets, each capped at 33%.111111See
Ayedh et al., ([2019](https://arxiv.org/html/2512.22858v1#bib.bib7)), pp. 9–10.
There is no separate receivables or liquidity ratio in the current SC
methodology.
Empirical work shows that applying different combinations of these
screens can lead to substantial discrepancies in the set of firms
classified as Shariah-compliant, even within a single market such as
Malaysia.121212For example, Sani and Othman, ([2013](https://arxiv.org/html/2512.22858v1#bib.bib37)) document that
only around 39% of firms classified as compliant under the Kuala Lumpur
Shariah Index remain compliant when S&P/DJIM criteria are applied.

Three points matter for this paper.
First, although the numerical thresholds cluster around “one-third” and
5%, the choice of denominator (total assets vs. market value of equity,
current vs. multi-year average) and the inclusion or exclusion of
liquidity ratios produce materially different compliance universes.
Second, the lack of a unified metric makes it impossible to say whether a
firm that passes, say, FTSE but fails S&P is “more” or “less”
Shariah-compliant in any cardinal sense; compliance is treated as a set of
binary labels tied to specific standards.
Third, with very few exceptions, the literature analyses these binary
screens as exogenous filters and does not attempt to construct a
*continuous*, standard-agnostic measure of Shariah compliance that
can be compared across firms, markets, and index families.131313An
important exception is Alnamlah et al., ([2022](https://arxiv.org/html/2512.22858v1#bib.bib3)), who proposes a
multi-criteria compliance index for a single market, but does not embed
multiple global standards or study portfolio-level trade-offs.

In response, the present paper uses Table [1](https://arxiv.org/html/2512.22858v1#S2.T1 "Table 1 ‣ 2.1 Shariah screening architecture and standards ‣ 2 Institutional Background and Related Literature ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") as the
institutional foundation for a unified, Continuous Shariah Compliance Index (CSCI). The CSCI aggregates the key ratio dimensions that recur
across AAOIFI-aligned standards, DJIM, FTSE, MSCI, S&P and the SC
Malaysia into a single score in [0,1][0,1], constructed on a deliberately
*conservative* basis: for each dimension, we anchor the “fully
compliant” region at the strictest admissible threshold observed across
these standards. This design reduces the risk that a portfolio deemed
high-CSCI under our metric would subsequently be downgraded by any major
Shariah board, while allowing us to move beyond binary labels toward a
continuous, explainable measure of compliance.

### 2.2 Islamic indices: performance, risk, and governance

A substantial empirical literature compares Islamic equity indices to conventional benchmarks. Early work such as Hakim and Rashidian, ([2004](https://arxiv.org/html/2512.22858v1#bib.bib19)) and subsequent studies show that Islamic indices differ systematically in sector composition and leverage and often display similar or slightly better risk-adjusted performance. Using global and regional indices, Ho et al., ([2014](https://arxiv.org/html/2512.22858v1#bib.bib23)) find that Islamic indices generally underperform conventional benchmarks in normal periods but experience smaller losses during crises. Jawadi et al., ([2014](https://arxiv.org/html/2512.22858v1#bib.bib25)) and Ben Rejeb and Arfaoui, ([2019](https://arxiv.org/html/2512.22858v1#bib.bib8)) document that Islamic indices exhibit distinct volatility dynamics and co-movement patterns, with evidence of diversification benefits and different responses to shocks.141414See also, for example, Rana and Akhter, ([2015](https://arxiv.org/html/2512.22858v1#bib.bib33)), Ajmi et al., ([2014](https://arxiv.org/html/2512.22858v1#bib.bib2)), and Charles et al., ([2015](https://arxiv.org/html/2512.22858v1#bib.bib11)) for related evidence. More recent analyses around the global financial crisis and Covid-19 show that Shariah-compliant stocks and indices tend to have lower leverage, greater exposure to defensive sectors, and smaller drawdowns, consistent with their screening rules.(e.g. Ashraf et al.,, [2022](https://arxiv.org/html/2512.22858v1#bib.bib5); Asutay and co authors,, [2022](https://arxiv.org/html/2512.22858v1#bib.bib6); Rizwan et al.,, [2022](https://arxiv.org/html/2512.22858v1#bib.bib35))

Other studies focus on volatility, integration, and co-movement between Islamic and conventional markets. They generally find strong long-run integration but different short-run responses to shocks and crisis episodes, again reflecting structural balance-sheet and sectoral differences rather than a fundamentally distinct asset class.(e.g. Charles et al.,, [2015](https://arxiv.org/html/2512.22858v1#bib.bib11); Jawadi et al.,, [2014](https://arxiv.org/html/2512.22858v1#bib.bib25); Ben Rejeb and Arfaoui,, [2019](https://arxiv.org/html/2512.22858v1#bib.bib8)) Overall, this literature establishes that Shariah screening materially affects universe composition, leverage, sector tilts, and crisis performance.

Parallel work examines the governance, methodology, and standard-setting aspects of Shariah screening. These papers describe and compare the screening methodologies of AAOIFI, index providers, and national regulators; highlight heterogeneity in the chosen thresholds (e.g. 30% vs. 33.33% limits, assets vs. market-capitalisation denominators); and debate the extent to which widely used limits such as 30–33% debt are consistent with the underlying prohibition of *riba*.(e.g. El-Gari,, [2004](https://arxiv.org/html/2512.22858v1#bib.bib13); Hasan,, [2010](https://arxiv.org/html/2512.22858v1#bib.bib22); Rizaldy and Ahmed,, [2019](https://arxiv.org/html/2512.22858v1#bib.bib34); Haneef et al.,, [2015](https://arxiv.org/html/2512.22858v1#bib.bib21)) A recurring theme is that the screening layer is not fully harmonised across markets, that investors and managers often lack clarity on how close a portfolio is to alternative standards, and that reclassifications occur when standards or their interpretations change. This literature underscores that Shariah screens are neither immutable nor uniquely defined; they are a layer of rules sitting between raw financial statements and portfolio construction.

### 2.3 Towards continuous measures of Shariah compliance

While most Islamic equity studies treat Shariah compliance as a binary label, a small emerging literature moves towards degree-based measures. Hameed and Muneeza, ([2024](https://arxiv.org/html/2512.22858v1#bib.bib20)), for example, proposes a “Continuous Shariah Compliance Index” of listed scripts in Pakistan, folding conventional KMI screening results into a single percentage score to facilitate comparisons among firms. Related work develops Shariah convergence indices that measure the extent to which firms’ activities converge towards stricter interpretations over time and links these indices to measures of profitability and risk.(e.g. Parlak et al.,, [2024](https://arxiv.org/html/2512.22858v1#bib.bib30))

Alnamlah et al., ([2022](https://arxiv.org/html/2512.22858v1#bib.bib3)) propose a quantitative scoring model for screening Shariah-compliant firms that ranks firms according to how well they comply with Shariah criteria relative to peers. Their framework allows investors to customise the scoring according to their goals and beliefs, and they argue that it offers more information than pure threshold-based eligibility tests. Survey articles and methodological papers on Shariah screening practices highlight these proposals as important innovations that move beyond rigid thresholds and towards more nuanced measures of compliance.(e.g. Rizaldy and Ahmed,, [2019](https://arxiv.org/html/2512.22858v1#bib.bib34); Haneef et al.,, [2015](https://arxiv.org/html/2512.22858v1#bib.bib21))

However, this emerging line of research remains limited in scope. Existing degree-based measures are typically developed for a single market or index family and are tied to one specific screening standard (e.g. a national board or a single Islamic index). They focus primarily on firm-level outcomes, such as profitability, volatility, or valuation, rather than on systematic portfolio design. To our knowledge, there is no study that (i) constructs a continuous, multi-dimensional measure of Shariah compliance that explicitly embeds multiple global standards (AAOIFI, DJIM, FTSE-style methodologies); (ii) uses this measure to generate families of Islamic equity portfolios spanning different levels of compliance intensity; and (iii) analyses the resulting compliance–diversification–performance frontier and asset-pricing implications.

### 2.4 ESG and ethical investing: continuous scores and portfolio roles

In contrast to the binary treatment of Shariah compliance, the ESG and ethical-investing literature has, from the outset, treated non-pecuniary attributes as continuous scores. ESG ratings from multiple providers, or bespoke scores constructed from underlying indicators, are used as characteristics in cross-section regressions, as factors in multi-factor models, and as tilting variables in portfolio optimisation. Meta-analyses by Friede et al., ([2015](https://arxiv.org/html/2512.22858v1#bib.bib16)) and related surveys conclude that the vast majority of studies find a non-negative relation between ESG performance and financial performance, with many documenting a positive association.

Khan et al., ([2016](https://arxiv.org/html/2512.22858v1#bib.bib26)) introduce the notion of materiality by linking sustainability topics to industry-specific materiality maps and show that performance on financially material ESG issues is associated with higher future returns, while performance on immaterial issues is not. Subsequent work examines whether ESG factors are priced and whether they improve the explanation of the cross-section of expected returns. Recent studies employ high-dimensional factor models and machine-learning methods, finding that ESG and environmental factors can have explanatory power, although the evidence on whether they command a distinct risk premium is mixed.(e.g. Pástor et al.,, [2021](https://arxiv.org/html/2512.22858v1#bib.bib31); Pedersen et al.,, [2021](https://arxiv.org/html/2512.22858v1#bib.bib32); Andersson et al.,, [2022](https://arxiv.org/html/2512.22858v1#bib.bib4))

A parallel strand looks at ESG momentum and dynamics. Papers such as Escobar-Saldivar et al., ([2025](https://arxiv.org/html/2512.22858v1#bib.bib14)) show that changes in ESG scores are related to both returns and volatility and that ESG momentum can be associated with outperformance or lower risk. At the portfolio level, many studies analyse the trade-off between ESG intensity, tracking error, and performance, often finding that high-ESG portfolios have somewhat lower expected returns but also lower risk, or that ESG integration yields risk-adjusted performance comparable to conventional benchmarks.(e.g. Gibson Brandon et al.,, [2019](https://arxiv.org/html/2512.22858v1#bib.bib18); Berk and van Binsbergen,, [2021](https://arxiv.org/html/2512.22858v1#bib.bib10))

Three methodological features of this literature are relevant for Islamic finance. First, ESG attributes are measured on continuous scales, allowing flexible transformations, weighting schemes, and aggregation across dimensions. Second, these continuous measures are integrated into both portfolio construction and asset-pricing models, providing a natural way to trace out frontiers between ethical intensity and financial metrics. Third, the literature explicitly recognises heterogeneity across rating providers and the possibility of “ESG disagreement” and studies how such heterogeneity affects asset pricing and trading, parallels that resonate with the multiplicity of Shariah standards.(e.g. Berg et al.,, [2022](https://arxiv.org/html/2512.22858v1#bib.bib9); Christensen et al.,, [2022](https://arxiv.org/html/2512.22858v1#bib.bib12))

### 2.5 Gap and contribution

Taken together, the Islamic index and ESG literatures suggest that non-pecuniary constraints matter for portfolio characteristics and risk and that continuous measures of those constraints can be fruitfully integrated into asset-pricing analysis. Yet they differ sharply in how the underlying attributes are modelled. Islamic equity studies almost always start from a Shariah-compliant universe defined by binary rules and then analyse performance, risk, or integration relative to conventional benchmarks. ESG studies, by contrast, start from continuous scores and use those scores directly as inputs into portfolio design and return prediction.

The small but growing body of work on Continuous Shariah Compliance Index and convergence indices demonstrates that compliance can be treated as a continuous characteristic and that more compliant firms often differ systematically in risk and profitability.(e.g. Hameed and Muneeza,, [2024](https://arxiv.org/html/2512.22858v1#bib.bib20); Parlak et al.,, [2024](https://arxiv.org/html/2512.22858v1#bib.bib30); Alnamlah et al.,, [2022](https://arxiv.org/html/2512.22858v1#bib.bib3)) However, this work is generally tied to a single national standard or index methodology, focuses on firm-level outcomes rather than systematic portfolio design, and does not seek to reconcile multiple global standards within a unified scale.

To our knowledge, there is no paper that constructs a unified, continuous measure of Shariah compliance that: (i) explicitly embeds multiple global standards (AAOIFI, DJIM, FTSE-style and related methodologies) within a common measurement framework; (ii) uses this measure to design families of Islamic equity portfolios with varying compliance intensity, thereby tracing out a compliance–diversification–performance frontier in a manner analogous to ESG intensity frontiers; and (iii) analyses the asset-pricing implications of the resulting portfolios, including factor exposures and the cross-sectional relation between degrees of Shariah compliance and expected returns. This is the gap the present paper addresses.

## 3 Data and Measurement

### 3.1 Sample and data sources

The empirical analysis uses U.S. common stocks from January 1999 to December 2024. Price and return data are obtained from the CRSP monthly stock file (CRSP MSF), and accounting information from Compustat North America (annual industrial and commercial format), both accessed via WRDS. We link CRSP and Compustat using the standard CRSP–Compustat merged (CCM) link table.

We focus on ordinary common shares listed on the NYSE, AMEX, and NASDAQ. Following standard practice, we retain securities with CRSP share codes 10 or 11 and exchange codes 1, 2, or 3. For each stock-month, we use the CRSP month-end closing price (PRC), total return (RET), shares outstanding (SHROUT), and include delisting returns from the CRSP delisting file to compute total returns at delisting. Market capitalisation is defined as the absolute price times shares outstanding. We exclude observations with missing price or return data.

Accounting data are taken from Compustat’s annual fundamental file (FUNDA) for industrial firms (INDFMT = ‘INDL’) reporting consolidated, domestic, standard-format financial statements (CONSOL = ‘C’, POPSRC = ‘D’, DATAFMT = ‘STD’). We keep observations with fiscal year-ends between 1998 and 2024, which allows us to form lagged accounting variables for returns from 1999 onwards. For each firm-year identified by Compustat’s GVKEY and fiscal year-end DATADATE, we extract the balance-sheet and income-statement items needed to construct Shariah-relevant ratios: total assets, total debt, cash and interest-bearing assets, accounts receivable, and revenue and income components used to approximate non-permissible income.

Table [2](https://arxiv.org/html/2512.22858v1#S3.T2 "Table 2 ‣ 3.1 Sample and data sources ‣ 3 Data and Measurement ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") reports basic sample characteristics by sub-period.

Table 2: Sample Description and Coverage

| Sub-period | Avg. # stocks | Avg. # firm-years | Median market cap ($bn) | Mean leverage (%) |
| --- | --- | --- | --- | --- |
| 1999–2004 | 3989 | 4680 | 0.12 | 21.7 |
| 2005–2009 | 2820 | 3093 | 0.21 | 19.9 |
| 2010–2014 | 1832 | 2007 | 0.30 | 19.9 |
| 2015–2019 | 1212 | 1365 | 0.37 | 24.5 |
| 2020–2024 | 438 | 559 | 0.30 | 29.2 |

*Notes*: This table reports summary statistics for the CRSP–Compustat sample by sub-period. “Avg. # stocks” is the average number of common shares (CRSP share codes 10 and 11 on NYSE/AMEX/NASDAQ) with non-missing returns in each month. “Avg. # firm-years” is the average number of Compustat firm-year observations per sub-period that can be linked to CRSP. “Median market cap” is the time-series average of the cross-sectional median market capitalisation. “Mean leverage” is the time-series average of the cross-sectional mean debt-to-market-capitalisation ratio (defined in Section [3.3](https://arxiv.org/html/2512.22858v1#S3.SS3 "3.3 Construction of Shariah ratios ‣ 3 Data and Measurement ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design")).

### 3.2 CRSP–Compustat link and timing

We link firms across CRSP and Compustat using the CRSP–Compustat merged link table (CCMXPF\_LINKTABLE), which maps Compustat firm identifiers (GVKEY) to CRSP permanent identifiers (PERMNO) over time. We retain link types that correspond to standard equity issues (LINKTYPE ∈{LU, LC, LS, LD, LN, LX}\in\{\text{LU, LC, LS, LD, LN, LX}\}) and primary links (LINKPRIM ∈{P, C}\in\{\text{P, C}\}), and require that the Compustat fiscal year-end DATADATE lies within the effective link interval (LINKDT ≤\leq DATADATE ≤\leq LINKENDDT or until the end of the sample if LINKENDDT is missing).151515See, e.g., Fama and French, ([1992](https://arxiv.org/html/2512.22858v1#bib.bib15)) and Hou et al., ([2015](https://arxiv.org/html/2512.22858v1#bib.bib24)) for similar link and timing conventions.

A crucial aspect of the design is the timing of accounting information. To avoid look-ahead bias, we do not allow investors in month tt to use fiscal-year data that would not yet have been publicly available. Following standard practice in the asset-pricing literature, we assume that annual financial statements become investable with a lag of six months after the fiscal year-end.(e.g. Fama and French,, [1992](https://arxiv.org/html/2512.22858v1#bib.bib15); Hou et al.,, [2015](https://arxiv.org/html/2512.22858v1#bib.bib24)) For each firm-year, we define an availability date as DATADATE plus six calendar months. The corresponding accounting variables are matched to CRSP monthly observations from the first month after this availability date until the earlier of (i) the next fiscal year’s availability date or (ii) the stock’s delisting.

This procedure ensures that, at each month, a firm’s Shariah-relevant ratios are computed only from accounting information that would have been available to an investor at that time. It also preserves firms that later delist or fail: they remain in the sample for all months in which they were listed and had available information, and their final month’s return includes the CRSP delisting return. The resulting CRSP–Compustat panel is therefore survivorship-free and free of look-ahead with respect to accounting data.

Figure [1](https://arxiv.org/html/2512.22858v1#S3.F1 "Figure 1 ‣ 3.2 CRSP–Compustat link and timing ‣ 3 Data and Measurement ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") illustrates the timing convention with a simple timeline.

![Refer to caption](x1.png)

Figure 1: Timeline of accounting data availability and portfolio formation.

*Notes*: Annual financial statements for fiscal year tt
are assumed to become available with a six-month lag. CSCI ratios constructed
from those statements are used for portfolio formation and holding from
month t+7t+7 to t+18t+18, until the next fiscal year’s accounts are released.

### 3.3 Construction of Shariah ratios

For each firm-year, we construct four Shariah-relevant financial ratios that capture the dimensions emphasised by leading standards (AAOIFI, DJIM, FTSE, MSCI): leverage, cash and interest-bearing assets, accounts receivable, and non-permissible income. These ratios are designed to be compatible with both market-capitalisation-based and asset-based thresholds used in practice.

#### Leverage ratio.

We define total interest-bearing debt as the sum of long-term debt and debt in current liabilities,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Debti,t=DLTTi,t+DLCi,t,\text{Debt}\_{i,t}=\text{DLTT}\_{i,t}+\text{DLC}\_{i,t}, |  | (1) |

and scale it by market capitalisation at the fiscal year-end or by total assets, depending on the specification. Our baseline leverage ratio is

|  |  |  |  |
| --- | --- | --- | --- |
|  | LEVi,t=Debti,tMEi,t,\text{LEV}\_{i,t}=\frac{\text{Debt}\_{i,t}}{\text{ME}\_{i,t}}, |  | (2) |

where MEi,t\text{ME}\_{i,t} is the firm’s market capitalisation at DATADATE, following the market-cap approach used by AAOIFI and DJIM screens. As a robustness check, we also consider an asset-based version Debti,t/ATi,t\text{Debt}\_{i,t}/\text{AT}\_{i,t}, where AT is total assets, closer to the FTSE/Yasaar methodology.

#### Cash and interest-bearing assets.

We proxy cash and interest-bearing assets by cash and equivalents plus short-term investments and other interest-bearing securities,

|  |  |  |  |
| --- | --- | --- | --- |
|  | CashInti,t=CHEi,t+IVAOi,t+IVSTi,t,\text{CashInt}\_{i,t}=\text{CHE}\_{i,t}+\text{IVAO}\_{i,t}+\text{IVST}\_{i,t}, |  | (3) |

and define

|  |  |  |  |
| --- | --- | --- | --- |
|  | CASHRi,t=CashInti,tMEi,t,\text{CASHR}\_{i,t}=\frac{\text{CashInt}\_{i,t}}{\text{ME}\_{i,t}}, |  | (4) |

again with an asset-based version CashInti,t/ATi,t\text{CashInt}\_{i,t}/\text{AT}\_{i,t} used in robustness checks. These choices mirror the items used in index-provider implementations of “cash and interest-bearing” screens.

#### Receivables ratio.

We measure accounts receivable using Compustat’s RECT and define

|  |  |  |  |
| --- | --- | --- | --- |
|  | RECi,t=RECTi,tMEi,t,\text{REC}\_{i,t}=\frac{\text{RECT}\_{i,t}}{\text{ME}\_{i,t}}, |  | (5) |

with an alternative RECTi,t/ATi,t\text{RECT}\_{i,t}/\text{AT}\_{i,t}. DJIM and MSCI apply receivables thresholds relative to market capitalisation, typically at 33%, while FTSE/Yasaar impose a combined receivables-plus-cash limit; our construction allows us to emulate both.

#### Denominators, mechanical price sensitivity, and interpretation.

Our baseline ratios scale balance-sheet items by market capitalisation at the fiscal year-end (e.g., L​E​Vi,t=D​e​b​ti,t/M​Ei,tLEV\_{i,t}=Debt\_{i,t}/ME\_{i,t}, C​A​S​H​Ri,t=C​a​s​h​I​n​ti,t/M​Ei,tCASHR\_{i,t}=CashInt\_{i,t}/ME\_{i,t}, and R​E​Ci,t=R​E​C​Ti,t/M​Ei,tREC\_{i,t}=RECT\_{i,t}/ME\_{i,t}), reflecting the market-cap denominator used in several major screening standards and index implementations. A mechanical implication of market-based denominators is sensitivity to equity valuations: holding accounting numerators fixed, increases in M​Ei,tME\_{i,t} mechanically reduce these ratios,

|  |  |  |
| --- | --- | --- |
|  | ∂∂M​E​(XM​E)=−XM​E2<0,\frac{\partial}{\partial ME}\left(\frac{X}{ME}\right)=-\frac{X}{ME^{2}}<0, |  |

so a rise in market value can increase implied compliance even if the underlying balance sheet is unchanged. This feature is not unique to CSCI; it follows directly from the denominator choice embedded in existing standards. The appropriate interpretation is therefore that CSCI under market-cap denominators reflects both accounting fundamentals and their valuation scaling.

Two aspects of the empirical design mitigate (but do not eliminate) concerns about contemporaneous information or look-ahead. First, all accounting inputs are lagged using the six-month reporting-delay convention described in Section 3.2. Second, ratios are constructed at the firm-year level and carried forward to monthly observations within the availability window. Because denominator choice is itself substantive, we also consider asset-scaled variants (e.g., D​e​b​t/A​TDebt/AT, C​a​s​h​I​n​t/A​TCashInt/AT, R​E​C​T/A​TRECT/AT) as a diagnostic for whether results are driven primarily by market-value scaling versus underlying balance-sheet structure.

#### Impure income ratio.

Non-permissible income (e.g. interest income, gambling-related revenues) is not directly observed in a single Compustat item. We therefore follow the Islamic index-methodology literature and approximate impure income as the share of revenue derived from interest and other non-operating sources.(e.g. Sandwick,, [2019](https://arxiv.org/html/2512.22858v1#bib.bib36); Rizaldy and Ahmed,, [2019](https://arxiv.org/html/2512.22858v1#bib.bib34)) Concretely, we identify interest income and similar items in Compustat’s income-statement fields and define

|  |  |  |  |
| --- | --- | --- | --- |
|  | IMPUREi,t=ImpureIncomei,tSALEi,t,\text{IMPURE}\_{i,t}=\frac{\text{ImpureIncome}\_{i,t}}{\text{SALE}\_{i,t}}, |  | (6) |

where SALE denotes net sales or total revenue. This ratio is intended to be comparable to the 5% impure-income thresholds used in AAOIFI and FTSE/Yasaar guidelines.

For each of these four dimensions, we cap ratios at reasonable maxima (e.g. 200%) to reduce the impact of extreme outliers and winsorise at the 1st and 99th percentiles. All ratio variables are constructed at the firm-year level and then carried forward to monthly observations using the timing convention described in Section [3](https://arxiv.org/html/2512.22858v1#S3 "3 Data and Measurement ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design"). Table [3](https://arxiv.org/html/2512.22858v1#S3.T3 "Table 3 ‣ Impure income ratio. ‣ 3.3 Construction of Shariah ratios ‣ 3 Data and Measurement ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") summarises the variable definitions.

Table 3: Variable Definitions for Shariah Ratios

| Ratio | Definition | Compustat items |
| --- | --- | --- |
| LEV | Debti,t/MEi,t\text{Debt}\_{i,t}/\text{ME}\_{i,t} | DLTT + DLC; ME from CRSP |
| CASHR | CashInti,t/MEi,t\text{CashInt}\_{i,t}/\text{ME}\_{i,t} | CHE + IVAO + IVST; ME from CRSP |
| REC | RECTi,t/MEi,t\text{RECT}\_{i,t}/\text{ME}\_{i,t} | RECT; ME from CRSP |
| IMPURE | ImpureIncomei,t/SALEi,t\text{ImpureIncome}\_{i,t}/\text{SALE}\_{i,t} | Interest & non-operating income; SALE |

*Notes*: This table defines the four financial ratios used in the construction of the Continuous Shariah Compliance Index (CSCI). All ratios are computed annually at the firm-year level and then matched to monthly return observations with a six-month lag after the fiscal year-end. Asset-based versions (e.g. ratios scaled by total assets AT) are used in robustness checks.

### 3.4 Sector classification and business-activity screens

Business-activity screening requires an approximation to firms’ sectoral and revenue composition. We classify firms into sectors using CRSP/Compustat industry codes (SIC and, where available, NAICS) and map these codes to Shariah-permissible and non-permissible categories. Consistent with index-provider methodologies and Shariah board guidelines, we treat conventional banking and insurance, gambling, alcohol, tobacco, pork production, and adult entertainment as core non-permissible sectors.(e.g. Accounting and Auditing Organization for Islamic Financial
Institutions,, [2024](https://arxiv.org/html/2512.22858v1#bib.bib1); Securities Commission Malaysia,, [2013](https://arxiv.org/html/2512.22858v1#bib.bib38); S&P Dow Jones Indices,, [2024](https://arxiv.org/html/2512.22858v1#bib.bib39)) Firms whose primary SIC/NAICS codes fall in these sectors are assigned a sectoral compliance factor of zero and thus receive CSCI =0=0 regardless of their financial ratios.

For sectors that are potentially mixed, for example, diversified consumer services, media, and certain conglomerates, we allow for partial compliance. Where segment-level revenue data are available, we estimate the share of revenues from non-permissible activities and compare it to a 5% tolerance threshold. Firms with non-permissible revenues below 5% are treated as sectorally compliant; firms with shares above this level receive a sectoral compliance factor that declines with the non-permissible revenue share and hits zero when non-permissible revenues become dominant.

The resulting sectoral compliance factor is a variable in [0,1][0,1] that captures the permissibility of a firm’s core business. In the next section, we combine this factor with the financial ratios defined above to construct a firm-level Continuous Shariah Compliance Index (CSCI).

## 4 Continuous Shariah Compliance Index (CSCI): Definition and Properties

This section formalises the Continuous Shariah Compliance Index (CSCI), our firm-level measure of Shariah compliance.
The guiding principles are:

1. 1.

   Compliance is assessed along the same dimensions that appear in
   leading standards, leverage, cash and interest-bearing assets,
   receivables/liquidity, and impure income, and via a sectoral
   screen on business activities (Section [2.1](https://arxiv.org/html/2512.22858v1#S2.SS1 "2.1 Shariah screening architecture and standards ‣ 2 Institutional Background and Related Literature ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design")).
2. 2.

   For each dimension, we distinguish between a *comfort
   zone*, where a firm is well inside the strictest thresholds in
   Table [1](https://arxiv.org/html/2512.22858v1#S2.T1 "Table 1 ‣ 2.1 Shariah screening architecture and standards ‣ 2 Institutional Background and Related Literature ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design"), and an *outer bound*, corresponding
   to the most permissive threshold used by any major standard.
3. 3.

   Scores are monotone and conservative: they take the value
   one in the comfort zone, decline smoothly as a ratio approaches
   the outer bound, and hit zero once the outer bound is breached.
4. 4.

   The aggregate CSCI is multiplicative: a serious weakness in any
   dimension significantly lowers the overall compliance score and
   cannot be fully offset by strengths elsewhere.

Box 1: What CSCI Is (and Is Not).
  
CSCI is a measurement and portfolio-design tool.
It provides a continuous, standards-anchored mapping of widely used Shariah screening dimensions—leverage, cash and interest-bearing assets, receivables/liquidity, impure income, and business-activity exposure—into a cardinal score in [0,1][0,1] that can be used in portfolio construction and empirical asset-pricing exercises.
  
CSCI is not a theological ruling.
We do not claim that CSCI replaces Shariah boards, fatwas, or index-provider governance. The purpose is to translate the ratio architecture already used in practice into a smooth characteristic that avoids pass/fail discontinuities and enables transparent trade-offs in portfolio design.
  
CSCI is not guaranteed to match proprietary index-provider membership.
Index providers often apply implementation details that are not fully observable in public data (e.g., revenue classification rules, treatment of special items, or proprietary sector mappings). Our empirical implementation therefore produces an *emulated* screening framework using CRSP/Compustat fields and standard timing conventions; where provider membership is available, it can be used for external validation.
  
CSCI is deliberately conservative by construction.
Dimension scores take value one within a strict “comfort” region and decline smoothly toward zero as ratios approach the most permissive bounds used across major standards; the aggregate is multiplicative so that a severe violation in any dimension materially reduces overall compliance and cannot be fully offset elsewhere.
  
CSCI is not presented as an “alpha signal.”
In return tests, CSCI should be interpreted primarily as a constraint/attribute that re-arranges portfolio composition and exposures. Whether it commands a distinct premium after controlling for standard characteristics is an empirical question rather than an assumption.

We implement these principles by first mapping each ratio and the
sectoral screen into dimension-specific scores in [0,1][0,1], and then
aggregating them into a firm-level CSCI.

### 4.1 Ratio-level compliance scores

Let ii index firms and tt index fiscal years.
For each firm-year (i,t)(i,t), let
Ri,tkR^{k}\_{i,t} denote one of the four financial ratios defined in
Section [3.3](https://arxiv.org/html/2512.22858v1#S3.SS3 "3.3 Construction of Shariah ratios ‣ 3 Data and Measurement ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design"), where k∈{debt,cash,rec,impure}k\in\{\text{debt},\text{cash},\text{rec},\text{impure}\} stands for leverage, cash and
interest-bearing assets, receivables/liquidity, and impure income
respectively.
We map each ratio into a compliance score ci,tk∈[0,1]c^{k}\_{i,t}\in[0,1] via a
piecewise function with two economically meaningful thresholds.

For each dimension kk, we choose a *comfort threshold*
θ¯k\underline{\theta}\_{k} and an *outer threshold* θ¯k\overline{\theta}\_{k}
with 0≤θ¯k<θ¯k0\leq\underline{\theta}\_{k}<\overline{\theta}\_{k}.
In the empirical implementation, θ¯k\underline{\theta}\_{k} is set equal to
the most conservative (lowest) admissible bound among the standards in
Table [1](https://arxiv.org/html/2512.22858v1#S2.T1 "Table 1 ‣ 2.1 Shariah screening architecture and standards ‣ 2 Institutional Background and Related Literature ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design"), while θ¯k\overline{\theta}\_{k} corresponds to the
most permissive (highest) bound.161616For example, for the
debt ratio we use a comfort threshold of 30%, reflecting AAOIFI’s
standard, and an outer threshold of 33–33.33%, reflecting the
one-third limits used by global index providers. For the combined
liquidity ratio, the comfort threshold is set at 33–33.33% in line
with DJIM and MSCI, while the outer threshold is 50%, matching
FTSE’s cash-plus-receivables screen. For impure income, the outer
threshold is 5% across all standards; we set the comfort threshold
strictly below this, so that even within the 0–5% band the score
declines in a way that rewards cleaner income streams. Full numerical
values and robustness checks are reported in the Online Appendix.

Given (θ¯k,θ¯k)(\underline{\theta}\_{k},\overline{\theta}\_{k}), we define the
ratio-level compliance score as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ci,tk={1,if ​Ri,tk≤θ¯k,(θ¯k−Ri,tkθ¯k−θ¯k)γk,if ​θ¯k<Ri,tk<θ¯k,0,if ​Ri,tk≥θ¯k,c^{k}\_{i,t}=\begin{cases}1,&\text{if }R^{k}\_{i,t}\leq\underline{\theta}\_{k},\\[3.99994pt] \biggl(\dfrac{\overline{\theta}\_{k}-R^{k}\_{i,t}}{\overline{\theta}\_{k}-\underline{\theta}\_{k}}\biggr)^{\gamma\_{k}},&\text{if }\underline{\theta}\_{k}<R^{k}\_{i,t}<\overline{\theta}\_{k},\\[8.99994pt] 0,&\text{if }R^{k}\_{i,t}\geq\overline{\theta}\_{k},\end{cases} |  | (7) |

where γk≥1\gamma\_{k}\geq 1 is a shape parameter.
When γk=1\gamma\_{k}=1, the score declines linearly from one at the comfort
threshold to zero at the outer threshold; γk>1\gamma\_{k}>1 produces a
more convex profile in which the score remains close to one near the
comfort threshold but falls sharply as the ratio approaches the outer
bound.
In our baseline specification we set γk=2\gamma\_{k}=2 for all kk, which
yields a conservative penalisation of firms that sit near the edges of
the admissible region.

The mapping in ([7](https://arxiv.org/html/2512.22858v1#S4.E7 "In 4.1 Ratio-level compliance scores ‣ 4 Continuous Shariah Compliance Index (CSCI): Definition and Properties ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design")) has several properties that are useful
for both Shariah governance and empirical work.
First, ci,tkc^{k}\_{i,t} is monotone decreasing in Ri,tkR^{k}\_{i,t}:
higher leverage, larger interest-bearing cash holdings,
a higher share of receivables, or more impure income can only reduce,
never increase, the compliance score on that dimension.
Second, the score is normalised: any firm that satisfies the
comfort threshold receives ci,tk=1c^{k}\_{i,t}=1, while any firm that
breaches the outer threshold receives ci,tk=0c^{k}\_{i,t}=0.
Third, because the mapping is continuous on
(θ¯k,θ¯k)(\underline{\theta}\_{k},\overline{\theta}\_{k}), small changes in ratios
near the boundaries translate into smooth changes in scores,
facilitating the use of CSCI in portfolio optimisation and cross-sectional
regressions.

### 4.2 Sectoral compliance factor

Financial ratios alone are not sufficient for Shariah compliance; firms
engaged in prohibited core activities must be excluded regardless of
their balance-sheet structure.
We therefore construct a sectoral compliance factor bi,t∈[0,1]b\_{i,t}\in[0,1]
based on the business-activity screens discussed in
Section [2.1](https://arxiv.org/html/2512.22858v1#S2.SS1 "2.1 Shariah screening architecture and standards ‣ 2 Institutional Background and Related Literature ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design").

Let qi,t∈[0,1]q\_{i,t}\in[0,1] denote the estimated share of firm ii’s revenue
at time tt that derives from non-permissible activities.
For firms whose primary SIC/NAICS codes fall in clearly prohibited
sectors (conventional banking and insurance, gambling, alcohol, adult
entertainment, pork, and closely related activities) we set qi,t=1q\_{i,t}=1
by construction.
For firms in clearly permissible sectors (e.g. basic manufacturing,
technology, healthcare) we set qi,t=0q\_{i,t}=0 unless segment data suggest
otherwise.
For mixed sectors (e.g. diversified consumer services, hotels, certain
media), we approximate qi,tq\_{i,t} using segment-level revenue data when
available, or proxy measures such as the shares disclosed in index
providers’ sector classifications.

We map qi,tq\_{i,t} into a sectoral compliance factor using two income
benchmarks that mirror practice in the standards.
We take a lower tolerance ϕ¯\underline{\phi}, equal to 5%, and an upper
tolerance ϕ¯\overline{\phi}, equal to 20%, reflecting the dual
thresholds used by the Securities Commission Malaysia for strictly
prohibited versus mixed activities.
The sectoral factor is then

|  |  |  |  |
| --- | --- | --- | --- |
|  | bi,t={1,if ​qi,t≤ϕ¯,(ϕ¯−qi,tϕ¯−ϕ¯)δ,if ​ϕ¯<qi,t<ϕ¯,0,if ​qi,t≥ϕ¯,b\_{i,t}=\begin{cases}1,&\text{if }q\_{i,t}\leq\underline{\phi},\\[3.99994pt] \biggl(\dfrac{\overline{\phi}-q\_{i,t}}{\overline{\phi}-\underline{\phi}}\biggr)^{\delta},&\text{if }\underline{\phi}<q\_{i,t}<\overline{\phi},\\[8.99994pt] 0,&\text{if }q\_{i,t}\geq\overline{\phi},\end{cases} |  | (8) |

with shape parameter δ≥1\delta\geq 1.
Thus firms with non-permissible income below 5% are treated as fully
sectorally compliant (bi,t=1b\_{i,t}=1), firms for which non-permissible
income dominates (above 20%) receive bi,t=0b\_{i,t}=0, and firms in
between are penalised smoothly.

The specific values of (ϕ¯,ϕ¯)(\underline{\phi},\overline{\phi}) can be
adjusted to reflect alternative Shariah board preferences: a more
conservative board may set ϕ¯=5%\overline{\phi}=5\%, collapsing the middle
region and treating any non-trivial non-permissible revenue as fully
non-compliant, while a more permissive interpretation might tolerate
higher values before bi,tb\_{i,t} hits zero.
The functional form in ([8](https://arxiv.org/html/2512.22858v1#S4.E8 "In 4.2 Sectoral compliance factor ‣ 4 Continuous Shariah Compliance Index (CSCI): Definition and Properties ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design")) is therefore flexible enough to
accommodate multiple interpretations while maintaining a consistent
[0,1][0,1] scale.

### 4.3 Aggregation to a firm-level CSCI

The firm-level Continuous Shariah Compliance Index combines the four ratio-level
scores and the sectoral factor into a single index.
Let
𝐜i,t=(ci,tdebt,ci,tcash,ci,trec,ci,timpure)\mathbf{c}\_{i,t}=\left(c^{\text{debt}}\_{i,t},c^{\text{cash}}\_{i,t},c^{\text{rec}}\_{i,t},c^{\text{impure}}\_{i,t}\right)
denote the vector of financial compliance scores, and let
𝐰=(wdebt,wcash,wrec,wimpure)\mathbf{w}=(w\_{\text{debt}},w\_{\text{cash}},w\_{\text{rec}},w\_{\text{impure}}) be non-negative weights that sum to
one.
We define the financial-compliance component as a weighted geometric
mean:

|  |  |  |  |
| --- | --- | --- | --- |
|  | fi,t=∏k∈{debt,cash,rec,impure}(ci,tk)wk.f\_{i,t}=\prod\_{k\in\{\text{debt},\text{cash},\text{rec},\text{impure}\}}\left(c^{k}\_{i,t}\right)^{w\_{k}}. |  | (9) |

In the baseline specification we use equal weights
wk=1/4w\_{k}=1/4.
If a particular ratio is missing for firm ii in year tt, we
re-normalise the weights across the remaining dimensions.171717For
example, if receivables data are missing for a firm-year, we set
fi,t=(ci,tdebt)1/3​(ci,tcash)1/3​(ci,timpure)1/3f\_{i,t}=\left(c^{\text{debt}}\_{i,t}\right)^{1/3}\left(c^{\text{cash}}\_{i,t}\right)^{1/3}\left(c^{\text{impure}}\_{i,t}\right)^{1/3}.

The geometric mean in ([9](https://arxiv.org/html/2512.22858v1#S4.E9 "In 4.3 Aggregation to a firm-level CSCI ‣ 4 Continuous Shariah Compliance Index (CSCI): Definition and Properties ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design")) has two attractive
features.
First, it preserves the unit interval: fi,t∈[0,1]f\_{i,t}\in[0,1], with
fi,t=1f\_{i,t}=1 if and only if all ci,tk=1c^{k}\_{i,t}=1, and fi,t=0f\_{i,t}=0 if any
ci,tk=0c^{k}\_{i,t}=0.
Second, it is harsh on outliers: a very low score in any dimension
drags down the overall financial score more than it would under a
simple arithmetic average, capturing the intuition that severe
violations in a single ratio are problematic even if other ratios look
healthy.

We then combine the financial score and the sectoral factor
multiplicatively:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CSCIi,t=bi,t×fi,t.\text{CSCI}\_{i,t}=b\_{i,t}\times f\_{i,t}. |  | (10) |

By construction, CSCIi,t∈[0,1]\text{CSCI}\_{i,t}\in[0,1].
Firms in prohibited core sectors have bi,t=0b\_{i,t}=0 and therefore
CSCIi,t=0\text{CSCI}\_{i,t}=0 regardless of their financial ratios.
Among firms in permissible or mixed sectors, CSCIi,t\text{CSCI}\_{i,t} reflects
both the cleanliness of their business activities (via bi,tb\_{i,t}) and
their proximity to the strictest financial-ratio thresholds (via
fi,tf\_{i,t}).

Equation ([10](https://arxiv.org/html/2512.22858v1#S4.E10 "In 4.3 Aggregation to a firm-level CSCI ‣ 4 Continuous Shariah Compliance Index (CSCI): Definition and Properties ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design")) can be interpreted as a continuous analogue of
the binary screens in Table [1](https://arxiv.org/html/2512.22858v1#S2.T1 "Table 1 ‣ 2.1 Shariah screening architecture and standards ‣ 2 Institutional Background and Related Literature ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design").
A firm that comfortably satisfies all strictest thresholds receives
CSCIi,t\text{CSCI}\_{i,t} close to one.
A firm that breaches any outer threshold, or whose core business
is prohibited, receives CSCIi,t=0\text{CSCI}\_{i,t}=0.
Firms in between obtain intermediate values that quantify *how
close* they are to the various boundaries.

### 4.4 Mapping binary standards into CSCI intervals

The CSCI framework provides a natural way to compare and reinterpret
existing binary standards.
For each standard ss (e.g. AAOIFI, DJIM, FTSE, MSCI, S&P, SC
Malaysia), let 𝒫s\mathcal{P}\_{s} denote the set of firms that pass all its
screens in a given year, and ℱs\mathcal{F}\_{s} the set of firms that
fail at least one screen.
Under a binary implementation, all firms in 𝒫s\mathcal{P}\_{s} are treated
as equally compliant and strictly preferred to those in ℱs\mathcal{F}\_{s}.

Given CSCI scores, we can instead examine the distribution of
CSCIi,t\text{CSCI}\_{i,t} within and across these sets.
In particular, we can ask whether there exists a threshold τs∈(0,1)\tau\_{s}\in(0,1) such that firms with CSCIi,t≥τs\text{CSCI}\_{i,t}\geq\tau\_{s} closely
correspond to 𝒫s\mathcal{P}\_{s}.
Formally, for each standard ss we define the CSCI-implied pass set

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫~s​(τ)={i:CSCIi,t≥τ},\widetilde{\mathcal{P}}\_{s}(\tau)=\left\{i:\text{CSCI}\_{i,t}\geq\tau\right\}, |  | (11) |

and choose τs\tau\_{s} to minimise a simple misclassification loss between
𝒫~s​(τ)\widetilde{\mathcal{P}}\_{s}(\tau) and 𝒫s\mathcal{P}\_{s}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τs=arg⁡minτ∈[0,1]⁡[Pr⁡(i∈𝒫s,i∉𝒫~s​(τ))+Pr⁡(i∉𝒫s,i∈𝒫~s​(τ))].\tau\_{s}=\arg\min\_{\tau\in[0,1]}\left[\Pr\!\left(i\in\mathcal{P}\_{s},\,i\notin\widetilde{\mathcal{P}}\_{s}(\tau)\right)+\Pr\!\left(i\notin\mathcal{P}\_{s},\,i\in\widetilde{\mathcal{P}}\_{s}(\tau)\right)\right]. |  | (12) |

In Section [6](https://arxiv.org/html/2512.22858v1#S6 "6 Empirical Results ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") we implement this mapping empirically and
show that, for reasonable choices of (θ¯k,θ¯k)(\underline{\theta}\_{k},\overline{\theta}\_{k}), each standard corresponds to an interval of CSCI
scores: firms that pass AAOIFI tend to have CSCIi,t\text{CSCI}\_{i,t} near
one, while firms that pass more permissive index-provider standards but
not AAOIFI cluster at lower CSCI values.

This exercise serves two purposes.
First, it validates that the CSCI scale is consistent with existing
practice: the main standards can be recovered, to a good approximation,
by choosing appropriate CSCI thresholds.
Second, it highlights that the standards occupy interior points on a
continuous compliance spectrum rather than uniquely defining what
“Shariah-compliant” must mean.
In the next section we exploit this structure to construct portfolios
that vary the minimum CSCI threshold and the strength of CSCI-based tilts,
thereby tracing out a compliance–diversification–performance frontier.

## 5 Portfolio Construction and Empirical Framework

This section describes how we use the Continuous Shariah Compliance Index (CSCI) in
portfolio construction and how we evaluate the resulting portfolios.
We begin by defining the investable universes and rebalancing
conventions, then specify benchmark and CSCI-based portfolios, and finally
set out the performance and risk-adjustment measures.

### 5.1 Investment universes and rebalancing

The starting point each month tt is the set of CRSP common stocks with
non-missing returns and prices, for which we can compute CSCI
scores based on information available at t−1t-1.
Concretely, we apply the following filters:

* •

  CRSP share codes 10 or 11 and exchange codes 1, 2, or 3
  (NYSE/AMEX/NASDAQ).
* •

  Positive price and market capitalisation at the end of month
  t−1t-1.
* •

  Non-missing CSCIi,t-1 and control characteristics used in
  asset-pricing tests (size, book-to-market, profitability, and
  investment) at t−1t-1.

Within this base universe, we distinguish two nested universes:

1. 1.

   A *conventional* universe 𝒰tall\mathcal{U}^{\text{all}}\_{t}
   consisting of all eligible stocks.
2. 2.

   A *Shariah-admissible* universe
   𝒰tCSCI>0={i∈𝒰tall:CSCIi,t−1>0}\mathcal{U}^{\text{CSCI}>0}\_{t}=\{i\in\mathcal{U}^{\text{all}}\_{t}:\text{CSCI}\_{i,t-1}>0\}, i.e. stocks that are not ruled out
   outright by our sector and ratio filters.

Portfolios are formed at the end of each month t−1t-1 using information
available at that time (accounting variables lagged as in
Section [3](https://arxiv.org/html/2512.22858v1#S3 "3 Data and Measurement ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design"), CSCI scores constructed as in
Section [4](https://arxiv.org/html/2512.22858v1#S4 "4 Continuous Shariah Compliance Index (CSCI): Definition and Properties ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design")), held during month tt, and rebalanced monthly.
Returns are calculated including delisting returns.
Unless otherwise stated, positions are value-weighted using market
capitalisation at t−1t-1.

To account for trading frictions, we apply a proportional round-trip
transaction cost of κ\kappa basis points to each portfolio’s one-way
turnover; in robustness checks we vary κ\kappa over a range that spans
estimates for institutional US equity investors.
Baseline results use κ=25\kappa=25 bp.

### 5.2 Benchmark portfolios

We construct two benchmark portfolios against which to evaluate CSCI-based
strategies.

#### Conventional market benchmark.

The first benchmark is a broad conventional market portfolio MtM\_{t}.
Each month t−1t-1 we form

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi,t−1M=MEi,t−1∑j∈𝒰tallMEj,t−1,i∈𝒰tall,w^{M}\_{i,t-1}=\frac{\text{ME}\_{i,t-1}}{\sum\_{j\in\mathcal{U}^{\text{all}}\_{t}}\text{ME}\_{j,t-1}},\qquad i\in\mathcal{U}^{\text{all}}\_{t}, |  | (13) |

where MEi,t−1\text{ME}\_{i,t-1} denotes the market capitalisation of stock ii
at the end of month t−1t-1.
The return on MtM\_{t} is the corresponding value-weighted return.

#### Binary Islamic benchmark.

The second benchmark approximates a standard Islamic index constructed
with binary rules.
Because we cannot directly observe all index providers’ proprietary
screens, we emulate a representative global standard using the financial
and sector criteria in Table [1](https://arxiv.org/html/2512.22858v1#S2.T1 "Table 1 ‣ 2.1 Shariah screening architecture and standards ‣ 2 Institutional Background and Related Literature ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design").
Specifically, we define an indicator 𝕀i,t−1bin\mathbb{I}^{\text{bin}}\_{i,t-1}
that equals one if firm ii passes all of the following:
(i) sector and business-activity screens,
(ii) leverage, cash and receivables ratio thresholds consistent with a
one-third limit (debt, cash, receivables ≤33\leq 33–33.33% of the
relevant denominator),
and (iii) impure income ≤5%\leq 5\% of revenue; and zero otherwise.
The binary Islamic universe is
𝒰tbin={i∈𝒰tall:𝕀i,t−1bin=1}\mathcal{U}^{\text{bin}}\_{t}=\{i\in\mathcal{U}^{\text{all}}\_{t}:\mathbb{I}^{\text{bin}}\_{i,t-1}=1\}.
The corresponding value-weighted benchmark portfolio ItI\_{t} has weights

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi,t−1I=𝕀i,t−1bin​MEi,t−1∑j∈𝒰tbinMEj,t−1,i∈𝒰tbin.w^{I}\_{i,t-1}=\frac{\mathbb{I}^{\text{bin}}\_{i,t-1}\,\text{ME}\_{i,t-1}}{\sum\_{j\in\mathcal{U}^{\text{bin}}\_{t}}\text{ME}\_{j,t-1}},\qquad i\in\mathcal{U}^{\text{bin}}\_{t}. |  | (14) |

In the results section we show that this emulated index behaves similarly
to published Islamic indices in terms of sector composition, leverage and
basic performance statistics, and use it as the main binary benchmark.

### 5.3 CSCI-threshold portfolios

The first family of CSCI-based strategies imposes explicit minimum
compliance thresholds on portfolio constituents.
For a given threshold τ∈(0,1]\tau\in(0,1], we define the CSCI-constrained
universe

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒰tτ={i∈𝒰tCSCI>0:CSCIi,t−1≥τ},\mathcal{U}^{\tau}\_{t}=\{i\in\mathcal{U}^{\text{CSCI}>0}\_{t}:\text{CSCI}\_{i,t-1}\geq\tau\}, |  | (15) |

and construct a value-weighted portfolio PtτP^{\tau}\_{t} with weights

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi,t−1τ=MEi,t−1∑j∈𝒰tτMEj,t−1,i∈𝒰tτ.w^{\tau}\_{i,t-1}=\frac{\text{ME}\_{i,t-1}}{\sum\_{j\in\mathcal{U}^{\tau}\_{t}}\text{ME}\_{j,t-1}},\qquad i\in\mathcal{U}^{\tau}\_{t}. |  | (16) |

We consider a grid of thresholds
τ∈{0.50,0.70,0.80,0.90}\tau\in\{0.50,0.70,0.80,0.90\}.
Lower values (e.g. τ=0.50\tau=0.50) correspond to relatively permissive
interpretations that admit most firms with non-zero CSCI, whereas higher
values (e.g. τ=0.90\tau=0.90) restrict the universe to firms that are
comfortably within the strictest financial and sectoral bounds.
Existing binary standards can be interpreted as lying at intermediate
points on this spectrum: in Section [4.4](https://arxiv.org/html/2512.22858v1#S4.SS4 "4.4 Mapping binary standards into CSCI intervals ‣ 4 Continuous Shariah Compliance Index (CSCI): Definition and Properties ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") we show that
the set of firms passing our emulated binary screen corresponds roughly
to firms with CSCI above a standard-specific threshold τs\tau\_{s}.

For each τ\tau we track not only returns but also portfolio
characteristics such as the number of constituents, effective number of
stocks (inverse Herfindahl index), sector weights, average leverage and
liquidity ratios, and average CSCI levels.
This allows us to describe how the investable universe and balance-sheet
profile evolve as compliance stringency is tightened.

### 5.4 CSCI-tilt portfolios

Threshold portfolios change the set of included firms.
An alternative is to keep a broad admissible universe and use CSCI
*within* that universe as a tilting variable.
For a given tilt intensity parameter κ≥0\kappa\geq 0, we define
CSCI-tilted weights on the admissible universe
𝒰tCSCI>0\mathcal{U}^{\text{CSCI}>0}\_{t} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | w~i,t−1κ=CSCIi,t−1κ​MEi,t−1∑j∈𝒰tCSCI>0CSCIj,t−1κ​MEj,t−1,i∈𝒰tCSCI>0.\widetilde{w}^{\kappa}\_{i,t-1}=\frac{\text{CSCI}\_{i,t-1}^{\kappa}\,\text{ME}\_{i,t-1}}{\sum\_{j\in\mathcal{U}^{\text{CSCI}>0}\_{t}}\text{CSCI}\_{j,t-1}^{\kappa}\,\text{ME}\_{j,t-1}},\qquad i\in\mathcal{U}^{\text{CSCI}>0}\_{t}. |  | (17) |

When κ=0\kappa=0, ([17](https://arxiv.org/html/2512.22858v1#S5.E17 "In 5.4 CSCI-tilt portfolios ‣ 5 Portfolio Construction and Empirical Framework ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design")) reduces to the value-weighted portfolio
on the admissible universe.
As κ\kappa increases, weights are progressively shifted towards
high-CSCI firms and away from low-CSCI firms, but no firm with CSCI>0>0 is
forced to zero weight.
In the empirical analysis we examine κ∈{0,1,2}\kappa\in\{0,1,2\}.
These portfolios are particularly relevant for asset managers who wish
to integrate CSCI into existing Islamic strategies without excluding
large parts of the universe.

### 5.5 Performance and risk-adjustment measures

Let rp,tr\_{p,t} denote the gross return on portfolio pp in month tt and
rf,tr\_{f,t} the one-month Treasury bill rate.
We focus on the following performance and risk measures:

* •

  Average excess return:
  r¯pe=1T​∑t=1T(rp,t−rf,t)\overline{r}^{\,e}\_{p}=\frac{1}{T}\sum\_{t=1}^{T}(r\_{p,t}-r\_{f,t}).
* •

  Volatility:
  σp=1T−1​∑t=1T[(rp,t−rf,t)−r¯pe]2\sigma\_{p}=\sqrt{\frac{1}{T-1}\sum\_{t=1}^{T}\left[(r\_{p,t}-r\_{f,t})-\overline{r}^{\,e}\_{p}\right]^{2}}.
* •

  Sharpe ratio:
  SRp=r¯pe/σp\text{SR}\_{p}=\overline{r}^{\,e}\_{p}/\sigma\_{p}.
* •

  Downside risk measures:
  Sortino ratios based on downside deviation, and maximum drawdown
  computed from the cumulated return series.
* •

  Turnover and trading costs:
  one-way turnover each month, and net performance after subtracting
  κ\kappa basis points per unit of turnover.

To adjust for standard risk factors, we estimate time-series regressions
of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | rp,t−rf,t=αp+𝜷p⊤​𝐟t+εp,t,r\_{p,t}-r\_{f,t}=\alpha\_{p}+\boldsymbol{\beta}\_{p}^{\top}\mathbf{f}\_{t}+\varepsilon\_{p,t}, |  | (18) |

where 𝐟t\mathbf{f}\_{t} is a vector of factor returns.
Our baseline specification uses the Fama–French five-factor model
augmented with momentum:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐟t=(MKTt,SMBt,HMLt,RMWt,CMAt,MOMt)⊤.\mathbf{f}\_{t}=\bigl(\text{MKT}\_{t},\text{SMB}\_{t},\text{HML}\_{t},\text{RMW}\_{t},\text{CMA}\_{t},\text{MOM}\_{t}\bigr)^{\top}. |  | (19) |

We report intercepts αp\alpha\_{p} (monthly and annualised),
factor loadings, tt-statistics using Newey–West standard errors, and
the regression R2R^{2}.
We also estimate a CAPM and a three-factor specification as robustness
checks.

### 5.6 Cross-sectional tests with CSCI

Finally, to explore whether CSCI carries incremental information about
expected returns beyond its role in defining investable universes, we
conduct cross-sectional asset-pricing tests at the individual-stock
level.
Our baseline approach is a monthly Fama–MacBeth regression of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ri,t+1−rf,t+1=at+bt​CSCIi,t+𝜸t⊤​𝐗i,t+ui,t+1,r\_{i,t+1}-r\_{f,t+1}=a\_{t}+b\_{t}\,\text{CSCI}\_{i,t}+\boldsymbol{\gamma}\_{t}^{\top}\mathbf{X}\_{i,t}+u\_{i,t+1}, |  | (20) |

where ri,t+1r\_{i,t+1} is the return on stock ii in month t+1t+1,
CSCIi,t\text{CSCI}\_{i,t} is the compliance degree at tt, and 𝐗i,t\mathbf{X}\_{i,t}
are control characteristics (log size, book-to-market, profitability,
investment, past return, and optionally leverage and beta).
We average the estimated slope coefficients btb\_{t} over time and compute
tt-statistics using the time-series of btb\_{t}.
A significantly positive (negative) b¯\overline{b} would indicate that
more compliant firms command a return premium (discount) after
controlling for standard determinants of expected returns.

These portfolio and regression frameworks provide the lens through which
we evaluate CSCI in the next section.
We first document the cross-sectional distribution and time-series
dynamics of CSCI, then show how varying CSCI thresholds and tilts reshapes
portfolio characteristics, and finally examine the performance and
risk-adjusted returns of CSCI-based strategies relative to conventional
and binary Islamic benchmarks.

## 6 Empirical Results

This section documents the empirical behaviour of the Continuous Shariah Compliance Index (CSCI) and assesses its implications for portfolio construction.
We begin with the cross-sectional distribution of CSCI and its relation to
firm characteristics, then map existing binary standards into CSCI
intervals, and finally analyse the performance of CSCI-based portfolios
and the cross-sectional pricing of CSCI at the stock level.

### 6.1 Cross-sectional distribution of the Continuous Shariah Compliance Index

Table [4](https://arxiv.org/html/2512.22858v1#S6.T4 "Table 4 ‣ 6.1 Cross-sectional distribution of the Continuous Shariah Compliance Index ‣ 6 Empirical Results ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") reports the cross-sectional distribution of the
Continuous Shariah Compliance Index between 1999 and 2024. We obtain 661,439 firm–month
observations with a well-defined CSCI. Roughly 19% of firm–months lie at
CSCI=0\mathrm{CSCI}=0, corresponding to firms in sectors that are excluded ex–ante
by Shariah sector screens (conventional finance, alcohol, gambling, tobacco,
and other clearly non-permissible industries). At the other extreme, about
20% of firm–months have CSCI≥0.99\mathrm{CSCI}\geq 0.99, reflecting firms with very
conservative balance sheets and negligible non-permissible income.

Conditional on belonging to permissible sectors (i.e. among firms with
bsector>0b\_{\text{sector}}>0), the CSCI exhibits rich continuous variation.
For this investable universe (535,084 firm–months), the median CSCI is 0.25,
with an interquartile range of 0.07 to 0.96, and approximately 74% of
observations lie strictly between 0.01 and 0.99. Figures [2](https://arxiv.org/html/2512.22858v1#S6.F2 "Figure 2 ‣ 6.1 Cross-sectional distribution of the Continuous Shariah Compliance Index ‣ 6 Empirical Results ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") and
[3](https://arxiv.org/html/2512.22858v1#S6.F3 "Figure 3 ‣ 6.1 Cross-sectional distribution of the Continuous Shariah Compliance Index ‣ 6 Empirical Results ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") plot the corresponding cross-sectional densities.
The first panel, based on all firms, makes clear that the sector screens
identify a sizeable mass of ex–ante non-investable firms. The second panel
shows that, within permissible sectors, CSCI is far from a binary indicator:
there is substantial mass at intermediate values, precisely capturing
“barely compliant” versus “comfortably compliant” issuers that standard
pass/fail index rules treat identically. This continuous dispersion is what
the portfolio experiments in Sections [6.4](https://arxiv.org/html/2512.22858v1#S6.SS4 "6.4 Portfolio characteristics across CSCI thresholds and tilts ‣ 6 Empirical Results ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design")
and [6.6](https://arxiv.org/html/2512.22858v1#S6.SS6 "6.6 Cross-sectional pricing of CSCI ‣ 6 Empirical Results ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") exploit.

Table 4: Cross-sectional distribution of the Continuous Shariah Compliance Index (CSCI), 1999–2024

|  | All firms | Permissible sectors |
| --- | --- | --- |
| Number of firm–months | 661,439 | 535,084 |
| Mean CSCI | 0.36 | 0.44 |
| Standard deviation | 0.39 | 0.39 |
| 1st percentile | 0.00 | 0.01 |
| 10th percentile | 0.00 | 0.03 |
| 25th percentile | 0.03 | 0.07 |
| Median | 0.18 | 0.25 |
| 75th percentile | 0.73 | 0.96 |
| 90th percentile | 1.00 | 1.00 |
| 99th percentile | 1.00 | 1.00 |
| Mass at CSCI=0\mathrm{CSCI}=0 | 0.19 | 0.00 |
| Mass at CSCI≥0.99\mathrm{CSCI}\geq 0.99 | 0.20 | 0.24 |

*Notes:* This table reports the cross-sectional distribution of the
Continuous Shariah Compliance Index (CSCI) at the monthly frequency between January
1999 and December 2024. “Permissible sectors” restricts the sample to
firms with strictly positive sector gate bsectorb\_{\text{sector}}, i.e. firms
not excluded by Shariah sector screens. Masses are fractions of
firm–month observations.

![Refer to caption](x2.png)


Figure 2: Cross-sectional distribution of the Continuous Shariah Compliance Index (CSCI) for all firms, 1999–2024.

![Refer to caption](x3.png)


Figure 3: Cross-sectional CSCI distribution in permissible sectors (investable universe), 1999–2024.




Table 5: Average firm characteristics by Continuous Shariah Compliance Index (CSCI) decile

|  | Mean CSCI | Log(ME) | Debt ratio | Cash ratio | Receivables ratio | Impure income ratio |
| --- | --- | --- | --- | --- | --- | --- |
| CSCI decile |  |  |  |  |  |  |
| 1 | 0.000 | 18.699 | 0.176 | 0.106 | 0.625 | 0.999 |
| 2 | 0.002 | 19.271 | 0.243 | 0.179 | 0.597 | 0.863 |
| 3 | 0.028 | 18.952 | 0.101 | 0.677 | 0.783 | 0.046 |
| 4 | 0.047 | 18.848 | 0.099 | 0.553 | 0.683 | 0.000 |
| 5 | 0.154 | 19.015 | 0.430 | 0.159 | 0.338 | 0.000 |
| 6 | 0.200 | 19.126 | 0.402 | 0.109 | 0.300 | 0.000 |
| 7 | 0.395 | 19.295 | 0.234 | 0.133 | 0.328 | 0.000 |
| 8 | 0.738 | 19.266 | 0.186 | 0.123 | 0.296 | 0.000 |
| 9 | 0.990 | 19.268 | 0.140 | 0.086 | 0.197 | 0.000 |
| 10 | 1.000 | 19.502 | 0.143 | 0.076 | 0.190 | 0.000 |

*Notes*: This table reports time–series averages of
cross–sectional firm characteristics by deciles of the Continuous Shariah Compliance Index (CSCI), computed monthly over 1999–2024. “Mean CSCI” is the mean
CSCI in each decile. Log(ME) is the natural logarithm of market equity
(in U.S. dollars). “Debt ratio”, “Cash ratio” and “Receivables ratio”
are interest–bearing debt, cash and interest–bearing assets, and accounts
receivable, respectively, each scaled by the denominator used in the CSCI
construction (see Section [4](https://arxiv.org/html/2512.22858v1#S4 "4 Continuous Shariah Compliance Index (CSCI): Definition and Properties ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design")). “Impure income ratio” is the
share of non–permissible income in total revenue. All ratios are
winsorised at the 1% and 99% levels; entries are rounded to three
decimal places.

The pattern in Table [5](https://arxiv.org/html/2512.22858v1#S6.T5 "Table 5 ‣ 6.1 Cross-sectional distribution of the Continuous Shariah Compliance Index ‣ 6 Empirical Results ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") confirms that the CSCI index orders firms
along a meaningful financial and income–purity gradient. The lowest CSCI deciles
have extremely low scores, very high impure–income shares (around one in decile 1
and above 0.85 in decile 2), and balance sheets dominated by cash and receivables.
As CSCI rises, impure income falls sharply towards zero while leverage, cash and
receivables ratios gradually decline, especially in the upper deciles. Mid–range
deciles (5–6) exhibit relatively high leverage despite almost fully permissible
income, indicating that the financial–ratio screens, rather than sector
exclusions alone, remain binding. High–CSCI firms (deciles 8–10) combine clean
income, more conservative balance sheets and somewhat larger size, showing that
CSCI captures both revenue cleanliness and balance–sheet conservatism rather than
simply reproducing a sector or size filter.

### 6.2 Mapping binary standards into CSCI

We next examine how existing binary standards correspond to regions of
the CSCI scale.
For each standard ss (AAOIFI, DJIM, FTSE Islamic, MSCI Islamic, S&P
Shariah, SC Malaysia), I construct a pass indicator
𝕀i,ts\mathbb{I}^{s}\_{i,t} that emulates its sector and ratio screens using
the harmonised definitions in Section [3](https://arxiv.org/html/2512.22858v1#S3 "3 Data and Measurement ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") and the thresholds
summarised in Table [1](https://arxiv.org/html/2512.22858v1#S2.T1 "Table 1 ‣ 2.1 Shariah screening architecture and standards ‣ 2 Institutional Background and Related Literature ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design").
Sector permissibility is captured by the indicator b​\_​sector,i​tb\\_{\text{sector},it},
and financial screens are evaluated on the unified debt, cash,
receivables/liquidity, and impure income ratios that also enter the CSCI
construction in Section [4](https://arxiv.org/html/2512.22858v1#S4 "4 Continuous Shariah Compliance Index (CSCI): Definition and Properties ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design").
This ensures that differences across standards reflect their
*thresholds*, not mechanical differences in denominators or data
sources.

Table [6](https://arxiv.org/html/2512.22858v1#S6.T6 "Table 6 ‣ 6.2 Mapping binary standards into CSCI ‣ 6 Empirical Results ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") reports the unconditional fraction of
firm–month observations that pass each standard over 1999–2024.
Roughly one third of the U.S. universe is investable at any point in
time under AAOIFI (32.3%), FTSE Islamic (32.2%), and S&P Shariah
(31.8%).
In contrast, only about one fifth of firm–months satisfy the joint
DJIM and MSCI Islamic constraints (both 22.2%), reflecting their
stricter one–third caps on leverage, cash, and receivables.
The Malaysian SC rules admit the broadest investable set, with 36.9% of
firm–months passing.
Annual pass rates (not tabulated) fluctuate in a relatively tight band
around these long–run averages, suggesting that cross–standard
differences are primarily structural rather than driven by particular
episodes.

Table 6: Share of Firm–Months Passing Major Shariah Screens

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | AAOIFI | DJIM | MSCI Islamic | FTSE Islamic | S&P Shariah | SC Malaysia |
| Fraction of firm–months | 0.323 | 0.222 | 0.222 | 0.322 | 0.318 | 0.370 |

*Notes*: This table reports the fraction of
firm–month observations in the CRSP–Compustat US panel (1999–2024)
that satisfy each set of financial–ratio and sectoral Shariah screens,
evaluated on the harmonised ratios defined in Section [3](https://arxiv.org/html/2512.22858v1#S3 "3 Data and Measurement ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design").
Entries are time–series averages of annual cross–sectional pass rates.

To relate the binary screening decisions back to the continuous CSCI, I
compare 𝕀i,ts\mathbb{I}^{s}\_{i,t} to each firm’s CSCI score and estimate,
for every standard ss, the CSCI threshold τs\tau\_{s} that best replicates
its pass set, as in equation ([12](https://arxiv.org/html/2512.22858v1#S4.E12 "In 4.4 Mapping binary standards into CSCI intervals ‣ 4 Continuous Shariah Compliance Index (CSCI): Definition and Properties ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design")).
Let 𝒫s={(i,t):𝕀i,ts=1}\mathcal{P}\_{s}=\{(i,t):\mathbb{I}^{s}\_{i,t}=1\} denote the set of
firm–months passing standard ss, and let
𝒫~s​(τ)={(i,t):CSCIi,t≥τ}\widetilde{\mathcal{P}}\_{s}(\tau)=\{(i,t):\text{CSCI}\_{i,t}\geq\tau\} be the CSCI–implied pass set for a
candidate cut–off τ\tau.
For each standard I search over a fine grid τ∈[0,1]\tau\in[0,1] and select
τs\tau\_{s} to minimise the sum of the false–negative and false–positive
rates between 𝒫s\mathcal{P}\_{s} and 𝒫~s​(τ)\widetilde{\mathcal{P}}\_{s}(\tau).

Table [7](https://arxiv.org/html/2512.22858v1#S6.T7 "Table 7 ‣ 6.2 Mapping binary standards into CSCI ‣ 6 Empirical Results ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") reports, for each standard:
(i) the estimated threshold τs\tau\_{s},
(ii) the fraction of firm–months classified as compliant under that
standard (the same object as in Table [6](https://arxiv.org/html/2512.22858v1#S6.T6 "Table 6 ‣ 6.2 Mapping binary standards into CSCI ‣ 6 Empirical Results ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design")),
(iii) the fraction of binary–compliant firm–months with
CSCIi,t<τs\text{CSCI}\_{i,t}<\tau\_{s} (false negatives under CSCI), and
(iv) the fraction of binary–non–compliant firm–months with
CSCIi,t≥τs\text{CSCI}\_{i,t}\geq\tau\_{s} (false positives).
The last column shows the average CSCI among firms classified as
compliant by each standard.

Table 7: Mapping Binary Standards into CSCI Thresholds

| Standard | τs\tau\_{s} | Compliant fraction | FN rate | FP rate | Avg. CSCI (compliant) |
| --- | --- | --- | --- | --- | --- |
| AAOIFI | 0.31 | 0.32 | 0.11 | 0.14 | 0.81 |
| DJIM | 0.68 | 0.22 | 0.00 | 0.05 | 0.98 |
| MSCI Islamic | 0.68 | 0.22 | 0.00 | 0.05 | 0.98 |
| FTSE Islamic | 0.34 | 0.32 | 0.01 | 0.07 | 0.87 |
| S&P Shariah | 0.36 | 0.32 | 0.01 | 0.06 | 0.88 |
| SC Malaysia | 0.29 | 0.37 | 0.11 | 0.09 | 0.79 |

*Notes*: This table summarises the mapping between
binary Shariah standards and CSCI thresholds.
τs\tau\_{s} is the CSCI threshold that minimises the total
misclassification rate between the binary pass set
𝒫s\mathcal{P}\_{s} and the CSCI–implied pass set
𝒫~s​(τ)\widetilde{\mathcal{P}}\_{s}(\tau).
“FN rate” is the fraction of binary–compliant firm–months with
CSCI<τs<\tau\_{s}, and “FP rate” is the fraction of
binary–non–compliant firm–months with CSCI≥τs\geq\tau\_{s}.

Two patterns emerge.
First, the recovered thresholds τs\tau\_{s} line up with the perceived
stringency of the standards.
SC Malaysia is associated with the lowest CSCI cut–off (τS​C=0.29\tau\_{SC}=0.29)
and the largest compliant fraction (around 37%), and it admits firms
with an average CSCI of only 0.79.
At the other end of the spectrum, DJIM and MSCI Islamic correspond to
very tight thresholds (τD​J​I​M=τM​S​C​I=0.68\tau\_{DJIM}=\tau\_{MSCI}=0.68) and pick a much
smaller universe (about 22% of firm–months), with average CSCI close to
one (0.98) and essentially no false negatives.
AAOIFI, FTSE Islamic, and S&P Shariah sit in between: they accept
around one third of firm–months, with thresholds in the 0.31–0.36 range
and average CSCIs between 0.81 and 0.88.

Second, misclassification rates are economically modest for all
standards.
The sum of false negatives and false positives is typically well below
0.25, and for DJIM and MSCI almost all of the error comes from a small
set of high–CSCI firms that the binary rules classify as non–compliant.
In other words, a single cut–off on the continuous CSCI scale can closely
replicate each binary pass set while revealing that the standards occupy
distinct *intervals* on the CSCI spectrum rather than defining
unique corner points.
This supports the interpretation of CSCI as a continuous,
practice–consistent measure of Shariah compliance.

### 6.3 Performance of binary Islamic benchmarks

Having established how existing binary standards map into regions of the
CSCI scale (Section [6.2](https://arxiv.org/html/2512.22858v1#S6.SS2 "6.2 Mapping binary standards into CSCI ‣ 6 Empirical Results ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design")), I next examine the
realised performance of the corresponding benchmark portfolios.
For each standard s∈{AAOIFI, DJIM, MSCI Islamic, FTSE Islamic,
S&P Shariah, SC Malaysia}s\in\{\text{AAOIFI, DJIM, MSCI Islamic, FTSE Islamic,
S\&P Shariah, SC Malaysia}\}, I form a value–weighted portfolio of all
firm–months that pass the sector and ratio screens for ss.
Returns are computed at the monthly frequency, using market
capitalisation as of the previous month as portfolio weights.
I evaluate each benchmark against the risk–free rate and against the
Fama–French five factors plus a momentum factor (FF5+MOM).

Table [8](https://arxiv.org/html/2512.22858v1#S6.T8 "Table 8 ‣ 6.3 Performance of binary Islamic benchmarks ‣ 6 Empirical Results ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") reports the main performance statistics.
For each standard I show the number of non–missing months in the sample,
the annualised mean excess return, annualised volatility, annualised
Sharpe ratio, and the intercept from an FF5+MOM regression together with
its tt–statistic and coefficient of determination.

Table 8: Performance of binary Islamic benchmark portfolios

| Standard | NN (months) | Excess return (ann.) | Vol. (ann.) | Sharpe | α\alpha (monthly) | t​(α)t(\alpha) | R2R^{2} |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AAOIFI | 311 | 0.174 | 0.190 | 0.916 | 0.0094 | 5.95 | 0.82 |
| DJIM | 311 | 0.161 | 0.180 | 0.892 | 0.0075 | 5.64 | 0.85 |
| MSCI Islamic | 311 | 0.161 | 0.180 | 0.892 | 0.0075 | 5.64 | 0.85 |
| FTSE Islamic | 311 | 0.175 | 0.188 | 0.928 | 0.0095 | 5.72 | 0.83 |
| S&P Shariah | 311 | 0.175 | 0.188 | 0.930 | 0.0095 | 5.68 | 0.83 |
| SC Malaysia | 311 | 0.176 | 0.190 | 0.926 | 0.0096 | 5.99 | 0.84 |

*Notes*: This table reports value–weighted performance
of portfolios formed under the main binary Shariah standards.
“Excess return (ann.)” is the annualised mean excess return over the
risk–free rate. “Vol. (ann.)” is the annualised standard deviation
of monthly returns. “Sharpe” is the annualised Sharpe ratio.
“α\alpha (monthly)” and t​(α)t(\alpha) are the intercept and associated
tt–statistic from a regression of monthly excess returns on the
Fama–French five factors and a momentum factor (FF5+MOM).
R2R^{2} is the regression coefficient of determination.

Two findings stand out.
First, the unconditional performance of the binary benchmarks is
remarkably similar across standards.
Annualised excess returns lie between 16% and 18%, with annualised
volatility around 18–19%, so Sharpe ratios fall in a narrow band
between 0.89 and 0.93.
From an investor’s perspective, shifting from AAOIFI to DJIM, FTSE,
MSCI, S&P or SC Malaysia does not dramatically change the basic
risk–return profile of the investable universe.

Second, all benchmarks earn economically large and statistically
significant factor–adjusted alphas.
Monthly intercepts range from 75 to 96 basis points, with tt–statistics
around 5.6–6.0, and the FF5+MOM regressions explain roughly 82–85% of
the variation in returns.
SC Malaysia, S&P Shariah and FTSE Islamic exhibit slightly higher
Sharpe ratios and alphas than AAOIFI, DJIM and MSCI Islamic, but the
dispersion across standards is small relative to the common level of
outperformance.
These results confirm that existing Shariah indices have historically
delivered attractive risk–adjusted returns, and they provide a natural
benchmark against which to evaluate the CSCI–based portfolios constructed
in the next subsection.

### 6.4 Portfolio characteristics across CSCI thresholds and tilts

We now turn to the portfolios defined in Section [5](https://arxiv.org/html/2512.22858v1#S5 "5 Portfolio Construction and Empirical Framework ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design").
Table [9](https://arxiv.org/html/2512.22858v1#S6.T9 "Table 9 ‣ 6.4 Portfolio characteristics across CSCI thresholds and tilts ‣ 6 Empirical Results ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") reports average characteristics for
value-weighted CSCI-threshold portfolios PtτP^{\tau}\_{t} with
τ∈{0.50,0.70,0.80,0.90}\tau\in\{0.50,0.70,0.80,0.90\}.
For each threshold we compute, month by month, the number of eligible
stocks, the effective number of stocks (inverse Herfindahl index), and
portfolio-weighted averages of the balance-sheet ratios
(debt, cash, and receivables) and CSCI.
The table reports time–series averages of these monthly quantities.

Table 9: Portfolio Characteristics by CSCI Threshold

| Portfolio | # stocks | Eff. # | Debt ratio | Cash ratio | Rec. ratio | Avg. CSCI |
| --- | --- | --- | --- | --- | --- | --- |
| CSCI ≥0.50\geq 0.50 | 671.4 | 61.1 | 0.196 | 0.100 | 0.206 | 0.918 |
| CSCI ≥0.70\geq 0.70 | 554.7 | 51.5 | 0.185 | 0.097 | 0.200 | 0.970 |
| CSCI ≥0.80\geq 0.80 | 506.1 | 47.4 | 0.183 | 0.092 | 0.193 | 0.985 |
| CSCI ≥0.90\geq 0.90 | 460.5 | 42.7 | 0.179 | 0.090 | 0.190 | 0.995 |

*Notes*: This table summarises average portfolio
characteristics for value-weighted CSCI-threshold portfolios
PtτP^{\tau}\_{t}. “# stocks” is the average number of constituents per
month. “Eff. #” denotes the effective number of stocks (inverse
Herfindahl index). The debt, cash and receivables ratios are averaged
across constituents using portfolio weights.
Impure-income shares are essentially zero for all thresholds and are
therefore omitted.

As expected, tightening the CSCI threshold reduces the number of eligible
stocks and raises the average CSCI of constituents.
Moving from τ=0.50\tau=0.50 to τ=0.90\tau=0.90 lowers the average number of
holdings from roughly 670670 to 460460, and the effective number of stocks
from about 6161 to 4343.
At the same time, the average CSCI of portfolio constituents increases
from 0.920.92 to almost 1.001.00.
The tightening operates along the intended balance-sheet dimensions:
portfolio-weighted debt, cash and receivables ratios all decline as
τ\tau increases (e.g. the average debt ratio falls from 0.200.20 to
0.180.18), while impure-income exposure is negligible throughout.
The reduction in effective breadth is gradual rather than catastrophic;
even at τ=0.90\tau=0.90 the portfolio remains well diversified across a
large cross-section of stocks.

CSCI-tilt portfolios, defined in equation ([17](https://arxiv.org/html/2512.22858v1#S5.E17 "In 5.4 CSCI-tilt portfolios ‣ 5 Portfolio Construction and Empirical Framework ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design")), show similar
patterns while keeping the full CSCI>0>0 universe intact.
For moderate tilt intensities (e.g. κ=1\kappa=1) the weight distribution
shifts towards high-CSCI firms without materially shrinking the number
of holdings.
This provides a practical route for asset managers who wish to raise the
average compliance of an existing Shariah portfolio without imposing
hard exclusion thresholds beyond those already required by their
Shariah boards.

### 6.5 Performance and compliance–performance frontier

Table [10](https://arxiv.org/html/2512.22858v1#S6.T10 "Table 10 ‣ 6.5 Performance and compliance–performance frontier ‣ 6 Empirical Results ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") reports annualised excess returns, volatility,
Sharpe ratios, and factor-adjusted alphas for the conventional market
benchmark MtM\_{t}, the binary Islamic benchmark ItI\_{t} (based on DJIM-style
screens), and CSCI-threshold portfolios PtτP\_{t}^{\tau}.
The statistics are computed from monthly returns over the full sample;
sub-period results (pre- and post-2008, pre- and post-2010, and pre- and
post-2020) are reported in the Online Appendix.

Table 10: Performance of CSCI-Based Portfolios

| Portfolio | Excess ret. | Volatility | Sharpe | FF5+MOM α\alpha | t​(α)t(\alpha) | Max drawdown |
| --- | --- | --- | --- | --- | --- | --- |
| Conventional market (MM) | 0.2250 | 0.1840 | 1.2227 | 0.1656 | 8.54 | -0.3846 |
| Binary Islamic (II) | 0.1606 | 0.1801 | 0.8919 | 0.0902 | 5.64 | -0.4270 |
| CSCI ≥0.50\geq 0.50 | 0.1772 | 0.1871 | 0.9473 | 0.1120 | 5.60 | -0.3953 |
| CSCI ≥0.70\geq 0.70 | 0.1708 | 0.1872 | 0.9122 | 0.1069 | 5.32 | -0.3932 |
| CSCI ≥0.80\geq 0.80 | 0.1615 | 0.1817 | 0.8889 | 0.0918 | 5.75 | -0.4084 |
| CSCI ≥0.90\geq 0.90 | 0.1600 | 0.1807 | 0.8851 | 0.0908 | 5.78 | -0.3979 |

*Notes*: This table reports annualised performance
statistics for the conventional market portfolio, the emulated
binary Islamic benchmark, and CSCI-threshold portfolios.
Statistics are computed from monthly returns.
“Excess ret.” is the mean excess return over T-bills,
“Volatility” is the standard deviation of excess returns,
“Sharpe” is the ratio of the two, and
“FF5+MOM α\alpha” is the intercept from a regression on the
Fama–French five factors plus momentum (equation ([18](https://arxiv.org/html/2512.22858v1#S5.E18 "In 5.5 Performance and risk-adjustment measures ‣ 5 Portfolio Construction and Empirical Framework ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design"))),
annualised by multiplying the monthly alpha by 12.
t​(α)t(\alpha) is the Newey–West tt-statistic; max drawdown is the
maximum cumulative loss from peak to trough of the total-return index.

Three results stand out.

First, the binary Islamic benchmark delivers strong risk-adjusted
performance, albeit below the conventional market.
The market portfolio earns an annualised excess return of roughly
22.5%22.5\% with volatility of 18.4%18.4\%, corresponding to a Sharpe ratio of
1.22 and a highly significant FF5+MOM alpha of about 16.6%16.6\% per year
(t=8.5t=8.5).
The DJIM-style Islamic benchmark earns an excess return of 16.1%16.1\% with
similar volatility (18.0%18.0\%), implying a Sharpe ratio of 0.89 and an
annualised alpha of about 9.0%9.0\% (t=5.6t=5.6).
Thus, even after controlling for standard equity factors, an Islamic
screen based on conventional index rules is not obviously penalised in
terms of risk-adjusted performance over the sample.

Second, CSCI-threshold portfolios trace out a clear but gentle
*compliance–performance frontier*.
At τ=0.50\tau=0.50, the CSCI portfolio attains an excess return of 17.7%17.7\%
and volatility of 18.7%18.7\%, yielding a Sharpe ratio of 0.95 and an
annualised alpha of 11.2%11.2\% (t=5.6t=5.6), both higher than for the binary
benchmark.
As the threshold is raised from 0.500.50 to 0.900.90, excess returns drift
down from 17.7%17.7\% to 16.0%16.0\% and volatility declines modestly from
18.7%18.7\% to 18.1%18.1\%; Sharpe ratios fall only slightly, from 0.95 to
0.89.
Across all thresholds, multi-factor alphas remain in the 99–11%11\%
range and are statistically highly significant (t≈5.3t\approx 5.3–5.85.8).
In other words, moving to stricter CSCI cuts some upside relative to the
market but does not generate a clear deterioration in risk-adjusted
performance relative to the binary Islamic benchmark.

Third, CSCI-tilt portfolios (not reported in the main table for brevity)
offer an intermediate implementation.
Moderate tilts towards high-CSCI firms preserve most of the Sharpe ratio
and alpha of the binary benchmark while raising the average CSCI level
and slightly reducing drawdowns.
In settings where tracking error to an established Islamic benchmark is
a binding constraint, such tilts may be more practical than imposing
hard CSCI thresholds.

Figure [4](https://arxiv.org/html/2512.22858v1#S6.F4 "Figure 4 ‣ 6.5 Performance and compliance–performance frontier ‣ 6 Empirical Results ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design") visualises the compliance–performance
frontier by plotting average CSCI against annualised Sharpe ratios and
alphas for the main portfolios.
The conventional market sits at low average CSCI and high Sharpe; the
binary Islamic benchmark moves up in CSCI with a moderate reduction in
Sharpe; and CSCI portfolios trace out a smooth locus as τ\tau increases,
illustrating the trade-off between stricter compliance and aggregate
equity exposure.

![Refer to caption](CSCI_compliance_performance_frontier.png)

Figure 4: Compliance–Performance Frontier

*Notes*: This figure plots the average Continuous Shariah Compliance Index (CSCI) of each portfolio against its annualised
Sharpe ratio (left panel) and annualised FF5+MOM alpha (right panel).
Portfolios are the conventional market benchmark MM, the DJIM-style
binary Islamic benchmark II, and CSCI-threshold portfolios with
τ∈{0.50,0.70,0.80,0.90}\tau\in\{0.50,0.70,0.80,0.90\}.

### 6.6 Cross-sectional pricing of CSCI

Finally, I ask whether the Continuous Shariah Compliance Index contains
information about the cross-section of expected returns.
Following Fama and MacBeth (1973), I run monthly cross-sectional
regressions of one-month-ahead returns on the current CSCI score,
with and without a standard size control (log market equity).
In month tt the regression is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ri,t+1=αt+βt​CSCIi,t+γt​log⁡(M​Ei,t)+εi,t+1,r\_{i,t+1}=\alpha\_{t}+\beta\_{t}\text{CSCI}\_{i,t}+\gamma\_{t}\log(ME\_{i,t})+\varepsilon\_{i,t+1}, |  | (21) |

where log⁡(M​Ei,t)\log(ME\_{i,t}) is included only in the second specification.
I then average the monthly slopes {βt,γt}\{\beta\_{t},\gamma\_{t}\} across time
and compute Fama–MacBeth tt-statistics.

Table 11: Fama–MacBeth Regressions of One-Month-Ahead Returns on CSCI

|  |  |  |
| --- | --- | --- |
|  | (1) CSCI only | (2) CSCI + log size |
| CSCI | 0.0005 | -0.0014 |
|  | (0.22) | (-0.62) |
| log market equity |  | -0.0000 |
|  |  | (-0.01) |
| Constant | 0.0073 | 0.0074 |
|  | (1.81) | (0.44) |

*Notes*: This table reports Fama–MacBeth
cross-sectional regressions of one-month-ahead stock returns on the
Continuous Shariah Compliance Index (CSCI). In each month tt, I regress
ri,t+1r\_{i,t+1} on CSCIi,t\text{CSCI}\_{i,t} with and without log market equity
(log market capitalisation) as a control, and then average the
resulting coefficients across time.
Coefficients are in monthly return units.
tt-statistics (in parentheses) are computed as the mean coefficient
divided by its time-series standard error.

The univariate specification in column (1) shows that the average slope
on CSCI is essentially zero: the point estimate is 0.00050.0005 per month
with a tt-statistic of 0.220.22, implying no economically or
statistically meaningful relation between CSCI and next-month returns.
When log market equity is added as a control (column (2)), the CSCI
coefficient becomes slightly negative (−0.0014-0.0014) but remains far from
significant (t=−0.62t=-0.62).
The size coefficient itself is also indistinguishable from zero
(t=−0.01t=-0.01).

Overall, these Fama–MacBeth results indicate that CSCI does not command
a distinct risk premium in the cross-section of individual stocks.
This is consistent with the portfolio evidence in
Section [6.5](https://arxiv.org/html/2512.22858v1#S6.SS5 "6.5 Performance and compliance–performance frontier ‣ 6 Empirical Results ‣ Beyond Binary Screens: A Continuous Shariah Compliance Index for Asset Pricing and Portfolio Design"): CSCI is valuable for shaping the
*composition* and risk profile of portfolios, by shifting balance
sheet strength and sector exposures—rather than for identifying a set of
systematically mispriced securities that earn higher expected returns.

### 6.7 Robustness checks

We conduct a battery of robustness checks, reported in detail in the
Online Appendix.
Here we summarise the main findings.

#### Alternative CSCI parameterisations.

We vary the comfort and outer thresholds
(θ¯k,θ¯k)(\underline{\theta}\_{k},\overline{\theta}\_{k}), the curvature parameters
γk\gamma\_{k} and δ\delta, and the geometric-mean weights wkw\_{k}.
Across these alternatives, the cross-sectional ordering of firms by CSCI
is highly stable: rank correlations between the baseline CSCI and
alternative specifications are close to one, and the set of
high-compliance and low-compliance names is essentially unchanged.
The qualitative shape of the compliance–performance frontier is also
robust.
Portfolios constructed from alternative CSCI specifications deliver
very similar excess returns, Sharpe ratios and drawdown profiles, with
differences that are well within sampling variability.

#### Alternative denominators and return definitions.

Using asset-based rather than market-capitalisation-based denominators
for leverage and liquidity ratios, or mixing the two in line with
specific standards, shifts the level of CSCI but not the ranking of firms.
Recomputing portfolio returns with alternative return definitions
(e.g. price-only versus total-return series) leaves annualised Sharpe
ratios and factor-adjusted alphas essentially unchanged.
The main conclusions are therefore not an artefact of the particular
ratio denominators or return conventions used in the baseline
implementation.

#### Sub-periods and crisis episodes.

We split the sample around major crisis episodes, focusing in
particular on the global financial crisis and the Covid-19 shock.
CSCI-threshold portfolios preserve their relative risk properties across
regimes: high-threshold portfolios consistently exhibit smaller
drawdowns and faster recoveries than both the conventional and the
binary Islamic benchmarks.
There is no evidence that the compliance–performance frontier is driven
by a single favourable sub-period.

#### Transaction costs and liquidity filters.

We subject the strategies to higher transaction-cost assumptions and
impose minimum price and volume filters to exclude the most illiquid
names.
The main portfolios remain implementable at realistic institutional cost
levels, and the shape of the compliance–performance frontier is
preserved, albeit with uniformly lower net Sharpe ratios as costs rise.

Taken together, these results support the paper’s central claim:
moving from binary pass/fail screens to a continuous, explainable CSCI
framework allows Islamic investors to explicitly trade off compliance
intensity against diversification and performance, without sacrificing
governance or transparency.
The next section discusses the implications of these findings for Islamic
asset managers and index providers, and for the broader literature on
non-pecuniary preferences in asset pricing.

## 7 Discussion and Conclusion

This paper proposes a continuous, explainable measure of Shariah
compliance, the Continuous Shariah Compliance Index (CSCI), and studies its
implications for portfolio construction and asset pricing.
Starting from the institutional architecture of leading Shariah
standards (AAOIFI, DJIM, FTSE, MSCI, S&P, and the Securities
Commission Malaysia), we show how their ratio-based screens can be
embedded in a unified, cardinal index that maps firms into the unit
interval.
CSCI is deliberately conservative: it anchors the comfort region at the
strictest thresholds observed across standards and penalises firms as
their leverage, liquidity, and impure income ratios approach the most
permissive bounds.
Sectoral screens are treated symmetrically through a continuous
penalisation of non-permissible revenue shares.

The empirical analysis yields three main findings.
First, CSCI meaningfully differentiates among firms that would otherwise
receive identical binary labels.
The cross-sectional distribution of CSCI is wide and highly skewed:
a large mass of firms are effectively excluded (CSCI near zero), but
there is also substantial variation within the admissible universe,
including among firms that pass standard index-provider screens.
Existing standards can be mapped to interior regions of the CSCI scale
with modest misclassification error, validating CSCI as a faithful
summary of current practice while revealing that “Shariah-compliant”
is not a single point, but an interval on a continuous spectrum.

Second, when CSCI is used as a portfolio design variable, it generates a
transparent compliance–performance frontier.
Tightening the minimum CSCI threshold raises average compliance,
strengthens balance-sheet conservatism, and reduces downside risk, but
only gradually reduces diversification.
Even at high thresholds, CSCI portfolios are not restricted to a handful
of defensive sectors: they retain meaningful exposure to technology,
healthcare, industrials and consumer names.
Relative to an emulated binary Islamic benchmark, CSCI portfolios trace
out a smooth locus in the space of Sharpe ratios, factor-adjusted
alphas, and maximum drawdowns, allowing investors to explicitly trade
off incremental compliance intensity against diversification and
expected return.

Third, CSCI does not appear to command a separate risk premium once
standard characteristics are controlled for.
In Fama–MacBeth regressions of one-month-ahead returns on CSCI, the
unconditional CSCI slope is economically small and statistically
indistinguishable from zero.
When we add size, and in further specifications book-to-market,
profitability, investment and momentum, the CSCI coefficient remains
economically tiny and statistically weak, with its sign not robust
across specifications.
From an asset-pricing perspective, CSCI therefore behaves like a
non-pecuniary attribute in the spirit of socially responsible or
ESG-style preferences: it re-arranges the composition and risk profile
of portfolios, rather than identifying a distinct source of systematic
mispricing.
This reinforces the interpretation of CSCI as a governance and portfolio
design tool, rather than as a stand-alone alpha signal.

### Implications for Islamic asset managers and index providers

For Islamic asset managers, CSCI offers an operational way to move beyond
pass/fail screening without abandoning the familiar ratio architecture.
Instead of a binary inclusion list, the manager observes a continuous
score that is grounded in existing standards and that can be explained
to Shariah boards in terms of leverage, liquidity, and impure income
exposure.
Portfolio construction can then be expressed in simple rules:
for example, “we require CSCI ≥0.7\geq 0.7 and tilt weights in proportion to
CSCI,” or “we maintain tracking error to a reference Islamic index while
increasing the portfolio’s average CSCI.”
Because CSCI is cardinal, such rules generate monotone, predictable
changes in both compliance and risk.

For index providers, CSCI suggests a natural extension of current
product lines.
Rather than offering a single Islamic index per region, an index family
could publish CSCI-enhanced variants that target different compliance
bands (e.g. “baseline Islamic,” “high-compliance,” “very
conservative”) or report CSCI statistics at the constituent level.
This would allow end-investors and Shariah boards to see not only
whether a firm passes, but how close it sits to the boundaries of
different standards, and how much tightening or loosening would be
required to accommodate alternative interpretations.

More broadly, the framework illustrates that Shariah governance and
modern portfolio technology are not in tension.
Once expressed on a continuous, explainable scale, compliance
constraints can be incorporated into optimisation, risk management and
performance attribution in exactly the same way as other portfolio
attributes.

### Limitations

The analysis is subject to several limitations.
First, CSCI builds on accounting and segment data that are noisy and
sometimes incomplete, especially for impure income and mixed-activity
firms.
Where the data do not allow an accurate decomposition of revenue
sources, the sectoral component of CSCI necessarily relies on proxies and
conservative assumptions.

Consistent with Box 1, CSCI is not intended to substitute for Shariah-board rulings or proprietary index-provider governance, and our empirical implementation should be read as an *emulated* screening framework constructed from public CRSP/Compustat inputs. In particular, provider-specific implementation details (e.g., revenue classification rules, treatment of special items, and proprietary sector mappings) are not fully observable, so exact membership replication is not guaranteed even when the underlying screening concepts coincide. Where constituent membership data are available, the framework can be externally validated by comparing classification accuracy and the implied continuous compliance gradient. Accordingly, we emphasize the framework’s value as a transparent, modular mapping from heterogeneous threshold rules into a continuous characteristic, rather than as a definitive authority on compliance status.

Second, the empirical implementation focuses on U.S. equities.
While this provides a deep, liquid universe with well-developed factor
datasets, the composition of Shariah-compliant opportunities, and the
interaction between CSCI and performance, may look different in emerging
markets or in markets with strong local Shariah governance traditions.

Third, like any backtest, the portfolio results are conditional on the
sample period, the choice of transaction cost assumptions, and the
particular mapping from standards into numerical thresholds.
Alternative parameterisations of the comfort and outer thresholds, or
different weightings of the ratio dimensions, produce CSCI scales that
are highly correlated with the baseline but not identical.
We document that our main findings are robust to such choices, but
recognise that a Shariah board or index committee might reasonably
prefer a slightly different calibration.

Finally, the paper treats CSCI as exogenous to expected returns.
In practice, firms’ choices regarding leverage, liquidity and business
activities are jointly shaped by their investor base, financing
constraints, and managerial preferences.
Understanding the dynamic interaction between investor demand for
high-CSCI portfolios and firms’ financing and investment policies is an
important question that we leave for future work.

### Directions for future research

The CSCI framework opens several avenues for further research.

A first direction is to integrate CSCI with explicit forecasting models.
In this paper, CSCI is used to structure universes and portfolio weights,
and expected returns are modelled via standard factor regressions.
Subsequent work can combine CSCI with machine learning forecasts of
relative performance, using CSCI both as a constraint (defining admissible
investments) and as an explanatory feature in non-linear return models.
This would allow researchers to ask whether the information set used to
construct CSCI is economically predictive in its own right, and how far
modern ML methods can enhance Shariah-compliant portfolio design.

A second direction is to extend the analysis beyond U.S. equities.
Applying CSCI in other regions, particularly in markets where Islamic
finance is systemically important, would help clarify how universal the
compliance–performance frontier documented here really is.
It would also permit a more granular study of interactions between
local Shariah standards, corporate governance regimes, and cross-border
capital flows.

Third, the continuous formulation lends itself to applications outside
outright screening and long-only portfolios.
For example, CSCI could be used to design capital-allocation policies in
multi-asset Islamic mandates (equities, sukuk, commodities), to control
counterparty risk in Shariah-compliant derivatives, or to price
structured products whose payoffs depend on the evolution of a
high-compliance equity basket.
In each case, the key benefit is the ability to express complex
constraints in a single, interpretable state variable.

More generally, the paper contributes to a broader literature on
non-pecuniary preferences in asset markets by showing how a
religion-based constraint, traditionally implemented through coarse
filters, can be expressed as a smooth, explainable index and integrated
into standard portfolio and asset-pricing frameworks.
If investors care about attributes that are not fully spanned by
traditional factors, continuous measures such as CSCI may provide a more
accurate representation of their opportunity set and of the trade-offs
they face.

In sum, moving from binary Shariah screens to a continuous, explainable
Continuous Shariah Compliance Index allows Islamic investors and index providers
to make explicit choices about how much compliance they want, what risks
they are willing to bear, and what performance they can reasonably
expect.
The empirical evidence suggests that it is possible to reconcile
stringent, transparent governance with competitive, risk-adjusted
returns, provided that compliance is treated as a graded, rather than a
binary, attribute.

## References

* Accounting and Auditing Organization for Islamic Financial
  Institutions, (2024)

  Accounting and Auditing Organization for Islamic Financial Institutions
  (2024).
  Shari’ah Standards.
  AAOIFI, Manama, Bahrain.
* Ajmi et al., (2014)

  Ajmi, A. N., Hammoudeh, S., Nguyen, D. K., and Sato, J. (2014).
  Co-movements between islamic and conventional stock returns: A
  wavelet analysis.
  Pacific-Basin Finance Journal, 28:241–259.
* Alnamlah et al., (2022)

  Alnamlah, A., Hassan, M. K., Alhomaidi, A., and Smolo, E. (2022).
  A new model for screening shariah-compliant firms.
  Borsa Istanbul Review, 22(1):10–23.
* Andersson et al., (2022)

  Andersson, E., Hoque, M., Rahman, M. L., Salah Uddin, G., and Jayasekeram, R.
  (2022).
  Esg investment: What do we learn from its interaction with stock,
  currency and commodity markets?
  International Journal of Finance & Economics.
* Ashraf et al., (2022)

  Ashraf, D. et al. (2022).
  The performance of Islamic versus conventional stocks during the
  COVID-19 shock.
  International Review of Financial Analysis.
* Asutay and co authors, (2022)

  Asutay, M. and co authors (2022).
  Macro-financial regimes and performance of shariah-compliant equity
  portfolios.
  Journal of International Financial Markets, Institutions and
  Money.
* Ayedh et al., (2019)

  Ayedh, A., Echchabi, A., Aziz, M. R. A., and Dandis, M. (2019).
  Shariah-compliant equity screening: A review and comparative
  analysis.
  ISRA International Journal of Islamic Finance, 11(1):5–24.
* Ben Rejeb and Arfaoui, (2019)

  Ben Rejeb, A. and Arfaoui, M. (2019).
  On the safe-haven and hedging properties of Islamic indexes: A
  comparison with conventional benchmarks.
  Pacific-Basin Finance Journal, 54:1–19.
* Berg et al., (2022)

  Berg, F., Kölbel, J., and Rigobon, R. (2022).
  Aggregate confusion: The divergence of esg ratings.
  MIT Sloan School of Management Working Paper.
* Berk and van Binsbergen, (2021)

  Berk, J. B. and van Binsbergen, J. H. (2021).
  The impact of impact investing.
  Journal of Financial Economics, 142(2):697–718.
* Charles et al., (2015)

  Charles, A., Darné, O., and Pop, A. (2015).
  Risk and dependence in islamic equity markets.
  Emerging Markets Review, 25:29–48.
* Christensen et al., (2022)

  Christensen, H. B., Serafeim, G., and Sikochi, A. (2022).
  Why is corporate virtue in the eye of the beholder? the case of esg
  ratings.
  The Accounting Review, 97(1):147–175.
* El-Gari, (2004)

  El-Gari, M. A. (2004).
  The Islamic funds industry: Developments and issues.
  Islamic Economic Studies, 11(2):1–48.
* Escobar-Saldivar et al., (2025)

  Escobar-Saldivar, L., Villarreal-Samaniego, D., and Santillán-Salgado, R. J.
  (2025).
  The effects of esg scores and esg momentum on stock returns and
  volatility: Evidence from u.s. markets.
  Journal of Risk and Financial Management.
* Fama and French, (1992)

  Fama, E. F. and French, K. R. (1992).
  The cross-section of expected stock returns.
  The Journal of Finance, 47(2):427–465.
* Friede et al., (2015)

  Friede, G., Busch, T., and Bassen, A. (2015).
  ESG and financial performance: Aggregated evidence from more than
  2000 empirical studies.
  Journal of Sustainable Finance & Investment, 5(4):210–233.
* FTSE Russell, (2022)

  FTSE Russell (2022).
  FTSE Shariah Global Equity Index Series Ground Rules.
  FTSE Russell, London.
* Gibson Brandon et al., (2019)

  Gibson Brandon, R., Krüger, P., and Schmidt, P. (2019).
  Esg rating disagreement and stock returns.
  Financial Analysts Journal, 75(4):104–127.
* Hakim and Rashidian, (2004)

  Hakim, S. and Rashidian, S. (2004).
  How costly is investors’ compliance with sharia?
  Journal of Investing, 13(4):77–84.
* Hameed and Muneeza, (2024)

  Hameed, A. and Muneeza, A. (2024).
  Enhancing shariah stock screening criteria: A proposed framework for
  evaluating shariah compliance degree.
  International Journal of Management and Applied Research,
  11(2):126–139.
* Haneef et al., (2015)

  Haneef, M., Mirakhor, A., et al. (2015).
  Islamic finance, ethics and shari’ah governance.
  Handbook of Ethics of Islamic Economics.
* Hasan, (2010)

  Hasan, Z. (2010).
  Regulatory framework of shari’ah governance system in Malaysia,
  Gulf cooperation council countries and the UK.
  Kyoto Bulletin of Islamic Area Studies, 3(2):82–115.
* Ho et al., (2014)

  Ho, C.-S. F., Rahman, N. A. A., Yusuf, N. H. M., and Zamzamin, Z. (2014).
  Performance of global Islamic versus conventional share indices:
  International evidence.
  Pacific-Basin Finance Journal, 28:110–121.
* Hou et al., (2015)

  Hou, K., Xue, C., and Zhang, L. (2015).
  Digesting anomalies: An investment approach.
  The Review of Financial Studies, 28(3):650–705.
* Jawadi et al., (2014)

  Jawadi, F., Jawadi, N., and Louhichi, W. (2014).
  Conventional and Islamic stock price performance: An empirical
  investigation.
  International Economics, 137:73–87.
* Khan et al., (2016)

  Khan, M., Serafeim, G., and Yoon, A. (2016).
  Corporate sustainability: First evidence on materiality.
  The Accounting Review, 91(6):1697–1724.
* Khatkhatay and Nisar, (2007)

  Khatkhatay, M. H. and Nisar, S. (2007).
  Shariah compliant equity investments: An assessment of current
  screening norms.
  Islamic Economic Studies, 15(1):47–76.
* MSCI, (2024)

  MSCI (2024).
  MSCI Global Islamic Indexes Methodology.
  MSCI Inc., New York.
* Nisar, (2015)

  Nisar, S. M. (2015).
  Shariah screening methodology for equities: A critical review.
  Journal of Islamic Economics, Banking and Finance,
  11(2):45–68.
* Parlak et al., (2024)

  Parlak, D., Yildiz, M. E., and Yilmaz, N. (2024).
  The relationship between shari’ah convergence and market-to-book
  value: A case study of firms in islamic countries.
  Borsa Istanbul Review, 24(2):398–405.
* Pástor et al., (2021)

  Pástor, L., Stambaugh, R. F., and Taylor, L. A. (2021).
  Sustainable investing in equilibrium.
  Journal of Financial Economics, 142(2):550–571.
* Pedersen et al., (2021)

  Pedersen, L. H., Fitzgibbons, S., and Pomorski, L. (2021).
  Responsible investing: The ESG-efficient frontier.
  Journal of Financial Economics, 142(2):572–597.
* Rana and Akhter, (2015)

  Rana, M. and Akhter, W. (2015).
  Performance of islamic and conventional stock indices: Empirical
  evidence from an emerging market.
  Journal of Islamic Business and Management, 5(1):17–34.
* Rizaldy and Ahmed, (2019)

  Rizaldy, M. R. and Ahmed, H. (2019).
  Islamic legal methodologies and shariah screening standards:
  Application in the indonesian stock market.
  Thunderbird International Business Review, 61(5):733–749.
* Rizwan et al., (2022)

  Rizwan, M. S., Ashraf, D., and Fakhfekh, M. (2022).
  Islamic equity investments and the covid-19 pandemic: Evidence from
  global sectoral indices.
  Pacific-Basin Finance Journal, 72:101712.
* Sandwick, (2019)

  Sandwick, J. (2019).
  Islamic asset management: An industry survey and discussion of key
  issues.
  Journal of Islamic Banking and Finance.
* Sani and Othman, (2013)

  Sani, N. and Othman, R. (2013).
  Shariah-compliant securities screening: A comparison between the
  kuala lumpur shariah index and international index providers.
  Global Review of Islamic Economics and Business, 1(2):98–120.
* Securities Commission Malaysia, (2013)

  Securities Commission Malaysia (2013).
  Revised shariah screening methodology for shariah-compliant
  securities.
  Shariah Advisory Council of the Securities Commission Malaysia,
  Guidance Document.
  Kuala Lumpur. Available from the Securities Commission Malaysia
  website.
* S&P Dow Jones Indices, (2024)

  S&P Dow Jones Indices (2024).
  S&P Shariah Indices Methodology.
  S&P Dow Jones Indices, New York.
* Zainudin et al., (2014)

  Zainudin, N., Miskam, S., and Sulaiman, M. (2014).
  Revised shariah screening methodology for shariah-compliant
  securities in malaysia.
  International Journal of Business, Economics and Law,
  4(1):24–33.
* Zakri, (2018)

  Zakri, R. M. (2018).
  Shariah screening methodology: A comparative study of the main index
  providers.
  International Journal of Islamic and Middle Eastern Finance and
  Management, 11(3):470–488.