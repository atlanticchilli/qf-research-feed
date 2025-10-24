---
authors:
- Wenjun Cao
doc_id: arxiv:2510.20612v1
family_id: arxiv:2510.20612
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Black Box Absorption: LLMs Undermining Innovative Ideas'
url_abs: http://arxiv.org/abs/2510.20612v1
url_html: https://arxiv.org/html/2510.20612v1
venue: arXiv q-fin
version: 1
year: 2025
---


Wenjun Cao
  
Independent Researcher
  
wenjun.cao.research@gmail.com

###### Abstract

Large Language Models are increasingly adopted as critical tools for accelerating innovation. This paper identifies and formalizes a systemic risk inherent in this paradigm: Black Box Absorption. We define this as the process by which the opaque internal architectures of LLM platforms, often operated by large-scale service providers, can internalize, generalize, and repurpose novel concepts contributed by users during interaction. This mechanism threatens to undermine the foundational principles of innovation economics by creating severe informational and structural asymmetries between individual creators and platform operators, thereby jeopardizing the long-term sustainability of the innovation ecosystem. To analyze this challenge, we introduce two core concepts: the idea unit, representing the transportable functional logic of an innovation, and idea safety, a multidimensional standard for its protection. This paper analyzes the mechanisms of absorption and proposes a concrete governance and engineering agenda to mitigate these risks, ensuring that creator contributions remain traceable, controllable, and equitable.

## 1 Introduction

