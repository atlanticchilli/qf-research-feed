---
authors:
- Luca Lazzaro
- Manuel S. Mariani
- René Algesheimer
- Radu Tanase
doc_id: arxiv:2510.04785v1
family_id: arxiv:2510.04785
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A behavioral reinvestigation of the effect of long ties on social contagions
url_abs: http://arxiv.org/abs/2510.04785v1
url_html: https://arxiv.org/html/2510.04785v1
venue: arXiv q-fin
version: 1
year: 2025
---


Luca Lazzaro∗
Department of Business Administration, University of Zurich, Zurich, Switzerland
University Research Priority Program on Social Networks, University of Zurich, 8032 Zurich, Switzerland
  
Manuel S. Mariani
Department of Business Administration, University of Zurich, Zurich, Switzerland
University Research Priority Program on Social Networks, University of Zurich, 8032 Zurich, Switzerland
  
René Algesheimer
Department of Business Administration, University of Zurich, Zurich, Switzerland
University Research Priority Program on Social Networks, University of Zurich, 8032 Zurich, Switzerland
  
Radu Tanase∗
Department of Business Administration, University of Zurich, Zurich, Switzerland
University Research Priority Program on Social Networks, University of Zurich, 8032 Zurich, Switzerland

###### Abstract

Faced with uncertainty in decision making, individuals often turn to their social networks to inform their decisions. In consequence, these networks become central to how new products and behaviors spread. A key structural feature of networks is the presence of long ties, which connect individuals who share few mutual contacts. Under what conditions do long ties facilitate or hinder diffusion? The literature provides conflicting results, largely due to differing assumptions about individual decision-making. We reinvestigate the role of long ties by experimentally measuring adoption decisions under social influence for products with uncertain payoffs and embedding these decisions in network simulations. At the individual level, we find that higher payoff uncertainty increases the average reliance on social influence. However, personal traits such as risk preferences and attitudes toward uncertainty lead to substantial heterogeneity in how individuals respond to social influence. At the collective level, the observed individual heterogeneity ensures that long ties consistently promote diffusion, but their positive effect weakens as uncertainty increases. Our results reveal that the effect of long ties is not determined by whether the aggregate process is a simple or complex contagion, but by the extent of heterogeneity in how individuals respond to social influence.

\*To whom correspondance should be addressed.
Email: <luca.lazzaro@uzh.ch> or <radu.tanase@uzh.ch>

