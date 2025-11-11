---
authors:
- Jordan T Kemp
- Laura Fürsich
- Luís M A Bettencourt
doc_id: arxiv:2511.06165v1
family_id: arxiv:2511.06165
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Spatial Selection and the Multiscale Dynamics of Urban Change
url_abs: http://arxiv.org/abs/2511.06165v1
url_html: https://arxiv.org/html/2511.06165v1
venue: arXiv q-fin
version: 1
year: 2025
---


Jordan T. Kemp1,2,3∗, Laura Fürsich4,5 and Luís M. A. Bettencourt3,6
1Institute for New Economic Thinking at the Martin School, University of Oxford, Oxford, OX1 3UQ, UK
2School of Geography and the Environment, University of Oxford, Oxford OX1 3QY, UK
3University of Chicago, Department of Ecology and Evolution, Chicago IL, 60637, USA
4University of Chicago, Mansueto Institute for Urban Innovation, Chicago IL, 60637, USA
5University of Chicago, Department of Sociology, Chicago IL, 60637, USA
6Santa Fe Institute, Santa Fe NM, 87501, USA
∗corresponding author: Jordan Kemp (jordan.kemp@ouce.ox.ac.uk)

###### Abstract

Growth is a multi-layered phenomenon in human societies, composed of socioeconomic and demographic change at many different scales. Yet, standard macroeconomic indicators average over most of these processes, blurring the spatial and hierarchical heterogeneity driving people’s choices and experiences. To address this gap, we introduce here a framework based on the Price equation to decompose aggregate growth exactly into endogenous and selection effects across nested spatial scales. We illustrate this approach with population and income data from the Chicago metropolitan area (2014–2019) and show that both growth rates and spatial selection effects are most intense at local levels, fat-tailed and spatially correlated.
We also find that selection, defined as the covariance between prevailing income and relative population change, is concentrated in few spatial units and exhibits scaling behavior when grouped by county. Despite the intensity of local sorting, selection effects largely cancel in the aggregate, implying that fast heterogeneous micro-dynamics can yield deceptively stable macro-trends. By treating local spatial units (neighborhoods) as evolving subpopulations under selection, we demonstrate how methods from complex systems provide new tools to classify residential selection processes, such as abandonment and gentrification, in an urban sociological framework. This approach is general and applies to any other nested economic systems such as networks of production, occupations, or innovation enabling a new mechanistic understanding of compositional change and growth across scales of organization.

††preprint: APS/123-QED

## Introduction