Large Language Models are rapidly becoming integral to modern productivity and creation. They have demonstrated substantial efficiency gains across diverse domains, including office automation, professional writing, and software development (Brynjolfsson et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib16); Noy & Zhang, [2023](https://arxiv.org/html/2510.20612v1#bib.bib73); Dell’Acqua et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib26); Chatterji et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib22)). Extending beyond simple automation, they are increasingly used as collaborative partners in innovative tasks, from creative work and art generation to scientific research and discovery (Anantrasirichai & Bull, [2021](https://arxiv.org/html/2510.20612v1#bib.bib1); Novikov et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib72); Si et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib95); Hubert et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib43); Horton, [2023](https://arxiv.org/html/2510.20612v1#bib.bib39); Anthis et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib4)). Individuals and organizations provide original ideas during interactive generation to refine concepts and accelerate the innovation lifecycle.

However, the new paradigm rests on an assumption that is often overlooked: the originality and privacy of ideas shared during these interactions are robustly protected.(King et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib49); Lukas et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib62); Mireshghallah et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib66); Mireshghallah & Li, [2025](https://arxiv.org/html/2510.20612v1#bib.bib65); Ngong et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib71); Tran et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib102); Ma et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib63); Green et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib34); Yi et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib108); Zhang & Yang, [2025](https://arxiv.org/html/2510.20612v1#bib.bib111); Shao et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib91); LLC, [2024](https://arxiv.org/html/2510.20612v1#bib.bib59); Tamkin et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib98); Huang et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib41)) We argue that the foundational principles of innovation, namely the ability to secure and control novel concepts, are being undermined by the structure of the current ecosystem.(Bommasani et al., [2022](https://arxiv.org/html/2510.20612v1#bib.bib13); Bender et al., [2021](https://arxiv.org/html/2510.20612v1#bib.bib10); Solaiman, [2023](https://arxiv.org/html/2510.20612v1#bib.bib96); Sastry et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib88); Bommasani et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib12); White et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib107); Casper et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib21); Kapoor et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib46); Anderljung et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib2))

The threat originates from the complex and opaque nature of LLM platforms. Protection of original ideas is not absolute. User inputs can be routed through internal systems for detection, annotation, utilization, and retraining (Han et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib35); Liu et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib58); PBC, [2025](https://arxiv.org/html/2510.20612v1#bib.bib83); LLC, [2025](https://arxiv.org/html/2510.20612v1#bib.bib60)). Terms of Service and Privacy Policies frequently grant broad licenses to the provider (Oakley, [2005](https://arxiv.org/html/2510.20612v1#bib.bib74)). Combined with the complexity of deep learning models, the overall platform behaves as a black box from the perspective of the user (Burrell, [2016](https://arxiv.org/html/2510.20612v1#bib.bib17); Pasquale, [2015](https://arxiv.org/html/2510.20612v1#bib.bib81)). The user lacks verifiable insight into how ideas are processed, stored, or repurposed. The opacity is particularly consequential because the assets at risk, namely functional ideas and processes, often fall into a legal gap outside traditional copyright, which protects expression and not function (Pasquale & Sun, [2024](https://arxiv.org/html/2510.20612v1#bib.bib82); Kyi et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib52)). We refer to the combination of technical opacity and potential legal ambiguity as Black Box Absorption.

It is important to distinguish this topic from adjacent work on LLM privacy. Most research concentrates on training data leakage and privacy-preserving inference.(PBC & Labs, [2025](https://arxiv.org/html/2510.20612v1#bib.bib84); LLC, [2025](https://arxiv.org/html/2510.20612v1#bib.bib60)) Training data leakage, including memorization and regurgitation of sensitive information(Lukas et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib62); Shokri et al., [2017](https://arxiv.org/html/2510.20612v1#bib.bib94); Yu et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib109); Shi et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib93); Carlini et al., [2023a](https://arxiv.org/html/2510.20612v1#bib.bib19); [2021](https://arxiv.org/html/2510.20612v1#bib.bib18); Kandpal et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib45); Kim et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib47)), does not directly address the live internal pipelines of deployed systems. The sources of training data are varied and often unrelated to interactive idea generation. Our analysis, therefore, focuses on the systemic risk of idea leakage within the deployment pipeline itself, where internal detection, annotation, and retraining workflows can operate as a continuous absorption mechanism.

The societal impact is clear in the economics of innovation (Lee & Mendelson, [2007](https://arxiv.org/html/2510.20612v1#bib.bib53); Partha & David, [1994](https://arxiv.org/html/2510.20612v1#bib.bib80); Heller & Eisenberg, [1998](https://arxiv.org/html/2510.20612v1#bib.bib37); Resnick & Zeckhauser, [2002](https://arxiv.org/html/2510.20612v1#bib.bib86); Scotchmer, [1991](https://arxiv.org/html/2510.20612v1#bib.bib89); Teece, [1986](https://arxiv.org/html/2510.20612v1#bib.bib100); Arrow, [1972](https://arxiv.org/html/2510.20612v1#bib.bib6); Gans & Stern, [2010](https://arxiv.org/html/2510.20612v1#bib.bib29)). Black Box Absorption creates a setting in which the platform becomes the central locus of value capture by drawing on unprotected ideas from many users. To analyze and safeguard this process, we introduce the idea unit as the specific asset at risk and propose idea safety as a multidimensional standard to protect such assets once they are articulated. Idea safety rests on three verifiable principles: traceability, control, and equitability.

Building on this perspective, the paper makes three contributions. It identifies and formalizes the systemic risk of Black Box Absorption that arises when deployment pipelines internalize valuable creator contributions. It develops the idea unit as a unit of analysis defined by a functional effect that specifies what is exposed during interaction and how it can diffuse. It advances idea safety as a deployable standard grounded in traceability, control, and equitability. This standard is used to trace the lifecycle of idea units on current platforms, analyze the economic consequences, and articulate a governance agenda that supports sustained innovation.

## 2 Economic and Conceptual Foundations

### 2.1 Economics of Innovation Knowledge

Large Language Models increasingly act as engines of innovation(Brynjolfsson et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib16)). They can lower search costs, accelerate recombination of prior knowledge, and shorten the path from concept to workable draft (Bommasani et al., [2022](https://arxiv.org/html/2510.20612v1#bib.bib13)).

Innovation economics also explains why acceleration can coexist with new risks Arrow ([1972](https://arxiv.org/html/2510.20612v1#bib.bib6)); Scotchmer ([1991](https://arxiv.org/html/2510.20612v1#bib.bib89)); Teece ([1986](https://arxiv.org/html/2510.20612v1#bib.bib100)). Knowledge, once articulated, differs from ordinary goods. It is nonrival in use, inexpensive to copy, and easy to transmit across organizations and markets (Scotchmer, [1991](https://arxiv.org/html/2510.20612v1#bib.bib89); Partha & David, [1994](https://arxiv.org/html/2510.20612v1#bib.bib80)). These properties enable diffusion that benefits society while reducing private value capture. To obtain support, an innovator must disclose enough detail for others to assess feasibility and impact, and the same disclosure can ease imitation or independent development (Arrow, [1972](https://arxiv.org/html/2510.20612v1#bib.bib6); Gans & Stern, [2010](https://arxiv.org/html/2510.20612v1#bib.bib29); Partha & David, [1994](https://arxiv.org/html/2510.20612v1#bib.bib80)). Legal protections mitigate some hazards but are incomplete (Heller & Eisenberg, [1998](https://arxiv.org/html/2510.20612v1#bib.bib37)). Many valuable elements of a concept, including methods, processes, problem framings, and strategic plans, are not fully covered, and legal protection often arrives slower than diffusion (Pasquale & Sun, [2024](https://arxiv.org/html/2510.20612v1#bib.bib82); Kyi et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib52)). Returns therefore depend on access to complementary assets such as data, compute, specialized labor, and distribution channels (Teece, [1986](https://arxiv.org/html/2510.20612v1#bib.bib100)). Actors that control these assets can realize value faster and on a larger scale than originators who lack them (Narechania, [2021](https://arxiv.org/html/2510.20612v1#bib.bib67); Narechania & Sitaraman, [2024](https://arxiv.org/html/2510.20612v1#bib.bib68)).

Placing this framework in the context of LLM-mediated creation helps clarify the mechanism. Interactive use requires turning implicit know-how into explicit prompts, sketches, specifications, and critiques that the system can process (King et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib49); Tran et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib102); Lucas et al., [2014](https://arxiv.org/html/2510.20612v1#bib.bib61); Croes et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib24); Zhang et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib112)). Once expressed, similar economic properties often apply: replication is cheap, downstream reuse is feasible, and the originator’s control depends on institutional and technical safeguards that are often outside their reach (Arrow, [1972](https://arxiv.org/html/2510.20612v1#bib.bib6); Scotchmer, [1991](https://arxiv.org/html/2510.20612v1#bib.bib89)). Platforms that host these interactions typically hold the complementary assets needed to transform promising content into deployable capabilities (Teece, [1986](https://arxiv.org/html/2510.20612v1#bib.bib100); Narechania, [2021](https://arxiv.org/html/2510.20612v1#bib.bib67)).

To analyze the dynamics with precision, we introduce the notion of an *idea unit*: a minimally actionable piece of innovative content that, once articulated during interaction with a model, becomes subject to the forces described above. This unit serves as the basic object for reasoning about diffusion, control, and value realization throughout the rest of the paper.

### 2.2 The Idea Unit

*An idea unit is identified by its functional effect, the transportable logic of a heuristic or reasoning pattern, rather than by its surface form as text, code, or a diagram*. It is the action-enabling structure that makes a proposal work: the organizing steps, the decision rule, the constraint that aligns choices, or the framing that unlocks a solution. Because it is defined by effect, the same unit can be rephrased many ways without altering what it enables.

Once a creator articulates reasoning to an LLM, the system receives a functional specification that can be separated from its wording and used in other contexts. The value and the vulnerability are both in that specification. It is easy to store, route, and recombine, and it travels across teams, products, and training pipelines. Control over the surface form does not guarantee control over the unit if its functional core has been captured (U.S. Congress, [1976](https://arxiv.org/html/2510.20612v1#bib.bib103); U.S. Supreme Court, [1879](https://arxiv.org/html/2510.20612v1#bib.bib104)).

Operationally, the idea unit is the object we track. It is the minimal slice of innovative content that, when exposed during interaction, can be evaluated, logged, sampled for review, curated into datasets, and generalized by models. Focusing on this unit allows clear reasoning about diffusion, control, and value realization without distraction from incidental phrasing.

### 2.3 Idea Safety

*A system is idea safe when the creator can verify what happened to each unit, can govern its lifecycle after interaction, and can receive fair recognition if a unit contributes to improvement.* We propose a directional framework that turns this goal into concrete guarantees. The framework rests on three principles that map to the practical capabilities a creator must hold: agency over how each unit is handled, verifiable observability of its path through systems, and alignment of rewards when a contribution leads to improvement. The following paragraphs define these principles at an operational level and specify the conditions a platform must meet to satisfy them.

#### Control.

Control requires that the creator retain agency over the idea unit after the interaction. Agency must be granular. A creator can decide, per unit, whether it may be retained for history, shared for safety review, used for training, or purged. Control includes the ability to correct misclassification, quarantine sensitive units, request redaction, and trigger unlearning or equivalent remedies when a unit was used against intent. Choices must be effective, visible, and reversible within clear time bounds(Ma et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib63); Yi et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib108); Mireshghallah & Li, [2025](https://arxiv.org/html/2510.20612v1#bib.bib65); Shao et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib91)).

#### Traceability.

Traceability requires that every step in the handling of an idea unit is knowable and auditable. A creator should be able to see when the unit was logged, who or what processed it, whether it entered review queues, whether any version was curated into datasets, and whether it influenced models or tools. Traceability is not a promise in policy language; it is a record that links the unit to its provenance and downstream use so that questions about exposure, reuse, and influence have concrete answers (Bae et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib8); Park et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib79); Bae et al., [2022](https://arxiv.org/html/2510.20612v1#bib.bib7)).

#### Equitability.

Equitability aligns incentives when a creator contributes an idea unit. If a unit with proper consent improves a model, a product, or an operational workflow, there should be a transparent path to recognition and value-sharing. The mechanism can take different forms, including royalties, credits, access, or other compensating benefits, but the principle is constant: contribution is not a free resource (Arrieta-Ibarra et al., [2018](https://arxiv.org/html/2510.20612v1#bib.bib5); Vipra & Korinek, [2023](https://arxiv.org/html/2510.20612v1#bib.bib105); Narechania & Sitaraman, [2024](https://arxiv.org/html/2510.20612v1#bib.bib68)). Equitability balances platform scale with creator authorship and helps ensure that the gains from diffusion do not erase the originator’s claim to value.

## 3 The Lifecycle of an Idea Unit on LLM Platforms

An idea unit, defined by novelty and value, is a distinct asset. Its vulnerability arises from the environment in which it is handled. Foundational research has established the black box as a core concept for analyzing the technical opacity of algorithms (Burrell, [2016](https://arxiv.org/html/2510.20612v1#bib.bib17)) and the socio-economic opacity of data-driven systems (Pasquale, [2015](https://arxiv.org/html/2510.20612v1#bib.bib81); Brevini & Pasquale, [2020](https://arxiv.org/html/2510.20612v1#bib.bib14)). Building on this, we introduce Black Box Absorption to define the process that occurs within this environment: the systemic internalization of idea units by platform providers. This absorption is not a single event but a multistage process enabled by standard internal operations. We trace the chronological lifecycle of an idea unit from the moment it is submitted. This pathway is synthesized from the operational details provided in public model reports and system cards, which document the key stages of data handling(BigScience Workshop, [2023](https://arxiv.org/html/2510.20612v1#bib.bib11); Touvron et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib101); OpenAI, [2024](https://arxiv.org/html/2510.20612v1#bib.bib75); Anil et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib3); Gemini Team, [2025b](https://arxiv.org/html/2510.20612v1#bib.bib32); PBC, [2025](https://arxiv.org/html/2510.20612v1#bib.bib83); Comanici et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib23); Gemini Team, [2025a](https://arxiv.org/html/2510.20612v1#bib.bib31); Paleyes et al., [2022](https://arxiv.org/html/2510.20612v1#bib.bib78); Pahune & Akhtar, [2025](https://arxiv.org/html/2510.20612v1#bib.bib77)).

### 3.1 Data Governance and User Licensing

The process begins before any idea unit is typed. The legal gateway is established by the Terms of Service and the Privacy Policy. Users commonly grant the platform a worldwide, nonexclusive, royalty-free license to use, copy, modify, and create derivative works of their content for operating, providing, and improving services. While essential for legitimate functions such as caching, a broad improvement clause can create opacity. It legally empowers the use of user-generated content, including valuable idea units, for many internal purposes. Users often have limited visibility into how this license is interpreted or operationalized, which may create information asymmetry (Oakley, [2005](https://arxiv.org/html/2510.20612v1#bib.bib74); Tang et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib99); Zhang et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib112); Pasquale & Sun, [2024](https://arxiv.org/html/2510.20612v1#bib.bib82); Lukas et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib62); Mireshghallah & Li, [2025](https://arxiv.org/html/2510.20612v1#bib.bib65)).

### 3.2 Data Ingestion and Interaction Logging

After acceptance of terms, submission of an idea unit triggers the technical lifecycle. Ingestion has two phases: real-time processing and durable storage.

#### Real-time Interaction Processing.

In many deployments, the system processes the interaction in real-time(Paleyes et al., [2022](https://arxiv.org/html/2510.20612v1#bib.bib78); Pahune & Akhtar, [2025](https://arxiv.org/html/2510.20612v1#bib.bib77)). Before reaching the generative model, the prompt that contains the idea unit may be scanned by a lightweight classification model acting as a prefilter for policy violations(Sheth et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib92); Markov et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib64); Hoover et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib38); PBC, [2025](https://arxiv.org/html/2510.20612v1#bib.bib83); LLC, [2025](https://arxiv.org/html/2510.20612v1#bib.bib60)). The generated response may then be scanned by a second classifier that checks the output for harmful content(Sheth et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib92); Markov et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib64); Hoover et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib38); Vishwamitra et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib106); PBC, [2025](https://arxiv.org/html/2510.20612v1#bib.bib83); LLC, [2025](https://arxiv.org/html/2510.20612v1#bib.bib60); Nghiem & Daumé Iii, [2024](https://arxiv.org/html/2510.20612v1#bib.bib70); Franco et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib28); Roy et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib87); Kumar et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib51); Huang, [2025](https://arxiv.org/html/2510.20612v1#bib.bib42); Gao et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib30)).

#### Persistent Interaction Logging.

After these multistep checks, the complete interaction tuple consisting of the user prompt that contains the idea unit, the model response, and any internal safety flags may be written to operational logs(Paleyes et al., [2022](https://arxiv.org/html/2510.20612v1#bib.bib78); Pahune & Akhtar, [2025](https://arxiv.org/html/2510.20612v1#bib.bib77)) (King et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib49); Tran et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib102); Mireshghallah et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib66); Lukas et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib62); Tamkin et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib98); Huang et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib41)). The processing often occurs within milliseconds(Paleyes et al., [2022](https://arxiv.org/html/2510.20612v1#bib.bib78); Pahune & Akhtar, [2025](https://arxiv.org/html/2510.20612v1#bib.bib77)). For the user, the interaction appears complete. For the platform, the lifecycle of the logged unit can continue (Tamkin et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib98)).

### 3.3 Data Sampling, Review, and Annotation

Operational logs may be treated as an active dataset. Automated triage and sampling can select specific interactions for human review, routing them to queues based on business needs.

#### Automated Triage and Sampling.

Automated processes may filter and sample raw logs, distributing interactions to specialized human-in-the-loop workstreams (Paleyes et al., [2022](https://arxiv.org/html/2510.20612v1#bib.bib78); Pahune & Akhtar, [2025](https://arxiv.org/html/2510.20612v1#bib.bib77)). Selected data can be sent to annotators for reinforcement learning from human feedback. Annotators rate, rewrite, or rank model responses. Reviewers may be exposed to the raw content of the idea unit. High value and novel units could be attractive candidates for review because they represent complex prompts that are useful for training more capable models(Liu et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib57); Lee et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib54); Huang et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib40); Dong et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib27); Han et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib35); Liu et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib58); Huang et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib41))

#### Safety and Audit Review.

Interactions flagged by automated classifiers can be prioritized and routed to internal teams or safety contractors. Reviewers audit classifier decisions, handle edge cases, and provide corrections. These judgments may be used to retrain and improve automated safety filters(Casper et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib21); Raji et al., [2020](https://arxiv.org/html/2510.20612v1#bib.bib85); LLC, [2025](https://arxiv.org/html/2510.20612v1#bib.bib60)).

#### Quality Assurance and Annotation.

A separate sampling pathway can target interactions based on other criteria, including negative user feedback or heuristics for high quality and novelty. These samples may be sent to annotators who provide labels useful for future training(Paleyes et al., [2022](https://arxiv.org/html/2510.20612v1#bib.bib78); Sculley et al., [2015](https://arxiv.org/html/2510.20612v1#bib.bib90); Gilardi et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib33)) (King et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib49); Tran et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib102)).

### 3.4 Data Curation and Model Retraining

This stage systematizes potential absorption. Valuable data identified earlier is prepared and consumed to update models.

#### Dataset Curation and Compiling.

Human-labeled data is aggregated and combined with data selected by automated quality filters. The set is cleaned and deduplicated to create a curated dataset for a future training cycle (Sculley et al., [2015](https://arxiv.org/html/2510.20612v1#bib.bib90); Kim et al., [2018](https://arxiv.org/html/2510.20612v1#bib.bib48); Lin & Ryaboy, [2013](https://arxiv.org/html/2510.20612v1#bib.bib56); Paleyes et al., [2022](https://arxiv.org/html/2510.20612v1#bib.bib78); Pahune & Akhtar, [2025](https://arxiv.org/html/2510.20612v1#bib.bib77)).

#### Model Retraining and Generalization.

The curated dataset may be used for fine-tuning or for building a new pre-training corpus. During retraining, parameters are updated, allowing patterns, concepts, and knowledge within the idea unit to be encoded and generalized. The novel concept within the unit could become non-exclusive if generalized into parameters. The generalized content may then influence responses to other users, including others in similar domains(OpenAI, [2024](https://arxiv.org/html/2510.20612v1#bib.bib75); Touvron et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib101); Gemini Team, [2025b](https://arxiv.org/html/2510.20612v1#bib.bib32); Anil et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib3); Carlini et al., [2021](https://arxiv.org/html/2510.20612v1#bib.bib18); Kandpal et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib45); Carlini et al., [2023a](https://arxiv.org/html/2510.20612v1#bib.bib19); Shokri et al., [2017](https://arxiv.org/html/2510.20612v1#bib.bib94); Kim et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib47); Mireshghallah & Li, [2025](https://arxiv.org/html/2510.20612v1#bib.bib65); Lukas et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib62); Pasquale & Sun, [2024](https://arxiv.org/html/2510.20612v1#bib.bib82); Comanici et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib23); Gemini Team, [2025a](https://arxiv.org/html/2510.20612v1#bib.bib31))
Across this multistage pipeline, from legal consent to automated generalization, transparency can be limited in practice. Creators may lack practical means to verify whether an idea unit was selected, how it was used, or whether removal was effective, and opt-out mechanisms may be limited or absent in some cases (Oakley, [2005](https://arxiv.org/html/2510.20612v1#bib.bib74); Tang et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib99); Burrell, [2016](https://arxiv.org/html/2510.20612v1#bib.bib17); Brevini & Pasquale, [2020](https://arxiv.org/html/2510.20612v1#bib.bib14)).

## 4 Consequences of Black Box Absorption

The absorption pathway, combined with the economics of innovation and the definition of the idea unit, can create systemic risks that shape behavior across the ecosystem. Rapid diffusion, incomplete protection, and concentrated implementation capacity may pressure creators into choices that reduce their ability to capture value.

### 4.1 Adoption Pressure in Competitive Settings

In competitive environments where peers use LLMs to accelerate work, declining to use such tools may become unattractive. Creators recognize that using interactive tools can raise throughput and quality, while abstaining can lead to slower iteration, weaker outputs, and loss of opportunities. At the same time, using these tools requires articulating functional content that can be stored, routed, and learned from. Short-run costs of abstention can be salient, while the risk of absorption is opaque, probabilistic, and delayed. Given this asymmetry, actors may adopt tooling even when idea units could be incorporated into platform pipelines without verification or control. Adoption may be individually rational yet may collectively expose originators to systematic value loss (Lee & Mendelson, [2007](https://arxiv.org/html/2510.20612v1#bib.bib53); Partha & David, [1994](https://arxiv.org/html/2510.20612v1#bib.bib80); Teece, [1986](https://arxiv.org/html/2510.20612v1#bib.bib100)).

### 4.2 Untraceable and Asymmetrical Control

The central hazard is *untraceability*. Once a functional pattern is generalized into a model, no straightforward audit trail ties a later capability to a specific contributing interaction. A creator may observe outputs, features, or practices that resemble prior submissions, yet the route from contribution to effect can remain hidden, which weakens any basis for recourse or negotiation(Bae et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib8); Park et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib79); Bae et al., [2022](https://arxiv.org/html/2510.20612v1#bib.bib7); Burrell, [2016](https://arxiv.org/html/2510.20612v1#bib.bib17)). Two forms of asymmetry follow. First, informational asymmetry: platforms can observe selection, review, curation, and training decisions end-to-end, while creators lack visibility into how their idea units are used. Second, structural asymmetry: platforms command complementary assets such as compute, data, engineering capacity, and distribution, which convert content into outcomes at speed and scale that originators typically cannot match(Narechania & Sitaraman, [2024](https://arxiv.org/html/2510.20612v1#bib.bib68); Narechania, [2021](https://arxiv.org/html/2510.20612v1#bib.bib67); Vipra & Korinek, [2023](https://arxiv.org/html/2510.20612v1#bib.bib105); Kleinberg & Raghavan, [2021](https://arxiv.org/html/2510.20612v1#bib.bib50)).

### 4.3 Asymmetrical Value Realization

These asymmetries can channel returns away from originators and toward asset holders (Kalluri, [2020](https://arxiv.org/html/2510.20612v1#bib.bib44)). When the functional core of an idea is easy to diffuse and difficult to exclude, value capture depends less on authorship and more on control of implementation bottlenecks(Teece, [1986](https://arxiv.org/html/2510.20612v1#bib.bib100)). Potential absorption could intensify this pattern. Idea units supplied during interaction may be filtered, refined, and embedded into systems that only the platform can deploy widely. Features and capabilities can then appear to originate within the platform boundary. At the same time, the creators who supplied the enabling logic cannot readily demonstrate influence or claim a share of realized value. Over time, value could concentrate in institutions with the means of execution. The long-run cost is not only distributive; incentives to articulate high-value idea units may weaken, which harms dynamic efficiency (Scotchmer, [1991](https://arxiv.org/html/2510.20612v1#bib.bib89)).

## 5 An Idea Safety Agenda

The risks of asymmetry and untraceable absorption necessitate a new governance framework. We outline the deployable Idea Safety agenda, which provides the strategic direction to address these challenges. It translates our economic lens and the definition of the idea unit into foundational guidance for both engineering and policy. The goal is to replace ad hoc promises with verifiable guarantees, establishing a system that aligns with how idea units are created, managed, and converted into capabilities on contemporary platforms.

### 5.1 The Control Principle

Control begins with the premise that agency does not end at submission. An articulated idea unit should remain subject to the originator’s choices over retention, review exposure, training use, and purging. In practice, this requires an interaction mode with non-retention available as a default, clear disclosures about what is recorded and for how long, and a dashboard available after interaction where decisions can be made at the level of individual units (LLC, [2024](https://arxiv.org/html/2510.20612v1#bib.bib59)). Where a unit was misrouted or mislabeled, the creator must be able to correct that status. Where a unit was used against intent, there must be an effective remedy, such as redaction from logs and unlearning of downstream use. These controls must be auditable and enforced within stated windows so that the agency is operational rather than symbolic (Ma et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib63); Yi et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib108); Mireshghallah & Li, [2025](https://arxiv.org/html/2510.20612v1#bib.bib65); Shao et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib91); LLC, [2025](https://arxiv.org/html/2510.20612v1#bib.bib60)).

### 5.2 The Traceability Principle

Traceability is an engineering commitment. Every idea unit that is selected for review or training carries its provenance forward, and the system can report what happened to it. An attribution first pipeline binds each copy, transformation, and decision to a consented source so that the path from submission to influence is reconstructable. On this substrate, the platform should answer two classes of questions without guesswork: where a unit went, including logging, sampling, curation, and evaluation, and how it mattered, including whether and where it contributed to model behavior or tool configurations. When removal is warranted, the exact provenance supports targeted unlearning and verification that subsequent artifacts no longer rely on the unit. Attribution, influence accounting, and unlearning are facets of a single system that makes the handling of idea units inspectable and, when necessary, reversible (Bae et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib8); Park et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib79); Bae et al., [2022](https://arxiv.org/html/2510.20612v1#bib.bib7); LLC, [2025](https://arxiv.org/html/2510.20612v1#bib.bib60)).

### 5.3 The Equitability Principle

Equitability addresses who benefits when idea units improve systems. Contractual guarantees today are often stronger for organizational accounts, while personal accounts are frequently treated as sources of training material by default. The remedy is a baseline that applies to everyone. The use of an idea unit for improvement must require explicit consent, accompanied by a clear account of permitted reuse and attribution. When a consented unit improves a model, product, or workflow, the platform should convert that contribution into tangible value such as credits, access, royalties, or other fair consideration, according to published terms that are auditable and applied symmetrically. Records that exist for traceability also serve as the ledger for contribution, ensuring that recognition and value-sharing reflect actual use (Arrieta-Ibarra et al., [2018](https://arxiv.org/html/2510.20612v1#bib.bib5); Vipra & Korinek, [2023](https://arxiv.org/html/2510.20612v1#bib.bib105); Narechania & Sitaraman, [2024](https://arxiv.org/html/2510.20612v1#bib.bib68)).

## 6 Discussion and Related Work

#### LLM Deployment.

Public system cards and engineering accounts outline a recurring deployment pattern in which user prompts are screened by lightweight classifiers, routed to large models, and logged together with safety metadata for later review and improvement(Paleyes et al., [2022](https://arxiv.org/html/2510.20612v1#bib.bib78); Pahune & Akhtar, [2025](https://arxiv.org/html/2510.20612v1#bib.bib77); OpenAI, [2024](https://arxiv.org/html/2510.20612v1#bib.bib75); Touvron et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib101); Gemini Team, [2025b](https://arxiv.org/html/2510.20612v1#bib.bib32); Anil et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib3); PBC, [2025](https://arxiv.org/html/2510.20612v1#bib.bib83); Comanici et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib23); Gemini Team, [2025a](https://arxiv.org/html/2510.20612v1#bib.bib31); LLC, [2025](https://arxiv.org/html/2510.20612v1#bib.bib60); Tamkin et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib98); Huang et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib41); Nghiem & Daumé Iii, [2024](https://arxiv.org/html/2510.20612v1#bib.bib70); Franco et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib28); Roy et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib87); Kumar et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib51); Huang, [2025](https://arxiv.org/html/2510.20612v1#bib.bib42); Gao et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib30)). Legal gateways such as Terms of Service and Privacy Policies typically authorize broad reuse of user content for service improvement, which establishes the contractual surface through which interactions can enter internal pipelines(Oakley, [2005](https://arxiv.org/html/2510.20612v1#bib.bib74); Tang et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib99); Zhang et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib112); LLC, [2024](https://arxiv.org/html/2510.20612v1#bib.bib59)). This literature clarifies infrastructure and licensing, but it does not model the functional granularity of what is at stake for creators. Our account centers the *idea unit* as the object that travels through these pipelines and provides a framework for what must be auditable and controllable once it has been articulated.

#### LLM Privacy.

Research on privacy has disproportionately targeted training data leakage and inference-time confidentiality; recent large-scale analyses of the field confirm that the vast majority of work overlooks threats from post-interaction data handling, platform governance, and retraining pipelines (Mireshghallah & Li, [2025](https://arxiv.org/html/2510.20612v1#bib.bib65); Brown et al., [2022](https://arxiv.org/html/2510.20612v1#bib.bib15)). This dominant focus is evident in a growing body of work that quantifies memorization, membership inference, and secret extraction risks in parametric models and fine-tuning regimes (Carlini et al., [2021](https://arxiv.org/html/2510.20612v1#bib.bib18); [2023a](https://arxiv.org/html/2510.20612v1#bib.bib19); Shokri et al., [2017](https://arxiv.org/html/2510.20612v1#bib.bib94); Kandpal et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib45); Lukas et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib62); Carlini et al., [2023b](https://arxiv.org/html/2510.20612v1#bib.bib20)). Another strand explores encrypted or privacy-preserving inference that hardens the runtime pathway at the cost of substantial latency and compute overheads (Li et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib55); Staab et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib97); de Castro et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib25); Zhang et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib110); Hao et al., [2022](https://arxiv.org/html/2510.20612v1#bib.bib36); PBC & Labs, [2025](https://arxiv.org/html/2510.20612v1#bib.bib84); LLC, [2025](https://arxiv.org/html/2510.20612v1#bib.bib60)). These advances secure data and interactions, yet they leave unresolved the critical gap of what happens when valuable reasoning is legitimately observed, labeled, curated, and then generalized within platform retraining. Our work complements privacy guarantees by specifying post-interaction rights over the functional content of ideas rather than only their textual surface.

#### RLHF.

Studies of human feedback pipelines describe how platforms select interactions, collect ratings, derive preference data, and use it for alignment and capability gains(Ouyang et al., [2022](https://arxiv.org/html/2510.20612v1#bib.bib76); Bai et al., [2022](https://arxiv.org/html/2510.20612v1#bib.bib9); Liu et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib57); Lee et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib54); Huang et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib40); Dong et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib27); Han et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib35); Liu et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib58); Tamkin et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib98); Huang et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib41)). Operations research highlights curation, quality control, and dataset construction as critical determinants of downstream behavior (Sculley et al., [2015](https://arxiv.org/html/2510.20612v1#bib.bib90); Kim et al., [2018](https://arxiv.org/html/2510.20612v1#bib.bib48); Lin & Ryaboy, [2013](https://arxiv.org/html/2510.20612v1#bib.bib56); Gilardi et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib33); Nazabal et al., [2020](https://arxiv.org/html/2510.20612v1#bib.bib69)). This literature explains how content is transformed into a training signal but remains agnostic about the creator’s claims once their reasoning has been integrated. We make those claims explicit by requiring traceability at the unit level and remedies such as targeted unlearning when use conflicts with consent.

#### Innovation Economics.

Economic analyses of knowledge production emphasize nonrivalry, diffusion, disclosure incentives, and the centrality of complementary assets in value capture (Arrow, [1972](https://arxiv.org/html/2510.20612v1#bib.bib6); Scotchmer, [1991](https://arxiv.org/html/2510.20612v1#bib.bib89); Partha & David, [1994](https://arxiv.org/html/2510.20612v1#bib.bib80); Teece, [1986](https://arxiv.org/html/2510.20612v1#bib.bib100); Gans & Stern, [2010](https://arxiv.org/html/2510.20612v1#bib.bib29)). Work on digital platforms and competition shows how control of infrastructure, data, and distribution shapes appropriation (Narechania, [2021](https://arxiv.org/html/2510.20612v1#bib.bib67); Narechania & Sitaraman, [2024](https://arxiv.org/html/2510.20612v1#bib.bib68)). We import this lens into LLM-mediated creation and make the exposure unit explicit: once a functional heuristic is articulated to a model, it becomes a transportable asset whose returns depend on provenance, consent, and the holder of complementary capabilities. The proposed notion of *idea safety* translates classic appropriability concerns into deployable engineering and governance requirements.

#### Social Impact of LLMs.

Surveys and systematizations document the expanding scope of LLM use, reported productivity gains, and emerging societal effects across research, industry, and culture (Bommasani et al., [2022](https://arxiv.org/html/2510.20612v1#bib.bib13); Brynjolfsson et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib16); Bommasani et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib12); Sastry et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib88); Tamkin et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib98); Huang et al., [2025](https://arxiv.org/html/2510.20612v1#bib.bib41)). Critical analyses warn that aggregate performance metrics can obscure distributional consequences and that capability scaling can reshape creative practice (Bender et al., [2021](https://arxiv.org/html/2510.20612v1#bib.bib10); Solaiman, [2023](https://arxiv.org/html/2510.20612v1#bib.bib96); White et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib107); Kapoor et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib46); Anderljung et al., [2023](https://arxiv.org/html/2510.20612v1#bib.bib2)). Our contribution engages these debates by identifying a concrete failure mode called Black Box Absorption, where the gains from diffusion may accrue within platform boundaries without verifiable pathways for recognition or control for the originators of functional ideas.

#### AI Risks.

Foundational critiques of the algorithmic black box argue that complex, opaque, and inscrutable learning systems create structural information asymmetries that frustrate accountability(Burrell, [2016](https://arxiv.org/html/2510.20612v1#bib.bib17); Pasquale, [2015](https://arxiv.org/html/2510.20612v1#bib.bib81); Brevini & Pasquale, [2020](https://arxiv.org/html/2510.20612v1#bib.bib14); Casper et al., [2024](https://arxiv.org/html/2510.20612v1#bib.bib21)). Policy-oriented work examines monopolization risk, concentration of critical inputs, and market power that can convert aggregate improvement into centralized value capture (Narechania & Sitaraman, [2024](https://arxiv.org/html/2510.20612v1#bib.bib68); Vipra & Korinek, [2023](https://arxiv.org/html/2510.20612v1#bib.bib105); Kleinberg & Raghavan, [2021](https://arxiv.org/html/2510.20612v1#bib.bib50)). Our framework operationalizes these concerns at the unit of contribution: by making provenance, influence, and remedial action primary system properties, it becomes possible to mitigate opacity without halting capability progress, and to counter homogenization by aligning improvement with auditable sources.

The present paper makes three contributions. It shifts the unit of analysis from datasets or conversations to idea units defined by functional effect, which explains why value can be at risk even when surface text is protected. It treats absorption as a deployment lifecycle phenomenon that spans legal gateways, logging, sampling, curation, and retraining, rather than a property of pretraining data alone. It specifies a deployable standard for idea safety, integrating control, traceability, and equitability as requirements for credible collaboration between creators and platforms. This synthesis complements privacy techniques, extends RLHF operations with provenance obligations, and grounds economic concerns in a concrete engineering target.

## 7 Conclusion

This paper studies a structural risk, called Black Box Absorption, in which interactive use of Large Language Models could allow providers to internalize the functional content of creator contributions in ways that are opaque and difficult to contest. We defined the idea unit as the minimal actionable content exposed during interaction, traced a plausible lifecycle through governance, ingestion, review, curation, and retraining pipelines, and analyzed how informational and structural asymmetries could shift value capture away from originators. Building on this perspective, we proposed the concept of idea safety as a deployable standard grounded in control, traceability, and equitability. The agenda’s importance is both economic and ethical, as sustained innovation depends on credible guarantees that align incentives for contribution. Future work should deliver verifiable provenance and influence accounting, practical unlearning at the level of individual units, and consent and value-sharing mechanisms that operate by default. It should also include reproducible audits and benchmarks for compliance, as well as policy and contractual frameworks that make these guarantees enforceable across providers.

## References

* Anantrasirichai & Bull (2021)

  Nantheera Anantrasirichai and David Bull.
  Artificial intelligence in the creative industries: a review.
  *Artificial Intelligence Review*, 55(1):589–656, July 2021.
  ISSN 1573-7462.
  doi: 10.1007/s10462-021-10039-7.
  URL <http://dx.doi.org/10.1007/s10462-021-10039-7>.
* Anderljung et al. (2023)

  Markus Anderljung, Joslyn Barnhart, Anton Korinek, Jade Leung, Cullen O’Keefe, Jess Whittlestone, Shahar Avin, Miles Brundage, Justin Bullock, Duncan Cass-Beggs, Ben Chang, Tantum Collins, Tim Fist, Gillian Hadfield, Alan Hayes, Lewis Ho, Sara Hooker, Eric Horvitz, Noam Kolt, Jonas Schuett, Yonadav Shavit, Divya Siddarth, Robert Trager, and Kevin Wolf.
  Frontier ai regulation: Managing emerging risks to public safety, 2023.
  URL <https://arxiv.org/abs/2307.03718>.
* Anil et al. (2023)

  Rohan Anil et al.
  Palm 2 technical report, 2023.
  URL <https://arxiv.org/abs/2305.10403>.
* Anthis et al. (2025)

  Jacy Reese Anthis, Ryan Liu, Sean M. Richardson, Austin C. Kozlowski, Bernard Koch, James Evans, Erik Brynjolfsson, and Michael Bernstein.
  Llm social simulations are a promising research method, 2025.
  URL <https://arxiv.org/abs/2504.02234>.
* Arrieta-Ibarra et al. (2018)

  Imanol Arrieta-Ibarra, Leonard Goff, Diego Jiménez-Hernández, Jaron Lanier, and E. Glen Weyl.
  Should we treat data as labor? moving beyond ”free”.
  *AEA Papers and Proceedings*, 108:38–42, May 2018.
  doi: 10.1257/pandp.20181003.
  URL <https://www.aeaweb.org/articles?id=10.1257/pandp.20181003>.
* Arrow (1972)

  K. J. Arrow.
  *Economic Welfare and the Allocation of Resources for Invention*, pp. 219–236.
  Macmillan Education UK, London, 1972.
  ISBN 978-1-349-15486-9.
  doi: 10.1007/978-1-349-15486-9˙13.
  URL <https://doi.org/10.1007/978-1-349-15486-9_13>.
* Bae et al. (2022)

  Juhan Bae, Nathan Hoyen Ng, Alston Lo, Marzyeh Ghassemi, and Roger Baker Grosse.
  If influence functions are the answer, then what is the question?
  In Alice H. Oh, Alekh Agarwal, Danielle Belgrave, and Kyunghyun Cho (eds.), *Advances in Neural Information Processing Systems*, 2022.
  URL <https://openreview.net/forum?id=hzbguA9zMJ>.
* Bae et al. (2024)

  Juhan Bae, Wu Lin, Jonathan Lorraine, and Roger Grosse.
  Training data attribution via approximate unrolling.
  In A. Globerson, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak, and C. Zhang (eds.), *Advances in Neural Information Processing Systems*, volume 37, pp. 66647–66686. Curran Associates, Inc., 2024.
  URL <https://proceedings.neurips.cc/paper_files/paper/2024/file/7af60ccb99c7a434a0d9d9c1fb00ca94-Paper-Conference.pdf>.
* Bai et al. (2022)

  Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion, Andy Jones, Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, Carol Chen, Catherine Olsson, Christopher Olah, Danny Hernandez, Dawn Drain, Deep Ganguli, Dustin Li, Eli Tran-Johnson, Ethan Perez, Jamie Kerr, Jared Mueller, Jeffrey Ladish, Joshua Landau, Kamal Ndousse, Kamile Lukosuite, Liane Lovitt, Michael Sellitto, Nelson Elhage, Nicholas Schiefer, Noemi Mercado, Nova DasSarma, Robert Lasenby, Robin Larson, Sam Ringer, Scott Johnston, Shauna Kravec, Sheer El Showk, Stanislav Fort, Tamera Lanham, Timothy Telleen-Lawton, Tom Conerly, Tom Henighan, Tristan Hume, Samuel R. Bowman, Zac Hatfield-Dodds, Ben Mann, Dario Amodei, Nicholas Joseph, Sam McCandlish, Tom Brown, and Jared Kaplan.
  Constitutional ai: Harmlessness from ai feedback, 2022.
  URL <https://arxiv.org/abs/2212.08073>.
* Bender et al. (2021)

  Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell.
  On the dangers of stochastic parrots: Can language models be too big?
  In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency*, FAccT ’21, pp. 610–623, New York, NY, USA, 2021. Association for Computing Machinery.
  ISBN 9781450383097.
  doi: 10.1145/3442188.3445922.
  URL <https://doi.org/10.1145/3442188.3445922>.
* BigScience Workshop (2023)

  BigScience Workshop.
  Bloom: A 176b-parameter open-access multilingual language model, 2023.
  URL <https://arxiv.org/abs/2211.05100>.
* Bommasani et al. (2024)

  Rishi Bommasani, Sayash Kapoor, Kevin Klyman, Shayne Longpre, Ashwin Ramaswami, Daniel Zhang, Marietje Schaake, Daniel E. Ho, Arvind Narayanan, and Percy Liang.
  Considerations for governing open foundation models.
  *Science*, 386(6718):151–153, October 2024.
  ISSN 0036-8075, 1095-9203.
  doi: 10.1126/science.adp1848.
  URL <https://www.science.org/doi/10.1126/science.adp1848>.
* Bommasani et al. (2022)

  Rishi Bommasani et al.
  On the opportunities and risks of foundation models, 2022.
  URL <https://arxiv.org/abs/2108.07258>.
* Brevini & Pasquale (2020)

  Benedetta Brevini and Frank Pasquale.
  Revisiting the black box society by rethinking the political economy of big data.
  *Big Data & Society*, 7(2):2053951720935146, 2020.
  doi: 10.1177/2053951720935146.
  URL <https://doi.org/10.1177/2053951720935146>.
* Brown et al. (2022)

  Hannah Brown, Katherine Lee, Fatemehsadat Mireshghallah, Reza Shokri, and Florian Tramèr.
  What does it mean for a language model to preserve privacy?, 2022.
  URL <https://arxiv.org/abs/2202.05520>.
* Brynjolfsson et al. (2025)

  Erik Brynjolfsson, Danielle Li, and Lindsey Raymond.
  Generative ai at work\*.
  *The Quarterly Journal of Economics*, 140(2):889–942, 02 2025.
  ISSN 0033-5533.
  doi: 10.1093/qje/qjae044.
  URL <https://doi.org/10.1093/qje/qjae044>.
* Burrell (2016)

  Jenna Burrell.
  How the machine ?thinks?: Understanding opacity in machine learning algorithms.
  *Big Data and Society*, 3(1):205395171562251, 2016.
  doi: 10.1177/2053951715622512.
* Carlini et al. (2021)

  Nicholas Carlini, Florian Tramer, Eric Wallace, Matthew Jagielski, Ariel Herbert-Voss, Katherine Lee, Adam Roberts, Tom Brown, Dawn Song, Ulfar Erlingsson, Alina Oprea, and Colin Raffel.
  Extracting training data from large language models, 2021.
  URL <https://arxiv.org/abs/2012.07805>.
* Carlini et al. (2023a)

  Nicholas Carlini, Jamie Hayes, Milad Nasr, Matthew Jagielski, Vikash Sehwag, Florian Tramèr, Borja Balle, Daphne Ippolito, and Eric Wallace.
  Extracting training data from diffusion models, 2023a.
  URL <https://arxiv.org/abs/2301.13188>.
* Carlini et al. (2023b)

  Nicholas Carlini, Daphne Ippolito, Matthew Jagielski, Katherine Lee, Florian Tramer, and Chiyuan Zhang.
  Quantifying memorization across neural language models, 2023b.
  URL <https://arxiv.org/abs/2202.07646>.
* Casper et al. (2024)

  Stephen Casper, Carson Ezell, Charlotte Siegmann, Noam Kolt, Taylor Lynn Curtis, Benjamin Bucknall, Andreas Haupt, Kevin Wei, Jérémy Scheurer, Marius Hobbhahn, Lee Sharkey, Satyapriya Krishna, Marvin Von Hagen, Silas Alberti, Alan Chan, Qinyi Sun, Michael Gerovitch, David Bau, Max Tegmark, David Krueger, and Dylan Hadfield-Menell.
  Black-box access is insufficient for rigorous ai audits.
  In *The 2024 ACM Conference on Fairness, Accountability, and Transparency*, FAccT ’24, pp. 2254–2272. ACM, June 2024.
  doi: 10.1145/3630106.3659037.
  URL <http://dx.doi.org/10.1145/3630106.3659037>.
* Chatterji et al. (2025)

  Aaron Chatterji, Tom Cunningham, David J. Deming, Zoë Hitzig, Christopher Ong, Carl Yan Shan, and Kevin Wadman.
  How people use chatgpt.
  Technical Report w34255, National Bureau of Economic Research, 2025.
  URL <https://cdn.openai.com/pdf/a253471f-8260-40c6-a2cc-aa93fe9f142e/economic-research-chatgpt-usage-paper.pdf>.
* Comanici et al. (2025)

  Gheorghe Comanici, Eric Bieber, Mike Schaekermann, Ice Pasupat, Noveen Sachdeva, Inderjit Dhillon, Marcel Blistein, Ori Ram, Dan Zhang, Evan Rosen, et al.
  Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities, 2025.
  URL <https://arxiv.org/abs/2507.06261>.
* Croes et al. (2024)

  Emmelyn A J Croes, Marjolijn L Antheunis, Chris van der Lee, and Jan M S de Wit.
  Digital confessions: The willingness to disclose intimate information to a chatbot and its impact on emotional well-being.
  *Interacting with Computers*, 36(5):279–292, 06 2024.
  ISSN 1873-7951.
  doi: 10.1093/iwc/iwae016.
  URL <https://doi.org/10.1093/iwc/iwae016>.
* de Castro et al. (2024)

  Leo de Castro, Antigoni Polychroniadou, and Daniel Escudero.
  Privacy-preserving large language model inference via GPU-accelerated fully homomorphic encryption.
  In *Neurips Safe Generative AI Workshop 2024*, 2024.
  URL <https://openreview.net/forum?id=Rs7h1od6ov>.
* Dell’Acqua et al. (2023)

  Fabrizio Dell’Acqua, Edward McFowland III, Ethan R. Mollick, Hila Lifshitz-Assaf, Katherine Kellogg, Saran Rajendran, Lisa Krayer, François Candelon, and Karim R. Lakhani.
  Navigating the jagged technological frontier: Field experimental evidence of the effects of ai on knowledge worker productivity and quality, September 2023.
  URL <https://ssrn.com/abstract=4573321>.
  Harvard Business School Technology & Operations Mgt. Unit Working Paper No. 24-013, The Wharton School Research Paper.
* Dong et al. (2024)

  Hanze Dong, Wei Xiong, Bo Pang, Haoxiang Wang, Han Zhao, Yingbo Zhou, Nan Jiang, Doyen Sahoo, Caiming Xiong, and Tong Zhang.
  RLHF workflow: From reward modeling to online RLHF.
  *Transactions on Machine Learning Research*, 2024.
  ISSN 2835-8856.
  URL <https://openreview.net/forum?id=a13aYUU9eU>.
* Franco et al. (2023)

  Mirko Franco, Ombretta Gaggi, and Claudio E. Palazzi.
  Analyzing the use of large language models for content moderation with chatgpt examples.
  In *Proceedings of the 3rd International Workshop on Open Challenges in Online Social Networks*, OASIS ’23, pp. 1–8, New York, NY, USA, 2023. Association for Computing Machinery.
  ISBN 9798400702259.
  doi: 10.1145/3599696.3612895.
  URL <https://doi.org/10.1145/3599696.3612895>.
* Gans & Stern (2010)

  Joshua S. Gans and Scott Stern.
  Is there a market for ideas?
  *Industrial and Corporate Change*, 19(3):805–837, 04 2010.
  ISSN 0960-6491.
  doi: 10.1093/icc/dtq023.
  URL <https://doi.org/10.1093/icc/dtq023>.
* Gao et al. (2025)

  Lan Gao, Oscar Chen, Rachel Lee, Nick Feamster, Chenhao Tan, and Marshini Chetty.
  ”i cannot write this because it violates our content policy”: Understanding content moderation policies and user experiences in generative ai products, 2025.
  URL <https://arxiv.org/abs/2506.14018>.
* Gemini Team (2025a)

  Gemini Team.
  Gemini: A family of highly capable multimodal models, 2025a.
  URL <https://arxiv.org/abs/2312.11805>.
* Gemini Team (2025b)

  Gemini Team.
  Gemini: A family of highly capable multimodal models, May 2025b.
  URL <http://arxiv.org/abs/2312.11805>.
  arXiv:2312.11805 [cs].
* Gilardi et al. (2023)

  Fabrizio Gilardi, Meysam Alizadeh, and Maël Kubli.
  Chatgpt outperforms crowd workers for text-annotation tasks.
  *Proceedings of the National Academy of Sciences*, 120(30):e2305016120, 2023.
  doi: 10.1073/pnas.2305016120.
  URL <https://www.pnas.org/doi/abs/10.1073/pnas.2305016120>.
* Green et al. (2025)

  Tommaso Green, Martin Gubri, Haritz Puerto, Sangdoo Yun, and Seong Joon Oh.
  Leaky thoughts: Large reasoning models are not private thinkers, 2025.
  URL <https://arxiv.org/abs/2506.15674>.
* Han et al. (2025)

  Eric Han, Jun Chen, Karthik Abinav Sankararaman, Xiaoliang Peng, Tengyu Xu, Eryk Helenowski, Kaiyan Peng, Mrinal Kumar, Sinong Wang, Han Fang, and Arya Talebzadeh.
  Reinforcement learning from user feedback, 2025.
  URL <https://arxiv.org/abs/2505.14946>.
* Hao et al. (2022)

  Meng Hao, Hongwei Li, Hanxiao Chen, Pengzhi Xing, Guowen Xu, and Tianwei Zhang.
  Iron: Private inference on transformers.
  In Alice H. Oh, Alekh Agarwal, Danielle Belgrave, and Kyunghyun Cho (eds.), *Advances in Neural Information Processing Systems*, 2022.
  URL <https://openreview.net/forum?id=deyqjpcTfsG>.
* Heller & Eisenberg (1998)

  M. A. Heller and R. S. Eisenberg.
  Can patents deter innovation? the anticommons in biomedical research.
  *Science*, 280(5364):698–701, 1998.
  doi: 10.1126/science.280.5364.698.
* Hoover et al. (2025)

  Monte Hoover, Vatsal Baherwani, Neel Jain, Khalid Saifullah, Joseph James Vincent, Chirag Jain, Melissa Kazemi Rad, C. Bayan Bruss, Ashwinee Panda, and Tom Goldstein.
  Dynamic guardian models: Realtime content moderation with user-defined policies.
  In *2nd Workshop on Models of Human Feedback for AI Alignment*, 2025.
  URL <https://openreview.net/forum?id=I2NLG0LGqf>.
* Horton (2023)

  John J. Horton.
  Large language models as simulated economic agents: What can we learn from homo silicus?, 2023.
  URL <https://arxiv.org/abs/2301.07543>.
* Huang et al. (2024)

  Saffron Huang, Divya Siddarth, Liane Lovitt, Thomas I. Liao, Esin Durmus, Alex Tamkin, and Deep Ganguli.
  Collective constitutional ai: Aligning a language model with public input.
  In *The 2024 ACM Conference on Fairness, Accountability, and Transparency*, FAccT ’24, pp. 1395–1417. ACM, June 2024.
  doi: 10.1145/3630106.3658979.
  URL <http://dx.doi.org/10.1145/3630106.3658979>.
* Huang et al. (2025)

  Saffron Huang, Esin Durmus, Miles McCain, Kunal Handa, Alex Tamkin, Jerry Hong, Michael Stern, Arushi Somani, Xiuruo Zhang, and Deep Ganguli.
  Values in the wild: Discovering and analyzing values in real-world language model interactions.
  In *Proceedings of the COLM 2025*, 2025.
  URL <https://assets.anthropic.com/m/18d20cca3cde3503/original/Values-in-the-Wild-Paper.pdf>.
  Accepted paper.
* Huang (2025)

  Tao Huang.
  Content moderation by llm: From accuracy to legitimacy, 2025.
  URL <https://arxiv.org/abs/2409.03219>.
* Hubert et al. (2024)

  Kent F. Hubert, Kim N. Awa, and Darya L. Zabelina.
  The current state of artificial intelligence generative language models is more creative than humans on divergent thinking tasks.
  *Scientific Reports*, 14(1):3440, 2024.
  doi: 10.1038/s41598-024-53303-w.
* Kalluri (2020)

  Pratyusha Kalluri.
  Don’t ask if artificial intelligence is good or fair, ask how it shifts power.
  *Nature*, 583(7815):169–169, 2020.
  doi: 10.1038/d41586-020-02003-2.
* Kandpal et al. (2023)

  Nikhil Kandpal, Haikang Deng, Adam Roberts, Eric Wallace, and Colin Raffel.
  Large language models struggle to learn long-tail knowledge, 2023.
  URL <https://arxiv.org/abs/2211.08411>.
* Kapoor et al. (2024)

  Sayash Kapoor, Rishi Bommasani, Kevin Klyman, Shayne Longpre, Ashwin Ramaswami, Peter Cihon, Aspen Hopkins, Kevin Bankston, Stella Biderman, Miranda Bogen, Rumman Chowdhury, Alex Engler, Peter Henderson, Yacine Jernite, Seth Lazar, Stefano Maffulli, Alondra Nelson, Joelle Pineau, Aviya Skowron, Dawn Song, Victor Storchan, Daniel Zhang, Daniel E. Ho, Percy Liang, and Arvind Narayanan.
  On the societal impact of open foundation models, 2024.
  URL <https://arxiv.org/abs/2403.07918>.
* Kim et al. (2025)

  Gyuwan Kim, Yang Li, Evangelia Spiliopoulou, Jie Ma, Miguel Ballesteros, and William Yang Wang.
  Detecting training data of large language models via expectation maximization, 2025.
  URL <https://arxiv.org/abs/2410.07582>.
* Kim et al. (2018)

  Miryung Kim, Thomas Zimmermann, Robert DeLine, and Andrew Begel.
  Data scientists in software teams: state of the art and challenges.
  In *Proceedings of the 40th International Conference on Software Engineering*, ICSE ’18, pp. 585, New York, NY, USA, 2018. Association for Computing Machinery.
  ISBN 9781450356381.
  doi: 10.1145/3180155.3182515.
  URL <https://doi.org/10.1145/3180155.3182515>.
* King et al. (2025)

  Jennifer King, Kevin Klyman, Emily Capstick, Tiffany Saade, and Victoria Hsieh.
  User privacy and large language models: An analysis of frontier developers’ privacy policies, 2025.
  URL <https://arxiv.org/abs/2509.05382>.
* Kleinberg & Raghavan (2021)

  Jon Kleinberg and Manish Raghavan.
  Algorithmic monoculture and social welfare.
  *Proceedings of the National Academy of Sciences*, 118(22), May 2021.
  ISSN 1091-6490.
  doi: 10.1073/pnas.2018340118.
  URL <http://dx.doi.org/10.1073/pnas.2018340118>.
* Kumar et al. (2024)

  Deepak Kumar, Yousef AbuHashem, and Zakir Durumeric.
  Watch your language: Investigating content moderation with large language models, 2024.
  URL <https://arxiv.org/abs/2309.14517>.
* Kyi et al. (2025)

  Lin Kyi, Amruta Mahuli, M. Six Silberman, Reuben Binns, Jun Zhao, and Asia J. Biega.
  Governance of generative ai in creative work: Consent, credit, compensation, and beyond, 2025.
  URL <https://arxiv.org/abs/2501.11457>.
* Lee & Mendelson (2007)

  Deishin Lee and Haim Mendelson.
  Adoption of information technology under network effects.
  *Info. Sys. Research*, 18(4):395–413, December 2007.
  ISSN 1526-5536.
  doi: 10.1287/isre.1070.0138.
  URL <https://doi.org/10.1287/isre.1070.0138>.
* Lee et al. (2024)

  Harrison Lee, Samrat Phatale, Hassan Mansoor, Thomas Mesnard, Johan Ferret, Kellie Lu, Colton Bishop, Ethan Hall, Victor Carbune, Abhinav Rastogi, and Sushant Prakash.
  Rlaif vs. rlhf: Scaling reinforcement learning from human feedback with ai feedback, 2024.
  URL <https://arxiv.org/abs/2309.00267>.
* Li et al. (2024)

  Zhengyi Li, Kang Yang, Jin Tan, Wen-jie Lu, Haoqi Wu, Xiao Wang, Yu Yu, Derun Zhao, Yancheng Zheng, Minyi Guo, and Jingwen Leng.
  Nimbus: Secure and efficient two-party inference for transformers.
  In A. Globerson, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak, and C. Zhang (eds.), *Advances in Neural Information Processing Systems*, volume 37, pp. 21572–21600. Curran Associates, Inc., 2024.
  URL <https://proceedings.neurips.cc/paper_files/paper/2024/file/264a9b3ce46abdf572dcfe0401141989-Paper-Conference.pdf>.
* Lin & Ryaboy (2013)

  Jimmy Lin and Dmitriy Ryaboy.
  Scaling big data mining infrastructure: the twitter experience.
  *SIGKDD Explor. Newsl.*, 14(2):6–19, April 2013.
  ISSN 1931-0145.
  doi: 10.1145/2481244.2481247.
  URL <https://doi.org/10.1145/2481244.2481247>.
* Liu et al. (2024)

  Wei Liu, Weihao Zeng, Keqing He, Yong Jiang, and Junxian He.
  What makes good data for alignment? a comprehensive study of automatic data selection in instruction tuning, 2024.
  URL <https://arxiv.org/abs/2312.15685>.
* Liu et al. (2025)

  Yuhan Liu, Michael J. Q. Zhang, and Eunsol Choi.
  User feedback in human-llm dialogues: A lens to understand users but noisy as a learning signal, 2025.
  URL <https://arxiv.org/abs/2507.23158>.
* LLC (2024)

  Google LLC.
  Generative ai and privacy: Policy recommendations working paper.
  Technical report, Google LLC, Mountain View, CA, USA, June 2024.
  URL <https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/Google_Generative_AI_and_Privacy_-_Policy_Recommendations_Working_Paper_-_June_2024.pdf>.
  Working paper.
* LLC (2025)

  Google LLC.
  Delivering trusted and secure ai.
  Technical report, Google Cloud, Google LLC, Mountain View, CA, USA, March 2025.
  URL <https://services.google.com/fh/files/misc/google_cloud_delivering_trusted_and_secure_ai.pdf>.
  White paper.
* Lucas et al. (2014)

  Gale M. Lucas, J. Gratch, Aisha King, and Louis philippe Morency.
  It’s only a computer: Virtual humans increase willingness to disclose.
  *Comput. Hum. Behav.*, 37:94–100, 2014.
  URL <https://api.semanticscholar.org/CorpusID:8823921>.
* Lukas et al. (2023)

  Nils Lukas, Ahmed Salem, Robert Sim, Shruti Tople, Lukas Wutschitz, and Santiago Zanella-Béguelin.
  Analyzing Leakage of Personally Identifiable Information in Language Models, April 2023.
  URL <http://arxiv.org/abs/2302.00539>.
  arXiv:2302.00539 [cs].
* Ma et al. (2025)

  Rongjun Ma, Caterina Maidhof, Juan Carlos Carrillo, Janne Lindqvist, and Jose Such.
  Privacy perceptions of custom gpts by users and creators.
  In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems*, CHI ’25, New York, NY, USA, 2025. Association for Computing Machinery.
  ISBN 9798400713941.
  doi: 10.1145/3706598.3713540.
  URL <https://doi.org/10.1145/3706598.3713540>.
* Markov et al. (2023)

  Todor Markov, Chong Zhang, Sandhini Agarwal, Tyna Eloundou, Teddy Lee, Steven Adler, Angela Jiang, and Lilian Weng.
  A holistic approach to undesired content detection in the real world, 2023.
  URL <https://arxiv.org/abs/2208.03274>.
* Mireshghallah & Li (2025)

  Niloofar Mireshghallah and Tianshi Li.
  Position: Privacy is not just memorization!, 2025.
  URL <https://arxiv.org/abs/2510.01645>.
* Mireshghallah et al. (2024)

  Niloofar Mireshghallah, Hyunwoo Kim, Xuhui Zhou, Yulia Tsvetkov, Maarten Sap, Reza Shokri, and Yejin Choi.
  Can LLMs keep a secret? testing privacy implications of language models via contextual integrity theory.
  In *The Twelfth International Conference on Learning Representations*, 2024.
  URL <https://openreview.net/forum?id=gmg7t8b4s0>.
* Narechania (2021)

  Tejas N. Narechania.
  Machine learning as natural monopoly.
  *SSRN Electronic Journal*, 2021.
  ISSN 1556-5068.
  doi: 10.2139/ssrn.3810366.
  URL <https://www.ssrn.com/abstract=3810366>.
* Narechania & Sitaraman (2024)

  Tejas N. Narechania and Ganesh Sitaraman.
  An antimonopoly approach to governing artificial intelligence.
  *Yale Law & Policy Review*, 43(1):95–170, 2024.
  URL <https://yalelawandpolicy.org/sites/default/files/YLPR/narechania_sitaraman_anantimonopolyapproach_ylpr_2024.pdf>.
* Nazabal et al. (2020)

  Alfredo Nazabal, Christopher K. I. Williams, Giovanni Colavizza, Camila Rangel Smith, and Angus Williams.
  Data engineering for data analytics: A classification of the issues, and case studies, 2020.
  URL <https://arxiv.org/abs/2004.12929>.
* Nghiem & Daumé Iii (2024)

  Huy Nghiem and Hal Daumé Iii.
  HateCOT: An explanation-enhanced dataset for generalizable offensive speech detection via large language models.
  In Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Chen (eds.), *Findings of the Association for Computational Linguistics: EMNLP 2024*, pp. 5938–5956, Miami, Florida, USA, November 2024. Association for Computational Linguistics.
  doi: 10.18653/v1/2024.findings-emnlp.343.
  URL <https://aclanthology.org/2024.findings-emnlp.343/>.
* Ngong et al. (2025)

  Ivoline Ngong, Swanand Kadhe, Hao Wang, Keerthiram Murugesan, Justin D. Weisz, Amit Dhurandhar, and Karthikeyan Natesan Ramamurthy.
  Protecting users from themselves: Safeguarding contextual privacy in interactions with conversational agents, 2025.
  URL <https://arxiv.org/abs/2502.18509>.
* Novikov et al. (2025)

  Alexander Novikov, Ngân Vũ, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco J. R. Ruiz, Abbas Mehrabian, M. Pawan Kumar, Abigail See, Swarat Chaudhuri, George Holland, Alex Davies, Sebastian Nowozin, Pushmeet Kohli, and Matej Balog.
  Alphaevolve: A coding agent for scientific and algorithmic discovery, 2025.
  URL <https://arxiv.org/abs/2506.13131>.
* Noy & Zhang (2023)

  Shakked Noy and Whitney Zhang.
  Experimental evidence on the productivity effects of generative artificial intelligence.
  *Science*, 381(6654):187–192, 2023.
  doi: 10.1126/science.adh2586.
  URL <https://www.science.org/doi/abs/10.1126/science.adh2586>.
* Oakley (2005)

  Robert L. Oakley.
  Fairness in electronic contracting: Minimum standards for non‐negotiated contracts.
  *Houston Law Review*, 42(4):1041–1105, 2005.
  URL <https://houstonlawreview.org/article/4789>.
  Posted: 24 Feb 2009 on SSRN; also SSRN ID 1348815.
* OpenAI (2024)

  et al. OpenAI.
  Gpt-4 technical report, 2024.
  URL <https://arxiv.org/abs/2303.08774>.
* Ouyang et al. (2022)

  Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul F Christiano, Jan Leike, and Ryan Lowe.
  Training language models to follow instructions with human feedback.
  In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh (eds.), *Advances in Neural Information Processing Systems*, volume 35, pp. 27730–27744. Curran Associates, Inc., 2022.
  URL <https://proceedings.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf>.
* Pahune & Akhtar (2025)

  Saurabh Pahune and Zahid Akhtar.
  Transitioning from mlops to llmops: Navigating the unique challenges of large language models.
  *Information*, 16(2), 2025.
  ISSN 2078-2489.
  doi: 10.3390/info16020087.
  URL <https://www.mdpi.com/2078-2489/16/2/87>.
* Paleyes et al. (2022)

  Andrei Paleyes, Raoul-Gabriel Urma, and Neil D. Lawrence.
  Challenges in deploying machine learning: A survey of case studies.
  *ACM Computing Surveys*, 55(6):1–29, December 2022.
  ISSN 1557-7341.
  doi: 10.1145/3533378.
  URL <http://dx.doi.org/10.1145/3533378>.
* Park et al. (2023)

  Sung Min Park, Kristian Georgiev, Andrew Ilyas, Guillaume Leclerc, and Aleksander Madry.
  Trak: Attributing model behavior at scale, 2023.
  URL <https://arxiv.org/abs/2303.14186>.
* Partha & David (1994)

  Dasgupta Partha and Paul A. David.
  Toward a new economics of science.
  *Research Policy*, 23(5):487–521, 1994.
  ISSN 0048-7333.
  doi: https://doi.org/10.1016/0048-7333(94)01002-1.
  URL <https://www.sciencedirect.com/science/article/pii/0048733394010021>.
  Special Issue in Honor of Nathan Rosenberg.
* Pasquale (2015)

  Frank Pasquale.
  *The Black Box Society: The Secret Algorithms That Control Money and Information*.
  Harvard University Press, USA, 2015.
  ISBN 0674368274.
* Pasquale & Sun (2024)

  Frank A. Pasquale and Haochen Sun.
  Consent and compensation: Resolving generative ai’s copyright crisis, May 2024.
  URL <https://ssrn.com/abstract=4826695>.
  Cornell Legal Studies Research Paper Volume 26, No. 5, University of Hong Kong Faculty of Law Research Paper No. 2024/07.
* PBC (2025)

  Anthropic PBC.
  System card: Claude opus 4 & claude sonnet 4.
  Technical report, Anthropic PBC, San Francisco, CA, USA, May 22 2025.
  URL <https://www.anthropic.com/model-card>.
  System card for Claude 4 model family.
* PBC & Labs (2025)

  Anthropic PBC and Pattern Labs.
  Confidential inference via trusted virtual machines.
  Technical report, Anthropic PBC, San Francisco, CA, USA, June 2025.
  URL <https://www.anthropic.com/research/confidential-inference-trusted-vms>.
  White-paper/Technical Report.
* Raji et al. (2020)

  Inioluwa Deborah Raji, Andrew Smart, Rebecca N. White, Margaret Mitchell, Timnit Gebru, Ben Hutchinson, Jamila Smith-Loud, Daniel Theron, and Parker Barnes.
  Closing the ai accountability gap: Defining an end-to-end framework for internal algorithmic auditing, 2020.
  URL <https://arxiv.org/abs/2001.00973>.
* Resnick & Zeckhauser (2002)

  Paul Resnick and Richard Zeckhauser.
  Trust among strangers in internet transactions: Empirical analysis of ebay’ s reputation system.
  In *The Economics of the Internet and E-commerce*. Emerald Group Publishing Limited, 10 2002.
  ISBN 978-0-76230-971-9.
  doi: 10.1016/S0278-0984(02)11030-3.
  URL <https://doi.org/10.1016/S0278-0984(02)11030-3>.
* Roy et al. (2023)

  Sarthak Roy, Ashish Harshvardhan, Animesh Mukherjee, and Punyajoy Saha.
  Probing LLMs for hate speech detection: strengths and vulnerabilities.
  In Houda Bouamor, Juan Pino, and Kalika Bali (eds.), *Findings of the Association for Computational Linguistics: EMNLP 2023*, pp. 6116–6128, Singapore, December 2023. Association for Computational Linguistics.
  doi: 10.18653/v1/2023.findings-emnlp.407.
  URL <https://aclanthology.org/2023.findings-emnlp.407/>.
* Sastry et al. (2024)

  Girish Sastry, Lennart Heim, Haydn Belfield, Markus Anderljung, Miles Brundage, Julian Hazell, Cullen O’Keefe, Gillian K. Hadfield, Richard Ngo, Konstantin Pilz, George Gor, Emma Bluemke, Sarah Shoker, Janet Egan, Robert F. Trager, Shahar Avin, Adrian Weller, Yoshua Bengio, and Diane Coyle.
  Computing power and the governance of artificial intelligence, 2024.
  URL <https://arxiv.org/abs/2402.08797>.
* Scotchmer (1991)

  Suzanne Scotchmer.
  Standing on the shoulders of giants: Cumulative research and the patent law.
  *Journal of Economic Perspectives*, 5(1):29–41, March 1991.
  doi: 10.1257/jep.5.1.29.
  URL <https://www.aeaweb.org/articles?id=10.1257/jep.5.1.29>.
* Sculley et al. (2015)

  D. Sculley, Gary Holt, Daniel Golovin, Eugene Davydov, Todd Phillips, Dietmar Ebner, Vinay Chaudhary, Michael Young, Jean-François Crespo, and Dan Dennison.
  Hidden technical debt in machine learning systems.
  In C. Cortes, N. Lawrence, D. Lee, M. Sugiyama, and R. Garnett (eds.), *Advances in Neural Information Processing Systems*, volume 28. Curran Associates, Inc., 2015.
  URL <https://proceedings.neurips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf>.
* Shao et al. (2024)

  Yijia Shao, Tianshi Li, Weiyan Shi, Yanchen Liu, and Diyi Yang.
  Privacylens: Evaluating privacy norm awareness of language models in action.
  In *The Thirty-eight Conference on Neural Information Processing Systems Datasets and Benchmarks Track*, 2024.
  URL <https://openreview.net/forum?id=CxNXoMnCKc>.
* Sheth et al. (2023)

  Paras Sheth, Tharindu Kumarage, Raha Moraffah, Aman Chadha, and Huan Liu.
  Causality guided disentanglement for cross-platform hate speech detection, 2023.
  URL <https://arxiv.org/abs/2308.02080>.
* Shi et al. (2024)

  Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer.
  Detecting pretraining data from large language models, 2024.
  URL <https://arxiv.org/abs/2310.16789>.
* Shokri et al. (2017)

  Reza Shokri, Marco Stronati, Congzheng Song, and Vitaly Shmatikov.
  Membership inference attacks against machine learning models, 2017.
  URL <https://arxiv.org/abs/1610.05820>.
* Si et al. (2025)

  Chenglei Si, Diyi Yang, and Tatsunori Hashimoto.
  Can LLMs generate novel research ideas? a large-scale human study with 100+ NLP researchers.
  In *The Thirteenth International Conference on Learning Representations*, 2025.
  URL <https://openreview.net/forum?id=M23dTGWCZy>.
* Solaiman (2023)

  Irene Solaiman.
  The gradient of generative ai release: Methods and considerations, 2023.
  URL <https://arxiv.org/abs/2302.04844>.
* Staab et al. (2024)

  Robin Staab, Mark Vero, Mislav Balunović, and Martin Vechev.
  Beyond memorization: Violating privacy via inference with large language models, 2024.
  URL <https://arxiv.org/abs/2310.07298>.
* Tamkin et al. (2024)

  Alex Tamkin, Miles McCain, Kunal Handa, Esin Durmus, Liane Lovitt, Ankur Rathi, Saffron Huang, Alfred Mountfield, Jerry Hong, Stuart Ritchie, Michael Stern, Brian Clarke, Landon Goldberg, Theodore R. Sumers, Jared Mueller, William McEachen, Wes Mitchell, Shan Carter, Jack Clark, Jared Kaplan, and Deep Ganguli.
  Clio: Privacy-preserving insights into real-world ai use, 2024.
  URL <https://arxiv.org/abs/2412.13678>.
* Tang et al. (2025)

  Jingyu Tang, Chaoran Chen, Jiawen Li, Zhiping Zhang, Bingcan Guo, Ibrahim Khalilov, Simret Araya Gebreegziabher, Bingsheng Yao, Dakuo Wang, Yanfang Ye, Tianshi Li, Ziang Xiao, Yaxing Yao, and Toby Jia-Jun Li.
  Dark patterns meet gui agents: Llm agent susceptibility to manipulative interfaces and the role of human oversight, 2025.
  URL <https://arxiv.org/abs/2509.10723>.
* Teece (1986)

  David J. Teece.
  Profiting from technological innovation: Implications for integration, collaboration, licensing and public policy.
  *Research Policy*, 15(6):285–305, 1986.
  ISSN 0048-7333.
  doi: https://doi.org/10.1016/0048-7333(86)90027-2.
  URL <https://www.sciencedirect.com/science/article/pii/0048733386900272>.
* Touvron et al. (2023)

  Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami, Naman Goyal, Anthony Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian, Xiaoqing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aurelien Rodriguez, Robert Stojnic, Sergey Edunov, and Thomas
  Scialom.
  Llama 2: Open foundation and fine-tuned chat models, 2023.
  URL <https://arxiv.org/abs/2307.09288>.
* Tran et al. (2025)

  Sarah Tran, Hongfan Lu, Isaac Slaughter, Bernease Herman, Aayushi Dangol, Yue Fu, Lufei Chen, Biniyam Gebreyohannes, Bill Howe, Alexis Hiniker, Nicholas Weber, and Robert Wolfe.
  Understanding privacy norms around llm-based chatbots: A contextual integrity perspective, 2025.
  URL <https://arxiv.org/abs/2508.06760>.
* U.S. Congress (1976)

  U.S. Congress.
  United States Code, Title 17, Section 102(b).
  17 U.S.C. § 102(b), 1976.
  This section of the U.S. Copyright Act codifies the idea-expression dichotomy, stating that copyright protection does not extend to any ”idea, procedure, process, system, method of operation, concept, principle, or discovery.”.
* U.S. Supreme Court (1879)

  U.S. Supreme Court.
  Baker v. Selden.
  101 U.S. 99, 1879.
  A landmark U.S. Supreme Court decision that is considered to have established the idea-expression dichotomy in copyright law.
* Vipra & Korinek (2023)

  Jai Vipra and Anton Korinek.
  Market concentration implications of foundation models, 2023.
  URL <https://arxiv.org/abs/2311.01550>.
* Vishwamitra et al. (2024)

  Nishant Vishwamitra, Keyan Guo, Farhan Tajwar Romit, Isabelle Ondracek, Long Cheng, Ziming Zhao, and Hongxin Hu.
   Moderating New Waves of Online Hate with Chain-of-Thought Reasoning in Large Language Models .
  In *2024 IEEE Symposium on Security and Privacy (SP)*, pp. 788–806, Los Alamitos, CA, USA, May 2024. IEEE Computer Society.
  doi: 10.1109/SP54263.2024.00181.
  URL <https://doi.ieeecomputersociety.org/10.1109/SP54263.2024.00181>.
* White et al. (2024)

  Matt White, Ibrahim Haddad, Cailean Osborne, Xiao-Yang Yanglet Liu, Ahmed Abdelmonsef, Sachin Varghese, and Arnaud Le Hors.
  The model openness framework: Promoting completeness and openness for reproducibility, transparency, and usability in artificial intelligence, 2024.
  URL <https://arxiv.org/abs/2403.13784>.
* Yi et al. (2025)

  Ren Yi, Octavian Suciu, Adria Gascon, Sarah Meiklejohn, Eugene Bagdasarian, and Marco Gruteser.
  Privacy reasoning in ambiguous contexts, 2025.
  URL <https://arxiv.org/abs/2506.12241>.
* Yu et al. (2023)

  Weichen Yu, Tianyu Pang, Qian Liu, Chao Du, Bingyi Kang, Yan Huang, Min Lin, and Shuicheng Yan.
  Bag of tricks for training data extraction from language models, 2023.
  URL <https://arxiv.org/abs/2302.04460>.
* Zhang et al. (2025)

  Yancheng Zhang, Jiaqi Xue, Mengxin Zheng, Mimi Xie, Mingzhe Zhang, Lei Jiang, and Qian Lou.
  Cipherprune: Efficient and scalable private transformer inference.
  In *The Thirteenth International Conference on Learning Representations*, 2025.
  URL <https://openreview.net/forum?id=mUMvr33FTu>.
* Zhang & Yang (2025)

  Yanzhe Zhang and Diyi Yang.
  Searching for privacy risks in llm agents via simulation, 2025.
  URL <https://arxiv.org/abs/2508.10880>.
* Zhang et al. (2024)

  Zhiping Zhang, Michelle Jia, Hao-Ping (Hank) Lee, Bingsheng Yao, Sauvik Das, Ada Lerner, Dakuo Wang, and Tianshi Li.
  “it’s a fair game”, or is it? examining how users navigate disclosure risks and benefits when using llm-based conversational agents.
  In *Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems*, CHI ’24, New York, NY, USA, 2024. Association for Computing Machinery.
  ISBN 9798400703300.
  doi: 10.1145/3613904.3642385.
  URL <https://doi.org/10.1145/3613904.3642385>.