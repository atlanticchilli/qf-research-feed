---
authors:
- Elizabeth Dadzie
- Wilfried Kuissi-Kamdem
- Marcel Ndengo
doc_id: arxiv:2511.03031v1
family_id: arxiv:2511.03031
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Robust optimal consumption, investment and reinsurance for recursive preferences
url_abs: http://arxiv.org/abs/2511.03031v1
url_html: https://arxiv.org/html/2511.03031v1
venue: arXiv q-fin
version: 1
year: 2025
---


Elizabeth Dadzie
Elizabeth Dadzie: Department of Mathematics, University of Ghana, Accra, LG 25, Ghana; African Institute for Mathematical Sciences, Accra, LG DTD 20046, Ghana
[edadzie@aims.edu.gh](mailto:edadzie@aims.edu.gh)
, 
Wilfried Kuissi-Kamdem
Wilfried Kuissi-Kamdem: Department of Mathematics, University of Rwanda, Kigali, 4285, Rwanda; African Institute for Mathematical Sciences, Accra, LG DTD 20046, Ghana; Department of Mathematical Stochastics, University of Freiburg, Freiburg, 79104, Germany
[donatien@aims.edu.gh, wilfried.kuissi.kamdem@stochastik.uni-freiburg.de](mailto:donatien@aims.edu.gh,%20wilfried.kuissi.kamdem@stochastik.uni-freiburg.de)
 and 
Marcel Ndengo
Marcel Ndengo: Department of Mathematics, University of Rwanda, Kigali, 4285, Rwanda
[serandengo@gmail.com](mailto:serandengo@gmail.com)

###### Abstract.

This paper investigates a robust optimal consumption, investment, and reinsurance problem for an insurer with Epstein-Zin recursive preferences operating under model uncertainty. The insurer’s surplus follows the diffusion approximation of the Cramér-Lundberg model, and the insurer can purchase proportional reinsurance. Model ambiguity is characterised by a class of equivalent probability measures, and the insurer, being ambiguity-averse, aims to maximise utility under the worst-case scenario. By solving the associated coupled forward-backward stochastic differential equation (FBSDE), we derive closed-form solutions for the optimal strategies and the value function. Our analysis reveals how ambiguity aversion, risk aversion, and the elasticity of intertemporal substitution (EIS) influence the optimal policies. Numerical experiments illustrate the effects of key parameters, showing that optimal consumption decreases with higher risk aversion and EIS, while investment and reinsurance strategies are co-dependent on both financial and insurance market parameters, even without correlation. This study provides a comprehensive framework for insurers to manage capital allocation and risk transfer under deep uncertainty.

###### Key words and phrases:

Consumption-investment-reinsurance strategies, Epstein-Zin recursive utility, Model uncertainty, Forward-backward stochastic differential equations.

###### 2020 Mathematics Subject Classification:

Primary 91B05, 91G05, 91G10; Secondary 91G80s

This work was supported by a grant from the African Institute for Mathematical Sciences, with financial support from the Government of Canada, provided through Global Affairs Canada, and the International Development Research Centre.

## 1. Introduction

