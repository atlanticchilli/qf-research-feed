---
authors:
- Tamara Broderick
- Ali Jadbabaie
- Vanessa Lin
- Manuel Quintero
- Arnab Sarker
- Sean R. Sinclair
doc_id: arxiv:2511.05691v1
family_id: arxiv:2511.05691
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2511.05691v1
url_html: https://arxiv.org/html/2511.05691v1
venue: arXiv q-fin
version: 1
year: 2025
---

\EquationsNumberedThrough\TheoremsNumberedThrough\ECRepeatTheorems\MANUSCRIPTNO

MNSC-0001-2024.00

\RUNAUTHOR

Broderick et al.

\RUNTITLE

Network and Risk Analysis of Surety Bonds

\TITLE

Network and Risk Analysis of Surety Bonds

\ARTICLEAUTHORS

\AUTHOR

Tamara Broderick, Ali Jadbabaie, Vanessa Lin, Manuel Quintero, Arnab Sarker
\AFFInstitute for Data, Systems, and Society,
Massachusetts Institute of Technology,
  
Cambridge, MA 02139, \EMAIL{tamarab,jadbabaie,vllin,mquint,arnabs}@mit.edu

\AUTHOR

Sean R. Sinclair111Contact author
\AFFDepartment of Industrial Engineering and Management Sciences,
Northwestern University,
  
Evanston, IL 60208, \EMAILsean.sinclair@northwestern.edu

\ABSTRACT

Surety bonds are financial agreements between a contractor (principal) and obligee (project owner) to complete a project. However, most large-scale projects involve multiple contractors, creating a network and introducing the possibility of incomplete obligations to propagate and result in project failures. Typical models for risk assessment assume independent failure probabilities within each contractor. However, we take a network approach, modeling the contractor network as a directed graph where nodes represent contractors and project owners and edges represent contractual obligations with associated financial records. To understand risk propagation throughout the contractor network, we extend the celebrated Friedkin-Johnsen model and introduce a stochastic process to simulate principal failures across the network. From a theoretical perspective, we show that under natural monotonicity conditions on the contractor network, incorporating network effects leads to increases in both the average risk and the tail probability mass of the loss distribution (i.e. larger right-tail risk) for the surety organization. We further use data from a partnering insurance company to validate our findings, estimating an approximately 2% higher exposure when accounting for network effects.

\KEYWORDS

Surety bonds, Contractor network, Risk propagation, Systemic risk, Opinion dynamics

## 1 Introduction

Surety bonds are a foundational mechanism in contractual risk management, widely used to guarantee the completion of projects in sectors such as construction, infrastructure, and public works. In a typical surety agreement, the surety company guarantees to the obligee (the project owner) that the principal (a contractor) will fulfill the terms of a bonded contract. If the principal fails to perform, the surety must step in to ensure project completion, often absorbing substantial financial losses in the process (russell1990surety). These agreements are not only mandated for public contracts under laws such as the U.S. Miller Act of 1935 (uscode40\_3131), but also play a growing role in private-sector project financing (wambach2011surety). Despite their ubiquity, surety bonds remain difficult for contractors to secure, in part due to the unexpected and systemic nature of failures, which can leave insurers liable; for instance, there were over $21 billion in claims between 1990 and 1997 in the U.S. alone (wambach2011surety).

