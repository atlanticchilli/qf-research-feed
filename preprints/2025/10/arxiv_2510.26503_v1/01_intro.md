---
authors:
- Pau Juan-Bartroli
- Esteban Muñoz-Sobrado
doc_id: arxiv:2510.26503v1
family_id: arxiv:2510.26503
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: The sustainability of contribution norms with income dynamics
url_abs: http://arxiv.org/abs/2510.26503v1
url_html: https://arxiv.org/html/2510.26503v1
venue: arXiv q-fin
version: 1
year: 2025
---


Pau Juan-Bartroli111This manuscript was previously distributed as Social Mobility and Long-Run Cooperation. For comments and discussions in either version of the manuscript, we thank Ingela Alger, Alae Baha, Astrid Hopfensitz, Gerard Maideu-Morera, Sébastien Pouget, Jaume Ventura, and Takuro Yamashita. We acknowledge funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 789111 - ERC EvolvingEconomics).
  
Toulouse School of Economics
  
Esteban Muñoz-Sobrado
  
Universitat Rovira i Virgili

(\monthyearformatOctober 30, 2025)

###### Abstract

The sustainability of cooperation is crucial for understanding the progress of societies. We study a repeated game in which individuals decide the share of their income to transfer to other group members. A central feature of our model is that individuals may, with some probability, switch incomes across periods—our measure of income mobility—while the overall income distribution remains constant over time. We analyze how income mobility and income inequality affect the sustainability of contribution norms—informal agreements about how much each member should transfer to the group. We find that greater income mobility facilitates cooperation. In contrast, the effect of inequality is ambiguous and depends on the progressivity of the contribution norm and the degree of mobility. We apply our framework to an optimal taxation problem to examine the interaction between public and private redistribution.

## 1 Introduction

