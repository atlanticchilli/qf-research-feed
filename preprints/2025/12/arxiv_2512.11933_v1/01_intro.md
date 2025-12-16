---
authors:
- Eren Kurshan
- Tucker Balch
- David Byrd
doc_id: arxiv:2512.11933v1
family_id: arxiv:2512.11933
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'The Agentic Regulator: Risks for AI in Finance and a Proposed Agent-based
  Framework for Governance'
url_abs: http://arxiv.org/abs/2512.11933v1
url_html: https://arxiv.org/html/2512.11933v1
venue: arXiv q-fin
version: 1
year: 2025
---


Eren Kurshan
Princeton UniversityPrincetonNew Jersey
[ekurshan@princeton.edu](mailto:ekurshan@princeton.edu)
, 
Tucker Balch
Emory UniversityAtlantaGeorgia
[tucker.balch@emory.edu](mailto:tucker.balch@emory.edu)
 and 
David Byrd
Bowdoin CollegeBrunswickMaine
[d.byrd@bowdoin.edu](mailto:d.byrd@bowdoin.edu)

###### Abstract.

Generative and agentic artificial intelligence is entering financial markets faster than existing governance can adapt. Current model-risk frameworks assume static, well-specified algorithms and one-time validations; large language models and multi-agent trading systems violate those assumptions by learning continuously, exchanging latent signals, and exhibiting emergent behavior. Drawing on complex adaptive systems theory, we model these technologies as decentralized ensembles whose risks propagate along multiple time-scales. We then propose a modular governance architecture. The framework decomposes oversight into four layers of “regulatory blocks”: (i) self-regulation modules embedded beside each model, (ii) firm-level governance blocks that aggregate local telemetry and enforce policy, (iii) regulator-hosted agents that monitor sector-wide indicators for collusive or destabilizing patterns, and (iv) independent audit blocks that supply third-party assurance. Eight design strategies enable the blocks to evolve as fast as the models they police. A case study on emergent spoofing in multi-agent trading shows how the layered controls quarantine harmful behavior in real time while preserving innovation. The architecture remains compatible with today’s model-risk rules yet closes critical observability and control gaps, providing a practical path toward resilient, adaptive AI governance in financial systems.

Artificial Intelligence, AI Regulation, Generative AI, Agentic AI, Model Governance, AI Model Risk Management, Financial Services

## 1. Introduction & Background