The optimal management of an insurance’s wealth requires balancing between different sources of risk and return: the allocation of funds in the financial market via investment decisions and the transfer of insurance (underwriting) risk through reinsurance. Classical financial economics and actuarial research has studied these problems extensively under expected utility theory; see [[10](https://arxiv.org/html/2511.03031v1#bib.bib10)] and reference therein. In this formulation, the insurer (or investor) maximises classical time-additive utilities of terminal wealth.

However, from an economics point of view, the main unattractive feature of time-additive preferences is the fact that they fail to separate investors’ desire to smooth consumption across states of nature (measured by the coefficient of risk aversion) and investors’ willingness to smooth consumption over time (measured by the coefficient of elasticity of intertemporal substitution EIS); see [[12](https://arxiv.org/html/2511.03031v1#bib.bib12), on pp.227-228] for more details. This limitation has led to a considerable amount of current theoretical and empirical research in finance and economics based on more general dynamic risk preferences.

One of the most popular response in the literature are recursive preferences. Such preferences allow to disentangle the link between risk aversion and EIS; thanks to the postulate that current consumption depend on the value of future consumption. Arguably the most popular among recursive utilities is the Epstein-Zin utility as proposed in [[4](https://arxiv.org/html/2511.03031v1#bib.bib4)]. Since then the Epstein-Zin utility has been widely used in a variety of different contexts covering asset pricing, decision theory, business cycles and growth, and monetary economics. However, despite the established and rapid growing literature on consumption and investment problems with recursive utilities, to the best of our knowledge no research has ever solved such problems when reinsurance is taken into account.

There is by now ample evidence in the literature that both insurers and investors operate under model uncertainty: the true drift or volatility of asset returns, and the intensity or severity of claims, may not be known with certainty; see [[3](https://arxiv.org/html/2511.03031v1#bib.bib3)] for a review. In the presence of such ambiguity, a robust decision maker evaluates outcomes under a set of plausible probability measures and maximises utility against the worst-case scenario. Robust control theory (see [[5](https://arxiv.org/html/2511.03031v1#bib.bib5), [9](https://arxiv.org/html/2511.03031v1#bib.bib9)]) integrates this feature by introducing an additional minimisation over alternative measures, penalised by a relative-entropy term. Combining Epstein–Zin utilities with robustness yields robust recursive preferences, which capture both the investors’ intertemporal trade-offs and their concern for model misspecification. For insurers, this provides a realistic framework for studying capital allocation, reinsurance design, and consumption smoothing under deep uncertainty.

In the present paper, we incorporate ambiguity aversion to study the optimal robust consumption (“dividend”, “refund”,…), investment and reinsurance problem through maximising, over a finite time-horizon, the Epstein-Zin recursive utility. A further improvement arises from the fact that we consider an insurer subject to a liability at the end of the investment period. We obtain closed-form solutions for the robust optimal consumption, investment-reinsurance strategy and the corresponding value function by adopting an extension of a well-known technique proposed by [[6](https://arxiv.org/html/2511.03031v1#bib.bib6)] (for time-additive utility) and [[12](https://arxiv.org/html/2511.03031v1#bib.bib12)] (for Epstein-Zin utility). This extension has been introduced in [[7](https://arxiv.org/html/2511.03031v1#bib.bib7)] to study a consumption-investment optimisation problem with liability and Epstein-Zin utility under partial information. In order to analyse the effect of ambiguity and the utility’s parameters (risk aversion coefficient and EIS coefficient) on the optimal strategy, we consider three special cases, i.e., uncorrelated claims, without ambiguity, and with ambiguity. Finally, we perform some numerical experiments to illustrate the robust optimal consumption, investment-reinsurance strategy.

The remainder of the present paper is structured as follows. Section [2.1](https://arxiv.org/html/2511.03031v1#S2.SS1 "2.1. Probability setting and wealth process of the insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") introduces the financial–insurance market model and the insurer’s wealth dynamics under proportional reinsurance. In Section [2.2](https://arxiv.org/html/2511.03031v1#S2.SS2 "2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") we formulate the robust stochastic optimisation problem. In Section [3](https://arxiv.org/html/2511.03031v1#S3 "3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") we give the main results of this paper. In Section [4](https://arxiv.org/html/2511.03031v1#S4 "4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") we perform some numerical analysis. Finally, Section [5](https://arxiv.org/html/2511.03031v1#S5 "5. Conclusion ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") summarises this paper.

## 2. Model and problem formulation

### 2.1. Probability setting and wealth process of the insurer

We consider a filtered probability space (Ω,ℱ,(ℱt)0≤t≤T,ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{0\leq t\leq T},\mathbb{P}) generated by a 22-dimensional Brownian motion B=(W,Wr​e)B=(W,W^{re}). The filtration (ℱt)0≤t≤T(\mathcal{F}\_{t})\_{0\leq t\leq T} is assumed to satisfy the usual conditions of completeness and right-continuity, so that we can take càdlàg versions for semi-martingales. We define some known spaces of stochastic processes.

* (i)(i)

  Let 𝒞\mathcal{C} be the set of non-negative progressively measurable processes on [0,T]×Ω[0,T]\times\Omega.
* (i​i)(ii)

  Let ℋℙq,q≥1\mathcal{H}\_{\mathbb{P}}^{q},~q\geq 1, denotes the space of progressively measurable ℝ\mathbb{R}-valued processes (Yt)0≤t≤T(Y\_{t})\_{0\leq t\leq T} such that ‖Y‖ℋℙq=𝔼​[∫0T|Yt|q​dt]1/q<∞\|Y\|\_{\mathcal{H}\_{\mathbb{P}}^{q}}=\mathbb{E}[\int\_{0}^{T}|Y\_{t}|^{q}\mathrm{d}t]^{1/q}<\infty.
* (i​i​i)(iii)

  Let Ξℙq,q≥1\Xi\_{\mathbb{P}}^{q},~q\geq 1, denotes the space of predictable ℝ2\mathbb{R}^{2}-valued processes
    
  (Zt)0≤t≤T(Z\_{t})\_{0\leq t\leq T} such that ‖Z‖Ξℙq=𝔼​[exp⁡(q2​∫0T‖Zt‖2​dt)]1/q<∞\|Z\|\_{\Xi\_{\mathbb{P}}^{q}}=\mathbb{E}[\exp\big(\frac{q}{2}\int\_{0}^{T}\|Z\_{t}\|^{2}\mathrm{d}t\big)]^{1/q}<\infty.
* (i​v)(iv)

  Let ℍℙq,q≥1\mathbb{H}\_{\mathbb{P}}^{q},~q\geq 1, denotes the space of predictable ℝ2\mathbb{R}^{2}-valued processes
    
  (Zt)0≤t≤T(Z\_{t})\_{0\leq t\leq T} such that ‖Z‖ℍℙq=𝔼​[(∫0T‖Zt‖2​dt)q2]1/q<∞\|Z\|\_{\mathbb{H}\_{\mathbb{P}}^{q}}=\mathbb{E}[(\int\_{0}^{T}\|Z\_{t}\|^{2}\mathrm{d}t)^{\frac{q}{2}}]^{1/q}<\infty.

Note that similar spaces can be defined under another probability measure ℚ\mathbb{Q}, by replacing ℙ\mathbb{P} with ℚ\mathbb{Q} in the subscripts of the corresponding spaces, and taking expectations with respect to ℚ\mathbb{Q}.

Now, we can introduce the wealth process, under ℙ\mathbb{P}, of an insurer. We consider a dynamic financial-insurance environment with two traded assets and the surplus process of the insurer. The traded assets consist of one riskless bond S0S^{0} and one risky asset SS with dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​St0=r​St0​d​t,S00>0,d​St=St​((r+μ)​d​t+σ​d​Wt),S0>0.\displaystyle\begin{cases}\mathrm{d}S\_{t}^{0}&=rS\_{t}^{0}\mathrm{d}t,~S\_{0}^{0}>0,\\ \mathrm{d}S\_{t}&=S\_{t}\left((r+\mu)\mathrm{d}t+\sigma\mathrm{d}W\_{t}\right),~S\_{0}>0.\end{cases} |  | (2.1) |

We assume that, without reinsurance, the surplus process U^\widehat{U} of the insurer satisfies the diffusion approximation of the classical Cramér-Lundberg model (see, e.g., [[1](https://arxiv.org/html/2511.03031v1#bib.bib1), Sect. IV.8] or [[8](https://arxiv.org/html/2511.03031v1#bib.bib8)])

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​U^t\displaystyle\mathrm{d}\widehat{U}\_{t} | =κ​ζ​d​t−κ​β​(ρS​d​Wt+ρr​e​d​Wtr​e)\displaystyle=\kappa\zeta\mathrm{d}t-\sqrt{\kappa\beta}\big(\rho^{S}\mathrm{d}W\_{t}+\rho^{re}\mathrm{d}W\_{t}^{re}\big) |  | (2.2) |

where ρS,ρr​e∈[−1,1]\rho^{S},\rho^{re}\in[-1,1] are the correlation coefficients such that ρr​e≠0\rho^{re}\neq 0 and (ρS)2+(ρr​e)2=1(\rho^{S})^{2}+(\rho^{re})^{2}=1, κ​ζ\kappa\zeta is the claim rate at t∈[0,T]t\in[0,T], and ζ,κ,β>0\zeta,\kappa,\beta>0. The insurance company participates in the reinsurance market and buys proportional reinsurance πtr​e\pi\_{t}^{re} at every time t∈[0,T]t\in[0,T]. As in [[2](https://arxiv.org/html/2511.03031v1#bib.bib2)], the reinsurance strategy πtr​e\pi\_{t}^{re} is allowed to be greater than 11; expressing the situation in which the insurance company also acts as reinsurer of other insurance companies. At any time tt, the insurance company retains 100​πtr​e%100\pi\_{t}^{re}\% of the total claims while the reinsurer undertakes the rest 100​(1−πtr​e)%100(1-\pi\_{t}^{re})\%. Using expected value principle the insurer and the reinsurer premium rates are determined by (1+νi​n)​κ​ζ(1+\nu^{in})\kappa\zeta and (1+νr​e)​κ​ζ(1+\nu^{re})\kappa\zeta, respectively, where νi​n\nu^{in} is the safety loading of the insurer and νr​e\nu^{re} the safety loading of the reinsurer. We exclude the insurer’s arbitrage opportunity by assuming νr​e>νi​n\nu^{re}>\nu^{in}. Hence, the modified dynamics of the insurer’s surplus is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Ut\displaystyle\mathrm{d}U\_{t} | =((1+νi​n)​κ​ζ−(1−πtr​e)​(1+νr​e)​κ​ζ)−πtr​e​d​U^t\displaystyle=\big((1+\nu^{in})\kappa\zeta-(1-\pi\_{t}^{re})(1+\nu^{re})\kappa\zeta\big)-\pi\_{t}^{re}\mathrm{d}\widehat{U}\_{t} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(νi​n−νr​e+πtr​e​νr​e)​κ​ζ​d​t+πtr​e​κ​β​(ρS​d​Wt+ρr​e​d​Wtr​e).\displaystyle=\big(\nu^{in}-\nu^{re}+\pi\_{t}^{re}\nu^{re}\big)\kappa\zeta\mathrm{d}t+\pi\_{t}^{re}\sqrt{\kappa\beta}\big(\rho^{S}\mathrm{d}W\_{t}+\rho^{re}\mathrm{d}W\_{t}^{re}\big). |  | (2.3) |

In addition to choosing an amount of reinsurance πtr​e\pi\_{t}^{re}, t∈[0,T]t\in[0,T], the insurer also chooses her consumption rate ctc\_{t} (in the form of “dividend”, “refund”,…) and an amount to be invested in the risky assets (investment strategy) πtS\pi\_{t}^{S}. For such (c,πS,πr​e)(c,\pi^{S},\pi^{re}), the wealth process X~\widetilde{X} of the company with initial endowment x≥0x\geq 0 at time 0 evolves according to the stochastic differential equation (SDE)

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​X~t\displaystyle\mathrm{d}\widetilde{X}\_{t} | =r​X~t​d​t+πtS​μ​d​t+πtS​d​Wt−ct​d​t+d​Ut\displaystyle=r\widetilde{X}\_{t}\mathrm{d}t+\pi\_{t}^{S}\mu\mathrm{d}t+\pi\_{t}^{S}\mathrm{d}W\_{t}-c\_{t}\mathrm{d}t+\mathrm{d}U\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =r​X~t​d​t+(πtS​μ+πtr​e​νr​e​κ​ζ)​d​t+(νi​n−νr​e)​κ​ζ​d​t+πtS​σ​d​Wt\displaystyle=r\widetilde{X}\_{t}\mathrm{d}t+\Big(\pi\_{t}^{S}\mu+\pi\_{t}^{re}\nu^{re}\kappa\zeta\Big)\mathrm{d}t+\big(\nu^{in}-\nu^{re}\big)\kappa\zeta\mathrm{d}t+\pi\_{t}^{S}\sigma\mathrm{d}W\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +πtr​e​κ​β​(ρS​d​Wt+ρr​e​d​Wtr​e)\displaystyle\phantom{X}+\pi\_{t}^{re}\sqrt{\kappa\beta}\big(\rho^{S}\mathrm{d}W\_{t}+\rho^{re}\mathrm{d}W\_{t}^{re}\big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =r​X~t​d​t+πt⊺​η​d​t+πt⊺​d​Bt+(νi​n−νr​e)​κ​ζ​d​t−ct​d​t,\displaystyle=r\widetilde{X}\_{t}\mathrm{d}t+\pi\_{t}^{\intercal}\eta\mathrm{d}t+\pi\_{t}^{\intercal}\mathrm{d}B\_{t}+\big(\nu^{in}-\nu^{re}\big)\kappa\zeta\mathrm{d}t-c\_{t}\mathrm{d}t, |  | (2.4) |

where Σ:=(σ0ρSκ​β​ρr​e)\Sigma:=\left(\begin{matrix}\sigma&0\\
\rho^{S}&\sqrt{\kappa\beta}\rho^{re}\end{matrix}\right), η:=Σ−1​(μνr​e​κ​ζ)\eta:=\Sigma^{-1}\left(\begin{matrix}\mu\\
\nu^{re}\kappa\zeta\end{matrix}\right) and πt⊺:=(πtS,πtr​e)​Σ,0≤t≤T\pi\_{t}^{\intercal}:=\big(\pi\_{t}^{S},\pi\_{t}^{re}\big)\Sigma,~0\leq t\leq T.

As in [[8](https://arxiv.org/html/2511.03031v1#bib.bib8)], instead of working with the wealth process (X~t)0≤t≤T(\widetilde{X}\_{t})\_{0\leq t\leq T} itself, we consider its self-financing form process given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt:=X~t+(νi​n−νr​e)​κ​ζ​∫tTe−r​(s−t)​ds​ for ​t∈[0,T].\displaystyle X\_{t}:=\widetilde{X}\_{t}+\big(\nu^{in}-\nu^{re}\big)\kappa\zeta\int\_{t}^{T}e^{-r(s-t)}\mathrm{d}s~\text{ for ~}t\in[0,T]. |  | (2.5) |

Clearly, XT=X~TX\_{T}=\widetilde{X}\_{T}. Hence, Equation ([2.1](https://arxiv.org/html/2511.03031v1#S2.Ex2 "2.1. Probability setting and wealth process of the insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) transforms to

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt\displaystyle\mathrm{d}X\_{t} | =d​X~t+r​(νi​n−νr​e)​κ​ζ​∫tTe−r​(s−t)​ds−(νi​n−νr​e)​κ​ζ​d​t\displaystyle=\mathrm{d}\widetilde{X}\_{t}+r\big(\nu^{in}-\nu^{re}\big)\kappa\zeta\int\_{t}^{T}e^{-r(s-t)}\mathrm{d}s-\big(\nu^{in}-\nu^{re}\big)\kappa\zeta\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =r​X~t​d​t+πt⊺​η​d​t+πt⊺​d​Bt−ct​d​t+r​(νi​n−νr​e)​κ​ζ​∫tTe−r​(s−t)​ds\displaystyle=r\widetilde{X}\_{t}\mathrm{d}t+\pi\_{t}^{\intercal}\eta\mathrm{d}t+\pi\_{t}^{\intercal}\mathrm{d}B\_{t}-c\_{t}\mathrm{d}t+r\big(\nu^{in}-\nu^{re}\big)\kappa\zeta\int\_{t}^{T}e^{-r(s-t)}\mathrm{d}s |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =r​Xt​d​t+πt⊺​η​d​t+πt⊺​d​Bt−ct​d​t,\displaystyle=rX\_{t}\mathrm{d}t+\pi\_{t}^{\intercal}\eta\mathrm{d}t+\pi\_{t}^{\intercal}\mathrm{d}B\_{t}-c\_{t}\mathrm{d}t, |  | (2.6) |

with X0=x+(νi​n−νr​e)​κ​ζ​∫0Te−r​s​dsX\_{0}=x+\big(\nu^{in}-\nu^{re}\big)\kappa\zeta\int\_{0}^{T}e^{-rs}\mathrm{d}s.

### 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer

The framework given in Section [2.1](https://arxiv.org/html/2511.03031v1#S2.SS1 "2.1. Probability setting and wealth process of the insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") concerned an insurer who has total confidence in model ([2.1](https://arxiv.org/html/2511.03031v1#S2.Ex5 "2.1. Probability setting and wealth process of the insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) under the probability measure ℙ\mathbb{P}. However, in practice insurers are concerned about model misspecification generated by the deviation from the reference probability measure ℙ\mathbb{P}. We shall then integrate the probability distribution uncertainty into the consumption-investment-reinsurance optimisation problem of an ambiguity-averse insurer (AAI). To define alternative models, we consider other probability measures—equivalent to the reference measure ℙ\mathbb{P}—defined, via Radon-Nykodim derivative, by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℚξd​ℙ|ℱT:=exp⁡(−12​∫0T‖ξs‖2​ds−∫0Tξs⊺​dBs),\displaystyle\frac{\mathrm{d}\mathbb{Q}^{\xi}}{\mathrm{d}\mathbb{P}}\Big|\_{\mathcal{F}\_{T}}:=\exp\Big(-\frac{1}{2}\int\_{0}^{T}\|\xi\_{s}\|^{2}\mathrm{d}s-\int\_{0}^{T}\xi\_{s}^{\intercal}\mathrm{d}B\_{s}\Big), |  | (2.7) |

where ξ:=(ξS,ξr​e)⊺∈Ξℙ2\xi:=(\xi^{S},\xi^{re})^{\intercal}\in\Xi\_{\mathbb{P}}^{2} is called the distortion process. According to Girsanov’s theorem, we can define on the probability measure ℚξ\mathbb{Q}^{\xi} the following Brownian motions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wtℚξ:=Wt+∫0tξsS​ds​ and ​Wtr​e,ℚξ:=Wtr​e+∫0tξsr​e​ds,\displaystyle W\_{t}^{\mathbb{Q}^{\xi}}:=W\_{t}+\int\_{0}^{t}\xi\_{s}^{S}\mathrm{d}s~\text{ and }~W\_{t}^{re,\mathbb{Q}^{\xi}}:=W\_{t}^{re}+\int\_{0}^{t}\xi\_{s}^{re}\mathrm{d}s, |  | (2.8) |

or, equivalently, Btℚξ:=Bt+∫0tξs​dsB\_{t}^{\mathbb{Q}^{\xi}}:=B\_{t}+\int\_{0}^{t}\xi\_{s}\mathrm{d}s for t∈[0,T]t\in[0,T].

Under ℚξ\mathbb{Q}^{\xi}, the dynamics of the wealth process XX in ([2.1](https://arxiv.org/html/2511.03031v1#S2.Ex5 "2.1. Probability setting and wealth process of the insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) becomes

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Xt\displaystyle\mathrm{d}X\_{t} | =r​Xt​d​t+πt⊺​η​d​t+πt⊺​d​Btℚξ−ct​d​t−πt⊺​ξt​d​t.\displaystyle=rX\_{t}\mathrm{d}t+\pi\_{t}^{\intercal}\eta\mathrm{d}t+\pi\_{t}^{\intercal}\mathrm{d}B\_{t}^{\mathbb{Q}^{\xi}}-c\_{t}\mathrm{d}t-\pi\_{t}^{\intercal}\xi\_{t}\mathrm{d}t. |  | (2.9) |

An AAI’s preference over 𝒞\mathcal{C}-valued consumption and Ξℙ2\Xi\_{\mathbb{P}}^{2}-valued distortion is given by a robust version of the classical continuous-time stochastic differential utility of Epstein-Zin type. To describe this preference, let δ>0\delta>0 represent the discounting rate, 0<γ≠10<\gamma\neq 1 be the relative risk aversion, and 0<ψ≠10<\psi\neq 1 be the elasticity of intertemporal substitution coefficient (EIS). Then, the Epstein–Zin aggregator is defined by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f​(c,v)\displaystyle f(c,v) | :=δ​e−δ​t​c1−1ψ1−1ψ​((1−γ)​v)1−1θ, with ​θ:=1−γ1−1ψ,\displaystyle:=\delta e^{-\delta t}\frac{c^{1-\frac{1}{\psi}}}{1-\frac{1}{\psi}}((1-\gamma)v)^{1-\frac{1}{\theta}},\text{ with }~\theta:=\frac{1-\gamma}{1-\frac{1}{\psi}}, |  | (2.10) |

and the bequest utility function by h​(c):=e−δ​θ​T​c1−γ1−γh(c):=e^{-\delta\theta T}\frac{c^{1-\gamma}}{1-\gamma}. Hence, the robust Epstein-Zin utility over the consumption stream c∈𝒞c\in\mathcal{C} and the distortion process ξ∈Ξℙ2\xi\in\Xi\_{\mathbb{P}}^{2} on a finite time horizon TT is a process (Vtc,ξ)t∈[0,T](V\_{t}^{c,\xi})\_{t\in[0,T]} which satisfies

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vtc,ξ\displaystyle V\_{t}^{c,\xi} | =𝔼tℚξ​[h​(cT)+∫tT(f​(cs,Vsc,ξ)+12​Ψs​‖ξs‖2)​ds]​for ​t∈[0,T],\displaystyle=\mathbb{E}\_{t}^{\mathbb{Q}^{\xi}}\Big[h(c\_{T})+\int\_{t}^{T}\Big(f(c\_{s},V\_{s}^{c,\xi})+\frac{1}{2\Psi\_{s}}\|\xi\_{s}\|^{2}\Big)\mathrm{d}s\Big]~\text{for }t\in[0,T], |  | (2.11) |

where (Ψt)t∈[0,T](\Psi\_{t})\_{t\in[0,T]} is a non-negative process which captures the AAI’s ambiguity aversion. Here, 𝔼tℚξ​[⋅]\mathbb{E}\_{t}^{\mathbb{Q}^{\xi}}[\cdot] stands for the conditional expectation 𝔼ℚξ[⋅|ℱt]\mathbb{E}^{\mathbb{Q}^{\xi}}[\cdot|\mathcal{F}\_{t}] under ℚξ\mathbb{Q}^{\xi}. Following [[9](https://arxiv.org/html/2511.03031v1#bib.bib9)], we adopt a homothetic robustness preference by defining Ψ\Psi via

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψt:=Φ(1−γ)​Vtc,ξ​ for ​t∈[0,T],\displaystyle\Psi\_{t}:=\frac{\Phi}{(1-\gamma)V\_{t}^{c,\xi}}~\text{ for }t\in[0,T], |  | (2.12) |

with Φ≥0\Phi\geq 0 denoting the ambiguity aversion parameter. Hence, the robust recursive utility process Vc,ξV^{c,\xi} in ([2.11](https://arxiv.org/html/2511.03031v1#S2.E11 "In 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) becomes

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vtc,ξ\displaystyle V\_{t}^{c,\xi} | =𝔼tℚξ​[h​(cT)+∫tT(f​(cs,Vsc,ξ)+12​Φ​‖ξs‖2​(1−γ)​Vsc,ξ)​ds],0≤t≤T.\displaystyle=\mathbb{E}\_{t}^{\mathbb{Q}^{\xi}}\Big[h(c\_{T})+\int\_{t}^{T}\Big(f(c\_{s},V\_{s}^{c,\xi})+\frac{1}{2\Phi}\|\xi\_{s}\|^{2}(1-\gamma)V\_{s}^{c,\xi}\Big)\mathrm{d}s\Big],~0\leq t\leq T. |  | (2.13) |

For the analysis in our paper, we study the case

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ>1​ and ​ψ>1.\displaystyle\gamma>1~\text{ and }~\psi>1. |  | (2.14) |

Our interest in the parameter specification in ([2.14](https://arxiv.org/html/2511.03031v1#S2.E14 "In 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) originates mainly from its empirical evidence on consumption and portfolio decisions; see [[12](https://arxiv.org/html/2511.03031v1#bib.bib12), on p.228].

Without the distortion term in the generator of ([2.13](https://arxiv.org/html/2511.03031v1#S2.E13 "In 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) (no ambiguity), existence and uniqueness results are well-established (see [[12](https://arxiv.org/html/2511.03031v1#bib.bib12), Prop. 2.2]). To guarantee the existence of a suitable unique solution to ([2.13](https://arxiv.org/html/2511.03031v1#S2.E13 "In 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")), for non-zero distortion term, we consider the following set of admissible consumption and distortion streams.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒜a:={(c,ξ)∈𝒞×Ξℚξ2|\displaystyle\mathcal{A}\_{a}:=\Big\{(c,\xi)\in\mathcal{C}\times\Xi\_{\mathbb{Q}^{\xi}}^{2}~\big| | 𝔼ℚξ[∫0Te−δ​scs1−1ψds]<∞ and 𝔼ℚξ[e∫0T12​Φ​‖ξs‖2​dscT1−γ]<∞}.\displaystyle~\mathbb{E}^{\mathbb{Q}^{\xi}}\Big[\int\_{0}^{T}e^{-\delta s}c\_{s}^{1-\frac{1}{\psi}}\mathrm{d}s\Big]<\infty~\text{ and }~\mathbb{E}^{\mathbb{Q}^{\xi}}\big[e^{\int\_{0}^{T}\frac{1}{2\Phi}\|\xi\_{s}\|^{2}\mathrm{d}s}c\_{T}^{1-\gamma}\big]<\infty\Big\}. |  | (2.15) |

###### Proposition 2.1.

Suppose γ,ψ>1\gamma,\psi>1 and (c,ξ)∈𝒜a(c,\xi)\in\mathcal{A}\_{a}. Then ([2.13](https://arxiv.org/html/2511.03031v1#S2.E13 "In 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) admits a unique solution Vc,ξV^{c,\xi}, with Vc,ξV^{c,\xi} continuous, strictly negative and of class (D). Moreover, there exists a square integrable process Zc,ξZ^{c,\xi} such that for t∈[0,T]t\in[0,T],

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vtc,ξ\displaystyle V\_{t}^{c,\xi} | =h​(cT)+∫tT(f​(cs,Vsc,ξ)+12​Φ​‖ξs‖2​(1−γ)​Vsc,ξ)​ds−∫tTZtc,ξ​dBsℚξ.\displaystyle=h(c\_{T})+\int\_{t}^{T}\Big(f(c\_{s},V\_{s}^{c,\xi})+\frac{1}{2\Phi}\|\xi\_{s}\|^{2}(1-\gamma)V\_{s}^{c,\xi}\Big)\mathrm{d}s-\int\_{t}^{T}Z\_{t}^{c,\xi}\mathrm{d}B\_{s}^{\mathbb{Q}^{\xi}}. |  | (2.16) |

###### Proof.

See Appendix [A](https://arxiv.org/html/2511.03031v1#A1 "Appendix A Proof of Proposition 2.1 ‣ Robust optimal consumption, investment and reinsurance for recursive preferences").
∎

In this section, we are interested in the optimal consumption, investment and reinsurance problem of an AAI with a constant liability G∈ℝG\in\mathbb{R} at terminal time TT and robust recursive preference of Epstein-Zin type. Note that GG is not necessarily positive. Hence, we want to find the best strategy (c^,π^,ξ^)(\widehat{c},\widehat{\pi},\widehat{\xi}) solution to the optimization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | supc,πinfξ𝔼ℚξ​[h​(XTc,π,ξ−G)+∫0T(f​(cs,Vsc,ξ)+12​Φ​‖ξ‖2​(1−γ)​Vsc,ξ)​ds],\displaystyle\sup\_{c,\pi}~\inf\_{\xi}~\mathbb{E}^{\mathbb{Q}^{\xi}}\Big[h(X\_{T}^{c,\pi,\xi}-G)+\int\_{0}^{T}\Big(f(c\_{s},V\_{s}^{c,\xi})+\frac{1}{2\Phi}\|\xi\|^{2}(1-\gamma)V\_{s}^{c,\xi}\Big)\mathrm{d}s\Big], |  | (2.17) |

where Xc,π,ξX^{c,\pi,\xi} denotes the solution to the SDE ([2.9](https://arxiv.org/html/2511.03031v1#S2.E9 "In 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) associated to the consumption cc, the investment-reinsurance strategy π\pi and the distortion process ξ\xi, with π⊺:=((πS)⊺,πr​e)​Σ\pi^{\intercal}:=\big((\pi^{S})^{\intercal},\pi^{re}\big)\Sigma (see the definition of Σ\Sigma just below ([2.1](https://arxiv.org/html/2511.03031v1#S2.Ex2 "2.1. Probability setting and wealth process of the insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences"))).

To define the set of admissible consumption, investment, reinsurance and distortion strategies, we introduce the BSDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Yt\displaystyle\mathrm{d}Y\_{t} | =−(ℋ​(t,Xtc,π,ξ,Yt,Zt)+Zt⊺​ξt)​d​t+Zt⊺​d​Btℚξ,YT=−e−r​T​G,\displaystyle=-\big(\mathcal{H}(t,X\_{t}^{c,\pi,\xi},Y\_{t},Z\_{t})+Z\_{t}^{\intercal}\xi\_{t}\big)\mathrm{d}t+Z\_{t}^{\intercal}\mathrm{d}B\_{t}^{\mathbb{Q}^{\xi}},\quad Y\_{T}=-e^{-rT}G, |  | (2.18) |

where the function ℋ\mathcal{H} is to be defined. Hence, we define the set of admissible consumption, investment, reinsurance and distortion strategies as follows.

###### Definition 2.2.

A triple (c,π,ξ)(c,\pi,\xi) of consumption, investment-reinsurance and distortion strategies is admissible if

* 1.

  (c,ξ)∈𝒜a(c,\xi)\in\mathcal{A}\_{a} with cT=XTc,π,ξ+er​T​YTc\_{T}=X\_{T}^{c,\pi,\xi}+e^{rT}Y\_{T};
* 2.

  Xtc,π,ξ+er​t​Yt>0X\_{t}^{c,\pi,\xi}+e^{rt}Y\_{t}>0 for all t∈[0,T]t\in[0,T];
* 3.

  (X⋅c,π,ξ+er⁣⋅​Y⋅)1−γ(X\_{\cdot}^{c,\pi,\xi}+e^{r\cdot}Y\_{\cdot})^{1-\gamma} is of class (D) under ℙ\mathbb{P}.

We denote by 𝒜A​A​I\mathcal{A}^{AAI} the set of admissible consumption, investment-reinsurance and distortion strategies. Therefore, we are interested in the following problem:

###### Problem 2.3.

Find (c^,π^,ξ^)∈𝒜A​A​I(\widehat{c},\widehat{\pi},\widehat{\xi})\in\mathcal{A}^{AAI} such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝒱A​A​I:=V0c^,π^,ξ^:=supinf(c,π,ξ)∈𝒜A​A​I​𝔼ℚξ​[h​(XTc,π,ξ−G)+∫0T(f​(cs,Vsc,ξ)+12​Φ​‖ξ‖2​(1−γ)​Vsc,ξ)​ds].\displaystyle\mathcal{V}^{AAI}:=V\_{0}^{\widehat{c},\widehat{\pi},\widehat{\xi}}:=\underset{(c,\pi,\xi)\in\mathcal{A}^{AAI}}{\sup~\inf}\mathbb{E}^{\mathbb{Q}^{\xi}}\Big[h(X\_{T}^{c,\pi,\xi}-G)+\int\_{0}^{T}\Big(f(c\_{s},V\_{s}^{c,\xi})+\frac{1}{2\Phi}\|\xi\|^{2}(1-\gamma)V\_{s}^{c,\xi}\Big)\mathrm{d}s\Big]. |  | (2.19) |

## 3. Solution to the AAI’s stochastic optimisation problem

We speculate that the optimal utility process takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | V^t=e−δ​θ​t​(Xt+er​t​Yt)1−γ1−γ,0≤t≤T,\displaystyle\widehat{V}\_{t}={e^{-\delta\theta t}}\frac{(X\_{t}+e^{rt}Y\_{t})^{1-\gamma}}{1-\gamma},\quad 0\leq t\leq T, |  | (3.1) |

where (Y,Z)(Y,Z) is the solution to the BSDE ([2.18](https://arxiv.org/html/2511.03031v1#S2.E18 "In 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")). We define the process

|  |  |  |  |
| --- | --- | --- | --- |
|  | M⋅c,π,ξ\displaystyle M\_{\cdot}^{c,\pi,\xi} | :=e−δ​θ​t​(X⋅+er⁣⋅​Y⋅)1−γ1−γ\displaystyle:={e^{-\delta\theta t}}\frac{(X\_{\cdot}+e^{r\cdot}Y\_{\cdot})^{1-\gamma}}{1-\gamma} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫0⋅(f​(cs,e−δ​θ​s​(Xs+er​s​Ys)1−γ1−γ)+12​Φ​‖ξ‖2​(Xs+er​s​Ys)1−γ)​ds.\displaystyle\phantom{xx}+\int\_{0}^{\cdot}\Big(f\big(c\_{s},e^{-\delta\theta s}\frac{(X\_{s}+e^{rs}Y\_{s})^{1-\gamma}}{1-\gamma}\big)+\frac{1}{2\Phi}\|\xi\|^{2}(X\_{s}+e^{rs}Y\_{s})^{1-\gamma}\Big)\mathrm{d}s. |  | (3.2) |

From the martingale optimality principle, the function ℋ\mathcal{H} in ([2.18](https://arxiv.org/html/2511.03031v1#S2.E18 "In 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) must be chosen according to the following rules:

* (1)(1)

  For any (c,π)(c,\pi), the process Mc,π,ξM^{c,\pi,\xi} is a local submartingale for all ξ\xi such that (c,π,ξ)∈𝒜A​A​I(c,\pi,\xi)\in\mathcal{A}^{AAI}.
* (2)(2)

  For any ξ\xi, the process Mc,π,ξM^{c,\pi,\xi} is a local supermartingale for all (c,π)(c,\pi) such that (c,π,ξ)∈𝒜A​A​I(c,\pi,\xi)\in\mathcal{A}^{AAI}.
* (3)(3)

  There exists a (c^,π^,ξ^)∈𝒜A​A​I(\widehat{c},\widehat{\pi},\widehat{\xi})\in\mathcal{A}^{AAI} such that Mc^,π^,ξ^M^{\widehat{c},\widehat{\pi},\widehat{\xi}} is a local martingale.

Recall ff defined in ([2.10](https://arxiv.org/html/2511.03031v1#S2.E10 "In 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")). Set ℋt:=ℋ​(t,Xt,Yt,Zt)\mathcal{H}\_{t}:=\mathcal{H}(t,X\_{t},Y\_{t},Z\_{t}) for all t∈[0,T]t\in[0,T]. To find ℋ\mathcal{H}, we apply Itô’s formula to Mc,π,ξM^{c,\pi,\xi} in ([3](https://arxiv.org/html/2511.03031v1#S3.Ex1 "3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) and obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Mtc,π,ξ\displaystyle\mathrm{d}M\_{t}^{c,\pi,\xi} | =−δ​θ​e−δ​θ​t​(Xt+er​t​Y0)1−γ1−γ​d​t+r​er​t​Yt​e−δ​θ​t​(Xt+er​t​Yt)−γ​d​t\displaystyle=-\delta\theta{e^{-\delta\theta t}}\frac{(X\_{t}+e^{rt}Y^{0})^{1-\gamma}}{1-\gamma}\mathrm{d}t+re^{rt}Y\_{t}e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma}\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +e−δ​θ​t​(Xt+er​t​Yt)−γ​d​Xt+er​t​e−δ​θ​t​(Xt+er​t​Yt)−γ​d​Yt\displaystyle+{e^{-\delta\theta t}}(X\_{t}+e^{rt}Y\_{t})^{-\gamma}\mathrm{d}X\_{t}+e^{rt}{e^{-\delta\theta t}}(X\_{t}+e^{rt}Y\_{t})^{-\gamma}\mathrm{d}Y\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ2​e−δ​θ​t​(Xt+er​t​Yt)−γ−1​(d​Xt)2−γ2​e2​r​t​e−δ​θ​t​(Xt+er​t​Yt)−γ−1​(d​Yt)2\displaystyle-\frac{\gamma}{2}{e^{-\delta\theta t}}(X\_{t}+e^{rt}Y\_{t})^{-\gamma-1}(\mathrm{d}X\_{t})^{2}-\frac{\gamma}{2}e^{2rt}{e^{-\delta\theta t}}(X\_{t}+e^{rt}Y\_{t})^{-\gamma-1}(\mathrm{d}Y\_{t})^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ​er​t​e−δ​θ​t​(Xt+er​t​Yt)−γ−1​d​Xt​d​Yt+f​(ct,e−δ​θ​t​(Xt+er​t​Yt)1−γ1−γ)​d​t\displaystyle-\gamma e^{rt}{e^{-\delta\theta t}}(X\_{t}+e^{rt}Y\_{t})^{-\gamma-1}\mathrm{d}X\_{t}\mathrm{d}Y\_{t}+f\big(c\_{t},{e^{-\delta\theta t}}\frac{(X\_{t}+e^{rt}Y\_{t})^{1-\gamma}}{1-\gamma}\big)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−δ​θ​e−δ​θ​t​(Xt+er​t​Yt)1−γ1−γ​d​t+e−δ​θ​t​(Xt+er​t​Yt)−γ​r​Xt​d​t\displaystyle=-\delta\theta e^{-\delta\theta t}\frac{(X\_{t}+e^{rt}Y\_{t})^{1-\gamma}}{1-\gamma}\mathrm{d}t+e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma}rX\_{t}\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +e−δ​θ​t​(Xt+er​t​Yt)−γ​πt⊺​η​d​t+e−δ​θ​t​(Xt+er​t​Yt)−γ​πt⊺​d​Btℚξ\displaystyle+{e^{-\delta\theta t}}(X\_{t}+e^{rt}Y\_{t})^{-\gamma}\pi\_{t}^{\intercal}\eta\mathrm{d}t+e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma}\pi\_{t}^{\intercal}\mathrm{d}B\_{t}^{\mathbb{Q}^{\xi}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −e−δ​θ​t​(Xt+er​t​Yt)−γ​ct​d​t−e−δ​θ​t​(Xt+er​t​Yt)−γ​πt⊺​ξt​d​t\displaystyle-e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma}c\_{t}\mathrm{d}t-e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma}\pi\_{t}^{\intercal}\xi\_{t}\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −er​t​e−δ​θ​t​(Xt+er​t​Yt)−γ​ℋt​d​t−er​t​e−δ​θ​t​(Xt+er​t​Yt)−γ​Zt⊺​ξt​d​t\displaystyle-e^{rt}e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma}\mathcal{H}\_{t}\mathrm{d}t-e^{rt}e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma}Z\_{t}^{\intercal}\xi\_{t}\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +er​t​e−δ​θ​t​(Xt+er​t​Yt)−γ​Zt⊺​d​Btℚξ−γ2​e−δ​θ​t​(Xt+er​t​Yt)−γ−1​πt⊺​πt​d​t\displaystyle+e^{rt}e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma}Z\_{t}^{\intercal}\mathrm{d}B\_{t}^{\mathbb{Q}^{\xi}}-\frac{\gamma}{2}e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma-1}\pi\_{t}^{\intercal}\pi\_{t}\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ2​e2​r​t​e−δ​θ​t​(Xt+er​t​Yt)−γ−1​‖Zt‖2​d​t−γ​er​t​e−δ​θ​t​(Xt+er​t​Yt)−γ−1​πt⊺​Zt​d​t\displaystyle-\frac{\gamma}{2}e^{2rt}e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma-1}\|Z\_{t}\|^{2}\mathrm{d}t-\gamma e^{rt}e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma-1}\pi\_{t}^{\intercal}Z\_{t}\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +δ​ct1−1ψ1−1ψ​e−δ​θ​t​(Xt+er​t​Yt)−γ+1ψ​d​t+12​Φ​‖ξ‖2​e−δ​θ​t​(Xt+er​t​Yt)1−γ​d​t\displaystyle+\delta\frac{c\_{t}^{1-\frac{1}{\psi}}}{1-\frac{1}{\psi}}e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma+\frac{1}{\psi}}\mathrm{d}t+\frac{1}{2\Phi}\|\xi\|^{2}e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{1-\gamma}\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +r​er​t​Yt​e−δ​θ​t​(Xt+er​t​Yt)−γ​d​t\displaystyle+re^{rt}Y\_{t}e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma}\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =[(−ct+δct1−1ψ1−1ψ(Xt+er​tYt)1ψ)e−δ​θ​t(Xt+er​tYt)−γ\displaystyle=\Big[\Big(-c\_{t}+\delta\frac{c\_{t}^{1-\frac{1}{\psi}}}{1-\frac{1}{\psi}}(X\_{t}+e^{rt}Y\_{t})^{\frac{1}{\psi}}\Big){e^{-\delta\theta t}}(X\_{t}+e^{rt}Y\_{t})^{-\gamma} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ+Φ2​e−δ​θ​t​(Xt+er​t​Yt)−γ−1​(πt⊺​πt+2​πt⊺​(er​t​Zt−1γ+Φ​(Xt+er​t​Yt)​η))\displaystyle-\frac{\gamma+\Phi}{2}e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma-1}\Big(\pi\_{t}^{\intercal}\pi\_{t}+2\pi\_{t}^{\intercal}\Big(e^{rt}Z\_{t}{-\frac{1}{\gamma+\Phi}}(X\_{t}+e^{rt}Y\_{t})\eta\Big)\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ+Φ2​e2​r​t​e−δ​θ​t​(Xt+er​t​Yt)−γ−1​‖Zt‖2−er​t​e−δ​θ​t​(Xt+er​t​Yt)−γ​ℋt\displaystyle-\frac{\gamma+\Phi}{2}e^{2rt}e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma-1}\|Z\_{t}\|^{2}-e^{rt}e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma}\mathcal{H}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +r​er​t​Yt​e−δ​θ​t​(Xt+er​t​Yt)−γ+e−δ​θ​t​(Xt+er​t​Yt)−γ​r​Xt\displaystyle+re^{rt}Y\_{t}e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma}+e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma}rX\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −δθe−δ​θ​t(Xt+er​t​Yt)1−γ1−γ]dt+e−δ​θ​t(Xt+er​tYt)−γ(πt⊺+er​tZt⊺)dBtℚξ\displaystyle-\delta\theta e^{-\delta\theta t}\frac{(X\_{t}+e^{rt}Y\_{t})^{1-\gamma}}{1-\gamma}\Big]\mathrm{d}t+e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma}\big(\pi\_{t}^{\intercal}+e^{rt}Z\_{t}^{\intercal}\big)\mathrm{d}B\_{t}^{\mathbb{Q}^{\xi}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​Φ​e−δ​θ​t​(Xt+er​t​Yt)1−γ​(‖ξt‖2−2​Φ​(Xt+er​t​Yt)−1​(πt⊺+er​t​Zt⊺)​ξt)​d​t\displaystyle+\frac{1}{2\Phi}e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{1-\gamma}\Big(\|\xi\_{t}\|^{2}-2\Phi(X\_{t}+e^{rt}Y\_{t})^{-1}\big(\pi\_{t}^{\intercal}+e^{rt}Z\_{t}^{\intercal}\big)\xi\_{t}\Big)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =e−δ​θ​t(Xt+er​tYt)−γ[−ct+δct1−1ψ1−1ψ(Xt+er​tYt)1ψ−er​tZt⊺η\displaystyle=e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma}\Bigg[-c\_{t}+\delta\frac{c\_{t}^{1-\frac{1}{\psi}}}{1-\frac{1}{\psi}}(X\_{t}+e^{rt}Y\_{t})^{\frac{1}{\psi}}-e^{rt}Z\_{t}^{\intercal}\eta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​Φ​(Xt+er​t​Yt)​‖ξt−Φ​(Xt+er​t​Yt)−1​(πt+er​t​Zt)‖2\displaystyle+\frac{1}{2\Phi}(X\_{t}+e^{rt}Y\_{t})\big\|\xi\_{t}-\Phi(X\_{t}+e^{rt}Y\_{t})^{-1}\big(\pi\_{t}+e^{rt}Z\_{t}\big)\big\|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ+Φ2​(Xt+er​t​Yt)−1​‖πt+(er​t​Zt−1γ+Φ​(Xt+er​t​Yt)​η)‖2\displaystyle-\frac{\gamma+\Phi}{2}(X\_{t}+e^{rt}Y\_{t})^{-1}\Big\|\pi\_{t}+\Big(e^{rt}Z\_{t}{-\frac{1}{\gamma+\Phi}}(X\_{t}+e^{rt}Y\_{t})\eta\Big)\Big\|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +121γ+Φ(Xt+er​tYt)∥η∥2+r(Xt+er​tYt)−δ​θ1−γ(Xt+er​tYt)−er​tℋt]dt\displaystyle+\frac{1}{2}\frac{1}{\gamma+\Phi}(X\_{t}+e^{rt}Y\_{t})\|\eta\|^{2}+r(X\_{t}+e^{rt}Y\_{t})-\frac{\delta\theta}{1-\gamma}(X\_{t}+e^{rt}Y\_{t})-e^{rt}\mathcal{H}\_{t}\Bigg]\mathrm{d}t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +e−δ​θ​t​(Xt+er​t​Yt)−γ​(πt⊺+er​t​Zt⊺)​d​Btℚξ.\displaystyle+e^{-\delta\theta t}(X\_{t}+e^{rt}Y\_{t})^{-\gamma}\big(\pi\_{t}^{\intercal}+e^{rt}Z\_{t}^{\intercal}\big)\mathrm{d}B\_{t}^{\mathbb{Q}^{\xi}}. |  | (3.3) |

Applying the rules 1,21,2 and 33 above, we expect that (1)(1) for any (c,π)(c,\pi), the drift in ([3](https://arxiv.org/html/2511.03031v1#S3.Ex2 "3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) is non-negative for all ξ\xi, (2)(2) for any ξ\xi, the drift in ([3](https://arxiv.org/html/2511.03031v1#S3.Ex2 "3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) is non-positive for all (c,π)(c,\pi), and (3)(3) the drift in ([3](https://arxiv.org/html/2511.03031v1#S3.Ex2 "3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) is zero for the optimal triple (c^,π^,ξ^)(\widehat{c},\widehat{\pi},\widehat{\xi}). Hence, the generator ℋ\mathcal{H} for ([2.18](https://arxiv.org/html/2511.03031v1#S2.E18 "In 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) can be obtained by formally taking the infimum over ξ\xi and a supremum over cc and π\pi in the drift in ([3](https://arxiv.org/html/2511.03031v1#S3.Ex2 "3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) and setting it to be zero. That is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋ​(t,Xt,Yt,Zt)\displaystyle\mathcal{H}(t,X\_{t},Y\_{t},Z\_{t}) | =e−r​t​maxc⁡{−ct+δ​ct1−1ψ1−1ψ​(Xt+er​t​Yt)1ψ}\displaystyle=e^{-rt}\max\_{c}\Big\{-c\_{t}+\delta\frac{c\_{t}^{1-\frac{1}{\psi}}}{1-\frac{1}{\psi}}(X\_{t}+e^{rt}Y\_{t})^{\frac{1}{\psi}}\Big\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +minξ⁡{12​Φ​e−r​t​(Xt+er​t​Yt)​‖ξt−Φ​(Xt+er​t​Yt)−1​(πt+er​t​Zt)‖2}\displaystyle+\min\_{\xi}\Big\{\frac{1}{2\Phi}e^{-rt}(X\_{t}+e^{rt}Y\_{t})\big\|\xi\_{t}-\Phi(X\_{t}+e^{rt}Y\_{t})^{-1}\big(\pi\_{t}+e^{rt}Z\_{t}\big)\big\|^{2}\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +maxπ⁡{−γ+Φ2​e−r​t​(Xt+er​t​Yt)−1​‖πt+(er​t​Zt−1γ+Φ​(Xt+er​t​Yt)​η)‖2}\displaystyle+\max\_{\pi}\Big\{-\frac{\gamma+\Phi}{2}e^{-rt}(X\_{t}+e^{rt}Y\_{t})^{-1}\Big\|\pi\_{t}+\Big(e^{rt}Z\_{t}{-\frac{1}{\gamma+\Phi}}(X\_{t}+e^{rt}Y\_{t})\eta\Big)\Big\|^{2}\Big\} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +12​1γ+Φ​e−r​t​(Xt+er​t​Yt)​‖η‖2+r​e−r​t​(Xt+er​t​Yt)−δ​θ1−γ​e−r​t​(Xt+er​t​Yt).\displaystyle+\frac{1}{2}\frac{1}{\gamma+\Phi}e^{-rt}(X\_{t}+e^{rt}Y\_{t})\|\eta\|^{2}+re^{-rt}(X\_{t}+e^{rt}Y\_{t})-\frac{\delta\theta}{1-\gamma}e^{-rt}(X\_{t}+e^{rt}Y\_{t}). |  | (3.4) |

Therefore, we deduce from the three optimisation problems in ([3](https://arxiv.org/html/2511.03031v1#S3.Ex24 "3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) that the candidate optimal consumption c^\widehat{c}, the candidate optimal investment-reinsurance π^\widehat{\pi} and the candidate optimal distortion process ξ^\widehat{\xi} are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | c^t\displaystyle\widehat{c}\_{t} | =δψ​(Xt+er​t​Yt)\displaystyle=\delta^{\psi}(X\_{t}+e^{rt}Y\_{t}) |  | (3.5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | π^t\displaystyle\widehat{\pi}\_{t} | =−er​t​Zt+1γ+Φ​(Xt+er​t​Yt)​η\displaystyle=-e^{rt}Z\_{t}+\frac{1}{\gamma+\Phi}(X\_{t}+e^{rt}Y\_{t})\eta |  | (3.6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ξ^t\displaystyle\widehat{\xi}\_{t} | =Φ​(Xt+er​t​Yt)−1​(π^t+er​t​Zt)=Φγ+Φ​η,\displaystyle=\Phi(X\_{t}+e^{rt}Y\_{t})^{-1}\big(\widehat{\pi}\_{t}+e^{rt}Z\_{t}\big)=\frac{\Phi}{\gamma+\Phi}\eta, |  | (3.7) |

Hence, substituting ([3.5](https://arxiv.org/html/2511.03031v1#S3.E5 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")), ([3.6](https://arxiv.org/html/2511.03031v1#S3.E6 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) and ([3.7](https://arxiv.org/html/2511.03031v1#S3.E7 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) into ([2.9](https://arxiv.org/html/2511.03031v1#S2.E9 "In 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) and ([3](https://arxiv.org/html/2511.03031v1#S3.Ex24 "3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")), the function ℋ\mathcal{H} and the wealth process X=:X^X=:\widehat{X} are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋ​(t,X^t,Yt,Zt)=e−r​t​(δψψ−1+r+12​1γ+Φ​‖η‖2−δ​θ1−γ)​(X^t+er​t​Yt)−Zt⊺​η\displaystyle\mathcal{H}(t,\widehat{X}\_{t},Y\_{t},Z\_{t})=e^{-rt}\Big(\frac{\delta^{\psi}}{\psi-1}+r+\frac{1}{2}\frac{1}{\gamma+\Phi}\|\eta\|^{2}{-\frac{\delta\theta}{1-\gamma}}\Big)(\widehat{X}\_{t}+e^{rt}Y\_{t})-Z\_{t}^{\intercal}\eta |  | (3.8) |
|  |  |  |
| --- | --- | --- |
|  | and ​d​X^t=(r​X^t+(−δψ+1γ+Φ​‖η‖2)​(X^t+er​t​Yt)−γγ+Φ​er​t​Zt⊺​η)​d​t\displaystyle\text{and }\mathrm{d}\widehat{X}\_{t}=\Big(r\widehat{X}\_{t}+\big(-\delta^{\psi}{+\frac{1}{\gamma+\Phi}}\|\eta\|^{2}\big)(\widehat{X}\_{t}+e^{rt}Y\_{t})-{\frac{\gamma}{\gamma+\Phi}}e^{rt}Z\_{t}^{\intercal}\eta\Big)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +(1γ+Φ​(X^t+er​t​Yt)​η⊺−er​t​Zt⊺)​d​Btℚξ^.\displaystyle\phantom{XXXX}+\Big({\frac{1}{\gamma+\Phi}}(\widehat{X}\_{t}+e^{rt}Y\_{t})\eta^{\intercal}-e^{rt}Z\_{t}^{\intercal}\Big)\mathrm{d}B\_{t}^{\mathbb{Q}^{\widehat{\xi}}}. |  | (3.9) |

Thus, a candidate solution to Problem [2.3](https://arxiv.org/html/2511.03031v1#S2.Thmdefi3 "Problem 2.3. ‣ 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") is given by ([3.5](https://arxiv.org/html/2511.03031v1#S3.E5 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")), ([3.6](https://arxiv.org/html/2511.03031v1#S3.E6 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) and ([3.7](https://arxiv.org/html/2511.03031v1#S3.E7 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")), provided that the FBSDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​X^t=(r​X^t+(−δψ+1γ+Φ​‖η‖2)​(X^t+er​t​Yt)−γγ+Φ​er​t​Zt⊺​η)​d​t+(1γ+Φ​(X^t+er​t​Yt)​η⊺−er​t​Zt⊺)​d​Btℚξ^.d​Yt=−(e−r​t​(δψψ−1+r+12​1γ+Φ​‖η‖2−δ​θ1−γ)​(X^t+er​t​Yt)−γγ+Φ​Zt⊺​η)​d​t+Zt⊺​d​Btℚξ^X^0=x+(νi​n−νr​e)​κ​ζ​∫0Te−r​s​ds,YT=−e−r​T​G\displaystyle\begin{cases}\mathrm{d}\widehat{X}\_{t}&=\Big(r\widehat{X}\_{t}+\big(-\delta^{\psi}{+\frac{1}{\gamma+\Phi}}\|\eta\|^{2}\big)(\widehat{X}\_{t}+e^{rt}Y\_{t})-{\frac{\gamma}{\gamma+\Phi}}e^{rt}Z\_{t}^{\intercal}\eta\Big)\mathrm{d}t\\ &\phantom{X}+\Big({\frac{1}{\gamma+\Phi}}(\widehat{X}\_{t}+e^{rt}Y\_{t})\eta^{\intercal}-e^{rt}Z\_{t}^{\intercal}\Big)\mathrm{d}B\_{t}^{\mathbb{Q}^{\widehat{\xi}}}.\\ \mathrm{d}Y\_{t}&=-\Big(e^{-rt}\Big(\frac{\delta^{\psi}}{\psi-1}+r+\frac{1}{2}\frac{1}{\gamma+\Phi}\|\eta\|^{2}{-\frac{\delta\theta}{1-\gamma}}\Big)(\widehat{X}\_{t}+e^{rt}Y\_{t})-{\frac{\gamma}{\gamma+\Phi}}Z\_{t}^{\intercal}\eta\Big)\mathrm{d}t\\ &\phantom{X}+Z\_{t}^{\intercal}\mathrm{d}B\_{t}^{\mathbb{Q}^{\widehat{\xi}}}\\ \widehat{X}\_{0}&=x+\big(\nu^{in}-\nu^{re}\big)\kappa\zeta\int\_{0}^{T}e^{-rs}\mathrm{d}s,~Y\_{T}=-e^{-rT}G\end{cases} |  | (3.10) |

is well-defined in an appropriate function space. In the sequel, to simplify the notations, we introduce the process Ht={Hst,t≤s≤T}H^{t}=\{H\_{s}^{t},t\leq s\leq T\} defined by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Hst\displaystyle H\_{s}^{t} | :=ℰ​(∫−η⊺​d​B)s/ℰ​(∫−η⊺​d​B)t,t≤s≤T,\displaystyle:=\mathcal{E}(\int-\eta^{\intercal}\mathrm{d}B)\_{s}\big/\mathcal{E}(\int-\eta^{\intercal}\mathrm{d}B)\_{t},~t\leq s\leq T, |  | (3.11) |

with H:=HtH:=H^{t} for t=0t=0, and the process φ={φt,0≤t≤T}\varphi=\{\varphi\_{t},0\leq t\leq T\} given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | φt\displaystyle\varphi\_{t} | :=exp⁡((−δψ​ψψ−1+γ+3​Φ−12​(γ+Φ)2​‖η‖2+δ​θ1−γ)​t+1γ+Φ​η⊺​Bt),t≤s≤T.\displaystyle:=\exp\Big(\Big(-\frac{\delta^{\psi}\psi}{\psi-1}+{\frac{\gamma+3\Phi-1}{2(\gamma+\Phi)^{2}}}\|\eta\|^{2}{+\frac{\delta\theta}{1-\gamma}}\Big)t+\frac{1}{\gamma+\Phi}\eta^{\intercal}B\_{t}\Big),~t\leq s\leq T. |  | (3.12) |

We can now confirm the well-definedness of the FBSDE ([3.10](https://arxiv.org/html/2511.03031v1#S3.E10 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")).

###### Proposition 3.1.

Let rmr\_{m} and x~\widetilde{x} denote the constants defined by
  
rm:=−δψ​ψψ−1−r−γ−Φ2​(γ+Φ)2​‖η‖2+δ​θ1−γr\_{m}:=-\frac{\delta^{\psi}\psi}{\psi-1}-r-\frac{\gamma-\Phi}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}+\frac{\delta\theta}{1-\gamma} and x~:=rm​(x+κ​ζr​(νi​n−νr​e)​(1−e−r​T)−e−r​T​G)rm+(rm+δψ−Φ(γ+Φ)2​‖η‖2)​(erm​T−1)\widetilde{x}:=\frac{r\_{m}\big(x+\frac{\kappa\zeta}{r}\big(\nu^{in}-\nu^{re}\big)\big(1-e^{-rT}\big)-e^{-rT}G\big)}{r\_{m}+\big(r\_{m}+\delta^{\psi}-\frac{\Phi}{(\gamma+\Phi)^{2}}\|\eta\|^{2}\big)\big(e^{r\_{m}T}-1\big)}. Assume that x~\widetilde{x} is finite. Then a solution (X^,Y,Z)∈ℋℙq×ℋℙq×ℍℙq,q≥1(\widehat{X},Y,Z)\in\mathcal{H}\_{\mathbb{P}}^{q}\times\mathcal{H}\_{\mathbb{P}}^{q}\times\mathbb{H}\_{\mathbb{P}}^{q},~q\geq 1, to the FBSDE ([3.10](https://arxiv.org/html/2511.03031v1#S3.E10 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | {X^t=x~​φt−er​t​YtYt=−e−r​T​G+x~​(−rm−δψ+Φ(γ+Φ)2​‖η‖2)​erm​T−erm​trm​exp⁡(−1+2​(γ+Φ)2​(γ+Φ)2​‖η‖2​t+1γ+Φ​η⊺​Bt)Zt=1γ+Φ​(Yt+e−r​T​G)​η.\displaystyle\begin{cases}\widehat{X}\_{t}&=\widetilde{x}\varphi\_{t}-e^{rt}Y\_{t}\\ Y\_{t}&=-e^{-rT}G\\ &\phantom{X}+\widetilde{x}\Big(-r\_{m}-\delta^{\psi}+\frac{\Phi}{(\gamma+\Phi)^{2}}\|\eta\|^{2}\Big)\frac{e^{r\_{m}T}-e^{r\_{m}t}}{r\_{m}}\exp\Big(\frac{-1+2(\gamma+\Phi)}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}t+\frac{1}{\gamma+\Phi}\eta^{\intercal}B\_{t}\Big)\\ Z\_{t}&=\frac{1}{\gamma+\Phi}\big(Y\_{t}+e^{-rT}G\big)\eta.\end{cases} |  | (3.13) |

Moreover, the solution (X^,Y,Z)(\widehat{X},Y,Z) given by ([3.13](https://arxiv.org/html/2511.03031v1#S3.E13 "In Proposition 3.1. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) is the unique local solution to the FBSDE ([3.10](https://arxiv.org/html/2511.03031v1#S3.E10 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")).

###### Proof.

See Appendix [B](https://arxiv.org/html/2511.03031v1#A2 "Appendix B Proof of Proposition 3.1 ‣ Robust optimal consumption, investment and reinsurance for recursive preferences").
∎

###### Remark 3.2.

Note that for Φ=0\Phi=0, the constant x~\widetilde{x} (=:x~0=:\widetilde{x}^{0}) in Proposition [3.1](https://arxiv.org/html/2511.03031v1#S3.Thmdefi1 "Proposition 3.1. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") is finite. Indeed,

|  |  |  |  |
| --- | --- | --- | --- |
|  | x~0\displaystyle\widetilde{x}^{0} | =rm​(x+κ​ζr​(νi​n−νr​e)​(1−e−r​T)−e−r​T​G)rm+(rm+δψ)​(erm​T−1)\displaystyle=\frac{r\_{m}\big(x+\frac{\kappa\zeta}{r}\big(\nu^{in}-\nu^{re}\big)\big(1-e^{-rT}\big)-e^{-rT}G\big)}{r\_{m}+\big(r\_{m}+\delta^{\psi}\big)\big(e^{r\_{m}T}-1\big)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =x+κ​ζr​(νi​n−νr​e)​(1−e−r​T)−e−r​T​Germ​T+δψrm​(erm​T−1)\displaystyle=\frac{x+\frac{\kappa\zeta}{r}\big(\nu^{in}-\nu^{re}\big)\big(1-e^{-rT}\big)-e^{-rT}G}{e^{r\_{m}T}+\frac{\delta^{\psi}}{r\_{m}}\big(e^{r\_{m}T}-1\big)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =x+κ​ζr​(νi​n−νr​e)​(1−e−r​T)−e−r​T​Germ​T+∫0Tδψ​erm​s​ds.\displaystyle=\frac{x+\frac{\kappa\zeta}{r}\big(\nu^{in}-\nu^{re}\big)\big(1-e^{-rT}\big)-e^{-rT}G}{e^{r\_{m}T}+\int\_{0}^{T}\delta^{\psi}e^{r\_{m}s}\mathrm{d}s}. |  |

Because erm​T+∫0Tδψ​erm​s​ds>0e^{r\_{m}T}+\int\_{0}^{T}\delta^{\psi}e^{r\_{m}s}\mathrm{d}s>0, we have x~0:=x~\widetilde{x}^{0}:=\widetilde{x} finite.

To ensure the optimality of the candidate strategies given by ([3.5](https://arxiv.org/html/2511.03031v1#S3.E5 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")), ([3.6](https://arxiv.org/html/2511.03031v1#S3.E6 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) and ([3.7](https://arxiv.org/html/2511.03031v1#S3.E7 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) we consider the following conditions.

###### Assumption 3.3.

x~>0\widetilde{x}>0, −ρS​μ+σ​νr​e​κ​ζσ>0\frac{-\rho^{S}\mu+\sigma\nu^{re}\kappa\zeta}{\sigma}>0 and −rm−δψ+Φ(γ+Φ)2​‖η‖2<0-r\_{m}-\delta^{\psi}+\frac{\Phi}{(\gamma+\Phi)^{2}}\|\eta\|^{2}<0.

###### Remark 3.4.

Note that when the liability is non-negative (that is, G≥0G\geq 0), then Assumption [3.3](https://arxiv.org/html/2511.03031v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") yields that the process YY, given in ([3.13](https://arxiv.org/html/2511.03031v1#S3.E13 "In Proposition 3.1. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")), is negative. As a by-product, we obtain that the optimal wealth process X^\widehat{X}, given in ([3.13](https://arxiv.org/html/2511.03031v1#S3.E13 "In Proposition 3.1. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")), is positive. Indeed, for G≥0G\geq 0, suppose Assumption [3.3](https://arxiv.org/html/2511.03031v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") holds. Then the right side of the second equality in ([3.13](https://arxiv.org/html/2511.03031v1#S3.E13 "In Proposition 3.1. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) is negative; because erm​T−erm​trm>0\frac{e^{r\_{m}T}-e^{r\_{m}t}}{r\_{m}}>0 for all rm∈ℝr\_{m}\in\mathbb{R}. Hence, Yt<0,t∈[0,T]Y\_{t}<0,~t\in[0,T]. Using the first equality in ([3.13](https://arxiv.org/html/2511.03031v1#S3.E13 "In Proposition 3.1. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) and the fact that x~>0\widetilde{x}>0 and φt>0,t∈[0,T]\varphi\_{t}>0,~t\in[0,T], we deduce that X^t>0\widehat{X}\_{t}>0 for all t∈[0,T]t\in[0,T].

We are now ready to give the main result of the present paper.

###### Theorem 3.5.

Suppose Assumption [3.3](https://arxiv.org/html/2511.03031v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") holds. Let x~\widetilde{x} be defined as in Proposition [3.1](https://arxiv.org/html/2511.03031v1#S3.Thmdefi1 "Proposition 3.1. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences"). Let Γ\varGamma be the process defined by Γt:=−1γ+Φ​e−r​t​(Yt+e−r​T​G)+1γ+Φ​x~​φt\varGamma\_{t}:=-\frac{1}{\gamma+\Phi}e^{-rt}\big(Y\_{t}+e^{-rT}G\big)+\frac{1}{\gamma+\Phi}\widetilde{x}\varphi\_{t} for t∈[0,T]t\in[0,T]. Then the robust optimal consumption c^\widehat{c}, distortion process ξ^\widehat{\xi}, investment π^S\widehat{\pi}^{S} and reinsurance π^r​e\widehat{\pi}^{re} strategies given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | {c^t=δψ​x~​φt,ξ^t=Φγ+Φ​1σ​ρr​e​κ​β​(μ​ρr​e​κ​β−ρS​μ+σ​νr​e​κ​ζ)π^tS=1κ​β​σ2​(ρr​e)2​(μ​κ​β​(ρr​e)2−ρS​(−ρS​μ+σ​νr​e​κ​ζ))​Γtπ^tr​e=1κ​β​σ​(ρr​e)2​(−ρS​μ+σ​νr​e​κ​ζ)​Γt\displaystyle\begin{cases}\widehat{c}\_{t}&=\delta^{\psi}\widetilde{x}\varphi\_{t},~~\widehat{\xi}\_{t}=\frac{\Phi}{\gamma+\Phi}\frac{1}{\sigma\rho^{re}\sqrt{\kappa\beta}}\left(\begin{matrix}\mu\rho^{re}\sqrt{\kappa\beta}\\ -\rho^{S}\mu+\sigma\nu^{re}\kappa\zeta\end{matrix}\right)\\ \widehat{\pi}\_{t}^{S}&=\frac{1}{\kappa\beta\sigma^{2}(\rho^{re})^{2}}\Big(\mu\kappa\beta(\rho^{re})^{2}-\rho^{S}\Big(-\rho^{S}\mu+\sigma\nu^{re}\kappa\zeta\Big)\Big)\varGamma\_{t}\\ \widehat{\pi}\_{t}^{re}&=\frac{1}{\kappa\beta\sigma(\rho^{re})^{2}}\Big(-\rho^{S}\mu+\sigma\nu^{re}\kappa\zeta\Big)\varGamma\_{t}\end{cases} |  | (3.14) |

solve the control problem ([2.19](https://arxiv.org/html/2511.03031v1#S2.E19 "In Problem 2.3. ‣ 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")), and their associated value function is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒱A​A​I\displaystyle\mathcal{V}^{AAI} | =11−γ​(rm​(x+κ​ζr​(νi​n−νr​e)​(1−e−r​T)−e−r​T​G)rm+(rm+δψ−Φ(γ+Φ)2​‖η‖2)​(erm​T−1))1−γ.\displaystyle=\frac{1}{1-\gamma}\left(\frac{r\_{m}\big(x+\frac{\kappa\zeta}{r}\big(\nu^{in}-\nu^{re}\big)\big(1-e^{-rT}\big)-e^{-rT}G\big)}{r\_{m}+\big(r\_{m}+\delta^{\psi}-\frac{\Phi}{(\gamma+\Phi)^{2}}\|\eta\|^{2}\big)\big(e^{r\_{m}T}-1\big)}\right)^{1-\gamma}. |  | (3.15) |

###### Remark 3.6.

Note, from ([3.14](https://arxiv.org/html/2511.03031v1#S3.E14 "In Theorem 3.5. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) and the definition of the vector η\eta just below ([2.1](https://arxiv.org/html/2511.03031v1#S2.Ex2 "2.1. Probability setting and wealth process of the insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")), that the robust optimal reinsurance strategy (RORS) depends on the parameters of the financial market. Similarly, the parameters of the insurance market impact both the robust optimal consumption strategy (ROCS) and the robust optimal investment strategy (ROIS). This co-dependence happens even if we assume no correlation (meaning, ρS=0\rho^{S}=0) between the insurance market and the financial market.

We state four preliminaries results, Lemma [3.7](https://arxiv.org/html/2511.03031v1#S3.Thmdefi7 "Lemma 3.7. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences"), [3.8](https://arxiv.org/html/2511.03031v1#S3.Thmdefi8 "Lemma 3.8. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences"), [3.9](https://arxiv.org/html/2511.03031v1#S3.Thmdefi9 "Lemma 3.9. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") and [3.10](https://arxiv.org/html/2511.03031v1#S3.Thmdefi10 "Lemma 3.10. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences"), from which the proof of Theorem [3.5](https://arxiv.org/html/2511.03031v1#S3.Thmdefi5 "Theorem 3.5. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") will follow (see Appendix [C](https://arxiv.org/html/2511.03031v1#A3 "Appendix C Proof of Lemmas 3.7, 3.8 and 3.9, and Theorem 3.5 ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")). Lemma [3.7](https://arxiv.org/html/2511.03031v1#S3.Thmdefi7 "Lemma 3.7. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") confirms that the candidate controls are admissible and their optimality is shown via Lemma [3.9](https://arxiv.org/html/2511.03031v1#S3.Thmdefi9 "Lemma 3.9. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences").

###### Lemma 3.7.

Recall (X^,Y)(\widehat{X},Y) given by ([3.13](https://arxiv.org/html/2511.03031v1#S3.E13 "In Proposition 3.1. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")). Let Assumption [3.3](https://arxiv.org/html/2511.03031v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") holds. Then

* (i)(i)

  X^t+er​t​Yt>0\widehat{X}\_{t}+e^{rt}Y\_{t}>0 for all t∈[0,T]t\in[0,T].
* (i​i)(ii)

  (c^,ξ^)∈𝒜a(\widehat{c},\widehat{\xi})\in\mathcal{A}\_{a} and (X^+er​t​Y)1−γ(\widehat{X}+e^{rt}Y)^{1-\gamma} is of class (D) under ℙ\mathbb{P}.

###### Proof.

See Appendix [C](https://arxiv.org/html/2511.03031v1#A3 "Appendix C Proof of Lemmas 3.7, 3.8 and 3.9, and Theorem 3.5 ‣ Robust optimal consumption, investment and reinsurance for recursive preferences").
∎

###### Lemma 3.8.

Let (Y,Z)(Y,Z) (respectively, (Y~,Z~)(\widetilde{Y},\widetilde{Z})) be a super-solution (respectively, sub-solution) to ([2.16](https://arxiv.org/html/2511.03031v1#S2.E16 "In Proposition 2.1. ‣ 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")). That is,

|  |  |  |
| --- | --- | --- |
|  | Y+∫0⋅(f​(cs,Ys)+12​Φ​‖ξs‖2​(1−γ)​Ys)​ds​ is a local super-martingale and\displaystyle Y+\int\_{0}^{\cdot}\Big(f(c\_{s},Y\_{s})+\frac{1}{2\Phi}\|\xi\_{s}\|^{2}(1-\gamma)Y\_{s}\Big)\mathrm{d}s\text{ is a local super-martingale and} |  |
|  |  |  |
| --- | --- | --- |
|  | Y~+∫0⋅(f​(cs,Y~s)+12​Φ​‖ξs‖2​(1−γ)​Y~s)​ds​ is a local sub-martingale\displaystyle\widetilde{Y}+\int\_{0}^{\cdot}\Big(f(c\_{s},\widetilde{Y}\_{s})+\frac{1}{2\Phi}\|\xi\_{s}\|^{2}(1-\gamma)\widetilde{Y}\_{s}\Big)\mathrm{d}s\text{ is a local sub-martingale} |  |

with YT≥e−δ​θ​T​cT1−γ1−γ≥Y~TY\_{T}\geq e^{-\delta\theta T}\frac{c\_{T}^{1-\gamma}}{1-\gamma}\geq\tilde{Y}\_{T}, where ZZ and Z~\tilde{Z} are determined by the Doob–Meyer decomposition and martingale representation. Assume that both YY and Y~\tilde{Y} are of class (D). Then Yt≥Y~tY\_{t}\geq\tilde{Y}\_{t} for t∈[0,T]t\in[0,T]. Moreover, if YT>Y~TY\_{T}>\tilde{Y}\_{T}, then Yt>Y~tY\_{t}>\tilde{Y}\_{t} for t∈[0,T]t\in[0,T].

###### Proof.

See Appendix [C](https://arxiv.org/html/2511.03031v1#A3 "Appendix C Proof of Lemmas 3.7, 3.8 and 3.9, and Theorem 3.5 ‣ Robust optimal consumption, investment and reinsurance for recursive preferences").
∎

###### Lemma 3.9.

Let Assumption [3.3](https://arxiv.org/html/2511.03031v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") holds. Then for any triple (c,π,ξ)(c,\pi,\xi) of admissible strategy we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | (x+Y0)1−γ1−γ≥V0c,ξ,\displaystyle\frac{(x+Y\_{0})^{1-\gamma}}{1-\gamma}\geq V\_{0}^{c,\xi}, |  | (3.16) |

with cc financed by π\pi via ([2.9](https://arxiv.org/html/2511.03031v1#S2.E9 "In 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")), Vc,ξV^{c,\xi} defined in Proposition [2.1](https://arxiv.org/html/2511.03031v1#S2.Thmdefi1 "Proposition 2.1. ‣ 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") and YY given in ([3.13](https://arxiv.org/html/2511.03031v1#S3.E13 "In Proposition 3.1. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")).

###### Proof.

See Appendix [C](https://arxiv.org/html/2511.03031v1#A3 "Appendix C Proof of Lemmas 3.7, 3.8 and 3.9, and Theorem 3.5 ‣ Robust optimal consumption, investment and reinsurance for recursive preferences").
∎

###### Lemma 3.10.

Let M~\widetilde{M} be the process defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | M~t:=exp⁡(∫0t(δψ​θ+Φ​(1−γ)2​(γ+Φ)2​‖η‖2​eδ​θ​s)​ds)​e−δ​θ​t​(X^t+er​t​Yt)1−γ1−γ,0≤t≤T,\displaystyle\widetilde{M}\_{t}:=\exp\Big(\int\_{0}^{t}\big(\delta^{\psi}\theta+\frac{\Phi(1-\gamma)}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}e^{\delta\theta s}\big)\mathrm{d}s\Big)e^{-\delta\theta t}\frac{(\widehat{X}\_{t}+e^{rt}Y\_{t})^{1-\gamma}}{1-\gamma},~0\leq t\leq T, |  | (3.17) |

with (X^,Y)(\widehat{X},Y) as in Proposition [3.1](https://arxiv.org/html/2511.03031v1#S3.Thmdefi1 "Proposition 3.1. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences"). Then the process M~\widetilde{M} is a martingale under ℚξ^\mathbb{Q}^{\widehat{\xi}}.

###### Proof.

See Appendix [C](https://arxiv.org/html/2511.03031v1#A3 "Appendix C Proof of Lemmas 3.7, 3.8 and 3.9, and Theorem 3.5 ‣ Robust optimal consumption, investment and reinsurance for recursive preferences").
∎

## 4. Numerical simulations

The goal of this section is to numerically illustrate the effects of model parameters on the optimal consumption, investment and reinsurance strategies, and the corresponding value function. We consider three cases: the no-correlation between insurance market and financial market case, the case of an ambiguity-neutral insurer (ANI) and the general case obtained in Theorem [3.5](https://arxiv.org/html/2511.03031v1#S3.Thmdefi5 "Theorem 3.5. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences"). For the numerical experiments, except otherwise stated, the basic parameters are chosen as those in Table [1](https://arxiv.org/html/2511.03031v1#S4.T1 "Table 1 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences").

|  |
| --- |
| r0.05\begin{array}[]{c}r\\ 0.05\end{array} μ0.04\begin{array}[]{c}\mu\\ 0.04\end{array} σ0.25\begin{array}[]{c}\sigma\\ 0.25\end{array} δ0.08\begin{array}[]{c}\delta\\ 0.08\end{array} γ5\begin{array}[]{c}\gamma\\ 5\end{array} ψ1.5\begin{array}[]{c}\psi\\ 1.5\end{array} T10\begin{array}[]{c}T\\ 10\end{array} x500\begin{array}[]{c}x\\ 500\end{array} |
| κ1.5\begin{array}[]{c}\kappa\\ 1.5\end{array} ζ1\begin{array}[]{c}\zeta\\ 1\end{array} β1\begin{array}[]{c}\beta\\ 1\end{array} ρS−12\begin{array}[]{c}\rho^{S}\\ -\frac{1}{2}\end{array} ρr​e32\begin{array}[]{c}\rho^{re}\\ \frac{\sqrt{3}}{2}\end{array} νi​n0.2\begin{array}[]{c}\nu^{in}\\ 0.2\end{array} νr​e0.5\begin{array}[]{c}\nu^{re}\\ 0.5\end{array} Φ2\begin{array}[]{c}\Phi\\ 2\end{array} G500\begin{array}[]{c}G\\ 500\end{array} |

Table 1. Values of model parameters.



![Refer to caption](AAI_consumption_vs_sigma_by_gamma.png)

![Refer to caption](AAI_consumption_vs_sigma_by_psi.png)

Figure 1. The time-0 optimal consumption for an ambiguity-averse insurer with correlation between insurance market and financial market (general case). The left panel uses ψ=1.5\psi=1.5, and the right panel takes γ=5\gamma=5.

In Figure [1](https://arxiv.org/html/2511.03031v1#S4.F1 "Figure 1 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") we display the time-0 robust optimal consumption strategy (ROCS) with respect to the volatility of the stock for different values of the risk aversion (see Figure [1](https://arxiv.org/html/2511.03031v1#S4.F1 "Figure 1 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) and the EIS (see Figure [1](https://arxiv.org/html/2511.03031v1#S4.F1 "Figure 1 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")). We observe that the risk aversion coefficient and the EIS coefficient both negatively impact the consumption. In addition, Figure [1](https://arxiv.org/html/2511.03031v1#S4.F1 "Figure 1 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") shows that the ROCS is highly sensitive to small values of the volatility of the stock (σ<0.2\sigma<0.2) and barely influenced by its high values (σ≥0.4\sigma\geq 0.4).

![Refer to caption](All_consumption_vs_delta.png)

![Refer to caption](All_consumption_vs_gamma__GENERAL_vs_ANI_vs_Nocorr.png)

Figure 2. The time-0 optimal consumption for an ambiguity-neutral insurer (ANI case) and an ambiguity-averse insurer when considering correlation (General case) or no-correlation (No-correlation case) between financial and insurance risks.

Next, to better understand the effect of ambiguity aversion and correlation between financial and insurance risks on the optimal consumption strategy, we display in Figure [2](https://arxiv.org/html/2511.03031v1#S4.F2 "Figure 2 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") three cases, i.e., the ambiguity-neutral case (Φ=0\Phi=0), the no-correlation between financial and insurance risks case (ρS=0\rho^{S}=0), and the general case which is determined through the first equation in ([3.14](https://arxiv.org/html/2511.03031v1#S3.E14 "In Theorem 3.5. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")).

In Figure [2](https://arxiv.org/html/2511.03031v1#S4.F2 "Figure 2 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") we display the effects of model uncertainty and correlation between financial and insurance risks on the optimal consumption strategy with respect to the discount rate/time preference (see Figure [2](https://arxiv.org/html/2511.03031v1#S4.F2 "Figure 2 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) and the risk aversion (see Figure [2](https://arxiv.org/html/2511.03031v1#S4.F2 "Figure 2 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")). Figure [2](https://arxiv.org/html/2511.03031v1#S4.F2 "Figure 2 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") shows an inverted U-shape in all three cases which indicates a non-monotonic relationship between the patience level–measured by the discount rate δ\delta– of insurers and their consumption. The ambiguity-neutral case dominates with highest consumption throughout all cases followed by the general case. In all cases, there is peak consumption with varying values at δ≈0.07\delta\approx 0.07. Figure [2](https://arxiv.org/html/2511.03031v1#S4.F2 "Figure 2 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") shows a declining consumption with increasing risk aversion for all three curves. Our numerical results show a similar effect of the EIS coefficient on the consumption.

![Refer to caption](strategies_t0_vs_gamma_general.png)

![Refer to caption](strategies_t0_vs_gamma_no_uncertainty.png)

![Refer to caption](strategies_t0_vs_gamma_no_correlation.png)

Figure 3. The time-0 optimal investment and reinsurance with respect to the risk aversion for an ambiguity-neutral insurer (ANI case) and an ambiguity-averse insurer when considering correlation (General case) or no-correlation (No-correlation case) between financial and insurance risks.

In Figure [3](https://arxiv.org/html/2511.03031v1#S4.F3 "Figure 3 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") we display the time-0 robust optimal investment (ROIS) and reinsurance (RORS) strategies with respect to the risk aversion for all three cases: the ambiguity-neutral case (no uncertainty), the no-correlation between financial and insurance risks case, and the general case which is determined through the first equation in ([3.14](https://arxiv.org/html/2511.03031v1#S3.E14 "In Theorem 3.5. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")). We observe that, except in the no-correlation case (see Figure [3](https://arxiv.org/html/2511.03031v1#S4.F3 "Figure 3 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")), the ROIS always dominates the RORS (see Figures [3](https://arxiv.org/html/2511.03031v1#S4.F3 "Figure 3 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") and [3](https://arxiv.org/html/2511.03031v1#S4.F3 "Figure 3 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")). Our numerical results show similar behaviours of the ROIS and the RORS with respect to the EIS coefficient. In addition, all three graphs show a monotonic decline (with different magnitude) of ROIS and RORS as risk aversion increases. On contrary, our numerical results show that the EIS has little effect on the ROIS and the RORS.

![Refer to caption](value_function_vs_psi_all_cases_annotated.png)

![Refer to caption](value_function_vs_gamma_all_cases_annotated.png)

![Refer to caption](value_function_vs_delta_all_cases_annotated.png)

Figure 4. The value function for all cases.

In Figure [4](https://arxiv.org/html/2511.03031v1#S4.F4 "Figure 4 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") shows the sensitivity of the value function with respect to the EIS coefficient (see Figure [4](https://arxiv.org/html/2511.03031v1#S4.F4 "Figure 4 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")), the risk aversion coefficient (see Figure [4](https://arxiv.org/html/2511.03031v1#S4.F4 "Figure 4 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) and the discount factor (see Figure [4](https://arxiv.org/html/2511.03031v1#S4.F4 "Figure 4 ‣ 4. Numerical simulations ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) for all the three cases mentioned in the previous paragraph.

## 5. Conclusion

This paper addresses the complex problem of how an ambiguity-averse insurer should optimally manage consumption, investment, and reinsurance over a finite time horizon. The insurer’s wealth dynamics incorporate a financial market (a risk-free bond and a risky asset) and an insurance surplus process based on the diffusion approximation of the classical Cramér-Lundberg model. A key challenge is that the insurer operates under model uncertainty (ambiguity) regarding the true probabilities of asset returns and insurance claims. Furthermore, the insurer’s preferences are modeled using Epstein-Zin recursive utility, which allows for a separation between risk aversion and the elasticity of intertemporal substitution (EIS), a more realistic and flexible framework than traditional time-additive utilities.

To solve this robust control problem, a max-min optimisation problem is formulated, where the insurer maximises utility under the worst-case scenario from a set of plausible models, penalised by relative entropy. The solution is achieved by characterising the problem through a system of coupled forward-backward stochastic differential equations (FBSDEs). Using the martingale optimality principle, a closed-form analytical expressions for the optimal consumption is derived, investment, reinsurance, and the corresponding worst-case distortion process studied.

Through simulation, the results observed yield several important insights. The explicit formulas show that the optimal reinsurance strategy depends on financial market parameters, and the investment strategy depends on insurance market parameters, demonstrating an intrinsic co-dependence even when the two markets are uncorrelated. Numerical analyses confirm that optimal consumption decreases with higher risk aversion and EIS, while both investment and reinsurance strategies monotonically decline as risk aversion increases. The study successfully integrates robustness, recursive preferences, and liability management into a unified framework, providing actionable strategies for insurers navigating deep uncertainty.

## Appendix A Proof of Proposition [2.1](https://arxiv.org/html/2511.03031v1#S2.Thmdefi1 "Proposition 2.1. ‣ 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")

###### Proof.

We construct Vc,ξV^{c,\xi}, given by ([2.13](https://arxiv.org/html/2511.03031v1#S2.E13 "In 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")), via the BSDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vtc,ξ\displaystyle V\_{t}^{c,\xi} | =h​(cT)+∫tT(f​(cs,Vsc,ξ)+12​Φ​‖ξs‖2​(1−γ)​Vsc,ξ)​ds−∫tTZtc,ξ​dBsℚξ.\displaystyle=h(c\_{T})+\int\_{t}^{T}\Big(f(c\_{s},V\_{s}^{c,\xi})+\frac{1}{2\Phi}\|\xi\_{s}\|^{2}(1-\gamma)V\_{s}^{c,\xi}\Big)\mathrm{d}s-\int\_{t}^{T}Z\_{t}^{c,\xi}\mathrm{d}B\_{s}^{\mathbb{Q}^{\xi}}. |  | (A.1) |

Recall the definition of ff in ([2.10](https://arxiv.org/html/2511.03031v1#S2.E10 "In 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) with γ,ψ>1\gamma,\psi>1 (that is, θ<0\theta<0). Then the generator of the BSDE ([A.1](https://arxiv.org/html/2511.03031v1#A1.E1 "In Appendix A Proof of Proposition 2.1 ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) is not Lipschitz. We obtain the unique solution of ([A.1](https://arxiv.org/html/2511.03031v1#A1.E1 "In Appendix A Proof of Proposition 2.1 ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) in a suitable space via the transformation

|  |  |  |
| --- | --- | --- |
|  | (Yt,Zt):=e∫0t12​Φ​‖ξs‖2​ds​(1−γ)​(Vtc,ξ,Ztc,ξ),t∈[0,T],\displaystyle\big(Y\_{t},Z\_{t}\big):=e^{\int\_{0}^{t}\frac{1}{2\Phi}\|\xi\_{s}\|^{2}\mathrm{d}s}(1-\gamma)\big(V\_{t}^{c,\xi},Z\_{t}^{c,\xi}\big),~t\in[0,T], |  |

so that Equation ([A.1](https://arxiv.org/html/2511.03031v1#A1.E1 "In Appendix A Proof of Proposition 2.1 ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt\displaystyle Y\_{t} | =e−δ​θ​T​(e∫0T12​Φ​(1−γ)​‖ξs‖2​ds​cT)1−γ\displaystyle=e^{-\delta\theta T}\big(e^{\int\_{0}^{T}\frac{1}{2\Phi(1-\gamma)}\|\xi\_{s}\|^{2}\mathrm{d}s}c\_{T}\big)^{1-\gamma} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫tTδ​θ​e−δ​s​(e∫0s12​Φ​(1−γ)​‖ξu‖2​du​cs)1−1ψ​Ys1−1θ​ds−∫tTZt​dBsℚξ.\displaystyle\phantom{X}+\int\_{t}^{T}\delta\theta e^{-\delta s}\big(e^{\int\_{0}^{s}\frac{1}{2\Phi(1-\gamma)}\|\xi\_{u}\|^{2}\mathrm{d}u}c\_{s}\big)^{1-\frac{1}{\psi}}Y\_{s}^{1-\frac{1}{\theta}}\mathrm{d}s-\int\_{t}^{T}Z\_{t}\mathrm{d}B\_{s}^{\mathbb{Q}^{\xi}}. |  | (A.2) |

This is precisely the type of BSDE considered in [[12](https://arxiv.org/html/2511.03031v1#bib.bib12), Prop. 2.2] with csc\_{s} replaced by e∫0s12​Φ​(1−γ)​‖ξu‖2​du​cse^{\int\_{0}^{s}\frac{1}{2\Phi(1-\gamma)}\|\xi\_{u}\|^{2}\mathrm{d}u}c\_{s} for 0≤s≤T0\leq s\leq T. Hence, by the proof of [[12](https://arxiv.org/html/2511.03031v1#bib.bib12), Prop. 2.2], the unique solution (Y,Z)(Y,Z) of the BSDE ([A](https://arxiv.org/html/2511.03031v1#A1.Ex2 "Appendix A Proof of Proposition 2.1 ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) is such that YY is continuous, strictly positive and belongs to the class (D), and ∫0T‖Zs‖2​ds<∞\int\_{0}^{T}\|Z\_{s}\|^{2}\mathrm{d}s<\infty ℚξ\mathbb{Q}^{\xi}-a.s. Using the fact that Vtc,ξ=11−γ​e−∫0t12​Φ​‖ξs‖2​ds​YtV\_{t}^{c,\xi}=\frac{1}{1-\gamma}e^{-\int\_{0}^{t}\frac{1}{2\Phi}\|\xi\_{s}\|^{2}\mathrm{d}s}Y\_{t} for t∈[0,T]t\in[0,T], with t↦11−γ​e−∫0t12​Φ​‖ξs‖2​dst\mapsto\frac{1}{1-\gamma}e^{-\int\_{0}^{t}\frac{1}{2\Phi}\|\xi\_{s}\|^{2}\mathrm{d}s} bounded almost surely, we deduce that the process Vc,ξV^{c,\xi} is continuous, strictly negative and of class (D). Moreover, using the fact that Φ≥0\Phi\geq 0, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0T‖Zsc,ξ‖2​ds\displaystyle\int\_{0}^{T}\|Z\_{s}^{c,\xi}\|^{2}\mathrm{d}s | =1(1−γ)2​∫0Te−∫0s1Φ​‖ξu‖2​du​‖Zs‖2​ds\displaystyle=\frac{1}{(1-\gamma)^{2}}\int\_{0}^{T}e^{-\int\_{0}^{s}\frac{1}{\Phi}\|\xi\_{u}\|^{2}\mathrm{d}u}\|Z\_{s}\|^{2}\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | <1(1−γ)2​∫0T‖Zs‖2​ds<∞.\displaystyle<\frac{1}{(1-\gamma)^{2}}\int\_{0}^{T}\|Z\_{s}\|^{2}\mathrm{d}s<\infty. |  |

Hence, ∫0T‖Zsc,ξ‖2​ds<∞\int\_{0}^{T}\|Z\_{s}^{c,\xi}\|^{2}\mathrm{d}s<\infty ℚξ\mathbb{Q}^{\xi}-a.s.
That concludes the proof.
∎

## Appendix B Proof of Proposition [3.1](https://arxiv.org/html/2511.03031v1#S3.Thmdefi1 "Proposition 3.1. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")

###### Proof.

We show that the triple (X^,Y,Z)(\widehat{X},Y,Z) given by ([3.13](https://arxiv.org/html/2511.03031v1#S3.E13 "In Proposition 3.1. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) satisfies the FBSDE ([3.10](https://arxiv.org/html/2511.03031v1#S3.E10 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")). Let x¯\bar{x} denotes the constant defined by x¯:=x~​(−rm−δψ+Φ(γ+Φ)2​‖η‖2)\bar{x}:=\widetilde{x}\big(-r\_{m}-\delta^{\psi}+\frac{\Phi}{(\gamma+\Phi)^{2}}\|\eta\|^{2}\big). Applying Itô’s formula to YY we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yt\displaystyle\mathrm{d}Y\_{t} | =−x¯​erm​t​exp⁡(−1+2​(γ+Φ)2​(γ+Φ)2​‖η‖2​t+1γ+Φ​η⊺​Bt)​d​t\displaystyle=-\bar{x}e^{r\_{m}t}\exp\Big(\frac{-1+2(\gamma+\Phi)}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}t+\frac{1}{\gamma+\Phi}\eta^{\intercal}B\_{t}\Big)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +x¯​erm​T−erm​trm​(1γ+Φ​‖η‖2​d​t+1γ+Φ​η⊺​d​Bt)​exp⁡(−1+2​(γ+Φ)2​(γ+Φ)2​‖η‖2​t+1γ+Φ​η⊺​Bt)\displaystyle+\bar{x}\frac{e^{r\_{m}T}-e^{r\_{m}t}}{r\_{m}}\big(\frac{1}{\gamma+\Phi}\|\eta\|^{2}\mathrm{d}t+\frac{1}{\gamma+\Phi}\eta^{\intercal}\mathrm{d}B\_{t}\big)\exp\Big(\frac{-1+2(\gamma+\Phi)}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}t+\frac{1}{\gamma+\Phi}\eta^{\intercal}B\_{t}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(−x¯​erm​t+x¯​erm​T−erm​trm​1γ+Φ​‖η‖2)​exp⁡(−1+2​(γ+Φ)2​(γ+Φ)2​‖η‖2​t+1γ+Φ​η⊺​Bt)​d​t\displaystyle=\Big(-\bar{x}e^{r\_{m}t}+\bar{x}\frac{e^{r\_{m}T}-e^{r\_{m}t}}{r\_{m}}\frac{1}{\gamma+\Phi}\|\eta\|^{2}\Big)\exp\Big(\frac{-1+2(\gamma+\Phi)}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}t+\frac{1}{\gamma+\Phi}\eta^{\intercal}B\_{t}\Big)\mathrm{d}t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +x¯​erm​T−erm​trm​exp⁡(−1+2​(γ+Φ)2​(γ+Φ)2​‖η‖2​t+1γ+Φ​η⊺​Bt)​1γ+Φ​η⊺​d​Bt.\displaystyle+\bar{x}\frac{e^{r\_{m}T}-e^{r\_{m}t}}{r\_{m}}\exp\Big(\frac{-1+2(\gamma+\Phi)}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}t+\frac{1}{\gamma+\Phi}\eta^{\intercal}B\_{t}\Big)\frac{1}{\gamma+\Phi}\eta^{\intercal}\mathrm{d}B\_{t}. |  | (B.1) |

Using the definition of YY in ([3.13](https://arxiv.org/html/2511.03031v1#S3.E13 "In Proposition 3.1. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) we deduce that

|  |  |  |
| --- | --- | --- |
|  | x¯​erm​T−erm​trm​exp⁡(−1+2​(γ+Φ)2​(γ+Φ)2​‖η‖2​t+1γ+Φ​η⊺​Bt)​1γ+Φ​η\displaystyle\bar{x}\frac{e^{r\_{m}T}-e^{r\_{m}t}}{r\_{m}}\exp\Big(\frac{-1+2(\gamma+\Phi)}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}t+\frac{1}{\gamma+\Phi}\eta^{\intercal}B\_{t}\Big)\frac{1}{\gamma+\Phi}\eta |  |
|  |  |  |
| --- | --- | --- |
|  | =1γ+Φ​(Yt+e−r​T​G)​η.\displaystyle=\frac{1}{\gamma+\Phi}\big(Y\_{t}+e^{-rT}G\big)\eta. |  |

Let Zt=1γ+Φ​(Yt+e−r​T​G)​ηZ\_{t}=\frac{1}{\gamma+\Phi}\big(Y\_{t}+e^{-rT}G\big)\eta for t∈[0,T]t\in[0,T]. Then the generator of the BSDE ([B](https://arxiv.org/html/2511.03031v1#A2.Ex1 "Appendix B Proof of Proposition 3.1 ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) becomes

|  |  |  |
| --- | --- | --- |
|  | Zt⊺​η−x¯​erm​t​exp⁡(−1+2​(γ+Φ)2​(γ+Φ)2​‖η‖2​t+1γ+Φ​η⊺​Bt).\displaystyle Z\_{t}^{\intercal}\eta-\bar{x}e^{r\_{m}t}\exp\Big(\frac{-1+2(\gamma+\Phi)}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}t+\frac{1}{\gamma+\Phi}\eta^{\intercal}B\_{t}\Big). |  |

Hence, using the definition of x~,ξ^\widetilde{x},\widehat{\xi} and X^t+er​t​Yt,0≤t≤T\widehat{X}\_{t}+e^{rt}Y\_{t},~0\leq t\leq T, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yt\displaystyle\mathrm{d}Y\_{t} | =−(e−r​t​(δψψ−1+r+12​1γ+Φ​‖η‖2−δ​θ1−γ)​(X^t+er​t​Yt)−Zt⊺​η)​d​t+Zt⊺​d​Bt\displaystyle=-\Big(e^{-rt}\big(\frac{\delta^{\psi}}{\psi-1}+r+\frac{1}{2}\frac{1}{\gamma+\Phi}\|\eta\|^{2}{-\frac{\delta\theta}{1-\gamma}}\big)\big(\widehat{X}\_{t}+e^{rt}Y\_{t}\big)-Z\_{t}^{\intercal}\eta\Big)\mathrm{d}t+Z\_{t}^{\intercal}\mathrm{d}B\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−(e−r​t​(δψψ−1+r+12​1γ+Φ​‖η‖2−δ​θ1−γ)​(X^t+er​t​Yt)−Zt⊺​η)​d​t\displaystyle=-\Big(e^{-rt}\big(\frac{\delta^{\psi}}{\psi-1}+r+\frac{1}{2}\frac{1}{\gamma+\Phi}\|\eta\|^{2}{-\frac{\delta\theta}{1-\gamma}}\big)\big(\widehat{X}\_{t}+e^{rt}Y\_{t}\big)-Z\_{t}^{\intercal}\eta\Big)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Zt⊺​(d​Btℚξ^−Φγ+Φ​η​d​t)\displaystyle\phantom{X}+Z\_{t}^{\intercal}\big(\mathrm{d}B\_{t}^{\mathbb{Q}^{\widehat{\xi}}}-\frac{\Phi}{\gamma+\Phi}\eta\mathrm{d}t\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−(e−r​t​(δψψ−1+r+12​1γ+Φ​‖η‖2−δ​θ1−γ)​(X^t+er​t​Yt)−γγ+Φ​Zt⊺​η)​d​t\displaystyle=-\Big(e^{-rt}\big(\frac{\delta^{\psi}}{\psi-1}+r+\frac{1}{2}\frac{1}{\gamma+\Phi}\|\eta\|^{2}{-\frac{\delta\theta}{1-\gamma}}\big)\big(\widehat{X}\_{t}+e^{rt}Y\_{t}\big)-\frac{\gamma}{\gamma+\Phi}Z\_{t}^{\intercal}\eta\Big)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Zt⊺​d​Btℚξ^.\displaystyle\phantom{X}+Z\_{t}^{\intercal}\mathrm{d}B\_{t}^{\mathbb{Q}^{\widehat{\xi}}}. |  |

Similar arguments applied to X^\widehat{X} give

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​X^t\displaystyle\mathrm{d}\widehat{X}\_{t} | =(r​X^t+(−δψ+1γ+Φ​‖η‖2)​(X^t+er​t​Yt)−γγ+Φ​er​t​Zt⊺​η)​d​t\displaystyle=\Big(r\widehat{X}\_{t}+\big(-\delta^{\psi}{+\frac{1}{\gamma+\Phi}}\|\eta\|^{2}\big)(\widehat{X}\_{t}+e^{rt}Y\_{t})-{\frac{\gamma}{\gamma+\Phi}}e^{rt}Z\_{t}^{\intercal}\eta\Big)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1γ+Φ​(X^t+er​t​Yt)​η⊺−er​t​Zt⊺)​d​Btℚξ^.\displaystyle\phantom{X}+\Big({\frac{1}{\gamma+\Phi}}(\widehat{X}\_{t}+e^{rt}Y\_{t})\eta^{\intercal}-e^{rt}Z\_{t}^{\intercal}\Big)\mathrm{d}B\_{t}^{\mathbb{Q}^{\widehat{\xi}}}. |  |

Local uniqueness follows from lemma 2.12.1 in [[11](https://arxiv.org/html/2511.03031v1#bib.bib11)]. That concludes the proof.
∎

## Appendix C Proof of Lemmas [3.7](https://arxiv.org/html/2511.03031v1#S3.Thmdefi7 "Lemma 3.7. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences"), [3.8](https://arxiv.org/html/2511.03031v1#S3.Thmdefi8 "Lemma 3.8. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") and [3.9](https://arxiv.org/html/2511.03031v1#S3.Thmdefi9 "Lemma 3.9. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences"), and Theorem [3.5](https://arxiv.org/html/2511.03031v1#S3.Thmdefi5 "Theorem 3.5. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")

###### Proof of Lemma [3.7](https://arxiv.org/html/2511.03031v1#S3.Thmdefi7 "Lemma 3.7. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences").

The proof is split in three steps.

Step 1: (The positivity of X^t+er​t​Yt>0\widehat{X}\_{t}+e^{rt}Y\_{t}>0 for t∈[0,T]t\in[0,T]). Since X^t+er​t​Yt=x~​φt\widehat{X}\_{t}+e^{rt}Y\_{t}=\widetilde{x}\varphi\_{t}, the proof follows directly from the first and third conditions in Assumption [3.3](https://arxiv.org/html/2511.03031v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences"), and the positivity of φ\varphi defined in ([3.12](https://arxiv.org/html/2511.03031v1#S3.E12 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")).

Step 2: (The class (D) property of positivity of (X^+er​t​Y)1−γ(\widehat{X}+e^{rt}Y)^{1-\gamma}). We have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (X^t+er​t​Yt)1−γ\displaystyle(\widehat{X}\_{t}+e^{rt}Y\_{t})^{1-\gamma} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =x~1−γ​exp⁡((−δψ​θ+(1−γ)​(γ+3​Φ−1)2​(γ+Φ)2​‖η‖2+δ​θ)​t+1−γγ+Φ​η⊺​Bt)\displaystyle=\widetilde{x}^{1-\gamma}\exp\Big(\Big(-\delta^{\psi}\theta+{\frac{(1-\gamma)(\gamma+3\Phi-1)}{2(\gamma+\Phi)^{2}}}\|\eta\|^{2}+\delta\theta\Big)t+\frac{1-\gamma}{\gamma+\Phi}\eta^{\intercal}B\_{t}\Big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =x~1−γ​exp⁡((−δψ​θ+3​Φ​(1−γ)2​(γ+Φ)2​‖η‖2+δ​θ)​t)​ℰ​(∫1−γγ+Φ​η⊺​dB)t,\displaystyle=\widetilde{x}^{1-\gamma}\exp\Big(\Big(-\delta^{\psi}\theta+{\frac{3\Phi(1-\gamma)}{2(\gamma+\Phi)^{2}}}\|\eta\|^{2}+\delta\theta\Big)t\Big)\mathcal{E}\big(\int\frac{1-\gamma}{\gamma+\Phi}\eta^{\intercal}\mathrm{d}B\big)\_{t}, |  | (C.1) |

where ℰ​(∫βs​dBs)t:=exp⁡(−12​∫0t‖βs‖2​ds+∫0tβs​dBs)\mathcal{E}\big(\int\beta\_{s}\mathrm{d}B\_{s}\big)\_{t}:=\exp\big(-\frac{1}{2}\int\_{0}^{t}\|\beta\_{s}\|^{2}\mathrm{d}s+\int\_{0}^{t}\beta\_{s}\mathrm{d}B\_{s}\big) is the Doléans-Dade exponential at time tt. Observe that the process ℰ​(∫1−γγ+Φ​η⊺​dB)\mathcal{E}\big(\int\frac{1-\gamma}{\gamma+\Phi}\eta^{\intercal}\mathrm{d}B\big) is a ℙ\mathbb{P}-martingale (hence of class (D)); because 1−γγ+Φ​η⊺∈ℝ2\frac{1-\gamma}{\gamma+\Phi}\eta^{\intercal}\in\mathbb{R}^{2}. Hence the right-side of ([C](https://arxiv.org/html/2511.03031v1#A3.Ex1 "Appendix C Proof of Lemmas 3.7, 3.8 and 3.9, and Theorem 3.5 ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) is of class (D) as a product of a bounded deterministic function (because the constant x~\widetilde{x} is positive and finite) and a process of class (D). Thus, (X^+er​t​Y)1−γ(\widehat{X}+e^{rt}Y)^{1-\gamma} is of class (D).

Step 3: (Confirm that (c^,ξ^)∈𝒜a(\widehat{c},\widehat{\xi})\in\mathcal{A}\_{a}). Recall from ([3.7](https://arxiv.org/html/2511.03031v1#S3.E7 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) and ([3.5](https://arxiv.org/html/2511.03031v1#S3.E5 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) that ξ^t=Φγ+Φ​η\widehat{\xi}\_{t}=\frac{\Phi}{\gamma+\Phi}\eta (meaning, ξ^\widehat{\xi} is a constant) and c^t=δψ​(X^t+er​t​Yt)\widehat{c}\_{t}=\delta^{\psi}(\widehat{X}\_{t}+e^{rt}Y\_{t}) for t∈[0,T]t\in[0,T]. Then, using the definition of φ\varphi in ([3.12](https://arxiv.org/html/2511.03031v1#S3.E12 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")), Girsanov theorem and the facts that cT=X^T+er​T​YTc\_{T}=\widehat{X}\_{T}+e^{rT}Y\_{T} (see Definition [2.2](https://arxiv.org/html/2511.03031v1#S2.Thmdefi2 "Definition 2.2. ‣ 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) and ξ^\widehat{\xi} is a constant, we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚξ^​[e∫0T12​Φ​‖ξ^s‖2​ds​cT1−γ]\displaystyle\mathbb{E}^{\mathbb{Q}^{\widehat{\xi}}}\Big[e^{\int\_{0}^{T}\frac{1}{2\Phi}\|\widehat{\xi}\_{s}\|^{2}\mathrm{d}s}c\_{T}^{1-\gamma}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼[δψ​(1−γ)eΦ2​(γ+Φ)2​‖η‖2​Tℰ(∫−Φγ+Φη⊺dB)T\displaystyle=\mathbb{E}\Big[\delta^{\psi(1-\gamma)}e^{\frac{\Phi}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}T}\mathcal{E}\Big(\int-\frac{\Phi}{\gamma+\Phi}\eta^{\intercal}\mathrm{d}B\Big)\_{T} |  |
|  |  |  |
| --- | --- | --- |
|  | ×exp((−δψθ+(1−γ)​(γ+3​Φ−1)2​(γ+Φ)2∥η∥2+δθ)T+1−γγ+Φη⊺BT)]\displaystyle\phantom{XX}\times\exp\Big(\Big(-\delta^{\psi}\theta+{\frac{(1-\gamma)(\gamma+3\Phi-1)}{2(\gamma+\Phi)^{2}}}\|\eta\|^{2}+\delta\theta\Big)T+\frac{1-\gamma}{\gamma+\Phi}\eta^{\intercal}B\_{T}\Big)\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼[δψ​(1−γ)eΦ2​(γ+Φ)2​‖η‖2​Texp((−δψθ+Φ​(1−γ)2​(γ+Φ)2∥η∥2+δθ)T)\displaystyle=\mathbb{E}\Big[\delta^{\psi(1-\gamma)}e^{\frac{\Phi}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}T}\exp\Big(\Big(-\delta^{\psi}\theta+{\frac{\Phi(1-\gamma)}{2(\gamma+\Phi)^{2}}}\|\eta\|^{2}+\delta\theta\Big)T\Big) |  |
|  |  |  |
| --- | --- | --- |
|  | ×ℰ(∫1−γ−Φγ+Φη⊺dB)T]\displaystyle\phantom{XX}\times\mathcal{E}\Big(\int\frac{1-\gamma-\Phi}{\gamma+\Phi}\eta^{\intercal}\mathrm{d}B\Big)\_{T}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =δψ​(1−γ)​eΦ2​(γ+Φ)2​‖η‖2​T​exp⁡((−δψ​θ+Φ​(1−γ)2​(γ+Φ)2​‖η‖2+δ​θ)​T)\displaystyle=\delta^{\psi(1-\gamma)}e^{\frac{\Phi}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}T}\exp\Big(\Big(-\delta^{\psi}\theta+{\frac{\Phi(1-\gamma)}{2(\gamma+\Phi)^{2}}}\|\eta\|^{2}+\delta\theta\Big)T\Big) |  |
|  |  |  |
| --- | --- | --- |
|  | <∞,\displaystyle<\infty, |  |

where the third equality holds due to ℰ​(∫1−γ−Φγ+Φ​η⊺​dB)\mathcal{E}\Big(\int\frac{1-\gamma-\Phi}{\gamma+\Phi}\eta^{\intercal}\mathrm{d}B\Big) being a ℙ\mathbb{P}-martingale. Besides, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚξ​[∫0Te−δ​s​cs1−1ψ​ds]\displaystyle\mathbb{E}^{\mathbb{Q}^{\xi}}\Big[\int\_{0}^{T}e^{-\delta s}c\_{s}^{1-\frac{1}{\psi}}\mathrm{d}s\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =δψ−1x~1−1ψ𝔼[ℰ(∫−Φγ+Φη⊺dB)T\displaystyle=\delta^{\psi-1}\widetilde{x}^{1-\frac{1}{\psi}}\mathbb{E}\Big[\mathcal{E}\Big(\int-\frac{\Phi}{\gamma+\Phi}\eta^{\intercal}\mathrm{d}B\Big)\_{T} |  |
|  |  |  |
| --- | --- | --- |
|  | ×∫0Te−δ​sexp((−δψ+ψψ−1γ+3​Φ−12​(γ+Φ)2∥η∥2+δ)s+ψψ−11γ+Φη⊺Bs)ds]\displaystyle\times\int\_{0}^{T}e^{-\delta s}\exp\Big(\Big(-\delta^{\psi}+\frac{\psi}{\psi-1}\frac{\gamma+3\Phi-1}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}+\delta\Big)s+\frac{\psi}{\psi-1}\frac{1}{\gamma+\Phi}\eta^{\intercal}B\_{s}\Big)\mathrm{d}s\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤δψ−1​x~1−1ψ​(𝔼​[ℰ​(∫−Φγ+Φ​η⊺​d​B)T2])12\displaystyle\leq\delta^{\psi-1}\widetilde{x}^{1-\frac{1}{\psi}}\Big(\mathbb{E}\Big[\mathcal{E}\Big(\int-\frac{\Phi}{\gamma+\Phi}\eta^{\intercal}\mathrm{d}B\Big)\_{T}^{2}\Big]\Big)^{\frac{1}{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | ×(𝔼​[(∫0Texp⁡((−δψ+ψψ−1​γ+3​Φ−12​(γ+Φ)2​‖η‖2)​s+ψψ−1​1γ+Φ​η⊺​Bs)​ds)2])12\displaystyle\times\Big(\mathbb{E}\Big[\Big(\int\_{0}^{T}\exp\Big(\big(-\delta^{\psi}+\frac{\psi}{\psi-1}\frac{\gamma+3\Phi-1}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}\big)s+\frac{\psi}{\psi-1}\frac{1}{\gamma+\Phi}\eta^{\intercal}B\_{s}\Big)\mathrm{d}s\Big)^{2}\Big]\Big)^{\frac{1}{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤δψ−1​x~1−1ψ​(𝔼​[exp⁡(−(Φγ+Φ)2​‖η‖2​T−2​Φγ+Φ​η⊺​BT)])12\displaystyle\leq\delta^{\psi-1}\widetilde{x}^{1-\frac{1}{\psi}}\Big(\mathbb{E}\Big[\exp\Big(-\Big(\frac{\Phi}{\gamma+\Phi}\Big)^{2}\|\eta\|^{2}T-\frac{2\Phi}{\gamma+\Phi}\eta^{\intercal}B\_{T}\Big)\Big]\Big)^{\frac{1}{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | ×(T2​𝔼​[∫0Texp⁡((−2​δψ+ψψ−1​γ+3​Φ−1(γ+Φ)2​‖η‖2)​s+2​ψψ−1​1γ+Φ​η⊺​Bs)​ds])12\displaystyle\times\Big(T^{2}\mathbb{E}\Big[\int\_{0}^{T}\exp\big(\Big(-2\delta^{\psi}+\frac{\psi}{\psi-1}\frac{\gamma+3\Phi-1}{(\gamma+\Phi)^{2}}\|\eta\|^{2}\Big)s+\frac{2\psi}{\psi-1}\frac{1}{\gamma+\Phi}\eta^{\intercal}B\_{s}\big)\mathrm{d}s\Big]\Big)^{\frac{1}{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | =δψ−1​x~1−1ψ​exp⁡(Φ22​(γ+Φ)2​‖η‖2​T)​(𝔼​[ℰ​(∫−2​Φγ+Φ​η⊺​d​B)T])12\displaystyle=\delta^{\psi-1}\widetilde{x}^{1-\frac{1}{\psi}}\exp\Big(\frac{\Phi^{2}}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}T\Big)\Big(\mathbb{E}\Big[\mathcal{E}\Big(\int-\frac{2\Phi}{\gamma+\Phi}\eta^{\intercal}\mathrm{d}B\Big)\_{T}\Big]\Big)^{\frac{1}{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | ×(𝔼[∫0Texp((−2δψ+ψ(ψ−1)2(ψ−1)​(γ+3​Φ−1)+2​ψ(γ+Φ)2∥η∥2+δ)s)\displaystyle\times\Big(\mathbb{E}\Big[\int\_{0}^{T}\exp\Big(\Big(-2\delta^{\psi}+\frac{\psi}{(\psi-1)^{2}}\frac{(\psi-1)(\gamma+3\Phi-1)+2\psi}{(\gamma+\Phi)^{2}}\|\eta\|^{2}+\delta\Big)s\Big) |  |
|  |  |  |
| --- | --- | --- |
|  | ×ℰ(∫2​ψψ−11γ+Φη⊺dB)sds])12\displaystyle\phantom{XXXXX}\times\mathcal{E}\Big(\int\frac{2\psi}{\psi-1}\frac{1}{\gamma+\Phi}\eta^{\intercal}\mathrm{d}B\Big)\_{s}\mathrm{d}s\Big]\Big)^{\frac{1}{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | =δψ−1​x~1−1ψ​exp⁡(Φ22​(γ+Φ)2​‖η‖2​T)\displaystyle=\delta^{\psi-1}\widetilde{x}^{1-\frac{1}{\psi}}\exp\Big(\frac{\Phi^{2}}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}T\Big) |  |
|  |  |  |
| --- | --- | --- |
|  | ×∫0Texp((−2δψ+ψ(ψ−1)2(ψ−1)​(γ+3​Φ−1)+2​ψ(γ+Φ)2∥η∥2+δ)s)ds\displaystyle\times\int\_{0}^{T}\exp\Big(\Big(-2\delta^{\psi}+\frac{\psi}{(\psi-1)^{2}}\frac{(\psi-1)(\gamma+3\Phi-1)+2\psi}{(\gamma+\Phi)^{2}}\|\eta\|^{2}+\delta\Big)s\Big)\mathrm{d}s |  |
|  |  |  |
| --- | --- | --- |
|  | <∞,\displaystyle<\infty, |  |

where the first inequality follows from Cauchy-Schwarz’s inequality, the second comes from Jensen’s inequality, and the third equality holds due to the fact that ℰ​(∫−2​Φγ+Φ​η⊺​d​B)\mathcal{E}\Big(\int-\frac{2\Phi}{\gamma+\Phi}\eta^{\intercal}\mathrm{d}B\Big) and ℰ​(∫2​ψψ−1​1γ+Φ​η⊺​dB)\mathcal{E}\Big(\int\frac{2\psi}{\psi-1}\frac{1}{\gamma+\Phi}\eta^{\intercal}\mathrm{d}B\Big) are ℙ\mathbb{P}-martingales.
∎

###### Proof of Lemma [3.8](https://arxiv.org/html/2511.03031v1#S3.Thmdefi8 "Lemma 3.8. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences").

The proof follows similar arguments as in the third step in the proof of proposition 2.22.2 in [[12](https://arxiv.org/html/2511.03031v1#bib.bib12)] with the generators F​(s,cs,Ys)F(s,c\_{s},Y\_{s}) and F​(s,cs,Y~s)F(s,c\_{s},\tilde{Y}\_{s}) replaced by f​(cs,Ys)+12​Φ​‖ξs‖2​(1−γ)​Ysf(c\_{s},Y\_{s})+\frac{1}{2\Phi}\|\xi\_{s}\|^{2}(1-\gamma)Y\_{s} and f​(cs,Y~s)+12​Φ​‖ξs‖2​(1−γ)​Y~sf(c\_{s},\tilde{Y}\_{s})+\frac{1}{2\Phi}\|\xi\_{s}\|^{2}(1-\gamma)\tilde{Y}\_{s}, respectively, for all s∈[0,T]s\in[0,T].
∎

###### Proof of Lemma [3.9](https://arxiv.org/html/2511.03031v1#S3.Thmdefi9 "Lemma 3.9. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences").

For a triple (c,π,ξ)(c,\pi,\xi) of admissible consumption, investment-reinsurance and distortion strategies (that is, (c,π,ξ)∈𝒜A​A​I(c,\pi,\xi)\in\mathcal{A}^{AAI}; see Definition [2.2](https://arxiv.org/html/2511.03031v1#S2.Thmdefi2 "Definition 2.2. ‣ 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")). Let (Mt)t∈[0,T](M\_{t})\_{t\in[0,T]} be the process given in ([3](https://arxiv.org/html/2511.03031v1#S3.Ex1 "3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mtc,π,ξ\displaystyle M\_{t}^{c,\pi,\xi} | :=e−δ​θ​t​(Xt+er​t​Yt)1−γ1−γ\displaystyle:={e^{-\delta\theta t}}\frac{(X\_{t}+e^{rt}Y\_{t})^{1-\gamma}}{1-\gamma} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0t(f​(cs,e−δ​θ​s​(Xs+er​s​Ys)1−γ1−γ)+12​Φ​‖ξ‖2​(Xs+er​s​Ys)1−γ)​ds.\displaystyle\phantom{xx}+\int\_{0}^{t}\Big(f\big(c\_{s},e^{-\delta\theta s}\frac{(X\_{s}+e^{rs}Y\_{s})^{1-\gamma}}{1-\gamma}\big)+\frac{1}{2\Phi}\|\xi\|^{2}(X\_{s}+e^{rs}Y\_{s})^{1-\gamma}\Big)\mathrm{d}s. |  |

Using ([3](https://arxiv.org/html/2511.03031v1#S3.Ex2 "3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) and ([3](https://arxiv.org/html/2511.03031v1#S3.Ex24 "3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) we deduce that MM is a local super-martingale. Moreover, using the Doob-Meyer decomposition and martingale representation, there exists an increasing process AA and a process ZMZ^{M} such that M=−A+∫0⋅ZsM​dBsℚξM=-A+\int\_{0}^{\cdot}Z\_{s}^{M}\mathrm{d}B\_{s}^{\mathbb{Q}^{\xi}}. Hence, (e−δ​θ⁣⋅​(X+e∫0rs​ds​Y)1−γ1−γ,ZM)(e^{-\delta\theta\cdot}\frac{(X+e^{\int\_{0}r\_{s}\mathrm{d}s}Y)^{1-\gamma}}{1-\gamma},Z^{M}) is a super-solution to ([2.16](https://arxiv.org/html/2511.03031v1#S2.E16 "In Proposition 2.1. ‣ 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) with integrable terminal condition e−δ​θ​T​(XT−G)1−γ1−γe^{-\delta\theta T}\frac{(X\_{T}-G)^{1-\gamma}}{1-\gamma}; see Lemma [3.8](https://arxiv.org/html/2511.03031v1#S3.Thmdefi8 "Lemma 3.8. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") for the notion of sub-/super- solutions of BSDEs. Now, consider the utility Vc,ξV^{c,\xi} associated to the consumption stream cc and the terminal lump sum XT−GX\_{T}-G; meaning that Vc,ξV^{c,\xi} is the first part of the solution of the BSDE ([2.16](https://arxiv.org/html/2511.03031v1#S2.E16 "In Proposition 2.1. ‣ 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) with terminal value h​(XT−G)h(X\_{T}-G). Therefore, using Lemma [3.8](https://arxiv.org/html/2511.03031v1#S3.Thmdefi8 "Lemma 3.8. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") we confirm Equation ([3.16](https://arxiv.org/html/2511.03031v1#S3.E16 "In Lemma 3.9. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")).
∎

###### Proof of lemma [3.10](https://arxiv.org/html/2511.03031v1#S3.Thmdefi10 "Lemma 3.10. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences").

Consider the process Mc,π,ξM^{c,\pi,\xi} defined by ([3](https://arxiv.org/html/2511.03031v1#S3.Ex2 "3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) for all (c,π,ξ)∈𝒜A​A​I(c,\pi,\xi)\in\mathcal{A}^{AAI}. For the consumption c^\widehat{c}, investment-reinsurance π^\widehat{\pi} and distortion process ξ^\widehat{\xi} (with associated function ℋ\mathcal{H}, given by ([3.8](https://arxiv.org/html/2511.03031v1#S3.E8 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")), of the BSDE ([2.18](https://arxiv.org/html/2511.03031v1#S2.E18 "In 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences"))) given by ([3.5](https://arxiv.org/html/2511.03031v1#S3.E5 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")), ([3.6](https://arxiv.org/html/2511.03031v1#S3.E6 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")), ([3.7](https://arxiv.org/html/2511.03031v1#S3.E7 "In 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) and , respectively, one can show that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Mtc^,π^,ξ^\displaystyle\mathrm{d}M\_{t}^{\widehat{c},\widehat{\pi},\widehat{\xi}} | =e−δ​θ​t​(X^tF+e∫0trs​ds​YtF)1−γ1−γ​1−γγ+Φ​η⊺​d​Btℚξ,0≤t≤T.\displaystyle=e^{-\delta\theta t}\frac{(\widehat{X}\_{t}^{F}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t}^{F})^{1-\gamma}}{1-\gamma}\frac{1-\gamma}{\gamma+\Phi}\eta^{\intercal}\mathrm{d}B\_{t}^{\mathbb{Q}^{\xi}},~0\leq t\leq T. |  | (C.2) |

On the other hand, using successively ([3](https://arxiv.org/html/2511.03031v1#S3.Ex1 "3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) and ([2.10](https://arxiv.org/html/2511.03031v1#S2.E10 "In 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Mtc^,π^,ξ^\displaystyle\mathrm{d}M\_{t}^{\widehat{c},\widehat{\pi},\widehat{\xi}} | =d​(e−δ​θ​t​(X^tF+e∫0trs​ds​YtF)1−γ1−γ)\displaystyle=\mathrm{d}\Big({e^{-\delta\theta t}}\frac{(\widehat{X}\_{t}^{F}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t}^{F})^{1-\gamma}}{1-\gamma}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(f​(c^t,e−δ​θ​t​(X^t+er​t​Yt)1−γ1−γ)+Φ2​(γ+Φ)2​‖η‖2​(X^t+er​t​Yt)1−γ)​d​t\displaystyle\phantom{X}+\Big(f\big(\widehat{c}\_{t},e^{-\delta\theta t}\frac{(\widehat{X}\_{t}+e^{rt}Y\_{t})^{1-\gamma}}{1-\gamma}\big)+\frac{\Phi}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}(\widehat{X}\_{t}+e^{rt}Y\_{t})^{1-\gamma}\Big)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =d​(e−δ​θ​t​(X^tF+e∫0trs​ds​YtF)1−γ1−γ)\displaystyle=\mathrm{d}\Big(e^{-\delta\theta t}\frac{(\widehat{X}\_{t}^{F}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t}^{F})^{1-\gamma}}{1-\gamma}\Big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(δψ​θ+Φ​(1−γ)2​(γ+Φ)2​‖η‖2​eδ​θ​t)​e−δ​θ​t​(X^tF+e∫0trs​ds​YtF)1−γ1−γ​d​t.\displaystyle\phantom{X}+\Big(\delta^{\psi}\theta+\frac{\Phi(1-\gamma)}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}e^{\delta\theta t}\Big)e^{-\delta\theta t}\frac{(\widehat{X}\_{t}^{F}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t}^{F})^{1-\gamma}}{1-\gamma}\mathrm{d}t. |  | (C.3) |

Hence, combining ([C.2](https://arxiv.org/html/2511.03031v1#A3.E2 "In Appendix C Proof of Lemmas 3.7, 3.8 and 3.9, and Theorem 3.5 ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) and ([C](https://arxiv.org/html/2511.03031v1#A3.Ex25 "Appendix C Proof of Lemmas 3.7, 3.8 and 3.9, and Theorem 3.5 ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | d​(e−δ​θ​t​(X^tF+e∫0trs​ds​YtF)1−γ1−γ)+(δψ​θ+Φ​(1−γ)2​(γ+Φ)2​‖η‖2​eδ​θ​t)​e−δ​θ​t​(X^tF+e∫0trs​ds​YtF)1−γ1−γ​d​t\displaystyle\mathrm{d}\Big(e^{-\delta\theta t}\frac{(\widehat{X}\_{t}^{F}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t}^{F})^{1-\gamma}}{1-\gamma}\Big)+\Big(\delta^{\psi}\theta+\frac{\Phi(1-\gamma)}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}e^{\delta\theta t}\Big)e^{-\delta\theta t}\frac{(\widehat{X}\_{t}^{F}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t}^{F})^{1-\gamma}}{1-\gamma}\mathrm{d}t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =e−δ​θ​t​(X^tF+e∫0trs​ds​YtF)1−γ1−γ​1−γγ​ηt⊺​d​Btℚξ.\displaystyle={e^{-\delta\theta t}}\frac{(\widehat{X}\_{t}^{F}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t}^{F})^{1-\gamma}}{1-\gamma}\frac{1-\gamma}{\gamma}\eta\_{t}^{\intercal}\mathrm{d}B\_{t}^{\mathbb{Q}^{\xi}}. |  | (C.4) |

Multiplying both sides of ([C](https://arxiv.org/html/2511.03031v1#A3.Ex28 "Appendix C Proof of Lemmas 3.7, 3.8 and 3.9, and Theorem 3.5 ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) by exp⁡(∫0t(δψ​θ+Φ​(1−γ)2​(γ+Φ)2​‖η‖2​eδ​θ​s)​ds),0≤t≤T\exp\big(\int\_{0}^{t}\big(\delta^{\psi}\theta+\frac{\Phi(1-\gamma)}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}e^{\delta\theta s}\big)\mathrm{d}s\big),~0\leq t\leq T, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | M~t=M~0​ℰ​(∫1−γγ​η⊺​dBℚξ)t​ for ​t∈[0,T],\displaystyle\widetilde{M}\_{t}=\widetilde{M}\_{0}\mathcal{E}\big(\int\frac{1-\gamma}{\gamma}\eta^{\intercal}\mathrm{d}B^{\mathbb{Q}^{\xi}}\big)\_{t}~\text{ for }t\in[0,T], |  | (C.5) |

where ℰ​(∫β⊺​dBℚξ)t:=exp⁡(−12​∫0t‖βs‖2​ds+∫0tβs⊺​dBsℚξ)\mathcal{E}(\int\beta^{\intercal}\mathrm{d}B^{\mathbb{Q}^{\xi}})\_{t}:=\exp\left(-\frac{1}{2}\int\_{0}^{t}\|\beta\_{s}\|^{2}\mathrm{d}s+\int\_{0}^{t}\beta\_{s}^{\intercal}\mathrm{d}B\_{s}^{\mathbb{Q}^{\xi}}\right).
∎

###### Proof of Theorem [3.5](https://arxiv.org/html/2511.03031v1#S3.Thmdefi5 "Theorem 3.5. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences").

Thanks to Lemma [3.7](https://arxiv.org/html/2511.03031v1#S3.Thmdefi7 "Lemma 3.7. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") the uplet (c^,π^S,π^r​e,ξ^)(\widehat{c},\widehat{\pi}^{S},\widehat{\pi}^{re},\widehat{\xi}) given by ([3.14](https://arxiv.org/html/2511.03031v1#S3.E14 "In Theorem 3.5. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) is admissible in the sense of Definition [2.2](https://arxiv.org/html/2511.03031v1#S2.Thmdefi2 "Definition 2.2. ‣ 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") with π^=(π^S,π^r​e)​Σ\widehat{\pi}=(\widehat{\pi}^{S},\widehat{\pi}^{re})\Sigma. Next, we prove that (c^,π^S,π^r​e,ξ^)(\widehat{c},\widehat{\pi}^{S},\widehat{\pi}^{re},\widehat{\xi}) is optimal. Let M~\widetilde{M} be as in Lemma [3.10](https://arxiv.org/html/2511.03031v1#S3.Thmdefi10 "Lemma 3.10. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences"). Thanks to Lemma [3.10](https://arxiv.org/html/2511.03031v1#S3.Thmdefi10 "Lemma 3.10. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences"), there exists a square integrable process Z~\widetilde{Z} such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​M~t\displaystyle\mathrm{d}\widetilde{M}\_{t} | =Z~t​d​Btℚξ^,0≤t≤T.\displaystyle=\widetilde{Z}\_{t}\mathrm{d}B\_{t}^{\mathbb{Q}^{\widehat{\xi}}},~0\leq t\leq T. |  | (C.6) |

Substituting ([3.17](https://arxiv.org/html/2511.03031v1#S3.E17 "In Lemma 3.10. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) into the left-side of ([C.6](https://arxiv.org/html/2511.03031v1#A3.E6 "In Appendix C Proof of Lemmas 3.7, 3.8 and 3.9, and Theorem 3.5 ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")) and applying Itô’s formula we obtain

|  |  |  |
| --- | --- | --- |
|  | d​(e−δ​θ​t​(X^tF+e∫0trs​ds​YtF)1−γ1−γ)+(δψ​θ+Φ​(1−γ)2​(γ+Φ)2​‖η‖2​eδ​θ​t)​e−δ​θ​t​(X^tF+e∫0trs​ds​YtF)1−γ1−γ​d​t\displaystyle\mathrm{d}\Big(e^{-\delta\theta t}\frac{(\widehat{X}\_{t}^{F}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t}^{F})^{1-\gamma}}{1-\gamma}\Big)+\Big(\delta^{\psi}\theta+\frac{\Phi(1-\gamma)}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}e^{\delta\theta t}\Big)e^{-\delta\theta t}\frac{(\widehat{X}\_{t}^{F}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t}^{F})^{1-\gamma}}{1-\gamma}\mathrm{d}t |  |
|  |  |  |
| --- | --- | --- |
|  | =exp⁡(−∫0t(δψ​θ+Φ​(1−γ)2​(γ+Φ)2​‖η‖2​eδ​θ​s)​ds)​Z~t​d​Btℚξ^.\displaystyle=\exp\Big(-\int\_{0}^{t}\big(\delta^{\psi}\theta+\frac{\Phi(1-\gamma)}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}e^{\delta\theta s}\big)\mathrm{d}s\Big)\widetilde{Z}\_{t}\mathrm{d}B\_{t}^{\mathbb{Q}^{\widehat{\xi}}}. |  |

Hence, using the fact that

|  |  |  |
| --- | --- | --- |
|  | f​(c^t,e−δ​θ​t​(X^t+er​t​Yt)1−γ1−γ)+Φ2​(γ+Φ)2​‖η‖2​(X^t+er​t​Yt)1−γ\displaystyle f\big(\widehat{c}\_{t},e^{-\delta\theta t}\frac{(\widehat{X}\_{t}+e^{rt}Y\_{t})^{1-\gamma}}{1-\gamma}\big)+\frac{\Phi}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}(\widehat{X}\_{t}+e^{rt}Y\_{t})^{1-\gamma} |  |
|  |  |  |
| --- | --- | --- |
|  | =(δψ​θ+Φ​(1−γ)2​(γ+Φ)2​‖η‖2​eδ​θ​t)​e−δ​θ​t​(X^tF+e∫0trs​ds​YtF)1−γ1−γ\displaystyle=\Big(\delta^{\psi}\theta+\frac{\Phi(1-\gamma)}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}e^{\delta\theta t}\Big)e^{-\delta\theta t}\frac{(\widehat{X}\_{t}^{F}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t}^{F})^{1-\gamma}}{1-\gamma} |  |

for t∈[0,T]t\in[0,T], and YT=−e−r​T​GY\_{T}=-e^{-rT}G we have (recall the definition of hh just below ([2.10](https://arxiv.org/html/2511.03031v1#S2.E10 "In 2.2. The consumption, investment and reinsurance problem for an ambiguity-averse insurer ‣ 2. Model and problem formulation ‣ Robust optimal consumption, investment and reinsurance for recursive preferences")))

|  |  |  |  |
| --- | --- | --- | --- |
|  | (X^0+Y0)1−γ1−γ\displaystyle\frac{(\widehat{X}\_{0}+Y\_{0})^{1-\gamma}}{1-\gamma} | =𝔼[h(X^T−G)+∫0T(f(c^t,e−δ​θ​t(X^t+er​t​Yt)1−γ1−γ)\displaystyle=\mathbb{E}\Big[h(\widehat{X}\_{T}-G)+\int\_{0}^{T}\Big(f\big(\widehat{c}\_{t},e^{-\delta\theta t}\frac{(\widehat{X}\_{t}+e^{rt}Y\_{t})^{1-\gamma}}{1-\gamma}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Φ2​(γ+Φ)2∥η∥2(X^t+er​tYt)1−γ)ds].\displaystyle\phantom{XXXXXXXXXXXx}+\frac{\Phi}{2(\gamma+\Phi)^{2}}\|\eta\|^{2}(\widehat{X}\_{t}+e^{rt}Y\_{t})^{1-\gamma}\Big)\mathrm{d}s\Big]. |  |

Hence the upper bound in Lemma [3.9](https://arxiv.org/html/2511.03031v1#S3.Thmdefi9 "Lemma 3.9. ‣ 3. Solution to the AAI’s stochastic optimisation problem ‣ Robust optimal consumption, investment and reinsurance for recursive preferences") is attained by (c^,π^S,π^r​e,ξ^)(\widehat{c},\widehat{\pi}^{S},\widehat{\pi}^{re},\widehat{\xi}). We conclude that (c^,π^S,π^r​e,ξ^)(\widehat{c},\widehat{\pi}^{S},\widehat{\pi}^{re},\widehat{\xi}) is optimal.
∎

## Acknowledgments

We would like to acknowledge fruitful discussions with Prof. Olivier Menoukeu Pamen.

## References

* [1]
   Asmussen, S., Steffensen, M.:
  Risk and Insurance. Springer, Berlin, 2020.
* [2]
   Bäuerle, N.: Benchmark and mean-variance problems for insurers. Mathematical Methods of Operations Research, 62: 159–165, 2005.
* [3]
   Chen, Z., Yang, P.: Robust optimal reinsurance–investment strategy with price jumps and correlated claims. Insurance: Mathematics and Economics, 92: 27–46, 2020.
* [4]
   Epstein, L.G., and Zin, S.E.:
  Substitution, risk aversion, and the temporal behavior of consumption and asset returns: A theoretical framework. Econometrica, 57: 937–969, 1989.
* [5]
   Hansen, L., Sargent, T.:
  Robust control and model uncertainty. American Economic Review, 91: 60–66, 2001.
* [6]
   Hu, Y., Imkeller, P., Müller, M.:
  Utility maximization in incomplete markets. Annals of Applied Probability, 15: 1691–1712, 2005.
* [7]
   Kuissi-Kamdem, W.: Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk. hal-05345383, 2025.
* [8]
   Ma, J., Lu, Z., Chen, D.: Optimal reinsurance-investment with loss aversion under rough Heston model. Quantitative Finance, 23: 95–109, 2023.
* [9]
   Maenhout, P.J.: Robust portfolio rules and asset pricing. Review of Financial Studies, 17: 951–983, 2004.
* [10]
   Schmidli, H.: Stochastic Control in Insurance. Springer-Verlag, London, 2008.
* [11]
   Xie, B., Yu, Z.: An exploration of Lp-theory for forward-backward stochastic differential equations with random coefficients on small durations. Journal of Mathematical Analysis and Applications, 483: 123642, 2020.
* [12]
   Xing, H.: Consumption–investment optimization with Epstein–Zin utility in incomplete markets. Finance and Stochastics, 21: 227–262, 2017.