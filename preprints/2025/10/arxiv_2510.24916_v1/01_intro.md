---
authors:
- Fabio Bertolotti
- Kyle Myers
- Wei Yang Tham
doc_id: arxiv:2510.24916v1
family_id: arxiv:2510.24916
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Productivity Beliefs and Efficiency in Science
url_abs: http://arxiv.org/abs/2510.24916v1
url_html: https://arxiv.org/html/2510.24916v1
venue: arXiv q-fin
version: 1
year: 2025
---


Fabio Bertolotti



Kyle R. Myers



Wei Yang Tham



Bank of Italy



Harvard & NBER



Univ. of Toronto
Fabio Bertolotti: [fabiobertolotti@hotmail.it](mailto:fabiobertolotti@hotmail.it). Kyle Myers: [kmyers@hbs.edu](mailto:kmyers@hbs.edu). Wei Yang Tham: [weiyang.tham@rotman.utoronto.ca](mailto:weiyang.tham@rotman.utoronto.ca). This project received financial support from The Alfred P. Sloan Foundation and the Harvard Business School. There are no financial relationships or other potential conflicts of interest that apply to the authors. This project would not have been possible without the excellent work of Rachel Mural, Nina Cohodes, and Yilun Xu as well as input from Marie Thursby, Jerry Thursby, and Karim Lakhani. We received helpful comments from Nick Bloom, Judy Chevalier, Matt Clancy, Zoë Cullen, Shane Greenstein, Matt Grennan, Daniel Gross, Jorge Guzman, Bronwyn Hall, Sabrina Howell, Bruce Kogut, Petra Moser, David Rivers, Tim Simcoe, Chad Syverson, Joel Waldfogel, as well as seminar participants at Columbia, JOMT, MIT, the Workshop on the Organisation Economics and Policy of Scientific Research, the Banff Productivity Innovation and Economic Growth Conference, the NBER Productivity Lunch, Boston University TPRI, IIOC, Washington University in St. Louis, and the Conference on the Economics of Innovation in Memory of Zvi Griliches.

(September 2025)

We develop a method to estimate producers’ productivity beliefs when output quantities and input prices are unobservable, and we use it to evaluate the market for science. Our model of researchers’ labor supply shows how their willingness to pay for inputs reveals their productivity beliefs. We estimate the model’s parameters using data from a nationally representative survey of researchers and find the distribution of productivity to be very skewed. Our counterfactuals indicate that a more efficient allocation of the current budget could be worth billions of dollars. There are substantial gains from developing new ways of identifying talented scientists.

## Introduction

