---
authors:
- Jin Ma
- Weixuan Xia
- Jianfeng Zhang
doc_id: arxiv:2512.06309v1
family_id: arxiv:2512.06309
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Wealth or Stealth? The Camouflage Effect in Insider Trading
url_abs: http://arxiv.org/abs/2512.06309v1
url_html: https://arxiv.org/html/2512.06309v1
venue: arXiv q-fin
version: 1
year: 2025
---


Jin Ma111Department of Mathematics, University of Southern California
Email: jinma@usc.edu
  
Weixuan Xia11footnotemark: 1
Email: weixuanx@usc.edu
  
Jianfeng Zhang11footnotemark: 1
Email: jianfenz@usc.edu

(This Version: December 6, 2025)

###### Abstract

We consider a Kyle-type model where insider trading takes place among a potentially large population of liquidity traders and is subject to legal penalties. Insiders exploit the liquidity provided by the trading masses to “camouflage” their actions and balance expected wealth with the necessary stealth to avoid detection. Under a diverse spectrum of prosecution schemes, we establish the existence of equilibria for arbitrary population sizes and a unique limiting equilibrium. A convergence analysis determines the scale of insider trading by a stealth index γ\gamma, revealing that the equilibrium can be closely approximated by a simple limit due to diminished price informativeness. Empirical aspects are derived from two calibration experiments using non-overlapping data sets spanning from 1980 to 2018, which underline the indispensable role of a large population in insider trading models with legal risk, along with important implications for the incidence of stealth trading and the deterrent effect of legal enforcement.

  

JEL Classifications: C73; D82; G14

  

Keywords: Insider trading; stealth trading; large population; civil and criminal penalties; equilibrium convergence; stealth index γ\gamma

## 1 Introduction

The main objective of the present paper is to conduct an in-depth analysis of the intrinsic link between an insider’s trade size choices and the number of liquidity traders (or noise traders) during concurrent trading episodes, in uncovering and quantifying the level of stealth that insiders exercise in illicit trading activity. The central methodology is based on a newly-constructed game-theoretic framework (following Kyle ([1985](https://arxiv.org/html/2512.06309v1#bib.bib28))) for insider trading that adapts to a wide variety of detection mechanisms and penalty functions while incorporating the population size of liquidity traders. In this general setting, the assumption of normally distributed liquidity trades is well supported by the large size of the liquidity trading crowd and the independence among individual trades, and we shall show that an equilibrium exists for any finite population of liquidity traders – a result that is in itself highly nontrivial. As the population size tends to infinity, we also establish the uniqueness of the corresponding limiting equilibrium – a critical outcome of considering the entire trading crowd. The convergence properties lead to the discovery of a stealth index γ\gamma that sets up a rigorous yet simple link between insider trading and stealth trading. Such quantification sheds light upon the prevalence of an often overlooked moderate stealth level in illicit insider trading, revealing an incentive whose dual dependence on both regulatory scrutiny and potential legal penalties illuminates practical interconnections between market behavior and the legal enforcement landscape.

The canonical model of Kyle ([1985](https://arxiv.org/html/2512.06309v1#bib.bib28)) provides a foundational framework for understanding informed trading in financial markets by exploring how an insider (informed trader) with private information about an asset’s value trades strategically to maximize profit. It was demonstrated that the insider’s trades are gradual and proportional to market liquidity, balancing profitability with informational concealment,222Developments in continuous time further highlight a gradual reduction in the tendency to conceal information towards the time when the asset’s value becomes publicly known; see Back ([1992](https://arxiv.org/html/2512.06309v1#bib.bib5)), Back and Baruch ([2004](https://arxiv.org/html/2512.06309v1#bib.bib6)), and Caldentey and Stacchetti ([2010](https://arxiv.org/html/2512.06309v1#bib.bib14)), among others. and the equilibrium reached highlights a tradeoff between information efficiency and risks from market manipulation.

While the Kyle model does not explicitly address illicit insider trading – focusing instead on informational concealment for profit maximization rather than avoidance of legal penalties – many recent studies have advanced the framework to incorporate the modeling of legal risk associated with illicit trading for a comprehensive exploration of the price impact and strategic behavior influenced by the dual objectives of wealth expansion and penalty mitigation. For instance, Carré, Collin-Dufresne, and Gabriel ([2022](https://arxiv.org/html/2512.06309v1#bib.bib15)) explicitly extended Kyle’s one-period model to a setting subject to legal penalties and analyzed insider trading regulations striking a balance between market liquidity and price informativeness, and Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27)), using data sourced from the U.S. Securities and Exchange Commission (SEC) case files across 1995 to 2018, argued that (illegal) insiders adjust trading strategies as they internalize legal risk from regulators, and that legal enforcement is indeed effective in deterring insider trading aggression and containing price informativeness.333Additionally, Çetin ([2025](https://arxiv.org/html/2512.06309v1#bib.bib16)), adopting a continuous-time approach, found that legal risks can impede the optimality for insiders to bring prices to the true valuation at the end of the trading episode.

A notable feature in much of the literature along these lines, whether or not legal risks are considered, is the treatment of non-insider trades collectively as a single entity. In essence, these trades can be thought of as being placed by a single (representative) liquidity (or noise) trader.444For example, in the original Kyle model, liquidity (noise) trading quantities are assumed to be normally distributed; we also refer to Bagnoli, Viswanathan, and Holden ([2001](https://arxiv.org/html/2512.06309v1#bib.bib7)) and Boulatov, Kyle, and Livdan ([2013](https://arxiv.org/html/2512.06309v1#bib.bib11)) regarding the existence and uniqueness properties of a (linear) equilibrium. Indeed, without legal risks, the number of liquidity traders is a relatively minor concern because the only potential harm from insider trading – from an insider’s viewpoint – lies in reduced profits caused by their price impact; as a result, it is optimal to trade at the same scale as the representative liquidity trader, or equivalently, all liquidity traders combined. As legal risks arise, however, (illegal) insiders should suppress their trade sizes further, as trading at comparable levels to the entirety of liquidity traders is likely to expose them to legal repercussions. More precisely, it increases the likelihood of drawing regulatory attention and triggering red flags (see, e.g., Picardo ([2022](https://arxiv.org/html/2512.06309v1#bib.bib33))). This raises the following question: How do insiders exploit the presence of a large crowd of liquidity traders (representing normal trading activity) to moderate their trade sizes, thereby reducing detection risk while simultaneously mitigating price impact to maximize profits? In particular, with a sizeable population of liquidity traders, it can be reasonably suspected that in equilibrium, while insiders still internalize legal risk when devising their trading strategies, they no longer account for the risks through the profit channel, as their consideration of price impact diminishes under the deterrent effect of legal consequences.

Although intuitive and seemingly natural, the understanding that the number of liquidity traders should far exceed that of insider traders – on insider trading days – can be justified by various legal and societal factors. First, laws against insider trading create a high barrier for engaging in it, and criminal and civil penalties, including fines, disgorgement, and prison sentences, deter most traders from engaging in insider trading (see, e.g., Patel and Putņinš ([2021](https://arxiv.org/html/2512.06309v1#bib.bib32)) Sect. 1 and Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27)) Tab. I).555According to recent reports, the SEC prosecuted a total of 583 enforcement actions in 2024, obtaining orders for $8.2 billion in financial remedies. See https://www.sec.gov/newsroom/press-releases/2024-186.
In addition, insider trading is contingent on access to material, non-public information, which is generally restricted to a small group (such as executives and directors) within firms, and only a minority of individuals within companies, or those heavily tied, have access to such sensitive information. Present legal risk, the large pool of liquidity traders can effectively provide insiders with the “necessary” cover to engage in illicit trading, while simultaneously reducing the likelihood of immediate detection, and contrarily, absence of a substantial trading crowd would readily render such illegal activities apparent and swiftly prosecuted, e.g. due to the relatively low costs associated with investigations, including legal and data analysis efforts (Picardo ([2022](https://arxiv.org/html/2512.06309v1#bib.bib33))).

In psychological terms, this phenomenon is commonly known as the “camouflage effect,” which describes situations where individuals blend into a crowd to avoid detection while engaging in wrongful or harmful acts; see, e.g., Griskevicius et al. ([2006](https://arxiv.org/html/2512.06309v1#bib.bib26)). In the insider trading context, this “simple” act of hiding was originally hinted at in the model of Kyle ([1985](https://arxiv.org/html/2512.06309v1#bib.bib28)), with the implication that when maximizing profit, (illicitly) informed traders tend to camouflage their information by splitting up their trades over time, while Admati and Pfeiderer ([1988](https://arxiv.org/html/2512.06309v1#bib.bib2)) argued that the same can also be achieved by purposefully engaging in trading amid high liquidity volume.

Noteworthily, the camouflage effect is closely associated with the well-studied concept of “stealth trading,” where informed traders strategically concentrate their trades in medium sizes. Intuitively, faced with legal risk, informed traders tend to execute volumes smaller than the total volume during periods of heavy trading activity to obscure their identities and reduce the likelihood of detection and prosecution. Meanwhile, driven by a clear profit motive, they are also inclined to trade in significantly larger volumes compared to the average liquidity trader. This phenomenon was early examined in Meulbroek ([1992](https://arxiv.org/html/2512.06309v1#bib.bib29)) in studying the price impact of informed trades using data sourced from the SEC case files over the 1980s. In particular, a notable finding is that the (daily) median ratio of the insider trading volume to the target firms’ total trading volume is about 11%. A later study by Del Guercio, Odders-White, and Ready ([2017](https://arxiv.org/html/2512.06309v1#bib.bib22)), utilizing SEC case files data from 2003 to 2011, has shown a significantly reduced price impact in contrast with the finding of Meulbroek ([1992](https://arxiv.org/html/2512.06309v1#bib.bib29)).666This is ascribed to gradually increased prudence among insiders after 2000, likely in response to enhanced regulatory measures (such as increased regulatory budgets and the introduction of the SEC Whistleblower Program).

This consideration also leads to what is known as the “stealth trading hypothesis” in the literature, originally proposed by Barclay and Warner ([1993](https://arxiv.org/html/2512.06309v1#bib.bib8)) in addressing the issue of informed traders’ choices of trade sizes. The hypothesis predicts that medium-size (precisely defined as 500 to 9,900 shares) trades come with disproportionately large cumulative price changes. Apart from their own empirical evidence from a sample of NYSE firms between 1981 and 1984, there have been numerous studies over the years to confirm the predictions of this hypothesis. To name a few, using audit trail data from NYSE firms, Chakravarty ([2001](https://arxiv.org/html/2512.06309v1#bib.bib18)) highlighted the disproportionately large role played by informed traders utilizing medium-sized trades in driving price movements. Anand and Chakravarty ([2007](https://arxiv.org/html/2512.06309v1#bib.bib4)) confirmed this preference for medium-sized trades in the options markets as well, particularly for high-leverage options. However, it is worth noting that this tendency toward moderate trade sizes is not consistently observed in non-U.S. markets, likely due to elevated levels of price manipulation associated with liquidity trading (see Cai, Cai, and Keasey ([2006](https://arxiv.org/html/2512.06309v1#bib.bib13))). Another empirical study by Frino et al. ([2013](https://arxiv.org/html/2512.06309v1#bib.bib25)) shows that insiders’ trade sizes are largely affected by both the probability of detection and expected penalty, and that insider volumes surpass liquidity trades at the individual level for a specific expected return while falling below the aggregate level.

A natural implication from the last line is that if detection of insider trading is triggered with abnormal order flow imbalances exceeding certain watermarks (see, e.g., DeMarzo, Fishman, and Hagerty ([1998](https://arxiv.org/html/2512.06309v1#bib.bib23)) and Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27)) Sect. II), then it would be optimal for insiders to execute trades at medium levels where normal trades are conspicuous to reduce the likelihood of detection. Alexander and Peterson ([2007](https://arxiv.org/html/2512.06309v1#bib.bib4)) referred to such occurrence as trade-size clustering, documenting that NYSE and NASDAQ trades typically cluster around multiples of 500, 1,000, or 5,000 shares, associated with the greatest price impact, and the clustering strengthens with aggregate trading activity; see also Chen ([2019](https://arxiv.org/html/2512.06309v1#bib.bib20)) for similar considerations for cryptocurrency trading. On the other hand, using futures trading data, Chang, Pinegar, and Schachter ([1997](https://arxiv.org/html/2512.06309v1#bib.bib19)) showed that when large speculative trades are singled out, a significantly stronger price–volume relationship is observed; see also Blau ([2017](https://arxiv.org/html/2512.06309v1#bib.bib10)). The concentration of medium-sized trades has the econometric implication of enhanced sparsity in trade size distributions despite significant overall trading volumes, as modeled and demonstrated by Fei and Xia ([2024](https://arxiv.org/html/2512.06309v1#bib.bib24)). From different angles, these studies consistently support the presence of stealth trading, confirming that informed traders camouflage their activities by favoring medium-sized trades during periods of heavy market activity.

With the above considerations, we aim to develop a Kyle-type model (Section [2](https://arxiv.org/html/2512.06309v1#S2 "2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) with legal penalties (compare Carré, Collin-Dufresne, and Gabriel ([2022](https://arxiv.org/html/2512.06309v1#bib.bib15)) Sect. 2 and Çetin ([2025](https://arxiv.org/html/2512.06309v1#bib.bib16)) Sect. 2) that incorporates the liquidity trading population for a formal study of the camouflage effect in insider trading. We quantify the camouflage effect by introducing a measure termed “stealth index,” gauging the level of stealth (or caution) that insiders exercise in illicit trading (Section [3](https://arxiv.org/html/2512.06309v1#S3 "3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). Determination of this stealth index relies in large part on the convergence of the corresponding equilibria as the liquidity trading population grows, which deciphers how insiders’ trade sizes vary with the number of liquidity traders in addition to the severity of legal penalties. We would like to highlight that the resulting limiting equilibrium can effectively reproduce a significantly reduced price impact which is adequate for practical purposes when justified by the presence of a large trading crowd.

It is worth noting that such a study would not be possible with only a scale parameter tracking the size of all liquidity trades (as adopted in Kyle ([1985](https://arxiv.org/html/2512.06309v1#bib.bib28)) Sect. 2). The reason is that with abnormal order flow imbalance-based detection of insider trading (DeMarzo, Fishman, and Hagerty ([1998](https://arxiv.org/html/2512.06309v1#bib.bib23))), market liquidity is well factored by insiders, whereas regulatory investigations are conducted on a case-by-case basis, i.e., on the individual trader level rather than the volume of trades.777What complicates the investigation process is not the total orders from liquidity traders, but their sheer number, thus giving insiders the opportunity to “camouflage.” Also, given that each liquidity trader places trades independently responding to idiosyncratic needs, the total liquidity order flow is in proportion to their average trade size but not their population size. This means that the particular size of liquidity trades does not directly contribute to the camouflage effect, which requires a sufficiently large population to manifest.888This perspective will be further clarified by the formal mathematical treatment in Section [2](https://arxiv.org/html/2512.06309v1#S2 "2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading").

From a modeling perspective, the present paper also runs parallel to research on regulatory approaches to insider trading, including investigation schemes and the imposition of penalties. We consider a flexible detection mechanism (Section [2.1](https://arxiv.org/html/2512.06309v1#S2.SS1 "2.1 Prosecution mechanism ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) that is adaptive to the detection mechanism postulated by DeMarzo, Fishman, and Hagerty ([1998](https://arxiv.org/html/2512.06309v1#bib.bib23)), who were among the first to consider the optimal design of insider trading regulation. Besides, our choice of the penalty function covers combinations of civil penalties and criminal penalties, with civil penalties determined based on insiders’ illicit trading profit and criminal penalties depending primarily on their trading strategies. Aside from reflecting practical scenarios encompassing both civil and criminal cases (detailed discussion in Section [2.2](https://arxiv.org/html/2512.06309v1#S2.SS2 "2.2 Composition of legal penalties ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), this consideration is broad enough to include most forms of penalty functions discussed in the literature, such as linear penalties (as in Carré, Collin-Dufresne, and Gabriel ([2022](https://arxiv.org/html/2512.06309v1#bib.bib15)) Sect. 3.4.2), quadratic penalties (as in Shin ([1996](https://arxiv.org/html/2512.06309v1#bib.bib35)), Carré, Collin-Dufresne, and Gabriel ([2022](https://arxiv.org/html/2512.06309v1#bib.bib15)) Sect. 3.4.1, and Çetin ([2025](https://arxiv.org/html/2512.06309v1#bib.bib16))), and multiples of illicit profit (as in Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27)) Sect. II).999Notably, while criminal penalties are naturally nondecreasing in the (insider) trading strategy, in the case of civil penalties, the expected penalty function is generally not symmetric or nondecreasing (see Section [4](https://arxiv.org/html/2512.06309v1#S4 "4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), and so it operates outside the framework of Carré, Collin-Dufresne, and Gabriel ([2022](https://arxiv.org/html/2512.06309v1#bib.bib15)) and Çetin ([2025](https://arxiv.org/html/2512.06309v1#bib.bib16)). In Section [3](https://arxiv.org/html/2512.06309v1#S3 "3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), we shall also demonstrate that such a penalty combination is materially significant by both accounting for the nuances of realized illicit gains and assessing the pre-trade intent in determining the appropriate legal charges.

In a theoretical construct, this paper focuses on the following main contributions:

* •

  Construct a Kyle-type model with legal risk incorporating a flexible detection mechanism as well as both civil and criminal penalties, in which the number of liquidity traders can be large (Section [2](https://arxiv.org/html/2512.06309v1#S2 "2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")).
* •

  Propose a stealth index to quantify the camouflage effect in insider trading, implying that in equilibrium, insiders prefer a trading intensity that lies strictly between that of an average liquidity trader and the combined activity of all liquidity traders (Section [3](https://arxiv.org/html/2512.06309v1#S3 "3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") and Section [6](https://arxiv.org/html/2512.06309v1#S6 "6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")).
* •

  Conduct a thorough convergence analysis to show that using the limiting equilibrium (with diminished price impact) as an approximate equilibrium offers great ease in computation while not altering the equilibrium implications (Section [3](https://arxiv.org/html/2512.06309v1#S3 "3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") and Section [6](https://arxiv.org/html/2512.06309v1#S6 "6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")).

Our model is also amenable to calibration to market data on insider trading volumes, while also aligning with unresolved empirical findings from the literature. With the calibration experiments in Section [5](https://arxiv.org/html/2512.06309v1#S5 "5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") based on two data sets, we confirm insiders’ internalization of legal risk from regulators as well as the effectiveness of legal enforcement in deterring insider trading, along with reduced price informativeness (Del Guercio, Odders-White, and Ready ([2017](https://arxiv.org/html/2512.06309v1#bib.bib22)) and Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27))). On the other hand, insiders adjust their trade sizes according to the size of liquidity trades (e.g., Barclay and Warner ([1993](https://arxiv.org/html/2512.06309v1#bib.bib8)) and Chakravarty ([2001](https://arxiv.org/html/2512.06309v1#bib.bib18))) in attempting to disguise their trades for legal risk avoidance, to such extent that their price impact asymptotically vanishes in equilibrium. All main proofs are provided in Appendices [A](https://arxiv.org/html/2512.06309v1#A1 "Appendix A Proof of Proposition 3.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), [B](https://arxiv.org/html/2512.06309v1#A2 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), and [C](https://arxiv.org/html/2512.06309v1#A3 "Appendix C Proof of Theorem 4.2 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), while the proofs of additional results and other auxiliary details are presented in Supplemental Appendices [A](https://arxiv.org/html/2512.06309v1#A1a "Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") and [B](https://arxiv.org/html/2512.06309v1#A2a "Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading").

## 2 A Kyle model with legal risk

We begin with a description of our model framework. Following the standard one-period model of Kyle ([1985](https://arxiv.org/html/2512.06309v1#bib.bib28)), the market features three types of agents trading a single risky asset with fundamental value VV, which is revealed, at time 1, to be 1 with probability 0<p<10<p<1 and 0 otherwise.

There are a total of NN liquidity traders who will trade the asset non-strategically for exogenous needs. At time 0, the liquidity traders have no prior access to the asset value VV and submit independent orders with sizes being i.i.d. random variables with zero mean and variance σ2\sigma^{2}. Thus, with the central limit theorem in place, we assume that the total (net) order flow from liquidity trading can be written as N​W\sqrt{N}W, where W​=d.​Normal​(0,σ2)W\overset{\rm d.}{=}\text{Normal}(0,\sigma^{2}) is independent of VV. There is a single (risk-neutral) insider trader who observes the value VV at time 0 at no cost and in a strategic manner submits his order Z​(V)Z(V) as a function of VV, knowing that placing the order is likely to introduce a contemporary price impact on the risky asset. At time 0, a competitive market maker sees the total (net) order flow N​W+Z​(V)=Y\sqrt{N}W+Z(V)=Y and executes orders at some price P​(Y)P(Y) as a function of YY.101010While taking account of his own price impact, the insider cannot design his trading strategy based on the orders from the liquidity traders; in other words, the insider’s order is submitted no later than the realization of WW.

One major distinction from the standard Kyle model (and its variations with legal risk) is in the population size of liquidity traders NN,111111If the one period (from time 0 to time 1) represents a generic insider trading episode, NN can also be regarded as the total number of liquidity trades, assuming that each trade is placed by a different (liquidity) trader. which we expect to be “very large.” Beyond the practical reasons for a large number of liquidity traders discussed in Section [1](https://arxiv.org/html/2512.06309v1#S1 "1 Introduction ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), a modeling perspective also supports choosing a normal distribution for WW. Indeed, if the population size were small, any specific distributional assumption (whether binomial, uniform, normal, etc.) would risk being overly restrictive; on the other hand, with a sufficiently large population size, independence among the liquidity traders sets the ground for the normal approximation.121212We may use 30 as a practical threshold – following conventional statistical guidelines – to show that the population size is large enough for this approximation to take hold. In our convergence analysis later, however, a larger value of NN may be required to ensure effectiveness of the convergence.

### 2.1 Prosecution mechanism

The insider trader is also aware of legal risk that he faces in the presence of a regulator, who initiates investigations into his trading behavior by various means, such as detections of abnormal trading activity (DeMarzo, Fishman, and Hagerty ([1998](https://arxiv.org/html/2512.06309v1#bib.bib23))), market surveillance associated with corporate events (Patel and Putņinš ([2021](https://arxiv.org/html/2512.06309v1#bib.bib32))), or informant reports (such as the SEC Whistleblower Program). Once an investigation starts, prosecution of the insider will ensue depending on the actual trading behavior. A general description of the prosecution mechanism event could be based on an independent Bernoulli random variable BNB\_{N} with strategy-dependent parameter, 𝓅N\mathcal{p}\_{N}; that is, given his order Z​(V)=zZ(V)=z placed at time 0, the insider will be charged with illicit trading with probability 𝓅N​(z)\mathcal{p}\_{N}(z) at time 1, where the dependence on zz is implied by the regulator gaining access to the insider’s trading account. More precisely, we consider this probability parameter, or the probability of successful prosecution, in the following form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝓅N​(z)=1−e−λN​(z),z∈ℝ,\mathcal{p}\_{N}(z)=1-e^{-\lambda\_{N}(z)},\quad z\in\mathbb{R}, |  | (2.1.1) |

where λN​(z)≥0\lambda\_{N}(z)\geq 0 is interpreted as the hazard rate and is a strictly increasing function in the magnitude of zz; contrarily, 1−𝓅N​(z)=e−λN​(z)1-\mathcal{p}\_{N}(z)=e^{-\lambda\_{N}(z)} is the probability of no investigation or a dismissal from court – or broadly, the corresponding “survival” probability. The structure ([2.1.1](https://arxiv.org/html/2512.06309v1#S2.E1 "In 2.1 Prosecution mechanism ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) allows us to focus on the prosecution intensity, directly related to the likelihood, and it immediately implies that successful prosecution is never guaranteed, which is also practical given the complex circumstances of each insider trading case. Meanwhile, it is important to impose that λN​(0)=0\lambda\_{N}(0)=0, for, if the insider does not trade at all, then there is no room for prosecution, while the increasing feature of λN\lambda\_{N} signifies that aggressive (insider) trading strategies necessarily result in a heightened probability of prosecution.

It is also crucial that the hazard rate (and thus the prosecution probability) explicitly depends on the population size NN, which is to incorporate the idea that the probability of identifying an insider trader should decrease as the total number of normal traders increases. Indeed, a large number of liquidity traders can create an elevated noise level, making it harder to distinguish abnormal trading patterns from normal trading activity. Since the insider’s trades are usually detected as they represent outliers in terms of order flow imbalances (DeMarzo, Fishman, and Hagerty ([1998](https://arxiv.org/html/2512.06309v1#bib.bib23))), with an increasing number of liquidity trades, the threshold for what counts as a statistical outlier also rises, in turn making it more challenging to detect his trades. The insider can then “camouflage” more easily, with his suspicious behavior becoming less conspicuous. To examine the scale effect of NN on the insider’s strategies, we impose a general power-type structure,

|  |  |  |
| --- | --- | --- |
|  | λN​(z)=λ​(N−β​z),\lambda\_{N}(z)=\lambda(N^{-\beta}z), |  |

where λ≡λ1\lambda\equiv\lambda\_{1} is a size-modulated hazard rate and β≥0\beta\geq 0 is a power coefficient governing the scale.

As an important example, the probability of prosecution may be conceptualized as arising from the sequential processes of abnormal order flow imbalance-triggered investigation and subsequent successful legal actions, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝓅N​(z)=D​(N−12​z)​ℙ​{|W+N−12​z|≥y¯},\mathcal{p}\_{N}(z)=D(N^{-\frac{1}{2}}z)\mathbb{P}\{|W+N^{-\frac{1}{2}}z|\geq\bar{y}\}, |  | (2.1.2) |

where D:ℝ↦[0,1]D:\mathbb{R}\mapsto[0,1] is a size-modulated function satisfying that D​(0)=0D(0)=0, representing the probability of prosecution conditional on investigation, and y¯>0\bar{y}>0 is a custom detection threshold. Then, we have the following functional form for the hazard rate:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λN​(z)\displaystyle\lambda\_{N}(z) | =−log⁡(1−𝓅N​(z))\displaystyle=-\log(1-\mathcal{p}\_{N}(z)) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−log⁡(1−D​(N−12​z)2​(erfc​(y¯+N−12​z2​σ2)+erfc​(y¯−N−12​z2​σ2))),\displaystyle=-\log\bigg(1-\frac{D(N^{-\frac{1}{2}}z)}{2}\bigg(\mathrm{erfc}\bigg(\frac{\bar{y}+N^{-\frac{1}{2}}z}{\sqrt{2\sigma^{2}}}\bigg)+\mathrm{erfc}\bigg(\frac{\bar{y}-N^{-\frac{1}{2}}z}{\sqrt{2\sigma^{2}}}\bigg)\bigg)\bigg), |  | (2.1.3) |

where erfc​(⋅)\mathrm{erfc}(\cdot) is the complementary Gauss error function; in this case, β=1/2\beta=1/2 exactly. Detailed derivations are found in Supplemental Appendix [B](https://arxiv.org/html/2512.06309v1#A2 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"). In Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27)), the prosecution probability is precisely 𝓅1\mathcal{p}\_{1} from ([2.1.2](https://arxiv.org/html/2512.06309v1#S2.E2 "In 2.1 Prosecution mechanism ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), except with D∈[0,1]D\in[0,1] being a constant probability.

In general, the power coefficient β\beta allows us to consider a flexible dependence structure of the prosecution probability with respect to the aggregate noise level, which is crucial to examining its impact on the behavior of the insider’s strategy ZZ when the population size becomes large.

### 2.2 Composition of legal penalties

Once successfully prosecuted, the insider trader is subject to legal penalties depending on the jurisdiction and the specific circumstances of the case. First, a common component of insider trading penalties is disgorgement of illicit profits, which involves the return of any profits gained from the illicit trading activity, ensuring unprofitability. The amount of disgorgement is usually calculated based on the total profits earned by the insider, equaling (V−P)​Z​(V)(V-P)Z(V) upon revelation of the asset value.

Another notable aspect is the adoption of so-called “penalty multipliers,” which are imposed in some cases as an enhancement of the deterrent effect of the penalties, based on factors such as the egregiousness of the violation or the level of harm caused to investors or the market. For example, in the U.S., the maximum civil penalty for insider trading is up to three times the profit gained or loss avoided, a.k.a. the “treble damages” provision under the Insider Trading and Securities Fraud Enforcement Act of 1988 (ITSFEA). Similarly, as amended by the ITSFEA, depending on evidence of the insider’s level of intent and trading behavior, significant penalties can be triggered in criminal cases to deter future misconduct; this includes prison sentences and steep fines – e.g., up to 20 years and up to $5 million for individuals in the U.S.

With these factors in mind, we believe that a comprehensive model for legal penalties should allow for explicit dependence on both the insider trader’s illicit profit (as a civil penalty) and his trading strategy (as a criminal penalty). Thus, it is desirable that a penalty function should be a bivariate function of the insider’s trading strategy (zz) as well as his profit gained ((v−P​(y))​z(v-P(y))z), taking the general form C​(z,(v−P​(y))​z)C(z,(v-P(y))z). In the present paper, we focus on the below composition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(z,(v−P​(y))​z)=C0​(z)+χ​((v−P​(y))​z)+,v∈{0,1},C\big(z,(v-P(y))z\big)=C\_{0}(z)+\chi\big((v-P(y))z\big)^{+},\quad v\in\{0,1\}, |  | (2.2.1) |

where (⋅)+(\cdot)^{+} denotes the positive part. On the right side of ([2.2.1](https://arxiv.org/html/2512.06309v1#S2.E1a "In 2.2 Composition of legal penalties ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), the first component with C0C\_{0} incorporates criminal penalties, including imprisonment and fines,131313In the case of imprisonment, C0C\_{0} can be considered equivalent to a capital penalty due to its severe, lifelong impact on one’s economic, social, and personal “capital.” Such an impact could manifest as opportunity costs, social and economic disconnection, lasting stigma, etc. that directly depends on the insider’s trading strategy, while the second stands for civil penalties (with regard to the profit) controlled by a penalty multiplier χ\chi. For a meaningful consideration, we require C0​(z)C\_{0}(z) to be increasing (not necessarily strictly) in the magnitude of zz, and it makes sense to force C0​(0)=0C\_{0}(0)=0 in the case of no trading. Additionally, we require that χ≥1\chi\geq 1, which implies disgorgement of the insider’s illicit profit following successful prosecution.141414This feature is also in keeping with the institutional parametric condition made in Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27)) Sect. II, ensuring a penalty no less than the profit gained. Clearly, when χ=1\chi=1, only C0C\_{0} will remain on top of disgorgement, and penalization is largely strategy-based, while by taking C0≡0C\_{0}\equiv 0, the second component dominates, leading to profit-based (civil) penalties.

### 2.3 Equilibrium definition

With the aforementioned legal risk specifications, we now formulate the insider trader’s optimization problem and give a formal definition of the equilibrium, for any population size NN of liquidity traders.

Accessing the value VV at time 0, the insider trader takes the price function PP from the market maker as given and designs a trading strategy to maximize his expected net profit. His objective function is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | JN​(P;z,v):=𝔼​[(v−P​(N​W+z))​z−𝓅N​(z)​C​(z,(v−P​(N​W+z))​z)],J\_{N}(P;z,v):=\mathbb{E}\Big[(v-P(\sqrt{N}W+z))z~-~\mathcal{p}\_{N}(z)C\big(z,(v-P(\sqrt{N}W+z))z\big)\Big], |  | (2.3.1) |

for z∈ℝz\in\mathbb{R}, v∈{0,1}v\in\{0,1\}, which he seeks to maximize over zz for each value of vv, namely z=Z​(v)z=Z(v). At the same time, given the insider’s trading strategy Z=(Z​(0),Z​(1))Z=(Z(0),Z(1)), the market maker observes the total order flow YY and sets a rational price function for break-even,151515This can be justified by a Bertrand competition argument; see e.g. Kyle ([1985](https://arxiv.org/html/2512.06309v1#bib.bib28)). An alternative interpretation is that the market maker chooses PP to minimize the squared error 𝔼​[(V−P​(N​W+Z​(V)))2]\mathbb{E}[(V-P(\sqrt{N}W+Z(V)))^{2}]. namely setting P​(y)=PN​(Z;y)P(y)=P\_{N}(Z;y), where

|  |  |  |  |
| --- | --- | --- | --- |
|  | PN​(Z;y):=𝔼​[V|N​W+Z​(V)=y],y∈ℝ.P\_{N}(Z;y):=\mathbb{E}\big[V|\sqrt{N}W+Z(V)=y\big],\quad y\in\mathbb{R}. |  | (2.3.2) |

Since VV only takes values 0 and 11, by applying Bayes’ rule, we easily obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | PN​(Z;y)\displaystyle P\_{N}(Z;y) | =ℙ​{V=1|N​W+Z​(V)=y}=p​e−(y−Z​(1))22​N​σ2p​e−(y−Z​(1))22​N​σ2+(1−p)​e−(y−Z​(0))22​N​σ2\displaystyle=\mathbb{P}\big\{V=1|\sqrt{N}W+Z(V)=y\big\}=\frac{pe^{-\frac{(y-Z(1))^{2}}{2N\sigma^{2}}}}{pe^{-\frac{(y-Z(1))^{2}}{2N\sigma^{2}}}+(1-p)e^{-\frac{(y-Z(0))^{2}}{2N\sigma^{2}}}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =11+q​e(2​y−Z​(0)−Z​(1))​(Z​(0)−Z​(1))2​N​σ2,with ​q:=1−pp.\displaystyle=\frac{1}{1+qe^{\frac{(2y-Z(0)-Z(1))(Z(0)-Z(1))}{2N\sigma^{2}}}},\quad\mbox{with }q:=\frac{1-p}{p}. |  | (2.3.3) |

With the population size NN fixed, the (original) hazard rate λN\lambda\_{N} and the liquidity order flow N​W​=d.​Normal​(0,N​σ2)\sqrt{N}W\overset{\rm d.}{=}\text{Normal}(0,N\sigma^{2}) are both well-defined and finite, and the notion of equilibrium can be stated as in the standard Kyle model setting.

###### Definition 2.1.

For any fixed N≥1N\geq 1, an equilibrium is a couple (ZN∗,PN∗)(Z^{\ast}\_{N},P^{\ast}\_{N}) of trading strategy and price function such that:
  
(i) Given PN∗P^{\ast}\_{N}, the insider trader maximizes his expected net profit from trade ([2.3.1](https://arxiv.org/html/2512.06309v1#S2.E1b "In 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | JN​(PN∗;ZN∗​(v),v)=supz∈ℝJN​(PN∗;z,v),v∈{0,1}.J\_{N}(P^{\ast}\_{N};Z^{\ast}\_{N}(v),v)=\sup\_{z\in\mathbb{R}}J\_{N}(P^{\ast}\_{N};z,v),\quad v\in\{0,1\}. |  | (2.3.4) |

(ii) Given ZN∗Z^{\ast}\_{N}, the market maker sets a rational price function for break-even, namely

|  |  |  |
| --- | --- | --- |
|  | PN∗​(y)=PN​(ZN∗;y),y∈ℝ.P^{\ast}\_{N}(y)=P\_{N}(Z^{\ast}\_{N};y),\quad y\in\mathbb{R}. |  |

According to condition (ii) above, for equilibrium analysis it is useful to rewrite the insider’s objective function as

|  |  |  |
| --- | --- | --- |
|  | J´N​(Z;z,v):=JN​(PN​(Z;⋅);z,v),\acute{J}\_{N}(Z;z,v):=J\_{N}(P\_{N}(Z;\cdot);z,v), |  |

where ZZ can be viewed as the market maker’s target strategy. Since VV is supported on {0,1}\{0,1\}, from ([2.3.2](https://arxiv.org/html/2512.06309v1#S2.E2a "In 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) it is clear that 0<PN<10<P\_{N}<1. Then, in light of ([2.2.1](https://arxiv.org/html/2512.06309v1#S2.E1a "In 2.2 Composition of legal penalties ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([2.3.1](https://arxiv.org/html/2512.06309v1#S2.E1b "In 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), regarding the profit maximization ([2.3.4](https://arxiv.org/html/2512.06309v1#S2.E4 "In Definition 2.1. ‣ 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), the insider would rationally concentrate on sell strategies with z≤0z\leq 0 when v=0v=0 and buy strategies with z≥0z\geq 0 when v=1v=1; indeed, by abstaining from trading entirely (z=0z=0), the investor guarantees a nonnegative net profit. However, a zero trading strategy is also trivial on account of legal risk and is demonstrably suboptimal for the insider.161616Under the key Assumption [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), it can be shown that a zero strategy cannot be optimal in equilibrium; see Step 1 in the proof of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") in Appendix [B](https://arxiv.org/html/2512.06309v1#A2 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"). With this consideration in mind, we may assume without loss of generality that the insider’s strategy satisfies the constraint Z=(Z​(0),Z​(1))∈(−∞,0)×(0,∞)Z=(Z(0),Z(1))\in(-\infty,0)\times(0,\infty). As a result, the objective ([2.3.4](https://arxiv.org/html/2512.06309v1#S2.E4 "In Definition 2.1. ‣ 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | J´N​(ZN∗;ZN∗​(v),v)=supz∈ℝvJ´N​(ZN∗;z,v),with ​ℝv:={(−∞,0),if ​v=0,(0,∞),if ​v=1.\acute{J}\_{N}(Z^{\ast}\_{N};Z^{\ast}\_{N}(v),v)=\sup\_{z\in\mathbb{R}\_{v}}\acute{J}\_{N}(Z^{\ast}\_{N};z,v),\quad\text{with }\mathbb{R}\_{v}:=\begin{cases}(-\infty,0),&\;\text{if }v=0,\\ (0,\infty),&\;\text{if }v=1.\end{cases} |  | (2.3.5) |

Besides, with v∈{0,1}v\in\{0,1\} and 0<PN<10<P\_{N}<1, we have in ([2.2.1](https://arxiv.org/html/2512.06309v1#S2.E1a "In 2.2 Composition of legal penalties ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ((v−P​(y))​z)+=(v−P​(y))​z​for all​z∈ℝv,and ​P=PN​(Z;⋅).((v-P(y))z)^{+}=(v-P(y))z~~\mbox{for all}~~z\in\mathbb{R}\_{v},\quad\mbox{and }P=P\_{N}(Z;\cdot). |  | (2.3.6) |

Then, recalling ([2.3.1](https://arxiv.org/html/2512.06309v1#S2.E1b "In 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([2.2.1](https://arxiv.org/html/2512.06309v1#S2.E1a "In 2.2 Composition of legal penalties ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we define the insider’s expected price, expected (gross) profit, and expected additional penalties respectively as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΦN​(Z;z)\displaystyle\varPhi\_{N}(Z;z) | :=𝔼​[PN​(Z;N​W+z)],QN​(Z;z,v):=(v−ΦN​(Z;z))​z,\displaystyle:=\mathbb{E}\big[P\_{N}(Z;\sqrt{N}W+z)\big],\quad Q\_{N}(Z;z,v):=\big(v-\varPhi\_{N}(Z;z)\big)z, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ΨN​(Z;z,v)\displaystyle\varPsi\_{N}(Z;z,v) | :=C0​(z)+(χ−1)​QN​(Z;z,v),\displaystyle:=C\_{0}(z)+(\chi-1)Q\_{N}(Z;z,v), |  | (2.3.7) |

which allow us to recast the objective function ([2.3.1](https://arxiv.org/html/2512.06309v1#S2.E1b "In 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) into the equivalent form

|  |  |  |  |
| --- | --- | --- | --- |
|  | J´N​(Z;z,v)=e−λN​(z)​QN​(Z;z,v)−(1−e−λN​(z))​ΨN​(Z;z,v),z∈ℝv.\acute{J}\_{N}(Z;z,v)=e^{-\lambda\_{N}(z)}Q\_{N}(Z;z,v)-(1-e^{-\lambda\_{N}(z)})\varPsi\_{N}(Z;z,v),\quad z\in\mathbb{R}\_{v}. |  | (2.3.8) |

In particular, ([2.3](https://arxiv.org/html/2512.06309v1#S2.Ex1a "2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) shows that the function ΦN\varPhi\_{N} is precisely the expected value of a Gaussian random variable under a sigmoid-type transformation.171717Despite no known closed form, it can be expressed in terms of an infinite series containing Gaussian moments and explicitly computable coefficients by adopting an expansion argument.

## 3 Limiting equilibrium and convergence

In exercising stealth trading, the insider trader has the tendency to trade in larger quantities compared to a single liquidity trader, while his trade size cannot be “too large” at the same time in view of the risk of detection and prosecution. We again refer to Frino et al. ([2013](https://arxiv.org/html/2512.06309v1#bib.bib25)) Sect. V.B, Meulbroek ([1992](https://arxiv.org/html/2512.06309v1#bib.bib29)) Sect. E and Chakravarty ([2001](https://arxiv.org/html/2512.06309v1#bib.bib18)) for related empirical evidence. This suggests that an insider’s optimal trading strategy should, ideally, scale with the total population size to adequately capture its asymptotic behavior.

From a mathematical viewpoint, in the limit as NN goes to infinity, the optimal trading strategy ZN∗Z^{\ast}\_{N} from Definition [2.1](https://arxiv.org/html/2512.06309v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") can well be infinity. Since we consider power-law growth in the hazard rate, it is reasonable to introduce the scaled strategy Z~N∗=N−γ​ZN∗\tilde{Z}^{\ast}\_{N}=N^{-\gamma}Z^{\ast}\_{N} for some (yet-to-be-determined) coefficient γ≥0\gamma\geq 0, subject to the requirement that the limiting scaled strategy Z~γ∗:=limN→∞Z~N∗\tilde{Z}^{\ast}\_{\gamma}:=\lim\_{N\to\infty}\tilde{Z}^{\ast}\_{N} exist with nonzero values in ℝ0×ℝ1\mathbb{R}\_{0}\times\mathbb{R}\_{1}. In other words, we suspect the insider’s (original) strategy to have the property that ZN∗∼Nγ​Z~γ∗Z^{\ast}\_{N}\sim N^{\gamma}\tilde{Z}^{\ast}\_{\gamma}, i.e., limN→∞ZN∗​(v)/(Nγ​Z~γ∗​(v))=1\lim\_{N\to\infty}Z^{\ast}\_{N}(v)/(N^{\gamma}\tilde{Z}^{\ast}\_{\gamma}(v))=1 for v∈{0,1}v\in\{0,1\}, as N→∞N\to\infty. The coefficient γ\gamma bears direct connections to the camouflage effect as it directly reflects the insider’s desire to balance his wealth expected from illicit trading and his level of stealth to avoid detection and prosecution. A smaller value is associated with a smaller chance of detection, or equivalently, a higher stealth level. In particular, we formally name it the stealth index and, considering the aforementioned moderateness of insider trade sizes, a desirable – but yet-to-be-verified – value range for this index will be (0,1/2)(0,1/2).181818Clearly, γ=0\gamma=0 would imply that the insider’s trade size is comparable to that of a single liquidity trader, while if γ=1/2\gamma=1/2, he would trade at the same scale as all the liquidity traders combined. Nevertheless, in what follows we shall still consider the general value range [0,∞)∋γ[0,\infty)\ni\gamma.

To formalize the notion of a limiting equilibrium based on the scaled trading strategy, Z~=N−γ​Z\tilde{Z}=N^{-\gamma}Z, we need to consider the limit of the price function ([2.3](https://arxiv.org/html/2512.06309v1#S2.Ex1a "2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) as N→∞N\to\infty. Since for zz at the scale of NγN^{\gamma}, y=N​W+zy=\sqrt{N}W+z is at the scale of Nmax⁡{γ,1/2}N^{\max\{\gamma,1/2\}}, we can introduce the scaled order flow y~=N−max⁡{γ,1/2}​y\tilde{y}=N^{-\max\{\gamma,1/2\}}y and re-parameterize the equilibrium price function in ([2.3.2](https://arxiv.org/html/2512.06309v1#S2.E2a "In 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([2.3](https://arxiv.org/html/2512.06309v1#S2.Ex1a "2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | P~Nγ​(Z~;y~)=PN​(Nγ​Z~;Nmax⁡{γ,1/2}​y~),Z~=(Z~​(0),Z~​(1))∈ℝ0×ℝ1,y~∈ℝ.\tilde{P}^{\gamma}\_{N}(\tilde{Z};\tilde{y})=P\_{N}(N^{\gamma}\tilde{Z};N^{\max\{\gamma,1/2\}}\tilde{y}),\quad\tilde{Z}=(\tilde{Z}(0),\tilde{Z}(1))\in\mathbb{R}\_{0}\times\mathbb{R}\_{1},\quad\tilde{y}\in\mathbb{R}. |  | (3.1) |

Throughout the paper, we use the tilde notation (~\tilde{\;}) to indicate the scaled quantities. The next proposition shows that the corresponding limit generally depends on γ\gamma.

###### Proposition 3.1.

For P~Nγ\tilde{P}^{\gamma}\_{N} as in ([3.1](https://arxiv.org/html/2512.06309v1#S3.E1 "In 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), Z~∈ℝ0×ℝ1\tilde{Z}\in\mathbb{R}\_{0}\times\mathbb{R}\_{1},
and y~∈ℝ\tilde{y}\in\mathbb{R}, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limN→∞P~Nγ​(Z~;y~)=P~∞γ​(Z~;y~):={p,if ​γ∈[0,12),P1​(Z~;y~),if ​γ=12,𝟙{2​y~>Z~​(0)+Z~​(1)}+p​𝟙{2​y~=Z~​(0)+Z~​(1)},if ​γ>12.\lim\_{N\to\infty}\tilde{P}^{\gamma}\_{N}(\tilde{Z};\tilde{y})=\tilde{P}^{\gamma}\_{\infty}(\tilde{Z};\tilde{y}):=\begin{cases}p,&\;\text{if }\gamma\in\big[0,\frac{1}{2}\big),\\ P\_{1}(\tilde{Z};\tilde{y}),&\;\text{if }\gamma=\frac{1}{2},\\ \mathds{1}\_{\{2\tilde{y}>\tilde{Z}(0)+\tilde{Z}(1)\}}+p\mathds{1}\_{\{2\tilde{y}=\tilde{Z}(0)+\tilde{Z}(1)\}},&\;\text{if }\gamma>\frac{1}{2}.\end{cases} |  | (3.2) |

Proposition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmproposition1 "Proposition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") demonstrates that for the interesting range γ∈(0,1/2)\gamma\in(0,1/2) of the stealth index, the limiting price function no longer depends on the insider’s trading strategy and is, in particular, constant, equal to the expected value of VV. In the case γ=1/2\gamma=1/2, as the insider trades at the scale of all liquidity trades, the limit is, unsurprisingly, invariant to the population size NN, which can be normalized to 1, as considered in the literature. The case γ>1/2\gamma>1/2 points to an audacious insider trading strategy, with volumes far exceeding typical aggregate levels, and the asset price is set in the usual way (equal to pp) when the market maker perceives no insider involvement, and is otherwise adjusted to the extremal values (0 or 1), making detection and prosecution nearly inevitable (no stealth). This observation suggests [0,1/2]∋γ[0,1/2]\ni\gamma as a plausible range and is to be verified through equilibrium analysis.

The price limits in Proposition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmproposition1 "Proposition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") allow to examine the corresponding limiting behaviors of the expected price, profit, and penalties, ΦN\varPhi\_{N}, QNQ\_{N}, and ΨN\varPsi\_{N} in equilibrium. However, simply analyzing these limits appears to offer little insight into the correct choice of the stealth index γ\gamma from the insider’s perspective. Instead, we shall re-scale the insider’s objective function (or expected net profit): Given a price function P~\tilde{P} on the scaled order flow y~\tilde{y}, we consider the following limiting scaled objective function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | J~∞γ​(P~;z~,v):=limN→∞N−γ​JN​(PNγ;Nγ​z~,v),z~∈ℝv,v∈{0,1},\tilde{J}^{\gamma}\_{\infty}(\tilde{P};\tilde{z},v):=\lim\_{N\to\infty}N^{-\gamma}J\_{N}(P^{\gamma}\_{N};N^{\gamma}\tilde{z},v),\quad\tilde{z}\in\mathbb{R}\_{v},\;v\in\{0,1\}, |  | (3.3) |

where JNJ\_{N} is the original objective function in ([2.3.8](https://arxiv.org/html/2512.06309v1#S2.E8 "In 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), and PNγ​(y):=P~​(N−max⁡{γ,1/2}​y)P^{\gamma}\_{N}(y):=\tilde{P}(N^{-\max\{\gamma,1/2\}}y) is the recovered price function. On the right side of ([3.3](https://arxiv.org/html/2512.06309v1#S3.E3 "In 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), JNJ\_{N} is scaled exactly by N−γN^{-\gamma} because based on ([2.3.8](https://arxiv.org/html/2512.06309v1#S2.E8 "In 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), when PNγ​(y)=PN​(Nγ​Z~;y)P^{\gamma}\_{N}(y)=P\_{N}(N^{\gamma}\tilde{Z};y), the expected price ΦN\varPhi\_{N} is bounded and the expected additional penalty ΨN\varPsi\_{N} must be controlled not to blow up either. Hence, the limiting equilibrium paired with Definition [2.1](https://arxiv.org/html/2512.06309v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") can be defined with γ\gamma chosen such that the limiting objective function ([3.3](https://arxiv.org/html/2512.06309v1#S3.E3 "In 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) is well-defined, and to ensure that the effect of γ\gamma is meaningful, it is important to restrict attention to nonzero limiting strategies as well as nonzero limiting objective function values.

###### Definition 3.1.

A γ\gamma-limiting equilibrium is a couple (Z~γ∗,P~γ∗)(\tilde{Z}^{\ast}\_{\gamma},\tilde{P}^{\ast}\_{\gamma}) of scaled trading strategy and price function such that:
  
(i) The insider trader maximizes his limiting scaled expected net profit ([3.3](https://arxiv.org/html/2512.06309v1#S3.E3 "In 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), i.e.,

|  |  |  |
| --- | --- | --- |
|  | J~∞γ​(P~γ∗;Z~γ∗​(v),v)=supz~∈ℝvJ~∞γ​(P~γ∗;z~,v)≠0,Z~γ∗​(v)≠0,v∈{0,1}.\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\ast}\_{\gamma};\tilde{Z}^{\ast}\_{\gamma}(v),v)=\sup\_{\tilde{z}\in\mathbb{R}\_{v}}\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\ast}\_{\gamma};\tilde{z},v)\neq 0,\quad\tilde{Z}^{\*}\_{\gamma}(v)\neq 0,\quad v\in\{0,1\}. |  |

(ii) The market maker sets a rational price function according to ([3.2](https://arxiv.org/html/2512.06309v1#S3.E2 "In Proposition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), P~γ∗=P~∞γ​(Z~γ∗;⋅)\tilde{P}^{\ast}\_{\gamma}=\tilde{P}^{\gamma}\_{\infty}(\tilde{Z}^{\ast}\_{\gamma};\cdot).

On paper, from the objective function forms ([2.3.8](https://arxiv.org/html/2512.06309v1#S2.E8 "In 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([3.3](https://arxiv.org/html/2512.06309v1#S3.E3 "In 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), a sophisticated choice of the stealth index γ\gamma should exhibit reliance on the growth rate of the size-modulated hazard rate λ\lambda, controlled by β≥0\beta\geq 0, as well as that of the criminal penalty component C0C\_{0}, with respect to the insider’s trading strategy.191919On the other hand, note that from ([2.2.1](https://arxiv.org/html/2512.06309v1#S2.E1a "In 2.2 Composition of legal penalties ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), the civil penalty component is always of linear growth as |z|→∞|z|\to\infty due to the boundedness of the price function PNP\_{N}. Intuitively, with light-to-moderate criminal penalties, the expected price ΦN\varPhi\_{N} tends to overshadow potential legal risk, prompting the insider to trade at larger scales and worry less about being detected, thereby using a larger γ\gamma, while severe criminal penalties are likely to place a deterrent effect on the trading behavior and yields a relatively small γ\gamma. Condition (ii) in Definition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") also reveals that if the insider trader exercises stealth trading with γ<1/2\gamma<1/2, then in the limit of the population size NN, the equilibrium price function becomes constant and decoupled from the trading strategy due to diminished price informativeness (see again Chakravarty ([2001](https://arxiv.org/html/2512.06309v1#bib.bib18)) and Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27))). This decoupling feature significantly simplifies subsequent equilibrium analysis.

The above suggests that the exact structure of the penalty function CC plays an important role in determining the correct stealth index with an increasing population size of liquidity traders. To provide a thorough understanding of convergence towards the limiting equilibria, instead of providing a balanced treatment of all penalty types, the following analysis concentrates on the predominant scenario of civil penalties, which represents the most common enforcement outcome in insider trading cases and matches the empirical nature of the data sets to be presented in Section [5](https://arxiv.org/html/2512.06309v1#S5 "5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"). The examination of scenarios involving criminal and mixed penalties is reserved for further discussions in Section [6](https://arxiv.org/html/2512.06309v1#S6 "6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), also helping align with various cases considered in the literature (Carré, Collin-Dufresne, and Gabriel ([2022](https://arxiv.org/html/2512.06309v1#bib.bib15)), Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27)), and Çetin ([2025](https://arxiv.org/html/2512.06309v1#bib.bib16))), apart from highlighting the technical differences.

## 4 Predominant scenario: Civil penalties

In the predominant scenario, upon successful prosecution, the insider trader faces civil penalties only (as considered in Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27)) Sect. 2). The penalties are imposed on his illicit profit ((V−PN)​Z​(V)(V-P\_{N})Z(V)) through the penalty multiplier χ≥1\chi\geq 1. In the absence of criminal charges, we shall take C0=0C\_{0}=0 in ([2.2.1](https://arxiv.org/html/2512.06309v1#S2.E1a "In 2.2 Composition of legal penalties ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")).

Given a population size N≥1N\geq 1, the equilibrium objective function ([2.3.8](https://arxiv.org/html/2512.06309v1#S2.E8 "In 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) reduces to

|  |  |  |  |
| --- | --- | --- | --- |
|  | J´N​(Z;z,v)\displaystyle\acute{J}\_{N}(Z;z,v) | =e−λN​(z)​QN​(Z;z,v)−(1−e−λN​(z))​ΨN​(Z;z,v)\displaystyle=e^{-\lambda\_{N}(z)}Q\_{N}(Z;z,v)-(1-e^{-\lambda\_{N}(z)})\varPsi\_{N}(Z;z,v) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =e−λN​(z)​QN​(Z;z,v)−χ0​(1−e−λN​(z))​QN​(Z;z,v),z∈ℝv,\displaystyle=e^{-\lambda\_{N}(z)}Q\_{N}(Z;z,v)-\chi\_{0}(1-e^{-\lambda\_{N}(z)})Q\_{N}(Z;z,v),\quad z\in\mathbb{R}\_{v}, |  | (4.1) |

where χ0:=χ−1≥0\chi\_{0}:=\chi-1\geq 0 is the disgorgement-adjusted penalty multiplier. Based on the expression of QNQ\_{N} in ([2.3](https://arxiv.org/html/2512.06309v1#S2.Ex4 "2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), a notable feature of the civil penalties is their explicit dependence on the asset value v∈{0,1}v\in\{0,1\}, and the insider designs his trading strategies knowing that the total order flow (Y=N​W+Z​(V)Y=\sqrt{N}W+Z(V)) observed by the market maker will automatically absorb uncertainty embedded in such strategies.

On a closer look, the expected (additional) penalty ΨN\varPsi\_{N} in ([4](https://arxiv.org/html/2512.06309v1#S4.Ex1 "4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) can increase at most linearly with the insider’s trade size (|z||z|), since the expected price ΦN\varPhi\_{N} is bounded, and more importantly, it is not a monotone function of zz,202020This non-monotonicity property is what makes the structure of civil penalties inherently different from that of criminal penalties – hence not regardable as a special instance of the latter; see Section [6](https://arxiv.org/html/2512.06309v1#S6 "6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"). which arises from a reduction in price informativeness that a significantly larger number of trades placed by the insider inevitably shifts the total order flow towards revelation of the fundamental asset value (VV), thereby pushing the market maker to adjust the price closer to this true value. This adjustment can then substantially reduce or even wipe out the insider’s profit, leading to a smaller penalty (in addition to disgorgement). From another viewpoint, considering that civil penalties are typically less severe than criminal penalties (reserved for serious violations), if only civil penalties are in force, the insider is likely to trade large amounts, knowing that the penalty might decrease as the profits diminish.212121From the proof of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") we shall see that in the present scenario with only civil penalties, for every N≥1N\geq 1 and both v∈{0,1}v\in\{0,1\}, ΨN​(Z;z,v)→0\varPsi\_{N}(Z;z,v)\to 0 as |z|→∞|z|\to\infty, meaning that the insider can technically reduce the penalty to none by increasing his trade size indefinitely. For this reason, sole reliance on profit-based civil penalties may seem “overly idealistic” in that it fails to adequately address and penalize extremely violent insider trading actions, as the absence of significant illicit profit should not absolve the insider of his malicious behavior from the outset. This key observation further motivates a more general consideration combining civil and criminal penalties, to be addressed in Section [6](https://arxiv.org/html/2512.06309v1#S6 "6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading").

To precisely determine the stealth index γ\gamma, we make the following technical assumption on the (size-modulated) hazard rate, which is also essential for establishing existence and uniqueness.

###### Assumption 4.1.

For v∈{0,1}v\in\{0,1\}, λ\lambda is continuously differentiable and convex (not necessarily strictly) on ℝv\mathbb{R}\_{v}, with λ′<0\lambda^{\prime}<0 on (−∞,0)(-\infty,0) and λ′>0\lambda^{\prime}>0 on (0,∞)(0,\infty).

The requirement that λ\lambda be convex (apart from its strict increase) is nonrestrictive, which signifies a growing inclination to detect and prosecute the insider trader as his trade size increases. This is, for example, the case for the order flow imbalance-based detection mechanism (DeMarzo, Fishman, and Hagerty ([1998](https://arxiv.org/html/2512.06309v1#bib.bib23))): For ([2.1](https://arxiv.org/html/2512.06309v1#S2.Ex2 "2.1 Prosecution mechanism ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) one can show that whenever D​(z)=KD​|z|θDD(z)=K\_{D}|z|^{\theta\_{D}} for some KD>0K\_{D}>0 and θD≥1\theta\_{D}\geq 1, then λ′\lambda^{\prime} is guaranteed to be increasing, and |λ′​(z)|≥Kθ′​|z|θD|\lambda^{\prime}(z)|\geq K^{\prime}\_{\theta}|z|^{\theta\_{D}} for some Kθ′>0K^{\prime}\_{\theta}>0. Details are given in Supplemental Appendix [B](https://arxiv.org/html/2512.06309v1#A2a "Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading").

The following theorem, serving as the main result of this section, details the existence and uniqueness of the finite-NN equilibrium and the limiting equilibrium, along with the desired convergence.

###### Theorem 4.1.

Consider the setting of ([4](https://arxiv.org/html/2512.06309v1#S4.Ex1 "4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), and let Assumption [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") hold true. Then, we have the following three assertions.

(i) For every N≥1N\geq 1, there exists an equilibrium (ZN∗,PN∗)(Z^{\ast}\_{N},P^{\ast}\_{N}) in the sense of Definition [2.1](https://arxiv.org/html/2512.06309v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading").
  
(ii) There exists a γ\gamma-limiting equilibrium in the sense of Definition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ=min⁡{β,12}.\gamma=\min\Big\{~\!\beta,~\frac{1}{2}~\!\Big\}. |  | (4.2) |

Moreover, when γ<1/2\gamma<1/2, the γ\gamma-limiting equilibrium (Z~γ∗,P~γ∗)(\tilde{Z}^{\ast}\_{\gamma},\tilde{P}^{\ast}\_{\gamma}) is unique with P~γ∗=p\tilde{P}^{\ast}\_{\gamma}=p.
  
(iii) Let γ<1/2\gamma<1/2 and (Z~γ∗,P~γ∗≡p)(\tilde{Z}^{\ast}\_{\gamma},\tilde{P}^{\ast}\_{\gamma}\equiv p) be the unique γ\gamma-limiting equilibrium from assertion (ii). Then, there exists a constant K>0K>0, depending only on the model parameters but not on NN, such that, for any equilibrium (ZN∗,PN∗)(Z^{\ast}\_{N},P^{\ast}\_{N}) from assertion (i),

|  |  |  |  |
| --- | --- | --- | --- |
|  | |N−γ​ZN∗​(v)−Z~γ∗​(v)|≤K​N2​γ−1,v∈{0,1},|N^{-\gamma}Z^{\ast}\_{N}(v)-\tilde{Z}^{\ast}\_{\gamma}(v)|\leq KN^{2\gamma-1},\quad v\in\{0,1\}, |  | (4.3) |

and, with P~γ∗=p\tilde{P}^{\ast}\_{\gamma}=p,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |PN∗​(y)−p|\displaystyle|P^{\ast}\_{N}(y)-p| | ≤K​(|y|​Nγ−1+N2​γ−1),y∈ℝ,\displaystyle\leq K\big(|y|N^{\gamma-1}+N^{2\gamma-1}\big),\quad y\in\mathbb{R}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |PN∗​(N​W+ZN∗​(V))−p|\displaystyle|P^{\ast}\_{N}(\sqrt{N}W+Z^{\*}\_{N}(V))-p| | ≤K​(|W|​Nγ−1/2+N2​γ−1)≤K​(|W|+1)​Nγ−12,ℙ​-a.s.\displaystyle\leq K\big(|W|N^{\gamma-1/\penalty 502}+N^{2\gamma-1}\big)\leq K(|W|+1)N^{\gamma-\frac{1}{2}},\quad\mathbb{P}\text{-a.s.} |  | (4.4) |

An immediate implication from the first two assertions is that Assumption [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") provides sufficient conditions to ensure the existence of a finite-NN equilibrium and a limiting equilibrium, the latter also being unique when γ<1/2\gamma<1/2 – as is the interesting case with stealth trading. Technically, analyzing the finite-NN equilibrium is significantly more involved than the limiting equilibrium and relies on a key lemma (Lemma [B.1](https://arxiv.org/html/2512.06309v1#A2.Thmlemma1 "Lemma B.1. ‣ Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") in Appendix [B](https://arxiv.org/html/2512.06309v1#A2 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), which elucidates a fundamental property of the function governing the insider’s expected (gross) profit.222222Although this property inherently follows from the normal distribution of total liquidity order flow, it is in fact shared by a broad class of log-concave distributions (including many infinitely divisible distributions); see Saumard and Wellner ([2014](https://arxiv.org/html/2512.06309v1#bib.bib34)) and Yamazato ([1978](https://arxiv.org/html/2512.06309v1#bib.bib36)). Besides, according to ([4.2](https://arxiv.org/html/2512.06309v1#S4.E2 "In Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), the stealth index γ\gamma for the trading strategy is capped at 1/21/2, meaning that the insider deliberately refrains from overly aggressive trading – at quantities exceeding the total orders – inevitably exposing himself.

Assertion (iii) from Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") expounds the convergence of any finite-NN equilibrium towards the (unique) γ\gamma-limiting equilibrium, in terms of both the insider’s optimal strategy and the market maker’s price function, on the assumption that γ<1/2\gamma<1/2. For the price function, the rate of convergence, identified as the inverse power of NN, is γ−1/2<0\gamma-1/2<0, proportionate to the stealth index γ\gamma. The intuition behind this is clear: As γ↘0\gamma\searrow 0, the insider’s trade size, scaled to match that of a single liquidity trader, becomes negligible within the total order flow, leaving the population size NN as the dominant factor; conversely, as γ↗1/2\gamma\nearrow 1/2, the trade size effectively matches the entire population of liquidity traders, nullifying the size impact, and convergence is out of question.

The convergence rate (2​γ−12\gamma-1) for the insider’s optimal strategies is proportionally related to how the population size obscures investigation and prosecution, as measured by the coefficient β\beta, and stems directly from the convergence of the price function. An important regulatory insight from this result is that the intensity of investigation (linked to β\beta) can significantly impact how closely insiders’ trade sizes approach their limit associated with diminished price impact. More specifically, when investigations are highly effective (β=0\beta=0) – nearly unaffected by the trading population – informed traders’ strategies tend to converge rapidly for any given stealth level and are driven by the price function’s behavior.

Pertaining to Definition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") further demonstrates that if γ\gamma happens to be less than 1/21/2, the limiting equilibrium price function becomes constant, decoupled from insider trading information, hence making itself much easier to analyze than that with a finite population, which is even explicitly solvable in specific settings. We give the following illustrative example, which considers a quadratic hazard rate while adhering to the “treble damages” provision. The proof is given in Supplemental Appendix [B](https://arxiv.org/html/2512.06309v1#A2a "Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading").

###### Example 4.1.

Let p∈(0,1)p\in(0,1) be arbitrary, and let λ​(z)=z2\lambda(z)=z^{2} (satisfying Assumption [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and χ=3\chi=3. Suppose that γ=β∈[0,1/2)\gamma=\beta\in[0,1/2). Then, the γ\gamma-limiting equilibrium is uniquely determined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z~γ∗=(−12−W0​(e3),12−W0​(e3))≈(−0.350753,0.350753),P~γ∗=p,\tilde{Z}^{\ast}\_{\gamma}=\Big(-\sqrt{\tfrac{1}{2}-\mathrm{W\_{0}}\big(\tfrac{\sqrt{e}}{3}\big)},\sqrt{\tfrac{1}{2}-\mathrm{W\_{0}}\big(\tfrac{\sqrt{e}}{3}\big)}~\Big)\approx(-0.350753,0.350753),\quad\tilde{P}^{\ast}\_{\gamma}=p, |  | (4.5) |

where W0​(⋅)\mathrm{W}\_{0}(\cdot) denotes the Lambert W\mathrm{W} function (a.k.a. the product logarithm).

An interesting observation in Example [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmexample1 "Example 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") is that regardless of the probability pp of revealing the asset value V=1V=1, at equilibrium, the insider sticks to trading the same amount in both states (|Z~γ∗​(0)|=Z~γ∗​(1)|\tilde{Z}^{\ast}\_{\gamma}(0)|=\tilde{Z}^{\ast}\_{\gamma}(1)). An explanation is that as the civil penalties are tied to the insider’s illicit profit, they can effectively remove his incentive to compare and exploit the price differences in the two states, even though the contingent expected profits may still be different.

Following Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), the approximation power of the limiting equilibrium towards any finite-population equilibrium can be further illuminated with the concept of ϵ\epsilon-equilibria, connected to Definition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), which we show in Definition [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmdefinition1 "Definition 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading").232323Generally speaking, the convergence of non-unique equilibria in stronger senses (e.g., with respect to the Hausdorff distance) cannot be established without imposing additional technical conditions. A thorough exploration of this convergence issue in the insider trading context is left for further research.

###### Definition 4.1.

For any fixed N≥1N\geq 1 and ϵ≥0\epsilon\geq 0, an ϵ\epsilon-equilibrium is a couple (ZN∗,ϵ,PN∗,ϵ)(Z^{\ast,\epsilon}\_{N},P^{\ast,\epsilon}\_{N}) of trading strategy and price function such that, based on ([2.3](https://arxiv.org/html/2512.06309v1#S2.Ex1a "2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), ([3.1](https://arxiv.org/html/2512.06309v1#S3.E1 "In 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), and ([3.3](https://arxiv.org/html/2512.06309v1#S3.E3 "In 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | N−γ​JN​(PN∗,ϵ;ZN∗,ϵ​(v),v)≥supz∈ℝvN−γ​JN​(PN∗,ϵ;z,v)−ϵ,v∈{0,1},N^{-\gamma}J\_{N}(P^{\ast,\epsilon}\_{N};Z^{\ast,\epsilon}\_{N}(v),v)\geq\sup\_{z\in\mathbb{R}\_{v}}N^{-\gamma}J\_{N}(P^{\ast,\epsilon}\_{N};z,v)-\epsilon,\quad v\in\{0,1\}, |  | (4.6) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | |PN∗,ϵ​(Nmax⁡{γ,12}​y~)−PN​(ZN∗,ϵ;Nmax⁡{γ,12}​y~)|≤ϵ​(1+|y~|),y~∈ℝ.|P^{\ast,\epsilon}\_{N}(N^{\max\{\gamma,\frac{1}{2}\}}\tilde{y})-P\_{N}(Z^{\ast,\epsilon}\_{N};N^{\max\{\gamma,\frac{1}{2}\}}\tilde{y})|\leq\epsilon(1+|\tilde{y}|),\quad\tilde{y}\in\mathbb{R}. |  | (4.7) |

We have the next important result about the approximation of any finite-population equilibrium via an arbitrary limiting equilibrium, with no uniqueness required.

###### Theorem 4.2.

Consider the setting of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") assertion (iii), with γ<1/2\gamma<1/2 and (Z~γ∗,p)(\tilde{Z}^{\ast}\_{\gamma},p) being the unique γ\gamma-limiting equilibrium. Then, for every N≥1N\geq 1, (Nγ​Z~γ∗,p)(N^{\gamma}\tilde{Z}^{\ast}\_{\gamma},p) is an ϵN\epsilon\_{N}-equilibrium in the sense of Definition [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmdefinition1 "Definition 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), where for some constant KK depending only on the model parameters,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵN=K​Nγ−12.\epsilon\_{N}=KN^{\gamma-\frac{1}{2}}. |  | (4.8) |

Theorem [4.2](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") asserts that any limiting equilibrium defined under Definition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") automatically qualifies as an ϵN\epsilon\_{N}-equilibrium within the actual, finitely populated market, for which the magnitude of ϵN\epsilon\_{N}, as a function of the population size NN, carries the same economic implications in terms of the stealth index γ\gamma as the equilibrium strategies. The statement highlights the central idea that the limiting equilibrium is a practical and robust approximation across a wide range of detection schemes, whenever the population of liquidity traders is justifiably large enough.

## 5 Empirical perspectives

In this section, we address the issue of estimating the population size of liquidity traders, NN, and the stealth index γ\gamma, using available data on insider trading cases. The main idea of this empirical analysis, as mentioned in Section [1](https://arxiv.org/html/2512.06309v1#S1 "1 Introduction ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), is to verify that the population of liquidity traders is, as expected, considerably large for any generic risky asset and – more importantly – that insiders favor trading with medium intensity (compared to all liquidity traders present in the same trading episodes) in the presence of legal risk by adopting a moderate stealth level, therefore confirming the deterrent effect of legal risk on insiders’ trade size choices, associated with diminished price informativeness (as implied from the convergence properties in Section [3](https://arxiv.org/html/2512.06309v1#S3 "3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")); see, again, Barclay and Warner ([1993](https://arxiv.org/html/2512.06309v1#bib.bib8)), Chakravarty ([2001](https://arxiv.org/html/2512.06309v1#bib.bib18)), and Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27)). We conduct the analysis with two calibration experiments, which rely on different calibration conditions and yet confirm the same phenomena of interest.

### 5.1 Calibration experiment I

Our first calibration experiment makes use of insider trading volume data collected and analyzed in one of the earliest financial studies of its kind, conducted by Meulbroek ([1992](https://arxiv.org/html/2512.06309v1#bib.bib29)). Specifically, the data set consists of a list of 320 defendants formally charged with insider trading by the SEC in civil or administrative cases from 1980 to 1989, with the (daily) trading volumes for these defendants sourced from (both public and non-public) SEC documents, along with the target firms’ total trading volumes on the days of insider trading (sourced from Iterative Data Services’ Investment Statistical Listing Tapes and from S&P’s Daily Stock Price Record).242424A more detailed breakdown of the data set, including a yearly analysis of reported insider trading volumes, can be found in Meulbroek ([1992](https://arxiv.org/html/2512.06309v1#bib.bib29)) Tab. I.

Table [1](https://arxiv.org/html/2512.06309v1#S5.T1 "Table 1 ‣ 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") summarizes useful statistics for this data set, extracted from Meulbreuk ([1992](https://arxiv.org/html/2512.06309v1#bib.bib29)) Sect. III.E. It is worth mentioning that the data set only covers detected insider trading violations (as reported to the SEC), and the volumes are precisely those traded by the defendants (who have been detected and prosecuted), while much insider trading remains undetected over the observation period. On average, the (detected) insider trading volume constitutes about 8% of the total volume, both in terms of shares traded and dollar value, and so we shall utilize the share volume statistics exclusively.

Table 1: Statistics for (daily) insider trading volume data (1980–1989)
  
(Source: Meulbroek ([1992](https://arxiv.org/html/2512.06309v1#bib.bib29)))

| Average insider share volume | 9,819 |
| --- | --- |
| Average insider dollar volume | $300,023 |
| Average total share volume | 113,909 |
| Standard error for average total share volume | 10,246 |
| Average total dollar volume | $4,121,533 |
| Standard error for average total dollar volume | $594,327 |
| Median insider-to-total volume ratio | 11.3% |

Under the equilibrium model framework, we adopt a method-of-moment-type estimation approach, which starts by deriving the theoretical counterparts of the statistics in Table [1](https://arxiv.org/html/2512.06309v1#S5.T1 "Table 1 ‣ 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") as functions of NN and γ\gamma, and then setting them to be equal to the sample statistics, respectively, on the assumption that the underlying economy is in equilibrium. It is hence understood that the (single) insider trader in our model acts as a representative agent of insider trading during any insider trading episode, with NN tracking the relative size of liquidity (non-inside or normal) traders compared to insiders. Also, as only defendants formally charged with insider trading are included in the data set, the statistics must be interpreted as conditional on prosecution – the reported average insider volumes exclude undetected or unprosecuted cases and unequivocally underestimate the actual insider trading volumes.

The theoretical counterparts of the above statistics are tractable to compute within the model by appealing to the approximate normality in the effect of large NN, as discussed below; detailed derivations are in Supplemental Appendix [B](https://arxiv.org/html/2512.06309v1#A2a "Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"). Recall that BNB\_{N} is the (independent) Bernoulli random variable representing the prosecution mechanism (see ([2.1.1](https://arxiv.org/html/2512.06309v1#S2.E1 "In 2.1 Prosecution mechanism ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"))). Then, given the insider’s strategy ZZ, the estimated prosecution probability is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​{BN​(Z​(V))=1}=∑v=01p​(v)​(1−e−λN​(Z​(v))),with​p​(v):={1−p,if ​v=0,p,if ​v=1.\mathbb{P}\big\{B\_{N}(Z(V))=1\big\}=\sum^{1}\_{v=0}p(v)(1-e^{-\lambda\_{N}(Z(v))}),\quad\mbox{with}~p(v):=\begin{cases}1-p,&~\text{if }v=0,\\ p,&~\text{if }v=1.\end{cases} |  | (5.1.1) |

The average insider trading volume (in shares) corresponds to the conditional expectation of the (representative) insider’s trade size upon successful prosecution, namely

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|Z​(V)||BN​(Z​(V))=1]=∑v=01p​(v)​|Z​(v)|​(1−e−λN​(Z​(v)))∑v=01p​(v)​(1−e−λN​(Z​(v))).\mathbb{E}\Big[|Z(V)|\big|B\_{N}(Z(V))=1\Big]=\frac{\sum^{1}\_{v=0}p(v)|Z(v)|\big(1-e^{-\lambda\_{N}(Z(v))}\big)}{\sum^{1}\_{v=0}p(v)\big(1-e^{-\lambda\_{N}(Z(v))}\big)}. |  | (5.1.2) |

To construct a meaningful match for the average total volume (in shares), let us recall that according to the model framework (Section [2](https://arxiv.org/html/2512.06309v1#S2 "2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), all the liquidity traders place independent orders, each with zero mean and variance σ2\sigma^{2}. Assuming that such orders are successfully filled, a reasonable proxy for the total liquidity volume is then the absolute sum of these independent random variables, and by the central limit theorem again, this sum can be approximated by a normal random variable XN​=d.​Normal​(N​μ,N​(σ2−μ2))X\_{N}\overset{\rm d.}{=}\text{Normal}(N\mu,N(\sigma^{2}-\mu^{2})) for some parameter μ>0\mu>0 (again, under the large-NN assumption).252525As each liquidity trader places an order ξi\xi\_{i}, i=1,…,Ni=1,\dots,N, i.i.d. with zero mean and variance σ2\sigma^{2}, the total liquidity order flow is ∑i=1Nξi≈N​W\sum^{N}\_{i=1}\xi\_{i}\approx\sqrt{N}W (assuming that NN is large), while the total liquidity volume is approximated as ∑i=1N|ξi|=XN\sum^{N}\_{i=1}|\xi\_{i}|=X\_{N}. Also, with 𝔼​[|ξ1|]=μ\mathbb{E}[|\xi\_{1}|]=\mu, we have Var​(|ξ1|)=𝔼​[ξ12]−𝔼​[|ξ1|]2=σ2−μ2\mathrm{Var}(|\xi\_{1}|)=\mathbb{E}[\xi^{2}\_{1}]-\mathbb{E}[|\xi\_{1}|]^{2}=\sigma^{2}-\mu^{2}. This coefficient, which depends on the exact trade distribution of an average liquidity trader, is yet to be determined, while for now we take it as given. Hence, the average total volume (in shares) should be matched to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[XN+|Z​(V)||BN​(Z​(V))=1]=N​μ+∑v=01p​(v)​|Z​(v)|​(1−e−λN​(Z​(v)))∑v=01p​(v)​(1−e−λN​(Z​(v))).\mathbb{E}\Big[X\_{N}+|Z(V)|\big|B\_{N}(Z(V))=1\Big]=N\mu+\frac{\sum^{1}\_{v=0}p(v)|Z(v)|\big(1-e^{-\lambda\_{N}(Z(v))}\big)}{\sum^{1}\_{v=0}p(v)\big(1-e^{-\lambda\_{N}(Z(v))}\big)}. |  | (5.1.3) |

For the insider-to-total volume ratio, it is more convenient to consider its reciprocal (“total-to-insider volume ratio”), whose conditional tail distribution function on prosecution is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​{XN+|Z​(V)||Z​(V)|>x|BN​(Z​(V))=1}=∑v=01p​(v)​(1−e−λN​(Z​(v)))​erfc​|Z​(v)|​(x−1)−N​μ2​N​σ22​∑v=01p​(v)​(1−e−λN​(Z​(v))),x≥1.\mathbb{P}\bigg\{\frac{X\_{N}+|Z(V)|}{|Z(V)|}>x\Big|B\_{N}(Z(V))=1\bigg\}=\frac{\sum^{1}\_{v=0}p(v)\big(1-e^{-\lambda\_{N}(Z(v))}\big)\mathrm{erfc}\frac{|Z(v)|(x-1)-N\mu}{\sqrt{2N\sigma^{2}}}}{2\sum^{1}\_{v=0}p(v)\big(1-e^{-\lambda\_{N}(Z(v))}\big)},\;\;x\geq 1. |  | (5.1.4) |

Since the data set focuses on civil cases with pecuniary charges only, we follow the setting of Example [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmexample1 "Example 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") to design our calibration experiment (with γ=β\gamma=\beta). Assuming market efficiency, we fix the probability of revealing the upstate (V=1V=1) at p=1/2p=1/2. The consideration of a quadratic (size-modulated) hazard rate λ​(z)=K​z2\lambda(z)=Kz^{2}, z∈ℝz\in\mathbb{R}, for some K>0K>0, agrees with the tail behaviors of ([2.1](https://arxiv.org/html/2512.06309v1#S2.Ex2 "2.1 Prosecution mechanism ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) for abnormal order flow imbalance-based detection and can be seen as a reasonable approximation of the latter, and we have further K=1/(2​σ2)K=1/(2\sigma^{2}); see Supplemental Appendix [B](https://arxiv.org/html/2512.06309v1#A2a "Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") for details. For civil penalties, we emphasize the “treble damages” provision again by testing three values of the penalty multiplier: χ∈{1,2,3}\chi\in\{1,2,3\} (or χ0∈{0,1,2}\chi\_{0}\in\{0,1,2\}).

If NN happens to be large, then according to assertion (iii) in Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") and Theorem [4.2](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), we can take the re-scaled limiting equilibrium (Nγ​Z~γ∗,P~γ∗)(N^{\gamma}\tilde{Z}^{\ast}\_{\gamma},\tilde{P}^{\ast}\_{\gamma}) as a reasonable approximation for the actual (finite-NN) equilibrium (ZN∗,PN∗)(Z^{\ast}\_{N},P^{\ast}\_{N}). This implicit assumption can be verified posteriorly after the calibration. In the limiting case, with the above specified parameters, by following Example [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmexample1 "Example 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") we obtain the following insider trading strategy at equilibrium:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Z~γ∗​(0),Z~γ∗​(1))=(−σ×𝔞,σ×𝔞),with ​𝔞=1−2​W0​(e​χ02​χ),(\tilde{Z}^{\ast}\_{\gamma}(0),\tilde{Z}^{\ast}\_{\gamma}(1))=(-\sigma\times\mathfrak{a},\sigma\times\mathfrak{a}),\quad\text{with }\mathfrak{a}=\sqrt{1-2\mathrm{W}\_{0}\big(\tfrac{\sqrt{e}\chi\_{0}}{2\chi}\big)}, |  | (5.1.5) |

which is proportional to σ\sigma, i.e., the trade size of an average liquidity trader, with a constant limiting price function P~γ∗=1/2\tilde{P}^{\ast}\_{\gamma}=1/2.

Next, we make the substitution Z=Nγ​Z~γ∗Z=N^{\gamma}\tilde{Z}^{\ast}\_{\gamma} from ([5.1.5](https://arxiv.org/html/2512.06309v1#S5.E5 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) in ([5.1.2](https://arxiv.org/html/2512.06309v1#S5.E2 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), ([5.1.3](https://arxiv.org/html/2512.06309v1#S5.E3 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), and ([5.1.4](https://arxiv.org/html/2512.06309v1#S5.E4 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), and then establish three calibration conditions by equating ([5.1.2](https://arxiv.org/html/2512.06309v1#S5.E2 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([5.1.3](https://arxiv.org/html/2512.06309v1#S5.E3 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) to the numbers 9819 and 113909, respectively, and setting ([5.1.4](https://arxiv.org/html/2512.06309v1#S5.E4 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) to be equal to 1/21/2 for x=1/11.3%x=1/11.3\%. However, it turns out that under ([5.1.5](https://arxiv.org/html/2512.06309v1#S5.E5 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), these conditions are not able to determine the values of NN and σ\sigma simultaneously, because the latter is inherently a scaling factor for the total order flow. Instead, since NN and σ\sigma clearly exhibit an inverse relationship, it is always possible to obtain a lower bound estimate for NN by imposing an upper bound on σ\sigma. In accordance with the standard 100 round lot in the U.S. as well as the phenomenon of trade-size clustering (Alexander and Peterson ([2007](https://arxiv.org/html/2512.06309v1#bib.bib3))), we set σ=1000\sigma=1000, which is a conservative enough estimate in this context given the (daily) average price around $36.18 traded during the observation period – amounting to $36,180 worth of trades placed per trader each day. Using smaller values of σ\sigma will necessarily lead to NN increasing, to which the value of γ\gamma (as a power coefficient) is also resistant.

In addition, while the additional parameter μ>0\mu>0 may be determined in several ways, we prefer to take on a direct approach leveraging the standard deviation of the total volume in the same data set, estimated to be 248,452; again, see Supplemental Appendix [B](https://arxiv.org/html/2512.06309v1#A2a "Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") for details. By equating the standard deviation of XNX\_{N}, or N​(σ2−μ2)\sqrt{N(\sigma^{2}-\mu^{2})}, to this value and using the calibration condition from ([5.1.3](https://arxiv.org/html/2512.06309v1#S5.E3 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we arrive at an estimate μ^≈1.68625\hat{\mu}\approx 1.68625.262626The estimate is numerically stable – using the more complex conditions ([5.1.2](https://arxiv.org/html/2512.06309v1#S5.E2 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) or ([5.1.4](https://arxiv.org/html/2512.06309v1#S5.E4 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) instead of ([5.1.3](https://arxiv.org/html/2512.06309v1#S5.E3 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) produces similar values in the range [1,2][1,2], and so for succinctness we stick with this estimate. This estimate is in keeping with the significant asymmetric and leptokurtic feature of trading volumes, which is a well-documented phenomenon in market microstructure; see, e.g., Mike and Farmer ([2008](https://arxiv.org/html/2512.06309v1#bib.bib30)) and Çetin and Waelbroeck ([2024](https://arxiv.org/html/2512.06309v1#bib.bib17)).272727This phenomenon indicates that while many trading episodes carry small or no trades, a few episodes contain very large trades, which also closely reflects the aforementioned trade size clustering (e.g., Chang, Pinegar, and Schachter ([1997](https://arxiv.org/html/2512.06309v1#bib.bib19)), Alexander and Peterson ([2007](https://arxiv.org/html/2512.06309v1#bib.bib4)), and Fei and Xia ([2024](https://arxiv.org/html/2512.06309v1#bib.bib24))). Notably, the heavy-tailed behavior does not conflict with the approximate-normality treatment for the present analysis, as the stated statistics are not tail-dependent and thus robust; indeed, replacing normality with a heavy-tailed distribution for XNX\_{N} yields virtually no change to the results to follow. In particular, at the individual level, the average trading volume is exceeded substantially by its standard deviation (σ\sigma) in value, the relative smallness persisting with smaller values of σ\sigma. Then, by setting μ=1.68625\mu=1.68625 and σ=1000\sigma=1000, we continue to solve exactly two calibration conditions at a time and compare the parameter estimates (N^,γ^)(\hat{N},\hat{\gamma}). Results are reported in Table [2](https://arxiv.org/html/2512.06309v1#S5.T2 "Table 2 ‣ 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading").

Table 2: Results on calibration experiment I

| Equations used | | ([5.1.2](https://arxiv.org/html/2512.06309v1#S5.E2 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([5.1.3](https://arxiv.org/html/2512.06309v1#S5.E3 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) | ([5.1.2](https://arxiv.org/html/2512.06309v1#S5.E2 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([5.1.4](https://arxiv.org/html/2512.06309v1#S5.E4 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) | ([5.1.3](https://arxiv.org/html/2512.06309v1#S5.E3 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([5.1.4](https://arxiv.org/html/2512.06309v1#S5.E4 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) |
| --- | --- | --- | --- | --- |
| (N^,γ^)(\hat{N},\hat{\gamma}) | χ=1\chi=1 | (61729,0.207091)(61729,0.207091) | (45708,0.21289)(45708,0.21289) | (59918,0.23226)(59918,0.23226) |
| χ=2\chi=2 | (61729,0.249565)(61729,0.249565) | (45708,0.256553)(45708,0.256553) | (59918,0.274849)(59918,0.274849) |
| χ=3\chi=3 | (61729,0.270651)(61729,0.270651) | (45708,0.27823)(45708,0.27823) | (59918,0.295992)(59918,0.295992) |

Table [2](https://arxiv.org/html/2512.06309v1#S5.T2 "Table 2 ‣ 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") shows that estimates for the stealth index γ\gamma are quite robust when using different calibration conditions, standing around 0.25, strictly lying between 0 and 0.5 as expected. These values represent a moderate stealth level and suggests that over the observation period, an insider tends to trade at significantly smaller scales than the entire population of liquidity traders while transcending an average liquidity trader. In the case χ=2\chi=2, for instance, by noting that 15<N^γ^<2115<\hat{N}^{\hat{\gamma}}<21, while 213<N^<249213<\sqrt{\hat{N}}<249, the insider trade size is roughly 17 times larger than a liquidity trade size, albeit 13 times smaller than the size of all trades combined. This observation is in line with a key conclusion of Meulbroek ([1992](https://arxiv.org/html/2512.06309v1#bib.bib29)) that in spite of abnormal volumes on insider trading days, the insider trading volume only makes up a small portion of the total. The (lower bound) estimates for the population size NN exhibit slightly larger variations across conditions but stand at a scale of 104≫3010^{4}\gg 30 (see Footnote [12](https://arxiv.org/html/2512.06309v1#footnote12 "footnote 12 ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), and the equilibrium model estimates that, on average, one insider trade is present for (at least) approximately every 50,000 non-insider trades over the same trading episodes.

One seemingly counterintuitive observation is that the estimate for γ\gamma exhibits an increasing trend with respect to the penalty multiplier χ\chi. While one might well expect heightened penalties to deter insider activity and thus reduce γ\gamma, this result is actually consistent with the calibration approach. As the calibration works by fixing the sample statistics and deriving implied model parameters, achieving the same insider trade size under stricter penalties necessitates more aggressive insider trading behavior. As such, Table [2](https://arxiv.org/html/2512.06309v1#S5.T2 "Table 2 ‣ 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") should not be interpreted as a guide for designing optimal penalty multipliers.

We proceed to solve the finite-population equilibrium (existent) with the values of N^\hat{N} in Table [2](https://arxiv.org/html/2512.06309v1#S5.T2 "Table 2 ‣ 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") to check its closeness to the limiting equilibrium employed for the calibration, for which purpose we employ a fixed-point algorithm developed according to the equilibrium conditions in ([B.11](https://arxiv.org/html/2512.06309v1#A2.E11 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([B.14](https://arxiv.org/html/2512.06309v1#A2.E14 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) in Appendix [B](https://arxiv.org/html/2512.06309v1#A2 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"). For a concise presentation, we concentrate on the case χ=3\chi=3, with the resulting equilibrium objects presented in Table [3](https://arxiv.org/html/2512.06309v1#S5.T3 "Table 3 ‣ 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") and Figure [1](https://arxiv.org/html/2512.06309v1#S5.F1 "Figure 1 ‣ 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") below – results in the cases χ=1\chi=1 and χ=2\chi=2 are substantially no different. Clearly, the finite-N^\hat{N} equilibrium objects are all very close to their limiting counterparts, verifying the validity of the approximation (ZN∗,PN∗)≈(Nγ​Z~γ∗,P~γ∗)(Z^{\ast}\_{N},P^{\ast}\_{N})\approx(N^{\gamma}\tilde{Z}^{\ast}\_{\gamma},\tilde{P}^{\ast}\_{\gamma}) in the outset. From Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), the rate of equilibrium convergence is proportionate to the stealth index γ\gamma.

Table 3: Comparison of equilibrium strategies in calibration experiment I (χ=3\chi=3)

| Equations used | ([5.1.2](https://arxiv.org/html/2512.06309v1#S5.E2 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([5.1.3](https://arxiv.org/html/2512.06309v1#S5.E3 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) | ([5.1.2](https://arxiv.org/html/2512.06309v1#S5.E2 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([5.1.4](https://arxiv.org/html/2512.06309v1#S5.E4 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) | ([5.1.3](https://arxiv.org/html/2512.06309v1#S5.E3 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([5.1.4](https://arxiv.org/html/2512.06309v1#S5.E4 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) |
| --- | --- | --- | --- |
| (ZN^∗​(0),ZN^∗​(1))(Z^{\ast}\_{\hat{N}}(0),Z^{\ast}\_{\hat{N}}(1)) | (−9813,9813)(-9813,9813) | (−9811,9811)(-9811,9811) | (−12862,12862)(-12862,12862) |
| (N^γ^​Z~γ^∗​(0),N^γ^​Z~γ^∗​(1))(\hat{N}^{\hat{\gamma}}\tilde{Z}^{\ast}\_{\hat{\gamma}}(0),\hat{N}^{\hat{\gamma}}\tilde{Z}^{\ast}\_{\hat{\gamma}}(1)) | (−9819,9819)(-9819,9819) | (−9819,9819)(-9819,9819) | (−12872,12872)(-12872,12872) |

![Refer to caption](ceI1.png)
  


Figure 1: Comparison of equilibrium price function in calibration experiment I (χ=3\chi=3)

### 5.2 Calibration experiment II

In the second calibration experiment, we leverage available data from two recent studies, Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27)) and Patel and Putņinš ([2021](https://arxiv.org/html/2512.06309v1#bib.bib32)), on legal risk in insider trading. First, using a data set of 530 insider trading cases prosecuted by the SEC between 1995 and 2018, Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27)) constructed two key empirical proxies: the total dollar volume traded by the insider over a trading episode (in units of days) (denoted as B^​et\widehat{\text{B}}\text{et} therein) and the corresponding (daily) insider-to-total volume ratio (B^​etNorm\widehat{\text{B}}\text{et}\text{Norm}), the latter serving to provide a clearer indication of the market impact of insider trades. For these calculations, the total dollar volume represents the average daily dollar volume traded for the corresponding assets over the prior calendar year. Second, Patel and Putņinš ([2021](https://arxiv.org/html/2512.06309v1#bib.bib32)) constructed a data set spanning the period from 1996 to 2016 and utilized a two-stage detection-controlled estimation method to derive contemporaneous estimates for the probability of detection and prosecution of insider trading across different corporate events. Thus, these two data sets cover observation periods that are considerably close in range.282828For more details regarding the two data sets we refer to Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27)) Tab. I and Patel and Putņinš ([2021](https://arxiv.org/html/2512.06309v1#bib.bib32)) Sect. 2, respectively.

We summarize some useful statistics for the calibration in Table [4](https://arxiv.org/html/2512.06309v1#S5.T4 "Table 4 ‣ 5.2 Calibration experiment II ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading").292929Although Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27)) primarily focuses on dollar volume, for adequate comparison (with calibration experiment I) we still use share volume statistics. The two statistics are gleaned from Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27)) Tab. III & Fig. IA.5.

The idea of the calibration is in principle identical to that of experiment I. In the setting of Example [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmexample1 "Example 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), we set p=1/2p=1/2 and consider three penalty multiplier values χ∈{1,2,3}\chi\in\{1,2,3\} for experimentation, along with a quadratic hazard rate λ​(z)=z2/(2​σ2)\lambda(z)=z^{2}/(2\sigma^{2}).303030The equilibrium simulation in Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27)) is conducted in a very similar setting, with a binary asset value VV with range equal to 1 and p=1/2p=1/2. The (size-modulated) hazard rate λ1\lambda\_{1} from ([2.1](https://arxiv.org/html/2512.06309v1#S2.Ex2 "2.1 Prosecution mechanism ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) can be reasonably approximated by the quadratic hazard rate. In this case, the limiting equilibrium strategy Z~γ∗\tilde{Z}^{\ast}\_{\gamma} is as given in ([5.1.5](https://arxiv.org/html/2512.06309v1#S5.E5 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), with P~γ∗=1/2\tilde{P}^{\ast}\_{\gamma}=1/2.

Table 4: Statistics for insider trading volume data (1995–2018)
  
(Source: Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27)))

|  |  |
| --- | --- |
| Median insider volume | 4,900 |
| Median insider-to-total volume ratio | 2.6% |

On the assumption that N≫1N\gg 1, according to Table [4](https://arxiv.org/html/2512.06309v1#S5.T4 "Table 4 ‣ 5.2 Calibration experiment II ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), we can match ([5.1.2](https://arxiv.org/html/2512.06309v1#S5.E2 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) to the number 4900 and equate ([5.1.4](https://arxiv.org/html/2512.06309v1#S5.E4 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) to 1/21/2 for x=1/2.6%x=1/2.6\% in order to form two calibration conditions. Indeed, in Table [4](https://arxiv.org/html/2512.06309v1#S5.T4 "Table 4 ‣ 5.2 Calibration experiment II ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), we use the median insider volume instead of the average because the insider volume distribution over these observation periods is severely right-skewed and fat-tailed; the theoretical counterpart can still be represented by the conditional expectation ([5.1.2](https://arxiv.org/html/2512.06309v1#S5.E2 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), as the sample median converges to this value asymptotically given that V​=d.​Bernoulli​(1/2)V\overset{\rm d.}{=}\text{Bernoulli}(1/2). For the trade size of an average liquidity trader, we stick to the previous values, namely μ=1.68625\mu=1.68625 and σ=1000\sigma=1000, in order to obtain a comparable conservative lower bound estimate for NN. As before, the insider volume data over the observation periods should be interpreted as being conditional on prosecution. The theoretical counterpart of the prosecution probability is given by ([5.1.1](https://arxiv.org/html/2512.06309v1#S5.E1 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")).
However, upon applying Z=Nγ​Z~γ∗Z=N^{\gamma}\tilde{Z}^{\ast}\_{\gamma} (with γ=β\gamma=\beta), the expression in ([5.1.1](https://arxiv.org/html/2512.06309v1#S5.E1 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) is not a function of the variables NN and γ\gamma but can be used for later verifying the functional form of the hazard rate. Table [5](https://arxiv.org/html/2512.06309v1#S5.T5 "Table 5 ‣ 5.2 Calibration experiment II ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") summarizes the calibration results in this experiment.

Table 5: Results on calibration experiment II

|  |  |  |
| --- | --- | --- |
| (N^,γ^)(\hat{N},\hat{\gamma}) | χ=1\chi=1 | (108858,0.137029)(108858,0.137029) |
| χ=2\chi=2 | (108858,0.177425)(108858,0.177425) |
| χ=3\chi=3 | (108858,0.19748)(108858,0.19748) |

Table 6: Comparison of equilibrium strategies in calibration experiment II (χ=3\chi=3)

|  | Strategy | implied prosecution probability |
| --- | --- | --- |
| (ZN^∗​(0),ZN^∗​(1))(Z^{\ast}\_{\hat{N}}(0),Z^{\ast}\_{\hat{N}}(1)) | (−4900,4900)(-4900,4900) | 11.572% |
| (N^γ^​Z~γ^∗​(0),N^γ^​Z~γ^∗​(1))(\hat{N}^{\hat{\gamma}}\tilde{Z}^{\ast}\_{\hat{\gamma}}(0),\hat{N}^{\hat{\gamma}}\tilde{Z}^{\ast}\_{\hat{\gamma}}(1)) | (−4900,4900)(-4900,4900) | 11.576% |

![Refer to caption](ceII1.png)
  


Figure 2: Comparison of equilibrium price function in calibration experiment II (χ=3\chi=3)

We see that based on statistics from this non-overlapping new observation period (1995–2018), the stealth index γ\gamma is again estimated to strictly lie within the interval (0,0.5)(0,0.5), as expected, though the estimates suggest a somewhat higher stealth level compared to the estimates from the first experiment covering a pre-1990 period. This could indicate gradually increased prudence among insiders after 2000, likely in response to enhanced regulatory measures (such as increased regulatory budgets and the introduction of the SEC Whistleblower Program), which also agrees with the increasing trends of the prosecution probability as discussed in Patel and Putņinš ([2021](https://arxiv.org/html/2512.06309v1#bib.bib32)) Sect. 4.3. In addition, the implied lower bound of the population size, N^\hat{N}, turns out to be larger than those from the first experiment (Table [2](https://arxiv.org/html/2512.06309v1#S5.T2 "Table 2 ‣ 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), standing at the 10510^{5} scale.

As before, we compute the finite-population equilibrium (existent) using the estimates (N^,γ^)(\hat{N},\hat{\gamma}) from Table [5](https://arxiv.org/html/2512.06309v1#S5.T5 "Table 5 ‣ 5.2 Calibration experiment II ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") to justify the validity of employing the limiting equilibrium; again, we only illustrate the case χ=3\chi=3. Table [6](https://arxiv.org/html/2512.06309v1#S5.T6 "Table 6 ‣ 5.2 Calibration experiment II ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") and Figure [2](https://arxiv.org/html/2512.06309v1#S5.F2 "Figure 2 ‣ 5.2 Calibration experiment II ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") verify the closeness between the equilibrium objects, respectively. In the last column, the model-implied prosecution probabilities are computed by plugging the equilibrium strategy values into ([5.1.1](https://arxiv.org/html/2512.06309v1#S5.E1 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), and notably, are at a comparable level to the average detection rate of 15% reported by Patel and Putņinš ([2021](https://arxiv.org/html/2512.06309v1#bib.bib32)) Sect. 2, a key conclusion of their study (with data range 1996–2016).313131The implied values both fall within the 95% confidence interval for the average detection rate for insider trading ahead of earnings announcements; see Patel and Putņinš ([2021](https://arxiv.org/html/2512.06309v1#bib.bib32)) Sect. 4.2. This observation also empirically validates the quadratic form of the hazard rate.

## 6 Further discussions: Criminal and mixed penalties

In this section, we discuss the general scenario where criminal charges are within consideration. Suppose that on successful prosecution, besides losing all of his illicit profit, the insider trader faces a mixture of both civil and criminal penalties. While civil penalties are calculated with penalty multipliers applied to the insider’s illicit profit as before, criminal penalties are determined based on his realized trading strategy (ZZ). Therefore, we are looking at the general form ([2.2.1](https://arxiv.org/html/2512.06309v1#S2.E1a "In 2.2 Composition of legal penalties ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) of the penalty function.

For any population size N≥1N\geq 1, the insider’s objective function is given by ([2.3.8](https://arxiv.org/html/2512.06309v1#S2.E8 "In 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) in equilibrium, which is detailed as, for v∈{0,1}v\in\{0,1\} and z∈ℝvz\in\mathbb{R}\_{v},

|  |  |  |  |
| --- | --- | --- | --- |
|  | J´N​(Z;z,v)=e−λN​(z)​QN​(Z;z,v)−(1−e−λN​(z))​(C0​(z)+χ0​QN​(Z;z,v)).\acute{J}\_{N}(Z;z,v)=e^{-\lambda\_{N}(z)}Q\_{N}(Z;z,v)-(1-e^{-\lambda\_{N}(z)})\big(C\_{0}(z)+\chi\_{0}Q\_{N}(Z;z,v)\big). |  | (6.1) |

Recall that χ0=χ−1\chi\_{0}=\chi-1 is the adjusted penalty multiplier, and QNQ\_{N} denotes the insider’s expected profit in ([2.3](https://arxiv.org/html/2512.06309v1#S2.Ex4 "2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). The last term in ([6.1](https://arxiv.org/html/2512.06309v1#S6.E1 "In 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) shows the total penalty besides disgorgement, reflecting a balanced mechanism that accounts for both the insider’s malicious intent in engaging in illicit trading and his realized profit, without either directly offsetting the other. We emphasize that under the general form ([2.2.1](https://arxiv.org/html/2512.06309v1#S2.E1a "In 2.2 Composition of legal penalties ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), any leniency or discretion exercised by the regulator can be incorporated through the functional form of the criminal penalty function (C0C\_{0}) or the penalty multiplier (χ0\chi\_{0}) governing civil penalties, and so the approach by adding both types of penalties is sufficiently general from a practical standpoint as well.

By setting the penalty multiplier χ=1\chi=1 in the structure ([2.2.1](https://arxiv.org/html/2512.06309v1#S2.E1a "In 2.2 Composition of legal penalties ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we come to a situation where the insider faces criminal penalties exclusively on top of disgorgement. Then, with χ0=0\chi\_{0}=0, ([6.1](https://arxiv.org/html/2512.06309v1#S6.E1 "In 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | J´N​(Z;z,v)=e−λN​(z)​QN​(Z;z,v)−(1−e−λN​(z))​C0​(z),z∈ℝv,v∈{0,1}.\acute{J}\_{N}(Z;z,v)=e^{-\lambda\_{N}(z)}Q\_{N}(Z;z,v)-(1-e^{-\lambda\_{N}(z)})C\_{0}(z),\quad z\in\mathbb{R}\_{v},\;v\in\{0,1\}. |  | (6.2) |

A comparison between ([6.2](https://arxiv.org/html/2512.06309v1#S6.E2 "In 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([4](https://arxiv.org/html/2512.06309v1#S4.Ex1 "4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) shows that, different from the predominant scenario involving civil penalties only, the penalty function C0C\_{0} has no explicit dependence on the asset value v∈{0,1}v\in\{0,1\}, focusing instead on the insider’s trading behavior for a specific asset value – and not that in the alternative situation, e.g., through the price function PNP\_{N} (or the general form of ΨN\varPsi\_{N}). This is reasonable, as in criminal cases, insider trading behavior is assessed based on the realized asset value (to which the insider has prior access), rather than evaluated in hypothetical situations (Picardo ([2022](https://arxiv.org/html/2512.06309v1#bib.bib33))). The insider is also aware that penalties necessarily increase with his actual trading activity, governed by the monotonicity of the penalty function C0C\_{0}.

As noted earlier, the asymptotic growth of C0C\_{0} should be decisive of the asymptotic behaviors of the trading strategies. This leads to the following conditions in addition to Assumption [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading").

###### Assumption 6.1.

The following three conditions hold.

(i) For v∈{0,1}v\in\{0,1\}, both λ\lambda and C0C\_{0} are continuously differentiable and convex (not necessarily strictly) on ℝv\mathbb{R}\_{v}, with λ′<0\lambda^{\prime}<0 and C0′≤0C^{\prime}\_{0}\leq 0 on (−∞,0)(-\infty,0), while λ′>0\lambda^{\prime}>0 and C0′≥0C^{\prime}\_{0}\geq 0 on (0,∞)(0,\infty).
  
(ii) There exist constants θ≥1\theta\geq 1, θ′>0\theta^{\prime}>0, and Kθ>0K\_{\theta}>0, such that323232Given the convexity of λ\lambda, an application of the monotone density theorem (see, e.g., Bingham, Goldie, and Teugels ([1989](https://arxiv.org/html/2512.06309v1#bib.bib9))) ensures that λ′​(z)=Kθ​θ​z​|z|θ−2\lambda^{\prime}(z)=K\_{\theta}\theta z|z|^{\theta-2} if λ​(z)∼Kθ​|z|θ\lambda(z)\sim K\_{\theta}|z|^{\theta}, both as |z|↘0|z|\searrow 0; however, there are no direct implications for the asymptotic behavior of the remainder (λ′​(z)−Kθ​θ​z​|z|θ−2\lambda^{\prime}(z)-K\_{\theta}\theta z|z|^{\theta-2}), hence the imposition of ([6.3](https://arxiv.org/html/2512.06309v1#S6.E3 "In Assumption 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")).

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​(z)=Kθ​|z|θ​(1+o​(1)),λ′​(z)=Kθ​θ​z​|z|θ−2+O​(|z|θ​(1+θ′)−1),as​|z|↘0.\lambda(z)=K\_{\theta}|z|^{\theta}(1+o(1)),\quad\lambda^{\prime}(z)=K\_{\theta}\theta z|z|^{\theta-2}+O(|z|^{\theta(1+\theta^{\prime})-1}),\quad\mbox{as}~|z|\searrow 0. |  | (6.3) |

(iii) There exist constants α≥1\alpha\geq 1 and Kα>0K\_{\alpha}>0 and, if α>1\alpha>1, an additional constant α′>0\alpha^{\prime}>0, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | C0​(z)=Kα​|z|α​(1+o​(1)),C0′​(z)=Kα​α​z​|z|α−2+O​(|z|α−1−α′),as​|z|→∞.C\_{0}(z)=K\_{\alpha}|z|^{\alpha}(1+o(1)),\quad C\_{0}^{\prime}(z)=K\_{\alpha}\alpha z|z|^{\alpha-2}+O(|z|^{\alpha-1-\alpha^{\prime}}),\quad\mbox{as}~|z|\to\infty. |  | (6.4) |

Since the choice of the penalty function is entirely up to the regulator, it is customizable and can be adjusted flexibly on a case-by-case basis.
By contrast, the small argument behavior assumption regarding the hazard rate is natural and covers abnormal order flow imbalance-based detection (DeMarzo, Fishman, and Hagerty ([1998](https://arxiv.org/html/2512.06309v1#bib.bib23))). For example, in ([2.1](https://arxiv.org/html/2512.06309v1#S2.Ex2 "2.1 Prosecution mechanism ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), since the sum of the two complementary error functions is asymptotically equivalent to z2z^{2} as |z|↘0|z|\searrow 0, we have that θ=min⁡{θD,2}\theta=\min\{\theta\_{D},2\} if D​(z)∼KD​|z|θDD(z)\sim K\_{D}|z|^{\theta\_{D}} as |z|↘0|z|\searrow 0 for KD>0K\_{D}>0 and θD≥1\theta\_{D}\geq 1; details are in Supplemental Appendix [B](https://arxiv.org/html/2512.06309v1#A2a "Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"). The value of α\alpha is likely inversely related to γ\gamma, and in fact, the assumption on λ\lambda is only dominant when α\alpha becomes “sufficiently large,” as the insider will judiciously reduce the prosecution probability so as to offset the fast-growing (additional) penalty term in ([6.2](https://arxiv.org/html/2512.06309v1#S6.E2 "In 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). Thus, Assumption [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") includes small arguments because the scaled quantity N−β​zN^{-\beta}z can still be small (as N→∞N\to\infty) even if zz is large.

Under Assumption [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), we are able to extrapolate the main results in the predominant scenario (Section [4](https://arxiv.org/html/2512.06309v1#S4 "4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) to the present general scenario concerning both civil and criminal penalties. In particular, a finite-population equilibrium (ZN∗,PN∗)(Z^{\ast}\_{N},P^{\ast}\_{N}) in the sense of Definition [2.1](https://arxiv.org/html/2512.06309v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") continues to exist;
see Supplemental Appendix [A](https://arxiv.org/html/2512.06309v1#A1a "Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") for details. Most striking is the existence of a unique γ\gamma-limiting equilibrium (Z~γ∗,P~γ∗)(\tilde{Z}^{\ast}\_{\gamma},\tilde{P}^{\ast}\_{\gamma}) in the sense of Definition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), which is also unique when γ<1/2\gamma<1/2; in particular, ([4.2](https://arxiv.org/html/2512.06309v1#S4.E2 "In Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) is to be replaced by the more elaborate condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ=min⁡{β​θθ+α−1,12}.\gamma=\min\Big\{\frac{\beta\theta}{\theta+\alpha-1},\frac{1}{2}\Big\}. |  | (6.5) |

Based on ([6.5](https://arxiv.org/html/2512.06309v1#S6.E5 "In 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), the stealth index still has the upper bound 1/21/2, while it further exhibits a clear inverse relationship with α\alpha. If α=1\alpha=1, the insider trader views the criminal penalties as relatively minor and simply chooses γ=min⁡{β,1/2}\gamma=\min\{\beta,1/2\}, based entirely on the scale effect from λ\lambda (equivalently, the prosecution probability), as in ([4.2](https://arxiv.org/html/2512.06309v1#S4.E2 "In Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")); in this case, the small argument behavior of λ\lambda (namely θ\theta) plays no role. Conversely, as α\alpha exceeds 1, indicating severe criminal penalties, the insider begins to place greater weight on the consequences of prosecution and, accordingly, trades less aggressively with a smaller value γ<β\gamma<\beta.
These results are formally stated in Theorem [SA.1](https://arxiv.org/html/2512.06309v1#A1.Thmtheorem1 "Theorem SA.1. ‣ Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") in Supplemental Appendix [A](https://arxiv.org/html/2512.06309v1#A1a "Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), along with the corresponding convergence rates that are jointly determined by all the coefficients β\beta, θ\theta, α\alpha, θ′\theta^{\prime}, and α′\alpha^{\prime}.

We give the following illustrative example to highlight the analytical simplicity of the limiting equilibrium.

###### Example 6.1.

Let p=1/3p=1/3, λ​(z)=C0​(z)=|z|\lambda(z)=C\_{0}(z)=|z|, and χ=1\chi=1, which satisfy Assumption [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), with θ=α=1\theta=\alpha=1. Suppose that β∈[0,1/2)\beta\in[0,1/2), so that γ=β<1/2\gamma=\beta<1/2. Then, with the Lambert W\mathrm{W} function W0\mathrm{W}\_{0}, the γ\gamma-limiting equilibrium is uniquely determined as

|  |  |  |
| --- | --- | --- |
|  | Z~γ∗≡(Z~γ∗​(0),Z~γ∗​(1))=(W0​(3​e4)−1,1−W0​(3​e5))≈(−0.138547,0.23844),P~γ∗=13.\tilde{Z}^{\ast}\_{\gamma}\equiv(\tilde{Z}^{\ast}\_{\gamma}(0),\tilde{Z}^{\ast}\_{\gamma}(1))=\Big(\mathrm{W}\_{0}\big(\tfrac{3e}{4}\big)-1,1-\mathrm{W}\_{0}\big(\tfrac{3e}{5}\big)\Big)\approx(-0.138547,0.23844),\quad\tilde{P}^{\ast}\_{\gamma}=\tfrac{1}{3}. |  |

In Example [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmexample1 "Example 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), the (size-modulated) hazard rate and the criminal penalty function are both perfectly proportional to the insider’s trading quantities, and the stealth index γ\gamma does not alter the form of the limiting equilibrium (Definition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), while only affecting the convergence rate of the finite-population equilibrium (Theorem [SA.1](https://arxiv.org/html/2512.06309v1#A1.Thmtheorem1 "Theorem SA.1. ‣ Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") assertion (iii)) – through the scaled equilibrium strategy Z~γ∗\tilde{Z}^{\ast}\_{\gamma}. With the asset value VV more likely revealed to be 0 than 1 (p<1/2p<1/2), at equilibrium the insider also tends to trade more if V=1V=1 (with Z~γ∗​(1)>|Z~γ∗​(0)|\tilde{Z}^{\ast}\_{\gamma}(1)>|\tilde{Z}^{\ast}\_{\gamma}(0)|) to exploit the price difference, which behavior differs fundamentally from what we have seen in Example [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmexample1 "Example 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") involving only civil penalties. From the regulator’s viewpoint, this fundamental difference speaks to a crucial benefit of retaining criminal penalties: to prosecute based on the intent of illicit trading – a factor that can exhibit significant asymmetry across different realizations (see, e.g., Öberg ([2014](https://arxiv.org/html/2512.06309v1#bib.bib31))).

The next example shows that if the convexity conditions in Assumption [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") are violated, then the uniqueness of the limiting equilibrium is not guaranteed.

###### Example 6.2.

Let p=1/3p=1/3, β=0\beta=0, and χ=1\chi=1. Consider λ​(z)=log⁡(|z|+1)\lambda(z)=\log(|z|+1), which is concave (violating Assumption [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")),
and the piecewise penalty function

|  |  |  |
| --- | --- | --- |
|  | C0​(z)={14​z+112,if ​z≤−6,−z144,if −6<z≤0,25​z144,if ​0<z≤65,512−14​z,if ​z>65,C\_{0}(z)=\begin{cases}\frac{1}{4z}+\frac{1}{12},&\quad\text{if }z\leq-6,\\ -\frac{z}{144},&\quad\text{if }-6<z\leq 0,\\ \frac{25z}{144},&\quad\text{if }0<z\leq\frac{6}{5},\\ \frac{5}{12}-\frac{1}{4z},&\quad\text{if }z>\frac{6}{5},\end{cases} |  |

which is strictly increasing and continuously differentiable but again concave in |z||z| on ℝv\mathbb{R}\_{v}, v∈{0,1}v\in\{0,1\}. Then, there is a continuum of 0-limiting equilibria:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z~0∗∈(−∞,−6]×[65,∞),P~0∗=13.\tilde{Z}^{\ast}\_{0}\in(-\infty,-6]\times\big[\tfrac{6}{5},\infty\big),\quad\tilde{P}^{\ast}\_{0}=\tfrac{1}{3}. |  | (6.6) |

Example [6.2](https://arxiv.org/html/2512.06309v1#S6.Thmexample2 "Example 6.2. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") illustrates an extreme case where the prosecution mechanism is considerably weak and ineffective, with the maximum penalty capped, leading to little-to-zero deterrent effect on insider trading. Consequently, the insider’s optimal strategies can involve unboundedly large trade sizes as the population of liquidity traders grows.

## 7 Conclusions

This paper has introduced a Kyle-type model for insider trading with legal risk featuring a flexible scheme of legal detection and penalty and the presence of a large liquidity trading crowd. Besides justifying the normal distribution of liquidity trade sizes, the population size NN of liquidity traders has spawned a series of limiting equilibria that provide a profound understanding of the camouflage effect in insider trading, particularly uncovering insiders’ choices of trading scales when taking advantage of the surrounding trading masses in avoidance of detection. These trading scales are quantified by the stealth index γ\gamma, which is heavily associated with the population size over concurrent trading episodes.

The equilibrium analysis covering various types of penalty functions has shown that the stealth index implied by insiders’ trading behavior is largely dependent on the mechanisms of detection as well as the imposition of penalties from regulators’ side (Picardo ([2022](https://arxiv.org/html/2512.06309v1#bib.bib33))). In particular, if only civil penalties are imposed – based on illicit profit from trade – then in equilibrium, insiders choose the stealth index solely based on the scale effect from the perceived probability of prosecution (see ([4.2](https://arxiv.org/html/2512.06309v1#S4.E2 "In Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"))), as long as the resulting trade size does not reach the level of the combined activity of all liquidity traders. On the other hand, when severe criminal penalties are devised (with α>1\alpha>1), insiders are prone to adopting an elevated stealth level (see ([6.5](https://arxiv.org/html/2512.06309v1#S6.E5 "In 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"))) compared to what the underlying detection mechanism implies. This striking disparity highlights the importance of reserving criminal sanctions in insider trading cases, due to their effectiveness in deterring illicit trading driven by a highly strategic intent such as market abuse (Öberg ([2014](https://arxiv.org/html/2512.06309v1#bib.bib31)) and Dalko and Wang ([2016](https://arxiv.org/html/2512.06309v1#bib.bib21))).

On a technical level, the proven equilibrium convergence properties (Theorem [4.2](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") and assertions (iii) in Theorems [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") and [SA.1](https://arxiv.org/html/2512.06309v1#A1.Thmtheorem1 "Theorem SA.1. ‣ Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) convey a key message that employing a limiting equilibrium significantly enhances the ease of analysis without altering the equilibrium’s fundamental implications. The empirical perspectives in Section [5](https://arxiv.org/html/2512.06309v1#S5 "5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") further demonstrate the ease of equilibrium calibration to insider trading volume data and confirm the prevalence of stealth trading amid sizeable normal trading activity, revealing a moderate stealth level in insider trading (Barclay and Warner ([1993](https://arxiv.org/html/2512.06309v1#bib.bib8)) and Chakravarty ([2001](https://arxiv.org/html/2512.06309v1#bib.bib18))) accompanied by a significant reduction in price informativeness (Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27))) – hence conforming to the camouflage effect.

## Acknowledgements

The authors are grateful to Marcin Kacperczyk for kindly sharing supplementary statistics for their data set in Kacperczyk and Pagnotta ([2024](https://arxiv.org/html/2512.06309v1#bib.bib27)). Jin Ma and Jianfeng Zhang are supported in part by U.S. NSF grant #DMS-2510403.

## References

* Abramowitz and Stegun, (1972)
   Abramowitz, M., & Stegun, I.A. (1972). Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables, 10th printing. U.S. National Bureau of Standards, Washington, D.C.
* Admati and Pfeiderer, (1988)
   Admati, A.R., & Pfleiderer, P. (1988). A theory of intraday patterns: Volume and price variability. The Review of Financial Studies, 1(1), 3–40.
* Alexander and Peterson, (2007)
   Alexander, G.J., & Peterson, M.A. (2007). An analysis of trade-size clustering and its relation to stealth trading. Journal of Financial Economics, 84(2), 435–471.
* Anand and Chakravarty, (2007)
   Anand, A., & Chakravarty, S. (2007). Stealth trading in options markets. Journal of Financial and Quantitative Analysis, 42(1), 167–187.
* Back, (1992)
   Back, K. (1992). Insider trading in continuous time. The Review of Financial Studies, 5(3), 387–409.
* Back and Baruch, (2004)
   Back, K., & Baruch, S. (2004). Information in securities markets: Kyle meets Glosten and Milgrom. Econometrica, 72(2), 433–465.
* Bagnoli, Viswanathan, and Holden, (2001)
   Bagnoli, M., Viswanathan, S., & Holden, C. (2001). On the existence of linear equilibria in models of market making. Mathematical Finance, 11(1), 1–31.
* Barclay and Warner, (1993)
   Barclay, M.J., & Warner, J.B. (1993). Stealth trading and volatility: Which trades move prices? Journal of Financial Economics, 34(3), 281–305.
* Bingham, Goldie, and Teugels, (1989)
   Bingham, N.H., Goldie, C.M., & Teugels, J. L. (1989). Regular Variation (Vol. 27). Cambridge university press.
* Blau, (2017)
   Blau, B. M. (2017). Price dynamics and speculative trading in bitcoin. Research in International Business and Finance, 41, 493–499.
* Boulatov, Kyle, and Livdan, (2013)
   Boulatov, A., Kyle, A.S., Livdan, D. (2013). Uniqueness of equilibrium in the single period Kyle’85 model. Working Paper. 35 pages.
* Brascamp and Lieb, (1976)
   Brascamp, H.J., & Lieb, E.H. (1976). On extensions of the Brunn–Minkowski and Prékopa–Leindler theorems, including inequalities for log concave functions, and with an application to the diffusion equation. Journal of functional analysis, 22(4): 366–389.
* Cai, Cai, and Keasey, (2006)
   Cai, B.M., Cai, C.X., & Keasey, K. (2006). Which trades move prices in emerging markets?: Evidence from China’s stock market. Pacific-Basin Finance Journal, 14(5), 453–466.
* Caldentey and Stacchetti, (2010)
   Caldentey, R., & Stacchetti, E. (2010). Insider trading with a random deadline. Econometrica, 78(1): 245–283.
* Carré, Collin-Dufresne, and Gabriel, (2022)
   Carré, S., Collin-Dufresne, P., & Gabriel, F. (2022). Insider trading with penalties. Journal of Economic Theory, 203, 105461.
* Çetin, (2025)
   Çetin, U. (2025). Insider trading with penalties in continuous time. Journal of Economic Theory, 228: 106061.
* Çetin and Waelbroeck, (2024)
   Çetin, U., & Waelbroeck, H. (2024). Power laws in market microstructure. In: Peter Carr Gedenkschrift: Research Advances in Mathematical Finance (pp. 753–819).
* Chakravarty, (2001)
   Chakravarty, S. (2001). Stealth-trading: Which traders’ trades move stock prices? Journal of Financial Economics, 61(2), 289-307.
* Chang, Pinegar, and Schachter, (1997)
   Chang, E.C., Pinegar, J.M., & Schachter, B. (1997). Interday variations in volume, variance and participation of large speculators. Journal of Banking and Finance, 21(6), 797–810.
* Chen, (2019)
   Chen, T. (2019). The price impact of trade-size clustering: Evidence from an intraday analysis. Journal of Business Research, 101, 300–314.
* Dalko and Wang, (2016)
   Dalko, V., & Wang, M.H. (2016). Why is insider trading law ineffective? Three antitrust suggestions. Studies in Economics and Finance, 33(4), 704–715.
* Del Guercio, Odders-White, and Ready, (2017)
   Del Guercio, D., Odders-White, E.R., & Ready, M.J. (2017). The deterrent effect of the Securities and Exchange Commission’s enforcement intensity on illegal insider trading: Evidence from run-up before news events. The Journal of Law and Economics, 60(2), 269–307.
* DeMarzo, Fishman, and Hagerty, (1998)
   DeMarzo, P.M., Fishman, M.J., & Hagerty, K.M. (1998). The optimal enforcement of insider trading regulations. Journal of Political Economy, 106(3), 602–632.
* Fei and Xia, (2024)
   Fei, Z., & Xia, W. (2024). Regulating stochastic clocks §\S. Quantitative Finance, 24(7), 921–953.
* Frino et al., (2013)
   Frino, A., Satchell, S., Wong, B., & Zheng, H. (2013). How much does an illegal insider trade? International Review of Finance, 13(2), 241–263.
* Griskevicius et al., (2006)
   Griskevicius, V., Goldstein, N.J., Mortensen, C.R., Cialdini, R.B., & Kenrick, D.T. (2006). Going along versus going alone: When fundamental motives facilitate strategic (non) conformity. Journal of Personality and Social Psychology, 91(2), 281–294.
* Kacperczyk and Pagnotta, (2024)
   Kacperczyk, M., & Pagnotta, E.S. (2024). Legal risk and insider trading. The Journal of Finance, 79(1), 305–355.
* Kyle, (1985)
   Kyle, A.S. (1985). Continuous auctions and insider trading. Econometrica, 53, 1315–1335.
* Meulbroek, (1992)
   Meulbroek, L.K. (1992). An empirical analysis of illegal insider trading. The Journal of Finance, 47(5), 1661–1699.
* Mike and Farmer, (2008)
   Mike, S., & Farmer, J.D. (2008). An empirical behavioral model of liquidity and volatility. Journal of Economic Dynamics and Control, 32(1), 200–234.
* Öberg, (2014)
   Öberg, J. (2014). Is it “essential” to imprison insider dealers to enforce insider dealing laws?. Journal of Corporate Law Studies, 14(1), 111–138.
* Patel and Putņinš, (2021)
   Patel, V., & Putņinš, T.J. (2021). How much insider trading happens in stock markets? SSRN Working Paper. Available at https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=3764192.
* Picardo, (2022)
   Picardo, E. (2022). How the SEC tracks insider trading. Investopedia. Available at 
    
  https://www.investopedia.com/articles/investing/021815/how-sec-tracks-insider-trading.asp.
* Saumard and Wellner, (2014)
   Saumard, A., & Wellner, J.A. (2014). Log-concavity and strong log-concavity: A review. Statistics Surveys, 8: p45.
* Shin, (1996)
   Shin, J. (1996). The optimal regulation of insider trading. Journal of Financial Intermediation, 5(1), 49–73.
* Yamazato, (1978)
   Yamazato, M. (1978). Unimodality of infinitely divisible distribution functions of class L. The Annals of Probability, 523–531.

## Appendix A Proof of Proposition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmproposition1 "Proposition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")

Based on ([2.3](https://arxiv.org/html/2512.06309v1#S2.Ex1a "2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we can write

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | P~Nγ​(Z~;y~)=PN​(Nγ​Z~;Nmax⁡{γ,12}​y~)=11+q​eκ~N​(y~),\displaystyle\tilde{P}^{\gamma}\_{N}(\tilde{Z};\tilde{y})=P\_{N}(N^{\gamma}\tilde{Z};N^{\max\{\gamma,\frac{1}{2}\}}\tilde{y})=\frac{1}{1+qe^{\tilde{\kappa}\_{N}(\tilde{y})}}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | withκ~N​(y~):=(2​Nmax⁡{12−γ,0}​y~−z~0−z~1)​(z~0−z~1)2​N1−2​γ​σ2,z~v:=Z~​(v).\displaystyle\mbox{with}\quad\tilde{\kappa}\_{N}(\tilde{y}):=\frac{(2N^{\max\{\frac{1}{2}-\gamma,0\}}\tilde{y}-\tilde{z}\_{0}-\tilde{z}\_{1})(\tilde{z}\_{0}-\tilde{z}\_{1})}{2N^{1-2\gamma}\sigma^{2}},\quad\tilde{z}\_{v}:=\tilde{Z}(v). |  | (A.1) |

First, if γ<1/2\gamma<1/2, then the exponent κ~N​(y~)\tilde{\kappa}\_{N}(\tilde{y}) above is

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ~N​(y~)=(2​N12−γ​y~−z~0−z~1)​(z~0−z~1)2​N1−2​γ​σ2=z~0−z~12​σ2​(2​y~N12−γ−z~0+z~1N1−2​γ),\tilde{\kappa}\_{N}(\tilde{y})=\frac{(2N^{\frac{1}{2}-\gamma}\tilde{y}-\tilde{z}\_{0}-\tilde{z}\_{1})(\tilde{z}\_{0}-\tilde{z}\_{1})}{2N^{1-2\gamma}\sigma^{2}}=\frac{\tilde{z}\_{0}-\tilde{z}\_{1}}{2\sigma^{2}}\bigg(\frac{2\tilde{y}}{N^{\frac{1}{2}-\gamma}}-\frac{\tilde{z}\_{0}+\tilde{z}\_{1}}{N^{1-2\gamma}}\bigg), |  | (A.2) |

which tends to 0 as N→∞N\to\infty. Thus, ([A](https://arxiv.org/html/2512.06309v1#A1.Ex1 "Appendix A Proof of Proposition 3.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) becomes limN→∞P~Nγ​(Z~;y~)=1/(1+q)=p\lim\_{N\to\infty}\tilde{P}^{\gamma}\_{N}(\tilde{Z};\tilde{y})=1/(1+q)=p.

Second, if γ=1/2\gamma=1/2, the terms involving NN cancel out, and we have for ([A](https://arxiv.org/html/2512.06309v1#A1.Ex1 "Appendix A Proof of Proposition 3.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) that P~Nγ​(Z~;y~)=1/(1+q​e(2​y~−z~0−z~1)​(z~0−z~1)/(2​σ2))=P1​(Z~;y~)\tilde{P}^{\gamma}\_{N}(\tilde{Z};\tilde{y})=1/(1+qe^{(2\tilde{y}-\tilde{z}\_{0}-\tilde{z}\_{1})(\tilde{z}\_{0}-\tilde{z}\_{1})/(2\sigma^{2})})=P\_{1}(\tilde{Z};\tilde{y}).

Third, let γ>1/2\gamma>1/2. Then κ~N​(y~)=(2​y~−z~0−z~1)​(z~0−z~1)/(2​N1−2​γ​σ2)\tilde{\kappa}\_{N}(\tilde{y})=(2\tilde{y}-\tilde{z}\_{0}-\tilde{z}\_{1})(\tilde{z}\_{0}-\tilde{z}\_{1})/(2N^{1-2\gamma}\sigma^{2}). If z~0=z~1=0\tilde{z}\_{0}=\tilde{z}\_{1}=0 or 2​y~−z~0−z~1=02\tilde{y}-\tilde{z}\_{0}-\tilde{z}\_{1}=0, it is clear that κ~N​(y~)=0\tilde{\kappa}\_{N}(\tilde{y})=0, and thus P~Nγ​(Z~;y~)=p\tilde{P}^{\gamma}\_{N}(\tilde{Z};\tilde{y})=p. Otherwise, we have z~0−z~1<0\tilde{z}\_{0}-\tilde{z}\_{1}<0, and so if 2​y~−z~0−z~1>02\tilde{y}-\tilde{z}\_{0}-\tilde{z}\_{1}>0, then with the exponent κ~N​(y~)\tilde{\kappa}\_{N}(\tilde{y}) tending to 0, we have P~Nγ​(Z~;y~)→1\tilde{P}^{\gamma}\_{N}(\tilde{Z};\tilde{y})\to 1, as N→∞N\to\infty, while if 2​y~−z~0−z~1<02\tilde{y}-\tilde{z}\_{0}-\tilde{z}\_{1}<0, the exponent κ~N​(y~)\tilde{\kappa}\_{N}(\tilde{y}) goes to ∞\infty, yielding that P~Nγ​(Z~;y~)→0\tilde{P}^{\gamma}\_{N}(\tilde{Z};\tilde{y})\to 0.

Summarizing the three cases, we have verified the limit expressions in ([3.2](https://arxiv.org/html/2512.06309v1#S3.E2 "In Proposition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")).
∎

## Appendix B Proof of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")

We start with the following lemma that governs the log-concavity property of the insider’s expected profit function.

###### Lemma B.1.

For any given N≥1N\geq 1, Z=(Z​(0),Z​(1))∈ℝ0×ℝ1Z=(Z(0),Z(1))\in\mathbb{R}\_{0}\times\mathbb{R}\_{1}, and v∈{0,1}v\in\{0,1\}, the function QN​(Z;z,v)Q\_{N}(Z;z,v) in ([2.3](https://arxiv.org/html/2512.06309v1#S2.Ex4 "2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"))
is strictly log-concave in z∈ℝvz\in\mathbb{R}\_{v}, i.e., log⁡QN​(Z;⋅,v)\log Q\_{N}(Z;\cdot,v) is a strictly concave function on ℝv\mathbb{R}\_{v}.

Proof. Let N≥1N\geq 1 and Z=(Z​(0),Z​(1))∈ℝ0×ℝ1Z=(Z(0),Z(1))\in\mathbb{R}\_{0}\times\mathbb{R}\_{1} be fixed. We first consider the case v=0v=0, with z<0z<0. By ([2.3](https://arxiv.org/html/2512.06309v1#S2.Ex1a "2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we write succinctly

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | PN​(Z;y)=11+ea​y+b,\displaystyle\quad\quad\quad\quad\quad\quad\quad\quad\quad P\_{N}(Z;y)=\frac{1}{1+e^{ay+b}}, |  | (B.1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | wherea:=Z​(0)−Z​(1)N​σ2<0,b:=log⁡q+Z​(1)2−Z​(0)22​N​σ2.\displaystyle\mbox{where}\quad a:=\tfrac{Z(0)-Z(1)}{N\sigma^{2}}<0,\quad b:=\log q+\tfrac{Z(1)^{2}-Z(0)^{2}}{2N\sigma^{2}}. |  |

Then, log⁡PN​(Z;y)=−log⁡(1+ea​y+b)\log P\_{N}(Z;y)=-\log\big(1+e^{ay+b}\big), and so

|  |  |  |
| --- | --- | --- |
|  | ∂ylog⁡PN​(Z;y)=−a​ea​y+b1+ea​y+b=−a+a1+ea​y+b,∂y​ylog⁡PN​(Z;y)=−a2​ea​y+b(1+ea​y+b)2<0,\partial\_{y}\log P\_{N}(Z;y)=-\frac{ae^{ay+b}}{1+e^{ay+b}}=-a+\frac{a}{1+e^{ay+b}},\quad\partial\_{yy}\log P\_{N}(Z;y)=-\frac{a^{2}e^{ay+b}}{(1+e^{ay+b})^{2}}<0, |  |

which show that PN​(Z;y)P\_{N}(Z;y) is strictly log-concave in yy. Also, note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΦN​(Z;z)=∫ℝPN​(Z;N​x+z)​e−x22​σ22​π​σ2​dx.\varPhi\_{N}(Z;z)=\int\_{\mathbb{R}}P\_{N}(Z;\sqrt{N}x+z)\frac{e^{-\frac{x^{2}}{2\sigma^{2}}}}{\sqrt{2\pi\sigma^{2}}}{\rm d}x. |  | (B.2) |

Since it is well-known that the Gaussian distribution is log-concave, in the sense that the density function e−x2/(2​σ2)/2​π​σ2e^{-x^{2}/(2\sigma^{2})}\big/\sqrt{2\pi\sigma^{2}} is log-concave in x∈ℝx\in\mathbb{R}, an application of the Prékopa–Leindler theorem (see, e.g., Brascamp and Lieb ([1976](https://arxiv.org/html/2512.06309v1#bib.bib12))) yields that ΦN​(Z;z)\varPhi\_{N}(Z;z) in ([B.2](https://arxiv.org/html/2512.06309v1#A2.E2 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) is log-concave in zz. Note further that, for v=0v=0 and z<0z<0, we have

|  |  |  |
| --- | --- | --- |
|  | log⁡QN​(Z;z,0)=log⁡(−z)+log⁡ΦN​(Z;z).\log Q\_{N}(Z;z,0)=\log(-z)+\log\varPhi\_{N}(Z;z). |  |

Then, by the (strict) concavity of the logarithm, we see that QN​(Z;z,0)Q\_{N}(Z;z,0) is (strictly) log-concave in z<0z<0.

Next, consider the case v=1v=1 and z>0z>0, with

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡QN​(Z;z,1)=log⁡z+log⁡(1−ΦN​(Z;z)),\log Q\_{N}(Z;z,1)=\log z+\log\big(1-\varPhi\_{N}(Z;z)\big), |  | (B.3) |

and 1−PN​(Z;y)=ea​y+b/(1+ea​y+b)=ea​y+b​PN​(Z;y)1-P\_{N}(Z;y)=e^{ay+b}/(1+e^{ay+b})=e^{ay+b}P\_{N}(Z;y), and so log⁡(1−PN​(Z;y))=a​y+b+log⁡PN​(Z;y)\log(1-P\_{N}(Z;y))=ay+b+\log P\_{N}(Z;y). The log-concavity of 1−PN​(Z;y)1-P\_{N}(Z;y) in yy, along with the Prékopa–Leindler theorem again, implies that 1−ΦN​(Z;z)1-\varPhi\_{N}(Z;z) is log-concave in zz. It then follows from ([B.3](https://arxiv.org/html/2512.06309v1#A2.E3 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) that QN​(Z;z,1)Q\_{N}(Z;z,1) is (strictly) log-concave in z>0z>0 as well.
∎

Proof of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") assertion (i). Consider the finite-NN equilibrium in Definition [2.1](https://arxiv.org/html/2512.06309v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"). We proceed in two steps.

Step 1 This step is concerned with the insider’s optimization problem – that is, given N≥1N\geq 1, Z=(Z​(0),Z​(1))∈ℝ0×ℝ1Z=(Z(0),Z(1))\in\mathbb{R}\_{0}\times\mathbb{R}\_{1}, and v∈{0,1}v\in\{0,1\}, we shall apply Lemma [B.1](https://arxiv.org/html/2512.06309v1#A2.Thmlemma1 "Lemma B.1. ‣ Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") to show that the objective function J´N​(Z;z,v)\acute{J}\_{N}(Z;z,v) has a unique maximum point zv∗∈ℝvz^{\*}\_{v}\in\mathbb{R}\_{v}. We assume for simplicity that λ​(z)≡λ1​(z)\lambda(z)\equiv\lambda\_{1}(z) (and hence λN​(z)\lambda\_{N}(z)) is twice-differentiable for z≠0z\neq 0.333333The twice-differentiability of λ\lambda is mainly to ease verification of the log-concavity of ΛN\varLambda\_{N} in ([B.5](https://arxiv.org/html/2512.06309v1#A2.E5 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). The same property can be verified by slightly more involved arguments if λ\lambda is only convex. By ([4](https://arxiv.org/html/2512.06309v1#S4.Ex1 "4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | J´N​(Z;z,v)=(χ​e−λN​(z)−χ0)​QN​(Z;z,v),z∈ℝv.\acute{J}\_{N}(Z;z,v)=(\chi e^{-\lambda\_{N}(z)}-\chi\_{0})Q\_{N}(Z;z,v),\quad z\in\mathbb{R}\_{v}. |  | (B.4) |

We shall only prove the case v=0v=0. The case v=1v=1 can be proved analogously.

We now restrict to z<0z<0, and denote ΛN​(z):=χ​e−λN​(z)−χ0\varLambda\_{N}(z):=\chi e^{-\lambda\_{N}(z)}-\chi\_{0}. Recall that QN>0Q\_{N}>0. By Assumption [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), since λN′​(z)<0\lambda^{\prime}\_{N}(z)<0, the (continuous) function ΛN\varLambda\_{N} is strictly increasing, with limz→−∞ΛN​(z)=−χ0≤0\lim\_{z\to-\infty}\varLambda\_{N}(z)=-\chi\_{0}\leq 0 and limz↗0ΛN​(z)=1\lim\_{z\nearrow 0}\varLambda\_{N}(z)=1. Thus, if χ0>0\chi\_{0}>0, then ΛN\varLambda\_{N} has a unique zero z0∘<0z^{\circ}\_{0}<0; if χ0=0\chi\_{0}=0, ΛN>0\varLambda\_{N}>0 on (−∞,0)(-\infty,0), and we can simply set z0∘=−∞z^{\circ}\_{0}=-\infty. In either case, on (z0∘,0)(z^{\circ}\_{0},0), we have ΛN>0\varLambda\_{N}>0, and so J´N​(Z;z,0)>0\acute{J}\_{N}(Z;z,0)>0. Note that
limz→z0∘J´N​(Z;z,0)=limz↗0J´N​(Z;z,0)=0\lim\_{z\to z^{\circ}\_{0}}\acute{J}\_{N}(Z;z,0)=\lim\_{z\nearrow 0}\acute{J}\_{N}(Z;z,0)=0, and then J´N​(Z;z,0)\acute{J}\_{N}(Z;z,0) admits a local maximum point z0∗∈(z0∘,0)z^{\*}\_{0}\in(z^{\circ}\_{0},0).

To show that z0∗z^{\*}\_{0} is the unique maximum point of J´N​(Z;⋅,0)\acute{J}\_{N}(Z;\cdot,0) on ℝ0=(−∞,0)\mathbb{R}\_{0}=(-\infty,0), let us note further that J´N​(Z;⋅,0)≤0\acute{J}\_{N}(Z;\cdot,0)\leq 0 on (−∞,z0∘](-\infty,z^{\circ}\_{0}] if χ0<0\chi\_{0}<0, and so it suffices to consider z∈(z0∘,0)z\in(z^{\circ}\_{0},0). By Lemma [B.1](https://arxiv.org/html/2512.06309v1#A2.Thmlemma1 "Lemma B.1. ‣ Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), the function QN​(Z;⋅,0)>0Q\_{N}(Z;\cdot,0)>0 is strictly log-concave. Since ΛN>0\varLambda\_{N}>0 and λN′′≥0\lambda\_{N}^{\prime\prime}\geq 0, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | d2d​z2​log⁡ΛN​(z)=−χ​χ0​(λN′​(z))2​e−λN​(z)(ΛN​(z))2−χ​λN′′​(z)​e−λN​(z)ΛN​(z)≤0;\frac{{\rm d}^{2}}{{\rm d}z^{2}}\log\varLambda\_{N}(z)=-\frac{\chi\chi\_{0}(\lambda\_{N}^{\prime}(z))^{2}e^{-\lambda\_{N}(z)}}{(\varLambda\_{N}(z))^{2}}-\frac{\chi\lambda\_{N}^{\prime\prime}(z)e^{-\lambda\_{N}(z)}}{\varLambda\_{N}(z)}\leq 0; |  | (B.5) |

that is, ΛN\varLambda\_{N} is log-concave on (z0∘,0)(z^{\circ}\_{0},0), and by ([B.4](https://arxiv.org/html/2512.06309v1#A2.E4 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and Lemma [B.1](https://arxiv.org/html/2512.06309v1#A2.Thmlemma1 "Lemma B.1. ‣ Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), J´N​(Z;⋅,0)\acute{J}\_{N}(Z;\cdot,0) is strictly log-concave. This implies that J´N​(Z;⋅,0)\acute{J}\_{N}(Z;\cdot,0) admits at most one maximum point on (z0∘,0)(z^{\circ}\_{0},0), which is z0∗z^{\*}\_{0}.

Step 2 In this step, we show the existence of a finite-NN equilibrium (Definition [2.1](https://arxiv.org/html/2512.06309v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). By continuous differentiability from Assumption [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), we take the first-order conditions for ([B.4](https://arxiv.org/html/2512.06309v1#A2.E4 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). Then, following the analysis in Step 1, any equilibrium strategy ZN∗=(ZN∗​(0),ZN∗​(1))∈ℝ0×ℝ1Z^{\ast}\_{N}=(Z^{\ast}\_{N}(0),Z^{\ast}\_{N}(1))\in\mathbb{R}\_{0}\times\mathbb{R}\_{1} must satisfy the equilibrium conditions

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | J˘N​(ZN∗;ZN∗​(v),v):=[eλN​(z)​∂zJ´N​(ZN∗;z,v)]|z=ZN∗​(v)=0,v∈{0,1}.\displaystyle\breve{J}\_{N}(Z^{\ast}\_{N};Z^{\ast}\_{N}(v),v):=\big[e^{\lambda\_{N}(z)}\partial\_{z}\acute{J}\_{N}(Z^{\*}\_{N};z,v)\big]\big|\_{z=Z^{\*}\_{N}(v)}=0,\quad v\in\{0,1\}. |  | (B.6) |

By ([2.3](https://arxiv.org/html/2512.06309v1#S2.Ex4 "2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | J˘N​(Z;z,v)=−χ​λN′​(z)​(v−ΦN​(Z;z))​z−(χ−χ0​eλN​(z))​(∂zΦN​(Z;z)​z−v+ΦN​(Z;z)).\breve{J}\_{N}(Z;z,v)=-\chi\lambda\_{N}^{\prime}(z)(v-\varPhi\_{N}(Z;z))z-\big(\chi-\chi\_{0}e^{\lambda\_{N}(z)}\big)\big(\partial\_{z}\varPhi\_{N}(Z;z)z-v+\varPhi\_{N}(Z;z)\big). |  | (B.7) |

Step 2.1 Consider the first-order conditions in ([B.6](https://arxiv.org/html/2512.06309v1#A2.E6 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) for v=0v=0 first. Denote ζN∗:=ZN∗​(1)−ZN∗​(0)>0\zeta^{\*}\_{N}:=Z^{\*}\_{N}(1)-Z^{\*}\_{N}(0)>0. Note that, for fixed ζ>0\zeta>0 and z<0z<0, by ([2.3](https://arxiv.org/html/2512.06309v1#S2.Ex1a "2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([2.3](https://arxiv.org/html/2512.06309v1#S2.Ex4 "2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ΦN​((z,ζ+z);z)=Φ¯N​(ζ),(∂zΦN)​((z,ζ+z);z)=Φ¯N′​(ζ),where\displaystyle\varPhi\_{N}((z,\zeta+z);z)=\bar{\varPhi}\_{N}(\zeta),\quad(\partial\_{z}\varPhi\_{N})((z,\zeta+z);z)=\bar{\varPhi}^{\prime}\_{N}(\zeta),\quad\mbox{where} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Φ¯N​(ζ):=𝔼​[11+q​eη¯N​(ζ)]>0,Φ¯N′​(ζ):=ζN​σ2​𝔼​[q​eη¯N​(ζ)(1+q​eη¯N​(ζ))2]>0,\displaystyle\bar{\varPhi}\_{N}(\zeta):=\mathbb{E}\bigg[\frac{1}{1+qe^{\bar{\eta}\_{N}(\zeta)}}\bigg]>0,\quad\bar{\varPhi}^{\prime}\_{N}(\zeta):=\frac{\zeta}{N\sigma^{2}}\mathbb{E}\bigg[\frac{qe^{\bar{\eta}\_{N}(\zeta)}}{\big(1+qe^{\bar{\eta}\_{N}(\zeta)}\big)^{2}}\bigg]>0, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | η¯N​(ζ):=ζ​(ζ−2​N​W)2​N​σ2.\displaystyle\bar{\eta}\_{N}(\zeta):=\frac{\zeta(\zeta-2\sqrt{N}W)}{2N\sigma^{2}}. |  | (B.8) |

Based on ([B.7](https://arxiv.org/html/2512.06309v1#A2.E7 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we define for any fixed ζ>0\zeta>0

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | F0N​(ζ;z):=J˘N​((z,ζ+z);z,0)=g1,N​(z)​Φ¯N​(ζ)+g2,N​(z)​Φ¯N′​(ζ),z<0,\displaystyle F^{N}\_{0}(\zeta;z):=\breve{J}\_{N}((z,\zeta+z);z,0)=g\_{1,N}(z)\bar{\varPhi}\_{N}(\zeta)+g\_{2,N}(z)\bar{\varPhi}^{\prime}\_{N}(\zeta),\quad z<0, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | whereg1,N​(z):=χ​z​λN′​(z)−χ+χ0​eλN​(z),g2,N​(z):=(χ0​eλN​(z)−χ)​z.\displaystyle\mbox{where}\quad g\_{1,N}(z):=\chi z\lambda^{\prime}\_{N}(z)-\chi+\chi\_{0}e^{\lambda\_{N}(z)},\quad g\_{2,N}(z):=(\chi\_{0}e^{\lambda\_{N}(z)}-\chi)z. |  | (B.9) |

Since ZN∗​(0)≤−ζN∗Z^{\*}\_{N}(0)\leq-\zeta^{\*}\_{N}, the effective domain of F0NF^{N}\_{0} in ([B](https://arxiv.org/html/2512.06309v1#A2.Ex6 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) should be (−∞,−ζ](-\infty,-\zeta]; however, for technical reasons, we extend F0NF^{N}\_{0} to the whole (−∞,0)(-\infty,0).

By Assumption [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), since g1,N′​(z)=(χ0​eλN​(z)+χ)​λN′​(z)+χ​z​λN′′​(z)<0g^{\prime}\_{1,N}(z)=(\chi\_{0}e^{\lambda\_{N}(z)}+\chi)\lambda^{\prime}\_{N}(z)+\chi z\lambda^{\prime\prime}\_{N}(z)<0, the function g1,Ng\_{1,N} is strictly decreasing on (−∞,0)(-\infty,0). Further, noting that limz→−∞g1,N​(z)=∞\lim\_{z\to-\infty}g\_{1,N}(z)=\infty and limz↗0g1,N​(z)=−1\lim\_{z\nearrow 0}g\_{1,N}(z)=-1, then g1,Ng\_{1,N} has a unique zero z0⋄<0z^{\diamond}\_{0}<0, and thus g1,N​(z)<0g\_{1,N}(z)<0 for z∈(z0⋄,0)z\in(z^{\diamond}\_{0},0). We now focus on the interval (z0⋄,0)(z^{\diamond}\_{0},0). Note that g2,N′​(z)=χ0​eλN​(z)​(z​λN′​(z)+1)−χg^{\prime}\_{2,N}(z)=\chi\_{0}e^{\lambda\_{N}(z)}(z\lambda^{\prime}\_{N}(z)+1)-\chi and λN​(z)>0>λN′​(z)\lambda\_{N}(z)>0>\lambda\_{N}^{\prime}(z) for z<0z<0, then for z∈(z0⋄,0)z\in(z^{\diamond}\_{0},0),

|  |  |  |  |
| --- | --- | --- | --- |
|  | g1,N​(z)−g2,N′​(z)=z​λN′​(z)​(χ−χ0​eλN​(z))=z​λN′​(z)​(z​λN′​(z)−g1,N​(z))>0;g\_{1,N}(z)-g^{\prime}\_{2,N}(z)=z\lambda^{\prime}\_{N}(z)\big(\chi-\chi\_{0}e^{\lambda\_{N}(z)}\big)=z\lambda^{\prime}\_{N}(z)\big(z\lambda^{\prime}\_{N}(z)-g\_{1,N}(z)\big)>0; |  | (B.10) |

thus g2,N′​(z)<g1,N​(z)<0g^{\prime}\_{2,N}(z)<g\_{1,N}(z)<0. Since Φ¯N,Φ¯N′>0\bar{\varPhi}\_{N},\bar{\varPhi}^{\prime}\_{N}>0 on (0,∞)(0,\infty), this implies that F0N​(ζ;⋅)F^{N}\_{0}(\zeta;\cdot), along with g2,Ng\_{2,N}, is strictly decreasing on (z0⋄,0)(z^{\diamond}\_{0},0). Moreover, since limz↗0g2,N​(z)=0\lim\_{z\nearrow 0}g\_{2,N}(z)=0, then g2,N​(z0⋄)>0g\_{2,N}(z^{\diamond}\_{0})>0, and F0N​(ζ;z⋄)=g2,N​(z0⋄)​Φ¯N′​(ζ)>0F^{N}\_{0}(\zeta;z^{\diamond})=g\_{2,N}(z^{\diamond}\_{0})\bar{\varPhi}^{\prime}\_{N}(\zeta)>0, with limz↗0F0N​(ζ;z)=−Φ¯N​(ζ)<0\lim\_{z\nearrow 0}F^{N}\_{0}(\zeta;z)=-\bar{\varPhi}\_{N}(\zeta)<0. Thus, F0N​(ζ;⋅)F^{N}\_{0}(\zeta;\cdot) has a unique zero in (z0⋄,0)(z^{\diamond}\_{0},0), denoted as 𝓏0​(ζ)\mathcal{z}\_{0}(\zeta).

Denote 𝓏1​(ζ):=ζ+𝓏0​(ζ)\mathcal{z}\_{1}(\zeta):=\zeta+\mathcal{z}\_{0}(\zeta) and 𝒵ζ:=(𝓏0​(ζ),𝓏1​(ζ))\mathcal{Z}^{\zeta}:=(\mathcal{z}\_{0}(\zeta),\mathcal{z}\_{1}(\zeta)). Recall the function ΛN\varLambda\_{N} and the point z0∘z^{\circ}\_{0} from Step 1. From ([B.10](https://arxiv.org/html/2512.06309v1#A2.E10 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) we also see that ΛN​(z)=e−λN​(z)​(χ−χ0​eλN​(z))>0\varLambda\_{N}(z)=e^{-\lambda\_{N}(z)}(\chi-\chi\_{0}e^{\lambda\_{N}(z)})>0 for z∈(z0⋄,0)z\in(z^{\diamond}\_{0},0), which implies that (z0⋄,0)⊂(z0∘,0)(z^{\diamond}\_{0},0)\subset(z^{\circ}\_{0},0), and thus, from Step 1, J´N​(𝒵ζ;⋅,0)\acute{J}\_{N}(\mathcal{Z}^{\zeta};\cdot,0) is strictly log-concave on (z0⋄,0)(z^{\diamond}\_{0},0). It then follows from the first-order condition ([B.6](https://arxiv.org/html/2512.06309v1#A2.E6 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and Step 1 that 𝓏0​(ζ)\mathcal{z}\_{0}(\zeta) is the (unique) maximum point of J´N​(𝒵ζ;⋅,0)\acute{J}\_{N}(\mathcal{Z}^{\zeta};\cdot,0) in ℝ0\mathbb{R}\_{0}. We remark that the above analysis does not require 𝓏1​(ζ)>0\mathcal{z}\_{1}(\zeta)>0, which will be verified later for the equilibrium however.

For the purpose of the next sub-step, let us also note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | F0N​(ζ;𝓏0​(ζ))=g1,N​(𝓏0​(ζ))​Φ¯N​(ζ)+g2,N​(𝓏0​(ζ))​Φ¯N′​(ζ)=0.F^{N}\_{0}(\zeta;\mathcal{z}\_{0}(\zeta))=g\_{1,N}(\mathcal{z}\_{0}(\zeta))\bar{\varPhi}\_{N}(\zeta)+g\_{2,N}(\mathcal{z}\_{0}(\zeta))\bar{\varPhi}^{\prime}\_{N}(\zeta)=0. |  | (B.11) |

Since g1,N,g2,Ng\_{1,N},g\_{2,N} are continuous and strictly decreasing on (z0⋄,0)(z^{\diamond}\_{0},0), and Φ¯N,Φ¯N′\bar{\varPhi}\_{N},\bar{\varPhi}^{\prime}\_{N} are obviously continuous in ζ\zeta, it is clear that 𝓏0​(ζ)\mathcal{z}\_{0}(\zeta) is continuous in ζ\zeta. Moreover, from ([B](https://arxiv.org/html/2512.06309v1#A2.Ex4 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) one can easily see that Φ¯N​(0)=1\bar{\varPhi}\_{N}(0)=1, Φ¯N′​(0)=0\bar{\varPhi}^{\prime}\_{N}(0)=0.
Hence, by ([B.11](https://arxiv.org/html/2512.06309v1#A2.E11 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we have that limζ↘0g1,N​(𝓏0​(ζ))=0\lim\_{\zeta\searrow 0}g\_{1,N}(\mathcal{z}\_{0}(\zeta))=0, and so

|  |  |  |  |
| --- | --- | --- | --- |
|  | limζ↘0𝓏0​(ζ)=z0⋄.\lim\_{\zeta\searrow 0}\mathcal{z}\_{0}(\zeta)=z^{\diamond}\_{0}. |  | (B.12) |

Step 2.2 Now we turn to ([B.6](https://arxiv.org/html/2512.06309v1#A2.E6 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) for v=1v=1, restricting to 𝒵ζ:=(𝓏0​(ζ),𝓏1​(ζ))\mathcal{Z}^{\zeta}:=(\mathcal{z}\_{0}(\zeta),\mathcal{z}\_{1}(\zeta)) based on Step 2.1.
We stress again that at this point, we do not require 𝓏1​(ζ)>0\mathcal{z}\_{1}(\zeta)>0. Note that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ΦN​((z−ζ,z);z)=Φ^N​(ζ),(∂zΦN)​((z−ζ,z);z)=Φ^N′​(ζ),where\displaystyle\varPhi\_{N}((z-\zeta,z);z)=\hat{\varPhi}\_{N}(\zeta),\quad(\partial\_{z}\varPhi\_{N})((z-\zeta,z);z)=\hat{\varPhi}^{\prime}\_{N}(\zeta),\quad\mbox{where} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Φ^N​(ζ):=𝔼​[11+q​eη^N​(ζ)]>0,Φ^N′​(ζ):=ζN​σ2​𝔼​[q​eη^N​(ζ)(1+q​eη^N​(ζ))2]>0,\displaystyle\hat{\varPhi}\_{N}(\zeta):=\mathbb{E}\bigg[\frac{1}{1+qe^{\hat{\eta}\_{N}(\zeta)}}\bigg]>0,\quad\hat{\varPhi}^{\prime}\_{N}(\zeta):=\frac{\zeta}{N\sigma^{2}}\mathbb{E}\bigg[\frac{qe^{\hat{\eta}\_{N}(\zeta)}}{\big(1+qe^{\hat{\eta}\_{N}(\zeta)}\big)^{2}}\bigg]>0, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | η^N​(ζ):=−ζ​(ζ+2​N​W)2​N​σ2.\displaystyle\hat{\eta}\_{N}(\zeta):=-\frac{\zeta(\zeta+2\sqrt{N}W)}{2N\sigma^{2}}. |  | (B.13) |

Recalling ([B.7](https://arxiv.org/html/2512.06309v1#A2.E7 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([B](https://arxiv.org/html/2512.06309v1#A2.Ex6 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | G1N​(ζ):=J˘N​(𝒵ζ;𝓏1​(ζ),1)=g1,N​(𝓏1​(ζ))​(Φ^N​(ζ)−1)+g2,N​(𝓏1​(ζ))​Φ^N′​(ζ).\displaystyle G^{N}\_{1}(\zeta):=\breve{J}\_{N}(\mathcal{Z}^{\zeta};\mathcal{z}\_{1}(\zeta),1)=g\_{1,N}(\mathcal{z}\_{1}(\zeta))\big(\hat{\varPhi}\_{N}(\zeta)-1\big)+g\_{2,N}(\mathcal{z}\_{1}(\zeta))\hat{\varPhi}^{\prime}\_{N}(\zeta). |  | (B.14) |

Note that 𝓏1​(ζ)=ζ+𝓏0​(ζ)\mathcal{z}\_{1}(\zeta)=\zeta+\mathcal{z}\_{0}(\zeta) is continuous for ζ>0\zeta>0 and 𝓏0​(ζ)>z0⋄\mathcal{z}\_{0}(\zeta)>z^{\diamond}\_{0}. By ([B.12](https://arxiv.org/html/2512.06309v1#A2.E12 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) we have limζ↘0𝓏1​(ζ)=z0⋄<0\lim\_{\zeta\searrow 0}\mathcal{z}\_{1}(\zeta)=z^{\diamond}\_{0}<0 and limζ→∞𝓏1​(ζ)=∞\lim\_{\zeta\to\infty}\mathcal{z}\_{1}(\zeta)=\infty. It is implied that there exists ζ˘>0\breve{\zeta}>0 such that 𝓏1​(ζ˘)=0\mathcal{z}\_{1}(\breve{\zeta})=0, and we choose the largest such ζ˘\breve{\zeta}, i.e., such that 𝓏1​(ζ)>0\mathcal{z}\_{1}(\zeta)>0 for all ζ>ζ˘\zeta>\breve{\zeta}. Since Φ^N​(ζ˘)<1\hat{\varPhi}\_{N}(\breve{\zeta})<1, then by ([B](https://arxiv.org/html/2512.06309v1#A2.Ex6 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([B.14](https://arxiv.org/html/2512.06309v1#A2.E14 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | limζ↘ζ˘G1N​(ζ)=(χ−χ0​eλN​(0))​(1−Φ^N​(ζ˘))=1−Φ^N​(ζ˘)>0.\lim\_{\zeta\searrow\breve{\zeta}}G^{N}\_{1}(\zeta)=\big(\chi-\chi\_{0}e^{\lambda\_{N}(0)}\big)\big(1-\hat{\varPhi}\_{N}(\breve{\zeta})\big)=1-\hat{\varPhi}\_{N}(\breve{\zeta})>0. |  | (B.15) |

On the other hand, since g1,N​(0)=−χ+χ0=−1<0g\_{1,N}(0)=-\chi+\chi\_{0}=-1<0, and clearly limz→∞g1,N​(z)=∞\lim\_{z\to\infty}g\_{1,N}(z)=\infty, then there exists z^∈(0,∞)\hat{z}\in(0,\infty) such that g1,N​(z^)=0g\_{1,N}(\hat{z})=0. In particular, this implies that χ0​eλN​(z^)−χ=−χ​z^​λN′​(z^)<0\chi\_{0}e^{\lambda\_{N}(\hat{z})}-\chi=-\chi\hat{z}\lambda^{\prime}\_{N}(\hat{z})<0, and so g2,N​(z^)=(χ0​eλN​(z^)−χ)​z^<0g\_{2,N}(\hat{z})=(\chi\_{0}e^{\lambda\_{N}(\hat{z})}-\chi)\hat{z}<0. Moreover, recalling again that 𝓏1​(ζ)\mathcal{z}\_{1}(\zeta) is continuous with 𝓏1​(ζ˘)=0\mathcal{z}\_{1}(\breve{\zeta})=0 and limζ→∞𝓏1​(ζ)=∞\lim\_{\zeta\to\infty}\mathcal{z}\_{1}(\zeta)=\infty, then there exists ζ^>ζ˘\hat{\zeta}>\breve{\zeta} such that 𝓏1​(ζ^)=z^\mathcal{z}\_{1}(\hat{\zeta})=\hat{z}. Therefore,

|  |  |  |
| --- | --- | --- |
|  | G1N​(ζ^)=g1,N​(z^)​(Φ^N​(ζ^)−1)+g2,N​(z^)​Φ^N′​(ζ^)=g2,N​(z^)​Φ^N′​(ζ^)<0.G^{N}\_{1}(\hat{\zeta})=g\_{1,N}(\hat{z})\big(\hat{\varPhi}\_{N}(\hat{\zeta})-1\big)+g\_{2,N}(\hat{z})\hat{\varPhi}^{\prime}\_{N}(\hat{\zeta})=g\_{2,N}(\hat{z})\hat{\varPhi}^{\prime}\_{N}(\hat{\zeta})<0. |  |

This, together with ([B.15](https://arxiv.org/html/2512.06309v1#A2.E15 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), implies that there exists ζ∗∈(ζ˘,ζ^)\zeta^{\*}\in(\breve{\zeta},\hat{\zeta}) such that G1N​(ζ∗)=0G^{N}\_{1}(\zeta^{\*})=0.

Finally, since ζ˘\breve{\zeta} is the largest zero of 𝓏1\mathcal{z}\_{1} and ζ∗>ζ˘\zeta^{\*}>\breve{\zeta}, we have 𝓏1​(ζ∗)>0\mathcal{z}\_{1}(\zeta^{\*})>0. Then, by the reasoning in Step 2.1 and Step 1 again, it follows that 𝓏1​(ζ∗)\mathcal{z}\_{1}(\zeta^{\*}) is also the unique maximum point of J´N​(𝒵ζ∗;⋅,1)\acute{J}\_{N}(\mathcal{Z}^{\zeta^{\*}};\cdot,1) on ℝ1\mathbb{R}\_{1}. This, together with Step 2.1, implies that (𝒵ζ∗,PN​(𝒵ζ∗;⋅))(\mathcal{Z}^{\zeta^{\*}},P\_{N}(\mathcal{Z}^{\zeta^{\*}};\cdot)) is an equilibrium in the sense of Definition [2.1](https://arxiv.org/html/2512.06309v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), as required.
∎

Proof of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") Assertion (ii). We shall prove the “if” direction and the “only if” direction separately. Let us recall Definition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") condition (ii), ([2.3.1](https://arxiv.org/html/2512.06309v1#S2.E1b "In 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), ([2.2.1](https://arxiv.org/html/2512.06309v1#S2.E1a "In 2.2 Composition of legal penalties ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) with C0=0C\_{0}=0, and ([2.3.6](https://arxiv.org/html/2512.06309v1#S2.E6 "In 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). We see that, for any γ\gamma-limiting equilibrium (Z~γ∗,P~γ∗)(\tilde{Z}^{\*}\_{\gamma},\tilde{P}^{\*}\_{\gamma}) (Z~γ∗≡(Z~γ∗​(0),Z~γ∗​(1))\tilde{Z}^{\ast}\_{\gamma}\equiv(\tilde{Z}^{\ast}\_{\gamma}(0),\tilde{Z}^{\ast}\_{\gamma}(1))),

|  |  |  |  |
| --- | --- | --- | --- |
|  | J~∞γ​(P~γ∗;z~,v)\displaystyle\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v) | =limN→∞N−γJN(P~∞γ(Z~γ∗;N−max⁡{γ,12}⋅);Nγz~,v)\displaystyle=\lim\_{N\to\infty}N^{-\gamma}J\_{N}\big(\tilde{P}^{\gamma}\_{\infty}(\tilde{Z}^{\*}\_{\gamma};N^{-\max\{\gamma,\frac{1}{2}\}}\cdot);N^{\gamma}\tilde{z},v\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =limN→∞N−γ​(Nγ​z~)​(e−λN​(Nγ​z~)−χ0​(1−e−λN​(Nγ​z~)))​(v−Φ~Nγ​(Z~γ∗;z~))\displaystyle=\lim\_{N\to\infty}N^{-\gamma}(N^{\gamma}\tilde{z})~\Big(e^{-\lambda\_{N}(N^{\gamma}\tilde{z})}-\chi\_{0}(1-e^{-\lambda\_{N}(N^{\gamma}\tilde{z})})\Big)\Big(v-\tilde{\varPhi}^{\gamma}\_{N}(\tilde{Z}^{\*}\_{\gamma};\tilde{z})\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =limN→∞z~​(χ​e−λ​(Nγ−β​z~)−χ0)​(v−Φ~Nγ​(Z~γ∗;z~)),z~∈ℝv,v∈{0,1},\displaystyle=\lim\_{N\to\infty}\tilde{z}~\big(\chi e^{-\lambda(N^{\gamma-\beta}\tilde{z})}-\chi\_{0}\big)\big(v-\tilde{\varPhi}^{\gamma}\_{N}(\tilde{Z}^{\*}\_{\gamma};\tilde{z})\big),\quad\tilde{z}\in\mathbb{R}\_{v},\;v\in\{0,1\}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | where | Φ~Nγ​(Z~γ∗;z~):=𝔼​[P~∞γ​(Z~γ∗;N−max⁡{γ,12}​(N​W+Nγ​z~))],\displaystyle\tilde{\varPhi}^{\gamma}\_{N}(\tilde{Z}^{\*}\_{\gamma};\tilde{z}):=\mathbb{E}\big[\tilde{P}^{\gamma}\_{\infty}(\tilde{Z}^{\*}\_{\gamma};N^{-\max\{\gamma,\frac{1}{2}\}}(\sqrt{N}W+N^{\gamma}\tilde{z}))\big], |  | (B.16) |

with λ≡λ1\lambda\equiv\lambda\_{1}. Under Assumption [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), we can easily verify the following limits: For z~≠0\tilde{z}\neq 0, with zγ∗:=(Z~γ∗​(0)+Z~γ∗​(1))/2z^{\*}\_{\gamma}:=(\tilde{Z}^{\*}\_{\gamma}(0)+\tilde{Z}^{\*}\_{\gamma}(1))/2,

|  |  |  |  |
| --- | --- | --- | --- |
|  | limN→∞e−λ​(Nγ−β​z~)={1,if ​γ<β,λ​(z~),if ​γ=β,0,if ​γ>β;limN→∞Φ~Nγ​(Z~γ∗;z~)={p,if ​γ<12,Φ1​(Z~γ∗;z~),if ​γ=12,𝟙{z~>zγ∗}+12​𝟙{z~=zγ∗},if ​γ>12;\lim\_{N\to\infty}e^{-\lambda(N^{\gamma-\beta}\tilde{z})}=\begin{cases}1,\quad&~\text{if }\gamma<\beta,\\ \lambda(\tilde{z}),&~\text{if }\gamma=\beta,\\ 0,\quad&~\text{if }\gamma>\beta;\end{cases}\quad\lim\_{N\to\infty}\tilde{\varPhi}^{\gamma}\_{N}(\tilde{Z}^{\*}\_{\gamma};\tilde{z})=\begin{cases}p,&~\text{if }\gamma<\frac{1}{2},\\ \varPhi\_{1}(\tilde{Z}^{\*}\_{\gamma};\tilde{z}),&~\text{if }\gamma=\frac{1}{2},\\ \mathds{1}\_{\{\tilde{z}>z^{\*}\_{\gamma}\}}+\frac{1}{2}\mathds{1}\_{\{\tilde{z}=z^{\*}\_{\gamma}\}},&~\text{if }\gamma>\frac{1}{2};\end{cases} |  | (B.17) |

in particular, the case γ>1/2\gamma>1/2 follows by using ([3.2](https://arxiv.org/html/2512.06309v1#S3.E2 "In Proposition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([B](https://arxiv.org/html/2512.06309v1#A2.Ex10 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) so that

|  |  |  |
| --- | --- | --- |
|  | Φ~Nγ​(Z~γ∗;z~)=𝔼​[𝟙{N1/2−γ​W+z~>zγ∗}+p​𝟙{N1/2−γ​W+z~=zγ∗}]→𝟙{z~>zγ∗}+12​𝟙{z~=zγ∗}.\displaystyle\tilde{\varPhi}^{\gamma}\_{N}(\tilde{Z}^{\*}\_{\gamma};\tilde{z})=\mathbb{E}\big[\mathds{1}\_{\{N^{{1/2}-\gamma}W+\tilde{z}>z^{\*}\_{\gamma}\}}+p\mathds{1}\_{\{N^{{1/2}-\gamma}W+\tilde{z}=z^{\*}\_{\gamma}\}}\big]\to\mathds{1}\_{\{\tilde{z}>z^{\*}\_{\gamma}\}}+\tfrac{1}{2}\mathds{1}\_{\{\tilde{z}=z^{\*}\_{\gamma}\}}. |  |

Step 1 In this step we prove the “if” direction. Assume γ=min⁡{β,1/2}\gamma=\min\{\beta,1/2\}. We naturally examine ([B](https://arxiv.org/html/2512.06309v1#A2.Ex10 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) in two cases.

Case 1 γ=β<1/2\gamma=\beta<1/2. In this case, by Definition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") (ii) and ([3.3](https://arxiv.org/html/2512.06309v1#S3.E3 "In 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) from Proposition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmproposition1 "Proposition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), we must set P~γ∗=p\tilde{P}^{\*}\_{\gamma}=p, and it is unique. Further, ([B](https://arxiv.org/html/2512.06309v1#A2.Ex10 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) gives that

|  |  |  |  |
| --- | --- | --- | --- |
|  | J~∞γ​(P~γ∗;z~,v)=(v−p)​z~​(χ​e−λ​(z~)−χ0),z~∈ℝv.\displaystyle\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=(v-p)\tilde{z}~\big(\chi e^{-\lambda(\tilde{z})}-\chi\_{0}\big),\quad\tilde{z}\in\mathbb{R}\_{v}. |  | (B.18) |

Similar to ([B.6](https://arxiv.org/html/2512.06309v1#A2.E6 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we define for z~∈ℝv\tilde{z}\in\mathbb{R}\_{v}

|  |  |  |  |
| --- | --- | --- | --- |
|  | J˘∞γ​(z~,v)\displaystyle\breve{J}^{\gamma}\_{\infty}(\tilde{z},v) | :=eλ​(z~)​∂z~J~∞γ​(P~γ∗;z~,v)=(v−p)​(χ−χ​z~​λ′​(z~)−χ0​eλ​(z~));\displaystyle:=e^{\lambda(\tilde{z})}\partial\_{\tilde{z}}\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=(v-p)\big(\chi-\chi\tilde{z}\lambda^{\prime}(\tilde{z})-\chi\_{0}e^{\lambda(\tilde{z})}\big); |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂z~J˘∞γ​(z~,v)\displaystyle\partial\_{\tilde{z}}\breve{J}^{\gamma}\_{\infty}(\tilde{z},v) | =−(v−p)​(χ​λ′​(z~)+χ​z~​λ′′​(z~)+χ0​eλ​(z~)​λ′​(z~)).\displaystyle=-(v-p)\big(\chi\lambda^{\prime}(\tilde{z})+\chi\tilde{z}\lambda^{\prime\prime}(\tilde{z})+\chi\_{0}e^{\lambda(\tilde{z})}\lambda^{\prime}(\tilde{z})\big). |  | (B.19) |

When v=0v=0, by Assumption [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), one can easily see that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | limz~↗0J~∞γ​(P~γ∗;z~,0)=0,limz~→−∞J~∞γ​(P~γ∗;z~,0)=−∞;\displaystyle\lim\_{\tilde{z}\nearrow 0}\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},0)=0,\quad\lim\_{\tilde{z}\to-\infty}\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},0)=-\infty; |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | limz~↗0J˘∞γ​(z~,0)=−p<0,limz~→−∞J˘∞γ​(z~,0)=∞;∂z~J˘∞γ​(z~,0)<0,z~<0.\displaystyle\lim\_{\tilde{z}\nearrow 0}\breve{J}^{\gamma}\_{\infty}(\tilde{z},0)=-p<0,\quad\lim\_{\tilde{z}\to-\infty}\breve{J}^{\gamma}\_{\infty}(\tilde{z},0)=\infty;\quad\partial\_{\tilde{z}}\breve{J}^{\gamma}\_{\infty}(\tilde{z},0)<0,\quad\tilde{z}<0. |  | (B.20) |

Based on the first and third limits in ([B](https://arxiv.org/html/2512.06309v1#A2.Ex15 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we have that J~∞γ​(P~γ∗;z~,0)>0\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},0)>0 when z~<0\tilde{z}<0 is close to 0. Along with the second limit, this implies that the function J~∞γ​(P~γ∗;z~,0)\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},0) has a maximum point Z~γ∗​(0)∈(−∞,0)\tilde{Z}^{\*}\_{\gamma}(0)\in(-\infty,0), with J~∞γ​(P~γ∗;Z~γ∗​(0),0)\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{Z}^{\*}\_{\gamma}(0),0)>0. Clearly, ∂z~J~∞γ​(P~γ∗;Z~γ∗​(0),0)=0\partial\_{\tilde{z}}\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{Z}^{\*}\_{\gamma}(0),0)=0. Also, from the second line of ([B](https://arxiv.org/html/2512.06309v1#A2.Ex15 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we see that J˘∞γ​(z~,0)\breve{J}^{\gamma}\_{\infty}(\tilde{z},0), and hence ∂z~J~∞γ​(P~γ∗;z~,0)\partial\_{\tilde{z}}\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},0), has a unique zero. Thus, Z~γ∗​(0)\tilde{Z}^{\*}\_{\gamma}(0) is the unique maximum point of J~∞γ​(P~γ∗;⋅,0)\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\cdot,0) in (−∞,0)(-\infty,0).

Similarly, when v=1v=1, we have

|  |  |  |
| --- | --- | --- |
|  | limz~↘0J~∞γ​(P~γ∗;z~,1)=0,limz~→∞J~∞γ​(P~γ∗;z~,1)=−∞;\displaystyle\lim\_{\tilde{z}\searrow 0}\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},1)=0,\quad\lim\_{\tilde{z}\to\infty}\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},1)=-\infty; |  |
|  |  |  |
| --- | --- | --- |
|  | limz~↘0J˘∞γ​(z~,1)=1−p>0,limz~→∞J˘∞γ​(z~,1)=−∞;∂z~J˘∞γ​(z~,1)<0,z~>0.\displaystyle\lim\_{\tilde{z}\searrow 0}\breve{J}^{\gamma}\_{\infty}(\tilde{z},1)=1-p>0,\quad\lim\_{\tilde{z}\to\infty}\breve{J}^{\gamma}\_{\infty}(\tilde{z},1)=-\infty;\quad\partial\_{\tilde{z}}\breve{J}^{\gamma}\_{\infty}(\tilde{z},1)<0,\quad\tilde{z}>0. |  |

By similar observations it follows that J~∞γ​(P~γ∗;z~,1)\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},1) has a unique maximum point Z~γ∗​(1)∈(0,∞)\tilde{Z}^{\*}\_{\gamma}(1)\in(0,\infty), with J~∞γ​(P~γ∗;Z~γ∗​(1),1)\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{Z}^{\*}\_{\gamma}(1),1)>0. Therefore, Z~γ∗=(Z~γ∗​(0),Z~γ∗​(1))\tilde{Z}^{\*}\_{\gamma}=(\tilde{Z}^{\*}\_{\gamma}(0),\tilde{Z}^{\*}\_{\gamma}(1)) and P~γ∗≡p\tilde{P}^{\*}\_{\gamma}\equiv p together constitute the unique γ\gamma-limiting equilibrium.

Case 2 γ=1/2≤β\gamma=1/2\leq\beta. In this case, by ([3.2](https://arxiv.org/html/2512.06309v1#S3.E2 "In Proposition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), ([B](https://arxiv.org/html/2512.06309v1#A2.Ex10 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), and ([2.3](https://arxiv.org/html/2512.06309v1#S2.Ex4 "2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) (with N=1N=1), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | J~∞γ​(P~γ∗;z~,v)=limN→∞(χ​e−λ​(Nγ−β​z~)−χ0)​Q1​(Z~γ∗;z~,v),z~∈ℝv.\displaystyle\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=\lim\_{N\to\infty}\big(\chi e^{-\lambda(N^{\gamma-\beta}\tilde{z})}-\chi\_{0}\big)Q\_{1}(\tilde{Z}^{\*}\_{\gamma};\tilde{z},v),\quad\tilde{z}\in\mathbb{R}\_{v}. |  | (B.21) |

When β=1/2\beta=1/2, this is the same as ([B.4](https://arxiv.org/html/2512.06309v1#A2.E4 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) with N=1N=1, and by assertion (i) of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") we know that there exists a γ\gamma-limiting equilibrium.

Now consider the case β>1/2=γ\beta>1/2=\gamma. Then J~∞γ​(P~γ∗;z~,v)=Q1​(Z~γ∗;z~,v)\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=Q\_{1}(\tilde{Z}^{\*}\_{\gamma};\tilde{z},v), z~∈ℝv\tilde{z}\in\mathbb{R}\_{v},
which is in the form of ([B.4](https://arxiv.org/html/2512.06309v1#A2.E4 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) with N=1N=1 and λ=0\lambda=0 (hence violating Assumption [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). In particular, ([B](https://arxiv.org/html/2512.06309v1#A2.Ex6 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) becomes (using zz instead of z~\tilde{z} and fixed ζ>0\zeta>0) F01​(ζ;z)=−Φ¯1​(ζ)−z​Φ¯1′​(ζ)F^{1}\_{0}(\zeta;z)=-\bar{\varPhi}\_{1}(\zeta)-z\bar{\varPhi}^{\prime}\_{1}(\zeta), z<0z<0,
with a unique zero 𝓏0​(ζ):=−Φ¯1​(ζ)/Φ¯1′​(ζ)<0\mathcal{z}\_{0}(\zeta):=-\bar{\varPhi}\_{1}(\zeta)/\penalty 50\bar{\varPhi}\_{1}^{\prime}(\zeta)<0. We claim that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limζ↘0𝓏0​(ζ)=−∞,limζ→∞𝓏0​(ζ)=0.\lim\_{\zeta\searrow 0}\mathcal{z}\_{0}(\zeta)=-\infty,\quad\lim\_{\zeta\to\infty}\mathcal{z}\_{0}(\zeta)=0. |  | (B.22) |

From ([B](https://arxiv.org/html/2512.06309v1#A2.Ex4 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), the first limit is obvious. To see the second limit, consider an arbitrary c>0c>0 and the function

|  |  |  |
| --- | --- | --- |
|  | Φ¯1c​(ζ):=Φ¯1​(ζ)−c​Φ¯1′​(ζ)=𝔼​[1+q​(1−c​ζσ2)​eη¯1​(ζ)(1+q​eη¯1​(ζ))2].\displaystyle\bar{\varPhi}^{c}\_{1}(\zeta):=\bar{\varPhi}\_{1}(\zeta)-c\bar{\varPhi}^{\prime}\_{1}(\zeta)=\mathbb{E}\bigg[\frac{1+q\big(1-\frac{c\zeta}{\sigma^{2}}\big)e^{\bar{\eta}\_{1}(\zeta)}}{\big(1+qe^{\bar{\eta}\_{1}(\zeta)}\big)^{2}}\bigg]. |  |

Recall that W​=d.​Normal​(0,σ2)W\overset{\rm d.}{=}\text{Normal}(0,\sigma^{2}). By ([B](https://arxiv.org/html/2512.06309v1#A2.Ex4 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), η¯1​(ζ)=ζ​(ζ−2​W)/(2​σ2)​=d.​Normal​(ζ2/(2​σ2),ζ2/σ2)\bar{\eta}\_{1}(\zeta)={\zeta(\zeta-2W)/(2\sigma^{2})}\overset{\rm d.}{=}\text{Normal}({\zeta^{2}/(2\sigma^{2})},{\zeta^{2}/\sigma^{2}}). After some rearrangement, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ¯1c​(ζ)\displaystyle\bar{\varPhi}^{c}\_{1}(\zeta) | =∫ℝ1+q​(1−c​ζσ2)​ex(1+q​ex)2​σ2​π​ζ​exp⁡(−σ2​(x−ζ22​σ2)22​ζ2)​dx\displaystyle=\int\_{\mathbb{R}}\frac{1+q\big(1-\frac{c\zeta}{\sigma^{2}}\big)e^{x}}{\big(1+qe^{x}\big)^{2}}\frac{\sigma}{\sqrt{2\pi}\zeta}\exp\bigg(-\frac{\sigma^{2}\big(x-\frac{\zeta^{2}}{2\sigma^{2}}\big)^{2}}{2\zeta^{2}}\bigg){\rm d}x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =σ​e−ζ28​σ22​π​ζ​(A¯1​(ζ)+q​(1−c​ζσ2)​A¯2​(ζ)),\displaystyle=\frac{\sigma e^{-\frac{\zeta^{2}}{8\sigma^{2}}}}{\sqrt{2\pi}\zeta}\Big(\bar{A}\_{1}(\zeta)+q\big(1-\tfrac{c\zeta}{\sigma^{2}}\big)\bar{A}\_{2}(\zeta)\Big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | where | A¯1​(ζ):=∫ℝe−σ22​ζ2​x2+12​x(1+q​ex)2​dx,A¯2​(ζ):=∫ℝe−σ22​ζ2​x2+32​x(1+q​ex)2​dx.\displaystyle\bar{A}\_{1}(\zeta):=\int\_{\mathbb{R}}\frac{e^{-\frac{\sigma^{2}}{2\zeta^{2}}x^{2}+\frac{1}{2}x}}{\big(1+qe^{x}\big)^{2}}{\rm d}x,\quad\bar{A}\_{2}(\zeta):=\int\_{\mathbb{R}}\frac{e^{-\frac{\sigma^{2}}{2\zeta^{2}}x^{2}+\frac{3}{2}x}}{\big(1+qe^{x}\big)^{2}}{\rm d}x. |  |

Then, note that

|  |  |  |
| --- | --- | --- |
|  | limζ→∞A¯1​(ζ)=∫ℝe12​x(1+q​ex)2​dx∈(0,∞),limζ→∞A¯2​(ζ)=∫ℝe32​x(1+q​ex)2​dx∈(0,∞).\displaystyle\lim\_{\zeta\to\infty}\bar{A}\_{1}(\zeta)=\int\_{\mathbb{R}}\frac{e^{\frac{1}{2}x}}{\big(1+qe^{x}\big)^{2}}{\rm d}x\in(0,\infty),\quad\lim\_{\zeta\to\infty}\bar{A}\_{2}(\zeta)=\int\_{\mathbb{R}}\frac{e^{\frac{3}{2}x}}{\big(1+qe^{x}\big)^{2}}{\rm d}x\in(0,\infty). |  |

Thus, it is clear that limζ→∞(A¯1​(ζ)+q​(1−c​ζ/σ2)​A¯2​(ζ))=−∞\lim\_{\zeta\to\infty}\big(\bar{A}\_{1}(\zeta)+q(1-c\zeta/\penalty 50\sigma^{2})\bar{A}\_{2}(\zeta)\big)=-\infty, which implies that Φ¯1c​(ζ)<0\bar{\varPhi}^{c}\_{1}(\zeta)<0 for ζ>0\zeta>0 sufficiently large. Thus, Φ¯1​(ζ)−c​Φ¯1′​(ζ)<0\bar{\varPhi}\_{1}(\zeta)-c\bar{\varPhi}^{\prime}\_{1}(\zeta)<0 and 𝓏0​(ζ)=−Φ¯1​(ζ)/Φ¯1′​(ζ)≥−c\mathcal{z}\_{0}(\zeta)=-\bar{\varPhi}\_{1}(\zeta)/\penalty 50\bar{\varPhi}\_{1}^{\prime}(\zeta)\geq-c for all sufficiently large ζ\zeta. Since c>0c>0 is arbitrary, we must have limζ→∞𝓏0​(ζ)=0\lim\_{\zeta\to\infty}\mathcal{z}\_{0}(\zeta)=0.

Next we analyze G11​(ζ)G^{1}\_{1}(\zeta). In particular, ([B.14](https://arxiv.org/html/2512.06309v1#A2.E14 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | G11​(ζ)=−(Φ^1​(ζ)−1)−𝓏1​(ζ)​Φ^1′​(ζ),𝓏1​(ζ)=ζ+𝓏0​(ζ).G^{1}\_{1}(\zeta)=-\big(\hat{\varPhi}\_{1}(\zeta)-1\big)-\mathcal{z}\_{1}(\zeta)\hat{\varPhi}^{\prime}\_{1}(\zeta),\quad\mathcal{z}\_{1}(\zeta)=\zeta+\mathcal{z}\_{0}(\zeta). |  | (B.23) |

By ([B.22](https://arxiv.org/html/2512.06309v1#A2.E22 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we have that limζ↘0𝓏1​(ζ)=−∞\lim\_{\zeta\searrow 0}\mathcal{z}\_{1}(\zeta)=-\infty and limζ→∞𝓏1​(ζ)=∞\lim\_{\zeta\to\infty}\mathcal{z}\_{1}(\zeta)=\infty.
Thus, there exists ζ˘>0\breve{\zeta}>0 such that 𝓏1​(ζ˘)=0\mathcal{z}\_{1}(\breve{\zeta})=0 and 𝓏1​(ζ)>0\mathcal{z}\_{1}(\zeta)>0 for all ζ>ζ˘\zeta>\breve{\zeta}. From ([B.23](https://arxiv.org/html/2512.06309v1#A2.E23 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), clearly G11​(ζ˘)>0G^{1}\_{1}(\breve{\zeta})>0. Also, recalling ([B](https://arxiv.org/html/2512.06309v1#A2.Ex7 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and noting that η^1​(ζ)​=d.​Normal​(−ζ2/(2​σ2),ζ2/σ2)\hat{\eta}\_{1}(\zeta)\overset{\rm d.}{=}\text{Normal}(-{\zeta^{2}/(2\sigma^{2})},{\zeta^{2}/\sigma^{2}}), in a similar fashion as above,

|  |  |  |
| --- | --- | --- |
|  | G11​(ζ)=𝔼​[q​eη^1​(ζ)1+q​eη^1​(ζ)−q​eη^1​(ζ)​ζ​𝓏1​(ζ)σ2​(1+q​eη^1​(ζ))2]=σ​e−ζ28​σ22​π​ζ​(A^1​(ζ)−1q​(ζ​𝓏1​(ζ)σ2−1)​A^2​(ζ)),\displaystyle G^{1}\_{1}(\zeta)=\mathbb{E}\bigg[\frac{qe^{\hat{\eta}\_{1}(\zeta)}}{1+qe^{\hat{\eta}\_{1}(\zeta)}}-\frac{qe^{\hat{\eta}\_{1}(\zeta)}\zeta\mathcal{z}\_{1}(\zeta)}{\sigma^{2}\big(1+qe^{\hat{\eta}\_{1}(\zeta)}\big)^{2}}\bigg]=\frac{\sigma e^{-\frac{\zeta^{2}}{8\sigma^{2}}}}{\sqrt{2\pi}\zeta}\Big(\hat{A}\_{1}(\zeta)-\tfrac{1}{q}\big(\tfrac{\zeta\mathcal{z}\_{1}(\zeta)}{\sigma^{2}}-1\big)\hat{A}\_{2}(\zeta)\Big), |  |
|  |  |  |
| --- | --- | --- |
|  | whereA^1​(ζ):=∫ℝe−σ22​ζ2​x2+12​x(1+exq)2​dx,A^2​(ζ):=∫ℝe−σ22​ζ2​x2+32​x(1+exq)2​dx.\displaystyle\mbox{where}\quad\hat{A}\_{1}(\zeta):=\int\_{\mathbb{R}}\frac{e^{-\frac{\sigma^{2}}{2\zeta^{2}}x^{2}+\frac{1}{2}x}}{\big(1+\frac{e^{x}}{q}\big)^{2}}{\rm d}x,\quad\hat{A}\_{2}(\zeta):=\int\_{\mathbb{R}}\frac{e^{-\frac{\sigma^{2}}{2\zeta^{2}}x^{2}+\frac{3}{2}x}}{\big(1+\frac{e^{x}}{q}\big)^{2}}{\rm d}x. |  |

Noting that limζ→∞A^1​(ζ),limζ→∞A^2​(ζ)∈(0,∞)\lim\_{\zeta\to\infty}\hat{A}\_{1}(\zeta),\lim\_{\zeta\to\infty}\hat{A}\_{2}(\zeta)\in(0,\infty), and limζ→∞𝓏1​(ζ)=∞\lim\_{\zeta\to\infty}\mathcal{z}\_{1}(\zeta)=\infty, we have limζ→∞(A^1​(ζ)−(ζ​𝓏1​(ζ)/σ2)​A^2​(ζ))=−∞\lim\_{\zeta\to\infty}\big(\hat{A}\_{1}(\zeta)-{(\zeta\mathcal{z}\_{1}(\zeta)/\sigma^{2})}\hat{A}\_{2}(\zeta)\big)=-\infty, and so G11​(ζ)<0G^{1}\_{1}(\zeta)<0 for ζ\zeta sufficiently large. Since G11​(ζ˘)>0G^{1}\_{1}(\breve{\zeta})>0, then there exists ζ∗>ζ˘\zeta^{\*}>\breve{\zeta} such that G11​(ζ∗)=0G^{1}\_{1}(\zeta^{\*})=0. Thus, following the same arguments as in Step 2 of the proof of assertion (i), (𝒵ζ∗,P1​(𝒵ζ∗;⋅))(\mathcal{Z}^{\zeta^{\*}},P\_{1}(\mathcal{Z}^{\zeta^{\*}};\cdot)) is a γ\gamma-limiting equilibrium in the sense of Definition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading").

Step 2 We now prove the “only if” direction. Assume that there exists a γ\gamma-limiting equilibrium.

Case 3 γ<1/2\gamma<1/2. Then, from ([3.2](https://arxiv.org/html/2512.06309v1#S3.E2 "In Proposition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), P~γ∗=p\tilde{P}^{\*}\_{\gamma}=p, and so by ([B](https://arxiv.org/html/2512.06309v1#A2.Ex10 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([B.17](https://arxiv.org/html/2512.06309v1#A2.E17 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")),

|  |  |  |
| --- | --- | --- |
|  | J~∞γ​(P~γ∗;z~,v)={(v−p)​z~,if ​γ<β,(v−p)​z~​(χ​e−λ​(z)−χ0),if ​γ=β,−χ0​(v−p)​z~,if ​γ>β,z~∈ℝv.\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=\begin{cases}(v-p)\tilde{z},\qquad\qquad\quad&~\text{if }\gamma<\beta,\\ (v-p)\tilde{z}(\chi e^{-\lambda(z)}-\chi\_{0}),&~\text{if }\gamma=\beta,\\ -\chi\_{0}(v-p)\tilde{z},&~\text{if }\gamma>\beta,\end{cases}\quad\tilde{z}\in\mathbb{R}\_{v}. |  |

Clearly, in the cases γ<β\gamma<\beta and γ>β\gamma>\beta with χ0>0\chi\_{0}>0, J~∞γ​(P~γ∗;⋅,v)\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\cdot,v) has no maximum point in ℝv\mathbb{R}\_{v}. In the case γ>β\gamma>\beta with χ0=0\chi\_{0}=0, J~∞γ​(P~γ∗;z~,v)=0\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=0 for all z~∈ℝv\tilde{z}\in\mathbb{R}\_{v}, but since in Definition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") condition (i) we require J~∞γ​(P~γ∗;Z~γ∗​(v),v)≠0\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{Z}^{\*}\_{\gamma}(v),v)\neq 0, there is no such Z~γ∗​(v)\tilde{Z}^{\*}\_{\gamma}(v). Thus, we must have γ=β\gamma=\beta, and since γ<1/2\gamma<1/2, we obtain γ=min⁡{β,1/2}\gamma=\min\{\beta,1/2\}.

Case 4 γ=1/2\gamma=1/2. If β<1/2\beta<1/2, then by ([B.21](https://arxiv.org/html/2512.06309v1#A2.E21 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([B.17](https://arxiv.org/html/2512.06309v1#A2.E17 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), J~∞γ​(P~γ∗;z~,v)=−χ0​Q1​(Z~γ∗;z~,v)\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=-\chi\_{0}Q\_{1}(\tilde{Z}^{\*}\_{\gamma};\tilde{z},v), z~∈ℝv\tilde{z}\in\mathbb{R}\_{v}.
By Lemma [B.1](https://arxiv.org/html/2512.06309v1#A2.Thmlemma1 "Lemma B.1. ‣ Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), Q1​(Z~γ∗;z~,v)Q\_{1}(\tilde{Z}^{\*}\_{\gamma};\tilde{z},v) is strictly log-concave in z∈ℝvz\in\mathbb{R}\_{v}; hence, if χ0>0\chi\_{0}>0, J~∞γ​(P~γ∗;⋅,v)\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\cdot,v) has no maximum point in ℝv\mathbb{R}\_{v}, while if χ0=0\chi\_{0}=0, then J~∞γ​(P~γ∗;⋅,v)=0\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\cdot,v)=0, also a violation, and it must be that β≥1/2\beta\geq 1/2; thus, γ=min⁡{β,1/2}\gamma=\min\{\beta,1/2\}.

Case 5 γ>1/2\gamma>1/2. Then, ([B](https://arxiv.org/html/2512.06309v1#A2.Ex10 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([B.17](https://arxiv.org/html/2512.06309v1#A2.E17 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) imply that

|  |  |  |
| --- | --- | --- |
|  | J~∞γ​(P~γ∗;z~,v)=z~​(v−𝟙{z~>zγ∗}−12​𝟙{z~=zγ∗})​limN→∞(χ​e−λ​(Nγ−β​z~)−χ0),z~∈ℝv,\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=\tilde{z}\big(v-\mathds{1}\_{\{\tilde{z}>z^{\*}\_{\gamma}\}}-\tfrac{1}{2}\mathds{1}\_{\{\tilde{z}=z^{\*}\_{\gamma}\}}\big)\lim\_{N\to\infty}\big(\chi e^{-\lambda(N^{\gamma-\beta}\tilde{z})}-\chi\_{0}\big),\quad\tilde{z}\in\mathbb{R}\_{v}, |  |

with the limit being finite. When zγ∗≥0z^{\*}\_{\gamma}\geq 0, we have J~∞γ​(P~γ∗;z~,0)=0\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},0)=0 for all z~<0\tilde{z}<0, which again violates the requirement J~∞γ​(P~γ∗;Z~γ∗​(0),0)≠0\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{Z}^{\*}\_{\gamma}(0),0)\neq 0. Similarly, when zγ∗<0z^{\*}\_{\gamma}<0, we have J~∞γ​(P~γ∗;z~,1)=0\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},1)=0 for all z~>0\tilde{z}>0. Therefore, there is no γ\gamma-limiting equilibrium.
∎

Proof of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") assertion (iii). Let Assumption [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") still hold. We now prove the convergence of a finite-NN equilibrium (ZN∗,PN∗)(Z^{\*}\_{N},P^{\*}\_{N}) (Definition [2.1](https://arxiv.org/html/2512.06309v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) towards the unique γ\gamma-limiting equilibrium (Z~γ∗,P~γ∗=p)(\tilde{Z}^{\*}\_{\gamma},\tilde{P}^{\*}\_{\gamma}=p), in the case γ=β<1/2\gamma=\beta<1/2. We proceed in three steps.

Step 1 In this step, we show that z~vN:=N−γ​ZN∗​(v)\tilde{z}^{N}\_{v}:=N^{-\gamma}Z^{\*}\_{N}(v) is bounded in NN. Consider v=0v=0 first. From Step 2.1 in the proof of Assertion (i), we see that z0⋄,N<ZN∗​(0)<0z^{\diamond,N}\_{0}<Z^{\*}\_{N}(0)<0, where z0⋄,N=z0⋄z^{\diamond,N}\_{0}=z^{\diamond}\_{0} is the unique zero of g1,Ng\_{1,N} defined in ([B](https://arxiv.org/html/2512.06309v1#A2.Ex6 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). Noting that

|  |  |  |  |
| --- | --- | --- | --- |
|  | g1,N​(z)=χ​z​N−β​λ′​(N−β​z)−χ+χ0​eλ​(N−β​z)=g1,1​(N−β​z),z<0,g\_{1,N}(z)=\chi zN^{-\beta}\lambda^{\prime}(N^{-\beta}z)-\chi+\chi\_{0}e^{\lambda(N^{-\beta}z)}=g\_{1,1}(N^{-\beta}z),\quad z<0, |  | (B.24) |

then z0⋄,N=Nβ​z0⋄,1z^{\diamond,N}\_{0}=N^{\beta}z^{\diamond,1}\_{0}, where z0⋄,1z^{\diamond,1}\_{0} is the unique zero of g1,1g\_{1,1}, depending only on the model parameters. Since γ=β\gamma=\beta, we have z0⋄,1≤z~0N<0z^{\diamond,1}\_{0}\leq\tilde{z}^{N}\_{0}<0, and so z~0N\tilde{z}^{N}\_{0} is bounded. We shall put |z~0N|≤K0|\tilde{z}^{N}\_{0}|\leq K\_{0}, for some constant K0>0K\_{0}>0.

In the same fashion we can prove that |z~1N|≤K0|\tilde{z}^{N}\_{1}|\leq K\_{0} for possibly larger K0K\_{0}. Note that one may not use the function G1NG^{N}\_{1} from ([B.14](https://arxiv.org/html/2512.06309v1#A2.E14 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) for this purpose – instead, the following function that is the counterpart of F0NF^{N}\_{0} in ([B](https://arxiv.org/html/2512.06309v1#A2.Ex6 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) for v=1v=1 and satisfies G1N​(ζ)=F1N​(ζ;𝓏1​(ζ))G^{N}\_{1}(\zeta)=F^{N}\_{1}(\zeta;\mathcal{z}\_{1}(\zeta)) should be used:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F1N​(ζ;z):=J˘N​((z−ζ,z);z,1)=g1,N​(z)​(Φ^N​(ζ)−1)+g2,N​(z)​Φ^N′​(ζ),z>0.F^{N}\_{1}(\zeta;z):=\breve{J}\_{N}((z-\zeta,z);z,1)=g\_{1,N}(z)(\hat{\varPhi}\_{N}(\zeta)-1)+g\_{2,N}(z)\hat{\varPhi}^{\prime}\_{N}(\zeta),\quad z>0. |  | (B.25) |

Step 2 In this step, we prove the desired uniform convergence of FvN​(Nγ​ζ~;Nγ​z~)F^{N}\_{v}(N^{\gamma}\tilde{\zeta};N^{\gamma}\tilde{z}). Recall J˘∞γ​(z~,v)\breve{J}^{\gamma}\_{\infty}(\tilde{z},v) in ([B](https://arxiv.org/html/2512.06309v1#A2.Ex14 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). For v=0v=0, ζ~>0\tilde{\zeta}>0, and z~<0\tilde{z}<0, using ([B](https://arxiv.org/html/2512.06309v1#A2.Ex6 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) further we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |F0N​(Nγ​ζ~;Nγ​z~)−J˘∞γ​(z~,0)|\displaystyle\big|F^{N}\_{0}(N^{\gamma}\tilde{\zeta};N^{\gamma}\tilde{z})-\breve{J}^{\gamma}\_{\infty}(\tilde{z},0)\big| | =|g1,1​(z~)​Φ¯N​(Nγ​ζ~)+g2,1​(z~)​Nγ​Φ¯N′​(Nγ​ζ~)−p​g1,1​(z~)|\displaystyle=\Big|g\_{1,1}(\tilde{z})\bar{\varPhi}\_{N}(N^{\gamma}\tilde{\zeta})+g\_{2,1}(\tilde{z})N^{\gamma}\bar{\varPhi}^{\prime}\_{N}(N^{\gamma}\tilde{\zeta})-pg\_{1,1}(\tilde{z})\Big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤|g1,1​(z~)|​|Φ¯N​(Nγ​ζ~)−p|+|g2,1​(z~)|​Nγ​Φ¯N′​(Nγ​ζ~).\displaystyle\leq|g\_{1,1}(\tilde{z})|\big|\bar{\varPhi}\_{N}(N^{\gamma}\tilde{\zeta})-p\big|+|g\_{2,1}(\tilde{z})|N^{\gamma}\bar{\varPhi}^{\prime}\_{N}(N^{\gamma}\tilde{\zeta}). |  |

From Step 1, we know |z~vN|≤K0|\tilde{z}^{N}\_{v}|\leq K\_{0} and ζ~N:=z~1N−z~0N≤2​K0\tilde{\zeta}^{N}:=\tilde{z}^{N}\_{1}-\tilde{z}^{N}\_{0}\leq 2K\_{0}, so from now on we shall restrict to −K0≤z~<0-K\_{0}\leq\tilde{z}<0 and 0<ζ~≤2​K00<\tilde{\zeta}\leq 2K\_{0}. In particular, this implies that |g1,1​(z~)|,|g2,1​(z~)|≤K|g\_{1,1}(\tilde{z})|,|g\_{2,1}(\tilde{z})|\leq K; here, we use K>0K>0 to denote a generic constant that depends only on the model parameters, and its value may vary from line to line.

Since x/(1+x)2≤1/4{x/(1+x)^{2}}\leq{1/4}, by ([B](https://arxiv.org/html/2512.06309v1#A2.Ex4 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) we have for ζ~∈(0,2​K0]\tilde{\zeta}\in(0,2K\_{0}],

|  |  |  |
| --- | --- | --- |
|  | Nγ​Φ¯N′​(Nγ​ζ~)=N2​γ​ζ~N​σ2​𝔼​[q​eη¯N​(ζ)(1+q​eη¯N​(ζ))2]≤N2​γ​ζ~4​N​σ2≤K​N2​γ−1.\displaystyle N^{\gamma}\bar{\varPhi}^{\prime}\_{N}(N^{\gamma}\tilde{\zeta})=\frac{N^{2\gamma}\tilde{\zeta}}{N\sigma^{2}}\mathbb{E}\bigg[\frac{qe^{\bar{\eta}\_{N}(\zeta)}}{\big(1+qe^{\bar{\eta}\_{N}(\zeta)}\big)^{2}}\bigg]\leq\frac{N^{2\gamma}\tilde{\zeta}}{4N\sigma^{2}}\leq KN^{2\gamma-1}. |  |

Moreover, one can easily verify that Φ¯N​(Nγ​ζ~)=Φ¯1​(Nγ−1/2​ζ~)\bar{\varPhi}\_{N}(N^{\gamma}\tilde{\zeta})=\bar{\varPhi}\_{1}\big(N^{\gamma-1/2}\tilde{\zeta}\big), Φ¯1​(0)=p\bar{\varPhi}\_{1}(0)=p, as well as Φ¯1′​(0)=−𝔼​[eη¯1​(ζ)​q​(ζ−W)/σ2/(1+q​eη¯1​(ζ))2]|ζ=0=0\bar{\varPhi}^{\prime}\_{1}(0)=-\mathbb{E}\big[{e^{\bar{\eta}\_{1}(\zeta)}q(\zeta-W)/\penalty 50\sigma^{2}\big/(1+qe^{\bar{\eta}\_{1}(\zeta)})^{2}}\big]\big|\_{\zeta=0}=0. Then, again, for ζ~∈(0,2​K0]\tilde{\zeta}\in(0,2K\_{0}], and hence Nγ−1/2​ζ~∈(0,2​K0]N^{\gamma-1/2}\tilde{\zeta}\in(0,2K\_{0}], we have

|  |  |  |
| --- | --- | --- |
|  | |Φ¯N​(Nγ​ζ~)−p|=|Φ¯1​(Nγ−12​ζ~)−Φ¯1​(0)|≤K​|Nγ−12​ζ~|2≤K​N2​γ−1.\big|\bar{\varPhi}\_{N}(N^{\gamma}\tilde{\zeta})-p\big|=\big|\bar{\varPhi}\_{1}\big(N^{\gamma-\frac{1}{2}}\tilde{\zeta}\big)-\bar{\varPhi}\_{1}(0)\big|\leq K\big|N^{\gamma-\frac{1}{2}}\tilde{\zeta}\big|^{2}\leq KN^{2\gamma-1}. |  |

Putting things together, we have shown that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supζ~∈(0,2​K0],z~∈[−K0,0)|F0N​(Nγ​ζ~;Nγ​z~)−J˘∞γ​(z~,0)|≤K​N2​γ−1.\sup\_{\tilde{\zeta}\in(0,2K\_{0}],~\tilde{z}\in[-K\_{0},0)}\big|F^{N}\_{0}(N^{\gamma}\tilde{\zeta};N^{\gamma}\tilde{z})-\breve{J}^{\gamma}\_{\infty}(\tilde{z},0)\big|\leq KN^{2\gamma-1}. |  | (B.26) |

It is similar to establish that supζ~∈(0,2​K0],z~∈(0,K0]|F1N​(Nγ​ζ~;Nγ​z~)−J˘∞γ​(z~,1)|≤K​N2​γ−1\sup\_{\tilde{\zeta}\in(0,2K\_{0}],~\tilde{z}\in(0,K\_{0}]}\big|F^{N}\_{1}(N^{\gamma}\tilde{\zeta};N^{\gamma}\tilde{z})-\breve{J}^{\gamma}\_{\infty}(\tilde{z},1)\big|\leq KN^{2\gamma-1}.

Step 3 We now prove ([4.3](https://arxiv.org/html/2512.06309v1#S4.E3 "In Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")).
Since F0N​(Nγ​ζ~N;Nγ​z~0N)=J˘∞γ​(Z~γ∗​(0),0)=0F^{N}\_{0}(N^{\gamma}\tilde{\zeta}^{N};N^{\gamma}\tilde{z}^{N}\_{0})=\breve{J}^{\gamma}\_{\infty}(\tilde{Z}^{\ast}\_{\gamma}(0),0)=0, ([B.26](https://arxiv.org/html/2512.06309v1#A2.E26 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | |J˘∞γ​(z~0N,0)−J˘∞γ​(Z~γ∗​(0),0)|=|J˘∞γ​(z~0N,0)−F0N​(Nγ​ζ~N;Nγ​z~0N)|≤K​N2​γ−1.\big|\breve{J}^{\gamma}\_{\infty}(\tilde{z}^{N}\_{0},0)-\breve{J}^{\gamma}\_{\infty}(\tilde{Z}^{\ast}\_{\gamma}(0),0)\big|=\big|\breve{J}^{\gamma}\_{\infty}(\tilde{z}^{N}\_{0},0)-F^{N}\_{0}(N^{\gamma}\tilde{\zeta}^{N};N^{\gamma}\tilde{z}^{N}\_{0})\big|\leq KN^{2\gamma-1}. |  | (B.27) |

Note that by ([B](https://arxiv.org/html/2512.06309v1#A2.Ex14 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")),

|  |  |  |
| --- | --- | --- |
|  | ∂z~J˘∞γ​(z~,0)=p​(χ​λ′​(z~)+χ​z~​λ′′​(z~)+χ0​eλ​(z~)​λ′​(z~))≤p​χ​λ′​(z~)<0,z~<0.\partial\_{\tilde{z}}\breve{J}^{\gamma}\_{\infty}(\tilde{z},0)=p\Big(\chi\lambda^{\prime}(\tilde{z})+\chi\tilde{z}\lambda^{\prime\prime}(\tilde{z})+\chi\_{0}e^{\lambda(\tilde{z})}\lambda^{\prime}(\tilde{z})\Big)\leq p\chi\lambda^{\prime}(\tilde{z})<0,\quad\tilde{z}<0. |  |

As λ′\lambda^{\prime} is increasing (by Assumption [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), ∂z~J˘∞γ​(z~,0)≤p​χ​λ′​(Z~γ∗​(0)/2)<0\partial\_{\tilde{z}}\breve{J}^{\gamma}\_{\infty}(\tilde{z},0)\leq p\chi\lambda^{\prime}(\tilde{Z}^{\ast}\_{\gamma}(0)/2)<0 for all z~≤Z~γ∗​(0)/2\tilde{z}\leq\tilde{Z}^{\ast}\_{\gamma}(0)/2. Then, denoting c0:=p​χ​|λ′​(Z~γ∗​(0)/2)|c\_{0}:=p\chi|\lambda^{\prime}(\tilde{Z}^{\ast}\_{\gamma}(0)/2)|, by the monotonicity of J˘∞γ​(z~,0)\breve{J}^{\gamma}\_{\infty}(\tilde{z},0),

|  |  |  |
| --- | --- | --- |
|  | |J˘∞γ​(z~,0)−J˘∞γ​(Z~γ∗​(0),0)|≥12​c0​|Z~γ∗​(0)|>0,z~∈[12​Z~γ∗​(0),0).\big|\breve{J}^{\gamma}\_{\infty}(\tilde{z},0)-\breve{J}^{\gamma}\_{\infty}(\tilde{Z}^{\ast}\_{\gamma}(0),0)\big|\geq\tfrac{1}{2}c\_{0}|\tilde{Z}^{\ast}\_{\gamma}(0)|>0,\quad\tilde{z}\in\big[\tfrac{1}{2}\tilde{Z}^{\ast}\_{\gamma}(0),0\big). |  |

By ([B.27](https://arxiv.org/html/2512.06309v1#A2.E27 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), this further implies that for NN large such that K​N2​γ−1<c0​|Z~γ∗​(0)|/2KN^{2\gamma-1}<c\_{0}|\tilde{Z}^{\ast}\_{\gamma}(0)|/\penalty 502, we must have z~0N≤Z~γ∗​(0)/2\tilde{z}^{N}\_{0}\leq\tilde{Z}^{\ast}\_{\gamma}(0)/2. Thus, with c0≤|∂z~J˘∞γ​(z~,0)|c\_{0}\leq|\partial\_{\tilde{z}}\breve{J}^{\gamma}\_{\infty}(\tilde{z},0)| for all z~≤Z~γ∗​(0)/2\tilde{z}\leq\tilde{Z}^{\ast}\_{\gamma}(0)/2,

|  |  |  |
| --- | --- | --- |
|  | K​N2​γ−1≥|J˘∞γ​(z~0N,0)−J˘∞γ​(Z~γ∗​(0),0)|≥c0​|z~0N−Z~γ∗​(0)|,KN^{2\gamma-1}\geq\big|\breve{J}^{\gamma}\_{\infty}(\tilde{z}^{N}\_{0},0)-\breve{J}^{\gamma}\_{\infty}(\tilde{Z}^{\ast}\_{\gamma}(0),0)\big|\geq c\_{0}|\tilde{z}^{N}\_{0}-\tilde{Z}^{\ast}\_{\gamma}(0)|, |  |

which immediately implies that

|  |  |  |
| --- | --- | --- |
|  | |z~0N−Z~γ∗​(0)|≤Kc0​N2​γ−1≤K​N2​γ−1.|\tilde{z}^{N}\_{0}-\tilde{Z}^{\ast}\_{\gamma}(0)|\leq\tfrac{K}{c\_{0}}N^{2\gamma-1}\leq KN^{2\gamma-1}. |  |

It is similar to show that |z~1N−Z~γ∗​(1)|≤K​N2​γ−1|\tilde{z}^{N}\_{1}-\tilde{Z}^{\ast}\_{\gamma}(1)|\leq KN^{2\gamma-1}, justifying ([4.3](https://arxiv.org/html/2512.06309v1#S4.E3 "In Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")).

For ([4.1](https://arxiv.org/html/2512.06309v1#S4.Ex2 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), note that

|  |  |  |
| --- | --- | --- |
|  | PN∗​(y)=PN​(ZN∗;y)=P~Nγ​(N−γ​ZN∗;N−max⁡{γ,12}​y)=11+q​eκ~N​(y~),P^{\*}\_{N}(y)=P\_{N}(Z^{\*}\_{N};y)=\tilde{P}^{\gamma}\_{N}(N^{-\gamma}Z^{\*}\_{N};N^{-\max\{\gamma,\frac{1}{2}\}}y)=\frac{1}{1+qe^{\tilde{\kappa}\_{N}(\tilde{y})}}, |  |

where κ~N\tilde{\kappa}\_{N} is as in ([A](https://arxiv.org/html/2512.06309v1#A1.Ex1 "Appendix A Proof of Proposition 3.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) corresponding to Z~=N−γ​ZN∗\tilde{Z}=N^{-\gamma}Z^{\*}\_{N} and y~=N−1/2​y\tilde{y}=N^{-1/2}y. By Step 1, |Z~|≤K0|\tilde{Z}|\leq K\_{0}. Since γ<1/2\gamma<1/2, then it follows from ([A.2](https://arxiv.org/html/2512.06309v1#A1.E2 "In Appendix A Proof of Proposition 3.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) that

|  |  |  |
| --- | --- | --- |
|  | |κ~N​(y~)|≤K​(|y~|​Nγ−12+N2​γ−1)=K​(|y|​Nγ−1+N2​γ−1).|\tilde{\kappa}\_{N}(\tilde{y})|\leq K\big(|\tilde{y}|N^{\gamma-\frac{1}{2}}+N^{2\gamma-1}\big)=K\big(|y|N^{\gamma-1}+N^{2\gamma-1}\big). |  |

Therefore, recalling q=(1−p)/pq=(1-p)/p, we have

|  |  |  |
| --- | --- | --- |
|  | |PN∗​(y)−p|=|11+q​eκ~N​(y~)−p|=(1−p)​|1−eκ~N​(y~)|1+q​eκ~N​(y~)≤K​(|y|​Nγ−1+N2​γ−1),|P^{\*}\_{N}(y)-p|=\bigg|\frac{1}{1+qe^{\tilde{\kappa}\_{N}(\tilde{y})}}-p\bigg|=(1-p)\frac{|1-e^{\tilde{\kappa}\_{N}(\tilde{y})}|}{1+qe^{\tilde{\kappa}\_{N}(\tilde{y})}}\leq K\big(|y|N^{\gamma-1}+N^{2\gamma-1}\big), |  |

proving the first estimate in ([4.1](https://arxiv.org/html/2512.06309v1#S4.Ex2 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). Finally, the last bound, along with the boundedness of N−γ​ZN∗​(v)N^{-\gamma}Z^{\*}\_{N}(v) established in Step 1, immediately leads to the second estimate in ([4.1](https://arxiv.org/html/2512.06309v1#S4.Ex2 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), completing the proof.
∎

## Appendix C Proof of Theorem [4.2](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")

We have γ=β<1/2\gamma=\beta<1/2. First, ([4](https://arxiv.org/html/2512.06309v1#S4.Ex1 "4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([B.18](https://arxiv.org/html/2512.06309v1#A2.E18 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) together imply that, for v∈{0,1}v\in\{0,1\} and z∈ℝvz\in\mathbb{R}\_{v},

|  |  |  |
| --- | --- | --- |
|  | N−γ​JN​(p;z,v)=(v−p)​N−γ​z​(χ​e−λ​(N−γ​z)−χ0)=J~∞γ​(p;N−γ​z,v).N^{-\gamma}J\_{N}(p;z,v)=(v-p)N^{-\gamma}z\big(\chi e^{-\lambda(N^{-\gamma}z)}-\chi\_{0}\big)=\tilde{J}^{\gamma}\_{\infty}(p;N^{-\gamma}z,v). |  |

Then, based on Definition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), since

|  |  |  |
| --- | --- | --- |
|  | N−γ​JN​(p;Nγ​Z~γ∗​(v),v)=J~∞γ​(p;Z~γ∗​(v),v)=supz∈ℝvJ~∞γ​(p;N−γ​z,v)=supz∈ℝvN−γ​JN​(p;z,v),N^{-\gamma}J\_{N}(p;N^{\gamma}\tilde{Z}^{\*}\_{\gamma}(v),v)=\tilde{J}^{\gamma}\_{\infty}(p;\tilde{Z}^{\*}\_{\gamma}(v),v)=\sup\_{z\in\mathbb{R}\_{v}}\tilde{J}^{\gamma}\_{\infty}(p;N^{-\gamma}z,v)=\sup\_{z\in\mathbb{R}\_{v}}N^{-\gamma}J\_{N}(p;z,v), |  |

we have that ([4.6](https://arxiv.org/html/2512.06309v1#S4.E6 "In Definition 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) in Definition [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmdefinition1 "Definition 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") holds with ϵ=0\epsilon=0.

Next, since max⁡{γ,1/2}=1/2\max\{\gamma,1/2\}=1/2, by ([A](https://arxiv.org/html/2512.06309v1#A1.Ex1 "Appendix A Proof of Proposition 3.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) we have PN​(Nγ​Z~γ∗;N1/2​y~)=1/(1+q​eκ~N​(y~))P\_{N}(N^{\gamma}\tilde{Z}^{\*}\_{\gamma};N^{1/2}\tilde{y})=1/(1+qe^{\tilde{\kappa}\_{N}(\tilde{y})}), where κ~N\tilde{\kappa}\_{N} corresponds to Z~=Z~γ∗\tilde{Z}=\tilde{Z}^{\*}\_{\gamma}. As Z~γ∗\tilde{Z}^{\*}\_{\gamma} is independent of NN, it follows from the exact same arguments for ([4.3](https://arxiv.org/html/2512.06309v1#S4.E3 "In Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) that

|  |  |  |
| --- | --- | --- |
|  | |PN​(Nγ​Z~γ∗;N12​y~)−p|≤K​(|N12​y~|​Nγ−1+N2​γ−1)≤K​Nγ−12​(|y~|+1),\big|P\_{N}(N^{\gamma}\tilde{Z}^{\*}\_{\gamma};N^{\frac{1}{2}}\tilde{y})-p\big|\leq K\big(|N^{\frac{1}{2}}\tilde{y}|N^{\gamma-1}+N^{2\gamma-1}\big)\leq KN^{\gamma-\frac{1}{2}}(|\tilde{y}|+1), |  |

which verifies ([4.7](https://arxiv.org/html/2512.06309v1#S4.E7 "In Definition 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) with ϵ≡ϵN=K​Nγ−1/2\epsilon\equiv\epsilon\_{N}=KN^{\gamma-{1/2}}, hence ([4.8](https://arxiv.org/html/2512.06309v1#S4.E8 "In Theorem 4.2. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). The proof is complete.
∎

## Supplemental Appendix A Proofs in further discussions

This supplemental appendix presents formal statements and their detailed proofs in the further discussions on the general scenario involving criminal penalties in Section [6](https://arxiv.org/html/2512.06309v1#S6 "6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"). The proofs are structurally similar to that of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") and Theorem [4.2](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") as presented in Appendix [B](https://arxiv.org/html/2512.06309v1#A2 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") and Appendix [C](https://arxiv.org/html/2512.06309v1#A3 "Appendix C Proof of Theorem 4.2 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), but with notable technical differences.

###### Theorem SA.1.

Consider the setting of ([6.1](https://arxiv.org/html/2512.06309v1#S6.E1 "In 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), and let Assumption [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") hold. We have the following four assertions.

(i) For every N≥1N\geq 1, there exists an equilibrium (ZN∗,PN∗)(Z^{\ast}\_{N},P^{\ast}\_{N}) in the sense of Definition [2.1](https://arxiv.org/html/2512.06309v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading").
  
(ii) There exists a γ\gamma-limiting equilibrium (Z~γ∗,P~γ∗)(\tilde{Z}^{\ast}\_{\gamma},\tilde{P}^{\ast}\_{\gamma}) in the sense of Definition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") if and only if ([6.5](https://arxiv.org/html/2512.06309v1#S6.E5 "In 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) holds. Moreover, when γ<1/2\gamma<1/2, the γ\gamma-limiting equilibrium (Z~γ∗,P~γ∗)(\tilde{Z}^{\ast}\_{\gamma},\tilde{P}^{\ast}\_{\gamma}) is unique with P~γ∗=p\tilde{P}^{\ast}\_{\gamma}=p.
  
(iii) Let γ<1/2\gamma<1/2 and (Z~γ∗,P~γ∗≡p)(\tilde{Z}^{\ast}\_{\gamma},\tilde{P}^{\ast}\_{\gamma}\equiv p) be the unique γ\gamma-limiting equilibrium from assertion (ii). Then, there exists a constant K>0K>0, depending only on the model parameters but not on NN, such that, for any equilibrium (ZN∗,PN∗)(Z^{\ast}\_{N},P^{\ast}\_{N}) from assertion (i),

|  |  |  |  |
| --- | --- | --- | --- |
|  | |N−γ​ZN∗​(v)−Z~γ∗​(v)|≤{K​N2​γ−1,if ​β=0​or​α=1,K​Nmax⁡{2​γ−1,−γ​(α−1)​θ′,−γ​α′},if ​β>0​and​α>1,​v∈{0,1},|N^{-\gamma}Z^{\ast}\_{N}(v)-\tilde{Z}^{\ast}\_{\gamma}(v)|\leq\begin{cases}KN^{2\gamma-1},&\!\!\!\text{if }\beta=0~\mbox{or}~\alpha=1,\\ KN^{\max\{2\gamma-1,-\gamma(\alpha-1)\theta^{\prime},-\gamma\alpha^{\prime}\}},&\!\!\!\text{if }\beta>0~\mbox{and}~\alpha>1,\end{cases}~v\in\{0,1\}, |  | (SA.1) |

and, with P~γ∗=p\tilde{P}^{\ast}\_{\gamma}=p, the estimates in ([4.1](https://arxiv.org/html/2512.06309v1#S4.Ex2 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) stand.
  
(iv) As in assertion (iii), let γ<1/2\gamma<1/2 and let (Z~γ∗,p)(\tilde{Z}^{\ast}\_{\gamma},p) be the unique γ\gamma-limiting equilibrium. For every N≥1N\geq 1, (Nγ​Z~γ∗,p)(N^{\gamma}\tilde{Z}^{\ast}\_{\gamma},p) is an ϵN\epsilon\_{N}-equilibrium in the sense of Definition [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmdefinition1 "Definition 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), where, for a constant KK depending only on the model parameters,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵN={K​Nγ−12,if ​β=0​or​α=1,K​Nmax⁡{γ−12,−γ​(α−1),−γ​(α−1)​θ′,−γ​α′},if ​β>0​and​α>1.\epsilon\_{N}=\begin{cases}KN^{\gamma-\frac{1}{2}},&\;\text{if }\beta=0~\mbox{or}~\alpha=1,\\ KN^{\max\{\gamma-\frac{1}{2},-\gamma(\alpha-1),-\gamma(\alpha-1)\theta^{\prime},-\gamma\alpha^{\prime}\}},&\;\text{if }\beta>0~\mbox{and}~\alpha>1.\end{cases} |  | (SA.2) |

Before proving Theorem [SA.1](https://arxiv.org/html/2512.06309v1#A1.Thmtheorem1 "Theorem SA.1. ‣ Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), we make a few additional comments on the convergence implications. Compared with Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), assertion (iii) in Theorem [SA.1](https://arxiv.org/html/2512.06309v1#A1.Thmtheorem1 "Theorem SA.1. ‣ Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") indicates the joint dependence of the convergence rate for the optimal strategies on both the intensity of investigation (β\beta) and the severity of criminal penalties (α\alpha), signaling a tradeoff between small and large values of γ\gamma. Within the maximum brackets in ([SA.1](https://arxiv.org/html/2512.06309v1#A1.E1a "In Theorem SA.1. ‣ Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), the first component (2​γ−12\gamma-1) stems from the convergence of the price function, whereas the second and third components (−γ​(α−1)​θ′-\gamma(\alpha-1)\theta^{\prime} or −γ​α′-\gamma\alpha^{\prime}) is a result of the large argument behavior for C0C\_{0} (as stated in Assumption [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). Intuitively, when investigations are sensitive to the population size (β>0\beta>0), the imposition of criminal penalties upon prosecution can substantially alter the convergence rate depending on their specific form. In this case, the jump in the convergence rate as α↘1\alpha\searrow 1 in ([SA.1](https://arxiv.org/html/2512.06309v1#A1.E1a "In Theorem SA.1. ‣ Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) results from the at-most-linear growth of the insider’s expected profit with his trade size (see ([6.2](https://arxiv.org/html/2512.06309v1#S6.E2 "In 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"))), which can be coalesced into the penalty component if and only if α=1\alpha=1. Further details can be found in the proof of Theorem [SA.1](https://arxiv.org/html/2512.06309v1#A1.Thmtheorem1 "Theorem SA.1. ‣ Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading").

To prepare for the proof of Theorem [SA.1](https://arxiv.org/html/2512.06309v1#A1.Thmtheorem1 "Theorem SA.1. ‣ Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), we establish a technical lemma.

###### Lemma SA.1.

Consider the setting of Lemma [B.1](https://arxiv.org/html/2512.06309v1#A2.Thmlemma1 "Lemma B.1. ‣ Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), and define

|  |  |  |  |
| --- | --- | --- | --- |
|  | RN​(Z;z,v):=eλN​(z)​∂z((χ​e−λN​(z)−χ0)​QN​(Z;z,v)),z∈ℝv,v∈{0,1}.R\_{N}(Z;z,v):=e^{\lambda\_{N}(z)}\partial\_{z}\big((\chi e^{-\lambda\_{N}(z)}-\chi\_{0})Q\_{N}(Z;z,v)\big),\quad z\in\mathbb{R}\_{v},\;v\in\{0,1\}. |  | (SA.3) |

Then, the following two assertions hold.

(i) RN​(Z;z,0)R\_{N}(Z;z,0), z<0z<0, admits a unique zero z˘0<0\breve{z}\_{0}<0. Also, RN​(Z;z,0)>0R\_{N}(Z;z,0)>0 for z<z˘0z<\breve{z}\_{0}, and RN​(Z;z,0)R\_{N}(Z;z,0) is negative and strictly decreasing for z∈(z˘0,0)z\in(\breve{z}\_{0},0).
  
(ii) RN​(Z;z,1)R\_{N}(Z;z,1), z>0z>0, admits a unique zero z˘1>0\breve{z}\_{1}>0. Also, RN​(Z;z,1)<0R\_{N}(Z;z,1)<0 for z>z˘1z>\breve{z}\_{1}, and RN​(Z;z,1)R\_{N}(Z;z,1) is positive and strictly decreasing for z∈(0,z˘1)z\in(0,\breve{z}\_{1}).

Proof. We only consider the case v=0v=0, with z<0z<0; the case v=1v=1 (with z>0z>0) can be proved in the same way. As before, without loss of generality, we assume in the proof that λ​(z)\lambda(z) is twice-differentiable for z≠0z\neq 0, and for notational simplicity we suppress the symbol ZZ in all the functions.

By Step 1 in the proof of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") assertion (i), the function (χ​e−λN​(z)−χ0)​QN​(z,0)(\chi e^{-\lambda\_{N}(z)}-\chi\_{0})Q\_{N}(z,0), z<0z<0, admits a unique maximum point z˘0<0\breve{z}\_{0}<0, and it satisfies RN​(z˘0,0)=0R\_{N}(\breve{z}\_{0},0)=0, RN​(z,0)>0R\_{N}(z,0)>0 for z<z˘0z<\breve{z}\_{0}, and RN​(z,0)<0R\_{N}(z,0)<0 for z∈(z˘0,0)z\in(\breve{z}\_{0},0). Moreover, since QN>0Q\_{N}>0, it is clear that χ​e−λN​(z˘0)−χ0>0\chi e^{-\lambda\_{N}(\breve{z}\_{0})}-\chi\_{0}>0, and then by the monotonicity of λN\lambda\_{N}, we see that χ​e−λN​(z)−χ0>0\chi e^{-\lambda\_{N}(z)}-\chi\_{0}>0 for all z∈(z˘0,0)z\in(\breve{z}\_{0},0).

It remains to show that RN​(z,0)R\_{N}(z,0) is strictly decreasing in (z˘0,0)(\breve{z}\_{0},0). Let us write

|  |  |  |  |
| --- | --- | --- | --- |
|  | HN​(z):=(χ−χ0​eλN​(z))​ΦN​(z)>0,z∈(z˘0,0).H\_{N}(z):=(\chi-\chi\_{0}e^{\lambda\_{N}(z)})\varPhi\_{N}(z)>0,\quad z\in(\breve{z}\_{0},0). |  | (SA.4) |

Then, (χ​e−λN​(z)−χ0)​QN​(z,0)=(−z)​e−λN​(z)​HN​(z)(\chi e^{-\lambda\_{N}(z)}-\chi\_{0})Q\_{N}(z,0)=(-z)e^{-\lambda\_{N}(z)}H\_{N}(z), and thus, for z∈(z˘0,0)z\in(\breve{z}\_{0},0),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | RN​(z,0)\displaystyle R\_{N}(z,0) | =(z​λN′​(z)−1)​HN​(z)−z​HN′​(z)<0;\displaystyle=(z\lambda\_{N}^{\prime}(z)-1)H\_{N}(z)-zH^{\prime}\_{N}(z)<0; |  | (SA.5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂zRN​(z,0)\displaystyle{\partial\_{z}}R\_{N}(z,0) | =(λN′​(z)+z​λN′′​(z))​HN​(z)+(z​λN′​(z)−2)​HN′​(z)−z​HN′′​(z).\displaystyle=(\lambda^{\prime}\_{N}(z)+z\lambda^{\prime\prime}\_{N}(z))H\_{N}(z)+(z\lambda^{\prime}\_{N}(z)-2)H^{\prime}\_{N}(z)-zH^{\prime\prime}\_{N}(z). |  | (SA.6) |

Recall that χ−χ0​eλN​(z)>0\chi-\chi\_{0}e^{\lambda\_{N}(z)}>0 for z∈(z˘0,0)z\in(\breve{z}\_{0},0), and similar to ([B.5](https://arxiv.org/html/2512.06309v1#A2.E5 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we have

|  |  |  |
| --- | --- | --- |
|  | d2d​z2​log⁡(χ−χ0​eλN​(z))=−χ0​eλN​(z)​((λN′​(z))2+λN′′​(z))χ−χ0​eλN​(z)−(χ0​λN′​(z)​eλN​(z))2(χ−χ0​eλN​(z))2≤0,\frac{{\rm d}^{2}}{{\rm d}z^{2}}\log\big(\chi-\chi\_{0}e^{\lambda\_{N}(z)}\big)=-\frac{\chi\_{0}e^{\lambda\_{N}(z)}((\lambda^{\prime}\_{N}(z))^{2}+\lambda\_{N}^{\prime\prime}(z))}{\chi-\chi\_{0}e^{\lambda\_{N}(z)}}-\frac{(\chi\_{0}\lambda\_{N}^{\prime}(z)e^{\lambda\_{N}(z)})^{2}}{(\chi-\chi\_{0}e^{\lambda\_{N}(z)})^{2}}\leq 0, |  |

implying that χ−χ0​eλN​(z)\chi-\chi\_{0}e^{\lambda\_{N}(z)} is log-concave. From the proof of Lemma [B.1](https://arxiv.org/html/2512.06309v1#A2.Thmlemma1 "Lemma B.1. ‣ Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), we know that ΦN\varPhi\_{N} is also log-concave, and so HNH\_{N} is log-concave in (z˘0,0)(\breve{z}\_{0},0). This implies that HN​(z)​HN′′​(z)−(HN′​(z))2≤0H\_{N}(z)H^{\prime\prime}\_{N}(z)-(H^{\prime}\_{N}(z))^{2}\leq 0.
Hence, from ([SA.6](https://arxiv.org/html/2512.06309v1#A1.E6 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂zRN​(z,0)\displaystyle{\partial\_{z}}R\_{N}(z,0) | ≤(λN′​(z)+z​λN′′​(z))​HN​(z)+(z​λN′​(z)−2)​HN′​(z)−z​(HN′​(z))2HN​(z)\displaystyle\leq(\lambda^{\prime}\_{N}(z)+z\lambda^{\prime\prime}\_{N}(z))H\_{N}(z)+(z\lambda^{\prime}\_{N}(z)-2)H^{\prime}\_{N}(z)-z\frac{(H^{\prime}\_{N}(z))^{2}}{H\_{N}(z)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(λN′​(z)+z​λN′′​(z))​HN​(z)+HN′​(z)HN​(z)​((z​λN′​(z)−2)​HN​(z)−z​HN′​(z))\displaystyle=(\lambda^{\prime}\_{N}(z)+z\lambda^{\prime\prime}\_{N}(z))H\_{N}(z)+\frac{H^{\prime}\_{N}(z)}{H\_{N}(z)}\big((z\lambda^{\prime}\_{N}(z)-2)H\_{N}(z)-zH\_{N}^{\prime}(z)\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(λN′​(z)+z​λN′′​(z))​HN​(z)+HN′​(z)HN​(z)​(RN​(z,0)−HN​(z)),\displaystyle=(\lambda^{\prime}\_{N}(z)+z\lambda^{\prime\prime}\_{N}(z))H\_{N}(z)+\frac{H^{\prime}\_{N}(z)}{H\_{N}(z)}\big(R\_{N}(z,0)-H\_{N}(z)\big), |  |

where the last line is due to ([SA.5](https://arxiv.org/html/2512.06309v1#A1.E5 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). Note further that for z∈(z˘0,0)z\in(\breve{z}\_{0},0),

|  |  |  |
| --- | --- | --- |
|  | HN′​(z):=−χ0​eλN​(z)​λN′​(z)​ΦN​(z)+(χ−χ0​eλN​(z))​ΦN′​(z)>0,H^{\prime}\_{N}(z):=-\chi\_{0}e^{\lambda\_{N}(z)}\lambda^{\prime}\_{N}(z)\varPhi\_{N}(z)+(\chi-\chi\_{0}e^{\lambda\_{N}(z)})\varPhi\_{N}^{\prime}(z)>0, |  |

and thus, by ([SA.5](https://arxiv.org/html/2512.06309v1#A1.E5 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) again and Assumption [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), ∂zRN​(z,0)<0{\partial\_{z}}R\_{N}(z,0)<0 for z∈(z˘0,0)z\in(\breve{z}\_{0},0).
∎

Proof of Theorem [SA.1](https://arxiv.org/html/2512.06309v1#A1.Thmtheorem1 "Theorem SA.1. ‣ Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") assertion (i). Consider the equilibrium in Definition [2.1](https://arxiv.org/html/2512.06309v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") for fixed N≥1N\geq 1. Similar to the proof of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") assertion (i), we proceed in two steps.

Step 1 In this step we show that, given Z=(Z​(0),Z​(1))∈ℝ0×ℝ1Z=(Z(0),Z(1))\in\mathbb{R}\_{0}\times\mathbb{R}\_{1}, the insider’s objective function J´N​(Z;z,v)\acute{J}\_{N}(Z;z,v) from ([2.3.8](https://arxiv.org/html/2512.06309v1#S2.E8 "In 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) has a unique maximum point zv∗∈ℝvz^{\*}\_{v}\in\mathbb{R}\_{v}. Without loss of generality, assume as before that λ\lambda and C0C\_{0} are twice-differentiable for z≠0z\neq 0, and again we shall only consider the case v=0v=0.

First, by ([6.1](https://arxiv.org/html/2512.06309v1#S6.E1 "In 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([B.4](https://arxiv.org/html/2512.06309v1#A2.E4 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) we have that, for z<0z<0,

|  |  |  |
| --- | --- | --- |
|  | J´N​(Z;z,0)=(χ​e−λN​(z)−χ0)​QN​(Z;z,v)−(1−e−λN​(z))​C0​(z).\acute{J}\_{N}(Z;z,0)=(\chi e^{-\lambda\_{N}(z)}-\chi\_{0})Q\_{N}(Z;z,v)-(1-e^{-\lambda\_{N}(z)})C\_{0}(z). |  |

Then, recalling ([SA.3](https://arxiv.org/html/2512.06309v1#A1.E3 "In Lemma SA.1. ‣ Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | J˘N​(Z;z,0):=eλN​(z)​∂zJ´N​(Z;z,0)=RN​(Z;z,0)+AN​(z),\displaystyle\breve{J}\_{N}(Z;z,0):=e^{\lambda\_{N}(z)}\partial\_{z}\acute{J}\_{N}(Z;z,0)=R\_{N}(Z;z,0)+A\_{N}(z), |  | (SA.7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | whereAN​(z):=−λN′​(z)​C0​(z)−(eλN​(z)−1)​C0′​(z).\displaystyle\mbox{where}\quad A\_{N}(z):=-\lambda^{\prime}\_{N}(z)C\_{0}(z)-(e^{\lambda\_{N}(z)}-1)C^{\prime}\_{0}(z). |  | (SA.8) |

By Assumption [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), it is clear that AN​(z)≥0A\_{N}(z)\geq 0 for z<0z<0, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | AN′​(z)=−λN′′​(z)​C0​(z)−(eλN​(z)+1)​λN′​(z)​C0′​(z)−(eλN​(z)−1)​C0′′​(z)≤0.A\_{N}^{\prime}(z)=-\lambda^{\prime\prime}\_{N}(z)C\_{0}(z)-(e^{\lambda\_{N}(z)}+1)\lambda^{\prime}\_{N}(z)C^{\prime}\_{0}(z)-(e^{\lambda\_{N}(z)}-1)C^{\prime\prime}\_{0}(z)\leq 0. |  | (SA.9) |

Let z˘0\breve{z}\_{0} be as in Lemma [SA.1](https://arxiv.org/html/2512.06309v1#A1.Thmlemma1 "Lemma SA.1. ‣ Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"). Then, it follows from ([SA.7](https://arxiv.org/html/2512.06309v1#A1.E7 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | J˘N​(Z;z,0)>0,z≤z˘0and∂zJ˘N​(Z;z,0)<0,z∈(z˘0,0).\breve{J}\_{N}(Z;z,0)>0,~z\leq\breve{z}\_{0}\quad\text{and}\quad\partial\_{z}\breve{J}\_{N}(Z;z,0)<0,~z\in(\breve{z}\_{0},0). |  | (SA.10) |

Note further that, by ([SA.5](https://arxiv.org/html/2512.06309v1#A1.E5 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([SA.4](https://arxiv.org/html/2512.06309v1#A1.E4 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | limz↗0J˘N​(Z;z,0)=limz↗0RN​(Z;z,0)=−ΦN​(Z;0)<0,\lim\_{z\nearrow 0}\breve{J}\_{N}(Z;z,0)=\lim\_{z\nearrow 0}R\_{N}(Z;z,0)=-\varPhi\_{N}(Z;0)<0, |  | (SA.11) |

which means that J˘N​(Z;⋅,0)\breve{J}\_{N}(Z;\cdot,0) has a unique zero z0∗∈(z˘0,0)z^{\*}\_{0}\in(\breve{z}\_{0},0), and by ([SA.10](https://arxiv.org/html/2512.06309v1#A1.E10 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), J˘N​(Z;z,0)>0\breve{J}\_{N}(Z;z,0)>0 for z<z0∗z<z^{\*}\_{0} and J˘N​(Z;z,0)<0\breve{J}\_{N}(Z;z,0)<0 for z∈(z0∗,0)z\in(z^{\*}\_{0},0). By continuity, this implies that z0∗z^{\*}\_{0} is the unique maximum point of J´N​(Z;⋅,0)\acute{J}\_{N}(Z;\cdot,0) on ℝ0=(−∞,0)\mathbb{R}\_{0}=(-\infty,0).

Step 2 This step is concerned with the existence of a finite-NN equilibrium (Definition [2.1](https://arxiv.org/html/2512.06309v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). As established in Step 1, ZN∗=(ZN∗​(0),ZN∗​(1))∈ℝ0×ℝ1Z^{\ast}\_{N}=(Z^{\ast}\_{N}(0),Z^{\ast}\_{N}(1))\in\mathbb{R}\_{0}\times\mathbb{R}\_{1} is an equilibrium strategy, i.e., (ZN∗,PN​(ZN∗;⋅))(Z^{\*}\_{N},P\_{N}(Z^{\*}\_{N};\cdot)) is an equilibrium, if and only if it satisfies the equilibrium conditions

|  |  |  |  |
| --- | --- | --- | --- |
|  | J˘N​(ZN∗;ZN∗​(v),v)=RN​(ZN∗;ZN∗​(v),v)+AN​(ZN∗​(v))=0,v∈{0,1},\breve{J}\_{N}(Z^{\*}\_{N};Z^{\*}\_{N}(v),v)=R\_{N}(Z^{\*}\_{N};Z^{\*}\_{N}(v),v)+A\_{N}(Z^{\*}\_{N}(v))=0,\quad v\in\{0,1\}, |  | (SA.12) |

again with ZN∗​(0),ZN∗​(1)≠0Z^{\ast}\_{N}(0),Z^{\ast}\_{N}(1)\neq 0.

Consider ([SA.12](https://arxiv.org/html/2512.06309v1#A1.E12 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) for v=0v=0. With ζN∗=ZN∗​(1)−ZN∗​(0)≥0\zeta^{\*}\_{N}=Z^{\*}\_{N}(1)-Z^{\*}\_{N}(0)\geq 0, fixing arbitrary ζ>0\zeta>0 as a parameter, we introduce the following function on (−∞,0)(-\infty,0):

|  |  |  |  |
| --- | --- | --- | --- |
|  | F0N​(ζ;z):=J˘N​((z,ζ+z);z,0)=RN​((z,ζ+z);z,0)+AN​(z),z<0.F^{N}\_{0}(\zeta;z):=\breve{J}\_{N}((z,\zeta+z);z,0)=R\_{N}((z,\zeta+z);z,0)+A\_{N}(z),\quad z<0. |  | (SA.13) |

Recalling ([B](https://arxiv.org/html/2512.06309v1#A2.Ex4 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([B](https://arxiv.org/html/2512.06309v1#A2.Ex6 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | F0N​(ζ;z)=g1,N​(z)​Φ¯N​(ζ)+g2,N​(z)​Φ¯N′​(ζ)+AN​(z),z<0.F^{N}\_{0}(\zeta;z)=g\_{1,N}(z)\bar{\varPhi}\_{N}(\zeta)+g\_{2,N}(z)\bar{\varPhi}^{\prime}\_{N}(\zeta)+A\_{N}(z),\quad z<0. |  | (SA.14) |

By Step 2.1 in the proof of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") (i), g1,Ng\_{1,N} has a unique zero z0⋄<0z^{\diamond}\_{0}<0 such that g1,N′​(z)<0g\_{1,N}^{\prime}(z)<0 and g2,N′​(z)<g1,N​(z)<0<g2,N​(z)g\_{2,N}^{\prime}(z)<g\_{1,N}(z)<0<g\_{2,N}(z) for z∈(z0⋄,0)z\in(z^{\diamond}\_{0},0). Since Φ¯N​(ζ)>0\bar{\varPhi}\_{N}(\zeta)>0, Φ¯N′​(ζ)>0\bar{\varPhi}\_{N}^{\prime}(\zeta)>0, and AN​(z)≥0A\_{N}(z)\geq 0, AN′​(z)≤0A\_{N}^{\prime}(z)\leq 0, then F0N​(ζ;z0⋄)>0F^{N}\_{0}(\zeta;z^{\diamond}\_{0})>0 and ∂zF0N​(ζ;z)<0\partial\_{z}F^{N}\_{0}(\zeta;z)<0 for z∈(z0⋄,0)z\in(z^{\diamond}\_{0},0). Similarly as in ([SA.11](https://arxiv.org/html/2512.06309v1#A1.E11 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we have limz↗0F0N​(ζ;z)=−Φ¯N​(ζ)<0\lim\_{z\nearrow 0}F^{N}\_{0}(\zeta;z)=-\bar{\varPhi}\_{N}(\zeta)<0, and so F0N​(ζ;⋅)F^{N}\_{0}(\zeta;\cdot) has a unique zero in (z0⋄,0)(z^{\diamond}\_{0},0), denoted as 𝓏0​(ζ)\mathcal{z}\_{0}(\zeta), which is a continuous function of ζ\zeta. Moreover, since Φ¯N​(0)=1\bar{\varPhi}\_{N}(0)=1 and Φ¯N′​(0)=0\bar{\varPhi}^{\prime}\_{N}(0)=0, we have

|  |  |  |
| --- | --- | --- |
|  | 0=limζ↘0F0N​(ζ;𝓏0​(ζ))=limζ↘0(g1,N​(𝓏0​(ζ))+AN​(𝓏0​(ζ))).0=\lim\_{\zeta\searrow 0}F^{N}\_{0}(\zeta;\mathcal{z}\_{0}(\zeta))=\lim\_{\zeta\searrow 0}\big(g\_{1,N}(\mathcal{z}\_{0}(\zeta))+A\_{N}(\mathcal{z}\_{0}(\zeta))\big). |  |

Again, noting that g1,N′<0g\_{1,N}^{\prime}<0 and AN′≤0A\_{N}^{\prime}\leq 0, then by ([B](https://arxiv.org/html/2512.06309v1#A2.Ex6 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([SA.8](https://arxiv.org/html/2512.06309v1#A1.E8 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), limz↗0(g1,N​(z)+AN​(z))=−1<0\lim\_{z\nearrow 0}(g\_{1,N}(z)+A\_{N}(z))=-1<0, and so we have limζ↘0𝓏0​(ζ)<0\lim\_{\zeta\searrow 0}\mathcal{z}\_{0}(\zeta)<0.

Next, consider ([SA.12](https://arxiv.org/html/2512.06309v1#A1.E12 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) for v=1v=1. As in the proof of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") assertion (i), we denote 𝓏1​(ζ):=ζ+𝓏0​(ζ)\mathcal{z}\_{1}(\zeta):=\zeta+\mathcal{z}\_{0}(\zeta) and 𝒵​(ζ):=(𝓏0​(ζ),𝓏1​(ζ))\mathcal{Z}(\zeta):=(\mathcal{z}\_{0}(\zeta),\mathcal{z}\_{1}(\zeta)). Recalling ([B](https://arxiv.org/html/2512.06309v1#A2.Ex7 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), by ([B.14](https://arxiv.org/html/2512.06309v1#A2.E14 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")),

|  |  |  |
| --- | --- | --- |
|  | G1N​(ζ):=J˘N​(𝒵ζ;𝓏1​(ζ),1)=g1,N​(𝓏1​(ζ))​(Φ^N​(ζ)−1)+g2,N​(𝓏1​(ζ))​Φ^N′​(ζ)+AN​(𝓏1​(ζ)),G^{N}\_{1}(\zeta):=\breve{J}\_{N}(\mathcal{Z}^{\zeta};\mathcal{z}\_{1}(\zeta),1)=g\_{1,N}(\mathcal{z}\_{1}(\zeta))\big(\hat{\varPhi}\_{N}(\zeta)-1\big)+g\_{2,N}(\mathcal{z}\_{1}(\zeta))\hat{\varPhi}^{\prime}\_{N}(\zeta)+A\_{N}(\mathcal{z}\_{1}(\zeta)), |  |

where Φ^N\hat{\varPhi}\_{N} and Φ^N′\hat{\varPhi}^{\prime}\_{N} are given in ([B](https://arxiv.org/html/2512.06309v1#A2.Ex7 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). Since limζ↘0𝓏0​(ζ)<0\lim\_{\zeta\searrow 0}\mathcal{z}\_{0}(\zeta)<0 and 𝓏0​(ζ)∈(z0⋄,0)\mathcal{z}\_{0}(\zeta)\in(z^{\diamond}\_{0},0), limζ↘0𝓏1​(ζ)<0\lim\_{\zeta\searrow 0}\mathcal{z}\_{1}(\zeta)<0 and limζ→∞𝓏1​(ζ)=∞\lim\_{\zeta\to\infty}\mathcal{z}\_{1}(\zeta)=\infty. Hence, there exists ζ˘>0\breve{\zeta}>0 such that 𝓏1​(ζ˘)=0\mathcal{z}\_{1}(\breve{\zeta})=0. Let ζ˘\breve{\zeta} be the largest one having this property, so that 𝓏1​(ζ)>0\mathcal{z}\_{1}(\zeta)>0 for all ζ>ζ˘\zeta>\breve{\zeta}. Note that limz↗0g1,N​(z)=−1\lim\_{z\nearrow 0}g\_{1,N}(z)=-1, limz↗0g2,N​(z)=0\lim\_{z\nearrow 0}g\_{2,N}(z)=0, and limz↗0AN​(z)=0\lim\_{z\nearrow 0}A\_{N}(z)=0, and so G1N​(ζ˘)=1−Φ^N​(ζ˘)>0G^{N}\_{1}(\breve{\zeta})=1-\hat{\varPhi}\_{N}(\breve{\zeta})>0. Moreover, similarly to Step 2.2 in the proof of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") assertion (i), there exists ζ^>ζ˘\hat{\zeta}>\breve{\zeta} such that g1,N​(𝓏1​(ζ^))=0g\_{1,N}(\mathcal{z}\_{1}(\hat{\zeta}))=0 and g2,N​(𝓏1​(ζ^))<0g\_{2,N}(\mathcal{z}\_{1}(\hat{\zeta}))<0. Note that Φ^N′​(ζ^)>0\hat{\varPhi}^{\prime}\_{N}(\hat{\zeta})>0 and, by ([SA.8](https://arxiv.org/html/2512.06309v1#A1.E8 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), AN​(𝓏1​(ζ^))≤0A\_{N}(\mathcal{z}\_{1}(\hat{\zeta}))\leq 0 (as 𝓏1​(ζ^)>0\mathcal{z}\_{1}(\hat{\zeta})>0), and then G1N​(ζ^)<0G^{N}\_{1}(\hat{\zeta})<0. Thus, there exists ζ∗∈(ζ˘,ζ^)\zeta^{\*}\in(\breve{\zeta},\hat{\zeta}) such that G1N​(ζ∗)=0G^{N}\_{1}(\zeta^{\*})=0. Therefore, (𝒵ζ∗,PN​(𝒵ζ∗;⋅))(\mathcal{Z}^{\zeta^{\*}},P\_{N}(\mathcal{Z}^{\zeta^{\*}};\cdot)), with 𝒵ζ∗=(𝓏0​(ζ∗),𝓏1​(ζ∗))\mathcal{Z}^{\zeta^{\*}}=\big(\mathcal{z}\_{0}(\zeta^{\*}),\mathcal{z}\_{1}(\zeta^{\*})\big), is a finite-NN equilibrium in the sense of Definition [2.1](https://arxiv.org/html/2512.06309v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2.3 Equilibrium definition ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading").
∎

Proof of Theorem [SA.1](https://arxiv.org/html/2512.06309v1#A1.Thmtheorem1 "Theorem SA.1. ‣ Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") assertion (ii). As before, we prove the “if” direction and the “only if” direction separately. In a similar fashion as in ([B](https://arxiv.org/html/2512.06309v1#A2.Ex10 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), especially for Φ~Nγ​(Z~γ∗;z~)\tilde{\varPhi}^{\gamma}\_{N}(\tilde{Z}^{\*}\_{\gamma};\tilde{z}), given any γ\gamma-limiting equilibrium (Z~γ∗,P~γ∗)(\tilde{Z}^{\*}\_{\gamma},\tilde{P}^{\*}\_{\gamma}), we have that for z~∈ℝv\tilde{z}\in\mathbb{R}\_{v}, v∈{0,1}v\in\{0,1\},

|  |  |  |  |
| --- | --- | --- | --- |
|  | J~∞γ​(P~γ∗;z~,v)=limN→∞(z~​(χ​e−λ​(Nγ−β​z~)−χ0)​(v−Φ~Nγ​(Z~γ∗;z~))−(1−e−λ​(Nγ−β​z~))​N−γ​C0​(Nγ​z~)).\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=\lim\_{N\to\infty}\Big(\tilde{z}~\big(\chi e^{-\lambda(N^{\gamma-\beta}\tilde{z})}-\chi\_{0}\big)\big(v-\tilde{\varPhi}^{\gamma}\_{N}(\tilde{Z}^{\*}\_{\gamma};\tilde{z})\big)-(1-e^{-\lambda(N^{\gamma-\beta}\tilde{z})})N^{-\gamma}C\_{0}(N^{\gamma}\tilde{z})\Big). |  | (SA.15) |

Let us recall ([B](https://arxiv.org/html/2512.06309v1#A2.Ex10 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and the limits in ([B.17](https://arxiv.org/html/2512.06309v1#A2.E17 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). Also, under Assumption [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), the following additional limits are easily justified: For z~≠0\tilde{z}\neq 0,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | limN→∞N−γ​C0​(Nγ​z~)={C0​(z~),if ​γ=0,Kα​|z~|,if ​γ>0,α=1,∞,if ​γ>0,α>1;\displaystyle\lim\_{N\to\infty}N^{-\gamma}C\_{0}(N^{\gamma}\tilde{z})=\begin{cases}C\_{0}(\tilde{z}),&\quad\text{if }\gamma=0,\\ K\_{\alpha}|\tilde{z}|,&\quad\text{if }\gamma>0,\;\alpha=1,\\ \infty,&\quad\text{if }\gamma>0,\;\alpha>1;\end{cases} |  | (SA.16) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | limN→∞(1−e−λ​(Nγ−β​z~))​N−γ​C0​(Nγ​z~)={0,if ​0<γ<β​θθ+α−1,Kθ​Kα​|z~|θ+α,if ​γ=β​θθ+α−1<β,∞,if ​β​θθ+α−1<γ<β.\displaystyle\lim\_{N\to\infty}(1-e^{-\lambda(N^{\gamma-\beta}\tilde{z})})N^{-\gamma}C\_{0}(N^{\gamma}\tilde{z})=\begin{cases}0,&\quad\text{if }0<\gamma<\frac{\beta\theta}{\theta+\alpha-1},\\ K\_{\theta}K\_{\alpha}|\tilde{z}|^{\theta+\alpha},&\quad\text{if }\gamma=\frac{\beta\theta}{\theta+\alpha-1}<\beta,\\ \infty,&\quad\text{if }\frac{\beta\theta}{\theta+\alpha-1}<\gamma<\beta.\end{cases} |  | (SA.17) |

Step 1 In this step we prove the “if” direction in two cases. Assume ([6.5](https://arxiv.org/html/2512.06309v1#S6.E5 "In 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) holds, and note that β​θ/(θ+α−1)≤β{\beta\theta}/(\theta+\alpha-1)\leq\beta, with equality holding if and only if β=0\beta=0 or α=1\alpha=1.

Case 1 γ=β​θ/(θ+α−1)<1/2\gamma=\beta\theta/(\theta+\alpha-1)<1/2. We must set P~γ∗=p\tilde{P}^{\*}\_{\gamma}=p, and it is unique.

Case 1.1 γ=β=0\gamma=\beta=0. In this case, ([SA.15](https://arxiv.org/html/2512.06309v1#A1.E15 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | J~∞γ​(P~γ∗;z~,v)=(v−p)​z~​(χ​e−λ​(z~)−χ0)−(1−e−λ​(z~))​C0​(z~),z~∈ℝv,v∈{0,1}.\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=(v-p)\tilde{z}~\big(\chi e^{-\lambda(\tilde{z})}-\chi\_{0}\big)-(1-e^{-\lambda(\tilde{z})})C\_{0}(\tilde{z}),\quad\tilde{z}\in\mathbb{R}\_{v},\;v\in\{0,1\}. |  | (SA.18) |

Analogous to ([B](https://arxiv.org/html/2512.06309v1#A2.Ex14 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), for AN​(z~)A\_{N}(\tilde{z}) (from ([SA.8](https://arxiv.org/html/2512.06309v1#A1.E8 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"))) with N=1N=1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | J˘∞γ​(z~,v)\displaystyle\breve{J}^{\gamma}\_{\infty}(\tilde{z},v) | :=eλ​(z~)​∂z~J~∞γ​(P~γ∗;z~,v)=(v−p)​(χ−χ​z~​λ′​(z~)−χ0​eλ​(z~))+A1​(z~);\displaystyle:=e^{\lambda(\tilde{z})}\partial\_{\tilde{z}}\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=(v-p)\big(\chi-\chi\tilde{z}\lambda^{\prime}(\tilde{z})-\chi\_{0}e^{\lambda(\tilde{z})}\big)+A\_{1}(\tilde{z}); |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂z~J˘∞γ​(z~,v)\displaystyle\partial\_{\tilde{z}}\breve{J}^{\gamma}\_{\infty}(\tilde{z},v) | =−(v−p)​(χ​λ′​(z~)+χ​z~​λ′′​(z~)+χ0​eλ​(z~)​λ′​(z~))+A1′​(z~),z<0.\displaystyle=-(v-p)\big(\chi\lambda^{\prime}(\tilde{z})+\chi\tilde{z}\lambda^{\prime\prime}(\tilde{z})+\chi\_{0}e^{\lambda(\tilde{z})}\lambda^{\prime}(\tilde{z})\big)+A\_{1}^{\prime}(\tilde{z}),\quad z<0. |  | (SA.19) |

For v=0v=0, under Assumption [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), it is clear that all the statements in ([B](https://arxiv.org/html/2512.06309v1#A2.Ex15 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) remain true. Thus, by following the same arguments after ([B](https://arxiv.org/html/2512.06309v1#A2.Ex15 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) we see that J~∞γ​(P~γ∗;⋅,0)\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\cdot,0) has a unique maximum point Z~γ∗​(0)<0\tilde{Z}^{\*}\_{\gamma}(0)<0. For v=1v=1, it is similar that J~∞γ​(P~γ∗;⋅,1)\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\cdot,1) has a unique maximum point Z~γ∗​(1)>0\tilde{Z}^{\*}\_{\gamma}(1)>0. Therefore, Z~γ∗=(Z~γ∗​(0),Z~γ∗​(1))\tilde{Z}^{\*}\_{\gamma}=(\tilde{Z}^{\*}\_{\gamma}(0),\tilde{Z}^{\*}\_{\gamma}(1)), together with P~γ∗≡p\tilde{P}^{\*}\_{\gamma}\equiv p, forms the unique γ\gamma-limiting equilibrium.

Case 1.2 β>0\beta>0 and α=1\alpha=1. Then, γ=β>0\gamma=\beta>0, and ([SA.15](https://arxiv.org/html/2512.06309v1#A1.E15 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | J~∞γ​(P~γ∗;z~,v)=(v−p)​z~​(χ​e−λ​(z~)−χ0)−(1−e−λ​(z~))​Kα​|z~|,z~∈ℝv,\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=(v-p)\tilde{z}~\big(\chi e^{-\lambda(\tilde{z})}-\chi\_{0}\big)-(1-e^{-\lambda(\tilde{z})})K\_{\alpha}|\tilde{z}|,\quad\tilde{z}\in\mathbb{R}\_{v}, |  | (SA.20) |

which is the same as ([SA.18](https://arxiv.org/html/2512.06309v1#A1.E18 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) with C0​(z~)=Kα​|z~|C\_{0}(\tilde{z})=K\_{\alpha}|\tilde{z}|. Thus, we claim again that there exists a unique γ\gamma-limiting equilibrium.

Case 1.3 β>0\beta>0 and α>1\alpha>1. Then, γ=β​θ/(θ+α−1)<β\gamma={\beta\theta}/(\theta+\alpha-1)<\beta, and ([SA.15](https://arxiv.org/html/2512.06309v1#A1.E15 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | J~∞γ​(P~γ∗;z~,v)=(v−p)​z~−Kθ​Kα​|z~|θ+α,z~∈ℝv.\displaystyle\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=(v-p)\tilde{z}-K\_{\theta}K\_{\alpha}|\tilde{z}|^{\theta+\alpha},\quad\tilde{z}\in\mathbb{R}\_{v}. |  | (SA.21) |

Since θ+α>1\theta+\alpha>1, it is clear that J~∞γ​(P~γ∗;z~,v)\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v) above has a unique maximum point Z~γ∗​(v)∈ℝv\tilde{Z}^{\*}\_{\gamma}(v)\in\mathbb{R}\_{v}, and so there exists a unique γ\gamma-limiting equilibrium.

Case 2 γ=1/2≤β​θ/(θ+α−1)≤β\gamma=1/2\leq{\beta\theta}/(\theta+\alpha-1)\leq\beta.

Case 2.1 β=γ=1/2\beta=\gamma=1/2. In this case, we have α=1\alpha=1, and based on Assumption [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") conditions (i) and (iii), observe that for some constant Kαv∈ℝK^{v}\_{\alpha}\in\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
|  | C0​(z)∼Kα​|z|+Kαv,as ​|z|→∞.C\_{0}(z)\sim K\_{\alpha}|z|+K^{v}\_{\alpha},\quad\text{as }|z|\to\infty. |  | (SA.22) |

Indeed, when v=1v=1, C0​(z)−Kα​zC\_{0}(z)-K\_{\alpha}z is still convex and C0​(z)−Kα​z=o​(z)C\_{0}(z)-K\_{\alpha}z=o(z) as z→∞z\to\infty, and so the only possibility is that C0​(z)−Kα​zC\_{0}(z)-K\_{\alpha}z is constant when z>0z>0 is large. The same idea goes for v=0v=0.

With this observation, ([SA.15](https://arxiv.org/html/2512.06309v1#A1.E15 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) specializes to

|  |  |  |  |
| --- | --- | --- | --- |
|  | J~∞γ​(P~γ∗;z~,v)=(χ​e−λ​(z~)−χ0)​Q1​(Z~γ∗;z~,v)−(1−e−λ​(z~))​Kα​|z~|,z~∈ℝv,\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=\big(\chi e^{-\lambda(\tilde{z})}-\chi\_{0}\big)Q\_{1}(\tilde{Z}^{\*}\_{\gamma};\tilde{z},v)-(1-e^{-\lambda(\tilde{z})})K\_{\alpha}|\tilde{z}|,\quad\tilde{z}\in\mathbb{R}\_{v}, |  | (SA.23) |

which is a special case of ([6.1](https://arxiv.org/html/2512.06309v1#S6.E1 "In 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) with N=1N=1 and C0​(z)=Kα​|z|C\_{0}(z)=K\_{\alpha}|z|. Thus, by assertion (i), a γ\gamma-limiting equilibrium exists.

Case 2.2 γ=1/2=β​θ/(θ+α−1)<β\gamma=1/2={\beta\theta}/(\theta+\alpha-1)<\beta. Then, ([SA.15](https://arxiv.org/html/2512.06309v1#A1.E15 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) becomes

|  |  |  |
| --- | --- | --- |
|  | J~∞γ​(P~γ∗;z~,v)=Q1​(Z~γ∗;z~,v)−Kθ​Kα​|z~|θ+α,z~∈ℝv.\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=Q\_{1}(\tilde{Z}^{\*}\_{\gamma};\tilde{z},v)-K\_{\theta}K\_{\alpha}|\tilde{z}|^{\theta+\alpha},\quad\tilde{z}\in\mathbb{R}\_{v}. |  |

Adapting the analysis in the proof of assertion (i), one can easily check that in this case, the condition ([B](https://arxiv.org/html/2512.06309v1#A2.Ex6 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) becomes (using zz instead of z~\tilde{z}):

|  |  |  |
| --- | --- | --- |
|  | F01​(ζ;z)=−Φ¯1​(ζ)−z​Φ¯1′​(ζ)+Kθ​Kα​(θ+α)​|z|θ+α−1,z<0.F^{1}\_{0}(\zeta;z)=-\bar{\varPhi}\_{1}(\zeta)-z\bar{\varPhi}^{\prime}\_{1}(\zeta)+K\_{\theta}K\_{\alpha}(\theta+\alpha)|z|^{\theta+\alpha-1},\quad z<0. |  |

Since θ+α>1\theta+\alpha>1, then clearly,

|  |  |  |
| --- | --- | --- |
|  | limz↗0F01​(ζ;z)=−Φ¯1​(ζ)<0,limz→−∞F01​(ζ;z)=∞,∂zF01​(ζ;z)<0.\lim\_{z\nearrow 0}F^{1}\_{0}(\zeta;z)=-\bar{\varPhi}\_{1}(\zeta)<0,\quad\lim\_{z\to-\infty}F^{1}\_{0}(\zeta;z)=\infty,\quad\partial\_{z}F^{1}\_{0}(\zeta;z)<0. |  |

Thus, F01​(ζ;z)F^{1}\_{0}(\zeta;z) has a unique zero 𝓏0​(ζ)<0\mathcal{z}\_{0}(\zeta)<0. Also, it is clear that 𝓏0​(ζ)≥−Φ¯1​(ζ)/Φ¯1′​(ζ)\mathcal{z}\_{0}(\zeta)\geq-\bar{\varPhi}\_{1}(\zeta)/\penalty 50\bar{\varPhi}\_{1}^{\prime}(\zeta). By ([B.22](https://arxiv.org/html/2512.06309v1#A2.E22 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we have limζ→∞𝓏0​(ζ)=0\lim\_{\zeta\to\infty}\mathcal{z}\_{0}(\zeta)=0. Moreover, with limζ↘0Φ¯1​(ζ)=1\lim\_{\zeta\searrow 0}\bar{\varPhi}\_{1}(\zeta)=1 and limζ↘0Φ¯1′​(ζ)=0\lim\_{\zeta\searrow 0}\bar{\varPhi}^{\prime}\_{1}(\zeta)=0, we easily see that limζ↘0𝓏0​(ζ)=−(Kθ​Kα​(θ+α))1/(θ+α−1)<0\lim\_{\zeta\searrow 0}\mathcal{z}\_{0}(\zeta)=-\big(K\_{\theta}K\_{\alpha}(\theta+\alpha)\big)^{1/(\theta+\alpha-1)}<0.
In particular, this implies that, for 𝓏1​(ζ)=ζ+𝓏0​(ζ)\mathcal{z}\_{1}(\zeta)=\zeta+\mathcal{z}\_{0}(\zeta),

|  |  |  |  |
| --- | --- | --- | --- |
|  | limζ↘0𝓏1​(ζ)<0,limζ→∞𝓏1​(ζ)=∞.\lim\_{\zeta\searrow 0}\mathcal{z}\_{1}(\zeta)<0,\quad\lim\_{\zeta\to\infty}\mathcal{z}\_{1}(\zeta)=\infty. |  | (SA.24) |

On the other hand, the condition ([B.23](https://arxiv.org/html/2512.06309v1#A2.E23 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | G11​(ζ)=−(Φ^1​(ζ)−1)−𝓏1​(ζ)​Φ^1′​(ζ)−Kθ​Kα​(θ+α)​|𝓏1​(ζ)|θ+α−1.G^{1}\_{1}(\zeta)=-\big(\hat{\varPhi}\_{1}(\zeta)-1\big)-\mathcal{z}\_{1}(\zeta)\hat{\varPhi}^{\prime}\_{1}(\zeta)-K\_{\theta}K\_{\alpha}(\theta+\alpha)|\mathcal{z}\_{1}(\zeta)|^{\theta+\alpha-1}. |  | (SA.25) |

By ([SA.24](https://arxiv.org/html/2512.06309v1#A1.E24 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), there exists ζ˘>0\breve{\zeta}>0 such that 𝓏1​(ζ˘)=0\mathcal{z}\_{1}(\breve{\zeta})=0, and 𝓏1​(ζ)>0\mathcal{z}\_{1}(\zeta)>0 for all ζ>ζ˘\zeta>\breve{\zeta}. By ([SA.25](https://arxiv.org/html/2512.06309v1#A1.E25 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([SA.24](https://arxiv.org/html/2512.06309v1#A1.E24 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), it is also clear that G11​(ζ˘)>0G^{1}\_{1}(\breve{\zeta})>0 and limζ→∞G11​(ζ)=−∞\lim\_{\zeta\to\infty}G^{1}\_{1}(\zeta)=-\infty, and so there exists ζ∗>ζ˘\zeta^{\*}>\breve{\zeta} such that G11​(ζ∗)=0G^{1}\_{1}(\zeta^{\*})=0. Therefore, it follows from the same arguments as in the proof of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") assertion (i) that, upon setting Z~γ∗:=(𝓏0​(ζ∗),𝓏1​(ζ∗))\tilde{Z}^{\*}\_{\gamma}:=(\mathcal{z}\_{0}(\zeta^{\*}),\mathcal{z}\_{1}(\zeta^{\*})), (Z~γ∗,P1​(Z~γ∗;⋅))(\tilde{Z}^{\*}\_{\gamma},P\_{1}(\tilde{Z}^{\*}\_{\gamma};\cdot)\big) is a γ\gamma-limiting equilibrium.

Case 2.3 γ=1/2<β​θ/(θ+α−1)≤β\gamma=1/2<{\beta\theta}/(\theta+\alpha-1)\leq\beta. Then, ([SA.15](https://arxiv.org/html/2512.06309v1#A1.E15 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) reduces to J~∞γ​(P~γ∗;z~,v)=Q1​(Z~γ∗;z~,v)\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=Q\_{1}(\tilde{Z}^{\*}\_{\gamma};\tilde{z},v) for z~∈ℝv\tilde{z}\in\mathbb{R}\_{v}, which has been analyzed in Case 2 in the proof of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") assertion (ii), so there exists a γ\gamma-limiting equilibrium.

Step 2 We now prove the “only if” direction. Assuming that there is a γ\gamma-limiting equilibrium (Z~γ∗,P~γ∗)(\tilde{Z}^{\*}\_{\gamma},\tilde{P}^{\*}\_{\gamma}), our goal is to prove that γ\gamma satisfies ([6.5](https://arxiv.org/html/2512.06309v1#S6.E5 "In 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). Notably, the limit ([SA.16](https://arxiv.org/html/2512.06309v1#A1.E16 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) is used when γ≥β\gamma\geq\beta, while ([SA.17](https://arxiv.org/html/2512.06309v1#A1.E17 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) is used when γ<β\gamma<\beta, and so we may exclude the cases (γ≥β,γ>0,α>1)(\gamma\geq\beta,\gamma>0,\alpha>1) and β​θ/(θ+α−1)<γ<β{\beta\theta}/(\theta+\alpha-1)<\gamma<\beta. Now, if β​θ/(θ+α−1)<γ{\beta\theta}/(\theta+\alpha-1)<\gamma, then by the second excluded case, we have γ≥β\gamma\geq\beta, which by the first excluded case further implies α=1\alpha=1. Hence, we can focus on the following two cases:

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ≤β​θθ+α−1≤βorα=1,γ>β=β​θθ+α−1.\gamma\leq\frac{\beta\theta}{\theta+\alpha-1}\leq\beta\quad\mbox{or}\quad\alpha=1,\;\gamma>\beta=\frac{\beta\theta}{\theta+\alpha-1}. |  | (SA.26) |

Case 3 γ<1/2\gamma<1/2. In the second case of ([SA.26](https://arxiv.org/html/2512.06309v1#A1.E26 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), with P~γ∗=p\tilde{P}^{\*}\_{\gamma}=p, ([SA.15](https://arxiv.org/html/2512.06309v1#A1.E15 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) gives

|  |  |  |
| --- | --- | --- |
|  | J~∞γ​(P~γ∗;z~,1)=−χ0​z~​(1−p)−Kα​|z~|=−(χ0​(1−p)+Kα)​z~,z~>0,\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},1)=-\chi\_{0}\tilde{z}~(1-p)-K\_{\alpha}|\tilde{z}|=-\big(\chi\_{0}(1-p)+K\_{\alpha}\big)\tilde{z},\quad\tilde{z}>0, |  |

which has no maximum point in (0,∞)(0,\infty), and so we must have the first case of ([SA.26](https://arxiv.org/html/2512.06309v1#A1.E26 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), but if γ<β​θ/(θ+α−1)≤β\gamma<{\beta\theta}/(\theta+\alpha-1)\leq\beta, then ([SA.15](https://arxiv.org/html/2512.06309v1#A1.E15 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) becomes J~∞γ​(P~γ∗;z~,v)=z~​(v−p)\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=\tilde{z}~(v-p), with no maximum point in ℝv\mathbb{R}\_{v} either. Thus, it can only be that γ=β​θ/(θ+α−1)\gamma={\beta\theta}/(\theta+\alpha-1), which verifies ([6.5](https://arxiv.org/html/2512.06309v1#S6.E5 "In 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) because γ<1/2\gamma<1/2 here.

Case 4 γ=1/2\gamma=1/2. Suppose β​θ/(θ+α−1)<1/2=γ{\beta\theta}/(\theta+\alpha-1)<1/2=\gamma. Then, we have the second case of ([SA.26](https://arxiv.org/html/2512.06309v1#A1.E26 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), and ([SA.15](https://arxiv.org/html/2512.06309v1#A1.E15 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) becomes

|  |  |  |
| --- | --- | --- |
|  | J~∞γ​(P~γ∗;z~,v)=−χ0​Q1​(Z~γ∗;z~,v)−Kα​|z~|,z~∈ℝv.\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=-\chi\_{0}Q\_{1}(\tilde{Z}^{\*}\_{\gamma};\tilde{z},v)-K\_{\alpha}|\tilde{z}|,\quad\tilde{z}\in\mathbb{R}\_{v}. |  |

Note that Q1​(Z~γ∗;z~,v)>0Q\_{1}(\tilde{Z}^{\*}\_{\gamma};\tilde{z},v)>0 for z~≠0\tilde{z}\neq 0. Then, J~∞γ​(P~γ∗;z~,v)<0\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)<0 for z~≠0\tilde{z}\neq 0, while limz~→0J~∞γ​(P~γ∗;z~,v)=0\lim\_{\tilde{z}\to 0}\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=0 clearly, which means that J~∞γ​(P~γ∗;⋅,v)\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\cdot,v) has no maximum point in ℝ∖{0}\mathbb{R}\setminus\{0\}. Therefore, we must have β​θ/(θ+α−1)≥1/2=γ{\beta\theta}/(\theta+\alpha-1)\geq 1/2=\gamma, verifying ([6.5](https://arxiv.org/html/2512.06309v1#S6.E5 "In 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")).

Case 5 γ>1/2\gamma>1/2. We consider two subcases. Again, we write zγ∗:=(Z~γ∗​(0)+Z~γ∗​(1))/2z^{\*}\_{\gamma}:=(\tilde{Z}^{\*}\_{\gamma}(0)+\tilde{Z}^{\*}\_{\gamma}(1))/2.

Case 5.1 zγ∗≥0z^{\*}\_{\gamma}\geq 0. Note that in this case, for v=0v=0, −(𝟙{z~>zγ∗}+𝟙{z~=zγ∗}/2)=0-(\mathds{1}\_{\{\tilde{z}>z^{\*}\_{\gamma}\}}+\mathds{1}\_{\{\tilde{z}=z^{\*}\_{\gamma}\}}/2)=0 for all z~<0\tilde{z}<0. Then, based on ([SA.26](https://arxiv.org/html/2512.06309v1#A1.E26 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), by ([SA.15](https://arxiv.org/html/2512.06309v1#A1.E15 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) we have that for z~<0\tilde{z}<0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | J~∞γ​(P~γ∗;z~,0)={0,if ​γ<β​θθ+α−1≤β,−Kθ​Kα​|z~|θ+α,if ​γ=β​θθ+α−1<β,−(1−e−λ​(z~))​Kα​|z~|,if ​γ=β​θθ+α−1<β,−Kα​|z~|,if ​α=1,γ>β=β​θθ+α−1,\displaystyle\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},0)=\begin{cases}0,&\quad\text{if }\gamma<\frac{\beta\theta}{\theta+\alpha-1}\leq\beta,\\ -K\_{\theta}K\_{\alpha}|\tilde{z}|^{\theta+\alpha},&\quad\text{if }\gamma=\frac{\beta\theta}{\theta+\alpha-1}<\beta,\\ -(1-e^{-\lambda(\tilde{z})})K\_{\alpha}|\tilde{z}|,&\quad\text{if }\gamma=\frac{\beta\theta}{\theta+\alpha-1}<\beta,\\ -K\_{\alpha}|\tilde{z}|,&\quad\text{if }\alpha=1,\gamma>\beta=\frac{\beta\theta}{\theta+\alpha-1},\end{cases} |  | (SA.27) |

and in all these cases, J~∞γ​(P~γ∗;Z~γ∗​(0),0)=supz~<0J~∞γ​(P~γ∗;z~,0)=0\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{Z}^{\*}\_{\gamma}(0),0)=\sup\_{\tilde{z}<0}\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},0)=0. This violates the requirement J~∞γ​(P~γ∗;Z~γ∗​(0),0)≠0\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{Z}^{\*}\_{\gamma}(0),0)\neq 0 in Definition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading").

Case 5.2 zγ∗<0z^{\*}\_{\gamma}<0. In this case, for v=1v=1, 1−(𝟙{z~>zγ∗}+𝟙{z~=zγ∗}/2)=𝟙{z~<zγ∗}+𝟙{z~=zγ∗}/2=01-(\mathds{1}\_{\{\tilde{z}>z^{\*}\_{\gamma}\}}+\mathds{1}\_{\{\tilde{z}=z^{\*}\_{\gamma}\}}/2)=\mathds{1}\_{\{\tilde{z}<z^{\*}\_{\gamma}\}}+\mathds{1}\_{\{\tilde{z}=z^{\*}\_{\gamma}\}}/2=0 for all z~>0\tilde{z}>0. Then, J~∞γ​(P~γ∗;z~,1)\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},1) has the same expression as in ([SA.27](https://arxiv.org/html/2512.06309v1#A1.E27 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) except with z~>0\tilde{z}>0, which results in the same violation. Thus, we conclude that no γ\gamma-limiting equilibrium exists in the case γ>1/2\gamma>1/2.
∎

Proof of Theorem [SA.1](https://arxiv.org/html/2512.06309v1#A1.Thmtheorem1 "Theorem SA.1. ‣ Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") assertion (iii). Let Assumption [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") hold; by ([6.5](https://arxiv.org/html/2512.06309v1#S6.E5 "In 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), let γ=β​θ/(θ+α−1)<1/2\gamma={\beta\theta/(\theta+\alpha-1)}<1/2. We proceed as in the proof of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") assertion (iii), particularly focusing on the case v=0v=0.

Step 1 Let us note that in ([SA.14](https://arxiv.org/html/2512.06309v1#A1.E14 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), the zero ZN∗​(0)Z^{\*}\_{N}(0) of the function F0N​(ZN∗​(1)−ZN∗​(0);⋅)F^{N}\_{0}(Z^{\*}\_{N}(1)-Z^{\*}\_{N}(0);\cdot) satisfies z⋄<ZN∗​(0)<0z^{\diamond}<Z^{\*}\_{N}(0)<0, where z⋄≡z0⋄z^{\diamond}\equiv z^{\diamond}\_{0} is the unique zero of g1,Ng\_{1,N} defined in ([B](https://arxiv.org/html/2512.06309v1#A2.Ex6 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). Write z~0N:=N−γ​ZN∗​(0)\tilde{z}^{N}\_{0}:=N^{-\gamma}Z^{\*}\_{N}(0) and z^0N:=N−β​ZN∗​(0)\hat{z}^{N}\_{0}:=N^{-\beta}Z^{\*}\_{N}(0). By ([B.24](https://arxiv.org/html/2512.06309v1#A2.E24 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and the subsequent arguments, we have that |z^0N|≤K1|\hat{z}^{N}\_{0}|\leq K\_{1} for some K1>0K\_{1}>0; in particular, when γ=β\gamma=\beta, z~0N=z^0N\tilde{z}^{N}\_{0}=\hat{z}^{N}\_{0} is also bounded in NN by K1K\_{1}.

Next, we justify the boundedness of z~0N\tilde{z}^{N}\_{0} in the case γ<β\gamma<\beta, which is recalled to imply α>1\alpha>1 and γ>0\gamma>0. Denote as before ζN∗:=ZN∗​(1)−ZN∗​(0)\zeta^{\*}\_{N}:=Z^{\*}\_{N}(1)-Z^{\*}\_{N}(0), and note that F0N​(ζN∗,ZN∗​(0))=0F^{N}\_{0}(\zeta^{\*}\_{N},Z^{\*}\_{N}(0))=0, where F0NF^{N}\_{0} is defined in ([SA.14](https://arxiv.org/html/2512.06309v1#A1.E14 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). From the arguments after ([B.10](https://arxiv.org/html/2512.06309v1#A2.E10 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we see that g2,Ng\_{2,N} is decreasing in (z⋄,0)(z^{\diamond},0) with limz↗0g2,N​(z)=0\lim\_{z\nearrow 0}g\_{2,N}(z)=0, so g2,N​(z)>0g\_{2,N}(z)>0 for z∈(z⋄,0)z\in(z^{\diamond},0), and in particular g2,N​(ZN∗​(0))>0g\_{2,N}(Z^{\*}\_{N}(0))>0. Recall ([SA.8](https://arxiv.org/html/2512.06309v1#A1.E8 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and note that −λN′​(ZN∗​(0))​C0​(ZN∗​(0))>0-\lambda^{\prime}\_{N}(Z^{\*}\_{N}(0))C\_{0}(Z^{\*}\_{N}(0))>0, −(eλN​(ZN∗​(0))−1)​C0′​(ZN∗​(0))>0-(e^{\lambda\_{N}(Z^{\*}\_{N}(0))}-1)C^{\prime}\_{0}(Z^{\*}\_{N}(0))>0.
Also note that λN​(ZN∗​(0))=λ​(z^0N)\lambda\_{N}(Z^{\*}\_{N}(0))=\lambda(\hat{z}^{N}\_{0}) and λN′​(ZN∗​(0))=N−β​λ′​(z^0N)\lambda\_{N}^{\prime}(Z^{\*}\_{N}(0))=N^{-\beta}\lambda^{\prime}(\hat{z}^{N}\_{0}). Since for ζ>0\zeta>0, 0<Φ¯N​(ζ)<10<\bar{\varPhi}\_{N}(\zeta)<1 and Φ¯N′​(ζ)>0\bar{\varPhi}\_{N}^{\prime}(\zeta)>0, by ([SA.14](https://arxiv.org/html/2512.06309v1#A1.E14 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([B](https://arxiv.org/html/2512.06309v1#A2.Ex6 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")),

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | N−β​|λ′​(z^0N)​C0​(ZN∗​(0))|=|λN′​(ZN∗​(0))​C0​(ZN∗​(0))|≤|g1,N​(ZN∗​(0))​Φ¯N​(ζN∗)|\displaystyle\quad N^{-\beta}\big|\lambda^{\prime}(\hat{z}^{N}\_{0})C\_{0}(Z^{\*}\_{N}(0))\big|=\big|\lambda\_{N}^{\prime}(Z^{\*}\_{N}(0))C\_{0}(Z^{\*}\_{N}(0))\big|\leq|g\_{1,N}(Z^{\*}\_{N}(0))\bar{\varPhi}\_{N}(\zeta^{\*}\_{N})| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤|χ​ZN∗​(0)​λN′​(ZN∗​(0))−χ+χ0​eλN​(ZN∗​(0))|=|χ​z^0N​λ′​(z^0N)−χ+χ0​eλ​(z^0N)|≤K2,\displaystyle\leq\big|\chi Z^{\*}\_{N}(0)\lambda^{\prime}\_{N}(Z^{\*}\_{N}(0))-\chi+\chi\_{0}e^{\lambda\_{N}(Z^{\*}\_{N}(0))}\big|=\big|\chi\hat{z}^{N}\_{0}\lambda^{\prime}(\hat{z}^{N}\_{0})-\chi+\chi\_{0}e^{\lambda(\hat{z}^{N}\_{0})}\big|\leq K\_{2}, |  | (SA.28) |

for some constant K2>0K\_{2}>0, where we have used the crucial fact that |z^0N|≤K1|\hat{z}^{N}\_{0}|\leq K\_{1}. Moreover, by Assumption [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") condition (ii), we have K3:=supz∈[−K1,0)|z|θ−1/|λ′​(z)|<∞K\_{3}:=\sup\_{z\in[-K\_{1},0)}{|z|^{\theta-1}/|\lambda^{\prime}(z)|}<\infty, and so |λ′​(z^0N)|≥|z^0N|θ−1/K3|\lambda^{\prime}(\hat{z}^{N}\_{0})|\geq|\hat{z}^{N}\_{0}|^{\theta-1}/K\_{3}. Further note that by assuming without loss of generality that |z~0N|≥1|\tilde{z}^{N}\_{0}|\geq 1 (as otherwise we have established the desired boundedness of z~0N\tilde{z}^{N}\_{0}), then |ZN∗​(0)|≥Nγ|Z^{\*}\_{N}(0)|\geq N^{\gamma}, and thus by Assumption [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") (iii) we have C0​(ZN∗​(0))≥Kα​|ZN∗​(0)|α/2C\_{0}(Z^{\*}\_{N}(0))\geq K\_{\alpha}|Z^{\*}\_{N}(0)|^{\alpha}/2 for NN large. Therefore, we obtain

|  |  |  |
| --- | --- | --- |
|  | 2​K2​K3Kα≥2​K2Kα​N−β​|λ′​(z^0N)​C0​(ZN∗​(0))|≥N−β​|z^0N|θ−1​|ZN∗​(0)|α\displaystyle\quad\tfrac{2K\_{2}K\_{3}}{K\_{\alpha}}\geq\tfrac{2K\_{2}}{K\_{\alpha}}N^{-\beta}\big|\lambda^{\prime}(\hat{z}^{N}\_{0})C\_{0}(Z^{\*}\_{N}(0))\big|\geq N^{-\beta}|\hat{z}^{N}\_{0}|^{\theta-1}|Z^{\*}\_{N}(0)|^{\alpha} |  |
|  |  |  |
| --- | --- | --- |
|  | =N−β​|Nγ−β​z~0N|θ−1​|Nγ​z~0N|α=N−β+(γ−β)​(θ−1)+γ​α​|z~0N|θ+α−1=|z~0N|θ+α−1,\displaystyle=N^{-\beta}|N^{\gamma-\beta}\tilde{z}^{N}\_{0}|^{\theta-1}|N^{\gamma}\tilde{z}^{N}\_{0}|^{\alpha}=N^{-\beta+(\gamma-\beta)(\theta-1)+\gamma\alpha}|\tilde{z}^{N}\_{0}|^{\theta+\alpha-1}=|\tilde{z}^{N}\_{0}|^{\theta+\alpha-1}, |  |

where the last equality is due to γ=β​θ/(θ+α−1)\gamma={\beta\theta/(\theta+\alpha-1)}. This immediately implies that |z~0N|≤K0|\tilde{z}^{N}\_{0}|\leq K\_{0} for some K0>0K\_{0}>0.

Furthermore, in this case ([B.25](https://arxiv.org/html/2512.06309v1#A2.E25 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) generalizes into

|  |  |  |  |
| --- | --- | --- | --- |
|  | F1N​(ζ;z):=g1,N​(z)​(Φ^N​(ζ)−1)+g2,N​(z)​Φ^N′​(ζ)+AN​(z),z>0,\displaystyle F^{N}\_{1}(\zeta;z):=g\_{1,N}(z)(\hat{\varPhi}\_{N}(\zeta)-1)+g\_{2,N}(z)\hat{\varPhi}^{\prime}\_{N}(\zeta)+A\_{N}(z),\quad z>0, |  | (SA.29) |

and in the same manner we can show that z~1N:=N−γ​ZN∗​(1)\tilde{z}^{N}\_{1}:=N^{-\gamma}Z^{\*}\_{N}(1) is also bounded by K0K\_{0}.

Step 2 In this step we prove the uniform convergence of FvN​(Nγ​ζ~;Nγ​z~)F^{N}\_{v}(N^{\gamma}\tilde{\zeta};N^{\gamma}\tilde{z}), for 0<ζ~≤2​K00<\tilde{\zeta}\leq 2K\_{0} and z~∈ℝv\tilde{z}\in\mathbb{R}\_{v} with |z~|≤K0|\tilde{z}|\leq K\_{0}, and we shall only do it for v=0v=0. The case v=1v=1 can be proved analogously. We consider three cases, corresponding to, respectively, Case 1.1, Case 1.2, and Case 1.3 in the proof of assertion (ii).

Case 1 γ=β=0\gamma=\beta=0. Recalling ([SA.14](https://arxiv.org/html/2512.06309v1#A1.E14 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([A](https://arxiv.org/html/2512.06309v1#A1.Ex9 "Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |F0N​(Nγ​ζ~;Nγ​z~)−J˘∞γ​(z~,0)|≤IN+|AN​(Nγ​z~)−A1​(z~)|,\displaystyle\big|F^{N}\_{0}(N^{\gamma}\tilde{\zeta};N^{\gamma}\tilde{z})-\breve{J}^{\gamma}\_{\infty}(\tilde{z},0)\big|\leq I\_{N}+\big|A\_{N}(N^{\gamma}\tilde{z})-A\_{1}(\tilde{z})\big|, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | where | IN:=|g1,N​(Nγ)​Φ¯N​(Nγ​ζ~)+g2,N​(Nγ​z~)​Φ¯N′​(Nγ​ζ~)−p​g1,1​(z~)|,\displaystyle\quad I\_{N}:=\big|g\_{1,N}(N^{\gamma})\bar{\varPhi}\_{N}(N^{\gamma}\tilde{\zeta})+g\_{2,N}(N^{\gamma}\tilde{z})\bar{\varPhi}^{\prime}\_{N}(N^{\gamma}\tilde{\zeta})-pg\_{1,1}(\tilde{z})\big|, |  |

where INI\_{N} is exactly the (absolute) difference indicated in ([B.26](https://arxiv.org/html/2512.06309v1#A2.E26 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), with |IN|≤K​N2​γ−1|I\_{N}|\leq KN^{2\gamma-1}. Moreover, from ([SA.8](https://arxiv.org/html/2512.06309v1#A1.E8 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) we see that AN​(Nγ​z~)=A1​(z~)A\_{N}(N^{\gamma}\tilde{z})=A\_{1}(\tilde{z}) when γ=β=0\gamma=\beta=0 or γ=β>0\gamma=\beta>0 and C0​(z)=Kα​|z|C\_{0}(z)=K\_{\alpha}|z|. Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |F0N​(Nγ​ζ~;Nγ​z~)−J˘∞γ​(z~,0)|≤K​N2​γ−1.\big|F^{N}\_{0}(N^{\gamma}\tilde{\zeta};N^{\gamma}\tilde{z})-\breve{J}^{\gamma}\_{\infty}(\tilde{z},0)\big|\leq KN^{2\gamma-1}. |  | (SA.30) |

Case 2 γ=β>0\gamma=\beta>0 and α=1\alpha=1. This is the same as Case 1, with the specialization C0​(z)=Kα​|z|C\_{0}(z)=K\_{\alpha}|z|, and thus ([SA.30](https://arxiv.org/html/2512.06309v1#A1.E30 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) remains true.

Case 3. β>0\beta>0 and α>1\alpha>1, so that γ=β​θ/(θ+α−1)<β\gamma={\beta\theta/(\theta+\alpha-1)}<\beta. In this case, recalling ([SA.21](https://arxiv.org/html/2512.06309v1#A1.E21 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | J˘∞γ​(z~,0):=∂z~J~∞γ​(P~γ∗;z~,v)=−p+Kθ​Kα​(θ+α)​|z~|θ+α−1.\breve{J}^{\gamma}\_{\infty}(\tilde{z},0):=\partial\_{\tilde{z}}\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},v)=-p+K\_{\theta}K\_{\alpha}(\theta+\alpha)|\tilde{z}|^{\theta+\alpha-1}. |  | (SA.31) |

Then, by ([SA.14](https://arxiv.org/html/2512.06309v1#A1.E14 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), ([B](https://arxiv.org/html/2512.06309v1#A2.Ex6 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), and ([SA.8](https://arxiv.org/html/2512.06309v1#A1.E8 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we have

|  |  |  |
| --- | --- | --- |
|  | |F0N​(Nγ​ζ~;Nγ​z~)−J˘∞γ​(z~,0)|\displaystyle\quad\big|F^{N}\_{0}(N^{\gamma}\tilde{\zeta};N^{\gamma}\tilde{z})-\breve{J}^{\gamma}\_{\infty}(\tilde{z},0)\big| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤|g1,N​(Nγ​z~)​Φ¯N​(Nγ​ζ~)+p|+|g2,N​(Nγ​z~)​Φ¯N′​(Nγ​ζ~)|\displaystyle\leq\big|g\_{1,N}(N^{\gamma}\tilde{z})\bar{\varPhi}\_{N}(N^{\gamma}\tilde{\zeta})+p\Big|+\Big|g\_{2,N}(N^{\gamma}\tilde{z})\bar{\varPhi}^{\prime}\_{N}(N^{\gamma}\tilde{\zeta})\big| |  |
|  |  |  |
| --- | --- | --- |
|  | +|−λN′​(Nγ​z~)​C0​(Nγ​z~)−(eλN​(Nγ​z~)−1)​C0′​(Nγ​z~)−Kθ​Kα​(θ+α)​|z~|θ+α−1|.\displaystyle\quad+\big|-\lambda^{\prime}\_{N}(N^{\gamma}\tilde{z})C\_{0}(N^{\gamma}\tilde{z})-(e^{\lambda\_{N}(N^{\gamma}\tilde{z})}-1)C^{\prime}\_{0}(N^{\gamma}\tilde{z})-K\_{\theta}K\_{\alpha}(\theta+\alpha)|\tilde{z}|^{\theta+\alpha-1}\big|. |  |

Recall that Nγ​Φ¯N′​(Nγ​ζ~)+|Φ¯N​(Nγ​ζ~)−p|≤K​N2​γ−1N^{\gamma}\bar{\varPhi}\_{N}^{\prime}(N^{\gamma}\tilde{\zeta})+\big|\bar{\varPhi}\_{N}(N^{\gamma}\tilde{\zeta})-p\big|\leq KN^{2\gamma-1} for 0<ζ~≤2​K00<\tilde{\zeta}\leq 2K\_{0}, and in the following KK again denotes a generic positive constant that can vary. Moreover, by Assumption [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmassumption1 "Assumption 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") conditions (ii) and (iii), defining θ~′:=θ​(1+θ′)\tilde{\theta}^{\prime}:=\theta(1+\theta^{\prime}), α~′:=α−α′\tilde{\alpha}^{\prime}:=\alpha-\alpha^{\prime}, for z~∈[−K0,0)\tilde{z}\in[-K\_{0},0),

|  |  |  |
| --- | --- | --- |
|  | g1,N​(Nγ​z~)=χ​Nγ​z~​N−β​λ′​(Nγ−β​z~)−χ+χ0​eλ​(Nγ−β​z~)\displaystyle g\_{1,N}(N^{\gamma}\tilde{z})=\chi N^{\gamma}\tilde{z}N^{-\beta}\lambda^{\prime}(N^{\gamma-\beta}\tilde{z})-\chi+\chi\_{0}e^{\lambda(N^{\gamma-\beta}\tilde{z})} |  |
|  |  |  |
| --- | --- | --- |
|  | =χ​z~​Nγ−β​(−Kθ​θ​|Nγ−β​z~|θ−1+O​(|Nγ−β|θ~′−1))−χ+χ0​(1+Kθ​|Nγ−β​z~|θ+O​(|Nγ−β|θ~′))\displaystyle\quad=\chi\tilde{z}N^{\gamma-\beta}\big(-K\_{\theta}\theta|N^{\gamma-\beta}\tilde{z}|^{\theta-1}+O(|N^{\gamma-\beta}|^{\tilde{\theta}^{\prime}-1})\big)-\chi+\chi\_{0}\big(1+K\_{\theta}|N^{\gamma-\beta}\tilde{z}|^{\theta}+O(|N^{\gamma-\beta}|^{\tilde{\theta}^{\prime}})\big) |  |
|  |  |  |
| --- | --- | --- |
|  | =−1+O​(N(γ−β)​θ​(1+θ′));\displaystyle\quad=-1+O(N^{(\gamma-\beta)\theta(1+\theta^{\prime})}); |  |
|  |  |  |
| --- | --- | --- |
|  | g2,N​(Nγ​z~)=(χ0​eλ​(Nγ−β​z~)−χ)​Nγ​z~=Nγ​z~​(−1+o​(1));\displaystyle g\_{2,N}(N^{\gamma}\tilde{z})=(\chi\_{0}e^{\lambda(N^{\gamma-\beta}\tilde{z})}-\chi)N^{\gamma}\tilde{z}=N^{\gamma}\tilde{z}\big(-1+o(1)\big); |  |
|  |  |  |
| --- | --- | --- |
|  | λN′​(Nγ​z~)​C0​(Nγ​z~)=N−β​λ′​(Nγ−β​z~)​C0​(Nγ​z~)\displaystyle\lambda^{\prime}\_{N}(N^{\gamma}\tilde{z})C\_{0}(N^{\gamma}\tilde{z})=N^{-\beta}\lambda^{\prime}(N^{\gamma-\beta}\tilde{z})C\_{0}(N^{\gamma}\tilde{z}) |  |
|  |  |  |
| --- | --- | --- |
|  | =N−β​(−Kθ​θ​|Nγ−β​z~|θ−1+O​(|Nγ−β|θ~′−1))​(Kα​|Nγ​z~|α+O​(|Nγ|α~′))\displaystyle\quad=N^{-\beta}\big(-K\_{\theta}\theta|N^{\gamma-\beta}\tilde{z}|^{\theta-1}+O(|N^{\gamma-\beta}|^{\tilde{\theta}^{\prime}-1})\big)\big(K\_{\alpha}|N^{\gamma}\tilde{z}|^{\alpha}+O(|N^{\gamma}|^{\tilde{\alpha}^{\prime}})\big) |  |
|  |  |  |
| --- | --- | --- |
|  | =−Kθ​Kα​θ​|z~|θ+α−1​N−β+(γ−β)​(θ−1)+γ​α+O​(N−β+max⁡{(γ−β)​(θ~′−1)+γ​α,(γ−β)​(θ−1)+γ​α~′})\displaystyle\quad=-K\_{\theta}K\_{\alpha}\theta|\tilde{z}|^{\theta+\alpha-1}N^{-\beta+(\gamma-\beta)(\theta-1)+\gamma\alpha}+O\big(N^{-\beta+\max\{(\gamma-\beta)(\tilde{\theta}^{\prime}-1)+\gamma\alpha,(\gamma-\beta)(\theta-1)+\gamma\tilde{\alpha}^{\prime}\}}\big) |  |
|  |  |  |
| --- | --- | --- |
|  | =−Kθ​Kα​θ​|z~|θ+α−1+O​(Nmax⁡{(γ−β)​θ​θ′,−γ​α′});\displaystyle\quad=-K\_{\theta}K\_{\alpha}\theta|\tilde{z}|^{\theta+\alpha-1}+O\big(N^{\max\{(\gamma-\beta)\theta\theta^{\prime},-\gamma\alpha^{\prime}\}}\big); |  |
|  |  |  |
| --- | --- | --- |
|  | (eλN​(Nγ​z~)−1)​C0′​(Nγ​z~)=(eλ​(Nγ−β​z~)−1)​C0′​(Nγ​z~)\displaystyle(e^{\lambda\_{N}(N^{\gamma}\tilde{z})}-1)C^{\prime}\_{0}(N^{\gamma}\tilde{z})=(e^{\lambda(N^{\gamma-\beta}\tilde{z})}-1)C^{\prime}\_{0}(N^{\gamma}\tilde{z}) |  |
|  |  |  |
| --- | --- | --- |
|  | =(−Kθ​|Nγ−β​z~|θ+O​(N(γ−β)​θ~′))​(Kα​α​|Nγ​z~|α−1+O​(Nγ​(α~′−1)))\displaystyle\quad=\big(-K\_{\theta}|N^{\gamma-\beta}\tilde{z}|^{\theta}+O(N^{(\gamma-\beta)\tilde{\theta}^{\prime}})\big)\big(K\_{\alpha}\alpha|N^{\gamma}\tilde{z}|^{\alpha-1}+O(N^{\gamma(\tilde{\alpha}^{\prime}-1)})\big) |  |
|  |  |  |
| --- | --- | --- |
|  | =−Kθ​Kα​α​|z~|θ+α−1​N(γ−β)​θ+γ​(α−1)+O​(Nmax⁡{(γ−β)​θ+γ​(α~′−1),(γ−β)​θ~′+γ​(α−1)})\displaystyle\quad=-K\_{\theta}K\_{\alpha}\alpha|\tilde{z}|^{\theta+\alpha-1}N^{(\gamma-\beta)\theta+\gamma(\alpha-1)}+O\big(N^{\max\{(\gamma-\beta)\theta+\gamma(\tilde{\alpha}^{\prime}-1),(\gamma-\beta)\tilde{\theta}^{\prime}+\gamma(\alpha-1)\}}\big) |  |
|  |  |  |
| --- | --- | --- |
|  | =−Kθ​Kα​θ​|z~|θ+α−1+O​(Nmax⁡{(γ−β)​θ​θ′,−γ​α′}),\displaystyle\quad=-K\_{\theta}K\_{\alpha}\theta|\tilde{z}|^{\theta+\alpha-1}+O\big(N^{\max\{(\gamma-\beta)\theta\theta^{\prime},-\gamma\alpha^{\prime}\}}\big), |  |

where the notations OO and oo are understood as being uniform in z~\tilde{z}. Then, since by γ=β​θ/(θ+α−1)\gamma={\beta\theta/(\theta+\alpha-1)}, β=γ​(1+(α−1)/θ)\beta=\gamma(1+{(\alpha-1)/\theta}),

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |F0N​(Nγ​ζ~;Nγ​z~)−J˘∞γ​(z~,0)|\displaystyle\quad\big|F^{N}\_{0}(N^{\gamma}\tilde{\zeta};N^{\gamma}\tilde{z})-\breve{J}^{\gamma}\_{\infty}(\tilde{z},0)\big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤|(−1+O​(N(γ−β)​θ​(1+θ′)))​(p+O​(N2​γ−1))+p|+|O​(N2​γ−1)|+|O​(Nmax⁡{(γ−β)​θ​θ′,−γ​α′})|\displaystyle\leq\big|\big(-1+O(N^{(\gamma-\beta)\theta(1+\theta^{\prime})})\big)\big(p+O(N^{2\gamma-1})\big)+p\big|+\big|O(N^{2\gamma-1})\big|+\big|O\big(N^{\max\{(\gamma-\beta)\theta\theta^{\prime},-\gamma\alpha^{\prime}\}}\big)\big| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤K​(N2​γ−1+Nmax⁡{(γ−β)​θ​θ′,−γ​α′})≤K​Nmax⁡{2​γ−1,−γ​(α−1)​θ′,−γ​α′}.\displaystyle\leq K\big(N^{2\gamma-1}+N^{\max\{(\gamma-\beta)\theta\theta^{\prime},-\gamma\alpha^{\prime}\}}\big)\leq KN^{\max\{2\gamma-1,-\gamma(\alpha-1)\theta^{\prime},-\gamma\alpha^{\prime}\}}. |  | (SA.32) |

Step 3 We now prove ([SA.1](https://arxiv.org/html/2512.06309v1#A1.E1a "In Theorem SA.1. ‣ Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). First, in Case 1 above, by ([SA.9](https://arxiv.org/html/2512.06309v1#A1.E9 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) we see A1′​(z~)≤0A\_{1}^{\prime}(\tilde{z})\leq 0, z~<0\tilde{z}<0. Then, based on Step 3 in the proof of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") assertion (iii) as well as ([A](https://arxiv.org/html/2512.06309v1#A1.Ex9 "Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we have
∂z~J˘∞γ​(z~,0)≤p​χ​λ′​(z~)≤−p​χ​|λ′​(Z~γ∗​(0)/2)|\partial\_{\tilde{z}}\breve{J}^{\gamma}\_{\infty}(\tilde{z},0)\leq p\chi\lambda^{\prime}(\tilde{z})\leq-p\chi|\lambda^{\prime}(\tilde{Z}^{\ast}\_{\gamma}(0)/2)|, for all z~≤Z~γ∗​(0)/2\tilde{z}\leq\tilde{Z}^{\ast}\_{\gamma}(0)/2. Thus, by ([SA.30](https://arxiv.org/html/2512.06309v1#A1.E30 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and exactly the same arguments as in Step 3 in the proof of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") assertion (iii), we obtain |z~0N−Z~γ∗​(0)|≤K​N2​γ−1|\tilde{z}^{N}\_{0}-\tilde{Z}^{\ast}\_{\gamma}(0)|\leq KN^{2\gamma-1}. Similarly, the same estimate holds for Case 2 above.

For Case 3 above,
by ([SA.31](https://arxiv.org/html/2512.06309v1#A1.E31 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂z~J˘∞γ​(z~,0)\displaystyle\partial\_{\tilde{z}}\breve{J}^{\gamma}\_{\infty}(\tilde{z},0) | =∂z~(−p+Kθ​Kα​(θ+α)​|z~|θ+α−1)=−Kθ​Kα​(θ+α)​(θ+α−1)​|z~|θ+α−2\displaystyle=\partial\_{\tilde{z}}\Big(-p+K\_{\theta}K\_{\alpha}(\theta+\alpha)|\tilde{z}|^{\theta+\alpha-1}\Big)=-K\_{\theta}K\_{\alpha}(\theta+\alpha)(\theta+\alpha-1)|\tilde{z}|^{\theta+\alpha-2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤−Kθ​Kα​(θ+α)​(θ+α−1)​|12​Z~γ∗​(0)|θ+α−2,z~≤12​Z~γ∗​(0),\displaystyle\leq-K\_{\theta}K\_{\alpha}(\theta+\alpha)(\theta+\alpha-1)\big|\tfrac{1}{2}\tilde{Z}^{\ast}\_{\gamma}(0)\big|^{\theta+\alpha-2},\quad\tilde{z}\leq\tfrac{1}{2}\tilde{Z}^{\ast}\_{\gamma}(0), |  |

from where similar arguments and ([A](https://arxiv.org/html/2512.06309v1#A1.Ex35 "Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) yield the last estimate in ([SA.1](https://arxiv.org/html/2512.06309v1#A1.E1a "In Theorem SA.1. ‣ Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")).

Finally, the case v=1v=1 can be proved similarly. Additionally, the same estimate in ([4.1](https://arxiv.org/html/2512.06309v1#S4.Ex2 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) in the setting of Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") stands – by the exact same arguments in its proof.
∎

Proof of Theorem [SA.1](https://arxiv.org/html/2512.06309v1#A1.Thmtheorem1 "Theorem SA.1. ‣ Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") assertion (iv). We follow the proof of Theorem [4.2](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") presented in Appendix [C](https://arxiv.org/html/2512.06309v1#A3 "Appendix C Proof of Theorem 4.2 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"). In Definition [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmdefinition1 "Definition 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), first, ([4.7](https://arxiv.org/html/2512.06309v1#S4.E7 "In Definition 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) is justified based on Theorem [4.2](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") with ϵ=ϵN=K​Nγ−1/2\epsilon=\epsilon\_{N}=KN^{\gamma-1/2}, so it suffices to verify ([4.6](https://arxiv.org/html/2512.06309v1#S4.E6 "In Definition 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) with some appropriate ϵ\epsilon. To this end, note that by ([6.1](https://arxiv.org/html/2512.06309v1#S6.E1 "In 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | N−γ​JN​(p;Nγ​z~,v)\displaystyle N^{-\gamma}J\_{N}(p;N^{\gamma}\tilde{z},v) | =N−γ​e−λ​(Nγ−β​z~)​(v−p)​Nγ​z~−N−γ​(1−e−λ​(Nγ−β​z~))​C0​(Nγ​z~)\displaystyle=N^{-\gamma}e^{-\lambda(N^{\gamma-\beta}\tilde{z})}(v-p)N^{\gamma}\tilde{z}-N^{-\gamma}(1-e^{-\lambda(N^{\gamma-\beta}\tilde{z})})C\_{0}(N^{\gamma}\tilde{z}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(v−p)​z~​(χ​e−λ​(Nγ−β​z~)−χ0)−(1−e−λ​(Nγ−β​z~))​N−γ​C0​(Nγ​z~),z∈ℝv.\displaystyle=(v-p)\tilde{z}(\chi e^{-\lambda(N^{\gamma-\beta}\tilde{z})}-\chi\_{0})-(1-e^{-\lambda(N^{\gamma-\beta}\tilde{z})})N^{-\gamma}C\_{0}(N^{\gamma}\tilde{z}),\quad z\in\mathbb{R}\_{v}. |  | (SA.33) |

Since, again, γ=β​θ/(θ+α−1)<1/2\gamma={\beta\theta/(\theta+\alpha-1)}<1/2 and P~γ∗=p\tilde{P}^{\*}\_{\gamma}=p, we turn to the two cases in Step 2 in the above proof of assertion (iii).

In Case 1, namely γ=β=0\gamma=\beta=0, ([SA.18](https://arxiv.org/html/2512.06309v1#A1.E18 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) gives that

|  |  |  |
| --- | --- | --- |
|  | N−γ​JN​(p;Nγ​z~,v)=(v−p)​z~​(χ​e−λ​(z~)−χ0)−(1−e−λ​(z~))​C0​(z~)=J~∞γ​(p;z,v).N^{-\gamma}J\_{N}(p;N^{\gamma}\tilde{z},v)=(v-p)\tilde{z}(\chi e^{-\lambda(\tilde{z})}-\chi\_{0})-(1-e^{-\lambda(\tilde{z})})C\_{0}(\tilde{z})=\tilde{J}^{\gamma}\_{\infty}(p;z,v). |  |

Then, by Definition [3.1](https://arxiv.org/html/2512.06309v1#S3.Thmdefinition1 "Definition 3.1. ‣ 3 Limiting equilibrium and convergence ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"),

|  |  |  |
| --- | --- | --- |
|  | N−γ​JN​(p;Nγ​Z~γ∗​(v),v)=J~∞γ​(p;Z~γ∗​(v),v)=supz~∈ℝvJ~∞γ​(p;z~,v)=supz∈ℝvN−γ​JN​(p;z,v),N^{-\gamma}J\_{N}(p;N^{\gamma}\tilde{Z}^{\*}\_{\gamma}(v),v)=\tilde{J}^{\gamma}\_{\infty}(p;\tilde{Z}^{\*}\_{\gamma}(v),v)=\sup\_{\tilde{z}\in\mathbb{R}\_{v}}\tilde{J}^{\gamma}\_{\infty}(p;\tilde{z},v)=\sup\_{z\in\mathbb{R}\_{v}}N^{-\gamma}J\_{N}(p;z,v), |  |

which implies ([4.6](https://arxiv.org/html/2512.06309v1#S4.E6 "In Definition 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) with ϵ=0\epsilon=0. Therefore, combined with ([4.7](https://arxiv.org/html/2512.06309v1#S4.E7 "In Definition 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), ϵ=ϵN=K​Nγ−1/2\epsilon=\epsilon\_{N}=KN^{\gamma-1/2}. The same holds in Case 2: γ=β>0\gamma=\beta>0 and α=1\alpha=1.

It remains to consider Case 3, namely β>0\beta>0 and α>1\alpha>1. We will verify ([4.6](https://arxiv.org/html/2512.06309v1#S4.E6 "In Definition 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) only for v=0v=0; the case v=1v=1 can be considered similarly. Recall ([A](https://arxiv.org/html/2512.06309v1#A1.Ex39 "Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and denote

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | J˘N​(p;z~,0):=e−λ​(Nγ−β​z~)​∂z~(N−γ​JN​(p;Nγ​z~,0))=−p​(χ−χ0​eλ​(Nγ−β​z~))\displaystyle\breve{J}\_{N}(p;\tilde{z},0):=e^{-\lambda(N^{\gamma-\beta}\tilde{z})}\partial\_{\tilde{z}}\Big(N^{-\gamma}J\_{N}(p;N^{\gamma}\tilde{z},0)\Big)=-p\big(\chi-\chi\_{0}e^{\lambda(N^{\gamma-\beta}\tilde{z})}\big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +p​χ​Nγ−β​z~​λ′​(Nγ−β​z~)−N−β​λ′​(Nγ−β​z~)​C0​(Nγ​z~)−(eλ​(Nγ−β​z~)−1)​C0′​(Nγ​z~),z~<0,\displaystyle\quad+p\chi N^{\gamma-\beta}\tilde{z}\lambda^{\prime}(N^{\gamma-\beta}\tilde{z})-N^{-\beta}\lambda^{\prime}(N^{\gamma-\beta}\tilde{z})C\_{0}(N^{\gamma}\tilde{z})-(e^{\lambda(N^{\gamma-\beta}\tilde{z})}-1)C\_{0}^{\prime}(N^{\gamma}\tilde{z}),\quad\tilde{z}<0, |  | (SA.34) |

with

|  |  |  |
| --- | --- | --- |
|  | limz~↘0JN​(p;Nγ​z~,0)=0,limz~→−∞JN​(p;Nγ​z~,0)=−∞,limz~↘0J˘N​(p;z~,0)=−p<0.\lim\_{\tilde{z}\searrow 0}J\_{N}(p;N^{\gamma}\tilde{z},0)=0,\quad\lim\_{\tilde{z}\to-\infty}J\_{N}(p;N^{\gamma}\tilde{z},0)=-\infty,\quad\lim\_{\tilde{z}\searrow 0}\breve{J}\_{N}(p;\tilde{z},0)=-p<0. |  |

By the first and third limits, it is clear that supz~<0JN​(p;Nγ​z~,0)>0\sup\_{\tilde{z}<0}J\_{N}(p;N^{\gamma}\tilde{z},0)>0. Then, by the first two limits above,
we see that JN​(p;⋅,0)J\_{N}(p;\cdot,0) has a maximum point z~N∗<0\tilde{z}^{\*}\_{N}<0, which satisfies J˘N​(p;z~N∗,0)=0\breve{J}\_{N}(p;\tilde{z}^{\*}\_{N},0)=0.

We claim that |z~N∗|≤K0|\tilde{z}^{\*}\_{N}|\leq K\_{0} for some K0>0K\_{0}>0. Indeed, note that all three terms in the second line of ([A](https://arxiv.org/html/2512.06309v1#A1.Ex42 "Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) are positive. Then, denoting z^N∗:=Nγ−β​z~N∗\hat{z}^{\*}\_{N}:=N^{\gamma-\beta}\tilde{z}^{\*}\_{N}, we must have

|  |  |  |
| --- | --- | --- |
|  | |p​χ​z^N∗​λ′​(z^N∗)|+|N−β​λ′​(z^N∗)​C0​(Nγ​z~N∗)|≤p​(χ−χ0​eλ​(z^N∗))≤p​χ.|p\chi\hat{z}^{\*}\_{N}\lambda^{\prime}(\hat{z}^{\*}\_{N})|+\big|N^{-\beta}\lambda^{\prime}(\hat{z}^{\*}\_{N})C\_{0}(N^{\gamma}\tilde{z}^{\*}\_{N})\big|\leq p\big(\chi-\chi\_{0}e^{\lambda(\hat{z}^{\*}\_{N})}\big)\leq p\chi. |  |

In particular, |z^N∗​λ′​(z^N∗)|≤1|\hat{z}^{\*}\_{N}\lambda^{\prime}(\hat{z}^{\*}\_{N})|\leq 1. Then, clearly |z^N∗|≤K1|\hat{z}^{\*}\_{N}|\leq K\_{1} for some K1>0K\_{1}>0, and

|  |  |  |
| --- | --- | --- |
|  | |N−β​λ′​(z^N∗)​C0​(Nγ​z~N∗)|≤p​χ,\big|N^{-\beta}\lambda^{\prime}(\hat{z}^{\*}\_{N})C\_{0}(N^{\gamma}\tilde{z}^{\*}\_{N})\big|\leq p\chi, |  |

which is ([A](https://arxiv.org/html/2512.06309v1#A1.Ex15 "Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) with K2=p​χK\_{2}=p\chi. Then, employing the arguments following ([A](https://arxiv.org/html/2512.06309v1#A1.Ex15 "Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we obtain the desired boundedness of z~N∗\tilde{z}^{\*}\_{N}.

Now, by ([SA.21](https://arxiv.org/html/2512.06309v1#A1.E21 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), we have

|  |  |  |
| --- | --- | --- |
|  | J~∞γ​(P~γ∗;z~,0)=−p​z~−Kθ​Kα​|z~|θ+α,z~<0,\displaystyle\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},0)=-p\tilde{z}-K\_{\theta}K\_{\alpha}|\tilde{z}|^{\theta+\alpha},\quad\tilde{z}<0, |  |

from which using that |z~|≤K0|\tilde{z}|\leq K\_{0}, by ([A](https://arxiv.org/html/2512.06309v1#A1.Ex39 "Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) we obtain that as N→∞N\to\infty,

|  |  |  |
| --- | --- | --- |
|  | |N−γ​JN​(p;Nγ​z~,0)−J~∞γ​(P~γ∗;z~,0)|\displaystyle\quad\big|N^{-\gamma}J\_{N}(p;N^{\gamma}\tilde{z},0)-\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z},0)\big| |  |
|  |  |  |
| --- | --- | --- |
|  | =|−p​z~​(χ​e−λ​(Nγ−β​z~)−χ0)−(1−e−λ​(Nγ−β​z~))​N−γ​C0​(Nγ​z~)+p​z~+Kθ​Kα​|z~|θ+α|\displaystyle=\big|-p\tilde{z}(\chi e^{-\lambda(N^{\gamma-\beta}\tilde{z})}-\chi\_{0})-(1-e^{-\lambda(N^{\gamma-\beta}\tilde{z})})N^{-\gamma}C\_{0}(N^{\gamma}\tilde{z})+p\tilde{z}+K\_{\theta}K\_{\alpha}|\tilde{z}|^{\theta+\alpha}\big| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤K​|e−λ​(Nγ−β​z~)−1|+|(1−e−λ​(Nγ−β​z~))​N−γ​C0​(Nγ​z~)−Kθ​Kα​|z~|θ+α|\displaystyle\leq K\big|e^{-\lambda(N^{\gamma-\beta}\tilde{z})}-1\big|+\big|(1-e^{-\lambda(N^{\gamma-\beta}\tilde{z})})N^{-\gamma}C\_{0}(N^{\gamma}\tilde{z})-K\_{\theta}K\_{\alpha}|\tilde{z}|^{\theta+\alpha}\big| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤K​|λ​(Nγ−β​z~)|+|(λ​(Nγ−β​z~)+O​(λ2​(Nγ−β​z~)))​N−γ​C0​(Nγ​z~)−Kθ​Kα​|z~|θ+α|\displaystyle\leq K\big|\lambda(N^{\gamma-\beta}\tilde{z})\big|+\big|\big(\lambda(N^{\gamma-\beta}\tilde{z})+O(\lambda^{2}(N^{\gamma-\beta}\tilde{z}))\big)N^{-\gamma}C\_{0}(N^{\gamma}\tilde{z})-K\_{\theta}K\_{\alpha}|\tilde{z}|^{\theta+\alpha}\big| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤K|Nγ−βz~|θ+|(Kθ|Nγ−βz~|θ+O(|Nγ−β|θ​(1+θ′))+O(|Nγ−β|2​θ))\displaystyle\leq K|N^{\gamma-\beta}\tilde{z}|^{\theta}+\big|\big(K\_{\theta}|N^{\gamma-\beta}\tilde{z}|^{\theta}+O(|N^{\gamma-\beta}|^{\theta(1+\theta^{\prime})})+O(|N^{\gamma-\beta}|^{2\theta})\big) |  |
|  |  |  |
| --- | --- | --- |
|  | ×N−γ(Kα|Nγz~|α+O(|Nγ|α−α′))−KθKα|z~|θ+α|\displaystyle\qquad\times N^{-\gamma}\big(K\_{\alpha}|N^{\gamma}\tilde{z}|^{\alpha}+O(|N^{\gamma}|^{\alpha-\alpha^{\prime}})\big)-K\_{\theta}K\_{\alpha}|\tilde{z}|^{\theta+\alpha}\big| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤K​(N(γ−β)​θ+N(γ−β)​θ−γ+γ​(α−α′)+N(γ−β)​θ​(1+θ′)−γ+γ​α+N(γ−β)​2​θ−γ+γ​α)\displaystyle\leq K\big(N^{(\gamma-\beta)\theta}+N^{(\gamma-\beta)\theta-\gamma+\gamma(\alpha-\alpha^{\prime})}+N^{(\gamma-\beta)\theta(1+\theta^{\prime})-\gamma+\gamma\alpha}+N^{(\gamma-\beta)2\theta-\gamma+\gamma\alpha}\big) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤K(N−γ​(α−1)+N−γ​α′+N−γ​(α−1)​θ′)≤KNmax⁡{−γ​(α−1),−γ​α′,−γ​(α−1)​θ′}=:12ϵN′.\displaystyle\leq K\big(N^{-\gamma(\alpha-1)}+N^{-\gamma\alpha^{\prime}}+N^{-\gamma(\alpha-1)\theta^{\prime}}\big)\leq KN^{\max\{-\gamma(\alpha-1),-\gamma\alpha^{\prime},-\gamma(\alpha-1)\theta^{\prime}\}}=:\tfrac{1}{2}\epsilon^{\prime}\_{N}. |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | supz<0N−γ​JN​(p;z,0)=N−γ​JN​(p;Nγ​z~N∗,0)≤J~∞γ​(P~γ∗;z~N∗,0)+12​ϵN′\displaystyle\quad\sup\_{z<0}N^{-\gamma}J\_{N}(p;z,0)=N^{-\gamma}J\_{N}(p;N^{\gamma}\tilde{z}^{\*}\_{N},0)\leq\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{z}^{\*}\_{N},0)+\tfrac{1}{2}\epsilon^{\prime}\_{N} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤J~∞γ​(P~γ∗;Z~γ∗​(0),0)+12​ϵN′≤N−γ​JN​(p;Nγ​Z~γ∗​(0),0)+ϵN′,\displaystyle\leq\tilde{J}^{\gamma}\_{\infty}(\tilde{P}^{\*}\_{\gamma};\tilde{Z}^{\*}\_{\gamma}(0),0)+\tfrac{1}{2}\epsilon^{\prime}\_{N}\leq N^{-\gamma}J\_{N}(p;N^{\gamma}\tilde{Z}^{\*}\_{\gamma}(0),0)+\epsilon^{\prime}\_{N}, |  |

which verifies ([4.6](https://arxiv.org/html/2512.06309v1#S4.E6 "In Definition 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) with ϵ=ϵN′\epsilon=\epsilon^{\prime}\_{N} and whose combination with ([4.7](https://arxiv.org/html/2512.06309v1#S4.E7 "In Definition 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) yields that in this case, ϵ=max⁡{ϵN,ϵN′}=K​Nmax⁡{γ−1/2,−γ​(α−1),−γ​α′,−γ​(α−1)​θ′}\epsilon=\max\{\epsilon\_{N},\epsilon^{\prime}\_{N}\}=KN^{\max\{\gamma-1/2,-\gamma(\alpha-1),-\gamma\alpha^{\prime},-\gamma(\alpha-1)\theta^{\prime}\}}. This completes the proof.
∎

## Supplemental Appendix B Auxiliary details

This supplemental appendix provides auxiliary details for minor illustrative or computational arguments made throughout the paper, including all those not covered in the preceding appendices.

Details for hazard rate ([2.1](https://arxiv.org/html/2512.06309v1#S2.Ex2 "2.1 Prosecution mechanism ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"))

Let N=σ=1N=\sigma=1 without loss of generality. Then, for ([2.1.2](https://arxiv.org/html/2512.06309v1#S2.E2 "In 2.1 Prosecution mechanism ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), it is easy to see that

|  |  |  |
| --- | --- | --- |
|  | 𝓅1​(z)=D​(z)​ℙ​{|W+z|≥y¯}=D​(z)2​(erfc​y¯+z2+erfc​y¯−z2),z∈ℝ,\mathcal{p}\_{1}(z)=D(z)\mathbb{P}\{|W+z|\geq\bar{y}\}=\frac{D(z)}{2}\bigg(\mathrm{erfc}\frac{\bar{y}+z}{\sqrt{2}}+\mathrm{erfc}\frac{\bar{y}-z}{\sqrt{2}}\bigg),\quad z\in\mathbb{R}, |  |

where y¯>0\bar{y}>0. Matching this to ([2.1.1](https://arxiv.org/html/2512.06309v1#S2.E1 "In 2.1 Prosecution mechanism ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and using that λ1\lambda\_{1} is positive-valued gives ([2.1](https://arxiv.org/html/2512.06309v1#S2.Ex2 "2.1 Prosecution mechanism ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")).

Further, for the complementary error function, it is familiar that (see Abramowitz and Stegun ([1972](https://arxiv.org/html/2512.06309v1#bib.bib1)) Chap. 7)

|  |  |  |
| --- | --- | --- |
|  | erfc​x=1−2​xπ+O​(x2),as ​x→0.\mathrm{erfc}x=1-\tfrac{2x}{\sqrt{\pi}}+O(x^{2}),\quad\text{as }x\to 0. |  |

Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ1​(z)≡λ​(z)\displaystyle\lambda\_{1}(z)\equiv\lambda(z) | =−log⁡(1−D​(z)2​(erfc​y¯+z2+erfc​y¯−z2))\displaystyle=-\log\bigg(1-\frac{D(z)}{2}\bigg(\mathrm{erfc}\frac{\bar{y}+z}{\sqrt{2}}+\mathrm{erfc}\frac{\bar{y}-z}{\sqrt{2}}\bigg)\bigg) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−log⁡(1−D​(z))+O​(z2)=O​(|z|min⁡{θD,2})as ​z→0,\displaystyle=-\log(1-D(z))+O(z^{2})=O(|z|^{\min\{\theta\_{D},2\}})\quad\text{as }z\to 0, |  | (SB.1) |

assuming that D​(z)∼KD​|z|θDD(z)\sim K\_{D}|z|^{\theta\_{D}} as |z|↘0|z|\searrow 0, with KD>0K\_{D}>0 and θD≥1\theta\_{D}\geq 1. Note that since |erfc​x|<1|\mathrm{erfc}x|<1, ∀x∈ℝ\forall x\in\mathbb{R}, the function DD is required to be bounded by 1, or else ([B](https://arxiv.org/html/2512.06309v1#A2.Ex3a "Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) is not real-valued. Moreover, if DD is twice continuously differentiable, then so is λ\lambda in ([B](https://arxiv.org/html/2512.06309v1#A2.Ex3a "Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). Using that erfc′​x=−2​ex2/π\mathrm{erfc}^{\prime}x=-2e^{x^{2}}/\sqrt{\pi}, for z>0z>0 we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ′​(z)=D​(z)2​π​(e−(y¯+z)2/2+e−(y¯−z)2/2)+D′​(z)2​(erfc​y¯+z2+erfc​y¯−z2)1−D​(z)2​(erfc​y¯+z2+erfc​y¯−z2).\lambda^{\prime}(z)=\frac{\frac{D(z)}{\sqrt{2\pi}}\big(e^{-(\bar{y}+z)^{2}/2}+e^{-(\bar{y}-z)^{2}/2}\big)+\frac{D^{\prime}(z)}{2}\big(\mathrm{erfc}\frac{\bar{y}+z}{\sqrt{2}}+\mathrm{erfc}\frac{\bar{y}-z}{\sqrt{2}}\big)}{1-\frac{D(z)}{2}\big(\mathrm{erfc}\frac{\bar{y}+z}{\sqrt{2}}+\mathrm{erfc}\frac{\bar{y}-z}{\sqrt{2}}\big)}. |  | (SB.2) |

Since the function erfc​((y¯+z)/2)+erfc​((y¯−z)/2)\mathrm{erfc}((\bar{y}+z)/\sqrt{2})+\mathrm{erfc}((\bar{y}-z)/\sqrt{2}), z>0z>0, is strictly increasing, ([SB.2](https://arxiv.org/html/2512.06309v1#A2.E2a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) is clearly increasing provided that D′D^{\prime} is also increasing; in particular,

|  |  |  |
| --- | --- | --- |
|  | λ′​(z)≥12​π​e−(y¯+z)2/2​(e2​y¯​z−1)​D​(z)≥2π​y¯​e−y¯2/2​D​(z),z>0.\lambda^{\prime}(z)\geq\tfrac{1}{\sqrt{2\pi}}e^{-(\bar{y}+z)^{2}/2}(e^{2\bar{y}z}-1)D(z)\geq\sqrt{\tfrac{2}{\pi}}\bar{y}e^{-\bar{y}^{2}/2}D(z),\quad z>0. |  |

It follows from the oddity of λ′\lambda^{\prime} that |λ′​(z)|≥b​D​(z)|\lambda^{\prime}(z)|\geq bD(z), z≠0z\neq 0, with b=2​y¯​e−y¯2/2/2​πb=2\bar{y}e^{-\bar{y}^{2}/2}/\sqrt{2\pi}. Therefore, for D​(z)=KD​|z|θDD(z)=K\_{D}|z|^{\theta\_{D}}, we have |λ′​(z)|≥b​D​(z)=b​KD​|z|θD|\lambda^{\prime}(z)|\geq bD(z)=bK\_{D}|z|^{\theta\_{D}}, z≠0z\neq 0. Additionally, with D′​(0)D^{\prime}(0) and D′′​(0)D^{\prime\prime}(0) both finite, a further expansion ([SB.2](https://arxiv.org/html/2512.06309v1#A2.E2a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) around z=0z=0 directly shows that λ′​(z)=λ′​(0)+O​(|z|)\lambda^{\prime}(z)=\lambda^{\prime}(0)+O(|z|) as z→0z\to 0.
∎

Details for Example [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmexample1 "Example 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"). Using Theorem [4.1](https://arxiv.org/html/2512.06309v1#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), since γ=β<1/2\gamma=\beta<1/2, the equilibrium price function P~γ∗=p∈(0,1)\tilde{P}^{\ast}\_{\gamma}=p\in(0,1), and, as in ([B.6](https://arxiv.org/html/2512.06309v1#A2.E6 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), the limiting equilibrium conditions are the decoupled equations J˘∞γ​(z~,v)=0\breve{J}^{\gamma}\_{\infty}(\tilde{z},v)=0, v∈{0,1}v\in\{0,1\}, for J˘∞γ​(z~,v)\breve{J}^{\gamma}\_{\infty}(\tilde{z},v) defined in ([B](https://arxiv.org/html/2512.06309v1#A2.Ex14 "Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). With λ​(z~)=z~2\lambda(\tilde{z})=\tilde{z}^{2} and χ0=χ−1≥0\chi\_{0}=\chi-1\geq 0, they specialize to

|  |  |  |  |
| --- | --- | --- | --- |
|  | J˘∞γ​(z~,v)=(v−p)​(χ−2​χ​z~2−χ0​ez~2)=0,\breve{J}^{\gamma}\_{\infty}(\tilde{z},v)=(v-p)\big(\chi-2\chi\tilde{z}^{2}-\chi\_{0}e^{\tilde{z}^{2}}\big)=0, |  | (SB.3) |

to be solved for z~∈ℝv\tilde{z}\in\mathbb{R}\_{v}. Note that J˘∞γ​(z~,1)=−(1−p)/p​J˘∞γ​(−z~,0)\breve{J}^{\gamma}\_{\infty}(\tilde{z},1)=-(1-p)/p\breve{J}^{\gamma}\_{\infty}(-\tilde{z},0) for z~>0\tilde{z}>0, which explains the symmetry (about 0) of their solutions. By letting x=1/2−z~2x=1/2-\tilde{z}^{2}, ([SB.3](https://arxiv.org/html/2512.06309v1#A2.E3a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) is equivalent to

|  |  |  |
| --- | --- | --- |
|  | 2​χ​x−χ0​e12−x=0⟺x​ex=e​χ02​χ.2\chi x-\chi\_{0}e^{\frac{1}{2}-x}=0\quad\Longleftrightarrow\quad xe^{x}=\tfrac{\sqrt{e}\chi\_{0}}{2\chi}. |  |

whose unique nonnegative solution can be expressed in terms of the Lambert W\mathrm{W} function as x=W0​(e​χ0/(2​χ))x=\mathrm{W}\_{0}(\sqrt{e}\chi\_{0}/(2\chi)), and z~=±1/2−x\tilde{z}=\pm\sqrt{1/2-x}. Thus, setting χ=3\chi=3 (and χ0=2\chi\_{0}=2) gives us the γ\gamma-limiting equilibrium strategy specified in ([4.5](https://arxiv.org/html/2512.06309v1#S4.E5 "In Example 4.1. ‣ 4 Predominant scenario: Civil penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")).
◆\blacklozenge

Details for Example [6.1](https://arxiv.org/html/2512.06309v1#S6.Thmexample1 "Example 6.1. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"). From the proof of Theorem [SA.1](https://arxiv.org/html/2512.06309v1#A1.Thmtheorem1 "Theorem SA.1. ‣ Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") assertion (ii), since γ=β<1/2\gamma=\beta<1/2, we clearly have P~γ∗=p=1/3\tilde{P}^{\ast}\_{\gamma}=p=1/3, while the limiting equilibrium conditions are again the decoupled system J˘∞γ​(z~,v)=0\breve{J}^{\gamma}\_{\infty}(\tilde{z},v)=0, v∈{0,1}v\in\{0,1\}, for J˘∞γ​(z~,v)\breve{J}^{\gamma}\_{\infty}(\tilde{z},v) in ([A](https://arxiv.org/html/2512.06309v1#A1.Ex9 "Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), both for β=0\beta=0 and for β>0\beta>0, the latter case being due to C0​(z)=|z|C\_{0}(z)=|z| as used in ([SA.20](https://arxiv.org/html/2512.06309v1#A1.E20 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) (with Kα=1K\_{\alpha}=1). With λ​(z)=|z~|\lambda(z)=|\tilde{z}| further, and recalling χ=1\chi=1, by ([A](https://arxiv.org/html/2512.06309v1#A1.Ex9 "Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([SA.8](https://arxiv.org/html/2512.06309v1#A1.E8 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) we find that

|  |  |  |  |
| --- | --- | --- | --- |
|  | J˘∞γ​(z~,v)=(v−13)​(1−|z~|)+(−1)v​(|z~|+e|z~|−1)=0,\breve{J}^{\gamma}\_{\infty}(\tilde{z},v)=\big(v-\tfrac{1}{3}\big)(1-|\tilde{z}|)+(-1)^{v}\big(|\tilde{z}|+e^{|\tilde{z}|}-1\big)=0, |  | (SB.4) |

to be solved for z~∈ℝv\tilde{z}\in\mathbb{R}\_{v}, v∈{0,1}v\in\{0,1\}. Let z~v∈ℝv\tilde{z}\_{v}\in\mathbb{R}\_{v} denote the solution, and set xv=1−|z~v|x\_{v}=1-|\tilde{z}\_{v}|. Then, for v=0v=0, ([SB.4](https://arxiv.org/html/2512.06309v1#A2.E4a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) is equivalent to

|  |  |  |
| --- | --- | --- |
|  | −13​x0+(−x0+e1−x0)=0⟺x0​ex0=3​e4.-\tfrac{1}{3}x\_{0}+\big(-x\_{0}+e^{1-x\_{0}}\big)=0\quad\Longleftrightarrow\quad x\_{0}e^{x\_{0}}=\tfrac{3e}{4}. |  |

Then, x0=W0​(3​e/4)x\_{0}=\mathrm{W}\_{0}(3e/\penalty 504), and so z~0=W0​(3​e/4)−1\tilde{z}\_{0}=\mathrm{W}\_{0}(3e/\penalty 504)-1. Similarly, for v=1v=1, ([SB.4](https://arxiv.org/html/2512.06309v1#A2.E4a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) is equivalent to

|  |  |  |
| --- | --- | --- |
|  | 23​x1−(−x1+e1−x1)=0⟺x1​ex1=3​e5.\tfrac{2}{3}x\_{1}-\big(-x\_{1}+e^{1-x\_{1}}\big)=0\quad\Longleftrightarrow\quad x\_{1}e^{x\_{1}}=\tfrac{3e}{5}. |  |

Then, x1=W0​(3​e/5)x\_{1}=\mathrm{W}\_{0}(3e/5), and so z~1=1−W0​(3​e/5)\tilde{z}\_{1}=1-\mathrm{W}\_{0}(3e/5).
∎

Details for Example [6.2](https://arxiv.org/html/2512.06309v1#S6.Thmexample2 "Example 6.2. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"). With γ=β=0\gamma=\beta=0, we have P~0∗=p=1/3\tilde{P}^{\ast}\_{0}=p=1/3, and the limiting equilibrium strategy amounts to maximizing the limiting objective functions in ([SA.18](https://arxiv.org/html/2512.06309v1#A1.E18 "In Supplemental Appendix A Proofs in further discussions ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), with χ=1\chi=1 and χ0=0\chi\_{0}=0.
By plugging in the given expressions of λ\lambda and C0C\_{0} and by straightforward calculations, we obtain

|  |  |  |
| --- | --- | --- |
|  | J~∞0​(p;z~,0)={14,if ​z~≤−6,z~​(z~+48)144​(z~−1),if −6<z~<0,J~∞0​(p;z~,1)={z~​(96−25​z~)144​(z~+1),if ​0<z~<65,14,if ​z~≥65.\tilde{J}^{0}\_{\infty}(p;\tilde{z},0)=\begin{cases}\frac{1}{4},&\text{if }\tilde{z}\leq-6,\\ \frac{\tilde{z}(\tilde{z}+48)}{144(\tilde{z}-1)},&\text{if }-6<\tilde{z}<0,\end{cases}\quad\tilde{J}^{0}\_{\infty}(p;\tilde{z},1)=\begin{cases}\frac{\tilde{z}(96-25\tilde{z})}{144(\tilde{z}+1)},&\text{if }0<\tilde{z}<\frac{6}{5},\\ \frac{1}{4},&\text{if }\tilde{z}\geq\frac{6}{5}.\end{cases} |  |

Since z~​(z~+48)/(144​(z~−1))<1/4{\tilde{z}(\tilde{z}+48)}/{(144(\tilde{z}-1))}<1/4 for −6<z~<0-6<\tilde{z}<0 and z~​(96−25​z~)/(144​(z~+1))<1/4{\tilde{z}(96-25\tilde{z})}/{(144(\tilde{z}+1))}<1/4 for 0<z~<6/50<\tilde{z}<6/5, the continuum of (limiting) equilibrium strategies in ([6.6](https://arxiv.org/html/2512.06309v1#S6.E6 "In Example 6.2. ‣ 6 Further discussions: Criminal and mixed penalties ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) is justified.
∎

Details for calibration experiments in Section [5](https://arxiv.org/html/2512.06309v1#S5 "5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading").

Suppose that there exists z¯>0\bar{z}>0 such that D​(z)=1D(z)=1 for |z|≥z¯|z|\geq\bar{z}, meaning that as the insider increases his trade size indefinitely, the probability of prosecution conditional on investigation can reach 1. Then, using that (see, again, Abramowitz and Stegun ([1972](https://arxiv.org/html/2512.06309v1#bib.bib1)) Chap. 7)

|  |  |  |
| --- | --- | --- |
|  | erfc​x={2+e−x2​(1π​x+O​(x−2)),as ​x→−∞,e−x2​(1π​x+O​(x−2)),as ​x→∞,\mathrm{erfc}x=\begin{cases}2+e^{-x^{2}}\Big(\frac{1}{\sqrt{\pi}x}+O(x^{-2})\Big),&\;\text{as }x\to-\infty,\\ e^{-x^{2}}\Big(\frac{1}{\sqrt{\pi}x}+O(x^{-2})\Big),&\;\text{as }x\to\infty,\\ \end{cases} |  |

we further see that the hazard rate ([2.1](https://arxiv.org/html/2512.06309v1#S2.Ex2 "2.1 Prosecution mechanism ‣ 2 A Kyle model with legal risk ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) satisfies

|  |  |  |
| --- | --- | --- |
|  | λ1​(z)≡λ​(z)∼z22​σ2,as ​|z|→∞,\lambda\_{1}(z)\equiv\lambda(z)\sim\frac{z^{2}}{2\sigma^{2}},\quad\text{as }|z|\to\infty, |  |

justifying the choice of the approximation λ​(z)=K​z2\lambda(z)=Kz^{2} with K=1/(2​σ2)K=1/(2\sigma^{2}). For example, Figure [3](https://arxiv.org/html/2512.06309v1#A2.F3 "Figure 3 ‣ Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") below gives an illustration with σ=1000\sigma=1000, β=0\beta=0, y¯=3\bar{y}=3, and D​(z)=min⁡{z2,1}D(z)=\min\{z^{2},1\} (with z¯=1\bar{z}=1).

![Refer to caption](ceI0.png)
  


Figure 3: Hazard rate approximation

The formula ([5.1.2](https://arxiv.org/html/2512.06309v1#S5.E2 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) follows straight from the law of total probability:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|Z​(V)||BN​(Z​(V))=1]=𝔼​[|Z​(V)|​𝟙​(BN​(Z​(V))=1)]ℙ​{BN​(Z​(V))=1}=𝔼​[|Z​(V)|​(1−e−λN​(Z​(V)))]𝔼​[1−e−λN​(Z​(V))],\mathbb{E}\big[|Z(V)|\big|B\_{N}(Z(V))=1\big]=\frac{\mathbb{E}\big[|Z(V)|\mathds{1}(B\_{N}(Z(V))=1)\big]}{\mathbb{P}\{B\_{N}(Z(V))=1\}}=\frac{\mathbb{E}[|Z(V)|(1-e^{-\lambda\_{N}(Z(V))})]}{\mathbb{E}[1-e^{-\lambda\_{N}(Z(V))}]}, |  |

recalling that V​=d.​Bernoulli​(p)V\overset{\rm d.}{=}\text{Bernoulli}(p). Similarly, for ([5.1.3](https://arxiv.org/html/2512.06309v1#S5.E3 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([5.1.4](https://arxiv.org/html/2512.06309v1#S5.E4 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), note that XN​=d.​Normal​(N​μ,N​(σ2−μ2))X\_{N}\overset{\rm d.}{=}\text{Normal}(N\mu,N(\sigma^{2}-\mu^{2})), independent of VV, and then

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[XN+|Z​(V)||BN​(Z​(V))=1]\displaystyle\mathbb{E}\big[X\_{N}+|Z(V)|\big|B\_{N}(Z(V))=1\big] | =𝔼​[XN]+𝔼​[|Z​(V)||BN​(Z​(V))=1]\displaystyle=\mathbb{E}[X\_{N}]+\mathbb{E}\big[|Z(V)|\big|B\_{N}(Z(V))=1\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =N​μ+∑v=01p​(v)​|Z​(v)|​(1−e−λN​(Z​(v)))∑v=01p​(v)​(1−e−λN​(Z​(v))),\displaystyle=N\mu+\frac{\sum^{1}\_{v=0}p(v)|Z(v)|\big(1-e^{-\lambda\_{N}(Z(v))}\big)}{\sum^{1}\_{v=0}p(v)\big(1-e^{-\lambda\_{N}(Z(v))}\big)}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​{XN+|Z​(V)||Z​(V)|>x|BN​(Z​(V))=1}\displaystyle\mathbb{P}\bigg\{\frac{X\_{N}+|Z(V)|}{|Z(V)|}>x\Big|B\_{N}(Z(V))=1\bigg\} | =ℙ​{XN>(x−1)​|Z​(V)||BN​(Z​(V))=1}\displaystyle=\mathbb{P}\bigg\{X\_{N}>(x-1)|Z(V)|\Big|B\_{N}(Z(V))=1\bigg\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑v=01p​(v)​(1−e−λN​(Z​(v)))​12​erfc​|Z​(v)|​(x−1)−N​μ2​N​(σ2−μ2)∑v=01p​(v)​(1−e−λN​(Z​(v))).\displaystyle=\frac{\sum^{1}\_{v=0}p(v)\big(1-e^{-\lambda\_{N}(Z(v))}\big)\frac{1}{2}\mathrm{erfc}\frac{|Z(v)|(x-1)-N\mu}{\sqrt{2N(\sigma^{2}-\mu^{2})}}}{\sum^{1}\_{v=0}p(v)\big(1-e^{-\lambda\_{N}(Z(v))}\big)}. |  |

For the calibration, by writing Z=Nγ​Z~γ∗Z=N^{\gamma}\tilde{Z}^{\ast}\_{\gamma} in terms of ([5.1.5](https://arxiv.org/html/2512.06309v1#S5.E5 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and using the symmetry |Z~γ∗​(0)|=Z~γ∗​(1)>0|\tilde{Z}^{\ast}\_{\gamma}(0)|=\tilde{Z}^{\ast}\_{\gamma}(1)>0, the equations ([5.1.2](https://arxiv.org/html/2512.06309v1#S5.E2 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), ([5.1.3](https://arxiv.org/html/2512.06309v1#S5.E3 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), and ([5.1.4](https://arxiv.org/html/2512.06309v1#S5.E4 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) can be significantly simplified, permitting explicit solutions. In particular,

|  |  |  |
| --- | --- | --- |
|  | ([5.1.2](https://arxiv.org/html/2512.06309v1#S5.E2 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"))=Nγ​σ×𝔞,([5.1.3](https://arxiv.org/html/2512.06309v1#S5.E3 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"))=N​μ+Nγ​σ×𝔞,([5.1.4](https://arxiv.org/html/2512.06309v1#S5.E4 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"))=12​erfc​(Nγ​σ×𝔞)​(x−1)−N​μ2​N​(σ2−μ2).\text{(\ref{4.1.1})}=N^{\gamma}\sigma\times\mathfrak{a},\quad\text{(\ref{4.1.2})}=N\mu+N^{\gamma}\sigma\times\mathfrak{a},\quad\text{(\ref{4.1.3})}=\tfrac{1}{2}\mathrm{erfc}\tfrac{(N^{\gamma}\sigma\times\mathfrak{a})(x-1)-N\mu}{\sqrt{2N(\sigma^{2}-\mu^{2})}}. |  |

For conciseness, let us denote the average insider share volume, the average total share volume, and the median insider-to-total volume ratio from data by 𝔦\mathfrak{i}, 𝔳\mathfrak{v}, and 𝔯\mathfrak{r}, respectively, and recall that 𝔞=1−2​W0​(e​χ0/(2​χ))\mathfrak{a}=\sqrt{1-2\mathrm{W}\_{0}(\sqrt{e}\chi\_{0}/(2\chi))}, with χ0=χ−1\chi\_{0}=\chi-1.

The first calibration condition is due to ([5.1.2](https://arxiv.org/html/2512.06309v1#S5.E2 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([5.1.5](https://arxiv.org/html/2512.06309v1#S5.E5 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | Nγ​σ×𝔞=𝔦.N^{\gamma}\sigma\times\mathfrak{a}=\mathfrak{i}. |  | (SB.5) |

Similarly, from ([5.1.3](https://arxiv.org/html/2512.06309v1#S5.E3 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) we have the second calibration condition,

|  |  |  |  |
| --- | --- | --- | --- |
|  | N​μ+Nγ​σ×𝔞=𝔳.N\mu+N^{\gamma}\sigma\times\mathfrak{a}=\mathfrak{v}. |  | (SB.6) |

The third calibration condition is obtained in the same manner by evaluating ([5.1.4](https://arxiv.org/html/2512.06309v1#S5.E4 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")). In particular, since erfc−1\mathrm{erfc}-1 is an odd function, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Nγ​σ×𝔞×(𝔯−1−1)−N​μ=0.N^{\gamma}\sigma\times\mathfrak{a}\times(\mathfrak{r}^{-1}-1)-N\mu=0. |  | (SB.7) |

Notably, in calibration experiment I, the average total trading volume is associated with the standard error 10,246, respectively, as reported by Meulbroek ([1992](https://arxiv.org/html/2512.06309v1#bib.bib29)). Since there are a total of 588 insider trading episodes included in the data set, a reasonable estimate for the standard deviation of the trading volume, given independence between insider trades and normal trades, is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔰=102462×588≈248452.\mathfrak{s}=\sqrt{10246^{2}\times 588}\approx 248452. |  | (SB.8) |

Thus, the additional condition N​(σ2−μ2)=𝔰2N(\sigma^{2}-\mu^{2})=\mathfrak{s}^{2} can be used along with ([SB.5](https://arxiv.org/html/2512.06309v1#A2.E5a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([SB.6](https://arxiv.org/html/2512.06309v1#A2.E6a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) to obtain an estimate for the parameter μ>0\mu>0, namely

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ^=𝔰4+4​σ2×(𝔳−𝔦)2−𝔰22×(𝔳−𝔦),\hat{\mu}=\frac{\sqrt{\mathfrak{s}^{4}+4\sigma^{2}\times(\mathfrak{v}-\mathfrak{i})^{2}}-\mathfrak{s}^{2}}{2\times(\mathfrak{v}-\mathfrak{i})}, |  | (SB.9) |

which we simply take as μ\mu.

Taking ([SB.9](https://arxiv.org/html/2512.06309v1#A2.E9a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) as given, the preceding calibration conditions are easily solvable by elementary means. In particular, from ([SB.5](https://arxiv.org/html/2512.06309v1#A2.E5a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([SB.6](https://arxiv.org/html/2512.06309v1#A2.E6a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | N^=𝔳−𝔦μ,γ^=log⁡𝔦σ×𝔞log⁡N^;\hat{N}=\frac{\mathfrak{v}-\mathfrak{i}}{\mu},\quad\hat{\gamma}=\frac{\log\frac{\mathfrak{i}}{\sigma\times\mathfrak{a}}}{\log\hat{N}}; |  | (SB.10) |

if ([SB.7](https://arxiv.org/html/2512.06309v1#A2.E7a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) is used instead of ([SB.6](https://arxiv.org/html/2512.06309v1#A2.E6a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | N^=𝔦×(1−𝔯)μ×𝔯,γ^=log⁡𝔦σ×𝔞log⁡N^;\hat{N}=\frac{\mathfrak{i}\times(1-\mathfrak{r})}{\mu\times\mathfrak{r}},\quad\hat{\gamma}=\frac{\log\frac{\mathfrak{i}}{\sigma\times\mathfrak{a}}}{\log\hat{N}}; |  | (SB.11) |

when only ([SB.6](https://arxiv.org/html/2512.06309v1#A2.E6a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) and ([SB.7](https://arxiv.org/html/2512.06309v1#A2.E7a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) are used, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | N^=𝔳×(1−𝔯)μ,γ^=log⁡𝔳×𝔯σ×𝔞log⁡N^.\hat{N}=\frac{\mathfrak{v}\times(1-\mathfrak{r})}{\mu},\quad\hat{\gamma}=\frac{\log\frac{\mathfrak{v}\times\mathfrak{r}}{\sigma\times\mathfrak{a}}}{\log\hat{N}}. |  | (SB.12) |

According to the statistics shown in Table [1](https://arxiv.org/html/2512.06309v1#S5.T1 "Table 1 ‣ 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading"), setting 𝔦=9819\mathfrak{i}=9819, 𝔳=113909\mathfrak{v}=113909, 𝔯=0.113\mathfrak{r}=0.113, σ=1000\sigma=1000, and χ∈{1,2,3}\chi\in\{1,2,3\} and evaluating ([SB.9](https://arxiv.org/html/2512.06309v1#A2.E9a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) verifies μ=1.68625\mu=1.68625, and subsequently evaluating ([SB.9](https://arxiv.org/html/2512.06309v1#A2.E9a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), ([SB.10](https://arxiv.org/html/2512.06309v1#A2.E10a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), ([SB.11](https://arxiv.org/html/2512.06309v1#A2.E11a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), and ([SB.12](https://arxiv.org/html/2512.06309v1#A2.E12a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) gives rise to Table [2](https://arxiv.org/html/2512.06309v1#S5.T2 "Table 2 ‣ 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") for calibration experiment I.

In the same vein, for calibration experiment II, Table [5](https://arxiv.org/html/2512.06309v1#S5.T5 "Table 5 ‣ 5.2 Calibration experiment II ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") is a result of evaluating ([SB.11](https://arxiv.org/html/2512.06309v1#A2.E11a "In Supplemental Appendix B Auxiliary details ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) with 𝔦=4900\mathfrak{i}=4900, 𝔯=0.026\mathfrak{r}=0.026, μ=1.68625\mu=1.68625, σ=1000\sigma=1000, and χ∈{1,2,3}\chi\in\{1,2,3\}, based on the information in Table [4](https://arxiv.org/html/2512.06309v1#S5.T4 "Table 4 ‣ 5.2 Calibration experiment II ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading").

Moreover, the formula ([5.1.1](https://arxiv.org/html/2512.06309v1#S5.E1 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) follows directly from the law of total probability, 𝔼​[B​(Z​(V))]=𝔼​[1−e−λN​(Z​(V))]\mathbb{E}[B(Z(V))]=\mathbb{E}[1-e^{-\lambda\_{N}(Z(V))}]. Then, using that |Z~γ∗​(0)|=Z~γ∗​(1)>0|\tilde{Z}^{\ast}\_{\gamma}(0)|=\tilde{Z}^{\ast}\_{\gamma}(1)>0, the prosecution probability implied by the equilibrium is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1−e−λN​(Nγ​Z~γ∗​(1))=1−e−λ​(Z~γ∗​(1)),1-e^{-\lambda\_{N}(N^{\gamma}\tilde{Z}^{\ast}\_{\gamma}(1))}=1-e^{-\lambda(\tilde{Z}^{\ast}\_{\gamma}(1))}, |  | (SB.13) |

which upon setting γ=β\gamma=\beta becomes independent of NN and γ\gamma. Putting the solved finite-population and limiting strategy values from Table [6](https://arxiv.org/html/2512.06309v1#S5.T6 "Table 6 ‣ 5.2 Calibration experiment II ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading") into ([5.1.1](https://arxiv.org/html/2512.06309v1#S5.E1 "In 5.1 Calibration experiment I ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")) (with Z=ZN∗Z=Z^{\ast}\_{N}) and ([B.7](https://arxiv.org/html/2512.06309v1#A2.E7 "In Appendix B Proof of Theorem 4.1 ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading")), respectively, gives the last column of Table [6](https://arxiv.org/html/2512.06309v1#S5.T6 "Table 6 ‣ 5.2 Calibration experiment II ‣ 5 Empirical perspectives ‣ Wealth or Stealth? The Camouflage Effect in Insider Trading").
∎