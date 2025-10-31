---
authors:
- J. D. A. Islas-García
- M. del Castillo-Mussotb
- Marcelo B. Ribeiro
doc_id: arxiv:2510.26030v1
family_id: arxiv:2510.26030
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: World personal income distribution evolution measured by purchasing power parity
  exchange rates
url_abs: http://arxiv.org/abs/2510.26030v1
url_html: https://arxiv.org/html/2510.26030v1
venue: arXiv q-fin
version: 1
year: 2025
---


J.D.A. Islas-García111Orcid 0000-0002-2440-0936
Posgrado Ciencias Físicas, Universidad Nacional
Autónoma de México, Mexico City, Mexico
[j\_da\_ig@ciencias.unam.mx](mailto:j_da_ig@ciencias.unam.mx)

M. del Castillo-Mussot222Orcid 0000-0001-5061-2601
Instituto de Física, Universidad Nacional Autónoma
de México, Mexico City, Mexico
[mussot@fisica.unam.mx](mailto:mussot@fisica.unam.mx)

Marcelo B. Ribeiro333Orcid 0000-0002-6919-2624
Instituto de Física, Universidade Federal do Rio de
Janeiro, Rio de Janeiro, Brazil
[mbr@if.ufrj.br](mailto:mbr@if.ufrj.br)

###### Abstract

The evolution of global income distribution from 1988 to 2018 is analyzed
using purchasing power parity exchange rates and well-established statistical
distributions. This research proposes the use of two separate distributions
to more accurately represent the overall data, rather than relying on a
single distribution. The global income distribution was fitted to log-normal
and gamma functions, which are standard tools in econophysics. Despite
limitations in data completeness during the early years, the available
information covered the vast majority of the world’s population. Probability
density function (PDF) curves enabled the identification of key peaks in the
distribution, while complementary cumulative distribution function (CCDF)
curves highlighted general trends in inequality. Initially, the global income
distribution exhibited a bimodal pattern; however, the growth of middle
classes in highly populated countries such as China and India has driven the
transition to a unimodal distribution in recent years. While single-function
fits with gamma or log-normal distributions provided reasonable accuracy,
the bimodal approach constructed as a sum of log-normal distributions yielded
near-perfect fits.

###### keywords:

econophysics , income distribution , gamma function , log-normal distribution

## 1 Introduction

