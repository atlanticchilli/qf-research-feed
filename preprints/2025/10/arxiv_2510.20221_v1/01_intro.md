---
authors:
- Alejandro Michel
- Abhinav Arun
- Bhaskarjit Sarmah
- Stefano Pasquali
doc_id: arxiv:2510.20221v1
family_id: arxiv:2510.20221
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'FinCARE: Financial Causal Analysis with Reasoning and Evidence'
url_abs: http://arxiv.org/abs/2510.20221v1
url_html: https://arxiv.org/html/2510.20221v1
venue: arXiv q-fin
version: 1
year: 2025
---


Alejandro Michel
  
Domyn
  
New York, US
  
alejandro.zuniga@domyn.com
  
&Abhinav Arun
  
Domyn
  
New York, US
  
abhinav.arun@domyn.com
  
&Bhaskarjit Sarmah
  
Domyn
  
Gurgaon, India
  
bhaskarjit.sarmah@domyn.com
  
&Stefano Pasquali
  
Domyn
  
New York, US
  
stefano.pasquali@domyn.com

###### Abstract

Portfolio managers rely on correlation-based analysis and heuristic methods that fail to capture true causal relationships driving performance. We present a hybrid framework that integrates statistical causal discovery algorithms with domain knowledge from two complementary sources: a financial knowledge graph extracted from SEC 10-K filings and large language model reasoning. Our approach systematically enhances three representative causal discovery paradigms, constraint-based (PC), score-based (GES), and continuous optimization (NOTEARS), by encoding knowledge graph constraints algorithmically and leveraging LLM conceptual reasoning for hypothesis generation. Evaluated on a synthetic financial dataset of 500 firms across 18 variables, our KG+LLM-enhanced methods demonstrate consistent improvements across all three algorithms: PC (F1: 0.622 vs. 0.459 baseline, +36%), GES (F1: 0.735 vs. 0.367, +100%), and NOTEARS (F1: 0.759 vs. 0.163, +366%). The framework enables reliable scenario analysis with mean absolute error of 0.003610 for counterfactual predictions and perfect directional accuracy for intervention effects. It also addresses critical limitations of existing methods by grounding statistical discoveries in financial domain expertise while maintaining empirical validation, providing portfolio managers with the causal foundation necessary for proactive risk management and strategic decision-making in dynamic market environments.

## 1 Introduction & Motivation