The pricing of surety bonds depends critically on the ability to assess the default risk of individual contractors. A large body of work in finance and insurance focuses on this task, estimating failure probabilities using firm-level covariates such as credit ratings, leverage ratios, and liquidity metrics (kim2019default). While such models (often using statistical machine learning) have improved the accuracy of idiosyncratic risk estimation, they share a key limitation: they assume failures occur independently across firms. This assumption neglects an increasingly salient feature of real-world contracting environments: network dependencies among contractors, subcontractors, and project owners (see [Fig. 1](https://arxiv.org/html/2511.05691v1#S1.F1 "In 1 Introduction") for a toy contractor network, later in [Section 5](https://arxiv.org/html/2511.05691v1#S5 "5 Numerical Results") we consider a real-world contractor network with ∼30,000\sim 30,000 organizations).
In practice, most large-scale projects involve multi-tiered contractual relationships, where the performance of one firm is contingent on the timely execution of work by others. As highlighted by recent industry reviews (assuredpartners2024surety, bci2021supplychain), subcontractor failure is one of the leading causes of bonded losses. For instance, if a plumbing contractor cannot begin work until the electrical subcontractor completes their portion of a build, the default of the latter creates a domino effect. In such environments, risk is not merely a function of a firm’s own characteristics, but also of its position in the broader contractor network. Moreover, these cascading effects are pervasive across domains. In supply chains, for example, the bankruptcy of an upstream supplier can cripple downstream production. In collaborative research, a delay in one lab’s work can stall the entire study. In interbank lending networks, financial contagion spreads through credit exposures. Across all these settings, a network-aware perspective is essential to understand and mitigate systemic risk.

![Refer to caption](x1.png)


Figure 1: Illustrated representation of a series of subcontractor dependencies. Here we observe that a failure of subcontractor A has the potential to propagate and affect C, and also the obligees D and E. Note that even though A does not work directly with D or E, the intermediary C allows them to influence the risk of project incompletion.

However, despite growing recognition of these interdependencies, there remains a lack of formal models that account for network effects in surety risk assessment. While prior work has examined dynamic models of credit contagion and equilibrium default (benzoni2015modeling, nickerson2017debt), these frameworks are often not tailored to the structure of bonded contractor networks, where obligations are directional. Notably, recent theoretical work in stochastic dynamics and mean-field models (amini2022dynamic, carmona2013mean) explores related ideas, but typically assumes irreversible failures or continuous-time evolution, and does not address the specific distributional shape of systemic losses, a critical consideration for insurers concerned about tail risk. Our work is motivated by this important gap. Namely, we seek to answer the following research questions:

How do contractor relationships influence systemic risk in surety-based contractor networks? What conditions lead to cascading failures, and how do these propagate over time? Can we identify key contractors whose failures disproportionately impact financial stability?

### 1.1 Main Contributions

#### Network-Based Model of Risk Propagation.

In an attempt to tackle these questions, one of the main contributions of this work is a network-based modeling framework for risk propagation in surety-based contractor networks. Traditional models like kim2019default assume independent failure probabilities, not capturing how failures spread through contractor relationships. Instead, we represent the contracting environment as a directed network G=(𝒱,ℰ)G=(\mathcal{V},\mathcal{E}), where nodes correspond to principals (contractors) and obligees (project owners), and edges capture the potential flow of risk through a contract for bonded work from principal to obligee. In contrast to network-unaware models of failure dynamics, we introduce a stochastic process 𝐗t=(Xit)i∈𝒱\mathbf{X}^{t}=(X\_{i}^{t})\_{i\in\mathcal{V}} which represents whether node i∈𝒱i\in\mathcal{V} in the network fails at timestep t∈ℕt\in\mathbb{N}. This stochastic process evolves according to the following simple dynamics (see [Eq. 1](https://arxiv.org/html/2511.05691v1#S2.E1 "In Stochastic Risk Propagation. ‣ 2 Network Model Definition")):

|  |  |  |
| --- | --- | --- |
|  | Xit+1=Bernoulli​((1−αi)​ri+αi​∑j∈δin​(i)wi​j​Xjt),X\_{i}^{t+1}=\textsf{Bernoulli}\Big((1-\alpha\_{i})r\_{i}+\alpha\_{i}\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}X\_{j}^{t}\Big), |  |

Here, rir\_{i} denotes the contractor’s idiosyncratic or individual risk score, αi\alpha\_{i} represents the probability that ii is affected by one of their neighbors, δin​(i)\delta\_{\text{in}}(i) is the set of in-neighbors to ii, and wi​jw\_{ij} is the fraction of ii’s projects that are contracted to principal jj. At t=0t=0, we set Xi0=Bernoulli​(ri)X\_{i}^{0}=\textsf{Bernoulli}(r\_{i}) to denote the “independent” failure model. However, as tt increases, we see that failures have the ability to propagate and affect their neighbors through the terms wi​j​Xjtw\_{ij}X\_{j}^{t}.
This framework generalizes standard independent failure models and allows for a more realistic assessment of systemic risk in these interdependent contracting environments, as we demonstrate in [Section 5](https://arxiv.org/html/2511.05691v1#S5 "5 Numerical Results").

#### Mean-Field and Limiting Distribution Analysis.

To understand how risk propagates in the network, we analyze the stationary distribution of the stochastic failure process XitX\_{i}^{t}. We start off by showing that the marginal failure probabilities mit=𝔼[Xit]m\_{i}^{t}=\mathbb{E}\mathopen{}\mathclose{{\left[X\_{i}^{t}}}\right] converge to a unique fixed point mim\_{i} as their limiting failure probability ([Section 3.1](https://arxiv.org/html/2511.05691v1#S3.SS1 "3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk")). This result generalizes the Friedkin-Johnsen model of opinion dynamics to a setting with heterogeneous bias parameters. We further quantify the rate of convergence, establishing an exponential decay in |mit−mi||m\_{i}^{t}-m\_{i}| governed by the operator norm of a squared weight-adjusted adjacency matrix, and additionally show that the convergence occurs in finite time for acyclic contractor networks ([Fig. 3](https://arxiv.org/html/2511.05691v1#S3.F3 "In 3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk")).

Building on the mean-field analysis, we next study the full joint distribution over failures. The stochastic process XitX\_{i}^{t} defines a Markov chain over {0,1}n\{0,1\}^{n}, where nn is the number of nodes (contractors and obligees) in the network. However, naive analysis will establish its convergence to the stationary distribution in 𝒪​(2n)\mathcal{O}(2^{n}) time (resnick2013adventures). In contrast, we show that in acyclic graphs, the convergence occurs in at most dd steps, where d>0d>0 is the length of the longest path in the network ([Definition 4.4](https://arxiv.org/html/2511.05691v1#S4.Thmtheorem4 "Definition 4.4 (In-neighbor layers) ‣ 4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process")). For general (not necessarily acyclic) networks, we leverage the structure of the stochastic process to show it admits a coupling. This allows us to develop a contraction-based analysis, and show that the rate of convergence scales logarithmically with respect to nn ([Section 4.1](https://arxiv.org/html/2511.05691v1#S4.SS1 "4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process")).
Together, these results characterize the stationary behavior of the failure stochastic process, and show that the stationary distribution can be simulated efficiently.

#### Structural Insights into Amplification of Systemic Risk.

Our modeling framework allows us to quantify how systemic risk is amplified by the network structure beyond what traditional independent risk models predict. The main insight of our analysis is we show that when obligees hire riskier contractors on average ([Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk")), which is often observed in contractor networks (dietz2018mitigating), both the expected failure probabilities ([Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk")) and the right-tail probability mass of the loss distribution ([Section 4.2](https://arxiv.org/html/2511.05691v1#S4.SS2 "4.2 Impact on Global Average Risk ‣ 4 Asymptotic Behavior of Stochastic Risk Process")) increase over time. To formalize this, we design a monotone coupling between the highly-correlated stochastic process to its mean-field, allowing us to show that these risk measures are stochastically dominated across time.
We further outline conditions ([Remark 3.2](https://arxiv.org/html/2511.05691v1#S3.Thmtheorem2 "Remark 3.2 ‣ 3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk")) such that the total risk and loss in the network is strictly larger ([Remark 3.2](https://arxiv.org/html/2511.05691v1#S3.Thmtheorem2 "Remark 3.2 ‣ 3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk")). With this analysis we observe that contractor failures are not uniformly impactful—intermediary nodes, which serve as bridges between multiple principals and obligees, are the primary drivers behind the propagation of project incompletion across the network. In essence, by accounting for network effects, we see that surety organizations may be fundamentally underestimating how risky a contractor network is.
Lastly, we define an eigenvalue centrality ([Definition 3.1](https://arxiv.org/html/2511.05691v1#S3.Thmtheorem1 "Definition 3.1 ‣ 3.2 Identifying the Impact of Network Structure ‣ 3 Mean Field Analysis of Expected Risk")) that captures the extent to which a contractor’s risk influences the broader network through downstream intermediaries.
To summarize, our results formally characterize when and how network structure exacerbates risk.

#### Empirical Validation and Risk Estimation.

We validate our theoretical findings using anonymized real-world surety bond data from a partnering insurance firm. Our empirical analysis shows that accounting for network dependencies leads to a 2% higher estimated systemic risk compared to traditional models that assume independent contractor failures, and that the distribution of losses exhibits larger right tails, underscoring the potential for more severe extreme events. We further develop a methodology for identifying critical nodes (contractors whose failures have large effects on the network’s overall stability) and illustrate this with a detailed case study.
Together, these insights provide methodology and actionable recommendations for insurance providers and policymakers seeking to better anticipate and mitigate systemic risk in contractor networks.

#### Paper Organization.

We review the related literature in the remainder of this section. We formally present our model in [Section 2](https://arxiv.org/html/2511.05691v1#S2 "2 Network Model Definition"). In [Section 3](https://arxiv.org/html/2511.05691v1#S3 "3 Mean Field Analysis of Expected Risk") we analyze the mean failure probabilities, establishing the rate of convergence to their limits. Then, in [Section 4](https://arxiv.org/html/2511.05691v1#S4 "4 Asymptotic Behavior of Stochastic Risk Process") we analyze the mixing time of our stochastic process. Under both sections we provide insights into risk propagation due to network structure. Finally, in [Section 5](https://arxiv.org/html/2511.05691v1#S5 "5 Numerical Results") we complement our theoretical results on real-world data from our partnering surety organization, and conclude in [Section 6](https://arxiv.org/html/2511.05691v1#S6 "6 Conclusion"). When omitted, all proofs are deferred to the appendix.

### 1.2 Related Literature

Our work lies at the intersection of operations research, economics, applied probability, and network analysis, with close connections to models of financial contagion and surety risk. See caccioli2018network for a broad survey.

#### Empirical Studies in Surety Bonds.

Surety bonds are a widely adopted mechanism to protect against contractor defaults and offer several advantages over traditional insurance (schubert2002point). Surety bonds are typically priced using firm-level information such as financial ratios or credit data (schubert2002point, kim2019default). A large empirical literature applies statistical and machine learning methods, including logit regression (tserng2014prediction), SVMs (tserng2011svm, horta2013company), ensemble learning (choi2018predicting), and Bayesian networks (cao\_2022), to estimate individual contractors’ default probabilities from accounting data (barboza2017machine, nguyen2025bankruptcy, shumway2001forecasting, vassalou2004default). Although some models incorporate macroeconomic covariates (shumway2001forecasting, vassalou2004default), all of this literature treats contractors as independent units, with no mechanism by which one contractor’s failure propagates to others.

In practice, however, systemic factors and subcontracting dependencies create correlations in defaults. Historical events such as the 1980s oil embargo led to widespread contractor failures despite strong individual credit profiles (russell1990surety), and modern construction projects often hinge on “lower-tier” subcontractors, whose disruptions can cascade through the supply chain (dietz2018mitigating, bci2021supplychain). Motivated by these limitations, our model augments contractor-level default estimates from the existing literature with network interactions, capturing how contractual ties generate correlated risks and amplify potential losses.

#### Financial Contagion and Cascade Models.

Much of the contagion literature studies interbank lending. An early contribution is allenFinancialContagion2000, who model contagion as an equilibrium phenomenon in interbank markets, where small liquidity shocks can spread through overlapping claims. Subsequent work often uses threshold models in which a node defaults once losses from its neighbors exceed a threshold (watts2002simple, gai2010contagion, elliott2014financial, acemoglu2015systemic). These frameworks highlight how localized shocks can spread systemically, but their dynamics are typically deterministic and tied to an initial shock event. More recent analyses consider noisy threshold contagion, where a small probability of below-threshold adoption can accelerate the spread of complex contagion (ecklesLongTiesAccelerate2024). Unlike threshold contagion models that assume diminishing returns from additional affected neighbors, our model is stochastic and cumulative: a contractor’s failure risk grows as an aggregate function of weighted neighbor defaults and an idiosyncratic baseline.

Other extensions consider multilayer contagion with mutations, where new strains can emerge as the process spreads and heterogeneity across layers (e.g., schools, workplaces) shapes transmission (SoodSridhar2023). This underscores how ignoring heterogeneity in either the contagion type or the network structure can miscalculate systemic risk. In our setting, the analogous challenge is to capture heterogeneity in contractor obligations and recovery, rather than multilayer or mutating contagions.

A further distinction is that most threshold models assume that failed institutions remain insolvent, whereas in surety settings, defaults trigger intervention from the surety organization to ensure project completion. Models with recovery or stochasticity include recovery in reinsurance networks (klages2020cascading), Gaussian noise in asset values (ramirez2023stochastic), and dynamic link formation with Cramér–Lundberg premiums/claims (amini2022dynamic). However, these approaches rely on explicit thresholds or detailed balance-sheet information uncommon for bonded contractors. Instead, we propose a stochastic cascade model with heterogeneous exposures and explicit recovery, tailored to contractor–surety networks.

davis2001infectious introduce an alternative to threshold contagion by modeling “infectious” defaults, where bonds fail independently or through Bernoulli contagion within a sector. This framework shares similarities with our approach in that defaults can arise either idiosyncratically or via neighbors, but it assumes uniform exposures and fully connected networks. Moreover, it lacks recovery, which are central in the surety context. Our model builds on this probabilistic contagion idea while incorporating heterogeneity in network structure, firm characteristics, and explicit recovery.

#### Opinion Dynamics.

Opinion dynamics provides a natural basis for modeling failure cascades, where contractors correspond to individuals, and default probabilities correspond to opinions. A central feature is neighbor influence, allowing local shocks to generate global effects across the network. For instance, benzoni2015modeling show how investors’ beliefs about bond pricing can propagate through financial networks in ways that resemble contagion. A well-known framework is the Friedkin–Johnsen model, in which agents reconcile their intrinsic beliefs with their neighbors’ views (FriedkinJohnsen). Our model has a similar structure: defaults may be triggered by neighbors but are also shaped by inherent contractor-level failure probabilities. In fact, the mean-field of our stochastic process corresponds to a variation of the Friedkin–Johnsen model when opinions are reinterpreted as default probabilities (see [Section 3.1](https://arxiv.org/html/2511.05691v1#S3.SS1 "3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk")). Related extensions, such as the interacting Pólya Urn model of tang2024estimating, further highlight how noisy observations and social pressure interact with intrinsic beliefs.

#### Eigenvalue Centralities.

The Friedkin–Johnsen model is closely connected to eigenvector-based centrality measures such as Bonacich centrality and PageRank. Namely, bonacich2001eigenvector highlight that Bonacich centrality can be applied to the same situations as the Friedkin-Johnsen model, with the distinction that the latter is concerned with the limiting state, while Bonacich centrality quantifies the level of influence each node has on the final equilibrium. This centrality is analogous to the equilibrium output in response to a shock in the input-output model introduced by leontief1986input and appears in other settings in the economics literature. For example, acemoglu2012network studies a network of production sectors and shows that the volatility of aggregate output scales with the size of an eigenvector-based centrality vector that is closely related to Bonacich centrality. A special class of the Friedkin-Johnsen model also coincides with the teleportation model of random surfing introduced by page1999pagerank, proskurnikov2016pagerank.

In financial settings, battiston2012debtrank propose DebtRank, an eigenvector-based measure of systemic importance in interbank lending. While their measure prevents risk from being transmitted multiple times along cycles, in surety networks repeated impacts of earlier failures are precisely what matter. For this reason, we use an eigenvector-based centrality as a complement to our stochastic model, capturing how individual risks amplify through contractual ties (see [Section 3.2](https://arxiv.org/html/2511.05691v1#S3.SS2 "3.2 Identifying the Impact of Network Structure ‣ 3 Mean Field Analysis of Expected Risk")).

## 2 Network Model Definition

#### Technical notation.

In what follows, for N∈ℕ+N\in\mathbb{N}\_{+}, we let [N]={1,2,…,N}[N]=\{1,2,\ldots,N\}. For a vector 𝐱\mathbf{x} we use ∥𝐱∥\lVert\mathbf{x}\rVert to be its ℓ∞\ell\_{\infty} norm, i.e. ∥𝐱∥=maxi⁡|xi|\lVert\mathbf{x}\rVert=\max\_{i}|x\_{i}|, and for a matrix 𝐀\mathbf{A} we use ∥𝐀∥\lVert\mathbf{A}\rVert to denote the ℓ∞\ell\_{\infty}-induced matrix norm, i.e. ∥𝐀∥=sup{∥𝐀𝐱∥:∥𝐱∥≤1}\lVert\mathbf{A}\rVert=\sup\{\lVert\mathbf{A}\mathbf{x}\rVert\,:\,\lVert\mathbf{x}\rVert\leq 1\}. For two vectors 𝐱\mathbf{x} and 𝐲\mathbf{y} we write 𝐱≥𝐲\mathbf{x}\geq\mathbf{y} to denote the inequality holds entrywise. See [Table 2](https://arxiv.org/html/2511.05691v1#S7.T2 "In 7 Table of Notation") (appendix) for a full table of notation.

#### Model primitives.

We consider a large-scale network of contracts (edges) between contractors and project owners (nodes). We represent this system as a directed graph G=(𝒱,ℰ)G=(\mathcal{V},\mathcal{E}), referred to as the contractor network, where each node i∈𝒱i\in\mathcal{V} corresponds to an organization (subcontractor), a sub-unit within an organization, a project owner (general contractor), or a collection thereof. Throughout, let n=|𝒱|n=|\mathcal{V}| denote the total number of nodes (equivalently, the number of contractors/project owners) in the graph. Directed edges e=(j,i)∈ℰe=(j,i)\in\mathcal{E} represent one or more bonded contracts from principal jj (the contractor) to obligee ii (the project owner). These edges can capture an entire portfolio of contracts issued from jj to ii, or a single agreement. Multiple edges are not permitted, though self-loops and cycles are allowed.222Self-loops may seem superfluous, but it is often the case that one arm of an organization subcontracts to another arm of the same organization. Crucially, a self-loop feeds the consequences of a default back into the same contractor one time-step later: node ii failing at time tt raises the likelihood that ii again defaults at t+1t+1. Nodes may act as both principals and obligees, and thus can have both incoming and outgoing edges. For notational convenience, we define the edge direction from jj to ii, indicating the flow of bonded obligations from contractor to project owner; this also aligns with the flow of risk in the network, which moves in the opposite direction of payment. Each edge e=(j,i)e=(j,i) is associated with a weight wi​jw\_{ij}, denoting the total fraction of ii’s projects that are subcontracted to principal jj. By construction, the incoming weights for any obligee sum to one. We let 𝐖\mathbf{W} denote the weighted adjacency matrix, with entries 𝐖i​j=wi​j\mathbf{W}\_{ij}=w\_{ij}, and use δin​(i)={j∣(j,i)∈ℰ}\delta\_{\text{in}}(i)=\{j\mid(j,i)\in\mathcal{E}\} and δout​(i)={k∣(i,k)∈ℰ}\delta\_{\text{out}}(i)=\{k\mid(i,k)\in\mathcal{E}\} to denote the incoming and outgoing neighborhoods of node ii, respectively.

A node i∈𝒱i\in\mathcal{V} is said to be a pure principal if δin​(i)=0\delta\_{\text{in}}(i)=0. This corresponds to organizations that only act as subcontractors to other obligees, and do not have any bonded work that is deferred to lower tier subcontractors. Similarly, a node i∈𝒱i\in\mathcal{V} is said to be a pure obligee if δout​(i)=0\delta\_{\text{out}}(i)=0.
In practice, pure obligees typically represent project owners such as municipal agencies that contract with a single general contractor or construction manager. Their indegree is usually one, reflecting the primary contractor that organizes the project on their behalf.
Any other nodes ii are said to be intermediaries. (See [Fig. 1](https://arxiv.org/html/2511.05691v1#S1.F1 "In 1 Introduction") for a representation of the three classes of contractors.)
If the graph contains only pure principals and pure obligees, it is bipartite and the flow of risk is straightforward to characterize; principals affect only their obligees, and obligees are influenced only by their principals. However, if the contracting network contains an intermediary, the risk exposure it imposes on its obligees is dependent on its principals, because it relies on principals to complete some of its obligations. This creates opportunities for risk to flow in unexpected ways, where obligees are affected by principals they do not directly contract with.

As a model for network failure, we assume that each principal i∈𝒱i\in\mathcal{V} has an associated idiosyncratic risk score ri∈(0,1)r\_{i}\in(0,1). We interpret rir\_{i} as the probability that node ii fails independently. These are assumed to be determined exogenously, based only on individual node level attributes and without any direct knowledge of the network.333In practice these scores are based on each organization’s financial records and hence include some limited network effects. However, we treat these as exogenous inputs into the model.
Because pure obligees do not perform bonded work themselves we model their idiosyncratic risk as zero, ri=0r\_{i}=0. Any project failure at that level is therefore interpreted as the consequence of downstream contractor defaults rather than an independent failure of the obligee.

We additionally associate with each node a value αi∈[0,1]\alpha\_{i}\in[0,1] corresponding to their network-associated failure propagation probability. We use αi\alpha\_{i} to denote the probability that a failure of one of node ii’s neighbors propagates and affects node ii, essentially a measure of node ii’s susceptibility to project incompletion by its principals. Accordingly, we set αi=1\alpha\_{i}=1 for pure obligees, which by construction means that any failure of their principals directly translates to project incompletion at the obligee node, and αi=0\alpha\_{i}=0 for any pure principals since none of their work is performed by other principals. Further, any node which is an intermediary has αi∈(0,1)\alpha\_{i}\in(0,1).
We let 𝐀\mathbf{A} be the diagonal matrix with entries 𝐀i​i=αi\mathbf{A}\_{ii}=\alpha\_{i} for i∈𝒱i\in\mathcal{V}.

###### Remark 2.1

In our model we assume that the entire contractor network is fully observed by the surety organization. This is unlikely to hold in practice, since each surety organization only observes contracts that their organization bonds.
In [Section 10.2](https://arxiv.org/html/2511.05691v1#S10.SS2 "10.2 Accounting for Unobserved Edges ‣ 10 Computational Experiments: Additional Details") we present methodology to impute these unobserved edges based on observed contracts and organization-level financial records.

#### Stochastic Risk Propagation.

We are interested in simulating cascading failures across the contractor network. In accordance with this goal, we will define a stochastic process (Xit)i∈𝒱,t∈ℕ(X\_{i}^{t})\_{i\in\mathcal{V},t\in\mathbb{N}} to model our failure dynamics, where Xit∈{0,1}X\_{i}^{t}\in\{0,1\} will denote the indicator of whether contractor ii fails at timestep tt. When ii is a pure obligee we represent this as the indicator that one of ii’s project fails. We further denote 𝐗t\mathbf{X}^{t} to represent the vector (Xit)i∈𝒱(X\_{i}^{t})\_{i\in\mathcal{V}} of node-level failures at time-step tt. This is with slight abuse of notation, since elsewhere we use bold capital letters to denote matrices. We emphasize that the notion of timestep in this model is primarily used as a vehicle for understanding the stationary failure dynamics.

Initially we assume that each Xi0∼Bernoulli​(ri)X\_{i}^{0}\sim\textsf{Bernoulli}(r\_{i}), corresponding to each node ii failing independently according to their own inherent idiosyncratic risk score. Since pure obligees have ri=0r\_{i}=0, Xi0=0X\_{i}^{0}=0 for those nodes. The dynamics of the stochastic process are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xit+1∼Bernoulli​((1−αi)​ri+αi​∑j∈δin​(i)wi​j​Xjt).X\_{i}^{t+1}\sim\textsf{Bernoulli}\Big((1-\alpha\_{i})r\_{i}+\alpha\_{i}\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}X\_{j}^{t}\Big). |  | (1) |

In Xi0X\_{i}^{0}, each node fails independently according to their inherent idiosyncratic failure probability. Afterwards, conditional on (Xjt)j∈𝒱(X\_{j}^{t})\_{j\in\mathcal{V}}, the failure probability is as follows. First, αi\alpha\_{i} denotes the probability that node ii’s failure is affected by its neighbors. Hence, αi​∑j∈δin​(i)wi​j​Xjt\alpha\_{i}\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}X\_{j}^{t} is the cumulative risk associated with their in-neighbors (principals) under this event. Otherwise, with probability (1−αi)(1-\alpha\_{i}) the node fails according to its own idiosyncratic risk score rir\_{i}.
We further note that this defines a probability distribution over {0,1}n\{0,1\}^{n} which we denote as ℙ​(𝐗t)\mathbb{P}(\mathbf{X}^{t}).

$2.1MAAEEBBCCDD$1.4M$0.7M$2.8M$1.7M


Figure 2: Sample contractor network (see [Fig. 1](https://arxiv.org/html/2511.05691v1#S1.F1 "In 1 Introduction")). Here we see that contractor CC is an obligee for both AA and BB (with contract value $2.1M and $1.4M respectively). Solid (dashed) edges denote active (failed) obligations; dark-filled nodes are in default; light-filled nodes are solvent. Hence, our model captures the effect of contractor AA’s failure on both the intermediary CC but also the pure obligee EE.

###### Example 2.2

Consider a simplified contracting network composed of five organizations (see [Figure 2](https://arxiv.org/html/2511.05691v1#S2.F2 "In Stochastic Risk Propagation. ‣ 2 Network Model Definition")). Each edge in the network represents a bonded contractual obligation, with annotated edges indicating the associated financial exposure. Edge weights are then calculated as the relative financial exposure to the obligee from each of its principals (e.g. CC’s exposure to AA is 0.60.6 since AA is responsible for 60%60\% of the work conducted to CC).
Companies AA and BB are pure principals, since they do not subcontract work to any other organizations. Company CC is an intermediary, since they are both subcontractors to Companies DD and EE, but obligees to companies AA and BB. Finally, Companies DD and EE are pure obligees.

This example illustrates how the failure of a pure principal (e.g., AA defaults) can propagate through the network in the stochastic process. If CC cannot complete its contractual obligations to EE because AA fails, then EE may incur losses, even though it never directly contracted with AA. Such indirect dependencies are not captured in standard models assuming independent risk, but they are central in our network-aware framework.
This further underscores the role of intermediaries like CC in amplifying risk: even with moderate idiosyncratic risk levels for AA and BB, the dependency structure means that failures can cascade through the network, elevating systemic risk beyond what node-level scores would suggest.

For each node i∈𝒱i\in\mathcal{V} we use βi\beta\_{i} to denote their financial loss, i.e. the amount that the insurer needs to pay out in case of node ii’s failure. Inherent to this definition is that βi=0\beta\_{i}=0 for all nodes ii that are pure obligees (since they only receive bonded work). Lastly, we denote the global financial loss as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(𝐗t)=∑i∈𝒱βi​Xit=β⊤​𝐗t,\mathcal{L}(\mathbf{X}^{t})=\sum\_{i\in\mathcal{V}}\beta\_{i}X\_{i}^{t}=\mathbf{\beta}^{\top}\mathbf{X}^{t}, |  | (2) |

which denotes the cumulative financial loss associated with all of the nodes in the network if their failures are dictated by 𝐗t\mathbf{X}^{t} and the financial loss per node is βi\beta\_{i}. This quantity captures how individual contractor defaults aggregate into broader network-wide loss for the surety organization.

Our main goal in the rest of this work centers on understanding the stochastic process 𝐗t\mathbf{X}^{t}, its asymptotic behavior, and providing insights into how network structure influences systemic risk. We then leverage this analysis to compare ℒ​(𝐗0)\mathcal{L}(\mathbf{X}^{0}) (the independent failure model) to the stationary behavior of ℒ​(𝐗t)\mathcal{L}(\mathbf{X}^{t}) to quantify the financial effect of cascading failures in surety networks. We focus on the stationary behavior of the stochastic process primarily to serve as a measure of risk propagation in the network, and leave further studies on the transient behavior of the stochastic process for future work.

### 2.1 Discussion of Modeling Assumptions

We conclude the section with a discussion of our modeling assumptions.

#### Static Network Structure.

In reality, contractor networks are time-varying since edges are dictated by contracts with fixed terms. However, our model assumes a fixed contractor network over time, meaning we do not allow for the entry or exit of contracting organizations, nor do we model the formation or dissolution of contractual ties. This assumption enables a clean equilibrium analysis of systemic risk and allows us to characterize how risk distributes over the network in steady state. That said, incorporating a dynamic network formation remains an important practical direction for future work. In [Section 4.1](https://arxiv.org/html/2511.05691v1#S4.SS1 "4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process") and [Section 9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs") we show that our result on the mixing time for the stochastic process applies under time-varying contractor networks.

#### Exogenous Risk Scores.

We treat each contractor ii’s idiosyncratic risk score rir\_{i} and network sensitivity parameter αi\alpha\_{i} as exogenously specified inputs to the model. In practice, these parameters are inferred from financial health indicators or historical default data, and likely take into account mild network risk indicators (kim2019default). However, regardless of how rir\_{i} are estimated, our model allows for the direct incorporation of network effects on risk in contractor networks.

#### Linear Risk Amplification.

Our stochastic process assumes that a contractor’s risk of failure increases linearly based on the impact of their neighbors via wi​jw\_{ij} (see [Eq. 1](https://arxiv.org/html/2511.05691v1#S2.E1 "In Stochastic Risk Propagation. ‣ 2 Network Model Definition")). This additive structure simplifies both analysis and simulation, but it may fail to capture important nonlinearities in real-world contagion effects. For instance, a contractor may be robust to isolated failures but vulnerable to risks beyond a certain threshold, such as in the threshold contagion model like watts2002simple.

#### Risk Amplification Proportional to Financial Obligations.

Our work assumes that network-induced risk depends on the proportion of a contractor’s total subcontracted value attributed to each subcontractor, as encoded by the normalized edge weights wi​jw\_{ij}. This formulation reflects a reasonable first-order approximation: risk exposure grows with financial dependence on risky neighbors. Although real-world contracts vary in risk beyond their dollar value, introducing such heterogeneity would significantly complicate the model without materially changing our core theoretical insights.

#### Inclusion of Pure Obligees.

We emphasize that pure obligees ii in the network have ri=0r\_{i}=0, βi=0\beta\_{i}=0, and no outgoing edges. Consequently, they do not contribute directly to either the global financial loss ℒ​(𝐗t)\mathcal{L}(\mathbf{X}^{t}) or to risk propagation through the network. In practice, pure obligees typically correspond to project owners such as city municipalities or agencies that contract with a single primary contractor and do not perform bonded work themselves. While such organizations could, in principle, experience project disruptions for idiosyncratic reasons (e.g., funding or scheduling issues), these are exogenous to the surety relationship and thus outside the scope of our model. We nevertheless include pure obligees to quantify the likelihood that project owners receive incomplete work from their principals, and to evaluate how the position of these owners within the network affects their exposure. Their inclusion also enables the computation of our centrality measure, which captures differences in downstream vulnerability across obligees. We return to these points in our numerical simulations ([Section 5](https://arxiv.org/html/2511.05691v1#S5 "5 Numerical Results")).

## 3 Mean Field Analysis of Expected Risk

We start off our analysis by considering the marginal expected risk failure probabilities of the stochastic process 𝐗t\mathbf{X}^{t} for each node ii. We will later see that this corresponds to a modified Friedkin-Johnsen model in the opinion dynamics literature (FriedkinJohnsen), and calculate a closed-form expression for the mean failure probabilities. We also exploit this representation to describe an eigenvector-based centrality measure, assigning scores to each node in the graph corresponding to their risk-based centrality within the contractor network. We close this section by providing a simple monotonicity condition under which the mean failure probabilities for each node increase due to network effects.

### 3.1 Expected Failure Probabilities

We start off by analyzing the mean field dynamics of our stochastic process 𝐗t\mathbf{X}^{t}. We introduce notation and set mit=𝔼[Xit]m\_{i}^{t}=\mathbb{E}\mathopen{}\mathclose{{\left[X\_{i}^{t}}}\right] for all i∈𝒱i\in\mathcal{V} and t∈ℕt\in\mathbb{N}. All proofs are deferred to [Section 8.1](https://arxiv.org/html/2511.05691v1#S8.SS1 "8.1 Section 3.1 Omitted Proofs ‣ 8 Section 3 Omitted Proofs"). Note that mitm\_{i}^{t} corresponds to the marginal failure probability of node ii in step tt of the stochastic process. By definition in [Eq. 1](https://arxiv.org/html/2511.05691v1#S2.E1 "In Stochastic Risk Propagation. ‣ 2 Network Model Definition"), it is easy to see that mitm\_{i}^{t} satisfies the following recursive equation:

{restatable}

lemmaMeanFieldRecurrence
For all i∈𝒱i\in\mathcal{V} and t∈ℕt\in\mathbb{N} we have that mi0=rim\_{i}^{0}=r\_{i} and

|  |  |  |  |
| --- | --- | --- | --- |
|  | mit+1=(1−αi)​ri+αi​∑j∈δin​(i)wi​j​mjt.m\_{i}^{t+1}=(1-\alpha\_{i})r\_{i}+\alpha\_{i}\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}m\_{j}^{t}. |  | (3) |

Equivalently in matrix notation, 𝐦0=𝐫\mathbf{m}^{0}=\mathbf{r} and 𝐦t+1=(𝐈−𝐀)​𝐫+𝐀𝐖𝐦t\mathbf{m}^{t+1}=(\mathbf{I}-\mathbf{A})\mathbf{r}+\mathbf{A}\mathbf{W}\mathbf{m}^{t}.

[Section 3.1](https://arxiv.org/html/2511.05691v1#S3.SS1 "3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk") shows how the mean failure probabilities satisfy a similar dynamics equation to the original stochastic process in [Eq. 1](https://arxiv.org/html/2511.05691v1#S2.E1 "In Stochastic Risk Propagation. ‣ 2 Network Model Definition"). The obvious next question is whether mitm\_{i}^{t} converges as t→∞t\rightarrow\infty, and whether we can characterize the rate of convergence by the underlying contractor network. In the case that mitm\_{i}^{t} converges, we let:

|  |  |  |  |
| --- | --- | --- | --- |
|  | mi≜limt→∞mit=limt→∞𝔼[Xit]m\_{i}{\triangleq}\lim\_{t\rightarrow\infty}m\_{i}^{t}=\lim\_{t\rightarrow\infty}\mathbb{E}\mathopen{}\mathclose{{\left[X\_{i}^{t}}}\right] |  | (4) |

denote the limiting failure probability of node i∈𝒱i\in\mathcal{V}.

Our first main result of this section shows that the limiting failure probabilities indeed exist and satisfy a fixed point equation.
{restatable}propositionInverseFixedPoint
For any contractor network and any node i∈𝒱i\in\mathcal{V}, the limiting failure probabilities mim\_{i} exist and satisfy the following fixed point equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | mi=(1−αi)​ri+αi​∑j∈δin​(i)wi​j​mj,𝐦=(𝐈−𝐀)​𝐫+𝐀𝐖𝐦.m\_{i}=(1-\alpha\_{i})r\_{i}+\alpha\_{i}\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}m\_{j},\quad\quad\mathbf{m}=(\mathbf{I}-\mathbf{A})\mathbf{r}+\mathbf{A}\mathbf{W}\mathbf{m}. |  | (5) |

Moreover, (𝐈−𝐀𝐖)(\mathbf{I}-\mathbf{A}\mathbf{W}) is invertible and so 𝐦\mathbf{m} is unique and satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐦=(𝐈−𝐀𝐖)−1​(𝐈−𝐀)​𝐫.\mathbf{m}=(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}(\mathbf{I}-\mathbf{A})\mathbf{r}. |  | (6) |

0.60.410.620.38AAEEBBCCDD


Figure 3: [Fig. 2](https://arxiv.org/html/2511.05691v1#S2.F2 "In Stochastic Risk Propagation. ‣ 2 Network Model Definition") but with normalized edge weights. If we set 𝐫=[.2,.1,.05,0,0]\mathbf{r}=[.2,.1,.05,0,0] and α=[0,0,0.25,1,1]\mathbf{\alpha}=[0,0,0.25,1,1] then 𝐦=[0.2,0.1,0.0775,0.0775,0.08605]\mathbf{m}=[0.2,0.1,0.0775,0.0775,0.08605]. Thus, we see that contractor CC’s risk score increases from 0.050.05 to 0.07750.0775 due to their position within the network. The pure obligee DD gets a risk score equal to its sole subcontractor CC, while obligee EE’s risk score is a weighted average of both its principals.

[Section 3.1](https://arxiv.org/html/2511.05691v1#S3.SS1 "3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk") establishes a closed-form expression for the limiting failure probabilities 𝐦\mathbf{m} in terms of the adjacency matrix 𝐖\mathbf{W}, idiosyncratic risk scores 𝐫\mathbf{r}, and failure propagation probabilities 𝐀\mathbf{A}. In [Fig. 3](https://arxiv.org/html/2511.05691v1#S3.F3 "In 3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk") we illustrate the average failure probabilities computed over the contractor network from [Example 2.2](https://arxiv.org/html/2511.05691v1#S2.Thmtheorem2 "Example 2.2 ‣ Stochastic Risk Propagation. ‣ 2 Network Model Definition"). First note that mi=rim\_{i}=r\_{i} for any pure principals ii, since they do not experience any network effects. However, the intermediary CC’s mean failure probability increases when taking into account network structure due to their position in the network (we provide conditions under which this occurs in [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk")).

The operator (𝐈−𝐀𝐖)−1(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1} admits multiple interpretations across related literatures. In Markov chain theory, it parallels the fundamental matrix of absorbing chains, where each entry gives the expected number of visits to a state prior to absorption (kemeny1969finite). From a graph-theoretic perspective, it plays a role similar to the pseudoinverse of the graph Laplacian, which encodes mean hitting times, commute times, and effective resistances (lovasz1993random, doyle1984random, chung1997spectral). In our context, this highlights that (𝐈−𝐀𝐖)−1(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1} aggregates contributions from all higher-order paths in the contractor network, providing an interpretable link between local idiosyncratic risks and their amplified global effects.

We defer the proof of [Section 3.1](https://arxiv.org/html/2511.05691v1#S3.SS1 "3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk") to [Section 8.1](https://arxiv.org/html/2511.05691v1#S8.SS1 "8.1 Section 3.1 Omitted Proofs ‣ 8 Section 3 Omitted Proofs"), and here we outline the key technical steps. Our approach begins by establishing in [Fig. 3](https://arxiv.org/html/2511.05691v1#S3.F3 "In 3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk") that the ℓ∞\ell\_{\infty}-induced norm satisfies ∥(𝐀𝐖)2∥<1\lVert(\mathbf{A}\mathbf{W})^{2}\rVert<1. This implies that the power sequence (𝐀𝐖)t(\mathbf{A}\mathbf{W})^{t} vanishes as t→∞t\to\infty, ensuring the existence and uniqueness of the limiting mean field. Importantly, while the process may not be contractive in a single iteration (since pure obligees with αi=1\alpha\_{i}=1 can only be influenced by their principals), it is always contractive after two iterations. Intuitively, every obligee is connected to at least one intermediary or principal with αi<1\alpha\_{i}<1, so risk propagation cannot sustain itself indefinitely. This “two-step contraction” property is a structural feature of the surety process.

{restatable}

lemmaSecondNormBounded
Let 𝐀\mathbf{A} be a diagonal matrix with 𝐀i​i=αi​ for all ​i∈𝒱\mathbf{A}\_{ii}=\alpha\_{i}\text{ for all }i\in\mathcal{V} and let 𝐖\mathbf{W} be the row-stochastic adjacency matrix of the contractor graph GG. Then we have ∥(𝐀𝐖)2∥<1\lVert(\mathbf{A}\mathbf{W})^{2}\rVert<1 and (𝐀𝐖)t→0(\mathbf{A}\mathbf{W})^{t}\to 0 as t→∞t\to\infty.

This bound is useful for showing that the Neumann series of 𝐀𝐖\mathbf{A}\mathbf{W} converges, which we formalize in the following corollary:
{restatable}corollaryNeumann
Let 𝐀\mathbf{A} be a diagonal matrix with 𝐀i​i=αi​ for all ​i∈𝒱\mathbf{A}\_{ii}=\alpha\_{i}\text{ for all }i\in\mathcal{V} and let 𝐖\mathbf{W} be the row-stochastic adjacency matrix of the contractor graph GG. Then (𝐈−𝐀𝐖)(\mathbf{I}-\mathbf{A}\mathbf{W}) is invertible, and the Neumann series ∑t=0∞(𝐀𝐖)t\sum\_{t=0}^{\infty}(\mathbf{A}\mathbf{W})^{t} converges to (𝐈−𝐀𝐖)−1(\mathbf{I}-\mathbf{A}\mathbf{W})^{{-1}}.

Consequently, we conclude that the matrix (𝐈−𝐀𝐖)(\mathbf{I}-\mathbf{A}\mathbf{W}) is invertible, and its inverse is given by the Neumann series. This guarantees both existence and uniqueness of the limiting vector 𝐦\mathbf{m}, which satisfies the fixed-point formula in [Eq. 6](https://arxiv.org/html/2511.05691v1#S3.E6 "In 3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk"). We complete the proof by expanding the recurrence relation in [Eq. 3](https://arxiv.org/html/2511.05691v1#S3.E3 "In 3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk") and taking limits as tt goes to infinity of the mean failure probability vector.

[Section 3.1](https://arxiv.org/html/2511.05691v1#S3.SS1 "3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk") highlights that, for all i∈𝒱i\in\mathcal{V}, the failure probabilities mitm\_{i}^{t} converge to their limiting failure probabilities mim\_{i}, and offers a closed form expression for mim\_{i}. This allows us to calculate the network-adjusted limiting failure probabilities for each node in the network for an arbitrary contractor graph. In our next result we quantify the rate of convergence.
We establish that in directed acyclic graphs, the convergence occurs in finite time. In particular, the process converges in just dd steps, where d>0d>0 is the longest path length in the graph.

{restatable}

propositionLimitingConvergenceRateAcyclic
For any contractor network and t≥2t\geq 2 we have that:

|  |  |  |
| --- | --- | --- |
|  | ∥𝐦t−𝐦∥≤(1+21−∥(𝐀𝐖)2∥)∥𝐫∥∥(𝐀𝐖)2∥⌊t/2⌋.\lVert\mathbf{m}^{t}-\mathbf{m}\rVert\leq\mathopen{}\mathclose{{\left(1+\frac{2}{1-\lVert(\mathbf{A}\mathbf{W})^{2}\rVert}}}\right)\lVert\mathbf{r}\rVert\lVert(\mathbf{A}\mathbf{W})^{2}\rVert^{\lfloor t/2\rfloor}. |  |

Moreover, if GG is acyclic and we denote by d>0d>0
its maximum path length, then for all t≥dt\geq d and all i∈𝒱i\in\mathcal{V} we have mit=mim\_{i}^{t}=m\_{i}.

#### Relation to FriedkinJohnsen.

Our model is closely related to the social influence model under static conditions introduced by FriedkinJohnsen, which describes a process in which an individual’s opinion at time t+1t+1 is represented as a real-valued linear function of both their innate opinion (determined by exogenous variables) and the opinions of their in-neighbors in the previous time step tt.
Let 𝐦t\mathbf{m}^{t} denote the vector of opinions at time t≥0t\geq 0, where 𝐫=𝐦0\mathbf{r}=\mathbf{m}^{0} denotes the vector of inherent opinions that each individual holds at time t=0t=0.
Then opinions evolve according to the following dynamics for all t∈ℕt\in\mathbb{N}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐦t+1=γ​𝐫+α​𝐖𝐦t,\mathbf{m}^{t+1}=\gamma\mathbf{r}+\alpha\mathbf{W}\mathbf{m}^{t}, |  | (7) |

where 𝐖\mathbf{W} is an influence matrix in which wi​jw\_{ij} corresponds to the extent to which ii takes jj’s opinion into account, and α,γ\alpha,\gamma are scalar bias parameters that represent the importance nodes place on the weighted sum of their neighbors’ opinions and on their inherent opinion, respectively.
Then if α<1\alpha<1 and α−1\alpha^{-1} is not an eigenvalue of 𝐖\mathbf{W}, the process converges to

|  |  |  |
| --- | --- | --- |
|  | 𝐦≜limt→∞𝐦t=limt→∞(𝐈+α𝐖+⋯+αt𝐖t)γ𝐫=(𝐈−α𝐖)−1γ𝐫.\mathbf{m}\triangleq\lim\_{t\rightarrow\infty}\mathbf{m}^{t}=\lim\_{t\rightarrow\infty}\mathopen{}\mathclose{{\left(\mathbf{I}+\alpha\mathbf{W}+\cdots+\alpha^{t}\mathbf{W}^{t}}}\right)\gamma\mathbf{r}=(\mathbf{I}-\alpha\mathbf{W})^{-1}\gamma\mathbf{r}. |  |

The stationary distribution then reflects each individual’s final opinion as a scalar on some spectrum.

Adapting their model to our context of risk, we interpret a node’s opinion as its probability of failure, which is dependent on failure probabilities of subcontractors according to the transition matrix 𝐖\mathbf{W} in the same manner that individuals in the social influence model take their neighbors’ opinions into account.
Thus in our context we require that “opinions” take values in [0,1][0,1].
Moreover, to ensure that 𝐦t\mathbf{m}^{t} maintains its interpretation as a vector of probabilities for all t∈ℕt\in\mathbb{N}, we also require 𝐖\mathbf{W} to be row-stochastic and that α,γ>0\alpha,\gamma>0 satisfy α+γ=1\alpha+\gamma=1.
Then we can rewrite [Equation 7](https://arxiv.org/html/2511.05691v1#S3.E7 "In Relation to FriedkinJohnsen. ‣ 3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk") as
𝐦t+1=(1−α)​𝐫+α​𝐖𝐦t.\mathbf{m}^{t+1}=(1-\alpha)\mathbf{r}+\alpha\mathbf{W}\mathbf{m}^{t}.

Comparing with our dynamics in [Equation 3](https://arxiv.org/html/2511.05691v1#S3.E3 "In 3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk"), the main difference from FriedkinJohnsen is that they assume a common bias parameter α\alpha, whereas our model allows node-specific bias parameters by replacing α\alpha and γ\gamma with diagonal matrices 𝐀\mathbf{A} and (𝐈−𝐀)(\mathbf{I}-\mathbf{A}). Note that in contrast to the Friedkin-Johnsen model, we consider a directed network, so to handle nodes i∈𝒱i\in\mathcal{V} that lack in- or out-edges we fix their αi\alpha\_{i} as described in [Section 2](https://arxiv.org/html/2511.05691v1#S2 "2 Network Model Definition"). More broadly, their framework models the deterministic evolution of average opinions, while ours defines a discrete stochastic process over binary outcomes, yielding the full distribution of failures across the network rather than only mean behavior.

### 3.2 Identifying the Impact of Network Structure

The previous discussion highlights that the mean failure probabilities 𝐦\mathbf{m} satisfy an equilibrium-type dynamic. This suggests that the underlying risk propagation in the network stabilizes to a fixed distribution of failure probabilities across nodes. Here, we exploit the closed-form definition of the failure probabilities to systematically identify “risky” nodes within the network — those whose individual or structural properties contribute significantly to overall systemic risk.

From [Section 3.1](https://arxiv.org/html/2511.05691v1#S3.SS1 "3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk") we established that, for all i∈𝒱i\in\mathcal{V} the failure probabilities mitm\_{i}^{t} converge to their steady-state values mim\_{i}, which satisfy the fixed-point equation:

|  |  |  |
| --- | --- | --- |
|  | 𝐦=(𝐈−𝐀𝐖)−1​(𝐈−𝐀)​𝐫.\mathbf{m}=(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}(\mathbf{I}-\mathbf{A})\mathbf{r}. |  |

This expression captures how the individual risk factors 𝐫\mathbf{r} interact with the network structure, where 𝐀\mathbf{A} and 𝐖\mathbf{W} determine the interplay between direct risks and dependencies between nodes.

To better understand the network-wide risk contribution, we consider the average limiting failure probability across all nodes, given by (where we denote 𝟏\mathbf{1} as the vector of all 11s):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟏⊤n​𝐦=𝟏⊤n​(𝐈−𝐀𝐖)−1​(𝐈−𝐀)⏟𝐮⊤​𝐫,\frac{\mathbf{1}^{\top}}{n}\mathbf{m}=\underbrace{\frac{\mathbf{1}^{\top}}{n}(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}(\mathbf{I}-\mathbf{A})}\_{\mathbf{u}^{\top}}\mathbf{r}, |  | (8) |

where nn is the total number of nodes in the network. This expression shows that the overall failure risk can be rewritten as a network-adjusted re-weighting of the individual idiosyncratic risk scores 𝐫\mathbf{r}. The term (𝐈−𝐀𝐖)−1(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1} highlights that risk exposure is not limited to direct neighbors: it aggregates contributions from all paths in the network, with longer paths down-weighted by successive products of exposure probabilities.

###### Definition 3.1

We set

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐮⊤=𝟏⊤n​(𝐈−𝐀𝐖)−1​(𝐈−𝐀)\mathbf{u}^{\top}=\frac{\mathbf{1}^{\top}}{n}(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}(\mathbf{I}-\mathbf{A}) |  | (9) |

to denote the risk-based centrality vector.

This definition is analogous to traditional PageRank in web search algorithms (BRIN1998107, page1999pagerank, kleinberg1999authoritative), where importance is assigned based on structural connectivity. Here, however, the risk-based centrality captures how individual nodes influence the system-wide failure probability. It accounts for both direct contributions from individual risk levels (through 𝐀\mathbf{A}) and the indirect propagation of risk through network interactions (through 𝐖\mathbf{W}).
Note that by construction, ui=0u\_{i}=0 for all pure obligees ii, i.e. nodes with αi=1\alpha\_{i}=1. This follows from the structure of 𝐈−𝐀\mathbf{I}-\mathbf{A}, where nodes corresponding to obligees contain only zero entries. Intuitively, pure obligees absorb risk but do not emit risk, and so their risk-based centrality measure is zero.

More generally, the value of uiu\_{i} for i∈𝒱i\in\mathcal{V} provides an interpretation of how risk is *structurally* amplified within the network.444Here we are primarily interested in how the *structure* amplifies individual risks, so we focus on the average failure probability over all nodes. If we instead consider the expected aggregate loss ℒ​(𝐦)\mathcal{L}(\mathbf{m}), we get an alternate centrality measure 𝐮~⊤=β⊤​(𝐈−𝐀𝐖)−1​(𝐈−𝐀)\tilde{\mathbf{u}}^{\top}=\mathbf{\beta}^{\top}(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}(\mathbf{I}-\mathbf{A}) that weights failure probabilities to describe the expected contribution of each node to aggregate loss.
Nodes with higher uiu\_{i} contribute more significantly to the overall risk amplification. These nodes not only possess inherent risk but also transmit risk to others, affecting the network-wide failure probability.

### 3.3 Impact of Risk Propagation on Mean Field

We close out this section with a central concern for contractor networks: the potential for risk amplification due to a contractor’s location within the network. While our model allows for flexible dynamics, it remains unclear how individual risk exposures respond to changes in the network structure. In particular, we seek to understand whether, for each i∈𝒱i\in\mathcal{V}, a firm’s limiting failure probability mim\_{i} is amplified (larger than rir\_{i}) when it interacts with riskier principals. To facilitate this analysis, we introduce a structural assumption on contracting organizations, which posits that contractors engage with organizations with higher risk. While this may not hold universally, we show that it is a sufficient condition for 𝐦≥𝐫\mathbf{m}\geq\mathbf{r} across the entire network.

{assumption}

We assume for all intermediaries ii ∈𝒱\in\mathcal{V}, the average risk of their principals is greater than or equal to their own inherent idiosyncratic risk score, i.e.

|  |  |  |
| --- | --- | --- |
|  | ∑j∈δin​(i)wi​j​rj≥ri.\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}r\_{j}\geq r\_{i}. |  |

While [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk") may appear restrictive, it aligns with patterns observed in real-world contractor networks (bci2021supplychain). In practice, principals that subcontract work are often larger and hence less risky, whereas the subcontractors they engage with are typically smaller and more exposed to risk, which is in part due to a less rigorous vetting process (dietz2018mitigating). Although this assumption does not hold universally in our empirical setting in [Section 5](https://arxiv.org/html/2511.05691v1#S5 "5 Numerical Results"), we demonstrate that similar results emerge in our application.

We now present our main result for this section (see [Section 8.2](https://arxiv.org/html/2511.05691v1#S8.SS2 "8.2 Section 3.3 Omitted Proofs ‣ 8 Section 3 Omitted Proofs") for the proof).

{restatable}

theoremAssumptionMeanIncrease
Under [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"), the mean failure probability vector evolves monotonically: for all tt ∈ℕ\in\mathbb{N},

|  |  |  |
| --- | --- | --- |
|  | 𝐦t≤𝐦t+1,𝔼[ℒ(𝐗t)]≤𝔼[ℒ(𝐗t+1)].\mathbf{m}^{t}\leq\mathbf{m}^{t+1},\qquad\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{t})}}\right]\leq\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{t+1})}}\right]. |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | 𝐦≥𝐫,𝔼[ℒ(𝐗∞)]≥𝔼[ℒ(𝐗0)].\mathbf{m}\geq\mathbf{r},\qquad\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{\infty})}}\right]\geq\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{0})}}\right]. |  |

Moreover, increasing the exposure parameter αi\alpha\_{i} of any intermediary ii can only raise the entries of 𝐦\mathbf{m}:

|  |  |  |
| --- | --- | --- |
|  | ∂𝐦∂αi=(𝐈−𝐀𝐖)−1∂𝐀∂αi[𝐖𝐦−𝐫]≥ 0.\frac{\partial\mathbf{m}}{\partial\alpha\_{i}}=(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\frac{\partial\mathbf{A}}{\partial\alpha\_{i}}\mathopen{}\mathclose{{\left[\mathbf{W}\mathbf{m}-\mathbf{r}}}\right]\;\geq\;\mathbf{0}. |  |

Under the opposite of [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"), all inequalities hold in the reverse direction.

###### Remark 3.2

The monotonicity in [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk") can be viewed through the lens of potential theory: under [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk") the mean failure probabilities evolve as a subharmonic function on the contractor graph, so the limiting vector 𝐦\mathbf{m} is the smallest subharmonic majorant of the initial risks 𝐫\mathbf{r} (chung1997spectral). Reversing the assumption yields the superharmonic analogue.

The first part of [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk") shows that, under [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"), the mean failure probability for each node mim\_{i} evolves monotonically over time. Consequently, the expected global average loss 𝔼[ℒ(𝐗t)]\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{t})}}\right] is also monotone with respect to tt and converges to the global average risk associated with the stationary process.
The intuition is straightforward: risk propagates through the network because intermediaries rely on principals who, on average, are at least as risky as themselves. Over time, this accumulation amplifies failure probabilities throughout the network. A central insight here is that under [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"), incorporating network structure consistently yields a higher expected global loss than models that assume independent failures.
The second part of [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk") examines monotonicity with respect to the network-associated failure propagation rates αi\alpha\_{i} for all i∈𝒱i\in\mathcal{V}. This highlights the robustness of [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"): its conclusions hold across a wide range of α\alpha values and underscore how systemic risk is shaped jointly by idiosyncratic contractor risk and network position.

Our next assumption strengthens [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk") by requiring that a contractor’s neighbors, on average, have not just a higher inherent risk but a risk level that exceeds the contractor’s by a fixed margin. We will then show the propagation of the margin in terms of its downstream cumulative risk measures.
{assumption}
We assume for all intermediaries ii, the average risk of their neighbors is strictly greater than their own inherent idiosyncratic risk score, i.e. there exists a δ>0\delta>0 such that

|  |  |  |
| --- | --- | --- |
|  | ∑j∈δin​(i)wi​j​rj−ri≥δ​ri.\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}r\_{j}-r\_{i}\geq\delta r\_{i}. |  |

Using this, we highlight the impact of risk propagation in the network by presenting lower bounds on the increase in failure probabilities. Indeed, under [Remark 3.2](https://arxiv.org/html/2511.05691v1#S3.Thmtheorem2 "Remark 3.2 ‣ 3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk") we can establish the following result (proof deferred to [Section 8.2](https://arxiv.org/html/2511.05691v1#S8.SS2 "8.2 Section 3.3 Omitted Proofs ‣ 8 Section 3 Omitted Proofs")).

{restatable}

propositionMeanFieldGap
Under [Remark 3.2](https://arxiv.org/html/2511.05691v1#S3.Thmtheorem2 "Remark 3.2 ‣ 3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk") we have that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐦−𝐫\displaystyle\mathbf{m}-\mathbf{r} | ≥δ​(𝐈−𝐀𝐖)−1​𝐀𝐫,\displaystyle\geq\delta(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\mathbf{A}\mathbf{r}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼[ℒ(𝐗∞)]−𝔼[ℒ(𝐗0)]\displaystyle\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{\infty})}}\right]-\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{0})}}\right] | ≥δ​β⊤​(𝐈−𝐀𝐖)−1​𝐀𝐫.\displaystyle\geq\delta\beta^{\top}(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\mathbf{A}\mathbf{r}. |  |

This result highlights how the limiting failure probabilities increase in proportion by a factor of δ\delta, highlighting how seemingly modest shifts in network composition can escalate systemic exposure.

## 4 Asymptotic Behavior of Stochastic Risk Process

![Refer to caption](x2.png)


Figure 4: *(Left)* Visualization of the stationary distribution over all possible states 𝐱∈{0,1}5\mathbf{x}\in\{0,1\}^{5} in [Example 2.2](https://arxiv.org/html/2511.05691v1#S2.Thmtheorem2 "Example 2.2 ‣ Stochastic Risk Propagation. ‣ 2 Network Model Definition") computed from [Definition 4.4](https://arxiv.org/html/2511.05691v1#S4.Thmtheorem4 "Definition 4.4 (In-neighbor layers) ‣ 4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process"). Rows enumerate the possible states of principals A,B,CA,B,C, while columns enumerate possible states of pure obligees D,ED,E. The heatmap entry in row (xA,xB,xC)(x\_{A},x\_{B},x\_{C}) and column (xD,xE)(x\_{D},x\_{E}) then gives the log probability of 𝐱=(xA,xB,xC,xD,xE)\mathbf{x}=(x\_{A},x\_{B},x\_{C},x\_{D},x\_{E}) in the stationary distribution.
*(Right)* Visualization of the joint distribution if node failures were instead sampled independently from the mean-field marginals. We point out that the probabilities of all joint default events in which DD and EE fail increase when we account for network effects, reflecting how the defaults of DD and EE become correlated through their shared principal CC.

The previous section analyzed the asymptotic behavior of the marginal average failure probabilities mim\_{i} for all i∈𝒱i\in\mathcal{V}. However, this approach ignores details about the network structure and the main feature that distinguishes this model from independent failure models: the potential for the limiting behavior of nodes to be correlated. In this section, we turn our attention to the full stochastic process 𝐗t\mathbf{X}^{t}. We first establish that 𝐗t\mathbf{X}^{t} is a Markov chain that converges to a unique stationary distribution (proof deferred to [Section 9](https://arxiv.org/html/2511.05691v1#S9 "9 Section 4 Omitted Proofs")), and then we quantify the rate of convergence to its stationary distribution in terms of the mixing time. We close out with a discussion on conditions under which the distribution of ℒ​(𝐗t)\mathcal{L}(\mathbf{X}^{t}) is stochastically dominated (a distributional extension of monotonicity) over tt, highlighting the positive impact of network effects on tail risk.

{restatable}

lemmaMarkovChainStationary
(𝐗t)t∈ℕ(\mathbf{X}^{t})\_{t\in\mathbb{N}} is a Markov chain over the state space {0,1}n\{0,1\}^{n} that converges to a unique stationary distribution with probability mass function π​(𝐱)=limt→∞ℙ​(𝐗t=𝐱)\mathbf{\pi}(\mathbf{x})=\lim\_{t\rightarrow\infty}\mathbb{P}(\mathbf{X}^{t}=\mathbf{x}) for all 𝐱∈{0,1}n\mathbf{x}\in\{0,1\}^{n}.
Before continuing, we note that by the continuous mapping theorem and the linearity of ℒ​(⋅)\mathcal{L}(\cdot), it follows from [Figure 4](https://arxiv.org/html/2511.05691v1#S4.F4 "In 4 Asymptotic Behavior of Stochastic Risk Process") that the sequence ℒ​(𝐗t)\mathcal{L}(\mathbf{X}^{t}) converges almost surely as t→∞t\to\infty to ℒ​(𝐗∞)\mathcal{L}(\mathbf{X}^{\infty}).

The previous lemma establishes that the stochastic process 𝐗t\mathbf{X}^{t} has a unique stationary distribution, which we will denote as π\pi. By analyzing π\pi, we can understand the limiting behavior of risk propagation in our contractor network. In [Fig. 4](https://arxiv.org/html/2511.05691v1#S4.F4 "In 4 Asymptotic Behavior of Stochastic Risk Process") we provide a visualization of the stationary distribution under [Example 2.2](https://arxiv.org/html/2511.05691v1#S2.Thmtheorem2 "Example 2.2 ‣ Stochastic Risk Propagation. ‣ 2 Network Model Definition"). We point out that the probabilities of all joint default events in which DD and EE fail increase when we account for network effects, reflecting how the defaults of DD and EE become correlated through their shared principal CC.

We will abuse notation slightly and let 𝐗∞\mathbf{X}^{\infty} denote a random variable whose distribution is sampled according to π\pi. We begin by focusing on quantifying the rate of convergence of the stochastic process 𝐗t\mathbf{X}^{t} for t∈ℕt\in\mathbb{N} to its stationary distribution π\mathbf{\pi}, measured in terms of the mixing time:

|  |  |  |
| --- | --- | --- |
|  | tmix​(ϵ)=inf{t≥0:dT​V​(π,ℙ​(𝐗t))≤ϵ},t\_{\textsf{mix}}(\epsilon)=\inf\{t\geq 0:d\_{TV}(\pi,\mathbb{P}(\mathbf{X}^{t}))\leq\epsilon\}, |  |

where ε>0\varepsilon>0 and we treat the distributions as vectors over ℝ2n\mathbb{R}^{2^{n}}. This directly impacts our ability to simulate network risk efficiently, as a slow-mixing process would require extensive time steps to approximate the long-run behavior accurately. By quantifying the mixing time, we establish bounds on how many iterations are needed before simulations yield reliable estimates of systemic risk (leveraged in our numerical simulations in [Section 5](https://arxiv.org/html/2511.05691v1#S5 "5 Numerical Results")). Additionally, knowing the convergence rate allows us to assess how network structure influences the speed of risk propagation.

### 4.1 Mixing Time of the Stochastic Process

Recall in [Section 3.1](https://arxiv.org/html/2511.05691v1#S3.SS1 "3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk") we showed that the convergence rate of the mean failure probabilities in our stochastic model depends on the rate of decay of 𝐀𝐖\mathbf{A}\mathbf{W}. Here, we extend this insight to the full stochastic process, showing that the distribution over network failures also mixes depending on the rate of decay of 𝐀𝐖\mathbf{A}\mathbf{W}. These results are, in a sense, quite surprising.
Classical Markov chain arguments that operate directly on our state space {0,1}n\{0,1\}^{n} would give bounds on the mixing time that scale with the size of the state space, i.e. exponentially in nn (resnick2013adventures). Such bounds are useless for the networks of interest here. Our analysis instead shows that the mixing time actually increases at a *logarithmic* rate in nn (for fixed accuracy ϵ\epsilon). Moreover, in the special but important case in which the contractor graph GG is a directed acyclic graph (DAG), the chain mixes in a *finite* number of steps that equals the depth of the DAG. Moreover, for DAGs the stationary distribution can be written in closed form by propagating probabilities along a topological order; see Fig. [5](https://arxiv.org/html/2511.05691v1#S4.F5 "Figure 5 ‣ 4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process").

The proof relies on a synchronous coupling of two copies of the process, (𝐗t,𝐘t)t∈ℕ(\mathbf{X}^{t},\mathbf{Y}^{t})\_{t\in\mathbb{N}}, driven by the same randomness. A single step of the dynamics need not be contractive in general because of the pure obligees, but we show that the evolution is contractive every two steps (similar to [Fig. 3](https://arxiv.org/html/2511.05691v1#S3.F3 "In 3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk")). Consequently, the decay of the discrepancy can be controlled by ‖(𝐀𝐖)2‖\|(\mathbf{A}\mathbf{W})^{2}\|, which was shown to be strictly less than one in [Fig. 3](https://arxiv.org/html/2511.05691v1#S3.F3 "In 3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk"). A version of this result also holds under time-varying graphs under the assumption that principals and obligees remain principals and obligees across all time steps. See [Section 9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs") for more details.

{restatable}

theoremMixingGeneral
Let GG be an arbitrary contractor network. Then for all t∈ℕt\in\mathbb{N} we have that,

|  |  |  |  |
| --- | --- | --- | --- |
|  | dT​V​(π,ℙ​(𝐗t))≤n​∥(𝐀𝐖)t∥.d\_{TV}(\pi,\mathbb{P}(\mathbf{X}^{t}))\leq n\lVert(\mathbf{A}\mathbf{W})^{t}\rVert. |  | (10) |

As a result, if GG is a directed acyclic graph and d>0d>0 denotes its maximum path length, then for all ϵ>0\epsilon>0 we have tmix​(ϵ)≤dt\_{\textsf{mix}}(\epsilon)\leq d. Similarly, if GG is a general graph then

|  |  |  |  |
| --- | --- | --- | --- |
|  | tmix(ϵ)≤2+21−‖(𝐀𝐖)2‖log(nϵ).t\_{\textsf{mix}}(\epsilon)\leq 2+\frac{2}{1-\|(\mathbf{A}\mathbf{W})^{2}\|}\,\log\!\mathopen{}\mathclose{{\left(\frac{n}{\epsilon}}}\right). |  | (11) |

###### Proof 4.1

At a high level, we will show for arbitrary starting states 𝐱\mathbf{x} and 𝐲\mathbf{y} that there exists a coupling of the stochastic process 𝐗t\mathbf{X}^{t} and 𝐘t\mathbf{Y}^{t} (which are initialized at 𝐱\mathbf{x} and 𝐲\mathbf{y} respectively) such that for all t∈ℕt\in\mathbb{N}:

|  |  |  |
| --- | --- | --- |
|  | 𝔼[∥𝐗t−𝐘t∥1]≤n∥(𝐀𝐖)t∥.\mathbb{E}\mathopen{}\mathclose{{\left[\lVert\mathbf{X}^{t}-\mathbf{Y}^{t}\rVert\_{1}}}\right]\leq n\lVert(\mathbf{A}\mathbf{W})^{t}\rVert. |  |

As a result, this then implies by letting 𝐲\mathbf{y} follow the law of π\pi that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dT​V(π,ℙ(𝐗t))≤ℙ(𝐗t≠𝐘t)=ℙ(∥𝐗t−𝐘t∥1≥1)≤𝔼[∥𝐗t−𝐘t∥1]≤n∥(𝐀𝐖)t∥,d\_{TV}(\pi,\mathbb{P}(\mathbf{X}^{t}))\leq\mathbb{P}(\mathbf{X}^{t}\neq\mathbf{Y}^{t})=\mathbb{P}(\lVert\mathbf{X}^{t}-\mathbf{Y}^{t}\rVert\_{1}\geq 1)\leq\mathbb{E}\mathopen{}\mathclose{{\left[\lVert\mathbf{X}^{t}-\mathbf{Y}^{t}\rVert\_{1}}}\right]\leq n\lVert(\mathbf{A}\mathbf{W})^{t}\rVert, |  | (12) |

as claimed.

Hence, we start by rewriting our stochastic process as 𝐗t+1=fθt+1​(𝐗t)\mathbf{X}^{t+1}=f\_{\mathbf{\theta}^{t+1}}(\mathbf{X}^{t}) where θt=(θit)i∈[N]\mathbf{\theta}^{t}=(\mathbf{\theta}\_{i}^{t})\_{i\in[N]} and each θit\theta\_{i}^{t} are independent random variables. We will use (θt)t∈ℕ(\mathbf{\theta}^{t})\_{t\in\mathbb{N}} to determine our coupling. Note that we can rewrite our stochastic process as

|  |  |  |
| --- | --- | --- |
|  | Xi0=𝟙[θi0≤ri],Xit+1=𝟙[θit+1≤(1−αi)ri+αi∑j∈δin​(i)wi​jXjt],X\_{i}^{0}=\mathbbm{1}\mathopen{}\mathclose{{\left[\theta\_{i}^{0}\leq r\_{i}}}\right],\quad X\_{i}^{t+1}=\mathbbm{1}\mathopen{}\mathclose{{\left[\theta\_{i}^{t+1}\leq(1-\alpha\_{i})r\_{i}+\alpha\_{i}\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}X\_{j}^{t}}}\right], |  |

where θit​∼iid​Uniform​[0,1]\theta\_{i}^{t}\overset{\text{iid}}{\sim}\text{Uniform}[0,1]. We set hi​(𝐱)=(1−αi)​ri+αi​∑j∈δin​(i)wi​j​𝐱jh\_{i}(\mathbf{x})=(1-\alpha\_{i})r\_{i}+\alpha\_{i}\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}\mathbf{x}\_{j}.

Now consider the *synchronous coupling* of two copies (𝐗t,𝐘t)(\mathbf{X}^{t},\mathbf{Y}^{t}) of the stochastic process driven by the same randomness (dictated by (θt)t∈ℕ(\mathbf{\theta}^{t})\_{t\in\mathbb{N}}), where 𝐘0=𝐲∼π\mathbf{Y}^{0}=\mathbf{y}\sim\pi so that ℙ​(𝐘t=⋅)=π​(⋅)\mathbb{P}(\mathbf{Y}^{t}=\cdot)=\pi(\cdot) for all t∈ℕt\in\mathbb{N}.
Define for i=1,…,ni=1,\ldots,n,

|  |  |  |
| --- | --- | --- |
|  | Dit≜𝔼[|Xit−Yit|],𝐃t≜(D1t,…,Dnt)⊤,D\_{i}^{t}\;\triangleq\;\mathbb{E}\mathopen{}\mathclose{{\left[\mathopen{}\mathclose{{\left\lvert X\_{i}^{t}-Y\_{i}^{t}}}\right\rvert}}\right],\qquad\mathbf{D}^{t}\;\triangleq\;\bigl(D\_{1}^{t},\ldots,D\_{n}^{t}\bigr)^{\top}, |  |

to be the expected difference between XitX\_{i}^{t} and YitY\_{i}^{t}.
We start by showing the following lemma:

###### Lemma 4.2

For all t≥1t\geq 1 we have that
𝐃t+1≤𝐀𝐖𝐃t.\mathbf{D}^{t+1}\leq\mathbf{A}\mathbf{W}\mathbf{D}^{t}.

###### Proof 4.3

Consider an arbitrary index i∈𝒱i\in\mathcal{V}. Then by definition of the stochastic process and the coupling, we have that:

|  |  |  |
| --- | --- | --- |
|  | Xit+1=𝟙{θit+1≤hi(𝐗t)}Yit+1=𝟙{θit+1≤hi(𝐘t)}.X\_{i}^{t+1}=\mathds{1}\mathopen{}\mathclose{{\left\{\theta\_{i}^{t+1}\leq h\_{i}(\mathbf{X}^{t})}}\right\}\quad\quad Y\_{i}^{t+1}=\mathds{1}\mathopen{}\mathclose{{\left\{\theta\_{i}^{t+1}\leq h\_{i}(\mathbf{Y}^{t})}}\right\}. |  |

Hence, Xit+1≠Yit+1X\_{i}^{t+1}\neq Y\_{i}^{t+1} if and only if min⁡{hi​(𝐗t),hi​(𝐘t)}<θit+1≤max⁡{hi​(𝐗t),hi​(𝐘t)}\min\{h\_{i}(\mathbf{X}^{t}),h\_{i}(\mathbf{Y}^{t})\}<\theta\_{i}^{t+1}\leq\max\{h\_{i}(\mathbf{X}^{t}),h\_{i}(\mathbf{Y}^{t})\}. Thus

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼[|Xit+1−Yit+1|∣𝐗t,𝐘t]\displaystyle\mathbb{E}\mathopen{}\mathclose{{\left[\mathopen{}\mathclose{{\left\lvert X\_{i}^{t+1}-Y\_{i}^{t+1}}}\right\rvert\mid\mathbf{X}^{t},\mathbf{Y}^{t}}}\right] | =𝔼[𝟙{min{hi(𝐗t),hi(𝐘t)}<θit+1≤max{hi(𝐗t),hi(𝐘t)}}∣𝐗t,𝐘t]\displaystyle=\mathbb{E}\mathopen{}\mathclose{{\left[\mathds{1}\mathopen{}\mathclose{{\left\{\min\{h\_{i}(\mathbf{X}^{t}),h\_{i}(\mathbf{Y}^{t})\}<\theta\_{i}^{t+1}\leq\max\{h\_{i}(\mathbf{X}^{t}),h\_{i}(\mathbf{Y}^{t})\}}}\right\}\mid\mathbf{X}^{t},\mathbf{Y}^{t}}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙ​(θit+1∈(min⁡{hi​(𝐗t),hi​(𝐘t)},max⁡{hi​(𝐗t),hi​(𝐘t)})∣𝐗t,𝐘t)\displaystyle=\mathbb{P}(\theta\_{i}^{t+1}\in(\min\{h\_{i}(\mathbf{X}^{t}),h\_{i}(\mathbf{Y}^{t})\},\max\{h\_{i}(\mathbf{X}^{t}),h\_{i}(\mathbf{Y}^{t})\})\mid\mathbf{X}^{t},\mathbf{Y}^{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =|hi(𝐗t)−hi(𝐘t)|\displaystyle=\mathopen{}\mathclose{{\left\lvert h\_{i}(\mathbf{X}^{t})-h\_{i}(\mathbf{Y}^{t})}}\right\rvert |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =|αiwi⊤(𝐗t−𝐘t)|≤αi∑j∈δin​(i)wi​j|Xjt−Yjt|,\displaystyle=\mathopen{}\mathclose{{\left\lvert\alpha\_{i}w\_{i}^{\top}(\mathbf{X}^{t}-\mathbf{Y}^{t})}}\right\rvert\leq\alpha\_{i}\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}|X\_{j}^{t}-Y\_{j}^{t}|, |  |

where the third equality follows from the fact that θit+1\theta\_{i}^{t+1} is distributed uniformly. Taking the expectation with respect to 𝐗t\mathbf{X}^{t} and 𝐘t\mathbf{Y}^{t} over the coupling yields 𝐃t+1≤𝐀𝐖𝐃t\mathbf{D}^{t+1}\leq\mathbf{A}\mathbf{W}\mathbf{D}^{t}.

With the previous lemma in hand, we are now ready to show the result. Indeed, by [Eq. 12](https://arxiv.org/html/2511.05691v1#S4.E12 "In Proof 4.1 ‣ 4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process") we have that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dT​V​(π,ℙ​(𝐗t))\displaystyle d\_{TV}(\pi,\mathbb{P}(\mathbf{X}^{t})) | ≤𝔼[∥𝐗t−𝐘t∥]=∥𝐃t∥1≤(C.S.)n∥𝐃t∥∞\displaystyle\leq\mathbb{E}\mathopen{}\mathclose{{\left[\lVert\mathbf{X}^{t}-\mathbf{Y}^{t}\rVert}}\right]=\lVert\mathbf{D}^{t}\rVert\_{1}\underset{(\text{C.S.})}{\leq}n\lVert\mathbf{D}^{t}\rVert\_{\infty} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤n​∥(𝐀𝐖)t​𝐃0∥∞\displaystyle\leq n\lVert(\mathbf{A}\mathbf{W})^{t}\mathbf{D}^{0}\rVert\_{\infty} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤n​∥(𝐀𝐖)t∥​∥𝐃0∥∞≤n​∥(𝐀𝐖)t∥.\displaystyle\leq n\lVert(\mathbf{A}\mathbf{W})^{t}\rVert\lVert\mathbf{D}^{0}\rVert\_{\infty}\leq n\lVert(\mathbf{A}\mathbf{W})^{t}\rVert. |  |

Now we note that if GG is a directed acyclic graph, then for any t≥dt\geq d we have (𝐀𝐖)t=0(\mathbf{A}\mathbf{W})^{t}=0. Hence, we get that tmix​(ϵ)≤dt\_{\textsf{mix}}(\epsilon)\leq d for any ϵ>0\epsilon>0. For the general case, we use the fact that ∥(𝐀𝐖)2∥<1\lVert(\mathbf{A}\mathbf{W})^{2}\rVert<1 via [Fig. 3](https://arxiv.org/html/2511.05691v1#S3.F3 "In 3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk"). Plugging this into the above bound yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dT​V​(π,ℙ​(𝐗t))≤n​(∥(𝐀𝐖)2∥)⌊t/2⌋.d\_{TV}(\pi,\mathbb{P}(\mathbf{X}^{t}))\leq n(\lVert(\mathbf{A}\mathbf{W})^{2}\rVert)^{\lfloor t/2\rfloor}. |  | (13) |

Setting the right hand side of [Eq. 13](https://arxiv.org/html/2511.05691v1#S4.E13 "In Proof 4.1 ‣ 4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process") ≤ϵ\leq\epsilon, using the fact that 1−γ≤−log⁡(γ)1-\gamma\leq-\log(\gamma) for γ∈(0,1)\gamma\in(0,1) and solving for tt gives the desired bound on tmix​(ϵ)t\_{\textsf{mix}}(\epsilon). Indeed, let t~≜⌊t/2⌋\tilde{t}\triangleq\lfloor t/2\rfloor. We want to solve n​∥(𝐀𝐖)2∥t~≤ϵn\lVert(\mathbf{A}\mathbf{W})^{2}\rVert^{\tilde{t}}\leq\epsilon. Taking the logarithms (and using that log⁡(∥(𝐀𝐖)2∥)<0\log(\lVert(\mathbf{A}\mathbf{W})^{2}\rVert)<0) gives:

|  |  |  |
| --- | --- | --- |
|  | t~≥log⁡(ε/n)log⁡(∥(𝐀𝐖)2∥)=log⁡(n/ε)−log⁡(∥(𝐀𝐖)2∥).\tilde{t}\geq\frac{\log(\varepsilon/n)}{\log(\lVert(\mathbf{A}\mathbf{W})^{2}\rVert)}\;=\;\frac{\log(n/\varepsilon)}{-\log(\lVert(\mathbf{A}\mathbf{W})^{2}\rVert)}. |  |

Hence it suffices to choose

|  |  |  |
| --- | --- | --- |
|  | t~:=⌈log⁡(n/ϵ)−log⁡(∥(𝐀𝐖)2∥)⌉,t=2​t~.\tilde{t}\;:=\;\Bigl\lceil\frac{\log(n/\epsilon)}{-\log(\lVert(\mathbf{A}\mathbf{W})^{2}\rVert)}\Bigr\rceil,\qquad t=2\tilde{t}. |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | tmix(ϵ)≤ 2⌈log⁡(n/ϵ)−log⁡(‖(𝐀𝐖)2‖)⌉≤21−‖(𝐀𝐖)2‖log(nϵ)+2,\;t\_{\mathrm{mix}}(\epsilon)\;\leq\;2\mathopen{}\mathclose{{\left\lceil\frac{\log(n/\epsilon)}{-\log(\|(\mathbf{A}\mathbf{W})^{2}\|)}}}\right\rceil\;\leq\;\frac{2}{1-\|(\mathbf{A}\mathbf{W})^{2}\|}\,\log\!\mathopen{}\mathclose{{\left(\frac{n}{\epsilon}}}\right)+2, |  |

which trades the logarithm in the denominator for the spectral gap–like term 1−‖(𝐀𝐖)2‖1-\|(\mathbf{A}\mathbf{W})^{2}\|.

A\displaystyle AB\displaystyle BC\displaystyle CE\displaystyle EH\displaystyle HF\displaystyle FG\displaystyle GI\displaystyle ID\displaystyle DΔind\displaystyle\Delta\_{\text{in}}^{d}Δind−1\displaystyle\Delta\_{\text{in}}^{d-1}Δin1\displaystyle\Delta\_{\text{in}}^{1}pure obligees…\displaystyle\dotsc…\displaystyle\dotsc

Figure 5: 
Representation of the “levels” Δink\Delta^{k}\_{\text{in}} in an acyclic graph such that Δin1⊃⋯⊃Δind\Delta^{1}\_{\text{in}}\supset\cdots\supset\Delta^{d}\_{\text{in}}.
Nodes AA and BB each have one dd-length path to HH, so they belong to Δind\Delta^{d}\_{\text{in}}. They also have an edge to the next node in paths (A,C,…,H)(A,C,\dots,H) and (B,D,…,H)(B,D,\dots,H), so they are also in Δin1\Delta^{1}\_{\text{in}}. EE and FF only have paths of length 1, so they are only contained in Δin1\Delta^{1}\_{\text{in}}.
Note that pure principals can belong to any level, not just Δind\Delta^{d}\_{\text{in}} (e.g. GG).
This represents that the states of obligees in Δink\Delta^{k}\_{\text{in}} at any time tt depend only on the previous states of principals in Δink+1\Delta^{k+1}\_{\text{in}} at t−1t-1.

We close out our discussion here with the case when the graph is a DAG. Because there are no directed cycles, the linear operator (𝐀𝐖)(\mathbf{A}\mathbf{W}) is nilpotent with index at most the depth dd, and therefore the coupled chains coalesce after at most dd steps. This immediately implies that tmix​(ϵ)≤dt\_{\textsf{mix}}(\epsilon)\leq d for all ϵ>0\epsilon>0, as described in [Section 4.1](https://arxiv.org/html/2511.05691v1#S4.SS1 "4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process"). In the same spirit, the stationary distribution is computable in closed form by propagating probabilities layer by layer along a (reverse) topological ordering of the contractor graph GG.

In particular, we leverage the Markov property and observe the transition to any time t≥1t\geq 1 depends only on the state of in-neighbors in the previous timestep. Thus, we can ignore the states of pure obligees at time t−1t-1 because they are not in-neighbors to any other nodes, and we only need to consider the set of nodes that act as principals. To formalize this, we introduce the following definition.

###### Definition 4.4 (In-neighbor layers)

For k=1k=1, define

|  |  |  |
| --- | --- | --- |
|  | Δin1≜⋃i∈𝒱δin​(i),\Delta\_{\text{in}}^{1}\triangleq\bigcup\_{i\in\mathcal{V}}\delta\_{\text{in}}(i), |  |

to be the set of nodes that act as principals of another node.
For k>1k>1, define recursively

|  |  |  |
| --- | --- | --- |
|  | Δink≜⋃i∈Δink−1δin​(i),\Delta\_{\text{in}}^{k}\triangleq\bigcup\_{i\in\Delta\_{\text{in}}^{k-1}}\delta\_{\text{in}}(i), |  |

which equivalently consists of all nodes ii such that there exists a directed path of length kk from ii to some node in 𝒱\mathcal{V}.

With this notation, the states of nodes in Δin1\Delta\_{\text{in}}^{1} at time tt depend only on the states of nodes in Δin2\Delta\_{\text{in}}^{2} at time t−1t-1, and so on. This reasoning can be applied recursively until we reach time t−dt-d, where dd is the maximum tree depth of the graph. The set Δind\Delta\_{\text{in}}^{d} contains only pure principals ii, whose failures occur independently and according to fixed rir\_{i} for all time steps. Thus, we do not need to consider earlier times past t−dt-d. In other words, we only need to consider a finite number of earlier time steps to obtain an exact form of the full distribution. [Figure 5](https://arxiv.org/html/2511.05691v1#S4.F5 "In 4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process") gives a visualization of these topological layers. Formalizing this we have the following representation for the distribution of the stochastic process.
{restatable}theoremMixingDAG
If GG is a directed acyclic graph, then for any t≥dt\geq d where d>0d>0 is the maximum tree depth of the graph, and using the in-neighbor layers Δink\Delta\_{\text{in}}^{k} from [Definition 4.4](https://arxiv.org/html/2511.05691v1#S4.Thmtheorem4 "Definition 4.4 (In-neighbor layers) ‣ 4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process"), the stationary distribution admits the following closed form:

|  |  |  |
| --- | --- | --- |
|  | ℙ​(𝐗t=𝐱)=∑𝐱Δin1t−1⋯​∑𝐱Δindt−dℙ​(𝐗t=𝐱∣𝐗Δin1t−1=𝐱Δin1t−1)​∏k=1d−1ℙ​(𝐗Δinkt−k=𝐱Δinkt−k∣𝐗Δink+1t−k−1=𝐱Δink+1t−k−1)​ℙ​(𝐗Δindt−d=𝐱Δindt−d).\mathbb{P}(\mathbf{X}^{t}=\mathbf{x})=\sum\_{\mathbf{x}^{t-1}\_{\Delta\_{\text{in}}^{1}}}\cdots\sum\_{\mathbf{x}^{t-d}\_{\Delta\_{\text{in}}^{d}}}\mathbb{P}(\mathbf{X}^{t}=\mathbf{x}\mid\mathbf{X}^{t-1}\_{\Delta\_{\text{in}}^{1}}=\mathbf{x}^{t-1}\_{\Delta\_{\text{in}}^{1}})\prod\_{k=1}^{d-1}\mathbb{P}(\mathbf{X}^{t-k}\_{\Delta\_{\text{in}}^{k}}=\mathbf{x}^{t-k}\_{\Delta\_{\text{in}}^{k}}\mid\mathbf{X}^{t-k-1}\_{\Delta\_{\text{in}}^{k+1}}=\mathbf{x}^{t-k-1}\_{\Delta\_{\text{in}}^{k+1}})\mathbb{P}(\mathbf{X}^{t-d}\_{\Delta\_{\text{in}}^{d}}=\mathbf{x}\_{\Delta\_{\text{in}}^{d}}^{t-d}). |  |

While the full derivation is technical and omitted from the discussion here (see [Section 9.2](https://arxiv.org/html/2511.05691v1#S9.SS2 "9.2 Section 4.1 Omitted Proofs ‣ 9 Section 4 Omitted Proofs")), we give an explicit representation of the stationary distribution for the Markov chain when the underlying contractor graph is acyclic.
Then for size nn acyclic graphs with directed diameter dd, computing the exact stationary distribution can be done in 𝒪​(d⋅2n)\mathcal{O}(d\cdot 2^{n}) time.
In most cases, this computation can actually be done in much less time, because the sets Δink\Delta\_{\text{in}}^{k} exclude pure obligees and are strictly decreasing in size.

### 4.2 Impact on Global Average Risk

In [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"), we established that under [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"), the marginal failure probabilities of individual nodes increase over time, as shown in [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"). We then used this to establish the monotonicity of 𝔼[ℒ(𝐗t)]\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{t})}}\right]. However, it is not immediately clear whether this monotonicity extends to the full distribution of the global average risk defined over the stochastic process (𝐗t)t∈ℕ(\mathbf{X}^{t})\_{t\in\mathbb{N}}. The rest of this section focuses on establishing that the distribution of global average risk is monotone (i.e. stochastically dominated) with respect to t∈ℕt\in\mathbb{N}, establishing the impact of network risk propagation to long-term financial insolvency.

Our first result formalizes the intuition that, under [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"), the probability of the global failure loss exceeding a given threshold is non-decreasing over time. The proof relies on constructing a coupling argument that establishes a form of stochastic dominance across time steps. This result confirms that as failures accumulate, they are unlikely to be reversed by the system dynamics alone. This reinforces the insight that traditional models, which often assume failures are independent, may underestimate long-term risk exposure when network dependencies are present.

{restatable}

theoremGARIncrease
Under Assumption [3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"), we have that for any ε∈ℝ≥0\varepsilon\in\mathbb{R}\_{\geq 0} and for all t∈ℕt\in\mathbb{N}

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ(ℒ(𝐗t+1)>ε)≥ℙ(ℒ(𝐗t)>ε).\mathbb{P}\mathopen{}\mathclose{{\left(\mathcal{L}(\mathbf{X}^{t+1})>\varepsilon}}\right)\geq\mathbb{P}\mathopen{}\mathclose{{\left(\mathcal{L}(\mathbf{X}^{t})>\varepsilon}}\right). |  | (14) |

As a result,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ(ℒ(𝐗∞)>ε)≥ℙ(ℒ(𝐗0)>ε).\mathbb{P}\mathopen{}\mathclose{{\left(\mathcal{L}(\mathbf{X}^{\infty})>\varepsilon}}\right)\geq\mathbb{P}\mathopen{}\mathclose{{\left(\mathcal{L}(\mathbf{X}^{0})>\varepsilon}}\right). |  | (15) |

Before presenting the proof we note that it leverages several results from muller2002comparison, which we include in [Section 11](https://arxiv.org/html/2511.05691v1#S11 "11 Useful definitions and results") for completeness.

###### Proof 4.5

To prove [Eq. 14](https://arxiv.org/html/2511.05691v1#S4.E14 "In 4.2 Impact on Global Average Risk ‣ 4 Asymptotic Behavior of Stochastic Risk Process"), we first show that for any i∈𝒱i\in\mathcal{V} and t∈ℕt\in\mathbb{N}, Xit⪯stXit+1X\_{i}^{t}\preceq\_{\text{st}}X\_{i}^{t+1} by using Strassen’s Theorem (Roch\_2024, Theorem 4.2.11). Then, we verify that the vectors 𝐗t\mathbf{X}^{t} and 𝐗t+1\mathbf{X}^{t+1} are coupled using the same source of randomness, and thus share a common copula. Therefore, we can conclude by [Theorem 11.1](https://arxiv.org/html/2511.05691v1#S11.Thmtheorem1 "Theorem 11.1 ((muller2002comparison, Theorem 3.3.8)) ‣ 11 Useful definitions and results") (appendix) that 𝐗t⪯st𝐗t+1\mathbf{X}^{t}\preceq\_{\text{st}}\mathbf{X}^{t+1} for all t≥0t\geq 0. Finally, we use the fact that ℒ​(⋅)\mathcal{L}(\cdot) is a monotone increasing function and apply [Theorem 11.2](https://arxiv.org/html/2511.05691v1#S11.Thmtheorem2 "Theorem 11.2 ((muller2002comparison, Theorem 3.3.11)) ‣ 11 Useful definitions and results") (appendix) to conclude that ℒ​(𝐗t)⪯stℒ​(𝐗t+1)\mathcal{L}(\mathbf{X}^{t})\preceq\_{\text{st}}\mathcal{L}(\mathbf{X}^{t+1}), which is equivalent to [Eq. 14](https://arxiv.org/html/2511.05691v1#S4.E14 "In 4.2 Impact on Global Average Risk ‣ 4 Asymptotic Behavior of Stochastic Risk Process").

Thus, we only need to show that Xit⪯stXit+1X\_{i}^{t}\preceq\_{\text{st}}X\_{i}^{t+1} and that the coupling inducing the ordering is defined through a common copula. First, note that {0,1}n\{0,1\}^{n} with the component-wise ordering is a finite poset. By Strassen’s Theorem, Xit⪯stXit+1X\_{i}^{t}\preceq\_{\text{st}}X\_{i}^{t+1} if and only if there exists a coupling (X~it,X~it+1)(\tilde{X}\_{i}^{t},\tilde{X}\_{i}^{t+1}) of (Xit,Xit+1)(X\_{i}^{t},X\_{i}^{t+1}) such that X~it≤X~it+1\tilde{X}\_{i}^{t}\leq\tilde{X}\_{i}^{t+1} almost surely under the coupling.

We now turn our efforts to constructing such a coupling. Recall mit≜𝔼​[Xit]m\_{i}^{t}\triangleq\mathbb{E}[X\_{i}^{t}], and define for each node i∈𝒱i\in\mathcal{V}, Ui​∼i​i​d​Unif​(0,1)U\_{i}\overset{iid}{\sim}\text{Unif}(0,1). For each t≥0t\geq 0, we define the coupled process:

|  |  |  |
| --- | --- | --- |
|  | X~it=𝟙​{Ui≤mit},\tilde{X}\_{i}^{t}=\mathbbm{1}\{U\_{i}\leq m\_{i}^{t}\}, |  |

which is a valid coupling since X~it∼Ber​(mit)\tilde{X}\_{i}^{t}\sim\text{Ber}(m\_{i}^{t}), matching the marginal distribution of XitX\_{i}^{t}. By [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"), we know mit≤mit+1m\_{i}^{t}\leq m\_{i}^{t+1}. Thus, when Ui≤mit≤mit+1U\_{i}\leq m\_{i}^{t}\leq m\_{i}^{t+1}, we get X~it=1=X~it+1\tilde{X}\_{i}^{t}=1=\tilde{X}\_{i}^{t+1}.
Similarly, when Ui>mitU\_{i}>m\_{i}^{t}, then X~it=0\tilde{X}\_{i}^{t}=0, and X~it+1∈{0,1}\tilde{X}\_{i}^{t+1}\in\{0,1\}. Therefore, for every ii and t≥0t\geq 0, we have

|  |  |  |
| --- | --- | --- |
|  | X~it≤X~it+1a.s. under the coupling.\tilde{X}\_{i}^{t}\leq\tilde{X}\_{i}^{t+1}\quad\text{a.s. under the coupling.} |  |

By Strassen’s Theorem, this implies

|  |  |  |
| --- | --- | --- |
|  | Xit⪯stXit+1.X\_{i}^{t}\preceq\_{\text{st}}X\_{i}^{t+1}. |  |

Moreover, because this coupling uses the same uniform random vector 𝐔=(U1,…,Un)\mathbf{U}=(U\_{1},\dots,U\_{n}) across all coordinates ii, the vectors 𝐗t\mathbf{X}^{t} and 𝐗t+1\mathbf{X}^{t+1} are constructed using the same dependence structure. Specifically, since the UiU\_{i} are independent, this induces the product copula C​(u1,…,un)=∏i=1nuiC(u\_{1},\dots,u\_{n})=\prod\_{i=1}^{n}u\_{i} for both 𝐗t\mathbf{X}^{t} and 𝐗t+1\mathbf{X}^{t+1}. Therefore, we conclude by [Theorem 11.1](https://arxiv.org/html/2511.05691v1#S11.Thmtheorem1 "Theorem 11.1 ((muller2002comparison, Theorem 3.3.8)) ‣ 11 Useful definitions and results") that 𝐗t⪯st𝐗t+1.\mathbf{X}^{t}\preceq\_{\text{st}}\mathbf{X}^{t+1}.

Finally, since ℒ​(𝐗t)=∑i=1nβi​Xit\mathcal{L}(\mathbf{X}^{t})=\sum\_{i=1}^{n}\beta\_{i}X\_{i}^{t} is a component-wise increasing function and βi>0\beta\_{i}>0 for all ii, [Theorem 11.2](https://arxiv.org/html/2511.05691v1#S11.Thmtheorem2 "Theorem 11.2 ((muller2002comparison, Theorem 3.3.11)) ‣ 11 Useful definitions and results") ensures that

|  |  |  |
| --- | --- | --- |
|  | ℒ​(𝐗t)⪯stℒ​(𝐗t+1).\mathcal{L}(\mathbf{X}^{t})\preceq\_{\text{st}}\mathcal{L}(\mathbf{X}^{t+1}). |  |

That is, for every ε∈ℝ\varepsilon\in\mathbb{R} and for all t≥0t\geq 0,

|  |  |  |
| --- | --- | --- |
|  | ℙ(ℒ(𝐗t+1)>ε)≥ℙ(ℒ(𝐗t)>ε),\mathbb{P}\mathopen{}\mathclose{{\left(\mathcal{L}(\mathbf{X}^{t+1})>\varepsilon}}\right)\geq\mathbb{P}\mathopen{}\mathclose{{\left(\mathcal{L}(\mathbf{X}^{t})>\varepsilon}}\right), |  |

which shows [Eq. 14](https://arxiv.org/html/2511.05691v1#S4.E14 "In 4.2 Impact on Global Average Risk ‣ 4 Asymptotic Behavior of Stochastic Risk Process"). [Eq. 15](https://arxiv.org/html/2511.05691v1#S4.E15 "In 4.2 Impact on Global Average Risk ‣ 4 Asymptotic Behavior of Stochastic Risk Process") follows since for each ε∈ℝ\varepsilon\in\mathbb{R} the sequence {ℙ​(ℒ​(𝐗t)>ε)}t∈ℕ\{\mathbb{P}(\mathcal{L}(\mathbf{X}^{t})>\varepsilon)\}\_{t\in\mathbb{N}} is non-decreasing. Moreover, by [Fig. 4](https://arxiv.org/html/2511.05691v1#S4.F4 "In 4 Asymptotic Behavior of Stochastic Risk Process"), we have ℒ​(𝐗t)→ℒ​(𝐗∞)\mathcal{L}(\mathbf{X}^{t})\to\mathcal{L}(\mathbf{X}^{\infty}) almost surely, which implies convergence in distribution. Hence, for every continuity point ε\varepsilon of the limiting distribution, we obtain

|  |  |  |
| --- | --- | --- |
|  | limt→∞ℙ​(ℒ​(𝐗t)>ε)=ℙ​(ℒ​(𝐗∞)>ε),\lim\_{t\to\infty}\mathbb{P}\bigl(\mathcal{L}(\mathbf{X}^{t})>\varepsilon\bigr)=\mathbb{P}\bigl(\mathcal{L}(\mathbf{X}^{\infty})>\varepsilon\bigr), |  |

and in particular,
ℙ​(ℒ​(𝐗0)>ε)≤ℙ​(ℒ​(𝐗∞)>ε).\mathbb{P}\bigl(\mathcal{L}(\mathbf{X}^{0})>\varepsilon\bigr)\leq\mathbb{P}\bigl(\mathcal{L}(\mathbf{X}^{\infty})>\varepsilon\bigr).

Theorem [4.2](https://arxiv.org/html/2511.05691v1#S4.SS2 "4.2 Impact on Global Average Risk ‣ 4 Asymptotic Behavior of Stochastic Risk Process") shows that under Assumption [3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"), the entire distribution of global financial loss stochastically dominates the independent failure model. That is, not only does the expected loss increase over time (as in [Corollary 8.10](https://arxiv.org/html/2511.05691v1#S8.Thmtheorem10 "Corollary 8.10 ‣ 8.2 Section 3.3 Omitted Proofs ‣ 8 Section 3 Omitted Proofs")), but the quantiles also become more severe. This has strong implications for surety organizations, as they must retain financial reserves to absorb losses during rare but extreme events. If such tail risks are systematically underestimated (as in ℒ​(𝐗0)\mathcal{L}(\mathbf{X}^{0}) by ignoring network spillovers), then reserve requirements will be miscalibrated.

## 5 Numerical Results

To complement our theoretical guarantees, we conduct extensive computational experiments to evaluate risk propagation in contractor networks. Our experiments are based on a contractor network constructed from empirical data provided by a partnering surety organization. Across all simulations, we evaluate the impact of network effects on global loss and the joint distribution of possible failure events.555See <https://github.com/seanrsinclair/Network-Risk-Analysis-Surety-Bounds> for the code base.The main questions we seek to answer through our experiments are:

* •

  Structure of real-world surety networks ([Section 5.1](https://arxiv.org/html/2511.05691v1#S5.SS1 "5.1 Description of Surety Network ‣ 5 Numerical Results")): We begin with a descriptive overview of an empirical surety network, highlighting its scale, connectivity, and summary statistics of the loss values βi\beta\_{i} and idiosyncratic risk scores rir\_{i} across nodes i∈𝒱i\in\mathcal{V} in the network.
* •

  Case study ([Section 5.2](https://arxiv.org/html/2511.05691v1#S5.SS2 "5.2 Case Study ‣ 5 Numerical Results")): We then present a detailed case study on a representative intermediary, illustrating how local network position affects systemic risk contributions.
* •

  Conditions for higher expected loss and tail behavior ([Section 5.3](https://arxiv.org/html/2511.05691v1#S5.SS3 "5.3 Impact of network effects on global financial loss ‣ 5 Numerical Results")): We analyze when expected losses are amplified and derive empirical tail bounds, emphasizing the increase in global average risk even in networks where [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk") fails.
* •

  Robustness to network exposure αi\alpha\_{i} ([Section 5.4](https://arxiv.org/html/2511.05691v1#S5.SS4 "5.4 Robustness to choice of 𝛼_𝑖 ‣ 5 Numerical Results")): Finally, we test the robustness of our findings under alternative specifications of the exposure parameters αi\alpha\_{i} for intermediaries ii in the network.

#### Network Construction

We build an anonymized contractor network from empirical surety bond data of a partnering surety organization, preserving key structural and statistical properties while protecting sensitive information. Original node identities are replaced with generic indices; contract values, risk scores, and loss amounts are rescaled and perturbed with Laplace noise. The network topology is reconstructed via an edge–rewiring procedure that retains degree distributions, node roles (pure principals, intermediaries, pure obligees), and depth in the hierarchy. Edge weights are recalibrated from the anonymized bond amounts to ensure each obligee’s in-degree sums to one. This produces a synthetic but structurally faithful replica of the real network for simulation and analysis. See [Section 10.1](https://arxiv.org/html/2511.05691v1#S10.SS1 "10.1 Construction of Anonymous Network ‣ 10 Computational Experiments: Additional Details") for further details.

#### Accounting for Unobserved Edges

Since the surety organization only observes bonded contracts with known principals, some obligees may have additional, unobserved contracting activity. We detect such cases by comparing an obligee’s reported revenue to the total value of observed bonded work; any excess implies unobserved principals. To incorporate the potential risk from these missing relationships, we introduce a synthetic “dummy” principal connected to the obligee with weight equal to the fraction of revenue not explained by observed principals. The dummy’s baseline risk is estimated from the observed mix of contractor types the obligee engages with, assuming the same type distribution holds for unobserved contractors. This approach preserves network structure while accounting for external risk exposure not directly visible in the data. Further details on this methodology are included in [Section 10.2](https://arxiv.org/html/2511.05691v1#S10.SS2 "10.2 Accounting for Unobserved Edges ‣ 10 Computational Experiments: Additional Details").

#### Experimental Setup.

We approximate the stationary distribution π\pi of the stochastic process 𝐗t\mathbf{X}^{t} via Monte-Carlo simulation. We set αi=0.25\alpha\_{i}=0.25 for all intermediaries ii in the network, as decided during discussion from our partnering organization. However, later in [Section 5.4](https://arxiv.org/html/2511.05691v1#S5.SS4 "5.4 Robustness to choice of 𝛼_𝑖 ‣ 5 Numerical Results") we test the robustness of our results to this selection. Since our contractor graph is a directed acyclic graph with maximum depth d=7d=7, the chain mixes in finite time (see [Section 4.1](https://arxiv.org/html/2511.05691v1#S4.SS1 "4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process")). Thus, we report the empirical distribution of 𝐗7\mathbf{X}^{7} after t=7t=7 time steps over 100,000100,000 times to form empirical estimates. All metrics are reported as the average over these replications, and confidence intervals are computed with a significance level of δ=0.05\delta=0.05 when presented.

### 5.1 Description of Surety Network

![Refer to caption](x3.png)


Figure 6: Visualization of the giant component in the anonymized empirical network. The left figure corresponds to the adjacency matrix of the weakly connected component of the network, where the xx and yy axes corresponds to different node indices. In the right figure we show the sub adjacency matrix between principals and obligees. Colors correspond to the edge weights wi​jw\_{ij}.

We start off our discussion by examining the contractor network obtained from our partnering surety organization. This network represents the contractual obligations between contractors and project owners insured by the surety, with each edge corresponding to a surety bond over a one-year period in 2018.

The full contractor graph contains 40,457 nodes (contracting organizations). The majority of these nodes belong to a single (weakly-connected) component, which accounts for roughly 87.7% of the graph and contains 35,483 nodes. We focus on this weakly connected component for the remainder of our simulations. Within this component, there are 8,984 pure principals (contractors who never act as obligees), making up roughly 25% of the nodes; 26,137 are pure obligees (project owners who never act as principals), accounting for 74%; and the remaining 362 nodes (about 1%) are intermediaries that appear as both principals and obligees in different contracts. This composition reflects the predominantly bipartite nature of the network, with only a small fraction of nodes serving the dual roles of both principal and obligee. However, we will see that these intermediaries are the key vehicle for risk to propagate through the network.

![Refer to caption](x4.png)


Figure 7: Histogram of the weighted out degree distribution for pure principals and intermediaries. Counts are shown on a logarithmic scale. Pure obligees are not included since their out-degree is zero by design.

See [Fig. 6](https://arxiv.org/html/2511.05691v1#S5.F6 "In 5.1 Description of Surety Network ‣ 5 Numerical Results") for a visualization of the adjacency matrix of our surety network. We emphasize that the graph is mostly bipartite, with the exception of a small number of intermediaries. We further note that the connectivity pattern in the graph is sparse: among the 35,483 nodes in the giant connected component the edge density is around 0.009%, representing 56,707 contracts. The nature of the graph also reveals interesting structural properties — it is acyclic with a directed diameter of seven. This acyclic structure has important implications for our modeling: our stochastic failure-propagation process converges to its stationary distribution in at most seven time steps (see [Definition 4.4](https://arxiv.org/html/2511.05691v1#S4.Thmtheorem4 "Definition 4.4 (In-neighbor layers) ‣ 4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process")). Lastly, we note some degree of heterogeneity in degree distribution across nodes, witnessed in [Fig. 7](https://arxiv.org/html/2511.05691v1#S5.F7 "In 5.1 Description of Surety Network ‣ 5 Numerical Results").

In addition to network topology, we measure the idiosyncratic risk scores rir\_{i} and loss-given-default values βi\beta\_{i} for each principal ii.
These features, shown in [Figure 8](https://arxiv.org/html/2511.05691v1#S5.F8 "In 5.1 Description of Surety Network ‣ 5 Numerical Results"), are heavy-tailed and right-skewed, with notable heterogeneity across node types. In particular, we observe that the βi\beta\_{i} values for intermediaries are, on average, larger than that of pure principals. However, for the risk scores rir\_{i}, pure principals have larger idiosyncratic risk. We emphasize that pure obligees are excluded from these plots because their risk and loss values are set to zero by definition.
The loss-given-default distribution also contains a single extreme outlier of approximately $31 billion; while rare, such high values can occur in large infrastructure projects underwritten by the surety organization.
Later in our analysis, we will explore how these attributes vary between pure principals and intermediaries, and how their heterogeneity influences network-wide risk propagation.

![Refer to caption](x5.png)

![Refer to caption](x6.png)

Figure 8: Histograms of idiosyncratic default probabilities rir\_{i} (left) and loss given default values βi\beta\_{i} in millions of USD (right). Both counts and values are shown on a logarithmic scale. Pure obligees are excluded here because their values for both attributes are set to zero by definition.

### 5.2 Case Study

![Refer to caption](x7.png)

![Refer to caption](x8.png)

Figure 9: Case study for node 39466. On the left we show its induced sub-graph of the contractor network, where green nodes correspond to principals, pink to other intermediaries, and blue to pure obligees. On the right we plot a histogram of the risk scores rir\_{i} (x-axis) against counts for the upstream neighbors. The red dotted line corresponds to the average risk score of the upstream neighbors, the orange to the risk score of node 39466, and the black line to the induced limiting failure probability m39466m\_{39466} of node 39466.

Before diving into our simulations on the weakly connected component of the network, we begin with an illustrative case study. While we emphasize that the nodes here do not refer to specific contractors, in our collaboration with the partnering insurance company we performed a similar methodological analysis that they leveraged for identifying and monitoring risk in key contractors.

We focus on node 39466, which contracts as an *intermediary* (has both incoming and outgoing edges). According to our risk-based centrality measure uiu\_{i} (cf. [Definition 3.1](https://arxiv.org/html/2511.05691v1#S3.Thmtheorem1 "Definition 3.1 ‣ 3.2 Identifying the Impact of Network Structure ‣ 3 Mean Field Analysis of Expected Risk")), this node lies in the 75th percentile of the distribution among intermediaries, marking it as structurally “risky” due to its prominent position in the network. Its induced subgraph ([Fig. 9](https://arxiv.org/html/2511.05691v1#S5.F9 "In 5.2 Case Study ‣ 5 Numerical Results"), left) shows both upstream principals and downstream obligees, highlighting its central role in bridging multiple tiers of the contracting system. This centrality measure thus provides a systematic way of flagging such intermediaries as candidates for closer attention.

Turning to the upstream neighbors’ risk distribution ([Fig. 9](https://arxiv.org/html/2511.05691v1#S5.F9 "In 5.2 Case Study ‣ 5 Numerical Results"), right), we observe substantial heterogeneity: some neighbors have risk scores lower than node 39466’s idiosyncratic value r39466=0.00182r\_{39466}=0.00182, while others are considerably higher. While some neighbors are less risky, when incorporating these exposures, the induced limiting failure probability increases to m39466=0.00264m\_{39466}=0.00264, corresponding to a relative increase of roughly  45%\,45\%. This amplification illustrates how even a moderately risky intermediary, once identified through the u39466u\_{39466} centrality metric, can see its effective default probability substantially elevated due to network position and contracting relationships.

### 5.3 Impact of network effects on global financial loss

Next we begin to illustrate the impact of network risk on the global average financial loss in the surety network. We start by recalling in [Sections 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk") and [4.2](https://arxiv.org/html/2511.05691v1#S4.SS2 "4.2 Impact on Global Average Risk ‣ 4 Asymptotic Behavior of Stochastic Risk Process") that under [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"), both the average risk and the tail probability mass of the loss distribution increases.
However, this assumption is not always satisfied in our surety network (see more discussion on this in [Section 10.3](https://arxiv.org/html/2511.05691v1#S10.SS3 "10.3 Real-World Network Satisfying Section 3.3 ‣ 10 Computational Experiments: Additional Details")).

![Refer to caption](x9.png)

![Refer to caption](x10.png)

Figure 10: Comparison of node-level risk metrics. (Left) Idiosyncratic default probabilities rir\_{i} compared to limiting failure probabilities mim\_{i} for intermediaries ii. (Right) Box plots of βi​ri\beta\_{i}r\_{i} (left) vs. βi​mi\beta\_{i}m\_{i} (right), where βi\beta\_{i} is in USD (log scale).

Despite this, we observe that for a nontrivial subset of nodes i∈𝒱i\in\mathcal{V}, the expected marginal loss probability mim\_{i} exceeds their idiosyncratic risk scores rir\_{i}. This effect is visible in [Fig. 10](https://arxiv.org/html/2511.05691v1#S5.F10 "In 5.3 Impact of network effects on global financial loss ‣ 5 Numerical Results"), which compares rir\_{i} (x-axis) and mim\_{i} (y-axis), with numerous points above the y=xy=x line. Moreover, as a result of this, the expected aggregate loss 𝔼[ℒ(𝐗∞)]=β⊤𝐦\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{\infty})}}\right]=\beta^{\top}\mathbf{m} increases from the expected aggregate loss under the independent failure model 𝔼[ℒ(𝐗0)]=β⊤𝐫\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{0})}}\right]=\beta^{\top}\mathbf{r} by 1.89%. This emphasizes that failing to account for network interference causes downstream risk to be under-estimated. While 1.89% might seem like a mild value, we emphasize that the units for these are on the order of hundreds of millions of dollars, so this increase is roughly on the order of 2 million dollars of underestimated risk. See [Fig. 10](https://arxiv.org/html/2511.05691v1#S5.F10 "In 5.3 Impact of network effects on global financial loss ‣ 5 Numerical Results") where we also include a box plot of βi​mi\beta\_{i}m\_{i} vs βi​ri\beta\_{i}r\_{i} across nodes i∈𝒱i\in\mathcal{V}. Here we observe not only does the average increase, but βi​mi\beta\_{i}m\_{i} is more right-skewed. This again emphasizes the ability for network risk to destabilize the network.

Lastly, we look at the distribution of ℒ​(𝐗∞)\mathcal{L}(\mathbf{X}^{\infty}) versus ℒ​(𝐗0)\mathcal{L}(\mathbf{X}^{0}).
Table [1](https://arxiv.org/html/2511.05691v1#S5.T1 "Table 1 ‣ 5.3 Impact of network effects on global financial loss ‣ 5 Numerical Results") reports several quantiles of the two distributions, including the 50th, 90th, 95th, 99th, and 99.5th percentiles. In every case, the quantile under ℒ​(𝐗∞)\mathcal{L}(\mathbf{X}^{\infty}) exceeds the corresponding quantile under ℒ​(𝐗0)\mathcal{L}(\mathbf{X}^{0}).
These plots reveal a clear shift in the distribution. Not only is the right tail substantially heavier, indicating a higher probability of extreme loss realizations, but the central behavior is also affected; the median aggregate loss under ℒ​(𝐗∞)\mathcal{L}(\mathbf{X}^{\infty}) is noticeably larger than that under ℒ​(𝐗0)\mathcal{L}(\mathbf{X}^{0}), in addition to the mean being higher. This combination of a heavier tail and an upward shift in the bulk of the distribution highlights that the amplification of network interactions are not just confined to rare catastrophic events, but also manifest across the entire distribution as well.

|  | ℒ​(𝐗0)\mathcal{L}(\mathbf{X}^{0}) | ℒ​(𝐗∞)\mathcal{L}(\mathbf{X}^{\infty}) |
| --- | --- | --- |
| 0.5 | 188.71±0.33188.71\pm 0.33 | 193.24⋆±0.33{\bf 193.24^{\star}\pm 0.33} |
| 0.9 | 344.92±0.80344.92\pm 0.80 | 349.16⋆±0.74{\bf 349.16^{\star}\pm 0.74} |
| 0.95 | 404.75±0.99404.75\pm 0.99 | 410.03⋆±1.02{\bf 410.03^{\star}\pm 1.02} |
| 0.99 | 536.35±2.40536.35\pm 2.40 | 559.99±3.08⋆{\bf 559.99\pm 3.08^{\star}} |
| 0.995 | 597.16±4.33597.16\pm 4.33 | 652.92±5.68⋆{\bf 652.92\pm 5.68^{\star}} |

Table 1: Comparison of the quantiles (in millions of dollars) of ℒ​(𝐗∞)\mathcal{L}(\mathbf{X}^{\infty}) to ℒ​(𝐗0)\mathcal{L}(\mathbf{X}^{0}). Confidence intervals computed with a two-sided binomial quantile test. Bold indicates larger for the same quantile, and ⋆\star that the increase is significant from the two-sided binomial quantile test.

To summarize, these results suggest that only considering the independent failure model without accounting for how the interconnectedness of contractors creates correlations in defaults leads to underestimating the potential losses incurred by failures. This can have significant repercussions in practice, such as from failing to set aside enough capital to cover large tail probability losses due to this underestimation.

### 5.4 Robustness to choice of αi\alpha\_{i}

![Refer to caption](x11.png)


Figure 11: Quantiles of ℒ​(𝐗∞)\mathcal{L}(\mathbf{X}^{\infty}) under different values of α\alpha in ten equal spaces between [0,1][0,1]. Confidence intervals computed with a two-sided binomial quantile test.

We close out by testing the robustness of our earlier empirical insights with respect to the choice of α\alpha, where the baseline specification set αi=0.25\alpha\_{i}=0.25 for all intermediaries ii in the network. In [Fig. 11](https://arxiv.org/html/2511.05691v1#S5.F11 "In 5.4 Robustness to choice of 𝛼_𝑖 ‣ 5 Numerical Results"), we report the quantiles of ℒ​(𝐗∞)\mathcal{L}(\mathbf{X}^{\infty}) as a function of α∈[0,1]\alpha\in[0,1], applied uniformly across all intermediaries. Across all specifications, the outcomes remain monotone in α\alpha: greater exposure consistently increases systemic risk. This finding is noteworthy because the formal monotonicity condition ([Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk")) does not hold in our empirical network. If it did, [Section 4.2](https://arxiv.org/html/2511.05691v1#S4.SS2 "4.2 Impact on Global Average Risk ‣ 4 Asymptotic Behavior of Stochastic Risk Process") would guarantee this result; the fact that monotonicity emerges regardless highlights the robustness of our conclusions.

More broadly, the extent of amplification is not uniform across the loss distribution. While moderate quantiles exhibit only gradual upward shifts as α\alpha increases, the tail behavior is dramatically more sensitive. For example, at the 0.9950.995 quantile we observe a sharp and disproportionate increase, indicating that the risk of catastrophic losses escalates much faster than median losses. This widening gap across quantiles highlights how network contagion disproportionately impacts the extreme right tail. Taken together, [Fig. 11](https://arxiv.org/html/2511.05691v1#S5.F11 "In 5.4 Robustness to choice of 𝛼_𝑖 ‣ 5 Numerical Results") conveys two critical insights: (i) our monotonicity results are robust in practice, even when their sufficient conditions are partially violated, and (ii) the most severe consequences of increasing α\alpha manifest in the extremes of the distribution, where insurers and policymakers are most vulnerable.

## 6 Conclusion

In this work, we introduced a network-based approach to analyzing risk propagation in surety-backed contractor networks. By modeling contractual dependencies as a directed stochastic process, we demonstrated that network effects systematically amplify failure probabilities and increase expected loss beyond what traditional independent risk models predict. Our theoretical results establish conditions under which systemic risk accumulates over time, and our empirical analysis using real-world surety data validates these findings, showing that accounting for network dependencies leads to a higher estimated risk exposure than independent models. Additionally, we identified key intermediary nodes that disproportionately influence network-wide stability, highlighting their role in amplifying or mitigating failures.

Several future directions emerge from our work. First, while our analysis focused on risk propagation in a static network, real-world contractor networks evolve over time as firms form new contracts or exit the market. Extending our model to a dynamic setting, where network structure evolves alongside risk accumulation, is a promising avenue for further research. Second, our framework assumes full network observability by the surety provider, yet in practice, some contractual relationships may be hidden due to the presence of multiple insurers or informal agreements. Developing robust risk estimation techniques that account for missing or latent network information would enhance the applicability of our approach. Finally, while we focused on financial surety networks, similar risk propagation dynamics arise in other interdependent systems, such as supply chains, infrastructure networks, and research collaborations. Extending our methods to these domains could provide new insights into systemic vulnerabilities and optimal risk mitigation strategies.

Acknowledgments. Part of this work was done while Sean R. Sinclair was a Postdoctoral Associate at Massachusetts Institute of Technology advised by Ali Jadbabaie and Devavrat Shah. The authors would also like to thank Alireza Tahbaz-Salehi for preliminary feedback on the network surety model. Icons for [Fig. 1](https://arxiv.org/html/2511.05691v1#S1.F1 "In 1 Introduction") are provided by flaticon2025. Finally, we gratefully acknowledge the partnership of an anonymous surety organization for providing data and insights that made this research possible.

{APPENDICES}

## 7 Table of Notation

| Symbol | Definition |
| --- | --- |
| Problem setting specifications | |
| 𝒢=(𝒱,ℰ)\mathcal{G}=(\mathcal{V},\mathcal{E}) | Network surety graph |
| i,j,k∈𝒱i,j,k\in\mathcal{V} | Index over nodes in the graph |
| (j,i)∈ℰ(j,i)\in\mathcal{E} | Directed edge from principal (subcontractor) jj to obligee (project owner) ii |
| δin​(i)\delta\_{\text{in}}(i) | Principals (in-neighbors) of obligee ii, δin​(i)={j:(i,j)∈ℰ}\delta\_{\text{in}}(i)=\{j:(i,j)\in\mathcal{E}\} |
| δout​(j)\delta\_{\text{out}}(j) | Obligees (out-neighbors) of principal jj, δout​(j)={i:(i,j)∈ℰ}\delta\_{\text{out}}(j)=\{i:(i,j)\in\mathcal{E}\} |
| wi​j∈[0,1]w\_{ij}\in[0,1] | Fraction of obligee ii’s projects contracted to principal jj, where ∑j∈δin​(i)wi​j≤1\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}\leq 1 |
| 𝐖∈ℝ|𝒱|×|𝒱|\mathbf{W}\in\mathbb{R}^{|\mathcal{V}|\times|\mathcal{V}|} | Weighted adjacency matrix with entries wi​jw\_{ij} |
| pure obligee | Node ii such that δout​(i)=0\delta\_{\text{out}}(i)=0 |
| pure principal | Node jj such that δin​(j)=0\delta\_{\text{in}}(j)=0 |
| rir\_{i} | Risk score for node ii (ri=0r\_{i}=0 if ii is a pure obligee) |
| 𝐫∈ℝ|𝒱|\mathbf{r}\in\mathbb{R}^{|\mathcal{V}|} | Column vector of idiosyncratic risk scores with entries rir\_{i} |
| αi∈[0,1]\alpha\_{i}\in[0,1] | Probability of network effects (αj=0,αi=1\alpha\_{j}=0,\alpha\_{i}=1 for pure principals jj and obligees ii) |
| βi\beta\_{i} | Financial loss for each node i∈𝒱i\in\mathcal{V} |
| 𝐀∈ℝ|𝒱|×|𝒱|\mathbf{A}\in\mathbb{R}^{|\mathcal{V}|\times|\mathcal{V}|} | Diagonal matrix of αi\alpha\_{i} |
| 𝐗t\mathbf{X}^{t} | Stochastic process for node failures at step tt |
| π\pi | Stationary distribution for 𝐗t\mathbf{X}^{t} |
| 𝐦t\mathbf{m}^{t} | Vector of failure probabilities with entries mit=𝔼[Xit]m\_{i}^{t}=\mathbb{E}\mathopen{}\mathclose{{\left[X\_{i}^{t}}}\right] |
| 𝐦\mathbf{m} | limt→∞𝐦t\lim\_{t\rightarrow\infty}\mathbf{m}^{t}, the limiting failure probabilities for each node |
| 𝟏{\mathbf{1}} | Column vector of all ones, dimensions may vary based on context |
| τ1,…,τT\tau\_{1},\dots,\tau\_{T} | Product segment IDs indicating the type of work performed |
| type​(i)\textsf{type}(i) | Product segment ID of node ii, type​(i)∈{τ1,…,τT}\textsf{type}(i)\in\{\tau\_{1},\dots,\tau\_{T}\} |
| r¯i\overline{r}\_{i} | Median risk score in ii’s product segment, r¯i=median​({rj:type​(j)=type​(i)})\overline{r}\_{i}=\text{median}(\{r\_{j}\,:\,\textsf{type}(j)=\textsf{type}(i)\}) |
| 𝐮∈ℝ|𝒱|\mathbf{u}\in\mathbb{R}^{|\mathcal{V}|} | risk-based centrality in equilibrium model, 𝐮=(𝐈−𝐀)​(𝐈−𝐖⊤​𝐀)−1​𝟏n\mathbf{u}=(\mathbf{I}-\mathbf{A})(\mathbf{I}-\mathbf{W}^{\top}\mathbf{A})^{-1}\frac{\mathbf{1}}{n} |
| ℒ​(𝐱)\mathcal{L}(\mathbf{x}) | Weighted average risk: ∑vβv​xv\sum\_{v}\beta\_{v}x\_{v} |

Table 2: Common notation

## 8 [Section 3](https://arxiv.org/html/2511.05691v1#S3 "3 Mean Field Analysis of Expected Risk") Omitted Proofs

### 8.1 [Section 3.1](https://arxiv.org/html/2511.05691v1#S3.SS1 "3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk") Omitted Proofs

We start off by analyzing the mean field dynamics of our stochastic process and showing the mean failure probabilities satisfy a similar dynamics to the original process.

\MeanFieldRecurrence

\*

###### Proof 8.1

The case when t=0t=0 immediately follows since Xi0∼Bernoulli​(ri)X\_{i}^{0}\sim\textsf{Bernoulli}(r\_{i}). For the step case we use the law of total probability and the Markov property of the Markov chain to have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | mit+1=𝔼[Xit+1]\displaystyle m\_{i}^{t+1}=\mathbb{E}\mathopen{}\mathclose{{\left[X\_{i}^{t+1}}}\right] | =𝔼[𝔼[Xit+1∣𝐗t]]=𝔼[(1−αi)ri+αi∑j∈δin​(i)wi​jXjt]\displaystyle=\mathbb{E}\mathopen{}\mathclose{{\left[\mathbb{E}\mathopen{}\mathclose{{\left[X\_{i}^{t+1}\mid\mathbf{X}^{t}}}\right]}}\right]=\mathbb{E}\mathopen{}\mathclose{{\left[(1-\alpha\_{i})r\_{i}+\alpha\_{i}\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}X\_{j}^{t}}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1−αi)ri+αi∑j∈δin​(i)wi​j𝔼[Xjt]=(1−αi)ri+αi∑j∈δin​(i)wi​jmjt,\displaystyle=(1-\alpha\_{i})r\_{i}+\alpha\_{i}\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}\mathbb{E}\mathopen{}\mathclose{{\left[X\_{j}^{t}}}\right]=(1-\alpha\_{i})r\_{i}+\alpha\_{i}\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}m\_{j}^{t}, |  |

where the second equality follows by [Eq. 1](https://arxiv.org/html/2511.05691v1#S2.E1 "In Stochastic Risk Propagation. ‣ 2 Network Model Definition"), and the final equality by an inductive argument.

Our first main result for the mean field shows that the limiting failure probabilities indeed exist and satisfy a fixed point equation.

\InverseFixedPoint

\*
Before presenting the proof of [Section 3.1](https://arxiv.org/html/2511.05691v1#S3.SS1 "3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk"), we start off with the following technical lemma.

\SecondNormBounded

\*

###### Proof 8.2

Since 𝐀𝐖\mathbf{A}\mathbf{W} is row sub-stochastic, we have that ∥𝐀𝐖∥≤1\lVert\mathbf{A}\mathbf{W}\rVert\leq 1. Additionally, for all pure obligees ii we have set αi=1\alpha\_{i}=1, so their corresponding row sums satisfy ∑j(𝐀𝐖)i​j=αi​∑jwi​j=1\sum\_{j}(\mathbf{A}\mathbf{W})\_{ij}=\alpha\_{i}\sum\_{j}w\_{ij}=1. Thus by construction, ‖𝐀𝐖‖=1\|\mathbf{A}\mathbf{W}\|=1, which does not necessarily imply that powers of 𝐀𝐖\mathbf{A}\mathbf{W} are decreasing in size.
We can, however, show that ∥(𝐀𝐖)2∥<1\lVert(\mathbf{A}\mathbf{W})^{2}\rVert<1. In particular, the row sums of (𝐀𝐖)2(\mathbf{A}\mathbf{W})^{2} are given by:

|  |  |  |
| --- | --- | --- |
|  | ∑j∈𝒱(𝐀𝐖)i​j2=∑j∈𝒱∑k∈𝒱αi​αk​wi​k​wk​j=αi​∑k∈𝒱αk​wi​k​∑j∈𝒱wk​j≤∑k∈𝒱αk​wi​k.\sum\_{j\in\mathcal{V}}(\mathbf{A}\mathbf{W})^{2}\_{ij}=\sum\_{j\in\mathcal{V}}\sum\_{k\in\mathcal{V}}\alpha\_{i}\alpha\_{k}w\_{ik}w\_{kj}=\alpha\_{i}\sum\_{k\in\mathcal{V}}\alpha\_{k}w\_{ik}\sum\_{j\in\mathcal{V}}w\_{kj}\leq\sum\_{k\in\mathcal{V}}\alpha\_{k}w\_{ik}. |  |

If wi​k>0w\_{ik}>0, node kk cannot be a pure obligee and αk\alpha\_{k} must be strictly less than 1.
Therefore, the row sums are strictly less than 1:

|  |  |  |
| --- | --- | --- |
|  | ∑j∈𝒱(𝐀𝐖)i​j2≤∑k∈𝒱αk​wi​k<∑k∈𝒱wi​k≤1,\sum\_{j\in\mathcal{V}}(\mathbf{A}\mathbf{W})^{2}\_{ij}\leq\sum\_{k\in\mathcal{V}}\alpha\_{k}w\_{ik}<\sum\_{k\in\mathcal{V}}w\_{ik}\leq 1, |  |

and ‖(𝐀𝐖)2‖<1\|(\mathbf{A}\mathbf{W})^{2}\|<1.
Then sub-multiplicativity of the norm implies that higher powers of 𝐀𝐖\mathbf{A}\mathbf{W} are decaying in size.
Even powers are bounded ‖(𝐀𝐖)2​k‖≤‖(𝐀𝐖)2‖k<1\|(\mathbf{A}\mathbf{W})^{2k}\|\leq\|(\mathbf{A}\mathbf{W})^{2}\|^{k}<1, and odd powers can be bounded by even powers: ‖(𝐀𝐖)2​k+1‖≤‖(𝐀𝐖)2​k‖​‖𝐀𝐖‖≤‖(𝐀𝐖)2​k‖.\|(\mathbf{A}\mathbf{W})^{2k+1}\|\leq\|(\mathbf{A}\mathbf{W})^{2k}\|\|\mathbf{A}\mathbf{W}\|\leq\|(\mathbf{A}\mathbf{W})^{2k}\|. Using that ∥(𝐀𝐖)2∥<1\lVert(\mathbf{A}\mathbf{W})^{2}\rVert<1 we get that (𝐀𝐖)t→0(\mathbf{A}\mathbf{W})^{t}\rightarrow 0 as required.

Using [Fig. 3](https://arxiv.org/html/2511.05691v1#S3.F3 "In 3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk") we can show the following corollary.

\Neumann

\*

###### Proof 8.3

The Neumann series of 𝐀𝐖\mathbf{A}\mathbf{W} satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∥∑t=0∞(𝐀𝐖)t∥\displaystyle\mathopen{}\mathclose{{\left\|\sum\_{t=0}^{\infty}(\mathbf{A}\mathbf{W})^{t}}}\right\| | ≤∑t=0∞∥(𝐀𝐖)t∥≤∑t=0∞∥𝐀𝐖∥t=∑k=0∞∥𝐀𝐖∥2​k+∥𝐀𝐖∥2​k+1\displaystyle\leq\sum\_{t=0}^{\infty}\mathopen{}\mathclose{{\left\|(\mathbf{A}\mathbf{W})^{t}}}\right\|\leq\sum\_{t=0}^{\infty}\mathopen{}\mathclose{{\left\|\mathbf{A}\mathbf{W}}}\right\|^{t}=\sum\_{k=0}^{\infty}\mathopen{}\mathclose{{\left\|\mathbf{A}\mathbf{W}}}\right\|^{2k}+\mathopen{}\mathclose{{\left\|\mathbf{A}\mathbf{W}}}\right\|^{2k+1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​∑k=0∞‖(𝐀𝐖)2‖k=21−‖(𝐀𝐖)2‖.\displaystyle\leq 2\sum\_{k=0}^{\infty}\|(\mathbf{A}\mathbf{W})^{2}\|^{k}=\frac{2}{1-\|(\mathbf{A}\mathbf{W})^{2}\|}. |  |

Since the operator norm of the series converges absolutely to a finite value, the limit of the series is well-defined.
In particular, the Neumann series converges to the inverse of (𝐈−𝐀𝐖)(\mathbf{I}-\mathbf{A}\mathbf{W}):

|  |  |  |
| --- | --- | --- |
|  | limt→∞(𝐈−𝐀𝐖)∑k=0t(𝐀𝐖)k=limt→∞(∑k=0t(𝐀𝐖)k−∑k=0t(𝐀𝐖)k+1)=limt→∞𝐈−(𝐀𝐖)t+1=𝐈,\lim\_{t\rightarrow\infty}(\mathbf{I}-\mathbf{A}\mathbf{W})\sum\_{k=0}^{t}(\mathbf{A}\mathbf{W})^{k}=\lim\_{t\rightarrow\infty}\mathopen{}\mathclose{{\left(\sum\_{k=0}^{t}(\mathbf{A}\mathbf{W})^{k}-\sum\_{k=0}^{t}(\mathbf{A}\mathbf{W})^{k+1}}}\right)=\lim\_{t\rightarrow\infty}\mathbf{I}-(\mathbf{A}\mathbf{W})^{t+1}=\mathbf{I}, |  |

using that ‖(𝐀𝐖)t‖≤‖𝐀𝐖‖t→0\|(\mathbf{A}\mathbf{W})^{t}\|\leq\|\mathbf{A}\mathbf{W}\|^{t}\rightarrow 0 and that (𝐀𝐖)t→𝟎.(\mathbf{A}\mathbf{W})^{t}\rightarrow\mathbf{0}.

With the previous results in hand, we are finally ready to show [Section 3.1](https://arxiv.org/html/2511.05691v1#S3.SS1 "3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk").

###### Proof 8.4

[Section 3.1](https://arxiv.org/html/2511.05691v1#S3.SS1 "3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk")
First via [Eq. 3](https://arxiv.org/html/2511.05691v1#S3.E3 "In 3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk") we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐦t+1=(𝐈−𝐀)​𝐫+𝐀𝐖𝐦t.\mathbf{m}^{t+1}=(\mathbf{I}-\mathbf{A})\mathbf{r}+\mathbf{A}\mathbf{W}\mathbf{m}^{t}. |  | (16) |

By expanding out the previous equation we have that:

|  |  |  |
| --- | --- | --- |
|  | 𝐦t+1=∑k<t+1(𝐀𝐖)k​(𝐈−𝐀)​𝐫+(𝐀𝐖)t+1​𝐫.\mathbf{m}^{t+1}=\sum\_{k<t+1}(\mathbf{A}\mathbf{W})^{k}(\mathbf{I}-\mathbf{A})\mathbf{r}+(\mathbf{A}\mathbf{W})^{t+1}\mathbf{r}. |  |

However, in [Fig. 3](https://arxiv.org/html/2511.05691v1#S3.F3 "In 3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk") we showed that the Neumann series ∑t=0∞(𝐀𝐖)t\sum\_{t=0}^{\infty}(\mathbf{A}\mathbf{W})^{t} converges to (𝐈−𝐀𝐖)−1(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}. Hence, it follows that

|  |  |  |
| --- | --- | --- |
|  | limt→∞𝐦t+1=limt→∞∑k<t+1(𝐀𝐖)k​(𝐈−𝐀)​𝐫+(𝐀𝐖)t+1​𝐫=(𝐈−𝐀𝐖)−1​(𝐈−𝐀)​𝐫=𝐦.\lim\_{t\rightarrow\infty}\mathbf{m}^{t+1}=\lim\_{t\rightarrow\infty}\sum\_{k<t+1}(\mathbf{A}\mathbf{W})^{k}(\mathbf{I}-\mathbf{A})\mathbf{r}+(\mathbf{A}\mathbf{W})^{t+1}\mathbf{r}=(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}(\mathbf{I}-\mathbf{A})\mathbf{r}=\mathbf{m}. |  |

\LimitingConvergenceRateAcyclic

\*

###### Proof 8.5

Using the fact that ∥(𝐀𝐖)2∥<1\lVert(\mathbf{A}\mathbf{W})^{2}\rVert<1 by [Fig. 3](https://arxiv.org/html/2511.05691v1#S3.F3 "In 3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk") we look at the vector 𝐦t−𝐦\mathbf{m}^{t}-\mathbf{m} to have:

|  |  |  |
| --- | --- | --- |
|  | (𝐦t−𝐦)=−∑k=t∞(𝐀𝐖)k​(𝐈−𝐀)​𝐫+(𝐀𝐖)t​𝐫.(\mathbf{m}^{t}-\mathbf{m})=-\sum\_{k=t}^{\infty}(\mathbf{A}\mathbf{W})^{k}(\mathbf{I}-\mathbf{A})\mathbf{r}+(\mathbf{A}\mathbf{W})^{t}\mathbf{r}. |  |

By the triangle inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∥𝐦t−𝐦∥\displaystyle\lVert\mathbf{m}^{t}-\mathbf{m}\rVert | ≤∥∑k≥t(𝐀𝐖)k​(𝐈−𝐀)​𝐫∥∞+∥(𝐀𝐖)t​𝐫∥∞,\displaystyle\leq\lVert\textstyle\sum\_{k\geq t}(\mathbf{A}\mathbf{W})^{k}(\mathbf{I}-\mathbf{A})\mathbf{r}\rVert\_{\infty}+\lVert(\mathbf{A}\mathbf{W})^{t}\mathbf{r}\rVert\_{\infty}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤∥(𝐀𝐖)t∥​∥𝐫∥∞​(∥∑k≥0(𝐀𝐖)k∥​∥𝐈−𝐀∥+1),\displaystyle\leq\lVert(\mathbf{A}\mathbf{W})^{t}\rVert\lVert\mathbf{r}\rVert\_{\infty}\Big(\lVert\textstyle\sum\_{k\geq 0}(\mathbf{A}\mathbf{W})^{k}\rVert\lVert\mathbf{I}-\mathbf{A}\rVert+1\Big), |  | (Cauchy-Schwarz) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(1+∑k≥0∥(𝐀𝐖)k∥)​∥𝐫∥∞​∥(𝐀𝐖)t∥.\displaystyle\leq\Big(1+\textstyle\sum\_{k\geq 0}\lVert(\mathbf{A}\mathbf{W})^{k}\rVert\Big)\lVert\mathbf{r}\rVert\_{\infty}\lVert(\mathbf{A}\mathbf{W})^{t}\rVert. |  |

Using that

|  |  |  |
| --- | --- | --- |
|  | ∑k≥0∥(𝐀𝐖)k∥≤∑k≥0∥(𝐀𝐖)2∥⌊k/2⌋=2​∑k≥0∥(𝐀𝐖)2∥k=21−∥(𝐀𝐖)2∥,\sum\_{k\geq 0}\lVert(\mathbf{A}\mathbf{W})^{k}\rVert\leq\sum\_{k\geq 0}\lVert(\mathbf{A}\mathbf{W})^{2}\rVert^{\lfloor k/2\rfloor}=2\sum\_{k\geq 0}\lVert(\mathbf{A}\mathbf{W})^{2}\rVert^{k}=\frac{2}{1-\lVert(\mathbf{A}\mathbf{W})^{2}\rVert}, |  |

we then get:

|  |  |  |
| --- | --- | --- |
|  | ∥𝐦t−𝐦∥∞≤(1+21−∥(𝐀𝐖)2∥)∥𝐫∥∞∥(𝐀𝐖)2∥⌊t/2⌋.\lVert\mathbf{m}^{t}-\mathbf{m}\rVert\_{\infty}\leq\mathopen{}\mathclose{{\left(1+\frac{2}{1-\lVert(\mathbf{A}\mathbf{W})^{2}\rVert}}}\right)\lVert\mathbf{r}\rVert\_{\infty}\lVert(\mathbf{A}\mathbf{W})^{2}\rVert^{\lfloor t/2\rfloor}. |  |

Next suppose that GG is a directed acyclic graph. Then the last property can be shown from the fact that (𝐀𝐖)t=0(\mathbf{A}\mathbf{W})^{t}=0 for all t>dt>d.
To see why this is, we observe that each entry is (𝐀𝐖)i​jt=∑(v0=i,…,vt=j)∈𝒱t∏k=0t−1αvk​wvk,vk+1>0(\mathbf{A}\mathbf{W})^{t}\_{ij}=\sum\_{(v\_{0}=i,\dots,v\_{t}=j)\in\mathcal{V}^{t}}\prod\_{k=0}^{t-1}\alpha\_{v\_{k}}w\_{v\_{k},v\_{k+1}}>0 if and only if (v0,…,vt)(v\_{0},\dots,v\_{t}) is a length tt path from v0v\_{0} to vtv\_{t}.
Since the longest path contains dd edges, it follows that all entries of (𝐀𝐖)t(\mathbf{A}\mathbf{W})^{t} are zero and 𝐦t=∑k≤d(𝐀𝐖)k​(𝐈−𝐀)​𝐫=𝐦\mathbf{m}^{t}=\sum\_{k\leq d}(\mathbf{A}\mathbf{W})^{k}(\mathbf{I}-\mathbf{A})\mathbf{r}=\mathbf{m} for t>dt>d.
In fact, we also have that 𝐦d=𝐦\mathbf{m}^{d}=\mathbf{m} because (𝐀𝐖)d(\mathbf{A}\mathbf{W})^{d} is only nonzero in columns corresponding to pure principals with αi=0\alpha\_{i}=0, so (𝐀𝐖)d=(𝐀𝐖)d​(𝐈−𝐀)(\mathbf{A}\mathbf{W})^{d}=(\mathbf{A}\mathbf{W})^{d}(\mathbf{I}-\mathbf{A}).
Then 𝐦d=∑k<d(𝐀𝐖)k​(𝐈−𝐀)​𝐫+(𝐀𝐖)d​(𝐈−𝐀)​𝐫=𝐦\mathbf{m}^{d}=\sum\_{k<d}(\mathbf{A}\mathbf{W})^{k}(\mathbf{I}-\mathbf{A})\mathbf{r}+(\mathbf{A}\mathbf{W})^{d}(\mathbf{I}-\mathbf{A})\mathbf{r}=\mathbf{m}.

### 8.2 [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk") Omitted Proofs

\AssumptionMeanIncrease

\*

We show the result through the combination of the following lemmas.

###### Lemma 8.6

Under [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"), increasing the exposure to risk from the network αi\alpha\_{i} of any intermediary i∈𝒱i\in\mathcal{V} can only increase default probabilities in 𝐦\mathbf{m}.
That is, all entries of 𝐦\mathbf{m} are monotonically non-decreasing with respect to αi\alpha\_{i}:

|  |  |  |
| --- | --- | --- |
|  | ∂𝐦∂αi=(𝐈−𝐀𝐖)−1∂𝐀∂αi[𝐖𝐦−𝐫]≥ 0.\frac{\partial\mathbf{m}}{\partial\alpha\_{i}}=(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\frac{\partial\mathbf{A}}{\partial\alpha\_{i}}\mathopen{}\mathclose{{\left[\mathbf{W}\mathbf{m}-\mathbf{r}}}\right]\;\geq\;\mathbf{0}. |  |

###### Proof 8.7

The vector derivative of 𝐦=(𝐈−𝐀𝐖)−1​(𝐈−𝐀)​𝐫\mathbf{m}=(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}(\mathbf{I}-\mathbf{A})\mathbf{r} with respect to αi\alpha\_{i} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂𝐦∂αi\displaystyle\frac{\partial\mathbf{m}}{\partial\alpha\_{i}} | =∂∂αi[(𝐈−𝐀𝐖)−1×(𝐈−𝐀)𝐫]\displaystyle=\frac{\partial}{\partial\alpha\_{i}}\mathopen{}\mathclose{{\left[(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\times(\mathbf{I}-\mathbf{A})\mathbf{r}}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∂(𝐈−𝐀𝐖)−1∂αi​(𝐈−𝐀)​𝐫+(𝐈−𝐀𝐖)−1​∂(𝐈−𝐀)​𝐫∂αi\displaystyle=\frac{\partial(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}}{\partial\alpha\_{i}}(\mathbf{I}-\mathbf{A})\mathbf{r}+(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\frac{\partial(\mathbf{I}-\mathbf{A})\mathbf{r}}{\partial\alpha\_{i}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−(𝐈−𝐀𝐖)−1​∂(𝐈−𝐀𝐖)∂αi​(𝐈−𝐀𝐖)−1​(𝐈−𝐀)​𝐫+(𝐈−𝐀𝐖)−1​∂(𝐈−𝐀)∂αi​𝐫\displaystyle=-(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\frac{\partial(\mathbf{I}-\mathbf{A}\mathbf{W})}{\partial\alpha\_{i}}(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}(\mathbf{I}-\mathbf{A})\mathbf{r}+(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\frac{\partial(\mathbf{I}-\mathbf{A})}{\partial\alpha\_{i}}\mathbf{r} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(𝐈−𝐀𝐖)−1​∂𝐀∂αi​𝐖​(𝐈−𝐀𝐖)−1​(𝐈−𝐀)​𝐫⏟𝐦−(𝐈−𝐀𝐖)−1​∂𝐀∂αi​𝐫\displaystyle=(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\frac{\partial\mathbf{A}}{\partial\alpha\_{i}}\mathbf{W}\underbrace{(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}(\mathbf{I}-\mathbf{A})\mathbf{r}}\_{\mathbf{m}}-(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\frac{\partial\mathbf{A}}{\partial\alpha\_{i}}\mathbf{r} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(𝐈−𝐀𝐖)−1​∂𝐀∂αi​(𝐖𝐦−𝐫).\displaystyle=(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\frac{\partial\mathbf{A}}{\partial\alpha\_{i}}(\mathbf{W}\mathbf{m}-\mathbf{r}). |  |

Because 𝐀𝐖\mathbf{A}\mathbf{W} is row sub-stochastic and non-negative, (𝐈−𝐀𝐖)−1=∑t=0∞(𝐀𝐖)t⪰𝟎(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}=\sum\_{t=0}^{\infty}(\mathbf{A}\mathbf{W})^{t}\succeq\mathbf{0} is also non-negative.
Additionally, ∂𝐀∂αi⪰𝟎\frac{\partial\mathbf{A}}{\partial\alpha\_{i}}\succeq\mathbf{0} is a diagonal matrix with zero entries for all rows corresponding to pure principals and pure obligees, since their entries are fixed as 0 and 1 in 𝐀\mathbf{A}.
We will multiply (𝐖𝐦−𝐫)(\mathbf{W}\mathbf{m}-\mathbf{r}) by ∂𝐀∂αi\frac{\partial\mathbf{A}}{\partial\alpha\_{i}} from the left, which will give a vector ∂𝐀∂αi​(𝐖𝐦−𝐫)\frac{\partial\mathbf{A}}{\partial\alpha\_{i}}(\mathbf{W}\mathbf{m}-\mathbf{r}) whose only nonzero entries are those corresponding to intermediaries.
From [Corollary 8.10](https://arxiv.org/html/2511.05691v1#S8.Thmtheorem10 "Corollary 8.10 ‣ 8.2 Section 3.3 Omitted Proofs ‣ 8 Section 3 Omitted Proofs") and [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"), we have that for all intermediaries ii,

|  |  |  |
| --- | --- | --- |
|  | (𝐖𝐦−𝐫)i=(∑j∈δin​(i)wi​j​mj)−ri≥(∑j∈δin​(i)wi​j​rj)−ri≥0.(\mathbf{W}\mathbf{m}-\mathbf{r})\_{i}=\Big(\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}m\_{j}\Big)-r\_{i}\geq\Big(\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}r\_{j}\Big)-r\_{i}\geq 0. |  |

Then ∂𝐀∂αi​(𝐖𝐦−𝐫)≥\frac{\partial\mathbf{A}}{\partial\alpha\_{i}}(\mathbf{W}\mathbf{m}-\mathbf{r})\geq, and the vector derivative ∂𝐦∂αi≥𝟎\frac{\partial\mathbf{m}}{\partial\alpha\_{i}}\geq\mathbf{0} is non-negative.

###### Lemma 8.8

Under Assumption [3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"), for all i∈𝒱i\in\mathcal{V} and t∈ℕt\in\mathbb{N} the mean failure probabilities mitm\_{i}^{t} are monotone with respect to tt, i.e.

|  |  |  |
| --- | --- | --- |
|  | mit+1≥mit.m\_{i}^{t+1}\geq m\_{i}^{t}. |  |

Hence, for all tt and ii, mi≥mitm\_{i}\geq m\_{i}^{t}.

###### Proof 8.9

We will show the property by induction for each node i∈𝒱i\in\mathcal{V}.

Base Case (t=0)(t=0):

|  |  |  |  |
| --- | --- | --- | --- |
|  | mi1\displaystyle m\_{i}^{1} | =(1−αi)ri+αi∑j∈δin​(i)wi​j𝔼[Xj0]=(1−αi)ri+αi∑j∈δin​(i)wi​jrj\displaystyle=(1-\alpha\_{i})r\_{i}+\alpha\_{i}\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}\mathbb{E}\mathopen{}\mathclose{{\left[X\_{j}^{0}}}\right]=(1-\alpha\_{i})r\_{i}+\alpha\_{i}\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}r\_{j} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥A​[3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk")​(1−αi)​ri+αi​ri=ri=mi0.\displaystyle\underset{A\ref{ass:larger\_neighbors}}{\geq}(1-\alpha\_{i})r\_{i}+\alpha\_{i}r\_{i}=r\_{i}=m\_{i}^{0}. |  |

Step Case (t→t+1)(t\rightarrow t+1): By definition of the mean failure probabilities,

|  |  |  |
| --- | --- | --- |
|  | {mit+1=(1−αi)​ri+αi​∑j∈δin​(i)wi​j​mjt,mit=(1−αi)​ri+αi​∑j∈δin​(i)wi​j​mjt−1.\begin{cases}m\_{i}^{t+1}=(1-\alpha\_{i})r\_{i}+\alpha\_{i}\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}m\_{j}^{t},\\ m\_{i}^{t}=(1-\alpha\_{i})r\_{i}+\alpha\_{i}\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}m\_{j}^{t-1}.\end{cases} |  |

Thus,

|  |  |  |
| --- | --- | --- |
|  | mit+1−mit=αi​∑j=1nwi​j​(mjt−mjt−1)​≥(I.H.)​0⟹mit+1≥mit,for all ​i∈𝒱.m\_{i}^{t+1}-m\_{i}^{t}=\alpha\_{i}\sum\_{j=1}^{n}w\_{ij}(m\_{j}^{t}-m\_{j}^{t-1})\underset{(\text{I.H.})}{\geq}0\implies m\_{i}^{t+1}\geq m\_{i}^{t},\quad\text{for all }i\in\mathcal{V}. |  |

Therefore, mit+1≥mitm\_{i}^{t+1}\geq m\_{i}^{t} as required.

###### Corollary 8.10

Under [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"), we have that for all t∈ℕt\in\mathbb{N},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼[ℒ(𝐗t+1)]≥𝔼[ℒ(𝐗t)].\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{t+1})}}\right]\geq\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{t})}}\right]. |  | (17) |

Hence, we have that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼[ℒ(𝐗∞)]≥𝔼[ℒ(𝐗0)].\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{\infty})}}\right]\geq\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{0})}}\right]. |  | (18) |

###### Proof 8.11

Since ℒ​(𝐗t)=∑i=1nβi​Xit\mathcal{L}(\mathbf{X}^{t})=\sum\_{i=1}^{n}\beta\_{i}X\_{i}^{t},
with βi>0\beta\_{i}>0 for all ii, [Eq. 17](https://arxiv.org/html/2511.05691v1#S8.E17 "In Corollary 8.10 ‣ 8.2 Section 3.3 Omitted Proofs ‣ 8 Section 3 Omitted Proofs") follows by linearity of expectation and [Lemma 8.8](https://arxiv.org/html/2511.05691v1#S8.Thmtheorem8 "Lemma 8.8 ‣ 8.2 Section 3.3 Omitted Proofs ‣ 8 Section 3 Omitted Proofs"), and [Eq. 18](https://arxiv.org/html/2511.05691v1#S8.E18 "In Corollary 8.10 ‣ 8.2 Section 3.3 Omitted Proofs ‣ 8 Section 3 Omitted Proofs") follows by taking the limit as t→∞t\to\infty and the continuous mapping theorem and the linearity of ℒ​(⋅)\mathcal{L}(\cdot).

An obvious question remains as to whether the reverse is true under [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"), i.e. if intermediaries have lower risk principals on average then the mean failure probabilities are monotone decreasing. Indeed, a straightforward extension to the previous discussion establishes the following:

###### Corollary 8.12

If all intermediaries i∈𝒱i\in\mathcal{V} have lower risk principals on average, i.e. ∑j∈δin​(i)wi​j​rj≤ri\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}r\_{j}\leq r\_{i}, then 𝐦t+1≤𝐦t\mathbf{m}^{t+1}\leq\mathbf{m}^{t} and 𝔼​[ℒ​(𝐗t+1)]≤𝔼​[ℒ​(𝐗t)]\mathbb{E}[\mathcal{L}(\mathbf{X}^{t+1})]\leq\mathbb{E}[\mathcal{L}(\mathbf{X}^{t})], which imply that

|  |  |  |
| --- | --- | --- |
|  | 𝐦≤𝐫,𝔼​[ℒ​(𝐗∞)]≤𝔼​[ℒ​(𝐗0)].\mathbf{m}\leq\mathbf{r},\hskip 20.00003pt\mathbb{E}[\mathcal{L}(\mathbf{X}^{\infty})]\leq\mathbb{E}[\mathcal{L}(\mathbf{X}^{0})]. |  |

Furthermore, ∂𝐦∂αi=(𝐈−𝐀𝐖)−1∂𝐀∂αi[𝐖𝐦−𝐫]≤ 0.\frac{\partial\mathbf{m}}{\partial\alpha\_{i}}=(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\frac{\partial\mathbf{A}}{\partial\alpha\_{i}}\mathopen{}\mathclose{{\left[\mathbf{W}\mathbf{m}-\mathbf{r}}}\right]\;\leq\;\mathbf{0}.

###### Proof 8.13

We can follow arguments similar to those in [Lemmas 8.8](https://arxiv.org/html/2511.05691v1#S8.Thmtheorem8 "Lemma 8.8 ‣ 8.2 Section 3.3 Omitted Proofs ‣ 8 Section 3 Omitted Proofs"), [8.10](https://arxiv.org/html/2511.05691v1#S8.Thmtheorem10 "Corollary 8.10 ‣ 8.2 Section 3.3 Omitted Proofs ‣ 8 Section 3 Omitted Proofs") and [8.8](https://arxiv.org/html/2511.05691v1#S8.Thmtheorem8 "Lemma 8.8 ‣ 8.2 Section 3.3 Omitted Proofs ‣ 8 Section 3 Omitted Proofs") by replacing ≥\geq with ≤\leq where appropriate to show that similar statements hold for the opposite direction.

\MeanFieldGap

\*

###### Proof 8.14

To show this claim we start off with the following lemma:

###### Lemma 8.15

For any contractor graph GG and all t∈ℕt\in\mathbb{N}, under [Remark 3.2](https://arxiv.org/html/2511.05691v1#S3.Thmtheorem2 "Remark 3.2 ‣ 3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk") we have

|  |  |  |
| --- | --- | --- |
|  | 𝐦t≥ft​(δ)​𝐫,\mathbf{m}^{t}\geq f\_{t}(\delta)\,\mathbf{r}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | ft​(δ):={𝐈,t=0,𝐈+δ​∑k=0t−1(𝐀𝐖)k​𝐀,t≥1.f\_{t}(\delta):=\begin{cases}\mathbf{I},&t=0,\\[6.0pt] \mathbf{I}+\delta\sum\_{k=0}^{t-1}(\mathbf{A}\mathbf{W})^{k}\mathbf{A},&t\geq 1.\end{cases} |  |

###### Proof 8.16

First we argue that under [Remark 3.2](https://arxiv.org/html/2511.05691v1#S3.Thmtheorem2 "Remark 3.2 ‣ 3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"), we have that for all nodes ii:

|  |  |  |
| --- | --- | --- |
|  | αi​wi⊤​𝐫≥(1+δ)​αi​ri,\alpha\_{i}w\_{i}^{\top}\mathbf{r}\geq(1+\delta)\alpha\_{i}r\_{i}, |  |

where wi⊤=[wi​1wi​2…wi​n]w\_{i}^{\top}=[w\_{i1}\quad w\_{i2}\quad\dots\quad w\_{in}] denotes the iith row in 𝐖\mathbf{W}.
For any pure principal ii we have αi=0\alpha\_{i}=0, so both sides are zero and the inequality is trivially satisfied. For pure obligees ii ri=0r\_{i}=0, and so again the inequality is trivially satisfied. Then for intermediaries with αi∈(0,1)\alpha\_{i}\in(0,1), the inequality is precisely [Remark 3.2](https://arxiv.org/html/2511.05691v1#S3.Thmtheorem2 "Remark 3.2 ‣ 3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk").
Thus, we have that 𝐀𝐖𝐫≥(1+δ)​𝐀𝐫\mathbf{A}\mathbf{W}\mathbf{r}\geq(1+\delta)\mathbf{A}\mathbf{r}.

We now show the result by considering the change in 𝐦t\mathbf{m}^{t} at each step.
In the first step, we have that

|  |  |  |
| --- | --- | --- |
|  | 𝐦1=(𝐈−𝐀)​𝐫+𝐀𝐖𝐦0=(𝐈−𝐀)​𝐫+𝐀𝐖𝐫⏟≥(1+δ)​𝐀𝐫≥r+δ​𝐀𝐫,\mathbf{m}^{1}=(\mathbf{I}-\mathbf{A})\mathbf{r}+\mathbf{A}\mathbf{W}\mathbf{m}^{0}=(\mathbf{I}-\mathbf{A})\mathbf{r}+\underbrace{\mathbf{A}\mathbf{W}\mathbf{r}}\_{\geq(1+\delta)\mathbf{A}\mathbf{r}}\geq r+\delta\mathbf{A}\mathbf{r}, |  |

i.e. 𝐦1−𝐦0≥δ​𝐀𝐫\mathbf{m}^{1}-\mathbf{m}^{0}\geq\delta\mathbf{A}\mathbf{r}.
Then [Section 3.1](https://arxiv.org/html/2511.05691v1#S3.SS1 "3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk") implies that 𝐦t+1−𝐦t=(𝐀𝐖)t​(𝐦1−𝐦0)\mathbf{m}^{t+1}-\mathbf{m}^{t}=(\mathbf{A}\mathbf{W})^{t}(\mathbf{m}^{1}-\mathbf{m}^{0}), so we have that 𝐦t+1−𝐦t≥δ​(𝐀𝐖)t​𝐀𝐫\mathbf{m}^{t+1}-\mathbf{m}^{t}\geq\delta(\mathbf{A}\mathbf{W})^{t}\mathbf{A}\mathbf{r}.
Then

|  |  |  |
| --- | --- | --- |
|  | 𝐦t=(𝐦t−𝐦t−1)+⋯+(𝐦1−𝐦0)+𝐦0≥𝐫+δ​∑k=0t−1(𝐀𝐖)k​𝐀𝐫,\mathbf{m}^{t}=(\mathbf{m}^{t}-\mathbf{m}^{t-1})+\cdots+(\mathbf{m}^{1}-\mathbf{m}^{0})+\mathbf{m}^{0}\geq\mathbf{r}+\delta\sum\_{k=0}^{t-1}(\mathbf{A}\mathbf{W})^{k}\mathbf{A}\mathbf{r}, |  |

which shows that 𝐦t≥[𝐈+δ​∑k=0t−1(𝐀𝐖)k​𝐀]​𝐫=ft​(δ)​𝐫\mathbf{m}^{t}\geq\Big[\mathbf{I}+\delta\sum\_{k=0}^{t-1}(\mathbf{A}\mathbf{W})^{k}\mathbf{A}\Big]\mathbf{r}=f\_{t}(\delta)\mathbf{r}.

Using [Lemma 8.15](https://arxiv.org/html/2511.05691v1#S8.Thmtheorem15 "Lemma 8.15 ‣ Proof 8.14 ‣ 8.2 Section 3.3 Omitted Proofs ‣ 8 Section 3 Omitted Proofs") and taking the limit as t→∞t\rightarrow\infty we have that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐦\displaystyle\mathbf{m} | ≥(limt→∞ft​(δ))​𝐫,\displaystyle\geq(\lim\_{t\rightarrow\infty}f\_{t}(\delta))\mathbf{r}, |  |

where we can use the interchange, since all of the limits exist. However,

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→∞ft​(δ)\displaystyle\lim\_{t\rightarrow\infty}f\_{t}(\delta) | =limt→∞𝐈+δ​∑k=0t−1(𝐀𝐖)k​𝐀\displaystyle=\lim\_{t\rightarrow\infty}\mathbf{I}+\delta\sum\_{k=0}^{t-1}(\mathbf{A}\mathbf{W})^{k}\mathbf{A} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝐈+δ​limt→∞∑k=0t−1(𝐀𝐖)k​𝐀\displaystyle=\mathbf{I}+\delta\lim\_{t\rightarrow\infty}\sum\_{k=0}^{t-1}(\mathbf{A}\mathbf{W})^{k}\mathbf{A} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝐈+δ​𝐀​(𝐈−𝐀𝐖)−1​𝐀\displaystyle=\mathbf{I}+\delta\mathbf{A}(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\mathbf{A} |  |

where in the last line we used the Von-Neumann expansion for a matrix (see [Fig. 3](https://arxiv.org/html/2511.05691v1#S3.F3 "In 3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk")). Rearranging this expression gives that 𝐦−𝐫≥δ​(𝐈−𝐀𝐖)−1​𝐀𝐫\mathbf{m}-\mathbf{r}\geq\delta(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\mathbf{A}\mathbf{r}.

Moreover, we also have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼[ℒ(𝐗∞)]\displaystyle\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{\infty})}}\right] | =∑iβi​𝐦i=β⊤​𝐦\displaystyle=\sum\_{i}\beta\_{i}\mathbf{m}\_{i}=\beta^{\top}\mathbf{m} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥β⊤(𝐈+δ(𝐈−𝐀𝐖)−1𝐀)𝐫=β⊤𝐫+δβ⊤(𝐈−𝐀𝐖)−1𝐀𝐫=𝔼[ℒ(𝐗0)]+δβ⊤(𝐈−𝐀𝐖)−1𝐀𝐫.\displaystyle\geq\beta^{\top}(\mathbf{I}+\delta(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\mathbf{A})\mathbf{r}=\beta^{\top}\mathbf{r}+\delta\beta^{\top}(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\mathbf{A}\mathbf{r}=\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{0})}}\right]+\delta\beta^{\top}(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\mathbf{A}\mathbf{r}. |  |

## 9 [Section 4](https://arxiv.org/html/2511.05691v1#S4 "4 Asymptotic Behavior of Stochastic Risk Process") Omitted Proofs

\MarkovChainStationary

\*

###### Proof 9.1

The fact that 𝐗t\mathbf{X}^{t} is a Markov chain over the finite state space {0,1}n\{0,1\}^{n} follows immediately from our construction; that is, (𝐗t)t∈ℕ(\mathbf{X}^{t})\_{t\in\mathbb{N}} is a sequence of random variables that satisfy the Markov property
ℙ​(𝐗t+1=𝐱t+1∣𝐗t,…,𝐗0)=ℙ​(𝐗t+1=𝐱t+1∣𝐗t)\mathbb{P}(\mathbf{X}^{t+1}=\mathbf{x}^{t+1}\mid\mathbf{X}^{t},\dots,\mathbf{X}^{0})=\mathbb{P}(\mathbf{X}^{t+1}=\mathbf{x}^{t+1}\mid\mathbf{X}^{t})
for all tt.
We will restrict our attention to states 𝐱t∈{0,1}n\mathbf{x}^{t}\in\{0,1\}^{n} that are *feasible*, in the sense that there exists some time tt such that ℙ​(𝐗t=𝐱t)>0\mathbb{P}(\mathbf{X}^{t}=\mathbf{x}^{t})>0.
The Markov chain 𝐗t\mathbf{X}^{t} has a unique stationary distribution if it is *ergodic* (irreducible, positive recurrent) and *aperiodic* over the feasible state space (resnick2013adventures). Thus, we wish to show that all feasible states can reach each other in a finite number of steps, and that at least one feasible state has a self-loop, so 𝐗t\mathbf{X}^{t} is also aperiodic whenever it is ergodic.

Before we show that self-loops exist and that the Markov chain is ergodic, we characterize the states that can be reached in one step from a given current state.
Conditioning on a feasible current state 𝐗t=𝐱t\mathbf{X}^{t}=\mathbf{x}^{t}, nodes fail or do not fail independently in the following time step, so we can consider the conditional default probability of each node individually.
We first consider principals (pure principals and intermediaries). Because we require ri∈(0,1)r\_{i}\in(0,1) and αi<1\alpha\_{i}<1 for all principals ii, all of their default probabilities lie strictly between zero and one. More formally, the probability of any principal ii failing in the next step satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0<(1−αi)​ri≤ℙ​(Xit+1=1∣𝐗t=𝐱t)≤(1−αi)​ri+αi<1,0<(1-\alpha\_{i})r\_{i}\leq\mathbb{P}(X\_{i}^{t+1}=1\mid\mathbf{X}^{t}=\mathbf{x}^{t})\leq(1-\alpha\_{i})r\_{i}+\alpha\_{i}<1, |  | (19) |

for any time tt and feasible state 𝐱t\mathbf{x}^{t}. Intuitively, this property holds for principals because their default probability contains an idiosyncratic component.
Pure obligees, on the other hand, can only fail (or not fail) if one of their principals failed (or did not fail) in the previous time step.
For any pure obligee i∈Oi\in O, feasible 𝐱t\mathbf{x}^{t}, and xit+1∈{0,1}x^{t+1}\_{i}\in\{0,1\},

|  |  |  |
| --- | --- | --- |
|  | ℙ(Xit+1=xit+1∣𝐗t=𝐱t)=∑j∈δin​(i)wi​j𝟙{xjt=xit+1}>0\mathbb{P}(X^{t+1}\_{i}=x^{t+1}\_{i}\mid\mathbf{X}^{t}=\mathbf{x}^{t})=\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}\mathds{1}\mathopen{}\mathclose{{\left\{x^{t}\_{j}=x^{t+1}\_{i}}}\right\}>0 |  |

if and only if at least one principal is currently in state xit+1x^{t+1}\_{i}.
Then conditional independence implies

|  |  |  |
| --- | --- | --- |
|  | ℙ​(𝐗t+1=𝐱t+1∣𝐗t=𝐱t)=∏j∈Nℙ​(Xjt+1=xjt+1∣𝐗t=𝐱t)⏟>0​∀j​∏i∈Oℙ​(Xit+1=xit+1∣𝐗t=𝐱t)⏟>0​ iff. ​{j∈δin​(i)∣xjt=xit+1}⁣≠∅.\mathbb{P}(\mathbf{X}^{t+1}=\mathbf{x}^{t+1}\mid\mathbf{X}^{t}=\mathbf{x}^{t})=\prod\_{j\in N}\underbrace{\mathbb{P}(X^{t+1}\_{j}=x^{t+1}\_{j}\mid\mathbf{X}^{t}=\mathbf{x}^{t})}\_{>0\;\forall j}\prod\_{i\in O}\underbrace{\mathbb{P}(X^{t+1}\_{i}=x^{t+1}\_{i}\mid\mathbf{X}^{t}=\mathbf{x}^{t})}\_{>0\text{ iff. }\{j\in\delta\_{\text{in}}(i)\mid x^{t}\_{j}=x^{t+1}\_{i}\}\neq\varnothing}. |  |

Thus we have the following necessary and sufficient condition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(𝐗t+1=𝐱t+1∣𝐗t=𝐱t)>0⇔{j∈δin​(i)∣xjt=xit+1}≠∅, for all pure obligees ​i.\mathbb{P}(\mathbf{X}^{t+1}=\mathbf{x}^{t+1}\mid\mathbf{X}^{t}=\mathbf{x}^{t})>0\iff\{j\in\delta\_{\text{in}}(i)\mid x^{t}\_{j}=x^{t+1}\_{i}\}\neq\varnothing,\text{ for all pure obligees }i. |  | (20) |

This shows that we can usually go between any two states in one step, with the only exception being when [Equation 20](https://arxiv.org/html/2511.05691v1#S9.E20 "In Proof 9.1 ‣ 9 Section 4 Omitted Proofs") does not hold.
In other words, we can reach 𝐱t+1\mathbf{x}^{t+1} from 𝐱t\mathbf{x}^{t} in one step as long as the states of principals in 𝐱t\mathbf{x}^{t} “coincide” with the states of pure obligees in 𝐱t+1\mathbf{x}^{t+1}.
We can now apply the above discussion to show aperiodicity and ergodicity of the Markov chain.
x
We first wish to show that there exists a feasible state 𝐱t\mathbf{x}^{t} with a self-loop, so that we can guarantee aperiodicity whenever we have ergodicity.
From [Equation 20](https://arxiv.org/html/2511.05691v1#S9.E20 "In Proof 9.1 ‣ 9 Section 4 Omitted Proofs") it follows that 𝐱t\mathbf{x}^{t} has a self-loop, i.e.
ℙ​(𝐗t+1=𝐱t∣𝐗t=𝐱t)>0,\mathbb{P}(\mathbf{X}^{t+1}=\mathbf{x}^{t}\mid\mathbf{X}^{t}=\mathbf{x}^{t})>0,
if and only if
{j∈δin​(i)∣xjt=xit}≠∅.\{j\in\delta\_{\text{in}}(i)\mid x^{t}\_{j}=x^{t}\_{i}\}\neq\varnothing.
Additionally, at least one such state always exists: the state in which no nodes fail, i.e. the vector of all zeros 𝐱=𝟎\mathbf{x}=\mathbf{0}. We define Xi0∼Bernoulli​(ri)X^{0}\_{i}\sim\text{Bernoulli}(r\_{i}) as independent random variables with ri<1r\_{i}<1, so
ℙ​(𝐗0=𝟎)=∏i∈𝒱(1−ri)>0.\mathbb{P}(\mathbf{X}^{0}=\mathbf{0})=\prod\_{i\in\mathcal{V}}(1-r\_{i})>0.
Therefore, we have that 𝐱t=𝟎\mathbf{x}^{t}=\mathbf{0} is a feasible state in which all pure obligees ii satisfy

|  |  |  |
| --- | --- | --- |
|  | {j∈δin​(i)∣xjt=xit}={j∈δin​(i)∣𝟎jt=𝟎it}=δin​(i)≠∅,\{j\in\delta\_{\text{in}}(i)\mid x\_{j}^{t}=x\_{i}^{t}\}=\{j\in\delta\_{\text{in}}(i)\mid\mathbf{0}\_{j}^{t}=\mathbf{0}\_{i}^{t}\}=\delta\_{\text{in}}(i)\neq\varnothing, |  |

so we always have at least one feasible state with a self-loop.

Next we show that the Markov chain is ergodic. Let 𝐱t+2\mathbf{x}^{t+2} and 𝐱t\mathbf{x}^{t} denote two arbitrary feasible states in the Markov chain. We claim that ℙ​(𝐗t+2=𝐱t+2∣𝐗t=𝐱t)>0\mathbb{P}(\mathbf{X}^{t+2}=\mathbf{x}^{t+2}\mid\mathbf{X}^{t}=\mathbf{x}^{t})>0 because we can always construct some state 𝐱t+1\mathbf{x}^{t+1} satisfying ℙ​(𝐗t+2=𝐱t+2∣𝐗t+1=𝐱t+1)>0\mathbb{P}(\mathbf{X}^{t+2}=\mathbf{x}^{t+2}\mid\mathbf{X}^{t+1}=\mathbf{x}^{t+1})>0 and ℙ​(𝐗t+1=𝐱t+1∣𝐗t=𝐱t)>0\mathbb{P}(\mathbf{X}^{t+1}=\mathbf{x}^{t+1}\mid\mathbf{X}^{t}=\mathbf{x}^{t})>0.
We will use the fact that no principals j∈δin​(i)j\in\delta\_{\text{in}}(i) of any pure obligee ii can be contained in the set of pure obligees and [Equation 20](https://arxiv.org/html/2511.05691v1#S9.E20 "In Proof 9.1 ‣ 9 Section 4 Omitted Proofs") to show that we can set the states of principals and pure obligees in 𝐱t+1\mathbf{x}^{t+1} separately, making it possible to coordinate with both 𝐱t\mathbf{x}^{t} and 𝐱t+2\mathbf{x}^{t+2}. In particular, we can set the states of principals in 𝐱t+1\mathbf{x}^{t+1} so that the states of pure obligees in 𝐱t+2\mathbf{x}^{t+2} are reachable, then set the states of pure obligees in 𝐱t+1\mathbf{x}^{t+1} to be reachable from the states of principals in 𝐱t\mathbf{x}^{t}.

We begin by observing that for any feasible 𝐱t+2\mathbf{x}^{t+2}, there must be some feasible 𝐱~t+1\tilde{\mathbf{x}}^{t+1} such that
ℙ​(𝐗t+2=𝐱t+2∣𝐗t+1=𝐱~t+1)>0.\mathbb{P}(\mathbf{X}^{t+2}=\mathbf{x}^{t+2}\mid\mathbf{X}^{t+1}=\tilde{\mathbf{x}}^{t+1})>0.
However, no pure obligees can be a principal in δin​(i)\delta\_{\text{in}}(i) for any node ii, so their realized states at time t+1t+1 do not influence any default probabilities at time t+2t+2:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(Xit+2=xit+2∣𝐗t+1=𝐱~t+1)\displaystyle\mathbb{P}(X^{t+2}\_{i}=x^{t+2}\_{i}\mid\mathbf{X}^{t+1}=\tilde{\mathbf{x}}^{t+1}) | =(1−xit+2)+(2​xit+2−1)​((1−αi)​ri+αi​∑j∈δin​(i)wi​j​x~jt+1)\displaystyle=(1-x^{t+2}\_{i})+(2x^{t+2}\_{i}-1)\Big((1-\alpha\_{i})r\_{i}+\alpha\_{i}\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}\tilde{x}^{t+1}\_{j}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙ(Xit+2=xit+2∣Xjt+1=x~jt+1∀j∈δin(i)).\displaystyle=\mathbb{P}\mathopen{}\mathclose{{\left(X^{t+2}\_{i}=x^{t+2}\_{i}\mid X^{t+1}\_{j}=\tilde{x}^{t+1}\_{j}\;\forall j\in\delta\_{\text{in}}(i)}}\right). |  |

That is, for any feasible state 𝐱t+1\mathbf{x}^{t+1} such that xjt+1=x~jt+1x^{t+1}\_{j}=\tilde{x}^{t+1}\_{j} for all principals jj, its transition probabilities are the same as those of 𝐱~t+1\tilde{\mathbf{x}}^{t+1}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(𝐗t+2=𝐱t+2∣𝐗t+1=𝐱~t+1)\displaystyle\mathbb{P}(\mathbf{X}^{t+2}=\mathbf{x}^{t+2}\mid\mathbf{X}^{t+1}=\tilde{\mathbf{x}}^{t+1}) | =∏i∈𝒱ℙ(Xit+2=xit+2∣Xjt+1=x~jt+1=xjt+1∀j∈δin(i))\displaystyle=\prod\_{i\in\mathcal{V}}\mathbb{P}\mathopen{}\mathclose{{\left(X^{t+2}\_{i}=x^{t+2}\_{i}\mid X^{t+1}\_{j}=\tilde{x}^{t+1}\_{j}=x^{t+1}\_{j}\;\forall j\in\delta\_{\text{in}}(i)}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙ​(𝐗t+2=𝐱t+2∣𝐗t+1=𝐱t+1)>0.\displaystyle=\mathbb{P}(\mathbf{X}^{t+2}=\mathbf{x}^{t+2}\mid\mathbf{X}^{t+1}=\mathbf{x}^{t+1})>0. |  |

We can then arbitrarily set the states of pure obligees ii in 𝐱t+1\mathbf{x}^{t+1} so that we also satisfy
ℙ​(𝐗t+1=𝐱t+1∣𝐗t=𝐱t)>0\mathbb{P}(\mathbf{X}^{t+1}=\mathbf{x}^{t+1}\mid\mathbf{X}^{t}=\mathbf{x}^{t})>0
by letting xit+1=x~jtx^{t+1}\_{i}=\tilde{x}^{t}\_{j} for any j∈δin​(i)j\in\delta\_{\text{in}}(i). Using [Equation 20](https://arxiv.org/html/2511.05691v1#S9.E20 "In Proof 9.1 ‣ 9 Section 4 Omitted Proofs"), we can check that this indeed ensures a positive transition probability.
Then 𝐱t+1\mathbf{x}^{t+1} is a feasible state that satisfies both ℙ​(𝐗t+2=𝐱t+2∣𝐗t+1=𝐱t+1)>0\mathbb{P}(\mathbf{X}^{t+2}=\mathbf{x}^{t+2}\mid\mathbf{X}^{t+1}=\mathbf{x}^{t+1})>0 and ℙ​(𝐗t+1=𝐱t+1∣𝐗t=𝐱t)>0\mathbb{P}(\mathbf{X}^{t+1}=\mathbf{x}^{t+1}\mid\mathbf{X}^{t}=\mathbf{x}^{t})>0, and we have described a way to construct 𝐱t+1\mathbf{x}^{t+1} such that
ℙ​(𝐗t+2=𝐱t+2,𝐗t+1=𝐱t+1∣𝐗t=𝐱t)>0.\mathbb{P}(\mathbf{X}^{t+2}=\mathbf{x}^{t+2},\mathbf{X}^{t+1}=\mathbf{x}^{t+1}\mid\mathbf{X}^{t}=\mathbf{x}^{t})>0.
Thus, we have that
ℙ​(𝐗t+2=𝐱t+2∣𝐗t=𝐱t)>0\mathbb{P}(\mathbf{X}^{t+2}=\mathbf{x}^{t+2}\mid\mathbf{X}^{t}=\mathbf{x}^{t})>0
for any two feasible states, i.e. any two states can always reach each other in just two steps with positive probability.

In summary, we have shown that most states can reach each other in one step, as long as states of principals and pure obligees are “consistent” with each other as described by [Equation 20](https://arxiv.org/html/2511.05691v1#S9.E20 "In Proof 9.1 ‣ 9 Section 4 Omitted Proofs").
Then this implies that the zero vector 𝟎\mathbf{0} is a feasible state with a self-loop, and that we can always construct an intermediate state 𝐱t+1\mathbf{x}^{t+1} that allows us to traverse between any two feasible states in two steps.
As a result, the Markov chain is ergodic and aperiodic, and therefore it converges to a unique stationary distribution.

### 9.1 Extension of [Section 4.1](https://arxiv.org/html/2511.05691v1#S4.SS1 "4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process") to Time-Varying Graphs

We next extend the mixing-time result in [Section 4.1](https://arxiv.org/html/2511.05691v1#S4.SS1 "4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process") to contractor networks whose structure evolves over time.
Specifically, we show that our coupling-based contraction argument continues to hold under mild regularity conditions even when the contracting relationships change dynamically.

Formally, consider a sequence of directed graphs (Gt)t≥0{(G\_{t})}\_{t\geq 0}, where each Gt=(𝒱,ℰt)G\_{t}=(\mathcal{V},\mathcal{E}\_{t}) represents the contracting relationships at time tt over a fixed set of nodes 𝒱\mathcal{V}.
The structure and interpretation of the model remain identical to [Section 2](https://arxiv.org/html/2511.05691v1#S2 "2 Network Model Definition"), except that contractual ties (and their associated weights) may now vary across time.
We then consider the same stochastic process as in [Eq. 1](https://arxiv.org/html/2511.05691v1#S2.E1 "In Stochastic Risk Propagation. ‣ 2 Network Model Definition"), but now allowing both the failure propagation probabilities and edge weights to evolve with tt.
Each node ii has a time-varying propagation probability αit∈[0,1]\alpha\_{i}^{t}\in[0,1], and wi​jtw\_{ij}^{t} denotes the fraction of ii’s projects subcontracted to principal jj at time tt.
For each t∈ℕt\in\mathbb{N}, this gives rise to the matrices

|  |  |  |
| --- | --- | --- |
|  | 𝐀t=diag​{αit},𝐖t=(wi​jt)i,j∈𝒱,\mathbf{A}\_{t}=\mathrm{diag}\{\alpha\_{i}^{t}\},\qquad\mathbf{W}\_{t}=(w\_{ij}^{t})\_{i,j\in\mathcal{V}}, |  |

where 𝐖t\mathbf{W}\_{t} is row sub-stochastic by construction.
Accordingly, the time-varying stochastic process evolves as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xit+1∼Bernoulli((1−αit)ri+αit∑j∈δint​(i)wi​jtXjt).X\_{i}^{t+1}\sim\textsf{Bernoulli}\mathopen{}\mathclose{{\left((1-\alpha\_{i}^{t})r\_{i}+\alpha\_{i}^{t}\sum\_{j\in\delta\_{\text{in}}^{t}(i)}w\_{ij}^{t}X\_{j}^{t}}}\right). |  | (21) |

In the static model of [Section 2](https://arxiv.org/html/2511.05691v1#S2 "2 Network Model Definition"), principals satisfy αi<1\alpha\_{i}<1 while pure obligees have αi=1\alpha\_{i}=1.
In the time–varying setting, it is natural to preserve these across nodes at each step: project owners (obligees) do not suddenly begin subcontracting, and principals do not abruptly stop serving as upstream contractors.
Formally, we impose the following role–persistence condition, together with a time–uniform analogue of the static assumption on propagation probabilities.
{assumption}
For every node i∈𝒱i\in\mathcal{V}, if ii is a pure obligee at time tt, it remains a pure obligee at time t+1t+1; likewise, if ii is a principal at time tt, it remains a principal at time t+1t+1.

[Section 9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs") reflects that pure obligees (e.g., municipal agencies or project owners) do not act as subcontractors from one period to the next, while principals continue to perform bonded work and may only evolve in their contractual connections.
Graphically, the assumption ensures that outgoing edges from a pure obligee do not appear between tt and t+1t+1, and that nodes identified as principals retain at least one outgoing edge across time.
Consistent with this interpretation, pure obligees always satisfy αit=1\alpha\_{i}^{t}=1 for all t∈ℕt\in\mathbb{N}.

In addition, we impose a uniform bound on the propagation parameters of all non-obligee nodes.

{assumption}

There exists α¯∈(0,1)\bar{\alpha}\in(0,1) such that, for every t∈ℕt\in\mathbb{N} and every node i∈𝒱i\in\mathcal{V} that is not a pure obligee at time tt, we have αit≤α¯\alpha\_{i}^{t}\leq\bar{\alpha}.

[Section 9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs") generalizes the static assumption that all principals and intermediaries transmit failures with probability strictly less than one.
Intuitively, while the magnitude of αit\alpha\_{i}^{t} may vary over time (e.g., as contracting conditions change), it remains uniformly bounded.
Together, [Sections 9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs") and [9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs") ensure that the network retains its hierarchical structure across time and that the two-step contraction property continues to hold uniformly.

We now extend the mixing-time bound in [Section 4.1](https://arxiv.org/html/2511.05691v1#S4.SS1 "4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process") to the time-varying setting.
In the time-varying regime, the process generally does not admit a stationary distribution, since the transition kernel changes with time. Accordingly, mixing should be interpreted as the rate at which the process forgets its initialization: we bound the total variation distance between any two trajectories started from arbitrary initial conditions.
Under [Sections 9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs") and [9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs"), the same coupling argument used for static graphs continues to ensure uniform geometric convergence, with a rate governed by the two-step contraction factor α¯\bar{\alpha}.
When the graph sequence Gtt≥0{G\_{t}}\_{t\geq 0} is time-homogeneous, this theorem exactly recovers [Section 4.1](https://arxiv.org/html/2511.05691v1#S4.SS1 "4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process"), recovering the unique stationary law of the static process.

{restatable}

theoremMixingGeneralTimeVarying
Let {(𝐀t,𝐖t)}t≥0\{(\mathbf{A}\_{t},\mathbf{W}\_{t})\}\_{t\geq 0} be a sequence of time-varying contractor-network matrices defined as above satisfying [Sections 9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs") and [9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs").

For any two initial states 𝐱,𝐲∈{0,1}n\mathbf{x},\mathbf{y}\in\{0,1\}^{n} let ℙ​(𝐗t∣𝐱)\mathbb{P}(\mathbf{X}^{t}\mid\mathbf{x}) and ℙ​(𝐘t∣y)\mathbb{P}(\mathbf{Y}^{t}\mid y) denote the distribution of two realizations of the stochastic process [Eq. 21](https://arxiv.org/html/2511.05691v1#S9.E21 "In 9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs") started from 𝐗0=𝐱\mathbf{X}^{0}=\mathbf{x} and 𝐘0=𝐲\mathbf{Y}^{0}=\mathbf{y} respectively.
Then for every t∈ℕt\in\mathbb{N},

|  |  |  |  |
| --- | --- | --- | --- |
|  | dT​V​(ℙ​(𝐗t∣𝐱),ℙ​(𝐘t∣𝐲))≤n​‖𝐌t−1​𝐌t−2​⋯​𝐌0‖∞.d\_{TV}\!\bigl(\mathbb{P}(\mathbf{X}^{t}\mid\mathbf{x}),\mathbb{P}(\mathbf{Y}^{t}\mid\mathbf{y})\bigr)\ \leq\ n\,\bigl\|\,\mathbf{M}\_{t-1}\mathbf{M}\_{t-2}\cdots\mathbf{M}\_{0}\,\bigr\|\_{\infty}. |  | (22) |

As a result,

|  |  |  |  |
| --- | --- | --- | --- |
|  | dT​V​(ℙ​(𝐗t∣𝐱),ℙ​(𝐘t∣𝐲))≤n​α¯⌊t/2⌋.d\_{TV}\!\bigl(\mathbb{P}(\mathbf{X}^{t}\mid\mathbf{x}),\mathbb{P}(\mathbf{Y}^{t}\mid\mathbf{y})\bigr)\ \leq n\bar{\alpha}^{\lfloor t/2\rfloor}. |  | (23) |

Before presenting the proof, we start with the following analog of [Fig. 3](https://arxiv.org/html/2511.05691v1#S3.F3 "In 3.1 Expected Failure Probabilities ‣ 3 Mean Field Analysis of Expected Risk") that establishes that under [Sections 9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs") and [9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs"), the fixed graph two–step contraction property continues to hold.

###### Lemma 9.2

Under [Sections 9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs") and [9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs"), we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supt∈ℕ‖𝐀t+1​𝐖t+1​𝐀t​𝐖t‖∞≤α¯< 1.\sup\_{t\in\mathbb{N}}\ \|\,\mathbf{A}\_{t+1}\mathbf{W}\_{t+1}\mathbf{A}\_{t}\mathbf{W}\_{t}\,\|\_{\infty}\;\leq\;\bar{\alpha}\;<\;1. |  | (24) |

###### Proof 9.3

For each tt, the matrix 𝐌t:=𝐀t​𝐖t\mathbf{M}\_{t}:=\mathbf{A}\_{t}\mathbf{W}\_{t} is entry-wise nonnegative and row sub–stochastic, hence ‖𝐌t‖∞≤1\|\mathbf{M}\_{t}\|\_{\infty}\leq 1.
To obtain a strict contraction over two steps, fix t∈ℕt\in\mathbb{N} and a row index ii. The ℓ∞\ell\_{\infty}–induced norm equals the maximum row sum, so we estimate the ii–th row sum of 𝐀t+1​𝐖t+1​𝐀t​𝐖t\mathbf{A}\_{t+1}\mathbf{W}\_{t+1}\mathbf{A}\_{t}\mathbf{W}\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑j(𝐀t+1​𝐖t+1​𝐀t​𝐖t)i​j\displaystyle\sum\_{j}\bigl(\mathbf{A}\_{t+1}\mathbf{W}\_{t+1}\mathbf{A}\_{t}\mathbf{W}\_{t}\bigr)\_{ij} | =∑j∑kαit+1​wi​kt+1​αkt​wk​jt\displaystyle=\sum\_{j}\sum\_{k}\alpha\_{i}^{t+1}w\_{ik}^{t+1}\,\alpha\_{k}^{t}\,w\_{kj}^{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =αit+1​∑kαkt​wi​kt+1​∑jwk​jt⏟≤ 1≤∑kαkt​wi​kt+1,\displaystyle=\alpha\_{i}^{t+1}\sum\_{k}\alpha\_{k}^{t}w\_{ik}^{t+1}\underbrace{\sum\_{j}w\_{kj}^{t}}\_{\leq\,1}\;\leq\;\sum\_{k}\alpha\_{k}^{t}w\_{ik}^{t+1}, |  |

where we used αit+1≤1\alpha\_{i}^{t+1}\leq 1 in the last inequality. Now, if wi​kt+1>0w\_{ik}^{t+1}>0 then node kk has positive outgoing weight at time t+1t{+}1, so it is a principal at t+1t{+}1. By [Section 9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs"), kk is also a principal at time tt and thus not a pure obligee at time tt. Therefore, by [Section 9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs"), αkt≤α¯<1\alpha\_{k}^{t}\leq\bar{\alpha}<1. Hence

|  |  |  |
| --- | --- | --- |
|  | ∑kαkt​wi​kt+1≤α¯​∑kwi​kt+1≤α¯,\sum\_{k}\alpha\_{k}^{t}w\_{ik}^{t+1}\;\leq\;\bar{\alpha}\sum\_{k}w\_{ik}^{t+1}\;\leq\;\bar{\alpha}, |  |

and taking the maximum over ii gives

|  |  |  |
| --- | --- | --- |
|  | ‖𝐀t+1​𝐖t+1​𝐀t​𝐖t‖∞≤α¯< 1.\|\mathbf{A}\_{t+1}\mathbf{W}\_{t+1}\mathbf{A}\_{t}\mathbf{W}\_{t}\|\_{\infty}\;\leq\;\bar{\alpha}\;<\;1. |  |

Finally, taking the supremum over tt, on both sides, proves the claim.

Using this lemma we can show [Section 9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs").

###### Proof 9.4

At a high level, the derivation of [Eq. 22](https://arxiv.org/html/2511.05691v1#S9.E22 "In 9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs") mirrors the static case; we highlight the time-varying modifications and refer to the proof of [Section 4.1](https://arxiv.org/html/2511.05691v1#S4.SS1 "4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process") for omitted steps.
We first construct a *synchronous coupling* of the two trajectories (𝐗t)t∈ℕ(\mathbf{X}^{t})\_{t\in\mathbb{N}} and (𝐘t)t∈ℕ(\mathbf{Y}^{t})\_{t\in\mathbb{N}} starting from 𝐗0=𝐱\mathbf{X}^{0}=\mathbf{x} and 𝐘0=𝐲\mathbf{Y}^{0}=\mathbf{y} respectively, and show that for all t∈ℕt\in\mathbb{N},

|  |  |  |
| --- | --- | --- |
|  | 𝔼[∥𝐗t−𝐘t∥1∣𝐱,𝐲]≤n∥𝐌t−1𝐌t−2⋯𝐌0∥∞,where 𝐌s≔𝐀s𝐖s.\mathbb{E}\mathopen{}\mathclose{{\left[\|\mathbf{X}^{t}-\mathbf{Y}^{t}\|\_{1}\mid\mathbf{x},\mathbf{y}}}\right]\;\leq\;n\,\bigl\|\mathbf{M}\_{t-1}\mathbf{M}\_{t-2}\cdots\mathbf{M}\_{0}\bigr\|\_{\infty},\qquad\text{where }\mathbf{M}\_{s}\coloneqq\mathbf{A}\_{s}\mathbf{W}\_{s}. |  |

By the standard coupling inequality,

|  |  |  |  |
| --- | --- | --- | --- |
|  | dT​V​(ℙ​(𝐗t∣𝐱),ℙ​(𝐘t∣𝐲))\displaystyle d\_{TV}(\mathbb{P}(\mathbf{X}^{t}\mid\mathbf{x}),\mathbb{P}(\mathbf{Y}^{t}\mid\mathbf{y})) | ≤ℙ​(𝐗t≠𝐘t∣𝐱,𝐲)=ℙ​(‖𝐗t−𝐘t‖1≥1∣𝐱,𝐲)\displaystyle\;\leq\;\mathbb{P}(\mathbf{X}^{t}\neq\mathbf{Y}^{t}\mid\mathbf{x},\mathbf{y})\;=\;\mathbb{P}\!\bigl(\|\mathbf{X}^{t}-\mathbf{Y}^{t}\|\_{1}\geq 1\mid\mathbf{x},\mathbf{y}\bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼[∥𝐗t−𝐘t∥1]≤n∥𝐌t−1⋯𝐌0∥∞,\displaystyle\;\leq\;\mathbb{E}\mathopen{}\mathclose{{\left[\|\mathbf{X}^{t}-\mathbf{Y}^{t}\|\_{1}}}\right]\;\leq\;n\,\bigl\|\mathbf{M}\_{t-1}\cdots\mathbf{M}\_{0}\bigr\|\_{\infty}, |  |

as claimed.

We now formalize the coupling step. Write the dynamics as 𝐗t+1=fθt+1​(𝐗t)\mathbf{X}^{t+1}=f\_{\mathbf{\theta}^{t+1}}(\mathbf{X}^{t}) where θt=(θit)i∈[n]\mathbf{\theta}^{t}=(\theta\_{i}^{t})\_{i\in[n]} are independent uniform random variables, exactly as in the proof of [Section 4.1](https://arxiv.org/html/2511.05691v1#S4.SS1 "4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process"). For i=1,…,ni=1,\ldots,n, define

|  |  |  |
| --- | --- | --- |
|  | Dit≜𝔼[|Xit−Yit|],𝐃t≜(D1t,…,Dnt)⊤.D\_{i}^{t}\;\triangleq\;\mathbb{E}\mathopen{}\mathclose{{\left[\mathopen{}\mathclose{{\left\lvert X\_{i}^{t}-Y\_{i}^{t}}}\right\rvert}}\right],\qquad\mathbf{D}^{t}\;\triangleq\;\bigl(D\_{1}^{t},\ldots,D\_{n}^{t}\bigr)^{\top}. |  |

By the same calculation as in [Lemma 4.2](https://arxiv.org/html/2511.05691v1#S4.Thmtheorem2 "Lemma 4.2 ‣ Proof 4.1 ‣ 4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process") (with time index tt carried through), we have for all t≥0t\geq 0,

|  |  |  |
| --- | --- | --- |
|  | 𝐃t+1≤𝐀t​𝐖t​𝐃t=𝐌t​𝐃t.\mathbf{D}^{t+1}\;\leq\;\mathbf{A}\_{t}\mathbf{W}\_{t}\,\mathbf{D}^{t}\;=\;\mathbf{M}\_{t}\,\mathbf{D}^{t}. |  |

Iterating this one-step domination yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | dT​V​(ℙ​(𝐗t∣𝐱),ℙ​(𝐘t∣𝐲))\displaystyle d\_{TV}(\mathbb{P}(\mathbf{X}^{t}\mid\mathbf{x}),\mathbb{P}(\mathbf{Y}^{t}\mid\mathbf{y})) | ≤𝔼[∥𝐗t−𝐘t∥1∣𝐱,𝐲]=∥𝐃t∥1≤(C.S.)n∥𝐃t∥∞\displaystyle\leq\mathbb{E}\mathopen{}\mathclose{{\left[\|\mathbf{X}^{t}-\mathbf{Y}^{t}\|\_{1}\mid\mathbf{x},\mathbf{y}}}\right]=\|\mathbf{D}^{t}\|\_{1}\underset{(\text{C.S.})}{\leq}\;n\,\|\mathbf{D}^{t}\|\_{\infty} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤n​‖𝐌t−1​⋯​𝐌0​𝐃0‖∞≤n​‖𝐌t−1​⋯​𝐌0‖∞​‖𝐃0‖∞≤n​‖𝐌t−1​⋯​𝐌0‖∞,\displaystyle\leq\;n\,\bigl\|\mathbf{M}\_{t-1}\cdots\mathbf{M}\_{0}\,\mathbf{D}^{0}\bigr\|\_{\infty}\;\leq\;n\,\bigl\|\mathbf{M}\_{t-1}\cdots\mathbf{M}\_{0}\bigr\|\_{\infty}\,\|\mathbf{D}^{0}\|\_{\infty}\;\leq\;n\,\bigl\|\mathbf{M}\_{t-1}\cdots\mathbf{M}\_{0}\bigr\|\_{\infty}, |  |

since ‖𝐃0‖∞=∥𝐱−𝐲∥∞≤1\|\mathbf{D}^{0}\|\_{\infty}=\lVert\mathbf{x}-\mathbf{y}\rVert\_{\infty}\leq 1. This is precisely the bound stated in [Eq. 22](https://arxiv.org/html/2511.05691v1#S9.E22 "In 9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs").

Under [Sections 9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs") and [9.1](https://arxiv.org/html/2511.05691v1#S9.SS1 "9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs"), [Lemma 9.2](https://arxiv.org/html/2511.05691v1#S9.Thmtheorem2 "Lemma 9.2 ‣ 9.1 Extension of Section 4.1 to Time-Varying Graphs ‣ 9 Section 4 Omitted Proofs") holds and gives a uniform two–step contraction. Hence, by submultiplicativity we have that for even steps, t=2​mt=2m,

|  |  |  |
| --- | --- | --- |
|  | ‖𝐌t−1​⋯​𝐌0‖∞=‖(𝐌2​m−1​𝐌2​m−2)​⋯​(𝐌1​𝐌0)‖∞≤α¯m,\|\mathbf{M}\_{t-1}\cdots\mathbf{M}\_{0}\|\_{\infty}=\|(\mathbf{M}\_{2m-1}\mathbf{M}\_{2m-2})\cdots(\mathbf{M}\_{1}\mathbf{M}\_{0})\|\_{\infty}\ \leq\ \bar{\alpha}^{\,m}, |  |

and for odd t=2​m+1t=2m{+}1,

|  |  |  |
| --- | --- | --- |
|  | ‖𝐌t−1​⋯​𝐌0‖∞=‖𝐌2​m​(𝐌2​m−1​𝐌2​m−2)​⋯​(𝐌1​𝐌0)‖∞≤‖𝐌2​m‖∞​α¯m≤α¯m.\|\mathbf{M}\_{t-1}\cdots\mathbf{M}\_{0}\|\_{\infty}=\|\mathbf{M}\_{2m}(\mathbf{M}\_{2m-1}\mathbf{M}\_{2m-2})\cdots(\mathbf{M}\_{1}\mathbf{M}\_{0})\|\_{\infty}\ \leq\ \|\mathbf{M}\_{2m}\|\_{\infty}\,\bar{\alpha}^{\,m}\ \leq\ \bar{\alpha}^{\,m}. |  |

Combining both cases gives

|  |  |  |
| --- | --- | --- |
|  | ‖𝐌t−1​⋯​𝐌0‖∞≤α¯⌊t/2⌋.\|\mathbf{M}\_{t-1}\cdots\mathbf{M}\_{0}\|\_{\infty}\leq\bar{\alpha}^{\lfloor t/2\rfloor}. |  |

Plugging this into the bound on dT​V​(ℙ​(𝐗t∣𝐱),ℙ​(𝐘t∣𝐲))d\_{TV}(\mathbb{P}(\mathbf{X}^{t}\mid\mathbf{x}),\mathbb{P}(\mathbf{Y}^{t}\mid\mathbf{y})) yields the second result.

### 9.2 [Section 4.1](https://arxiv.org/html/2511.05691v1#S4.SS1 "4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process") Omitted Proofs

\MixingDAG

\*

###### Proof 9.5

Let 𝐗St≜(Xit)i∈S\mathbf{X}^{t}\_{S}\triangleq(X^{t}\_{i})\_{i\in S} be a random vector containing the entries of 𝐗t\mathbf{X}^{t} corresponding to nodes in S⊂𝒱S\subset\mathcal{V}.
By definition, the transition ℙ​(Xit=Xit∣𝐗t−1=𝐱t−1)\mathbb{P}(X\_{i}^{t}=X\_{i}^{t}\mid\mathbf{X}^{t-1}=\mathbf{x}^{t-1}) depends only on the state of in-neighbors (principals) in the previous step and is fixed for all t>0t>0:

|  |  |  |
| --- | --- | --- |
|  | ℙ​(Xit=1∣𝐗t−1=𝐱t−1)=(1−αi)​ri+αi​∑j∈δin​(i)wi​j​xjt−1=ℙ​(Xit=1∣𝐗δin​(i)t−1=𝐱δin​(i)t−1).\mathbb{P}(X\_{i}^{t}=1\mid\mathbf{X}^{t-1}=\mathbf{x}^{t-1})=(1-\alpha\_{i})r\_{i}+\alpha\_{i}\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}x\_{j}^{t-1}=\mathbb{P}(X\_{i}^{t}=1\mid\mathbf{X}^{t-1}\_{\delta\_{\text{in}}(i)}=\mathbf{x}^{t-1}\_{\delta\_{\text{in}}(i)}). |  |

Then from conditional independence we have that

|  |  |  |
| --- | --- | --- |
|  | ℙ​(𝐗t=𝐱t∣𝐗t−1=𝐱t−1)=∏i∈𝒱ℙ​(Xit=xit∣𝐗δin​(i)t−1=𝐱δin​(i)t−1)=ℙ​(𝐗t=𝐱t∣𝐗Δin1t−1=𝐱Δin1t−1),\mathbb{P}(\mathbf{X}^{t}=\mathbf{x}^{t}\mid\mathbf{X}^{t-1}=\mathbf{x}^{t-1})=\prod\_{i\in\mathcal{V}}\mathbb{P}(X\_{i}^{t}=x\_{i}^{t}\mid\mathbf{X}^{t-1}\_{\delta\_{\text{in}}(i)}=\mathbf{x}^{t-1}\_{\delta\_{\text{in}}(i)})=\mathbb{P}(\mathbf{X}^{t}=\mathbf{x}^{t}\mid\mathbf{X}^{t-1}\_{\Delta\_{\text{in}}^{1}}=\mathbf{x}^{t-1}\_{\Delta\_{\text{in}}^{1}}), |  |

where Δin1\Delta\_{\text{in}}^{1} (see [Definition 4.4](https://arxiv.org/html/2511.05691v1#S4.Thmtheorem4 "Definition 4.4 (In-neighbor layers) ‣ 4.1 Mixing Time of the Stochastic Process ‣ 4 Asymptotic Behavior of Stochastic Risk Process")) denotes the subset of nodes that are in-neighbors (principals) of another node.
In other words, the joint distribution over 𝐗t\mathbf{X}^{t} can be determined without knowing the previous states of nodes not in Δin1\Delta\_{\text{in}}^{1}, i.e., pure obligees.

Similarly, conditional independence implies that the default probabilities of nodes in Δink\Delta\_{\text{in}}^{k} depend only on the previous states of their principals, which are contained in Δink+1\Delta\_{\text{in}}^{k+1}:

|  |  |  |
| --- | --- | --- |
|  | ℙ​(𝐗Δinkt=𝐱Δinkt∣𝐗t−1=𝐱t−1)=∏i∈Δinkℙ​(Xit=xit∣𝐗δin​(i)t−1=𝐱δin​(i)t−1)=ℙ​(𝐗Δinkt=𝐱Δinkt∣𝐗Δink+1t−1=𝐱Δink+1t−1).\mathbb{P}(\mathbf{X}^{t}\_{\Delta\_{\text{in}}^{k}}=\mathbf{x}^{t}\_{\Delta\_{\text{in}}^{k}}\mid\mathbf{X}^{t-1}=\mathbf{x}^{t-1})=\prod\_{i\in\Delta\_{\text{in}}^{k}}\mathbb{P}(X\_{i}^{t}=x\_{i}^{t}\mid\mathbf{X}^{t-1}\_{\delta\_{\text{in}}(i)}=\mathbf{x}^{t-1}\_{\delta\_{\text{in}}(i)})=\mathbb{P}(\mathbf{X}^{t}\_{\Delta\_{\text{in}}^{k}}=\mathbf{x}^{t}\_{\Delta\_{\text{in}}^{k}}\mid\mathbf{X}^{t-1}\_{\Delta\_{\text{in}}^{k+1}}=\mathbf{x}^{t-1}\_{\Delta\_{\text{in}}^{k+1}}). |  |

Then the law of total probability implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(𝐗t=𝐱t∣𝐗t−2=𝐱t−2)\displaystyle\mathbb{P}(\mathbf{X}^{t}=\mathbf{x}^{t}\mid\mathbf{X}^{t-2}=\mathbf{x}^{t-2}) | =∑𝐱Δin1t−1ℙ​(𝐗t=𝐱t∣𝐗Δin1t−1=𝐱Δin1t−1)​ℙ​(𝐗Δin1t−1=𝐱Δin1t−1∣𝐗t−2=𝐱t−2)\displaystyle=\sum\_{\mathbf{x}^{t-1}\_{\Delta\_{\text{in}}^{1}}}\mathbb{P}(\mathbf{X}^{t}=\mathbf{x}^{t}\mid\mathbf{X}^{t-1}\_{\Delta\_{\text{in}}^{1}}=\mathbf{x}^{t-1}\_{\Delta\_{\text{in}}^{1}})\mathbb{P}(\mathbf{X}^{t-1}\_{\Delta\_{\text{in}}^{1}}=\mathbf{x}^{t-1}\_{\Delta\_{\text{in}}^{1}}\mid\mathbf{X}^{t-2}=\mathbf{x}^{t-2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑𝐱Δin1t−1ℙ​(𝐗t=𝐱t∣𝐗Δin1t−1=𝐱Δin1t−1)​ℙ​(𝐗Δin1t−1=𝐱Δin1t−1∣𝐗Δin2t−2=𝐱Δin2t−2)\displaystyle=\sum\_{\mathbf{x}^{t-1}\_{\Delta\_{\text{in}}^{1}}}\mathbb{P}(\mathbf{X}^{t}=\mathbf{x}^{t}\mid\mathbf{X}^{t-1}\_{\Delta\_{\text{in}}^{1}}=\mathbf{x}^{t-1}\_{\Delta\_{\text{in}}^{1}})\mathbb{P}(\mathbf{X}^{t-1}\_{\Delta\_{\text{in}}^{1}}=\mathbf{x}^{t-1}\_{\Delta\_{\text{in}}^{1}}\mid\mathbf{X}^{t-2}\_{\Delta\_{\text{in}}^{2}}=\mathbf{x}^{t-2}\_{\Delta\_{\text{in}}^{2}}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙ​(𝐗t=𝐱t∣𝐗Δin2t−2=𝐱Δin2t−2).\displaystyle=\mathbb{P}(\mathbf{X}^{t}=\mathbf{x}^{t}\mid\mathbf{X}^{t-2}\_{\Delta\_{\text{in}}^{2}}=\mathbf{x}^{t-2}\_{\Delta\_{\text{in}}^{2}}). |  |

Repeating this argument, we eventually get that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(𝐗t=𝐱t∣𝐗t−d=𝐱t−d)\displaystyle\mathbb{P}(\mathbf{X}^{t}=\mathbf{x}^{t}\mid\mathbf{X}^{t-d}=\mathbf{x}^{t-d}) | =∑𝐱Δin1t−1⋯​∑𝐱Δind−1t−d+1ℙ​(𝐗t=𝐱t∣𝐗Δin1t−1=𝐱Δin1t−1)​∏k=1d−1ℙ​(𝐗Δinkt−k=𝐱Δinkt−k∣𝐗Δink+1t−k−1=𝐱Δink+1t−k−1)\displaystyle=\sum\_{\mathbf{x}^{t-1}\_{\Delta\_{\text{in}}^{1}}}\cdots\sum\_{\mathbf{x}^{t-d+1}\_{\Delta\_{\text{in}}^{d-1}}}\mathbb{P}(\mathbf{X}^{t}=\mathbf{x}^{t}\mid\mathbf{X}^{t-1}\_{\Delta\_{\text{in}}^{1}}=\mathbf{x}^{t-1}\_{\Delta\_{\text{in}}^{1}})\prod\_{k=1}^{d-1}\mathbb{P}(\mathbf{X}^{t-k}\_{\Delta\_{\text{in}}^{k}}=\mathbf{x}^{t-k}\_{\Delta\_{\text{in}}^{k}}\mid\mathbf{X}^{t-k-1}\_{\Delta\_{\text{in}}^{k+1}}=\mathbf{x}^{t-k-1}\_{\Delta\_{\text{in}}^{k+1}}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙ​(𝐗t=𝐱t∣𝐗Δindt−d=𝐱Δindt−d),\displaystyle=\mathbb{P}(\mathbf{X}^{t}=\mathbf{x}^{t}\mid\mathbf{X}^{t-d}\_{\Delta\_{\text{in}}^{d}}=\mathbf{x}^{t-d}\_{\Delta\_{\text{in}}^{d}}), |  |

where dd is the longest directed path length. We note that this gives a special case of the Chapman–Kolmogorov equation as derived by Kolmogoroff1931 and chapman1928brownian, which describes a general relation between joint probabilities in stochastic processes.
Note that any dd-length path must start from a pure principal, so Δind\Delta\_{\text{in}}^{d} is contained in the set of pure principals who are unaffected by the network and always fail idiosyncratically according to their inherent risk score in 𝐫\mathbf{r}.
Thus, ℙ​(𝐗Δindt−d=𝐱Δind)=ℙ​(𝐗Δind0=𝐱Δind)\mathbb{P}(\mathbf{X}^{t-d}\_{\Delta\_{\text{in}}^{d}}=\mathbf{x}\_{\Delta\_{\text{in}}^{d}})=\mathbb{P}(\mathbf{X}^{0}\_{\Delta\_{\text{in}}^{d}}=\mathbf{x}\_{\Delta\_{\text{in}}^{d}}) is fixed for all t≥dt\geq d.
Then it follows that for all t≥dt\geq d,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(𝐗t=𝐱t)=∑𝐱Δindℙ​(𝐗t=𝐱t∣𝐗Δindt−d=𝐱Δind)​ℙ​(𝐗Δindt−d=𝐱Δind)=ℙ​(𝐗d=𝐱t)=π​(𝐱t).\mathbb{P}(\mathbf{X}^{t}=\mathbf{x}^{t})=\sum\_{\mathbf{x}\_{\Delta\_{\text{in}}^{d}}}\mathbb{P}(\mathbf{X}^{t}=\mathbf{x}^{t}\mid\mathbf{X}^{t-d}\_{\Delta\_{\text{in}}^{d}}=\mathbf{x}\_{\Delta\_{\text{in}}^{d}})\mathbb{P}(\mathbf{X}^{t-d}\_{\Delta\_{\text{in}}^{d}}=\mathbf{x}\_{\Delta\_{\text{in}}^{d}})=\mathbb{P}(\mathbf{X}^{d}=\mathbf{x}^{t})=\pi(\mathbf{x}^{t}). |  | (25) |

That is, when the contractor network is acyclic and has a maximum depth of dd, the joint distribution converges to its stationary distribution π​(⋅)\pi(\cdot) in at most dd steps.

## 10 Computational Experiments: Additional Details

### 10.1 Construction of Anonymous Network

In our simulations we use real contract and firm data from our partnering surety organization. For privacy reasons, we do not use the original data directly. Instead, we construct a replica network that preserves key structural and distributional properties of the empirical network while protecting sensitive information. [Section 5.1](https://arxiv.org/html/2511.05691v1#S5.SS1 "5.1 Description of Surety Network ‣ 5 Numerical Results") provides a high level description of the surety network, with the network data included in the attached code details.

Our empirical dataset includes all bonded contracts that were active at any time in calendar year 2018 (i.e. with start date before December 31, 2018 and end date after January 1, 2018). The graph GG contains the set of nodes as contracting organizations which had at least one active contract within that time period. Each organization ii has an observed value Revenue​(i)\textsf{Revenue}(i) for their the total contract volume of obligee ii within that year, as observed in the surety’s dataset. Contracts are dictated by a directed edge e=(j,i)e=(j,i) between an obligee ii and principal jj, with a corresponding bond amount BondAmt​(i,j)\textsf{BondAmt}(i,j). Note that in the event that ii and jj have multiple contracts, then BondAmt​(i,j)\textsf{BondAmt}(i,j) corresponds to the cumulative bond amount across all contracts active within that one year period. In order to normalize the scale, we construct the edge weights wi​jw\_{ij} via:

|  |  |  |
| --- | --- | --- |
|  | wi​j=BondAmt​(i,j)Revenue​(i).w\_{ij}=\frac{\textsf{BondAmt}(i,j)}{\textsf{Revenue}(i)}. |  |

Note that in the event ∑j∈δin​(i)BondAmt​(i,j)≠Revenue​(i)\sum\_{j\in\delta\_{\text{in}}(i)}\textsf{BondAmt}(i,j)\neq\textsf{Revenue}(i) then this node has unobserved contracts. We present a methodology to handle this case in [Section 10.2](https://arxiv.org/html/2511.05691v1#S10.SS2 "10.2 Accounting for Unobserved Edges ‣ 10 Computational Experiments: Additional Details"). For each organization in the network, we also have their idionyncratic risk score (default probability) rir\_{i} and loss amount suffered by the surety if it defaults βi\beta\_{i}. To ensure anonymity, node labels are discarded and replaced with indices under a fixed ordering.

Based on these primitives, we generate a noisy observation of this empirical network that conceals sensitive contractor information while retaining essential features: the edge structure, the distributions of βi\beta\_{i}, rir\_{i}, and the relationship between network position and node characteristics based on the framework of differential privacy (dwork2006calibrating). The construction proceeds as follows. Beginning with the set of pure principals (nodes at depth τ=0\tau=0), we rewire edges iteratively across depths:

1. (i)

   Each node at depth τ\tau maintains at least one outgoing edge to a node at depth τ+1\tau+1.
2. (ii)

   Each node at depth τ+1\tau+1 with kk unmatched in-edges is assigned kk incoming edges from nodes at depth τ\tau.
3. (iii)

   Any remaining unmatched out-edges from nodes at depth τ\tau are randomly connected to unmatched in-edges of nodes at later depths.

This process continues until depth d−1d-1. Nodes at depth dd are pure obligees and therefore have no outgoing edges. Conditions (i)–(iii) guarantee that all stubs are matched, degree distributions are preserved, and nodes remain at their original depth, ensuring that principals and obligees retain their types.

To further protect privacy, we apply the Laplace mechanism with scale calibrated to the global sensitivity of each statistic (cf. dwork2006calibrating): each rir\_{i} and βi\beta\_{i} is re-scaled and then perturbed with independent Laplace noise. Finally, we also redefine the edge weights in our replica network. The bond amounts of each contract (edge) in the original network also pass through the same re-scaling and Laplace mechanism as the node features, and each re-scaled amount is associated to the contract obligee. After rewiring, these bond amounts are then arbitrarily reassigned to the rewired in-edges of the obligee and normalized so that the sum of incoming weights to each obligee is one.

This procedure yields a replica network that preserves several important characteristics of the empirical data: the shapes of the distributions of ri,βir\_{i},\beta\_{i} and wi​jw\_{ij}; the way obligees distribute contracts among principals; and the relationship between a node’s position in the network and its features. For example, an obligee that originally allocates most projects to a single principal behaves similarly in the replica, and a high-risk contractor embedded in a long path of intermediaries retains that network role.

### 10.2 Accounting for Unobserved Edges

In practice, an obligee’s reported revenue Revenue​(i)\textsf{Revenue}(i) may exceed the value of contracts bonded by the surety, since competing surety organizations may also underwrite a portion of their contracting principal’s work. In this case, we observe that Revenue​(i)>∑j∈δin​(i)BondAmt​(i,j)\textsf{Revenue}(i)>\sum\_{j\in\delta\_{\text{in}}(i)}\textsf{BondAmt}(i,j) and the proposed methodology will result in a node whose weighted in-degree (∑j∈δin​iwi​j\sum\_{j\in\delta\_{\text{in}}{i}}w\_{ij}) is strictly less than one. To account for such unobserved contracts (aka unobserved edges) we present a methodology to impute the graph under reasonable assumption on each obligees contracting behavior.

For each obligee ii such that Revenue​(i)>∑j∈δin​(i)BondAmt​(i,j)\textsf{Revenue}(i)>\sum\_{j\in\delta\_{\text{in}}(i)}\textsf{BondAmt}(i,j), we define a dummy principal with baseline risk rioutr\_{i}^{\textsf{out}} and a single outgoing edge weighted as:

|  |  |  |
| --- | --- | --- |
|  | wi,out=1−∑k∈δin​(i)wi​kw\_{i,\text{out}}=1-\sum\_{k\in\delta\_{\text{in}}(i)}w\_{ik} |  |

to represent all unobserved principals. Note that by using this dummy variable we rely on the implicit assumption that the subcontractors of ii and kk do not contract with each other, so that rioutr\_{i}^{\textsf{out}} and rkoutr\_{k}^{\textsf{out}} can be expressed as independent risk scores.
In order to estimate rioutr\_{i}^{\textsf{out}} we make the following assumption.

{assumption}

Suppose each contractor jj is assigned one of TT product segment types Type​(j)∈{τ1,…,τT}\textsf{Type}(j)\in\{\tau\_{1},\dots,\tau\_{T}\}.
Furthermore, let δin​(i)\delta\_{\text{in}}(i) denote the set of all of ii’s contractors, including unobserved contractors.
We assume that for any type τk\tau\_{k},

|  |  |  |
| --- | --- | --- |
|  | ∑{j∈δin​(i):Type​(j)=τk}wi​j∑{j∈δin​(i)}wi​j=∑{j∈𝒱∖δin​(i):Type​(j)=τk}wi​j∑{j∈𝒱∖δin​(i)}wi​j.\frac{\sum\_{\{j\in\delta\_{\text{in}}(i)\,:\,\textsf{Type}(j)=\tau\_{k}\}}w\_{ij}}{\sum\_{\{j\in\delta\_{\text{in}}(i)\}}w\_{ij}}=\frac{\sum\_{\{j\in\mathcal{V}\setminus\delta\_{\text{in}}(i)\,:\,\textsf{Type}(j)=\tau\_{k}\}}w\_{ij}}{\sum\_{\{j\in\mathcal{V}\setminus\delta\_{\text{in}}(i)\}}w\_{ij}}. |  |

In other words, the fraction of ii’s obligations to subcontractors jj of type τk\tau\_{k} in the unobserved network is the same as the fraction in our observed network.
Given this assumption, we define rioutr\_{i}^{\textsf{out}} to be a convex combination of the median baseline risk scores r¯j\bar{r}\_{j} associated with each product segment type, weighted by how often obligee ii works with contractors of the same type in our observed network. In particular, we set:

|  |  |  |
| --- | --- | --- |
|  | riout=∑j∈δin​(i)wi​j∑j∈δin​(i)wi​j​r¯j.r\_{i}^{\textsf{out}}=\sum\_{j\in\delta\_{\text{in}}(i)}\frac{w\_{ij}}{\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}}\bar{r}\_{j}. |  |

### 10.3 Real-World Network Satisfying [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk")

In [Section 3](https://arxiv.org/html/2511.05691v1#S3 "3 Mean Field Analysis of Expected Risk"), we established that under [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk"), that is, when each intermediary ii satisfies ∑j∈δin​(i)wi​j​rj≥ri\sum\_{j\in\delta\_{\text{in}}(i)}w\_{ij}r\_{j}\geq r\_{i}, the limiting failure probabilities mim\_{i} are guaranteed to exceed their idiosyncratic risk levels rir\_{i}. While this condition is sufficient to ensure higher expected losses, it is not necessary. In practice, we observe that the condition holds for many but not all intermediaries, yet the expected aggregate loss 𝔼[ℒ(𝐗∞)]\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{\infty})}}\right] is still larger than 𝔼[ℒ(𝐗0)]\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{0})}}\right]. Indeed, as showin in [Figure 12(a)](https://arxiv.org/html/2511.05691v1#S10.F12.sf1 "In Figure 12 ‣ 10.3 Real-World Network Satisfying Section 3.3 ‣ 10 Computational Experiments: Additional Details"), a number of intermediaries in our empirical network violate the assumption, but the net effect of those satisfying the inequality dominates, producing greeater expected losses and amplified tail risk.

![Refer to caption](x12.png)


(a) rir\_{i} vs ∑jwi​j​rj\sum\_{j}w\_{ij}r\_{j}

![Refer to caption](x13.png)


(b) mi−rim\_{i}-r\_{i}

Figure 12: (Left) The idiosyncratic default probabilities rir\_{i} for intermediaries ii as compared to the weighted average of their principals’ idiosyncratic default probabilities. Several points fall below the dashed y=xy=x line, indicating that for these intermediaries, [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk") is not satisfied. Note that plot is shown on a logarithmic scale. (Right) Values mi−ri=[(𝐈−𝐀𝐖)−1​𝐀​(𝐖−𝐈)​𝐫]im\_{i}-r\_{i}=[(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\mathbf{A}(\mathbf{W}-\mathbf{I})\mathbf{r}]\_{i} for intermediaries ii, sorted in ascending order. Most points lie above the xx-axis, indicating that the limiting failure probabilities of these intermediaries satisfy mi>rim\_{i}>r\_{i}.

To further formalize this observation, we derive an alternative sufficient condition for mi≥rim\_{i}\geq r\_{i}. Starting from the closed-form expression

|  |  |  |
| --- | --- | --- |
|  | 𝐦=(𝐈−𝐀𝐖)−1​(𝐈−𝐀)​𝐫,\mathbf{m}=(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}(\mathbf{I}-\mathbf{A})\mathbf{r}, |  |

we compute

|  |  |  |
| --- | --- | --- |
|  | 𝐦−𝐫=(𝐈−𝐀𝐖)−1​𝐀​(𝐖−𝐈)​𝐫.\mathbf{m}-\mathbf{r}=(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\mathbf{A}(\mathbf{W}-\mathbf{I})\mathbf{r}. |  |

Thus, for each intermediary ii, we have mi≥rim\_{i}\geq r\_{i} if and only if

|  |  |  |
| --- | --- | --- |
|  | [(𝐈−𝐀𝐖)−1​𝐀​(𝐖−𝐈)​𝐫]i≥0.\bigl[(\mathbf{I}-\mathbf{A}\mathbf{W})^{-1}\mathbf{A}(\mathbf{W}-\mathbf{I})\mathbf{r}\bigr]\_{i}\geq 0. |  |

Empirically, this condition is satisfied for the majority of intermediaries in our dataset (see [Figure 12(b)](https://arxiv.org/html/2511.05691v1#S10.F12.sf2 "In Figure 12 ‣ 10.3 Real-World Network Satisfying Section 3.3 ‣ 10 Computational Experiments: Additional Details")), meaning that their network-adjusted failure probabilities exceed their idiosyncratic risks.

Taken together, these results show that although [Section 3.3](https://arxiv.org/html/2511.05691v1#S3.SS3 "3.3 Impact of Risk Propagation on Mean Field ‣ 3 Mean Field Analysis of Expected Risk") does not universally hold, a sufficient mass of intermediaries nonetheless experience risk amplification (mi≥rim\_{i}\geq r\_{i}). Consequently, as summarized in [Figure 10](https://arxiv.org/html/2511.05691v1#S5.F10 "In 5.3 Impact of network effects on global financial loss ‣ 5 Numerical Results"), the expected aggregate loss 𝔼[ℒ(𝐗∞)]\mathbb{E}\mathopen{}\mathclose{{\left[\mathcal{L}(\mathbf{X}^{\infty})}}\right] strictly exceeds its independent-failure counterpart, consistent with the heavier right tails observed in the empirical loss distribution.

## 11 Useful definitions and results

For completeness we state a couple results from muller2002comparison that are used here for the proof of [Section 4.2](https://arxiv.org/html/2511.05691v1#S4.SS2 "4.2 Impact on Global Average Risk ‣ 4 Asymptotic Behavior of Stochastic Risk Process").

###### Theorem 11.1 ((muller2002comparison, Theorem 3.3.8))

Let 𝐗=(X1,X2,…,Xn)\mathbf{X}=(X\_{1},X\_{2},\ldots,X\_{n}) and 𝐘=(Y1,Y2,…,Yn)\mathbf{Y}=(Y\_{1},Y\_{2},\ldots,Y\_{n}) have a common copula. If Xi⪯stYiX\_{i}\preceq\_{\text{st}}Y\_{i} for all i=1,2,…,ni=1,2,\ldots,n, then 𝐗⪯st𝐘\mathbf{X}\preceq\_{\text{st}}\mathbf{Y}.

###### Theorem 11.2 ((muller2002comparison, Theorem 3.3.11))

If 𝐗⪯st𝐘\mathbf{X}\preceq\_{\text{st}}\mathbf{Y} and g:ℝn→ℝkg:\mathbb{R}^{n}\to\mathbb{R}^{k} is increasing, then g​(𝐗)⪯stg​(𝐘)g(\mathbf{X})\preceq\_{\text{st}}g(\mathbf{Y}).