---
authors:
- Janne Rotter
- William Bailkoski
doc_id: arxiv:2510.15509v1
family_id: arxiv:2510.15509
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'AI Adoption in NGOs: A Systematic Literature Review'
url_abs: http://arxiv.org/abs/2510.15509v1
url_html: https://arxiv.org/html/2510.15509v1
venue: arXiv q-fin
version: 1
year: 2025
---


1st Janne Rotter
  
Universitat Pompeu Fabra
  
Barcelona, Spain
  
jannedavid.rotter01@estudiant.upf.edu
  
ORCID:
 [0009-0001-3520-958X](https://orcid.org/0009-0001-3520-958X)
  
2nd William Bailkoski
  
Universitat Pompeu Fabra
  
Barcelona, Spain
  
william.bailkoski01@estudiant.upf.edu
  
ORCID:
 [0009-0009-0744-6228](https://orcid.org/0009-0009-0744-6228)

Abstract –
AI has the potential to significantly improve how NGOs utilize their limited resources for societal benefits, but evidence about how NGOs adopt AI remains scattered. In this study, we systematically investigate the types of AI adoption use cases in NGOs and identify common challenges and solutions, contextualized by organizational size and geographic context. We review the existing primary literature, including studies that investigate AI adoption in NGOs related to social impact between 2020 and 2025 in English. Following the PRISMA protocol, two independent reviewers conduct study selection, with regular cross-checking to ensure methodological rigour, resulting in a final literature body of 65 studies. Leveraging a thematic and narrative approach, we identify six AI use case categories in NGOs — Engagement, Creativity, Decision-Making, Prediction, Management, and Optimization — and extract common challenges and solutions within the Technology–Organization–Environment (TOE) framework. By integrating our findings, this review provides a novel understanding of AI adoption in NGOs, linking specific use cases and challenges to organizational and environmental factors. Our results demonstrate that while AI is promising, adoption among NGOs remains uneven and biased towards larger organizations. Nevertheless, following a roadmap grounded in literature can help NGOs overcome initial barriers to AI adoption, ultimately improving effectiveness, engagement, and social impact.
  
  
This paper has been submitted to ACM JCSS for review (October 2025).

Keywords - Artificial Intelligence, Surveys and Overviews, AI use cases, Non-governmental organizations (NGOs), AI for
Good, Technology Adoption, IT governance, Enterprise information systems

## ntroduction

Artificial intelligence (AI) is quickly reshaping the way organizations gather information, make decisions, and provide services. This trend in adoption is reflected in the forecast for the global AI market, which is expected to reach $1.81 trillion by 2030, with a projected compound annual growth rate (CAGR) of 35.9% between 2025 and 2030 [[1](https://arxiv.org/html/2510.15509v1#bib.bibx1)]. While this widespread adoption in the private sector is getting increased attention, the parallel progression in the non-profit and charity sector has seen significantly less focus. Considering NGOs follow missions that increase social good, such as education, disaster relief, or democratization, it is in the public interest to ensure their work is as effective as possible.

For NGOs, AI has the potential to act as a catalyst, helping them improve efficiency, raise their public profile, and strengthen the reach of their initiatives. Among other applications, it can streamline routine tasks, offer data-driven guidance for program development, and support more focused and effective fundraising and advocacy efforts. For example, AI can be used to support NGOs in targeting donors more effectively and gaining insights into their likely contributions, potentially reducing campaign expenses and boosting fundraising outcomes [[2](https://arxiv.org/html/2510.15509v1#bib.bibx2)]. However, NGOs operate under a distinct set of constraints that affect their adoption journey. They often have to deal with tight budgets and an organizational culture that tends to be mission-centric rather than technology-driven [[3](https://arxiv.org/html/2510.15509v1#bib.bibx3)]. This creates a clear tension: Although NGOs face growing pressure to prove their effectiveness in the face of economic uncertainty and competition for funding, their unique financial and organizational limitations often prevent them from embracing the very technologies that could help them meet these demands. This tension between AI’s promised advantages and the practical limitations faced by NGOs represents a critical concern.

Although AI adoption in the non-profit sector is both highly important and shaped by distinctive dynamics, current research remains scattered and lacks a broad synthesis.
Much of the existing research consists of isolated case studies or reports that either focus on a single country or a specific project. This can paint a biased and skewed picture of the overarching systematic dynamics of AI adoption in NGOs. While some systematic reviews in this field exist they either focus on narrow geographic contexts [[4](https://arxiv.org/html/2510.15509v1#bib.bibx4)], primarily emphasize ethical considerations [[5](https://arxiv.org/html/2510.15509v1#bib.bibx5)], or concentrate on government and for-profit organizations [[6](https://arxiv.org/html/2510.15509v1#bib.bibx6), [7](https://arxiv.org/html/2510.15509v1#bib.bibx7)]. Therefore, a systematic review is needed that fills this research gap and synthesize the fragmented literature into a broad and nuanced summary that addresses how AI is adopted by NGOs. Specifically, there is a notable absence of systematic analysis that compares AI uses and barriers across different NGO sizes and geographic contexts, which would provide a more detailed and generalizable perspective.

To guide this research, we focused on two core research questions:

* •

  RQ1. In what ways is AI primarily utilized by NGOs and how does this differ based on size and location?
* •

  RQ2. What challenges and solutions are found in the literature about the adoption of AI in NGOs and how are these dynamics influenced by size and location?

In order to address these questions we draw on peer-reviewed studies as well as high-quality grey literature published in English between 2020 and 2025, ensuring a solid and up-to-date evidence base for the analysis.

This review makes three main contributions. For one it draws on the fragmented literature base to arrive at a comprehensive understanding of how AI is adopted and used by NGOs. Secondly, it investigates how AI adopting differs across different organizational contexts such as NGO size and geographic location. Finally, it also identifies emerging challenges and offers groundwork for practical guidance regarding NGOs’ highly individual journeys to technological adoption. The remainder of the paper is organized as follows: The next section outlines the theoretical background, followed by the methodology for conducting the systematic review, the results of the narrative and thematic synthesis, a discussion of the findings with implications and directions for future research, and finally, the conclusion.

## heoretical Background

For the purpose of this review AI is defined in a functional and applied sense, referring to computational systems designed to perform tasks that typically require human intelligence [[8](https://arxiv.org/html/2510.15509v1#bib.bibx8)]. This encompasses but is not limited to tasks such as data analysis, predictive modelling, pattern recognition, and content generation through machine learning (ML) and large language models (LLMs). Throughout this paper the term NGO is used broadly for the non-profit sector, including international NGOs, local community-based organizations, and other civil society groups and charities. It acknowledges that this sector is not a singular homogeneous entity but encompasses a diverse set of mission-driven organizations that can vary significantly in their structure, resources, purpose and operational context [[9](https://arxiv.org/html/2510.15509v1#bib.bibx9)].

To provide a robust analytical structure for this review, the Technology-Organization-Environment (TOE) framework will serve as the primary conceptual lens.
This framework introduced by Tornatzky et al. [[10](https://arxiv.org/html/2510.15509v1#bib.bibx10)] provides a powerful tool to analyse technology adaptation and implementation on an organizational-level based on three key contexts: The technology context describes what technical tools are currently used within the organization and are potentially available to it. Additionally, it incorporates the characteristics of the technology itself, including its complexity, perceived usefulness, and compatibility with existing systems. Secondly, the organizational context includes the internal characteristics of the organization, such as its size, management structure, resource availability, and culture. Thirdly, the environment context describes the external environment in which the organization operates, including donor expectations, the regulatory landscape, and local infrastructure.

While the framework is often viewed as generic and broad [[11](https://arxiv.org/html/2510.15509v1#bib.bibx11)], it still remains the gold-standard for analysis of technology adoption on an organizational level. Furthermore, it is particularly well-suited for this study because its three dimensions align directly with the research questions, allowing for a holistic and structured analysis of the challenges faced by NGOs in the context of organizational size and geographic context. In addition to TOE, the Diffusion of Innovations (DOI) theory [[12](https://arxiv.org/html/2510.15509v1#bib.bibx12)] is used as a secondary lens to understand the current state of AI adoption within the non-profit sector. DOI helps to explain why NGOs, as a social system, might be lacking behind in technology adoption compared to the private sector. It highlights that adoption follows an S-shaped curve influenced by the varying readiness of different adopter groups. It is commonly seen as being closely related to TOE and thus methodologically fit for this review [[13](https://arxiv.org/html/2510.15509v1#bib.bibx13)].

This systematic review will utilize a combination of narrative and thematic synthesis approaches, which is particularly well suited given the heterogeneous nature of the available literature, which includes both quantitative survey data and qualitative case studies. This data heterogeneity also makes a meta-analysis unfit in this context. The narrative synthesis approach goes beyond a simple summary but tells a structured and thematic story of the literature, that allows for identifying patterns and integrating diverse types of evidence into a coherent understanding of the topic. This method will use the TOE and DOI frameworks as scaffolding for guidance and will be thematically oriented at the research question. This approach ensures that the findings are well organized and rigorous.

Given the limited structured syntheses on AI adoption within NGOs, especially when compared to the private sector, this study seeks to address that gap and offer a cohesive understanding of the topic.

## ethodology

![Refer to caption](SLR_Process.png)


Figure 1: Pipeline for this SLR. Note that this graphic is inspired by [[14](https://arxiv.org/html/2510.15509v1#bib.bibx14)]

This study explores and aims to gain a comprehensive understanding of the adoption and usage of AI by a diverse set of NGOs on a global scale from the published research literature. Our
research was guided by the two research questions defined in the introduction.
We conducted a systematic literature review (SLR) following the PRISMA 2020 guidelines proposed by Page et al. [[15](https://arxiv.org/html/2510.15509v1#bib.bibx15)]. This framework is widely adopted in contemporary literature and is generally regarded as best practice for conducting SLRs. It offers a comprehensive checklist to guide the design, execution, and reporting of systematic reviews, ensuring rigour and transparency throughout the research process.

Additionally, we utilized the SPIDER framework developed by Cooke et al. [[16](https://arxiv.org/html/2510.15509v1#bib.bibx16)]. This search strategy tool improves over the PICO paradigm [[17](https://arxiv.org/html/2510.15509v1#bib.bibx17)] by offering improved efficiency for researchers, thereby saving them valuable time by eliminating irrelevant articles. It is additionally developed to particularly fit qualitative and mixed-methods research, something highly desirable in the context of this SLR.

The components of the SPIDER framework in this review are the following:

* •

  Sample: Non-Governmental Organizations (NGOs), Non-Profit Organizations (NPOs), and international aid agencies.
* •

  Phenomenon of Interest: The utilization and application of Artificial Intelligence
* •

  Design: Empirical studies, case studies, and technical reports documenting AI applications
* •

  Evaluation: The evaluation will focus on the social impact, efficiency gains, and operational improvements, as well as the associated ethical and practical considerations.
* •

  Research Type: Qualitative and quantitative research, observational studies, and case studies, recognizing that a randomized controlled trial design is highly unlikely in this field.

Before conducting the full systematic search, we carried out a pilot study to test and refine our search strategy and eligibility criteria.
The initial search queries were run in Google Scholar and OpenAlex, and the first 40 results from each database were screened against the preliminary eligibility criteria.
This step revealed that while the core concepts of ”artificial intelligence” and ”NGOs” retrieved relevant literature, several irrelevant results were also captured,
particularly in domains unrelated to the social sector (e.g. AI for business analytics or government applications).
Based on insights from the pilot study, the search strings were iteratively refined in several ways. First, additional synonyms and related concepts (e.g. charity, NLP) were incorporated to broaden coverage. Second, certain terms were restricted to the title or abstract fields to increase precision. In particular, the term ’NGO’ was limited to the title and abstract field, since ’Ngo’ is also a common Vietnamese surname that could otherwise introduce irrelevant results. Third, the use of wildcards was applied more selectively to increase retrieval accuracy and reduce irrelevant matches. Fourth, the set of application-related terms was expanded by including additional fields synonymous with social impact. Finally, the eligibility criteria regarding population and context were slightly clarified to ensure consistency and alignment with the objectives of this review.

After refinement, the pilot search produced a substantially higher proportion of relevant hits (approximately 49% vs. 23% in the first iteration) as assessed by title and abstract,
which confirmed that the strategy was sufficiently sensitive and specific to be used for the main review.
The initial and finalized search strings are documented in Appendix [A](https://arxiv.org/html/2510.15509v1#A1 "Appendix A Search Queries ‣ AI Adoption in NGOs: A Systematic Literature Review"). Generally they are derived from the Sample, Phenomenon of Interest and Evaluation definitions given in the SPIDER framework. Please note that Design and Research Type are dealt with by the eligibility criteria.

### 3.1  Primary Search

In accordance to the findings by Martin et al. [[18](https://arxiv.org/html/2510.15509v1#bib.bibx18)] at least two databases were used for the primary search. Due to the relative novelty of the field the two databases with the highest coverage, Google Scholar and OpenAlex [[19](https://arxiv.org/html/2510.15509v1#bib.bibx19)] were chosen. Additionally, Scopus was used.

To mitigate publication bias, a thorough search of grey literature was conducted [[20](https://arxiv.org/html/2510.15509v1#bib.bibx20)]. This included technical reports, white papers from NGOs, and government reports that may not be indexed in academic databases. These documents were collected through Relief Web, a repository featuring official UN and NGO reports. All of the findings are included or excluded according to the same criteria as the white literature.

In the context of this SLR the eligibility criteria were the following:

* •

  Population: The study must involve a Non-Governmental Organization (NGO), Non-Profit Organization (NPO), charity, or a similar civil society organization. Studies focused on for-profit companies or government agencies including UN bodies are excluded.
* •

  Intervention: The study must detail the use or application of AI, machine learning (ML), natural language processing (NLP), or other closely related AI technologies.
* •

  Context: Studies must be related to the social impact sector. This could include humanitarian aid, social services, environmental conservation, public health, or human rights.
* •

  Study Design: The review will utilize primary research, such as case studies, empirical studies, or project reports. Secondary publications like editorials, commentaries, and other literature reviews are ignored to avoid redundant information and potential bias.
* •

  Research Type: Included studies are qualitative as well as quantitative research. Master theses and PhD Dissertations are excluded to ensure a minimum quality standard and mitigate the issue of accessibility and consistency between different databases.
* •

  Publication Dates & Language: The review investigates the time frame from the emergence of modern AI to the present to capture the state-of-the-art in this rapidly evolving field (2020–2025). The review is limited to publications in English, as this is the only languages in which the contributing authors all have sufficient proficiency in to accurately interpret, assess, and synthesize the content. Including other languages could compromise the reliability of data extraction and analysis.
* •

  Practical Considerations: Literature is excluded if the full paper is unavailable or not freely available online under Universitat Pomepu Fabra literature agreements.

All of these criteria were evaluated and slightly refined as part of the pilot study to ensure relevance and consistency. For an exact overview of the number of included studies and reasons for exclusion, please refer to Figure [2](https://arxiv.org/html/2510.15509v1#S3.F2 "Figure 2 ‣ 3.3 Secondary Search ‣ ethodology ‣ AI Adoption in NGOs: A Systematic Literature Review").

### 3.2  Selection Process

Following the recommendations of Pigott et al. [[21](https://arxiv.org/html/2510.15509v1#bib.bibx21)], the screening process was carried out in sequential steps:

1. 1.

   Duplicate citations from different databases were removed.
2. 2.

   The titles and abstracts were screened for relevance by two independent researchers to reduce bias and increase reliability and consistency. Reviewers were not blinded to the journal or author information. Any discrepancies in the screening were resolved through discussion until a consensus was reached. If a consensus could not be reached, a third person (a mutually agreed-upon arbitrator) made the final decision. Only studies that clearly did not meet one or more of the eligibility criteria were removed.
3. 3.

   The remaining articles underwent full-text screening. In this stage remaining literature was reviewed in detail against the full set of eligibility criteria to ensure the study design, population, and intervention align with this review’s scope.

Although the review was conducted by only two authors, which could introduce a slight risk of bias, several measures were implemented to minimize this risk. Both authors worked independently during study selection, data extraction, and coding, and methodological rigour was maintained by adhering to a pre-defined review protocol found under this [Open Science Framework (OSF) link](https://osf.io/a2357/?view_only=7120b178719540608dc97cd2a178ceff). Regular discussions and cross-checking ensured consistency and transparency, helping to mitigate potential biases and strengthen the reliability of the findings. Inter-annotator reliability was assessed using Cohen’s Kappa. Agreement was substantial for Google Scholar (κ\kappa = 0.76), Open Alex (κ\kappa = 0.70) and Scopus (κ\kappa = 0.72) and perfect for ReliefWeb (κ\kappa = 1.00). Overall Cohen’s Kappa was also substantial (κ\kappa = 0.74).

### 3.3  Secondary Search

After identifying a set of key studies in the primary search using the selection process, we employed forward and backward citation tracking (snowballing) to increase the body of relevant literature [[22](https://arxiv.org/html/2510.15509v1#bib.bibx22)]. Snowballing can be beneficial as it helps capture relevant studies that may not appear in database searches due to indexing limitations or differing terminology. Initially, studies found this way were judged based on their title and abstract. Later on, a full review of remaining studies was conducted to ensure they meet the eligibility criteria. An overview of the exact number of studies identified through this process and potential reasons for their exclusion is provided in Figure [2](https://arxiv.org/html/2510.15509v1#S3.F2 "Figure 2 ‣ 3.3 Secondary Search ‣ ethodology ‣ AI Adoption in NGOs: A Systematic Literature Review").

![Refer to caption](Prisma_flowchart_filled.png)


Figure 2: PRISMA flowchart as defined by Page et al.[[15](https://arxiv.org/html/2510.15509v1#bib.bibx15)]

### 3.4  Quality Assessment

To ensure only high quality studies are used in this review the CASP (Critical Appraisal
Skills Programme) paradigm [[23](https://arxiv.org/html/2510.15509v1#bib.bibx23)] was deployed. This quality assessment tool
includes multiple checklists suitable for qualitative studies, case studies, mixed-method research and quantitative studies and provides
clear questions to assess rigor, credibility, and relevance. Depending on the methodology used in the study it consists of between ten and twelve questions (evaluating validity, results and the value of the research) which can be answered either with ”Yes”, ”No” or ”Can’t tell”. As the review included a number of quantitative and algorithmic studies, the CASP checklists were adapted to better reflect aspects of quantitative rigor, such as statistical validity, reproducibility, data transparency, and performance evaluation. In accordance to common practice we considered studies which have two or more questions answered with ”No” as too poor quality to take them into account for the SLR.

Of the studies remaining after the selection process and the secondary search, 43 did not receive any “No” responses. 16 studies received a single “No” response, while seven received two or more and were thus excluded. The remaining six documents were white papers, which are not fit for appraisal using the CASP framework. These were instead evaluated for internal validity and the credibility of their sources, both of which were all documents deemed sufficient.

### 3.5  Data Extraction

Data from the included studies were extracted using a structured Excel spreadsheet to systematically capture both demographic and content-related information. Demographic data included bibliographic details such as author(s), year of publication, title, journal or source, and geographic location of the study. Study characteristics such as study design (e.g. case study, survey), NGO context (e.g. size, mission), and AI application specifics (e.g. type of AI, function, and specific application) were also recorded. Content-related data included reported findings and outcomes (quantitative results and qualitative observations), ethical considerations (e.g. bias, data privacy, transparency, accountability), and limitations highlighted in the original studies.

Data extraction was conducted manually by the first author and cross-checked with the second authors to ensure consistency and accuracy. A structured extraction form was piloted on a subset of studies prior to full extraction to confirm that all relevant information could be reliably captured.

### 3.6  Data synthesis and analysis

Due to the heterogeneity of the included studies and the limited availability of directly comparable quantitative data, a meta-analysis was deemed inappropriate. Instead, a qualitative approach combining narrative and thematic synthesis was employed to interpret and summarize the findings, providing a nuanced and coherent overview of the field [[24](https://arxiv.org/html/2510.15509v1#bib.bibx24)]. Thematic synthesis involved several steps: reviewers first immersed themselves in the studies, reading them thoroughly to gain a comprehensive understanding of the data. Key words, phrases, and concepts were then systematically and manually coded using both deductive codes (derived from the research questions, e.g. “AI use in donor management”) and inductive codes (emerging directly from the data, e.g. a specific use case of AI). Related codes were subsequently manually grouped into broader, overarching themes, with thematic mapping used as a visual aid to identify relationships between themes. A simplified version of the final thematic mapping can be found in appendix [B](https://arxiv.org/html/2510.15509v1#A2 "Appendix B Thematic Map ‣ AI Adoption in NGOs: A Systematic Literature Review") and a full overview is available in the [additional material](https://osf.io/a2357/?view_only=7120b178719540608dc97cd2a178ceff). Finally, these themes were integrated into a cohesive narrative that synthesized the evidence and directly addressed the research questions. While the process was primarily carried out by the first author, who repeatedly re-read the literature to gain deeper immersion, the second author was actively involved throughout the review. The final results were determined through multiple rounds of iterative discussions among all authors, leading to a consensus on the completed mapping.

## esults

This section reports the findings of the systematic literature review, beginning with an overview of the characteristics of the 65 included studies. Furthermore, we analyse the extracted relevant findings regarding the different utilization of AI by NGOs as well as the emerging challenges and solution regarding the implementation process. We specifically focus on how this differs based on location and size of the NGO.

For operationalization purposes, we decided to categorize the studies regarding location and size. This is beneficial for later thematic and structured analysis of relevant findings. For the location component we drew on the World Bank country classifications by income level for 2024-2025 [[25](https://arxiv.org/html/2510.15509v1#bib.bibx25)] which classifies each country based on the Gross National Income (GNI) per capita in four income levels: Low income, lower-middle income, higher-middle income and high income. This allows to move beyond the simplistic definition of developing vs. developed countries towards a more nuanced understanding of the economic situation. This is particularly important in the context of this SLR, as differences in infrastructure and access to technology and resources can influence the adoption of AI in NGOs. Furthermore, this classification enables more meaningful comparisons across countries with similar economic conditions.

We also classified NGOs by size into three different categories based on their number of employees, as assessed by publicly available information like corresponding websites: Small (less than 15 employees), moderate (between 15 and 50 employees) and large (more than 50 employees).

### 4.1  Characteristics of included studies

![Refer to caption](bar_chart_bw.png)


(a) Publications by Year (2020–2025)

![Refer to caption](donut_chart_bw_lighter.png)


(b) Research Type Distribution

Figure 3: Visualization of publication dates and research methodology

As illustrated in Figure [3](https://arxiv.org/html/2510.15509v1#S4.F3 "Figure 3 ‣ 4.1 Characteristics of included studies ‣ esults ‣ AI Adoption in NGOs: A Systematic Literature Review") the number of studies on AI adoption in NGOs has shown a steady increase since 2021 (considering only around three quaters of the year 2025 have already passed at the time of writing), highlighting the growing importance of the research area. Furthermore, included studies had an approximate balanced research type between quantitative and qualitative methods. This exemplifies the variety of approaches to this complex topic and improves the reliability of this SLR, as it draws on findings derived with multiple different approaches. Moreover, the studies were published in a variety of journals and conferences, further emphasizing the breadth of scholarly interest. For an tabular overview of included studies and their discussed topics please refer to appendix [C](https://arxiv.org/html/2510.15509v1#A3 "Appendix C Overview of Included Studies ‣ AI Adoption in NGOs: A Systematic Literature Review"). An even more detailed overview of a matching between journals/conferences, key findings, research methodology, ethical considerations and limitations to the corresponding papers, is provided in the [additional material](https://osf.io/a2357/?view_only=7120b178719540608dc97cd2a178ceff).

Unsurprisingly, most research was dedicated to large NGOs (29.3%). This was followed by research specifically concerning moderate (12.3%) and small (9.2%) NGOs. The other studies (53.8%) were unspecific on which type of NGO they concerned. Regarding the location of NGOs, most of the included studies pertained to high (26.2%) or lower-middle (26.2%) income countries, whereas only a minority concerned medium-high (12.3%) and lower income (3.1%) nations. The rest of the studies (46.2%) concerned either NGOs that acted globally or were unspecific to the location of NGOs they concerned. Please note that these numbers do not necessarily sum up to 100% as some studies concerned multiple NGOs of different sizes and with different geographic contexts.

This demonstrates a significant gap in the literature, as most available research focuses on large NGOs and higher or lower-middle income nations. However, AI adoption in small NGOs or NGOs operating within low income countries remains largely unexplored. Possible explanations for this biased focus include structural barriers, as small NGOs tend to have less capacity to cooperate with researchers and lower income nations typically lack digital infrastructure required for academic collaborations. Furthermore, data availability concerns might play a role, as research from low-income nations is often less visible and accessible in academic databases. Another possible explanation might be a bias in research interest.

Another notable characteristic is that among the 31 studies developing new AI innovations for NGOs, only about half actively involved NGOs as collaborators (32.3%) or had the NGO driving the development process (12.9%). The remaining studies either treated NGOs merely as data providers and end users (9.7%) or designed solutions without any active NGO engagement (45.1%). This limited engagement suggests a potential misalignment between AI innovations and NGO needs, which may hinder adoption, reduce practical impact, and limit the contextual relevance of these tools.

### 4.2  Utilization of AI in NGOs (RQ1)

The adoption of AI in NGOs is still in its infancy. Several studies report that NGOs have been slow to leverage AI [[26](https://arxiv.org/html/2510.15509v1#bib.bibx26), [27](https://arxiv.org/html/2510.15509v1#bib.bibx27), [28](https://arxiv.org/html/2510.15509v1#bib.bibx28), [29](https://arxiv.org/html/2510.15509v1#bib.bibx29)] and even when they do, the perceived impact remains limited [[30](https://arxiv.org/html/2510.15509v1#bib.bibx30)]. Depending on sector geographic context and size, research indicates that between 7.6% [[31](https://arxiv.org/html/2510.15509v1#bib.bibx31)] and 40% [[32](https://arxiv.org/html/2510.15509v1#bib.bibx32)] of NGOs utilize AI in some shape for now. Drawing on the DOI model, this positions AI adoption in NGOs between the early adopter and early majority stage [[12](https://arxiv.org/html/2510.15509v1#bib.bibx12)]. This stage is characterized by cautious but growing experimentation, visible success stories that begin to influence peers, and uneven diffusion shaped by resources and infrastructure. At present, AI serves primarily as a supportive resource rather than a replacement for human judgment, with some larger projects being implemented and a highly variable degree of organizational integration across the sector [[33](https://arxiv.org/html/2510.15509v1#bib.bibx33)]. In the following, we identify and six primary categories of how AI is utilized by NGOs that are visualized in figure [4](https://arxiv.org/html/2510.15509v1#S4.F4 "Figure 4 ‣ 4.2 Utilization of AI in NGOs (RQ1) ‣ esults ‣ AI Adoption in NGOs: A Systematic Literature Review").

![Refer to caption](AI_Usecases.png)


Figure 4: Overview of identified use cases of AI in NGOs

One prominent method NGOs utilize AI is as an engagement tool. In one study amongst a variety of non-profits in size, speciality, and area, 60% of participants reported that AI-driven engagement solutions increased stakeholder interaction and lead to better satisfaction scores [[34](https://arxiv.org/html/2510.15509v1#bib.bibx34)]. In the educational sector, for instance, AI can be utilized by NGOs to improve educational outcomes through individualization via personalized learning platforms that can be deployed in underserved communities where access to quality education is limited [[35](https://arxiv.org/html/2510.15509v1#bib.bibx35), [36](https://arxiv.org/html/2510.15509v1#bib.bibx36)]. Early adopters like the International Rescue Committee [[37](https://arxiv.org/html/2510.15509v1#bib.bibx37)], Khan Academy [[38](https://arxiv.org/html/2510.15509v1#bib.bibx38)] or a portion of NGO owned schools in Egypt already use and investigate its application [[39](https://arxiv.org/html/2510.15509v1#bib.bibx39)].

Another promising strand of AI-supported engagement is its application in interactive chatbots. Large NGOs employ these systems to provide refugees with accessible, localized information about their rights [[40](https://arxiv.org/html/2510.15509v1#bib.bibx40), [41](https://arxiv.org/html/2510.15509v1#bib.bibx41), [37](https://arxiv.org/html/2510.15509v1#bib.bibx37)] and to enhance the communication with beneficiaries through round-the-clock availability [[42](https://arxiv.org/html/2510.15509v1#bib.bibx42)]. Chatbots expend organizational reach and engagement through interaction with a larger audience simultaneously, saving costs in the long run, and freeing up time for staff [[32](https://arxiv.org/html/2510.15509v1#bib.bibx32)].

A further significant use case is the application of AI as an optimization tool. In the healthcare domain, AI supports critical innovations such as optimizing vaccine distribution in lower and lower-middle income countries [[43](https://arxiv.org/html/2510.15509v1#bib.bibx43)], effectively delivering timely preventive care information to new and expecting mothers [[44](https://arxiv.org/html/2510.15509v1#bib.bibx44)], and reducing total response time in emergency medical services [[45](https://arxiv.org/html/2510.15509v1#bib.bibx45)].

Furthermore, AI as an optimization tool is also used in service delivery by organizations like the Danish Refugee Council or the International Rescue Committee that leverage it to optimize their routing and enhance timely delivery to refugees [[40](https://arxiv.org/html/2510.15509v1#bib.bibx40), [37](https://arxiv.org/html/2510.15509v1#bib.bibx37)]. Similarly, another study developed an AI-powered tool for optimizing food delivery in cooperation with Ekram, a small Saudi Arabia NGO, and demonstrated increased effectiveness in the delivery process [[46](https://arxiv.org/html/2510.15509v1#bib.bibx46)]. A further use case lies in the application in disaster relief, where AI and big data analytics capabilities (AI-BDAC) were shown to significantly increase resilience and humanitarian supply chain agility in NGOs [[40](https://arxiv.org/html/2510.15509v1#bib.bibx40), [26](https://arxiv.org/html/2510.15509v1#bib.bibx26), [47](https://arxiv.org/html/2510.15509v1#bib.bibx47)].

Beyond optimized service delivery, the optimization capabilities of AI also extend to sustainability efforts. By helping to develop effective long-term strategies for protected areas [[27](https://arxiv.org/html/2510.15509v1#bib.bibx27)] or optimize biodegradable plastic packaging design [[48](https://arxiv.org/html/2510.15509v1#bib.bibx48)] AI was also shown to effectively enhance green initiatives.

The most prominent utilization of AI as an optimization tool, however, remains its application in donation management. Here AI enhances donor matching with beneficiaries [[49](https://arxiv.org/html/2510.15509v1#bib.bibx49)], keeps track and secures physical donations [[50](https://arxiv.org/html/2510.15509v1#bib.bibx50), [51](https://arxiv.org/html/2510.15509v1#bib.bibx51)], helps with verification of eligible recipients [[51](https://arxiv.org/html/2510.15509v1#bib.bibx51)], and analyses donor behaviour for more effective fundraising [[40](https://arxiv.org/html/2510.15509v1#bib.bibx40)]. Data taken from a wide range of NGOs with humanitarian missions through quantitative surveys revealed that total funds raised increased by an average 20% when using AI applications [[34](https://arxiv.org/html/2510.15509v1#bib.bibx34)]. However, some researchers note that content and objectives of fundraising strategies are unlikely to change as a result of AI. Nonetheless, we might see how increasing automation may shift strategies from broad target groups to fully individualized approaches [[33](https://arxiv.org/html/2510.15509v1#bib.bibx33)].

NGOs, particularly those in disaster relief, often face challenges that require fast and well-informed decision-making. AI as a decision-support tool is one solution to address this issue. In public health, for instance, AI has been deployed to forecast disease outbreaks [[36](https://arxiv.org/html/2510.15509v1#bib.bibx36)], identify high-risk populations for targeted interventions like during the Ebola pandemic in West Africa [[35](https://arxiv.org/html/2510.15509v1#bib.bibx35)], predict air quality in India [[35](https://arxiv.org/html/2510.15509v1#bib.bibx35)] or analyse food quality for charitable donations [[52](https://arxiv.org/html/2510.15509v1#bib.bibx52)]. Furthermore, AI-powered decision-support tools can be leveraged to inform project funding and where to deploy resources [[53](https://arxiv.org/html/2510.15509v1#bib.bibx53)] or assist in the development of more effective intervention strategies for sextortion [[54](https://arxiv.org/html/2510.15509v1#bib.bibx54)] or cyber bullying cases [[55](https://arxiv.org/html/2510.15509v1#bib.bibx55)]. In Disaster Relief, AI can help by providing real-time information for emergency response for example via social media analysis [[40](https://arxiv.org/html/2510.15509v1#bib.bibx40), [41](https://arxiv.org/html/2510.15509v1#bib.bibx41)]. For example, Care Centre, a large global NGO, used AI to get more accurate and timely analysis of the Syrian conflict [[37](https://arxiv.org/html/2510.15509v1#bib.bibx37)].

For NGOs, another promising path forward is adopting AI as a management tool. For instance, AI functions as a powerful instrument for optimizing resource allocation and mitigating risks related to financial instability [[56](https://arxiv.org/html/2510.15509v1#bib.bibx56), [35](https://arxiv.org/html/2510.15509v1#bib.bibx35)], while increasing efficiency and reducing errors in accounting and procurement [[57](https://arxiv.org/html/2510.15509v1#bib.bibx57), [58](https://arxiv.org/html/2510.15509v1#bib.bibx58)]. A study amongst global NGO representatives showed that AI usage reduced work hours needed for data entry by 60% and for resource allocation by 30% [[34](https://arxiv.org/html/2510.15509v1#bib.bibx34)]. AI has also been employed to predict the financial requirements of various charitable projects [[59](https://arxiv.org/html/2510.15509v1#bib.bibx59)] and for evaluating program impact by analysing outcome data [[40](https://arxiv.org/html/2510.15509v1#bib.bibx40)]. Supporting this, Alnamrouti et al. demonstrated that AI also has a positive and significant impact on sustainable organizational performance [[60](https://arxiv.org/html/2510.15509v1#bib.bibx60)].

In staff management AI-powered tools can be utilized to screen and hire promising employees [[40](https://arxiv.org/html/2510.15509v1#bib.bibx40)] or volunteers [[61](https://arxiv.org/html/2510.15509v1#bib.bibx61)], while reducing costs and solving recruiting delays [[62](https://arxiv.org/html/2510.15509v1#bib.bibx62)]. However, the main agency for human resource management still remains largely human, with technology adoption being minimal and serving rudimentary or supporting functionalities [[63](https://arxiv.org/html/2510.15509v1#bib.bibx63)]. Another crucial part of NGOs day-to-day work is the integration of volunteers. This area has also benefited from AI-powered platforms such as IDEA NGO [[64](https://arxiv.org/html/2510.15509v1#bib.bibx64)] or UniteVol [[65](https://arxiv.org/html/2510.15509v1#bib.bibx65)], which facilitate efficient matching between organizations and prospective volunteers [[66](https://arxiv.org/html/2510.15509v1#bib.bibx66)].

AI as a management tool can also simplify internal organizational flow by automating routine conversations and improving event planning [[40](https://arxiv.org/html/2510.15509v1#bib.bibx40), [67](https://arxiv.org/html/2510.15509v1#bib.bibx67), [68](https://arxiv.org/html/2510.15509v1#bib.bibx68)]. Its integration has been identified as a significant predictor and moderator of long-term organizational performance [[60](https://arxiv.org/html/2510.15509v1#bib.bibx60)]. However, adoption is not without drawbacks: One study found that the use of AI increased the time required for internal communication by 25% among global NGOs [[34](https://arxiv.org/html/2510.15509v1#bib.bibx34)].

Another promising area for NGOs lies in the area of leveraging AI as a creative tool. Among charity workers in the UK, AI is increasingly recognized for its potential to improve efficiencies in content generation [[69](https://arxiv.org/html/2510.15509v1#bib.bibx69)], and even conservative organizations like churches see potential for its utilization in areas such as sermon preparation [[70](https://arxiv.org/html/2510.15509v1#bib.bibx70)]. In fact, NGOs already use AI to help write and refine individualized donor thank-you notes, newsletters, grant proposals, and press releases [[71](https://arxiv.org/html/2510.15509v1#bib.bibx71), [68](https://arxiv.org/html/2510.15509v1#bib.bibx68)].

Beyond communication and fundraising, AI also supports educational and awareness-raising initiatives. Examples include the assistance in preparing educational material for using food in healthy ways via recipe generation [[72](https://arxiv.org/html/2510.15509v1#bib.bibx72)] or the refinement of resources for informing about sextortion [[54](https://arxiv.org/html/2510.15509v1#bib.bibx54)]. More experimental approaches emphasize participatory creativity. For instance Crea.vision, a platform following a citizen-science approach focused on human-AI collaboration, allows users to create images on societal issues utilizing AI, and being subsequently linked to relevant NGOs [[73](https://arxiv.org/html/2510.15509v1#bib.bibx73)].

AI as a predictive tool can also assist NGOs in diverse ways. For instance, local NGOs have used AI models based on satellite data to predict shelter locations of refugees in Syria [[74](https://arxiv.org/html/2510.15509v1#bib.bibx74)], Columbia [[75](https://arxiv.org/html/2510.15509v1#bib.bibx75)], or West Africa [[37](https://arxiv.org/html/2510.15509v1#bib.bibx37)]. Another example is the EUMigraTool (EMT), a joint European initiative using AI to predict short- and mid-term migration. EMT assists NGOs by guiding strategy development, informing funding decisions, supporting advocacy, and addressing gender-specific needs such as safe spaces and reproductive healthcare [[76](https://arxiv.org/html/2510.15509v1#bib.bibx76)]. Similarly, the Danish Refugee Council (DRC) [[77](https://arxiv.org/html/2510.15509v1#bib.bibx77)] and Save The Children [[29](https://arxiv.org/html/2510.15509v1#bib.bibx29)], both large NGOs, developed separate forecasting models for predicting forced displacement that informs plan development and policy formulation.

Predictive modelling also play a key role in disaster preparation. Applications range from anticipating of conflicts and crises [[37](https://arxiv.org/html/2510.15509v1#bib.bibx37)], to forecasting of climate change impact on vulnerable groups [[35](https://arxiv.org/html/2510.15509v1#bib.bibx35)] and predicting natural disasters [[36](https://arxiv.org/html/2510.15509v1#bib.bibx36), [41](https://arxiv.org/html/2510.15509v1#bib.bibx41), [78](https://arxiv.org/html/2510.15509v1#bib.bibx78), [79](https://arxiv.org/html/2510.15509v1#bib.bibx79)]. At a more localized scale, a study in Texas developed a Deep Neural Network that helps predict tenants-at-risk of eviction in cooperation with Child Poverty Action Lab, a moderate sized NGO [[80](https://arxiv.org/html/2510.15509v1#bib.bibx80)].

Overall, we identified six different categories of utilizations of AI in NGOs. However, the exact degree of application and usage differs with the size and geographical context of the organization. Large organizations like the red cross are reported to often utilize AI for more niche subjects like data visualization [[81](https://arxiv.org/html/2510.15509v1#bib.bibx81)]. Due to their comparatively higher financial budget and their ability to hire domain experts [[82](https://arxiv.org/html/2510.15509v1#bib.bibx82)], they can also develop in-house solutions in cooperation with academic and industry partners. For example, Mercy Corps use an early warning system they developed in partnership with IBM [[40](https://arxiv.org/html/2510.15509v1#bib.bibx40)]. According to the literature body, the usage of AI as an engagement, predictive and optimization tool is primarily limited to larger NGOs, while smaller NGOs already adopt it as a management and creative solution.

The location of the corresponding NGO also plays a crucial role in the type of use cases of AI. High income countries which have advanced technological infrastructure posses a number of NGOs that are extremely technology ready and specifically focus on integrating technological innovations. For example, the NGO STEM for Dance in the US build an AI-powered virtual coding environment to code interactive dance routines in cooperation with academic partners [[83](https://arxiv.org/html/2510.15509v1#bib.bibx83)]. Another example is Qatar Foundation (QF), which developed a comprehensive multi-year strategy on the integration of AI [[58](https://arxiv.org/html/2510.15509v1#bib.bibx58)]. On the other hand, different sociocultural challenges also hold new room for AI applications. For instance, AI can be used by NGOs to help streamline the distribution process of Zakat, a Muslim tradition of charitable giving [[51](https://arxiv.org/html/2510.15509v1#bib.bibx51), [84](https://arxiv.org/html/2510.15509v1#bib.bibx84)]. Unlike high income countries, many low- and lower-middle income nations, like India, have decentralized emergency medical services involving both semi-government and non-government organizations, which is another area of application of AI for NGOs [[45](https://arxiv.org/html/2510.15509v1#bib.bibx45)].

### 4.3  Challenges and Solutions in AI Adoption (RQ2)

The adoption of AI by NGOs faces numerous challenges and obstacles. The TOE framework provides a useful lens for categorizing and understanding these barriers [[10](https://arxiv.org/html/2510.15509v1#bib.bibx10)]. Figure [5](https://arxiv.org/html/2510.15509v1#S4.F5 "Figure 5 ‣ 4.3 Challenges and Solutions in AI Adoption (RQ2) ‣ esults ‣ AI Adoption in NGOs: A Systematic Literature Review") gives an overview of the identified challenges, matched to the corresponding parts of the TOE framework.

![Refer to caption](Challenges.png)


Figure 5: Summary of identified challenges

#### 4.3.1 Challenges in Technology Context

The technology context centres around the internal and external technologies available to an organization itself. For instance, AI at its core always requires some form of data to work with. Data availability and management are thus a central concern, which can negatively affect the accuracy of machine learning predictions [[40](https://arxiv.org/html/2510.15509v1#bib.bibx40), [28](https://arxiv.org/html/2510.15509v1#bib.bibx28)]. NGOs are often faced with complex data that includes multiple possibly delayed data streams, diverse data structures, multiple ways of data acquisition [[85](https://arxiv.org/html/2510.15509v1#bib.bibx85), [77](https://arxiv.org/html/2510.15509v1#bib.bibx77)] and incomplete records [[35](https://arxiv.org/html/2510.15509v1#bib.bibx35)], particularly in lower income regions [[74](https://arxiv.org/html/2510.15509v1#bib.bibx74)]. Therefore, establishing robust internal data governance becomes a key challenge in the AI adoption journey [[36](https://arxiv.org/html/2510.15509v1#bib.bibx36)]. From an academic perspective, researchers such as Mate et al. argue that these challenges should be viewed as genuine research question rather than limitations [[44](https://arxiv.org/html/2510.15509v1#bib.bibx44)]. However, other research finds that in specific scenarios, like the DRC forecasting project, the high availability of data can also be an enabler for AI integration [[77](https://arxiv.org/html/2510.15509v1#bib.bibx77)].

Another key concern within the technological context involves ethical considerations. NGOs must ensure that the adoption of AI not only aligns with their unique missions and goals [[50](https://arxiv.org/html/2510.15509v1#bib.bibx50)] but also complies with broader ethical standards. A central issue is the fairness and accountability of AI solutions [[30](https://arxiv.org/html/2510.15509v1#bib.bibx30)]. Since these systems heavily rely on the quality of data, flawed or incomplete datasets can lead to biased outcomes that systematically disadvantage already marginalized groups [[35](https://arxiv.org/html/2510.15509v1#bib.bibx35), [81](https://arxiv.org/html/2510.15509v1#bib.bibx81), [69](https://arxiv.org/html/2510.15509v1#bib.bibx69), [55](https://arxiv.org/html/2510.15509v1#bib.bibx55)]. Especially in the midst of an emergency, humanitarian staff might not have the time to verify the information provided by the AI solution [[41](https://arxiv.org/html/2510.15509v1#bib.bibx41)]. This issue relates back to the opacity of algorithms, underscoring the importance of human-in-the-loop approaches [[81](https://arxiv.org/html/2510.15509v1#bib.bibx81), [69](https://arxiv.org/html/2510.15509v1#bib.bibx69)], particularly in areas that rely on individualized outputs like education [[39](https://arxiv.org/html/2510.15509v1#bib.bibx39)].

Beyond fairness and accountability, the risk of overreliance on technology represents another critical concern. NGOs tend to be cautious about ethical matters, as they do not want to over rely on technological solutions, emphasizing their mission-driven orientation in contrast to becoming technology-driven [[30](https://arxiv.org/html/2510.15509v1#bib.bibx30)]. Safeguarding the ability to remain functional, even without the usage of AI, is a key concern regarding the critical independence of NGOs [[53](https://arxiv.org/html/2510.15509v1#bib.bibx53), [41](https://arxiv.org/html/2510.15509v1#bib.bibx41), [68](https://arxiv.org/html/2510.15509v1#bib.bibx68)].

Another key dimension of ethical considerations concerns security and privacy. NGOs need to comply with data confidentiality and ensure that data is stored securely [[81](https://arxiv.org/html/2510.15509v1#bib.bibx81), [32](https://arxiv.org/html/2510.15509v1#bib.bibx32), [34](https://arxiv.org/html/2510.15509v1#bib.bibx34), [38](https://arxiv.org/html/2510.15509v1#bib.bibx38), [54](https://arxiv.org/html/2510.15509v1#bib.bibx54), [57](https://arxiv.org/html/2510.15509v1#bib.bibx57), [86](https://arxiv.org/html/2510.15509v1#bib.bibx86), [55](https://arxiv.org/html/2510.15509v1#bib.bibx55)]. Data servers are also frequently located abroad, outside the direct control of NGOs, increasing data security concerns [[33](https://arxiv.org/html/2510.15509v1#bib.bibx33)]. For NGOs in particular, breaches of data security carry severe consequences, as they can result in significant losses of trust within the communities they serve [[35](https://arxiv.org/html/2510.15509v1#bib.bibx35)]. Overall, research emphasizes the need for NGOs to strike a balance between data protection and program accessibility [[81](https://arxiv.org/html/2510.15509v1#bib.bibx81)].

Beyond classical approaches to ethics, Sandberg et al. [[71](https://arxiv.org/html/2510.15509v1#bib.bibx71)] developed a data feminist pedagogy regarding AI in NGOs, framing AI not merely as a technological tool but as a political instrument that reflects and reinforces prevailing values. From this perspective, NGOs must navigate the tension between safeguarding ethical standards, such as avoiding the use of AI in sensitive areas like hiring, and leveraging AI to enhance efficiency and effectiveness [[62](https://arxiv.org/html/2510.15509v1#bib.bibx62)].

A further technological challenge concerns trust in AI. For instance, a study on AI in biodegradable package design in Bangladesh found that merely 35% of consumers place trust in AI-generated solutions [[48](https://arxiv.org/html/2510.15509v1#bib.bibx48)]. Similarly, research on AI as a decision-maker in public services suggests that public perceptions remain largely negative, despite some evidence that AI can increase perceptions of distributive justice and thereby strengthen donation intentions in specific groups [[87](https://arxiv.org/html/2510.15509v1#bib.bibx87)]. As most NGOs rely heavily on donations, such attitudes can directly influence the willingness to adopt AI [[32](https://arxiv.org/html/2510.15509v1#bib.bibx32)]. At the same time, NGOs face considerable pressure to maintain public trust and transparency, making them particularly vulnerable to reputational damage [[56](https://arxiv.org/html/2510.15509v1#bib.bibx56), [33](https://arxiv.org/html/2510.15509v1#bib.bibx33)]. Such damage not only undermines the organizations’ credibility but can also have legal consequences and risk their future funding [[81](https://arxiv.org/html/2510.15509v1#bib.bibx81)].

#### 4.3.2 Challenges in the Organization Context

The organization context of the TOE-framework refers to the internal characteristics of an organization that influence its ability and readiness to adopt and implement new technologies. For NGOs, financial constraints fall within this category. Most NGOs have limited budgets that primarily stem from donations, grants, or government funding, which are more volatile than commercial revenue streams [[56](https://arxiv.org/html/2510.15509v1#bib.bibx56)]. Since the acquisition and integration of AI systems can be costly, financial limitations are often cited as a major barrier to adoption [[37](https://arxiv.org/html/2510.15509v1#bib.bibx37), [63](https://arxiv.org/html/2510.15509v1#bib.bibx63), [34](https://arxiv.org/html/2510.15509v1#bib.bibx34), [32](https://arxiv.org/html/2510.15509v1#bib.bibx32), [40](https://arxiv.org/html/2510.15509v1#bib.bibx40), [35](https://arxiv.org/html/2510.15509v1#bib.bibx35), [36](https://arxiv.org/html/2510.15509v1#bib.bibx36), [29](https://arxiv.org/html/2510.15509v1#bib.bibx29)]. NGOs must therefore weigh the potential benefits of AI against the upfront cost of its implementation [[57](https://arxiv.org/html/2510.15509v1#bib.bibx57)]. This challenge is not limited to low or lower-middle income countries but also remains central in higher-income contexts like Slovenia or the US [[30](https://arxiv.org/html/2510.15509v1#bib.bibx30), [38](https://arxiv.org/html/2510.15509v1#bib.bibx38)]. As a result, NGOs might be especially motivated to experiment with affordable AI-generated solutions [[88](https://arxiv.org/html/2510.15509v1#bib.bibx88)]. However, in contrast to the mainstream view, some scholars suggest that free versions of AI applications may already be sufficient for many NGOs, thereby partially contradicting the assumption that AI adoption is hindered due to financial constraints [[33](https://arxiv.org/html/2510.15509v1#bib.bibx33)].

These financial constraints within NGOs are further amplified by the challenge of competition for funding. Contemporary research notes that organizations that fail to embrace emerging technologies like AI that increase efficiency risk falling behind their competition, thereby diminishing future funding opportunities [[62](https://arxiv.org/html/2510.15509v1#bib.bibx62), [32](https://arxiv.org/html/2510.15509v1#bib.bibx32)]. Larger charities, with their highly skilled teams and greater financial resources, possess a substantial capitalistic advantage over smaller organizations [[69](https://arxiv.org/html/2510.15509v1#bib.bibx69)]. This dynamic risks creating a “winner-takes-all” environment in which well-resourced NGOs consolidate their dominance, potentially reinforcing structural inequalities and worsening disparities within the non-profit sector.

Another crucial organizational challenge is the lack of awareness of AI or an unwillingness for its adoption [[37](https://arxiv.org/html/2510.15509v1#bib.bibx37), [32](https://arxiv.org/html/2510.15509v1#bib.bibx32), [40](https://arxiv.org/html/2510.15509v1#bib.bibx40), [27](https://arxiv.org/html/2510.15509v1#bib.bibx27)]. For instance, many NGOs in Tanzania perceive AI adoption as a potential threat to their human resource practices [[62](https://arxiv.org/html/2510.15509v1#bib.bibx62)], while a survey of NGOs in Zambia found that 56.7% of respondents had limited or no familiarity with the technology [[32](https://arxiv.org/html/2510.15509v1#bib.bibx32)]. This unwillingness is often driven by employees fearing replacement by AI [[33](https://arxiv.org/html/2510.15509v1#bib.bibx33), [68](https://arxiv.org/html/2510.15509v1#bib.bibx68)] and a lack in leadership and management support [[32](https://arxiv.org/html/2510.15509v1#bib.bibx32)]. Moreover, NGOs depend extensively on the individual motivation of their staff [[63](https://arxiv.org/html/2510.15509v1#bib.bibx63)], many of whom already juggle multiple and overlapping responsibilities, particularly in smaller organizations, further constraining the capacity to experiment with or integrate new technologies.[[63](https://arxiv.org/html/2510.15509v1#bib.bibx63)].

As AI implementation usually requires a minimum of technical familiarity with itself, lacking expertise can be another major organizational barrier to adoption [[32](https://arxiv.org/html/2510.15509v1#bib.bibx32)]. Many NGOs do not have what they believe to be adequate expertise in AI and a lack of skilled workforce with contextual understanding [[28](https://arxiv.org/html/2510.15509v1#bib.bibx28), [34](https://arxiv.org/html/2510.15509v1#bib.bibx34), [71](https://arxiv.org/html/2510.15509v1#bib.bibx71), [41](https://arxiv.org/html/2510.15509v1#bib.bibx41), [89](https://arxiv.org/html/2510.15509v1#bib.bibx89), [26](https://arxiv.org/html/2510.15509v1#bib.bibx26), [78](https://arxiv.org/html/2510.15509v1#bib.bibx78)]. Adopting a knowledge-based view Scutto et al. argue that value creation of humanitarian AI actions is still largely determined by individual skills rather than collective knowledge [[29](https://arxiv.org/html/2510.15509v1#bib.bibx29)]. As AI technologies continue to grow in complexity, this expertise gap is becoming an increasingly critical obstacle [[36](https://arxiv.org/html/2510.15509v1#bib.bibx36)]. Interestingly, this effect does not only appear in low or lower-middle income countries but also in high-income contexts like Slovenia [[30](https://arxiv.org/html/2510.15509v1#bib.bibx30)].

Another major issue in the organization context are organizational challenges. Many NGOs report that they do not feel like they have clear organizational policies regarding AI [[71](https://arxiv.org/html/2510.15509v1#bib.bibx71)]. Additionally, the multitude of solutions and approaches to choose from, with roadmaps and pricing mechanisms that are not clearly defined yet, make the selection of the “right” solution a challenge [[89](https://arxiv.org/html/2510.15509v1#bib.bibx89)]. Furthermore, NGOs are often forced to adopt ad hoc information management solutions to react to crises, which leads to a loss of historic data, the need to ”reinvent the wheel” each time and difficulties with setting up an AI infrastructure [[85](https://arxiv.org/html/2510.15509v1#bib.bibx85)]. While these challenges persist, researchers like Ahatsi et al. argue that they remain marginal compared to technical and financial constraints [[78](https://arxiv.org/html/2510.15509v1#bib.bibx78)].

Within the organizational context, the size of an NGO significantly shapes the AI adoption journey. In contrast to moderate or small sized NGOs, large organizations usually have an advanced IT infrastructure, a culture supportive of technological innovation and stronger donor support for AI initatives [[32](https://arxiv.org/html/2510.15509v1#bib.bibx32)]. These advantages enable them to specifically hire technical experts, and they possess a clearer understanding of what they want from someone in this position [[82](https://arxiv.org/html/2510.15509v1#bib.bibx82)]. They also have the capacity to actively initiate cooperations with experts from industry and academia [[37](https://arxiv.org/html/2510.15509v1#bib.bibx37)], something that due to their resource constraints, small and moderate size NGOs sometimes lack. Moreover, more traditional or smaller entities are at risk in an artificial intelligence economy, facing greater challenges in adapting to technological transformations and maintaining competitiveness [[68](https://arxiv.org/html/2510.15509v1#bib.bibx68)]. Cooperations between large NGOs like NetHope also have the capacity to develop resources like the Artificial Intelligence Ethics for Non-Profit Toolkit, the Humanitarian AI Code of Conduct or the Data Governece Toolkit: A guide to implementing data governance in nonprofits [[41](https://arxiv.org/html/2510.15509v1#bib.bibx41)] which supports compliance with ethical and legal standards.

On the other hand, small NGOs often juggle limited budgets and staff while attempting to achieve significant social impact [[57](https://arxiv.org/html/2510.15509v1#bib.bibx57)]. Their adoption of AI is further constrained by comparatively weaker digital infrastructures [[32](https://arxiv.org/html/2510.15509v1#bib.bibx32)], as well as the need to plan for scalability and continuous adaptation despite resource shortages [[57](https://arxiv.org/html/2510.15509v1#bib.bibx57)].

#### 4.3.3 Challenges in the Environment Context

Within the TOE framework, the environmental context refers to external factors that influence an organizations’ technology adoption. For example, legal challenges can play a crucial role, as NGOs have to adhere to complex local and global legislative guidelines regarding the usage of AI [[57](https://arxiv.org/html/2510.15509v1#bib.bibx57)]. In many places, however, the absence or inadequacy of legal frameworks can itself hinder the widespread adoption of AI technologies [[27](https://arxiv.org/html/2510.15509v1#bib.bibx27)].

A further environmental challenge is the lack of collaborations, with academic, government and industry partners, which can hinder AI adoption in NGOs [[32](https://arxiv.org/html/2510.15509v1#bib.bibx32), [34](https://arxiv.org/html/2510.15509v1#bib.bibx34)]. In general, structural weaknesses in public–private sector collaboration limit the societal benefits of technological transfer. Some countries, such as Morocco, are now actively seeking to encourage such partnerships [[27](https://arxiv.org/html/2510.15509v1#bib.bibx27)]. The collaboration between the charity sector and government bodies also often lags behind, as many NGOs encounter difficulties in accessing government data [[85](https://arxiv.org/html/2510.15509v1#bib.bibx85)]. Moreover, the absence of a common standard for a systematic information management process among different NGOs, frequently leads to individual flawed adoption and ad hoc cooperations that are not persistent [[85](https://arxiv.org/html/2510.15509v1#bib.bibx85)].

Finally, geographic context plays a crucial role in shaping AI adoption in NGOs. This relates back to the digital divide, which represents a structural gap in infrastructure, capabilities, and knowledge between different nations which can significantly hinder adoption [[41](https://arxiv.org/html/2510.15509v1#bib.bibx41)]. In some regions, limited internet penetration can constrain data handling [[85](https://arxiv.org/html/2510.15509v1#bib.bibx85)], while NGOs may need to charge for AI-based services due to high costs, reducing accessibility in low income contexts as a result [[38](https://arxiv.org/html/2510.15509v1#bib.bibx38)]. Furthermore, resource constraint locations often require specialized solutions, for instance through edge computing, that are not publicly or cheaply available [[43](https://arxiv.org/html/2510.15509v1#bib.bibx43)]. Additionally, discrepancies between policy objectives and their execution, especially in enforcement across various geographic areas [[48](https://arxiv.org/html/2510.15509v1#bib.bibx48)] further worsen geographic disparities.

On the other hand, high-income nations, like Qatar, have the capacity to make support for AI integration in NGOs a priority [[58](https://arxiv.org/html/2510.15509v1#bib.bibx58)]. A study investigating generative AI use in NGO owned schools in Egypt also emphasized the importance of localization, including the use of local language, to enhance AI’s impact on local communities [[39](https://arxiv.org/html/2510.15509v1#bib.bibx39)]. However, biases in the available training data can structurally hinder localization efforts. For instance, Shrma et al. noted an insufficient number of datasets for non-English tools, showcasing how certain areas can be structurally disadvantaged in the usage of AI [[66](https://arxiv.org/html/2510.15509v1#bib.bibx66)]. In addition, a dataset-driven study observed that ecological NGOs in areas such as Southern Europe, Northern and Middle Africa, Central Asia, Polynesia, and Micronesia have yet to adopt AI tools [[31](https://arxiv.org/html/2510.15509v1#bib.bibx31)]. While these findings are based on limited evidence, the authors theorize that these regions face barriers including insufficient technological infrastructure, skill gaps, funding constraints, and restricted data access.

#### 4.3.4 Proposed Solutions for AI Adoption

To solve these numerous challenges, literature proposes a set of guidelines and solutions. A common starting point is capacity building, which includes improving data quality [[28](https://arxiv.org/html/2510.15509v1#bib.bibx28), [28](https://arxiv.org/html/2510.15509v1#bib.bibx28), [89](https://arxiv.org/html/2510.15509v1#bib.bibx89)] and investments in comprehensive staff training [[48](https://arxiv.org/html/2510.15509v1#bib.bibx48), [32](https://arxiv.org/html/2510.15509v1#bib.bibx32), [34](https://arxiv.org/html/2510.15509v1#bib.bibx34), [57](https://arxiv.org/html/2510.15509v1#bib.bibx57), [78](https://arxiv.org/html/2510.15509v1#bib.bibx78), [68](https://arxiv.org/html/2510.15509v1#bib.bibx68)]. This ensures that AI systems operate on reliable inputs and that staff develops the necessary skills and confidence to engage with new technologies. Additionally, targeted funding and resource allocations dedicated specifically to AI can provide the financial stability required to support these initiatives [[32](https://arxiv.org/html/2510.15509v1#bib.bibx32)].

Because of the high stake nature under which many NGOs operate, AI solutions must be tested, evaluated and refined before deployment [[41](https://arxiv.org/html/2510.15509v1#bib.bibx41)]. Such processes enable organizations to better understand both the potential and limitations of AI [[40](https://arxiv.org/html/2510.15509v1#bib.bibx40), [32](https://arxiv.org/html/2510.15509v1#bib.bibx32)]. A common strategy is to begin with small-scale pilot projects and incrementally build up on initial findings [[37](https://arxiv.org/html/2510.15509v1#bib.bibx37)]. Stakeholder involvement is essential in this phase, ensures that refinements are grounded in practical insights and organizational needs [[36](https://arxiv.org/html/2510.15509v1#bib.bibx36)]. For instance, NGOs in Tanzania utilized qualitative measures to understand how and when AI should be integrated in their hiring process [[62](https://arxiv.org/html/2510.15509v1#bib.bibx62)]. This incremental approach is paramount as it ensures both reliability and ethical use throughout all stages of the AI lifecycle [[57](https://arxiv.org/html/2510.15509v1#bib.bibx57), [81](https://arxiv.org/html/2510.15509v1#bib.bibx81), [60](https://arxiv.org/html/2510.15509v1#bib.bibx60), [77](https://arxiv.org/html/2510.15509v1#bib.bibx77)]. Furthermore, regular audits can support decision-making on whether existing solutions suffice or further development is necessary [[89](https://arxiv.org/html/2510.15509v1#bib.bibx89)].

Another important insights is that open-source solutions are sometimes already sufficient for the intended use case of the NGO [[30](https://arxiv.org/html/2510.15509v1#bib.bibx30)]. In a semi-strucutred interview with ten unspecified NGOs Popescu et al. found that most organizations currently primarily rely on open-source chatbots [[68](https://arxiv.org/html/2510.15509v1#bib.bibx68)]. The use of low-cost intelligent systems can not only help adoption [[34](https://arxiv.org/html/2510.15509v1#bib.bibx34)] but also keep the product at scale [[44](https://arxiv.org/html/2510.15509v1#bib.bibx44)]. However, choosing the right tool remains essential. For instance, Kraus developed an overview for NGOs regarding the pros and cons of available accounting solutions [[57](https://arxiv.org/html/2510.15509v1#bib.bibx57)]. In addition, some AI providers offer discounted or free rates for social organizations, thereby helping to overcome financial boundaries [[34](https://arxiv.org/html/2510.15509v1#bib.bibx34)]. As the cost of AI is anticipated to decrease further, NGOs such as Khan Academy remain optimistic about the prospect of wider adoption [[38](https://arxiv.org/html/2510.15509v1#bib.bibx38)].

With respect to AI-generated content, most studies advocate for a balanced approach. Research indicates that the use of AI-generated images can negatively impact donation intentions [[88](https://arxiv.org/html/2510.15509v1#bib.bibx88)]. However, making ethical motives salient or using these images under extraordinary circumstances which require timely response, was shown to lead to similar donation outcomes as using real images [[88](https://arxiv.org/html/2510.15509v1#bib.bibx88)]. Furthermore, deploying functional (e.g. ease of use) and emotional features (e.g. emotional connection) in interactive chatbots was shown to increase trust, which in turn correlates with stronger social media engagement and higher willingness to donate [[42](https://arxiv.org/html/2510.15509v1#bib.bibx42)].

As practical guidance, research emphasizes the importance of ensuring data anonymity and security through a privacy-by-design approach [[81](https://arxiv.org/html/2510.15509v1#bib.bibx81), [76](https://arxiv.org/html/2510.15509v1#bib.bibx76)] and engagement with critical theory [[71](https://arxiv.org/html/2510.15509v1#bib.bibx71)]. To preempt biases, some studies suggest removing sensitive attributes, such as gender-identifying features, when they are not strictly necessary [[61](https://arxiv.org/html/2510.15509v1#bib.bibx61)]. At the same time, it is important to recognize that AI should not be viewed as an end in itself. In many cases non-AI solutions fully suffice for their intended use cases [[50](https://arxiv.org/html/2510.15509v1#bib.bibx50)]. Ultimately, what matters most is that applied solutions are genuinely useful and well scoped, while still allowing for scalability and adaptability [[36](https://arxiv.org/html/2510.15509v1#bib.bibx36), [89](https://arxiv.org/html/2510.15509v1#bib.bibx89)].

There are also many calls for a unified, inclusive AI governance framework that prioritizes ethical considerations, ensures adequate resource allocation, strengthens education and training, and fosters collaboration between governments, NGOs, and academic institutions [[30](https://arxiv.org/html/2510.15509v1#bib.bibx30), [35](https://arxiv.org/html/2510.15509v1#bib.bibx35)]. At the same time, research often appeals to policymakers to create a supportive environment for AI adoption in NGOs, by for instance investing in digital infrastructure [[62](https://arxiv.org/html/2510.15509v1#bib.bibx62)], or creating concrete legals structures to guide the adoption process [[27](https://arxiv.org/html/2510.15509v1#bib.bibx27), [78](https://arxiv.org/html/2510.15509v1#bib.bibx78)].

Another crucial factor in addressing challenges is the importance of the environment and sociocultural context [[27](https://arxiv.org/html/2510.15509v1#bib.bibx27), [79](https://arxiv.org/html/2510.15509v1#bib.bibx79)]. Pereira & Shafique argue, that NGOs should focus on their unique resources and adapt their strategies to local conditions in order to effectively implement AI into their supply chains [[47](https://arxiv.org/html/2510.15509v1#bib.bibx47)]. Furthermore, individual geographic constraints have to be assessed by local NGO, as external collaborators often lack the contextual knowledge required [[43](https://arxiv.org/html/2510.15509v1#bib.bibx43)]. To enhance access and distributive justice, AI solutions should also be localized, both by providing interfaces in local languages and by ensuring remote accessibility in underdeveloped regions [[81](https://arxiv.org/html/2510.15509v1#bib.bibx81), [39](https://arxiv.org/html/2510.15509v1#bib.bibx39), [28](https://arxiv.org/html/2510.15509v1#bib.bibx28)].

What emerges most strongly from the literature is the emphasis on partnerships and collaborations as a prerequisite for successful AI adoption in NGOs [[32](https://arxiv.org/html/2510.15509v1#bib.bibx32), [34](https://arxiv.org/html/2510.15509v1#bib.bibx34)]. For one, this includes inter-NGO cooperation to develop shared ethical framework for AI use [[28](https://arxiv.org/html/2510.15509v1#bib.bibx28)] like the Artificial Intelligence Ethics for Nonprofits Toolkit [[41](https://arxiv.org/html/2510.15509v1#bib.bibx41)]. Additionally, collaboration with government bodies through data sharing, and joint initiatives improves the effectiveness of AI [[54](https://arxiv.org/html/2510.15509v1#bib.bibx54), [85](https://arxiv.org/html/2510.15509v1#bib.bibx85)]. However, when acting as data providers to government bodies, NGOs have to maintain neutrality [[86](https://arxiv.org/html/2510.15509v1#bib.bibx86)]. To profit from state-of-the-art AI solutions, a close collaboration with technology companies also remains beneficial [[28](https://arxiv.org/html/2510.15509v1#bib.bibx28), [34](https://arxiv.org/html/2510.15509v1#bib.bibx34), [50](https://arxiv.org/html/2510.15509v1#bib.bibx50), [78](https://arxiv.org/html/2510.15509v1#bib.bibx78), [77](https://arxiv.org/html/2510.15509v1#bib.bibx77)]. Improving public–private sector collaborations is identified as one of the key solutions for AI Adoption in NGOs [[27](https://arxiv.org/html/2510.15509v1#bib.bibx27)]. Academic collaborations provide an additional pathway, helping NGOs experiment with and evaluate AI in practice [[76](https://arxiv.org/html/2510.15509v1#bib.bibx76), [75](https://arxiv.org/html/2510.15509v1#bib.bibx75), [80](https://arxiv.org/html/2510.15509v1#bib.bibx80), [90](https://arxiv.org/html/2510.15509v1#bib.bibx90), [44](https://arxiv.org/html/2510.15509v1#bib.bibx44), [46](https://arxiv.org/html/2510.15509v1#bib.bibx46)]. This systematic literature review includes a wide spectrum of such collaborations, ranging from localized projects in low-income contexts [[74](https://arxiv.org/html/2510.15509v1#bib.bibx74)] to long-term, large-scale partnerships such as ADVISER [[43](https://arxiv.org/html/2510.15509v1#bib.bibx43)], illustrating the diversity of approaches available to NGOs.

## iscussion & Implications

This systematic literature review examined 65 documents to answer two central questions: How NGOs currently utilize AI (RQ1), and what challenges and solutions shape their adoption processes (RQ2). In the following we interpret our findings, emphasize theoretical and practical implications, state limitations, and discuss future research directions.

While we observed a growing research interest in NGOs adoption of AI, utilizing the DOI framework we placed the current adoption stage, depending on context, between early adoptor and early majority [[31](https://arxiv.org/html/2510.15509v1#bib.bibx31), [32](https://arxiv.org/html/2510.15509v1#bib.bibx32)]. Across the literature, NGOs utilize AI in the following six ways:

* •

  Engagement: AI tools for outreach and conversational support (e.g. interactive chatbots) that scale communication and personalize donor and beneficiary interactions.
* •

  Optimization: AI applied to logistics, resource allocation and fundraising efficiency, for example in vehicle routing and donor matching.
* •

  Decision-support: Predictive analytics and dashboards that inform prioritization and operational decisions in crises or program targeting.
* •

  Management: Automation for back-office functions like finance, procurement, HR, or volunteer coordination.
* •

  Creative: Generative AI for content production, educational material curation and campaign assets.
* •

  Predictive: Models usually using geospatial or socio-economic data to forecast displacement, disasters, or risk (early-warning systems).

Generally, large NGOs are more capable to develop in-house and complex projects [[32](https://arxiv.org/html/2510.15509v1#bib.bibx32), [82](https://arxiv.org/html/2510.15509v1#bib.bibx82)], while smaller organizations tend to use off-the-shelf or open-source tools [[57](https://arxiv.org/html/2510.15509v1#bib.bibx57)]. This resource and capability difference helps explain the uneven diffusion of adoption under the DOI model and underscores the risk of inequity within the NGO sector.

Utilizing the TOE-framework, we identified multiple challenges to AI adoption in NGOs. Within the technological context, challenges include limited data availability and diverse ethical challenges such as fairness, accountability, security, the need to keep humans in the loop, and the risk of overreliance on technology. Furthermore, concerns with trust and user acceptability further complicate adoption. In the organizational context, the most pressing obstacles are financial constraints, especially among smaller NGOs [[88](https://arxiv.org/html/2510.15509v1#bib.bibx88)], which contribute to intensified competition for funding. Additionally, research indicates a lack of awareness, willingness, expertise and organizational preparedness. Size-specific limitations, such as restricted infrastructure and staff capacity, place smaller NGOs at a further disadvantage [[32](https://arxiv.org/html/2510.15509v1#bib.bibx32)]. Finally, challenges in the environment context include inadequate or absent legal frameworks, structurally disadvantaged digital infrastructure, skill gaps, and restricted data accessibility in low- and lower-middle-income countries [[43](https://arxiv.org/html/2510.15509v1#bib.bibx43)], alongside weak or fragmented partnerships.

The literature proposes several solution pathways. These include initial capacity building through improved data governance and staff training, pilot projects, incremental approaches and leveraging open-source solutions that require less upfront investments compared to in-house products. The suitability of these solutions is strongly shaped by organizational size and geographic context. However, across studies, the most consistently emphasized recommendation is the need for stronger collaborations between NGOs and external actors such as governments, industry, and academia [[34](https://arxiv.org/html/2510.15509v1#bib.bibx34)].

Based on available literature, NGOs should approach AI adoption through a stepwise process that includes initial need assessment, running small pilot projects, ensuring secure data governance, and scaling solutions in collaboration with partners. Donors are advised to fund capacity building, underwrite shared infrastructure, and support the localization of the technology. Policymakers can accelerate adoption by investing in digital infrastructure, create legal clarity on data use, and incentive public-private partnerships. Furthermore, industry partners can contribute by offering discounted or free access for NGOs, developing tailored AI applications, and providing privacy-preserving hosting options.

We acknowledge that this study faces several limitations. First, by excluding non-English literature, we might introduce publication and language bias. Second, although both authors worked independently, regularly cross-checked their results, and followed a predefined research protocol, the small author team still leaves room for potential bias. Third, the sample of investigated studies is skewed toward lower-middle and high-income countries as well as larger NGOs, with many studies positioning NGOs merely as end users or data providers rather than active collaborators. Fourth, the heterogeneity in study designs prevented a meta-analysis, which means we defaulted to narrative and thematic synthesis, which includes inherently subjective elements. Finally, we note that while we also searched for grey literature, there might be possible misses or emerging projects not yet published. As a result, this paper primarily views the issue from an academic perspective.

Future research should prioritize empirical studies of AI adoption in small NGOs and low-income countries to fill in existing research gaps. Additionally, longitudinal studies that track AI adoption over time to test the DOI trajectories and comparative evaluations of open-source vs paid tools in NGOs seem to be desirable. Finally, further investigations into localization (languages, cultural adaptation) of AI tools would provide a foundation for more effective and context-sensitive implementation.

## onclusion

This review examined how NGOs adopt and use AI, with a focus on utilization patterns, barriers, and solutions across different organizational and geographic contexts. In sum, it shows that AI is currently being used by NGOs primarily for engagement, optimization, decision-support, management, creative, and predictive purposes, with structured uptake concentrated among larger organizations (RQ1). The main barriers are technical capacity, organizational resources, and environmental constraints such as funding and infrastructure, while feasible solutions include partnerships, capacity-building, and governance frameworks that ensure ethical and context-sensitive use (RQ2). Overall, AI is promising, but adoption remains uneven. Over the next five years, policies should prioritize equitable capacity building, supportive infrastructure, and ethical guidelines to ensure smaller NGOs and those from lower-income contexts are not left behind. At the same time, research should expand to underrepresented contexts and investigate longitudinal patterns of AI adoption to inform sustainable strategies.

## tatements and Declarations

The authors have no competing interests to declare that are relevant to the content of this article. Additionally, they did not receive support from any organization for the submitted work.

## cknowledgements

Special thanks is attributed to Grow Ghana, a Ghanian NGO, that was one of the main motivations to conduct this work.

In some parts, we used ChatGPT version 5 for grammar polishing and style fixes. These contributions were minor and all content was reviewed and edited by the authors.

## References

* [1]
   Grand View Research, Inc.
  “Artificial Intelligence Market Size, Share & Trends Analysis Report By Solution, By Technology (Deep Learning, Machine Learning, NLP, Machine Vision, Generative AI), By Function, By End-Use, By Region, And Segment Forecasts, 2025–2030” Forecast period: 2025–2030, 2025
  URL: <https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-market>
* [2]
  Satwik Mamidi
  “Integration of AI-Powered Analytics for Donor Behavior Insights”
  In *Progress in Medical Sciences* 7.2, 2023, pp. 1–4
  DOI: [10.47363/PMS/2023(7)E127](https://dx.doi.org/10.47363/PMS/2023(7)E127)
* [3]
  Marie-E Godefroid, Ralf Plattfaut and Björn Niehaves
  “Identifying key barriers to nonprofit organizations’ adoption of technology innovations”
  In *Nonprofit Management and Leadership* 35.1
  Wiley Online Library, 2024, pp. 237–259
  DOI: [10.1002/nml.21609](https://dx.doi.org/10.1002/nml.21609)
* [4]
  Pamela Eng’airo
  “The Impact of AI-Driven Performance Evaluation on Organizational Outcomes in Kenya: A Systematic Literature Review”
  In *Journal of Information and Technology* 8.2, 2024, pp. 1–15
  DOI: [10.53819/81018102t7040](https://dx.doi.org/10.53819/81018102t7040)
* [5]
  Daniel Schiff, Jason Borenstein, Justin Biddle and Kelly Laas
  “AI ethics in the public, private, and NGO sectors: A review of a global document collection”
  In *IEEE Transactions on Technology and Society* 2.1
  IEEE, 2021, pp. 31–42
  DOI: [10.1109/TTS.2021.3052127](https://dx.doi.org/10.1109/TTS.2021.3052127)
* [6]
  Nina Tomazevic, Eva Murko and Aleksander Aristovnik
  “Organizational Enablers of Artificial Intelligence Adoption in Public Institutions: A Systematic Literature Review”
  In *Cent. Eur. Pub. Admin. Rev.* 22
  HeinOnline, 2024, pp. 109
  DOI: [10.17573/cepar.2024.1.05](https://dx.doi.org/10.17573/cepar.2024.1.05)
* [7]
  Ianire Taboada, Abouzar Daneshpajouh, Nerea Toledo and Tharaka De Vass
  “Artificial intelligence enabled project management: a systematic literature review”
  In *Applied Sciences* 13.8
  MDPI, 2023, pp. 5014
  DOI: [10.3390/app13085014](https://dx.doi.org/10.3390/app13085014)
* [8]
  Stuart J. Russell and Peter Norvig
  “Artificial Intelligence: A Modern Approach”
  Upper Saddle River, NJ: Pearson, 2020
* [9]
  Luz M Muñoz Marquez
  “The relevance of organizational structure to NGOs’ approaches to the policy process”
  In *VOLUNTAS: International Journal of Voluntary and Nonprofit Organizations* 27.1
  Springer, 2016, pp. 465–486
  DOI: [10.1007/s11266-015-9555-5](https://dx.doi.org/10.1007/s11266-015-9555-5)
* [10]
  Louis G. Tornatzky and Mitchell Fleischer
  “The Processes of Technological Innovation”
  Lexington, MA: Lexington Books, 1990
* [11]
  Kevin Zhu and Kenneth L Kraemer
  “Post-adoption variations in usage and value of e-business by organizations: cross-country evidence from the retail industry”
  In *Information systems research* 16.1
  INFORMS, 2005, pp. 61–84
  DOI: [10.1287/isre.1050.0045](https://dx.doi.org/10.1287/isre.1050.0045)
* [12]
  Everett M. Rogers
  “Diffusion of Innovations”
  New York: Free Press, 2003
* [13]
  Jeff Baker
  “The Technology–Organization–Environment Framework”
  In *Information Systems Theory: Explaining and Predicting Our Digital Society* 28
  Springer, 2011, pp. 231–245
  DOI: [10.1007/978-1-4419-6108-2˙12](https://dx.doi.org/10.1007/978-1-4419-6108-2_12)
* [14]
  Rifat Ara Shams, Didar Zowghi and Muneera Bano
  “AI and the quest for diversity and inclusion: a systematic literature review”
  In *AI and Ethics* 5.1
  Springer, 2025, pp. 411–438
  DOI: [10.1007/s43681-023-00362-w](https://dx.doi.org/10.1007/s43681-023-00362-w)
* [15]
  Matthew J Page et al.
  “The PRISMA 2020 statement: an updated guideline for reporting systematic reviews”
  In *bmj* 372
  British Medical Journal Publishing Group, 2021
  DOI: [10.1136/bmj.n71](https://dx.doi.org/10.1136/bmj.n71)
* [16]
  Alison Cooke, David Smith and Andrew Booth
  “Beyond PICO: The SPIDER Tool for Qualitative Evidence Synthesis”
  In *Qualitative Health Research* 22.10, 2012, pp. 1435–1443
  DOI: [10.1177/1049732312452938](https://dx.doi.org/10.1177/1049732312452938)
* [17]
  W Scott Richardson, Mark C Wilson, Jim Nishikawa and Robert S Hayward
  “The well-built clinical question: a key to evidence-based decisions.”
  In *ACP journal club* 123.3, 1995, pp. A12–3
* [18]
  Alberto Martín-Martín, Mike Thelwall, Enrique Orduna-Malea and Emilio Delgado López-Cózar
  “Google Scholar, Microsoft Academic, Scopus, Dimensions, Web of Science, and OpenCitations’ COCI: a multidisciplinary comparison of coverage via citations”
  In *Scientometrics* 126.1
  Springer, 2021, pp. 871–906
  DOI: [10.1007/s11192-020-03690-4](https://dx.doi.org/10.1007/s11192-020-03690-4)
* [19]
  William H Walters
  “Comparing conventional and alternative mechanisms of discovering and accessing the scientific literature”
  In *Proceedings of the National Academy of Sciences* 122.27
  National Academy of Sciences, 2025, pp. e2503051122
  DOI: [10.1073/pnas.2503051122](https://dx.doi.org/10.1073/pnas.2503051122)
* [20]
  Richard J Adams, Palie Smart and Anne Sigismund Huff
  “Shades of grey: guidelines for working with the grey literature in systematic reviews for management and organizational studies”
  In *International journal of management reviews* 19.4
  Wiley Online Library, 2017, pp. 432–454
  DOI: [10.1111/ijmr.12102](https://dx.doi.org/10.1111/ijmr.12102)
* [21]
  Terri D Pigott and Joshua R Polanin
  “Methodological guidance paper: High-quality meta-analysis in a systematic review”
  In *Review of Educational Research* 90.1
  SAGE Publications Sage CA: Los Angeles, CA, 2020, pp. 24–46
  DOI: [10.3102/0034654319877153](https://dx.doi.org/10.3102/0034654319877153)
* [22]
  Julian Hirt, Thomas Nordhausen, Christian Appenzeller-Herzog and Hannah Ewald
  “Citation tracking for systematic literature searching: A scoping review”
  In *Research Synthesis Methods* 14.3
  Wiley Online Library, 2023, pp. 563–579
  DOI: [10.1002/jrsm](https://dx.doi.org/10.1002/jrsm)
* [23]
   Critical Appraisal Skills Programme (CASP)
  “CASP Qualitative Studies Checklist” Accessed: 2025-08-16, 2018
  URL: <https://casp-uk.net/casp-tools-checklists/qualitative-studies-checklist/>
* [24]
  Mohammed A Mohammed, Rebekah J Moles and Timothy F Chen
  “Meta-synthesis of qualitative research: the challenges and opportunities”
  In *International journal of clinical pharmacy* 38.3
  Springer, 2016, pp. 695–704
  DOI: [10.1007/s11096-016-0289-2](https://dx.doi.org/10.1007/s11096-016-0289-2)
* [25]
  Eric Metreau, Kathryn Elizabeth Young and Shwetha Grace Eapen
  “World Bank country classifications by income level for 2024–2025” Accessed: 2025-09-02, 2024
  World Bank Group
  URL: <https://blogs.worldbank.org/en/opendata/world-bank-country-classifications-by-income-level-for-2024-2025>
* [26]
  Rameshwar Dubey et al.
  “Impact of artificial intelligence-driven big data analytics culture on agility and resilience in humanitarian supply chain: A practice-based view” Special Issue celebrating Volume 250 of the International Journal of Production Economics
  In *International Journal of Production Economics* 250, 2022, pp. 108618
  DOI: [https://doi.org/10.1016/j.ijpe.2022.108618](https://dx.doi.org/https://doi.org/10.1016/j.ijpe.2022.108618)
* [27]
  A. Atalay et al.
  “Artificial Intelligence Technologies as Smart Solutions for Sustainable Protected Areas Management”
  In *Sustainability* 17.11, 2025, pp. 5006
  DOI: [10.3390/su17115006](https://dx.doi.org/10.3390/su17115006)
* [28]
  E. Ahatsi and O.. Olanrewaju
  “Enhancing Humanitarian Supply Chain Resilience: Evaluating Artificial Intelligence and Big Data Analytics in Two Nations”
  In *Logistics* 9.2, 2025, pp. 64
  DOI: [10.3390/logistics9020064](https://dx.doi.org/10.3390/logistics9020064)
* [29]
  Veronica Scuotto, Kingsley Obi Omeihe, Valentina Cillo and Del Giudice Manlio
  “Tackling the empowerment of Artificial Intelligence for humanitarian intervention from Save the Children”
  In *Technological Forecasting and Social Change* 221, 2025, pp. 124330
  DOI: [https://doi.org/10.1016/j.techfore.2025.124330](https://dx.doi.org/https://doi.org/10.1016/j.techfore.2025.124330)
* [30]
  Nejc Brezovar
  “The Role of Artificial Intelligence in NGOs: Challenges and Opportunities for Slovenia’s Information Society”
  In *NISPAcee Journal of Public Administration and Policy* 18, 2025, pp. 11–30
  DOI: [10.2478/nispa-2025-0002](https://dx.doi.org/10.2478/nispa-2025-0002)
* [31]
  Amirmohammad Kazemeini et al.
  “A Dataset-Driven Study of AI Opportunities in the Climate NGO Ecosystem”
  In *Proceedings of the 2025 ACM SIGCAS/SIGCHI Conference on Computing and Sustainable Societies*, COMPASS ’25
  New York, NY, USA: Association for Computing Machinery, 2025, pp. 780–785
  DOI: [10.1145/3715335.3744894](https://dx.doi.org/10.1145/3715335.3744894)
* [32]
  Macdonald Dube, Sibusisiwe Dube and Belinda Mutunhu Ndlovu
  “Factors Influencing the Adoption of AI Chatbots By Non- Governmental Organizations”, 2024
  DOI: [10.46254/EU07.20240155](https://dx.doi.org/10.46254/EU07.20240155)
* [33]
  Luisa Regina Hahn, Lina Hartmann, Anita Knjasew and Felicia Maria Weißer
  “From Data to Donors: Can AI Reshape Fundraising Strategies”
  In *Strategic Communication in Disruptive Times: How Sociopolitical Polarization, Virtual Media and AI Reshape Organizational Communication*, 2025, pp. 115–137
* [34]
  Omar Faruq et al.
  “AI-Driven Strategies for Enhancing Non-Profit Organizational Impact”, 2024
  DOI: [10.62127/aijmr.2024.v02i05.1088](https://dx.doi.org/10.62127/aijmr.2024.v02i05.1088)
* [35]
  Rayid Ghani
  “Machine Learning for Social Good: Applications in Non-Profit and Public Sectors”
  In *American Journal of Machine Learning* 2.4, 2021
* [36]
  Mustafa Osman I. Elamin
  “Modernizing the Charitable Sector through Artificial Intelligence: Enhancing Efficiency and Impact”
  In *Journal of Ecohumanism* 3.4
  Transnational Press London, 2024, pp. 3426–3443
* [37]
  Leila Toplic
  “AI in the Humanitarian Sector” Accessed: 2025-09-01, 2020
  NetHope - NewsPress Releases
  URL: <https://reliefweb.int/report/world/ai-emergency-response-not-time-experiments>
* [38]
  Sal Khan and Anuliina Savolainen
  “Sal Khan: ”I see AI as an additional tool, but a very powerful one””
  In *The UNESCO Courier* 4, 2023, pp. 12–14
  URL: <https://unesdoc.unesco.org/ark:/48223/pf0000387033_eng>
* [39]
  Marwa Soudi, Esraa Ali, Maha Bali and Nihal Mabrouk
  “Generative AI-Based Tutoring System for Upper Egypt Community Schools”
  In *Proceedings of the 2023 Conference on Human Centered Artificial Intelligence: Education and Practice*, HCAIep ’23
  Dublin, Ireland: Association for Computing Machinery, 2023, pp. 16–21
  DOI: [10.1145/3633083.3633085](https://dx.doi.org/10.1145/3633083.3633085)
* [40]
  Iris-Panagiota Efthymiou, Antonios Alevizos and Symeon Sidiropoulos
  “The Role of Artificial Intelligence in Revolutionizing NGOs’ Work”
  In *Journal of Politics and Ethics in New Technologies and AI* 2, 2023, pp. 1–7
  DOI: [10.12681/jpentai.35137](https://dx.doi.org/10.12681/jpentai.35137)
* [41]
  Daniela Weber
  “AI in Emergency Response: Not the Time for Experiments” Accessed: 2025-09-01, 2024
  NetHope - NewsPress Releases
  URL: <https://reliefweb.int/report/world/ai-emergency-response-not-time-experiments>
* [42]
  Yang Cheng and Yuan Wang
  “Leveraging Artificial Intelligence–Powered Chatbots for Nonprofit Organizations: Examining the Antecedents and Outcomes of Chatbot Trust and Social Media Engagement”
  In *Journal of Philanthropy* 30.1, 2025, pp. Article e70013
  DOI: [10.1002/nvsm.70013](https://dx.doi.org/10.1002/nvsm.70013)
* [43]
  Vineet Nair et al.
  “ADVISER: AI-Driven Vaccination Intervention Optimiser for Increasing Vaccine Uptake in Nigeria”
  In *Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI-22), AI for Good Track*, 2022
  DOI: [10.48550/arXiv.2204.13663](https://dx.doi.org/10.48550/arXiv.2204.13663)
* [44]
  A. Mate et al.
  “Field Study in Deploying Restless Multi-Armed Bandits: Assisting Non-profits in Improving Maternal and Child Health”
  In *Proceedings of the AAAI Conference on Artificial Intelligence* 36.11, 2022, pp. 12017–12025
  DOI: [10.1609/aaai.v36i11.21460](https://dx.doi.org/10.1609/aaai.v36i11.21460)
* [45]
  N. Rathore, P.. Jain and M. Parida
  “A Sustainable Model for Emergency Medical Services in Developing Countries: A Novel Approach Using Partial Outsourcing and Machine Learning”
  In *Risk Management and Healthcare Policy* 15, 2022, pp. 193–218
  DOI: [10.2147/RMHP.S338186](https://dx.doi.org/10.2147/RMHP.S338186)
* [46]
  Ahmad Alhindi, Abrar Alsaidi, Waleed Alasmary and Maazen Alsabaan
  “Vehicle Routing Optimization for Surplus Food in Nonprofit Organizations”
  In *International Journal of Advanced Computer Science and Applications* 11, 2020, pp. 680
  DOI: [10.14569/IJACSA.2020.0110384](https://dx.doi.org/10.14569/IJACSA.2020.0110384)
* [47]
  Elisabeth T. Pereira and Muhammad Noman Shafique
  “The Role of Artificial Intelligence in Supply Chain Agility: A Perspective of Humanitarian Supply Chain”
  In *Engineering Economics* 35.1, 2024
  DOI: [10.5755/j01.ee.35.1.32928](https://dx.doi.org/10.5755/j01.ee.35.1.32928)
* [48]
  Mohammad Arije Ulfy, Ahasanul Haque and Md. Huda
  “Integration of Artificial Intelligence in Biodegradable Plastic Packaging Design: Exploring Stakeholder Attitudes”, SSRN Electronic Journal, 2025
  DOI: [10.2139/ssrn.5367646](https://dx.doi.org/10.2139/ssrn.5367646)
* [49]
  Sethika Manumitha Kapuge and Thepul NDS Ginige
  “Optimizing AI recommendation algorithms for efficient matching of most needed beneficiaries with donors in Sri Lankan charity sector”
  In *DATA SCIENCE AND AI-I 1-6*, 2024, pp. 63
* [50]
  Akanksha A Pai, Ramakanth Kumar P, Sharon Thomas and Pratiba D
  “NGO CONNECT: Technology for Non-Profit Organisation Management”
  In *2023 7th International Conference on Computation System and Information Technology for Sustainable Solutions (CSITSS)*, 2023, pp. 1–6
  DOI: [10.1109/CSITSS60515.2023.10334076](https://dx.doi.org/10.1109/CSITSS60515.2023.10334076)
* [51]
  Karshiboyeva Laylo
  “The impact of AI and information technologies on Islamic charity (zakat): Modern solutions for efficient distribution”
  In *International Journal of Law and Policy* 1.5, 2023, pp. 1–8
* [52]
  Shailaja Uke et al.
  “FoodSavior: Distributing Surplus Food to NGOs or Manure Producers Using Internet of Things and Machine Learning”
  In *2024 International Conference on Sustainable Communication Networks and Application (ICSCNA)*, 2024, pp. 146–153
  DOI: [10.1109/ICSCNA63714.2024.10863911](https://dx.doi.org/10.1109/ICSCNA63714.2024.10863911)
* [53]
  Victoire Amalraj, M. Vasuki and S. Anitha
  “A machine learning approach to categorizing countries by socio-economic and health development factors using PCA, K-means, and silhouette scoring”
  In *International Scientific Journal of Engineering and Management* 04.06, 2025
  DOI: [10.55041/ISJEM03977](https://dx.doi.org/10.55041/ISJEM03977)
* [54]
  Norta Alex and Makrygiannis Sotiris
  “Designing Artificial Intelligence Equipped Social Decentralized Autonomous Organizations for Tackling Sextortion Cases Version 0.7”
  In *arXiv preprint arXiv:2312.14090*, 2023
* [55]
  Rohan Gupta et al.
  “AI Based Cyberbullying Detection and Prevention”
  In *2024 3rd Edition of IEEE Delhi Section Flagship Conference (DELCON)*, 2024, pp. 1–6
  DOI: [10.1109/DELCON64804.2024.10866680](https://dx.doi.org/10.1109/DELCON64804.2024.10866680)
* [56]
  H. Huang
  “Technology-Driven Financial Risk Management: Exploring the Benefits of Machine Learning for Non-Profit Organizations”
  In *Systems* 12.10, 2024, pp. 416
  DOI: [10.3390/systems12100416](https://dx.doi.org/10.3390/systems12100416)
* [57]
  David Krause
  “AI Agents and Automation in Small Non-Profit Organizations’ Accounting Functions”, SSRN Electronic Journal, 2025
  DOI: [10.2139/ssrn.5082437](https://dx.doi.org/10.2139/ssrn.5082437)
* [58]
  Bedoor Bahameish, Mohammed Yaqot, R. Franzoi and Brenno Menezes
  “Artificial Intelligence in Procurement: An Overview and Case Study of Qatar Foundation”, 2023
  DOI: [10.46254/EU05.20220146](https://dx.doi.org/10.46254/EU05.20220146)
* [59]
  Sanjana K, Asha G R and Nandhini Vineeth
  “Integrating Transparent Crowdfunding Platform and AI-Based Treatment Fund Estimation”
  In *2024 2nd DMIHER International Conference on Artificial Intelligence in Healthcare, Education and Industry (IDICAIEI)*, 2024, pp. 1–6
  DOI: [10.1109/IDICAIEI61867.2024.10842939](https://dx.doi.org/10.1109/IDICAIEI61867.2024.10842939)
* [60]
  A. Alnamrouti, H. Rjoub and H. Ozgit
  “Do Strategic Human Resources and Artificial Intelligence Help to Make Organisations More Sustainable? Evidence from Non-Governmental Organisations”
  In *Sustainability* 14.12, 2022, pp. 7327
  DOI: [10.3390/su14127327](https://dx.doi.org/10.3390/su14127327)
* [61]
  Avetis Avagyan and Hae-Yeon Alice Jeong
  “Utilizing artificial intelligence for equitable and efficient volunteer selection” Accessed: 2025-09-01, 2020
  UN Volunteers
  URL: <https://www.unv.org/Success-stories/utilizing-artificial-intelligence-equitable-and-efficient-volunteer-selection>
* [62]
  Michael Asajile, Silverius Komba and Crispin Mbogo
  “Influence of Artificial Intelligence on Selection Stage of Recruitment in Tanzania: A Case of Selected NGOs in Kinondoni Municipality”
  In *International Journal of Research and Innovation in Social Science (IJRISS)* 8.12, 2024, pp. 3406–3416
* [63]
  Debolina Dutta and Anasha Kannan Poyil
  “The machine/human agentic impact on practices in learning and development: A study across MSME, NGO and MNC organizations”
  In *Personnel Review* 53.3, 2024, pp. 791–815
  DOI: [10.1108/PR-09-2022-0658](https://dx.doi.org/10.1108/PR-09-2022-0658)
* [64]
  M.K.Jayanthi Kannan et al.
  “AI-Driven Digital Volunteering @ Freelancing Website for NGO Collaboration with Online Talent Worldwide”, 2025, pp. 6600–6613
  DOI: [10.15680/IJMRSET.2025.0804405](https://dx.doi.org/10.15680/IJMRSET.2025.0804405)
* [65]
  R Bhuvaneswari, Dhivya Shree K, Divya Dharshini K and Farheen Tabassum H
  “UniteVol: AI-Powered Social Impact and Leadership Platform”
  In *2025 6th International Conference on Data Intelligence and Cognitive Informatics (ICDICI)*, 2025, pp. 1703–1707
  DOI: [10.1109/ICDICI66477.2025.11135302](https://dx.doi.org/10.1109/ICDICI66477.2025.11135302)
* [66]
  Ruchi Sharma, Parv Dave and Jay Chaudhary
  “OCR for Data Retrieval :An analysis and Machine Learning Application model for NGO social volunteering”
  In *2021 Fifth International Conference on I-SMAC (IoT in Social, Mobile, Analytics and Cloud) (I-SMAC)*, 2021, pp. 422–427
  DOI: [10.1109/I-SMAC52330.2021.9640890](https://dx.doi.org/10.1109/I-SMAC52330.2021.9640890)
* [67]
  Divija Joshi
  “SmartNGO: An Integrated Platform for Managing Volunteers and Events”
  In *INTERNATIONAL JOURNAL OF SCIENTIFIC RESEARCH IN ENGINEERING AND MANAGEMENT* 09, 2025, pp. 1–9
  DOI: [10.55041/IJSREM46660](https://dx.doi.org/10.55041/IJSREM46660)
* [68]
  Cristina Raluca Gh Popescu and Jarmila Duháček Šebestová
  “The Impact of Artificial Intelligence on Intellectual Capital Development: Shifting Requirements for Professions and Processes in the Non-Profit Sector”
  In *Journal of Infrastructure Policy and Development* 8, 2024, pp. 3899
  DOI: [10.24294/jipd.v8i10.3899](https://dx.doi.org/10.24294/jipd.v8i10.3899)
* [69]
  Sakina Hansen
  “Exclusion or Efficiency: Understanding Perspectives about AI Ethics Among Charity Workers in the United Kingdom”
  In *Proceedings of the Fourth European Workshop on Algorithmic Fairness (EWAF’25)*, Proceedings of Machine Learning Research, 2025
* [70]
  Holger Sievert and Marco Inderhees
  “AI, Diversity and Trust in Digital Non-Profit Communication: Results of a Survey within the Major Traditional Churches of a Western European Country”, SSRN Electronic Journal, 2024
  DOI: [10.2139/ssrn.5087283](https://dx.doi.org/10.2139/ssrn.5087283)
* [71]
  B. Sandberg, R. Wasif and L.. Hand
  “Addressing the promise and peril of AI for nonprofit management through a data feminist pedagogy”
  In *Journal of Public Affairs Education* 31.2, 2025, pp. 192–212
  DOI: [10.1080/15236803.2025.2475589](https://dx.doi.org/10.1080/15236803.2025.2475589)
* [72]
  Marcus Sammer et al.
  “AI-FEED: Prototyping an AI-Powered Platform for the Food Charity Ecosystem”
  In *International Journal of Computational Intelligence Systems* 17, 2024, pp. 259
  DOI: [10.1007/s44196-024-00656-9](https://dx.doi.org/10.1007/s44196-024-00656-9)
* [73]
  J.. Rafner et al.
  “Crea.visions: A Platform for Casual Co-Creation with a Purpose Envisioning the Future through Human-AI Collaboration with Multiple Stakeholders” <https://openaccess.city.ac.uk/id/eprint/30700/>, Open Access Report, 2023
* [74]
  Emilia Grass, Janosch Ortmann, Burcu Balcik and Walter Rei
  “A Machine Learning Approach to Deal with Ambiguity in the Humanitarian Decision-Making” Handling Editor: Sushil Gupta
  In *Production and Operations Management* 32.9, 2023, pp. 2956–2974
  DOI: [10.1111/poms.14018](https://dx.doi.org/10.1111/poms.14018)
* [75]
  Isabelle Tingzon et al.
  “Mapping New Informal Settlements Using Machine Learning and Time Series Satellite Images: An Application in the Venezuelan Migration Crisis”
  In *2020 IEEE / ITU International Conference on Artificial Intelligence for Good (AI4G)*, 2020, pp. 198–203
  DOI: [10.1109/AI4G50087.2020.9311041](https://dx.doi.org/10.1109/AI4G50087.2020.9311041)
* [76]
  Cristina Blasi Casagran and Georgios Stavropoulos
  “Developing AI Predictive Migration Tools to Enhance Humanitarian Support: The Case of EUMigraTool”
  In *Data & Policy* 6, 2024, pp. e64
  DOI: [10.1017/dap.2024.76](https://dx.doi.org/10.1017/dap.2024.76)
* [77]
  Zaid Kbah and Erica Gralla
  “Understanding Enablers and Barriers for Deploying AI/ML in Humanitarian Organizations: the Case of DRC’s Foresight”
  In *Proceedings of the IISE Annual Conference & Expo 2023*, 2023
* [78]
  Emmanuel Ahatsi and Oludolapo Akanni Olanrewaju
  “Resilience in Humanitarian Supply Chains: Addressing Artificial Intelligence and Big Data Hurdles Across Borders”
  In *Engineering Reports* 7.7
  Wiley Online Library, 2025, pp. e70310
  DOI: [https://doi.org/10.1002/eng2.70310](https://dx.doi.org/https://doi.org/10.1002/eng2.70310)
* [79]
  Mahfuzur Rahman et al.
  “Development of flood hazard map and emergency relief operation system using hydrodynamic modeling and machine learning algorithm”
  In *Journal of Cleaner Production* 311, 2021, pp. 127594
  DOI: [https://doi.org/10.1016/j.jclepro.2021.127594](https://dx.doi.org/https://doi.org/10.1016/j.jclepro.2021.127594)
* [80]
  Maryam Tabar et al.
  “Forecasting the Number of Tenants At-Risk of Formal Eviction: A Machine Learning Approach to Inform Public Policy”, 2022, pp. 5144–5150
  DOI: [10.24963/ijcai.2022/715](https://dx.doi.org/10.24963/ijcai.2022/715)
* [81]
  Y. Kravchuk
  “Ethical Implications of AI Applications in Nonprofit and Charity Sectors”
  In *COMPUTER-INTEGRATED TECHNOLOGIES: EDUCATION, SCIENCE, PRODUCTION* 58, 2025, pp. 46–52
  DOI: [10.36910/6775-2524-0560-2025-58-06](https://dx.doi.org/10.36910/6775-2524-0560-2025-58-06)
* [82]
  S. Niranjana
  “AI for Sustainable Development: Assessing Student Interest, Education, and Career Pathways”
  In *EPRA International Journal of Research and Development (IJRD)* 8.10, 2023
  DOI: [10.36713/epra14795](https://dx.doi.org/10.36713/epra14795)
* [83]
  Francisco Enrique Vicente Castro et al.
  “AI + Dance: Co-Designing Culturally Sustaining Curricular Resources for AI and Ethics Education Through Artistic Computing”
  In *Proceedings of the 2022 ACM Conference on International Computing Education Research - Volume 2*, ICER ’22
  LuganoVirtual Event, Switzerland: Association for Computing Machinery, 2022, pp. 26–27
  DOI: [10.1145/3501709.3544275](https://dx.doi.org/10.1145/3501709.3544275)
* [84]
  D. Defnizal and R.. Ernes
  “The Implementation of Artificial Intelligence in Charity Box at Mosque and Musholla as RFID Based Security System”
  In *Sinkron: Jurnal Dan Penelitian Teknik Informatika* 5.1, 2020, pp. 35–42
  DOI: [10.33395/sinkron.v5i1.10594](https://dx.doi.org/10.33395/sinkron.v5i1.10594)
* [85]
  NetHope - News and Press Releases
  “Empowering Humanitarian Response Through Crisis Informatics” Accessed: 2025-09-01, 2024
  URL: <https://reliefweb.int/report/world/ai-emergency-response-not-time-experiments>
* [86]
  Gianluca Iazzolino
  “Trading efficiency for control: The AI conundrum in migration management”
  In *Cosmopolitan Civil Societies: An Interdisciplinary Journal* 17.1
  UTS ePress Sydney, 2025, pp. 35–46
  DOI: [https://doi.org/10.5130/ccs.v17.i1.9423](https://dx.doi.org/https://doi.org/10.5130/ccs.v17.i1.9423)
* [87]
  Chen Yang, Yi Yang and Yuezi Zhang
  “Understanding the impact of artificial intelligence on the justice of charitable giving: The moderating role of trust and regulatory orientation”
  In *Journal of Consumer Behaviour* 23.5, 2024, pp. 2624–2636
  DOI: [10.1002/cb.2365](https://dx.doi.org/10.1002/cb.2365)
* [88]
  L. Arango, S.. Singaraju and O. Niininen
  “Consumer responses to AI-generated charitable giving ads”
  In *Journal of Advertising* 52.4, 2023, pp. 486–503
  DOI: [10.1080/00913367.2023.2183285](https://dx.doi.org/10.1080/00913367.2023.2183285)
* [89]
  Daniela Weber
  “Amplifying the efforts of nonprofit organizations with AI” Accessed: 2025-09-01, 2023
  NetHope - NewsPress Releases
  URL: <https://reliefweb.int/report/world/ai-emergency-response-not-time-experiments>
* [90]
  M. Thalor et al.
  “Green Mapper: An AI-Driven Initiative for Aerial Tree Mapping, Maintaining Environmental Balance”
  In *Current Agricultural Research Journal* 12.2, 2024
  DOI: [10.12944/CARJ.12.2.34](https://dx.doi.org/10.12944/CARJ.12.2.34)

## Appendix A Search Queries

Table 1: Initial search strings and results

| Digital library | Search string | Search time | No. of |
| --- | --- | --- | --- |
|  |  |  | papers |
| Google Scholar | (”artificial intelligence” OR AI OR ”machine learning” OR ML) AND (”non-governmental organization\*” OR NGO\* OR ”non-profit\*” OR ”charity\*” OR ”humanitarian\*” OR ”aid organization\*”) AND (”social impact” OR ”social good” OR ”community development” OR ”sustainability” OR ”disaster response” OR ”refugee support”) | 18/08/2025 | 18,300 |
| OpenAlex | ’abstract.search:((”artificial intelligence” OR ”machine learning” OR ”AI”) AND (”non-governmental organization” OR NGO OR ”non-profit organization” OR ”humanitarian organization”)),’ ’default.search:(”social impact” OR ”social good” OR ”community development” OR ”sustainability” OR ”disaster response” OR ”refugee support”)’ ), | 18/08/2025 | 339 |




Table 2: Refined search strings and results

| Digital library | Search string | Search time | No. of |
| --- | --- | --- | --- |
|  |  |  | papers |
| Google Scholar | (intitle:”artificial intelligence” OR intitle:”machine learning” OR intitle:AI OR intitle:”Natural language processing” OR intitle:NLP) AND (intitle:”non-governmental\*” OR intitle:NGO OR intitle:”non-profit\*” OR intitle:”humanitarian organization” OR intitle:”charity” OR intitle:”civil society organization”) AND (”humanitarian aid” OR ”disaster response” OR ”refugee support” OR ”community development” OR ”education” OR ”public health” OR ”development aid” OR ”crisis management” OR ”poverty alleviation” OR ”sustainability” OR ”human rights” OR ”education”) | 18/08/2025 | 47 |
| Open Alex | ’title.search:(”artificial intelligence” OR ”machine learning” OR ”AI”),’ ’abstract.search:(”non-governmental organization” OR NGO OR ”non-profit organization” OR ”humanitarian organization”),’ ’default.search:(”humanitarian aid” OR ”disaster response” OR ”refugee support” OR ”community development” OR ”education” OR ”public health” OR ”development aid” OR ”crisis management” OR ”poverty alleviation” OR ”sustainability” OR ”human rights”)’ | 18/08/2025 | 129 |
| Scopus | Title: (”artificial intelligence” OR ”machine learning” OR ”AI”) AND Abstract: (”non-governmental organization” OR NGO OR ”non-profit organization” OR ”humanitarian organization”) AND All fields: (”humanitarian aid” OR ”disaster response” OR ”refugee support” OR ”community development” OR ”education” OR ”public health” OR ”development aid” OR ”crisis management” OR ”poverty alleviation” OR ”sustainability” OR ”human rights”) | 01/10/2025 | 91 |
| Relief Web | (”artificial intelligence” OR ”machine learning” OR ”AI”) AND (”adoption” OR ”implementation” OR ”strategy”) AND (”NGO” OR ”non-governmental organization” OR ”nonprofit” OR ”NPO” OR ”charity” OR ”aid organization”) [using filter for Non-Governmental Organization] | 18/08/2025 | 83 |

## Appendix B Thematic Map

![Refer to caption](thematic_mapping.png)


Figure 6: Thematic mapping. Note that each thematic category contains multiple sub-themes. For reasons of visual clarity, only the main themes are displayed here. For a mapping of used sub-themes to concrete papers please refer to the [additional material](https://osf.io/a2357/?view_only=7120b178719540608dc97cd2a178ceff).

## Appendix C Overview of Included Studies

Table 3: Included studys from 2020

| Authors | Title | Type | Discussed Topics | Citation |
| --- | --- | --- | --- | --- |
| Tingzon et al. | Mapping New Informal Settlements Using Machine Learning and Time Series Satellite Images: An Application in the Venezuelan Migration Crisis | Conference paper | Use Cases, Solutions | [[75](https://arxiv.org/html/2510.15509v1#bib.bibx75)] |
| Defnizal & Ernes | The Implementation of Artificial Intelligence in Charity Box at Mosque and Musholla as RFID Based Security System | Article | Use cases | [[84](https://arxiv.org/html/2510.15509v1#bib.bibx84)] |
| Alhindi et al. | Vehicle routing optimization for surplus food in nonprofit organizations | Article | Use cases, Solutions | [[46](https://arxiv.org/html/2510.15509v1#bib.bibx46)] |
| Toplic | AI in the Humanitarian Sector | NGO paper | Use Cases, Challenges, Solutions | [[37](https://arxiv.org/html/2510.15509v1#bib.bibx37)] |
| Avagyan & Jeong | Utilizing Artificial Intelligence for Equitable and Efficient Volunteer Selection | NGO paper | Use cases, Solutions | [[61](https://arxiv.org/html/2510.15509v1#bib.bibx61)] |




Table 4: Included studys from 2021

| Authors | Title | Type | Discussed Topics | Citation |
| --- | --- | --- | --- | --- |
| Ghani | Machine Learning for Social Good: Applications in Non-Profit and Public Sectors | Article | Use cases, Challenges, Solutions | [[35](https://arxiv.org/html/2510.15509v1#bib.bibx35)] |
| Rahman et al. | Development of flood hazard map and emergency relief operation system using hydrodynamic modeling and machine learning algorithm | Article | Use cases, Solutions | [[79](https://arxiv.org/html/2510.15509v1#bib.bibx79)] |
| Sharma et al. | OCR for Data Retrieval: An analysis and Machine Learning Application model for NGO social volunteering | Conference paper | Use cases, Challenges | [[66](https://arxiv.org/html/2510.15509v1#bib.bibx66)] |




Table 5: Included studys from 2022

| Authors | Title | Type | Discussed Topics | Citation |
| --- | --- | --- | --- | --- |
| Dubey et al. | Impact of artificial intelligence-driven big data analytics culture on agility and resilience in humanitarian supply chain: A practice-based view | Article | Use Cases, Challenges | [[26](https://arxiv.org/html/2510.15509v1#bib.bibx26)] |
| Castro et al. | AI + Dance: Co-Designing Culturally Sustaining Curricular Resources for AI and Ethics Education Through Artistic Computing | Conference paper | Use Cases | [[83](https://arxiv.org/html/2510.15509v1#bib.bibx83)] |
| Rathore et al. | A Sustainable Model for Emergency Medical Services in Developing Countries: A Novel Approach Using Partial Outsourcing and Machine Learning | Article | Use Cases | [[45](https://arxiv.org/html/2510.15509v1#bib.bibx45)] |
| Tabar et al. | Forecasting the Number of Tenants At-Risk of Formal Eviction: A Machine Learning Approach to Inform Public Policy | Article | Use cases, Solutions | [[80](https://arxiv.org/html/2510.15509v1#bib.bibx80)] |
| Nair et al. | ADVISER: AI-Driven Vaccination Intervention Optimiser for Increasing Vaccine Uptake in Nigeria | Conference Paper | Use cases, Challenges, Solutions | [[43](https://arxiv.org/html/2510.15509v1#bib.bibx43)] |
| Alnamrouti et al. | Do Strategic Human Resources and Artificial Intelligence Help to Make Organisations More Sustainable? Evidence from Non-Governmental Organisations | Article | Use cases, Challenges, Solutions | [[60](https://arxiv.org/html/2510.15509v1#bib.bibx60)] |
| Mate et al. | Field study in deploying restless multi-armed bandits: Assisting non-profits in improving maternal and child health | Conference paper | Use cases, Challenges, Solutions | [[44](https://arxiv.org/html/2510.15509v1#bib.bibx44)] |




Table 6: Included studys from 2023

| Authors | Title | Type | Discussed Topics | Citation |
| --- | --- | --- | --- | --- |
| Efthymiou et al. | The Role of Artificial Intelligence in Revolutionizing NGOs’ Work | Article | Use Cases, Challenges, Solutions | [[40](https://arxiv.org/html/2510.15509v1#bib.bibx40)] |
| Grass et al. | A machine learning approach to deal with ambiguity in the humanitarian decision making | Article | Use Cases, Challenges, Solutions | [[74](https://arxiv.org/html/2510.15509v1#bib.bibx74)] |
| Bahameish et al. | Artificial Intelligence in Procurement: An Overview and Case Study of Qatar Foundation | Conference paper | Use Cases, Challenges | [[58](https://arxiv.org/html/2510.15509v1#bib.bibx58)] |
| Soudi et al. | Generative AI-Based Tutoring System for Upper Egypt Community Schools | Conference paper | Use cases, Challenges, Solutions | [[39](https://arxiv.org/html/2510.15509v1#bib.bibx39)] |
| Niranjana | AI for Sustainable Development: Assessing Student Interest, Education, and Career Pathways | Article | Challenges | [[82](https://arxiv.org/html/2510.15509v1#bib.bibx82)] |
| Alex & Sotiris | Designing Artificial Intelligence Equipped Social Decentralized Autonomous Organizations for Tackling Sextortion Cases Version 0.7 | Preprint | Use Cases, Challenges, Solutions | [[54](https://arxiv.org/html/2510.15509v1#bib.bibx54)] |
| Rafner et al. | Crea.visions : A Platform for Casual Co-Creation with a Purpose Envisioning the Future through Human-AI Collaboration with Multiple Stakeholders | Conference Paper | Use cases | [[73](https://arxiv.org/html/2510.15509v1#bib.bibx73)] |
| Laylo | The Impact of AI and Information Technologies on Islamic Charity (Zakat): Modern Solutions for Efficient Distribution | Article | Use cases | [[51](https://arxiv.org/html/2510.15509v1#bib.bibx51)] |
| Pai et al. | NGO CONNECT: Technology for Non-Profit Organisation Management | Conference paper | Use cases, Challenges, Solutions | [[50](https://arxiv.org/html/2510.15509v1#bib.bibx50)] |
| Arango et al. | Consumer Responses to AI-Generated Charitable Giving Ads | Article | Challenges, Solutions | [[88](https://arxiv.org/html/2510.15509v1#bib.bibx88)] |
| Khan & Savolainen | Sal Khan: ”I see AI as an additional tool, but a very powerful one” | Article | Challenges, Solutions | [[38](https://arxiv.org/html/2510.15509v1#bib.bibx38)] |
| Kbah & Gralla | Understanding Enablers and Barriers for Deploying AI/ML in Humanitarian Organizations: the case of DRC’s Foresight | Conference paper | Use cases, Challenges, Solutions | [[77](https://arxiv.org/html/2510.15509v1#bib.bibx77)] |
| Nethope (org.) | Amplifying the efforts of nonprofit organizations with AI | NGO paper | Challenges, Solutions | [[89](https://arxiv.org/html/2510.15509v1#bib.bibx89)] |




Table 7: Included studys from 2024 (Part 1)

| Authors | Title | Type | Discussed Topics | Citation |
| --- | --- | --- | --- | --- |
| Pereira & Shafique | The Role of Artificial Intelligence in Supply Chain Agility: A Perspective of Humanitarian Supply Chain | Article | Use Cases, Solutions | [[47](https://arxiv.org/html/2510.15509v1#bib.bibx47)] |
| Huang | Technology-Driven Financial Risk Management: Exploring the Benefits of Machine Learning for Non-Profit Organizations | Article | Use Cases, Challenges | [[56](https://arxiv.org/html/2510.15509v1#bib.bibx56)] |
| Casagran & Stavropoulos | Developing AI predictive migration tools to enhance humanitarian support: The case of EUMigraTool | Article | Use cases, Challenges, Solutions | [[76](https://arxiv.org/html/2510.15509v1#bib.bibx76)] |
| Asajile et al. | Influence of Artificial Intelligence on Selection Stage of Recruitment in Tanzania: A Case of Selected NGOs in Kinondoni Municipality | Article | Use Cases, Challenges, Solutions | [[62](https://arxiv.org/html/2510.15509v1#bib.bibx62)] |
| Thalor et al. | Green Mapper: An AI-Driven Initiative for Aerial Tree Mapping, Maintaining Environmental Balance | Article | Use cases, Solutions | [[90](https://arxiv.org/html/2510.15509v1#bib.bibx90)] |
| Dube et al. | Factors Influencing the Adoption of AI Chatbots By Non-Governmental Organizations | Conference Paper | Use cases, Challenges, Solutions | [[32](https://arxiv.org/html/2510.15509v1#bib.bibx32)] |
| Faruq et al. | AI-Driven Strategies for Enhancing Non-Profit Organizational Impact | Article | Use cases, Challenges, Solutions | [[34](https://arxiv.org/html/2510.15509v1#bib.bibx34)] |
| Kapuge & Ginige | Optimizing AI Recommendation Algorithms for Efficient Matching of Most Needed Beneficiaries with Donors in Sri Lankan Charity Sector | Conference paper | Use cases | [[49](https://arxiv.org/html/2510.15509v1#bib.bibx49)] |
| Sammer et al. | AI-FEED: Prototyping an AI-Powered Platform for the Food Charity Ecosystem | Article | Use cases, Solutions | [[72](https://arxiv.org/html/2510.15509v1#bib.bibx72)] |
| Sievert & Inderhees | AI, Diversity and Trust in Digital Non-Profit Communication: Results of a Survey within the Major Traditional Churches of a Western European Country | Conference paper | Use cases | [[70](https://arxiv.org/html/2510.15509v1#bib.bibx70)] |
| Dutta & Kannan Poyil | The machine/human argentic impact on practices in learning and development: a study across MSME, NGO and MNC organizations | Article | Use cases, Challenges | [[63](https://arxiv.org/html/2510.15509v1#bib.bibx63)] |
| Elamin | Modernizing the Charitable Sector through Artificial Intelligence: Enhancing Efficiency and Impact | Article | Use cases, Challenges, Solutions | [[36](https://arxiv.org/html/2510.15509v1#bib.bibx36)] |
| Yang et al. | Understanding the impact of artificial intelligence on the justice of charitable giving: The moderating role of trust and regulatory orientation | Article | Challenges | [[87](https://arxiv.org/html/2510.15509v1#bib.bibx87)] |
| Popescu et al. | The impact of artificial intelligence on intellectual capital development: Shifting requirements for professions and processes in the non-profit sector | Article | Use cases, Challenges, Solutions | [[68](https://arxiv.org/html/2510.15509v1#bib.bibx68)] |




Table 8: Included studys from 2024 (Part 2)

| Authors | Title | Type | Discussed Topics | Citation |
| --- | --- | --- | --- | --- |
| Gupta et al. | AI Based Cyberbullying Detection and Prevention | Conference paper | Use cases, Challenges | [[55](https://arxiv.org/html/2510.15509v1#bib.bibx55)] |
| Sanjana et al. | Integrating Transparent Crowdfunding Platform and AI-Based Treatment Fund Estimation | Conference paper | Use cases | [[59](https://arxiv.org/html/2510.15509v1#bib.bibx59)] |
| Weber | AI in Emergency Response: Not the time for experiments | NGO paper | Use cases, Challenges, Solutions | [[41](https://arxiv.org/html/2510.15509v1#bib.bibx41)] |
| Nethope (org.) | Empowering Humanitarian Response Through Crisis Informatics | NGO paper | Challenges, Solutions | [[85](https://arxiv.org/html/2510.15509v1#bib.bibx85)] |
| Uke et al. | FoodSavior: Distributing Surplus Food to NGOs or Manure Producers Using Internet of Things and Machine Learning | Conference paper | Use cases | [[52](https://arxiv.org/html/2510.15509v1#bib.bibx52)] |




Table 9: Included studys from 2025 (Part 1)

| Authors | Title | Type | Discussed Topics | Citation |
| --- | --- | --- | --- | --- |
| Brezovar | The Role of Artificial Intelligence in NGOs: Challenges and Opportunities for Slovenia’s Information Society | Article | Use Cases, Challenges, Solutions | [[30](https://arxiv.org/html/2510.15509v1#bib.bibx30)] |
| Victoire | A Machine Learning Approach to Categorizing Countries by Socio-economic and Health Development Factors Using PCA, K-Means, and Silhouette Scoring | Article | Use Cases, Challenges | [[53](https://arxiv.org/html/2510.15509v1#bib.bibx53)] |
| Atalay et al. | Artificial Intelligence Technologies as Smart Solutions for Sustainable Protected Areas Management | Article | Use cases, Challenges, Solutions | [[27](https://arxiv.org/html/2510.15509v1#bib.bibx27)] |
| Ahatsi & Olanrewaju | Enhancing Humanitarian Supply Chain Resilience: Evaluating Artificial Intelligence and Big Data Analytics in Two Nations | Article | Use Cases, Challenges, Solutions | [[28](https://arxiv.org/html/2510.15509v1#bib.bibx28)] |
| Ulfy et al. | Integration of Artificial Intelligence in Biodegradable Plastic Packaging Design: Exploring Stakeholder Attitudes | Article | Use cases, Challenges, Solutions | [[48](https://arxiv.org/html/2510.15509v1#bib.bibx48)] |
| Kravchuk | Ethical Implications of AI Applications in Nonprofit and Charity Sectors | Article | Use Cases, Solutions, Challenges | [[81](https://arxiv.org/html/2510.15509v1#bib.bibx81)] |
| Kazemeini et al. | A Dataset-Driven Study of AI Opportunities in the Climate NGO Ecosystem | Conference paper | Use cases, Challenges | [[31](https://arxiv.org/html/2510.15509v1#bib.bibx31)] |
| Krause | AI Agents and Automation in Small Non-Profit Organizations’ Accounting Functions | Article | Use cases, Challenges, Solutions | [[57](https://arxiv.org/html/2510.15509v1#bib.bibx57)] |
| Kannan et al. | AI-Driven Digital Volunteering @ Freelancing Website for NGO Collaboration with Online Talent Worldwide | Article | Use cases | [[64](https://arxiv.org/html/2510.15509v1#bib.bibx64)] |
| Hansen | Exclusion or Efficiency: Understanding Perspectives about AI Ethics Among Charity Workers in the United Kingdom | Conference paper | Use cases, Challenges | [[69](https://arxiv.org/html/2510.15509v1#bib.bibx69)] |




Table 10: Included studys from 2025 (Part 2)

| Authors | Title | Type | Discussed Topics | Citation |
| --- | --- | --- | --- | --- |
| Cheng & Wang | Leveraging Artificial Intelligence–Powered Chatbots for Nonprofit Organizations: Examining the Antecedents and Outcomes of Chatbot Trust and Social Media Engagement | Article | Use cases, Challenges, Solutions | [[42](https://arxiv.org/html/2510.15509v1#bib.bibx42)] |
| Hahn et al. | From Data to Donors: Can AI Reshape Fundraising Strategies | Conference paper | Use cases, Challenges | [[33](https://arxiv.org/html/2510.15509v1#bib.bibx33)] |
| Joshi et al. | SmartNGO: An Integrated Platform for Managing Volunteers and Events | Article | Use cases | [[67](https://arxiv.org/html/2510.15509v1#bib.bibx67)] |
| Scuotto et al. | Tackling the empowerment of Artificial Intelligence for humanitarian intervention from Save the Children | Article | Use cases, Challenges | [[29](https://arxiv.org/html/2510.15509v1#bib.bibx29)] |
| Ahatsi et al. | Resilience in Humanitarian Supply Chains: Addressing Artificial Intelligence and Big Data Hurdles Across Borders | Article | Use cases, Challenges, Solutions | [[78](https://arxiv.org/html/2510.15509v1#bib.bibx78)] |
| Iazzolino | Trading Efficiency for Control: the AI Conundrum in Migration Management | Article | Use cases, Challenges, Solutions | [[86](https://arxiv.org/html/2510.15509v1#bib.bibx86)] |
| Bhuvaneswari et al. | UniteVol: AI-Powered Social Impact and Leadership Platform | Conference paper | Use cases | [[65](https://arxiv.org/html/2510.15509v1#bib.bibx65)] |
| Sandberg et al. | Addressing the promise and peril of AI for nonprofit management through a data feminist pedagogy | Article | Use cases, Challenges, Solutions | [[71](https://arxiv.org/html/2510.15509v1#bib.bibx71)] |