Science has continuously proven to be the engine of economic growth.111For motivating theory, see: Jones ([2005](https://arxiv.org/html/2510.24916v1#bib.bib34)). For a recent review, see: Bryan and Williams ([2021](https://arxiv.org/html/2510.24916v1#bib.bib13)). Academic science, in particular, is now a $100 billion engine for the United States (Gibbons and NCSES [2024](https://arxiv.org/html/2510.24916v1#bib.bib22)). How efficiently is this engine operating? How much more knowledge could be produced if we optimized the allocation of resources to better support the most talented scientists? In this paper, we formalize and answer these questions.

A long line of work has documented frictions in science; some researchers are denied resources for reasons plausibly unrelated to their productivity.222For example: Azoulay, Fons-Rosen, and Graff Zivin ([2019](https://arxiv.org/html/2510.24916v1#bib.bib8)); Hager, Schwarz, and Waldinger ([2024](https://arxiv.org/html/2510.24916v1#bib.bib25)). However, economists have struggled to quantify how much these frictions slow down the production of knowledge overall. Despite growing evidence that the *average* marginal returns to investments in science are significant, the *distribution* of marginal returns across researchers — estimates of each researcher’s productivity — has remained elusive. And without this distribution of marginal returns, we cannot make statements about efficiency in science.

Estimating researcher-level productivity in science using conventional methods (e.g., via factor shares or control functions) poses some major challenges. First, the output of science is difficult to observe; how does one quantify a unit of knowledge? Bibliometric data is commonly used; however, as noted by Adams and Griliches ([1998](https://arxiv.org/html/2510.24916v1#bib.bib3)), “*what constitutes a scientific paper makes for an elastic yardstick of scientific achievement*.” Second, scientific inputs are often not allocated via price mechanisms and researchers face large adjustment costs (Myers [2020](https://arxiv.org/html/2510.24916v1#bib.bib42); Baruffaldi and Gaessler [2025](https://arxiv.org/html/2510.24916v1#bib.bib9)). This severs the link between producers’ productivity and their observed input choices, which is at the core of conventional methods.

To overcome these challenges, we develop a new method for estimating productivity in teh absence of data on output quantities or inputs prices. The logic of our method is similar to conventional methods — producers’ input demand reveals information about their productivity. However, our approach involves a new step: the direct solicitation of producers’ willingness to pay (WTP) for inputs. This new step, combined with additional assumptions, allows us to recover the distribution of researcher-level productivity, which is very skewed, and quantify the value from more efficiently allocating inputs in science, which is very large.

To illustrate our approach clearly, the following simple example shows how soliciting producers’ WTP for some quantity of an input can be used to estimate their productivities:

> Profit maximizing producers are indexed by i\mst@varfam@dot{\mst@i}. Output () is produced using a single variable input () per the production function: =iii\mst@varfam@dot{}\_{\mst@i}={}\_{\mst@i}{}\_{\mst@i}, where i is the focal productivity parameter. Producers are price-takers and face a common output price (p>0\mst@varfam@dot{\mskip 2.0mu\mst@p\mskip 0.0mu}>0), which we can either observe or estimate. Input costs are heterogeneous and convex as given by: cii\mst@varfam@dot{}\_{\mst@i}^{{\mst@c}\_{\mst@i}}, where ci>1\mst@varfam@dot{\mst@c}\_{\mst@i}>1.
>
> We cannot observe the productivity or cost parameters (,ici\mst@varfam@dot{}\_{\mst@i},{\mst@c}\_{\mst@i}), and we can never observe output (i). Our goal is to estimate productivity (i).333Note that, even if we could also observe or estimate producers’ expected input choice, i∗\mst@varfam@dot{}^{\*}\_{\mst@i}, then the first order condition, =i∗(p⇑ici)1⇑(ci−1)\mst@varfam@dot{}^{\*}\_{\mst@i}=({\mskip 2.0mu\mst@p\mskip 0.0mu}{}\_{\mst@i}/{\mst@c}\_{\mst@i})^{1/({\mst@c}\_{\mst@i}-1)}, still does not separately identify the productivity and cost parameters (,ici\mst@varfam@dot{}\_{\mst@i},{\mst@c}\_{\mst@i}).
>
> Our solution is to solicit producers’ willingness to pay (WTPi\mst@varfam@dot\text{WTP}\_{\mst@i}) to obtain a fixed quantity of input from outside the market (e.g., from us, the experimenters). Consider an experiment where producers are asked to report their WTP to obtain 1 unit of in this way. Producers’ WTP will equate their profits inside the market whether or not they purchase the 1 unit of from outside the market. Formally, their WTPi\mst@varfam@dot\text{WTP}\_{\mst@i} should make the following equality hold: maxi(p−ii⌋ici=maxi(p(+i1)i−−iciWTPi⌋\mst@varfam@dot\max\_{{}\_{\mst@i}}\,[{\mskip 2.0mu\mst@p\mskip 0.0mu}{}\_{\mst@i}{}\_{{\mst@i}}-{}\_{{\mst@i}}^{{\mst@c}\_{\mst@i}}]=\max\_{{}\_{\mst@i}}\,[{\mskip 2.0mu\mst@p\mskip 0.0mu}{}\_{\mst@i}({}\_{{\mst@i}}+1)-{}\_{{\mst@i}}^{{\mst@c}\_{\mst@i}}-\text{WTP}\_{\mst@i}].
>
> This yields a simple expression for identifying producers’ productivity that does not require output quantities or input prices: =iWTPi⇑p\mst@varfam@dot{}\_{\mst@i}=\text{WTP}\_{\mst@i}/{\mskip 2.0mu\mst@p\mskip 0.0mu}.

The example above reflects the canonical setting of manufacturing firms producing physical goods that generate revenue via prices in the product market. But the underlying concept applies to science as well: researchers use their inputs to produce knowledge that generates utility via the incentive structures of science. Just as a firm’s WTP for inputs reveals their belief about how productively they can produce goods, a researcher’s WTP for scientific inputs reveals their belief about how productively they can produce knowledge.

In general, the mapping between productivity and willingness to pay for inputs is less transparent than in the simple example above. Below, we develop the general methodological framework that leverages this intuition. Our approach is not without limitations, and it requires some unconventional data. But engaging with these challenges can yield estimates of productivity in settings where other methods fail. We tailor our method to estimating productivity in science, but the general approach provides a path forward for productivity estimation in settings where heterogeneous producers (e.g., individual workers) obtain inputs that are not explicitly priced and generate output that is difficult to observe.

In order to apply this method to the market for science, we first present a new model of researchers’ production and consumption decisions. Researchers have heterogeneous preferences and derive utility from three sources: their salary, their scientific output (i.e., the quantity of knowledge they produce), and their leisure time. Researchers choose how to allocate their time across fundraising (e.g., writing grants), research, and leisure given their beliefs, budgets, and constraints. Each researcher has a unique production function with constant returns to scale, defined by two researcher-specific parameters: (i\mst@varfam@dot{\mst@i}) a funding-intensity parameter that determines the relative weight of the two key inputs, funding and time, and (i​i\mst@varfam@dot{\mst@i}{\mst@i}) a total factor productivity (TFP) parameter that describes the efficiency with which researchers produce scientific output using their inputs.

Using the model, we can write a researcher’s willingness to trade off their salary for inputs as a function of their productivity beliefs. This trade-off mirrors real decisions researchers make in the job market, and it forms the basis of the experiments that provide the variation necessary to identify the model’s parameters. By identifying researchers’ input demand via their WTP, we can handle the fact that inputs are not explicitly priced. Moreover, since the survey also solicits researchers’ actual input levels, we can still estimate researchers’ scientific output despite the fact that we never need to observe the knowledge they expect to produce. Throughout the paper, we highlight several important limitations to our general approach and the specific model.

In order to generate the data necessary to estimate the model, we make use of a nationally representative survey of research-active professors across all major fields of science at roughly 150 major institutions of higher education in the US; for details, see Myers et al. ([2023](https://arxiv.org/html/2510.24916v1#bib.bib43)).444Evidence is provided in Myers et al. ([2023](https://arxiv.org/html/2510.24916v1#bib.bib43)) suggesting the presence of non-response bias in the sample is very low on observable dimensions such as institutional rank, grant funding, and publication rates; some of this is reprinted in the Appendix. The survey recruitment included randomized incentives and reminders, which we use to test for sample selection per Heckman ([1979](https://arxiv.org/html/2510.24916v1#bib.bib27)) and find little evidence of any sample selection bias. The survey solicits researchers’ salaries, time allocations, and access to inputs. Importantly, the survey also includes a series of hypothetical experiments that solicit researchers’ willingness to trade off their salary for more research funding or fewer administrative duties.

Researchers’ willingness to pay for inputs are of plausible magnitudes and behavior. The median researcher is willing to pay 10
cents for $1 of research funding and $68
for one less hour of administrative duties. The components of the model explain a large fraction of the variation in researchers’ responses (82–96
%) and, for the most part, responses do not appear to reflect sample selection or systematic noise in respondents’ willingness to pay for any hypothetical good. Furthermore, researchers’ willingness to pay for free time is strongly correlated with their implied hourly wages as expected.555We also implement [Dizon-Ross and Jayachandran](https://arxiv.org/html/2510.24916v1#bib.bib20)’s ([2022](https://arxiv.org/html/2510.24916v1#bib.bib20)) approach of using a “benchmark good” as a part of our willingness-to-pay elicitation to test whether respondents exhibit systematic noise in their stated preferences.

Our estimates of productivity beliefs vary widely across researchers, even after accounting for outliers. Within major fields of study, the ratio of the 90th and 10th percentile of TFP is approximately 52
. When we look in narrower fields of study and attempt to control for other sources of heterogeneity, we estimate 90–10 TFP ratios to be approximately 29
. This represents a high degree of dispersion compared to what is observed in commercial markets at the firm-level (e.g., Syverson [2011](https://arxiv.org/html/2510.24916v1#bib.bib54)); however, this scale of dispersion in productivity across individual workers has been observed in some high-skilled settings (e.g., Sackman, Erikson, and Grant [1968](https://arxiv.org/html/2510.24916v1#bib.bib50)). Motivated by Gabaix ([2009](https://arxiv.org/html/2510.24916v1#bib.bib21)), we investigate the upper tail of the TFP distribution and find it to exhibit power laws.

As a sign of face validity, our productivity estimates are positively correlated with common metrics of knowledge production (e.g., publications, citations, grant funding) and exhibits a similar degree of dispersion as those metrics. Notably, our estimates indicate that approximately half of the variance in scientific output across individual researchers is due to variance in their productivity.666We are unable to distinguish the degree to which our productivity estimates reflects an individual’s fixed capabilities as a researcher versus any cumulative advantage they have acquired (c.f., Hall and Mairesse [2024](https://arxiv.org/html/2510.24916v1#bib.bib26)). The high degree of dispersion suggests that it may be hard for the market to facilitate positive selection on productivity.

To evaluate allocative efficiency, we compare inputs and outputs under actual allocations, to those under alternative allocations. Specifically, we consider two alternative objectives: (i\mst@varfam@dot{\mst@i}) maximize total scientific output, or (i​i\mst@varfam@dot{\mst@i}{\mst@i}) maximize researchers’ private utility. Using the model, we can solve for the allocation of inputs that achieves an objective while allowing for researchers’ behavioral responses as they re-optimize their choices.

Overall, we find evidence of a moderate degree of efficiency given our proposed objectives. The correlations between researchers’ actual input levels and the optima implied by our model generally span 0.4–0.8
; more productive researchers acquire more inputs on average. However, there are significant gains from alternative allocations. Our counterfactuals suggest that total annual scientific output could be increased by approximately 160
%. The private value to researchers of this additional output is on the scale of 5
%. Estimating the social value of this growth requires assumptions about externalities, which we explore.

To provide another way of characterizing the gains from reallocation, we ask the following: how much would funding levels need to increase under actual allocations to produce the same growth in output as our alternative allocations that hold input levels fixed? We find that aggregate funding levels would need to increase roughly 40%
to achieve the same growth in output our alternative allocations can achieve. That we can obtain a 160
% growth in aggregate output from a 40%
increase in aggregate funding is due to the combination of a mechanical composition effect and a endogenous behavioral response, which we detail further. Conservative approaches to scaling these estimates to the size of the population imply gains from reallocation that are equivalent to multi-billion dollar increases in annual funding.

We also evaluate the degree to which differences in aggregate output across major fields of study are due to differences in the number of researchers, their productivities, their input levels, or the fields’ allocative efficiency. Overall, differences in allocative efficiency are the largest determinant of differences in aggregate output. At efficient allocations, the gaps in output between fields shrink by 20–50%.

Lastly, we unpack the counterfactuals to explore the following questions: Is the efficient allocation of inputs implied by the model more or less concentrated than the actual allocation? How does the reallocation of each input (i.e., funding and time) independently change the results? How much does the efficient allocation change under different objectives? What is the distribution of input wedges (i.e., the difference between their optimal and actual input levels) across researchers? Are researchers’ input wedges predictable given their observable features?

Our estimates come with many caveats due to our method and setting. First, we face a set of challenges common to all existing productivity estimation techniques.777Specifically: (i\mst@varfam@dot{\mst@i}) noise due to mismeasurement or misspecification; (i​i\mst@varfam@dot{\mst@i}{\mst@i}) the presence of unmeasured, tradable inputs; and (i​i​i\mst@varfam@dot{\mst@i}{\mst@i}{\mst@i}) the presence of unmodeled heterogeneity in output prices (or preferences over payoffs). Second, we face some unique limitations: (i\mst@varfam@dot{\mst@i}) our method provides only ex-ante productivity beliefs and has no way of identifying ex-post differences in production; and (i​i\mst@varfam@dot{\mst@i}{\mst@i}) the identifying variation in our data is based on stated preferences from hypothetical experiments, which may suffer from a range of biases. Throughout the paper we engage with these limitations by providing robustness tests of our assumptions and face validity tests of the data. Overall, the results from these tests give us confidence in our conclusions. Still, we interpret our results as plausible upper bounds on the productivity dispersion and gains from reallocation in science. Given the dearth of quantitative evidence on these points, we view this as an important step forward.

After a brief review of our connection to the literature, the rest of the paper proceeds as follows: Section [2](https://arxiv.org/html/2510.24916v1#S2 "Methodological Framework ‣ Productivity Beliefs and Efficiency in Science") provides the general framework of and key assumptions underpinning our methodology; Section [3](https://arxiv.org/html/2510.24916v1#S3 "Survey and Data Overview ‣ Productivity Beliefs and Efficiency in Science") details the survey data; Section [4](https://arxiv.org/html/2510.24916v1#S4 "Model of Science ‣ Productivity Beliefs and Efficiency in Science") describes our model of researchers’ production and consumption; Section [5](https://arxiv.org/html/2510.24916v1#S5 "Survey Experiment ‣ Productivity Beliefs and Efficiency in Science") describes and reports the results of the survey experiments; Section [6](https://arxiv.org/html/2510.24916v1#S6 "Estimates for the Model of Science ‣ Productivity Beliefs and Efficiency in Science") provides the model estimates; Section [7](https://arxiv.org/html/2510.24916v1#S7 "Counterfactuals and Allocative Efficiency ‣ Productivity Beliefs and Efficiency in Science") contains our counterfactual allocation exercises; and Section [8](https://arxiv.org/html/2510.24916v1#S8 "Discussion ‣ Productivity Beliefs and Efficiency in Science") concludes with a discussion of our results and the usefulness of our methodology more generally.

### Related Literature

Our paper sits at the intersection of two bodies of literature: empirical studies of science and markets for innovation (i.e., Merton [1973](https://arxiv.org/html/2510.24916v1#bib.bib41); Stephan [1996](https://arxiv.org/html/2510.24916v1#bib.bib53); Bryan and Williams [2021](https://arxiv.org/html/2510.24916v1#bib.bib13)); and economic studies of producers’ productivity and factor misallocation (i.e., Syverson [2011](https://arxiv.org/html/2510.24916v1#bib.bib54); Restuccia and Rogerson [2017](https://arxiv.org/html/2510.24916v1#bib.bib49); De Loecker and Syverson [2021](https://arxiv.org/html/2510.24916v1#bib.bib17)).

The meta-science literature has long been interested in misallocation. Following a long line of sociological work (Merton [1973](https://arxiv.org/html/2510.24916v1#bib.bib41); Zuckerman [1988](https://arxiv.org/html/2510.24916v1#bib.bib58); Shapin [1995](https://arxiv.org/html/2510.24916v1#bib.bib51)) economists have quantified some status-based frictions (Azoulay, Fons-Rosen, and Graff Zivin [2019](https://arxiv.org/html/2510.24916v1#bib.bib8)) and have also studied potential frictions such as: political lobbying (Hegde and Sampat [2015](https://arxiv.org/html/2510.24916v1#bib.bib28)), information asymmetries regarding researchers’ output (Hager, Schwarz, and Waldinger [2024](https://arxiv.org/html/2510.24916v1#bib.bib25)), and competitive pressures from priority-based credit mechanisms (Hill and Stein [2025](https://arxiv.org/html/2510.24916v1#bib.bib29)).

Looking towards the productivity literature, our methodology is centered on understanding producers’ factor demand. This concept is at the core of prevailing methods for estimating productivity, where identification can depend on input cost shares (e.g., Hsieh and Klenow [2009](https://arxiv.org/html/2510.24916v1#bib.bib31)) or the inversion of input demand into control functions (e.g., Olley and Pakes [1996](https://arxiv.org/html/2510.24916v1#bib.bib46); Levinsohn and Petrin [2003](https://arxiv.org/html/2510.24916v1#bib.bib39); Ackerberg, Caves, and Frazer [2015](https://arxiv.org/html/2510.24916v1#bib.bib2)). Much work has been done to extend these methods to account for features such as unobservable prices (De Loecker et al. [2016](https://arxiv.org/html/2510.24916v1#bib.bib16)), adjustment costs (Petrin and Sivadasan [2013](https://arxiv.org/html/2510.24916v1#bib.bib47); Asker, Collard-Wexler, and De Loecker [2014](https://arxiv.org/html/2510.24916v1#bib.bib5)), as well as measurement error and heterogeneity (Kim, Petrin, and Song [2016](https://arxiv.org/html/2510.24916v1#bib.bib35); Gollin and Udry [2021](https://arxiv.org/html/2510.24916v1#bib.bib23)). To our knowledge, we are the first to formalize an approach for estimating production functions without data on output quantities and input prices.

We also follow a growing body of work using surveys to study the determinants of productivity in settings with inputs and outputs that are subjective or difficult to measure (e.g., Bloom, Sadun, and Van Reenen [2012](https://arxiv.org/html/2510.24916v1#bib.bib12); Atkin, Khandelwal, and Osman [2019](https://arxiv.org/html/2510.24916v1#bib.bib7)). We are not the first to solicit producers’ WTP for inputs (c.f., Cole et al. [2013](https://arxiv.org/html/2510.24916v1#bib.bib15); Wossen et al. [2024](https://arxiv.org/html/2510.24916v1#bib.bib57)); however, those studies tend to have an inherent interest in producers’ demand for a specific input. Our work also runs parallel to the development of methods that use (quasi-)experimental variation to estimate misallocation (e.g., Sraer and Thesmar [2023](https://arxiv.org/html/2510.24916v1#bib.bib52); Carrillo et al. [2023](https://arxiv.org/html/2510.24916v1#bib.bib14)).

## Methodological Framework

In this section, we describe a producer’s optimization problem and show how their productivity can be estimated by using information about their WTP for a fixed amount of inputs. The setup is general; the producers of interest may be organizations or individuals. Our approach requires four key assumptions that we describe in detail.

### Setup

Our goal is to estimate producers’ productivity beliefs: their rational expectations about their productivity in a future period of production. Rational expectations implies that producers have known beliefs about relevant variables; for example, a business manager can answer the question “*how many employees do you plan to have for next year?*”, or an individual researcher can answer the question “*how many hours per week do you plan to spend on your work next semester?*” Despite revolving around forecasts, we present the framework as static; there is no dynamic optimization.888We also omit the expectation operator despite variables being forecasts.

There are producers indexed by i\mst@varfam@dot{\mst@i}. For simplicity, we focus on the case where the producer uses a single, variable input to produce some quantity of output; extensions to multiple inputs and stocks are possible. Producers have heterogeneous production functions with a Hicks-neutral total factor productivity (TFP) term: =ifi(,i𝛍i)\mst@varfam@dot{}\_{\mst@i}={}\_{\mst@i}{\mskip 3.0mu\mst@f\mskip 0.0mu}({}\_{\mst@i},\bm{\upmu}\_{\mst@i}), which is monotonically increasing in .999Thus, i is a TFP-Quantity (TFPQ) parameter. Heterogeneity depends on the vector 𝛍i\mst@varfam@dot\bm{\upmu}\_{\mst@i}, which can include producers’ observable characteristics i and some common parameters designated 𝛍\mst@varfam@dot\bm{\upmu}. Estimating the productivity parameter i is our primary goal.

Payoff from production is governed by a benefit function b(,i,ii𝛍i)\mst@varfam@dot{\mst@b}({}\_{\mst@i},{}\_{\mst@i}{}\_{\mst@i},\bm{\upmu}\_{\mst@i}), which depends on output prices (i) and output quantity (i), some endowment of liquid capital that is valued by the producer and guaranteed regardless of output (i), and parameters 𝛍i\mst@varfam@dot\bm{\upmu}\_{\mst@i}. For a business, i could reflect cash reserves and the benefit function can be viewed as a generalized revenue function that includes value to the business from these cash reserves. For individual researchers, i could reflect their guaranteed salary and the benefit function describes their utility from their salary as well as any additional benefits that they expect to receive from producing more output (e.g., prestige, expectations of a promotion).101010For simplicity, we do not allow for financial markets, but they could be incorporated. Total costs depend on an input cost function c(,i𝛍i)\mst@varfam@dot{\mst@c}({}\_{\mst@i},\bm{\upmu}\_{\mst@i}) and there may also be constraints on input levels denoted by g(,i𝛍i)=0\mst@varfam@dot{\mst@g}({}\_{\mst@i},\bm{\upmu}\_{\mst@i})=0.

Thus, producers choose input levels that maximize their payoff per:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | maxi\displaystyle\max\_{{}\_{\mst@i}} | b(,ifiii()i,𝛍i)−c(,i𝛍i)\displaystyle{\mst@b}\bigl({}\_{\mst@i},{}\_{\mst@i}{}\_{\mst@i}{\mskip 3.0mu\mst@f\mskip 0.0mu}\_{\mst@i}({}\_{\mst@i}),\bm{\upmu}\_{\mst@i}\bigr)-{\mst@c}({}\_{\mst@i},\bm{\upmu}\_{\mst@i}) |  | (1) |
|  |  | subject tog(,i𝛍i)=0,\displaystyle\text{subject to}\;\;{\mst@g}({}\_{\mst@i},\bm{\upmu}\_{\mst@i})=0\;, |  |

where we will define i∗\mst@varfam@dot{}^{\*}\_{\mst@i} as the argument that maximizes Eq. ([1](https://arxiv.org/html/2510.24916v1#S2.E1 "In Setup ‣ Methodological Framework ‣ Productivity Beliefs and Efficiency in Science")). Next, we walk through the key assumptions of our framework that facilitate identification of the focal productivity parameter i based on producers’ WTP for additional units of the input from us, the experimenters.

#### Assumption 1 — Observable Plans

*Producers’ optimal input plans i∗\mst@varfam@dot{}^{\*}\_{\mst@i} are observable*. Variation in planned input levels (absent the WTP experiment) are necessary.111111There are some knife-edge cases where input plans need not be observed, such as the example in the Introduction. However, those cases are likely rare in practice.

#### Assumption 2 — Output Prices

*Producers are price takers and output prices are either observable or depend on observable covariates.* Our framework does not allow for unobservable horizontal differentiation as we would not be able to separately identify producer-specific output prices and productivity. Prices must either be observable (and assumed to reflect all quality differences) or homogeneous conditional on other observables, so that productivity reflects all quality differences (and producers are producing a commodity).

#### Assumption 3 — Convex Input Costs

*The direct costs of inputs are convex: c(,i𝛍i)>0\mst@varfam@dot{\mst@c}({}\_{\mst@i},\bm{\upmu}\_{\mst@i})>0 and c(,i𝛍i)>0\mst@varfam@dot{\mst@c}({}\_{\mst@i},\bm{\upmu}\_{\mst@i})>0.* These convexities can be due to any sort of friction or adjustment cost. If this assumption does not hold, then the producer’s WTP in the experiment may not depend on their productivity, as we illustrate below.121212This is perhaps the least intuitive of our assumptions. Formally, this assumption ensures the necessary rank condition for estimation. Intuitively, the WTP experiment operates via an implicit linear cost schedule, so if the producer already faces a linear cost schedule in the actual input market, our WTP experiment will simply reflect those linear costs. It is trivial to show that if a producer uses a single input and faces a linear price for that input, then their WTP will not depend on their productivity, because they will simply report the price they face in their input market (i.e., the producer would never pay us, the experimenters, more for an input than what they pay in their own input market).

#### Assumption 4 — Monotonic Payoffs

*The benefit function b​()\mst@varfam@dot{\mst@b}(\cdot) is strictly monotonically increasing in i and i.* This implies that more output or more liquid resources always increases the producers’ payoff and, furthermore, that b​()\mst@varfam@dot{\mst@b}(\cdot) is invertible.131313Extensions to settings where producers have market power may be possible.

### Productivity and First Order Conditions

In what follows, we assume there are no constraints on the producer and we set the output price to 1 as the numeraire in order to keep our expressions simpler. Solving the first order conditions of the producer’s problem (Eq. [1](https://arxiv.org/html/2510.24916v1#S2.E1 "In Setup ‣ Methodological Framework ‣ Productivity Beliefs and Efficiency in Science")), sans constraints, yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | bi(,ifi(,i𝛍i),𝛍i)f(,i𝛍i)−c(,i𝛍i)=0,\mst@varfam@dot{}\_{\mst@i}{\mst@b}\bigl({}\_{\mst@i},{}\_{\mst@i}{\mskip 3.0mu\mst@f\mskip 0.0mu}({}\_{\mst@i},\bm{\upmu}\_{\mst@i}),\bm{\upmu}\_{\mst@i}\bigr){\mskip 3.0mu\mst@f\mskip 0.0mu}({}\_{\mst@i},\bm{\upmu}\_{\mst@i})-{\mst@c}({}\_{\mst@i},\bm{\upmu}\_{\mst@i})=0\;, |  | (2) |

which shows that productivity (i) is an implicit function of observables and the unknown parameters 𝛍i\mst@varfam@dot\bm{\upmu}\_{\mst@i} that govern the functions b\mst@varfam@dot{\mst@b},f\mst@varfam@dot{\mskip 3.0mu\mst@f\mskip 0.0mu}, and c\mst@varfam@dot{\mst@c}. This illustrates the value of Assumptions 1 and 2, but still leaves productivity unidentified due to the unknown parameters in 𝛍i\mst@varfam@dot\bm{\upmu}\_{\mst@i}.

### WTP Solicitation

In order to identify the productivity and other parameters in Eq. [2](https://arxiv.org/html/2510.24916v1#S2.E2 "In Productivity and First Order Conditions ‣ Methodological Framework ‣ Productivity Beliefs and Efficiency in Science"), we experimentally solicit producers’ WTP for a fixed quantity of the input outside their input market (e.g., directly from us, the experimenters). For example, we offer the producer units of the input and solicit their WTP (e.g., via stated preferences or incentive-compatible revealed preferences).

To see the value of this experiment, first consider the producer’s optimization problem in the scenario where they choose to pay their WTP to purchase inputs from us:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | maxwidetildei\displaystyle\max\_{\widetilde{{\mst@X}}\_{\mst@i}} | b(−i,ifi(widetildei+,𝛍i),𝛍i)−c(widetildei,𝛍i),\displaystyle{\mst@b}({}\_{\mst@i}-{\mst@W}{\mst@T}{}\_{\mst@i},{}\_{\mst@i}{\mskip 3.0mu\mst@f\mskip 0.0mu}(\widetilde{{\mst@X}}\_{\mst@i}+\mst@Delta,\bm{\upmu}\_{\mst@i}),\bm{\upmu}\_{\mst@i})-{\mst@c}(\widetilde{{\mst@X}}\_{\mst@i},\bm{\upmu}\_{\mst@i})\;, |  | (3) |

where we define widetildei∗\mst@varfam@dot\widetilde{{\mst@X}}^{\*}\_{\mst@i} as the argument that maximizes Eq. ([3](https://arxiv.org/html/2510.24916v1#S2.E3 "In WTP Solicitation ‣ Methodological Framework ‣ Productivity Beliefs and Efficiency in Science")). In this scenario, the producer’s i is subtracted from their i since they are both in monetary units and are perfect substitutes in the benefit function. The inputs purchased, , are added to the production function, but the producer’s cost function c\mst@varfam@dot{\mst@c} still only depends on the quantity of inputs they choose to purchase in the market.

Therefore, the producer’s WTP for units of the input equates the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | b(i,if(∗i,𝛍i),𝛍i)−c(∗i,𝛍i)\@mathmeasureb(Mi, i f(X\*i,μi),μi) - c(X\*i,μi)\@mathmeasure\@mathmeasure\@mathmeasure\@mathmeasure\@mathmeasureexpected payoff inno-purchase scenario=b(i−i,if(widetilde∗i+,𝛍i),𝛍i)−c(widetilde∗i,𝛍i)\@mathmeasureb(Mi-WTPi,i f(X\*i+,μi),μi) - c(X\*i,μi)\@mathmeasure\@mathmeasure\@mathmeasure\@mathmeasure\@mathmeasureexpected payoff inscenario paying for .\displaystyle\mathop{\mathchoice{\vtop{\halign{#\cr$\hfil\displaystyle{\mst@b}({}\_{\mst@i},{}\_{\mst@i}{\mskip 3.0mu\mst@f\mskip 0.0mu}({}^{\*}\_{\mst@i},\bm{\upmu}\_{\mst@i}),\bm{\upmu}\_{\mst@i})-{\mst@c}({}^{\*}\_{\mst@i},\bm{\upmu}\_{\mst@i})\hfil$\crcr\kern 2.0pt\cr\@mathmeasure\displaystyle{b(M\_{i}, {}\_{i} f(X^{\*}\_{i},\bm{\upmu}\_{i}),\bm{\upmu}\_{i}) - c(X^{\*}\_{i},\bm{\upmu}\_{i})}\@mathmeasure\displaystyle{\upbrace}\@mathmeasure\displaystyle{\upbraceg}\@mathmeasure\displaystyle{\upbracegg}\@mathmeasure\displaystyle{\upbraceggg}\@mathmeasure\displaystyle{\upbracegggg}$\displaystyle\bracelu\leaders{\hbox{$\bracemid$}}{\hfill}\bracemu\leaders{\hbox{$\bracemid$}}{\hfill}\braceru$\crcr}}}{\vtop{\halign{#\cr$\hfil\textstyle{\mst@b}({}\_{\mst@i},{}\_{\mst@i}{\mskip 3.0mu\mst@f\mskip 0.0mu}({}^{\*}\_{\mst@i},\bm{\upmu}\_{\mst@i}),\bm{\upmu}\_{\mst@i})-{\mst@c}({}^{\*}\_{\mst@i},\bm{\upmu}\_{\mst@i})\hfil$\crcr\kern 2.0pt\cr\@mathmeasure\textstyle{b(M\_{i}, {}\_{i} f(X^{\*}\_{i},\bm{\upmu}\_{i}),\bm{\upmu}\_{i}) - c(X^{\*}\_{i},\bm{\upmu}\_{i})}\@mathmeasure\textstyle{\upbrace}\@mathmeasure\textstyle{\upbraceg}\@mathmeasure\textstyle{\upbracegg}\@mathmeasure\textstyle{\upbraceggg}\@mathmeasure\textstyle{\upbracegggg}$\textstyle\bracelu\leaders{\hbox{$\bracemid$}}{\hfill}\bracemu\leaders{\hbox{$\bracemid$}}{\hfill}\braceru$\crcr}}}{\vtop{\halign{#\cr$\hfil\scriptstyle{\mst@b}({}\_{\mst@i},{}\_{\mst@i}{\mskip 3.0mu\mst@f\mskip 0.0mu}({}^{\*}\_{\mst@i},\bm{\upmu}\_{\mst@i}),\bm{\upmu}\_{\mst@i})-{\mst@c}({}^{\*}\_{\mst@i},\bm{\upmu}\_{\mst@i})\hfil$\crcr\kern 2.0pt\cr\@mathmeasure\scriptstyle{b(M\_{i}, {}\_{i} f(X^{\*}\_{i},\bm{\upmu}\_{i}),\bm{\upmu}\_{i}) - c(X^{\*}\_{i},\bm{\upmu}\_{i})}\@mathmeasure\scriptstyle{\upbrace}\@mathmeasure\scriptstyle{\upbraceg}\@mathmeasure\scriptstyle{\upbracegg}\@mathmeasure\scriptstyle{\upbraceggg}\@mathmeasure\scriptstyle{\upbracegggg}$\scriptstyle\bracelu\leaders{\hbox{$\bracemid$}}{\hfill}\bracemu\leaders{\hbox{$\bracemid$}}{\hfill}\braceru$\crcr}}}{\vtop{\halign{#\cr$\hfil\scriptscriptstyle{\mst@b}({}\_{\mst@i},{}\_{\mst@i}{\mskip 3.0mu\mst@f\mskip 0.0mu}({}^{\*}\_{\mst@i},\bm{\upmu}\_{\mst@i}),\bm{\upmu}\_{\mst@i})-{\mst@c}({}^{\*}\_{\mst@i},\bm{\upmu}\_{\mst@i})\hfil$\crcr\kern 2.0pt\cr\@mathmeasure\scriptscriptstyle{b(M\_{i}, {}\_{i} f(X^{\*}\_{i},\bm{\upmu}\_{i}),\bm{\upmu}\_{i}) - c(X^{\*}\_{i},\bm{\upmu}\_{i})}\@mathmeasure\scriptscriptstyle{\upbrace}\@mathmeasure\scriptscriptstyle{\upbraceg}\@mathmeasure\scriptscriptstyle{\upbracegg}\@mathmeasure\scriptscriptstyle{\upbraceggg}\@mathmeasure\scriptscriptstyle{\upbracegggg}$\scriptscriptstyle\bracelu\leaders{\hbox{$\bracemid$}}{\hfill}\bracemu\leaders{\hbox{$\bracemid$}}{\hfill}\braceru$\crcr}}}}\limits\_{\begin{{\mst@s}{\mst@u}{\mst@b}{\mst@a}{\mst@r}{\mst@r}{\mst@a}{\mskip 2.0mu\mst@y\mskip 0.0mu}}{{\mst@c}}\text{expected payoff in}\\ \text{no-purchase scenario}\end{{\mst@s}{\mst@u}{\mst@b}{\mst@a}{\mst@r}{\mst@r}{\mst@a}{\mskip 2.0mu\mst@y\mskip 0.0mu}}}=\mathop{\mathchoice{\vtop{\halign{#\cr$\hfil\displaystyle{\mst@b}({}\_{\mst@i}-{\mst@W}{\mst@T}{}\_{\mst@i},{}\_{\mst@i}{\mskip 3.0mu\mst@f\mskip 0.0mu}(\widetilde{{\mst@X}}^{\*}\_{\mst@i}+\mst@Delta,\bm{\upmu}\_{\mst@i}),\bm{\upmu}\_{\mst@i})-{\mst@c}(\widetilde{{\mst@X}}^{\*}\_{\mst@i},\bm{\upmu}\_{\mst@i})\hfil$\crcr\kern 2.0pt\cr\@mathmeasure\displaystyle{b(M\_{i}-WTP\_{i},{}\_{i} f(\widetilde{X}^{\*}\_{i}+\mst@Delta,\bm{\upmu}\_{i}),\bm{\upmu}\_{i}) - c(\widetilde{X}^{\*}\_{i},\bm{\upmu}\_{i})}\@mathmeasure\displaystyle{\upbrace}\@mathmeasure\displaystyle{\upbraceg}\@mathmeasure\displaystyle{\upbracegg}\@mathmeasure\displaystyle{\upbraceggg}\@mathmeasure\displaystyle{\upbracegggg}$\displaystyle\bracelu\leaders{\hbox{$\bracemid$}}{\hfill}\bracemu\leaders{\hbox{$\bracemid$}}{\hfill}\braceru$\crcr}}}{\vtop{\halign{#\cr$\hfil\textstyle{\mst@b}({}\_{\mst@i}-{\mst@W}{\mst@T}{}\_{\mst@i},{}\_{\mst@i}{\mskip 3.0mu\mst@f\mskip 0.0mu}(\widetilde{{\mst@X}}^{\*}\_{\mst@i}+\mst@Delta,\bm{\upmu}\_{\mst@i}),\bm{\upmu}\_{\mst@i})-{\mst@c}(\widetilde{{\mst@X}}^{\*}\_{\mst@i},\bm{\upmu}\_{\mst@i})\hfil$\crcr\kern 2.0pt\cr\@mathmeasure\textstyle{b(M\_{i}-WTP\_{i},{}\_{i} f(\widetilde{X}^{\*}\_{i}+\mst@Delta,\bm{\upmu}\_{i}),\bm{\upmu}\_{i}) - c(\widetilde{X}^{\*}\_{i},\bm{\upmu}\_{i})}\@mathmeasure\textstyle{\upbrace}\@mathmeasure\textstyle{\upbraceg}\@mathmeasure\textstyle{\upbracegg}\@mathmeasure\textstyle{\upbraceggg}\@mathmeasure\textstyle{\upbracegggg}$\textstyle\bracelu\leaders{\hbox{$\bracemid$}}{\hfill}\bracemu\leaders{\hbox{$\bracemid$}}{\hfill}\braceru$\crcr}}}{\vtop{\halign{#\cr$\hfil\scriptstyle{\mst@b}({}\_{\mst@i}-{\mst@W}{\mst@T}{}\_{\mst@i},{}\_{\mst@i}{\mskip 3.0mu\mst@f\mskip 0.0mu}(\widetilde{{\mst@X}}^{\*}\_{\mst@i}+\mst@Delta,\bm{\upmu}\_{\mst@i}),\bm{\upmu}\_{\mst@i})-{\mst@c}(\widetilde{{\mst@X}}^{\*}\_{\mst@i},\bm{\upmu}\_{\mst@i})\hfil$\crcr\kern 2.0pt\cr\@mathmeasure\scriptstyle{b(M\_{i}-WTP\_{i},{}\_{i} f(\widetilde{X}^{\*}\_{i}+\mst@Delta,\bm{\upmu}\_{i}),\bm{\upmu}\_{i}) - c(\widetilde{X}^{\*}\_{i},\bm{\upmu}\_{i})}\@mathmeasure\scriptstyle{\upbrace}\@mathmeasure\scriptstyle{\upbraceg}\@mathmeasure\scriptstyle{\upbracegg}\@mathmeasure\scriptstyle{\upbraceggg}\@mathmeasure\scriptstyle{\upbracegggg}$\scriptstyle\bracelu\leaders{\hbox{$\bracemid$}}{\hfill}\bracemu\leaders{\hbox{$\bracemid$}}{\hfill}\braceru$\crcr}}}{\vtop{\halign{#\cr$\hfil\scriptscriptstyle{\mst@b}({}\_{\mst@i}-{\mst@W}{\mst@T}{}\_{\mst@i},{}\_{\mst@i}{\mskip 3.0mu\mst@f\mskip 0.0mu}(\widetilde{{\mst@X}}^{\*}\_{\mst@i}+\mst@Delta,\bm{\upmu}\_{\mst@i}),\bm{\upmu}\_{\mst@i})-{\mst@c}(\widetilde{{\mst@X}}^{\*}\_{\mst@i},\bm{\upmu}\_{\mst@i})\hfil$\crcr\kern 2.0pt\cr\@mathmeasure\scriptscriptstyle{b(M\_{i}-WTP\_{i},{}\_{i} f(\widetilde{X}^{\*}\_{i}+\mst@Delta,\bm{\upmu}\_{i}),\bm{\upmu}\_{i}) - c(\widetilde{X}^{\*}\_{i},\bm{\upmu}\_{i})}\@mathmeasure\scriptscriptstyle{\upbrace}\@mathmeasure\scriptscriptstyle{\upbraceg}\@mathmeasure\scriptscriptstyle{\upbracegg}\@mathmeasure\scriptscriptstyle{\upbraceggg}\@mathmeasure\scriptscriptstyle{\upbracegggg}$\scriptscriptstyle\bracelu\leaders{\hbox{$\bracemid$}}{\hfill}\bracemu\leaders{\hbox{$\bracemid$}}{\hfill}\braceru$\crcr}}}}\limits\_{\begin{{\mst@s}{\mst@u}{\mst@b}{\mst@a}{\mst@r}{\mst@r}{\mst@a}{\mskip 2.0mu\mst@y\mskip 0.0mu}}{{\mst@c}}\text{expected payoff in}\\ \text{scenario paying ${\mst@W}{\mst@T}{\mst@P}$ for $\mst@Delta$}\end{{\mst@s}{\mst@u}{\mst@b}{\mst@a}{\mst@r}{\mst@r}{\mst@a}{\mskip 2.0mu\mst@y\mskip 0.0mu}}}\;. |  | (4) |

That is, their WTP equates their net expected payoff in both (i\mst@varfam@dot{\mst@i}) the scenario where they don’t purchase the inputs from us (left-hand side of Eq. [4](https://arxiv.org/html/2510.24916v1#S2.E4 "In WTP Solicitation ‣ Methodological Framework ‣ Productivity Beliefs and Efficiency in Science")) and (i​i\mst@varfam@dot{\mst@i}{\mst@i}) the scenario where they do purchase from us (right-hand side of Eq. [4](https://arxiv.org/html/2510.24916v1#S2.E4 "In WTP Solicitation ‣ Methodological Framework ‣ Productivity Beliefs and Efficiency in Science")). Assumption 3 — convex input costs — guarantees that the i that solves Eq. ([4](https://arxiv.org/html/2510.24916v1#S2.E4 "In WTP Solicitation ‣ Methodological Framework ‣ Productivity Beliefs and Efficiency in Science")) depends on productivity (i) and, therefore, on the parameters in i\mst@varfam@dot\bm{\mst@mu}\_{\mst@i} per Eq. ([2](https://arxiv.org/html/2510.24916v1#S2.E2 "In Productivity and First Order Conditions ‣ Methodological Framework ‣ Productivity Beliefs and Efficiency in Science")).141414In the Appendix, we show how linear cost functions yield corner solutions for producers’ that do not reflect their productivity and instead reflect the linear input costs the producers face in their market.

### Estimation

As written, identifying the productivity term (i) from Eq. ([4](https://arxiv.org/html/2510.24916v1#S2.E4 "In WTP Solicitation ‣ Methodological Framework ‣ Productivity Beliefs and Efficiency in Science")) appears challenging because it depends on two unobserved components: (i\mst@varfam@dot{\mst@i}) the producer’s optimal input choice in the purchase scenario (widetildei∗\mst@varfam@dot\widetilde{{\mst@X}}^{\*}\_{\mst@i}), and (i​i\mst@varfam@dot{\mst@i}{\mst@i}) the unknown parameters of 𝛍i\mst@varfam@dot\bm{\upmu}\_{\mst@i}.151515Recall, the vector 𝛍i\mst@varfam@dot\bm{\upmu}\_{\mst@i} includes unknown common parameters 𝛍\mst@varfam@dot\bm{\upmu} and observable individual-specific attributes i. However, we know that widetildei∗\mst@varfam@dot\widetilde{{\mst@X}}^{\*}\_{\mst@i} — the solution to Eq. ([3](https://arxiv.org/html/2510.24916v1#S2.E3 "In WTP Solicitation ‣ Methodological Framework ‣ Productivity Beliefs and Efficiency in Science")) — is itself an implicit function of productivity (i), the amount of input offered (), and the vector 𝛍i\mst@varfam@dot\bm{\upmu}\_{\mst@i}.

Per Assumption 4 — the benefit function (b\mst@varfam@dot{\mst@b}) is invertible — we can write a producer’s i as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | =i(,,i,i∗,i𝛍i)widehat(,,i,i∗,i𝛍i),\mst@varfam@dot{\mst@W}{\mst@T}{}\_{\mst@i}=\mst@Pi(\mst@Delta,{}\_{\mst@i},{}^{\*}\_{\mst@i},{}\_{\mst@i},\bm{\upmu}\_{\mst@i})\equiv{\mst@W}\widehat{{\mst@T}}{\mst@P}(\mst@Delta,{}\_{\mst@i},{}^{\*}\_{\mst@i},{}\_{\mst@i},\bm{\upmu}\_{\mst@i})\;, |  | (5) |

which leaves only the unknown parameters 𝛍i\mst@varfam@dot\bm{\upmu}\_{\mst@i} to be estimated. This approach makes use of the fact that productivity (i) and optimal allocations in the purchase scenario (~i∗\mst@varfam@dot\tilde{{\mst@X}}^{\*}\_{\mst@i}) are implicit functions of observables and unknown parameters.161616Specifically, Assumptions 3 and 4 generally guarantees that i is a direct function of i, which, by Eq. ([C13](https://arxiv.org/html/2510.24916v1#A3.E13 "In Estimation Outline ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")) in the Appendix, depends on 𝛍\mst@varfam@dot\bm{\upmu}.
At this point we have a theoretical prediction of a producer’s i for units of the input as well as the empirical value solicited in the experiment, call this iobs\mst@varfam@dot{\mst@W}{\mst@T}{}^{\text{obs}}\_{\mst@i}.

For estimation, we leverage the parameterization of 𝛍i\mst@varfam@dot\bm{\upmu}\_{\mst@i}, which includes some common parameters 𝛍\mst@varfam@dot\bm{\upmu} and may depend on producers’ observable characteristics i. The GMM estimator for 𝛍\mst@varfam@dot\bm{\upmu} solves the minimization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝛍\slimits@i=1(widehat(,,i,i∗,i𝛍)−)iobs2,\mst@varfam@dot\min\_{\bm{\upmu}}\tsum\slimits@\_{{\mst@i}=1}\Bigl({\mst@W}\widehat{{\mst@T}}{\mst@P}(\mst@Delta,{}\_{\mst@i},{}^{\*}\_{\mst@i},{}\_{\mst@i},\bm{\upmu})-{\mst@W}{\mst@T}{}^{\text{obs}}\_{\mst@i}\Bigr)^{2}\;, |  | (6) |

which identifies 𝛍\mst@varfam@dot\bm{\upmu} given standard GMM identification conditions being met.

Particularly relevant for identification is the rank condition, which requires that the matrix of derivatives of the stacked moment conditions with respect to the vector of parameters has full rank. This condition fails, for example, if the WTP does not directly depend on a specific parameter, or if a parameter is redundant. It can be shown that Assumption 3 (Convex Input Costs) is a sufficient condition for the rank condition being met.

### Examples

In Appendix [A](https://arxiv.org/html/2510.24916v1#A1 "Appendix A Example Applications of Methodology ‣ Productivity Beliefs and Efficiency in Science"), we walk through four additional example settings of different forms of production and cost functions to show the usefulness and limitations of our approach. We provide a variety of examples where the methodology is applicable as well as an example where identification is not achieved. For illustrative purposes, we focus on settings with an analytical characterization, but of course the method extends to cases where the solution is numerical, as in our application to researchers below.

## Survey and Data Overview

### Survey Design

We use the National Survey of Academic Researchers (Myers et al. [2023](https://arxiv.org/html/2510.24916v1#bib.bib43)) and provide a brief overview of the survey methodology here. The population target is U.S. professors who conduct research at major institutions of higher education. To construct the sampling frame, information on professors was collected from the 158 largest institutions in the US by total R&D funding using the National Science Foundation’s 2019 Higher Education R&D survey (HERD; National Science Foundation [2023](https://arxiv.org/html/2510.24916v1#bib.bib44)).

The population consisted of 264,036 unique e-mails. A total of 131,672 individuals were e-mailed and 4,388 (3.33%) completed the survey.171717The IRB approval permitted e-mailing only 50% of the population. The response rate is more than twice what has been obtained from sourcing academic researcher contacts from the corresponding author data contained within the publication record (e.g., myers2020unequal). We then restrict the sample to the 4,003 individuals (91.2% of respondents) who reported being a professor, spending a non-zero amount of time on research, and having a non-zero salary from their primary institution.

During recruitment, incentives and reminders were randomly assigned. The four incentive arms were: (i\mst@varfam@dot{\mst@i}) no incentive, (i​i\mst@varfam@dot{\mst@i}{\mst@i}) entry into a lottery to win a gift card, (i​i​i\mst@varfam@dot{\mst@i}{\mst@i}{\mst@i}) the ability to vote for a set of charities to receive a donation, and (i​v\mst@varfam@dot{\mst@i}{\mst@v}) both the second and third incentives. The reminder arms were zero, one, or two follow-up emails. Each email was randomly assigned to one incentive arm and one reminder arm with equal probability, resulting in twelve possible combinations.

The randomized incentives and reminders provide us with instruments that we can use to implement a sample selection correction (i.e., Heckman [1979](https://arxiv.org/html/2510.24916v1#bib.bib27)). The validity of this approach relies on having variables that cause entry into the sample (i.e., completing the survey) but do not affect the outcomes of interest. This allows us to adjust for unobservable differences between the population and our sample. Appendix Table [B1](https://arxiv.org/html/2510.24916v1#A2.T1 "table B1 ‣ Appendix B Additional Survey Statistics and Comparisons ‣ Productivity Beliefs and Efficiency in Science") reports the results from a regression of an indicator for survey completion on the different incentive and reminder arms, showing that all arms had a statistically significant positive effect on researchers’ propensity to complete the survey.

In addition to adjusting for unobservable differences, Myers et al. ([2023](https://arxiv.org/html/2510.24916v1#bib.bib43)) also checks the representativeness of the respondent sample by comparing it to the invited sample on observable characteristics. First, the authors explore a series of observable characteristics at the researcher level by comparing the grant and publication histories of respondents and non-respondents using the Dimensions database (Digital Science [2018](https://arxiv.org/html/2510.24916v1#bib.bib19)), which collects and disambiguates scientific metrics for researchers worldwide.181818Using a fuzzy name matching process, Myers et al. ([2023](https://arxiv.org/html/2510.24916v1#bib.bib43)) are able to confidently match 87,000 (66%)
of the researchers to their records in Dimensions. Appendix Figure [B1](https://arxiv.org/html/2510.24916v1#A2.F1 "figure B1 ‣ Appendix B Additional Survey Statistics and Comparisons ‣ Productivity Beliefs and Efficiency in Science") (replicated from Myers et al. ([2023](https://arxiv.org/html/2510.24916v1#bib.bib43))) shows invite-respondent overlap on various measures of scientific inputs and outputs. Overall, there is little difference between the respondents and non-respondents both economically and statistically speaking.

Looking at the institutional level, Appendix Figure [B2](https://arxiv.org/html/2510.24916v1#A2.F2 "figure B2 ‣ Appendix B Additional Survey Statistics and Comparisons ‣ Productivity Beliefs and Efficiency in Science") (replicated from Myers et al. ([2023](https://arxiv.org/html/2510.24916v1#bib.bib43))) shows invite-respondent overlap on various measures of institution funding derived from the HERD survey. As in the case of the researcher-level comparison, the distributions overlap substantially. In this case, there are some statistically significant differences; on average, respondents come from institutions with slightly less research funding (4–6%).

### Summary Statistics: Researchers and their Inputs

Table [1](https://arxiv.org/html/2510.24916v1#S3.T1 "table 1 ‣ Fields of Study ‣ Summary Statistics: Researchers and their Inputs ‣ Survey and Data Overview ‣ Productivity Beliefs and Efficiency in Science") reports the summary statistics of the key covariates in our analyses. See Myers et al. ([2023](https://arxiv.org/html/2510.24916v1#bib.bib43)) for a more detailed investigation of these summary statistics.

#### Fields of Study

Using the name of the professor’s department, we assign them to a narrow set of twenty “minor” fields of study and aggregate those fields into five broader “major” fields: Humanities and related; Engineering, Math, and related; Medicine and Health Sciences; Natural Sciences; and Social Sciences. Unless otherwise noted, our counterfactual analyses constrain the reallocation of inputs to only occur *within* the major fields.

table 1: Summary Statistics—Salary, Funding, Time, and Fields

|  |  |  |  |
| --- | --- | --- | --- |
|  | *mean* | *s.d.* | p\mst@varfam@dot{\mskip 2.0mu\mst@p\mskip 0.0mu}50 |
| *Salary and research funds, $/year* |  |  |  |
| Total salary | 159,028.23 | 74,516.13 | 140,000.00 |
| Guaranteed & existing funding | 52,223.08 | 83,420.47 | 5,000.00 |
| Fundraising expectations | 93,909.19 | 144,013.69 | 20,000.00 |
| *Work time, hrs./week* |  |  |  |
| Total work | 48.55 | 10.00 | 48.00 |
| Research | 18.51 | 9.60 | 17.40 |
| Fundraising | 4.47 | 5.09 | 2.65 |
| Administration | 7.48 | 6.17 | 5.80 |
| Teaching and other work | 18.09 | 9.78 | 17.20 |
| *Major field*, {0,1} |  |  |  |
| Engineering, math, & related | 0.17 | 0.37 |  |
| Humanities & related | 0.19 | 0.39 |  |
| Medical & health sciences | 0.28 | 0.45 |  |
| Natural sciences | 0.16 | 0.37 |  |
| Social sciences | 0.21 | 0.40 |  |

*Note*: Reports summary statistics for 4,003 researcher-level observations. Unless otherwise noted, all variables are continuous and bound below by zero. *{0,1}* indicates binary variables.

#### Salaries and Research Inputs

The survey solicits a range of details regarding researchers’ salary, their guaranteed funding (e.g., from prior grants or institutional guarantees), expected funds they will raise over the coming five years, and their time allocations. Importantly, most variables are elicited as expectations over the coming five years to ensure the responses span the same time horizon as the thought experiments described below. In the Appendix, we replicate a test of respondents’ self-reporting by comparing their self-reported salaries to the publicly-reported salaries we are able to locate for a subset of researchers. Overall, there is a high degree of alignment (see Appendix Figure [B3](https://arxiv.org/html/2510.24916v1#A2.F3 "figure B3 ‣ Appendix B Additional Survey Statistics and Comparisons ‣ Productivity Beliefs and Efficiency in Science")).

#### Position and Socio-demographics

Appendix Table [B2](https://arxiv.org/html/2510.24916v1#A2.T2 "table B2 ‣ Appendix B Additional Survey Statistics and Comparisons ‣ Productivity Beliefs and Efficiency in Science")provides a full summary of all other major features collected regarding researchers’ positions (e.g., rank and tenure status) and their socio-demographics (e.g., gender, race/ethnicity, citizenship).

table 2: Summary Statistics—Subjective Output

|  |  |  |
| --- | --- | --- |
|  | *mean* | *s.d.* |
| *Intended research outputs*, {0,1,2} |  |  |
| Journal articles | 1.87 | 0.37 |
| Books | 0.52 | 0.68 |
| Materials or methods | 0.70 | 0.68 |
| Products | 0.47 | 0.64 |
| *Intended research audience*, {0,1,2} |  |  |
| Academic peers | 1.88 | 0.36 |
| Policymakers | 0.84 | 0.69 |
| Businesses | 0.54 | 0.62 |
| General public | 0.83 | 0.62 |
| *Riskiness of own research*, [0,10] |  |  |
| Own belief | 4.63 | 2.34 |
| Belief of peers’ beliefs | 4.57 | 2.37 |
| *Theoretical vs. empirical*, [0,10] |  |  |
| Ask [0] or answer [10] questions | 4.89 | 2.54 |

*Note*: Reports summary statistics for 4,003 researcher-level observations. The intended research outputs and audience variables are coded responses to questions of the form *How often are the following the intended output / audience of your research*, where responses are coded as follows: *Rarely*=0, *Sometimes*=1, *Very often*=2. The question about risk used a scale where 0 indicated no risk and 10 indicated very high risk. The question about theory versus empirics used a scale where 0 indicated that the researcher focused on asking new questions and 10 indicated that the researcher focsed on answering existing questions.

### Summary Statistics: Subjective Output Measures

Our methodology for estimating productivity is explicitly designed to avoid the need to quantify the output produced by researchers’ efforts. Still, it is useful to have a more qualitative understanding of what researchers are producing. Fortunately, the survey includes a number of subjective questions regarding researchers’ output. Table [2](https://arxiv.org/html/2510.24916v1#S3.T2 "table 2 ‣ Position and Socio-demographics ‣ Summary Statistics: Researchers and their Inputs ‣ Survey and Data Overview ‣ Productivity Beliefs and Efficiency in Science") summarizes answers to these questions, which asked the frequency with which researchers intended to produce outputs of certain types (e.g., articles, books, materials, products) for certain types of audiences (e.g., peers, policymakers, businesses, general public) as well as other measures of riskiness and the degree to which the researcher focused on asking new questions or answering existing questions.

The traditional proxy for scientific output is peer-reviewed journal articles, and the data indicate that this is the most common output type that researchers intend to produce. However, there is a considerable amount of variation and a significant amount of attention focused on producing output of types and for audiences that may never be codified in a journal article. More importantly, these measures are often negatively correlated in a way that suggests strategic substitution (see Appendix Table [B3](https://arxiv.org/html/2510.24916v1#A2.T3 "table B3 ‣ Appendix B Additional Survey Statistics and Comparisons ‣ Productivity Beliefs and Efficiency in Science")). For instance, researchers who focus more on publishing articles for their academic peers are less likely to focus on publishing books or developing products intended for non-academic audiences. This highlights the limitation of observable output proxies.

## Model of Science

In this section, we model researchers’ labor supply, which describes their utility from production and consumption. First, we present the environment and researchers’ optimal decisions (Subsection [4.1](https://arxiv.org/html/2510.24916v1#S4.SS1 "Researchers’ Labor Supply ‣ Model of Science ‣ Productivity Beliefs and Efficiency in Science")). Then we incorporate externalities in production to define social welfare (Subsection [4.2](https://arxiv.org/html/2510.24916v1#S4.SS2 "Social Value ‣ Model of Science ‣ Productivity Beliefs and Efficiency in Science")) and highlight the connection between the model and the survey thought experiments that solicit researchers’ willingness to pay (WTP) for different factors (Subsection [4.3](https://arxiv.org/html/2510.24916v1#S4.SS3 "WTP and Productivity ‣ Model of Science ‣ Productivity Beliefs and Efficiency in Science")). Additional details regarding the model and estimation are contained in Appendix [C](https://arxiv.org/html/2510.24916v1#A3 "Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science").

### Researchers’ Labor Supply

There are researchers indexed by i\mst@varfam@dot{\mst@i} who each choose how much total time to work (i) and how to allocate their time between research i and fundraising i over a fixed horizon. Their choices maximize their utility conditional on a contract from their primary institution, which is a triplet of state variables Si=(,i,i)i\mst@varfam@dot\text{{S}}\_{\mst@i}=({}\_{\mst@i},{}\_{\mst@i},{}\_{\mst@i}): salary i ($), guaranteed funding i ($), and administrative and teaching duties i (hours).191919We use the term “*contract*” loosely, since, for example, a researcher’s guaranteed funding may come in part from future flows of funding from grants obtained outside the institution. In the context of the methodological framework presented in Section [2](https://arxiv.org/html/2510.24916v1#S2 "Methodological Framework ‣ Productivity Beliefs and Efficiency in Science"), the function u1​i​()+u2​i​()\mst@varfam@dot{\mst@u}\_{1{\mst@i}}(\cdot)+{\mst@u}\_{2{\mst@i}}(\cdot) serves the role of the “benefit” function, while labor disutility u3​i​()\mst@varfam@dot{\mst@u}\_{3{\mst@i}}(\cdot) represents the cost function, which is parameterized to be convex. Researchers’ indirect utility is given by:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | (Si,𝛉i,𝛍i)=max,i,ii\mst@varfam@dot\displaystyle\mathcal{{\mst@V}}(\text{{S}}\_{\mst@i}\,,\,\bm{\uptheta}\_{\mst@i}\,,\,\bm{\upmu}\_{\mst@i})=\max\_{{}\_{\mst@i}\,,\,{}\_{\mst@i}\,,\,{}\_{\mst@i}} | u1​i()i+u2​i()i−u3​i(,i,i)i\mst@varfam@dot\displaystyle\;{\mst@u}\_{1{\mst@i}}({}\_{\mst@i})+{\mst@u}\_{2{\mst@i}}({}\_{\mst@i})-{\mst@u}\_{3{\mst@i}}({}\_{\mst@i}\,,\,{}\_{\mst@i}\,,\,{}\_{\mst@i}) |  | (7a) |
|  |  | subject to |  |
|  |  | =i+min+iii\mst@varfam@dot\displaystyle{}\_{\mst@i}={}\_{\text{min}}+{}\_{\mst@i}+{}\_{\mst@i}{}\_{\mst@i} |  | (7b) |
|  |  | +i+i=ii\mst@varfam@dot\displaystyle{}\_{\mst@i}+{}\_{\mst@i}+{}\_{\mst@i}={}\_{\mst@i} |  | (7c) |
|  |  | =i,iiii1−i\mst@varfam@dot\displaystyle{}\_{\mst@i}={}\_{\mst@i}{}\_{\mst@i}^{{}\_{\mst@i}}{}\_{\mst@i}^{1-{}\_{\mst@i}}\;, |  | (7d) |

where 𝛉i=(,i,i)i\mst@varfam@dot\bm{\uptheta}\_{\mst@i}=({}\_{\mst@i}\,,\,{}\_{\mst@i}\,,\,{}\_{\mst@i}) is the vector of individual-specific attributes related to scientific activity and 𝛍i\mst@varfam@dot\bm{\upmu}\_{\mst@i} is a vector of parameters that govern the shape of the u\mst@varfam@dot{\mst@u} functions.

The quantity of knowledge i that researchers produce is a Cobb-Douglas function of total funding i and research time i, which includes researcher-specific productivities (i) and output elasticities (per i). Additionally, we assume a minimum funding amount min\mst@varfam@dot{}\_{\text{min}}, and that all work hours are non-negative and have an upper bound max\mst@varfam@dot{}\_{\text{max}}.

Utility from salary, output, and effort are given by the following functional forms:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | u1​i​()\mst@varfam@dot\displaystyle{\mst@u}\_{1{\mst@i}}(\cdot) | =()i1−i1−i\mst@varfam@dot\displaystyle=\mst@omega\frac{({}\_{\mst@i})^{1-{}\_{\mst@i}}}{1-{}\_{\mst@i}} |  | (8a) |
|  | u2​i​()\mst@varfam@dot\displaystyle{\mst@u}\_{2{\mst@i}}(\cdot) | =()i1−i1−i\mst@varfam@dot\displaystyle=\frac{({}\_{\mst@i})^{1-{}\_{\mst@i}}}{1-{}\_{\mst@i}} |  | (8b) |
|  | u3​i​()\mst@varfam@dot\displaystyle{\mst@u}\_{3{\mst@i}}(\cdot) | =(+i+i)ii1+i1+i​.\mst@varfam@dot\displaystyle=\mst@psi\frac{({}\_{\mst@i}+{}\_{\mst@i}+{}\_{\mst@i}^{{}\_{\mst@i}})^{1+{}\_{\mst@i}}}{1+{}\_{\mst@i}}\;. |  | (8c) |

The vector 𝛍i\mst@varfam@dot\bm{\upmu}\_{\mst@i} collects the parameters (,,i,i,,i)i\mst@varfam@dot(\mst@omega,{}\_{\mst@i},{}\_{\mst@i},\mst@psi,{}\_{\mst@i},{}\_{\mst@i}).202020The i parameter allows for additional disutility from duty-related work (e.g., administration or teaching), which improves the model’s fit to the data. We also assume the following: (0,1)i\mst@varfam@dot{}\_{\mst@i}\in(0,1), >0\mst@varfam@dot\mst@psi>0, >i0\mst@varfam@dot{}\_{\mst@i}>0, and >i0\mst@varfam@dot{}\_{\mst@i}>0.

The policy functions (Si,𝛉i,𝛍i)\mst@varfam@dot\mathcal{{\mst@R}}(\text{{S}}\_{\mst@i},\bm{\uptheta}\_{\mst@i},\bm{\upmu}\_{\mst@i}), ()\mst@varfam@dot\mathcal{{\mst@F}}(\cdot), and ()\mst@varfam@dot\mathcal{{\mst@H}}(\cdot) characterize the solutions to Equation ([7](https://arxiv.org/html/2510.24916v1#S4.E7 "In Researchers’ Labor Supply ‣ Model of Science ‣ Productivity Beliefs and Efficiency in Science")). For each individual researcher, these policies determine optimal (,i∗,i∗)i∗\mst@varfam@dot({}^{\*}\_{\mst@i},{}^{\*}\_{\mst@i},{}^{\*}\_{\mst@i}) as a function of states, attributes, and parameters. The derivations of these policy functions are described in Appendix [C.1](https://arxiv.org/html/2510.24916v1#A3.SS1 "Derivation of Policy Functions ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science").

Ideally, we would have enough variation to estimate all researcher-specific attributes including the production-related parameters (,i,ii\mst@varfam@dot{}\_{\mst@i},{}\_{\mst@i},{}\_{\mst@i}) as well as all of the consumption-related parameters that govern researchers’ utility from salary, output, and effort (,i,i,ii\mst@varfam@dot{}\_{\mst@i},{}\_{\mst@i},{}\_{\mst@i},{}\_{\mst@i}). However, as shown below, we only have enough structural conditions to uniquely identify the production-related parameters (,i,ii\mst@varfam@dot{}\_{\mst@i},{}\_{\mst@i},{}\_{\mst@i}). Thus, we choose to specify each of the consumption-related parameters as parametric function of researchers’ observable features, whose common parameters we then estimate by GMM consistent with the framework of Section [2](https://arxiv.org/html/2510.24916v1#S2 "Methodological Framework ‣ Productivity Beliefs and Efficiency in Science").

Fortunately, we have a large vector of observable features (i\mst@varfam@dot\mathbf{{\mst@X}}\_{\mst@i}) that describe researchers’ positions, their backgrounds, and their subjective descriptions of their scientific output (i.e., the features summarized in Table [2](https://arxiv.org/html/2510.24916v1#S3.T2 "table 2 ‣ Position and Socio-demographics ‣ Summary Statistics: Researchers and their Inputs ‣ Survey and Data Overview ‣ Productivity Beliefs and Efficiency in Science") and Appendix Tables [B2](https://arxiv.org/html/2510.24916v1#A2.T2 "table B2 ‣ Appendix B Additional Survey Statistics and Comparisons ‣ Productivity Beliefs and Efficiency in Science")). This is useful because it allows us to incorporate more heterogeneity into the consumption components of the model and limit the degree to which variation in the data might otherwise cause us to overstate the heterogeneity in the production parameters.

Unfortunately, the computational demands of estimating the model limit the flexibility with which we can incorporate the dozens of features available. Thus, to balance the benefits of allowing for heterogeneity in consumption with the benefits of simpler estimation, we use k\mst@varfam@dot{\mst@k}-means clustering to reduce the full set of observable features (i\mst@varfam@dot\mathbf{{\mst@X}}\_{\mst@i}) into a one-dimensional index. We assume there are two clusters of researcher types (k=2\mst@varfam@dot{\mst@k}=2) and estimate each researcher’s distance from these clusters with their Euclidean similarity score. This distance provides a one-dimensional description of all of the different ways researchers responded to questions that could plausibly be driven by heterogeneous preferences.

We refer to this resulting index as describing researchers’ type, i. Appendix [C.2](https://arxiv.org/html/2510.24916v1#A3.SS2 "Reducing Dimensions of Heterogeneity: 𝑘-means Clustering Results ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science") reports the results of the k\mst@varfam@dot{\mst@k}-means estimation showing the distribution of researcher type in the sample as well as a view of the mean differences in the features of researchers per their type.

We then specify each of the consumption-related parameters (,i,i,ii\mst@varfam@dot{}\_{\mst@i},{}\_{\mst@i},{}\_{\mst@i},{}\_{\mst@i}) to be simple, univariate functions of a researcher’s type. For instance, the parameter that governs the utility from private consumption is parameterized as: =iexp(+,0)i,1\mst@varfam@dot{}\_{\mst@i}=\exp({}\_{\mst@sigma,0}+{}\_{\mst@i}{}\_{\mst@sigma,1}). We similarly parameterize i and i with exponential functions with intercept and slope, respectively. The curvature of utility in scientific output, i, is modeled with a logistic function bounded in the interval (0,1)\mst@varfam@dot(0,1). Therefore, we express individual-specific parameters 𝛍i(,i𝛍)\mst@varfam@dot\bm{\upmu}\_{\mst@i}({}\_{\mst@i},\bm{\upmu}) as a function of a researcher’s type i and of the vector of common parameters to be estimated, denoted by 𝛍=(,,𝛅)\mst@varfam@dot\bm{\upmu}=(\mst@omega,\mst@psi,\bm{\updelta}), where 𝛅\mst@varfam@dot\bm{\updelta} includes the deep parameters that govern the utility functions.

Allowing the 𝛍i\mst@varfam@dot\bm{\upmu}\_{\mst@i} parameters to be type-specific is not a panacea, but it helps reduce the degree to which variation in the experimental data that is truly driven by heterogeneous preferences or heterogeneous demand for scientific output contaminates our productivity estimates. We further detail the estimation process below.

### Social Value

To incorporate the externalities of knowledge production, which we assume to be net positive, we define the social value produced by each researcher as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Si,𝛉i,𝛍i,)=u1​i()i+u2​i()i∗−u3​i(,i∗,i∗)i,\mst@varfam@dot\mathcal{{\mst@W}}(\text{{S}}\_{\mst@i}\,,\,\bm{\uptheta}\_{\mst@i}\,,\,\bm{\upmu}\_{\mst@i}\,,\,\mst@kappa)=\;{\mst@u}\_{1{\mst@i}}({}\_{\mst@i})+\mst@kappa{\mst@u}\_{2{\mst@i}}({}^{\*}\_{\mst@i})-{\mst@u}\_{3{\mst@i}}({}^{\*}\_{\mst@i}\,,\,{}^{\*}\_{\mst@i}\,,\,{}\_{\mst@i})\;, |  | (9) |

where researchers’ privately optimal choices and output are given by i∗\mst@varfam@dot{}^{\*}\_{\mst@i}, i∗\mst@varfam@dot{}^{\*}\_{\mst@i} and i∗\mst@varfam@dot{}^{\*}\_{\mst@i}. reflects the size of the externalities associated with researchers’ output. Thus, 1/ gives the share of the social value generated by each researcher’s output that they themselves capture and 1−1⇑\mst@varfam@dot 1-1/\mst@kappa is the size of the positive externality.

This formulation of externalities is an ad hoc way of implicitly modeling consumer surplus as some constant multiple of producer surplus. However, it has a clear economic interpretation as a measure of appropriation, and we can draw on prior studies that have sought to identify precisely this measure. Studies that focus on commercial innovators have found producers’ value capture to be as large as 15% (=6.7\mst@varfam@dot\mst@kappa=6.7) and as low as 2% (=50\mst@varfam@dot\mst@kappa=50) (Nordhaus [2004](https://arxiv.org/html/2510.24916v1#bib.bib45); Jena and Philipson [2008](https://arxiv.org/html/2510.24916v1#bib.bib32); Lakdawalla et al. [2010](https://arxiv.org/html/2510.24916v1#bib.bib37)). In our empirical analyses, our baseline assumption is =10\mst@varfam@dot\mst@kappa=10, which implies researchers capture 10% of the social value they create.212121Note also that this approach implies that researchers’ private utility reflects the case where =1\mst@varfam@dot\mst@kappa=1. Interestingly, as we will show below, the median researcher is willing to pay approximately $0.10 dollars to purchase $1 of research funding, which is a magnitude that is consistent with our assumption that =10\mst@varfam@dot\mst@kappa=10.

### WTP and Productivity

As described in Section [2](https://arxiv.org/html/2510.24916v1#S2 "Methodological Framework ‣ Productivity Beliefs and Efficiency in Science"), if we can solicit researchers’ WTP for some fixed quantity of their inputs, we can estimate their productivity beliefs. Here we outline our specific application of the methodology.

Consider the period prior to production but after which researchers have formed their expectations about their time allocations and, therefore, their expectations about their utility over the 5-year horizon. Now, researchers are offered some alternative contracts by their primary institution that vary either funding guarantees (widetilde\mst@varfam@dot{\mst@G}\rightarrow\widetilde{{\mst@G}}) or administrative duties (widetilde\mst@varfam@dot{\mst@D}\rightarrow\widetilde{{\mst@D}}), but leave the salary unspecified.

For each offer indexed by j\mst@varfam@dot{\mskip 2.0mu\mst@j\mskip 0.0mu} and characterized by (widetildei​j,widetildei​j\mst@varfam@dot\widetilde{{\mst@G}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}}\,,\,\widetilde{{\mst@D}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}}), there is a salary (widetildei​j=−i​ji​j\mst@varfam@dot\widetilde{{\mst@M}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}}={}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}}-{\mst@W}{\mst@T}{}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}}) that makes the researcher indifferent between their actual contract (,i,ii\mst@varfam@dot{}\_{\mst@i}\,,\,{}\_{\mst@i}\,,\,{}\_{\mst@i}) and the offer such that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (,i,i,i𝛉i,𝛍,…)=(widetildei​j,widetildei​j,widetildei​j,𝛉i,𝛍,…).\mst@varfam@dot\mathcal{{\mst@V}}({}\_{\mst@i}\,,\,{}\_{\mst@i}\,,\,{}\_{\mst@i}\,,\,\bm{\uptheta}\_{\mst@i}\,,\,\bm{\upmu}\,,\,...)=\mathcal{{\mst@V}}(\widetilde{{\mst@M}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}}\,,\,\widetilde{{\mst@G}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}}\,,\,\widetilde{{\mst@D}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}}\,,\,\bm{\uptheta}\_{\mst@i}\,,\,\bm{\upmu}\,,\,...)\;. |  | (10) |

For example, if a researcher is offered more guaranteed funding (<iwidetildei​j\mst@varfam@dot{}\_{\mst@i}<\widetilde{{\mst@G}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}}), then they will forecast how this additional funding will lead to changes in their optimal time allocations, their expected input levels, their expected output levels (per their productivity beliefs), and their expected indirect utility. The total increase in their expected indirect utility can be priced by the researcher and stated as a new, lower salary (>iwidetildei​j\mst@varfam@dot{}\_{\mst@i}>\widetilde{{\mst@M}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}}).

As shown in Section [2](https://arxiv.org/html/2510.24916v1#S2 "Methodological Framework ‣ Productivity Beliefs and Efficiency in Science"), we can write the alternative salary (widetildei​j\mst@varfam@dot\widetilde{{\mst@M}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}}) that makes researchers indifferent between their actual position and the offer as a function of known variables and the unknown parameters to be estimated:

|  |  |  |  |
| --- | --- | --- | --- |
|  | widetildei​j=(widetildei​j,widetildei​j,,i,i,i𝛉i,𝛍,…),\mst@varfam@dot\widetilde{{\mst@M}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}}=\mst@Pi(\widetilde{{\mst@G}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}}\,,\,\widetilde{{\mst@D}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}}\,,\,{}\_{\mst@i}\,,\,{}\_{\mst@i}\,,\,{}\_{\mst@i}\,,\,\bm{\uptheta}\_{\mst@i}\,,\,\bm{\upmu}\,,\,...)\;, |  | (11) |

where is determined by functional forms of, and optimality conditions implied by, Equation ([7](https://arxiv.org/html/2510.24916v1#S4.E7 "In Researchers’ Labor Supply ‣ Model of Science ‣ Productivity Beliefs and Efficiency in Science")). Thus, if we know the left-hand side of Equation ([11](https://arxiv.org/html/2510.24916v1#S4.E11 "In WTP and Productivity ‣ Model of Science ‣ Productivity Beliefs and Efficiency in Science")) from some experimental offers, and we also know all components of except for the parameters 𝛍\mst@varfam@dot\bm{\upmu}, then we can estimate those parameters. Appendix [C.3](https://arxiv.org/html/2510.24916v1#A3.SS3 "Estimation Outline ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science") contains the full details on our estimation routine.

## Survey Experiment

Here, we describe the thought experiments in the survey (Subsection [5.1](https://arxiv.org/html/2510.24916v1#S5.SS1 "Soliciting Willingness to Pay ‣ Survey Experiment ‣ Productivity Beliefs and Efficiency in Science")) and how they connect to the model (Subsection [5.2](https://arxiv.org/html/2510.24916v1#S5.SS2 "Connection to Model: WTP and Compensating Variation ‣ Survey Experiment ‣ Productivity Beliefs and Efficiency in Science")). We then report the distribution of responses and conduct tests for face validity, sample selection, and other potential concerns (Subsection [5.3](https://arxiv.org/html/2510.24916v1#S5.SS3 "Survey Experiment Results ‣ Survey Experiment ‣ Productivity Beliefs and Efficiency in Science")).

### Soliciting Willingness to Pay

#### WTP for Funding and Time

Respondents are presented with four hypothetical scenarios, each offering different trade-offs between salary and inputs. They are asked to imagine that their primary institution has offered them: (i\mst@varfam@dot{\mst@i}) an increase of $250,000 in guaranteed funding in exchange for a lower salary, (i​i\mst@varfam@dot{\mst@i}{\mst@i}) an increase of $1,000,000 in guaranteed funding in exchange for a lower salary, (i​i​i\mst@varfam@dot{\mst@i}{\mst@i}{\mst@i}) an elimination of all administrative duties in exchange for a lower salary, and (i​v\mst@varfam@dot{\mst@i}{\mst@v}) an increase in duties by 20 hours per month over a five-year period in exchange for a higher salary.222222Researchers who report no administrative duties are not shown scenario (i​i​i\mst@varfam@dot{\mst@i}{\mst@i}{\mst@i}). All of these hypotheticals are posed over a five-year span to fix the time horizon for all respondents. In order to solicit the salary at which they are indifferent between the current position and each offer, respondents are asked to report the lowest offered salary at which they would be willing to accept the offer.232323Pilot tests indicated that researchers could more easily report the lowest salary that could make them take the offer as opposed to the literal salary at indifference, and since indifference is a vanishingly small amount less than this reported value, we treat their answer as the amount at indifference. Importantly, the survey only solicits researchers’ WTP for more funding. This matters because counterfactual reallocations will involve reducing some researchers’ funding. In the case of time, the survey solicits both WTP (for more free time) and willingness to accept (WTA; for less free time) and we treat these as symmetric after being filtered through the model. Appendix Figure [C2](https://arxiv.org/html/2510.24916v1#A3.F2 "figure C2 ‣ Objectives and Constraints for Counterfactuals ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science") displays examples of how these thought experiments appeared to the survey respondents.

#### WTP for a Benchmark Good

When soliciting willingness to pay, especially in an un-incentivized manner, it is always possible that respondents under- or overstate their price sensitivity. In order to test for this, we follow Dizon-Ross and Jayachandran ([2022](https://arxiv.org/html/2510.24916v1#bib.bib20)) and explore respondents’ willingness to pay for a “benchmark good.” Dizon-Ross and Jayachandran ([2022](https://arxiv.org/html/2510.24916v1#bib.bib20)) note that, if one solicits a subject’s willingness to pay for a good whose value (to the subject) is plausibly uncorrelated with the value of the focal good, then any correlation between the two willingness-to-pay values can be attributed to systematic noise. The survey asks respondents
to report the maximum amount they would be willing to pay per month for high-speed internet access at their primary residence. We use this as our benchmark good since researchers scientific productivity should plausibly be uncorrelated with their demand for high-speed internet access at home. In Appendix Table [C1](https://arxiv.org/html/2510.24916v1#A3.T1 "table C1 ‣ Objectives and Constraints for Counterfactuals ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science"), we show that respondents’ stated WTP for scientific inputs are rarely correlated with their stated WTP for the benchmark good, which suggests a small amount of variation in researchers’ answers is attributable to systematic noise.

### Connection to Model: WTP and Compensating Variation

Four survey thought experiments elicit the compensating variation of individual researchers in relation to (i\mst@varfam@dot{\mst@i}) an increase of $250,000 in guaranteed funding i, (i​i\mst@varfam@dot{\mst@i}{\mst@i}) an increase of $1,000,000 in guaranteed funding i, (i​i​i\mst@varfam@dot{\mst@i}{\mst@i}{\mst@i}) a reduction of duties i to 0, and (i​v\mst@varfam@dot{\mst@i}{\mst@v}) an increase in duties by 20 hours per month over a 5-year period. In other words, we ask for income levels widehati​j\mst@varfam@dot\widehat{{\mst@M}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}}, where j={1,2,3,4}\mst@varfam@dot{\mskip 2.0mu\mst@j\mskip 0.0mu}=\{1,2,3,4\} indexes the four experiments, that would make the researcher’s utility in the counterfactual scenario equal to their indirect utility ∗i\mst@varfam@dot\mathcal{{\mst@V}}^{\*}\_{\mst@i} at current allocations. Formally, counterfactual guaranteed funding and duties in the four experiments are:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (widetildei​1,widetildei​1)=((+i$250,000),)i\displaystyle(\widetilde{{\mst@G}}\_{{\mst@i}1}\,,\widetilde{{\mst@D}}\_{{\mst@i}1})=\bigl(({}\_{\mst@i}+\text{\textdollar 250,000})\,,{}\_{\mst@i}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (widetildei​2,widetildei​2)=((+i$1,000,000),)i\displaystyle(\widetilde{{\mst@G}}\_{{\mst@i}2}\,,\widetilde{{\mst@D}}\_{{\mst@i}2})=\bigl(({}\_{\mst@i}+\text{\textdollar 1,000,000})\,,{}\_{\mst@i}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (widetildei​3,widetildei​3)=(,i0)\displaystyle(\widetilde{{\mst@G}}\_{{\mst@i}3}\,,\widetilde{{\mst@D}}\_{{\mst@i}3})=\bigl({}\_{\mst@i}\,,0\bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (widetildei​4,widetildei​4)=(,i(+i20 hours/month)),\displaystyle(\widetilde{{\mst@G}}\_{{\mst@i}4}\,,\widetilde{{\mst@D}}\_{{\mst@i}4})=\bigl({}\_{\mst@i}\,,({}\_{\mst@i}+0\text{ hours/month})\bigr)\;, |  |

where i and i represent actual states.

As noted above, the values of widehati​j\mst@varfam@dot\widehat{{\mst@M}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}} reported in these four experiments make the researcher indifferent between all possibilities (per Eq. [10](https://arxiv.org/html/2510.24916v1#S4.E10 "In WTP and Productivity ‣ Model of Science ‣ Productivity Beliefs and Efficiency in Science")), and therefore we can write these reported values to be a known function of observable data and the unknown parameters to be estimated (per Eq. [11](https://arxiv.org/html/2510.24916v1#S4.E11 "In WTP and Productivity ‣ Model of Science ‣ Productivity Beliefs and Efficiency in Science")).

### Survey Experiment Results

Figure [1](https://arxiv.org/html/2510.24916v1#S5.F1 "figure 1 ‣ Survey Experiment Results ‣ Survey Experiment ‣ Productivity Beliefs and Efficiency in Science") plots the distribution of WTP for guaranteed research funding and free time (in the form of WTP for less duties or WTA for more duties). The values shown are averaged over the two thought experiments for either factor and converted to a per-dollar basis. As evidenced by Figure [1](https://arxiv.org/html/2510.24916v1#S5.F1 "figure 1 ‣ Survey Experiment Results ‣ Survey Experiment ‣ Productivity Beliefs and Efficiency in Science"), there is considerable variation in WTP responses across researchers. Some of this variation reflects different preferences and constraints, but another portion reflects heterogeneous productivity across researchers. The model described above allows us to separate these two forces.

figure 1: Willingness to Pay Experiment Responses

![Refer to caption](x1.png)


A

![Refer to caption](x2.png)


B

*Note*: Shows the distribution of researchers’ stated WTP for $1 more of additional research funds (Panel A) and 1 hour less of administrative duties (Panel B). Approximately 1% of the upper tails have been trimmed for visibility.

Validating these WTP responses is a difficult but important task. They are the key ingredient of our entire exercise, but they may be driven in part by sample selection effects, behavioral biases, or noise. Although these are practical trade-offs that professors face throughout their careers, systematic data have not been collected in this way before to our knowledge. Thus, it is not clear what plausible variation would look like here. Still, we can conduct some tests motivated by economic and statistical theory to explore how reasonable these distributions of WTP are.

Motivated by the notion of opportunity costs, we test how WTP varies with researchers’ implied hourly wage (per their annual salary divided by their total hours of work). Assuming this implied wage rate is a proxy for researchers’ opportunity costs, it should be the case that researchers with higher hourly wages are willing to pay more for their free time. In Appendix Figure [3A](https://arxiv.org/html/2510.24916v1#A3.F3.sf1 "In figure C3 ‣ Objectives and Constraints for Counterfactuals ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science"), we see that this is indeed the case. Furthermore, it should be the case that, conditional on opportunity costs of time, researchers who expect to spend more time fundraising should have a higher WTP for guaranteed funding. In Appendix Figure [3B](https://arxiv.org/html/2510.24916v1#A3.F3.sf2 "In figure C3 ‣ Objectives and Constraints for Counterfactuals ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science"), we find this to be true.

As another test, Appendix Tables [C1](https://arxiv.org/html/2510.24916v1#A3.T1 "table C1 ‣ Objectives and Constraints for Counterfactuals ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science") and [C2](https://arxiv.org/html/2510.24916v1#A3.T2 "table C2 ‣ Objectives and Constraints for Counterfactuals ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science") describe analyses where we regress researchers’ WTP responses on the variables in the model as well as (i\mst@varfam@dot{\mst@i}) the large vector of observable features (i\mst@varfam@dot\mathbf{{\mst@X}}\_{\mst@i}), (i​i\mst@varfam@dot{\mst@i}{\mst@i}) an inverse Mills ratio constructed using the randomized survey participation incentives following Heckman ([1979](https://arxiv.org/html/2510.24916v1#bib.bib27)), and/or (i​i​i\mst@varfam@dot{\mst@i}{\mst@i}{\mst@i}) researchers’ WTP for the benchmark good (high-speed internet) following Dizon-Ross and Jayachandran ([2022](https://arxiv.org/html/2510.24916v1#bib.bib20)). We find the variables in the model can explain 82–96% of the variation in WTP responses (see Appendix Table [C1](https://arxiv.org/html/2510.24916v1#A3.T1 "table C1 ‣ Objectives and Constraints for Counterfactuals ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")). This supports the model’s ingredients as being key determinants of researchers’ answers. When we include the large vector of observable features in addition as additional explanatory features, the 2 statistics increase by only one to four percentage points. Residual variation in WTP responses (conditional on the variables of the model) are not well explained by these heterogeneous observables. This gives us confidence that we are not dramatically mis-specifying heterogeneity in the model.

We also find that the inverse Mills ratio is not a statistically significant predictor of responses (see Appendix Table [C2](https://arxiv.org/html/2510.24916v1#A3.T2 "table C2 ‣ Objectives and Constraints for Counterfactuals ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")). Under the assumptions outlined in Heckman ([1979](https://arxiv.org/html/2510.24916v1#bib.bib27)), this supports the notion that respondents did not differentially select into our sample as a function of their WTP for inputs and suggests some generalizability of our responses. Finally, we find that researchers’ WTP for the benchmark good (high-speed internet at their house) is correlated with their WTP for inputs (see Appendix Table [C2](https://arxiv.org/html/2510.24916v1#A3.T2 "table C2 ‣ Objectives and Constraints for Counterfactuals ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")). Under the assumption that researchers’ demand for home internet is truly uncorrelated with their productivity, this provides some evidence of systematic noise in how respondents are reporting their WTP in these experiments. However, the economic magnitude of this relationship is quite small. Furthermore, the benchmark good WTP is included in our vector of features we use to make the researcher type index (that determines heterogeneity in the consumption parameters), which allows us to control for this to some degree. Overall, despite not being incentivized experiments, researchers’ responses behave as expected and are of plausible magnitudes.

## Estimates for the Model of Science

### A View of Researchers’ Utility Functions

To illustrate our estimates of the utility function, Appendix Figure [D1](https://arxiv.org/html/2510.24916v1#A4.F1 "figure D1 ‣ Additional Tables and Figures ‣ Appendix D Additional Productivity and Efficiency Results ‣ Productivity Beliefs and Efficiency in Science") shows how an average researcher’s utility depends on the levels of the three state variables (salary, administrative duties, guaranteed research funding) and research output. The figure shows the percent change in a researcher’s utility as the variable is increased from the 10th percentile level to the 90th percentile level while all other variables and parameters are held fixed at the sample averages.

In terms of magnitude, salary and administrative duties are the most important for researchers’ utility. Shifting the average researcher’s salary from the 10th percentile to the 90th percentile increases their utility by roughly 60%. An equivalent relative increase in administrative duties reduces utility by about 20%. In contrast, similarly scaled increases in guaranteed funding or research output raise utility by only a few percentage points.242424As evidence of fit, the median absolute difference between a researcher’s stated WTP and the model’s prediction ranges from 6–12 percentage points across the four questions. The numerical estimates of the common parameters and more detailed descriptions of the model’s fit are available from the authors upon request.

### Productivity Distributions

Figure [2](https://arxiv.org/html/2510.24916v1#S6.F2 "figure 2 ‣ Productivity Distributions ‣ Estimates for the Model of Science ‣ Productivity Beliefs and Efficiency in Science") shows the unconditional distributions of the production function parameters i (funding intensity) and i (TFP). Figure [2A](https://arxiv.org/html/2510.24916v1#S6.F2.sf1 "In figure 2 ‣ Productivity Distributions ‣ Estimates for the Model of Science ‣ Productivity Beliefs and Efficiency in Science") displays the distribution of the i parameter, which describes the relative weight of funding versus research time in researchers’ production functions. The distribution highlights a significant degree of heterogeneity across researchers, with roughly 20% of our sample having a funding intensity either larger than 0.6 or smaller than 0.2.

figure 2: Production Function Parameters

![Refer to caption](x3.png)


A

![Refer to caption](x4.png)


B

*Note*: Shows the distribution of researcher-specific estimates of the production function parameters i (funding intensity; Panel A) and i (productivity; Panel B). In Panel (A, larger values indicate more funding intensity and (0,1⌋\mst@varfam@dot\mst@gamma\in[0,1]. In Panel (B), the top 5% of productivities have been trimmed for visibility and estimates are scaled into units where the mean is normalized to equal 1 (with the 10th and 90th percentiles of the distribution noted on the x\mst@varfam@dot{\mst@x} axis).

As both an interesting exercise and test of face validity, Appendix Figure [D2](https://arxiv.org/html/2510.24916v1#A4.F2 "figure D2 ‣ Additional Tables and Figures ‣ Appendix D Additional Productivity and Efficiency Results ‣ Productivity Beliefs and Efficiency in Science") plots the average funding intensity parameters (i) for the twenty minor fields represented in the sample. We find that i is highest in chemistry and engineering, where research is often capital intensive and involves the use of expensive lab equipment. In contrast, and in line with intuition, the social sciences (e.g., economics, political science) display the lowest funding intensity on average. Notably, Appendix Figure [D2](https://arxiv.org/html/2510.24916v1#A4.F2 "figure D2 ‣ Additional Tables and Figures ‣ Appendix D Additional Productivity and Efficiency Results ‣ Productivity Beliefs and Efficiency in Science") highlights the heterogeneity in funding intensity across researchers even within these narrower fields of study.

Figure [2B](https://arxiv.org/html/2510.24916v1#S6.F2.sf2 "In figure 2 ‣ Productivity Distributions ‣ Estimates for the Model of Science ‣ Productivity Beliefs and Efficiency in Science") displays the distribution of the i parameter, our measure of researchers’ TFP. Our estimates reveal a large skew in researchers’ beliefs about their productivity.

As one test of face validity, Appendix Table [D1](https://arxiv.org/html/2510.24916v1#A4.T1 "table D1 ‣ Additional Tables and Figures ‣ Appendix D Additional Productivity and Efficiency Results ‣ Productivity Beliefs and Efficiency in Science") reports regression results that test for associations between researchers’ productivity (i) and their performance per traditional metrics of scientific productivity, which are often simply output levels (e.g., publications, citations). Under some reasonable assumptions, we expect a positive association between these metrics, and we find it.252525Specifically, those assumptions are: (i\mst@varfam@dot{\mst@i}) there is a positive correlation between researchers’ input levels and productivity; (i​i\mst@varfam@dot{\mst@i}{\mst@i}) these traditional output metrics are positively correlated with researchers’ true output; (i​i​i\mst@varfam@dot{\mst@i}{\mst@i}{\mst@i}) researchers’ output levels are semi-persistent over time (since we can only work with pre-survey bibliographic data). Researchers with higher productivity beliefs are more likely to have more actual publication output whether that output is measured using recent publication counts or citation-weighted counts. This provides a signal that our estimates do in fact reflect real productivity differences across researchers.

To understand how variation in TFP affects output, we decompose the variance in log output into components attributable to TFP, input levels, and factor intensity. Note that the variance in log output due to the variance in log TFP is given by: Var(log()i)+2Cov(log()i,logi()i)+2Cov(log()i,(1−)ilog()i)\mst@varfam@dot\text{Var}(\log({}\_{\mst@i}))+2\text{Cov}(\log({}\_{\mst@i})\,,\,{}\_{\mst@i}\log({}\_{\mst@i}))+2\text{Cov}(\log({}\_{\mst@i})\,,\,(1-{}\_{\mst@i})\log({}\_{\mst@i})). Using this relationship, we estimate that 46
% of the variance in output across researchers is due to the variance in TFP. Without adjusting for the covariances between TFP and the input levels and funding-intensity parameter, we obtain an estimate of 80
%. This finding indicates that more productive researchers obtain more inputs that are well-suited to their production functions, and it motivates questions related to allocative efficiency that we return to in the next section.

While Figure [2B](https://arxiv.org/html/2510.24916v1#S6.F2.sf2 "In figure 2 ‣ Productivity Distributions ‣ Estimates for the Model of Science ‣ Productivity Beliefs and Efficiency in Science") shows a substantial degree of heterogeneity, some fraction of this variation may be due to differences in the demand for their output or the nature of science within their fields of study; for a similar reason, most studies on the industrial organization of firms report productivity distributions based only on within-industry variation. Thus, Figure [3](https://arxiv.org/html/2510.24916v1#S6.F3 "figure 3 ‣ Productivity Distributions ‣ Estimates for the Model of Science ‣ Productivity Beliefs and Efficiency in Science") shows the distribution of researcher productivity (i) after various controls for field-specific (or “industry-specific”) variation are introduced.

First, Figure [3](https://arxiv.org/html/2510.24916v1#S6.F3 "figure 3 ‣ Productivity Distributions ‣ Estimates for the Model of Science ‣ Productivity Beliefs and Efficiency in Science") shows the raw distribution of productivity levels, which mirrors the distribution shown in Figure [2B](https://arxiv.org/html/2510.24916v1#S6.F2.sf2 "In figure 2 ‣ Productivity Distributions ‣ Estimates for the Model of Science ‣ Productivity Beliefs and Efficiency in Science") but now on a logarithmic scale. Next, we regress researchers’ TFP estimates on a set of major-field fixed effects, and we report the distribution of residual productivity levels. Lastly, we also condition productivity on the full vector of covariates used to generate the researcher type index.

figure 3: TFP Distributions

![Refer to caption](x5.png)

*Note*: Shows the distribution of researchers’ TFP (i) where units have been rescaled so the mean equals 1; note the log scale. In addition to (*i*) the distribution of the raw values, productivities are also shown after removing residual variation due to (*ii*) major field fixed effects, and (*iii*) the covariates used to construct the researcher type index. 90-10 percentile ratios are also shown.

Figure [3](https://arxiv.org/html/2510.24916v1#S6.F3 "figure 3 ‣ Productivity Distributions ‣ Estimates for the Model of Science ‣ Productivity Beliefs and Efficiency in Science") also reports the ratio of the 90th and 10th percentiles, the “90–10 TFP ratio” measure of variance commonly reported in traditional, firm-level studies. The 90–10 TFP ratio of the raw productivity estimates is substantial, but, even after conditioning on the additional controls, we still find a large dispersion. The 90th percentile researcher believes they are roughly 30 times as productive as the 10th percentile researcher.

It is difficult to benchmark this dispersion. Firm-level estimates are primarily from manufacturing sectors, which typically involve 90–10 TFP ratios on the scale of 1.5 to 5 (Syverson [2011](https://arxiv.org/html/2510.24916v1#bib.bib54)). To date, most worker-level productivity estimates tend to be similarly dispersed (Hoffman and Stanton [2024](https://arxiv.org/html/2510.24916v1#bib.bib30)); however, those estimates do not come from occupations as complex and creatively oriented as science. One notable example is Sackman, Erikson, and Grant ([1968](https://arxiv.org/html/2510.24916v1#bib.bib50)) who used direct observation to estimate software engineers’ productivity and found that some individuals were as much as an order of magnitude faster on coding tasks than others. Interestingly, this is the same approximate scale that we identify with our sample of researchers.262626For more evidence of face validity, we note that the 90-10 ratio for field-normalized citations in our sample is 56, which is very similar to the degree of productivity dispersion we estimate.

Motivated by the prevalence of power laws in the tails of distributions (Gabaix [2009](https://arxiv.org/html/2510.24916v1#bib.bib21)), we examine the distribution of TFP among the most productive researchers. Appendix Figure [D3](https://arxiv.org/html/2510.24916v1#A4.F3 "figure D3 ‣ Additional Tables and Figures ‣ Appendix D Additional Productivity and Efficiency Results ‣ Productivity Beliefs and Efficiency in Science") shows the traditional log rank versus log value plots along with the regression results following the approach described by Gabaix ([2009](https://arxiv.org/html/2510.24916v1#bib.bib21)). We find clear evidence of power laws when focusing on the top 20% or top 1% of researchers per their TFP. The regressions yield power law exponents of approximately 2–3, which are significantly larger than Zipf’s law (exponent of 1) but are on the same scale as the power law exponents observed in income distributions and stock prices (Gabaix [2009](https://arxiv.org/html/2510.24916v1#bib.bib21)). Future work that estimates high-skilled workers’ productivity (and not simply their output) in other settings would be worthwhile.

## Counterfactuals and Allocative Efficiency

### Overview

In this section, we use our productivity estimates to analyze allocative efficiency through the lens of our model. Specifically, we treat guaranteed funding () and duties () as policy levers a planner can adjust to maximize a given objective. Importantly, we search for the allocations of guaranteed funding and duties that maximize an objective after accounting for researchers’ endogenous behavioral responses to the planner’s decisions. The margins for behavioral responses are total hours worked, time spent fundraising (to obtain additional funds), and time spent on research (to directly produce output). In reality, researchers may endogenously adjust along many other margins (e.g., the types of projects they pursue), but these complexities are beyond the scope of our model. Still, adjustments to time allocations are likely a first-order response, and ignoring other margins allows us to keep the problem tractable.

Within the literature on misallocation, tests of efficiency are performed using either: (i\mst@varfam@dot{\mst@i}) *relative* benchmarks, where allocative efficiency across multiple markets is equated, which reveals how much of the gap in aggregate output between markets is due to allocative frictions (e.g., Hsieh and Klenow [2009](https://arxiv.org/html/2510.24916v1#bib.bib31)); and (i​i\mst@varfam@dot{\mst@i}{\mst@i}) *absolute* benchmarks, which compare the actual output level to that which a social planner could achieve (e.g., Petrin and Sivadasan [2013](https://arxiv.org/html/2510.24916v1#bib.bib47); Asker, Collard-Wexler, and De Loecker [2019](https://arxiv.org/html/2510.24916v1#bib.bib6)). Our approach allows us to perform both of these types of tests.272727However, we do not explicitly model the sources of inefficiencies that give rise to wedges between actual an optimal input allocations. But, in Sections [7.3](https://arxiv.org/html/2510.24916v1#S7.SS3 "Input Wedges: Actual Versus Optimal ‣ Counterfactuals and Allocative Efficiency ‣ Productivity Beliefs and Efficiency in Science") and [7.4](https://arxiv.org/html/2510.24916v1#S7.SS4 "Case Studies of Potential Frictions ‣ Counterfactuals and Allocative Efficiency ‣ Productivity Beliefs and Efficiency in Science") we identify and investigate features of producers that are correlated with the size of their input wedge.

We consider two alternative objectives. First, we estimate the allocation that maximizes total output. Second, we optimize for a utilitarian objective of maximizing researchers’ aggregate utility. To aid interpretation, we conduct an exercise where we estimate how much total research funding must be increased *using actual allocations* to achieve the same growth in scientific output that we are able to achieve *using actual funding levels* in alternative allocations. Beyond this, we explore a range of alternative constraints on how inputs are reallocated to draw broader conclusions about the gains from reallocation. Appendix [C](https://arxiv.org/html/2510.24916v1#A3 "Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science") contains further details on how we specify the optimization problems and constraints.

The externalities of science loom large in these counterfactuals. As noted, our approach assumes all researchers’ production involves the same relative amount of externalities (per the common parameter that multiplies their private value from output into social value). In practice, externalities likely vary greatly across fields, which is why we primarily focus on reallocations *within* the five major fields of researchers in our sample (i.e., Engineering, Math and related; Humanities and related; Medical and Health Sciences; Natural Sciences; Social Sciences). We also report results where we condition researchers’ actual and counterfactual outcomes (i.e., output, utility) on the large vector of covariates used in the researcher type index. This approach allows us to isolate gains from reallocation between researchers with similar observable features.

### Summary of Counterfactuals

Table [3](https://arxiv.org/html/2510.24916v1#S7.T3 "table 3 ‣ Summary of Counterfactuals ‣ Counterfactuals and Allocative Efficiency ‣ Productivity Beliefs and Efficiency in Science") details the changes we estimate after reallocating inputs to maximize total output (Cols. 2–3) or researchers’ total utility (Cols. 4–5); Column (1) describes the actual allocation of inputs for reference. In all cases of Table [3](https://arxiv.org/html/2510.24916v1#S7.T3 "table 3 ‣ Summary of Counterfactuals ‣ Counterfactuals and Allocative Efficiency ‣ Productivity Beliefs and Efficiency in Science"), we hold the total amount of funding in each major field fixed, we only reallocate within fields, and social value is evaluated at =10\mst@varfam@dot\mst@kappa=10 (implying that scientists capture 10% of the value of their output). Given our limited ability to incorporate heterogeneous preferences into the model, Columns (3) and (5) report changes in output and welfare after removing variation in those metrics correlated with the covariates used to construct the researcher type index.282828In those cases, we regress researcher-level output or welfare metrics on the model variables and the full vector of covariates used in the type index, and then we subtract out variation in the metric predicted by the covariates conditional on the model variables. We include the model variables as controls because the productivity parameters are (partially) determined by them and so we do not want to remove variation in outcomes due to productivity differences.

table 3: Outcomes given Actual and Optimized Allocations

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Current |  | Optimized | | | |
|  | allocation |  | allocations | | | |
|  | (1) |  | (2) | (3) | (4) | (5) |
| *Research inputs* |  |  |  |  |  |  |
| Research hrs./week, avg. | 18.5 |  | +27% | +27% | +14% | +14% |
| Research hrs./week, s.d. | 9.6 |  | +43% | +43% | +43% | +43% |
| Budget $-K/year, avg. | 147.1 |  | 0% | 0% | 0% | 0% |
| Budget $-K/year, s.d. | 206.9 |  | –18% | –18% | –20% | –20% |
| *Research output* |  |  |  |  |  |  |
| Output, avg. | *n.r.* |  | +160% | +140% | +160% | +130% |
| Output, s.d. | *n.r.* |  | –5.2% | –7.9% | –5.4% | –5.7% |
| Output per hr. | *n.r.* |  | +100% | +91% | +130% | +110% |
| *Welfare* |  |  |  |  |  |  |
| Researcher utility, avg. | *n.r.* |  | +4.5% | +3.3% | +4.7% | +3.2% |
| Researcher utility, s.d. | *n.r.* |  | –5.2% | –7.9% | –5.4% | –5.7% |
| Researcher utility per hr. | *n.r.* |  | +25% | +24% | +16% | +15% |
| Social value, avg. | *n.r.* |  | +16% | +5.7% | +16% | +5.2% |
| Social value, s.d. | *n.r.* |  | +21% | –6.5% | +20% | –3.4% |
| Social value per hr. | *n.r.* |  | +34% | +27% | +26% | +19% |
| Objective, max |  |  |  |  |  |  |
| Type controls |  |  |  |  |  |  |

*Note*: Reports summary statistics for inputs under actualallocations (Col. 1). The first three sets of rows in Columns 2–5 report the percentage change in research inputs (*Research inputs*), outputs (*Research outputs*), and utility (*Welfare*) under alternative allocations; estimates are rounded to aid in comparison. The bottom sets of rows outline the objective of the counterfactuals explored in Columns 2–5. The two different objectives explored are maximizing output () or researchers’ private utility (). Models with *Type controls* report output and welfare changes after removing residual variation due to covariates used to construct the researcher type index. All optimized allocations allow for researchers’ behavioral responses.

#### Input Reallocation

The first four rows of Table [3](https://arxiv.org/html/2510.24916v1#S7.T3 "table 3 ‣ Summary of Counterfactuals ‣ Counterfactuals and Allocative Efficiency ‣ Productivity Beliefs and Efficiency in Science") report how reallocation changes the equilibrium distribution of inputs. For these rows, Columns (2–3) are identical since they are based on the same counterfactual and we do not include any controls for these statistics; likewise for Columns (4–5). Compared to the status quo, the counterfactual allocations lead to more research time on average (approximately 20%), they increase the variance in research time (approximately 40%), and they decrease the variance in research budgets (approximately –20%).

In the Appendix, we illustrate the actual and optimal input distributions as well as Lorenz curves (see Figure [D4](https://arxiv.org/html/2510.24916v1#A4.F4 "figure D4 ‣ Additional Tables and Figures ‣ Appendix D Additional Productivity and Efficiency Results ‣ Productivity Beliefs and Efficiency in Science")) to show how more or less unequal the distributions are under actual and optimal allocations. In general, the model opts to make the distribution of duties more unequal, while the inequality of the distribution of guaranteed funding is relatively unchanged. After researchers’ behavioral responses to these reallocations, there is little change in the inequality of the distribution of research time and total funding (see Figure [D4](https://arxiv.org/html/2510.24916v1#A4.F4 "figure D4 ‣ Additional Tables and Figures ‣ Appendix D Additional Productivity and Efficiency Results ‣ Productivity Beliefs and Efficiency in Science")).

#### Gains from Reallocations

Overall, the model suggests that there are large gains in output to be had from alternative allocations. Whether the objective is to maximize output or researchers’ private utility, the new allocations yield roughly 130–160% more output. Given the changes in research time, this translates into significant welfare gains on the scale of 3–4% for researchers and 5–15% for society. The finding that both objectives yield qualitatively similar gains is primarily driven by the fact that researchers have control over their time. Whatever the planner hopes to maximize, the approach is to ensure that the most productive researchers are incentivized to spend more time working on their science.

To contextualize these gains, we estimate how much more funding under actual allocations would be necessary to achieve the same growth in scientific output that our counterfactual allocations achieve using current funding levels. For simplicity, we assume these additional funds are injected into the market as proportional increases in guaranteed funds () for all researchers. Specifically, we solve for the percentage increase in researchers’ that ultimately yields the same total growth in output reported in Table [3](https://arxiv.org/html/2510.24916v1#S7.T3 "table 3 ‣ Summary of Counterfactuals ‣ Counterfactuals and Allocative Efficiency ‣ Productivity Beliefs and Efficiency in Science"). Importantly, a 1% increase in for all researchers can yield a 1% increase in aggregate funding and, in turn, output even in the absence of a behavioral response despite the fact that we have specified production as constant returns to scale. We formally describe this mechanical composition effect in Appendix [D.2](https://arxiv.org/html/2510.24916v1#A4.SS2 "Mechanical Composition Effect in the Counterfactual ‣ Appendix D Additional Productivity and Efficiency Results ‣ Productivity Beliefs and Efficiency in Science"). In short, since guaranteed funding is (weakly) less than total funding , the percentage change in a scientists’ total funding and output will vary across researchers depending on correlations between initial output shares, funding intensity parameters (i), and the share of funding from guarantees (⇑ii\mst@varfam@dot{}\_{\mst@i}/{}\_{\mst@i}); see Appendix [D.2](https://arxiv.org/html/2510.24916v1#A4.SS2 "Mechanical Composition Effect in the Counterfactual ‣ Appendix D Additional Productivity and Efficiency Results ‣ Productivity Beliefs and Efficiency in Science") for more discussion.

Table [4](https://arxiv.org/html/2510.24916v1#S7.T4 "table 4 ‣ Gains from Reallocations ‣ Summary of Counterfactuals ‣ Counterfactuals and Allocative Efficiency ‣ Productivity Beliefs and Efficiency in Science") reports these estimates under both a “*Mechanical*” scenario that does not incorporate researchers’ behavioral responses and a “*Behavioral*” scenario that does. Allowing for the behavioral response, this exercise indicates that funding guarantees would need to grow by roughly 200% for the actual allocations to achieve the same growth in output that we observe in the counterfactuals. In the case allowing a behavioral response, this corresponds to total research budgets increasing by roughly 40%. On an annual basis this amounts to roughly $60,000 per researcher. Scaling these results from our sample to the entire population of researchers targeted by the survey, this implies the gains from a more efficient allocation are equivalent to a funding increase of roughly $14 billion per year.

table 4: Growth in Funding with Actual Allocations Needed to Produce the Same Output
  
as Optimized Allocation of Actual Funding

|  | Mechanical | Behavioral |
| --- | --- | --- |
| *Relative growth in funding* |  |  |
| Guaranteed, | 210% | 206% |
| Total, | 85% | 41% |
| *Absolute growth in total funding,* |  |  |
| Sample average | +$126K | +$60K |
| Sample total | +$503M | +$240M |
| Population total | +$30,186M | +$14,444M |

*Note*: Reports the increase in guaranteed () and total () research funding under actual allocations necessary to achieve the same growth in output achieved by the reallocation of actual input levels that maximizes researchers’ utility. Sample averages on a per-researcher basis are reported in addition to sample totals (summing over all in-sample researchers) and implied population totals (scaling the sample up to the population size per the survey response rate). The *Mechanical* scenario does not allow researchers to re-optimize their time allocations and the *Behavioral* scenario does.

Notably, allowing for the behavioral response is economically important. More guaranteed research funding (which substitutes for fundraising and complements researcher time) leads researchers to spend less time fundraising and more time on their research (approximately +25% in the aggregate). Without accounting for researchers’ endogenous response to budget growth, we underestimate the impact of growing the budget by roughly two-fold.

#### Additional Results

In the Appendix, we report results from alternative counterfactual exercises (Appendix Table [D2](https://arxiv.org/html/2510.24916v1#A4.T2 "table D2 ‣ Additional Tables and Figures ‣ Appendix D Additional Productivity and Efficiency Results ‣ Productivity Beliefs and Efficiency in Science")). There are a few findings of note. First, the allocation of duties is only meaningfully relevant for influencing researchers’ utility, whereas the allocation of funding is what has the main influence on output.292929When only duties are reallocated, researchers’ utility increases by roughly 3%, but output only increases by roughly 1%. When only funding is reallocated, researchers’ utility increases by only 1%, but output increases by 150%. Maximizing output or researchers’ utility yield relatively similar outcomes Second, and rather interestingly, when we allow the total research budget to be unconstrained, and therefore only researchers’ fundraising decisions constrain the size of the budget, the total research budget grows only about 15%. While we caution against interpreting this result too seriously, but it suggests that the total research budget is not far from the optimum given the (fixed) size of the research workforce. Of course, this ignores dynamic concerns which may certainly be relevant. In other unreported analyses, we find qualitatively similar outcomes when we alter our assumptions about input caps, preference heterogeneity, and reallocation constraints, which suggest our results do not hinge on any specific modeling assumption.303030These additional specification tests are available from the authors on request.

### Input Wedges: Actual Versus Optimal

The results summarized thus far suggest that reallocating researchers’ time and funding constraints can yield significant gains in output and welfare. In order to better understand how these gains are achieved, we now focus on a single counterfactual specification and compare the actual and optimized input levels. For simplicity, we focus for the remainder of this section on the scenario where duties and funding are jointly optimized to maximize output, which corresponds to the counterfactual described in Columns (2–3) of Table [3](https://arxiv.org/html/2510.24916v1#S7.T3 "table 3 ‣ Summary of Counterfactuals ‣ Counterfactuals and Allocative Efficiency ‣ Productivity Beliefs and Efficiency in Science").

To better understand how actual and optimal input levels correlate at the individual level, we estimate a series of regressions of the following form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Actual Input Leveli=a+Optimal Input Leveli++i,i\mst@varfam@dot\text{Actual Input Level}\_{\mst@i}={\mst@a}+\mst@beta\text{Optimal Input Level}\_{\mst@i}+\mst@delta{}\_{\mst@i}+{}\_{\mst@i}\;, |  | (12) |

which relates researchers’ actual and optimal input levels possibly conditioning on one (or more) covariate . If allocations were perfectly efficient, such a regression would yield an estimate widehat=1\mst@varfam@dot\widehat{\mst@beta}=1 (with no standard error) since actual levels would equal optimal levels. If allocations are not efficient, then widehat<1\mst@varfam@dot\widehat{\mst@beta}<1.

figure 4: Actual and Optimal Input Level Correlations

![Refer to caption](x6.png)


A

![Refer to caption](x7.png)


B

*Note*: Shows the binned scatterplot of actual and optimal input levels per an objective of maximizing output. Also reports the coeffificient estimate from a regression of actual on optimal input levels and the mean absolute difference between actual and optimal input levels.

Focusing first on estimating Equation [12](https://arxiv.org/html/2510.24916v1#S7.E12 "In Input Wedges: Actual Versus Optimal ‣ Counterfactuals and Allocative Efficiency ‣ Productivity Beliefs and Efficiency in Science") with no covariates, Figure [4](https://arxiv.org/html/2510.24916v1#S7.F4 "figure 4 ‣ Input Wedges: Actual Versus Optimal ‣ Counterfactuals and Allocative Efficiency ‣ Productivity Beliefs and Efficiency in Science") reports estimates of on a binned scatterplot of the data. For both inputs, there is a clear positive relationship between researchers’ actual and optimal levels. For every hour a researcher *should* commit to research, they actually commit 0.3 hours on average. Interestingly, for every one dollar in total funding the researcher *should* have, they actually have nearly one dollar (0.987) on average. The figure also reports the mean absolute differences between actual and optimal levels, which are approximately 10 hours of research time and $70,000 in funding. For reference, these values are both roughly half the sample means.

Appendix Table [D3](https://arxiv.org/html/2510.24916v1#A4.T3 "table D3 ‣ Additional Tables and Figures ‣ Appendix D Additional Productivity and Efficiency Results ‣ Productivity Beliefs and Efficiency in Science") Column (1) replicates these univariate regressions, and then Columns (2–5) include additional sets of covariates, which are all subsets of the vector of covariates used in the researcher type index: researchers’ professional positions (e.g., rank, tenure status); their subjective measures of their research output (i.e., as reported in Table [2](https://arxiv.org/html/2510.24916v1#S3.T2 "table 2 ‣ Position and Socio-demographics ‣ Summary Statistics: Researchers and their Inputs ‣ Survey and Data Overview ‣ Productivity Beliefs and Efficiency in Science")); and their socio-demographic features (e.g., age, gender, household structure).

Examining the 2 statistics reported in Table [D3](https://arxiv.org/html/2510.24916v1#A4.T3 "table D3 ‣ Additional Tables and Figures ‣ Appendix D Additional Productivity and Efficiency Results ‣ Productivity Beliefs and Efficiency in Science") Columns (2–5) as we include different sets of covariates generally reveals small increases in 2 compared to Column (1). At most, the inclusion of the full vector of covariates increases the 2 by 4–14 percentage points. We interpret this pattern as indicating that misallocation using these sorts of observable features is a challenging exercise, and that the degree of misspecification in the model (along these specific dimensions) is relatively small. The latter gives us confidence in our results, and the former has the interesting implication that predicting which researchers are over- or under-resourced based only on their observables may be a challenging exercise.

### Case Studies of Potential Frictions

When estimating regressions of the form in Equation [12](https://arxiv.org/html/2510.24916v1#S7.E12 "In Input Wedges: Actual Versus Optimal ‣ Counterfactuals and Allocative Efficiency ‣ Productivity Beliefs and Efficiency in Science"), it is important to be careful when interpreting the coefficient. A covariate may be a significant predictor of actual levels conditional on optimal levels (i.e., widehat​0\mst@varfam@dot\widehat{\mst@delta}\neq 0) for two reasons: (i\mst@varfam@dot{\mst@i}) the feature truly is a predictor of misallocation as implied by the model, in which case a positive (negative) association indicates that the feature is predictive of a researcher being over-resourced (under-resourced) due to a friction; (i​i\mst@varfam@dot{\mst@i}{\mst@i}) there is misspecification in the model and the feature describes some heterogeneous preferences or demand variation that we have failed to capture, which has led to bias in our productivity estimates. We cannot separate these two possibilities.

Here, we embrace the interpretation that our estimates of are indicative of a friction (and not misspecification) only for two features for which misspecification is unlikely to be a major concern, but these results should still be interpreted cautiously.

First, we focus on a highly scrutinized feature: gender. A large body of work has documented a wide range of biases and frictions facing female researchers when it comes to the acquisition of inputs (or credit) for their science.313131See, for example, Witteman et al. ([2019](https://arxiv.org/html/2510.24916v1#bib.bib56)); Kim and Moser ([2025](https://arxiv.org/html/2510.24916v1#bib.bib36)). But while the vast majority of this work rejects null hypotheses and finds female researchers are under-resourced, they typically cannot formally quantify *how much* female researchers are under-resourced. Our model and approach allow us to do just that.

In Appendix Table [D3](https://arxiv.org/html/2510.24916v1#A4.T3 "table D3 ‣ Additional Tables and Figures ‣ Appendix D Additional Productivity and Efficiency Results ‣ Productivity Beliefs and Efficiency in Science"), Columns (4–5) report the results from estimating regressions of the form shown in Equation [12](https://arxiv.org/html/2510.24916v1#S7.E12 "In Input Wedges: Actual Versus Optimal ‣ Counterfactuals and Allocative Efficiency ‣ Productivity Beliefs and Efficiency in Science"), where i is an indicator for researchers who self-report as female. Whether we only include other socio-demographic covariates (Col. 4) or the full set of covariates (Col. 5), we estimate a statistically significant negative association indicating female researchers are under-resourced. They spend approximately 1 hour fewer on their research per week and have roughly $10,000 less in total research funding annually. Both of these wedges are approximately 10% of the sample mean.

Next, we focus on another question that has received much attention by meta-science scholars: the Matthew effect. In general, the Matthew effect posits that researchers amass resources beyond what their productivity warrants due to their social status (Merton [1968](https://arxiv.org/html/2510.24916v1#bib.bib40)). The specific version of this effect that we can test for is the degree to which the use of grant dollars and publication outcomes as productivity proxies distorts the allocation of inputs (e.g., Lee et al. [2013](https://arxiv.org/html/2510.24916v1#bib.bib38); Gralka, Wohlrabe, and Bornmann [2019](https://arxiv.org/html/2510.24916v1#bib.bib24)). Again, we run regressions of the form shown in Equation [12](https://arxiv.org/html/2510.24916v1#S7.E12 "In Input Wedges: Actual Versus Optimal ‣ Counterfactuals and Allocative Efficiency ‣ Productivity Beliefs and Efficiency in Science"), now including a vector of variables describing researchers’ recent grant funding and publication or citation output. As reported in Appendix Table [D4](https://arxiv.org/html/2510.24916v1#A4.T4 "table D4 ‣ Additional Tables and Figures ‣ Appendix D Additional Productivity and Efficiency Results ‣ Productivity Beliefs and Efficiency in Science"), we find some evidence of statistically significant distortions whereby a one standard deviation increase in these traditional proxies leads to over-resourcing on the scale of roughly 0.1–0.2 standard deviations (approximately 5–10% relative to the sample means).

These two cases reveal statistically significant predictors of the input wedges that are plausibly due to frictions in the allocation process. Researchers are more likely to be under-resourced if they are female, and they are more likely to be over-resourced if their observable input and output measures are higher. Still, the 2 statistics shown in Table [D3](https://arxiv.org/html/2510.24916v1#A4.T3 "table D3 ‣ Additional Tables and Figures ‣ Appendix D Additional Productivity and Efficiency Results ‣ Productivity Beliefs and Efficiency in Science") convey a seemingly novel point—these observable features, which have received so much attention thus far, explain a very small amount of the misallocation implied by the model. It appears difficult to use standard observable features to predict which researchers are over or under-resourced.

### Output Differences across Major Fields

Our final exercise seeks to understand the determinants of scientific output differences across the major fields of researchers. Doing so takes a strong stance on the comparability of output across fields, which is debatable. Thus, we treat this exercise as more speculative.

In general, the aggregate output of a market depends on input levels (i.e., the number of researchers, their funding, and their time spent on research), productivity levels (i.e., researchers’ TFP), and the market’s allocative efficiency. Here, we explore the relative importance of these three dimensions.

First, we divide all fields’ total output by the number of researchers in that field in order to compare the per capita output only. Next, we use the field with the most output, Medicine, as a benchmark and consider the other fields’ output in percentage terms relative to Medicine’s actual total (per capita) output. The gray bars in Figure [5](https://arxiv.org/html/2510.24916v1#S7.F5 "figure 5 ‣ Output Differences across Major Fields ‣ Counterfactuals and Allocative Efficiency ‣ Productivity Beliefs and Efficiency in Science") plot the total scientific output implied by the data and our productivity estimates across the five major fields of study. The four comparison fields have aggregate output levels that are roughly 25–75% that of Medicine.

figure 5: Across Field Output Comparisons

![Refer to caption](x8.png)

*Note*: Shows the per capita scientific output of each major field benchmarked to the field with the most output, Medicine. Actual output levels (in percentage terms relative to the benchmark) are shown alongisde counterfactual output levels where all fields have the same average input levels per researcher, average productivity, and allocative efficiency.

Medicine is the most resourced field, so our first test is to equate input levels across fields. In this case, aggregate output in the Social Sciences and the Humanities more than doubles. But, except for the Social Sciences most of the gap in aggregate output between each field and Medicine remains.

Average TFP levels across the fields are relatively similar such that equating productivity has little impact on differences in aggregate output. In fact, the average TFP level in Medicine is slightly lower than that of all other fields, which may be related to the size of the field.

Lastly, we use our estimates from the counterfactual where we maximize output within each of the five major fields to estimate aggregate output gaps in the scenario where all fields are equal in their allocative efficiency (i.e., output is maximized).323232Since this leads to output growth in all fields, we re-scale aggregate levels so that the level observed in the field of Medicine remains the benchmark at 100%. Here, we see a reordering of fields in terms of their per capita output. The Natural and Social sciences would produce more output than Medicine, and the other two fields would rise to producing nearly 75% the output of Medicine. In this sense, differences in allocative efficiency appear to be the most important determinant of differences in aggregate output across fields of science.

We can only speculate as to why, based on our sample of medical researchers, the field of medicine appears to be the best at allocating resources efficiently. One might think that medical researchers spend more time engaged in fundraising efforts and that process facilitates positive selection on productivity; however, medical researchers exhibit quite average levels of fundraising effort.333333The field-specific averages for fundraising hours per week are as follows: Engineering & Math = 6.1; Humanities = 2.7; Medicine = 4.9; Natural sciences = 6.7; Social Sciences = 2.5. The mean duty level for medical researchers is slightly lower relative to other fields, and the variance is much larger. This sort of allocation is consistent with the logic of our model and results — in a world with highly dispersed productivity, the planner should move non-research duties onto as few, low productivity (in the scientific sense) researchers. Of course there are both practical constraints and unmodeled objectives. For example, high-productivity researchers could plausibly have the largest externalities from their other duties (e.g., teaching) and the allocations we observe are balancing social value from research with social value from those other duties. Further work on understanding across-field differences in allocation mechanisms in science seems warranted.

## Discussion

Studies of industrial markets continue to find that a substantial share of the variation in output across sectors and regions can be attributed to differences in allocative efficiency. In this paper, we use a new approach to productivity estimation to study the market for science. Our approach allows us to estimate researchers’ productivity beliefs without observing output quantities or input prices. We find actual input allocations to be positively correlated with those that maximize plausible objectives, but we also find large gains to be had from more efficient allocations. In the counterfactuals we explore, total scientific output per research-hour or per research-dollar could be more than doubled.

Our model abstracts away from many important considerations that likely drive actual allocations (e.g., dynamic returns), and our data relies on researchers’ stated preferences. These and other limitations of our approach motivate us to interpret these magnitudes as plausible upper bounds on the gains from more efficient use of scientific inputs. Still, these large potential gains provide a glimmer of hope amid declining R&D productivity across most sectors of the economy (Bloom et al. [2020](https://arxiv.org/html/2510.24916v1#bib.bib11)) and the persistently growing burden of knowledge that raises the cost of conducting frontier science (Jones [2009](https://arxiv.org/html/2510.24916v1#bib.bib33)). Furthermore, our approach to identifying productive scientists may prove useful in talent selection processes more generally (e.g., Agarwal and Gaule [2020](https://arxiv.org/html/2510.24916v1#bib.bib4)).

Our approach has deep roots in the economics of labor (i.e., surveys of time use and work-leisure trade-offs), industrial organization (i.e., production function estimation), marketing (i.e., using surveys to identify demand functions), and macroeconomics (i.e., models of factor misallocation). By drawing on insights from these fields, our methodology allows us to overcome many of the challenges that have long plagued our understanding of productivity and efficiency in science.

Our analyses reveal researchers’ *beliefs* about their productivity and therefore their *beliefs* about how well inputs are allocated. This is a crucial limitation, since there are clearly many potential biases affecting these beliefs. Still, science is inherently about forecasting uncertain outcomes, and, therefore, the optimal mechanisms for identifying productive researchers and allocating them more inputs will need to tackle this challenge of engaging with researchers’ forecasts of their productivity. Specifically, one important next step in this line of work will be to ensure that the producers being studied report their willingness-to-pay for inputs truthfully. Of course, the theoretical underpinnings of how to elicit true willingness-to-pay estimates have long been established (e.g., Becker, DeGroot, and Marschak [1964](https://arxiv.org/html/2510.24916v1#bib.bib10)). However, the magnitudes of costs in our are on the scale of tens to hundreds of thousands of dollars. Thus, developing the practical details of incentivizing truthful responses from producers at this scale would be a fruitful endeavor.

More broadly, our approach may prove useful in other settings. There are many markets populated by a large number of producers acquiring inputs in a highly decentralized way to produce outputs that are not easy to observe. For example, in developing economies, accurate producer-level data on outputs can be difficult to obtain (e.g., Tybout [2000](https://arxiv.org/html/2510.24916v1#bib.bib55)); in entrepreneurship, many organizations never produce observable output before exiting (e.g., Decker et al. [2014](https://arxiv.org/html/2510.24916v1#bib.bib18)); and in nonprofit sectors, the output may be so high-dimensional that reaching consensus on a suitable proxy is challenging (e.g., Philipson and Lakdawalla [2001](https://arxiv.org/html/2510.24916v1#bib.bib48)). In each of these examples, our methodology could provide a way forward to better understand the distribution and determinants of productivity and efficiency.

## References

* (1)
* Ackerberg, Caves, and Frazer (2015)

  Ackerberg, Daniel A, Kevin Caves, and Garth Frazer. 2015. “Identification
  properties of recent production function estimators.” Econometrica
  83 (6): 2411–2451.
* Adams and Griliches (1998)

  Adams, James D, and Zvi Griliches. 1998. “Research Productivity in a System of
  Universities.” Annals of Economics and Statistics 49-50: 127–162.
* Agarwal and Gaule (2020)

  Agarwal, Ruchir, and Patrick Gaule. 2020. “Invisible geniuses: Could the
  knowledge frontier advance faster?” American Economic Review:
  Insights 2 (4): 409–424.
* Asker, Collard-Wexler, and De Loecker (2014)

  Asker, John, Allan Collard-Wexler, and Jan De Loecker. 2014. “Dynamic inputs
  and resource (mis) allocation.” Journal of Political Economy 122
  (5): 1013–1063.
* Asker, Collard-Wexler, and De Loecker (2019)

  Asker, John, Allan Collard-Wexler, and Jan De Loecker. 2019. “(Mis)allocation,
  market power, and global oil extraction.” American Economic Review
  109 (4): 1568–1615.
* Atkin, Khandelwal, and Osman (2019)

  Atkin, David, Amit K. Khandelwal, and Adam Osman. 2019. “Measuring
  Productivity: Lessons from Tailored Surveys and Productivity Benchmarking.”
  AEA Papers and Proceedings 109: 444–49.
* Azoulay, Fons-Rosen, and Graff Zivin (2019)

  Azoulay, Pierre, Christian Fons-Rosen, and Joshua S Graff Zivin. 2019. “Does
  science advance one funeral at a time?” American Economic Review
  109 (8): 2889–2920.
* Baruffaldi and Gaessler (2025)

  Baruffaldi, Stefano, and Fabian Gaessler. 2025. “The returns to physical
  capital in knowledge production: Evidence from lab disasters.”
  American Economic Journal: Applied Economics Forthcoming.
* Becker, DeGroot, and Marschak (1964)

  Becker, Gordon M, Morris H DeGroot, and Jacob Marschak. 1964. “Measuring
  utility by a single-response sequential method.” Behavioral Science
  9 (3): 226–232.
* Bloom et al. (2020)

  Bloom, Nicholas, Charles I Jones, John Van Reenen, and Michael Webb. 2020.
  “Are ideas getting harder to find?” American Economic Review 110
  (4): 1104–1144.
* Bloom, Sadun, and Van Reenen (2012)

  Bloom, Nicholas, Raffaella Sadun, and John Van Reenen. 2012. “The organization
  of firms across countries.” The Quarterly Journal of Economics 127
  (4): 1663–1705.
* Bryan and Williams (2021)

  Bryan, Kevin A, and Heidi L Williams. 2021. “Innovation: Market failures and
  public policies.” In Handbook of Industrial Organization, vol. 5,
  281–388: Elsevier.
* Carrillo et al. (2023)

  Carrillo, Paul, Dave Donaldson, Dina Pomeranz, and Monica Singhal. 2023.
  “Misallocation in firm production: A nonparametric analysis using
  procurement lotteries.” Mimeo.
* Cole et al. (2013)

  Cole, Shawn, Xavier Giné, Jeremy Tobacman, Petia Topalova, Robert Townsend,
  and James Vickery. 2013. “Barriers to household risk management: Evidence
  from India.” American Economic Journal: Applied Economics 5 (1):
  104–135.
* De Loecker et al. (2016)

  De Loecker, Jan, Pinelopi K Goldberg, Amit K Khandelwal, and Nina Pavcnik.
  2016. “Prices, markups, and trade reform.” Econometrica 84 (2):
  445–510.
* De Loecker and Syverson (2021)

  De Loecker, Jan, and Chad Syverson. 2021. “An industrial organization
  perspective on productivity.” In Handbook of Industrial
  Organization, vol. 4, 141–223: Elsevier.
* Decker et al. (2014)

  Decker, Ryan, John Haltiwanger, Ron Jarmin, and Javier Miranda. 2014. “The
  role of entrepreneurship in US job creation and economic dynamism.”
  Journal of Economic Perspectives 28 (3): 3–24.
* Digital Science (2018)

  Digital Science. 2018. “Dimensions [Software].” Available from
  https://app.dimensions.ai. Accessed in 2023, under licence agreement.
* Dizon-Ross and Jayachandran (2022)

  Dizon-Ross, Rebecca, and Seema Jayachandran. 2022. “Improving
  Willingness-to-Pay Elicitation by Including a Benchmark Good.” AEA
  Papers and Proceedings 112: 551–555.
* Gabaix (2009)

  Gabaix, Xavier. 2009. “Power laws in economics and finance.” Annual
  Review of Economics 1 (1): 255–294.
* Gibbons and NCSES (2024)

  Gibbons, Michael T, and NCSES. 2024. “Higher Education R&D Expenditures
  Increased 11.2%, Exceeded $108 Billion in FY 2023.” National Science
  Foundation 25-313. https://ncses.nsf.gov/pubs/nsf25313.
* Gollin and Udry (2021)

  Gollin, Douglas, and Christopher Udry. 2021. “Heterogeneity, measurement
  error, and misallocation: Evidence from African agriculture.”
  Journal of Political Economy 129 (1): 1–80.
* Gralka, Wohlrabe, and Bornmann (2019)

  Gralka, Sabine, Klaus Wohlrabe, and Lutz Bornmann. 2019. “How to measure
  research efficiency in higher education? Research grants vs. publication
  output.” Journal of Higher Education Policy and Management 41 (3):
  322–341.
* Hager, Schwarz, and Waldinger (2024)

  Hager, Sebastian, Carlo Schwarz, and Fabian Waldinger. 2024. “Measuring
  science: Performance metrics and the allocation of talent.” American
  Economic Review 114 (12): 4052–4090.
* Hall and Mairesse (2024)

  Hall, Bronwyn H, and Jacques Mairesse. 2024. “Explorations of Cumulative
  Advantage Using Data on French Physicists.”
* Heckman (1979)

  Heckman, James J. 1979. “Sample selection bias as a specification error.”
  Econometrica 47 (1): 153–161.
* Hegde and Sampat (2015)

  Hegde, Deepak, and Bhaven Sampat. 2015. “Can private money buy public science?
  Disease group lobbying and federal funding for biomedical research.”
  Management Science 61 (10): 2281–2298.
* Hill and Stein (2025)

  Hill, Ryan, and Carolyn Stein. 2025. “Race to the bottom: Competition and
  quality in science.” The Quarterly Journal of Economics 140 (2):
  1111–1185.
* Hoffman and Stanton (2024)

  Hoffman, Mitchell, and Christopher T. Stanton. 2024. “People, Practices, and
  Productivity: A Review of New Advances in Personnel Economics.” In
  Handbook of Labor Economics,: Elsevier.
* Hsieh and Klenow (2009)

  Hsieh, Chang-Tai, and Peter J Klenow. 2009. “Misallocation and manufacturing
  TFP in China and India.” The Quarterly Journal of Economics 124
  (4): 1403–1448.
* Jena and Philipson (2008)

  Jena, Anupam B, and Tomas J Philipson. 2008. “Cost-effectiveness analysis and
  innovation.” Journal of Health Economics 27 (5): 1224–1236.
* Jones (2009)

  Jones, Benjamin F. 2009. “The burden of knowledge and the “Death of the
  renaissance man”: Is innovation getting harder?” Review of
  Economic Studies 76 (1): 283–317.
* Jones (2005)

  Jones, Charles I. 2005. “Growth and ideas.” In Handbook of economic
  growth, vol. 1, 1063–1111: Elsevier.
* Kim, Petrin, and Song (2016)

  Kim, Kyoo, Amil Petrin, and Suyong Song. 2016. “Estimating production
  functions with control functions when capital is measured with error.”
  Journal of Econometrics 190 (2): 267–279.
* Kim and Moser (2025)

  Kim, Scott Daewon, and Petra Moser. 2025. “Women in science. Lessons from the
  Baby Boom.” Econometrica.
* Lakdawalla et al. (2010)

  Lakdawalla, Darius N, Eric C Sun, Anupam B Jena, Carolina M Reyes, Dana P
  Goldman, and Tomas J Philipson. 2010. “An economic evaluation of the war on
  cancer.” Journal of Health Economics 29 (3): 333–346.
* Lee et al. (2013)

  Lee, Carole J, Cassidy R Sugimoto, Guo Zhang, and Blaise Cronin. 2013. “Bias
  in peer review.” Journal of the American Society for Information
  Science and Technology 64 (1): 2–17.
* Levinsohn and Petrin (2003)

  Levinsohn, James, and Amil Petrin. 2003. “Estimating production functions
  using inputs to control for unobservables.” Review of Economic
  Studies 70 (2): 317–341.
* Merton (1968)

  Merton, Robert K. 1968. “The Matthew effect in science: The reward and
  communication systems of science are considered.” Science 159
  (3810): 56–63.
* Merton (1973)

  Merton, Robert K. 1973. The Sociology of Science: Theoretical and
  Empirical Investigations. Chicago: The University of Chicago Press.
* Myers (2020)

  Myers, Kyle R. 2020. “The Elasticity of Science.” American Economic
  Journal: Applied Economics 12 (4): 103–134.
* Myers et al. (2023)

  Myers, Kyle R, Wei Yang Tham, Nina Cohodes, Karim Lakhani, Rachel Mural,
  Jerry G Thursby, Marie C Thursby, and Yilun Xu. 2023. “New facts and data
  about US research professors.”
* National Science Foundation (2023)

  National Science Foundation. 2023. “Higher Education Research and
  Development Survey (HERD).” Available from
  https://www.nsf.gov/statistics/srvyherd/. Accessed in 2023.
* Nordhaus (2004)

  Nordhaus, William D. 2004. “Schumpeterian profits in the American economy:
  Theory and measurement.”
* Olley and Pakes (1996)

  Olley, G Steven, and Ariel Pakes. 1996. “The dynamics of productivity in the
  telecommunications equipment industry.” Econometrica 64 (6): 1263.
* Petrin and Sivadasan (2013)

  Petrin, Amil, and Jagadeesh Sivadasan. 2013. “Estimating lost output from
  allocative inefficiency, with an application to Chile and firing costs.”
  Review of Economics and Statistics 95 (1): 286–301.
* Philipson and Lakdawalla (2001)

  Philipson, Tomas, and Darius Lakdawalla. 2001. “Medical care output and
  productivity in the nonprofit sector.” In Medical Care Output and
  Productivity, edited by David M Cutler and Ernst R. Berndt, 119–140:
  University of Chicago Press.
* Restuccia and Rogerson (2017)

  Restuccia, Diego, and Richard Rogerson. 2017. “The causes and costs of
  misallocation.” Journal of Economic Perspectives 31 (3): 151–174.
* Sackman, Erikson, and Grant (1968)

  Sackman, Harold, Warren J Erikson, and E Eugene Grant. 1968. “Exploratory
  experimental studies comparing online and offline programming performance.”
  Communications of the ACM 11 (1): 3–11.
* Shapin (1995)

  Shapin, Steven. 1995. “Here and Everywhere: Sociology of Scientific
  Knowledge.” Annual Review of Sociology 21 (1): 289–321.
* Sraer and Thesmar (2023)

  Sraer, David, and David Thesmar. 2023. “How to use natural experiments to
  estimate misallocation.” American Economic Review 113 (4):
  906–938.
* Stephan (1996)

  Stephan, Paula E. 1996. “The economics of science.” Journal of
  Economic Literature 34 (3): 1199–1235.
* Syverson (2011)

  Syverson, Chad. 2011. “What determines productivity?” Journal of
  Economic Literature 49 (2): 326–365.
* Tybout (2000)

  Tybout, James R. 2000. “Manufacturing firms in developing countries: How
  well do they do, and why?” Journal of Economic Literature 38 (1):
  11–44.
* Witteman et al. (2019)

  Witteman, Holly O, Michael Hendricks, Sharon Straus, and Cara Tannenbaum. 2019.
  “Are gender gaps due to evaluations of the applicant or the science? A
  natural experiment at a national funding agency.” The Lancet 393
  (10171): 531–540.
* Wossen et al. (2024)

  Wossen, Tesfamicheal, David J Spielman, Arega D Alene, and Tahirou Abdoulaye.
  2024. “Estimating seed demand in the presence of market frictions: Evidence
  from an auction experiment in Nigeria.” Journal of Development
  Economics 167: 103242.
* Zuckerman (1988)

  Zuckerman, H. 1988. “The Sociology of Science.” In Handbook of
  Sociology, edited by NJ Smelser, 511–574: Sage Publications.

## Supplemental Appendix

## Appendix A Example Applications of Methodology

### Application 1: Constant Returns to Scale and Convex Costs

Consider first the case of a firm that operates a linear production function in a single input, e.g., labor, and faces convex adjustment costs because, e.g., there are hiring and firing frictions. The optimization problem is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxlilii−w​li−c​li\displaystyle\max\_{{\mst@l}\_{\mst@i}}\ \ {}\_{\mst@i}{\mst@l}\_{\mst@i}-{\mst@w}{\mst@l}\_{\mst@i}-{\mst@c}{\mst@l}\_{\mst@i} |  | (A1) |

with b​()=lii+mi\mst@varfam@dot{\mst@b}(\cdot)={}\_{\mst@i}{\mst@l}\_{\mst@i}+{\mst@m}\_{\mst@i} and mi=0\mst@varfam@dot{\mst@m}\_{\mst@i}=0, c​()=w​li+c​li\mst@varfam@dot{\mst@c}(\cdot)={\mst@w}{\mst@l}\_{\mst@i}+{\mst@c}{\mst@l}\_{\mst@i} (c>0\mst@varfam@dot{\mst@c}>0 and >1\mst@varfam@dot\mst@psi>1), and 𝛍i=𝛍=(w,c,)\mst@varfam@dot\bm{\upmu}\_{\mst@i}=\bm{\upmu}=({\mst@w},{\mst@c},\mst@psi).
The optimality condition of the problem is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −iw−cli−1=0\mst@varfam@dot{}\_{\mst@i}-{\mst@w}-{\mst@c}\mst@psi{\mst@l}\_{\mst@i}^{\mst@psi-1}=0 |  | (A2) |

In the first step of the estimation procedure, we evaluate the optimality condition at observed allocations to characterize i as a function of parameters and observed allocations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (l^i,w,c,)i=w+cl^i−1\mst@varfam@dot{}\_{\mst@i}(\hat{{\mst@l}}\_{\mst@i},{\mst@w},{\mst@c},\mst@psi)={\mst@w}+{\mst@c}\mst@psi\hat{{\mst@l}}\_{\mst@i}^{\mst@psi-1} |  | (A3) |

where l^i\mst@varfam@dot\hat{{\mst@l}}\_{\mst@i} denotes the observed input allocation. Moreover, conditional on attributes, parameters, and prices, the solution is determined by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | li∗=(−iwc)1−1\mst@varfam@dot{\mst@l}^{\*}\_{\mst@i}=\left(\frac{{}\_{\mst@i}-{\mst@w}}{\mst@psi{\mst@c}}\right)^{\frac{1}{\mst@psi-1}} |  | (A4) |

In the second step, we implement the thought experiment and we offer to the firm >0\mst@varfam@dot\mst@Delta>0 extra units of labor, which the firm can hire by just paying i dollars and without incurring the convex adjustment cost. Of course, the firm can re-optimize the quantity of labor that hires at market conditions. Therefore, the problem is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxl~i(l~i+)i−wl~i−cl~i−i\displaystyle\max\_{\tilde{{\mst@l}}\_{\mst@i}}\ \ {}\_{\mst@i}(\tilde{{\mst@l}}\_{\mst@i}+\mst@Delta)-{\mst@w}\tilde{{\mst@l}}\_{\mst@i}-{\mst@c}\tilde{{\mst@l}}\_{\mst@i}-{\mst@W}{\mst@T}{}\_{\mst@i} |  | (A5) |

and the solution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | l~i∗=(−iwc)1−1=li∗\mst@varfam@dot\tilde{{\mst@l}}^{\*}\_{\mst@i}=\left(\frac{{}\_{\mst@i}-{\mst@w}}{\mst@psi{\mst@c}}\right)^{\frac{1}{\mst@psi-1}}={\mst@l}^{\*}\_{\mst@i} |  | (A6) |

Replacing the solution in the profit function and equating profits at current allocations and in the thought experiment, we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | =i(l^i,w,c,)i(l~i∗+)−wl~i∗−c(l~i∗)−(l^i,w,c,)il∗+wl∗+c(l∗)\mst@varfam@dot{\mst@W}{\mst@T}{}\_{\mst@i}={}\_{\mst@i}(\hat{{\mst@l}}\_{\mst@i},{\mst@w},{\mst@c},\mst@psi)(\tilde{{\mst@l}}^{\*}\_{\mst@i}+\mst@Delta)-{\mst@w}\tilde{{\mst@l}}^{\*}\_{\mst@i}-{\mst@c}\left(\tilde{{\mst@l}}^{\*}\_{\mst@i}\right)-{}\_{\mst@i}(\hat{{\mst@l}}\_{\mst@i},{\mst@w},{\mst@c},\mst@psi){\mst@l}^{\*}+{\mst@w}{\mst@l}^{\*}+{\mst@c}\left({\mst@l}^{\*}\right) |  | (A7) |

Using the fact that l~i∗=li∗\mst@varfam@dot\tilde{{\mst@l}}^{\*}\_{\mst@i}={\mst@l}^{\*}\_{\mst@i}, we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | =i(l^i,w,c,)i=(w+cl^i−1)\mst@varfam@dot{\mst@W}{\mst@T}{}\_{\mst@i}={}\_{\mst@i}(\hat{{\mst@l}}\_{\mst@i},{\mst@w},{\mst@c},\mst@psi)\mst@Delta=\left({\mst@w}+{\mst@c}\mst@psi\hat{{\mst@l}}\_{\mst@i}^{\mst@psi-1}\right)\mst@Delta |  | (A8) |

which allows the identification of w,c,\mst@varfam@dot{\mst@w},{\mst@c},\mst@psi and thus (l^i,w,c,)i\mst@varfam@dot{}\_{\mst@i}(\hat{{\mst@l}}\_{\mst@i},{\mst@w},{\mst@c},\mst@psi), given l^i\mst@varfam@dot\hat{{\mst@l}}\_{\mst@i} and . The same logic applies to the case of decreasing returns to scale, namely:

|  |  |  |
| --- | --- | --- |
|  | maxlilii−w​li−c​li\mst@varfam@dot\max\_{{\mst@l}\_{\mst@i}}\ \ {}\_{\mst@i}{\mst@l}\_{\mst@i}-{\mst@w}{\mst@l}\_{\mst@i}-{\mst@c}{\mst@l}\_{\mst@i} |  |

with v​()=lii+mi\mst@varfam@dot{\mst@v}(\cdot)={}\_{\mst@i}{\mst@l}\_{\mst@i}+{\mst@m}\_{\mst@i} for mi=0\mst@varfam@dot{\mst@m}\_{\mst@i}=0 and (0,1)\mst@varfam@dot\mst@beta\in(0,1), c​()=w​li+c​li\mst@varfam@dot{\mst@c}(\cdot)={\mst@w}{\mst@l}\_{\mst@i}+{\mst@c}{\mst@l}\_{\mst@i} for c>0\mst@varfam@dot{\mst@c}>0 and >1\mst@varfam@dot\mst@psi>1, and 𝛍i=𝛍=(,w,c,)\mst@varfam@dot\bm{\upmu}\_{\mst@i}=\bm{\upmu}=(\mst@beta,{\mst@w},{\mst@c},\mst@psi). In the general case, the optimal input choice does not admit a closed-form expression, but we can show that l~i∗−1\mst@varfam@dot\frac{\mst@partial\tilde{{\mst@l}}^{\*}\_{\mst@i}}{\mst@partial\mst@Delta}\neq-1, i.e., the additional input does not perfectly crowd out the quantity of input sourced in the market. This is a sufficient condition such that i does depend on i and thus on all estimands 𝛍\mst@varfam@dot\bm{\upmu}.

### Application 2: Decreasing Returns to Scale and Linear Costs

Here, we show an example of how a linear cost schedule renders our approach unable to recover productivity. The setting is:

|  |  |  |
| --- | --- | --- |
|  | maxlilii−w​li\mst@varfam@dot\max\_{{\mst@l}\_{\mst@i}}\ \ {}\_{\mst@i}{\mst@l}\_{\mst@i}-{\mst@w}{\mst@l}\_{\mst@i} |  |

i.e., the problem coincides with the previous application for =0\mst@varfam@dot\mst@psi=0. The first order condition is li−1i=w\mst@varfam@dot\mst@beta{}\_{\mst@i}{\mst@l}^{\mst@beta-1}\_{\mst@i}={\mst@w}, which identifies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (l^i,,w)i=(w)l^i1−\mst@varfam@dot{}\_{\mst@i}(\hat{{\mst@l}}\_{\mst@i},\mst@beta,{\mst@w})=\left(\frac{{\mst@w}}{\mst@beta}\right)\hat{{\mst@l}}^{1-\mst@beta}\_{\mst@i} |  | (A9) |

and determines the optimal allocation as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | li∗=(iw)11−\mst@varfam@dot{\mst@l}^{\*}\_{\mst@i}=\left(\frac{\mst@beta{}\_{\mst@i}}{{\mst@w}}\right)^{\frac{1}{1-\mst@beta}} |  | (A10) |

Under the thought experiment, the optimization problem becomes:

|  |  |  |
| --- | --- | --- |
|  | maxl~i(l~i+)i−wl~i\mst@varfam@dot\max\_{\tilde{{\mst@l}}\_{\mst@i}}\ \ {}\_{\mst@i}(\tilde{{\mst@l}}\_{\mst@i}+\mst@Delta)-{\mst@w}\tilde{{\mst@l}}\_{\mst@i} |  |

which implies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | l~i∗=(iw)11−−=li∗−\mst@varfam@dot\tilde{{\mst@l}}^{\*}\_{\mst@i}=\left(\frac{\mst@beta{}\_{\mst@i}}{{\mst@w}}\right)^{\frac{1}{1-\mst@beta}}-\mst@Delta={\mst@l}^{\*}\_{\mst@i}-\mst@Delta |  | (A11) |

Replacing in the profit function and deriving i, we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | =i\displaystyle{\mst@W}{\mst@T}{}\_{\mst@i}= | (l~i∗+)i−wl~i∗−li∗i+wli∗\displaystyle{}\_{\mst@i}(\tilde{{\mst@l}}^{\*}\_{\mst@i}+\mst@Delta)-{\mst@w}\tilde{{\mst@l}}^{\*}\_{\mst@i}-{}\_{\mst@i}{\mst@l}^{\*}\_{\mst@i}+{\mst@w}{\mst@l}^{\*}\_{\mst@i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (li∗−+)i−w(li∗−)−li∗i+wli∗\displaystyle{}\_{\mst@i}({\mst@l}^{\*}\_{\mst@i}-\mst@Delta+\mst@Delta)-{\mst@w}({\mst@l}^{\*}\_{\mst@i}-\mst@delta)-{}\_{\mst@i}{\mst@l}^{\*}\_{\mst@i}+{\mst@w}{\mst@l}^{\*}\_{\mst@i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | w\displaystyle{\mst@w}\mst@Delta |  |

where from the first to the second line we replace l~i∗=li∗−\mst@varfam@dot\tilde{{\mst@l}}^{\*}\_{\mst@i}={\mst@l}^{\*}\_{\mst@i}-\mst@Delta. Because the willingness to pay just depends on w\mst@varfam@dot{\mst@w}, cannot be identified, which implies that also i is not pinned down.

### Application 3: Individuals as Producers with Utility Function

Consider the problem of an agent that gets utility from income mi\mst@varfam@dot{\mst@m}\_{\mst@i} and output dii​li1−\mst@varfam@dot{}\_{\mst@i}{\mst@d}\_{\mst@i}{\mst@l}\_{\mst@i}^{1-\mst@beta}—produced using a fixed input di\mst@varfam@dot{\mst@d}\_{\mst@i} and labor li\mst@varfam@dot{\mst@l}\_{\mst@i}—and gets disutility from working. The problem is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxliln⁡mi+(dii​li1−)−li\displaystyle\max\_{{\mst@l}\_{\mst@i}}\ \ \ln{\mst@m}\_{\mst@i}+\left({}\_{\mst@i}{\mst@d}\_{\mst@i}{\mst@l}\_{\mst@i}^{1-\mst@beta}\right)-\mst@phi{\mst@l}\_{\mst@i} |  | (A12) |

with b​()=ln⁡m​ii+(lii​di1−)\mst@varfam@dot{\mst@b}(\cdot)=\ln{\mst@m}{\mst@i}\_{\mst@i}+\left({}\_{\mst@i}{\mst@l}\_{\mst@i}{\mst@d}\_{\mst@i}^{1-\mst@beta}\right) for (0,1)\mst@varfam@dot\mst@beta\in(0,1) and (0,1)\mst@varfam@dot\mst@eta\in(0,1), c​()=li\mst@varfam@dot{\mst@c}(\cdot)=\mst@phi{\mst@l}\_{\mst@i} for >0,>1\mst@varfam@dot\mst@phi>0,\mst@psi>1, and 𝛍i=𝛍=(,,,)\mst@varfam@dot\bm{\upmu}\_{\mst@i}=\bm{\upmu}=(\mst@beta,\mst@eta,\mst@phi,\mst@psi).
The optimality condition is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1−)​dii​li(1−)−1=li−1\mst@varfam@dot\mst@eta(1-\mst@beta){}\_{\mst@i}{\mst@d}\_{\mst@i}{\mst@l}\_{\mst@i}^{(1-\mst@beta)\mst@eta-1}=\mst@phi\mst@psi{\mst@l}\_{\mst@i}^{\mst@psi-1} |  | (A13) |

Therefore:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (l^i,di,,,,)i=(l^i−1(1−)​di​l^i(1−)−1)1\mst@varfam@dot{}\_{\mst@i}(\hat{{\mst@l}}\_{\mst@i},{\mst@d}\_{\mst@i},\mst@beta,\mst@eta,\mst@phi,\mst@psi)=\left(\frac{\mst@phi\mst@psi\hat{{\mst@l}}\_{\mst@i}^{\mst@psi-1}}{\mst@eta(1-\mst@beta){\mst@d}\_{\mst@i}\hat{{\mst@l}}\_{\mst@i}^{\mst@eta(1-\mst@beta)-1}}\right)^{\frac{1}{\mst@eta}} |  | (A14) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | li∗=((1−)​dii)1−(1−)\mst@varfam@dot{\mst@l}^{\*}\_{\mst@i}=\left(\frac{\mst@eta(1-\mst@beta){}\_{\mst@i}{\mst@d}\_{\mst@i}}{\mst@phi\mst@psi}\right)^{\frac{1}{\mst@psi-\mst@eta(1-\mst@beta)}} |  | (A15) |

In the setting of a thought experiment where additional units of the fixed input are offered to the agent, the problem becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxl~iln(mi−)i+((di+)il~i1−)−l~i\displaystyle\max\_{\tilde{{\mst@l}}\_{\mst@i}}\ \ \ln\left({\mst@m}\_{\mst@i}-{\mst@W}{\mst@T}{}\_{\mst@i}\right)+\left({}\_{\mst@i}({\mst@d}\_{\mst@i}+\mst@Delta)\tilde{{\mst@l}}\_{\mst@i}^{1-\mst@beta}\right)-\mst@phi\tilde{{\mst@l}}\_{\mst@i} |  | (A16) |

with

|  |  |  |
| --- | --- | --- |
|  | l~i∗=((1−)(di+)i)1−(1−)\mst@varfam@dot\tilde{{\mst@l}}^{\*}\_{\mst@i}=\left(\frac{\mst@eta(1-\mst@beta){}\_{\mst@i}({\mst@d}\_{\mst@i}+\mst@Delta)}{\mst@phi\mst@psi}\right)^{\frac{1}{\mst@psi-\mst@eta(1-\mst@beta)}} |  |

Therefore, i solves:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ln(mi−)i+((1−))(1−)−(1−)i(di+)−(1−)−((1−)(di+)i)−(1−)+\displaystyle\ln\left({\mst@m}\_{\mst@i}-{\mst@W}{\mst@T}{}\_{\mst@i}\right)+{}\_{\mst@i}\left(\frac{\mst@eta(1-\mst@beta)}{\mst@phi\mst@psi}\right)^{\frac{\mst@eta(1-\mst@beta)}{\mst@psi-\mst@eta(1-\mst@beta)}}({\mst@d}\_{\mst@i}+\mst@Delta)^{\frac{\mst@beta\mst@psi\mst@eta}{\mst@psi-\mst@eta(1-\mst@beta)}}-\mst@phi\left(\frac{\mst@eta(1-\mst@beta){}\_{\mst@i}({\mst@d}\_{\mst@i}+\mst@Delta)}{\mst@phi\mst@psi}\right)^{\frac{\mst@psi}{\mst@psi-\mst@eta(1-\mst@beta)}}+ |  | (A17) |
|  |  | −lnmi−((1−))(1−)−(1−)idi−(1−)−((1−)​dii)−(1−)=0\displaystyle-\ln{\mst@m}\_{\mst@i}-{}\_{\mst@i}\left(\frac{\mst@eta(1-\mst@beta)}{\mst@phi\mst@psi}\right)^{\frac{\mst@eta(1-\mst@beta)}{\mst@psi-\mst@eta(1-\mst@beta)}}{\mst@d}\_{\mst@i}^{\frac{\mst@beta\mst@psi\mst@eta}{\mst@psi-\mst@eta(1-\mst@beta)}}-\mst@phi\left(\frac{\mst@eta(1-\mst@beta){}\_{\mst@i}{\mst@d}\_{\mst@i}}{\mst@phi\mst@psi}\right)^{\frac{\mst@psi}{\mst@psi-\mst@eta(1-\mst@beta)}}=0 |  |

and depends on all parameters.

## Appendix B Additional Survey Statistics and Comparisons

Table [B1](https://arxiv.org/html/2510.24916v1#A2.T1 "table B1 ‣ Appendix B Additional Survey Statistics and Comparisons ‣ Productivity Beliefs and Efficiency in Science") shows the effects of the randomized participation incentives and reminders on survey completion. Figures [B1](https://arxiv.org/html/2510.24916v1#A2.F1 "figure B1 ‣ Appendix B Additional Survey Statistics and Comparisons ‣ Productivity Beliefs and Efficiency in Science")−\mst@varfam@dot-[B2](https://arxiv.org/html/2510.24916v1#A2.F2 "figure B2 ‣ Appendix B Additional Survey Statistics and Comparisons ‣ Productivity Beliefs and Efficiency in Science") illustrate sample representativeness and Figure [B3](https://arxiv.org/html/2510.24916v1#A2.F3 "figure B3 ‣ Appendix B Additional Survey Statistics and Comparisons ‣ Productivity Beliefs and Efficiency in Science") documents the alignment between self- and publicly-reported salaries (see Myers et al. ([2023](https://arxiv.org/html/2510.24916v1#bib.bib43)) for more on the sample). Table [B2](https://arxiv.org/html/2510.24916v1#A2.T2 "table B2 ‣ Appendix B Additional Survey Statistics and Comparisons ‣ Productivity Beliefs and Efficiency in Science") describes the summary statistics for the sample on numerous dimensions. Table [B3](https://arxiv.org/html/2510.24916v1#A2.T3 "table B3 ‣ Appendix B Additional Survey Statistics and Comparisons ‣ Productivity Beliefs and Efficiency in Science") shows the pairwise correlations of the subjective output measures.

table B1: Survey Completion per Randomized Treatments

|  | (1) |
| --- | --- |
| Either incentive | 0.00297∗∗ |
|  | (0.00117) |
| Both incentives | 0.00797∗∗∗ |
|  | (0.00141) |
| 1 reminder | 0.0112∗∗∗ |
|  | (0.00114) |
| 2 reminders | 0.0188∗∗∗ |
|  | (0.00119) |
| Constant | 0.0197∗∗∗ |
|  | (0.00107) |
| obs. | 131,672 |

*Note*: Reports estimates from a regression of a binary indicator of survey completion on binary indicators for the randomized incentives and reminders including observations for all researchers emailed. Robust standard errors reported; p∗<0.10,∗∗p<0.05,∗⁣∗∗p<0.01{}^{\*}{\mskip 2.0mu\mst@p\mskip 0.0mu}<0.10,^{\*\*}{\mskip 2.0mu\mst@p\mskip 0.0mu}<0.05,^{\*\*\*}{\mskip 2.0mu\mst@p\mskip 0.0mu}<0.01.




figure B1: Sample Representativeness per Publication and Grant Funding Measures

![Refer to caption](x9.png)

-NoValue-

(*Note*: Shows the distribution of publication and grant outcomes split by whether the researcher was emailed (i.e., the full sample) versus those who completed the survey; note the log x\mst@varfam@dot{\mst@x} axes. See Myers et al. ([2023](https://arxiv.org/html/2510.24916v1#bib.bib43)) for regression-based estimates of the differences.




figure B2: Sample Representativeness per Institutional Funding Measures

![Refer to caption](x10.png)

*Note*: Shows the distribution of institution-level funding split by whether the researcher was emailed (i.e., the full sample) versus those who completed the survey. See Myers et al. ([2023](https://arxiv.org/html/2510.24916v1#bib.bib43)) for regression-based estimates of the differences.




figure B3: Correlation of Self- and Publicly-reported Annual Salaries

![Refer to caption](x11.png)

*Note*: Shows the publicly- and self-reported annual salaries for 1,369 in-sample researchers whose salaries were located in public reportings, and reports the pairwise correlation alongside the 2 statistic from a regression of self-reported on publicly-reported salary.




table B2: Summary Statistics of Other Variables

|  |  |  |
| --- | --- | --- |
|  | *mean* | *s.d.* |
| *From HERD: Institution-level R&D* |  |  |
| Total R&D, $M | 611.32 | 451.18 |
| R&D per researcher, $M | 0.61 | 0.86 |
| Share federal gov.’t R&D, [0,1] | 0.52 | 0.12 |
| Share basic R&D, [0,1] | 0.63 | 0.20 |
| *From Dimensions: Research output* |  |  |
| Publications per year | 5.28 | 7.09 |
| Citations per year | 23.07 | 49.10 |
| Co-authors per publication per year | 9.09 | 68.40 |
| *Position details* |  |  |
| Assistant professor, {0,1} | 0.26 | 0.44 |
| Associate professor, {0,1} | 0.26 | 0.44 |
| Full professor, {0,1} | 0.41 | 0.49 |
| Other rank, {0,1} | 0.07 | 0.25 |
| Not on tenure track, {0,1} | 0.19 | 0.39 |
| Pre-tenure, {0,1} | 0.22 | 0.42 |
| Tenured, {0,1} | 0.58 | 0.49 |
| Years until next contract eval. | 3.68 | 1.82 |
| Duration of contract | 2.45 | 1.93 |
| *Gender identity*, {0,1} |  |  |
| Female | 0.40 | 0.49 |
| Male | 0.55 | 0.50 |
| Other or N.R | 0.05 | 0.22 |
| *Racial/ethnic identity*, {0,1} |  |  |
| Asian | 0.13 | 0.33 |
| Black | 0.03 | 0.18 |
| Hispanic | 0.06 | 0.23 |
| White | 0.77 | 0.42 |
| Other or N.R | 0.05 | 0.21 |
| *Citizenship*, {0,1} |  |  |
| Citizen, domestic-born | 0.71 | 0.45 |
| Citizen or perm resident, foreign-born | 0.24 | 0.43 |
| Other or N.R citizenship | 0.05 | 0.21 |
| 1st–3rd generation in U.S. | 0.30 | 0.46 |
| Other or N.R generation in U.S. | 0.70 | 0.46 |
| *Other covariates* |  |  |
| Age | 48.78 | 12.05 |
| Household total income | 260,336.00 | 215,388.31 |
| Married or domestic partnership, {0,1} | 0.82 | 0.39 |
| Single, {0,1} | 0.13 | 0.34 |
| Other or N.R relationship, {0,1} | 0.05 | 0.22 |
| Dependents in household | 0.98 | 1.13 |
| Risk-taking in personal life, [0,10] | 5.26 | 2.13 |

*Note*: Reports summary statistics for 4,003 researcher-level observations. *From HERD* indicates variables from National Science Foundation ([2023](https://arxiv.org/html/2510.24916v1#bib.bib44)). *From Dimensions* indicates variables from the Digital Science ([2018](https://arxiv.org/html/2510.24916v1#bib.bib19)) dataset. *N.R.* stands for Not Reported.




table B3: Pairwise Correlations of Subjective Output Measures

|  | Articles | Books | Methods | Products | Academic | Policy | Business | Public |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Articles |  |  |  |  |  |  |  |  |
| Books | –0.13s |  |  |  |  |  |  |  |
| Methods | 0.08s | –0.20s |  |  |  |  |  |  |
| Products | –0.13s | –0.12s | 0.23s |  |  |  |  |  |
| Academic | 0.48s | –0.01 | 0.02 | –0.24s |  |  |  |  |
| Policy | 0.01 | –0.00 | 0.10s | 0.25s | –0.07s |  |  |  |
| Business | –0.03 | –0.07s | 0.20s | 0.38s | –0.12s | 0.24s |  |  |
| Public | –0.12s | 0.19s | 0.04 | 0.21s | –0.20s | 0.28s | 0.13s |  |

*Note*: Reports pairwise correlations for the four subjective measures of researchers’ intended output types (Journal articles; Books; Materials or Methods; Products) and the four subjective measures of researchers’ intended audiences (Academic peers; Policymakers; Businesses and organizations; General public); ps<0.01{}^{{\mst@s}}{\mskip 2.0mu\mst@p\mskip 0.0mu}<0.01.

## Appendix C Additional Model and Experiment Details

### Derivation of Policy Functions

The policy functions (Si,𝛉i,𝛍i)\mst@varfam@dot\mathcal{{\mst@R}}(\text{{S}}\_{\mst@i},\bm{\uptheta}\_{\mst@i},\bm{\upmu}\_{\mst@i}), (Si,𝛉i,𝛍i)\mst@varfam@dot\mathcal{{\mst@F}}(\text{{S}}\_{\mst@i},\bm{\uptheta}\_{\mst@i},\bm{\upmu}\_{\mst@i}) and (Si,𝛉i,𝛍i)\mst@varfam@dot\mathcal{{\mst@H}}(\text{{S}}\_{\mst@i},\bm{\uptheta}\_{\mst@i},\bm{\upmu}\_{\mst@i}) characterize the solution (,i∗,i∗)i∗\mst@varfam@dot({}^{\*}\_{\mst@i},{}^{\*}\_{\mst@i},{}^{\*}\_{\mst@i}) to problem ([7](https://arxiv.org/html/2510.24916v1#S4.E7 "In Researchers’ Labor Supply ‣ Model of Science ‣ Productivity Beliefs and Efficiency in Science")) for each individual scientist i\mst@varfam@dot{\mst@i} as a function of states Si\mst@varfam@dot\text{{S}}\_{\mst@i}, attributes 𝛉i\mst@varfam@dot\bm{\uptheta}\_{\mst@i}, and parameters 𝛍i\mst@varfam@dot\bm{\upmu}\_{\mst@i}. They determine indirect utility ∗i=(Si,𝛉i,𝛍i)\mst@varfam@dot\mathcal{{\mst@V}}^{\*}\_{\mst@i}=\mathcal{{\mst@V}}(\text{{S}}\_{\mst@i},\bm{\uptheta}\_{\mst@i},\bm{\upmu}\_{\mst@i}) at current allocations. Substituting the constraints, the utility maximization problem is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ()=max,iiu1​i()i+u2​i((+min+i)iiii(−i−i)i1−i)−u3​i(,i)i,\displaystyle\mathcal{{\mst@V}}(\cdot)=\max\_{{}\_{\mst@i},{}\_{\mst@i}}{\mst@u}\_{1{\mst@i}}({}\_{\mst@i})+{\mst@u}\_{2{\mst@i}}({}\_{\mst@i}\left({}\_{\text{min}}+{}\_{\mst@i}+{}\_{\mst@i}{}\_{\mst@i}\right)^{{}\_{\mst@i}}\left({}\_{\mst@i}-{}\_{\mst@i}-{}\_{\mst@i}\right)^{1-{}\_{\mst@i}})-{\mst@u}\_{3{\mst@i}}({}\_{\mst@i},{}\_{\mst@i})\;, |  | (C1) |

with the policy functions (,,)\mst@varfam@dot\mathcal{{\mst@F}}(\cdot,\cdot,\cdot) and (,,)\mst@varfam@dot\mathcal{{\mst@H}}(\cdot,\cdot,\cdot) solving the optimality conditions:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | u2,i()iiii+,i\mst@varfam@dot\displaystyle\frac{\mst@partial{\mst@u}\_{2,{\mst@i}}({}\_{\mst@i})}{\mst@partial{}\_{\mst@i}}\frac{\mst@partial{}\_{\mst@i}}{\mst@partial{}\_{\mst@i}}+{}\_{{\mst@F},{\mst@i}} | =0\mst@varfam@dot\displaystyle=0\;\; |  |  | (C2) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | u2,i()iiii−u3,i(,i)ii−,i\mst@varfam@dot\displaystyle\frac{\mst@partial{\mst@u}\_{2,{\mst@i}}({}\_{\mst@i})}{\mst@partial{}\_{\mst@i}}\frac{\mst@partial{}\_{\mst@i}}{\mst@partial{}\_{\mst@i}}-\frac{\mst@partial{\mst@u}\_{3,{\mst@i}}({}\_{\mst@i},{}\_{\mst@i})}{\mst@partial{}\_{\mst@i}}-{}\_{{\mst@H},{\mst@i}} | =0,\mst@varfam@dot\displaystyle=0\;, |  |  | (C3) |

and (,,)\mst@varfam@dot\mathcal{{\mst@R}}(\cdot,\cdot,\cdot) being residually determined based on the time-constraint ([7c](https://arxiv.org/html/2510.24916v1#S4.E7.3 "In 7 ‣ Researchers’ Labor Supply ‣ Model of Science ‣ Productivity Beliefs and Efficiency in Science")). To derive the policy functions, we start from model’s optimality conditions ([C3](https://arxiv.org/html/2510.24916v1#A3.E3 "In Derivation of Policy Functions ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")) and ([C3](https://arxiv.org/html/2510.24916v1#A3.E3 "In Derivation of Policy Functions ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")) and evaluate them using the functional forms described in the main text. We obtain the conditions:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ((+min+i)ii−1ii−(1−)i(−i−i)i−1⌋i1−i+,i\mst@varfam@dot\displaystyle{}\_{\mst@i}^{1-{}\_{\mst@i}}\Big[{}\_{\mst@i}{}\_{\mst@i}({}\_{\text{min}}+{}\_{\mst@i}+{}\_{\mst@i}{}\_{\mst@i})^{-1}-(1-{}\_{\mst@i})({}\_{\mst@i}-{}\_{\mst@i}-{}\_{\mst@i})^{-1}\Big]+{}\_{{\mst@F},{\mst@i}} | =0\mst@varfam@dot\displaystyle=0\;\; |  |  | (C4) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | (−i−i)i−1i1−i(1−)i−(−i+i)iii−,i\mst@varfam@dot\displaystyle{}\_{\mst@i}^{1-{}\_{\mst@i}}({}\_{\mst@i}-{}\_{\mst@i}-{}\_{\mst@i})^{-1}(1-{}\_{\mst@i})-\mst@psi({}\_{\mst@i}-{}\_{\mst@i}+{}\_{\mst@i}^{{}\_{\mst@i}})^{{}\_{\mst@i}}-{}\_{{\mst@H},{\mst@i}} | =0​.\mst@varfam@dot\displaystyle=0\;. |  |  | (C5) |

We characterize the policy functions in two intervals of i. The first is (,i⌋i,>0i\mst@varfam@dot{}\_{\mst@i}\in({}\_{\mst@i},{}\_{{\mst@i},{\mst@F}>0}] and the second is (,i,>0⌋maxi\mst@varfam@dot{}\_{\mst@i}\in({}\_{{\mst@i},{\mst@F}>0},{}\_{\text{max}}], depending on whether the optimal fundraising time allocation is a corner solution (=i0\mst@varfam@dot{}\_{\mst@i}=0) or not (>i0\mst@varfam@dot{}\_{\mst@i}>0). We identify the threshold i,>0 below which optimal fundraising is zero by solving ([C5](https://arxiv.org/html/2510.24916v1#A3.E5 "In Derivation of Policy Functions ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")) for i as a function of i assuming that i is strictly positive, i.e., =,i0\mst@varfam@dot{}\_{{\mst@F},{\mst@i}}=0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | =i(−i)ii−1−ii(+min)i.\mst@varfam@dot{}\_{\mst@i}={}\_{\mst@i}({}\_{\mst@i}-{}\_{\mst@i})-\frac{1-{}\_{\mst@i}}{{}\_{\mst@i}}({}\_{\text{min}}+{}\_{\mst@i})\;. |  | (C6) |

Therefore, ([C6](https://arxiv.org/html/2510.24916v1#A3.E6 "In Derivation of Policy Functions ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")) implies that fundraising time is strictly positive as long as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | >i+i1−iii(+min)i,\mst@varfam@dot{}\_{\mst@i}>{}\_{\mst@i}+\frac{1-{}\_{\mst@i}}{{}\_{\mst@i}{}\_{\mst@i}}({}\_{\text{min}}+{}\_{\mst@i})\;, |  | (C7) |

which identifies the threshold i,>0 that is strictly larger than i as long as <i1\mst@varfam@dot{}\_{\mst@i}<1. As a consequence, we can solve for optimal hours i using equation ([C5](https://arxiv.org/html/2510.24916v1#A3.E5 "In Derivation of Policy Functions ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")), which takes the piece-wise functional form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {(1−)i((+min)iii⌋1−i(−i)i(1−)i(1−)i−1−(−i+i)iii−=,i0ifi,>0i(()iiii(1−)i1−i⌋1−i(−i+miniii)−i−(−i+i)iii−=,i0if>ii,>0\mst@varfam@dot\begin{{\mst@c}{\mst@a}{\mst@s}{\mst@e}{\mst@s}}(1-{}\_{\mst@i})[{}\_{\mst@i}({}\_{\text{min}}+{}\_{\mst@i})^{{}\_{\mst@i}}]^{1-{}\_{\mst@i}}({}\_{\mst@i}-{}\_{\mst@i})^{(1-{}\_{\mst@i})(1-{}\_{\mst@i})-1}-\mst@psi({}\_{\mst@i}-{}\_{\mst@i}+{}\_{\mst@i}^{{}\_{\mst@i}})^{{}\_{\mst@i}}-{}\_{{\mst@H},{\mst@i}}=0&\text{if}\ {}\_{\mst@i}\leq{}\_{{\mst@i},{\mst@F}>0}\\ \Big[{}\_{\mst@i}({}\_{\mst@i}{}\_{\mst@i})^{{}\_{\mst@i}}(1-{}\_{\mst@i})^{1-{}\_{\mst@i}}\Big]^{1-{}\_{\mst@i}}\Big({}\_{\mst@i}-{}\_{\mst@i}\frac{{}\_{\text{min}}+{}\_{\mst@i}}{{}\_{\mst@i}}\Big)^{-{}\_{\mst@i}}-\mst@psi({}\_{\mst@i}-{}\_{\mst@i}+{}\_{\mst@i}^{{}\_{\mst@i}})^{{}\_{\mst@i}}-{}\_{{\mst@H},{\mst@i}}=0&\text{if}\ {}\_{\mst@i}>{}\_{{\mst@i},{\mst@F}>0}\end{{\mst@c}{\mst@a}{\mst@s}{\mst@e}{\mst@s}} |  | (C8) |

and defines an implicit solution i\mst@varfam@dot\mathcal{{\mst@H}}\_{\mst@i} for i as a function of all parameters and state variables. ([C8](https://arxiv.org/html/2510.24916v1#A3.E8 "In Derivation of Policy Functions ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")) is continuous but not differentiable at i,>0. Moreover, the Lagrange multiplier ,i equals zero for <imax\mst@varfam@dot{}\_{\mst@i}<{}\_{\text{max}} and i is always strictly larger than i because limii([C8](https://arxiv.org/html/2510.24916v1#A3.E8 "In Derivation of Policy Functions ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science"))=+\mst@varfam@dot\lim\_{{}\_{\mst@i}\rightarrow{}\_{\mst@i}}\eqref{eq:solH}=+\infty. Hence, the non-negativity constraint on research time is always met. Given the policy function i\mst@varfam@dot\mathcal{{\mst@H}}\_{\mst@i} for hours, the functions defining optimal allocation to fundraising time and research time are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | i={0ifii,>0(i−)ii−1−ii(+min)iifi>i,>0\mst@varfam@dot\mathcal{{\mst@F}}\_{\mst@i}=\begin{{\mst@c}{\mst@a}{\mst@s}{\mst@e}{\mst@s}}0&\text{if}\ \mathcal{{\mst@H}}\_{\mst@i}\leq{}\_{{\mst@i},{\mst@F}>0}\\ {}\_{\mst@i}(\mathcal{{\mst@H}}\_{\mst@i}-{}\_{\mst@i})-\frac{1-{}\_{\mst@i}}{{}\_{\mst@i}}({}\_{\text{min}}+{}\_{\mst@i})&\text{if}\ \mathcal{{\mst@H}}\_{\mst@i}>{}\_{{\mst@i},{\mst@F}>0}\end{{\mst@c}{\mst@a}{\mst@s}{\mst@e}{\mst@s}} |  | (C9) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | i=i−−ii.\mst@varfam@dot\mathcal{{\mst@R}}\_{\mst@i}=\mathcal{{\mst@H}}\_{\mst@i}-{}\_{\mst@i}-\mathcal{{\mst@F}}\_{\mst@i}\;. |  | (C10) |

### Reducing Dimensions of Heterogeneity: k\mst@varfam@dot{\mst@k}-means Clustering Results

Ideally, our model would allow for rich heterogeneity in researchers’ preferences (i.e., the u1,i​()\mst@varfam@dot{\mst@u}\_{1,{\mst@i}}(\cdot), u2,i​()\mst@varfam@dot{\mst@u}\_{2,{\mst@i}}(\cdot), and u3,i​()\mst@varfam@dot{\mst@u}\_{3,{\mst@i}}(\cdot) functions). This would help ensure that (true) variation in preferences would not mistakenly be attributed as (estimated) variation in productivity. We lack enough data to estimate researcher-specific preference functions, but we do have the large vector of observables from the survey i\mst@varfam@dot\mathbf{{\mst@X}}\_{\mst@i}.343434We could allow the parameters that govern the preference functions to depend on deep parameters and these observables. For example, for the preference function parameter i, we could assume that =iexp(+,0\slimits@x)i,x\mst@varfam@dot{}\_{\mst@i}=\exp({}\_{\mst@sigma,0}+\tsum\slimits@\_{\mst@x}{}\_{\mst@i}{}\_{\mst@sigma,{\mst@x}}). However, this presents some practical estimation challenges (i.e., estimating approximately (353=) 105 additional parameters; the ,x parameters in the previous example). This motivates the approach outlined in Section [4](https://arxiv.org/html/2510.24916v1#S4 "Model of Science ‣ Productivity Beliefs and Efficiency in Science"). We use k\mst@varfam@dot{\mst@k}-means clustering to collapse the multi-dimensional heterogeneity from the observables i\mst@varfam@dot\mathbf{{\mst@X}}\_{\mst@i} into a single-dimensional index, i. Specifically, we assume there are two clusters of researcher types (k\mst@varfam@dot{\mst@k}=2), and we use k\mst@varfam@dot{\mst@k}-means clustering to estimate each researcher’s euclidean distance from one of those groups; we use that distance as i, which provides a smooth, continuous measure of heterogeneity. Thus, for the preference function parameter i, we assume that =iexp(+,0)i\mst@varfam@dot{}\_{\mst@i}=\exp({}\_{\mst@sigma,0}+{}\_{\mst@i}). Figure [C1](https://arxiv.org/html/2510.24916v1#A3.F1 "figure C1 ‣ Reducing Dimensions of Heterogeneity: 𝑘-means Clustering Results ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science") shows the distribution of the one-dimensional euclidean similarity scores. Researchers with larger values of i tend to be, among other things, older, white, males that are full professors in the humanities and natural sciences. A table reporting the mean differences between the two types of researchers is available upon request.

figure C1: Researcher Heterogeneity

![Refer to caption](x12.png)

*Note*: Shows the distribution of the log-transformed and standardized euclidean similarity scores from the k\mst@varfam@dot{\mst@k}-means cluster estimation with two k\mst@varfam@dot{\mst@k}=I,II.

### Estimation Outline

We infer individual attributes and parameters using a mix of calibration and estimation. First, we set minimum funding =m​i​n$5,000\mst@varfam@dot{}\_{{\mst@m}{\mst@i}{\mst@n}}=\mst@varfam@mathdollar 5,000 and fix total hours endowment max to 62 work hours per week (approximately the 90th percentile of the observed work hours). Second, we estimate individual attributes and common parameters of the utility function, including deep parameters that determine individual-specific parameters in 𝛍i\mst@varfam@dot\bm{\upmu}\_{\mst@i} as functions of researcher’s type i. We use survey information on hours worked, research time, fundraising time, guaranteed funding, expected additional funds raised, duties, and the salaries reported in the alternative offer experiments, which we map to model counterparts (,i,i,i,i,ii,i{}i​jj=14)\mst@varfam@dot({}\_{\mst@i},{}\_{\mst@i}\,,\,{}\_{\mst@i}\,,\,{}\_{\mst@i}\,,\,{}\_{\mst@i}{}\_{\mst@i}\,,\,{}\_{\mst@i}\,,\,\{{}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}}\}\_{{\mskip 2.0mu\mst@j\mskip 0.0mu}=1}^{4}), respectively.

Conditional on some common parameters, we can infer individual-specific attributes 𝛉i\mst@varfam@dot\bm{\uptheta}\_{\mst@i} from researchers’ optimality conditions and model’s structure. One important note is that we have separate estimation routines for inferring individual attributes 𝛉i\mst@varfam@dot\bm{\uptheta}\_{\mst@i} among researchers with non-zero fundraising time (>i0\mst@varfam@dot{}\_{\mst@i}>0) and those at a corner solution (=i0\mst@varfam@dot{}\_{\mst@i}=0). For the former group, we first infer fundraising ability i by exploiting the identity equating the observed, expected additional funding (i) to ii\mst@varfam@dot{}\_{\mst@i}{}\_{\mst@i}. Therefore, i=1,…,\mst@varfam@dot\forall\mskip 0.0mu{\mst@i}=1,...,:

|  |  |  |  |
| --- | --- | --- | --- |
|  | widehati=ii​.\mst@varfam@dot\widehat{\mst@phi}\_{\mst@i}=\frac{{\mst@E}{}\_{\mst@i}}{{}\_{\mst@i}}\;. |  | (C11) |

Expression ([C11](https://arxiv.org/html/2510.24916v1#A3.E11 "In Estimation Outline ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")) is well-defined if and only if observed >i0\mst@varfam@dot{}\_{\mst@i}>0, which is why the inference strategy must differ for researchers with =i0\mst@varfam@dot{}\_{\mst@i}=0 at observed allocations.353535For numerical stability, we constrain widehati​1\mst@varfam@dot\widehat{\mst@phi}\_{\mst@i}\geq 1. As a second step, conditional on widehati\mst@varfam@dot\widehat{\mst@phi}\_{\mst@i}, we infer factor shares iwidehat\mst@varfam@dot\widehat{{}\_{\mst@i}} from researchers’ first order condition in fundraising time, which we derive in Appendix [C.1](https://arxiv.org/html/2510.24916v1#A3.SS1 "Derivation of Policy Functions ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science"). For the chosen functional forms, this takes the expression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | widehati=i+iii=+min+iwidehatii+min+iwidehati+iwidehatii​.\mst@varfam@dot\widehat{\mst@gamma}\_{\mst@i}=\frac{{}\_{\mst@i}}{{}\_{\mst@i}+{}\_{\mst@i}{}\_{\mst@i}}=\frac{{}\_{\text{min}}+{}\_{\mst@i}+\widehat{\mst@phi}\_{\mst@i}{}\_{\mst@i}}{{}\_{\text{min}}+{}\_{\mst@i}+\widehat{\mst@phi}\_{\mst@i}{}\_{\mst@i}+\widehat{\mst@phi}\_{\mst@i}{}\_{\mst@i}}\;. |  | (C12) |

Equation ([C12](https://arxiv.org/html/2510.24916v1#A3.E12 "In Estimation Outline ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")) states that i constitutes the weight of total funding over the total dollar-value of inputs used in scientific activity, with the last term of the denominator being the dollar-valued opportunity cost of research time relative to fundraising. Finally, the optimality condition for total hours worked determines productivity widehati\mst@varfam@dot\widehat{\mst@alpha}\_{\mst@i} as a function of parameters, observed allocations, and widehati\mst@varfam@dot\widehat{\mst@phi}\_{\mst@i} and widehati\mst@varfam@dot\widehat{\mst@gamma}\_{\mst@i}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1−widehati)iwidehati1−i(+min+iwidehati)i(1−)iwidehati=i(1−)i(1−widehati)−1(−i+i)iii,\mst@varfam@dot{}\_{\mst@i}(1-\widehat{\mst@gamma}\_{\mst@i})\widehat{\mst@alpha}\_{\mst@i}^{1-{}\_{\mst@i}}({}\_{\text{min}}+{}\_{\mst@i}+\widehat{\mst@phi}\_{\mst@i}{}\_{\mst@i})^{(1-{}\_{\mst@i})\widehat{\mst@gamma}\_{\mst@i}}{}\_{\mst@i}^{(1-{}\_{\mst@i})(1-\widehat{\mst@gamma}\_{\mst@i})-1}=\mst@psi({}\_{\mst@i}-{}\_{\mst@i}+{}\_{\mst@i}^{{}\_{\mst@i}})^{{}\_{\mst@i}}\;, |  | (C13) |

This equation holds exactly if <imax\mst@varfam@dot{}\_{\mst@i}<{}\_{\text{max}}. Therefore, Equations ([C11](https://arxiv.org/html/2510.24916v1#A3.E11 "In Estimation Outline ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")), ([C12](https://arxiv.org/html/2510.24916v1#A3.E12 "In Estimation Outline ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")), and ([C13](https://arxiv.org/html/2510.24916v1#A3.E13 "In Estimation Outline ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")) determine individual attributes as functions of parameters and observed allocations for researchers with positive fundraising time. Unfortunately, for the group of researchers reporting zero fundraising time, we can neither infer widehati\mst@varfam@dot\widehat{\mst@phi}\_{\mst@i} from Equation ([C11](https://arxiv.org/html/2510.24916v1#A3.E11 "In Estimation Outline ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")), nor can we compute widehati\mst@varfam@dot\widehat{\mst@gamma}\_{\mst@i}.363636The Lagrange multiplier ,i is strictly positive and unknown. Therefore, we assume that i and i are parametric polynomial functions of state variables, and we estimate these functions using the other sub-sample of researchers with >i0\mst@varfam@dot{}\_{\mst@i}>0.373737We use the following specifications: =iexp{\slimits@p=13+,pip\slimits@p=13+,pip\slimits@p=13},pip\mst@varfam@dot{}\_{\mst@i}=\exp\left\{\tsum\slimits@\_{{\mskip 2.0mu\mst@p\mskip 0.0mu}=1}^{3}{}\_{{\mst@G},{\mskip 2.0mu\mst@p\mskip 0.0mu}}{}^{\mskip 2.0mu\mst@p\mskip 0.0mu}\_{\mst@i}+\tsum\slimits@\_{{\mskip 2.0mu\mst@p\mskip 0.0mu}=1}^{3}{}\_{{\mst@D},{\mskip 2.0mu\mst@p\mskip 0.0mu}}{}^{\mskip 2.0mu\mst@p\mskip 0.0mu}\_{\mst@i}+\tsum\slimits@\_{{\mskip 2.0mu\mst@p\mskip 0.0mu}=1}^{3}{}\_{{\mst@M},{\mskip 2.0mu\mst@p\mskip 0.0mu}}{}^{\mskip 2.0mu\mst@p\mskip 0.0mu}\_{\mst@i}\right\}, and =i(1+exp{\slimits@p=13+,pip\slimits@p=13+,pip\slimits@p=13},pip)−1\mst@varfam@dot{}\_{\mst@i}=\left(1+\exp\left\{\tsum\slimits@\_{{\mskip 2.0mu\mst@p\mskip 0.0mu}=1}^{3}{}\_{{\mst@G},{\mskip 2.0mu\mst@p\mskip 0.0mu}}{}^{\mskip 2.0mu\mst@p\mskip 0.0mu}\_{\mst@i}+\tsum\slimits@\_{{\mskip 2.0mu\mst@p\mskip 0.0mu}=1}^{3}{}\_{{\mst@D},{\mskip 2.0mu\mst@p\mskip 0.0mu}}{}^{\mskip 2.0mu\mst@p\mskip 0.0mu}\_{\mst@i}+\tsum\slimits@\_{{\mskip 2.0mu\mst@p\mskip 0.0mu}=1}^{3}{}\_{{\mst@M},{\mskip 2.0mu\mst@p\mskip 0.0mu}}{}^{\mskip 2.0mu\mst@p\mskip 0.0mu}\_{\mst@i}\right\}\right)^{-1}, which we estimate using poisson and logistic regressions. Whenever the fitted (widehati,widehati)\mst@varfam@dot(\widehat{\mst@phi}\_{\mst@i},\widehat{\mst@gamma}\_{\mst@i}) combination would imply, given the observed state variables and for a specific vector of parameters 𝛍i\mst@varfam@dot\bm{\upmu}\_{\mst@i}, that the optimal (observed) time allocation to fundraising would be strictly positive, we re-scale widehati\mst@varfam@dot\widehat{\mst@phi}\_{\mst@i} below the individual-specific lower bound below which the optimal fundraising time at observed states is indeed null.

Finally, given the estimates attributes widehati\mst@varfam@dot\widehat{\mst@phi}\_{\mst@i} and widehati\mst@varfam@dot\widehat{\mst@gamma}\_{\mst@i}, the state variables, and the vector of common parameters 𝛍widehat\mst@varfam@dot\widehat{\bm{\upmu}}, we infer productivity beliefs widehati\mst@varfam@dot\widehat{\mst@alpha}\_{\mst@i} through Equation ([C13](https://arxiv.org/html/2510.24916v1#A3.E13 "In Estimation Outline ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")). Given estimates of individual attributes 𝛉widehati=(widehati,widehati,widehati)\mst@varfam@dot\widehat{\bm{\uptheta}}\_{\mst@i}=(\widehat{\mst@alpha}\_{\mst@i},\widehat{\mst@gamma}\_{\mst@i},\widehat{\mst@phi}\_{\mst@i}) as functions of parameters 𝛍=(,,𝛅)\mst@varfam@dot\bm{\upmu}=(\mst@omega,\mst@psi,\bm{\updelta}), calibrated values (,min)max\mst@varfam@dot({}\_{\text{min}},{}\_{\text{max}}), and observed allocations, we estimate the vector 𝛍\mst@varfam@dot\bm{\upmu} by generalized method of moments as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝛍widehat=argmin𝛍(𝛍)=argmin𝛍\slimits@i=1\slimits@j=14(−i​jobswidehati​j(Si​j,𝛉widehati(𝛍i(𝛍,)i),𝛍i(𝛍,)i))2,\mst@varfam@dot\widehat{\bm{\upmu}}=\arg\min\_{\bm{\upmu}}\mathcal{{\mst@L}}(\bm{\upmu})=\arg\min\_{\bm{\upmu}}\tsum\slimits@\_{{\mst@i}=1}\tsum\slimits@\_{{\mskip 2.0mu\mst@j\mskip 0.0mu}=1}^{4}\left({}^{\text{obs}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}}-\widehat{{\mst@M}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}}(\text{{S}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}},\widehat{\bm{\uptheta}}\_{\mst@i}(\bm{\upmu}\_{\mst@i}(\bm{\upmu},{}\_{\mst@i})),\bm{\upmu}\_{\mst@i}(\bm{\upmu},{}\_{\mst@i}))\right)^{2}\;, |  | (C14) |

where i​j\mst@varfam@dot{}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}} is researcher i\mst@varfam@dot{\mst@i}’s answer to thought experiment j\mst@varfam@dot{\mskip 2.0mu\mst@j\mskip 0.0mu} in the data and widehati​j\mst@varfam@dot\widehat{{\mst@M}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}} is its model-based counterpart, which is itself an implicit function of the vector of counterfactual states Si\mst@varfam@dot\text{{S}}\_{\mst@i}, researcher’s type i, and of the estimand 𝛍\mst@varfam@dot\bm{\upmu} which determines individual attributes 𝛉widehati\mst@varfam@dot\widehat{\bm{\uptheta}}\_{\mst@i} and individual-specific parameters 𝛍i\mst@varfam@dot\bm{\upmu}\_{\mst@i}.383838To save notation, we omit that widehati​j\mst@varfam@dot\widehat{{\mst@M}}\_{{\mst@i}{\mskip 2.0mu\mst@j\mskip 0.0mu}} are also a function of calibrated (,min)max\mst@varfam@dot({}\_{\text{min}},{}\_{\text{max}}). Parameter estimates 𝛍widehat\mst@varfam@dot\widehat{\bm{\upmu}} solve ([C14](https://arxiv.org/html/2510.24916v1#A3.E14 "In Estimation Outline ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")) conditional on parameter restrictions specified in Section [4.1](https://arxiv.org/html/2510.24916v1#S4.SS1 "Researchers’ Labor Supply ‣ Model of Science ‣ Productivity Beliefs and Efficiency in Science"). Appendix [C.4](https://arxiv.org/html/2510.24916v1#A3.SS4 "Estimation Algorithm ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science") provides additional details on the search algorithm.

### Estimation Algorithm

Here, we describe the estimation of the common parameters
  
𝛍=(,,,,0,,1,,0,,1,,0,,1,,0),1\mst@varfam@dot\bm{\upmu}=(\mst@omega,\mst@psi,{}\_{\mst@sigma,0},{}\_{\mst@sigma,1},{}\_{\mst@eta,0},{}\_{\mst@eta,1},{}\_{\mst@xi,0},{}\_{\mst@xi,1},{}\_{\mst@zeta,0},{}\_{\mst@zeta,1}). First, we define a grid of parameter values at which we perform a preliminary evaluation of the loss function in ([C14](https://arxiv.org/html/2510.24916v1#A3.E14 "In Estimation Outline ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")). The grid is defined by the Cartesian product of the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (0)=(0.1,1,10⌋,(0)=(0.00001,1,10⌋,\displaystyle\bm{\mst@omega}^{(0)}=[1,1,0]\;,\quad\bm{\mst@psi}^{(0)}=[00001,1,0]\;, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ,0(0)=(−100,0⌋,,1(0)=(0⌋,\displaystyle\bm{\mst@delta}\_{\mst@sigma,0}^{(0)}=[-00,0]\;,\quad\bm{\mst@delta}\_{\mst@sigma,1}^{(0)}=[0]\;, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ,0(0)=(ln(0.8)−ln(0.2),0,ln(0.2)−ln(0.8)⌋,,1(0)=(0⌋\displaystyle\bm{\mst@delta}\_{\mst@eta,0}^{(0)}=[\ln(8)-\ln(2),0,\ln(2)-\ln(8)]\;,\quad\bm{\mst@delta}\_{\mst@eta,1}^{(0)}=[0] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ,0(0)=(−11.5,ln(2)⌋,,1(0)=(0⌋,\displaystyle\bm{\mst@delta}\_{\mst@xi,0}^{(0)}=[-15,\ln(2)]\;,\quad\bm{\mst@delta}\_{\mst@xi,1}^{(0)}=[0]\;, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ,0(0)=(−11.5,0⌋,,1(0)=(0⌋.\displaystyle\bm{\mst@delta}\_{\mst@zeta,0}^{(0)}=[-15,0]\;,\quad\bm{\mst@delta}\_{\mst@zeta,1}^{(0)}=[0]\;. |  |

Second, we select the grid-points where the value of the loss function is within 0.5% of the minimum, and we use them as initial points for the numerical solution. We perform a preliminary “Nelder-Mead simplex direct search” with a high tolerance on the loss function and standard tolerance on parameter values. We then select the parameters vectors where the value of the loss function is within 1% of the minimum, and we use them as initial points with the same search algorithm and with lower loss function tolerance. We repeat this step twice until we are left with a single candidate optimal parameter vector.

### Objectives and Constraints for Counterfactuals

We first analyze a setting where social planner’s objective is to maximize field-specific aggregate scientist’s utility by reallocating guaranteed funding i and administrative duties i within the major field. We define the output function

|  |  |  |
| --- | --- | --- |
|  | i(widetildei,widetildei,)f=(+min+i(widetildei,widetildei,)fi)ii(widetildei,widetildei,)f1−i\mst@varfam@dot\mathcal{{\mst@Y}}\_{\mst@i}(\widetilde{{\mst@G}}\_{\mst@i},\widetilde{{\mst@D}}\_{\mst@i},{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu})={}\_{\mst@i}\left({}\_{\text{min}}+{}\_{\mst@i}+{}\_{\mst@i}\mathcal{{\mst@F}}(\widetilde{{\mst@G}}\_{\mst@i},\widetilde{{\mst@D}}\_{\mst@i},{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu})\right)^{{}\_{\mst@i}}\mathcal{{\mst@R}}(\widetilde{{\mst@G}}\_{\mst@i},\widetilde{{\mst@D}}\_{\mst@i},{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu})^{1-{}\_{\mst@i}}\, |  |

where the adjustment factor f\mst@varfam@dot{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu} to fundraising ability in field f\mst@varfam@dot{\mskip 3.0mu\mst@f\mskip 0.0mu} enforces the constraint that additional funding in the counterfactual allocation must equal observed funding. For convenience, in this section we omit from the notation the dependence of the policy functions on attributes 𝛉widehati\mst@varfam@dot\widehat{\bm{\uptheta}}\_{\mst@i} and parameters 𝛍widehati\mst@varfam@dot\widehat{\bm{\upmu}}\_{\mst@i}. Therefore, the problem in field f\mst@varfam@dot{\mskip 3.0mu\mst@f\mskip 0.0mu} is:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | max(widetildei,widetildei)i=1f\displaystyle\max\_{(\widetilde{{\mst@G}}\_{\mst@i},\widetilde{{\mst@D}}\_{\mst@i})\_{{\mst@i}=1}^{{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu}}} | \slimits@i=1f​(i(widetildei,widetildei,)f1−i1−i−(i(widetildei,widetildei,)f−iwidetilde+widetildeii)1+i1+i)\displaystyle\tsum\slimits@\_{{\mst@i}=1}^{{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu}}\biggl(\mst@kappa\frac{\mathcal{{\mst@Y}}\_{\mst@i}(\widetilde{{\mst@G}}\_{\mst@i},\widetilde{{\mst@D}}\_{\mst@i},{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu})^{1-{}\_{\mst@i}}}{1-{}\_{\mst@i}}-\mst@psi\frac{(\mathcal{{\mst@H}}\_{\mst@i}(\widetilde{{\mst@G}}\_{\mst@i},\widetilde{{\mst@D}}\_{\mst@i},{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu})-\widetilde{{}\_{\mst@i}}+\widetilde{{\mst@D}}\_{\mst@i}^{{}\_{\mst@i}})^{1+{}\_{\mst@i}}}{1+{}\_{\mst@i}}\biggr) |  | (C15) |
|  |  | subject to |  |
|  |  | \slimits@i=1fwidetildei=widehatt​o​t(Multiplier⌋,f\displaystyle\tsum\slimits@\_{{\mst@i}=1}^{{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu}}\widetilde{{\mst@G}}\_{\mst@i}=\widehat{{\mst@G}}^{{\mst@t}{\mst@o}{\mst@t}}\;\;\;[\text{Multiplier}\ {}\_{{\mst@G},{\mskip 3.0mu\mst@f\mskip 0.0mu}}] |  |
|  |  | \slimits@i=1fwidetildei=widehatt​o​t(Multiplier⌋,f\displaystyle\tsum\slimits@\_{{\mst@i}=1}^{{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu}}\widetilde{{\mst@D}}\_{\mst@i}=\widehat{{\mst@D}}^{{\mst@t}{\mst@o}{\mst@t}}\;\;\;[\text{Multiplier}\ {}\_{{\mst@D},{\mskip 3.0mu\mst@f\mskip 0.0mu}}] |  |
|  |  | \slimits@i=1f=i\slimits@i=1ffwidehatii(widetildei,widetildei,)f,\displaystyle\tsum\slimits@\_{{\mst@i}=1}^{{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu}}{\mst@E}{}\_{\mst@i}={}\_{\mskip 3.0mu\mst@f\mskip 0.0mu}\tsum\slimits@\_{{\mst@i}=1}^{{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu}}\widehat{\mst@phi}\_{\mst@i}\mathcal{{\mst@F}}\_{\mst@i}(\widetilde{{\mst@G}}\_{\mst@i},\widetilde{{\mst@D}}\_{\mst@i},{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu})\;, |  |

where f\mst@varfam@dot{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu} is the number of scientists in field f\mst@varfam@dot{\mskip 3.0mu\mst@f\mskip 0.0mu}. We also impose non-negativity constraints on individual widetildei\mst@varfam@dot\widetilde{{\mst@G}}\_{\mst@i} and widetildei\mst@varfam@dot\widetilde{{\mst@D}}\_{\mst@i} allocations. The individual research output function i=widehatiiwidehatii1−widehati\mst@varfam@dot\mathcal{{\mst@Y}}\_{\mst@i}=\widehat{\mst@alpha}\_{\mst@i}\mathcal{{\mst@B}}\_{\mst@i}^{\widehat{\mst@gamma}\_{\mst@i}}\mathcal{{\mst@R}}\_{\mst@i}^{1-\widehat{\mst@gamma}\_{\mst@i}} and hours i\mst@varfam@dot\mathcal{{\mst@H}}\_{\mst@i} make explicit that both are functions of the considered instruments (widetildei,widetildei)\mst@varfam@dot(\widetilde{{\mst@G}}\_{\mst@i},\widetilde{{\mst@D}}\_{\mst@i}). The last constraint requires that total additional funding in the observed allocations. Therefore, all the policy functions not only vary with policy levers (widetildei,widetildei)\mst@varfam@dot(\widetilde{{\mst@G}}\_{\mst@i},\widetilde{{\mst@D}}\_{\mst@i}) but also with f\mst@varfam@dot{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu}, which can be interpreted as an endogenous adjustment to fundraising probability. When the new allocation violates the constraint, fundraising probability uniformly shrinks, thus reducing additional funding both directly and indirectly through the behavioral decline in fundraising hours.

In the optimal allocations, the planner seeks to equate the marginal utility of guaranteed funding and duties across individuals, conditional on the non-negativity constraint and the additional funding constraint. Therefore, the solution satisfies the following equations for each i=1,…,f\mst@varfam@dot{\mst@i}=1,...,{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | did​widetildei=i−idid​widetildei−(i−widetildei+widetildeii)iiwidetildei=−,f,∗i\mst@varfam@dot\displaystyle\frac{{\mst@d}\mathcal{{\mst@V}}\_{\mst@i}}{{\mst@d}\widetilde{{\mst@G}}\_{\mst@i}}=\mst@kappa\mathcal{{\mst@Y}}\_{\mst@i}^{-{}\_{\mst@i}}\frac{{\mst@d}\mathcal{{\mst@Y}}\_{\mst@i}}{{\mst@d}\widetilde{{\mst@G}}\_{\mst@i}}-\mst@psi(\mathcal{{\mst@H}}\_{\mst@i}-\widetilde{{\mst@D}}\_{\mst@i}+\widetilde{{\mst@D}}\_{\mst@i}^{{}\_{\mst@i}})^{{}\_{\mst@i}}\frac{\mst@partial\mathcal{{\mst@H}}\_{\mst@i}}{\mst@partial\widetilde{{\mst@G}}\_{\mst@i}}={}\_{{\mst@G},{\mskip 3.0mu\mst@f\mskip 0.0mu}}-{}\_{{}^{\*},{\mst@i}} |  | (C16) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | did​widetildei=i−idid​widetildei−(i−widetildei+)iii(iwidetildei−1+widetildei−i1i)=−,f,,∗i\mst@varfam@dot\displaystyle\frac{{\mst@d}\mathcal{{\mst@V}}\_{\mst@i}}{{\mst@d}\widetilde{{\mst@D}}\_{\mst@i}}=\mst@kappa\mathcal{{\mst@Y}}\_{\mst@i}^{-{}\_{\mst@i}}\frac{{\mst@d}\mathcal{{\mst@Y}}\_{\mst@i}}{{\mst@d}\widetilde{{\mst@D}}\_{\mst@i}}-\mst@psi(\mathcal{{\mst@H}}\_{\mst@i}-\widetilde{{\mst@D}}\_{\mst@i}+{}\_{\mst@i}^{{}\_{\mst@i}})^{{}\_{\mst@i}}\Bigl(\frac{\mst@partial\mathcal{{\mst@H}}\_{\mst@i}}{\mst@partial\widetilde{{\mst@D}}\_{\mst@i}}-1+{}\_{\mst@i}\widetilde{{\mst@D}}\_{\mst@i}^{{}\_{\mst@i}-1}\Bigr)={}\_{{\mst@D},{\mskip 3.0mu\mst@f\mskip 0.0mu}}-{}\_{{}^{\*},{\mst@i}}\;, |  | (C17) |

where the marginal product of guaranteed funds did​widetildei\mst@varfam@dot\frac{{\mst@d}\mathcal{{\mst@Y}}\_{\mst@i}}{{\mst@d}\widetilde{{\mst@G}}\_{\mst@i}} and the (negative) marginal product of duties did​widetildei\mst@varfam@dot\frac{{\mst@d}\mathcal{{\mst@Y}}\_{\mst@i}}{{\mst@d}\widetilde{{\mst@D}}\_{\mst@i}} are determined by equations ([C18](https://arxiv.org/html/2510.24916v1#A3.E18 "In Objectives and Constraints for Counterfactuals ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")) and ([C19](https://arxiv.org/html/2510.24916v1#A3.E19 "In Objectives and Constraints for Counterfactuals ‣ Appendix C Additional Model and Experiment Details ‣ Productivity Beliefs and Efficiency in Science")), respectively:

|  |  |  |  |
| --- | --- | --- | --- |
|  | didi=widehatiiwidehatii1−widehati​(widehatii−1​iiwidetilde+(1−widehati)i−1​iiwidetilde)\mst@varfam@dot\displaystyle\frac{{\mst@d}\mathcal{{\mst@Y}}\_{\mst@i}}{{\mst@d}{}\_{\mst@i}}=\widehat{\mst@alpha}\_{\mst@i}\mathcal{{\mst@B}}\_{\mst@i}^{\widehat{\mst@gamma}\_{\mst@i}}\mathcal{{\mst@R}}\_{\mst@i}^{1-\widehat{\mst@gamma}\_{\mst@i}}\Bigl(\widehat{\mst@gamma}\_{\mst@i}\mathcal{{\mst@B}}\_{\mst@i}^{-1}\frac{\mst@partial\mathcal{{\mst@B}}\_{\mst@i}}{\mst@partial\widetilde{{}\_{\mst@i}}}+(1-\widehat{\mst@gamma}\_{\mst@i})\mathcal{{\mst@R}}\_{\mst@i}^{-1}\frac{\mst@partial\mathcal{{\mst@R}}\_{\mst@i}}{\mst@partial\widetilde{{}\_{\mst@i}}}\Bigr) |  | (C18) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | didi=widehatiiwidehatii1−widehati​(widehatii−1​iiwidetilde+(1−widehati)i−1​iiwidetilde)​.\mst@varfam@dot\displaystyle\frac{{\mst@d}\mathcal{{\mst@Y}}\_{\mst@i}}{{\mst@d}{}\_{\mst@i}}=\widehat{\mst@alpha}\_{\mst@i}\mathcal{{\mst@B}}\_{\mst@i}^{\widehat{\mst@gamma}\_{\mst@i}}\mathcal{{\mst@R}}\_{\mst@i}^{1-\widehat{\mst@gamma}\_{\mst@i}}\Bigl(\widehat{\mst@gamma}\_{\mst@i}\mathcal{{\mst@B}}\_{\mst@i}^{-1}\frac{\mst@partial\mathcal{{\mst@B}}\_{\mst@i}}{\mst@partial\widetilde{{}\_{\mst@i}}}+(1-\widehat{\mst@gamma}\_{\mst@i})\mathcal{{\mst@R}}\_{\mst@i}^{-1}\frac{\mst@partial\mathcal{{\mst@R}}\_{\mst@i}}{\mst@partial\widetilde{{}\_{\mst@i}}}\Bigr)\;. |  | (C19) |

Total funding as a function of state variables is defined by i(,i,i)f=+min+iwidehatiif(,i,i)f\mst@varfam@dot\mathcal{{\mst@B}}\_{\mst@i}({}\_{\mst@i},{}\_{\mst@i},{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu})={}\_{\text{min}}+{}\_{\mst@i}+{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu}\widehat{\mst@phi}\_{\mst@i}\mathcal{{\mst@F}}\_{\mst@i}({}\_{\mst@i},{}\_{\mst@i},{}\_{\mskip 3.0mu\mst@f\mskip 0.0mu}).

figure C2: Example Image of Survey Experiment

![Refer to caption](x13.png)

*Note*: Shows a screenshot of the survey experiment designed to solicit researchers’ willingness to trade off their salary for additional guaranteed funding.




figure C3: Correlations of Implied Valuations

![Refer to caption](x14.png)


A

![Refer to caption](x15.png)


B

*Note*: Shows a binned scatterplot and line-of-fit for the relationship between researchers’ implied hourly wage and their willingness to pay for 1 less hour of administrative duties (Panel A), and the relationship between how many hours per week a researcher spends on fundraising and their willingness to pay for $1 more of additional research funds conditional on their implied hourly wage (Panel B).




table C1: Proportion of Response Variation Correlated with Model and Non-model Variables

|  | WTP +$250K | |  | WTP +$1M | |  | WTP +admin. | |  | WTP –admin. | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (1) | (2) |  | (3) | (4) |  | (5) | (6) |  | (7) | (8) |
| 2 | 0.95 | 0.96 |  | 0.87 | 0.89 |  | 0.82 | 0.86 |  | 0.96 | 0.97 |
| Model vars. |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
| obs. | 4,003 | 4,003 |  | 4,003 | 4,003 |  | 4,003 | 4,003 |  | 4,003 | 4,003 |

*Note*: Reports the 2 statistics from regressions of researchers’ responses to the four experiments (i.e., their willingness to pay for the alternative scenarios) on different combinations of variables: *Model vars.* includes the state and choice variables of the model;  includes the full vector of variables that comprise the type index.




table C2: Potential Role of Non-response Bias and Stated Preference WTP Bias

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | WTP +$250K | |  | WTP +$1M | |  | WTP +admin. | |  | WTP –admin. | |
|  | (1) | (2) |  | (3) | (4) |  | (5) | (6) |  | (7) | (8) |
| IMR |  | –0.000858 |  |  | –0.00391 |  |  | –0.00466 |  |  | –0.000835 |
|  |  | (0.00379) |  |  | (0.00593) |  |  | (0.00684) |  |  | (0.00327) |
| Benchmark |  | –0.0126∗∗∗ |  |  | –0.0258∗∗∗ |  |  | 0.0134∗ |  |  | –0.0102∗∗∗ |
|  |  | (0.00411) |  |  | (0.00644) |  |  | (0.00742) |  |  | (0.00355) |
| 2 | 0.95 | 0.95 |  | 0.87 | 0.87 |  | 0.82 | 0.82 |  | 0.96 | 0.96 |
| Model vars. |  |  |  |  |  |  |  |  |  |  |  |
| obs. | 4,003 | 4,003 |  | 4,003 | 4,003 |  | 4,003 | 4,003 |  | 4,003 | 4,003 |

*Note*: Reports the estimates from regressions of researchers’ responses to the four experiments (i.e., their willingness to pay for the alternative scenarios) on a control for non-response bias in the form of the Inverse Mills Ratio (IMR) and a control for bias in individuals’ stated WTP in the form of their WTP for the benchmark good (i.e., high-speed internet at home); all variables are standardized. *Model vars.* includes the state and choice variables of the model. Robust standard errors reported; p∗<0.10,∗∗p<0.05,∗⁣∗∗p<0.01{}^{\*}{\mskip 2.0mu\mst@p\mskip 0.0mu}<0.10,^{\*\*}{\mskip 2.0mu\mst@p\mskip 0.0mu}<0.05,^{\*\*\*}{\mskip 2.0mu\mst@p\mskip 0.0mu}<0.01.

## Appendix D Additional Productivity and Efficiency Results

### Additional Tables and Figures

figure D1: Utility Function Visualization

![Refer to caption](x16.png)


A

![Refer to caption](x17.png)


B

![Refer to caption](x18.png)


C

![Refer to caption](x19.png)


D

*Note*: Shows the percent change in utility in four of the key model variables (Panels A–D) holding all other variables and parameters fixed at the sample means. The black line (left y\mst@varfam@dot{\mskip 2.0mu\mst@y\mskip 0.0mu} axis) shows the percent change in utility as the focal variable increases from the 10th percentile to the 90th percentile. The histogram (right y\mst@varfam@dot{\mskip 2.0mu\mst@y\mskip 0.0mu} axis) shows the distribution of the focal variable in the sample. Note the different scales of all y\mst@varfam@dot{\mskip 2.0mu\mst@y\mskip 0.0mu} axes.
For simplicity, behavioral responses where researchers re-optimize are not incorporated here.




figure D2: Research Funding Intensity () by Minor Field of Study

![Refer to caption](x20.png)

*Note*: Shows the mean and standard deviations of researcher-specific estimates of the production function parameter i (funding intensity) split by minor field of study.




figure D3: Power Laws in the TFP Tail

![Refer to caption](x21.png)


A

![Refer to caption](x22.png)


B

*Note*: Shows the log rank of researchers’ TFP (i, where the sample mean is normalized to 1) versus the log of the TFP for either the top 20% of researchers (Panel a) or the top 1% (Panel b). The power law exponent reported is based on the linear regression of log rank on log TFP (see the dashed line) following Gabaix ([2009](https://arxiv.org/html/2510.24916v1#bib.bib21)).




table D1: Observable Output Correlations

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Recent publications, | |  | Recent publications, | |
|  | count | |  | cite-weighted | |
|  | (1) | (2) |  | (3) | (4) |
| log​()\mst@varfam@dot\log(\mst@alpha) | 0.201∗∗∗ | 0.176∗∗∗ |  | 0.276∗∗∗ | 0.254∗∗∗ |
|  | (0.0406) | (0.0397) |  | (0.0648) | (0.0648) |
| log⁡(recent grant $)\mst@varfam@dot\log(\text{recent grant \textdollar}) |  | 0.0220∗∗∗ |  |  | 0.0174∗∗∗ |
|  |  | (0.00350) |  |  | (0.00525) |
| Field–FE, ,,\mst@varfam@dot\mst@gamma,\mst@phi,\mathbf{{\mst@X}}–index |  |  |  |  |  |
| 2 | 0.18 | 0.20 |  | 0.15 | 0.16 |
| obs. | 2,703 | 2,703 |  | 2,703 | 2,703 |

*Note*: Reports the estimates from regressions of researchers’ publication measures (including publications from 2018–2022) on their estimated research productivity () as well as vector of controls that includes major field fixed effects (*Field-FE*) and the researchers’ funding intensity (), fundraising efficiency (), their type (-*index*), and, in some specifications, a control for their publicly observable research grant funding over the same period. Robust standard errors reported; p∗<0.10,∗∗p<0.05,∗⁣∗∗p<0.01{}^{\*}{\mskip 2.0mu\mst@p\mskip 0.0mu}<0.10,^{\*\*}{\mskip 2.0mu\mst@p\mskip 0.0mu}<0.05,^{\*\*\*}{\mskip 2.0mu\mst@p\mskip 0.0mu}<0.01.




figure D4: Lorenz Curves for Actual and Optimal Input Levels

![Refer to caption](x23.png)


A

![Refer to caption](x24.png)


B

![Refer to caption](x25.png)


C

![Refer to caption](x26.png)


D

*Note*: Shows Lorenz curves for actual and optimal input levels. Researchers are sorted on the x\mst@varfam@dot{\mst@x} axis per their ranking in terms of how much of each input they have, and the lines plot the cumulative share of total inputs (per the y\mst@varfam@dot{\mskip 2.0mu\mst@y\mskip 0.0mu} axis) summing from the lowest- to highest-ranked researcher. Thus, plots closer to the 45o\mst@varfam@dot 45^{\mst@o} line indicate input allocations closer to equality.




table D2: Production with Actual and Optimized Allocations—Alternative Counterfactuals

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Current |  | Optimized | | | | |
|  | allocation |  | allocations | | | | |
|  | (1) |  | (2) | (3) | (4) | (5) | (6) |
| *Research inputs* |  |  |  |  |  |  |  |
| Research hrs./week, avg. | 18.5 |  | –11% | +18% | +14% | +25% | +16% |
| Research hrs./week, s.d. | 9.6 |  | +6.0% | +18% | +43% | +39% | +41% |
| Budget $-K/year, avg. | 147.1 |  | 0% | 0% | 0% | 0% | +14% |
| Budget $-K/year, s.d. | 206.9 |  | +14% | –24% | –20% | –20% | –3.9% |
| *Research output* |  |  |  |  |  |  |  |
| Output, avg. | *n.r.* |  | +1.3% | +150% | +160% | +160% | +160% |
| Output, s.d. | *n.r.* |  | +0.7% | +43% | +44% | +44% | +44% |
| Output per hr. | *n.r.* |  | +14% | +110% | +130% | +110% | +120% |
| Output per $ | *n.r.* |  | +1.4% | +150% | +160% | +160% | +130% |
| *Welfare* |  |  |  |  |  |  |  |
| Researcher utility, avg. | *n.r.* |  | +3.6% | +1.0% | +4.7% | +2.1% | +4.7% |
| Researcher utility, s.d. | *n.r.* |  | –5.7% | +0.3% | –5.4% | –2.4% | –5.4% |
| Researcher utility per hr. | *n.r.* |  | –8.3% | +16% | +16% | +21% | +18% |
| Researcher utility per $ | *n.r.* |  | +3.6% | +1.0% | +4.8% | +2.3% | +16% |
| Social value, avg. | *n.r.* |  | +3.4% | +12% | +16% | +13% | +16% |
| Social value, s.d. | *n.r.* |  | –4.0% | +23% | +20% | +21% | +20% |
| Social value per hr. | *n.r.* |  | –8.5% | +25% | +26% | +30% | +28% |
| Social value per $ | *n.r.* |  | +3.4% | +12% | +16% | +13% | +26% |
| *Input reallocation* |  |  |  |  |  |  |  |
| Research hrs./week |  |  | 9% | 19% | 27% | 24% | 25% |
| Budget $-K/year |  |  | 14% | 27% | 28% | 25% | 25% |
| Objective, max |  |  |  |  |  |  |  |
| Reallocate |  |  |  |  |  |  |  |
| Reallocate |  |  |  |  |  |  |  |
| Unconstrained |  |  |  |  |  |  |  |

*Note*: Reports summary statistics for inputs under actual allocations (Col. 1). The first three sets of rows in Columns 2–6 report the percentage change in research inputs (*Research inputs*), outputs (*Research outputs*), and utility (*Welfare*) under alternative allocations; estimates are rounded to aid in comparison. The *Input Reallocation* rows report the amount of inputs reallocated expressed as a percentage of the total level of the input (e.g., 50% implies that half of all dollars are moved from one researcher to another). The bottom sets of rows outline the objective and constraints of the five different counterfactual allocations explored in Columns 2–6. The two different objectives explored are maximizing researchers’ private utility () or output ().  refers to administrative duties, and  refers to guaranteed research funding.  *Unconstrained*  indicates the scenario when the total research budget is left unconstrained and so the total amount of funding in the market is limited only by researchers’ fundraising choices. All optimized allocations allow for researchers’ behavioral responses after  and/or  have been reallocated.

table D3: Input Wedges and Gender Differences

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) | (5) |
| *Panel (a): Actual research time* | | | | |  |
| Optimal level | 0.301∗∗∗ | 0.294∗∗∗ | 0.300∗∗∗ | 0.352∗∗∗ | 0.349∗∗∗ |
|  | (0.00970) | (0.00989) | (0.00991) | (0.00985) | (0.0102) |
| Female |  |  |  | –1.333∗∗∗ | –0.885∗∗∗ |
|  |  |  |  | (0.286) | (0.279) |
| 2 | 0.18 | 0.22 | 0.26 | 0.24 | 0.32 |
| : position |  |  |  |  |  |
| : output |  |  |  |  |  |
| : socio–demog. |  |  |  |  |  |
| obs. | 4,003 | 4,003 | 4,003 | 4,003 | 4,003 |
| *Panel (b): Actual research funding* | | | | |  |
| Optimal level | 0.987∗∗∗ | 0.982∗∗∗ | 0.928∗∗∗ | 0.985∗∗∗ | 0.932∗∗∗ |
|  | (0.00856) | (0.00883) | (0.0102) | (0.00939) | (0.0109) |
| Female |  |  |  | –12111.4∗∗∗ | –7907.5∗∗ |
|  |  |  |  | (3950.8) | (3872.1) |
| 2 | 0.65 | 0.65 | 0.67 | 0.67 | 0.69 |
| : position |  |  |  |  |  |
| : output |  |  |  |  |  |
| : socio–demog. |  |  |  |  |  |
| obs. | 4,003 | 4,003 | 4,003 | 4,003 | 4,003 |

*Note*: Reports results from regressions of actual input levels on optimal input levels and as described in Equation [12](https://arxiv.org/html/2510.24916v1#S7.E12 "In Input Wedges: Actual Versus Optimal ‣ Counterfactuals and Allocative Efficiency ‣ Productivity Beliefs and Efficiency in Science"). Robust standard errors reported; p∗<0.10,∗∗p<0.05,∗⁣∗∗p<0.01{}^{\*}{\mskip 2.0mu\mst@p\mskip 0.0mu}<0.10,^{\*\*}{\mskip 2.0mu\mst@p\mskip 0.0mu}<0.05,^{\*\*\*}{\mskip 2.0mu\mst@p\mskip 0.0mu}<0.01.




table D4: Input Wedges per Common Productivity Proxies

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) |
| *Panel (a): Actual research time* | | | |  |
| Optimal level | 0.508∗∗∗ | 0.506∗∗∗ | 0.509∗∗∗ | 0.508∗∗∗ |
|  | (0.0164) | (0.0166) | (0.0162) | (0.0163) |
| Recent research funding, own | 0.130∗∗∗ |  |  |  |
|  | (0.0311) |  |  |  |
| Recent research funding, institution |  | –0.0137 |  |  |
|  |  | (0.0139) |  |  |
| Recent publications |  |  | 0.177∗∗∗ |  |
|  |  |  | (0.0197) |  |
| Recent citations |  |  |  | 0.148∗∗∗ |
|  |  |  |  | (0.0223) |
| 2 | 0.32 | 0.30 | 0.33 | 0.32 |
| : position, output, socio–demog. |  |  |  |  |
| obs. | 3,072 | 3,057 | 3,072 | 3,072 |
| *Panel (b): Actual research funding* | | | |  |
| Optimal level | 0.746∗∗∗ | 0.763∗∗∗ | 0.744∗∗∗ | 0.753∗∗∗ |
|  | (0.0110) | (0.00974) | (0.0106) | (0.0101) |
| Recent research funding, own | 0.0767∗∗∗ |  |  |  |
|  | (0.0264) |  |  |  |
| Recent research funding, institution |  | 0.00202 |  |  |
|  |  | (0.00958) |  |  |
| Recent publications |  |  | 0.0760∗∗∗ |  |
|  |  |  | (0.0153) |  |
| Recent citations |  |  |  | 0.0592∗∗∗ |
|  |  |  |  | (0.0142) |
| 2 | 0.70 | 0.69 | 0.69 | 0.69 |
| : position, output, socio–demog. |  |  |  |  |
| obs. | 3,072 | 3,057 | 3,072 | 3,072 |

*Note*: Reports results from regressions of actual input levels on optimal input levels and common proxies for researchers’ producitivities. All variables are standardized. All proxies are based on data from one to two years prior to the survey. Robust standard errors reported; p∗<0.10,∗∗p<0.05,∗⁣∗∗p<0.01{}^{\*}{\mskip 2.0mu\mst@p\mskip 0.0mu}<0.10,^{\*\*}{\mskip 2.0mu\mst@p\mskip 0.0mu}<0.05,^{\*\*\*}{\mskip 2.0mu\mst@p\mskip 0.0mu}<0.01.

### Mechanical Composition Effect in the Counterfactual

In Section [7.2](https://arxiv.org/html/2510.24916v1#S7.SS2 "Summary of Counterfactuals ‣ Counterfactuals and Allocative Efficiency ‣ Productivity Beliefs and Efficiency in Science"), we estimate the growth in funding using current allocations that is necessary to achieve the same growth in output that we achieve using alternative allocations of the current funding. We choose guaranteed funding () as our policy lever for injecting funding into the market because it is exogenous in the model.393939The other component of funding, which researchers obtain via fundraising, is the product of an exogenous component (researchers’ fundraising productivity, i) and an endogenous component (researchers’ time spent fundraising, i). Practically, it is much easier to engage with simulations that manipulate , especially when behavioral responses are allowed. In the main counterfactual, we find that a 210% increase in guaranteed funding for all researchers—equivalent to a 210% increase in aggregate guaranteed funding (\slimits@ii\mst@varfam@dot{\mst@G}\equiv\tsum\slimits@\_{\mst@i}{}\_{\mst@i})—translates into an 85% increase in total aggregate funding (\slimits@ii\mst@varfam@dot{\mst@B}\equiv\tsum\slimits@\_{\mst@i}{}\_{\mst@i}), which then yields a 160% increase in aggregate output (\slimits@ii\mst@varfam@dot{\mst@Y}\equiv\tsum\slimits@\_{\mst@i}{}\_{\mst@i}). This may seem counterintuitive given that our specification of the scientific production function features decreasing returns to funding (<i1\mst@varfam@dot{}\_{\mst@i}<1 for all i\mst@varfam@dot{\mst@i}). Below, we explain how this can occur.

Recall the production functions is: =ii1−iiii\mst@varfam@dot{}\_{\mst@i}={}\_{\mst@i}{}\_{\mst@i}^{{}\_{\mst@i}}{}\_{\mst@i}^{1-{}\_{\mst@i}}, where i is researcher i\mst@varfam@dot{\mst@i}’s total funding and i is their time spent on research. A researcher’s total budget is:=i+i+m​i​nii\mst@varfam@dot{}\_{\mst@i}={}\_{\mst@i}+{}\_{{\mst@m}{\mst@i}{\mst@n}}+{}\_{\mst@i}{}\_{\mst@i}. Given these functional forms, the marginal change in a researchers’ log-output (dln()i\mst@varfam@dot{\mst@d}\ln({}\_{\mst@i})) given a change to their total budget, holding their time spent on research (i) fixed, is: dln()i=diln()i\mst@varfam@dot{\mst@d}\ln({}\_{\mst@i})={}\_{\mst@i}{\mst@d}\ln({}\_{\mst@i}). Next, define a researcher’s share of total funding due to their guarantees as: si⇑ii\mst@varfam@dot{\mst@s}\_{\mst@i}\equiv{}\_{\mst@i}/{}\_{\mst@i}.

This allows us to approximate the marginal change in a researcher’s log-output given a change to their guaranteed funding: dln()isiidln()i\mst@varfam@dot{\mst@d}\ln({}\_{\mst@i})\approx{}\_{\mst@i}{\mst@s}\_{\mst@i}{\mst@d}\ln({}\_{\mst@i}), which holds as an approximation because it keeps si\mst@varfam@dot{\mst@s}\_{\mst@i} fixed to its value before the change. Define a researcher’s share of total budget as: ti⇑i\mst@varfam@dot{\mst@t}\_{\mst@i}\equiv{}\_{\mst@i}/{\mst@B}, and their share of total output under initial allocations as: zi⇑i\mst@varfam@dot{\mst@z}\_{\mst@i}\equiv{}\_{\mst@i}/{\mst@Y}. Thus, the relative change in aggregate budget and aggregate output given a change in each individual researcher’s output are: dln\slimits@itidln()i\mst@varfam@dot{\mst@d}\ln{\mst@B}\approx\tsum\slimits@\_{\mst@i}{\mst@t}\_{\mst@i}{\mst@d}\ln({}\_{\mst@i}) and dln\slimits@izidln()i\mst@varfam@dot{\mst@d}\ln{\mst@Y}\approx\tsum\slimits@\_{\mst@i}{\mst@z}\_{\mst@i}{\mst@d}\ln({}\_{\mst@i}). Combining these last two equations with previous derivations gives us two expressions for the relative change in aggregate budget and in aggregate output given an average relative change in funding guarantees: dln()\slimits@itisidln()i\slimits@itidln()i\mst@varfam@dot{\mst@d}\ln({\mst@B})\approx\tsum\slimits@\_{\mst@i}{\mst@t}\_{\mst@i}{\mst@s}\_{\mst@i}{\mst@d}\ln({}\_{\mst@i})\approx\tsum\slimits@\_{\mst@i}{\mst@t}\_{\mst@i}{\mst@d}\ln({}\_{\mst@i}) and dln()\slimits@izisiidln()i\slimits@izidiln()i\mst@varfam@dot{\mst@d}\ln({\mst@Y})\approx\tsum\slimits@\_{\mst@i}{\mst@z}\_{\mst@i}{}\_{\mst@i}{\mst@s}\_{\mst@i}{\mst@d}\ln({}\_{\mst@i})\approx\tsum\slimits@\_{\mst@i}{\mst@z}\_{\mst@i}{}\_{\mst@i}{\mst@d}\ln({}\_{\mst@i}).

If there is a positive covariance between the dln()i\mst@varfam@dot{\mst@d}\ln({}\_{\mst@i}) and i terms, *then the relative growth in aggregate output () can exceed the relative growth in the total budget ()*. This is what we find in practice. Furthermore, note that the change in aggregate budget never exceeds the change in funding guarantees (dln()i\mst@varfam@dot{\mst@d}\ln({}\_{\mst@i})), because it is a convex combination of individual dln()i\mst@varfam@dot{\mst@d}\ln({}\_{\mst@i}), and the latter never exceed dln()i\mst@varfam@dot{\mst@d}\ln({}\_{\mst@i}) because the weights si\mst@varfam@dot{\mst@s}\_{\mst@i} are smaller than one. In contrast, d​ln​()\mst@varfam@dot{\mst@d}\ln({\mst@Y}) is not a convex combination of variations in individual budget dln()i\mst@varfam@dot{\mst@d}\ln({}\_{\mst@i}), because the sum of zii\mst@varfam@dot{\mst@z}\_{\mst@i}{}\_{\mst@i} weights may exceed one. Therefore, a positive covariance between i and dln()i\mst@varfam@dot{\mst@d}\ln({}\_{\mst@i}) inflates d​ln​()\mst@varfam@dot{\mst@d}\ln({\mst@Y}).