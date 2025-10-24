---
authors:
- Rosella Giacometti
- Gabriele Torri
- Marco Bonomelli
- Davide Lauria
doc_id: arxiv:2510.20434v1
family_id: arxiv:2510.20434
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings'
url_abs: http://arxiv.org/abs/2510.20434v1
url_html: https://arxiv.org/html/2510.20434v1
venue: arXiv q-fin
version: 1
year: 2025
---


R. Giacometti
University of Bergamo, Department of Management, Via dei Caniana, 2, Bergamo, 24127, BG, Italy.

G. Torri
CONTACT G. Torri. Email: gabriele.torri@unibg.it
University of Bergamo, Department of Management, Via dei Caniana, 2, Bergamo, 24127, BG, Italy.

M. Bonomelli
University of Bergamo, Department of Management, Via dei Caniana, 2, Bergamo, 24127, BG, Italy.

D. Lauria
University of Bergamo, Department of Management, Via dei Caniana, 2, Bergamo, 24127, BG, Italy.

(October 23, 2025)

###### Abstract

In this work, we aim to develop a market-implied sustainability score for companies, based on the extent to which a stock is over- or under-represented in sustainable funds compared to traditional ones. To identify sustainable funds, we rely on the Sustainable Finance Disclosure Regulation (SFDR), a European framework designed to clearly categorize investment funds into different classes according to their commitment to sustainability. In our analysis, we classify as sustainable those funds categorized as Article 9 – also known as “dark green” – and compare them to funds categorized as Article 8 or Article 6.

We compute an SFDR Market-Implied Sustainability (SMIS) score for a large set of European companies. We then conduct an econometric analysis to identify the factors influencing SMIS and compare them with state-of-the-art ESG (Environmental, Social, and Governance) scores provided by Refinitiv. Finally, we assess the realized risk-adjusted performance of stocks using portfolio-tilting strategies.

Our results show that SMIS scores deviate substantially from traditional ESG scores and that, over the period 2010–2023, companies with high SMIS have been associated with significant financial outperformance.

Keywords: Sustainable finance; Financial regulation; Investment strategy; quantile regression; Risk-adjusted performance.

## 1 Introduction

