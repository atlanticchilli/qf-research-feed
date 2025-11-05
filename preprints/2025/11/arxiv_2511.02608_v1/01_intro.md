---
authors:
- Yudi Yang
- Fan Yang
- Xiajie Yi
- Dongwei He
doc_id: arxiv:2511.02608v1
family_id: arxiv:2511.02608
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'How FinTech affects financial sustainability: Evidence from Chinese commercial
  banks using a three-stage network DEA-Malmquist model'
url_abs: http://arxiv.org/abs/2511.02608v1
url_html: https://arxiv.org/html/2511.02608v1
venue: arXiv q-fin
version: 1
year: 2025
---


Yudi Yang a, Fan Yang a, ∗\* , Xiajie Yi b, ∗\*, Dongwei He a, 111Corresponding authors. E-mail address: fan\_yang@shnu.edu.cn (F. Yang), x.yi@ieseg.fr(X. Yi),
  
donwayho@shnu.edu.cn (D. He).
  
  
a School of Finance and Business, Shanghai Normal University, Shanghai, China
  
b IÉSEG School of Management, University Lille, CNRS, UMR 9221 - LEM - Lille
  
Economie Management, F-59000 Lille, France

###### Abstract

This paper investigates the impact of financial technology (FinTech) on the financial sustainability (FS) of commercial banks. We employ a three-stage network DEA-Malmquist model to evaluate the FS performance of 104 Chinese commercial banks from 2015 to 2023. A two-way fixed effects model is utilized to examine the effects of FinTech on FS, revealing a significant negative relationship. Further mechanistic analysis indicates that FinTech primarily undermines FS by eroding banks’ loan efficiency and profitability. Notably, banks with more patents or listed status demonstrate greater resilience to FinTech disruptions. These findings help banks identify external risks stemming from FinTech development, and by elucidating the mechanisms underlying FS, enhance their capacity to monitor and manage FS in the era of rapid FinTech advancement.
  
Keywords: Financial technology, Financial sustainability, DEA-Malmquist model, Two-way fixed effects model, Commercial banks

## 1 Introduction

