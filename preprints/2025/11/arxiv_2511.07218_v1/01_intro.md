---
authors:
- Masaya Nishihata
doc_id: arxiv:2511.07218v1
family_id: arxiv:2511.07218
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team
  Production I am grateful to Ryo Nakajima for his valuable comments and suggestions
  that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing
  his domain expertise and providing insightful feedback from a practitioner’s perspective.
  Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful
  and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number
  JPMJSP2123.'
url_abs: http://arxiv.org/abs/2511.07218v1
url_html: https://arxiv.org/html/2511.07218v1
venue: arXiv q-fin
version: 1
year: 2025
---


Masaya Nishihata
Graduate School of Economics, Keio University, 2-15-45 Mita, Minato-ku, Tokyo 108-8345, Japan (e-mail: [nishihata.masaya@gmail.com](mailto:)).

(
November 10, 2025)

###### Abstract

Superstars often dominate key tasks because of their exceptional abilities, but this concentration of responsibility may unintentionally limit on-the-job learning opportunities for others. Using panel data from Major League Baseball (MLB), this study examines how superstar presence affects teammates’ opportunities and career outcomes. To address potential endogeneity in team composition, we exploit plausibly exogenous variation in superstar availability caused by injuries. When a superstar is active in the same team-position unit, non-star teammates play significantly less. These short-term reductions in playing time extend to longer horizons: players who begin their careers alongside a superstar who remains active for a full season (i.e., not on the injured list) are about 1.7 times more likely to exit MLB earlier than comparable peers. A key mechanism is reduced skill development—limited playing opportunities hinder subsequent growth in offensive performance. At the team level, greater dependence on superstars raises immediate productivity but magnifies performance declines after their departure, indicating a trade-off between short-term success and long-term adaptability. Overall, the findings suggest that while concentrating key roles in top performers boosts output in the short run, it can restrict others’ development and retention. Similar dynamics may arise in other organizations that rely heavily on a few exceptional individuals.
  
Keywords: superstar, human capital, long-term career
  
JEL code: J24, J44, L83, M54

## 1 Introduction

Even within the same workplace, worker productivity is rarely uniform. Such differences in individual ability can shape how tasks are allocated within organizations, as managers tend to assign more critical or visible tasks to higher-performing workers. This tendency may create disparities in learning opportunities and long-term career development among colleagues. rosen1981economics formalizes how differences in talent, combined with demand structures that reward quality over quantity, can generate “superstar” outcomes, as illustrated by markets for musicians, artists, and athletes. While these examples describe extreme cases in which technology amplifies small differences in talent, a similar—though less pronounced—concentration of responsibility likely arises in typical workplace environments as well. Understanding how such concentration affects coworkers’ opportunities for on-the-job learning and the dynamics of team production is crucial for thinking about the optimal allocation of tasks and talent within organizations.

This study uses data from Major League Baseball (MLB) to examine how the presence of superstars affects the opportunities and long-term career outcomes of their non-star teammates. We first investigate whether sharing a team and position with a superstar reduces the playing opportunities, as measured by plate appearances, for their non-star teammates during a season. We then analyze longer-term effects by examining how exposure to superstars during a player’s MLB debut season influences their career length and the development of performance over time. Finally, we explore whether teams that heavily rely on superstars experience different trajectories of team productivity following their departure.

