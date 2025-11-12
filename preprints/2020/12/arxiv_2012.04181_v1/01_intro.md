---
authors:
- Hyun Jin Jang
- Kiseop Lee
- Kyungsub Lee
doc_id: arxiv:2012.04181v1
family_id: arxiv:2012.04181
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[2012.04181] Systemic Risk in Market Microstructure of Crude Oil and Gasoline
  Futures Prices: A Hawkes Flocking Model Approach'
url_abs: http://arxiv.org/abs/2012.04181v1
url_html: https://ar5iv.org/html/2012.04181v1
venue: arXiv q-fin
version: 1
year: 2020
---


Hyun Jin Jang
School of Business Administration, Ulsan National Institute of Science and Technology (UNIST), Ulsan, Republic of Korea
  
Kiseop Lee
Department of Statistics, Purdue University, West Lafayette, Indiana, USA
  
Kyungsub Lee
Corresponding author. Department of Statistics, Yeungnam University, Gyeongsan, Republic of Korea (Email:ksublee@yu.ac.kr, Tel:+82-53-810-2324, Fax:+82-53-810-2036)

###### Abstract

We propose the Hawkes flocking model that assesses systemic risk in high-frequency processes at the two perspectives – endogeneity and interactivity.
We examine the futures markets of WTI crude oil and gasoline for the past decade, and perform a comparative analysis with conditional value-at-risk as a benchmark measure.
In terms of high-frequency structure, we derive the empirical findings.
The endogenous systemic risk in WTI was significantly higher than that in gasoline, and the level at which gasoline affects WTI was constantly higher than in the opposite case.
Moreover, although the relative influence’s degree was asymmetric, its difference has gradually reduced.

𝐤𝐞𝐲𝐰𝐨𝐫𝐝𝐤𝐞𝐲𝐰𝐨𝐫𝐝\mathbf{keyword}:
Systemic risk;
Hawkes process;
flocking;
WTI crude oil futures;
gasoline futures;
calibration;
branching ratio;
CoVaR

𝐉𝐄𝐋𝐉𝐄𝐋\mathbf{JEL}: G13, C13

## 1 Introduction