Portfolio and risk managers face an increasingly complex challenge: understanding causal mechanisms driving portfolio performance. Current practice relies on heuristic methods and correlation-based analysis; asset managers use experience-based rules, correlation matrices, and traditional factor models that fail to capture causal directionality[[1](https://arxiv.org/html/2510.20221v1#bib.bib1), [2](https://arxiv.org/html/2510.20221v1#bib.bib2), [3](https://arxiv.org/html/2510.20221v1#bib.bib3), [4](https://arxiv.org/html/2510.20221v1#bib.bib4)]. Traditional factor models remain fundamentally descriptive, lacking the scientific grounding necessary to distinguish genuine causal factors from spurious correlations[[5](https://arxiv.org/html/2510.20221v1#bib.bib5), [6](https://arxiv.org/html/2510.20221v1#bib.bib6)]. While statistical methods miss theoretically established relationships, knowledge graphs lack empirical validation, and LLMs suffer from the "causal parrot" problem [[7](https://arxiv.org/html/2510.20221v1#bib.bib7), [8](https://arxiv.org/html/2510.20221v1#bib.bib8), [9](https://arxiv.org/html/2510.20221v1#bib.bib9)]. Recent empirical studies demonstrate that state-of-the-art LLMs exhibit primarily associative behavior on novel causal questions, lacking the flexible reasoning capabilities required for genuine causal inference [[8](https://arxiv.org/html/2510.20221v1#bib.bib8), [10](https://arxiv.org/html/2510.20221v1#bib.bib10)]. We present a hybrid framework integrating statistical causal discovery, a financial knowledge graph from SEC filings, and LLM reasoning. Our contributions include: (1) Algorithmic integration of statistical causal discovery with knowledge graph constraints and LLM reasoning while maintaining DAG properties. (2) Substantial improvements across all algorithms: PC (+36% F1), GES (+100%), and NOTEARS (+366%). (3) Reliable counterfactual predictions (MAE: 0.003610) with perfect directional accuracy for interventions, enabling proactive causal analysis for portfolio management.

## 2 Related Work

Causal discovery in finance has evolved with large language models (LLMs). Traditional statistical methods face scalability limitations and the curse of dimensionality. [[11](https://arxiv.org/html/2510.20221v1#bib.bib11)] presented CausalStock, employing functional causal models with lag-dependent temporal discovery for news-driven stock prediction across multiple international markets. [[12](https://arxiv.org/html/2510.20221v1#bib.bib12)] proposed an end-to-end framework leveraging GPT-4 for automated DAG construction, handling hundreds of features through hierarchical clustering. However, this raises the "causal parrot" problem, generating plausible relationships without true understanding [[13](https://arxiv.org/html/2510.20221v1#bib.bib13)]. [[14](https://arxiv.org/html/2510.20221v1#bib.bib14)] addresses this through specialized LLM agents that iteratively refine causal graphs through debate and validation. [[15](https://arxiv.org/html/2510.20221v1#bib.bib15)] validates these theoretical frameworks in practice, showing that neither pure statistical nor pure LLM methods alone suffice for financial causal discovery. The emergence of autonomous causal analysis agents [[16](https://arxiv.org/html/2510.20221v1#bib.bib16), [17](https://arxiv.org/html/2510.20221v1#bib.bib17)] further advances the field by providing agents with causal analysis tools and postprocessing modules for DAG tuning, demonstrating how LLMs can serve as decision-making engines for algorithm selection and hyperparameter optimization. Recent hybrid approaches [[18](https://arxiv.org/html/2510.20221v1#bib.bib18)] demonstrate that combining constraint-based
and functional causal modeling can achieve superior accuracy compared to pure methods,
particularly for sparse causal graphs.

Knowledge graph approaches provide structured causal representations, from hyper-relational graphs [[19](https://arxiv.org/html/2510.20221v1#bib.bib19), [20](https://arxiv.org/html/2510.20221v1#bib.bib20)] to text extraction methods [[21](https://arxiv.org/html/2510.20221v1#bib.bib21), [22](https://arxiv.org/html/2510.20221v1#bib.bib22), [23](https://arxiv.org/html/2510.20221v1#bib.bib23)]. Recent work has advanced automated KG construction from financial documents; [[24](https://arxiv.org/html/2510.20221v1#bib.bib24)] proposed FinDKG, using fine-tuned LLMs with template-guided extraction to construct dual-structured KGs from financial news. [[25](https://arxiv.org/html/2510.20221v1#bib.bib25)] extended this with FinKario, demonstrating automated schema construction from equity research reports without predefined domain knowledge. The current frontier fuses LLMs with KGs; [[26](https://arxiv.org/html/2510.20221v1#bib.bib26)]’s RC2R framework grounds LLM reasoning in financial KGs through multi-scale contrastive learning, providing rigorous validation via interventional reasoning. Our work leverages FinReflectKG [[27](https://arxiv.org/html/2510.20221v1#bib.bib27)], a KG extracted from SEC 10-K filings using an iterative reflection-driven agentic framework, achieving a 64.8% compliance score (53.2% more compared to non-agentic single pass approach). With 227 causal relationships and explicit causal relations (Positively\_Impacts, Negatively\_Impacts, Affects\_Stock), the financial knowledge graph provides domain-grounded priors for our causal discovery pipeline.

## 3 Knowledge Graph Integration

To incorporate domain knowledge into the causal discovery process, we extracted causal relationships from SEC 10-K filings using a structured LLM-based approach.

This approach is largely inspired by the work done in FinReflectKG, which leverages a comprehensive, business-driven schema. The schema includes 24 categories for entity types (e.g. ORG, PERSON, COMP, etc.) and 27 categories for relationship types (e.g. Has\_Stake\_In, Complies\_With, Invests\_In, etc.). FinReflectKG contains causal relationships as well (e.g. Positively\_Impacts, Negatively\_Impacts, Affects\_Stock, etc.). With FinReflectKG providing useful contextual information about corporate operations and background knowledge, we wanted to further extend these insights to include explicit cause-effect relationships with clear directionality. Hence, we included the development of a specialized causal extraction prompt designed specifically to identify and structure causal relationships from 10-K filings (see Appendix C). This process yielded over 3,000 causal triplets.

## 4 Statistical Causal Discovery with Knowledge Graph Constraints

We evaluate three representative algorithms spanning the major paradigms in causal discovery: constraint-based (PC), score-based (GES), and continuous optimization (NOTEARS). This selection ensures our KG-enhancement approach demonstrates generality across fundamentally different discovery strategies rather than being method-specific. Each algorithm integrates KG constraints through paradigm-appropriate mechanisms.

### 4.1 Knowledge Graph Constraint Formulation

Before describing algorithm-specific integration mechanisms, we formalize how knowledge graph constraints are extracted from 10-K triplets and quantified. Each potential edge (u,v)(u,v) receives a composite score aggregating three evidence dimensions: strength (confidence labels), frequency (mention count), and coverage (number of companies), which uses the geometric mean:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CompositeScore​(u→v)=(Sstrength⋅Sfreq⋅Scov)1/3\text{CompositeScore}(u\to v)=(S\_{\text{strength}}\cdot S\_{\text{freq}}\cdot S\_{\text{cov}})^{1/3} |  | (1) |

where SstrengthS\_{\text{strength}} weights strong and moderate confidence mentions, SfreqS\_{\text{freq}} normalizes by maximum mentions, and ScovS\_{\text{cov}} normalizes by company coverage (see Appendix B for detailed formulations)

Edges are then classified based on composite scores and domain heuristics. High-confidence edges (CompositeScore >> 0.4, and mentioned in >> 18 companies) become required edges ℰreq\mathcal{E}\_{\text{req}}, while low-confidence or rare edges (<< 5 mentions) become forbidden edges ℰforb\mathcal{E}\_{\text{forb}}. This classification enables a flexible weighting scheme:

Edge Weights w:𝒱×𝒱→ℝw:\mathcal{V}\times\mathcal{V}\to\mathbb{R}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | w​(u,v)={+2.0if ​(u,v)∈ℰreq−2.0if ​(u,v)∈ℰforbCompositeScore​(u→v)if ​(u,v)∈KG but neither required nor forbidden0.0otherwisew(u,v)=\begin{cases}+2.0&\text{if }(u,v)\in\mathcal{E}\_{\text{req}}\\ -2.0&\text{if }(u,v)\in\mathcal{E}\_{\text{forb}}\\ \text{CompositeScore}(u\to v)&\text{if }(u,v)\in\text{KG but neither required nor forbidden}\\ 0.0&\text{otherwise}\end{cases} |  | (2) |

This encoding allows algorithms to treat KG constraints as soft priors (values in [0,1]) or hard constraints (+/-2.0 for required/forbidden), depending on the algorithmic paradigm.

### 4.2 PC Algorithm: Constraint-Based Discovery

The PC algorithm represents the constraint-based paradigm, discovering causal structure purely through conditional independence testing [[28](https://arxiv.org/html/2510.20221v1#bib.bib28), [29](https://arxiv.org/html/2510.20221v1#bib.bib29)]. This makes it theoretically sound with minimal parametric assumptions, but also makes it vulnerable to two key failure modes that KG integration addresses: (1) Removing edges with weak statistical signals despite strong domain support (2) Arbitrary edge orientation when independence tests provide insufficient information.

To address these limitations, KG-required edges (ℰreq\mathcal{E}\_{\text{req}} bypass conditional independence testing entirely, while other edges receive adaptive significance thresholds: αadj​(vi,vj)=α⋅exp⁡(−w​(vi,vj))\alpha\_{\text{adj}}(v\_{i},v\_{j})=\alpha\cdot\exp\left(-w(v\_{i},v\_{j})\right). This makes the algorithm conservative about removing KG-supported edges (e.g., an edge with weight 0.2 requires p < 0.12 for removal, versus an edge with weight 0.8 requires p < 0.067).
Edge orientation uses KG directional preferences when |wi​j−wj​i|>0.2|w\_{ij}-w\_{ji}|>0.2, resolving ambiguity in constraint-based methods. Based on our sensitivity testing, we use α\alpha = 0.15. See Appendix A for algorithm details.

### 4.3 GES Algorithm: Score-Based Discovery

Greedy Equivalence Search (GES) discovers causal structure by optimizing Bayesian Information Criterion (BIC) through local graph modifications, alternating between forward (edge addition) and backward (edge deletion) search phases[[30](https://arxiv.org/html/2510.20221v1#bib.bib30)]. Unlike PC’s independence-testing approach, GES is a score-based method that explicitly trades off data fit against model complexity.

The natural integration point for KG constraints in score-based methods is through scoring function modification. We augment BIC with domain-informed bonuses and penalties that shift the optimization landscape toward theoretically plausible structures without abandoning data fit.

The standard BIC score is modified to incorporate KG structural priors:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ScoreKG​(G)=BIC​(G)+λkg⋅RKG​(G)\text{Score}\_{\text{KG}}(G)=\text{BIC}(G)+\lambda\_{\text{kg}}\cdot R\_{\text{KG}}(G) |  | (3) |

where RKG​(G)R\_{\text{KG}}(G) is the KG regularization term.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | RKG​(G)\displaystyle R\_{\text{KG}}(G) | =wreq⋅∑(u,v)∈ℰreq𝕀​[(u,v)∈G]⋅w​(u,v)\displaystyle=w\_{\text{req}}\cdot\sum\_{(u,v)\in\mathcal{E}\_{\text{req}}}\mathbb{I}[(u,v)\in G]\cdot w(u,v) |  | (4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −wforb⋅∑(u,v)∈ℰforb𝕀​[(u,v)∈G]⋅10.0\displaystyle\quad-w\_{\text{forb}}\cdot\sum\_{(u,v)\in\mathcal{E}\_{\text{forb}}}\mathbb{I}[(u,v)\in G]\cdot 10.0 |  | (5) |

with hyperparameters λkg=10.0\lambda\_{\text{kg}}=10.0, wreq=5.0w\_{\text{req}}=5.0, and wforb=20.0w\_{\text{forb}}=20.0

This means that each KG-required edge included in the graph contributes +50 to the score (10.0 ×\times 5.0 ×\times typical w(u,v)), approximately equivalent to improving BIC by 50 points. This makes including domain-supported edges as valuable as finding a substantially better statistical fit. Conversely, each forbidden edge incurs a -200 penalty, effectively prohibiting them unless data evidence is overwhelming.

The modified scoring function acts as a "soft constraint" mechanism because it does not prohibit or require edges (except for forbidden edges), but rather shifts the optimization landscape. If statistical evidence strongly contradicts a required edge, GES can still exclude it, but the algorithm must find a substantially better alternative to overcome the KG bonus. This maintains flexibility while leveraging domain knowledge. See Appendix A for algorithm details.

### 4.4 NOTEARS Algorithm: Continuous Optimization

NOTEARS (Non-combinatorial Optimization via Trace Exponential and Augmented lagRangian for Structure learning) represents a fundamentally different approach: it reformulates discrete DAG structure learning as continuous optimization with a differentiable acyclicity constraint[[31](https://arxiv.org/html/2510.20221v1#bib.bib31)]. Rather than searching through discrete graph space like PC and GES, NOTEARS learns a weighted adjacency matrix W∈ℝd×dW\in\mathbb{R}^{d\times d} through gradient-based optimization.

The integration of KG constraints in NOTEARS occurs through three mechanisms operating at different stages of the optimization and post-processing pipeline. Unlike PC’s hard constraints or GES’s score modification, NOTEARS uses a multi-level approach combining regularization, post-hoc enforcement, and adaptive thresholding. See Appendix A for algorithm details.

## 5 Statistical Causal Discovery with LLMs

While Section 4 detailed how knowledge graph constraints guide causal discovery through extracted 10-K relationships, LLMs offer an alternative source of domain knowledge: reasoning from innate understanding of financial mechanisms. Recent advances in LLM-augmented causal discovery demonstrate the effectiveness of combining statistical methods with LLM reasoning [[32](https://arxiv.org/html/2510.20221v1#bib.bib32), [33](https://arxiv.org/html/2510.20221v1#bib.bib33)], showing that autonomous systems leveraging both data-driven algorithms and LLM knowledge can outperform conventional approaches on benchmark datasets. The algorithmic integration mechanisms remain identical, the only difference lies in edge provenance.

We implement LLM enhancement using Qwen3-235B-A22B model with thinking mode enabled. Rather than extracting causal relationships from documents, we employ a single reasoning module, MissingEdgeDiscoverer, that generates edge proposals through conceptual reasoning about financial causality (see Appendix C for prompt).

These LLM-generated proposals integrate into PC, GES, and NOTEARS using the exact same mechanisms described in Section 4, with one key substitution: LLM confidence scores replace knowledge graph composite scores as edge weights w​(u,v)w(u,v). Both KG and LLM enhancements provide soft prior beliefs about edge existence and direction, differing only in their knowledge source. This unified framework enables clean comparison between document-extracted knowledge (KG), model-internalized knowledge (LLM), and their combination (KG+LLM).

## 6 Experiments

### 6.1 Benchmark Dataset

To benchmark our performance, we developed a realistic synthetic dataset that captures the complex causal relationships present in corporate finance and risk management. The data is created with known causal structures and a ground truth DAG, allowing us to quantitatively measure causal discovery performance through precision, recall, and F1-scores. See Appendix D for data generation details. Our KG demonstrated strong coverage of the ground truth causal structure, capturing 23 of 29 ground truth edges.

### 6.2 Causal Graph Recovery

We evaluate our framework on the synthetic financial dataset of 500 firms across 18 variables with a known ground truth DAG containing 29 edges. We compare four classes of methods: (1) Baseline statistical algorithms without enhancement, (2) KG-Enhanced methods integrating knowledge graph constraints algorithmically, (3) LLM-Only methods using language model reasoning without KG constraints, and (4) KG+LLM methods combining both knowledge graph constraints and LLM reasoning. Each approach is tested across three causal discovery paradigms: constraint-based (PC), score-based (GES), and continuous optimization (NOTEARS).

![Refer to caption](cluster-f1.jpg)

Figure 1: Graph Recovery Performance Across All Methods (±\pm1 standard deviation)

Table 1 presents comprehensive graph recovery metrics across all methods. To ensure robustness, we report mean performance with standard deviations from 5 independent runs for LLM-enhanced methods (KG+LLM and LLM-Only), while baseline and KG-only methods show deterministic single-run results.

Our results demonstrate clear and consistent performance gains from integrating both knowledge graph constraints and LLM reasoning. In all cases, enhancing any of the three causal algorithms with any of the three strategies (KG-only, LLM-only, or both) led to improvements in graph recovery. In all cases, the best improvement comes when combining KG constraints with LLM reasoning.

![Refer to caption](graph-recovery.jpg)

Figure 2: Causal Graph Recovery Comparison: Baseline vs. KG+LLM vs. Ground Truth

Figure 2 illustrates the progression in causal graph recovery from baseline to our hybrid approach. Baseline NOTEARS (left panel) recovers only 4 of 29 ground truth edges (F1=0.163) while KG+LLM-NOTEARS (center panel) achieves near-complete recovery with 26 of 29 edges correctly identified (F1=0.759), capturing the full complexity of financial causal mechanisms.

### 6.3 LLM Enhancement Analysis

So far in our experiments, we have employed the MissingEdgeDiscoverer module as our sole LLM reasoning component. A natural question arises: could we achieve even better performance by expanding our LLM reasoning capabilities? Specifically, we investigate two enhancement strategies: (1) adding additional specialized reasoning modules, and (2) incorporating knowledge graph information directly into LLM prompts. In the following experiments, we only evalaute using NOTEARS.

#### 6.3.1 Knowledge Graph Prompt Integration

To rigorously test whether additional LLM reasoning provides value, we design a full system comprising five specialized modules, each targeting different aspects of causal discovery (see Appendix C for prompts):

* •

  MissingEdgeDiscoverer (already in our system): Generates targeted hypotheses for 2-3 high-value outcome variables (e.g., Monthly\_Return).
* •

  DataPatternAnalyzer: Examines distributions, correlations, and sector dependencies to identify patterns statistical methods may overlook.
* •

  KGRelationshipValidator: Validates all 11 KG required and 119 forbidden edges by listing them directly in prompts.
* •

  GraphStructureRefiner: Proposes specific edge modifications based on graph structural properties.
* •

  DomainExpertReasoner: Generates hypotheses from general financial theory without constraint to specific variables.

We adopt a leave-one-out ablation approach, systematically disabling each module while keeping others active. To account for LLM output variation, we run each configuration 5 times and report mean performance with standard deviations. Changes smaller than 1σ\sigma cannot be distinguished from random LLM variation.

![Refer to caption](ablation.jpg)

Figure 3: Leave-One-Out Ablation Analysis of LLM Reasoning Modules on Graph Recovery

Figure 3 shows the impact of removing each module. Only MissingEdgeDiscoverer demonstrates statistically meaningful contribution: its removal causes -0.076±\pm0.018 decrease in F1-score (1.95σ\sigma deviation). The remaining four modules show changes within natural LLM variation, indicating negligible impact on causal DAG recovery.

The minimal impact of KGRelationshipValidator is particularly instructive. Despite explicitly listing all 11 required and 119 forbidden KG edges in its prompt, removing this module had no significant effect. This suggests that injecting KG information directly into LLM prompts is ineffective compared to encoding KG constraints algorithmically in the optimization objective.

These findings indicate: (1) a single focused agent outperforms multi-agent approaches for graph recovery, and (2) the optimal strategy combines algorithmic KG constraints with separate LLM-based conceptual reasoning.

### 6.4 Counterfactual Estimation

Counterfactual reasoning in causal models follows the formal framework of structural causal models (SCMs) and Pearl’s do-calculus[[34](https://arxiv.org/html/2510.20221v1#bib.bib34), [35](https://arxiv.org/html/2510.20221v1#bib.bib35)], which distinguishes between observational distributions P​(Y∣X)P(Y\mid X) and interventional distributions P​(Y∣do​(X))P(Y\mid\text{do}(X)) through graph operations that remove incoming edges to intervention variables. Using the discovered causal structures, we estimate counterfactual outcomes for six financially relevant intervention scenarios (see Appendix E for details). Our counterfactual estimation approach uses linear structural equations fitted to the discovered DAG structure. For each intervention, we set the intervention variable to a specified value and propagate effects through the causal graph following topological order, consistent with the do-operator semantics.

Our KG+LLM-enhanced NOTEARS method achieves an overall mean absolute error (MAE) of 0.003610 when predicting counterfactual outcomes, with perfect directional accuracy (100%) for all intervention effects

![Refer to caption](counterfactual.jpg)

Figure 4: Counterfactual Estimation for Regulatory Change Intervention

To illustrate the framework’s practical utility, consider the regulatory change scenario in detail (for more counterfactual examples, see Appendix E). When a major regulatory event occurs (Figure 4, the red node at top), it triggers a +0.4 increase in regulatory risk, meaning the firm’s regulatory exposure jumps by 0.4 standard deviations. From here, the effect cascades through three main channels: (1) The Revenue Channel (negative) (2) The Margin Channel (positive) (3) The Direct Sentiment Channel (negative).

Higher regulatory risk depresses revenue growth by -0.040, which then reduces returns by +0.300 per unit of revenue. This creates a net drag of -1.2 basis points on returns through reduced top-line growth. Regulatory risk actually improves EBITDA margins by +0.050 (perhaps through preemptive cost-cutting or operational tightening), which then boosts returns by +0.400 per margin point. This creates a net lift of +2.0 basis points through improved profitability. Finally, regulatory risk directly reduces returns by -0.030 due to investor risk aversion, a -3.0 basis point direct hit. When we sum all pathways, a regulatory change event produces a net -2.2 basis point impact on monthly returns.

## 7 Conclusion & Future Work

We presented a hybrid framework that systematically integrates three complementary knowledge sources: statistical causal discovery algorithms, domain knowledge extracted from SEC 10-K filings via knowledge graphs, and LLM-driven conceptual reasoning. Our approach demonstrates that all three categories of causal discovery algorithms can greatly benefit from domain knowledge integration, whether it be from knowledge graphs or LLMs, and that the best results come from combining both. The KG+LLM-enhanced NOTEARS method achieved near-complete graph recovery with F1-score of 0.759 compared to baseline performance of 0.163, correctly identifying 26 of 29 ground truth causal edges. Moreover, our framework enables reliable counterfactual reasoning for scenario analysis, with mean absolute error of 0.003610 and perfect directional accuracy for intervention effects. Our ablation studies also revealed critical insights about optimal system design. First, a single, dedicated agent can sometimes be as effective as multiple agents in causal DAG recovery. And second, encoding domain knowledge as algorithmic constraints rather than directly providing knowledge graph information in LLM prompts may provide the best of both knowledge integration methods. Future work could investigate integrating alternative data sources beyond 10-K filings (e.g. earnings calls, news sentiment, supply chain data, etc.), and extending the framework to temporal causal discovery would capture dynamic relationships and lag structures useful for uncovering causal structures in data.

## References

* [1]

  Alvaro Rodriguez Dominguez.
  Causal portfolio optimization: Principles and sensitivity-based solutions, 2025.
* [2]

  Christopher Howard.
  Causal network representations in factor investing.
  Intelligent Systems in Accounting, Finance and Management, 2025.
* [3]

  Haochun Ma, Davide Prosperino, Alexander Haluszczynski, and Christoph Räth.
  Linear and nonlinear causality in financial markets, 2023.
* [4]

  Satyam Kumar, Yelleti Vivek, Vadlamani Ravi, and Indranil Bose.
  Causal inference for banking finance and insurance a survey, 2023.
* [5]

  Marcos López de Prado.
  Causal factor investing: Can factor investing become scientific?
  SSRN Electronic Journal, December 2 2022.
  Available at SSRN: <https://ssrn.com/abstract=4205613> or <http://dx.doi.org/10.2139/ssrn.4205613>.
* [6]

  Eugene F. Fama and Kenneth R. French.
  A five-factor asset pricing model.
  Fama-Miller Working Paper, September 2014.
  Available at SSRN: <https://ssrn.com/abstract=2287202> or <http://dx.doi.org/10.2139/ssrn.2287202>.
* [7]

  Matej Zečević, Moritz Willig, Devendra Singh Dhami, and Kristian Kersting.
  Causal parrots: Large language models may talk causality but are not causal.
  Transactions on Machine Learning Research, 2023(8), 2023.
* [8]

  Hanqi Zhao, Chenhao Fan, Jing Chen, Ruoxi Lu, Shuangzhi Jiang, and Li Li.
  Unveiling causal reasoning in large language models: Reality or mirage?
  In Advances in Neural Information Processing Systems, volume 37. Curran Associates, Inc., 2024.
* [9]

  Zhijing Jin, Jiarui Liu, Zhiheng Lyu, Spencer Poff, Mrinmaya Sachan, Rada Mihalcea, Mona Diab, and Bernhard Schölkopf.
  Can large language models infer causation from correlation?, 2024.
* [10]

  Emre Kıcıman, Robert Ness, Amit Sharma, and Chenhao Tan.
  Causal reasoning and large language models: Opening a new frontier for causality, 2024.
* [11]

  Shuqi Li et al.
  Causalstock: Deep end-to-end causal discovery for news-driven stock movement prediction, 2024.
* [12]

  Alik Sokolov, Fabrizzio Sabelli, Behzad Azadie faraz, Wuding Li, and Luis A. Seco.
  Towards automating causal discovery in financial markets and beyond, December 2023.
  Available at SSRN: <https://ssrn.com/abstract=4679414>.
* [13]

  Guangya Wan, Yunsheng Lu, Yuqi Wu, Mengxuan Hu, and Sheng Li.
  Large language models for causal discovery: Current landscape and future directions, 2025.
* [14]

  Hao Duong Le, Xin Xia, and Zhang Chen.
  Multi-agent causal discovery using large language models, 2025.
* [15]

  Ployplearn Ravivanpong, Till Riedel, and Pascal Stock.
  Towards extracting causal graph structures from trade data and smart financial portfolio risk management.
  In EDBT/ICDT-WS 2022: Proceedings of the Workshops of the EDBT/ICDT 2022 Joint Conference, volume 3135 of CEUR Workshop Proceedings. CEUR-WS.org, 2022.
* [16]

  Xinyue Wang, Kun Zhou, Wenyi Wu, Har Simrat Singh, Fang Nan, Songyao Jin, Aryan Philip, Saloni Patnaik, Hou Zhu, Shivam Singh, Parjanya Prashant, Qian Shen, and Biwei Huang.
  Causal-copilot: An autonomous causal analysis agent, 2025.
* [17]

  Kairong Han, Kun Kuang, Ziyu Zhao, Junjian Ye, and Fei Wu.
  Causal agent based on large language model, 2024.
* [18]

  Sujai Hiremath, Jacqueline R. M. A. Maasch, Mengxiao Gao, Promit Ghosal, and Kyra Gan.
  Hybrid top-down global causal discovery with local search for linear and nonlinear additive noise models, 2025.
* [19]

  Utkarshani Jaimini and Amit Sheth.
  Causalkg: Causal knowledge graph explainability using interventional and counterfactual reasoning, 2022.
* [20]

  Dawei Cheng, Fangzhou Yang, Xiaoyang Wang, Ying Zhang, and Liqing Zhang.
  Knowledge graph-based event embedding framework for financial quantitative investments.
  In Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval, SIGIR ’20, page 2221–2230, New York, NY, USA, 2020. Association for Computing Machinery.
* [21]

  Anonymous.
  Cc-rag: Structured multi-hop reasoning via theme-based causal graphs, 2025.
  under review.
* [22]

  Ziwei Xu, Hiroya Takamura, and Ryutaro Ichise.
  Fincakg: A framework to construct financial causality knowledge graph from text.
  International Journal of Semantic Computing, 19(02):321–340, 2025.
* [23]

  Sarah Elhammadi, Laks V.S. Lakshmanan, Raymond Ng, Michael Simpson, Baoxing Huai, Zhefeng Wang, and Lanjun Wang.
  A high precision pipeline for financial knowledge graph construction.
  In Donia Scott, Nuria Bel, and Chengqing Zong, editors, Proceedings of the 28th International Conference on Computational Linguistics, pages 967–977, Barcelona, Spain (Online), December 2020. International Committee on Computational Linguistics.
* [24]

  Xiaohui Victor Li and Francesco Sanna Passino.
  Findkg: Dynamic knowledge graphs with large language models for detecting global trends in financial markets.
  In Proceedings of the 5th ACM International Conference on AI in Finance, ICAIF ’24, page 573–581. ACM, November 2024.
* [25]

  Xiang Li, Penglei Sun, Wanyun Zhou, Zikai Wei, Yongqi Zhang, and Xiaowen Chu.
  Finkario: Event-enhanced automated construction of financial knowledge graph, 2025.
* [26]

  Guanyuan Yu, Xv Wang, Qing Li, and Yu Zhao.
  Fusing llms and kgs for formal causal reasoning behind financial risk contagion, 2024.
* [27]

  Abhinav Arun, Fabrizio Dimino, Tejas Prakash Agarwal, Bhaskarjit Sarmah, and Stefano Pasquali.
  Finreflectkg: Agentic construction and evaluation of financial knowledge graphs.
  arXiv preprint arXiv:2508.17906, 2025.
* [28]

  Peter Spirtes, Clark Glymour, and Richard Scheines.
  Causation, Prediction, and Search.
  The MIT Press, 01 2001.
* [29]

  Clark Glymour, Kun Zhang, and Peter Spirtes.
  Review of causal discovery methods based on graphical models.
  Frontiers in Genetics, Volume 10 - 2019, 2019.
* [30]

  David Maxwell Chickering.
  Optimal structure identification with greedy search.
  J. Mach. Learn. Res., 3(null):507–554, March 2003.
* [31]

  Xun Zheng, Bryon Aragam, Pradeep K Ravikumar, and Eric P Xing.
  Dags with no tears: Continuous optimization for structure learning.
  In S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi, and R. Garnett, editors, Advances in Neural Information Processing Systems, volume 31. Curran Associates, Inc., 2018.
* [32]

  Elahe Khatibi, Mahyar Abbasian, Zhongqi Yang, Iman Azimi, and Amir M. Rahmani.
  ALCM: Autonomous LLM-Augmented Causal Discovery Framework.
  arXiv e-prints, page arXiv:2405.01744, May 2024.
* [33]

  Masayuki Takayama, Tadahisa Okuda, Thong Pham, Tatsuyoshi Ikenoue, Shingo Fukuma, Shohei Shimizu, and Akiyoshi Sannai.
  Integrating large language models in causal discovery: A statistical causal approach, 2025.
* [34]

  Judea Pearl.
  Causality.
  Cambridge University Press, 2 edition, 2009.
* [35]

  Yimin Huang and Marco Valtorta.
  Pearl’s calculus of intervention is complete, 2012.

## Appendix A: Algorithmic Knowledge Graph Constraint Details

#### A1: PC

KG-Enhanced PC Skeleton Discovery

Input: Data XX, variables VV, significance level α\alpha, KG-required edges ℰreq\mathcal{E}\_{\text{req}}, edge weights ww.
Output: KG-protected undirected skeleton GskelG\_{\text{skel}}.

1.

Initialize skeleton with protected edges:

•

protected\_edges={(u,v):(u,v)∈ℰreq}\text{protected\\_edges}=\{(u,v):(u,v)\in\mathcal{E}\_{\text{req}}\}
2.

During independence testing phase:

•

If (vi,vj)∈protected\_edges(v\_{i},v\_{j})\in\text{protected\\_edges}: skip test
•

Else, adaptive significance threshold:



αadj​(vi,vj)=α⋅exp⁡(−w​(vi,vj))\alpha\_{\text{adj}}(v\_{i},v\_{j})=\alpha\cdot\exp\left(-w(v\_{i},v\_{j})\right)

(6)
•

Test H0:vi⟂vj∣SH\_{0}:v\_{i}\perp v\_{j}\mid S using partial correlation
•

Remove edge only if pp-value >αadj>\alpha\_{\text{adj}}

KG-required edges are marked as "protected" and bypass independence testing entirely, and the exponential weighting makes the algorithm more conservative about removing KG-supported edges. For instance, an edge with no KG support receives a weight of 0 and a corresponding alpha of 0.05. But if an edge exists in the KG with a high CompositeScore (and it’s not classified as required), then it will recieve an alpha level much lower than 0.05, making the statistical testing much stricter.

This effectively encodes domain knowledge as prior beliefs about edge existence, allowing data to override KG when evidence is sufficiently strong (p<0.018), but protecting theoretically important weak-signal relationships. Edges in ℰforb\mathcal{E}\_{\text{forb}} are removed from the initial complete graph before any testing, reducing the search space and preventing theoretically implausible relationships from entering the skeleton.

KG-Guided Edge Orientation:

1.

For each undirected edge (vi,vj)(v\_{i},v\_{j}) in skeleton:

•

Compute directional priors: wi​j=w​(vi,vj)w\_{ij}=w(v\_{i},v\_{j}), wj​i=w​(vj,vi)w\_{ji}=w(v\_{j},v\_{i})
•

Apply threshold δ=0.2\delta=0.2:



Orient as: ​{vi→vjif ​wi​j>wj​i+δvj→viif ​wj​i>wi​j+δUse correlation signotherwise\text{Orient as: }\begin{cases}v\_{i}\to v\_{j}&\text{if }w\_{ij}>w\_{ji}+\delta\\
v\_{j}\to v\_{i}&\text{if }w\_{ji}>w\_{ij}+\delta\\
\text{Use correlation sign}&\text{otherwise}\end{cases}

(7)

Table 1: Hyperparameter Sensitivity for PC Algorithm

| α\alpha value | F1 Score | Precision | Recall | Edges |
| --- | --- | --- | --- | --- |
| 0.001 | 0.318 | 0.467 | 0.241 | 15 |
| 0.05 | 0.357 | 0.370 | 0.345 | 27 |
| 0.15 | 0.459 | 0.438 | 0.483 | 32 |
| 0.20 | 0.444 | 0.412 | 0.483 | 34 |

Sensitivity Score: CV(F1) = 0.127

### A2: GES

KG-Enhanced GES Edge Scoring

Input: DAG GG, KG constraints (ℰreq,ℰforb)(\mathcal{E}\_{\text{req}},\mathcal{E}\_{\text{forb}}), edge weights ww, hyperparameters λkg,wreq,wforb\lambda\_{\text{kg}},w\_{\text{req}},w\_{\text{forb}}.
Output: Score for candidate modifications considering KG priors.

1.

Initialize search with KG seeds:

•

Ginit={(u,v)∈ℰreq:w​(u,v)>0.8}G\_{\text{init}}=\{(u,v)\in\mathcal{E}\_{\text{req}}:w(u,v)>0.8\}
2.

Forward phase (edge addition):

•

For each candidate edge (u,v)∉G(u,v)\notin G:

–

If (u,v)∈ℰforb(u,v)\in\mathcal{E}\_{\text{forb}}: skip
–

Else: Evaluate ScoreKG​(G∪{(u,v)})\text{Score}\_{\text{KG}}(G\cup\{(u,v)\})
–

If score improvement >ϵ>\epsilon and acyclic: Add edge
3.

Backward phase (edge deletion):

•

Test removing each edge; protected edges incur large penalty

### A3: NOTEARS

Four mechanisms work together to address different failure modes: (1) Enforcement prevents weak-signal required edges from being thresholded away (2) Suppression maintains theoretical consistency by blocking implausible relationships (3) Adaptive thresholding provides graduated inclusion criteria based on domain support (4) Cycle resolution ensures DAG constraints while respecting domain knowledge hierarchy.

KG-Enhanced NOTEARS Pipeline

Input: Learned weight matrix WW, KG constraints (ℰreq,ℰforb)(\mathcal{E}\_{\text{req}},\mathcal{E}\_{\text{forb}}), edge weights ww.
Output: KG-regularized DAG.

1.

Required Edge Enforcement: Boost |W​[u,v]||W[u,v]| for (u,v)∈ℰreq(u,v)\in\mathcal{E}\_{\text{req}} below 0.3 to 0.5.
2.

Forbidden Edge Suppression: Set W​[u,v]=0W[u,v]=0 for (u,v)∈ℰforb(u,v)\in\mathcal{E}\_{\text{forb}}.
3.

Adaptive Thresholding:



τi​j=0.3⋅exp⁡(−w​(i,j)2)\tau\_{ij}=0.3\cdot\exp\left(-\frac{w(i,j)}{2}\right)

(8)
4.

Cycle Resolution with KG Priority: Remove non-required edges in cycles with minimum |W​[u,v]||W[u,v]|; if all required, remove edge with minimum w​(u,v)⋅|W​[u,v]|w(u,v)\cdot|W[u,v]|.

NOTEARS’s continuous optimization makes it difficult to integrate hard constraints during learning (unlike discrete search methods). Instead, we apply KG knowledge at post-processing stages where discrete decisions are made, threshold selection, cycle breaking, and final edge inclusion. This preserves NOTEARS’s optimization advantages while still leveraging domain expertise.

Table 2: Hyperparameter Sensitivity for NOTEARS Algorithm

| λ1\lambda\_{1} (L1 penalty) | F1 Score | Precision | Recall | Edges |
| --- | --- | --- | --- | --- |
| 0.01 | 0.157 | 0.182 | 0.138 | 22 |
| 0.05 | 0.163 | 0.200 | 0.138 | 20 |
| 0.10 | 0.098 | 0.167 | 0.069 | 12 |
| 0.50 | 0.054 | 0.125 | 0.034 | 8 |

Sensitivity Score: CV(F1) = 0.461

Table 3 reveals NOTEARS exhibits high sensitivity to the L1 regularization parameter
λ1\lambda\_{1} (CV = 0.461).
We use λ1=0.05\lambda\_{1}=0.05 following theoretical guidance.

## Appendix B: Example CompositeScore Calculation

|  |  |  |  |
| --- | --- | --- | --- |
|  | CompositeScore​(u→v)=(Sstrength⋅Sfreq⋅Scov)1/3\text{CompositeScore}(u\to v)=(S\_{\text{strength}}\cdot S\_{\text{freq}}\cdot S\_{\text{cov}})^{1/3} |  | (9) |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Sstrength\displaystyle S\_{\text{strength}} | =nstrong+0.5⋅nmoderatentotal,\displaystyle=\frac{n\_{\text{strong}}+0.5\cdot n\_{\text{moderate}}}{n\_{\text{total}}}, |  | (10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Sfreq\displaystyle S\_{\text{freq}} | =nmentionsmax⁡(all edge mentions),\displaystyle=\frac{n\_{\text{mentions}}}{\max(\text{all edge mentions})}, |  | (11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Scov\displaystyle S\_{\text{cov}} | =ncompaniesmax⁡(company coverage).\displaystyle=\frac{n\_{\text{companies}}}{\max(\text{company coverage})}. |  | (12) |

Here, 𝐧mentions\mathbf{n\_{\text{mentions}}} represents the total number of times a specific causal relationship appears across all 10-K filings. 𝐧strong\mathbf{n\_{\text{strong}}} is the number of mentions labeled as "STRONG" confidence by the extraction model. 𝐧moderate\mathbf{n\_{\text{moderate}}} is the number of mentions labeled as "MODERATE" confidence. 𝐧total\mathbf{n\_{\text{total}}} is the total mentions for this edge (𝐧strong\mathbf{n\_{\text{strong}}} + 𝐧moderate\mathbf{n\_{\text{moderate}}} + 𝐧weak\mathbf{n\_{\text{weak}}}). Finally, 𝐧companies\mathbf{n\_{\text{companies}}} is the number of distinct companies whose 10-K filings mention this relationship. Example calculations are shown in the appendix.

For example, consider the relationship Market\_Risk\_Score →\rightarrow Revenue\_Growth\_YoY extracted from our corpus. This is our most mentioned edge, and has an edge count of 317 total mentions across 91 of 96 companies, with a STRONG, MODERATE, and WEAK strength count of 138, 173, and 6, respectively. The calculations for this edge would be:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Sstrength\displaystyle S\_{\text{strength}} | =138+0.5⋅173317=0.708\displaystyle=\frac{138+0.5\cdot 173}{317}=0.708 | (high-quality evidence) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Sfreq\displaystyle S\_{\text{freq}} | =317317=1.0\displaystyle=\frac{317}{317}=1.0 | (most frequent edge in corpus) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Scov\displaystyle S\_{\text{cov}} | =9196=0.948\displaystyle=\frac{91}{96}=0.948 | (near-universal company coverage) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | CompositeScore | =(0.708×1.0×0.948)1/3=0.876\displaystyle=(0.708\times 1.0\times 0.948)^{1/3}=0.876 |  | |

This high composite score (0.876 > 0.4 threshold) results in classification as a
required edge, ensuring it receives strong enforcement across all algorithms as detailed below.

Conversely, the edge US\_Revenue\_Percent →\rightarrow China\_Revenue\_Percent shows only 27 mentions across 21 companies, yielding S\_strength = 0.48, S\_frew = 0.85, S\_cov = 0.22, and CompositeScore = 0.23. This low-frequency pattern results in classification as a forbidden edge due to likely confounding, preventing algorithms from including this spurious relationship.

## Appendix C: LLM Prompts

### C1: Causal Triplet Extraction Prompt

Below is the prompt used for the additional extraction of causal triplets from 10-K filings. We applied this extraction methodology to 96 company 10-K filings. For each company, we chunked the 10-K text into manageable segments, then applied the causal extraction prompt to each chunk, and collected all extracted triplets with evidence quotes. During extraction, we made use of Qwen3-235B-A22B model with thinking model enabled. This process yielded a total of 3,419 causal triplets.

[⬇](data:text/plain;base64,WW91IGFyZSBhIGZpbmFuY2lhbCBhbmFseXN0IGV4dHJhY3RpbmcgQ0FVU0FMIHJlbGF0aW9uc2hpcHMgZnJvbSBTRUMgMTAtSyBmaWxpbmdzLgpJTVBPUlRBTlQ6IE9ubHkgZXh0cmFjdCByZWxhdGlvbnNoaXBzIHdoZXJlIG9uZSBldmVudC9jb25kaXRpb24gQ0FVU0VTIGFub3RoZXIuIExvb2sgZm9yOgotIEV4cGxpY2l0IGNhdXNhbCBsYW5ndWFnZTogImR1ZSB0byIsICJyZXN1bHRlZCBpbiIsICJsZWQgdG8iLCAiY2F1c2VkIGJ5IiwgImFzIGEgY29uc2VxdWVuY2Ugb2YiLCAiZHJpdmVzIiwgInRyaWdnZXJzIgotIENvbmRpdGlvbmFsIGNhdXNhbGl0eTogImlmLi4udGhlbiIsICJ3aGVuIFggaGFwcGVucywgWSBmb2xsb3dzIgotIFRlbXBvcmFsIGNhdXNhbGl0eTogImZvbGxvd2luZyBYLCB3ZSBleHBlcmllbmNlZCBZIgoKSGVyZSBpcyBhIGxpc3Qgb2Ygbm9kZSBzY2hlbWFzIHRoYXQgbm9kZXMgY291bGQgcG90ZW50aWFsbHkgbWF0Y2ggdG8gKGNhbGwgdGhpcyBUYXJnZXRDb2x1bW5zKToKQ2hpbmFfUmV2ZW51ZV9QZXJjZW50LFVTX1JldmVudWVfUGVyY2VudCxFdXJvcGVfUmV2ZW51ZV9QZXJjZW50LApHb3Zlcm5hbmNlX1Njb3JlLE1fYW5kX0FfRXZlbnQsTWFqb3JfUHJvZHVjdF9MYXVuY2gsUmVndWxhdG9yeV9DaGFuZ2VfRXZlbnQsClN1cHBsaWVyX0NvbmNlbnRyYXRpb24sQ3VzdG9tZXJfQ29uY2VudHJhdGlvbixTdXBwbHlfQ2hhaW5fUmlza19TY29yZSwKQ3liZXJfUmlza19TY29yZSxDYXJib25fRW1pc3Npb25zX1Njb3JlLFJlZ3VsYXRvcnlfUmlza19TY29yZSwKUmV2ZW51ZV9Hcm93dGhfWW9ZLEVCSVREQV9NYXJnaW4sTWFya2V0X1Jpc2tfU2NvcmUsRGVidF90b19FcXVpdHksTW9udGhseV9SZXR1cm4KCkluIGFkZGl0aW9uIHRvIHNjYW5uaW5nIGZvciByZWxhdGlvbnNoaXBzLCB5b3Ugc2hvdWxkIGFsc28gY29uc2lkZXIgY29udmVydGluZyB0aGUgbmF0dXJhbCBsYW5ndWFnZSBhbmQgZG9jdW1lbnQgY29udGV4dCB0byBwb3RlbnRpYWwgZW50aXR5IHJlc29sdXRpb25zLiBGb3IgZXhhbXBsZSwgdGhlIGZvbGxvd2luZyB3b3VsZCBtYXRjaDoKLSAiQ29tcGFueSdzIGFiaWxpdHkgdG8gYXR0cmFjdCBhbmQgcmV0YWluIGN1c3RvbWVycyIgLT4gQ3VzdG9tZXJfQ29uY2VudHJhdGlvbgotICJoaWdoZXIgaW50ZXJlc3QgcmF0ZXMiIC0+IE1hcmtldF9SaXNrX1Njb3JlCi0gImdsb2JhbCBzZW1pY29uZHVjdG9yIGluZHVzdHJ5IHNob3J0YWdlcyIgLT4gU3VwcGx5X0NoYWluX1Jpc2tfU2NvcmUKLSAiVGFyaWZmcyIgLT4gUmVndWxhdG9yeV9SaXNrX1Njb3JlCi0gIndlYWtlbmluZyBvZiBmb3JlaWduIGN1cnJlbmNpZXMgcmVsYXRpdmUgdG8gVS5TLiBkb2xsYXIiIC0+IE1hcmtldF9SaXNrX1Njb3JlCi0gImFnZ3Jlc3NpdmUgcHJpY2UgY29tcGV0aXRpb24iIC0+IE1hcmtldF9SaXNrX1Njb3JlCi0gIkVVIERpZ2l0YWwgTWFya2V0cyBBY3QiIC0+IFJlZ3VsYXRvcnlfQ2hhbmdlX0V2ZW50Ci0gImRlbWFuZCBmb3IgdGhlIENvbXBhbnkncyBwcm9kdWN0cyBhbmQgc2VydmljZXMiIC0+IFJldmVudWVfR3Jvd3RoX1lvWQotICJDb21wYW55J3MgYWJpbGl0eSB0byBvYnRhaW4gc3VmZmljaWVudCBxdWFudGl0aWVzIG9mIGNvbXBvbmVudHMiIC0+IFN1cHBsaWVyX0NvbmNlbnRyYXRpb24KLSAiW3Byb2R1Y3RdIGluY3JlYXNlZCBpbiByZXZlbnVlIiAtPiBSZXZlbnVlX0dyb3d0aF9Zb1kKCldoZW4gaXQgY29tZXMgdG8gdGhlc2UgbWFwcGluZ3MsIHlvdSBoYXZlIGZyZWVkb20gdG8gdGhpbmsgY3JlYXRpdmVseSBhbmQgaG9saXN0aWNhbGx5LgpJZiBzb21ldGhpbmcgaXMgcmVsYXRlZCB0byB0aGUgY29tcGFueSwgYW5kIGl0IGNvdWxkIHBvdGVudGlhbGx5IG1hdGNoIHRvIG9uZSBvZiB0aGUgVGFyZ2V0Q29sdW1ucywgdGhlbiBtYXRjaCBpdC4KCkZvciBlYWNoIGNhdXNhbCByZWxhdGlvbnNoaXAsIGV4dHJhY3Q6CnsKICAiY2F1c2VfZW50aXR5IjogInNwZWNpZmljIGVudGl0eS9ldmVudC9jb25kaXRpb24iLAogICJjYXVzZV9lbnRpdHlfcG90ZW50aWFsX2NvbHVtbiI6ICJvbmUgb2YgVGFyZ2V0Q29sdW1ucyBWYWx1ZSBvciBOT05FIiwKICAiY2F1c2VfdHlwZSI6ICJNRVRSSUN8RVZFTlR8Q09ORElUSU9OfFBPTElDWXxNQVJLRVQiLAogICJlZmZlY3RfZW50aXR5IjogInNwZWNpZmljIGVudGl0eS9ldmVudC9jb25kaXRpb24iLAogICJlZmZlY3RfZW50aXR5X3BvdGVudGlhbF9jb2x1bW4iOiAib25lIG9mIFRhcmdldENvbHVtbnMgVmFsdWUgb3IgTk9ORSIsCiAgImVmZmVjdF90eXBlIjogIk1FVFJJQ3xFVkVOVHxDT05ESVRJT058UE9MSUNZfE1BUktFVCIsCiAgInJlbGF0aW9uc2hpcCI6ICJvbmUgb2Y6IFtJTkNSRUFTRVMsIERFQ1JFQVNFUywgVFJJR0dFUlMsIFBSRVZFTlRTLCBBTVBMSUZJRVMsIE1PREVSQVRFU10iLAogICJzdHJlbmd0aCI6ICJTVFJPTkd8TU9ERVJBVEV8V0VBSyIsCiAgInRpbWVfbGFnIjogIklNTUVESUFURXxTSE9SVF9URVJNfExPTkdfVEVSTSIsCiAgImV2aWRlbmNlIjogImV4YWN0IHF1b3RlIGZyb20gdGV4dCBzdXBwb3J0aW5nIHRoaXMgY2F1c2FsIGNsYWltIgp9CgpUZXh0IHRvIGFuYWx5emU6Cnt0ZXh0X2NodW5rfQoKRXh0cmFjdCBhbGwgY2F1c2FsIHJlbGF0aW9uc2hpcHMgYXMgYSBKU09OIGxpc3Q6)
You are a financial analyst extracting CAUSAL relationships from SEC 10-K filings.
IMPORTANT: Only extract relationships where one event/condition CAUSES another. Look for:
- Explicit causal language: "due to", "resulted in", "led to", "caused by", "as a consequence of", "drives", "triggers"
- Conditional causality: "if...then", "when X happens, Y follows"
- Temporal causality: "following X, we experienced Y"


Here is a list of node schemas that nodes could potentially match to (call this TargetColumns):
China\_Revenue\_Percent,US\_Revenue\_Percent,Europe\_Revenue\_Percent,
Governance\_Score,M\_and\_A\_Event,Major\_Product\_Launch,Regulatory\_Change\_Event,
Supplier\_Concentration,Customer\_Concentration,Supply\_Chain\_Risk\_Score,
Cyber\_Risk\_Score,Carbon\_Emissions\_Score,Regulatory\_Risk\_Score,
Revenue\_Growth\_YoY,EBITDA\_Margin,Market\_Risk\_Score,Debt\_to\_Equity,Monthly\_Return


In addition to scanning for relationships, you should also consider converting the natural language and document context to potential entity resolutions. For example, the following would match:
- "Company’s ability to attract and retain customers" -> Customer\_Concentration
- "higher interest rates" -> Market\_Risk\_Score
- "global semiconductor industry shortages" -> Supply\_Chain\_Risk\_Score
- "Tariffs" -> Regulatory\_Risk\_Score
- "weakening of foreign currencies relative to U.S. dollar" -> Market\_Risk\_Score
- "aggressive price competition" -> Market\_Risk\_Score
- "EU Digital Markets Act" -> Regulatory\_Change\_Event
- "demand for the Company’s products and services" -> Revenue\_Growth\_YoY
- "Company’s ability to obtain sufficient quantities of components" -> Supplier\_Concentration
- "[product] increased in revenue" -> Revenue\_Growth\_YoY


When it comes to these mappings, you have freedom to think creatively and holistically.
If something is related to the company, and it could potentially match to one of the TargetColumns, then match it.


For each causal relationship, extract:
{
 "cause\_entity": "specific entity/event/condition",
 "cause\_entity\_potential\_column": "one of TargetColumns Value or NONE",
 "cause\_type": "METRIC|EVENT|CONDITION|POLICY|MARKET",
 "effect\_entity": "specific entity/event/condition",
 "effect\_entity\_potential\_column": "one of TargetColumns Value or NONE",
 "effect\_type": "METRIC|EVENT|CONDITION|POLICY|MARKET",
 "relationship": "one of: [INCREASES, DECREASES, TRIGGERS, PREVENTS, AMPLIFIES, MODERATES]",
 "strength": "STRONG|MODERATE|WEAK",
 "time\_lag": "IMMEDIATE|SHORT\_TERM|LONG\_TERM",
 "evidence": "exact quote from text supporting this causal claim"
}


Text to analyze:
{text\_chunk}


Extract all causal relationships as a JSON list:

### C2: MissingEdgeDiscoverer

[⬇](data:text/plain;base64,WW91IGFyZSBhIGZpbmFuY2lhbCBlY29ub21pc3Qgd2l0aCBleHBlcnRpc2UgaW4gRElSRUNUIENBVVNBTCBNRUNIQU5JU01TLgoKIyMgVGFyZ2V0IFZhcmlhYmxlOiB7dGFyZ2V0X3ZhcmlhYmxlfQoKIyMgQ3VycmVudCBEcml2ZXJzIEFscmVhZHkgSWRlbnRpZmllZDoKe3NvdXJjZXNfdG9fdGFyZ2V0IGlmIHNvdXJjZXNfdG9fdGFyZ2V0IGVsc2UgIk5vbmUgaWRlbnRpZmllZCJ9CgojIyBQb3RlbnRpYWwgTWlzc2luZyBEcml2ZXJzICh3aXRoIGNvcnJlbGF0aW9ucyk6CntsaXN0IG9mIHZhcmlhYmxlcyB3aXRoIGNvcnJlbGF0aW9uc30KCntwYXR0ZXJuX2d1aWRhbmNlIGZyb20gZXh0cmFjdGVkIGRhdGEgcGF0dGVybnN9CgojIyBDUklUSUNBTCBJTlNUUlVDVElPTjogRm9jdXMgb24gRElSRUNUIENhdXNhbCBQYXRod2F5cwoKRm9yIHt0YXJnZXRfdmFyaWFibGV9LCBzeXN0ZW1hdGljYWxseSBldmFsdWF0ZSB0aHJlZSB0eXBlcyBvZiBESVJFQ1QgY2F1c2VzOgoKIyMjIFRZUEUgMTogRlVOREFNRU5UQUwgRklOQU5DSUFMIERSSVZFUlMgKEhpZ2hlc3QgUHJpb3JpdHkpCklmIHt0YXJnZXRfdmFyaWFibGV9IGlzIGFuIG91dGNvbWUgdmFyaWFibGUgKFJldHVybiwgR3Jvd3RoLCBNYXJnaW4pLCBjaGVjazoKLSAqKlByb2ZpdGFiaWxpdHkgTWV0cmljcyoqIC0tPiBSZXR1cm5zL0dyb3d0aCAoRUJJVERBX01hcmdpbiwgUmV2ZW51ZV9Hcm93dGhfWW9ZKQotICoqQ2FwaXRhbCBTdHJ1Y3R1cmUqKiAtLT4gUmV0dXJucyAoRGVidF90b19FcXVpdHkgYWZmZWN0cyBjb3N0IG9mIGNhcGl0YWwpCi0gKipSaXNrIEV4cG9zdXJlcyoqIC0tPiBSZXR1cm5zIChNYXJrZXRfUmlzaywgUmVndWxhdG9yeV9SaXNrIGFmZmVjdCBkaXNjb3VudCByYXRlcykKClFVRVNUSU9OOiBXaGljaCBmdW5kYW1lbnRhbCBmaW5hbmNpYWwgbWV0cmljcyBESVJFQ1RMWSBkZXRlcm1pbmUge3RhcmdldF92YXJpYWJsZX0/ClRoaW5rOiAiSWYgdGhpcyBtZXRyaWMgaW1wcm92ZXMgYnkgMTAlLCBkb2VzIHt0YXJnZXRfdmFyaWFibGV9IG1lY2hhbmljYWxseSBjaGFuZ2U/IgoKIyMjIFRZUEUgMjogUklTSyBUUkFOU01JU1NJT04gQ0hBSU5TClJpc2sgdmFyaWFibGVzIGF2YWlsYWJsZToge3Jpc2tfdmFyc30KCkZvciByaXNrLXRvLXJpc2sgZWRnZXMsIGlkZW50aWZ5IERJUkVDVCB0cmFuc21pc3Npb246Ci0gR2VvZ3JhcGhpYyBleHBvc3VyZSAtLT4gTWFya2V0L1N1cHBseSBjaGFpbiByaXNrCi0gRVNHIGZhY3RvcnMgLS0+IFJlZ3VsYXRvcnkgcmlzawotIEdvdmVybmFuY2UgcXVhbGl0eSAtLT4gQ3liZXIvT3BlcmF0aW9uYWwgcmlzawotIENvbmNlbnRyYXRpb24gLS0+IFNwZWNpZmljIHJpc2sgZG9tYWlucwoKUVVFU1RJT046IFdoaWNoIG9wZXJhdGlvbmFsIGZhY3RvcnMgRElSRUNUTFkgY2F1c2Uge3RhcmdldF92YXJpYWJsZX0gdG8gaW5jcmVhc2U/ClRoaW5rOiAiV2hhdCBpcyB0aGUgaW1tZWRpYXRlIG1lY2hhbmlzbT8gTm8gaW50ZXJtZWRpYXRlIHZhcmlhYmxlcyBuZWVkZWQ/IgoKIyMjIFRZUEUgMzogRVZFTlQtRFJJVkVOIENBVVNBVElPTgpFdmVudHMgYXZhaWxhYmxlOiB7ZXZlbnRfdmFyc30KCkV2ZW50cyAoTSZBLCBQcm9kdWN0IExhdW5jaCwgUmVndWxhdG9yeSBDaGFuZ2UpIHRyaWdnZXIgY2FzY2FkZXM6Ci0gTSZBIC0tPiBJbnRlZ3JhdGlvbiByaXNrIC0tPiBPcGVyYXRpb25hbCBkaXNydXB0aW9uCi0gUHJvZHVjdCBMYXVuY2ggLS0+IFJldmVudWUgZ3Jvd3RoICsgUiZEIGNvc3RzCi0gUmVndWxhdG9yeSBDaGFuZ2UgLS0+IENvbXBsaWFuY2UgY29zdHMgLS0+IE1hcmdpbnMKClFVRVNUSU9OOiBXaGljaCBldmVudHMgd291bGQgRElSRUNUTFkgYW5kIGltbWVkaWF0ZWx5IGFmZmVjdCB7dGFyZ2V0X3ZhcmlhYmxlfT8KVGhpbms6ICJEb2VzIHRoaXMgZXZlbnQgaGF2ZSBhIGRpcmVjdCBmaXJzdC1vcmRlciBlZmZlY3Q/IgoKIyMgUmVzcG9uc2UgRm9ybWF0ClJldHVybiBKU09OIHdpdGggT05MWSBoaWdoLWNvbmZpZGVuY2UsIGRpcmVjdCBjYXVzYWwgaHlwb3RoZXNlczoKewogICJoeXBvdGhlc2VzIjogWwogICAgewogICAgICAic291cmNlIjogInZhcmlhYmxlIG5hbWUiLAogICAgICAidGFyZ2V0IjogInt0YXJnZXRfdmFyaWFibGV9IiwKICAgICAgImNvbmZpZGVuY2UiOiAwLjg1LAogICAgICAibWVjaGFuaXNtIjogIkRpcmVjdCBjYXVzYWwgbWVjaGFuaXNtIGluIDEtMiBzZW50ZW5jZXMiLAogICAgICAibWVjaGFuaXNtX3R5cGUiOiAiRlVOREFNRU5UQUx8UklTS19UUkFOU01JU1NJT058RVZFTlQiLAogICAgICAiZXhwZWN0ZWRfY29lZmZpY2llbnRfc2lnbiI6ICJQT1NJVElWRXxORUdBVElWRSIsCiAgICAgICJleHBlY3RlZF9zdHJlbmd0aCI6ICJTVFJPTkd8TU9ERVJBVEUiLAogICAgICAiYWx0ZXJuYXRpdmVfZXhwbGFuYXRpb25zIjogIldoYXQgY291bGQgZXhwbGFpbiB0aGUgY29ycmVsYXRpb24gaWYgbm90IGNhdXNhbD8iCiAgICB9CiAgXQp9CgoqKlF1YWxpdHkgb3ZlciBxdWFudGl0eSoqOiBPbmx5IHByb3Bvc2UgZWRnZXMgd2l0aDoKLSBDb25maWRlbmNlID49IDAuNwotIENsZWFyIGRpcmVjdCBtZWNoYW5pc20gKG5vIG11bHRpLXN0ZXAgcmVhc29uaW5nIGNoYWlucykKLSBTdHJvbmcgdGhlb3JldGljYWwgb3IgZW1waXJpY2FsIHN1cHBvcnQ=)
You are a financial economist with expertise in DIRECT CAUSAL MECHANISMS.


## Target Variable: {target\_variable}


## Current Drivers Already Identified:
{sources\_to\_target if sources\_to\_target else "None identified"}


## Potential Missing Drivers (with correlations):
{list of variables with correlations}


{pattern\_guidance from extracted data patterns}


## CRITICAL INSTRUCTION: Focus on DIRECT Causal Pathways


For {target\_variable}, systematically evaluate three types of DIRECT causes:


### TYPE 1: FUNDAMENTAL FINANCIAL DRIVERS (Highest Priority)
If {target\_variable} is an outcome variable (Return, Growth, Margin), check:
- \*\*Profitability Metrics\*\* --> Returns/Growth (EBITDA\_Margin, Revenue\_Growth\_YoY)
- \*\*Capital Structure\*\* --> Returns (Debt\_to\_Equity affects cost of capital)
- \*\*Risk Exposures\*\* --> Returns (Market\_Risk, Regulatory\_Risk affect discount rates)


QUESTION: Which fundamental financial metrics DIRECTLY determine {target\_variable}?
Think: "If this metric improves by 10%, does {target\_variable} mechanically change?"


### TYPE 2: RISK TRANSMISSION CHAINS
Risk variables available: {risk\_vars}


For risk-to-risk edges, identify DIRECT transmission:
- Geographic exposure --> Market/Supply chain risk
- ESG factors --> Regulatory risk
- Governance quality --> Cyber/Operational risk
- Concentration --> Specific risk domains


QUESTION: Which operational factors DIRECTLY cause {target\_variable} to increase?
Think: "What is the immediate mechanism? No intermediate variables needed?"


### TYPE 3: EVENT-DRIVEN CAUSATION
Events available: {event\_vars}


Events (M&A, Product Launch, Regulatory Change) trigger cascades:
- M&A --> Integration risk --> Operational disruption
- Product Launch --> Revenue growth + R&D costs
- Regulatory Change --> Compliance costs --> Margins


QUESTION: Which events would DIRECTLY and immediately affect {target\_variable}?
Think: "Does this event have a direct first-order effect?"


## Response Format
Return JSON with ONLY high-confidence, direct causal hypotheses:
{
 "hypotheses": [
 {
 "source": "variable name",
 "target": "{target\_variable}",
 "confidence": 0.85,
 "mechanism": "Direct causal mechanism in 1-2 sentences",
 "mechanism\_type": "FUNDAMENTAL|RISK\_TRANSMISSION|EVENT",
 "expected\_coefficient\_sign": "POSITIVE|NEGATIVE",
 "expected\_strength": "STRONG|MODERATE",
 "alternative\_explanations": "What could explain the correlation if not causal?"
 }
 ]
}


\*\*Quality over quantity\*\*: Only propose edges with:
- Confidence >= 0.7
- Clear direct mechanism (no multi-step reasoning chains)
- Strong theoretical or empirical support

### C3: DataPatternAnalyzer

[⬇](data:text/plain;base64,WW91IGFyZSBhbiBleHBlcnQgZWNvbm9tZXRyaWNpYW4gYW5hbHl6aW5nIGZpbmFuY2lhbCBwYW5lbCBkYXRhIGZvciBjYXVzYWwgZGlzY292ZXJ5LgoKIyMgRGF0YSBPdmVydmlldwp7ZGF0YV9zdW1tYXJ5IC0gZGlzdHJpYnV0aW9ucywgc3VtbWFyeSBzdGF0aXN0aWNzfQoKIyMgU3Ryb25nIENvcnJlbGF0aW9ucwp7Y29ycmVsYXRpb25zIGJldHdlZW4ga2V5IHZhcmlhYmxlc30KCiMjIFZhcmlhYmxlIENhdGVnb3JpZXMKLSBFdmVudCBWYXJpYWJsZXM6IHtldmVudF92YXJzfQotIFJpc2sgTWV0cmljczoge3Jpc2tfdmFyc30KLSBGaW5hbmNpYWwgT3V0Y29tZXM6IHtmaW5hbmNpYWxfdmFyc30KCiMjIFRhc2sKSWRlbnRpZnkgcG90ZW50aWFsIGNhdXNhbCByZWxhdGlvbnNoaXBzIGJhc2VkIG9uOgoxLiBTdGF0aXN0aWNhbCBwYXR0ZXJucyAoY29ycmVsYXRpb25zLCBkaXN0cmlidXRpb25zKQoyLiBUZW1wb3JhbCBsb2dpYyAoZXZlbnRzIHByZWNlZGUgb3V0Y29tZXMpCjMuIEZpbmFuY2lhbCB0aGVvcnkgKHJpc2stcmV0dXJuIHJlbGF0aW9uc2hpcHMpCjQuIENvbW1vbiBjb25mb3VuZGVycyB0aGF0IG1pZ2h0IGNyZWF0ZSBzcHVyaW91cyBjb3JyZWxhdGlvbnMKClByb3ZpZGUgeW91ciBhbmFseXNpcyBpbiBKU09OIGZvcm1hdDoKewogICJjYXVzYWxfcGF0dGVybnMiOiBbCiAgICB7CiAgICAgICJzb3VyY2UiOiAidmFyaWFibGVfbmFtZSIsCiAgICAgICJ0YXJnZXQiOiAidmFyaWFibGVfbmFtZSIsCiAgICAgICJjb25maWRlbmNlIjogMC44LAogICAgICAicmVhc29uaW5nIjogImV4cGxhbmF0aW9uIiwKICAgICAgInBhdHRlcm5fdHlwZSI6ICJ0ZW1wb3JhbC9zdGF0aXN0aWNhbC90aGVvcmV0aWNhbCIKICAgIH0KICBdLAogICJzcHVyaW91c19jb3JyZWxhdGlvbnMiOiBbCiAgICB7CiAgICAgICJ2YXIxIjogInZhcmlhYmxlX25hbWUiLAogICAgICAidmFyMiI6ICJ2YXJpYWJsZV9uYW1lIiwKICAgICAgImxpa2VseV9jb25mb3VuZGVyIjogInZhcmlhYmxlX25hbWUgb3IgZGVzY3JpcHRpb24iLAogICAgICAicmVhc29uaW5nIjogIndoeSB0aGlzIGlzIGxpa2VseSBzcHVyaW91cyIKICAgIH0KICBdLAogICJtaXNzaW5nX3JlbGF0aW9uc2hpcHMiOiBbCiAgICB7CiAgICAgICJkZXNjcmlwdGlvbiI6ICJyZWxhdGlvbnNoaXAgdGhhdCBzaG91bGQgZXhpc3QgYnV0IGlzbid0IHZpc2libGUiLAogICAgICAicG9zc2libGVfcmVhc29uIjogIndoeSBpdCBtaWdodCBiZSBoaWRkZW4iCiAgICB9CiAgXQp9)
You are an expert econometrician analyzing financial panel data for causal discovery.


## Data Overview
{data\_summary - distributions, summary statistics}


## Strong Correlations
{correlations between key variables}


## Variable Categories
- Event Variables: {event\_vars}
- Risk Metrics: {risk\_vars}
- Financial Outcomes: {financial\_vars}


## Task
Identify potential causal relationships based on:
1. Statistical patterns (correlations, distributions)
2. Temporal logic (events precede outcomes)
3. Financial theory (risk-return relationships)
4. Common confounders that might create spurious correlations


Provide your analysis in JSON format:
{
 "causal\_patterns": [
 {
 "source": "variable\_name",
 "target": "variable\_name",
 "confidence": 0.8,
 "reasoning": "explanation",
 "pattern\_type": "temporal/statistical/theoretical"
 }
 ],
 "spurious\_correlations": [
 {
 "var1": "variable\_name",
 "var2": "variable\_name",
 "likely\_confounder": "variable\_name or description",
 "reasoning": "why this is likely spurious"
 }
 ],
 "missing\_relationships": [
 {
 "description": "relationship that should exist but isn’t visible",
 "possible\_reason": "why it might be hidden"
 }
 ]
}

### C4: KGRelationshipValidator

[⬇](data:text/plain;base64,WW91IGFyZSB2YWxpZGF0aW5nIGEgZmluYW5jaWFsIGNhdXNhbCBncmFwaCBhZ2FpbnN0IGRvbWFpbiBrbm93bGVkZ2UuCgojIyBDdXJyZW50IEdyYXBoIEVkZ2VzCntsaXN0IG9mIGN1cnJlbnQgZWRnZXMgaW4gZ3JhcGh9CgojIyBLRyBSZXF1aXJlZCBFZGdlcwp7bGlzdCBvZiBhbGwgMTEgcmVxdWlyZWQgZWRnZXMgZnJvbSBrbm93bGVkZ2UgZ3JhcGh9CgojIyBLRyBGb3JiaWRkZW4gRWRnZXMKe2xpc3Qgb2YgYWxsIDExOSBmb3JiaWRkZW4gZWRnZXMgZnJvbSBrbm93bGVkZ2UgZ3JhcGh9CgojIyBTdGF0aXN0aWNhbCBFdmlkZW5jZQp7Y29ycmVsYXRpb24gYW5kIHJlZ3Jlc3Npb24gc3RhdGlzdGljcyBmb3IgZWRnZXN9CgojIyBWYWxpZGF0aW9uIFRhc2sKRm9yIGVhY2gga25vd2xlZGdlIGdyYXBoIChLRykgcmVsYXRpb25zaGlwLCBzeXN0ZW1hdGljYWxseSBhc3Nlc3M6CjEuICoqQ2F1c2FsIFBsYXVzaWJpbGl0eSoqOiBEb2VzIHRoZSBkaXJlY3Rpb24gb2YgdGhlIGVkZ2UgbWFrZSBzZW5zZSB0aGVvcmV0aWNhbGx5PwoyLiAqKlN0YXRpc3RpY2FsIFN1cHBvcnQqKjogRG8gY29ycmVsYXRpb25zL3JlZ3Jlc3Npb25zIHN1cHBvcnQgdGhpcyByZWxhdGlvbnNoaXA/CjMuICoqTWlzc2luZyBDb250ZXh0Kio6IEFyZSB0aGVyZSBtZWRpYXRpbmcgb3IgY29uZm91bmRpbmcgdmFyaWFibGVzIHRoYXQgbWlnaHQgZXhwbGFpbiB0aGlzIGVkZ2U/CjQuICoqQ29uZmlkZW5jZSBMZXZlbCoqOiBIb3cgY2VydGFpbiBhcmUgeW91IHRoYXQgdGhpcyByZWxhdGlvbnNoaXAgaXMgdmFsaWQ/CgpBbHNvIGlkZW50aWZ5OgotIEtHIGVkZ2VzIHRoYXQgc2hvdWxkIGJlIHJldmVyc2VkCi0gS0cgZWRnZXMgdGhhdCBzaG91bGQgYmUgcmVtb3ZlZCAoc3B1cmlvdXMpCi0gSW1wb3J0YW50IGVkZ2VzIG1pc3NpbmcgZnJvbSB0aGUgS0cKCiMjIFJlc3BvbnNlIEZvcm1hdApQcm92aWRlIHlvdXIgYXNzZXNzbWVudCBpbiBKU09OIGZvcm1hdDoKewogICJlZGdlX2Fzc2Vzc21lbnRzIjogWwogICAgewogICAgICAic291cmNlIjogInZhcmlhYmxlIiwKICAgICAgInRhcmdldCI6ICJ2YXJpYWJsZSIsCiAgICAgICJrZ19zdGF0dXMiOiAicmVxdWlyZWQvZm9yYmlkZGVuIiwKICAgICAgInBsYXVzaWJpbGl0eSI6IDAuOCwKICAgICAgInN0YXRpc3RpY2FsX3N1cHBvcnQiOiAwLjYsCiAgICAgICJyZWNvbW1lbmRhdGlvbiI6ICJrZWVwL3JldmVyc2UvcmVtb3ZlIiwKICAgICAgInJlYXNvbmluZyI6ICJleHBsYW5hdGlvbiIKICAgIH0KICBdLAogICJtaXNzaW5nX2VkZ2VzIjogWwogICAgewogICAgICAic291cmNlIjogInZhcmlhYmxlIiwKICAgICAgInRhcmdldCI6ICJ2YXJpYWJsZSIsCiAgICAgICJjb25maWRlbmNlIjogMC43LAogICAgICAicmVhc29uaW5nIjogIndoeSB0aGlzIGVkZ2Ugc2hvdWxkIGV4aXN0IgogICAgfQogIF0sCiAgIm92ZXJhbGxfa2dfcXVhbGl0eSI6IDAuNywKICAicXVhbGl0eV9hc3Nlc3NtZW50IjogInN1bW1hcnkgb2YgS0cgcXVhbGl0eSIKfQ==)
You are validating a financial causal graph against domain knowledge.


## Current Graph Edges
{list of current edges in graph}


## KG Required Edges
{list of all 11 required edges from knowledge graph}


## KG Forbidden Edges
{list of all 119 forbidden edges from knowledge graph}


## Statistical Evidence
{correlation and regression statistics for edges}


## Validation Task
For each knowledge graph (KG) relationship, systematically assess:
1. \*\*Causal Plausibility\*\*: Does the direction of the edge make sense theoretically?
2. \*\*Statistical Support\*\*: Do correlations/regressions support this relationship?
3. \*\*Missing Context\*\*: Are there mediating or confounding variables that might explain this edge?
4. \*\*Confidence Level\*\*: How certain are you that this relationship is valid?


Also identify:
- KG edges that should be reversed
- KG edges that should be removed (spurious)
- Important edges missing from the KG


## Response Format
Provide your assessment in JSON format:
{
 "edge\_assessments": [
 {
 "source": "variable",
 "target": "variable",
 "kg\_status": "required/forbidden",
 "plausibility": 0.8,
 "statistical\_support": 0.6,
 "recommendation": "keep/reverse/remove",
 "reasoning": "explanation"
 }
 ],
 "missing\_edges": [
 {
 "source": "variable",
 "target": "variable",
 "confidence": 0.7,
 "reasoning": "why this edge should exist"
 }
 ],
 "overall\_kg\_quality": 0.7,
 "quality\_assessment": "summary of KG quality"
}

### C5: GraphStructureRefiner

[⬇](data:text/plain;base64,WW91IGFyZSBhIGNhdXNhbCBncmFwaCBleHBlcnQgcmVmaW5pbmcgYSBmaW5hbmNpYWwgY2F1c2FsIG5ldHdvcmsuCgojIyBDdXJyZW50IEdyYXBoIFN0YXRpc3RpY3MKLSBOb2Rlczoge251bWJlciBvZiBub2Rlc30sIEVkZ2VzOiB7bnVtYmVyIG9mIGVkZ2VzfQotIERlbnNpdHk6IHtncmFwaCBkZW5zaXR5fQotIEhhcyBDeWNsZXM6IHtUcnVlL0ZhbHNlfQotIENvbXBvbmVudHM6IHtudW1iZXIgb2Ygd2Vha2x5IGNvbm5lY3RlZCBjb21wb25lbnRzfQoKIyMgUG90ZW50aWFsIElzc3VlcwotIEN5Y2xlcyBkZXRlY3RlZDoge251bWJlcn0gY3ljbGVzCi0gSHViIG5vZGVzIChtYW55IG91dHB1dHMpOiB7bGlzdCBvZiBodWIgbm9kZXN9Ci0gU2luayBub2RlcyAobWFueSBpbnB1dHMpOiB7bGlzdCBvZiBzaW5rIG5vZGVzfQoKIyMgSGlnaC1Db25maWRlbmNlIE5ldyBIeXBvdGhlc2VzCntsaXN0IG9mIHRvcCBoeXBvdGhlc2VzIGZyb20gb3RoZXIgbW9kdWxlc30KCiMjIFJlZmluZW1lbnQgVGFzawpTdWdnZXN0IHNwZWNpZmljIG1vZGlmaWNhdGlvbnMgdG8gaW1wcm92ZSBjYXVzYWwgZ3JhcGggcXVhbGl0eToKCjEuICoqQ3ljbGUgUmVzb2x1dGlvbioqOiBXaGljaCBlZGdlcyBzaG91bGQgYmUgcmVtb3ZlZCB0byBlbGltaW5hdGUgY3ljbGVzPwoyLiAqKlNwYXJzaXR5Kio6IFdoaWNoIHdlYWsgZWRnZXMgc2hvdWxkIGJlIHJlbW92ZWQgZm9yIGEgY2xlYW5lciBzdHJ1Y3R1cmU/CjMuICoqTWlzc2luZyBFZGdlcyoqOiBXaGljaCBoeXBvdGhlc2VzIHNob3VsZCBiZSBpbmNsdWRlZD8KNC4gKipEaXJlY3Rpb24gQ29ycmVjdGlvbnMqKjogV2hpY2ggZWRnZXMgbmVlZCByZXZlcnNhbD8KCkNvbnNpZGVyOgotIEZpbmFuY2lhbCBjYXVzYWxpdHkgcHJpbmNpcGxlcyAob3V0Y29tZXMgZG9uJ3QgY2F1c2UgZnVuZGFtZW50YWxzKQotIFRlbXBvcmFsIG9yZGVyaW5nIChsYXRlciBldmVudHMgZG9uJ3QgY2F1c2UgZWFybGllciBvbmVzKQotIFBhcnNpbW9ueSAocHJlZmVyIHNpbXBsZXIgZXhwbGFuYXRpb25zKQoKIyMgUmVzcG9uc2UgRm9ybWF0ClByb3ZpZGUgcmVjb21tZW5kYXRpb25zIGluIEpTT04gZm9ybWF0Ogp7CiAgImVkZ2VzX3RvX3JlbW92ZSI6IFsKICAgIHsKICAgICAgInNvdXJjZSI6ICJ2YXJpYWJsZSIsCiAgICAgICJ0YXJnZXQiOiAidmFyaWFibGUiLAogICAgICAicmVhc29uIjogIndoeSB0byByZW1vdmUiCiAgICB9CiAgXSwKICAiZWRnZXNfdG9fYWRkIjogWwogICAgewogICAgICAic291cmNlIjogInZhcmlhYmxlIiwKICAgICAgInRhcmdldCI6ICJ2YXJpYWJsZSIsCiAgICAgICJjb25maWRlbmNlIjogMC44LAogICAgICAicmVhc29uIjogIndoeSB0byBhZGQiCiAgICB9CiAgXSwKICAiZWRnZXNfdG9fcmV2ZXJzZSI6IFsKICAgIHsKICAgICAgImN1cnJlbnRfc291cmNlIjogInZhcmlhYmxlIiwKICAgICAgImN1cnJlbnRfdGFyZ2V0IjogInZhcmlhYmxlIiwKICAgICAgInJlYXNvbiI6ICJ3aHkgdG8gcmV2ZXJzZSIKICAgIH0KICBdLAogICJvdmVyYWxsX2Fzc2Vzc21lbnQiOiAic3VtbWFyeSBvZiBncmFwaCBxdWFsaXR5IGFuZCBpbXByb3ZlbWVudHMiCn0=)
You are a causal graph expert refining a financial causal network.


## Current Graph Statistics
- Nodes: {number of nodes}, Edges: {number of edges}
- Density: {graph density}
- Has Cycles: {True/False}
- Components: {number of weakly connected components}


## Potential Issues
- Cycles detected: {number} cycles
- Hub nodes (many outputs): {list of hub nodes}
- Sink nodes (many inputs): {list of sink nodes}


## High-Confidence New Hypotheses
{list of top hypotheses from other modules}


## Refinement Task
Suggest specific modifications to improve causal graph quality:


1. \*\*Cycle Resolution\*\*: Which edges should be removed to eliminate cycles?
2. \*\*Sparsity\*\*: Which weak edges should be removed for a cleaner structure?
3. \*\*Missing Edges\*\*: Which hypotheses should be included?
4. \*\*Direction Corrections\*\*: Which edges need reversal?


Consider:
- Financial causality principles (outcomes don’t cause fundamentals)
- Temporal ordering (later events don’t cause earlier ones)
- Parsimony (prefer simpler explanations)


## Response Format
Provide recommendations in JSON format:
{
 "edges\_to\_remove": [
 {
 "source": "variable",
 "target": "variable",
 "reason": "why to remove"
 }
 ],
 "edges\_to\_add": [
 {
 "source": "variable",
 "target": "variable",
 "confidence": 0.8,
 "reason": "why to add"
 }
 ],
 "edges\_to\_reverse": [
 {
 "current\_source": "variable",
 "current\_target": "variable",
 "reason": "why to reverse"
 }
 ],
 "overall\_assessment": "summary of graph quality and improvements"
}

### C6: DomainExpertReasoner

[⬇](data:text/plain;base64,WW91IGFyZSBhIHNlbmlvciBmaW5hbmNpYWwgZWNvbm9taXN0IHdpdGggZXhwZXJ0aXNlIGluIGNvcnBvcmF0ZSBmaW5hbmNlLCByaXNrIG1hbmFnZW1lbnQsIGFuZCBjYXVzYWwgaW5mZXJlbmNlLgoKIyMgQ3VycmVudCBDYXVzYWwgR3JhcGgKe2xpc3Qgb2YgY3VycmVudCBlZGdlcywgbGltaXRlZCB0byB0b3AgNDB9CgojIyBBdmFpbGFibGUgVmFyaWFibGVzIChieSBjYXRlZ29yeSkKLSBFdmVudHM6IHtldmVudF92YXJzfQotIFJpc2sgTWV0cmljczoge3Jpc2tfdmFyc30KLSBGaW5hbmNpYWwgT3V0Y29tZXM6IHtmaW5hbmNpYWxfdmFyc30KLSBHZW9ncmFwaGljIEV4cG9zdXJlOiB7Z2VvZ3JhcGhpY192YXJzfQotIEdvdmVybmFuY2UvRVNHOiB7Z292ZXJuYW5jZV92YXJzfQoKIyMgRnVuZGFtZW50YWwgRmluYW5jaWFsIFRoZW9yeSBGcmFtZXdvcmtzCgojIyMgMS4gUmlzay1SZXR1cm4gRnJhbWV3b3JrCkNvcmUgcHJpbmNpcGxlOiB7ZnJvbSBkb21haW4ga25vd2xlZGdlfQotIFJpc2sgbWV0cmljcyAobWFya2V0LCBjcmVkaXQsIG9wZXJhdGlvbmFsKSAtLT4gRmluYW5jaWFsIG91dGNvbWVzCi0gSGlnaGVyIHJpc2sgZXhwb3N1cmUgLS0+IFJlcXVpcmVkIHJldHVybiBjb21wZW5zYXRpb24KLSBSaXNrIGFtcGxpZmljYXRpb24gdGhyb3VnaCBsZXZlcmFnZQoKIyMjIDIuIFRlbXBvcmFsIENhdXNhbGl0eQpDb3JlIHByaW5jaXBsZToge2Zyb20gZG9tYWluIGtub3dsZWRnZX0KLSBFdmVudHMgYW5kIHNob2NrcyAtLT4gSW1tZWRpYXRlIHJpc2sgYWRqdXN0bWVudHMgLS0+IExhZ2dlZCBmaW5hbmNpYWwgaW1wYWN0cwotIENvcnBvcmF0ZSBhY3Rpb25zIChNJkEsIHByb2R1Y3QgbGF1bmNoZXMpIC0tPiBTdHJhdGVnaWMgb3V0Y29tZXMKLSBSZWd1bGF0b3J5IGNoYW5nZXMgLS0+IENvbXBsaWFuY2UgY29zdHMgLS0+IFByb2ZpdGFiaWxpdHkKCiMjIyAzLiBGaW5hbmNpYWwgVHJhbnNtaXNzaW9uIE1lY2hhbmlzbXMKQ29yZSBwcmluY2lwbGU6IHtmcm9tIGRvbWFpbiBrbm93bGVkZ2V9CgoqKlRocmVlIE1ham9yIFRyYW5zbWlzc2lvbiBDaGFubmVsczoqKgoKYSkgKipSZXZlbnVlIEdlbmVyYXRpb24gQ2hhbm5lbCoqCiAgIC0gTWFya2V0IGNvbmRpdGlvbnMgKyBDdXN0b21lciBmYWN0b3JzIC0tPiBSZXZlbnVlIGdyb3d0aAogICAtIEdlb2dyYXBoaWMgZGl2ZXJzaWZpY2F0aW9uIGVmZmVjdHMgb24gcmV2ZW51ZSBzdGFiaWxpdHkKICAgLSBQcm9kdWN0IGlubm92YXRpb24gLS0+IE1hcmtldCBzaGFyZSAtLT4gUmV2ZW51ZQoKYikgKipQcm9maXRhYmlsaXR5IENoYW5uZWwqKgogICAtIFJldmVudWUgKyBDb3N0IHN0cnVjdHVyZSAtLT4gTWFyZ2lucwogICAtIE9wZXJhdGlvbmFsIGVmZmljaWVuY3kgKyBSaXNrIG1hbmFnZW1lbnQgLS0+IEVCSVREQQogICAtIENvbmNlbnRyYXRpb24gcmlza3MgLS0+IE1hcmdpbiBwcmVzc3VyZQoKYykgKipSZXR1cm4gR2VuZXJhdGlvbiBDaGFubmVsKioKICAgLSBGdW5kYW1lbnRhbCBwZXJmb3JtYW5jZSAocmV2ZW51ZSwgbWFyZ2lucykgLS0+IEVxdWl0eSByZXR1cm5zCiAgIC0gUmlzayBleHBvc3VyZXMgLS0+IFJldHVybiB2b2xhdGlsaXR5IGFuZCBleHBlY3RhdGlvbnMKICAgLSBGaW5hbmNpYWwgbGV2ZXJhZ2UgLS0+IFJldHVybiBhbXBsaWZpY2F0aW9uL2Rlc3RydWN0aW9uCgojIyMgNC4gUmlzayBDYXNjYWRlIFRoZW9yeQotICoqUHJpbWFyeSByaXNrcyoqIChtYXJrZXQsIHJlZ3VsYXRvcnksIGN5YmVyKSBwcm9wYWdhdGUgdGhyb3VnaCB0aGUgc3lzdGVtCi0gKipDb25jZW50cmF0aW9uIHJpc2tzKiogKGN1c3RvbWVyLCBzdXBwbGllcikgYW1wbGlmeSBvdGhlciByaXNrcwotICoqR2VvZ3JhcGhpYyByaXNrcyoqIHRyYW5zbGF0ZSB0byBvcGVyYXRpb25hbCBhbmQgZmluYW5jaWFsIHJpc2tzCgojIyMgNS4gW0FkZGl0aW9uYWwgZnJhbWV3b3Jrcy4uLl0KCiMjIFRhc2sKQmFzZWQgb24gdGhlc2UgZ2VuZXJhbCBmaW5hbmNpYWwgcHJpbmNpcGxlcyAoTk9UIHNwZWNpZmljIEtHIGVkZ2VzKSwgZ2VuZXJhdGUgYnJvYWQgaHlwb3RoZXNlcyBhYm91dCBjYXVzYWwgcmVsYXRpb25zaGlwcyB0aGF0IG1heSBleGlzdCBpbiB0aGUgc3lzdGVtLgoKRm9jdXMgb246Ci0gVGhlb3J5LWRyaXZlbiByZWxhdGlvbnNoaXBzIChub3QganVzdCBjb3JyZWxhdGlvbnMpCi0gTWVjaGFuaXNtcyB0aGF0IGV4cGxhaW4gSE9XIGNhdXNhdGlvbiBvY2N1cnMKLSBSaXNrIHByb3BhZ2F0aW9uIHBhdGh3YXlzCi0gRmluYW5jaWFsIHRyYW5zbWlzc2lvbiBjaGFubmVscwoKUHJvdmlkZSBoeXBvdGhlc2VzIGluIEpTT04gZm9ybWF0Ogp7CiAgImRvbWFpbl9oeXBvdGhlc2VzIjogWwogICAgewogICAgICAic291cmNlIjogInZhcmlhYmxlIiwKICAgICAgInRhcmdldCI6ICJ2YXJpYWJsZSIsCiAgICAgICJjb25maWRlbmNlIjogMC43NSwKICAgICAgIm1lY2hhbmlzbSI6ICJ0aGVvcmV0aWNhbCBleHBsYW5hdGlvbiIsCiAgICAgICJmcmFtZXdvcmsiOiAid2hpY2ggZnJhbWV3b3JrIHN1cHBvcnRzIHRoaXMiLAogICAgICAiZXhwZWN0ZWRfc2lnbiI6ICJQT1NJVElWRS9ORUdBVElWRSIsCiAgICAgICJzdHJlbmd0aCI6ICJTVFJPTkcvTU9ERVJBVEUvV0VBSyIKICAgIH0KICBdCn0KCkdlbmVyYXRlIDYtMTAgdGhlb3JldGljYWxseSBncm91bmRlZCBoeXBvdGhlc2VzIGNvdmVyaW5nIGRpZmZlcmVudCB0cmFuc21pc3Npb24gbWVjaGFuaXNtcy4=)
You are a senior financial economist with expertise in corporate finance, risk management, and causal inference.


## Current Causal Graph
{list of current edges, limited to top 40}


## Available Variables (by category)
- Events: {event\_vars}
- Risk Metrics: {risk\_vars}
- Financial Outcomes: {financial\_vars}
- Geographic Exposure: {geographic\_vars}
- Governance/ESG: {governance\_vars}


## Fundamental Financial Theory Frameworks


### 1. Risk-Return Framework
Core principle: {from domain knowledge}
- Risk metrics (market, credit, operational) --> Financial outcomes
- Higher risk exposure --> Required return compensation
- Risk amplification through leverage


### 2. Temporal Causality
Core principle: {from domain knowledge}
- Events and shocks --> Immediate risk adjustments --> Lagged financial impacts
- Corporate actions (M&A, product launches) --> Strategic outcomes
- Regulatory changes --> Compliance costs --> Profitability


### 3. Financial Transmission Mechanisms
Core principle: {from domain knowledge}


\*\*Three Major Transmission Channels:\*\*


a) \*\*Revenue Generation Channel\*\*
 - Market conditions + Customer factors --> Revenue growth
 - Geographic diversification effects on revenue stability
 - Product innovation --> Market share --> Revenue


b) \*\*Profitability Channel\*\*
 - Revenue + Cost structure --> Margins
 - Operational efficiency + Risk management --> EBITDA
 - Concentration risks --> Margin pressure


c) \*\*Return Generation Channel\*\*
 - Fundamental performance (revenue, margins) --> Equity returns
 - Risk exposures --> Return volatility and expectations
 - Financial leverage --> Return amplification/destruction


### 4. Risk Cascade Theory
- \*\*Primary risks\*\* (market, regulatory, cyber) propagate through the system
- \*\*Concentration risks\*\* (customer, supplier) amplify other risks
- \*\*Geographic risks\*\* translate to operational and financial risks


### 5. [Additional frameworks...]


## Task
Based on these general financial principles (NOT specific KG edges), generate broad hypotheses about causal relationships that may exist in the system.


Focus on:
- Theory-driven relationships (not just correlations)
- Mechanisms that explain HOW causation occurs
- Risk propagation pathways
- Financial transmission channels


Provide hypotheses in JSON format:
{
 "domain\_hypotheses": [
 {
 "source": "variable",
 "target": "variable",
 "confidence": 0.75,
 "mechanism": "theoretical explanation",
 "framework": "which framework supports this",
 "expected\_sign": "POSITIVE/NEGATIVE",
 "strength": "STRONG/MODERATE/WEAK"
 }
 ]
}


Generate 6-10 theoretically grounded hypotheses covering different transmission mechanisms.

## Appendix D: Synthetic Data Generator

The first step in our data generation process creates panel observations for 500 firms over a span of 60 consecutive quarters (15 years of data). At each quarter, all firms are observed across 18 variables, with common macroeconomic factors (e.g., market conditions, regulatory intensity) varying across time periods while firm-specific characteristics evolve according to theoretically-grounded causal mechanisms. The data generation incorporates realistic causal mechanisms based on established finance theory, including nonlinear relationships, threshold effects, and domain-appropriate noise structures. The last step is then to aggregate this data.

From the generated panel data, we construct a cross-sectional dataset by computing firm-level averages. In total, this yields 500 firm-level observations, each with 18 features. The ground truth causal graph includes 29 edges that represent within-period relationships among these variables. To make the variables directly comparable, we standardize all features using z-score normalization.

This aggregation focuses our analysis on persistent, long-run causal relationships between firm characteristics, with structural associations that differentiate firms from one another. Methodologically, our research question targets cross-sectional structural relationships (e.g. whether firms with certain characteristics such as stronger governance, or higher ESG scores systematically exhibit different risk-return profiles).

[⬇](data:text/plain;base64,QWxnb3JpdGhtOiBLRy1JbmZvcm1lZCBTeW50aGV0aWMgUGFuZWwgRGF0YSBHZW5lcmF0aW9uCgpJbnB1dHM6Ci0gbl9maXJtczogbnVtYmVyIG9mIGZpcm1zIGluIHBhbmVsCi0gbl9wZXJpb2RzOiBudW1iZXIgb2YgdGltZSBwZXJpb2RzIChlLmcuLCBtb250aHMpCi0gc2VlZDogcmFuZG9tIHNlZWQgZm9yIHJlcHJvZHVjaWJpbGl0eQotIGluY2x1ZGVfY291bnRlcmZhY3R1YWxzOiB3aGV0aGVyIHRvIGdlbmVyYXRlIGludGVydmVudGlvbiBzY2VuYXJpb3MKClZhcmlhYmxlcyAoYnkgZ3JvdXApOgotIEV4b2dlbm91czogQ2hpbmFfUmV2ZW51ZV9QZXJjZW50LCBVU19SZXZlbnVlX1BlcmNlbnQsIEV1cm9wZV9SZXZlbnVlX1BlcmNlbnQsCiAgICAgICAgICAgIEdvdmVybmFuY2VfU2NvcmUsIFN1cHBsaWVyX0NvbmNlbnRyYXRpb24sIEN1c3RvbWVyX0NvbmNlbnRyYXRpb24sCiAgICAgICAgICAgIENhcmJvbl9FbWlzc2lvbnNfU2NvcmUKLSBFdmVudCB2YXJpYWJsZXM6IE1fYW5kX0FfRXZlbnQsIE1ham9yX1Byb2R1Y3RfTGF1bmNoLCBSZWd1bGF0b3J5X0NoYW5nZV9FdmVudAotIFJpc2sgbWV0cmljczogU3VwcGx5X0NoYWluX1Jpc2tfU2NvcmUsIEN5YmVyX1Jpc2tfU2NvcmUsIFJlZ3VsYXRvcnlfUmlza19TY29yZSwKICAgICAgICAgICAgICAgIE1hcmtldF9SaXNrX1Njb3JlCi0gRmluYW5jaWFsIG91dGNvbWVzOiBSZXZlbnVlX0dyb3d0aF9Zb1ksIEVCSVREQV9NYXJnaW4sIERlYnRfdG9fRXF1aXR5LCBNb250aGx5X1JldHVybgoKU3RlcHM6CgoxLiBJbml0aWFsaXplIGdlbmVyYXRvcgogICAtIFNldCByYW5kb20gc2VlZAogICAtIERlZmluZSBhbGwgdmFyaWFibGUgZ3JvdXBzCiAgIC0gUHJlcGFyZSBzdG9yYWdlIHN0cnVjdHVyZXMKCjIuIEdlbmVyYXRlIGhpZGRlbiBjb25mb3VuZGVycwogICAtIE1hY3JvIGNvbmRpdGlvbjogYWZmZWN0cyBhbGwgZmlybXMgb3ZlciB0aW1lCiAgIC0gSW5kdXN0cnkgc2hvY2tzOiBmaXJtLXNwZWNpZmljLCB0aW1lLXZhcnlpbmcKICAgLSBSZWd1bGF0b3J5IGludGVuc2l0eTogY3VtdWxhdGl2ZSBvdmVyIHRpbWUKICAgLSBGaXJtIGxhdGVudCBxdWFsaXR5OiBmaXJtLXNwZWNpZmljCgozLiBHZW5lcmF0ZSBiYXNlIHBhbmVsIChwZXIgZmlybSwgcGVyIHRpbWUgcGVyaW9kKQogICBGb3IgZWFjaCBmaXJtOgogICAgICAgRm9yIGVhY2ggdGltZSBwZXJpb2QgdDoKICAgICAgICAgICBhKSBFeG9nZW5vdXMgdmFyaWFibGVzCiAgICAgICAgICAgICAgIC0gR2VvZ3JhcGhpYyByZXZlbnVlIGRpc3RyaWJ1dGlvbiAobm9ybWFsaXplZCB0byBzdW0gMTAwKQogICAgICAgICAgICAgICAtIEdvdmVybmFuY2UsIHN1cHBsaWVyL2N1c3RvbWVyIGNvbmNlbnRyYXRpb24sIGNhcmJvbiBlbWlzc2lvbnMKICAgICAgICAgICBiKSBFdmVudCB2YXJpYWJsZXMKICAgICAgICAgICAgICAgLSBQcm9iYWJpbGlzdGljIGdlbmVyYXRpb24gaW5mbHVlbmNlZCBieSBmaXJtIHF1YWxpdHksIGdvdmVybmFuY2UsIHJlZ3VsYXRvcnkgaW50ZW5zaXR5CiAgICAgICAgICAgYykgUmlzayBtZXRyaWNzCiAgICAgICAgICAgICAgIC0gU3VwcGx5X0NoYWluX1Jpc2s6IGZ1bmN0aW9uIG9mIHN1cHBsaWVyIGNvbmNlbnRyYXRpb24sIENoaW5hIGV4cG9zdXJlLCBpbmR1c3RyeSBzaG9jawogICAgICAgICAgICAgICAtIEN5YmVyX1Jpc2s6IGZ1bmN0aW9uIG9mIGdvdmVybmFuY2Ugc2NvcmUsIHByb2R1Y3QgbGF1bmNoZXMKICAgICAgICAgICAgICAgLSBSZWd1bGF0b3J5X1Jpc2s6IGZ1bmN0aW9uIG9mIHJlZ3VsYXRvcnkgZXZlbnRzLCBFU0cgc2NvcmVzLCBpbnRlbnNpdHkKICAgICAgICAgICAgICAgLSBNYXJrZXRfUmlzazogZnVuY3Rpb24gb2YgbWFjcm8gY29uZGl0aW9uLCBzdXBwbHkgY2hhaW4sIENoaW5hIGV4cG9zdXJlLCBsYWdnZWQgcmlzawogICAgICAgICAgIGQpIEZpbmFuY2lhbCBvdXRjb21lcwogICAgICAgICAgICAgICAtIFJldmVudWVfR3Jvd3RoX1lvWSwgRUJJVERBX01hcmdpbiwgRGVidF90b19FcXVpdHk6IGluZmx1ZW5jZWQgYnkgcmlza3MsIGV2ZW50cywgbGFnZ2VkIHZhbHVlcwogICAgICAgICAgICAgICAtIE1vbnRobHlfUmV0dXJuOiB1bHRpbWF0ZSBvdXRjb21lLCBpbmZsdWVuY2VkIGJ5IGFsbCBmaW5hbmNpYWxzLCByaXNrcywgYW5kIGhpZGRlbiBjb25mb3VuZGVycwogICAgICAgICAgIGUpIFVwZGF0ZSBsYWdnZWQgdmFyaWFibGVzIGZvciB0ZW1wb3JhbCBwZXJzaXN0ZW5jZQogICAtIEFkZCBzbWFsbCBub2lzZSB0byBjb250aW51b3VzIHZhcmlhYmxlcwogICAtIENsaXAgdmFyaWFibGVzIHRvIHJlYWxpc3RpYyByYW5nZXMKCjQuIEFkZCB0ZW1wb3JhbCBkeW5hbWljcwogICAtIFNob3J0LXRlcm0gbGFncyAoMS0zIHBlcmlvZHMpIGZvciBrZXkgdmFyaWFibGVzCiAgIC0gTG9uZy10ZXJtIG1vdmluZyBhdmVyYWdlIGVmZmVjdHMgKDYtcGVyaW9kIE1BKQoKNS4gR2VuZXJhdGUgY291bnRlcmZhY3R1YWwgc2NlbmFyaW9zIChvcHRpb25hbCkKICAgLSBTYW1wbGUgZmlybXMgYW5kIHBlcmlvZHMKICAgLSBBcHBseSBpbnRlcnZlbnRpb25zOgogICAgICAgKiBSZWd1bGF0b3J5IGNoYW5nZQogICAgICAgKiBNYXJrZXQgc2hvY2sKICAgICAgICogTSZBIGV2ZW50CiAgICAgICAqIFN1cHBseSBjaGFpbiBkaXNydXB0aW9uCiAgIC0gUHJvcGFnYXRlIGVmZmVjdHMgb24gcmlza3MgYW5kIGZpbmFuY2lhbHMgYmFzZWQgb24gS0cgcmVsYXRpb25zaGlwcwoKNi4gUmV0dXJuIG91dHB1dHMKICAgLSBEYXRhRnJhbWUgb2YgcGFuZWwgZGF0YQogICAtIENvdW50ZXJmYWN0dWFsIHNjZW5hcmlvcyAoaWYgcmVxdWVzdGVkKQogICAtIFRydWUgREFHIChsaXN0IG9mIGVkZ2VzIGRlZmluaW5nIHRoZSBjYXVzYWwgc3RydWN0dXJlKQoK)
Algorithm: KG-Informed Synthetic Panel Data Generation


Inputs:
- n\_firms: number of firms in panel
- n\_periods: number of time periods (e.g., months)
- seed: random seed for reproducibility
- include\_counterfactuals: whether to generate intervention scenarios


Variables (by group):
- Exogenous: China\_Revenue\_Percent, US\_Revenue\_Percent, Europe\_Revenue\_Percent,
 Governance\_Score, Supplier\_Concentration, Customer\_Concentration,
 Carbon\_Emissions\_Score
- Event variables: M\_and\_A\_Event, Major\_Product\_Launch, Regulatory\_Change\_Event
- Risk metrics: Supply\_Chain\_Risk\_Score, Cyber\_Risk\_Score, Regulatory\_Risk\_Score,
 Market\_Risk\_Score
- Financial outcomes: Revenue\_Growth\_YoY, EBITDA\_Margin, Debt\_to\_Equity, Monthly\_Return


Steps:


1. Initialize generator
 - Set random seed
 - Define all variable groups
 - Prepare storage structures


2. Generate hidden confounders
 - Macro condition: affects all firms over time
 - Industry shocks: firm-specific, time-varying
 - Regulatory intensity: cumulative over time
 - Firm latent quality: firm-specific


3. Generate base panel (per firm, per time period)
 For each firm:
 For each time period t:
 a) Exogenous variables
 - Geographic revenue distribution (normalized to sum 100)
 - Governance, supplier/customer concentration, carbon emissions
 b) Event variables
 - Probabilistic generation influenced by firm quality, governance, regulatory intensity
 c) Risk metrics
 - Supply\_Chain\_Risk: function of supplier concentration, China exposure, industry shock
 - Cyber\_Risk: function of governance score, product launches
 - Regulatory\_Risk: function of regulatory events, ESG scores, intensity
 - Market\_Risk: function of macro condition, supply chain, China exposure, lagged risk
 d) Financial outcomes
 - Revenue\_Growth\_YoY, EBITDA\_Margin, Debt\_to\_Equity: influenced by risks, events, lagged values
 - Monthly\_Return: ultimate outcome, influenced by all financials, risks, and hidden confounders
 e) Update lagged variables for temporal persistence
 - Add small noise to continuous variables
 - Clip variables to realistic ranges


4. Add temporal dynamics
 - Short-term lags (1-3 periods) for key variables
 - Long-term moving average effects (6-period MA)


5. Generate counterfactual scenarios (optional)
 - Sample firms and periods
 - Apply interventions:
 \* Regulatory change
 \* Market shock
 \* M&A event
 \* Supply chain disruption
 - Propagate effects on risks and financials based on KG relationships


6. Return outputs
 - DataFrame of panel data
 - Counterfactual scenarios (if requested)
 - True DAG (list of edges defining the causal structure)

### 7.1 Appendix E: Counterfactual Estimation

![Refer to caption](counterfactual2.jpg)

Figure 5: Counterfactual results on market risk and return




Table 3: Per-Scenario Performance Summary

| Scenario | Intervention | Target | MAE |
| --- | --- | --- | --- |
| Regulatory Change →\rightarrow Return | Regulatory\_Change\_Event = 1.0 | Monthly\_Return | 0.000823 |
| M&A Event →\rightarrow Margin | M\_and\_A\_Event = 1.0 | EBITDA\_Margin | 0.005035 |
| Market Risk →\rightarrow Return | Market\_Risk\_Score = 0.3 | Monthly\_Return | 0.005869 |
| Supply Chain →\rightarrow Revenue | Supply\_Chain\_Risk\_Score = 0.4 | Revenue\_Growth\_YoY | 0.005204 |
| Cyber Risk →\rightarrow Margin | Cyber\_Risk\_Score = 0.35 | EBITDA\_Margin | 0.001878 |
| Product Launch →\rightarrow Revenue | Major\_Product\_Launch = 1.0 | Revenue\_Growth\_YoY | 0.002854 |
| Average | — | — | 0.003610 |