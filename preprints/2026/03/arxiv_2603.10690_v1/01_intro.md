---
authors:
- Carlos Canon
- Eddie Gerba
- Jozef Barunik
doc_id: arxiv:2603.10690v1
family_id: arxiv:2603.10690
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'When David becomes Goliath: Repo dealer-driven bond mispricing'
url_abs: http://arxiv.org/abs/2603.10690v1
url_html: https://arxiv.org/html/2603.10690v1
venue: arXiv q-fin
version: 1
year: 2026
---


Carlos Cañón
[carlos.canonsalazar@bankofengland.co.uk](2603.10690v1/carlos.canonsalazar@bankofengland.co.uk)
Bank of England & King’s College London

Eddie Gerba
[eddie.gerba@bankofengland.co.uk](2603.10690v1/eddie.gerba@bankofengland.co.uk)
Bank of England & LSE

Jozef Baruník
[barunik@fsv.cuni.cz](2603.10690v1/barunik@fsv.cuni.cz)
Charles University & Czech Academy of Sciences

###### Abstract

This paper studies the impact of funding market frictions on bond prices and market-wide liquidity. Using proprietary transaction‑level data on all gilt‑backed repo and reverse-repo trades, we demonstrate how the market power of individual dealers and their linkages generate frictions. Specifically, we show that frictions related to market power account for between 0.5 and 1.3 percentage points of bond yield deviation, while the transmission of heterogeneously persistent shocks between dealers accounts for between 2 and 4 percentage points of yield deviation.

Keywords: Market power, Inefficiencies, Mispricing, Market liquidity.
  
JEL Codes: G14, G21, G22, G23.

Acknowledgments: We have benefited from detailed comments from Tobias Dieler (discussant), Hillary Stein (discussant), Robert Czech, Nick Vause, Patrick Coen, Yiming Ma. We also thank Marco Bardoscia, Semih Uslu, Jorge Florez, Karoll Gomez, Rodrigo Guimaraes, Petros Katsoulis, Gabor Pinter, Andres Murcia, Matt Roberts-Sklar, Laura Silvestri, and seminar participants at Bank of England, Banco de la Republica, Charles University, Boston CEBRA 2025, 2025 Bristol Financial Markets Conference, Oxford IFABS 2025, Rome EARIE 2023, and Portsmouth MMF 2023 for valuable insights. The views expressed in this paper are those of the authors and do not reflect the views of the Bank of England, the PRA, or any of its committees.

## 1 Introduction

At what point does the structure of funding markets become apparent in government bond prices? Episodes such as the ‘dash for cash’ in March 2020 suggest that stresses in repo markets can quickly leak into sovereign bond markets, causing price fluctuations and reduced liquidity. However, there is little systematic evidence on the mechanisms through which funding-market frictions lead to bond mispricing and impaired market liquidity. Most research focuses either on aggregate liquidity and funding conditions or on the microstructure of individual markets. Rarely does it combine micro-level measures of dealer behaviour with bond-level mispricing and a market-wide liquidity metric.

In this paper, we examine how market power and dealer linkages in the UK repo market may shape gilt prices and market-wide liquidity. Our focus is on the core, dealer-centric structure of the market, whereby a limited number of bank dealers facilitate funding between a wide range of non-bank financial institutions and central counterparties using UK government bonds as collateral. Using proprietary, transaction-level data on all repo and reverse repo trades involving gilts between 2016 and 2022, combined with a cross-section of gilt yields, we quantify the impact of dealer market power, its dispersion across dealers, and the transmission of shocks through the dealer network as the three channels impacting bond mispricing and market liquidity. Although our data is UK specific, the core mechanisms we identify are common for all large money markets.