Sustainable investing has emerged as a pivotal strategy in the financial landscape, and investors can contribute to the transition to a more sustainable economy by directing their capital towards investments labelled as “sustainable” or “green”. This class of investments known as Socially Responsible Investments (SRI) has been studied since the late 1980s by scholars and practitioners (see, e.g., Bruyn [1987](https://arxiv.org/html/2510.20434v1#bib.bib9) and Hylton [1992](https://arxiv.org/html/2510.20434v1#bib.bib24)). SRI strategies combine ethical, social, environmental or corporate governance criteria to the “standard” financial ones (see, e.g. Sandberg et al. [2009](https://arxiv.org/html/2510.20434v1#bib.bib35)). Still, there does not seem to exist an universally accepted definition of SRI. Throughout the years, the demand for SRI has significantly grown (Eurosif [2018](https://arxiv.org/html/2510.20434v1#bib.bib14), GSIA [2020](https://arxiv.org/html/2510.20434v1#bib.bib20)), mainly because of the increased attention of the stakeholders with respect to social issues. Furthermore, the growing popularity of ESG investing in recent years was driven not only by the increased attention to environmental and social sustainability, but also for the supposed benefits in terms risk-adjusted performance, as sustainability may help to better manage risks and seize opportunities (see Amel-Zadeh and Serafeim [2018](https://arxiv.org/html/2510.20434v1#bib.bib1); Becchetti et al. [2018](https://arxiv.org/html/2510.20434v1#bib.bib2)). However, the empirical evidence regarding the financial performance of ESG funds remains mixed, with debates surrounding the potential trade-off between social responsibility and risk-adjusted returns (see Revelli and Viviani [2015](https://arxiv.org/html/2510.20434v1#bib.bib33) and Hornuf and Yüksel [2024](https://arxiv.org/html/2510.20434v1#bib.bib23)).

Similarly to credit risk, where in the early 1900s ratings and scores began to be applied to securities in order to evaluate a debtor’s ability to pay back debt and the likelihood of default, ratings and scores able to measure of “greenness” were needed.
Nowadays, investors interested in sustainable investing can rely on several specialized ESG rating agencies that provide scores and analyses of the sustainable performance of companies. Investors can use these assessments to make informed decisions about which stocks to include in their portfolio.
Over the past decade, the proliferation of ESG scores has provided investors with a framework to assess the sustainability and ethical impact of their portfolios. However, despite the rising popularity of ESG investing, challenges persist due to the lack of consistency in ESG scores across different rating agencies and the absence of universally accepted standards (see e.g. Billio et al. [2021](https://arxiv.org/html/2510.20434v1#bib.bib8)).

The rise in mainstream popularity, together with the lack of clear ESG definitions, the heterogeneous diffusion of rigorous reporting requirements, and the desire to please consumers and investors may increase the risk of greenwashing practices.111The term greenwashing is defined by the Concise Oxford English Dictionary as: “Disinformation disseminated by an organization so as to present an environmentally responsible public image; a public image of environmental responsibility promulgated by or for an organization, etc., but perceived as being unfounded or intentionally misleading” (see also de Freitas Netto et al. [2020](https://arxiv.org/html/2510.20434v1#bib.bib18)). However, there is a belief that the situation may be improving due to increased investor awareness, potential reputational damage, accountability of boards of directors, and the impact of legislation and regulatory actions.
In order to enhance transparency on sustainability-related considerations in investments and help channel capital to investments contributing towards the transition to a sustainable economy, regulatory initiatives such as the Sustainable Finance Disclosure Regulation (SFDR) have been introduced. The SFDR is one of the legislative measures from the European Commission’s Action Plan on Sustainable Finance, and it has been introduced in 2019 together with the Taxonomy Regulation and the Low Carbon Benchmarks Regulation.
The SFDR requires asset managers to provide prescript and standardised disclosures on how ESG factors are integrated at both entity and product level. A significant portion of the SFDR applies to all asset managers, whether or not they have an express ESG or sustainability focus.
The SFDR framework categorizes funds into different classes based on their sustainability objectives, providing investors with valuable information on the environmental and social characteristics of investment products.
Asset managers have to classify their funds according to one of these three classes:

* •

  Article 9: Funds that have sustainable investment as their objective (dark green);
* •

  Article 8: Funds that promote environmental or social characteristics (light green);
* •

  Article 6: Funds without a sustainability scope.

This paper uses the information embedded in a comprehensive dataset of funds’ ownership information to synthesize the market-implied sustainability score of companies. At the core of our approach is the idea that if funds with a strong focus on sustainability (SFDR article 9 “dark green” funds) are more likely to invest in a certain asset compared to the rest of the funds, such asset is perceived by the market as highly sustainable. On the contrary, if “dark green” funds invest less in a stock compared to other funds, such asset is less sustainable. Starting form this intuition, for each company we compute a SMIS or SFDR Market-Implied Sustainability score for ii-th company: SMISi\textit{SMIS}\_{i}. We then study the properties of these scores, comparing them to traditional ESG scores. Finally, we contribute to the debate on the relation between sustainable investing and financial performance by using SMIS and ESG scores in a portfolio management framework introducing optimal portfolio tilting strategies.

The paper is structured as follow: Section [2](https://arxiv.org/html/2510.20434v1#S2 "2 Measuring sustainability - ESG scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") introduces ESG as a measure of sustainability. In Section [3](https://arxiv.org/html/2510.20434v1#S3 "3 The SFDR framework ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") we present the SFDR framework. Section [4](https://arxiv.org/html/2510.20434v1#S4 "4 SFDR market-implied sustainability scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") is devoted to presentation of the research questions and the methodology applied to derive the SMIS scores. Section [6](https://arxiv.org/html/2510.20434v1#S6 "6 Explaining the SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") and [7](https://arxiv.org/html/2510.20434v1#S7 "7 Portfolio tilting ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") are devoted to the empirical analysis and the portfolio tilting. Section [8](https://arxiv.org/html/2510.20434v1#S8 "8 Conclusions ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") concludes.

## 2 Measuring sustainability - ESG scores

ESG, an acronym for Environmental, Social, and Governance, represents the three fundamental pillars utilized in assessing the sustainability and ethical impact of investments. Originating from the 2004 “Who Cares Wins” report by the United Nations Global Compact, in collaboration with financial institutions, ESG emerged as a framework to encourage the financial industry to integrate environmental, social, and governance considerations into analysis, asset management, and securities brokerage (The Global Compact [2004](https://arxiv.org/html/2510.20434v1#bib.bib37)). Serving as a simplified tool for comparing firms in terms of their sustainability objectives, ESG scores have gained prominence in the last decade, propelled by improved non-financial reporting quality and increased data providers. The advantages lie in providing a streamlined method for assessing firms, fostering transparency through standardized data, and encouraging companies to enhance sustainability reporting. According to Amel-Zadeh and Serafeim ([2018](https://arxiv.org/html/2510.20434v1#bib.bib1)), the most significant motivation for incorporating ESG factors is related to financial performance, as sustainability factors are perceived as relevant to investment returns. That is, investors believe that ESG data can be used to identify potential risks and opportunities, and that such information is not yet fully incorporated into market prices. Hence, ESG information should help investors to control risk better and improve their financial performance. The empirical information however is mixed: the meta-analysis conducted by Revelli and Viviani ([2015](https://arxiv.org/html/2510.20434v1#bib.bib33)) shows that sustainable and responsible investing (SRI) is neither a weakness nor a strength compared with conventional investing.
Responsible companies are typically viewed as more secure due to the fact that stakeholders are less likely to engage conflicts with them (see, e.g., Freeman [2010](https://arxiv.org/html/2510.20434v1#bib.bib17)), or boycott them (see Luo and Balvers [2017](https://arxiv.org/html/2510.20434v1#bib.bib28)). On the other hand, “sin” stocks, i.e., those belonging to the alcohol, tobacco and gaming industries, tend to experience higher expected returns with respect to “regular” stocks (see, e.g., Fabozzi et al. [2008](https://arxiv.org/html/2510.20434v1#bib.bib15), Hong and Kacperczyk [2009](https://arxiv.org/html/2510.20434v1#bib.bib22)). The performance of sustainable stocks may also be positively affected by their growing demand by investors, as demonstrated by Van der Beck ([2021](https://arxiv.org/html/2510.20434v1#bib.bib3)) that shows how the performance of ESG stocks is strongly driven by the price impact from flows towards ESG funds. Finally, recent studies suggest that financial performance may be more influenced by ESG-related controversies than by overall ESG scores. Rating agencies such as Refinitiv and Sustainalytics provide specific indicators to capture these controversies. Dorfleitner et al. ([2020](https://arxiv.org/html/2510.20434v1#bib.bib12)) show that portfolio strategies dependent on the controversies scores can generate significant overperformance, and Elamer and Boulhaga ([2024](https://arxiv.org/html/2510.20434v1#bib.bib13)) show a significant negative relation between the presence of ESG controversies and firm performance.

The widespread diffusion of ESG scores generates several challenges, including a lack of consistency in scores across rating agencies, absence of a universally accepted standard leading to diverse methodologies, and subjectivity in the evaluation process. These issues underscore the complexity of ESG evaluation, with variations among agencies and potential difficulties in estimating indicators when companies do not report comprehensive data (Billio et al. [2021](https://arxiv.org/html/2510.20434v1#bib.bib8); Berg et al. [2022](https://arxiv.org/html/2510.20434v1#bib.bib7)). The disagreement across ESG data providers may increase the complexity of assessing the relationship between ESG and financial performances, as highlighted by Gibson Brandon et al. ([2021](https://arxiv.org/html/2510.20434v1#bib.bib19)) that found the presence of a risk premium for firms with high ESG disagreement.

In the last decade ESG investing become a relevant trend in the industry, leading to large inflows and rebranding of popular investment funds. Since 2023 however, due to underwhelming performances and decrease in interest the trend is reverting, with net inflows to sustainable funds lagging behind the rest of the market, and a growing number of sustainable funds closures (Morningstar Sustainalytics [2024a](https://arxiv.org/html/2510.20434v1#bib.bib31)).

## 3 The SFDR framework

The Sustainable Finance Disclosure Regulation (SFDR) is a set of rules introduced by the European Commission on 27th November 2019 related to sustainability‐disclosures in the financial services sector. The framework aims to improve the transparency of financial products, imposing to asset managers and financial advisers to communicate clearly to customers the process of integration of sustainability concerns, the effects of such integration on the financial performance, and the impact on the environment and society (<https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32019R2088>).

The financial products involved are portfolio managed in accordance with mandates given by clients on a discretionary client-by-client basis where such portfolios include one or more financial instrument, Alternative Investment Funds (AIFs), Insurance-Based Investment Products (IBIPs), pension products and schemes, Pan-European Personal Pension Product (PEPP) and Undertakings for the Collective Investment in Transferable Securities (UCITS). The framework defines the rules that must be followed to justify sustainability claims for financial products, and it does not force market participants to incorporate sustainability criteria in the investment process.

Focusing our attention of UCITS funds,222UCITS is a regulatory framework that allows for the sale of cross-boundary mutual funds for EU member states, created so that retail investors have transparent, regulated, and cross-border investment opportunities. asset managers have to classify their funds according to one of these three classes:

* •

  Article 9, also known as “products targeting sustainable investments” or dark green, covers products targeting bespoke sustainable investments and applies “[…] where a financial product has sustainable investment as its objective”.
* •

  Article 8: Funds that promote environmental or social characteristics (light green); a financial product promotes, among other goals, environmental or social targets, or a combination of those, provided that the companies in which the investments are made follow good governance practices. They are also known as “environmental and socially promoting”.
* •

  Article 6: Funds without a sustainability scope. Article 6 covers funds which do not integrate any kind of sustainability into the investment process and could include stocks currently excluded by ESG funds such as tobacco companies or thermal coal producers. While these will be allowed to continue to be sold in the EU, provided they are clearly labelled as non-sustainable, they may face considerable marketing difficulties when matched against more sustainable funds.

In the first years after the implementation of the SFDR, the universe of funds classified as “light green” (Article 8) or “dark green” (Article 9) continued to evolve, with persistent concerns about green washing and regulatory uncertainty. Morningstar Sustainalytics ([2024b](https://arxiv.org/html/2510.20434v1#bib.bib32)) reports the assets of Article 8 and Article 9 funds exceeded €6 trillion at the end September 2024. The two fund groups represent a consistent share of the European universe at 59.2%. Still, “dark green” funds represent only 3.3% of the total asset under management. Scheitza and Busch ([2024](https://arxiv.org/html/2510.20434v1#bib.bib36)) analysed the characteristics of Article 9 funds, finding that in 2023, two years after the beginning of the implementation, 60% of the funds followed an impact-oriented strategy, while the remaining 40% of funds follow a general ESG strategy. In contrast, the group of funds that was initially classified as Article 9, and later downgraded to Article 6, was less focused on impact-oriented strategies (pursued by 26% of the funds), and the remaining 74% followed a general ESG approach.

The Sustainable Finance Disclosure Regulation is currently under revision with the goal of improving clarity, transparency, and consistency. Key updates include the end of Article 8 and 9 Labels. These will be replaced with two voluntary new categories: Sustainable Products (for investments already sustainable) and Transition Products (for investments improving their sustainability). Further changes will be the introduction of clearer definitions (core terms like “sustainable investment” will be better aligned with the EU Taxonomy, reducing ambiguity), more emissions transparency (asset managers must report detailed greenhouse gas emission targets, metrics, and methodologies). The SFDR reform was proposed by the European Commission, following recommendations from European Supervisory Authorities. As a result, the European Commission launched a public consultation (“Call for Evidence”) on May 2, 2025, to gather stakeholder feedback on how to simplify and improve the SFDR.333<https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14666-Revision-of-EU-rules-on-sustainable-finance-disclosure_en>

## 4 SFDR market-implied sustainability scores

A set of research questions arise quite spontaneously, related to the different nature of information conveyed in these two frameworks, one (ESG) originated from rating agency and the other (SFDR) from asset managers’ perceptions.
First, we aim to investigate if there is a relationship between ESG and SFDR funds’ categorization. In other words, do the SFDR 9 “dark green funds” invest in stocks with high ESG scores? ESG scores represent an apparently objective way to measure the sustainability of the companies, and one may naturally think that “dark green funds” tend to invest more in highly rated companies. The wide diversity among sustainable investment strategies (exclusion strategies, best in class approaches, impact investing, etc.), together with the high level of disagreement between ESG data providers (see Billio et al. [2021](https://arxiv.org/html/2510.20434v1#bib.bib8)) may however reduce or cancel the potential relation between the investment strategy of SFDR 9 funds and a specific set of ESG scores.

Our second goal is to develop an indicator based on the composition of SFDR 9 “dark green” funds that synthesize the sustainability analysis of funds managers usable as a implied sustainability score. ESG scores are evaluation criteria typically computed on the basis of specific sustainability indicators appropriately weighted and aggregated to provide a synthetic evaluation. The choice of such indicators, the transformation applied to the raw data, and the weighting scheme used by the data provider strongly affects the final evaluation. These modeling decisions are highly subjective, as they depend on the specific goals of an investor or analyst. The presence of a widely accepted and well codified classification of funds may help us to create a market-based sustainability scores according to which an asset is evaluated as more sustainable if it is over-represented in SFDR 9 funds compared to other – less sustainable – investment funds.

Finally, we explore the possibility to use the implied sustainability scores to improve the financial performances of a portfolio. The empirical literature shows mixed results for performance of sustainable investing. The comparison however is complex due to the high heterogeneity of ESG scores across data providers and diversified strategies of sustainable funds. In this work we aim to test the effect on financial performance of our SMIS scores where starting from a benchmark portfolio, the asset weights are tilted up or down either by a fixed quantity or in an optimal way based on the scores.

We propose the SFDR market-implied sustainability score (SMIS score) as a novel indicator able to synthesize the sustainability analysis of funds managers. It relies on comprehensive portfolio ownership data to unveil latent signals about the sustainability analysis of fund manager on the individual assets. By scrutinizing the ownership patterns of investment funds and comparing the allocations of “dark green funds” SFDR 9 to the rest of the market, we explore how market participants implicitly factor in ESG considerations when constructing their portfolios. This methodology offers a dynamic perspective on the perceived sustainability of companies and allows for a nuanced understanding of how market forces influence the ESG landscape.

The core of our approach is to identify which assets are over/under-invested in SFDR 9 funds compared to other funds. In particular, for each quarter we identify two groups of funds: SFDR 9 on one side (the most sustainable “dark green funds”), and SFDR 6 and 8 on the other (funds that have limited or no focus on sustainability). Then, for each asset we compute the percentage of funds in each group with a non-zero exposure in it, and we take the difference. Let ii be the index of the ii-th security, its SMIS score is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SMISi=p9,i−pU\9,i\textit{SMIS}\_{i}=p\_{9,i}-p\_{U\backslash 9,i} |  | (1) |

where:

* •

  U is set of indices characterising the different SFDR type, i.e. U={9,8,6}U=\{9,8,6\},
* •

  p9,ip\_{9,i} is the % of SFDR 9 funds with asset ii-th in portfolio,
* •

  pU\9,ip\_{U\backslash 9,i} is % of other funds with asset ii-th in portfolios.444In this paper we present the results obtained comparing article 9 funds’ compositions versus all the other funds ones but different comparisons are possible. We obtained similar results comparing article 9 funds’ compositions versus article 6 ones.

Assuming long-only positions, the indicator is bounded between −1-1 and 11, with positive values denoting assets that are over-represented in the SFDR 9 funds (hence implicitly more sustainable), and negative values denoting assets that are under-represented in such funds (less sustainable).

Furthermore, we point out that the measure that we provide is relative, and not absolute, as it uses the market funds as a baseline: a score of zero denotes a prevalence of a stock in SFDR 9 funds equivalent to the prevalence in the rest of the market, and is not tied to a specific level of sustainability. As a consequence, an increased level of sustainability across companies, or a rising concern for the sustainability among the managers of non-SFDR 9 funds may lead to a change in the baseline, making the comparison of the scores between different time periods problematic.

The indicator is informative when the values are different from zero. Indeed, zero values can be caused by either very small percentages of funds invested in a specific stock, or no difference from the rest of the market. It is therefore relevant to assess the statistical significance of the results, testing if the score is different from zero. Since the score can be interpreted as a comparison of proportions, we can use a standard statistical test. Let p9,ip\_{9,i} be the percentage of SFDR funds with asset ii-th in the portfolio, and pU\9,ip\_{U\backslash 9,i} the percentage in SFDR 6 and 8 funds, the test statistic for test the null hypothesis H0:p9,i−pU\9,i=0H\_{0}:p\_{9,i}-p\_{U\backslash 9,i}=0 is:

|  |  |  |
| --- | --- | --- |
|  | Z=p9,i−pU\9,ip​(1−p)​(1n1+1n2),Z=\displaystyle\frac{p\_{9,i}-p\_{U\backslash 9,i}}{\sqrt{p(1-p)(\frac{1}{n\_{1}}+\frac{1}{n\_{2}})}}, |  |

where p=S1,i+S2,in1+n2p=\frac{S\_{1,i}+S\_{2,i}}{n\_{1}+n\_{2}}, n1n\_{1} and n2n\_{2} are the number of SFDR 9 and other funds, respectively, and S1,iS\_{1,i}, S2,iS\_{2,i} are the corresponding number of funds with asset ii in their portfolios.

In Appendix [A](https://arxiv.org/html/2510.20434v1#A1 "Appendix A Alternative SFDR market-implied sustainability scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") we present an alternative approach to compute the SMIS scores (that we define SMISw) that compares the average weights of the exposure to a specific asset among SFDR 9 and the other funds (rather than the percentage of funds with such asset in the portfolio). The advantage of this alternative method is to consider not only the presence of the asset in a fund, but also the relative portfolio weight. This comes at the cost of more noisy information, due to the fact that the asset management strategies may be very diversified across funds, and the effect of outliers would be more marked.

A similar approach to SMIS has been used also by Lambillon and Chesney ([2023](https://arxiv.org/html/2510.20434v1#bib.bib27)), that compute a greenness index of stocks based on the presence of such companies in SFDR 9 portfolios. Differently from us, they do not account for the presence of the stocks in other non-SFDR 9 funds. This results in a bias towards the stocks that are more popular in general, irregardless of the sustainability of the fund. Indeed, such approach cannot differentiate between assets chosen by SFDR 9 funds due to their good sustainability profile, and the ones chosen due to other factors such as good risk adjusted performance, or high capitalization. With our indicator instead, a company that is highly capitalized or that is perceived positively by the market is expected to be included in a large percentage of SFDR 9 funds, but if it is equally invested in other less sustainable funds, the score will be close to zero. Similarly, a stock with a smaller capitalization or mediocre financial performance, may be included in a limited percentage of SFDR 9 funds, but if the percentage is even smaller in other funds, the implied score would be positive, signalling of a high level of sustainability.

Our approach is also related to the one proposed by Van der Beck ([2021](https://arxiv.org/html/2510.20434v1#bib.bib3)), that uses an indicator similar to SMIS to study the effect of investment flows to ESG funds on stock prices. Differently from us, he creates two aggregate portfolios, one composed of a set of ESG equity funds (weighted by asset under management), the other by all mutual funds, then computes a revealed-preference measure of investors’ ESG taste for a stock by taking the difference of the weights in the two portfolios. Compared to our approach, Van der Beck ([2021](https://arxiv.org/html/2510.20434v1#bib.bib3)), by aggregating the weights of different funds, and considering their asset under management, gives more emphasis on the aggregate exposures, overweighting the role of large funds. The aggregation of portfolio weights makes this approach similar to the alternative measures that we compute in Appendix [A](https://arxiv.org/html/2510.20434v1#A1 "Appendix A Alternative SFDR market-implied sustainability scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings"). A relevant difference is that the selection of ESG funds in such paper is not related to the SFDR, but it is instead based on the presence of ESG-related keywords in the name of the funds.

## 5 Computation of SMIS scores

### 5.1 Dataset description

In order to study the composition of SFDR funds and to compute the SMIS scores, we use a unique dataset that includes the historical portfolio composition for a panel of approximately 500 equity investment funds and ETFs with geographic focus on Europe by Lipper.555Data up to December 2020 have been retrieved using Factset, while for the period 2021-2023 we downloaded them from Refinitiv Eikon. The dataset covers the period 2002-2023, and has quarterly frequency. The coverage of the dataset grows over time, with 108 funds in 2002 and 607 in 2023.666For some of the funds the portfolio composition was missing for some quarters. In case a single quarter was missing, we imputed the dataset using the composition for the previous quarter. In total 8.1% or the observations in the dataset were imputed in this way. The statistics reported below refer to the imputed dataset.. The asset under management of the funds ranges from approximately 50 bln € in 2002 to more than 217 bln € in 2023. In total, 89% of the assets under management consists of European stocks (the rest is stocks from other geographical regions and investments in other asset classes).

![Refer to caption](descr_coverage_ESG.png)


Figure 1: Coverage of ESG data. In the left panel we report the number of assets with a ESG score for each quarter. In the right panel we report the volume of AUM.

![Refer to caption](descr_coverage_ts.png)


Figure 2: Coverage of price time series data. In the left panel we report the number of assets with a complete time series for each quarter. In the right panel we report the volume of AUM.

For each fund in the panel we associate the SFDR label (SFDR 6, SFDR 8, or SFDR 9). The SFDR labels have been downloaded from Refinitiv Eikon in mid 2023. Together the funds have exposures in more than 5400 European stocks, for which we downloaded from Refinitiv Eikon the daily price time series and the annual ESG score for the period 2002-2023. Figure [1](https://arxiv.org/html/2510.20434v1#S5.F1 "Figure 1 ‣ 5.1 Dataset description ‣ 5 Computation of SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") and [2](https://arxiv.org/html/2510.20434v1#S5.F2 "Figure 2 ‣ 5.1 Dataset description ‣ 5 Computation of SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") report the coverage of the dataset in terms of ESG score and time series. We see that in terms of asset under management (AUM) the coverage is high, although the ESG and equity price is missing for a large number of stocks, meaning that the dataset covers the companies most commonly included in the portfolios. The ESG coverage is limited for 2023, and thus in the rest of the analysis for missing data we used the ESG score of 2022. Figure [3](https://arxiv.org/html/2510.20434v1#S5.F3 "Figure 3 ‣ 5.1 Dataset description ‣ 5 Computation of SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") shows the number of funds in the dataset, together with the split by SFDR label. We see that the majority of the funds is labelled as SFDR 8, with only a minority of the funds being categorized as SFDR 9 “dark green funds”. The red part (labelled as “0”) represent the funds with no available SFDR status, that are a minority in the dataset. Figure [4](https://arxiv.org/html/2510.20434v1#S5.F4 "Figure 4 ‣ 5.1 Dataset description ‣ 5 Computation of SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") shows a wordcloud that summarizes the most used words in the name of the fund. We see that, together with more generic keywords such as “Europe”, “equity”, “European”, or “EUR”, the SFDR 9 funds use frequently in their naming words related to sustainability (e.g. “sustainable”, “impact”, “climate”, “ESG”). SFDR 8 funds on the contrary use less frequently such keywords, with the only exception of “ESG”, that appears with a certain frequency. Finally, SFDR 6 funds do not use frequently any word related to sustainable investing.

We underline that the SFDR legislation has been introduced only recently, and therefore the study that we conduct is retrospective, and assumes that the investment goals of funds currently labelled as SFDR 9 were characterized by a high level of sustainability also in the previous years.

![Refer to caption](descr_coverage_SFDR.png)


Figure 3: SFDR coverage in 2023. In the left panel we report the number of assets with the SFDR category, as assigned in 2023, for each quarter. In the right panel we report the volume of AUM.

![Refer to caption](wordcloud_SFDR.png)


Figure 4: Wordcloud of funds’ names for SFDR 6 (left), SFDR 8 (middle), and SFDR 9 (right) funds.

As a first analysis, we compute the weighted average ESG of the funds aggregated by SFDR class. This would help us to answer our first research question: Do the SFDR 9 “dark green funds” invest in funds with high ESG scores? Is there a relationship between ESG and SFDR?

In the left panel of Figure [5](https://arxiv.org/html/2510.20434v1#S5.F5 "Figure 5 ‣ 5.1 Dataset description ‣ 5 Computation of SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") we see the average ESG score of the funds by class over time, and we see a growing trend, especially before 2010, most likely due to the overall trend in the ESG scores provided by Refinitiv Eikon777The growing trend in Refinitiv’s ESG scores has been noticed in other works, and it has been associated not only to the growing sustainability of companies, but also to the methodology used by the data provider (see Benuzzi et al. [2023](https://arxiv.org/html/2510.20434v1#bib.bib6)). Comparing the SFDR classes we do not see any relevant difference between classes, with alternated ranking over time, and no higher average scores for “dark green funds”. The panel on the right shows the distribution of the average fund score for the third quarter of 2023 using box plots. Also in this case, we do not see relevant differences among the SFDR classes, apart from a tendency of SFDR 9 funds to have less outliers in the bottom part of the distribution. Overall, the results show very limited differences among the classes of funds in terms of ESG scores, suggesting a very low relation between the ESG scores assigned by Refinitiv and the composition of different classes of SFDR funds.

![Refer to caption](mean_ESG.png)


Figure 5: Average ESG score by SFDR funds’ classes and standard deviation.

### 5.2 SMIS scores and ESG scores

Using the methodology outlined in Section [4](https://arxiv.org/html/2510.20434v1#S4 "4 SFDR market-implied sustainability scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings"), we compute the SMIS scores, and we compare them to the ESG scores provided by Refinitiv Eikon. The SMIS score is computed quarterly, in line with the frequency of the portfolio composition available to us. Figure [6](https://arxiv.org/html/2510.20434v1#S5.F6 "Figure 6 ‣ 5.2 SMIS scores and ESG scores ‣ 5 Computation of SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") plots the SMIS score vs. the ESG score for three dates. The color denotes the statistical significance (with 90% confidence level) of the SMIS scores. The plots do not highlight a positive association between the two dimensions. Looking at the historical evolution, we see a concentration of the ESG scores in the upper ranges. We also highlight that the SMIS scores tend to show a higher level of dispersion for high levels of ESG, meaning that assets with high ESG can be either largely over- or under-invested in SFDR 9 funds compared to the rest of the market.

![Refer to caption](elephant_ears_history.png)


Figure 6: SMIS score vs ESG score for three time periods. Red dots represent stocks with SMIS score statistically significantly different from 0 with 90% confidence.

The ranking of the companies across two dimensions (ESG and SMIS scores) allows us to classify them in four groups ([7](https://arxiv.org/html/2510.20434v1#S5.F7 "Figure 7 ‣ 5.2 SMIS scores and ESG scores ‣ 5 Computation of SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings")). In the top-right corner we have companies characterized by high ESG score and high SMIS score. These companies are the ones that are recognized both by the market and by the ESG rating agency as the most sustainable (high ESG/SMIS). On the contrary, in the bottom-left corner, we have the companies that are under-invested in SFDR 9 funds, and have low ESG score: we thus have a double signal that classifies them as not sustainable (low ESG/SMIS). In the top-left corner we find companies with high ESG score that are under-invested by SFDR 9 funds. We refer synthetically to these group as high ESG/low SMIS, and the class imply that the actual presence in sustainable funds of such companies is more than the one that could be expected from their ESG score. Finally the companies in the bottom-right corner (low ESG/high SMIS) are not recognised by Refinitiv as being sustainable, but are over-represented in dark green funds (i.e. the market considers them sustainable, although the rating agency does not). This mismatch between the ESG scores could be attributable to differences in the goals and features considered by each scoring methodology. We emphasize that the disalignment may also be indicative of greenwashing practices by companies. Such practices may involve either selectively improving the metrics used in ESG evaluations to inflate their scores, or creating a perception of sustainability among investors that is not supported by actual sustainability indicators. We leave the application of our framework for detecting greenwashing to future work.

![Refer to caption](elephant_ears_quadrants.png)


Figure 7: SMIS score vs ESG score with quadrants highlighted.

Considering the sector split of the companies, it is possible to highlight interesting trends. Figure [8](https://arxiv.org/html/2510.20434v1#S5.F8 "Figure 8 ‣ 5.2 SMIS scores and ESG scores ‣ 5 Computation of SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") shows the ESG scores vs. the SMIS scores aggregated by GICS industry888The Global Industry Classification Standard (GICS) is an industry taxonomy developed in 1999 by MSCI and Standard &\& Poor’s (S&\&P) for use by the global financial community (color represent the GICS sector). We observe some relevant differences among industries: in particular, Food, beverages, and tobacco, as well as Energy and Telecommunication Services have on average high ESG score, while the SMIS score is low. These discrepancies between ESG scores and Market-implied scores can be explained by considering the role of exclusion strategies for sustainable investing fund, that often ban from the portfolios companies involved in controversial activities such as mining, oil extraction, or tobacco, thus leading to under- representation of companies operating in certain sectors such as Materials, Energy and Food, beverages, and tobacco.

![Refer to caption](sectors_elephant_ears1.png)


Figure 8: SMIS score vs ESG score by sector, computed at 30/09/2023.



|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ranking by SMIS score | | | | ranking by ESG score | | |
|  | name | ESG | implied | name | ESG | implied |
| 1 | Schneider Electric SE | 73.2 | 0.38 | Roche Holding AG | 95.2 | -0.09 |
| 2 | Kerry Group PLC | 70.8 | 0.22 | AstraZeneca PLC | 95.1 | 0.08 |
| 3 | Kingspan Group PLC | 82.3 | 0.21 | BNP Paribas SA | 95.1 | -0.19 |
| 4 | Siemens Gamesa | 65.3 | 0.20 | Shell PLC | 94.4 | -0.16 |
| 5 | Alstom SA | 87.8 | 0.19 | Allianz SE | 94.2 | -0.04 |
| 6 | Alfen NV | 46.8 | 0.18 | Abb Ltd | 94.0 | -0.03 |
| … | | | | … | | |
| n-5 | Carlsberg A/S | 77.0 | -0.20 | Fortnox AB | 8.5 | -0.005 |
| n-4 | Novartis AG | 86.5 | -0.21 | Civitas Social Hou. PLC | 7.6 | -0.002 |
| n-3 | Prosus NV | 58.1 | -0.22 | Enad Global 7 AB (publ) | 6.1 | -0.002 |
| n-2 | Enel SpA | 92.0 | -0.22 | St Galler Kantonalb. AG | 6.0 | -0.004 |
| n-1 | TotalEnergies SE | 89.6 | -0.25 | Warehouse REIT PLC | 5.4 | -0.002 |
| n | Rio Tinto PLC | 79.5 | -0.26 | Bank of Greece | 2.7 | -0.002 |

Table 1: Best and worst performers according to the SMIS score (left) and Refinitiv ESG score (right).

Table [1](https://arxiv.org/html/2510.20434v1#S5.T1 "Table 1 ‣ 5.2 SMIS scores and ESG scores ‣ 5 Computation of SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") reports the names of the companies rated best and worst in terms of SMIS score, and ESG score. We see that the top-performers according to the market based ranking are companies involved in the green transition, carrying specific innovations and technologies focused on sustainability. On the contrary, the worst performers are companies involved in controversial sectors such as mining, fossil fuels and alcoholic beverages, or companies that have been hit by controversies in the past. Looking at the ranking by ESG score, we see that the highest ranked companies are large multinational companies belonging to a diversified pool of sectors, while the worst performer are in large part small companies that likely suffer from insufficient sustainability reporting.

Overall, the results shows how the ESG scores and the SMIS scores carry substantially different information. In particular, it emerges how the market-implied scores allow to identify either companies with a prominent focus on sustainability (positive scores), or companies and sectors that are controversial (negative scores). The ESG scores provided by Refinitiv on the other hand are standardized by sector, and may help investors to pick companies with the best sustainability policies among the peer group of firms. This divergence between the two scoring systems leaves us the question on whether one of the two systems carries relevant information to improve the risk-adjusted performance of a portfolio. In the next section we conduct an analysis to answer such question.

## 6 Explaining the SMIS scores

In this section we set up an econometric analysis to identify the factors that drive the SMIS scores. In particular, we aim to investigate the relationship between an asset’s ESG score by Refinitiv and its market-implied sustainable score. Following Lambillon and Chesney ([2023](https://arxiv.org/html/2510.20434v1#bib.bib27)) we use a set of control variables including both “sustainability variables” and “corporate variables”. Finally, we include the dummy variables of the industry sector in which the company operates its business. Table [2](https://arxiv.org/html/2510.20434v1#S6.T2 "Table 2 ‣ 6 Explaining the SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") provides a description of all variables, while Table [3](https://arxiv.org/html/2510.20434v1#S6.T3 "Table 3 ‣ 6 Explaining the SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") shows the corresponding descriptive statistics. We sample the variable at quarterly frequency, and we lag the independent variables by one quarter to avoid endogeneity problems and to model delayed effects.

Table 2: Description and source of the dependent variable, main variables, and control variables.

|  |  |  |
| --- | --- | --- |
| Variables | Description | Source |
| Dependent variable | | |
| SMIS | Difference between the percentage of SFDR 9 funds with the ii-th asset in portfolio and the percentage of other funds (SFDR 6 and SFDR 8) with the ii-th asset in portfolio. Range: from -1 (worst) to 1 (best). | Computed |
| Main variable | | |
| ESG score | Refinitiv’s ESG score.Range: from 0 (worst) to 100 (best). | Refinitiv |
| Sustainable variables | | |
| Green revenues | Company’s green revenue as a proportion of total revenue. | Refinitiv |
| Standardized Total emission | Standardized GHGs total emissions (Scope 1 + Scope 2), computed as log(1 + Total emission/Total assets) | Computed |
| Target reduction | Has the company set targets or objectives to be achieved on emission reduction? (Y/N) | Refinitiv |
| Board diversity | Proportion of female gender included in the board (%) | Refinitiv |
| Human policy rights | Does the company have a policy for the exclusion of child, forced or compulsory labour, or to guarantee the freedom of association universally applied independent of local laws? (Y/N) | Refinitiv |
| Armaments | The company produces vehicles, planes, armaments, or any combat materials used by the military (Y/N) | Refinitiv |
| ESG controversial score | The company’s score in terms of environmental, social, and governance controversies and negative events reflected in global media. Range: from 0 (worst) to 100 (best). | Refinitiv |
| Corporate variables | | |
| Size | Total assets (in million €) | Refinitiv |
| P/B value | Price to book value (%) | Refinitiv |
| ROE | Return On Equity (%) | Refinitiv |
| P/E ratio | Price to Earnings value | Refinitiv |
| Dividend yield | Dividend per share as a percentage of the share price (%) | Refinitiv |
| Sector Dummies | Dummies based on 11 GICS (Global Industry Classification Standard) Sectors | Refinitiv |

From Figure [6](https://arxiv.org/html/2510.20434v1#S5.F6 "Figure 6 ‣ 5.2 SMIS scores and ESG scores ‣ 5 Computation of SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") we see that the SMIS is related in a non-linear way to ESG, suggesting that a simple OLS mean regression framework may not fully capture the relation between SMIS and other variables. We use the panel data quantile regression model by using the Method of Moments (MMQR) by Machado and Silva ([2019](https://arxiv.org/html/2510.20434v1#bib.bib29)). The methodology of the MMQR is based on a conditional location-scale model, similar to He ([1997](https://arxiv.org/html/2510.20434v1#bib.bib21)) and Zhao ([2000](https://arxiv.org/html/2510.20434v1#bib.bib39)), but the advantage is that it allows the use of methods that are only valid in the estimation of conditional means, such as differencing out individual effects in panel data models, while providing information on how the regressors affect the entire conditional distribution.

The MMQR approach can be adapted to the estimation of cross-sectional models with endogenous variable (Machado and Silva [2019](https://arxiv.org/html/2510.20434v1#bib.bib29)). Moreover, it allows individual fixed effects to have heterogeneous effects on the entire conditional distribution of the outcome, rather than constraining their effect to be a location shift only, as in Canay ([2011](https://arxiv.org/html/2510.20434v1#bib.bib10)), Koenker ([2004](https://arxiv.org/html/2510.20434v1#bib.bib25)), and Lamarche ([2010](https://arxiv.org/html/2510.20434v1#bib.bib26)). The conditional quantile of the dependent variable (SMIS) is computed as a function of variables that include the ESG score of the company, a set of sustainability-related variables, corporate variables, and sector dummies.

|  |  |  |
| --- | --- | --- |
|  | QS​M​I​St|X​(τ)=β0,τ+β1,τ​E​S​Gt−1+β2,τ​s​u​s​t​a​i​n​a​b​i​l​i​t​yt−1+β3,τ​c​o​r​p​o​r​a​t​et−1+β4,τ​s​e​c​t​o​r.Q\_{SMIS\_{t}|X}(\tau)=\beta\_{0,\tau}+\beta\_{1,\tau}ESG\_{t-1}+\beta\_{2,\tau}sustainability\_{t-1}+\beta\_{3,\tau}corporate\_{t-1}+\beta\_{4,\tau}sector. |  |

For the complete list of regressors we refer to Table [2](https://arxiv.org/html/2510.20434v1#S6.T2 "Table 2 ‣ 6 Explaining the SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings"). The sustainability-related variables and the control variables have been selected based on their relevance as key factors influencing the sustainability profile of a company, ensuring a comprehensive and robust analysis. The variables are consistent with the analysis of Lambillon and Chesney ([2023](https://arxiv.org/html/2510.20434v1#bib.bib27)). In addition, given the strong emphasis posed on the green transition by the European Commission (Fetting [2020](https://arxiv.org/html/2510.20434v1#bib.bib16)), we considered the variable Green Revenues, a metric that reflects companies’ exposure to the transition to green economy. We tested for potential collinearity by computing the VIF (Variance Inflation Factor), finding that the values are smaller than 2 for all the regressions performed, suggesting the lack of relevant collinearity in the regressors.

Table 3: Descriptive statistics.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Variables | Mean | Std. Dev. | Min | Max |
| Dependent variable | | | | |
| SMIS (%) | -4.821811 | 8.27222 | -41.34733 | 42.35852 |
| Main variables | | | | |
| ESG score | 68.86167 | 15.91454 | 7.92 | 95.72 |
| E score | 71.00005 | 20.33406 | 0 | 98.91 |
| S score | 71.6821 | 19.01234 | 4.39 | 98.47 |
| G score | 63.21164 | 20.46036 | 2.78 | 98.56 |
| Sustainability variables | | | | |
| Green revenues (%) | 7.62282 | 19.58956 | 0 | 100 |
| Stand. Total emission | 2.882759 | 2.013805 | 0 | 8.001779 |
| Target reduction | 0.8221383 | 0.3824088 | 0 | 1 |
| Board diversity (%) | 28.69469 | 13.08666 | 0 | 72.73 |
| Human policy rights | 0.7523841 | 0.4316418 | 0 | 1 |
| Armaments | 0.0577888 | 0.2333512 | 0 | 1 |
| ESG controversial score | 78.25331 | 31.71355 | 0.3 | 100 |
| Corporate variables | | | | |
| Size (in million euros) | 118.0307 | 310.0916 | 0 | 2914.278 |
| PB ratio | 2.662639 | 3.863162 | -109.04 | 54.09 |
| ROE (%) | 15.24715 | 37.4341 | -252.84 | 1976.85 |
| PE ratio | 22.65364 | 75.89612 | 0 | 6301.5 |
| Dividend yield (%) | 3.708713 | 23.07964 | 0 | 1283.07 |

### 6.1 Quantile regression results

Table [4](https://arxiv.org/html/2510.20434v1#S6.T4 "Table 4 ‣ 6.1.1 The drivers of SMIS ‣ 6.1 Quantile regression results ‣ 6 Explaining the SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") presents the main quantile regression results, highlighting how the ESG score behaves differently across quantiles. Specifically, for lower quantiles (ranging from τ=0.05\tau=0.05 to τ=0.5\tau=0.5), the ESG score coefficient is consistently negative and statistically significant at the 1%1\% level. In contrast, from τ=0.75\tau=0.75 to τ=0.95\tau=0.95, the coefficient is positive.
This suggests that SMIS sensitivity to ESG depends on the value of the score. An interpretation could be that some companies are excluded by SFDR 9 funds (i.e. they have a low SMIS) for factors that are not measured by the ESG score. In such cases, a high ESG score can even be detrimental, as it could be perceived as a sign of greenwashing. In contrast, for companies that are included in the SFDR 9 funds (i.e. the ones with high SMIS), the factors measured by the ESG score are relevant for the fund managers, thus there is a positive coefficient. The results therefore confirm the presence of a misalignment between SMIS and ESG scores.

Focusing on the sustainability variables, we see that the coefficient for Green Revenues is consistently positive and significant at the 1%1\% level across all models, indicating that SFDR 9 funds positively value green revenues as a key factor for asset inclusion, regardless of whether the company has a low or high SMIS score. Then, we find that the coefficient of the Standardized total emissions is negative and significant across all models (i.e. higher emissions are associated to lower SMIS). The result is in line with expectations, and confirms the results in Lambillon and Chesney ([2023](https://arxiv.org/html/2510.20434v1#bib.bib27)) that find similar results for their greenness score. We then document that companies with a target emissions reduction policy are associated with a higher SMIS, in line with the results of Lambillon and Chesney ([2023](https://arxiv.org/html/2510.20434v1#bib.bib27)). Investors might see a target emissions reduction as a level of commitment of companies to lower GHG emissions in the future, thus, assets with a target reduction policy may be over-represented in SFDR 9 funds with respect to other funds. Furthermore, the coefficient for the Armaments variable is negative and increases in absolute value as τ\tau increases, remaining statistically significant in all models. This suggests that companies involved in weapons production or military services are increasingly less likely to be included in SFDR 9 funds as we move to higher quantiles, compared to other funds. The coefficients of the board diversity variable are also positive and significant, showing that companies in SFDR 9 funds have more diverse boards.
Interestingly, we find a negative coefficient for the Human Rights Policy variable, indicating that companies with established human rights policies have a lower likelihood of being included in SFDR 9 funds. This counterintuitive result may be related to the perceived weakness of such policies in contrasting human right violations (e.g. they may be considered too broad and generic), or by the fact that companies with a human right policies may be more likely to be involved in activity with high risk of human right violations. The coefficient for the ESG Controversies score is always positive and statistically significant at the 1%1\% level, suggesting that companies with fewer ESG controversies are more likely to be included in SFDR 9 funds, confirming the relevance of ESG controversies for portfolio managers highlighted by Dorfleitner et al. ([2020](https://arxiv.org/html/2510.20434v1#bib.bib12)).

To conclude the comment on sustainability variables, we observe a positive relationship between SMIS and Board Diversity.

Regarding corporate variables, we find that company Size, measured by total assets, has a statistically significantly negative coefficient for τ\tau between 0.050.05 and 0.750.75. This suggests that company size has a detrimental effect on SMIS (with the exception of the companies with the highest SMIS scores – those most heavily represented in SFDR 9 funds). This finding suggests that SFDR 9 funds, in general, tend to overweight smaller companies and underweight compared to the rest of the funds. Finally, the variables PB ratio (price to book) and PE ratio (Price to Earning) show significant and positive effect on the SMIS, while ROE (Return on Equity) has a negative coefficient, significant for τ\tau up to 0.5.

#### 6.1.1 The drivers of SMIS

Table 4: Regression baseline results – determinants of SMIS scores.

Dependent variable: SMIS
(1)
(2)
(3)
(4)
(5)
(6)
(7)


qtile\_0.5
qtile\_1
qtile\_2.5
qtile\_5
qtile\_7.5
qtile\_9
qtile\_9.5



Lag\_ESG\_score
-0.101\*\*\*
-0.084\*\*\*
-0.059\*\*\*
-0.031\*\*\*
0.001
0.036\*\*\*
0.059\*\*\*


(0.007)
(0.006)
(0.005)
(0.005)
(0.006)
(0.009)
(0.010)



Lag\_green\_revenues
0.029\*\*\*
0.042\*\*\*
0.061\*\*\*
0.083\*\*\*
0.107\*\*\*
0.133\*\*\*
0.151\*\*\*


(0.006)
(0.005)
(0.004)
(0.004)
(0.005)
(0.007)
(0.009)



Lag\_std\_total\_emission
-0.372\*\*\*
-0.427\*\*\*
-0.512\*\*\*
-0.608\*\*\*
-0.714\*\*\*
-0.830\*\*\*
-0.909\*\*\*


(0.085)
(0.073)
(0.061)
(0.060)
(0.074)
(0.100)
(0.121)



Lag\_target\_reduction
0.727\*\*\*
0.728\*\*\*
0.730\*\*\*
0.732\*\*\*
0.734\*\*\*
0.737\*\*
0.739\*\*


(0.248)
(0.215)
(0.179)
(0.175)
(0.216)
(0.293)
(0.353)



Lag\_board\_diversity
0.081\*\*\*
0.075\*\*\*
0.066\*\*\*
0.055\*\*\*
0.044\*\*\*
0.031\*\*\*
0.022\*\*


(0.008)
(0.007)
(0.006)
(0.005)
(0.007)
(0.009)
(0.011)



Lag\_hum\_pol\_rights
0.054
-0.113
-0.373\*\*
-0.668\*\*\*
-0.992\*\*\*
-1.348\*\*\*
-1.590\*\*\*


(0.248)
(0.214)
(0.179)
(0.175)
(0.216)
(0.292)
(0.353)



Lag\_armaments
-0.554
-0.755\*\*
-1.067\*\*\*
-1.420\*\*\*
-1.809\*\*\*
-2.235\*\*\*
-2.525\*\*\*


(0.375)
(0.325)
(0.271)
(0.264)
(0.326)
(0.442)
(0.534)



Lag\_ESG\_controversies
0.041\*\*\*
0.040\*\*\*
0.039\*\*\*
0.037\*\*\*
0.036\*\*\*
0.034\*\*\*
0.033\*\*\*


(0.003)
(0.003)
(0.002)
(0.002)
(0.003)
(0.004)
(0.005)



Lag\_size
-0.005\*\*\*
-0.004\*\*\*
-0.003\*\*\*
-0.002\*\*\*
-0.001\*\*\*
0.000
0.001


(0.000)
(0.000)
(0.000)
(0.000)
(0.000)
(0.001)
(0.001)



Lag\_PB\_ratio
0.039\*
0.049\*\*\*
0.066\*\*\*
0.084\*\*\*
0.104\*\*\*
0.127\*\*\*
0.142\*\*\*


(0.022)
(0.019)
(0.016)
(0.015)
(0.019)
(0.026)
(0.031)



Lag\_ROE
-0.011\*\*\*
-0.010\*\*\*
-0.008\*\*\*
-0.006\*
-0.003
-0.000
0.002


(0.004)
(0.004)
(0.003)
(0.003)
(0.004)
(0.005)
(0.006)



Lag\_PE\_ratio
0.001
0.002
0.002\*\*
0.003\*\*
0.003\*\*
0.003\*\*
0.004\*


(0.001)
(0.001)
(0.001)
(0.001)
(0.001)
(0.002)
(0.002)



Lag\_div\_yield
-0.004
-0.004
-0.004
-0.004\*
-0.005
-0.005
-0.005


(0.004)
(0.003)
(0.003)
(0.003)
(0.003)
(0.004)
(0.005)



Observations
14,579
14,579
14,579
14,579
14,579
14,579
14,579


Note: Standard errors are reported in parentheses. \* p<0.1p<0.1, \*\* p<0.05p<0.05, \*\*\* p<0.01p<0.01.

#### 6.1.2 Does the SMIS explain the ESG score?

We test here the opposite relation compared to Section [6.1.1](https://arxiv.org/html/2510.20434v1#S6.SS1.SSS1 "6.1.1 The drivers of SMIS ‣ 6.1 Quantile regression results ‣ 6 Explaining the SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") – that is, does the SMIS allows to explain the ESG score? Table [5](https://arxiv.org/html/2510.20434v1#S6.T5 "Table 5 ‣ 6.1.2 Does the SMIS explain the ESG score? ‣ 6.1 Quantile regression results ‣ 6 Explaining the SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") presents the results of the quantile regressions where the ESG score is the dependent variable and the SMIS score is the main independent variable. The analysis shows that the coefficient for the SMIS score is consistently negative and statistically significant across all models.

Concerning the sustainability variables, we see that Green revenues have a positive and significant effect only for quantiles higher than 0.75, while the relation is not significant for intermediate quantiles, and is negative for very low quantiles. This suggests that the green revenues metric is not tightly related to the ESG scores. Surprisingly, standardized total emissions are not significant for high quantiles, and they have a negative and statistically significant coefficient for τ≤0.5\tau\leq 0.5. This means that – at least for low ESG scores – higher emissions are associated to higher scores. This may be explainable by the fact that ESG scores do not use GHG emissions alone, but they elaborate the data, focusing on instance on the comparison with peers, or on the implementation of specific policies to reduce emissions. The coefficients for Target reduction, Board diversity, and Human policy rights instead are in line with expectation, showing higher ESG scores across all quantiles for higher values of these variables, suggesting that these measures are integral to the evaluation of a company’s ESG score. The coefficient for the Armaments variable instead is negative for τ≤0.5\tau\leq 0.5, suggesting that ESG scores do not account for armaments using an approach in line with this variable. Finally, we notice that the coefficient for the controversies score is negative and significant, in accordance with the fact that ESG scores do not directly include the effect of controversies.

For the corporate variables, we see that the coefficient for the Size variable is always positive and statistically significant at the 1%1\% level. As discussed in the existing literature Lambillon and Chesney ([2023](https://arxiv.org/html/2510.20434v1#bib.bib27)), larger companies are more likely to disclose sustainability information, often in larger quantities. This likely explains why a larger Size is associated with a higher ESG score. ESG score is also higher for companies with a smaller P to B value, and a large dividend yield.

Overall, the econometric analysis shows that SMIS and ESG scores from Refinitiv are related in non-linear ways, and that different factors contribute to explain them.

Table 5: Quantile Regression Results: Determinants of ESG Score

Dependent variable: ESG score
(1)
(2)
(3)
(4)
(5)
(6)
(7)


qtile\_05
qtile\_1
qtile\_25
qtile\_5
qtile\_75
qtile\_9
qtile\_95

Lag\_SMIS
-0.053\*\*
-0.056\*\*\*
-0.061\*\*\*
-0.066\*\*\*
-0.070\*\*\*
-0.073\*\*\*
-0.075\*\*\*


(0.025)
(0.021)
(0.015)
(0.012)
(0.011)
(0.013)
(0.014)

Lag\_green\_revenues
-0.021\*
-0.015
-0.004
0.007
0.016\*\*\*
0.023\*\*\*
0.026\*\*\*


(0.011)
(0.009)
(0.007)
(0.005)
(0.005)
(0.006)
(0.007)

Lag\_std\_total\_emission
0.422\*\*
0.361\*\*
0.260\*\*
0.161\*
0.077
0.013
-0.020


(0.188)
(0.160)
(0.118)
(0.090)
(0.087)
(0.100)
(0.110)

Lag\_target\_reduction
15.921\*\*\*
14.719\*\*\*
12.726\*\*\*
10.760\*\*\*
9.098\*\*\*
7.824\*\*\*
7.163\*\*\*


(0.634)
(0.537)
(0.396)
(0.302)
(0.293)
(0.335)
(0.369)

Lag\_board\_diversity
0.343\*\*\*
0.305\*\*\*
0.242\*\*\*
0.180\*\*\*
0.127\*\*\*
0.087\*\*\*
0.066\*\*\*


(0.017)
(0.015)
(0.011)
(0.008)
(0.008)
(0.009)
(0.010)

Lag\_hum\_pol\_rights
15.192\*\*\*
14.548\*\*\*
13.481\*\*\*
12.429\*\*\*
11.539\*\*\*
10.857\*\*\*
10.503\*\*\*


(0.569)
(0.483)
(0.356)
(0.272)
(0.263)
(0.301)
(0.333)

Lag\_armaments
-4.020\*\*\*
-3.316\*\*\*
-2.150\*\*\*
-0.999\*\*
-0.027
0.719
1.106\*


(1.025)
(0.870)
(0.641)
(0.489)
(0.474)
(0.543)
(0.600)

Lag\_ESG\_controversies
-0.079\*\*\*
-0.075\*\*\*
-0.068\*\*\*
-0.060\*\*\*
-0.054\*\*\*
-0.050\*\*\*
-0.047\*\*\*


(0.006)
(0.005)
(0.004)
(0.003)
(0.003)
(0.003)
(0.004)

Lag\_size
0.008\*\*\*
0.008\*\*\*
0.008\*\*\*
0.009\*\*\*
0.009\*\*\*
0.009\*\*\*
0.009\*\*\*


(0.001)
(0.001)
(0.001)
(0.000)
(0.000)
(0.000)
(0.000)

Lag\_PB\_ratio
-0.108\*\*
-0.111\*\*
-0.116\*\*\*
-0.122\*\*\*
-0.126\*\*\*
-0.130\*\*\*
-0.132\*\*\*


(0.054)
(0.046)
(0.034)
(0.026)
(0.025)
(0.029)
(0.032)

Lag\_ROE
-0.004
-0.003
-0.002
-0.001
-0.000
0.000
0.001


(0.006)
(0.005)
(0.004)
(0.003)
(0.003)
(0.003)
(0.003)

Lag\_PE\_ratio
0.001
0.001
-0.000
-0.001
-0.002\*\*\*
-0.003\*\*\*
-0.003\*\*\*


(0.002)
(0.001)
(0.001)
(0.001)
(0.001)
(0.001)
(0.001)

Lag\_div\_yield
0.012\*\*\*
0.011\*\*\*
0.009\*\*\*
0.007\*\*\*
0.006\*\*\*
0.005\*\*
0.004\*


(0.004)
(0.003)
(0.002)
(0.002)
(0.002)
(0.002)
(0.002)


Note: Standard errors are reported in parentheses. \* p<0.1p<0.1, \*\* p<0.05p<0.05, \*\*\* p<0.01p<0.01.

## 7 Portfolio tilting

In this Section we investigate if we can exploit the information embedded in our SMIS scores to improve the portfolios’ financial and sustainability performance. A portfolio “tilt” is an investment strategy that over-weighs a particular investment style. An example would be tilting to small-cap stocks or value stocks that have historically delivered higher returns than the stock market. Over-weighing to a style is always done with the expectation of achieving a higher return or higher risk-adjusted return than the market. In our case we also expect to increase the sustainability of the initial portfolio. In the first part of our analysis, we tilt a benchmark index by a fixed amount, over-weighting or under-weighting specific securities according their sustainability scores. In a second step, we consider more sophisticated allocation strategies in which, instead of fixed weight variation, the optimal portfolio weights are defined as the solutions of constrained optimization problems.
Both the fixed tilting and optimal tilting allocations rely on preselection strategies that identify assets to over/under-weight compared to a benchmark based on the ranking of the companies according to the SMIS score, ESG score, and the four groups described in Figure [7](https://arxiv.org/html/2510.20434v1#S5.F7 "Figure 7 ‣ 5.2 SMIS scores and ESG scores ‣ 5 Computation of SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings").
The strategies that we consider are synthetically described below

1. 𝒮\mathcal{S}1

   Top ESG - over-weight top kk companies with best ESG, under-weight kk worst ESG.
2. 𝒮\mathcal{S}2

   Top SMIS - over-weight top kk companies with best implied SMIS scores, under-weight the kk worst implied SMIS score.
3. 𝒮\mathcal{S}3

   Corners TT (Top-Top) - over-weight top kk highest ESG and SMIS companies, under-weight kk lowest ESG and SMIS.
4. 𝒮\mathcal{S}4

   Corners TB (Top ESG-Bottom SMIS) - over-weight top kk highest ESG and lowest SMIS, under-weight kk lowest ESG and highest SMIS.
5. 𝒮\mathcal{S}5

   Corners BT (Bottom ESG-Top SMIS) - over-weight top kk highest SMIS and lowest ESG, under-weight kk lowest SMIS and highest ESG.

To grasp an intuitive understanding of the preselection approaches, the different strategies are illustrated graphically in Figure [9](https://arxiv.org/html/2510.20434v1#S7.F9 "Figure 9 ‣ 7 Portfolio tilting ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings"). The interpretation of the first two strategies – Top ESG and Top SMIS – is straightforward: the assets to over/under weight are selected based on each of the two scoring systems, respectively. The other strategies aim to assess the interaction effect between the ESG and SMIS scores. In particular, strategy 𝒮\mathcal{S}3 (Top-Top) is an approach that considers and trusts both the market (SMIS scores) and the data provider (ESG scores), and over-weights assets rated positively according to both scores, under-weighting the ones with negative scores according to both criteria. Strategies 𝒮\mathcal{S}4 and 𝒮\mathcal{S}5 focus on asset for which the ESG and SMIS scores diverge, that is, on the groups identified as the Top ESG-Bottom SMIS and the Bottom ESG-Top SMIS. In particular strategy 𝒮\mathcal{S}4 over-weights the assets with a high ESG score and low SMIS score, and under-weights with a low ESG score and high SMIS score.

In practice, to select the assets for strategies 𝒮\mathcal{S}1 and 𝒮\mathcal{S}2 we use the quantiles of the distribution of assets’ ESG and SMIS scores. For strategies 𝒮\mathcal{S}3, 𝒮\mathcal{S}4, and 𝒮\mathcal{S}5 we use the following approach to identify the groups of assets to under/over-weight using the joint bivariate distribution of the two scores:

* •

  define a grid of probability values π1,…,πm\pi\_{1},\dots,\pi\_{m},
* •

  compute the corresponding univariate quantiles QE​S​G,1,…,QE​S​G,mQ\_{ESG,1},\dots,Q\_{ESG,m} and QS​M​I​S,1,…,QS​M​I​S,mQ\_{SMIS,1},\dots,Q\_{SMIS,m} for both ESG and SMIS scores, respectively,
* •

  then, to identify the borders of the lower-left quadrant that includes kk companies we select the smallest ii such that P​r​(E​S​G<QE​S​G,i∧S​M​I​S<QS​M​I​S,i)=k/nPr(ESG<Q\_{ESG,i}\land SMIS<Q\_{SMIS,i})=k/n, where nn is the number of companies. To identify other quadrants we simply invert the sign of the inequalities appropriately.

![Refer to caption](corners_plot.png)


Figure 9: Tilting strategies: the portfolio adds to the benchmark a long position in the stocks in the green area, and a short position in the red area according to the described procedure. Both the red and the green areas include a number k=200k=200 assets.

### 7.1 Portfolio tilting strategies

#### 7.1.1 Portfolio tilting

For the tilting strategies, we start from a benchmark (the STOXX Europe 600), and we add long and short positions based on the SMIS scores and ESG scores based on the preselection strategies defined above. We rebalance the portfolio quarterly according to the latest available information.

More in details, each quarter we set up a baseline portfolio that replicates the benchmark, excluding the stocks with incomplete information for the quarter. Then on top of it we invest in a long-short portfolio with long positions equal to 10% of the initial invested amount, and short of the same size. The long and short positions are equally divided between the kk best and kk worse companies in the preselection strategies, respectively (in this work we consider k=100k=100).

#### 7.1.2 Optimized portfolio tilting

The analysis of tilting portfolios allows us to assess the aggregate contribution to portfolio performance of ESG and SMIS scores. In this section we aim to further analyse the effect on performance, considering active management strategies that incorporate sustainability scores, but where the managers perform stock picking in order to seize opportunities or avoid unnecessary risks.

Funds managers’ stock picking strategies are often based on subjective decisions and expert’s judgement. To make the analysis reproducible and objective, we thus consider optimal allocation strategies in which the portfolio weights are obtained by solving constrained optimization problems. In particular, we aim to minimize some risk measure or maximise reward-risk ratios while under/over-weighting certain groups of assets compared to a benchmark (e.g. over-weighting the 100 assets with the highest ESG score and under-weighting the ones with the lowest).

We consider four well know optimization strategies (mean-CVaR, mean-EVaR, mean-variance, and maximum Sharpe ratio), and we impose constraints on the weights by opportunely add lower and upper bounds to the weights. For the first three strategies (the ones that minimize risk) we constrain the expected return to be greater or equal than the one of the benchmark. The four optimal strategies are defined in Appendix B.
The models have been implemented in Matlab 2023b using Mosek 10.1 for the linear and quadratic constrained optimizations. The confidence level for the mean-CVaR and mean-EVaR portfolios has been set to α=95%\alpha=95\%.

Since the analysis is focused on the over-weighting and under-weighting of individual positions in a benchmark, differently from the portfolio in Section [7.1.1](https://arxiv.org/html/2510.20434v1#S7.SS1.SSS1 "7.1.1 Portfolio tilting ‣ 7.1 Portfolio tilting strategies ‣ 7 Portfolio tilting ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings"), we limit our analysis to the constituents of the benchmark in a given quarter. Thus, from the approximately 600 assets included in the benchmark, the set 𝒜under\mathcal{A}\_{\text{under}} includes the best 100 assets in the benchmark for a specific criterion, and 𝒜under\mathcal{A}\_{\text{under}} the worst ones.
The groups of assets to under/over-weight are the same used in Section [7.1.1](https://arxiv.org/html/2510.20434v1#S7.SS1.SSS1 "7.1.1 Portfolio tilting ‣ 7.1 Portfolio tilting strategies ‣ 7 Portfolio tilting ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") for the tilting portfolios (Top ESG, Top SMIS, Corners TT, Corners TB, Corners BT). We also use the same benchmark portfolio (i.e. the STOXX Europe 600 index).

### 7.2 Empirical set-up

We run the analysis recalibrating the portfolios every quarter, using the most recent information at the beginning of the investment period. That is, we use the SMIS score computed at the beginning of the period, and the last published ESG score by Refinitiv. We limit the out-of-sample analysis to the period April 1st, 2010 to December 31th, 2023 discarding earlier data in order to have more stable ESG scores and a sufficient number of SFDR 9 funds.

For the tilting portfolios in Section [7.1.1](https://arxiv.org/html/2510.20434v1#S7.SS1.SSS1 "7.1.1 Portfolio tilting ‣ 7.1 Portfolio tilting strategies ‣ 7 Portfolio tilting ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") we consider k=100k=100 (i.e. selecting the best and worst 100 assets for each of the criteria considered), and for each quarter we include in the ranking all the European companies in the sample with complete time series, ESG score, and implied SMIS score.

For the optimized portfolios we consider a calibration window of 1 year (250 daily observations), and an investment period of 3 months. That is, we rebalance the portfolio quarterly using the previous 250 observations for the estimation of the optimal weights. In each optimization we include only the asset with a complete time series for the calibration period and for the investment period. Since we aim to study a realistic strategy, we limit our portfolios to the assets with complete time series, ESG scores, and implied SMIS score that are included in the benchmark at the beginning of the investment period (approximately 500 companies).

As a benchmark we use a synthetic version of the index that includes the assets with complete time series in the relevant period (holding period for tilting portfolio, calibration + holding period for the optimized portfolios).

In order to assess whether the performance of the funds is genuinely related to selection of assets based on sustainability criteria, we run a statistical validation analysis: for any of the portfolio allocation defined in Sections [7.1.1](https://arxiv.org/html/2510.20434v1#S7.SS1.SSS1 "7.1.1 Portfolio tilting ‣ 7.1 Portfolio tilting strategies ‣ 7 Portfolio tilting ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") and [7.1.2](https://arxiv.org/html/2510.20434v1#S7.SS1.SSS2 "7.1.2 Optimized portfolio tilting ‣ 7.1 Portfolio tilting strategies ‣ 7 Portfolio tilting ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings"), we construct 200 alternative portfolios in which we select randomly the assets to over/under-weight (rather than following the strategies described in Section [7.1.1](https://arxiv.org/html/2510.20434v1#S7.SS1.SSS1 "7.1.1 Portfolio tilting ‣ 7.1 Portfolio tilting strategies ‣ 7 Portfolio tilting ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings")). In this way, for each portfolio allocation and for each risk/reward measure we compute a confidence interval that is based on the corresponding optimization or tilting strategy. Using the empirical distribution of the random portfolios we test if the obtained risk and reward out-of-sample measures are outside the 90% confidence interval for random selection.

### 7.3 Analysis of the results

Table [6](https://arxiv.org/html/2510.20434v1#S7.T6 "Table 6 ‣ 7.3 Analysis of the results ‣ 7 Portfolio tilting ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") reports the performance of the tilting portfolios defined in Section [7.1.1](https://arxiv.org/html/2510.20434v1#S7.SS1.SSS1 "7.1.1 Portfolio tilting ‣ 7.1 Portfolio tilting strategies ‣ 7 Portfolio tilting ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings"). The table reports the annualized return, VaR95%, CVaR95%, standard deviation (for brevity we use the acronym std), Sharpe ratio, max drawdown (maxDD), average turnover, average number of assets, maximum invidual weight, and Herfindahl-Hirschman Index (HHI). The values of risk and reward measures outside the 90%90\% confidence interval (CI) computed using a random strategy in which the kk assets to over/under-weight are chosen randomly each quarter. For readability, the values outside the confidence interval are colored green if they are an improvement, and red if they are a worsening.

We see that, among the ones provided, the strategies with the best out-of-sample performance are the “Top SMIS”, and the “Bottom ESG-Top SMIS”, that have lower risk than the benchmark, higher average return, and higher Sharpe ratio. On the contrary, “ESG”, “Top-Top”, and “Top ESG-Bottom SMIS” underperform the benchmark in terms of risk and risk-adjusted performance. The results are statistically significant, as the measures are outside the confidence interval computed using random strategies. Overall, the Table suggests that companies with a high implied SMIS score have in aggregate positive performance, while companies with a low score are characterized by sub-par risk-adjusted performance. High ESG companies on the contrary seem to be associated to worse performance than low ESG ones. The very good performance of the “Bottom ESG-Top SMIS” strategies suggest that the best financial opportunities are associated to the assets that are included in the dark green funds, but don’t have a high ESG score. The table reports also portfolio statistics: the turnovers are overall comparable, and is lowest for the “Top ESG” strategy likely due to the greater stability of the ESG scores (that change annually) compared to the SMIS scores (that are computed quarterly). The number of assets, maximum exposure to a single asset and Herfindahl-Hirschman indices are comparable.

Table [7](https://arxiv.org/html/2510.20434v1#S7.T7 "Table 7 ‣ 7.3 Analysis of the results ‣ 7 Portfolio tilting ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") reports the performance of the optimal funds, defined in Section [7.1.2](https://arxiv.org/html/2510.20434v1#S7.SS1.SSS2 "7.1.2 Optimized portfolio tilting ‣ 7.1 Portfolio tilting strategies ‣ 7 Portfolio tilting ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings"), using four alternative asset allocation frameworks (Panel A: mean-CVaR, Panel B: Mean-EVaR, Panel C: Mean-Variance, Panel D: maximum Sharpe ratio), and the five preselection strategies discussed above. We observe that the results are consistent across the optimizations, with “Top SMIS” and “Bottom ESG-Top SMIS” portfolios being characterized by good risk-adjusted performance. The “Top ESG”, “Top-Top”, and “Top ESG-Bottom SMIS” strategies instead, despite beating in most cases the benchmark, are in most cases statistically significant worse that the random strategies. We stress that the confidence interval is based on optimal portfolio with random selection of the assets to over/under-weight, and not on the benchmark (that is in most cases significantly more risky than the optimal portfolios).999The benchmark is slightly different from the one used in Table [6](https://arxiv.org/html/2510.20434v1#S7.T6 "Table 6 ‣ 7.3 Analysis of the results ‣ 7 Portfolio tilting ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") since for the optimal portfolios we need to include assets with complete time series for both the in-sample and out-of-sample periods, while for the tilting strategies we only need complete time series for the investment period. Concerning portfolio statistics, we see that the “Top SMIS” and “Bottom ESG-Top SMIS” portfolios are slightly more concentrated compared to the other strategies (higher HHI and higher maximum individual weight), and have the highest turnover (between 30% and 40% of quarterly turnover). The values are still well under control, considering the high number of assets in the portfolio and the low rebalancing frequency. Overall, the results suggests that the selection process of sustainable companies carried out by “dark green” funds has positive implications on the performance, possibly due to identification of valuable investment opportunities, a better control of risks, or a reduced exposure to assets with ESG controversies. On the contrary, the criteria used to attribute ESG scores does not seem to be associated to higher performance.

We point out that the good performance of the “SMIS” strategy does not necessarily imply superior performance of the dark green funds available on the market, as the performance of such funds is affected by a series of other factors such as the sectorial and geographical diversification, the presence of exclusionary strategies for controversial sectors, the subjective choices of the fund managers in terms of stock picking and market timing, or the level of management fees. The market-implied SMIS score, by cumulating allocations of multiple funds and comparing them to the ones of non-sustainable funds, allows to extract a signal that synthesize the aggregate perception of the market on sustainability, and the corresponding financial performance.

| Tilting portfolios | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tilting portfolios | mean | VaR | EVaR | CVaR | std | Sharpe | maxDD | turnover | # assets | max w\_i | HHI |
| Benchmark | 2.55 % | 1.27 % | 1.02 % | 2.1 % | 13.16 % | 0.19 | 38.09 % | 3.94 % | 530.57 | 3.18 % | 0.01 |
| Top ESG | 2.38 % | 1.45 %\* | 1.17 %\* | 2.41 %\* | 15.12 %\* | 0.16\* | 43.21 %\* | 10.48 % | 530.38 | 3.48 % | 0.01 |
| Top SMIS | 3.28 %\* | 1.24 %\* | 0.97 %\* | 1.98 %\* | 12.48 %\* | 0.26\* | 31.52 %\* | 17.87 % | 528.81 | 2.98 % | 0.01 |
| Top-Top | 2.42 % | 1.35 %\* | 1.08 %\* | 2.22 %\* | 13.93 %\* | 0.17 | 38.31 % | 17.39 % | 529.85 | 3.19 % | 0.01 |
| Top ESG-Bottom SMIS | 2.25 % | 1.46 %\* | 1.16 %\* | 2.4 %\* | 15.06 %\* | 0.15\* | 45.6 %\* | 16.92 % | 530.11 | 3.47 % | 0.01 |
| Bottom ESG-Top SMIS | 2.86 % | 1.16 %\* | 0.9 %\* | 1.83 %\* | 11.53 %\* | 0.25\* | 29.9 %\* | 16.81 % | 528.77 | 2.89 % | 0.01 |

Table 6: Out-of-sample portfolio performance of the tilting portfolios. The values with “\*” denote the measures that are outside the 90% confidence interval for random selection of assets to under/over-weight. The values outside the confidence interval are green if they are an improvement (e.g. lower risk or higher return), and red if they are a worsening. Benchmark is the baseline portfolio without tilting.

| Panel A - optimal tilting - CVaR portfolios | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| optimal tilting - CVaR | mean | VaR | EVaR | CVaR | std | Sharpe | maxDD | turnover | # assets | max w\_i | HHI |
| Benchmark | 2.64 % | 1.29 %\* | 1.02 %\* | 2.11 %\* | 13.21 %\* | 0.2 | 37.68 %\* | 3.64 % | 512.58 | 3.21 % | 0.01 |
| Top ESG | 2.78 % | 1.28 %\* | 1.01 %\* | 2.07 %\* | 12.97 %\* | 0.21 | 35.13 % | 6.94 % | 439.21 | 4.1 % | 0.01 |
| Top SMIS | 3.71 % | 1.05 %\* | 0.83 %\* | 1.7 %\* | 10.69 %\* | 0.35\* | 29.93 % | 35.32 % | 427.6 | 14 % | 0.04 |
| Top-Top | 2.79 % | 1.22 %\* | 0.98 %\* | 2.01 %\* | 12.59 %\* | 0.22 | 33.4 % | 12.07 % | 431.17 | 6.36 % | 0.01 |
| Top ESG-Bottom SMIS | 2.69 % | 1.24 %\* | 1 %\* | 2.06 %\* | 12.9 %\* | 0.21 | 39.43 %\* | 9.31 % | 433.6 | 4.63 % | 0.01 |
| Bottom ESG-Top SMIS | 4.02 % | 1.01 %\* | 0.82 %\* | 1.7 %\* | 10.82 %\* | 0.37\* | 32.6 % | 36.15 % | 425.47 | 15.8 % | 0.05 |
| Panel B - optimal tilting - EVaR portfolios | | | | | | | | | | | |
| optimal tilting - EVaR | mean | VaR | EVaR | CVaR | std | Sharpe | maxDD | turnover | # assets | max w\_i | HHI |
| Benchmark | 2.64 % | 1.29 %\* | 1.02 %\* | 2.11 %\* | 13.21 %\* | 0.2 | 37.68 %\* | 3.64 % | 512.58 | 3.21 % | 0.01 |
| Top ESG | 2.71 % | 1.28 %\* | 1.01 %\* | 2.08 %\* | 12.98 %\* | 0.21 | 36.26 % | 7 % | 439.51 | 4.12 % | 0.01 |
| Top SMIS | 2.89 % | 1.03 %\* | 0.81 %\* | 1.68 %\* | 10.8 %\* | 0.27 | 28.5 %\* | 36.99 % | 427.98 | 16.84 % | 0.05 |
| Top-Top | 2.57 % | 1.23 %\* | 0.97 %\* | 2 %\* | 12.56 %\* | 0.2 | 35.48 % | 12.04 % | 432.21 | 5.67 % | 0.01 |
| Top ESG-Bottom SMIS | 2.73 % | 1.28 %\* | 1 %\* | 2.06 %\* | 12.92 %\* | 0.21 | 38.3 %\* | 9.17 % | 434.6 | 4.32 % | 0.01 |
| Bottom ESG-Top SMIS | 3.8 % | 0.98 %\* | 0.8 %\* | 1.65 %\* | 10.56 %\* | 0.36\* | 31.61 % | 39.41 % | 424.98 | 17.9 % | 0.05 |
| Panel C - optimal tilting - mean-variance portfolios | | | | | | | | | | | |
| optimal tilting - MV | mean | VaR | EVaR | CVaR | std | Sharpe | maxDD | turnover | # assets | max w\_i | HHI |
| Benchmark | 2.64 % | 1.29 %\* | 1.02 %\* | 2.11 %\* | 13.21 %\* | 0.2 | 37.68 %\* | 3.64 % | 512.58 | 3.21 % | 0.01 |
| Top ESG | 2.6 % | 1.27 %\* | 1 %\* | 2.06 %\* | 12.89 %\* | 0.2 | 36.4 % | 6.84 % | 442.72 | 3.52 % | 0.01 |
| Top SMIS | 3.64 % | 0.98 %\* | 0.76 %\* | 1.56 %\* | 10.01 %\* | 0.36\* | 26.23 %\* | 32.28 % | 432.19 | 12.35 % | 0.03 |
| Top-Top | 2.91 % | 1.22 %\* | 0.97 %\* | 1.98 %\* | 12.44 %\* | 0.23 | 34.31 % | 11.15 % | 433.62 | 4.26 % | 0.01 |
| Top ESG-Bottom SMIS | 3.13 % | 1.23 %\* | 0.99 %\* | 2.04 %\* | 12.81 %\* | 0.24 | 36.02 % | 8.5 % | 437.58 | 3.82 % | 0.01 |
| Bottom ESG-Top SMIS | 3.49 % | 0.94 %\* | 0.74 %\* | 1.52 %\* | 10 %\* | 0.35\* | 30.67 % | 34.12 % | 427.81 | 13.58 % | 0.04 |
| Panel D - optimal tilting - max-Sharpe portfolios | | | | | | | | | | | |
| optimal tilting - max-Sharpe | mean | VaR | EVaR | CVaR | std | Sharpe | maxDD | turnover | # assets | max w\_i | HHI |
| Benchmark | 2.64 % | 1.29 % | 1.02 % | 2.11 % | 13.21 % | 0.2 | 37.68 % | 3.64 % | 512.58 | 3.21 % | 0.01 |
| Top ESG | 3.07 % | 1.3 % | 1.03 % | 2.11 % | 13.25 % | 0.23 | 35.52 % | 7.14 % | 454 | 4.41 % | 0.01 |
| Top SMIS | 4.35 % | 1.19 %\* | 0.92 %\* | 1.89 %\* | 12.18 %\* | 0.36 | 30.87 %\* | 35.98 % | 432.45 | 14.39 % | 0.05 |
| Top-Top | 2.81 % | 1.32 % | 1.02 % | 2.1 % | 13.12 % | 0.21 | 39.13 % | 11.81 % | 449.38 | 6.47 % | 0.01 |
| Top ESG-Bottom SMIS | 3.73 % | 1.29 % | 1.02 % | 2.1 % | 13.24 % | 0.28 | 34.82 % | 8.86 % | 451.83 | 4.92 % | 0.01 |
| Bottom ESG-Top SMIS | 3.47 % | 1.19 %\* | 0.93 %\* | 1.92 %\* | 12 %\* | 0.29 | 33.16 % | 39.8 % | 425.15 | 14.89 % | 0.05 |

Table 7: Out-of-sample portfolio performance of the optimal portfolios. The values with “\*” denote the measures that are outside the 90% confidence interval for random selection of assets to under/over-weight. The values outside the confidence interval are green if they are an improvement (e.g. lower risk or higher return), and red if they are a worsening.

## 8 Conclusions

SFDR is a relevant European framework aimed at improving the transparency and standardization of the sustainable investing landscape. The framework identifies three different classes of funds depending on their commitment to sustainability.
In this work we introduce a simple methodology that allows us to extract SFDR market-implied sustainability (SMIS) scores that reflect the under/over representation of specific stocks in SFDR 9 “dark green” funds compared to the rest of the market. We compute the measure on a large set of European companies, using equity funds for which we have a granular dataset with the quarterly composition of funds’ portfolios for the period 2002-2023.

SMIS scores are compared to the ESG scores provided by Refinitiv, finding that they carry substantially different information: companies with high implied SMIS scores are typically involved in sectors and activities relevant for the green transition, while the ones with low implied SMIS score are operating in controversial activities such as mining and fossil fuels. Instead, the highest ranked stocks according to the ESG scores are large multinational companies operating in a diverse spectrum of sectors (including controversial ones), while the lowest ranking are relatively small companies.

We perform an econometric analysis using quantile regression to explore the factors influencing the SMIS, focusing on the relationship between an asset’s ESG score (from Refinitiv) and its market-implied sustainability score. Key variables include company size, measured by total assets, and green involvement, assessed through green revenue. We find that the ESG score negatively impacts SMIS at lower quantiles but becomes positive at higher quantiles, indicating that SMIS differentiates between “bad” and “good” ESG scores, aligning with asset managers’ market-implied perspectives. Company size negatively influences SMIS at lower quantiles but shows no significant effect at higher quantiles, suggesting that larger companies are under-represented in SFDR 9 funds except for those with the highest SMIS scores. Green Revenues exhibit a consistently positive and significant impact, highlighting their critical role in SFDR 9 fund inclusion. Emission-related variables, such target reduction policies, positively correlate with higher SMIS scores, emphasizing investors’ preference for long-term sustainability commitments.

In the last section of the paper we exploit these characteristics and we show that, using portfolio tilting strategies, over-weighting stocks with high SMIS scores and under-weighting the ones with a low score has a beneficial effect on the risk-adjusted performance. On the contrary, over-weighting assets with high ESG score has a negative effect. We further explore the relation between SMIS scores and the financial performance by setting up optimal allocation strategies based on the minimization of risk or the maximization of reward-risk ratios with constraints based on the market-implied SMIS scores and ESG scores. The results confirm that portfolios tilted towards companies with high implied SMIS score tend to perform well in terms of lower risk, higher returns, and higher risk-adjusted performance. Such positive relationship between sustainability and performance may be due a better risk control (see e.g. Freeman [2010](https://arxiv.org/html/2510.20434v1#bib.bib17); Luo and Balvers [2017](https://arxiv.org/html/2510.20434v1#bib.bib28)), but also to the growing demand of sustainable investments, that led to strong investment flows towards ESG funds, as discussed by Van der Beck ([2021](https://arxiv.org/html/2510.20434v1#bib.bib3)).

The work contributes to the literature in several ways: first, our simple and replicable methodology allows to synthesize the market view of sustainability aggregating the view of multiple asset managers with different information sets, beliefs, constraints and goals. Second, by comparing SMIS scores with ESG scores, we explore the relationship between actual market practices and the ESG scores available to investors, showing that the connection is weak. Finally, we contribute to the debate on the performance of ESG funds, finding that, at least for the considered period, tilting the portfolios towards high ESG companies does not allow to improve performance, while tilting it towards companies with high SMIS scores allows to increase performance and reduce risk. The results are confirmed both by the simple tilting strategies, and the optimal tilting ones (that mimic portfolio strategies implemented by funds’ managers).

The framework that we propose can be extended in several directions that we leave for further works: examples are the detection of greenwashing practice, the identification of specific balance-sheet characteristics associated to high SMIS scores, and the implementation of more sophisticated asset allocation strategies. More generally, we believe that the development of market-based sustainability metrics is a fundamental step for the standardization and convergence of sustainability scores across rating agencies, allowing them to provide more relevant scores and to promptly catch relevant flows of information.

## Acknowledgments

This study was funded by the European Union - NextGenerationEU, in the framework of the GRINS -Growing Resilient, INclusive and Sustainable project (GRINS PE00000018 – CUP F83C22001720001). The views and opinions expressed are solely those of the authors and do not necessarily reflect those of the European Union, nor can the European Union be held responsible for them.

## Appendix A Alternative SFDR market-implied sustainability scores

We show here an alternative approach to compute the SMIS scores. Instead of comparing the percentage of funds with a given asset in the portfolio, we compare the average percentage of portfolio allocated in a given asset:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​M​I​S​wi=w9,i−wU\9,iSMISw\_{i}=w\_{9,i}-w\_{U\backslash 9,i} |  | (2) |

where:

* •

  w9,iw\_{9,i} is the average % allocation of asset ii-th in SFDR 9 funds,
* •

  wU\9,iw\_{U\backslash 9,i} is the average % allocation of asset ii-th in other funds.

We compute the statistical significance of the indicator by considering the standard tests for the comparison of sample means between populations with unequal sample size. The test statistic for test the null hypothesis H0:w9,i−wU\9,i=0H\_{0}:w\_{9,i}-w\_{U\backslash 9,i}=0 is:

|  |  |  |
| --- | --- | --- |
|  | t=w9,i−wU\9,isp⋅1/n1+1/n2,t=\displaystyle\frac{w\_{9,i}-w\_{U\backslash 9,i}}{s\_{p}\cdot\sqrt{1/n\_{1}+1/n\_{2}}}, |  |

where the pooled standard deviation sps\_{p} is

|  |  |  |
| --- | --- | --- |
|  | sp=(n1−1)​s12+(n2−1)​s22n1+n2−2,s\_{p}=\sqrt{\frac{(n\_{1}-1)s^{2}\_{1}+(n\_{2}-1)s^{2}\_{2}}{n\_{1}+n\_{2}-2}}, |  |

n1n\_{1} and n2n\_{2} are the number of SFDR 9 and other funds, respectively, and the test statistic is distributed as a Student’s t distribution with n1+n2−2n\_{1}+n\_{2}-2 degrees of freedom.

Figure [10](https://arxiv.org/html/2510.20434v1#A1.F10 "Figure 10 ‣ Appendix A Alternative SFDR market-implied sustainability scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") reports the scatterplot between the alternative SMISw score and the ESG score. We see that the distributions and the historical evolution are qualitatively similar to the ones in Figure [6](https://arxiv.org/html/2510.20434v1#S5.F6 "Figure 6 ‣ 5.2 SMIS scores and ESG scores ‣ 5 Computation of SMIS scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings"). Figure [11](https://arxiv.org/html/2510.20434v1#A1.F11 "Figure 11 ‣ Appendix A Alternative SFDR market-implied sustainability scores ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings") shows the relation between SMIS and SMISw scores, highlighting a positive relation between the two measures.

![Refer to caption](elephant_ears_history_w.png)


Figure 10: Alternative Market-implied sustainability score (SMISw score) vs ESG score for three time periods. Red dots represent stocks with SMISw score statistically significantly different from 0 with 90% confidence.

![Refer to caption](SFDR_vs_SFDRw.png)


Figure 11: Alternative Market-implied sustainability score (SMISw score) vs SMIS score for three time periods.

## Appendix B Optimisation Models

* •

  Mean-risk portfolios. The first three allocation strategies aim to minimize a risk measure ρ​(x)\rho(x),101010Denote by 𝕃p\mathbb{L}^{p} the set of all random variables XX with 𝔼​[|X|p]<+∞\mathbb{E}[|X|^{p}]<+\infty, defined on a probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}),
  where p∈[1,+∞)p\in[1,+\infty). A risk measure is defined as a mapping from a set of random variables to the real numbers
  ρ:𝕃p→ℝ∪{+∞}\rho:\mathbb{L}^{p}\to\mathbb{R}\cup\{+\infty\}.
  while constraining the expected return to be higher or equal that the one of the benchmark, while respecting the budget constraint and setting upper and lower bounds in order to under/over-weight assets based on the preselection strategies described above:

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | min𝒘∈ℝn\displaystyle\min\_{\boldsymbol{w}\in\mathbb{R}^{n}} | ρ​(R​𝒘)\displaystyle\rho(R\boldsymbol{w}) |  | (3) |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | s.t.\displaystyle s.t.\quad | 𝒘′​𝟏=1,\displaystyle\boldsymbol{w}^{\prime}\boldsymbol{1}=1, |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | 𝔼​[R]​𝒘≥𝔼​[Rb​m​k],\displaystyle\mathbb{E}[R]\boldsymbol{w}\geq\mathbb{E}[R\_{bmk}], |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | wi≤u​bi,\displaystyle w\_{i}\leq ub\_{i}, |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | wi≥l​bi.\displaystyle w\_{i}\geq lb\_{i}. |  |

  where 𝒘=[w1,…,wn]′\boldsymbol{w}=[w\_{1},\dots,w\_{n}]^{\prime} is the [n×1][n\times 1] vector of portfolio weights, RR is the n−n-variate random variable that denotes the returns of the assets, Rb​m​kR\_{bmk} the returns of the benchmark portfolio, and l​bilb\_{i}, u​biub\_{i} the lower and upper bound of asset ii, computed as follows:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | l​bi={wi,b​m​kif ​Xi∈𝒜over,0otherwise.,u​bi={wi,b​m​kif ​Xi∈𝒜under,1otherwise.lb\_{i}=\begin{cases}w\_{i,bmk}&\text{if }X\_{i}\in\mathcal{A}\_{\text{over}},\\ 0&\text{otherwise}.\end{cases},\quad ub\_{i}=\begin{cases}w\_{i,bmk}&\text{if }X\_{i}\in\mathcal{A}\_{\text{under}},\\ 1&\text{otherwise}.\end{cases} |  | (4) |

  The three risk measures considered are variance (mean-variance portfolio), CVaRα - Conditional Value at Risk (mean-CVaR portfolio), and expectile (mean-EVaR portfolio). The first is the classical Markowitz portfolio (Markowitz [1952](https://arxiv.org/html/2510.20434v1#bib.bib30)) with additional upper and lower bound constraints, and it can be written as a quadratic program with linear constraints. Mean-CVaR portfolio can be formulated as a linear program (see Rockafellar and Uryasev [2000](https://arxiv.org/html/2510.20434v1#bib.bib34)). Finally, mean-EVaR is based on the framework in Bellini et al. ([2021](https://arxiv.org/html/2510.20434v1#bib.bib4)), where the EVaR is the 1−α1-\alpha expectile of the portfolio returns’ changed in sign (Bellini and Di Bernardino [2017](https://arxiv.org/html/2510.20434v1#bib.bib5)). The problem can be expressed as a linear program (Bellini et al. [2021](https://arxiv.org/html/2510.20434v1#bib.bib4); Torri and Giacometti [2022](https://arxiv.org/html/2510.20434v1#bib.bib38)).
* •

  Maximum Sharpe ratio portfolio. This strategy maximises the Sharpe ratio of the portfolio, defined as the ratio between excess return and standard deviation.

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | max𝒘∈ℝn\displaystyle\max\_{\boldsymbol{w}\in\mathbb{R}^{n}} | 𝔼​[R]​𝒘−rf𝒘′​𝚺​𝒘\displaystyle\frac{\mathbb{E}[R]\boldsymbol{w}-r\_{f}}{\boldsymbol{w}^{\prime}\boldsymbol{\Sigma}\boldsymbol{w}} |  | (5) |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | s.t.\displaystyle s.t.\quad | 𝒘′​𝟏=1,\displaystyle\boldsymbol{w}^{\prime}\boldsymbol{1}=1, |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | wi≤u​bi,\displaystyle w\_{i}\leq ub\_{i}, |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | wi≥l​bi.\displaystyle w\_{i}\geq lb\_{i}. |  |

  Assuming that a portfolio with expected return higher that the risk-free rate exists, the problem ([5](https://arxiv.org/html/2510.20434v1#A2.E5 "In 2nd item ‣ Appendix B Optimisation Models ‣ Market-Implied Sustainability: Insights from Funds’ Portfolio Holdings")) can be reformulated as a quadratic program:111111With the exception of the upper and lower bound constraints the formulation is analogous to Cornuejols and
  Tütüncü ([2006](https://arxiv.org/html/2510.20434v1#bib.bib11)).

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | min𝒙∈ℝn,y∈ℝ\displaystyle\min\_{\boldsymbol{x}\in\mathbb{R}^{n},y\in\mathbb{R}} | 𝒙′​𝚺​𝒙\displaystyle\boldsymbol{x}^{\prime}\boldsymbol{\Sigma}\boldsymbol{x} |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | s.t.\displaystyle s.t.\quad | (𝔼​[R]​𝒙−rf)=1\displaystyle(\mathbb{E}[R]\boldsymbol{x}-r\_{f})=1 |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | 𝒙′​𝟏=y\displaystyle\boldsymbol{x}^{\prime}\boldsymbol{1}=y |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | xi/y≤u​bi,i=1,…​n\displaystyle x\_{i}/y\leq ub\_{i},\quad i=1,\dots n |  |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  |  | xi/y≥l​bi,i=1,…​n.\displaystyle x\_{i}/y\geq lb\_{i},\quad i=1,\dots n. |  | (6) |

  where the vector of portfolio weights is 𝒘=𝒙/y\boldsymbol{w}=\boldsymbol{x}/y. The problem is quadratic with linear constraints as the last two constraints can be rewritten as xi≤y⋅u​bix\_{i}\leq y\cdot ub\_{i} and xi≥y⋅l​bix\_{i}\geq y\cdot lb\_{i}, respectively.

## References

* Amel-Zadeh and Serafeim (2018)

  Amel-Zadeh, A., Serafeim, G.,
  2018.
  Why and how investors use ESG information: Evidence
  from a global survey.
  Financial Analysts Journal 74,
  87–103.
* Becchetti et al. (2018)

  Becchetti, L., Ciciretti, R.,
  Dalò, A., 2018.
  Fishing the corporate social responsibility risk
  factors.
  Journal of Financial Stability
  37, 25–48.
* Van der Beck (2021)

  Van der Beck, P., 2021.
  Flow-driven esg returns.
  Swiss Finance Institute Research Paper .
* Bellini et al. (2021)

  Bellini, F., Cesarone, F.,
  Colombo, C., Tardella, F.,
  2021.
  Risk parity with expectiles.
  European journal of operational research
  291, 1149–1163.
* Bellini and Di Bernardino (2017)

  Bellini, F., Di Bernardino, E.,
  2017.
  Risk management with expectiles.
  The European Journal of Finance
  23, 487–506.
* Benuzzi et al. (2023)

  Benuzzi, M., Bax, K.,
  Paterlini, S., Taufer, E.,
  2023.
  Chasing ESG performance: Revealing the impact of
  refinitiv’s scoring system.
  Available at SSRN 4662257 .
* Berg et al. (2022)

  Berg, F., Koelbel, J.F.,
  Rigobon, R., 2022.
  Aggregate confusion: The divergence of esg ratings.
  Review of Finance 26,
  1315–1344.
* Billio et al. (2021)

  Billio, M., Costola, M.,
  Hristova, I., Latino, C.,
  Pelizzon, L., 2021.
  Inside the ESG ratings:(Dis) agreement and
  performance.
  Corporate Social Responsibility and Environmental
  Management 28, 1426–1445.
* Bruyn (1987)

  Bruyn, S., 1987.
  The Field of Social Investment.
  Cambridge University Press, London.
* Canay (2011)

  Canay, I.A., 2011.
  A simple approach to quantile regression for panel
  data.
  The econometrics journal 14,
  368–386.
* Cornuejols and
  Tütüncü (2006)

  Cornuejols, G., Tütüncü, R.,
  2006.
  Optimization methods in finance.
  volume 5.
  Cambridge University Press.
* Dorfleitner et al. (2020)

  Dorfleitner, G., Kreuzer, C.,
  Sparrer, C., 2020.
  ESG controversies and controversial ESG: about
  silent saints and small sinners.
  Journal of Asset Management 21,
  393–412.
* Elamer and Boulhaga (2024)

  Elamer, A.A., Boulhaga, M.,
  2024.
  ESG controversies and corporate performance: The
  moderating effect of governance mechanisms and ESG practices.
  Corporate Social Responsibility and Environmental
  Management 31, 3312–3327.
* Eurosif (2018)

  Eurosif, 2018.
  European SRI study 2018.
* Fabozzi et al. (2008)

  Fabozzi, F.J., Ma, K.,
  Oliphant, B.J., 2008.
  Sin stock returns.
  The Journal of Portfolio Management
  35, 82–94.
* Fetting (2020)

  Fetting, C., 2020.
  The european green deal.
  ESDN Report, December 2,
  53.
* Freeman (2010)

  Freeman, R.E., 2010.
  Strategic management: A stakeholder approach.
  Cambridge university press.
* de Freitas Netto et al. (2020)

  de Freitas Netto, S.V., Sobral, M.F.F.,
  Ribeiro, A.R.B., Soares, G.R.d.L.,
  2020.
  Concepts and forms of greenwashing: A systematic
  review.
  Environmental Sciences Europe
  32, 1–12.
* Gibson Brandon et al. (2021)

  Gibson Brandon, R., Krueger, P.,
  Schmidt, P.S., 2021.
  Esg rating disagreement and stock returns.
  Financial analysts journal 77,
  104–127.
* GSIA (2020)

  GSIA, 2020.
  Global sustainable investment review 2020.
* He (1997)

  He, X., 1997.
  Quantile curves without crossing.
  The American Statistician 51,
  186–192.
* Hong and Kacperczyk (2009)

  Hong, H., Kacperczyk, M.,
  2009.
  The price of sin: The effects of social norms on
  markets.
  Journal of financial economics
  93, 15–36.
* Hornuf and Yüksel (2024)

  Hornuf, L., Yüksel, G.,
  2024.
  The performance of socially responsible investments:
  A meta-analysis.
  European Financial Management
  30, 1012–1061.
* Hylton (1992)

  Hylton, M.O., 1992.
  Socially responsible investing: Doing good versus
  doing well in an inefficient market.
  Am. UL Rev. 42,
  1.
* Koenker (2004)

  Koenker, R., 2004.
  Quantile regression for longitudinal data.
  Journal of multivariate analysis
  91, 74–89.
* Lamarche (2010)

  Lamarche, C., 2010.
  Robust penalized quantile regression estimation for
  panel data.
  Journal of Econometrics 157,
  396–408.
* Lambillon and Chesney (2023)

  Lambillon, A.P., Chesney, M.,
  2023.
  How green is ‘dark green’? an analysis of SFDR
  article 9 funds.
  Available at SSRN 4366889 .
* Luo and Balvers (2017)

  Luo, H.A., Balvers, R.J.,
  2017.
  Social screens and systematic investor boycott risk.
  Journal of Financial and Quantitative Analysis
  52, 365–399.
* Machado and Silva (2019)

  Machado, J.A., Silva, J.S.,
  2019.
  Quantiles via moments.
  Journal of econometrics 213,
  145–173.
* Markowitz (1952)

  Markowitz, H., 1952.
  Portfolio selection.
  The Journal of Finance 7,
  77–91.
* Morningstar Sustainalytics (2024a)

  Morningstar Sustainalytics, 2024a.
  Global Sustainable Fund Flows: Q3 2024 in Review.
  Technical Report. Morningstar Sustainalytics.
* Morningstar Sustainalytics (2024b)

  Morningstar Sustainalytics, 2024b.
  SFDR Article 8 and Article 9 Funds: Q3 2024
  in Review.
  Technical Report. Morningstar Sustainalytics.
* Revelli and Viviani (2015)

  Revelli, C., Viviani, J.L.,
  2015.
  Financial performance of socially responsible
  investing (SRI): What have we learned? A meta-analysis.
  Business Ethics: A European Review
  24, 158–185.
* Rockafellar and Uryasev (2000)

  Rockafellar, R., Uryasev, S.,
  2000.
  Optimization of Conditional Value-at-Risk.
  Journal of risk 2,
  21–42.
* Sandberg et al. (2009)

  Sandberg, J., Juravle, C.,
  Hedesström, T.M., Hamilton, I.,
  2009.
  The heterogeneity of socially responsible
  investment.
  Journal of business ethics 87,
  519–533.
* Scheitza and Busch (2024)

  Scheitza, L., Busch, T.,
  2024.
  SFDR article 9: Is it all about impact?
  Finance Research Letters 62,
  105179.
* The Global Compact (2004)

  The Global Compact, 2004.
  Who Cares Wins. Connecting Financial Markets to a
  Changing World.
  Technical Report. The Global Compact.
* Torri and Giacometti (2022)

  Torri, G., Giacometti, R.,
  2022.
  Penalized expectiles optimal portfolios.
  Available at SSRN 4018243 .
* Zhao (2000)

  Zhao, Q., 2000.
  Restricted regression quantiles.
  Journal of Multivariate Analysis
  72, 78–99.