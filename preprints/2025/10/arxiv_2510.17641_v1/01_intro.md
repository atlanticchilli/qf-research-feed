---
authors:
- László Csató
- Dóra Gréta Petróczy
doc_id: arxiv:2510.17641v1
family_id: arxiv:2510.17641
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Are penalty shootouts better than a coin toss? Evidence from European football
url_abs: http://arxiv.org/abs/2510.17641v1
url_html: https://arxiv.org/html/2510.17641v1
venue: arXiv q-fin
version: 1
year: 2025
---


[László Csató](https://sites.google.com/view/laszlocsato)
    
[Dóra Gréta Petróczy](https://sites.google.com/view/doragretapetroczy)
 Corresponding author
  
E-mail: *laszlo.csato@sztaki.hun-ren.hu*
  
Institute for Computer Science and Control (SZTAKI), Hungarian Research Network (HUN-REN), Laboratory on Engineering and Management Intelligence, Research Group of Operations Research and Decision Systems, Budapest, Hungary
  
Corvinus University of Budapest (BCE), Institute of Operations and Decision Sciences, Department of Operations Research and Actuarial Sciences, Budapest, Hungary E-mail: *apetroczy@metropolitan.hu*
  
MNB Institute, Budapest Metropolitan University, Budapest, Hungary

(20th October 2025)

###### Abstract

Penalty shootouts play an important role in the knockout stage of major football tournaments, especially since the 2021/22 season, when the Union of European Football Associations (UEFA) scrapped the away goals rule in its club competitions. Inspired by this rule change, our paper examines whether the outcome of a penalty shootout can be predicted in UEFA club competitions. Based on all shootouts between 2000 and 2025, we find no evidence for the effect of the kicking order, the field of the match, and psychological momentum. In contrast to previous results, stronger teams, defined first by Elo ratings, do not perform better than their weaker opponents. Consequently, penalty shootouts are equivalent to a perfect lottery in top European football.

“*The outcome of penalty shoot-outs is often referred to as a “lottery”, suggesting that luck, rather than the skill level of the player, predetermines outcome success.*”111 Source: Wood et al., ([2015](https://arxiv.org/html/2510.17641v1#bib.bib39), Abstract).

Keywords: Elo rating; football; home advantage; momentum; penalty shootout

*MSC* class: 62P20, 90B90

*JEL* classification number: D79, Z20

## 1 Introduction

The penalty shootout is the ultimate tie-breaking rule in (association) football and several other sports to decide which team qualifies in a knockout match. Penalty shootouts are usually kicked if the result is tied in both regular and extra time. Penalty shootouts directly follow regular time in some tournaments, too. For instance, in the 2025 Leagues Cup, games went straight to a penalty shootout after a tie, and teams were awarded three points for a win in regular time, two points for a win by a penalty shootout, and one point for a loss by a penalty shootout (Leagues Cup,, [2025](https://arxiv.org/html/2510.17641v1#bib.bib28)).

Penalty shootouts are the subject of serious academic interest since Apesteguia and Palacios-Huerta, ([2010](https://arxiv.org/html/2510.17641v1#bib.bib4)) has appeared in a leading economic journal, the *American Economic Review*, one and a half decades ago (see Section [2](https://arxiv.org/html/2510.17641v1#S2 "2 Related literature ‣ Are penalty shootouts better than a coin toss? Evidence from European football")). In particular, the authors found a systematic first-mover advantage; the team kicking the first penalty has a significantly higher probability of winning the penalty shootout than its opponent.

The present paper contributes to this discussion by investigating four research questions:

1. 1.

   Does the shooting order affect the outcome of a penalty shootout?
2. 2.

   Does the field of the match affect the outcome of a penalty shootout?
3. 3.

   Does psychological momentum affect the outcome of a penalty shootout?
4. 4.

   Does the strength of the teams affect the outcome of a penalty shootout?

All of these issues have partially been investigated in the existing literature, as revealed by Section [2](https://arxiv.org/html/2510.17641v1#S2 "2 Related literature ‣ Are penalty shootouts better than a coin toss? Evidence from European football").
However, our research has three innovative aspects.
First, we analyse a relatively homogeneous sample provided by matches played in UEFA club competitions without any matches from national cups, where the strengths of the opponents can vary widely.
Second, the comeback team is identified in a novel way, according to which team scored the last goal.
Third, team strength is measured by Football Club Elo Ratings, a well-established statistical method to create ratings based on past performance (Aldous,, [2017](https://arxiv.org/html/2510.17641v1#bib.bib1); Gomes de Pinho Zanco et al.,, [2024](https://arxiv.org/html/2510.17641v1#bib.bib23); van Eetvelde and Ley,, [2019](https://arxiv.org/html/2510.17641v1#bib.bib35)). Previous studies used either the division of the team (Arrondel et al.,, [2019](https://arxiv.org/html/2510.17641v1#bib.bib5); Krumer,, [2020](https://arxiv.org/html/2510.17641v1#bib.bib26)), or betting odds (Wunderlich et al.,, [2020](https://arxiv.org/html/2510.17641v1#bib.bib40); Pipke,, [2025](https://arxiv.org/html/2510.17641v1#bib.bib32)) for this purpose. But the first approach is inappropriate in international competitions, while betting odds suffer from several biases (Braun and Kvasnicka,, [2013](https://arxiv.org/html/2510.17641v1#bib.bib10); Cain et al.,, [2000](https://arxiv.org/html/2510.17641v1#bib.bib11); Feddersen et al.,, [2017](https://arxiv.org/html/2510.17641v1#bib.bib20); Winkelmann et al.,, [2021](https://arxiv.org/html/2510.17641v1#bib.bib38)), and may be less persuasive for decision-makers than a measure given by an “objective” mathematical formula.

As we show, the outcomes of the 268 penalty shootouts played in UEFA club competitions between 2000 and 2025 seem to be entirely unpredictable. This contradicts the results of some previous works, which uncover a first-mover advantage (Apesteguia and Palacios-Huerta,, [2010](https://arxiv.org/html/2510.17641v1#bib.bib4); Palacios-Huerta,, [2014](https://arxiv.org/html/2510.17641v1#bib.bib30); Da Silva et al.,, [2018](https://arxiv.org/html/2510.17641v1#bib.bib17); Rudi et al.,, [2020](https://arxiv.org/html/2510.17641v1#bib.bib33)) and the positive impact of psychological momentum (Krumer,, [2021](https://arxiv.org/html/2510.17641v1#bib.bib27)). Furthermore, according to our knowledge, *all* existing studies agree that stronger teams are more likely to win in a shootout (Arrondel et al.,, [2019](https://arxiv.org/html/2510.17641v1#bib.bib5); Krumer,, [2020](https://arxiv.org/html/2510.17641v1#bib.bib26); Wunderlich et al.,, [2020](https://arxiv.org/html/2510.17641v1#bib.bib40); Pipke,, [2025](https://arxiv.org/html/2510.17641v1#bib.bib32)).

Our findings could be especially important for the Union of European Football Associations (UEFA) when they decide on rule changes in the future.
In 2021, UEFA abolished the so-called away goals rule, which awarded the prize (qualification for the next round) in a two-legged match to the team that scored more away goals. This change has increased the probability of reaching a penalty shootout by approximately ten percentage points, from below 5% to nearly 15% (Forrest et al.,, [2025](https://arxiv.org/html/2510.17641v1#bib.bib22)).
In addition, UEFA has recently given serious consideration to removing extra time in order to ease the burden of the best players (Ames,, [2025](https://arxiv.org/html/2510.17641v1#bib.bib2)). Since a penalty shootout is equivalent to a perfect lottery in UEFA club competitions, such a measure would favour weaker teams and teams playing away, level the playing field, and decrease the dominance of the top clubs.

The paper is structured as follows.
An overview of related studies is given in Section [2](https://arxiv.org/html/2510.17641v1#S2 "2 Related literature ‣ Are penalty shootouts better than a coin toss? Evidence from European football"). Materials and methods are presented in Section [3](https://arxiv.org/html/2510.17641v1#S3 "3 Data and methodology ‣ Are penalty shootouts better than a coin toss? Evidence from European football"). Section [4](https://arxiv.org/html/2510.17641v1#S4 "4 Results and discussion ‣ Are penalty shootouts better than a coin toss? Evidence from European football") reveals and discusses the results, while Section [5](https://arxiv.org/html/2510.17641v1#S5 "5 Concluding remarks ‣ Are penalty shootouts better than a coin toss? Evidence from European football") concludes.

## 2 Related literature

The issue of first-mover advantage in football penalty shootouts has received serious attention since the pioneering work of Apesteguia and Palacios-Huerta, ([2010](https://arxiv.org/html/2510.17641v1#bib.bib4)). Some studies find evidence for a significant advantage enjoyed by the team that kicks the first penalty in each round (Apesteguia and Palacios-Huerta,, [2010](https://arxiv.org/html/2510.17641v1#bib.bib4); Palacios-Huerta,, [2014](https://arxiv.org/html/2510.17641v1#bib.bib30); Da Silva et al.,, [2018](https://arxiv.org/html/2510.17641v1#bib.bib17); Rudi et al.,, [2020](https://arxiv.org/html/2510.17641v1#bib.bib33)). These results have inspired formal modelling of the first-mover advantage, as well as several proposals for alternative mechanisms to mitigate or even eliminate this source of unfairness (Palacios-Huerta,, [2012](https://arxiv.org/html/2510.17641v1#bib.bib29); Echenique,, [2017](https://arxiv.org/html/2510.17641v1#bib.bib19); Brams and Ismail,, [2018](https://arxiv.org/html/2510.17641v1#bib.bib8); Vandebroek et al.,, [2018](https://arxiv.org/html/2510.17641v1#bib.bib36); Del Giudice,, [2019](https://arxiv.org/html/2510.17641v1#bib.bib18); Anbarcı et al.,, [2021](https://arxiv.org/html/2510.17641v1#bib.bib3); [Csató, 2021a,](https://arxiv.org/html/2510.17641v1#bib.bib12) ; [Csató, 2021b,](https://arxiv.org/html/2510.17641v1#bib.bib13) ; Csató and Petróczy,, [2022](https://arxiv.org/html/2510.17641v1#bib.bib16); Brams et al.,, [2024](https://arxiv.org/html/2510.17641v1#bib.bib9)). The alternating (or ABBA) order was even tried in various tournaments between 2017 and 2018 (Palacios-Huerta,, [2020](https://arxiv.org/html/2510.17641v1#bib.bib31); [Csató, 2021a,](https://arxiv.org/html/2510.17641v1#bib.bib12) ), albeit the IFAB (International Football Association Board), the rule-making body of football, stopped the experiments in 2018 (FIFA,, [2018](https://arxiv.org/html/2510.17641v1#bib.bib21)).

On the other hand, several papers report no significant difference between the winning probability of the first-mover and the second-mover (Kocher et al.,, [2012](https://arxiv.org/html/2510.17641v1#bib.bib25); Arrondel et al.,, [2019](https://arxiv.org/html/2510.17641v1#bib.bib5); Santos,, [2023](https://arxiv.org/html/2510.17641v1#bib.bib34)). Kassis et al., ([2021](https://arxiv.org/html/2510.17641v1#bib.bib24)) conclude that teams whose captains win the coin toss and can choose the shooting order enjoy the advantage. The conflicting results can probably be attributed to small sample sizes (Vandebroek et al.,, [2018](https://arxiv.org/html/2510.17641v1#bib.bib36)). Two recent studies (Vollmer et al.,, [2024](https://arxiv.org/html/2510.17641v1#bib.bib37); Pipke,, [2025](https://arxiv.org/html/2510.17641v1#bib.bib32)) analysing the highest number of penalty shootouts with respect to first-mover advantage—1759 and 7116, respectively—do not find evidence for the effect of the shooting sequence. However, while the dataset of Pipke, ([2025](https://arxiv.org/html/2510.17641v1#bib.bib32)) includes all available shootouts up to the 2023/24 season, this does not mean that first-mover advantage cannot emerge in a more homogeneous subset of matches.

Regarding the existence of a penalty-specific home advantage, Apesteguia and Palacios-Huerta, ([2010](https://arxiv.org/html/2510.17641v1#bib.bib4)) show no difference in the chances of home and away teams for 129 shootouts between 1976 and 2003. Kocher et al., ([2012](https://arxiv.org/html/2510.17641v1#bib.bib25)) reinforce this based on 540 shootouts between 1970 and 2003. Analogously, playing at home does not influence the probability of winning in 252 shootouts from French cup competitions (Arrondel et al.,, [2019](https://arxiv.org/html/2510.17641v1#bib.bib5)).
The results of Wunderlich et al., ([2020](https://arxiv.org/html/2510.17641v1#bib.bib40)) suggest no home advantage in 1067 penalty shootouts that took place between 2004 and 2018. The logistic regression of Bahamonde-Birke and Bahamonde-Birke, ([2023](https://arxiv.org/html/2510.17641v1#bib.bib6)) based on a sample of 471 shootouts demonstrates the absence of such an effect, too.

We know only one study on the impact of psychological momentum. Krumer, ([2021](https://arxiv.org/html/2510.17641v1#bib.bib27)) analyses 214 penalty shootouts from two-legged matches in European cups (European Champion Clubs’ Cup/UEFA Champions League, European Cup Winners’ Cup/UEFA Cup Winners’ Cup, UEFA Cup/UEFA Europa League) between 1970 and 2018. Every additional goal scored by the away team in regular time in the second leg increases its probability of winning the penalty shootout by 12.5 percentage points. However, if the home team wins in regular time, it has only a 50% chance to qualify after a shootout.

Arrondel et al., ([2019](https://arxiv.org/html/2510.17641v1#bib.bib5)) reveal that the team playing at a higher level than its opponent wins the penalty shootout with an approximately 20% higher probability. Analogously, a team from a higher division has a significantly higher chance to win according to Krumer, ([2020](https://arxiv.org/html/2510.17641v1#bib.bib26)): a difference in one league translates to a gap of 8 percentage points in winning probabilities. For instance, a team from the first division defeats its opponent from the second division with a probability of 54%. The author studies 586 shootouts in the cup competitions of the top five European football nations (England, France, Germany, Italy, Spain) between 1979 and 2018.

Stronger football teams have a significantly higher chance to win a penalty shootout based on 1067 shootouts from the domestic cup competitions of ten European associations (the top five, as well as Belgium, Portugal, Russia, Turkey, Ukraine), the Brazilian cup, the UEFA Champions League, and the UEFA Europa League (Wunderlich et al.,, [2020](https://arxiv.org/html/2510.17641v1#bib.bib40)). However, the effect of team strength on success remains rather small; the winning probability does not exceed 60% even against an extremely weak team. The novelty of Wunderlich et al., ([2020](https://arxiv.org/html/2510.17641v1#bib.bib40)) resides in the measure of strength difference, determined by winning probabilities based on pre-match betting odds, adjusted for home advantage.
The recent analysis of all available penalty shootouts until the 2023/24 season reinforces that the favourites identified by pre-match odds are more likely to win (Pipke,, [2025](https://arxiv.org/html/2510.17641v1#bib.bib32), Table A.5). But the favourite team might not be the stronger team due to home advantage (Wunderlich et al.,, [2020](https://arxiv.org/html/2510.17641v1#bib.bib40)).

To summarise, *all* studies considering the strength of teams find at least some bias towards the stronger team in winning penalty shootouts. In other words, penalty shootouts are not equivalent to a pure coin toss; ability is an important success factor even for a mechanical task carried out in a high-pressure environment.

## 3 Data and methodology

Table 1: Penalty shootouts in UEFA club competitions from the 2000/01 season to 2025

Champions League


Europa League


Conference League


Total


Qualification


41


103


63


207

Knockout stage


14


27


9


50

Final


6


5


0


11

Total


61


135


72


268

•

UEFA Conference League was called UEFA Europa Conference League until the 2023/24 season.
•

Knockout stage matches contain only two-legged matches, but not the final, which is played on a neutral field.

We have collected data from all penalty shootouts that took place in UEFA club competitions, including their qualifiers, from the 2000/01 season until the end of 2025. In the 2025/26 season, only the qualification matches are considered since the knockout stage of this season is played only in 2026.
Table [1](https://arxiv.org/html/2510.17641v1#S3.T1 "Table 1 ‣ 3 Data and methodology ‣ Are penalty shootouts better than a coin toss? Evidence from European football") summarises the distribution of shootouts across the three tournaments, as well as across their stages. The final is distinguished from other knockout stage matches because it consists of one game played at a neutral venue and is not the usual two-legged match, where one team plays at home in a second leg.

200020002002200220042004200620062008200820102010201220122014201420162016201820182020202020222022202420240101020203030SeasonNumber of penalty shootouts


Figure 1: Number of penalty shootouts in UEFA club competitions in each season
  
*Note*: Seasons are identified by their starting year.

Figure [1](https://arxiv.org/html/2510.17641v1#S3.F1 "Figure 1 ‣ 3 Data and methodology ‣ Are penalty shootouts better than a coin toss? Evidence from European football") presents the number of penalty shootouts in each season from 2000/01 to 2025/26 (in the latter case, without the spring of 2026). Besides the natural fluctuation, a dramatic increase can be seen from 2020/21, when most qualification matches were played in one leg instead of two due to COVID-19 restrictions such that the field of the match was decided by a random draw. In addition, the away goals rule was abolished, and a new competition, the UEFA (Europa) Conference League, started in 2021/22. Therefore, our sample is dominated by recent matches over these 25 years: 139 of the 268 penalty shootouts (51.9%) took place in the last six seasons.

For all matches decided by a penalty shootout, the dataset contains
(a) the time of the match;
(b) the round of the game in the tournament;
(c) the names of both teams;
(d) the location of the match;
(e) the number of goals scored by both teams in the match;
(f) the name of the team that scored the last goal in regular or extra time (if relevant);
(g) the team that kicked the first penalty (first-mover).

The first-mover advantage can be analysed on the basis of all (268) penalty shootouts since this information is always available.
On the other hand, some matches were played on a neutral field. In order to examine home advantage, we consider two sets of matches, an extended and a restricted set, where the latter is a strict subset of the former. The extended set does not contain the finals except for the 2011/12 UEFA Champions League final, which was played in München by Bayern München and Chelsea (10 matches are dropped). In addition, one match played by an Israeli and two matches played by Belarussian teams in 2024 and 2025 are disregarded, which leads to 255 matches in the extended set. In the restricted set, 20 matches played behind closed doors in the 2020/21 season, as well as the 2011/12 UEFA Champions League final, are removed.

We identify a comeback team in two different ways. The first adopts the method of Krumer, ([2021](https://arxiv.org/html/2510.17641v1#bib.bib27)): the team that scored more goals than its opponent in the match is the comeback team. Consequently, 121 matches where the second leg game is tied should be ignored.
The second approach is novel: the team that scored the last equalising goal, which is responsible for reaching the penalty shootout, is the comeback team. Hence, only 37 shootouts could not be examined.

The strengths of teams are quantified by Football Club Elo Ratings (<http://clubelo.com>). Csató, ([2024](https://arxiv.org/html/2510.17641v1#bib.bib15)) shows that this measure of strength predicts the results of the UEFA Champions League more accurately than the official UEFA club coefficient. Unsurprisingly, Football Club Elo Ratings are widely used in the literature, too (Bosker and Gürtler,, [2024](https://arxiv.org/html/2510.17641v1#bib.bib7); Csató,, [2022](https://arxiv.org/html/2510.17641v1#bib.bib14); [Yildirim and Bilman, 2025a,](https://arxiv.org/html/2510.17641v1#bib.bib41) ; [Yildirim and Bilman, 2025b,](https://arxiv.org/html/2510.17641v1#bib.bib42) ). They are available for all penalty shootouts, although we have found a problem in the database of Football Club Elo Ratings (see Appendix [A.1](https://arxiv.org/html/2510.17641v1#Sx2.SS1 "A.1 A mistake in Football Club Elo Ratings data ‣ Appendix ‣ Are penalty shootouts better than a coin toss? Evidence from European football") for details). Thus, the impact of the difference in team strength is studied based on 266 penalty shootouts in the baseline, because two Elo ratings are inaccurate.
As a robustness check, we also use different thresholds tt: a match is retained in the sample only if the difference between the Elo ratings exceeds tt.

All research questions are first investigated by a two-sided binomial test.
The number of penalty shootout wins and losses is calculated for the first-mover, the home team (two cases depending on the definition of neutral field), the comeback team (two cases depending on the type of psychological momentum), and the stronger team (five cases depending on the minimal threshold tt).

The connection between the relative strength of teams and the probability of winning the penalty shootout is assessed by logistic regressions, too. The binary dependent variable is the home win/loss.
Denote the Elo rating of the home and the away team by EiE\_{i} and EjE\_{j}, respectively. The only independent variable Δi​j\Delta\_{ij} is either the difference of Elo ratings (Δi​j(1)=Ei−Ej\Delta\_{ij}^{(1)}=E\_{i}-E\_{j}), or the winning probability implied by the Elo ratings according to the Elo equation of Football Club Elo Ratings (<http://clubelo.com/system>):

|  |  |  |
| --- | --- | --- |
|  | Δi​j(2)=11+10−(Ei−Ej)/400.\Delta\_{ij}^{(2)}=\frac{1}{1+10^{-(E\_{i}-E\_{j})/400}}. |  |

Note that Δj​i(1)=−Δi​j(1)\Delta\_{ji}^{(1)}=-\Delta\_{ij}^{(1)} and Δj​i(2)=1−Δi​j(2)\Delta\_{ji}^{(2)}=1-\Delta\_{ij}^{(2)}.

To summarise, the following equation is estimated:

|  |  |  |
| --- | --- | --- |
|  | Ph=11+eβ0+β1​Δ,P\_{h}=\frac{1}{1+e^{\beta\_{0}+\beta\_{1}\Delta}}, |  |

where PhP\_{h} is the probability that the home team wins the penalty shootout, and Δ\Delta is the strength difference of the opposing teams. Matches played at a neutral venue are considered according to the designated home team.

a Difference in Elo ratings Δ(1)\Delta^{(1)}

−-700–−-650−-650–−-600−-600–−-550−-550–−-500−-500–−-450−-450–−-400−-400–−-350−-350–−-300−-300–−-250−-250–−-200−-200–−-150−-150–−-100−-100–−-50−-50–00–5050–100100–150150–200200–250250–300300–350350–400400–450450–5000101020203030Home team Elo rating minus away team Elo ratingNumber of penalty shootouts

b Difference in winning probabilities Δ(2)\Delta^{(2)}

0–0.050.05–0.10.1–0.150.15–0.20.2–0.250.25–0.30.3–0.350.35–0.40.4–0.450.45–0.50.5–0.550.55–0.60.6–0.650.65–0.70.7–0.750.75–0.80.8–0.850.85–0.90.9–0.950.95–1010102020Home team winning probability minus away team winning probabilityNumber of penalty shootouts

Figure 2: Distribution of the difference between team strengths

Figure [2](https://arxiv.org/html/2510.17641v1#S3.F2 "Figure 2 ‣ 3 Data and methodology ‣ Are penalty shootouts better than a coin toss? Evidence from European football") shows histograms of strength difference Δ\Delta: Figure [2.a](https://arxiv.org/html/2510.17641v1#S3.F2.sf1 "In Figure 2 ‣ 3 Data and methodology ‣ Are penalty shootouts better than a coin toss? Evidence from European football") if the difference is measured directly by Elo ratings (Δ(1)\Delta^{(1)}), and Figure [2.b](https://arxiv.org/html/2510.17641v1#S3.F2.sf2 "In Figure 2 ‣ 3 Data and methodology ‣ Are penalty shootouts better than a coin toss? Evidence from European football") if it is based on the implied winning probabilities (Δ(2)\Delta^{(2)}). Although all matches are decided by a penalty shootout, the database is quite heterogeneous, the winning probability of the home team lies between 40% and 60% in less than 30% of the sample.

Wunderlich et al., ([2020](https://arxiv.org/html/2510.17641v1#bib.bib40)) warn that, although the logistic regression provides information about the connection between team strength and the outcome of the penalty shootout, this is an in-sample approach, which may suffer from overfitting. Since our results are strongly insignificant (see Section [4](https://arxiv.org/html/2510.17641v1#S4 "4 Results and discussion ‣ Are penalty shootouts better than a coin toss? Evidence from European football")), we are not worried about this potential bias.

## 4 Results and discussion

First-mover winHome win (extended)Home win (restricted)Comeback win (all)Comeback win (last)40404545505055556060Probability (%)


Figure 3: Binomial tests: first-mover advantage, home advantage, momentum
  
*Note*: The dashed lines show the bounds of the 95% confidence interval around no advantage of 50% in a two-sided test.

Figure [3](https://arxiv.org/html/2510.17641v1#S4.F3 "Figure 3 ‣ 4 Results and discussion ‣ Are penalty shootouts better than a coin toss? Evidence from European football") shows the results of five binomial tests that examine the effect of the shooting sequence, the match venue according to two definitions (mild and strict) of home field, as well as psychological momentum according to two assumptions again. None of them is significant even at the 10% level. Thus, our study joins the set of papers that find no impact of the shooting order, and are fully in line with the literature on home advantage in penalty shootouts. In contrast to Krumer, ([2021](https://arxiv.org/html/2510.17641v1#bib.bib27), Table 4), comeback teams do not win more than 50% of penalty shootouts.
These calculations can be reproduced on the basis of Table [A.1](https://arxiv.org/html/2510.17641v1#Sx2.T1 "Table A.1 ‣ A.2 Supplementary tables ‣ Appendix ‣ Are penalty shootouts better than a coin toss? Evidence from European football") in Appendix [A.2](https://arxiv.org/html/2510.17641v1#Sx2.SS2 "A.2 Supplementary tables ‣ Appendix ‣ Are penalty shootouts better than a coin toss? Evidence from European football"), which also reports the associated pp-values.

Elo difference >0>0Elo difference >25>25Elo difference >50>50Elo difference >75>75Elo difference >100>10040404545505055556060Probability (%)


Figure 4: Binomial tests: team strength
  
*Note*: The dashed lines show the bounds of the 95% confidence interval around no advantage of 50% in a two-sided test.

Figure [4](https://arxiv.org/html/2510.17641v1#S4.F4 "Figure 4 ‣ 4 Results and discussion ‣ Are penalty shootouts better than a coin toss? Evidence from European football") focuses on the winning probability of the stronger team based on Football Club Elo Ratings. Five definitions of the favourite are used by gradually restricting the sample according to the minimal difference in the Elo ratings of the two teams. However, even teams that have at least 100 points more than their opponents fail to win 50% of their penalty shootouts.
These calculations can be reproduced on the basis of Table [A.2](https://arxiv.org/html/2510.17641v1#Sx2.T2 "Table A.2 ‣ A.2 Supplementary tables ‣ Appendix ‣ Are penalty shootouts better than a coin toss? Evidence from European football") in Appendix [A.2](https://arxiv.org/html/2510.17641v1#Sx2.SS2 "A.2 Supplementary tables ‣ Appendix ‣ Are penalty shootouts better than a coin toss? Evidence from European football"), which also reports the associated pp-values.

Table 2: Logistic regression models: the effect of and team strength

Strength difference Δ\Delta


Elo rating (Δ(1)\Delta^{(1)})


Winning probability (Δ(2)\Delta^{(2)})



Coefficient


−-0.121


−-0.027

β0\beta\_{0}
Standard error


0.123


0.307


pp-value


0.326


0.930


Coefficient


−-0.004


−-0.194

β1\beta\_{1}
Standard error


0.069


0.582


pp-value


0.959


0.739

Number of observations


266


266

•

In the model Elo rating, strength difference Δ(1)\Delta^{(1)} is the Elo rating of the home team minus the Elo rating of the away team divided by 100.
•

In the model Elo rating, strength difference Δ(2)\Delta^{(2)} is the winning probability of the home team based on the Elo ratings of the two teams.
•

Significance: \* p<5%p<5\%; \*\* p<1%p<1\%; \*\*\* p<0.1%p<0.1\%.

The lack of positive impact is in stark contrast to the findings of the previous literature: all existing papers (Arrondel et al.,, [2019](https://arxiv.org/html/2510.17641v1#bib.bib5); Krumer,, [2020](https://arxiv.org/html/2510.17641v1#bib.bib26); Wunderlich et al.,, [2020](https://arxiv.org/html/2510.17641v1#bib.bib40); Pipke,, [2025](https://arxiv.org/html/2510.17641v1#bib.bib32)) demonstrate a significantly higher winning probability for a “sufficiently” stronger team.
Thus, Table [2](https://arxiv.org/html/2510.17641v1#S4.T2 "Table 2 ‣ 4 Results and discussion ‣ Are penalty shootouts better than a coin toss? Evidence from European football") investigates the same issue by logistic regressions similar to Wunderlich et al., ([2020](https://arxiv.org/html/2510.17641v1#bib.bib40)). Both coefficients are insignificant, that is, neither the field of the match nor the strength of the teams influence success in penalty shootouts, independent of how strength difference is measured. Furthermore, the estimations of β0\beta\_{0} and β1\beta\_{1} are negative in accordance with Figures [3](https://arxiv.org/html/2510.17641v1#S4.F3 "Figure 3 ‣ 4 Results and discussion ‣ Are penalty shootouts better than a coin toss? Evidence from European football") and [4](https://arxiv.org/html/2510.17641v1#S4.F4 "Figure 4 ‣ 4 Results and discussion ‣ Are penalty shootouts better than a coin toss? Evidence from European football"), making the implications regarding home advantage and team strength even more robust.

a Strength difference Δ(1)\Delta^{(1)}: Elo rating of the home team minus Elo rating of the away team

200020002002200220042004200620062008200820102010201220122014201420162016201820182020202020222022202420240.010.010.10.111Starting year of the first season in the estimationpp-valuepp-value of the coefficient β0\beta\_{0} for the constant   pp-value of the coefficient β1\beta\_{1} for Δ\Delta

b Strength difference Δ(2)\Delta^{(2)}: winning probability of the home team based on Elo ratings

200020002002200220042004200620062008200820102010201220122014201420162016201820182020202020222022202420240.010.010.10.111Starting year of the first season in the estimationpp-valuepp-value of the coefficient β0\beta\_{0} for the constant   pp-value of the coefficient β1\beta\_{1} for Δ\Delta

Figure 5: Logistic regressions: Sensitivity of pp-values to the first season of the sample
  
*Notes*: The dotted (dashed) line shows significance at 5% (1%) level.
  
Seasons are identified by their starting year.

Last but not least, we have assessed whether team strength could have a significant effect if the sample is restricted to the recent seasons. Hence, 26 logistic regressions are estimated in both versions such that the sample begins in the 20xx/20xx+1 season and ends in 2025. Figure [5](https://arxiv.org/html/2510.17641v1#S4.F5 "Figure 5 ‣ 4 Results and discussion ‣ Are penalty shootouts better than a coin toss? Evidence from European football") plots the corresponding pp-values for the coefficients β0\beta\_{0} and β1\beta\_{1}. The winning probability becomes different from a coin toss only if the sample consists of the last season 2025/26—when the number of observations is 14, and a higher Elo rating seems to be disadvantageous. Consequently, in contrast to domestic cups, stronger teams are not expected to win more penalty shootouts in UEFA club competitions.

## 5 Concluding remarks

Our paper has aimed to predict success in penalty shootouts in top European football during the last 25 years. We have considered several possible factors, such as the shooting order, the field of the match, and psychological momentum, but none of them affects the probability of winning. First in the literature, team strength is measured by Elo ratings instead of the division of the team or betting odds. This has led to a surprising finding: even though Elo ratings can forecast results in the UEFA Champions League, they entirely lose their predictive power if the qualification is decided by penalty shootouts.

These results could have important policy implications.
First, if a drawn match is followed by penalty shootouts where the winner receives two points instead of one such as in the 2025 Leagues Cup, stronger teams would usually have more powerful incentives to attack since a draw means half extra points for both teams in expected value.
Second, abolishing extra time, an intervention recently contemplated by UEFA, would favour weaker teams and improve competitive balance.

## Acknowledgements

We appreciate the help of *Milán Kolonics* in data collection.
  
The research was supported by the National Research, Development and Innovation Office under Grants FK 145838 and PD 153835, and by the János Bolyai Research Scholarship of the Hungarian Academy of Sciences.

## References

* Aldous, (2017)

  Aldous, D. (2017).
  Elo ratings and the sports model: A neglected topic in applied
  probability?
  Statistical Science, 32(4):616–629.
* Ames, (2025)

  Ames, N. (2025).
  Uefa weighs up scrapping extra time for Champions League knockout
  rounds.
  The Guardian.
  5 February.
  <https://www.theguardian.com/football/2025/feb/05/uefa-weighs-up-scrapping-extra-time-for-champions-league-knockout-rounds>.
* Anbarcı et al., (2021)

  Anbarcı, N., Sun, C.-J., and Ünver, M. U. (2021).
  Designing practical and fair sequential team contests: The case of
  penalty shootouts.
  Games and Economic Behavior, 130:25–43.
* Apesteguia and Palacios-Huerta, (2010)

  Apesteguia, J. and Palacios-Huerta, I. (2010).
  Psychological pressure in competitive environments: Evidence from a
  randomized natural experiment.
  American Economic Review, 100(5):2548–2564.
* Arrondel et al., (2019)

  Arrondel, L., Duhautois, R., and Laslier, J.-F. (2019).
  Decision under psychological pressure: The shooter’s anxiety at the
  penalty kick.
  Journal of Economic Psychology, 70:22–35.
* Bahamonde-Birke and Bahamonde-Birke,
  (2023)

  Bahamonde-Birke, F. J. and Bahamonde-Birke, R. A. (2023).
  About the “away goals rule” in association football. Does
  scrapping the rule increase the fairness of the game?
  Journal of Sports Economics, 24(3):310–328.
* Bosker and Gürtler, (2024)

  Bosker, J. and Gürtler, M. (2024).
  The impact of cultural differences on the success of elite labor
  migration—Evidence from professional soccer.
  Annals of Operations Research, 341(2-3):781–824.
* Brams and Ismail, (2018)

  Brams, S. J. and Ismail, M. S. (2018).
  Making the rules of sports fairer.
  SIAM Review, 60(1):181–202.
* Brams et al., (2024)

  Brams, S. J., Ismail, M. S., and Kilgour, D. M. (2024).
  Fairer shootouts in soccer: The (m,n)(m,n) rule.
  Mathematics Magazine, 97(4):366–379.
* Braun and Kvasnicka, (2013)

  Braun, S. and Kvasnicka, M. (2013).
  National sentiment and economic behavior: Evidence from online
  betting on European football.
  Journal of Sports Economics, 14(1):45–64.
* Cain et al., (2000)

  Cain, M., Law, D., and Peel, D. (2000).
  The favourite-longshot bias and market efficiency in UK football
  betting.
  Scottish Journal of Political Economy, 47(1):25–36.
* (12)

  Csató, L. (2021a).
  A comparison of penalty shootout designs in soccer.
  4OR, 19(5):183–198.
* (13)

  Csató, L. (2021b).
  Tournament Design: How Operations Research Can Improve Sports
  Rules.
  Palgrave Pivots in Sports Economics. Palgrave Macmillan, Cham,
  Switzerland.
* Csató, (2022)

  Csató, L. (2022).
  UEFA against the champions? An evaluation of the recent reform of
  the Champions League qualification.
  Journal of Sports Economics, 23(8):991–1016.
* Csató, (2024)

  Csató, L. (2024).
  Club coefficients in the UEFA Champions League: Time for shift
  to an Elo-based formula.
  International Journal of Performance Analysis in Sport,
  24(2):119–134.
* Csató and Petróczy, (2022)

  Csató, L. and Petróczy, D. G. (2022).
  Fairness in penalty shootouts: Is it worth using dynamic sequences?
  Journal of Sports Sciences, 40(12):1392–1398.
* Da Silva et al., (2018)

  Da Silva, S., Mioranza, D., and Matsushita, R. (2018).
  FIFA is right: The penalty shootout should adopt the tennis
  tiebreak format.
  Open Access Library Journal, 5(3):1–23.
* Del Giudice, (2019)

  Del Giudice, P. E. S. (2019).
  Modeling football penalty shootouts: How improving individual
  performance affects team performance and the fairness of the ABAB sequence.
  International Journal of Sport and Health Sciences,
  13(5):240–245.
* Echenique, (2017)

  Echenique, F. (2017).
  ABAB or ABBA? The arithmetics of penalty shootouts in soccer.
  Manuscript. <http://www.its.caltech.edu/~fede/wp/penales.pdf>.
* Feddersen et al., (2017)

  Feddersen, A., Humphreys, B. R., and Soebbing, B. P. (2017).
  Sentiment bias and asset prices: Evidence from sports betting markets
  and social media.
  Economic Inquiry, 55(2):1119–1129.
* FIFA, (2018)

  FIFA (2018).
  IFAB’s 133rd Annual Business Meeting recommends fine-tuning
  Laws for the benefit of the game.
  22 November.
  <http://web.archive.org/web/20200829060851/https://www.fifa.com/who-we-are/news/ifab-s-133rd-annual-business-meeting-recommends-fine-tuning-laws-for-the-benefit>.
* Forrest et al., (2025)

  Forrest, D., Kościółek, S., and Tena, J. D. (2025).
  The removal of the away goals rule: Intended or unintended
  consequences?
  Manuscript. DOI:
  [10.2139/ssrn.5239269](https://doi.org/10.2139/ssrn.5239269).
* Gomes de Pinho Zanco et al.,
  (2024)

  Gomes de Pinho Zanco, D., Szczecinski, L., Kuhn, E. V., and Seara, R. (2024).
  Stochastic analysis of the Elo rating algorithm in round-robin
  tournaments.
  Digital Signal Processing, 145:104313.
* Kassis et al., (2021)

  Kassis, M., Schmidt, S. L., Schreyer, D., and Sutter, M. (2021).
  Psychological pressure and the right to determine the moves in
  dynamic tournaments – evidence from a natural field experiment.
  Games and Economic Behavior, 126:278–287.
* Kocher et al., (2012)

  Kocher, M. G., Lenz, M. V., and Sutter, M. (2012).
  Psychological pressure in competitive environments: New evidence from
  randomized natural experiments.
  Management Science, 58(8):1585–1591.
* Krumer, (2020)

  Krumer, A. (2020).
  Pressure versus ability: Evidence from penalty shoot-outs between
  teams from different divisions.
  Journal of Behavioral and Experimental Economics, 89:101578.
* Krumer, (2021)

  Krumer, A. (2021).
  Does psychological momentum differ for home and away teams?
  Evidence from penalty shoot-outs in European cups.
  In Altman, H. J. R., Altman, M., and Torgler, B., editors, Behavioural Sports Economics, pages 159–171. Routledge, London, United
  Kingdom.
* Leagues Cup, (2025)

  Leagues Cup (2025).
  Leagues Cup 2025 Guide: Everything fans need to know.
  25 July.
  <https://www.mlssoccer.com/news/leagues-cup-2025-guide-everything-fans-need-to-know-questions-answered>.
* Palacios-Huerta, (2012)

  Palacios-Huerta, I. (2012).
  Tournaments, fairness and the Prouhet–Thue–Morse sequence.
  Economic Inquiry, 50(3):848–849.
* Palacios-Huerta, (2014)

  Palacios-Huerta, I. (2014).
  Beautiful Game Theory: How Soccer Can Help Economics.
  Princeton University Press, Princeton, New Jersey, USA.
* Palacios-Huerta, (2020)

  Palacios-Huerta, I. (2020).
  Data revealed: ABBA penalty kick shootout trials yield a more
  balanced outcome.
  Sports Illustrated.
  4 December.
  <https://www.si.com/soccer/2020/12/04/ifab-abba-penalty-shootout-trials-results-pk-fifa>.
* Pipke, (2025)

  Pipke, D. (2025).
  No evidence of first-mover advantage in a large sample of penalty
  shootouts.
  Journal of Economic Psychology, 108:102816.
* Rudi et al., (2020)

  Rudi, N., Olivares, M., and Shetty, A. (2020).
  Ordering sequential competitions to reduce order relevance: Soccer
  penalty shootouts.
  PLoS ONE, 15(12):e0243786.
* Santos, (2023)

  Santos, R. M. (2023).
  Effects of psychological pressure on first-mover advantage in
  competitive environments: Evidence from penalty shootouts.
  Contemporary Economic Policy, 41(2):354–369.
* van Eetvelde and Ley, (2019)

  van Eetvelde, H. and Ley, C. (2019).
  Ranking methods in soccer.
  In Kenett, R. S., Longford, T. N., Piegorsch, W., and Ruggeri, F.,
  editors, Wiley StatsRef: Statistics Reference Online, pages 1–9.
  Springer, Hoboken, New Jersey, USA.
* Vandebroek et al., (2018)

  Vandebroek, T. P., McCann, B. T., and Vroom, G. (2018).
  Modeling the effects of psychological pressure on first-mover
  advantage in competitive interactions: The case of penalty shoot-outs.
  Journal of Sports Economics, 19(5):725–754.
* Vollmer et al., (2024)

  Vollmer, S., Schoch, D., and Brandes, U. (2024).
  Penalty shoot-outs are tough, but the alternating order is fair.
  PLoS ONE, 19(12):e0315017.
* Winkelmann et al., (2021)

  Winkelmann, D., Deutscher, C., and Ötting, M. (2021).
  Bookmakers’ mispricing of the disappeared home advantage in the
  German Bundesliga after the COVID-19 break.
  Applied Economics, 53(26):3054–3064.
* Wood et al., (2015)

  Wood, G., Jordet, G., and Wilson, M. R. (2015).
  On winning the “lottery”: psychological preparation for football
  penalty shoot-outs.
  Journal of Sports Sciences, 33(17):1758–1765.
* Wunderlich et al., (2020)

  Wunderlich, F., Berge, F., Memmert, D., and Rein, R. (2020).
  Almost a lottery: the influence of team strength on success in
  penalty shootouts.
  International Journal of Performance Analysis in Sport,
  20(5):857–869.
* (41)

  Yildirim, M. and Bilman, M. E. (2025a).
  New rules, new game? The effects of the away goals rule removal and
  video assistant referee adoption on game dynamics in UEFA Champions
  League ties.
  Journal of Policy Modeling, 47(1):78–96.
* (42)

  Yildirim, M. and Bilman, M. E. (2025b).
  Second-leg home advantage no more? The impact of Video
  Assistant Referee and no away goals rule in elite soccer.
  Journal of Policy Modeling, 47(5):1097–1112.

## Appendix

### A.1 A mistake in Football Club Elo Ratings data

Two Armenian football clubs, Ararat Yerevan (<http://clubelo.com/Ararat>) and Ararat-Armenia (<http://clubelo.com/Ararat-Armenia>), have similar names. Both teams have played in UEFA club competitions recently.

In the 2021/22 Armenian Premier League, Ararat-Armenia was the runner-up and qualified for the second qualifying round of the 2022/23 UEFA Europa Conference League. Ararat Yerevan was ranked fourth and qualified for the first qualifying round of the 2022/23 UEFA Europa Conference League. Ararat Yerevan lost in the first round against the North Macedonian club Shkëndiye, while Ararat-Armenia lost in the second round—by penalty shootouts—against the Estonian club Paide Linnameeskond.
However, Football Club Elo Ratings registered both matches for Ararat Yerevan, see <http://clubelo.com/Ararat/Games/Latest>.
Thus, the Elo rating of Ararat-Armenia remains unknown in these matches.

In the 2022/23 Armenian Premier League, Ararat-Armenia was ranked third and qualified for the first qualifying round of the 2023/24 UEFA Europa Conference League. It won in the first round—by penalty shootouts—against the Albanian club Egnatia, and lost in the second round against the Greek club Aris.
However, Football Club Elo Ratings registered both matches for Ararat Yerevan, see <http://clubelo.com/Ararat/Games/Latest>.
Thus, the Elo rating of Ararat-Armenia remains unknown in these matches.

In the 2023/24 Armenian Premier League, Ararat-Armenia was ranked third and qualified for the second qualifying round of the 2024/25 UEFA Conference League. It won in the second round against the Moldavian club Zimbru Chişinău, and lost in the third round against the Hungarian club Puskás Akadémia.
However, Football Club Elo Ratings registered both matches for Ararat Yerevan, see <http://clubelo.com/Ararat/Games/Latest>.
Thus, the Elo rating of Ararat-Armenia remains unknown in these matches.

In the 2024/25 Armenian Premier League, Ararat-Armenia was ranked second and qualified for the second qualifying round of the 2025/26 UEFA Conference League. It won in the second round against the Romanian club Universitatea Cluj, and lost in the third round against the Czech club Sparta Praha.
However, Football Club Elo Ratings registered both matches for Ararat Yerevan, see <http://clubelo.com/Ararat/Games/Latest>.
Thus, the Elo rating of Ararat-Armenia remains unknown in these matches.

Therefore, we could not know the Elo rating of one team, Ararat-Armenia, in two penalty shootouts, which were ignored in the corresponding analyses.

More worryingly, the unreliability of the Elo ratings for Ararat Yerevan spreads to their (supposed) opponents, opponents of opponents, and so on, raising questions about the validity of Football Club Elo Ratings data. Unfortunately, we are not able to correct this error of the underlying database. We have informed the creator of Football Club Elo Ratings, *Lars Schiefler*, about the problem but received no answer.

### A.2 Supplementary tables

Table A.1: Results of binomial tests: first-mover advantage, home advantage, momentum

Potential success factor


Wins


Loses


Total


Win ratio


pp-value


First-mover


143


125


268


53.4%


0.299

Home (extended data)


118


137


255


46.3%


0.260

Home (restricted data)


111


123


234


47.4%


0.472

Comeback (all goals)


72


75


147


49.0%


0.869

Comeback (last goal)


121


110


231


52.4%


0.511

•

Two-sided binomial tests. Significance: \* p<5%p<5\%; \*\* p<1%p<1\%; \*\*\* p<0.1%p<0.1\%.




Table A.2: Results of binomial tests: team strength

Scenario
Favourite wins
Favourite loses


Total
Win ratio


pp-value


Elo difference >0>0
125
141


266
47.0%


0.358

Elo difference >25>25
115
127


242
47.5%


0.480

Elo difference >50>50
101
112


213
47.4%


0.493

Elo difference >75>75
84
95


179
46.9%


0.455

Elo difference >100>100
73
81


154
47.4%


0.573

•

Two-sided binomial tests. Significance: \* p<5%p<5\%; \*\* p<1%p<1\%; \*\*\* p<0.1%p<0.1\%.