Commercial banks play a central role in a financial system by channeling funds from savers to businesses and supporting liquidity creation. Their stability and sustainability are vital to overall economic development. In 2023, Silicon Valley Bank (SVB) went bankrupt due to bank runs, in which many depositors withdrew their deposits simultaneously out of concern that the bank might become insolvent. The collapse of SVB stemmed from an overreliance on short-term deposits from tech firms and excessive exposure to long-term fixed-income securities. When interest rates rose sharply, the bank faced an acute liquidity crisis (Metrick,, [2024](https://arxiv.org/html/2511.02608v1#bib.bib42)). As the 16th largest bank in the US, the collapse of SVB triggered the failures of Silvergate Bank and Signature Bank, raising concerns about the resilience of the banking system and the potential for contagion across the broader financial sector. Aharon et al., ([2023](https://arxiv.org/html/2511.02608v1#bib.bib2)) document abnormal returns on both event and post-event days, indicating a negative response to the collapse of SVB in equity markets. Akhtaruzzaman et al., ([2023](https://arxiv.org/html/2511.02608v1#bib.bib3)) indicate that the collapse of SVB severely shook and threatened the global banking industry, and led to a pronounced elevation of financial contagion confined to the banking sector. Overall, this event reveals weaknesses in the risk management of banks and asset allocation. It also underscores the critical role of maintaining financial resilience and sustainability in the banking sector to prevent global systemic risks amid rising interest rates and increasing uncertainty.

According to the National Administration of Financial Regulation (NAFR)222The data on total assets and liabilities refer to quarterly figures for legal-person banking institutions. Before 2018, the data were released by the former China Banking Regulatory Commission (CBRC). Since 2023, they have been published by the NAFR, which succeeded the CBRC., the total assets of Chinese commercial banks increased from 155.83 trillion yuan in 2015 to 354.85 trillion yuan in 2023, while total liabilities rose from 144.27 trillion yuan to 327.15 trillion yuan during the same period. These numbers represent increases of 127.72% and 126.76%, respectively, underscoring the sustained expansion of scale and financial depth of the banking sector, as shown in Figure [1](https://arxiv.org/html/2511.02608v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"). It should be noted that the growth in total assets and liabilities does not necessarily indicate improved financial sustainability (FS). Larger balance sheets, although indicative of business expansion, do not guarantee enhanced profitability or sufficient internal revenue to cover operating costs. At the same time, a rapid increase may entail higher leverage or riskier investments, which can exacerbate costs and financial vulnerability. Here the FS refers to the ability of a firm to cover its operating costs through internal revenue without external support (Zeller and Meyer,, [2002](https://arxiv.org/html/2511.02608v1#bib.bib68)). It encompasses various aspects of bank operations, such as financial performance, risk management, and strategic planning. This definition has been widely studied in empirical studies of microfinance institutions (MFIs). One stream of research provides systematic reviews of FS in MFIs (Gupta and Sharma,, [2023](https://arxiv.org/html/2511.02608v1#bib.bib27); Maeenuddin et al.,, [2023](https://arxiv.org/html/2511.02608v1#bib.bib39)). Another stream examines factors affecting FS, including the trade-offs between social objectives and financial performance in MFIs (Wry and Zhao,, [2018](https://arxiv.org/html/2511.02608v1#bib.bib63)), internal arrangements that influence sustainability (Dabi et al.,, [2023](https://arxiv.org/html/2511.02608v1#bib.bib20)), and analyses of FS in commercial banks, such as its classifications and key determinants (Shi et al.,, [2025](https://arxiv.org/html/2511.02608v1#bib.bib51)). These studies provide a detailed account of the significance of FS in financial institutions, and imply that appropriate indicators must be selected based on its definition.

20152016201720182019202020212022202305050100100150150200200250250300300350350156156182182197197210210239239266266289289320320355355144144169169182182193193220220245245265265294294327327YearTrillion yuanTotal assetsTotal liabilities


Figure 1: The total assets and liabilities of Chinese commercial banks from 2015 to 2023

Measuring FS is an important methodological challenge. Given its multidimensional nature, identifying appropriate measurement methods is essential. Such methods are generally categorized into single-factor and multi-factor ways. The former methods focus on one representative financial ratio to reflect the financial condition of an entity. For example, indicators such as financial self-sufficiency (Kinde,, [2012](https://arxiv.org/html/2511.02608v1#bib.bib32)), return on assets (ROA) (Najam et al.,, [2022](https://arxiv.org/html/2511.02608v1#bib.bib44)), and operational self-sufficiency (Bogan,, [2012](https://arxiv.org/html/2511.02608v1#bib.bib11); Abu Wadi et al.,, [2022](https://arxiv.org/html/2511.02608v1#bib.bib1); Fonchamnyo et al.,, [2023](https://arxiv.org/html/2511.02608v1#bib.bib23)) are commonly used. Single-factor approaches often fail to account explicitly for risk, which may lead to biased assessments of the actual performance of banks (Prior et al.,, [2019](https://arxiv.org/html/2511.02608v1#bib.bib46)). To overcome this limitation, multi-factor measurements often incorporate financial and non-financial variables to capture a more comprehensive picture of FS. Data Envelopment Analysis (DEA) (Charnes et al.,, [1978](https://arxiv.org/html/2511.02608v1#bib.bib16)) is one of the most widely used approaches (Shi et al.,, [2020](https://arxiv.org/html/2511.02608v1#bib.bib52)). DEA is a non-parametric method that evaluates organizational performance by integrating multiple input and output indicators into a composite index. The method calculates the efficiency in converting consumed resources into final outputs. Its advantages include not requiring assumptions about the underlying distribution of performance variables and accommodating conflicting performance measures. Consequently, it has been applied in diverse fields such as energy management (Wei and Zhao,, [2024](https://arxiv.org/html/2511.02608v1#bib.bib60)), environmental governance (Zhang et al.,, [2020](https://arxiv.org/html/2511.02608v1#bib.bib69)), public services (Kohl et al.,, [2019](https://arxiv.org/html/2511.02608v1#bib.bib33)), the pharmaceutical industry (Qiu et al.,, [2023](https://arxiv.org/html/2511.02608v1#bib.bib47)), etc. In the banking industry, scholars have developed multi-stage network DEA models to reflect the structure of the banking sector. For instance, Wang et al., ([2014](https://arxiv.org/html/2511.02608v1#bib.bib56)) use an additive two-stage network DEA for Chinese commercial banks to assess overall and stage efficiencies in deposit producing and profit earning stages. Similarly, a two-stage network DEA model is applied by Fukuyama et al., ([2020](https://arxiv.org/html/2511.02608v1#bib.bib24)) to divide the banking process into fund-raising and revenue-generation stages. Shi et al., ([2025](https://arxiv.org/html/2511.02608v1#bib.bib51)) adopt a three-stage network DEA approach for US commercial banks, decomposing the process into deposit, loan, and profitability stages. Overall, the indicators developed in these studies reflect FS across multiple operational stages and show that it is influenced by multiple factors. However, with technological changes, competitive pressures arise not only from internal operations but also from external factors. Among the emerging external factors, the rapid development of financial technology (FinTech) has attracted increasing attention. It is changing the business landscape for banks, expanding their services, and “interfering” in the fields traditionally covered by banks (Romānova and Kudinska,, [2016](https://arxiv.org/html/2511.02608v1#bib.bib48)).

Generally, FinTech uses technology to provide new and improved financial services (Thakor,, [2020](https://arxiv.org/html/2511.02608v1#bib.bib54)). Among the major economies in the world, China offers an example of how FinTech has rapidly taken hold in practice. In 2016, the total financing of Chinese FinTech companies reached 7.7 billion US dollars, surpassing that of the US for the first time, making China the largest market in the world (Gao,, [2022](https://arxiv.org/html/2511.02608v1#bib.bib25)). By 2022, in terms of transaction volume, Alipay and WeChat Pay accounted for over 90% of the mobile payment market. The emergence of FinTech exerts various impacts on traditional financial sectors, and its influence on conventional commercial banks remains debated. Existing studies find that FinTech has driven the transformation of the banking sector and challenged traditional banking practices (Romānova and Kudinska,, [2016](https://arxiv.org/html/2511.02608v1#bib.bib48); Thakor,, [2020](https://arxiv.org/html/2511.02608v1#bib.bib54)). On the one hand, FinTech improves efficiency and promotes innovation. Lee et al., ([2021](https://arxiv.org/html/2511.02608v1#bib.bib34)) show that FinTech enhances the cost efficiency and technological capabilities of banks by optimizing resource allocation, reducing operational costs, and expanding service boundaries. [Wang et al., 2021b](https://arxiv.org/html/2511.02608v1#bib.bib58)  also find that commercial banks adopt FinTech to upgrade traditional business models, which helps improve operational efficiency and overall competitiveness. On the other hand, FinTech exerts disruptive effects on banks. Studies show that FinTech diverts business from traditional channels through third-party payments and internet wealth management, thereby reducing interest margins and increasing risks to profitability (Murinde et al.,, [2022](https://arxiv.org/html/2511.02608v1#bib.bib43); Lee et al.,, [2023](https://arxiv.org/html/2511.02608v1#bib.bib35)). Li et al., ([2023](https://arxiv.org/html/2511.02608v1#bib.bib36)) find that the “Matthew Effect” in FinTech investment concentrates resources in large banks, placing small and medium-sized banks at a technological and capital disadvantage. Excessive reliance on external technology may also lead to technological dependency and worsen operational risks such as data security and privacy breaches. Furthermore, [Wang et al., 2021a](https://arxiv.org/html/2511.02608v1#bib.bib57)  show that FinTech development increases bank risk-taking, with more potent effects for larger banks with greater involvement in shadow banking. As noted above, the rise of FinTech has introduced both opportunities and threats to banking operations, which affect the FS of banks in turn.

FinTech might promote bank development through technology spillover effects. It may also undermine traditional operations through competition effects. The effect of FinTech on the long-term FS of banks, however, remains unclear. To the best of our knowledge, previous studies do not systematically examine the relationship between FS and FinTech. Therefore, we conduct an empirical analysis to investigate how FinTech influences the FS of Chinese commercial banks. The analysis is based on panel data from 104 commercial banks between 2015 and 2023. Besides, we also perform robustness checks to validate our findings.

The main contributions of this paper are threefold. First, we construct a three-stage network DEA-Malmquist framework to measure the dynamic FS of Chinese commercial banks. This framework also captures the efficiencies of FS in its the deposit, loan, and profitability sub-stages. Second, we use a two-way fixed effects model to examine how FinTech affects FS and the transmission channels, which fills a gap in the literature on FS. Third, we further explore heterogeneity across banks with different levels of innovation and marketization.

The remainder of the paper proceeds as follows. Section [2](https://arxiv.org/html/2511.02608v1#S2 "2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model") introduces the three-stage network DEA-Malmquist model for the FS and the empirical model. In Section [3](https://arxiv.org/html/2511.02608v1#S3 "3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"), we empirically evaluate the impact of FinTech on the FS of 104 Chinese commercial banks. Finally, in Section [4](https://arxiv.org/html/2511.02608v1#S4 "4 Conclusion ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"), we discuss the findings and future research possibilities.

## 2 Methodology

This section outlines the methodological framework and describes the data used for the regression analysis. To empirically measure FS, we adopt a three-stage network DEA model of Shi et al., ([2025](https://arxiv.org/html/2511.02608v1#bib.bib51)) in combination with the Malmquist productivity index (MI) (Malmquist,, [1953](https://arxiv.org/html/2511.02608v1#bib.bib40)). Thereafter, to analyze the relationship between FinTech and FS, we employ a two-way fixed effects model (Wooldridge,, [2010](https://arxiv.org/html/2511.02608v1#bib.bib61); Hsiao,, [2014](https://arxiv.org/html/2511.02608v1#bib.bib29)) and present an overview of the relevant data. The dataset consists of panel data from 104 commercial banks in China from 2015 to 2023. Bank-level data are obtained from the CSMAR333CSMAR (China Stock Market & Accounting Research Database), developed by GTA Information Technology Co., Ltd., is widely used for empirical studies on the Chinese capital market. and Wind444Wind Database, developed by Wind Information Co., Ltd., provides comprehensive financial and economic data for China. databases, with missing values supplemented by annual reports555The reports are derived from the official websites of various banks and the China Foreign Exchange Trade System. of the commercial banks. Additionally, macroeconomic data are collected from the China Statistical Yearbook.

### 2.1 The three-stage network DEA-Malmquist model

Sherman and Gold, ([1985](https://arxiv.org/html/2511.02608v1#bib.bib50)) first apply DEA to banking studies, after which DEA has been widely used to address banking problems. Staub et al., ([2010](https://arxiv.org/html/2511.02608v1#bib.bib53)) develop a DEA model to measure cost, technical, and allocative efficiencies of Brazilian banks, finding that inefficiency was mainly technical and state-owned banks were more cost efficient than other types of banks. Avkiran, ([2015](https://arxiv.org/html/2511.02608v1#bib.bib5)) uses a dynamic network DEA model (DN-DEA) to evaluate Chinese commercial banks, showing that DN-DEA captures dynamic performance and highlights sub-unit inefficiencies. Recently, Shi et al., ([2025](https://arxiv.org/html/2511.02608v1#bib.bib51)) construct the FS of commercial banks in the US using a three-stage network DEA model, conceptualizing FS as a multi-stage, multi-factor structure. They also develop a random forest model with SHapley Additive exPlanations (SHAP) to analyze the impacts of variables. Further references can be consulted in Matthews, ([2013](https://arxiv.org/html/2511.02608v1#bib.bib41)), Yu et al., ([2021](https://arxiv.org/html/2511.02608v1#bib.bib67)), Xie et al., ([2022](https://arxiv.org/html/2511.02608v1#bib.bib65)), and Li et al., ([2024](https://arxiv.org/html/2511.02608v1#bib.bib37)).

Bank operations encompass a diverse range of operations, and FinTech has carried distinct degrees of importance across these activities in recent years. As a result, FS has also been impacted by FinTech. In particular, the emergence of third-party payment platforms has simultaneously disrupted the ability of banks to attract deposits and challenged their profitability. These changes underscore the need for a comprehensive framework to evaluate FS across the stages of bank operations. For this purpose, we adopt the three-stage network DEA model by Shi et al., ([2025](https://arxiv.org/html/2511.02608v1#bib.bib51)). This approach decomposes the banking process into three stages: the deposit stage, the loan stage, and the profitability stage, based on the production approach (Sealey Jr. and Lindley,, [1977](https://arxiv.org/html/2511.02608v1#bib.bib49)) and the intermediation approach (Benston,, [1965](https://arxiv.org/html/2511.02608v1#bib.bib10)). Figure [2](https://arxiv.org/html/2511.02608v1#S2.F2 "Figure 2 ‣ 2.1 The three-stage network DEA-Malmquist model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model") illustrates the structure of this three-stage DEA model.

![Refer to caption](pictures/process_with_character.png)


Figure 2: Three-stage network DEA structure for FS

Specifically, following Figure [2](https://arxiv.org/html/2511.02608v1#S2.F2 "Figure 2 ‣ 2.1 The three-stage network DEA-Malmquist model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"), in the deposit stage, the focus is on capturing the FS factors involved in deposit-taking. This stage evaluates the ability of the bank to attract customer deposits and its capacity to manage deposits effectively. Salary per employee, capital expenditures (CapEx), and equity of shareholders are initial inputs, representing labor cost structure, capital investment, and financial strength. The outputs from this stage include total deposits, cash from operations, and return on equity (ROE). Subsequently, in the loan stage, the banks utilize the outputs of the deposit stage (deposits and operating cash) as primary funding sources, with total assets added as an external input. The outputs from this stage include net loan amount, net interest income, and ROA, reflecting credit issuance capacity and asset utilization efficiency. Finally, the profitability stage measures the FS of banks. It focuses on their ability to convert income from various sources into profits that benefits employees, customers, and investors. Given that most commercial banks in China are not publicly listed, we replace earnings per share with net profit margin and shares outstanding with share capital in the original model of Shi et al., ([2025](https://arxiv.org/html/2511.02608v1#bib.bib51)). Therefore, revenue per employee, total revenue, and net profit margin are treated as outputs that measure this ability.

We employ the additive efficiency decomposition method (Cook et al.,, [2010](https://arxiv.org/html/2511.02608v1#bib.bib18)), implemented for a three-stage network DEA (Shi et al.,, [2025](https://arxiv.org/html/2511.02608v1#bib.bib51)), to model the structure in Figure [2](https://arxiv.org/html/2511.02608v1#S2.F2 "Figure 2 ‣ 2.1 The three-stage network DEA-Malmquist model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"). Let I={1,2,…,|I|}I=\{1,2,\dots,|I|\} denote the set of decision-making units (DMUs), where each i∈Ii\in I represents a bank, denoted as D​M​UiDMU\_{i}. Let P={1,…,|P|}P=\{1,\dots,|P|\} represent the set of stages in the process, with p∈Pp\in P indexing each stage.
Following the network DEA framework established by Cook et al., ([2010](https://arxiv.org/html/2511.02608v1#bib.bib18)), we classify the flows into and out of each stage pp as distinct vectors to ensure clear definition:

1. (1)

   RpR\_{p}-dimensional vector Z0Z\_{0}: The inputs enter the first stage (p=1p=1);
2. (2)

   RpR\_{p}-dimensional vector Zp1Z\_{p}^{1}: The outputs are generated at stage pp and not passed to the stage p+1p+1;
3. (3)

   SpS\_{p}-dimensional vector Zp2Z\_{p}^{2}: The outputs are generated at stage pp and transferred as inputs to the stage p+1p+1;
4. (4)

   JpJ\_{p}-dimensional vector Zp3Z\_{p}^{3}: External inputs enter the process at the beginning of stage p+1p+1.

The flow of these input and output vectors through the three-stage banking process is visually represented in Figure [2](https://arxiv.org/html/2511.02608v1#S2.F2 "Figure 2 ‣ 2.1 The three-stage network DEA-Malmquist model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"). The specific components of these vectors for D​M​UiDMU\_{i} are indexed as follows:

1. (1)

   zp​ri​1z\_{pr}^{i1} denotes the rr-th component (r=1,…,Rpr=1,\dots,R\_{p}) of the RpR\_{p}-dimensional output vector for D​M​UiDMU\_{i} flowing from stage pp, which leaves the process at that stage pp, and is not passed on as an input to stage p+1p+1. In the last stage |P||P|, all the outputs are viewed as z|P|​ri​1z\_{|P|r}^{i1}, as they leave the process;
2. (2)

   zp​ki​2z\_{pk}^{i2} denotes the kk-th component (k=1,…,Spk=1,\dots,S\_{p}) of the SpS\_{p}-dimensional output vector for D​M​UiDMU\_{i} flowing from stage pp, and is passed on as a portion of inputs to stage p+1p+1;
3. (3)

   zp​ji​3z\_{pj}^{i3} denotes the jj-th component (j=1,…,Jpj=1,\dots,J\_{p}) of the JpJ\_{p}-dimensional input vector for D​M​UiDMU\_{i} at stage p+1p+1, that enters the process at the beginning of that stage.

Specifically, for any stage pp (p≥2p\geq 2), the total inputs are derived from the intermediate output Zp−12Z\_{p-1}^{2} and the external input Zp−13Z\_{p-1}^{3}.
The weights for the above factors are defined as:

1. (1)

   up​ru\_{pr} is the weight assigned to the output component zp​ri​1z\_{pr}^{i1} flowing from stage pp;
2. (2)

   ηp​k\eta\_{pk} is the weight for the output component zp​ki​2z\_{pk}^{i2} at stage pp, and it is also assigned to the same component which becomes an input to stage p+1p+1;
3. (3)

   νp​j\nu\_{pj} is the weight assigned to the jj-th input component zp​ji​3z\_{pj}^{i3} that enters the process at the beginning of stage p+1p+1.

Table 1: Notations in the three-stage network DEA-Malmquist model

| Notation | Description |
| --- | --- |
| i∈{1,…,|I|}i\in\{1,\ldots,|I|\} | Index for DMUs. |
| p∈{1,…,|P|}p\in\{1,\ldots,|P|\} | Index for stages. |
| r∈{1,…,Rp}r\in\{1,\ldots,R\_{p}\} | Index for final output variables, where RpR\_{p} is the dimension of Zp1Z\_{p}^{1}. |
| k∈{1,…,Sp}k\in\{1,\ldots,S\_{p}\} | Index for intermediate output variables, where SpS\_{p} is the dimension of Zp2Z\_{p}^{2}. |
| j∈{1,…,Jp}j\in\{1,\ldots,J\_{p}\} | Index for external input variables, where JpJ\_{p} is the dimension of Zp3Z\_{p}^{3}. |
| t∈{1,…,|T|}t\in\{1,\ldots,|T|\} | Index for years in the MI model. |
| Z0Z\_{0} | The initial input vector to the first stage (p=1p=1). |
| Zp1Z\_{p}^{1} | The RpR\_{p}-dimensional output vector generated at stage pp. |
| Zp2Z\_{p}^{2} | The SpS\_{p}-dimensional output vector generated at stage pp that links to stage p+1p+1. |
| Zp3Z\_{p}^{3} | The JpJ\_{p}-dimensional input vector that enters the process at the beginning of stage p+1p+1. |
| zp​ri​1z\_{pr}^{i1} | The rr-th component of the final output vector Zp1Z\_{p}^{1} for D​M​UiDMU\_{i}, flowing from stage pp and exiting the process. |
| zp​ki​2z\_{pk}^{i2} | The kk-th component of the output vector Zp2Z\_{p}^{2} for D​M​UiDMU\_{i}, flowing from stage pp and passed on as an input to stage p+1p+1. |
| zp​ji​3z\_{pj}^{i3} | The jj-th component of the external input vector Zp3Z\_{p}^{3} for D​M​UiDMU\_{i}, which is an input to stage p+1p+1 and enters the process at its beginning. |
| up​ru\_{pr} | Weight for the rr-th output zp​ri​1z\_{pr}^{i1} at stage pp. |
| ηp​k\eta\_{pk} | Weight for the kk-th output zp​ki​2z\_{pk}^{i2} at stage pp. |
| νp​j\nu\_{pj} | Weight for the jj-th external input zp​ji​3z\_{pj}^{i3} entering stage p+1p+1. |
| θp\theta\_{p} | DEA estimated efficiency score of a D​M​UiDMU\_{i} at stage pp. |
| θ\theta | Weighted aggregate efficiency score across all stages, typically calculated using stage weights w1,w2,w3w\_{1},w\_{2},w\_{3}. |
| w1,w2,w3w\_{1},w\_{2},w\_{3} | Weights assigned to the efficiency scores of stages 1, 2, and 3, respectively, where w1+w2+w3=1w\_{1}+w\_{2}+w\_{3}=1. |
| θt+1t\theta^{t}\_{t+1} | Efficiency of the D​M​UiDMU\_{i} at time t+1t+1, measured against the period tt technology frontier; captures intertemporal efficiency in the MI. |
| θpt​(t+1)\theta\_{p}^{t}(t+1) | Efficiency of the D​M​UiDMU\_{i} at time t+1t+1 in stage pp, measured against the period tt technology frontier; captures intertemporal efficiency in the MI. |

When p=2,3,…p=2,3,\dots, the efficiency for D​M​UiDMU\_{i} would be expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θp=∑r=1Rpup​r​zp​ri​1+∑k=1Spηp​k​zp​ki​2+εp∑k=1Sp−1ηp−1​k​zp−1​ki​2+∑j=1Jpνp−1​j​zp−1​ji​3,εp​ is unrestricted in sign.\theta\_{p}=\frac{\sum\_{r=1}^{R\_{p}}u\_{pr}z\_{pr}^{i1}+\sum\_{k=1}^{S\_{p}}\eta\_{pk}z\_{pk}^{i2}+\varepsilon\_{p}}{\sum\_{k=1}^{S\_{p-1}}\eta\_{p-1k}z\_{p-1k}^{i2}+\sum\_{j=1}^{J\_{p}}\nu\_{p-1j}z\_{p-1j}^{i3}},\quad\varepsilon\_{p}\text{ is unrestricted in sign}. |  | (1) |

The DEA formulations for each sub-stage corresponding to Equation ([1](https://arxiv.org/html/2511.02608v1#S2.E1 "In 2.1 The three-stage network DEA-Malmquist model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model")) are presented below:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | θ1\displaystyle\theta\_{1} | =u11​z11i​1+(η11​z11i​2+η12​z12i​2)+ε1ν01​z01i+ν02​z02i+ν03​z03i,ε1​ is unrestricted in sign,\displaystyle=\frac{u\_{11}z\_{11}^{i1}+\left(\eta\_{11}z\_{11}^{i2}+\eta\_{12}z\_{12}^{i2}\right)+\varepsilon\_{1}}{\nu\_{01}z\_{01}^{i}+\nu\_{02}z\_{02}^{i}+\nu\_{03}z\_{03}^{i}},\quad\varepsilon\_{1}\text{ is unrestricted in sign}, |  | (2a) |
|  | θ2\displaystyle\theta\_{2} | =u21​z21i​1+(η21​z21i​2+η22​z22i​2)+ε2(η11​z11i​2+η12​z12i​2)+ν11​z11i​3,ε2​ is unrestricted in sign,\displaystyle=\frac{u\_{21}z\_{21}^{i1}+\left(\eta\_{21}z\_{21}^{i2}+\eta\_{22}z\_{22}^{i2}\right)+\varepsilon\_{2}}{\left(\eta\_{11}z\_{11}^{i2}+\eta\_{12}z\_{12}^{i2}\right)+\nu\_{11}z\_{11}^{i3}},\quad\varepsilon\_{2}\text{ is unrestricted in sign}, |  | (2b) |
|  | θ3\displaystyle\theta\_{3} | =u31​z31i​1+u32​z32i​1+u33​z33i​1+ε3(η21​z21i​2+η22​z22i​2)+ν21​z21i​3,ε3​ is unrestricted in sign,\displaystyle=\frac{u\_{31}z\_{31}^{i1}+u\_{32}z\_{32}^{i1}+u\_{33}z\_{33}^{i1}+\varepsilon\_{3}}{\left(\eta\_{21}z\_{21}^{i2}+\eta\_{22}z\_{22}^{i2}\right)+\nu\_{21}z\_{21}^{i3}},\quad\varepsilon\_{3}\text{ is unrestricted in sign}, |  | (2c) |

where z0​jiz\_{0j}^{i} are the only inputs to first stage.

The overall performance t​h​e​t​atheta is computed as a weighted sum of the stage-specific efficiency scores, subject to a unit-sum constraint on the weights:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ=w1​θ1+w2​θ2+w3​θ3,w1+w2+w3=1.\theta=w\_{1}\theta\_{1}+w\_{2}\theta\_{2}+w\_{3}\theta\_{3},\quad w\_{1}+w\_{2}+w\_{3}=1. |  | (3) |

We formulate a linear programming model to evaluate the overall efficiency across the three stages. Equation ([4a](https://arxiv.org/html/2511.02608v1#S2.E4.1 "In 4 ‣ 2.1 The three-stage network DEA-Malmquist model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model")) maximizes the weighted sum of outputs and intermediate products across all stages. Equation ([4b](https://arxiv.org/html/2511.02608v1#S2.E4.2 "In 4 ‣ 2.1 The three-stage network DEA-Malmquist model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model")) imposes a normalization condition, and equations ([4c](https://arxiv.org/html/2511.02608v1#S2.E4.3 "In 4 ‣ 2.1 The three-stage network DEA-Malmquist model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"))–([4e](https://arxiv.org/html/2511.02608v1#S2.E4.5 "In 4 ‣ 2.1 The three-stage network DEA-Malmquist model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model")) give stage-specific feasibility constraints.
Equations ([4f](https://arxiv.org/html/2511.02608v1#S2.E4.6 "In 4 ‣ 2.1 The three-stage network DEA-Malmquist model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"))–([4i](https://arxiv.org/html/2511.02608v1#S2.E4.9 "In 4 ‣ 2.1 The three-stage network DEA-Malmquist model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model")) are domain constraints

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | max\displaystyle\max\quad | ∑p=1P(∑r=1Rpup​r​zp​ro​1+∑k=1Spηp​k​zp​ko​2+εp)\displaystyle\sum\_{p=1}^{P}\Big(\sum\_{r=1}^{R\_{p}}u\_{pr}z\_{pr}^{o1}+\sum\_{k=1}^{S\_{p}}\eta\_{pk}z\_{pk}^{o2}+\varepsilon\_{p}\Big) |  | (4a) |
|  | s.t. | ν01​z01o+ν02​z02o+ν03​z03o+η11​z11o​2+η12​z12o​2+ν11​z11o​3+η21​z21o​2+η22​z22o​2+ν21​z21o​3=1\displaystyle\nu\_{01}z\_{01}^{o}+\nu\_{02}z\_{02}^{o}+\nu\_{03}z\_{03}^{o}+\eta\_{11}z\_{11}^{o2}+\eta\_{12}z\_{12}^{o2}+\nu\_{11}z\_{11}^{o3}+\eta\_{21}z\_{21}^{o2}+\eta\_{22}z\_{22}^{o2}+\nu\_{21}z\_{21}^{o3}=1 |  | (4b) |
|  |  | u11​z11i​1+η11​z11i​2+η12​z12i​2+ε1≤ν01​z01i+ν02​z02i+ν03​z03i,∀i∈I\displaystyle u\_{11}z\_{11}^{i1}+\eta\_{11}z\_{11}^{i2}+\eta\_{12}z\_{12}^{i2}+\varepsilon\_{1}\leq\nu\_{01}z\_{01}^{i}+\nu\_{02}z\_{02}^{i}+\nu\_{03}z\_{03}^{i},\quad\forall i\in I |  | (4c) |
|  |  | u21​z21i​1+η21​z21i​2+η22​z22i​2+ε2≤η11​z11i​2+η12​z12i​2+ν11​z11i​3,∀i∈I\displaystyle u\_{21}z\_{21}^{i1}+\eta\_{21}z\_{21}^{i2}+\eta\_{22}z\_{22}^{i2}+\varepsilon\_{2}\leq\eta\_{11}z\_{11}^{i2}+\eta\_{12}z\_{12}^{i2}+\nu\_{11}z\_{11}^{i3},\quad\forall i\in I |  | (4d) |
|  |  | u31​z31i​1+u32​z32i​1+u33​z33i​1+ε3≤η21​z21i​2+η22​z22i​2+ν21​z21i​3,∀i∈I\displaystyle u\_{31}z\_{31}^{i1}+u\_{32}z\_{32}^{i1}+u\_{33}z\_{33}^{i1}+\varepsilon\_{3}\leq\eta\_{21}z\_{21}^{i2}+\eta\_{22}z\_{22}^{i2}+\nu\_{21}z\_{21}^{i3},\quad\forall i\in I |  | (4e) |
|  |  | u11,u21,u31,u32,u33>0\displaystyle u\_{11},u\_{21},u\_{31},u\_{32},u\_{33}>0 |  | (4f) |
|  |  | η11,η12,η21,η22>0\displaystyle\eta\_{11},\eta\_{12},\eta\_{21},\eta\_{22}>0 |  | (4g) |
|  |  | ν01,ν02,ν03,ν11,ν21>0\displaystyle\nu\_{01},\nu\_{02},\nu\_{03},\nu\_{11},\nu\_{21}>0 |  | (4h) |
|  |  | ε1,ε2,ε3​ are unrestricted in sign\displaystyle\varepsilon\_{1},\varepsilon\_{2},\varepsilon\_{3}\text{ are unrestricted in sign} |  | (4i) |

Traditional DEA models suffer from the inherent limitation of being static and failing to capture intertemporal performance dynamics (Färe et al.,, [1994](https://arxiv.org/html/2511.02608v1#bib.bib22)). Thus, we incorporate the MI, allowing us to track how bank performance evolves over time. The MI is widely applied to measure the changes in productivity of banks (Caves et al.,, [1982](https://arxiv.org/html/2511.02608v1#bib.bib15)). Studies include analyses of credit banks in Japan (Barros et al.,, [2009](https://arxiv.org/html/2511.02608v1#bib.bib8)), and Bansal et al., ([2022](https://arxiv.org/html/2511.02608v1#bib.bib7)) use a dynamic network DEA-based Malmquist–Luenberger index to measure the productivity changes of Indian banks. The MI measures efficiency changes between two time periods by calculating the ratio of the distances of each data point to a common technology frontier (Casu et al.,, [2004](https://arxiv.org/html/2511.02608v1#bib.bib14)). The overall MI is defined for periods t∈Tt\in T, where T={1,2,…,|T|−1}T=\{1,2,\dots,|T|-1\}, as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | M​It,t+1=θt+1tθtt⋅θt+1t+1θtt+1.MI\_{t,t+1}=\sqrt{\frac{\theta^{t}\_{t+1}}{\theta^{t}\_{t}}\cdot\frac{\theta^{t+1}\_{t+1}}{\theta^{t+1}\_{t}}}. |  | (5) |

Let θt+1t\theta^{t}\_{t+1} denote the efficiency of D​M​UiDMU\_{i} at period t+1t+1 evaluated under the technology of period tt, and the other θ\theta terms in the formula are interpreted similarly.

We use MI to analyze the changes in FS of Chinese commercial banks. Changes in FS can be assessed by an output-oriented or input-oriented approach. The former way measures how the actual output compares to the maximum possible output achievable with the same inputs and technology. On the contrary, the latter one measures productivity changes when the same output is produced with fewer inputs under a given technology. According to Jaffry et al., ([2007](https://arxiv.org/html/2511.02608v1#bib.bib31)), an output-oriented model is more suitable for developing countries. Therefore, we adopt an output-oriented approach. In the following, Equation ([6](https://arxiv.org/html/2511.02608v1#S2.E6 "In 2.1 The three-stage network DEA-Malmquist model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model")) for each production stage p∈Pp\in P is used:

|  |  |  |  |
| --- | --- | --- | --- |
|  | M​It,t+1p=θpt​(t+1)θpt​(t)⋅θpt+1​(t+1)θpt+1​(t),MI\_{t,t+1}^{p}=\sqrt{\frac{\theta\_{p}^{t}(t+1)}{\theta\_{p}^{t}(t)}\cdot\frac{\theta\_{p}^{t+1}(t+1)}{\theta\_{p}^{t+1}(t)}}, |  | (6) |

where θpt​(t+1)\theta\_{p}^{t}(t+1) denotes the efficiency of D​M​UiDMU\_{i} at stage pp and period t+1t+1, evaluated under the technology of period tt, and the other θ\theta terms in the formula are interpreted similarly.

Accordingly, an MI value greater than one indicates a positive trend in FS, a value equal to one indicates no change, and a value less than one indicates a decline relative to the prior period.
The overall measure of FS can be decomposed into technical change (TC) and efficiency change (EC).
The TC reflects improvements in technology and shifts in the production frontier, and the EC captures the catching-up effect, indicating whether banks move closer to or farther from the best-practice frontier. TC and EC are computed as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | M​It,t+1=θt+1t+1θtt⏟Efficiency Change (EC)×θt+1tθt+1t+1⋅θttθtt+1⏟Technical Change (TC).\displaystyle MI\_{t,t+1}=\underbrace{\frac{\theta^{t+1}\_{t+1}}{\theta^{t}\_{t}}\vphantom{\sqrt{\frac{\theta^{t}\_{t+1}}{\theta^{t+1}\_{t+1}}\cdot\frac{\theta^{t}\_{t}}{\theta^{t+1}\_{t}}}}}\_{\text{Efficiency Change (EC)}}\;\times\;\underbrace{\sqrt{\frac{\theta^{t}\_{t+1}}{\theta^{t+1}\_{t+1}}\cdot\frac{\theta^{t}\_{t}}{\theta^{t+1}\_{t}}}}\_{\text{Technical Change (TC)}}. |  | (7) |

In empirical studies of the banking sector, researchers often employ TC and EC. For instance, Portela and Thanassoulis, ([2010](https://arxiv.org/html/2511.02608v1#bib.bib45)) evaluate productivity changes in Portuguese bank branches across different periods and branches by TC and EC. Assaf et al., ([2013](https://arxiv.org/html/2511.02608v1#bib.bib4)) compare TC and EC across different types of banks in Turkey. Given the above studies, we also adopt this approach as part of our robustness tests in Section [3.2](https://arxiv.org/html/2511.02608v1#S3.SS2 "3.2 Robustness tests ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model").

### 2.2 Two-way fixed effects model

To examine the relationship between FS and FinTech, we run a two-way fixed effects regression using panel data. Reviewing existing literature (Baltagi,, [2008](https://arxiv.org/html/2511.02608v1#bib.bib6); Wooldridge,, [2010](https://arxiv.org/html/2511.02608v1#bib.bib61)), we find that unobserved heterogeneity across units and periods may bias estimation results. The two-way fixed effects model mitigates this issue by controlling for both individual and time effects. Let ii and tt denote the evaluated commercial bank and year, respectively.
The dependent variable is F​S​IFSI (FS index), which represents the FS of commercial banks. To this end, the regression model is specified as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​S​Ii,t=β0+β1​F​T​Ii,t+∑c=23βc​Mc,t+∑c=410βc​Xc,i,t+δi+μt+ei,t,∀i∈I,∀t∈T.FSI\_{i,t}=\beta\_{0}+\beta\_{1}FTI\_{i,t}+\sum\_{c=2}^{3}\beta\_{c}\,M\_{c,t}+\sum\_{c=4}^{10}\beta\_{c}\,X\_{c,i,t}+\delta\_{i}+\mu\_{t}+e\_{i,t},\quad\forall i\in I,\forall t\in T. |  | (8) |

In Equation ([8](https://arxiv.org/html/2511.02608v1#S2.E8 "In 2.2 Two-way fixed effects model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model")), the explanatory variable is F​T​IFTI (FinTech index). The set of control variables consists of two parts: macroeconomic variables and bank-level variables. The macroeconomic variables are represented by Mc,tM\_{c,t}, and the bank-level variables by Xc,i,tX\_{c,i,t}. The subscript cc indexes different control variables within each category, while ei,te\_{i,t} denotes the stochastic error term. Moreover, δi\delta\_{i} and μt\mu\_{t} denote the individual (bank-specific) and time fixed effects, respectively. The sign and significance of β1\beta\_{1} are used to examine the relationship between FinTech and the FS of commercial banks,
and β0\beta\_{0} is the constant term.
Standard errors are clustered at the individual level to address within-group correlation and to avoid underestimating standard errors.

We primarily evaluate the FS of commercial banks and analyze the impact of FinTech thereon. The dependent variable F​S​IFSI is derived from the three-stage network DEA-Malmquist model. We use the Peking University Digital Financial Inclusion Index compiled by Guo et al., ([2020](https://arxiv.org/html/2511.02608v1#bib.bib26)) to represent FinTech (Lee et al.,, [2023](https://arxiv.org/html/2511.02608v1#bib.bib35); Hu et al.,, [2024](https://arxiv.org/html/2511.02608v1#bib.bib30)). Notably, this index reflects the extent of digital delivery and accessibility of financial services across regions, aligning with the core dimensions of technology-driven financial development. We standardize the index by dividing its original values by 100 to control for scale differences and ensure regional comparability. The resulting standardized index is the core explanatory variable (F​T​IFTI).

The empirical analysis and robustness checks incorporate a set of control variables consistent with prior studies (Cheng and Qu,, [2020](https://arxiv.org/html/2511.02608v1#bib.bib17); [Wang et al., 2021b,](https://arxiv.org/html/2511.02608v1#bib.bib58) ; Lee et al.,, [2023](https://arxiv.org/html/2511.02608v1#bib.bib35)). At the macroeconomic level, the prefecture-level GDP growth rate (G​D​PgGDP\_{g}) and the financial development level (F​D​LFDL) are included. Since banks operate in different regions with varying economic and capital market conditions, we include these variables as controls to mitigate potential bias caused by regional differences. At the individual bank level, variables such as loan-to-deposit ratio (L​D​RLDR), non-interest income ratio (N​I​I​RNIIR), return on assets (R​O​AROA), debt-to-asset ratio (D​A​RDAR), total assets (T​A​STAS), operating expenses (O​E​XOEX), and capital adequacy ratio (C​A​RCAR) are included. These variables account for differences in profitability, bank size, risk management, and other related aspects. Controlling these factors reduces bias due to individual bank differences. Definitions and calculation methods for these variables are presented in Table [2](https://arxiv.org/html/2511.02608v1#S2.T2 "Table 2 ‣ 2.2 Two-way fixed effects model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model").

Table 2: Variables of the two-way fixed effects model

| Category | Variable Name | Abbreviation | Definition |
| --- | --- | --- | --- |
| Dependent Variable | Financial Sustainability Index | F​S​IFSI | Composite financial indicators calculated by a three-stage network DEA-Malmquist model |
| Explanatory Variable | FinTech Index | F​T​IFTI | The Peking University Digital Financial Inclusion Index divided by 100 |
| Control Variables | GDP Growth Rate (the prefecture-level) | G​D​PgGDP\_{g} | (Current GDP - Previous GDP) / Previous GDP |
|  | Financial Development Level | F​D​LFDL | Ratio of total deposits and loans to local GDP |
|  | Loan-to-Deposit Ratio | L​D​RLDR | Total loans / Total deposits |
|  | Non-interest Income Ratio | N​I​I​RNIIR | Non-interest income / Operating income |
|  | Return on Assets | R​O​AROA | Net profit / Total assets |
|  | Debt-to-Asset Ratio | D​A​RDAR | Total liabilities / Total assets |
|  | Total Assets | T​A​STAS | Natural logarithm of total assets at year-end |
|  | Operating Expenses | O​E​XOEX | Natural logarithm of operating expenses at year-end |
|  | Capital Adequacy Ratio | C​A​RCAR | Eligible capital / Risk-weighted assets |

## 3 Empirical analysis

This section presents an empirical analysis to identify the impact, underlying mechanisms, and heterogeneous effects of FinTech on FS. Firstly, the values of FS are computed based on the methodology in Section [2](https://arxiv.org/html/2511.02608v1#S2 "2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"). We also conduct descriptive statistics for relevant variables and run a fixed-effects panel regression to examine the impact of FinTech development. Secondly, a series of robustness checks is performed to verify the reliability of the baseline regression results. Thirdly, stage-specific MIs are introduced as channel variables to investigate the transmission mechanisms, where FinTech affects bank financial performance across different operational stages. Finally, heterogeneity analyses are conducted based on bank listing status and patent ownership to explore differential impacts across bank types.

### 3.1 Main results

FS estimation results: Table [3](https://arxiv.org/html/2511.02608v1#S3.T3 "Table 3 ‣ 3.1 Main results ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model") reports the annual averages of FS for 104 banks from 2015 to 2023. The mean MI exceeds one in most years, indicating an overall upward trend in FS of the banking sector. The highest MI value is 1.3287 in 2020, suggesting that the financial capability of banks demonstrated strong resilience during the initial period of the COVID-19 pandemic, in line with evidence of policy-supported stability in Chinese banks (Wu and Olson,, [2020](https://arxiv.org/html/2511.02608v1#bib.bib64)). In contrast, the MI falls sharply to 0.7530 in 2021, the lowest level during the sample period. This deterioration may be associated with pressures on FS in the post-pandemic period. These pressures may stem from heightened asset quality risks, tighter regulatory oversight, and shifts in credit allocation patterns, which are supported by the findings of Elnahass et al., ([2021](https://arxiv.org/html/2511.02608v1#bib.bib21)) and Yao and Fan, ([2025](https://arxiv.org/html/2511.02608v1#bib.bib66)). By 2023, the MI returns to 1.0016, a near-neutral level, showing that FS in the banking sector has little change compared to the previous year.

Table 3: Annual average MI for 104 banks from 2015 to 2023

|  |  |  |  |
| --- | --- | --- | --- |
| Year | MI | TC | EC |
| 2015 | 1.1311 | 1.0847 | 1.0572 |
| 2016 | 0.8056 | 0.8242 | 0.9567 |
| 2017 | 1.1678 | 1.1693 | 1.0109 |
| 2018 | 1.0798 | 1.0561 | 1.0251 |
| 2019 | 1.0760 | 1.0872 | 0.9973 |
| 2020 | 1.3287 | 1.3368 | 1.0066 |
| 2021 | 0.7530 | 0.6963 | 1.0930 |
| 2022 | 1.0677 | 1.0531 | 1.0183 |
| 2023 | 1.0016 | 1.0250 | 0.9867 |
| Notes: This table reports the annual average values of the MI and its two components: TC and EC, over the period 2015–2023. An MI value greater than one indicates an improvement in FS performance relative to the previous year, while a value less than one indicates a decline. | | | |

Descriptive statistical analysis: The descriptive statistics of the variables are reported in Table [4](https://arxiv.org/html/2511.02608v1#S3.T4 "Table 4 ‣ 3.1 Main results ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"). Specifically, the mean of F​S​IFSI is 1.0457, with a standard deviation of 0.2781, indicating that the FS of Chinese commercial banks in the sample remains relatively stable. For F​T​IFTI, the average value is 2.7769 with a standard deviation of 0.4801, suggesting some variation in the development of FinTech across regions. Regarding the control variables, N​I​I​RNIIR displays considerable variation across banks, while C​A​RCAR and D​A​RDAR are relatively stable, likely reflecting regulatory consistency. It is worth noting that the minimum value of G​D​PgGDP\_{g} is −5.6-5.6, which occurred in Shenyang in 2016, highlighting the existence of substantial regional economic disparities and underscoring the necessity of controlling for such heterogeneity in subsequent analyses. Given the focus of this study, i.e., examining how FinTech affects the FS of commercial banks, the detailed statistical characteristics of control variables are not further elaborated here.

Table 4: Descriptive statistics of all variables

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Variable | Sample size | Mean | Std. Dev. | Min | Max |
| F​S​IFSI | 936 | 1.0457 | 0.2781 | 0.5464 | 1.6356 |
| F​T​IFTI | 936 | 2.7769 | 0.4801 | 1.5221 | 3.7322 |
| G​D​PgGDP\_{g} | 935 | 6.2198 | 2.5265 | -5.6000 | 12.5000 |
| F​D​LFDL | 927 | 4.2641 | 1.5934 | 1.4265 | 7.9760 |
| L​D​RLDR | 935 | 0.7492 | 0.1215 | 0.5263 | 0.9809 |
| N​I​I​RNIIR | 936 | 21.3664 | 12.5907 | 3.6860 | 51.5334 |
| R​O​AROA | 936 | 0.6973 | 0.2270 | 0.2532 | 1.0747 |
| D​A​RDAR | 936 | 0.9255 | 0.0135 | 0.7824 | 0.9629 |
| T​A​STAS | 936 | 26.8395 | 1.5258 | 24.0439 | 31.4309 |
| O​E​XOEX | 936 | 22.6281 | 1.5297 | 19.6937 | 26.9756 |
| C​A​RCAR | 936 | 13.4558 | 1.9846 | 2.3700 | 33.8600 |
| Notes: This table shows the explanation and descriptive statistics of all variables. Differences in sample size are due to missing values in control variables. | | | | | |

Baseline regression: According to Equation ([8](https://arxiv.org/html/2511.02608v1#S2.E8 "In 2.2 Two-way fixed effects model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model")), we use panel data to test the relation between FinTech and FS, and Table [5](https://arxiv.org/html/2511.02608v1#S3.T5 "Table 5 ‣ 3.1 Main results ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model") presents results of a two-way fixed effects model. Columns (1) and (2) report results without additional control variables, whereas Columns (3) and (4) include them. Moreover, we cluster standard errors at the bank level in all estimations. Columns (1) and (3) do not include individual fixed effects, while Columns (2) and (4) control for both individual and time fixed effects.

Several important observations can be drawn. First, the coefficients of F​T​IFTI on F​S​IFSI are negative and statistically significant across all specifications, regardless of whether control variables or fixed effects are included. This relationship remains stable even after accounting for potential bank-level and time-varying confounders. Further, in Column (4), which incorporates individual and time fixed effects as well as additional controls, the coefficient on F​T​IFTI is -0.540, and statistically significant at the 1% level. This result implies that a one-unit increase in FinTech development is associated with a 0.54-point decline in F​S​IFSI, i.e., a non-trivial magnitude relative to its standard deviation. Economically, FinTech may weaken FS of commercial banks by intensifying disintermediation and shifting customers toward technology-based financial services. This potential mechanism will be empirically examined in the following analysis. Finally, among the control variables, R​O​AROA and O​E​XOEX are positively and significantly associated with F​S​IFSI, confirming the importance of profitability and operational investment for maintaining stability. By contrast, T​A​STAS exhibits a significantly negative coefficient, suggesting that excessive asset expansion can undermine financial stability through resource misallocation and heightened financial risk. The primary finding remains robust, as the negative impact of F​T​IFTI persists across all model specifications.

Table 5: Baseline regression

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) |
|  | FinTech Only | | Full Controls | |
|  | F​S​IFSI | | F​S​IFSI | |
| F​T​IFTI | -0.042∗∗ | -0.530∗∗∗ | -0.062∗∗∗ | -0.540∗∗∗ |
|  | (0.017) | (0.189) | (0.023) | (0.203) |
| G​D​PgGDP\_{g} |  |  | -0.036∗∗∗ | 0.005 |
|  |  |  | (0.004) | (0.007) |
| F​D​LFDL |  |  | -0.002 | -0.004 |
|  |  |  | (0.006) | (0.028) |
| L​D​RLDR |  |  | 0.063 | 0.167 |
|  |  |  | (0.083) | (0.129) |
| N​I​I​RNIIR |  |  | -0.000 | -0.001 |
|  |  |  | (0.001) | (0.001) |
| R​O​AROA |  |  | 0.184∗∗∗ | 0.166∗∗ |
|  |  |  | (0.050) | (0.075) |
| D​A​RDAR |  |  | 1.579 | 2.783∗ |
|  |  |  | (0.982) | (1.562) |
| T​A​STAS |  |  | -0.151∗∗∗ | -0.254∗∗ |
|  |  |  | (0.039) | (0.108) |
| O​E​XOEX |  |  | 0.130∗∗∗ | 0.196∗∗∗ |
|  |  |  | (0.036) | (0.063) |
| C​A​RCAR |  |  | 0.012∗∗ | 0.010 |
|  |  |  | (0.006) | (0.007) |
| Bank FE | NO | YES | NO | YES |
| Year FE | YES | YES | NO | YES |
| Constant term | 1.163∗∗∗ | 2.517∗∗∗ | 0.766 | 1.996 |
|  | (0.048) | (0.525) | (0.866) | (2.471) |
| Observations | 936 | 936 | 925 | 925 |
| R2R^{2} | 0.06 | 0.42 | 0.10 | 0.45 |
| Notes: The dependent variable is the F​S​IFSI rating from the three-stage network DEA-Malmquist model. Columns (1) and (2) report results without control variables, while Columns (3) and (4) include control variables. Differences in sample size are due to missing values in control variables. The main model controls for individual and time fixed effects. Variable definitions are provided in Table [2](https://arxiv.org/html/2511.02608v1#S2.T2 "Table 2 ‣ 2.2 Two-way fixed effects model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"). ∗, ∗∗, and ∗∗∗ indicate statistical significance at the 10%, 5%, and 1% levels, respectively. Standard errors are clustered at the bank level and reported in parentheses. R2R^{2} represents the coefficient of determination. | | | | |
| --- | --- | --- | --- | --- |

### 3.2 Robustness tests

We perform a series of robustness tests to validate the consistency of the main findings. Specifically, we examine whether the results remain robust when using alternative TC and EC measures from Equation ([7](https://arxiv.org/html/2511.02608v1#S2.E7 "In 2.1 The three-stage network DEA-Malmquist model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model")). These measures are components decomposed from the MI applied to F​S​IFSI. Furthermore, we alleviate potential endogeneity issues by implementing an instrumental variable (IV) approach.

IV approach: We include a battery of control variables and apply a two-way fixed effects model, but the estimation is still influenced by unobserved heterogeneity or omitted variables. To mitigate these problems, we adopt a strategy with instrumental variables. Specifically, we implement a two-stage least squares (2SLS) method (Wooldridge,, [2010](https://arxiv.org/html/2511.02608v1#bib.bib61)) and a control function (CF) method (Wooldridge,, [2015](https://arxiv.org/html/2511.02608v1#bib.bib62)) to obtain more consistent estimates.

We introduce two instrumental variables. The first instrumental variable (I​V1IV\_{1}) is the one-period lag of F​T​IFTI. Due to the temporal precedence over bank financial outcomes, I​V1IV\_{1} helps alleviate potential endogeneity bias. The second instrument (I​V2IV\_{2}) is the logarithm of the interaction between the distance to Hangzhou, a recognized FinTech hub, and the average annual Digital Financial Inclusion Index (excluding the city itself). This variable captures the regional spillover effects of FinTech development. To ensure the reliability of the instrumental variables estimation, several diagnostic tests are conducted. The Kleibergen–Paap rk LM and rk Wald F statistics are used to assess underidentification and weak instrument issues, respectively, while the Hansen J test examines instrument validity. As shown in the Column (1) of Table [6](https://arxiv.org/html/2511.02608v1#S3.T6 "Table 6 ‣ 3.2 Robustness tests ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"), both instruments strongly correlate with F​T​IFTI. The Kleibergen-Paap rk LM statistic rejects the null of underidentification (pp <0.01), and the rk Wald F statistic (27.377) exceeds the Stock-Yogo critical value of 19.93, suggesting no weak instrument issue. The Hansen J test also yields an insignificant pp-value (0.1906), confirming the validity of the instruments. Then, let F​T​I^i,t\widehat{FTI}\_{i,t} denote the predicted value from the first-stage regression, and δi\delta\_{i} and μt\mu\_{t} indicate the fixed effects of individual and time, respectively. The instrumental variables include I​V1IV\_{1} and I​V2IV\_{2}. All other control variables are consistent with those used in the baseline regressions. The IV approach is conducted by estimating the following 2SLS method Equations ([9](https://arxiv.org/html/2511.02608v1#S3.E9 "In 3.2 Robustness tests ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model")) and ([10](https://arxiv.org/html/2511.02608v1#S3.E10 "In 3.2 Robustness tests ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model")):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | F​T​Ii,t=ρ0+ρ1​I​V1,i,t+ρ2​I​V2,i,t+∑c=12βc​Mc,t+∑c=39βc​Xc,i,t+δi+μt+ξi,t,\displaystyle FTI\_{i,t}=\rho\_{0}+\rho\_{1}\,IV\_{1,i,t}+\rho\_{2}\,IV\_{2,i,t}+\sum\_{c=1}^{2}\beta\_{c}\,M\_{c,t}+\sum\_{c=3}^{9}\beta\_{c}\,X\_{c,i,t}+\delta\_{i}+\mu\_{t}+\xi\_{i,t}, | ∀i∈I,∀t∈T,\displaystyle\forall i\in I,\forall t\in T, |  | (9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | F​S​Ii,t=β0+β1​F​T​I^i,t+∑c=23βc​Mc,t+∑c=410βc​Xc,i,t+δi+μt+ei,t,\displaystyle FSI\_{i,t}=\beta\_{0}+\beta\_{1}\,\widehat{FTI}\_{i,t}+\sum\_{c=2}^{3}\beta\_{c}\,M\_{c,t}+\sum\_{c=4}^{10}\beta\_{c}\,X\_{c,i,t}+\delta\_{i}+\mu\_{t}+e\_{i,t}, | ∀i∈I,∀t∈T.\displaystyle\forall i\in I,\forall t\in T. |  | (10) |

As reported in the Column (2) of Table [6](https://arxiv.org/html/2511.02608v1#S3.T6 "Table 6 ‣ 3.2 Robustness tests ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"), the estimated coefficient on F​T​IFTI remains significantly negative after controlling for endogeneity. Overall, the results of this analysis are consistent with the main findings, namely that FinTech negatively affects FS.

In addition to 2SLS method, we also adopt the CF method as a complementary strategy to alleviate potential endogeneity. Compared to 2SLS method, the CF method offers greater flexibility when dealing with heteroskedasticity or complex error structures. The CF method is specified in Equations ([11](https://arxiv.org/html/2511.02608v1#S3.E11 "In 3.2 Robustness tests ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"))–([12](https://arxiv.org/html/2511.02608v1#S3.E12 "In 3.2 Robustness tests ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model")). Let ξ^i,t\widehat{\xi}\_{i,t} denote the residuals from the first-stage regression, capturing endogeneity effects, while the remaining variables are consistent with those in the baseline regressions, we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | F​T​Ii,t=ρ0+ρ1​I​V1,i,t+ρ2​I​V2,i,t+∑c=12βc​Mc,t+∑c=39βc​Xc,i,t+δi+μt+ξi,t,\displaystyle FTI\_{i,t}=\rho\_{0}+\rho\_{1}\,IV\_{1,i,t}+\rho\_{2}\,IV\_{2,i,t}+\sum\_{c=1}^{2}\beta\_{c}\,M\_{c,t}+\sum\_{c=3}^{9}\beta\_{c}\,X\_{c,i,t}+\delta\_{i}+\mu\_{t}+\xi\_{i,t}, | ∀i∈I,∀t∈T,\displaystyle\forall i\in I,\forall t\in T, |  | (11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | F​S​Ii,t=β0+β1​F​T​Ii,t+λ​ξ^i,t+∑c=23βc​Mc,t+∑c=410βc​Xc,i,t+δi+μt+ei,t,\displaystyle FSI\_{i,t}=\beta\_{0}+\beta\_{1}\,FTI\_{i,t}+\lambda\,\widehat{\xi}\_{i,t}+\sum\_{c=2}^{3}\beta\_{c}\,M\_{c,t}+\sum\_{c=4}^{10}\beta\_{c}\,X\_{c,i,t}+\delta\_{i}+\mu\_{t}+e\_{i,t}, | ∀i∈I,∀t∈T.\displaystyle\forall i\in I,\forall t\in T. |  | (12) |

We present the results in the Column (3) of Table [6](https://arxiv.org/html/2511.02608v1#S3.T6 "Table 6 ‣ 3.2 Robustness tests ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"). The coefficient on F​T​IFTI remains significantly negative, consistent with the baseline and 2SLS method estimates. Importantly, the residual term from the second stage is statistically significant, which suggests that the original F​T​IFTI variable suffers from endogeneity. This finding suggests that the CF method successfully corrects for this bias. Together, these findings reinforce the robustness of the adverse effect of FinTech development on the FS of commercial banks.

Alternative measure of FS: Given that it is calculated using a three-stage network DEA-Malmquist model, we examine the influence of the internal components of the MI. Specifically, we decompose the MI into two sub-indicators, TC and EC, and replace F​S​IFSI with them in the regression model for robustness checks. These two components reflect technological progress over time and changes in managerial efficiency. Table [3](https://arxiv.org/html/2511.02608v1#S3.T3 "Table 3 ‣ 3.1 Main results ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model") presents the annual means of these two indices. As reported in Columns (4) and (5) of Table [6](https://arxiv.org/html/2511.02608v1#S3.T6 "Table 6 ‣ 3.2 Robustness tests ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"), the signs of the key explanatory variables remain unchanged, despite the statistical significance of some coefficients declining compared to the baseline results. This result suggests that the main findings of this study, namely the negative effect of FinTech on FS of banks, are reasonably robust to alternative specifications.

Table 6: Robustness tests

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | (1) 2SLS & CF 1st | (2) 2SLS 2nd | (3) CF 2nd | (4) TC | (5) EC |
| F​T​IFTI |  | -0.878∗∗ | -0.878∗∗∗ | -0.342∗ | -0.237∗ |
|  |  | (0.405) | (0.304) | (0.181) | (0.124) |
| I​V1IV\_{1} | 0.559∗∗∗ |  |  |  |  |
|  | (0.069) |  |  |  |  |
| I​V2IV\_{2} | -0.117∗∗∗ |  |  |  |  |
|  | (0.034) |  |  |  |  |
| ξ^i,t\widehat{\xi}\_{i,t} |  |  | 0.840∗∗ |  |  |
|  |  |  | (0.374) |  |  |
| G​D​PgGDP\_{g} | 0.002∗ | 0.007 | 0.007 | -0.005 | 0.011∗∗ |
|  | (0.001) | (0.007) | (0.007) | (0.004) | (0.005) |
| F​D​LFDL | -0.001 | -0.013 | -0.013 | 0.006 | -0.006 |
|  | (0.005) | (0.028) | (0.026) | (0.017) | (0.016) |
| L​D​RLDR | -0.057 | 0.145 | 0.145 | -0.003 | 0.203∗∗ |
|  | (0.035) | (0.165) | (0.138) | (0.111) | (0.086) |
| N​I​I​RNIIR | -0.000 | -0.002∗ | -0.002∗ | -0.001 | -0.000 |
|  | (0.000) | (0.001) | (0.001) | (0.001) | (0.001) |
| R​O​AROA | 0.033∗∗ | 0.304∗∗∗ | 0.304∗∗∗ | -0.081 | 0.205∗∗∗ |
|  | (0.013) | (0.082) | (0.072) | (0.052) | (0.053) |
| D​A​RDAR | 0.238 | 2.780∗ | 2.780 | -0.114 | 2.822∗∗∗ |
|  | (0.167) | (1.559) | (1.705) | (1.099) | (0.868) |
| T​A​STAS | 0.004 | -0.289∗∗∗ | -0.289∗∗ | -0.069 | -0.225∗∗∗ |
|  | (0.017) | (0.111) | (0.116) | (0.072) | (0.059) |
| O​E​XOEX | -0.006 | 0.220∗∗∗ | 0.220∗∗∗ | 0.050 | 0.144∗∗∗ |
|  | (0.009) | (0.065) | (0.067) | (0.051) | (0.042) |
| C​A​RCAR | 0.002∗∗ | 0.007 | 0.007 | 0.005 | 0.003 |
|  | (0.001) | (0.007) | (0.007) | (0.006) | (0.005) |
| Observations | 821 | 821 | 821 | 925 | 925 |
| R2R^{2} | 0.99 | 0.45 | 0.49 | 0.57 | 0.17 |

| IV diagnostics for Columns (1)–(3): | |
| --- | --- |
| Kleibergen-Paap rk LM statistic | 112.984 (pp-value = 0.0000) |
| Cragg-Donald Wald F statistic | 205.381 (19.93) |
| Kleibergen-Paap rk Wald F statistic | 27.377 (19.93) |
| Hansen J statistic | 1.713 (pp-value = 0.1906) |

Notes: This table shows the results of robustness tests.
Column (1) reports the first-stage regressions of 2SLS and the CF methods.
The numbers in parentheses after the Cragg–Donald and Kleibergen–Paap rk Wald F statistics indicate
the Stock–Yogo 10% maximal instrumental variables size distortion critical value.
Variable definitions are provided in Table [2](https://arxiv.org/html/2511.02608v1#S2.T2 "Table 2 ‣ 2.2 Two-way fixed effects model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model").
ξ^i,t\widehat{\xi}\_{i,t} denotes the residual term from the first stage of the CF method.
Differences in sample size are due to missing values in control variables and using one-period lagged explanatory variables.
All regressions include individual and time fixed effects.
\*, \*\*, and \*\*\* indicate significance at the 10%, 5%, and 1% levels, respectively. Standard errors are clustered at the bank level and reported in parentheses. R2R^{2} represents the coefficient of determination.

### 3.3 Economic mechanisms

Building on the baseline regression results, which indicate a negative relationship between FinTech and overall FS of banks, we further explore the potential transmission mechanisms. Following the approach of Liang and Renneboog, ([2017](https://arxiv.org/html/2511.02608v1#bib.bib38)), we conduct separate regressions in two steps using the stage-level MIs, corresponding to the deposit (M​IdMI\_{d}), loan (M​IlMI\_{l}), and profitability (M​IpMI\_{p}) stages. These indices serve as the channel through which FinTech influences FS of banks. In the first stage, each channel variable is regressed on F​T​IFTI to obtain the component explained by FinTech. In the second stage, we regress F​S​IFSI on the predicted values of channel variables from the first stage. These predicted values capture the part of FS variation that operates through FinTech-driven channels. Control variables are included in both stages. While this strategy resembles an IV approach in structure, FinTech is not formally used as an instrument for channel variables. The specific two-stage model is formally presented in Equations ([13](https://arxiv.org/html/2511.02608v1#S3.E13 "In 3.3 Economic mechanisms ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model")) and ([14](https://arxiv.org/html/2511.02608v1#S3.E14 "In 3.3 Economic mechanisms ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model")):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | M​Ii,t(ϕ)=α0(ϕ)+α1(ϕ)​F​T​Ii,t+∑c=12βc​Mc,t+∑c=39βc​Xc,i,t+δi+μt+ei,t(ϕ),\displaystyle MI^{(\phi)}\_{i,t}=\alpha\_{0}^{(\phi)}+\alpha\_{1}^{(\phi)}\,FTI\_{i,t}+\sum\_{c=1}^{2}\beta\_{c}\,M\_{c,t}+\sum\_{c=3}^{9}\beta\_{c}\,X\_{c,i,t}+\delta\_{i}+\mu\_{t}+e^{(\phi)}\_{i,t}, | ∀i∈I,∀t∈T,\displaystyle\forall i\in I,\forall t\in T, |  | (13) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | F​S​Ii,t=κ0(ϕ)+κ1(ϕ)​M​I^i,t(ϕ)+∑c=12βc​Mc,t+∑c=39βc​Xc,i,t+δi+μt+ei,t(ϕ,2),\displaystyle FSI\_{i,t}=\kappa\_{0}^{(\phi)}+\kappa\_{1}^{(\phi)}\,\widehat{MI}^{(\phi)}\_{i,t}+\sum\_{c=1}^{2}\beta\_{c}\,M\_{c,t}+\sum\_{c=3}^{9}\beta\_{c}\,X\_{c,i,t}+\delta\_{i}+\mu\_{t}+e\_{i,t}^{(\phi,2)}, | ∀i∈I,∀t∈T,\displaystyle\forall i\in I,\forall t\in T, |  | (14) |

where ϕ∈{d,l,p}\phi\in\{d,l,p\}666The superscript ϕ∈d,l,p\phi\in{d,l,p} denotes the three sub-stages of the FS of banks: the deposit (dd), the loan (ll), and the profitability (pp) stages. Each ei,t(ϕ)e^{(\phi)}\_{i,t} represents the regression residual corresponding to the respective stage.
.

The dynamic patterns of banking efficiency across different operational stages are illustrated in Table [7](https://arxiv.org/html/2511.02608v1#S3.T7 "Table 7 ‣ 3.3 Economic mechanisms ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"), which reports the annual averages of MIs for each stage from 2015 to 2023. As shown, the indices in most years exceed one across all stages, suggesting a generally positive performance in FS across stages. In 2020, M​IdMI\_{d} peaked at 1.7710, reflecting a sharp improvement in deposit efficiency during the early period of the COVID-19 pandemic. In contrast, M​IpMI\_{p} dropped to 0.7104 in 2021, which is the lowest among all years, indicating a substantial decline in the earning capacity of banks. This deterioration is likely attributable to mounting pressure from non-performing loans, narrowing interest margins, and a tightening regulatory environment.

Table 7: Annual average MIs for each stage from 2015 to 2023

| Year | Deposit stage | Loan stage | Profitability stage |
| --- | --- | --- | --- |
|  | M​IdMI\_{d} | M​IlMI\_{l} | M​IpMI\_{p} |
| 2015 | 1.1972 | 1.1700 | 1.1643 |
| 2016 | 0.7285 | 0.8477 | 0.9187 |
| 2017 | 1.4727 | 1.0662 | 1.1391 |
| 2018 | 1.0590 | 1.0821 | 1.1605 |
| 2019 | 1.0331 | 1.0787 | 1.1783 |
| 2020 | 1.7710 | 1.1711 | 1.2709 |
| 2021 | 0.7473 | 0.8932 | 0.7104 |
| 2022 | 1.0021 | 1.0398 | 1.2527 |
| 2023 | 0.8125 | 0.9850 | 1.3863 |

Table [8](https://arxiv.org/html/2511.02608v1#S3.T8 "Table 8 ‣ 3.3 Economic mechanisms ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model") reports the results of the two-stage analysis. In the first stage, we find that FinTech development is negatively associated with financial efficiency in the loan and profitability stages. It implies that FinTech companies have eroded the market share of banks in these key areas by offering lower-cost and more efficient financial services. As a result, they exert substantial competitive pressure on traditional banking operations. In the second stage, we regress F​S​IFSI on the FinTech-predicted MIs from the deposit, loan, and profitability stages. The results indicate that efficiency in all three stages is positively associated with FS. These findings suggest that the negative impact of FinTech on the financial efficiency of core banking operations may partly contribute to the overall adverse effect. We note, however, that this analysis is not definitive, as FinTech probably also operates through alternative channels or mechanisms that negatively affect FS of banks.

Table 8: Mechanism analysis

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) | (5) | (6) |
|  | M​IdMI\_{d} | F​S​IFSI | M​IlMI\_{l} | F​S​IFSI | M​IpMI\_{p} | F​S​IFSI |
| F​T​IFTI | -0.324 |  | -0.404∗ |  | -0.690∗ |  |
|  | (0.305) |  | (0.209) |  | (0.358) |  |
| M​Id^\widehat{MI\_{d}} |  | 1.666∗∗∗ |  |  |  |  |
|  |  | (0.628) |  |  |  |  |
| M​Il^\widehat{MI\_{l}} |  |  |  | 1.000∗∗∗ |  |  |
|  |  |  |  | (0.377) |  |  |
| M​Ip^\widehat{MI\_{p}} |  |  |  |  |  | 0.782∗∗∗ |
|  |  |  |  |  |  | (0.295) |
| G​D​PgGDP\_{g} | 0.010 | -0.011 | 0.013∗∗ | 0.000 | -0.007 | 0.011 |
|  | (0.010) | (0.010) | (0.006) | (0.008) | (0.013) | (0.007) |
| F​D​LFDL | 0.013 | -0.026 | 0.013 | -0.000 | 0.012 | -0.014 |
|  | (0.038) | (0.031) | (0.021) | (0.027) | (0.056) | (0.029) |
| L​D​RLDR | 0.302 | -0.336 | -0.155 | 0.000 | 0.301 | -0.069 |
|  | (0.256) | (0.242) | (0.148) | (0.150) | (0.226) | (0.165) |
| N​I​I​RNIIR | -0.002∗∗ | 0.003 | -0.001 | -0.000 | -0.001 | -0.001 |
|  | (0.001) | (0.002) | (0.001) | (0.001) | (0.002) | (0.001) |
| R​O​AROA | 0.145 | -0.075 | 0.163∗∗ | 0.000 | 0.168 | 0.034 |
|  | (0.118) | (0.117) | (0.081) | (0.097) | (0.135) | (0.089) |
| D​A​RDAR | 1.045 | 1.041 | 1.477 | 0.000 | 4.688∗ | -0.884 |
|  | (2.198) | (1.786) | (1.278) | (2.013) | (2.600) | (2.241) |
| T​A​STAS | -0.185 | 0.054 | -0.193∗∗ | -0.000 | -0.559∗∗∗ | 0.183 |
|  | (0.137) | (0.172) | (0.082) | (0.156) | (0.198) | (0.212) |
| O​E​XOEX | 0.098 | 0.033 | 0.169∗∗∗ | 0.000 | 0.411∗∗∗ | -0.125 |
|  | (0.110) | (0.091) | (0.062) | (0.100) | (0.112) | (0.140) |
| C​A​RCAR | 0.006 | -0.000 | 0.009 | 0.000 | 0.013 | -0.000 |
|  | (0.011) | (0.008) | (0.007) | (0.008) | (0.015) | (0.008) |
| Constant term | 3.288 | -3.483 | 1.898 | -0.000 | 3.905 | -1.058 |
|  | (3.186) | (2.952) | (2.295) | (2.464) | (4.851) | (2.551) |
| Bank FE | YES | YES | YES | YES | YES | YES |
| Year FE | YES | YES | YES | YES | YES | YES |
| Observations | 925 | 925 | 925 | 925 | 925 | 925 |
| R2R^{2} | 0.49 | 0.45 | 0.27 | 0.45 | 0.28 | 0.45 |
| Notes: This table reports results on potential mechanisms (“channels”) behind the link between FinTech and FS. The channel variables include the MIs of the deposit, loan, and profitability stages, forming the F​S​IFSI jointly. Variable definitions are provided in Table [2](https://arxiv.org/html/2511.02608v1#S2.T2 "Table 2 ‣ 2.2 Two-way fixed effects model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"). Each set of tests contains two stages of regression. In the first stage, F​T​IFTI is regressed on the channel variables to generate its predicted values. In the second stage, F​S​IFSI is regressed on the channel variable “predicted” from the first-stage regression. M​Id^\widehat{MI\_{d}}, M​Il^\widehat{MI\_{l}}, and M​Ip^\widehat{MI\_{p}} denote the stage-level predicted MIs from Equation ([13](https://arxiv.org/html/2511.02608v1#S3.E13 "In 3.3 Economic mechanisms ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model")). ∗, ∗∗, and ∗∗∗ indicate statistical significance at the 10%, 5%, and 1%levels, respectively. Standard errors are clustered at the bank level and reported in parentheses. R2R^{2} represents the coefficient of determination. | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |

### 3.4 Heterogeneity analysis

Based on the baseline regression, we further classify the 104 bank samples according to innovation level and marketization degree. This classification allows us to investigate how FinTech influences FS of different types of commercial banks.

Firstly, under a well-established market competition mechanism, banks face the pressure to survive the fittest. This pressure drives them to open new markets, launch new products, and invest in new technologies, thereby achieving patent-driven innovation (Bos et al.,, [2013](https://arxiv.org/html/2511.02608v1#bib.bib12)). Against this background, the innovation level of banks is commonly measured by the number of patents they hold. Previous studies have found that banks achieved cost reduction and efficiency improvement by establishing technological barriers. Meanwhile, banks strengthen their market position through differentiated services (Buchak et al.,, [2018](https://arxiv.org/html/2511.02608v1#bib.bib13)). Based on these insights, banks with more patents will likely experience less significant impacts from FinTech on FS of banks.

Guided by the above analysis, we use whether the cumulative patent count of a bank exceeds the cross-sectional median as the basis for subsample grouping777The patent data is sourced from the China National Intellectual Property Administration.. The regression results are shown in Columns (1) and (2) of Table [9](https://arxiv.org/html/2511.02608v1#S3.T9 "Table 9 ‣ 3.4 Heterogeneity analysis ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"). These results display that FinTech significantly and negatively impacts FS for banks with cumulative patent counts below the median. In contrast, the regression coefficient is insignificant for those above the median. This subsample analysis supports our earlier reasoning, i.e., the adverse effect of FinTech on FS is primarily concentrated among banks with fewer patents.

Secondly, considering the degree of marketization, we classify the banks into two groups: listed and non-listed. We do so because the listed banks typically have more diversified financing options, healthier capital positions, and more formalized risk management practices. Non-listed banks often operate under softer market constraints, relying heavily on private funding sources and facing limited external oversight. These structural advantages facilitate greater investment in technological development and help listed banks realize economies of scale (Beccalli et al.,, [2015](https://arxiv.org/html/2511.02608v1#bib.bib9)). Consequently, listed banks are likely to experience only a minor impact of FinTech development on their FS.

We estimate separate regressions for listed and non-listed banks to test this hypothesis. The results, reported in Columns (3) and (4) of Table [9](https://arxiv.org/html/2511.02608v1#S3.T9 "Table 9 ‣ 3.4 Heterogeneity analysis ‣ 3 Empirical analysis ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"), reveal a notable difference in how FinTech development affects the two groups. For listed banks, the estimated effect is not statistically significant, which suggests a certain degree of resilience to the disruptions brought by FinTech. Conversely, we find a significant negative relationship between FinTech development and the FS of non-listed banks. This difference reflects that banks vary in their ability to handle external shocks. Listed banks have more capital, funding sources, and transparent governance, enabling them to better handle challenges from technological changes. Non-listed banks, in comparison, often operate with thinner buffers and less institutional support, leaving them more vulnerable to the pressure of FinTech advancement.

Table 9: Heterogeneity analysis

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) |
|  | HighInnov | LowInnov | Listed | NonListed |
|  | F​S​IFSI | F​S​IFSI | F​S​IFSI | F​S​IFSI |
| F​T​IFTI | -0.197 | -0.644∗∗ | -0.509 | -0.506∗∗ |
|  | (0.467) | (0.261) | (0.393) | (0.239) |
| G​D​PgGDP\_{g} | 0.024∗∗ | -0.000 | 0.019 | 0.000 |
|  | (0.012) | (0.008) | (0.012) | (0.008) |
| F​D​LFDL | 0.083∗∗ | -0.044 | 0.010 | -0.023 |
|  | (0.034) | (0.035) | (0.041) | (0.037) |
| L​D​RLDR | -0.057 | 0.161 | 0.160 | 0.075 |
|  | (0.278) | (0.166) | (0.181) | (0.175) |
| N​I​I​RNIIR | -0.001 | -0.002∗ | 0.001 | -0.002∗ |
|  | (0.003) | (0.001) | (0.003) | (0.001) |
| R​O​AROA | 0.142 | 0.156∗∗ | 0.238∗ | 0.194∗ |
|  | (0.139) | (0.074) | (0.131) | (0.098) |
| D​A​RDAR | 2.138 | 3.455∗∗ | 6.627∗∗ | 2.483 |
|  | (3.062) | (1.597) | (3.060) | (1.653) |
| T​A​STAS | -0.355∗∗ | -0.148 | -0.654∗∗∗ | -0.269∗∗ |
|  | (0.136) | (0.115) | (0.236) | (0.114) |
| O​E​XOEX | 0.464∗∗∗ | 0.175∗∗∗ | 0.304∗∗ | 0.193∗∗∗ |
|  | (0.094) | (0.063) | (0.116) | (0.072) |
| C​A​RCAR | -0.006 | 0.019∗∗ | 0.002 | 0.016 |
|  | (0.004) | (0.010) | (0.006) | (0.010) |
| Constant term | -2.036 | -0.684 | 7.103 | 2.616 |
|  | (3.001) | (2.382) | (5.740) | (2.821) |
| Bank FE | YES | YES | YES | YES |
| Year FE | YES | YES | YES | YES |
| Observations | 228 | 675 | 298 | 618 |
| R2R^{2} | 0.72 | 0.45 | 0.69 | 0.38 |
| Notes: This table presents the regression results of the heterogeneity analysis. Columns (1) and (2) show the results for subsamples with patent counts above and below the annual median patent count of all banks, respectively; Columns (3) and (4) report results for listed and non-listed banks, respectively. Differences in sample size are due to missing values in control variables. The model controls for individual and time fixed effects. Variable definitions are provided in Table [2](https://arxiv.org/html/2511.02608v1#S2.T2 "Table 2 ‣ 2.2 Two-way fixed effects model ‣ 2 Methodology ‣ How FinTech affects financial sustainability: Evidence from Chinese commercial banks using a three-stage network DEA-Malmquist model"). ∗, ∗∗, and ∗∗∗ indicate statistical significance at the 10%, 5%, and 1% levels, respectively. Standard errors are clustered at the bank level and reported in parentheses. R2R^{2} represents the coefficient of determination. | | | | |
| --- | --- | --- | --- | --- |

## 4 Conclusion

In this paper, we provide evidence that FinTech undermines the FS of commercial banks. Our main findings are as follows. First, we measure the FS of 104 Chinese commercial banks from 2015 to 2023 using a three-stage network DEA-Malmquist model. Except for the period affected by the COVID-19 pandemic, the FS of banks generally exhibits a steady upward trend. Second, empirical results across multiple model specifications, including two-way fixed effects and an IV approach, reveal that FinTech significantly diminishes the FS of commercial banks. Furthermore, the mechanism analysis reveals that the impact of FinTech mainly operates through the erosion of the loan and profitability efficiencies of banks. In addition, heterogeneity analysis indicates that banks with fewer patents and non-listed experience a greater impact from FinTech.

This paper offers an initial exploration of the impact of FinTech on FS of Chinese commercial banks, which has rarely been studied, and we contribute by bridging this gap. An open question remains as to whether the rise of FinTech will ultimately foster complementary benefits for traditional banks in the future. Some studies find that the responses of banks to FinTech can improve their performance. Incumbent banks that invest in or collaborate with FinTech firms may achieve synergies that partly offset the negative impacts of competition (Hornuf et al.,, [2021](https://arxiv.org/html/2511.02608v1#bib.bib28)). However, other research argues that competition, interest margins, and the adverse effects of alternative digital credit might offset these gains (Cuadros-Solas et al.,, [2023](https://arxiv.org/html/2511.02608v1#bib.bib19)). This situation is particularly the case for banks lacking innovation capabilities or market discipline. Moreover, the net effect could also depend on how regulatory frameworks evolve to balance innovation with financial stability (Vives,, [2019](https://arxiv.org/html/2511.02608v1#bib.bib55)). Future research could quantify the benefits and costs of FinTech adoption for different types of banks. It also could explore how technological innovation interacts with strategic adaptation, and whether the adverse effects we document persist, attenuate, or reverse over time. Such analyses would provide valuable insights for policymakers and bank managers seeking to leverage technological development while safeguarding FS. In addition, besides FinTech, other factors might also influence the FS of banks. Future research could investigate alternative explanations from the perspectives of green finance, macroeconomic policy shocks, and internal governance structures to further enrich the relevant literature. Methodologically, future research could also consider noise-adjusted approaches, such as the NSCNLS and NStoNED models proposed by Wang et al., ([2025](https://arxiv.org/html/2511.02608v1#bib.bib59)). These models extend network DEA to account for stochastic noise and may provide more robust efficiency estimates in multi-stage banking processes.

## Acknowledgements

This work is supported by the Young Scientists Fund of the National Natural Science Foundation of China (grant number 72301177), the Shanghai Pujiang Program (grant number 22PJC091), and the National Social Science Fund of China (grant number 24BGL062).

## References

* Abu Wadi et al., (2022)

  Abu Wadi, R., Bashayreh, A., Khalaf, L., and Abdelhadi, S. (2022).
  Financial sustainability and outreach in microfinance institutions:
  Evidence from MENA countries.
  Journal of Sustainable Finance & Investment, 12(1):238–250.
* Aharon et al., (2023)

  Aharon, D. Y., Ali, S., and Naved, M. (2023).
  Too big to fail: The aftermath of Silicon Valley Bank (SVB)
  collapse and its impact on financial markets.
  Research in International Business and Finance, 66:102036.
* Akhtaruzzaman et al., (2023)

  Akhtaruzzaman, M., Boubaker, S., and Goodell, J. W. (2023).
  Did the collapse of Silicon Valley Bank catalyze financial
  contagion?
  Finance Research Letters, 56:104082.
* Assaf et al., (2013)

  Assaf, A. G., Matousek, R., and Tsionas, E. G. (2013).
  Turkish bank efficiency: Bayesian estimation with undesirable
  outputs.
  Journal of Banking & Finance, 37(2):506–517.
* Avkiran, (2015)

  Avkiran, N. K. (2015).
  An illustration of dynamic network DEA in commercial banking
  including robustness tests.
  Omega, 55:141–150.
* Baltagi, (2008)

  Baltagi, B. H. (2008).
  Econometric Analysis of Panel Data.
  John Wiley & Sons.
* Bansal et al., (2022)

  Bansal, P., Mehra, A., and Kumar, S. (2022).
  Dynamic metafrontier Malmquist–Luenberger productivity index in
  network DEA: An application to banking data.
  Computational Economics, 59(1):297–324.
* Barros et al., (2009)

  Barros, C. P., Managi, S., and Matousek, R. (2009).
  Productivity growth and biased technological change: Credit banks
  in Japan.
  Journal of International Financial Markets, Institutions and
  Money, 19(5):924–936.
* Beccalli et al., (2015)

  Beccalli, E., Anolli, M., and Borello, G. (2015).
  Are European banks too big? Evidence on economies of scale.
  Journal of Banking & Finance, 58:232–246.
* Benston, (1965)

  Benston, G. J. (1965).
  Branch banking and economies of scale.
  The Journal of Finance, 20(2):312–331.
* Bogan, (2012)

  Bogan, V. L. (2012).
  Capital structure and sustainability: An empirical study of
  microfinance institutions.
  Review of Economics and Statistics, 94(4):1045–1058.
* Bos et al., (2013)

  Bos, J. W., Kolari, J. W., and van Lamoen, R. C. (2013).
  Competition and innovation: Evidence from financial services.
  Journal of Banking & Finance, 37(5):1590–1601.
* Buchak et al., (2018)

  Buchak, G., Matvos, G., Piskorski, T., and Seru, A. (2018).
  Fintech, regulatory arbitrage, and the rise of shadow banks.
  Journal of Financial Economics, 130(3):453–483.
* Casu et al., (2004)

  Casu, B., Girardone, C., and Molyneux, P. (2004).
  Productivity change in European banking: A comparison of
  parametric and non-parametric approaches.
  Journal of Banking & Finance, 28(10):2521–2540.
* Caves et al., (1982)

  Caves, D. W., Christensen, L. R., and Diewert, W. E. (1982).
  The economic theory of index numbers and the measurement of input,
  output, and productivity.
  Econometrica: Journal of the Econometric Society,
  50(6):1393–1414.
* Charnes et al., (1978)

  Charnes, A., Cooper, W. W., and Rhodes, E. (1978).
  Measuring the efficiency of decision making units.
  European Journal of Operational Research, 2(6):429–444.
* Cheng and Qu, (2020)

  Cheng, M. and Qu, Y. (2020).
  Does bank FinTech reduce credit risk? Evidence from China.
  Pacific-Basin Finance Journal, 63:101398.
* Cook et al., (2010)

  Cook, W. D., Zhu, J., Bi, G., and Yang, F. (2010).
  Network DEA: Additive efficiency decomposition.
  European Journal of Operational Research, 207(2):1122–1129.
* Cuadros-Solas et al., (2023)

  Cuadros-Solas, P. J., Cubillas, E., and Salvador, C. (2023).
  Does alternative digital lending affect bank performance?
  Cross-country and bank-level evidence.
  International Review of Financial Analysis, 90:102873.
* Dabi et al., (2023)

  Dabi, R. S. K., Nugraha, Disman, and Sari, M. (2023).
  Capital structure, financial performance and sustainability of
  microfinance institutions (MFIs) in Ghana.
  Cogent Economics & Finance, 11(2):2230013.
* Elnahass et al., (2021)

  Elnahass, M., Trinh, V. Q., and Li, T. (2021).
  Global banking stability in the shadow of Covid-19 outbreak.
  Journal of International Financial Markets, Institutions and
  Money, 72:101322.
* Färe et al., (1994)

  Färe, R., Grosskopf, S., Norris, M., and Zhang, Z. (1994).
  Productivity growth, technical progress, and efficiency change in
  industrialized countries.
  The American Economic Review, pages 66–83.
* Fonchamnyo et al., (2023)

  Fonchamnyo, D. C., Anyangwe, T., Chantal, N. N., and Dinga, G. D. (2023).
  Capital structure and financial sustainability: Stakes of
  microfinance institutions in Bamenda, Cameroon.
  Future Business Journal, 9(1):41.
* Fukuyama et al., (2020)

  Fukuyama, H., Matousek, R., and Tzeremes, N. G. (2020).
  A Nerlovian cost inefficiency two-stage DEA model for modeling
  banks’ production process: Evidence from the Turkish banking system.
  Omega, 95:102198.
* Gao, (2022)

  Gao, J. (2022).
  Comparison of fintech development between China and the United
  States.
  International Journal of Innovative Science and Research
  Technology, 6563524:1272–6.
* Guo et al., (2020)

  Guo, F., Wang, J., Wang, F., Kong, T., Zhang, X., and Cheng, Z. (2020).
  Measuring China’s digital financial inclusion: Index compilation
  and spatial characteristics.
  China Economic Quarterly, 19(4):1401–1418.
* Gupta and Sharma, (2023)

  Gupta, P. K. and Sharma, S. (2023).
  Literature review on effect of microfinance institutions on poverty
  in South Asian countries and their sustainability.
  International Journal of Emerging Markets, 18(8):1827–1845.
* Hornuf et al., (2021)

  Hornuf, L., Klus, M. F., Lohwasser, T. S., and Schwienbacher, A. (2021).
  How do banks interact with fintech startups?
  Small Business Economics, 57:1505–1526.
* Hsiao, (2014)

  Hsiao, C. (2014).
  Analysis of Panel Data.
  Cambridge University Press.
* Hu et al., (2024)

  Hu, D., Zhao, S., and Yang, F. (2024).
  Will fintech development increase commercial banks risk-taking?
  Evidence from China.
  Electronic Commerce Research, 24(1):37–67.
* Jaffry et al., (2007)

  Jaffry, S., Ghulam, Y., Pascoe, S., and Cox, J. (2007).
  Regulatory changes and productivity of the banking sector in the
  Indian sub-continent.
  Journal of Asian Economics, 18(3):415–438.
* Kinde, (2012)

  Kinde, B. A. (2012).
  Financial sustainability of microfinance institutions (MFIs) in
  Ethiopia.
  European Journal of Business and Management, 4(15):1–10.
* Kohl et al., (2019)

  Kohl, S., Schoenfelder, J., Fügener, A., and Brunner, J. O. (2019).
  The use of data envelopment analysis (DEA) in healthcare with a
  focus on hospitals.
  Health Care Management Science, 22(2):245–286.
* Lee et al., (2021)

  Lee, C.-C., Li, X., Yu, C.-H., and Zhao, J. (2021).
  Does fintech innovation improve bank efficiency? Evidence from
  China’s banking industry.
  International Review of Economics & Finance, 74:468–483.
* Lee et al., (2023)

  Lee, C.-C., Ni, W., and Zhang, X. (2023).
  Fintech development and commercial bank efficiency in China.
  Global Finance Journal, 57:100850.
* Li et al., (2023)

  Li, L., Gao, W., and Gu, W. (2023).
  Fintech, bank concentration and commercial bank profitability:
  Evidence from Chinese urban commercial banks.
  Finance Research Letters, 57:104234.
* Li et al., (2024)

  Li, X., Xu, G., Wu, J., Xu, C., and Zhu, Q. (2024).
  Evaluation of bank efficiency by considering the uncertainty of
  nonperforming loans.
  Omega, 126:103069.
* Liang and Renneboog, (2017)

  Liang, H. and Renneboog, L. (2017).
  On the foundations of corporate social responsibility.
  The Journal of Finance, 72(2):853–910.
* Maeenuddin et al., (2023)

  Maeenuddin, S. A. H., Nassir, A., and Hashim, P. M. (2023).
  Developing an index for the measurement of financial sustainability
  of microfinance providers: A theoretical review.
  Central European Management Journal, 31(1):197–205.
* Malmquist, (1953)

  Malmquist, S. (1953).
  Index numbers and indifference surfaces.
  Trabajos de estadística, 4(2):209–242.
* Matthews, (2013)

  Matthews, K. (2013).
  Risk management and managerial efficiency in Chinese banks: A
  network DEA framework.
  Omega, 41(2):207–215.
* Metrick, (2024)

  Metrick, A. (2024).
  The failure of Silicon Valley Bank and the panic of 2023.
  Journal of Economic Perspectives, 38(1):133–152.
* Murinde et al., (2022)

  Murinde, V., Rizopoulos, E., and Zachariadis, M. (2022).
  The impact of the FinTech revolution on the future of banking:
  Opportunities and risks.
  International Review of Financial Analysis, 81:102103.
* Najam et al., (2022)

  Najam, H., Abbas, J., Alvarez-Otero, S., Dogan, E., and Sial, M. S. (2022).
  Towards green recovery: Can banks achieve financial sustainability
  through income diversification in ASEAN countries?
  Economic Analysis and Policy, 76:522–533.
* Portela and Thanassoulis, (2010)

  Portela, M. C. and Thanassoulis, E. (2010).
  Malmquist-type indices in the presence of negative data: An
  application to bank branches.
  Journal of Banking & Finance, 34(7):1472–1483.
* Prior et al., (2019)

  Prior, D., Tortosa-Ausina, E., García-Alcober, M. P., and Illueca, M.
  (2019).
  Profit efficiency and earnings quality: Evidence from the Spanish
  banking industry.
  Journal of Productivity Analysis, 51(2):153–174.
* Qiu et al., (2023)

  Qiu, L., Yu, R., Hu, F., Zhou, H., and Hu, H. (2023).
  How can China’s medical manufacturing listed firms improve their
  technological innovation efficiency? An analysis based on a three-stage
  DEA model and corporate governance configurations.
  Technological Forecasting and Social Change, 194:122684.
* Romānova and Kudinska, (2016)

  Romānova, I. and Kudinska, M. (2016).
  Banking and Fintech: A challenge or opportunity?
  In Contemporary Issues in Finance: Current Challenges
  from Across Europe, volume 98, pages 21–35. Emerald Group Publishing
  Limited.
* Sealey Jr. and Lindley, (1977)

  Sealey Jr., C. W. and Lindley, J. T. (1977).
  Inputs, outputs, and a theory of production and cost at depository
  financial institutions.
  The Journal of Finance, 32(4):1251–1266.
* Sherman and Gold, (1985)

  Sherman, H. D. and Gold, F. (1985).
  Bank branch operating efficiency: Evaluation with data envelopment
  analysis.
  Journal of Banking & Finance, 9(2):297–315.
* Shi et al., (2025)

  Shi, Y., Charles, V., and Zhu, J. (2025).
  Bank financial sustainability evaluation: Data envelopment analysis
  with random forest and shapley additive explanations.
  European Journal of Operational Research, 321(2):614–630.
* Shi et al., (2020)

  Shi, Y., Zhu, J., and Charles, V. (2020).
  Data science and productivity: A bibliometric review of data
  science applications and approaches in productivity evaluations.
  Journal of the Operational Research Society, 72(5):975–988.
* Staub et al., (2010)

  Staub, R. B., Souza, G. d. S., and Tabak, B. M. (2010).
  Evolution of bank efficiency in Brazil: A DEA approach.
  European Journal of Operational Research, 202(1):204–213.
* Thakor, (2020)

  Thakor, A. V. (2020).
  Fintech and banking: What do we know?
  Journal of Financial Intermediation, 41:100833.
* Vives, (2019)

  Vives, X. (2019).
  Digital disruption in banking.
  Annual Review of Financial Economics, 11(1):243–272.
* Wang et al., (2014)

  Wang, K., Huang, W., Wu, J., and Liu, Y.-N. (2014).
  Efficiency measures of the Chinese commercial banking system using
  an additive two-stage DEA.
  Omega, 44:5–20.
* (57)

  Wang, R., Liu, J., and Luo, H. (2021a).
  Fintech development and bank risk taking in China.
  The European Journal of Finance, 27(4-5):397–418.
* (58)

  Wang, Y., Xiuping, S., and Zhang, Q. (2021b).
  Can fintech improve the efficiency of commercial banks? —An
  analysis based on big data.
  Research in International Business and Finance, 55:101338.
* Wang et al., (2025)

  Wang, Z., Yang, M., Liang, L., and Zhu, J. (2025).
  A nonparametric least-squares model in network data envelopment
  analysis.
  European Journal of Operational Research.
  In press.
* Wei and Zhao, (2024)

  Wei, X. and Zhao, R. (2024).
  Evaluation and spatial convergence of carbon emission reduction
  efficiency in China’s power industry: Based on a three-stage DEA model
  with game cross-efficiency.
  Science of The Total Environment, 906:167851.
* Wooldridge, (2010)

  Wooldridge, J. M. (2010).
  Econometric Analysis of Cross Section and Panel Data.
  MIT Press.
* Wooldridge, (2015)

  Wooldridge, J. M. (2015).
  Control function methods in applied econometrics.
  Journal of Human Resources, 50(2):420–445.
* Wry and Zhao, (2018)

  Wry, T. and Zhao, E. Y. (2018).
  Taking trade-offs seriously: Examining the contextually contingent
  relationship between social outreach intensity and financial sustainability
  in global microfinance.
  Organization Science, 29(3):507–528.
* Wu and Olson, (2020)

  Wu, D. D. and Olson, D. L. (2020).
  The effect of COVID-19 on the banking sector.
  In Pandemic Risk Management in Operations and Finance:
  Modeling the Impact of COVID-19, pages 89–99. Springer.
* Xie et al., (2022)

  Xie, Q., Xu, Q., Chen, L., Jin, X., Li, S., and Li, Y. (2022).
  Efficiency evaluation of China’s listed commercial banks based on a
  multi-period leader-follower model.
  Omega, 110:102615.
* Yao and Fan, (2025)

  Yao, J. and Fan, J. (2025).
  The impact of policy uncertainty and risk taking on the credit
  resource allocation of urban commercial banks.
  International Review of Economics & Finance, 97:103766.
* Yu et al., (2021)

  Yu, M.-M., Lin, C.-I., Chen, K.-C., and Chen, L.-H. (2021).
  Measuring Taiwanese bank performance: A two-system dynamic
  network data envelopment analysis approach.
  Omega, 98:102145.
* Zeller and Meyer, (2002)

  Zeller, M. and Meyer, R. L. (2002).
  The Triangle of Microfinance: Financial Sustainability,
  Outreach, and Impact.
  The Johns Hopkins University Press.
* Zhang et al., (2020)

  Zhang, Y.-J., Liang, T., Jin, Y.-L., and Shen, B. (2020).
  The impact of carbon trading on economic output and carbon emissions
  reduction in China’s industrial sectors.
  Applied Energy, 260:114290.