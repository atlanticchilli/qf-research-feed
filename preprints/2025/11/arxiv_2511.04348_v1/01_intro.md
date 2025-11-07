---
authors:
- Domenico delli Gatti
- Filippo Gusella
- Giorgio Ricchiuti
doc_id: arxiv:2511.04348v1
family_id: arxiv:2511.04348
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in
  a Nonlinear Setting'
url_abs: http://arxiv.org/abs/2511.04348v1
url_html: https://arxiv.org/html/2511.04348v1
venue: arXiv q-fin
version: 1
year: 2025
---


Domenico Delli Gatti
  
CLE, Università Cattolica del Sacro Cuore, Milano
  
Filippo Gusella
  
CLE, Università Cattolica del Sacro Cuore, Milano
  
Università degli Studi di Firenze
  
New York University in Florence
  
Giorgio Ricchiuti
  
Università degli Studi di Firenze
  
CLE, Università Cattolica del Sacro Cuore, Milano

###### Abstract

This paper investigates Minsky’s cycles by extending the paper of stockhammer2019short with a nonlinear model to capture possible local real-financial endogenous cycles. We trace nonlinear regime changes and check the presence of Minsky cycles from the 1970s to 2020 for the USA, France, Germany, Canada, Australia, and the UK, linking the GDP with corporate debt, interest rate, and household debt. When considering corporate debt, the results reveal real-financial endogenous cycles in all countries, except Australia, and across all countries when interest rates are included. We find evidence for an interaction mechanism between household debt and GDP only for the USA and the UK. These findings underscore the importance of nonlinear regime transitions in empirically assessing Minsky’s theory.

Keywords: Minsky, real-financial cycles, Markov switching

Jel codes: E32, G01

## 1  Introduction

The role of the financial system lies at the heart of macroeconomic analysis. Understanding how financial variables evolve and interact with real variables, driving economic growth, but also episodes of instability, has increasingly attracted the attention of economists. Among the theories that highlight this centrality, Hyman Minsky’s financial instability hypothesis (FIH) stands out as particularly influential (minsky1978financial). This theory emphasizes the crucial role that financial factors play in shaping the dynamics of business cycles: As real activity expands, it gradually creates a financially fragile environment, subsequently casting a negative influence on the real economy. This mechanism is at the core of Minsky’s hypothesis and provides a framework for understanding the real-financial interaction.

The literature on Minsky’s theory is largely dominated by theoretical contributions with limited empirical validation. From a theoretical point of view, the interaction mechanism à la Minsky has been analyzed in a wide and heterogeneous literature (see, e.g. nikolaidi2018minsky, for an overview). This body of work has been formalized through different theoretical frameworks, including nonlinear dynamic macroeconomic models, agent-based models, and stock-flow consistent models. Among them, some models emphasize the role of the interest rate in relation to the dynamics of corporate or household debt (see, among others, semmler1987macroeconomic; lima2007macrodynamics; fazzari2008cash; gatti2010financial; riccetti2013leveraged; riccetti2015agent; dafermos2018debt; reissl2020minsky; kohler2019exchange), while another strand highlights the destabilizing dynamics of asset prices (see, for example, taylor1985minsky; gatti1990financial; ryoo2010long; chiarella2011financial; riccetti2016stock; alessia2021ir; gusella2025financial). Despite these differences, the common idea is that financial fragility builds endogenously in periods of expansion, sowing the seeds for subsequent economic recession.

From an empirical perspective, only a limited number of studies have attempted to investigate the instability hypothesis. For instance, at the micro level, some works aim to discern hedge, speculative, and Ponzi states that characterize a firm’s financial condition in various countries and economic sectors (schroeder2009defining; nishi2012dynamic; mulligan2013sectoral; davis2019empirical).111The financial instability hypothesis originally focused on firms’ investment and financing behavior. In Minsky’s framework, firms move from hedge positions - where cash flows are sufficient to meet debt obligations - to speculative positions - where refinancing becomes necessary - and finally to Ponzi positions, which rely on rising asset prices to service debt; this progressive shift for most firms makes the economy systemically fragile and ultimately leads to financial and economic crises.
Conversely, at the macro level, empirical literature can be broadly grouped into two main strands. A first group interprets macrofinancial fluctuations as the result of exogenous shocks hitting the financial sector, which subsequently propagate to the real economy (kim2016macroeconomic; ma2016financial). In contrast, a more recent contribution by stockhammer2019short, and subsequent studies building on this approach (kohler2022estimating; kohler2023flexible; stockhammer2023debt), adopt an explicitly endogenous perspective, framing the interaction between the financial and real sides within a vector autoregressive (VAR) setting, which allows empirical assessment of the mathematical condition for the existence of endogenous Minskyan cycles.

Despite the distinction between exogenous and endogenous mechanisms as the source of Minskyan cycles, both macro-empirical approaches remain grounded in a linear analytical structure. This hypothesis constrains the ability to capture nonlinear transitions and regime-dependent dynamics. In fact, the linear specification rules out the possibility that different macro-financial dynamics may emerge across distinct time periods, potentially overlooking cyclical patterns that are temporally concentrated. To address these limitations, we extend the paper by stockhammer2019short, introducing a bivariate Markov-switching vector autoregressive model (MS-VAR) that describes the dynamic behavior of economic time series in the presence of possible nonlinear endogenous regime changes (krolzig1997markov; hamilton2020time; hamilton2016macroeconomic). In this framework, we distinguish between two regimes: one involves an interaction mechanism between the real and financial variables, allowing for a possible estimation of Minsky cycles. The other regime, in contrast, assumes no interaction between real and financial variables. This modeling approach allows us to capture the occurrence of real-financial interactions in line with Minsky’s theory within a regime-changing nonlinear context, providing valuable insight into its temporal and local dynamics. In doing so, we contribute to the literature by providing the first empirical implementation of a nonlinear estimation framework explicitly designed to identify Minsky cycles within macrofinancial dynamics. Furthermore, by applying filtering techniques to uncover state dynamics, we can trace regime changes and observe the manifestation of financial instability within specific years. Consequently, one structure, for example, the “Minsky regime” (“No Minsky regime”), may dominate for a specific period until it is replaced by the “No Minsky regime” (“Minsky regime”) when the switching takes place. The time-varying filtering technique, applied across different countries and financial variables, offers a novel comparative perspective on how endogenous instability mechanisms emerge across various institutional and financial environments over different time periods.

Estimation is conducted using data from the USA, France, Germany, Canada, Australia, and the UK from the 1970s to 2020. We consider the gross domestic product as the real variable, while the non-financial corporate debt, the housing debt, and the short-term interest rate are the financial variables. When focusing on corporate debt, the results indicate the presence of local Minsky cycles in all countries, with the sole exception of Australia. When short-term interest rates are incorporated into the analysis, evidence of such interaction mechanisms emerges consistently across all countries examined. In contrast, the relationship between household debt and GDP appears more limited. In this case, significant endogenous Minsky cycles are identified only for the United States and the United Kingdom, suggesting that the macroeconomic relevance of household debt may be more context-dependent and institutionally specific.

The remainder of the paper is structured as follows. Section 2 provides the mathematical framework and the empirical strategy for studying real-financial cycles in a nonlinear estimation context. Section 3 presents the data and the estimation results. Section 4 concludes.

## 2  Methodology

In this section, we introduce the proposed approach for the analysis of real-financial cycles. Based on stockhammer2019short, the mathematical framework is presented in Section 2.1. Then, in Section 2.2, we extend the empirical estimation strategy from a linear to a nonlinear setting.

### 2.1  Minsky cycles

Minsky’s theory suggests the interdependence between real and financial dynamics. The theory can be summarized in the famous sentence *“stability is destabilizing”*. A period of economic expansion, characterized by an increase in GDP, entails an upward shift in debt and risk attitude. As financial fragility grows, a debt overhang or an increase in interest rates is reflected in a decline of the economic expansion (stockhammer2019short).

To formalize the cycle-generating interaction mechanism, the real variable (yty\_{t}) and the financial variable (ftf\_{t}) are integrated into a simple first-order bivariate system of difference equations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | [ytft]=A​[yt−1ft−1],w​i​t​hA=[α1α2β1β2].\left[{\begin{array}[]{\*{20}{c}}{{y\_{t}}}\\ {{f\_{t}}}\end{array}}\right]=A{\left[{\begin{array}[]{\*{20}{c}}{{y\_{t-1}}}\\ {{f\_{t-1}}}\end{array}}\right]\_{,}}\quad\quad with\quad\quad A={\left[{\begin{array}[]{\*{20}{c}}{{\alpha\_{1}}}&{{\alpha\_{2}}}\\ {{\beta\_{1}}}&{{\beta\_{2}}}\end{array}}\right]\_{.}} |  | (1) |

The dynamics of the system is given by the transition equation AA, which describes the evolution of the real and financial variables. Eigenvalue analysis can be performed to investigate the conditions for potential oscillations in a two-dimensional discrete dynamical system.

The eigenvalues λ\lambda of the system satisfy the following characteristic equation:

|  |  |  |
| --- | --- | --- |
|  | det(A−λ​I)=0,\det\left({A-\lambda I}\right)=0, |  |

i.e.:

|  |  |  |
| --- | --- | --- |
|  | det[α1−λα2β1β2−λ]=0.\det\left[{\begin{array}[]{\*{20}{c}}{{\alpha\_{1}}-\lambda}&{{\alpha\_{2}}}\\ {{\beta\_{1}}}&{{\beta\_{2}}-\lambda}\end{array}}\right]=0\_{.} |  |

