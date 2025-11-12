---
authors:
- Alexandre Carbonneau
doc_id: arxiv:2007.15128v1
family_id: arxiv:2007.15128
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[2007.15128] Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA
  GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau.
  The author gratefully acknowledges financial support from the Fonds de recherche
  du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments
  and suggestions.'
url_abs: http://arxiv.org/abs/2007.15128v1
url_html: https://ar5iv.org/html/2007.15128v1
venue: arXiv q-fin
version: 1
year: 2020
---


Alexandre Carbonneau
Email address:[alexandre.carbonneau@mail.concordia.ca](mailto:alexandre.carbonneau@mail.concordia.ca)

###### Abstract

This study presents a deep reinforcement learning approach for global hedging of long-term financial derivatives. A similar setup as in Coleman et al., ([2007](#bib.bib18)) is considered with the risk management of lookback options embedded in guarantees of variable annuities with ratchet features.
The deep hedging algorithm of [Buehler et al., 2019a](#bib.bib15)  is applied to optimize neural networks representing global hedging policies with both quadratic and non-quadratic penalties.
To the best of the author’s knowledge, this is the first paper that presents an extensive benchmarking of global policies for long-term contingent claims with the use of various hedging instruments (e.g. underlying and standard options) and with the presence of jump risk for equity.
Monte Carlo experiments demonstrate the vast superiority of non-quadratic global hedging as it results simultaneously in downside risk metrics two to three times smaller than best benchmarks and in significant hedging gains.
Analyses show that the neural networks are able to effectively adapt their hedging decisions to different penalties and stylized facts of risky asset dynamics only by experiencing simulations of the financial market exhibiting these features.
Numerical results also indicate that non-quadratic global policies are significantly more geared towards being long equity risk which entails earning the equity risk premium.

Keywords: Reinforcement learning; Global hedging; Variable annuity; Lookback option; Jump risk.

## 1   Introduction

Variable annuities (VAs), also known as segregated funds and equity-linked insurance, are financial products that enable investors to gain exposure to the market through cashflows that depend on equity performance. These products often include financial guarantees to protect investors against downside equity risk with benefits which can be expressed as the payoff of derivatives. For instance, a guaranteed minimum maturity benefit (GMMB) with ratchet feature is analogous to a lookback put option by providing a minimum monetary amount at the maturity of the contract equal to the maximum account value on specific dates (e.g. anniversary dates of the policy).
The valuation of VAs guarantees is typically done with classical option pricing theory by computing the expected risk-neutral discounted cashflows of embedded options under an appropriate equivalent martingale measure; see, for instance, Brennan and Schwartz, ([1976](#bib.bib14)), Boyle and Schwartz, ([1977](#bib.bib13)), Persson and Aase, ([1997](#bib.bib44)), Bacinello, ([2003](#bib.bib6)) and Bauer et al., ([2008](#bib.bib7)). A comprehensive review of pricing segregated funds guarantees literature can be found in Gan, ([2013](#bib.bib25)).

During the subprime mortgage financial crisis, many insurers incurred large losses in segregated fund portfolios due in part to poor risk management with some insurers even stopping writing VAs guarantees in certain markets (Zhang, ([2010](#bib.bib53))). Two categories of risk management approaches are typically used in practice: the actuarial method and the financial engineering method (Boyle and Hardy, ([1997](#bib.bib12))). The foremost
consist
in providing stochastic models for the risk factors and setting a reserve held in risk-free assets to cover the liabilities associated to VAs guarantees with a certain probability (e.g. the Value-at-Risk at 99%percent9999\%). The second approach commonly known as dynamic hedging entails finding a self-funded sequence of positions in securities to hedge the risk exposure of embedded options. Dynamic hedging is a popular risk management approach among insurance companies and is studied in this current paper;
the reader is referred to Hardy, ([2003](#bib.bib31)) for a detailed description of the actuarial approach.

Financial markets are said to be complete if every contingent claim can be perfectly replicated with some dynamic hedging strategy. In practice, segregated funds embedded options are typically not attainable as a consequence of their many interrelated risks which are very complex to manage such as equity risk, interest rate risk, mortality risk and basis risk. For insurance companies selling VAs with guarantees, market incompleteness entails that some level of residual risk must be accepted as being intrinsic to the embedded options; the identification of optimal hedging policies in such context is thus highly relevant.
Nevertheless, the attention of the actuarial literature has predominantly been on the valuation of segregated funds, not on the design of optimal hedging policies. Indeed, the hedging strategies considered are most often suboptimal and are not necessarily in line with the financial objectives of insurance companies.
One popular hedging approach is the greek-based policy where assets positions depend on the sensitivities of the option value (i.e. the value of the guarantee) to different risk factors. Boyle and Hardy, ([1997](#bib.bib12)) and Hardy, ([2000](#bib.bib32)) delta-hedge GMMBs under market completeness for mortality risk and Augustyniak and Boudreault, ([2017](#bib.bib4)) delta-rho hedge GMMBs and guaranteed minimum death benefits (GMDBs) in the presence of model uncertainty for both equity and interest rate.
An important pitfall of greek-based policies in incomplete markets is their suboptimality by design: they are a by-product of the choice of pricing kernel (i.e. of the equivalent martingale measure) for option valuation, not of an optimization
procedure over hedging decisions to minimize residual risk.
Also, as shown in the seminal work of Harrison and Pliska, ([1981](#bib.bib33)), in incomplete markets, there exist an infinite set of equivalent martingale measures each of which is consistent with arbitrage-free pricing and can thus be used to compute the hedging positions (i.e. the greeks).

Another strand of literature optimizes hedging policies with local and global criterions. Local risk minimization (Föllmer and Schweizer, ([1988](#bib.bib23)) and Schweizer, ([1991](#bib.bib49)))
consists in choosing assets positions to minimize the periodic risk associated with the hedging portfolio. On the other hand, global risk minimization procedures jointly optimize all hedging decisions
with the objective of minimizing the expected value of a loss function applied to the terminal hedging error. In spite of their myopic view
of the hedging problem by not necessarily minimizing the risk associated with hedging shortfalls, local risk minimization procedures are attractive for the risk mitigation of VAs guarantees as they are simple to implement and they
have outperformed greek-based hedging in several studies. Coleman et al., ([2006](#bib.bib19)) and Coleman et al., ([2007](#bib.bib18)) apply local risk minimization procedures for risk mitigation of GMDBs using standard options with the foremost considering the presence of both interest rate and jump risk and the latter the presence of volatility and jump risk. Kélani and Quittard-Pinon, ([2017](#bib.bib37)) extends the work of Coleman et al., ([2007](#bib.bib18)) in a general Lévy market by including mortality and transaction costs, and [Trottier et al., 2018b](#bib.bib52)  and [Trottier et al., 2018a](#bib.bib51)  propose a local risk minimization scheme for guarantees in the presence of basis risk.

Within the realm of total risk minimization, global quadratic hedging pioneered by the seminal work of Schweizer, ([1995](#bib.bib50)) aims at jointly optimizing all hedging decisions with a quadratic penalty for hedging shortfalls. The latter paper provides a
theoretical solution to the optimal policy with a single risky asset (see Rémillard and Rubenthaler, ([2013](#bib.bib46)) for the multidimensional asset case) and
Bertsimas et al., ([2001](#bib.bib10)) develops a tractable solution to the optimal policy relying on stochastic dynamic programming.
A major drawback of global quadratic hedging is in penalizing equally gains and losses which is naturally not in line with the financial objectives of insurance companies. Alternatively, non-quadratic global hedging applies an asymmetric treatment to hedging errors by overly (and most often strictly) penalizing hedging losses. In contrast to global quadratic hedging, there is usually no closed-form solution to the optimal policy, but numerical implementations have been proposed in the literature: François et al., ([2014](#bib.bib24)) developed a methodology with stochastic dynamic programming algorithms for global hedging with any desired penalty function, Godin, ([2016](#bib.bib27)) adapts the latter numerical implementation under the Conditional Value-at-Risk measure in the presence of transaction costs and Dupuis et al., ([2016](#bib.bib22)) apply global hedging under the semi-mean-square error penalty
in the context of short-term hedging for an electricity retailer. The aforementioned studies demonstrated the vast superiority of non-quadratic global hedging over other hedging schemes (e.g. greek-based policies, local risk minimization and global quadratic hedging). Yet, to the best of the author’s knowledge,
both quadratic and non-quadratic global hedging has seldom
been applied for risk mitigation of segregated funds guarantees, or more generally, of long-term contingent claims.111
An exception is the work of Ankirchner et al., ([2014](#bib.bib3)) which considers a minimal-variance hedging strategy for VAs guarantees in continuous-time in the presence of basis risk.
Moreover, numerical schemes for global hedging are computationally intensive and often rely on solving Bellman’s equations which is known to be prone to the curse of dimensionality (Powell,, [2009](#bib.bib45)). In the context of dynamically hedging segregated funds guarantees, the latter is a major drawback as it restrains the number of risk factors to consider for the financial market as well as prevents the use of multiple assets in the design of hedging policies.
A feasible implementation of global hedging for the risk mitigation of VAs guarantees which is flexible to the choice of market features, to the hedging instruments and to the penalty for hedging errors would be desirable.

Recently, [Buehler et al., 2019a](#bib.bib15)  introduced a deep reinforcement learning (deep RL) algorithm called deep hedging to hedge a portfolio of over-the-counter derivatives in the presence of market frictions.
The general framework of RL is for an agent to learn over many iterations of an environment how to select sequences of actions to optimize a cost function.
RL has been applied successfully in many areas of quantitative finance such as algorithmic trading (e.g. Moody and Saffell, ([2001](#bib.bib43)) and Deng et al., ([2016](#bib.bib21))), portfolio optimization (e.g. Jiang et al., ([2017](#bib.bib36)) and Almahdi and Yang, ([2017](#bib.bib2))) and option pricing (e.g. Li et al., ([2009](#bib.bib41)), Becker et al., ([2019](#bib.bib8)) and Carbonneau and Godin, ([2020](#bib.bib17))). Hedging has also received some attention: Halperin, ([2020](#bib.bib29)) and Kolm and Ritter, ([2019](#bib.bib39)) propose TD-learning approaches to the hedging problem
and Hongkai et al., ([2020](#bib.bib35)) and Carbonneau and Godin, ([2020](#bib.bib17)) deep hedge European options under respectively the quadratic penalty and the Conditional Value-at-Risk measure.
The deep hedging algorithm trains an agent to learn how to approximate optimal hedging decisions by neural networks
through many simulations of a synthetic market. This approach is related to the deep learning method of Han and E, ([2016](#bib.bib30)) by directly optimizing policies for stochastic control problems with Monte Carlo simulations. Arguably, the most important benefit of using neural networks to approximate optimal policies is to overcome the curse of dimensionality which arises when the state-space gets too large.

The contribution of this paper is threefold. First, this study presents a deep reinforcement learning procedure for global hedging long-term financial derivatives which are analogous under assumptions made in this study to embedded options of segregated funds. Our methodological approach which relies on the deep hedging algorithm can be applied
for the risk mitigation of any long-term European-type contingent claims (e.g. vanilla, path-dependent) with multiple hedging instruments (e.g. standard options and underlying) under any desired penalty (e.g. quadratic and non-quadratic) and in the presence of different risky assets stylized features (e.g. jump, volatility and regime risk).
The second contribution consists in conducting broad numerical experiments of hedging long-term contingent claims with the optimized global policies. A similar setup as in the work of Coleman et al., ([2007](#bib.bib18)) is considered with the risk mitigation of ratchet GMMBs
strictly for financial risks in the presence of jumps for equity. To the best of the author’s knowledge, this is the first paper that presents such an extensive benchmarking of quadratic and non-quadratic global policies for long-term options with the use of various hedging instruments and by considering different risky assets dynamics. Such benchmarking would have been inaccessible when relying on more traditional optimization procedures for global hedging such as stochastic dynamic programming due to the curse of dimensionality. Numerical results demonstrate the vast superiority of non-quadratic global hedging as it results simultaneously in downside risk metrics two to three times smaller than best benchmarks and in significant hedging gains. Our results clearly demonstrate that non-quadratic global hedging should be prioritized over other popular dynamic hedging procedures found in the literature as it is tailor-made to match the financial objectives of the hedger by always significantly reducing the downside risk as well as earning large expected positive returns.
The third contribution is in providing important insights into specific characteristics of the optimized global policies. Monte Carlo experiments indicate that on average, non-quadratic global policies are significantly more bullish than their quadratic counterpart by holding a larger average equity risk exposure which entails earning the equity risk premium.
Key factors which contribute to this specific characteristic of non-quadratic global policies are identified.
Furthermore, analyses of numerical results show
that the training algorithm is able to effectively adapt hedging policies (i.e. neural networks parameters) to different stylized features of risky asset dynamics only by experiencing simulations of the financial market exhibiting these features.

The paper is structured as follows. [Section 2](#S2 "2 Hedging of long-term contingent claims ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") introduces the notation and the optimal hedging problem. [Section 3](#S3 "3 Methodology ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") describes the numerical scheme based on deep RL to optimize global hedging policies. [Section 4](#S4 "4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") presents benchmarking of the risk mitigation of GMMBs under various market settings. [Section 5](#S5 "5 Conclusion ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") concludes.

## 2   Hedging of long-term contingent claims

This section details the financial market setup and the hedging problem considered in this paper.

### 2.1   Market setup

The financial market is in discrete-time with a finite time horizon of T∈ℕ𝑇ℕT\in\mathbb{N} years and N+1𝑁1N+1 known observation dates 𝒯:={ti:ti=i​ΔN,i=0,…,N}assign𝒯conditional-setsubscript𝑡𝑖formulae-sequencesubscript𝑡𝑖𝑖subscriptΔ𝑁𝑖

0…𝑁\mathcal{T}:=\{t\_{i}:t\_{i}=i\Delta\_{N},i=0,\ldots,N\}
with ΔN:=T/NassignsubscriptΔ𝑁𝑇𝑁\Delta\_{N}:=T/N. The probability space
(Ω,ℱT,ℙ)Ωsubscriptℱ𝑇ℙ(\Omega,\mathcal{F}\_{T},\mathbb{P}) with ℙℙ\mathbb{P} as the physical measure is equipped with the filtration 𝔽:={ℱtn}n=0Nassign𝔽superscriptsubscriptsubscriptℱsubscript𝑡𝑛𝑛0𝑁\mathbb{F}:=\{\mathcal{F}\_{t\_{n}}\}\_{n=0}^{N} that defines all available information of the financial market to investors. A total of D+2𝐷2D+2 liquid assets are accessible to financial participants with D+1𝐷1D+1 risky assets and one risk-free asset. Let {Btn}n=0Nsuperscriptsubscriptsubscript𝐵subscript𝑡𝑛𝑛0𝑁\{B\_{t\_{n}}\}\_{n=0}^{N} be the price process of the risk-free asset where Btn:=er​tnassignsubscript𝐵subscript𝑡𝑛superscript𝑒𝑟subscript𝑡𝑛B\_{t\_{n}}:=e^{rt\_{n}} with r∈ℝ𝑟ℝr\in\mathbb{R} as the annualized continuous risk-free rate. The risky assets include a non-dividend paying stock and D𝐷D liquid vanilla European-type options such as calls and puts on the stock which expire on observation dates in 𝒯𝒯\mathcal{T}. In this context, the specification of two distinct price processes, one at the beginning and one at the end of each trading period, is required. Let {S¯tn(b)}n=0Nsuperscriptsubscriptsuperscriptsubscript¯𝑆subscript𝑡𝑛𝑏𝑛0𝑁\{\bar{S}\_{t\_{n}}^{(b)}\}\_{n=0}^{N} be the risky price process at the beginning of each trading period where S¯tn(b):=[Stn(0,b),…,Stn(D,b)]assignsuperscriptsubscript¯𝑆subscript𝑡𝑛𝑏

superscriptsubscript𝑆subscript𝑡𝑛0𝑏…superscriptsubscript𝑆subscript𝑡𝑛𝐷𝑏\bar{S}\_{t\_{n}}^{(b)}:=[S\_{t\_{n}}^{(0,b)},\ldots,S\_{t\_{n}}^{(D,b)}] are the prices at the beginning of [tn,tn+1)subscript𝑡𝑛subscript𝑡𝑛1[t\_{n},t\_{n+1}) with Stn(0,b)superscriptsubscript𝑆subscript𝑡𝑛0𝑏S\_{t\_{n}}^{(0,b)} and Stn(j,b)superscriptsubscript𝑆subscript𝑡𝑛𝑗𝑏S\_{t\_{n}}^{(j,b)} respectively as the price of the underlying and of the jthsuperscript𝑗thj^{\text{th}} option. Similarly, let {S¯tn(e)}n=0N−1superscriptsubscriptsuperscriptsubscript¯𝑆subscript𝑡𝑛𝑒𝑛0𝑁1\{\bar{S}\_{t\_{n}}^{(e)}\}\_{n=0}^{N-1} be the risky price process at the end of each trading period where S¯tn(e):=[Stn(0,e),…,Stn(D,e)]assignsuperscriptsubscript¯𝑆subscript𝑡𝑛𝑒

superscriptsubscript𝑆subscript𝑡𝑛0𝑒…superscriptsubscript𝑆subscript𝑡𝑛𝐷𝑒\bar{S}\_{t\_{n}}^{(e)}:=[S\_{t\_{n}}^{(0,e)},\ldots,S\_{t\_{n}}^{(D,e)}] are the prices at the end of [tn,tn+1)subscript𝑡𝑛subscript𝑡𝑛1[t\_{n},t\_{n+1}) before the next rebalancing at tn+1subscript𝑡𝑛1t\_{n+1}. For the tradable options, if the jthsuperscript𝑗thj^{\text{th}} option matures at tn+1subscript𝑡𝑛1t\_{n+1}, then Stn(j,e)superscriptsubscript𝑆subscript𝑡𝑛𝑗𝑒S\_{t\_{n}}^{(j,e)} is the payoff of the derivative and Stn+1(j,b)superscriptsubscript𝑆subscript𝑡𝑛1𝑗𝑏S\_{t\_{n+1}}^{(j,b)} is the price of a new contract with the same characteristics (i.e. same payoff function and time-to-maturity). For the underlying, the equality Stn+1(0,b)=Stn(0,e)superscriptsubscript𝑆subscript𝑡𝑛10𝑏superscriptsubscript𝑆subscript𝑡𝑛0𝑒S\_{t\_{n+1}}^{(0,b)}=S\_{t\_{n}}^{(0,e)} holds ℙℙ\mathbb{P}-a.s. for n=0,…,N−1𝑛

0…𝑁1n=0,\ldots,N-1.

This paper studies the problem of hedging long-term contingent claims embedded in segregated funds guarantees by means of dynamic hedging with a similar setup as in the work of Coleman et al., ([2007](#bib.bib18)).
While the latter paper considers the presence of both jump risk and volatility risk for the equity, the current work strictly assesses the impact of jump risk on the risk management of long-term contingent claims. We note that the methodological approach presented in [Section 3](#S3 "3 Methodology ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") for
optimizing
global policies can easily be adapted to the presence of additional risk factors for equity (e.g. volatility risk and regime risk).
For the rest of the paper, assume that mortality risk can be completely diversified away and let T𝑇T be the known maturity in years of the embedded guarantee to be hedged. This assumption can be motivated by the fact that in practice, insurance companies can significantly reduce the impact of mortality risk on their segregated funds portfolios by insuring additional policies. Furthermore, all VAs are assumed to be held until expiration (i.e. no lapse risk) and their values are linked to a liquid index such as the S&P500 which implies no basis risk.

In this study, the option embedded in VAs is a GMMB with an annual ratchet feature which provides a payoff at time T𝑇T of the maximum anniversary account value. The anniversary dates of the equity-linked insurance account are assumed to form a subset of the observation dates, i.e. {0,1,…,T}⊆𝒯01…𝑇𝒯\{0,1,\ldots,T\}\subseteq\mathcal{T}.
Let {Ztn}n=0Nsuperscriptsubscriptsubscript𝑍subscript𝑡𝑛𝑛0𝑁\{Z\_{t\_{n}}\}\_{n=0}^{N} be the running maximum anniversary value process of the equity-linked account222
⌊⋅⌋:ℝ→ℝ:⋅→ℝℝ\lfloor\cdot\rfloor:\mathbb{R}\rightarrow\mathbb{R} is the floor function, i.e. ⌊x⌋𝑥\lfloor x\rfloor is the largest integer smaller or equal to x𝑥x.
:

|  |  |  |
| --- | --- | --- |
|  | Ztn={max⁡(S0(0,b),…,Sm(0,b)),if ​⌊tn⌋=m​ and ​m∈{0,…,T−1},max⁡(S0(0,b),…,ST−1(0,b)),if ​tn=T.subscript𝑍subscript𝑡𝑛casessuperscriptsubscript𝑆00𝑏…superscriptsubscript𝑆𝑚0𝑏if subscript𝑡𝑛𝑚 and 𝑚0…𝑇1superscriptsubscript𝑆00𝑏…superscriptsubscript𝑆𝑇10𝑏if subscript𝑡𝑛𝑇Z\_{t\_{n}}=\begin{cases}\max(S\_{0}^{(0,b)},\ldots,S\_{m}^{(0,b)}),&\mbox{if }\left\lfloor t\_{n}\right\rfloor=m\mbox{ and }m\in\{0,\ldots,T-1\},\\ \max(S\_{0}^{(0,b)},\ldots,S\_{T-1}^{(0,b)}),&\mbox{if }t\_{n}=T.\\ \end{cases} |  |

The payoff of the GMMB with annual ratchet can be expressed as the account value at time T𝑇T plus a lookback put option payoff

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡(S0(0,b),…,ST(0,b))superscriptsubscript𝑆00𝑏…superscriptsubscript𝑆𝑇0𝑏\displaystyle\max(S\_{0}^{(0,b)},\ldots,S\_{T}^{(0,b)}) | =max⁡(max⁡(S0(0,b),…,ST−1(0,b)),ST(0,b))absentsuperscriptsubscript𝑆00𝑏…superscriptsubscript𝑆𝑇10𝑏superscriptsubscript𝑆𝑇0𝑏\displaystyle=\max(\max(S\_{0}^{(0,b)},\ldots,S\_{T-1}^{(0,b)}),S\_{T}^{(0,b)}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =max⁡(ZT−ST(0,b),0)+ST(0,b).absentsubscript𝑍𝑇superscriptsubscript𝑆𝑇0𝑏0superscriptsubscript𝑆𝑇0𝑏\displaystyle=\max(Z\_{T}-S\_{T}^{(0,b)},0)+S\_{T}^{(0,b)}. |  | (2.1) |

Thus, the assumptions of market completeness with respect to mortality risk and lapse risk considered in this paper entail that the risk exposure of the insurer selling a GMMB333
Coleman et al., ([2007](#bib.bib18)) consider the problem of hedging a ratchet GMDB with a fixed and known maturity T𝑇T. The use of a fixed maturity in the latter paper is motivated by assuming market completeness under mortality risk and hedging the expected loss of the guarantee. While the current paper considers the risk mitigation of a GMMB instead of a GMDB, assumptions made in both papers (i.e. no mortality risk and lapse risk) entail that the benefits of the two guarantees are equivalent and result in the same lookback put option to hedge as in ([2.2](#S2.E2 "Equation 2.2 ‣ 2.1 Market setup ‣ 2 Hedging of long-term contingent claims ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.")).
 is equivalent to holding short position in a long-term lookback option of fixed maturity T𝑇T and of payoff Φ:ℝ×ℝT→[0,∞):Φ→ℝsuperscriptℝ𝑇0\Phi:\mathbb{R}\times\mathbb{R}^{T}\rightarrow[0,\infty):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ​(ST(0,b),ZT):=max⁡(ZT−ST(0,b),0).assignΦsuperscriptsubscript𝑆𝑇0𝑏subscript𝑍𝑇subscript𝑍𝑇superscriptsubscript𝑆𝑇0𝑏0\displaystyle\Phi(S\_{T}^{(0,b)},Z\_{T}):=\max(Z\_{T}-S\_{T}^{(0,b)},0). |  | (2.2) |

Let δ:={δtn}n=0Nassign𝛿superscriptsubscriptsubscript𝛿subscript𝑡𝑛𝑛0𝑁\delta:=\{\delta\_{t\_{n}}\}\_{n=0}^{N} be a trading strategy used by the hedger to minimize his risk exposure to ΦΦ\Phi where for n=1,…,N𝑛

1…𝑁n=1,\ldots,N, δtn:=(δtn(0),…,δtn(D),δtn(B))assignsubscript𝛿subscript𝑡𝑛superscriptsubscript𝛿subscript𝑡𝑛0…superscriptsubscript𝛿subscript𝑡𝑛𝐷superscriptsubscript𝛿subscript𝑡𝑛𝐵\delta\_{t\_{n}}:=(\delta\_{t\_{n}}^{(0)},\ldots,\delta\_{t\_{n}}^{(D)},\delta\_{t\_{n}}^{(B)}) is a vector containing the number of shares held in each asset during the period (tn−1,tn]subscript𝑡𝑛1subscript𝑡𝑛(t\_{n-1},t\_{n}] with δtn(0:D):=(δtn(0),…,δtn(D))assignsuperscriptsubscript𝛿subscript𝑡𝑛:0𝐷superscriptsubscript𝛿subscript𝑡𝑛0…superscriptsubscript𝛿subscript𝑡𝑛𝐷\delta\_{t\_{n}}^{(0:D)}:=(\delta\_{t\_{n}}^{(0)},\ldots,\delta\_{t\_{n}}^{(D)}) and δtn(B)superscriptsubscript𝛿subscript𝑡𝑛𝐵\delta\_{t\_{n}}^{(B)} respectively as the positions in the D+1𝐷1D+1 risky assets and in the risk-free asset. The initial portfolio (at time 00 before the first trade) is invested strictly in the risk-free asset. Also, for convenience, all options used as hedging instruments have one period maturity, i.e. they are traded once and held until expiration.
Here is an additional assumption considered for the rest of the paper.

###### Assumption 2.1.

The market is liquid and trading in risky assets does not affect their prices.

Before describing the optimization problem of hedging ΦΦ\Phi, some well-known concepts in the mathematical finance literature must be described. The reader is referred to Lamberton and Lapeyre, ([2011](#bib.bib40)) for additional details. Let {Gtnδ}n=0Nsuperscriptsubscriptsuperscriptsubscript𝐺subscript𝑡𝑛𝛿𝑛0𝑁\{G\_{t\_{n}}^{\delta}\}\_{n=0}^{N} be the discounted gain process associated with the strategy δ𝛿\delta where Gtnδsuperscriptsubscript𝐺subscript𝑡𝑛𝛿G\_{t\_{n}}^{\delta} is the discounted gain at time tnsubscript𝑡𝑛t\_{n} prior to rebalancing. G0δ:=0assignsuperscriptsubscript𝐺0𝛿0G\_{0}^{\delta}:=0 and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gtnδ:=∑k=1nδtk(0:D)∙(Btk−1​S¯tk−1(e)−Btk−1−1​S¯tk−1(b)),n=1,2,…,N,formulae-sequenceassignsuperscriptsubscript𝐺subscript𝑡𝑛𝛿superscriptsubscript𝑘1𝑛∙superscriptsubscript𝛿subscript𝑡𝑘:0𝐷superscriptsubscript𝐵subscript𝑡𝑘1superscriptsubscript¯𝑆subscript𝑡𝑘1𝑒superscriptsubscript𝐵subscript𝑡𝑘11superscriptsubscript¯𝑆subscript𝑡𝑘1𝑏𝑛  12…𝑁\displaystyle G\_{t\_{n}}^{\delta}:=\sum\_{k=1}^{n}\delta\_{t\_{k}}^{(0:D)}\mathchoice{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\displaystyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\textstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\scriptstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\scriptscriptstyle\bullet$}}}}}(B\_{t\_{k}}^{-1}\bar{S}\_{t\_{k-1}}^{(e)}-B\_{t\_{k-1}}^{-1}\bar{S}\_{t\_{k-1}}^{(b)}),\quad n=1,2,\ldots,N, |  | (2.3) |

where ∙∙\mathchoice{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\displaystyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\textstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\scriptstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\scriptscriptstyle\bullet$}}}}} is the dot product operator.444
If X=[X1,…,XK]𝑋

subscript𝑋1…subscript𝑋𝐾X=[X\_{1},\ldots,X\_{K}] and Y=[Y1,…,YK]𝑌

subscript𝑌1…subscript𝑌𝐾Y=[Y\_{1},\ldots,Y\_{K}], X∙Y:=∑i=1KXi​Yiassign∙𝑋𝑌superscriptsubscript𝑖1𝐾subscript𝑋𝑖subscript𝑌𝑖X\mathchoice{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\displaystyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\textstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\scriptstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\scriptscriptstyle\bullet$}}}}}Y:=\sum\_{i=1}^{K}X\_{i}Y\_{i}.
 Moreover, let {Vtnδ}n=0Nsuperscriptsubscriptsuperscriptsubscript𝑉subscript𝑡𝑛𝛿𝑛0𝑁\{V\_{t\_{n}}^{\delta}\}\_{n=0}^{N} be hedging portfolio values for a trading strategy δ𝛿\delta where Vtnδsuperscriptsubscript𝑉subscript𝑡𝑛𝛿V\_{t\_{n}}^{\delta} is the value prior to rebalancing at time tnsubscript𝑡𝑛t\_{n}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtnδ:=δtn(0:D)∙S¯tn−1(e)+δtn(B)​Btn,n=1,…,N,formulae-sequenceassignsuperscriptsubscript𝑉subscript𝑡𝑛𝛿∙superscriptsubscript𝛿subscript𝑡𝑛:0𝐷superscriptsubscript¯𝑆subscript𝑡𝑛1𝑒superscriptsubscript𝛿subscript𝑡𝑛𝐵subscript𝐵subscript𝑡𝑛𝑛  1…𝑁\displaystyle V\_{t\_{n}}^{\delta}:=\delta\_{t\_{n}}^{(0:D)}\mathchoice{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\displaystyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\textstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\scriptstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\scriptscriptstyle\bullet$}}}}}\bar{S}\_{t\_{n-1}}^{(e)}+\delta\_{t\_{n}}^{(B)}B\_{t\_{n}},\quad n=1,\ldots,N, |  | (2.4) |

and V0δ:=δ0(B)assignsuperscriptsubscript𝑉0𝛿superscriptsubscript𝛿0𝐵V\_{0}^{\delta}:=\delta\_{0}^{(B)} since the initial capital amount is assumed to be strictly invested in the risk-free asset. In this paper, the trading strategies considered require no cash infusion nor withdrawal except at the initialization of the contract (i.e. at time 00). Such strategies are called self-financing. More precisely, the hedging strategy δ𝛿\delta is said to be self-financing if it is predictable555
X={Xn}n=0N𝑋superscriptsubscriptsubscript𝑋𝑛𝑛0𝑁X=\{X\_{n}\}\_{n=0}^{N} with Xn=[Xn(1),…,Xn(K)]subscript𝑋𝑛

superscriptsubscript𝑋𝑛1…superscriptsubscript𝑋𝑛𝐾X\_{n}=[X\_{n}^{(1)},\ldots,X\_{n}^{(K)}] is 𝔽𝔽\mathbb{F}-predictable if for j=1,…,K,𝑗

1…𝐾j=1,\ldots,K, X0(j)∈ℱ0superscriptsubscript𝑋0𝑗subscriptℱ0X\_{0}^{(j)}\in\mathcal{F}\_{0} and Xn+1(j)∈ℱnsuperscriptsubscript𝑋𝑛1𝑗subscriptℱ𝑛X\_{n+1}^{(j)}\in\mathcal{F}\_{n} for n=0,…,N−1𝑛

0…𝑁1n=0,\ldots,N-1.
 and if

|  |  |  |  |
| --- | --- | --- | --- |
|  | δtn+1(0:D)∙S¯tn(b)+δtn+1(B)​Btn=Vtnδ,n=0,1,…,N−1.formulae-sequence∙superscriptsubscript𝛿subscript𝑡𝑛1:0𝐷superscriptsubscript¯𝑆subscript𝑡𝑛𝑏superscriptsubscript𝛿subscript𝑡𝑛1𝐵subscript𝐵subscript𝑡𝑛superscriptsubscript𝑉subscript𝑡𝑛𝛿𝑛  01…𝑁1\displaystyle\delta\_{t\_{n+1}}^{(0:D)}\mathchoice{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\displaystyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\textstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\scriptstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\scriptscriptstyle\bullet$}}}}}\bar{S}\_{t\_{n}}^{(b)}+\delta\_{t\_{n+1}}^{(B)}B\_{t\_{n}}=V\_{t\_{n}}^{\delta},\quad n=0,1,\ldots,N-1. |  | (2.5) |

Lastly, let ΠΠ\Pi be the set of admissible trading strategies for the hedger which consists of all sufficiently well-behaved self-financing strategies.

###### Remark 2.1.

It can be shown that δ𝛿\delta is self-financing if and only if Vtnδ=Btn​(V0δ+Gtnδ)superscriptsubscript𝑉subscript𝑡𝑛𝛿subscript𝐵subscript𝑡𝑛superscriptsubscript𝑉0𝛿superscriptsubscript𝐺subscript𝑡𝑛𝛿V\_{t\_{n}}^{\delta}=B\_{t\_{n}}(V\_{0}^{\delta}+G\_{t\_{n}}^{\delta}) for n=0,1,…,N.𝑛

01…𝑁n=0,1,\ldots,N. See for instance Lamberton and Lapeyre, ([2011](#bib.bib40)).

### 2.2   Optimal hedging problem

The optimization problem of hedging the risk exposure associated to a short position in the long-term lookback option is now formally defined. For the hedger, the problem consists in the design of a trading policy which minimizes a penalty, also referred to as a loss function, of the difference between the payoff of the lookback option and the hedging portfolio value at maturity (i.e. the hedging error or hedging shortfall). Strategies embedded in such policies are called global hedging strategies as they are jointly optimized over all hedging decisions until the maturity of the lookback option.
Let ℒ:ℝ→ℝ:ℒ→ℝℝ\mathcal{L}:\mathbb{R}\rightarrow\mathbb{R} be a loss function for the hedging error. For the rest of the paper, assume without loss of generality that the position in the hedging portfolio is long, and that all assets and penalties are well-behaved and integrable enough. Specific conditions are beyond the scope of this study.

###### Definition 2.1.

(Global risk exposure)
Define ϵ​(V0)italic-ϵsubscript𝑉0\epsilon(V\_{0}) as the global risk exposure of the short position in ΦΦ\Phi under optimal hedge if the value of the initial hedging portfolio is V0∈ℝsubscript𝑉0ℝV\_{0}\in\mathbb{R}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ϵ​(V0)italic-ϵsubscript𝑉0\displaystyle\epsilon(V\_{0}) | :=minδ∈Π​𝔼​[ℒ​(Φ​(ST(0,b),ZT)−VTδ)],assignabsent𝛿Π𝔼delimited-[]ℒΦsuperscriptsubscript𝑆𝑇0𝑏subscript𝑍𝑇superscriptsubscript𝑉𝑇𝛿\displaystyle:=\underset{\delta\in\Pi}{\min}\,\mathbb{E}\left[\mathcal{L}\left(\Phi(S\_{T}^{(0,b)},Z\_{T})-V\_{T}^{\delta}\right)\right], |  | (2.6) |

where the expectation is taken with respect to the physical measure.

###### Remark 2.2.

An assumption implicit to [2.1](#S2.ThmDef1 "Definition 2.1. ‣ 2.2 Optimal hedging problem ‣ 2 Hedging of long-term contingent claims ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") is that the minimum ([2.6](#S2.E6 "Equation 2.6 ‣ Definition 2.1. ‣ 2.2 Optimal hedging problem ‣ 2 Hedging of long-term contingent claims ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.")) is indeed attained by some trading strategy, i.e. that the infimum is in fact a minimum. The identification of conditions which ensure that this assumption is satisfied are left out-of-scope.

The following defines the optimal hedging strategy for ΦΦ\Phi given the initial capital investment and the loss function for hedging errors.

###### Definition 2.2.

(Optimal hedging strategy)
Let δ⋆​(V0)superscript𝛿⋆subscript𝑉0\delta^{\star}(V\_{0}) be the optimal hedging strategy corresponding to the global risk exposure of the hedger if the initial portfolio value is V0∈ℝsubscript𝑉0ℝV\_{0}\in\mathbb{R}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | δ⋆​(V0)superscript𝛿⋆subscript𝑉0\displaystyle\delta^{\star}(V\_{0}) | :=arg​minδ∈Π​𝔼​[ℒ​(Φ​(ST(0,b),ZT)−VTδ)].assignabsent𝛿Πargmin𝔼delimited-[]ℒΦsuperscriptsubscript𝑆𝑇0𝑏subscript𝑍𝑇superscriptsubscript𝑉𝑇𝛿\displaystyle:=\underset{\delta\in\Pi}{\operatorname\*{arg\,min}}\,\mathbb{E}\left[\mathcal{L}\left(\Phi(S\_{T}^{(0,b)},Z\_{T})-V\_{T}^{\delta}\right)\right]. |  | (2.7) |

In a realistic setting, the choice of loss function should reflect the financial objectives and the risk aversion of the hedger. One example of penalty which has been extensively studied in the hedging literature is the mean-square error (MSE): ℒ​(x)=x2ℒ𝑥superscript𝑥2\mathcal{L}(x)=x^{2}. This penalty entails that hedging gains and losses are treated equally which could be desirable for a financial participant who has to provide a price quote on a security prior to knowing his position (long or short). In the context of this paper where the position in ΦΦ\Phi is always short, penalizing hedging gains is clearly undesirable for the hedger. The corresponding loss function to the MSE that penalizes only hedging losses is the semi-mean-square error (SMSE): ℒ​(x)=x2​𝟙{x>0}ℒ𝑥superscript𝑥2subscript1𝑥0\mathcal{L}(x)=x^{2}\mathds{1}\_{\{x>0\}}.
While the MSE and SMSE are the only penalties considered in numerical experiments of [Section 4](#S4 "4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions."), the optimization procedure for global hedging policies presented in [Section 3](#S3 "3 Methodology ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") is flexible to any well-behaved penalties (see e.g. Carbonneau and Godin, ([2020](#bib.bib17)) for an implementation with the Conditional Value-at-Risk measure).

The author wants to emphasize that different penalties will often result in different optimal hedging strategies. An extensive numerical study of the impact of the choice of loss function on the hedging policy for the risk management of lookback options is done in [Section 4](#S4 "4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions."). Moreover, while the numerical section of this paper strictly studies a specific example of long-term option to hedge, namely the lookback option of payoff ΦΦ\Phi, the methodological approach to approximate optimal hedging strategies can be applied for any European-type derivative of well-behaved payoff function which can naturally include other VAs guarantees with payoffs analogous to financial derivatives.

## 3   Methodology

This section describes the reinforcement learning procedure used to optimize global policies.
The approach relies on the deep hedging algorithm of [Buehler et al., 2019a](#bib.bib15)  who showed that a feedforward neural network (FFNN) can be used to approximate arbitrarily well optimal hedging strategies in very general financial market conditions. At its core, a FFNN is a parameterized composite function which maps input to output vectors through the composition of a sequence of functions called hidden layers.
Each hidden layer applies an affine transformation and a nonlinear transformation to input vectors.
A FFNN Fθ:ℝd0→ℝd~:subscript𝐹𝜃→superscriptℝsubscript𝑑0superscriptℝ~𝑑F\_{\theta}:\mathbb{R}^{d\_{0}}\rightarrow\mathbb{R}^{\tilde{d}} with L𝐿L hidden layers has the following representation:

|  |  |  |
| --- | --- | --- |
|  | Fθ​(X):=o∘hL∘…∘h1,assignsubscript𝐹𝜃𝑋𝑜subscriptℎ𝐿…subscriptℎ1F\_{\theta}(X):=o\circ h\_{L}\circ\ldots\circ h\_{1}, |  |

|  |  |  |
| --- | --- | --- |
|  | hl​(X):=g​(Wl​X+bl),l=1,…,L,formulae-sequenceassignsubscriptℎ𝑙𝑋𝑔subscript𝑊𝑙𝑋subscript𝑏𝑙𝑙  1…𝐿h\_{l}(X):=g(W\_{l}X+b\_{l}),\quad l=1,\ldots,L, |  |

where Wl∈ℝdl×dl−1subscript𝑊𝑙superscriptℝsubscript𝑑𝑙subscript𝑑𝑙1W\_{l}\in\mathbb{R}^{d\_{l}\times d\_{l-1}} and bl∈ℝdl×1subscript𝑏𝑙superscriptℝsubscript𝑑𝑙1b\_{l}\in\mathbb{R}^{d\_{l}\times 1} are respectively known as the weight matrix and bias vector of the lthsuperscript𝑙thl^{\text{th}} hidden layer hlsubscriptℎ𝑙h\_{l}, g𝑔g is a non-linear function applied to each scalar given as input and o:ℝdL→ℝd~:𝑜→superscriptℝsubscript𝑑𝐿superscriptℝ~𝑑o:\mathbb{R}^{d\_{L}}\rightarrow\mathbb{R}^{\tilde{d}} is the output function which applies an affine transformation to the output of the last hidden layer hLsubscriptℎ𝐿h\_{L} and possibly also a nonlinear transformation with the same range as Fθsubscript𝐹𝜃F\_{\theta}. Furthermore, the trainable parameters θ𝜃\theta is the set of all weight matrices and bias vectors which are learned (i.e. fitted in statistical terms) by minimizing a specified cost function.

In the current study, the type of neural network considered for functions representing hedging policies is from the family of recurrent neural networks (RNNs, Rumelhart et al., ([1986](#bib.bib48))), a class of neural networks which maps input sequences to output sequences. The architecture of RNNs is similar to FFNNs but differs by having self-connections in hidden layers: each hidden layer is a function of both an input vector from the current time-step and an output vector from the hidden layer of the previous time-step, hence the name recurrent.
More formally, for an input vector Xtnsubscript𝑋subscript𝑡𝑛X\_{t\_{n}} at time tnsubscript𝑡𝑛t\_{n}, the time-tnsubscript𝑡𝑛t\_{n} output of the hidden layer is computed as htn=f​(htn−1,Xtn)subscriptℎsubscript𝑡𝑛𝑓subscriptℎsubscript𝑡𝑛1subscript𝑋subscript𝑡𝑛h\_{t\_{n}}=f(h\_{t\_{n-1}},X\_{t\_{n}}) for some time-independent function f𝑓f.666
Here, htn−1subscriptℎsubscript𝑡𝑛1h\_{t\_{n-1}} and htnsubscriptℎsubscript𝑡𝑛h\_{t\_{n}} are to be understood for convenience as output vectors from hidden layers and not as mappings.
In contrast to FFNNs, feedback loops in hidden layers entail that each output is dependent of past inputs which makes RNNs more appropriate for time-series modeling.
The type of RNN considered for dynamic hedging in this study is the long short-term memory (LSTM) introduced by Hochreiter and Schmidhuber, ([1997](#bib.bib34)). This choice of neural network is motivated by recent results of [Buehler et al., 2019b](#bib.bib16)  who showed that LSTMs hedging policies
are more effective for the risk mitigation of path-dependent contingent claims than FFNNs policies.
Additional remarks are made in subsequent sections to motivate the choice of an LSTM for the specific setup considered in the current paper. For more general information about RNNs, the reader is referred to Chapter 101010 of Goodfellow et al., ([2016](#bib.bib28)) and the many references therein.

The LSTM architecture is now formally defined. The application of LSTMs as functions representing global hedging policies is described in [Section 3.1](#S3.SS1 "3.1 Hedging with an LSTM ‣ 3 Methodology ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.").
In what follows, the time-steps are the same as the observation dates of the financial market.

###### Definition 3.1.

(LSTM)
Let Fθ:ℝN×ℝdin→ℝN×ℝdout:subscript𝐹𝜃→superscriptℝ𝑁superscriptℝsubscript𝑑insuperscriptℝ𝑁superscriptℝsubscript𝑑outF\_{\theta}:\mathbb{R}^{N}\times\mathbb{R}^{d\_{\text{in}}}\rightarrow\mathbb{R}^{N}\times\mathbb{R}^{d\_{\text{out}}} be an LSTM which maps the sequence of feature vectors {Xtn}n=0N−1superscriptsubscriptsubscript𝑋subscript𝑡𝑛𝑛0𝑁1\{X\_{t\_{n}}\}\_{n=0}^{N-1} to {Ytn}n=0N−1superscriptsubscriptsubscript𝑌subscript𝑡𝑛𝑛0𝑁1\{Y\_{t\_{n}}\}\_{n=0}^{N-1} where Xtnsubscript𝑋subscript𝑡𝑛X\_{t\_{n}} and Ytnsubscript𝑌subscript𝑡𝑛Y\_{t\_{n}} are respectively two vectors of dimensions din,dout∈ℕ

subscript𝑑insubscript𝑑out
ℕd\_{\text{in}},d\_{\text{out}}\in\mathbb{N}. Let sigm​(⋅)sigm⋅\text{sigm}(\cdot) and tanh​(⋅)tanh⋅\text{tanh}(\cdot) be the sigmoid and hyperbolic tangent functions applied element-wise to each scalar given as input.777
For X:=[X1,…,XK]assign𝑋

subscript𝑋1…subscript𝑋𝐾X:=[X\_{1},\ldots,X\_{K}], sigm​(X):=[11+e−X1,…,11+e−XK]assignsigm𝑋

11superscript𝑒subscript𝑋1…11superscript𝑒subscript𝑋𝐾\text{sigm}(X):=\left[\frac{1}{1+e^{-X\_{1}}},\ldots,\frac{1}{1+e^{-X\_{K}}}\right] and tanh​(X):=[eX1−e−X1eX1+e−X1,…,eXK−e−XKeXK+e−XK]assigntanh𝑋

superscript𝑒subscript𝑋1superscript𝑒subscript𝑋1superscript𝑒subscript𝑋1superscript𝑒subscript𝑋1…superscript𝑒subscript𝑋𝐾superscript𝑒subscript𝑋𝐾superscript𝑒subscript𝑋𝐾superscript𝑒subscript𝑋𝐾\text{tanh}(X):=\left[\frac{e^{X\_{1}}-e^{-X\_{1}}}{e^{X\_{1}}+e^{-X\_{1}}},\ldots,\frac{e^{X\_{K}}-e^{-X\_{K}}}{e^{X\_{K}}+e^{-X\_{K}}}\right].
 For H∈ℕ𝐻ℕH\in\mathbb{N}, the computation of Fθsubscript𝐹𝜃F\_{\theta} at each time-step consists of H𝐻H LSTM cells which are analogous to but more complex than RNNs hidden layers. Each LSTM cell outputs a vector of djsubscript𝑑𝑗d\_{j} neurons denoted as htn(j)∈ℝdj×1superscriptsubscriptℎsubscript𝑡𝑛𝑗superscriptℝsubscript𝑑𝑗1h\_{t\_{n}}^{(j)}\in\mathbb{R}^{d\_{j}\times 1} at time tnsubscript𝑡𝑛t\_{n} for dj∈ℕsubscript𝑑𝑗ℕd\_{j}\in\mathbb{N} and j=1,…,H𝑗

1…𝐻j=1,\ldots,H.
More precisely, the computation done by the jthsuperscript𝑗thj^{\text{th}} LSTM cell at time tnsubscript𝑡𝑛t\_{n} is as follows888
At time 00 (i.e. n=0𝑛0n=0), the computation of the H𝐻H LSTM cells is the same as in ([3.1](#S3.E1 "Equation 3.1 ‣ Definition 3.1. ‣ 3 Methodology ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.")) with ht−1(j)superscriptsubscriptℎsubscript𝑡1𝑗h\_{t\_{-1}}^{(j)} and ct−1(j)superscriptsubscript𝑐subscript𝑡1𝑗c\_{t\_{-1}}^{(j)} as vectors of zeros of dimensions djsubscript𝑑𝑗d\_{j} for j=1,…,H𝑗

1…𝐻j=1,\ldots,H.
:

|  |  |  |  |
| --- | --- | --- | --- |
|  | itn(j)superscriptsubscript𝑖subscript𝑡𝑛𝑗\displaystyle i\_{t\_{n}}^{(j)} | =sigm​(Wi(j)​[htn−1(j),htn(j−1)]+bi(j)),absentsigmsuperscriptsubscript𝑊𝑖𝑗superscriptsubscriptℎsubscript𝑡𝑛1𝑗superscriptsubscriptℎsubscript𝑡𝑛𝑗1superscriptsubscript𝑏𝑖𝑗\displaystyle=\text{sigm}(W\_{i}^{(j)}[h\_{t\_{n-1}}^{(j)},h\_{t\_{n}}^{(j-1)}]+b\_{i}^{(j)}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ftn(j)superscriptsubscript𝑓subscript𝑡𝑛𝑗\displaystyle f\_{t\_{n}}^{(j)} | =sigm​(Wf(j)​[htn−1(j),htn(j−1)]+bf(j)),absentsigmsuperscriptsubscript𝑊𝑓𝑗superscriptsubscriptℎsubscript𝑡𝑛1𝑗superscriptsubscriptℎsubscript𝑡𝑛𝑗1superscriptsubscript𝑏𝑓𝑗\displaystyle=\text{sigm}(W\_{f}^{(j)}[h\_{t\_{n-1}}^{(j)},h\_{t\_{n}}^{(j-1)}]+b\_{f}^{(j)}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | otn(j)superscriptsubscript𝑜subscript𝑡𝑛𝑗\displaystyle o\_{t\_{n}}^{(j)} | =sigm​(Wo(j)​[htn−1(j),htn(j−1)]+bo(j)),absentsigmsuperscriptsubscript𝑊𝑜𝑗superscriptsubscriptℎsubscript𝑡𝑛1𝑗superscriptsubscriptℎsubscript𝑡𝑛𝑗1superscriptsubscript𝑏𝑜𝑗\displaystyle=\text{sigm}(W\_{o}^{(j)}[h\_{t\_{n-1}}^{(j)},h\_{t\_{n}}^{(j-1)}]+b\_{o}^{(j)}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ctn(j)superscriptsubscript𝑐subscript𝑡𝑛𝑗\displaystyle c\_{t\_{n}}^{(j)} | =ftn(j)∘ctn−1(j)+itn(j)∘tanh​(Wc(j)​[htn−1(j),htn(j−1)]+bc(j)),absentsuperscriptsubscript𝑓subscript𝑡𝑛𝑗superscriptsubscript𝑐subscript𝑡𝑛1𝑗superscriptsubscript𝑖subscript𝑡𝑛𝑗tanhsuperscriptsubscript𝑊𝑐𝑗superscriptsubscriptℎsubscript𝑡𝑛1𝑗superscriptsubscriptℎsubscript𝑡𝑛𝑗1superscriptsubscript𝑏𝑐𝑗\displaystyle=f\_{t\_{n}}^{(j)}\circ c\_{t\_{n-1}}^{(j)}+i\_{t\_{n}}^{(j)}\circ\text{tanh}(W\_{c}^{(j)}[h\_{t\_{n-1}}^{(j)},h\_{t\_{n}}^{(j-1)}]+b\_{c}^{(j)}), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | htn(j)superscriptsubscriptℎsubscript𝑡𝑛𝑗\displaystyle h\_{t\_{n}}^{(j)} | =otn(j)∘tanh​(ctn(j)),absentsuperscriptsubscript𝑜subscript𝑡𝑛𝑗tanhsuperscriptsubscript𝑐subscript𝑡𝑛𝑗\displaystyle=o\_{t\_{n}}^{(j)}\circ\text{tanh}(c\_{t\_{n}}^{(j)}), |  | (3.1) |

where [⋅,⋅]⋅⋅[\cdot\,,\cdot] and ∘\circ denote respectively the concatenation of two vectors and the Hadamard product (i.e. the element-wise product) and

* •

  Wi(1),Wf(1),Wo(1),Wc(1)∈ℝd1×(d1+din)
  superscriptsubscript𝑊𝑖1superscriptsubscript𝑊𝑓1superscriptsubscript𝑊𝑜1superscriptsubscript𝑊𝑐1superscriptℝsubscript𝑑1subscript𝑑1subscript𝑑inW\_{i}^{(1)},W\_{f}^{(1)},W\_{o}^{(1)},W\_{c}^{(1)}\in\mathbb{R}^{d\_{1}\times(d\_{1}+d\_{\text{in}})} and bi(1),bf(1),bo(1),bc(1)∈ℝd1×1
  superscriptsubscript𝑏𝑖1superscriptsubscript𝑏𝑓1superscriptsubscript𝑏𝑜1superscriptsubscript𝑏𝑐1superscriptℝsubscript𝑑11b\_{i}^{(1)},b\_{f}^{(1)},b\_{o}^{(1)},b\_{c}^{(1)}\in\mathbb{R}^{d\_{1}\times 1}.
* •

  If H≥2𝐻2H\geq 2: Wi(j),Wf(j),Wo(j),Wc(j)∈ℝdj×(dj+dj−1)
  superscriptsubscript𝑊𝑖𝑗superscriptsubscript𝑊𝑓𝑗superscriptsubscript𝑊𝑜𝑗superscriptsubscript𝑊𝑐𝑗superscriptℝsubscript𝑑𝑗subscript𝑑𝑗subscript𝑑𝑗1W\_{i}^{(j)},W\_{f}^{(j)},W\_{o}^{(j)},W\_{c}^{(j)}\in\mathbb{R}^{d\_{j}\times(d\_{j}+d\_{j-1})} and bi(j),bf(j),bo(j),bc(j)∈ℝdj×1
  superscriptsubscript𝑏𝑖𝑗superscriptsubscript𝑏𝑓𝑗superscriptsubscript𝑏𝑜𝑗superscriptsubscript𝑏𝑐𝑗superscriptℝsubscript𝑑𝑗1b\_{i}^{(j)},b\_{f}^{(j)},b\_{o}^{(j)},b\_{c}^{(j)}\in\mathbb{R}^{d\_{j}\times 1} for j=2,…,H𝑗
  2…𝐻j=2,\ldots,H.

At each time-step, the input of the first LSTM cell is the feature vector (i.e. htn(0):=Xtnassignsuperscriptsubscriptℎsubscript𝑡𝑛0subscript𝑋subscript𝑡𝑛h\_{t\_{n}}^{(0)}:=X\_{t\_{n}}) and the final output is an affine transformation of the output of the last LSTM cell:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ytn=Wy​htn(H)+by,n=0,…,N−1,formulae-sequencesubscript𝑌subscript𝑡𝑛subscript𝑊𝑦superscriptsubscriptℎsubscript𝑡𝑛𝐻subscript𝑏𝑦𝑛  0…𝑁1\displaystyle Y\_{t\_{n}}=W\_{y}h\_{t\_{n}}^{(H)}+b\_{y},\quad n=0,\ldots,N-1, |  | (3.2) |

where Wy∈ℝdo​u​t×dHsubscript𝑊𝑦superscriptℝsubscript𝑑𝑜𝑢𝑡subscript𝑑𝐻W\_{y}\in\mathbb{R}^{d\_{out}\times d\_{H}} and by∈ℝdo​u​t×1subscript𝑏𝑦superscriptℝsubscript𝑑𝑜𝑢𝑡1b\_{y}\in\mathbb{R}^{d\_{out}\times 1}.
Lastly, the set of trainable parameters denoted as θ𝜃\theta consists of all weight matrices and bias vectors:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ:={{Wi(j),Wf(j),Wo(j),Wc(j),bi(j),bf(j),bo(j),bc(j)}j=1H,Wy,by}.assign𝜃superscriptsubscriptsuperscriptsubscript𝑊𝑖𝑗superscriptsubscript𝑊𝑓𝑗superscriptsubscript𝑊𝑜𝑗superscriptsubscript𝑊𝑐𝑗superscriptsubscript𝑏𝑖𝑗superscriptsubscript𝑏𝑓𝑗superscriptsubscript𝑏𝑜𝑗superscriptsubscript𝑏𝑐𝑗𝑗1𝐻subscript𝑊𝑦subscript𝑏𝑦\displaystyle\theta:=\left\{\{W\_{i}^{(j)},W\_{f}^{(j)},W\_{o}^{(j)},W\_{c}^{(j)},b\_{i}^{(j)},b\_{f}^{(j)},b\_{o}^{(j)},b\_{c}^{(j)}\}\_{j=1}^{H},W\_{y},b\_{y}\right\}. |  | (3.3) |

###### Remark 3.1.

In the deep learning literature, the itn(j)superscriptsubscript𝑖subscript𝑡𝑛𝑗i\_{t\_{n}}^{(j)}, ftn(j)superscriptsubscript𝑓subscript𝑡𝑛𝑗f\_{t\_{n}}^{(j)} and otn(j)superscriptsubscript𝑜subscript𝑡𝑛𝑗o\_{t\_{n}}^{(j)} are known as input gates, forget gates and output gates. Their architectures have shown to help to alleviate the issue of learning long-term dependencies of time series with classical RNNs as they control the information passed through the LSTM cells. The reader is referred to Bengio et al., ([1994](#bib.bib9)) for more information about this latter pitfall of RNNs and to Chapter 10.1010.1010.10 of Goodfellow et al., ([2016](#bib.bib28)) and the many references therein for more general information about LSTMs.

### 3.1   Hedging with an LSTM

In the context of dynamic hedging, an LSTM maps a sequence of feature vectors consisting of relevant financial market observations to the sequence of positions in each asset for all time-steps. The trainable parameters θ𝜃\theta are optimized to minimize the expected value of a loss function applied to the terminal hedging error
obtained as a result of the trading decisions made by the LSTM. The following definition describes more formally how the LSTM computes the hedging strategy. Note that in the numerical experiments of [Section 4](#S4 "4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions."), the hedging instruments used for the risk minimization of ΦΦ\Phi are either only the underlying or standard options. The case of using both the underlying and options is not considered because of its redundancy; the options can replicate positions in the underlying with calls and puts.

###### Definition 3.2.

(Hedging with an LSTM)
Let Fθsubscript𝐹𝜃F\_{\theta} be an LSTM as in [3.1](#S3.ThmDef1 "Definition 3.1. ‣ 3 Methodology ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") which maps the sequence of feature vectors {Xtn}n=0N−1superscriptsubscriptsubscript𝑋subscript𝑡𝑛𝑛0𝑁1\{X\_{t\_{n}}\}\_{n=0}^{N-1} to the output vectors {Ytn}n=0N−1superscriptsubscriptsubscript𝑌subscript𝑡𝑛𝑛0𝑁1\{Y\_{t\_{n}}\}\_{n=0}^{N-1}. The choice of hedging instruments (i.e. the underlying or standard options) implies differences for the feature vectors and output vectors999
The computation of {Vtnδ}n=0N−1superscriptsubscriptsuperscriptsubscript𝑉subscript𝑡𝑛𝛿𝑛0𝑁1\{V\_{t\_{n}}^{\delta}\}\_{n=0}^{N-1} can be done for instance as in ([2.4](#S2.E4 "Equation 2.4 ‣ 2.1 Market setup ‣ 2 Hedging of long-term contingent claims ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.")) where asset positions are given by the output vectors of the LSTM.
:

* 1)

  Hedging only with the underlying: the feature vector at each time-step is101010
  Using the transformations
  {log⁡(Stn(0,b)),log⁡(Ztn),Vtnδ/V0δ}superscriptsubscript𝑆subscript𝑡𝑛0𝑏subscript𝑍subscript𝑡𝑛superscriptsubscript𝑉subscript𝑡𝑛𝛿superscriptsubscript𝑉0𝛿\{\log(S\_{t\_{n}}^{(0,b)}),\log(Z\_{t\_{n}}),V\_{t\_{n}}^{\delta}/V\_{0}^{\delta}\}
  instead of {Stn(0,b),Ztn,Vtnδ}superscriptsubscript𝑆subscript𝑡𝑛0𝑏subscript𝑍subscript𝑡𝑛superscriptsubscript𝑉subscript𝑡𝑛𝛿\{S\_{t\_{n}}^{(0,b)},Z\_{t\_{n}},V\_{t\_{n}}^{\delta}\} in feature vectors for the numerical experiments of [Section 4](#S4 "4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") was found to significantly improve the training of neural networks. We note that the log\log transformation could not be applied for the hedging portfolio values since Vtnδsuperscriptsubscript𝑉subscript𝑡𝑛𝛿V\_{t\_{n}}^{\delta} can theoretically take values on the real line.

  |  |  |  |
  | --- | --- | --- |
  |  | Xtn:=[log⁡(Stn(0,b)),log⁡(Ztn),Vtnδ/V0δ],n=0,…,N−1,formulae-sequenceassignsubscript𝑋subscript𝑡𝑛 superscriptsubscript𝑆subscript𝑡𝑛0𝑏subscript𝑍subscript𝑡𝑛superscriptsubscript𝑉subscript𝑡𝑛𝛿superscriptsubscript𝑉0𝛿𝑛 0…𝑁1X\_{t\_{n}}:=[\log(S\_{t\_{n}}^{(0,b)}),\log(Z\_{t\_{n}}),V\_{t\_{n}}^{\delta}/V\_{0}^{\delta}],\quad n=0,\ldots,N-1, |  |

  and Fθsubscript𝐹𝜃F\_{\theta} outputs at each rebalancing date the position in the underlying: δtn(0)=Ytn−1superscriptsubscript𝛿subscript𝑡𝑛0subscript𝑌subscript𝑡𝑛1\delta\_{t\_{n}}^{(0)}=Y\_{t\_{n-1}}.
* 2)

  Hedging only with options: the feature vector at each time-step includes option prices as well as the price of the underlying:

  |  |  |  |
  | --- | --- | --- |
  |  | Xtn:=[log⁡(S¯tn(b)),log⁡(Ztn),Vtnδ/V0δ],n=0,…,N−1,formulae-sequenceassignsubscript𝑋subscript𝑡𝑛 superscriptsubscript¯𝑆subscript𝑡𝑛𝑏subscript𝑍subscript𝑡𝑛superscriptsubscript𝑉subscript𝑡𝑛𝛿superscriptsubscript𝑉0𝛿𝑛 0…𝑁1X\_{t\_{n}}:=[\log(\bar{S}\_{t\_{n}}^{(b)}),\log(Z\_{t\_{n}}),V\_{t\_{n}}^{\delta}/V\_{0}^{\delta}],\quad n=0,\ldots,N-1, |  |

  and Fθsubscript𝐹𝜃F\_{\theta} outputs at each rebalancing date the position in the D𝐷D options: [δtn(1),…,δtn(D)]=Ytn−1
  superscriptsubscript𝛿subscript𝑡𝑛1…superscriptsubscript𝛿subscript𝑡𝑛𝐷subscript𝑌subscript𝑡𝑛1[\delta\_{t\_{n}}^{(1)},\ldots,\delta\_{t\_{n}}^{(D)}]=Y\_{t\_{n-1}}.

It is important to note that the choice of dynamics for the financial market could imply that relevant necessary information to compute the time-tnsubscript𝑡𝑛t\_{n} trading strategy should be added to feature vectors. For instance, Carbonneau and Godin, ([2020](#bib.bib17)) apply the deep hedging algorithm with GARCH models which entails adding the volatility process to feature vectors. In the current paper, the models considered for the underlying imply that {Stn(0,b)}n=0Nsuperscriptsubscriptsuperscriptsubscript𝑆subscript𝑡𝑛0𝑏𝑛0𝑁\{S\_{t\_{n}}^{(0,b)}\}\_{n=0}^{N} is a Markov process under ℙℙ\mathbb{P} and thus that no additional variables must be added to feature vectors. Nevertheless, we note that the same methodological approach for hedging described in this section can easily be adapted to dynamics requiring the inclusion of additional state variables.

###### Remark 3.2.

[Buehler et al., 2019b](#bib.bib16)  deep hedge exotic derivatives with an LSTM with feature vectors that does not
include a path-dependent state variable such as {Ztn}n=0N−1superscriptsubscriptsubscript𝑍subscript𝑡𝑛𝑛0𝑁1\{Z\_{t\_{n}}\}\_{n=0}^{N-1}.
The author of the current paper observed that adding {Ztn}n=0N−1superscriptsubscriptsubscript𝑍subscript𝑡𝑛𝑛0𝑁1\{Z\_{t\_{n}}\}\_{n=0}^{N-1} to feature vectors as per [3.2](#S3.ThmDef2 "Definition 3.2. ‣ 3.1 Hedging with an LSTM ‣ 3 Methodology ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") significantly improved the performance of the optimized hedging policies when the number of trading period was large (i.e. for large N𝑁N), while for less frequent trading, the gain was marginal.

###### Remark 3.3.

Theoretical results from [Buehler et al., 2019a](#bib.bib15)  show that a FFNN
could have been used to approximate arbitrarily well the optimal hedging policy in the setup considered in this study (see Proposition 4.3 of their paper). However, the author of the current paper observed that hedging with an LSTM was significantly more effective than with a FFNN for the numerical experiments conducted in [Section 4](#S4 "4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") in terms of both computational time (i.e. faster learning with LSTMs) and hedging effectiveness which motivated the use of LSTMs as trading policies. The justifications of the superiority of LSTMs over FFNNs in the context of this paper are out-of-scope and are left out as interesting potential future work.

For the rest of the paper, a single set of hyperparameters for the LSTM is considered in terms of the number of LSTM cells and neurons per cell.111111
Note that as per [3.2](#S3.ThmDef2 "Definition 3.2. ‣ 3.1 Hedging with an LSTM ‣ 3 Methodology ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions."), the dimensions of the input and output of the LSTM at each time-step, i.e. dinsubscript𝑑ind\_{\text{in}} and doutsubscript𝑑outd\_{\text{out}}, are dependent of the choice of hedging instruments. Thus, while the number of neurons d1,…,dH

subscript𝑑1…subscript𝑑𝐻d\_{1},\ldots,d\_{H} and the number of LSTM cells H𝐻H is fixed for the numerical experiments of [Section 4](#S4 "4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions."), the total number of trainable parameters will vary with respect to the choice of hedging instruments.
 The optimization problem thus consists in searching for the optimal values of trainable parameters for this specific architecture of LSTM. The hyperparameter tuning step is not considered in this paper; the reader is referred to [Buehler et al., 2019a](#bib.bib15)  or Carbonneau and Godin, ([2020](#bib.bib17)) for a complete description of the optimal hedging problem with FFNNs which includes hyperparameter tuning.

###### Definition 3.3.

(Global risk exposure with an LSTM)
Define ϵ~​(V0)~italic-ϵsubscript𝑉0\tilde{\epsilon}(V\_{0}) as the global risk exposure of the short position in ΦΦ\Phi under optimal hedge if the hedging strategy is given by Fθsubscript𝐹𝜃F\_{\theta} and if the value of the initial hedging portfolio is V0∈ℝsubscript𝑉0ℝV\_{0}\in\mathbb{R}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ϵ~​(V0)~italic-ϵsubscript𝑉0\displaystyle\tilde{\epsilon}(V\_{0}) | :=minθ∈ℝq​𝔼​[ℒ​(Φ​(ST(0,b),ZT)−VTδθ)],assignabsent𝜃superscriptℝ𝑞𝔼delimited-[]ℒΦsuperscriptsubscript𝑆𝑇0𝑏subscript𝑍𝑇superscriptsubscript𝑉𝑇superscript𝛿𝜃\displaystyle:=\underset{\theta\in\mathbb{R}^{q}}{\min}\,\mathbb{E}\left[\mathcal{L}\left(\Phi(S\_{T}^{(0,b)},Z\_{T})-V\_{T}^{\delta^{\theta}}\right)\right], |  | (3.4) |

where δθsuperscript𝛿𝜃\delta^{\theta} is to be understood as the output vectors of Fθsubscript𝐹𝜃F\_{\theta} and q∈ℕ𝑞ℕq\in\mathbb{N} is the total number of trainable parameters.

### 3.2   Training of neural networks

The numerical scheme to optimize the trainable parameters θ𝜃\theta is now described. For convenience, a similar notation as in the work of Carbonneau and Godin, ([2020](#bib.bib17)) is used. For a given loss function and an initial portfolio value, the objective is to find θ𝜃\theta such that the risk exposure of a short position in ΦΦ\Phi is minimized (i.e. as in ([3.4](#S3.E4 "Equation 3.4 ‣ Definition 3.3. ‣ 3.1 Hedging with an LSTM ‣ 3 Methodology ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions."))). The training procedure was originally proposed in [Buehler et al., 2019a](#bib.bib15)  and relies on (mini-batch) stochastic gradient descent (SGD), a very popular algorithm in the deep learning literature to train neural networks. Denote J​(θ)𝐽𝜃J(\theta) as the cost function to minimize:

|  |  |  |
| --- | --- | --- |
|  | J​(θ):=𝔼​[ℒ​(Φ​(ST(0,b),ZT)−VTδθ)],θ∈ℝq.formulae-sequenceassign𝐽𝜃𝔼delimited-[]ℒΦsuperscriptsubscript𝑆𝑇0𝑏subscript𝑍𝑇superscriptsubscript𝑉𝑇superscript𝛿𝜃𝜃superscriptℝ𝑞J(\theta):=\mathbb{E}\left[\mathcal{L}\left(\Phi(S\_{T}^{(0,b)},Z\_{T})-V\_{T}^{\delta^{\theta}}\right)\right],\quad\theta\in\mathbb{R}^{q}. |  |

Let θ0subscript𝜃0\theta\_{0} be the initial values for the trainable parameters.121212
In this paper, the initial values of θ𝜃\theta are always set as the glorot initialization of Glorot and Bengio, ([2010](#bib.bib26)).
 The optimization procedure consists in the following iterations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θj+1=θj−ηj​∇θJ​(θj),subscript𝜃𝑗1subscript𝜃𝑗subscript𝜂𝑗subscript∇𝜃𝐽subscript𝜃𝑗\displaystyle\theta\_{j+1}=\theta\_{j}-\eta\_{j}\nabla\_{\theta}J(\theta\_{j}), |  | (3.5) |

where ∇θsubscript∇𝜃\nabla\_{\theta} is the gradient operator with respect to θ𝜃\theta and {ηj}j≥0subscriptsubscript𝜂𝑗𝑗0\{\eta\_{j}\}\_{j\geq 0} is a sequence of small positive real values. In the context of this paper, ∇θJ​(θ)subscript∇𝜃𝐽𝜃\nabla\_{\theta}J(\theta) is unknown analytically and is estimated with Monte Carlo sampling.
Let 𝔹j:={πi,j}i=1Nbatchassignsubscript𝔹𝑗superscriptsubscriptsubscript𝜋

𝑖𝑗𝑖1subscript𝑁batch\mathbb{B}\_{j}:=\{\pi\_{i,j}\}\_{i=1}^{N\_{\text{batch}}} be a mini-batch of simulated hedging errors of size Nbatch∈ℕsubscript𝑁batchℕN\_{\text{batch}}\in\mathbb{N} with πi,jsubscript𝜋

𝑖𝑗\pi\_{i,j} as the ithsuperscript𝑖thi^{\text{th}} hedging error if θ=θj𝜃subscript𝜃𝑗\theta=\theta\_{j}:

|  |  |  |
| --- | --- | --- |
|  | πi,j:=Φ​(ST,i(0,b),ZT,i)−VT,iδθj,assignsubscript𝜋  𝑖𝑗Φsuperscriptsubscript𝑆  𝑇𝑖0𝑏subscript𝑍  𝑇𝑖superscriptsubscript𝑉  𝑇𝑖superscript𝛿subscript𝜃𝑗\pi\_{i,j}:=\Phi(S\_{T,i}^{(0,b)},Z\_{T,i})-V\_{T,i}^{\delta^{\theta\_{j}}}, |  |

where ST,i(0,b),ZT,i

superscriptsubscript𝑆

𝑇𝑖0𝑏subscript𝑍

𝑇𝑖S\_{T,i}^{(0,b)},Z\_{T,i} and VT,iδθjsuperscriptsubscript𝑉

𝑇𝑖superscript𝛿subscript𝜃𝑗V\_{T,i}^{\delta^{\theta\_{j}}} are to be understood as the values of the ithsuperscript𝑖thi^{\text{th}} simulated path. Moreover, denote
J^:ℝNbatch→ℝ:^𝐽→superscriptℝsubscript𝑁batchℝ\hat{J}:\mathbb{R}^{N\_{\text{batch}}}\rightarrow\mathbb{R} as the empirical estimator of J​(θj)𝐽subscript𝜃𝑗J(\theta\_{j}) evaluated with 𝔹jsubscript𝔹𝑗\mathbb{B}\_{j} and ∇θJ^​(𝔹j)subscript∇𝜃^𝐽subscript𝔹𝑗\nabla\_{\theta}\hat{J}(\mathbb{B}\_{j}) as the empirical estimator of ∇θJ​(θj)subscript∇𝜃𝐽subscript𝜃𝑗\nabla\_{\theta}J(\theta\_{j}) evaluated at θ=θj𝜃subscript𝜃𝑗\theta=\theta\_{j}. In [Section 4](#S4 "4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions."), the MSE and SMSE penalties defined respectively as ℒMSE​(x):=x2assignsuperscriptℒMSE𝑥superscript𝑥2\mathcal{L}^{\text{MSE}}(x):=x^{2} and ℒSMSE​(x):=x2​𝟙{x>0}assignsuperscriptℒSMSE𝑥superscript𝑥2subscript1𝑥0\mathcal{L}^{\text{SMSE}}(x):=x^{2}\mathds{1}\_{\{x>0\}} are extensively used. The empirical estimator of the cost function under each penalty can be stated as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | J^MSE​(𝔹j)superscript^𝐽MSEsubscript𝔹𝑗\displaystyle\hat{J}^{\text{MSE}}(\mathbb{B}\_{j}) | :=1Nbatch​∑i=1Nbatchπi,j2,assignabsent1subscript𝑁batchsuperscriptsubscript𝑖1subscript𝑁batchsuperscriptsubscript𝜋  𝑖𝑗2\displaystyle:=\frac{1}{N\_{\text{batch}}}\sum\_{i=1}^{N\_{\text{batch}}}\pi\_{i,j}^{2}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | J^SMSE​(𝔹j)superscript^𝐽SMSEsubscript𝔹𝑗\displaystyle\hat{J}^{\text{SMSE}}(\mathbb{B}\_{j}) | :=1Nbatch​∑i=1Nbatchπi,j2​𝟙{πi,j>0}.assignabsent1subscript𝑁batchsuperscriptsubscript𝑖1subscript𝑁batchsuperscriptsubscript𝜋  𝑖𝑗2subscript1subscript𝜋  𝑖𝑗0\displaystyle:=\frac{1}{N\_{\text{batch}}}\sum\_{i=1}^{N\_{\text{batch}}}\pi\_{i,j}^{2}\mathds{1}\_{\{\pi\_{i,j}>0\}}. |  | (3.6) |

One essential property of the architecture of neural networks is that the gradient of empirical cost functions (i.e. ∇θJ^​(𝔹j)subscript∇𝜃^𝐽subscript𝔹𝑗\nabla\_{\theta}\hat{J}(\mathbb{B}\_{j}) for both penalties) is known analytically. Indeed, we note that hedging errors are linearly dependent of the trading strategies produced as the outputs of the LSTM. Furthermore, the gradient of the outputs of an LSTM with respect to trainable parameters is known analytically (see e.g. Chapter 10 of Goodfellow et al., ([2016](#bib.bib28))).

###### Remark 3.4.

In practice, the algorithm backpropagation through time (BPTT) is often used to compute analytically the gradient of a cost function with respect to the trainable parameters for recurrent type of neural networks such as an LSTM. BPTT leverages the structure of LSTMs (e.g. parameters sharing at each time-step) as well as the chain rule of calculus to obtain such gradients. In practice, efficient deep learning libraries such as Tensorflow (Abadi et al.,, [2016](#bib.bib1)) are often used to implement BPTT. Moreover, algorithms such as Adam (Kingma and Ba,, [2014](#bib.bib38)) which dynamically adapt the terms {ηj}j≥0subscriptsubscript𝜂𝑗𝑗0\{\eta\_{j}\}\_{j\geq 0} in ([3.5](#S3.E5 "Equation 3.5 ‣ 3.2 Training of neural networks ‣ 3 Methodology ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.")) have been shown to improve the training of neural networks. For the rest of the paper, Tensorflow and Adam are used to train every neural network.

## 4   Numerical study

In this section, an extensive numerical study benchmarking different dynamic hedging strategies for the long-term lookback option is presented. [Section 4.3](#S4.SS3 "4.3 Benchmarking of hedging policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") benchmarks two global hedging strategies optimized with the deep hedging algorithm and the local risk minimization scheme of Coleman et al., ([2007](#bib.bib18)) with different hedging instruments and different dynamics for the financial market. [Section 4.4](#S4.SS4 "4.4 Qualitative characteristics of global policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") provides insight into specific characteristics of the optimized global policies.
The setup for the latter numerical experiments is described in [Section 4.1](#S4.SS1 "4.1 Market setup ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") and [Section 4.2](#S4.SS2 "4.2 Dynamics of financial market ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.").

### 4.1   Market setup

The market setup considered in this paper is very similar to the work of Coleman et al., ([2007](#bib.bib18)). The contingent claim to hedge is a lookback option of payoff ΦΦ\Phi as in ([2.2](#S2.E2 "Equation 2.2 ‣ 2.1 Market setup ‣ 2 Hedging of long-term contingent claims ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.")) with a time-to-maturity of 101010 years (i.e. T=10𝑇10T=10). The annualized continuous risk-free rate is set at 3%percent33\% (i.e. r=0.03𝑟0.03r=0.03) and S0(0,b)=100superscriptsubscript𝑆00𝑏100S\_{0}^{(0,b)}=100. In the design of hedging policies, the trading instruments considered are either the underlying, two options or six options. All options have a time-to-maturity of 111 year, are traded once and are held until expiration. For the case of two options, the hedging instruments available at the beginning of each year consist of at-the-money (ATM) calls and puts. With six options, three calls of moneynesses K∈{Stn,1.1​Stn,1.2​Stn}𝐾subscript𝑆subscript𝑡𝑛1.1subscript𝑆subscript𝑡𝑛1.2subscript𝑆subscript𝑡𝑛K\in\{S\_{t\_{n}},1.1S\_{t\_{n}},1.2S\_{t\_{n}}\} and three puts of moneynesses K∈{Stn,0.9​Stn,0.8​Stn}𝐾subscript𝑆subscript𝑡𝑛0.9subscript𝑆subscript𝑡𝑛0.8subscript𝑆subscript𝑡𝑛K\in\{S\_{t\_{n}},0.9S\_{t\_{n}},0.8S\_{t\_{n}}\} are available at the beginning of each year tnsubscript𝑡𝑛t\_{n}.
As for the underlying, both monthly and yearly rebalancing are considered in numerical experiments. Yearly time-steps are used for all hedging instruments (i.e. N=10𝑁10N=10) except when hedging is done with the underlying on a monthly basis (i.e. N=120𝑁120N=120).

###### Remark 4.1.

The methodological approach of [Section 3](#S3 "3 Methodology ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") is in no way dependent on this choice of hedging instruments.

#### 4.1.1   Global hedging penalties

The penalties studied for global hedging are the MSE and SMSE, and the respective optimization procedures are referred to as quadratic deep hedging (QDH) and semi-quadratic deep hedging (SQDH). While the MSE penalizes equally hedging gains and losses, the SMSE is more in line with the actual objectives of the hedger as it corresponds to an agent who strictly penalizes hedging losses proportionally to their squared values.
It is important to note that the computational cost of the deep hedging algorithm is closed to invariant to the choice of loss function. The motivation for assessing the effectiveness of QDH is the popularity of the quadratic penalty in the global hedging literature.

#### 4.1.2   LSTM training

The training of the LSTM is done as described in [Section 3.2](#S3.SS2 "3.2 Training of neural networks ‣ 3 Methodology ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") on a training set of 350,000

350000350,\!000 paths with 150150150 epochs131313
One epoch is defined as a complete iteration of SGD on the training set. For a training set and mini-batch size of respectively 350,000

350000350,\!000 and 1,000

10001,\!000, one epoch consists of a total of 350350350 updates of parameters as in ([3.5](#S3.E5 "Equation 3.5 ‣ 3.2 Training of neural networks ‣ 3 Methodology ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.")).
 and a mini-batch size of 1,000

10001,\!000. A validation set of 75,000

7500075,\!000 paths is used to find the optimal set of trainable parameters out of the 150150150 epochs. More precisely,
at the end of each epoch, the hedging metric associated to the penalty being optimized (i.e. MSE for QDH and SMSE for SQDH) is evaluated on the validation set at the current values of the trainable parameters. The optimal set of trainable parameters is approximated by the one that minimizes the empirical cost function on the validation set out of 150150150 epochs. The use of a validation set to select the number of epochs was found to significantly improve the out-of-sample hedging performance obtained with SQDH, while for QDH, the improvement was marginal.

All results presented in subsequent sections are from a test set (out-of-sample) of 75,000

7500075,\!000 paths. The structure of the LSTM is as in [3.1](#S3.ThmDef1 "Definition 3.1. ‣ 3 Methodology ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") with two LSTM cells (i.e. H=2𝐻2H=2) and 242424 neurons per cell (i.e. d1=d2=24subscript𝑑1subscript𝑑224d\_{1}=d\_{2}=24). The Adam optimizer (Kingma and Ba, ([2014](#bib.bib38))) is used for all examples with a learning rate of 0.010.010.01 for QDH and 0.0160.016\frac{0.01}{6} for SQDH since a smaller learning rate was found to improve the training under the SMSE penalty.

#### 4.1.3   Local risk minimization

Define {Ctnδ}n=0Nsuperscriptsubscriptsuperscriptsubscript𝐶subscript𝑡𝑛𝛿𝑛0𝑁\{C\_{t\_{n}}^{\delta}\}\_{n=0}^{N} as the discounted cumulative cost process associated to a trading strategy δ𝛿\delta:

|  |  |  |
| --- | --- | --- |
|  | Ctnδ:=Btn−1​Vtnδ−Gtnδ,n=0,…,N.formulae-sequenceassignsuperscriptsubscript𝐶subscript𝑡𝑛𝛿superscriptsubscript𝐵subscript𝑡𝑛1superscriptsubscript𝑉subscript𝑡𝑛𝛿superscriptsubscript𝐺subscript𝑡𝑛𝛿𝑛  0…𝑁C\_{t\_{n}}^{\delta}:=B\_{t\_{n}}^{-1}V\_{t\_{n}}^{\delta}-G\_{t\_{n}}^{\delta},\quad n=0,\ldots,N. |  |

Contrarily to global hedging, local risk minimization results in strategies that are not necessarily self-financing. Indeed, the optimization of hedging strategies under this framework imposes the constraint that the terminal portfolio value exactly matches the payoff of the contingent claim, i.e. VTδ=Φ​(ST(0,b),ZT)superscriptsubscript𝑉𝑇𝛿Φsuperscriptsubscript𝑆𝑇0𝑏subscript𝑍𝑇V\_{T}^{\delta}=\Phi(S\_{T}^{(0,b)},Z\_{T}) ℙℙ\mathbb{P}-a.s., which can always be respected by the injection or withdrawal of capital at time T𝑇T. Under this constraint, local risk minimization optimizes at each time-step starting backward from time T𝑇T positions in the assets which minimize the expected squared incremental cost. More precisely, for n=N−1,…,0𝑛

𝑁1…0n=N-1,\ldots,0, the optimization aims at finding (δtn+1(0:D),δtn+1(B))superscriptsubscript𝛿subscript𝑡𝑛1:0𝐷superscriptsubscript𝛿subscript𝑡𝑛1𝐵(\delta\_{t\_{n+1}}^{(0:D)},\delta\_{t\_{n+1}}^{(B)}) that minimize 𝔼​[(Ctn+1δ−Ctnδ)2|ℱtn]𝔼delimited-[]conditionalsuperscriptsuperscriptsubscript𝐶subscript𝑡𝑛1𝛿superscriptsubscript𝐶subscript𝑡𝑛𝛿2subscriptℱsubscript𝑡𝑛\mathbb{E}[(C\_{t\_{n+1}}^{\delta}-C\_{t\_{n}}^{\delta})^{2}|\mathcal{F}\_{t\_{n}}] at time tnsubscript𝑡𝑛t\_{n} with the constraint that VTδ=Φ​(ST(0,b),ZT)superscriptsubscript𝑉𝑇𝛿Φsuperscriptsubscript𝑆𝑇0𝑏subscript𝑍𝑇V\_{T}^{\delta}=\Phi(S\_{T}^{(0,b)},Z\_{T}) ℙℙ\mathbb{P}-a.s. The optimal initial capital amount to invest denoted as V0⋆superscriptsubscript𝑉0⋆V\_{0}^{\star} is also obtained as a result of this scheme. Once the trading strategy δ𝛿\delta is optimized with the local risk minimization procedure, a self-financing strategy can be constructed by setting the initial portfolio value as V0δ=V0⋆superscriptsubscript𝑉0𝛿superscriptsubscript𝑉0⋆V\_{0}^{\delta}=V\_{0}^{\star}, by following the optimized trading strategy strictly for the risky assets (i.e. δtn(0:D)superscriptsubscript𝛿subscript𝑡𝑛:0𝐷\delta\_{t\_{n}}^{(0:D)} for n=1,…,N𝑛

1…𝑁n=1,\ldots,N) and by adjusting positions in the risk-free asset such that the trading strategy is self-financing (i.e. respecting ([2.5](#S2.E5 "Equation 2.5 ‣ 2.1 Market setup ‣ 2 Hedging of long-term contingent claims ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions."))). Hedging results presented in the numerical experiments of this section with local risk minimization are self-financing as per the latter description and are from the work of Coleman et al., ([2007](#bib.bib18)). For examples of numerical schemes to implement local risk procedures, the reader is referred to Coleman et al., ([2006](#bib.bib19)) or Augustyniak et al., ([2017](#bib.bib5)).

The motivation for benchmarking the global policies optimized with our methodological approach to local risk minimization is twofold. First, local risk procedures are popular for the risk mitigation of VAs guarantees in the literature (e.g. Coleman et al., ([2006](#bib.bib19)), Coleman et al., ([2007](#bib.bib18)), Kélani and Quittard-Pinon, ([2017](#bib.bib37)), [Trottier et al., 2018b](#bib.bib52)  and [Trottier et al., 2018a](#bib.bib51) ).
Second, in the context of hedging European vanilla options of maturity one to three years, Augustyniak et al., ([2017](#bib.bib5)) showed that global quadratic hedging with the underlying improves upon the downside risk reduction over local risk minimization. The question remains if the latter holds for longer maturities and when liquid options are used as hedging instruments.

#### 4.1.4   Hedging metrics

The hedging metrics considered for the benchmarking of the different trading policies include the root-mean-square error (RMSE) and the semi-RMSE (i.e. the root of the SMSE statistic). Tail risk metrics are also studied with the Value-at-Risk (VaR) and the Conditional Value-at-Risk (CVaR, Rockafellar and Uryasev, ([2002](#bib.bib47))). For an absolutely continuous integrable random variable141414
All dynamics assumed for the underlying in [Section 4](#S4 "4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") imply that hedging errors are absolutely continuous integrable random variables.
, the CVaR at confidence level α𝛼\alpha has the following representation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CVaRα​(X):=𝔼​[X|X≥VaRα​(X)],α∈(0,1),formulae-sequenceassignsubscriptCVaR𝛼𝑋𝔼delimited-[]conditional𝑋𝑋subscriptVaR𝛼𝑋𝛼01\displaystyle\text{CVaR}\_{\alpha}(X):=\mathbb{E}[X|X\geq\text{VaR}\_{\alpha}(X)],\quad\alpha\in(0,1), |  | (4.1) |

where VaRα​(X):=min𝑥​{x|ℙ​(X≤x)≥α}assignsubscriptVaR𝛼𝑋𝑥conditional-set𝑥ℙ𝑋𝑥𝛼\text{VaR}\_{\alpha}(X):=\underset{x}{\min}\,\{x|\mathbb{P}(X\leq x)\geq\alpha\} is the VaR at confidence level α𝛼\alpha. The CVaRαsubscriptCVaR𝛼\text{CVaR}\_{\alpha} represents tail risk by averaging all hedging errors larger than the αthsuperscript𝛼th\alpha^{\text{th}} percentile of the distribution of hedging errors (i.e. the VaRαsubscriptVaR𝛼\text{VaR}\_{\alpha} metric). Hedging statistics presented in subsequent sections are estimated with conventional empirical estimators on the test set.

### 4.2   Dynamics of financial market

The choice of dynamics for the underlying is motivated by the objective of studying the optimized global policies under different stylized features of the financial market. It is important to recall that deep hedging is a model-free reinforcement learning approach: the LSTM is never explicitly told the dynamics of the financial market during its training phase. Instead, the neural network must learn through many simulations of a market generator how to dynamically adapt its embedded policy, i.e. its trainable parameters, with the objective of minimizing the expected loss function of the resulting hedging errors. The current work studies the impact of the presence of jump risk on optimized global policies by considering the Merton jump-diffusion model (MJD, Merton, ([1976](#bib.bib42))) as well as the Black-Scholes model (BSM, Black and Scholes, ([1973](#bib.bib11))).
Both dynamics are described subsequently and the parameters values presented in [Table 1](#S4.T1 "In 4.2.4 MJD under ℚ ‣ 4.2 Dynamics of financial market ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") and [Table 2](#S4.T2 "In 4.2.4 MJD under ℚ ‣ 4.2 Dynamics of financial market ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.")
are the same as in Coleman et al., ([2007](#bib.bib18)). It is worth noting that while the values of the parameters imply somewhat similar periodic means and standard deviations for log-returns, the MJD parameters entail large and volatile negative jumps occurring on average once over the lifetime of the lookback option.

Moreover, the stochastic models considered in this paper imply that the market is arbitrage-free. By the first fundamental theorem of asset pricing, there exist a probability measure ℚℚ\mathbb{Q} equivalent to ℙℙ\mathbb{P} such that {e−r​tn​Stn(b,0)}n=0Nsuperscriptsubscriptsuperscript𝑒𝑟subscript𝑡𝑛superscriptsubscript𝑆subscript𝑡𝑛𝑏0𝑛0𝑁\{e^{-rt\_{n}}S\_{t\_{n}}^{(b,0)}\}\_{n=0}^{N} is an (𝔽,ℚ

𝔽ℚ\mathbb{F},\mathbb{Q})-martingale (see, for instance, Delbaen and Schachermayer, ([1994](#bib.bib20))). Let ytn:=log⁡(Stn(0,b)/Stn−1(0,b))assignsubscript𝑦subscript𝑡𝑛superscriptsubscript𝑆subscript𝑡𝑛0𝑏superscriptsubscript𝑆subscript𝑡𝑛10𝑏y\_{t\_{n}}:=\log(S\_{t\_{n}}^{(0,b)}/S\_{t\_{n-1}}^{(0,b)}) be the periodic log-return of the underlying, and {ϵtnℙ}n=1Nsuperscriptsubscriptsuperscriptsubscriptitalic-ϵsubscript𝑡𝑛ℙ𝑛1𝑁\{\epsilon\_{t\_{n}}^{\mathbb{P}}\}\_{n=1}^{N} and {ϵtnℚ}n=1Nsuperscriptsubscriptsuperscriptsubscriptitalic-ϵsubscript𝑡𝑛ℚ𝑛1𝑁\{\epsilon\_{t\_{n}}^{\mathbb{Q}}\}\_{n=1}^{N} be sequences of independent standard normal random variables under respectively ℙℙ\mathbb{P} and ℚℚ\mathbb{Q}. The dynamics of both models are now formally defined.

#### 4.2.1   BSM under ℙℙ\mathbb{P}

The discrete BSM assumes that log-returns are i.i.d. normal random variables of periodic mean and variance of respectively (μ−σ22)​ΔN𝜇superscript𝜎22subscriptΔ𝑁(\mu-\frac{\sigma^{2}}{2})\Delta\_{N} and σ2​ΔNsuperscript𝜎2subscriptΔ𝑁\sigma^{2}\Delta\_{N}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ytnsubscript𝑦subscript𝑡𝑛\displaystyle y\_{t\_{n}} | =(μ−σ22)​ΔN+σ​ΔN​ϵtnℙ,n=1,…,N,formulae-sequenceabsent𝜇superscript𝜎22subscriptΔ𝑁𝜎subscriptΔ𝑁superscriptsubscriptitalic-ϵsubscript𝑡𝑛ℙ𝑛  1…𝑁\displaystyle=\left(\mu-\frac{\sigma^{2}}{2}\right)\Delta\_{N}+\sigma\sqrt{\Delta\_{N}}\epsilon\_{t\_{n}}^{\mathbb{P}},\quad n=1,\ldots,N, |  | (4.2) |

where μ∈ℝ𝜇ℝ\mu\in\mathbb{R} and σ>0𝜎0\sigma>0 are the yearly model parameters.

#### 4.2.2   MJD under ℙℙ\mathbb{P}

The MJD model extends the BSM by assuming the presence of random jumps to the underlying stock price. More precisely, let {ζkℙ}k=1∞superscriptsubscriptsuperscriptsubscript𝜁𝑘ℙ𝑘1\{\zeta\_{k}^{\mathbb{P}}\}\_{k=1}^{\infty} be independent normal random variables of mean μJsubscript𝜇𝐽\mu\_{J} and variance σJ2superscriptsubscript𝜎𝐽2\sigma\_{J}^{2}, and {Ntnℙ}n=0Nsuperscriptsubscriptsuperscriptsubscript𝑁subscript𝑡𝑛ℙ𝑛0𝑁\{N\_{t\_{n}}^{\mathbb{P}}\}\_{n=0}^{N} be values of a Poisson process of intensity λ>0𝜆0\lambda>0 where {ζkℙ}k=1∞,{Ntnℙ}n=0N

superscriptsubscriptsuperscriptsubscript𝜁𝑘ℙ𝑘1superscriptsubscriptsuperscriptsubscript𝑁subscript𝑡𝑛ℙ𝑛0𝑁\{\zeta\_{k}^{\mathbb{P}}\}\_{k=1}^{\infty},\{N\_{t\_{n}}^{\mathbb{P}}\}\_{n=0}^{N} and {ϵtnℙ}n=1Nsuperscriptsubscriptsuperscriptsubscriptitalic-ϵsubscript𝑡𝑛ℙ𝑛1𝑁\{\epsilon\_{t\_{n}}^{\mathbb{P}}\}\_{n=1}^{N} are independent. Periodic log-returns under this model can be stated as follows151515
We adopt the convention that if Ntnℙ=Ntn−1ℙsuperscriptsubscript𝑁subscript𝑡𝑛ℙsuperscriptsubscript𝑁subscript𝑡𝑛1ℙN\_{t\_{n}}^{\mathbb{P}}=N\_{t\_{n-1}}^{\mathbb{P}}, then:

∑k=Ntn−1ℙ+1Ntnℙζkℙ=0.superscriptsubscript𝑘superscriptsubscript𝑁subscript𝑡𝑛1ℙ1superscriptsubscript𝑁subscript𝑡𝑛ℙsuperscriptsubscript𝜁𝑘ℙ0\sum\_{k=N\_{t\_{n-1}}^{\mathbb{P}}+1}^{N\_{t\_{n}}^{\mathbb{P}}}\zeta\_{k}^{\mathbb{P}}=0.
:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ytn=(α−λ​(eμJ+σJ2/2−1)−σ22)​ΔN+σ​ΔN​ϵtnℙ+∑k=Ntn−1ℙ+1Ntnℙζkℙ,subscript𝑦subscript𝑡𝑛𝛼𝜆superscript𝑒subscript𝜇𝐽superscriptsubscript𝜎𝐽221superscript𝜎22subscriptΔ𝑁𝜎subscriptΔ𝑁superscriptsubscriptitalic-ϵsubscript𝑡𝑛ℙsuperscriptsubscript𝑘superscriptsubscript𝑁subscript𝑡𝑛1ℙ1superscriptsubscript𝑁subscript𝑡𝑛ℙsuperscriptsubscript𝜁𝑘ℙ\displaystyle y\_{t\_{n}}=\left(\alpha-\lambda\left(e^{\mu\_{J}+\sigma\_{J}^{2}/2}-1\right)-\frac{\sigma^{2}}{2}\right)\Delta\_{N}+\sigma\sqrt{\Delta\_{N}}\epsilon\_{t\_{n}}^{\mathbb{P}}+\sum\_{k=N\_{t\_{n-1}}^{\mathbb{P}}+1}^{N\_{t\_{n}}^{\mathbb{P}}}\zeta\_{k}^{\mathbb{P}}, |  | (4.3) |

where {α,μJ,σJ,λ,σ}𝛼subscript𝜇𝐽subscript𝜎𝐽𝜆𝜎\{\alpha,\mu\_{J},\sigma\_{J},\lambda,\sigma\} are the model parameters with {α,λ,σ}𝛼𝜆𝜎\{\alpha,\lambda,\sigma\} being on a yearly scale, α∈ℝ𝛼ℝ\alpha\in\mathbb{R} and σ>0𝜎0\sigma>0.

#### 4.2.3   BSM under ℚℚ\mathbb{Q}

By a discrete-time version of the Girsanov theorem, there exist an 𝔽𝔽\mathbb{F}-adapted market price of risk process {φtn}n=1Nsuperscriptsubscriptsubscript𝜑subscript𝑡𝑛𝑛1𝑁\{\varphi\_{t\_{n}}\}\_{n=1}^{N} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵtnℚ=ϵtnℙ−φtn,n=1,…,N.formulae-sequencesuperscriptsubscriptitalic-ϵsubscript𝑡𝑛ℚsuperscriptsubscriptitalic-ϵsubscript𝑡𝑛ℙsubscript𝜑subscript𝑡𝑛𝑛  1…𝑁\displaystyle\epsilon\_{t\_{n}}^{\mathbb{Q}}=\epsilon\_{t\_{n}}^{\mathbb{P}}-\varphi\_{t\_{n}},\quad n=1,\ldots,N. |  | (4.4) |

For n=1,…,N𝑛

1…𝑁n=1,\ldots,N, let φtn:=−ΔN​(μ−rσ)assignsubscript𝜑subscript𝑡𝑛subscriptΔ𝑁𝜇𝑟𝜎\varphi\_{t\_{n}}:=-\sqrt{\Delta\_{N}}\left(\frac{\mu-r}{\sigma}\right). By replacing ϵtnℙ=ϵtnℚ+φtnsuperscriptsubscriptitalic-ϵsubscript𝑡𝑛ℙsuperscriptsubscriptitalic-ϵsubscript𝑡𝑛ℚsubscript𝜑subscript𝑡𝑛\epsilon\_{t\_{n}}^{\mathbb{P}}=\epsilon\_{t\_{n}}^{\mathbb{Q}}+\varphi\_{t\_{n}} into ([4.2](#S4.E2 "Equation 4.2 ‣ 4.2.1 BSM under ℙ ‣ 4.2 Dynamics of financial market ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.")), it is straightforward to obtain the ℚℚ\mathbb{Q}-dynamics of log-returns:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ytnsubscript𝑦subscript𝑡𝑛\displaystyle y\_{t\_{n}} | =(r−σ22)​ΔN+σ​ΔN​ϵtnℚ,n=1,…,N.formulae-sequenceabsent𝑟superscript𝜎22subscriptΔ𝑁𝜎subscriptΔ𝑁superscriptsubscriptitalic-ϵsubscript𝑡𝑛ℚ𝑛  1…𝑁\displaystyle=\left(r-\frac{\sigma^{2}}{2}\right)\Delta\_{N}+\sigma\sqrt{\Delta\_{N}}\epsilon\_{t\_{n}}^{\mathbb{Q}},\quad n=1,\ldots,N. |  | (4.5) |

The pricing of European calls and puts used as hedging instruments under this model is done with the well-known Black-Scholes closed-form solutions.

#### 4.2.4   MJD under ℚℚ\mathbb{Q}

The change of measure considered is the same as the one from Coleman et al., ([2007](#bib.bib18)). Let {ζkℚ}k=1∞superscriptsubscriptsuperscriptsubscript𝜁𝑘ℚ𝑘1\{\zeta\_{k}^{\mathbb{Q}}\}\_{k=1}^{\infty} be independent normal random variables under ℚℚ\mathbb{Q} of mean μ~Jsubscript~𝜇𝐽\tilde{\mu}\_{J} and variance σ~J2superscriptsubscript~𝜎𝐽2\tilde{\sigma}\_{J}^{2}, and {Ntnℚ}n=0Nsuperscriptsubscriptsuperscriptsubscript𝑁subscript𝑡𝑛ℚ𝑛0𝑁\{N\_{t\_{n}}^{\mathbb{Q}}\}\_{n=0}^{N} be values of a Poisson process of intensity λ~>0~𝜆0\tilde{\lambda}>0 where {ζkℚ}k=1∞superscriptsubscriptsuperscriptsubscript𝜁𝑘ℚ𝑘1\{\zeta\_{k}^{\mathbb{Q}}\}\_{k=1}^{\infty}, {Ntnℚ}n=0Nsuperscriptsubscriptsuperscriptsubscript𝑁subscript𝑡𝑛ℚ𝑛0𝑁\{N\_{t\_{n}}^{\mathbb{Q}}\}\_{n=0}^{N} and {ϵtnℚ}n=1Nsuperscriptsubscriptsuperscriptsubscriptitalic-ϵsubscript𝑡𝑛ℚ𝑛1𝑁\{\epsilon\_{t\_{n}}^{\mathbb{Q}}\}\_{n=1}^{N} are independent. The ℚℚ\mathbb{Q}-dynamics of log-returns can be stated as follows:

|  |  |  |
| --- | --- | --- |
|  | ytn=(r−λ~​(eμ~J+σ~J2/2−1)−σ22)​ΔN+σ​ΔN​ϵtnℚ+∑k=Ntn−1ℚ+1Ntnℚζkℚ,subscript𝑦subscript𝑡𝑛𝑟~𝜆superscript𝑒subscript~𝜇𝐽superscriptsubscript~𝜎𝐽221superscript𝜎22subscriptΔ𝑁𝜎subscriptΔ𝑁superscriptsubscriptitalic-ϵsubscript𝑡𝑛ℚsuperscriptsubscript𝑘superscriptsubscript𝑁subscript𝑡𝑛1ℚ1superscriptsubscript𝑁subscript𝑡𝑛ℚsuperscriptsubscript𝜁𝑘ℚ\displaystyle y\_{t\_{n}}=\left(r-\tilde{\lambda}\left(e^{\tilde{\mu}\_{J}+\tilde{\sigma}\_{J}^{2}/2}-1\right)-\frac{\sigma^{2}}{2}\right)\Delta\_{N}+\sigma\sqrt{\Delta\_{N}}\epsilon\_{t\_{n}}^{\mathbb{Q}}+\sum\_{k=N\_{t\_{n-1}}^{\mathbb{Q}}+1}^{N\_{t\_{n}}^{\mathbb{Q}}}\zeta\_{k}^{\mathbb{Q}}, |  |

where σ~J:=σJassignsubscript~𝜎𝐽subscript𝜎𝐽\tilde{\sigma}\_{J}:=\sigma\_{J}, μ~J:=μJ−(1−γ)​σJ2,λ~:=λ​e−(1−γ)​(μJ−12​(1−γ)​σJ2)formulae-sequenceassignsubscript~𝜇𝐽subscript𝜇𝐽1𝛾superscriptsubscript𝜎𝐽2assign~𝜆𝜆superscript𝑒1𝛾subscript𝜇𝐽121𝛾superscriptsubscript𝜎𝐽2\tilde{\mu}\_{J}:=\mu\_{J}-(1-\gamma)\sigma\_{J}^{2},\tilde{\lambda}:=\lambda e^{-(1-\gamma)(\mu\_{J}-\frac{1}{2}(1-\gamma)\sigma\_{J}^{2})} with γ≤1𝛾1\gamma\leq 1 as the risk aversion parameter which is set at γ=−1.5𝛾1.5\gamma=-1.5. The value of the risk aversion parameter implies more frequent and more negative jumps on average under ℚℚ\mathbb{Q} than under ℙℙ\mathbb{P} by increasing λ~~𝜆\tilde{\lambda} and decreasing μ~Jsubscript~𝜇𝐽\tilde{\mu}\_{J}.
The pricing of European calls and puts used as hedging instruments under the MJD model is done with the well-known closed-form solutions.

Table 1: Parameters of the Black-Scholes model.

|  |  |
| --- | --- |
| μ𝜇\mu | σ𝜎\sigma |
| 0.100.100.10 | 0.150.150.15 |

Notes: Both μ𝜇\mu and σ𝜎\sigma are on an annual basis.




Table 2: Parameters of the Merton jump-diffusion model.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| α𝛼\alpha | σ𝜎\sigma | λ𝜆\lambda | μJsubscript𝜇𝐽\mu\_{J} | σJsubscript𝜎𝐽\sigma\_{J} | γ𝛾\gamma |
| 0.100.100.10 | 0.150.150.15 | 0.100.100.10 | −0.200.20-0.20 | 0.150.150.15 | −1.51.5-1.5 |

Notes: α𝛼\alpha, σ𝜎\sigma and λ𝜆\lambda are on an annual basis.

### 4.3   Benchmarking of hedging policies

In this section, the hedging effectiveness of QDH, SQDH and local risk minimization is assessed under various market settings. The analysis starts off in [Section 4.3.1](#S4.SS3.SSS1 "4.3.1 QDH and local risk minimization benchmark ‣ 4.3 Benchmarking of hedging policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") by comparing QDH and local risk minimization performance as both approaches are optimized with a quadratic criterion; the benchmarking of global hedging policies embedded in QDH and SQDH is done in [Section 4.3.2](#S4.SS3.SSS2 "4.3.2 QDH and SQDH benchmark ‣ 4.3 Benchmarking of hedging policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.").

#### 4.3.1   QDH and local risk minimization benchmark

[Table 3](#S4.T3 "In 4.3.1 QDH and local risk minimization benchmark ‣ 4.3 Benchmarking of hedging policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") and [Table 4](#S4.T4 "In 4.3.1 QDH and local risk minimization benchmark ‣ 4.3 Benchmarking of hedging policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") presents hedging statistics of QDH and local risk minimization under respectively the BSM and MJD model.161616
The choice of hedging statistics presented in [Table 3](#S4.T3 "In 4.3.1 QDH and local risk minimization benchmark ‣ 4.3 Benchmarking of hedging policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") and [Table 4](#S4.T4 "In 4.3.1 QDH and local risk minimization benchmark ‣ 4.3 Benchmarking of hedging policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") are the ones considered in Coleman et al., ([2007](#bib.bib18)). Additional hedging statistics for QDH are presented in [Section 4.3.2](#S4.SS3.SSS2 "4.3.2 QDH and SQDH benchmark ‣ 4.3 Benchmarking of hedging policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.").
 For comparative purposes, the initial capital investment
is set to the optimized value obtained as a result of the local risk minimization procedure of Coleman et al., ([2007](#bib.bib18)) for all examples. We note that this choice naturally gives a disadvantage to QDH.

Table 3: Benchmarking of quadratic deep hedging (QDH) and local risk minimization to hedge the lookback option of T=10𝑇10T=10 years under the BSM.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Local risk minimization | | |  | QDH | | |  |
| Statistics | V0δsuperscriptsubscript𝑉0𝛿V\_{0}^{\delta} | RMSE | VaR0.95subscriptVaR0.95\text{VaR}\_{0.95} | CVaR0.95subscriptCVaR0.95\text{CVaR}\_{0.95} |  | RMSE | VaR0.95subscriptVaR0.95\text{VaR}\_{0.95} | CVaR0.95subscriptCVaR0.95\text{CVaR}\_{0.95} |  |
| Stock (year) | 13.913.913.9 | 15.915.915.9 | 28.528.528.5 | 43.243.243.2 |  | 14.814.814.8 | 25.525.525.5 | 41.241.241.2 |  |
| Stock (month) | 17.317.317.3 | 5.55.55.5 | 8.98.98.9 | 13.013.013.0 |  | 4.94.94.9 | 7.77.77.7 | 12.212.212.2 |  |
| Two options | 17.417.417.4 | 4.64.64.6 | 7.07.07.0 | 11.911.911.9 |  | 4.24.24.2 | 6.16.16.1 | 11.211.211.2 |  |
| Six options | 17.717.717.7 | 1.61.61.6 | 2.42.42.4 | 3.83.83.8 |  | 1.11.11.1 | 1.21.21.2 | 2.42.42.4 |  |

Notes: Hedging statistics under the BSM with μ=0.1,σ=0.15,r=0.03formulae-sequence𝜇0.1formulae-sequence𝜎0.15𝑟0.03\mu=0.1,\sigma=0.15,r=0.03 and S0(0,b)=100superscriptsubscript𝑆00𝑏100S\_{0}^{(0,b)}=100 (see [Section 4.2.1](#S4.SS2.SSS1 "4.2.1 BSM under ℙ ‣ 4.2 Dynamics of financial market ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") for model description under ℙℙ\mathbb{P} and [Section 4.2.3](#S4.SS2.SSS3 "4.2.3 BSM under ℚ ‣ 4.2 Dynamics of financial market ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") for the risk-neutral dynamics used for option pricing). Hedging instruments: monthly and yearly underlying, yearly ATM call and put options (two options) and three yearly calls and puts of strikes K={Stn(0,b),1.1​Stn(0,b),1.2​Stn(0,b)}𝐾superscriptsubscript𝑆subscript𝑡𝑛0𝑏1.1superscriptsubscript𝑆subscript𝑡𝑛0𝑏1.2superscriptsubscript𝑆subscript𝑡𝑛0𝑏K=\{S\_{t\_{n}}^{(0,b)},1.1S\_{t\_{n}}^{(0,b)},1.2S\_{t\_{n}}^{(0,b)}\} and K={Stn(0,b),0.9​Stn(0,b),0.8​Stn(0,b)}𝐾superscriptsubscript𝑆subscript𝑡𝑛0𝑏0.9superscriptsubscript𝑆subscript𝑡𝑛0𝑏0.8superscriptsubscript𝑆subscript𝑡𝑛0𝑏K=\{S\_{t\_{n}}^{(0,b)},0.9S\_{t\_{n}}^{(0,b)},0.8S\_{t\_{n}}^{(0,b)}\} (six options). Results for local risk minimization and initial portfolio values V0δsuperscriptsubscript𝑉0𝛿V\_{0}^{\delta} are from Table 333 of Coleman et al., ([2007](#bib.bib18)). Results for QDH are computed based on 75,000

7500075,\!000 independent paths generated from the BSM under ℙℙ\mathbb{P}. Training of the neural networks is done as described in [Section 4.1.2](#S4.SS1.SSS2 "4.1.2 LSTM training ‣ 4.1 Market setup ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.").




Table 4: Benchmarking of quadratic deep hedging (QDH) and local risk minimization to hedge the lookback option of T=10𝑇10T=10 years under the MJD model.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Local risk minimization | | |  | QDH | | |  |
| Statistics | V0δsuperscriptsubscript𝑉0𝛿V\_{0}^{\delta} | RMSE | VaR0.95subscriptVaR0.95\text{VaR}\_{0.95} | CVaR0.95subscriptCVaR0.95\text{CVaR}\_{0.95} |  | RMSE | VaR0.95subscriptVaR0.95\text{VaR}\_{0.95} | CVaR0.95subscriptCVaR0.95\text{CVaR}\_{0.95} |  |
| Stock (year) | 19.519.519.5 | 21.421.421.4 | 38.438.438.4 | 60.560.560.5 |  | 19.519.519.5 | 33.133.133.1 | 55.855.855.8 |  |
| Stock (month) | 22.822.822.8 | 13.013.013.0 | 23.523.523.5 | 38.438.438.4 |  | 11.011.011.0 | 16.316.316.3 | 33.533.533.5 |  |
| Two options | 24.624.624.6 | 6.06.06.0 | 8.48.48.4 | 15.215.215.2 |  | 5.25.25.2 | 6.76.76.7 | 12.912.912.9 |  |
| Six options | 25.225.225.2 | 1.91.91.9 | 2.82.82.8 | 4.64.64.6 |  | 1.31.31.3 | 1.71.71.7 | 3.23.23.2 |  |

Notes: Hedging statistics under the MJD model with α=0.1,σ=0.15,λ=0.1,μJ=−0.2,σJ=0.15,γ=−1.5,r=0.03formulae-sequence𝛼0.1formulae-sequence𝜎0.15formulae-sequence𝜆0.1formulae-sequencesubscript𝜇𝐽0.2formulae-sequencesubscript𝜎𝐽0.15formulae-sequence𝛾1.5𝑟0.03\alpha=0.1,\sigma=0.15,\lambda=0.1,\mu\_{J}=-0.2,\sigma\_{J}=0.15,\gamma=-1.5,r=0.03 and S0(0,b)=100superscriptsubscript𝑆00𝑏100S\_{0}^{(0,b)}=100 (see [Section 4.2.2](#S4.SS2.SSS2 "4.2.2 MJD under ℙ ‣ 4.2 Dynamics of financial market ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") for model description under ℙℙ\mathbb{P} and [Section 4.2.4](#S4.SS2.SSS4 "4.2.4 MJD under ℚ ‣ 4.2 Dynamics of financial market ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") for the risk-neutral dynamics used for option pricing). Hedging instruments: monthly and yearly underlying, yearly ATM call and put options (two options) and three yearly calls and puts of strikes K={Stn(0,b),1.1​Stn(0,b),1.2​Stn(0,b)}𝐾superscriptsubscript𝑆subscript𝑡𝑛0𝑏1.1superscriptsubscript𝑆subscript𝑡𝑛0𝑏1.2superscriptsubscript𝑆subscript𝑡𝑛0𝑏K=\{S\_{t\_{n}}^{(0,b)},1.1S\_{t\_{n}}^{(0,b)},1.2S\_{t\_{n}}^{(0,b)}\} and K={Stn(0,b),0.9​Stn(0,b),0.8​Stn(0,b)}𝐾superscriptsubscript𝑆subscript𝑡𝑛0𝑏0.9superscriptsubscript𝑆subscript𝑡𝑛0𝑏0.8superscriptsubscript𝑆subscript𝑡𝑛0𝑏K=\{S\_{t\_{n}}^{(0,b)},0.9S\_{t\_{n}}^{(0,b)},0.8S\_{t\_{n}}^{(0,b)}\} (six options). Results for local risk minimization and initial portfolio values V0δsuperscriptsubscript𝑉0𝛿V\_{0}^{\delta} are from Table 444 of Coleman et al., ([2007](#bib.bib18)). Results for QDH are computed based on 75,000

7500075,\!000 independent paths generated from the MJD model under ℙℙ\mathbb{P}. Training of the neural networks is done as described in [Section 4.1.2](#S4.SS1.SSS2 "4.1.2 LSTM training ‣ 4.1 Market setup ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.").

Since QDH optimizes the MSE penalty, the latter was expected to outperform local risk minimization on the RMSE metric. The question remained if QDH also improved upon the downside risk captured by the VaR0.95subscriptVaR0.95\text{VaR}\_{0.95} and CVaR0.95subscriptCVaR0.95\text{CVaR}\_{0.95} statistics. Numerical results under both dynamics demonstrate that QDH outperforms local risk minimization across all downside risk metrics and all hedging instruments. The risk reduction obtained with QDH over local risk minimization is most impressive with six options: the percentage decrease for respectively the RMSE, VaR0.95subscriptVaR0.95\text{VaR}\_{0.95} and CVaR0.95subscriptCVaR0.95\text{CVaR}\_{0.95} statistics are of 33%,52%

percent33percent5233\%,52\% and 36%percent3636\% under the BSM and of 27%,38%

percent27percent3827\%,38\% and 30%percent3030\% under the MJD model. As for hedging with the underlying on a monthly and yearly basis as well as with two options, the improvement of QDH over local risk minimization for the three hedging statistics
ranges between 5%percent55\% to 13%percent1313\% under the BSM and 8%percent88\% to 20%percent2020\% under the MJD model except for the VaR0.95subscriptVaR0.95\text{VaR}\_{0.95} metric with the stock on a monthly basis under the MJD dynamics which achieves 30%percent3030\% reduction.
These results demonstrate that the use of a global procedure rather than a local procedure provides better hedging performance.

#### 4.3.2   QDH and SQDH benchmark

The benchmarking of QDH and SQDH policies is now presented with the same setup as in the previous section except for the initial capital investment which is set as the risk-neutral price of the lookback option under both dynamics for all hedging instruments: 17.7​$17.7currency-dollar17.7\$ for BSM and 25.3​$25.3currency-dollar25.3\$ for MJD.171717
Risk-neutral prices of the lookback option were estimated with simulations for both dynamics.
 This choice is motivated by the objective of comparing on common grounds the results obtained across the different hedging instruments for both global hedging approaches. [Table 5](#S4.T5 "In 4.3.2 QDH and SQDH benchmark ‣ 4.3 Benchmarking of hedging policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") and [Table 6](#S4.T6 "In 4.3.2 QDH and SQDH benchmark ‣ 4.3 Benchmarking of hedging policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") present descriptive statistics of the hedging shortfall obtained with QDH and SQDH under respectively the BSM and MJD model.

Table 5: Benchmarking of quadratic deep hedging (QDH) and semi-quadratic deep hedging (SQDH) to hedge the lookback option of T=10𝑇10T=10 years under the BSM.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Statistics | Mean | RMSE | semi-RMSE | VaR0.95subscriptVaR0.95\text{VaR}\_{0.95} | VaR0.99subscriptVaR0.99\text{VaR}\_{0.99} | CVaR0.95subscriptCVaR0.95\text{CVaR}\_{0.95} | CVaR0.99subscriptCVaR0.99\text{CVaR}\_{0.99} | Skew |
| *QDH* | | | |  |  |  |  |  |
| Stock (year) | −0.50.5-0.5 | 14.814.814.8 | 12.012.012.0 | 25.825.825.8 | 49.849.849.8 | 41.441.441.4 | 69.969.969.9 | 1.91.91.9 |
| Stock (month) | 0.20.20.2 | 4.94.94.9 | 3.63.63.6 | 7.97.97.9 | 14.514.514.5 | 12.112.112.1 | 19.419.419.4 | 0.40.40.4 |
| Two options | 0.00.00.0 | 4.24.24.2 | 3.23.23.2 | 6.56.56.5 | 14.014.014.0 | 11.511.511.5 | 20.920.920.9 | 1.91.91.9 |
| Six options | 0.00.00.0 | 1.11.11.1 | 0.80.80.8 | 1.21.21.2 | 2.82.82.8 | 2.42.42.4 | 5.15.15.1 | 3.33.33.3 |
| *SQDH* | | | |  |  |  |  |  |
| Stock (year) | −32.132.1-32.1 | 43.843.843.8 | 4.44.44.4 | 6.46.46.4 | 21.121.121.1 | 16.016.016.0 | 32.732.732.7 | −1.01.0-1.0 |
| Stock (month) | −10.110.1-10.1 | 15.015.015.0 | 1.51.51.5 | 2.52.52.5 | 6.16.16.1 | 4.94.94.9 | 9.49.49.4 | −1.51.5-1.5 |
| Two options | −5.45.4-5.4 | 10.010.010.0 | 1.61.61.6 | 1.31.31.3 | 5.55.55.5 | 4.14.14.1 | 9.89.89.8 | −2.32.3-2.3 |
| Six options | −0.90.9-0.9 | 2.22.22.2 | 0.40.40.4 | 0.20.20.2 | 1.01.01.0 | 0.80.80.8 | 2.02.02.0 | −5.05.0-5.0 |

Notes: Hedging statistics under the BSM with μ=0.1,σ=0.15,r=0.03,S0(0,b)=100formulae-sequence𝜇0.1formulae-sequence𝜎0.15formulae-sequence𝑟0.03superscriptsubscript𝑆00𝑏100\mu=0.1,\sigma=0.15,r=0.03,S\_{0}^{(0,b)}=100 and V0δ=17.7superscriptsubscript𝑉0𝛿17.7V\_{0}^{\delta}=17.7 for all examples (see [Section 4.2.1](#S4.SS2.SSS1 "4.2.1 BSM under ℙ ‣ 4.2 Dynamics of financial market ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") for model description under ℙℙ\mathbb{P} and [Section 4.2.3](#S4.SS2.SSS3 "4.2.3 BSM under ℚ ‣ 4.2 Dynamics of financial market ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") for the risk-neutral dynamics used for option pricing). Hedging instruments: monthly and yearly underlying, yearly ATM call and put options (two options) and three yearly calls and puts of strikes K={Stn(0,b),1.1​Stn(0,b),1.2​Stn(0,b)}𝐾superscriptsubscript𝑆subscript𝑡𝑛0𝑏1.1superscriptsubscript𝑆subscript𝑡𝑛0𝑏1.2superscriptsubscript𝑆subscript𝑡𝑛0𝑏K=\{S\_{t\_{n}}^{(0,b)},1.1S\_{t\_{n}}^{(0,b)},1.2S\_{t\_{n}}^{(0,b)}\} and K={Stn(0,b),0.9​Stn(0,b),0.8​Stn(0,b)}𝐾superscriptsubscript𝑆subscript𝑡𝑛0𝑏0.9superscriptsubscript𝑆subscript𝑡𝑛0𝑏0.8superscriptsubscript𝑆subscript𝑡𝑛0𝑏K=\{S\_{t\_{n}}^{(0,b)},0.9S\_{t\_{n}}^{(0,b)},0.8S\_{t\_{n}}^{(0,b)}\} (six options). Results for each penalty are computed based on 75,000

7500075,\!000 independent paths generated from the BSM under ℙℙ\mathbb{P}. Training of the neural networks is done as described in [Section 4.1.2](#S4.SS1.SSS2 "4.1.2 LSTM training ‣ 4.1 Market setup ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.").




Table 6: Benchmarking of quadratic deep hedging (QDH) and semi-quadratic deep hedging (SQDH) to hedge the lookback option of T=10𝑇10T=10 years under the MJD model.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Statistics | Mean | RMSE | semi-RMSE | VaR0.95subscriptVaR0.95\text{VaR}\_{0.95} | VaR0.99subscriptVaR0.99\text{VaR}\_{0.99} | CVaR0.95subscriptCVaR0.95\text{CVaR}\_{0.95} | CVaR0.99subscriptCVaR0.99\text{CVaR}\_{0.99} | Skew |
| *QDH* | | | |  |  |  |  |  |
| Stock (year) | −1.61.6-1.6 | 19.819.819.8 | 15.615.615.6 | 32.332.332.3 | 66.466.466.4 | 54.554.554.5 | 95.495.495.4 | 2.12.12.1 |
| Stock (month) | 0.20.20.2 | 11.211.211.2 | 9.49.49.4 | 15.715.715.7 | 42.842.842.8 | 32.632.632.6 | 64.664.664.6 | 3.23.23.2 |
| Two options | 0.00.00.0 | 5.25.25.2 | 3.83.83.8 | 6.76.76.7 | 15.415.415.4 | 12.712.712.7 | 25.125.125.1 | 1.61.61.6 |
| Six options | −0.10.1-0.1 | 1.31.31.3 | 0.90.90.9 | 1.41.41.4 | 3.63.63.6 | 2.92.92.9 | 6.26.26.2 | 2.32.32.3 |
| *SQDH* | | | |  |  |  |  |  |
| Stock (year) | −35.235.2-35.2 | 49.749.749.7 | 6.76.76.7 | 11.411.411.4 | 31.731.731.7 | 24.624.624.6 | 47.747.747.7 | −0.80.8-0.8 |
| Stock (month) | −22.822.8-22.8 | 33.833.833.8 | 4.24.24.2 | 6.56.56.5 | 18.318.318.3 | 14.314.314.3 | 29.629.629.6 | −1.11.1-1.1 |
| Two options | −5.95.9-5.9 | 11.211.211.2 | 1.71.71.7 | 2.22.22.2 | 7.17.17.1 | 5.55.55.5 | 12.212.212.2 | −2.52.5-2.5 |
| Six options | −1.31.3-1.3 | 3.13.13.1 | 0.50.50.5 | 0.30.30.3 | 1.41.41.4 | 1.11.11.1 | 2.92.92.9 | −4.84.8-4.8 |

Notes: Hedging statistics under the MJD model with α=0.1,σ=0.15,λ=0.1,μJ=−0.2,σJ=0.15,γ=−1.5,r=0.03,S0(0,b)=100formulae-sequence𝛼0.1formulae-sequence𝜎0.15formulae-sequence𝜆0.1formulae-sequencesubscript𝜇𝐽0.2formulae-sequencesubscript𝜎𝐽0.15formulae-sequence𝛾1.5formulae-sequence𝑟0.03superscriptsubscript𝑆00𝑏100\alpha=0.1,\sigma=0.15,\lambda=0.1,\mu\_{J}=-0.2,\sigma\_{J}=0.15,\gamma=-1.5,r=0.03,S\_{0}^{(0,b)}=100 and V0δ=25.3superscriptsubscript𝑉0𝛿25.3V\_{0}^{\delta}=25.3 for all examples (see [Section 4.2.2](#S4.SS2.SSS2 "4.2.2 MJD under ℙ ‣ 4.2 Dynamics of financial market ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") for model description under ℙℙ\mathbb{P} and [Section 4.2.4](#S4.SS2.SSS4 "4.2.4 MJD under ℚ ‣ 4.2 Dynamics of financial market ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") for the risk-neutral dynamics used for option pricing). Hedging instruments: monthly and yearly underlying, yearly ATM call and put options (two options) and three yearly calls and puts of strikes K={Stn(0,b),1.1​Stn(0,b),1.2​Stn(0,b)}𝐾superscriptsubscript𝑆subscript𝑡𝑛0𝑏1.1superscriptsubscript𝑆subscript𝑡𝑛0𝑏1.2superscriptsubscript𝑆subscript𝑡𝑛0𝑏K=\{S\_{t\_{n}}^{(0,b)},1.1S\_{t\_{n}}^{(0,b)},1.2S\_{t\_{n}}^{(0,b)}\} and K={Stn(0,b),0.9​Stn(0,b),0.8​Stn(0,b)}𝐾superscriptsubscript𝑆subscript𝑡𝑛0𝑏0.9superscriptsubscript𝑆subscript𝑡𝑛0𝑏0.8superscriptsubscript𝑆subscript𝑡𝑛0𝑏K=\{S\_{t\_{n}}^{(0,b)},0.9S\_{t\_{n}}^{(0,b)},0.8S\_{t\_{n}}^{(0,b)}\} (six options). Results for each penalty are computed based on 75,000

7500075,\!000 independent paths generated from the MJD model. Training of the neural networks is done as described in [Section 4.1.2](#S4.SS1.SSS2 "4.1.2 LSTM training ‣ 4.1 Market setup ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.").

Numerical results indicate that as compared to QDH, SQDH policies result in downside risk metrics two to three times smaller for almost all examples and earn significant gains across all hedging instruments (i.e. negative mean hedging errors). While QDH minimizes the RMSE statistic, the downside risk captured by the semi-RMSE, VaRαsubscriptVaR𝛼\text{VaR}\_{\alpha} and CVaRαsubscriptCVaR𝛼\text{CVaR}\_{\alpha} statistics for α𝛼\alpha equal to 0.950.950.95 and 0.990.990.99 are always significantly reduced by SQDH policies. Indeed, the downside risk reduction with SQDH over QDH in the latter hedging statistics ranges between 51%percent5151\% to 85%percent8585\% under the BSM and 45%percent4545\% to 76%percent7676\% under the MJD model.
These impressive gains in risk reduction can be attributed to the fact that QDH penalizes equally upside and downside risk,
while on the other hand, SQDH strictly penalizes hedging losses proportionally to their squared values.
Furthermore, hedging statistics also indicate that SQDH policies achieve significant gains under both models and across all hedging instruments with a lesser extend for six options. We observe that hedging with the underlying on a yearly basis result in the most expected gains, followed by monthly underlying, two options and six options. All of these results clearly demonstrate that SQDH policies should be prioritized over QDH policies as they are tailor-made to match the financial objectives of the hedger by always significantly reducing the downside risk as well as earning positive returns on average. [Section 4.4](#S4.SS4 "4.4 Qualitative characteristics of global policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") that follows will shed some light on specific characteristics of the SQDH policies which result in these large average hedging gains and downside risk reduction.
Moreover, it is also interesting to note that the distinct treatment of hedging shortfalls by each penalty has a direct implication on the skewness statistic. Indeed, by strictly optimizing squared hedging losses, SQDH effectively minimize the right tail of hedging errors which entails negative skewness. As for QDH, the positive skewness for all examples can be explained by the fact that the payoff of the lookback option is highly positively asymmetric since it is bounded below at zero and has no upper bound.

Lastly, Coleman et al., ([2007](#bib.bib18)) observed with local risk minimization that while hedging with six options always results in better policies in terms of hedging effectiveness, the relative performance of using yearly ATM call and put options (i.e. two options) or the underlying on a monthly basis depends on the dynamics of the risky asset. The same conclusions can be made from our results obtained with global hedging. Indeed, hedging statistics of both QDH and SQDH policies under the Black-Scholes dynamics in [Table 5](#S4.T5 "In 4.3.2 QDH and SQDH benchmark ‣ 4.3 Benchmarking of hedging policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") show that the downside risk metrics are most often only slightly better with two options as compared to hedging with the underlying on a monthly basis. On the other hand, values from [Table 6](#S4.T6 "In 4.3.2 QDH and SQDH benchmark ‣ 4.3 Benchmarking of hedging policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") indicate that hedging with two options under the MJD model result in downside risk metrics at least two times smaller than with the underlying on a monthly basis for both QDH and SQDH. This observation stems from the fact that hedging with options is significantly more effective than with the underlying in the presence of jump risk. Thus, our results show that the observation made by Coleman et al., ([2007](#bib.bib18)) with respect to the significant improvement in hedging effectiveness of local risk minimization with options in the presence of jump risk also holds for both QDH and SQDH policies.

### 4.4   Qualitative characteristics of global policies

While the previous section assessed the hedging performance of QDH and SQDH with various hedging instruments and different market scenarios, the current section provides insights into specific characteristics of the optimized global policies. The analysis starts off by comparing the average equity risk exposure of QDH and SQDH policies, also called average exposure for convenience, with the same dynamics for the underlying as in previous sections (i.e. BSM and MJD model). The motivation of the latter is to assess if either the MSE or SMSE penalty result in hedging policies more geared towards being long equity risk and are thus earning the equity risk premium.
In this paper, the equity risk exposure is measured as the average portfolio delta over one complete path of the financial market. More formally, for (δtn+1(0:D),δtn+1(B))superscriptsubscript𝛿subscript𝑡𝑛1:0𝐷superscriptsubscript𝛿subscript𝑡𝑛1𝐵(\delta\_{t\_{n+1}}^{(0:D)},\delta\_{t\_{n+1}}^{(B)}) given and fixed, the portfolio delta at the beginning of year tnsubscript𝑡𝑛t\_{n} denoted as Δ~tn(p​f)subscriptsuperscript~Δ𝑝𝑓subscript𝑡𝑛\tilde{\Delta}^{(pf)}\_{t\_{n}} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ~tn(p​f)subscriptsuperscript~Δ𝑝𝑓subscript𝑡𝑛\displaystyle\tilde{\Delta}^{(pf)}\_{t\_{n}} | :=∂Vtnδ∂Stn(0,b)assignabsentsuperscriptsubscript𝑉subscript𝑡𝑛𝛿superscriptsubscript𝑆subscript𝑡𝑛0𝑏\displaystyle:=\frac{\partial V\_{t\_{n}}^{\delta}}{\partial S\_{t\_{n}}^{(0,b)}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∂∂Stn(0,b)​(δtn+1(0:D)∙S¯tn(b)+δtn+1(B)​Btn)absentsuperscriptsubscript𝑆subscript𝑡𝑛0𝑏∙superscriptsubscript𝛿subscript𝑡𝑛1:0𝐷superscriptsubscript¯𝑆subscript𝑡𝑛𝑏superscriptsubscript𝛿subscript𝑡𝑛1𝐵subscript𝐵subscript𝑡𝑛\displaystyle=\frac{\partial}{\partial S\_{t\_{n}}^{(0,b)}}\left(\delta\_{t\_{n+1}}^{(0:D)}\mathchoice{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\displaystyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\textstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\scriptstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{0.5}{$\scriptscriptstyle\bullet$}}}}}\bar{S}\_{t\_{n}}^{(b)}+\delta\_{t\_{n+1}}^{(B)}B\_{t\_{n}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =δtn+1(0)+∑j=1Dδtn+1(j)​Δ~(j),absentsuperscriptsubscript𝛿subscript𝑡𝑛10superscriptsubscript𝑗1𝐷superscriptsubscript𝛿subscript𝑡𝑛1𝑗superscript~Δ𝑗\displaystyle=\delta\_{t\_{n+1}}^{(0)}+\sum\_{j=1}^{D}\delta\_{t\_{n+1}}^{(j)}\tilde{\Delta}^{(j)}, |  |

where Δ~(j)superscript~Δ𝑗\tilde{\Delta}^{(j)} is the jthsuperscript𝑗thj^{\text{th}} option delta (i.e. Δ~(j)=∂Stn(j,b)∂Stn(0,b)superscript~Δ𝑗superscriptsubscript𝑆subscript𝑡𝑛𝑗𝑏superscriptsubscript𝑆subscript𝑡𝑛0𝑏\tilde{\Delta}^{(j)}=\frac{\partial S\_{t\_{n}}^{(j,b)}}{\partial S\_{t\_{n}}^{(0,b)}}). Note that Δ~(j)superscript~Δ𝑗\tilde{\Delta}^{(j)} is time-independent since the calls and puts used for hedging are always of the same characteristics at each trading date (i.e. same moneyness and maturity) and both risky asset models are homoskedastic which entails that the underlying returns have the same conditional distribution for all time-steps. The Δ~(j)superscript~Δ𝑗\tilde{\Delta}^{(j)} can be computed with the well-known closed form solutions under both models. For a total of N~~𝑁\tilde{N} simulated paths, the average exposure is computed as follows:

|  |  |  |
| --- | --- | --- |
|  | Δ¯(p​f):=1N~​N​∑k=1N~∑n=0N−1Δ~tn,k(p​f),assignsuperscript¯Δ𝑝𝑓1~𝑁𝑁superscriptsubscript𝑘1~𝑁superscriptsubscript𝑛0𝑁1subscriptsuperscript~Δ𝑝𝑓  subscript𝑡𝑛𝑘\bar{\Delta}^{(pf)}:=\frac{1}{\tilde{N}N}\sum\_{k=1}^{\tilde{N}}\sum\_{n=0}^{N-1}\tilde{\Delta}^{(pf)}\_{t\_{n},k}, |  |

where Δ~tn,k(p​f)subscriptsuperscript~Δ𝑝𝑓

subscript𝑡𝑛𝑘\tilde{\Delta}^{(pf)}\_{t\_{n},k} is the time-tnsubscript𝑡𝑛t\_{n} portfolio delta of the kthsuperscript𝑘thk^{\text{th}} simulated path. Results presented below for average exposures are from the test set.

#### 4.4.1   Average exposure results

[Table 7](#S4.T7 "In 4.4.1 Average exposure results ‣ 4.4 Qualitative characteristics of global policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") presents average exposures of QDH and SQDH policies with the same market setup as in previous sections with respect to hedging instruments, model parameters and lookback option to hedge. The initial capital investments are again set as the risk-neutral price of the lookback option under each dynamics (i.e. 17.7​$17.7currency-dollar17.7\$ and 25.3​$25.3currency-dollar25.3\$ for BSM and MJD).

Table 7: Average equity exposures with quadratic deep hedging (QDH) and semi-quadratic deep hedging (SQDH) for the lookback option of T=10𝑇10T=10 years under the BSM and MJD model.

|  | BSM | |  | MJD | |
| --- | --- | --- | --- | --- | --- |
|  | QDH | SQDH |  | QDH | SQDH |
| Stock (year) | −0.100.10-0.10 | 0.180.180.18 |  | −0.140.14-0.14 | 0.170.170.17 |
| Stock (month) | −0.100.10-0.10 | −0.010.01-0.01 |  | −0.150.15-0.15 | 0.070.070.07 |
| Two options | −0.120.12-0.12 | −0.060.06-0.06 |  | −0.100.10-0.10 | −0.040.04-0.04 |
| Six options | −0.120.12-0.12 | −0.110.11-0.11 |  | −0.100.10-0.10 | −0.080.08-0.08 |

Notes: Average equity exposures under the BSM and MJD model with S0(0,b)=100superscriptsubscript𝑆00𝑏100S\_{0}^{(0,b)}=100 and r=0.03𝑟0.03r=0.03. Both models dynamics under ℙℙ\mathbb{P} and ℚℚ\mathbb{Q} are described in [Section 4.2](#S4.SS2 "4.2 Dynamics of financial market ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") (see [Table 1](#S4.T1 "In 4.2.4 MJD under ℚ ‣ 4.2 Dynamics of financial market ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") and [Table 2](#S4.T2 "In 4.2.4 MJD under ℚ ‣ 4.2 Dynamics of financial market ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") for parameters values). Initial capital investments are respectively of 17.7​$17.7currency-dollar17.7\$ and 25.3​$25.3currency-dollar25.3\$ under BSM and MJD. Hedging instruments: monthly and yearly underlying, yearly ATM call and put options (two options) and three yearly calls and puts of strikes K={Stn(0,b),1.1​Stn(0,b),1.2​Stn(0,b)}𝐾superscriptsubscript𝑆subscript𝑡𝑛0𝑏1.1superscriptsubscript𝑆subscript𝑡𝑛0𝑏1.2superscriptsubscript𝑆subscript𝑡𝑛0𝑏K=\{S\_{t\_{n}}^{(0,b)},1.1S\_{t\_{n}}^{(0,b)},1.2S\_{t\_{n}}^{(0,b)}\} and K={Stn(0,b),0.9​Stn(0,b),0.8​Stn(0,b)}𝐾superscriptsubscript𝑆subscript𝑡𝑛0𝑏0.9superscriptsubscript𝑆subscript𝑡𝑛0𝑏0.8superscriptsubscript𝑆subscript𝑡𝑛0𝑏K=\{S\_{t\_{n}}^{(0,b)},0.9S\_{t\_{n}}^{(0,b)},0.8S\_{t\_{n}}^{(0,b)}\} (six options). Results for QDH and SQDH are computed based on 75,000

7500075,\!000 independent paths generated from the BSM and MJD model under ℙℙ\mathbb{P}. Training of the neural networks is done as described in [Section 4.1.2](#S4.SS1.SSS2 "4.1.2 LSTM training ‣ 4.1 Market setup ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.").

Numerical results indicate that on average, SQDH policies are significantly more bullish than QDH policies under both dynamics and for all hedging instruments with a lesser extend for six options.
This characteristic of SQDH policies to be more geared towards being long equity risk through a larger average exposure is most important with the underlying on a yearly basis, followed by monthly trading in the underlying, two options and six options. The observation that the average exposure of SQDH policies is only slightly larger than the average exposure of QDH policies when hedging with six options is consistent with benchmarks presented in previous sections.
Indeed, values from [Table 5](#S4.T5 "In 4.3.2 QDH and SQDH benchmark ‣ 4.3 Benchmarking of hedging policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") and [Table 6](#S4.T6 "In 4.3.2 QDH and SQDH benchmark ‣ 4.3 Benchmarking of hedging policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") show that the absolute difference between the hedging statistics of QDH and SQDH is by far the smallest with six options. The latter naturally implies that the hedging positions of quadratic and non-quadratic policies are on average more similar with six options than with the other hedging instruments, which thus results in relatively closer average equity exposure.
One direct implication of the larger average exposure of SQDH policies
is that in the risk management of the lookback option, SQDH
should result in positive expected gains. This was in fact observed in the benchmarking of global policies presented in [Table 5](#S4.T5 "In 4.3.2 QDH and SQDH benchmark ‣ 4.3 Benchmarking of hedging policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") and [Table 6](#S4.T6 "In 4.3.2 QDH and SQDH benchmark ‣ 4.3 Benchmarking of hedging policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") where SQDH resulted in negative mean hedging error statistics (i.e. mean hedging gains) under both risky assets dynamics.
It is worth noting that [Trottier et al., 2018a](#bib.bib51)  developed local risk minimization strategies for long-term options which also earned positive returns on average as well as reduced downside risk as compared to delta-hedging by having larger equity risk exposures.

#### 4.4.2   Analysis of SQDH bullishness

The distinctive feature of SQDH policies to hold a larger average equity exposure than with QDH can firstly be explained by the impact of hedging gains and losses on the optimized policies as measured by each penalty. On the one hand, by minimizing the MSE statistic in a market with positive expected log-returns for the underlying as implied by both models parameters values, QDH policies have to be less bullish whenever the hedging portfolio value at maturity is expected to be larger than the lookback option payoff. On the other hand, SQDH policies are strictly penalized for hedging losses proportionally to their squared values, not for hedging gains. The latter entails that SQDH policies are not constrained to reduce their equity risk exposure when the hedging portfolio value is expected to be larger than the lookback option payoff. The second important factor which contributes to SQDH bullishness specifically when hedging is done with the underlying is the capacity of deep agents to learn to benefit from time diversification of risk. In the context of this study, time diversification of risk refers to the fact that investing in stocks over a long-term horizon reduces the risk of observing large losses as compared to short-term investments. Average exposure values in [Table 7](#S4.T7 "In 4.4.1 Average exposure results ‣ 4.4 Qualitative characteristics of global policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions.") indicate that
deep agents hedging with the underlying and penalized with the SMSE have learned to hold a larger equity risk exposure than under the MSE penalty
to benefit simultaneously from the positive expected returns of the underlying and from the downside risk reduction with time diversification of risk. This observation is most important with the underlying on a yearly basis with SQDH obtaining average exposures of 0.180.180.18 and 0.170.170.17 under respectively the Black-Scholes and the MJD dynamics as compared to −0.100.10-0.10 and −0.140.14-0.14 with QDH.

Moreover, it is very interesting to note that the deep agents rely more on time diversification of risk in the presence of jump risk, i.e. with the MJD dynamics. Indeed,
the average exposure difference between SQDH and QDH policies with the underlying is significantly larger under the MJD dynamics with a difference of 0.310.310.31 and 0.220.220.22 for yearly and monthly trading as compared to 0.280.280.28 and 0.090.090.09 under the BSM.181818
For instance, the average exposure difference between SQDH and QDH with the underlying on a yearly basis under the MJD model is 0.17−(−0.14)=0.310.170.140.310.17-(-0.14)=0.31.
 The latter observations can be explained by the fact that as shown in [Section 4.3.2](#S4.SS3.SSS2 "4.3.2 QDH and SQDH benchmark ‣ 4.3 Benchmarking of hedging policies ‣ 4 Numerical study ‣ Deep Hedging of Long-Term Financial Derivativesfootnote FootnoteFootnoteFootnotesFootnotesfootnoteA GitHub repository with some examples of codes can be found at github.com/alexandrecarbonneau. The author gratefully acknowledges financial support from the Fonds de recherche du Québec (FRQNT). He would also like to thank Frédéric Godin for his helpful comments and suggestions."), hedging only with the underlying in the presence of jump risk is inefficient as compared to hedging with options. Thus, in the presence of jump risk, SQDH agents learn to rely more on time diversification of risk by having on average larger positions in the underlying as compared to SQDH agents trained on a Black-Scholes dynamics.
These findings thus provide additional evidence that the deep hedging algorithm is in fact model-free in the sense that the neural networks are able to effectively adapt their trading policies to different stylized facts of risky asset dynamics only by experiencing simulations of the financial market exhibiting these features.

## 5   Conclusion

This paper studies global hedging strategies of long-term financial derivatives with a reinforcement learning approach. A similar financial market setup to the work of Coleman et al., ([2007](#bib.bib18)) is considered by studying the impact of equity risk with jump risk for the equity on the hedging effectiveness of segregated funds GMMBs. In the context of this paper, the latter guarantee is equivalent to holding a short position in a long-term lookback option of fixed maturity. The deep hedging algorithm of [Buehler et al., 2019a](#bib.bib15)  is applied to optimize long short-term memory networks representing global hedging policies
with the mean-square error (MSE) and semi-mean-square error (SMSE) penalties
and with various hedging instruments (e.g. standard options and the underlying).

Monte Carlo simulations are performed under the Black-Scholes model (BSM) and the Merton jump-diffusion (MJD) model to benchmark the hedging effectiveness of quadratic deep hedging (QDH) and semi-quadratic deep hedging (SQDH). Numerical results showed that under both dynamics and across all trading instruments, SQDH results in hedging policies which simultaneously reduce downside risk and increase expected returns as compared to QDH. The downside risk reduction achieved with SQDH over QDH ranges between 51%percent5151\% to 85%percent8585\% under the BSM and 45%percent4545\% to 76%percent7676\% under the MJD model.
Numerical experiments also indicated that QDH outperforms the local risk minimization scheme of Coleman et al., ([2007](#bib.bib18)) across all downside risk metrics and all hedging instruments. Thus, our results clearly demonstrate that SQDH policies should be prioritized as they are tailor-made to match the financial objectives of the hedger by significantly reducing downside risk as well as resulting in large expected positive returns.

Monte Carlo experiments are also done to provide insight into specific characteristics of the optimized global policies. Numerical results showed that on average, SQDH policies
are significantly more bullish than QDH policies for every example considered.
Analysis presented in this paper indicate that the bullishness of SQDH policies stems from the impact of hedging gains and losses on the optimized policies as measured by each penalty.
Furthermore, an additional factor which contributes to the larger average equity exposure of SQDH policies when hedging with the underlying is the capacity of deep agents to learn to benefit from time diversification of risk. The latter was shown to be most important in the presence of jump risk for the equity where deep agents penalized with the SMSE learned by experiencing many simulations of the financial market to rely more on time diversification risk through larger positions in the underlying as compared to training on the Black-Scholes dynamics due to the lesser efficiency of hedging with the underlying in the presence of jumps.

Further research in the area of global hedging for long-term contingent claims with the deep hedging algorithm would prove worthwhile. The analysis of the impact of additional equity risk factors (e.g. volatility risk and regime risk)
on the optimized policies would be of interest. The same methodological approach presented in this paper could be applied with the addition of the latter equity risk factors with closed to no modification to the algorithm. Moreover, robustness analysis of the optimized policies when dynamics experienced slightly differ from the ones used to train the neural networks would prove worthwhile. The inclusion of realistic transaction costs for each hedging instrument could also be considered following the methodology of the original work of [Buehler et al., 2019a](#bib.bib15) .

## References

* Abadi et al., (2016)

  Abadi, M. et al. (2016).
  Tensorflow: Large-scale machine learning on heterogeneous distributed
  systems.
  arXiv preprint arXiv:1603.04467.
* Almahdi and Yang, (2017)

  Almahdi, S. and Yang, S. Y. (2017).
  An adaptive portfolio trading system: A risk-return portfolio
  optimization using recurrent reinforcement learning with expected maximum
  drawdown.
  Expert Systems with Applications, 87:267–279.
* Ankirchner et al., (2014)

  Ankirchner, S., Schneider, J. C., and Schweizer, N. (2014).
  Cross-hedging minimum return guarantees: Basis and liquidity risks.
  Journal of Economic Dynamics and Control, 41:93–109.
* Augustyniak and Boudreault, (2017)

  Augustyniak, M. and Boudreault, M. (2017).
  Mitigating interest rate risk in variable annuities: An analysis of
  hedging effectiveness under model risk.
  North American Actuarial Journal, 21(4):502–525.
* Augustyniak et al., (2017)

  Augustyniak, M., Godin, F., and Simard, C. (2017).
  Assessing the effectiveness of local and global quadratic hedging
  under GARCH models.
  Quantitative Finance, 17(9):1305–1318.
* Bacinello, (2003)

  Bacinello, A. R. (2003).
  Fair valuation of a guaranteed life insurance participating contract
  embedding a surrender option.
  Journal of risk and insurance, 70(3):461–487.
* Bauer et al., (2008)

  Bauer, D., Kling, A., and Russ, J. (2008).
  A universal pricing framework for guaranteed minimum benefits in
  variable annuities.
  ASTIN Bulletin: The Journal of the IAA, 38(2):621–651.
* Becker et al., (2019)

  Becker, S., Cheridito, P., and Jentzen, A. (2019).
  Deep optimal stopping.
  Journal of Machine Learning Research, 20:1–25.
* Bengio et al., (1994)

  Bengio, Y., Simard, P., and Frasconi, P. (1994).
  Learning long-term dependencies with gradient descent is difficult.
  IEEE transactions on neural networks, 5(2):157–166.
* Bertsimas et al., (2001)

  Bertsimas, D., Kogan, L., and Lo, A. W. (2001).
  Hedging derivative securities and incomplete markets: an
  ϵitalic-ϵ\epsilon-arbitrage approach.
  Operations Research, 49(3):372–397.
* Black and Scholes, (1973)

  Black, F. and Scholes, M. (1973).
  The pricing of options and corporate liabilities.
  Journal of Political Economy, 81(3):637–654.
* Boyle and Hardy, (1997)

  Boyle, P. P. and Hardy, M. R. (1997).
  Reserving for maturity guarantees: Two approaches.
  Insurance: Mathematics and Economics, 21(2):113–127.
* Boyle and Schwartz, (1977)

  Boyle, P. P. and Schwartz, E. S. (1977).
  Equilibrium prices of guarantees under equity-linked contracts.
  Journal of Risk and Insurance, 44:639–660.
* Brennan and Schwartz, (1976)

  Brennan, M. J. and Schwartz, E. S. (1976).
  The pricing of equity-linked life insurance policies with an asset
  value guarantee.
  Journal of Financial Economics, 3(3):195–213.
* (15)

  Buehler, H., Gonon, L., Teichmann, J., and Wood, B. (2019a).
  Deep hedging.
  Quantitative Finance, 19(8):1271–1291.
* (16)

  Buehler, H., Gonon, L., Teichmann, J., Wood, B., Mohan, B., and Kochems, J.
  (2019b).
  Deep hedging: hedging derivatives under generic market frictions
  using reinforcement learning.
  Technical Report 19-80.
* Carbonneau and Godin, (2020)

  Carbonneau, A. and Godin, F. (2020).
  Equal risk pricing of derivatives with deep hedging.
  arXiv preprint arXiv:2002.08492.
* Coleman et al., (2007)

  Coleman, T., Kim, Y., Li, Y., and Patron, M. (2007).
  Robustly hedging variable annuities with guarantees under jump and
  volatility risks.
  Journal of Risk and Insurance, 74(2):347–376.
* Coleman et al., (2006)

  Coleman, T., Li, Y., and Patron, M. (2006).
  Hedging guarantees in variable annuities under both equity and
  interest rate risks.
  Insurance: Mathematics and Economics, 38(2):215–228.
* Delbaen and Schachermayer, (1994)

  Delbaen, F. and Schachermayer, W. (1994).
  A general version of the fundamental theorem of asset pricing.
  Mathematische Annalen, 300(1):463–520.
* Deng et al., (2016)

  Deng, Y. et al. (2016).
  Deep direct reinforcement learning for financial signal
  representation and trading.
  IEEE Transactions on Neural Networks and Learning Systems,
  28(3):653–664.
* Dupuis et al., (2016)

  Dupuis, D., Gauthier, G., and Godin, F. (2016).
  Short-term hedging for an electricity retailer.
  The Energy Journal, 37(2):31–59.
* Föllmer and Schweizer, (1988)

  Föllmer, H. and Schweizer, M. (1988).
  Hedging by sequential regression: An introduction to the mathematics
  of option trading.
  ASTIN Bulletin: The Journal of the IAA, 18(2):147–160.
* François et al., (2014)

  François, P., Gauthier, G., and Godin, F. (2014).
  Optimal hedging when the underlying asset follows a regime-switching
  markov process.
  European Journal of Operational Research, 237(1):312–322.
* Gan, (2013)

  Gan, G. (2013).
  Application of data clustering and machine learning in variable
  annuity valuation.
  Insurance: Mathematics and Economics, 53(3):795–801.
* Glorot and Bengio, (2010)

  Glorot, X. and Bengio, Y. (2010).
  Understanding the difficulty of training deep feedforward neural
  networks.
  In Proceedings of the thirteenth international conference on
  artificial intelligence and statistics, pages 249–256.
* Godin, (2016)

  Godin, F. (2016).
  Minimizing CVaR in global dynamic hedging with transaction
  costs.
  Quantitative Finance, 16(3):461–475.
* Goodfellow et al., (2016)

  Goodfellow, I., Bengio, Y., and Courville, A. (2016).
  Deep learning.
  MIT press.
* Halperin, (2020)

  Halperin, I. (2020).
  Qlbs: Q-learner in the black-scholes (-merton) worlds.
  The Journal of Derivatives.
* Han and E, (2016)

  Han, J. and E, W. (2016).
  Deep learning approximation for stochastic control problems.
  arXiv preprint arXiv:1611.07422.
* Hardy, (2003)

  Hardy, M. (2003).
  Investment guarantees: modeling and risk management for
  equity-linked life insurance, volume 215.
  John Wiley & Sons.
* Hardy, (2000)

  Hardy, M. R. (2000).
  Hedging and reserving for single-premium segregated fund contracts.
  North American Actuarial Journal, 4(2):63–74.
* Harrison and Pliska, (1981)

  Harrison, J. M. and Pliska, S. R. (1981).
  Martingales and stochastic integrals in the theory of continuous
  trading.
  Stochastic Processes and their Applications, 11(3):215–260.
* Hochreiter and Schmidhuber, (1997)

  Hochreiter, S. and Schmidhuber, J. (1997).
  Long short-term memory.
  Neural computation, 9(8):1735–1780.
* Hongkai et al., (2020)

  Hongkai, C., Cui, Z., and Yanchu, L. (2020).
  Discrete-time variance-optimal deep hedging in affine GARCH
  models.
  Working paper.
* Jiang et al., (2017)

  Jiang, Z., Xu, D., and Liang, J. (2017).
  A deep reinforcement learning framework for the financial portfolio
  management problem.
  arXiv preprint arXiv:1706.10059.
* Kélani and Quittard-Pinon, (2017)

  Kélani, A. and Quittard-Pinon, F. (2017).
  Pricing and hedging variable annuities in a Lévy market: a
  risk management perspective.
  Journal of Risk and Insurance, 84(1):209–238.
* Kingma and Ba, (2014)

  Kingma, D. P. and Ba, J. (2014).
  Adam: A method for stochastic optimization.
  arXiv preprint arXiv:1412.6980.
* Kolm and Ritter, (2019)

  Kolm, P. N. and Ritter, G. (2019).
  Dynamic replication and hedging: A reinforcement learning approach.
  The Journal of Financial Data Science, 1(1):159–171.
* Lamberton and Lapeyre, (2011)

  Lamberton, D. and Lapeyre, B. (2011).
  Introduction to stochastic calculus applied to finance.
  Chapman and Hall/CRC.
* Li et al., (2009)

  Li, Y., Szepesvari, C., and Schuurmans, D. (2009).
  Learning exercise policies for american options.
  In Artificial Intelligence and Statistics, pages 352–359.
* Merton, (1976)

  Merton, R. C. (1976).
  Option pricing when underlying stock returns are discontinuous.
  Journal of Financial Economics, 3:125–144.
* Moody and Saffell, (2001)

  Moody, J. and Saffell, M. (2001).
  Learning to trade via direct reinforcement.
  IEEE Transactions on Neural Networks, 12(4):875–889.
* Persson and Aase, (1997)

  Persson, S.-A. and Aase, K. K. (1997).
  Valuation of the minimum guaranteed return embedded in life insurance
  products.
  Journal of Risk and Insurance, 64(4):599–617.
* Powell, (2009)

  Powell, W. B. (2009).
  What you should know about approximate dynamic programming.
  Naval Research Logistics (NRL), 56(3):239–249.
* Rémillard and Rubenthaler, (2013)

  Rémillard, B. and Rubenthaler, S. (2013).
  Optimal hedging in discrete time.
  Quantitative Finance, 13(6):819–825.
* Rockafellar and Uryasev, (2002)

  Rockafellar, R. T. and Uryasev, S. (2002).
  Conditional Value-at-Risk for general loss distributions.
  Journal of Banking & Finance, 26(7):1443–1471.
* Rumelhart et al., (1986)

  Rumelhart, D. E., Hinton, G. E., and Williams, R. J. (1986).
  Learning representations by back-propagating errors.
  Nature, 323(6088):533–536.
* Schweizer, (1991)

  Schweizer, M. (1991).
  Option hedging for semimartingales.
  Stochastic processes and their Applications, 37(2):339–363.
* Schweizer, (1995)

  Schweizer, M. (1995).
  Variance-optimal hedging in discrete time.
  Mathematics of Operations Research, 20(1):1–32.
* (51)

  Trottier, D.-A., Godin, F., and Hamel, E. (2018a).
  Local hedging of variable annuities in the presence of basis risk.
  ASTIN Bulletin: The Journal of the IAA, 48(2):611–646.
* (52)

  Trottier, D.-A., Godin, F., and Hamel, E. (2018b).
  On fund mapping regressions applied to segregated funds hedging under
  regime-switching dynamics.
  Risks, 6(3):78.
* Zhang, (2010)

  Zhang, F. (2010).
  Integrating robust risk management into pricing: New thinking for
  VA writers.
  Risk and Rewards, 55:34–36.

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/2007.15128)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2007.15128)
[View original  
on arXiv](https://arxiv.org/abs/2007.15128)[►](javascript: void(0))