Using MLB data to estimate the effects of superstars offers several advantages. First, the data provide detailed individual performance metrics over multiple seasons, making them well-suited for analyzing long-term impacts. Unlike typical workplace datasets, MLB records allow us to identify precisely who works with whom—linking each player to specific teammates and positions within a team—while tracking those same individuals throughout their professional careers. This structure enables precise measurement of both team composition and career trajectories. Second, identifying superstar effects requires addressing the endogeneity of team decisions, such as acquiring or releasing star players in response to their teammates’ performance. MLB’s institutional environment helps to mitigate this concern. In particular, the league operates a formal Injured List (IL) system, under which any player placed on the IL is prohibited from participating in games for a designated minimum period. These forced absences generate exogenous variation in teammates’ exposure to superstars, providing a natural experiment for identifying causal effects. This approach parallels azoulay2010superstar, who exploit the unexpected deaths of star scientists as exogenous shocks to estimate superstar effects. Finally, MLB data provide a transparent and objective definition of stardom based on All-Star game selections: as discussed in Section [3](https://arxiv.org/html/2511.07218v1#S3 "3 Data ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123."), we define a superstar as a player who was selected for the All-Star game at least twice.

This study contributes to three strands of literature. First, it adds to the research on superstar effects. azoulay2010superstar identify such effects among scientists, finding positive externalities through knowledge spillovers. brown2011quitters analyzes data from golf tournaments and shows that the presence of superstars reduces other players’ performance, interpreting the results through the lens of tournament incentives. However, these studies do not explore the mechanisms through which superstars might hinder their peers’ human capital accumulation. This study makes a novel contribution by focusing on this previously overlooked mechanism. A related study in management, li2020boon, shows that stars reduce non-stars’ learning. Yet their analysis relies on single-year survey data and is limited in addressing endogeneity. By examining long-term outcomes and leveraging exogenous variation from superstar injuries, this study offers new insights into how superstars affect human capital formation among colleagues.

Second, this study contributes to the literature on peer effects in the workplace. While extensive research has examined peer effects, the evidence remains mixed. Positive peer effects have been documented in some contexts, such as among cashiers (mas2009peers), fruit pickers (bandiera2010social), and swimmers (yamane2015peer), whereas other studies find no evidence of such effects among professional golfers (guryan2009peer) or university scientists (waldinger2012peer). Moreover, heterogeneous peer effects have been observed depending on factors such as gender (beugnot2019gender), the nature of tasks, and the presence of monetary incentives (nishihata2022heterogeneous). However, most existing studies focus on short-term peer influences—how individuals adjust their immediate effort or performance in response to high-performing colleagues—while relatively little is known about their lasting implications for career outcomes. In contrast, this study investigates the long-term consequences of peer exposure, specifically how playing alongside a superstar shapes career trajectories over time. By analyzing long-term superstar effects in a highly professionalized labor market such as MLB, this study provides a new perspective on how peer influences affect career development rather than merely contemporaneous productivity.

A recent insightful and closely related study by chalioti2025peer uses National Basketball Association (NBA) data to show that rookies who join stronger teams tend to receive less playing time and exhibit lower performance. However, their analysis interprets playing time primarily as a matter of visibility and relies on a static framework. In contrast, this study adopts a dynamic perspective, focusing on how the concentration of key tasks in superstars may limit on-the-job training opportunities and hinder the human capital accumulation of non-star teammates. In this sense, our work complements theirs by highlighting a distinct mechanism through which superstars can affect their peers’ long-term development. Moreover, while chalioti2025peer focus on the individual-level consequences for rookies, we extend the analysis to the team level by examining whether reliance on superstars enhances or undermines team productivity in both the short and medium term.

Finally, this study contributes to the literature on the long-term effects of early-career random shocks on subsequent career outcomes. For instance, genda2010long and kahn2010long show that entering the labor market during a recession has persistent negative effects on earnings and employment. Similarly, koizumi2024much uses data from professional speedboat races to investigate how early-stage luck can generate enduring disparities in success. Building on this line of research, the present study examines whether early-career exposure to a superstar teammate in the same position has lasting effects on a player’s career trajectory. By analyzing these dynamics, the study contributes to understanding the long-term implications of workplace design and task allocation.

Our analysis reveals that the presence of superstars on the same team and in the same position significantly reduces the playing opportunities of their non-star teammates, as measured by plate appearances. Moreover, the influence of superstar exposure extends beyond short-term constraints on playing time. Players who share a position with a superstar during their MLB debut season face a higher likelihood of exiting the league in the long run, even after accounting for subsequent exposure to superstars in later seasons. One plausible mechanism is that limited playing opportunities restrict on-the-job learning, slowing the accumulation of human capital and the development of offensive performance, which in turn lowers players’ subsequent evaluations and shortens their career longevity. This dynamic creates a self-reinforcing disadvantage, whereby players with fewer early-career opportunities are more likely to experience premature career exits. At the team level, we find that greater reliance on superstars is associated with higher contemporaneous productivity, but teams that were more dependent on their stars suffer larger relative declines in OPS following a superstar’s exit, with these effects lasting through the season of exit and the subsequent year.

These findings highlight a fundamental trade-off in organizational task allocation: while concentrating key responsibilities in the hands of top performers can boost short-term efficiency, it may simultaneously limit opportunities for skill development among others, thereby undermining the long-term depth and adaptability of the team. In the context of MLB, institutional mechanisms designed to promote competitive balance—such as the reverse-order player draft—may prevent the negative effects of superstar dependence from persisting over the long term. By contrast, in typical workplace settings or industries where such balancing mechanisms are absent and disparities are more persistent, reliance on a few top performers could entail greater long-term costs. These results thus underscore the importance of designing task assignments and talent management practices that balance immediate productivity gains with sustained human capital development.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2511.07218v1#S2 "2 Conceptual framework ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.") develops a conceptual framework that illustrates the trade-off between short-term efficiency and long-term human capital accumulation arising from the concentration of key tasks in superstars. Section [3](https://arxiv.org/html/2511.07218v1#S3 "3 Data ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.") describes the MLB data and key variables used in the analysis. Sections [4](https://arxiv.org/html/2511.07218v1#S4 "4 Empirical framework ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.") and [5](https://arxiv.org/html/2511.07218v1#S5 "5 Results ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.") describe the empirical strategy and present the main estimation results, respectively. Finally, Section [6](https://arxiv.org/html/2511.07218v1#S6 "6 Conclusion ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.") discusses the implications of the findings and concludes.

## 2 Conceptual framework

In this section, we develop a simple dynamic model to illustrate how the presence of a highly skilled teammate—a “superstar”—affects the allocation of playing time and the process of skill formation within a team.

Following chalioti2025peer, we consider a team production setting in which a principal must allocate a limited task opportunity across workers. We simplify the setting to a two-person environment where a single task slot is continuously divided between the two workers each period, while explicitly incorporating dynamic learning effects to analyze how on-the-job training (OJT) mechanisms interact with task allocation decisions over time.

The framework applies not only to sports but also to many organizational settings characterized by capacity or coordination constraints that limit how many individuals can engage in core tasks at any given time—such as law firms where only a few associates lead client meetings, surgical teams where one physician operates while others assist, or software and consulting projects where front-line roles rotate among team members.

### 2.1 Setup

In each period, there is a single position (one task slot) to be filled by two members, ii and jj. The team (principal) decides how to allocate time between them. Total available time is normalized to one:

|  |  |  |
| --- | --- | --- |
|  | τi+τj=1,τi,τj∈[0,1].\displaystyle\tau\_{i}+\tau\_{j}=1,\quad\tau\_{i},\tau\_{j}\in[0,1]. |  |

Let si​ts\_{it} and sj​ts\_{jt} denote the skill levels of players ii and jj at time tt. Team output in period tt is given by

|  |  |  |
| --- | --- | --- |
|  | Yt=fi​(si​t,τi)+fj​(sj​t,τj),\displaystyle Y\_{t}=f\_{i}(s\_{it},\tau\_{i})+f\_{j}(s\_{jt},\tau\_{j}), |  |

where fi​(⋅)f\_{i}(\cdot) and fj​(⋅)f\_{j}(\cdot) are twice continuously differentiable production functions satisfying
fi,s>0f\_{i,s}>0, fi,τ>0f\_{i,\tau}>0, and fi,τ​τ<0f\_{i,\tau\tau}<0.
Hence, output is increasing in both skill and assigned time, but exhibits diminishing returns in time.

### 2.2 Skill formation

The skill formation process follows the on-the-job training (OJT) framework of kuruscu2006training, which extends the standard human capital investment model of ben1967production to settings where skills are accumulated through productive experience. Consistent with this approach, we assume that a player’s skill in the next period depends on both the current level of skill and on-the-job learning during the current period:

|  |  |  |
| --- | --- | --- |
|  | si,t+1=(1−δ)​si​t+λi​(τi,sj​t),\displaystyle s\_{i,t+1}=(1-\delta)s\_{it}+\lambda\_{i}(\tau\_{i},s\_{jt}), |  |

where δ∈(0,1)\delta\in(0,1) represents the depreciation rate of skills, capturing forgetting or obsolescence, and λi​(⋅)\lambda\_{i}(\cdot) is a learning function that summarizes returns to on-the-job experience. Learning is increasing in one’s own task time and in the skill of one’s teammate: λi,τ>0\lambda\_{i,\tau}>0, λi,sj>0\lambda\_{i,s\_{j}}>0, and λi,τ​τ<0\lambda\_{i,\tau\tau}<0.

Relative to standard OJT models, in which individuals choose their own training effort or time allocation, here the allocation of task time τi\tau\_{i} is determined by the principal as part of a team-level optimization problem. This formulation embeds the OJT mechanism within a team production context, where individual learning depends not only on assigned task time but also on the skill of one’s teammate, sjs\_{j}. The inclusion of sjs\_{j} captures potential spillover effects from working alongside a more skilled teammate, while the concavity in τi\tau\_{i} reflects diminishing returns to repeated task exposure.

### 2.3 Dynamic optimization problem

The team chooses τi\tau\_{i} each period to maximize the discounted sum of future outputs:

|  |  |  |
| --- | --- | --- |
|  | V​(si​t,sj​t)=maxτi∈[0,1]⁡{fi​(si​t,τi)+fj​(sj​t,1−τi)+β​V​(si,t+1,sj,t+1)},\displaystyle V(s\_{it},s\_{jt})=\max\_{\tau\_{i}\in[0,1]}\left\{f\_{i}(s\_{it},\tau\_{i})+f\_{j}(s\_{jt},1-\tau\_{i})+\beta V(s\_{i,t+1},s\_{j,t+1})\right\}, |  |

where β∈(0,1)\beta\in(0,1) is the discount factor. The first-order condition (FOC) for optimal time allocation is

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(τi;si​t,sj​t)\displaystyle F(\tau\_{i};s\_{it},s\_{jt}) | ≡fi,τi​(si​t,τi)−fj,τj​(sj​t,1−τi)+β​[Vsi​(si,t+1,sj,t+1)​λi,τi−Vsj​(si,t+1,sj,t+1)​λj,τj]\displaystyle\equiv f\_{i,\tau\_{i}}(s\_{it},\tau\_{i})-f\_{j,\tau\_{j}}(s\_{jt},1-\tau\_{i})+\beta\left[V\_{s\_{i}}(s\_{i,t+1},s\_{j,t+1})\lambda\_{i,\tau\_{i}}-V\_{s\_{j}}(s\_{i,t+1},s\_{j,t+1})\lambda\_{j,\tau\_{j}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =0.\displaystyle=0. |  |

To ensure a stable interior solution, we impose the following second-order condition: for all relevant (si​t,sj​t,τi)(s\_{it},s\_{jt},\tau\_{i}), the first-order condition is strictly decreasing in task time, ∂F/∂τi<0\partial F/\partial\tau\_{i}<0. This assumption implies that the static concavity of team production and learning in τi\tau\_{i} dominates any dynamic learning incentives, ensuring local concavity of the objective in τi\tau\_{i} and a unique interior optimum.

We are interested in how the presence of a more skilled teammate affects the optimal allocation of task time. Let τi∗​(si​t,sj​t)\tau\_{i}^{\*}(s\_{it},s\_{jt}) denote the optimal time share that solves F​(τi;si​t,sj​t)=0F(\tau\_{i};s\_{it},s\_{jt})=0. Under the second-order condition above, we have ∂F/∂τi<0\partial F/\partial\tau\_{i}<0 at the optimum, so by the Implicit Function Theorem there exists a continuously differentiable function τi∗​(⋅)\tau\_{i}^{\*}(\cdot) such that

|  |  |  |
| --- | --- | --- |
|  | F​(τi∗​(si​t,sj​t);si​t,sj​t)=0\displaystyle F(\tau\_{i}^{\*}(s\_{it},s\_{jt});s\_{it},s\_{jt})=0 |  |

and

|  |  |  |
| --- | --- | --- |
|  | d​τi∗d​sj​t=−∂F/∂sj​t∂F/∂τi.\displaystyle\frac{d\tau\_{i}^{\*}}{ds\_{jt}}=-\frac{\partial F/\partial s\_{jt}}{\partial F/\partial\tau\_{i}}. |  |

Because ∂F/∂τi<0\partial F/\partial\tau\_{i}<0 by assumption, the sign of d​τi∗/d​sj​td\tau\_{i}^{\*}/ds\_{jt} is determined by the sign of ∂F/∂sj​t\partial F/\partial s\_{jt}. Differentiating F​(τi;si​t,sj​t)F(\tau\_{i};s\_{it},s\_{jt}) with respect to sj​ts\_{jt} gives

|  |  |  |
| --- | --- | --- |
|  | ∂F∂sj​t=−fj,τj​sj​(sj​t,1−τi)+β​Ξ​(si​t,sj​t,τi),\displaystyle\frac{\partial F}{\partial s\_{jt}}=-f\_{j,\tau\_{j}s\_{j}}(s\_{jt},1-\tau\_{i})+\beta\,\Xi(s\_{it},s\_{jt},\tau\_{i}), |  |

where the first term captures the static effect of an increase in the teammate’s skill on the marginal productivity of assigning time to player jj, and Ξ​(⋅)\Xi(\cdot) collects the dynamic terms arising from how sj​ts\_{jt} affects future skill accumulation and the continuation value through the learning functions λi​(⋅)\lambda\_{i}(\cdot) and λj​(⋅)\lambda\_{j}(\cdot) and the value function V​(⋅)V(\cdot).

Under the natural assumption that individual skill and task time are complementary in production for player jj (i.e., fj,τj​sj>0f\_{j,\tau\_{j}s\_{j}}>0), the static term −fj,τj​sj​(sj​t,1−τi)-f\_{j,\tau\_{j}s\_{j}}(s\_{jt},1-\tau\_{i}) is negative: a higher sj​ts\_{jt} raises the marginal return to assigning time to the more skilled teammate, which ceteris paribus tilts the optimal allocation away from player ii and reduces τi∗\tau\_{i}^{\*}. By contrast, the dynamic component depends on how the skills of both players evolve over time. If the non-star player has greater potential for improvement while the superstar has already reached a plateau, the future-value term can become positive, as allocating more time to the non-star enhances overall future productivity. Moreover, if the superstar is more likely to be poached by other teams, or if their unique ability is difficult to replace, the marginal value of investing additional time in the superstar may decline relative to developing the non-star.

Thus, while allocating more time to the highly skilled player is efficient from a short-run production perspective, doing so may come at the cost of reduced learning opportunities for others. The principal therefore faces an intertemporal trade-off between maximizing current output and fostering long-term human capital development within the team. This framework highlights that reliance on superstars, although beneficial in the short term, can generate side effects by crowding out the growth of less-skilled teammates.

## 3 Data

### 3.1 Data source

We use data from the Lahman Baseball Database,111Retrieved February 25, 2025, from <http://seanlahman.com/> which provides comprehensive player-level statistics for MLB dating back to 1871, including detailed annual pitching, hitting, and fielding records as well as All-Star Game results. Our analysis focuses on position players, excluding designated hitters (DH), because the presence of fielding positions allows us to define substitution relationships with superstars in a meaningful way. In contrast, pitchers are excluded since their playing opportunities are governed by rotational schedules and role adjustments (e.g., between starting and relieving), which make substitution relationships less comparable across players.

We supplement these statistics with data on injured list (IL) placements obtained from Baseball Prospectus.222Retrieved May 3, 2025, from <https://www.baseballprospectus.com/> Baseball Prospectus provides curated and historically consistent records on MLB player transactions, including injuries and roster changes, based on official team reports and league documentation.

Our analysis covers the 1996–2019 MLB seasons. This period ensures consistency in league structure and schedule length, as the number of regular-season games per team remained fixed and no major structural changes occurred during these years.

### 3.2 Definition of superstars

Following the definition proposed by call2015stargazing, a “star” employee is characterized by (a) exceptional performance, (b) high visibility, and (c) relevant social capital. Under this framework, individuals who achieve temporary fame or visibility without consistent excellence—so-called “one-hit wonders”—do not qualify as stars.

Translating this concept into the context of MLB, we define a superstar as a player who has been selected to the All-Star Game at least twice. The All-Star Game selection serves as an observable and widely recognized indicator of both performance and reputation within MLB. Requiring at least two selections balances two potential risks: misclassifying players who achieve a single outstanding season as superstars, and excluding consistently elite players who may not have accumulated many appearances due to competition or injuries.

Using this criterion, players identified as superstars account for approximately 4.6% of all those who appeared in the MLB during the 1996–2019 seasons. This implies that fewer than 5% of players are recognized as superstars, highlighting that the definition effectively captures a small and distinct group of top performers.

This operational definition thus captures players with sustained excellence and visibility, consistent with the conceptual framework in call2015stargazing, while maintaining a sufficient number of observations for empirical analysis.

### 3.3 Summary statistics

Table [1](https://arxiv.org/html/2511.07218v1#S3.T1 "Table 1 ‣ 3.3 Summary statistics ‣ 3 Data ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.") reports the summary statistics for all players who appeared in at least one game at the season–team level between 1996 and 2019. The average number of game appearances is 68.53, with a standard deviation of 49.88, while the mean number of plate appearances per season is 235.83, with a standard deviation of 208.77. The relatively large standard deviations indicate substantial variation in playing opportunities across players—some appear in nearly all games throughout the season, whereas others participate only sporadically.

We also construct a measure of superstar exposure, Star active days, defined as the number of days during the regular season (from Opening Day to the final game) in which a superstar teammate occupying the same team and position was active, excluding periods when the superstar was on the IL. The average number of star active days per season is 65.48, while the mean value at a player’s debut season is 11.99. The lower debut-season value partly reflects differences in the underlying sample, as debut seasons include players who first appeared before 1996, when the number of games and active players per team differed from the later period.

On average, 39% of players share the same team and position with a superstar in a given season, while among debuting players the proportion is slightly higher at 41%. The average on-base plus slugging (OPS), a standard measure of batting performance, is 0.66, and the mean player age is 27.88 years. The average number of in-season transfers per player is 0.17, indicating that most players remain with the same team throughout a season. The average number of transfers involving a superstar is 0.11, reflecting the relative stability of top players’ team affiliations.

Table 1: Summary statistics

|  | N | Mean | SD | Min | Max |
| --- | --- | --- | --- | --- | --- |
| Game appearances | 14055 | 68.53 | 49.88 | 1.00 | 163.00 |
| Plate appearances | 14055 | 235.83 | 208.77 | 0.00 | 754.00 |
| Star active days | 14055 | 65.48 | 84.09 | 0.00 | 193.00 |
| Star active days at debut | 14055 | 11.99 | 43.97 | 0.00 | 193.00 |
| With star teammate | 14055 | 0.39 | 0.49 | 0.00 | 1.00 |
| With star teammate at debut | 14055 | 0.41 | 0.49 | 0.00 | 1.00 |
| OPS | 14022 | 0.66 | 0.21 | 0.00 | 5.00 |
| Age | 14055 | 27.88 | 3.79 | 19.00 | 43.00 |
| Transfer | 14055 | 0.17 | 0.42 | 0.00 | 3.00 |
| Star transfer | 14055 | 0.11 | 0.33 | 0.00 | 2.00 |

Figure [1](https://arxiv.org/html/2511.07218v1#S3.F1 "Figure 1 ‣ 3.3 Summary statistics ‣ 3 Data ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.") illustrates the distribution of game appearances by the presence of a superstar and by position. Players who share a position with a superstar are concentrated in the lower range of game appearances, while those without a superstar in the same position tend to play more frequently. Descriptively, outfielders—left field, center field, and right field—appear less affected by the presence of a superstar than infielders. Because outfielders can more easily rotate among the three outfield positions, their playing opportunities are less restricted by superstar teammates, whereas infielders, who face greater positional constraints, experience sharper reductions in playing time.

However, whether a player shares a position with a superstar is not random: it may reflect endogenous team composition and lineup decisions. In the next section, we address this concern by exploiting injury-induced variations in superstar availability as a source of exogenous shifts in playing opportunities.

![Refer to caption](figuretable/Figure1.png)


Figure 1: Distribution of game appearances by presence of a superstar and position

### 3.4 Are superstar injuries exogenous?

To treat superstar injuries as an exogenous source of variation, it is essential to rule out the possibility that injuries occur endogenously because superstars are overused when there are few capable substitutes. Directly examining the relationship between a superstar’s playing time and injury incidence would be misleading, since injuries mechanically reduce playing time. Therefore, we take an indirect approach: among players who share the same team and position with a superstar, we test whether the distribution of their abilities differs depending on whether the superstar subsequently sustained an injury.

Figure [2](https://arxiv.org/html/2511.07218v1#S3.F2 "Figure 2 ‣ 3.4 Are superstar injuries exogenous? ‣ 3 Data ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.") shows the distribution of the previous season’s OPS for players who shared a position with a superstar, separated by whether the superstar experienced an injury in the following season. Because a player’s OPS in the current season may be affected by increased playing time after a superstar’s injury, we use the previous season’s OPS as a proxy for underlying ability. The two OPS distributions largely overlap regardless of the superstar’s injury status, and the pp-value from the Mann–Whitney U test (0.500) provides no evidence of a statistically significant difference.

These results suggest that there is no observable pattern in which superstars are more likely to be injured when their teammates are less capable. This supports—at least plausibly—the assumption that superstar injuries can be treated as exogenous shocks to team composition.

![Refer to caption](figuretable/Figure2.png)


Figure 2: Distribution of previous-season OPS by superstar injury status

To further examine whether superstar injuries are systematically related to teammate ability, we regress the incidence and duration of superstar injuries on the prior season OPS of players sharing the same position, both with and without fixed effects and control variables. As shown in Table [2](https://arxiv.org/html/2511.07218v1#S3.T2 "Table 2 ‣ 3.4 Are superstar injuries exogenous? ‣ 3 Data ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123."), the coefficients on OPS are small and statistically insignificant across all specifications, suggesting no systematic relationship between teammate ability and the likelihood or length of superstar injuries.

Table 2: Relationship between superstar injuries and teammate ability

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Dependent variable: | 𝟙​(I​L>0)\mathbbm{1}(IL>0) | I​LIL | 𝟙​(I​L>0)\mathbbm{1}(IL>0) | I​LIL |
|  | (1) | (2) | (3) | (4) |
| Prior season OPS | -0.012 | -2.833 | 0.058 | 1.599 |
|  | (0.034) | (2.232) | (0.048) | (3.299) |
| Fixed effects and controls |  |  | ✓\checkmark | ✓\checkmark |
| Observations | 4505 | 4505 | 4505 | 4505 |
| R2R^{2} | 0.000 | 0.000 | 0.506 | 0.502 |
| Adjusted R2R^{2} | 0.000 | 0.000 | 0.201 | 0.195 |
| RMSE | 0.46 | 32.64 | 0.33 | 23.03 |

Notes: Columns (3) and (4) include player and team-by-year fixed effects, and control for main position, age, transfers, and superstar transfers. Robust standard errors with clustering at the team-year-position level are in parentheses.

## 4 Empirical framework

### 4.1 Effects on individual playing opportunities

To estimate the impact of superstars on their teammates’ playing opportunities, we must account for potential endogeneity in team composition. Specifically, the acquisition, retention, or release of superstars may depend on the performance of their teammates, which could lead to biased estimates in a standard OLS setting. To address this concern, we exploit variation in the number of days a superstar is active on the roster, excluding periods spent on the IL. Because injuries are plausibly exogenous to teammates’ ability and performance (as shown in Section ([3.4](https://arxiv.org/html/2511.07218v1#S3.SS4 "3.4 Are superstar injuries exogenous? ‣ 3 Data ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.")), variation in superstar active days provides a quasi-experimental source of identification for the availability of superstars.

We estimate the following OLS specification to examine how superstar availability affects teammates’ playing opportunities:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​Ai​g​t=β​S​t​a​r​A​c​t​i​v​ei​g​t+Xi​g​t​θ+μi+ηg​t+εi​g​t,\displaystyle PA\_{igt}=\beta StarActive\_{igt}+X\_{igt}\theta+\mu\_{i}+\eta\_{gt}+\varepsilon\_{igt}, |  | (1) |

where P​Ai​g​tPA\_{igt} denotes playing opportunity measured by the number of plate appearances for player ii on team gg in season tt. S​t​a​r​A​c​t​i​v​ei​g​tStarActive\_{igt} measures the number of days during the regular season that a superstar in the same team and position was active on the roster (i.e., not on the IL). If multiple superstars share the same position, the maximum value is used. This construction implies that during those periods of activity, at least one superstar competed with non-superstar teammates for playing opportunities. It is possible that while one superstar was on the IL, another remained active. Such cases would bias the estimated effect toward zero. This is because the measure would understate the extent to which teammates’ opportunities are constrained by superstar presence. Therefore, our estimates can be interpreted as providing a conservative lower bound on the true effect of superstar availability. The vector Xi​g​tX\_{igt} includes control variables such as main defensive position, age dummies, within-season transfers of player ii, and superstar transfers. μi\mu\_{i} denotes player fixed effects, and ηg​t\eta\_{gt} denotes team-by-year fixed effects, controlling for unobserved heterogeneity across players and team–year–specific shocks. Standard errors are clustered at the team–year-position level.

The coefficient of interest, β\beta, captures the marginal effect of superstar availability on a teammate’s playing opportunities. A negative value of β\beta indicates that greater superstar availability reduces the playing opportunities of non-star teammates, consistent with the idea that superstars crowd out others in the lineup.

### 4.2 Effects on career duration

To examine how exposure to superstars affects the length of players’ careers, we estimate a discrete-time hazard model, which is well suited for panel data observed at annual intervals. In our context, exit from MLB is defined at the season level, and the hazard represents the conditional probability of leaving the league between seasons.

The model is specified as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡[−log⁡(1−hi​t)]=γ0​S​t​a​r​A​c​t​i​v​ei​t0+γ1​S​t​a​r​A​c​t​i​v​ei​t+Wi​t​ζ+ηg​t,\displaystyle\log[-\log(1-h\_{it})]=\gamma\_{0}\,StarActive\_{it\_{0}}+\gamma\_{1}\,StarActive\_{it}+W\_{it}\zeta+\eta\_{gt}, |  | (2) |

where hi​th\_{it} denotes the discrete-time hazard rate—the conditional probability that player ii exits MLB in year tt, given survival up to tt. S​t​a​r​A​c​t​i​v​ei​t0StarActive\_{it\_{0}} measures the number of days per season that a superstar in the same position was active during player ii’s debut season. If several superstars shared the position, the maximum value is used. S​t​a​r​A​c​t​i​v​ei​tStarActive\_{it} represents the same measure in year tt. The vector Wi​tW\_{it} includes control variables such as main defensive position, age dummies, the presence of a superstar teammate at debut (t0t\_{0}) and in year tt, and the proportion of previous seasons with a superstar in the same position. ηg​t\eta\_{gt} denotes team-by-year fixed effects, accounting for unobserved team-level shocks. Standard errors are clustered at the team–year-position level.

The coefficients of interest are γ0\gamma\_{0} and γ1\gamma\_{1}. γ0\gamma\_{0} captures the long-term effect of initial exposure to a superstar at debut, while γ1\gamma\_{1} reflects the contemporaneous effect of superstar availability on the hazard of career exit. A positive coefficient indicates that greater superstar presence is associated with a higher exit probability, suggesting that competition with superstars shortens the careers of non-star players.

### 4.3 Superstar dependence and team production

To complement the individual-level analysis, we examine how dependence on superstars is associated with team-level performance, both in the short run and in subsequent seasons. The analysis focuses on the team-position level, which can be viewed as the smallest unit of production within a team. This level of aggregation allows us to capture how the degree of superstar dependence within a specific role relates to overall productivity in that unit over time.

We estimate the following specification:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | O​P​Sg​p,t+h\displaystyle OPS\_{gp,t+h} | =ϕ1​S​t​a​r​S​h​a​r​eg​p​t+ϕ2​E​x​i​tg​p​t+ϕ3​(S​t​a​r​S​h​a​r​eg​p​t×E​x​i​tg​p​t)\displaystyle=\phi\_{1}\,StarShare\_{gpt}+\phi\_{2}\,Exit\_{gpt}+\phi\_{3}\,(StarShare\_{gpt}\times Exit\_{gpt}) |  | (3) |
|  |  | +ψ​Δ​S​t​a​rg​p,t+h+τt+ωg​p+νg​p​t,\displaystyle\quad+\psi\,\Delta Star\_{gp,t+h}+\tau\_{t}+\omega\_{gp}+\nu\_{gpt}, |  |

where O​P​Sg​p,t+hOPS\_{gp,t+h} denotes the on-base plus slugging (OPS) for team gg at position pp in season t+ht+h (h=0,1,2,3h=0,1,2,3), capturing team-position productivity up to three years after period tt.
S​t​a​r​S​h​a​r​eg​p​tStarShare\_{gpt} represents the share of plate appearances accounted for by superstars in that team-position unit during season tt, which we interpret as a measure of superstar dependence.
E​x​i​tg​p​tExit\_{gpt} is a dummy variable equal to one if the number of superstars decreases between tt and t+1t+1, and the interaction term S​t​a​r​S​h​a​r​eg​p​t×E​x​i​tg​p​tStarShare\_{gpt}\times Exit\_{gpt} captures how reliance on superstars affects subsequent performance when those players depart. Δ​S​t​a​rg​p,t+h\Delta Star\_{gp,t+h} measures the change in the number of superstars between t+1t+1 and t+ht+h (h=2,3h=2,3). The specification includes season fixed effects (τt\tau\_{t}) and team–position fixed effects (ωg​p\omega\_{gp}), and standard errors are clustered at the team level.

In the case of h=0h=0, the coefficient ϕ1\phi\_{1} captures the contemporaneous association between superstar dependence and team-position performance. A positive value of ϕ1\phi\_{1} is expected, as relying on superstars typically enhances immediate productivity through their superior skills and experience. The coefficient ϕ2\phi\_{2} reflects the effect of a superstar’s departure between seasons tt and t+1t+1, which is expected to be negative if losing a superstar directly lowers team performance.
Our primary interest lies in ϕ3\phi\_{3}, which indicates how teams that were more dependent on superstars perform in the years following a superstar’s exit. If ϕ3\phi\_{3} remains negative for multiple future periods (h>0h>0), it would suggest that heavy reliance on superstars hampers the accumulation of human capital among other teammates, leading to persistent adjustment costs and weaker long-term performance.

## 5 Results

### 5.1 Effects on individual playing opportunities

Table [3](https://arxiv.org/html/2511.07218v1#S5.T3 "Table 3 ‣ 5.1 Effects on individual playing opportunities ‣ 5 Results ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.") reports the estimates from Equation ([1](https://arxiv.org/html/2511.07218v1#S4.E1 "In 4.1 Effects on individual playing opportunities ‣ 4 Empirical framework ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.")). Although Equation ([1](https://arxiv.org/html/2511.07218v1#S4.E1 "In 4.1 Effects on individual playing opportunities ‣ 4 Empirical framework ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.")) focuses on plate appearances (P​APA) as the main outcome, we also estimate parallel specifications using games played (GG) and games started (G​SGS) as dependent variables to verify robustness.

The coefficients on Star active days are negative and statistically significant in all specifications. When using the full sample of non-superstar players, variation in Star active days arises from two sources: (i) differences between players who have and do not have a superstar teammate, and (ii) within-player variation in the number of days that a superstar teammate is active during a season. The first source may reflect endogenous team composition, while the second is plausibly exogenous, driven by injury-related absences of superstars. By controlling for whether a player has a superstar teammate, the specification isolates the latter source of variation—capturing the quasi-experimental effect of exogenous fluctuations in superstar availability driven by injuries.

Interpreting the magnitude, a full-season increase of 180 active days by a superstar in the same position reduces teammates’ plate appearances by roughly 51, with corresponding declines of about 12 games played and 13 games started.

When the sample is restricted to players who share a team–position unit with at least one superstar, the variation in Star active days is entirely driven by injury and thus fully exogenous. The estimates remain nearly identical in magnitude, reinforcing that the negative relationship reflects the causal crowding-out effect of superstar presence.

Table 3: Effects of superstar availability on teammates’ playing opportunities

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Sample: | All non-stars | | | Non-stars with star teammate | | |
| Dependent variable: | P​APA | GG | G​SGS | P​APA | GG | G​SGS |
|  | (1) | (2) | (3) | (4) | (5) | (6) |
| Star active days | -0.285\*\*\* | -0.068\*\*\* | -0.073\*\*\* | -0.292\*\*\* | -0.071\*\*\* | -0.074\*\*\* |
|  | (0.071) | (0.018) | (0.016) | (0.087) | (0.023) | (0.020) |
| With star teammate | ✓\checkmark | ✓\checkmark | ✓\checkmark |  |  |  |
| Observations | 14055 | 14055 | 14055 | 5506 | 5506 | 5506 |
| R2R^{2} | 0.635 | 0.602 | 0.631 | 0.688 | 0.662 | 0.684 |
| Adjusted R2R^{2} | 0.542 | 0.501 | 0.537 | 0.498 | 0.456 | 0.491 |
| RMSE | 126.19 | 31.47 | 29.58 | 105.86 | 27.43 | 24.54 |

Notes: All specifications include player and team-by-year fixed effects, and control for main position, age, transfers, and superstar transfers. Robust standard errors with clustering at the team-year-position level are in parentheses. \*\*\*, \*\*, and \* denote significance at the 1%, 5%, and 10% level, respectively.

### 5.2 Effects on career duration

Table [4](https://arxiv.org/html/2511.07218v1#S5.T4 "Table 4 ‣ 5.2 Effects on career duration ‣ 5 Results ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.") presents the results from the discrete-time hazard model. The coefficient on Star active days at debut is positive and statistically significant in Column (1), indicating that players who begin their careers alongside active superstars face a substantially higher probability of exiting MLB earlier. This result remains robust even after controlling for contemporaneous superstar availability (Star active days) and the proportion of prior seasons spent sharing a position with a superstar, which account for players’ general likelihood of being matched with star teammates throughout their careers. The coefficient in Column (3) implies that a player who was exposed to an active superstar for a full season (180 days) during their debut year faced about a 1.7 times higher hazard of exiting MLB (exp⁡(180×0.003)=1.716\exp(180\times 0.003)=1.716).

The estimated effect weakens once performance-related controls such as OPS and plate appearances are added, suggesting that the long-term impact of early exposure to superstars is partly mediated by constrained playing opportunities and slower accumulation of performance capital. In contrast, contemporaneous exposure to superstars (Star active days) shows no significant association with the exit hazard.

Overall, these results imply that early-career exposure to superstars has a persistent and adverse effect on career longevity, consistent with crowding-out mechanisms operating during formative stages of player development.

Table 4: Superstar effects on teammates’ career duration

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) | (5) |
| Star active days at debut | 0.004\*\*\* |  | 0.003\*\*\* | 0.001 | -0.002\*\* |
|  | (0.001) |  | (0.001) | (0.001) | (0.001) |
| Star active days |  | 0.001 | 0.000 | -0.000 | -0.001 |
|  |  | (0.001) | (0.001) | (0.001) | (0.001) |
| OPS |  |  |  | -3.622\*\*\* | -0.871\*\*\* |
|  |  |  |  | (0.160) | (0.128) |
| Plate appearances |  |  |  |  | -0.009\*\*\* |
|  |  |  |  |  | (0.000) |
| With star teammate at debut | ✓\checkmark |  | ✓\checkmark | ✓\checkmark | ✓\checkmark |
| With star teammate at tt |  | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark |
| Observations | 10808 | 10808 | 10808 | 10808 | 10808 |
| AIC | 9646.6 | 9655.8 | 9634.7 | 8802.9 | 7229.9 |
| BIC | 14624.4 | 14633.5 | 14627.0 | 13802.5 | 12236.8 |
| RMSE | 0.34 | 0.34 | 0.34 | 0.32 | 0.29 |

Notes: All specifications include team-by-year fixed effects, and control for main position, age, and the proportion of prior seasons spent sharing a position with a superstar. Robust standard errors with clustering at the team-year-position level are in parentheses. \*\*\*, \*\*, and \* denote significance at the 1%, 5%, and 10% level, respectively.

### 5.3 Mechanism

To this point, we have shown that debut-season exposure to active superstars significantly increases the hazard of exiting MLB. To explore the mechanism behind this relationship, we examine whether reduced playing opportunities hinder subsequent performance growth, as measured by OPS. Specifically, we conduct a mediation analysis that decomposes the total effect of superstar activity on next-season OPS into direct and indirect components operating through playing opportunities.

We estimate the following equations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | O​P​Si,g,t+1\displaystyle OPS\_{i,g,t+1} | =π1​P​Ai​g​t+π2​S​t​a​r​A​c​t​i​v​ei​g​t+Xi​g​t​θ+μi+ηg​t+ui​g​t,\displaystyle=\pi\_{1}PA\_{igt}+\pi\_{2}StarActive\_{igt}+X\_{igt}\theta+\mu\_{i}+\eta\_{gt}+u\_{igt}, |  | (4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | P​Ai​g​t\displaystyle PA\_{igt} | =β​S​t​a​r​A​c​t​i​v​ei​g​t+Xi​g​t​θ+μi+ηg​t+εi​g​t.\displaystyle=\beta StarActive\_{igt}+X\_{igt}\theta+\mu\_{i}+\eta\_{gt}+\varepsilon\_{igt}. |  | (5) |

Equation ([5](https://arxiv.org/html/2511.07218v1#S5.E5 "In 5.3 Mechanism ‣ 5 Results ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.")) is identical to Equation ([1](https://arxiv.org/html/2511.07218v1#S4.E1 "In 4.1 Effects on individual playing opportunities ‣ 4 Empirical framework ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.")), except that the sample is restricted to observations for which next-season OPS is available. Equation ([4](https://arxiv.org/html/2511.07218v1#S5.E4 "In 5.3 Mechanism ‣ 5 Results ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.")) uses next-season OPS as the dependent variable and includes both plate appearances (P​APA) and superstar active days (S​t​a​r​A​c​t​i​v​eStarActive) as explanatory variables, with the same set of control variables as in Equation ([5](https://arxiv.org/html/2511.07218v1#S5.E5 "In 5.3 Mechanism ‣ 5 Results ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.")).
The indirect effect (IE) is given by β×π1\beta\times\pi\_{1}, capturing the pathway through which reduced plate appearances affect OPS growth. The direct effect (DE) corresponds to π2\pi\_{2}, representing the residual influence of superstar activity not mediated by playing opportunities. The total effect equals D​E+I​EDE+IE.

Table [5](https://arxiv.org/html/2511.07218v1#S5.T5 "Table 5 ‣ 5.3 Mechanism ‣ 5 Results ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.") reports the estimation results for Equations ([4](https://arxiv.org/html/2511.07218v1#S5.E4 "In 5.3 Mechanism ‣ 5 Results ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.")) and ([5](https://arxiv.org/html/2511.07218v1#S5.E5 "In 5.3 Mechanism ‣ 5 Results ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.")). For readability, Plate appearances and Star active days are rescaled, but the indirect effect is computed using the original scales to ensure comparability across equations. Both coefficients forming the indirect pathway, β\beta and π1\pi\_{1}, are statistically significant, whereas the direct effect is not.

Table 5: Estimation results for the mediation analysis

|  |  |  |
| --- | --- | --- |
| Dependent variable: | O​P​St+1OPS\_{t+1} | P​APA |
|  | (1) | (2) |
| Star active days (per 180 days) | 0.001 | -51.020\*\*\* |
|  | (0.016) | (14.085) |
| Plate appearances (per 100) | 0.002\* |  |
|  | (0.001) |  |
| Observations | 12026 | 12026 |
| R2R^{2} | 0.447 | 0.647 |
| Adjusted R2R^{2} | 0.307 | 0.557 |
| RMSE | 0.15 | 125.75 |

Notes: All specifications include player and team-by-year fixed effects, and control for whether a player has a superstar teammate, main position, age, transfers, and superstar transfers. Robust standard errors with clustering at the team-year-position level are in parentheses. \*\*\*, \*\*, and \* denote significance at the 1%, 5%, and 10% level, respectively.

Table [6](https://arxiv.org/html/2511.07218v1#S5.T6 "Table 6 ‣ 5.3 Mechanism ‣ 5 Results ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123.") summarizes the decomposition into direct, indirect, and total effects. Because the mediation analysis involves two linked equations, we compute means and standard errors using 2,000 bootstrap replications clustered at the team-year-position level. The indirect effect is small but statistically significant, suggesting that exposure to superstars suppresses OPS growth through reduced playing opportunities. By contrast, the direct effect is positive but insignificant, indicating substantial heterogeneity across players.

These results imply that while some players may benefit directly from positive spillovers—such as learning from or competing with superstars—others may fail to do so, and for them, the small yet stable negative indirect effect through reduced opportunities may cumulatively lead to adverse long-term career outcomes.

Table 6: Decomposition of superstar effects on teammates’ OPS growth

|  | Direct effect | Indirect effect | Total effect |
| --- | --- | --- | --- |
| Star active days (per 180 days) | 0.0026 | -0.0011\* | 0.0015 |
|  | (0.0138) | (0.0005) | (0.0138) |

Notes: Estimates and robust standard errors in parentheses are computed using 2,000 bootstrap replications clustered at the team–year–position level. \*\*\*, \*\*, and \* denote significance at the 1%, 5%, and 10% level, respectively.

### 5.4 Superstar dependence and team performance

Finally, we examine how dependence on superstars is associated with team-position performance, as summarized in Table [7](https://arxiv.org/html/2511.07218v1#S5.T7 "Table 7 ‣ 5.4 Superstar dependence and team performance ‣ 5 Results ‣ The Long Shadow of Superstars: Effects on Opportunities, Careers, and Team Production I am grateful to Ryo Nakajima for his valuable comments and suggestions that greatly improved this paper. I thank Reio Tanji, a baseball analyst, for sharing his domain expertise and providing insightful feedback from a practitioner’s perspective. Comments from participants at the Kansai Labor Workshop (March 2025) were also helpful and are gratefully acknowledged. This work was supported by JST SPRING, Grant Number JPMJSP2123."). In Column (1), the coefficient on Star PA share is positive and statistically significant, indicating that team-position units that rely more heavily on superstars achieve higher contemporaneous OPS in the same season (h=0h=0). The coefficient on Star exit is negative across columns, including for h=0h=0, implying that team-position units in which the number of superstars will fall between tt and t+1t+1 already exhibit lower OPS in year tt. Thus, these units appear to be on a weaker performance trajectory even before the superstar actually leaves.

The interaction term Star PA share ×\times Star exit becomes negative and statistically significant for h=1h=1 and h=2h=2, showing that among positions that lose a superstar, those that were more dependent on superstars suffer a larger relative decline in OPS in the exit year and the following season. This pattern is consistent with the idea that heavy superstar dependence leaves fewer well-prepared substitutes, so the productivity cost of losing a superstar is greater where their role was more concentrated.

By contrast, for h=3h=3 the interaction term is no longer significant, suggesting that these negative effects do not persist indefinitely. Over a horizon of roughly three seasons, teams appear able to adjust—through internal development, roster moves, or changes in role allocation—and close much of the performance gap created by the lack of well-prepared substitutes.

Table 7: Superstar dependence and team-position performance

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Dependent variable: | O​P​StOPS\_{t} | O​P​St+1OPS\_{t+1} | O​P​St+2OPS\_{t+2} | O​P​St+3OPS\_{t+3} |
|  | (1) | (2) | (3) | (4) |
| Star PA share | 0.090\*\*\* | 0.051\*\*\* | 0.038\*\*\* | 0.023\*\*\* |
|  | (0.005) | (0.007) | (0.006) | (0.006) |
| Star exit at t+1t+1 | -0.038\*\*\* | -0.016\*\*\* | -0.014\*\*\* | -0.012\*\* |
|  | (0.005) | (0.006) | (0.005) | (0.005) |
| Star PA share ×\times star exit at t+1t+1 | 0.006 | -0.028\* | -0.023\*\* | 0.004 |
|  | (0.012) | (0.015) | (0.010) | (0.012) |
| Post-exit Δ\Delta stars (h=2h=2) |  |  | ✓\checkmark |  |
| Post-exit Δ\Delta stars (h=3h=3) |  |  |  | ✓\checkmark |
| Observations | 4296 | 4296 | 4296 | 4296 |
| R2R^{2} | 0.382 | 0.299 | 0.284 | 0.281 |
| Adjusted R2R^{2} | 0.373 | 0.290 | 0.274 | 0.270 |
| RMSE | 0.07 | 0.07 | 0.07 | 0.07 |

Notes: All specifications include year and team-position fixed effects. Robust standard errors with clustering at the team level are in parentheses. \*\*\*, \*\*, and \* denote significance at the 1%, 5%, and 10% level, respectively.

## 6 Conclusion

This study examines how the presence of superstars affects the playing opportunities and subsequent career outcomes of their teammates, using panel data from MLB. To address potential endogeneity in team composition, the analysis exploits plausibly exogenous variation in superstar availability generated by injuries, allowing us to identify how changes in superstar activity influence teammates’ opportunities and longer-term performance.

At the individual level, we find that when a superstar is active in the same team-position unit, non-star teammates experience significantly fewer playing opportunities. Early-career exposure to superstars also has persistent consequences: players who begin their careers alongside a superstar who remains active for a full season are about 1.7 times more likely to exit MLB earlier than comparable peers. This suggests that competition with superstars during formative years can have lasting effects on career longevity.

To understand the mechanism behind this pattern, we analyze whether the presence of superstas hinders subsequent performance growth. The results show that exposure to superstars suppresses the next season’s OPS growth through reduced playing time, consistent with constrained opportunities for human capital accumulation. The direct effect of exposure, by contrast, is statistically insignificant, suggesting that positive spillovers—such as learning from or being motivated by superstars—are limited or highly heterogeneous across players.

At the team level, we examine how dependence on superstars relates to team-position productivity. Although this analysis does not establish strict causality, the estimates reveal patterns consistent with theoretical expectations. Units that rely more heavily on superstars achieve higher short-term performance but experience larger declines in productivity when those superstars depart, particularly in the following two seasons. In the MLB context, these negative effects dissipate after about three years, likely reflecting the league’s institutional mechanisms—such as the draft system—that promote roster renewal and competitive balance. In other industries lacking such mechanisms, however, over-reliance on star performers may produce more persistent and structural productivity losses.

These findings highlight two important implications. First, at the individual level, competing directly with superstars can limit on-the-job learning and reduce opportunities to accumulate human capital, with potential long-term career costs. While knowledge spillovers from high performers may exist, in settings where experiential learning and task repetition are critical, direct competition with stars may hinder development.
Second, at the organizational level, superstar dependence generates a trade-off between short-term gains and long-term adaptability. Teams benefit immediately from concentrating key roles in top performers but risk undermining the growth of others and weakening resilience when those stars leave. Where future depth and continuity are important—such as in organizations vulnerable to turnover or poaching—the long-term costs of superstar dependence may outweigh its short-term benefits.