We obtain:

|  |  |  |
| --- | --- | --- |
|  | (α1−λ)​(β2−λ)−β1​α2=0,\left({{\alpha\_{1}}-\lambda}\right)\left({{\beta\_{2}}-\lambda}\right)-{\beta\_{1}}{\alpha\_{2}}=0, |  |

from which:

|  |  |  |
| --- | --- | --- |
|  | λ2−λ​T​r​(A)−det(A).{\lambda^{2}}-\lambda Tr\left(A\right)-\det\left(A\right). |  |

The roots assume the following form:

|  |  |  |
| --- | --- | --- |
|  | λ1,2=T​r​(A)±T​r​(A)2−4​det(A)2.{\lambda\_{1,2}}=\frac{{Tr\left(A\right)\pm\sqrt{Tr{{\left(A\right)}^{2}}-4\det\left(A\right)}}}{2}. |  |

The condition for oscillations is expressed in terms of the discriminant, which must be negative for the existence of complex eigenvalues. This criterion translates as follows:

|  |  |  |
| --- | --- | --- |
|  | Δ=T​r​(A)2−4​det(A)<0=(α1+β2)2−4​(α1​β2−α2​β1)<0\begin{array}[]{l}\Delta=Tr{\left(A\right)^{2}}-4\det\left(A\right)<0\\ \;\;\;\;={\left({{\alpha\_{1}}+{\beta\_{2}}}\right)^{2}}-4\left({{\alpha\_{1}}{\beta\_{2}}-{\alpha\_{2}}{\beta\_{1}}}\right)<0\\ \end{array} |  |

from which the following condition must be satisfied:

|  |  |  |
| --- | --- | --- |
|  | (α1−β2)2+4​α2​β1<0{\left({{\alpha\_{1}}-{\beta\_{2}}}\right)^{2}}+4{\alpha\_{2}}{\beta\_{1}}<0 |  |