Over the past two decades, the systemic risk level has increased in financial markets due to the growth of securitization, hedge fund markets, and increase in intraday trading.
Recently, the emergence of innovative technologies has accelerated the paradigm shift of trading activities in financial markets.
Traditional trading platforms such as phone conversations or clicks on a screen by humans has moved to automated trading by computers based on the ultra-low latency electronic system.
The increased trading speed enables execution of orders within microseconds by the use of sophisticated algorithms; this is called high-frequency trading.
According to a report of the Commodity Futures Trading Commission (CFTC)111CFTC, “Remarks of Chairman Timothy Massad before the Conference on the Evolving Structure of the US Treasury Market,” October 21, 2015, at <http://www.cftc.gov/PressRoom/SpeechesTestimony/opamassad-30>., the volume of high-frequency trading in futures markets has grown remarkably over the past decade.
It accounts for 80% of foreign exchange futures, 67% of interest rate futures, 62% of equity futures, and 47% of metals and energy futures trading volume.
In addition, flash crash events frequently occur in security markets which are attributed to high-frequency trading222For example, the DJIA index plunged roughly 1,100 points in the first five minutes of trading on August 24, 2015..
Such an environmental change in trading potentially allows large price movements within a short period of time as well as the rapid risk propagation to different assets, as mentioned in Miller and
Shorter ([2016](#bib.bib45)).

In this context of high-frequency finance, we develop a novel Hawkes process-based model to examine the level of systemic risk that exists within and between price dynamics at the microscopic level.
The proposed model allows capturing contagious and clustered phenomena that can be investigated in the excessive volatile and correlated markets.
Studies related to systemic risk in high-frequency trading are discussed under various aspects.
Filimonov and
Sornette ([2012](#bib.bib27)) conduct event studies to investigate the changes in the systemic risk before and after the announcements of two extreme events: downgrading of Greece/Portugal and the flash crash event for the E-mini S&P500 futures in 2010.
Hardiman
et al. ([2013](#bib.bib31)) perform a similar analysis with Filimonov and
Sornette ([2012](#bib.bib27)) by taking power-law kernels.
Chavez-Demoulin
and McGill ([2012](#bib.bib14)) compute intraday value-at-risk (VaR) for stocks in New York Stock Exchange (NYSE) using a peak-over-threshold model, and Jain
et al. ([2016](#bib.bib38)) assess the extent to which a high-frequency system increases systemic risk in the Tokyo Stock Exchange.
Bormetti et al. ([2015](#bib.bib8)) use a multivariate Hawkes process with a common factor that controls a large number of jumps in the transaction movement.
Calcagnile et al. ([2018](#bib.bib11)) compute the number of co-jumps occurring in Russell 3000 index stocks to measure the frequency of the collective instability at high-frequency.

On the other hand, there is little discussion on the increased systemic risk in energy markets associated with high-frequency trading.
However, energy futures markets are no longer exceptional on this matter.
As noted in the beginning, almost the half of the trading volume in the energy markets is raised from high-frequency trading. Moreover,
the CFTC examined how frequently flash events have occurred in the top-five most active futures contracts in 2015, that is, corn, gold, West Texas Intermediate (WTI) crude oil, E-mini S&P 500 futures, and Euro FX333In this research, the flash crash is defined by the episodes in which a contract price moved at least 2% within an hour, but returned to within 0.75% of the original or starting price within that same hour..
Among them, surprisingly, more than 35 similar intraday flash have occurred just for WTI crude oil futures444<https://www.cftc.gov/sites/default/files/idc/groups/public/@newsroom/documents/file/hourlyflashevents102115.pdf>.
This result implies that WTI crude oil futures are utilized actively as instruments of algorithmic trading strategies.

In this study, we attempt to discover empirical evidences of the systemic risk level in the dynamics of the two futures prices of WTI crude oil and gasoline observed at the intraday transaction level over the past decade.
The gasoline futures contracts are being traded most actively in the New York Mercantile Exchange (NYMEX) in the energy sector, following the WTI crude oil futures.
We consider two kinds of definitions for systemic risk in the market microstructure with the instability perspective.
The first view is the degree of instability that exists within a price process.
It is regarded as the term endogeneity, which is introduced in the earlier literature (e.g.,Danielsson
et al., [2012](#bib.bib19); Filimonov and
Sornette, [2012](#bib.bib27); Hardiman
et al., [2013](#bib.bib31)555In Filimonov and
Sornette ([2012](#bib.bib27)) and Hardiman
et al. ([2013](#bib.bib31)), this is referred to “reflexivity” instead of endogeneity).
By estimating this level, we examine whether the trend of price decline leads to additional price decreases (or price rebounds).
The second view is the degree of instability that exists between price processes caused by interaction between two different markets.
In that point of view, we investigate how the change in one price affects to the change in the other price, and vice versa. In addition, we observe how micro-movements of prices in the two markets are likely to close to each other when the price difference widens or narrows.

Meanwhile, WTI crude oil and gasoline futures prices have maintained a strong dependence for a long time (EIA, [2014](#bib.bib21)).
From a macroeconomic perspective, the main causes of the price difference between crude oil and gasoline are refining costs and supply/demand balance of each product.
Such comovement has been studied in terms of market cointegration in econometrics or flocking behavior.
When the two markets are co-integrated or have a flocking feature, the associated prices are closely correlated. Furthermore, one price could lead the other, while the reverse also occurs from time to time, or all prices in a system could follow the same behavior.

Cointegration refers to two or more non-stationary time series that are driven by one or more common non-stationary time series, proposed in the seminal works by Granger ([1981](#bib.bib29)) and Engle and
Granger ([1987](#bib.bib24)).
Many financial data series are known to exhibit the cointegration,
for example, international stock markets (Cerchi and
Havenner, [1988](#bib.bib13); Taylor and
Tonks, [1989](#bib.bib60); Duan and
Pliska, [2004](#bib.bib20)),
foreign exchange rates (Baillie and
Bollerslev, [1989](#bib.bib7); Kellard
et al., [2010](#bib.bib40)),
futures and spot prices (Ng and
Pirrong, [1994](#bib.bib46), [1996](#bib.bib47); Maslyuka and
Smyth, [2009](#bib.bib44)),
especially, crude oil, gasoline, and heating oil futures prices (Serletis, [1992](#bib.bib58); Chiu
et al., [2015](#bib.bib15)).
As a similiar manner, flocking is known to the collective motion of a large number of self-propelled entities. Reynolds ([1987](#bib.bib55)) firstly proposed the breaking-through algorithm that makes it feasible to generate realistic computer simulation of flocking agents.
The flocking behavior appears in many contexts of physics, biology, engineering, and human systems including financial markets
(Rauch
et al., [1995](#bib.bib52); Huepe and
Aldana, [2008](#bib.bib37); Ha
et al., [2015](#bib.bib30); Fang
et al., [2017](#bib.bib25); among many others).
Even though comovement propensity in two or more dynamics has been discussed with different terms of cointegration or flocking in an amount of literature, at our knowledge there is no investigation of such tendency focusing on ‘microstructure’ movements.

Based on the notions of systemic risk and comovement tendency in high-frequency markets, we propose a Hawkes flocking model that enables us to quantify systemic risk embedded in price structures at a microscopic level.
This model addresses how to measure the extent of both endogeneity and interactivity.
By manipulating intensity processes that depend on the relative level of a couple of prices, the proposed model describes a feedback mechanism containing self/mutually-exciting features as well as the flocking behavior.
Moreover, as a direct indicator of systemic risk, we formulate branching ratios, which are generally used in a Hawkes-based model to gauge how many additional jumps occur in the intensity process due to one exogenous event, and is employed for checking out the stability of the process.
For the empirical analysis, we choose the nearest dated futures prices of WTI crude oil and gasoline that are collected at a transaction level in the time period of January 2007 to December 2016.
During this period, prices plunged three times in both markets.

We also compute the systemic risk level by employing an existing methodology, that is, a conditional value-at-risk (CoVaR) approach, as a complementary measure of the proposed model.
The concept of CoVaR is that the maximum loss can happen in an entity within a confidence level due to the effect of large loss from the other entity.
This was firstly proposed by Adrian and
Brunnermeier ([2016](#bib.bib3)) and generalized by Girardi and
Ergun ([2013](#bib.bib28)).
In this study, we adopt the CoVaR defined by Girardi and
Ergun ([2013](#bib.bib28)) and use
a copula method to implement the CoVaR introduced by Reboredo and
Ugolini ([2015](#bib.bib54)).
Then, we simulate the results from the CoVaR method and from the Hawkes flocking model and compare the evolution of systemic risk in the high-frequency markets of WTI crude oil and gasoline, which interplay actively.

The main contribution of this study is twofold.
First, we develop a novel class of Hawkes-based model that assesses two types of systemic risk in high-frequency price processes: the endogenous systemic risk in a single process and interactive systemic risk in a couple of processes.
Second, we examine the existence of the systemic risk at a microscopic level via the futures markets of WTI crude oil and gasoline that are most liquid in the US energy sector.
Through the empirical test based on the proposed model,
we obtain the following results.
The overall systemic risk level that exists in the two futures markets was the highest just before the onset of the global credit crisis.
For the past decade, the level of endogeneity in the WTI market was significantly higher than that in the gasoline market.
In particular, the level at which gasoline price affects WTI price was steadily higher than in the opposite case.
Although the two markets have been interactive, their relative influences, that is, from WTI to gasoline and vice versa, were very asymmetric, but the degree of the difference has been gradually reducing over the study period.

This paper is organized as follows.
In Section [2](#S2 "2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach"), we introduce the Hawkes flocking model and derive branching ratios to check the stability condition of the process.
Section [3](#S3 "3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") presents the intraday transaction data for the two futures prices of WTI crude oil and gasoline from 2007 to 2016 along with estimate results under the proposed model using the maximum likelihood (ML) method.
Section [4](#S4 "4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") presents a comparative analysis between the branching ratios of the proposed model and the CoVaR measure.
Section [5](#S5 "5 Concluding Remark ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") concludes the paper, and
technical proofs and additional figures/tables are presented in the Appendix.

## 2 The Hawkes Flocking Model

In this section, we develop the Hawkes flocking model. The proposed model can be categorized to generalized Hawkes processes, which is introduced in the serial papers (Hawkes, [1971a](#bib.bib32); Hawkes, [1971b](#bib.bib33); Hawkes and
Oakes, [1974](#bib.bib34)).
As the Hawkes process is based on a class of multivariate counting processes, this model can account for the interaction of various types of Poisson-like events through its intensity process.

Because of their great flexibility and versatility, Hawkes-based models are very popular for modeling high-frequency finance.
As a pioneering work, Bowsher ([2007](#bib.bib9)) introduce a bivariate Hawkes processes to model the joint dynamics of trades and mid-price changes in NYSE stocks.
After that, many studies related to high-frequency finance have employed Hawkes processes (Bacry
et al., [2012](#bib.bib4); Bacry
et al., [2013](#bib.bib5); Da Fonseca and
Zaatour, [2014](#bib.bib17); Bacry
et al., [2015](#bib.bib6); Lee and Seo, [2017](#bib.bib42)).

### 2.1 Model specification

As noted in the introduction,
the model we propose captures the interaction between two highly correlated processes observed at the level of transaction data.
Consider the bivariate price processes that are defined by the differences between the two counting processes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C1​(t)subscript𝐶1𝑡\displaystyle C\_{1}(t) | =δ1​(N1u​(t)−N1d​(t))absentsubscript𝛿1superscriptsubscript𝑁1𝑢𝑡superscriptsubscript𝑁1𝑑𝑡\displaystyle=\delta\_{1}(N\_{1}^{u}(t)-N\_{1}^{d}(t)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | C2​(t)subscript𝐶2𝑡\displaystyle C\_{2}(t) | =δ2​(N2u​(t)−N2d​(t))absentsubscript𝛿2superscriptsubscript𝑁2𝑢𝑡superscriptsubscript𝑁2𝑑𝑡\displaystyle=\delta\_{2}(N\_{2}^{u}(t)-N\_{2}^{d}(t)) |  |

where processes Niu​(t)superscriptsubscript𝑁𝑖𝑢𝑡N\_{i}^{u}(t) and Nid​(t)superscriptsubscript𝑁𝑖𝑑𝑡N\_{i}^{d}(t) count the number of events for upward and downward movement in price Ci​(t)subscript𝐶𝑖𝑡C\_{i}(t) up to time t𝑡t, respectively, and δisubscript𝛿𝑖\delta\_{i} are tick sizes.

We present a system of the counting process 𝑵𝑵\bm{N} and its intensity process 𝝀𝝀\bm{\lambda} by employing the following matrix form

|  |  |  |
| --- | --- | --- |
|  | 𝑵t=[N1u​(t)N1d​(t)N2u​(t)N2d​(t)],𝝀t=[λ1u​(t)λ1d​(t)λ2u​(t)λ2d​(t)]formulae-sequencesubscript𝑵𝑡matrixsuperscriptsubscript𝑁1𝑢𝑡superscriptsubscript𝑁1𝑑𝑡superscriptsubscript𝑁2𝑢𝑡superscriptsubscript𝑁2𝑑𝑡subscript𝝀𝑡matrixsuperscriptsubscript𝜆1𝑢𝑡superscriptsubscript𝜆1𝑑𝑡superscriptsubscript𝜆2𝑢𝑡superscriptsubscript𝜆2𝑑𝑡\bm{N}\_{t}=\begin{bmatrix}N\_{1}^{u}(t)\\ N\_{1}^{d}(t)\\ N\_{2}^{u}(t)\\ N\_{2}^{d}(t)\end{bmatrix},\quad\bm{\lambda}\_{t}=\begin{bmatrix}\lambda\_{1}^{u}(t)\\ \lambda\_{1}^{d}(t)\\ \lambda\_{2}^{u}(t)\\ \lambda\_{2}^{d}(t)\end{bmatrix} |  |

where intensity process 𝝀𝝀\bm{\lambda} represents the expected number of arrivals of counting events over an infinitesimal time interval d​td𝑡\mathrm{d}t divided by d​td𝑡\mathrm{d}t.
Let the intensity process be

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝀t=𝝁+∫−∞t𝒉​(t−u)​d𝑵usubscript𝝀𝑡𝝁superscriptsubscript𝑡𝒉𝑡𝑢differential-dsubscript𝑵𝑢\bm{\lambda}\_{t}=\bm{\mu}+\int\_{-\infty}^{t}\bm{h}(t-u)\mathrm{d}\bm{N}\_{u} |  | (1) |

where 𝝁=[μ1,μ1,μ2,μ2]⊤𝝁superscript

subscript𝜇1subscript𝜇1subscript𝜇2subscript𝜇2
top\bm{\mu}=[\mu\_{1},\mu\_{1},\mu\_{2},\mu\_{2}]^{\top} is a constant vector, and 𝒉𝒉\bm{h} is a four-by-four matrix.
Here, the vector 𝝁𝝁\bm{\mu} is called base intensity that accounts for the average frequency of exogenous events coming into this system, which is independent of the other asset’s movement as well as its past movement.
Parameters μ1subscript𝜇1\mu\_{1} and μ2subscript𝜇2\mu\_{2} are interpreted as the pressure of orders for buying or selling at price C1subscript𝐶1C\_{1} and C2subscript𝐶2C\_{2}, respectively.
The matrix 𝒉𝒉\bm{h} is called a feedback kernel of the Hawkes process that decides the weight to be attributed to events d​𝑵d𝑵\mathrm{d}\bm{N} occurring at lag u𝑢u in the past.

We set the feedback kernel by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒉​(t−u)=Φ​(t−u)+k​(t)∘Ψ​(t−u)𝒉𝑡𝑢Φ𝑡𝑢𝑘𝑡Ψ𝑡𝑢\bm{h}(t-u)=\Phi(t-u)+{k}(t)\circ\Psi(t-u) |  | (2) |

where Φ,k

Φ𝑘\Phi,{k}, and ΨΨ\Psi are four-by-four matrices, and “∘\circ” denotes the element-wise multiplication of matrices.
The kernel 𝒉𝒉\bm{h} consists of two components:

1. (i)

   The matrix ΦΦ\Phi controls the self/mutually-exciting patterns between the two prices, which is defined as

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Φ​(t)=[α1​s​e−β1​tα1​c​e−β1​t00α1​c​e−β1​tα1​s​e−β1​t0000α2​s​e−β2​tα2​c​e−β2​t00α2​c​e−β2​tα2​s​e−β2​t]Φ𝑡matrixsubscript𝛼1𝑠superscriptesubscript𝛽1𝑡subscript𝛼1𝑐superscriptesubscript𝛽1𝑡00subscript𝛼1𝑐superscriptesubscript𝛽1𝑡subscript𝛼1𝑠superscriptesubscript𝛽1𝑡0000subscript𝛼2𝑠superscriptesubscript𝛽2𝑡subscript𝛼2𝑐superscriptesubscript𝛽2𝑡00subscript𝛼2𝑐superscriptesubscript𝛽2𝑡subscript𝛼2𝑠superscriptesubscript𝛽2𝑡\Phi(t)=\begin{bmatrix}\alpha\_{1s}\mathrm{e}^{-\beta\_{1}t}&\alpha\_{1c}\mathrm{e}^{-\beta\_{1}t}&0&0\\ \alpha\_{1c}\mathrm{e}^{-\beta\_{1}t}&\alpha\_{1s}\mathrm{e}^{-\beta\_{1}t}&0&0\\ 0&0&\alpha\_{2s}\mathrm{e}^{-\beta\_{2}t}&\alpha\_{2c}\mathrm{e}^{-\beta\_{2}t}\\ 0&0&\alpha\_{2c}\mathrm{e}^{-\beta\_{2}t}&\alpha\_{2s}\mathrm{e}^{-\beta\_{2}t}\end{bmatrix} |  | (3) |

   where non-negative constants αi​ssubscript𝛼𝑖𝑠\alpha\_{is} and αi​csubscript𝛼𝑖𝑐\alpha\_{ic} denote the self/mutually-exciting terms, respectively,
   and βisubscript𝛽𝑖\beta\_{i} governs the speed of decay to the base intensity level of the i𝑖i-th price process.
2. (ii)

   The matrix k∘Ψ𝑘Ψ{k}\circ\Psi controls the flocking phenomenon according to which two price movements interact, and where
   matrix k𝑘{k} is defined by an indicator function matrix such as

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | k​(t)=[𝟙{C1​(t)<C2​(t)}𝟙{C1​(t)<C2​(t)}𝟙{C1​(t)<C2​(t)}𝟙{C1​(t)<C2​(t)}𝟙{C1​(t)>C2​(t)}𝟙{C1​(t)>C2​(t)}𝟙{C1​(t)>C2​(t)}𝟙{C1​(t)>C2​(t)}𝟙{C2​(t)<C1​(t)}𝟙{C2​(t)<C1​(t)}𝟙{C2​(t)<C1​(t)}𝟙{C2​(t)<C1​(t)}𝟙{C2​(t)>C1​(t)}𝟙{C2​(t)>C1​(t)}𝟙{C2​(t)>C1​(t)}𝟙{C2​(t)>C1​(t)}],𝑘𝑡matrixsubscript1subscript𝐶1𝑡subscript𝐶2𝑡subscript1subscript𝐶1𝑡subscript𝐶2𝑡subscript1subscript𝐶1𝑡subscript𝐶2𝑡subscript1subscript𝐶1𝑡subscript𝐶2𝑡subscript1subscript𝐶1𝑡subscript𝐶2𝑡subscript1subscript𝐶1𝑡subscript𝐶2𝑡subscript1subscript𝐶1𝑡subscript𝐶2𝑡subscript1subscript𝐶1𝑡subscript𝐶2𝑡subscript1subscript𝐶2𝑡subscript𝐶1𝑡subscript1subscript𝐶2𝑡subscript𝐶1𝑡subscript1subscript𝐶2𝑡subscript𝐶1𝑡subscript1subscript𝐶2𝑡subscript𝐶1𝑡subscript1subscript𝐶2𝑡subscript𝐶1𝑡subscript1subscript𝐶2𝑡subscript𝐶1𝑡subscript1subscript𝐶2𝑡subscript𝐶1𝑡subscript1subscript𝐶2𝑡subscript𝐶1𝑡{k}(t)=\begin{bmatrix}\mathbbm{1}\_{\{C\_{1}(t)<C\_{2}(t)\}}&\mathbbm{1}\_{\{C\_{1}(t)<C\_{2}(t)\}}&\mathbbm{1}\_{\{C\_{1}(t)<C\_{2}(t)\}}&\mathbbm{1}\_{\{C\_{1}(t)<C\_{2}(t)\}}\\ \mathbbm{1}\_{\{C\_{1}(t)>C\_{2}(t)\}}&\mathbbm{1}\_{\{C\_{1}(t)>C\_{2}(t)\}}&\mathbbm{1}\_{\{C\_{1}(t)>C\_{2}(t)\}}&\mathbbm{1}\_{\{C\_{1}(t)>C\_{2}(t)\}}\\ \mathbbm{1}\_{\{C\_{2}(t)<C\_{1}(t)\}}&\mathbbm{1}\_{\{C\_{2}(t)<C\_{1}(t)\}}&\mathbbm{1}\_{\{C\_{2}(t)<C\_{1}(t)\}}&\mathbbm{1}\_{\{C\_{2}(t)<C\_{1}(t)\}}\\ \mathbbm{1}\_{\{C\_{2}(t)>C\_{1}(t)\}}&\mathbbm{1}\_{\{C\_{2}(t)>C\_{1}(t)\}}&\mathbbm{1}\_{\{C\_{2}(t)>C\_{1}(t)\}}&\mathbbm{1}\_{\{C\_{2}(t)>C\_{1}(t)\}}\end{bmatrix}, |  | (4) |

   and the matrix Ψ​(t)Ψ𝑡\Psi(t) is defined by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Ψ​(t)=[00α1​w​e−β1​tα1​n​e−β1​t00α1​n​e−β1​tα1​w​e−β1​tα2​w​e−β2​tα2​n​e−β2​t00α2​n​e−β2​tα2​w​e−β2​t00]Ψ𝑡matrix00subscript𝛼1𝑤superscriptesubscript𝛽1𝑡subscript𝛼1𝑛superscriptesubscript𝛽1𝑡00subscript𝛼1𝑛superscriptesubscript𝛽1𝑡subscript𝛼1𝑤superscriptesubscript𝛽1𝑡subscript𝛼2𝑤superscriptesubscript𝛽2𝑡subscript𝛼2𝑛superscriptesubscript𝛽2𝑡00subscript𝛼2𝑛superscriptesubscript𝛽2𝑡subscript𝛼2𝑤superscriptesubscript𝛽2𝑡00\Psi(t)=\begin{bmatrix}0&0&\alpha\_{1w}\mathrm{e}^{-\beta\_{1}t}&\alpha\_{1n}\mathrm{e}^{-\beta\_{1}t}\\ 0&0&\alpha\_{1n}\mathrm{e}^{-\beta\_{1}t}&\alpha\_{1w}\mathrm{e}^{-\beta\_{1}t}\\ \alpha\_{2w}\mathrm{e}^{-\beta\_{2}t}&\alpha\_{2n}\mathrm{e}^{-\beta\_{2}t}&0&0\\ \alpha\_{2n}\mathrm{e}^{-\beta\_{2}t}&\alpha\_{2w}\mathrm{e}^{-\beta\_{2}t}&0&0\end{bmatrix} |  | (5) |

   where non-negative constants αi​wsubscript𝛼𝑖𝑤\alpha\_{iw} and αi​nsubscript𝛼𝑖𝑛\alpha\_{in} denote the flocking exciting terms.

In part (i), the exponential decaying setup in the bivariate Hawkes process with symmetric α𝛼\alpha’s shows a prototypical model for high-frequency finance.
In part (ii), k𝑘k deals with the flocking phenomenon while considering an additional term under which intensity λ1usuperscriptsubscript𝜆1𝑢\lambda\_{1}^{u} increases only when C1subscript𝐶1C\_{1} is less than C2subscript𝐶2C\_{2}
and λ1dsuperscriptsubscript𝜆1𝑑\lambda\_{1}^{d} increases only when C1subscript𝐶1C\_{1} is larger than C2subscript𝐶2C\_{2}.
ΨΨ\Psi captures the degree of a flocking phenomenon.
The parameter αi​wsubscript𝛼𝑖𝑤\alpha\_{iw} or αi​nsubscript𝛼𝑖𝑛\alpha\_{in} is triggered depending on whether the difference between the two prices is narrowed (n𝑛n) or widened (w𝑤w).

Figure [1](#S2.F1 "Figure 1 ‣ 2.1 Model specification ‣ 2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") shows a descriptive idea on the intensity movements in a Hawkes flocking model.
In this figure, the paths represent the dynamics of two prices and the associated four intensities666This is for an illustrative purpose and the actual values of prices and intensities may be different from the figure..
The black straight line is for price movement C1subscript𝐶1C\_{1}. The black curved line and curved dashed line represent the intensities for upward and downward movement, respectively.
Accordingly, the red lines are for price C2subscript𝐶2C\_{2} and its intensities.

Assume C1>C2subscript𝐶1subscript𝐶2C\_{1}>C\_{2}.
Suppose that a widening upward jump of C1subscript𝐶1C\_{1} occurs. Then, three simultaneous jumps in intensities are instantly activated, λ1usuperscriptsubscript𝜆1𝑢\lambda\_{1}^{u}, λ1dsuperscriptsubscript𝜆1𝑑\lambda\_{1}^{d} and λ2usuperscriptsubscript𝜆2𝑢\lambda\_{2}^{u}.
The jumps in λ1usuperscriptsubscript𝜆1𝑢\lambda\_{1}^{u} and λ1dsuperscriptsubscript𝜆1𝑑\lambda\_{1}^{d} are due to self/mutually-exciting tendency in the individual Hawkes model and jump sizes are given by α1​ssubscript𝛼1𝑠\alpha\_{1s} and α1​csubscript𝛼1𝑐\alpha\_{1c}, respectively.
The jump in λ2usuperscriptsubscript𝜆2𝑢\lambda\_{2}^{u} is due to the flocking feature to accelerate a upward movement of C2subscript𝐶2C\_{2} resulting from the jump in C1subscript𝐶1C\_{1}
and a jump size is given as α2​wsubscript𝛼2𝑤\alpha\_{2w}.

Later on, a narrowing upward movement of C2subscript𝐶2C\_{2} occurs. In a similar way, simultaneous jumps arrive in intensities, λ2usuperscriptsubscript𝜆2𝑢\lambda\_{2}^{u}, λ2usuperscriptsubscript𝜆2𝑢\lambda\_{2}^{u} and λ1dsuperscriptsubscript𝜆1𝑑\lambda\_{1}^{d}.
The jumps in λ2usuperscriptsubscript𝜆2𝑢\lambda\_{2}^{u} and λ2dsuperscriptsubscript𝜆2𝑑\lambda\_{2}^{d} are due to self/mutually-exciting propensity,
and the jump in λ1dsuperscriptsubscript𝜆1𝑑\lambda\_{1}^{d} is due to the flocking mechanism attributed to a narrowing event.
Note that jump sizes of λ1dsuperscriptsubscript𝜆1𝑑\lambda\_{1}^{d} and α1​nsubscript𝛼1𝑛\alpha\_{1n}, are intentionally expressed as quite small in the figure,
since the jumps in intensities due to the narrowing event are close to zero in the empirical analysis.

![Refer to caption](/html/2012.04181/assets/x1.png)


Figure 1: Illustration of the idea on the Hawkes flocking model

###### Remark 1 (The role of k𝑘k).

We simply put Φi​j=0subscriptΦ𝑖𝑗0\Phi\_{ij}=0 and Ψi​j=1subscriptΨ𝑖𝑗1\Psi\_{ij}=1 for all i,j

𝑖𝑗i,j.
Then

|  |  |  |
| --- | --- | --- |
|  | λ1u​(t)=μ1+∫−∞t𝟙{C1​(u)<C2​(u)}​d​(N1u+N1d+N2u+N2d)​(u)superscriptsubscript𝜆1𝑢𝑡subscript𝜇1superscriptsubscript𝑡subscript1subscript𝐶1𝑢subscript𝐶2𝑢dsuperscriptsubscript𝑁1𝑢superscriptsubscript𝑁1𝑑superscriptsubscript𝑁2𝑢superscriptsubscript𝑁2𝑑𝑢\lambda\_{1}^{u}(t)=\mu\_{1}+\int\_{-\infty}^{t}\mathbbm{1}\_{\{C\_{1}(u)<C\_{2}(u)\}}\mathrm{d}\left(N\_{1}^{u}+N\_{1}^{d}+N\_{2}^{u}+N\_{2}^{d}\right)(u) |  |

and this implies that the intensity of the up movement of C1subscript𝐶1C\_{1} changes (typically increases) when C1​(t)subscript𝐶1𝑡C\_{1}(t) is less than C2​(t)subscript𝐶2𝑡C\_{2}(t).

When C1​(t)<C2​(t)subscript𝐶1𝑡subscript𝐶2𝑡C\_{1}(t)<C\_{2}(t), the intensity of the up movement of C1subscript𝐶1C\_{1} increases, and C1subscript𝐶1C\_{1} and C2subscript𝐶2C\_{2} tend to be close to each other, indicating a flocking phenomenon.
With similar arguments, when C1​(t)<C2​(t)subscript𝐶1𝑡subscript𝐶2𝑡C\_{1}(t)<C\_{2}(t),
the up movement of C1subscript𝐶1C\_{1} and down movement of C2subscript𝐶2C\_{2} tend to increase and
when C1​(t)>C2​(t)subscript𝐶1𝑡subscript𝐶2𝑡C\_{1}(t)>C\_{2}(t),
the down movement of C1subscript𝐶1C\_{1} and up movement of C2subscript𝐶2C\_{2} tend to increase.

###### Remark 2 (Comparison between ΦΦ\Phi and ΨΨ\Psi).

The matrices ΦΦ\Phi and ΨΨ\Psi have zero components in positions that do not overlap each other.
This ensures each role of the matrix is separated:
ΦΦ\Phi only affects the movements in the individual price process,
and ΨΨ\Psi only controls the effect of the new information from another prices process.
Therefore, the test of the significance of ΨΨ\Psi verifies the existence of interactions between the two prices, especially through the sign of C1−C2subscript𝐶1subscript𝐶2C\_{1}-C\_{2}.

Through combination with k𝑘{k}, αi​nsubscript𝛼𝑖𝑛\alpha\_{in}, and αi​wsubscript𝛼𝑖𝑤\alpha\_{iw} respectively represent the effects of the narrowing and widening events of price difference on intensities.
To see this, we simply put Φi​j=0subscriptΦ𝑖𝑗0\Phi\_{ij}=0, and then

|  |  |  |
| --- | --- | --- |
|  | λ1u​(t)=μ1+∫−∞t𝟙{C1​(u)<C2​(u)}​e−β1​(t−u)​(α1​w​d​N2u​(u)+α1​n​d​N2d​(u)).superscriptsubscript𝜆1𝑢𝑡subscript𝜇1superscriptsubscript𝑡subscript1subscript𝐶1𝑢subscript𝐶2𝑢superscriptesubscript𝛽1𝑡𝑢subscript𝛼1𝑤dsuperscriptsubscript𝑁2𝑢𝑢subscript𝛼1𝑛dsuperscriptsubscript𝑁2𝑑𝑢\lambda\_{1}^{u}(t)=\mu\_{1}+\int\_{-\infty}^{t}\mathbbm{1}\_{\{C\_{1}(u)<C\_{2}(u)\}}\mathrm{e}^{-\beta\_{1}(t-u)}\left(\alpha\_{1w}\mathrm{d}N\_{2}^{u}(u)+\alpha\_{1n}\mathrm{d}N\_{2}^{d}(u)\right). |  |

When C1​(u)<C2​(u)subscript𝐶1𝑢subscript𝐶2𝑢C\_{1}(u)<C\_{2}(u), the increase of N2u​(u)superscriptsubscript𝑁2𝑢𝑢N\_{2}^{u}(u) is the price difference widening event, and
the occurrence of N2dsuperscriptsubscript𝑁2𝑑N\_{2}^{d} is the price difference narrowing event.

From the setup for the components in the kernel matrix 𝒉𝒉\bm{h},
the proposed model can be expressed with a differential form using a Markov property.
Let the decay parameter for C1subscript𝐶1C\_{1} and C2subscript𝐶2C\_{2} be fixed as β1subscript𝛽1\beta\_{1} and β2subscript𝛽2\beta\_{2}, respectively.
Then, the intensity process satisfies the system of stochastic differential equations such as

|  |  |  |
| --- | --- | --- |
|  | d​𝝀t=𝜷∘(𝝁−𝝀t)​d​t+𝜶​d​𝑵tdsubscript𝝀𝑡𝜷𝝁subscript𝝀𝑡d𝑡𝜶dsubscript𝑵𝑡\mathrm{d}\bm{\lambda}\_{t}=\bm{\beta}\circ(\bm{\mu}-\bm{\lambda}\_{t})\mathrm{d}t+\bm{\alpha}\mathrm{d}\bm{N}\_{t} |  |

where 𝜶𝜶\bm{\alpha} and 𝜷𝜷\bm{\beta} are given as

|  |  |  |
| --- | --- | --- |
|  | 𝜶=[α1​sα1​c𝟙{C1​(t)<C2​(t)}​α1​w𝟙{C1​(t)<C2​(t)}​α1​nα1​cα1​s𝟙{C1​(t)>C2​(t)}​α1​n𝟙{C1​(t)>C2​(t)}​α1​w𝟙{C2​(t)<C1​(t)}​α2​w𝟙{C2​(t)<C1​(t)}​α2​nα2​sα2​c𝟙{C2​(t)>C1​(t)}​α2​n𝟙{C2​(t)>C1​(t)}​α2​wα2​cα2​s],𝜷=[β1β1β2β2].formulae-sequence𝜶matrixsubscript𝛼1𝑠subscript𝛼1𝑐subscript1subscript𝐶1𝑡subscript𝐶2𝑡subscript𝛼1𝑤subscript1subscript𝐶1𝑡subscript𝐶2𝑡subscript𝛼1𝑛subscript𝛼1𝑐subscript𝛼1𝑠subscript1subscript𝐶1𝑡subscript𝐶2𝑡subscript𝛼1𝑛subscript1subscript𝐶1𝑡subscript𝐶2𝑡subscript𝛼1𝑤subscript1subscript𝐶2𝑡subscript𝐶1𝑡subscript𝛼2𝑤subscript1subscript𝐶2𝑡subscript𝐶1𝑡subscript𝛼2𝑛subscript𝛼2𝑠subscript𝛼2𝑐subscript1subscript𝐶2𝑡subscript𝐶1𝑡subscript𝛼2𝑛subscript1subscript𝐶2𝑡subscript𝐶1𝑡subscript𝛼2𝑤subscript𝛼2𝑐subscript𝛼2𝑠𝜷matrixsubscript𝛽1subscript𝛽1subscript𝛽2subscript𝛽2\displaystyle\bm{\alpha}=\begin{bmatrix}\alpha\_{1s}&\alpha\_{1c}&\mathbbm{1}\_{\{C\_{1}(t)<C\_{2}(t)\}}\alpha\_{1w}&\mathbbm{1}\_{\{C\_{1}(t)<C\_{2}(t)\}}\alpha\_{1n}\\ \alpha\_{1c}&\alpha\_{1s}&\mathbbm{1}\_{\{C\_{1}(t)>C\_{2}(t)\}}\alpha\_{1n}&\mathbbm{1}\_{\{C\_{1}(t)>C\_{2}(t)\}}\alpha\_{1w}\\ \mathbbm{1}\_{\{C\_{2}(t)<C\_{1}(t)\}}\alpha\_{2w}&\mathbbm{1}\_{\{C\_{2}(t)<C\_{1}(t)\}}\alpha\_{2n}&\alpha\_{2s}&\alpha\_{2c}\\ \mathbbm{1}\_{\{C\_{2}(t)>C\_{1}(t)\}}\alpha\_{2n}&\mathbbm{1}\_{\{C\_{2}(t)>C\_{1}(t)\}}\alpha\_{2w}&\alpha\_{2c}&\alpha\_{2s}\end{bmatrix},\quad\bm{\beta}=\begin{bmatrix}\beta\_{1}\\ \beta\_{1}\\ \beta\_{2}\\ \beta\_{2}\end{bmatrix}. |  |

This model can be understood as follows. Market orders (buy or sell) arrive with intensity 𝝁𝝁\bm{\mu}, and the arrival intensity jumps by the amount of 𝜶𝜶\bm{\alpha} instantly when an arrival event occurs, and then it decays to the base intensity level 𝝁𝝁\bm{\mu} with the speed of 𝜷𝜷\bm{\beta}.

This model can be extended to the multi-dimensional case as the Remark [3](#Thmtheorem3 "Remark 3. ‣ 2.1 Model specification ‣ 2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") shows.

###### Remark 3.

(The multi-dimensional Hawkes flocking model)
Consider m𝑚m-dimensional price processes such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | C1​(t)=N1u​(t)−N1d​(t),⋯,Cm​(t)=Nmu​(t)−Nmd​(t),formulae-sequencesubscript𝐶1𝑡  superscriptsubscript𝑁1𝑢𝑡superscriptsubscript𝑁1𝑑𝑡⋯subscript𝐶𝑚𝑡superscriptsubscript𝑁𝑚𝑢𝑡superscriptsubscript𝑁𝑚𝑑𝑡C\_{1}(t)=N\_{1}^{u}(t)-N\_{1}^{d}(t),\,\,\,\cdots,\,\,\,C\_{m}(t)=N\_{m}^{u}(t)-N\_{m}^{d}(t), |  | (6) |

where processes Niu​(t)superscriptsubscript𝑁𝑖𝑢𝑡N\_{i}^{u}(t) and Nid​(t)superscriptsubscript𝑁𝑖𝑑𝑡N\_{i}^{d}(t) have intensity processes λiu​(t)superscriptsubscript𝜆𝑖𝑢𝑡\lambda\_{i}^{u}(t) and λid​(t)superscriptsubscript𝜆𝑖𝑑𝑡\lambda\_{i}^{d}(t), respectively, for each i=1,⋯,m𝑖

1⋯𝑚i=1,\cdots,m.
For a system of 2​m2𝑚2m-dimensional counting process 𝑵𝑵\bm{N} and its intensity process 𝝀𝝀\bm{\lambda}

|  |  |  |
| --- | --- | --- |
|  | 𝑵t=[N1u​(t)N1d​(t)⋮Nmu​(t)Nmd​(t)],𝝀t=[λ1u​(t)λ1d​(t)⋮λmu​(t)λmd​(t)]formulae-sequencesubscript𝑵𝑡matrixsuperscriptsubscript𝑁1𝑢𝑡superscriptsubscript𝑁1𝑑𝑡⋮superscriptsubscript𝑁𝑚𝑢𝑡superscriptsubscript𝑁𝑚𝑑𝑡subscript𝝀𝑡matrixsuperscriptsubscript𝜆1𝑢𝑡superscriptsubscript𝜆1𝑑𝑡⋮superscriptsubscript𝜆𝑚𝑢𝑡superscriptsubscript𝜆𝑚𝑑𝑡\bm{N}\_{t}=\begin{bmatrix}N\_{1}^{u}(t)\\ N\_{1}^{d}(t)\\ \vdots\\ N\_{m}^{u}(t)\\ N\_{m}^{d}(t)\end{bmatrix},\quad\bm{\lambda}\_{t}=\begin{bmatrix}\lambda\_{1}^{u}(t)\\ \lambda\_{1}^{d}(t)\\ \vdots\\ \lambda\_{m}^{u}(t)\\ \lambda\_{m}^{d}(t)\end{bmatrix} |  |

we can extend the intensity process in ([1](#S2.E1 "In 2.1 Model specification ‣ 2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) with the feedback kernel in ([2](#S2.E2 "In 2.1 Model specification ‣ 2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) to the multi-dimensional version as follows.

1. (i)

   The matrix ΦΦ\Phi in ([3](#S2.E3 "In item (i) ‣ 2.1 Model specification ‣ 2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) is given as the 2​m2𝑚2m-by-2​m2𝑚2m sized form,

   |  |  |  |
   | --- | --- | --- |
   |  | Φ​(t)=[α1​s​e−β1​tα1​c​e−β1​t⋯00α1​c​e−β1​tα1​s​e−β1​t⋯00⋯⋯⋯⋯⋯00⋯αm​s​e−βm​tαm​c​e−βm​t00⋯αm​c​e−βm​tαm​s​e−βm​t]Φ𝑡matrixsubscript𝛼1𝑠superscriptesubscript𝛽1𝑡subscript𝛼1𝑐superscriptesubscript𝛽1𝑡⋯00subscript𝛼1𝑐superscriptesubscript𝛽1𝑡subscript𝛼1𝑠superscriptesubscript𝛽1𝑡⋯00⋯⋯⋯⋯⋯00⋯subscript𝛼𝑚𝑠superscriptesubscript𝛽𝑚𝑡subscript𝛼𝑚𝑐superscriptesubscript𝛽𝑚𝑡00⋯subscript𝛼𝑚𝑐superscriptesubscript𝛽𝑚𝑡subscript𝛼𝑚𝑠superscriptesubscript𝛽𝑚𝑡\Phi(t)=\begin{bmatrix}\alpha\_{1s}\mathrm{e}^{-\beta\_{1}t}&\alpha\_{1c}\mathrm{e}^{-\beta\_{1}t}&\cdots&0&0\\ \alpha\_{1c}\mathrm{e}^{-\beta\_{1}t}&\alpha\_{1s}\mathrm{e}^{-\beta\_{1}t}&\cdots&0&0\\ \cdots&\cdots&\cdots&\cdots&\cdots\\ 0&0&\cdots&\alpha\_{ms}\mathrm{e}^{-\beta\_{m}t}&\alpha\_{mc}\mathrm{e}^{-\beta\_{m}t}\\ 0&0&\cdots&\alpha\_{mc}\mathrm{e}^{-\beta\_{m}t}&\alpha\_{ms}\mathrm{e}^{-\beta\_{m}t}\end{bmatrix} |  |
2. (ii)

   The matrix k∘Ψ𝑘Ψ{k}\circ\Psi in ([4](#S2.E4 "In item (ii) ‣ 2.1 Model specification ‣ 2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) and ([5](#S2.E5 "In item (ii) ‣ 2.1 Model specification ‣ 2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) is also given as the 2​m2𝑚2m-by-2​m2𝑚2m sized form such that

   |  |  |  |
   | --- | --- | --- |
   |  | k​(t)=[𝟙{C1​(t)<C¯​(t)}𝟙{C1​(t)<C¯​(t)}⋯𝟙{C1​(t)<C¯​(t)}𝟙{C1​(t)<C¯​(t)}𝟙{C1​(t)>C¯​(t)}𝟙{C1​(t)>C¯​(t)}⋯𝟙{C1​(t)>C¯​(t)}𝟙{C1​(t)>C¯​(t)}⋯⋯⋯⋯⋯𝟙{Cm​(t)<C¯​(t)}𝟙{Cm​(t)<C¯​(t)}⋯𝟙{Cm​(t)<C¯​(t)}𝟙{Cm​(t)<C¯​(t)}𝟙{Cm​(t)>C¯​(t)}𝟙{Cm​(t)>C¯​(t)}⋯𝟙{Cm​(t)>C¯​(t)}𝟙{Cm​(t)>C¯​(t)}],𝑘𝑡matrixsubscript1subscript𝐶1𝑡¯𝐶𝑡subscript1subscript𝐶1𝑡¯𝐶𝑡⋯subscript1subscript𝐶1𝑡¯𝐶𝑡subscript1subscript𝐶1𝑡¯𝐶𝑡subscript1subscript𝐶1𝑡¯𝐶𝑡subscript1subscript𝐶1𝑡¯𝐶𝑡⋯subscript1subscript𝐶1𝑡¯𝐶𝑡subscript1subscript𝐶1𝑡¯𝐶𝑡⋯⋯⋯⋯⋯subscript1subscript𝐶𝑚𝑡¯𝐶𝑡subscript1subscript𝐶𝑚𝑡¯𝐶𝑡⋯subscript1subscript𝐶𝑚𝑡¯𝐶𝑡subscript1subscript𝐶𝑚𝑡¯𝐶𝑡subscript1subscript𝐶𝑚𝑡¯𝐶𝑡subscript1subscript𝐶𝑚𝑡¯𝐶𝑡⋯subscript1subscript𝐶𝑚𝑡¯𝐶𝑡subscript1subscript𝐶𝑚𝑡¯𝐶𝑡{k}(t)=\begin{bmatrix}\mathbbm{1}\_{\{C\_{1}(t)<\bar{C}(t)\}}&\mathbbm{1}\_{\{C\_{1}(t)<\bar{C}(t)\}}&\cdots&\mathbbm{1}\_{\{C\_{1}(t)<\bar{C}(t)\}}&\mathbbm{1}\_{\{C\_{1}(t)<\bar{C}(t)\}}\\ \mathbbm{1}\_{\{C\_{1}(t)>\bar{C}(t)\}}&\mathbbm{1}\_{\{C\_{1}(t)>\bar{C}(t)\}}&\cdots&\mathbbm{1}\_{\{C\_{1}(t)>\bar{C}(t)\}}&\mathbbm{1}\_{\{C\_{1}(t)>\bar{C}(t)\}}\\ \cdots&\cdots&\cdots&\cdots&\cdots\\ \mathbbm{1}\_{\{C\_{m}(t)<\bar{C}(t)\}}&\mathbbm{1}\_{\{C\_{m}(t)<\bar{C}(t)\}}&\cdots&\mathbbm{1}\_{\{C\_{m}(t)<\bar{C}(t)\}}&\mathbbm{1}\_{\{C\_{m}(t)<\bar{C}(t)\}}\\ \mathbbm{1}\_{\{C\_{m}(t)>\bar{C}(t)\}}&\mathbbm{1}\_{\{C\_{m}(t)>\bar{C}(t)\}}&\cdots&\mathbbm{1}\_{\{C\_{m}(t)>\bar{C}(t)\}}&\mathbbm{1}\_{\{C\_{m}(t)>\bar{C}(t)\}}\end{bmatrix}, |  |

   where C¯​(t)¯𝐶𝑡\bar{C}(t) is given as the average of Ci​(t)subscript𝐶𝑖𝑡C\_{i}(t)’s such as

   |  |  |  |
   | --- | --- | --- |
   |  | C¯​(t)=C1​(t)+⋯+Cm​(t)m,¯𝐶𝑡subscript𝐶1𝑡⋯subscript𝐶𝑚𝑡𝑚\bar{C}(t)=\frac{C\_{1}(t)+\cdots+C\_{m}(t)}{m}, |  |

   and

   |  |  |  |
   | --- | --- | --- |
   |  | Ψ​(t)=[00⋯α1​w​e−β1​tα1​n​e−β1​t00⋯α1​n​e−β1​tα1​w​e−β1​t⋯⋯⋯⋯⋯αm​w​e−βm​tαm​n​e−βm​t⋯00αm​n​e−βm​tαm​w​e−βm​t⋯00]Ψ𝑡matrix00⋯subscript𝛼1𝑤superscriptesubscript𝛽1𝑡subscript𝛼1𝑛superscriptesubscript𝛽1𝑡00⋯subscript𝛼1𝑛superscriptesubscript𝛽1𝑡subscript𝛼1𝑤superscriptesubscript𝛽1𝑡⋯⋯⋯⋯⋯subscript𝛼𝑚𝑤superscriptesubscript𝛽𝑚𝑡subscript𝛼𝑚𝑛superscriptesubscript𝛽𝑚𝑡⋯00subscript𝛼𝑚𝑛superscriptesubscript𝛽𝑚𝑡subscript𝛼𝑚𝑤superscriptesubscript𝛽𝑚𝑡⋯00\Psi(t)=\begin{bmatrix}0&0&\cdots&\alpha\_{1w}\mathrm{e}^{-\beta\_{1}t}&\alpha\_{1n}\mathrm{e}^{-\beta\_{1}t}\\ 0&0&\cdots&\alpha\_{1n}\mathrm{e}^{-\beta\_{1}t}&\alpha\_{1w}\mathrm{e}^{-\beta\_{1}t}\\ \cdots&\cdots&\cdots&\cdots&\cdots\\ \alpha\_{mw}\mathrm{e}^{-\beta\_{m}t}&\alpha\_{mn}\mathrm{e}^{-\beta\_{m}t}&\cdots&0&0\\ \alpha\_{mn}\mathrm{e}^{-\beta\_{m}t}&\alpha\_{mw}\mathrm{e}^{-\beta\_{m}t}&\cdots&0&0\end{bmatrix} |  |

### 2.2 Stability condition

The proposed process can be shown to be well defined and to admit a version with stationary increments under the condition holds of which all eigenvalues of the matrix

|  |  |  |
| --- | --- | --- |
|  | ∫0∞𝒉​(τ)​𝑑τsuperscriptsubscript0𝒉𝜏differential-d𝜏\int\_{0}^{\infty}\bm{h}(\tau)d\tau |  |

are less than one
(Hawkes, [1971b](#bib.bib33); Bacry
et al., [2013](#bib.bib5)). The matrix is called a branching matrix, which is used by, e.g. Filimonov and
Sornette ([2012](#bib.bib27)), Hardiman
et al. ([2013](#bib.bib31)).
Such terminology is related to the ancestor-offspring argument.
The immigrant ancestor arrives at the system exogenously at a basic intensity rate 𝝁𝝁\bm{\mu},
and this ancestor event produces internally offspring arrivals in the system with the intensity hℎh that relies on the ancestor’s arrivals.
Both ancestor and offspring arrivals can increase likelihood of occurrence for additional events in the system.
Satisfying the stability condition indicates that each ancestor arrival generates “less than one offspring event” on average, and hence the process can be stable. Otherwise, the process can diverge to an infinite value within a finite time.

From this argument, we investigate stability of the Hawkes flocking process by computing spectral radius, which is defined by the largest absolute value among the eigenvalues of the branching matrix, and checking out that the spectral radius is less than one.
Since the branching matrix still depends on the original process 𝑵tsubscript𝑵𝑡\bm{N}\_{t}, unlike the pure Hawkes model777In the Hawkes process, the feedback kernel is usually given as a deterministic function., the stability condition gets to have a stochastic form.
To make the stability condition be feasible to implement in computation, we take account of approximation of the branching matrix by taking unconditional expectation on it.
For the proposed model, we set a branching matrix M𝑀M with a component

|  |  |  |
| --- | --- | --- |
|  | Mi,j=∫0∞|Φi​j​(t)+𝔼​[ki​j​(t)]​Ψi​j​(t)|​dt,for​   1≤i,j≤4.formulae-sequencesubscript𝑀  𝑖𝑗superscriptsubscript0subscriptΦ𝑖𝑗𝑡𝔼delimited-[]subscript𝑘𝑖𝑗𝑡subscriptΨ𝑖𝑗𝑡differential-d𝑡formulae-sequencefor1𝑖𝑗4M\_{i,j}=\int\_{0}^{\infty}|\Phi\_{ij}(t)+\mathbb{E}[k\_{ij}(t)]\Psi\_{ij}(t)|\mathrm{d}t,\,\,\,\text{for}\,\,\,1\leq i,j\leq 4. |  |

It implies the expected level of the number of offspring events caused by one ancestor event arriving at the rate 𝝁𝝁\bm{\mu}.

For the expectation 𝔼​[ki​j​(t)]𝔼delimited-[]subscript𝑘𝑖𝑗𝑡\mathbb{E}[k\_{ij}(t)], we set the probabilities of {C1​(t)<C2​(t)}subscript𝐶1𝑡subscript𝐶2𝑡\{C\_{1}(t)<C\_{2}(t)\} and {C1​(t)>C2​(t)}subscript𝐶1𝑡subscript𝐶2𝑡\{C\_{1}(t)>C\_{2}(t)\} by p≤0.5𝑝0.5p\leq 0.5 and 1−p1𝑝1-p, respectively888This model does not consider occurrence for the case {C1​(t)=C2​(t)}subscript𝐶1𝑡subscript𝐶2𝑡\{C\_{1}(t)=C\_{2}(t)\}.. Thus, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | M=[α1​sβ1α1​cβ1p​α1​wβ1p​α1​nβ1α1​cβ1α1​sβ1(1−p)​α1​nβ1(1−p)​α1​wβ1(1−p)​α2​wβ2(1−p)​α2​nβ2α2​sβ2α2​cβ2p​α2​nβ2p​α2​wβ2α2​cβ2α2​sβ2].𝑀matrixsubscript𝛼1𝑠subscript𝛽1subscript𝛼1𝑐subscript𝛽1𝑝subscript𝛼1𝑤subscript𝛽1𝑝subscript𝛼1𝑛subscript𝛽1subscript𝛼1𝑐subscript𝛽1subscript𝛼1𝑠subscript𝛽11𝑝subscript𝛼1𝑛subscript𝛽11𝑝subscript𝛼1𝑤subscript𝛽11𝑝subscript𝛼2𝑤subscript𝛽21𝑝subscript𝛼2𝑛subscript𝛽2subscript𝛼2𝑠subscript𝛽2subscript𝛼2𝑐subscript𝛽2𝑝subscript𝛼2𝑛subscript𝛽2𝑝subscript𝛼2𝑤subscript𝛽2subscript𝛼2𝑐subscript𝛽2subscript𝛼2𝑠subscript𝛽2M=\begin{bmatrix}\frac{\alpha\_{1s}}{\beta\_{1}}&\frac{\alpha\_{1c}}{\beta\_{1}}&p\frac{\alpha\_{1w}}{\beta\_{1}}&p\frac{\alpha\_{1n}}{\beta\_{1}}\\[6.0pt] \frac{\alpha\_{1c}}{\beta\_{1}}&\frac{\alpha\_{1s}}{\beta\_{1}}&(1-p)\frac{\alpha\_{1n}}{\beta\_{1}}&(1-p)\frac{\alpha\_{1w}}{\beta\_{1}}\\[6.0pt] (1-p)\frac{\alpha\_{2w}}{\beta\_{2}}&(1-p)\frac{\alpha\_{2n}}{\beta\_{2}}&\frac{\alpha\_{2s}}{\beta\_{2}}&\frac{\alpha\_{2c}}{\beta\_{2}}\\[6.0pt] p\frac{\alpha\_{2n}}{\beta\_{2}}&p\frac{\alpha\_{2w}}{\beta\_{2}}&\frac{\alpha\_{2c}}{\beta\_{2}}&\frac{\alpha\_{2s}}{\beta\_{2}}\end{bmatrix}. |  | (7) |

Since it is empirically shown that p𝑝p is quite close to 0.5, we may assume that both probabilities
are identical.
Under the setup, we obtain the spectral radius of the branching matrix M𝑀M such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρM=12​(a+a2+4​(b−c)),subscript𝜌𝑀12𝑎superscript𝑎24𝑏𝑐\rho\_{M}=\frac{1}{2}\left(a+\sqrt{a^{2}+4(b-c)}\right), |  | (8) |

where a,b,

𝑎𝑏a,b, and c𝑐c are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | a𝑎\displaystyle a | =α1​s+α1​cβ1+α2​s+α2​cβ2,absentsubscript𝛼1𝑠subscript𝛼1𝑐subscript𝛽1subscript𝛼2𝑠subscript𝛼2𝑐subscript𝛽2\displaystyle=\frac{\alpha\_{1s}+\alpha\_{1c}}{\beta\_{1}}+\frac{\alpha\_{2s}+\alpha\_{2c}}{\beta\_{2}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | b𝑏\displaystyle b | =α1​n​α2​n+α1​n​α2​w+α1​w​α2​n+α1​w​α2​w4​β1​β2,absentsubscript𝛼1𝑛subscript𝛼2𝑛subscript𝛼1𝑛subscript𝛼2𝑤subscript𝛼1𝑤subscript𝛼2𝑛subscript𝛼1𝑤subscript𝛼2𝑤4subscript𝛽1subscript𝛽2\displaystyle=\frac{\alpha\_{1n}\alpha\_{2n}+\alpha\_{1n}\alpha\_{2w}+\alpha\_{1w}\alpha\_{2n}+\alpha\_{1w}\alpha\_{2w}}{4\beta\_{1}\beta\_{2}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | c𝑐\displaystyle c | =α1​s​α2​s+α1​s​α2​c+α1​c​α2​s+α1​c​α2​cβ1​β2,absentsubscript𝛼1𝑠subscript𝛼2𝑠subscript𝛼1𝑠subscript𝛼2𝑐subscript𝛼1𝑐subscript𝛼2𝑠subscript𝛼1𝑐subscript𝛼2𝑐subscript𝛽1subscript𝛽2\displaystyle=\frac{\alpha\_{1s}\alpha\_{2s}+\alpha\_{1s}\alpha\_{2c}+\alpha\_{1c}\alpha\_{2s}+\alpha\_{1c}\alpha\_{2c}}{\beta\_{1}\beta\_{2}}, |  |

and hereafter we call ρMsubscript𝜌𝑀\rho\_{M} by a branching ratio.

The branching ratio ρMsubscript𝜌𝑀\rho\_{M} measures how fast the increased feedback kernel due to arrivals generated from internal and external sources is shrinking as time goes.
If it shrinks quickly, it infers that instability in microscopic price dynamics stays low.
Oppositely, if it does shrink reluctantly, it may infer that instability stays high.
In this context, we may find a relevance of the branching ratio with a systemic risk level in price dynamics.
More discussion on the branching ratio with a systemic risk indicator will be in Section [4.1](#S4.SS1 "4.1 The Hawkes flocking model and its relevance of systemic risk ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").

To summarize, the Hawkes flocking model has the following characteristics.
Each price process has a self/mutually-exciting terms that are affected by its original changes in tick price dynamics.
In addition, both prices incorporate a flocking feature describing as propensity of two dynamics moving together.
Such phenomenon emerges when narrowing and widening events between two prices occur.
We obtain a direct mapping between an original process 𝑵tsubscript𝑵𝑡\bm{N}\_{t} and a feedback kernel with a branching matrix M𝑀M, in which a main event occurs exogenously with basic intensity 𝝁𝝁\bm{\mu} and may give rise to additional following events endogenously with intensity M𝑀M on average.

## 3 Application to Empirical Data

In this section we examine the stylized facts of two major oil-related energy prices in the US.
Figure [2](#S3.F2 "Figure 2 ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") indicates the time series of daily closing prices for WTI crude oil futures and RBOB999RBOB stands for reformulated gasoline blendstock for oxygen blending. gasoline futures from 2007 to 2016.
In this section, we use the gasoline price multiplied by a factor 42 because crude oil price is quoted per barrel, whereas gasoline price is quoted per gallon1010101 barrel = 42 gallons.
Each series is created by connecting the prices of the nearest maturity contracts.

![Refer to caption](/html/2012.04181/assets/x2.png)


Figure 2: The history of daily closing prices for WTI crude oil futures (black) and RBOB gasoline futures (orange) from January 1, 2007 to December 30, 2016. The cyan-shaded areas represent (i) September 2008 – December 2008 (ii) July 2014 – January 2015 (iii) July 2015 – February 2016, in order.

As shown in Figure [2](#S3.F2 "Figure 2 ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach"), there were a three times of significant drops in both series – from September 2008 to December 2008; from July 2014 to January 2015; from July 2015 to February 2016 – representing a cyan-shaded area in order.
We investigate the change in parameters of the Hawkes flocking model, especially focusing on the three specified periods when the two prices plunged, and we compare them with the CoVaR values in the following section.
The data considered in this test are tick size change data in milliseconds for the WTI crude oil and gasoline futures listed in NYMEX from 2007 to 2016.

### 3.1 Estimation method

This section explains the ML estimation method used for the empirical study and demonstrates simulation to show the ML estimator’s goodness-of-fit to the Hawkes flocking model.
By following the idea in the algorithm by Ogata ([1978](#bib.bib48), [1981](#bib.bib49)), we perform the ML method using the log-likelihood function represented by conditional intensities as follows.

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(θ)=𝐿𝜃absent\displaystyle L(\theta)= | ∑j=1N1u​(T)log⁡λ1u​(t1,ju)+∑j=1N1d​(T)log⁡λ1d​(t1,jd)+∑j=1N2u​(T)log⁡λ2u​(t2,ju)+∑j=1N2d​(T)log⁡λ2d​(t2,jd)superscriptsubscript𝑗1superscriptsubscript𝑁1𝑢𝑇superscriptsubscript𝜆1𝑢superscriptsubscript𝑡  1𝑗𝑢superscriptsubscript𝑗1superscriptsubscript𝑁1𝑑𝑇superscriptsubscript𝜆1𝑑superscriptsubscript𝑡  1𝑗𝑑superscriptsubscript𝑗1superscriptsubscript𝑁2𝑢𝑇superscriptsubscript𝜆2𝑢superscriptsubscript𝑡  2𝑗𝑢superscriptsubscript𝑗1superscriptsubscript𝑁2𝑑𝑇superscriptsubscript𝜆2𝑑superscriptsubscript𝑡  2𝑗𝑑\displaystyle\sum\_{j=1}^{N\_{1}^{u}(T)}\log\lambda\_{1}^{u}(t\_{1,j}^{u})+\sum\_{j=1}^{N\_{1}^{d}(T)}\log\lambda\_{1}^{d}(t\_{1,j}^{d})+\sum\_{j=1}^{N\_{2}^{u}(T)}\log\lambda\_{2}^{u}(t\_{2,j}^{u})+\sum\_{j=1}^{N\_{2}^{d}(T)}\log\lambda\_{2}^{d}(t\_{2,j}^{d}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −∫0T(λ1u​(u)+λ1d​(u)+λ2u​(u)+λ2d​(u))​dusuperscriptsubscript0𝑇superscriptsubscript𝜆1𝑢𝑢superscriptsubscript𝜆1𝑑𝑢superscriptsubscript𝜆2𝑢𝑢superscriptsubscript𝜆2𝑑𝑢differential-d𝑢\displaystyle-\int\_{0}^{T}\left(\lambda\_{1}^{u}(u)+\lambda\_{1}^{d}(u)+\lambda\_{2}^{u}(u)+\lambda\_{2}^{d}(u)\right)\mathrm{d}u |  | (9) |

where λi⋅superscriptsubscript𝜆𝑖⋅\lambda\_{i}^{\cdot} indicates the left-continuous versions of the conditional intensity processes, and
ti,j⋅superscriptsubscript𝑡

𝑖𝑗⋅t\_{i,j}^{\cdot} indicates the associated event times.
The parameter set θ=(μi,βi,αi​s,αi​c,αi​n,αi​w)𝜃subscript𝜇𝑖subscript𝛽𝑖subscript𝛼𝑖𝑠subscript𝛼𝑖𝑐subscript𝛼𝑖𝑛subscript𝛼𝑖𝑤\theta=(\mu\_{i},\beta\_{i},\alpha\_{is},\alpha\_{ic},\alpha\_{in},\alpha\_{iw}) for all i=1,2𝑖

12i=1,2 is estimated by maximizing the log-likelihood function numerically.

Since the estimation proceeds numerically with twelve parameters without the assurance of the convexity of the log-likelihood function,
it is not mathematically guaranteed to find the global maximum.
It is therefore worthwhile to check under various situations whether the numerical optimizer can find the correct estimates.
Using the present parameters, 500 sample paths are generated for two price processes under the Hawkes flocking model.
The presumed values are presented in the column titled “True” in Table [1](#S3.T1 "Table 1 ‣ 3.1 Estimation method ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").
The column “Mean” presents the means of the estimates of 500 estimation procedures, which are quite close to the true values.
Since the above results show that the numerical optimizer that Henningsen and
Toomet ([2011](#bib.bib35)) used works well, we apply this procedure in empirical studies.

Table 1: Simulation using ML estimation for a Hawkes flocking model with 500 sample paths

|  | True | Mean | Std. | True | Mean | Std. | True | Mean | Std. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| μ1subscript𝜇1\mu\_{1} | 0.0800 | 0.0803 | 0.0039 | 0.0500 | 0.0503 | 0.0025 | 0.1000 | 0.1000 | 0.0074 |
| α1​nsubscript𝛼1𝑛\alpha\_{1n} | 0.0000 | -0.0009 | 0.0124 | 0.2000 | 0.2001 | 0.0206 | 0.3000 | 0.3015 | 0.0324 |
| α1​wsubscript𝛼1𝑤\alpha\_{1w} | 0.2000 | 0.2007 | 0.0142 | 0.3500 | 0.3509 | 0.0200 | 0.3500 | 0.3501 | 0.0247 |
| α1​ssubscript𝛼1𝑠\alpha\_{1s} | 0.4000 | 0.4013 | 0.0083 | 0.1500 | 0.1505 | 0.0140 | 0.2000 | 0.1988 | 0.0176 |
| α1​csubscript𝛼1𝑐\alpha\_{1c} | 0.0000 | -0.0004 | 0.0141 | 0.4000 | 0.4005 | 0.0168 | 0.2000 | 0.2005 | 0.0157 |
| β1subscript𝛽1\beta\_{1} | 0.6000 | 0.6008 | 0.0212 | 1.0500 | 1.0513 | 0.0368 | 0.9000 | 0.9011 | 0.0402 |
| μ2subscript𝜇2\mu\_{2} | 0.0500 | 0.0500 | 0.0023 | 0.0700 | 0.0702 | 0.0027 | 0.1200 | 0.1207 | 0.0072 |
| α2​nsubscript𝛼2𝑛\alpha\_{2n} | 0.0000 | -0.0001 | 0.0105 | 0.3500 | 0.3495 | 0.0269 | 0.0000 | 0.0010 | 0.0215 |
| α2​wsubscript𝛼2𝑤\alpha\_{2w} | 0.1000 | 0.1009 | 0.0115 | 0.1000 | 0.1001 | 0.0162 | 0.1000 | 0.1003 | 0.0216 |
| α2​ssubscript𝛼2𝑠\alpha\_{2s} | 0.5000 | 0.5014 | 0.0242 | 0.4500 | 0.4505 | 0.0213 | 0.3000 | 0.2995 | 0.0224 |
| α2​csubscript𝛼2𝑐\alpha\_{2c} | 0.3000 | 0.3005 | 0.0178 | 0.2500 | 0.2497 | 0.0142 | 0.6000 | 0.6006 | 0.0282 |
| β2subscript𝛽2\beta\_{2} | 1.2000 | 1.2028 | 0.0446 | 1.3000 | 1.2999 | 0.0465 | 1.1500 | 1.1519 | 0.0467 |

### 3.2 Data

Data on WTI crude oil and gasoline futures’ trade prices are obtained from the database of Tickdatamarket (<www.tickdatamarket.com>).
We choose the futures data on “Light Sweet Crude Oil” for WTI crude oil (referred to as “CL” henceforth) and “RBOB Gasoline” for gasoline (referred to as “RB” henceforth) in the energy sector of North America.
We consider the data for 10 years from January 1, 2007 to December 30, 2016, and each year has twelve delivery months.
To construct a single time series over that period for each futures contract, we select data with the nearest delivery month from the observation date, which is usually the most liquid among contracts with maturity longer than one month.

To ensure that raw data can be more feasibly applied to the proposed model, a data wrangling procedure is needed.
Without loss of generality, we transform the raw data into a more appropriate format in terms of the following aspects.

(i) Different price level: The two futures prices of CL and RB have different price levels.
For instance, the CL price at January 13, 2016 with maturity in January 2016 is around $31, but the RB price is around $1.07 per gallon, which is $44.94 per barrel.
Minimum tick sizes are also different.
The tick size is 0.01 for CL and 0.0001 for RB.
Therefore, we need to adjust prices to similar levels.
For adjustment, we consider the sample mean ratio, X¯/Y¯¯𝑋¯𝑌\bar{X}/\bar{Y}
where X¯¯𝑋\bar{X} implies the sample mean of prices, for example, of the day.

Let X𝑋X and Y𝑌Y be the original price processes.
Define C1=Xsubscript𝐶1𝑋C\_{1}=X, C2=(X¯/Y¯)​Ysubscript𝐶2¯𝑋¯𝑌𝑌C\_{2}=(\bar{X}/\bar{Y})Y.
However, the adjusted prices on a daily basis are not applicable for the Hawkes flocking model as presented in the left of Figure [3](#S3.F3 "Figure 3 ‣ 3.2 Data ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach"), where C1subscript𝐶1C\_{1} denotes CL and C2subscript𝐶2C\_{2} denotes RB.
Data for March 15, 2016 with maturity March 2016 were used.
In the early part of the day, it is almost always C1<C2subscript𝐶1subscript𝐶2C\_{1}<C\_{2}, but in the later part, it is almost always C2>C1subscript𝐶2subscript𝐶1C\_{2}>C\_{1}.
Thus, the sample mean should be computed under a shorter time interval.
For example, we calculate the sample mean every 10 minutes, and the prices are adjusted during each 10-minute interval.
Then the price processes are more applicable, as in the right of Figure [3](#S3.F3 "Figure 3 ‣ 3.2 Data ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").

(ii) Multiple price changes in unit time:
The minimum resolution time of the data is one second, and multiple price changes can be observed in one second.
In this case, we assume that each change occurs at the equi-distant time interval that divides one second with the same number of observations.

(iii) Simultaneous changes in the two prices:
The probability that the two prices change at the same time is almost zero in our model, but simultaneous changes in both prices can be recorded in practice.
In this case, one price change was assumed to have occurred slightly earlier than the other change.
Since this simultaneous jump can be observed several times a day,
we consider that one jump to have occurred before the other.

![Refer to caption](/html/2012.04181/assets/x3.png)

![Refer to caption](/html/2012.04181/assets/x4.png)

Figure 3: Before (left) and after adjustment (right) for CL and RB prices traded at March 15, 2016

### 3.3 Robustness test for calibration

From the time series of the CL and RB futures prices after data pre-processing,
we estimate the model parameters using the ML estimator presented in Section [3.1](#S3.SS1 "3.1 Estimation method ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").
The estimation is performed for up to 10 years.
We investigate the dynamics of all parameters for the proposed model over time,
especially focusing on the periods of plunges in the CL and RB prices.

Before implementing model calibration, we conduct a test for the relation between the two parts in the intensity kernel 𝒉𝒉\bm{h}: a self/mutually-exciting factor and a flocking factor.
We consider two models with different kernels: (i) a symmetric Hawkes model without a flocking term versus (ii) a Hawkes flocking model. Then, we compare the parameter estimation results derived from each model.

First, we assume that CL and RB futures prices follow a symmetric Hawkes process that has an exponential decaying kernel without a flocking term, that is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝀t=𝝁+∫−∞tΦ​(t−u)​d𝑵usubscript𝝀𝑡𝝁superscriptsubscript𝑡Φ𝑡𝑢differential-dsubscript𝑵𝑢\bm{\lambda}\_{t}=\bm{\mu}+\int\_{-\infty}^{t}\Phi(t-u)\mathrm{d}\bm{N}\_{u} |  | (10) |

where the matrix ΦΦ\Phi is symmetric with parameters αi​s,αi​c

subscript𝛼𝑖𝑠subscript𝛼𝑖𝑐\alpha\_{is},\alpha\_{ic}, and βisubscript𝛽𝑖\beta\_{i} for i=1,2𝑖

12i=1,2, as defined in ([3](#S2.E3 "In item (i) ‣ 2.1 Model specification ‣ 2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")).
In this setup, since the flocking phenomenon between the CL and RB futures prices is not implicated, the two processes are independent.

Second, we assume that CL and RB futures prices follow the Hawkes flocking process, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝀t=𝝁+∫−∞tΦ​(t−u)+k​(u)∘Ψ​(t−u)​d​𝑵usubscript𝝀𝑡𝝁superscriptsubscript𝑡Φ𝑡𝑢𝑘𝑢Ψ𝑡𝑢dsubscript𝑵𝑢\bm{\lambda}\_{t}=\bm{\mu}+\int\_{-\infty}^{t}\Phi(t-u)+{k}(u)\circ\Psi(t-u)\mathrm{d}\bm{N}\_{u} |  | (11) |

where the matrix k𝑘{k} and ΨΨ\Psi are defined in ([4](#S2.E4 "In item (ii) ‣ 2.1 Model specification ‣ 2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) and ([5](#S2.E5 "In item (ii) ‣ 2.1 Model specification ‣ 2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")), respectively,
with additional parameters αi​n,αi​w

subscript𝛼𝑖𝑛subscript𝛼𝑖𝑤\alpha\_{in},\alpha\_{iw} for i=1,2𝑖

12i=1,2.

###### Example 1.

[Multicollinearity for αssubscript𝛼𝑠\alpha\_{s} and αcsubscript𝛼𝑐\alpha\_{c}].
We estimate the parameters αssubscript𝛼𝑠\alpha\_{s} and αcsubscript𝛼𝑐\alpha\_{c} from CL and RB futures prices under each model assumption.
The test is performed on a daily basis on the futures prices with maturity in February 2016, and the observation period is from January 4 to February 22, 2016.
Figure [4](#S3.F4 "Figure 4 ‣ Example 1. ‣ 3.3 Robustness test for calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") illustrates the results of αssubscript𝛼𝑠\alpha\_{s} and αcsubscript𝛼𝑐\alpha\_{c} for CL and RB under the symmetric Hawkes model (red solid line) and the Hawkes flocking model (black dashed line).

We find that the estimates under different model assumptions are almost identical over the observed period.
This implies that k​(u)∘Ψ​(t−u)𝑘𝑢Ψ𝑡𝑢{k}(u)\circ\Psi(t-u) in the Hawkes flocking model does not affect the existing self/mutually-exciting parts Φ​(t−u)Φ𝑡𝑢\Phi(t-u).
This concept can be considered as being similar to the non-existence of multicollinearity in linear regression.

![Refer to caption](/html/2012.04181/assets/x5.png)


(a) αssubscript𝛼𝑠\alpha\_{s} in CL

![Refer to caption](/html/2012.04181/assets/x6.png)


(b) αcsubscript𝛼𝑐\alpha\_{c} in CL

![Refer to caption](/html/2012.04181/assets/x7.png)


(c) αssubscript𝛼𝑠\alpha\_{s} in RB

![Refer to caption](/html/2012.04181/assets/x8.png)


(d) αcsubscript𝛼𝑐\alpha\_{c} in RB

Figure 4: Comparison of estimates of αssubscript𝛼𝑠\alpha\_{s} and αcsubscript𝛼𝑐\alpha\_{c} under a symmetric Hawkes model (red solid line) and the Hawkes flocking model (black dotted line) for CL and RB futures prices (with maturity in February 2016) from January 4 to February 22, 2016

###### Example 2.

[Multicollinearity for μ𝜇\mu and β𝛽\beta].
We conduct the same test as conducted in Example [1](#Thmexample1 "Example 1. ‣ 3.3 Robustness test for calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") on the base intensity parameter μisubscript𝜇𝑖\mu\_{i} and the resilience speed to the base intensity βisubscript𝛽𝑖\beta\_{i} over the same sample period.
Figures [6](#S3.F6 "Figure 6 ‣ Example 2. ‣ 3.3 Robustness test for calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") and [6](#S3.F6 "Figure 6 ‣ Example 2. ‣ 3.3 Robustness test for calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") show the results of parameters μisubscript𝜇𝑖\mu\_{i} and βisubscript𝛽𝑖\beta\_{i} based on the two models, respectively.

For μ𝜇\mu, we find that both CL and RB futures prices of the symmetric Hawkes model have larger μ𝜇\mu than those of the Hawkes flocking model.
The reason is that additional fluctuations in price processes due to the flocking phenomenon are considered as a part of exogenous dynamics, and hence they are inherent to μ𝜇\mu
under the symmetric Hawkes models where flocking terms, αnsubscript𝛼𝑛\alpha\_{n} and αwsubscript𝛼𝑤\alpha\_{w}, do not exist.

For β𝛽\beta,
we see that results from the symmetric Hawkes and Hawkes flocking models are very similar for the CL futures price.
Meanwhile, the β𝛽\beta in the Hawkes flocking model is slightly larger than β𝛽\beta in the symmetric Hawkes model for the RB futures price.
This implies that “β𝛽\beta due to αnsubscript𝛼𝑛\alpha\_{n} and αwsubscript𝛼𝑤\alpha\_{w}” is larger than “β𝛽\beta due to αssubscript𝛼𝑠\alpha\_{s} and αcsubscript𝛼𝑐\alpha\_{c}” in RB.
Note that a large β𝛽\beta implies weak persistence.
We do not rule the possibility out that β𝛽\beta depends on α𝛼\alpha’s but merely consider unified β𝛽\beta for model parsimony.

![Refer to caption](/html/2012.04181/assets/x9.png)

![Refer to caption](/html/2012.04181/assets/x10.png)

Figure 5: Comparison of estimates of μ1subscript𝜇1\mu\_{1} and μ2subscript𝜇2\mu\_{2} under the symmetric Hawkes model (red line) and the Hawkes flocking model (black dotted line) for CL and RB futures prices (with maturity in February 2016) from January 4 to February 22, 2016

![Refer to caption](/html/2012.04181/assets/x11.png)

![Refer to caption](/html/2012.04181/assets/x12.png)

Figure 6: Comparison of estimates of β1subscript𝛽1\beta\_{1} and β2subscript𝛽2\beta\_{2} under the symmetric Hawkes model (red line) and the Hawkes flocking model (black dotted line) for CL and RB futures prices (with maturity in February 2016) from January 4 to February 22, 2016

More relevant examples for other sample periods appear in Appendix [D](#A4 "Appendix D More tests for calibration in Section 3 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").

### 3.4 Calibration

Based on the argument of the model’s robustness check, we conduct calibration for all 12 parameters in the Hawkes flocking model on the partial period in 2016, where the results are presented in Tables [4](#A4.T4 "Table 4 ‣ Appendix D More tests for calibration in Section 3 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") and [5](#A4.T5 "Table 5 ‣ Appendix D More tests for calibration in Section 3 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").
In particular, we investigate significance of flocking parameters αnsubscript𝛼𝑛\alpha\_{n} and αwsubscript𝛼𝑤\alpha\_{w} with more attention.
Figure [7](#S3.F7 "Figure 7 ‣ 3.4 Calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") compares αnsubscript𝛼𝑛\alpha\_{n} and αwsubscript𝛼𝑤\alpha\_{w} under the Hawkes flocking model over the same sample period.
The narrowing events’ parameters αi​nsubscript𝛼𝑖𝑛\alpha\_{in} are depicted with plus minus two times of standard errors (dotted lines) to check the significance of the estimates.
The result shows that αi​nsubscript𝛼𝑖𝑛\alpha\_{in} are close to zero in the selected time period
and this means that the price difference of narrowing events does not substantially affect the intensities.

On the other hand, αi​wsubscript𝛼𝑖𝑤\alpha\_{iw} are significant. This means that the widening event significantly increases intensities associated with the flocking
so that the two price processes tend to converge toward each other after widening events.
The standard errors of αi​wsubscript𝛼𝑖𝑤\alpha\_{iw} are omitted for clarity of the graph
but the estimates of αi​wsubscript𝛼𝑖𝑤\alpha\_{iw} are statistically significant for all time period.
For the graph, selected maturity for the futures is in February 2016 and estimates are computed on a daily basis.
In addition, αwsubscript𝛼𝑤\alpha\_{w} in CL is larger than that in RB.

![Refer to caption](/html/2012.04181/assets/x13.png)

![Refer to caption](/html/2012.04181/assets/x14.png)

Figure 7: Comparison of αnsubscript𝛼𝑛\alpha\_{n} and αwsubscript𝛼𝑤\alpha\_{w} for CL (left) and RB (right) futures prices (with maturity in February 2016) from January 4 to February 22, 2016

From now,
we calibrate the Hawkes flocking model by expanding the test period from a sample month (February 2016) to the recent decade from January 2007 to December 2016.
Using the transaction data of CL and RB futures prices, the estimates are computed on a daily basis and the daily estimates are averaged over a month for better visualization.
The associated results are displayed in Figures [10](#S3.F10 "Figure 10 ‣ 3.4 Calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach"), [10](#S3.F10 "Figure 10 ‣ 3.4 Calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach"), and [10](#S3.F10 "Figure 10 ‣ 3.4 Calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").

Figure [10](#S3.F10 "Figure 10 ‣ 3.4 Calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") exhibits the flocking parameters αnsubscript𝛼𝑛\alpha\_{n} (red solid line) and αwsubscript𝛼𝑤\alpha\_{w} (black dotted line) for CL (left panel) and RB (right panel).
For each futures price, the level of αnsubscript𝛼𝑛\alpha\_{n} is much smaller than that of αwsubscript𝛼𝑤\alpha\_{w} and it is close to zero for a long time period.
This seems reasonable because widening events have a strong role causing the flocking phenomenon, while narrowing events have no or relatively small effects.
In CL, αwsubscript𝛼𝑤\alpha\_{w} has the maximum value near the fourth quarter of 2008, and it gradually decreases and then increases again around 2015.
In RB, αwsubscript𝛼𝑤\alpha\_{w} gradually increases.

Figure [10](#S3.F10 "Figure 10 ‣ 3.4 Calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") shows the behavior of αssubscript𝛼𝑠\alpha\_{s} (black dotted line) and αcsubscript𝛼𝑐\alpha\_{c} (red solid line) for CL (left panel) and RB (right panel).
The self-exciting parameter αssubscript𝛼𝑠\alpha\_{s} in CL gradually decreases over time and is close to zero in 2016.
All other parameters are far from zero and do not show any particular trend.
In general, αcsubscript𝛼𝑐\alpha\_{c} is greater than αssubscript𝛼𝑠\alpha\_{s} in CL and αcsubscript𝛼𝑐\alpha\_{c} is less than αssubscript𝛼𝑠\alpha\_{s} in RB over the sample period.
It is known that the self-exciting pattern is due to order splitting
and the mutually-exciting pattern is due to microstructure noise.

Figure [10](#S3.F10 "Figure 10 ‣ 3.4 Calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") plots the behavior of exogenous fluctuation parameter μ𝜇\mu (left panel) and persistence parameter β𝛽\beta (right panel).
As mentioned before, the dynamics of μ𝜇\mu seem related to the dynamics of αwsubscript𝛼𝑤\alpha\_{w}.
In general, μ𝜇\mu in CL is larger than RB but the gap is closing.
Meanwhile, the persistence parameter β𝛽\beta is smaller in CL,
and this implies that persistence in CL is stronger than in RB.
In addition, there is no particular trend in β𝛽\beta.

![Refer to caption](/html/2012.04181/assets/x15.png)

![Refer to caption](/html/2012.04181/assets/x16.png)

Figure 8: Comparison of changes in the flocking parameters αnsubscript𝛼𝑛\alpha\_{n} (red line) and αwsubscript𝛼𝑤\alpha\_{w} (black dotted line) for CL (left) and RB (right) from January 2007 to December 2016

![Refer to caption](/html/2012.04181/assets/x17.png)

![Refer to caption](/html/2012.04181/assets/x18.png)

Figure 9: Comparison of changes in the self/mutually exciting parameters αssubscript𝛼𝑠\alpha\_{s} (red line) and αcsubscript𝛼𝑐\alpha\_{c} (black dotted line) for CL (left) and RB (right) from January 2007 to December 2016

![Refer to caption](/html/2012.04181/assets/x19.png)

![Refer to caption](/html/2012.04181/assets/x20.png)

Figure 10: Comparison of changes in the exogenous fluctuation parameter μ𝜇\mu (left) and the persistence β𝛽\beta (right) for CL (black dotted line) and RB (red line) from January 2007 to December 2016

### 3.5 Interpretation of the estimation results

Through the calibration results discussed in Section [3.4](#S3.SS4 "3.4 Calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach"),
we figure out the stylized behavioral characteristics exhibited in WTI and gasoline futures prices.
First, we observe that the main source for comovement of the two price processes is CL
by the fact that αwsubscript𝛼𝑤\alpha\_{w} in CL is greater than αwsubscript𝛼𝑤\alpha\_{w} in RB as shown in Figure [10](#S3.F10 "Figure 10 ‣ 3.4 Calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").
Both prices have comovement propensity if when a widening event occurs driven by either of them.
However, in terms of the absolute magnitude for power to move, CL is greater than RB.

Next, in a different viewpoint, we consider the following situation.
Suppose that the CL price is larger than RB, and a widening event happens by a RB’s down movement,
as illustrated in the left of Figure [11](#S3.F11 "Figure 11 ‣ 3.5 Interpretation of the estimation results ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").
In this case, the narrowing tendency can be facilitated by
(i) increase of the up intensity in RB
or (ii) increase of the down intensity in CL.
Increase of the up intensity in RB price is measured by α2​csubscript𝛼2𝑐\alpha\_{2c},
since it is caused by the previous downward movement in RB which is captured by the individual Hawkes price model within the RB price.
Similarly, increase of the down intensity in CL is represented by α1​wsubscript𝛼1𝑤\alpha\_{1w},
since this jumping is caused by a widening event affecting the intensity of CL.

When comparing α2​csubscript𝛼2𝑐\alpha\_{2c} in RB and α1​wsubscript𝛼1𝑤\alpha\_{1w} in CL in Figures [10](#S3.F10 "Figure 10 ‣ 3.4 Calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") and [10](#S3.F10 "Figure 10 ‣ 3.4 Calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach"),
it is observed that generally α1​wsubscript𝛼1𝑤\alpha\_{1w} is larger than α2​csubscript𝛼2𝑐\alpha\_{2c}.
Although it does not strictly imply that the two price paths are more likely to be narrowed by CL, we deduce that the influence of CL on narrowing is quite significant.

We also suppose that CL is greater than RB and a widening event is activated by a CL’s up movement, as in the right of Figure [11](#S3.F11 "Figure 11 ‣ 3.5 Interpretation of the estimation results ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").
In the same manner, the narrowing tendency can be facilitated by
(i) increase of the up intensity in RB
or (ii) increase of the down intensity in CL.
Increase of the up intensity in RB is captured by α2​wsubscript𝛼2𝑤\alpha\_{2w},
since it is caused by a widening event affecting the intensity of RB.
The increase of the down intensity in CL is represented by α1​csubscript𝛼1𝑐\alpha\_{1c},
since it is caused by an upward movement of CL.

Comparing α2​wsubscript𝛼2𝑤\alpha\_{2w} in RB and α1​csubscript𝛼1𝑐\alpha\_{1c} in CL in Figures [10](#S3.F10 "Figure 10 ‣ 3.4 Calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") and [10](#S3.F10 "Figure 10 ‣ 3.4 Calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach"),
it is shown that α1​csubscript𝛼1𝑐\alpha\_{1c} has a much larger value than αwsubscript𝛼𝑤\alpha\_{w} generally.
This means that if the two price levels get widened
then tendency to converge toward each other increases for both prices,
but the magnitude of power to move is much more significant in CL than in RB.
We can deduce that, in many cases, the flocking feature between CL and RB is more likely to be owing to CL.

![Refer to caption](/html/2012.04181/assets/x21.png)

![Refer to caption](/html/2012.04181/assets/x22.png)

Figure 11: Examples of widening events and their possible consequences

One possible interpretation of this result is that participants in WTI crude oil futures market seem to use information from the gasoline market more actively than do participants in the gasoline futures market from the WTI crude oil futures market.

## 4 Systemic Risk in Market Microstructure

So far, we proposed the Hawkes flocking model with an approximative stability condition given as the branching ratio ρMsubscript𝜌𝑀\rho\_{M} of the branching matrix M𝑀M in Section [2](#S2 "2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach"),
and we then calibrated the proposed model from the high-frequency data for WTI crude oil and gasoline futures in Section [3](#S3 "3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").

In this section, we discuss how to quantify systemic risk existing within and between the two price processes in a microscopic level based on the definition of the branching ratio.
We finally compare the systemic risk levels embedded in the two futures prices by using different measurements through (i) a branching ratio analysis in the proposed model and (ii) CoVaR which is a widely used method for systemic risk.
To implement the CoVaR for the empirical data of WTI crude oil and gasoline futures prices, we adopt
a CoVaR-copula approach, which is developed by Reboredo and
Ugolini ([2015](#bib.bib54)) and Reboredo ([2015](#bib.bib53)).

### 4.1 The Hawkes flocking model and its relevance of systemic risk

Understanding systemic risk is one of major topics in modern financial risk management in terms of definition, quantification, and regulation.
A wide range of literature discusses on systemic risk.
One strand of the literature relates to a market-based risk measure, which are
CoVaR proposed by Adrian and
Brunnermeier ([2016](#bib.bib3)); marginal expected shortfall by Acharya et al. ([2017](#bib.bib2)); SRISK by Brownlees and
Engle ([2017](#bib.bib10));
distress insurance measure by Huang
et al. ([2009](#bib.bib36)).
Another strand is under a network-based approach developed by Elliott
et al. ([2014](#bib.bib23)), Rogers and
Veraart ([2013](#bib.bib56)), Capponi and
Chen ([2015](#bib.bib12)) based on the idea by Eisenberg and
Noe ([2001](#bib.bib22)).
In addition, ones empirically observe systemic risk in a time-varying perspective through various data set. For example,
Lucas
et al. ([2014](#bib.bib43)), Oh and Patton ([2017](#bib.bib50)) use CDS spread; Reboredo ([2015](#bib.bib53)) takes stock prices; Jammazi
et al. ([2015](#bib.bib39)) uses stock-bond returns; Choroś-Tomczyk et al. ([2014](#bib.bib16)), Okhrin and
Xu ([2017](#bib.bib51)) employ portfolio credit derivative prices.

In terms of defining systemic risk, this study is inspired by the idea proposed by Danielsson and
Shin ([2003](#bib.bib18)), Danielsson
et al. ([2012](#bib.bib19)); and it is also related to Filimonov and
Sornette ([2012](#bib.bib27)), Hardiman
et al. ([2013](#bib.bib31)).
Danielsson
et al. ([2012](#bib.bib19)) firstly characterize systemic risk by introducing the concept of “endogenous risk”, which is defined as
the additional risk that the financial system adds on top of equilibrium risk as commonly understood.
In addition, price movements would be consistent with price efficiency if they were entirely driven by payoff-relevant fundamental news. However, a large part of volatility/correlation is due to a number of feedback effects.
Although the volatility/correlation stem from exogenous factors, a large part of eventual realized magnitude is due to the amplification within the system by the exogenous news.

Taking this argument into the market microstucture,
the Hawkes intensity process in ([1](#S2.E1 "In 2.1 Model specification ‣ 2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) may have the following meanings:
the base intensity is related to a portion due to the incorporation of fundamental news; and
the feedback kernel has a role of an endogenous feedback due to the trading patterns of market participants over the incorporation of fundamental news.
In this context, we employ the stability condition estimated with the branching ratio in ([8](#S2.E8 "In 2.2 Stability condition ‣ 2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) as an indicator of systemic risk in two price processes.
In other words, we may assess that a systemic risk level stays higher as the branching ratio is closer to one and does lower as it is closer to zero.
Thus, we observe how empirical values of ([8](#S2.E8 "In 2.2 Stability condition ‣ 2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) change over time using the estimated parameters in Section [3](#S3 "3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").

With more precise investigation for the proposed feedback kernel,
it is composed of two parts, the self/mutually-exciting kernel defined in ([3](#S2.E3 "In item (i) ‣ 2.1 Model specification ‣ 2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) and the flocking kernel in ([4](#S2.E4 "In item (ii) ‣ 2.1 Model specification ‣ 2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) and ([5](#S2.E5 "In item (ii) ‣ 2.1 Model specification ‣ 2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")).
We analyze the systemic risk level by distinguishing it into two factors – endogeneity within a single price process and interaction between two price processes.
As a systemic risk indicator for microstructure dynamics, we compute a quarter-wise branching ratio from the feedback kernel, which is related to each factor of endogeneity and interaction in each WTI and gasoline futures price.

The quarter-wise branching ratio is described as follows.
The branching matrix M𝑀{M} is of four-by-four size that contains 16 components as follows.

|  |  |  |  |
| --- | --- | --- | --- |
|  | M=[α1​sβ1α1​cβ1α1w2β1α1n2β1α1​cβ1α1​sβ1α1n2β1α1w2β1\hdashline​[2​p​t/2​p​t]​α2​w2​β2α2​n2​β2α2sβ2α2cβ2α2​n2​β2α2​w2​β2α2cβ2α2sβ2]𝑀delimited-[]subscript𝛼1𝑠subscript𝛽1subscript𝛼1𝑐subscript𝛽1α1w2β1α1n2β1missing-subexpressionmissing-subexpressionsubscript𝛼1𝑐subscript𝛽1subscript𝛼1𝑠subscript𝛽1α1n2β1α1w2β1missing-subexpressionmissing-subexpression\hdashlinedelimited-[]2𝑝𝑡2𝑝𝑡subscript𝛼2𝑤2subscript𝛽2subscript𝛼2𝑛2subscript𝛽2α2sβ2α2cβ2missing-subexpressionmissing-subexpressionsubscript𝛼2𝑛2subscript𝛽2subscript𝛼2𝑤2subscript𝛽2α2cβ2α2sβ2missing-subexpressionmissing-subexpressionM=\left[\begin{array}[]{cc;{2pt/2pt}cc}\frac{\alpha\_{1s}}{\beta\_{1}}&\frac{\alpha\_{1c}}{\beta\_{1}}&\frac{\alpha\_{1w}}{2\beta\_{1}}&\frac{\alpha\_{1n}}{2\beta\_{1}}\\ \frac{\alpha\_{1c}}{\beta\_{1}}&\frac{\alpha\_{1s}}{\beta\_{1}}&\frac{\alpha\_{1n}}{2\beta\_{1}}&\frac{\alpha\_{1w}}{2\beta\_{1}}\\ \hdashline[2pt/2pt]\frac{\alpha\_{2w}}{2\beta\_{2}}&\frac{\alpha\_{2n}}{2\beta\_{2}}&\frac{\alpha\_{2s}}{\beta\_{2}}&\frac{\alpha\_{2c}}{\beta\_{2}}\\ \frac{\alpha\_{2n}}{2\beta\_{2}}&\frac{\alpha\_{2w}}{2\beta\_{2}}&\frac{\alpha\_{2c}}{\beta\_{2}}&\frac{\alpha\_{2s}}{\beta\_{2}}\end{array}\right] |  | (12) |

The matrix can be divided by a four distinct quadrants (indicated by dash lines) according to the role of parameters, as shown in ([12](#S4.E12 "In 4.1 The Hawkes flocking model and its relevance of systemic risk ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")).
The components in the first and fourth quadrants represent the branching ratios that affect the self/mutually-exciting factors in CL and RB price processes, respectively.
Similarly, the components in the second and third quadrants represent the branching ratios that affect the flocking behavior (widening and narrowing events) in CL and RB price processes, respectively.

To measure the extent of amplification caused by the self/mutually-exciting factor explained by αi​s,αi​c

subscript𝛼𝑖𝑠subscript𝛼𝑖𝑐\alpha\_{is},\alpha\_{ic} and flocking factor by αi​n,αi​w

subscript𝛼𝑖𝑛subscript𝛼𝑖𝑤\alpha\_{in},\alpha\_{iw} separately,
we examine the branching ratios by component.
By taking average of four components belonging to each quadrant, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | α1​s+α1​cβ1,α2​s+α2​cβ2,α1​n+α1​w2​β1,α2​n+α2​w2​β2.  subscript𝛼1𝑠subscript𝛼1𝑐subscript𝛽1subscript𝛼2𝑠subscript𝛼2𝑐subscript𝛽2subscript𝛼1𝑛subscript𝛼1𝑤2subscript𝛽1subscript𝛼2𝑛subscript𝛼2𝑤2subscript𝛽2\frac{\alpha\_{1s}+\alpha\_{1c}}{\beta\_{1}},\,\,\,\,\frac{\alpha\_{2s}+\alpha\_{2c}}{\beta\_{2}},\,\,\,\,\frac{\alpha\_{1n}+\alpha\_{1w}}{2\beta\_{1}},\,\,\,\,\frac{\alpha\_{2n}+\alpha\_{2w}}{2\beta\_{2}}. |  | (13) |

Each value has the following interpretation:
First,
(αi​s+αi​c)/βisubscript𝛼𝑖𝑠subscript𝛼𝑖𝑐subscript𝛽𝑖(\alpha\_{is}+\alpha\_{ic})/{\beta\_{i}} indicates the average frequency of the occurrence of offspring events due to price upward or downward movements out of total arrivals for each CL or RB futures price, for i=1,2𝑖

12i=1,2.
This can be interpreted as the level of endogeneity that exists in WTI crude oil futures market for i=1𝑖1i=1 and gasoline future market for i=2𝑖2i=2.
Next,
(αi​n+αi​w)/(2​βi)subscript𝛼𝑖𝑛subscript𝛼𝑖𝑤2subscript𝛽𝑖(\alpha\_{in}+\alpha\_{iw})/(2\beta\_{i}) corresponds to the average frequency of the occurrence of offspring events due to widening and narrowing events between the two prices out of total arrivals.
This can be interpreted as the level of interaction from gasoline to WTI crude oil futures markets for i=1𝑖1i=1 and the opposite direction for i=2𝑖2i=2.

### 4.2 A CoVaR-copula approach and its implementation

A systemic risk measure focuses on a tail distribution for potential losses of given portfolios in order to investigate a spillover effect from one to another.
Among the aforementioned systemic measures in practice, CoVaR is a most widely used systemic risk measure, proposed by Adrian and
Brunnermeier ([2016](#bib.bib3)).

The CoVaR is the VaR for the financial system conditional on the fact that an individual financial institution is under stress.
Let Rtisuperscriptsubscript𝑅𝑡𝑖R\_{t}^{i} be the return for the financial market as a whole at time t𝑡t and let Rtjsuperscriptsubscript𝑅𝑡𝑗R\_{t}^{j} be the return for market j𝑗j at time t𝑡t.
The original definition of CoVaR is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(Rti≤CoVaRβ,ti|j,α=q|Rtj=VaRq,tj)=β.ℙsuperscriptsubscript𝑅𝑡𝑖conditionalsuperscriptsubscriptCoVaR  𝛽𝑡conditional𝑖  𝑗𝛼𝑞superscriptsubscript𝑅𝑡𝑗superscriptsubscriptVaR  𝑞𝑡𝑗𝛽\mathbb{P}\left(R\_{t}^{i}\leq\text{CoVaR}\_{\beta,t}^{i|j,\alpha=q}|R\_{t}^{j}=\text{VaR}\_{q,t}^{j}\right)=\beta. |  | (14) |

This is the VaR when the return of market j𝑗j stands at the VaR with the q𝑞q-percent confidence level. After that, by replacing the condition to make it more realistic, the definition was extended to the following form.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(Rti≤CoVaRβ,ti|j|Rtj≤VaRα,tj)=β,ℙsuperscriptsubscript𝑅𝑡𝑖conditionalsuperscriptsubscriptCoVaR  𝛽𝑡conditional𝑖𝑗superscriptsubscript𝑅𝑡𝑗superscriptsubscriptVaR  𝛼𝑡𝑗𝛽\mathbb{P}\left(R\_{t}^{i}\leq\text{CoVaR}\_{\beta,t}^{i|j}|R\_{t}^{j}\leq\text{VaR}\_{\alpha,t}^{j}\right)=\beta, |  | (15) |

where VaRα,tjsuperscriptsubscriptVaR

𝛼𝑡𝑗\text{VaR}\_{\alpha,t}^{j} is the VaR for market j𝑗j, measuring the maximum loss that market j𝑗j may experience for confidence level 1−α1𝛼1-\alpha and a specific time horizon, that is, the α𝛼\alpha-quantile of the return distribution for the market j𝑗j: ℙ​(Rtj≤VaRα,tj)=αℙsuperscriptsubscript𝑅𝑡𝑗superscriptsubscriptVaR

𝛼𝑡𝑗𝛼\mathbb{P}(R\_{t}^{j}\leq\text{VaR}\_{\alpha,t}^{j})=\alpha.

Using the CoVaR, the systemic risk can be measured by the delta CoVaR (Δ​CoVaRΔCoVaR\Delta\text{CoVaR}), which is the difference between the VaR of whole market conditional on the distressed state of market j𝑗j, that is, Rtj≤VaRα,tjsuperscriptsubscript𝑅𝑡𝑗superscriptsubscriptVaR

𝛼𝑡𝑗R\_{t}^{j}\leq\text{VaR}\_{\alpha,t}^{j},
and the VaR of the the whole market conditional on the normal state of market j𝑗j, that is, Rtj=VaRα=50%,tjsuperscriptsubscript𝑅𝑡𝑗superscriptsubscriptVaR𝛼

percent50𝑡𝑗R\_{t}^{j}=\text{VaR}\_{\alpha=50\%,t}^{j}. Note that usually the median quantile is considered.

To implement the defined Δ​CoVaRΔCoVaR\Delta\text{CoVaR} as presented,
we consider a copula function approach to implement Δ​CoVaRΔCoVaR\Delta\text{CoVaR}.
By consolidating the definition of CoVaR proposed by the relevant literature,
we present the formula as an analytic form using a copula function.
The following proposition shows the formula for computing Δ​CoVaRΔCoVaR\Delta\text{CoVaR} with
the relevant proof in Appendix [B](#A2 "Appendix B Proof of Proposition 4 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").

###### Proposition 4.

For a uniform vector (U,V)𝑈𝑉(U,V) with a copula function C𝐶C,
let ζv​(u)subscript𝜁𝑣𝑢\zeta\_{v}(u) denote the conditional distribution by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζv​(u)=ℙ​(U≤u|V=v)=∂C​(u,v)∂v,subscript𝜁𝑣𝑢ℙ𝑈conditional𝑢𝑉𝑣𝐶𝑢𝑣𝑣\zeta\_{v}(u)=\mathbb{P}(U\leq u|V=v)=\frac{\partial C(u,v)}{\partial v}, |  | (16) |

and Cα−1​(⋅)superscriptsubscript𝐶𝛼1⋅C\_{\alpha}^{-1}(\cdot) denote the inverse of Cα:x→C​(⋅,α):subscript𝐶𝛼→𝑥𝐶⋅𝛼C\_{\alpha}:x\rightarrow C(\cdot,\alpha).
Then, the β𝛽\beta-quantile Δ​CoVaRti|jΔsuperscriptsubscriptCoVaR𝑡conditional𝑖𝑗\Delta\text{CoVaR}\_{t}^{i|j} of asset i𝑖i’s return Risuperscript𝑅𝑖R^{i} conditional on asset j𝑗j’s return Rjsuperscript𝑅𝑗R^{j} is given as an analytic form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​CoVaRti|j=CoVaRβ,ti|j−CoVaRβ,ti|j,α=0.5.ΔsuperscriptsubscriptCoVaR𝑡conditional𝑖𝑗superscriptsubscriptCoVaR  𝛽𝑡conditional𝑖𝑗superscriptsubscriptCoVaR  𝛽𝑡conditional𝑖  𝑗𝛼0.5\Delta\text{CoVaR}\_{t}^{i|j}=\text{CoVaR}\_{\beta,t}^{i|j}-\text{CoVaR}\_{\beta,t}^{i|j,\alpha=0.5}. |  | (17) |

Each part of ([17](#S4.E17 "In Proposition 4. ‣ 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) is computed by

|  |  |  |  |
| --- | --- | --- | --- |
|  | CoVaRβ,ti|j=FRti−1​(Cα−1​(α​β))​and​CoVaRβ,ti|j,α=q=FRti−1​(hq−1​(β)),superscriptsubscriptCoVaR  𝛽𝑡conditional𝑖𝑗subscriptsuperscript𝐹1superscriptsubscript𝑅𝑡𝑖subscriptsuperscript𝐶1𝛼𝛼𝛽andsuperscriptsubscriptCoVaR  𝛽𝑡conditional𝑖  𝑗𝛼𝑞superscriptsubscript𝐹superscriptsubscript𝑅𝑡𝑖1subscriptsuperscriptℎ1𝑞𝛽\text{CoVaR}\_{\beta,t}^{i|j}=F^{-1}\_{R\_{t}^{i}}\left(C^{-1}\_{\alpha}(\alpha\beta)\right)\,\,\,\text{and}\,\,\,\text{CoVaR}\_{\beta,t}^{i|j,\alpha=q}=F\_{R\_{t}^{i}}^{-1}\left(h^{-1}\_{q}(\beta)\right), |  | (18) |

where FRtisubscript𝐹superscriptsubscript𝑅𝑡𝑖F\_{R\_{t}^{i}} is the marginal distribution function of Rtisuperscriptsubscript𝑅𝑡𝑖R\_{t}^{i}.

To apply the notion of Δ​CoVaRΔCoVaR\Delta\text{CoVaR} to our study,
we compute it based on daily returns for two price dynamics.
This measure captures the level of systemic risk in a day.
We replicate the computation presented in Proposition [4](#Thmtheorem4 "Proposition 4. ‣ 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") to the transaction data over a regular time stamp t𝑡t.

Let Rt1superscriptsubscript𝑅𝑡1R\_{t}^{1} and Rt2superscriptsubscript𝑅𝑡2R\_{t}^{2} be the returns for daily observations of C1​(t)subscript𝐶1𝑡C\_{1}(t) and C2​(t)subscript𝐶2𝑡C\_{2}(t), respectively, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt1=C1​(t+Δ​t)−C1​(t)C1​(t),Rt2=C2​(t+Δ​t)−C2​(t)C2​(t),formulae-sequencesuperscriptsubscript𝑅𝑡1subscript𝐶1𝑡Δ𝑡subscript𝐶1𝑡subscript𝐶1𝑡superscriptsubscript𝑅𝑡2subscript𝐶2𝑡Δ𝑡subscript𝐶2𝑡subscript𝐶2𝑡R\_{t}^{1}=\frac{C\_{1}(t+\Delta t)-C\_{1}(t)}{C\_{1}(t)},\,\,\,\,R\_{t}^{2}=\frac{C\_{2}(t+\Delta t)-C\_{2}(t)}{C\_{2}(t)}, |  | (19) |

where Δ​tΔ𝑡\Delta t is given by a one-day length.

We consider the following four kinds of copula with different tail dependencies and symmetries:
the Gaussian copula with tail independence; Student t𝑡t copula with symmetric tail dependence; Gumbel copula with upper tail dependence and lower tail independence; Clayton copula with upper tail independence and lower tail dependence.
The details are specified in Table [2](#S4.T2 "Table 2 ‣ 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").

| Copula | Distribution C​(u,v;⋅)𝐶𝑢𝑣⋅C(u,v;\cdot) | Range of θ𝜃\theta | λLsubscript𝜆𝐿\lambda\_{L} | λUsubscript𝜆𝑈\lambda\_{U} | Generator ψ​(⋅)𝜓⋅\psi(\cdot) |
| --- | --- | --- | --- | --- | --- |
| Guassian | Φθ​(Φ−1​(u),Φ−1​(v))subscriptΦ𝜃superscriptΦ1𝑢superscriptΦ1𝑣\Phi\_{\theta}(\Phi^{-1}(u),\Phi^{-1}(v)) | (−1,1)11(-1,1) | 0 | 0 | ×\times |
| Student t𝑡t | Tν,θ​(tν−1​(u),tν−1​(v))subscript𝑇  𝜈𝜃superscriptsubscript𝑡𝜈1𝑢superscriptsubscript𝑡𝜈1𝑣T\_{\nu,\theta}(t\_{\nu}^{-1}(u),t\_{\nu}^{-1}(v)) | (−1,1)11(-1,1) | 2​tν+1​(−ν+1​1−θ1+θ)2subscript𝑡𝜈1𝜈11𝜃1𝜃2t\_{\nu+1}\left(-\frac{\sqrt{\nu+1}\sqrt{1-\theta}}{\sqrt{1+\theta}}\right) | | ×\times |
| Gumbel | exp⁡(−[(ln⁡u)θ+(ln⁡v)θ]1/θ)superscriptdelimited-[]superscript𝑢𝜃superscript𝑣𝜃1𝜃\exp\left(-[(\ln u)^{\theta}+(\ln v)^{\theta}]^{1/\theta}\right) | [1,∞)1[1,\infty) | 0 | 2−21/θ2superscript21𝜃2-2^{1/\theta} | (−ln⁡t)θsuperscript𝑡𝜃(-\ln t)^{\theta} |
| Clayton | (u−θ+v−θ−1)−1θsuperscriptsuperscript𝑢𝜃superscript𝑣𝜃11𝜃\left(u^{-\theta}+v^{-\theta}-1\right)^{-\frac{1}{\theta}} | (0,∞)0(0,\infty) | 2−21/θ2superscript21𝜃2-2^{1/\theta} | 0 | (t−θ−1)/θsuperscript𝑡𝜃1𝜃(t^{-\theta}-1)/\theta |

Table 2: Bivariate copula models with correlation parameter θ𝜃\theta, upper tail dependence λLsubscript𝜆𝐿\lambda\_{L}, lower tail λUsubscript𝜆𝑈\lambda\_{U} dependence parameters

Appendix [A](#A1 "Appendix A A CoVaR-Copula Approach ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") presents how to implement time-varying CoVaR using the copula functions.

For application of the CoVaR’s definition to our data set, we set Rt1superscriptsubscript𝑅𝑡1R\_{t}^{1} and Rt2superscriptsubscript𝑅𝑡2R\_{t}^{2} by the daily returns of CL and RB futures prices, respectively, such as defined in ([19](#S4.E19 "In 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")).
We compute one-day Δ​CoVaRt1|2ΔsubscriptsuperscriptCoVaRconditional12𝑡\Delta\text{CoVaR}^{1|2}\_{t} and one-day Δ​CoVaRt2|1ΔsubscriptsuperscriptCoVaRconditional21𝑡\Delta\text{CoVaR}^{2|1}\_{t} based on Rt1,Rt2

superscriptsubscript𝑅𝑡1superscriptsubscript𝑅𝑡2R\_{t}^{1},R\_{t}^{2}111111Since profit returns (not loss returns) are used in the computation of CoVaR and VaR, the CoVaR and VaR values with the minus sign are considered throughout the test. The minus VaR is usually given as a positive value when the quantile level is greater than 50%. .
The value of one-day Δ​CoVaRt1|2ΔsubscriptsuperscriptCoVaRconditional12𝑡\Delta\text{CoVaR}^{1|2}\_{t} is interpreted as the extent to which extreme downward changes in gasoline futures price (conditioned variable) contribute to the systemic risk in WTI crude oil futures price for a day at time t.
Conversely, the value of Δ​CoVaRt2|1ΔsubscriptsuperscriptCoVaRconditional21𝑡\Delta\text{CoVaR}^{2|1}\_{t} indicates the contribution of extreme downward changes in WTI crude oil futures price (conditioned variable) to systemic risk in gasoline futures price.

By finding the best fitting copula among the aforementioned ones (the detail procedure is explained in Appendix [C](#A3 "Appendix C Selection of the best fitting copula in Section 4.2 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")), we compute time-varying CoVaRtsubscriptCoVaR𝑡\text{CoVaR}\_{t} using Proposition [4](#Thmtheorem4 "Proposition 4. ‣ 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") with an analytic form of the ζαsubscript𝜁𝛼\zeta\_{\alpha} function.
Since the Student t𝑡t copula is chosen as having the best fit to our data over the whole test period by the AIC and BIC tests, function ([24](#A1.E24 "In 2nd item ‣ Appendix A A CoVaR-Copula Approach ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) is employed only in our analysis.
We pick the 95% quantile level for computing the CoVaR and VaR used in the conditioned part of CoVaR, that is, α=5%𝛼percent5\alpha=5\% and β=5%𝛽percent5\beta=5\%.

Figure [20](#A5.F20 "Figure 20 ‣ Appendix E Figures related to Section 4 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") (Appendix [E](#A5 "Appendix E Figures related to Section 4 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) shows the dynamics of one-day 95% CoVaRt1|2subscriptsuperscriptCoVaRconditional12𝑡\text{CoVaR}^{1|2}\_{t} and CoVaRt2|1subscriptsuperscriptCoVaRconditional21𝑡\text{CoVaR}^{2|1}\_{t} when the conditional variable is given as the distressed situation and when it is given as the normal situation α=50%𝛼percent50\alpha=50\% as presented in ([14](#S4.E14 "In 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) and ([15](#S4.E15 "In 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")), respectively,
from 2007 to 2016.
The shaded areas represent the three large drops in the WTI crude oil and gasoline futures prices as mentioned in Figure [2](#S3.F2 "Figure 2 ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").
We find that both CoVaR and Δ​CoVaRΔCoVaR\Delta\text{CoVaR} values significantly increase in distressed time periods compared with other normal times.
Moreover, relative contributions of the WTI crude oil futures to the systemic risk in gasoline futures, and vice versa, change almost similarly over time.

### 4.3 Comparison of branching ratios with CoVaRs

We simulate the branching ratio ρMsubscript𝜌𝑀\rho\_{M} in ([8](#S2.E8 "In 2.2 Stability condition ‣ 2 The Hawkes Flocking Model ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) and the quarter-wise branching ratios in ([13](#S4.E13 "In 4.1 The Hawkes flocking model and its relevance of systemic risk ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) using the best fitting kernel parameters αi​s,αi​c,αi​n,αi​w,

subscript𝛼𝑖𝑠subscript𝛼𝑖𝑐subscript𝛼𝑖𝑛subscript𝛼𝑖𝑤\alpha\_{is},\alpha\_{ic},\alpha\_{in},\alpha\_{iw}, and βisubscript𝛽𝑖\beta\_{i} for i=1,2𝑖

12i=1,2 in the Hawkes flocking model with p=1/2𝑝12p=1/2, as discussed in Subsection [3.3](#S3.SS3 "3.3 Robustness test for calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").
Moreover, the branching ratios are compared with VaR and CoVaR as a benchmark of the systemic risk.
The relevant results are displayed in Figures [12](#S4.F12 "Figure 12 ‣ 4.3 Comparison of branching ratios with CoVaRs ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach"), [13](#S4.F13 "Figure 13 ‣ 4.3 Comparison of branching ratios with CoVaRs ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach"), and [14](#S4.F14 "Figure 14 ‣ 4.3 Comparison of branching ratios with CoVaRs ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").

Figure [12](#S4.F12 "Figure 12 ‣ 4.3 Comparison of branching ratios with CoVaRs ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") illustrates time-varying ρMsubscript𝜌𝑀\rho\_{M}.
We observe that mid-2008 had the highest level of spectral radius at around 85% just before the collapse of Lehman Brothers in September 2008.
With the onset of the global credit crisis, the overall level decreased until the beginning of 2011 when it was the lowest at around 63% during the test period up to December 2016.

![Refer to caption](/html/2012.04181/assets/x23.png)


Figure 12: Illustration of spectral radius from January 2007 to December 2016

Figure [13](#S4.F13 "Figure 13 ‣ 4.3 Comparison of branching ratios with CoVaRs ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") presents the evolution of the quarter-wise branching ratios (α1​s+α1​c)/β1subscript𝛼1𝑠subscript𝛼1𝑐subscript𝛽1(\alpha\_{1s}+\alpha\_{1c})/\beta\_{1} for CL futures, (α2​s+α2​c)/β2subscript𝛼2𝑠subscript𝛼2𝑐subscript𝛽2(\alpha\_{2s}+\alpha\_{2c})/\beta\_{2} for RB futures
and their one-day 95% VaR values from January 2007 to December 2016.
For the CL futures, it varies between 58% and 82%; however, for RB futures, it varies between 32% and 60%.
This implies that the level of endogeneity in CL futures market was consistently higher than that in RB futures prices for the past decade.
In CL futures in mid-2008, the highest level of endogeneity was recorded just before the onset of the global crisis.
Meanwhile, there were no significant changes for this level in the second and third plunge periods in the CL and RB markets in 2014 and 2016, respectively.
On the other hand, for one-day 95% VaR values, precipitous rises occurred on mid-2008, 2014, and 2016 in both CL and RB markets, and the overall flows of VaR in CL and RB markets were similar.

![Refer to caption](/html/2012.04181/assets/x24.png)

![Refer to caption](/html/2012.04181/assets/x25.png)

![Refer to caption](/html/2012.04181/assets/x26.png)

![Refer to caption](/html/2012.04181/assets/x27.png)

Figure 13: Illustration of evolution of (α1​s+α1​c)/β1subscript𝛼1𝑠subscript𝛼1𝑐subscript𝛽1(\alpha\_{1s}+\alpha\_{1c})/\beta\_{1} for CL (top, left), (α2​s+α2​c)/β2subscript𝛼2𝑠subscript𝛼2𝑐subscript𝛽2(\alpha\_{2s}+\alpha\_{2c})/\beta\_{2} for RB (top, right), time-varying one-day 95% VaRVaR\mathrm{VaR} for CL (bottom, left), and VaRVaR\mathrm{VaR} for RB (bottom, right)
from January 2007 to December 2016

Figure [14](#S4.F14 "Figure 14 ‣ 4.3 Comparison of branching ratios with CoVaRs ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") presents the evolution of the quarter-wise branching ratios (α1​n+α1​w)/(2​β1)subscript𝛼1𝑛subscript𝛼1𝑤2subscript𝛽1(\alpha\_{1n}+\alpha\_{1w})/(2\beta\_{1}) for the CL process affected by the RB price fluctuation,
(α2​n+α2​w)/(2​β2)subscript𝛼2𝑛subscript𝛼2𝑤2subscript𝛽2(\alpha\_{2n}+\alpha\_{2w})/(2\beta\_{2}) for the RB process affected by CL price fluctuation,
and one-day 95% Δ​CoVaRt1|2ΔsubscriptsuperscriptCoVaRconditional12𝑡\Delta\text{CoVaR}^{1|2}\_{t} and Δ​CoVaRt2|1ΔsubscriptsuperscriptCoVaRconditional21𝑡\Delta\text{CoVaR}^{2|1}\_{t} from January 2007 to December 2016.
At a microscopic level,
the degree to which RB affects CL has values ranging between 10% and 55%;
however, the degree to which CL affects RB is between 2% and 8%.
It infers that the level to which RB price affects CL price has been consistently higher than that in its opposite direction over the past 10 years.
Moreover, a reverse pattern was observed between the relative influences on the two high-frequency price processes.
For the degree of the impact of the change in RB price on CL price, the highest level was recorded in late 2008, it gradually decreased after that but rose slightly during the second and third plunge periods.
On the other hand, the level to which the CL price affects RB price was the lowest in late 2008, but it increased to the highest level during the second and third plunge periods.
For delta CoVaR values, the extent of their relative contribution to systemic risk due to each futures market was almost symmetric.

![Refer to caption](/html/2012.04181/assets/x28.png)

![Refer to caption](/html/2012.04181/assets/x29.png)

![Refer to caption](/html/2012.04181/assets/x30.png)

![Refer to caption](/html/2012.04181/assets/x31.png)

Figure 14: Illustration of evolution of (α1​n+α1​w)/2​β1subscript𝛼1𝑛subscript𝛼1𝑤2subscript𝛽1(\alpha\_{1n}+\alpha\_{1w})/2\beta\_{1} (top, left), (α2​n+α2​w)/2​β2subscript𝛼2𝑛subscript𝛼2𝑤2subscript𝛽2(\alpha\_{2n}+\alpha\_{2w})/2\beta\_{2} (top, right),
Δ​CoVaRt1|2ΔsubscriptsuperscriptCoVaRconditional12𝑡\Delta\mathrm{CoVaR}^{1|2}\_{t} (bottom, left), and Δ​CoVaRt2|1ΔsubscriptsuperscriptCoVaRconditional21𝑡\Delta\mathrm{CoVaR}^{2|1}\_{t} (bottom, right) where Rt1superscriptsubscript𝑅𝑡1R\_{t}^{1} and Rt2superscriptsubscript𝑅𝑡2R\_{t}^{2} are given by the CL and RB daily returns at time t𝑡t, respectively, from January 2007 to December 2016

Throughout the test, we find some remarkable facts about the futures markets of WTI crude oil and gasoline in terms of high-frequency structure.
First, the overall systemic risk level in the two futures markets was the highest before the onset of the global credit crisis, and there was no considerable change in overall systemic risk in these markets when the prices plunge occurred in 2014 and 2016.
Second, when we compare the levels of endogeneity embedded in each futures market, the level of the WTI market was a significantly higher than that in the gasoline market.
Moreover, since the WTI crude oil market is more actively affected by change in the gasoline market, it is more likely to react promptly to a delicate change in the gasoline market than in the opposite case.
Last, the levels of the risk interaction between the two markets, that is, from WTI crude oil to gasoline and vice versa, were very asymmetric. However, the degree of the difference has been reducing steadily over the past decade.

## 5 Concluding Remark

We propose the Hawkes flocking model to quantify systemic risk in high-frequency markets.
The model is designed to capture self/mutually-exciting features as well as cross-exciting on the intensity processes depending on the relative position of asset prices
as the price difference is narrowed or widened.
In the empirical study, we observe a micro-level behavior between the two futures markets of WTI crude oil and gasoline.
We see that when the difference of the two prices narrows, no additional flocking phenomenon occurs, but, when they get widened, a strong flocking phenomenon occurred.
The Hawkes flocking model-based assessment is highly suitable for application of tick-by-tick data,
and it is also feasible to capture a delicate change in the level of systemic risk that appears in highly correlated data.

In terms of the assessment of systemic risk, we compare the results of the branching ratios derived from the Hawkes flocking model with the delta CoVaR, which is
introduced as a benchmark for the proposed metric of the systemic risk.
Estimating the best fit kernel using a ML estimator from the given data set, we obtain the following empirical results.
The systemic risk level in the WTI crude oil futures price has been consistently higher than that in the gasoline futures price for the test period.
Furthermore, the change in gasoline futures price has a significantly greater impact on WTI crude oil futures price than in the opposite case,
which implies that the relative contribution of each price is asymmetric at the microscopic level of price structure.

## Data Availability Statement

The part of data that support the findings of this study are openly available in figshare at <https://doi.org/10.6084/m9.figshare.9114383.v4>, refer to Lee
et al. ([2019](#bib.bib41)).

## Acknowledgements

This work was supported by “Human Resources Program in Energy Technology” of the Korea Institute of Energy Technology Evaluation and Planning (KETEP), granted financial resource from the Ministry of Trade, Industry & Energy, Republic of Korea. (No. 20184010201680); and the National Research Foundation of Korea(NRF) grant funded by the Korea government(MSIT) (No.2017R1C1B5017338).

## References

* Aas
  et al. (2009)

  Aas, K., C. Czado, A. Frigessi, and H. Bakken (2009).
  Pair-copula constructions of multiple dependence.
  Insurance: Mathematics and Economics 44(2), 182–198.
* Acharya et al. (2017)

  Acharya, V. V., L. H. Pedersen, T. Philippon, and M. Richardson (2017).
  Measuring systemic risk.
  The Review of Financial Studies 30(1), 2–47.
* Adrian and
  Brunnermeier (2016)

  Adrian, T. and M. K. Brunnermeier (2016).
  Covar.
  American Economic Review 106(7), 1705–41.
* Bacry
  et al. (2012)

  Bacry, E., K. Dayri, and J.-F. Muzy (2012).
  Non-parametric kernel estimation for symmetric hawkes processes.
  application to high frequency financial data.
  The European Physical Journal B 85(5), 157.
* Bacry
  et al. (2013)

  Bacry, E., S. Delattre, M. Hoffmann, and J.-F. Muzy (2013).
  Modelling microstructure noise with mutually exciting point
  processes.
  Quantitative Finance 13(1), 65–77.
* Bacry
  et al. (2015)

  Bacry, E., I. Mastromatteo, and J.-F. Muzy (2015).
  Hawkes processes in finance.
  Market Microstructure and Liquidity 1(01), 1550005.
* Baillie and
  Bollerslev (1989)

  Baillie, R. and T. Bollerslev (1989).
  The message in daily exchange rates: A conditional-variance tale.
  Journal of Business & Economic Statistics 7(3),
  197–305.
* Bormetti et al. (2015)

  Bormetti, G., L. M. Calcagnile, M. Treccani, F. Corsi, S. Marmi, and F. Lillo
  (2015).
  Modelling systemic price cojumps with hawkes factor models.
  Quantitative Finance 15(7), 1137–1156.
* Bowsher (2007)

  Bowsher, C.-G. (2007).
  Modelling security market events in continuous time: Intensity based,
  multivariate point process models.
  Journal of Econometrics 141(2), 876–912.
* Brownlees and
  Engle (2017)

  Brownlees, C. and R.-F. Engle (2017).
  Srisk: A conditional capital shortfall measure of systemic risk.
  The Review of Financial Studies 30(1), 48–79.
* Calcagnile et al. (2018)

  Calcagnile, L.-M., G. Bormetti, M. Treccani, S. Marmi, and F. Lillo (2018).
  Collective synchornization and high frequency systemic instabilties
  in financial markets.
  Quantitative Finance 18, 237–247.
* Capponi and
  Chen (2015)

  Capponi, A. and P.-C. Chen (2015).
  Systemic risk mitigation in financial networks.
  Journal of Economic Dynamics and Control 58, 152–166.
* Cerchi and
  Havenner (1988)

  Cerchi, M. and A. Havenner (1988).
  Cointegration and stock prices: The random walk and wall street
  revisited.
  Journal of Economic Dynamics and Control 12(-),
  333–346.
* Chavez-Demoulin
  and McGill (2012)

  Chavez-Demoulin, V. and J. McGill (2012).
  High-frequency financial data modeling using hawkes processes.
  Journal of Banking & Finance 36(12), 3415–3426.
* Chiu
  et al. (2015)

  Chiu, M. C., H. Y. Wong, and J. Zhao (2015).
  Commodity derivatives pricing with cointegration and stochastic
  covariances.
  European Journal of Operational Research 246(2),
  476–486.
* Choroś-Tomczyk et al. (2014)

  Choroś-Tomczyk, B., W. K. Härdle, and L. Overbeck (2014).
  Copula dynamics in CDOs.
  Quantitative Finance 14(9), 1573–1585.
* Da Fonseca and
  Zaatour (2014)

  Da Fonseca, J. and R. Zaatour (2014).
  Hawkes process: Fast calibration, application to trade clustering,
  and diffusive limit.
  Journal of Futures Market 34(6), 548–579.
* Danielsson and
  Shin (2003)

  Danielsson, J. and H. S. Shin (2003).
  Endogenous risk.
  pp.  297–314.
* Danielsson
  et al. (2012)

  Danielsson, J., H. S. Shin, and J.-P. Zigrand (2012).
  Endogenous and systemic risk.
  pp.  73–94.
* Duan and
  Pliska (2004)

  Duan, J.-C. and S. Pliska (2004).
  Option valuation with co-integrated asset prices.
  Journal of Economic Dynamics & Control 28(2),
  727–754.
* EIA (2014)

  EIA (2014).
  What drives us gasoline prices?
  EIA, Independent Statistics & Analysis -(October),
  –.
* Eisenberg and
  Noe (2001)

  Eisenberg, L. and T. H. Noe (2001).
  Systemic risk in financial systems.
  Management Science 47(2), 236–249.
* Elliott
  et al. (2014)

  Elliott, M., B. Golub, and M. O. Jackson (2014).
  Financial networks and contagion.
  American Economic Review 104(10), 3115–53.
* Engle and
  Granger (1987)

  Engle, R. F. and C. W. Granger (1987).
  Co-integration and error correction: representation, estimation, and
  testing.
  Econometrica: journal of the Econometric Society, 251–276.
* Fang
  et al. (2017)

  Fang, F., Y. Sun, and K. Spiliopoulos (2017).
  On the effect of heterogeneity on flocking behavior and systemic
  risk.
  Statistics & Risk Modeling 34(3-4), –.
* Fernández and
  Steel (1998)

  Fernández, C. and M. F. Steel (1998).
  On bayesian modeling of fat tails and skewness.
  Journal of the American Statistical Association 93(441), 359–371.
* Filimonov and
  Sornette (2012)

  Filimonov, V. and D. Sornette (2012).
  Quantifying reflexivity in financial markets: Toward a prediction of
  flash crashes.
  Physical Review E 85(5), 056108.
* Girardi and
  Ergun (2013)

  Girardi, G. and A.-T. Ergun (2013).
  Systemic risk measurement: Multivariate garch estimation of covar.
  Journal of Banking and Finance 37(11), 3169–3180.
* Granger (1981)

  Granger, C. W. (1981).
  Some properties of time series data and their use in econometric
  model specification.
  Journal of Econometrics 16(1), 121–130.
* Ha
  et al. (2015)

  Ha, S.-Y., K.-K. Kim, and K. Lee (2015).
  A mathematical model for multi-name credit based on community
  flocking.
  Quantitative Finance 15(5), 841–851.
* Hardiman
  et al. (2013)

  Hardiman, S. J., N. Bercot, and J.-P. Bouchaud (2013).
  Critical reflexivity in financial markets: a hawkes process analysis.
  The European Physical Journal B 86(10), 442.
* Hawkes (1971a)

  Hawkes, A. G. (1971a).
  Point spectra of some mutually exciting point processes.
  Journal of the Royal Statistical Society. Series B
  (Methodological) 33(3), 438–443.
* Hawkes (1971b)

  Hawkes, A. G. (1971b).
  Spectra of some self-exciting and mutually exciting point processes.
  Biometrika 58(1), 83–90.
* Hawkes and
  Oakes (1974)

  Hawkes, A. G. and D. Oakes (1974).
  A cluster process representation of a self-exciting process.
  Journal of Applied Probability 11(3), 493–503.
* Henningsen and
  Toomet (2011)

  Henningsen, A. and O. Toomet (2011).
  maxlik: A package for maximum likelihood estimation in r.
  Computational Statistics 26(3), 443–458.
* Huang
  et al. (2009)

  Huang, X., H. Zhou, and H. Zhu (2009).
  A framework for assessing the systemic risk of major financial
  institutions.
  Journal of Banking and Finance 33(11), 2036–2049.
* Huepe and
  Aldana (2008)

  Huepe, C. and M. Aldana (2008).
  New tools for characterizing swarming systems: A comparison of
  minimal models.
  Physic A: Statistical Mechanics and its Applications 387(12), 2809–2822.
* Jain
  et al. (2016)

  Jain, P. K., P. Jain, and T. H. McInish (2016).
  Does high-frequency trading increase systemic risk?
  Journal of Financial Markets 31, 1–24.
* Jammazi
  et al. (2015)

  Jammazi, R., A. K. Tiwari, R. Ferrer, and P. Moya (2015).
  Time-varying dependence between stock and government bond returns:
  International evidence with dynamic copulas.
  The North American Journal of Economics and Finance 33,
  74–93.
* Kellard
  et al. (2010)

  Kellard, N., C. Dunis, and N. Sarantis (2010).
  Foreign exchange, fractional cointegration and the implied–realized
  volatility relation.
  Journal of Banking & Finance 34(-), 882–891.
* Lee
  et al. (2019)

  Lee, K., H. J. Jang, and K. Lee (2019).
  WTI crude oil and RBOB gasoline futures dataset.
* Lee and Seo (2017)

  Lee, K. and B.-K. Seo (2017).
  Modeling microstructure price dynamics with symmetric hawkes and
  diffusion model using ultra-high-frequency stock data.
  Journal of Economic Dynamics and Control 79(6),
  154–183.
* Lucas
  et al. (2014)

  Lucas, A., B. Schwaab, and X. Zhang (2014).
  Conditional euro area sovereign default risk.
  Journal of Business & Economic Statistics 32(2),
  271–284.
* Maslyuka and
  Smyth (2009)

  Maslyuka, S. and R. Smyth (2009).
  Cointegration between oil spot and future prices of the same and
  different grades in the presence of structural change.
  Energy Policy 37(-), 1687–1963.
* Miller and
  Shorter (2016)

  Miller, R.-S. and G. Shorter (2016).
  High frequency trading: Overview of recent developments.
  Congressional Research Service.
* Ng and
  Pirrong (1994)

  Ng, V. K. and S. C. Pirrong (1994).
  Fundamentals and volatility: Storage, spreads, and the dynamics of
  metals prices.
  The Journal of Business 67(2), 203–230.
* Ng and
  Pirrong (1996)

  Ng, V. K. and S. C. Pirrong (1996).
  Price dynamics in refined petroleum spot and futures markets.
  Journal of Empirical Finance 2(4), 359–388.
* Ogata (1978)

  Ogata, Y. (1978).
  The asymtotic behaviour of maximum liklihood estimators for
  stationary point processes.
  Ann. Inst. Statist. Math. 30(Part A), 243–261.
* Ogata (1981)

  Ogata, Y. (1981).
  On lewis simulation method for point processes.
  IEEE Inform. Theory 27, 23–31.
* Oh and Patton (2017)

  Oh, D. H. and A. J. Patton (2017, jan).
  Modeling dependence in high dimensions with factor copulas.
  Journal of Business & Economic Statistics 35(1),
  139–154.
* Okhrin and
  Xu (2017)

  Okhrin, O. and Y. F. Xu (2017).
  A comparison study of pricing credit default swap index tranches
  with convex combination of copulae.
  The North American Journal of Economics and Finance 42,
  193–217.
* Rauch
  et al. (1995)

  Rauch, E. M., M. M. Millonas, and D. R. Chialvo (1995).
  Pattern formation and functionality in swarm models.
  Physics Letters A 207(3-4), 185–193.
* Reboredo (2015)

  Reboredo, J. C. (2015).
  Is there dependence and systemic risk between oil and renewable
  energy stock prices?
  Energy Economics 48, 32–45.
* Reboredo and
  Ugolini (2015)

  Reboredo, J. C. and A. Ugolini (2015).
  Systemic risk in european sovereign debt markets: A covar-copula
  approach.
  Journal of International Money and Finance 51,
  214–244.
* Reynolds (1987)

  Reynolds, C. W. (1987).
  Flocks, herds and schools: A distributed behavioral model.
  ACM SIGGRAPH Computer Graphics 21(-), 25–34.
* Rogers and
  Veraart (2013)

  Rogers, L. C. and L. A. Veraart (2013).
  Failure and rescue in an interbank network.
  Management Science 59(4), 882–898.
* Schepsmeier and
  Stöber (2014)

  Schepsmeier, U. and J. Stöber (2014).
  Derivatives and fisher information of bivariate copulas.
  Statistical Papers 55(2), 525–542.
* Serletis (1992)

  Serletis, A. (1992).
  Maturity effects in energy futures.
  Energy Economics 14(2), 150–157.
* Sklar (1959)

  Sklar, A. (1959).
  Fonctions de répartition à n dimensions et leurs marges.
  Publ. Inst. Statist. Univ. Paris 8, 229–234.
* Taylor and
  Tonks (1989)

  Taylor, M. and I. Tonks (1989).
  The internationalisation of stock markets and the abolition of uk
  exchange control.
  The Review of Economics and Statistics 71(2),
  332–336.

## Appendix A A CoVaR-Copula Approach

Under the copula specifications in Table [2](#S4.T2 "Table 2 ‣ 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach"), we follow a three-step procedure to implement the time-varying CoVaR.

Step 1. Estimating marginal distributions for returns.

To estimate the marginal distributions for each return Rtℓsuperscriptsubscript𝑅𝑡ℓR\_{t}^{\ell} for ℓ=1,2ℓ

12\ell=1,2, we use an ARMA​(p,q)−TGARCH​(r,m)ARMA𝑝𝑞TGARCH𝑟𝑚\text{ARMA}(p,q)-\text{TGARCH}(r,m) model, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt=ϕ0+∑j=1pϕj​Rt−j+ϵt−∑i=1qθi​ϵt−i,subscript𝑅𝑡subscriptitalic-ϕ0superscriptsubscript𝑗1𝑝subscriptitalic-ϕ𝑗subscript𝑅𝑡𝑗subscriptitalic-ϵ𝑡superscriptsubscript𝑖1𝑞subscript𝜃𝑖subscriptitalic-ϵ𝑡𝑖R\_{t}=\phi\_{0}+\sum\_{j=1}^{p}\phi\_{j}R\_{t-j}+\epsilon\_{t}-\sum\_{i=1}^{q}\theta\_{i}\epsilon\_{t-i}, |  | (20) |

where p𝑝p and q𝑞q are non-negative integers and ϕitalic-ϕ\phi and θ𝜃\theta are the ARMA parameters, respectively.
Here, ϵt=σt​zt,subscriptitalic-ϵ𝑡subscript𝜎𝑡subscript𝑧𝑡\epsilon\_{t}=\sigma\_{t}z\_{t}, and σt2superscriptsubscript𝜎𝑡2\sigma\_{t}^{2} is the conditional variance given by a TGARCH specification:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σt2=ω+∑k=1rβ​σt−k2+∑h=1mαh​ϵt−h2+∑h=1mλh​ϵt−h2​𝟙{t−h>0},superscriptsubscript𝜎𝑡2𝜔superscriptsubscript𝑘1𝑟𝛽superscriptsubscript𝜎𝑡𝑘2superscriptsubscriptℎ1𝑚subscript𝛼ℎsuperscriptsubscriptitalic-ϵ𝑡ℎ2superscriptsubscriptℎ1𝑚subscript𝜆ℎsuperscriptsubscriptitalic-ϵ𝑡ℎ2subscript1𝑡ℎ0\sigma\_{t}^{2}=\omega+\sum\_{k=1}^{r}\beta\sigma\_{t-k}^{2}+\sum\_{h=1}^{m}\alpha\_{h}\epsilon\_{t-h}^{2}+\sum\_{h=1}^{m}\lambda\_{h}\epsilon\_{t-h}^{2}\mathbbm{1}\_{\{t-h>0\}}, |  | (21) |

where ω𝜔\omega is a constant, σt−k2superscriptsubscript𝜎𝑡𝑘2\sigma\_{t-k}^{2} is the GARCH component, ϵt−hsubscriptitalic-ϵ𝑡ℎ\epsilon\_{t-h} is the ARCH component, and λ𝜆\lambda captures asymmetric effects. If λ>0𝜆0\lambda>0, then the future conditional variance will increase more following a negative shock than following a positive shock of the same magnitude.
Here, ztsubscript𝑧𝑡z\_{t} is an independent and identically distributed random variable with zero mean and unit variance that follows
a skewed-t𝑡t distribution, given by Fernández and
Steel ([1998](#bib.bib26)):

|  |  |  |
| --- | --- | --- |
|  | f​(zj,t;γ)=2γ+1γ​{fν​(zj,tγ)​𝟙[0,∞)​(zj,t)+fν​(γ​zj,t)​𝟙(−∞,0)​(zj,t)}𝑓  subscript𝑧  𝑗𝑡𝛾2𝛾1𝛾subscript𝑓𝜈subscript𝑧  𝑗𝑡𝛾subscript10subscript𝑧  𝑗𝑡subscript𝑓𝜈𝛾subscript𝑧  𝑗𝑡subscript10subscript𝑧  𝑗𝑡f(z\_{j,t};\gamma)=\frac{2}{\gamma+\frac{1}{\gamma}}\left\{f\_{\nu}\left(\frac{z\_{j,t}}{\gamma}\right)\mathbbm{1}\_{[0,\infty)}(z\_{j,t})+f\_{\nu}(\gamma z\_{j,t})\mathbbm{1}\_{(-\infty,0)}(z\_{j,t})\right\} |  |

where γ𝛾\gamma is a skew parameter, and fνsubscript𝑓𝜈f\_{\nu} is the density of the t𝑡t distribution with ν𝜈\nu degree of freedom.

Step 2. Finding the best fitting copula.

Among the copulas, we find one with the best fit in Table [2](#S4.T2 "Table 2 ‣ 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") with empirical marginal distributions of Rtℓsuperscriptsubscript𝑅𝑡ℓR\_{t}^{\ell}. We use an ML estimation method, that is,

|  |  |  |
| --- | --- | --- |
|  | θi=argmaxθ​∑t=ii+dln⁡c​(u^t,v^t;θ)subscript𝜃𝑖subscriptargmax𝜃superscriptsubscript𝑡𝑖𝑖𝑑𝑐subscript^𝑢𝑡subscript^𝑣𝑡𝜃\theta\_{i}=\mathrm{argmax}\_{\theta}\sum\_{t=i}^{i+d}\ln c(\hat{u}\_{t},\hat{v}\_{t};\theta) |  |

where c​(⋅,⋅;θ)𝑐⋅⋅𝜃c(\cdot,\cdot;\theta) is a copula density obtained by ∂2C​(u,v;θ)/∂u​∂vsuperscript2𝐶𝑢𝑣𝜃𝑢𝑣\partial^{2}C(u,v;\theta)/\partial u\partial v, u^tsubscript^𝑢𝑡\hat{u}\_{t}, and v^tsubscript^𝑣𝑡\hat{v}\_{t} are samples transformed from observations Rtℓsuperscriptsubscript𝑅𝑡ℓR\_{t}^{\ell} by their empirical distributions obtained in step (1). To estimate θisubscript𝜃𝑖\theta\_{i}, d𝑑d days of samples (u^t,v^t)subscript^𝑢𝑡subscript^𝑣𝑡(\hat{u}\_{t},\hat{v}\_{t}) are used.

Step 3. Computing Δ​CoVaRΔCoVaR\Delta\text{CoVaR}.

We compute the time-varying Δ​CoVaRtΔsubscriptCoVaR𝑡\Delta\text{CoVaR}\_{t} with the best fitting copula obtained in step (2) and marginal distributions in step (1), as stated in Proposition [4](#Thmtheorem4 "Proposition 4. ‣ 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").
To quantify the systemic impact of an asset price return on another asset price return, we compute the β𝛽\beta-quantile
CoVaRβ,t1|2superscriptsubscriptCoVaR

𝛽𝑡conditional12\text{CoVaR}\_{\beta,t}^{1|2} and CoVaRβ,t2|1superscriptsubscriptCoVaR

𝛽𝑡conditional21\text{CoVaR}\_{\beta,t}^{2|1} that are defined by

|  |  |  |
| --- | --- | --- |
|  | ℙ​(Rt1≤CoVaRβ,t1|2|Rt2≤VaRα,t2)=β​and​ℙ​(Rt2≤CoVaRβ,t2|1|Rt1≤VaRα,t1)=β,ℙsuperscriptsubscript𝑅𝑡1conditionalsuperscriptsubscriptCoVaR  𝛽𝑡conditional12superscriptsubscript𝑅𝑡2superscriptsubscriptVaR  𝛼𝑡2𝛽andℙsuperscriptsubscript𝑅𝑡2conditionalsuperscriptsubscriptCoVaR  𝛽𝑡conditional21superscriptsubscript𝑅𝑡1superscriptsubscriptVaR  𝛼𝑡1𝛽\mathbb{P}\left(R\_{t}^{1}\leq\text{CoVaR}\_{\beta,t}^{1|2}|R\_{t}^{2}\leq\text{VaR}\_{\alpha,t}^{2}\right)=\beta\,\,\text{and}\,\,\mathbb{P}\left(R\_{t}^{2}\leq\text{CoVaR}\_{\beta,t}^{2|1}|R\_{t}^{1}\leq\text{VaR}\_{\alpha,t}^{1}\right)=\beta, |  |

respectively.
Then, we compute CoVaRβ,t1|2,α=0.5superscriptsubscriptCoVaR

𝛽𝑡conditional1

2𝛼0.5\text{CoVaR}\_{\beta,t}^{1|2,\alpha=0.5} and CoVaRβ,t2|1,α=0.5superscriptsubscriptCoVaR

𝛽𝑡conditional2

1𝛼0.5\text{CoVaR}\_{\beta,t}^{2|1,\alpha=0.5} .

To implement the first term of Δ​CoVaRΔCoVaR\Delta\text{CoVaR} in Proposition [4](#Thmtheorem4 "Proposition 4. ‣ 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach"), the numerical inversion is needed for the Gaussian and Student t𝑡t copulas.
For the Gumbel and Clayton copulas with generator ψ𝜓\psi, Cα−1subscriptsuperscript𝐶1𝛼C^{-1}\_{\alpha} can be easily derived in an explicit form as
ψ−1​(ψ​(x)−ψ​(α))superscript𝜓1𝜓𝑥𝜓𝛼\psi^{-1}(\psi(x)-\psi(\alpha)) for x∈(0,α)𝑥0𝛼x\in(0,\alpha).
Thus, ([33](#A2.E33 "In Appendix B Proof of Proposition 4 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) is written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | CoVaRβ,t1|2=FRt1−1​(ψ−1​(ψ​(α​β)−ψ​(α))),superscriptsubscriptCoVaR  𝛽𝑡conditional12subscriptsuperscript𝐹1superscriptsubscript𝑅𝑡1superscript𝜓1𝜓𝛼𝛽𝜓𝛼\text{CoVaR}\_{\beta,t}^{1|2}=F^{-1}\_{R\_{t}^{1}}\left(\psi^{-1}(\psi(\alpha\beta)-\psi(\alpha))\right), |  | (22) |

where α𝛼\alpha and β𝛽\beta are the given levels.

Next, for the second term of Δ​CoVaRΔCoVaR\Delta\text{CoVaR} in Proposition [4](#Thmtheorem4 "Proposition 4. ‣ 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach"), computing the conditional copula function ζα​(u)subscript𝜁𝛼𝑢\zeta\_{\alpha}(u) with a given level α𝛼\alpha is required as defined in ([16](#S4.E16 "In Proposition 4. ‣ 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")).
Depending on a choice of copulas, the functions ζα​(u)subscript𝜁𝛼𝑢\zeta\_{\alpha}(u) are obtained as analytic forms, which are derived by Aas
et al. ([2009](#bib.bib1)) and Schepsmeier and
Stöber ([2014](#bib.bib57)), as follows.

* •

  Gaussian copula:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ζα​(u)=Φ​(Φ−1​(u)−θ​Φ−1​(α)1−θ2)subscript𝜁𝛼𝑢ΦsuperscriptΦ1𝑢𝜃superscriptΦ1𝛼1superscript𝜃2\zeta\_{\alpha}(u)=\Phi\left(\frac{\Phi^{-1}(u)-\theta\Phi^{-1}(\alpha)}{\sqrt{1-\theta^{2}}}\right) |  | (23) |
* •

  Student t𝑡t copula with the degree of freedom ν𝜈\nu:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ζα​(u)=tν+1​(tν−1​(u)−θ​tν−1​(α)(ν+[tν−1​(α)]2)​(1−θ2)/(ν+1))subscript𝜁𝛼𝑢subscript𝑡𝜈1superscriptsubscript𝑡𝜈1𝑢𝜃superscriptsubscript𝑡𝜈1𝛼𝜈superscriptdelimited-[]superscriptsubscript𝑡𝜈1𝛼21superscript𝜃2𝜈1\zeta\_{\alpha}(u)=t\_{\nu+1}\left(\frac{t\_{\nu}^{-1}(u)-\theta t\_{\nu}^{-1}(\alpha)}{\sqrt{\left(\nu+[t\_{\nu}^{-1}(\alpha)]^{2}\right)(1-\theta^{2})/(\nu+1)}}\right) |  | (24) |
* •

  Gumbel copula: for x=(−ln⁡u)θ𝑥superscript𝑢𝜃x=(-\ln u)^{\theta} and y=(−ln⁡α)θ𝑦superscript𝛼𝜃y=(-\ln\alpha)^{\theta}

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ζα​(u)=−exp⁡(−(x+y)1θ)⋅(x+y)1θ−1⋅yα​ln⁡αsubscript𝜁𝛼𝑢⋅superscript𝑥𝑦1𝜃superscript𝑥𝑦1𝜃1𝑦𝛼𝛼\zeta\_{\alpha}(u)=-\frac{\exp\left(-(x+y)^{\frac{1}{\theta}}\right)\cdot\left(x+y\right)^{\frac{1}{\theta}-1}\cdot y}{\alpha\ln\alpha} |  | (25) |
* •

  Clayton copula

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ζα​(u)=α−θ−1⋅(u−θ+α−θ−1)−1−1θsubscript𝜁𝛼𝑢⋅superscript𝛼𝜃1superscriptsuperscript𝑢𝜃superscript𝛼𝜃111𝜃\zeta\_{\alpha}(u)=\alpha^{-\theta-1}\cdot\left(u^{-\theta}+\alpha^{-\theta}-1\right)^{-1-\frac{1}{\theta}} |  | (26) |

Dependence parameter θ𝜃\theta is the value estimated in step (2), and the level of α𝛼\alpha is chosen as the median (i.e., α=0.5𝛼0.5\alpha=0.5).

By conducting the three-step procedure described above, we compute the time-varying Δ​CoVaRΔCoVaR\Delta\text{CoVaR}’s.
Then, we compare them with the calibrated parameters from the proposed model in Section 2 to examine the consistency of systemic risk measures for high frequency data.

## Appendix B Proof of Proposition [4](#Thmtheorem4 "Proposition 4. ‣ 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")

As defined in ([17](#S4.E17 "In Proposition 4. ‣ 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")), computing Δ​CoVaRΔCoVaR\Delta\text{CoVaR} consists of determining two types of CoVaR specified in ([15](#S4.E15 "In 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) and ([14](#S4.E14 "In 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")). Each part is derived in the following step (i) and (ii).

(i) The CoVaR defined in ([14](#S4.E14 "In 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")).

It can be computed by using the property of a copula function.
Then ([14](#S4.E14 "In 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζq​(FRtj​(CoVaRβ,td|j,α=q))=β.subscript𝜁𝑞subscript𝐹superscriptsubscript𝑅𝑡𝑗superscriptsubscriptCoVaR  𝛽𝑡conditional𝑑  𝑗𝛼𝑞𝛽\zeta\_{q}\left(F\_{R\_{t}^{j}}\left(\text{CoVaR}\_{\beta,t}^{d|j,\alpha=q}\right)\right)=\beta. |  | (27) |

Thus, the CoVaR is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | CoVaRβ,ti|j,α=q=FRtj−1​(ζq−1​(β)).superscriptsubscriptCoVaR  𝛽𝑡conditional𝑖  𝑗𝛼𝑞superscriptsubscript𝐹superscriptsubscript𝑅𝑡𝑗1subscriptsuperscript𝜁1𝑞𝛽\text{CoVaR}\_{\beta,t}^{i|j,\alpha=q}=F\_{R\_{t}^{j}}^{-1}\left(\zeta^{-1}\_{q}(\beta)\right). |  | (28) |

(ii) The CoVaR defined in ([15](#S4.E15 "In 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")).

In this case, the quantile value of a conditional distribution, or, alternatively, of an unconditional bivariate distribution is needed if we express in ([15](#S4.E15 "In 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(Rti≤CoVaRβ,ti|j,Rtj≤VaRα,tj)ℙ​(Rtj≤VaRα,tj)=β.ℙformulae-sequencesuperscriptsubscript𝑅𝑡𝑖superscriptsubscriptCoVaR  𝛽𝑡conditional𝑖𝑗superscriptsubscript𝑅𝑡𝑗superscriptsubscriptVaR  𝛼𝑡𝑗ℙsuperscriptsubscript𝑅𝑡𝑗superscriptsubscriptVaR  𝛼𝑡𝑗𝛽\frac{\mathbb{P}\left(R\_{t}^{i}\leq\text{CoVaR}\_{\beta,t}^{i|j},R\_{t}^{j}\leq\text{VaR}\_{\alpha,t}^{j}\right)}{\mathbb{P}(R\_{t}^{j}\leq\text{VaR}\_{\alpha,t}^{j})}=\beta. |  | (29) |

Given that ℙ​(Rtj≤VaRα,tj)=αℙsuperscriptsubscript𝑅𝑡𝑗superscriptsubscriptVaR

𝛼𝑡𝑗𝛼\mathbb{P}(R\_{t}^{j}\leq\text{VaR}\_{\alpha,t}^{j})=\alpha, the CoVaR in ([29](#A2.E29 "In Appendix B Proof of Proposition 4 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) can be expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(Rti≤CoVaRβ,ti|j,Rtj≤VaRα,tj)=α​β.ℙformulae-sequencesuperscriptsubscript𝑅𝑡𝑖superscriptsubscriptCoVaR  𝛽𝑡conditional𝑖𝑗superscriptsubscript𝑅𝑡𝑗superscriptsubscriptVaR  𝛼𝑡𝑗𝛼𝛽\mathbb{P}\left(R\_{t}^{i}\leq\text{CoVaR}\_{\beta,t}^{i|j},R\_{t}^{j}\leq\text{VaR}\_{\alpha,t}^{j}\right)=\alpha\beta. |  | (30) |

Here, the form ([29](#A2.E29 "In Appendix B Proof of Proposition 4 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) can be expressed in terms of the joint distribution function of Rtisuperscriptsubscript𝑅𝑡𝑖R\_{t}^{i} and Rtjsuperscriptsubscript𝑅𝑡𝑗R\_{t}^{j}, FRti,Rtjsubscript𝐹

superscriptsubscript𝑅𝑡𝑖superscriptsubscript𝑅𝑡𝑗F\_{R\_{t}^{i},R\_{t}^{j}}, as

|  |  |  |  |
| --- | --- | --- | --- |
|  | FRti,Rtj​(CoVaRβ,ti|j,VaRα,tj)=α​β,subscript𝐹  superscriptsubscript𝑅𝑡𝑖superscriptsubscript𝑅𝑡𝑗superscriptsubscriptCoVaR  𝛽𝑡conditional𝑖𝑗superscriptsubscriptVaR  𝛼𝑡𝑗𝛼𝛽F\_{R\_{t}^{i},R\_{t}^{j}}\left(\text{CoVaR}\_{\beta,t}^{i|j},\text{VaR}\_{\alpha,t}^{j}\right)=\alpha\beta, |  | (31) |

and that, according to Sklar’s theorem (Sklar, [1959](#bib.bib59)), the joint distribution function of two continuous variables can be expressed in terms of a copula function.
Hence, ([31](#A2.E31 "In Appendix B Proof of Proposition 4 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(u,v)=α​β,𝐶𝑢𝑣𝛼𝛽C(u,v)=\alpha\beta, |  | (32) |

where C​(⋅,⋅)𝐶⋅⋅C(\cdot,\cdot) is a copula function, u=FRti​(CoVaRβ,ti|j)𝑢subscript𝐹superscriptsubscript𝑅𝑡𝑖superscriptsubscriptCoVaR

𝛽𝑡conditional𝑖𝑗u=F\_{R\_{t}^{i}}(\text{CoVaR}\_{\beta,t}^{i|j}) and
v=FRtj​(VaRα,tj)𝑣subscript𝐹superscriptsubscript𝑅𝑡𝑗superscriptsubscriptVaR

𝛼𝑡𝑗v=F\_{R\_{t}^{j}}(\text{VaR}\_{\alpha,t}^{j}), and where FRtisubscript𝐹superscriptsubscript𝑅𝑡𝑖F\_{R\_{t}^{i}} and FRtjsubscript𝐹superscriptsubscript𝑅𝑡𝑗F\_{R\_{t}^{j}} are the marginal distribution function of Rtisuperscriptsubscript𝑅𝑡𝑖R\_{t}^{i} and Rtjsuperscriptsubscript𝑅𝑡𝑗R\_{t}^{j}, respectively.
Given its copula representation in ([32](#A2.E32 "In Appendix B Proof of Proposition 4 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")), the CoVaR can be computed from that equation through copulas in a two-step procedure.
First, we obtain the value of u=FRti​(CoVaRβ,ti|j)𝑢subscript𝐹superscriptsubscript𝑅𝑡𝑖superscriptsubscriptCoVaR

𝛽𝑡conditional𝑖𝑗u=F\_{R\_{t}^{i}}(\text{CoVaR}\_{\beta,t}^{i|j}).
Since C​(u,v)=α​β𝐶𝑢𝑣𝛼𝛽C(u,v)=\alpha\beta, where α,β

𝛼𝛽\alpha,\beta, and v𝑣v are given (note that v=α𝑣𝛼v=\alpha), from the copula function specification we can solve to determine the value of u𝑢u.
Next, taking u𝑢u, we can obtain the CoVaR value as the quantile of distribution Rtisuperscriptsubscript𝑅𝑡𝑖R\_{t}^{i}, with a cumulative probability equal to u𝑢u, by inverting the marginal distribution function of Rtisuperscriptsubscript𝑅𝑡𝑖R\_{t}^{i}: CoVaRβ,ti|j=FRti−1​(u)superscriptsubscriptCoVaR

𝛽𝑡conditional𝑖𝑗subscriptsuperscript𝐹1superscriptsubscript𝑅𝑡𝑖𝑢\text{CoVaR}\_{\beta,t}^{i|j}=F^{-1}\_{R\_{t}^{i}}(u).
Letting Cα−1​(⋅)superscriptsubscript𝐶𝛼1⋅C\_{\alpha}^{-1}(\cdot) be the inverse of Cα:x→C​(⋅,α):subscript𝐶𝛼→𝑥𝐶⋅𝛼C\_{\alpha}:x\rightarrow C(\cdot,\alpha), then the CoVaR can be expressed as an analytic form

|  |  |  |  |
| --- | --- | --- | --- |
|  | CoVaRβ,ti|j=FRti−1​(Cα−1​(α​β)).superscriptsubscriptCoVaR  𝛽𝑡conditional𝑖𝑗subscriptsuperscript𝐹1superscriptsubscript𝑅𝑡𝑖subscriptsuperscript𝐶1𝛼𝛼𝛽\text{CoVaR}\_{\beta,t}^{i|j}=F^{-1}\_{R\_{t}^{i}}\left(C^{-1}\_{\alpha}(\alpha\beta)\right). |  | (33) |

## Appendix C Selection of the best fitting copula in Section [4.2](#S4.SS2 "4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")

We estimated marginal distributions for each return series of CL and RB futures prices using the ARMA(1,1)-TGARCH(1,1) model with skewed-t𝑡t distribution.
Then, we transformed the daily return series into uniform variables such that u^t=F^1​(xt)subscript^𝑢𝑡subscript^𝐹1subscript𝑥𝑡\hat{u}\_{t}=\hat{F}\_{1}(x\_{t}) and v^t=F^2​(yt)subscript^𝑣𝑡subscript^𝐹2subscript𝑦𝑡\hat{v}\_{t}=\hat{F}\_{2}(y\_{t}) where F^isubscript^𝐹𝑖\hat{F}\_{i} is the estimated distribution and xt,yt

subscript𝑥𝑡subscript𝑦𝑡x\_{t},y\_{t} are the standardized returns of Rt1,Rt2

superscriptsubscript𝑅𝑡1superscriptsubscript𝑅𝑡2R\_{t}^{1},R\_{t}^{2}, respectively.
Figure [15](#A3.F15 "Figure 15 ‣ Appendix C Selection of the best fitting copula in Section 4.2 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") displays the scatter plot of 2,000 days of pseudo-sample observations, u^t,v^t

subscript^𝑢𝑡subscript^𝑣𝑡\hat{u}\_{t},\hat{v}\_{t} under the marginal distribution model.

![Refer to caption](/html/2012.04181/assets/x32.png)


Figure 15: Scatter plot of u^t,v^t

subscript^𝑢𝑡subscript^𝑣𝑡\hat{u}\_{t},\hat{v}\_{t} using the ARMA(1,1)-TGARCH(1,1) model with skewed-t𝑡t distribution

We extracted dependence parameters of the copula functions reported in Table [2](#S4.T2 "Table 2 ‣ 4.2 A CoVaR-copula approach and its implementation ‣ 4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") using the consecutive d𝑑d days of series pairs.
Figure [18](#A5.F18 "Figure 18 ‣ Appendix E Figures related to Section 4 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") (Appendix [E](#A5 "Appendix E Figures related to Section 4 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")) illustrates the dynamics of the estimated parameter θ𝜃\theta of CL and RB futures prices using given copulas with the standard error during the test period from 2007 to 2016.

To select the best fitting copula among them, we compare different copula specifications using the commonly used error measures of Akaike information criterion (AIC) and Bayesian information criterion (BIC) in the model selection based on an ML estimation.
Figure [16](#A3.F16 "Figure 16 ‣ Appendix C Selection of the best fitting copula in Section 4.2 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") shows the results of AIC and BIC values from estimations of the Gaussian, Student t𝑡t, Gumbel, and Clayton copulas over time.
We find that the Student t𝑡t copula provides the lowest values by both measures on the entire timeline.

![Refer to caption](/html/2012.04181/assets/x33.png)

![Refer to caption](/html/2012.04181/assets/x34.png)

Figure 16: Results of AIC (left) and BIC (right) measures for Gaussian, Student t𝑡t, Gumbel, and Clayton copulas from January 2007 to December 2016

In addition, the degrees of freedom ν𝜈\nu for the Student t𝑡t copula are estimated over time and displayed in Figure [19](#A5.F19 "Figure 19 ‣ Appendix E Figures related to Section 4 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") (Appendix [E](#A5 "Appendix E Figures related to Section 4 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")), which provides evidence of fat tails of the joint distribution of the return pair of CL and RB futures prices.
The empirical result indicates the existence of positive and symmetric dependence with fat tails between the two futures prices.
The extent of the overall positive dependency and extreme tail dependency has varied over time.

## Appendix D More tests for calibration in Section [3](#S3 "3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")

Some of selected estimates are presented in Table [3](#A4.T3 "Table 3 ‣ Appendix D More tests for calibration in Section 3 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")
with the numerically computed standard errors in the parentheses.
In this period of time, the self-exciting term α1​ssubscript𝛼1𝑠\alpha\_{1s} of CL is close to zero and all other parameters are significant.
Since we performed non-constraint parameter estimation, sometimes negative αssubscript𝛼𝑠\alpha\_{s} are observed,
but it is better to be considered as zero by the Hawkes-based model definition.
In general, μ𝜇\mu in CL is larger than that in RB implying larger trade frequency in CL
and β𝛽\beta in RB is larger than that in CL implying longer persistence in RB.

Table 3: Estimates for CL (left) and RB (right) under the Hawkes-based model without the flocking-related parameters

|  | WTI crude oil | | | | RBOB gasoline | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Date/Maturity | μ1subscript𝜇1\mu\_{1} | α1​ssubscript𝛼1𝑠\alpha\_{1s} | α1​csubscript𝛼1𝑐\alpha\_{1c} | β1subscript𝛽1\beta\_{1} | μ2subscript𝜇2\mu\_{2} | α2​ssubscript𝛼2𝑠\alpha\_{2s} | α2​csubscript𝛼2𝑐\alpha\_{2c} | β2subscript𝛽2\beta\_{2} |
| 2016-03-16 | 0.0780 | 0.0400 | 0.3710 | 0.5120 | 0.0577 | 0.3763 | 0.2001 | 0.9109 |
| March 2016 | (0.0025) | (0.0050) | (0.0122) | (0.0176) | (0.0017) | (0.0183) | (0.0110) | (0.0439) |
| 2016-04-15 | 0.0731 | 0.0128 | 0.3455 | 0.4827 | 0.0593 | 0.5337 | 0.2126 | 1.3083 |
| April 2016 | (0.0025) | (0.0044) | (0.0119) | (0.0184) | (0.0014) | (0.0204) | (0.0118) | (0.0446) |
| 2016-05-17 | 0.0872 | -0.0206 | 0.3527 | 0.5106 | 0.0568 | 0.4200 | 0.2712 | 1.1314 |
| May 2016 | (0.0025) | (0.0037) | (0.0112) | (0.0195) | (0.0015) | (0.0204) | (0.0144) | (0.0510) |
| 2016-06-16 | 0.1001 | -0.0033 | 0.4315 | 0.6022 | 0.0574 | 0.3405 | 0.1954 | 0.8668 |
| June 2016 | (0.0027) | (0.0041) | (0.0124) | (0.0189) | (0.0016) | (0.0151) | (0.0101) | (0.0367) |

The estimates and numerically computed standard errors in parenthesis are presented in Table [4](#A4.T4 "Table 4 ‣ Appendix D More tests for calibration in Section 3 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach").
Note that αi​ssubscript𝛼𝑖𝑠\alpha\_{is} and αi​csubscript𝛼𝑖𝑐\alpha\_{ic} are similar to the estimates in Table [3](#A4.T3 "Table 3 ‣ Appendix D More tests for calibration in Section 3 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") for i=1,2𝑖

12i=1,2,
which means that the additionally introduced αi​nsubscript𝛼𝑖𝑛\alpha\_{in} and αi​wsubscript𝛼𝑖𝑤\alpha\_{iw} do not affect the self/mutually-exciting terms.
The result also shows that αi​nsubscript𝛼𝑖𝑛\alpha\_{in} are close to zero in the selected time period, which means that the price difference for narrowing events does not affect the intensities.
We expand the time range, nonzero positive α1​nsubscript𝛼1𝑛\alpha\_{1n} of CL is also observed,
but overall αi​nsubscript𝛼𝑖𝑛\alpha\_{in} is quite small and close to zero.
In addition, αi​wsubscript𝛼𝑖𝑤\alpha\_{iw} are significant, which means that the price difference widening events
increase the intensities so that the two price processes tend to converge to each other.

Table 4: Estimates for CL (top) and RB (bottom) with the Hawkes flocking model

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | WTI crude oil | | | | | |
| date/maturity | μ1subscript𝜇1\mu\_{1} | α1​nsubscript𝛼1𝑛\alpha\_{1n} | α1​wsubscript𝛼1𝑤\alpha\_{1w} | α1​ssubscript𝛼1𝑠\alpha\_{1s} | α1​csubscript𝛼1𝑐\alpha\_{1c} | β1subscript𝛽1\beta\_{1} |
| 2016-03-16 | 0.0755 | -0.0120 | 0.2265 | 0.0105 | 0.4333 | 0.6079 |
| March 2016 | (0.0039) | (0.0086) | (0.0286) | (0.0053) | (0.0321) | (0.0523) |
| 2016-04-15 | 0.0345 | 0.0046 | 0.1993 | 0.0076 | 0.2992 | 0.4084 |
| April 2016 | (0.0021) | (0.0078) | (0.0118) | (0.0038) | (0.0108) | (0.0160) |
| 2016-05-17 | 0.0670 | -0.0085 | 0.2053 | -0.0318 | 0.3761 | 0.5699 |
| May 2016 | (0.0024) | (0.0069) | (0.0119) | (0.0032) | (0.0121) | (0.0217) |
| 2016-06-16 | 0.0706 | -0.0189 | 0.2748 | -0.0121 | 0.4348 | 0.6142 |
| June 2016 | (0.0026) | (0.0093) | (0.0160) | (0.0032) | (0.0154) | (0.0245) |
|  | RBOB gasoline | | | | | |
| date/maturity | μ2subscript𝜇2\mu\_{2} | α2​nsubscript𝛼2𝑛\alpha\_{2n} | α2​wsubscript𝛼2𝑤\alpha\_{2w} | α2​ssubscript𝛼2𝑠\alpha\_{2s} | α2​csubscript𝛼2𝑐\alpha\_{2c} | β2subscript𝛽2\beta\_{2} |
| 2016-03-16 | 0.0499 | -0.0109 | 0.1335 | 0.4384 | 0.2306 | 1.2513 |
| March, 2016 | (0.0037) | (0.0083) | (0.0269) | (0.1005) | (0.0471) | (0.3109) |
| 2016-04-15 | 0.0403 | 0.0098 | 0.1719 | 0.4450 | 0.1836 | 1.5166 |
| April, 2016 | (0.0013) | (0.0073) | (0.0112) | (0.0212) | (0.0125) | (0.0598) |
| 2016-05-17 | 0.0413 | 0.0347 | 0.2229 | 0.4555 | 0.3085 | 1.4429 |
| May, 2016 | (0.0013) | (0.0096) | (0.0121) | (0.0200) | (0.0151) | (0.0492) |
| 2016-06-16 | 0.0348 | 0.0186 | 0.1302 | 0.2950 | 0.1882 | 0.9146 |
| June, 2016 | (0.0014) | (0.0065) | (0.0077) | (0.0133) | (0.0096) | (0.0352) |

By data visualization, we confirm the previous discussion.
For the graph, the selected maturity for the futures is February 2016 and estimates are computed on a daily basis over the sample period from January 4 to February 22, 2016.
Figure [7](#S3.F7 "Figure 7 ‣ 3.4 Calibration ‣ 3 Application to Empirical Data ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") compares αnsubscript𝛼𝑛\alpha\_{n} and αwsubscript𝛼𝑤\alpha\_{w}.
For both CL and RB, the estimated αnsubscript𝛼𝑛\alpha\_{n} are almost zero, but αwsubscript𝛼𝑤\alpha\_{w} are far from zero
and αwsubscript𝛼𝑤\alpha\_{w} in CL is larger than that in RB.

Figure [17](#A4.F17 "Figure 17 ‣ Appendix D More tests for calibration in Section 3 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach") compares αssubscript𝛼𝑠\alpha\_{s} and αcsubscript𝛼𝑐\alpha\_{c}.
For CL, αssubscript𝛼𝑠\alpha\_{s} are close to zero and for other cases, αcsubscript𝛼𝑐\alpha\_{c} in CL and αssubscript𝛼𝑠\alpha\_{s}, αcsubscript𝛼𝑐\alpha\_{c} in RB, the estimates are significantly positive.
In addition, αssubscript𝛼𝑠\alpha\_{s} is less than αcsubscript𝛼𝑐\alpha\_{c} in CL, but αssubscript𝛼𝑠\alpha\_{s} is greater than αcsubscript𝛼𝑐\alpha\_{c} in RB over the sample period.

![Refer to caption](/html/2012.04181/assets/CL_alpha1sc.png)

![Refer to caption](/html/2012.04181/assets/RB_alpha2sc.png)

Figure 17: Comparison of αssubscript𝛼𝑠\alpha\_{s} and αcsubscript𝛼𝑐\alpha\_{c} for CL (left) and RB (right) futures prices with maturity in February 2016

In Table [5](#A4.T5 "Table 5 ‣ Appendix D More tests for calibration in Section 3 ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach"), for each maturity,
we calculated the averages of estimates on a daily basis using 20 days’ data.
In this result, we also observe that αi​nsubscript𝛼𝑖𝑛\alpha\_{in} are close to zero for all maturities.

Table 5: Means of estimates for CL and RB

|  | WTI crude oil | | | | RBOB gasoline | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| maturity | α1​nsubscript𝛼1𝑛\alpha\_{1n} | α1​wsubscript𝛼1𝑤\alpha\_{1w} | α1​ssubscript𝛼1𝑠\alpha\_{1s} | α1​csubscript𝛼1𝑐\alpha\_{1c} | α2​nsubscript𝛼2𝑛\alpha\_{2n} | α2​wsubscript𝛼2𝑤\alpha\_{2w} | α2​ssubscript𝛼2𝑠\alpha\_{2s} | α2​csubscript𝛼2𝑐\alpha\_{2c} |
| 2016-01 | -0.0229 | 0.1828 | 0.0003 | 0.3919 | 0.0197 | 0.1683 | 0.5835 | 0.2900 |
| 2016-02 | -0.0332 | 0.2782 | 0.0106 | 0.4662 | -0.0059 | 0.1290 | 0.4887 | 0.2605 |
| 2016-03 | -0.0237 | 0.2481 | -0.0129 | 0.4621 | -0.0059 | 0.1321 | 0.4625 | 0.2491 |
| 2016-04 | -0.0234 | 0.2161 | -0.0266 | 0.4359 | -0.0020 | 0.1517 | 0.4600 | 0.2333 |
| 2016-05 | -0.0229 | 0.2497 | -0.0233 | 0.4611 | -0.0026 | 0.1480 | 0.4570 | 0.2577 |
| 2016-06 | -0.0187 | 0.1725 | -0.0250 | 0.4136 | 0.0174 | 0.1618 | 0.4737 | 0.2731 |
| 2016-07 | -0.0157 | 0.2321 | -0.0199 | 0.4300 | 0.0185 | 0.1872 | 0.4588 | 0.2579 |
| 2016-08 | -0.0205 | 0.2013 | -0.0149 | 0.4707 | 0.0026 | 0.1787 | 0.4498 | 0.2497 |
| 2016-09 | -0.0145 | 0.2223 | -0.0178 | 0.4870 | -0.0015 | 0.1834 | 0.4574 | 0.2237 |
| 2016-10 | -0.0115 | 0.2205 | -0.0222 | 0.4970 | 0.0005 | 0.1738 | 0.4053 | 0.2212 |
| 2016-11 | -0.0137 | 0.2123 | -0.0164 | 0.4798 | -0.0049 | 0.1576 | 0.4033 | 0.2123 |
| 2016-12 | -0.0073 | 0.2756 | -0.0242 | 0.4879 | 0.0028 | 0.1363 | 0.4169 | 0.2217 |

## Appendix E Figures related to Section [4](#S4 "4 Systemic Risk in Market Microstructure ‣ Systemic Risk in Market Microstructure of Crude Oil and Gasoline Futures Prices: A Hawkes Flocking Model Approach")

![Refer to caption]()

![Refer to caption](/html/2012.04181/assets/x36.png)

![Refer to caption](/html/2012.04181/assets/x37.png)

![Refer to caption](/html/2012.04181/assets/x38.png)

Figure 18: The evolution of the estimated dependence parameter θ𝜃\theta of CL and RB futures prices using Gaussian copula (top, right), Student t𝑡t copula (top, left), Gumbel copula (bottom, left), and Clayton copula (bottom, right) with the standard error (red dotted line) from January 2007 to December 2016

![Refer to caption](/html/2012.04181/assets/t_nu.png)


Figure 19: The evolution of the estimated degree of freedom parameter ν𝜈\nu in the Student t𝑡t copula for the return pairs of CL and RB futures prices from January 2007 to December 2016



![Refer to caption](/html/2012.04181/assets/x39.png)

![Refer to caption](/html/2012.04181/assets/x40.png)

![Refer to caption](/html/2012.04181/assets/x41.png)

![Refer to caption](/html/2012.04181/assets/x42.png)

Figure 20: Illustration of time-varying one-day CoVaR95%,t1|2subscriptsuperscriptCoVaRconditional12

percent95𝑡\mathrm{CoVaR}^{1|2}\_{95\%,t} (top, left), Δ​CoVaR95%,t2|1ΔsubscriptsuperscriptCoVaRconditional21

percent95𝑡\Delta\mathrm{CoVaR}^{2|1}\_{95\%,t} (top, right),
CoVaR95%,t1|2,α=50%subscriptsuperscriptCoVaRconditional1

2𝛼percent50

percent95𝑡\mathrm{CoVaR}^{1|2,\alpha=50\%}\_{95\%,t} (bottom, left), and Δ​CoVaR95%,t2|1,α=50%ΔsubscriptsuperscriptCoVaRconditional2

1𝛼percent50

percent95𝑡\Delta\mathrm{CoVaR}^{2|1,\alpha=50\%}\_{95\%,t} (bottom, right)
where Rt1superscriptsubscript𝑅𝑡1R\_{t}^{1} and Rt2superscriptsubscript𝑅𝑡2R\_{t}^{2} are given by the CL and RB daily returns at time t𝑡t, respectively, from January 2007 to December 2016

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/2012.04181)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2012.04181)
[View original  
on arXiv](https://arxiv.org/abs/2012.04181)[►](javascript: void(0))