---
authors:
- Gaëlle Aymeric
- Emmanuelle Lavaine
- Brice Magdalou
doc_id: arxiv:2510.18481v1
family_id: arxiv:2510.18481
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Parental environment and student achievement: Does a Matthew effect exist?
  1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract
  ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was
  written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille
  School of Economics. We acknowledge financial support from the French government
  under the “France 2030” investment plan managed by the French National Research
  Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille
  University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus
  Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy
  for their useful comments.'
url_abs: http://arxiv.org/abs/2510.18481v1
url_html: https://arxiv.org/html/2510.18481v1
venue: arXiv q-fin
version: 1
year: 2025
---


Gaëlle Aymeric,222Universidad Complutense de Madrid
  
E-mail: gaymeric@ucm.es. Emmanuelle Lavaine 333CEE-M, Univ. Montpellier, CNRS, INRAE, Institut Agro, Montpellier, France.
  
E-mail: emmanuelle.lavaine@umontpellier.fr. and Brice Magdalou 444CNRS, AMSE, Marseille, France.
  
E-mail: brice.magdalou@umontpellier.fr.

###### Abstract

This paper investigates the causal impact of the parental environment on the student’s academic performance in mathematics, literature and English (as a foreign language), using a new database covering all children aged 8 to 15 of the Madrid community, from 2016 to 2019. Parental environment refers here to the parents’ level of education (i.e. the skills they acquired before bringing up their children), and parental investment (the effort made by parents to bring up their children). We distinguish the persistent effect of the parental environment from the so-called Matthew effect, which describes a possible tendency for the impact of the parental environment to increase as the child grows up. Whatever the subject (mathematics, literature or English), our results are in line with most studies concerning the persistent effect: a favourable parental environment goes hand in hand with better results for the children. As regards the Matthew effect, the results differ between subjects: while the impact of the parental environment tends to diminish from the age of 8 to 15 in mathematics, it forms a bell curve in literature (first increasing, then decreasing) and increases steadily in English. This result, which is encouraging for mathematics and even literature, confirms the social dimension involved in learning a foreign language compared to more academic subjects.

JEL Classification Numbers: I24, D63. Keywords: Academic results; Parental environment; Equality of opportunity; Matthew effect.

‘To all those who have, more will be given, and they will have an abundance; but from those who have nothing, even what they have will be taken away’

[Matthew (the Bible 13:12, NRSV)]

## 1 Introduction