From the previous equation, we can see that the necessary condition for oscillations is α2​β1<0{\alpha\_{2}}{\beta\_{1}}<0. In other words, fluctuations in the system described by Eq. [1](https://arxiv.org/html/2511.04348v1#S2.E1 "In 2.1 Minsky cycles ‣ 2 Methodology ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting") occur only if the interaction between the two variables is such that an increase in one leads to a rise in the second, which then pulls the first down. In Minsky’s vision of financial-real cycles, the usual assumption is that a rise in GDP has a positive effect on financial variables (β1>0{\beta\_{1}}>0), such as interest rates or debt, while an increase in financial variables has a negative effect on the real variable (α2<0{\alpha\_{2}}<0).

### 2.2  The estimation strategy

Building on the theoretical model presented in the previous section, we extend it to a nonlinear context using a Markov Switching Vector Autoregressive (MS-VAR) model. This framework allows the dynamics of the system to evolve across different regimes, governed by a latent state variable, sts\_{t}, which follows a first order discrete-time Markov process. The general form of the MS-VAR model is given by:

|  |  |  |
| --- | --- | --- |
|  | 𝐲t=𝐀​(st)​𝐲t−1+ϵt,\mathbf{y}\_{t}=\mathbf{A}(s\_{t})\mathbf{y}\_{t-1}+\mathbf{\epsilon}\_{t}, |  |

where 𝐲t∈ℝn\mathbf{y}\_{t}\in\mathbb{R}^{n} is the vector variables at time tt, 𝐀​(st)∈ℝn×n\mathbf{A}(s\_{t})\in\mathbb{R}^{n\times n} is the regime-dependent coefficient matrix and ϵt∼N​(0,Σst)\mathbf{\epsilon}\_{t}\sim N(0,\Sigma\_{s\_{t}}) is the vector error term with the variance-covariance matrix Σst∈ℝn×n\Sigma\_{s\_{t}}\in\mathbb{R}^{n\times n}.

With respect to our case, while the baseline model initially accounted for a single regime, it now differentiates between two distinct regimes (i.e., n=2n=2): one representing potential real-financial interaction and another with independent real-financial dynamics, with the absence of cyclical interaction dynamics. In a two-regime MS-VAR model, the system is represented as:

|  |  |  |
| --- | --- | --- |
|  | 𝐲t={𝐀1​𝐲t−1+ϵtif ​st=1​(possible real-financial interaction)𝐀2​𝐲t−1+ϵtif ​st=2​(no real-financial interaction)\mathbf{y}\_{t}=\begin{cases}\mathbf{A}\_{1}\mathbf{y}\_{t-1}+\mathbf{\epsilon}\_{t}&\text{if }s\_{t}=1\ (\text{possible real-financial interaction})\\ \mathbf{A}\_{2}\mathbf{y}\_{t-1}+\mathbf{\epsilon}\_{t}&\text{if }s\_{t}=2\ (\text{no real-financial interaction})\end{cases} |  |

Where:

|  |  |  |
| --- | --- | --- |
|  | 𝐲t=[ytft].\mathbf{y}\_{t}=\begin{bmatrix}y\_{t}\\ f\_{t}\end{bmatrix}\_{.} |  |

The coefficient matrix for regime 1 is:

|  |  |  |
| --- | --- | --- |
|  | 𝐀1=[α1α2β1β2],\mathbf{A}\_{1}=\begin{bmatrix}\alpha\_{1}&\alpha\_{2}\\ \beta\_{1}&\beta\_{2}\end{bmatrix}\_{,} |  |

with the following error term:

|  |  |  |
| --- | --- | --- |
|  | ϵt=[εtφt],ϵt∼N​(0,Σ1).\mathbf{\epsilon}\_{t}=\begin{bmatrix}\varepsilon\_{t}\\ \varphi\_{t}\end{bmatrix},\quad\mathbf{\epsilon}\_{t}\sim N(0,\Sigma\_{1}). |  |

The coefficient matrix for regime 2 is:

|  |  |  |
| --- | --- | --- |
|  | 𝐀2=[ψ100ω2],\mathbf{A}\_{2}=\begin{bmatrix}\psi\_{1}&0\\ 0&\omega\_{2}\end{bmatrix}\_{,} |  |

with the following error term:

|  |  |  |
| --- | --- | --- |
|  | ϵt=[δtρt],ϵt∼N​(0,Σ2).\mathbf{\epsilon}\_{t}=\begin{bmatrix}\delta\_{t}\\ \rho\_{t}\end{bmatrix},\quad\mathbf{\epsilon}\_{t}\sim N(0,\Sigma\_{2})\_{.} |  |

In an extensive stochastic form, we obtain:

|  |  |  |
| --- | --- | --- |
|  | [ytft]={(st)​[α1α2β1β2]​[yt−1ft−1]+[εtφt](possible real-financial cycle) (st)​[ψ100ω2]​[yt−1ft−1]+[δtρt](no real-financial cycle)\left[{\begin{array}[]{\*{20}{c}}{{y\_{t}}}\\ {{f\_{t}}}\end{array}}\right]=\left\{{\begin{array}[]{\*{20}{l}}{({s\_{t}})\left[{\begin{array}[]{\*{20}{c}}{{\alpha\_{1}}}&{{\alpha\_{2}}}\\ {{\beta\_{1}}}&{{\beta\_{2}}}\end{array}}\right]\left[{\begin{array}[]{\*{20}{c}}{{y\_{t-1}}}\\ {{f\_{t-1}}}\end{array}}\right]+\left[{\begin{array}[]{\*{20}{c}}{{\varepsilon\_{t}}}\\ {{\varphi\_{t}}}\end{array}}\right]{\kern 1.0pt}\quad\text{(possible\quad real-financial\quad cycle)\quad}}\\ \begin{array}[]{l}\\ ({s\_{t}})\left[{\begin{array}[]{\*{20}{c}}{{\psi\_{1}}}&0\\ 0&{{\omega\_{2}}}\end{array}}\right]\left[{\begin{array}[]{\*{20}{c}}{{y\_{t-1}}}\\ {{f\_{t-1}}}\end{array}}\right]+\left[{\begin{array}[]{\*{20}{c}}{{\delta\_{t}}}\\ {{\rho\_{t}}}\end{array}}\right]\quad\text{(no\quad real-financial\quad cycle)}\end{array}\end{array}}\right. |  |

In the first regime, with coefficients α1\alpha\_{1}, α2\alpha\_{2}, β1\beta\_{1}, and β2\beta\_{2}, if α2​β1<0{\alpha\_{2}}{\beta\_{1}}<0 there is a local cyclical interaction between real and financial variables with a feedback loop between financial conditions and real economic outcomes. If β1>0{\beta\_{1}}>0 and α2<0{\alpha\_{2}}<0 these cycles are Mynskian cycles. In contrast, the second regime, represented only by the coefficients in the main diagonal ψ1\psi\_{1} and ω2\omega\_{2}, captures periods when the real and financial variables follow independent paths, without cyclical interaction. Error terms (εt\varepsilon\_{t}, φt\varphi\_{t}, δt\delta\_{t} and ρt\rho\_{t}) are zero mean withe-noise processes with variance collected in the variance-covariance matrices Σ1\Sigma\_{1} and Σ2\Sigma\_{2}.

st{s\_{t}} is the latent state-space discrete-time Markov chain representing the switching mechanism among the two regimes (or states). The state variable sts\_{t} follows the first regime (regime 11) when a possible real financial interaction is detected from the data and the second regime (regime 2) when the two variables follow an independent path.

There are four kinds of possible transitions between the two states:

* •

  From state 1 to state 1: with probability p11=P​(st=1|st−1=1){p\_{11}}=P\left({{s\_{t}}=1\left|{{s\_{t-1}}=1}\right.}\right)222This is read as the probability that the system is in regime 1 at time
  tt, given that it was in the same regime at the previous time (t−1)(t-1).
* •

  From state 1 to state 2: with probability p12=P​(st=2|st−1=1){p\_{12}}=P\left({{s\_{t}}=2\left|{{s\_{t-1}}=1}\right.}\right)
* •

  From state 2 to state 1: with probability p21=P​(st=1|st−1=2){p\_{21}}=P\left({{s\_{t}}=1\left|{{s\_{t-1}}=2}\right.}\right)
* •

  From state 2 to state 2: with probability p22=P​(st=2|st−1=2){p\_{22}}=P\left({{s\_{t}}=2\left|{{s\_{t-1}}=2}\right.}\right)

with:

|  |  |  |
| --- | --- | --- |
|  | p11+p12=1a​n​dp21+p22=1.{p\_{11}}+{p\_{12}}=1\quad and\quad{p\_{21}}+{p\_{22}}=1\_{.} |  |

In this way, st{s\_{t}} depends on st−1{s\_{t-1}} according to the following state transition matrix, which illustrates the probability of switching between these regimes over time.

|  |  |  |
| --- | --- | --- |
|  | [p11p12p21p22].\left[{\begin{array}[]{\*{20}{c}}{{p\_{11}}}&{{p\_{12}}}\\ {{p\_{21}}}&{{p\_{22}}}\end{array}}\right]\_{.} |  |

## 3  Dataset and estimation results

We use data spanning from the 1970s to 2020 for six OECD countries: the United States, the United Kingdom, France, Germany, Canada, and Australia. The real variable yy is proxied by seasonally adjusted real gross domestic product (GDP), obtained from the OECD Statistics and transformed into logarithmic levels. As financial variables ff, we consider nonfinancial corporate debt (NFCD), housing debt (HD), and the short-term nominal interest rate (STIR). Data on NFCD and HD are sourced from the Bank for International Settlements (BIS) Data Portal, while STIR is obtained from the OECD Statistics.333For the UK, the nominal interest rate is recovered from Federal Reserve Economic Data (FRED).

All the data are at yearly frequency, a choice motivated by several considerations. First, from a theoretical perspective, Minsky’s framework addresses medium- to long-term dynamics, which are more appropriately analyzed with lower-frequency data.444This choice also aligns with the original analysis by stockhammer2019short, which employs annual data. Second, from an empirical standpoint, yearly data mitigates serial correlation in the errors. In contrast, higher-frequency data would exacerbate serial correlation, requiring the inclusion of lag operators. This adjustment would increase the dimensionality of the system and preclude the recovery of a simple mathematical condition for cyclical dynamics. Furthermore, within a nonlinear framework, additional lag operators would place excessive demands on the sample. To ensure tractability and reliable estimation, we therefore focus on a selective estimation of the most essential parameters (hamilton2016macroeconomic). Finally, we address the small-sample issue by conducting 100 Monte Carlo simulations to verify the robustness of our results.

Once data are collected, we focus on cyclical phenomena by first extracting cycles from the time series using the Hodrick-Prescott filter, setting the smoothing parameter suggested for the yearly frequency (hodrick1997postwar). This also allows us to transform our series into a stationary series, thereby maximizing the likelihood function. Concerning this last point, the Markov switching estimation is carried out using the expectation-maximization algorithm (krolzig1997markov; hamilton2020time; hamilton2016macroeconomic). The iterative EM process consists of an expectation (E) step, where expected latent variable values are calculated based on current parameters, followed by a maximization (M) step, which identifies parameter values that enhance the expected log-likelihood from the E step. The parameters are used to recover the latent states’ distribution in the next E step.

### 3.1  GDP/NFCD interaction

Table [1](https://arxiv.org/html/2511.04348v1#S3.T1 "Table 1 ‣ 3.1 GDP/NFCD interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting") presents the estimation results when GDP and NFCD are included in the system.555As previously specified, the cyclical component of the two series is obtained by implementing the HP filter, which renders the series stationary and allows us to maximize the log-likelihood function. The results in Appendix A confirm the stationarity of the series for all the cases considered. The table is structured to display the coefficients for the two regimes with the associated transition matrix.

Table 1: Estimation Results for GDP/NFCD

| GDP/NFCD | Regime 1 | Regime 2 | Transition Matrix |
| --- | --- | --- | --- |
| USA | |  |  | | --- | --- | | 0.8215∗⁣∗∗0.8215^{\*\*\*} | −0.1066∗⁣∗∗-0.1066^{\*\*\*} | | (0.0678) | (0.0255) | | 1.6348∗⁣∗∗1.6348^{\*\*\*} | 0.4027∗⁣∗∗0.4027^{\*\*\*} | | (0.0884) | (0.0333) | | |  |  | | --- | --- | | 0.5389∗⁣∗∗0.5389^{\*\*\*} |  | | (0.1330) |  | |  | 0.9884∗⁣∗∗0.9884^{\*\*\*} | |  | (0.0669) | | |  |  | | --- | --- | | 0.837 | 0.163 | | 0.132 | 0.868 | |
|  |  |  |  |
| UK | |  |  | | --- | --- | | 0.8541∗⁣∗∗0.8541^{\*\*\*} | −0.0924∗⁣∗∗-0.0924^{\*\*\*} | | (0.0578) | (0.0170) | | 1.4605∗⁣∗∗1.4605^{\*\*\*} | 0.7026∗⁣∗∗0.7026^{\*\*\*} | | (0.2292) | (0.0676) | | |  |  | | --- | --- | | 0.044290.04429 |  | | (0.1180) |  | |  | 0.5760∗⁣∗∗0.5760^{\*\*\*} | |  | (0.0797) | | |  |  | | --- | --- | | 0.900 | 0.100 | | 0.310 | 0.690 | |
|  |  |  |  |
| France | |  |  | | --- | --- | | 0.9783∗⁣∗∗0.9783^{\*\*\*} | −0.1284∗⁣∗∗-0.1284^{\*\*\*} | | (0.1361) | (0.0418) | | 1.6935∗⁣∗∗1.6935^{\*\*\*} | 0.7408∗⁣∗∗0.7408^{\*\*\*} | | (0.1516) | (0.0466) | | |  |  | | --- | --- | | 0.3312∗⁣∗∗0.3312^{\*\*\*} |  | | (0.0539) |  | |  | 0.8120∗⁣∗∗0.8120^{\*\*\*} | |  | (0.0953) | | |  |  | | --- | --- | | 0.641 | 0.359 | | 0.388 | 0.612 | |
|  |  |  |  |
| Germany | |  |  | | --- | --- | | 0.5682∗⁣∗∗0.5682^{\*\*\*} | −0.1550∗⁣∗∗-0.1550^{\*\*\*} | | (0.1160) | (0.0481) | | 0.59835∗⁣∗∗0.59835^{\*\*\*} | 0.8093∗⁣∗∗0.8093^{\*\*\*} | | (0.1373) | (0.0569) | | |  |  | | --- | --- | | 0.6848∗⁣∗∗0.6848^{\*\*\*} |  | | (0.0719) |  | |  | 0.5400∗⁣∗∗0.5400^{\*\*\*} | |  | (0.1249) | | |  |  | | --- | --- | | 0.945 | 0.055 | | 0.150 | 0.850 | |
|  |  |  |  |
| Canada | |  |  | | --- | --- | | 0.02460.0246 | −0.30430∗⁣∗∗-0.30430^{\*\*\*} | | (0.0768) | (0.0309) | | 1.525∗⁣∗∗1.525^{\*\*\*} | 0.6036∗⁣∗∗0.6036^{\*\*\*} | | (0.2236) | (0.0899) | | |  |  | | --- | --- | | 0.5951∗⁣∗∗0.5951^{\*\*\*} |  | | (0.1281) |  | |  | 0.4882∗⁣∗∗0.4882^{\*\*\*} | |  | (0.1119) | | |  |  | | --- | --- | | 0.630 | 0.370 | | 0.311 | 0.689 | |
|  |  |  |  |
| Australia | |  |  | | --- | --- | | 0.83897∗⁣∗∗0.83897^{\*\*\*} | 0.01100.0110 | | (0.199) | (0.0353) | | 3.2656∗⁣∗∗3.2656^{\*\*\*} | 0.7459∗⁣∗∗0.7459^{\*\*\*} | | (0.5873) | (0.1040) | | |  |  | | --- | --- | | −0.0888∗-0.0888^{\*} |  | | (0.0491) |  | |  | 0.7009∗⁣∗∗0.7009^{\*\*\*} | |  | (0.0578) | | |  |  | | --- | --- | | 0.507 | 0.493 | | 0.695 | 0.305 | |
|  |  |  |  |

* •

  ∗∗∗, ∗∗, ∗ are significance level at 1%, 5% and 10%.
* •

  Standard errors are in parenthesis.
* •

  In regime one, regime two and the transition matrix, the reported values follow the positions of the parameters in section 2.1.

For all countries, except Australia, the mathematical condition to obtain complex eigenvalues is respected [(α1−β2)2+4​α2​β1<0{\left({{\alpha\_{1}}-{\beta\_{2}}}\right)^{2}}+4{\alpha\_{2}}{\beta\_{1}}<0]. The necessary condition (α2​β1<0{\alpha\_{2}}{\beta\_{1}}<0) is satisfied with cyclical parameters significant at a one percent statistical level. For Australia, signs are not respected, and parameters are not significant. Moreover, for the USA, France, Germany, Canada and the UK, the signs of cyclical coefficients (α2<0\alpha\_{2}<0 and β1>0\beta\_{1}>0) in regime one lead to the generation of endogenous Minsky cycles, a cyclical mechanism where an increase in the real variable leads to a subsequent rise in the financial variable, which in turn results in a decline in the real component. Contrary to regime one, regime two involves the absence of real-financial interaction between the real and the financial variable. The coefficients of the lagged values of the variables are significant for most countries, with the exception of Australia and the UK. For both regimes, the diagnostic check for autocorrelation is performed on the error terms following krolzig1997markov. Serial correlation tests (refer to Appendix B) indicate that MS-VAR models do not exhibit autocorrelation for all countries considered.

To verify the robustness of our estimates, we conduct a Monte Carlo simulation study. To implement it, we generate n=100n=100 sample paths of observations from the estimated model by randomly generating state disturbances from the standard normal distribution and incorporating them into the nonlinear regime-switching model. We repeat the estimation process 100 times. Once we obtain the results, we calculate the mean value of the parameters to determine the presence of Minskyan fluctuations. Consistent with previous findings, for the USA, France, Germany, Canada, and the UK, the results confirm the presence of endogenous real-financial interaction à la Minsky, alternating with a regime of no interaction between the real and financial variables (see Appendix C).

Shifting our focus toward the transition matrices, they reveal interesting insights into the persistence of the two regimes. From Table [1](https://arxiv.org/html/2511.04348v1#S3.T1 "Table 1 ‣ 3.1 GDP/NFCD interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting"), the USA, Germany and the UK show the highest probabilities of remaining within the same regime (e.g., for regime 1, p11=0.837p\_{11}=0.837 in the USA, p11=0.945p\_{11}=0.945 for Germany, and p11=0.900p\_{11}=0.900 in the UK), suggesting a stable regime structure over time. In contrast, France and Canada exhibit more frequent state transitions, indicating a greater probability of shifting between the two different regimes.

Figures [1](https://arxiv.org/html/2511.04348v1#S3.F1 "Figure 1 ‣ 3.1 GDP/NFCD interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting"), [2](https://arxiv.org/html/2511.04348v1#S3.F2 "Figure 2 ‣ 3.1 GDP/NFCD interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting"), [3](https://arxiv.org/html/2511.04348v1#S3.F3 "Figure 3 ‣ 3.1 GDP/NFCD interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting"), [4](https://arxiv.org/html/2511.04348v1#S3.F4 "Figure 4 ‣ 3.1 GDP/NFCD interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting"), [5](https://arxiv.org/html/2511.04348v1#S3.F5 "Figure 5 ‣ 3.1 GDP/NFCD interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting") show the filtered probabilities of two regimes across the USA, the UK, France, Germany, and Canada from the 1970s to 2020, with the solid line representing the “Minsky Regime” and the dashed line representing the “No Minsky Regime”. For the USA, from the 1970s to the early 1980s, the probability of being in the “Minsky Regime” was relatively high. In contrast, from the mid-1980s to the early 1990s, the probabilities shifted significantly towards the “No Minsky Regime”, suggesting a period of independence between real and financial variables. This pattern changed in the mid-1990s with a clear return to the “Minsky Regime”. This trend culminated in the explosion of the global financial crisis of 2007-2008, with a temporary increase in the “No Minsky Regime” probability in the early 2010s. From 2010 to 2020, the graph shows alternating probabilities with a general trend toward the “Minsky Regime.” A similar pattern can be observed for the UK. The only difference is the starting period of the real/financial interaction à la Minsky. In fact, the UK experienced an increasing probability of the “Minsky Regime” starting from the middle of the 1980s. As in the USA, this regime has been persistent around the dot-com crisis and during the global financial crisis.

Figs. [3](https://arxiv.org/html/2511.04348v1#S3.F3 "Figure 3 ‣ 3.1 GDP/NFCD interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting") and [5](https://arxiv.org/html/2511.04348v1#S3.F5 "Figure 5 ‣ 3.1 GDP/NFCD interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting") for France and Canada indicate more volatile patterns compared to the USA and the UK. These fluctuations reflect a greater sensitivity to frequent transitions between the two regimes. Similar to the USA and the UK, France also shows high probabilities for the “Minsky Regime” during the early 2000s and pre-2007/2008. For Germany, the “Minsky Regime” dominated for an extended period from the late 1970s through the mid-1990s. Post-1995, there is a noticeable shift towards the “No Minsky Regime”, interrupted around the global financial crisis.

Overall, the results highlight a time-dependent Minsky-type cyclical relationship between GDP and NFCD in most countries. From the filtered probabilities, this regime dominates essentially during the 1970s and in periods that culminated with the dot-com crisis and the global financial crisis. Transition matrices further reveal heterogeneity across countries, with the UK, Germany, and the USA showing high regime persistence, while France and Canada display more frequent shifts.

![Refer to caption](Figure/USA_Filtered_Probabilities.jpg)


Figure 1: Filtered probability of the two regimes in the USA.

![Refer to caption](Figure/UK_Filtered_Probabilities.jpg)


Figure 2: Filtered probability of the two regimes in the UK.

![Refer to caption](Figure/France_Filtered_Probabilities.jpg)


Figure 3: Filtered probability of the two regimes in France.

![Refer to caption](Figure/Germany_Filtered_Probabilities.jpg)


Figure 4: Filtered probability of the two regimes in Germany.

![Refer to caption](Figure/Canada_Filtered_Probabilities.jpg)


Figure 5: Filtered probability of the two regimes in Canada.

### 3.2  GDP/HD interaction

Table [2](https://arxiv.org/html/2511.04348v1#S3.T2 "Table 2 ‣ 3.2 GDP/HD interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting") presents the estimation results from the MS-VAR model that examines the relationship between GDP and HD across the countries considered.

In the USA, the cyclical coefficients for regime 1 are β1=0.7348\beta\_{1}=0.7348 and α2=−0.1123\alpha\_{2}=-0.1123, significant at levels 1% and 5%, respectively, and with signs that reflect the generation of endogenous Minskyan cycles. This regime is persistent, with p11=0.824p\_{11}=0.824, suggesting that once the system enters this state, it will likely remain there for an extended period. In particular, this regime emerged strongly during the 1990s, with peaks during the global financial crisis (Fig. [6](https://arxiv.org/html/2511.04348v1#S3.F6 "Figure 6 ‣ 3.2 GDP/HD interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting")). Similarly, the UK exhibits significant coefficients in regime 1: β1=0.7925\beta\_{1}=0.7925, and α2=−0.1763\alpha\_{2}=-0.1763 at the 1% statistical level. As for the USA, the transition probability for regime 1 is p11=0.802p\_{11}=0.802, indicating high persistence, especially for the 90s through the subsequent period (Fig. [7](https://arxiv.org/html/2511.04348v1#S3.F7 "Figure 7 ‣ 3.2 GDP/HD interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting")).

For Germany and Australia, regime one does not display the mathematical conditions to obtain endogenous cycles. In Germany, β1=−0.0433\beta\_{1}=-0.0433 and α2=−0.2991\alpha\_{2}=-0.2991, while for Australia, they are β1=0.4722\beta\_{1}=0.4722 and α2=0.2357\alpha\_{2}=0.2357. In other words, the necessary condition (α​β1<0\alpha\beta\_{1}<0) is not satisfied. For France, although the mathematical conditions are satisfied, the coefficients are not statistically significant. Finally, for Canada, α2=−0.21825\alpha\_{2}=-0.21825 and β1=0.18783\beta\_{1}=0.18783 respect the necessary condition to obtain cyclical conditions and are statistically significant at one percent and five percent statistical levels, respectively, but the magnitudes are too small to sustain cyclical dynamics.

As in the case with nonfinancial corporate debt, we tested the robustness of the results. Monte Carlo simulation results, summarized in Appendix C, provide further empirical evidence supporting the existence of distinct regimes with the existence of local endogenous Minskyan cycles for the UK and the USA, but not for the other countries considered.

In summary, the introduction of household debt into the analysis indicates that Minsky’s hypothesis is empirically found in the USA and the UK. Specifically, in regime 1, which persisted during the global financial crisis, the cyclical parameters are statistically significant and exhibit signs consistent with Minskyan cycle generation. In contrast, other countries show no evidence of Minsky cycles associated with household debt. For example, regime one does not meet the mathematical condition for endogenous cycles in Germany and Australia, parameters lack statistical significance in France, and the magnitudes are insufficient to generate cyclical phenomena in Canada. These findings highlight the unique economic dynamics in the USA and UK, where household debt played a critical role in generating Minskyan cycles, unlike in the other countries studied.

Table 2: Estimation Results for GDP/HD

| GDP/HD | Regime 1 | Regime 2 | Transition Matrix |
| --- | --- | --- | --- |
| USA | |  |  | | --- | --- | | 0.6615∗⁣∗∗0.6615^{\*\*\*} | −0.1123∗∗-0.1123^{\*\*} | | (0.1050) | (0.0437) | | 0.7348∗⁣∗∗0.7348^{\*\*\*} | 0.6325∗⁣∗∗0.6325^{\*\*\*} | | 0.0802) | (0.0334) | | |  |  | | --- | --- | | 0.2878∗⁣∗∗0.2878^{\*\*\*} |  | | (0.0994) |  | |  | 0.8359∗⁣∗∗0.8359^{\*\*\*} | |  | (0.0939) | | |  |  | | --- | --- | | 0.824 | 0.176 | | 0.157 | 0.843 | |
|  |  |  |  |
| UK | |  |  | | --- | --- | | 0.7595∗⁣∗∗0.7595^{\*\*\*} | −0.1763∗⁣∗∗-0.1763^{\*\*\*} | | (0.0756) | (0.0378) | | 0.7925∗⁣∗∗0.7925^{\*\*\*} | 0.7203∗⁣∗∗0.7203^{\*\*\*} | | (0.0752) | (0.0376) | | |  |  | | --- | --- | | −0.0203-0.0203 |  | | (0.1474) |  | |  | 0.18670.1867 | |  | (0.1386) | | |  |  | | --- | --- | | 0.802 | 0.198 | | 0.292 | 0.708 | |
|  |  |  |  |
| France | |  |  | | --- | --- | | 0.3992∗⁣∗∗0.3992^{\*\*\*} | −0.1136-0.1136 | | (0.1196) | (0.1093) | | 0.15600.1560 | 0.6310∗⁣∗∗0.6310^{\*\*\*} | | (0.1090) | (0.0996) | | |  |  | | --- | --- | | 1.2871∗⁣∗∗1.2871^{\*\*\*} |  | | (0.0496) |  | |  | 0.9872∗⁣∗∗0.9872^{\*\*\*} | |  | (0.0746) | | |  |  | | --- | --- | | 0.497 | 0.503 | | 0.945 | 0.055 | |
|  |  |  |  |
| Germany | |  |  | | --- | --- | | 1.0552∗⁣∗∗1.0552^{\*\*\*} | −0.2991∗⁣∗∗-0.2991^{\*\*\*} | | (0.1465) | (0.0972) | | −0.0433∗⁣∗∗-0.0433^{\*\*\*} | 0.7763∗⁣∗∗0.7763^{\*\*\*} | | (0.1600) | (0.1061) | | |  |  | | --- | --- | | −0.0420∗⁣∗∗-0.0420^{\*\*\*} |  | | (0.0537) |  | |  | 0.8091∗⁣∗∗0.8091^{\*\*\*} | |  | (0.0415) | | |  |  | | --- | --- | | 0.331 | 0.669 | | 1.000 | 0.000 | |
|  |  |  |  |
| Canada | |  |  | | --- | --- | | 0.3706∗⁣∗∗0.3706^{\*\*\*} | −0.2182∗⁣∗∗-0.2182^{\*\*\*} | | (0.1111) | (0.0676) | | 0.1878∗∗0.1878^{\*\*} | 0.7923∗⁣∗∗0.7923^{\*\*\*} | | (0.0957) | (0.0582) | | |  |  | | --- | --- | | 0.13440.1344 |  | | (0.0973) |  | |  | 0.8100∗⁣∗∗0.8100^{\*\*\*} | |  | (0.0602) | | |  |  | | --- | --- | | 0.937 | 0.063 | | 0.086 | 0.914 | |
|  |  |  |  |
| Australia | |  |  | | --- | --- | | 0.1638∗⁣∗∗0.1638^{\*\*\*} | 0.2357∗⁣∗∗0.2357^{\*\*\*} | | (0.0499) | (0.0352) | | 0.4722∗⁣∗∗0.4722^{\*\*\*} | 0.6692∗⁣∗∗0.6692^{\*\*\*} | | (0.0626) | (0.0442) | | |  |  | | --- | --- | | 0.6194∗⁣∗∗0.6194^{\*\*\*} |  | | (0.1266) |  | |  | 0.4327∗⁣∗∗0.4327^{\*\*\*} | |  | (0.1192) | | |  |  | | --- | --- | | 0.495 | 0.505 | | 0.253 | 0.747 | |
|  |  |  |  |

* •

  ∗∗∗, ∗∗, ∗ are significance level at 1%, 5% and 10%.
* •

  Standard errors are in parenthesis.
* •

  In regime one, regime two and the transition matrix, the reported values follow the positions of the parameters in section 2.1.

![Refer to caption](Figure/USA_Filtered_Probabilities_House.jpg)


Figure 6: Filtered probability of the two regimes in the USA.

![Refer to caption](Figure/UK_Filtered_Probabilities_House.jpg)


Figure 7: Filtered probability of the two regimes in the UK.

### 3.3  GDP/STIR interaction

Table [3](https://arxiv.org/html/2511.04348v1#S3.T3 "Table 3 ‣ 3.3 GDP/STIR interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting") presents the results of the MS-VAR model, which examines the interaction between GDP and the short-term interest rate. In regime 1, for all countries, the cyclical condition is respected ((α1−β2)2+4​α2​β1<0{\left({{\alpha\_{1}}-{\beta\_{2}}}\right)^{2}}+4{\alpha\_{2}}{\beta\_{1}}<0). The two parameters of interest (α2\alpha\_{2} and β1)\beta\_{1}) exhibit signs of generating Minsky cycles (α2<0\alpha\_{2}<0 and β1>0\beta\_{1}>0), indicating that an increase in the real variable leads to a subsequent increase in the interest rate, which eventually constrains GDP growth.

The transition matrices in Table reveal a high probability of remaining in the two regimes for the USA, France, Australia and the UK, suggesting persistent Minsky cycles but also persistent independent processes. Canada and Germany show a more frequent transition between the two regimes, reflecting frequent periods of both real-financial interaction and autonomous processes.

Similarly to our analysis with corporate and household debt, we extend our analysis with 100 Monte Carlo simulations. A summary of the results is presented in Appendix C. Overall, the estimation results provide empirical evidence supporting the presence of endogenous real-financial cycles in regime 1 for all the countries considered.

We now pass to analyze the filtered probabilities of the system being in two distinct regimes. For the USA (Fig. [8](https://arxiv.org/html/2511.04348v1#S3.F8 "Figure 8 ‣ 3.3 GDP/STIR interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting")), from the early 1970s to the mid-1980s, the “Minsky Regime” appears to dominate, indicating frequent or prolonged periods of real-financial interactions. After the 1985, there are noticeable shifts between the two regimes, with some periods dominated by the “No Minsky Regime”, such as the mid-1990s and post-2010, while others, in the corresponding of 2007/2008, reflect a resurgence of the “Minsky Regime”.

For the UK (Fig. [9](https://arxiv.org/html/2511.04348v1#S3.F9 "Figure 9 ‣ 3.3 GDP/STIR interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting")), prior to 1985, the system alternates between the two regimes, with brief intervals where the “Minsky Regime” (solid line) is dominant. However, after 1985, the probability of being in a “Minsky Regime” sharply increases, and this dynamics persists through the end of the sample period, with the ”No Minsky” regime rarely appearing. These dynamics are very similar to those presented for Australia (Fig. [13](https://arxiv.org/html/2511.04348v1#S3.F13 "Figure 13 ‣ 3.3 GDP/STIR interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting")).

French and Germany (Fig. [10](https://arxiv.org/html/2511.04348v1#S3.F10 "Figure 10 ‣ 3.3 GDP/STIR interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting") and [11](https://arxiv.org/html/2511.04348v1#S3.F11 "Figure 11 ‣ 3.3 GDP/STIR interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting"), respectively) present similarities and differences. For both countries, from 70s to mid 80s, “Minsky Regime” seems to dominate in term of percentage compared to the other regime. Then for France, except for the dominance of “No Minsky Regime” in the 1985, “Minsky Regime” becomes predominant from the mid-1990s to the late 2000s, as in the UK. Germany, on the other hand, exhibits more frequent transitions between the two regimes across the entire sample period, with no prolonged dominance of either regime. A very similar results can be noticed for Canada (Fig [12](https://arxiv.org/html/2511.04348v1#S3.F12 "Figure 12 ‣ 3.3 GDP/STIR interaction ‣ 3 Dataset and estimation results ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting")). These transitions highlight that neither economy maintained prolonged periods in either regime during this earlier time frame. Finally, for both France and Germany, there is a tendency toward a ’No Minsky Regime’ after the 2010, a common dynamic influenced by the actions of the European Central Bank during the post-2007/2008 European crisis.

Overall, the presence of Minskyan cycles emphasizes the crucial role that central banks play in influencing economic cycles through their interest rate policies, as shifts in interest rates can either amplify or dampen the real economy. In other words, in economies where real-financial interactions are strong, central banks’ manipulation of interest rates can trigger endogenous economic fluctuations, consistent with Minsky’s financial instability hypothesis.

Table 3: Estimation Results for GDP/STIR

| GDP/STIR | Regime 1 | Regime 2 | Transition Matrix |
| --- | --- | --- | --- |
| USA | |  |  | | --- | --- | | 0.4801∗⁣∗∗0.4801^{\*\*\*} | −1.1992∗⁣∗∗-1.1992^{\*\*\*} | | (0.1293) | (0.2213) | | 0.4484∗⁣∗∗0.4484^{\*\*\*} | 0.4364∗⁣∗∗0.4364^{\*\*\*} | | (0.0670) | (0.1147) | | |  |  | | --- | --- | | 0.6403∗⁣∗∗0.6403^{\*\*\*} |  | | (0.0593) |  | |  | 0.3446∗⁣∗∗0.3446^{\*\*\*} | |  | (0.0957) | | |  |  | | --- | --- | | 0.537 | 0.463 | | 0.584 | 0.416 | |
|  |  |  |  |
| UK | |  |  | | --- | --- | | 0.9328∗⁣∗∗0.9328^{\*\*\*} | −0.6669∗⁣∗∗-0.6669^{\*\*\*} | | (0.0928) | (0.1251) | | 0.3125∗⁣∗∗0.3125^{\*\*\*} | 0.3440∗⁣∗∗0.3440^{\*\*\*} | | (0.0737) | (0.0993) | | |  |  | | --- | --- | | 1.0135∗⁣∗∗1.0135^{\*\*\*} |  | | (0.0681) |  | |  | −0.3127∗-0.3127^{\*} | |  | (0.1684) | | |  |  | | --- | --- | | 0.898 | 0.102 | | 0.597 | 0.403 | |
|  |  |  |  |
| France | |  |  | | --- | --- | | 0.9308∗⁣∗∗0.9308^{\*\*\*} | −0.6493∗⁣∗∗-0.6493^{\*\*\*} | | (0.1196) | (0.1093) | | 0.3892∗⁣∗∗0.3892^{\*\*\*} | 0.0983∗⁣∗∗0.0983^{\*\*\*} | | (0.1090) | (0.0996) | | |  |  | | --- | --- | | 0.14210.1421 |  | | (0.1289) |  | |  | 1.0866∗⁣∗∗1.0866^{\*\*\*} | |  | (0.0284) | | |  |  | | --- | --- | | 0.936 | 0.064 | | 0.130 | 0.870 | |
|  |  |  |  |
| Germany | |  |  | | --- | --- | | 0.6854∗⁣∗∗0.6854^{\*\*\*} | −0.5688∗⁣∗∗-0.5688^{\*\*\*} | | (0.0967) | (0.0841) | | 0.5028∗⁣∗∗0.5028^{\*\*\*} | 0.33433∗⁣∗∗0.33433^{\*\*\*} | | (0.1481) | (0.1288) | | |  |  | | --- | --- | | 0.6955∗⁣∗∗0.6955^{\*\*\*} |  | | (0.0969) |  | |  | 0.7211∗⁣∗∗0.7211^{\*\*\*} | |  | (0.0463) | | |  |  | | --- | --- | | 0.760 | 0.240 | | 0.222 | 0.778 | |
|  |  |  |  |
| Canada | |  |  | | --- | --- | | 0.9885∗⁣∗∗0.9885^{\*\*\*} | −1.037∗⁣∗∗-1.037^{\*\*\*} | | (0.0905) | (0.1217) | | 0.6089∗∗0.6089^{\*\*} | 0.00750.0075 | | (0.0570) | (0.0767) | | |  |  | | --- | --- | | 0.5392∗⁣∗∗0.5392^{\*\*\*} |  | | (0.0784) |  | |  | 0.6474∗⁣∗∗0.6474^{\*\*\*} | |  | (0.1135) | | |  |  | | --- | --- | | 0.484 | 0.516 | | 0.501 | 0.499 | |
|  |  |  |  |
| Australia | |  |  | | --- | --- | | 0.51990.5199 | −0.2810∗⁣∗∗-0.2810^{\*\*\*} | | (0.1288) | (0.1104) | | 0.4907∗⁣∗∗0.4907^{\*\*\*} | 0.3367∗⁣∗∗0.3367^{\*\*\*} | | (0.1091) | (0.0935) | | |  |  | | --- | --- | | 0.6730∗0.6730^{\*} |  | | (0.123) |  | |  | 0.1695∗⁣∗∗0.1695^{\*\*\*} | |  | (0.1515) | | |  |  | | --- | --- | | 0.970 | 0.030 | | 0.164 | 0.836 | |
|  |  |  |  |

* •

  ∗∗∗, ∗∗, ∗ are significance level at 1%, 5% and 10%.
* •

  Standard errors are in parenthesis.
* •

  In regime one, regime two and the transition matrix, the reported values follow the positions of the parameters in section 2.1.

![Refer to caption](Figure/USA_Filtered_Probabilities_Interest.jpg)


Figure 8: Filtered probability of the two regimes in the USA.

![Refer to caption](Figure/UK_Filtered_Probabilities_Interest.jpg)


Figure 9: Filtered probability of the two regimes in the UK.

![Refer to caption](Figure/France_Filtered_Probabilities_Interest.jpg)


Figure 10: Filtered probability of the two regimes in France.

![Refer to caption](Figure/Germany_Filtered_Probabilities_Interest.jpg)


Figure 11: Filtered probability of the two regimes in Germany.

![Refer to caption](Figure/Canada_Filtered_Probabilities_Interest.jpg)


Figure 12: Filtered probability of the two regimes in Canada.

![Refer to caption](Figure/Australia_Filtered_Probabilities_Interest.jpg)


Figure 13: Filtered probability of the two regimes in Australia.

## 4  Conclusions

This paper explored Minsky’s financial instability hypothesis by examining the interaction mechanisms behind real-financial cycles, with a specific focus on the roles of household debt, corporate debt, and interest rates. The aim was to determine whether Minsky’s hypothesis can be captured within the context of nonlinear endogenous regime changes, thereby offering a deeper understanding of the financial instability hypothesis and its implications across different countries.

To implement our analysis, we built on the framework of stockhammer2019short and extended it by introducing a bivariate Markov-switching vector autoregressive model. This extension enabled us to capture local dynamic interaction in a context of nonlinear regime changes. Through the nonlinear filtering technique, we traced the occurrence of regime changes and observed the manifestation of Minskyan endogenous real-financial cycles during specific years between 1970 and 2020. The relationship between household debt and GDP appears comparatively weak, with significant local effects of real-financial interaction identified only in the United States and the United Kingdom. In contrast, corporate debt exhibits more robust and widespread patterns of local interaction, observed across all countries in the sample except Australia. When short-term interest rates are incorporated into the analysis, the evidence of such interaction mechanisms becomes consistent across all countries, highlighting the central role of monetary conditions in mediating real-financial linkages.

Our study highlights the importance of considering nonlinear regime changes in the analysis of Minsky endogenous cycles, providing a more comprehensive view of real-financial fluctuations and their underlying mechanisms. At the same time, the paper contributes to the broader literature on financial instability and macroeconomic fluctuations, providing valuable insights that could inform future economic policies aimed at mitigating financial instability.

## Appendix A

Table [4](https://arxiv.org/html/2511.04348v1#Ax1.T4 "Table 4 ‣ Appendix A ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting") shows the results of the unit root test when corporate debt, household debt and interest rate are included in the system with GDP for all the countries considered. The Dicke-Fuller test is used to test the null hypothesis that a unit root is present in the cyclical component of the series. cValue and StatValues represent the critical value and test statistics, respectively.

Table 4: Unit Root Test.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| USA | GDP/InterestRate | GDP/HouseDebt | GDP/CorporateDebt |  |
| |  | | --- | | cValue | | StatValues | | |  | | --- | | -1.94 | | (-3.3341/-3.4015) | | |  | | --- | | -1.94 | | (-4.4224/-2.4317) | | |  | | --- | | -1.94 | | (-3.3341/-2.1046) | |  |
| UK |  |  |  |  |
| |  | | --- | | cValue | | StatValues | | |  | | --- | | -1.94 | | (-2.6198/-4.3916) | | |  | | --- | | -1.94 | | (-5.1540/-2.5585) | | |  | | --- | | -1.94 | | (-3.3733/-2.4019) | |  |
| France |  |  |  |  |
| |  | | --- | | cValue | | StatValues | | |  | | --- | | -1.94 | | (-3.2219/-3.7994) | | |  | | --- | | -1.94 | | (-3.1545/-2.2614) | | |  | | --- | | -1.94 | | (-3.1535/-2.2069) | |  |
| Germany |  |  |  |  |
| |  | | --- | | cValue | | StatValues | | |  | | --- | | -1.94 | | (-3.6747/-3.7094) | | |  | | --- | | -1.94 | | (-4.7684/-2.3155) | | |  | | --- | | -1.94 | | (-3.6062/-2.4593) | |  |
| Canada |  |  |  |  |
| |  | | --- | | cValue | | StatValues | | |  | | --- | | -1.94 | | (-3.4071/-4.2600) | | |  | | --- | | -1.94 | | (-5.0253/-2.1799) | | |  | | --- | | -1.94 | | (-5.0253/-3.9932) | |  |
| Australia |  |  |  |  |
| |  | | --- | | cValue | | StatValues | | |  | | --- | | -1.94 | | (-4.3303/-3.3673) | | |  | | --- | | -1.94 | | (-3.3481/-3.1034) | | |  | | --- | | -1.94 | | (-4.5847/-2.6934) | |  |

## Appendix B

Tables [5](https://arxiv.org/html/2511.04348v1#Ax2.T5 "Table 5 ‣ Appendix B ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting"), [6](https://arxiv.org/html/2511.04348v1#Ax2.T6 "Table 6 ‣ Appendix B ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting"), and [7](https://arxiv.org/html/2511.04348v1#Ax2.T7 "Table 7 ‣ Appendix B ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting") show the results of the Ljung-Box Q-test for autocorrelation in residuals. The test is used to test the null hypothesis of no serial correlation. cValue and StatValues stand for the critical value and test statistics, respectively.

Table 5: Diagnostic check for residual autocorrelation (GDP/NFCD)

| USA | εt\varepsilon\_{t} | φt\varphi\_{t} | δt\delta\_{t} | ρt\rho\_{t} |
| --- | --- | --- | --- | --- |
| |  | | --- | | cValue | | StatValue | | |  | | --- | | 6.63 | | 4.39 | | |  | | --- | | 6.63 | | 6.10 | | |  | | --- | | 6.63 | | 0.29 | | |  | | --- | | 6.63 | | 2.83 | |
| UK |  |  |  |  |
| |  | | --- | | cValue | | StatValue | | |  | | --- | | 6.63 | | 0.03 | | |  | | --- | | 6.63 | | 1.94 | | |  | | --- | | 6.63 | | 0.46 | | |  | | --- | | 6.63 | | 0.47 | |
| France |  |  |  |  |
| |  | | --- | | cValue | | StatValue | | |  | | --- | | 6.63 | | 0.09 | | |  | | --- | | 6.63 | | 3.00 | | |  | | --- | | 6.63 | | 2.20 | | |  | | --- | | 6.63 | | 2.14 | |
| Germany |  |  |  |  |
| |  | | --- | | cValue | | StatValue | | |  | | --- | | 6.63 | | 3.18 | | |  | | --- | | 6.63 | | 3.74 | | |  | | --- | | 6.63 | | 0.68 | | |  | | --- | | 6.63 | | 5.95 | |
| Canada |  |  |  |  |
| |  | | --- | | cValue | | StatValue | | |  | | --- | | 6.63 | | 2.18 | | |  | | --- | | 6.63 | | 2.64 | | |  | | --- | | 6.63 | | 1.13 | | |  | | --- | | 6.63 | | 1.54 | |
| Australia |  |  |  |  |
| |  | | --- | | cValue | | StatValue | | |  | | --- | | 6.63 | | 4.30 | | |  | | --- | | 6.63 | | 1.64 | | |  | | --- | | 6.63 | | 0.12 | | |  | | --- | | 6.63 | | 0.85 | |




Table 6: Diagnostic check for residual autocorrelation (GDP/HD)

| USA | εt\varepsilon\_{t} | φt\varphi\_{t} | δt\delta\_{t} | ρt\rho\_{t} |
| --- | --- | --- | --- | --- |
| |  | | --- | | cValue | | StatValue | | |  | | --- | | 6.63 | | 2.72 | | |  | | --- | | 6.63 | | 0.88 | | |  | | --- | | 6.63 | | 1.74 | | |  | | --- | | 6.63 | | 5.17 | |
| UK |  |  |  |  |
| |  | | --- | | cValue | | StatValue | | |  | | --- | | 6.63 | | 7.75 | | |  | | --- | | 6.63 | | 0.39 | | |  | | --- | | 6.63 | | 0.75 | | |  | | --- | | 6.63 | | 5.25 | |
| France |  |  |  |  |
| |  | | --- | | cValue | | StatValue | | |  | | --- | | 6.63 | | 0.34 | | |  | | --- | | 6.63 | | 1.58 | | |  | | --- | | 6.63 | | 0.85 | | |  | | --- | | 6.63 | | 0.60 | |
| Germany |  |  |  |  |
| |  | | --- | | cValue | | StatValue | | |  | | --- | | 6.63 | | 1.72 | | |  | | --- | | 6.63 | | 2.37 | | |  | | --- | | 6.63 | | 0.86 | | |  | | --- | | 6.63 | | 2.65 | |
| Canada |  |  |  |  |
| |  | | --- | | cValue | | StatValue | | |  | | --- | | 6.63 | | 5.14 | | |  | | --- | | 6.63 | | 5.82 | | |  | | --- | | 6.63 | | 3.04 | | |  | | --- | | 6.63 | | 18 | |
| Australia |  |  |  |  |
| |  | | --- | | cValue | | StatValue | | |  | | --- | | 6.63 | | 2.00 | | |  | | --- | | 6.63 | | 3.57 | | |  | | --- | | 6.63 | | 0.76 | | |  | | --- | | 6.63 | | 6.43 | |




Table 7: Diagnostic check for residual autocorrelation (GDP/STIR)

| USA | εt\varepsilon\_{t} | φt\varphi\_{t} | δt\delta\_{t} | ρt\rho\_{t} |
| --- | --- | --- | --- | --- |
| |  | | --- | | cValue | | StatValue | | |  | | --- | | 6.63 | | 3.18 | | |  | | --- | | 6.63 | | 0.47 | | |  | | --- | | 6.63 | | 1.92 | | |  | | --- | | 6.63 | | 3.74 | |
| UK |  |  |  |  |
| |  | | --- | | cValue | | StatValue | | |  | | --- | | 6.63 | | 0.76 | | |  | | --- | | 6.63 | | 5.71 | | |  | | --- | | 6.63 | | 1.00 | | |  | | --- | | 6.63 | | 2.30 | |
| France |  |  |  |  |
| |  | | --- | | cValue | | StatValue | | |  | | --- | | 6.63 | | 3.41 | | |  | | --- | | 6.63 | | 0.72 | | |  | | --- | | 6.63 | | 1.20 | | |  | | --- | | 6.63 | | 5.61 | |
| Germany |  |  |  |  |
| |  | | --- | | cValue | | StatValue | | |  | | --- | | 6.63 | | 0.66 | | |  | | --- | | 6.63 | | 0.05 | | |  | | --- | | 6.63 | | 3.84 | | |  | | --- | | 6.63 | | 3.28 | |
| Canada |  |  |  |  |
| |  | | --- | | cValue | | StatValue | | |  | | --- | | 6.63 | | 3.33 | | |  | | --- | | 6.63 | | 1.04 | | |  | | --- | | 6.63 | | 0.03 | | |  | | --- | | 6.63 | | 0.19 | |
| Australia |  |  |  |  |
| |  | | --- | | cValue | | StatValue | | |  | | --- | | 6.63 | | 0.87 | | |  | | --- | | 6.63 | | 7.35 | | |  | | --- | | 6.63 | | 2.42 | | |  | | --- | | 6.63 | | 8.54 | |

## Appendix C

In this appendix, we present the estimation results of 100 Monte Carlo simulations when GDP is included into the system with corporate debt (table [8](https://arxiv.org/html/2511.04348v1#Ax3.T8 "Table 8 ‣ Appendix C ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting")), household debt (table [9](https://arxiv.org/html/2511.04348v1#Ax3.T9 "Table 9 ‣ Appendix C ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting")) and interest rate (table [10](https://arxiv.org/html/2511.04348v1#Ax3.T10 "Table 10 ‣ Appendix C ‣ Regime Changes and Real-Financial Cycles: Searching Minsky’s Hypothesis in a Nonlinear Setting")).

| GDP/NFCD | Regime 1 | Regime 2 | Transition Matrix |
| --- | --- | --- | --- |
| USA | |  |  | | --- | --- | | 0.77460.7746 | −0.0905-0.0905 | | (0.7115 , 0.8378) | (-0.1183 , - 0.0627) | | 1.20181.2018 | 0.55400.5540 | | (1.0684 , 1.3351) | (0.4989 , 0.5896) | | |  |  | | --- | --- | | 0.43350.4335 |  | | (0.3811 , 0.4859) |  | |  | 0.93850.9385 | |  | (0.9077 , 0.9693) | | |  |  | | --- | --- | | 0.6636 | 0.3364 | | 0.3254 | 0.6746 | |
|  |  |  |  |
| UK | |  |  | | --- | --- | | 0.66170.6617 | −0.0796-0.0796 | | (0.58897 , 0.7336) | (-0.1024 , - 0.0569) | | 1.53731.5373 | 0.65160.6516 | | (1.4123 , 1.6623) | (0.4989 , 0.5896) | | |  |  | | --- | --- | | 0.32980.3298 |  | | (0.6268 , 0.6821) |  | |  | 0.63400.6340 | |  | (0.2429 , 0.4147) | | |  |  | | --- | --- | | 0.7389 | 0.2611 | | 0.4289 | 0.5711 | |
|  |  |  |  |
| France | |  |  | | --- | --- | | 0.96720.9672 | −0.1423-0.1423 | | (0.9176 , 0.0168) | (-0.161 , - 0.1232) | | 1.71091.7109 | 0.72040.7204 | | (1.6421 , 1.7797) | (0.6895 , 0.7514) | | |  |  | | --- | --- | | 0.37710.3771 |  | | (0.3371 , 0.4171) |  | |  | 0.78620.7862 | |  | (0.7520 , 0.8205) | | |  |  | | --- | --- | | 0.6141 | 0.3859 | | 0.4306 | 0.5694 | |
|  |  |  |  |
| Germany | |  |  | | --- | --- | | 0.60900.6090 | −0.1793-0.1793 | | (0.5706 , 0.6473) | (-0.2019 , - 0.1566) | | 1.71351.7135 | 0.73910.7391 | | (1.6171 , 1.8100) | (0.6983 , 0.7799) | | |  |  | | --- | --- | | 0.50290.5029 |  | | (0.4380 , 0.5678) |  | |  | 0.69470.6947 | |  | (0.6077 , 0.7818) | | |  |  | | --- | --- | | 0.7230 | 0.2770 | | 0.4825 | 0.5175 | |
|  |  |  |  |
| Canada | |  |  | | --- | --- | | 0.10380.1038 | −0.3034-0.3034 | | (0.0602 , 0.1475) | (-0.3204 , - 0.2863) | | 1.55401.5540 | 0.59530.5953 | | (1.4291 , 1.6788) | (0.5598 , 0.6318) | | |  |  | | --- | --- | | 0.58750.5875 |  | | (0.5440 , 0.6311) |  | |  | 0.48080.4808 | |  | (0.4339 , 0.5277) | | |  |  | | --- | --- | | 0.5844 | 0.4156 | | 0.3379 | 0.6221 | |
|  |  |  |  |
| Australia | |  |  | | --- | --- | | 0.80040.8004 | 0.00860.0086 | | (0.73627 , 0.8647) | (-0.0056 , 0.0228) | | 3.41883.4188 | 0.67970.6797 | | (3.2253 , 3.6124) | (0.6430 , 0.7164) | | |  |  | | --- | --- | | 0.014080.01408 |  | | (-0.0448 , 0.0727) |  | |  | 0.72770.7277 | |  | (0.7025 , 0.7529) | | |  |  | | --- | --- | | 0.5091 | 0.4909 | | 0.5877 | 0.4123 | |
|  |  |  |  |

* •

  Confidence interval at 95% level in parenthesis.
* •

  In regime one, regime two and the transition matrix, the reported values follow the positions of the parameters in section 2.1.

Table 8: Monte Carlo Estimation Results for GDP/NFCD



| GDP/HD | Regime 1 | Regime 2 | Transition Matrix |
| --- | --- | --- | --- |
| USA | |  |  | | --- | --- | | 0.61850.6185 | −0.1194-0.1194 | | (0.5317 , 0.7052) | (-0.1686 , - 0.0702) | | 0.57830.5783 | 0.65500.6550 | | (0.4665 , 0.6900) | (0.6034 , 0.7066) | | |  |  | | --- | --- | | 0.26890.2689 |  | | (0.2132 , 0.3245) |  | |  | 0.79850.7985 | |  | (0.7591 , 0.8379) | | |  |  | | --- | --- | | 0.6314 | 0.3686 | | 0.4172 | 0.5828 | |
|  |  |  |  |
| UK | |  |  | | --- | --- | | 0.66270.6627 | −0.1500-0.1500 | | (0.6085 , 0.7169) | (-0.1868 , - 0.1132) | | 0.72730.7273 | 0.59310.5931 | | (0.6694 , 0.7852) | (0.5427 , 0.6435) | | |  |  | | --- | --- | | −0.0660-0.0660 |  | | (-0.1440 , 0.0081) |  | |  | 0.30310.3031 | |  | (0.2221 , 0.3841) | | |  |  | | --- | --- | | 0.7231 | 0.2769 | | 0.3855 | 0.6145 | |
|  |  |  |  |
| France | |  |  | | --- | --- | | 0.68750.6875 | −0.0760-0.0760 | | (0.6001 , 0.7741) | (-0.1303 , - 0.0218) | | 0.24450.2445 | 0.668040.66804 | | (0.1893 , 0.2996) | (0.6129 , 0.7231) | | |  |  | | --- | --- | | 0.69330.6933 |  | | (0.5975 , 0.7890) |  | |  | 0.79110.7911 | |  | (0.7507 , 0.8476) | | |  |  | | --- | --- | | 0.3571 | 0.6429 | | 0.6501 | 0.3490 | |
|  |  |  |  |
| Germany | |  |  | | --- | --- | | 0.75150.7515 | −0.2867-0.2867 | | (0.6483 , 0.8547) | (-0.3399 , - 0.2336) | | −0.0054-0.0054 | 0.72580.7258 | | (-0.0580 , 0.0472) | (0.6852 , 0.7665) | | |  |  | | --- | --- | | 0.28840.2884 |  | | (0.1846 , 0.3922) |  | |  | 0.83650.8365 | |  | (0.8006 , 0.8724) | | |  |  | | --- | --- | | 0.3392 | 0.6608 | | 0.6906 | 0.0394 | |
|  |  |  |  |
| Canada | |  |  | | --- | --- | | 0.30860.3086 | −0.2108-0.2108 | | (0.2225 , 0.3948) | (-0.2666 , - 0.1549) | | 0.18380.1838 | 0.69210.6921 | | (0.0638 , 0.3038) | (0.6385 , 0.7456) | | |  |  | | --- | --- | | 0.21600.2160 |  | | (0.1448 , 0.2872) |  | |  | 0.82350.8235 | |  | (0.47784 , 0.8686) | | |  |  | | --- | --- | | 0.6273 | 0.3727 | | 0.3972 | 0.6028 | |
|  |  |  |  |
| Australia | |  |  | | --- | --- | | 0.50050.5005 | 0.04100.0410 | | (0.4368 , 0.5643) | (0.0158 , 0.0662) | | 1.25451.2545 | 0.48550.4855 | | (1.1073 , 1.4020) | (0.4343 , 0.5367) | | |  |  | | --- | --- | | 0.47890.4789 |  | | (0.4242 , 0.5336) |  | |  | 0.51490.5149 | |  | (0.4536 , 0.5762) | | |  |  | | --- | --- | | 0.6604 | 0.3396 | | 0.4245 | 0.5755 | |
|  |  |  |  |

* •

  Confidence interval at 95% level in parenthesis.
* •

  In regime one, regime two and the transition matrix, the reported values follow the positions of the parameters in section 2.1.

Table 9: Monte Carlo Estimation Results for GDP/HD



| GDP/STIR | Regime 1 | Regime 2 | Transition Matrix |
| --- | --- | --- | --- |
| USA | |  |  | | --- | --- | | 0.84740.8474 | −0.7936-0.7936 | | (0.8116 , 0.8832) | (-0.8551 , - 0.7322) | | 0.59700.5970 | 0.33980.3398 | | (0.5618 , 0.6322) | (0.2979 , 0.3818) | | |  |  | | --- | --- | | 0.65370.6537 |  | | (0.6104 , 0.6969) |  | |  | 0.68940.6894 | |  | (0.6534 , 0.7255) | | |  |  | | --- | --- | | 0.7026 | 0.2974 | | 0.3184 | 0.6816 | |
|  |  |  |  |
| UK | |  |  | | --- | --- | | 0.66270.6627 | −0.1500-0.1500 | | (0.6085 , 0.7169) | (-0.1868 , - 0.1132) | | 0.72730.7273 | 0.59310.5931 | | (0.6694 , 0.7852) | (0.5427 , 0.6435) | | |  |  | | --- | --- | | −0.0660-0.0660 |  | | (-0.1440 , 0.0081) |  | |  | 0.30310.3031 | |  | (0.2221 , 0.3841) | | |  |  | | --- | --- | | 0.7231 | 0.2769 | | 0.3855 | 0.6145 | |
|  |  |  |  |
| France | |  |  | | --- | --- | | 0.90160.9016 | −0.6910-0.6910 | | (0.8544 , 0.9487) | (-0.7265 , - 0.6554) | | 0.44460.4446 | 0.10320.1032 | | (0.4083 , 0.4909) | (0.0477 , 0.1587) | | |  |  | | --- | --- | | 0.25700.2570 |  | | (0.1829 , 0.3311) |  | |  | 0.83530.8353 | |  | (0.7505 , 0.9201) | | |  |  | | --- | --- | | 0.7941 | 0.2059 | | 0.3283 | 0.6717 | |
|  |  |  |  |
| Germany | |  |  | | --- | --- | | 0.76400.7640 | −0.6091-0.6091 | | (0.7159 , 0.8122) | (-0.6483 , - 0.5700) | | 0.55160.5516 | 0.26050.2605 | | (0.4827 , 0.6205) | (0.2059 , 0.3152) | | |  |  | | --- | --- | | 0.62780.6278 |  | | (0.5747 , 0.6810) |  | |  | 0.73770.7377 | |  | (0.6926 , 0.7829) | | |  |  | | --- | --- | | 0.6828 | 0.3172 | | 0.3280 | 0.6720 | |
|  |  |  |  |
| Canada | |  |  | | --- | --- | | 0.98860.9886 | −1.0010-1.0010 | | (0.9505 , 1.0267) | (-1.0633 , - 0.9387) | | 0.60110.6011 | 0.02100.0210 | | (0.5713 , 0.6308) | (-0.01515 , 0.0571) | | |  |  | | --- | --- | | 0.50050.5005 |  | | (0.4568 , 0.5443) |  | |  | 0.64710.6471 | |  | (0.5865 , 0.7076) | | |  |  | | --- | --- | | 0.5134 | 0.4876 | | 0.5178 | 0.4822 | |
|  |  |  |  |
| Australia | |  |  | | --- | --- | | 0.56880.5688 | −0.2934-0.2934 | | (0.5152 , 0.6221) | (-0.3559 , -0.2309) | | 0.49550.4955 | 0.31290.3129 | | (0.3702 , 0.6309) | (0.2528 , 0.3729) | | |  |  | | --- | --- | | 0.45990.4599 |  | | (0.3698 , 0.5500) |  | |  | 0.30000.3000 | |  | (0.2010 , 0.3989) | | |  |  | | --- | --- | | 0.7176 | 0.2824 | | 0.4882 | 0.5117 | |
|  |  |  |  |

* •

  Confidence interval at 95% level in parenthesis.
* •

  In regime one, regime two and the transition matrix, the reported values follow the positions of the parameters in section 2.1.

Table 10: Monte Carlo Estimation Results for GDP/STIR