Uncertainty permeates everyday decisions. To navigate an uncertain world, individuals rely on what others think, do, and approve [[1](https://arxiv.org/html/2510.04785v1#bib.bib1), [2](https://arxiv.org/html/2510.04785v1#bib.bib2), [3](https://arxiv.org/html/2510.04785v1#bib.bib3), [4](https://arxiv.org/html/2510.04785v1#bib.bib4)]. Think of a farmer deciding whether to adopt a new agricultural practice. Faced with uncertain payoffs, they may rely on their neighbors’ decisions and experiences with the new practice to inform their own decision [[5](https://arxiv.org/html/2510.04785v1#bib.bib5), [6](https://arxiv.org/html/2510.04785v1#bib.bib6)]. In light of these social influences, the spread of products and behaviors is often characterized as a diffusion process within a relevant social network [[7](https://arxiv.org/html/2510.04785v1#bib.bib7), [8](https://arxiv.org/html/2510.04785v1#bib.bib8), [9](https://arxiv.org/html/2510.04785v1#bib.bib9), [10](https://arxiv.org/html/2510.04785v1#bib.bib10)]. This raises the question of how network structures may facilitate the diffusion of new products and behaviors. Answering this question has broad practical implications for decision-makers, such as governments or organizations, who intend to intervene in a population either by seeding information, products, and behaviors, or by modifying network connections through rewiring interventions [[11](https://arxiv.org/html/2510.04785v1#bib.bib11)].

One of the key features of a network is the presence of long ties—connections between individuals with few or no mutual contacts. How long ties affect the spread of products and behaviors remains highly debated. Prior research provides conflicting evidence. Some work suggests that long ties accelerate diffusion by bridging distant clusters [[12](https://arxiv.org/html/2510.04785v1#bib.bib12), [13](https://arxiv.org/html/2510.04785v1#bib.bib13), [14](https://arxiv.org/html/2510.04785v1#bib.bib14), [15](https://arxiv.org/html/2510.04785v1#bib.bib15), [16](https://arxiv.org/html/2510.04785v1#bib.bib16), [17](https://arxiv.org/html/2510.04785v1#bib.bib17), [18](https://arxiv.org/html/2510.04785v1#bib.bib18), [19](https://arxiv.org/html/2510.04785v1#bib.bib19), [20](https://arxiv.org/html/2510.04785v1#bib.bib20), [21](https://arxiv.org/html/2510.04785v1#bib.bib21), [22](https://arxiv.org/html/2510.04785v1#bib.bib22)], whereas other work highlights that long ties can impede the spread by weakening the local social reinforcement individuals need to adopt a behavior [[23](https://arxiv.org/html/2510.04785v1#bib.bib23), [24](https://arxiv.org/html/2510.04785v1#bib.bib24), [25](https://arxiv.org/html/2510.04785v1#bib.bib25), [26](https://arxiv.org/html/2510.04785v1#bib.bib26), [27](https://arxiv.org/html/2510.04785v1#bib.bib27), [28](https://arxiv.org/html/2510.04785v1#bib.bib28)].

These conflicting findings can be understood through the theoretical distinction between simple and complex contagion. Simple contagion models adoption analogous to a biological infection in which each contact with an adopter independently increases one’s adoption probability [[29](https://arxiv.org/html/2510.04785v1#bib.bib29)]. Here, long ties, by creating distant exposures, accelerate diffusion. In contrast, complex contagion posits that individuals require social reinforcement: they adopt only after a threshold (or fraction) of their peers have already adopted. Here, long ties, which dilute local clusters, hinder spread [[23](https://arxiv.org/html/2510.04785v1#bib.bib23), [26](https://arxiv.org/html/2510.04785v1#bib.bib26)]. Recent studies integrate both social contagion mechanisms into a single model—informing on boundary conditions on the effect of long ties [[30](https://arxiv.org/html/2510.04785v1#bib.bib30), [31](https://arxiv.org/html/2510.04785v1#bib.bib31), [32](https://arxiv.org/html/2510.04785v1#bib.bib32)].

However, these theoretical models rest on untested assumptions about how individuals respond to social influence. Simple contagion reduces adoption to independent “infections” overlooking the social reinforcement individuals typically require in making decisions under uncertainty [[23](https://arxiv.org/html/2510.04785v1#bib.bib23)]. Complex contagion introduces social reinforcement but ignores below-threshold adoption [[30](https://arxiv.org/html/2510.04785v1#bib.bib30)]. Even recent models that integrate simple and complex contagion mechanisms [[30](https://arxiv.org/html/2510.04785v1#bib.bib30), [31](https://arxiv.org/html/2510.04785v1#bib.bib31), [32](https://arxiv.org/html/2510.04785v1#bib.bib32)] rely on behavioral assumptions, leaving the debate purely theoretical. The basic conclusion from this literature is that the role of long ties in social contagions is dictated by the behavioral assumptions embedded in the computational model. This conclusion is largely due to the divide between behavioral research, which studies individual decision-making processes, and computational research, which models collective dynamics [[33](https://arxiv.org/html/2510.04785v1#bib.bib33)]. Scholars across disciplines have called for integrating these perspectives to ground computational models in behavioral data [[34](https://arxiv.org/html/2510.04785v1#bib.bib34), [35](https://arxiv.org/html/2510.04785v1#bib.bib35), [36](https://arxiv.org/html/2510.04785v1#bib.bib36), [37](https://arxiv.org/html/2510.04785v1#bib.bib37)].

We translate the question of how long ties affect social contagions from a theoretical to an empirical inquiry. Our work offers an empirical microfoundation for social contagion models, bridging the gap between behavioral experiments and network simulations. In an experiment, we elicit individuals’ choice function—the mapping from the number of adopting peers to the subject’s own adoption decision—for several products with uncertain payoffs. Then, to assess the effect of long ties, we embed the empirically derived choice functions into agent-based simulations, and examine how long ties and payoff uncertainty jointly shape product diffusion.

At the individual level, we find that, on average, higher payoff uncertainty increases the proportion of individuals susceptible to social influence and their need for social reinforcement. However, we document substantial heterogeneity in individuals’ choice functions; some individuals are willing to adopt the product with minimal social influence, while others require substantial social reinforcement. Average choice functions are driven by product characteristics (such as risk and uncertainty), whereas choice function heterogeneity within the same product is driven by personal characteristics (such as risk preferences and the subjective interpretation of uncertainty). At the collective level, we find that long ties consistently promote diffusion across all product configurations, but their positive effect weakens with increasing uncertainty until it disappears under full uncertainty.

In sum, our behavioral reinvestigation of the role of long ties in social contagions highlights that the microfoundations of social influence are not fixed at the population level—as assumed by the simple vs. complex contagion dichotomy. Instead, they emerge from individual-level traits, such as preferences. As a consequence, in heterogeneous populations where simple and complex choice functions coexist, products and behaviors spread through a mixture of contagion types, making long ties consistently beneficial. When the population consists of only individuals with complex adoption patterns, long ties hinder the diffusion. Our work highlights the importance of considering heterogeneity in both research and practice.

![Refer to caption](framework.png)


Fig. 1: Connecting behavioral experiments and computational simulations (A) In the experiment, subjects decided whether to adopt risky products with uncertain payoffs. Subjects provided a separate adoption decision for each possible peer-adoption level (0–4 adopting peers, presented in a pre-specified order). This procedure yields each subject’s complete choice function. (B) The measured choice functions serve as decision rules for nodes in network simulations. Subjects are randomly assigned to nodes, and diffusion begins by selecting a pair of connected nodes (seeds) and setting their state to adopted. At each time step, nodes with at least one adopted neighbor simultaneously update their state by evaluating their experimentally measured choice function at the current peer-adoption level. Panel B illustrates a focal node evaluating the choice function elicited in Panel A. In this example, the subject assigned to the focal node is connected to four neighbors, two adopters (the seeds) and two non-adopters. Following the measured choice function the focal node will adopt the product.

## Experimental design

We followed a two-step approach. First, we conducted an experiment to elicit each individual’s choice function across products that varied in risk and payoff uncertainty. Second, we used these empirically derived choice functions as decision rules in simulations of product diffusion on synthetic networks.

We modeled products as lotteries and visualized them as an urn containing 40 balls (Fig. [1](https://arxiv.org/html/2510.04785v1#S0.F1 "Fig. 1 ‣ A behavioral reinvestigation of the effect of long ties on social contagions")A). Lotteries provide a well-established paradigm to study decision making under risk and uncertainty [[38](https://arxiv.org/html/2510.04785v1#bib.bib38)], offering both precise manipulation of risk and uncertainty and a simple incentive-aligned experimental task that generalizes to real-world decisions. Adopting the product corresponded to drawing a ball at random from the urn, yielding either a payoff of 300 points (blue ball) or 0 points (orange ball). Choosing not to adopt provided a guaranteed payoff of 100 points. We manipulated two features of the product: (i) uncertainty, by varying how much of the payoff probability was known, and (ii) risk, by altering the known probability of winning 300 points. To operationalize uncertainty, we hid the colors of a fraction of the balls, presenting them as gray. We varied the proportion of gray balls at four levels: 0%0\% (no uncertainty), 25%25\% (low uncertainty), 50%50\% (high uncertainty), and 100%100\% (full uncertainty). Risk was manipulated by adjusting the probability of winning, i.e. the ratio of blue to orange balls in the visible portion of the urn, creating two levels: 90%90\% probability of winning (low risk) and 50%50\% probability of winning (high risk). See Methods Fig. [4](https://arxiv.org/html/2510.04785v1#Sx4.F4 "Fig. 4 ‣ Material and Methods ‣ A behavioral reinvestigation of the effect of long ties on social contagions") for full details and visualizations of all risk and uncertainty product configurations.

To measure adoption decisions under social influence, we used a modification of the “strategy method” [[39](https://arxiv.org/html/2510.04785v1#bib.bib39)]. In each adoption task, subjects were presented with a product. Rather than providing a single “unconditional” choice, subjects indicated for each possible number of peers (0–4) observed adopting the product whether they themselves would adopt (Fig. [1](https://arxiv.org/html/2510.04785v1#S0.F1 "Fig. 1 ‣ A behavioral reinvestigation of the effect of long ties on social contagions")A). Crucially, subjects knew that their peers might possess different amounts of information about the product’s winning probability. This elicitation yielded a choice function (i.e. a complete contingency plan) mapping peer-adoption levels to individual adoption decisions.

This 44 (uncertainty) × 22 (risk) within-subject design yielded seven unique tasks (since under full uncertainty, all known probabilities were hidden, eliminating risk differences). Subjects (N=399N=399) completed the seven tasks in a randomized order. All decisions were incentivized (see Methods for details). Beyond the adoption tasks, we measured risk preferences using the multiple price list method [[40](https://arxiv.org/html/2510.04785v1#bib.bib40)] and asked subjects to estimate the probability of success for products with uncertain payoff to measure subjective interpretation of uncertainty (see estimation task in Methods).

To translate subjects’ decisions into diffusion dynamics, we implemented an agent-based model in which subjects’ experimentally measured choice functions served as decision rules (Fig. [1](https://arxiv.org/html/2510.04785v1#S0.F1 "Fig. 1 ‣ A behavioral reinvestigation of the effect of long ties on social contagions")B). We generated ring lattice networks (fixed degree k=4k=4, size N=399N=399) and systematically introduced long ties by rewiring edges using a degree-preserving algorithm [[41](https://arxiv.org/html/2510.04785v1#bib.bib41)] (Fig. [3](https://arxiv.org/html/2510.04785v1#Sx2.F3 "Fig. 3 ‣ Implication for the role of long ties in social contagions ‣ Results ‣ A behavioral reinvestigation of the effect of long ties on social contagions")A). Subjects were randomly assigned to nodes in the network. We started the diffusion by seeding adoption in a randomly selected pair of connected nodes to ensure initial local social reinforcement. Diffusion proceeded in synchronous time steps: at each step, every non-adopter with at least one adopting neighbor evaluated their choice function based on current peer adoption level and updated simultaneously. To account for variability in the rewiring algorithm, subject-to-node placement, and initial seed choice, we conducted 500500 diffusion runs for each product and rewiring level.

## Results

We organize our findings into two parts. First, we report individual‐level results on how uncertainty affects individuals response to social influence. Second, we report the collective‐dynamics of social influence and the consequences for the role of long ties. In the main text, we report results for products in the low‐risk condition across all uncertainty levels. Results of the high-risk products are qualitatively similar and are reported in the SI Appendix (Fig. S6-9).

### Measuring the microfuncation of social influence

The choice function.
We define a *choice function* as the mapping from peer adoption levels to an individual’s probability of adoption. Formally, for subject ii with kk peers, the choice function is

|  |  |  |
| --- | --- | --- |
|  | fi:{0,1,…,k}→[0,1],n↦fi​(n)=Pr⁡(adopti∣n),f\_{i}:\{0,1,\dots,k\}\to[0,1],\quad n\mapsto f\_{i}(n)=\Pr(\text{adopt}\_{i}\mid n), |  |

where fi​(n)f\_{i}(n) denotes the probability that subject ii adopts when nn peers are observed adopting. This general formulation encompasses canonical contagion models: in simple contagion, each adopting peer independently increases adoption probability by pp, yielding a smooth increase such as fi​(n)=1−(1−p)nf\_{i}(n)=1-(1-p)^{n} [[29](https://arxiv.org/html/2510.04785v1#bib.bib29)]; in complex contagion, adoption is deterministic and requires reinforcement from multiple peers, corresponding to a step function with a threshold θi≥2\theta\_{i}\geq 2 such that fi​(n)=0f\_{i}(n)=0 for n<θin<\theta\_{i} and fi​(n)=1f\_{i}(n)=1 for n≥θin\geq\theta\_{i} [[23](https://arxiv.org/html/2510.04785v1#bib.bib23)]. In our experiment, subjects indicated for each possible number of adopting peers (0–44) whether they would adopt. This procedure yielded binary responses fi​(n)∈{0,1}f\_{i}(n)\in\{0,1\}, which we interpret as realizations of the underlying choice function. For convenience, we refer to these elicited contingency plans as “choice functions” throughout, acknowledging that they represent observed outputs of the latent choice function.

Across all conditions, roughly 90%90\% of individual choice functions were well described by a threshold, meaning adoption increased monotonically with the number of adopting peers (Fig. [2](https://arxiv.org/html/2510.04785v1#Sx2.F2 "Fig. 2 ‣ Measuring the microfuncation of social influence ‣ Results ‣ A behavioral reinvestigation of the effect of long ties on social contagions")D). Based on their thresholds, we classified subjects as unconditional adopters (0/40/4), unconditional non-adopters (>1>1), or conditional adopters (1/41/4 to 4/44/4). The latter group, whose adoption depended on peer behavior, captures individuals who are susceptible to social influence. A minority of subjects (roughly 10%10\%) displayed non-monotonic choice functions.

![Refer to caption](micro.png)


Fig. 2:  Individual-level results
(A) Fraction of individuals susceptible to social influence in the different uncertainty conditions (N=399N=399). Error bars are the 95%95\% confidence intervals.
(B) Average social reinforcement required to adopt in the different uncertainty conditions (computed from adopting individuals in the different uncertainty conditions, Nno=365,Nlow=351,Nhigh=329,Nfull=253N\_{\text{no}}=365,\;N\_{\text{low}}=351,\;N\_{\text{high}}=329,\;N\_{\text{full}}=253). Error bars are the 95%95\% confidence intervals.
(C) Fraction of individuals exhibiting simple and complex adoptions pattens in their choice functions for the different uncertainty condition (computed from adopting individuals, Nno=365,Nlow=351,Nhigh=329,Nfull=253N\_{\text{no}}=365,\;N\_{\text{low}}=351,\;N\_{\text{high}}=329,\;N\_{\text{full}}=253. Error bars are the 95%95\% confidence intervals.
(D) Distribution of thresholds (choice functions patterns) for each uncertainty condition. Threshold values indicate the fraction of adopting peers required for adoption, >1>1 indicates no adoption, NM indicates non-monotonic threshold (N=399N=399).

The effect of uncertainty on aggregate choice functions.
Uncertainty had two distinct effects on aggregate choice functions. First, the fraction of susceptible individuals increased from no to high uncertainty, but plateaued under full uncertainty (Fig. [2](https://arxiv.org/html/2510.04785v1#Sx2.F2 "Fig. 2 ‣ Measuring the microfuncation of social influence ‣ Results ‣ A behavioral reinvestigation of the effect of long ties on social contagions")A), as many subjects shifted to unconditional non-adoption. Second, social reinforcement—the fraction of adopting peers required to trigger adoption—increased with uncertainty (Fig. [2](https://arxiv.org/html/2510.04785v1#Sx2.F2 "Fig. 2 ‣ Measuring the microfuncation of social influence ‣ Results ‣ A behavioral reinvestigation of the effect of long ties on social contagions")B). Under no uncertainty, individuals required on average 7.5%7.5\% of their peers to adopt, whereas under full uncertainty they required 62.9%62.9\% (Fig. [2](https://arxiv.org/html/2510.04785v1#Sx2.F2 "Fig. 2 ‣ Measuring the microfuncation of social influence ‣ Results ‣ A behavioral reinvestigation of the effect of long ties on social contagions")B). In summary, uncertainty increases both the fraction of individuals who are susceptible to social influence and the level of social reinforcement required for adoption.

Table 1: Two stage mixed-effects models predicting adoption (Stage 1) and adoption thresholds among adopters (Stage 2). Predictors are z-scored. Odds ratios (OR) with 95% CI are reported. Intercepts, ordinal cut-points, and additional model statistics are included in the SI Appendix Table S1.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Stage 1: Adoption (logit) | | | Stage 2: Threshold (ordinal logit) | | |
| Predictor | OR | 95% CI | p-value | OR | 95% CI | p-value |
| Uncertainty | 0.02 | [0.01, 0.05] | <<0.001 | 8.41 | [6.75, 10.48] | <<0.001 |
| Risk aversion | 0.64 | [0.29, 1.39] | 0.262 | 1.31 | [1.02, 1.68] | 0.033 |
| Estimated prob. success | 1.50 | [0.72, 3.13] | 0.283 | 0.64 | [0.50, 0.82] | 0.001 |
| Age | 0.60 | [0.28, 1.29] | 0.194 | 1.17 | [0.91, 1.50] | 0.229 |
| Education | 0.94 | [0.46, 1.94] | 0.867 | 1.31 | [1.02, 1.67] | 0.034 |
| Gender (male) | 0.85 | [0.20, 3.65] | 0.826 | 0.54 | [0.33, 0.88] | 0.014 |
| Random effects | | | | | | |
| Residual variance (σ2\sigma^{2}) | 3.29 |  |  | 3.29 |  |  |
| Intercept variance (τ00\tau\_{00}) | 111.95 |  |  | 3.28 |  |  |
| N subjects | 326 |  |  | 320 |  |  |
| Model statistics | | | | | | |
| Observations | 1304 |  |  | 1150 |  |  |
| Marginal R2R^{2} | 0.123 |  |  | 0.405 |  |  |
| Conditional R2R^{2} | 0.975 |  |  | 0.702 |  |  |

Documenting and explaining heterogeneity in choice functions.
Having established how uncertainty shapes aggregate choice functions, we now turn to individual-level heterogeneity. Fig. [2](https://arxiv.org/html/2510.04785v1#Sx2.F2 "Fig. 2 ‣ Measuring the microfuncation of social influence ‣ Results ‣ A behavioral reinvestigation of the effect of long ties on social contagions")D highlights high heterogeneity in the choice function across all products. While some subjects adopted the product without any adopting peer (threshold of 0/40/4), others required all four peers (threshold of 4/44/4) or never adopted (threshold >1>1). To quantify the extent of this heterogeneity, we classified choice functions into simple and complex. Drawing from the literature of simple and complex contagion, we define choice functions dictating adoption upon a single exposure (threshold of 0/40/4 and 1/41/4) as simple, whereas choice functions requiring social reinforcement (threshold of 2/42/4, 3/43/4, 4/44/4) as complex. Fig. [2](https://arxiv.org/html/2510.04785v1#Sx2.F2 "Fig. 2 ‣ Measuring the microfuncation of social influence ‣ Results ‣ A behavioral reinvestigation of the effect of long ties on social contagions")C shows that the prevalence of simple choice functions decreases with uncertainty, while the prevalence of complex choice functions increases. Nevertheless, both simple and complex choice functions were present for all product configurations.

Next, we study the source of individual heterogeneity in choice function. Because some subjects never adopted while others did so at varying thresholds, we used a two-stage mixed-effects model (Tab. [1](https://arxiv.org/html/2510.04785v1#Sx2.T1 "Table 1 ‣ Measuring the microfuncation of social influence ‣ Results ‣ A behavioral reinvestigation of the effect of long ties on social contagions")). The first stage estimated the probability of adoption using a binomial logistic regression with participant random intercepts. The second stage estimated adoption thresholds conditional on adoption using a cumulative logit mixed model for the ordered categories (0, 1/41/4, 2/42/4, 3/43/4, 4/44/4), again with participant random intercepts. In the adoption stage (Stage 1), the baseline probability of adoption was very high (p≈0.99p\approx 0.99), with adoption less likely under higher uncertainty (OR = 0.02, 95% CI [0.01, 0.05], p<0.001p<0.001). In the threshold stage (Stage 2), uncertainty had a strong positive effect on thresholds (OR = 8.41, 95% CI [6.75, 10.48], p<0.001p<0.001), indicating that individuals required more adopting peers under greater payoff uncertainty. Risk preferences and subjective interpretations of uncertainty (measured in the probability estimation task, see Methods) were significant predictors of adoption thresholds. More risk-averse individuals displayed higher thresholds (OR = 1.31, 95% CI [1.02, 1.68], p=0.033p=0.033). In addition, individuals who overestimated the probability of product success under uncertainty exhibited lower thresholds (OR = 0.64, 95% CI [0.50, 0.82], p=0.001p=0.001). Furthermore, higher education (OR = 1.31, 95% CI [1.02, 1.67], p=0.034p=0.034) was associated with higher thresholds while male gender was associated with lower thresholds (OR = 0.54, 95% CI [0.33, 0.88], p=0.014p=0.014). Overall, fixed effects explained 12% of the variance in adoption (Stage 1 marginal R2=0.12R^{2}=0.12) and 41% of the variance in thresholds (Stage 2 marginal R2=0.41R^{2}=0.41). Including random intercepts increased explained variance to 98% and 70%, respectively (conditional R2R^{2}), indicating substantial between-participant heterogeneity in choice functions.

Together, these results demonstrate that heterogeneity in choice functions arises both from product characteristics such as payoff uncertainty, and individual characteristics such as risk preferences, subjective interpretation of uncertainty, and demographic factors.

### Implication for the role of long ties in social contagions

![Refer to caption](macro.png)


Fig. 3: Collective-level results (A) We manipulate long ties by rewiring pairs of edges starting from a ring lattice while keeping the degree of the network fixed [[41](https://arxiv.org/html/2510.04785v1#bib.bib41)]. Each rewiring introduces long ties, moving the network from a ring lattice to a random graph. (B) Average final fraction of adopters in the different uncertainty conditions in function of the number of rewiring. Results from the ABM simulations with: network size N=399N=399, degree k=4k=4. The initial seeds are random pair of connected nodes. Each point in the graph is the average of R=500R=500 diffusion realization in which subjects are randomly placed on the network. Error bars are the 95%95\% confidence intervals.

Uncertainty moderates the strength of long ties.
To study the role of long ties in social contagions, we simulate the diffusion of products by embedding the experimentally measured choice functions into an agent‐based model on synthetic networks. Starting from a ring lattice (N=399N=399, k=4k=4), we progressively introduce long ties by rewiring pairs of edges, preserving node degrees [[41](https://arxiv.org/html/2510.04785v1#bib.bib41)] (Fig. [3](https://arxiv.org/html/2510.04785v1#Sx2.F3 "Fig. 3 ‣ Implication for the role of long ties in social contagions ‣ Results ‣ A behavioral reinvestigation of the effect of long ties on social contagions")A).

Fig. [3](https://arxiv.org/html/2510.04785v1#Sx2.F3 "Fig. 3 ‣ Implication for the role of long ties in social contagions ‣ Results ‣ A behavioral reinvestigation of the effect of long ties on social contagions")B shows the average fraction of adopters as a function of the number of rewired edges for each uncertainty condition. Under no, low, and high uncertainty, adding long ties increased the final fraction of adopters. In contrast, under full uncertainty, diffusion stalled shortly after seeding due to the predominance of high-threshold individuals; in this case, long ties did not facilitate the diffusion process. Although our individual-level analysis showed that uncertainty on average increased the need for social reinforcement, at the collective level long ties did not hinder diffusion. This result is driven by heterogeneity in choice functions: in every uncertainty condition, a core group of low-threshold adopters remained. While long ties diluted local reinforcement, preventing some high-threshold individuals from adopting, they nonetheless reached low-threshold individuals. This prevented any negative effect of long ties. Our findings are robust for seeding size and network degree (see SI Appendix, Fig. S10 and Fig. S11), with larger seed sizes reducing the strength of the rewiring effect.

To study the mechanism, we examine the full uncertainty product and focus the analysis on individuals who adopt the product. While the total number of adopters did not vary with the number of rewiring (Fig. [3](https://arxiv.org/html/2510.04785v1#Sx2.F3 "Fig. 3 ‣ Implication for the role of long ties in social contagions ‣ Results ‣ A behavioral reinvestigation of the effect of long ties on social contagions")B), the average thresholds of adopters did. Adopters in a ring lattice (rewiring =0=0) had significantly higher thresholds (M=0.198M=0.198) compared to those in the more random network (rewiring =200=200) (M=0.055M=0.055; Welch’s t-test, t​(436.7)=10.898t(436.7)=10.898, p<0.001p<0.001, 95%95\% CI [0.1170.117, 0.1690.169], see SI Appendix Fig. S4). This result illustrates how, in a heterogeneous population, introducing long ties generates a trade-off between activating local nodes with higher thresholds or distant ones with lower thresholds. Only in the special case in which we restrict the population composition to individuals with complex choice functions, long ties hinder diffusion (see SI Appendix Fig. S5).

## Discussion

Many real-world decisions involve some degree of risk and uncertainty. In navigating these decisions, individuals often look at their social networks [[3](https://arxiv.org/html/2510.04785v1#bib.bib3)], giving rise to social contagion dynamics. Understanding how network structure moderates contagion processes not only addresses core theoretical debates in social sciences but also informs practical interventions in domains ranging from technology adoption and public health to collective creativity and team performance [[42](https://arxiv.org/html/2510.04785v1#bib.bib42), [43](https://arxiv.org/html/2510.04785v1#bib.bib43), [44](https://arxiv.org/html/2510.04785v1#bib.bib44)].

This paper investigates the effect of long ties on the diffusion of products with uncertain payoffs. Prior theoretical work has highlighted both the potential benefits of long ties for spreading products and behaviors, as well as conditions under which long ties may hinder diffusion [[26](https://arxiv.org/html/2510.04785v1#bib.bib26), [31](https://arxiv.org/html/2510.04785v1#bib.bib31), [32](https://arxiv.org/html/2510.04785v1#bib.bib32)]. Yet, empirical evidence on the role of long ties directly connecting individual-level decision-making to network-level diffusion outcomes remains limited. Ref. [[24](https://arxiv.org/html/2510.04785v1#bib.bib24)] is among the few, possibly the only, controlled experiments manipulating network structure. We empirically measure the microfoundations of social influence using a lottery-based adoption task [[38](https://arxiv.org/html/2510.04785v1#bib.bib38)] and a modified strategy method [[39](https://arxiv.org/html/2510.04785v1#bib.bib39)]. We then embed the measured choice function in simulations manipulating network structure. The advantage of measuring individual choice functions is that we can study counterfactual “worlds” [[45](https://arxiv.org/html/2510.04785v1#bib.bib45)] simulating diffusion dynamics using the same subject sample.

We find that roughly 90%90\% of individuals exhibit a monotonic choice function which can be well captured by a threshold. The remaining 10%10\% exhibit non-monotonic choice functions that can be interpreted as noise [[30](https://arxiv.org/html/2510.04785v1#bib.bib30)] or as genuine preferences (e.g., majority aversion). On average, as payoff uncertainty increases, more subjects become susceptible to social influence and require higher social reinforcement to adopt, moving the population from having predominantly simple to complex choice functions. This pattern aligns with previous empirical findings [[46](https://arxiv.org/html/2510.04785v1#bib.bib46)] as well as with complex contagion theory, which argues that costly or risky decisions require social reinforcement to propagate [[23](https://arxiv.org/html/2510.04785v1#bib.bib23), [26](https://arxiv.org/html/2510.04785v1#bib.bib26)].

Measuring individual‐level choice functions allows us to move beyond average social‐reinforcement effects [[47](https://arxiv.org/html/2510.04785v1#bib.bib47), [24](https://arxiv.org/html/2510.04785v1#bib.bib24), [48](https://arxiv.org/html/2510.04785v1#bib.bib48), [49](https://arxiv.org/html/2510.04785v1#bib.bib49)] and study individual differences [[50](https://arxiv.org/html/2510.04785v1#bib.bib50)]. We document substantial heterogeneity even under high and full uncertainty: while many subjects require multiple adopting peers to trigger adoption, a minority adopt after minimal exposure. Classic diffusion research emphasized heterogeneity primarily through the timing of adoption—categorizing individuals as innovators, early adopters, or laggards [[51](https://arxiv.org/html/2510.04785v1#bib.bib51), [52](https://arxiv.org/html/2510.04785v1#bib.bib52)]. Our findings provide a behavioral account of such heterogeneity. We find that, while diffusion-level attributes such as product risk and uncertainty shape the average choice function, preferences and subjective interpretations of uncertainty account for individual heterogeneity in choice functions. More closely aligned with our design, recent work has demonstrated systematic variation in how individuals integrate social information [[53](https://arxiv.org/html/2510.04785v1#bib.bib53)] and respond to uncertainty [[54](https://arxiv.org/html/2510.04785v1#bib.bib54)].

Heterogeneity in individual choice functions is a fundamental driver of diffusion dynamics [[55](https://arxiv.org/html/2510.04785v1#bib.bib55), [56](https://arxiv.org/html/2510.04785v1#bib.bib56), [57](https://arxiv.org/html/2510.04785v1#bib.bib57), [58](https://arxiv.org/html/2510.04785v1#bib.bib58)]. Yet, most simulation studies examining long ties assume a homogeneous population or rely on arbitrary threshold distributions (normal or truncated normal), mostly relegating heterogeneity to robustness analyses [[23](https://arxiv.org/html/2510.04785v1#bib.bib23), [32](https://arxiv.org/html/2510.04785v1#bib.bib32)]. To date, the most notable discussion of heterogeneity focuses on stochastic perturbations to individual thresholds [[30](https://arxiv.org/html/2510.04785v1#bib.bib30)], treating heterogeneity as random noise rather than systematic differences to understand [[50](https://arxiv.org/html/2510.04785v1#bib.bib50)]. By embedding empirically measured heterogeneity into agent-based models, we find that although the marginal advantage of long ties declines with increasing uncertainty, the observed presence of simple choice functions prevents the “weakness of long ties” [[23](https://arxiv.org/html/2510.04785v1#bib.bib23)]. The reason behind this result is that, across all product configurations we find heterogeneous populations in which individuals with simple and complex choice functions coexist. In such cases, long ties—while diluting local reinforcement and thus reducing adoption in individuals with more complex choice functions—still reach the small fraction of individuals with simple choice functions, which ultimately prevents any negative effect of long ties. This means that in a heterogeneous population, the reach–reinforcement trade‐off highlighted in Ref. [[32](https://arxiv.org/html/2510.04785v1#bib.bib32)] unfolds within the same social contagion. Our results point to a mechanism—heterogeneity in choice function—for which long ties are robust to behavioral complexity [[30](https://arxiv.org/html/2510.04785v1#bib.bib30), [49](https://arxiv.org/html/2510.04785v1#bib.bib49), [31](https://arxiv.org/html/2510.04785v1#bib.bib31), [32](https://arxiv.org/html/2510.04785v1#bib.bib32)].

Overall the effect of long ties in social contagion depends on the population composition. We show that both results reported in prior literature are possible. For homogeneous populations with simple choice functions, long ties are strong and promote diffusion [[12](https://arxiv.org/html/2510.04785v1#bib.bib12)]. For homogeneous populations with complex choice functions, long ties are weak and hinder diffusion [[23](https://arxiv.org/html/2510.04785v1#bib.bib23)]. For heterogeneous populations, long ties promote diffusion as long as some individuals have simple choice functions [[30](https://arxiv.org/html/2510.04785v1#bib.bib30)]. This behavioral perspective suggests that empirical evidence of the “weakness of long ties” [[24](https://arxiv.org/html/2510.04785v1#bib.bib24)] may stem from homogeneous populations, where individuals share similar preferences and respond similarly to peers’ behavior.

In sum, we empirically revisit the role of long ties in social contagions by connecting experimental decisions to computational simulations. We document and explain heterogeneity in how individuals respond to social influence and highlight its central role in moderating the relation between network structure and diffusion dynamics. We propose that whether long ties are beneficial or detrimental cannot be reduced to an inherent property of the diffusion process (simple vs. complex contagion) but rather depends on the distribution of individual-level choice functions in the population.

We acknowledge several limitations which call for future research. At the task level, our incentive-aligned design captures decisions under social influence for products with payoff uncertainty but omits temporal dynamics and normative pressures. Specifically, our elicitation method might encourage subjects to express monotonic choice functions, thus setting an upper bound for threshold-like behavior. At the information level, subjects observed peers’ adoption decisions but no topology; thus, the manipulation operated through exposure patterns rather than perceived network structure. At the modeling level, simulations used synthetic fixed-degree networks and excluded homophily. Future work could explore different forms of uncertainty [[59](https://arxiv.org/html/2510.04785v1#bib.bib59)], extend the design to different adoption tasks [[33](https://arxiv.org/html/2510.04785v1#bib.bib33)], allow subjects to learn and reason about network structure [[60](https://arxiv.org/html/2510.04785v1#bib.bib60)], and embed measured choice functions in empirical networks with homophily [[61](https://arxiv.org/html/2510.04785v1#bib.bib61), [62](https://arxiv.org/html/2510.04785v1#bib.bib62), [63](https://arxiv.org/html/2510.04785v1#bib.bib63)]. By linking experimentally measured choice functions to network simulations, our approach provides a basis for these extensions.

## Material and Methods

![Refer to caption](lottery.png)


Fig. 4: Product configurations. Products were represented as urn lotteries. Each lottery is denoted by (nb,no,ng;X)(n\_{b},n\_{o},n\_{g};X) in an urn of N=40N=40 balls: nbn\_{b} blue balls (giving a payoff of XX), non\_{o} orange balls (giving payoff of 0), and ngn\_{g} gray balls (hidden color). The seven products varied along two dimensions: uncertainty, given by the proportion of hidden (gray) balls (0%0\%, 25%25\%, 50%50\%, 100%100\%), and risk, defined as the probability of a winning XX based on the visible balls (low risk: 90%90\%; high risk: 50%50\%).

### Subjects and experimental conditions

This study was approved by the Institutional Review Board at the University of Zurich and preregistered (AsPredicted #228275). All subjects provided informed consent. We recruited 572572 subjects from the online platform Prolific. All subjects were required to successfully complete comprehension checks prior to accessing the experiment to ensure full understanding of the task, payoff structure, and conditional choice elicitation procedure (attrition rate of 13%13\%). A total of 500500 subjects completed the study. Of the total sample, 399399 subjects were randomly assigned to the social influence condition reported in the main text. 101101 subjects were assigned to the no-social-influence condition, in this condition subjects completed the same tasks but without peer information, providing unconditional adoption choices that served as a baseline estimate of intrinsic adoption propensity (see SI Appendix for results of this condition).

### Products as risky lotteries with uncertain payoff

We used Ellsberg-style urn lotteries to represent products [[38](https://arxiv.org/html/2510.04785v1#bib.bib38)]. Each lottery is specified by (nb,no,ng;X)(n\_{b},n\_{o},n\_{g};X) in an urn with 4040 balls: nbn\_{b} blue (win XX), non\_{o} orange (win 0), and ngn\_{g} gray (hidden color). Subjects observed (nb,no,ng)(n\_{b},n\_{o},n\_{g}) but not the composition of the gray balls. The true success probability π\pi is fixed but unknown and lies in [L,U][L,U], where L=nb/NL=n\_{b}/N and U=(nb+ng)/NU=(n\_{b}+n\_{g})/N. We did not specify or assume any distribution over the hidden composition; subjects observed only the bounds [L,U][L,U]. The safe lottery yielded a sure 100100 points. Risky and uncertain lotteries paid X=300X=300 upon a blue draw, otherwise 0. For example, the lottery (10,10,20;300)(10,10,20;300) (with 4040 balls) is displayed as 10 blue, 10 orange, and 20 gray balls, implying π∈[10/40,(10+20)/40]=[0.25,0.75]\pi\in\big[10/40,\,(10+20)/40\big]=[0.25,0.75]. See Fig. [4](https://arxiv.org/html/2510.04785v1#Sx4.F4 "Fig. 4 ‣ Material and Methods ‣ A behavioral reinvestigation of the effect of long ties on social contagions") for all product configurations and SI Appendix Fig. S1 for the adoption task instructions.

### Incentive scheme

To ensure incentive compatibility, we employed the following procedure. In the instructions, we told subjects that after the experiment, we would form groups and their decisions would be played for real monetary payoff. After the experiment, we randomly drew (i) one of the two risk levels and (ii) for each subject, a payoff-uncertainty level. Because subjects had been told that peers might hold more or less information about the product, this randomization ensured consistency between instructions and incentives. The resulting combination defined the single individual task that was used to determine each subject’s payoff. We then simulated a diffusion process on a synthetic network in which each subject was connected to k=4k=4 peers. From the subject’s perspective, this was equivalent to belonging to a group of four others. Subjects whose choice function prescribed adoption when observing 0/40/4 adopters were designated as initial adopters (seeds). In each subsequent time step, non-adopters observed the number of their four neighbors who had adopted and applied their pre-recorded choice function to decide whether to adopt. The diffusion process continued until no further adoptions occurred (or until 100 time step). Each subject’s final adoption state then determined their payoff. Because any entry in every conditional choice function could become payoff-relevant, subjects had a strict incentive to reveal their true adoption preferences for all peer-adoption level [[39](https://arxiv.org/html/2510.04785v1#bib.bib39), [64](https://arxiv.org/html/2510.04785v1#bib.bib64), [65](https://arxiv.org/html/2510.04785v1#bib.bib65)].

### Probability estimation task

To capture how subjects interpret uncertainty, we asked them to estimate the probability of drawing a blue ball from a 40-ball urn in the high risk condition (50% blue, 50% orange) and three uncertainty levels: none (0% gray balls), low (25%), and high (50%). Subjects provided numerical estimates of the probability (0–100%), without monetary incentives. The no-uncertainty condition was always presented first, while the order of the low- and high-uncertainty conditions was randomized across subjects. All N=500N=500 subjects completed the task. Full task details and are provided in SI Appendix Fig. S3.

### Risk preference task

To measure subjects’ risk preferences, we implemented the multiple price list method [[40](https://arxiv.org/html/2510.04785v1#bib.bib40)]. In each of ten paired lottery choices (see SI Appendix Fig. S3), subjects selected between a relatively safe Option A (smaller variance, lower expected payoff) and a riskier Option B (higher variance, higher expected payoff). Across rows, the probability of receiving the high payoff increased in increments of 0.1 (from 0.1 to 1.0), while payoffs remained fixed within each option. Risk aversion was quantified as the fraction of safe Option A choices across the ten decisions. To provide incentives, one participant was selected at random at the end of the study, and one of their ten choices was randomly drawn and played for real monetary payoffs. All N=500N=500 subjects completed the task.

### Network structure

All simulations used synthetic networks with fixed degree k=4k=4, consisting of N=399N=399 nodes, corresponding to the number of subjects in the social influence condition. We used ring lattice network and introduced long ties by rewiring pairs of edges using a degree-preserving rewiring algorithm [[41](https://arxiv.org/html/2510.04785v1#bib.bib41)]. For each rewiring step, two randomly chosen edges were selected and their endpoints swapped, thereby preserving node degrees while progressively introducing long ties.

### Seeding and diffusion dynamics

To simulate the diffusion of the products, we implemented an agent-based model (ABM) analogous to a susceptible-infected (SI) model, where individuals are either non-adopters (susceptible) or adopters (infected). Adoption decisions were governed by the empirically measured choice functions obtained from the experimental data. For each simulation run, a new network structure was generated and subjects’ empirically measured choice functions were randomly assigned to nodes. Diffusion was initiated by randomly selecting one pair of connected nodes to serve as initial adopters (seeds). At each time step, all non-adopting nodes synchronously evaluated their adoption decision based on the number of adopting peers at the previous time step. Adoption occurred following the decisions of the subject’s experimentally measured choice function. Each simulation proceeded iteratively until the system reached a stable state or after 100100 time steps. For each combination of product and rewiring level, we conducted 500500 independent simulation runs with newly generated network to account for stochastic variation in network rewiring, node assignment, and seed placement. The outcome measure was the final fraction of adopters in the network at convergence.

### Code and data availability

The code and data used to obtain the findings of this study will be made publicly available upon publication.

### Acknowledgments

We thank P. Smaldino, E. Fehr, participants in the Quantitative Marketing Research seminar at the University of Zurich and ETH Zurich, as well as attendees at the Sunbelt and IC2S2 conferences, for their helpful comments and insightful discussions. This work has been supported by the URPP Social Networks and the Swiss National Science Foundation (SNSF) (Grant No. 100013–207888 and 100013-236802).

## References

\c@NAT@ctr

## References

* [1]

  Cristina Bicchieri.
  Norms in the wild: How to diagnose, measure, and change social norms.
  Oxford University Press, 2016.
* [2]

  Eitan Muller and Renana Peres.
  The effect of social networks structure on innovation performance: A review and directions for research.
  International Journal of Research in Marketing, 36(1):3–19, 2019.
* [3]

  Oriel FeldmanHall and Amitai Shenhav.
  Resolving uncertainty in a social world.
  Nature Human Behaviour, 3(5):426–435, 4 2019.
* [4]

  Arnout Van De Rijt.
  Self-Correcting dynamics in social influence processes.
  American Journal of Sociology, 124(5):1468–1495, 3 2019.
* [5]

  Bryce Ryan and Neal C Gross.
  The diffusion of hybrid seed corn in two iowa communities.
  Rural sociology, 8(1):15, 1943.
* [6]

  Herbert Frederick Lionberger.
  Adoption of new ideas and practices.
  Iowa State Press, 1 1960.
* [7]

  James Coleman, Elihu Katz, and Herbert Menzel.
  The diffusion of an innovation among physicians.
  Sociometry, 20(4):253–270, 1957.
* [8]

  Nicholas A. Christakis and James H. Fowler.
  The Spread of Obesity in a Large Social Network over 32 Years.
  New England Journal of Medicine, 357(4):370–379, 7 2007.
* [9]

  Abhijit Banerjee, Arun G. Chandrasekhar, Esther Duflo, and Matthew O. Jackson.
  The diffusion of microfinance.
  Science, 341(6144), 7 2013.
* [10]

  Sinan Aral and Christos Nicolaides.
  Exercise contagion in a global social network.
  Nature Communications, 8(1), 4 2017.
* [11]

  Thomas W Valente.
  Network interventions.
  Science, 337(6090):49–53, 2012.
* [12]

  Mark S Granovetter.
  The strength of weak ties.
  American Journal of Sociology, 78(6):1360–1380, 1973.
* [13]

  Jacqueline Johnson Brown and Peter H Reingen.
  Social ties and word-of-mouth referral behavior.
  Journal of Consumer research, 14(3):350–362, 1987.
* [14]

  Ronald S. Burt.
  Structural Holes: The Social Structure of Competition.
  Harvard University Press, Cambridge, MA, 1992.
* [15]

  Duncan J Watts and Steven H Strogatz.
  Collective dynamics of small-world networks.
  Nature, 393(6684):440–442, 1998.
* [16]

  Jacob Goldenberg, Barak Libai, and Eitan Muller.
  Talk of the network: A complex systems look at the underlying process of word-of-mouth.
  Marketing Letters, 12:211–223, 2001.
* [17]

  Oliver Hinz, Bernd Skiera, Christian Barrot, and Jan U Becker.
  Seeding strategies for viral marketing: An empirical comparison.
  Journal of Marketing, 75(6):55–71, 2011.
* [18]

  Linyuan Lü, Duan-Bing Chen, and Tao Zhou.
  The small world yields the most effective information spreading.
  New Journal of Physics, 13(12):123005, 2011.
* [19]

  Eytan Bakshy, Itamar Rosenn, Cameron Marlow, and Lada Adamic.
  The role of social networks in information diffusion.
  In Proceedings of the 21st International Conference on World Wide Web, pages 519–528, 2012.
* [20]

  Jeffrey K Lee and Ann Kronrod.
  The strength of weak-tie consensus language.
  Journal of Marketing Research, 57(2):353–374, 2020.
* [21]

  Karthik Rajkumar, Guillaume Saint-Jacques, Iavor Bojinov, Erik Brynjolfsson, and Sinan Aral.
  A causal test of the strength of weak ties.
  Science, 377(6612):1304–1310, 2022.
* [22]

  Eaman Jahani, Samuel P Fraiberger, Michael Bailey, and Dean Eckles.
  Long ties, disruptive life events, and economic prosperity.
  Proceedings of the National Academy of Sciences, 120(28):e2211062120, 2023.
* [23]

  Damon Centola and Michael Macy.
  Complex Contagions and the Weakness of Long Ties.
  American Journal of Sociology, pages 702–734, 2007.
* [24]

  Damon Centola.
  The spread of behavior in an online social network experiment.
  Science, 329(5996):1194–1197, 9 2010.
* [25]

  Muhua Zheng, Linyuan Lü, and Ming Zhao.
  Spreading in online social networks: The role of social reinforcement.
  Physical Review E, 88(1):012818, 2013.
* [26]

  Douglas Guilbeault, Joshua Becker, and Damon Centola.
  Complex contagions: A decade in review.
  Complex Spreading Phenomena in Social Systems, pages 3–25, 2018.
* [27]

  Daniele Notarmuzi, Claudio Castellano, Alessandro Flammini, Dario Mazzilli, and Filippo Radicchi.
  Universality, criticality and complexity of information propagation in social media.
  Nature Communications, 13(1):1308, 2022.
* [28]

  Manuel S Mariani, Federico Battiston, Emőke-Ágnes Horvát, Giacomo Livan, Federico Musciotto, and Dashun Wang.
  Collective dynamics behind success.
  Nature Communications, 15(1):10701, 2024.
* [29]

  P.S. Dodds and D.J. Watts.
  A generalized model of social and biological contagion.
  Journal of Theoretical Biology, 232(4):587–604, 2005.
* [30]

  Dean Eckles, Elchanan Mossel, M. Amin Rahimian, and Subhabrata Sen.
  Long ties accelerate noisy threshold-based contagions.
  Nature Human Behaviour, pages 1057–1064, 2024.
* [31]

  Jad Georges Sassine and Hazhir Rahmandad.
  How does network structure impact socially reinforced diffusion?
  Organization Science, 35(1):52–70, 2024.
* [32]

  Allison Wan, Christoph Riedl, and David Lazer.
  Diffusion of complex contagions is shaped by a trade-off between reach and reinforcement.
  Proceedings of the National Academy of Sciences, 122(28), 7 2025.
* [33]

  Radu Tanase, René Algesheimer, and Manuel S Mariani.
  Integrating behavioral experimental findings into dynamical models to inform social change interventions.
  arXiv preprint arXiv:2405.13224, 2024.
* [34]

  Renana Peres, Eitan Muller, and Vijay Mahajan.
  Innovation diffusion and new product growth models: A critical review and research directions.
  International Journal of Research in Marketing, 27(2):91–106, 3 2010.
* [35]

  Edward Bishop Smith and William Rand.
  Simulating Macro-Level Effects from Micro-Level Observations.
  Management Science, 64(11):5405–5421, 12 2017.
* [36]

  Joseph B. Bak-Coleman, Mark Alfano, Wolfram Barfuss, Carl T. Bergstrom, Miguel A. Centeno, Iain D. Couzin, Jonathan F. Donges, Mirta Galesic, Andrew S. Gersick, Jennifer Jacquet, Albert B. Kao, Rachel E. Moran, Pawel Romanczuk, Daniel I. Rubenstein, Kaia J. Tombak, Jay J. Van Bavel, and Elke U. Weber.
  Stewardship of global collective behavior.
  Proceedings of the National Academy of Sciences, 118(27), 6 2021.
* [37]

  Mirta Galesic, Wändi Bruine De Bruin, Jonas Dalege, Scott L. Feld, Frauke Kreuter, Henrik Olsson, Drazen Prelec, Daniel L. Stein, and Tamara Van Der Does.
  Human social sensing is an untapped resource for computational social science.
  Nature, 595(7866):214–222, 6 2021.
* [38]

  Daniel Ellsberg.
  Risk, ambiguity, and the savage axioms.
  The Quarterly Journal of Economics, 75(4):643, 11 1961.
* [39]

  Reinhard Selten.
  Die strategiemethode zur erforschung des eingeschränkt rationalen verhaltens im rahmen eines oligopolexperimentes.
  Beiträge zur experimentellen Wirtschaftsforschung, page 136, 1967.
* [40]

  Charles A Holt and Susan K Laury.
  Risk aversion and incentive effects.
  American Economic Review, 92(5):1644–1655, 11 2002.
* [41]

  Sergei Maslov and Kim Sneppen.
  Specificity and stability in topology of protein networks.
  Science, 296(5569):910–913, 5 2002.
* [42]

  Lori Beaman, Ariel BenYishay, Jeremy Magruder, and Ahmed Mushfiq Mobarak.
  Can Network Theory-Based targeting increase technology adoption?
  American Economic Review, 111(6):1918–1943, 5 2021.
* [43]

  David A Kim, Alison R Hwong, Derek Stafford, D Alex Hughes, A James O’Malley, James H Fowler, and Nicholas A Christakis.
  Social network targeting to maximise population behaviour change: a cluster randomised controlled trial.
  The Lancet, 386(9989):145–153, 5 2015.
* [44]

  Brian Uzzi and Jarrett Spiro.
  Collaboration and Creativity: the Small World Problem.
  American Journal of Sociology, 111(2):447–504, 9 2005.
* [45]

  Matthew J. Salganik, Peter Sheridan Dodds, and Duncan J. Watts.
  Experimental study of inequality and unpredictability in an artificial cultural market.
  Science, 311(5762):854–856, 2006.
* [46]

  Wataru Toyokawa, Andrew Whalen, and Kevin N. Laland.
  Social learning strategies regulate the wisdom and madness of interactive crowds.
  Nature Human Behaviour, 3(2):183–193, 1 2019.
* [47]

  Jure Leskovec, Lada A. Adamic, and Bernardo A. Huberman.
  The dynamics of viral marketing.
  ACM Transactions on the Web, 1(1):5, 5 2007.
* [48]

  Eytan Bakshy, Dean Eckles, Rong Yan, and Itamar Rosenn.
  Social influence in social advertising: evidence from field experiments.
  In Proceedings of the 13th ACM Conference on Electronic Commerce, EC ’12, page 146–161, New York, NY, USA, 2012. Association for Computing Machinery.
* [49]

  Jaemin Lee, David Lazer, and Christoph Riedl.
  Complex contagion in viral marketing: Causal evidence from a country-scale field experiment.
  Northeastern U. D’Amore-McKim School of Business Research Paper, (4092057), 2022.
* [50]

  Christopher J. Bryan, Elizabeth Tipton, and David S. Yeager.
  Behavioural science is unlikely to change the world without a heterogeneity revolution.
  Nature Human Behaviour, 5(8):980–989, 7 2021.
* [51]

  Everett M. Rogers.
  Diffusion of innovations.
  New York : Free Press of Glencoe, 1 1962.
* [52]

  Thomas W. Valente.
  Social network thresholds in the diffusion of innovations.
  Social Networks, 18(1):69–89, 1 1996.
* [53]

  Lucas Molleman, Alan N. Tump, Andrea Gradassi, Stefan Herzog, Bertrand Jayles, Ralf H. J. M. Kurvers, and Wouter Van Den Bos.
  Strategies for integrating disparate social information.
  Proceedings of the Royal Society B Biological Sciences, 287(1939):20202413, 11 2020.
* [54]

  Laura Zimmermann, Jeeva Somasundaram, and Barsha Saha.
  Adoption of new technology vaccines.
  Journal of Marketing, 88(4):1–21, 11 2023.
* [55]

  Mark Granovetter.
  Threshold models of collective behavior.
  American Journal of Sociology, 83(6):1420–1443, 5 1978.
* [56]

  Duncan J. Watts.
  A simple model of global cascades on random networks.
  Proceedings of the National Academy of Sciences, 99(9):5766–5771, 4 2002.
* [57]

  Hazhir Rahmandad and John Sterman.
  Heterogeneity and network structure in the dynamics of diffusion: Comparing Agent-Based and Differential Equation models.
  Management Science, 54(5):998–1014, 3 2008.
* [58]

  H. Peyton Young.
  Innovation diffusion in heterogeneous populations: contagion, social influence, and social learning.
  American Economic Review, 99(5):1899–1924, 12 2009.
* [59]

  Matthew A. Turner, Cristina Moya, Paul E. Smaldino, and James Holland Jones.
  The form of uncertainty affects selection for social learning.
  Evolutionary Human Sciences, 5:e20, 2023.
* [60]

  Raina A. Brands.
  Cognitive social structures in social network research: A review.
  Journal of Organizational Behavior, 34(S1), 7 2013.
* [61]

  Sinan Aral, Lev Muchnik, and Arun Sundararajan.
  Distinguishing influence-based contagion from homophily-driven diffusion in dynamic networks.
  Proceedings of the National Academy of Sciences, 106(51):21544–21549, 2009.
* [62]

  Damon Centola.
  An experimental study of homophily in the adoption of health behavior.
  Science, 334(6060):1269–1272, 2011.
* [63]

  Elena M. Tur, Paolo Zeppini, and Koen Frenken.
  Diffusion in small worlds with homophily and social reinforcement: A theoretical model.
  Social Networks, 76:12–21, 6 2023.
* [64]

  Urs Fischbacher, Simon Gächter, and Ernst Fehr.
  Are people conditionally cooperative? Evidence from a public goods experiment.
  Economics Letters, 71(3):397–404, 6 2001.
* [65]

  G. Charness and M. Rabin.
  Understanding Social Preferences with Simple Tests.
  The Quarterly Journal of Economics, 117(3):817–869, 8 2002.

Supplementary Material for:

A behavioral reinvestigation of the effect of long ties on social contagions

Luca Lazzaro, Manuel S. Mariani, René Algesheimer, Radu Tanase

## S1 Supporting text

### Result for all product configurations

#### Individual-level results

Fig. [S6](https://arxiv.org/html/2510.04785v1#S2.F6 "Fig. S6 ‣ S2 Additional figures ‣ A behavioral reinvestigation of the effect of long ties on social contagions") shows the individual choice functions for products in the high-risk condition (Panel B). Similar to the low-risk condition (Panel A), individual choice functions showed high heterogeneity and were well described by monotonic thresholds in roughly 90% of cases. The main difference, compared to the low-risk condition, was that thresholds were on average higher, indicating that riskier products required higher social reinforcement before adoption or will not be adopted at all. Fig. [S8](https://arxiv.org/html/2510.04785v1#S2.F8 "Fig. S8 ‣ S2 Additional figures ‣ A behavioral reinvestigation of the effect of long ties on social contagions") shows the individual-level results for the high-risk condition (Panel B). The results remained qualitatively similar to the low-risk condition (Panel A). Although high risk reduced differences across uncertainty levels, the same overall patterns emerged: higher uncertainty increased the number of susceptible individuals and the reliance on social reinforcement. Consequently, the prevalence of simple (complex) choice functions decreased (increased) with uncertainty.

To explore the sources of heterogeneity in choice functions, we used the same two-stage mixed-effects model as in the main text. The first stage estimated the probability of adoption using a binomial logistic regression with participant random intercepts. The second stage estimated adoption thresholds conditional on adoption using a cumulative logit mixed model, again with participant random intercepts. Results are reported in Tab. [S2](https://arxiv.org/html/2510.04785v1#S3.T2 "Table S2 ‣ S3 Additional tables ‣ A behavioral reinvestigation of the effect of long ties on social contagions").
In the adoption stage (Stage 1), the baseline probability of adoption was high (p≈0.81p\approx 0.81) but lower than in the low-risk condition. Adoption was less likely for more risk-averse individuals (OR = 0.55, 95% CI [0.42, 0.73], p<0.001p<0.001), while those who overestimated the probability of success under uncertainty (see estimation task in Methods and Fig. [S2](https://arxiv.org/html/2510.04785v1#S2.F2 "Fig. S2 ‣ S2 Additional figures ‣ A behavioral reinvestigation of the effect of long ties on social contagions")) were more likely to adopt the product (OR = 1.52, 95% CI [1.18, 1.96], p=0.001p=0.001). Uncertainty, unlike in the low-risk condition, was not a significant predictor of adoption (OR = 0.96, 95% CI [0.82, 1.12], p=0.594p=0.594). Together, the results from Stage 1 indicate that adoption in the high-risk condition depended less on uncertainty and more on preferences and subjective uncertainty evaluations.
In the threshold stage (Stage 2), uncertainty had a strong positive effect on thresholds (OR = 1.46, 95% CI [1.27, 1.69], p<0.001p<0.001), indicating that individuals required more adopting peers under greater payoff uncertainty. Individuals who overestimated the probability of success under uncertainty exhibited lower thresholds (OR = 0.66, 95% CI [0.48, 0.91], p=0.011p=0.011), while male gender was associated with lower thresholds (OR = 0.51, 95% CI [0.27, 0.95], p=0.035p=0.035). Overall, the results broadly mirrored those of the low-risk condition, except for the role of risk aversion, which predicted the probability of adoption (Stage 1) but not the amount of social reinforcement needed (Stage 2).
Fixed effects explained 10% of the variance in adoption (Stage 1 marginal R2=0.10R^{2}=0.10) and 6% of the variance in thresholds (Stage 2 marginal R2=0.06R^{2}=0.06). Including random intercepts increased explained variance to 52% and 65%, respectively (conditional R2R^{2}), again indicating substantial between-participant heterogeneity in choice functions.

#### Collective-level results

Fig. [S9](https://arxiv.org/html/2510.04785v1#S2.F9 "Fig. S9 ‣ S2 Additional figures ‣ A behavioral reinvestigation of the effect of long ties on social contagions") shows the collective-level results for the high-risk condition (Panel B). Again, the results remained qualitatively similar. Although high risk reduced differences across uncertainty levels, uncertainty continued to moderate the impact of long ties. The main difference was that for high-risk products, even a minimal degree of uncertainty was sufficient to impede diffusion, as many individuals exhibited high thresholds. This is reflected in the very low number of final adopters shown in the figure.

### Results for the no-social influence condition

In the no–social influence condition, subjects (N=101N=101) completed the same adoption task described in the main text, but without peer information. This produced independent adoption choices that served as a baseline estimate of intrinsic adoption probability. Fig. [S7](https://arxiv.org/html/2510.04785v1#S2.F7 "Fig. S7 ‣ S2 Additional figures ‣ A behavioral reinvestigation of the effect of long ties on social contagions") shows aggregate choice functions, plotting the probability of adoption as a function of the number of adopting peers across uncertainty levels. The red dotted line represents the intrinsic adoption probability. Comparing the no–social influence condition with the social influence condition revealed that social influence could have both positive and negative effects on adoption probability. Overall, adoption probability increased with peer adoption. This effect was moderated by uncertainty and risk: low peer adoption was associated with below-intrinsic adoption probability across all product configurations, whereas high peer adoption was associated with above-intrinsic adoption probability only for products with high risk or high uncertainty.

## S2 Additional figures

![Refer to caption](Figures/adoption_task.png)


Fig. S1: Adoption task measuring choice functions. Subjects pre-specified whether they would adopt for each possible number of adopting peers (contingent plan for k∈{0,…,4}k\in\{0,\dots,4\}). This adapts the strategy method to incorporate social influence [[39](https://arxiv.org/html/2510.04785v1#bib.bib39)] and measure choice functions. The screenshot illustrates the low risk, high uncertainty product configuration.

![Refer to caption](Figures/estimation-task.png)


Fig. S2: Probability estimation task. Subjects estimated the probability of drawing a blue ball from a 40-ball urn under high (50% blue; 50% orange) risk and three uncertainty levels: no (0% gray balls), low (25%), and high (50%). The screenshot illustrates the high risk, low uncertainty configuration. We used this task to measure how individuals interpret uncertainty.

![Refer to caption](Figures/risk-aversion.png)


Fig. S3: Risk preference task. Choices between paired lotteries used to elicit risk preferences following the multiple price list method [[40](https://arxiv.org/html/2510.04785v1#bib.bib40)]. Option A represents the relatively safe lottery with smaller variance in payoffs, while Option B is the riskier lottery with higher variance. Probabilities of the high payoff increase in increments of 0.1 across rows. Risk aversion is measured as the fraction of safe Option A choices across the ten decisions.

![Refer to caption](Figures/boxplot_activation.png)


Fig. S4: Average threshold among adopters (high uncertainty, low risk condition). For each realization on a k=4k=4 network (N=399N=399), we compute the mean adoption threshold of the nodes that adopt the product at the end of the diffusion. Threshold defined as the smallest number of adopting neighbors (out of 4) required for adoption (k/4k/4). Results are shown for a ring lattice (clustered network with rewiring = 0) and for a more random network (rewiring = 200200). Diffusion is seeded with a randomly chosen connected pair, subjects are randomly assigned to nodes each run, and updates are synchronous. We report the exact p-value. R=500R=500 independent realizations per condition. Welch’s two-sample tt-test (two-sided) on means shows a higher threshold in clustered than random networks: Δ=0.140\Delta=0.140 (95% CI [0.115, 0.165][0.115,\,0.165], t​(418.13)=10.93t(418.13)=10.93, p<0.001p<0.001).

![Refer to caption](Figures/weakness_long.png)


Fig. S5: Diffusion with complex choice functions only (high uncertainty, low risk condition). We restrict the population to subjects whose elicited choice functions exhibit complex contagion (threshold ≥2\geq 2 of 4 neighbors; allowed thresholds {2/4, 3/4, 4/4}\{2/4,\,3/4,\,4/4\}). Simulations run on a ring‐lattice network (degree k=4k=4, size N=221N=221) with long ties introduced via degree-preserving rewiring [[41](https://arxiv.org/html/2510.04785v1#bib.bib41)] at the indicated rewiring level. Diffusion is seeded by a randomly chosen connected pair and updates synchronously until convergence; subjects are randomly assigned to nodes each run. Points show the final number of adopters across R=500R=500 independent realizations; error bars are 95% CI across realizations.

![Refer to caption](Figures/all_threshold.png)


Fig. S6: Threshold distribution in all risk and uncertainty conditions. (A) Low-risk condition (same plot as in the main text, reported for comparison); (B) high-risk condition. Within each panel, bars show the proportion of subjects (N=399N=399) falling into each adoption-threshold category for each uncertainty level (No = 0% gray balls, Low = 25%, High = 50%, Full = 100%). A threshold is the smallest number of adopting neighbors (out of 4) required for adoption, derived from each participant’s experimental choices: 0/40/4 = unconditional adopter; 1/41/4, 2/42/4, 3/43/4, 4/44/4 = conditional adopters requiring progressively more peers; >1>1 = non-adopter (never adopts for k∈{0,…,4}k\in\{0,\dots,4\}); NM = non-monotonic pattern (choices not representable by a single threshold). Under Full uncertainty, risk is not manipulated by design; the corresponding distributions are identical across panels.

![Refer to caption](Figures/adoption_prob.png)


Fig. S7: Adoption probability in all risk and uncertainty conditions.
(A) low-risk condition; (B) high-risk condition. Within each panel, points show the adoption probability (fraction of subjects who adopt, N=399N=399) conditional on peer adoption k∈{0,…,4}k\in\{0,\dots,4\}, for each uncertainty level (No == 0% gray balls, Low == 25%, High == 50%, Full == 100%). Error bars are the 95%95\% confidence intervals for a single proportion computed per condition. The red dotted line marks the baseline adoption probability without social information (independent sample, N=101N=101); the light red band indicates its 95%95\% confidence intervals. Under Full uncertainty, risk is not manipulated by design; the corresponding plot are identical across panels.

![Refer to caption](Figures/micro-results.png)


Fig. S8: The effect of uncertainty on aggregated choice functions. (A) Low-risk condition (same plot as in the main text, reported for comparison). Fraction of individuals susceptible to social influence in the different uncertainty conditions (N=399N=399). Average social reinforcement required to adopt in the different uncertainty conditions (computed from adopting individuals in the different uncertainty conditions, Nno=365,Nlow=351,Nhigh=329,Nfull=253N\_{\text{no}}=365,\;N\_{\text{low}}=351,\;N\_{\text{high}}=329,\;N\_{\text{full}}=253. Fraction of individuals exhibiting simple and complex adoptions pattens in their choice functions for the different uncertainty condition (computed from adopting individuals, Nno=365,Nlow=351,Nhigh=329,Nfull=253N\_{\text{no}}=365,\;N\_{\text{low}}=351,\;N\_{\text{high}}=329,\;N\_{\text{full}}=253.
(B) high-risk condition. Fraction of individuals susceptible to social influence in the different uncertainty conditions (N=399N=399). Average social reinforcement required to adopt in the different uncertainty conditions (computed from adopting individuals in the different uncertainty conditions, Nno=249,Nlow=288,Nhigh=291,Nfull=253N\_{\text{no}}=249,\;N\_{\text{low}}=288,\;N\_{\text{high}}=291,\;N\_{\text{full}}=253. Fraction of individuals exhibiting simple and complex adoptions pattens in their choice functions for the different uncertainty condition (computed from adopting individuals, Nno=249,Nlow=288,Nhigh=291,Nfull=253N\_{\text{no}}=249,\;N\_{\text{low}}=288,\;N\_{\text{high}}=291,\;N\_{\text{full}}=253.
Error bars are the 95%95\% confidence intervals.

![Refer to caption](Figures/adopters-rewirings.png)


Fig. S9: Collective-level results Average final fraction of adopters in the different uncertainty conditions in function of the number of rewiring. (A) Low-risk condition (same plot as in the main text, reported for comparison); (B) high-risk condition. Simulations run on a ring‐lattice network (degree k=4k=4, size N=399N=399) with long ties introduced via degree-preserving rewiring [[41](https://arxiv.org/html/2510.04785v1#bib.bib41)] at the indicated rewiring level (Methods). Diffusion is seeded by a randomly chosen connected pair and updates synchronously until convergence; subjects are randomly assigned to nodes each run. Points show the final number of adopters across R=500R=500 independent realizations; error bars are 95% CI across realizations.

![Refer to caption](Figures/robust-seeding.png)


Fig. S10: Robustness check: seed size. Diffusion of products in the low-risk condition. Simulations are run on a ring‐lattice network (degree k=4k=4, size N=399N=399) with long ties introduced via degree-preserving rewiring [[41](https://arxiv.org/html/2510.04785v1#bib.bib41)] at the indicated rewiring level (Methods). Diffusion is initiated by randomly seeding adoption in s∈1,5,15,30s\in{1,5,15,30} connected pairs of node, and proceeds with synchronous updating until convergence. Subjects are randomly assigned to nodes in each run. Points show the final number of adopters across R=500R=500 independent realizations; error bars denote 95% confidence intervals across realizations.

![Refer to caption](Figures/robust-degree.png)


Fig. S11: Robustness check: network degree. Diffusion of products in the low-risk condition. Simulations are run on ring‐lattice networks (size N=399N=399) with degree k∈2,4,8,16k\in{2,4,8,16}, and long ties introduced via degree-preserving rewiring [[41](https://arxiv.org/html/2510.04785v1#bib.bib41)] at the indicated rewiring level (Methods). To extrapolate decisions to continuous fraction of adopting peers a∈[0,1]a\in[0,1], we mapped each aa to the nearest of the five experimentally observed levels {0,0.25,0.5,0.75,1}\{0,0.25,0.5,0.75,1\} (corresponding to 0–44 peers out of 44) and assigned the adoption decision measured at that level (ties resolved upward). Diffusion is initiated by randomly seeding a connected pair of adopters, and proceeds with synchronous updating until convergence. Subjects are randomly assigned to nodes in each run. Points show the final number of adopters across R=500R=500 independent realizations; error bars denote 95% confidence intervals across realizations.

## S3 Additional tables

Table S1: Full results of 2 stage mixed-effects models for low risk condition. Stage 1 models adoption (binary logit); Stage 2 models adoption thresholds among adopters (cumulative logit). Predictors are z-scored. Odds ratios (OR) with 95% CI and p-values are reported. The large intercept in Stage 1 reflects a very high baseline probability of adoption (p≈0.99p\approx 0.99).

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Stage 1: Adoption (logit) | | | Stage 2: Threshold (ordinal logit) | | |
| Predictor | OR | 95% CI | p-value | OR | 95% CI | p-value |
| (Intercept) | 423868.26 | [13800.10, 13019058.06] | <<0.001 | – | – | – |
| Uncertainty (numeric) | 0.02 | [0.01, 0.05] | <<0.001 | 8.41 | [6.75, 10.48] | <<0.001 |
| Risk aversion | 0.64 | [0.29, 1.39] | 0.262 | 1.31 | [1.02, 1.68] | 0.033 |
| Estimated prob. success | 1.50 | [0.72, 3.13] | 0.283 | 0.64 | [0.50, 0.82] | 0.001 |
| Age | 0.60 | [0.28, 1.29] | 0.194 | 1.17 | [0.91, 1.50] | 0.229 |
| Education | 0.94 | [0.46, 1.94] | 0.867 | 1.31 | [1.02, 1.67] | 0.034 |
| Gender (male) | 0.85 | [0.20, 3.65] | 0.826 | 0.54 | [0.33, 0.88] | 0.014 |
| Cutpoints (Stage 2 only) | | | | | | |
| 0||1/4 | – | – | – | 0.22 | [0.10, 0.50] | <<0.001 |
| 1/4||2/4 | – | – | – | 0.51 | [0.22, 1.16] | 0.106 |
| 2/4||3/4 | – | – | – | 2.73 | [1.19, 6.23] | 0.017 |
| 3/4||1 | – | – | – | 40.37 | [16.73, 97.41] | <<0.001 |
| Random effects | | | | | | |
| Residual variance (σ2\sigma^{2}) | 3.29 |  |  | 3.29 |  |  |
| Intercept variance (τ00\tau\_{00}) | 111.95 |  |  | 3.28 |  |  |
| ICC | 0.97 |  |  | 0.50 |  |  |
| N subjects | 326 |  |  | 320 |  |  |
| Model statistics | | | | | | |
| Observations | 1304 |  |  | 1150 |  |  |
| Marginal R2R^{2} | 0.123 |  |  | 0.405 |  |  |
| Conditional R2R^{2} | 0.975 |  |  | 0.702 |  |  |

Table S2: Full results of two stage mixed-effects models for the high risk condition. Stage 1 models adoption (binary logit); Stage 2 models adoption thresholds among adopters (cumulative logit). Predictors are z-scored. Odds ratios (OR) with 95% CI and p-values are reported.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Stage 1: Adoption (logit) | | | Stage 2: Threshold (ordinal logit) | | |
| Predictor | OR | 95% CI | p-value | OR | 95% CI | p-value |
| (Intercept) | 4.29 | [1.83, 10.09] | 0.001 | – | – | – |
| Uncertainty | 0.96 | [0.82, 1.12] | 0.594 | 1.46 | [1.27, 1.69] | <<0.001 |
| Risk aversion | 0.55 | [0.42, 0.73] | <<0.001 | 1.30 | [0.95, 1.76] | 0.099 |
| Estimated prob. success | 1.52 | [1.18, 1.96] | 0.001 | 0.66 | [0.48, 0.91] | 0.011 |
| Age | 0.83 | [0.64, 1.07] | 0.158 | 1.05 | [0.77, 1.44] | 0.750 |
| Education | 0.84 | [0.65, 1.08] | 0.173 | 1.16 | [0.85, 1.59] | 0.342 |
| Gender (male) | 1.16 | [0.69, 1.94] | 0.570 | 0.51 | [0.27, 0.95] | 0.035 |
| Cutpoints (Stage 2 only) | | | | | | |
| 0||1/4 | – | – | – | 0.02 | [0.01, 0.06] | <<0.001 |
| 1/4||2/4 | – | – | – | 0.03 | [0.01, 0.09] | <<0.001 |
| 2/4||3/4 | – | – | – | 0.14 | [0.05, 0.40] | <<0.001 |
| 3/4||1 | – | – | – | 2.87 | [1.02, 8.13] | 0.047 |
| Random effects | | | | | | |
| Residual variance (σ2\sigma^{2}) | 3.29 |  |  | 3.29 |  |  |
| Intercept variance (τ00\tau\_{00}) | 2.84 |  |  | 5.56 |  |  |
| ICC | 0.46 |  |  | 0.63 |  |  |
| N subjects | 326 |  |  | 299 |  |  |
| Model statistics | | | | | | |
| Observations | 1304 |  |  | 972 |  |  |
| Marginal R2R^{2} | 0.096 |  |  | 0.056 |  |  |
| Conditional R2R^{2} | 0.515 |  |  | 0.649 |  |  |