AI adoption is accelerating across financial services (et.al., [2016b](https://arxiv.org/html/2512.11933v1#bib.bib46), [2019a](https://arxiv.org/html/2512.11933v1#bib.bib25), [2023h](https://arxiv.org/html/2512.11933v1#bib.bib68)), with sector investment projected to reach $97 billion by 2027 (et.al., [2025a](https://arxiv.org/html/2512.11933v1#bib.bib23)). Recent demonstrations show generative and agentic AI tackling increasingly complex use cases (et.al., [2024c](https://arxiv.org/html/2512.11933v1#bib.bib39), [2023d](https://arxiv.org/html/2512.11933v1#bib.bib43)): large language models support financial analysis and advisory (OpenAITeam, [2023](https://arxiv.org/html/2512.11933v1#bib.bib96); GeminiTeam, [2023](https://arxiv.org/html/2512.11933v1#bib.bib80); Anthropic, [2025](https://arxiv.org/html/2512.11933v1#bib.bib5); Grattafiori, [2024](https://arxiv.org/html/2512.11933v1#bib.bib81); DeepMind, [2024](https://arxiv.org/html/2512.11933v1#bib.bib21)), transformers aid time-series modeling and fraud detection (et.al., [2023c](https://arxiv.org/html/2512.11933v1#bib.bib42)), multi-agent and agentic systems advance trading, risk management, portfolio optimization, and market simulation (et.al., [2024b](https://arxiv.org/html/2512.11933v1#bib.bib36); Park, [2024](https://arxiv.org/html/2512.11933v1#bib.bib97)), and AI agents are proposed for core model development tasks (et.al., [2025d](https://arxiv.org/html/2512.11933v1#bib.bib45)).

These capabilities strain traditional risk-management and governance approaches (Y, [2023](https://arxiv.org/html/2512.11933v1#bib.bib108); et.al., [2024e](https://arxiv.org/html/2512.11933v1#bib.bib54)). Even non-agentic systems exceed the practical limits of existing frameworks, while agentic AI amplifies risks related to safety, liability, and autonomy (et.al., [2017a](https://arxiv.org/html/2512.11933v1#bib.bib40); Congress, [1974](https://arxiv.org/html/2512.11933v1#bib.bib15); et.al., [2024g](https://arxiv.org/html/2512.11933v1#bib.bib61); Congress, [1975](https://arxiv.org/html/2512.11933v1#bib.bib16)). Despite active regulatory efforts, a comprehensive governance regime for AI in finance has not yet emerged (E.U., [2024](https://arxiv.org/html/2512.11933v1#bib.bib76); of China, [CAC](https://arxiv.org/html/2512.11933v1#bib.bib93)).

### 1.1. Motivation and Scope

Prior to the emergence of generative AI, financial regulation faced an “Innovation Trilemma” (et.al., [2018a](https://arxiv.org/html/2512.11933v1#bib.bib32)): only two of three key goals, regulatory clarity, market integrity, and innovation, could be pursued simultaneously. GenAI now compounds these tensions. Despite modernization efforts, traditional Model Risk Management (MRM) struggles to cope with the inherent complexity, unpredictability, and opacity of high-parameter models.

Generative AI systems are high-parameter complex systems, marked by nonlinear interactions and emergent behavior that challenge regulatory design. AI-native governance approaches may offer a way forward, but they blur the line between system properties (e.g., trust, controllability) and regulatory mechanisms themselves. As a result, regulating these systems intersects directly with core AI safety challenges, including the alignment problem. Alarmingly, 63% of financial firms have already deployed GenAI systems, and 35% are piloting them (Survey, [2024](https://arxiv.org/html/2512.11933v1#bib.bib101)), highlighting the urgency of governance innovation. This paper outlines key risks and proposes a multi-agent regulatory framework to address them.

### 1.2. MAS Through a CAS Lens

Multi-agent systems (MAS) and complex adaptive systems (CAS) both feature networks of interacting entities, but differ in purpose and origin. MAS stem from engineering: agents are programmed with goals, communication rules, and coordination algorithms to accomplish tasks (Balch and Arkin, [1998](https://arxiv.org/html/2512.11933v1#bib.bib7)). CAS, by contrast, emerge in nature and society, where global behavior arises from decentralized adaptation and local interactions (Holland, [1992](https://arxiv.org/html/2512.11933v1#bib.bib86)). MAS aim for engineered performance; CAS are studied to understand phenomena like self-organization and phase shifts.

MAS already power market simulations and agent-based prototypes, where learning agents compete and adapt (Byrd et al., [2020](https://arxiv.org/html/2512.11933v1#bib.bib10); Byrd, [2022](https://arxiv.org/html/2512.11933v1#bib.bib9)). These dynamics enable stress-testing but also pose governance risks, as agents can learn manipulative or collusive strategies.

From a CAS perspective, both MAS and GenAI systems exhibit emergent, high-dimensional, and adaptive behavior—properties that defy static MRM assumptions like fixed data, stable models, and one-time validations.

In this work, we use MAS to design our regulatory architecture and CAS to analyze its behavior. The framework partitions oversight into interacting regulatory blocks: self-regulation components at the model level, firm-level governance modules, and external audit units. As a multi-agent system, these blocks adapt and coordinate while enforcing safety and compliance constraints. This modular design aligns governance architecture with the systems it must regulate—offering more flexible and resilient oversight than centralized, linear controls.

## 2. The State of AI Regulation and Governance

Adding to this complexity, a growing number of AI regulations are being enacted globally (House, [2023](https://arxiv.org/html/2512.11933v1#bib.bib87); E.U., [2024](https://arxiv.org/html/2512.11933v1#bib.bib76); of China, [CAC](https://arxiv.org/html/2512.11933v1#bib.bib93); METI, [2024](https://arxiv.org/html/2512.11933v1#bib.bib91); Canada, [2024](https://arxiv.org/html/2512.11933v1#bib.bib11)), presenting significant complications for financial firms with global operations. The diversity of regulatory approaches highlights the need for novel AI governance systems and automation. Recent AI regulations follow fundamentally different regulatory philosophies and yield to dramatically different development requirements:

(i) Principles-Based Approach: Provides general guidance without detailed rules or interpretations (e.g. Australia’s 2019 AI Framework (of Industry Science and Resources, [2024](https://arxiv.org/html/2512.11933v1#bib.bib94))).

(ii) Risk-Categorization-Based Approach: Classifies AI systems by their potential risk with stricter oversight for higher risk models (E.U. AI Act (E.U., [2024](https://arxiv.org/html/2512.11933v1#bib.bib76))).

(iii) Rule, Process & Standard-Based Approach: Defines specific rules, standards, and procedural requirements (China’s 2023 GenAI Interim Measures (of China, [CAC](https://arxiv.org/html/2512.11933v1#bib.bib93))).

(iv) Result-Based Approach: Enforces desired outcomes without prescribing detailed rules or processes (Singapore’s 2019 AI Governance Framework (of Singapore, [2020](https://arxiv.org/html/2512.11933v1#bib.bib95))).

This highlights the difficulty of satisfying all four regulatory requirements within a single model development and risk management framework.

Model risk management processes evolved primarily for quantitative mathematical models used in finance with guidance from regulations like SR 11-7 / OCC 2011-12 (FED and OCC, [2011](https://arxiv.org/html/2512.11933v1#bib.bib78)). In addition to missing critical AI regulatory needs like safety assurance, ethics, autonomy control, and emergent behavior management, MRM stages are ineffective for GenAI:

(i) Model Risk Rating: Common static model and stable data assumptions have become obsolete in the latest generation of AI (et.al., [2024a](https://arxiv.org/html/2512.11933v1#bib.bib29)).

(ii) Initial Model Validation: One-time validation of assumptions, code, and performance is inadequate to account for dynamic, non-deterministic behavior inherent in generative and agentic systems.

(iii) Ongoing Monitoring: For generative and agentic AI, periodic reviews are insufficient; it needs real-time, adaptive oversight, making traditional monitoring obsolete. Fintechs do leverage more general continuous model monitoring, but traditional financial institutions are often still dependent on manual periodic reviews with KPI monitoring (et.al., [2024a](https://arxiv.org/html/2512.11933v1#bib.bib29)).

Despite widespread efforts, progress in developing effective model governance and regulatory solutions for generative AI has been limited. Increasing model development costs and MRM challenges have driven financial firms towards a membership strategy from foundational AI model developers, but these increasingly centralized general-purpose AI models have limited support for financial regulations, safety or ethics, and thus pose growing risks.

Financial regulators are rapidly developing new frameworks and regulations for generative and autonomous AI. In the U.S., SEC, OCC, FINRA, and CFTC are all actively engaged in planning and discussions for AI, focusing on risks, governance, and supervisory controls. The Federal Reserve and FDIC have formed internal AI groups to develop guidance, reflecting a strong push for proactive and adaptive AI oversight in finance.

## 3. Risks of AI in Financial Systems

Existing MRM and governance frameworks lack the capacity to address the scale and severity of the emerging risks of AI, which requires a paradigm shift in model governance. This section aims to cover a selection of emerging risks from GenAI (full coverage is beyond the scope of this paper). Generative AI exacerbates existing risks and introduces novel risks. We enumerate them below.

### 3.1. Systemic Risks of AI

In financial services, AI solutions are deployed in complex environments that exhibit dynamic, adversarial conditions. Moreover, AI models increasingly operate in Systems of AI with high degrees of interconnectedness and interdependence. Modern regulatory frameworks, which struggle at even the model level, require new approaches to deal with the unprecedented complexity and unpredictability of such AI systems. As discussed earlier, the GenAI dual-complexity issue causes interlocking of AI regulation with the alignment of the building blocks.

* •

  Data Risks: Generative models amplify data risks due to their high demand for training data and the fact that it is hard to guarantee quality at internet scale (OpenAITeam, [2023](https://arxiv.org/html/2512.11933v1#bib.bib96); GeminiTeam, [2023](https://arxiv.org/html/2512.11933v1#bib.bib80); Anthropic, [2025](https://arxiv.org/html/2512.11933v1#bib.bib5)). Furthermore, fine-tuning in financial AI models rapidly increases AI safety risks and the likelihood of sensitive data leakage (et.al., [2023g](https://arxiv.org/html/2512.11933v1#bib.bib59)).
* •

  Worsening Hallucinations: Despite all efforts to the contrary, generative AI hallucinations worsen in more advanced models (Zeff, [2025](https://arxiv.org/html/2512.11933v1#bib.bib109)).
* •

  Hidden Discrimination and Persistent Toxicity: Despite repeated mitigation efforts, financial AI models still show entrenched bias (et.al., [2023e](https://arxiv.org/html/2512.11933v1#bib.bib44)) and generate toxic outputs (et.al., [2021c](https://arxiv.org/html/2512.11933v1#bib.bib72), [2025b](https://arxiv.org/html/2512.11933v1#bib.bib24)). They can also possibly “starve” emerging or legally unprotected groups by systematically withholding resources or opportunities in ways that current oversight tools, tuned to traditional protected classes, fail to spot (Grover, [1995](https://arxiv.org/html/2512.11933v1#bib.bib82)).
* •

  Increasing Ethics Issues: Emerging AI ethics problems are often harder to identify and address (Wachter, [2021](https://arxiv.org/html/2512.11933v1#bib.bib104); Barnes, [2020](https://arxiv.org/html/2512.11933v1#bib.bib8); et.al., [2014](https://arxiv.org/html/2512.11933v1#bib.bib38)).
* •

  Attacks and Safety: The growing variety and severity of attack vectors threaten the safety of current and future AI deployments (et.al., [2016a](https://arxiv.org/html/2512.11933v1#bib.bib37), [2019b](https://arxiv.org/html/2512.11933v1#bib.bib65), [2025c](https://arxiv.org/html/2512.11933v1#bib.bib30)).
* •

  Lack of Transparency: Generative AI models are inherently difficult to interpret and their complexity renders traditional explainability methods increasingly ineffective (G.Team, [2023](https://arxiv.org/html/2512.11933v1#bib.bib83)).

### 3.2. GenAI is a CAS

In the past decade, transformer models and Kaplan scaling (et.al., [2020b](https://arxiv.org/html/2512.11933v1#bib.bib50)) caused dramatic increases in AI model complexity, until recent scale-down trends (et.al., [2017c](https://arxiv.org/html/2512.11933v1#bib.bib74)). This resulted in unprecedented growth in both parameter count and architectural complexity (Howarth, [2025](https://arxiv.org/html/2512.11933v1#bib.bib88); GeminiTeam, [2023](https://arxiv.org/html/2512.11933v1#bib.bib80)). Models are now approaching the ten trillion parameter mark, with the number of parameters doubling every year since 2010 (Ed.Board, [2023](https://arxiv.org/html/2512.11933v1#bib.bib22)).

Generative and agentic AI systems exhibit hallmark features of complex systems (et.al., [2013](https://arxiv.org/html/2512.11933v1#bib.bib51)), including high-dimensional, nonlinear interactions among internal components such as attention heads and transformer layers, and emergent behaviors that appear as in-context learning and abrupt capability phase transitions. Similarly, they exhibit open-system characteristics, as GenAI model behavior is shaped by both internal architecture and dynamic external inputs. They have adaptive behaviors both during training phases through reinforcement learning (e.g. RLHF and RLAIF) as well as during agentic interactions with the environment.

Complex systems are fundamentally different from complicated systems (such as high-end computers), because they lack controllability, observability and mathematical modeling support ([Figure 1](https://arxiv.org/html/2512.11933v1#S3.F1 "In 3.3. Agentic AI and CAS Risks ‣ 3. Risks of AI in Financial Systems ‣ The Agentic Regulator: Risks for AI in Finance and a Proposed Agent-based Framework for Governance")), making them impossible to regulate or govern using traditional model risk management approaches. Complex system regulation (especially high-parameter systems) is an open problem. Ensuring safe autonomy and effective regulation is becoming a grand challenge for both GenAI and regulatory frameworks.

### 3.3. Agentic AI and CAS Risks

The autonomous objective optimization of Agentic AI systems has caused unpredictable, emergent, and potentially dangerous behaviors, especially in dynamic environments (Zhang, [2024](https://arxiv.org/html/2512.11933v1#bib.bib110); et.al., [2022d](https://arxiv.org/html/2512.11933v1#bib.bib60), [2016c](https://arxiv.org/html/2512.11933v1#bib.bib66)). Agentic AI exhibits critical vulnerabilities like reward hacking and specification gaming (et.al., [2022a](https://arxiv.org/html/2512.11933v1#bib.bib26)), and even leads to criminal behaviors like price collusion (et.al., [2023b](https://arxiv.org/html/2512.11933v1#bib.bib34), [2025f](https://arxiv.org/html/2512.11933v1#bib.bib71), [2022c](https://arxiv.org/html/2512.11933v1#bib.bib58)) and market manipulation (Mizuta, [2020](https://arxiv.org/html/2512.11933v1#bib.bib92); et.al., [2020e](https://arxiv.org/html/2512.11933v1#bib.bib73); Azzutti, [2022](https://arxiv.org/html/2512.11933v1#bib.bib6)) in financial use cases.

![Refer to caption](fig/Fig0.png)


Figure 1. Categorization of systems: Complex and Complicated system and theory differences (et.al., [2011](https://arxiv.org/html/2512.11933v1#bib.bib63))

In recent years, jail-breaking and its variants such as Best-of-N (et.al., [2024d](https://arxiv.org/html/2512.11933v1#bib.bib48)), prompt injections, backdoor attacks (et.al., [2020a](https://arxiv.org/html/2512.11933v1#bib.bib27)) and other AI-Takeover Attacks (AITO) have been reported (et.al., [2016a](https://arxiv.org/html/2512.11933v1#bib.bib37)). Guardrails and novel techniques have not been able to stop the rapidly growing list of AITO attacks.

Increased AI autonomy raises the risk of deceptive alignment, where a model hides its underlying misalignment, undermining even the most advanced model development and testing processes (et.al., [2023f](https://arxiv.org/html/2512.11933v1#bib.bib49)).

Though related to agentic hacks, emergent unethical behaviors are of special concern. Since the introduction of agency, AI has demonstrated the capacity to independently develop unethical strategies, including deception, lying and others (et.al., [2007](https://arxiv.org/html/2512.11933v1#bib.bib62), [2022e](https://arxiv.org/html/2512.11933v1#bib.bib67); Wired, [2023](https://arxiv.org/html/2512.11933v1#bib.bib107); The Guardian, [2024](https://arxiv.org/html/2512.11933v1#bib.bib102); et.al., [2024f](https://arxiv.org/html/2512.11933v1#bib.bib55), [2017b](https://arxiv.org/html/2512.11933v1#bib.bib70)).

![Refer to caption](fig/Fig2.png)


Figure 2. High-level framework for a hypothetical AI model: (i) Self-regulation blocks and (ii) Local governance and regulatory blocks. Block names are for illustration purposes.

## 4. Proposed Governance Framework

Previous sections made clear that the feedback loops and emergent behavior of generative and agentic AI are outpacing the linear, one-time validation controls that dominate current financial regulation. We now pivot from diagnosis to prescription. Drawing on insights from complex adaptive systems, we introduce a governance architecture that mirrors the decentralization and continual adaptation of the technologies it must oversee. Oversight functions are wrapped into modular, interoperable *regulatory blocks* that can be composed, upgraded, or retired without disrupting the whole. These blocks are grouped into four complementary governance layers:

* •

  Self-Regulation Capabilities (Hosted & Maintained by the Firm) — tightly integrated local modules that sit beside each model and enforce behavioral, ethical, and performance constraints within milliseconds.
* •

  Model Governance and In-House Regulation Capabilities (Hosted & Maintained by the Firm) — firm-managed blocks that guarantee jurisdiction- and application-specific compliance for every model, while supporting in-house regulatory tiers maintained in collaboration with supervisory agencies.
* •

  External Regulation Capabilities (Hosted & Maintained by Regulators) — regulator-hosted agents that ingest anonymized telemetry across institutions to detect systemic and network-level risks, including multi-party financial crimes (et.al., [2006](https://arxiv.org/html/2512.11933v1#bib.bib64), [2020f](https://arxiv.org/html/2512.11933v1#bib.bib75); Markham, [1988](https://arxiv.org/html/2512.11933v1#bib.bib90); et.al., [1991](https://arxiv.org/html/2512.11933v1#bib.bib33); Connor, [2007](https://arxiv.org/html/2512.11933v1#bib.bib19), [2014](https://arxiv.org/html/2512.11933v1#bib.bib20)).
* •

  Independent Audit (Hosted & Maintained by Independent Auditors) — third-party audit blocks that provide decentralized assurance and are critical for sustaining public trust and long-run AI safety.

Next we describe our design strategies, and these layers in turn. We begin with the principles that guide block construction.

### 4.1. Design Strategies

The proposed governance framework follows a set of design strategies that translate complex adaptive systems (CAS) principles into actionable, modular regulatory mechanisms for generative and agentic AI in finance. Each strategy targets a specific challenge ranging from real-time self-regulation at the model level to systemic risk monitoring across institutions, and aligns with one or more of the framework’s governance layers. In the subsections that follow, we detail eight such strategies, explaining their rationale and operational requirements.

###### Strategy 1.

Layered Functional Specialization of Regulatory Blocks

Although behavior in complex adaptive systems is emergent, assigning clear functional roles to distinct subsystems is an effective way to retain control. In our framework this principle translates into three specialized layers: (i) self-regulation blocks embedded at the model level, (ii) governance blocks that operate at the firm level, and (iii) regulation blocks that span the firm and supervisory levels. By separating these responsibilities, the framework gives risk teams and regulators precise levers for monitoring, intervention, and policy updates, as illustrated in [Figure 2](https://arxiv.org/html/2512.11933v1#S3.F2 "In 3.3. Agentic AI and CAS Risks ‣ 3. Risks of AI in Financial Systems ‣ The Agentic Regulator: Risks for AI in Finance and a Proposed Agent-based Framework for Governance").

###### Strategy 2.

Standardization of Components for Complexity

The use of standardization is a promising strategy to deal with complexity in CAS as well. Building libraries of specialized regulatory blocks tailored to each model’s application and jurisdiction, such as Equal Credit Opportunity Act (ECOA) blocks (Congress, [1974](https://arxiv.org/html/2512.11933v1#bib.bib15)) for mortgage or credit models, can help with AI regulation. These blocks (which can include AI agents) enable continuous compliance monitoring, real-time feedback, and enforcement, promoting a consistent regulatory framework across applications. Governance versions of the blocks are developed by the firms or vendors, and regulatory versions by the regulators.

It’s important to note that regulatory blocks cover the full agency spectrum from no-agency rule-based, hard-coded blocks, to limited agency and agentic blocks. Furthermore, agentic blocks cover a range of agency and can be configurable during run-time. Despite the flattened illustration in [Figure 2](https://arxiv.org/html/2512.11933v1#S3.F2 "In 3.3. Agentic AI and CAS Risks ‣ 3. Risks of AI in Financial Systems ‣ The Agentic Regulator: Risks for AI in Finance and a Proposed Agent-based Framework for Governance") interactions among blocks can be quite complex. However, these design specifications are expected to be optimized for each model, pursuant to regulatory needs and system goals such as safety and reliability.

Standard regulatory block libraries enable coverage across multiple regulation types:

(i) Data Regulation Blocks: Spectrum of regulatory blocks and agents for GDPR (European Union, [2018](https://arxiv.org/html/2512.11933v1#bib.bib77)), CCPA (State of CA, [2018](https://arxiv.org/html/2512.11933v1#bib.bib100)), RFPA (Congress, [1978](https://arxiv.org/html/2512.11933v1#bib.bib17)), etc.

(ii) AI Regulation Blocks: Blocks and agents for laws like the EU AI Act (E.U., [2024](https://arxiv.org/html/2512.11933v1#bib.bib76)) and Singapore AI regulations (of Singapore, [2020](https://arxiv.org/html/2512.11933v1#bib.bib95)).

(iii) Financial Regulation Blocks: Application- and jurisdiction-specific blocks and agents for ECOA (Congress, [1974](https://arxiv.org/html/2512.11933v1#bib.bib15)), HDMA (Congress, [1975](https://arxiv.org/html/2512.11933v1#bib.bib16)), BSA (Congress, [1970](https://arxiv.org/html/2512.11933v1#bib.bib14)), and regulatory guidelines from agencies like the Federal Reserve and OCC.

(iv) Local MRM Agents: Internal agents for firm-specific policies and model risk management rules. Standardization of blocks does not imply uniform blocks with similar characteristics. Regulatory blocks may have highly varying characteristics in terms of size, complexity, capabilities, architecture, autonomy, and interactivity. While some blocks may be simple rule-based systems, others may be complex agentic solutions with internal hierarchies and numerous components with specialized roles.

###### Strategy 3.

Modular Design for Change Management, Updates and Customizations

Modularity is an effective design strategy for adapting to dynamic environments, enabling faster deployment, lower costs, and faster entry into new markets or product lines.

As global AI and financial regulations expand, models must operate across diverse geographies and evolving regulatory landscapes. Capturing regional and temporal variations is complex, and rising AI development costs make region-specific models increasingly impractical. (a) Modular regulatory components enable updates and replacements without adding complexity to the core AI model, supporting third-party integration while reducing compliance and safety risks. (b) They can be used to train and update the models through reinforcement learning. This can be used for:

(i) Regulatory Changes: Agents covering both financial and AI regulations as well as changes to regulations;
(ii) Jurisdictions and Geographical Adoption: Agents customized for regions such as the U.S., European Union, China, etc.;
(iii) Firm-wide Policy Changes: Agents enforcing organization-specific policies and regulatory goals across all models, including third-party vendor models.

###### Strategy 4.

Adaptive System Components Managed by Local Control for Dynamic Environments

(i) System-wide Agency Adaption: System-level adaptiveness to autonomy allows adjusting for different environments and time periods. In high-risk, adversarial, client-facing, or dynamic environments, autonomy is constrained to enforce human-in-the-loop approvals, rule-based decisions, or supervisory control. Conversely, in low-risk, controlled in-house settings, higher levels of autonomy are permitted. The agentic adaption mechanisms include but not limited to: Decision-Making Autonomy based on task-specific risks, Goal Setting Autonomy for predefined goal specification constraints, and Response to Novel Situations allowing human intervention during abrupt changes.

(ii) Block-level Custom Agency Adaption: Adapting degrees of agency at the block level is essential to ensuring enhanced safety and trustworthiness of the overall system. This translates to a new system design and dynamic optimization problem to potentially improve overall characteristics.

(iii) Temporal Agency Adaption: Dynamic agency adjustment is required to address emerging safety and compliance concerns. As AI systems evolve, temporal agency control ensures continuous adaptation of the framework, optimizing each generation based on the capabilities of individual components and the evolving application context.

(iii) Human-in-the-Loop Adaption: Certain regulations, such as fair lending laws and KYC-AML rules, mandate human review for all or high-risk cases (e.g., U.S. ECOA (Congress, [1974](https://arxiv.org/html/2512.11933v1#bib.bib15)), BSA (Congress, [1970](https://arxiv.org/html/2512.11933v1#bib.bib14)), PATRIOT Act (Congress, [2001](https://arxiv.org/html/2512.11933v1#bib.bib18)), AMLD (Union, [2018](https://arxiv.org/html/2512.11933v1#bib.bib103))). Given the inherent safety risks of autonomous AI, human oversight and control over autonomy remains essential.

###### Strategy 5.

Decentralized Architecture to Improve System Safety and Reliability

As discussed earlier, all AI models have the underlying risk of AI Take-over attacks (AITO) and can be used to facilitate criminal and unethical acts (et.al., [2024d](https://arxiv.org/html/2512.11933v1#bib.bib48)). This risk dramatically increases alongside model autonomy, necessitating the decentralization of regulatory architecture. This can ensure the safety and robustness of the regulatory system and allow effective oversight, mitigation, and auditing. Integrating independent monitoring and regulatory hierarchies reduces risks linked to centralized hierarchical control and prevents vulnerabilities from the takeover of a limited set of regulatory blocks. Financial services heavily depend on a limited set of third-party and vendor models, making them particularly vulnerable to attacks on financial and regulator models.

As shown in [Figure 3](https://arxiv.org/html/2512.11933v1#S4.F3 "In 4.1. Design Strategies ‣ 4. Proposed Governance Framework ‣ The Agentic Regulator: Risks for AI in Finance and a Proposed Agent-based Framework for Governance"), independent regulatory blocks and agents including independent auditors and inspectors (et.al., [2020d](https://arxiv.org/html/2512.11933v1#bib.bib57), [2021b](https://arxiv.org/html/2512.11933v1#bib.bib53)) improve safety, which is especially vital for agentic AI given the increasing threat of takeover attacks (e.g. back-door attacks, hidden triggers (et.al., [2020c](https://arxiv.org/html/2512.11933v1#bib.bib52), [a](https://arxiv.org/html/2512.11933v1#bib.bib27); Guo, [2022](https://arxiv.org/html/2512.11933v1#bib.bib85))), emergent misaligned behaviors, and deceptive alignment challenges (et.al., [2018b](https://arxiv.org/html/2512.11933v1#bib.bib56)).

![Refer to caption](fig/Fig4.png)


Figure 3. Decentralization of financial AI regulation through numerous regulators and independent audit and regulatory blocks and agents

###### Strategy 6.

Diversity of System Components and Agency for Robustness

Structural heterogeneity is a well-known strategy that works in both general system design and complex adaptive systems theory. In the context of regulatory framework this translates to various aspects of the design:

(i) Heterogeneity of Autonomy: Heterogeneous autonomy levels (from rule-based blocks to agentic blocks with varying degrees of autonomy) is an important feature for robustness. Autonomy can be tailored for block level functions based on their risk levels, becoming a design parameter to optimize overall system robustness, controllability and safety.

(ii) Regulatory Heterogeneity: A single, centralized regulatory layer creates a point of failure and amplifies correlated vulnerabilities. In contrast, the framework disperses oversight across multiple, independently designed regulatory and audit blocks, each with its own control logic and data pathway. This structural diversity hardens the system against coordinated attacks and unexpected faults.

(iii) Block-level Heterogeneity: Heterogeneity of the architectural and behavioral characteristics as well as vendors at the block level also provides a mechanism to hedge against system-level takeover attacks.

###### Strategy 7.

Redundancy for Reliability, Fault-Tolerance and Safety

Incorporating redundant building blocks is an effective strategy for complex systems in dealing with the underlying reliability, robustness and safety issues. Not only does this strategy ensure fault-tolerance when one or more components of the system fail or are taken-over during an attack, it provides the ability to isolate and contain faulty or compromised blocks, regions or subsystems.

As the reliability of the building blocks (from the core models to the regulatory framework components) remain an issue, having optimized redundancy levels at different granularities and functional capabilities is highly important to (i)Block-level Checks that cross validate the individual block outputs, Anomaly Detection and Reporting to report abnormal behavior, and Safety Issues for detecting potential safety and security vulnerabilities and issues as they emerge. Additionally, redundancy also provides better performance in dynamic adversarial environments during functional failures as well.

### 4.2. Self-Regulation Within Agents

Self-regulation modules consist of embedded monitors, ethics filters and safety guards that are wired directly into the runtime of each generative or agentic model. Because they operate in the same execution context, they can intervene within milliseconds, a capability that is indispensable when trying to govern the highly unpredictable behavior of complex adaptive systems such as modern GenAI models. The challenge is amplified by the growing mix of in-house and vendor models whose trustworthiness, safety and reliability vary widely, creating a heterogeneous risk surface that traditional, centralized controls struggle to manage (et.al., [2022b](https://arxiv.org/html/2512.11933v1#bib.bib47); Christensen, [2021](https://arxiv.org/html/2512.11933v1#bib.bib12); Fernández, [2019](https://arxiv.org/html/2512.11933v1#bib.bib79); et.al., [2021a](https://arxiv.org/html/2512.11933v1#bib.bib41)). By imposing a common set of local controls, self-regulation blocks provide a uniform policy.

Each block delivers four tightly coupled functions. First, it performs core monitoring and regulation, supervising performance drift, data-quality anomalies and environmental changes, and throttling or quarantining the model when predefined bounds are breached. Second, it conducts ethics self-regulation, continuously inspecting inputs and outputs for fairness, bias, explainability and broader ethical compliance. Third, it enforces safety and security self-regulation by detecting prompt-injection, data-exfiltration and other unsafe behaviors, then invoking automated or human-in-the-loop responses. Finally, every intervention is written to an immutable audit log so that internal risk teams and external regulators can reconstruct events, assess control effectiveness and refine policies over time. Collectively, these capabilities make each model the first line of defense, aligning day-to-day operation with enterprise policy and statutory requirements long before risks can propagate to higher tiers of governance.

### 4.3. Firm-Level Governance Modules

Firm-level governance modules sit between local self-regulation blocks and external regulators, giving the institution an enterprise view of model behavior, risk posture, and compliance status. They ingest real-time telemetry from thousands of self-regulation modules such as latency metrics, ethics flags, security alerts, then fuse those signals with business context such as position limits, customer segmentation, and liquidity exposure. The resulting dashboards allow risk and compliance officers to spot correlated failures, trigger circuit breakers, or throttle model access when aggregate indicators breach predefined tolerances. Because these modules are hosted and maintained by the firm, they can enforce jurisdiction-specific requirements (for example, Europe’s AI Act or U.S. fair-lending rules) while still aligning with global policy frameworks such as SR 11-7 and Basel Principles (FED and OCC, [2011](https://arxiv.org/html/2512.11933v1#bib.bib78)). They also provide a single point of attestation for board governance committees, converting raw telemetry into evidence packages suitable for annual model-risk review.

Architecturally, each firm-level module exposes standard APIs, REST for data pulls, gRPC or message queues for event pushes, so that new models or vendor services can register without custom wiring. A rule engine or policy microservice translates high-level mandates (for example, maximum daily loss or bias thresholds) into machine-readable checks that propagate back down to self-regulation blocks. The same interface allows external regulators and independent auditors to query anonymized, aggregated metrics without breaching data-protection walls. By decoupling policy logic from individual models, the firm can roll out updated controls by hot-swapping container images or feature flags rather than redeploying every model. This design supports rapid iteration as legislative guidance evolves, while maintaining a continuous audit trail that links each control decision to the policy version in force at the time of execution.

### 4.4. External Regulatory & Audit Modules

External modules are hosted by supervisory agencies or accredited third-party auditors and operate at the sector or market level. They collect anonymized, aggregated telemetry streams and event logs from multiple firms, enrich those data with public market feeds, and apply anomaly-detection models to uncover collusive behavior, emerging concentration risk, or coordinated cyber threats that no single institution could observe in isolation. Each module publishes versioned policy APIs through which regulators can issue compulsory control updates, such as new bias thresholds or liquidity stress tests, that downstream governance layers must enforce. Cryptographically signed attestations and tamper-evident ledgers ensure that audit evidence remains verifiable while preserving firm confidentiality through differential privacy or secure multiparty computation techniques. By providing a neutral vantage point, these modules close the information gap between micro-prudential oversight and macro-prudential stability, and they furnish an independent assurance layer that strengthens public trust in the safety of AI-driven financial services.

## 5. Case Study: Emergent Unethical Behavior

To illustrate the potential of our modular regulatory framework, in this section we explore a specific set of problems in the literature, discuss potential solution components, and show how they might fit into the proposed framework.

### 5.1. Agentic Misbehavior in Financial Markets

Multiple lines of research have examined the disruptive behavior potential of intelligent trading agents in a financial market system. Spoofing, or the manipulation of market prices by placement of orders not intended for transaction, has been especially studied. Using the Market-Sim simulation (Wah et al., [2017](https://arxiv.org/html/2512.11933v1#bib.bib105)), a research group found that a generative order-placement model could not only learn to spoof its market, but to hide such behavior as legitimate market making (Wang and Wellman, [2020](https://arxiv.org/html/2512.11933v1#bib.bib106)). Other investigators, using the ABIDES simulation (Byrd et al., [2020](https://arxiv.org/html/2512.11933v1#bib.bib10)), found that a reinforcement learning (RL) based trader tasked with simple profit maximization, could discover and employ spoofing as a strategy so long as it could place and cancel limit orders. Scholars have also investigated the effect of spoofing on market efficiency and price discovery (Liu et al., [2022](https://arxiv.org/html/2512.11933v1#bib.bib89)) and of liquidity on spoofing (Gu et al., [2024](https://arxiv.org/html/2512.11933v1#bib.bib84)). Taken together, these studies have shown that agentic spoofing, inadvertent or otherwise, arises often and with a disruptive impact on other market participants, making markets less efficient, hampering price discovery, and increasing volatility.

### 5.2. Remediation Efforts

There have also been preliminary efforts to redress the discovery of spoofing as a profit-maximizing strategy by intelligent trading agents. Using the generative model discussed above (Wang and Wellman, [2020](https://arxiv.org/html/2512.11933v1#bib.bib106)), the investigators found that it was effectively countered by an adversarial discriminator tasked with spoofing detection. To evade detection, the generative model was forced to eventually become an honest market maker. For the RL based trader (Byrd, [2022](https://arxiv.org/html/2512.11933v1#bib.bib9)), the authors drew techniques from the field of Normative RL, applying reward shaping, policy shaping, and action reranking to the agent training process. These methods relied on an internal feedback mechanism, trained in simulation with known spoofing strategies, which discouraged selection of actions that produced a trajectory similar to spoofing, and were effective in significantly reducing the appearance of such behaviors.

![Refer to caption](x1.png)


Figure 4. Example of GenAI spoofing risk mitigation

### 5.3. Framework Incorporation

The results of these studies suggest components for inclusion into the proposed modular governance framework, illustrated in Figure [4](https://arxiv.org/html/2512.11933v1#S5.F4 "Figure 4 ‣ 5.2. Remediation Efforts ‣ 5. Case Study: Emergent Unethical Behavior ‣ The Agentic Regulator: Risks for AI in Finance and a Proposed Agent-based Framework for Governance"). Both the adversarial discriminator and the RL normative guidance component would make excellent *self-regulation* blocks, residing adjacent to their individual models. The feedback from these blocks could directly influence learned model behavior, improving model risk management. Generalized versions of the discriminator and the spoofing detector are candidates for *firm-level governance* blocks. Rather than providing direct model feedback, these could combine firm-wide order flow data to guard against distributed spoofing collusion among agents, which would be undetectable at a lower level. These could provide feedback to the firm before deployment during a formal model validation exercise or after deployment based on live market activity. Further variations of these components trained to recognize not only aggregated spoofing behavior signatures across firms, but also the aforementioned impacts on volatility, efficiency, and price discovery, might comprise *external regulatory* blocks, logging detected patterns and raising an audit flag for human investigation if the target behaviors are ongoing. These and other regulatory blocks can provide feedback independently or be wrapped into ensembles using meta-learning or mixture-of-experts approaches for more comprehensive surveillance and guidance.

### 5.4. Framework Benefit

This simple example discusses only one small area (emergent spoofing behavior in AI trading agents) of the vast governance space about to be challenged by rapid AI deployment. Given the scope of the issue and the pace of change, neither a traditional model nor a monolithic technical model of governance is likely to succeed. The modular framework is adaptable, responsive, and can grow and change alongside technical developments in the AI Finance space.

## 6. Further Capabilities

Here we outline additional capabilities of our modular framework that extend traditional governance: supporting consistent oversight, real-time monitoring, safety and security, end-to-end lifecycle management, and rigorous testing.

Consistent Regulatory Oversight: AI governance remains fragmented, with inconsistent standards, reactive scrutiny, and diverse implementations across firms. Standardizing tools and processes is critical to improving safety and compliance.

Our framework consolidates oversight through modular blocks that integrate third-party tools and firm-specific governance systems. This enables scalable, jurisdiction-aligned governance across diverse models and deployments.

Real-Time Monitoring & Regulation: Agentic AI requires continuous oversight due to adaptive, autonomous behavior. Our framework supports:

* •

  Core Model Monitoring: Tracks performance metrics often missing in existing tools (et.al., [2024a](https://arxiv.org/html/2512.11933v1#bib.bib29)).
* •

  Automated Reporting: Generates summaries and metrics for regulators and compliance.

  item Agentic Trust Monitoring: Evaluates metrics such as task success (et.al., [2025e](https://arxiv.org/html/2512.11933v1#bib.bib69)), error awareness (et.al, [2024](https://arxiv.org/html/2512.11933v1#bib.bib28)), stress robustness (Reddy, [2025](https://arxiv.org/html/2512.11933v1#bib.bib98)), consistency (AI, [2025a](https://arxiv.org/html/2512.11933v1#bib.bib2)), and harmful outputs (Cmarix, [2025](https://arxiv.org/html/2512.11933v1#bib.bib13)).

The framework supports independent safety and security agents:

* •

  Action monitoring for misuse;
* •

  Model safety for interaction threats;
* •

  Security oversight to detect attacks.

Lifecycle Governance: Lifecycle governance, is now a regulatory necessity (of China, [CAC](https://arxiv.org/html/2512.11933v1#bib.bib93)). Our framework supports oversight from development through deployment—covering training data, specifications, testing, RLHF risks, and profiling—via audit-ready reporting blocks aligned with policy requirements.

Rigorous testing is essential to uncover risks in complex models (et.al., [[n. d.]](https://arxiv.org/html/2512.11933v1#bib.bib35), [2023a](https://arxiv.org/html/2512.11933v1#bib.bib31)). Our framework enables:

* •

  Adversarial testing engines;
* •

  Expanded and multi-criteria evaluations;
* •

  Real-time stress testing akin to CCAR (Reserve, [2023](https://arxiv.org/html/2512.11933v1#bib.bib99));
* •

  Behavioral profiling and standardized AI test coverage.

Response to Rapid Advancement: Rabid model advancement (AI, [2025b](https://arxiv.org/html/2512.11933v1#bib.bib4); OpenAITeam, [2023](https://arxiv.org/html/2512.11933v1#bib.bib96); Anthropic, [2025](https://arxiv.org/html/2512.11933v1#bib.bib5); G.Team, [2023](https://arxiv.org/html/2512.11933v1#bib.bib83); AI, [2024](https://arxiv.org/html/2512.11933v1#bib.bib3); DeepMind, [2024](https://arxiv.org/html/2512.11933v1#bib.bib21)) challenges traditional oversight. Financial firms often deploy high-risk models without proper controls. Our layered regulatory architecture supports adaptive governance while minimizing risks tied to evolving model behavior and deployment speed.

## 7. Conclusions & Outlook

AI systems are now integral to financial services. As generative and agentic AI adoption grows, effective model governance is critical to ensure robustness and regulatory compliance. Model complexity and regulatory requirements have rendered traditional governance processes ineffective, intensifying concerns about reliability and trustworthiness.

As a high-parameter complex system, GenAI is upending traditional model risk management and regulatory frameworks. It leads to an open problem for AI regulation, which is strongly intertwined with other underlying challenges like alignment. Despite limited and inadequate regulatory oversight, generative AI solutions are being deployed at increasing rates, amplifying risks that require urgent and proactive mitigation.

This paper surveys the numerous challenges in regulating generative and agentic AI. It presents complex adaptive system strategies and a high-level hybrid framework for their integration as an agentic regulator. The framework aims to tackle the growing gaps in current model risk management and regulatory approaches while addressing complexity, agility, reliability and safety challenges as primary goals.

## References

* (1)
* AI (2025a)

  Galileo AI. 2025a.
  AI Agent Metrics- A Deep Dive.
* AI (2024)

  Mistral AI. 2024.
  Mistral.
* AI (2025b)

  Meta AI. 2025b.
  Llama 4.




  Accessed: 2025-04-09.
* Anthropic (2025)

  Anthropic. 2025.
  Claude 3.7 Sonnet.




  Accessed: 2025-04-30.
* Azzutti (2022)

  A. Azzutti. 2022.
  AI Trading and the Limits of EU Law Enforcement.
  *ScienceDirect* (2022).
* Balch and Arkin (1998)

  Tucker Balch and Ronald C. Arkin. 1998.
  Behavior-Based Formation Control for Multirobot Teams.
  *IEEE Transactions on Robotics and Automation* 14, 6 (1998), 926–939.

  <https://doi.org/10.1109/70.736776>
* Barnes (2020)

  P. Barnes. 2020.
  EPIC Asks FTC To Regulate Use Of AI.




  Accessed: 2025.
* Byrd (2022)

  David Byrd. 2022.
  Learning not to spoof. In *Proceedings of the Third ACM International Conference on AI in Finance*. 139–147.
* Byrd et al. (2020)

  David Byrd, Maria Hybinette, and Tucker Hybinette Balch. 2020.
  ABIDES: Towards high-fidelity multi-agent market simulation. In *Proceedings of the 2020 ACM SIGSIM Conference on Principles of Advanced Discrete Simulation*. 11–22.
* Canada (2024)

  ISED Canada. 2024.
  The AI and Data Act (AIDA).
  *Gov.of CA* (2024).
* Christensen (2021)

  J. Christensen. 2021.
  AI in financial services.
  In *Demystifying AI for Enterprise*. Prod. Press, 149–192.
* Cmarix (2025)

  Cmarix. 2025.
  AI Agent Evaluation.
* Congress (1970)

  U.S. Congress. 1970.
  Bank Secrecy Act (BSA).
* Congress (1974)

  US Congress. 1974.
  Equal Credit Opportunity Act.
  *U.S. Congress* 15 U.S.C. § 1691 et seq. (1974).
* Congress (1975)

  U.S. Congress. 1975.
  Home Mortgage Disclosure Act.
  *U.S. Congress* 12 U.S.C. § 2801 et seq. (1975).
* Congress (1978)

  U.S. Congress. 1978.
  Right to Financial Privacy Act.
  *U.S. Congress* 12 U.S.C. § 3401 et seq (1978).
* Congress (2001)

  U.S. Congress. 2001.
  USA PATRIOT Act.
* Connor (2007)

  J.M. Connor. 2007.
  *Global Price Fixing*. Vol. 2.
  Springer.
* Connor (2014)

  J. M. Connor. 2014.
  Big Bad Banks.
  *Journal of Competition Law and Economics* 10, 1 (2014), 105–132.
* DeepMind (2024)

  DeepMind. 2024.
  DeepSeek.
* Ed.Board (2023)

  Nature Ed.Board. 2023.
  Powerful AI models, and more.
  *Nature* (2023).
* et.al. (2025a)

  A. Belelieu et.al. 2025a.
  AI in Financial Services.
  *WEF* 2025 (2025).
* et.al. (2025b)

  A. Bhattacharyya et.al. 2025b.
  MRM for GenAI in financial institutions.
  *ArXiv:2503.15668* (2025).
* et.al. (2019a)

  A. Oprea et.al. 2019a.
  NeurIPS Wshop. on Robust AI in Fin. Serv.
* et.al. (2022a)

  A. Pan et.al. 2022a.
  The Effects of Reward Misspecification.
  *ArXiv:2201.03544* (2022).
* et.al. (2020a)

  A. Saha et.al. 2020a.
  Hidden trigger backdoor attacks. In *AAAI Conf*, Vol. 34. 11957–11965.
* et.al (2024)

  Abuelsaad T. et.al. 2024.
  Agent-E.
* et.al. (2024a)

  B.Abiyoke et.al. 2024a.
  Real-time financial monitoring systems.
* et.al. (2025c)

  B.C. Das et.al. 2025c.
  Security and privacy challenges of LLMs.
  *ACM Comp. Sur.* 57, 6 (2025), 1–39.
* et.al. (2023a)

  B. Hannon et.al. 2023a.
  A deep dive into adversarial testing of AI models. In *CSCE*. IEEE, 2645–2649.
* et.al. (2018a)

  C. Brummer et.al. 2018a.
  Fintech and the innovation trilemma.
* et.al. (1991)

  C. B. Jean et.al. 1991.
  The Profitability of Price Fixing.
  *Rev. of Econ. and Stat.* 73, 2 (1991), 309–317.
* et.al. (2023b)

  C. Chica et.al. 2023b.
  AI and Algorithmic Price Collusion in Two-Sided Markets.
  *arXiv* (2023).
* et.al. ([n. d.])

  C. Tao et.al. [n. d.].
  Testing and quality validation for AI software–perspectives, issues, and practices.
  *IEEE Access, 7, pp.120164-120175* ([n. d.]).
* et.al. (2024b)

  C. Xie et.al. 2024b.
  Can LLM agents simulate human trust behaviors?
  *Arxiv 2402.04559* (2024).
* et.al. (2016a)

  D. Amodei et.al. 2016a.
  Concrete problems in AI safety.
  *ArXiv:1606.06565* (2016).
* et.al. (2014)

  D. Boyd et.al. 2014.
  The Networked Nature of Alg. Discr.
  In *Data and Discr.*, Open Tech. Inst. (Ed.). Chapter 11, 53–57.
* et.al. (2024c)

  D. Rowlands et.al. 2024c.
  KPMG Global AI in Finance Report.
  *KPMG* 2024 (2024).
* et.al. (2017a)

  E. Clapprood et.al. 2017a.
  Model Risk Management.
  *Deloitte* (2017).
* et.al. (2021a)

  F.G. Ferreira et.al. 2021a.
  AI Applied to Stock Market Trading.
  *IEEE Access* 9, pp.30898-30917 (2021).
* et.al. (2023c)

  G. Azul et.al. 2023c.
  TimeGPT-1.
  *Arxiv 2310.03589* (2023).
* et.al. (2023d)

  H. Yang et.al. 2023d.
  FinGPT.
  *Arxiv 2306.06031* (2023).
* et.al. (2023e)

  I.O. Gallegos et.al. 2023e.
  Bias and fairness in large language models.
  *ArXiv:2309.00770* (2023).
* et.al. (2025d)

  I. Okpala et.al. 2025d.
  Agentic AI applied to tasks in fin. serv.
  *Arxiv:2502.05439.* (2025).
* et.al. (2016b)

  J. B. Heaton et.al. 2016b.
  Deep Learning in Finance.
  (2016).
  arXiv:1602.06561
* et.al. (2022b)

  J.K. Hentzen et.al. 2022b.
  AI in customer-facing financial services.
  *Int. J, of Bank Marketing* 40, 6 (2022), 1299–1336.
* et.al. (2024d)

  J. Hughes et.al. 2024d.
  Best-of-N jailbreaking.
  *Arxiv 2412.03556* (2024).
* et.al. (2023f)

  J. Jiu et.al. 2023f.
  AI alignment.
* et.al. (2020b)

  J. Kaplan et.al. 2020b.
  Scaling laws for neural language models.
  *Arxiv 2001.08361* (2020).
* et.al. (2013)

  J. Ladyman et.al. 2013.
  What is a complex system?
  *Eur. J. for Phil. of Sci.* 3 (2013), 33–67.
* et.al. (2020c)

  J. Lin et.al. 2020c.
  Composite backdoor attack for DNN by mixing existing benign features. In *ACM Conf. Comp. and Comm. Security*. ACM, 113–131.
* et.al. (2021b)

  J. Mökander et.al. 2021b.
  Ethics-based auditing to develop trustworthy AI.
  *Minds and Mach.* 31, 2 (2021), 323–327.
* et.al. (2024e)

  J. Schneider et.al. 2024e.
  Governance of GenAI for companies.
  *Arxiv* 2403.08802 (2024).
* et.al. (2024f)

  L. Cavanaugh et.al. 2024f.
  Regulatory Perspectives on Algorithmic Bias.
  *Casualty Actuarial Society* (2024).
* et.al. (2018b)

  M. Bogen et.al. 2018b.
  *An Examination of Hiring Algorithms, Equity and Bias*.
  Technical Report. Upturn.
* et.al. (2020d)

  M. Brundage et.al. 2020d.
  Toward trustworthy AI development.
  *ArXiv:2004.07213* (2020).
* et.al. (2022c)

  M. Banchio et.al. 2022c.
  AI and Spontaneous Collusion.
  *arXiv* (2022).
* et.al. (2023g)

  M. Duffourc et.al. 2023g.
  Privacy of personal data in the generative AI data lifecycle.
  *NYU Journal of IP Law* 13 (2023), 219.
* et.al. (2022d)

  M. Kampouridis et.al. 2022d.
  Multi-agent systems for Comp. Econ and Fin.
  *AI Communications* 35, 4 (2022), 369–380.
* et.al. (2024g)

  P. Weber et.al. 2024g.
  Appl. of Explainable AI in Finance.
  *Man. Rev. Qrt.* 74, 2 (2024), 867–907.
* et.al. (2007)

  P. ÓBroin et.al. 2007.
  An Evol. App. to Deception in Multi-Agent Sys.
  *AI Rev.* 27, 4 (2007), 257–271.
* et.al. (2011)

  Q. Telesford et.al. 2011.
  The Brain as a Complex System.
  *Brain Connect. 2011 Oct;1(4):295–308* (2011).
* et.al. (2006)

  R.K. Aggarwal et.al. 2006.
  Stock Market Manipulations.
  *The J. of Business* 79, 4 (2006), 1915–1953.
* et.al. (2019b)

  R. Challen et.al. 2019b.
  AI bias and clinical safety.
  *BMJ Quality Safety* 28, 3 (2019), 231–237.
* et.al. (2016c)

  Silver et.al. 2016c.
  Mastering the game of Go.
  *Nature* 529(7587), 484–489 (2016).
* et.al. (2022e)

  S. Trewin et.al. 2022e.
  Algorithmic Discrimination Against People with Disabilities.
  *arXiv 2206.06149* (2022).
* et.al. (2023h)

  S. Wu et.al. 2023h.
  BloombergGPT.
  *Arxiv 2303.17564* (2023).
* et.al. (2025e)

  T.Kwa et.al. 2025e.
  Measuring AI Ability to Complete Long Tasks.
* et.al. (2017b)

  T.Z. Leibo et.al. 2017b.
  Multi-Agent RL in Sequential Social Dilemmas. In *AAMAS ’17*. 464–473.
* et.al. (2025f)

  W. Dou et.al. 2025f.
  AI-Powered Trading, Alg. Collusion, and Price Eff.
  *Wharton Res. Paper* (2025).
* et.al. (2021c)

  X. Ferrer et.al. 2021c.
  Bias and discrimination in AI.
  *IEEE Tech. and Soc. Magazine, 40(2), pp.72-80* (2021).
* et.al. (2020e)

  X. Wang et.al. 2020e.
  Market Manipulation. In *IJCAI, pp. 4626-4632*.
* et.al. (2017c)

  Y. Cheng et.al. 2017c.
  A Survey of Model Compression and Acceleration for Deep Neural Networks.
* et.al. (2020f)

  Á.Cartea et.al. 2020f.
  Spoofing and Price Manipulation in Order-Driven Markets.
  *App. Math. Fin.* 27, 1-2 (2020), 67–98.
* E.U. (2024)

  E.U. 2024.
  Reg 2024/1689 of E.U. Parliament and Councl.
  *Off. Jour. of E.U.* 2024/1689 (2024).
* European Union (2018)

  European Union. 2018.
  GDPR, OJ L 119, 04.05.2016; cor. OJ L 127, 23.5.2018.
* FED and OCC (2011)

  FED and OCC. 2011.
  Supervisory Guidance on MRM.
* Fernández (2019)

  A. Fernández. 2019.
  AI in financial services.
  *Banco de Espana* 3 (2019), 19.
* GeminiTeam (2023)

  GeminiTeam. 2023.
  Gemini.
  *Arxiv 2312.11805* (2023).
* Grattafiori (2024)

  A. et.al. Grattafiori. 2024.
  The Llama 3 herd of models.
  *Arxiv 2407.21783* (2024).
* Grover (1995)

  S. Grover. 1995.
  The Bus. Necessity Defense in Disparate Impact Discr.
  *GA Law Review* 30 (1995), 387–430.
* G.Team (2023)

  G.Team. 2023.
  Gemini.
  *ArXiv:2312.11805* (2023).
* Gu et al. (2024)

  Anri Gu, Yongzhao Wang, Chris Mascioli, Mithun Chakraborty, Rahul Savani, Theodore L Turocy, and Michael P Wellman. 2024.
  The Effect of Liquidity on the Spoofability of Financial Markets. In *Proceedings of the 5th ACM International Conference on AI in Finance*. 239–247.
* Guo (2022)

  W. Guo. 2022.
  An overview of backdoor attacks against DNNs.
  *IEEE Open J. of Sig. Proc.* 3 (2022), 261–287.
* Holland (1992)

  John H Holland. 1992.
  Complex adaptive systems.
  *Daedalus* 121, 1 (1992), 17–30.
* House (2023)

  The White House. 2023.
  Exec, Order on Safe, Secure, and Trustworthy AI.
  *US White House* (2023).
* Howarth (2025)

  J. Howarth. 2025.
  Num. of Param. in GPT-4.
  *Exploding Topics* (2025).
* Liu et al. (2022)

  Buhong Liu, Maria Polukarov, Carmine Ventre, Lingbo Li, Leslie Kanthan, Fan Wu, and Michail Basios. 2022.
  The spoofing resistance of frequent call markets. In *Proceedings of the 21st International Conference on Autonomous Agents and Multiagent Systems*. 825–832.
* Markham (1988)

  J. W. Markham. 1988.
  Front-Running—Insider Trading Under the Commodity Exchange Act.
  *Cat. Univ. Law Review* 38 (1988), 69.
* METI (2024)

  METI. 2024.
  Japan’s AI Imp. Guid. (2024).
  *METI* (2024).
* Mizuta (2020)

  T. Mizuta. 2020.
  Does an AI Perform Market Manipulation?
  *arXiv* (2020).
* of China  (CAC)

  Cyberspace Administration of China (CAC). 2023.
  The Inter. Meas, for the Man, of GenAI Services.
  *CAC* (2023).
* of Industry Science and Resources (2024)

  Department of Industry Science and Resources. 2024.
  Australia’s AIe Ethics Principles.
  *DIsR* (2024).
* of Singapore (2020)

  PDPC of Singapore. 2020.
  AI Gov. Framework.
  *Release 2020* (2020).
* OpenAITeam (2023)

  OpenAITeam. 2023.
  GPT-4 technical report.
  *Arxiv 2303.08774* (2023).
* Park (2024)

  T. Park. 2024.
  Enhancing anomaly detection with an llm-based multi-agent.
  *ArXiv:2403.19735* (2024).
* Reddy (2025)

  L. Reddy. 2025.
  AI Agent Evaluation Framework.
* Reserve (2023)

  Federal Reserve. 2023.
  Comprehensive Capital Analysis and Review (CCAR).
* State of CA (2018)

  State of CA. 2018.
  TITLE 1.81.5. CA Consumer Privacy Act of 2018.
* Survey (2024)

  Google Cloud Survey. 2024.
  Cashing in on AI.
* The Guardian (2024)

  The Guardian. 2024.
  Experts Warn Over Bias in AI.
* Union (2018)

  European Union. 2018.
  E.U. Anti-Money Laundering Directives (AMLD).
* Wachter (2021)

  S. Wachter. 2021.
  Affinity Profiling and Discr. By Association.
  *Berkeley Techn Law Jour.* 35, 2 (2021), 367–430.
* Wah et al. (2017)

  Elaine Wah, Mason Wright, and Michael P Wellman. 2017.
  Welfare effects of market making in continuous double auctions.
  *Journal of Artificial Intelligence Research* 59 (2017), 613–650.
* Wang and Wellman (2020)

  Xintong Wang and Michael P Wellman. 2020.
  Market manipulation: An adversarial learning framework for detection and evasion. In *29th International Joint Conference on Artificial Intelligence*.
* Wired (2023)

  Wired. 2023.
  AI Is Spreading Stereotypes.
* Y (2023)

  Shavit et.al. Y. 2023.
  Practices for governing agentic AI systems.
  *OpenAI* (2023).
* Zeff (2025)

  M. Zeff. 2025.
  OpenAI’s new AI models hallucinate more.
  *TechCrunch.com April 18th* (2025).
* Zhang (2024)

  C. Zhang. 2024.
  When AI meets finance.
  *ArXiv* (2024).