Our approach involves two steps. First, we measure market power specific to each dealer in both the repo and reverse-repo segments. Using a structural demand-and-supply framework that treats each dealer as supplying a differentiated funding ‘product’ to non-dealers, we estimate dealer-level markups and markdowns and recover markups and markdowns from the implied Lerner indices. To address endogeneity in repo rates, quantities and relationship-trading variables, we exploit the granularity of the panel data to construct instrumental variables based on idiosyncratic shocks at the dealer–non-dealer level, as described by Gabaix and Koijen ([2024](#bib.bib37)). Second, we embed dealers and non-dealers in a dynamic network. Using a time-varying VAR and persistence-based variance decompositions, we construct global dealer factors that capture the proportion of transitory and persistent shocks originating from a subset of major dealers and transmitted to the rest of the system. These factors quantify the extent to which the market as a whole is exposed to shocks affecting the most influential dealers.

We then link these funding-market primitives to gilt pricing and market liquidity. At the bond level, we measure mispricing as the absolute deviation of each gilt’s yield from a smooth term-structure benchmark. At the market level, we use the “noise” index proposed by Hu et al. ([2013](#bib.bib43)) as a proxy of overall market liquidity. By regressing bond-level mispricing and market liquidity on: i) dealer markups and markdowns, ii) their dispersion across dealers, and iii) the corresponding global dealer factors, we can decompose bond price distortions and liquidity into components attributable to different funding-market frictions.111We control for bond characteristics, monetary policy and other macro-financial covariates.

Our main findings are threefold. First, dealer-specific market power in the reverse-repo and repo segments leads to significant mispricing of gilts (channel A): conditional on controls, frictions related to markups and markdowns explain between 0.5 and 1.3 percentage points of bond yield deviations along the curve. Second, the heterogeneity of market power among dealers (channel B) and the transmission of shocks through the dealer network (channel C) are equally important. Our time-varying global dealer factors explain an additional 2–4 percentage points of mispricing. These are particularly strong effects for longer-maturity gilts. Taken together, these funding-market frictions account for between 2.5 and 5.3 percentage points of gilt yield deviation from the term-structure benchmark. Third, the same mechanisms shape market-wide liquidity. Higher markdowns and their dispersion, as well as stronger exposure to persistent dealer shocks in the reverse repo segment, are associated with significantly worse market liquidity. In contrast, the repo segment plays a more benign role. These effects are nonlinear and become especially pronounced during periods of stress, such as the ’dash for cash’ period.

These results contribute to several areas of research. First, it makes a contribution to the literature on mispricing (Greenwood and Vayanos, [2014](#bib.bib39); Lewis et al., [2021](#bib.bib52)) that attributes persistent price deviations to frictions in core markets (such as the bond, repo and foreign exchange (FX) swap markets), to central bank decisions, or to changes in intermediation capacity. Pelizzon et al. ([2025](#bib.bib60)) show that Central Banks can induce bond-level mispricing through a collateral scarcity channel associated with the implementation of quantitative easing, while Kerssenfischer and Helmus ([2024](#bib.bib50)) argue that outages in the futures market produce bond-level mispricing through hedging and price signalling channels. Brauning and Stein ([2025](#bib.bib15)); Barbeiro et al. ([2024](#bib.bib6)) and Stein and Wallen ([2025](#bib.bib65)) discuss how the reduction in intermediation capacity affects asset prices in foreign exchange and Treasury markets. From Brunnermeier and Pedersen ([2008](#bib.bib17)); Huh and Infante ([2021](#bib.bib46)), we are aware of the tight relationship between market and funding liquidity (Bai et al. ([2018](#bib.bib5))), and we provide evidence that frictions in the core funding market arising from: i) dealer market power, ii) heterogeneous market power distribution across dealers, and iii) network-driven shocks translate directly into mispricing at the level of individual bonds and market-wide liquidity.

Second, we contribute to the expanding body of research on the microstructure of the repo market by demonstrating that the ramifications of dealer dominance extend beyond the transmission of policy rates to the pricing and liquidity of the underlying collateral (Duffie et al., [2005](#bib.bib29); Afonso et al., [2014](#bib.bib1); Mancini et al., [2016](#bib.bib56); Di Maggio et al., [2017](#bib.bib27)). A close reference is Eisenschmidt et al. ([2024](#bib.bib32)), who show how the market power of dealers in the European repo market impedes the pass-through of ECB’s policy rate. Based on the notion that most repo trades are conducted over-the-counter by a very small number of dealers, these dealers have significant market power. The result is an imperfect and heterogeneous pass-through from interdealer repo rates to OTC repo rates (similar to the findings in Huber ([2023b](#bib.bib45)) but for the US), with the interdealer repo rate in turn determined by the central bank’s deposit facility rate and the value of collateral. While undoubtedly innovative and insightful, our paper goes beyond that study in three ways. First, we take a much broader perspective by distinguishing market power in the repo to that of reserve repo segment, both in prices and volumes, and contrast individual market power with global dealer factors. Second, we link dealer-level frictions to market-level phenomenon through the lens of market-wide liquidity. Third, and perhaps most fundamentally, we examine market power and trading behaviour as inextricably linked to market pricing in the bond market.

Third, we contribute to the UK-specific literature on gilt and repo markets, which emphasises their role in providing liquidity and ensuring financial stability. Our paper is particularly related to Huser et al. ([2024](#bib.bib47)); Coen et al. ([2024](#bib.bib21)) as we study the UK repo market. Huser et al. ([2024](#bib.bib47)) provides a detailed description of what happened during the Dash-for-Cash period, and Coen et al. ([2024](#bib.bib21)) follows a structural approach to highlight that collateral demand is an important driver in the repo market. Our paper contributes in two dimensions. One, we assess the impact of dealer-level market power in both repo segments, as well as transitory/persistent dealer factor shocks on repo prices and quantities. Two, we show that dealer-level frictions explain bond-level mispricing in the gilt market.

The remainder of the paper is structured as follows. Section 2 outlines our hypotheses and reasoning. In Section 3, we describe our data, present some stylized facts about the market, and outline our identification approach. Section 4 discusses our core results on the three frictions and their spillovers. Further details and results are also available in the Online Appendix. Concluding remarks wrap up the paper in Section 5.

## 2 Hypotheses

Dealers in the UK repo market may hold market power on non-dealers due to their access to central counterparty clearing services. Thus, we expect the traditional deadweight loss to operate in the form of lower volumes and higher funding costs.222Huber ([2023a](#bib.bib44)); Eisenschmidt et al. ([2022](#bib.bib31)) document the impact of market power for the US and EUR repo markets. We also expect to find evidence of losses associated with the dispersion of market power (across dealers), which is reflected in market-wide aggregate distortions (Boar and Midrigan ([2019](#bib.bib13)); Brooks et al. ([2021](#bib.bib16)); David and Venkateswaran ([2019](#bib.bib26)); Haltiwanger et al. ([2018](#bib.bib40)); Liang ([2023](#bib.bib54)); Weinberger ([2020](#bib.bib69))). Because the repo market is closely related to other core markets, Brunnermeier and Pedersen ([2008](#bib.bib17)), markups and markdowns in the repo market could spill over to individual collateral acquired in the bond and reverse repo markets, and to market-wide measures of market liquidity. We will investigate these next.

The effect of repo market markups and markdowns is mediated by several factors. First, there is ample evidence of relationship lending in various OTC markets, e.g. Jurkatis et al. ([2022](#bib.bib48)); Di Maggio et al. ([2017](#bib.bib27)); Hau et al. ([2021](#bib.bib42)); Afonso et al. ([2014](#bib.bib1)), yet it is unclear whether stronger relationships counterbalance dealers’ market power. Second, market power could operate through quantities and prices, and it is empirically interesting to measure this. Third, market power could operate differently across financial sector segments, i.e. hedge funds, asset managers, insurance companies, and pension funds. Finally, since we know the identity of non-dealers, we can test whether non-dealers active in both the repo and reverse repo segments receive different terms of trade vis-a-vis non-dealers active in only one segment.

Let us, next, outline our reasoning for channel A. The first hypothesis focuses on the impact of dealer-specific market power on repo market quantities and prices. Concretely, we want to understand how market power operates at individual repo transaction level, and the role of other factors, e.g. relationship lending, sector specific differences, and common shock to main dealers, in attenuating the impact on quantities or prices.

###### Hypothesis 1.

Dealer-specific market power (markup and markdown) creates frictions that affect both repo prices and volumes.

The second dimension focuses on dealer-specific market power spillovers. From the repo segment, non-dealers could face difficulties in accessing arbitrage capital, which should increase mispricing, e.g. Hu et al. ([2013](#bib.bib43)), and deteriorate market liquidity. From the reverse repo segment, non-dealers could face difficulties in acquiring gilts in exchange for funding, contributing to search frictions in the gilt market and ultimately increasing mispricing, e.g. Duffie et al. ([2015](#bib.bib30)), also deteriorating market liquidity.

###### Hypothesis 2.

Dealer-specific market power (markup and markdown) impacts individual gilts, bond-market liquidity, and (financial) market-wide liquidity.

The literature on misallocation due to market power emphasises that this specific friction does not depend on repo dealers holding positive markups and markdowns, but is also related to how market power is distributed across dealers, Syverson ([2024](#bib.bib66)).333Another way of framing it is that the welfare loss is proportional to the wedge between marginal revenue and marginal cost. We evaluate this interpretation empirically and the results hold. The next hypothesis focuses on this channel B.

###### Hypothesis 3.

There is a friction due to the distribution/dispersion of market power across dealers (markups and markdowns), which impacts bond-level mispricing and market-wide liquidity.

Next, we argue that common repo dealer shocks may generate similar spillovers.444The OTC segmentation literature is closely related as it predicts how dealers will segment clients, e.g. based on their characteristics, trading patterns, etc. The literature remains inconclusive on the determinants of dealer heterogeneity. Sambalaibat ([2023](#bib.bib63)) argues that the largest dealers in an OTC market will specialise in the most active non-dealers, and Lewis et al. ([2021](#bib.bib52)) shows empirically that this intuition can be extended to other asset classes. There are authors who assume away any dealer heterogeneity, e.g. Farboodi et al. ([2022](#bib.bib35)); Wang ([2021](#bib.bib67)), or who explain it on the basis of ex ante factors, e.g. Üslü ([2019](#bib.bib72)); Eisfeldt et al. ([2022](#bib.bib33)). In any case, assuming dealer heterogeneity, quantity (prices) will increase (decline) as core traders become more interconnected. The next hypothesis focuses on channel C: How do common persistent and transitory shocks to repo dealers shape individual bonds, bond market-makers, and market-wide liquidity? If collateralised funding markets are short-term in nature, we should expect common persistent shocks to have powerful spillovers to the bond market, and to market-wide aggregates.

###### Hypothesis 4.

Persistent shocks to repo dealers matter for bond-level mispricing and market-wide liquidity.

So far, the stated hypotheses describe three mechanisms that relate repo dealers to individual gilt-, bond market-, and (financial) market-wide liquidity. The final hypothesis focuses on their interaction (channels A+B+C). The first two mechanisms, associated with dealer-specific market power, are known to be interrelated but operate under very specific conditions, i.e. if all dealers have the same level of market power, then the second mechanism disappears. The last mechanism is more general, as it zooms in on heterogeneously persistent shocks, that are not uniquely associated with market power, and which can potentially be the main driver of spillovers.

###### Hypothesis 5.

The combined effects of the three frictions on bond yield deviations and market liquidity are sizeable and larger than any of those individually.

## 3 Empirics

### 3.1 Data

We use proprietary transaction-level data for the UK repo market between January 2016 and January 2022. As shown below, we focus on the subsample of transactions utilising gilts as collateral to avoid dealing with asset classes that are illiquid relative to gilts and to avoid biasing the formation of relationship trading based on ownership of illiquid assets. Another reason for focusing on gilt repo is that our analysis on mispricing only uses these securities. The dataset includes all repo and reverse repo transactions between dealers and non-dealers, and between dealers and CCPs. A detailed description of the structural features of the UK repo market can be found in Online Appendix [A](#A1 "Appendix A The UK Repo Market ‣ When David becomes Goliath: Repo dealer-driven bond mispricing").

Table 1: Summary statistics for the repo market by type of transaction (repo vs. reverse repo) between dealers and non-dealers. Our sample only uses gilts as collateral. Volumes are expressed in 10710^{7} of sterling and the interest rate spread (in percentage points) is relative to the BoE reference rate.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Median | Mean | SD | Min | Max | N |
|  | Repo | | | | | |
| Volume | 3.12 | 4.59 | 4.41 | 0.11 | 27.40 | 335601 |
| Rate spread | -0.01 | -0.01 | 0.09 | -0.75 | 0.77 | 335601 |
|  | Reverse | | | | | |
| Volume | 4.50 | 6.51 | 7.26 | 0.11 | 75.00 | 350609 |
| Rate spread | -0.08 | -0.10 | 0.08 | -0.79 | 0.64 | 350609 |

Table [1](#S3.T1 "Table 1 ‣ 3.1 Data ‣ 3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") presents summary statistics on repo market data by type of transaction between dealers and non-dealers. The median transaction is £31 million at a repo rate of 0.01 pp below the BoE reference rate when dealers provide liquidity in exchange for collateral, and £45 million at a repo rate of 0.08 pp below the BoE reference rate when dealers receive liquidity in exchange for collateral. Further, summary statistics by type of transaction between dealers and CCPs (Table [F.1](#A6.T1 "Table F.1 ‣ Appendix F Tables ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") in Online Appendix [F](#A6 "Appendix F Tables ‣ When David becomes Goliath: Repo dealer-driven bond mispricing")) shows the median transaction is £23 million with a repo rate of 6 pp below the BoE reference rate when dealers provide liquidity in exchange for collateral and £22 million with a repo rate of 6 pp below the BoE reference rate when dealers receive liquidity in exchange for collateral.

To examine the impact of repo dealer market power on mispricing of gilts, we use ISIN-level metrics of mispricing, volatility, liquidity, residual maturity, and a set of bond-level characteristics. The mispricing metric is the difference between the bond yield and a daily (spline) benchmark yield constructed using all gilts available in the market at the time.555Later, we will construct the market liquidity proxy, following Hu et al. ([2013](#bib.bib43)), by adding the square of the mispricing of the individual bonds.

Table 2: Summary statistics of the gilts market by residual maturity. Mispricing is the difference between the yield and the benchmark yield, liquidity is the ask/bid spread, volatility is the high/low spread. Market liquidity is constructed according to Hu et al. ([2013](#bib.bib43)).

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Median | Mean | SD | Min | Max | N |
| 3yr - 7yr | Mispricing | -0.11 | 0.10 | 2.18 | -4.92 | 6.61 | 7566 |
|  | Duration | 5.28 | 5.32 | 1.22 | 2.86 | 7.66 | 7566 |
|  | Liquidity | 0.03 | 0.04 | 0.02 | 0.01 | 0.26 | 7566 |
|  | Volatility | 0.24 | 0.28 | 0.23 | 0.05 | 6.87 | 7566 |
| 8yr - 19yr | Mispricing | 0.20 | 0.12 | 1.48 | -5.24 | 4.74 | 10810 |
|  | Duration | 9.94 | 10.69 | 2.60 | 6.73 | 18.55 | 10810 |
|  | Liquidity | 0.05 | 0.06 | 0.04 | 0.01 | 0.54 | 10810 |
|  | Volatility | 0.66 | 0.77 | 0.48 | 0.15 | 11.00 | 10810 |
| 20yr or more | Mispricing | 0.03 | -0.16 | 1.27 | -5.19 | 3.46 | 14309 |
|  | Duration | 22.56 | 22.90 | 4.95 | 14.64 | 37.31 | 14309 |
|  | Liquidity | 0.11 | 0.12 | 0.06 | 0.03 | 0.57 | 14309 |
|  | Volatility | 1.57 | 1.87 | 1.18 | 0.33 | 37.94 | 14309 |
| Total | Mispricing | 0.066 | 0.00 | 1.60 | -5.24 | 6.61 | 32685 |
|  | Duration | 13.40 | 14.79 | 8.27 | 2.86 | 37.31 | 32685 |
|  | Liquidity | 0.07 | 0.08 | 0.06 | 0.01 | 0.57 | 32685 |
|  | Volatility | 0.86 | 1.14 | 1.07 | 0.05 | 37.94 | 32685 |
| Market Liquidity |  | 1.73 | 1.92 | 0.55 | 1.23 | 3.62 | 1470 |

Table [2](#S3.T2 "Table 2 ‣ 3.1 Data ‣ 3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") shows summary statistics for the gilt market. The median gilt has a positive mispricing of 0.07 pp. However, when zooming in on the three different residual maturity buckets, only short-end gilts have a negative mispricing of 0.11 pp. The measures of all other bond characteristics (duration, liquidity and volatility) increase as residual maturity increases.

### 3.2 Stylized facts

Table [3](#S3.T3 "Table 3 ‣ 3.2 Stylized facts ‣ 3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") shows the number of potential counterparts that could form a trading relationship. While we observe a fixed number of dealers, the number of non-dealers can change depending on the segment. For example, in the repo segment we have 3380 different non-dealers belonging to 727 different families, and in the reverse segment these numbers are 2004 and 682 respectively.666By family we mean a financial institution that could offer different investment vehicles to end-investors. For example, imagine a large asset management firm offering many individual funds to retail investors. In our data, individual non-dealers are each of these funds and the asset management firm is the family. As we explain in the paper, our analysis is done at the family level. Our data is granular enough to identify non-dealers that operate in both segments simultaneously with the same dealer.

Table 3: Dealer (D), Non-Dealers (D), Family of Non-Dealers, average number of counterparts and average counterparty dependence in our sample.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | No Counter. | |  | % Funding | |
|  | Repo | Reverse Repo |  | Repo | Reverse Repo |  | Repo | Reverse Repo |
| Dealers | 15 | 15 |  | 9.46 | 6.77 |  | 41.95% | 46.13% |
| Non-Dealers | 3380 | 2004 |  | 2.73 | 2.93 |  | 52.39% | 60.04% |
| Family of ND | 727 | 682 |  |  |  |  |  |  |
| Dyads D/ND | 5803 | 3484 |  |  |  |  |  |  |
| Dyads D/Family | 2112 | 1767 |  |  |  |  |  |  |

Table [3](#S3.T3 "Table 3 ‣ 3.2 Stylized facts ‣ 3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") shows the number of dyads in our sample, which is the unit of analysis for our panel estimation. For the repo segment, we observe 2112 dealer/family non-dealer dyads, and for the reverse repo segment, this number decreases to 1767. If we zoom in on non-dealers that are active in both segments simultaneously, the number of dyads falls to 1048. Our analysis is at the non-dealer family level, so we drop the word "family" and use non-dealers.

#### Dealers hold more counterparts than non-dealers

Table [3](#S3.T3 "Table 3 ‣ 3.2 Stylized facts ‣ 3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") further shows the number of counterparts for dealers and non-dealers. On average, a non-dealer has fewer counterparts than a dealer. While for dealers this number fluctuates around ten counterparts, for non-dealers it does not reach three counterparts. This feature is not unexpected as it’s also observed in other OTC markets.

#### OTC vs inter-dealer segments

Dealers are active in both the OTC and inter-dealer markets on a daily basis. As emphasized above, the inter-dealer market accounts for a large proportion of daily volume, e.g. around 70%70\%. There are also more fundamental differences. While virtually all transactions in the inter-dealer segment are overnight, in the OTC segment this share does not reach 50% and the remaining share is made up of transactions with maturities of less than one week or one month (Table [F.2](#A6.T2 "Table F.2 ‣ Appendix F Tables ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") in Appendix [F](#A6 "Appendix F Tables ‣ When David becomes Goliath: Repo dealer-driven bond mispricing")). Dealers’ use of the inter-dealer market is also closely related to their holdings. While dealers use, on average, three different gilts in the OTC segment, they use ten times as many in the inter-dealer segment (Table [F.2](#A6.T2 "Table F.2 ‣ Appendix F Tables ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") in Appendix [F](#A6 "Appendix F Tables ‣ When David becomes Goliath: Repo dealer-driven bond mispricing")).

In addition, Figure [1](#S3.F1.3 "Figure 1 ‣ OTC vs inter-dealer segments ‣ 3.2 Stylized facts ‣ 3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") shows a negative relationship between the number of unique gilts and the size and duration of repo (as well as reverse repo) transactions. Repo transactions are, on average, larger and longer when dealers operate with fewer gilts, and this holds for reverse repo transactions as well. We interpret this as evidence of inventory constraints.

Figure 1: Unique gilts vs Mean Volume & Mean ResMaturity at OTC segment for both repo and reverse repo. Note the volumes are divided by 10610^{6}.

![Refer to caption](2603.10690v1/Figures/figure1_scatter.png)

#### Sector heterogeneity in OTC segment

Figures [2(a)](#S3.F2.sf1 "In Figure 2 ‣ Sector heterogeneity in OTC segment ‣ 3.2 Stylized facts ‣ 3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") - [2(b)](#S3.F2.sf2 "In Figure 2 ‣ Sector heterogeneity in OTC segment ‣ 3.2 Stylized facts ‣ 3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") show the historical volume and the repo spread. Hedge funds and other funds are the two most important sectors in the OTC segment, and the spread to the bank rate is usually negative. In contrast, pension funds have a smaller but still relevant presence, yet their spread is positive.

Figure 2: Log volume and repo rate spread using the non-dealer dataset with daily frequency. The spread is the difference between the repo rate and the reference rate.

(a) Volume

![Refer to caption](2603.10690v1/x1.png)

(b) Rate Spread

![Refer to caption](2603.10690v1/x2.png)

#### Existence of global dealer factors

Figures [3(a)](#S3.F3.sf1 "In Figure 3 ‣ Existence of global dealer factors ‣ 3.2 Stylized facts ‣ 3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") and [3(b)](#S3.F3.sf2 "In Figure 3 ‣ Existence of global dealer factors ‣ 3.2 Stylized facts ‣ 3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") depict the global dealer factors for both transaction volume and spread on both the repo and reverse repo segments, formed in response to transitory and persistent shocks. Note that we select 5 dealers that explain 40% of all funding in both the repo and reverse repo markets (note that these may be different), and we can see that the total contribution of this subset of dealers is between 8% and 18% (as the sum of transitory and persistent factors). Note that the global factor derived from spread shocks is more volatile.

Figure 3: Global dealer factors derived from both transitory and persistent shocks to repo and reverse repo volumes and spreads.

(a) Volume

![Refer to caption](2603.10690v1/x3.png)

(b) Rate Spread

![Refer to caption](2603.10690v1/x4.png)

### 3.3 Main Variables

#### Market Power

We use markups and markdowns as a proxy for market power. Dealers operate in the repo segment providing liquidity in exchange for collateral, and in the reverse repo segment, absorbing liquidity also in exchange for collateral. The repo dealers we focus on also have an important role as market makers in the gilt market, and have access to the repo market inter-dealer segment. As non-dealers operate with a small number of dealers, the latter can exercise their bargaining power in both repo segments in their favour.

The markup in the repo segment is a function of the marginal cost of production, which is not observed in our data.777A common practice in reduced-form approaches, see Cañón et al. ([2022](#bib.bib19)), is to use dealers’ balance sheet data and estimate their cost function, and thus obtain the marginal cost. This approach is not feasible in our setup due to data availability. In the context of price competition with differentiated products, a firm’s optimal pricing rule in a symmetric equilibrium equates the markup to the inverse of the elasticity of demand for liquidity. Our strategy is to back out the dealer-level markup using a simple structural model of supply and demand, following the standard demand estimation literature in empirical industrial organisation.

For the reverse repo segment, e.g. when dealers absorb liquidity in exchange for collateral, the market power proxy (markdown) is instead a function of the marginal revenue of liquidity, see Manning ([2003](#bib.bib57)), but again unobservable. Analogous to equation [C.2](#A3.E2 "In Appendix C A stylized structural model for markups and markdowns ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), it’s possible to use a one-to-one relationship between the markdown and the inverse elasticity of liquidity supply, see Yeh et al. ([2022](#bib.bib70)).

The estimation is done in two steps.888See Online Appendix [C](#A3 "Appendix C A stylized structural model for markups and markdowns ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") for details. First, we construct supply and demand models for short-term funding and estimate the demand (supply) coefficients using our dataset of dealer/non-dealer transactions. We then use the coefficients to compute own-price elasticities and then apply the price-cost markup (or marginal revenue-price markdown) formula derived from the model to back out product-level markups (markdowns) and compute a proxy for dealer-level market power.

The optimal pricing rule allows us to derive a markup and a markdown for each dealer in each period tt. In Online Appendix [C](#A3 "Appendix C A stylized structural model for markups and markdowns ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") we explain the procedure in detail.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | M​a​r​k​u​pd​t≡rd​t−cd​trd​t=−1ηd​t,\displaystyle Markup\_{dt}\equiv\frac{r\_{dt}-c\_{dt}}{r\_{dt}}=-\frac{1}{\eta\_{dt}}, | M​a​r​k​d​o​w​nd​t≡m​r​e​vd​t−rd​trd​t=1νd​t\displaystyle Markdown\_{dt}\equiv\frac{mrev\_{dt}-r\_{dt}}{r\_{dt}}=\frac{1}{\nu\_{dt}} |  | (1) |

where rd​tr\_{dt} is the average repo rate of dealer dd at time tt, cd​tc\_{dt} is the marginal cost of dealer dd at time tt, m​r​e​vd​tmrev\_{dt} is the marginal revenue of liquidity of dealer dd at time tt. Finally, ηd​t\eta\_{dt} (νd​t\nu\_{dt}) is the elasticity of demand (supply).

The supply and demand framework for short-term funding, though stylized, incorporates several key features observed in the data. On the supply side, a small number of dealers provide liquidity and hold inventories of gilts with varying characteristics, while competing aggressively to attract non-dealer. On the demand side, non-dealers typically operate with a limited set of dealers and are assumed to transact with only one dealer per day. Their choice of dealer depends on transaction characteristics (the repo rate and maturity), collateral characteristics (the market value of the gilt), and dealer-specific liquidity management, proxied by the number of transactions conducted with each dealer in the past month. Our measures of market power capture dealers’ ability to set prices that deviate from the benchmark of perfect competition, without conflating this with search, switching, or transaction costs.

#### Dealer Factors

Transaction volumes and spreads between dealers and non-dealers in the UK repo market (for both repo and reverse repo) can be altered by shocks between these market participants, which may form an asymmetric network of trading relationships between dealers. We are interested in measuring such a network, in particular, the extent to which dealers that drive most of the volume matter for the rest of the market. In addition, we want to identify such relationships formed by shocks of heterogeneous persistence, namely transitory and persistent shocks transmitted between dealers and non-dealers. More specifically, our global dealer factor will measure the percentage share of shocks from selected dealers that contribute to the overall market variation. In other words, we will measure the extent to which all dealers are influenced by selected dealers relative to the shock transmission across all dealers and non-dealers. Later, we will be interested in exploring how increasing the intensity of the global dealer factor affects volumes, spreads, gilt mispricing, and market-wide liquidity.

Formally, we consider a N×NN\times N dimensional system with N=ND+NN​DN=N^{D}+N^{ND} number of dealers (NDN^{D}) and non-dealers (NN​DN^{ND}) who can transmit shocks to each other throughout the system. To quantify the influence of shocks, we draw on the literature (Diebold and Yilmaz, [2012](#bib.bib28)), which notes that variance decompositions are useful for tracking how shocks affect the future variation of variables within a system, and are therefore a natural choice for inferring shock transmission. Following Baruník and Kr̆ehlík ([2018](#bib.bib9)); Barunik and Ellington ([2024](#bib.bib8)), who further work with time dynamics as well as heterogeneous persistence of shocks, we will define the global dealer factors that vary smoothly over time and are inferred from shocks of heterogeneous persistence. Specifically, these shocks will be of transitory (t​rtr) or persistent (p​e​rper) nature, and we will collect them in a time-varying variance decomposition matrix θt,d\theta\_{t,d} identified from the underlying TVP-VAR model at a given level of persistence d∈{t​r,p​e​r}d\in\{tr,per\} as detailed in the appendix [D](#A4 "Appendix D Global Dealer Factors: Estimation ‣ When David becomes Goliath: Repo dealer-driven bond mispricing").

Specifically, θt,d\theta\_{t,d} holds information about how much of the future variation of a variable jj is due to a shock with persistence dd to the variable kk at a given time. This is important because the influence of shocks can evolve smoothly over time.

The impact of a selected set of dealers D​s​e​lDsel on the rest of the dealers in the system, relative to all other shocks that may be transmitted between dealers and non-dealers, then forms our global dealer factor with a given persistence dd as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒢​l​o​b​a​l​ℱt,dD​s​e​l=∑j=1j≠kk∈D​s​e​lND[θ^t,d]j,k/∑j,k=1ND+NN​D[θ^t]j,k,\mathcal{G}lobal\mathcal{F}\_{t,d}^{Dsel}=\displaystyle\sum\_{\begin{subarray}{c}j=1\\ j\neq k\\ k\in Dsel\end{subarray}}^{N^{D}}\Big[\widehat{\theta}\_{t,d}\Big]\_{j,k}\Bigg/\displaystyle\sum\_{j,k=1}^{N^{D}+N^{ND}}\Big[\widehat{\theta}\_{t}\Big]\_{j,k}, |  | (2) |

where D​S​e​lDSel is the set of selected dealers whose importance we want to measure. Note that θ^t=θ^t,t​r+θ^t,p​e​r\widehat{\theta}\_{t}=\widehat{\theta}\_{t,tr}+\widehat{\theta}\_{t,per} and therefore 𝒢​l​o​b​a​l​ℱt,dD​s​e​l∈[0,1]\mathcal{G}lobal\mathcal{F}\_{t,d}^{Dsel}\in[0,1] measures the contribution of shocks of a specific persistence of selected dealers relative to the total shocks in the system, and [θ^t]j,k\Big[\widehat{\theta}\_{t}\Big]\_{j,k} is a j,kj,kth element of the time-varying decomposition matrix.

In the estimation, we construct a global factor containing 15 dealers and 7 non-dealer sectors (banks, central banks, asset managers, hedge funds, pension funds, etc.), working with a 22×2222\times 22 matrix θ^t\widehat{\theta}\_{t} measuring the impact of dealers on dealers, dealers on non-dealers, non-dealers on dealers, and non-dealers on non-dealers over the whole period, estimated on volumes and spreads. We will select a number of dealers that account for a large proportion of all funding and we will be interested to see if there is a significant global factor that influences the whole market. The global factor for both repo and reverse repo markets, measured independently of volume and spread shocks, will measure the intensity with which a few selected dealers influence the rest of the market.

#### Other relevant covariates

Dealers and non-dealers in the UK repo market are non-randomly matched. In our sample, dealers have an average of nine non-dealer counterparties, while non-dealers have an average of less than three dealers. Moreover, these trading relationships tend to be stable. These features are observed in other OTC markets, e.g. Zhou Yueshen and Zou ([2023](#bib.bib71)), and we need to include them in the analysis.

We measure relationship trading in two dimensions, e.g. depth and intensity. Our measure of depth, denoted D​e​p​t​hN​D,tDDepth\_{ND,t}^{D} and in line with Afonso et al. ([2014](#bib.bib1)); Li ([2021](#bib.bib53)); Han et al. ([2022](#bib.bib41)), is calculated as the share of financing received/provided by dealer D to non-dealer ND out of all financing received/provided by all non-dealers in the previous month.999Analogously, we could calculate the share of financing received/provided by non-dealer ND from dealer D out of all financing received/provided by all dealers in the previous month. The results are qualitatively the same, and are available on request.

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​e​p​t​hN​D,tD=∑tt−20v​o​l​u​m​eN​D,tD∑tt−20∑N​Dv​o​l​u​m​eN​D,tDDepth\_{ND,t}^{D}=\dfrac{\sum\_{t}^{t-20}volume\_{ND,t}^{D}}{\sum\_{t}^{t-20}\sum\_{ND}volume\_{ND,t}^{D}} |  | (3) |

The equation [3](#S3.E3 "In Other relevant covariates ‣ 3.3 Main Variables ‣ 3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") is a proxy for intensity of the trading relationship. A valuable feature of our dataset is that we are able to calculate each metric individually accounting for different segments. In principle, there is nothing to prevent a dealer from having differentiated relationships in the repo and reverse repo segments. Indeed, we observe that some non-dealers only interact with dealers in certain market segments.

Trading relationships aren’t just characterised by their depth. From the point of view of dealers, two non-dealers with the same depth may have a different impact on inventory constraints if one executes frequently small trades and the other rare albeit large trades.101010Sambalaibat ([2023](#bib.bib63)) shows that OTC dealers segment based on the trading needs of their clients. Dealers at the core of the dealer network would serve the most active non-dealers. Recurring trades could be associated with proactive risk management strategies, while end-of-month/quarter trades could be associated with window-dressing strategies, see Anbil and Senyuz ([2018](#bib.bib3)); Gerba and Katsoulis ([2024](#bib.bib38)); Bassi et al. ([2023](#bib.bib10)).

Our measure of intensity, I​n​t​e​n​s​i​t​yD​N​D,tIntensity\_{DND,t}, is computed as the number of transactions in the last 20 working days between dealer D and non-dealer ND. There are variations of this metric in the relationship trading literature for OTC markets, e.g.Brauning and Fecht ([2017](#bib.bib14)), but all use the frequency of transactions as the main input source. Higher intensity also implies more opportunities for dealers to learn private information from non-dealers, so while dealers may prefer to increase intensity, non-dealers may not want to, if the trading relationship is sufficiently beneficial to them.

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​n​t​e​n​s​i​t​yD​N​D,t=∑tt−20(𝟏v​o​l​u​m​eD​N​D,t>0)Intensity\_{DND,t}=\sum\_{t}^{t-20}(\mathbf{1}\_{volume\_{DND,t}>0}) |  | (4) |

Our dataset is granular enough to construct the intensity metric individually for repo and reverse repo segments. This feature is convenient as we can measure the relationship of any given dealer non-dealer dyad in each repo segment.

### 3.4 Identification

#### Market power and relationship-trading metrics

The identification strategy for the analysis of the repo market poses several challenges. First, reverse causality is expected in relational trading.111111We will properly define these variables in the next section. Volumes and repo rates between dealers and non-dealers are determined at the dyadic level, as are the measures of relational trading. Thus, if the repo rate increases (relative to a risk-free rate), non-dealers would have incentives to change the frequency of trading and the funding dependence with that dealer. Second, there could also be reverse causality with market power. Markups and markdowns are constructed at the dealer level. If a dealer has to change the repo rate with an important counterparty, this will change its overall market power.

To address reverse causality on the proxies for market power and relationship trading metrics, we exploit the granularity of our data to construct granular instrumental variables (see Gabaix and Koijen ([2024](#bib.bib37))). We recover idiosyncratic shocks at the level of individual dealers and non-dealers and use them to construct valid instruments for each variable. Essentially, we run a principal components factor model for each endogenous variable using the characteristics of the dealer/non-dealer dyad and extract the residuals. The constructed instruments are the size-weighted residuals of the regression of each endogenous variable on the factors, controlled for fixed effects.

For example, depth from the dealers’ perspective is assumed to be driven by common and idiosyncratic shocks. The instrument is based on netting dealers’ idiosyncratic variation in D​e​p​t​hN​D,tDDepth\_{ND,t}^{D} from their common shock. We use variables that explain the formation of relationships with non-dealers but have little or no correlation with non-dealers’ terms of trade, such as volumes and repo rates, to extract the common shock using principal component analysis. We retain the principal components that explain 90% of the total variation and use them to run the following rr factor model,

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​e​p​t​hN​D,tD=∑r=1Rλd​lr​ηt+ed​l​tDepth\_{ND,t}^{D}=\sum^{R}\_{r=1}\lambda^{r}\_{dl}\eta\_{t}+e\_{dlt} |  | (5) |

where ηt\eta\_{t} is the common shock and ed​l​te\_{dlt} is an idiosyncratic shock. The residuals from equation [5](#S3.E5 "In Market power and relationship-trading metrics ‣ 3.4 Identification ‣ 3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), denoted by e^d​l​t\hat{e}\_{dlt}, are used to compute the GIV as the share-weighted average idiosyncratic shock:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ztD​e​p​t​hD=∑i​d​lSd​l​e^tz^{Depth^{D}}\_{t}=\sum\_{idl}S\_{dl}\hat{e}\_{t} |  | (6) |

where Sd​lS\_{dl} is the dealer/non-dealer d​ldl share of transactions. As an additional robustness check, we include additional terms in equation [5](#S3.E5 "In Market power and relationship-trading metrics ‣ 3.4 Identification ‣ 3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"): λd\lambda\_{d}, ξl\xi\_{l} and ϕm\phi\_{m} which are dealer, non-dealer, and month fixed effects. To account for non-linearities, we include the square of the granular instrument and call it ztD​e​p​t​h2Dz^{Depth^{D}\_{2}}\_{t}. We do the same for the other endogenous variables, so that we end up with eight GIVs, two for each endogenous variable zD​e​p​t​htDz^{Depth^{D}\_{t}}, ztD​e​p​t​hN​Dz^{Depth^{ND}}\_{t}, ztI​n​t​e​n​s​i​t​yD​N​Dz^{Intensity^{DND}}\_{t}, ztL​Iz^{LI}\_{t} and ztD​e​p​t​h2Dz^{Depth^{D}\_{2}}\_{t}, ztD​e​p​t​h2N​Dz^{Depth^{ND}\_{2}}\_{t}, ztI​n​t​e​n​s​i​t​y2D​N​Dz^{Intensity^{DND}\_{2}}\_{t}, ztL​I2z^{LI\_{2}}\_{t}.

#### Dealer factors

To identify dealer factors, we use the generalised identification scheme of Pesaran and Shin ([1998](#bib.bib61)) adapted by Barunik and Ellington ([2024](#bib.bib8)) to approximate models with time-varying parameters, since a shock to one variable in the model does not necessarily occur in isolation. The use of time-varying frequency responses further identifies the persistence of shocks (Barunik and Ellington, [2024](#bib.bib8)). As the global factors derived from the aggregate shock transmission of dealers and non-dealers are used to explain volumes and spreads in both markets at the dyadic level, there is no other type of endogeneity to be addressed in the regressions.

## 4 Results

### 4.1 Market Power

We implement a simple structural model to identify dealer-level markups and markdowns using data from bilateral OTC repo market segments. We follow a demand approach (Berry, [1994](#bib.bib11)) and use the equality between predicted shares, given by equation ([C.5](#A3.E5 "In Appendix C A stylized structural model for markups and markdowns ‣ When David becomes Goliath: Repo dealer-driven bond mispricing")) in the Online Appendix, and observed market shares Sd​tS\_{dt} to transform the initial non-linear model into a linear one.121212The Online Appendix section [C](#A3 "Appendix C A stylized structural model for markups and markdowns ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") presents the model in detail.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ln⁡Sd​t−ln⁡S0​t=𝐱d​𝜷−α​rd​t+γ​Id​t+ϕt+ξd+Δ​ξd​t.\ln S\_{dt}-\ln S\_{0t}=\mathbf{x}\_{d}\bm{\beta}-\alpha r\_{dt}+\gamma I\_{dt}+\phi\_{t}+\xi\_{d}+\Delta\xi\_{dt}. |  | (7) |

where 𝐱d\mathbf{x}\_{d} is a (row) vector of observable product (dealer) characteristics that do not vary over time; ln⁡S0​t\ln S\_{0t} is the market share of the outside option; rd​tr\_{dt} is the average repo rate between dealer dd and non-dealers at tt; Id​tI\_{dt} is the average frequency, across non-dealers, of dealer dd’s lending/borrowing relationships at tt; ϕt\phi\_{t} accounts for time shocks common to all transactions observed in the market at tt; ξd\xi\_{d} captures the mean valuation of unobserved dealer characteristics that do not vary over time; Δ​ξd​t\Delta\xi\_{dt} are unobserved dealer characteristics that vary over time.

We have three potentially endogenous variables, e.g. the repo rate, frequency and residual maturity, as they are determined by the individual dealers. Dealers dd may have incentives to adjust these variables in response to changes in non-dealers’ need for funding or securities, or changes in preferences for time-varying dealer characteristics, Δ​ξf​t\Delta\xi\_{ft}, that are unobserved by the econometrician. To correct for potential bias in our estimates, we exploit both the granularity and the panel structure of our data to generate instrumental variables: two granular IVs (GIVs) for frequency, two difference IVs (DIVs) for repo rate, and three DIVs for residual maturity.131313GIVs are computed as in Gabaix and Koijen ([2024](#bib.bib37)), and DIVs are computed as the difference of the dealer-level variable from the mean across dealers divided by the standard deviation across dealers. Repo rate DIVs are the unique ISINs in the OTC reverse repo segment and the unique ISINs in the interdealer reverse repo segment. Maturity DIVs are the average maturity in the interdealer repo segment, the percentage of overnight in the OTC repo segment and the average funding in the OTC reverse repo segment. Thus, the identification assumption is that our instrumental variables are not correlated with demand shocks after controlling for aggregate shocks at the market level and observed and unobserved characteristics at the dealer level.

We estimate the model ([7](#S4.E7 "In 4.1 Market Power ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing")) using two-stage least squares. We report the results of the estimation in table [4](#S4.T4 "Table 4 ‣ 4.1 Market Power ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"). The top panel presents estimates with the reverse repo segment used to calculate the markdown, and the bottom panel presents estimates with the repo segment used to calculate the markup. Both panels have two columns: the first shows the estimates without correcting for endogeneity, and the second correcting for it. As very few non-dealers may be large enough to flip bargaining power in their favour, we eliminate the top 5% of non-dealers (according to their transaction volume) to ensure that dealers’ bargaining power is not distorted. Estimates with all non-dealers are qualitatively similar and are available upon request.

Table 4: Demand Estimation: Repo and Reverse Repo Segments

|  |  |  |
| --- | --- | --- |
|  | Reverse Repo Data | |
| Repo Rate | -1.649\*\*\* | 1.25\*\*\* |
|  | 0.139 | 0.130 |
| Residual Maturity | -0.003\*\*\* | 0.014\*\*\* |
|  | 0.001 | 0.003 |
| Frequency | 0.046\*\*\* | -0.227\*\*\* |
|  | 0.001 | 0.034 |
| Collateral Market Value | -0.000\*\*\* | -0.000\*\*\* |
|  | 0.000 | 0.000 |
| Control function | no | yes |
| Month FE | yes | yes |
| Obs | 7,822,333 | 7,822,333 |
| R2 | 0.1266 | 0.1594 |
|  | Repo Data | |
| Repo Rate | 0.992\*\*\* | -0.641\*\*\* |
|  | 0.139 | 0.183 |
| Residual Maturity | 0.012\*\*\* | 0.009\*\*\* |
|  | 0.000 | 0.003 |
| Frequency | 0.068\*\*\* | -0.071 |
|  | 0.002 | 0.054 |
| Collateral Market Value | -0.000\*\*\* | -0.000\*\*\* |
|  | 0.000 | 0.000 |
| Control function | no | yes |
| Month FE | yes | yes |
| Obs | 7,281,915 | 7,281,915 |
| R2 | 0.1187 | 0.1252 |
| ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | |
| --- | --- | --- |
| Note: This table reports the results of the regressions for demand estimation, as discussed in Section [3](#S3 "3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), for the period 2016:M1 to 2022:M1. Definitions, sources and frequency of all independent variables are presented in Section [3](#S3 "3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"). The top panel present results using the reverse repo data, and the bottom panel presents the results using repo data. | | |

The coefficients for the repo rate have the expected sign in each repo segment and are highly significant. In the top panel, the positive sign implies that the supply of funds from non-dealers is upward sloping; in the bottom panel, the negative sign implies that the demand for liquidity from non-dealers is downward sloping. It is interesting to observe that non-dealers providing liquidity are twice as reactive to price changes than when they demand liquidity, and this is consistent with the assumption that dealers have more bargaining power than non-dealers.

The estimates for frequency provide insight into the drivers of market power. Table [4](#S4.T4 "Table 4 ‣ 4.1 Market Power ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") shows that market power of dealers decreases as the number of interactions, between dealers and non-dealers in the last month, increases. This characteristic is only statistically significant when we calculate the markdown, but the sign remains when we calculate the markup. This result supports the argument that market power of repo dealers is, at least, partly driven by adverse selection as better trading conditions endure following more frequent transactions.

Market power of dealers may differ between the repo and reverse repo segments. To suggest otherwise is misleading, as we show in table [F.3](#A6.T3 "Table F.3 ‣ Appendix F Tables ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") in the online appendix, where we estimate the demand model using data from both repo segments. In particular, the estimate for the repo rate (column (4)) is no longer statistically significant, and its level (-0.18) is a fraction of that obtained in Table [4](#S4.T4 "Table 4 ‣ 4.1 Market Power ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing").

### 4.2 Repo Market Impact

Market power of repo dealers should affect the terms of trade for non-dealers. Theoretically we have two competing views. According to first, we should expect dealers with higher market power to deteriorate terms of trade, i.e. to reduce volumes and increase prices. Alternatively, if the main friction between dealers and non-dealers is asymmetric information, then dealers with higher market power will improve the terms of trade of non-dealers as counterparties trade more frequently.141414Crawford et al. ([2018](#bib.bib22)) argue that higher markups reduce the negative impact on prices associated with an increase in adverse selection. Empirical work has been largely confined to the banking sector; see Altunbas et al. ([2022](#bib.bib2)); Carlson et al. ([2022](#bib.bib18)); Cruz-García et al. ([2021](#bib.bib23)); Cañón et al. ([2022](#bib.bib19)). Studies with transaction-level data, such as the data quality we have, tend to support the first view, i.e. higher levels of market power affect negatively the borrower’s terms of trade.

Our preferred specification is below,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ΓD​l​t\displaystyle\Gamma\_{Dlt} | =\displaystyle= | β0+β1​M​a​r​k​e​t​P​o​w​e​rD,t+β3​d​e​p​t​hN​D,tD+β2​f​r​e​q​u​e​n​c​yD​N​D,t\displaystyle\beta\_{0}+\beta\_{1}{Market\hskip 2.84544ptPower}\_{D,t}+\beta\_{3}{depth}\_{ND,t}^{D}+\beta\_{2}{frequency}\_{DND,t} |  | (8) |
|  |  | +\displaystyle+ | β3​log⁡C​B​r​e​s​e​r​v​e​st+β4​D​F​t​o​t​r​e​p​ot+β5​D​F​t​o​t​r​e​v​e​r​s​et\displaystyle\beta\_{3}\log\hskip 2.84544ptCB\hskip 2.84544ptreserves\_{t}+\beta\_{4}DF\hskip 2.84544pttot\hskip 2.84544ptrepo\_{t}+\beta\_{5}DF\hskip 2.84544pttot\hskip 2.84544ptreverse\_{t} |  |
|  |  | +\displaystyle+ | β6​𝐗D​N​D,t+β7​𝐆D,t+β8​𝐇t+λd+ϵl+ηt+νd​l​t\displaystyle\beta\_{6}\mathbf{X}\_{DND,t}+\beta\_{7}\mathbf{G}\_{D,t}+\beta\_{8}\mathbf{H}\_{t}+\lambda\_{d}+\epsilon\_{l}+\eta\_{t}+\nu\_{dlt} |  |

where ΓD​t\Gamma\_{Dt} can be the logarithmic volume
between dealer D and non-dealer ND at time t (l​v​o​lD​N​D,tlvol\_{DND,t}) or the repo rate spread over the reference rate for the same transaction (r​a​t​eD​N​D,trate\_{DND,t}). The explanatory variables are the market power proxy (i.e. markup or markdown) for dealer D at time t (M​a​r​k​e​t​P​o​w​e​rD​tMarket\hskip 2.84544ptPower\_{Dt}), the depth metrics for dealer D (d​e​p​t​hN​D,tD{depth}\_{ND,t}^{D}) and the monthly frequency of interactions of dealer D and non-dealer ND at time t (f​r​e​q​u​e​n​c​yD​N​D,t{frequency}\_{DND,t}), and the dealer factors for each repo segment (D​F​t​o​t​r​e​p​otDF\hskip 2.84544pttot\hskip 2.84544ptrepo\_{t} and D​F​t​o​t​r​e​v​e​r​s​etDF\hskip 2.84544pttot\hskip 2.84544ptreverse\_{t}).151515This specification does not distinguish between transitory and persistent shocks to repo dealers. We introduce the distinction later. We include dealer-specific controls (𝐆D,t\mathbf{G}\_{D,t}) and time-specific controls (𝐇t\mathbf{H}\_{t}). Finally, we include dealer (non-dealer) fixed effects, non-dealer (dealer) fixed effects interacted with month fixed effects for the situation where dealers (non-dealers) provide liquidity to non-dealers (dealers).161616Following the banking literature (see Cañón et al. ([2022](#bib.bib19))), the interaction of dealer (non-dealer) fixed effects with monthly fixed effect in the reverse (repo) segment is to controls for unobserved liquidity demand by dealers (non-dealers) confounders. Alternatively, we use dealer/non-dealer dyad fixed effects and the results are very similar, qualitatively and quantitatively.

Some explanatory variables are potentially endogenous, i.e. the relationship trading proxies and market power, or might exhibit measurement error. Relationship trading proxies vary at the dyadic level and it may be that changes in the terms of trade affect depth or frequency. Market power varies only at the dealer level, but it could happen that changes in the terms of trade of large non-dealers affect the market power of dealers. Also, market power proxies could suffer from measurement errors attributed to model selection. To correct for these potential estimation biases, we exploit the granularity of our dataset and the panel structure of our data to generate a granular IV for each variable. The identifying assumption is that our instruments are not correlated with demand shocks after controlling for market-level aggregate shocks and dealer-level observed and unobserved characteristics.

We estimate our preferred specification using two-stage least squares. In all tables, we distinguish estimates for repo transactions from those for reverse repo transactions. As our data is granular enough to identify pairs of dealers and non-dealers that engage in repo and reverse repo on the same day, in online appendix we show results using the subsample of non-dealers that simultaneously operate in both segments.

Tables [5](#S4.T5 "Table 5 ‣ 4.2 Repo Market Impact ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") - [E.1](#A5.T1 "Table E.1 ‣ E.1 Non-Dealer Sectors and Repo Market Segmentation ‣ Appendix E Additional results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") show the impact of market power and dealer factors in the repo market. The structure of the tables is always the same. In the top panel, we present estimates for funding, measured as the logarithm of volume, and in the bottom panel we present estimates for the repo spread, in absolute values. In both panels we present estimates for both segments separately. We always distinguish dealer factors attributed to transitory shocks from persistent shocks.171717Table [F.4](#A6.T4 "Table F.4 ‣ Appendix F Tables ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") in the Online Appendix [F](#A6 "Appendix F Tables ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") shows the results for the estimates on simultanoues dyads.

Dealers’ interact with non-dealers in two ways, either by providing liquidity in exchange for gilts as collateral, or by receiving liquidity and providing gilts as collateral. In both situations, dealers are in an advantageous position, but we would expect market power to operate differently in each case. In repo transactions, when dealers are liquidity providers, we would expect dealers with higher market power to provide less funding. There is a large literature in banking showing that lenders with higher market power reduce lending, Altunbas et al. ([2022](#bib.bib2)); Carlson et al. ([2022](#bib.bib18)); Cruz-García et al. ([2021](#bib.bib23)); Cañón et al. ([2022](#bib.bib19)). In reverse repos, on the other hand, dealers have opposite incentives and we would expect qualitatively different results.

Table [5](#S4.T5 "Table 5 ‣ 4.2 Repo Market Impact ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") shows the estimates of our benchmark model ([8](#S4.E8 "In 4.2 Repo Market Impact ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing")) for the log volume, and highlight the role of relationship metrics and repo dealer factors. As expected the estimates of market power at both repo segments are negative, but they are not statistically significant. On the other hand, the coefficients for relationship metrics (specially Depth) are positive and highly significant.181818We provide evidence of a non-monotonic relationship between the importance of non-dealers to dealers and the funding they receive. In tables [F.5](#A6.T5 "Table F.5 ‣ Appendix F Tables ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") - [F.6](#A6.T6 "Table F.6 ‣ Appendix F Tables ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") of the Online Appendix [F](#A6 "Appendix F Tables ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), we replace the relationship trading proxies with two dummies, e.g. ‘Client’ and ‘Client Low’. We find that Client is equal to one if the non-dealer in a given pair is simultaneously above quantile 70 in all relationship trading metrics; on the other hand, a non-dealer is a Low Client if it is simultaneously below quantile 30. Consistently, both dummies are statistically significant, but while Client has a positive sign, Client Low has a negative sign. Similarly, the estimates for dealer factors are positive, highly significant, and slightly higher in the reverse repo segment. In terms of magnitudes, the impact on volume is rather small. For example, as the average transaction of dealers in the reverse segment is £65 million, the impact of a persistent shock in the reverse segment, which has the largest magnitude of all estimates, is equivalent to 104.3=£​19,952​m10^{4.3}=\pounds 19,952m .

The bottom panel of Table [5](#S4.T5 "Table 5 ‣ 4.2 Repo Market Impact ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") shows the impact on the (absolute) spread between the repo rate and the bank rate. We consistently find that dealers with higher market power charge or pay higher spreads (which are negative on average, see Table [1](#S3.T1 "Table 1 ‣ 3.1 Data ‣ 3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing")). In the repo segment, this is consistent with dealers charging a repo rate below the reference rate to access gilts. In the reverse repo segment, dealers with higher market power also receive larger (negative) spreads. It’s worth noting that the estimates for the relationship trading proxies are not statistically significant. In terms of magnitude, the story is different vis-a-vis the volume. Dealers with (1%1\%) higher market power in the repo segment will increase the spread by 0.039 pp, which is roughly half of it’s standard deviation (see Table [1](#S3.T1 "Table 1 ‣ 3.1 Data ‣ 3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing")). In the reverse repo segment, the impact is large as dealers with (1%1\%) higher market power will increase their spread by 0.53 pp, which greatly exceeds its’ standard deviations of 0.08.

Dealer factors, particularly transitory shocks, always reduce the spread. This effect is consistent with the presence of centrality discount from core dealers, see Weill ([2020](#bib.bib68)); Feldhütter ([2012](#bib.bib36)); Sambalaibat ([2023](#bib.bib63)). In magnitude, their impact is larger than the impact of market power in the repo segment, e.g. 0.25 pp reduction versus 0.04 pp increase from market power, but smaller for the reverse repo segment, e.g. 0.134 pp decrease versus 0.53 pp increase from market power.

Returning to Hypothesis [1](#Thmhypothesis1 "Hypothesis 1. ‣ 2 Hypotheses ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") around channel A, Table [5](#S4.T5 "Table 5 ‣ 4.2 Repo Market Impact ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") shows that dealer-specific market power produces the expected distortions in the repo market, but only through repo rates, as volumes are determined by relationship trading and dealer factors. Hence, we have sufficient evidence to reject the null hypothesis, as the transmission is only through prices.

Table 5: OTC impact by persistence of shocks: volume and spread

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Log volume | | | | |
|  | Repo | |  | Reverse | |
| Market Power | -0.204 | -0.184 |  | -0.378 | -0.420 |
|  | [0.136] | [0.124] |  | [0.260] | [0.264] |
| Depth | 0.719\*\*\* | 0.717\*\*\* |  | 0.927\*\*\* | 0.933\*\*\* |
|  | [0.238] | [0.238] |  | [0.301] | [0.300] |
| Frequency | 0.008\*\*\* | 0.008\*\*\* |  | 0.012\*\*\* | 0.012\*\*\* |
|  | [0.001] | [0.001] |  | [0.002] | [0.002] |
| DF tran repo | 1.837\*\*\* |  |  | 4.349\*\*\* |  |
|  | [0.634] |  |  | [0.741] |  |
| DF tran reverse | -1.037 |  |  | 2.227\*\*\* |  |
|  | [0.917] |  |  | [0.651] |  |
| DF per repo |  | 3.944\*\* |  |  | -1.031 |
|  |  | [1.562] |  |  | [1.259] |
| DF per reverse |  | -0.511 |  |  | 4.290\*\*\* |
|  |  | [1.070] |  |  | [1.193] |
| Dealer FE | Yes | Yes |  | No | No |
| NonDealer FE | No | No |  | Yes | Yes |
| NonDealer\*Week FE | Yes | Yes |  | No | No |
| Dealer\*Week FE | No | No |  | Yes | Yes |
| Year FE | Yes | Yes |  | Yes | Yes |
| Controls | Yes | Yes |  | Yes | Yes |
| Observations | 92,314 | 92,314 |  | 115,555 | 115,555 |
| R-squared | 0.597 | 0.597 |  | 0.484 | 0.483 |
|  | Repo rate spread | | | | |
|  | Repo | |  | Reverse | |
| Market Power | 0.034\*\* | 0.039\*\*\* |  | 0.532\*\*\* | 0.528\*\*\* |
|  | [0.013] | [0.013] |  | [0.020] | [0.020] |
| Depth | -0.003 | -0.003 |  | 0.008 | 0.009 |
|  | [0.012] | [0.012] |  | [0.009] | [0.009] |
| Frequency | -0.000 | -0.000 |  | 0.000 | 0.000 |
|  | [0.000] | [0.000] |  | [0.000] | [0.000] |
| DF tran repo | -0.259\*\*\* |  |  | -0.134\*\*\* |  |
|  | [0.038] |  |  | [0.025] |  |
| DF tran reverse | -0.073\*\* |  |  | -0.066\*\*\* |  |
|  | [0.037] |  |  | [0.025] |  |
| DF per repo |  | 0.021 |  |  | -0.030 |
|  |  | [0.064] |  |  | [0.041] |
| DF per reverse |  | 0.064 |  |  | -0.239\*\*\* |
|  |  | [0.079] |  |  | [0.047] |
| Dealer FE | Yes | Yes |  | No | No |
| NonDealer FE | No | No |  | Yes | Yes |
| NonDealer\*Week FE | Yes | Yes |  | No | No |
| Dealer\*Week FE | No | No |  | Yes | Yes |
| Year FE | Yes | Yes |  | Yes | Yes |
| Controls | Yes | Yes |  | Yes | Yes |
| Observations | 92,314 | 92,314 |  | 115,555 | 115,555 |
| R-squared | 0.090 | 0.087 |  | 0.129 | 0.129 |
| ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | | | | |
| --- | --- | --- | --- | --- | --- |
| Note: This table reports the results of the regressions for repo market impact by persistence of shocks to dealer, as discussed in Section [4](#S4 "4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), for the period 2016:M1 to 2022:M1. Definitions, sources and frequency of all independent variables are presented in Section [3](#S3 "3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"). Panels report the results for the dependent variables as follows: the top panel uses log of volume, and the bottom panel uses the absolute value of repo spread to the reference rate determined by Bank of England. Clustered standard errors on dealer / non-dealer dyads. | | | | | |

Dealers tend to operate in both repo segments, as do a non-negligible fraction of non-dealers. As a robustness test, we repeat the same analysis, but only with dealer/non-dealer dyads operating simultaneously in both segments with the objective of testing if dealers provide different treatment to counterparts that enable them to remain active in both segments. Table [F.4](#A6.T4 "Table F.4 ‣ Appendix F Tables ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") in the Online Appendix [F](#A6 "Appendix F Tables ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") shows that the results are qualitatively unchanged. For market power, there are no major differences between estimates using all dyads and dyads active in both segments. The only difference is for the dealer factors, as once the main dealers become more interconnected, only transitory shocks increase repo volumes.

### 4.3 Bond-Level Mispricing

Market power of repo dealers generates two different frictions that could result in bond mispricing, see Syverson ([2024](#bib.bib66)). Market power induces the traditional friction of reducing funding (access to gilts) through the repo (reverse repo) segment and distorting repo rates in favour of dealers. A second friction is related to the distribution in markups or markdowns across dealers, which can lead to misallocation of funds in the repo market, as more efficient dealers receive less funding in the reverse repo segment, which in turn can lead to arbitrage frictions in the bond market.191919Relatedly, Eisfeldt et al. ([2024](#bib.bib34)) show, for the corporate bond market, that the interdealer price dispersion explains changes in the yield spread.

Our benchmark specification includes both the individual and collective impact of repo dealers on bond market mispricing.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | yb​t\displaystyle y\_{bt} | =\displaystyle= | α0+α1​M​a​r​k​u​pb​t+α2​M​a​r​k​d​o​w​nb​t+α3​D​FtR​e​p​o+α4​D​FtR​e​v\displaystyle\alpha\_{0}+\alpha\_{1}Markup\_{bt}+\alpha\_{2}Markdown\_{bt}+\alpha\_{3}DF^{Repo}\_{t}+\alpha\_{4}DF^{Rev}\_{t} |  | (9) |
|  |  | +\displaystyle+ | β1​Xb​t+β2​γt+β3​F​Eb+β4​F​Et+ϵb​t\displaystyle\beta\_{1}X\_{bt}+\beta\_{2}\gamma\_{t}+\beta\_{3}FE\_{b}+\beta\_{4}FE\_{t}+\epsilon\_{bt} |  |

where yb​ty\_{bt} is the difference, in absolute value, between the yield on bond bb at time tt and a benchmark yield constructed using a spline-based method, see Anderson and Sleath ([2001](#bib.bib4)),202020Nymand-Andersen ([2018](#bib.bib59)) compares well-known methods using ECB data and finds that spline-based methods perform slightly better. M​a​r​k​u​pb​tMarkup\_{bt} and M​a​r​k​d​o​w​nb​tMarkdown\_{bt} are the (volume-)weighted average market power of dealers trading bond bb at time tt in each of the repo segments,212121In other specifications, we replace these variables with the (volume-)weighted average standard deviation across dealers trading bond bb at time tt in each of the repo segments, i.e. M​a​r​k​u​p​D​i​s​p​e​r​s​i​o​nMarkup\hskip 2.84544ptDispersion and M​a​r​k​d​o​w​n​D​i​s​p​e​r​s​i​o​nMarkdown\hskip 2.84544ptDispersion, or the interaction between them. D​FtR​e​p​oDF^{Repo}\_{t} and D​FtR​e​vDF^{Rev}\_{t} are the repo dealer factors222222At the implementation stage, we include both the transitory and persistent shocks. at time tt in each repo segment, Xb​tX\_{bt} are bond-level time-varying characteristics such as bid-ask spread, volatility, duration, repo premium,232323Measured as the difference between repo trades using bond bb at time tt and repo trades using the general collateral category.  residual maturity and the Bank of England free-float share. γt\gamma\_{t} are market-level time-varying confounders such as the log of Bank of England reserves, a proxy for UK systemic risk, and individual period-specific dummy variables (March 2020 dash-for-cash in the UK, September 2019 US repo market stress period, and Brexit period). Finally, we include bond fixed effects, and month fixed effects.

Table [6](#S4.T6 "Table 6 ‣ 4.3 Bond-Level Mispricing ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") shows the estimates for different versions of equation [9](#S4.E9 "In 4.3 Bond-Level Mispricing ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") using gilts at all maturities. The first two columns show the impact of markup and markdown controlling for endogeneity bias using GIVs, one column includes transitory shocks to dealer factors, and the other includes persistent shocks. Both columns show that, as the (weighted) average market power of dealers accepting/using a specific gilt in repo market increases, the mispricing of that same gilt increases in the bond market. In terms of magnitude, the impact of markup (markdown) is non-negligible, at 0.52 pp (0.64 pp).

The dispersion of market power between repo dealers can also lead to mispricing of individual gilts.242424Previous studies have raised awareness of the role of market power dispersion in explaining macroeconomic aggregates, see for example Syverson ([2024](#bib.bib66)). Columns three and four of Table [6](#S4.T6 "Table 6 ‣ 4.3 Bond-Level Mispricing ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") modify our benchmark specification of equation [9](#S4.E9 "In 4.3 Bond-Level Mispricing ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") by replacing the (weighted) average markup (markdown) with the (weighted) average standard deviation of the markup (markdown). Columns five and six modify the benchmark specification with the interactions between both (weighted) averages, i.e. markup and markup dispersion, and markdown and markdown dispersion.

Table [6](#S4.T6 "Table 6 ‣ 4.3 Bond-Level Mispricing ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") shows evidence that the (weighted) average standard deviation of market power between dealers is positively correlated with gilt mispricing. The evidence is particularly strong, in a statistical sense, when repo dealers receive funding from non-dealers in exchange for gilts. Then, an increase in markdown dispersion by 1%1\% increases bond mispricing (in absolute terms) by 1.3 pp. We also find that the interaction between market power proxies and their dispersion is not significant, at least when we include gilts of all maturities, but later we observe that this result does not hold for gilts with more than 20 years of residual maturity.

Table 6: Mispricing: All sample by persistence of shocks

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | (1) - (2) | | (3) - (4) | | (5) - (6) | |
| Markup | 0.523\*\*\* | 0.522\*\*\* |  |  | 0.189\* | 0.197\* |
|  | [0.150] | [0.144] |  |  | [0.103] | [0.102] |
| Markup Dispersion |  |  | 0.227 | 0.200 | 0.766 | 0.822 |
|  |  |  | [0.288] | [0.284] | [2.388] | [2.354] |
| Markup\*Markup Dispersion |  |  |  |  | -0.466 | -0.530 |
|  |  |  |  |  | [1.863] | [1.822] |
| Markdown | 0.638\*\*\* | 0.653\*\*\* |  |  | 0.733\*\*\* | 0.737\*\*\* |
|  | [0.186] | [0.181] |  |  | [0.191] | [0.179] |
| Markdown Dispersion |  |  | 1.362\*\*\* | 1.397\*\*\* | -4.155 | -4.043 |
|  |  |  | [0.258] | [0.256] | [3.596] | [3.605] |
| Markdown\*Markdown Dispersion |  |  |  |  | 4.362 | 4.295 |
|  |  |  |  |  | [2.872] | [2.880] |
| Markdown - Markup |  |  |  |  |  |  |
| DF tran repo | -0.785 |  | -1.084 |  | -0.823 |  |
|  | [0.643] |  | [0.681] |  | [0.637] |  |
| DF tran reverse | 2.080\*\* |  | 1.644\* |  | 2.026\*\* |  |
|  | [0.895] |  | [0.950] |  | [0.897] |  |
| DF per repo |  | -3.008\*\* |  | -2.600\* |  | -2.974\*\* |
|  |  | [1.235] |  | [1.377] |  | [1.237] |
| DF per reverse |  | 4.151\*\* |  | 3.971\*\* |  | 4.124\*\* |
|  |  | [1.711] |  | [1.955] |  | [1.725] |
| CB Market Share | -0.230\*\*\* | -0.228\*\*\* | -0.250\*\*\* | -0.249\*\*\* | -0.232\*\*\* | -0.230\*\*\* |
|  | [0.079] | [0.079] | [0.077] | [0.077] | [0.078] | [0.079] |
| Log CB Reserves | -0.358\*\*\* | -0.389\*\*\* | -0.101 | -0.149 | -0.313\*\* | -0.348\*\*\* |
|  | [0.134] | [0.128] | [0.148] | [0.149] | [0.133] | [0.128] |
| Bond\*Month FE | Yes | Yes | Yes | Yes | Yes | Yes |
| Year FE | Yes | Yes | Yes | Yes | Yes | Yes |
| Controls | Yes | Yes | Yes | Yes | Yes | Yes |
| Mat Bucket FE | Yes | Yes | Yes | No | Yes | No |
| GIVs | Yes | Yes | No | No | No | No |
| Observations | 32,585 | 32,585 | 32,585 | 32,585 | 32,585 | 32,585 |
| R-squared | 0.033 | 0.035 | 0.030 | 0.031 | 0.035 | 0.037 |
| ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Note: This table reports the results of the regressions for bond-level mispricing by frequency of shock on dealers, as discussed in Section [4](#S4 "4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), for the period 2016:M1 to 2022:M1. Definitions, sources and frequency of all independent variables are presented in Section [3](#S3 "3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"). The dependent variable is the absolute value of the spread between the bond yield and the predicted yield based on a spline. We use Driscoll-Kraay standard errors with 20 working days lag. | | | | | | |

Table [7](#S4.T7 "Table 7 ‣ 4.3 Bond-Level Mispricing ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") extends the previous table and reports estimates for gilts of different maturities.252525Short-term gilts have a residual maturity of between 3 and 7 years, medium-term gilts have a residual maturity of between 8 and 19 years and long-term gilts have a residual maturity of 20 years, or more. We exclude gilts with less than three years to maturity because the model selection error is higher for the front segment of the yield curve. All results are robust to the inclusion of the latter and are available on request. We observe that market power operates mainly through the reverse repo segment. In the first six columns, we observe a positive and significant impact of markdown for all maturities, equivalent to 1 pp at the short-end and 0.5 pp for the rest of the curve, but for markup it is only significant for medium-term gilts and equivalent to 1.2 pp.

The dispersion of market power between dealers is relevant for the longer end of the curve. Columns seven to twelve show that for short- and medium-term gilts, a 1%1\% increase in markdown correlates with a 1.1 pp increase in bond mispricing. For markup we only observe a 0.6 pp increase for medium-term gilts. Moreover, long-term gilt mispricing is solely affected by the dispersion of markdown and markdown. In terms of magnitude, the effect of markdown is nonlinear. For lower dispersion values, the mispricing effect is close to zero. Yet, it rises rapidly as dispersion increases. For example, when markdown disperson exceeds one standard deviation, long-term gilt mispricing easily exceeds several percentage points.

Table 7: Mispricing: All sample by persistence of shocks and maturity

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (1) - (6) | | | | | | (7) - (12) | | | | | |
|  | Short | | Medium | | Long | | Short | | Medium | | Long | |
| Markup | 0.043 | 0.066 | 1.223\*\*\* | 1.217\*\*\* | 0.126 | 0.109 | 0.064 | 0.079 | 0.642\*\*\* | 0.660\*\*\* | -0.015 | -0.017 |
|  | [0.218] | [0.214] | [0.261] | [0.250] | [0.179] | [0.177] | [0.172] | [0.175] | [0.233] | [0.224] | [0.132] | [0.133] |
| Markup Dispersion |  |  |  |  |  |  | -8.775 | -8.262 | 3.852 | 4.116 | 0.756 | 0.787 |
|  |  |  |  |  |  |  | [5.720] | [5.775] | [4.624] | [4.948] | [3.003] | [2.968] |
| Markup\*Markup Dispersion |  |  |  |  |  |  | 7.212 | 6.804 | -3.058 | -3.297 | -0.375 | -0.408 |
|  |  |  |  |  |  |  | [4.463] | [4.498] | [3.685] | [3.976] | [2.381] | [2.345] |
| Markdown | 1.056\*\*\* | 1.072\*\*\* | 0.550\*\* | 0.623\*\* | 0.517\*\* | 0.524\*\* | 1.115\*\*\* | 1.150\*\*\* | 1.072\*\*\* | 1.102\*\*\* | 0.320 | 0.317 |
|  | [0.248] | [0.244] | [0.277] | [0.265] | [0.234] | [0.238] | [0.181] | [0.174] | [0.251] | [0.242] | [0.230] | [0.226] |
| Markdown Dispersion |  |  |  |  |  |  | 6.050 | 6.508 | -4.679 | -3.797 | -13.116\*\*\* | -12.994\*\*\* |
|  |  |  |  |  |  |  | [6.852] | [6.805] | [5.245] | [5.175] | [4.490] | [4.553] |
| Markdown\*Markdown Dispersion |  |  |  |  |  |  | -4.642 | -4.952 | 4.352 | 3.662 | 11.915\*\*\* | 11.842\*\*\* |
|  |  |  |  |  |  |  | [5.431] | [5.379] | [4.111] | [4.048] | [3.660] | [3.716] |
| DF tran repo | -0.496 |  | -2.529\*\* |  | -0.512 |  | -0.469 |  | -2.491\*\* |  | -0.557 |  |
|  | [0.947] |  | [1.098] |  | [0.736] |  | [0.941] |  | [1.080] |  | [0.720] |  |
| DF tran reverse | 0.208 |  | 2.409 |  | 3.185\*\*\* |  | 0.265 |  | 2.392 |  | 3.117\*\*\* |  |
|  | [1.284] |  | [1.498] |  | [1.095] |  | [1.289] |  | [1.487] |  | [1.091] |  |
| DF per repo |  | -3.157\*\* |  | -4.053\*\* |  | -2.687\* |  | -3.197\*\* |  | -4.019\*\* |  | -2.643\*\* |
|  |  | [1.366] |  | [1.880] |  | [1.371] |  | [1.351] |  | [1.869] |  | [1.347] |
| DF per reverse |  | 4.022\*\* |  | 7.608\*\*\* |  | 2.404 |  | 4.009\*\* |  | 7.541\*\*\* |  | 2.361 |
|  |  | [1.819] |  | [2.329] |  | [1.985] |  | [1.800] |  | [2.308] |  | [1.976] |
| CB Market Share | 0.734\*\*\* | 0.738\*\*\* | -0.677\*\*\* | -0.654\*\*\* | -0.537\*\*\* | -0.533\*\*\* | 0.744\*\*\* | 0.750\*\*\* | -0.659\*\*\* | -0.637\*\*\* | -0.539\*\*\* | -0.534\*\*\* |
|  | [0.172] | [0.173] | [0.107] | [0.109] | [0.182] | [0.181] | [0.174] | [0.174] | [0.108] | [0.109] | [0.181] | [0.181] |
| Log CB Reserves | -0.721\*\*\* | -0.900\*\*\* | -0.564\*\* | -0.670\*\* | -0.060 | -0.026 | -0.740\*\*\* | -0.919\*\*\* | -0.557\*\* | -0.658\*\* | -0.007 | 0.021 |
|  | [0.240] | [0.230] | [0.269] | [0.275] | [0.198] | [0.175] | [0.240] | [0.230] | [0.267] | [0.274] | [0.189] | [0.167] |
| Bond\*Month FE | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Year FE | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Controls | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Mat Bucket FE | No | No | No | No | No | No | No | No | No | No | No | No |
| Observations | 7,536 | 7,536 | 10,770 | 10,770 | 14,274 | 14,274 | 7,536 | 7,536 | 10,770 | 10,770 | 14,274 | 14,274 |
| R-squared | 0.102 | 0.106 | 0.115 | 0.120 | 0.015 | 0.013 | 0.102 | 0.107 | 0.119 | 0.123 | 0.017 | 0.016 |
| ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Note: This table reports the results of the regressions for bond-level mispricing by bond residual maturity and frequency of dealer shocks, as discussed in Section [4](#S4 "4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), for the period 2016:M1 to 2022:M1. Definitions, sources and frequency of all independent variables are presented in Section [3](#S3 "3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"). The dependent variable is the absolute value of the spread between the bond yield and the predicted yield based on a spline. We use Driscoll-Kraay standard errors with 20 working days lag. | | | | | | | | | | | | |

Repo dealers can collectively influence the functioning of the bond market, via the repo market. Returning to Sambalaibat ([2023](#bib.bib63)), if the largest dealers specialise in non-dealers based on their activity or importance, then as the main dealers become more interconnected, certain non-dealer sectors will have access to either more funding or more gilts. We argue that our dealer factors (DFs) capture new information relative to other market-level variables262626For example, the correlation between the DF from the reverse segment and CB market share is 0.3, with log of CB reserves is 0.22, and with UK systemic risk is -0.01. Similar correlations are obtained with the DF from the repo segment, have the advantage of distinguishing between transitory and persistent shocks and should therefore be included in the benchmark specification.

On the one hand, in Tables [6](#S4.T6 "Table 6 ‣ 4.3 Bond-Level Mispricing ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") and [7](#S4.T7 "Table 7 ‣ 4.3 Bond-Level Mispricing ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") we observe that transitory and persistent shocks in the reverse repo segment increase gilt mispricing. On the other hand, we observe the opposite effect, for persistent shocks only in the repo segment (same table). In terms of magnitudes, the increase in mispricing through the reverse repo segment is around 1 pp for transitory shocks, and around 4 pp for persistent shocks. The reduction on mispricing through the repo segment, and associated to persistent shocks, is around 3 pp.

The qualitative difference between the repo and reverse repo segments corresponds to the way in which the main dealers segment the repo market. We argue that the main dealers in the repo segment specialise in pension funds and insurance companies, while in the reverse segment they specialise in hedge funds and asset managers. For example, as the main dealers in the reverse segment become more interconnected, hedge funds and asset managers will increase their funding to dealers and acquire gilts, and the pricing of gilts will deviate from the benchmark price. Conversely, as the repo segment’s main dealers become more interconnected, on the margin pension funds and insurance companies will receive more funding in exchange for gilts, and the pricing of gilts will move closer to the benchmark price.

The “dash-for-cash” period permits to further test the role of repo dealer segmentation during periods of stress. According to Czech et al. ([2021](#bib.bib24)); Gerba and Katsoulis ([2024](#bib.bib38)); Huser et al. ([2024](#bib.bib47)), in the dash-for-cash period, hedge funds and PFs & ICs were net borrowers (in the repo segment), and other non-bank sector, mostly money market funds, decreased their lending to repo dealers (in the reverse repo segment). Finally, non-bank financial institutions significantly increased their activity in the gilt market.

Table [8](#S4.T8 "Table 8 ‣ 4.3 Bond-Level Mispricing ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") shows that dealer factors have different effects across different gilt maturities during periods of high liquidity stress and high bond market activity. We observe that for medium-term gilts, the impact of DFs was much stronger during the dash-for-cash compared to normal periods. Notably, for long-term gilts, as the main dealers in the reverse repo segment become more interconnected, mispricing during dash-for-cash does not increase, but rather decreases. The latter effect correlates with the fact that hedge funds tend to trade short- and medium-term gilts, whereas pension funds and insurance companies prefer long-term gilts.

Table 8: Mispricing: Dash-for-Cash by persistence

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (1) - (4) | | | | (5) - (8) | | | | (9) - (12) | | | |
|  | Short | | | | Medium | | | | Long | | | |
| Markup | 0.120 | 0.130 | 0.133 | 0.136 | 0.601\*\*\* | 0.607\*\*\* | 0.619\*\*\* | 0.628\*\*\* | -0.007 | -0.009 | -0.009 | -0.009 |
|  | [0.169] | [0.170] | [0.173] | [0.174] | [0.218] | [0.219] | [0.211] | [0.211] | [0.117] | [0.117] | [0.119] | [0.119] |
| Markdown | 1.076\*\*\* | 1.084\*\*\* | 1.109\*\*\* | 1.111\*\*\* | 1.139\*\*\* | 1.153\*\*\* | 1.161\*\*\* | 1.169\*\*\* | 0.415\* | 0.409\* | 0.410\* | 0.402\* |
|  | [0.178] | [0.178] | [0.173] | [0.172] | [0.248] | [0.247] | [0.239] | [0.238] | [0.226] | [0.227] | [0.223] | [0.224] |
| DF tran repo | -0.477 | -0.503 |  |  | -2.501\*\* | -2.524\*\* |  |  | -0.577 | -0.563 |  |  |
|  | [0.942] | [0.938] |  |  | [1.084] | [1.083] |  |  | [0.724] | [0.725] |  |  |
| Dum Dash \* DF tran repo |  | 10.026\* |  |  |  | 8.157 |  |  |  | -9.136\*\*\* |  |  |
|  |  | [6.034] |  |  |  | [11.498] |  |  |  | [2.336] |  |  |
| DF tran reverse | 0.251 | 0.228 |  |  | 2.385 | 2.364 |  |  | 3.088\*\*\* | 3.098\*\*\* |  |  |
|  | [1.288] | [1.286] |  |  | [1.495] | [1.496] |  |  | [1.094] | [1.094] |  |  |
| Dum Dash \* DF tran reverse |  | 5.233 |  |  |  | 38.077\*\*\* |  |  |  | 1.524 |  |  |
|  |  | [13.890] |  |  |  | [9.466] |  |  |  | [4.681] |  |  |
| DF per repo |  |  | -3.189\*\* | -3.180\*\* |  |  | -4.006\*\* | -3.977\*\* |  |  | -2.574\* | -2.612\* |
|  |  |  | [1.352] | [1.354] |  |  | [1.879] | [1.884] |  |  | [1.374] | [1.376] |
| Dum Dash \* DF per repo |  |  |  | -12.393 |  |  |  | -52.292\*\*\* |  |  |  | 22.775\*\*\* |
|  |  |  |  | [7.752] |  |  |  | [12.023] |  |  |  | [4.639] |
| DF per reverse |  |  | 4.029\*\* | 4.024\*\* |  |  | 7.556\*\*\* | 7.523\*\*\* |  |  | 2.316 | 2.351 |
|  |  |  | [1.799] | [1.803] |  |  | [2.321] | [2.328] |  |  | [2.004] | [2.005] |
| Dum Dash \* DF per reverse |  |  |  | -15.434 |  |  |  | -58.753\*\*\* |  |  |  | 0.433 |
|  |  |  |  | [19.758] |  |  |  | [17.547] |  |  |  | [4.573] |
| CB Market Share | 0.742\*\*\* | 0.745\*\*\* | 0.748\*\*\* | 0.748\*\*\* | -0.665\*\*\* | -0.666\*\*\* | -0.643\*\*\* | -0.644\*\*\* | -0.536\*\*\* | -0.535\*\*\* | -0.531\*\*\* | -0.530\*\*\* |
|  | [0.173] | [0.173] | [0.174] | [0.174] | [0.108] | [0.108] | [0.109] | [0.109] | [0.182] | [0.182] | [0.181] | [0.181] |
| Log CB Reserves | -0.741\*\*\* | -0.741\*\*\* | -0.919\*\*\* | -0.920\*\*\* | -0.563\*\* | -0.564\*\* | -0.662\*\* | -0.663\*\* | -0.006 | -0.006 | 0.024 | 0.022 |
|  | [0.240] | [0.240] | [0.230] | [0.230] | [0.267] | [0.267] | [0.274] | [0.274] | [0.191] | [0.191] | [0.170] | [0.170] |
| Dum Dash | -0.285\*\*\* | -0.968\* | -0.218\*\* | 3.023 | -0.220\* | -2.434\*\*\* | -0.101 | 12.982\*\*\* | -0.049 | 0.270 | 0.009 | -3.312\*\*\* |
|  | [0.096] | [0.534] | [0.090] | [2.377] | [0.130] | [0.403] | [0.110] | [2.095] | [0.070] | [0.240] | [0.079] | [0.869] |
| Bond\*Month FE | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Year FE | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Controls | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Observations | 7,536 | 7,536 | 7,536 | 7,536 | 10,770 | 10,770 | 10,770 | 10,770 | 14,274 | 14,274 | 14,274 | 14,274 |
| R-squared | 0.102 | 0.102 | 0.106 | 0.106 | 0.118 | 0.118 | 0.122 | 0.123 | 0.015 | 0.015 | 0.013 | 0.013 |
| ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Note: This table reports the results of the regressions for bond-level mispricing, by frequency of shocks to dealers, including a dummy for the dash-for-cash period and interaction with dealer factors, as discussed in Section [4](#S4 "4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), for the period 2016:M1 to 2022:M1. Definitions, sources and frequency of all independent variables are presented in Section [3](#S3 "3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"). The dependent variable is the absolute value of the spread between the bond yield and the predicted yield based on a spline. We use Driscoll-Kraay standard errors with 20 working days lag. | | | | | | | | | | | | |

### 4.4 Impact on Market Liquidity

We now turn to the question of whether the individual repo dealer market power and the collective segmentation of the repo market have an impact on (financial) market-level aggregates.

This paper explores the linkages between the funding and bond markets, see Brunnermeier and Pedersen ([2008](#bib.bib17)), but so far we have focused the analysis at the bond (or gilt) level. We now move on to assess the impact on market liquidity, understood as in Hu et al. ([2013](#bib.bib43)). To this end, we aggregate equation [9](#S4.E9 "In 4.3 Bond-Level Mispricing ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") at the daily level.

Table [9](#S4.T9 "Table 9 ‣ 4.4 Impact on Market Liquidity ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") shows evidence that both individual and collective repo dealer actions affect market liquidity. The first three columns incorporate transitory DF shocks, and the last three columns the persistent DF shocks. We show that higher market power and dispersion of market power indeed deteriorate market liquidity, but only in the reverse repo segment. The latter is an interesting result, as the literature that includes market power generally does not distinguish between repo segments. Also, the relationship between both variables is non-linear, since markdown dispersion increases as market liquidity deteriorates, but holding dispersion constant, as average markdown increases, market liquidity improves.

Market liquidity responds also to transitory and persistent shocks to dealer factors. Table [9](#S4.T9 "Table 9 ‣ 4.4 Impact on Market Liquidity ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") shows that persistent shocks in the reverse repo segment deteriorate market liquidity, but same shocks in the repo segment improve it. This result is consistent with previous evidence that shocks to dealers in the reverse segment improves HFs & MAs activity, and shocks in the repo segment improves PFs & ICs. Transitory shocks unequivocally deteriorates market liquidity.

Table 9: Aggregate Effect on Market Liquidity

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | (1) - (3) | | | (4) - (6) | | |
| Markup | 5.519 |  | 0.947 | 4.911 |  | 0.844 |
|  | [4.274] |  | [2.352] | [4.090] |  | [2.337] |
| Markup Dispersion |  | -3.389 | -60.236 |  | -5.155 | -58.373 |
|  |  | [3.540] | [54.056] |  | [3.651] | [53.726] |
| Markup\*Markup Dispersion |  |  | 44.507 |  |  | 41.924 |
|  |  |  | [40.290] |  |  | [40.072] |
| Markdown | -3.776 |  | 1.173 | -3.262 |  | 1.091 |
|  | [4.383] |  | [2.306] | [4.169] |  | [2.299] |
| Markdown Dispersion |  | 12.458\*\* | -77.307\* |  | 11.351\*\* | -82.390\*\* |
|  |  | [4.903] | [39.858] |  | [4.874] | [36.748] |
| Markdown\*Markdown Dispersion |  |  | 64.114\*\* |  |  | 67.709\*\* |
|  |  |  | [30.885] |  |  | [28.206] |
| DF tran repo | 4.483\*\*\* | 4.397\*\*\* | 4.342\*\*\* |  |  |  |
|  | [1.042] | [1.099] | [0.962] |  |  |  |
| DF tran reverse | 5.729\*\*\* | 5.230\*\*\* | 5.345\*\*\* |  |  |  |
|  | [1.274] | [1.298] | [1.136] |  |  |  |
| DF per repo |  |  |  | -3.985\*\* | -4.309\*\* | -3.815\*\* |
|  |  |  |  | [1.733] | [1.793] | [1.545] |
| DF per reverse |  |  |  | 7.616\*\*\* | 9.252\*\*\* | 6.727\*\*\* |
|  |  |  |  | [2.346] | [2.700] | [2.107] |
| CB Market Share | 2.725\*\* | 3.048\*\*\* | 2.604\*\*\* | 2.910\*\* | 3.200\*\*\* | 2.854\*\*\* |
|  | [1.065] | [1.128] | [0.985] | [1.136] | [1.176] | [1.052] |
| Log CB Reserves | -1.468\*\*\* | -1.308\*\*\* | -1.556\*\*\* | -1.414\*\*\* | -1.285\*\*\* | -1.503\*\*\* |
|  | [0.379] | [0.367] | [0.394] | [0.391] | [0.376] | [0.407] |
| Month FE | Yes | Yes | Yes | Yes | Yes | Yes |
| GIVs | Yes | No | No | Yes | No | No |
| Controls | Yes | Yes | Yes | Yes | Yes | Yes |
| Observations | 852 | 852 | 852 | 852 | 852 | 852 |
| R-squared | 0.231 | 0.222 | 0.242 | 0.226 | 0.219 | 0.236 |
| ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Note: This table reports the results of the regressions of market liquitidy, as discussed in Section [4](#S4 "4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), for the period 2016 to 2022. Definitions, sources and frequency of all independent variables are presented in Section [3](#S3 "3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"). The dependent variable is market liquidity metrics from Hu et al. ([2013](#bib.bib43)) We use robust standard errors. | | | | | | |

Returning to our hypotheses, the evidence from the last 2 subsections indicates that there is not enough evidence to reject the null hypotheses in Hypothesis [2](#Thmhypothesis2 "Hypothesis 2. ‣ 2 Hypotheses ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") - Hypothesis [4](#Thmhypothesis4 "Hypothesis 4. ‣ 2 Hypotheses ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), noting that a larger share of the transmission is via the reverse repo segment. This implies we have sufficient evidence for the existence and quantitative significance of channels B and C.

### 4.5 Overarching discussion

This paper pins down three channels that result in spillover of frictions from repo to bond market, and create dysfunctionalities at the bond level. Furthermore, we show that all three mechanisms have a market-wide impact by determining overall (financial) market liquidity. We are ex ante agnostic about how these mechanisms interact, as there currently is no theoretical literature to anchor to. Yet, we wish to test, as stated in Hypothesis [5](#Thmhypothesis5 "Hypothesis 5. ‣ 2 Hypotheses ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), whether these three mechanisms interact, either additively, or off-setting.

Again, in Table [9](#S4.T9 "Table 9 ‣ 4.4 Impact on Market Liquidity ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") we provide evidence that once we include them all in our benchmark specification, they individually and additively contribute to market (il)liquidity.272727The impact on other macro variables is certainly of interest but it’s out of scope and we leave it for future research. As expected, most qualitative results at the bond-level are also observed at the market-level, but noticeably we obtain two new insights. First, at the aggregate level, the level of market power is less important than its dispersion between dealers. Second, the difference between transitory and persistent shocks to repo dealers is very clear. While transitory shocks undoubtedly worsen market liquidity, persistent shocks on the repo (reverse) segment actually improve (worsen) market liquidity. We argue that the latter qualitative difference between repo segments is explained by our evidence of OTC segmentation, e.g. main dealer from the repo segment specialize in PFs & ICs, and those from the reverse segment specialize in HFs & AMs.

Finally, Table [9](#S4.T9 "Table 9 ‣ 4.4 Impact on Market Liquidity ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") shows that the interaction between the (weighted) average market power and its dispersion is statistically significant for the reverse segment. So why don’t we observe it in both repo segments? The reverse segment is used by hedge funds and asset managers to obtain gilts from dealers, most of which are on-the-run and might have high demand. Moreover, collateral scarcity observed during most of the sample period generated excess demand for it, which may explain why market power has a disproportionately large role to play in the reverse segment. We therefore have enough evidence to reject the null hypothesis [5](#Thmhypothesis5 "Hypothesis 5. ‣ 2 Hypotheses ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") given that, although the combined effects are larger than any individual, the transmission of market power to bond mispricing and market liquidity from the two repo segments are, at times, off-setting.

Table [10](#S4.T10 "Table 10 ‣ 4.5 Overarching discussion ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") summarize the main takeaways.

Table 10: Hypotheses and Takeaways

| Hypothesis | Accept/Reject | Takeaway |
| --- | --- | --- |
| 1 (channel A) | REJECT | Dealer-specific market power (markup and markdown) |
|  |  | creates inefficiencies that affect both repo prices and volumes. |
| 2 (channel A) | ACCEPT | Dealer-specific market power (markup and markdown) impacts |
|  |  | individual gilts, bond-market liquidity, and (financial) market-wide liquidity. |
| 3 (channel B) | ACCEPT | There is a sizeable inefficiency effect due to the distribution/dispersion |
|  |  | of market power across dealers (markups and markdowns), |
|  |  | which impacts bond-level mispricing and market-wide liquidity. |
| 4 (channel C) | ACCEPT | Persistent shocks to repo dealers matter for bond-level mispricing |
|  |  | and market-wide liquidity. |
| 5 (A+B+C) | REJECT | The combined effects of the three inefficiencies on bond yield deviations |
|  |  | and market liquidity are sizeable and larger than any of those individually. |

## 5 Concluding remarks

Using a proprietary gilt market dataset, we identify how microstructure inefficiencies impact gilt mispricing and market-wide liquidity, and we provide new perspective on how inefficiencies in the money market, measured by market power and global factors, affect the real economy through shocks to individual dealer capacity.

We contribute to the growing literature on financial market frictions in three ways. First, we pin down the size of the friction using market liquidity metrics and suggest a way to conceptualise it in aggregate or system-wide terms. Second, we explicitly link industrial organisation features in financial markets to individual bond mispricing, which operates through the notion of market liquidity and collateral availability. Finally, we also show how transitory and persistent shocks to repo core dealers affect individual bond mispricing, and market-wide liquidity. The conceptual novelty, we believe, lies in linking micro and macro phenomena in financial markets, by providing empirical basis for financial market frictions in aggregate fluctuations.

## References

* Afonso et al. (2014)

  G. Afonso, A. Kovner, and A. Schoar.
  Trading partners in the interbank lending market.
  *Federal Reserve Bank of New York Staff Reports*, 8(620), 2014.
* Altunbas et al. (2022)

  Y. Altunbas, D. Marques-Ibanez, M. van Leuvensteijn, and T. Zhao.
  Market power and bank systemic risk: Role of securitization and bank
  capital.
  *Journal of Banking & Finance*, 138:106451, 2022.
  ISSN 0378-4266.
  doi: https://doi.org/10.1016/j.jbankfin.2022.106451.
  URL
  <https://www.sciencedirect.com/science/article/pii/S0378426622000516>.
* Anbil and Senyuz (2018)

  S. Anbil and Z. Senyuz.
  The regulatory and monetary policy nexus in the repo market.
  *Finance and Economics Discussion Series, Board of Governors of
  the Federal Reserve System*, (027), 2018.
* Anderson and Sleath (2001)

  N. Anderson and J. Sleath.
  New estimates of the uk real and nominal yield curves.
  *Bank of England SWP*, 126, 2001.
* Bai et al. (2018)

  J. Bai, A. Krishnamurthy, and C.-H. Weymuller.
  Measuring liquidity mismatch in the banking sector.
  *The Journal of Finance*, 73(1):51–93,
  2018.
  doi: https://doi.org/10.1111/jofi.12591.
  URL <https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12591>.
* Barbeiro et al. (2024)

  O. Barbeiro, F. Brauning, G. Joaquim, and H. Stein.
  Dealer risk limits and currency retuns.
  *Federal Reserve Bank of Boston Research Department WP 24-11*,
  2024.
  doi: https://doi.org/10.29412/res.wp.2024.11.
  URL
  <https://www.bostonfed.org/publications/research-department-working-paper/2024/dealer-risk-limits-and-currency-returns.aspx>.
* Barunik and Ellington (2020)

  J. Barunik and M. Ellington.
  Dynamic networks in large financial and economic systems.
  *arXiv preprint arXiv:2007.07842*, 2020.
* Barunik and Ellington (2024)

  J. Barunik and M. Ellington.
  Persistence in financial connectedness and systemic risk.
  *European Journal of Operational Research*, 314(1):393–407, 2024.
  ISSN 0377-2217.
  doi: https://doi.org/10.1016/j.ejor.2023.11.023.
  URL
  <https://www.sciencedirect.com/science/article/pii/S0377221723008640>.
* Baruník and Kr̆ehlík (2018)

  J. Baruník and T. Kr̆ehlík.
  Measuring the Frequency Dynamics of Financial Connectedness and
  Systemic Risk.
  *Journal of Financial Econometrics*, 16(2):271–296, 2018.
* Bassi et al. (2023)

  C. Bassi, M. Behn, M. Grill, and M. Waibel.
  Window dressing of regulatory metrics: evidence from repo markets.
  *ECB Working Paper Series*, (2771), 2023.
* Berry (1994)

  S. Berry.
  Estimating discrete-choice models of product differentiation.
  *The RAND Journal of Economics*, 25(2):242–262, 1994.
* Bicu et al. (2017)

  A. Bicu, L. Chen, and D. Elliott.
  The leverage ratio and liquidity in the gilt and repo markets.
  *Bank of England SWP*, 690, 2017.
* Boar and Midrigan (2019)

  C. Boar and V. Midrigan.
  Markups and inequality.
  Working Paper 25952, National Bureau of Economic Research, June 2019.
* Brauning and Fecht (2017)

  F. Brauning and F. Fecht.
  Relationship lending in the interbank market and the price of
  liquidity.
  *Review of Finance*, 21(1):33–75, 2017.
* Brauning and Stein (2025)

  F. Brauning and H. Stein.
  The effect of primary dealer constraints on intermediation in the
  treasury market.
  *Available at SSRN*, 2025.
  doi: http://dx.doi.org/10.2139/ssrn.4862212.
  URL <https://ssrn.com/abstract=4862212>.
* Brooks et al. (2021)

  W. J. Brooks, J. P. Kaboski, and Y. A. Li.
  Agglomeration, misallocation, and (the lack of) competition.
  *American Economic Journal: Macroeconomics*, 13(4):483–519, October 2021.
  doi: 10.1257/mac.20180443.
* Brunnermeier and Pedersen (2008)

  M. K. Brunnermeier and L. H. Pedersen.
  Market Liquidity and Funding Liquidity.
  *The Review of Financial Studies*, 22(6):2201–2238, 11 2008.
  doi: 10.1093/rfs/hhn098.
* Carlson et al. (2022)

  M. Carlson, S. Correia, and S. Luck.
  The effects of banking competition on growth and financial stability:
  Evidence from the national banking era.
  *Journal of Political Economy*, 130(2):462–520, 2022.
  doi: 10.1086/717453.
  URL <https://doi.org/10.1086/717453>.
* Cañón et al. (2022)

  C. Cañón, E. Cortés, and R. Guerrero.
  Bank competition and the price of credit: Evidence using mexican
  loan-level data.
  *International Review of Economics & Finance*, 79:56–74, 2022.
  ISSN 1059-0560.
  doi: https://doi.org/10.1016/j.iref.2021.11.007.
  URL
  <https://www.sciencedirect.com/science/article/pii/S1059056021002379>.
* Clark et al. (2021)

  R. Clark, J.-F. Houde, and J. Kastl.
  The industrial organization of financial markets.
  *NBER WP*, 29183, 2021.
* Coen et al. (2024)

  J. Coen, P. Coen, and A.-C. Huser.
  Collateral demand in wholesale funding markets.
  *Bank of England Staff Working Paper*, (1082), 2024.
  URL
  <https://www.bankofengland.co.uk/working-paper/2024/collateral-demand-in-wholesale-funding-markets>.
* Crawford et al. (2018)

  G. Crawford, N. Pavanini, and F. Schivardi.
  Asymmetric information and imperfect competition in lending markets.
  *American Economic Review*, 108(7):1659–1701, 2018.
* Cruz-García et al. (2021)

  P. Cruz-García, J. Fernández de Guevara, and J. Maudos.
  Bank competition and multimarket contact intensity.
  *Journal of International Money and Finance*, 113:102338, 2021.
  ISSN 0261-5606.
  doi: https://doi.org/10.1016/j.jimonfin.2020.102338.
  URL
  <https://www.sciencedirect.com/science/article/pii/S0261560620302941>.
* Czech et al. (2021)

  R. Czech, B. Gual-Ricart, J. Lillis, and J. Worlidge.
  The role of non-bank financial intermediaries in the “dash for
  cash” in sterling markets.
  *Bank of England Financial Stability Paper*, 2021.
  URL
  <https://www.bankofengland.co.uk/financial-stability-paper/2021/the-role-of-non-bank-financial-intermediaries-in-the-dash-for-cash-in-sterling-markets>.
* Dahlhaus (1996)

  R. Dahlhaus.
  On the kullback-leibler information divergence of locally stationary
  processes.
  *Stochastic processes and their applications*, 62(1):139–168, 1996.
* David and Venkateswaran (2019)

  J. David and V. Venkateswaran.
  The sources of capital misallocation.
  *American Economic Reveiw*, 109(7):2531–67,
  2019.
  doi: 10.1257/aer.20180336.
* Di Maggio et al. (2017)

  M. Di Maggio, A. Kermani, and Z. Song.
  The value of trading relations in turbulent times.
  *Journal of Financial Economics*, 124(2):266–284, 2017.
  ISSN 0304-405X.
  doi: https://doi.org/10.1016/j.jfineco.2017.01.003.
  URL
  <https://www.sciencedirect.com/science/article/pii/S0304405X1730003X>.
* Diebold and Yilmaz (2012)

  F. X. Diebold and K. Yilmaz.
  Better to give than to receive: Predictive directional measurement
  of volatility spillovers.
  *International Journal of Forecasting*, 28(1):57–66, 2012.
* Duffie et al. (2005)

  D. Duffie, N. Gârleanu, and L. H. Pedersen.
  Over-the-counter markets.
  *Econometrica*, 73(6):1815–1847, 2005.
  doi: https://doi.org/10.1111/j.1468-0262.2005.00639.x.
* Duffie et al. (2015)

  D. Duffie, S. Malamud, and G. Manso.
  : Information percolation in segmented markets.
  *The Journal of Economic Theory*, 158:838–869, 2015.
* Eisenschmidt et al. (2022)

  J. Eisenschmidt, Y. Ma, and A. Lee Zhang.
  Monetary policy transmission in segmented markets.
  *ECB Working Paper Series*, 2706, 2022.
* Eisenschmidt et al. (2024)

  J. Eisenschmidt, Y. Ma, and A. L. Zhang.
  Monetary policy transmission in segmented markets.
  *Journal of Financial Economics*, 151:103738, 2024.
* Eisfeldt et al. (2022)

  A. L. Eisfeldt, B. Herskovic, S. Rajan, and E. Siriwardane.
  OTC Intermediaries.
  *The Review of Financial Studies*, 36(2):615–677, 09 2022.
  doi: 10.1093/rfs/hhac062.
* Eisfeldt et al. (2024)

  A. L. Eisfeldt, B. Herskovic, and S. Liu.
  Interdealer price dispersion and intermediary capacity.
  Working Paper 32998, National Bureau of Economic Research, September
  2024.
* Farboodi et al. (2022)

  M. Farboodi, G. Jarosch, and R. Shimer.
  The Emergence of Market Structure.
  *The Review of Economic Studies*, 90(1):261–292, 03 2022.
  doi: 10.1093/restud/rdac014.
  URL <https://doi.org/10.1093/restud/rdac014>.
* Feldhütter (2012)

  P. Feldhütter.
  The same bond at different prices: Identifying search frictions and
  selling pressures.
  *The Review of Financial Studies*, 25(4):1155–1206, 2012.
  doi: 10.1093/rfs/hhr093.
* Gabaix and Koijen (2024)

  X. Gabaix and R. Koijen.
  Granular instrumental variables.
  *Journal of Political Economy*, 132(7):2274–2303, 2024.
* Gerba and Katsoulis (2024)

  E. Gerba and P. Katsoulis.
  The repo market under basel iii: Effects of capital and liquidity
  regulations on market fragmentation.
  *International Journal of Finance & Economics*, 2024.
* Greenwood and Vayanos (2014)

  R. Greenwood and D. Vayanos.
  Bond supply and excess bond returns.
  *The Review of Financial Studies*, 27(3):663–713, 2014.
* Haltiwanger et al. (2018)

  J. Haltiwanger, R. Kulick, and C. Syverson.
  Misallocation measures: The distortion that ate the residual.
  Working Paper 24199, National Bureau of Economic Research, January
  2018.
* Han et al. (2022)

  S. Han, K. Nikolaou, and M. Tase.
  Trading relationships in secured markets: Evidence from triparty
  repos.
  *Journal of Banking & Finance*, 139:106486, 2022.
  ISSN 0378-4266.
  doi: https://doi.org/10.1016/j.jbankfin.2022.106486.
  URL
  <https://www.sciencedirect.com/science/article/pii/S0378426622000851>.
* Hau et al. (2021)

  H. Hau, P. Hoffmann, S. Langfield, and Y. Timmer.
  Discriminatory pricing of over-the-counter derivatives.
  *Management Science*, 67(11):6660–6677,
  2021.
  doi: https://doi.org/10.1287/mnsc.2020.3787.
* Hu et al. (2013)

  G. X. Hu, J. Pan, and J. Wang.
  Noise as information for illiquidity.
  *The Journal of Finance*, 68(6):2341–2382,
  2013.
  doi: https://doi.org/10.1111/jofi.12083.
  URL <https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12083>.
* Huber (2023a)

  A. W. Huber.
  Market power in wholesale funding: A structural perspective from the
  triparty repo market.
  *Journal of Financial Economics*, 149(2):235–259, 2023a.
  doi: https://doi.org/10.1016/j.jfineco.2023.04.007.
  URL
  <https://www.sciencedirect.com/science/article/pii/S0304405X23000673>.
* Huber (2023b)

  A. W. Huber.
  Market power in wholesale funding: A structural perspective from the
  triparty repo market.
  *Journal of Financial Economics*, 149(2):235–259, 2023b.
* Huh and Infante (2021)

  Y. Huh and S. Infante.
  Bond market intermediation and the role of repo.
  *Journal of Banking & Finance*, 122:105999, 2021.
  ISSN 0378-4266.
  doi: https://doi.org/10.1016/j.jbankfin.2020.105999.
  URL
  <https://www.sciencedirect.com/science/article/pii/S0378426620302612>.
* Huser et al. (2024)

  A.-C. Huser, C. Lepore, and L. Veraart.
  How does the repo market behave under stress? evidence from the
  covid-19 crisis.
  *Journal of Financial Stability*, 70:101193, 2024.
* Jurkatis et al. (2022)

  S. Jurkatis, A. Schrimpf, K. Todorov, and N. Vause.
  Relationship discounts in corporate bond trading (december 13, 2022).
  *SSRN*, 2022.
  doi: http://dx.doi.org/10.2139/ssrn.4301416.
  URL <https://ssrn.com/abstract=4301416>.
* Kadiyala and Karlsson (1997)

  K. R. Kadiyala and S. Karlsson.
  Numerical methods for estimation and inference in Bayesian
  VAR-models.
  *Journal of Applied Econometrics*, 12(2):99–132, 1997.
* Kerssenfischer and Helmus (2024)

  M. Kerssenfischer and C. Helmus.
  Outages in soverign bond markes.
  *Available at SSRN*, 2024.
* Kotidis and van Horen (2018)

  A. Kotidis and N. van Horen.
  Repo market functioning: the role of capital regulation.
  *Bank of England SWP*, 746, 2018.
* Lewis et al. (2021)

  K. F. Lewis, F. A. Longstaff, and L. Petrasek.
  Asset mispricing.
  *Journal of Financial Economics*, 141(3):981–1006, 2021.
  ISSN 0304-405X.
  doi: https://doi.org/10.1016/j.jfineco.2020.05.011.
  URL
  <https://www.sciencedirect.com/science/article/pii/S0304405X21001471>.
* Li (2021)

  Y. Li.
  Reciprocal lending relationships in shadow banking.
  *Journal of Financial Economics*, 141(2):600–619, 2021.
  ISSN 0304-405X.
  doi: https://doi.org/10.1016/j.jfineco.2021.04.004.
  URL
  <https://www.sciencedirect.com/science/article/pii/S0304405X21001318>.
* Liang (2023)

  Y. Liang.
  Misallocation and markups: Evidence from indian manufacturing.
  *Review of Economic Dynamics*, 51:161–176, 2023.
  doi: https://doi.org/10.1016/j.red.2022.12.004.
* Lütkepohl (2005)

  H. Lütkepohl.
  *New introduction to multiple time series analysis*.
  Springer Science & Business Media, 2005.
* Mancini et al. (2016)

  L. Mancini, A. Ranaldo, and J. Wrampelmeyer.
  The euro interbank repo market.
  *The Review of Financial Studies*, 29(7):1747–1779, 2016.
* Manning (2003)

  A. Manning.
  *Monopsony in Motion: Imperfect Competition in Labor Markets*.
  Princeton University Press, 2003.
  ISBN 9780691123288.
  URL <http://www.jstor.org/stable/j.ctt5hhpvk>.
* Nevo (2000)

  A. Nevo.
  A practitioner’s guide to estimation of random-coefficients logit
  models of demand.
  *Journal of Economics and Management Strategy*, 9(4):513–548, 2000.
* Nymand-Andersen (2018)

  P. Nymand-Andersen.
  Yield curve modelling and a conceptual framework for estimating yield
  curves: evidence from the european central bank’s yield curve.
  *ECB WP*, 27, 2018.
* Pelizzon et al. (2025)

  L. Pelizzon, M. G. Subrahmanyam, and D. Tomio.
  Central bank–driven mispricing.
  *Journal of Financial Economics*, 166:104004, 2025.
* Pesaran and Shin (1998)

  H. H. Pesaran and Y. Shin.
  Generalized impulse response analysis in linear multivariate models.
  *Economics letters*, 58(1):17–29, 1998.
* Petrova (2019)

  K. Petrova.
  A quasi-Bayesian local likelihood approach to time varying
  parameter VAR models.
  *Journal of Econometrics*, 2019.
* Sambalaibat (2023)

  B. Sambalaibat.
  Endogenous specialization and dealer networks.
  *Available at SSRN*, 2023.
  doi: http://dx.doi.org/10.2139/ssrn.2676116.
  URL <https://ssrn.com/abstract=2676116>.
* Schrimpf et al. (2020)

  A. Schrimpf, H. S. Shin, and V. Sushko.
  Leverage and margin spirals in fixed income markets during the
  covid-19 crisis.
  Bulletin 2, BIS, 2020.
* Stein and Wallen (2025)

  J. Stein and J. Wallen.
  The imperfect intermediation of money-like assets.
  *Forthcoming Journal of Finance*, 2025.
* Syverson (2024)

  C. Syverson.
  Markups and markdowns.
  Working Paper 32871, National Bureau of Economic Research, August
  2024.
* Wang (2021)

  C. Wang.
  Core-periphery trading networks.
  *Working paper*, 2021.
* Weill (2020)

  P.-O. Weill.
  The search theory of otc markets.
  Working Paper 27354, National Bureau of Economic Research, June 2020.
* Weinberger (2020)

  A. Weinberger.
  Markups and misallocation with evidence from exchange rate shocks.
  *Journal of Development Economics*, 146:102494, 2020.
  doi: https://doi.org/10.1016/j.jdeveco.2020.102494.
* Yeh et al. (2022)

  C. Yeh, C. Macaluso, and B. Hershbein.
  Monopsony in the us labor market.
  *American Economic Review*, 112(7):2099–2138, July 2022.
  doi: 10.1257/aer.20200025.
  URL <https://www.aeaweb.org/articles?id=10.1257/aer.20200025>.
* Zhou Yueshen and Zou (2023)

  B. Zhou Yueshen and J. Zou.
  Less is more.
  *Available at SSRN*, 2023.
* Üslü (2019)

  S. Üslü.
  Pricing and liquidity in decentralized asset markets.
  *Econometrica*, 87(6):2079–2140, 2019.

Online Appendix

## Appendix A The UK Repo Market

### A.1 Overview

We wish to describe the UK repo market, both in terms of the institutional set-up and the participants.282828It’s important to point out the UK’s institutional peculiarities in the repo market, as it differentiates significantly from that of the US or the Euro Area. We follow the description laid out in Gerba and Katsoulis ([2024](#bib.bib38)).

A repo transaction involves selling a security and agreeing to buy it back at a later date for a pre-agreed price. The security acts as collateral in the case the seller cannot buy it back and offers counterparty risk protection to the buyer who can sell it in order to limit losses. The difference between the sell price and the repurchase price determines the interest rate paid by the seller to borrow cash and is known as the repo rate, or price of the contract. The buyer can demand collateral haircuts to further reduce the risk of losses in case of a counterparty default by overcollateralising the loan. The transaction is called repo from the cash borrower’s perspective and reverse repo from the cash lender’s perspective. When a pre-specified security is exchanged as collateral, the transaction is known as special repo. On the other hand, when any security satisfying certain criteria, such as specific credit rating, is accepted the transaction is known as general repo. In special repo trades, the rate is typically lower compared to general repo, or even negative as demand is driven by cash lenders who are willing to pay interest to obtain the security (e.g. for collateral management purposes). In general repo, the rate is typically higher and positive as demand is driven by cash borrowers who seek funding.

### A.2 Role of the repo market

Figure [4](#A1.F4 "Figure 4 ‣ A.2 Role of the repo market ‣ Appendix A The UK Repo Market ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), from Clark et al. ([2021](#bib.bib20)), depicts where repos fit into the overall financial market vertical chain (or system). It’s evident the essential role played by repos for the modern financial firm, e.g. banks and non-banks, since it’s a core source of liquidity and collateral. For example, hedge funds could use the repo to fund long bond positions, or obtain collateral to implement short bond positions.

c

![Refer to caption](2603.10690v1/Figures/supply_chain.jpg)

Figure 4:

### A.3 UK microstructure

The UK repo market is dominated by bank dealers that intermediate transactions mostly backed by UK government bonds, or gilts (Kotidis and van Horen, [2018](#bib.bib51)). A wide range of other institutions also participate in the repo market including non-dealer banks, money market funds, central counterparties and corporates that invest cash through reverse repos. Hedge funds, pension funds, asset managers and insurance companies, on the other hand, borrow cash through repos to finance their investments (Bicu et al., [2017](#bib.bib12); Huser et al., [2024](#bib.bib47)). The market includes transactions that occur between bank dealers (i.e. interdealer segment), which are mostly cleared through CCPs, and transactions that occur between dealers and clients that are mostly traded bilaterally or OTC (Kotidis and van Horen, [2018](#bib.bib51)).

Figure [5](#A1.F5 "Figure 5 ‣ A.3 UK microstructure ‣ Appendix A The UK Repo Market ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") summarizes the stylized structure of the market in which dealers intervene.

![Refer to caption](2603.10690v1/Figures/Repo_Structure-Mickey_Mouse_version.png)


Figure 5: Repo Market Structure

In Figure [6(a)](#A1.F6.sf1 "In Figure 6 ‣ A.3 UK microstructure ‣ Appendix A The UK Repo Market ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), we plot the evolution of the UK gilts repo market using Bank of England’s proprietary dataset SMMD (or Sterling Money Markets Data), splitting total monthly volume by general collaterial (GC) and special collateral (SC) trades. As can be seen, since 2016 there has been an increase in market activity, mainly SC trades, which constitute 95% of transactions and 83% of total transactions volume. In Figure [6(b)](#A1.F6.sf2 "In Figure 6 ‣ A.3 UK microstructure ‣ Appendix A The UK Repo Market ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") we split total transaction volumes by maturity buckets, i.e. less than or equal to 30 days, and more than 30 days. The graph shows that the majority of trades have a maturity of less than 30 days (97% of transactions and total volume). In Figure [7](#A1.F7 "Figure 7 ‣ A.3 UK microstructure ‣ Appendix A The UK Repo Market ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") we decompose total volume by participants’ headquarters region. As is to be expected, UK-domiciled banks dominate the market in terms of traded volumes (32% of transactions and 40% of total volume), followed by US-domiciled banks (36% of transactions and 33% of total volume), EU-domiciled banks (24% of transactions and 20% of total volume), and Asia-domiciled banks (8% of transactions and 7% of total volume). Overall, on a monthly basis transaction volumes have doubled from £2 trillion in 2016 to £4 trillion in November 2020 which highlights the significance of repos as a key funding market in the UK.

To give perspective, we report gilts repo vis-a-vis reverse repo holdings separated across maturity and region, as share of the total market. As can be seen, short-term holdings constitute 54% of the total, indicating that while they represent the vast majority of transactions since they roll-over much more frequently, they are roughly equal to long-term repo and reverse repo holdings. Expressed differently, while in terms of flows (or volumes), short-term clearly dominates long-term, in terms of stocks (or holdings), the two are relatively equal. Furthermore, UK banks hold 45% of the total volume, followed by US banks with 35%, EU banks with 14% and Asian banks with 6%.

![Refer to caption](2603.10690v1/Figures/smmd_col_paper.png)


(a) By collateral type (SMMD)

![Refer to caption](2603.10690v1/Figures/smmd_mat_paper.png)


(b) B bucket (SMMD)

Figure 6: Monthly gilts repo and reverse repo transaction volumes

![Refer to caption](2603.10690v1/Figures/smmd_region_paper.png)


Figure 7: Monthly gilts repo and reverse repo transaction volumes by region (SMMD)

![Refer to caption](2603.10690v1/Figures/pie_holdings_paper.png)


Figure 8: gilts repo and reverse repo holdings volumes by maturity bucket and region (SMMD)

In Panel A of Table LABEL:tab:descriptives, descriptive statistics for daily and quarterly transaction volumes from SMMD are provided. On a daily frequency, the average general repo transaction volume across institutions is £1,542.68 million, while the average general reverse repo transaction volume is £469.48 million. On a quarterly frequency, the corresponding mean volumes are £51,328.04 million and £10,654.75 million. Special collateral transaction volumes follow a similar pattern, with daily average repo volumes being £2,333.68 million and reverse repo volumes being £1,728.02 million. On a quarterly frequency they average £91,351.56 million and £78,072.54 million. Overall, the higher volumes in repo compared to reverse repo transactions corroborates previous findings that banks and dealers are net borrowers in the UK repo market (Huser et al., [2024](#bib.bib47)).

## Appendix B Context

### B.1 UK financial market

As a global financial centre, London is home to some of the world’s largest repo dealers, who also act as market makers in gilts. We analyse two over-the-counter (OTC) segments between 2016 and 2022: Repurchase agreements, where dealers provide cash in exchange for collateral from non-dealers, and reverse repurchase agreements, where dealers receive cash in exchange for collateral. Trading is concentrated within stable dealer–client relationships, which vary by sector. Reverse repo activity favours hedge funds and asset managers seeking on-the-run collateral, while repo activity favours pension funds and insurers looking to fund themselves with gilts. We combine transaction data with gilt-level measures of mispricing relative to a flexible yield curve benchmark and a market-wide liquidity proxy. The sample spans major events such as the US repo stress in September 2019, and the Dash-for-cash events of March 2020. This enables us to study both normal and stressed conditions (e.g. Mancini et al., [2016](#bib.bib56); Hu et al., [2013](#bib.bib43)).

We use two key terms throughout: (i) Market power refers to a dealer’s ability to set spreads and quantities differently in bilateral OTC trading than would prevail under perfect competition or full pass-through from interdealer markets, without conflating this with search, switching or transaction costs. Operationally, we estimate dealer-level markups (repo) and markdowns (reverse repo) from a structural supply–demand framework at the dealer–counterparty dyad level. This takes into account bond characteristics and rich time fixed effects. Our short-term funding model, though stylized, reflects key market features. (ii) Persistent shocks refer to changes in dealers’ intermediation capacity or willingness that endure beyond short-lived fluctuations (e.g. sustained balance sheet constraints or shifts in collateral availability). We identify persistence using a dynamic network approach based on time-varying VARs and generalised variance decompositions (Lütkepohl, [2005](#bib.bib55); Pesaran and Shin, [1998](#bib.bib61); Diebold and Yilmaz, [2012](#bib.bib28)). Additionally, we interpret dealer factors as market-wide influences arising when a subset of dealers transmits shocks of heterogeneous persistence through the trading network. These factors capture the extent to which repo market outcomes are shaped by a few influential dealers.

In line with standard IO literature (Syverson, [2024](#bib.bib66))) and using bilateral OTC segment data, we calculate dealer-level markup and markdown metrics. Additionally, in line with the literature on relationship lending (Brauning and Fecht, [2017](#bib.bib14); Jurkatis et al., [2022](#bib.bib48)), we calculate dealer- and non-dealer-level metrics for relationship trading. Finally, based on recent literature on dynamic networks (Barunik and Ellington, [2020](#bib.bib7), [2024](#bib.bib8)), we calculate market-wide dealer global factors. For the bond market, we construct bond-level mispricing metrics and a market-wide metric of market liquidity, following literature on mispricing (Lewis et al., [2021](#bib.bib52); Pelizzon et al., [2025](#bib.bib60); Hu et al., [2013](#bib.bib43)).

Our contribution to the literature is characterised by several key findings. First of all, the market power of individual dealers is economically significant in bilateral over-the-counter (OTC) transactions. Higher market power metrics are associated with larger absolute spreads and quantities that deviate from competitive benchmarks. These distortions result in mispricing at the gilt level. Next, the dispersion of market power among dealers is important for aggregate liquidity. Holding the average level fixed, a more uneven distribution of bargaining power is associated with lower market-wide liquidity and greater deviations of gilt prices from benchmark values. Finally, the persistence of dealer shocks affects transmission: persistent shocks to influential reverse-repo dealers increase gilt mispricing, whereas persistent shocks to influential repo dealers reduce it. This is consistent with improved funding availability for pension funds and insurers against gilts. By contrast, transitory shocks have materially smaller effects.

We emphasise that market power has a stronger effect in the reverse repo segment. Here, the demand for scarce collateral from hedge funds and asset managers amplifies scarcity premia and pushes gilt prices away from the benchmark values. By contrast, a sustained increase in the influence of repo dealers tends to ease funding conditions against gilts and support the realignment of prices with fundamentals.

The second key finding, concerning the dispersion of market power, also shows that the impact operates at both the aggregate liquidity level and the individual bond level. The mispricing effects are in the same direction as the effects associated with illiquidity metrics, which highlights that dispersion in market power reinforces bond-specific pricing frictions.

## Appendix C A stylized structural model for markups and markdowns

We implement a simple structural model to retrieve dealer-level markups and markdown using data from bilateral OTC repo market segment. In the repo segment, we calculate the markup of dealers, as they are the only providers of liquidity to non-dealers. In the reverse repo segment, we calculate the markdown of dealers, as they are the only buyers of liquidity from non-dealers.

Below, we explain in detail the case for markups. Markdowns have an analogous specification and we comment briefly on the main differences.292929We argue repo dealers have both product and factor market power. Our approach is an approximation for markup and markdown estimation as we do not jointly estimate them. Following Syverson ([2024](#bib.bib66)), a profit maximizing dealer’s first-order conditions show that a combination of both metrics is equal to the ratio of elasticity of output wrt liquidity, and dealer’s expenditure on liquidity expressed as a share of revenue. Our approach responds to this , but with data limitation.

Supply side. Suppose that there are DD dealers in the repo market, indexed by d=1,…,Dd=1,\dots,D each of which supplies liquidity or collateral through market making services. For the sake of simplicity, we assume that dealers are single-product firms; that is, each dealer supplies repo/reverse repo with fixed characteristics (e.g., interest rate, maturity and haircut) to non-dealers looking for liquidity/collateral in the bilateral OTC market. Accordingly, datawise, we aggregate all transactions made by a given dealer in a single product indexed by the same index of the dealer; the characteristics of that product correspond to averages of the observed lending terms across non-dealers that transacted from the same dealer in period tt.303030This is a restrictive assumption relative to how the market works in reality, in which a given dealer/non-dealer pair may agree on several transactions in the same day, each of them characterized by a particular volume, a given interest rate, a given maturity, and a given collateral. Products provided by the same dealer to the same non-dealer may, therefore, be heterogeneous; we, therefore, obtain an average measure of the true market power of each dealer, which can vary across non-dealers. The variable profit of dealer dd derived from its transactions in the repo market is given by:

|  |  |  |
| --- | --- | --- |
|  | Πd​t=(rd​t−cd​t)​Mt​sd​(𝐫d),\Pi\_{dt}=(r\_{dt}-c\_{dt})M\_{t}s\_{d}(\mathbf{r}\_{d}), |  |

where rd​tr\_{dt} is weighted average interest rate given by dd at time tt, cd​tc\_{dt} is the dealer’s marginal cost, sd​ts\_{dt} is the market share of dealer dd at time tt, 𝐫t\mathbf{r}\_{t} is the F×1F\times 1 vector of interest rates of all dealers in the market, and MtM\_{t} is the size of the repo market, which we take as all of the money borrowed by dealers and non-dealers in the repo market from any firm providing wholesale liquidity at time tt.313131For simplicity, we assume that dealers expect the full repayment of each loan from borrowers and that they actually do the full repayment of their loans; this implies that there is no loss of profits due to default. For a model that explicitly accounts for default, see Crawford et al. ([2018](#bib.bib22)). We assume that dealers compete in setting interest rates and that a pure-strategy Bertrand-Nash equilibrium in prices exist. Therefore, the interest rate of the lending supplied by dealer dd must satisfy the first order condition:

|  |  |  |
| --- | --- | --- |
|  | sd​(𝐫t)+(rd​t−cd​t)​∂sd​(𝐫t)∂rd​t=0.s\_{d}(\mathbf{r}\_{t})+(r\_{dt}-c\_{dt})\frac{\partial s\_{d}(\mathbf{r}\_{t})}{\partial r\_{dt}}=0. |  |

We have, therefore, a system of DD equations, one for each of the dealers (products) existing in the market.
Solving dealer dd’s equation for its interest rate-cost margin yields, for d=1,…,Dd=1,\dots,D:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rd​t−cd​t=1−∂sd​(𝐫t)∂rd​t​sd​(𝐫t).r\_{dt}-c\_{dt}=\frac{1}{-\frac{\partial s\_{d}(\mathbf{r}\_{t})}{\partial r\_{dt}}}s\_{d}(\mathbf{r}\_{t}). |  | (C.1) |

This optimal pricing rule allows us to back out a markup index for each dealer in each period tt. Dividing the two sides of equation ([C.1](#A3.E1 "In Appendix C A stylized structural model for markups and markdowns ‣ When David becomes Goliath: Repo dealer-driven bond mispricing")) by dd’s interest rate yields:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | M​a​r​k​u​pd​t≡rd​t−cd​trd​t=1ηd​t,\displaystyle{Markup}\_{dt}\equiv\frac{r\_{dt}-c\_{dt}}{r\_{dt}}=\frac{1}{\eta\_{dt}}, | with | ηd​t=−∂sd​(𝐫t)∂rd​t​rd​tsd​(𝐫t),\displaystyle\eta\_{dt}=-\frac{\partial s\_{d}(\mathbf{r}\_{t})}{\partial r\_{dt}}\frac{r\_{dt}}{s\_{d}(\mathbf{r}\_{t})}, |  | (C.2) |

being the positive own price elasticity of demand. The Lerner index being a function of the demand elasticity implies that we do not need to observe the marginal costs of dealers to estimate the Lerner index, but to have a good estimate of the own price elasticity of demand.

The case of markdown is similar. Dealer dd maximize profit Πd​tf=(m​r​e​vd​t−rd​t)​Mtf​sdf​(𝐫d)\Pi^{f}\_{dt}=(mrev\_{dt}-r\_{dt})M^{f}\_{t}s^{f}\_{d}(\mathbf{r}\_{d}) , where m​r​e​vd​tmrev\_{dt} is the marginal revenue from aggregate funding obtained from non-dealers, and rd​tr\_{dt} is the average repo rate from such funding. The remaining variables are, just as with markup but superscript ff refers to the factor market (e.g. reverse repo segment), where dealer dd has market power. Following a similar first order condition approach, the markdown is inversely related to the elasticity of supply (νd​t\nu\_{dt}).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | M​a​r​k​d​o​w​nd​t≡m​r​e​vd​t−rd​trd​t=1νd​t,\displaystyle{Markdown}\_{dt}\equiv\frac{mrev\_{dt}-r\_{dt}}{r\_{dt}}=\frac{1}{\nu\_{dt}}, | with | νd​t=∂sdf​(𝐫t)∂rd​t​rd​tsdf​(𝐫t),\displaystyle\nu\_{dt}=\frac{\partial s^{f}\_{d}(\mathbf{r}\_{t})}{\partial r\_{dt}}\frac{r\_{dt}}{s^{f}\_{d}(\mathbf{r}\_{t})}, |  | (C.3) |

Demand model. The demand model presented in this section is in the spirit of the empirical industrial organization literature (in particular, Berry ([1994](#bib.bib11)) and Nevo ([2000](#bib.bib58))). Non-dealers, indexed by l=1,2,…,N​Dl=1,2,\dots,ND face a multiple-choice decision among dd dealers in each period. Assume that the conditional indirect utility of non-dealer ll from choosing to borrow money from dealer dd at time tt is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ul​d​t=𝐱d​𝜷−α​rd​t+γ​Id​t+ϕt+ξd+Δ​ξd​t+εl​d​tu\_{ldt}=\mathbf{x}\_{d}\bm{\beta}-\alpha r\_{dt}+\gamma I\_{dt}+\phi\_{t}+\xi\_{d}+\Delta\xi\_{dt}+\varepsilon\_{ldt} |  | (C.4) |

where 𝐱d\mathbf{x}\_{d} is a (row) vector of observable product (dealer) characteristics that do not vary with time; rd​tr\_{dt} is the mean interest rate of the lending granted by dealer dd to non-dealers at tt; Id​tI\_{dt} is the mean intensity, across non-dealers, of dealer dd’s lending relationships at tt; ϕt\phi\_{t} accounts for time shocks that are common to all of the transactions observed at tt in the market; ξd\xi\_{d} captures the mean valuation of the unobserved dealer characteristics that do not vary with time; Δ​ξd​t\Delta\xi\_{dt} are unobserved dealer characteristics that vary with time; and εl​d​t\varepsilon\_{ldt} is an additively separable mean-zero random shock that captures idiosyncratic non-dealer preferences.323232There is no practical distinction between markup and markdown specification. Noticeably, the main difference is the expected sign of α\alpha, e.g. negative for markup and positive for markdown.

We assume that non-dealers’ choice set includes an “outside good”, which may capture all other liquidity sources not considered in this analysis. Normalizing its mean utility to zero, the indirect utility derived by non-dealer ll from the outside option writes as ul​0​t=εl​0​tu\_{l0t}=\varepsilon\_{l0t}. Another key assumption of this model is that non-dealers choose at most one product (i.e., dealer) at each period tt. The product (dealer) chosen is the one giving the highest utility. For given unobserved demand shocks, 𝜺l​d​t\bm{\varepsilon}\_{ldt}, bank ll will choose product dd if:

|  |  |  |
| --- | --- | --- |
|  | ul​d​t⩾ul​k​t,∀k=0,1,…,D.u\_{ldt}\geqslant u\_{lkt},\;\forall\,k=0,1,\dots,D. |  |

Assuming that the shocks to utility εl​d​t\varepsilon\_{ldt} are independent of the product characteristics and of each other (i.i.d.), and drawn from a Type 1 Extreme Value distribution, the market share of dealer dd at time tt is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | sd​(𝐗,𝐫t)=exp⁡(𝐱d​𝜷−α​rd​t+γ​Id​t+ϕt+ξd+Δ​ξd​t)1+∑kexp⁡(𝐱k​𝜷−α​rk​t+γ​Ik​t+ϕt+ξk+Δ​ξk​t),s\_{d}(\mathbf{X},\mathbf{r}\_{t})=\frac{\exp(\mathbf{x}\_{d}\bm{\beta}-\alpha r\_{dt}+\gamma I\_{dt}+\phi\_{t}+\xi\_{d}+\Delta\xi\_{dt})}{1+\sum\_{k}\exp(\mathbf{x}\_{k}\bm{\beta}-\alpha r\_{kt}+\gamma I\_{kt}+\phi\_{t}+\xi\_{k}+\Delta\xi\_{kt})}, |  | (C.5) |

where 𝐗\mathbf{X} is the matrix of observed characteristics of all of the included dealers, that do not vary over time.

Elasticities.
The non-dealer-level, own- and cross-price demand elasticities are given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηl​d​k​t=∂sd​t∂rk​t​rk​tsd​t={−α​(1−sd​t)​rd​tidd=k,α​sk​t​rk​tifd≠k.\displaystyle\eta\_{ldkt}=\frac{\partial s\_{dt}}{\partial r\_{kt}}\frac{r\_{kt}}{s\_{dt}}=\left\{\begin{array}[]{rcl}-\alpha(1-s\_{dt})r\_{dt}&\mbox{id}\ \ d=k,\\[5.0pt] \alpha s\_{kt}r\_{kt}&\mbox{if}\ \ d\neq k.\end{array}\right. |  | (C.8) |

The non-dealer-level, own- and cross-price supply elasticities are given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | νl​d​k​t=∂sd​tf∂rk​t​rk​tsd​tf={α​(1−sd​tf)​rd​tidd=k,α​sk​tf​rk​tifd≠k.\displaystyle\nu\_{ldkt}=\frac{\partial s^{f}\_{dt}}{\partial r\_{kt}}\frac{r\_{kt}}{s^{f}\_{dt}}=\left\{\begin{array}[]{rcl}\alpha(1-s^{f}\_{dt})r\_{dt}&\mbox{id}\ \ d=k,\\[5.0pt] \alpha s^{f}\_{kt}r\_{kt}&\mbox{if}\ \ d\neq k.\end{array}\right. |  | (C.11) |

Estimation and results. We follow Berry ([1994](#bib.bib11)) and use the equality between predicted shares, given by equation ([C.5](#A3.E5 "In Appendix C A stylized structural model for markups and markdowns ‣ When David becomes Goliath: Repo dealer-driven bond mispricing")), and observed market shares Sd​tS\_{dt} to transform our non-linear model to a linear one. Formally, the model we obtain is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ln⁡Sd​t−ln⁡S0​t=𝐱d​𝜷−α​rd​t+γ​S​Id​t+ϕt+ξd+Δ​ξd​t.\ln S\_{dt}-\ln S\_{0t}=\mathbf{x}\_{d}\bm{\beta}-\alpha r\_{dt}+\gamma SI\_{dt}+\phi\_{t}+\xi\_{d}+\Delta\xi\_{dt}. |  | (C.12) |

Notice that our demand model allows for unobserved factors at time ϕt\phi\_{t} and fund levels ξd\xi\_{d}. We account for those unobservables by including time and fund dummies, respectively. The latter capture also all of the observed fund attributes that do not vary over time 𝐱d​𝜷\mathbf{x}\_{d}\bm{\beta}. We do not account for dealer-time unobserved factors, Δ​ξd​t\Delta\xi\_{dt}; thus, we leave it as the error term of the model.

## Appendix D Global Dealer Factors: Estimation

### D.1 Overview of the time-varying parameter VAR model

Since the behaviour of dealers and non-dealers is highly dynamic, we approximate it with time-varying parameter vector autoregression (TVP-VAR) model:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xt,T=ϕ0​(tT)+ϕ1​(tT)​xt−1,T+…+ϕp​(tT)​xt−p,T+ϵt,x\_{t,T}=\phi\_{0}\left(\frac{t}{T}\right)+\phi\_{1}\left(\frac{t}{T}\right)x\_{t-1,T}+\ldots+\phi\_{p}\left(\frac{t}{T}\right)x\_{t-p,T}+\epsilon\_{t}, |  | (D.1) |

estimated from (ND+NN​DN^{D}+N^{ND}) dimensional vector of volume of the repo or reverse repo dealers and non-dealers xt,T=(V​o​l1,t,TD,…,V​o​lND,t,TD,V​o​l1,t,TN​D​…,V​o​lNN​D,t,TN​D)′x\_{t,T}=\left(Vol^{D}\_{1,t,T},\ldots,Vol^{D}\_{N^{D},t,T},Vol^{ND}\_{1,t,T}\ldots,Vol^{ND}\_{N^{ND},t,T}\right)^{\prime} in one system, or from (ND+NN​DN^{D}+N^{ND}) dimensional vector of rate spread of the repo or reverse repo dealers and non-dealers xt,T=(R​a​t​e1,t,TD,…,R​a​t​eND,t,TD,R​a​t​e1,t,TN​D​…,R​a​t​eNN​D,t,TN​D)′x\_{t,T}=\left(Rate^{D}\_{1,t,T},\ldots,Rate^{D}\_{N^{D},t,T},Rate^{ND}\_{1,t,T}\ldots,Rate^{ND}\_{N^{ND},t,T}\right)^{\prime} in day t=1,…,Tt=1,\ldots,T following the methodology of Barunik and Ellington ([2024](#bib.bib8)). Note the variable xt,Tx\_{t,T} is triangular array of observations (xt,T;t=1,…,T)(x\_{t,T};t=1,\ldots,T) with sample size TT that can be interpreted as a locally stationary approximation around a fixed point t/Tt/T. As a consequence, the process can change its properties smoothly over time.

An important feature of such local approximation is the possibility to represent a locally stationary process xt,Tx\_{t,T} as a time-varying vector moving average:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xt,T=∑h=−∞+∞αt,T​(h)​ϵt−h,x\_{t,T}=\sum\_{h=-\infty}^{+\infty}\alpha\_{t,T}\left(h\right)\epsilon\_{t-h}, |  | (D.2) |

where coefficients αt,T​(h)\alpha\_{t,T}\left(h\right) can be approximated under certain smoothness assumptions a αt,T​(h)≈α​(t/T,h)\alpha\_{t,T}\left(h\right)\approx\alpha(t/T,h), see Dahlhaus ([1996](#bib.bib25)). The innovations ϵt\epsilon\_{t} are independent random variables with zero mean and finite variation. The original process xt,Tx\_{t,T} can be represented as a linear combination of uncorrelated innovations with time-varying impulse response (TV-IRF) functions αt,T​(h)\alpha\_{t,T}\left(h\right). The information contained in the impulse response functions allows the contribution of shocks in the system to be measured. Thus, their transformations over time determine the interconnectedness of dealers and non-dealers.

We further transform local impulse responses in the system into local impulse transfer functions using Fourier transformations. This allows us to identify the persistence dynamics of interconnectedness based on the heterogeneous persistence of shocks in the system. A dynamic representation of the variance decomposition of shocks from dealer (or non-dealers) jj to dealer (or non-dealers) kk then establishes a dynamic horizon-specific adjacency matrix, which is central to our measures.

Specifically, the element of such matrix that captures how shocks propagate from a dealer (or non-dealers) jj to a dealer (or non-dealers) kk at a given time and horizon333333In the empirical investigation, 20 business days divides the transitory and persistent horizons. di∈ℋ={Tr,Per},d\_{i}\in\mathcal{H}=\{\text{Tr},\text{Per}\}, is formally defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | [θt,Td]j,k=σ^k​k−1​∑ω∈di([α^t,T​(ω)​Σ^t,T]j,k)2∑ω∈ℋ[α^t,T​(ω)​Σ^t,T​α^t,T⊤​(ω)]j,j,\Big[\theta\_{t,T}^{d}\Big]\_{j,k}=\frac{\widehat{\sigma}\_{kk}^{-1}\displaystyle\sum\_{\omega\in d\_{i}}\left(\bigg[\widehat{\alpha}\_{t,T}(\omega)\widehat{\Sigma}\_{t,T}\bigg]\_{j,k}\right)^{2}}{\displaystyle\sum\_{\omega\in\mathcal{H}}\Bigg[\widehat{\alpha}\_{t,T}(\omega)\widehat{\Sigma}\_{t,T}\widehat{\alpha}^{\top}\_{t,T}(\omega)\Bigg]\_{j,j}}, |  | (D.3) |

where α^t,T​(ω)=∑h=0H−1∑hα^t,T​(h)​e−i​ω​h\widehat{\alpha}\_{t,T}(\omega)=\sum\_{h=0}^{H-1}\sum\_{h}\widehat{\alpha}\_{t,T}(h)e^{-i\omega h} is an impulse transfer function estimated from Fourier frequencies ω\omega of impulse responses covering a given horizon did\_{i} frequencies.343434Note that i=−1i=\sqrt{-1}. Since the rows of the dynamic adjacency matrix do not necessarily sum up to one, we normalise the element in each row by the corresponding row sum: [θ~t,Td]j,k=[θt,Td]j,k/∑k=1N[θt,Td]j,k\Big[\widetilde{\theta}\_{t,T}^{d}\Big]\_{j,k}=\Big[\theta\_{t,T}^{d}\Big]\_{j,k}\Big/\sum\limits\_{k=1}^{N}\Big[\theta\_{t,T}^{d}\Big]\_{j,k}. Equation ([D.3](#A4.E3 "In D.1 Overview of the time-varying parameter VAR model ‣ Appendix D Global Dealer Factors: Estimation ‣ When David becomes Goliath: Repo dealer-driven bond mispricing")) fully defines a dynamic horizon-specific link between banks. Note that in the paper we denote [θ^t,d]j,k=[θ~t,Td]j,k\Big[\widehat{\theta}\_{t,d}\Big]\_{j,k}=\Big[\widetilde{\theta}\_{t,T}^{d}\Big]\_{j,k} to ease the notation burden.

To obtain the time-varying coefficient estimates
ϕ^1,t,T,…,ϕ^p,t,T\widehat{\phi}\_{1,t,T},...,\widehat{\phi}\_{p,t,T}
and the time-varying covariance matrix
Σ^t,T\widehat{\Sigma}\_{t,T}
we estimate the approximating model in Equation ([D.1](#A4.E1 "In D.1 Overview of the time-varying parameter VAR model ‣ Appendix D Global Dealer Factors: Estimation ‣ When David becomes Goliath: Repo dealer-driven bond mispricing")) using Quasi-Bayesian Local-Likelihood (QBLL) methods (Petrova, [2019](#bib.bib62)). We provide a detailed discussion of the estimation algorithm in Appendix [D.2](#A4.SS2 "D.2 Estimation of the time-varying parameter VAR model ‣ Appendix D Global Dealer Factors: Estimation ‣ When David becomes Goliath: Repo dealer-driven bond mispricing").

For the estimation we use a kernel weighting function, which gives larger weights to those observations surrounding the period whose coefficient and covariance matrices are of interest. Using conjugate priors, the (quasi) posterior distribution of the parameters of the model are available analytically. This alleviates the need to use a Markov Chain Monte Carlo (MCMC) simulation algorithm and permits the use of parallel computing.

Finally, the variance decompositions of the forecast errors from the VMA(∞\infty) representation require a truncation of the infinite horizon with a HH horizon approximation. As H→∞H\rightarrow\infty the error disappears (Lütkepohl, [2005](#bib.bib55)). We note here that HH serves as an approximating factor and has no interpretation in the time-domain. We obtain horizon specific measures using Fourier transforms and set our truncation horizon HH=100; the results are qualitatively similar for H∈{50,100,200}H\in\{50,100,200\}. In computing our measures, we also diagonalise the covariance matrix because our objective is to focus on the connections controlled for possible contemporaneous correlation in residuals of the system. The α​(u,d)\alpha(u,d) matrix embeds the causal nature of connections, and the covariance matrix Σ​(u)\Sigma(u) contains contemporaneous covariances within the off-diagonal elements.

### D.2 Estimation of the time-varying parameter VAR model

Let xtx\_{t} be an N×1N\times 1 vector generated by a stable time-varying parameter (TVP) heteroskedastic VAR model with pp lags:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xt,T=ϕ1​(t/T)​xt−1,T+…+ϕp​(t/T)​xt−p,T+ϵt,T,x\_{t,T}=\phi\_{1}(t/T)x\_{t-1,T}+\ldots+\phi\_{p}(t/T)x\_{t-p,T}+\epsilon\_{t,T}, |  | (D.4) |

where
ϵt,T=Σ−1/2​(t/T)​βt,T,βt,T∼N​I​D​(0,IM)\epsilon\_{t,T}=\Sigma^{-1/2}(t/T)\beta\_{t,T},\beta\_{t,T}\sim NID(0,I\_{M})
and
ϕ​(t/T)=(ϕ1​(t/T),…,ϕp​(t/T))⊤\phi(t/T)=(\phi\_{1}(t/T),\ldots,\phi\_{p}(t/T))^{\top}
are the time varying autoregressive coefficients.

Note that all roots of the polynomial χ​(z)=det​(IN−∑p=1Lzp​xp,t)\chi(z)=\text{det}\left(I\_{N}-\sum^{L}\_{p=1}z^{p}x\_{p,t}\right) lie outside the unit circle, and Σt−1\Sigma^{-1}\_{t} is a positive definite time-varying covariance matrix. Stacking the time-varying intercepts and autoregressive matrices in the vector ϕt,T\phi\_{t,T} with x¯t⊤=(IN⊗xt),xt=(1,xt−1⊤,…,xt−p⊤)\overline{x}^{\top}\_{t}=\left(\text{I}\_{N}\otimes x\_{t}\right),\>x\_{t}=\left(1,x^{\top}\_{t-1},\dots,x^{\top}\_{t-p}\right) and denoting the Kronecker product by ⊗,\otimes, the model can be written as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xt,T=x¯t,T⊤​ϕt,T+Σt/T−12​βt,T\displaystyle x\_{t,T}=\overline{x}^{\top}\_{t,T}\phi\_{t,T}+\Sigma^{-\frac{1}{2}}\_{t/T}\beta\_{t,T} |  | (D.5) |

We obtain the time-varying parameters of the model by employing the Quasi-Bayesian Local-Likelihood (QBLL) approach of Petrova ([2019](#bib.bib62)). The estimation of Equation ([D.4](#A4.E4 "In D.2 Estimation of the time-varying parameter VAR model ‣ Appendix D Global Dealer Factors: Estimation ‣ When David becomes Goliath: Repo dealer-driven bond mispricing")) requires re-weighting the likelihood function. The weighting function gives higher proportions to observations surrounding the time period whose parameter values are of interest. The local likelihood function at period kk is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lk​(x|θk,Σk,x¯)∝\displaystyle\text{L}\_{k}\left(x|\theta\_{k},\Sigma\_{k},\overline{x}\right)\propto |  | (D.6) |
|  |  |  |
| --- | --- | --- |
|  | |Σk|trace​(Dk)/2​exp⁡{−12​(x−x¯⊤​ϕk)⊤​(Σk⊗Dk)​(x−x¯⊤​ϕk)}\displaystyle|\Sigma\_{k}|^{\text{trace}(D\_{k})/2}\exp\left\{-\frac{1}{2}(x-\overline{x}^{\top}\phi\_{k})^{\top}\left(\Sigma\_{k}\otimes D\_{k}\right)(x-\overline{x}^{\top}\phi\_{k})\right\} |  |

The DkD\_{k} is a diagonal matrix whose elements hold the weights:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Dk\displaystyle D\_{k} | =\displaystyle= | diag​(ϱk​1,…,ϱk​T)\displaystyle\text{diag}(\varrho\_{k1},\dots,\varrho\_{kT}) |  | (D.7) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ϱk​t\displaystyle\varrho\_{kt} | =\displaystyle= | ϕT,k​wk​t/∑t=1Twk​t\displaystyle\phi\_{T,k}w\_{kt}/\sum^{T}\_{t=1}w\_{kt} |  | (D.8) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | wk​t\displaystyle w\_{kt} | =\displaystyle= | (1/2​π)​exp⁡((−1/2)​((k−t)/H)2),for​k,t∈{1,…,T}\displaystyle(1/\sqrt{2\pi})\exp((-1/2)((k-t)/H)^{2}),\quad\text{for}\>k,t\in\{1,\dots,T\} |  | (D.9) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ζT​k\displaystyle\zeta\_{Tk} | =\displaystyle= | ((∑t=1Twk​t)2)−1\displaystyle\left(\left(\sum^{T}\_{t=1}w\_{kt}\right)^{2}\right)^{-1} |  | (D.10) |

where ϱk​t\varrho\_{kt} is a normalised kernel function. wk​tw\_{kt} uses a Normal kernel weighting function. ζT​k\zeta\_{Tk} gives the rate of convergence and behaves like the bandwidth parameter HH in ([D.9](#A4.E9 "In D.2 Estimation of the time-varying parameter VAR model ‣ Appendix D Global Dealer Factors: Estimation ‣ When David becomes Goliath: Repo dealer-driven bond mispricing")). The kernel function puts a greater weight on the observations surrounding the parameter estimates at time kk relative to more distant observations.

We use a Normal-Wishart prior distribution for ϕk|Σk\phi\_{k}|\>\Sigma\_{k} for k∈{1,…,T}k\in\{1,\dots,T\}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕk|Σk∽𝒩​(ϕ0​k,(Σk⊗Ξ0​k)−1)\displaystyle\phi\_{k}|\Sigma\_{k}\backsim\mathcal{N}\left(\phi\_{0k},(\Sigma\_{k}\otimes\Xi\_{0k})^{-1}\right) |  | (D.11) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Σk∽𝒲​(α0​k,Γ0​k)\displaystyle\Sigma\_{k}\backsim\mathcal{W}\left(\alpha\_{0k},\Gamma\_{0k}\right) |  | (D.12) |

where ϕ0​k\phi\_{0k} is a vector of prior means, Ξ0​k\Xi\_{0k} is a positive definite matrix, α0​k\alpha\_{0k} is a scale parameter of the Wishart distribution (𝒲\mathcal{W}), and Γ0​k\Gamma\_{0k} is a positive definite matrix.

The prior and weighted likelihood function implies a Normal-Wishart quasi posterior distribution for ϕk|Σk\phi\_{k}|\>\Sigma\_{k} for k={1,…,T}k=\{1,\dots,T\}. Formally, let A=(x¯1⊤,…,x¯T⊤)⊤A=(\overline{x}^{\top}\_{1},\dots,\overline{x}^{\top}\_{T})^{\top} and Y=(x1,…,xT)⊤Y=(x\_{1},\dots,x\_{T})^{\top}, then:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ϕk|Σk,A,Y\displaystyle\phi\_{k}|\Sigma\_{k},A,Y | ∽\displaystyle\backsim | 𝒩​(θ~k,(Σk⊗Ξ~k)−1)\displaystyle\mathcal{N}\left(\widetilde{\theta}\_{k},\left(\Sigma\_{k}\otimes\widetilde{\Xi}\_{k}\right)^{-1}\right) |  | (D.13) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Σk\displaystyle\Sigma\_{k} | ∽\displaystyle\backsim | 𝒲​(α~k,Γ~k−1)\displaystyle\mathcal{W}\left(\widetilde{\alpha}\_{k},{\widetilde{\Gamma}}^{-1}\_{k}\right) |  | (D.14) |

with quasi posterior parameters:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ϕ~k\displaystyle\widetilde{\phi}\_{k} | =\displaystyle= | (IN⊗Ξ~k−1)​[(IN⊗A⊤​Dk​A)​ϕ^k+(IN⊗Ξ0​k)​ϕ0​k]\displaystyle\left(I\_{N}\otimes{\widetilde{\Xi}}^{-1}\_{k}\right)\left[\left({I}\_{N}\otimes{A}^{\top}{D}\_{k}{A}\right)\hat{\phi}\_{k}+\left({I}\_{N}\otimes{\Xi}\_{0k}\right)\phi\_{0k}\right] |  | (D.15) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Ξ~k\displaystyle{\widetilde{\Xi}}\_{k} | =\displaystyle= | Ξ~0​k+A⊤​Dk​A\displaystyle{\widetilde{\Xi}}\_{0k}+{A}^{\top}{D}\_{k}{A} |  | (D.16) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | α~k\displaystyle\widetilde{\alpha}\_{k} | =\displaystyle= | α0​k+∑t=1Tϱk​t\displaystyle\alpha\_{0k}+\sum^{T}\_{t=1}\varrho\_{kt} |  | (D.17) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Γ~k\displaystyle{\widetilde{\Gamma}}\_{k} | =\displaystyle= | Γ0​k+Y′​Dk​Y+Φ0​k​Γ0​k​Φ0​k⊤−Φ~k​Γ~k​Φ~k⊤\displaystyle{\Gamma}\_{0k}+{Y}^{\prime}{D}\_{k}{Y}+{\Phi}\_{0k}{\Gamma}\_{0k}{\Phi}^{\top}\_{0k}-{\widetilde{\Phi}}\_{k}{\widetilde{\Gamma}}\_{k}{\widetilde{\Phi}}^{\top}\_{k} |  | (D.18) |

where ϕ^k=(IN⊗A⊤​Dk​A)−1​(IN⊗A⊤​Dk)​y\widehat{\phi}\_{k}=\left({I}\_{N}\otimes{A}^{\top}{D}\_{k}{A}\right)^{-1}\left({I}\_{N}\otimes{A}^{\top}{D}\_{k}\right)y is the local likelihood estimator for ϕk\phi\_{k}. The matrices Φ0​k,Φ~k{\Phi}\_{0k},\>{\widetilde{\Phi}}\_{k} are conformable matrices from the vector of prior means, ϕ0​k\phi\_{0k}, and a draw from the quasi posterior distribution, ϕ~k\widetilde{\phi}\_{k}, respectively.

The motivation for employing these methods are threefold. First, we are able to estimate large systems that conventional Bayesian estimation methods do not permit. This is typically because the state-space representation of an NN-dimensional TVP VAR (pp) requires an additional N​(3/2+N​(p+1/2))N(3/2+N(p+1/2)) state equations for every additional variable. Conventional Markov Chain Monte Carlo (MCMC) methods fail to estimate larger models, which in general confine one to (usually) fewer than 6 variables in the system. Second, the standard approach is fully parametric and requires a law of motion. This can distort inference if the true law of motion is misspecified. Third, the methods used here permit direct estimation of the VAR’s time-varying covariance matrix, which has an inverse-Wishart density and is symmetric positive definite at every point in time.

In estimating the model, we use pp=2 and a Minnesota Normal-Wishart prior with a shrinkage value φ=0.05\varphi=0.05 and centre the coefficient on the first lag of each variable to 0.1 in each respective equation. The prior for the Wishart parameters are set following Kadiyala and Karlsson ([1997](#bib.bib49)). For each point in time, we run 100 simulations of the model to generate the (quasi) posterior distribution of parameter estimates. Note we experiment with various lag lengths, p={2,3,4,5}p=\{2,3,4,5\}; shrinkage values, φ={0.01,0.25,0.5}\varphi=\{0.01,0.25,0.5\}; and values to centre the coefficient on the first lag of each variable, {0,0.05,0.2,0.5}\{0,0.05,0.2,0.5\}. Network measures from these experiments are qualitatively similar. Notably, adding lags to the VAR and increasing the persistence in the prior value of the first lagged dependent variable in each equation increases computation time.

## Appendix E Additional results

### E.1 Non-Dealer Sectors and Repo Market Segmentation

We observe qualitative differences between non-dealers from different sectors. Evidence from the UK and elsewhere, e.g. Czech et al. ([2021](#bib.bib24)); Schrimpf et al. ([2020](#bib.bib64)), suggests that hedge funds and asset managers behave more procyclically than pension funds and insurance companies.353535In the “Dash-for-Cash” period, at the Gilt repo, while hedge funds and pension funds increased the demands to dealers, money market funds reduced dealers’ funding provision. In the Gilt market, Czech et al. ([2021](#bib.bib24)) document that hedge funds in aggregate did not behave as procyclically as reported by Schrimpf et al. ([2020](#bib.bib64)).363636Procyclicality here is viewed in terms of market volumes. In business cycle terms, they would be considered countercylical.

Table [E.1](#A5.T1 "Table E.1 ‣ E.1 Non-Dealer Sectors and Repo Market Segmentation ‣ Appendix E Additional results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") presents our benchmark specification in equation [8](#S4.E8 "In 4.2 Repo Market Impact ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") for two sectors, namely hedge funds & asset managers (HFs & AMs) on one hand, and pension funds & insurance companies (PFs & ICs) on the other. The left panel shows estimates for the repo segment and the right panel estimates for the reverse repo segment. Finally, each panel presents estimates for each sector as well as dealer factors, constituted by transitory and persistent shocks.

Focusing on the volume, we highlight two features of market power. First, the market power of dealers does not affect HFs & AMs, but it does affect PFs & ICs.373737In previous versions, we show that the volume of non-dealer banks is not affected by the market power of repo dealers. They are available on request. This is consistent with the fact that these institutions are responsible for most daily transactions. In our estimation of market power in Table [4](#S4.T4 "Table 4 ‣ 4.1 Market Power ‣ 4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") we show that market power decreases with a reduction in variable frequency, i.e. monthly interactions. Second, the impact of market power is higher (in absolute terms) in the reverse repo segment than in the repo segment. In terms of magnitude, the reduction in volume is small, as in the worst case it is equivalent to a reduction of 101.72=£​52.5​m10^{1.72}=\pounds 52.5m.

Table [E.1](#A5.T1 "Table E.1 ‣ E.1 Non-Dealer Sectors and Repo Market Segmentation ‣ Appendix E Additional results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") highlights that HFs & AMs and PFs & ICs highly value relationships with dealers. Estimates of both proxies, i.e. depth and frequency, are statistically significant for HFs & AMs. PFs & ICs tend to operate less frequently and that’s why Depth is the only relationship metric that is statistically significant. In terms of magnitude, just as with market power, the impact is rather small.

We now proceed to discuss market segmentation (or specialization). According to Sambalaibat ([2023](#bib.bib63)), there is evidence of segmentation if, as main dealers become more interconnected, specific non-dealer sectors also increase their funding from/to repo dealers. The common characteristic of these sectors is that they trade more frequently relative to other sectors and account for a large share of the total volume. In terms of pricing, as main dealer are more interconnected, repo rates should decrease for all sectors reflecting a centrality discount.383838The effect on pricing is also consistent with Duffie et al. ([2005](#bib.bib29)) as most sophisticated dealers, i.e. with higher intensity-adjusted bargaining power, will trade at lower prices relative to less sophisticated dealers. See Weill ([2020](#bib.bib68)); Feldhütter ([2012](#bib.bib36))

We posit that persistent and transitory shocks operate differently across non-dealers sectors, and that dealers segment the repo and the reverse repo segments when dealer factors have a heterogeneous impact across non-dealers.

Table [E.1](#A5.T1 "Table E.1 ‣ E.1 Non-Dealer Sectors and Repo Market Segmentation ‣ Appendix E Additional results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") shows how persistent and transitory shocks operate on different sectors. On the one hand, persistent shocks to dealer factors greatly increase PFs & ICs funding. For the repo segment, while HFs & AMs reduce slightly their funding in 102.3=£​199​m10^{2.3}=\pounds 199m, PFs & ICs increases their funding by large orders of magnitude. In the reverse repo segment, we observe qualitatively similar results. On the other hand, dealer-originated transitory shocks affect HFs & AMs at the reverse repo segment only. We argue that this evidence supports the segmentation (or specialization) hypothesis, as HFs & AMs are the most relevant institutions in the reverse repo segment, meanwhile PFs & ICs mostly implement long-term strategies.

Table E.1: OTC impact by sector and Persistence of shocks: Volume and Spread

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Volume | | | | | | | | |
|  | Repo segment | | | |  | Reverse Repo segment | | | |
|  | HFs & AMs | | PFs & Ics | |  | HFs & AMs | | PFs & Ics | |
| Market Power | 0.053 | 0.032 | -0.518\* | -0.373 |  | -0.128 | -0.176 | -1.717\*\*\* | -1.468\*\*\* |
|  | [0.116] | [0.114] | [0.266] | [0.234] |  | [0.258] | [0.261] | [0.556] | [0.553] |
| Depth | 0.623\*\* | 0.623\*\* | 0.963\*\*\* | 0.964\*\*\* |  | 0.514 | 0.521 | 2.154\*\* | 2.051\*\* |
|  | [0.246] | [0.246] | [0.349] | [0.352] |  | [0.327] | [0.326] | [0.864] | [0.845] |
| Frequency | 0.009\*\*\* | 0.009\*\*\* | 0.002 | 0.001 |  | 0.014\*\*\* | 0.014\*\*\* | -0.002 | -0.001 |
|  | [0.001] | [0.001] | [0.002] | [0.002] |  | [0.002] | [0.002] | [0.003] | [0.003] |
| DF tran repo | -0.046 |  | 0.353 |  |  | 4.021\*\*\* |  | -4.707 |  |
|  | [0.693] |  | [1.908] |  |  | [0.726] |  | [3.290] |  |
| DF tran reverse | -0.221 |  | -4.697 |  |  | 2.038\*\*\* |  | -5.110\* |  |
|  | [0.693] |  | [4.115] |  |  | [0.653] |  | [2.788] |  |
| DF per repo |  | 1.455 |  | 17.607\*\*\* |  |  | -1.172 |  | 12.144\* |
|  |  | [1.251] |  | [6.582] |  |  | [1.378] |  | [7.272] |
| DF per reverse |  | -2.284\*\* |  | -0.264 |  |  | 3.705\*\*\* |  | 1.996 |
|  |  | [1.045] |  | [3.844] |  |  | [1.215] |  | [7.428] |
| R-squared | 0.632 | 0.632 | 0.504 | 0.507 |  | 0.455 | 0.454 | 0.364 | 0.367 |
|  | Spread | | | | | | | | |
|  | HFs & AMs | | PFs & Ics | |  | HFs & AMs | | PFs & Ics | |
| Market Power | 0.115\*\*\* | 0.118\*\*\* | -0.205\*\*\* | -0.205\*\*\* |  | 0.564\*\*\* | 0.559\*\*\* | 0.182\*\*\* | 0.180\*\*\* |
|  | [0.008] | [0.008] | [0.027] | [0.029] |  | [0.022] | [0.022] | [0.023] | [0.023] |
| Depth | 0.001 | 0.002 | 0.005 | 0.001 |  | 0.007 | 0.007 | 0.023 | 0.024 |
|  | [0.010] | [0.010] | [0.015] | [0.015] |  | [0.012] | [0.012] | [0.017] | [0.017] |
| Frequency | -0.000 | -0.000 | -0.000 | -0.000 |  | 0.000 | 0.000 | -0.000 | -0.000 |
|  | [0.000] | [0.000] | [0.000] | [0.000] |  | [0.000] | [0.000] | [0.000] | [0.000] |
| DF tran repo | -0.147\*\*\* |  | -0.921\*\*\* |  |  | -0.139\*\*\* |  | -0.208\*\*\* |  |
|  | [0.026] |  | [0.164] |  |  | [0.030] |  | [0.061] |  |
| DF tran reverse | -0.119\*\*\* |  | 0.218\*\* |  |  | -0.082\*\*\* |  | 0.000 |  |
|  | [0.031] |  | [0.097] |  |  | [0.029] |  | [0.043] |  |
| DF per repo |  | 0.024 |  | -0.323\* |  |  | -0.045 |  | -0.131 |
|  |  | [0.053] |  | [0.189] |  |  | [0.051] |  | [0.090] |
| DF per reverse |  | -0.025 |  | 0.298 |  |  | -0.282\*\*\* |  | -0.130 |
|  |  | [0.052] |  | [0.236] |  |  | [0.056] |  | [0.121] |
| R-squared | 0.055 | 0.053 | 0.314 | 0.298 |  | 0.142 | 0.142 | 0.158 | 0.156 |
| D/ND FE | Yes | Yes | Yes | Yes |  | Yes | Yes | Yes | Yes |
| ND/D\*Week FE | Yes | Yes | Yes | Yes |  | Yes | Yes | Yes | Yes |
| Year FE | Yes | Yes | Yes | Yes |  | Yes | Yes | Yes | Yes |
| Controls | Yes | Yes | Yes | Yes |  | Yes | Yes | Yes | Yes |
| Observations | 68,781 | 68,781 | 11,955 | 11,955 |  | 85,643 | 85,643 | 9,867 | 9,867 |
| ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Note: This table reports the results of the regressions for repo market volume and rate spread (in absolute value) impact by non-dealer sector and persistence of shocks to dealers, as discussed in Section [4](#S4 "4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), for the period 2016:M1 to 2022:M1. Definitions, sources and frequency of all independent variables are presented in Section [3](#S3 "3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"). Panels report the results for the dependent variables as follows: the left panel uses repo segment transactions, and the right panel uses reverse repo segment transactions. Clustered standard errors on dealer / non-dealer dyads. | | | | | | | | | |

Table [E.1](#A5.T1 "Table E.1 ‣ E.1 Non-Dealer Sectors and Repo Market Segmentation ‣ Appendix E Additional results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing") reports the sector-specific impact on repo spread by non-dealer sector. The impact of market power on HFs & AMs has the expected sign, and in terms of magnitude, dealers with 1%1\% higher market power increase the spread in the reverse segment by 0.55 pp, while it’s only 0.11 pp for the repo segment. The impact on PFs & ICs is roughly 0.2 pp on both sides. Noticeably, impact on the repo segment has the opposite sign, i.e. −0.208-0.208 pp, probably explained by the size of transaction.

## Appendix F Tables

Table F.1: Summary statistics for the repo market by type of transaction (repo vs. reverse repo) between dealers and CCPs. Our sample only uses gilts as collateral. Volumes are expressed in 10710^{7} of sterling and the interest rate spread is relative to the BoE reference rate.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Median | Mean | SD | Min | Max | N |
|  | Repo | | | | | |
| Volume | 2.34 | 3.47 | 3.85 | 0.10 | 33.00 | 1149310 |
| Rate spread | -0.06 | -0.08 | 0.08 | -0.95 | 0.65 | 1149310 |
|  | Reverse | | | | | |
| Volume | 2.27 | 3.44 | 4.11 | 0.10 | 50.00 | 1103752 |
| Rate spread | -0.06 | -0.07 | 0.08 | -0.95 | 0.56 | 1103752 |




Table F.2: % Overnight Funding

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | OTC | |  | CCP | |
|  |  | Repo | Reverse |  | Repo | Reverse |
| Overnight Funding |  | 31.59% | 46.61% |  | 99.06% | 98.64% |
| Unique ISINs |  | 2.42 | 2.11 |  | 25.19 | 22.25 |




Table F.3: Demand Estimation with Jointly Repo and Reverse Repo Segments

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Repo and Reverse Repo Data | | | | |
| Repo Rate | -0.094 | 0.086 | -0.209\*\*\* | -0.118 | 0.129 |
|  | 0.067 | 0.075 | 0.089 | 0.100 | 0.096 |
| Residual Maturity | 0.003\*\*\* | 0.010\*\*\* | 0.010\*\*\* | 0.013\*\*\* | 0.014\*\*\* |
|  | 0.000 | 0.001 | 0.000 | 0.002 | 0.002 |
| Frequency | 0.045\*\*\* | -0.752\*\*\* | 0.0914\*\*\* | -0.369\*\*\* |  |
|  | 0.001 | 0.022 | 0.001 | 0.033 |  |
| Collateral Market Value | -0.000\*\*\* | -0.000\*\*\* | -0.000\*\*\* | -0.000\*\*\* | -0.000\*\*\* |
|  | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Sample | All | All | Restricted | Restricted | Restricted |
| Control function | no | yes | no | yes | yes |
| Month FE | yes | yes | yes | yes | yes |
| Year FE | yes | yes | yes | yes | yes |
| Obs | 12,024,349 | 12,024,349 | 10,882,728 | 10,882,728 | 10,882,728 |
| R2 | 0.0847 | 0.0931 | 0.0881 | 0.0901 | 0.0501 |
| ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | | | | |
| --- | --- | --- | --- | --- | --- |
| Note: This table reports the results of the regressions for demand estimation, as discussed in Section [3](#S3 "3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), for the period 2016:M1 to 2022:M1. Definitions, sources and frequency of all independent variables are presented in Section [3](#S3 "3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"). This tables uses all repo transactions without distinguishing between repo and reverse repo. | | | | | |




Table F.4: OTC impact by persistence of shocks: simultaneous dyads

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Log volume | | | | |
|  | Repo | |  | Reverse | |
| Market Power | -0.119 | -0.121 |  | -0.188 | -0.301 |
|  | [0.132] | [0.131] |  | [0.259] | [0.249] |
| Depth | 0.512\*\* | 0.508\*\* |  | 0.583\*\*\* | 0.585\*\*\* |
|  | [0.247] | [0.247] |  | [0.191] | [0.194] |
| Frequency | 0.009\*\*\* | 0.009\*\*\* |  | 0.009\*\*\* | 0.009\*\*\* |
|  | [0.001] | [0.001] |  | [0.001] | [0.001] |
| Log CB Reserves | -0.193 | -0.044 |  | -0.328\* | -0.148 |
|  | [0.214] | [0.243] |  | [0.170] | [0.188] |
| DF tran repo | 0.466 |  |  | 2.065\*\*\* |  |
|  | [0.627] |  |  | [0.648] |  |
| DF tran reverse | 0.796 |  |  | 1.452\*\* |  |
|  | [0.719] |  |  | [0.727] |  |
| DF per repo |  | 1.128 |  |  | -1.062 |
|  |  | [1.196] |  |  | [1.390] |
| DF per reverse |  | 0.396 |  |  | 0.583 |
|  |  | [1.267] |  |  | [1.053] |
| Dealer FE | Yes | Yes |  | No | No |
| NonDealer FE | No | No |  | Yes | Yes |
| NonDealer\*Week FE | Yes | Yes |  | No | No |
| Dealer\*Week FE | No | No |  | Yes | Yes |
| Year FE | Yes | Yes |  | Yes | Yes |
| Controls | Yes | Yes |  | Yes | Yes |
| Observations | 52,396 | 52,396 |  | 52,597 | 52,597 |
| R-squared | 0.624 | 0.624 |  | 0.596 | 0.596 |
|  | Repo rate spread | | | | |
|  | Repo | |  | Reverse | |
| Market Power | 0.103\*\*\* | 0.107\*\*\* |  | 0.581\*\*\* | 0.577\*\*\* |
|  | [0.007] | [0.007] |  | [0.023] | [0.022] |
| Depth | 0.014 | 0.015 |  | 0.025\* | 0.026\* |
|  | [0.014] | [0.014] |  | [0.014] | [0.014] |
| Frequency | -0.000 | -0.000 |  | -0.000 | -0.000 |
|  | [0.000] | [0.000] |  | [0.000] | [0.000] |
| Log CB Reserves | 0.029\*\* | 0.009 |  | 0.065\*\*\* | 0.046\*\*\* |
|  | [0.012] | [0.013] |  | [0.013] | [0.011] |
| DF tran repo | -0.158\*\*\* |  |  | -0.134\*\*\* |  |
|  | [0.030] |  |  | [0.037] |  |
| DF tran reverse | -0.119\*\*\* |  |  | -0.126\*\*\* |  |
|  | [0.037] |  |  | [0.041] |  |
| DF per repo |  | 0.047 |  |  | 0.019 |
|  |  | [0.059] |  |  | [0.062] |
| DF per reverse |  | 0.032 |  |  | -0.328\*\*\* |
|  |  | [0.076] |  |  | [0.073] |
| Dealer FE | Yes | Yes |  | No | No |
| NonDealer FE | No | No |  | Yes | Yes |
| NonDealer\*Week FE | Yes | Yes |  | No | No |
| Dealer\*Week FE | No | No |  | Yes | Yes |
| Year FE | Yes | Yes |  | Yes | Yes |
| Controls | Yes | Yes |  | Yes | Yes |
| Observations | 52,396 | 52,396 |  | 52,597 | 52,597 |
| R-squared | 0.112 | 0.110 |  | 0.142 | 0.142 |
| ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | | | | |
| --- | --- | --- | --- | --- | --- |
| Note: This table reports the results of the regressions for repo market impact for simultaneous dyads by frequency of shock to dealers, as discussed in Section [4](#S4 "4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), for the period 2016:M1 to 2022:M1. Definitions, sources and frequency of all independent variables are presented in Section [3](#S3 "3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"). Panels report the results for the dependent variables as follows: the top panel uses log of volume, and the bottom panel uses the absolute value of repo spread to the reference rate determined by Bank of England. Clustered standard errors on dealer / non-dealer dyads. | | | | | |




Table F.5: OTC impact by persistence: High Client vs Low Client

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Log volume | | | |
|  | Repo | | Reverse | |
| Market Power | -0.224\* | -0.206\* | -0.776\*\*\* | -0.792\*\*\* |
|  | [0.121] | [0.116] | [0.272] | [0.273] |
| Client High | 0.785\*\*\* | 0.781\*\*\* | 1.559\*\*\* | 1.564\*\*\* |
|  | [0.252] | [0.252] | [0.193] | [0.194] |
| Client Low | -1.091\*\*\* | -1.096\*\*\* | -0.013 | -0.005 |
|  | [0.284] | [0.284] | [0.317] | [0.320] |
| Log CB Reserves | -0.608\*\*\* | -0.326\* | 1.487\*\*\* | 1.843\*\*\* |
|  | [0.182] | [0.189] | [0.245] | [0.248] |
| DF tran repo | 2.045\*\*\* |  | 3.854\*\*\* |  |
|  | [0.630] |  | [0.748] |  |
| DF tran reverse | -0.161 |  | 2.004\*\*\* |  |
|  | [0.978] |  | [0.701] |  |
| DF per repo |  | 3.412\*\* |  | -1.482 |
|  |  | [1.445] |  | [1.330] |
| DF per reverse |  | 0.420 |  | 4.741\*\*\* |
|  |  | [1.210] |  | [1.321] |
| Dealer FE | Yes | Yes | No | No |
| NonDealer FE | No | No | Yes | Yes |
| NonDealer\*Week FE | Yes | Yes | No | No |
| Dealer\*Week FE | No | No | Yes | Yes |
| Year FE | Yes | Yes | Yes | Yes |
| Controls | Yes | Yes | Yes | Yes |
| Observations | 92,314 | 92,314 | 115,555 | 115,555 |
| R-squared | 0.568 | 0.568 | 0.420 | 0.419 |
|  | Repo rate spread | | | |
|  | Repo | | Reverse | |
| Market Power | 0.035\*\*\* | 0.040\*\*\* | 0.530\*\*\* | 0.527\*\*\* |
|  | [0.013] | [0.013] | [0.020] | [0.020] |
| Client High | -0.016 | -0.015 | 0.007 | 0.006 |
|  | [0.011] | [0.011] | [0.006] | [0.006] |
| Client Low | -0.012 | -0.012 | 0.001 | 0.001 |
|  | [0.011] | [0.011] | [0.006] | [0.006] |
| Log CB Reserves | 0.046\*\*\* | 0.025\*\*\* | 0.070\*\*\* | 0.053\*\*\* |
|  | [0.008] | [0.009] | [0.009] | [0.008] |
| DF tran repo | -0.263\*\*\* |  | -0.136\*\*\* |  |
|  | [0.039] |  | [0.025] |  |
| DF tran reverse | -0.086\*\* |  | -0.066\*\*\* |  |
|  | [0.038] |  | [0.025] |  |
| DF per repo |  | 0.022 |  | -0.031 |
|  |  | [0.067] |  | [0.041] |
| DF per reverse |  | 0.058 |  | -0.236\*\*\* |
|  |  | [0.082] |  | [0.047] |
| Dealer FE | Yes | Yes | No | No |
| NonDealer FE | No | No | Yes | Yes |
| NonDealer\*Week FE | Yes | Yes | No | No |
| Dealer\*Week FE | No | No | Yes | Yes |
| Year FE | Yes | Yes | Yes | Yes |
| Controls | Yes | Yes | Yes | Yes |
| Observations | 92,314 | 92,314 | 115,555 | 115,555 |
| R-squared | 0.075 | 0.072 | 0.129 | 0.129 |
| ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | | | |
| Note: This table reports the results of the regressions for repo market impact by frequency of shocks to repo dealers, replacing relationship trading metrics with dummy variables “High Client” and “Low Client”, as discussed in Section [4](#S4 "4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), for the period 2016:M1 to 2022:M1. Definitions, sources and frequency of all independent variables are presented in Section [3](#S3 "3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"). Panels report the results for the dependent variables as follows: the top panel uses log of volume, and the bottom panel uses the absolute value of repo spread to the reference rate determined by Bank of England. Clustered standard errors on dealer / non-dealer dyads. | | | | |




Table F.6: OTC impact by persistence, Simultaneous Dyads: High Clients vs Low Clients

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Log volume | | | |
|  | Repo | | Reverse | |
| Market Power | -0.342\*\* | -0.356\*\* | -0.488\* | -0.606\*\* |
|  | [0.151] | [0.149] | [0.286] | [0.271] |
| Client High | 0.996\*\*\* | 0.992\*\*\* | 0.919\*\*\* | 0.915\*\*\* |
|  | [0.147] | [0.147] | [0.087] | [0.087] |
| Client Low | -0.796\*\*\* | -0.799\*\*\* | -0.359\*\*\* | -0.360\*\*\* |
|  | [0.185] | [0.186] | [0.116] | [0.116] |
| Log CB Reserves | 0.232 | 0.434\* | -0.103 | 0.021 |
|  | [0.202] | [0.234] | [0.188] | [0.204] |
| DF tran repo | 0.591 |  | 2.018\*\*\* |  |
|  | [0.668] |  | [0.686] |  |
| DF tran reverse | 1.905\*\* |  | 0.842 |  |
|  | [0.812] |  | [0.735] |  |
| DF per repo |  | 0.603 |  | -1.155 |
|  |  | [1.184] |  | [1.470] |
| DF per reverse |  | 0.925 |  | -0.033 |
|  |  | [1.535] |  | [1.194] |
| Dealer FE | Yes | Yes | No | No |
| NonDealer FE | No | No | Yes | Yes |
| NonDealer\*Week FE | Yes | Yes | No | No |
| Dealer\*Week FE | No | No | Yes | Yes |
| Year FE | Yes | Yes | Yes | Yes |
| Controls | Yes | Yes | Yes | Yes |
| Observations | 52,396 | 52,396 | 52,597 | 52,597 |
| R-squared | 0.585 | 0.585 | 0.574 | 0.575 |
|  | Repo rate spread | | | |
|  | Repo | | Reverse | |
| Market Power | 0.106\*\*\* | 0.110\*\*\* | 0.581\*\*\* | 0.577\*\*\* |
|  | [0.007] | [0.007] | [0.023] | [0.022] |
| Client High | -0.001 | -0.001 | 0.005 | 0.005 |
|  | [0.004] | [0.004] | [0.008] | [0.008] |
| Client Low | 0.011 | 0.011 | 0.002 | 0.002 |
|  | [0.008] | [0.008] | [0.006] | [0.006] |
| Log CB Reserves | 0.026\*\* | 0.006 | 0.067\*\*\* | 0.048\*\*\* |
|  | [0.011] | [0.012] | [0.014] | [0.012] |
| DF tran repo | -0.159\*\*\* |  | -0.134\*\*\* |  |
|  | [0.031] |  | [0.037] |  |
| DF tran reverse | -0.125\*\*\* |  | -0.126\*\*\* |  |
|  | [0.040] |  | [0.042] |  |
| DF per repo |  | 0.053 |  | 0.024 |
|  |  | [0.061] |  | [0.063] |
| DF per reverse |  | 0.020 |  | -0.328\*\*\* |
|  |  | [0.084] |  | [0.072] |
| Dealer FE | Yes | Yes | No | No |
| NonDealer FE | No | No | Yes | Yes |
| NonDealer\*Week FE | Yes | Yes | No | No |
| Dealer\*Week FE | No | No | Yes | Yes |
| Year FE | Yes | Yes | Yes | Yes |
| Controls | Yes | Yes | Yes | Yes |
| Observations | 52,396 | 52,396 | 52,597 | 52,597 |
| R-squared | 0.104 | 0.101 | 0.141 | 0.141 |
| ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | | | |
| Note: This table reports the results of the regressions for repo market impact by frequency of shocks to repo dealers and simultaneous dyads, replacing relationship trading metrics with dummy variables “High Client” and “Low Client”, as discussed in Section [4](#S4 "4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), for the period 2016:M1 to 2022:M1. Definitions, sources and frequency of all independent variables are presented in Section [3](#S3 "3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"). Panels report the results for the dependent variables as follows: the top panel uses log of volume, and the bottom panel uses the absolute value of repo spread to the reference rate determined by Bank of England. Clustered standard errors on dealer / non-dealer dyads. | | | | |




Table F.7: OTC impact by sector, by persistence: High Client and Low Client

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Log Volume | | | | Rate spread | | | |
| Repo segment | HFs & AMs | | PFs & Ics | | HFs & AMs | | PFs & Ics | |
| Market Power | -0.165 | -0.186 | -0.312 | -0.150 | 0.117\*\*\* | 0.120\*\*\* | -0.206\*\*\* | -0.206\*\*\* |
|  | [0.137] | [0.134] | [0.333] | [0.307] | [0.008] | [0.008] | [0.029] | [0.030] |
| Client High | 0.948\*\*\* | 0.944\*\*\* | -1.458\*\* | -1.546\*\* | 0.004 | 0.004 | -0.034 | -0.039 |
|  | [0.187] | [0.188] | [0.622] | [0.662] | [0.005] | [0.005] | [0.040] | [0.037] |
| Client Low | -0.995\*\*\* | -1.000\*\*\* | -2.547\*\*\* | -2.591\*\*\* | 0.016\*\* | 0.016\*\* | -0.024 | -0.028 |
|  | [0.254] | [0.255] | [0.668] | [0.690] | [0.007] | [0.007] | [0.027] | [0.027] |
| Log CB Reserves | -0.968\*\*\* | -0.843\*\*\* | -0.801 | -0.285 | 0.032\*\*\* | 0.015 | -0.047 | -0.085\*\*\* |
|  | [0.198] | [0.205] | [0.575] | [0.538] | [0.008] | [0.009] | [0.029] | [0.030] |
| DF tran repo | 0.357 |  | 2.727 |  | -0.148\*\*\* |  | -0.885\*\*\* |  |
|  | [0.712] |  | [2.394] |  | [0.027] |  | [0.186] |  |
| DF tran reverse | 0.724 |  | -6.533 |  | -0.118\*\*\* |  | 0.172 |  |
|  | [0.784] |  | [4.355] |  | [0.032] |  | [0.115] |  |
| DF per repo |  | 1.183 |  | 17.654\*\* |  | 0.029 |  | -0.292 |
|  |  | [1.212] |  | [7.800] |  | [0.054] |  | [0.194] |
| DF per reverse |  | -1.091 |  | -0.129 |  | -0.029 |  | 0.292 |
|  |  | [1.216] |  | [3.644] |  | [0.053] |  | [0.235] |
| Dealer FE | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| NonDealer\*Week FE | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Year FE | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Controls | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Observations | 68,781 | 68,781 | 11,955 | 11,955 | 68,781 | 68,781 | 11,955 | 11,955 |
| R-squared | 0.588 | 0.588 | 0.336 | 0.326 | 0.043 | 0.040 | 0.289 | 0.265 |
|  | Log Volume | | | | Rate spread | | | |
| Reverse segment | HFs & AMs | | PFs & Ics | | HFs & AMs | | PFs & Ics | |
| Market Power | -0.382 | -0.393 | -1.746\*\*\* | -1.503\*\* | 0.563\*\*\* | 0.558\*\*\* | 0.187\*\*\* | 0.185\*\*\* |
|  | [0.279] | [0.279] | [0.643] | [0.651] | [0.022] | [0.022] | [0.025] | [0.024] |
| Client High | 1.350\*\*\* | 1.351\*\*\* | 0.418 | 0.405 | 0.009 | 0.008 | -0.009 | -0.009 |
|  | [0.136] | [0.136] | [0.705] | [0.693] | [0.007] | [0.007] | [0.011] | [0.011] |
| Client Low | -0.315 | -0.314 | -0.398 | -0.498 | 0.008 | 0.008 | -0.012 | -0.013 |
|  | [0.262] | [0.262] | [0.857] | [0.811] | [0.006] | [0.006] | [0.010] | [0.010] |
| Log CB Reserves | 0.853\*\*\* | 1.156\*\*\* | 0.424 | 0.476 | 0.089\*\*\* | 0.070\*\*\* | 0.057\*\*\* | 0.037\*\* |
|  | [0.233] | [0.241] | [0.910] | [0.915] | [0.010] | [0.009] | [0.017] | [0.017] |
| DF tran repo | 3.747\*\*\* |  | -4.909 |  | -0.137\*\*\* |  | -0.190\*\*\* |  |
|  | [0.748] |  | [3.757] |  | [0.030] |  | [0.061] |  |
| DF tran reverse | 1.475\*\* |  | -4.587\* |  | -0.088\*\*\* |  | 0.006 |  |
|  | [0.677] |  | [2.651] |  | [0.030] |  | [0.044] |  |
| DF per repo |  | -1.400 |  | 12.365\* |  | -0.040 |  | -0.129 |
|  |  | [1.452] |  | [7.278] |  | [0.051] |  | [0.093] |
| DF per reverse |  | 4.203\*\*\* |  | 1.966 |  | -0.282\*\*\* |  | -0.124 |
|  |  | [1.249] |  | [7.071] |  | [0.056] |  | [0.126] |
| NonDealer FE | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Dealer\*Week FE | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Year FE | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Controls | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Observations | 85,643 | 85,643 | 9,867 | 9,867 | 85,643 | 85,643 | 9,867 | 9,867 |
| R-squared | 0.402 | 0.401 | 0.362 | 0.364 | 0.138 | 0.139 | 0.138 | 0.135 |
| ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | | | | | | | |
| Note: This table reports the results of the regressions for repo market impact by frequency of shocks to repo dealers and non-dealer sectors, replacing relationship trading metrics with dummy variables “High Client” and “Low Client”, as discussed in Section [4](#S4 "4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), for the period 2016:M1 to 2022:M1. Definitions, sources and frequency of all independent variables are presented in Section [3](#S3 "3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"). Panels report the results for the dependent variables as follows: the top panel uses log of volume, and the bottom panel uses the absolute value of repo spread to the reference rate determined by Bank of England. Clustered standard errors on dealer / non-dealer dyads. | | | | | | | | |




Table F.8: Mispricing: One-day mispricing lag

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | All | | Short | | Medium | | Long | |
| Markup | 0.248\* | 0.270\* | 0.385 | 0.393 | 0.194 | 0.219 | 0.100 | 0.127 |
|  | [0.143] | [0.144] | [0.267] | [0.264] | [0.256] | [0.254] | [0.158] | [0.158] |
| Markdown | -0.175 | -0.147 | 0.542 | 0.558 | -0.168 | -0.149 | -0.436\* | -0.400 |
|  | [0.200] | [0.193] | [0.353] | [0.351] | [0.244] | [0.238] | [0.255] | [0.245] |
| DF tran repo | -0.134 |  | -0.500 |  | -0.170 |  | 0.051 |  |
|  | [1.304] |  | [1.169] |  | [1.484] |  | [1.547] |  |
| DF tran reverse | 0.122 |  | 0.517 |  | 0.389 |  | 0.090 |  |
|  | [1.382] |  | [1.355] |  | [1.515] |  | [1.752] |  |
| DF per repo |  | -1.782 |  | -0.400 |  | -1.595 |  | -3.073 |
|  |  | [1.567] |  | [1.674] |  | [1.630] |  | [1.949] |
| DF per reverse |  | 0.091 |  | -0.504 |  | -0.533 |  | 0.803 |
|  |  | [1.865] |  | [2.082] |  | [2.089] |  | [2.133] |
| CB Market Share | -0.045 | -0.044 | 0.231\* | 0.225\* | -0.046 | -0.053 | -0.031 | -0.020 |
|  | [0.048] | [0.049] | [0.126] | [0.127] | [0.067] | [0.068] | [0.083] | [0.086] |
| Log CB Reserves | 0.010 | -0.157 | -0.581\*\* | -0.626\*\*\* | 0.041 | -0.115 | 0.364 | 0.101 |
|  | [0.318] | [0.242] | [0.254] | [0.212] | [0.349] | [0.264] | [0.378] | [0.305] |
| Bond\*Month FE | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Year FE | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Controls | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Observations | 21,532 | 21,532 | 5,222 | 5,222 | 7,507 | 7,507 | 8,799 | 8,799 |
| R-squared | 0.041 | 0.042 | 0.024 | 0.024 | 0.031 | 0.032 | 0.056 | 0.059 |
| ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Note: This table reports the results of the regressions for bond-level one-day-ahead mispricing, as discussed in Section [4](#S4 "4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), for the period 2016:M1 to 2022:M1. Definitions, sources and frequency of all independent variables are presented in Section [3](#S3 "3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"). The dependent variable is the absolute value of the spread between the bond-level yield and the predicted yield based on a spline. We use Driscoll-Kraay standard errors with 20 working days lag. | | | | | | | | |




Table F.9: Mispricing benchmark: Three-day mispricing lag

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | All | | Short | | Medium | | Long | |
| Markup | 0.441\*\* | 0.486\*\*\* | 0.180 | 0.242 | 0.595\* | 0.625\* | 0.221 | 0.242 |
|  | [0.191] | [0.187] | [0.370] | [0.363] | [0.337] | [0.331] | [0.183] | [0.179] |
| Markdown | 0.135 | 0.191 | 1.124\* | 1.222\*\* | 0.245 | 0.290 | -0.257 | -0.228 |
|  | [0.300] | [0.294] | [0.573] | [0.571] | [0.339] | [0.334] | [0.323] | [0.314] |
| DF tran repo | -1.543 |  | -3.857\*\*\* |  | -1.416 |  | -0.127 |  |
|  | [1.589] |  | [1.372] |  | [1.796] |  | [1.781] |  |
| DF tran reverse | -0.834 |  | -1.804 |  | -0.008 |  | -0.598 |  |
|  | [1.777] |  | [2.105] |  | [1.870] |  | [2.018] |  |
| DF per repo |  | -1.868 |  | -2.630 |  | -1.698 |  | -1.796 |
|  |  | [2.317] |  | [2.773] |  | [2.337] |  | [2.663] |
| DF per reverse |  | 2.084 |  | 4.308 |  | 1.367 |  | 1.199 |
|  |  | [2.524] |  | [3.247] |  | [2.841] |  | [2.863] |
| CB Market Share | -0.096\* | -0.099\* | -0.070 | -0.094 | -0.158\*\* | -0.157\*\* | -0.020 | -0.019 |
|  | [0.055] | [0.055] | [0.136] | [0.134] | [0.069] | [0.070] | [0.093] | [0.094] |
| Log CB Reserves | -0.013 | -0.293 | -0.301 | -0.852\*\* | -0.076 | -0.289 | 0.358 | 0.173 |
|  | [0.356] | [0.339] | [0.398] | [0.383] | [0.402] | [0.366] | [0.364] | [0.353] |
| Bond\*Month FE | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Year FE | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Controls | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Observations | 15,089 | 15,089 | 3,639 | 3,639 | 5,269 | 5,269 | 6,174 | 6,174 |
| R-squared | 0.038 | 0.037 | 0.057 | 0.052 | 0.032 | 0.032 | 0.042 | 0.043 |
| ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Note: This table reports the results of the regressions for bond-level three-days-ahead mispricing, as discussed in Section [4](#S4 "4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), for the period 2016:M1 to 2022:M1. Definitions, sources and frequency of all independent variables are presented in Section [3](#S3 "3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"). The dependent variable is the absolute value of the spread between the bond-level yield and the predicted yield based on a spline. We use Driscoll-Kraay standard errors with 20 working days lag. | | | | | | | | |




Table F.10: Mispricing benchmark: Five-day mispricing lag

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | All | | Short | | Medium | | Long | |
| Markup | 0.159 | 0.230 | 0.084 | 0.110 | 0.228 | 0.282 | 0.084 | 0.154 |
|  | [0.179] | [0.180] | [0.362] | [0.369] | [0.299] | [0.307] | [0.214] | [0.211] |
| Markdown | 0.113 | 0.198 | 0.459 | 0.508 | 0.419 | 0.524\* | -0.245 | -0.155 |
|  | [0.249] | [0.251] | [0.493] | [0.489] | [0.313] | [0.314] | [0.265] | [0.267] |
| DF tran repo | -2.613\* |  | -2.406 |  | -3.527\*\* |  | -2.022 |  |
|  | [1.559] |  | [1.732] |  | [1.796] |  | [1.713] |  |
| DF tran reverse | -1.711 |  | -0.096 |  | -0.749 |  | -2.504 |  |
|  | [1.909] |  | [2.431] |  | [2.076] |  | [2.097] |  |
| DF per repo |  | -1.396 |  | -0.125 |  | -1.551 |  | -1.836 |
|  |  | [2.609] |  | [3.449] |  | [2.782] |  | [2.551] |
| DF per reverse |  | 1.916 |  | 0.996 |  | 1.958 |  | 1.412 |
|  |  | [3.164] |  | [4.410] |  | [3.495] |  | [2.923] |
| CB Market Share | -0.052 | -0.065 | -0.043 | -0.059 | -0.038 | -0.036 | 0.022 | 0.011 |
|  | [0.069] | [0.070] | [0.133] | [0.137] | [0.082] | [0.084] | [0.116] | [0.114] |
| Log CB Reserves | 0.084 | -0.276 | -0.576 | -0.733\* | -0.028 | -0.396 | 0.532 | 0.104 |
|  | [0.387] | [0.363] | [0.443] | [0.428] | [0.428] | [0.386] | [0.403] | [0.380] |
| Bond\*Month FE | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Year FE | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Controls | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Observations | 15,547 | 15,547 | 3,759 | 3,759 | 5,457 | 5,457 | 6,326 | 6,326 |
| R-squared | 0.161 | 0.158 | 0.078 | 0.075 | 0.107 | 0.103 | 0.261 | 0.259 |
| ∗p<<0.1; ∗∗p<<0.05; ∗∗∗p<<0.01 | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Note: This table reports the results of the regressions for bond-level five-days-ahead mispricing, as discussed in Section [4](#S4 "4 Results ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"), for the period 2016:M1 to 2022:M1. Definitions, sources and frequency of all independent variables are presented in Section [3](#S3 "3 Empirics ‣ When David becomes Goliath: Repo dealer-driven bond mispricing"). The dependent variable is the absolute value of the spread between the bond-level yield and the predicted yield based on a spline. We use Driscoll-Kraay standard errors with 20 working days lag. | | | | | | | | |

BETA