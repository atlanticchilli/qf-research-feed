---
authors:
- Minh Chau Nguyen
- Tony S. Wirjanto
- Fan Yang
doc_id: arxiv:2512.18790v1
family_id: arxiv:2512.18790
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for
  their comments and suggestions on an earlier version of the paper. We also thank
  participants at the following conferences: Climate Change and Insurance Conference
  2025, International Centre for Mathematical Science (Edinburgh, U.K., September
  10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical
  Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research
  Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025);
  2025 ICSA China Conference, International Chinese Statistical Association, Beijing
  Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual
  Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th,
  2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight
  (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer
  Educational Foundation, and Department of Statistics and Actuarial Science at the
  University of Waterloo. The usual disclaimer applies.'
url_abs: http://arxiv.org/abs/2512.18790v1
url_html: https://arxiv.org/html/2512.18790v1
venue: arXiv q-fin
version: 1
year: 2025
---


Minh Chau Nguyen 111Corresponding author. E-mail: mcnguyen@uwaterloo.ca   Tony Wirjanto 222E-mail: twirjanto@uwaterloo.ca    Fan Yang 333E-mail: fan.yang@uwaterloo.ca
  
 Department of Statistics and Actuarial Science, University of
Waterloo
  
Waterloo, ON N2L 3G1, Canada

(December 19, 2025)

###### Abstract

Catastrophe risk has long been recognized to pose a serious threat to the
insurance sector. Although natural disasters such as flooding, hurricane or
severe drought are rare events, they generally lead to devastating damages
that traditional insurance schemes may not be able to efficiently cover.
Catastrophe risk pooling is an effective way to diversify the losses from such
risks. In this paper, we improve the catastrophe risk pool by Pareto-optimally
allocating the diversification benefits among participants. Finding the
practical Pareto-optimal pool entails solving a high-dimensional optimization
problem, for which analytical solutions are typically unavailable and
numerical methods can be computationally intensive and potentially unreliable.
We propose evaluating the diversification
benefits at the limit case and using it to approximate the optimal
pool by deriving an asymptotic optimal pool. Simulation studies are undertaken to explore the implications of the results and an empirical analysis from the U.S. National Flood Insurance Program is also carried
out to illustrate how this framework can be applied in practice.

Key words: catastrophe risk, extreme events, optimal pooling, heavy tail, Pareto optimality.

## 1 Introduction

Climate change has increased the severity and frequency of natural disasters.
Since 2015, losses from natural disasters worldwide have been steadily
increasing, more than 50% of which are uninsured (see Figure
[1](https://arxiv.org/html/2512.18790v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")). A catastrophe risk pool is a promising mechanism for
managing extreme losses, as it helps diversify participants’ catastrophic risk
and strengthen their resilience against natural disasters. Real-world
examples of such risk pools include the Florida Hurricane Catastrophe Fund,
the Caribbean Catastrophe Risk Insurance Facility (CCRIF), and the African Risk
Capacity (for further details of these examples, see bollmann2019international for instance). In
this paper, we aim at improving the efficiency of catastrophe risk pools by
optimally allocating the diversification benefits among participants.

![Refer to caption](Uninsured.png)


Figure 1: Global catastrophe losses from 2015 to 2024 (USD billion, 2024 prices) (Source: swiss\_re\_sigma\_2025)

It has been shown that economic losses from natural disasters exhibit
power-law tail behavior when the underlying hazard intensities
follow a power-law distribution. A power-law tail means that the survival
function of a loss variable XX satisfies

|  |  |  |
| --- | --- | --- |
|  | Pr⁡(X>x)∼c​x−α,x>0,\Pr\left(X>x\right)\sim cx^{-\alpha},\qquad x>0, |  |

for some tail index α>0\alpha>0. Such distributions are also referred to as
heavy-tailed. Empirical evidence supports this behavior for various types of
catastrophes, including earthquakes (sornette1996rank), hurricanes
(hogg1983estimation; hsieh1999robustness), wildfires
(malamud2005characterizing), and river floods
(woo2011calculating). Furthermore, since the goal of participants in a
catastrophe risk pool is to diversify their risks, and independence among
losses enhances the potential for diversification (see e.g., Theorem 2.3 of embrechts2009additivity), we assume that all losses
in the pool are independent. This can be achieved by pooling losses from
different geographic areas or from different perils. As such, in this paper we
assume that the catastrophic losses follow heavy-tailed distributions, which
do not need to be identical, and that they are independent.

We consider a pooling structure where the pool provides each participant with coverage for a
specific layer of their loss, and the participant pays a premium for this coverage
that is proportional to the aggregated loss of the pool. A formal definition of this pooling structure is provided in
Section [2.1](https://arxiv.org/html/2512.18790v1#S2.SS1 "2.1 Pool setup ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."). The diversification
benefit is measured using a so-called diversification ratio (DR), based on the Value-at-Risk (VaR) measure, which compares the participant’s risk before and
after joining the pool.

Since the catastrophic losses are not necessarily identically distributed, in our set up, the
diversification benefit that each participant obtains from the pool depends on
the layer of their loss covered by the pool. It is generally
not feasible for every participant to simultaneously achieve their maximum diversification
benefit from the pool. Often, one’s diversification benefit is increased at
the cost of other’s benefit. Hence, to promote a fair allocation of
diversification benefits in the pool, we propose allocating the
diversification benefit among the participants in a Pareto optimal way. According to this optimality criterion, no individual can improve their diversification benefit
without reducing the benefit of someone else. In practice, DR is measured at
any specific level pp of the VaR measure. However, solving the Pareto-optimal
allocation of diversification benefit for such a practical pool is a
high-dimensional optimization problem. The analytical solution is generally
unavailable, while numerical solutions can be time-consuming and potentially
unreliable. In this paper, we propose using the asymptotic optimal pool, which is a
Pareto-optimal pool where the DR is evaluated at the limit as p→1p\rightarrow 1,
to approximate the practical optimal pool at any finite level pp close to 1.
To be more specific, we consider two types of risk pools. In the first model,
all losses are assumed to be tail equivalent, i.e., they share the same
tail index, although they may not be identically distributed. In the second
model, we allow the losses to have different tail indices, in which case more
substantial heterogeneity arises among participants. For each model, we derive
asymptotic expressions of the DR as the level pp of the VaR measure
approaches 1. These expressions characterize the diversification benefit that
each participant obtains in the asymptotic pool. Based on these results, we
construct the asymptotic optimal pool by selecting the optimal loss layer for
each participant. We find that not only we achieve Pareto optimality in this pool, but more importantly, each participant obtains the maximum
possible diversification benefit.

Through a set of simulation studies, we show that the asymptotic optimal pool
provides a reasonably accurate and reliable approximation to the practical optimal pool.
The practical optimal pools at specific levels pp of VaR are obtained
using a global optimization algorithm. In Appendix [B](https://arxiv.org/html/2512.18790v1#A2 "Appendix B Comparison of algorithms for simulation study ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."), we
show that the chosen algorithm, in comparison with four other optimization algorithms,
provides accurate solutions while also being efficient at the same time. In the empirical
study, we construct three Pareto-optimal flood risk pools using the asymptotic optimal pooling strategy and flood loss
data from the U.S. National Flood Insurance Program (NFIP). As part of the presentation of our method, we discuss practical issues related to the
implementation of our framework and show that the resulting pools are consistent with our
theoretical findings.

The remainder of this paper is structured as follows. In Section [2](https://arxiv.org/html/2512.18790v1#S2 "2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."),
we first provide the formal setup of the catastrophe risk pool. Then we derive
the asymptotic expressions for the DR when the level pp of VaR
approaches 1. This is done for two types of risk pools, one having tail
equivalent losses and the other having general heavy-tailed losses. Based on
these expressions, we derive the asymptotic optimal pool. In Section
[3](https://arxiv.org/html/2512.18790v1#S3 "3 Simulation study ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."), we examine the performance of the asymptotic optimal pool
through a set of simulations. Lastly, in Section [4](https://arxiv.org/html/2512.18790v1#S4 "4 Empirical analysis ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."), we carry out an
empirical analysis to illustrate how this framework can be implemented in
practice. The appendices contain detailed proofs of the main results, a comparison
of algorithms used in the simulation study, and an additional exploratory analysis of the
flood loss data.

## 2 Optimal pooling structure

### 2.1 Pool setup

Suppose that there are nn participants in the pool and each has a ground-up
catastrophe loss XiX\_{i}, i=1,…,ni=1,...,n. Let the losses X1,X2,…,XnX\_{1},X\_{2},...,X\_{n}
be independent with distribution functions F1,…,FnF\_{1},...,F\_{n}. This condition is not overly restrictive, since it is possible to find such losses by selecting different types of perils or locations spaced far apart. As discussed in the introduction, these losses are assumed to follow heavy-tailed distributions. More
specifically, a loss XX with a distribution function F=1−F¯F=1-\overline{F} is
said to have a regularly varying tail with index α>0\alpha>0, denoted by
X∈RV−αX\in\mathrm{RV}\_{-\alpha} or F¯∈RV−α\overline{F}\in\mathrm{RV}\_{-\alpha}, if

|  |  |  |
| --- | --- | --- |
|  | limt→∞F¯​(t​x)F¯​(t)=x−α,x>0.\lim\_{t\rightarrow\infty}\frac{\overline{F}(tx)}{\overline{F}(t)}=x^{-\alpha},\qquad x>0. |  |

The tail index α\alpha represents the heaviness of the tail of the distribution, where the
smaller the value of α\alpha is, the heavier the tail is. See, for example,
haan2006extreme for more details on regularly varying (RV) functions.

By joining the pool, each participant is covered for a layer of XiX\_{i} with
an attachment point did\_{i} and a limit lil\_{i}, defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yi={0,Xi<di,Xi−di,di≤Xi<li,li−di,li≤Xi.Y\_{i}=\left\{\begin{array}[c]{lll}0,&&X\_{i}<d\_{i},\\ X\_{i}-d\_{i},&&d\_{i}\leq X\_{i}<l\_{i},\\ l\_{i}-d\_{i},&&l\_{i}\leq X\_{i}.\end{array}\right. |  | (2.1) |

This form of coverage is a common practice in many lines of property and casualty insurance, which is often applied in the contribution structure of existing climate
risk pools such as CCRIF (bollmann2019international).

The aggregated loss in this pool is then given by Sn=∑i=1nYiS\_{n}=\sum\_{i=1}^{n}Y\_{i}.
To receive the coverage from the pool, each participant pays a premium PiP\_{i}
defined as

|  |  |  |
| --- | --- | --- |
|  | Pi=E​[Yi]E​[Sn]​VaRp​(Sn),P\_{i}=\frac{E\left[Y\_{i}\right]}{E\left[S\_{n}\right]}\mathrm{VaR}\_{p}(S\_{n}), |  |

where VaRp​(Z)=G←​(p)=inf{z:G​(z)>p}\mathrm{VaR}\_{p}(Z)=G^{\leftarrow}(p)=\inf\{z:G(z)>p\} is the Value-at-Risk (VaR) or the general inverse function for a random variable ZZ with a distribution function GG at a level p∈(0,1)p\in(0,1). This premium can be interpreted as the participants sharing the aggregated risk through a mean-proportional risk-sharing rule (see denuit2022risk for instance). In particular, each participant shares a portion of E​[Yi]E​[Sn]\frac{E\left[Y\_{i}\right]}{E\left[S\_{n}\right]} of the total risk of the pool. Furthermore, this premium can be rewritten as

|  |  |  |
| --- | --- | --- |
|  | Pi=E​[Yi]​(1+η),P\_{i}=E[Y\_{i}]\left(1+\eta\right), |  |

where η=VaRp​(Sn)E​[Sn]−1\eta=\frac{\mathrm{VaR}\_{p}(S\_{n})}{E[S\_{n}]}-1. When the level pp of VaR is close to 1, we have η>0\eta>0. Thus, the premium PiP\_{i}
follows the expected value principle, and the loading η\eta represents the
exceedance of the tail aggregated risk over the expected aggregated risk.

With the layer loss YiY\_{i} covered by the pool, the retained risk by
participant ii is given by VaRp​(Xi−Yi)\mathrm{VaR}\_{p}(X\_{i}-Y\_{i}). Then we quantify the
diversification benefit that participant ii obtains when joining the pool by using the
diversification ratio (DR) defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | DRi​(p)=VaRp​(Xi−Yi)+E​[Yi]E​[Sn]​VaRp​(Sn)VaRp​(Xi).\mathrm{DR}\_{i}(p)=\frac{\mathrm{VaR}\_{p}(X\_{i}-Y\_{i})+\frac{E\left[Y\_{i}\right]}{E\left[S\_{n}\right]}\mathrm{VaR}\_{p}(S\_{n})}{\mathrm{VaR}\_{p}(X\_{i})}. |  | (2.2) |

DR compares the risk of a participant before and after joining the
pool. A DR value less than 1 indicates that the participant obtains a positive diversification benefit from joining the pool, and a smaller DR value means a
greater risk reduction for the participant. Note that the total risk a
participant holds after joining the pool, including both the retained risk and
the portion of risk shared from the pool, is used for the definition ([2.2](https://arxiv.org/html/2512.18790v1#S2.E2 "In 2.1 Pool setup ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")).
This is different from the diversification ratio in cui2021diversification or
cui2022asymptotic, where only the risk shared from the pool is
considered as the participant’s post-pooling risk. By including the total risk that a participant holds after joining the pool, our newly proposed DR measure ([2.2](https://arxiv.org/html/2512.18790v1#S2.E2 "In 2.1 Pool setup ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) reflects the real situation faced by a pool participant and thus better captures the diversification effect of joining the pool.

The goal of this paper is to construct the pool by choosing the attachment
points did\_{i}’s and the limits lil\_{i}’s such that all pool participants can enjoy the
diversification benefit in an optimal way. As mentioned above, it is generally not feasible for all
participants in the pool to achieve their individual maximum diversification benefit at
any level of pp, i.e.,

|  |  |  |
| --- | --- | --- |
|  | mindi,li,i=1,…,n⁡DRi​(p)​,  for all ​i=1,…,n​.\min\_{d\_{i},l\_{i},i=1,...,n}\mathrm{DR}\_{i}(p)\text{,\qquad for all }i=1,...,n\text{.} |  |

Instead, Pareto optimality is often sought. It is a way to allocate the diversification benefits
among the participants so that no individual can improve their diversification
benefit without reducing the benefit of someone else. Within this paper, such optimal allocation is defined by solving the optimization program

|  |  |  |  |
| --- | --- | --- | --- |
|  | mindi,li,i=1,…,n​∑i=1nDRi​(p).\min\_{d\_{i},l\_{i},i=1,...,n}\sum\_{i=1}^{n}\mathrm{DR}\_{i}(p). |  | (2.3) |

However, an analytical solution to
([2.3](https://arxiv.org/html/2512.18790v1#S2.E3 "In 2.1 Pool setup ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) is generally not available. Considering that the pool is used to manage
the extreme risks for participants, we focus on the case where the confidence
level pp is close to 1. Denote the limit diversification benefit that
participant ii has when p→1p\rightarrow 1 as

|  |  |  |
| --- | --- | --- |
|  | DRi​(1):=limp→1DRi​(p).\mathrm{DR}\_{i}(1):=\lim\_{p\rightarrow 1}\mathrm{DR}\_{i}(p). |  |

In the following subsections, we set the attachment points in such a way that each participant asymptotically has the same tail
probability at these points. Then we look for the optimal solution of the problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | minli,i=1,…,n​∑i=1nDRi​(1),\min\_{l\_{i},i=1,...,n}\sum\_{i=1}^{n}\mathrm{DR}\_{i}(1), |  | (2.4) |

for given did\_{i}’s. This means that, at certain attachment points did\_{i}’s, we solve for the
optimal limits lil\_{i}’s which allow pool participants to achieve Pareto optimality.
Through a set of simulations, we demonstrate that this solution can be used to
approximate the optimal solution to the practical optimal problem ([2.3](https://arxiv.org/html/2512.18790v1#S2.E3 "In 2.1 Pool setup ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."))
when pp is close to 1. Moreover, we find that the optimal solution to
([2.4](https://arxiv.org/html/2512.18790v1#S2.E4 "In 2.1 Pool setup ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) also solves the global optimization problem

|  |  |  |
| --- | --- | --- |
|  | minli,i=1,…,n⁡DRi​(1)​,  for all ​i=1,…,n\min\_{l\_{i},i=1,...,n}\mathrm{DR}\_{i}(1)\text{,\qquad for all }i=1,...,n |  |

for given did\_{i}’s. This means that, at the limit, not only the participants are able to achieve Pareto
optimality in the pool, but each participant in the pool can also attain their individual
maximum diversification benefit.

### 2.2 Pool with tail equivalent losses

In this subsection, we first consider a pool of losses which have the same heavy-tailedness but are not necessarily identically distributed, as detailed in the following model. By assuming a common tail index for all losses, we provide a simplified version of the general model, which helps illustrate the structure of the pool and the implications of the results. We extend the study to a pool of losses with general heavy-tailedness in the next subsection.

Model 1

* •

  F¯i∈RV−α\overline{F}\_{i}\in\mathrm{RV}\_{-\alpha} with α>0\alpha>0, for
  i=1,…,ni=1,...,n, i.e., any two losses are tail equivalent. Furthermore, for
  i=1,…,ni=1,...,n, there exists θi>0\theta\_{i}>0 such that

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | limt→∞F¯i​(t)F¯1​(t)=θi>0.\lim\_{t\rightarrow\infty}\frac{\overline{F}\_{i}(t)}{\overline{F}\_{1}(t)}=\theta\_{i}>0. |  | (2.5) |
* •

  The attachment point and limit are functions of pp, meaning that di=di​(p)d\_{i}=d\_{i}(p)
  and li=li​(p)l\_{i}=l\_{i}(p), i=1,…,ni=1,...,n, which satisfy, for some ξ>0\xi>0, that

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | limp→1di​(p)VaRp​(Xi)=ξ,\lim\_{p\rightarrow 1}\frac{d\_{i}(p)}{\mathrm{VaR}\_{p}(X\_{i})}=\xi, |  | (2.6) |

  and for some λi>1\lambda\_{i}>1,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | limp→1li​(p)di​(p)=λi>1.\lim\_{p\rightarrow 1}\frac{l\_{i}(p)}{d\_{i}(p)}=\lambda\_{i}>1. |  | (2.7) |

In Model 1, all losses are heavy-tailed with the same tail index α\alpha. We further assume that the losses may have different scales,
captured by θi\theta\_{i}, compared to the first loss distribution
F¯1​(t)\overline{F}\_{1}(t). A larger scale θi\theta\_{i} means a higher tail
probability of XiX\_{i} at the level tt compared to that of X1X\_{1}. Under
the assumptions ([2.6](https://arxiv.org/html/2512.18790v1#S2.E6 "In 2nd item ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) and ([2.7](https://arxiv.org/html/2512.18790v1#S2.E7 "In 2nd item ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")), both di​(p)d\_{i}(p) and li​(p)l\_{i}(p)
diverge to infinity as the confidence level pp approaches 1. For each loss
XiX\_{i}, its attachment point di​(p)d\_{i}(p) is approximately ξ\xi times its
benchmark risk VaRp​(Xi)\mathrm{VaR}\_{p}(X\_{i}). This multiplier is set to be the same for
all losses. The limit li​(p)l\_{i}(p) is λi\lambda\_{i} times di​(p)d\_{i}(p).
The multipliers λi\lambda\_{i}’s are allowed to be different for each loss and will be optimally chosen for fixed levels of ξ\xi to achieve a Pareto optimal pool in Subsection [2.4](https://arxiv.org/html/2512.18790v1#S2.SS4 "2.4 Asymptotic optimal pool ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.").

Next, we obtain several relations that are helpful for further illustrating Model 1
and useful for establishing the proof of the main theorem in this subsection.

###### Lemma 2.1

Under Model 1, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | limp→1di​(p)d1​(p)=θi1/α,limp→1F¯i​(di)F¯1​(d1)=1,\lim\_{p\rightarrow 1}\frac{d\_{i}(p)}{d\_{1}(p)}=\theta\_{i}^{1/\alpha},\qquad\lim\_{p\rightarrow 1}\frac{\overline{F}\_{i}(d\_{i})}{\overline{F}\_{1}(d\_{1})}=1, |  | (2.8) |

and

|  |  |  |
| --- | --- | --- |
|  | limp→1di​(p)VaRp​(X1)=θi1/α​ξ,limp→1li​(p)VaRp​(X1)=λi​θi1/α​ξ.\lim\_{p\rightarrow 1}\frac{d\_{i}(p)}{\mathrm{VaR}\_{p}(X\_{1})}=\theta\_{i}^{1/\alpha}\xi,\qquad\lim\_{p\rightarrow 1}\frac{l\_{i}(p)}{\mathrm{VaR}\_{p}(X\_{1})}=\lambda\_{i}\theta\_{i}^{1/\alpha}\xi. |  |

From Lemma [2.1](https://arxiv.org/html/2512.18790v1#S2.Thmlemma1 "Lemma 2.1 ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."), we observe several additional implications of Model 1.
Firstly, when the level pp is close to 1, the attachment point
did\_{i} for loss XiX\_{i} is approximately θi1/α\theta\_{i}^{1/\alpha} times
d1d\_{1} for X1X\_{1}. Thus, for a loss XiX\_{i} with a larger scale θi\theta\_{i},
its attachment point did\_{i} are set at higher levels than those with
smaller scales. Secondly, the attachment points are set in such a way that the tail
probability of each loss at its attachment point is approximately the same.
Following the similar proof of Lemma [2.1](https://arxiv.org/html/2512.18790v1#S2.Thmlemma1 "Lemma 2.1 ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."), we can show that

|  |  |  |
| --- | --- | --- |
|  | limp→1F¯i​(li)F¯1​(l1)=(λ1λi)α.\lim\_{p\rightarrow 1}\frac{\overline{F}\_{i}(l\_{i})}{\overline{F}\_{1}(l\_{1})}=\left(\frac{\lambda\_{1}}{\lambda\_{i}}\right)^{\alpha}. |  |

This means that the tail probability of loss XiX\_{i} at its limit lil\_{i} is (λ1/λi)α\left(\lambda\_{1}/\lambda\_{i}\right)^{\alpha} times that of X1X\_{1}, which
depends on λ1\lambda\_{1} and λi\lambda\_{i}. Thirdly, for loss XiX\_{i}, its
attachment point di​(p)d\_{i}(p) is approximately θi1/α​ξ\theta\_{i}^{1/\alpha}\xi times
the benchmark risk VaRp​(X1)\mathrm{VaR}\_{p}(X\_{1}) of X1X\_{1}. It further
illustrates that risks with larger scales have higher attachment points.

Now we are ready to derive the asymptotic expression of DRi​(p)\mathrm{DR}\_{i}(p)
as p→1p\rightarrow 1.

###### Theorem 2.1

Under Model 1, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | DRi​(1)={1+δi​Δξ,𝝀,ξ≥1,ξ+δi​Δξ,𝝀,1/λi≤ξ<1,1−(λi−1)​ξ+δi​Δξ,𝝀,ξ<1/λi,\mathrm{DR}\_{i}(1)=\left\{\begin{array}[c]{lll}1+\delta\_{i}\Delta\_{\xi,\boldsymbol{\lambda}},&&\xi\geq 1,\\ \xi+\delta\_{i}\Delta\_{\xi,\boldsymbol{\lambda}},&&1/\lambda\_{i}\leq\xi<1,\\ 1-(\lambda\_{i}-1)\xi+\delta\_{i}\Delta\_{\xi,\boldsymbol{\lambda}},&&\xi<1/\lambda\_{i},\end{array}\right. |  | (2.9) |

where

|  |  |  |
| --- | --- | --- |
|  | δi=(λi1−α−1)∑j=1n(λj1−α−1)​θj1/α,Δξ,𝝀=(∑j∈Z(θj−1/α+ξ)−α)1/α\delta\_{i}=\frac{\left(\lambda\_{i}^{1-\alpha}-1\right)}{\sum\_{j=1}^{n}\left(\lambda\_{j}^{1-\alpha}-1\right)\theta\_{j}^{1/\alpha}},\qquad\Delta\_{\xi,\boldsymbol{\lambda}}=\left(\sum\_{j\in Z}\left(\theta\_{j}^{-1/\alpha}+\xi\right)^{-\alpha}\right)^{1/\alpha} |  |

with Z={j=1,2,…,n:ξ>θj−1/α​(λj−1)−1}Z=\left\{j=1,2,...,n:\xi>\theta\_{j}^{-1/\alpha}\left(\lambda\_{j}-1\right)^{-1}\right\}.

A smaller DRi​(1)\mathrm{DR}\_{i}(1) is preferred for pool participant ii
because it means that more risk is diversified by joining the pool. From Theorem
[2.1](https://arxiv.org/html/2512.18790v1#S2.Thmtheorem1 "Theorem 2.1 ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."), since δi>0\delta\_{i}>0 for any λi>1\lambda\_{i}>1 and Δξ,𝝀≥0\Delta\_{\xi,\boldsymbol{\lambda}}\geq 0, we see that if
ξ≥1\xi\geq 1, then DRi​(1)≥1\mathrm{DR}\_{i}(1)\geq 1. In other words, if the deductible
did\_{i} is set at a higher level than VaRp​(Xi)\mathrm{VaR}\_{p}(X\_{i}), too much risk
is retained, and pool participant ii would fail to gain any risk diversification by joining
the pool. Since this is not an ideal situation, we focus on the case where ξ<1\xi<1 in applications. Moreover, Δξ,𝝀\Delta\_{\xi,\boldsymbol{\lambda}} can be considered as a representation of the overall risk diversification level of the pool, and in addition, a smaller Δξ,𝝀\Delta\_{\xi,\boldsymbol{\lambda}} is also preferred as it can yield lower DRi​(1)\mathrm{DR}\_{i}(1) due to δi\delta\_{i}’s being positive.

### 2.3 Pool with general losses

In this subsection, we consider the general case where risks can have different
heavy-tailedness, which is specified in the following model.

Model 2

* •

  F¯i∈RV−αi\overline{F}\_{i}\in\mathrm{RV}\_{-\alpha\_{i}} with αi>0\alpha\_{i}>0, for
  i=1,…,ni=1,...,n, and α1=min⁡{α1,…,αn}\alpha\_{1}=\min\left\{\alpha\_{1},...,\alpha\_{n}\right\}. Furthermore, we assume that there exists θi≥0\theta\_{i}\geq 0 such that

  |  |  |  |
  | --- | --- | --- |
  |  | limt→∞F¯i​(t)F¯1​(t)=θi≥0,\lim\_{t\rightarrow\infty}\frac{\overline{F}\_{i}(t)}{\overline{F}\_{1}(t)}=\theta\_{i}\geq 0, |  |

  provided that θi>0\theta\_{i}>0 if αi=α1\alpha\_{i}=\alpha\_{1} and θi=0\theta\_{i}=0 if
  αi>α1\alpha\_{i}>\alpha\_{1}.
* •

  The attachment point and limit are functions of pp, i.e., di=di​(p)d\_{i}=d\_{i}(p)
  and li=li​(p)l\_{i}=l\_{i}(p), i=1,…,ni=1,...,n, which satisfy that for some ξ>0\xi>0,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | limp→1di​(p)VaRp​(Xi)=ξα1/αi,\lim\_{p\rightarrow 1}\frac{d\_{i}(p)}{\mathrm{VaR}\_{p}(X\_{i})}=\xi^{\alpha\_{1}/\alpha\_{i}}, |  | (2.10) |

  and for some λi>1\lambda\_{i}>1,

  |  |  |  |
  | --- | --- | --- |
  |  | limp→1li​(p)di​(p)=λi>1.\lim\_{p\rightarrow 1}\frac{l\_{i}(p)}{d\_{i}(p)}=\lambda\_{i}>1. |  |

In Model 2, the tails of X1,X2,…,XnX\_{1},X\_{2},...,X\_{n} can decay at different speeds
captured by the tail indices αi\alpha\_{i}’s. There is a more substantial
difference among the risks than that in Model 1, where, although with different scales, the tails decay at the same speed (i.e., with same tail index). A smaller tail
index means a heavier tail for the risk. Without loss of generality, the loss X1X\_{1} is
assumed to have the heaviest tail in the pool.

When a loss XiX\_{i} has the same tail index as X1X\_{1}, they are
tail equivalent, which is the same as in Model 1, but may be
different in scale, again captured by θi>0\theta\_{i}>0. When a loss XiX\_{i} has
a different tail index from X1X\_{1}, by the assumption that X1X\_{1} has the
heaviest tail, its tail index αi\alpha\_{i} is strictly larger than α1\alpha\_{1}, and its scale parameter θi\theta\_{i} is still well-defined as 0.

The attachment point did\_{i} is assumed to be ξα1/αi\xi^{\alpha\_{1}/\alpha\_{i}}
times the benchmark risk level VaRp​(Xi)\mathrm{VaR}\_{p}(X\_{i}), which takes the difference in heavy-tailedness into account. When αi=α1\alpha\_{i}=\alpha\_{1}, it is reduced to ξ\xi as seen in
Model 1. Again, we allow λi\lambda\_{i}’s to be different for each loss and they
will be optimally chosen for fixed levels of ξ\xi in order to achieve a Pareto optimal pool in Subsection
[2.4](https://arxiv.org/html/2512.18790v1#S2.SS4 "2.4 Asymptotic optimal pool ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.").

Overall, when all tail indices in Model 2 are the same, Model 2 reduces to
Model 1. Similarly to Lemma [2.1](https://arxiv.org/html/2512.18790v1#S2.Thmlemma1 "Lemma 2.1 ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."), we obtain the following useful
relations for Model 2.

###### Lemma 2.2

Under Model 2, we have

|  |  |  |
| --- | --- | --- |
|  | limp→1di​(p)d1​(p)=θi1/α1,limp→1F¯i​(di)F¯1​(d1)=1,\lim\_{p\rightarrow 1}\frac{d\_{i}(p)}{d\_{1}(p)}=\theta\_{i}^{1/\alpha\_{1}},\qquad\lim\_{p\rightarrow 1}\frac{\overline{F}\_{i}(d\_{i})}{\overline{F}\_{1}(d\_{1})}=1, |  |

and

|  |  |  |
| --- | --- | --- |
|  | limp→1di​(p)VaRp​(X1)=θi1/α1​ξ,limp→1li​(p)VaRp​(X1)=λi​θi1/α1​ξ.\lim\_{p\rightarrow 1}\frac{d\_{i}(p)}{\mathrm{VaR}\_{p}(X\_{1})}=\theta\_{i}^{1/\alpha\_{1}}\xi,\qquad\lim\_{p\rightarrow 1}\frac{l\_{i}(p)}{\mathrm{VaR}\_{p}(X\_{1})}=\lambda\_{i}\theta\_{i}^{1/\alpha\_{1}}\xi. |  |

When θi≠0\theta\_{i}\neq 0, Lemma
[2.2](https://arxiv.org/html/2512.18790v1#S2.Thmlemma2 "Lemma 2.2 ‣ 2.3 Pool with general losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") confers the same implications as Lemma [2.1](https://arxiv.org/html/2512.18790v1#S2.Thmlemma1 "Lemma 2.1 ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."). When θi=0\theta\_{i}=0, three
limits in Lemma [2.2](https://arxiv.org/html/2512.18790v1#S2.Thmlemma2 "Lemma 2.2 ‣ 2.3 Pool with general losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") are reduced to 0. This result is intuitive because when
θi=0\theta\_{i}=0, XiX\_{i} has a lighter tail than X1X\_{1}
and its attachment point did\_{i} (or its limit lil\_{i}) grows at a lower speed than
d1d\_{1} (or l1l\_{1}) as pp approaches 1. Nonetheless, for any θi≥0\theta\_{i}\geq 0,
the attachment points are still set in such a way that the tail probability of each
loss at its attachment point is approximately the same. Moreover, following
the proof of Lemma [2.2](https://arxiv.org/html/2512.18790v1#S2.Thmlemma2 "Lemma 2.2 ‣ 2.3 Pool with general losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."), we can show that for θi≥0\theta\_{i}\geq 0,

|  |  |  |
| --- | --- | --- |
|  | limp→1F¯i​(li)F¯1​(l1)=λ1α1λiαi.\lim\_{p\rightarrow 1}\frac{\overline{F}\_{i}(l\_{i})}{\overline{F}\_{1}(l\_{1})}=\frac{\lambda\_{1}^{\alpha\_{1}}}{\lambda\_{i}^{\alpha\_{i}}}. |  |

This means that the tail probability of loss XiX\_{i} at its limit lil\_{i} is
λ1α1/λiαi\lambda\_{1}^{\alpha\_{1}}/\lambda\_{i}^{\alpha\_{i}} times that of X1X\_{1},
which depends on λ1\lambda\_{1}, λi\lambda\_{i}, and the tail indices.

Now, we are ready to show the asymptotic expression of DRi​(p)\mathrm{DR}\_{i}(p) as
p→1p\rightarrow 1 under Model 2.

###### Theorem 2.2

Under Model 2, we have

|  |  |  |
| --- | --- | --- |
|  | DRi​(1)={1+δ~i​Δξ,𝝀,ξ≥1,ξα1/αi+δ~i​Δξ,𝝀,1/λi≤ξα1/αi<1,1−(λi−1)​ξα1/αi+δ~i​Δξ,𝝀,ξα1/αi<1/λi.\mathrm{DR}\_{i}(1)=\left\{\begin{array}[c]{lll}1+\widetilde{\delta}\_{i}\Delta\_{\xi,\boldsymbol{\lambda}},&&\xi\geq 1,\\ \xi^{\alpha\_{1}/\alpha\_{i}}+\widetilde{\delta}\_{i}\Delta\_{\xi,\boldsymbol{\lambda}},&&1/\lambda\_{i}\leq\xi^{\alpha\_{1}/\alpha\_{i}}<1,\\ 1-(\lambda\_{i}-1)\xi^{\alpha\_{1}/\alpha\_{i}}+\widetilde{\delta}\_{i}\Delta\_{\xi,\boldsymbol{\lambda}},&&\xi^{\alpha\_{1}/\alpha\_{i}}<1/\lambda\_{i}.\end{array}\right. |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ~i=(1−α1)​(λi1−αi−1)​ξα1/αi−1(1−αi)​∑j=1n(λj1−α1−1)​θj1/α1,Δξ,𝝀=(∑j∈Z(θj−1/α1+ξ)−α1)1/α1\widetilde{\delta}\_{i}=\frac{\left(1-\alpha\_{1}\right)\left(\lambda\_{i}^{1-\alpha\_{i}}-1\right)\xi^{\alpha\_{1}/\alpha\_{i}-1}}{(1-\alpha\_{i})\sum\_{j=1}^{n}\left(\lambda\_{j}^{1-\alpha\_{1}}-1\right)\theta\_{j}^{1/\alpha\_{1}}},\qquad\Delta\_{\xi,\boldsymbol{\lambda}}=\left(\sum\_{j\in Z}\left(\theta\_{j}^{-1/\alpha\_{1}}+\xi\right)^{-\alpha\_{1}}\right)^{1/\alpha\_{1}} |  | (2.11) |

with Z={j=1,2,…,n:ξ>θj−1/α1​(λj−1)−1}Z=\left\{j=1,2,...,n:\xi>\theta\_{j}^{-1/\alpha\_{1}}\left(\lambda\_{j}-1\right)^{-1}\right\}.

When all tail indices αi\alpha\_{i}’s are the same, Theorem [2.2](https://arxiv.org/html/2512.18790v1#S2.Thmtheorem2 "Theorem 2.2 ‣ 2.3 Pool with general losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") reduces to Theorem [2.1](https://arxiv.org/html/2512.18790v1#S2.Thmtheorem1 "Theorem 2.1 ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."). Similarly to Theorem
[2.1](https://arxiv.org/html/2512.18790v1#S2.Thmtheorem1 "Theorem 2.1 ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."), we observe that a
smaller Δξ,𝝀\Delta\_{\xi,\boldsymbol{\lambda}}
can yield a lower DRi​(1)\mathrm{DR}\_{i}(1), which is the preferred case.
Note that
if θj=0\theta\_{j}=0, then risk jj does not belong to the set ZZ in
([2.11](https://arxiv.org/html/2512.18790v1#S2.E11 "In Theorem 2.2 ‣ 2.3 Pool with general losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")). Thus, lighter-tailed risks have no contribution to
Δξ,𝝀\Delta\_{\xi,\boldsymbol{\lambda}}, and only losses as heavy-tailed
as X1X\_{1} determine the overall risk diversification level of the pool.

### 2.4 Asymptotic optimal pool

In this subsection, we derive the optimal pooling structure at the limit for a pool
with general losses under Model 2. More specifically, we aim at minimizing
DRi​(1)\mathrm{DR}\_{i}(1) for each participant based on the asymptotic expression
derived earlier in Theorem [2.2](https://arxiv.org/html/2512.18790v1#S2.Thmtheorem2 "Theorem 2.2 ‣ 2.3 Pool with general losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."). This is done first by fixing the value of ξ\xi and
solving for the optimal λi\lambda\_{i}’s. The resulting pool, called the asymptotic
optimal pool, enables a global maximization of the diversification benefit
for all participants in the pool and naturally leads to a Pareto optimality. It provides an
approximation to the practical problem ([2.3](https://arxiv.org/html/2512.18790v1#S2.E3 "In 2.1 Pool setup ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) at a level pp close to 1.

###### Theorem 2.3

Assume that 0≤θi≤10\leq\theta\_{i}\leq 1 for i=1,…,ni=1,...,n. Under Model 2, we have for any ξ>0\xi>0,

|  |  |  |
| --- | --- | --- |
|  | min𝝀⁡DRi​(1)={1,ξ≥1,ξα1/αi,0<ξ<1,\min\_{\boldsymbol{\lambda}}\mathrm{DR}\_{i}(1)=\left\{\begin{array}[c]{lll}1,&&\xi\geq 1,\\ \xi^{\alpha\_{1}/\alpha\_{i}},&&0<\xi<1,\end{array}\right. |  |

where the optimal 𝛌∗=arg⁡min𝛌⁡DRi​(1)\boldsymbol{\lambda}^{\ast}=\arg\min\_{\boldsymbol{\lambda}}\mathrm{DR}\_{i}(1) satisfies that

|  |  |  |
| --- | --- | --- |
|  | 𝝀∗∈{(λ1,…,λn):min⁡{ξ−α1/αi,1}≤λi≤1+θi−1/α1​ξ−1,i=1,…,n}.\boldsymbol{\lambda}^{\ast}\in\{(\lambda\_{1},...,\lambda\_{n}):\min\left\{\xi^{-\alpha\_{1}/\alpha\_{i}},1\right\}\leq\lambda\_{i}\leq 1+\theta\_{i}^{-1/\alpha\_{1}}\xi^{-1},i=1,...,n\}. |  |

We note that in Theorem [2.3](https://arxiv.org/html/2512.18790v1#S2.Thmtheorem3 "Theorem 2.3 ‣ 2.4 Asymptotic optimal pool ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."), the condition that 0≤θi≤10\leq\theta\_{i}\leq 1 is without loss of generality. Indeed, 0<θi≤10<\theta\_{i}\leq 1 means that X1X\_{1} is set so that all other risks of same heavy-tailedness as X1X\_{1} has smaller scales, while θi=0\theta\_{i}=0 means that the risk of the ii-th participant has a lighter tail than X1X\_{1}. As such, this theorem can be applied to any pool of risks satisfying Model 2.

Theorem [2.3](https://arxiv.org/html/2512.18790v1#S2.Thmtheorem3 "Theorem 2.3 ‣ 2.4 Asymptotic optimal pool ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") shows that at the limit, for any given ξ\xi, the
global optimal is achieved, i.e., each DRi​(1)\mathrm{DR}\_{i}(1) is minimized, which
means that all participants in the pool can simultaneously obtain the maximum diversification benefit from the
pool. It naturally implies that this pooling structure is Pareto optimal as well, where we have for any ξ>0\xi>0

|  |  |  |
| --- | --- | --- |
|  | min𝝀​∑i=1nDRi​(1)={n,ξ≥1,∑i=1nξα1/αi,0<ξ<1.\min\_{\boldsymbol{\lambda}}\sum\_{i=1}^{n}\mathrm{DR}\_{i}(1)=\left\{\begin{array}[c]{lll}n,&&\xi\geq 1,\\ \sum\_{i=1}^{n}\xi^{\alpha\_{1}/\alpha\_{i}},&&0<\xi<1.\end{array}\right. |  |

By incorporating the assumptions of Model 2 at a level pp close to 1, the practical problem ([2.3](https://arxiv.org/html/2512.18790v1#S2.E3 "In 2.1 Pool setup ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) can be specified for a fixed level ξ>0\xi>0 as

|  |  |  |  |
| --- | --- | --- | --- |
|  | minλi>1,i=1,…,n​∑i=1nDRi​(p).\min\_{\lambda\_{i}>1,i=1,...,n}\sum\_{i=1}^{n}\mathrm{DR}\_{i}(p). |  | (2.12) |

The optimal 𝝀∗\boldsymbol{\lambda}^{\ast} can be used to approximate the
optimal solution 𝝀​(p)\boldsymbol{\lambda}(p) of the practical problem
([2.12](https://arxiv.org/html/2512.18790v1#S2.E12 "In 2.4 Asymptotic optimal pool ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) at a level pp close to 1, which is a high-dimensional
optimization problem for which the analytical solution is highly intractable.
We show with a set of simulations in the next section that the asymptotic solution is a
good approximation to the solution of the practical problem.

If the given ξ\xi is greater than or equal to 11, then each participant has a
DRi​(1)\mathrm{DR}\_{i}(1) of at least 11, which is not ideal as no risk
reduction is obtained from joining the pool. When the given ξ\xi is less than
1, each participant can achieve the lowest DRi​(1)\mathrm{DR}\_{i}(1) as
ξα1/αi<1\xi^{\alpha\_{1}/\alpha\_{i}}<1. Therefore, each
participant obtains the largest risk reduction by joining the pool and the
pool distributes the diversification benefit efficiently among participants.

From Theorem [2.3](https://arxiv.org/html/2512.18790v1#S2.Thmtheorem3 "Theorem 2.3 ‣ 2.4 Asymptotic optimal pool ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."), we see that the lower ξ\xi is, the more
diversification benefit each participant obtains. However, it is important to point out that the current methodology does
not apply to the case where ξ=0\xi=0. Therefore, the asymptotic pool in this paper is
derived for any given ξ\xi that is less than 1 and strictly greater than 0.

From the proof of Theorem [2.3](https://arxiv.org/html/2512.18790v1#S2.Thmtheorem3 "Theorem 2.3 ‣ 2.4 Asymptotic optimal pool ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."), we see that the feasible set
𝝀∗\boldsymbol{\lambda}^{\ast} is obtained from solving Δξ,𝝀=0\Delta\_{\xi,\boldsymbol{\lambda}}=0 for any given ξ\xi. It means that the asymptotic
optimal pool can completely diversify away the aggregated risk. As a result, each participant is only left with the retained risk. Participants with heavier tails (i.e., smaller
αi\alpha\_{i}) can gain a larger diversification benefit (smaller ξα1/αi\xi^{\alpha\_{1}/\alpha\_{i}}) in this pool. For a participant with a lighter
tail (i.e., αi>α1\alpha\_{i}>\alpha\_{1}), its scale θi\theta\_{i} is 0, which leads to the
upper bound of λi∗\lambda\_{i}^{\ast} being ∞\infty. This means that
participants with lighter tails can bring in unlimited risk to the pool, which
provides greater flexibility for these pool participants.

## 3 Simulation study

In this section, we compare the solution 𝝀∗\boldsymbol{\lambda}^{\ast} of the
optimization problem min𝝀​∑i=1nDRi​(1)\min\_{\boldsymbol{\lambda}}\sum\_{i=1}^{n}\mathrm{DR}\_{i}(1) obtained from Theorem [2.3](https://arxiv.org/html/2512.18790v1#S2.Thmtheorem3 "Theorem 2.3 ‣ 2.4 Asymptotic optimal pool ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") with the
optimal solution 𝝀​(p)\boldsymbol{\lambda}(p) to the practical problem
([2.12](https://arxiv.org/html/2512.18790v1#S2.E12 "In 2.4 Asymptotic optimal pool ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")). The analytical expression of
𝝀​(p)\boldsymbol{\lambda}(p) is generally not available, and its numerical approximation has a high computational cost as it requires solving the
multi-dimensional optimization program ([2.12](https://arxiv.org/html/2512.18790v1#S2.E12 "In 2.4 Asymptotic optimal pool ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")). In this section, we apply a
Generalized Simulated Annealing (GSA) optimization algorithm (package GenSA in R) to search for
a multi-dimensional optimal solution. GSA is a generalized version of Simulated Annealing which is a popular stochastic optimization algorithm inspired by the annealing heat treatment used in Metallurgy to minimize the material’s internal energy (tsallis1996generalized; xiang\_generalized\_2013).
In Appendix [B](https://arxiv.org/html/2512.18790v1#A2 "Appendix B Comparison of algorithms for simulation study ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."), we compare the GSA
algorithm with four other optimization algorithms and find that GSA
provides accurate solutions while also being efficient at the same time.

In this study, we assume that the losses XiX\_{i}’s follow a Fréchet distribution

|  |  |  |
| --- | --- | --- |
|  | Fi​(x)=e−(x/si)−αi,si>0​,F\_{i}(x)=e^{-(x/s\_{i})^{-\alpha\_{i}}},\qquad s\_{i}>0\text{,} |  |

denoted by Fi∼Fr​e´​chet​(αi,si)F\_{i}\sim\mathrm{Fr\acute{e}chet}\left(\alpha\_{i},s\_{i}\right). It can be
shown that F¯i∈RV−αi\overline{F}\_{i}\in\mathrm{RV}\_{-\alpha\_{i}} and that the analytical form of its quantile function is Fi←​(p)=si​[−ln⁡(p)]−1/αiF\_{i}^{\leftarrow}(p)=s\_{i}[-\ln(p)]^{-1/\alpha\_{i}}. To compute the numerical solution of ([2.12](https://arxiv.org/html/2512.18790v1#S2.E12 "In 2.4 Asymptotic optimal pool ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) at a level pp, we first
simulate a sample of one million observations for the random vector
(X1,…,Xn)(X\_{1},...,X\_{n}), denoted by {(Xj,1,…,Xj,n)}{j=1,…,m}\{(X\_{j,1},...,X\_{j,n})\}\_{\{j=1,...,m\}},
with m=1,000,000m=1,000,000. For a given ξ\xi and each (λ1,…,λn)(\lambda\_{1},...,\lambda\_{n}), the attachment point did\_{i} is computed as ξα1/αi​Fi←​(p)\xi^{\alpha\_{1}/\alpha\_{i}}F\_{i}^{\leftarrow}(p), and the limit lil\_{i} is λi​di\lambda\_{i}d\_{i} for
i=1,…,ni=1,...,n. The observed layer loss Yj,iY\_{j,i} for each observation Xj,iX\_{j,i}
are then computed by using ([2.1](https://arxiv.org/html/2512.18790v1#S2.E1 "In 2.1 Pool setup ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")). Thus the jj-th observation of the
aggregated loss of the pool is Sj=∑i=1nYj,iS\_{j}=\sum\_{i=1}^{n}Y\_{j,i}. Let Z(1)≤Z(2)≤⋯≤Z(m)Z\_{(1)}\leq Z\_{(2)}\leq\cdots\leq Z\_{(m)} denote the order statistics of the sample
Z1,…,ZmZ\_{1},...,Z\_{m}, Z(1),i≤Z(2),i≤⋯≤Z(m),iZ\_{(1),i}\leq Z\_{(2),i}\leq\cdots\leq Z\_{(m),i}
denote the order statistics of the sample Z1,i,…,Zm,iZ\_{1,i},...,Z\_{m,i}, and ⌊x⌋\lfloor x\rfloor denote the integer value of xx. Then
DRi​(p)\mathrm{DR}\_{i}(p) is estimated as

|  |  |  |
| --- | --- | --- |
|  | DR^i​(p)=VaRp​(Xi−Yi)VaRp​(Xi)+E​[Yi]^∑i=1nE​[Yi]^​S(⌊p​m⌋)X(⌊p​m⌋),i,\widehat{\mathrm{DR}}\_{i}(p)=\frac{\mathrm{VaR}\_{p}(X\_{i}-Y\_{i})}{\mathrm{VaR}\_{p}(X\_{i})}+\frac{\widehat{E[Y\_{i}]}}{\sum\_{i=1}^{n}\widehat{E[Y\_{i}]}}\frac{S\_{(\lfloor pm\rfloor)}}{X\_{(\lfloor pm\rfloor),i}}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | VaRp​(Xi−Yi)VaRp​(Xi)={1,Fi←​(p)≤di,diFi←​(p),di<Fi←​(p)≤li,1−li−diFi←​(p),Fi←​(p)>li,\frac{\mathrm{VaR}\_{p}(X\_{i}-Y\_{i})}{\mathrm{VaR}\_{p}(X\_{i})}=\left\{\begin{array}[c]{lll}1,&&F\_{i}^{\leftarrow}(p)\leq d\_{i},\\ \frac{d\_{i}}{F\_{i}^{\leftarrow}(p)},&&d\_{i}<F\_{i}^{\leftarrow}(p)\leq l\_{i},\\ 1-\frac{l\_{i}-d\_{i}}{F\_{i}^{\leftarrow}(p)},&&F\_{i}^{\leftarrow}(p)>l\_{i},\end{array}\right. |  |

and E​[Yi]^\widehat{E[Y\_{i}]} is the approximation of

|  |  |  |
| --- | --- | --- |
|  | E​[Yi]=∫diliF¯i​(x)​𝑑x=∫dili(1−e−(x/si)−αi)​𝑑xE[Y\_{i}]=\int\_{d\_{i}}^{l\_{i}}\overline{F}\_{i}(x)dx=\int\_{d\_{i}}^{l\_{i}}\left(1-e^{-(x/s\_{i})^{-\alpha\_{i}}}\right)dx |  |

by using function integrate()
in R.
Then we apply the GSA algorithm to search for the solution
𝝀^​(p)\boldsymbol{\widehat{\lambda}}(p) of ([2.12](https://arxiv.org/html/2512.18790v1#S2.E12 "In 2.4 Asymptotic optimal pool ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")).

Since the feasible solutions 𝝀∗\boldsymbol{\lambda}^{\ast} form a set and the
GSA algorithm only produces one single value of 𝝀^​(p)\boldsymbol{\widehat{\lambda}}(p) for each sample, we define the distance between 𝝀∗\boldsymbol{\lambda}^{\ast} and
𝝀^​(p)\boldsymbol{\widehat{\lambda}}(p) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π​(p)=min𝝀∗⁡‖𝝀^​(p)−𝝀∗‖,\Pi(p)=\min\_{\boldsymbol{\lambda}^{\ast}}\left\|\boldsymbol{\widehat{\lambda}}(p)-\boldsymbol{\lambda}^{\ast}\right\|, |  | (3.1) |

where ∥⋅∥\left\|\cdot\right\| denotes a Euclidean norm.

In the first study, we consider two tail equivalent losses represented by X1∼Fr​e´​chet​(8.5,100)X\_{1}\sim\mathrm{Fr\acute{e}chet}\left(8.5,100\right) and X2∼Fr​e´​chet​(8.5,90)X\_{2}\sim\mathrm{Fr\acute{e}chet}\left(8.5,90\right). Then they have the same tail index of 8.58.5 but with
different scales. It can be shown that θ1=1\theta\_{1}=1 and θ2=(9/10)8.5\theta\_{2}=(9/10)^{8.5} according to ([2.5](https://arxiv.org/html/2512.18790v1#S2.E5 "In 1st item ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")). Thus X1X\_{1} and X2X\_{2} satisfy
Model 1. We use 50 samples, for each of which we
repeat the process of finding 𝝀^​(p)=(λ^1​(p),λ^2​(p))\boldsymbol{\widehat{\lambda}}(p)=(\widehat{\lambda}\_{1}(p),\widehat{\lambda}\_{2}(p)) for a selection of levels pp: {0.8,0.825,0.85,0.875,0.9,0.925,0.95,0.975,0.99}\{0.8,0.825,0.85,0.875,0.9,0.925,0.95,0.975,0.99\}.
A summary of the results is shown in Table [1](https://arxiv.org/html/2512.18790v1#S3.T1 "Table 1 ‣ 3 Simulation study ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.").

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ^1​(p)\widehat{\lambda}\_{1}(p) | λ^2​(p)\widehat{\lambda}\_{2}(p) | Π​(p)\Pi(p) |
| ξ=0.11/8.5\xi=0.1^{1/8.5}, 𝝀∗∈{(λ1,λ2):1.3111≤λ1≤2.3111,1.3111≤λ2≤2.4568}\boldsymbol{\lambda}^{\ast}\in\{(\lambda\_{1},\lambda\_{2}):1.3111\leq\lambda\_{1}\leq 2.3111,1.3111\leq\lambda\_{2}\leq 2.4568\} | | | |
| p=0.800p=0.800 | 1.311136 (3.485×10−63.485\times 10^{-6}) | 1.311134 (8.637×10−78.637\times 10^{-7}) | 2.086×10−62.086\times 10^{-6} (3.353×10−63.353\times 10^{-6}) |
| p=0.825p=0.825 | 1.311135 (2.492×10−62.492\times 10^{-6}) | 1.311134 (6.727×10−76.727\times 10^{-7}) | 2.006×10−62.006\times 10^{-6} (2.012×10−62.012\times 10^{-6}) |
| p=0.850p=0.850 | 1.311136 (3.293×10−63.293\times 10^{-6}) | 1.311134 (8.034×10−78.034\times 10^{-7}) | 2.559×10−62.559\times 10^{-6} (2.754×10−62.754\times 10^{-6}) |
| p=0.875p=0.875 | 1.311137 (7.945×10−67.945\times 10^{-6}) | 1.311135 (3.952×10−63.952\times 10^{-6}) | 4.415×10−64.415\times 10^{-6} (8.294×10−68.294\times 10^{-6}) |
| p=0.900p=0.900 | 1.311135 (4.989×10−64.989\times 10^{-6}) | 1.311135 (1.123×10−61.123\times 10^{-6}) | 3.313×10−63.313\times 10^{-6} (4.138×10−64.138\times 10^{-6}) |
| p=0.925p=0.925 | 1.311137 (5.973×10−65.973\times 10^{-6}) | 1.311135 (1.157×10−61.157\times 10^{-6}) | 4.658×10−64.658\times 10^{-6} (4.837×10−64.837\times 10^{-6}) |
| p=0.950p=0.950 | 1.311139 (7.343×10−67.343\times 10^{-6}) | 1.311135 (1.067×10−61.067\times 10^{-6}) | 6.000×10−66.000\times 10^{-6} (6.355×10−66.355\times 10^{-6}) |
| p=0.975p=0.975 | 1.280022 (2.252×10−62.252\times 10^{-6}) | 1.311135 (2.536×10−62.536\times 10^{-6}) | 0.031112 (2.252×10−62.252\times 10^{-6}) |
| p=0.990p=0.990 | 1.290521 (0.01476691) | 7198.80 (13290.34) | 7197.11 (13289.91) |
| ξ=0.31/8.5\xi=0.3^{1/8.5}, 𝝀∗∈{(λ1,λ2):1.1522≤λ1≤2.1522,1.1522≤λ2≤2.2802}\boldsymbol{\lambda}^{\ast}\in\{(\lambda\_{1},\lambda\_{2}):1.1522\leq\lambda\_{1}\leq 2.1522,1.1522\leq\lambda\_{2}\leq 2.2802\} | | | |
| p=0.800p=0.800 | 1.147701 (2.929×10−42.929\times 10^{-4}) | 1.152167 (2.018×10−62.018\times 10^{-6}) | 0.004465 (2.929×10−42.929\times 10^{-4}) |
| p=0.825p=0.825 | 1.136951 (2.245×10−62.245\times 10^{-6}) | 1.152168 (2.457×10−62.457\times 10^{-6}) | 0.015215 (2.245×10−62.245\times 10^{-6}) |
| p=0.850p=0.850 | 1.136950 (6.760×10−86.760\times 10^{-8}) | 1.152166 (3.083×10−83.083\times 10^{-8}) | 0.015216 (6.760×10−86.760\times 10^{-8}) |
| p=0.875p=0.875 | 1.136951 (9.338×10−79.338\times 10^{-7}) | 1.152168 (9.206×10−79.206\times 10^{-7}) | 0.015215 (9.338×10−79.338\times 10^{-7}) |
| p=0.900p=0.900 | 1.136950 (1.093×10−61.093\times 10^{-6}) | 1.152167 (2.628×10−72.628\times 10^{-7}) | 0.015216 (1.093×10−61.093\times 10^{-6}) |
| p=0.925p=0.925 | 1.136978 (1.400×10−41.400\times 10^{-4}) | 1.152168 (7.317×10−67.317\times 10^{-6}) | 0.015189 (1.400×10−41.400\times 10^{-4}) |
| p=0.950p=0.950 | 1.136953 (1.332×10−51.332\times 10^{-5}) | 1.152170 (1.483×10−51.483\times 10^{-5}) | 0.015213 (1.328×10−51.328\times 10^{-5}) |
| p=0.975p=0.975 | 1.139445 (0.0054) | 9880.94 (46848.42) | 9879.60 (46848.22) |
| p=0.990p=0.990 | 1.139079 (0.0053) | 2005.45 (5243.49) | 2004.15 (5243.10) |
| ξ=0.51/8.5\xi=0.5^{1/8.5}, 𝝀∗∈{(λ1,λ2):1.0850≤λ1≤2.0850,1.0850≤λ2≤2.2055}\boldsymbol{\lambda}^{\ast}\in\{(\lambda\_{1},\lambda\_{2}):1.0850\leq\lambda\_{1}\leq 2.0850,1.0850\leq\lambda\_{2}\leq 2.2055\} | | | |
| p=0.800p=0.800 | 1.076468 (2.489×10−82.489\times 10^{-8}) | 1.084964 (5.657×10−95.657\times 10^{-9}) | 0.008496 (2.489×10−82.489\times 10^{-8}) |
| p=0.825p=0.825 | 1.076472 (1.466×10−61.466\times 10^{-6}) | 1.084964 (1.980×10−81.980\times 10^{-8}) | 0.008492 (1.466×10−61.466\times 10^{-6}) |
| p=0.850p=0.850 | 1.076472 (1.359×10−81.359\times 10^{-8}) | 1.084964 (5.094×10−95.094\times 10^{-9}) | 0.008492 (1.359×10−81.359\times 10^{-8}) |
| p=0.875p=0.875 | 1.076472 (1.078×10−61.078\times 10^{-6}) | 1.084968 (1.159×10−61.159\times 10^{-6}) | 0.008492 (1.078×10−61.078\times 10^{-6}) |
| p=0.900p=0.900 | 1.076471 (1.880×10−61.880\times 10^{-6}) | 1.084968 (2.022×10−62.022\times 10^{-6}) | 0.008493 (1.880×10−61.880\times 10^{-6}) |
| p=0.925p=0.925 | 1.076691 (0.001558) | 5274.84 (37291.11) | 5273.74 (37290.95) |
| p=0.950p=0.950 | 1.076806 (0.001671) | 470.53 (2389.10) | 469.41 (2388.89) |
| p=0.975p=0.975 | 1.120331 (0.299812) | 35621.42 (111784.24) | 35620.07 (111783.96) |
| p=0.990p=0.990 | 2.022278 (0.996342) | 1223.92 (6821.75) | 1.223.26 (6821.47) |
| ξ=0.71/8.5\xi=0.7^{1/8.5}, 𝝀∗∈{(λ1,λ2):1.0428≤λ1≤2.0428,1.0428≤λ2≤2.1587}\boldsymbol{\lambda}^{\ast}\in\{(\lambda\_{1},\lambda\_{2}):1.0428\leq\lambda\_{1}\leq 2.0428,1.0428\leq\lambda\_{2}\leq 2.1587\} | | | |
| p=0.800p=0.800 | 1.038573 (1.515×10−91.515\times 10^{-9}) | 1.042858 (6.061×10−106.061\times 10^{-10}) | 0.004282 (1.515×10−91.515\times 10^{-9}) |
| p=0.825p=0.825 | 1.038573 (8.314×10−98.314\times 10^{-9}) | 1.042858 (8.512×10−98.512\times 10^{-9}) | 0.004282 (8.306×10−98.306\times 10^{-9}) |
| p=0.850p=0.850 | 1.038570 (1.584×10−81.584\times 10^{-8}) | 1.042855 (5.233×10−95.233\times 10^{-9}) | 0.004285 (1.584×10−81.584\times 10^{-8}) |
| p=0.875p=0.875 | 1.038571 (2.295×10−62.295\times 10^{-6}) | 1.042856 (2.832×10−62.832\times 10^{-6}) | 0.004284 (2.292×10−62.292\times 10^{-6}) |
| p=0.900p=0.900 | 1.038570 (5.663×10−75.663\times 10^{-7}) | 1.042855 (4.288×10−74.288\times 10^{-7}) | 0.004284 (5.663×10−75.663\times 10^{-7}) |
| p=0.925p=0.925 | 1.038571 (2.935×10−62.935\times 10^{-6}) | 1.042855 (8.213×10−78.213\times 10^{-7}) | 0.004283 (2.935×10−62.935\times 10^{-6}) |
| p=0.950p=0.950 | 1.070454 (0.223433) | 1615.48 (4892.52) | 1614.34 (4892.18) |
| p=0.975p=0.975 | 2.679588 (6.628282) | 1.042856 (2.396×10−62.396\times 10^{-6}) | 1.181359 (6.50907) |
| p=0.990p=0.990 | 3.352461 (7.815203) | 936.62 (6615.53) | 937.17 (6615.14) |

Table 1: Pool with two tail equivalent losses X1∼Fr​e´​chet​(8.5,100)X\_{1}\sim\mathrm{Fr\acute{e}chet}\left(8.5,100\right) and X2∼Fr​e´​chet​(8.5,90)X\_{2}\sim\mathrm{Fr\acute{e}chet}\left(8.5,90\right). Sample mean and standard error are reported.

In the second study, we have two losses represented by X1∼Fr​e´​chet​(8.5,100)X\_{1}\sim\mathrm{Fr\acute{e}chet}(8.5,100) and X2∼Fr​e´​chet​(9,100)X\_{2}\sim\mathrm{Fr\acute{e}chet}(9,100). Thus, they have
different tail indices of 8.58.5 and 99. It can be shown that θ1=1\theta\_{1}=1
and θ2=0\theta\_{2}=0 according to ([2.5](https://arxiv.org/html/2512.18790v1#S2.E5 "In 1st item ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")). So X1X\_{1} and X2X\_{2} satisfy
Model 2.
We use 50 samples, for each of which we
repeat the process of finding 𝝀^​(p)=(λ^1​(p),λ^2​(p))\boldsymbol{\widehat{\lambda}}(p)=(\widehat{\lambda}\_{1}(p),\widehat{\lambda}\_{2}(p)) for the same selection of levels pp as that in the first study.
A summary of the results is shown in Table [2](https://arxiv.org/html/2512.18790v1#S3.T2 "Table 2 ‣ 3 Simulation study ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.").

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ^1​(p)\widehat{\lambda}\_{1}(p) | λ^2​(p)\widehat{\lambda}\_{2}(p) | Π​(p)\Pi(p) |
| ξ=0.11/8.5\xi=0.1^{1/8.5}, 𝝀∗∈{(λ1,λ2):1.3111≤λ1≤2.3111,λ2≥1.2915}\boldsymbol{\lambda}^{\ast}\in\{(\lambda\_{1},\lambda\_{2}):1.3111\leq\lambda\_{1}\leq 2.3111,\lambda\_{2}\geq 1.2915\} | | | |
| p=0.800p=0.800 | 1.311135 (1.776×10−61.776\times 10^{-6}) | 1.291550 (9.240×10−79.240\times 10^{-7}) | 1.209982×10−61.209982\times 10^{-6} (1.557×10−61.557\times 10^{-6}) |
| p=0.825p=0.825 | 1.311134 (1.456×10−61.456\times 10^{-6}) | 1.291550 (6.781×10−76.781\times 10^{-7}) | 1.064790×10−61.064790\times 10^{-6} (1.081×10−61.081\times 10^{-6}) |
| p=0.850p=0.850 | 1.311135 (3.336×10−63.336\times 10^{-6}) | 1.291550 (1.539×10−61.539\times 10^{-6}) | 2.075998×10−62.075998\times 10^{-6} (2.961×10−62.961\times 10^{-6}) |
| p=0.875p=0.875 | 1.311135 (2.428×10−62.428\times 10^{-6}) | 1.291550 (9.873×10−79.873\times 10^{-7}) | 2.042666×10−62.042666\times 10^{-6} (1.982×10−61.982\times 10^{-6}) |
| p=0.900p=0.900 | 1.311137 (8.617×10−68.617\times 10^{-6}) | 1.291551 (2.215×10−62.215\times 10^{-6}) | 4.206583×10−64.206583\times 10^{-6} (8.181×10−68.181\times 10^{-6}) |
| p=0.925p=0.925 | 1.311138 (9.893×10−69.893\times 10^{-6}) | 1.291551 (4.177×10−64.177\times 10^{-6}) | 4.433363×10−64.433363\times 10^{-6} (9.544×10−69.544\times 10^{-6}) |
| p=0.950p=0.950 | 1.311138 (9.893×10−69.893\times 10^{-6}) | 1.291551 (4.177×10−64.177\times 10^{-6}) | 4.433363×10−64.433363\times 10^{-6} (9.544×10−69.544\times 10^{-6}) |
| p=0.975p=0.975 | 1.288958 (1.336×10−51.336\times 10^{-5}) | 1.291560 (1.252×10−51.252\times 10^{-5}) | 0.022176 (1.336×10−51.336\times 10^{-5}) |
| p=0.990p=0.990 | 1.287235 (0.000133) | 1.291553 (4.712×10−64.712\times 10^{-6}) | 0.023899 (0.000133) |
| ξ=0.31/8.5\xi=0.3^{1/8.5}, 𝝀∗∈{(λ1,λ2):1.1522≤λ1≤2.1522,λ2≥1.1431}\boldsymbol{\lambda}^{\ast}\in\{(\lambda\_{1},\lambda\_{2}):1.1522\leq\lambda\_{1}\leq 2.1522,\lambda\_{2}\geq 1.1431\} | | | |
| p=0.800p=0.800 | 1.152009 (0.000186) | 1.143137 (2.242×10−62.242\times 10^{-6}) | 0.000158 (0.000185) |
| p=0.825p=0.825 | 1.142726 (1.207×10−51.207\times 10^{-5}) | 1.143141 (1.186×10−51.186\times 10^{-5}) | 0.009440 (1.207×10−51.207\times 10^{-5}) |
| p=0.850p=0.850 | 1.142595 (1.468×10−51.468\times 10^{-5}) | 1.143144 (1.057×10−51.057\times 10^{-5}) | 0.009571 (1.468×10−51.468\times 10^{-5}) |
| p=0.875p=0.875 | 1.142404 (6.793×10−56.793\times 10^{-5}) | 1.143157 (6.801×10−56.801\times 10^{-5}) | 0.009762 (6.793×10−56.793\times 10^{-5}) |
| p=0.900p=0.900 | 1.142168 (9.421×10−69.421\times 10^{-6}) | 1.143143 (9.787×10−69.787\times 10^{-6}) | 0.009998 (9.421×10−69.421\times 10^{-6}) |
| p=0.925p=0.925 | 1.141885 (1.320×10−51.320\times 10^{-5}) | 1.143140 (1.337×10−51.337\times 10^{-5}) | 0.010281 (1.320×10−51.320\times 10^{-5}) |
| p=0.950p=0.950 | 1.141505 (2.996×10−52.996\times 10^{-5}) | 1.143144 (3.104×10−53.104\times 10^{-5}) | 0.010662 (2.996×10−52.996\times 10^{-5}) |
| p=0.975p=0.975 | 1.141307 (0.002242) | 1607.40 (9992.78) | 0.010861 (0.002237) |
| p=0.990p=0.990 | 1.140792 (0.002672) | 3176.93 (12684.18) | 0.011374 (0.002672) |
| ξ=0.51/8.5\xi=0.5^{1/8.5}, 𝝀∗∈{(λ1,λ2):1.0850≤λ1≤2.0850,λ2≥1.0801}\boldsymbol{\lambda}^{\ast}\in\{(\lambda\_{1},\lambda\_{2}):1.0850\leq\lambda\_{1}\leq 2.0850,\lambda\_{2}\geq 1.0801\} | | | |
| p=0.800p=0.800 | 1.079644 (2.206×10−62.206\times 10^{-6}) | 1.080063 (2.184×10−62.184\times 10^{-6}) | 0.005320 (2.206×10−62.206\times 10^{-6}) |
| p=0.825p=0.825 | 1.079565 (1.590×10−61.590\times 10^{-6}) | 1.080062 (1.819×10−61.819\times 10^{-6}) | 0.005400 (1.590×10−61.590\times 10^{-6}) |
| p=0.850p=0.850 | 1.079474 (1.047×10−71.047\times 10^{-7}) | 1.080060 (1.188×10−81.188\times 10^{-8}) | 0.005489 (1.047×10−71.047\times 10^{-7}) |
| p=0.875p=0.875 | 1.079375 (4.760×10−64.760\times 10^{-6}) | 1.080061 (4.415×10−64.415\times 10^{-6}) | 0.005589 (4.760×10−64.760\times 10^{-6}) |
| p=0.900p=0.900 | 1.079390 (1.974×10−51.974\times 10^{-5}) | 1.080060 (5.233×10−95.233\times 10^{-9}) | 0.005574 (1.974×10−51.974\times 10^{-5}) |
| p=0.925p=0.925 | 1.079095 (3.024×10−63.024\times 10^{-6}) | 1.080061 (2.361×10−62.361\times 10^{-6}) | 0.005869 (3.024×10−63.024\times 10^{-6}) |
| p=0.950p=0.950 | 1.078885 (2.786×10−62.786\times 10^{-6}) | 1.080061 (3.106×10−63.106\times 10^{-6}) | 0.006079 (2.786×10−62.786\times 10^{-6}) |
| p=0.975p=0.975 | 1.078530 (5.088×10−55.088\times 10^{-5}) | 1.080068 (1.049×10−51.049\times 10^{-5}) | 0.006434 (5.088×10−55.088\times 10^{-5}) |
| p=0.990p=0.990 | 1.401185 (1.013326) | 2646.74 (18707.64) | 0.187982 (0.760469) |
| ξ=0.71/8.5\xi=0.7^{1/8.5}, 𝝀∗∈{(λ1,λ2):1.0428≤λ1≤2.0428,λ2≥1.0404}\boldsymbol{\lambda}^{\ast}\in\{(\lambda\_{1},\lambda\_{2}):1.0428\leq\lambda\_{1}\leq 2.0428,\lambda\_{2}\geq 1.0404\} | | | |
| p=0.800p=0.800 | 1.040178 (1.922×10−51.922\times 10^{-5}) | 1.040427 (7.051×10−87.051\times 10^{-8}) | 0.002677 (1.922×10−51.922\times 10^{-5}) |
| p=0.825p=0.825 | 1.040100 (8.694×10−68.694\times 10^{-6}) | 1.040434 (1.095×10−51.095\times 10^{-5}) | 0.002754 (8.694×10−68.694\times 10^{-6}) |
| p=0.850p=0.850 | 1.040061 (1.776×10−51.776\times 10^{-5}) | 1.040436 (1.224×10−51.224\times 10^{-5}) | 0.002793 (1.776×10−51.776\times 10^{-5}) |
| p=0.875p=0.875 | 1.039997 (2.079×10−62.079\times 10^{-6}) | 1.040431 (3.339×10−63.339\times 10^{-6}) | 0.002858 (2.079×10−62.079\times 10^{-6}) |
| p=0.900p=0.900 | 1.039934 (3.940×10−63.940\times 10^{-6}) | 1.040429 (2.463×10−62.463\times 10^{-6}) | 0.002921 (3.940×10−63.940\times 10^{-6}) |
| p=0.925p=0.925 | 1.039856 (6.023×10−66.023\times 10^{-6}) | 1.040428 (1.509×10−61.509\times 10^{-6}) | 0.002999 (6.023×10−66.023\times 10^{-6}) |
| p=0.950p=0.950 | 1.040296 (0.001181) | 1242.01 (4665.02) | 0.002560 (0.001176) |
| p=0.975p=0.975 | 1.107629 (0.372054) | 1.040431 (2.081×10−52.081\times 10^{-5}) | 0.034428 (0.208918) |
| p=0.990p=0.990 | 3.289461 (6.477553) | 671.27 (2688.12) | 1.927083 (6.251131) |

Table 2: Pool with two losses of different heavy-tailedness X1∼Fr​e´​chet​(8.5,100)X\_{1}\sim\mathrm{Fr\acute{e}chet}(8.5,100) and X2∼Fr​e´​chet​(9,100)X\_{2}\sim\mathrm{Fr\acute{e}chet}(9,100). Sample mean and standard error are reported.

As mentioned above, an auxiliary comparison between optimization algorithms is performed to select the best candidate for these two studies (see Appendix [B](https://arxiv.org/html/2512.18790v1#A2 "Appendix B Comparison of algorithms for simulation study ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") for further details). In the experiments within this comparison, we use a smaller set of 20 samples with parameters from the second study of risks of different indices, and set ξ=0.31/8.5\xi=0.3^{1/8.5} and p=0.95p=0.95. On average, it takes 3.74 hours to obtain each 𝝀^​(p)\boldsymbol{\widehat{\lambda}}(p) corresponding to each of the 20 samples using the GSA algorithm444These experiments were carried out using the group of servers “biglinux.math” of University of Waterloo. More details on the computing power of these servers can be found at: <https://uwaterloo.ca/math-faculty-computing-facility/services/service-catalogue-research-linux/research-linux-server-hardware#biglinux> . Therefore, by using parallel computing, we can say that each line in Tables [1](https://arxiv.org/html/2512.18790v1#S3.T1 "Table 1 ‣ 3 Simulation study ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") and [2](https://arxiv.org/html/2512.18790v1#S3.T2 "Table 2 ‣ 3 Simulation study ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") (which employs 50 samples) requires between 3.74 and 187 hours depending on the available computing power. As such, it is clear that the explicit expression of the approximation proposed in this paper provides a much needed reduction in computational cost when solving the practical problem ([2.12](https://arxiv.org/html/2512.18790v1#S2.E12 "In 2.4 Asymptotic optimal pool ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")). We also observe next that the approximation 𝝀∗\boldsymbol{\lambda}^{\ast} has a high level of accuracy in comparison to 𝝀^​(p)\widehat{\boldsymbol{\lambda}}(p) provided by the algorithm.

From Tables [1](https://arxiv.org/html/2512.18790v1#S3.T1 "Table 1 ‣ 3 Simulation study ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") and [2](https://arxiv.org/html/2512.18790v1#S3.T2 "Table 2 ‣ 3 Simulation study ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."), we have some observations which are similar for both studies. The lower bounds of 𝝀∗\boldsymbol{\lambda}^{\ast} generally provide a good approximation to 𝝀^​(p)\widehat{\boldsymbol{\lambda}}(p) when pp is between 0.8 and 0.95, especially for losses with a lower scale or a lighter tail (X2X\_{2} in both studies). As such, in practical implementations, one could use λi=ξ−α1/αi\lambda\_{i}=\xi^{-\alpha\_{1}/\alpha\_{i}} for i=1,…,ni=1,...,n and would have a good approximation to the optimal pool.

However, we notice that as pp gets closer to 1, 𝝀^​(p)\widehat{\boldsymbol{\lambda}}(p) no longer represents a reliable solution to the practical problem ([2.12](https://arxiv.org/html/2512.18790v1#S2.E12 "In 2.4 Asymptotic optimal pool ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) due to its large variations. This can be explained by the fact that a higher level pp lowers the number of observations used for estimations, thus leading to a higher level of uncertainty, which is evident in the magnitudes of the standard deviations of λ^1​(p)\widehat{\lambda}\_{1}(p), λ^2​(p)\widehat{\lambda}\_{2}(p) and Π​(p)\Pi(p). This effect is further amplified by a larger value of ξ\xi for the same reason. As such, these two effects potentially contribute to the poorer performance of the approximation when pp is close to 1.

## 4 Empirical analysis

In this section, we examine the application of the theoretical framework by using flood loss data from the U.S. National Flood Insurance Program (NFIP). Created in 1968, this program aims at sharing the losses from flood damages with homeowners and to limit flood damages by reducing development in floodplains. NFIP is managed and administered by the Federal Emergency Management Agency (FEMA)555These data are available from: <https://www.fema.gov/openfema-data-page/fima-nfip-redacted-claims-v2>. It includes multiple details on each claim since 1978: date, damage amounts, payment amounts, characteristics of the building, details on the location, information on the coverage in the insurance policy, etc.. We use the damage amounts, which are aggregated from the building damage (buildingDamageAmount) and contents damage (contentsDamageAmount) for each state and each month from 1978 to 2023. Hence, each state has a total of 552 observations.

In this study, we consider three states: New York (NY), California (CA), Florida (FL). We first conduct some preliminary data analysis, and the details of each statistical test are provided in Appendix [C](https://arxiv.org/html/2512.18790v1#A3 "Appendix C Exploratory analysis of the NFIP data ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."). The main results of this analysis are summarized here in the main text. Using the test proposed in dietrich2002testing, we find that there is statistically significant evidence that NY, CA, FL have regularly varying tail distributions. This result confirms the assertion that the three losses satisfy the assumption of having regularly varying tails in Model 1 and Model 2. Using Pearson correlation tests, we also find that there is statistically significant evidence of pairwise linear independence between the three losses. However, the Spearman correlation test shows a significant monotonic relation between NY and FL, meaning that these three losses may not be strictly independent. Nonetheless, the following empirical studies show that our results still hold, indicating that the independence assumption among the losses may be relaxed in our theorems.

Moreover, we apply the tail equivalence test proposed in daouia2024optimal and show the pp-values of the tests calculated at different values of kk in Figure [2](https://arxiv.org/html/2512.18790v1#S4.F2 "Figure 2 ‣ 4 Empirical analysis ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."). FL and CA show strong evidence of having the same tail index, while NY and CA can be considered either tail equivalent or not depending on the particular choice of kk.

![Refer to caption](same_tail_FLCA.png)


(a) FL and CA

![Refer to caption](same_tail_NYCA.png)


(b) NY and CA

Figure 2: Results of equivalent tail tests. The pp-value is computed based on kk largest observations of X1X\_{1} and kk largest observations of X2X\_{2}. The null hypothesis is that X1X\_{1} and X2X\_{2} have equivalent tails. The dashed line indicates a pp-value of 0.05.

Based on the above analysis, we study the following three pools of losses.
Pool 1 consists of the losses from FL (X1X\_{1}) and CA (X2X\_{2}), which
satisfy the assumptions in Model 1. Pool 2 consists of the losses from CA
(X1X\_{1}) and NY (X2X\_{2}), which satisfy the assumptions in Model 2. Pool 3
consists of all three losses, FL (X1X\_{1}), CA (X2X\_{2}), and NY (X3X\_{3}),
which satisfy the assumptions in Model 2. In each pool, let X1,i,X2,i,…,Xm,iX\_{1,i},X\_{2,i},...,X\_{m,i} be the mm (=552)(=552) observations for loss XiX\_{i}. We
use the following steps to calculate the DR for each participant.

First we determine the tail index of each loss. In Pool 1, since the losses
are considered to be tail equivalent, we use the pooled tail estimator defined
as ([C.1](https://arxiv.org/html/2512.18790v1#A3.E1 "In Appendix C Exploratory analysis of the NFIP data ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) in Appendix [C](https://arxiv.org/html/2512.18790v1#A3 "Appendix C Exploratory analysis of the NFIP data ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."),
α^F​L−C​A\widehat{\alpha}\_{FL-CA}, which was proposed in daouia2024optimal. In
Pool 2 and Pool 3, since the losses are considered to have different tail
indices, we estimate the tail index with the Hill’s estimator for each loss
separately. The Hill’s estimator (hill1975) for a sample X1,…,XmX\_{1},...,X\_{m}
is defined as

|  |  |  |
| --- | --- | --- |
|  | α^=(1k​∑j=1klog⁡X(m−j+1)−log⁡X(m−k))−1.\widehat{\alpha}=\left(\frac{1}{k}\sum\_{j=1}^{k}\log X\_{(m-j+1)}-\log X\_{(m-k)}\right)^{-1}. |  |

The plots for each estimator with varying kk are shown in Figure
[3](https://arxiv.org/html/2512.18790v1#S4.F3 "Figure 3 ‣ 4 Empirical analysis ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."). From these plots, we set kk to be 5555, which is the
10% of the entire data points for each loss. Then we obtain: (i) for Pool 1,
α^F​L−C​A=α^1=α^2=0.604\widehat{\alpha}\_{FL-CA}=\widehat{\alpha}\_{1}=\widehat{\alpha}\_{2}=0.604, (ii) for Pool 2, α^C​A=α^1=0.646\widehat{\alpha}\_{CA}=\widehat{\alpha}\_{1}=0.646 and
α^N​Y=α^2=0.719\widehat{\alpha}\_{NY}=\widehat{\alpha}\_{2}=0.719, and (iii) for Pool 3, α^F​L=α^1=0.555\widehat{\alpha}\_{FL}=\widehat{\alpha}\_{1}=0.555, α^C​A=α^2=0.646\widehat{\alpha}\_{CA}=\widehat{\alpha}\_{2}=0.646 and α^N​Y=α^3=0.719\widehat{\alpha}\_{NY}=\widehat{\alpha}\_{3}=0.719. We can see that all of these losses are extremely heavy-tailed
with an infinite first moment.

![Refer to caption](Hill_FL_CA_same.png)


(a) Pooled α^F​L−C​A\widehat{\alpha}\_{FL-CA}

![Refer to caption](Hill_NY.png)


(b) α^N​Y\widehat{\alpha}\_{NY}

![Refer to caption](Hill_CA.png)


(c) α^C​A\widehat{\alpha}\_{CA}

![Refer to caption](Hill_FL.png)


(d) α^F​L\widehat{\alpha}\_{FL}

Figure 3: Plots of Hill’s estimator for each loss

Next for losses in Pool 1, which are considered to be tail equivalent, we also
need to estimate the scale parameter θC​A\theta\_{CA} for CA as defined in
([2.5](https://arxiv.org/html/2512.18790v1#S2.E5 "In 1st item ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")). Note that by definition θF​L\theta\_{FL} in Pool 1 is 1. We propose
the following empirical estimator for θC​A\theta\_{CA}

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ^C​A=F¯^C​A​(X(m−h),F​L)F¯^F​L​(X(m−h),F​L)=∑j=1m1{Xj,C​A≥X(m−h),F​L}∑j=1m1{Xj,F​L≥X(m−h),F​L},\widehat{\theta}\_{CA}=\frac{\widehat{\overline{F}}\_{CA}(X\_{(m-h),FL})}{\widehat{\overline{F}}\_{FL}(X\_{(m-h),FL})}=\frac{\sum\_{j=1}^{m}1\_{\left\{X\_{j,CA}\geq X\_{(m-h),FL}\right\}}}{\sum\_{j=1}^{m}1\_{\left\{X\_{j,FL}\geq X\_{(m-h),FL}\right\}}}, |  | (4.1) |

where m=552m=552. By varying hh, we plot the values of θ^C​A\widehat{\theta}\_{CA}
in Figure [4](https://arxiv.org/html/2512.18790v1#S4.F4 "Figure 4 ‣ 4 Empirical analysis ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."). Then by taking h=55h=55, which is the 10% of the entire data
points, θ^C​A\widehat{\theta}\_{CA} is calculated as 0.36370.3637.

![Refer to caption](theta_FL_CA.png)


Figure 4: Plot of θ^C​A\widehat{\theta}\_{CA} with varying hh

Now we are ready to compute the DR for each participant in a pool. We apply
the following estimator for DRi​(p)\mathrm{DR}\_{i}(p)

|  |  |  |
| --- | --- | --- |
|  | DR^i​(p)=VaR^p​(Xi−Yi)VaR^p​(Xi)+E​[Yi]^∑i=1nE​[Yi]^​S(⌊p​m⌋)X(⌊p​m⌋),i,\widehat{\mathrm{DR}}\_{i}(p)=\frac{\widehat{\mathrm{VaR}}\_{p}(X\_{i}-Y\_{i})}{\widehat{\mathrm{VaR}}\_{p}(X\_{i})}+\frac{\widehat{E[Y\_{i}]}}{\sum\_{i=1}^{n}\widehat{E[Y\_{i}]}}\frac{S\_{(\lfloor pm\rfloor)}}{X\_{(\lfloor pm\rfloor),i}}, |  |

with each term being calculated as follows. First, to make the estimation more stable for high
levels of pp, we adopt the following EVT-based quantile estimator for
VaRp​(Xi)\mathrm{VaR}\_{p}(X\_{i}) with p>0.8p>0.8

|  |  |  |
| --- | --- | --- |
|  | VaR^p​(Xi)=X(⌊0.8​m⌋),i​(0.21−p)1/α^i,\widehat{\mathrm{VaR}}\_{p}(X\_{i})=X\_{(\lfloor 0.8m\rfloor),i}\left(\frac{0.2}{1-p}\right)^{1/\widehat{\alpha}\_{i}}, |  |

where m=552m=552. This means that to
estimate VaRp​(Xi)\mathrm{VaR}\_{p}(X\_{i}) at a confidence level p>0.8p>0.8 close to 1,
we extrapolate the empirical estimator of VaR0.8​(Xi)\mathrm{VaR}\_{0.8}(X\_{i}),
X(⌊0.8​m⌋),iX\_{(\lfloor 0.8m\rfloor),i}, to the level pp (for details of this estimator
see for example Theorem 4.3.8 of haan2006extreme). Then, following the assumptions in
Model 1 and 2, we set the levels of the attachment points in each pool as
di=ξα^1/α^i​VaR^p​(Xi)d\_{i}=\xi^{\widehat{\alpha}\_{1}/\widehat{\alpha}\_{i}}\widehat{\mathrm{VaR}}\_{p}(X\_{i}) for i=1,2,3i=1,2,3, where ξ\xi is
chosen to be of certain values, and the limits in each pool as li=λi​dil\_{i}=\lambda\_{i}d\_{i}, where λi=ξ−α^1/α^i\lambda\_{i}=\xi^{-\widehat{\alpha}\_{1}/\widehat{\alpha}\_{i}} are the lower bounds of 𝝀∗\boldsymbol{\lambda}^{\ast} from Theorem [2.3](https://arxiv.org/html/2512.18790v1#S2.Thmtheorem3 "Theorem 2.3 ‣ 2.4 Asymptotic optimal pool ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."). This is based on the observation in the previous section that the lower bounds provide the most accurate approximation to the solution of the practical optimization problem. Then, for each loss
observation Xj,iX\_{j,i}, the layer loss Yj,iY\_{j,i} is calculated according to
([2.1](https://arxiv.org/html/2512.18790v1#S2.E1 "In 2.1 Pool setup ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")). Let Rj,i=Xj,i−Yj,iR\_{j,i}=X\_{j,i}-Y\_{j,i}. Thus we have

|  |  |  |
| --- | --- | --- |
|  | VaR^p​(Xi−Yi)=R(⌊p​m⌋),i.\widehat{\mathrm{VaR}}\_{p}(X\_{i}-Y\_{i})=R\_{(\lfloor pm\rfloor),i}. |  |

and

|  |  |  |
| --- | --- | --- |
|  | E​[Yi]^=1m​∑j=1mYj,i.\widehat{E[Y\_{i}]}=\frac{1}{m}{\displaystyle\sum\limits\_{j=1}^{m}}Y\_{j,i}. |  |

Lastly, the aggregated loss in the pool is Sj=∑i=1nYj,iS\_{j}={\displaystyle\sum\limits\_{i=1}^{n}}Y\_{j,i}, where n=2n=2 or 33.

![Refer to caption](kxi0.1_FL_CA_mid.png)


(a) ξ=0.11/α^F​L−C​A\xi=0.1^{1/\widehat{\alpha}\_{FL-CA}}

![Refer to caption](kxi0.3_FL_CA_mid.png)


(b) ξ=0.31/α^F​L−C​A\xi=0.3^{1/\widehat{\alpha}\_{FL-CA}}

![Refer to caption](kxi0.5_FL_CA_mid.png)


(c) ξ=0.51/α^F​L−C​A\xi=0.5^{1/\widehat{\alpha}\_{FL-CA}}

![Refer to caption](kxi0.7_FL_CA_mid.png)


(d) ξ=0.71/α^F​L−C​A\xi=0.7^{1/\widehat{\alpha}\_{FL-CA}}

Figure 5: DRi​(p)\mathrm{DR}\_{i}(p) in pool 1 for selected values of ξ\xi

Figure [5](https://arxiv.org/html/2512.18790v1#S4.F5 "Figure 5 ‣ 4 Empirical analysis ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") shows DRi​(p)\mathrm{DR}\_{i}(p) for each participant
in Pool 1 (FL and CA) for pp ranging from 0.8 to 0.975 at a stepsize of 0.001, where ξ\xi is set as 0.11/α^1,0.1^{1/\widehat{\alpha}\_{1}},
0.31/α^1,0.3^{1/\widehat{\alpha}\_{1}}, 0.51/α^1,0.5^{1/\widehat{\alpha}\_{1}}, or
0.71/α^10.7^{1/\widehat{\alpha}\_{1}}. We observe that, in all scenarios, DRi​(p)\mathrm{DR}\_{i}(p) is generally smaller
than 1 for both FL and CA, which means that all participants in the pool obtain a
diversification benefit from joining the pool. For smaller values of ξ\xi,
DRi​(p)\mathrm{DR}\_{i}(p) of FL and CA are smaller as well. This means that a higher
diversification benefit is achieved when the lower layer loss is brought to
the pool, which is consistent with our insight from Theorem [2.3](https://arxiv.org/html/2512.18790v1#S2.Thmtheorem3 "Theorem 2.3 ‣ 2.4 Asymptotic optimal pool ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.").
Furthermore, we notice that FL generally obtains a smaller DR1​(p)\mathrm{DR}\_{1}(p) than that of CA, which means that FL obtains more diversification benefit
than CA. As θ^C​A<1\widehat{\theta}\_{CA}<1, this implies that a participant int he pool with a larger loss enjoys a greater diversification benefit from the pool.

![Refer to caption](kxi0.1_NY_CA_mid2.png)


(a) ξ=0.11/α^C​A\xi=0.1^{1/\widehat{\alpha}\_{CA}}

![Refer to caption](kxi0.3_NY_CA_mid2.png)


(b) ξ=0.31/α^C​A\xi=0.3^{1/\widehat{\alpha}\_{CA}}

![Refer to caption](kxi0.5_NY_CA_mid2.png)


(c) ξ=0.51/α^C​A\xi=0.5^{1/\widehat{\alpha}\_{CA}}

![Refer to caption](kxi0.7_NY_CA_mid2.png)


(d) ξ=0.71/α^C​A\xi=0.7^{1/\widehat{\alpha}\_{CA}}

Figure 6: DRi​(p)\mathrm{DR}\_{i}(p) in Pool 2 for selected values of ξ\xi

Figure [6](https://arxiv.org/html/2512.18790v1#S4.F6 "Figure 6 ‣ 4 Empirical analysis ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") shows DRi​(p)\mathrm{DR}\_{i}(p) for each participant
in Pool 2 (CA and NY) for pp ranging from 0.8 to 0.975 at a stepsize of 0.001, where ξ\xi is set as 0.11/α^1,0.1^{1/\widehat{\alpha}\_{1}},
0.31/α^1,0.3^{1/\widehat{\alpha}\_{1}}, 0.51/α^1,0.5^{1/\widehat{\alpha}\_{1}}, or
0.71/α^10.7^{1/\widehat{\alpha}\_{1}}. Similarly to Pool 1, in all scenarios,
DRi​(p)\mathrm{DR}\_{i}(p) is generally smaller than 1 for both CA and NY, and that
they are able to reach smaller values when ξ\xi is lower.

![Refer to caption](kxi0.1_NYCAFL.png)


(a) ξ=0.11/α^F​L\xi=0.1^{1/\widehat{\alpha}\_{FL}}

![Refer to caption](kxi0.3_NYCAFL.png)


(b) ξ=0.31/α^F​L\xi=0.3^{1/\widehat{\alpha}\_{FL}}

![Refer to caption](kxi0.5_NYCAFL.png)


(c) ξ=0.51/α^F​L\xi=0.5^{1/\widehat{\alpha}\_{FL}}

![Refer to caption](kxi0.7_NYCAFL.png)


(d) ξ=0.71/α^F​L\xi=0.7^{1/\widehat{\alpha}\_{FL}}

Figure 7: DRi​(p)\mathrm{DR}\_{i}(p) in Pool 3 for selected values of ξ\xi

Finally, Figure [7](https://arxiv.org/html/2512.18790v1#S4.F7 "Figure 7 ‣ 4 Empirical analysis ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") shows DRi​(p)\mathrm{DR}\_{i}(p) for pp ranging from 0.8 to 0.975 at a stepsize of 0.001, where ξ\xi is set as 0.11/α^1,0.1^{1/\widehat{\alpha}\_{1}},
0.31/α^1,0.3^{1/\widehat{\alpha}\_{1}}, 0.51/α^1,0.5^{1/\widehat{\alpha}\_{1}}, or
0.71/α^10.7^{1/\widehat{\alpha}\_{1}}. Similarly to Pool 1 and Pool 2, in all
scenarios DRi​(p)\mathrm{DR}\_{i}(p) is generally smaller than 1 and that they are
smaller and more different from each other when ξ\xi is closer to 0.

## 5 Conclusion

In this paper, we investigate how to efficiently allocate the diversification
benefit among participants in a catastrophe risk pool. By joining the pool,
each participant is covered for a layer of their loss, determined by an attachment
point and a limit. To receive this coverage, the pool participant pays a premium
proportional to the aggregated loss of the pool. The diversification benefit
is measured using a so-called diversification ratio based on the VaR measure, which
compares the participant’s risk before and after joining the pool. Achieving a
Pareto-optimal allocation of diversification benefit at a given level pp of the VaR measure requires solving a high-dimensional optimization problem, for
which an analytical solution is generally unavailable, while numerical
solutions can be time-consuming and potentially unreliable. In this paper, we propose using
the asymptotic optimal pool, which is a Pareto-optimal pool when the
diversification ratio is evaluated at the limit, to
approximate the practical optimal pool at any finite level pp close to 1. This result relies on the assumptions that the ground-up losses of participants in the pool are independent and heavy-tailed, possibly with different scales and tail indices. Furthermore, it emerges from our results that the asymptotic optimal pool, in addition to being a Pareto-optimality, allows all participants in the pool to attain their individual maximum diversification benefit. Through simulation and empirical studies, we show that the asymptotic optimal
pool provides an accurate and reliable approximation to the practical optimal
pool, and that its implementation is relatively straightforward.

\appendixpage

## Appendix A Proofs of analytical results

### A.1 Proofs of results under Model 1

Proof of Lemma [2.1](https://arxiv.org/html/2512.18790v1#S2.Thmlemma1 "Lemma 2.1 ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.").

By ([2.5](https://arxiv.org/html/2512.18790v1#S2.E5 "In 1st item ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) and Potter’s bounds (see Proposition B.1.9(5) of haan2006extreme for example), we have

|  |  |  |
| --- | --- | --- |
|  | 1=limp→1F¯i​(VaRp​(Xi))F¯1​(VaRp​(X1))=limp→1F¯i​(VaRp​(Xi))F¯1​(VaRp​(Xi))​F¯1​(VaRp​(Xi))F¯1​(VaRp​(X1))=limp→1θi​(VaRp​(Xi)VaRp​(X1))−α.1=\lim\_{p\rightarrow 1}\frac{\overline{F}\_{i}\left(\mathrm{VaR}\_{p}(X\_{i})\right)}{\overline{F}\_{1}\left(\mathrm{VaR}\_{p}(X\_{1})\right)}=\lim\_{p\rightarrow 1}\frac{\overline{F}\_{i}\left(\mathrm{VaR}\_{p}(X\_{i})\right)}{\overline{F}\_{1}\left(\mathrm{VaR}\_{p}(X\_{i})\right)}\frac{\overline{F}\_{1}\left(\mathrm{VaR}\_{p}(X\_{i})\right)}{\overline{F}\_{1}\left(\mathrm{VaR}\_{p}(X\_{1})\right)}=\lim\_{p\rightarrow 1}\theta\_{i}\left(\frac{\mathrm{VaR}\_{p}(X\_{i})}{\mathrm{VaR}\_{p}(X\_{1})}\right)^{-\alpha}. |  |

This leads to the following result

|  |  |  |
| --- | --- | --- |
|  | limp→1VaRp​(Xi)VaRp​(X1)=θi1/α.\lim\_{p\rightarrow 1}\frac{\mathrm{VaR}\_{p}(X\_{i})}{\mathrm{VaR}\_{p}(X\_{1})}=\theta\_{i}^{1/\alpha}. |  |

Then under assumption ([2.6](https://arxiv.org/html/2512.18790v1#S2.E6 "In 2nd item ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")), we have

|  |  |  |
| --- | --- | --- |
|  | limp→1di​(p)d1​(p)=limp→1di​(p)VaRp​(Xi)​VaRp​(X1)d1​(p)​VaRp​(Xi)VaRp​(X1)=θi1/α.\lim\_{p\rightarrow 1}\frac{d\_{i}(p)}{d\_{1}(p)}=\lim\_{p\rightarrow 1}\frac{d\_{i}(p)}{\mathrm{VaR}\_{p}(X\_{i})}\frac{\mathrm{VaR}\_{p}(X\_{1})}{d\_{1}(p)}\frac{\mathrm{VaR}\_{p}(X\_{i})}{\mathrm{VaR}\_{p}(X\_{1})}=\theta\_{i}^{1/\alpha}. |  |

Similarly, by Potter’s bounds, we have

|  |  |  |
| --- | --- | --- |
|  | limp→1F¯i​(di)F¯1​(d1)=limp→1F¯i​(di)F¯1​(di)​F¯1​(di)F¯1​(d1)=limp→1θi​(di​(p)d1​(p))−α=1.\lim\_{p\rightarrow 1}\frac{\overline{F}\_{i}(d\_{i})}{\overline{F}\_{1}(d\_{1})}=\lim\_{p\rightarrow 1}\frac{\overline{F}\_{i}(d\_{i})}{\overline{F}\_{1}(d\_{i})}\frac{\overline{F}\_{1}(d\_{i})}{\overline{F}\_{1}(d\_{1})}=\lim\_{p\rightarrow 1}\theta\_{i}\left(\frac{d\_{i}(p)}{d\_{1}(p)}\right)^{-\alpha}=1. |  |

Lastly, we have

|  |  |  |
| --- | --- | --- |
|  | limp→1di​(p)VaRp​(X1)=limp→1di​(p)VaRp​(Xi)​VaRp​(Xi)VaRp​(X1)=θi1/α​ξ\lim\_{p\rightarrow 1}\frac{d\_{i}(p)}{\mathrm{VaR}\_{p}(X\_{1})}=\lim\_{p\rightarrow 1}\frac{d\_{i}(p)}{\mathrm{VaR}\_{p}(X\_{i})}\frac{\mathrm{VaR}\_{p}(X\_{i})}{\mathrm{VaR}\_{p}(X\_{1})}=\theta\_{i}^{1/\alpha}\xi |  |

and

|  |  |  |
| --- | --- | --- |
|  | limp→1li​(p)VaRp​(X1)=limp→1li​(p)di​(p)​di​(p)VaRp​(X1)=λi​θi1/α​ξ.\lim\_{p\rightarrow 1}\frac{l\_{i}(p)}{\mathrm{VaR}\_{p}(X\_{1})}=\lim\_{p\rightarrow 1}\frac{l\_{i}(p)}{d\_{i}(p)}\frac{d\_{i}(p)}{\mathrm{VaR}\_{p}(X\_{1})}=\lambda\_{i}\theta\_{i}^{1/\alpha}\xi. |  |

by assumption ([2.6](https://arxiv.org/html/2512.18790v1#S2.E6 "In 2nd item ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")). This completes the proof.

 

Proof of Theorem [2.1](https://arxiv.org/html/2512.18790v1#S2.Thmtheorem1 "Theorem 2.1 ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.").

Consider the split

|  |  |  |  |
| --- | --- | --- | --- |
|  | DRi​(p)\displaystyle\mathrm{DR}\_{i}(p) | =VaRp​(Xi−Yi)VaRp​(Xi)+E​[Yi]E​[Sn]⋅VaRp​(Sn)VaRp​(Xi)\displaystyle=\frac{\mathrm{VaR}\_{p}(X\_{i}-Y\_{i})}{\mathrm{VaR}\_{p}(X\_{i})}+\frac{E\left[Y\_{i}\right]}{E\left[S\_{n}\right]}\cdot\frac{\mathrm{VaR}\_{p}(S\_{n})}{\mathrm{VaR}\_{p}(X\_{i})} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | :=I1+I2⋅I3.\displaystyle:=I\_{1}+I\_{2}\cdot I\_{3}. |  | (A.1) |

Next we analyze each term separately.

First we consider I1I\_{1}. For any 0<p<10<p<1, we have

|  |  |  |
| --- | --- | --- |
|  | I1={1,p≤Fi​(di),diVaRp​(Xi),Fi​(di)<p≤Fi​(li),1−li−diVaRp​(Xi),p>Fi​(li).I\_{1}=\left\{\begin{array}[c]{lll}1,&&p\leq F\_{i}(d\_{i}),\\ \frac{d\_{i}}{\mathrm{VaR}\_{p}(X\_{i})},&&F\_{i}(d\_{i})<p\leq F\_{i}(l\_{i}),\\ 1-\frac{l\_{i}-d\_{i}}{\mathrm{VaR}\_{p}(X\_{i})},&&p>F\_{i}(l\_{i}).\end{array}\right. |  |

This leads to the following expression

|  |  |  |
| --- | --- | --- |
|  | limp→1I1={1,ξ≥1,ξ,1/λi≤ξ<1,1−(λi−1)​ξ,ξ<1/λi.\lim\_{p\rightarrow 1}I\_{1}=\left\{\begin{array}[c]{lll}1,&&\xi\geq 1,\\ \xi,&&1/\lambda\_{i}\leq\xi<1,\\ 1-(\lambda\_{i}-1)\xi,&&\xi<1/\lambda\_{i}.\end{array}\right. |  |

Now we turn to I2I\_{2}. Note that

|  |  |  |
| --- | --- | --- |
|  | E​[Yi]=∫diliF¯i​(x)​𝑑x=di​∫1li/diF¯i​(di​x)​𝑑x.E[Y\_{i}]=\int\_{d\_{i}}^{l\_{i}}\overline{F}\_{i}(x)dx=d\_{i}\int\_{1}^{l\_{i}/d\_{i}}\overline{F}\_{i}\left(d\_{i}x\right)dx. |  |

By Potter’s bounds (see Proposition B.1.9(5) of haan2006extreme for example) and assumption ([2.6](https://arxiv.org/html/2512.18790v1#S2.E6 "In 2nd item ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")),
for any ε,δ>0\varepsilon,\delta>0, there exists p0>0p\_{0}>0 and d0>0d\_{0}>0, such
that for p0<p<1p\_{0}<p<1, we have di​(p)>d0d\_{i}(p)>d\_{0}, li​(p)/di​(p)<λi+εl\_{i}(p)/d\_{i}(p)<\lambda\_{i}+\varepsilon and

|  |  |  |
| --- | --- | --- |
|  | F¯i​(di​x)F¯i​(di)≤(1+ε)​x−α+δ\frac{\overline{F}\_{i}\left(d\_{i}x\right)}{\overline{F}\_{i}\left(d\_{i}\right)}\leq(1+\varepsilon)x^{-\alpha+\delta} |  |

for all x>1x>1. Then for p0<p<1p\_{0}<p<1, we have

|  |  |  |
| --- | --- | --- |
|  | E​[Yi]di​F¯i​(di)≤∫1λi+ε(1+ε)​x−α+δ​𝑑x<∞\frac{E[Y\_{i}]}{d\_{i}\overline{F}\_{i}\left(d\_{i}\right)}\leq\int\_{1}^{\lambda\_{i}+\varepsilon}(1+\varepsilon)x^{-\alpha+\delta}dx<\infty |  |

for all α>0\alpha>0. Adhering to the Lebesgue dominated convergence theorem gives us

|  |  |  |  |
| --- | --- | --- | --- |
|  | limp→1E​[Yi]di​F¯i​(di)=∫1λix−α​𝑑x=λi1−α−11−α.\lim\_{p\rightarrow 1}\frac{E[Y\_{i}]}{d\_{i}\overline{F}\_{i}\left(d\_{i}\right)}=\int\_{1}^{\lambda\_{i}}x^{-\alpha}dx=\frac{\lambda\_{i}^{1-\alpha}-1}{1-\alpha}. |  | (A.2) |

If α=1\alpha=1, the right-hand side of ([A.2](https://arxiv.org/html/2512.18790v1#A1.E2 "In A.1 Proofs of results under Model 1 ‣ Appendix A Proofs of analytical results ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) is understood to be
ln⁡λi\ln\lambda\_{i}. Then, by ([2.8](https://arxiv.org/html/2512.18790v1#S2.E8 "In Lemma 2.1 ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")), we have

|  |  |  |
| --- | --- | --- |
|  | limp→1E​[Yi]d1​F¯1​(d1)=limp→1E​[Yi]di​F¯i​(di)​di​F¯i​(di)d1​F¯1​(d1)=(λi1−α−1)​θi1/α1−α.\lim\_{p\rightarrow 1}\frac{E[Y\_{i}]}{d\_{1}\overline{F}\_{1}\left(d\_{1}\right)}=\lim\_{p\rightarrow 1}\frac{E[Y\_{i}]}{d\_{i}\overline{F}\_{i}\left(d\_{i}\right)}\frac{d\_{i}\overline{F}\_{i}\left(d\_{i}\right)}{d\_{1}\overline{F}\_{1}\left(d\_{1}\right)}=\frac{\left(\lambda\_{i}^{1-\alpha}-1\right)\theta\_{i}^{1/\alpha}}{1-\alpha}. |  |

Moreover, we also have

|  |  |  |
| --- | --- | --- |
|  | limp→1E​[Sn]d1​F¯1​(d1)=limp→1∑j=1nE​[Yj]d1​F¯1​(d1)=∑j=1n(λj1−α−1)​θj1/α1−α.\lim\_{p\rightarrow 1}\frac{E\left[S\_{n}\right]}{d\_{1}\overline{F}\_{1}\left(d\_{1}\right)}=\lim\_{p\rightarrow 1}\sum\_{j=1}^{n}\frac{E[Y\_{j}]}{d\_{1}\overline{F}\_{1}\left(d\_{1}\right)}=\sum\_{j=1}^{n}\frac{\left(\lambda\_{j}^{1-\alpha}-1\right)\theta\_{j}^{1/\alpha}}{1-\alpha}. |  |

It follows that

|  |  |  |
| --- | --- | --- |
|  | limp→1I2=(λi1−α−1)​θi1/α∑j=1n(λj1−α−1)​θj1/α.\lim\_{p\rightarrow 1}I\_{2}=\frac{\left(\lambda\_{i}^{1-\alpha}-1\right)\theta\_{i}^{1/\alpha}}{\sum\_{j=1}^{n}\left(\lambda\_{j}^{1-\alpha}-1\right)\theta\_{j}^{1/\alpha}}. |  |

Lastly, we consider I3I\_{3}. To analyze VaRp​(Sn)\mathrm{VaR}\_{p}(S\_{n}), we start
with ℙ​(Sn>t)\mathbb{P}(S\_{n}>t) and compare it with F¯1​(t)\overline{F}\_{1}(t), where t=VaRp​(X1)t=\mathrm{VaR}\_{p}(X\_{1}). Then p→1p\rightarrow 1 can be replaced by t→∞t\rightarrow\infty. Denote J={1,….n}J=\{1,....n\} and 𝕁={(J1,J2,J3):J1∪J2∪J3=J\mathbb{J}=\{\left(J\_{1},J\_{2},J\_{3}\right):J\_{1}\cup J\_{2}\cup J\_{3}=J and
J1,J2,J3J\_{1},J\_{2},J\_{3} mutually exclusive}\}. Note that at most two of J1J\_{1},
J2J\_{2} and J3J\_{3} can be empty sets. Let 𝕁1={Xi≤di:i∈J1}\mathbb{J}\_{1}=\left\{X\_{i}\leq d\_{i}:i\in J\_{1}\right\}, 𝕁2={di<Xi≤li:i∈J2}\mathbb{J}\_{2}=\left\{d\_{i}<X\_{i}\leq l\_{i}:i\in J\_{2}\right\} and 𝕁3={Xi>li:i∈J3}\mathbb{J}\_{3}=\left\{X\_{i}>l\_{i}:i\in J\_{3}\right\}. Then we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(Sn>t)\displaystyle\mathbb{P}(S\_{n}>t) | =∑(J1,J2,J3)∈𝕁​ℙ​(∑i∈J1​Yi+∑j∈J2​Yj+∑k∈J3​Yk>t)\displaystyle=\underset{\left(J\_{1},J\_{2},J\_{3}\right)\in\mathbb{J}}{\sum}\mathbb{P}\left(\underset{i\in J\_{1}}{\sum}Y\_{i}+\underset{j\in J\_{2}}{\sum}Y\_{j}+\underset{k\in J\_{3}}{\sum}Y\_{k}>t\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑(J1,J2,J3)∈𝕁​ℙ​(∑j∈J2​Xj>t+∑j∈J2​dj−∑k∈J3​(lk−dk),𝕁1∩𝕁2∩𝕁3)\displaystyle=\underset{\left(J\_{1},J\_{2},J\_{3}\right)\in\mathbb{J}}{\sum}\mathbb{P}\left(\underset{j\in J\_{2}}{\sum}X\_{j}>t+\underset{j\in J\_{2}}{\sum}d\_{j}-\underset{k\in J\_{3}}{\sum}(l\_{k}-d\_{k}),\mathbb{J}\_{1}\cap\mathbb{J}\_{2}\cap\mathbb{J}\_{3}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑(J1,J2,J3)∈𝕁​I.\displaystyle=\underset{\left(J\_{1},J\_{2},J\_{3}\right)\in\mathbb{J}}{\sum}I. |  |

Note that if J2=J3=∅J\_{2}=J\_{3}=\varnothing, then I=0I=0. Next, we show that if at
least one of J2J\_{2} and J3J\_{3} is not an empty set, then the cardinality of
J2∪J3J\_{2}\cup J\_{3} is at most 1 such that

|  |  |  |
| --- | --- | --- |
|  | limt→∞IF¯1​(t)≠0.\lim\_{t\rightarrow\infty}\frac{I}{\overline{F}\_{1}\left(t\right)}\not=0. |  |

It suffices to show the following cases for some 1≤i≠j≤n1\leq i\not=j\leq n and
ii or j∉J1j\not\in J\_{1}: (1) J2={i}J\_{2}=\{i\} and J3=∅J\_{3}=\varnothing; (2)
J2={i,j}J\_{2}=\{i,j\} and J3=∅J\_{3}=\varnothing; (3) J2=∅J\_{2}=\varnothing and
J3={i}J\_{3}=\{i\}; (4) J2=∅J\_{2}=\varnothing and J3={i,j}J\_{3}=\{i,j\}; (5) J2={i}J\_{2}=\{i\}
and J3={j}J\_{3}=\{j\}.

(1) In this case, since XiX\_{i}’s are independent, we obtain the following result

|  |  |  |
| --- | --- | --- |
|  | I=ℙ​(Xi>t+di,di<Xi≤li)​ℙ​(𝕁1).I=\mathbb{P}\left(X\_{i}>t+d\_{i},d\_{i}<X\_{i}\leq l\_{i}\right)\mathbb{P}\left(\mathbb{J}\_{1}\right). |  |

For t>li−dit>l\_{i}-d\_{i} which is equivalent to ξ<θi−1/α​(λi−1)−1\xi<\theta\_{i}^{-1/\alpha}\left(\lambda\_{i}-1\right)^{-1}, we have I=0I=0. For 0<t<li−di0<t<l\_{i}-d\_{i} which is
equivalent to ξ>θi−1/α​(λi−1)−1\xi>\theta\_{i}^{-1/\alpha}\left(\lambda\_{i}-1\right)^{-1},
since t=VaRp​(X1)t=\mathrm{VaR}\_{p}(X\_{1}), by Lemma [2.1](https://arxiv.org/html/2512.18790v1#S2.Thmlemma1 "Lemma 2.1 ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→∞IF¯1​(t)\displaystyle\lim\_{t\rightarrow\infty}\frac{I}{\overline{F}\_{1}\left(t\right)} | =limt→∞(F¯i​(t+di)F¯1​(t)−F¯i​(li)F¯1​(t))​∏k∈J1Fk​(dk)\displaystyle=\lim\_{t\rightarrow\infty}\left(\frac{\overline{F}\_{i}\left(t+d\_{i}\right)}{\overline{F}\_{1}\left(t\right)}-\frac{\overline{F}\_{i}\left(l\_{i}\right)}{\overline{F}\_{1}\left(t\right)}\right){\displaystyle\prod\limits\_{k\in J\_{1}}}F\_{k}(d\_{k}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =limt→∞(F¯i​(t+di)F¯i​(t)​F¯i​(t)F¯1​(t)−F¯i​(li)F¯i​(t)​F¯i​(t)F¯1​(t))​limt→∞∏k∈J1Fk​(dk)\displaystyle=\lim\_{t\rightarrow\infty}\left(\frac{\overline{F}\_{i}\left(t+d\_{i}\right)}{\overline{F}\_{i}\left(t\right)}\frac{\overline{F}\_{i}\left(t\right)}{\overline{F}\_{1}\left(t\right)}-\frac{\overline{F}\_{i}\left(l\_{i}\right)}{\overline{F}\_{i}\left(t\right)}\frac{\overline{F}\_{i}\left(t\right)}{\overline{F}\_{1}\left(t\right)}\right)\lim\_{t\rightarrow\infty}{\displaystyle\prod\limits\_{k\in J\_{1}}}F\_{k}(d\_{k}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(θi−1/α+ξ)−α−(ξ​λi)−α.\displaystyle=\left(\theta\_{i}^{-1/\alpha}+\xi\right)^{-\alpha}-\left(\xi\lambda\_{i}\right)^{-\alpha}. |  |

(2) In this case, since XiX\_{i}’s are independent, we obtain the following result

|  |  |  |  |
| --- | --- | --- | --- |
|  | I\displaystyle I | =ℙ(Xi+Xj>t+di+dj,di<Xi≤li,dj<Xj≤lj)ℙ(𝕁1)\displaystyle=\mathbb{P}\left(X\_{i}+X\_{j}>t+d\_{i}+d\_{j},d\_{i}<X\_{i}\leq l\_{i},d\_{j}<X\_{j}\leq l\_{j}\right)\mathbb{P}\left(\mathbb{J}\_{1}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙ(Xi+Xj>t+di+dj|di<Xi≤li,dj<Xj≤lj)ℙ(di<Xi≤li)ℙ(dj<Xj≤lj)ℙ(𝕁1).\displaystyle=\mathbb{P}\left(X\_{i}+X\_{j}>t+d\_{i}+d\_{j}\left|d\_{i}<X\_{i}\leq l\_{i},d\_{j}<X\_{j}\leq l\_{j}\right.\right)\mathbb{P}\left(d\_{i}<X\_{i}\leq l\_{i}\right)\mathbb{P}\left(d\_{j}<X\_{j}\leq l\_{j}\right)\mathbb{P}\left(\mathbb{J}\_{1}\right). |  |

Then, following the similar proof to that for case (1), we have

|  |  |  |
| --- | --- | --- |
|  | limt→∞ℙ​(di<Xi≤li)F¯1​(t)​ℙ​(dj<Xj≤lj)=0,\lim\_{t\rightarrow\infty}\frac{\mathbb{P}\left(d\_{i}<X\_{i}\leq l\_{i}\right)}{\overline{F}\_{1}\left(t\right)}\mathbb{P}\left(d\_{j}<X\_{j}\leq l\_{j}\right)=0, |  |

which leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→∞IF¯1​(t)=0.\lim\_{t\rightarrow\infty}\frac{I}{\overline{F}\_{1}\left(t\right)}=0. |  | (A.3) |

Thus, when the cardinality of J2J\_{2} is greater than 11, ([A.3](https://arxiv.org/html/2512.18790v1#A1.E3 "In A.1 Proofs of results under Model 1 ‣ Appendix A Proofs of analytical results ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) holds true.

(3) In this case, since XiX\_{i}’s are independent, we obtain the following result

|  |  |  |
| --- | --- | --- |
|  | I=ℙ​(li−di>t,Xi>li)​ℙ​(𝕁1).I=\mathbb{P}\left(l\_{i}-d\_{i}>t,X\_{i}>l\_{i}\right)\mathbb{P}\left(\mathbb{J}\_{1}\right). |  |

For t>li−dit>l\_{i}-d\_{i} which is equivalent to ξ<θi−1/α​(λi−1)−1\xi<\theta\_{i}^{-1/\alpha}\left(\lambda\_{i}-1\right)^{-1}, we have I=0I=0. For 0<t<li−di0<t<l\_{i}-d\_{i} which is
equivalent to ξ>θi−1/α​(λi−1)−1\xi>\theta\_{i}^{-1/\alpha}\left(\lambda\_{i}-1\right)^{-1},
we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→∞IF¯1​(t)\displaystyle\lim\_{t\rightarrow\infty}\frac{I}{\overline{F}\_{1}\left(t\right)} | =limt→∞F¯i​(li)F¯1​(t)​∏k∈J1Fk​(dk)\displaystyle=\lim\_{t\rightarrow\infty}\frac{\overline{F}\_{i}\left(l\_{i}\right)}{\overline{F}\_{1}\left(t\right)}{\displaystyle\prod\limits\_{k\in J\_{1}}}F\_{k}(d\_{k}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(ξ​λi)−α.\displaystyle=\left(\xi\lambda\_{i}\right)^{-\alpha}. |  |

(4) In this case, since XiX\_{i}’s are independent, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | I\displaystyle I | =ℙ​(li+lj>t+di+dj,Xi>li,Xj>lj)​ℙ​(𝕁1)\displaystyle=\mathbb{P}\left(l\_{i}+l\_{j}>t+d\_{i}+d\_{j},X\_{i}>l\_{i},X\_{j}>l\_{j}\right)\mathbb{P}\left(\mathbb{J}\_{1}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙ​(li+lj>t+di+dj​|Xi>​li,Xj>lj)​ℙ​(Xi>li)​ℙ​(Xj>lj)​ℙ​(𝕁1).\displaystyle=\mathbb{P}\left(l\_{i}+l\_{j}>t+d\_{i}+d\_{j}\left|X\_{i}>l\_{i},X\_{j}>l\_{j}\right.\right)\mathbb{P}\left(X\_{i}>l\_{i}\right)\mathbb{P}\left(X\_{j}>l\_{j}\right)\mathbb{P}\left(\mathbb{J}\_{1}\right). |  |

Then, following the similar proof to that for case (3), we have

|  |  |  |
| --- | --- | --- |
|  | limt→∞ℙ​(Xi>li)F¯1​(t)​ℙ​(Xj>lj)=0,\lim\_{t\rightarrow\infty}\frac{\mathbb{P}\left(X\_{i}>l\_{i}\right)}{\overline{F}\_{1}\left(t\right)}\mathbb{P}\left(X\_{j}>l\_{j}\right)=0, |  |

which leads to ([A.3](https://arxiv.org/html/2512.18790v1#A1.E3 "In A.1 Proofs of results under Model 1 ‣ Appendix A Proofs of analytical results ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")). Moreover, when the cardinality of J3J\_{3} is
greater than 11, ([A.3](https://arxiv.org/html/2512.18790v1#A1.E3 "In A.1 Proofs of results under Model 1 ‣ Appendix A Proofs of analytical results ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) holds as well.

(5) In this case, since XiX\_{i}’s are independent, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | I\displaystyle I | =ℙ(Xi+lj>t+di+dj,di<Xi≤li,Xj>lj)ℙ(𝕁1)\displaystyle=\mathbb{P}\left(X\_{i}+l\_{j}>t+d\_{i}+d\_{j},d\_{i}<X\_{i}\leq l\_{i},X\_{j}>l\_{j}\right)\mathbb{P}\left(\mathbb{J}\_{1}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙ(Xi+lj>t+di+dj|di<Xi≤li,Xj>lj)ℙ(di<Xi≤li)ℙ(Xj>lj)ℙ(𝕁1).\displaystyle=\mathbb{P}\left(X\_{i}+l\_{j}>t+d\_{i}+d\_{j}\left|d\_{i}<X\_{i}\leq l\_{i},X\_{j}>l\_{j}\right.\right)\mathbb{P}\left(d\_{i}<X\_{i}\leq l\_{i}\right)\mathbb{P}\left(X\_{j}>l\_{j}\right)\mathbb{P}\left(\mathbb{J}\_{1}\right). |  |

Then following the similar proof to that for case (1), we have

|  |  |  |
| --- | --- | --- |
|  | limt→∞ℙ​(di<Xi≤li)F¯1​(t)​ℙ​(Xj>lj)=0,\lim\_{t\rightarrow\infty}\frac{\mathbb{P}\left(d\_{i}<X\_{i}\leq l\_{i}\right)}{\overline{F}\_{1}\left(t\right)}\mathbb{P}\left(X\_{j}>l\_{j}\right)=0, |  |

which leads to ([A.3](https://arxiv.org/html/2512.18790v1#A1.E3 "In A.1 Proofs of results under Model 1 ‣ Appendix A Proofs of analytical results ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")). Moreover, when the cardinality of J2∪J3J\_{2}\cup J\_{3} is greater than 11, ([A.3](https://arxiv.org/html/2512.18790v1#A1.E3 "In A.1 Proofs of results under Model 1 ‣ Appendix A Proofs of analytical results ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) holds as well.

To sum up, we obtain the following result

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→∞ℙ​(Sn>t)F¯1​(t)=∑j∈Z(θj−1/α+ξ)−α,\lim\_{t\rightarrow\infty}\frac{\mathbb{P}(S\_{n}>t)}{\overline{F}\_{1}\left(t\right)}=\sum\_{j\in Z}\left(\theta\_{j}^{-1/\alpha}+\xi\right)^{-\alpha}, |  | (A.4) |

where Z={j=1,2,…,n:ξ>θj−1/α​(λj−1)−1}Z=\left\{j=1,2,...,n:\xi>\theta\_{j}^{-1/\alpha}\left(\lambda\_{j}-1\right)^{-1}\right\}.

Next, we obtain the limit of VaRp​(Sn)VaRp​(X1)\frac{\mathrm{VaR}\_{p}(S\_{n})}{\mathrm{VaR}\_{p}(X\_{1})} as p→1p\rightarrow 1. If ZZ is an empty set, then limp→1VaRp​(Sn)VaRp​(X1)=0\lim\_{p\rightarrow 1}\frac{\mathrm{VaR}\_{p}(S\_{n})}{\mathrm{VaR}\_{p}(X\_{1})}=0.
When ZZ is not empty, we denote the right-hand side of ([A.4](https://arxiv.org/html/2512.18790v1#A1.E4 "In A.1 Proofs of results under Model 1 ‣ Appendix A Proofs of analytical results ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) by aa, which
is not 0. Then for any ε>0\varepsilon>0, there exits t0>0t\_{0}>0 such that for
t>t0t>t\_{0}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | a​F¯1​(t)−ε≤ℙ​(Sn>t)≤a​F¯1​(t)+ε.a\overline{F}\_{1}\left(t\right)-\varepsilon\leq\mathbb{P}(S\_{n}>t)\leq a\overline{F}\_{1}\left(t\right)+\varepsilon. |  | (A.5) |

Since

|  |  |  |
| --- | --- | --- |
|  | VaRp​(Sn)=inf{x:ℙ​(Sn≤x)≥p}=inf{x:ℙ​(Sn>x)≤1−p},\mathrm{VaR}\_{p}(S\_{n})=\inf\left\{x:\mathbb{P}(S\_{n}\leq x)\geq p\right\}=\inf\left\{x:\mathbb{P}(S\_{n}>x)\leq 1-p\right\}, |  |

([A.5](https://arxiv.org/html/2512.18790v1#A1.E5 "In A.1 Proofs of results under Model 1 ‣ Appendix A Proofs of analytical results ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) implies that for pp close to 1, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | inf{x:F¯1​(x)≤1−p+εa}≤VaRp​(Sn)≤inf{x:F¯1​(x)≤1−p−εa}.\inf\left\{x:\overline{F}\_{1}\left(x\right)\leq\frac{1-p+\varepsilon}{a}\right\}\leq\mathrm{VaR}\_{p}(S\_{n})\leq\inf\left\{x:\overline{F}\_{1}\left(x\right)\leq\frac{1-p-\varepsilon}{a}\right\}. |  | (A.6) |

Since ([A.6](https://arxiv.org/html/2512.18790v1#A1.E6 "In A.1 Proofs of results under Model 1 ‣ Appendix A Proofs of analytical results ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) holds for arbitrary ε\varepsilon, we have

|  |  |  |
| --- | --- | --- |
|  | VaRp​(Sn)∼VaR1−(1−p)/a​(X1).\mathrm{VaR}\_{p}(S\_{n})\sim\mathrm{VaR}\_{1-\left(1-p\right)/a}(X\_{1}). |  |

This leads to the following result

|  |  |  |
| --- | --- | --- |
|  | limp→1VaRp​(Sn)VaRp​(X1)=limp→1VaRp​(Sn)VaR1−(1−p)/a​(X1)​VaR1−(1−p)/a​(X1)VaRp​(X1)=a1/α\lim\_{p\rightarrow 1}\frac{\mathrm{VaR}\_{p}(S\_{n})}{\mathrm{VaR}\_{p}(X\_{1})}=\lim\_{p\rightarrow 1}\frac{\mathrm{VaR}\_{p}(S\_{n})}{\mathrm{VaR}\_{1-\left(1-p\right)/a}(X\_{1})}\frac{\mathrm{VaR}\_{1-\left(1-p\right)/a}(X\_{1})}{\mathrm{VaR}\_{p}(X\_{1})}=a^{1/\alpha} |  |

by the convergence of extreme quantile estimator (see e.g., Theorem 4.3.8 of haan2006extreme). When a=0a=0, it reduces to the case that ZZ is an empty set.
Similarly, from the assumption ([2.5](https://arxiv.org/html/2512.18790v1#S2.E5 "In 1st item ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")), we can show that

|  |  |  |
| --- | --- | --- |
|  | limp→1VaRp​(Xi)VaRp​(X1)=θi1/α.\lim\_{p\rightarrow 1}\frac{\mathrm{VaR}\_{p}(X\_{i})}{\mathrm{VaR}\_{p}(X\_{1})}=\theta\_{i}^{1/\alpha}. |  |

Furthermore, we also have

|  |  |  |
| --- | --- | --- |
|  | limp→1I3=limp→1VaRp​(Sn)VaRp​(X1)​VaRp​(X1)VaRp​(Xi)=(aθi)1/α=θi−1/α​(∑j∈Z(θj−1/α+ξ)−α)1/α.\lim\_{p\rightarrow 1}I\_{3}=\lim\_{p\rightarrow 1}\frac{\mathrm{VaR}\_{p}(S\_{n})}{\mathrm{VaR}\_{p}(X\_{1})}\frac{\mathrm{VaR}\_{p}(X\_{1})}{\mathrm{VaR}\_{p}(X\_{i})}=\left(\frac{a}{\theta\_{i}}\right)^{1/\alpha}=\theta\_{i}^{-1/\alpha}\left(\sum\_{j\in Z}\left(\theta\_{j}^{-1/\alpha}+\xi\right)^{-\alpha}\right)^{1/\alpha}. |  |

The desired result follows by combining all of the above three terms.

### A.2 Proofs of results under Model 2

Proof of Lemma [2.2](https://arxiv.org/html/2512.18790v1#S2.Thmlemma2 "Lemma 2.2 ‣ 2.3 Pool with general losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.").

If αi=α1\alpha\_{i}=\alpha\_{1}, then all the results can be proved in the same way as that for Lemma [2.1](https://arxiv.org/html/2512.18790v1#S2.Thmlemma1 "Lemma 2.1 ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."). If αi>α1\alpha\_{i}>\alpha\_{1}, then

|  |  |  |
| --- | --- | --- |
|  | limt→∞F¯i​(t)F¯1​(t)=0,andlimp→1VaRp​(Xi)VaRp​(X1)=0.\lim\_{t\rightarrow\infty}\frac{\overline{F}\_{i}(t)}{\overline{F}\_{1}(t)}=0,\qquad\text{and}\qquad\lim\_{p\rightarrow 1}\frac{\mathrm{VaR}\_{p}(X\_{i})}{\mathrm{VaR}\_{p}(X\_{1})}=0. |  |

Thus we obtain the following result

|  |  |  |
| --- | --- | --- |
|  | limp→1di​(p)d1​(p)=limp→1di​(p)VaRp​(Xi)​VaRp​(X1)d1​(p)​VaRp​(Xi)VaRp​(X1)=0,\lim\_{p\rightarrow 1}\frac{d\_{i}(p)}{d\_{1}(p)}=\lim\_{p\rightarrow 1}\frac{d\_{i}(p)}{\mathrm{VaR}\_{p}(X\_{i})}\frac{\mathrm{VaR}\_{p}(X\_{1})}{d\_{1}(p)}\frac{\mathrm{VaR}\_{p}(X\_{i})}{\mathrm{VaR}\_{p}(X\_{1})}=0, |  |

and similarly we have

|  |  |  |
| --- | --- | --- |
|  | limp→1di​(p)VaRp​(X1)=limp→1li​(p)VaRp​(X1)=0.\lim\_{p\rightarrow 1}\frac{d\_{i}(p)}{\mathrm{VaR}\_{p}(X\_{1})}=\lim\_{p\rightarrow 1}\frac{l\_{i}(p)}{\mathrm{VaR}\_{p}(X\_{1})}=0. |  |

Note that when αi>α1\alpha\_{i}>\alpha\_{1}, we have θi=0\theta\_{i}=0. Thus the
desired results hold. Now we are left to show limp→1F¯i​(di)F¯1​(d1)=1\lim\_{p\rightarrow 1}\frac{\overline{F}\_{i}(d\_{i})}{\overline{F}\_{1}(d\_{1})}=1, which follows
from

|  |  |  |
| --- | --- | --- |
|  | limp→1F¯i​(di)F¯1​(d1)=limp→1F¯i​(di)/(1−p)F¯1​(d1)/(1−p)=limp→1F¯i​(di)/F¯i​(VaRp​(Xi))F¯1​(d1)/F¯1​(VaRp​(X1))=1\lim\_{p\rightarrow 1}\frac{\overline{F}\_{i}(d\_{i})}{\overline{F}\_{1}(d\_{1})}=\lim\_{p\rightarrow 1}\frac{\overline{F}\_{i}(d\_{i})/(1-p)}{\overline{F}\_{1}(d\_{1})/(1-p)}=\lim\_{p\rightarrow 1}\frac{\overline{F}\_{i}(d\_{i})/\overline{F}\_{i}\left(\mathrm{VaR}\_{p}(X\_{i})\right)}{\overline{F}\_{1}(d\_{1})/\overline{F}\_{1}\left(\mathrm{VaR}\_{p}(X\_{1})\right)}=1 |  |

by ([2.10](https://arxiv.org/html/2512.18790v1#S2.E10 "In 2nd item ‣ 2.3 Pool with general losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) and the definition of regular variation. This completes the proof.

 

Proof of Theorem [2.2](https://arxiv.org/html/2512.18790v1#S2.Thmtheorem2 "Theorem 2.2 ‣ 2.3 Pool with general losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.").

Consider the same split ([A.1](https://arxiv.org/html/2512.18790v1#A1.E1 "In A.1 Proofs of results under Model 1 ‣ Appendix A Proofs of analytical results ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) as in Theorem [2.1](https://arxiv.org/html/2512.18790v1#S2.Thmtheorem1 "Theorem 2.1 ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."). Applying the
analysis of I1I\_{1} to Model 2, we have

|  |  |  |
| --- | --- | --- |
|  | limp→1I1={1,ξα1/αi≥1,ξα1/αi,1/λi≤ξα1/αi<1,1−(λi−1)​ξα1/αi,ξα1/αi<1/λi.\lim\_{p\rightarrow 1}I\_{1}=\left\{\begin{array}[c]{lll}1,&&\xi^{\alpha\_{1}/\alpha\_{i}}\geq 1,\\ \xi^{\alpha\_{1}/\alpha\_{i}},&&1/\lambda\_{i}\leq\xi^{\alpha\_{1}/\alpha\_{i}}<1,\\ 1-(\lambda\_{i}-1)\xi^{\alpha\_{1}/\alpha\_{i}},&&\xi^{\alpha\_{1}/\alpha\_{i}}<1/\lambda\_{i}.\end{array}\right. |  |

For I2⋅I3I\_{2}\cdot I\_{3}, on the one hand, the relation ([A.2](https://arxiv.org/html/2512.18790v1#A1.E2 "In A.1 Proofs of results under Model 1 ‣ Appendix A Proofs of analytical results ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")) holds for E​[Yi]E[Y\_{i}]:

|  |  |  |
| --- | --- | --- |
|  | limp→1E​[Yi]di​F¯i​(di)=λi1−αi−11−αi.\lim\_{p\rightarrow 1}\frac{E[Y\_{i}]}{d\_{i}\overline{F}\_{i}\left(d\_{i}\right)}=\frac{\lambda\_{i}^{1-\alpha\_{i}}-1}{1-\alpha\_{i}}. |  |

For E​[Sn]E\left[S\_{n}\right], first note that by Lemma [2.2](https://arxiv.org/html/2512.18790v1#S2.Thmlemma2 "Lemma 2.2 ‣ 2.3 Pool with general losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."), for
αi≥α1\alpha\_{i}\geq\alpha\_{1},

|  |  |  |
| --- | --- | --- |
|  | limp→1E​[Yi]d1​F¯1​(d1)=limp→1E​[Yi]di​F¯i​(di)​di​F¯i​(di)d1​F¯1​(d1)=(λi1−α1−1)​θi1/α11−α1,\lim\_{p\rightarrow 1}\frac{E[Y\_{i}]}{d\_{1}\overline{F}\_{1}\left(d\_{1}\right)}=\lim\_{p\rightarrow 1}\frac{E[Y\_{i}]}{d\_{i}\overline{F}\_{i}\left(d\_{i}\right)}\frac{d\_{i}\overline{F}\_{i}\left(d\_{i}\right)}{d\_{1}\overline{F}\_{1}\left(d\_{1}\right)}=\frac{\left(\lambda\_{i}^{1-\alpha\_{1}}-1\right)\theta\_{i}^{1/\alpha\_{1}}}{1-\alpha\_{1}}, |  |

which is 0 if αi>α1\alpha\_{i}>\alpha\_{1} as θi=0\theta\_{i}=0. Then we have

|  |  |  |
| --- | --- | --- |
|  | limp→1E​[Sn]d1​F¯1​(d1)=limp→1∑j=1nE​[Yj]d1​F¯1​(d1)=∑j=1n(λj1−α1−1)​θj1/α11−α1.\lim\_{p\rightarrow 1}\frac{E\left[S\_{n}\right]}{d\_{1}\overline{F}\_{1}\left(d\_{1}\right)}=\lim\_{p\rightarrow 1}\sum\_{j=1}^{n}\frac{E[Y\_{j}]}{d\_{1}\overline{F}\_{1}\left(d\_{1}\right)}=\sum\_{j=1}^{n}\frac{\left(\lambda\_{j}^{1-\alpha\_{1}}-1\right)\theta\_{j}^{1/\alpha\_{1}}}{1-\alpha\_{1}}. |  |

On the other hand, by Lemma [2.2](https://arxiv.org/html/2512.18790v1#S2.Thmlemma2 "Lemma 2.2 ‣ 2.3 Pool with general losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") and following the proof of Theorem [2.1](https://arxiv.org/html/2512.18790v1#S2.Thmtheorem1 "Theorem 2.1 ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."), we have

|  |  |  |
| --- | --- | --- |
|  | limp→1VaRp​(Sn)VaRp​(X1)=(∑j∈Z(θj−1/α1+ξα1/αj)−α1)1/α1.\lim\_{p\rightarrow 1}\frac{\mathrm{VaR}\_{p}(S\_{n})}{\mathrm{VaR}\_{p}(X\_{1})}=\left(\sum\_{j\in Z}\left(\theta\_{j}^{-1/\alpha\_{1}}+\xi^{\alpha\_{1}/\alpha\_{j}}\right)^{-\alpha\_{1}}\right)^{1/\alpha\_{1}}. |  |

This is due to the fact that if αj>α1\alpha\_{j}>\alpha\_{1}, we have θj=0\theta\_{j}=0
and j∉Zj\not\in Z. Then, it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limp→1I2⋅I3\displaystyle\lim\_{p\rightarrow 1}I\_{2}\cdot I\_{3} | =limp→1E​[Yi]E​[Sn]​VaRp​(Sn)VaRp​(Xi)\displaystyle=\lim\_{p\rightarrow 1}\frac{E\left[Y\_{i}\right]}{E\left[S\_{n}\right]}\frac{\mathrm{VaR}\_{p}(S\_{n})}{\mathrm{VaR}\_{p}(X\_{i})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =limp→1E​[Yi]di​F¯i​(di)​d1​F¯1​(d1)E​[Sn]​VaRp​(Sn)VaRp​(X1)​diVaRp​(Xi)​VaRp​(X1)d1​F¯i​(di)F¯1​(d1)\displaystyle=\lim\_{p\rightarrow 1}\frac{E[Y\_{i}]}{d\_{i}\overline{F}\_{i}\left(d\_{i}\right)}\frac{d\_{1}\overline{F}\_{1}\left(d\_{1}\right)}{E\left[S\_{n}\right]}\frac{\mathrm{VaR}\_{p}(S\_{n})}{\mathrm{VaR}\_{p}(X\_{1})}\frac{d\_{i}}{\mathrm{VaR}\_{p}(X\_{i})}\frac{\mathrm{VaR}\_{p}(X\_{1})}{d\_{1}}\frac{\overline{F}\_{i}\left(d\_{i}\right)}{\overline{F}\_{1}\left(d\_{1}\right)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1−α1)​(λi1−αi−1)​ξα1/αi−1(1−αi)​∑j=1n(λj1−α1−1)​θj1/α1​(∑j∈Z(θj−1/α1+ξ)−α1)1/α1.\displaystyle=\frac{\left(1-\alpha\_{1}\right)\left(\lambda\_{i}^{1-\alpha\_{i}}-1\right)\xi^{\alpha\_{1}/\alpha\_{i}-1}}{(1-\alpha\_{i})\sum\_{j=1}^{n}\left(\lambda\_{j}^{1-\alpha\_{1}}-1\right)\theta\_{j}^{1/\alpha\_{1}}}\left(\sum\_{j\in Z}\left(\theta\_{j}^{-1/\alpha\_{1}}+\xi\right)^{-\alpha\_{1}}\right)^{1/\alpha\_{1}}. |  |

This completes the proof.

### A.3 Proof of Theorem [2.3](https://arxiv.org/html/2512.18790v1#S2.Thmtheorem3 "Theorem 2.3 ‣ 2.4 Asymptotic optimal pool ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.")

Proof. When ξ≥1\xi\geq 1, the smallest value possible of DRi​(1)\mathrm{DR}\_{i}(1) is 1, which is achieved when Δξ,𝝀=0\Delta\_{\xi,\boldsymbol{\lambda}}=0. When ξ<1\xi<1, the smallest possible
DRi​(1)\mathrm{DR}\_{i}(1) is ξα1/αi\xi^{\alpha\_{1}/\alpha\_{i}}, which is achieve when
λi≥ξ−α1/αi\lambda\_{i}\geq\xi^{-\alpha\_{1}/\alpha\_{i}} and Δξ,𝝀=0\Delta\_{\xi,\boldsymbol{\lambda}}=0. Next, we find λi\lambda\_{i}’s such that Δξ,𝝀=0\Delta\_{\xi,\boldsymbol{\lambda}}=0 and show that λi≥ξ−α1/αi\lambda\_{i}\geq\xi^{-\alpha\_{1}/\alpha\_{i}} and Δξ,𝝀=0\Delta\_{\xi,\boldsymbol{\lambda}}=0 can be satisfied
at the same time.

Firstly, we find λi\lambda\_{i}’s such that Δξ,𝝀=0\Delta\_{\xi,\boldsymbol{\lambda}}=0.
This is obtained when the set ZZ is an empty set, which happens when ξ≤θj−1/α1​(λj−1)−1\xi\leq\theta\_{j}^{-1/\alpha\_{1}}\left(\lambda\_{j}-1\right)^{-1}, or
equivalently λj≤1+θj−1/α1​ξ−1\lambda\_{j}\leq 1+\theta\_{j}^{-1/\alpha\_{1}}\xi^{-1}, for all
j=1,2,…,nj=1,2,...,n.

Combining this result with λi≥ξ−α1/αi\lambda\_{i}\geq\xi^{-\alpha\_{1}/\alpha\_{i}} (when
0<ξ<10<\xi<1) and λi>1\lambda\_{i}>1 (when ξ≥1\xi\geq 1 by ([2.7](https://arxiv.org/html/2512.18790v1#S2.E7 "In 2nd item ‣ 2.2 Pool with tail equivalent losses ‣ 2 Optimal pooling structure ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."))) leads to the feasible set of
𝝀\boldsymbol{\lambda}, which is

|  |  |  |
| --- | --- | --- |
|  | 𝝀∈{(λ1,…,λn):min⁡{ξ−α1/αi,1}≤λi​ and ​λi≤1+θi−1/α1​ξ−1}.\boldsymbol{\lambda}\in\{(\lambda\_{1},...,\lambda\_{n}):\min\{\xi^{-\alpha\_{1}/\alpha\_{i}},1\}\leq\lambda\_{i}\text{ and }\lambda\_{i}\leq 1+\theta\_{i}^{-1/\alpha\_{1}}\xi^{-1}\}. |  |

Lastly, we need to verify that min⁡{ξ−α1/αi,1}≤1+θi−1/α1​ξ−1\min\{\xi^{-\alpha\_{1}/\alpha\_{i}},1\}\leq 1+\theta\_{i}^{-1/\alpha\_{1}}\xi^{-1}. This is due to the facts that
0≤θi≤10\leq\theta\_{i}\leq 1 for all i=1,…,ni=1,...,n and that in Model 2, α1=min⁡{α1,…,αn}\alpha\_{1}=\min\left\{\alpha\_{1},...,\alpha\_{n}\right\}, which yields
α1/αi≤1\alpha\_{1}/\alpha\_{i}\leq 1 for all i=1,…,ni=1,...,n. The desired result follows immediately.

## Appendix B Comparison of algorithms for simulation study

In this section, we provide a comparison of candidates for the numerical optimization algorithm used in Section [3](https://arxiv.org/html/2512.18790v1#S3 "3 Simulation study ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."), and justify the choice of GSA used in this paper. In the experiments within this comparison, we use a set of 20 samples with parameters from the second study of risks of different indices, and set ξ=0.31/8.5\xi=0.3^{1/8.5} and p=0.95p=0.95. We consider the following global optimization algorithms:

1. 1.

   Artificial Bee Colony (ABC) (karaboga2005idea): an optimizer inspired by the foraging behaviour of a honey bee colony which searches for an optimal food source.
2. 2.

   Differential Evolution (DE) (storn1997differential; mullen2011deoptim): an optimization algorithm where candidates for the optimal solution are improved through evolution mechanisms such as mutation, crossover, selection.
3. 3.

   Generalized Simulated Annealing (GSA) (tsallis1996generalized; xiang\_generalized\_2013): a stochastic optimizer inspired by the annealing process in Metallurgy, which uses a heat treatment to minimize the material’s internal energy (thermodynamics).
4. 4.

   Harmony Search (HS) (geem\_new\_2001): an optimization algorithm which mimics the process of improvisation of musicians in search of harmony.
5. 5.

   Particle Swarm Optimization (PSO) (kennedy1995particle; clerc\_standard\_2012): an algorithm imitating the movements of a flock of birds or a school of fish towards the optimal solution.

While DE and GSA are applied using their respective R packages (DEoptim and GenSA), the algorithms ABC, HS and PSO are built from scratch due to the unstable performance and poor maintenance of their R packages. To ensure the fairness of the comparison between algorithms, four factors are kept unchanged across these five experiments. Firstly, all experiments use the same 20 samples of XiX\_{i}’s for the estimations described in Section [3](https://arxiv.org/html/2512.18790v1#S3 "3 Simulation study ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies."), where each sample leads to an approximation of the optimal solution 𝝀​(p)\boldsymbol{\lambda}(p). Secondly, all variations of these experiments use the same starting points for the algorithm (i.e. the initial guess for the optimal solution). Thirdly, the convergence criterion is consistent across algorithms, where algorithms are deemed to have found the optimal solution if the function value is not improved after 500 consecutive iterations, with an iteration refers to an update of the optimal solution. Lastly, the maximum number of iterations allowed for each algorithm is the same, where algorithms are terminated if they do not converge after 10 thousand iterations.

We compare the performance of the algorithms based on two criteria: efficiency and accuracy. On the one hand, the efficiency is measured by the time TkT\_{k} (k∈{ABC, DE, GSA, HS, PSO}k\in\{\text{ABC, DE, GSA, HS, PSO}\}) needed for the algorithm to either converge or be terminated. Using 20 samples of XiX\_{i}’s, we obtain a sample t1,k,…,t20,kt\_{1,k},...,t\_{20,k} of TkT\_{k}. Inspired by the comparison protocols presented by beiranvand2017best, Figures [8](https://arxiv.org/html/2512.18790v1#A2.F8 "Figure 8 ‣ Appendix B Comparison of algorithms for simulation study ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") and [9](https://arxiv.org/html/2512.18790v1#A2.F9 "Figure 9 ‣ Appendix B Comparison of algorithms for simulation study ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") show the box plots and the empirical cumulative distribution functions of TkT\_{k}

|  |  |  |
| --- | --- | --- |
|  | F^Tk​(x)=120​∑j=1201{tj​k≤x}.\widehat{F}\_{T\_{k}}(x)=\frac{1}{20}\sum\_{j=1}^{20}1\_{\{t\_{jk}\leq x\}}. |  |

The results show that GSA and HS are the most efficient algorithms, as 100% of numerical optimization problems tested are solved within 5 hours using these algorithms. ABC is the most inefficient among five algorithms as it takes more than 90 hours for ABC to solve any problem.

![Refer to caption](box_time1.png)


(a) With ABC

![Refer to caption](box_time2.png)


(b) Without ABC

Figure 8: Box plots of TkT\_{k}

![Refer to caption](cdf_time.png)


Figure 9: Plots of empirical cumulative distribution functions of TkT\_{k}

On the other hand, the accuracy of algorithms is measured by the absolute error E​RkER\_{k} (k∈{ABC, DE, GSA, HS, PSO}k\in\{\text{ABC, DE, GSA, HS, PSO}\}), with observations e​rj,ker\_{j,k} (j=1,…,20j=1,...,20) defined as follows:

|  |  |  |
| --- | --- | --- |
|  | e​rj,k=|xj,k−mink⁡{xj,k}|er\_{j,k}=|x\_{j,k}-\min\_{k}\{x\_{j,k}\}| |  |

where xj,kx\_{j,k} is the optimal solution of the problem from the jj-th sample obtained using algorithm kk, and mink⁡{xj,k}\min\_{k}\{x\_{j,k}\} is assumed to be the true optimal solution of problem jj. Figures [10](https://arxiv.org/html/2512.18790v1#A2.F10 "Figure 10 ‣ Appendix B Comparison of algorithms for simulation study ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") and [11](https://arxiv.org/html/2512.18790v1#A2.F11 "Figure 11 ‣ Appendix B Comparison of algorithms for simulation study ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") show the box plots of E​RkER\_{k} and the empirical cumulative distribution functions F^E​Rk\widehat{F}\_{ER\_{k}}, which is defined similarly to F^Tk\widehat{F}\_{T\_{k}}. It is clear that HS has the worst performance in terms of accuracy. Although GSA is not as accurate is ABC, DE and PSO, it still allows us to obtain a solution within 10−610^{-6} of the true optimal solution in all problems.

![Refer to caption](box_error1.png)


(a) With HS

![Refer to caption](box_error2.png)


(b) Without HS

Figure 10: Box plots of E​RkER\_{k}

![Refer to caption](cdf_error.png)


Figure 11: Plots of empirical cumulative distribution functions of E​RkER\_{k}

Considering the performance of those five algorithms, GSA is the best candidate for the simulation study due to its ability to balance efficiency and accuracy.

## Appendix C Exploratory analysis of the NFIP data

In this section, we provide further details on the results of the statistical tests carried out in the exploratory analysis of the NFIP data in the main text. Denote γ^​(k)=1/α^​(k)\widehat{\gamma}(k)=1/\widehat{\alpha}(k) an inverse tail index estimated using the Hill’s estimator with kk largest observations. The first test is for the regularly varying tail of the risks (Theorem 1 of dietrich2002testing). A stricter version of the null hypothesis H0:F¯∈R​V−1/γH\_{0}:\overline{F}\in RV\_{-1/\gamma} for some γ>0\gamma>0 is not rejected if the test statistic

|  |  |  |
| --- | --- | --- |
|  | k​∫01(log⁡X(m−⌊k​t⌋)−log⁡X(m−k)γ^​(k)+log⁡t)2​t2​𝑑t,k\int^{1}\_{0}\left(\frac{\log{X}\_{(m-\lfloor kt\rfloor)}-\log{X}\_{(m-k)}}{\widehat{\gamma}(k)}+\log t\right)^{2}t^{2}dt, |  |

where X(1)≤X(2)≤⋯≤X(m){X}\_{(1)}\leq{X}\_{(2)}\leq\cdots\leq{X}\_{(m)} denote the order statistics
for a sample X1,…,Xm{X}\_{1},...,{X}\_{m} of distribution FF, converges in distribution as m→∞m\rightarrow\infty to

|  |  |  |
| --- | --- | --- |
|  | T=∫01(B​(t)+t​log⁡t​∫01B​(s)s​ ​d​s)2​𝑑t,T=\int\_{0}^{1}\left(B(t)+t\log t\int\_{0}^{1}\frac{B(s)}{s\text{ }ds}\right)^{2}dt, |  |

where {B​(t)}\{B(t)\} is a Brownian bridge. Critical values of TT are available in dietrich2002testing. The results in Figure [12](https://arxiv.org/html/2512.18790v1#A3.F12 "Figure 12 ‣ Appendix C Exploratory analysis of the NFIP data ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") show that there is strong evidence at the chosen significance level 0.01 that all three risks in our dataset have a regularly varying tail.

![Refer to caption](RV_test_NY.png)


(a) NY

![Refer to caption](RV_test_CA.png)


(b) CA

![Refer to caption](RV_test_FL.png)


(c) FL

Figure 12: Results of regularly varying distribution tests. If the test statistic is smaller than the critical value for a large range of kk then there is strong evidence that FF has a regularly varying tail. The dashed line indicates the critical value of TT of significance level 0.01.

Table [3](https://arxiv.org/html/2512.18790v1#A3.T3 "Table 3 ‣ Appendix C Exploratory analysis of the NFIP data ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") shows the results of the Pearson and Spearman correlation tests. Two pairs of risks NY - CA and CA - FL present strong evidence of independence at significance level 0.01, while NY - FL seems to have a non-linear monotonic relation.

|  |  |  |
| --- | --- | --- |
|  | Pearson correlation test | Spearman correlation test |
|  | H0H\_{0}: two risks are  linearly independent | H0H\_{0}: two risks do not have  monotonic relation |
| NY vs. CA | corr: -0.009524  p-value: 0.8233 | corr: 0.042562  p-value: 0.1435 |
| NY vs. FL | corr: -0.002893  p-value: 0.9459 | corr: 0.131117  p-value: 4.192×10−64.192\times 10^{-6} |
| CA vs. FL | corr: -0.007786  p-value: 0.8552 | corr: -0.031568  p-value: 0.2777 |

Table 3: Results of independence tests

Lastly, we carry out tests for tail equivalence proposed by daouia2024optimal for two pairs of risks NY - CA and CA - FL (denoted below X1X\_{1} and X2X\_{2}). For i=1,2i=1,2, based on kik\_{i} largest observations of XiX\_{i}, we obtain the estimated inverse tail index γ^i​(ki)\widehat{\gamma}\_{i}(k\_{i}) of XiX\_{i} by using the Hill’s estimator. Under the assumption of independence between risks, daouia2024optimal define the pooled inverse tail index as

|  |  |  |
| --- | --- | --- |
|  | γ^p​o​o​l=∑i=12wi​γ^i​(ki),\widehat{\gamma}\_{pool}=\sum\_{i=1}^{2}w\_{i}\widehat{\gamma}\_{i}(k\_{i}), |  |

where

|  |  |  |
| --- | --- | --- |
|  | (w1,w2)=𝒘=Σ−1​𝟏𝟏T​Σ−1​𝟏,Σ=[γ^12​(k1)/k100γ^22​(k2)/k2](w\_{1},w\_{2})=\boldsymbol{w}=\frac{\Sigma^{-1}\mathbf{1}}{\mathbf{1}^{\mathrm{T}}\Sigma^{-1}\mathbf{1}},\qquad\Sigma=\begin{bmatrix}\widehat{\gamma}\_{1}^{2}(k\_{1})/k\_{1}&0\\ 0&\widehat{\gamma}\_{2}^{2}(k\_{2})/k\_{2}\end{bmatrix} |  |

and 𝟏=(1,1)T∈ℝ2\mathbf{1}=(1,1)^{\mathrm{T}}\in\mathbb{R}^{2}. Therefore, the test statistic is defined as

|  |  |  |
| --- | --- | --- |
|  | ∑i=12ki​(γ^i​(ki)−γ^p​o​o​l)2γ^i2​(ki)\sum\_{i=1}^{2}k\_{i}\frac{(\widehat{\gamma}\_{i}(k\_{i})-\widehat{\gamma}\_{pool})^{2}}{\widehat{\gamma}\_{i}^{2}(k\_{i})} |  |

and follows a χ12\chi^{2}\_{1} distribution under the null hypothesis H0:γ^i​(ki)=γ^p​o​o​l​∀i\mathrm{H}\_{0}:\widehat{\gamma}\_{i}(k\_{i})=\widehat{\gamma}\_{pool}\forall i. If the null hypothesis is not rejected, then X1X\_{1} and X2X\_{2} are assumed to have the same tail index defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | α^p​o​o​l=1/γ^p​o​o​l,\widehat{\alpha}\_{pool}=1/\widehat{\gamma}\_{pool}, |  | (C.1) |

which is called the pooled tail estimator. Results of this test are discussed in Section [4](https://arxiv.org/html/2512.18790v1#S4 "4 Empirical analysis ‣ Optimal Catastrophe Risk Pooling We thank Lisa Gao and David Saunders for their comments and suggestions on an earlier version of the paper. We also thank participants at the following conferences: Climate Change and Insurance Conference 2025, International Centre for Mathematical Science (Edinburgh, U.K., September 10th - September 12th, 2025); RSS International Conference 2025, Royal Statistical Society (Edinburgh, U.K, September 1st - September 4th, 2025); 2025 Actuarial Research Conference, Society of Actuaries (Toronto, Canada, July 29th - August 1st, 2025); 2025 ICSA China Conference, International Chinese Statistical Association, Beijing Normal University (Zhuhai, Guangdong, China, June 28th - June 30th, 2025); SSC Annual Meeting 2025, Statistical Society of Canada (Saskatoon, Canada, May 25th - May 28th, 2025). This research is partially funded by NSERC-RGPIN (2025-01123), SSRHC-Insight (435-2015-0682), the Pre-Dissertation PhD Candidate Scholarship from the Spencer Educational Foundation, and Department of Statistics and Actuarial Science at the University of Waterloo. The usual disclaimer applies.") of the main text.