---
authors:
- Saani Rawat
doc_id: arxiv:2511.06562v1
family_id: arxiv:2511.06562
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I
  am grateful to SHRUG, for making their data publicly available. I thank David Brasington,
  Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and
  suggestions. All errors are my own. No external funding was received for this project.'
url_abs: http://arxiv.org/abs/2511.06562v1
url_html: https://arxiv.org/html/2511.06562v1
venue: arXiv q-fin
version: 1
year: 2025
---


Saani Rawat
PhD Candidate, University of Cincinnati. Corresponding author: rawatsa@mail.uc.edu

(November 9, 2025)

This paper examines the causal effect of urban local governance on public goods provision in India. We exploit quasi-random variation in multi-threshold criteria utilized for classifying Census Towns (CTs) and focus on settlements near the thresholds that are likely to obtain statutory recognition. Using a fuzzy regression discontinuity design, we instrument for urban local governance to identify the Local Average Treatment Effect (LATE). We document a strong first stage relationship between meeting CT thresholds and statutory recognition. Our results show that obtaining an Urban Local Body (ULB) increases local public good provision: government schools increase by approximately 14 (primary), 8 (middle), and 5 (secondary), healthcare infrastructure expands by 2 hospitals and 3 family welfare centers, and financial access deepens with 15 private banks, 2 cooperative banks, and 2 agricultural credit societies. Community amenities improve modestly with an additional public library, reading room, and cinema hall. Sports infrastructure declines by 5 facilities, consistent with our understanding of reallocation of urban space and investments. Our findings suggest that timely municipalization of emerging urban areas can expand provision of certain public goods, which may improve living standards and economic opportunities in urbanizing economies.
  
  
Keywords: Urban Local Governance, Statutory towns, Census Towns, Public Goods
  
  
JEL Codes: H75, R53, O18

## 1 Introduction

Urban local bodies (ULBs) are responsible for a substantial share of on-the-ground public goods in developing countries—schools, primary health facilities, sanitation, streets, lighting, and local regulation. Whether and how urban local governance matters for local economic development is a long-standing question, with renewed urgency in rapidly urbanizing economies (BrolloEtAl2013; Faguet2012; PatrickMothorpe2017). A key empirical challenge is that governance structures are endogenous: places that are bigger and more developed are more likely to be recognized as urban towns and receive municipal governance, while smaller or less developed settlements may not receive such recognition and therefore stagnate even further by being outside the urban system (Gadenne2017). Simple cross-sectional comparisons in such contexts will conflate pre-existing differences with the effects of policy. In other words, urban governance status is chosen rather than randomly assigned, making causal inference difficult.

This paper leverages a sharp institutional feature in India to address this identification problem: the Census Town (CT) classification thresholds that determine eligibility for an area to be considered urban. The Indian Census defines Census Towns as settlements meeting all three criteria: (i) population of at least 5,000 (ii) population density of at least 400 per square kilometer and (iii) at least 75% of the male main workforce in non-agricultural activities. Crossing these multi-dimensional cutoffs sharply increases the probability that a settlement will be formally recognized by state governments as a Statutory Town (ST) (i.e. given a municipality or other ULB status) but notably, it does not guarantee it. We exploit this quasi-random variation in recognition likelihood around the thresholds to construct a local fuzzy regression discontinuity (RD) design. In effect, meeting the Census Town criteria in 2001 serves as an instrument for obtaining urban local governance in 2011, allowing us to identify the causal effects of statutory town status on local outcomes.

The core idea is a fuzzy multi-threshold RD with multiple running variables. Using rich settlement-level microdata from the Socioeconomic High-resolution Rural-Urban Geographic (SHRUG) platform (asher2019shrug), we create a running variable called frontier distance using the three CT cutoffs and restrict attention to settlements near these thresholds. We first confirm a strong first-stage relationship: becoming marginally eligible as a Census Town in 2001 leads to a large jump in the probability of statutory recognition in 2011. We then estimate the Local Average Treatment Effect (LATE) of urban local governance (statutory town status) on a broad set of development indicators measured by the 2011 Indian Census. Our outcome data are assembled by harmonizing the 2011 Village Directory (VD) and Town Directory (TD) which enumerate local infrastructure and amenities. We link these to demographic data from the 2011 Primary Census Abstract (PCA). This provides a comprehensive settlement-level panel of outcomes including educational facilities, health infrastructure, financial institutions, and other community amenities.

Preview of results. We find that crossing the urban eligibility thresholds leads to a pronounced increase in the likelihood of statutory recognition. In particular, meeting all three Census Town criteria raises the probability of obtaining urban local governance by approximately 7.1 percentage points, with a first-stage F-statistic of 18.81, indicating a reasonably strong instrumental variable. Using this fuzzy RD design, our two-stage least squares (2SLS) estimates indicate that formal urban status substantially improves local public goods provision. For example, obtaining a municipality leads to an increase of about 13.5 additional government primary schools in a settlement (relative to the mean for similar settlements just below the threshold), along with roughly 7.8 more middle schools and 5.0 more secondary schools on average. We also find large positive effects on health and financial infrastructure: being recognized as a town increases the number of hospitals by about 2.5 and family welfare centers by about 3.0, and boosts the presence of banking facilities (e.g. approximately 15.4 more private bank branches, 2.3 more cooperative banks, and 2.2 more agricultural credit societies). We also observe improvements in community infrastructure, including 1.1 additional public libraries, 1.4 more public reading rooms, and 0.8 more cinema halls. These are sizable improvements, given that settlements just below the threshold typically have only a handful of such facilities. Results are robust to bandwidth choices and polynomial specifications111Available in forthcoming drafts., and they remain consistent when clustering standard errors at the district or state level. Furthermore, robustness checks support the validity of the design – we find no evidence for manipulation around the thresholds, detect overall balance in baseline characteristics and find null reduced form effects via the direct relationship between crossing the thresholds and outcomes absent of the change in statutory town status.

Our work builds on a growing literature that examines how local institutional capacity and governance shape development outcomes in low- and middle-income countries.
besley2010state emphasize that investments in fiscal and legal capacity are key determinants of long-run development, and that variations in local administrative effectiveness can shape the quality of service delivery.
Relatedly, gadenne2017tax shows that greater fiscal autonomy can improve accountability and service delivery when citizens can observe how funds are used, while burgess2015value highlights how political incentives affect the allocation of public goods across regions. We contribute to this literature by providing causal evidence on a different but complementary margin — the formal transition of villages to urban local governance. Rather than focusing on local fiscal resources, we study how the administrative act of granting municipal status itself changes public goods provision. By leveraging the multi-threshold eligibility criteria for Census Town classification as a quasi-experiment, we isolate exogenous variation in the likelihood of urban local governance and estimate its local average treatment effect on infrastructure outcomes. This approach provides new evidence on how the extension of urban local governance institutions affects provision of local public goods in urbanizing economies.

The paper contributes to the literature via two main fronts. First, it adds to the causal evidence literature by quantifying the effect of urban governance on local public goods provision in large developing economies. Second, it uses a novel instrument and builds a framework for using multi-dimensional cutoffs in a fuzzy RD design setting, which can be applied to other contexts where policy eligibility and implementation is affected by multiple criteria, allowing researchers to exploit quasi-random variation in policy exposure for causal inference.