It is now well-documented that the cognitive and non-cognitive abilities developed in the early childhood drive the educational, social and professional success of people throughout their entire life. It is also well-recognized that the social background and the investment of parents in their own children impact ability acquisition, which partly explains the inequalities in academic performance across children. According to the Matthew effect,111The Matthew effect, a standard concept in sociology, has been popularized by Merton ([1968](https://arxiv.org/html/2510.18481v1#bib.bib26)). Rigney ([2010](https://arxiv.org/html/2510.18481v1#bib.bib31)) proposes a review of applications in several (social) sciences, including education. in many spheres of life, ‘the rich get richer and the poor get poorer’. In the education field, this effect describes a possible tendency of initial advantages, in early life, to accumulate through time. Whereas the persistent effect of the parental environment on student achievement is now admitted, the theoretical and empirical literatures are more balanced on the existence of a possible Matthew effect. This paper aims at contributing to this debate.

Different channels can explain the impact of parental environment on children academic performance. The first is a possible intergenerational transmission of cognitive skills, which implies that the association between parents and children abilities can be partly driven by genetic.222Hanushek et al. ([2021](https://arxiv.org/html/2510.18481v1#bib.bib18)) identify a causal connection between cognitive skills of the parents and their children, based on a Dutch survey on math and language skills. Sacerdote ([2007](https://arxiv.org/html/2510.18481v1#bib.bib33)) uses Korean American adoptees data to show that genetic factors explain 44% of the variation in educational attainment and 33% of the variation in income. A second is through the parent’s level of education. The children can benefit from the knowledge and diplomas acquired by their parents, but also from the related positive spillovers.333The survey proposed by Holmlund et al. ([2011](https://arxiv.org/html/2510.18481v1#bib.bib19)) concludes that the estimates of the causal effect of parent’s schooling on child’s schooling differ across studies, but also that selection is the main component of the intergenerational association. At the opposite, by using original Finnish data, Suhonen and Karhunen ([2019](https://arxiv.org/html/2510.18481v1#bib.bib36)) find a strong positive causal effect (of around 0.5) from parent’s to child’s attained years of education. A third channel is parental investment, which can be a major input in the child production of skills. In that case, a distinction has to be drawn between cognitive and non-cognitive skills. Cunha et al. ([2010](https://arxiv.org/html/2510.18481v1#bib.bib11)) found that the productivity of parental investment for cognitive skills is high in the early stages of education (before 6), but tends to significantly decrease after. At the opposite, the productivity of parental investment on non-cognitive skills is found to be higher at later stages. Finally, these channels can be exacerbated by a possible assortative mating of the parents.444Bingley et al. ([2022](https://arxiv.org/html/2510.18481v1#bib.bib7)) find that 75% of the correlation in education attainment between parents and their children is driven by the joint contribution of the parents (as compared to the contribution of each parent independently). Eika et al. ([2019](https://arxiv.org/html/2510.18481v1#bib.bib16)) also find that educational assortative mating has declined among college graduates in the US since the 1960s, while it has progressively increased among the low-educated (a trend also true for the other countries studied: Denmark, Germany, the United Kingdom, and Norway).

The literature on the technology of skills formation, initiated by Cunha and Heckman ([2007](https://arxiv.org/html/2510.18481v1#bib.bib10)) and Cunha et al. ([2010](https://arxiv.org/html/2510.18481v1#bib.bib11)), tends to support the hypothesis of cumulative advantages. The authors propose and estimate a model where, at each stage of the child development, the inputs and the production technology can differ. They find that self-productivity (the stock of skills produced at one stage augment the skills attained at later stages), for both cognitive and non-cognitive skills, becomes stronger as the child becomes older. They also observe dynamic complementary (the productivity of an investment can be raised by skills produced at previous stages), but with a decrease in substitutability between investment in one period and the existing stock of skills. Hence, it is more and more difficult to compensate for initial endowment differences, which can imply an increasing attainment gap between advantaged and disadvantaged children.555One main policy recommendation resulting from these estimations is that successful adolescent remediation strategies for disadvantaged children should focus on fostering non-cognitive skills.

On the other hand, the equality of opportunity literature suggests that, in moving towards adulthood, the child is able to free herself (at least partially) from some external factors that have determined her previous achievements. In the same vain of the age of sexual consent or the age of criminal responsibility, this theory refers to what we can call an age (of consent) for responsible choices Roemer and Trannoy ([2016](https://arxiv.org/html/2510.18481v1#bib.bib32)); Hufe et al. ([2017](https://arxiv.org/html/2510.18481v1#bib.bib22)). In early childhood, the child cannot be held responsible for her behaviors and achievements as they result from circumstances not under her control.666Laziness at school, for instance, might be explained by a home environment which is neither stimulating nor rewarding. In contrast, one can assume that an adult is able to set out personal objectives and to take free and enlightened decisions (whatever her background), such as the level of effort she decides to put at work. This prerequisite is actually necessary for the existence of freedom in itself, by considering that the life trajectory is not fully deterministic. Of course the age of consent is a normative concept here, not a precise age threshold, and it is debatable to fix it before adulthood.777Roemer and Trannoy ([2016](https://arxiv.org/html/2510.18481v1#bib.bib32)) emphasize that it is controversial to use years of education as an effort variable (hence after the age of consent) until the end of secondary education, and consider that only tertiary education is immune to this criticism. Hufe et al. ([2017](https://arxiv.org/html/2510.18481v1#bib.bib22)) fix this age between 12 and 16, and recalculate the fraction of income inequality due to circumstances in the US and the UK, by considering that all the childhood achievements before the age of consent is a circumstance. But with this concept in hands, one can hypothesize that initial disadvantages or the parental influence can be partially mitigated, throughout schooling, by the emancipation of the child as she grows up.888By studying the academic performance of students who are the first in their family to attend university, Edwards et al. ([2022](https://arxiv.org/html/2510.18481v1#bib.bib15)) establish that some non-cognitive skills such as conscientiousness or extraversion, predict academic performance almost as strongly as standardised university admissions test scores. One can assume that such skills do not necessarily result from parental investment.

In this paper, we investigate a rich and never exploited database on the Madrid Community (Spain) to analyse the impact of parental environment (including parental highest schooling and parental investment) on their child’s academic performance in three subjects (mathematics, literature and English as foreign language) and its change at three different education grades (Grades 3, 6 and 10, respectively about 8, 11 and 15 years old), over four academic years (from 2016 to 2019). We have combined data from various sources, provided by the Ministry of Education and Research of the Community of Madrid. First, for each grade, we have the scores of the students in each subject. The scores are normalised following a method comparable to the one used by the OECD’s Programme for International Student Assessment (PISA). Then, we have the data from two questionnaires, one sent to the students and another sent to the parents. We obtain various descriptive observations for the students and the parents (gender, country of birth, …) as well as behavioral observations, which can be used as proxy of the parental investment and child’s effort. This repeated cross-sectional dataset covers the overall Madrid Community, including private and public schools, and gathering data for more than 320,000 students.

Our empirical results contribute to the literature in several main directions. First, through a linear regression with fixed effects, we observe that the parental environment–both parents’ highest level of education and their investment–is a strong predictor of the child’s score in mathematics, literature, and English. Hence, a favorable parental environment goes hand in hand with better results for the children, what we call the persistent effect. Second, by using interaction components to observe how this influence evolves as the child progresses through school, we find mixed but informative results on the Matthew effect: whereas the parental influence on a child’s score decreases from age 11 to 15 in mathematics and follows a bell curve in literature, it is continuously and significantly increasing in English. Third, to address potential endogeneity and establish causality, we employ an instrumental variable (IV) analysis using the historical gender gap in tertiary education in the parents’ country of origin as an instrument. These IV estimates reinforce our initial findings, providing stronger causal evidences for the persistent effect and the mixed picture regarding the Matthew effect. Finally, our results also show that while a child’s own effort (proxied by time spent on homework) becomes increasingly impactful on academic results as they get older in all subjects, this effect is slightly weaker in English. This result confirms the special status of second language learning in schools Gardner ([1968](https://arxiv.org/html/2510.18481v1#bib.bib17)): The acquisition of a new language is a highly social process, determined by the environment in which the child lives, and which can be a source of important inequality of opportunity. In contrast, remediation programs for adolescent could be effective in mathematics or literature Bahr ([2007](https://arxiv.org/html/2510.18481v1#bib.bib2), [2008](https://arxiv.org/html/2510.18481v1#bib.bib3)) by fostering, for instance, non-cognitive skills, which serve as catalysts for cognitive development, such as perseverance, conscientiousness, or curiosity. Such optimism is supported by the clear indication, obtained from our data, that effort is more and more successful after some age (for all the subjects).

The rest of the paper is organized as follows. We present in Section [2](https://arxiv.org/html/2510.18481v1#S2 "2 Data ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") our data and some descriptive results. Section [3](https://arxiv.org/html/2510.18481v1#S3 "3 Initial estimation strategy and results ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") investigates the impact of parental highest schooling on student achievement, on the basis of two linear regression strategies (with or without interaction components). In this section, we also analyze the impact of parental investment and child’s effort. In Section [4](https://arxiv.org/html/2510.18481v1#S4 "4 Adressing endogeneity: Instrumental variable (IV) analysis ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments."), we continue our investigation into the impact of parental highest schooling, using an instrumental variable approach, to avoid any potential endogeneity issues. Finally, we discuss in Section [5](https://arxiv.org/html/2510.18481v1#S5 "5 Discussion, related literature, and policy implications ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") our main results, in the light of a related literature, mainly in psychology. We also present some implications in terms of educational policies.

## 2 Data

This paper is based on a rich database that has never been used in academic research. From 2016 to 2019, the Ministry of Education and Research of Madrid Community (Spain)999Consejeria de Educacion y Investigacion de la Comunidad de Madrid. has organized annual exams for all the students of the community in Grade 3 (8 years old), Grade 6 (11 years old) and Grade 10 (15 years old; not assessed in 2016). In parallel with these examinations, four questionnaires were organized for the various stakeholders: one addressed to the parents, one addressed to the student (Grade 6 and Grade 10), one addressed to the school director, and one addressed to the teachers. The main aim of these questionnaires was to assess people’s own feelings about the quality of the educational system, but also to evaluate people’s involvement (such as the time parents devote to their child’s education, or the weekly time children spend on homework). Surprisingly enough, these data have never been used in academic research up to date.

The first contribution of the present paper is to gather a set of disparate files and documents. We obtain a unique and harmonized cross-sectional database, covering more than 320,000 students. This database has a number of advantages, over most existing databases. First, this is not a simple survey as they cover all pupils in the Madrid community (whether in private or public schools). Then, pupils have a common identifier on examinations and questionnaires, so that it is possible to combine quantitative data on academic performance with more qualitative data, describing the educational environment in some detail.

This study focuses on three subjects: mathematics, literature and English (foreign language). As with many of the world’s leading education surveys,101010A few examples: PISA, TALIS or PIAAC, for the OECD; TIMSS or PIRLS for the International Association for the Evaluation of Educational Achievement (IEA); TOEFL and Cambridge Certification. the final exam score in each subject is calculated on the basis of the Item Response Theory (IRT). That refers to a family of mathematical models that attempt to explain the relationship between a candidate’s response to an item and that candidate’s aptitude or skills. In this study, the Partial Credit Model (PCM) is implemented (see Masters and Wright, [1997](https://arxiv.org/html/2510.18481v1#bib.bib25)). As with the Pisa results, the scoring is then transformed so that the mean is 500 and the standard deviation 100.

The database contains information for, approximately, 615,000 students: 230,000 in Grade 3, 240,000 in Grade 6 and 145,000 in Grade 10. If we take into account students whose parents responded to the questionnaire, we obtain 321,544 students: 145,096 students in Grade 3, 123,811 students in Grade 6 and 52,637 students in Grade 10. An important question concerns the impact of parents’ level of education on their child’s academic performance. We create a variables with three ‘homogenous’ categories, based on the highest level of education observed among parents:111111We could also have chosen the father’s highest level, or that of the mother. In this paper, we do not investigate whether the effects of parental schooling can be explained by assortative mating, or if the partial effects of parents can be differentiated. We consider parents’ education as a potential from which children can benefit. See Holmlund et al. ([2011](https://arxiv.org/html/2510.18481v1#bib.bib19)), Page 3, for a detailed discussion on this issue. before Grade 11, Grade 12/Vocational Training/Short-Cycle Tertiary Education and Bachelor/Master/Doctorate. Respectively, they are coded from 0 to 2 and correspond, according to the International Standard Classification of Education (ISCED 2011), respectively to Levels 0 to 2, Levels 3 to 5 and Levels 6 to 8. The rest of the data is described in Tables LABEL:var-desc to [6](https://arxiv.org/html/2510.18481v1#A1.T6 "Table 6 ‣ Appendix A Appendix ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments."), in Appendix.

We illustrate in Figure [1](https://arxiv.org/html/2510.18481v1#S2.F1 "Figure 1 ‣ 2 Data ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") the impact of the parents’ highest level of education on child’s mathematics scores, for Grades 3 and 10. We plot the cumulative distribution functions of the scores, conditional on the parents (highest level of schooling) group.

Figure 1:  CDFs of mathematics scores according to parents’ highest level of education

|  |  |
| --- | --- |
| Refer to caption | Refer to caption |
| Grade 3 | Grade 10 |

For each grade, we can see that the cumulative distribution functions are ordered in the sense of first order stochastic dominance: For any given score, the probability of having a score higher than it, is all the greater the higher the parent group. This pattern holds true for mathematics, but it also applies to all subjects and all grades in our data (discussed hereafter). First-order dominance is generally considered to be a clear indication of inequality of opportunity, since academic performance depends on a dimension beyond the child’s control Lefranc et al. ([2009](https://arxiv.org/html/2510.18481v1#bib.bib24)); Jaoul-Grammare and Magdalou ([2013](https://arxiv.org/html/2510.18481v1#bib.bib23)). This result is in line with a robust trend already observed in the literature.

The second question looks at the evolution of parental influence on child’s results, throughout schooling. In Figure [1](https://arxiv.org/html/2510.18481v1#S2.F1 "Figure 1 ‣ 2 Data ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments."), we see a convergence of the three conditional CDFs between Grades 3 and 10 (in mathematics), suggesting that the dependence of results on parent group decreases. However, such an observation must be treated with caution. First, the tests are of a different nature for each grade. Then, the fact that the results are standardized (average of 500) can be misleading for comparison purposes. Finally, external factors can significantly impact the results, that can only be analyzed by econometric estimates.

One possible bias in the comparison of the impact of parents’ level of education on child’s score, at different grades, may be linked to a composition effect. For instance, the convergence of the CDFs between Grades 3 and 10 may be a consequence of the fact that, in the group of children whose parents have the lowest level of education, only the most gifted children remain represented in Grade 10. As established in Table [6](https://arxiv.org/html/2510.18481v1#A1.T6 "Table 6 ‣ Appendix A Appendix ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") in Appendix, we do not observe, for each year and each grade, any significant difference in the proportions that each group represents: The proportions are all close to those obtained at global level, i.e. 9.5%, 31.5%, and 59% for parents with ISCED levels, respectively, 0–2, 3–5, and 6–8. We can therefore consider that our data do not suffer from this compositional bias.

The equivalent of Figure [1](https://arxiv.org/html/2510.18481v1#S2.F1 "Figure 1 ‣ 2 Data ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") in literature and English is provided, respectively, in Figures [9](https://arxiv.org/html/2510.18481v1#A1.F9 "Figure 9 ‣ Appendix A Appendix ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") and [10](https://arxiv.org/html/2510.18481v1#A1.F10 "Figure 10 ‣ Appendix A Appendix ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") in Appendix. Whereas the convergence of CDFs is evident in mathematics and literature between Grades 3 and 10, this is not the case for English: The inequality of opportunity observed at Grade 3 seems to increase at Grade 10. This finding is confirmed by the econometric analysis presented in the following sections.

## 3 Initial estimation strategy and results

### 3.1 Impact of parent’s highest level of education

In this section we regress students’ score in the three subjects under consideration (three regressions), focusing on the impact of parents’ highest level of education. The score of student ii is denoted yi​t​sy\_{its}, where tt is the year (from 2016 to 2019) and ss the school attended. As described earlier, parents’ highest level of education is modeled by an ordered categorical variable with 3 possible values, hereafter referred as parent groups. We introduce independent dummy variables (pj\textnormal{{p}}\_{j} with j=0,1,2j=0,1,2) that allow us to compare the impact of parent groups two by two, with the lowest group (j=0j=0) as the reference value.

We also introduce two groups of control variables, one for the student characteristics (each denoted sks\_{k}) and another for the households characteristics (each denoted hkh\_{k}).121212Student characteristics include country of birth, number of days a week spent on homework, and gender. Household characteristics include country of birth of both parent, the frequency of use of books/computers/internet at home, the number of books at home, the employment status of both parents, the frequency with which parents talk about school subjects/teach homework/help with homework/check homework with the child.
For each subject, we make an overall estimate of the student’s score for all academic years and all grades. Although the tests are common to all schools in the Community of Madrid over the whole period, results may vary in time (from one year to another), and in space (from one school to another, particularly between public and private schools). With the aim of controlling these dimensions, we introduce two fixed effects, one for the academic year (ata\_{t}) and one for the identifier of the school ss where the student ii is registered (bsb\_{s}).131313At this stage, we do not introduce a fixed effect for the grade because the mean score, whatever the grade, is always normalised at 500 at the population level (and the standard deviation at 100). Even if there is a small variation in average scores between subjects and grades in our samples, they remain very close to 500. Notice that the constants estimated in regressions ([1](https://arxiv.org/html/2510.18481v1#S3.E1 "In 3.1 Impact of parent’s highest level of education ‣ 3 Initial estimation strategy and results ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.")) is close to this value (see results tables). 
One obtains the following regression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | yi​t​s=α0+∑j=1,2αj​pj​i+∑kβk​sk​i+∑kγk​hk​i+at+bs+ϵi​t​s.y\_{its}=\alpha\_{0}+\textstyle\sum\_{j=1,2}\alpha\_{j}\,p\_{ji}+\textstyle\sum\_{k}\beta\_{k}\,s\_{ki}+\textstyle\sum\_{k}\gamma\_{k}\,h\_{ki}+a\_{t}+b\_{s}+\epsilon\_{its}\,. |  | (1) |

This first regression, for each subject, isolates the influence of parents’ highest level of education on student’s score, without distinguishing the grade. The results are shown in Table [7](https://arxiv.org/html/2510.18481v1#A1.T7 "Table 7 ‣ Appendix A Appendix ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") for mathematics, Table [8](https://arxiv.org/html/2510.18481v1#A1.T8 "Table 8 ‣ Appendix A Appendix ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") for literature and Table [9](https://arxiv.org/html/2510.18481v1#A1.T9 "Table 9 ‣ Appendix A Appendix ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") for English. Whatever the regression specification (including or not the control variables), and for each subject, the results are the same and robust: moving from one parent group to a higher one, significantly increases student’s score. For instance, in mathematics, moving from Parent Group 0 (ISCED 0 to 2) to Parent Group 22 (ISCED 6 to 8) increases the score by 29.7 points on average when all control variables are included (regression 3 in Table [7](https://arxiv.org/html/2510.18481v1#A1.T7 "Table 7 ‣ Appendix A Appendix ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.")). The effect is larger in literature than in mathematics, and in English than in literature. We summarise these results in Figure [2](https://arxiv.org/html/2510.18481v1#S3.F2 "Figure 2 ‣ 3.1 Impact of parent’s highest level of education ‣ 3 Initial estimation strategy and results ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") (estimates with all control variables, also plotting standard deviation). This result confirms a trend already widely observed in the literature, namely that the parents’ level of education has a major influence on the child’s academic performance, whatever the subject.

Figure 2:  Global impact of parents’ highest level of education on student’s score

![Refer to caption](x3.png)

Reading: In mathematics, moving from Parent Group 0 (Education ISCED 0–2) to Parent Group 11 (Education ISCED 3–5) increases the student’s score by about 10 points (which represents 2% of the normalised average score and 10% of the normalised standard deviation, respectively equal to 500 and 100). ±\pm standard deviation around the curve.

A more complex question (at the heart of this paper) concerns the evolution of this impact over time, throughout children’s education. To this end, we supplement the previous regression with interaction components between parental highest education and grade level of the student (Grade 3, Grade 6 or Grade 10). Precisely, we compare the grades two by two (3 vs. 6, 6 vs. 10 and 3 vs. 10), running a regression for each possible grades pair (u,v)(u,v), where u<vu<v. In each of these regressions, we retain only the observations of students’ scores for grades uu and vv (excluding the third grade). With gg indicating the grade, we introduce a dummy variable I​(u,v)I(u,v) which takes the value 0 if g=ug=u (reference grade), and 11 if g=vg=v. When we compare the grades uu and vv, we obtain the following expression, with g∈{u,v}g\in\{u,v\}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | yi​g​t​s=α0+∑j=1,2αj​pj​i+η​I​(u,v)+∑j=1,2θj​pj​i​I​(u,v)+∑kβk​sk​i+∑kγk​hk​i+at+bs+ϵi​g​t​s.y\_{igts}=\alpha\_{0}+\textstyle\sum\_{j=1,2}\alpha\_{j}\,p\_{ji}+\eta I(u,v)+\textstyle\sum\_{j=1,2}\theta\_{j}\,p\_{ji}I(u,v)+\textstyle\sum\_{k}\beta\_{k}\,s\_{ki}+\textstyle\sum\_{k}\gamma\_{k}\,h\_{ki}+a\_{t}+b\_{s}+\epsilon\_{igts}\,. |  | (2) |

The η\eta coefficient indicates the extra points obtained on average by the students in Grade vv, compared with Grade uu, whatever the parent group. As the average score is standardised at 500 for all grades, this coefficient is not very informative (values other than 0 are due to sample selection). We focus on coefficients αj\alpha\_{j} and θj\theta\_{j}, for j=1,2j=1,2. By definition of pj​ip\_{ji} and I​(u,v)I(u,v), the variable pj​i×I​(u,v)p\_{ji}\times I(u,v) takes the value 11 if and only if student ii is in Grade vv, with parents from group jj. Since the parent reference group is the lowest (j=0j=0), and the same applies to the grade (the reference is uu, with u<vu<v), the αj\alpha\_{j} coefficient is interpreted as the extra points obtained by the student in Grade uu when the parents are in group jj (compared with 0), and θj\theta\_{j} is interpreted as the marginal impact of parent’s group jj, when the student is in Grade vv instead of Grade uu.

For each subject, we obtain 9 regressions (3 regressions, depending on whether the student and household characteristics are included or not, for each of the 3 pairs of grades compared). The results are shown in Tables LABEL:G3-G6, LABEL:G6-G10 and LABEL:G3-G10 for, respectively, the comparison of Grade 3 versus Grade 6, Grade 6 versus Grade 10, and Grade 3 versus Grade 10 (each table showing the results for the 3 subjects). As established in the regressions without interaction components, parents’ highest level of education significantly increases student’s score, in each subject (coefficients αj\alpha\_{j}). If we focus on the regressions that take into account all the control variables (columns 3, 6 and 9 for each subject in, respectively, Tables LABEL:G3-G6, LABEL:G6-G10 and LABEL:G3-G10), we can see that moving from Parent Group 0 (ISCED 0 to 2) to Group 1 (ISCED 3 to 5) significantly increases the score, between 11 and 16 points in the three subjects. From Parent Group 0 to 2 (ISCED 6 to 8), the score increases between 28 and 37 points. These last values are relatively high, in the range of a third of the normalised standard deviation at the population level (equal to 100).

We now examine the estimates of the interaction components (θj\theta\_{j}), again focussing on the regressions that take into account all the control variables (columns 3, 6 and 9 for each subject, of Tables LABEL:G3-G6, LABEL:G6-G10 and LABEL:G3-G10). In mathematics, there is no significant marginal impact of parent group between Grades 3 and 6, but the impact is significant and negative between Grades 6 and 10 (and, consequently, also between Grades 3 and 10). As a result, the impact of parents’ highest level of education diminishes as student progresses through grades, from Grade 6 upwards. Between Grades 6 and 10, moving from Parent Group 0 to 1 results in a 7.9 point decrease in the score gap, and moving from Parent Group 0 to 2 results in a 13.6 point decrease in the score gap. A comparable pattern applies to literature, with a small difference: Between Grades 3 and 6, the marginal impact of moving from Parent Group 0 to 2 is significantly positive (about 12.2 points). The same change in parent group, but between Grades 6 and 10, implies a gap reduction of 11.6 points. The effect is therefore a bell-shaped curve in literature. The situation is completely different in English. Between Grades 3 and 6, and also between Grades 6 and 10, the impact of parent group increases significantly. For instance, between Grades 3 and 6, the marginal impact of moving from Parent Group 0 to 2 is around 9.5 points and, from Grade 6 to Grade 10, is about 9.9 additional points. Hence, influence of parent group is continuously and significantly increasing in English. We summarise the main results of the estimates with interaction components in Figure [3](https://arxiv.org/html/2510.18481v1#S3.F3 "Figure 3 ‣ 3.1 Impact of parent’s highest level of education ‣ 3 Initial estimation strategy and results ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") (estimates with all control variables).

Figure 3: Marginal impact of parents’ highest level of education on student’s score

![Refer to caption](Graph-Grade3-to-6.png)

![Refer to caption](Graph-Grade6-to-10.png)

Reading: Between Grade 6 and Grade 10 in mathematics, the marginal impact on the student’s score, of Parent Group 11 (ISCED 3 to 5) compared with Parent Group 0 (Education ISCED 0–2), is reduced by about 7.5 points (which represents 1.5% of the normalised average score and 7.5% of the normalised standard deviation, respectively equal to 500 and 100). ±\pm standard deviation around the curve.

### 3.2 Impact of parental investment and student’s effort

In this paper, we analyse the impact of parental environment on academic performance for their child through two channels: parent’s level of education (thus, skills acquired before bringing up children), and parental investment (an effort made by parents during the upbringing of their child). In the previous section, we showed that the effect of parents’ education tends to decrease between Grades 6 and 10 in mathematics and literature, but increases in English. This section focuses on the second aspect, i.e. the impact of parental investment, but also on the impact of efforts made by the child in her studies. We run regressions comparable to Equation ([1](https://arxiv.org/html/2510.18481v1#S3.E1 "In 3.1 Impact of parent’s highest level of education ‣ 3 Initial estimation strategy and results ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.")), but one per subject and per grade. The results are presented in Table LABEL:parent-invest. We focus on two explanatory dimensions for, respectively, parental investment and child’s effort: ‘frequency parents talk to their child about school’ and ‘days per week devoted to homework’ (both are introduced in the form of dummy variables).

Estimates are summarised in Figure [4](https://arxiv.org/html/2510.18481v1#S3.F4 "Figure 4 ‣ 3.2 Impact of parental investment and student’s effort ‣ 3 Initial estimation strategy and results ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments."). In terms of student’s effort, a clear trend emerges, whatever the subject: in Grade 3, the more days per week devoted to homework, the lower the scores (compared with the lowest category, i.e. ‘one day or less’). In Grade 6, an increase in the number of days dedicated to homework goes with an increase in results up to 4-5 days per week, then decreases thereafter. In Grade 10, scores increase with the number of days dedicated to homework.

Figure 4: Impact of student’s effort on score

![Refer to caption](x4.png)

Reading: In Grade 3 in mathematics, spending more that 5 days a week on homework, as opposed to one day or less, reduces a student’s score by around 10 points (which represents 2% of the normalised average score and 10% of the normalised standard deviation, respectively equal to 500 and 100). ±\pm standard deviation around the curve.

The negative impact of the number of days dedicated to homework in the first grade seems to indicate a reverse causality (which could be confirmed by further investigations), i.e. it is poor school results that implies more time devoted to homework (the volume of homework being lower than in the higher grades). As students progress in their studies, effort seems to have an increasing impact, culminating in a clear positive impact in Grade 10. Finally, if we focus on the highest effort category (‘five days or more’) in Grade 10, we can see that the greatest positive impact is for literature (+19.23 points), then mathematics (+14.05 points), and finally English (+12.68 points).

The number of days per week dedicated to homework cannot be considered as a purely effort variable for the child, as homework is supervised by parents (particularly in early childhood). However, children gain independence as they progress through the grades and, as time goes on, the more work they do, the better their results. This form of emancipation seems to be weaker in English, compared with the other two subjects.

The impact of parental investment on child’s achievement also seems to go hand in hand with lower emancipation in English. First of all, we observe in Table LABEL:parent-invest that, whatever the subject or grade (with some few exceptions), if the frequency with which parents talk to their child about school increases, then student achievement improves. However, between Grades 3 and 10, if we focus on the highest category of investment (‘every or almost every day’), the positive impact of parental investment decreases slightly in mathematics (from 10.6 to 9.0 points) and sharply in literature (from 16.1 to 8.3 points), while it rises sharply in English (from 8.7 to 12.9 points). Hence, between Grades 3 and 10, the impact of parental investment is clearly increasing in English, unlike in the the two other subjects. These results are shown in Figure [5](https://arxiv.org/html/2510.18481v1#S3.F5 "Figure 5 ‣ 3.2 Impact of parental investment and student’s effort ‣ 3 Initial estimation strategy and results ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") (where standard deviations have not been shown for the sake of clarity).

Figure 5: Impact of parental investment on student’s score

![Refer to caption](x5.png)

Reading: In Grade 10 in mathematics, if the parents talk to their child about school ‘once or twice a month’ instead of ‘never’, the child’s score increases by around 5 points (which represents 1% of the normalised average score and 5% of the normalised standard deviation, respectively equal to 500 and 100).

Finally, if we look at all the explanatory variables in Grade 10 (Table LABEL:parent-invest), we see that in mathematics and literature, the impact of child’s effort exceeds the impact of parental investment and is comparable to the impact of parents’ level of education. This is not the case in English: the impact of the child’s effort and that of the parents’ investment are roughly comparable, while the impact of parents’ level of education is much greater.

## 4 Adressing endogeneity: Instrumental variable (IV) analysis

### 4.1 Identification strategy

Section [3](https://arxiv.org/html/2510.18481v1#S3 "3 Initial estimation strategy and results ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") relies on linear regressions to estimate the relationship between parental environment and student achievement. The advantage is that they allow for detailed analysis, as in Figure [3](https://arxiv.org/html/2510.18481v1#S3.F3 "Figure 3 ‣ 3.1 Impact of parent’s highest level of education ‣ 3 Initial estimation strategy and results ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") where, from Grade to Grade and by subject, we can see the differentiated impact of the three categories of parental education. However, these estimates may be biased due to the endogeneity of the dependent variables of interest. For instance, parents’ level of education is likely correlated with unobserved family characteristics, such as motivation or inherited abilities, which also support a child’s accumulation of human capital. This correlation can make it difficult to isolate the true causal effect of parental schooling.

To address this endogeneity issue and identify the causal impact of parents’ level of education on the academic performance of students, we employ an instrumental variable approach. Following Cordero et al. ([2018](https://arxiv.org/html/2510.18481v1#bib.bib9)), who recommend the use of historical sources of exogenous variation, our chosen instrument is the gender gap in tertiary education in 1960 in the country of birth of the more educated parent. This variable is constructed using the Educational Attainment Data from Barro and Lee ([2013](https://arxiv.org/html/2510.18481v1#bib.bib4)). The gender gap is specifically calculated as the difference between the share of women and men who completed tertiary education. The viability of this instrument rests on its significant variation across the countries relevant to our analysis, a fact illustrated in Figures [6](https://arxiv.org/html/2510.18481v1#S4.F6 "Figure 6 ‣ 4.1 Identification strategy ‣ 4 Adressing endogeneity: Instrumental variable (IV) analysis ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") and [7](https://arxiv.org/html/2510.18481v1#S4.F7 "Figure 7 ‣ 4.1 Identification strategy ‣ 4 Adressing endogeneity: Instrumental variable (IV) analysis ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments."). The parents in our database come from 115 different countries, out of the 146 studied by Barro and Lee ([2013](https://arxiv.org/html/2510.18481v1#bib.bib4)) in 1960. For these countries, Figure [6](https://arxiv.org/html/2510.18481v1#S4.F6 "Figure 6 ‣ 4.1 Identification strategy ‣ 4 Adressing endogeneity: Instrumental variable (IV) analysis ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") plots the share of women versus the share of men with complete tertiary education, demonstrating substantial cross-country differences. Figure [7](https://arxiv.org/html/2510.18481v1#S4.F7 "Figure 7 ‣ 4.1 Identification strategy ‣ 4 Adressing endogeneity: Instrumental variable (IV) analysis ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") further details this variation by ranking countries according to the gender gap (‘share of women’ minus ‘share of men’), showing that the gap is negative for almost all the countries we are interested in, indicating lower rates of higher education for women.

Figure 6:  Disparities in tertiary education between women and men in 1960

|  |  |
| --- | --- |
| All the countries | Southwest zoom |
| Refer to caption | Refer to caption |

Reading: In 1960, in Australia (AUS), approximately 5% of adult women had completed higher education, compared to approximately 10% of adult men.

Source: Educational Attainment Data, Barro and Lee ([2013](https://arxiv.org/html/2510.18481v1#bib.bib4)).




Figure 7:  Gender gaps in tertiary education in 1960

![Refer to caption](x8.png)

Reading: In 1960, in Gabon (GAB), the share of women with complete tertiary education was 0.5% higher than that of men.

Source: Educational Attainment Data, Barro and Lee ([2013](https://arxiv.org/html/2510.18481v1#bib.bib4)).

Our identification strategy relies on the assumption that the gender gap in the parent’s country of origin influences their child’s academic performance exclusively through its effect on that parent’s educational attainment. While this assumption cannot be tested directly, the richness of our data allows us to mitigate most concerns. For instance, one potential issue is that a country’s wealth might be correlated with its gender gap, and that the wealth of the parents’ country of origin could independently influence a child’s academic success. The association between the gender gap in tertiary education and wealth is not confirmed in the literature. By analyzing global educational gender gaps (not only in tertiary education), Minasyan et al. ([2019](https://arxiv.org/html/2510.18481v1#bib.bib27)) show a relative weak correlation of 0.25 with economic growth, and that there is no significant difference when considering per capita income measures instead of growth. Focusing on the gender gap in tertiary education, Huber and Paule-Paludkiewicz ([2024](https://arxiv.org/html/2510.18481v1#bib.bib21)) show that it can be negative or positive regardless of wealth, and establish that the difference between countries is partially explained by differences in social norms, relating to gender, within each country.141414For example, the United States, which in 1960 was the richest country in the world, had the 9th9^{\textnormal{th}} most unequal gender gap in completed tertiary education in our database, among the 115 countries observed.

The causal effect of the parent’s highest level education on child’s score is estimated using a two-stage least squares (2SLS) model. We first regress the endogenous variable, the parents’ highest level of education (PHE, which can take three values, namely 0, 1 and 2 for, respectively, ISCED 0–2, 3–5, and 6–8), on the instrument, the gender gap in tertiary education (GG), including all the exogenous controls presented in regression ([1](https://arxiv.org/html/2510.18481v1#S3.E1 "In 3.1 Impact of parent’s highest level of education ‣ 3 Initial estimation strategy and results ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.")). As in Figure [7](https://arxiv.org/html/2510.18481v1#S4.F7 "Figure 7 ‣ 4.1 Identification strategy ‣ 4 Adressing endogeneity: Instrumental variable (IV) analysis ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments."), the gender gap is calculated as the difference between the share of women and the share of men who have completed higher education. The first-stage equation is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | PHEi=π0+π1​GGi+∑kσk​sk​i+∑kλk​hk​i+at+bs+νi​t​s.\textnormal{PHE}\_{i}=\pi\_{0}+\pi\_{1}\textnormal{GG}\_{i}+\textstyle\sum\_{k}\sigma\_{k}\,s\_{ki}+\textstyle\sum\_{k}\lambda\_{k}\,h\_{ki}+a\_{t}+b\_{s}+\nu\_{its}\,. |  | (3) |

A negative value for π1\pi\_{1} can be expected, which would mean that the greater the gender inequality in education in the country of origin, the more educated parents tend to be. The literature explains this pattern through selective migration. For foreign parents, most of whom come from developing countries in our study, migration can be perceived as an opportunity.151515By examining the Great Migration (1940–1970), during which millions of African Americans left the segregationist South for cities in the North, Derenoncourt ([2022](https://arxiv.org/html/2510.18481v1#bib.bib13)) challenges the notion that moving to areas offering better opportunities systematically guarantees greater intergenerational social mobility. Because of mobility costs and spatial frictions, it is typically the most educated who are able to migrate Schmutz et al. ([2021](https://arxiv.org/html/2510.18481v1#bib.bib34)); Bergman et al. ([2024](https://arxiv.org/html/2510.18481v1#bib.bib6)). This pattern is, for instance, confirmed in Black et al. ([2006](https://arxiv.org/html/2510.18481v1#bib.bib8)) on the basis of three concrete case studies (Kerala in India, Bangladesh, and Albania).

We then use the predicted values of parents’ highest level of education (PHE^i\widehat{\textnormal{PHE}}\_{i}) from the first stage to estimate the impact on student scores (yi​t​sy\_{its}). The second-stage equation is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | yi​t​s=α0+α1​PHE^i+∑kβk​sk​i+∑kγk​hk​i+at+bs+ϵi​t​s.y\_{its}=\alpha\_{0}+\alpha\_{1}\widehat{\textnormal{PHE}}\_{i}+\textstyle\sum\_{k}\beta\_{k}\,s\_{ki}+\textstyle\sum\_{k}\gamma\_{k}\,h\_{ki}+a\_{t}+b\_{s}+\epsilon\_{its}\,. |  | (4) |

In this framework, the coefficient α1\alpha\_{1} represents the causal effect of parents’ highest level of education on student academic achievement. This regression is therefore equivalent to Equation ([1](https://arxiv.org/html/2510.18481v1#S3.E1 "In 3.1 Impact of parent’s highest level of education ‣ 3 Initial estimation strategy and results ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.")), but with an instrumented version of parents’ highest level of education, and without it being put into dummy variables (which would have required a larger number of instruments, which could have posed potential problems in terms of validity).

As in Section [3](https://arxiv.org/html/2510.18481v1#S3 "3 Initial estimation strategy and results ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments."), we complete the previous regression with interaction components between parental highest education and the student’s grade level. Again, we compare the grades two by two (3 vs. 6, 6 vs. 10 and 3 vs. 10), running a regression for each possible grades pair (u,v)(u,v) where u<vu<v, and excluding the non-concerned third grade. With gg indicating the grade, we introduce a dummy variable I​(u,v)I(u,v) which takes the value 0 if g=ug=u (reference grade), and 11 if g=vg=v. When we compare the grades uu and vv, we obtain the following expression, with g∈{u,v}g\in\{u,v\}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | yi​g​t​s=α0+α1​PHE^i+η​I​(u,v)+α2​PHE^i​I​(u,v)+∑kβk​sk​i+∑kγk​hk​i+at+bs+ϵi​g​t​s.y\_{igts}=\alpha\_{0}+\alpha\_{1}\widehat{\textnormal{PHE}}\_{i}+\eta I(u,v)+\alpha\_{2}\widehat{\textnormal{PHE}}\_{i}I(u,v)+\textstyle\sum\_{k}\beta\_{k}\,s\_{ki}+\textstyle\sum\_{k}\gamma\_{k}\,h\_{ki}+a\_{t}+b\_{s}+\epsilon\_{igts}\,. |  | (5) |

This regression is the instrumented version of Equation ([2](https://arxiv.org/html/2510.18481v1#S3.E2 "In 3.1 Impact of parent’s highest level of education ‣ 3 Initial estimation strategy and results ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.")). Again the η\eta coefficient–which indicates the extra points obtained on average by the students in Grade vv, compared with Grade uu, whatever the parent group–is not informative due to the normalisation of the scores. The coefficient we are interest in is α2\alpha\_{2}, which corresponds to the average impact, from Grade uu to Grade vv, of a one-level increase in the highest level of parental education (among the three possible levels).

### 4.2 Results

The results of the instrumental variable estimations of Equations ([3](https://arxiv.org/html/2510.18481v1#S4.E3 "In 4.1 Identification strategy ‣ 4 Adressing endogeneity: Instrumental variable (IV) analysis ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.")) and ([4](https://arxiv.org/html/2510.18481v1#S4.E4 "In 4.1 Identification strategy ‣ 4 Adressing endogeneity: Instrumental variable (IV) analysis ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.")) for the three subjects (mathematics, literature and English), aggregating all grade levels, are presented in Table [1](https://arxiv.org/html/2510.18481v1#S4.T1 "Table 1 ‣ 4.2 Results ‣ 4 Adressing endogeneity: Instrumental variable (IV) analysis ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.").

Table 1: Global and causal impact (IV) of parents’ highest level of education on student’s score

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1) | (2) | (3) |
|  | Mathematics | Literature | English |
| First stage: Impact of gender gap in tertiary education (GG) | | | |
| on parents’ highest level of education (PHE) | | | |
| Gender gap in tertiary education | -0.051\*\*\* | -0.051\*\*\* | -0.052\*\*\* |
|  | (0.003) | (0.003) | (0.003) |
| F-test of excluded instrument | 248.06\*\*\* | 242.11\*\*\* | 250.91\*\*\* |
| Reduced form: Impact of GG on student’s score | | | |
| Gender gap in tertiary education | -1.86\*\*\* | -2.634\*\*\* | -3.764\*\*\* |
|  | (0.533) | (0.568) | (0.487) |
| Second stage: Impact of PHE, instrumented by GG, on student’s score | | | |
| Parents highest education | 37.46\*\*\* | 51.30\*\*\* | 72.47\*\*\* |
|  | (10.46) | (11.36) | (9.89) |
| Academic Year FE | Yes | Yes | Yes |
| School FE | Yes | Yes | Yes |
| Child’s characteristics | Yes | Yes | Yes |
| Household’s characteristics | Yes | Yes | Yes |
| Observations | 297491 | 299350 | 297851 |
| Standard errors in parentheses | | | |
| \* p<0.10p<0.10, \*\* p<0.05p<0.05, \*\*\* p<0.01p<0.01 | | | |

The first-stage results show a strong and significant relationship between our instrument, the gender gap in tertiary education (GG), and the endogenous variable, parents’ highest level of education (PHE). The coefficient on the gender gap is negative and statistically significant across all three subjects (approximately -0.05). This suggests that a larger gender gap in the parents’ country of origin, which indicates lower educational attainment for women, is associated with a higher level of education for the parents in our sample, consistent with a selective migration pattern. The F-statistics for the excluded instrument are well above conventional thresholds for weak instruments, with values of 248.06 for mathematics, 242.11 for literature, and 250.91 for English, confirming the instrument’s strength. The reduced-form estimates confirm a statistically significant negative relationship between the gender gap and children’s scores across all subjects.

The second-stage results in Table [1](https://arxiv.org/html/2510.18481v1#S4.T1 "Table 1 ‣ 4.2 Results ‣ 4 Adressing endogeneity: Instrumental variable (IV) analysis ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.") reveal a positive and significant causal effect of parents’ highest education on their children’s academic scores in all subjects. An increase in the parents’ education level (recalling that we have three possible values, 0, 1 and 2) leads to a score increase of 37.46 points in mathematics, 51.30 points in literature, and 72.47 points in English. These results confirm that the parental environment has a substantial causal influence on student achievement after addressing potential endogeneity (persistent effect). These results also establish that the impact appears to be stronger in English, which confirms our observations in Section [3](https://arxiv.org/html/2510.18481v1#S3 "3 Initial estimation strategy and results ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.").

Table LABEL:IV\_by\_grade\_reformatted presents, still on the basis of Equations ([3](https://arxiv.org/html/2510.18481v1#S4.E3 "In 4.1 Identification strategy ‣ 4 Adressing endogeneity: Instrumental variable (IV) analysis ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.")) and ([4](https://arxiv.org/html/2510.18481v1#S4.E4 "In 4.1 Identification strategy ‣ 4 Adressing endogeneity: Instrumental variable (IV) analysis ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.")), the results disaggregated by grade level, allowing us to observe the evolution of this causal impact. In all grade-level regressions, the first-stage F-statistics are robust, ranging from 65.45 to 99.80, which supports the validity of the instrument across all subsamples. Now we focus on analyzing the results of the second-stage. One clear fact is the similar trend in mathematics and literature. The causal effect of parents’ highest education is positive and significant in Grade 3 (at 1%) and Grade 6 (at 5%), but decreasing between the two grade levels. By Grade 10, the effect becomes statistically insignificant. In contrast to the other subjects, the causal effect of parents’ education on English scores remains positive and statistically significant across all three grades (always at 1%). While the magnitude of the coefficient decreases between Grade 6 and Grade 10, the influence of parental education persists strongly into adolescence for foreign language learning. As an illustration, in Grade 10, an increase in the parents’ education level leads, on average, to an insignificant increase of about 10 points in mathematics and literature, and a significant increase of more than 50 points in English. This pattern seems to confirm that the causal influence of parental education on mathematics and literature performance diminishes as the child gets older, while it increases in English (Matthew effect), as established in Section [3](https://arxiv.org/html/2510.18481v1#S3 "3 Initial estimation strategy and results ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.").

We now discuss the estimation results of Equation ([5](https://arxiv.org/html/2510.18481v1#S4.E5 "In 4.1 Identification strategy ‣ 4 Adressing endogeneity: Instrumental variable (IV) analysis ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.")), which includes an interaction term between parental highest education and the student’s grade level. These results are summarised in Tables LABEL:G3-G6-IV, LABEL:G6-G10-IV and LABEL:G3-G10-IV for, respectively, the transition from Grade 3 to Grade 6, Grade 6 to Grade 10, and Grade 3 to Grade 10. Once again, the causal effect of the variable ‘parents’ highest level of education’ remains positive and significant, regardless of the subject and regardless of the econometric specification. We are now interested in the marginal impact from one grade to another, considering only estimates that include all control variables. These results can be viewed in Figure [8](https://arxiv.org/html/2510.18481v1#S4.F8 "Figure 8 ‣ 4.2 Results ‣ 4 Adressing endogeneity: Instrumental variable (IV) analysis ‣ Parental environment and student achievement: Does a Matthew effect exist? 1footnote 11footnote 1This paper is part of the research project MaDimIn (Contract ANR-24-CE26-3823-02), from which financial support is acknowledged. This paper was written when Brice Magdalou was on a temporary CNRS research assignment at the Aix-Marseille School of Economics. We acknowledge financial support from the French government under the “France 2030” investment plan managed by the French National Research Agency Grant ANR-17-EURE-0020, and by the Excellence Initiative of Aix-Marseille University - A*MIDEX. We are grateful to Elena Bárcena-Mártin, Nicolas Gravel, Markus Jäntti, Jo Thori Lind, Vito Peragine, Rafael Salas, Daniel Santín and Alain Trannoy for their useful comments.").

Figure 8: Marginal and causal impact (IV) of parents’ highest level of education on student’s score

![Refer to caption](Graph-interactions-IV.png)

Reading: Between Grades 3 and 6 in literature, increasing the parents’ highest level of education (among the three possible categories: ISCED 0–2, ISCED 3–5 and ISCED 6–8) by one category increases the score by an average of 14.26 points. Thereafter, between Grade 6 and Grade 10 in literature, the marginal impact of a higher category for the parents’ highest level of education, on the student’s score, is reduced by an average of 15.37 points. ±\pm standard deviation around the line.

In mathematics, between Grades 3 and 6, a one-category increase in the parent’s level of education leads, on average, to a slight increase (significant at only 10%) of 2.8 points of the student’s score. Then, between Grades 6 and 10, this impact is significantly negative (-14.5 points). The trend is similar in literature, except that the positive impact is significant between Grades 3 and 6 (+14.3 points). As in mathematics, it is then negative and significant between Grades 6 and 10 (-15.4 points). The results for these two subjects confirm a general downward trend in the impact of parents’ level of education on student’s score in mathematics between the ages of 8 and 15, and a bell-shaped trend in literature. The pattern in English is completely different. The marginal impact remains strongly positive (and significant) between Grades 3 and 6 (+13.9 points), and Grades 6 and 10 (+15.5 points). Overall, between Grades 3 and 10, the marginal impact decreases in mathematics and literature (by -4.7 and -2.6 points, respectively) while it increases by 32.5 points in English.

To sum up, these instrumental variable estimates reinforce the findings from our initial OLS models, providing stronger causal evidence for a mixed Matthew effect: the influence of the parental environment diminishes for mathematics and literature as students mature (with a bell-shaped curve in literature), but it is unambiguously amplified in foreign language acquisition.

## 5 Discussion, related literature, and policy implications

Matthew effect in education. Few empirical studies have attempted to test the Matthew effect hypothesis in education, most of them applied to reading abilities and its impact on acquisition of literacy (and other related skills). They all agree that the differences in reading abilities in the early education stages continue on until adulthood Cunningham and Stanovich ([1997](https://arxiv.org/html/2510.18481v1#bib.bib12)); Rigney ([2010](https://arxiv.org/html/2510.18481v1#bib.bib31)), but the results are mixed on the existence of a Matthew effect: There is not a strong support for a pattern of widening or decreasing achievement differences Pfost et al. ([2014](https://arxiv.org/html/2510.18481v1#bib.bib29)). Some papers find that the effect is strongly increasing Awaida and Beech ([1995](https://arxiv.org/html/2510.18481v1#bib.bib1)); Howley ([2001](https://arxiv.org/html/2510.18481v1#bib.bib20)) , others that it is intermediate Bast and Reitsma ([1998](https://arxiv.org/html/2510.18481v1#bib.bib5)) and some that it is not even significant or related to social background Shawitz et al. ([1995](https://arxiv.org/html/2510.18481v1#bib.bib35)); Protopapas et al. ([2011](https://arxiv.org/html/2510.18481v1#bib.bib30)). But no study has tested, on a unified database, the existence of a possible Matthew effect on the core subjects of mathematics, literature and the main foreign language (in our case English).

While our study confirms a persistent impact of parental environment on child’s academic performance (a fact widely accepted since the Coleman report, 1966), the results differ between subjects as regards the Matthew effect. From age 11 to 15, the effect of parent’s level of education decreases in mathematics and literature, while it increases in English. At age of 15, spending ‘5 days or more’ doing homework (compared with ‘one day or less’) increases child achievement, but more strongly in literature than in mathematics, and more strongly in mathematics than in English. Similarly, at the same age, the impact of ‘the frequency with which parents talk to their child about school’ is stronger in English, followed by mathematics and then by literature (although the order is reversed at age 8).

To sum up, these results therefore reflect a partial emancipation (from the influence of parental environment) in mathematics and literature, while social determinism increases in English. In the first two subjects, the results echo the work of cognitive psychology initiated by Jean Piaget, according to which the child is partly master of his or her own development: They have an intrinsic ability to learn, without this necessarily being transmitted by others, and their strategies and involvement play a role in their academic performance Onatsu-Arvilomni and Nurmi ([2000](https://arxiv.org/html/2510.18481v1#bib.bib28)). The notion of an age of consent (for responsible choice) can therefore make sense, including in education, and this age can be set between 12 and 16, as proposed by Hufe et al. ([2017](https://arxiv.org/html/2510.18481v1#bib.bib22)).

Conversely, our results confirm the social dimension of learning a foreign language, compared with other academic subjects. In that case, external factors appear to play a decisive role in the learning process Vygotsky ([1978](https://arxiv.org/html/2510.18481v1#bib.bib37)). In addition, the theory of Cunha and Heckman ([2007](https://arxiv.org/html/2510.18481v1#bib.bib10)) which describes a path-dependency in the formation of cognitive skills, seems to be confirmed. As Gardner ([1968](https://arxiv.org/html/2510.18481v1#bib.bib17)) and Dornyei ([1998](https://arxiv.org/html/2510.18481v1#bib.bib14)) point out, the acquisition of a new language involves a great deal of integrative motivation (in the sense that people are interested in learning a language because they want to communicate with the other language community), and parents play a crucial role in encouraging this integrative motivation (as opposed to instrumental motivation). According to Gardner ([1968](https://arxiv.org/html/2510.18481v1#bib.bib17)), parents play two roles in their child’s success in learning a second language: an active role which consists of actively and consciously encouraging their child to learn the language, and a (more important) passive role, which consists of the attitudes that parents have towards the community whose language their child is learning.

Policy implications. Our results, which need to be confirmed using other databases and complementary methodologies, have several implications for educational policies. The first concerns remediation programmes, aimed at improving the skills of children experiencing difficulties. The second concerns national selection processes in higher education (‘Grandes Ecoles’ in France, for instance), which include foreign language skills as a criterion for admission.

With regard to remedial programmes, the main recommendation resulting from the empirical estimates of Cunha and Heckman ([2007](https://arxiv.org/html/2510.18481v1#bib.bib10)) and Cunha et al. ([2010](https://arxiv.org/html/2510.18481v1#bib.bib11)) is to focus (adolescent) remediation strategies for disadvantaged children on the development of non-cognitive skills. Our results indicate that programmes focusing on cognitive skills can also be effective, particularly in mathematics. These results are in line with those of Bahr ([2007](https://arxiv.org/html/2510.18481v1#bib.bib2), [2008](https://arxiv.org/html/2510.18481v1#bib.bib3)), who assesses US postsecondary remediation programmes. He first observes that the degree of deficiency (depth) and the number of deficient basic skill areas (breadth) are good predictors of successful math remediation: Those who require the least remediation are the most likely to remediate successfully. But he also observes that when remediation works (at a low rate, unfortunately) it works extremely well: ‘students who remediate successfully in mathematics exhibit attainment that is comparable to that of students who achieve college mathematics skill without the need for remediation’ (Bahr, [2008](https://arxiv.org/html/2510.18481v1#bib.bib3), Page 442).

The second implication in terms of public education policy concerns the weight of foreign languages in the selection process to access higher education, at different levels. We have found that parents’ education and involvement are essential factors in children’s success in learning a foreign language. What’s more, the child’s effort has (slightly) less impact on results than in subjects such as mathematics or literature. This is a strong sign of inequality of opportunity, and including foreign languages as an admission criterion reinforces this inequality. It therefore seems essential that educational systems give a high priority to foreign language teaching, particularly in non-English-speaking countries, from an early age, so as not to further penalise children from socially disadvantaged backgrounds.

## References

* Awaida and Beech (1995)

  Awaida, M. and Beech, J. (1995). Children’s lexical and
  sublexical development while learning to read. Journal of
  Experimental Education, 63, 97–113.
* Bahr (2007)

  Bahr, P. (2007). Double jeopardy: Testing the effects of multiple
  basic skill deficiencies on successful remediation. Research in
  Higher Education, 48(6), 695–725.
* Bahr (2008)

  — (2008). Does mathematics remediation work?: A comparative analysis
  of academic attainment among community college students. Research in
  Higher Education, 49(5), 420–450.
* Barro and Lee (2013)

  Barro, R. and Lee, J.-W. (2013). A new data set of
  educational attainment in the world, 1950-2010. Journal of
  Development Economics, 104, 184–198.
* Bast and Reitsma (1998)

  Bast, J. and Reitsma, P. (1998). Analyzing the development of
  individual differences in terms of matthew effects in reading: Results from a
  dutch longitudinal study. Developmental Psychology, 34(6),
  1373–1399.
* Bergman et al. (2024)

  Bergman, P., Chetty, R., DeLuca, S.,
  Hendren, N., Katz, L. F. and Palmer, C. (2024).
  Creating moves to opportunity: Experimental evidence on barriers to
  neighborhood choice. American Economic Review, 114 (5),
  1281–1337.
* Bingley et al. (2022)

  Bingley, P., Cappellari, L. and Tatsiramos, K.
  (2022). Parental assortative mating and the intergenerational transmission of
  human capital. Labor Economics, 77, 102047.
* Black et al. (2006)

  Black, R., Natali, C. and Skinner, J. (2006).
  Migration and inequality. Washington: World Bank.
* Cordero et al. (2018)

  Cordero, J. M., Cristóbal, V. and Santín, D.
  (2018). Causal inference on education policies: A survey of empirical studies
  using PISA, TIMSS and PIRLS. Journal of Economic Surveys,
  32 (3), 878–915.
* Cunha and Heckman (2007)

  Cunha, F. and Heckman, J. (2007). The technology of skill
  formation. American Economic Review P&P, 97, 31–47.
* Cunha et al. (2010)

  —, — and Schennach, S. (2010). Estimating the
  technology of cognitive and noncognitive skill formation.
  Econometrica, 78(3), 883–931.
* Cunningham and Stanovich (1997)

  Cunningham, A. and Stanovich, K. (1997). Early reading
  acquisition and its relation to reading experience and ability 10 years
  later. Developmental Psychology, 33(6), 934–945.
* Derenoncourt (2022)

  Derenoncourt, E. (2022). Can you move to opportunity? evidence from
  the great migration. American Economic Review, 112 (2),
  369–408.
* Dornyei (1998)

  Dornyei, Z. (1998). Motivation in second and foreign language
  learning. Language Teaching, 31(1), 117–135.
* Edwards et al. (2022)

  Edwards, R., Gibson, R., Harmon, C. and
  Schurer, S. (2022). First in their families at university: Can
  non-cognitive skills compensate for social origin? Economics of
  Education Review, 91, 102318.
* Eika et al. (2019)

  Eika, L., Mogstad, M. and Zafar, B. (2019).
  Educational assortative mating and household income inequality.
  Journal of Political Economy, 127(6), 2795–2835.
* Gardner (1968)

  Gardner, R. (1968). Attitudes and motivation: Their role in
  second-language acquisition. TESO Quaterly, 2(3),
  141–150.
* Hanushek et al. (2021)

  Hanushek, E., Jacobs, B., Schwerdt, G.,
  van der Velden, R., Vermeulen, S. and S., W.
  (2021). The intergenerational transmission of cognitive skills: An
  investigation of the causal impact of families on student outcomes, ISA
  Discussion Paper No.14854.
* Holmlund et al. (2011)

  Holmlund, H., Lindhal, M. and Plug, E. (2011). The
  causal effect of parents’ schooling on children’s schooling: A comparison of
  estimation methods. Journal of Economic Literature, 49(3),
  615–651.
* Howley (2001)

  Howley, C. (2001). The matthew principle: A west virginia replication?
  Education Policy Analysis Archives, 3(18).
* Huber and Paule-Paludkiewicz (2024)

  Huber, S. J. and Paule-Paludkiewicz, H. (2024). Gender norms
  and the gender gap in higher education. Labour Economics,
  87, 102491.
* Hufe et al. (2017)

  Hufe, P., Peichl, A., Roemer, J. and
  Ungerer, M. (2017). Inequality of income acquisition: The role of
  childhood circumstances. Social Choice and Welfare, 49,
  499–544.
* Jaoul-Grammare and Magdalou (2013)

  Jaoul-Grammare, M. and Magdalou, B. (2013). Opportunities in
  higher education: An application to france. Annals of Economics and
  Statistics, 111-112, 295–325.
* Lefranc et al. (2009)

  Lefranc, A., Pistolesi, N. and Trannoy, A. (2009).
  Equality of opportunity and luck: Definitions and testables conditions, with
  an application to income in France. Journal of Public Economics,
  93, 1189–1207.
* Masters and Wright (1997)

  Masters, G. and Wright, B. (1997). The partial credit model.
  In W. van der Linden and R. Hambleton (eds.), Handbook of Modern Item
  Response Theory, Chapter 6, New York: Springer Science and
  Business Media, LLC, pp. 101–122.
* Merton (1968)

  Merton, R. (1968). The matthew effect in science. Science,
  159, 56–63.
* Minasyan et al. (2019)

  Minasyan, A., Zenker, J., Klasen, S. and
  Vollmer, S. (2019). Educational gender gaps and economic growth: A
  systematic review and meta-regression analysis. World Development,
  122, 199–217.
* Onatsu-Arvilomni and Nurmi (2000)

  Onatsu-Arvilomni, T. and Nurmi, J. (2000). The role of
  task-avoidant and task-focused behaviors in the development of reading and
  mathematical skills during the first school year: A cross-lagged longitudinal
  study. Journal of Educational Psychology, 92(3), 478–491.
* Pfost et al. (2014)

  Pfost, M., Hattie, J., Dörfler, T. and
  Artelt, C. (2014). Individual differences in reading development: A
  review of 25 years of empirical research on matthew effects in reading.
  Review of Educational Research, 84(2), 122–136.
* Protopapas et al. (2011)

  Protopapas, A., Sideridis, G. D., Mouzaki, A. and
  Simos, P. G. (2011). Matthew effects in reading comprehension: Myth
  or reality? Journal of Learning Disabilities, 44(5),
  402–420.
* Rigney (2010)

  Rigney, D. (2010). The Matthew Effect: How Advantage Begests
  Further Advantage. New York: Columbia University Press.
* Roemer and Trannoy (2016)

  Roemer, J. and Trannoy, A. (2016). Equality of opportunity:
  Theory and measurement. Journal of Economic Literature,
  54(4), 1288–1332.
* Sacerdote (2007)

  Sacerdote, B. (2007). How large are the effects from changes in family
  environment? A study of Korean American adoptees. Quarterly
  Journal of Economics, 122, 119–157.
* Schmutz et al. (2021)

  Schmutz, B., Sidibé, M. and Vidal-Naquet, E.
  (2021). Why are low-skilled workers less mobile? the role of mobility costs
  and spatial frictions. Annals of Economics and Statistics,
  142, 283–304.
* Shawitz et al. (1995)

  Shawitz, B., Holford, T., Holahan, J.,
  Fletcher, J., Stuebing, K., Francis, D. and
  Shaywitz, S. (1995). A Matthew effect for IQ but not for
  reading: Results from a longitudinal study. Reading Research
  Quarterly, 30(4), 613–625.
* Suhonen and Karhunen (2019)

  Suhonen, T. and Karhunen, H. (2019). The intergenerational
  effects of parental higher education: Evidence from changes in university
  accessibility. Journal of Public Economics, 176, 195–217.
* Vygotsky (1978)

  Vygotsky, L. (1978). Mind in society: The development of
  higher psychological processes. Massachusetts: Harvard University Press.

## Appendix A Appendix

Figure 9:  CDFs of literature scores according to parents’ highest level of education

|  |  |
| --- | --- |
| Refer to caption | Refer to caption |
| Grade 3 | Grade 10 |




Figure 10:  CDFs of English scores according to parents’ highest level of education

|  |  |
| --- | --- |
| Refer to caption | Refer to caption |
| Grade 3 | Grade 10 |

Table 2: Variables Description

|  | Type | Values | Description |
| --- | --- | --- | --- |
| Students marks | | | |
| Mathematics | Num. | 0 - 1034 | Transformed Mathematics mark |
| Literature | Num. | 0 - 1001 | Transformed Literature mark |
| English (Foreign Language) | Num. | 0 - 845 | Transformed English mark |
| Parents’ highest education | | | |
| Parents’ highest education | Qual. | 0 - 2 | 0 ISCED 0 to 2 |
|  |  |  | 1 ISCED 3 to 5 |
|  |  |  | 2 ISCED 6 to 8 |
| Child’s characteristics | | | |
| Child’s country of birth | Qual. | 1 - 2 | 1 Spain |
|  |  |  | 2 Other |
| Days/week dedicated to homework | Qual. | 1 - 4 | 1 One day or less |
|  |  |  | 2 Two or 3 days |
|  |  |  | 3 Four or 5 days |
|  |  |  | 4 More than 5 |
| Child’s gender | Qual. | 1 - 2 | 1 Female |
|  |  |  | 2 Male |
| Household’s characteristics | | | |
| Mother’s country of birth | Qual. | 1 - 2 | 1 Spain |
|  |  |  | 2 Other |
| Father’s country of birth | Qual. | 1 - 2 | 1 Spain |
|  |  |  | 2 Other |
| Freq. books used at home | Qual. | 1 - 4 | 1 Never or almost never |
|  |  |  | 2 One or 2 times/month |
|  |  |  | 3 One or 2 times/week |
|  |  |  | 4 Every or almost every days |
| Freq. computer used at home | Qual. | 1 - 4 | 1 Never or almost never |
|  |  |  | 2 One or 2 times/month |
|  |  |  | 3 One or 2 times/week |
|  |  |  | 4 Every or almost every days |
| Freq. internet used at home | Qual. | 1 - 4 | 1 Never or almost never |
|  |  |  | 2 One or 2 times/month |
|  |  |  | 3 One or 2 times/week |
|  |  |  | 4 Every or almost every days |
| Nb of books at home | Qual. | 1 - 5 | 1 From 0 to 10 |
|  |  |  | 2 From 11 to 50 |
|  |  |  | 3 From 51 to 100 |
|  |  |  | 4 From 101 to 200 |
|  |  |  | 5 More than 200 |
| Mother’s labour situation | Qual. | 1 - 5 | 1 Full time employee |
|  |  |  | 2 Part time employee |
|  |  |  | 3 Unemployed looking for a job |
|  |  |  | 4 Retired |
|  |  |  | 5 Don’t have and don’t look for a job |
| Father’s labour situation | Qual. | 1 - 5 | 1 Full time employee |
|  |  |  | 2 Part time employee |
|  |  |  | 3 Unemployed looking for a job |
|  |  |  | 4 Retired |
|  |  |  | 5 Don’t have and don’t look for a job |
| Freq. parents talk about school | Qual. | 1 - 4 | 1 Never or almost never |
|  |  |  | 2 One or 2 times/month |
|  |  |  | 3 One or 2 times/week |
|  |  |  | 4 Every or almost every days |
| Freq. parents schedule homework | Qual. | 1 - 4 | 1 Never or almost never |
|  |  |  | 2 One or 2 times/month |
|  |  |  | 3 One or 2 times/week |
|  |  |  | 4 Every or almost every days |
| Freq. parents help for homework | Qual. | 1 - 4 | 1 Never or almost never |
|  |  |  | 2 One or 2 times/month |
|  |  |  | 3 One or 2 times/week |
|  |  |  | 4 Every or almost every days |
| Freq. parents check homework | Qual. | 1 - 4 | 1 Never or almost never |
|  |  |  | 2 One or 2 times/month |
|  |  |  | 3 One or 2 times/week |
|  |  |  | 4 Every or almost every days |
| NN | 327163 |  |  |

Table 2: Variables Description (continued)




Table 3: Summary Statistics

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Mean | Stand. Dev. |  |  |
| Students marks | |  |  |  |
| Mathematics | 517.4546 | 95.00513 |  |  |
| Literature | 505.935 | 101.8927 |  |  |
| English Foreign Language | 517.1402 | 93.7307 |  |  |
| Parents’ highest education | |  |  |  |
| Parents highest education | 1.494245 | .6642053 |  |  |
| Child’s characteristics | |  |  |  |
| Child’s country of birth | 1.044064 | .2052369 |  |  |
| Days/week dedicated to homework | 3.310194 | .7581023 |  |  |
| Child’s gender | 1.502942 | .4999921 |  |  |
| Household’s characteristics | |  |  |  |
| Mother’s country of birth | 1.165642 | .3717597 |  |  |
| Father’s country of birth | 1.159382 | .3660328 |  |  |
| Freq. books used at home | 3.375672 | .837836 |  |  |
| Freq. computer used at home | 3.794766 | .5249957 |  |  |
| Freq. internet used at home | 3.865501 | .4511002 |  |  |
| Nb of books at home | 3.515174 | 1.203279 |  |  |
| Mother’s labour situation | 1.651739 | 1.015354 |  |  |
| Father’s labour situation | 1.303231 | .7056803 |  |  |
| Freq. parents talk about school with child | 3.82281 | .5012083 |  |  |
| Freq. parents schedule homework with child | 3.476625 | .9059994 |  |  |
| Freq. parents help for homework | 2.99286 | 1.098742 |  |  |
| Freq. parents check homework with child | 3.440297 | .9775864 |  |  |
| NN | 327163 |  |  |  |




Table 4: Average scores according to grade level

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1) | (2) | (3) |
|  | Gr.3 | Gr.6 | Gr.10 |
| Mathematics | 513.29 | 521.52 | 519.33 |
| Literature | 514.21 | 489.35 | 522.26 |
| English | 515.02 | 515.77 | 526.17 |
| NN | 145096 | 123811 | 52637 |




Table 5: Average scores according to grade level, by academic year

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) | (9) | (10) | (11) |
|  | 2016 | 2016 | 2017 | 2017 | 2017 | 2018 | 2018 | 2018 | 2019 | 2019 | 2019 |
|  | Gr.3 | Gr.6 | Gr.3 | Gr.6 | Gr.10 | Gr.3 | Gr.6 | Gr.10 | Gr.3 | Gr.6 | Gr.10 |
| Mathematics | 507.1 | 509.8 | 514.5 | 515.3 | 514.1 | 518.1 | 545.5 | 522.9 | 515.9 | 518.4 | 520.9 |
| Literature | 510.5 | 436.3 | 513.3 | 514.8 | 518.7 | 517.6 | 524.1 | 526.5 | 517.0 | 516.6 | 521.1 |
| English | 509.2 | 510.0 | 515.3 | 516.1 | 522.2 | 520.1 | 520.1 | 530.7 | 517.7 | 520.5 | 525.1 |
| NN | 47061 | 44249 | 32390 | 24578 | 18029 | 36535 | 31060 | 19594 | 29110 | 23924 | 15014 |




Table 6: Students distribution according to parent highest education, grade level and academic year

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) | (9) | (10) | (11) |
|  | 2016 | 2016 | 2017 | 2017 | 2017 | 2018 | 2018 | 2018 | 2019 | 2019 | 2019 |
|  | Gr.3 | Gr.6 | Gr.3 | Gr.6 | Gr.10 | Gr.3 | Gr.6 | Gr.10 | Gr.3 | Gr.6 | Gr.10 |
| ISCED 0–2 | 11.15%\% | 10.90%\% | 7.945%\% | 9.520%\% | 9.335%\% | 8.845%\% | 10.15%\% | 8.574%\% | 8.737%\% | 9.296%\% | 8.468%\% |
| ISCED 3–5 | 33.40%\% | 35.43%\% | 29.87%\% | 32.93%\% | 35.53%\% | 28.87%\% | 31.07%\% | 32.08%\% | 26.72%\% | 28.57%\% | 30.14%\% |
| ISCED 6–8 | 55.45%\% | 53.67%\% | 62.19%\% | 57.55%\% | 55.14%\% | 62.28%\% | 58.79%\% | 59.35%\% | 64.54%\% | 62.13%\% | 61.40%\% |
| Total | 100%\% | 100%\% | 100%\% | 100%\% | 100%\% | 100%\% | 100%\% | 100%\% | 100%\% | 100%\% | 100%\% |
| NN | 47081 | 44305 | 33077 | 24706 | 18425 | 36619 | 31036 | 19909 | 29769 | 24644 | 15470 |




Table 7: Impact of parents’ highest level of education – Mathematics

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1) | (2) | (3) |
|  | Mathematics | Mathematics | Mathematics |
| Parents’ highest education | | | |
| ISCED 0–2 | 0 | 0 | 0 |
|  | (.) | (.) | (.) |
| ISCED 3–5 | 15.81∗∗∗ | 16.72∗∗∗ | 10.27∗∗∗ |
|  | (0.479) | (0.517) | (0.589) |
| ISCED 6–8 | 41.40∗∗∗ | 42.92∗∗∗ | 29.70∗∗∗ |
|  | (0.491) | (0.530) | (0.625) |
| Constant | | | |
|  | 482.3∗∗∗ | 486.6∗∗∗ | 476.5∗∗∗ |
|  | (0.499) | (1.150) | (2.661) |
| Academic year fixed-effect | Yes | Yes | Yes |
| School fixed-effect | Yes | Yes | Yes |
| Child’s characteristics | No | Yes | Yes |
| Household’s characteristics | No | No | Yes |
| Observations | 415226 | 367492 | 316294 |
| Adjusted R2R^{2} | 0.160 | 0.172 | 0.204 |
| Standard errors in parentheses | | | |
| ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01 | | | |




Table 8: Impact of parents’ highest level of education – Literature

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1) | (2) | (3) |
|  | Literature | Literature | Literature |
| Parents’ highest education | | | |
| ISCED 0–2 | 0 | 0 | 0 |
|  | (.) | (.) | (.) |
| ISCED 3–5 | 19.25∗∗∗ | 20.27∗∗∗ | 14.28∗∗∗ |
|  | (0.515) | (0.556) | (0.634) |
| ISCED 6–8 | 46.42∗∗∗ | 48.65∗∗∗ | 35.89∗∗∗ |
|  | (0.527) | (0.569) | (0.673) |
| Constant | | | |
|  | 478.3∗∗∗ | 504.4∗∗∗ | 488.8∗∗∗ |
|  | (0.536) | (1.237) | (2.865) |
| Academic year fixed-effect | Yes | Yes | Yes |
| School fixed-effect | Yes | Yes | Yes |
| Child’s characteristics | No | Yes | Yes |
| Household’s characteristics | No | No | Yes |
| Observations | 414805 | 367757 | 316529 |
| Adjusted R2R^{2} | 0.146 | 0.175 | 0.197 |
| Standard errors in parentheses | | | |
| ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01 | | | |




Table 9: Impact of parents’ highest level of education – English

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1) | (2) | (3) |
|  | English | English | English |
| Parents’ highest education | | | |
| ISCED 0–2 | 0 | 0 | 0 |
|  | (.) | (.) | (.) |
| ISCED 3–5 | 21.81∗∗∗ | 21.75∗∗∗ | 16.06∗∗∗ |
|  | (0.437) | (0.471) | (0.535) |
| ISCED 6–8 | 52.55∗∗∗ | 52.34∗∗∗ | 39.68∗∗∗ |
|  | (0.448) | (0.483) | (0.568) |
| Constant | | | |
|  | 473.7∗∗∗ | 492.3∗∗∗ | 468.3∗∗∗ |
|  | (0.455) | (1.048) | (2.418) |
| Academic year fixed-effect | Yes | Yes | Yes |
| School fixed-effect | Yes | Yes | Yes |
| Child’s characteristics | No | Yes | Yes |
| Household’s characteristics | No | No | Yes |
| Observations | 413466 | 365774 | 314863 |
| Adjusted R2R^{2} | 0.293 | 0.303 | 0.329 |
| Standard errors in parentheses | | | |
| ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01 | | | |




Table 10: Impact of parents’ highest level of education according to grade level – Grade 3 vs Grade 6

|  | Mathematics | | | Literature | | | English | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (1) | (2) | (3) | (1) | (2) | (3) |
|  | Math. | Math. | Math. | Lit. | Lit. | Lit. | Engl. | Engl. | Engl. |
| Parents highest education | | | | | | | | | |
| ISCED 0–2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | (.) | (.) | (.) | (.) | (.) | (.) | (.) | (.) | (.) |
| ISCED 3–5 | 18.84∗∗∗ | 19.05∗∗∗ | 12.05∗∗∗ | 19.91∗∗∗ | 20.39∗∗∗ | 13.30∗∗∗ | 18.59∗∗∗ | 19.22∗∗∗ | 13.35∗∗∗ |
|  | (0.757) | (0.762) | (0.864) | (0.845) | (0.840) | (0.950) | (0.698) | (0.700) | (0.794) |
| ISCED 6–8 | 46.16∗∗∗ | 46.16∗∗∗ | 30.22∗∗∗ | 44.50∗∗∗ | 45.18∗∗∗ | 28.44∗∗∗ | 46.57∗∗∗ | 47.07∗∗∗ | 33.11∗∗∗ |
|  | (0.745) | (0.750) | (0.874) | (0.832) | (0.826) | (0.960) | (0.687) | (0.689) | (0.803) |
| Grade 3 vs Grade 6 | | | | | | | | | |
| I(3,6) | 9.017∗∗∗ | 10.49∗∗∗ | -2.856∗∗∗ | -30.56∗∗∗ | -29.72∗∗∗ | -42.57∗∗∗ | -3.799∗∗∗ | -3.022∗∗∗ | -13.54∗∗∗ |
|  | (0.932) | (0.940) | (1.081) | (1.040) | (1.035) | (1.188) | (0.859) | (0.862) | (0.993) |
| Interactions | | | | | | | | | |
| ISCED 0–2 ×\times I(3,6) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | (.) | (.) | (.) | (.) | (.) | (.) | (.) | (.) | (.) |
| ISCED 3–5 ×\times I(3,6) | -0.759 | -1.029 | -1.161 | 1.955 | 2.237∗ | 2.442∗ | 4.857∗∗∗ | 4.882∗∗∗ | 5.017∗∗∗ |
|  | (1.083) | (1.090) | (1.219) | (1.210) | (1.201) | (1.339) | (0.998) | (1.000) | (1.119) |
| ISCED 6–8 ×\times I(3,6) | -0.0122 | 0.0649 | 0.626 | 10.85∗∗∗ | 11.26∗∗∗ | 12.21∗∗∗ | 8.692∗∗∗ | 9.089∗∗∗ | 9.549∗∗∗ |
|  | (1.021) | (1.027) | (1.155) | (1.140) | (1.133) | (1.269) | (0.940) | (0.943) | (1.060) |
| Constant | | | | | | | | | |
|  | 475.5∗∗∗ | 483.6∗∗∗ | 485.8∗∗∗ | 491.3∗∗∗ | 518.2∗∗∗ | 508.6∗∗∗ | 477.8∗∗∗ | 498.6∗∗∗ | 483.3∗∗∗ |
|  | (0.740) | (1.329) | (3.166) | (0.826) | (1.467) | (3.479) | (0.682) | (1.222) | (2.908) |
| Academic year Fixed-Effect | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| School Fixed-Effect | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Child’s characteristics | No | Yes | Yes | No | Yes | Yes | No | Yes | Yes |
| Household’s characteristic | No | No | Yes | No | No | Yes | No | No | Yes |
| Observations | 310508 | 306732 | 264386 | 311019 | 307233 | 264811 | 308884 | 305117 | 263032 |
| Adjusted R2R^{2} | 0.178 | 0.186 | 0.222 | 0.162 | 0.192 | 0.224 | 0.301 | 0.312 | 0.337 |
| Standard errors in parentheses | | | | | | | | | |
| ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01 | | | | | | | | | |
| I​(u,v)I(u,v) is a dummy variable which takes the value 0 if g=ug=u (reference grade), and 1 if g=vg=v | | | | | | | | | |

Table 10: Parents highest education’s impact according to grade level (compared two-by-two) – Mathematics, Literature, and English (continued)




Table 11: Impact of parents’ highest level of education according to grade level – Grade 6 vs Grade 10

|  | Mathematics | | | Literature | | | English | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (4) | (5) | (6) | (4) | (5) | (6) | (4) | (5) | (6) |
|  | Math. | Math. | Math. | Lit. | Lit. | Lit. | Engl. | Engl. | Engl. |
| Parents highest education | | | | | | | | | |
| ISCED 0–2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | (.) | (.) | (.) | (.) | (.) | (.) | (.) | (.) | (.) |
| ISCED 3–5 | 18.40∗∗∗ | 17.86∗∗∗ | 11.03∗∗∗ | 21.82∗∗∗ | 22.05∗∗∗ | 14.96∗∗∗ | 22.10∗∗∗ | 22.29∗∗∗ | 15.87∗∗∗ |
|  | (0.819) | (0.816) | (0.921) | (0.877) | (0.884) | (0.993) | (0.727) | (0.719) | (0.806) |
| ISCED 6–8 | 47.02∗∗∗ | 46.62∗∗∗ | 31.28∗∗∗ | 52.57∗∗∗ | 53.50∗∗∗ | 36.83∗∗∗ | 51.79∗∗∗ | 52.93∗∗∗ | 37.69∗∗∗ |
|  | (0.833) | (0.833) | (0.966) | (0.892) | (0.902) | (1.042) | (0.739) | (0.734) | (0.846) |
| Grade 6 vs Grade 10 | | | | | | | | | |
| I(6,10) | 6.615∗∗∗ | 13.98∗∗∗ | -8.327∗∗∗ | 15.05∗∗∗ | 21.71∗∗∗ | 3.264∗ | -2.601∗∗ | 3.110∗∗ | -10.94∗∗∗ |
|  | (1.205) | (1.506) | (1.696) | (1.297) | (1.637) | (1.837) | (1.069) | (1.326) | (1.484) |
| Interactions | | | | | | | | | |
| ISCED 0–2 ×\times I(6,10) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | (.) | (.) | (.) | (.) | (.) | (.) | (.) | (.) | (.) |
| ISCED 3–5 ×\times I(6,10) | -9.866∗∗∗ | -11.76∗∗∗ | -7.850∗∗∗ | -5.898∗∗∗ | -7.829∗∗∗ | -6.367∗∗∗ | 1.979∗ | 1.604 | 2.445 |
|  | (1.229) | (1.545) | (1.714) | (1.324) | (1.680) | (1.858) | (1.090) | (1.359) | (1.499) |
| ISCED 6–8 ×\times I(6,10) | -19.15∗∗∗ | -20.84∗∗∗ | -13.61∗∗∗ | -15.16∗∗∗ | -17.01∗∗∗ | -11.55∗∗∗ | 7.618∗∗∗ | 6.814∗∗∗ | 9.885∗∗∗ |
|  | (1.220) | (1.529) | (1.700) | (1.314) | (1.662) | (1.842) | (1.083) | (1.346) | (1.488) |
| Constant | | | | | | | | | |
|  | 474.7∗∗∗ | 469.3∗∗∗ | 464.1∗∗∗ | 395.9∗∗∗ | 409.4∗∗∗ | 390.1∗∗∗ | 474.3∗∗∗ | 483.2∗∗∗ | 457.9∗∗∗ |
|  | (0.822) | (1.784) | (4.107) | (0.879) | (1.939) | (4.434) | (0.729) | (1.572) | (3.599) |
| Academic year Fixed-Effect | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| School Fixed-Effect | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Child’s characteristics | No | Yes | Yes | No | Yes | Yes | No | Yes | Yes |
| Household’s characteristic | No | No | Yes | No | No | Yes | No | No | Yes |
| Observations | 248339 | 202678 | 173619 | 247527 | 202556 | 173528 | 247798 | 202173 | 173209 |
| Adjusted R2R^{2} | 0.155 | 0.167 | 0.206 | 0.209 | 0.249 | 0.282 | 0.315 | 0.328 | 0.360 |
| Standard errors in parentheses | | | | | | | | | |
| ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01 | | | | | | | | | |
| I​(u,v)I(u,v) is a dummy variable which takes the value 0 if g=ug=u (reference grade), and 1 if g=vg=v | | | | | | | | | |

Table 11: Parents highest education’s impact according to grade level (compared two-by-two) – Grade 6 vs Grade 10 (continued)




Table 12: Impact of parents’ highest level of education according to grade level – Grade 3 vs Grade 10

|  | Mathematics | | | Literature | | | English | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (7) | (8) | (9) | (7) | (8) | (9) | (7) | (8) | (9) |
|  | Math. | Math. | Math. | Lit. | Lit. | Lit. | Engl. | Engl. | Engl. |
| Parents’ highest education | | | | | | | | | |
| ISCED 0–2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | (.) | (.) | (.) | (.) | (.) | (.) | (.) | (.) | (.) |
| ISCED 3–5 | 18.97∗∗∗ | 19.00∗∗∗ | 12.33∗∗∗ | 21.19∗∗∗ | 21.90∗∗∗ | 15.32∗∗∗ | 19.19∗∗∗ | 19.93∗∗∗ | 14.05∗∗∗ |
|  | (0.769) | (0.765) | (0.877) | (0.751) | (0.745) | (0.850) | (0.711) | (0.708) | (0.806) |
| ISCED 6–8 | 45.24∗∗∗ | 45.39∗∗∗ | 30.08∗∗∗ | 46.60∗∗∗ | 48.01∗∗∗ | 32.75∗∗∗ | 45.51∗∗∗ | 47.29∗∗∗ | 33.20∗∗∗ |
|  | (0.777) | (0.776) | (0.917) | (0.758) | (0.754) | (0.888) | (0.718) | (0.717) | (0.843) |
| Grade 3 vs Grade 10 | | | | | | | | | |
| I(3,10) | 9.617∗∗∗ | 17.89∗∗∗ | -12.96∗∗∗ | 9.118∗∗∗ | 16.65∗∗∗ | -8.665∗∗∗ | -11.74∗∗∗ | -5.893∗∗∗ | -28.24∗∗∗ |
|  | (1.163) | (1.463) | (1.707) | (1.140) | (1.428) | (1.661) | (1.072) | (1.348) | (1.565) |
| Interactions | | | | | | | | | |
| ISCED 0–2 ×\times I(3,10) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | (.) | (.) | (.) | (.) | (.) | (.) | (.) | (.) | (.) |
| ISCED 3–5 ×\times I(3,10) | -10.50∗∗∗ | -12.24∗∗∗ | -8.859∗∗∗ | -5.154∗∗∗ | -7.210∗∗∗ | -6.144∗∗∗ | 4.794∗∗∗ | 4.653∗∗∗ | 5.232∗∗∗ |
|  | (1.187) | (1.500) | (1.684) | (1.165) | (1.466) | (1.639) | (1.094) | (1.382) | (1.543) |
| ISCED 6–8 ×\times I(3,10) | -16.23∗∗∗ | -16.64∗∗∗ | -9.076∗∗∗ | -7.959∗∗∗ | -9.132∗∗∗ | -3.856∗∗ | 16.01∗∗∗ | 16.55∗∗∗ | 19.72∗∗∗ |
|  | (1.175) | (1.484) | (1.675) | (1.152) | (1.449) | (1.630) | (1.083) | (1.368) | (1.535) |
| Constant | | | | | | | | | |
|  | 474.8∗∗∗ | 482.1∗∗∗ | 480.3∗∗∗ | 475.5∗∗∗ | 499.9∗∗∗ | 488.1∗∗∗ | 478.4∗∗∗ | 497.2∗∗∗ | 478.7∗∗∗ |
|  | (0.769) | (1.410) | (3.225) | (0.750) | (1.373) | (3.129) | (0.712) | (1.304) | (2.961) |
| Academic year Fixed-Effect | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| School Fixed-Effect | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Child’s characteristics | No | Yes | Yes | No | Yes | Yes | No | Yes | Yes |
| Household’s characteristic | No | No | Yes | No | No | Yes | No | No | Yes |
| Observations | 271605 | 225574 | 194583 | 271064 | 225725 | 194719 | 270250 | 224258 | 193485 |
| Adjusted R2R^{2} | 0.180 | 0.200 | 0.225 | 0.152 | 0.176 | 0.205 | 0.302 | 0.314 | 0.337 |
| Standard errors in parentheses | | | | | | | | | |
| ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01 | | | | | | | | | |
| I​(u,v)I(u,v) is a dummy variable which takes the value 0 if g=ug=u (reference grade), and 1 if g=vg=v | | | | | | | | | |

Table 12: Parents highest education’s impact according to grade level (compared two-by-two) – Mathematics, Literature, and English (continued)




Table 13: Impact of parental investment and student’s effort

|  | Mathematics | | | Literature | | | English | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) | (9) |
|  | Gr.3 | Gr.6 | Gr.10 | Gr.3 | Gr.6 | Gr.10 | Gr.3 | Gr.6 | Gr.10 |
| Parents’ highest education | | | | | | | | | |
| ISCED 0–2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | (.) | (.) | (.) | (.) | (.) | (.) | (.) | (.) | (.) |
| ISCED 3–5 | 12.04∗∗∗ | 10.99∗∗∗ | 3.304∗∗ | 15.27∗∗∗ | 14.68∗∗∗ | 7.688∗∗∗ | 14.71∗∗∗ | 16.40∗∗∗ | 16.46∗∗∗ |
|  | (0.861) | (0.909) | (1.496) | (0.864) | (1.054) | (1.325) | (0.806) | (0.806) | (1.290) |
| ISCED 6–8 | 30.01∗∗∗ | 30.84∗∗∗ | 17.90∗∗∗ | 32.99∗∗∗ | 35.96∗∗∗ | 24.54∗∗∗ | 35.62∗∗∗ | 39.08∗∗∗ | 42.99∗∗∗ |
|  | (0.914) | (0.972) | (1.584) | (0.917) | (1.128) | (1.403) | (0.855) | (0.862) | (1.366) |
| Days/week dedicated to homework | | | | | | | | | |
| One day or less | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | (.) | (.) | (.) | (.) | (.) | (.) | (.) | (.) | (.) |
| 2 or 3 days | -0.185 | 2.338 | 9.076∗∗∗ | -2.184 | 7.045∗∗∗ | 9.176∗∗∗ | -0.957 | 3.693∗ | 3.954 |
|  | (1.533) | (2.288) | (2.978) | (1.538) | (2.658) | (2.648) | (1.437) | (2.030) | (2.572) |
| 4 or 5 days | -3.599∗∗ | 5.090∗∗ | 10.51∗∗∗ | -5.920∗∗∗ | 10.56∗∗∗ | 14.59∗∗∗ | -5.995∗∗∗ | 4.559∗∗ | 7.796∗∗∗ |
|  | (1.516) | (2.194) | (2.863) | (1.521) | (2.548) | (2.545) | (1.421) | (1.947) | (2.473) |
| More than 5 | -10.90∗∗∗ | 4.527∗∗ | 14.05∗∗∗ | -15.81∗∗∗ | 9.282∗∗∗ | 19.23∗∗∗ | -14.08∗∗∗ | 3.986∗∗ | 12.68∗∗∗ |
|  | (1.548) | (2.203) | (2.866) | (1.553) | (2.558) | (2.548) | (1.451) | (1.955) | (2.476) |
| Freq. parents talk about school | | | | | | | | | |
| Never or almost never | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | (.) | (.) | (.) | (.) | (.) | (.) | (.) | (.) | (.) |
| 1 or 2 times/month | 5.461 | -0.716 | 4.868∗ | 2.225 | -1.567 | -0.793 | 0.894 | -0.611 | 3.610 |
|  | (4.141) | (3.151) | (2.705) | (4.152) | (3.661) | (2.394) | (3.862) | (2.798) | (2.339) |
| 1 or 2 times/week | 9.676∗∗∗ | 2.266 | 6.345∗∗∗ | 10.45∗∗∗ | 7.938∗∗∗ | 4.034∗∗ | 4.841 | 4.593∗ | 9.155∗∗∗ |
|  | (3.545) | (2.650) | (2.303) | (3.553) | (3.077) | (2.038) | (3.299) | (2.353) | (1.992) |
| Every or almost every day | 10.57∗∗∗ | 4.455∗ | 9.023∗∗∗ | 16.06∗∗∗ | 14.41∗∗∗ | 8.285∗∗∗ | 8.704∗∗∗ | 9.119∗∗∗ | 12.91∗∗∗ |
|  | (3.485) | (2.585) | (2.228) | (3.492) | (3.001) | (1.970) | (3.243) | (2.295) | (1.927) |
| Constant | | | | | | | | | |
|  | 482.3∗∗∗ | 473.2∗∗∗ | 470.8∗∗∗ | 491.0∗∗∗ | 472.2∗∗∗ | 463.2∗∗∗ | 483.7∗∗∗ | 463.5∗∗∗ | 441.5∗∗∗ |
|  | (4.572) | (4.881) | (9.367) | (4.582) | (5.657) | (8.268) | (4.265) | (4.331) | (8.148) |
| Academic year Fixed-Effect | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| School Fixed-Effect | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Child’s characteristics | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Household’s characteristic | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Observations | 142675 | 121711 | 51908 | 143001 | 121810 | 51718 | 141654 | 121378 | 51831 |
| Adjusted R2R^{2} | 0.262 | 0.235 | 0.202 | 0.230 | 0.301 | 0.200 | 0.361 | 0.378 | 0.343 |
| Standard errors in parentheses | | | | | | | | | |
| ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01 | | | | | | | | | |

Table 13: Parental investment and child effort (continued)




Table 14: Impact of parent’s highest level of education (predicted values by first stage IV regression) according to grade level - Grade 3 vs Grade 6

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Mathematics | | | Literature | | | English | | |
|  | (1) | (2) | (3) | (1) | (2) | (3) | (1) | (2) | (3) |
|  | Math. | Math. | Math. | Lit. | Lit. | Lit. | Engl. | Engl. | Engl. |
| Parent’s highest education | | | | | | | | | |
|  | 67.52∗⁣∗∗67.52^{\*\*\*} | 65.63∗⁣∗∗65.63^{\*\*\*} | 46.97∗⁣∗∗46.97^{\*\*\*} | 63.02∗⁣∗∗63.02^{\*\*\*} | 65.58∗⁣∗∗65.58^{\*\*\*} | 59.24∗⁣∗∗59.24^{\*\*\*} | 57.75∗⁣∗∗57.75^{\*\*\*} | 58.80∗⁣∗∗58.80^{\*\*\*} | 69.05∗⁣∗∗69.05^{\*\*\*} |
|  | (1.062)(1.062) | (1.058)(1.058) | (11.74)(11.74) | (1.171)(1.171) | (1.151)(1.151) | (12.82)(12.82) | (0.985)(0.985) | (0.976)(0.976) | (10.85)(10.85) |
| Grade 3 vs Grade 6 | | | | | | | | | |
| I(3,6) | 9.682∗⁣∗∗9.682^{\*\*\*} | 8.517∗⁣∗∗8.517^{\*\*\*} | −8.106∗⁣∗∗-8.106^{\*\*\*} | −36.42∗⁣∗∗-36.42^{\*\*\*} | −36.62∗⁣∗∗-36.62^{\*\*\*} | −53.68∗⁣∗∗-53.68^{\*\*\*} | −15.35∗⁣∗∗-15.35^{\*\*\*} | −16.14∗⁣∗∗-16.14^{\*\*\*} | −28.49∗⁣∗∗-28.49^{\*\*\*} |
|  | (2.262)(2.262) | (2.251)(2.251) | (2.239)(2.239) | (2.494)(2.494) | (2.449)(2.449) | (2.442)(2.442) | (2.097)(2.097) | (2.076)(2.076) | (2.070)(2.070) |
| Interactions | | | | | | | | | |
|  | −1.522-1.522 | 0.2720.272 | 2.828∗2.828^{\*} | 10.11∗⁣∗∗10.11^{\*\*\*} | 10.97∗⁣∗∗10.97^{\*\*\*} | 14.26∗⁣∗∗14.26^{\*\*\*} | 11.00∗⁣∗∗11.00^{\*\*\*} | 12.24∗⁣∗∗12.24^{\*\*\*} | 13.88∗⁣∗∗13.88^{\*\*\*} |
|  | (1.477)(1.477) | (1.470)(1.470) | (1.457)(1.457) | (1.628)(1.628) | (1.600)(1.600) | (1.588)(1.588) | (1.369)(1.369) | (1.356)(1.356) | (1.346)(1.346) |
| Constant | | | | | | | | | |
|  | 409.4∗⁣∗∗409.4^{\*\*\*} | 425.6∗⁣∗∗425.6^{\*\*\*} | 466.5∗⁣∗∗466.5^{\*\*\*} | 429.1∗⁣∗∗429.1^{\*\*\*} | 457.3∗⁣∗∗457.3^{\*\*\*} | 484.7∗⁣∗∗484.7^{\*\*\*} | 427.6∗⁣∗∗427.6^{\*\*\*} | 451.4∗⁣∗∗451.4^{\*\*\*} | 453.3∗⁣∗∗453.3^{\*\*\*} |
|  | (1.662)(1.662) | (2.075)(2.075) | (8.471)(8.471) | (1.834)(1.834) | (2.259)(2.259) | (9.246)(9.246) | (1.542)(1.542) | (1.916)(1.916) | (7.824)(7.824) |
| Academic year Fixed-Effect | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| School Fixed-Effect | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Child’s characteristics | No | Yes | Yes | No | Yes | Yes | No | Yes | Yes |
| Household’s characteristics | No | No | Yes | No | No | Yes | No | No | Yes |
| Observations | 248466 | 248466 | 248466 | 248816 | 248816 | 248816 | 247207 | 247207 | 247207 |
| Adjusted R2R^{2} | 0.171 | 0.180 | 0.215 | 0.146 | 0.177 | 0.209 | 0.278 | 0.293 | 0.321 |
| Standard errors in parentheses | | | | | | | | | |
| ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01 | | | | | | | | | |
| I(u,v) is a dummy variable which takes the value 0 if g=u (reference grade), and 1 if g=v | | | | | | | | | |




Table 15: Impact of parent’s highest level of education (predicted values by first stage IV regression) according to grade level - Grade 6 vs Grade 10

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Mathematics | | | Literature | | | English | | |
|  | (4) | (5) | (6) | (4) | (5) | (6) | (4) | (5) | (6) |
|  | Math. | Math. | Math. | Lit. | Lit. | Lit. | Engl. | Engl. | Engl. |
| Parent’s highest education | | | | | | | | | |
|  | 66.80∗⁣∗∗66.80^{\*\*\*} | 66.13∗⁣∗∗66.13^{\*\*\*} | 34.14∗∗34.14^{\*\*} | 70.74∗⁣∗∗70.74^{\*\*\*} | 73.56∗⁣∗∗73.56^{\*\*\*} | 40.30∗⁣∗∗40.30^{\*\*\*} | 65.08∗⁣∗∗65.08^{\*\*\*} | 66.82∗⁣∗∗66.82^{\*\*\*} | 76.60∗⁣∗∗76.60^{\*\*\*} |
|  | (1.212)(1.212) | (1.206)(1.206) | (13.74)(13.74) | (1.305)(1.305) | (1.284)(1.284) | (14.66)(14.66) | (1.078)(1.078) | (1.069)(1.069) | (12.14)(12.14) |
| Grade 6 vs Grade 10 | | | | | | | | | |
| I(6,10) | 22.26∗⁣∗∗22.26^{\*\*\*} | 25.73∗⁣∗∗25.73^{\*\*\*} | 1.6931.693 | 35.62∗⁣∗∗35.62^{\*\*\*} | 37.89∗⁣∗∗37.89^{\*\*\*} | 16.24∗⁣∗∗16.24^{\*\*\*} | −10.08∗⁣∗∗-10.08^{\*\*\*} | −8.706∗⁣∗∗-8.706^{\*\*\*} | −29.77∗⁣∗∗-29.77^{\*\*\*} |
|  | (3.380)(3.380) | (3.370)(3.370) | (3.384)(3.384) | (3.649)(3.649) | (3.598)(3.598) | (3.617)(3.617) | (3.005)(3.005) | (2.986)(2.986) | (2.993)(2.993) |
| Interactions | | | | | | | | | |
|  | −18.06∗⁣∗∗-18.06^{\*\*\*} | −19.85∗⁣∗∗-19.85^{\*\*\*} | −14.54∗⁣∗∗-14.54^{\*\*\*} | −18.64∗⁣∗∗-18.64^{\*\*\*} | −19.89∗⁣∗∗-19.89^{\*\*\*} | −15.37∗⁣∗∗-15.37^{\*\*\*} | 10.71∗⁣∗∗10.71^{\*\*\*} | 9.912∗⁣∗∗9.912^{\*\*\*} | 15.44∗⁣∗∗15.44^{\*\*\*} |
|  | (2.107)(2.107) | (2.101)(2.101) | (2.099)(2.099) | (2.274)(2.274) | (2.243)(2.243) | (2.243)(2.243) | (1.872)(1.872) | (1.861)(1.861) | (1.856)(1.856) |
| Constant | | | | | | | | | |
|  | 411.4∗⁣∗∗411.4^{\*\*\*} | 407.8∗⁣∗∗407.8^{\*\*\*} | 447.5∗⁣∗∗447.5^{\*\*\*} | 333.5∗⁣∗∗333.5^{\*\*\*} | 344.3∗⁣∗∗344.3^{\*\*\*} | 375.1∗⁣∗∗375.1^{\*\*\*} | 417.8∗⁣∗∗417.8^{\*\*\*} | 426.0∗⁣∗∗426.0^{\*\*\*} | 422.8∗⁣∗∗422.8^{\*\*\*} |
|  | (1.905)(1.905) | (2.606)(2.606) | (9.320)(9.320) | (2.051)(2.051) | (2.780)(2.780) | (9.948)(9.948) | (1.694)(1.694) | (2.309)(2.309) | (8.241)(8.241) |
| Academic year Fixed-Effect | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| School Fixed-Effect | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Child’s characteristics | No | Yes | Yes | No | Yes | Yes | No | Yes | Yes |
| Household’s characteristics | No | No | Yes | No | No | Yes | No | No | Yes |
| Observations | 166358 | 166358 | 166358 | 166220 | 166220 | 166220 | 165923 | 165923 | 165923 |
| Adjusted R2R^{2} | 0.149 | 0.159 | 0.197 | 0.197 | 0.223 | 0.257 | 0.291 | 0.304 | 0.338 |
| Standard errors in parentheses | | | | | | | | | |
| ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01 | | | | | | | | | |
| I(u,v) is a dummy variable which takes the value 0 if g=u (reference grade), and 1 if g=v | | | | | | | | | |




Table 16: Impact of parent’s highest level of education (predicted values by first stage IV regression) according to grade level - Grade 3 vs Grade 10

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Mathematics | | | Literature | | | English | | |
|  | (7) | (8) | (9) | (7) | (8) | (9) | (7) | (8) | (9) |
|  | Math. | Math. | Math. | Lit. | Lit. | Lit. | Engl. | Engl. | Engl. |
| Parent’s highest education | | | | | | | | | |
|  | 65.68∗⁣∗∗65.68^{\*\*\*} | 63.94∗⁣∗∗63.94^{\*\*\*} | 36.96∗⁣∗∗36.96^{\*\*\*} | 63.71∗⁣∗∗63.71^{\*\*\*} | 65.60∗⁣∗∗65.60^{\*\*\*} | 48.73∗⁣∗∗48.73^{\*\*\*} | 57.45∗⁣∗∗57.45^{\*\*\*} | 58.61∗⁣∗∗58.61^{\*\*\*} | 50.93∗⁣∗∗50.93^{\*\*\*} |
|  | (1.101)(1.101) | (1.097)(1.097) | (12.70)(12.70) | (1.076)(1.076) | (1.064)(1.064) | (12.33)(12.33) | (1.022)(1.022) | (1.016)(1.016) | (11.72)(11.72) |
| Grade 3 vs Grade 10 | | | | | | | | | |
| I(3,10) | 19.91∗⁣∗∗19.91^{\*\*\*} | 20.19∗⁣∗∗20.19^{\*\*\*} | −16.85∗⁣∗∗-16.85^{\*\*\*} | 18.21∗⁣∗∗18.21^{\*\*\*} | 17.95∗⁣∗∗17.95^{\*\*\*} | −11.83∗⁣∗∗-11.83^{\*\*\*} | −34.30∗⁣∗∗-34.30^{\*\*\*} | −35.37∗⁣∗∗-35.37^{\*\*\*} | −67.77∗⁣∗∗-67.77^{\*\*\*} |
|  | (3.243)(3.243) | (3.233)(3.233) | (3.397)(3.397) | (3.178)(3.178) | (3.145)(3.145) | (3.304)(3.304) | (3.005)(3.005) | (2.991)(2.991) | (3.136)(3.136) |
| Interactions | | | | | | | | | |
|  | −14.48∗⁣∗∗-14.48^{\*\*\*} | −12.74∗⁣∗∗-12.74^{\*\*\*} | −4.696∗∗-4.696^{\*\*} | −9.742∗⁣∗∗-9.742^{\*\*\*} | −8.109∗⁣∗∗-8.109^{\*\*\*} | −2.643-2.643 | 23.12∗⁣∗∗23.12^{\*\*\*} | 24.98∗⁣∗∗24.98^{\*\*\*} | 32.48∗⁣∗∗32.48^{\*\*\*} |
|  | (2.026)(2.026) | (2.023)(2.023) | (2.094)(2.094) | (1.986)(1.986) | (1.968)(1.968) | (2.036)(2.036) | (1.878)(1.878) | (1.872)(1.872) | (1.933)(1.933) |
| Constant | | | | | | | | | |
|  | 413.9∗⁣∗∗413.9^{\*\*\*} | 425.9∗⁣∗∗425.9^{\*\*\*} | 467.7∗⁣∗∗467.7^{\*\*\*} | 418.3∗⁣∗∗418.3^{\*\*\*} | 441.9∗⁣∗∗441.9^{\*\*\*} | 469.1∗⁣∗∗469.1^{\*\*\*} | 429.7∗⁣∗∗429.7^{\*\*\*} | 449.4∗⁣∗∗449.4^{\*\*\*} | 466.6∗⁣∗∗466.6^{\*\*\*} |
|  | (1.719)(1.719) | (2.170)(2.170) | (8.311)(8.311) | (1.679)(1.679) | (2.108)(2.108) | (8.067)(8.067) | (1.595)(1.595) | (2.012)(2.012) | (7.670)(7.670) |
| Academic year Fixed-Effect | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| School Fixed-Effect | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Child’s characteristics | No | Yes | Yes | No | Yes | Yes | No | Yes | Yes |
| Household’s characteristics | No | No | Yes | No | No | Yes | No | No | Yes |
| Observations | 186008 | 186008 | 186008 | 186130 | 186130 | 186130 | 185028 | 185028 | 185028 |
| Adjusted R2R^{2} | 0.183 | 0.193 | 0.218 | 0.149 | 0.171 | 0.197 | 0.284 | 0.294 | 0.320 |
| Standard errors in parentheses | | | | | | | | | |
| ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01 | | | | | | | | | |
| I(u,v) is a dummy variable which takes the value 0 if g=u (reference grade), and 1 if g=v | | | | | | | | | |