Income inequality and income mobility jointly shape incentives for cooperation.222Given that we keep the income distribution constant, income mobility is interpreted as relative income mobility: changes in the relative positions of individuals within the income distribution over time (Shorrocks, [1978a](https://arxiv.org/html/2510.26503v1#bib.bib48)). This is particularly relevant in the intragenerational context, where mobility is viewed as movement within a fixed income structure rather than across generations (Jäntti and
Jenkins, [2015](https://arxiv.org/html/2510.26503v1#bib.bib33)). While inequality provides a snapshot of the income distribution, mobility reflects the potential for individuals to change their income over time. Milton Friedman famously noted that the importance of inequality depends on whether it reflects temporary differences or entrenched long-run status: “*A major problem in interpreting evidence on the distribution of income is the need to distinguish between two basically different kinds of income inequality: temporary, short-run differences in income, and differences in long-run income status*” (Friedman, [1962](https://arxiv.org/html/2510.26503v1#bib.bib30), p. 171).
This quote emphasizes the instrumental role of mobility in shaping the normative interpretation of inequality.
Despite the importance of income mobility, it is rarely incorporated into theoretical models of cooperation. This omission can lead to misleading predictions: the same level of inequality may foster or hinder cooperation depending on how likely individuals are to change their income over time.

This paper examines how the interaction between inequality and mobility affects cooperation in repeated interactions. To investigate this interaction, we develop a tractable theoretical framework that captures the interplay between income inequality, income mobility, and contribution norms. The model features three key parameters: a mobility parameter that governs the likelihood of individuals changing their income over time, an inequality parameter that determines the dispersion between individuals’ incomes, and a progressivity parameter that characterizes the shape of the contribution norm—how society dictates transfers should vary with income. This parsimonious structure allows us to isolate each component’s effect and analyze how their interaction influences the sustainability of cooperation. While previous work has emphasized that income mobility is instrumentally valuable because it reduces long-term inequality (Jäntti and
Jenkins, [2015](https://arxiv.org/html/2510.26503v1#bib.bib33)), our contribution is to show that mobility also plays a critical role in sustaining cooperation.

#### Setting

The simplest version of the model consists of an organization with two individuals who differ in their incomes. They play an infinitely repeated stochastic game where, in each period, they decide what share of their income to transfer to the organization, which equally distributes transfers among its members. This stage game is infinitely repeated, and individuals maximize the discounted sum of their utility, given complete information about the history of contributions. Contributing to the organization is individually costly—any amount transferred reduces one’s material payoff—but aggregate utility is maximized when both individuals transfer their entire income to the organization.
Although individuals are solely concerned with their material payoffs, even high-income individuals may have incentives to contribute to the organization, as their prospect of becoming low-income in the future makes the benefits of redistribution valuable to them over time.

Our model has three key features. First, with some probability, individuals switch roles: the rich individual becomes poor, and the poor individual becomes rich. We model income mobility as a homogeneous Markov process over the set of individual rankings, where each state represents a specific ordering of individuals by income. This transition is governed by a parameter m∈[0,1]m\in[0,1], which captures the degree of income mobility within the organization. When m=0m=0, the individuals remain in the same role in all periods; the organization has no income mobility. When m=1m=1, the individuals have the same probability of moving to either role; the organization has full income mobility. More generally, higher values of mm correspond to a greater probability of switching roles and, thus, greater income mobility within the organization. This approach aligns with standard stochastic models of income dynamics while allowing us to embed mobility into a repeated-game framework where strategic cooperation is endogenous.

Second, the organization’s income distribution remains constant over time. Although individuals may change their income level, the organization’s total income and income levels are fixed.
To measure income inequality, we use the Atkinson index in which a parameter α≥0\alpha\geq 0 governs income inequality (Atkinson, [1970](https://arxiv.org/html/2510.26503v1#bib.bib8)). When α=0\alpha=0, all income types receive the same share of the endowment; the organization has full income equality. When α→∞\alpha\to\infty, all income becomes concentrated in the highest income type; the organization has full income inequality. More generally, the higher α\alpha, the higher the inequality within the organization.

Third, the organization’s members have an informal shared agreement on the transfers individuals should make to the organization given their income, referred to as the contribution norm (Reuben and
Riedl, [2013](https://arxiv.org/html/2510.26503v1#bib.bib44)). This agreement can be interpreted as a social norm of behavior that dictates how people should behave in society (Bicchieri, [2008](https://arxiv.org/html/2510.26503v1#bib.bib13); Burke and
Young, [2011](https://arxiv.org/html/2510.26503v1#bib.bib17)). We consider a set of norms parametrized by a parameter β≥0\beta\geq 0 that governs the progressivity of the agreement. When β∈(0,1)\beta\in(0,1), the rule is regressive: rich individuals contribute more in absolute terms but less in relative terms. When β>1\beta>1, the rule is progressive: rich individuals contribute more in absolute and relative terms.

In this paper, instead of focusing on characterizing the set of Subgame Perfect Nash Equilibria (SPNE), we focus on characterizing the lowest discount factor δ¯\underline{\delta} such that the outcome in which all individuals follow the contribution norm is an SPNE. As is standard in repeated games, our analysis concentrates on the efficient cooperative equilibrium among the set of sustainable outcomes, rather than characterizing the entire equilibrium set.

In our context this can also be justified for three reasons. First, this outcome is normatively appealing: it represents the outcome in which all individuals follow the group’s agreement, aligning with the government’s perspective or the community norms (Caplin and
Schotter, [2008](https://arxiv.org/html/2510.26503v1#bib.bib18); Dold
et al., [2018](https://arxiv.org/html/2510.26503v1#bib.bib24)).
Second, cooperative outcomes are commonly observed in empirical settings involving informal redistribution, such as risk-sharing arrangements in villages or among co-workers (Dercon, [2005](https://arxiv.org/html/2510.26503v1#bib.bib22); Dubois
et al., [2008](https://arxiv.org/html/2510.26503v1#bib.bib25); Mobarak and
Rosenzweig, [2013](https://arxiv.org/html/2510.26503v1#bib.bib40)).
Third, focusing on a unique outcome allows for transparent comparative static analysis, which would be challenging with the set of SPNE.

#### Results

We show three main results. First, as long as the organization has a positive degree of income mobility, the contribution norm can be sustained if individuals are sufficiently patient. This result is important as cooperation is never sustainable when m=0m=0. Hence, cooperation is discontinuous when changing from zero to positive mobility.
More generally, income mobility facilitates cooperation among its members for any level of income inequality and progressivity of the contribution norm.333More formally, the lowest discount factor δ¯\underline{\delta} such that the cooperative outcome is an SPNE is decreasing on mm for any α>0\alpha>0 and β≥0\beta\geq 0. Intuitively, income mobility enhances high-income individuals’ incentives to cooperate, as it raises the probability that they might eventually become low-income, benefiting from the contribution norm. This prospect strengthens the value of cooperation as a form of intertemporal insurance, encouraging individuals to contribute even when they are currently better off.

Second, inequality has an ambiguous effect on cooperation, which crucially depends on the degree of progressivity of the contribution norm. When contribution norms are regressive, higher inequality has a positive effect on cooperation. On the other hand, when contribution norms are progressive, the relationship between inequality and cooperation is non-monotonic, especially when income mobility is low. Intuitively, when contribution norms are regressive, higher inequality makes it less costly for the rich to comply, strengthening cooperation. In contrast, with progressive norms, increasing inequality places a greater burden on the rich, which can discourage compliance, especially when the rich expect to remain in that position in the future.

Finally, we examine which contribution norms are most conducive to sustaining cooperation in the long run. For each level of inequality and mobility, we identify the rule that makes cooperation easiest to sustain, that is, the one requiring the least patience from individuals. This provides an efficiency benchmark that summarizes how the optimal degree of progressivity varies with inequality and mobility.444This efficiency criterion can also be interpreted as the outcome of a long-run evolutionary process in which norms that better sustain cooperation are more likely to persist or be imitated; see Witt ([1993](https://arxiv.org/html/2510.26503v1#bib.bib53)), Safarzyńska and van den Bergh ([2010](https://arxiv.org/html/2510.26503v1#bib.bib45)), Alger and
Weibull ([2007](https://arxiv.org/html/2510.26503v1#bib.bib5), [2010](https://arxiv.org/html/2510.26503v1#bib.bib6)), Alger ([2025](https://arxiv.org/html/2510.26503v1#bib.bib4)).

We characterize how the optimal norm depends on inequality and mobility. A central finding is that the selected norm can be either progressive or regressive, depending on the environment.
More generally, as inequality rises, the optimal norm initially becomes more progressive but eventually becomes less progressive beyond a critical level of inequality. In contrast, higher mobility consistently reduces the optimal degree of progressivity, as individuals are more likely to move across income ranks.

#### Application

We extend the model to study the interaction between private and public redistribution (Alesina and
Angeletos, [2005](https://arxiv.org/html/2510.26503v1#bib.bib3); Krueger and
Perri, [2011](https://arxiv.org/html/2510.26503v1#bib.bib36)). Specifically, we add a policy stage in which a benevolent utilitarian government sets a proportional income tax before individuals engage in voluntary transfers. The government collects taxes and redistributes a fraction of the revenue equally among group members. After taxation, individuals decide how much of their disposable income to voluntarily transfer to others. We analyze how the optimal tax rate depends on income inequality and mobility, and how it interacts with the prevailing contribution norms.

The analysis establishes a regime-dependent relationship between public and private redistribution. When voluntary cooperation cannot be sustained for any tax rate, the government is the sole provider of redistribution, and the optimal tax rate increases with income inequality. When voluntary cooperation is sustainable, voluntary transfers reduce the need for public redistribution. In this case, the welfare-maximising tax rate decreases with inequality, income mobility, and the progressivity of the contribution norm. These results indicate that public and private redistribution are substitutes and that the design of tax policy depends on the incentive compatibility of private cooperation. Ignoring endogenous cooperation can lead to different policy prescriptions, especially in settings with high mobility or well-defined informal norms. This complements previous work on the political economy of redistribution, which typically assumes either public or private transfers as exogenous (e.g., Alesina and
Angeletos, [2005](https://arxiv.org/html/2510.26503v1#bib.bib3), Benabou and
Ok, [2001](https://arxiv.org/html/2510.26503v1#bib.bib12)).

#### Related Literature

This paper relates to several strands of literature on income mobility, redistribution, and informal cooperation. Empirical studies document substantial variation in income mobility across space and time (Chetty et al., [2014](https://arxiv.org/html/2510.26503v1#bib.bib20), [2017](https://arxiv.org/html/2510.26503v1#bib.bib19), Deutscher and
Mazumder, [2023](https://arxiv.org/html/2510.26503v1#bib.bib23)). In the United States, relative mobility has remained stable, but rising inequality has magnified the consequences of the birth lottery (Chetty et al., [2014](https://arxiv.org/html/2510.26503v1#bib.bib20)).
Different mobility metrics can also yield different policy implications (Deutscher and
Mazumder, [2023](https://arxiv.org/html/2510.26503v1#bib.bib23)), underscoring the importance of mobility as both an outcome and a determinant of expectations.555For a broader review of the link between inequality and mobility, see Durlauf
et al. ([2022](https://arxiv.org/html/2510.26503v1#bib.bib26)). For comprehensive overviews of mobility concepts, measurement, and trends, see Fields and
Ok ([1999](https://arxiv.org/html/2510.26503v1#bib.bib29)) and Jäntti and
Jenkins ([2015](https://arxiv.org/html/2510.26503v1#bib.bib33)).

Theoretically, models such as Benabou and
Ok ([2001](https://arxiv.org/html/2510.26503v1#bib.bib12)) and Acemoglu
et al. ([2018](https://arxiv.org/html/2510.26503v1#bib.bib1)) formalize mobility using Markovian income and status transitions, respectively. Our framework differs from these studies by focusing on intra-personal (rather than intergenerational or group-based) mobility, allowing for downward income transitions and abstracting from dynastic preferences. We examine how such individual income dynamics affect the sustainability of redistribution through voluntary transfers, holding group structure and intergenerational links constant.

Our analysis also builds on the literature on informal risk-sharing under limited commitment (Thomas and
Worrall, [1988](https://arxiv.org/html/2510.26503v1#bib.bib51), Kocherlakota, [1996](https://arxiv.org/html/2510.26503v1#bib.bib34)). In these settings, cooperation is sustained by future punishment threats, and efficient allocations are constrained by enforceability. We depart from this work by considering an environment with N≥2N\geq 2 individuals and introducing income mobility as a central parameter. This allows us to isolate how dynamic risk exposure interacts with cooperation incentives in group settings in which individuals may use social norms to coordinate and insure themselves against negative income shocks.

#### Outline

The remainder of the paper is organized as follows. In Section [2](https://arxiv.org/html/2510.26503v1#S2 "2 Theoretical model ‣ The sustainability of contribution norms with income dynamics"), we present the theoretical framework. In Section [3](https://arxiv.org/html/2510.26503v1#S3 "3 General solution ‣ The sustainability of contribution norms with income dynamics"), we characterize the general solution. In Section [4](https://arxiv.org/html/2510.26503v1#S4 "4 The effect of income mobility and income inequality ‣ The sustainability of contribution norms with income dynamics"), we conduct several comparative statics. In Section [5](https://arxiv.org/html/2510.26503v1#S5 "5 Application: Government’s Optimal Taxation ‣ The sustainability of contribution norms with income dynamics"), we apply our framework to an optimal taxation problem. In Section [6](https://arxiv.org/html/2510.26503v1#S6 "6 Conclusions ‣ The sustainability of contribution norms with income dynamics"), we conclude. All mathematical proofs are in Appendix [A](https://arxiv.org/html/2510.26503v1#A1 "Appendix A Appendix A: Mathematical Proofs ‣ The sustainability of contribution norms with income dynamics").

## 2 Theoretical model

### 2.1 Stochastic game

To model repeated cooperation, we consider an infinitely repeated stochastic game; a generalization of infinitely repeated games.666Stochastic games were introduced in Shapley ([1953](https://arxiv.org/html/2510.26503v1#bib.bib47)). For detailed discussions, see Neyman and
Sorin ([2003](https://arxiv.org/html/2510.26503v1#bib.bib41)), Amir ([2003](https://arxiv.org/html/2510.26503v1#bib.bib7)), and Solan and
Vieille ([2015](https://arxiv.org/html/2510.26503v1#bib.bib50)). Stochastic games have been used mainly in resource-extraction problems (Levhari
et al., [1980](https://arxiv.org/html/2510.26503v1#bib.bib37)) but also in industrial organization (Ericson and
Pakes, [1995](https://arxiv.org/html/2510.26503v1#bib.bib27)) and inspection problems (Baston and
Bostock, [1991](https://arxiv.org/html/2510.26503v1#bib.bib9); Darlington et al., [2023](https://arxiv.org/html/2510.26503v1#bib.bib21)). In stochastic games the stage game may change over time due to players’ behavior and chance. In our setting, we consider a stochastic game with (i) a finite set of states, (ii) a finite number of players, (iii) a common action set, (iv) a transition probability matrix that only depends on chance, and (v) perfect monitoring. More formally, the game is a tuple (S,N,A,P,Π)(S,N,A,P,\Pi), where:

* •

  SS is a finite set of states.
* •

  NN is a finite number of players.
* •

  A=A1×…×AnA=A\_{1}\times...\times A\_{n} is the action set.
* •

  P:S×S→[0,1]P:S\times S\rightarrow[0,1] is a transition probability function.
* •

  Π=π1×π2×…×πn\Pi=\pi\_{1}\times\pi\_{2}\times...\times\pi\_{n} is the payoff function set.

In our application, the states represent the income rankings of the players, while the transition probability function PP represents the probability of moving to any state at t+1t+1 given the state in period tt.

### 2.2 Stage game

Each stage game is composed of N≥2N\geq 2 players who differ in which of the NN positions they have been assigned. Each position is allocated a deterministic income w1>…>wN>0w\_{1}>...>w\_{N}>0. Thus, the player assigned to position ii receives an income of wiw\_{i}. There is a total of N!N! states, each representing an income rank in the organization. After players learn their positions, they decide the share of their income to transfer to the organization. The total amount transferred is equally shared among the group members.
The amount transferred by player i∈{1,…,N}i\in\{1,...,N\} in position k∈{1,…,N}k\in\{1,...,N\}, in period t∈{1,2,…}t\in\{1,2,...\} is denoted by xi,kt∈[0,1]{x\_{i,k}^{t}}\in[0,1].

Players’ material payoff in the stage game depends on players’ choices and their incomes. For simplicity, we assume that in the first period, individual ii is allocated to position ii, and refer to xi,i1{x\_{i,i}^{1}} as xi1{x\_{i}^{1}}. In that case, player ii’s material payoff at t=1t=1 is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | πi​(xi1;x−i1)=wi​(1−xi1)+1N​∑j=1Nxj1​wj,\pi\_{i}({x\_{i}^{1}};{x\_{-i}^{1}})=w\_{i}(1-x\_{i}^{1})+\frac{1}{N}\sum\_{j=1}^{N}x\_{j}^{1}\ w\_{j}, |  | (1) |

where x−i1{x\_{-i}^{1}} refers to the strategy profile of all players except ii.
Players evaluate their material payoff with an increasing and strictly concave function uu (i.e., u′>0u^{\prime}>0 and u′′<0u^{\prime\prime}<0). Thus, players decrease their utility when transferring money to the organization, but having all players doing so is socially efficient.777This formulation is equivalent to assuming that players evaluate their monetary payoffs with a linear function u​(x)=xu(x)=x and that contributions to the organization are multiplied by a parameter γ>1\gamma>1, as in linear public goods games (Zelmer, [2003](https://arxiv.org/html/2510.26503v1#bib.bib55)).

### 2.3 Income mobility

We model income mobility as a homogeneous Markov process over the set of states. The transition matrix specifies the probability of moving from one state to another across periods, assuming that transitions are governed by chance and not by individual actions. The model satisfies three standard assumptions from the mobility literature: (i) the Markov property—transitions depend only on the current state and not on prior history (McFarland, [1970](https://arxiv.org/html/2510.26503v1#bib.bib39)); (ii) time-homogeneity—transition probabilities are constant over time (Shorrocks, [1978b](https://arxiv.org/html/2510.26503v1#bib.bib49)); and (iii) exogeneity—mobility arises independently of individuals’ behavior, reflecting institutional or environmental randomness (Prais, [1955](https://arxiv.org/html/2510.26503v1#bib.bib42), Fields and
Ok, [1999](https://arxiv.org/html/2510.26503v1#bib.bib29)).

The degree of mobility is governed by a single parameter m∈[0,1]m\in[0,1], with m=0m=0 representing full persistence (identity matrix) and m=1m=1 corresponding to maximal mobility (uniform transitions across permissible states). Our formulation maintains a fixed income distribution across periods and captures pure exchange mobility through probabilistic re-rankings. This structure aligns with the literature on transition matrices while enabling us to embed mobility into a repeated-game framework with strategic interactions. When N=2N=2, we consider the following transition matrix:

|  |  |  |
| --- | --- | --- |
|  | si​jsj​isi​j( 1−12​m12​m) sj​i12​m1−12​m\bordermatrix{\penalty 10000\ &s\_{ij}&s\_{ji}\cr s\_{ij}&1-\frac{1}{2}m&\frac{1}{2}m\cr s\_{ji}&\frac{1}{2}m&1-\frac{1}{2}m} |  |

where si​js\_{ij} represents the state where player ii and jj are in the first and second position, respectively.888The income distribution is constant across periods and states. That is, there is always a player with a high and one with a low income. The rows of the matrix represent the state at period tt, and the columns represent the state at t+1t+1. Each cell represents the probability of moving from a given state at tt to a given state at t+1t+1. The parameter m∈[0,1]m\in[0,1] represents the degree of income mobility. When m=0m=0, the organization has no income mobility (i.e., players remain in the same position with certainty). When m=1m=1, there is full income mobility (i.e., each player moves to any position with equal probability). More generally, the larger mm, the more likely players are to switch positions.

When N>2N>2, we define S′​(s)⊂SS^{\prime}(s)\subset S to be the set of states such that there is no player in the same position as in s∈Ss\in S.999For example, when s=si​j​ks=s\_{ijk}, S′​(si​j​k)={sj​k​i,sk​i​j}S^{\prime}({s\_{ijk}})=\{s\_{jki},s\_{kij}\}. We consider the following transition matrix:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μs,s′={1−N−1N​m if ​s=s′,1N​m if ​s′∈S′​(s),0 otherwise.\mu\_{s,s^{\prime}}=\begin{cases}1-\frac{N-1}{N}m\hskip 17.07182pt\text{ if }s=s^{\prime},&\\[0.0pt] \frac{1}{N}m\hskip 48.36958pt\text{ if }s^{\prime}\in S^{\prime}(s),&\\[5.69046pt] 0\hskip 62.59596pt\text{ otherwise}.&\\[5.69046pt] \end{cases} |  | (2) |

Here, μs,s′\mu\_{s,s^{\prime}} denotes the probability of moving from state ss at period tt to state s′s^{\prime} at period t+1t+1. The transition probability matrix is constructed then by computing μs,s′\mu\_{s,s^{\prime}} for each pair of states.
With the proposed transition matrix, each player has a probability of 1−N−1N​m1-\frac{N-1}{N}m to remain in the same position, and a probability of 1N​m\frac{1}{N}m to move to a different one. When N=3N=3, the transition matrix is given by

|  |  |  |
| --- | --- | --- |
|  | si​j​ksi​k​jsj​i​ksj​k​isk​i​jsk​j​isi​j​k( 1−23​m0013​m13​m0) si​k​j01−23​m13​m0013​msj​i​k013​m1−23​m0013​msj​k​i13​m001−23​m13​m0sk​i​j13​m0013​m1−23​m0sk​j​i013​m13​m001−23​m\bordermatrix{\text{}&s\_{ijk}&s\_{ikj}&s\_{jik}&s\_{jki}&s\_{kij}&s\_{kji}\cr s\_{ijk}&1-\frac{2}{3}m&0&0&\frac{1}{3}m&\frac{1}{3}m&0\cr s\_{ikj}&0&1-\frac{2}{3}m&\frac{1}{3}m&0&0&\frac{1}{3}m\cr s\_{jik}&0&\frac{1}{3}m&1-\frac{2}{3}m&0&0&\frac{1}{3}m\cr s\_{jki}&\frac{1}{3}m&0&0&1-\frac{2}{3}m&\frac{1}{3}m&0\cr s\_{kij}&\frac{1}{3}m&0&0&\frac{1}{3}m&1-\frac{2}{3}m&0\cr s\_{kji}&0&\frac{1}{3}m&\frac{1}{3}m&0&0&1-\frac{2}{3}m\cr} |  |

As before, when m=0m=0, players remain in the same position with certainty, while when m=1m=1, they have the same probability to move to any position.101010Our mobility parameter mm can be interpreted analogously to a class of mobility indices, such as the Prais index (Prais, [1955](https://arxiv.org/html/2510.26503v1#bib.bib42)). In our setting, applying the Prais index to the transition matrix yields Prais​(P)=mN−1\text{Prais}(P)=\frac{m}{N-1}.
This aligns with our interpretation of mm as the degree of income mobility. While we do not propose a new index, our framework embeds this parametric measure of mobility directly into a repeated-game structure.

Despite its simplicity, the transition matrix is in line with the definition of relative social mobility proposed in Behrman
et al. ([2000](https://arxiv.org/html/2510.26503v1#bib.bib11)): “*Holding total income and income distribution constant, after all, relative social mobility is greater if wealthier people more frequently change places with poorer people than if such exchanges occur less frequently*” (p. 74).111111A limitation of our transition matrix is that moving across positions does not depend on the distance between them. For example, in the N=3N=3 case, the players in the second and third income rank have the same probability of moving to the first income rank. Accounting for this would require a more complex transition matrix with additional parameters, complicating the analysis.

### 2.4 Income inequality

Following the Atkinson index (Atkinson, [1970](https://arxiv.org/html/2510.26503v1#bib.bib8)),
we define each income level as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi​(α)=exp⁡(α​(N−i+1))∑j=1Nexp⁡(α​(N−j+1))∈[0,1],w\_{i}(\alpha)=\frac{\exp(\alpha(N-i+1))}{\sum\_{j=1}^{N}\exp(\alpha(N-j+1))}\in[0,1], |  | (3) |

where i∈{1,2,…,N}i\in\{1,2,\dotsc,N\} is the index of the income type, and α≥0\alpha\geq 0 is a parameter that governs the degree of inequality. For any α≥0\alpha\geq 0, the total income is normalized to 1, ∑i=1Nwi​(α)=1\sum\_{i=1}^{N}w\_{i}(\alpha)=1.

When α=0\alpha=0, there is full income equality, with wi=1Nw\_{i}=\frac{1}{N} for any i∈{1,…,N}i\in\{1,...,N\}. As α\alpha increases, higher income types are allocated progressively larger shares, thereby increasing income inequality. In the limit, as α→∞\alpha\to\infty, there is full income inequality, with w1=1w\_{1}=1 and wi=0w\_{i}=0 for any i∈{2,…,N}i\in\{2,...,N\}. Thus, higher values of α\alpha are associated with greater income inequality within the organization.

### 2.5 Types of sharing rules

We study the sustainability of sharing rules in which players’ contributions to the organization may be a function of their income level. More concretely, we focus on the parametrization where the share contributed by an player with income wiw\_{i} is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ​(wi)=wiβ∈[0,1],\theta(w\_{i})=w\_{i}^{\beta}\in[0,1], |  | (4) |

where β≥0\beta\geq 0 determines the degree of progressivity of the sharing rule.121212Since wiw\_{i} is between 0 and 11, θ​(wi)\theta(w\_{i}) is also between 0 and 11, consistent with interpreting θ​(wi)\theta(w\_{i}) as the share of income one should transfer. When β=0\beta=0, all players should contribute all their endowment. If 0<β<10<\beta<1, the contribution rule is regressive: high-income players should contribute more in absolute terms, but less in relative terms. When β=1\beta=1, contributions are exactly proportional to income. When β>1\beta>1, the contribution rule is progressive: higher-income players should contribute more than proportionally.

In our main analysis, we consider contribution norms as (exogenous) parameters that societies are endowed with. That is, rather than deriving these norms from individual optimization, we take them as given and explore how income mobility and income inequality affect their sustainability.131313In Section [4.3](https://arxiv.org/html/2510.26503v1#S4.SS3 "4.3 Long-term norm selection ‣ 4 The effect of income mobility and income inequality ‣ The sustainability of contribution norms with income dynamics"), we endogenize contribution norms with evolutionary foundations. We motivate this with the findings of Reuben and
Riedl ([2013](https://arxiv.org/html/2510.26503v1#bib.bib44)), who document, in a public goods game experiment with heterogeneous endowments, that income heterogeneity gives rise to “*a plurality of normatively appealing rules of behavior that are potential candidates for emerging contribution norms*" (p. 15).

### 2.6 Visual representation when N=2N=2

Figure 1 displays a visual representation of the game when N=2N=2. In this case, each period has two possible states depending on the income ranks assigned to players ii and jj. At t=1t=1, the game starts in state si,js\_{i,j} or sj,is\_{j,i}. Players ii and jj simultaneously choose the share of their income to transfer to the organization. Both players observe the transfers, and their monetary payoffs are determined according to equation [1](https://arxiv.org/html/2510.26503v1#S2.E1 "In 2.2 Stage game ‣ 2 Theoretical model ‣ The sustainability of contribution norms with income dynamics"). At t=2t=2, with probability 1−12​m1-\frac{1}{2}m, the players remain in the same position, and with probability 12​m\frac{1}{2}m, they switch positions. Players observe the realized state and choose their transfers. This process continues indefinitely.

![Refer to caption](Images/ImageGame.png)


Figure 1: Visual representation of the N=2N=2 game.

### 2.7 Notation and Equilibrium Concept

We now describe the main components of the game when N=2N=2.141414The notation easily generalizes to the case with N>2N>2. Let st∈{si,j,sj,i}s^{t}\in\{s\_{i,j},s\_{j,i}\} denote the state realized in period tt, and let st=(s1,s2,…,st)∈Sts^{t}=(s^{1},s^{2},\dots,s^{t})\in S^{t} denote the history of states up to period tt. Correspondingly, let xt​(st)x\_{t}(s^{t}) denote the profile of contributions made in period tt given sts^{t}. For instance, if st=si,js^{t}=s\_{i,j}, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | xt​(si,j)={xi,1t,xj,2t},x\_{t}(s\_{i,j})=\{x\_{i,1}^{t},x\_{j,2}^{t}\}, |  | (5) |

where xi,1t∈[0,1]x\_{i,1}^{t}\in[0,1] is the share of income that player ii contributes while occupying the first position. Let xt=(x1​(s1),x2​(s2),…,xt​(st))x^{t}=(x\_{1}(s^{1}),x\_{2}(s^{2}),\dots,x\_{t}(s^{t})) denote the full history of observed contributions and states up to period tt. A strategy for player ii is a mapping that assigns a contribution level given the full public history xt−1x^{t-1} and the current state sts^{t}. Formally,

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi,kt:xt−1×st→[0,1],x\_{i,k}^{t}:x^{t-1}\times s^{t}\rightarrow[0,1], |  | (6) |

where k∈{1,2}k\in\{1,2\} denotes the position occupied by player ii in state sts^{t}. Players share a common discount factor δ∈[0,1)\delta\in[0,1) and maximize their expected discounted sum of utility over an infinite horizon. The equilibrium concept is Subgame Perfect Nash Equilibrium (SPNE). A strategy profile {xi∗,xj∗}\{x\_{i}^{\*},x\_{j}^{\*}\} is an SPNE if, at every history (xt−1,st)(x^{t-1},s^{t}), the continuation strategies form a Nash equilibrium of the subgame starting at that point. That is, for each player ii,

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi∗∈arg⁡maxx^i⁡Ui​(x^i,xj∗∣xt−1,st),x\_{i}^{\*}\in\arg\max\_{\hat{x}\_{i}}U\_{i}(\hat{x}\_{i},x\_{j}^{\*}\mid x^{t-1},s^{t}), |  | (7) |

where UiU\_{i} denotes player ii’s expected discounted utility from period tt onward.

## 3 General solution

We characterize the conditions under which cooperation can be sustained in all periods. We define the cooperative strategy as the strategy in which the player follows the contribution norm as long as others also do so. For player ii, the cooperative strategy is defined as follows:

* •

  At t=1t=1, select xi1=wiβx\_{i}^{1}=w\_{i}^{\beta}.
* •

  For t>1t>1:
  If in all previous periods τ<t\tau<t, each player j∈{1,…,N}j\in\{1,\dots,N\} has selected xj,kτ=wkβx\_{j,k}^{\tau}=w\_{k}^{\beta} for their respective position kk, then choose xi,kt=wkβx\_{i,k}^{t}=w\_{k}^{\beta}.
  Otherwise, select xi,kt=0x\_{i,k}^{t}=0.

The cooperative outcome corresponds to the outcome in which all players follow the cooperative strategy.
To determine when the cooperative outcome constitutes a SPNE, we compare the discounted expected payoff of cooperation with that of deviation.
We focus on the most profitable one-shot deviation: contributing zero in the first period.

We denote by VicV\_{i}^{c}, VidV\_{i}^{d}, and ViaV\_{i}^{a}, player ii’s expected discounted payoffs from cooperation, deviation, and autarky, respectively. Under the cooperative outcome, each player contributes according to the rule θ​(wi)=wiβ\theta(w\_{i})=w\_{i}^{\beta} in every period. The value of cooperation is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vic=u​(wic)+δ​[(1−N−1N​m)​Vic+mN​∑j≠iVjc],V\_{i}^{c}=u(w\_{i}^{c})+\delta\left[\left(1-\frac{N-1}{N}m\right)V\_{i}^{c}+\frac{m}{N}\sum\_{j\neq i}V\_{j}^{c}\right], |  | (8) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | wic=[1−θ​(wi)]​wi+1N​∑j=1Nθ​(wj)​wj.w\_{i}^{c}=[1-\theta(w\_{i})]w\_{i}+\frac{1}{N}\sum\_{j=1}^{N}\theta(w\_{j})w\_{j}. |  | (9) |

The first term of equation [9](https://arxiv.org/html/2510.26503v1#S3.E9 "In 3 General solution ‣ The sustainability of contribution norms with income dynamics") corresponds to the income kept after contributing θ​(wi)​wi\theta(w\_{i})w\_{i}, while the second term reflects the equally shared benefit from the public good.
The value of deviation is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vid=u​(wi+1N​∑j≠iθ​(wj)​wj)+δ​[(1−N−1N​m)​Via+mN​∑j≠iVja].V\_{i}^{d}=u\left(w\_{i}+\frac{1}{N}\sum\_{j\neq i}\theta(w\_{j})w\_{j}\right)+\delta\left[\left(1-\frac{N-1}{N}m\right)V\_{i}^{a}+\frac{m}{N}\sum\_{j\neq i}V\_{j}^{a}\right]. |  | (10) |

The first term of equation [10](https://arxiv.org/html/2510.26503v1#S3.E10 "In 3 General solution ‣ The sustainability of contribution norms with income dynamics") represents the one-shot gain from not contributing, while
the second term represents the discounted continuation value under autarky, in which all players revert permanently to the non-cooperative outcome, defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Via=u​(wi)+δ​[(1−N−1N​m)​Via+mN​∑j≠iVja].V\_{i}^{a}=u(w\_{i})+\delta\left[\left(1-\frac{N-1}{N}m\right)V\_{i}^{a}+\frac{m}{N}\sum\_{j\neq i}V\_{j}^{a}\right]. |  | (11) |

In Appendix [A](https://arxiv.org/html/2510.26503v1#A1 "Appendix A Appendix A: Mathematical Proofs ‣ The sustainability of contribution norms with income dynamics"), we derive closed-form expressions for VicV\_{i}^{c}, VidV\_{i}^{d}, and ViaV\_{i}^{a} as functions of the model’s primitives. Lemma [1](https://arxiv.org/html/2510.26503v1#Thmtheorem1 "Lemma 1 (Comparative statics for type 𝑖=1). ‣ 3 General solution ‣ The sustainability of contribution norms with income dynamics") characterizes how the first-type player’s values of cooperation and deviation, V1cV\_{1}^{c} and V1dV\_{1}^{d}, change with mm and α\alpha.

###### Lemma 1 (Comparative statics for type i=1i=1).

Let V1cV\_{1}^{c} and V1dV\_{1}^{d} denote the cooperative and deviation payoffs for the richest type. Then, there exists a threshold function m​(β)>0m(\beta)>0 such that:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∂V1c∂m\displaystyle\frac{\partial V\_{1}^{c}}{\partial m} | ={0if ​β=0,<0if ​β>0,\displaystyle=\begin{cases}0&\text{if }\beta=0,\\ <0&\text{if }\beta>0,\end{cases} | ∂V1d∂m\displaystyle\qquad\frac{\partial V\_{1}^{d}}{\partial m} | <0,\displaystyle<0, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∂V1c∂α\displaystyle\frac{\partial V\_{1}^{c}}{\partial\alpha} | ={0if ​β=0,<0if ​β>0,\displaystyle=\begin{cases}0&\text{if }\beta=0,\\ <0&\text{if }\beta>0,\end{cases} | ∂V1d∂α\displaystyle\qquad\frac{\partial V\_{1}^{d}}{\partial\alpha} | ={0if ​β=0,<0if ​β∈(0,m​(β)),>0if ​β>m​(β).\displaystyle=\begin{cases}0&\text{if }\beta=0,\\ <0&\text{if }\beta\in(0,m(\beta)),\\ >0&\text{if }\beta>m(\beta).\end{cases} |  |

Lemma [1](https://arxiv.org/html/2510.26503v1#Thmtheorem1 "Lemma 1 (Comparative statics for type 𝑖=1). ‣ 3 General solution ‣ The sustainability of contribution norms with income dynamics") characterizes how the value of cooperation and the value of deviation for the richest player changes with income mobility (mm) and income inequality (α\alpha). When β=0\beta=0, all individuals contribute the same share of their income regardless of their type, and changes in mm and α\alpha do not affect the richest player’s value from cooperation. When β>0\beta>0, an increase in mobility reduces both the value of cooperation and the value of deviation, as it raises uncertainty about future positions and weakens the link between present actions and future benefits. The effect of inequality on the deviation value is non-monotonic: for low values of β\beta, rising inequality discourages deviation, but when β\beta is high, the burden of contributing rises faster than the corresponding benefit, making deviation more attractive. This trade-off is captured by a threshold function m​(β)m(\beta), which separates the two regimes.

###### Lemma 2.

Let N≥2N\geq 2, w1>w2>⋯>wNw\_{1}>w\_{2}>\dots>w\_{N}, δ∈(0,1)\delta\in(0,1), m∈[0,1]m\in[0,1], and β≥0\beta\geq 0. Then, the value of deviation satisfies: V1d​e​v>V2d​e​v>⋯>VNd​e​vV\_{1}^{dev}>V\_{2}^{dev}>\dots>V\_{N}^{dev}.

Lemma [2](https://arxiv.org/html/2510.26503v1#Thmtheorem2 "Lemma 2. ‣ 3 General solution ‣ The sustainability of contribution norms with income dynamics") shows that richer individuals have stronger incentives to deviate from cooperation. This holds even when the value of cooperation varies across types due to redistributive norms (i.e., β>0\beta>0), because the private gains from defection and the continuation value in autarky both increase with income and outweigh the non-monotonic effects arising from cooperation under progressive norms. This observation plays a crucial role in determining whether cooperation can be sustained in equilibrium: if the richest type finds it optimal to cooperate, then all lower-income types—who face weaker incentives to defect—will also choose to cooperate. Thus, the sustainability of cooperation boils down to checking the richest’ type incentive condition. Proposition [1](https://arxiv.org/html/2510.26503v1#Thmproposition1 "Proposition 1. ‣ 3 General solution ‣ The sustainability of contribution norms with income dynamics") formalizes this insight.

###### Proposition 1.

The set of discount factors that guarantees cooperation for all individuals is given by the interval D=[δ¯,1]D=[\underline{\delta},1], where δ¯∈(0,1)\underline{\delta}\in(0,1) is the unique discount factor such that V1c=V1dV\_{1}^{c}=V\_{1}^{d}.

Proposition [1](https://arxiv.org/html/2510.26503v1#Thmproposition1 "Proposition 1. ‣ 3 General solution ‣ The sustainability of contribution norms with income dynamics") characterizes the conditions under which cooperation can be sustained in equilibrium. The result indicates that the richest individual typically faces the strongest incentive to defect. If this individual prefers to adhere to the cooperative strategy, others will follow as well. The minimum discount factor δ¯\underline{\delta} is implicitly defined by the indifference point where the richest player’s cooperative and deviation payoffs coincide. Therefore, cooperation can be sustained in equilibrium whenever δ≥δ¯\delta\geq\underline{\delta}.

## 4 The effect of income mobility and income inequality

In this section we study how does δ¯\underline{\delta} vary with mm and α\alpha.

### 4.1 The role of income mobility

Lemma [3](https://arxiv.org/html/2510.26503v1#Thmtheorem3 "Lemma 3. ‣ 4.1 The role of income mobility ‣ 4 The effect of income mobility and income inequality ‣ The sustainability of contribution norms with income dynamics") shows that increasing income mobility has a positive effect on sustaining cooperation.

###### Lemma 3.

Let δ¯\underline{\delta} denote the minimum discount factor that sustains cooperation for all individuals, as defined in Proposition [1](https://arxiv.org/html/2510.26503v1#Thmproposition1 "Proposition 1. ‣ 3 General solution ‣ The sustainability of contribution norms with income dynamics"). Then:

* (i)

  If m∈(0,1]m\in(0,1], then δ¯<1\underline{\delta}<1. If m=0m=0, then δ¯=1\underline{\delta}=1.
* (ii)

  For all m∈(0,1]m\in(0,1], then ∂δ¯∂m<0\frac{\partial\,\underline{\delta}}{\partial m}<0.

When m=0m=0, cooperation cannot be sustained for any δ<0\delta<0. Intuitively, the richest individual is certain that it will remain forever in the highest position, and therefore its autarky payoff is higher than the cooperation payoff. In this case, high-income players have nothing to lose from deviation, as they enjoy a higher utility outside the cooperative agreement.
When m>0m>0, future income becomes uncertain. This uncertainty reduces the long-run value of deviation because a rich player is more likely to transition into a lower-income position, where the value of autarky is lower. In contrast, the cooperative payoff remains relatively stable due to the smoothing effect of public good provision. Increasing mm, amplifies the gap between the relatively stable cooperative payoff and the declining deviation payoff, thereby reducing the minimum discount factor δ¯\underline{\delta} required to sustain cooperation.151515The effect is particularly strong when β=0\beta=0, where contributions are independent of income and cooperative payoffs remain constant across states. Here, mobility reduces the temptation to deviate without diminishing cooperative gains, making cooperation increasingly easier to sustain.

Figure [2](https://arxiv.org/html/2510.26503v1#S4.F2 "Figure 2 ‣ 4.1 The role of income mobility ‣ 4 The effect of income mobility and income inequality ‣ The sustainability of contribution norms with income dynamics") illustrates how δ¯\underline{\delta} varies with income mobility mm, across different levels of inequality α\alpha when β=0\beta=0.

![Refer to caption](figures/delta_vs_m_by_alpha_rho1_beta1_N3.png)


Figure 2: Minimum discount factor δ¯\underline{\delta} required for cooperation as a function of income mobility mm, for different levels of inequality α\alpha. Parameters: ρ=1\rho=1, β=1\beta=1, N=3N=3.

### 4.2 The role of income inequality

To study the effect of a permanent increase in inequality in all future periods, we distinguish between inequality at t=0t=0 and inequality in future periods t>0t>0. To do so, we fix α0≥0\alpha\_{0}\geq 0, and consider an increase to α1>α0\alpha\_{1}>\alpha\_{0} in all subsequent periods. This allows us to study an increase in future inequality, while keeping total income constant across periods, while abstracting from income effects at t=0t=0. Lemma [4](https://arxiv.org/html/2510.26503v1#Thmtheorem4 "Lemma 4. ‣ 4.2 The role of income inequality ‣ 4 The effect of income mobility and income inequality ‣ The sustainability of contribution norms with income dynamics") shows that the effect of inequality on cooperation crucially depends on β\beta and mm.

###### Lemma 4.

Let δ¯​(α1;m,β,α0)\underline{\delta}(\alpha\_{1};m,\beta,\alpha\_{0}) denote the minimum discount factor required to sustain cooperation when future inequality is α1\alpha\_{1}, inequality at t=0t=0 is α0>0\alpha\_{0}>0, income mobility is m∈(0,1]m\in(0,1], and the contribution norm’s progressivity is β≥0\beta\geq 0. Then:

* (i)

  If β≤1\beta\leq 1, then δ¯​(α1;m,β,α0)\underline{\delta}(\alpha\_{1};m,\beta,\alpha\_{0}) is weakly decreasing in α1\alpha\_{1}.
* (ii)

  If β>1\beta>1, the function δ¯​(α1;m,β,α0)\underline{\delta}(\alpha\_{1};m,\beta,\alpha\_{0}) is generally non-monotonic with a single-peaked shape.
* (iii)

  In both cases, the marginal effect of α1\alpha\_{1} on δ¯​(α1;m,β,α0)\underline{\delta}(\alpha\_{1};m,\beta,\alpha\_{0}) is decreasing in mm.

Lemma [4](https://arxiv.org/html/2510.26503v1#Thmtheorem4 "Lemma 4. ‣ 4.2 The role of income inequality ‣ 4 The effect of income mobility and income inequality ‣ The sustainability of contribution norms with income dynamics") shows that the effect of future inequality on the sustainability of cooperation depends crucially on the progressivity of the sharing norm and the degree of income mobility. When β<1\beta<1, the norm is regressive, so high-income individuals are not excessively burdened by contributions. In contrast, when β>1\beta>1, the norm is progressive placing a heavier burden on the rich. As inequality rises, so does their cost of cooperation, increasing the temptation to deviate. This initially raises the cooperation threshold δ¯\underline{\delta}. However, at high enough levels of inequality, autarky becomes less attractive: income mobility increases the chance of transitioning to a worse position, reducing the expected value of deviation. As a result, the threshold δ¯\underline{\delta} eventually declines.

This generates a single-peaked relationship between inequality and the cooperation threshold. Importantly, when β>1\beta>1, the sign of the effect of inequality on cooperation depends on the level of mobility: for low mm, inequality may increase the cooperation threshold (making cooperation harder to sustain), while for high mm, it lowers the threshold (making cooperation easier to sustain). Finally, (iii) captures the complementarity between inequality and mobility: greater mobility amplifies the stabilizing effect of inequality on cooperation, further lowering the discount factor required to sustain it.

![Refer to caption](figures/delta_vs_alpha1_by_m_rho1_beta1_alpha005_N5.png)


β=1\beta=1 (Proportional contributions)

![Refer to caption](figures/delta_vs_alpha1_by_m_rho1_beta4_alpha005_N5.png)


β=4\beta=4 (Progressive contributions)

Figure 3: Minimum discount factor δ¯\underline{\delta} required for cooperation as a function of future inequality α1\alpha\_{1}, for various levels of income mobility mm.
Parameters: ρ=1\rho=1, α0=0.5\alpha\_{0}=0.5, N=5N=5.

### 4.3 Long-term norm selection

We now study which contribution norm β\beta is most conducive to the sustainability of cooperation in the long run. Our aim is to endogenize β\beta by appealing to an evolutionary logic. Consider a population in which contribution norms are subject to selection: groups that fail to sustain cooperation are less likely to survive or be imitated, while groups that succeed in maintaining cooperation are more likely to reproduce their norm.

Formally, let δ¯​(β;α,m)\underline{\delta}(\beta;\alpha,m) denote the minimum discount factor required to sustain cooperation, given inequality α\alpha, income mobility mm, and the norm’s progressivity β\beta. Assume individuals have heterogeneous discount factors, with δi∈(0,1)\delta\_{i}\in(0,1) independently drawn from a continuous distribution F​(⋅)F(\cdot). For any given (α,m)(\alpha,m), cooperation is viable for individuals with δi≥δ¯​(β;α,m)\delta\_{i}\geq\underline{\delta}(\beta;\alpha,m). Therefore, the share of individuals who can cooperate under a given norm is given by 1−F​(δ¯​(β;α,m)).1-F\left(\underline{\delta}(\beta;\alpha,m)\right).

Selection favor the norm with the progressivity that minimize δ¯\underline{\delta}, as they maximize the probability of sustaining cooperation within the group. This motivates defining the long-run norm as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | β∗​(α,m)=arg⁡minβ≥0⁡δ¯​(β;α,m).\displaystyle\beta^{\*}(\alpha,m)=\arg\min\_{\beta\geq 0}\,\underline{\delta}(\beta;\alpha,m). |  | (12) |

Proposition [2](https://arxiv.org/html/2510.26503v1#Thmproposition2 "Proposition 2 (Long-run norm selection). ‣ 4.3 Long-term norm selection ‣ 4 The effect of income mobility and income inequality ‣ The sustainability of contribution norms with income dynamics") characterizes how β∗​(α,m)\beta^{\*}(\alpha,m) varies with inequality and mobility.161616These properties are established computationally using the method described in Figure [4](https://arxiv.org/html/2510.26503v1#S4.F4 "Figure 4 ‣ 4.3 Long-term norm selection ‣ 4 The effect of income mobility and income inequality ‣ The sustainability of contribution norms with income dynamics"), which numerically minimizes the cooperation threshold over a grid of β\beta values.

###### Proposition 2 (Long-run norm selection).

Let β∗​(α,m)=arg⁡minβ≥0⁡δ¯​(β;α,m)\beta^{\*}(\alpha,m)=\arg\min\_{\beta\geq 0}\,\underline{\delta}(\beta;\alpha,m). Then:

1. 1.

   For fixed mm, the mapping α↦β∗​(α,m)\alpha\mapsto\beta^{\*}(\alpha,m) is generally non-monotonic: it tends to increase with inequality at low levels of α\alpha, and decrease at high levels of α\alpha.
2. 2.

   For fixed α\alpha, higher mobility mm is associated with a lower optimal norm β∗​(α,m)\beta^{\*}(\alpha,m).

The selected norm β∗​(α,m)\beta^{\*}(\alpha,m) can be either progressive (β∗>1\beta^{\*}>1) or regressive (β∗<1\beta^{\*}<1), depending on the environment. When inequality is low, progressive norms are more effective at triggering cooperation by encouraging greater transfers from high earners. As inequality rises, however, overly progressive norms become harder to sustain, and regressive rules may perform better by reducing the burden on top earners. Similarly, higher mobility reduces the need for strong norm enforcement, since individuals are more willing to cooperate in anticipation of future income changes.

![Refer to caption](figures/betaEvol.png)


Figure 4: β∗​(α,m)\beta^{\*}(\alpha,m) as a function of α\alpha, for two values of mm. Each curve reports the value of β\beta that minimizes the cooperation threshold δ¯​(β;α,m)\underline{\delta}(\beta;\alpha,m), computed via a two-stage grid search with local refinement (using 1000 values for β\beta). For clarity, the resulting series is smoothed using a Savitzky–Golay filter. The dashed line marks β=1\beta=1, corresponding to a flat contribution rule. Parameters: N=6N=6, ρ=4\rho=4.

Figure [4](https://arxiv.org/html/2510.26503v1#S4.F4 "Figure 4 ‣ 4.3 Long-term norm selection ‣ 4 The effect of income mobility and income inequality ‣ The sustainability of contribution norms with income dynamics") illustrates the relationship between inequality and the optimal contribution norm for two mobility values. When inequality is low, the optimal norm rises steeply as progressive rules help enforce cooperation. However, beyond a critical point, further increases in inequality reduce the sustainability of steep norms, and β∗\beta^{\*} declines. The figure also shows that for any level of inequality, higher mobility leads to a lower optimal norm, consistent with Proposition [2](https://arxiv.org/html/2510.26503v1#Thmproposition2 "Proposition 2 (Long-run norm selection). ‣ 4.3 Long-term norm selection ‣ 4 The effect of income mobility and income inequality ‣ The sustainability of contribution norms with income dynamics").171717The function δ¯​(β;α,m)\underline{\delta}(\beta;\alpha,m) is computed numerically over a discrete grid. As a result, β∗​(α,m)\beta^{\*}(\alpha,m) may exhibit small jumps or flat regions, especially around local minima. Proposition [2](https://arxiv.org/html/2510.26503v1#Thmproposition2 "Proposition 2 (Long-run norm selection). ‣ 4.3 Long-term norm selection ‣ 4 The effect of income mobility and income inequality ‣ The sustainability of contribution norms with income dynamics") focuses on the robust qualitative patterns.

## 5 Application: Government’s Optimal Taxation

We extend the baseline model by introducing a preliminary stage in which the government sets a (time-invariant) proportional income tax. This tax is set before the repeated game of voluntary transfers begins. Players then engage in private redistribution on each period, based on their disposable (post-tax) incomes. This two-stage structure allows us to study how government taxation interacts with endogenous cooperation and to what extent public policy can facilitate—or crowd out—informal redistribution.

To analyze the government’s role, we consider a setting in which each player receives a pre-tax income wiw\_{i}, and the government levies a
proportional tax schedule:

|  |  |  |  |
| --- | --- | --- | --- |
|  | T​(wi)=τ​wi,\displaystyle T(w\_{i})=\tau w\_{i}, |  | (13) |

where τ∈[0,1]\tau\in[0,1] is the tax rate.
Post-tax consumption, after voluntary transfers and public redistribution, is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi​(θ)=yi​[1−θ​(yi)]+1N​∑jθ​(yj)​yj+1−sN​∑jT​(wj)⏟=τ.x\_{i}(\theta)=y\_{i}[1-\theta(y\_{i})]+\frac{1}{N}\sum\_{j}\theta(y\_{j})y\_{j}+\frac{1-s}{N}\underbrace{\sum\_{j}T(w\_{j})}\_{=\ \tau}. |  | (14) |

The first term of equation [14](https://arxiv.org/html/2510.26503v1#S5.E14 "In 5 Application: Government’s Optimal Taxation ‣ The sustainability of contribution norms with income dynamics") represents what individual ii keeps after making their voluntary contribution, the second term reflects their equal share of the collectively provided transfers, and the third term captures their share of redistributed tax revenue. The parameter s∈(0,1]s\in(0,1] captures the exogenous cost of public funds, which could stem from administrative burdens or distortionary effects of taxation.

When s>0s>0, public redistribution is less efficient than private redistribution, which creates a trade-off for the planner. If s=0s=0, redistribution through taxes would dominate, making voluntary transfers irrelevant and leading the government to fully equalize post-tax incomes by setting T​(wi)=wiT(w\_{i})=w\_{i}. To maintain a meaningful role for voluntary transfers, we assume s>0s>0 throughout.181818This is akin to assuming that the government faces an exogenous revenue requirement R>0R>0, leading to a constraint of the form GP+R≤TG^{P}+R\leq T (Sandmo, [1975](https://arxiv.org/html/2510.26503v1#bib.bib46)).

### 5.1 The Planner’s Problem

The planner’s objective is to maximize social welfare by choosing an optimal redistribution policy τ\tau. Welfare depends not only on the resulting payoffs under autarky and cooperation, but also on whether cooperation is sustainable given the underlying incentives. Formally, the planner evaluates:

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​(τ;δ)={V^ia​(τ)if ​δ<δ¯​(τ),V^ic​(τ)if ​δ≥δ¯​(τ),W(\tau;\delta)=\begin{cases}\hat{V}\_{i}^{a}(\tau)&\text{if }\delta<\underline{\delta}(\tau),\\ \\ \hat{V}\_{i}^{c}(\tau)&\text{if }\delta\geq\underline{\delta}(\tau),\end{cases} |  | (15) |

where δ¯​(τ)\underline{\delta}(\tau) denotes the minimum discount factor that makes cooperation incentive-compatible under tax policy τ\tau. The functions V^ia​(τ)\hat{V}\_{i}^{a}(\tau) and V^ic​(τ)\hat{V}\_{i}^{c}(\tau) represent average utility across players in the autarkic and cooperative outcomes, respectively:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V^ia​(τ)\displaystyle\hat{V}\_{i}^{a}(\tau) | =1N​∑i=1Nu​(xia​(τ)),\displaystyle=\frac{1}{N}\sum\_{i=1}^{N}u\left(x\_{i}^{a}(\tau)\right), |  | (16) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V^ic​(τ)\displaystyle\hat{V}\_{i}^{c}(\tau) | =1N​∑i=1Nuic​(τ),\displaystyle=\frac{1}{N}\sum\_{i=1}^{N}u\_{i}^{c}(\tau), |  | (17) |

where xia​(τ)x\_{i}^{a}(\tau) denotes individual consumption under autarky. The planner chooses the tax rate τ\tau to maximize expected welfare, taking into account both economic outcomes and the incentives for cooperation.
A central challenge is that both the value of cooperation and the incentive constraint—summarized by δ¯​(τ)\underline{\delta}(\tau)—depend on the tax policy itself. Even when the discount factor δ\delta is fixed, the planner may be able to induce or discourage cooperation through their choice of τ∈[0,1]\tau\in[0,1]. Taxation thus shapes not only the redistribution of income, but also the sustainability of cooperative behavior in the repeated game.

Proposition [3](https://arxiv.org/html/2510.26503v1#Thmproposition3 "Proposition 3. ‣ 5.1 The Planner’s Problem ‣ 5 Application: Government’s Optimal Taxation ‣ The sustainability of contribution norms with income dynamics") formalizes the distinction between two regimes: when cooperation can be sustained and when it cannot. It also describes how the optimal tax responds to changes in inequality, mobility, and norm’s progressivity in each regime.

###### Proposition 3.

Let δ¯​(τ)\underline{\delta}(\tau) denote the minimal discount factor required to sustain cooperation at tax rate τ\tau.
Let τa​(α)=arg⁡maxτ∈[0,1]⁡V^ia​(τ)\tau^{a}(\alpha)=\arg\max\_{\tau\in[0,1]}\hat{V}\_{i}^{a}(\tau) denote the optimal tax rate under autarky.

Then:

* •

  If there exists τ∈[0,1]\tau\in[0,1] such that δ=δ¯​(τ)\delta=\underline{\delta}(\tau), then cooperation is attainable, and the planner implements:

  |  |  |  |
  | --- | --- | --- |
  |  | τ∗=τ†​(δ)such thatδ¯​(τ†)=δ,\tau^{\*}=\tau^{\dagger}(\delta)\quad\text{such that}\quad\underline{\delta}(\tau^{\dagger})=\delta, |  |

  with the following comparative statics:

  |  |  |  |
  | --- | --- | --- |
  |  | ∂τ†∂m<0,∂τ†∂β<0,∂τ†∂α<0.\frac{\partial\tau^{\dagger}}{\partial m}<0,\quad\frac{\partial\tau^{\dagger}}{\partial\beta}<0,\quad\frac{\partial\tau^{\dagger}}{\partial\alpha}<0. |  |
* •

  If no such τ∈[0,1]\tau\in[0,1] exists (i.e., δ<minτ⁡δ¯​(τ)\delta<\min\_{\tau}\underline{\delta}(\tau)), then cooperation is not sustainable, and the planner chooses:

  |  |  |  |
  | --- | --- | --- |
  |  | τ∗=τa​(α),\tau^{\*}=\tau^{a}(\alpha), |  |

  with:

  |  |  |  |
  | --- | --- | --- |
  |  | ∂τa∂m=0,∂τa∂β=0,∂τa∂α>0.\frac{\partial\tau^{a}}{\partial m}=0,\quad\frac{\partial\tau^{a}}{\partial\beta}=0,\quad\frac{\partial\tau^{a}}{\partial\alpha}>0. |  |

Proposition [3](https://arxiv.org/html/2510.26503v1#Thmproposition3 "Proposition 3. ‣ 5.1 The Planner’s Problem ‣ 5 Application: Government’s Optimal Taxation ‣ The sustainability of contribution norms with income dynamics") distinguishes two regimes depending on whether cooperation can be sustained at any feasible tax rate. In the autarkic regime, where δ<δ¯​(τ)\delta<\underline{\delta}(\tau) for all τ∈[0,1]\tau\in[0,1], private cooperation is not feasible. Therefore, redistribution occurs solely through taxation. In this case, the optimal tax rate τa\tau^{a} depends only on inequality: as α\alpha increases, the planner’s incentive to reduce income dispersion leads to a higher tax. Since private transfers are absent in this regime, income mobility mm and the norm’s progressivity β\beta have no effect on the planner’s choice.

In the cooperative regime, where δ=δ¯​(τ)\delta=\underline{\delta}(\tau) for some τ∈[0,1]\tau\in[0,1], the planner implements cooperation exactly at the threshold of sustainability. That is, the planner selects a tax rate τ†​(δ)\tau^{\dagger}(\delta) such that cooperation becomes just viable in equilibrium. This tax rate enables both public and private redistribution. Because private transfers depend on income mobility and the norm’s progressivity, higher mm and β\beta improve the effectiveness of voluntary redistribution, allowing the planner to reduce reliance on taxation. Moreover, greater inequality α\alpha increases the volume of private transfers once cooperation is in place, further reducing the optimal tax burden. As a result, the optimal cooperative tax rate τ†\tau^{\dagger} is decreasing in all three parameters: mm, β\beta, and α\alpha.

![Refer to caption](figures/tau_star_vs_alpha_rho05_mu1_s009_delta07_N3_m08b2_m08b15_m08b0_m04b2.png)


Figure 5:  Welfare-maximizing tax rate τ∗\tau^{\*} as a function of inequality α\alpha, for different values of income mobility mm and norm’s progressivity β\beta.
Parameters: ρ=0.5\rho=0.5, μ=1\mu=1, s=0.09s=0.09, δ=0.7\delta=0.7, N=3N=3.

Figure [5](https://arxiv.org/html/2510.26503v1#S5.F5 "Figure 5 ‣ 5.1 The Planner’s Problem ‣ 5 Application: Government’s Optimal Taxation ‣ The sustainability of contribution norms with income dynamics") shows how the welfare-maximizing tax rate τ∗\tau^{\*} varies with inequality α\alpha for four combinations of income mobility mm and norm’s progressivity β\beta. Each curve exhibits a threshold value α\alpha at which cooperation becomes sustainable. To the left of this threshold, the planner operates in the autarkic regime; to the right, in the cooperative regime. The transition is marked by a vertical line for each curve.

Comparing the blue and orange lines (both with m=0.8m=0.8), we see that increasing the norm’s progressivity from β=1.5\beta=1.5 to β=2\beta=2 shifts the cooperation threshold leftward and lowers the optimal tax under cooperation. This illustrates that more progressive norms facilitate cooperation at lower inequality levels and reduce the need for taxation. Next, comparing the blue and red lines (both with β=2\beta=2), we observe that reducing mobility from m=0.8m=0.8 to m=0.4m=0.4 enables cooperation to emerge at a lower level of inequality. It also leads to a higher cooperative tax rate, since lower mobility reduces endogenous transfers. The green line, with m=0.8m=0.8 and β=0\beta=0, serves as a benchmark without public cooperation. This trajectory aligns with the autarkic segments of the other curves, confirming that in the absence of cooperation, the optimal tax rises with inequality and is unaffected by mm or β\beta.

## 6 Conclusions

This paper studies how income mobility and income inequality jointly shape the sustainability of cooperation in repeated interactions. We introduce a tractable framework of a risk-sharing organization in which individuals decide how much of their income to transfer to others. A key feature of the model is that individuals change their income over time, while keeping the organization’s income distribution constant. We characterize the conditions under which contribution norms—informal agreements about how much each member should transfer—can be sustained in equilibrium. Specifically, we find that income mobility has a positive effect on sustaining cooperation. In contrast, the effect of inequality is ambiguous and depends on the progressivity of the contribution norm and the degree of mobility.

Our framework relates to a variety of contexts where cooperation is crucial. Examples include risk-sharing between workers (Ligon
et al., [2002](https://arxiv.org/html/2510.26503v1#bib.bib38); Bigsten
et al., [2003](https://arxiv.org/html/2510.26503v1#bib.bib14)), local tax agreements (Wolf-Powers, [2010](https://arxiv.org/html/2510.26503v1#bib.bib54)), village-based health insurance schemes (Jajoo, [1992](https://arxiv.org/html/2510.26503v1#bib.bib32); Ahmed et al., [2016](https://arxiv.org/html/2510.26503v1#bib.bib2)), or fiscal arrangements within regions or monetary unions (Ventura, [2019](https://arxiv.org/html/2510.26503v1#bib.bib52)). In all these cases, participants repeatedly interact, face unequal incomes, and must rely on informal or partially enforced norms to govern transfers. Our results suggest that income mobility—whether driven by institutional design or economic shocks—plays a central role in determining the sustainability of such arrangements.

One could extend the proposed framework in several dimensions. First, while our baseline model assumes self-interested individuals, incorporating social preferences such as altruism (Becker, [1974](https://arxiv.org/html/2510.26503v1#bib.bib10)), reciprocity (Rabin, [1993](https://arxiv.org/html/2510.26503v1#bib.bib43)), or inequity aversion (Fehr and
Schmidt, [1999](https://arxiv.org/html/2510.26503v1#bib.bib28)) may alter our conclusions. Second, introducing heterogeneity in, for example, risk preferences or income risk could generate additional insights into the effect of income dynamics on cooperation (Briys and
Schlesinger, [1990](https://arxiv.org/html/2510.26503v1#bib.bib15); Huber, [2022](https://arxiv.org/html/2510.26503v1#bib.bib31)). Third, allowing individuals to save across periods would introduce a trade-off between informal insurance and self-insurance, providing a connection with models of precautionary savings (Kocherlakota, [2004](https://arxiv.org/html/2510.26503v1#bib.bib35); Buera and
Shin, [2011](https://arxiv.org/html/2510.26503v1#bib.bib16)). We leave these extensions for future research.

## References

* Acemoglu
  et al. (2018)

  Acemoglu, D., G. Egorov, and K. Sonin (2018).
  Social mobility and stability of democracy: Reevaluating de
  tocqueville.
  The Quarterly Journal of Economics 133(2),
  1041–1105.
* Ahmed et al. (2016)

  Ahmed, S., M. E. Hoque, A. R. Sarker, M. Sultana, Z. Islam, R. Gazi, and J. A.
  Khan (2016).
  Willingness-to-pay for community-based health insurance among
  informal workers in urban bangladesh.
  PloS one 11(2), e0148211.
* Alesina and
  Angeletos (2005)

  Alesina, A. and G.-M. Angeletos (2005).
  Fairness and redistribution.
  American economic review 95(4), 960–980.
* Alger (2025)

  Alger, I. (2025).
  Norms and norm change-driven by social kantian preferences.
* Alger and
  Weibull (2007)

  Alger, I. and J. W. Weibull (2007).
  Family ties, incentives and development: a model of coerced altruism.
  SSE/EFI Working Paper Series in Economics and Finance (681),
  07–10.
* Alger and
  Weibull (2010)

  Alger, I. and J. W. Weibull (2010).
  Kinship, incentives, and evolution.
  American Economic Review 100(4), 1725–1758.
* Amir (2003)

  Amir, R. (2003).
  Stochastic games in economics and related fields: an overview.
  Stochastic games and applications, 455–470.
* Atkinson (1970)

  Atkinson, A. B. (1970).
  On the measurement of inequality.
  Journal of Economic Theory 2(3), 244–263.
* Baston and
  Bostock (1991)

  Baston, V. J. and F. Bostock (1991).
  A generalized inspection game.
  Naval Research Logistics (NRL) 38(2), 171–182.
* Becker (1974)

  Becker, G. S. (1974).
  A theory of social interactions.
  Journal of political economy 82(6), 1063–1093.
* Behrman
  et al. (2000)

  Behrman, J., A. Gaviria, and M. Zsékely (2000).
  Social mobility: concepts and measurement.
  New markets, new opportunities, 3–21.
* Benabou and
  Ok (2001)

  Benabou, R. and E. A. Ok (2001).
  Social mobility and the demand for redistribution: the poum
  hypothesis.
  The Quarterly journal of economics 116(2), 447–487.
* Bicchieri (2008)

  Bicchieri, C. (2008).
  The fragility of fairness: An experimental investigation on the
  conditional status of pro-social norms.
  Philosophical issues 18, 229–248.
* Bigsten
  et al. (2003)

  Bigsten, A., P. Collier, S. Dercon, M. Fafchamps, B. Gauthier, J. W. Gunning,
  A. Oduro, R. Oostendorp, C. Pattillo, M. Söderbom, et al. (2003).
  Risk sharing in labor markets.
  The World Bank Economic Review 17(3), 349–366.
* Briys and
  Schlesinger (1990)

  Briys, E. and H. Schlesinger (1990).
  Risk aversion and the propensities for self-insurance and
  self-protection.
  Southern Economic Journal, 458–467.
* Buera and
  Shin (2011)

  Buera, F. J. and Y. Shin (2011).
  Self-insurance vs. self-financing: A welfare analysis of the
  persistence of shocks.
  Journal of Economic Theory 146(3), 845–862.
* Burke and
  Young (2011)

  Burke, M. A. and H. P. Young (2011).
  Social norms.
  In Handbook of social economics, Volume 1, pp. 311–338.
  Elsevier.
* Caplin and
  Schotter (2008)

  Caplin, A. and A. Schotter (2008).
  The foundations of positive and normative economics: a
  handbook.
  Oxford University Press.
* Chetty et al. (2017)

  Chetty, R., D. Grusky, M. Hell, N. Hendren, R. Manduca, and J. Narang (2017).
  The fading american dream: Trends in absolute income mobility since
  1940.
  Science 356(6336), 398–406.
* Chetty et al. (2014)

  Chetty, R., N. Hendren, P. Kline, E. Saez, and N. Turner (2014).
  Is the united states still a land of opportunity? recent trends in
  intergenerational mobility.
  American Economic Review 104(5), 141–147.
* Darlington et al. (2023)

  Darlington, M., K. D. Glazebrook, D. S. Leslie, R. Shone, and R. Szechtman
  (2023).
  A stochastic game framework for patrolling a border.
  European Journal of Operational Research.
* Dercon (2005)

  Dercon, S. (2005).
  Risk, insurance, and poverty: a review.
  Insurance against poverty, 9–37.
* Deutscher and
  Mazumder (2023)

  Deutscher, N. and B. Mazumder (2023).
  Measuring intergenerational income mobility: A synthesis of
  approaches.
  Journal of Economic Literature 61(3), 988–1036.
* Dold
  et al. (2018)

  Dold, M. F., C. Schubert, et al. (2018).
  Toward a behavioral foundation of normative economics.
  Review of Behavioral Economics 5(3-4), 221–241.
* Dubois
  et al. (2008)

  Dubois, P., B. Jullien, and T. Magnac (2008).
  Formal and informal risk sharing in ldcs: Theory and empirical
  evidence.
  Econometrica 76(4), 679–725.
* Durlauf
  et al. (2022)

  Durlauf, S. N., A. Kourtellos, and C. M. Tan (2022).
  The great gatsby curve.
  Annual Review of Economics 14(1), 571–605.
* Ericson and
  Pakes (1995)

  Ericson, R. and A. Pakes (1995).
  Markov-perfect industry dynamics: A framework for empirical work.
  The Review of economic studies 62(1), 53–82.
* Fehr and
  Schmidt (1999)

  Fehr, E. and K. M. Schmidt (1999).
  A theory of fairness, competition, and cooperation.
  The quarterly journal of economics 114(3), 817–868.
* Fields and
  Ok (1999)

  Fields, G. S. and E. A. Ok (1999).
  The measurement of income mobility: An introduction to the
  literature.
  In J. Silber (Ed.), Handbook of Income Inequality Measurement,
  pp. 557–598. Springer.
* Friedman (1962)

  Friedman, M. (1962).
  Capitalism and Freedom.
  Chicago: University of Chicago Press.
* Huber (2022)

  Huber, T. (2022).
  Comparative risk aversion in two periods: An application to
  self-insurance and self-protection.
  Journal of Risk and Insurance 89(1), 97–130.
* Jajoo (1992)

  Jajoo, U. (1992).
  Risk-sharing in rural health care.
  In World health forum, Volume 13, pp. 171.
* Jäntti and
  Jenkins (2015)

  Jäntti, M. and S. P. Jenkins (2015).
  Chapter 10 - income mobility.
  In A. B. Atkinson and F. Bourguignon (Eds.), Handbook of Income
  Distribution, Volume 2, pp. 807–935. Elsevier.
* Kocherlakota (1996)

  Kocherlakota, N. R. (1996).
  Implications of efficient risk sharing without commitment.
  The Review of Economic Studies 63(4), 595–609.
* Kocherlakota (2004)

  Kocherlakota, N. R. (2004).
  Figuring out the impact of hidden savings on optimal unemployment
  insurance.
  Review of Economic Dynamics 7(3), 541–554.
* Krueger and
  Perri (2011)

  Krueger, D. and F. Perri (2011).
  Public versus private risk sharing.
  Journal of Economic Theory 146(3), 920–956.
* Levhari
  et al. (1980)

  Levhari, D., L. J. Mirman, et al. (1980).
  The great fish war: An example using a dynamic cournot-nash solution.
  Bell Journal of Economics 11(1), 322–334.
* Ligon
  et al. (2002)

  Ligon, E., J. P. Thomas, and T. Worrall (2002).
  Informal insurance arrangements with limited commitment: Theory and
  evidence from village economies.
  The Review of Economic Studies 69(1), 209–244.
* McFarland (1970)

  McFarland, D. D. (1970).
  Intragenerational social mobility as a markov process: Including a
  time-stationary mark-ovian model that explains observed declines in mobility
  rates over time.
  American Sociological Review, 463–476.
* Mobarak and
  Rosenzweig (2013)

  Mobarak, A. M. and M. R. Rosenzweig (2013).
  Informal risk sharing, index insurance, and risk taking in developing
  countries.
  American Economic Review 103(3), 375–380.
* Neyman and
  Sorin (2003)

  Neyman, A. and S. Sorin (2003).
  Stochastic games and applications, Volume 570.
  Springer Science & Business Media.
* Prais (1955)

  Prais, S. J. (1955).
  Measuring social mobility.
  Journal of the Royal Statistical Society. Series A
  (General) 118(1), 56–66.
* Rabin (1993)

  Rabin, M. (1993).
  Incorporating fairness into game theory and economics.
  The American economic review, 1281–1302.
* Reuben and
  Riedl (2013)

  Reuben, E. and A. Riedl (2013).
  Enforcement of contribution norms in public good games with
  heterogeneous populations.
  Games and Economic Behavior 77(1), 122–137.
* Safarzyńska and van den Bergh (2010)

  Safarzyńska, K. and J. C. van den Bergh (2010).
  Evolutionary models in economics: a survey of methods and building
  blocks.
  Journal of Evolutionary Economics 20, 329–373.
* Sandmo (1975)

  Sandmo, A. (1975).
  Optimal taxation in the presence of externalities.
  Swedish Journal of Economics 77(1), 86–98.
* Shapley (1953)

  Shapley, L. S. (1953).
  Stochastic games.
  Proceedings of the national academy of sciences 39(10), 1095–1100.
* Shorrocks (1978a)

  Shorrocks, A. (1978a).
  Income inequality and income mobility.
  Journal of Economic Theory 19(2), 376–393.
* Shorrocks (1978b)

  Shorrocks, A. F. (1978b).
  The measurement of mobility.
  Econometrica 46, 1013–1024.
* Solan and
  Vieille (2015)

  Solan, E. and N. Vieille (2015).
  Stochastic games.
  Proceedings of the National Academy of Sciences 112(45), 13743–13746.
* Thomas and
  Worrall (1988)

  Thomas, J. and T. Worrall (1988).
  Self-enforcing wage contracts.
  The Review of Economic Studies 55(4), 541–554.
* Ventura (2019)

  Ventura, J. (2019).
  Joseph schumpeter lecture: Sharing a government.
  Journal of the European Economic Association 17(6),
  1723–1752.
* Witt (1993)

  Witt, U. (1993).
  Evolutionary economics.
  Aldershot, UK.
* Wolf-Powers (2010)

  Wolf-Powers, L. (2010).
  Community benefits agreements and local government: A review of
  recent evidence.
  Journal of the American Planning Association 76(2),
  141–159.
* Zelmer (2003)

  Zelmer, J. (2003).
  Linear public goods experiments: A meta-analysis.
  Experimental Economics 6, 299–310.

## Appendix A Appendix A: Mathematical Proofs

### A.1 Preliminaries

###### Lemma 5.

Let u¯a​u​t=1N​∑j=1Nu​(wj)\overline{u}^{\,aut}=\frac{1}{N}\sum\_{j=1}^{N}u(w\_{j}), uic=u​((1−θ​(wi))​wi+1N​∑j=1Nθ​(wj)​wj)u\_{i}^{c}=u\left((1-\theta(w\_{i}))w\_{i}+\frac{1}{N}\sum\_{j=1}^{N}\theta(w\_{j})w\_{j}\right), and u¯c​o​o​p=1N​∑j=1Nujc\overline{u}^{\,coop}=\frac{1}{N}\sum\_{j=1}^{N}u\_{j}^{c}. The values of autarky, deviation, and cooperation are given by:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Via\displaystyle V\_{i}^{a} | =11−δ​(1−m)​u​(wi)+δ​m(1−δ)​(1−δ​(1−m))​u¯a​u​t,\displaystyle=\frac{1}{1-\delta(1-m)}u(w\_{i})+\frac{\delta m}{(1-\delta)(1-\delta(1-m))}\,\overline{u}^{\,aut}, |  | (18) |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vid\displaystyle V\_{i}^{d} | =u​(wi+1N​∑j≠iθ​(wj)​wj)+δ​[(1−m)​(u​(wi)+δ​m​u¯a​u​t1−δ​(1−m))+m​u¯a​u​t],\displaystyle=u\left(w\_{i}+\frac{1}{N}\sum\_{j\neq i}\theta(w\_{j})w\_{j}\right)+\delta\left[(1-m)\left(\frac{u(w\_{i})+\delta m\,\overline{u}^{\,aut}}{1-\delta(1-m)}\right)+m\,\overline{u}^{\,aut}\right], |  | (19) |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vic\displaystyle V\_{i}^{c} | =(1−δ)​uic+δ​m​u¯c​o​o​p(1−δ)​(1−δ​(1−m)).\displaystyle=\frac{(1-\delta)u\_{i}^{c}+\delta m\,\overline{u}^{\,coop}}{(1-\delta)(1-\delta(1-m))}. |  | (20) |

### Proof of Lemma [5](https://arxiv.org/html/2510.26503v1#Thmtheorem5 "Lemma 5. ‣ A.1 Preliminaries ‣ Appendix A Appendix A: Mathematical Proofs ‣ The sustainability of contribution norms with income dynamics")

#### Autarky-algebra.

Define the sum of autarky values across income-types as S=∑j=1NVjaS=\sum\_{j=1}^{N}V\_{j}^{a}, we can the re express the equation above as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Via=u​(wi)+δ​[(1−N−1N​m)​Via+mN​(S−Via)].V\_{i}^{a}=u(w\_{i})+\delta\left[\left(1-\frac{N-1}{N}m\right)V\_{i}^{a}+\frac{m}{N}\left(S-V\_{i}^{a}\right)\right]. |  | (21) |

If we take the sum of the expression above we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S=∑i=1Nu​(wi)+δ​[(1−N−1N​m)​S+mN​(S⋅N−S)].S=\sum\_{i=1}^{N}u(w\_{i})+\delta\left[\left(1-\frac{N-1}{N}m\right)S+\frac{m}{N}\left(S\cdot N-S\right)\right]. |  | (22) |

By simple algebra we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S=∑i=1Nu​(wi)1−δ.\displaystyle S=\frac{\sum\_{i=1}^{N}u(w\_{i})}{1-\delta}. |  | (23) |

Substituting the value of SS into the expression for ViaV\_{i}^{a} yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Via=11−δ​(1−m)​[u​(wi)+δ​mN​∑i=1Nu​(wi)1−δ].\displaystyle V\_{i}^{a}=\frac{1}{1-\delta(1-m)}\left[u(w\_{i})+\frac{\delta m}{N}\frac{\sum\_{i=1}^{N}u(w\_{i})}{1-\delta}\right]. |  | (24) |

Autarky values are monotonically increasing in income levels wiw\_{i}.

#### Algebra of deviations.

We have that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vid\displaystyle V\_{i}^{d} | =u​(wi+∑j≠iwjN)+δ​[(1−N−1N​m)​Via+∑j≠i1N​m​Vja]\displaystyle=u\left(w\_{i}+\frac{\sum\_{j\neq i}w\_{j}}{N}\right)+\delta\left[\left(1-\frac{N-1}{N}m\right)V\_{i}^{a}+\sum\_{j\neq i}\frac{1}{N}mV\_{j}^{a}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =u​(wi+∑j≠iwjN)+δ​[(1−m)​(u​(wi)+δ​mN​S1−δ​(1−m))+mN​S]\displaystyle=u\left(w\_{i}+\frac{\sum\_{j\neq i}w\_{j}}{N}\right)+\delta\left[\left(1-m\right)\left(\frac{u(w\_{i})+{\delta}\frac{m}{N}S}{1-\delta(1-m)}\right)+\frac{m}{N}S\right] |  |

### Proof of Lemma [2](https://arxiv.org/html/2510.26503v1#Thmtheorem2 "Lemma 2. ‣ 3 General solution ‣ The sustainability of contribution norms with income dynamics")

###### Proof.

Take k>ik>i, then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vid−Vkd\displaystyle V\_{i}^{d}-V\_{k}^{d} | =u​(wi+∑j≠iwjN)−u​(wk+∑j≠kwjN)\displaystyle=u\left(w\_{i}+\frac{\sum\_{j\neq i}w\_{j}}{N}\right)-u\left(w\_{k}+\frac{\sum\_{j\neq k}w\_{j}}{N}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +δ​[(1−N−1N​m)​(Via−Vka)+mN​(Vka−Via)]\displaystyle+\delta\left[\left(1-\frac{N-1}{N}m\right)\left(V\_{i}^{a}-V\_{k}^{a}\right)+\frac{m}{N}\left(V\_{k}^{a}-V\_{i}^{a}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =u​(wi+∑j≠iwjN)−u​(wk+∑j≠kwjN)+δ​[(1−m)​(Via−Vka)]\displaystyle=u\left(w\_{i}+\frac{\sum\_{j\neq i}w\_{j}}{N}\right)-u\left(w\_{k}+\frac{\sum\_{j\neq k}w\_{j}}{N}\right)+\delta\left[\left(1-m\right)\left(V\_{i}^{a}-V\_{k}^{a}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | >0\displaystyle>0 |  |

Since both terms in the last line are positive. The instantaneous utility terms decreases in wiw\_{i}, which can be seen by noting that:

|  |  |  |
| --- | --- | --- |
|  | wi+∑j≠iwjN=wi​(N−1N)+WN.\displaystyle w\_{i}+\frac{\sum\_{j\neq i}w\_{j}}{N}=w\_{i}\left(\frac{N-1}{N}\right)+\frac{W}{N}. |  |

for W=∑j=1NwjW=\sum\_{j=1}^{N}w\_{j}.
∎

### Proof of Lemma [4](https://arxiv.org/html/2510.26503v1#Thmtheorem4 "Lemma 4. ‣ 4.2 The role of income inequality ‣ 4 The effect of income mobility and income inequality ‣ The sustainability of contribution norms with income dynamics")

###### Proof.

Consider now:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δi​(δ)\displaystyle\Delta\_{i}(\delta) | =Vid​e​v−Vic​o​o​p\displaystyle={V\_{i}}^{dev}-{V\_{i}}^{coop} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =u​(wi+∑j≠iwjN)+δ​[(1−m)​(u​(wi)+δ​mN​S1−δ​(1−m))+mN​S]−u​(w¯)1−δ,\displaystyle=u\left(w\_{i}+\frac{\sum\_{j\neq i}w\_{j}}{N}\right)+\delta\left[\left(1-m\right)\left(\frac{u(w\_{i})+{\delta}\frac{m}{N}S}{1-\delta(1-m)}\right)+\frac{m}{N}S\right]-\frac{u(\bar{w})}{1-\delta}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =u​(wi+∑j≠iwjN)+δ​[(1−m)​(u​(wi)+δ​mN​∑i=1Nu​(wi)1−δ1−δ​(1−m))+mN​∑i=1Nu​(wi)1−δ]−u​(w¯)1−δ,\displaystyle=u\left(w\_{i}+\frac{\sum\_{j\neq i}w\_{j}}{N}\right)+\delta\left[\left(1-m\right)\left(\frac{u(w\_{i})+{\delta}\frac{m}{N}\frac{\sum\_{i=1}^{N}u(w\_{i})}{1-\delta}}{1-\delta(1-m)}\right)+\frac{m}{N}\frac{\sum\_{i=1}^{N}u(w\_{i})}{1-\delta}\right]-\frac{u(\bar{w})}{1-\delta}, |  |

where w¯=∑i=1Nwi/N\bar{w}=\sum\_{i=1}^{N}w\_{i}/N is the average income. We are looking for conditions such that Δi​(δ)<0\Delta\_{i}(\delta)<0, which are given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | >u​(wi+∑j≠iwjN)+δ​[(1−m)​(u​(wi)+δ​mN​∑i=1Nu​(wi)1−δ1−δ​(1−m))+mN​∑i=1Nu​(wi)1−δ]−u​(w¯)1−δ.\displaystyle>u\left(w\_{i}+\frac{\sum\_{j\neq i}w\_{j}}{N}\right)+\delta\left[\left(1-m\right)\left(\frac{u(w\_{i})+{\delta}\frac{m}{N}\frac{\sum\_{i=1}^{N}u(w\_{i})}{1-\delta}}{1-\delta(1-m)}\right)+\frac{m}{N}\frac{\sum\_{i=1}^{N}u(w\_{i})}{1-\delta}\right]-\frac{u(\bar{w})}{1-\delta}. |  |

∎

### Proof of Proposition [1](https://arxiv.org/html/2510.26503v1#Thmproposition1 "Proposition 1. ‣ 3 General solution ‣ The sustainability of contribution norms with income dynamics")

###### Proof.

Define the coefficients:

|  |  |  |
| --- | --- | --- |
|  | c0=u​(wi+∑j≠iwjN),\displaystyle c\_{0}=u\left(w\_{i}+\frac{\sum\_{j\neq i}w\_{j}}{N}\right), |  |
|  |  |  |
| --- | --- | --- |
|  | c1=u​(wi),\displaystyle c\_{1}=u(w\_{i}), |  |
|  |  |  |
| --- | --- | --- |
|  | c2=u​(w¯)=u​(∑i=1NwiN),\displaystyle c\_{2}=u\left(\overline{w}\right)=u\left(\frac{\sum\_{i=1}^{N}w\_{i}}{N}\right), |  |
|  |  |  |
| --- | --- | --- |
|  | c3=1N​∑i=1Nu​(wi).\displaystyle c\_{3}=\frac{1}{N}\sum\_{i=1}^{N}u(w\_{i}). |  |

The value of deviation is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Videv\displaystyle V\_{i}^{\text{dev}} | =u​(wi+∑j≠iwjN)+δ​[(1−m)​(u​(wi)+δ​mN​S1−δ​(1−m))+mN​S]\displaystyle=u\left(w\_{i}+\frac{\sum\_{j\neq i}w\_{j}}{N}\right)+\delta\left[(1-m)\left(\frac{u(w\_{i})+\delta\frac{m}{N}S}{1-\delta(1-m)}\right)+\frac{m}{N}S\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c0+δ​[(1−m)​(c1+δ​m1−δ​c31−δ​(1−m))+m1−δ​c3].\displaystyle=c\_{0}+\delta\left[(1-m)\left(\frac{c\_{1}+\delta\frac{m}{1-\delta}c\_{3}}{1-\delta(1-m)}\right)+\frac{m}{1-\delta}c\_{3}\right]. |  |

The value of cooperation is:

|  |  |  |
| --- | --- | --- |
|  | Vcoop=11−δ​u​(∑i=1NwiN)=11−δ​c2.\displaystyle V^{\text{coop}}=\frac{1}{1-\delta}u\left(\frac{\sum\_{i=1}^{N}w\_{i}}{N}\right)=\frac{1}{1-\delta}c\_{2}. |  |

We aim to analyze:

|  |  |  |
| --- | --- | --- |
|  | Δ​(δ)=Vcoop−Videv>0,\displaystyle\Delta(\delta)=V^{\text{coop}}-V\_{i}^{\text{dev}}>0, |  |

which leads to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​(δ)\displaystyle\Delta(\delta) | =c21−δ−c0−δ​[(1−m)​(c1+δ​m1−δ​c31−δ​(1−m))+m1−δ​c3]>0.\displaystyle=\frac{c\_{2}}{1-\delta}-c\_{0}-\delta\left[(1-m)\left(\frac{c\_{1}+\delta\frac{m}{1-\delta}c\_{3}}{1-\delta(1-m)}\right)+\frac{m}{1-\delta}c\_{3}\right]>0. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⇒c2−c0​(1−δ)−δ​(1−δ)​[(1−m)​(c1+δ​m1−δ​c31−δ​(1−m))+m1−δ​c3]>0.\displaystyle\Rightarrow c\_{2}-c\_{0}(1-\delta)-\delta(1-\delta)\left[(1-m)\left(\frac{c\_{1}+\delta\frac{m}{1-\delta}c\_{3}}{1-\delta(1-m)}\right)+\frac{m}{1-\delta}c\_{3}\right]>0. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⇒(1−δ​(1−m))​c2−(1−δ​(1−m))​c0​(1−δ)\displaystyle\Rightarrow(1-\delta(1-m))c\_{2}-(1-\delta(1-m))c\_{0}(1-\delta) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −δ​(1−m)​[(1−δ)​(c1+δ​m1−δ​c3)+m​c3​(1−δ​(1−m))]>0.\displaystyle\quad-\delta(1-m)\left[(1-\delta)(c\_{1}+\delta\frac{m}{1-\delta}c\_{3})+mc\_{3}(1-\delta(1-m))\right]>0. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⇒c2−c0−δ​((1−m)​c2−c0−c0​(1−m))−δ2​c0​(1−m)\displaystyle\Rightarrow c\_{2}-c\_{0}-\delta((1-m)c\_{2}-c\_{0}-c\_{0}(1-m))-\delta^{2}c\_{0}(1-m) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −δ​((1−m)​(c1+δ​(m​c3−c1))+m​c3−δ​m​c3​(1−m))>0.\displaystyle\quad-\delta((1-m)(c\_{1}+\delta(mc\_{3}-c\_{1}))+mc\_{3}-\delta mc\_{3}(1-m))>0. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⇒c2−c0+δ​[c0−m​c3−(1−m)​(c2−c0+c1)]\displaystyle\Rightarrow c\_{2}-c\_{0}+\delta[c\_{0}-mc\_{3}-(1-m)(c\_{2}-c\_{0}+c\_{1})] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +δ2​(1−m)​(c1−c0)>0.\displaystyle\quad+\delta^{2}(1-m)(c\_{1}-c\_{0})>0. |  |

#### Analyzing the roots.

The quadratic inequality is given by:

|  |  |  |
| --- | --- | --- |
|  | c2−c0+δ​[c0−m​c3−(1−m)​(c2−c0+c1)]+δ2​(1−m)​(c1−c0)>0.c\_{2}-c\_{0}+\delta\left[c\_{0}-mc\_{3}-(1-m)(c\_{2}-c\_{0}+c\_{1})\right]+\delta^{2}(1-m)(c\_{1}-c\_{0})>0. |  |

Rewriting this in standard quadratic form, we have:

|  |  |  |
| --- | --- | --- |
|  | A​δ2+B​δ+C=0,A\delta^{2}+B\delta+C=0, |  |

where the coefficients are defined as:

|  |  |  |
| --- | --- | --- |
|  | A=(1−m)​(c1−c0),A=(1-m)(c\_{1}-c\_{0}), |  |

|  |  |  |
| --- | --- | --- |
|  | B=c0−m​c3−(1−m)​(c2−c0+c1),B=c\_{0}-mc\_{3}-(1-m)(c\_{2}-c\_{0}+c\_{1}), |  |

|  |  |  |
| --- | --- | --- |
|  | C=c2−c0.C=c\_{2}-c\_{0}. |  |

To analyze the sign of each coefficient, note that from the given inequalities c0>c1>c2>c3c\_{0}>c\_{1}>c\_{2}>c\_{3}:

1. For AA, since c1−c0<0c\_{1}-c\_{0}<0 and 1−m>01-m>0 for m∈[0,1)m\in[0,1), it follows that A=(1−m)​(c1−c0)<0A=(1-m)(c\_{1}-c\_{0})<0. Thus, the parabola opens downward.
2. For CC, since c2−c0<0c\_{2}-c\_{0}<0, it follows that C<0C<0.
3. For BB, we observe that c0−m​c3>0c\_{0}-mc\_{3}>0 (since c0>c3c\_{0}>c\_{3} and m∈[0,1)m\in[0,1)). Additionally, the term −(1−m)​(c2−c0+c1)-(1-m)(c\_{2}-c\_{0}+c\_{1}) contributes negatively. Therefore, B>0B>0.

The roots of the quadratic equation are given by:

|  |  |  |
| --- | --- | --- |
|  | δ1,2=−B±B2−4​A​C2​A.\delta\_{1,2}=\frac{-B\pm\sqrt{B^{2}-4AC}}{2A}. |  |

Consider the negative root δ1\delta\_{1}. We can use the fact that c0>c1>c2>c4c\_{0}>c\_{1}>c\_{2}>c\_{4}, and that the discriminant is minimal for either A=0A=0 or C=0C=0 to find a lower bound for this root:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | δ1\displaystyle\delta\_{1} | ≥−B+B2−02​A\displaystyle\geq\frac{-B+\sqrt{B^{2}-0}}{2A} |  | (25) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−BA\displaystyle=\frac{-B}{A} |  | (26) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =c0−m​c3−(1−m)​(c2−c0+c1)−(1−m)​(c1−c0)\displaystyle=\frac{c\_{0}-mc\_{3}-(1-m)(c\_{2}-c\_{0}+c\_{1})}{-(1-m)(c\_{1}-c\_{0})} |  | (27) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =c0−c3(c1−c0)+c0−c1−c2(c1−c0)+m​c0+c3−2​m​c3(1−m)​(c1−c0)\displaystyle=\frac{c\_{0}-c\_{3}}{(c\_{1}-c\_{0})}+\frac{c\_{0}-c\_{1}-c\_{2}}{(c\_{1}-c\_{0})}+\frac{mc\_{0}+c\_{3}-2mc\_{3}}{(1-m)(c\_{1}-c\_{0})} |  | (28) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | >1\displaystyle>1 |  | (29) |

This means that we only need to take of the second root of the polynomial.

#### Bounds for δ2\delta\_{2}.-

Analogously as we did before, the maximal value of the discriminant, obtained by evaluating A=0A=0 or C=0C=0, yield a lower zero bound for the second root: δ2≥0\delta\_{2}\geq 0. Finally, the root is maximal when then discriminant is null, i.e:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ1\displaystyle\delta\_{1} | ≤−B+02​A\displaystyle\leq\frac{-B+\sqrt{0}}{2A} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−B2​A\displaystyle=\frac{-B}{2A} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c0−c32​(c1−c0)+c0−c1−c22​(c1−c0)+m​c0+c3−2​m​c32​(1−m)​(c1−c0)\displaystyle=\frac{c\_{0}-c\_{3}}{2(c\_{1}-c\_{0})}+\frac{c\_{0}-c\_{1}-c\_{2}}{2(c\_{1}-c\_{0})}+\frac{mc\_{0}+c\_{3}-2mc\_{3}}{2(1-m)(c\_{1}-c\_{0})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | <1\displaystyle<1 |  |

∎