Section [2](https://arxiv.org/html/2511.06562v1#S2 "2 Literature Review ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") covers the literature review. Section [3](https://arxiv.org/html/2511.06562v1#S3 "3 Background & Data ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") provides institutional background and describes data construction. Section [4](https://arxiv.org/html/2511.06562v1#S4 "4 Empirical Strategy ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") develops the identification strategy and estimation. Section [5](https://arxiv.org/html/2511.06562v1#S5 "5 Results ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") presents results and robustness. The conclusion discusses implications for urban policy and future research avenues.

## 2 Literature Review

This section situates our contribution within several strands of literature on local governance, urbanization, and econometric methods.

##### Urban governance and decentralization.

A large body of work examines whether shifting authority to local governments leads to better public goods provision and welfare outcomes. Classic fiscal federalism theory argues that local governments have informational advantages and can be more responsive to citizen needs (Oates1972). Greater proximity and accountability at the local level may improve allocation of resources to match local preferences. However, other theories warn of potential pitfalls: local elites might capture resources, or small governments may lack administrative capacity and financial resources (BardhanMookherjee2006). Empirical findings on decentralization are mixed. For example, faguet2014can finds that decentralization in Bolivia increased investment in social infrastructure, but similar reforms in other contexts have yielded varying results depending on community participation and oversight. In India, the 73rd and 74th Constitutional Amendments devolved powers to rural panchayats and urban municipalities, respectively, spurring research on their impacts. Studies of village council (panchayat) reforms have found that who leads the council can matter for public goods: for instance, ChattopadhyayDuflo2004 show that mandating women leaders in Indian villages altered the composition of public goods (e.g., more drinking water infrastructure), and (BesleyPandeRao2005) document that more accountable local governments can better target beneficiaries. Still, there is limited causal evidence isolating the effect of having an urban local government in particular – a gap this paper begins to fill.

##### India’s urban classification and Census Towns.

Our study also relates to research on India’s unique two-tier system of urban classification. Indian settlements can be recognized as urban in two ways: (1) by statutory notification as a municipality or other ULB (a political process controlled by state governments), or (2) by satisfying the Census definition of a “Census Town” based on demographic and economic criteria (a statistical designation by the Census of India). A rich descriptive literature documents the tension between rapid urban population growth and slow municipal incorporation. For example, pradhan2017 highlights the phenomenon of new Census Towns in the 2011 Census – over 3,500 places that became urban by Census criteria since 2001 – many of which were not granted municipal status (“unacknowledged urbanisation”). Kundu2011 and others have argued that state governments often hesitate to create new municipalities due to fiscal and political constraints, leading to a backlog of urbanizing villages that lack urban governance. Our work uses the Census Town thresholds as a natural experiment to study this institutional friction. In doing so, we build on government documentation of these criteria (Registrar General of India, 2011) and recent analyses of the socio-economic differences between statutory towns and Census Towns. By focusing on settlements around the threshold cutoffs, we effectively compare places that are very similar in population and economy – one just meeting the “urban” criteria and one just below – to see if being officially recognized as a town yields different outcomes.

##### Urban public goods and service delivery.

Our outcome measures contribute to a literature on public service provision in urban areas. Much prior research on urban services in developing countries has relied on household surveys or city-level aggregates. For instance, health and education outcomes are often studied via household data (e.g., the National Family Health Survey or NFHS in India, which provides indicators like immunization rates or school attendance) or via municipal expenditures on services. These approaches, however, can miss granular differences in infrastructure availability at the community level. We instead use the village/town administrative directories to directly measure the presence and quantity of infrastructure (schools, hospitals, banks, libraries, sports facilities, etc.) in each settlement. This complements studies that have examined urban service delivery through other lenses – such as comparisons of slum versus non-slum neighborhoods Auerbach2018 or analyses of the effect of local political incentives on service quality Banerjee2024. By examining a broad set of infrastructure outcomes, our paper provides a holistic view of how municipal status might change the provision of public goods. The evidence on whether municipal governance improves services is limited; for example, some case studies suggest that cities with elected mayors perform better in solid waste management or water provision, but confounding factors abound. Our contribution is to use a causal design to measure these effects at the settlement level.

In summary, our study provides new evidence on the development impacts of urban local governance, leveraging a policy threshold in India’s urban classification system. It bridges the decentralization literature and urbanization debates, introduces a novel multi-threshold RD approach, and contributes a unified data framework for analyzing settlements. Next, we describe the institutional setting and data in more detail.

## 3 Background & Data

### 3.1 Institutional Background

India’s urban classification rests on two pillars. First, are settlements officially designated as urban by state governments via a notification under municipal law. These include municipal corporations, municipalities, and nagar panchayats222a type of town council for smaller urban areas, and are each known as *Statutory Towns* (STs). Second, *Census Towns* (CTs) are settlements that satisfy Census thresholds: total population at least 5,000; population density of at least 400 persons per km²; and at least 75 percent of the male main workforce in non-agricultural activities. CTs are urban for statistical purposes but may continue under rural governance unless notified as STs by the state governments. Crossing the CT thresholds increases the chance of statutory recognition but does not guarantee it as states differ in municipalization policy and timing. Some states have proactive policies to incorporate new urbanizing areas, while others delay or avoid creating new ULBs due to budgetary or political considerations.

### 3.2 Local Governance in India

#### 3.2.1 How are Urban Local Bodies (ULBs) formed?

The Nagarpalika Act, which was the 74th Amendment to the Indian Constitution enacted in 1992, provides the legal framework for urban local governance in India (MHA\_74thAmendment). This constitutional amendment is supported by state-level municipal acts, such as GoaMunicipalities1968; GujaratMunicipalities1963; KarnatakaMunicipalities1964; MaharashtraMunicipalities1965; TelanganaMunicipalities2019 etc., that outline the specific procedures for forming Urban Local Bodies (ULBs). Although the process differs slightly across states, it typically has similar considerations and involves several steps:

1. 1.

   Identification and Survey: State governments or local development authorities identify settlements that have urbanized characteristics or meet certain census or urban-classification criteria333as per state’s discretion. (population, density, non-agricultural workforce). A survey may be conducted to assess the settlement’s infrastructure, population, and economic activities.
2. 2.

   Proposal and Feasibility Study: In many states, the district administration or relevant state department may prepare a proposal for granting municipal status. This includes a feasibility assessment of the settlement’s capacity to sustain urban governance, including revenue potential, administrative requirements, and infrastructure needs.
3. 3.

   Public Consultation: The proposal may be opened for public consultation where residents and stakeholders can provide feedback. This step also varies by state and may include public hearings or written submissions.
4. 4.

   State Government Approval: The proposal is submitted to the state government, usually through the Urban Development or Municipal Affairs Department, for review. The state government evaluates political, administrative, and fiscal considerations.
5. 5.

   Official Notification: Upon approval, the state government issues an official gazette notification declaring the settlement as a statutory town (municipality, municipal corporation, or nagar panchayat, depending on size and status). This notification legally establishes the ULB and defines its boundaries.
6. 6.

   Election and Formation: Following notification, elections are conducted to form the urban local body. Elected representatives constitute the municipal council or corporation, with a mayor or chairperson as the executive head.
7. 7.

   Transfer of Functions and Resources: The newly formed ULB assumes responsibility for urban functions as per the 74th Amendment and state municipal acts. For many states, this includes transfer of staff, assets, and revenue sources from previous administrative authorities.

The entire process, from initial identification to operational ULB, can take several years and is subject to state-specific variations in policy, political will, and administrative capacity. Some states proactively municipalize urbanizing settlements, while others delay recognition due to fiscal or political constraints, leading to the phenomenon of Census Towns—settlements that are functionally urban but remain under rural governance.

#### 3.2.2 What comes with ULB recognition?

When a settlement receives statutory recognition as an Urban Local Body (ULB), it undergoes a fundamental transformation in governance structure, fiscal arrangements, and administrative responsibilities. The 74th Constitutional Amendment Act of 1992 mandates that ULBs assume control over 18 functions listed in the Twelfth Schedule, including urban planning, regulation of land use, roads and bridges, water supply, public health and sanitation, fire services, urban poverty alleviation, and provision of urban amenities (MHA\_74thAmendment).

Crucially, ULB recognition brings changes in three key dimensions:

Governance and Administrative Structure: Statutory towns transition from rural governance under gram panchayats to elected municipal councils or corporations. This shift creates a dedicated urban administrative apparatus with specialized departments for engineering, health, education, and revenue collection. ULBs are headed by elected mayors or municipal chairpersons, with ward-level representation ensuring political accountability for urban service delivery.

Fiscal Autonomy and Revenue Sources: ULBs gain the authority to levy and collect municipal taxes, most notably property taxes, as well as user charges for water, sanitation, and other services. They also become eligible for devolved funds from state finance commissions and centrally-sponsored urban schemes such as the Jawaharlal Nehru National Urban Renewal Mission (JNNURM) and later the Smart Cities Mission and AMRUT (Atal Mission for Rejuvenation and Urban Transformation). While many ULBs remain fiscally dependent on state transfers, statutory recognition opens access to dedicated urban funding streams unavailable to rural settlements.

Service Delivery Mandates: Upon municipalization, ULBs inherit responsibility for providing and maintaining urban infrastructure and services. This includes establishing and operating primary schools, health dispensaries, water supply systems, sewerage and drainage networks, street lighting, solid waste management, and fire protection services. State governments typically transfer relevant staff, assets, and liabilities from predecessor rural bodies to the newly formed ULB, though the comprehensiveness and timeliness of such transfers vary considerably across states.

However, the practical impact of ULB recognition is heterogeneous. Well-functioning municipalities in states with strong urban governance traditions may deliver substantially better services, while newly formed ULBs in resource-constrained states may struggle with capacity limitations, inadequate transfers, and weak revenue collection. Our empirical analysis examines whether, on average, statutory recognition translates into measurable improvements in local public goods provision.

#### 3.2.3 How does Census Town classification affect statutory recognition?

Although Census Town (CT) classification and statutory recognition are distinct processes that are built on different criteria and governed by different authorities, there is a strong relationship between the two and one often inspires the other (NIUA2020InterStateVar; roy2018predicting). Meeting the CT criteria signals that a settlement has urban characteristics and may warrant municipal governance. When a settlement crosses the CT thresholds, it draws attention from state urban development authorities and policymakers, who may then consider it for notification as a statutory town. The CT designation provides an objective benchmark indicating that the settlement has reached a level of population size, density, and economic activity consistent with urban areas.
This can prompt state governments to evaluate whether the settlement is ready for municipal governance and whether it can sustain the administrative and fiscal responsibilities of a ULB.
In fact, the central government also monitors CTs and encourages states to municipalize them, as exhorted by mohua2016 where the Ministry of Housing and Urban Affairs (MoHUA) formally urged states to consider CTs for statutory recognition.

### 3.3 Data Sources and Construction

Using SHRUG data platform444version 2.1 was available at the time of our study., we collect data at the village and town level555This is the most granular level at which information is available and is identified using SHRUG IDs. for our study (asher2019shrug). We also collect state-level town directories from the Government of India’s Open Government Data (OGD) platform and list of Statutory Towns (STs) from National Housing Bank’s (NHB) website. We highlight the main datasets used in our analysis:

* •

  Population Census Data (2001 & 2011): We draw on comprehensive census data for all Indian settlements across two decennial rounds. The Primary Census Abstract (PCA) provides basic demographic characteristics including total population, gender and age composition, Scheduled Caste and Scheduled Tribe populations, literacy rates, and detailed workforce composition. These data allow us to construct the three Census Town eligibility criteria: population size, population density, and share of male main workers in non-agricultural activities. Further, we use the two village and town directory files on SHRUG -

  + –

    Village Directory (Rural Areas): For rural settlements, we obtain detailed infrastructure and amenity data including area measures, education facilities at all levels (primary through senior secondary, both government and private), health facilities (hospitals, dispensaries, primary and community health centers, maternity centers, family welfare centers, tuberculosis clinics, veterinary hospitals), utilities (power supply availability, water supply sources, sanitation infrastructure), financial access (private banks, cooperative banks, agricultural credit societies), communication and transport infrastructure (post offices, telegraph offices, bus services, railways, paved roads), recreational facilities (public libraries, reading rooms, cinema halls, sports infrastructure), and distances to nearest urban facilities.
  + –

    Town Directory (Urban Areas): For urban settlements, we collect infrastructure data analogous to the Village Directory (VD) with some differences in format and definition. These include area measures (in square kilometers), household counts, education facilities by level and type, health facilities with medical personnel counts, utilities differentiated by connection type, banking facilities, distances to key amenities when not present within town limits, and recreational and sports infrastructure.
* •

  Urban-Rural Classification: We use SHRUG’s official urban-rural classification identifiers to define each settlement’s status for the 2001 and 2011 census rounds. These classification keys link administrative identifiers (state and district codes) to unique SHRUG settlement identifiers, enabling us to match demographic and infrastructure data across datasets and accurately identify whether settlements are officially classified as urban or rural in each census year.
* •

  Statutory Town Lists: We obtain comprehensive lists of all statutorily recognized urban local bodies from the National Housing Bank and state-level census town directories from the Government of India’s Open Government Data (OGD) platform. These administrative records identify which settlements have been officially notified as municipalities, municipal corporations, town panchayats etc., regardless of whether they meet Census Town criteria. We merge these lists with census data using state, district, and settlement name identifiers to construct our treatment indicator for statutory recognition.

Our final sample consists of over 575,000 settlements in India, which includes every inhabited village and town in the 2001 and 2011 Census. Of these, approximately 3,750 have statutory urban status (municipalities of some form) as of 2011, while the remaining  571,000 are governed as rural villages. However, many of those rural-governed settlements are urban in character. In total, about 8,946 settlements meet the Census definition of urban (either they are statutory towns or they qualify as Census Towns). This implies that roughly 1.6% of all Indian settlements were considered urban in 2011 by either criterion, and the rest ( 98.4%) were rural villages. These figures highlight that India’s urban population is concentrated in a relatively small number of settlements – which tend to be much larger on average than the multitude of villages.

### 3.4 Running Variables and Treatment Assignment

The key running variables for our analysis are the three Census Town eligibility criteria: population size, population density, and share of male main workers in non-agricultural activities. We construct these variables using the 2001 Census data for each settlement. Specifically, we consider the following definitions for the running variables666Density plots of these variables are presented in the Appendix.:

* •

  Population Size (PP): Total population of the settlement as recorded in the 2001 Census.
* •

  Population Density (DD): Total population in 2001 divided by the area of the settlement in square kilometers, computed from the area measures provided in the Village and Town Directories.
* •

  Non-Agricultural Share (NN): The proportion of male main workers engaged in non-agricultural activities in 2001, calculated as the number of male main workers in non-agricultural sectors divided by the total number of male main workers in the settlement.

We then define the treatment variable for statutory recognition based on whether a settlement was officially designated as a statutory town (ST) in 2011. This is a binary indicator that takes the value of 1 if the settlement was recognized as an ST in 2011, and 0 otherwise. The treatment assignment is not deterministic based on the running variables alone, as some settlements that meet the Census Town criteria may not receive statutory recognition due to state-level policy decisions, while others that do not meet the criteria may be recognized due to historical or political reasons. Therefore, we use a fuzzy regression discontinuity design that exploits the discontinuities in the probability of receiving statutory recognition at the thresholds defined by the running variables to identify the causal effect of urban governance on local public goods provision.

### 3.5 Key Outcome Variables

Outcomes come in two forms: presence/status indicators (e.g., existence of a primary school), counts (e.g., number of dispensaries), and in TD, distances to nearest facility. Education outcomes cover primary, middle, secondary, senior secondary, colleges (by stream), and vocational institutions. Health outcomes include total hospitals and dispensaries and staffing proxies (doctors/paramedics where available) and specialized centers (PHC/PHSC/MCW/FWC/TB/veterinary). Power outcomes record availability by sector; water/sanitation capture source types and drainage/processing. Access includes banks, markets, communications, transport modes, and road types. Appendix [Appendix](https://arxiv.org/html/2511.06562v1#Ax1 "Appendix ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") reports a full crosswalk between VD and TD variable names.

### 3.6 Sample and Summary Statistics

#### 3.6.1 Urban/Rural Classification vs Statutory Recognition

We define statutory recognition using the state-level files available on Indian government’s Open Government Data (OGD) platform777https://data.gov.in/. These files report the list of statutory towns (municipalities, corporations, nagar panchayats, etc.) for each state as of 2011. We merge these files with the PCA data using state and settlement names to create an indicator for statutory recognition.

Table below shows the cross-tabulation of statutory recognition and whether a settlement meets the CT thresholds.

Table 1: Statutory Recognition and Urban Thresholds

| Panel A: Population ≥\geq 5,000 | | |
| --- | --- | --- |
|  | Pop << 5,000 | Pop ≥\geq 5,000 |
| Not Statutory | 544,894 | 26,848 |
| Statutory | 119 | 3,633 |

| Panel B: Density ≥\geq 400 per km² | | |
| --- | --- | --- |
|  | Density << 400 | Density ≥\geq 400 |
| Not Statutory | 307,343 | 264,399 |
| Statutory | 119 | 3,633 |

| Panel C: Non-Agricultural Male Workers ≥\geq 75% | | |
| --- | --- | --- |
|  | Non-Ag << 75% | Non-Ag ≥\geq 75% |
| Not Statutory | 510,053 | 61,689 |
| Statutory | 1,064 | 2,688 |

| Panel D: All Three Thresholds Combined | | |
| --- | --- | --- |
|  | Did not Meet Thresholds | Met Thresholds |
| Not Statutory | 566,548 | 5,194 |
| Statutory | 1,175 | 2,577 |

Table [1](https://arxiv.org/html/2511.06562v1#S3.T1 "Table 1 ‣ 3.6.1 Urban/Rural Classification vs Statutory Recognition ‣ 3.6 Sample and Summary Statistics ‣ 3 Background & Data ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") provides a descriptive sense of this process by cross-tabulating 2011 Census data on threshold eligibility and actual statutory status. Several patterns stand out. First, many settlements that exceed each individual threshold remain unrecognized. For instance, over 26,800 settlements had populations above 5,000 yet were not statutory towns in 2011, compared to only 3,633 settlements that were both above 5,000 and officially urban (Panel A of Table 1). A similar discrepancy is seen for the density criterion (Panel B) and the non-agricultural workforce criterion (Panel C). Second, looking at the combined criteria (Panel D), we see that a total of 7,771 settlements met all three urban criteria as of 2011. However, only 2,577 of these were actually recognized as statutory towns, while 5,194 settlements met the criteria but remained governed as rural. Conversely, there were 1,175 statutory towns that did not meet all the criteria – these are typically older small towns or special cases that had municipal status historically despite falling short on one of the Census metrics. This highlights that satisfying the Census definition is not sufficient for urban governance; political implementation by states is crucial. It also underscores the quasi-random aspect of our design: among settlements around the thresholds, some will have been converted to ULBs (treatment) and others not (control), not purely based on merit but partly due to state-specific policies and timing.

Recognizing a settlement as an urban local body brings a change in governance structure. Upon becoming a ULB, the settlement is governed by an elected urban local government (municipality or town council) rather than a rural council. Indian ULBs, as per the 74th Constitutional Amendment, are entrusted with a range of local functions. These include providing core public goods and services such as primary education, basic health and sanitation, water supply, solid waste management, street lighting, roads and transportation, and regulation of land use and construction. They also have authority to collect certain taxes (like property taxes) and user fees, and they receive transfers from state and central governments. In theory, municipalities should have greater resources and autonomy to invest in local infrastructure compared to rural bodies, although in practice many ULBs face capacity and funding constraints. We are interested in whether a settlement’s “switch” from rural to urban governance (statutory recognition) translates into measurable differences in local development indicators. Our hypothesis is that municipalities, despite their challenges, may deliver better access to public services than the rural governance system, due to a combination of dedicated funding, political accountability, and administrative focus on urban needs.

#### 3.6.2 Treatment Assignment and Treatment Status

Table [2](https://arxiv.org/html/2511.06562v1#S3.T2 "Table 2 ‣ 3.6.2 Treatment Assignment and Treatment Status ‣ 3.6 Sample and Summary Statistics ‣ 3 Background & Data ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") presents the distribution of settlements by Census Town (CT) classification in 2001 and statutory town (ST) status by 2011. Panel A shows the full sample of all settlements, while Panel B restricts to settlements close to the CT thresholds.

Table 2: Treatment Assignment and Status

| Panel A: Full Sample | | | |
| --- | --- | --- | --- |
| CT in 2001 | Statutory by 2011 | N | Share (%) |
| No | No | 495,215 | 98.50 |
| No | Yes | 1,199 | 0.24 |
| Yes | No | 3,223 | 0.64 |
| Yes | Yes | 2,542 | 0.51 |
| Total |  | 502,179 | 100.00 |

|  |  |  |  |
| --- | --- | --- | --- |
| Panel B: Close to Threshold Sample | | | |
| CT in 2001 | Statutory by 2011 | N | Share (%) |
| No | No | 36,726 | 99.19 |
| No | Yes | 100 | 0.27 |
| Yes | No | 297 | 0.80 |
| Yes | Yes | 28 | 0.08 |
| Total |  | 37,151 | 100.00 |

Notes: “CT in 2001” indicates whether a settlement met all three Census Town criteria (population ≥\geq 5,000, density ≥\geq 400 per km², non-agricultural workers ≥\geq 75%) in 2001. “Statutory by 2011” indicates whether the settlement had statutory town status in 2011. Panel B restricts to settlements within the bandwidth around the CT thresholds.

Several patterns emerge from Table [2](https://arxiv.org/html/2511.06562v1#S3.T2 "Table 2 ‣ 3.6.2 Treatment Assignment and Treatment Status ‣ 3.6 Sample and Summary Statistics ‣ 3 Background & Data ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project."). In the full sample (Panel A), the vast majority of settlements (98.5%) neither met the CT criteria in 2001 nor received statutory recognition by 2011. Among the 5,765 settlements that met the CT thresholds in 2001, only 2,542 (44%) gained statutory status by 2011, while 3,223 (56%) remained under rural governance despite being functionally urban. This substantial gap between eligibility and recognition illustrates the discretionary nature of state municipalization policy. Conversely, 1,199 settlements that did not meet the CT criteria nevertheless received statutory recognition, typically reflecting historical municipal status or special circumstances.

The close-to-threshold sample (Panel B) reveals similar patterns on a smaller scale, with 297 settlements meeting CT criteria but not receiving statutory status, and 100 settlements gaining statutory status despite not meeting the criteria. This variation around the thresholds provides the identifying variation for our fuzzy regression discontinuity design, where crossing the CT thresholds substantially increases but does not guarantee statutory recognition.

## 4 Empirical Strategy

In this section, we lay out the identification strategy. The goal is to estimate the causal effect of statutory recognition (municipal governance) on settlement outcomes.

### 4.1 Quasi-random variation from Census Towns

In this section, we show that Census Town (CT) designation leads to a discontinuous increase in the probability of statutory recognition for each of the thresholds. Furthermore, becoming a CT does not directly change local governance as the decision to grant a ULB is made by the state government. So theoretically, we should not expect a direct effect of CT designation on local outcomes coming from the local governance channel unless the settlement is also statutorily recognized. One could argue that CT may be capturing the differences in agglomeration economies or other unobserved characteristics that may be correlated with local outcomes. However, close to the thresholds, these characteristics should be similar on either side of the cutoff. For a country of 1.5 billion people, a settlement with a population of 4,900 and 5,100, or density of 390 and 410, is not likely to be systematically different in terms of agglomeration economies. Furthermore, even though we cannot rule out differences in unobserved characteristics, we can test for balance in observed characteristics (e.g., literacy rate, caste composition) and run placebo tests at pseudo-thresholds to check if there are any discontinuities in outcomes at these points. First, we show that there is a strong first stage relationship between meeting the CT thresholds and statutory recognition. We then use this quasi-random variation to instrument for statutory recognition and identify the Local Average Treatment Effect (LATE) of statutory recognition on local outcomes.

Below we describe how we implement this empirical strategy in practice. Let PiP\_{i}, DiD\_{i}, and NiN\_{i} denote the population, density (per km²), and non-agricultural employment share of settlement ii. Define three binary indicators for meeting the CT thresholds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ZP,i\displaystyle Z\_{P,i} | =1​(Pi5000−1)≥0\displaystyle=1(\frac{P\_{i}}{5000}-1)\geq 0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ZD,i\displaystyle Z\_{D,i} | =1​(Di400−1)≥0\displaystyle=1(\frac{D\_{i}}{400}-1)\geq 0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ZN,i\displaystyle Z\_{N,i} | =1​(Ni0.75−1)≥0\displaystyle=1(\frac{N\_{i}}{0.75}-1)\geq 0 |  |

We define CT eligibility as Zi=ZP,i×ZD,i×ZN,iZ\_{i}=Z\_{P,i}\times Z\_{D,i}\times Z\_{N,i}, which equals 1 if settlement ii meets all three thresholds and 0 otherwise, which we use as an instrument for statutory recognition. The idea is that settlements that meet the CT thresholds are more likely to receive statutory recognition, but the decision to grant statutory recognition is not deterministic based on the CT thresholds alone. Therefore, we can use the variation in CT eligibility to identify the causal effect of statutory recognition on local outcomes.

Next, let S​TiST\_{i} be an indicator for statutory recognition by 2011 i.e. whether settlement ii gets an Urban Local Body (ULB) or not, by 2011. Then, our object of interest is the probability of statutory recognition P​(S​Ti=1|Zi,Xi)P(ST\_{i}=1|Z\_{i},X\_{i}), where XiX\_{i} is a vector of controls. Our data enables us to estimate the following first stage regression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​Ti=π0+π1​Zi+Xi′​β+δs​(i)+εiST\_{i}=\pi\_{0}+\pi\_{1}Z\_{i}+X\_{i}^{\prime}\beta+\delta\_{s(i)}+\varepsilon\_{i} |  | (1) |

where ZiZ\_{i} is CT eligibility in 2001 (instrument), XiX\_{i} is a vector of smooth functions of the running variables and other controls (e.g. ZP,i,ZD,i,ZN,iZ\_{P,i},Z\_{D,i},Z\_{N,i}, literacy, caste shares), and δs​(i)\delta\_{s(i)} are district-level fixed effects.

![Refer to caption](images/treat_prob_pop.png)


(A) Population threshold

![Refer to caption](images/treat_prob_dens.png)


(B) Density threshold

![Refer to caption](images/treat_prob_nonag.png)


(C) Non-agricultural share threshold

Figure 1: First-stage Discontinuities and Statutory Recognition

Figure [1](https://arxiv.org/html/2511.06562v1#S4.F1 "Figure 1 ‣ 4.1 Quasi-random variation from Census Towns ‣ 4 Empirical Strategy ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") presents graphically the first stage of our fuzzy RD design explained in equation [1](https://arxiv.org/html/2511.06562v1#S4.E1 "In 4.1 Quasi-random variation from Census Towns ‣ 4 Empirical Strategy ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") close to the thresholds888We present results upto 100% away from the thresholds. The figure shows binned scatter plots of the probability of statutory status in 2011 against each running variable in 2001. Sub-figure (A) of Figure [1](https://arxiv.org/html/2511.06562v1#S4.F1 "Figure 1 ‣ 4.1 Quasi-random variation from Census Towns ‣ 4 Empirical Strategy ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") shows the relationship between population and statutory recognition. Probability of statutory recognition is positively related to population, which is expected since an increase in population signifies a larger settlement that is more likely to be recognized as a town. Despite this positive relationship, there is a clear discontinuity in the probability of statutory recognition at the population threshold of 0 after normalization. This discontinuity indicates that settlements that just meet the population threshold are significantly more likely to receive statutory recognition than those that just miss it. Sub-figure (B) of Figure [1](https://arxiv.org/html/2511.06562v1#S4.F1 "Figure 1 ‣ 4.1 Quasi-random variation from Census Towns ‣ 4 Empirical Strategy ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") shows the relationship between density and statutory recognition. Similar to population, there is a positive relationship between density and statutory recognition, but the discontinuity at the density threshold, while present, is less pronounced than for population. Sub-figure (C) of Figure [1](https://arxiv.org/html/2511.06562v1#S4.F1 "Figure 1 ‣ 4.1 Quasi-random variation from Census Towns ‣ 4 Empirical Strategy ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") shows the relationship between non-agricultural share and statutory recognition. The relationship is flat, but there is a clear discontinuity at the non-agricultural share threshold. Settlements that just meet the non-agricultural share threshold are more likely to receive statutory recognition than those that just miss it. Overall, these figures provide evidence of a strong first stage relationship between meeting the CT thresholds and statutory recognition, which supports our identification strategy for estimating the causal effect of statutory recognition on local outcomes. In Section [5.1](https://arxiv.org/html/2511.06562v1#S5.SS1 "5.1 First stage: Effects on Statutory Recognition ‣ 5 Results ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project."), we present a table that reports the first-stage coefficient and F-statistics for global and local estimates.

### 4.2 Fuzzy RD with multiple running variables

India’s CT thresholds create jointly-binding rules on three dimensions: population P≥5,000P\geq 5{,}000, density D≥400D\geq 400 per km², and male main non-agricultural share N≥0.75N\geq 0.75. Define running variables as normalized distances to the cutoffs: rP=P/5000−1r\_{P}=P/5000-1, rD=D/400−1r\_{D}=D/400-1, and rN=N/0.75−1r\_{N}=N/0.75-1. Following the logic of multi-cutoff RD, we focus on observations near the cutoffs and develop a frontier using a soft-min functional specification.

![Refer to caption](images/treat_prob_soft_min.png)


Figure 2: Probability of Treatment by Frontier Distance

Figure [2](https://arxiv.org/html/2511.06562v1#S4.F2 "Figure 2 ‣ 4.2 Fuzzy RD with multiple running variables ‣ 4 Empirical Strategy ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") shows the binned scatter plot of the probability of statutory recognition in 2011 against the minimum distance to any of the three thresholds (frontier distance) in 2001. As presented in the figure, there is a clear discontinuity in the probability of statutory recognition at the cutoff (frontier distance = 0). We implement a fuzzy RD design using this frontier distance as the running variable. Specifically, we estimate the following first stage and reduced form equations using observations close to the cutoff.

## 5 Results

### 5.1 First stage: Effects on Statutory Recognition

Table 3: First-stage: Effect of Census-Town Eligibility on Statutory Status

|  |  |  |
| --- | --- | --- |
|  | Global | Local |
| Dependent variable: (Statutory town =1=1) | | |
| Instrument: CT eligibility in 2001 | 0.431∗∗∗ | 0.071∗∗∗ |
|  | (0.0157) | (0.0167) |
| Controls | Yes | Yes |
| District fixed effects | Yes | Yes |
| SEs clustered at district level | Yes | Yes |
| First-stage FF-statistic | 749.43 | 18.05 |
| Partial R2R^{2} of instrument | 0.2522 | 0.0127 |
| Adj. R2R^{2} | 0.3493 | 0.1007 |
| Observations | 502,179 | 37,151 |
| Districts (FE groups) | 619 | 558 |
| Notes: First-stage estimates of statutory recognition on the census-threshold instrument with controls and district fixed effects. Controls include population, density, non-agricultural male workforce share, literacy rate, and caste composition. Standard errors are clustered by district (in parentheses). “Local” restricts to settlements near the 2001 census thresholds (population ≈\approx 5,000, density ≈\approx 400, non-agricultural male workforce share ≈\approx 0.75). The single-IV first-stage FF is t2t^{2} from the clustered specification. | | |
| --- | --- | --- |
| p∗⁣∗∗<0.01{}^{\*\*\*}p<0.01, p∗∗<0.05{}^{\*\*}p<0.05, p∗<0.1{}^{\*}p<0.1. | | |

The first-stage results in Table [3](https://arxiv.org/html/2511.06562v1#S5.T3 "Table 3 ‣ 5.1 First stage: Effects on Statutory Recognition ‣ 5 Results ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") reveal important patterns regarding the strength and validity of our instrumental variable strategy. In the global sample, the instrument exhibits substantial explanatory power with a coefficient of 0.427 (standard error 0.0159) and a first-stage F-statistic of 717.68, well exceeding conventional thresholds for weak instrument concerns. However, this strong statistical relationship may be misleading for causal identification purposes. The global specification, while statistically powerful, is potentially vulnerable to endogeneity. Settlements across the entire population and density spectrum may differ systematically in ways that correlate with both census threshold compliance and subsequent outcomes. For instance, larger settlements may have greater political influence or administrative capacity that simultaneously makes them more likely to meet census criteria and more likely to attract infrastructure investment, regardless of statutory status. The high explanatory power (adjusted R2R^{2} of 0.3233) suggests that the instrument is capturing substantial systematic variation that may not be quasi-random.

In contrast, the local specification of restricting analysis to settlements near the census cutoffs999We use the following restrictions around the thresholds: (i) population ±5000\pm 5000 (ii) density ±400\pm 400 (iii) non-ag male main work share ±0.2\pm 0.2. provides more credible identification despite the smaller coefficient magnitude (0.071) and relatively lower F-statistic (18.81). This specification focuses on settlements that are observationally similar except for small differences in census characteristics that push them just above or below the thresholds. The lower adjusted R2R^{2} (0.0581) and partial R2R^{2} of instrument (0.0130) indicate that we are capturing variation that is more plausibly exogenous, as settlements just above and below the cutoffs should be similar in unobservable characteristics in the absence of treatment, as long as no manipulation occurs.

The F-statistic of 18.81 for our local specification is above the conventional threshold of 16.38 for strong instruments in the just-identified case (stock1997testing) and well above the critical value of 8.96 for 15% maximal IV bias (stock2002testing), suggesting the instrument maintains reasonable strength for our identification strategy. The local estimates thus provide our preferred specification for downstream analysis, offering a more credible foundation for interpreting the causal effects of statutory recognition on settlement outcomes.

### 5.2 Main effects on outcomes

We next present 2SLS estimates of the effect of statutory recognition on settlement outcomes. We group outcomes into categories most relevant to local public goods and services: education, health, financial access, and community infrastructure.

##### Education.

Table 4: Effect of Local Urban Governance on School Provision

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dependent variable: Number of government schools | | |
|  | Primary | Middle | Secondary |
| Effect of ULB | 13.85\*\*\* | 7.71\*\*\* | 5.01\*\*\* |
|  | (4.03) | (2.27) | (1.31) |
| Controls | Yes | Yes | Yes |
| District FE | Yes | Yes | Yes |
| Observations | 37,140 | 37,096 | 37,145 |

* •

  Notes: Table reports two-stage least squares estimates where the instrument for ULB status is Census Town classification at the thresholds used in the definition of census towns. All specifications include controls for population, density, non-agricultural male workforce share, literacy, and caste composition, as well as district fixed effects101010state-level fixed effects yielded similar results.. Robust standard errors clustered at the district level are reported in parentheses.
* •

  Significance levels: \*\*\* p<0.01p<0.01, \*\* p<0.05p<0.05, \* p<0.1p<0.1.

Table [4](https://arxiv.org/html/2511.06562v1#S5.T4 "Table 4 ‣ Education. ‣ 5.2 Main effects on outcomes ‣ 5 Results ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") presents the estimated effects of local urban governance on educational infrastructure provision. The results demonstrate substantial positive impacts across all levels of schooling. Statutory recognition leads to an increase of 13.54 additional primary schools (SE = 3.94), 7.76 additional middle schools (SE = 2.24), and 5.01 additional secondary schools (SE = 1.31). All estimates are statistically significant at the 1% level, with robust standard errors clustered at the district level.
These findings reveal important patterns in how urban governance affects educational provision. The largest absolute effect occurs at the primary level, which is consistent with primary education being a foundational service that local governments prioritize. In India, primary schools are the least regulated and easiest to establish, requiring modest capital investment and fewer students to justify operation, whereas these requirements increase substantially for middle and secondary schools. The magnitude of effects decreases as we move up the educational ladder, with middle and secondary schools showing progressively smaller impacts. This gradient may reflect not only the differential regulatory barriers and capital requirements across school levels, but also differences in administrative priorities and demand patterns. Nonetheless, the fact that all three levels show significant positive effects suggests that urban governance structures facilitate comprehensive improvements in educational infrastructure at all levels, potentially leading to better educational outcomes for residents in newly urbanized areas.

##### Health.

Table 5: Effect of Local Urban Governance on Hospital Provision

|  |  |  |
| --- | --- | --- |
|  | Dependent variable | |
|  | All hospitals | Family welfare centers |
| Effect of ULB | 2.53\*\*\* | 2.99\*\*\* |
|  | (0.69) | (0.88) |
| Controls | Yes | Yes |
| District FE | Yes | Yes |
| Observations | 37,074 | 37,074 |

* •

  Notes: Two-stage least squares estimates where the endogenous regressor is ULB status, the instrument is Census Town status at the thresholds used in the official definition. All specifications include controls for population, density, literacy, caste composition, and economic activity, as well as district-level fixed effects111111State-level fixed effects yielded similar results.. Robust standard errors clustered at the district level are in parentheses.
  Significance: \*\*\* p<0.01p<0.01, \*\* p<0.05p<0.05, \* p<0.1p<0.1.

Table [5](https://arxiv.org/html/2511.06562v1#S5.T5 "Table 5 ‣ Health. ‣ 5.2 Main effects on outcomes ‣ 5 Results ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") shows the effects of statutory recognition on health infrastructure. The estimates indicate that becoming a statutory town leads to an increase of 2.52 additional hospitals and 3.04 additional family welfare centers, both statistically significant at the 1% level. These results suggest that urban local governance significantly enhances health service availability, potentially improving access to medical care for residents.

##### Financial Access.

Table 6: Effect of Local Urban Governance on Financial Access

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dependent variable | | |
|  | Private banks | Cooperative banks | Agricultural credit societies |
| Effect of ULB | 15.23\*\*\* | 2.23\*\*\* | 2.16\*\*\* |
|  | (3.97) | (0.89) | (0.63) |
| Controls | Yes | Yes | Yes |
| District FE | Yes | Yes | Yes |
| Observations | 37,062 | 37,060 | 37,085 |

* •

  Notes: Two-stage least squares estimates where the endogenous regressor is ULB status, the instrument is Census Town status at the thresholds used in the official definition. All specifications include controls for population, density, literacy, caste composition, and economic activity, as well as district-level fixed effects121212State-level fixed effects yielded similar results.. Robust standard errors clustered at the district level are in parentheses; 95% confidence intervals in brackets. Significance: \*\*\* p<0.01p<0.01, \*\* p<0.05p<0.05, \* p<0.1p<0.1.

Table [6](https://arxiv.org/html/2511.06562v1#S5.T6 "Table 6 ‣ Financial Access. ‣ 5.2 Main effects on outcomes ‣ 5 Results ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") presents the estimated effects of statutory recognition on financial infrastructure provision. The results show substantial positive impacts across all types of financial institutions. Statutory recognition leads to an increase of 15.39 additional private banks, 2.34 additional cooperative banks, and 2.24 additional agricultural credit societies. All estimates are statistically significant at the 1% level with robust standard errors clustered at the district level. These findings suggest that formal urban governance significantly enhances financial infrastructure access, with the largest effects observed for private banking services, potentially improving financial inclusion and economic development opportunities for residents.

##### Community Access.

Table 7: Effect of Local Urban Governance on Community Access

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Dependent variable | | | |
|  | Public libraries | Public reading rooms | Cinema halls | Sports infrastructure |
| Effect of ULB | 1.04\*\* | 1.44\*\*\* | 0.83\* | -5.69\*\*\* |
|  | (0.50) | (0.63) | (0.49) | (1.46) |
| Controls | Yes | Yes | Yes | Yes |
| District FE | Yes | Yes | Yes | Yes |
| Observations | 37,144 | 37,144 | 37,144 | 37,143 |

* •

  Notes: Two-stage least squares estimates where the endogenous regressor is ULB status, the instrument is Census Town status at the thresholds used in the official definition. All specifications include controls for population, density, literacy, caste composition, and economic activity, as well as district-level fixed effects131313State-level fixed effects yielded similar results.. Robust standard errors clustered at the district level are in parentheses. Significance: \*\*\* p<0.01p<0.01, \*\* p<0.05p<0.05, \* p<0.1p<0.1.

Table [7](https://arxiv.org/html/2511.06562v1#S5.T7 "Table 7 ‣ Community Access. ‣ 5.2 Main effects on outcomes ‣ 5 Results ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") presents the estimated effects of statutory recognition on community infrastructure and access. The results show significant positive impacts on most community facilities. Statutory recognition leads to an increase of 1.07 additional public libraries (significant at the 5% level), 1.44 additional public reading rooms (significant at the 1% level), and 0.83 additional cinema halls (significant at the 10% level). Interestingly, the estimate for sports infrastructure is negative and significant at the 1% level, indicating a decrease of 5.69 facilities. This negative effect may reflect the spatial constraints and land-use tradeoffs inherent in urban development. As settlements formalize into statutory towns, open spaces previously used for sports facilities (such as playgrounds or fields) may be repurposed for higher-priority urban infrastructure like schools, hospitals, banks, or residential development. Moreover, municipal planning often consolidates multiple informal sports venues into fewer, more formal facilities, resulting in a net reduction in the count of such infrastructure even as quality or accessibility may improve. Overall, these findings suggest that formal urban governance enhances access to cultural and educational community facilities, though the transition may involve restructuring of certain types of infrastructure, particularly those requiring substantial land area.

### 5.3 Robustness and validity

#### 5.3.1 Exclusion Restriction Assumption

A key assumption for the validity of our IV strategy is that the instrument (Census Town eligibility) affects outcomes only through its impact on statutory recognition, and not through other channels. To assess this exclusion restriction, we conduct robustness checks. First, for areas that remained non-statutory towns, we check the effects of census eligibility on outcomes to see if any direct effects exist absent statutory recognition. Second, we check for balance in baseline covariates around the thresholds to ensure that settlements just above and below the cutoffs are similar in observable characteristics (see Appendix).

Table 8: Reduced-Form Effects Comparison: Main Estimates vs Census Town Eligibility Effect on Outcomes for Non-Statutory Towns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Main 2SLS estimate | | Direct Effect | |
| Outcome | Estimate | SE | Estimate | SE |
| Education | | | | |
| Primary schools | 13.85\*\*\* | (4.03) | 0.81\*\*\* | (0.13) |
| Middle schools | 7.71\*\*\* | (2.27) | 0.51\*\*\* | (0.10) |
| Secondary schools | 5.01\*\*\* | (1.31) | 0.30\*\*\* | (0.06) |
| Health | | | | |
| All hospitals | 2.53\*\*\* | (0.69) | 0.16\*\*\* | (0.04) |
| Family welfare centers | 2.99\*\*\* | (0.88) | 0.21\*\*\* | (0.04) |
| Financial access | | | | |
| Private banks | 15.23\*\*\* | (3.97) | 0.92\*\*\* | (0.11) |
| Cooperative banks | 2.23\*\*\* | (0.89) | 0.14\*\*\* | (0.05) |
| Agricultural credit societies | 2.16\*\*\* | (0.63) | 0.12\*\*\* | (0.04) |
| Community infrastructure | | | | |
| Public libraries | 1.04\*\* | (0.50) | 0.10\*\*\* | (0.03) |
| Public reading rooms | 1.44\*\*\* | (0.63) | 0.13\*\*\* | (0.04) |
| Cinema halls | 0.83\* | (0.49) | 0.07\*\* | (0.03) |
| Sports infrastructure | −-5.69\*\*\* | (1.46) | −-0.38\*\*\* | (0.06) |

* •

  Notes: The first two columns report the main 2SLS estimates from Tables [4](https://arxiv.org/html/2511.06562v1#S5.T4 "Table 4 ‣ Education. ‣ 5.2 Main effects on outcomes ‣ 5 Results ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.")–[7](https://arxiv.org/html/2511.06562v1#S5.T7 "Table 7 ‣ Community Access. ‣ 5.2 Main effects on outcomes ‣ 5 Results ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project."), showing the effect of statutory ULB status instrumented by Census Town eligibility. The last two columns report direct effects of Census Town eligibility on outcomes for the subsample of settlements that remained non-statutory i.e. testing whether the instrument has direct effects on outcomes absent statutory recognition. All specifications include controls for population, density, literacy, caste composition, and economic activity, as well as district-level fixed effects. Robust standard errors clustered at the district level are in parentheses. Significance: \*\*\* p<0.01p<0.01, \*\* p<0.05p<0.05, \* p<0.1p<0.1.

Table [8](https://arxiv.org/html/2511.06562v1#S5.T8 "Table 8 ‣ 5.3.1 Exclusion Restriction Assumption ‣ 5.3 Robustness and validity ‣ 5 Results ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") presents evidence on the exclusion restriction assumption by comparing the main 2SLS estimates with reduced-form effects of Census Town eligibility among settlements that remained non-statutory. While the reduced-form estimates are statistically significant and consistently positive (or negative for sports infrastructure) across all outcomes, their magnitudes are substantially smaller than the main IV estimates. For example, the effect on primary schools is 0.81 (SE = 0.13) in the non-statutory sample compared to 13.85 (SE = 4.03) in the main specification, and the effect on private banks is 0.92 (SE = 0.11) versus 15.23 (SE = 3.97). The relative magnitudes thus provide support for the validity of our instrumental variable strategy, as the direct effects are an order of magnitude smaller than the effects mediated through actual municipalization.

## 6 Conclusion

This paper provides causal evidence that statutory municipalization – the extension of urban local governance to a settlement – leads to some improvements in local public goods at India’s urbanizing fringe. Using a novel multi-threshold RD design based on the Census Town criteria, we isolate the effect of formal urban status from underlying confounding factors such as population growth, density and economic changes. The results indicate that when a village becomes a town (in administrative terms), it experiences gains in infrastructure: more schools, health centers, banks, and other facilities emerge, relative to similar villages that remain under rural governance. These findings suggest that institutions and governance structures do play a role in shaping development outcomes, even at the very local level. However, the magnitudes of the effects are up for interpretation. While statistically significant, the increases in infrastructure may be considered modest or substantial, depending on the context and baseline levels of local services.

The policy implications are twofold. First, there may be benefits to timely municipalization of emerging urban areas. Our paper shows that delaying the recognition of de facto urban settlements can mean missed opportunities for infrastructure investment and service delivery. If urban local bodies indeed facilitate better outcomes, then proactively converting eligible large villages into statutory towns, especially the villages that are already urban as per the Census Town criteria, and providing them fiscal support and governance framework, could help improve their overall infrastructure. Second, our results highlight the importance of state capacity and support for new ULBs. Simply declaring a settlement as a municipality is not a panacea; the improvements we document likely come from a combination of local initiatives and higher-level funding and oversight. State governments could enhance the benefits of municipalization by ensuring that newly formed ULBs receive adequate resources, technical assistance, and training to fulfill their functions. Strengthening local governance – through measures like capacity-building programs for municipal officials or incentivizing revenue generation – could further amplify the positive impacts on public goods.

Our study also opens avenues for future research. One extension would be to examine longer-term and broader outcomes of municipalization. Due to data limitations, we focused on infrastructure inputs as of 2011. It would be valuable to see if these translate into improved local public goods for residents over time. For example, higher school enrollment or better health indicators in newly urbanized areas. Household survey data, such as subsequent rounds of NFHS, could be linked to our design to assess impacts on education, health, and income. Another avenue is to explore the fiscal side: how do the finances of local bodies change at the threshold? Are municipalities able to raise more revenue or attract more investment? Additionally, the heterogeneity across states hints at interesting political economy dynamics – understanding why some states are reluctant to create new towns, possibly to avoid sharing revenue or due to political patronage networks, could inform strategies to overcome those barriers. Our findings underscore that urban local governance matters: even in a context where local governments often have limited capacity, formally bringing a settlement into the urban administrative fold has certain measurable benefits for the community. As countries throughout the developing world continue to urbanize, ensuring that institutional change keeps pace with demographic change will be crucial for sustainable long-term development.

## Data and Code Availability

Data. All data used are public.

Code & replication. A complete replication package (scripts to build the running variables, construct outcomes, and reproduce figures/tables) will be submitted with the manuscript and deposited in a stable repository (e.g., Harvard Dataverse, GitHub) upon request.

## Declaration of Competing Interests and Funding

The author declares no competing interests. No external funding was received for this research.

## Appendix

### Density Plots and McCrary Test

We conduct density tests around the statutory recognition thresholds to assess the validity of our RD design. Specifically, we implement the mccrary2008manipulation test for manipulation of the running variable, which examines the continuity of the density of the running variable at the cutoff.

![Refer to caption](images/rd_density_plots.png)


Figure 3: Density plots of CT-definition variables and thresholds

The mccrary2008manipulation density test formally assesses whether there is evidence of manipulation of the running variable around the cutoff. The test estimates the density of the running variable separately on each side of the threshold and tests whether there is a discontinuity in the density at the cutoff. A significant discontinuity would suggest strategic sorting around the threshold, which would violate the identifying assumptions of the RD design.

Table [9](https://arxiv.org/html/2511.06562v1#Ax1.T9 "Table 9 ‣ Density Plots and McCrary Test ‣ Appendix ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") presents the results of the mccrary2008manipulation test for each of our three running variables used to define census town status. For population in 2001 (cutoff at 5,000), the test statistic is 0.754 with a p-value of 0.451. For population density in 2001 (cutoff at 400 persons per km²), the test statistic is 0.245 with a p-value of 0.807. For the share of non-agricultural male workers (cutoff at 0.75), the test statistic is −1.101-1.101 with a p-value of 0.271. In all three cases, we fail to reject the null hypothesis of no discontinuity in the density at conventional significance levels. This provides reassuring evidence that there is no systematic manipulation of these running variables around the statutory thresholds.

Table 9: McCrary Density Tests at CT Thresholds

| Running Variable | Cutoff | T-statistic | P-value |
| --- | --- | --- | --- |
| Population (2001) | 5,000 | 0.754 | 0.451 |
| Population Density (2001) | 400 | 0.245 | 0.807 |
| % Non-Agricultural Male Workers (2001) | 0.75 | −1.101-1.101 | 0.271 |

* •

  Notes: This table reports results from the mccrary2008manipulation manipulation test which examines whether there is a discontinuity in the density of the running variable at the statutory threshold. The T-statistic tests the null hypothesis of no discontinuity. All tests use a triangular kernel with bandwidth selection and jackknife variance estimation. P-values greater than 0.10 indicate no evidence of manipulation at conventional significance levels.

### Location of ULBs

We map the settlements with Urban Local Bodies (ULBs) in India and present them below in Figure [4](https://arxiv.org/html/2511.06562v1#Ax1.F4 "Figure 4 ‣ Location of ULBs ‣ Appendix ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.").

![Refer to caption](images/ulb_plot.png)


Figure 4: Urban Local Bodies (ULBs) in India

#### Balance Checks

To assess the validity of our regression discontinuity design, we examine whether settlements just below and just above the Census Town thresholds are comparable on observable characteristics measured in 2001. Table [10](https://arxiv.org/html/2511.06562v1#Ax1.T10 "Table 10 ‣ Balance Checks ‣ Location of ULBs ‣ Appendix ‣ Does Urban Local Governance Matter? Evidence from IndiaAcknowledgements: I am grateful to SHRUG, for making their data publicly available. I thank David Brasington, Gary Painter, Olivier Parent, Clemens Pilgram, and others for helpful comments and suggestions. All errors are my own. No external funding was received for this project.") presents balance tests for key demographic and economic variables across both the full sample (Panel A) and the close-to-threshold sample (Panel B). The variables include log population, log density, share of non-agricultural male workers, literacy rate, main worker rate, and shares of Scheduled Caste and Scheduled Tribe populations.

Table 10: Balance Checks: 2001 variables by CT Status

|  |  |  |  |
| --- | --- | --- | --- |
| Variable | Non-CT | CT | N |
| Panel A: Full Sample | | | |
| Log Population | 6.55 | 9.84 | 502,179 |
|  | (1.23) | (0.87) |  |
| Log Density | 5.69 | 7.77 | 502,179 |
|  | (1.45) | (1.12) |  |
| Non-Ag Male Workers | 0.26 | 0.90 | 502,179 |
|  | (0.24) | (0.15) |  |
| Literacy Rate | 0.47 | 0.67 | 502,179 |
|  | (0.18) | (0.12) |  |
| Main Worker Rate | 0.32 | 0.28 | 502,179 |
|  | (0.12) | (0.08) |  |
| SC Share | 0.17 | 0.13 | 502,179 |
|  | (0.21) | (0.15) |  |
| ST Share | 0.16 | 0.04 | 502,179 |
|  | (0.31) | (0.15) |  |
| Panel B: Close-to-Threshold Sample | | | |
| Log Population | 6.42 | 8.85 | 37,151 |
|  | (1.18) | (0.92) |  |
| Log Density | 5.60 | 6.37 | 37,151 |
|  | (1.38) | (1.25) |  |
| Non-Ag Male Workers | 0.71 | 0.83 | 37,151 |
|  | (0.18) | (0.14) |  |
| Literacy Rate | 0.55 | 0.63 | 37,151 |
|  | (0.16) | (0.13) |  |
| Main Worker Rate | 0.27 | 0.32 | 37,151 |
|  | (0.11) | (0.09) |  |
| SC Share | 0.19 | 0.14 | 37,151 |
|  | (0.22) | (0.17) |  |
| ST Share | 0.12 | 0.05 | 37,151 |
|  | (0.27) | (0.18) |  |

Notes: This table presents mean characteristics in 2001 for settlements that did not meet Census Town (CT) criteria versus those that did. Standard deviations are reported in parentheses below means. Panel A shows the full sample; Panel B restricts to settlements close to the CT thresholds (within specified bandwidth). All variables are measured in 2001, prior to potential statutory recognition by 2011.

As expected in the full sample (Panel A), settlements meeting CT criteria differ substantially from those that do not—they are considerably larger, denser, more economically non-agricultural, and have higher literacy rates. However, when we restrict attention to the close-to-threshold sample (Panel B), these differences narrow substantially. While some gaps remain—particularly in population and density, which are among the threshold criteria themselves—the key observation is that settlements just above and below the thresholds are much more similar than the full sample comparison would suggest. This pattern is consistent with local randomization around the threshold and supports the identifying assumption that, conditional on being close to the CT cutoffs, assignment to CT status is quasi-random with respect to unobserved determinants of public goods provision.