The increasing interconnectedness of the global economy over the past four
decades has sparked intense interest in understanding how income is distributed
across the world’s population. This interest stems from the growing realization
that globalization has often been accompanied by rising income and wealth
inequalities [oxfam1](https://arxiv.org/html/2510.26030v1#bib.bib1) , [oxfam2](https://arxiv.org/html/2510.26030v1#bib.bib2) . Inasmuch as both income and wealth
distributions, and their respective inequalities, go to the heart of any
society’s viewpoints on issues regarding egalitarianism and social opportunity,
the relationship between globalization processes and its impact on the income
inequality has attracted a lot of recent interest, becoming in fact an
important research topic among economists and econophysicists
[piketty](https://arxiv.org/html/2510.26030v1#bib.bib3) , [incomedistro](https://arxiv.org/html/2510.26030v1#bib.bib4) , [ribeiro2020income](https://arxiv.org/html/2510.26030v1#bib.bib5) . In particular, the
characterization of income distributions yield critical information for
determining richness, the gap between rich and poor and societies’ well
being rates at any gross domestic product (GDP) level
[elephantpaper2](https://arxiv.org/html/2510.26030v1#bib.bib6) .

Research aimed at determining the overall behavior of income
distributions were initially focused on some countries and regions
and within limited time period intervals. More recently such an
approach, although much more detailed than earlier studies, still
focuses on particular countries and regions, which renders such
studies basically fragmented if one considers the worldwide income
distribution [ribeiro2020income](https://arxiv.org/html/2510.26030v1#bib.bib5)  and, therefore, do not present
a general scenario of its global situation. This is a clearly
desirable goal in order to advance our understanding of the
income distribution dynamic evolution at the world scale.

The aim of establishing a global income distribution must, however,
rely upon the combination of as many national household surveys as
possible because there is no global household survey of individual
incomes. To include all countries is not an easy task, as discussed
by Milanovic [milanovic2002true](https://arxiv.org/html/2510.26030v1#bib.bib7) , [milanovic2016greatest](https://arxiv.org/html/2510.26030v1#bib.bib8) , and
more recently by Anand and Segal [anand2015global](https://arxiv.org/html/2510.26030v1#bib.bib9) , because
most of the first works focusing on the world income distribution
are studies of international inequality in the sense that they
calculated what would be inequality in the world if it were
populated by representative individuals from all countries, that
is, by people having the mean income of their countries.

More accurate representations of the world income distributions were
constructed afterwards from assembling income distributions of
countries obtained by using income surveys or tax data. As mentioned
by Milanovic [milanovic2016greatest](https://arxiv.org/html/2510.26030v1#bib.bib8) , global inequality is a
relatively recent topic because in order to calculate it one needs
to have data on national income distributions for most of the
countries in the world, or at least for most of the populous
countries. Only from the early to mid 1980s that such data became
available for China, the Soviet Union and its constituent republics,
as well as large parts of Africa. Nevertheless, the problem of data
homogeneity, which ensures that variables are defined the same way
as much as possible, has been a difficult one in this area since its
inception.

The world income, or expenditure distribution, for 1988 and 1993
was calculated in Ref. [milanovic2002true](https://arxiv.org/html/2510.26030v1#bib.bib7)  for individuals
based entirely on household surveys from 91 countries adjusted for
differences in purchasing power parity (PPP) between
countries covering about 84% of world population and 93% of
world GDP. In similar works [bourguignon2002size](https://arxiv.org/html/2510.26030v1#bib.bib10) , [berry1983changes](https://arxiv.org/html/2510.26030v1#bib.bib11)  income shares for a number of countries were
approximated using income shares of “similar” countries. More
recently, making use of household income data from more than 130
countries the evolution of the global income distribution between 2008
and 2013 after the financial crisis was analyzed
[milanovic2022after](https://arxiv.org/html/2510.26030v1#bib.bib12) . For a comprehensive review of many
recent aspects of the global distribution of income, including
conceptual and methodological issues, inequality and global poverty
, we refer to the works of Milanovic
[milanovic2016greatest](https://arxiv.org/html/2510.26030v1#bib.bib8) , [milanovic2006global](https://arxiv.org/html/2510.26030v1#bib.bib13) , [milanovic2011worlds](https://arxiv.org/html/2510.26030v1#bib.bib14) , [milanovic2012global](https://arxiv.org/html/2510.26030v1#bib.bib15) , [milanovic2016income](https://arxiv.org/html/2510.26030v1#bib.bib16) , [milanovic2023great](https://arxiv.org/html/2510.26030v1#bib.bib17)  and Anand and Segal [anand2015global](https://arxiv.org/html/2510.26030v1#bib.bib9) , [anand2008we](https://arxiv.org/html/2510.26030v1#bib.bib18) , [anand2010debates](https://arxiv.org/html/2510.26030v1#bib.bib19) , [anand2017global](https://arxiv.org/html/2510.26030v1#bib.bib20) , [segal2022inequality](https://arxiv.org/html/2510.26030v1#bib.bib21) .

This paper aims at fitting the global income distribution data over
several years and studying it evolution. Here we follow the tradition
of economists, physicists and mathematicians who have sought to
characterize the distribution of income in countries by a mixture of
known statistical distributions [ribeiro2020income](https://arxiv.org/html/2510.26030v1#bib.bib5) . Our approach
here is to try to characterize the changes in time of the individual
income distribution in the world as a whole by means of known statistical
distributions with the smallest possible number of parameters.

The ultimate aim of studies on income and wealth distribution must be
to reveal the inner dynamics of both quantities by expressing them in
terms of time evolving differential equations [ribeiro2020income](https://arxiv.org/html/2510.26030v1#bib.bib5) .
So, the ultimate aim must be to identify the mechanisms at work so that
some further theoretical work clarifies and enhances our understanding
of what we observe [piketty](https://arxiv.org/html/2510.26030v1#bib.bib3) . However, income distribution is a
subject that was unfortunately very much neglected by mainstream academic
economics for a very long time [atkinson97](https://arxiv.org/html/2510.26030v1#bib.bib22) , and whose revival basically
happened on the onset of the 21st century [ribeiro2020income](https://arxiv.org/html/2510.26030v1#bib.bib5) , so the
present research level of this subject still very much remains in the
stage of data collecting and analyzing in order to see which basic
conclusions can be reached from the data in order to try to point out
possible future theoretical endeavors. This is particularly true of
global income distribution, which means that the present study is very
much focused on this initial research stage.

The plan of the paper is as follows. §2 is devoted to briefly
review some models of wealth and income distributions used by
economists, econophysicists and other scientists that will be
employed in the present approach. The exponential-like distributions
such as the gamma and log-normal distributions. Since our data are at
household-level (micro) data, then in §3 we briefly present the
limitations of the databases we employed in terms of their sources,
standardization, drawbacks and advantages, together with the
convenience of PPP to compare overall consumption and income between
nations. In §4 we present our results of world income distribution
between 1988 and 2018 measured by PPP in US dollars. §5 is devoted
to our conclusions.

## 2 Modeling income and wealth distributions used in econophysics

It is fair to state that at present there is a consensus among most,
if not all, researchers devoted to the income distribution problem
that the richest stratum of a country income distribution, that is,
its upper end segment, is well represented by a power law as Vilfredo
Pareto argued over a century ago [pareto1964cours](https://arxiv.org/html/2510.26030v1#bib.bib23) .
However, the distributive characterization of the not so rich
still remains an open problem. Different authors proposed different
fitting functions to characterize the income distribution of the
vast majority of populations, but until the turn of the 21st century
little more has been done than trying different functional fits in
relatively limited number of countries or group of countries
[incomedistro](https://arxiv.org/html/2510.26030v1#bib.bib4) , [ribeiro2020income](https://arxiv.org/html/2510.26030v1#bib.bib5) .

Among the early attempts at different functional fits one should
recall the work of Robert Gibrat, who in 1931 had already indicated
that the Pareto law is only valid for the high income range, whereas
for the small and middle income ranges he suggested the log-normal
probability density as a better descriptor. He also proposed a law
of proportionate effect, which states that a small change in a
quantity is independent of the quantity itself [gibrat1931inegalits](https://arxiv.org/html/2510.26030v1#bib.bib24) .

An important, and much more recent, work in this respect was the
analysis of the income distribution data of the USA as studied by
Silva and Yakovenko [yakovenko2005two](https://arxiv.org/html/2510.26030v1#bib.bib25) . It revealed the
coexistence of two social classes as far as functional fitting is
concerned: the large majority of the population is characterized
by a quasi-exponential distribution, and the very small upper income
segment exhibits the Pareto power-law distribution with characteristic
fat tails. They argued that there is a similar-to-physics energy
conservation law such that in the income distribution problem
translates itself as conservation of money. This means that the
middle and lower income populations of the USA are described by an
exponential function whose interpretation is of being a Boltzmann-Gibbs
distribution which entails such a conservative money quantity.

Silva and Yakovenko also considered currency transactions as being
equivalent to elastic molecular collisions in a gas particle, where
in principle all the conserved energy, in this case money, would be
transferred from one particle, or agent, to another in an one-to-one
interaction, or transaction, without money loss [silva2004temporal](https://arxiv.org/html/2510.26030v1#bib.bib26) .
The income distribution data of Mexico [soriano2017non](https://arxiv.org/html/2510.26030v1#bib.bib27) , the
European Union [jagielski2013modelling](https://arxiv.org/html/2510.26030v1#bib.bib28) , and more than 60
countries [tao2019exponential](https://arxiv.org/html/2510.26030v1#bib.bib29)  also present similar two-classes
structure.

Chakrabarti and collaborators [incomedistro](https://arxiv.org/html/2510.26030v1#bib.bib4) , [ribeiro2020income](https://arxiv.org/html/2510.26030v1#bib.bib5) , [joseph2022](https://arxiv.org/html/2510.26030v1#bib.bib30) 
extended this kinetic collision model to include savings, which then
better reflects real economic transactions, yielding, in the case of
a constant saving fraction for all agents, a stationary distribution
very similar to the gamma function.

In general, the bulk of the lower distribution stratum of both income
and wealth can be fitted by exponential, log-normal and gamma
distributions. Nevertheless, contrary
to the lower regions which remain basically unchanged for both
income and wealth, apart from the different functional fits, the
Pareto tail slope exhibits changes in time, a behavior that could
be possibly explained by the complex processes of creation and
destruction of money through investments, credit, financial derivatives,
big stock market crisis, etc, features which are much more clearly
related to the Pareto tail because these processes are basically from
where the rich people extract their income and wealth [ribeiro2020income](https://arxiv.org/html/2510.26030v1#bib.bib5) .

### 2.1 Distribution functions

The cumulative distribution function (CDF) is defined as
follows,

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(m)=∫0mP​(m′)​𝑑m′,F(m)=\int\_{0}^{m}P(m^{\prime})\,dm^{\prime}, |  | (1) |

where PP signifies the probability distribution function (PDF),
also known as probability density. In the present context mm
represents monetary value. The complement of Eq. ([1](https://arxiv.org/html/2510.26030v1#S2.E1 "In 2.1 Distribution functions ‣ 2 Modeling income and wealth distributions used in econophysics ‣ World personal income distribution evolution measured by purchasing power parity exchange rates")) defines
the complementary cumulative distribution function (CCDF), which
may be written as below [ribeiro2020income](https://arxiv.org/html/2510.26030v1#bib.bib5) ,

|  |  |  |  |
| --- | --- | --- | --- |
|  | F¯​(m)=∫m∞P​(m′)​𝑑m′=1−F​(m).\bar{F}(m)=\int\_{m}^{\infty}P(m^{\prime})\,dm^{\prime}=1-F(m). |  | (2) |

This is a very useful quantity to study income distribution because it
provides valuable insights on the data it represents by offering better
visualization of tail behavior, which in turn highlights rare events
given by extreme values in the dataset, that is, far from the mean. In
addition, several CCDFs plots provide helpful comparisons on how the
tails behave, allowing the assessment of the heavier or lighter ones.
Discussing the income distribution by means of the CCDF provides a
meaningful way to comprehend the probability of values greater than
or equal to a given threshold mm, facilitating a deeper understanding
of the data’s behavior and tail characteristics.444Eq. ([2](https://arxiv.org/html/2510.26030v1#S2.E2 "In 2.1 Distribution functions ‣ 2 Modeling income and wealth distributions used in econophysics ‣ World personal income distribution evolution measured by purchasing power parity exchange rates")) has several applications when it is integrated in time,
specially in, but not limited to, medicine and engineering. In the
medical literature the CCDF is known as survival function
[survive](https://arxiv.org/html/2510.26030v1#bib.bib31) , whereas in the engineering literature
it is referred as reliability function [reli](https://arxiv.org/html/2510.26030v1#bib.bib32) .
In these two applications the CCDF gives the probability that a patient
survives, or a device remains reliable, past a certain time.

### 2.2 Log-normal distribution

This is basically a normal function whose independent variable xx
scales as ln⁡x\ln x. That is, the log-normal distribution is a normal
one of the logarithm of xx [ribeiro2020income](https://arxiv.org/html/2510.26030v1#bib.bib5) , [kleiber2003statistical](https://arxiv.org/html/2510.26030v1#bib.bib33) .
So, the probability density of the normal function scaled that way may be
written as,

|  |  |  |  |
| --- | --- | --- | --- |
|  | N​(ln⁡x)=1σ​2​π​exp⁡[−(ln⁡x−μ)22​σ2],N(\ln x)=\frac{1}{\sigma\sqrt{2\pi}}\exp{\left[-\frac{(\ln x-\mu)^{2}}{2\sigma^{2}}\right]}, |  | (3) |

where the parameters μ\mu and σ\sigma are respectively the mean value of
the logarithmic variable and its variance, that is, μ=⟨ln⁡x⟩\mu=\langle\ln x\rangle and σ=⟨(ln⁡x−μ)2⟩\sigma=\langle(\ln x-\mu)^{2}\rangle. A change of variables
produces,

|  |  |  |  |
| --- | --- | --- | --- |
|  | N​(ln⁡x)​d​(ln⁡x)=[N​(ln⁡x)x]​d​x.N(\ln x)\,d(\ln x)=\left[\frac{N(\ln x)}{x}\right]\,dx. |  | (4) |

For equal probabilities under the normal and log-normal densities,
incremental areas should also be equal, that is, N​(ln⁡x)​d​(ln⁡x)=Nl​(x)​d​xN(\ln x)\,d(\ln x)=N\_{l}(x)\,dx. This means that the probability density of the
log-normal distribution is given by,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Nl​(x)=N​(ln⁡x)x=1x​σ​2​π​exp⁡[−(ln⁡x−μ)22​σ2].N\_{l}(x)=\frac{N(\ln x)}{x}=\frac{1}{x\sigma\sqrt{2\pi}}\exp{\left[-\frac{(\ln x-\mu)^{2}}{2\sigma^{2}}\right]}. |  | (5) |

### 2.3 Gamma distribution

The income distribution of the less than rich can also be reasonably well
fitted by the gamma distribution [ribeiro2020income](https://arxiv.org/html/2510.26030v1#bib.bib5) , [ferrero2004statistical](https://arxiv.org/html/2510.26030v1#bib.bib34) , [ferrero2005monomodal](https://arxiv.org/html/2510.26030v1#bib.bib35) ]. This is a three-parameter
function whose probability density reads as,

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x)=[AΓ​(n)​mn]​x(n−1)​e−(x/m),f(x)=\left[\frac{A}{\Gamma(n)m^{n}}\right]x^{(n-1)}{\mathrm{e}}^{-({x}/{m})}, |  | (6) |

where AA, nn, and 1/m{1}/{m} are, respectively, the normalizing, shape,
and rate parameters.

### 2.4 Distributions constructed as sums

During the process of data fitting we found useful to summing up
two log-normal or gamma distributions with different parameter
values. Hence, the bi-gamma PDF is written as,

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x)=A1​x(n1−1)​[e−(x/m1)Γ​(n1)​m1(n1−1)]+A2​x(n2−1)​[e−(x/m2)Γ​(n2)​m2(n2−1)],f(x)=A\_{1}x^{(n\_{1}-1)}\left[\frac{{\mathrm{e}}^{-({x}/{m\_{1}})}}{\Gamma(n\_{1})m\_{1}^{(n\_{1}-1)}}\right]\\ +A\_{2}x^{(n\_{2}-1)}\left[\frac{{\mathrm{e}}^{-({x}/{m\_{2}})}}{\Gamma(n\_{2})m\_{2}^{(n\_{2}-1)}}\right], |  | (7) |

whereas the bi-log-normal PDF yields,

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x)=A1x​σ1​exp⁡[−(ln⁡x−μ1)22​(σ1)2]+A2x​σ2​exp⁡[−(ln⁡x−μ2)22​(σ2)2].f(x)=\frac{A\_{1}}{x\sigma\_{1}}\exp{\left[-\frac{(\ln x-\mu\_{1})^{2}}{2{(\sigma\_{1})}^{2}}\right]}\\ +\frac{A\_{2}}{x\sigma\_{2}}\exp{\left[-\frac{(\ln x-\mu\_{2})^{2}}{2{(\sigma\_{2})}^{2}}\right]}. |  | (8) |

Statistical distributions such as the log-normal and gamma distributions
are well suited for modeling income and wealth because of their ability
to capture the natural variability of economic systems. The log-normal
distribution effectively represents middle- and low-income segments,
where incomes grow multiplicatively through investment or other economic
processes. In contrast, the gamma distribution is particularly well suited
for modeling lower-income populations because of its exponential decay but
it is vanishing at the origin. The introduction of a bimodal fit, where
two distributions are combined, allows for a more accurate representation
of the data by taking into account the coexistence of different income
groups within global populations.

## 3 Database

The GDP is a widely used monetary measure of the market value of all
final goods and services produced in a period of time, often annually.
There are two ways to measure GDP: nominally or via PPP. The first
way, nominal or market value GDP, or GDP at exchange rate, occurs when
the GDP of countries in their corresponding currencies are converted
into a single currency, like, for example, into the United
States dollar (USD). The second measure is GDP at PPP (GDP-PPP), when
a “basket of goods” comprising a wide range of goods and services is
priced equally in different countries and territories and by taking
into account exchange rate.

In what follows, for brevity reasons, when we write countries, it
is understood that we refer to both countries and territories. The
so-called “international dollar” would buy in a given country a
comparable amount of goods and services a USD would buy in the US
according to PPP data. Although estimating the PPP across countries
is not an easy task, it is accepted that PPP measures are generally
regarded as better and more stable way than market values to compare
overall consumption and income among nations. The GDP-PPP of
developing countries is in general, higher than their nominal GDP,
so the per capita income gap between rich and poor countries is
reduced under PPP values.

The empirical data used here were obtained from two sets of data: Lakner
and Milanovic [lakner2015global](https://arxiv.org/html/2510.26030v1#bib.bib36)  and Roser [Roser2023-et](https://arxiv.org/html/2510.26030v1#bib.bib37) . As
it will be shown below, our main fitting results were derived from the
former’s database, whereas the latter’s one was employed to subtract
the income distributions of China and India in order to show how
important these countries populations are to fill the “global
middle-class” valley as time passes.

All aforementioned data do not include the entire world population
because it has a 60k USDs upper cutoff limit that considered the
inflation adjusted year 2011. In addition, the income values were
measured in each country according to PPP in USD. Milanovic’s data
[lakner2015global](https://arxiv.org/html/2510.26030v1#bib.bib36)  were measured in 2011 PPP USD and Roser’s
data [Roser2023-et](https://arxiv.org/html/2510.26030v1#bib.bib37)  in 2005 PPP USD. Even so, despite this
limitation the available data included the vast majority of the
world’s population. The results of our analysis will demonstrate how
simple statistical models can effectively capture the dynamic evolution
of income distributions over time. The following section delves into
these results, highlighting key patterns and through our fitting methods.

## 4 Results

Data fitting using the distribution functions discussed above were
carried out with all available data. The results are presented below
grouped by the respective function used to fit the data. In all figures
the term “semilogx” at the top indicates that there is a logarithmic
scale at the x-axis.

### 4.1 Gamma and bi-gamma fits

Fig. [1](https://arxiv.org/html/2510.26030v1#S4.F1 "Figure 1 ‣ 4.1 Gamma and bi-gamma fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") shows the world income PDF in 2011 PPP USD from
1988 to 2018 obtained by Milanovic. Two results can be clearly noticed
from the plots as time passes: the distribution shifts to the right
and the valley tends to disappear.

![Refer to caption](x1.png)


Figure 1: Milanovic income distribution from 1988 to 2018.

Figs. [2](https://arxiv.org/html/2510.26030v1#S4.F2 "Figure 2 ‣ 4.1 Gamma and bi-gamma fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") to [7](https://arxiv.org/html/2510.26030v1#S4.F7 "Figure 7 ‣ 4.1 Gamma and bi-gamma fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") show that a single gamma
distribution only matches the first peak. The adjustment parameter R2R^{2}
is around 0.72 except for year 2018 when it is 0.85. These plots also
show that a single gamma distribution only matches the first peak. The
adjustment parameter R2R^{2} is around 0.72 except for year 2018 when it
is equal to 0.85. Table 1 shows the values of R2R^{2} of all the fittings
we present here.

![Refer to caption](x2.png)


Figure 2: Gamma fit for Milanovic income distribution for year 1988, R2=0.69068R^{2}=0.69068

![Refer to caption](x3.png)


Figure 3: Gamma fit for year 1993, R2=0.73948R^{2}=0.73948

![Refer to caption](x4.png)


Figure 4: Gamma fit for year 1998, R2=0.72081R^{2}=0.72081

![Refer to caption](x5.png)


Figure 5: Gamma fit for year 2003, R2=0.73558R^{2}=0.73558

![Refer to caption](x6.png)


Figure 6: Gamma fit for year 2008, R2=0.72134R^{2}=0.72134

![Refer to caption](x7.png)


Figure 7: Gamma fit for year 2018, R2=0.85627R^{2}=0.85627

Figs. [8](https://arxiv.org/html/2510.26030v1#S4.F8 "Figure 8 ‣ 4.1 Gamma and bi-gamma fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") to [13](https://arxiv.org/html/2510.26030v1#S4.F13 "Figure 13 ‣ 4.1 Gamma and bi-gamma fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") show basically the same data as
in previous figures now fitted with bi-gamma functions, either separately
or together. The plots show that each one fits well some portion of the
data and that taking them together provides a better fit to the whole
distribution. In general the fitting is better in the low “poor” region
than in the “rich” one.

![Refer to caption](x8.png)


Figure 8: Bi-Gamma fit for Milanovic income distribution in 1988, R2=0.96115R^{2}=0.96115

![Refer to caption](x9.png)


Figure 9: Same as Fig. [8](https://arxiv.org/html/2510.26030v1#S4.F8 "Figure 8 ‣ 4.1 Gamma and bi-gamma fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") but for 1993, R2=0.9499R^{2}=0.9499

![Refer to caption](x10.png)


Figure 10: Same as Fig. [8](https://arxiv.org/html/2510.26030v1#S4.F8 "Figure 8 ‣ 4.1 Gamma and bi-gamma fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") but for 1998, R2=0.94064R^{2}=0.94064

![Refer to caption](x11.png)


Figure 11: Same as Fig. [8](https://arxiv.org/html/2510.26030v1#S4.F8 "Figure 8 ‣ 4.1 Gamma and bi-gamma fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") but for 2003, R2=0.93372R^{2}=0.93372

![Refer to caption](x12.png)


Figure 12: Same as Fig. [8](https://arxiv.org/html/2510.26030v1#S4.F8 "Figure 8 ‣ 4.1 Gamma and bi-gamma fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") but for 2008, R2=0.94681R^{2}=0.94681

![Refer to caption](x13.png)


Figure 13: Same as Fig. [8](https://arxiv.org/html/2510.26030v1#S4.F8 "Figure 8 ‣ 4.1 Gamma and bi-gamma fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") but for 2018, R2=0.85627R^{2}=0.85627

Figs. [14](https://arxiv.org/html/2510.26030v1#S4.F14 "Figure 14 ‣ 4.1 Gamma and bi-gamma fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") to [20](https://arxiv.org/html/2510.26030v1#S4.F20 "Figure 20 ‣ 4.1 Gamma and bi-gamma fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") present the same data as in
previous figures, but fitted to the CCDF bi-gamma to obtain better
values for R2R^{2} than the PDF fittings. It is clear how in the bi-gamma
CCDF curves deviate slightly below the ones of the empirical values at
the tail of the distribution, that is, in the rich region.

![Refer to caption](x14.png)


Figure 14: CCDF bi-gamma for 1988, R2=0.99782R^{2}=0.99782

![Refer to caption](x15.png)


Figure 15: CCDF bi-gamma for 1993, R2=0.99712R^{2}=0.99712

![Refer to caption](x16.png)


Figure 16: CCDF bi-gamma for 1998, R2=0.99721R^{2}=0.99721

![Refer to caption](x17.png)


Figure 17: CCDF bi-gamma for 2003, R2=0.99711R^{2}=0.99711

![Refer to caption](x18.png)


Figure 18: CCDF bi-gamma for 2008, R2=0.99685R^{2}=0.99685

![Refer to caption](x19.png)


Figure 19: CCDF bi-gamma for 2011, R2=0.99743R^{2}=0.99743

![Refer to caption](x20.png)


Figure 20: CCDF bi-gamma for 2018, R2=0.99896R^{2}=0.99896

### 4.2 Log-normal and bi-log-normal fits

As in the case of the gamma function, the log-normal fits shown in
Figs. [21](https://arxiv.org/html/2510.26030v1#S4.F21 "Figure 21 ‣ 4.2 Log-normal and bi-log-normal fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") to [26](https://arxiv.org/html/2510.26030v1#S4.F26 "Figure 26 ‣ 4.2 Log-normal and bi-log-normal fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") coincide well with all
data for the first peak. Figs. [27](https://arxiv.org/html/2510.26030v1#S4.F27 "Figure 27 ‣ 4.2 Log-normal and bi-log-normal fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") to [33](https://arxiv.org/html/2510.26030v1#S4.F33 "Figure 33 ‣ 4.2 Log-normal and bi-log-normal fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates")
show that bi-log-normal fits are better than bi-gamma fits as shown
by the R2R^{2} values shown in Table [1](https://arxiv.org/html/2510.26030v1#S4.T1 "Table 1 ‣ 4.2 Log-normal and bi-log-normal fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates"). Figs. [34](https://arxiv.org/html/2510.26030v1#S4.F34 "Figure 34 ‣ 4.2 Log-normal and bi-log-normal fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates")
to [40](https://arxiv.org/html/2510.26030v1#S4.F40 "Figure 40 ‣ 4.2 Log-normal and bi-log-normal fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") present the respective bi-log-normal CCDF where it
is clear that this function provides a better fit at the tail of the
distribution as compared to the bi-gamma CCDF ones.

![Refer to caption](x21.png)


Figure 21: Log-normal fit for Milanovic income distribution
in 1988, R2=0.77358R^{2}=0.77358

![Refer to caption](x22.png)


Figure 22: Same as Fig. [21](https://arxiv.org/html/2510.26030v1#S4.F21 "Figure 21 ‣ 4.2 Log-normal and bi-log-normal fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") but for 1993, R2=0.8366R^{2}=0.8366

![Refer to caption](x23.png)


Figure 23: Same as Fig. [21](https://arxiv.org/html/2510.26030v1#S4.F21 "Figure 21 ‣ 4.2 Log-normal and bi-log-normal fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") but for 1998, R2=0.84092R^{2}=0.84092

![Refer to caption](x24.png)


Figure 24: Same as Fig. [21](https://arxiv.org/html/2510.26030v1#S4.F21 "Figure 21 ‣ 4.2 Log-normal and bi-log-normal fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") but for 2003, R2=0.85684R^{2}=0.85684

![Refer to caption](x25.png)


Figure 25: Same as Fig. [21](https://arxiv.org/html/2510.26030v1#S4.F21 "Figure 21 ‣ 4.2 Log-normal and bi-log-normal fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") but for 2008, R2=0.86455R^{2}=0.86455

![Refer to caption](x26.png)


Figure 26: Same as Fig. [21](https://arxiv.org/html/2510.26030v1#S4.F21 "Figure 21 ‣ 4.2 Log-normal and bi-log-normal fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") but for 2018, R2=0.98991R^{2}=0.98991

![Refer to caption](x27.png)


Figure 27: Bi-log-normal fit for Milanovic income distribution
in 1988, R2=0.99383R^{2}=0.99383.

![Refer to caption](x28.png)


Figure 28: Same as Fig. [27](https://arxiv.org/html/2510.26030v1#S4.F27 "Figure 27 ‣ 4.2 Log-normal and bi-log-normal fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") but for 1993 R2=0.98898R^{2}=0.98898.

![Refer to caption](x29.png)


Figure 29: Same as Fig. [27](https://arxiv.org/html/2510.26030v1#S4.F27 "Figure 27 ‣ 4.2 Log-normal and bi-log-normal fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") but for 1998 R2=0.98634R^{2}=0.98634

![Refer to caption](x30.png)


Figure 30: Same as Fig. [27](https://arxiv.org/html/2510.26030v1#S4.F27 "Figure 27 ‣ 4.2 Log-normal and bi-log-normal fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") but for 2003 R2=0.98224R^{2}=0.98224

![Refer to caption](x31.png)


Figure 31: Same as Fig. [27](https://arxiv.org/html/2510.26030v1#S4.F27 "Figure 27 ‣ 4.2 Log-normal and bi-log-normal fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") but for 2008 R2=0.99129R^{2}=0.99129

![Refer to caption](x32.png)


Figure 32: Same as Fig. [27](https://arxiv.org/html/2510.26030v1#S4.F27 "Figure 27 ‣ 4.2 Log-normal and bi-log-normal fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") but for 2011 R2=0.99729R^{2}=0.99729

![Refer to caption](x33.png)


Figure 33: Same as Fig. [27](https://arxiv.org/html/2510.26030v1#S4.F27 "Figure 27 ‣ 4.2 Log-normal and bi-log-normal fits ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") but for 2018 R2=0.99973R^{2}=0.99973




Table 1: R2R^{2} values of fittings.

|  |  |  |  |
| --- | --- | --- | --- |
| year | gamma | bi-gamma | bi-gamma CCDF |
| 1988 | 0.69068 | 0.96115 | 0.99782 |
| 1993 | 0.73948 | 0.9499 | 0.99712 |
| 1998 | 0.72081 | 0.94064 | 0.99721 |
| 2003 | 0.73558 | 0.93372 | 0.99711 |
| 2008 | 0.72134 | 0.94681 | 0.99685 |
| 2011 | 0.69562 | 0.94975 | 0.99743 |
| 2018 | 0.85627 | 0.85627 | 0.99896 |
| year | log-normal | bi-log-normal | bi-log-normal CCDF |
| 1988 | 0.77358 | 0.99383 | 0.99989 |
| 1993 | 0.8366 | 0.98898 | 0.99987 |
| 1998 | 0.84092 | 0.98634 | 0.99981 |
| 2003 | 0.85684 | 0.98224 | 0.99976 |
| 2008 | 0.86455 | 0.99129 | 0.99991 |
| 2011 | 0.90122 | 0.99729 | 0.99995 |
| 2018 | 0.98991 | 0.99973 | 0.99999 |

![Refer to caption](x34.png)


Figure 34: 1988, R2=0.99989R^{2}=0.99989

![Refer to caption](x35.png)


Figure 35: 1993, R2=0.99987R^{2}=0.99987

![Refer to caption](x36.png)


Figure 36: 1998, R2=0.99981R^{2}=0.99981

![Refer to caption](x37.png)


Figure 37: 2003, R2=0.99976R^{2}=0.99976

![Refer to caption](x38.png)


Figure 38: 2008, R2=0.99991R^{2}=0.99991

![Refer to caption](x39.png)


Figure 39: 2011, R2=0.99995R^{2}=0.99995

![Refer to caption](x40.png)


Figure 40: 2018, R2=0.99999R^{2}=0.99999

### 4.3 World distribution without both China and India

Roser [Roser2023-et](https://arxiv.org/html/2510.26030v1#bib.bib37)  provided the income distributions of China
and India along time, and this allowed us to conveniently subtract
their contribution to the global distribution after realizing these
countries play a fundamental role in shaping global distribution.
Figs. [41](https://arxiv.org/html/2510.26030v1#S4.F41 "Figure 41 ‣ 4.3 World distribution without both China and India ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") to [46](https://arxiv.org/html/2510.26030v1#S4.F46 "Figure 46 ‣ 4.3 World distribution without both China and India ‣ 4 Results ‣ World personal income distribution evolution measured by purchasing power parity exchange rates") present these results where
the Y-axis is the PDF of the fitted functions.

If we envision a scenario without the presence of these two significant
demographic and economic players, a pronounced decline in the poor and
middle-class values emerge, creating a noticeable “valley” in the
graph. So, it seems that China and India, with their vast populations
and expanding economies, act as a bridge that fills this valley, thereby
generating a more uniform and comprehensive data distribution.

![Refer to caption](x41.png)


Figure 41: 1988, R2=0.96851R^{2}=0.96851

![Refer to caption](x42.png)


Figure 42: 1993, R2=0.93952R^{2}=0.93952

![Refer to caption](x43.png)


Figure 43: 1998, R2=0.93612R^{2}=0.93612

![Refer to caption](x44.png)


Figure 44: 2003, R2=0.93766R^{2}=0.93766

![Refer to caption](x45.png)


Figure 45: 2008, R2=0.94921R^{2}=0.94921

![Refer to caption](x46.png)


Figure 46: 2011, R2=0.97056R^{2}=0.97056

A comparative analysis shows that while earlier works, such as those by
Milanovic, focused on single-peak representations of income distribution,
they often failed to capture the complexities introduced by bimodal patterns,
especially in global datasets. Similarly, many works in econophysics
highlighted exponential and power-law distributions for national economies
but to our knowledge, but did not address the multimodal characteristics
observed in global contexts.

Therefore, our bimodal adjustments provide a new way of fitting the world
income distribution along the years (qualified with R values) showing the
usefulness of combining multiple distributions to model diverse economic
systems effectively. Insights gained from our models can provide elegant
interpretations of broader economic trends that can be improved by employing
distributions with more parameters.

## 5 Conclusions

This paper analyzed the evolution of global income distributions over
several decades using empirical datasets and fits to standard statistical
functions: gamma, log-normal, and their bimodal combinations. The graphical
analysis of the probability density function (PDF) and the
complementary cumulative density function (CCDF) revealed clear
patterns of inequality and the presence of multimodality in global income.

A key result is that single-function fits (gamma or log-normal) yield
reasonably good approximations up to $60k (2011 PPP USD), but the use
of bimodal combinations significantly improves fit quality across all years
studied. This suggests the global income distribution is better described
as a composition of at least two subpopulations, reflecting different
economic realities. The goodness-of-fit, measured by R2R^{2}, supports this
conclusion.

More recently, although there were improvements in collecting datasets
for income and wealth in many countries, data for the very poor and the
very rich households and individuals are still, in general, quite
unreliable. Due to the above mentioned upper limit data cutoff most
people from poor countries, with low per capita GDP, were included, but
in places like Monaco, Qatar and others with relatively large income per
capita, the datasets do not include large percentages of their respective
populations. The absence of significant world high-income datasets
explains why the Pareto power-law is very poorly presented, or
non-existent, in various upper segments of the income distributions
showed here. Therefore, world income distributions with higher upper
limits should have exhibited clear power law behaviors for higher income
values in addition to, possibly, second or third similar power-law
behaviors in subsets of increasing incomes. For instance, the income
and wealth data for billionaires as given by Forbes magazine
[noauthor\_undated-wn](https://arxiv.org/html/2510.26030v1#bib.bib38)  every year represents a very small subset of
humans who are very important in studies of economic income and wealth
inequalities related to the so-called, and much talked about, 99% vs. 1% economic disparity in the whole world.

A particularly novel finding is the structural role of China and India
in shaping the global income distribution. Between 1988 and 2008, the
global distribution transitioned from a bimodal to a more unimodal form,
largely due to income growth in these populous nations. When these two
countries are excluded, a valley between low- and middle-income peaks
re-emerges, underscoring their bridging function in the global economy.

These results underscore the value of combining multiple distributions to
better capture global economic heterogeneity. Moreover, they open the
door to richer interpretations of macroeconomic trends and transitions
in global inequality.

Importantly, such modeling approaches can be applied to study the effects
of shocks or policy interventions. For example, by fitting similar
distributions to post-pandemic datasets, one could quantify the impact
of COVID-19 on income polarization or middle-class shrinkage in different
regions, an issue already under debate in recent literature
[neelima2022post](https://arxiv.org/html/2510.26030v1#bib.bib39) , [UNDP2022](https://arxiv.org/html/2510.26030v1#bib.bib40) .

This work provides a simple and elegant comprehensive approach to the
world income distributions fitted to commonly used functions in econophysics.

The implications of these findings pave the way for more refined studies
and expanded datasets. The following section outlines potential directions
to deepen our understanding of income dynamics and possible policy implications.

## 6 Future work

We are particularly interested in extending the present analysis employing
very recent data from the LIS database [LIS](https://arxiv.org/html/2510.26030v1#bib.bib41) , which contain household
-and person- level data on labor income, capital income, pensions, public
social benefits and private transfers, as well as taxes and contributions,
demography, employment, and expenditures. So, this database will provide
enough empirical results to perform many important comparative
interdisciplinary analysis.

## Acknowledgments

J.D.A.I.G. and M.d.C.M. acknowledge the partial financial support
provided by DGAPA-UNAM, Mexico, grant No. IN106225. M.B.R. received
partial financial support from FAPERJ – Rio de Janeiro State
Research Funding Agency, grant number E-26/210.552/2024.

## References

* [1]

  A. Thériault, Richest 1% bag nearly twice as much wealth as the rest of
  the world put together over the past two years, Press release, Oxfam
  International,
  <https://www.oxfam.org/en/press-releases/richest-1-bag-nearly-twice-much-wealth-rest-world-put-together-over-past-two-years>,
  (accessed 17 June 2024) (2023).
* [2]

  M.-B. Christensen, C. Hallum, A. Maitland, Q. Parrinello, C. Putaturo, D. Abed,
  C. Brown, A. Kamande, M. Lawson, S. Ruiz,
  [Survival of the richest](www.oxfam.org/en/research/survival-richest),
  Policy paper (last accessed 29 August 2024), Oxfam International (2023).
    
  URL <www.oxfam.org/en/research/survival-richest>
* [3]

  T. Piketty, Capital in the Twenty-First Century, Harvard University Press,
  Cambridge, Massachusetts, 2014, translated by Arthur Goldhammer from the
  author’s original in French Le capital au XXIe siécle.
* [4]

  B. K. Chakrabarti, A. Chakraborti, S. T. Chakravarty, A. Chatterjee,
  Econophysics of Income and Wealth Distributions, Cambridge University Press,
  Cambridge, 2013.
* [5]

  M. B. Ribeiro, Income Distribution Dynamics of Economic Systems: An
  Econophysical Approach, Cambridge University Press, Cambridge, 2020.
* [6]

  C. Lakner, B. Milanovic, Global Income Distribution: From the Fall of the
  Berlin Wall to the Great Recession, The World Bank Economic Review
  30 (2) (2015) 203–232.
  [doi:10.1093/wber/lhv039](https://doi.org/10.1093/wber/lhv039).
* [7]

  B. Milanovic, True world income distribution, 1988 and 1993: First calculation
  based on household surveys alone, The economic journal 112 (476) (2002)
  51–92.
* [8]

  B. Milanovic, The greatest reshuffle of individual incomes since the industrial
  revolution, VoxEU July 1 (2016) 2016.
* [9]

  S. Anand, P. Segal, The global distribution of income, in: Handbook of income
  distribution, Vol. 2, Elsevier, 2015, pp. 937–979.
* [10]

  F. Bourguignon, C. Morrisson, The size distribution of income among world
  citizens, 1820-1990, American Economic Review 92 (4) (2002) 727–44.
* [11]

  A. Berry, F. Bourguignon, C. Morrison, Changes in the world distribution of
  income between 1950 and 1977, The Economic Journal 93 (370) (1983) 331–350.
* [12]

  B. Milanovic, After the financial crisis: the evolution of the global income
  distribution between 2008 and 2013, Review of Income and Wealth 68 (1) (2022)
  43–73.
* [13]

  B. Milanovic, Global income inequality: What it is and why it matters (2006).
* [14]

  B. Milanovic, Worlds apart: Measuring international and global inequality,
  Princeton University Press, 2011.
* [15]

  B. Milanovic, Global inequality recalculated and updated: the effect of new ppp
  estimates on global inequality and 2005 estimates, The Journal of Economic
  Inequality 10 (2012) 1–18.
* [16]

  B. Milanovic, Income inequality is cyclical, Nature 537 (7621) (2016) 479–482.
* [17]

  B. Milanovic, The great convergence: Global equality and its discontents,
  Foreign Aff. 102 (2023) 78.
* [18]

  S. Anand, P. Segal, What do we know about global income inequality?, Journal of
  Economic Literature 46 (1) (2008) 57–94.
* [19]

  S. Anand, P. Segal, J. E. Stiglitz, Debates on the measurement of global
  poverty, Oxford University Press, 2010.
* [20]

  S. Anand, P. Segal, Who are the global top 1%?, World Development 95 (2017)
  111–126.
* [21]

  P. Segal, Inequality interactions: The dynamics of multidimensional
  inequalities, Development and Change 53 (5) (2022) 941–961.
* [22]

  A. B. Atkinson, Bringing income distribution in from the cold, The Economic
  Journal 107 (1997) 297–321.
* [23]

  V. Pareto, Cours d’Économie Politique, Vol. 2, F. Rouge, Lausanne, 1897.
* [24]

  R. Gibrat, Les inégalits économiques, Sirey (1931).
* [25]

  V. M. Yakovenko, A. C. Silva, Two-class structure of income distribution in the
  usa: Exponential bulk and power-law tail, in: Econophysics of Wealth
  Distributions: Econophys-Kolkata I, Springer, 2005, pp. 15–23.
* [26]

  A. C. Silva, V. M. Yakovenko, Temporal evolution of the “thermal” and
  “superthermal” income classes in the usa during 1983–2001, Europhysics
  Letters 69 (2) (2004) 304.
* [27]

  P. Soriano-Hernández, M. del Castillo-Mussot,
  O. Córdoba-Rodríguez, R. Mansilla-Corona, Non-stationary individual
  and household income of poor, rich and middle classes in mexico, Physica A:
  Statistical Mechanics and its Applications 465 (2017) 403–413.
* [28]

  M. Jagielski, R. Kutner, Modelling of income distribution in the european union
  with the fokker–planck equation, Physica A: Statistical Mechanics and its
  Applications 392 (9) (2013) 2130–2138.
* [29]

  Y. Tao, X. Wu, T. Zhou, W. Yan, Y. Huang, H. Yu, B. Mondal, V. M. Yakovenko,
  Exponential structure of income inequality: evidence from 67 countries,
  Journal of Economic Interaction and Coordination 14 (2019) 345–376.
* [30]

  B. Joseph, B. K. Chakrabarti, Variation of Gini and Kolkata indices with
  saving propensity in the kinetic exchange model of wealth distribution: An
  analytical study, Physica A 594 (2022) 127051.
  [doi:10.1016/j.physa.2022.127051](https://doi.org/10.1016/j.physa.2022.127051).
* [31]

  D. F. Moore, Applied Survival Analysis Using R, Springer, 2016.
* [32]

  M. Mohammad Modarres, M. Kaminskiy, V. Krivtsov, Reliability Engineering and
  Risk Analysis: A Practical Guide, Marcel Dekker, Inc., 1999.
* [33]

  C. Kleiber, S. Kotz, Statistical size distributions in economics and actuarial
  sciences, John Wiley & Sons, 2003.
* [34]

  J. C. Ferrero, The statistical distribution of money and the rate of money
  transference, Physica A: Statistical Mechanics and its Applications 341
  (2004) 575–585.
* [35]

  J. C. Ferrero, The monomodal, polymodal, equilibrium and nonequilibrium
  distribution of money, in: Econophysics of Wealth Distributions:
  Econophys-Kolkata I, Springer, 2005, pp. 159–167.
* [36]

  C. Lakner, B. Milanovic, Global income distribution from the fall of the berlin
  wall to the great recession, Revista de Economía Institucional 17 (32)
  (2015) 71–128.
* [37]

  M. Roser, The history of global economic inequality, ’The history of global
  economic inequality’. Published online at OurWorldInData.org. Retrieved from:
  ’https://ourworldindata.org/the-history-of-global-economic-inequality’
  [Online Resource] (2017).
* [38]

  The world’s real-time billionaires,
    
  <https://www.forbes.com/real-time->
    
  <billionaires/#321e71413d78>, (accessed 5 September 2023) (2024).
* [39]

  K. Neelima, S. Chennapalli, Post-pandemic global inequalities: Causes and
  measures, in: Emerging Trends and Insights on Economic Inequality in the Wake
  of Global Crises, IGI Global, 2022, pp. 40–55.
* [40]

  U. N. D. Programme,
  [Uncertain
  times, unsettled lives: Shaping our future in a transforming world](https://hdr.undp.org/content/human-development-report-2021-22) (2022).
    
  URL <https://hdr.undp.org/content/human-development-report-2021-22>
* [41]

  [The Luxembourg
  Income Study Database (LIS)](https://www.lisdatacenter.org/our-data/lis-database/).
    
  URL <https://www.lisdatacenter.org/our-data/lis-database/>