Growth is a fundamental measure of change in modern human societies. While the social value of economic growth remains contested [[1](https://arxiv.org/html/2511.06165v1#bib.bib1)], it is commonly used to gauge a society’s vitality, its ability to produce and consume goods and services and, over time, to improve its stability and social welfare [[2](https://arxiv.org/html/2511.06165v1#bib.bib2)].
Beyond economics, growth can reveal compositional changes in populations [[3](https://arxiv.org/html/2511.06165v1#bib.bib3), [4](https://arxiv.org/html/2511.06165v1#bib.bib4)], and encode latent features of economic agents’ environments [[5](https://arxiv.org/html/2511.06165v1#bib.bib5)], making it broadly useful for studying sociodemographic dynamics.

Growth and change occur at multiple scales, often amplifying or mitigating inequalities across populations [[6](https://arxiv.org/html/2511.06165v1#bib.bib6)]. For example, there are typically stronger income inequalities between urban neighborhoods than within them [[7](https://arxiv.org/html/2511.06165v1#bib.bib7)]. Consequently, policy guided primarily by aggregate indicators such as total wages or GDP can produce unforeseen distributional effects felt acutely by disadvantaged households. Population aggregation in policy studies often averages away local socioeconomic dynamics relevant to individual households [[8](https://arxiv.org/html/2511.06165v1#bib.bib8)], undermining any theory of real agents responsive to heteogeneous local environmental change [[5](https://arxiv.org/html/2511.06165v1#bib.bib5)].
Crucially, such local and relative variations in income and population dominate socioeconomic dynamics in developed societies, where overall growth is slow.
Only recently has detailed and consistent small-scale data made it possible to empirically understand these dynamics.

As more disaggregated data become available and improve, however, new challenges arise.
Multi-scalar analysis of income growth, for example, remains difficult due to several interrelated factors. Data are embedded in sociopolitical contexts and reflect local regulatory environments that vary by local constituency (municipality) [[9](https://arxiv.org/html/2511.06165v1#bib.bib9)].
Moreover, empirical growth depends on dynamic processes such as the spatial sorting of heterogeneous populations, capital, and incomes [[10](https://arxiv.org/html/2511.06165v1#bib.bib10), [11](https://arxiv.org/html/2511.06165v1#bib.bib11)], making results highly sensitive to different aggregation methods [[12](https://arxiv.org/html/2511.06165v1#bib.bib12), [13](https://arxiv.org/html/2511.06165v1#bib.bib13)].

Multi-scale spatial accounting is therefore essential to studying income dynamics in cities [[7](https://arxiv.org/html/2511.06165v1#bib.bib7), [14](https://arxiv.org/html/2511.06165v1#bib.bib14)].
Several methodological approaches have been developed for this purpose, including hierarchical linear, spatial econometric, and structural decomposition models [[15](https://arxiv.org/html/2511.06165v1#bib.bib15), [16](https://arxiv.org/html/2511.06165v1#bib.bib16)].
These methods typically sum growth contributions across sectors or spatial units while accounting for spatial and temporal correlations [[17](https://arxiv.org/html/2511.06165v1#bib.bib17)].
Although influential in research and policy, such methods rely on restrictive assumptions such as linearity, separability, or phenomenological fits that limit interpretability [[18](https://arxiv.org/html/2511.06165v1#bib.bib18), [19](https://arxiv.org/html/2511.06165v1#bib.bib19)].

Resolving heterogeneous dynamics across scales is not a challenge unique to social studies.
Statistical methods for ecosystems and economic supply networks often aim to describe multiscalar dynamics of interaction [[20](https://arxiv.org/html/2511.06165v1#bib.bib20)] and shock propagation [[21](https://arxiv.org/html/2511.06165v1#bib.bib21)].
The Price equation [[22](https://arxiv.org/html/2511.06165v1#bib.bib22)] offers an exact decomposition separating endogenous growth effects from population sorting, or selection.
It is also recursive, making it well suited for measuring variations in subpopulations at successively lower levels. This hierarchical structure [[23](https://arxiv.org/html/2511.06165v1#bib.bib23)] captures selection processes operating independently across multiple scales, enabling the analysis of heterogeneous growth patterns in complex societies such as cities.

![Refer to caption](x1.png)


Figure 1: Local income and population growth rates are very heterogeneous and spatially correlated. In Chicago, A) relative income growth (left) and population growth (right) in neighborhoods (census tracts) vary strongly, on the order of γptr=±5%\gamma\_{p\_{\textrm{tr}}}=\pm 5\%/year and Δ​γptr±8%\Delta\gamma\_{p\_{\textrm{tr}}}\pm 8\%/year respectively. The insets show how the local heterogeneity and correlations in growth rates at the tract level wash out under averaging (Ecm​[⋅]\textrm{E}\_{\textrm{cm}}[\cdot]) into community areas. B) Heterogeneity, measured by the standard deviation at each organizational level across the MSA, decreases under aggregation. Shifts in the mean value encode selection effects to be explored in this paper. C) Differences between income growth aggregation methods, defined in Eqs. [2](https://arxiv.org/html/2511.06165v1#Sx2.E2 "In Results ‣ Spatial Selection and the Multiscale Dynamics of Urban Change") and [3](https://arxiv.org/html/2511.06165v1#Sx2.E3 "In Results ‣ Spatial Selection and the Multiscale Dynamics of Urban Change"), and a standard measure of aggregate income growth via Eq. [1](https://arxiv.org/html/2511.06165v1#Sx2.E1 "In Results ‣ Spatial Selection and the Multiscale Dynamics of Urban Change") encode information about growth dynamics.

In this paper, we develop a simple and exact method to disaggregate income growth in terms of local demographic effects using the Price equation of population selection.
As an illustration, we explore the rich spatial heterogeneity of urban population and income growth in the city of Chicago, which we show is averaged away in standard aggregate metrics. We show how the Price equation decomposes aggregate income growth into selection and endogenous effects at each organizational scale.
This enables comparative analysis of growth trends across local and citywide scales, for instance in response to policy choices. We demonstrate its utility by identifying local population change effects such as gentrification and income concentration. Lastly, we use the Price equation to aggregate these effects and produce exact summary statistics attributing the macroscopic growth effects to variations at each level.

## Results

To illustrate the problem, we use data from the city of Chicago.
Chicago’s has a highly dynamic demographic and economic history.
Between the 1850s and 1950s, the city’s population, pp, expanded rapidly, with growth largely concentrated in the urban core. More recently,
between the 1990 and 2020 censuses, the city’s population, experienced bursts of local growth and contraction, resulting in a net loss of approximately 40k residents. We report these dynamics for Chicago’s urban core (Cook county) between t=2014t=2014 and t′=2019t^{\prime}=2019 through the annualized population growth rate measured across census tracts tr, γpbg=ln⁡(ptr,t′/ptr,t)/Δ​t\gamma\_{p\_{\textrm{bg}}}=\ln(p\_{\textrm{tr},t^{\prime}}/p\_{\textrm{tr},t})/\Delta t (see Appendix A for details). In Fig. [1](https://arxiv.org/html/2511.06165v1#Sx1.F1 "Figure 1 ‣ Introduction ‣ Spatial Selection and the Multiscale Dynamics of Urban Change")A, we observe strong population growth in the east, along the lake shore, that is balanced by inland decline, mostly in the southern and western regions of the city. By contrast, we observe almost stagnant population growth at the MSA level at .025%.025\%, visualized in Fig [1](https://arxiv.org/html/2511.06165v1#Sx1.F1 "Figure 1 ‣ Introduction ‣ Spatial Selection and the Multiscale Dynamics of Urban Change")B. As demographic growth slows down across the world, this situation is becoming common of many other cities and regions.

Income growth has a somewhat different character. MSA-wide nominal income growth rate is measured at γm=3.42%\gamma\_{\textrm{m}}=3.42\%/year. The empirical growth rate is defined

|  |  |  |  |
| --- | --- | --- | --- |
|  | γj=Δ​ln⁡Ej​[yk]=ln⁡yj​t′−ln⁡yj​tΔ​t,\gamma\_{j}=\Delta\ln\textrm{E}\_{j}[y\_{k}]=\frac{\ln y\_{jt^{\prime}}-\ln y\_{jt}}{\Delta t}, |  | (1) |

with comparable amounts of spatial and distributional heterogeneity reported in Fig. [1](https://arxiv.org/html/2511.06165v1#Sx1.F1 "Figure 1 ‣ Introduction ‣ Spatial Selection and the Multiscale Dynamics of Urban Change")A and B. We report relative growth in sub-figure A, where Δ​γtr=γct−γtr\Delta\gamma\_{\textrm{tr}}=\gamma\_{\textrm{ct}}-\gamma\_{\textrm{tr}} to identify where income disparities are growing. We observe stronger growth inland, on the northwest regions of the city, slower to stagnant growth in the east along the lake, and lagging growth in the southern regions of the city.
This mismatch between aggregate economic and demographic growth motivates examining more granular, neighborhood level data, which more directly reflects individual experiences and residential decisions.

The crucial issue is whether the interplay between endogenous growth, where people’s real incomes increase, versus sorting, where people with different incomes are attracted or repelled differentially by location. As we will show, sorting (or spatial selection) affects aggregate growth whenever richer and poorer populations replace one another, even in the absence of endogenous income growth. Evidence of racial and economic displacement [[24](https://arxiv.org/html/2511.06165v1#bib.bib24), [25](https://arxiv.org/html/2511.06165v1#bib.bib25)] suggests that it may contribute significantly to aggregate economic growth rates in cities.

To measure these factors, we now analyze the statistics of population and income distribution across scales in Chicago. We start with the smallest possible units (block groups with populations ∼1,000\sim 1,000) and characterize each unit’s exact contribution to aggregate rates of change at larger scales. This will allow us to systematically identify a typology of growth patterns in different locations.
In principle, successive scales of aggregation can be identified flexibly to reflect the local character of the city. For our analysis here, we will use a standard hierarchy of nested scales defined by the US Census, which starts with block groups (bg) at the smallest scales, aggregated into census tracts (tr), communities (cm for Chicago communities and census places), and counties (ct) at the largest scales. The Price equation then provides a method for tabulating these selection effects at each scale, and aggregating them relative to the overall income growth.

The Price equation describes the temporal change in an average trait zjz\_{j}, aggregated in terms of subgroup trait zkz\_{k}. As we show in Appendix B1, the most straightforward trait assignment for our purposes is in terms of logarithmic income, z=ln⁡yz=\ln y. Then, income growth rates, γ=d​ln⁡yd​t\gamma=\frac{d\ln y}{dt}, are averages (aggregations) of variations of logarithmic income at lower levels. Making these scales explicit, the growth rate is defined as (Appendix A4)

|  |  |  |  |
| --- | --- | --- | --- |
|  | γjp≡Δ​Ej​[ln⁡yk]=∑k∈j(fk​t′​zk​t′−fk​t​zk​t),\gamma\_{j}^{p}\equiv\Delta\textrm{E}\_{j}[\ln y\_{k}]=\sum\_{k\in j}(f\_{kt^{\prime}}z\_{kt^{\prime}}-f\_{kt}z\_{kt}), |  | (2) |

where fk​t=pk​t/∑kpk​tf\_{kt}=p\_{kt}/\sum\_{k}p\_{kt} is the fraction of the population in unit kk at time tt. Another trait choice could be z=yz=y, where growth rates are aggregated from incomes [[26](https://arxiv.org/html/2511.06165v1#bib.bib26)].

|  |  |  |  |
| --- | --- | --- | --- |
|  | γjy≡Ej​[yk​Δ​ln⁡yk]/Ej​[yk]\gamma\_{j}^{y}\equiv\textrm{E}\_{j}[y\_{k}\Delta\ln y\_{k}]/\textrm{E}\_{j}[y\_{k}] |  | (3) |

The former decomposes growth in terms of population selection effects (hence the superscript) in an analysis consistent with the original formulation of the Price equation [[22](https://arxiv.org/html/2511.06165v1#bib.bib22), [27](https://arxiv.org/html/2511.06165v1#bib.bib27)] and will be discussed next. The latter decomposes income sorting effects its relationships to Eq. [2](https://arxiv.org/html/2511.06165v1#Sx2.E2 "In Results ‣ Spatial Selection and the Multiscale Dynamics of Urban Change") is discussed in the supplement.
Fig [1](https://arxiv.org/html/2511.06165v1#Sx1.F1 "Figure 1 ‣ Introduction ‣ Spatial Selection and the Multiscale Dynamics of Urban Change")C demonstrates that while these quantities generally predict the empirical growth rate well, there are some noticeably strong outliers, suggesting different observable selection effects between aggregation methods.

![Refer to caption](x2.png)


Figure 2: Schematic of 3-level decomposition in a typical community area with no population growth but positive income growth.
Between tracts (mid-level) the population rebalances from the low-income A to the high-income tract B. Between block groups (lowest level), populations and incomes are growing in tract B’s lower income areas, and populations are declining in tract A’s low income areas. These changes are recorded as selection effects and transmitted via averaging to the community level.

#### Multiscale Growth Decomposition

So far, we have discussed why attention to evidence on disaggregated growth rates is necessary for developing coherent narratives of change concerning people in organizational hierarchies, such as cities.
We have also introduced two methods of computing growth rate data, and have shown that standard aggregation methods erase much statistical and spatial variation in the data. We will now introduce the Price equation, the standard accounting device of evolutionary dynamics. The Price equation measures how a population-averaged trait zz changes over time as the result of contributions from changes across groupings of the population.
Crucially, it separates effects of population sorting, referred to as s​e​l​e​c​t​i​o​nselection, from all other effects that result in endogenous trait growth.
This enables an exact hierarchical decomposition of change in terms of contributions from nesting subgroups.
In the following, we apply this Price decomposition to log incomes, revealing the magnitude of neighborhood selection and the effects of these compositional changes on growth.

The aggregation in Eq. [2](https://arxiv.org/html/2511.06165v1#Sx2.E2 "In Results ‣ Spatial Selection and the Multiscale Dynamics of Urban Change") measures the population reweighting over time between subunits as a result of changes in local population.
In the Price equation, this is measured by wk≡exp⁡[γpk]=pk,t′/pk,tw\_{k}\equiv\ \exp[\gamma\_{p\_{k}}]=p\_{k,t^{\prime}}/p\_{k,t}.
To ecologists, this represents a way to measure the fitness of a subgroup (here a neighborhood).
This is a relative measure, which is commonly defined versus the average across all subgroups, wjw\_{j}, as w¯k=wk/wj\bar{w}\_{k}=w\_{k}/w\_{j}.
When w¯k>0\bar{w}\_{k}>0, subgroup kk is more attractive in that it has a more positive growth rate than the average, regardless of whether nominal growth is positive.
In this case, prevailing dynamics select for that trait, and the value of that trait becomes increasingly more represented in the population.

Here, we identify groups by spatial units such as census tracts, whereas the trait is log income, zj=Ej​[ln⁡yk]z\_{j}=\textrm{E}\_{j}[\ln y\_{k}], averaged over lower units kk.
In these terms, the Price equation restates Eq. [2](https://arxiv.org/html/2511.06165v1#Sx2.E2 "In Results ‣ Spatial Selection and the Multiscale Dynamics of Urban Change") as

|  |  |  |  |
| --- | --- | --- | --- |
|  | γjp=Ej​[w¯k​γkp]+covj​[w¯k,zk].\gamma\_{j}^{p}=\textrm{E}\_{j}\big[\bar{w}\_{k}\gamma\_{k}^{p}\big]+\textrm{cov}\_{j}\big[\bar{w}\_{k},z\_{k}\big]. |  | (4) |

This says that the average growth rate of the higher level unit is equal to the expectation over the reweighted growth rates, plus the covariance between fitness and log incomes across all lower level units. The t​r​a​n​s​m​i​s​s​i​o​ntransmission, given by the first term Tk→jp≡Ej​[w¯k​γkp]T\_{k\rightarrow j}^{p}\equiv E\_{j}[\bar{w}\_{k}\gamma\_{k}^{p}], measures the endogenous contribution of each subunit to the average growth of the larger unit, whereas s​e​l​e​c​t​i​o​nselection, given by the second term Sk→jp≡covj​[w¯k,zk]S\_{k\rightarrow j}^{p}\equiv\textrm{cov}\_{j}\big[\bar{w}\_{k},z\_{k}\big], measures the statistical effects of population sorting along log incomes between spatial units. When selection is positive (negative), populations concentrate in relatively higher (lower) income units, either through population loss (gain) in lower income areas or population gain (loss) in higher income areas. As a result, sorting across spatial units may increase the observed aggregate growth if the rebalancing concentrates population in higher-income areas.

The Price equation can be defined recursively, so that the growth rate of unit jj is described in terms of statistical effects among lower units kk and their subunits ll.
The Price equation for the growth rate of any subunit
is γkp=Tl→kp+Sl→kp\gamma\_{k}^{p}=T\_{l\rightarrow k}^{p}+S\_{l\rightarrow k}^{p}.
We substitute this into the transmission term of Eq. [4](https://arxiv.org/html/2511.06165v1#Sx2.E4 "In Multiscale Growth Decomposition ‣ Results ‣ Spatial Selection and the Multiscale Dynamics of Urban Change") to retrieve the two-level Price decomposition as γjp=Sk→jp+Sl→jp+Tl→jp\gamma\_{j}^{p}=S\_{k\rightarrow j}^{p}+S\_{l\rightarrow j}^{p}+\textrm{T}\_{l\rightarrow j}^{p}, where an index spanning more than one level implies averaging Xl→j=Ej​[Xl→k]X\_{l\rightarrow j}=\textrm{E}\_{j}[X\_{l\rightarrow k}].
This redefines a previously endogenous transmission term Tk→jpT\_{k\rightarrow j}^{p} in Eq. [4](https://arxiv.org/html/2511.06165v1#Sx2.E4 "In Multiscale Growth Decomposition ‣ Results ‣ Spatial Selection and the Multiscale Dynamics of Urban Change") in terms of selection driven by internal sorting, Sl→jpS\_{l\rightarrow j}^{p}, and transmission Tl→jpT\_{l\rightarrow j}^{p}.
Thus, a multi-level Price decomposition is the weighted sum over the selection effects at each level, transmitted to the level of the parent through population-weighted averaging.
Comparing population selection effects across scales then becomes a scalar difference between selection terms.

![Refer to caption](x3.png)


Figure 3:  Population selection on income varies widely across neighborhoods and scales. A. The raw income and population growth data are divided into three regions (contour lines). B. Local income selection effects transmitted to the community area level, mapped for the city of Chicago by region are computed from block group-level effects (left) and tract-level effects (right). The aggregate selection effect for each unit is amplified or hidden, depending on whether the selection is complementary (same-sign) or competing (opposite-sign).

Applying this to urban income data, the average growth rate of the MSA can then be disaggregated in terms of the terminal child, bg, and the three intermediate levels, tr, cm, and ct as

|  |  |  |  |
| --- | --- | --- | --- |
|  | γmp=Sct→mp+Scm→mp+Str→mp+Sbg→mp+Tbg→mp.\begin{split}\gamma\_{\textrm{m}}^{p}=&S\_{\textrm{ct}\rightarrow\textrm{m}}^{p}+S\_{\textrm{cm}\rightarrow\textrm{m}}^{p}+S\_{\textrm{tr}\rightarrow\textrm{m}}^{p}+S\_{\textrm{bg}\rightarrow\textrm{m}}^{p}+T\_{\textrm{bg}\rightarrow\textrm{m}}^{p}.\end{split} |  | (5) |

Here, local fitness are defined relative to the MSA, w¯k=wk/wm\bar{w}\_{k}=w\_{k}/w\_{m}, rather than the tract.
This expression measures the cumulative selection, measured between units at each level of organization, aggregated to the level of the MSA.

By construction, selection between levels is statistically independent, permitting a level-by-level analysis of selection statistics.
Fig. [2](https://arxiv.org/html/2511.06165v1#Sx2.F2 "Figure 2 ‣ Results ‣ Spatial Selection and the Multiscale Dynamics of Urban Change") visualizes a schematic community with positive income growth and a stagnating (aggregate) population.
The community is composed of tracts A and B of roughly equal population and income, both demonstrating income growth. In tract A, individuals sort into high-income block groups (while leaving low-income block groups), producing a positive covariance for tract A.
Meanwhile, other individuals sort themselves into low-income block groups in B, producing negative covariance for tract B. Assuming selection in A is stronger than B, positive selection is transmitted from block groups.
Imagine, however, the population of tract A shrinks as B grows. Because there are negligible income differences between A and B, this migration cannot be attributed to tract-level income sorting, producing negligibly small selection between tracts.
Aggregating local selection reveals considerable effects of population sorting on income growth, despite negligible aggregate population change.

This example illustrates how the Price equation reveals dynamical effects that standard aggregation measures overlook. Its recursive structure preserves multilevel spatial stratification, addressing a longstanding challenge in urban sociology of linking micro-ecological processes to macro-structural outcomes [[28](https://arxiv.org/html/2511.06165v1#bib.bib28), [23](https://arxiv.org/html/2511.06165v1#bib.bib23)].
Figure [3](https://arxiv.org/html/2511.06165v1#Sx2.F3 "Figure 3 ‣ Multiscale Growth Decomposition ‣ Results ‣ Spatial Selection and the Multiscale Dynamics of Urban Change") presents the Price equation defined for each community using real income and population growth data from Chicago’s urban core.
For interpretability, we express selection as a percentage relative to the county-wide growth rate, ωxp=Sxp/γctp∗100\omega\_{x}^{p}=S\_{x}^{p}/\gamma\_{\textrm{ct}}^{p}\*100.
Figure [3](https://arxiv.org/html/2511.06165v1#Sx2.F3 "Figure 3 ‣ Multiscale Growth Decomposition ‣ Results ‣ Spatial Selection and the Multiscale Dynamics of Urban Change")A highlights three spatial regions with consistent selection effects, while Fig. [3](https://arxiv.org/html/2511.06165v1#Sx2.F3 "Figure 3 ‣ Multiscale Growth Decomposition ‣ Results ‣ Spatial Selection and the Multiscale Dynamics of Urban Change")B shows their internal selection at the tract level (left), and within tracts across block groups (right).
Purple represents negative selection and orange positive.
In Region 1 (near north/northwest), selection is negative at the block-group level but positive across tracts, indicating residential sorting toward high-income tracts but low-income blocks—competing selection pressures across scales.
In Region 2, encompassing much of the near-west communities, selection is aligned across scales: individuals consistently sorted into high-income tracts and block groups inland, whereas in the downtown and near-south, sorting favored lower-income units.
Elsewhere, including most of Region 3, cross-scale selection is inconsistent, reflecting more complex sorting patterns.

![Refer to caption](x4.png)


Figure 4: Analyses of local selection enables a more systematic understanding of urban dynamics. A. Aggregate income and population growth data are complemented by selection, suggesting potential hypotheses of local change. B. Selection effects are spatially concentrated, with 20% of tracts (communities) accounting for 59% (64%) of overall selection. C. The average selection magnitude is larger in more populated counties. D. Selection magnitudes, ρjp\rho\_{j}^{p}, are the highest within tracts, however selection effects transmitted via the Price equation, ωjp\omega\_{j}^{p}, are the most consistent across communities in a county. Low transmitted selection effects indicate they largely counterbalance in the Chicago MSA.

#### Data-driven Hypotheses of Urban Change

Urban sociology has long emphasized that powerful groups promote physical separation from those they deem undesirable [[29](https://arxiv.org/html/2511.06165v1#bib.bib29), [30](https://arxiv.org/html/2511.06165v1#bib.bib30)], while spatial assimilation theory posits that individuals use socioeconomic resources to access better neighborhoods [[31](https://arxiv.org/html/2511.06165v1#bib.bib31)].
Both processes reflect nonrandom population sorting, which can masquerade as causal neighborhood effects on various outcomes, from crime to child health [[32](https://arxiv.org/html/2511.06165v1#bib.bib32), [33](https://arxiv.org/html/2511.06165v1#bib.bib33)].
Our analysis separates these selection effects from noise, providing insight into the dynamics of inequality in neighborhood attainment.

Fig. [3](https://arxiv.org/html/2511.06165v1#Sx2.F3 "Figure 3 ‣ Multiscale Growth Decomposition ‣ Results ‣ Spatial Selection and the Multiscale Dynamics of Urban Change")A combines local multilevel population selection, ωcmp=(Sbg→cmp+Str→cmp)/γctp\omega\_{\textrm{cm}}^{p}=(S\_{\textrm{bg}\rightarrow\textrm{cm}}^{p}+S\_{\textrm{tr}\rightarrow\textrm{cm}}^{p})/\gamma\_{\textrm{ct}}^{p}, with income and population growth data, to identify where residential decisions tangibly alter the landscape of incomes and inequality, revealing when segregation, gentrification, or suburbanization reinforce or offset one another. We observe a rich typology of situations. For example,
in case i.i. (more affluent lakefront communities) population growth was high but with mixed effects on relative income.
The mixed-to-negative income selection indicates that much of this migration is into low-income subareas, suggesting potential revitalization. Case i​iii. shows low population gains with relatively high income growth, coupled with strongly positive selection. This reflects higher income populations’ preference for higher-income areas, an instance of income concentration.
These dynamics contrast with i​i​i.iii. and i​v.iv. where populations are stagnating or declining.
In i​i​i.iii. (lower income southern communities), we observe relative income loss coupled with negative selection, signaling out-migration of relatively higher income residents. This is a pattern commonly discussed with the creation of concentrated poverty [[34](https://arxiv.org/html/2511.06165v1#bib.bib34), [23](https://arxiv.org/html/2511.06165v1#bib.bib23)]. Lastly, we observe income gains in some southwest neighborhoods in i​viv, along with competing selection but population stagnation. This suggests a more spatially complex, scale-dependent displacement of incumbent residents. Here, we observe micro-segregation inside affluent tracts: households move into high-income tracts (positive between-tract selection) but concentrate in their lower-income block groups (negative within-tract selection).
This pattern enables access to tract-level opportunities while reproducing fine-grained income segregation locally.

To measure the amount of overall selection variation in the data, we report the single-level selection magnitude ρtrp=|Sbg→trp|/γChip\rho\_{\textrm{tr}}^{p}=|S\_{\textrm{bg}\rightarrow\textrm{tr}}^{p}|/\gamma\_{\textrm{Chi}}^{p}. We find that selection is highly spatially clustered, as only 20% of tracts (communities, ρcmp\rho\_{\textrm{cm}}^{p}) account for 59% (64%) of all selection (Figure 4B).
While tract and community-level selection are concentrated similarly, Figure S2A shows that tract-level selection has wider variation and skew than community-level selection, indicating stronger local heterogeneity.
Accordingly, any model of residential selection must increase in complexity with finer spatial resolution, consistent with recent findings on neighborhood selection using information as a metric [[7](https://arxiv.org/html/2511.06165v1#bib.bib7)].
In Fig. [4](https://arxiv.org/html/2511.06165v1#Sx2.F4 "Figure 4 ‣ Multiscale Growth Decomposition ‣ Results ‣ Spatial Selection and the Multiscale Dynamics of Urban Change")C, we show that these selection magnitudes exhibit a superlinear scaling behavior when aggregated to the county level.
However, Appendix [D](https://arxiv.org/html/2511.06165v1#A4 "Appendix D Scaling Behavior of Selection ‣ Spatial Selection and the Multiscale Dynamics of Urban Change") shows that these effects vanish in the data when accounting for relative tract and county population.
Fig. [4](https://arxiv.org/html/2511.06165v1#Sx2.F4 "Figure 4 ‣ Multiscale Growth Decomposition ‣ Results ‣ Spatial Selection and the Multiscale Dynamics of Urban Change")D reports both the population-weighted average, ⟨ρjp⟩\langle\rho\_{j}^{p}\rangle and its standard deviation, σ​(ρjp)\sigma(\rho\_{j}^{p}) across spatial units, revealing the largest heterogeneity at the tract level at 13.6%13.6\%, with standard deviation of 15.9%15.9\%.

Despite this local richness, most variation vanishes when aggregated to the MSA level via the Price equation, yielding low cumulative selection.
The lower panel of Fig. [4](https://arxiv.org/html/2511.06165v1#Sx2.F4 "Figure 4 ‣ Multiscale Growth Decomposition ‣ Results ‣ Spatial Selection and the Multiscale Dynamics of Urban Change")D reports the empirical selection effects, ωjp\omega\_{j}^{p}, where opposing signs among sibling units offset.
Selection effects within tracts reduces aggregate growth by only 1.4%1.4\% while selection across communities contributes 3.3%3.3\%. Overall, selection effects within communities and across the MSA nearly balance, contributing an additional 2.1% increase to aggregate MSA income growth.

By treating spatial units as evolving subpopulations under selection, we measure both how prevailing incomes shape residential choices and how these choices, in turn, influence aggregate income growth.
Selection effects grow more heterogeneous and pronounced at finer spatial scales in our study but exhibit the greatest spatial coherence at the county level.
Put differently, residents most consistently prefer high-income community areas, while favoring generally lower-income block groups.

These results demonstrate that residential choices can be rigorously quantified by income, along with their aggregate effects on metropolitan growth dynamics.
Consistent with scale-sensitive segregation theory [[35](https://arxiv.org/html/2511.06165v1#bib.bib35)], we find large ⟨ρjp⟩\langle\rho\_{j}^{p}\rangle at the tract level, persistent ωjp\omega\_{j}^{p} within counties, and negligible ω\omega at the MSA scale—identifying the level at which population sorting by income most strongly operates.
The findings underscore the complexity that models of residential selection must capture to reproduce observed dynamics.
They also provide an exact quantitative framework for disentangling contextual effects from compositional sorting for any trait, not just income, thereby advancing explanatory models of urban change. Our approach pinpoints where sorting accumulates or cancels and identifies which sorting mechanisms are at play to explain observed changes in spatial inequality.
An analogous decomposition applies to Eq. [3](https://arxiv.org/html/2511.06165v1#Sx2.E3 "In Results ‣ Spatial Selection and the Multiscale Dynamics of Urban Change"), which measures income concentration more directly [[26](https://arxiv.org/html/2511.06165v1#bib.bib26)] and will be explored in future work.

## Discussion

In this paper, we demonstrated a novel application of the Price equation to disaggregate urban income growth in terms of residential selection effects across a spatial hierarchy connecting very small local communities (neighborhoods) to counties and their metropolitan area. We showed that the heterogeneity of income and population growth data is largely lost under aggregation, limiting quantitative analyses of local urban dynamics.
We then used the Price equation to derive a multi-level decomposition of income growth in terms of scale-dependent selection effects.
We showed that selection effects are spatially concentrated, fat-tailed, and exhibit basic scaling relationships.
We then demonstrated the use of this systematic in producing hypotheses for local socio-urban change when paired with income and population growth data.
We concluded by showing that despite this variation, selection effects largely cancel out on larger scales in Chicago, resulting in a small statistical effect on aggregate growth.

Stratified urban data analyses make explicit the coupling between local structural forces and the compositional evolution of metropolitan areas.
Future research could extend this framework by modeling how local institutional structures such as zoning, school district boundaries, and neighborhood-level political organization influence selection across space and scale [[36](https://arxiv.org/html/2511.06165v1#bib.bib36)].
These structures interact with other demographic characteristics such as race and class to shape residential mobility and, often, to reproduce segregation and concentrated poverty.
Evidence shows that, even at similar incomes, Black households face higher risks of downward neighborhood moves, with gentrification and displacement amplifying churn among lower-income renters [[37](https://arxiv.org/html/2511.06165v1#bib.bib37), [38](https://arxiv.org/html/2511.06165v1#bib.bib38), [39](https://arxiv.org/html/2511.06165v1#bib.bib39), [40](https://arxiv.org/html/2511.06165v1#bib.bib40), [31](https://arxiv.org/html/2511.06165v1#bib.bib31)].
Comparative analyses across metropolitan areas, before and after the pandemic, with varying degrees of fragmentation and segregation, would further clarify how these structural conditions affect the balance between spatial assimilation and place stratification.

Future research could also explore how local place identities, perceived neighborhood boundaries, and mental maps shape the spatial scale at which residential turnover occurs (e.g., boroughs in NYC, community areas in Chicago, micro-neighborhoods in LA). Prior work [[41](https://arxiv.org/html/2511.06165v1#bib.bib41), [42](https://arxiv.org/html/2511.06165v1#bib.bib42)] suggests that symbolic and cognitive boundaries, e.g., racial blindspots [[43](https://arxiv.org/html/2511.06165v1#bib.bib43)], may interact with formal governance structures to reinforce barriers to upward mobility and neighborhood attainment. This analysis could be extended to examine the bidirectional influence of residential choice and capital allocation through the dynamics of point of interest (POI) dependency networks [[44](https://arxiv.org/html/2511.06165v1#bib.bib44)], particularly as climate disasters influence dramatic population churn that persists post-recovery [[45](https://arxiv.org/html/2511.06165v1#bib.bib45)].
Ultimately, such work would inform policy at scales relevant to people and households to reduce inequities in neighborhood access and ensure that the benefits of (urban) growth are more equitably distributed.

Lastly, trait-based, multilevel decompositions can summarize emerging disaggregate trends in hierarchical economic datasets such as production [[46](https://arxiv.org/html/2511.06165v1#bib.bib46)], occupation networks [[47](https://arxiv.org/html/2511.06165v1#bib.bib47)], and infrastructure [[48](https://arxiv.org/html/2511.06165v1#bib.bib48)].
Revealing scale-dependent churn from shocks such as future pandemics, climate events, or the emergence of artificial intelligence will inform benchmarks for future disequilibrium economic [[49](https://arxiv.org/html/2511.06165v1#bib.bib49)] and infrastructure [[48](https://arxiv.org/html/2511.06165v1#bib.bib48)] models, improving our ability to predict out-of-sample structural responses in multi-scale economic systems.

## Achknowledgements

We thank Andrew Stier, and François Lafond for their discussions and comments on the manuscript.
This work is supported by the Department of Ecology and Evolution at the University of Chicago, and the Institute for New Economic Thinking at the University of Oxford.

### Author contribution

JTK and LMAB conceived the research. JTK designed the experiments, produced the figures, and developed the draft. JTK and LF produced the maps. All authors edited the manuscript.

## References

* Jackson [2009]
  T. Jackson, *Prosperity without growth?: The transition to a sustainable economy* (Sustainable Development Commission, 2009).
* Barro [1991]
  R. J. Barro, Economic growth in a cross section of countries, The Quarterly Journal of Economics 106, 407 (1991).
* Hairston *et al.* [1970]
  N. G. Hairston, D. W. Tinkle, and H. M. Wilbur, Natural selection and the parameters of population growth, The Journal of Wildlife Management , 681 (1970).
* Lee [2002]
  R. Lee, The demographic transition: three centuries of fundamental change, Journal of economic perspectives 17, 167 (2002).
* Kemp and Bettencourt [2023]
  J. T. Kemp and L. M. Bettencourt, Learning increases growth and reduces inequality in shared noisy environments, PNAS nexus 2, pgad093 (2023).
* Cholli *et al.* [2024]
  N. A. Cholli, S. N. Durlauf, R. Landersø, and S. Navarro, *Understanding the heterogeneity of intergenerational mobility across neighborhoods*, Tech. Rep. (National Bureau of Economic Research, 2024).
* Bettencourt *et al.* [2025]
  L. Bettencourt, I. Rodriguez, J. T. Kemp, and J. Lobo, Decoding the city: multiscale spatial information of urban income, arXiv preprint arXiv:2509.22954 (2025).
* Glaeser *et al.* [1995]
  E. L. Glaeser, J. Scheinkman, and A. Shleifer, Economic growth in a cross-section of cities, Journal of Monetary Economics 36, 117 (1995).
* Oosterhaven [2024]
  J. Oosterhaven, A decomposition of economic growth decompositions, [Annals of Regional Science 73, 1395 (2024)](https://doi.org/10.1007/s00168-024-01309-7), “disaggregating” version.
* Maestas *et al.* [2016]
  N. Maestas, K. J. Mullen, and D. Powell, The effect of population aging on economic growth, the labor force and productivity, NBER Working Paper (2016).
* Bloom *et al.* [2003]
  D. Bloom, D. Canning, and J. Sevilla, *The demographic dividend: A new perspective on the economic consequences of population change* (Rand Corporation, 2003).
* Hulten [2010]
  C. R. Hulten, Growth accounting, Handbook of the Economics of Innovation 2 (2010).
* Melitz and Polanec [2015]
  M. J. Melitz and S. Polanec, Dynamic olley-pakes productivity decomposition with entry and exit, The RAND Journal of Economics 46, 264 (2015).
* Duranton and Puga [2004]
  G. Duranton and D. Puga, Micro-foundations of urban agglomeration economies, in *Handbook of Regional and Urban Economics*, Vol. 4 (Elsevier, 2004) pp. 2063–2117.
* Anselin [1988]
  L. Anselin, *Spatial Econometrics: Methods and Models* (Springer, Dordrecht, 1988).
* Elhorst [2017]
  J. P. Elhorst, *Spatial Econometrics: From Cross-Sectional Data to Spatial Panels* (Springer, Cham, 2017).
* Rey *et al.* [2021]
  S. J. Rey, L. Anselin, D. Arribas-Bel, L. J. Wolf, W. Kang, and E. Knaap, Pysal: A python library of spatial analytical methods, in [*Handbook of Regional Science*](https://doi.org/10.1007/978-3-662-60723-7_120-1), edited by M. M. Fischer and P. Nijkamp (Springer, Cham, 2021) pp. 1–23.
* Manski [1993]
  C. F. Manski, Identification of endogenous social effects: The reflection problem, [The Review of Economic Studies 60, 531 (1993)](https://doi.org/10.2307/2298123).
* Helbing [2015]
  D. Helbing, Societal, economic, and technological complex systems, [Advances in Complex Systems 18, 1550025 (2015)](https://doi.org/10.1142/S0219525915500253).
* Chave [2013]
  J. Chave, The problem of pattern and scale in ecology: what have we learned in 20 years?, Ecology letters 16, 4 (2013).
* Carvalho [2014]
  V. M. Carvalho, From micro to macro via production networks, [Journal of Economic Perspectives 28, 23 (2014)](https://doi.org/10.1257/jep.28.4.23).
* Price [1972]
  G. R. Price, Fisher’s ‘fundamental theorem’ made clear, Annals of human genetics 36, 129 (1972).
* Bettencourt [2021]
  L. M. Bettencourt, *Introduction to urban science: evidence and theory of cities as complex systems* (MIT Press, 2021).
* Betancur [2002]
  J. J. Betancur, The politics of gentrification: The case of west town in chicago, Urban Affairs Review 37, 780 (2002).
* Hwang and Sampson [2014]
  J. Hwang and R. J. Sampson, Divergent pathways of gentrification: Racial inequality and the social order of renewal in chicago neighborhoods, American Sociological Review 79, 726 (2014).
* Olley and Pakes [1992]
  S. Olley and A. Pakes, The dynamics of productivity in the telecommunications equipment industry (1992).
* Frank [2012]
  S. A. Frank, Natural selection. iv. the price equation, Journal of Evolutionary Biology 25, 1002 (2012).
* McKenzie [1925]
  R. D. McKenzie, The Ecological Approach to the Study of the Human Community, in *The City* (The University of Chicago Press, Chicago, IL, 1925) pp. 63 – 79.
* Charles [2003]
  C. Z. Charles, The dynamics of racial residential segregation, Annual Review of Sociology 29, 167 (2003).
* Massey [1990]
  D. S. Massey, American apartheid: Segregation and the making of the underclass, American journal of sociology 96, 329 (1990).
* Massey *et al.* [1994]
  D. S. Massey, A. B. Gross, and K. Shibuya, Migration, segregation, and the geographic concentration of poverty, American Sociological Review 59, 425 (1994).
* Sampson [2008]
  R. J. Sampson, Moving to inequality: Neighborhood effects and experiments meet social structure, American journal of sociology 114, 189 (2008).
* Sampson *et al.* [2002]
  R. J. Sampson, J. D. Morenoff, and T. Gannon-Rowley, Assessing “neighborhood effects”: Social processes and new directions in research, Annual review of sociology 28, 443 (2002).
* Sampson [2012]
  R. J. Sampson, *Great American city: Chicago and the enduring neighborhood effect* (University of Chicago press, 2012).
* Reardon *et al.* [2008]
  S. F. Reardon, S. A. Matthews, D. O’sullivan, B. A. Lee, G. Firebaugh, C. R. Farrell, and K. Bischoff, The geographic scale of metropolitan racial segregation, Demography 45, 489 (2008).
* Crowder *et al.* [2012]
  K. Crowder, J. Pais, and S. J. South, Neighborhood diversity, metropolitan constraints, and household migration, American Sociological Review 77, 325 (2012).
* Crowder and South [2005]
  K. Crowder and S. J. South, Race, class, and changing patterns of migration between poor and nonpoor neighborhoods, American Journal of Sociology 110, 1715 (2005).
* South and Crowder [1997]
  S. J. South and K. D. Crowder, Escaping distressed neighborhoods: Individual, community, and metropolitan contextual effects on residential mobility, American Journal of Sociology 102, 1040 (1997).
* Quillian [1999]
  L. Quillian, Migration patterns and the growth of high-poverty neighborhoods, 1970-1990, American Journal of Sociology 105, 1 (1999).
* Desmond [2016]
  M. Desmond, *Evicted: Poverty and Profit in the American City* (Crown, New York, 2016).
* Logan and Collver [1983]
  J. R. Logan and O. A. Collver, Residents’ perceptions of suburban community differences, American Sociological Review , 428 (1983).
* Krysan and Bader [2007]
  M. Krysan and M. Bader, Perceiving the metropolis: Seeing the city through a prism of race, Social Forces 86, 699 (2007).
* Krysan and Bader [2009]
  M. Krysan and M. D. M. Bader, Racial blind spots: Black-white-Latino differences in community knowledge, Social Problems 56, 677 (2009).
* Yabe *et al.* [2025]
  T. Yabe, B. García Bulle Bueno, M. R. Frank, A. Pentland, and E. Moro, Behaviour-based dependency networks between places shape urban economic resilience, Nature Human Behaviour 9, 496 (2025).
* Park *et al.* [2024]
  S. Park, T. Yabe, and S. V. Ukkusuri, Post-disaster recovery policy assessment of urban socio-physical systems, Computers, Environment and Urban Systems 114, 102184 (2024).
* Bacilieri *et al.* [2023]
  A. Bacilieri, A. Borsos, P. Astudillo-Estevez, and F. Lafond, Firm-level production networks: what do we (really) know, INET Oxford Working Paper (2023).
* del Rio-Chanona *et al.* [2021]
  R. M. del Rio-Chanona, P. Mealy, M. Beguerisse-Díaz, F. Lafond, and J. D. Farmer, Occupational mobility and automation: a data-driven network model, Journal of the Royal Society Interface 18, 20200898 (2021).
* Sutradhar *et al.* [2024]
  U. Sutradhar, L. Spearing, and S. Derrible, Depopulation and associated challenges for us cities by 2100, Nature Cities 1, 51 (2024).
* Wiese *et al.* [2024]
  S. Wiese, J. Kaszowska-Mojsa, J. Dyer, J. Moran, M. Pangallo, F. Lafond, J. Muellbauer, A. Calinescu, and J. D. Farmer, Forecasting macroeconomic dynamics using a calibrated data-driven agent-based model, arXiv preprint arXiv:2409.18760 (2024).
* Guvenen *et al.* [2021]
  F. Guvenen, F. Karahan, S. Ozkan, and J. Song, What do data on millions of us workers reveal about lifecycle earnings dynamics?, Econometrica 89, 2303 (2021).
* Balk [2008]
  B. M. Balk, [*Price and Quantity Index Numbers: Models for Measuring Aggregate Change and Difference*](https://doi.org/10.1017/CBO9780511810178) (Cambridge University Press, Cambridge, 2008).
* Kemp and Bettencourt [2022]
  J. T. Kemp and L. M. Bettencourt, Statistical dynamics of wealth inequality in stochastic models of growth, Physica A: Statistical Mechanics and its Applications 607, 128180 (2022).
* Bettencourt [2013]
  L. M. Bettencourt, The origins of scaling in cities, science 340, 1438 (2013).

## Supplementary Material

Annual population and income distribution estimates at the census block group (bg) level are retrieved from the American Community Survey (ACS).
We compute changes in population and income as annualized growth rates to build spatial distributions of net migration and income growth.
We compute population growth rate γpbg\gamma\_{p\_{\textrm{bg}}} for block group bg with population pbgp\_{\textrm{bg}}, as the log ratio in population between the final and initial year, as γpbg=(1/Δ​t)​ln⁡(pbg,t′/pbg,t)\gamma\_{p\_{\textrm{bg}}}=(1/\Delta t)\ln(p\_{\textrm{bg},t^{\prime}}/p\_{\textrm{bg},t}), where t′=2019,t=2014,t^{\prime}=2019,t=2014, and Δ​t=t′−t=5\Delta t=t^{\prime}-t=5 years.
We compute these growth rates similarly for larger spatial scales, such as tract (tr), communities (cm, encompassing City of Chicago community areas and Illinois census designated places), county (ct), and MSA (m), by first summing populations among sibling units in a parent unit (Appendix A2).
We find that the distribution of population growth rates for all block groups in the MSA is fat-tailed, fitted with a Student-t distribution with mean of −0.2%-0.2\% (Fig [5](https://arxiv.org/html/2511.06165v1#A1.F5 "Figure 5 ‣ Appendix A Dataset Generation ‣ Spatial Selection and the Multiscale Dynamics of Urban Change")).
We map the population growth rates at the tract level for a most of Cook County in Fig. [1](https://arxiv.org/html/2511.06165v1#Sx1.F1 "Figure 1 ‣ Introduction ‣ Spatial Selection and the Multiscale Dynamics of Urban Change")A.

The definition for the approximate average income of a block group, ybgy\_{\textrm{bg}}, is estimated from the midpoint expectation value of ACS income histogram data, where the top income bin is set to $​400\mathdollar 400k (Appendix A).
The annualized growth rate in incomes for a block group is computed similarly as before, γbg=(1/Δ​t)​ln⁡(ybg,t′/ybg,t)\gamma\_{\textrm{bg}}=(1/\Delta t)\ln(y\_{\textrm{bg},t^{\prime}}/y\_{\textrm{bg},t}).
Nominal income growth rates are also fat-tailed, in agreement with cross-sectional studies of income [[50](https://arxiv.org/html/2511.06165v1#bib.bib50)], and are described by a t distribution with mean 4.78%4.78\%.
For readability, we report growth rates relative to the county as Δ​γtr=γtr−γct\Delta\gamma\_{\textrm{tr}}=\gamma\_{\textrm{tr}}-\gamma\_{\textrm{ct}}, where γct=Ect​[γtr]\gamma\_{\textrm{ct}}=\textrm{E}\_{\textrm{ct}}[\gamma\_{\textrm{tr}}].

We show in Fig. [1](https://arxiv.org/html/2511.06165v1#Sx1.F1 "Figure 1 ‣ Introduction ‣ Spatial Selection and the Multiscale Dynamics of Urban Change")B that this rich heterogeneity is lost under aggregation, as the variation in population and growth shrinks as we examine the population statistics at larger levels of aggregation.
We find that the distribution of population growth rates for all block groups in the MSA is fat-tailed, fitted with a Student-t distribution with mean of −0.2%-0.2\% (Fig [5](https://arxiv.org/html/2511.06165v1#A1.F5 "Figure 5 ‣ Appendix A Dataset Generation ‣ Spatial Selection and the Multiscale Dynamics of Urban Change")).
We find that the distribution of population growth rates for all block groups in the MSA is fat-tailed, fitted with a Student-t distribution with mean of −0.2%-0.2\% (Fig [5](https://arxiv.org/html/2511.06165v1#A1.F5 "Figure 5 ‣ Appendix A Dataset Generation ‣ Spatial Selection and the Multiscale Dynamics of Urban Change")).

| Variable | Name/Description |
| --- | --- |
| pjp\_{j} | Population of spatial unit jj. |
| yi​xy\_{ix} | Income bin ii of unit xx; when ii is excluded, this is the average income over unit xx. |
| zjz\_{j} | Log average income of unit jj. |
| wjw\_{j} | Absolute fitness of unit jj. |
| w¯j\bar{w}\_{j} | Relative fitness of unit jj. |
| γj\gamma\_{j} | Empirical growth rate of unit jj. |
| γjp\gamma\_{j}^{p} | Population-weighted growth rate of unit jj. |
| γjy\gamma\_{j}^{y} | Income-weighted growth rate of unit jj. |
| Sk→jpS\_{k\rightarrow j}^{p} | Selection along incomes aggregated from units kk to jj. If the subscript spans more than one level, it is implied that Sl→jp=Ej​[Sl→kp]S\_{l\rightarrow j}^{p}=\mathrm{E}\_{j}\!\left[S\_{l\rightarrow k}^{p}\right]. |
| ωjp\omega\_{j}^{p} | Selection within unit jj normalized by the terminal parent’s growth rate. In Fig. 3, the terminal parent is Cook County; in Fig. 4, it is the Chicago MSA. |
| ρjp\rho\_{j}^{p} | Selection magnitude of unit jj normalized by terminal parent growth. In Fig. 4, the terminal parent is the Chicago MSA. |

Table 1: Model variables and their definitions.

## Appendix A Dataset Generation

To generate the dataset, we read in population and income distribution data from the ACS survey, which is available at the tract level starting in 2010, and available from the block group level between 2014-2023.
Following the 2020 census, the boundaries of some tracts and block groups were redrawn.
Tract and block group definitions are therefore not guaranteed to align between 2019 and 2020.
This break conveniently aligns with major productivity and migration shifts during the COVID pandemic in 2020.
As such, the analysis in this paper is conducted primarily using data between 2014 and 2019.

![Refer to caption](x5.png)


Figure 5: Income and population growth rate data reported between the 2014-2019 period. A) Population and income growth rates are symmetric and fat-tailed, while log incomes are fit with a Gaussian distribution. B) Community-level maps demonstrate that populations were concentrated on the north side and far-west side, however most population growth was measured along the eastern lakefron. Incomes were concentrated along the lakefront in 2014, however most income growth was observed inland in the northwest side neighborhoods, and southwest side communities.

### A.1 Data retrieval

The data provided by the ACS are assigned, at its most granular level, to spatial units called census block groups. Block groups (B), with subscript bg are defined by a FIPS serial code, and its geographic boundaries are by the spatial coordinates of the indices of its shapefile polygons.
We retrieve the population of a block groups using the API code B​01003​\_​001​EB01003\\_001E, the number of households with code B​11001​\_​001​EB11001\\_001E, and the persons per household as B​25010​\_​001​EB25010\\_001E.
The income bin counts in the ACS data are computed by household, so we estimate population using unit-wide household estimates, denoted hbgh\_{\textrm{bg}}, weighed by the number of people per household, ρbg\rho\_{\textrm{bg}}
The population is computed as the product of these quantities, pbg=hbg∗ρbgp\_{\textrm{bg}}=h\_{\textrm{bg}}\*\rho\_{\textrm{bg}}.
For block groups with zero population, which could be the case for industrial corridors, bodies of water, or airports, we manually assert pbg=0p\_{\textrm{bg}}=0 (in these cases, the persons per household data is set by the Census Bureau to a sentinel value of -666…) .
In aggregate we find generally negligible qualitative differences between the distribution of raw population counts, and population counts computed from density adjusted household counts.

We could similarly read in such values at the tract level, denoted in this text as tr (T), the county level, ct (C), or the state level, st (S).
However, to ensure that population and income counts are consistent across scales, we aggregate such values directly from the block group level in a process described in the following section.
We introduce an intermediate level of aggregation, the community, denoted cm, a unit of aggregation reported as community areas for the City of Chicago, and as census designated places in non-Chicago municipalities throughout the state.
The spatial boundaries at this level of aggregation are not standardized in ACS data such that tracts may span more than one community area, and census places span more than one county.
We match tracts to the community in which lies the centroid of the tract.
Communities that span more than one county at partitioned along the counties’ boundaries, so as to partition the population dynamics generally between counties.
For example, Naperville, IL, which spans DuPage and Will County, is partitioned into ”NAPERVILLE (DUPAGE)” and ”NAPERVILLE (WILL)” in the data.
Here, we study data from the Illinois-side of the Chicago MSA, which includes Chicago’s 77 community areas, as well municipalities throughout Cook, DuPage, Kane, McHenry, Will, DeKalb, and Kendall counties.

We read in the income bin data at the block-group level, from ACS codes B​19001​\_​0​X​X​EB19001\\_0XXE, where X​XXX runs from 02 to 17.
We assign the income value of the bin to the midpoint of the range the bin spans.
We set the midpoint of the highest income bin, >$​250​K>\mathdollar 250K, to be $​400​K\mathdollar 400K.
Generally, this value is arbitrary, but is selected to balance between a good fit of income distribution data under a $​300​K\mathdollar 300K midpoint, and empirically fat tail of incomes given by $​500​K\mathdollar 500K.
The effects studied in this paper are determined mostly by the rank-order of incomes, rather than the length of the tail.
Therefore, estimating a precise tail isn’t critical to the results, so a precise estimate is beyond the scope of this work.
For every block group, denoted bg, we compute the average income for every spatial unit.
Consider incomes yiy\_{i} in bins of population pip\_{i} reported in number of people for spatial unit kk.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ybg=∑ipbg,i​ybg,i∑jpbg,j,y\_{\textrm{bg}}=\sum\_{i}\frac{p\_{\textrm{bg},i}y\_{\textrm{bg},i}}{\sum\_{j}p\_{\textrm{bg},j}}, |  | (6) |

where the sum is taken over income bins indexed by ii.

### A.2 Aggregation

For all block groups bg in tract tr, which are matched using the components of the full 11-digit serial code FIPS code (organized by SSCCCTTTTTB), the population is aggregated br→tr\textrm{br}\rightarrow\textrm{tr} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ptr=∑bg∈trpbg,p\_{\textrm{tr}}=\sum\_{\textrm{bg}\in\textrm{tr}}p\_{\textrm{bg}}, |  | (7) |

where belongingness is determined by common FIPS S,C, and T digits among block groups.
This aggregation is similarly defined from tracts to communities, tr→cm\textrm{tr}\rightarrow\textrm{cm}, communities to counties as cm→ct\textrm{cm}\rightarrow\textrm{ct}, and from counties to states ct→st\textrm{ct}\rightarrow\textrm{st}.
Note that community areas are not defined in the FIPS code, and must be identified through the aforementioned geographic matching, both from tracts to community areas, and community areas to counties.
In general, a metropolitan statistical area (MSA) can span more than one state, st→m\textrm{st}\rightarrow\textrm{m}.
However, for both simplicity and because the Chicago MSA, the predominant focus of this paper, lies mostly in Illinois, we only aggregate counties within Illinois.

We further define two methods of aggregating incomes, by which we average among children within a spatial unit, and then introduce three methods for aggregating growth rates.
For quantity xx, we compute the expectation value as the population-weighted average across spatial units within a parent unit of aggregation as Ej​[xk]=∑k∈j(pk/pj)​xkE\_{j}[x\_{k}]=\sum\_{k\in j}(p\_{k}/p\_{j})x\_{k}.

Here, we study the statistics of both incomes and log incomes.
We compute the income of a parent unit from its children in two ways.
First, to aggregate the income in the most standard way, here considered the empirical income, we take the expectation value of incomes across its children (equivalent the expectation value of the sum over child bins).
This is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | yj≡Ej​[yk]=∑k∈jpkpj​yk.y\_{j}\equiv\textrm{E}\_{j}[y\_{k}]=\sum\_{k\in j}\frac{p\_{k}}{p\_{j}}y\_{k}. |  | (8) |

We also aggregate the log income as

|  |  |  |  |
| --- | --- | --- | --- |
|  | zj=Ej​[ln⁡yk]=∑k∈jpkpj​ln⁡ykz\_{j}=\textrm{E}\_{j}[\ln y\_{k}]=\sum\_{k\in j}\frac{p\_{k}}{p\_{j}}\ln y\_{k} |  | (9) |

This definition differs from the log of Eq. [8](https://arxiv.org/html/2511.06165v1#A1.E8 "In A.2 Aggregation ‣ Appendix A Dataset Generation ‣ Spatial Selection and the Multiscale Dynamics of Urban Change"), up to Jensen’s inequality, and is not a standard method for aggregating incomes or growth rates.
However, we show that this aggregation encodes informative population dynamical data, measured through changes in population.

### A.3 Population growth statistics

We measure the change in population of a block group between two years t<t′t<t^{\prime} with the compound growth rate over the time period.
From the number of households, the population growth rate is computed over the interval Δ​t=t′−t\Delta t=t^{\prime}-t as

|  |  |  |  |
| --- | --- | --- | --- |
|  | γpbg≡1Δ​t​ln⁡pbg,t′pbg,t=ln⁡pbg,t′−ln⁡pbg,tΔ​t=Δ​ln⁡pbgΔ​t.\gamma\_{p\_{\textrm{bg}}}\equiv\frac{1}{\Delta t}\ln\frac{p\_{\textrm{bg},t^{\prime}}}{p\_{\textrm{bg},t}}=\frac{\ln p\_{\textrm{bg},t^{\prime}}-\ln p\_{\textrm{bg},t}}{\Delta t}=\frac{\Delta\ln p\_{\textrm{bg}}}{\Delta t}. |  | (10) |

This provides an intuitive measure for population change across arbitrary timescales.
The empirical growth rate is computed for higher levels of aggregation by first aggregating incomes, then computing growth rates.
The growth rates in incomes across Chicago city proper are visualized in [1](https://arxiv.org/html/2511.06165v1#Sx1.F1 "Figure 1 ‣ Introduction ‣ Spatial Selection and the Multiscale Dynamics of Urban Change")A.
We find that, although the population growth rate across all of Cook County, converted from households, is around −.025%-.025\%, we see from the figure that the real changes are highly heterogeneous.

A less common, but useful quantity is the reproductive fitness of a spatial unit.
The fitness measures the relative population between timesteps, and is simply the exponential of the growth rate.
It is a positive semi-definite quantity defined

|  |  |  |  |
| --- | --- | --- | --- |
|  | wbg=pbg,t′pbg,t.w\_{\textrm{bg}}=\frac{p\_{\textrm{bg},t^{\prime}}}{p\_{\textrm{bg},t}}. |  | (11) |

We can compute the fitness across sibling spatial units by taking the ratio of its fitness to its nnth parent.
For example, we could compute the fitness of a block group relative to all other block groups in its county by computing

|  |  |  |  |
| --- | --- | --- | --- |
|  | w¯bg=wbgwct=exp​[γbg−γtr]\bar{w}\_{\textrm{bg}}=\frac{w\_{\textrm{bg}}}{w\_{\textrm{ct}}}=\textrm{exp}[\gamma\_{\textrm{bg}}-\gamma\_{\textrm{tr}}] |  | (12) |

There is notational ambiguity as to which value a blockgroup is normalized, so it will always be specified in text.
These two measures of population change will be used throughout the analysis.

### A.4 Growth statistics

So far, we have defined income and population aggregation methods, and some statistical measures of population dynamics.
In this section, we compute growth dynamics for incomes.
We compute the empirical growth rate for that spatial unit across time span Δ​t=t′−t\Delta t=t^{\prime}-t as the difference in the logarithm of empirical incomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | γj≡Δ​ln⁡Ej​[yk]=ln⁡yj​t′−ln⁡yj​tΔ​t\gamma\_{j}\equiv\Delta\ln\textrm{E}\_{j}[y\_{k}]=\frac{\ln y\_{jt^{\prime}}-\ln y\_{jt}}{\Delta t} |  | (13) |

Assume Δ​t=1\Delta t=1 for brevity. In the analysis in the main text, Δ​t=5​y​r​s\Delta t=5yrs as the data is analyzed in the 2014-19 span, but can be in principle any value.

To study growth in block groups where no aggregation has been performed, the empirical growth rate serves as the only growth quantity.
However, for studying the growth statistics of larger spatial units such as tracts and beyond, we have several choices.
Consider the weights

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕk=pk​yk∑k′∈jpk′​yk′;fk=pk∑k′∈jpk′.\phi\_{k}=\frac{p\_{k}y\_{k}}{\sum\_{k^{\prime}\in j}p\_{k^{\prime}}y\_{k^{\prime}}};\hskip 7.11317ptf\_{k}=\frac{p\_{k}}{\sum\_{k^{\prime}\in j}p\_{k^{\prime}}}. |  | (14) |

The first weight defines an expectation value weighed additionally by income, whereas the second weight defines a standard population-weighted average.

Using these two weighting schemes, we now define the aggregation methods. The first option is to aggregate incomes according to Eq. [8](https://arxiv.org/html/2511.06165v1#A1.E8 "In A.2 Aggregation ‣ Appendix A Dataset Generation ‣ Spatial Selection and the Multiscale Dynamics of Urban Change").
Then, the growth rate is computed

|  |  |  |  |
| --- | --- | --- | --- |
|  | γjy≡Ej​[yk​Δ​ln⁡yk]/Ej​[yk]=∑k∈jϕk​γk\gamma\_{j}^{y}\equiv\textrm{E}\_{j}[y\_{k}\Delta\ln y\_{k}]/\textrm{E}\_{j}[y\_{k}]=\sum\_{k\in j}\phi\_{k}\gamma\_{k} |  | (15) |

This measure explicitly considers the context of growth by factoring in the nominal income value.
This method is standard in the capital allocation literature [[26](https://arxiv.org/html/2511.06165v1#bib.bib26)], and involves an expectation over the empirical growth rates, weighed by their income.
Note that we explicitly weigh by the initial population composition, consistent with a Laspeyres aggregation scheme, whereas a Paasche aggregation would instead weigh by the final population composition [[51](https://arxiv.org/html/2511.06165v1#bib.bib51)].
The distinction is analogous to that between base-weighted and current-weighted index numbers in price and productivity measurement. Under the Laspeyres aggregation, aggregate growth reflects changes in incomes while holding the population structure fixed at its initial distribution, thereby isolating within-unit changes. In contrast, the Paasche formulation evaluates growth using the end-of-period composition, incorporating realized reallocation or sorting effects. It measures how shifts in population shares toward higher or lower income areas contribute to overall change.

In this paper, we adopt the Laspeyres specification so that compositional effects arising from population reweighting can later be identified explicitly through a Price decomposition.
Thus defines the second aggregation method.
We to first aggregate log income according to Eq. [9](https://arxiv.org/html/2511.06165v1#A1.E9 "In A.2 Aggregation ‣ Appendix A Dataset Generation ‣ Spatial Selection and the Multiscale Dynamics of Urban Change"), an approach not standard in the economics literature, then compute the growth as a difference using the standard weights

|  |  |  |  |
| --- | --- | --- | --- |
|  | γjp​=​Δ​Ej​[ln⁡yk]=∑k[fk​t′​zk​t′−fk​t​zk​t].\gamma\_{j}^{p}\textrm{=}\Delta\textrm{E}\_{j}[\ln y\_{k}]=\sum\_{k}\big[f\_{kt^{\prime}}z\_{kt^{\prime}}-f\_{kt}z\_{kt}\big]. |  | (16) |

Note that this explicitly re-weights the growth of each spatial unit by its population between time steps. As we will see later, this allows for an explicit retrieval of population sorting along incomes using the Price equation.

These two calculations differ particularly by the order in which the logarithm and average are applied.
When growth rates are small, we can apply the first order approximation yk​Δ​ln⁡yk≈Δ​yky\_{k}\Delta\ln y\_{k}\approx\Delta y\_{k}.
Applying this substitution this, we find that

|  |  |  |
| --- | --- | --- |
|  | γky≈E​[Δ​yk]E​[yk]≈Δ​ln⁡E​[yk],\gamma^{y}\_{k}\approx\frac{\textrm{E}[\Delta y\_{k}]}{\textrm{E}[y\_{k}]}\approx\Delta\ln\textrm{E}[y\_{k}], |  |

This final expression states that the income-weighted aggregagte growth rate approximates to the first order [13](https://arxiv.org/html/2511.06165v1#A1.E13 "In A.4 Growth statistics ‣ Appendix A Dataset Generation ‣ Spatial Selection and the Multiscale Dynamics of Urban Change").
This provides some theoretical justification for the close fit between empirical and income-weighted growth rates in Fig. [1](https://arxiv.org/html/2511.06165v1#Sx1.F1 "Figure 1 ‣ Introduction ‣ Spatial Selection and the Multiscale Dynamics of Urban Change")C of the main text, and distinguishes the weighting schemes in Eq. [14](https://arxiv.org/html/2511.06165v1#A1.E14 "In A.4 Growth statistics ‣ Appendix A Dataset Generation ‣ Spatial Selection and the Multiscale Dynamics of Urban Change") differ to higher order by Jensen’s inequality.

![Refer to caption](x6.png)


Figure 6: Income and population growth data is highly correlated and heterogeneous A) Selection effects within community areas (purple) and tracts (orange) are fat tailed and skewed, suggesting spatial correlations or spillover effects between units. Local heterogeneity and correlations in ACS income and population growth data at the tract level is lost when aggregating to community areas. Fat tails (above) match a high degree of concentration in a subset of the population (below). B) Aggregating income and log income reveal distributions reveal differing growth statistics. C) Differences between aggregated growth statistics and standard, empirical measures of growth encode information about growth dynamics.

## Appendix B Multiscale growth

In this appendix, we define the price equation in terms of the growth rate and fitness expressions derived in the previous sections.

### B.1 Price equation decomposition of log incomes

For an average trait zj=Ej​[ln⁡yk]z\_{j}=\textrm{E}\_{j}[\ln y\_{k}] , The price equation states that.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Ej​[ln⁡yk]=1wj​cov​[wk,zk]+1wj​E​[wk​zk].\mathrm{\Delta}\textrm{E}\_{j}[\ln y\_{k}]=\tfrac{1}{w\_{j}}\textrm{cov}[w\_{k},z\_{k}]+\tfrac{1}{w\_{j}}\textrm{E}[w\_{k}z\_{k}]. |  | (17) |

If we assume Δ​t=1\Delta t=1, it follows that Δ​⟨ln⁡y⟩j=γjp\Delta\langle\ln y\rangle\_{j}=\gamma^{p}\_{j}. As explained in the main text, this expression decomposes the expectation value over growth rates (the average of log quantities) into compositional changes between units, the selection term, and endogenous shifts in that quantity in each unit (the transmission term. It is important to note that a log incone, zjz\_{j} is an average over log incomes, and explicitly not the log of an average over incomes. Most precisely, its written as

|  |  |  |
| --- | --- | --- |
|  | zj=∑l∈kfk​E​[ln⁡yl]k.z\_{j}=\sum\_{l\in k}f\_{k}\textrm{E}[\ln y\_{l}]\_{k}. |  |

For the terminal child unit (in our case, the block group), zj=ln⁡yjz\_{j}=\ln y\_{j}
Assuming kk is not the terminal child, we can define the Price equation for each growth term in the transmission term as

|  |  |  |  |
| --- | --- | --- | --- |
|  | γkp=1wk​cov​[wl,zl]+1wκ​E​[wl​γlp].\gamma\_{k}^{p}=\tfrac{1}{w\_{k}}\textrm{cov}[w\_{l},z\_{l}]+\tfrac{1}{w\_{\kappa}}\textrm{E}[w\_{l}\gamma\_{l}^{p}]. |  | (18) |

We can plug this expression into Eq [17](https://arxiv.org/html/2511.06165v1#A2.E17 "In B.1 Price equation decomposition of log incomes ‣ Appendix B Multiscale growth ‣ Spatial Selection and the Multiscale Dynamics of Urban Change") to retrieve

|  |  |  |  |
| --- | --- | --- | --- |
|  | γjp=1wj​covj​[wk,zk]+1wj​Ej​[covk​[wl,zl]+Ek​[wl​γlp]].\gamma\_{j}^{p}=\tfrac{1}{w\_{j}}\textrm{cov}\_{j}\big[w\_{k},z\_{k}\big]+\tfrac{1}{w\_{j}}\textrm{E}\_{j}\big[\textrm{cov}\_{k}[w\_{l},z\_{l}]+\textrm{E}\_{k}[w\_{l}\gamma\_{l}^{p}]\big]. |  | (19) |

Now that we have a concise definition for the two-level decomposition, we can describe the decomposition for the dataset across multiple levels. Consider block groups, denoted bg, nested in tracts, denoted tr, nested in community areas, denoted cm, nested in counties, denoted ct, nested in the Illinois-side MSA, denoted m, we can define the decomposition for log incomes (via the Price equation) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | γmp=Em,ct,cm,tr​[w¯bg​γbgp]+Em,ct,cm​[covtr​(w¯bg,zbg)]+Em,ct​[covcm​(w¯tr,ztr)]+Em​[covct​(w¯cm,zcm)]+covm​(w¯ct,zct).\begin{split}\gamma\_{\textrm{m}}^{p}=&\textrm{E}\_{\textrm{m,ct,cm,tr}}\big[\bar{w}\_{\textrm{bg}}\gamma\_{\textrm{bg}}^{p}\big]+\textrm{E}\_{\textrm{m,ct,cm}}\Big[\textrm{cov}\_{\textrm{tr}}\big(\bar{w}\_{\textrm{bg}},z\_{\textrm{bg}}\big)\Big]\\ &+\textrm{E}\_{\textrm{m,ct}}\Big[\textrm{cov}\_{\textrm{cm}}\big(\bar{w}\_{\textrm{tr}},z\_{\textrm{tr}}\big)\Big]+\textrm{E}\_{\textrm{m}}\Big[\textrm{cov}\_{\textrm{ct}}\big(\bar{w}\_{\textrm{cm}},z\_{\textrm{cm}}\big)\Big]\\ &+\textrm{cov}\_{\textrm{m}}\big(\bar{w}\_{\textrm{ct}},z\_{\textrm{ct}}\big).\end{split} |  | (20) |

Here, the fitnesses are normalized to the MSA, such that w¯j=wj/wm\bar{w}\_{j}=w\_{j}/w\_{\textrm{m}}.

A similar multiscale decomposition can be defined for Eq. [15](https://arxiv.org/html/2511.06165v1#A1.E15 "In A.4 Growth statistics ‣ Appendix A Dataset Generation ‣ Spatial Selection and the Multiscale Dynamics of Urban Change"), where the decomposition is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | γjy=Ej​[γky]+covj​[fyk,yk],\gamma\_{j}^{y}=\textrm{E}\_{j}[\gamma\_{k}^{y}]+\textrm{cov}\_{j}[f\_{y\_{k}},y\_{k}], |  | (21) |

where fyk=yk/yjf\_{y\_{k}}=y\_{k}/y\_{j}.
This quantity measures the relationship between incomes and growth rates, and is closely related to the emergence of inequality [[52](https://arxiv.org/html/2511.06165v1#bib.bib52)].
The full decomposition is then

|  |  |  |  |
| --- | --- | --- | --- |
|  | γmy=Em,ct,cm,tr​[γbgy]+Em,ct,cm​[covtr​[fybg,ybg]]+Em,ct​[covcm​[fytr,ytr]]+Em​[covct​[fycm,ycm]]+covm​[fyct,yct].\begin{split}\gamma\_{\textrm{m}}^{y}=&\textrm{E}\_{\textrm{m,ct,cm,tr}}\big[\gamma\_{\textrm{bg}}^{y}\big]+\textrm{E}\_{\textrm{m,ct,cm}}\Big[\textrm{cov}\_{\textrm{tr}}[f\_{y\_{\textrm{bg}}},y\_{\textrm{bg}}]\Big]\\ &+\textrm{E}\_{\textrm{m,ct}}\Big[\textrm{cov}\_{\textrm{cm}}[f\_{y\_{\textrm{tr}}},y\_{\textrm{tr}}]\Big]+\textrm{E}\_{\textrm{m}}\Big[\textrm{cov}\_{\textrm{ct}}[f\_{y\_{\textrm{cm}}},y\_{\textrm{cm}}]\Big]\\ &+\textrm{cov}\_{\textrm{m}}[f\_{y\_{\textrm{ct}}},y\_{\textrm{ct}}].\end{split} |  | (22) |

We analyze the relationship between income selection effects and changes in the Gini index for spatial, computed is Δ​Gtr→cm=Gt′−Gt\Delta G\_{\textrm{tr}\rightarrow\textrm{cm}}=G\_{t^{\prime}}-G\_{t}
The Gini index is computed for a spatial unit by applying the standard Lorenz curve method to the child units’ income data at the initial and final timestep.
We find that selection predicts change in Gini, that is more positive selection predicts increases to inequality, with an r2=.5r^{2}=.5 across communities and r2=.42r^{2}=.42 across tracts.

We also partitioned the Gini change data to compare predictions of increases and decreases in Gini. Across communities, selection predicts positive Gini change, Δcmz+\Delta\_{\textrm{cm}}^{z+} better with r2=.6r^{2}=.6 than negative Gini change, Δcmz−\Delta\_{\textrm{cm}}^{z-} with r2=.45r^{2}=.45.

![Refer to caption](x7.png)


Figure 7: Income selection effects, ωjy\omega\_{j}^{y} predict changes in gini within communities and tracts (inset). The spatial dynamics of income-selection will be explored in future work.

![Refer to caption](x8.png)


Figure 8: Scaling effects are observed in the data. A. relative population shares by county. B. Selection scales superlinearly across counties (top), however this becomes linear when accounting for relative population between tracts (middle), and scale invariant when accounting for tract and county population differences.

## Appendix C Skew-t Distribution

A Student-t distribution behaves like a Gaussian distribution with fatter tails.
The Student-t distribution is defined

|  |  |  |  |
| --- | --- | --- | --- |
|  | p′​(x|v)=Γ​(ν+12)v​π​Γ​(ν2)​(1+xν2)−−ν+12,p^{\prime}(x|v)=\frac{\Gamma(\frac{\nu+1}{2})}{\sqrt{v\pi}\Gamma(\frac{\nu}{2})}\bigg(1+\frac{x}{\nu^{2}}\bigg)^{-\frac{-\nu+1}{2}}, |  | (23) |

where the domain is defined over all real xx with degrees of freedom (DOF) ν\nu.
The gamma function is given by Γ​(⋅)\Gamma(\cdot), a function often used to normalize gamma distributions.
The DOF is bounded below by zero, and the tails converge to that of a Gaussian (shrink) as ν→∞\nu\rightarrow\infty.
In this limit, the ratio of gamma functions converge to (ν2)1/2(\tfrac{\nu}{2})^{1/2}, and the prefactor converges to 12​π\tfrac{1}{\sqrt{2\pi}}

The mean of a Student-t distribution can be shifted with parameter μ\mu, and the variance scaled with σ\sigma.
The shifted Student-t becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(x|ν,μ,σ)=1σ​p′​(x−μσ|ν),p(x|\nu,\mu,\sigma)=\frac{1}{\sigma}p^{\prime}\bigg(\frac{x-\mu}{\sigma}|\nu\bigg), |  | (24) |

which converges to a Gaussian centered about μ\mu and a standard deviation of σ\sigma as ν→∞\nu\rightarrow\infty.

The Skew-t distribution is then modified by the skew parameter α\alpha, which is right skewed (the right tail is fatter) when α>0\alpha>0 and left skewed with α<0\alpha<0.
The full definition of the Skew-t is

|  |  |  |  |
| --- | --- | --- | --- |
|  | p(x|ν,μ,σ,α)=2σp′(z|μ))P′(αzν+1ν+z2|ν+1),p(x|\nu,\mu,\sigma,\alpha)=\frac{2}{\sigma}p^{\prime}(z|\mu))P^{\prime}\bigg(\alpha z\sqrt{\frac{\nu+1}{\nu+z^{2}}}|\nu+1\bigg), |  | (25) |

where the Gaussian standardized value is defined z=x−μσz=\tfrac{x-\mu}{\sigma}. The skew is given by the CDF of p′p^{\prime}, and is defined

|  |  |  |  |
| --- | --- | --- | --- |
|  | P′​(x|a)=∫−∞xp′​(u;a)​𝑑uP^{\prime}(x|a)=\int\_{-\infty}^{x}p^{\prime}(u;a)du |  | (26) |

,
which evaluates to a cumbersome expression that will not be fully defined here.
This is a modulating function that adds weight to the Student-t distribution depending on the integration limit.
When the skew factor α=0\alpha=0, the function evaluates to 0.5, and the factor of 2 in equation [25](https://arxiv.org/html/2511.06165v1#A3.E25 "In Appendix C Skew-t Distribution ‣ Spatial Selection and the Multiscale Dynamics of Urban Change") cancels, reducing to the symmetric Student-t distribution. When α≠0\alpha\neq 0, the CDF creates asymmetry by differentially weighting the left and right tails of the distribution.
For α>0\alpha>0, positive values of zz produce larger integration limits, causing P′P^{\prime} to exceed 0.5 and amplify the right tail. Conversely, negative values of zz produce smaller integration limits, causing P′P^{\prime} to fall below 0.5 and suppress the left tail. This creates a right-skewed distribution with a longer tail extending to positive values.
This construction allows the skew-t distribution to model data exhibiting both heavy tails (controlled by ν\nu) and asymmetry (controlled by α\alpha), making it particularly suitable for real-world phenomena such as distributions of selection values where correlated local fluctuations cause extreme values to occur more frequently than predicted by normal distributions.

The fit for the tract level selection data has higher skew, αtr=0.55\alpha\_{\textrm{tr}}=0.55, than community level, αcm=0.20\alpha\_{\textrm{cm}}=0.20, with fatter tails as measured by the degrees of freedom parameter, νtr=1.43\nu\_{\textrm{tr}}=1.43 to νcm=2.47\nu\_{\textrm{cm}}=2.47.

## Appendix D Scaling Behavior of Selection

Urban scaling theory posits that many properties of cities can be described by a simple power-law relationship with their population, pp, S=S0​pβS=S\_{0}p^{\beta}. Here, SS is the observed, urban indicator while β\beta is the scaling exponent.
When expressed on a logarithmic scale, the expression takes a linear form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ln⁡S=ln⁡S0+β​ln⁡p.\ln S=\ln S\_{0}+\beta\ln p. |  | (27) |

We see clearly that β\beta describes how the indicator changes with city size.
Analyzing its value gives us insights into potential mechanisms for how people interact, move and self sort around cities [[53](https://arxiv.org/html/2511.06165v1#bib.bib53)].

In this section, we will discuss the scaling behavior of the empirical selection quantities, aggregated to the county level.
By comparing relative selection quantities between counties, we gain some insights on the spatial assortment and scale-dependence of sorting.
We note that this is not a typical application of scaling theory, for which the city is the unit of measurement and not subdivisons of the city and analysis is conducted cross-sectionally across an ensemble of cities.
As such, the following results cannot be interpreted under standard scaling theory.
Secondly, as this analysis is performed for a handful of counties in a single city, we do not attempt to extrapolate these results nor make any general claim about how selection scales in cities or subunits of cities.
Instead, we only aim to interpret the scaling results Chicago dataset, and identify patterns worth exploring across other datasets.

In Fig. [8](https://arxiv.org/html/2511.06165v1#A2.F8 "Figure 8 ‣ B.1 Price equation decomposition of log incomes ‣ Appendix B Multiscale growth ‣ Spatial Selection and the Multiscale Dynamics of Urban Change"), we establish the population share of Chicago MSA counties in Illinois.
Cook county, in which the City of Chicago and other urban centers, like Evanston and Oak Park are location, accounts for nearly 2/3rds of the MSA population.
Other population centers like Aurora and Naperville, are internally split between the counties of DuPage, Lake, and Will and so on.
These populationn splits will become important as we re-weigh selection effects in the scaling analysis.

The first quantity we report is a distributional average selection selection scaling effect, reported at the top of in Fig. [8](https://arxiv.org/html/2511.06165v1#A2.F8 "Figure 8 ‣ B.1 Price equation decomposition of log incomes ‣ Appendix B Multiscale growth ‣ Spatial Selection and the Multiscale Dynamics of Urban Change")B.
Here,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨ρtr⟩ct=∑tr∈ct|Strp|Ntrct,\langle\rho\_{\textrm{tr}}\rangle\_{\textrm{ct}}=\frac{\sum\_{\textrm{tr}\in\textrm{ct}}|S\_{\textrm{tr}}^{p}|}{N\_{\textrm{tr}}^{\textrm{ct}}}, |  | (28) |

where NtrctN\_{\textrm{tr}}^{\textrm{ct}} counts the number of tracts in the county.
This quantity measures the total geographic churn, treating a selection event in a low-density tract the same as one in a high-density tract. It measures the total magnitude of selection events across all places.
In the data, we observe a scaling coefficient of βd=1.31\beta\_{d}=1.31,
indicating county that is 10% larger in population has approximately 13% more total selection magnitude across its tracts
The superlinearity indicates that selections effects are disproportionately more intense in larger counties.

This measurement equally weighs each spatial unit.
If we account for spatial population heterogeneity across units within county, we can measure more directly the human impact on selection.
We will do this in two steps: first by just considering the apportionment of households internal to each county.
The second will introduce weighing counties relative population, providing a per-capita measurement of selection.

The population-weighted selection is computed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σtr→ct=∑tr∈ctptr​|Strp|,\Sigma\_{\textrm{tr}\rightarrow\textrm{ct}}=\sum\_{\textrm{tr}\in\textrm{ct}}p\_{\textrm{tr}}|S\_{\textrm{tr}}^{p}|, |  | (29) |

and measurs the total magnitude of selection as experienced by the population.
We measure a virtually linear scaling coefficient of βw=1.03\beta\_{w}=1.03.
This means that selection across units scale superlinear with county size, the total impact on the population scales directly with size.
This implies that the more intense sorting events observed in larger counties are preferentially occurring in less populated tracts. This frontier of demographic change in Chicago lies in more sparsely populated populated tracts across counties.

Finally, when we consider the relative population of each county, as we do for the expression

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ect​[ρtr]=Σtr→ctpc​t.\textrm{E}\_{\textrm{ct}}[\rho\_{\textrm{tr}}]=\frac{\Sigma\_{\textrm{tr}\rightarrow\textrm{ct}}}{p\_{ct}}. |  | (30) |

This expression measures the average, per-capita intensity of selection.
We observe a βp=.03\beta\_{p}=.03, meaning that for Chicago, experienced selection is scale-invariant.
This confirms the insight from before, that an average person in a large county experiences the same intensity of selection as an average person in a small county.

Generally, we observe that while the system as a whole produces more total churn as indicated by the superlinearity of βd\beta\_{d}, it has organized itself in such a way that the average experience remains constant. It implies that the sorting processes are not accelerating on a per-person basis with city size, and that in this limited case, the ”social accelerator” effect that makes cities more productive or innovative does not seem to apply to the intensity of neighborhood churn.