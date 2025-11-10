---
authors:
- Hamidreza Maleki Almani
doc_id: arxiv:2511.04784v1
family_id: arxiv:2511.04784
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Insights into Tail-Based and Order Statistics
url_abs: http://arxiv.org/abs/2511.04784v1
url_html: https://arxiv.org/html/2511.04784v1
venue: arXiv q-fin
version: 1
year: 2025
---

Insights into Tail-Based and Order Statistics

![[Uncaptioned image]](IMG_7763_Final.jpg)

Hamidreza Maleki Almani

ORCID: <https://orcid.org/0000-0002-3071-4982>

Web: <https://www.uwasa.fi/en/person/2169161>

This article is an independent work by the author. He is a Postdoctoral Researcher in the Department of Mathematics and Statistics and the Department of Energy Technology at the University of Vaasa, Finland. He independently conducted and completed all aspects of this study.

November 6, 2025

Vaasa, FINLAND

Insights into Tail-Based and Order Statistics

###### Abstract.

Heavy-tailed phenomena appear across diverse domains—from wealth and firm sizes in economics to network traffic, biological systems, and physical processes—characterized by the disproportionate influence of extreme values. These distributions challenge classical statistical models, as their tails decay too slowly for conventional approximations to hold. Among their key descriptive measures are quantile contributions, which quantify the proportion of a total quantity (such as income, energy, or risk) attributed to observations above a given quantile threshold.
This paper presents a theoretical study of the quantile contribution statistic and its relationship with order statistics. We derive a closed-form expression for the joint cumulative distribution function (CDF) of order statistics and, based on it, obtain an explicit CDF for quantile contributions applicable to small samples. We then investigate the asymptotic behavior of these contributions as the sample size increases, establishing the asymptotic normality of the numerator and characterizing the limiting distribution of the quantile contribution. Finally, simulation studies illustrate the convergence properties and empirical accuracy of the theoretical results, providing a foundation for applying quantile contributions in the analysis of heavy-tailed data.

###### Key words and phrases:

Heavy-tailed distributions,
Quantile contributions,
Order statistics,
Asymptotic distribution,
Ratio distribution,
Convergence analysis,
Extreme value theory,
Empirical simulation,

###### 2020 Mathematics Subject Classification:

60E05, 62E20, 60F05, 60G15, 60G70, 62G30, 62G32, 62M10, 62P20.

## 1. Introduction

In 1906, Pareto, in his first well-known work [[46](https://arxiv.org/html/2511.04784v1#bib.bib46)], showed that approximately 80% of the land in the Kingdom of Italy was owned by only 20% of the population at that time. This became known as Pareto’s 80/20 principle.
Sturgeon’s publications in the 1950s [[55](https://arxiv.org/html/2511.04784v1#bib.bib55), [56](https://arxiv.org/html/2511.04784v1#bib.bib56), [57](https://arxiv.org/html/2511.04784v1#bib.bib57), [58](https://arxiv.org/html/2511.04784v1#bib.bib58)] highlighted the observation that the majority of everything is of low quality. However, the prevalence of low-quality content across all genres disproves the notion that any single genre is inherently inferior. This idea is now known as Sturgeon’s adage: ”Ninety percent of everything is crud!”
Computer programmers are familiar with this in another form [[10](https://arxiv.org/html/2511.04784v1#bib.bib10), [41](https://arxiv.org/html/2511.04784v1#bib.bib41)]: in computer programming and software engineering, the Ninety–Ninety Rule is a humorous aphorism that states, “The first 90% of the code accounts for the first 90% of the development time, and the remaining 10% of the code accounts for the other 90% of the development time!” This adds up to 180%, making a wry allusion to the notorious tendency of software development projects to significantly overrun their schedules.
In global health care, as a seriouse issue, the 10/90 gap is a term adopted by the Global Forum for Health Research to highlight the finding by the Commission on Health Research for Development in 1990 that less than 10% of worldwide resources devoted to health research were allocated to developing countries—where over 90% of all preventable deaths worldwide occur (see [[62](https://arxiv.org/html/2511.04784v1#bib.bib62), [22](https://arxiv.org/html/2511.04784v1#bib.bib22), [1](https://arxiv.org/html/2511.04784v1#bib.bib1)]). This disparity is a major concern of the World Health Organization (WHO) [[19](https://arxiv.org/html/2511.04784v1#bib.bib19), [20](https://arxiv.org/html/2511.04784v1#bib.bib20)].
This is observed even more sharply in internet culture [[13](https://arxiv.org/html/2511.04784v1#bib.bib13), [61](https://arxiv.org/html/2511.04784v1#bib.bib61)]. The 1% rule is a general rule of thumb regarding participation in an online community, stating that only 1% of a website’s users actively create new content, while the other 99% simply lurk.

The observations mentioned above relate to a deeper fact beyond mere statistical inference. Informally, to estimate the probability of an event, it is often sufficient to focus on the concentration region of its distribution—provided we have a large enough sample and the distribution’s tails “vanish rapidly enough.” However, this assumption does not hold if the tails are thicker than negligible. In such cases, infrequent events have a significant probability, meaning that the usual “well-behaved” statistical models fail to accurately represent them. This is when the tails of the distribution must be taken into account, leading to what are called heavy-tailed processes. The historical evolution of heavy-tailed phenomena, some of which we have mentioned, reveals the following setup:

1. ∙\bullet

   Vanishing rapidly enough means a negligible tail, typically vanishing exponentially,
2. ∙\bullet

   Well-behaved also refers to distributions with exponentially vanishing tails.

So, a distribution FF is heavy-tailed [[50](https://arxiv.org/html/2511.04784v1#bib.bib50), [28](https://arxiv.org/html/2511.04784v1#bib.bib28)] if 1−F​(x)=ℙ​[X>x]≫e−s​x1-F(x)=\mathbb{P}[X>x]\gg e^{-sx} for x→∞x\to\infty and s>0s>0, i.e.,

|  |  |  |
| --- | --- | --- |
|  | limx→∞es​x​(1−F​(x))=∞.\lim\_{x\to\infty}e^{sx}(1-F(x))\,=\,\infty. |  |

Three well-known sub-classes of the heavy-tailed distributions are

1. (i)

   Fat-tailed distributions [[44](https://arxiv.org/html/2511.04784v1#bib.bib44), [40](https://arxiv.org/html/2511.04784v1#bib.bib40)] with index 0<α<20<\alpha<2 that

   |  |  |  |
   | --- | --- | --- |
   |  | 1−F​(x)∼x−α​ for ​x→∞,1-F(x)\sim x^{-\alpha}\text{ for }x\to\infty, |  |
2. (ii)

   Long-tailed distribution [[4](https://arxiv.org/html/2511.04784v1#bib.bib4)] that for all t>0t>0 we have

   |  |  |  |
   | --- | --- | --- |
   |  | 1−F​(x+t)∼1−F​(x)​ for ​x→∞,1-F(x+t)\sim 1-F(x)\text{ for }x\to\infty, |  |
3. (iii)

   Subexponential distributions [[23](https://arxiv.org/html/2511.04784v1#bib.bib23), [14](https://arxiv.org/html/2511.04784v1#bib.bib14)] that for all independent processes X1,…,Xn∼FX\_{1},\ldots,X\_{n}\sim F we have

   |  |  |  |
   | --- | --- | --- |
   |  | ℙ​[X1+⋯+Xn>x]∼ℙ​[max⁡(X1,…,Xn)>x]​ for ​x→∞.\mathbb{P}[X\_{1}+\cdots+X\_{n}>x]\sim\mathbb{P}[\max(X\_{1},\ldots,X\_{n})>x]\text{ for }x\to\infty. |  |

Heavy-tailed distributions are crucial in numerous scientific fields due to their ability to model rare, high-impact events and skewed distributions. In economy, finance, and business, they capture extreme asset returns [[39](https://arxiv.org/html/2511.04784v1#bib.bib39), [26](https://arxiv.org/html/2511.04784v1#bib.bib26)], volatility clustering [[16](https://arxiv.org/html/2511.04784v1#bib.bib16)], and market shocks [[53](https://arxiv.org/html/2511.04784v1#bib.bib53)], enhancing risk modeling and forecasting. Wealth and firm size distributions often follow power laws, aiding economic analysis [[29](https://arxiv.org/html/2511.04784v1#bib.bib29), [5](https://arxiv.org/html/2511.04784v1#bib.bib5)]. These models also inform business strategies in sales, resource allocation, and resilience to demand shocks [[59](https://arxiv.org/html/2511.04784v1#bib.bib59), [23](https://arxiv.org/html/2511.04784v1#bib.bib23), [38](https://arxiv.org/html/2511.04784v1#bib.bib38)]. In computer science, heavy-tailed patterns appear in internet traffic [[35](https://arxiv.org/html/2511.04784v1#bib.bib35)], file sizes [[21](https://arxiv.org/html/2511.04784v1#bib.bib21)], and server loads, affecting network protocols and performance [[18](https://arxiv.org/html/2511.04784v1#bib.bib18), [47](https://arxiv.org/html/2511.04784v1#bib.bib47)]. They also underpin job scheduling in distributed systems [[31](https://arxiv.org/html/2511.04784v1#bib.bib31), [36](https://arxiv.org/html/2511.04784v1#bib.bib36)] and anomaly detection in cybersecurity [[8](https://arxiv.org/html/2511.04784v1#bib.bib8)].

In physics and engineering, heavy-tailed distributions describe anomalous diffusion [[52](https://arxiv.org/html/2511.04784v1#bib.bib52)], turbulent transport [[42](https://arxiv.org/html/2511.04784v1#bib.bib42)], and structural failure in materials [[9](https://arxiv.org/html/2511.04784v1#bib.bib9), [12](https://arxiv.org/html/2511.04784v1#bib.bib12)]. They are used in modeling impulsive noise and signal degradation in communication systems [[45](https://arxiv.org/html/2511.04784v1#bib.bib45), [43](https://arxiv.org/html/2511.04784v1#bib.bib43)], as well as robust signal processing under uncertainty.In biology and health sciences, these distributions explain superspreading in epidemics [[37](https://arxiv.org/html/2511.04784v1#bib.bib37), [24](https://arxiv.org/html/2511.04784v1#bib.bib24)], scale-free gene and protein networks [[7](https://arxiv.org/html/2511.04784v1#bib.bib7), [33](https://arxiv.org/html/2511.04784v1#bib.bib33)], and variability in neural dynamics [[11](https://arxiv.org/html/2511.04784v1#bib.bib11)]. They also capture skewed healthcare metrics such as drug response and hospital stays [[15](https://arxiv.org/html/2511.04784v1#bib.bib15)]. Across disciplines, heavy-tailed distributions support more realistic, data-driven modeling of complex systems, improving prediction, design, and decision-making.

The most important statistics of a heavy-tailed distribution are its quantiles. This is because we aim to identify a precise split of the distribution into two parts: the head and the tail. Specifically, we look for the point below which a considerable percentage pp of the population falls (the pth quantile), while the accumulated value of the remaining (1−p)(1-p) percent above that point constitutes a significant portion of the total value in the population. This measure is known as the quantile contribution [[60](https://arxiv.org/html/2511.04784v1#bib.bib60)]. It refers to the proportion of a total quantity—such as income, risk, energy, or emissions—attributed to elements above (or sometimes below) a certain quantile threshold within a statistical distribution. In simple terms, it shows how much of a total amount is accounted for by a particular subset of units ranked by size (e.g., income, energy, or emissions).
The “natural” estimator for the quantile contribution is calculated as the ratio of the sum of values above the exceedance threshold (the value above a specific quantile) to the total sum. That is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λn​(p)=∑j∈𝒥n​(p)Xj∑j=1nXj,\Lambda\_{n}(p)=\frac{\sum\_{j\in\mathscr{J}\_{n}(p)}X\_{j}}{\sum\_{j=1}^{n}X\_{j}}, |  | (1.1) |

where p∈[0,1]p\in[0,1] is a constant number, Xj,j=1,…,nX\_{j},j=1,\ldots,n are independently identically distributed (i.i.d), and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥n​(p)={j|Xj∈100​p%​largest observations among​X1,…,Xn},\mathscr{J}\_{n}(p)=\{j\,|\,X\_{j}\in 100p\%\,\text{largest observations among}\,X\_{1},\ldots,X\_{n}\}, |  | (1.2) |

we note that for all p∈[0,1],n≥1p\in[0,1],n\geq 1 we have |λn​(p)|≤1|\lambda\_{n}(p)|\leq 1.

In this article, we study the connection between quantile contributions and order statistics, focusing on their distributions and convergence. In Section [2](https://arxiv.org/html/2511.04784v1#S2 "2. Ordered and Tail-Based Statistics"), we derive a closed-form expression for the joint cumulative distribution function (CDF) of order statistics. Building on this, Section [3](https://arxiv.org/html/2511.04784v1#S3 "3. Exact Distribution of Tail-Based Statistics") presents an explicit form of the CDF for quantile contributions, applicable to a small number of variables. Section [4](https://arxiv.org/html/2511.04784v1#S4 "4. Convergence of Tail-Based Statistics") explores the convergence of quantile contributions as the number of variables grows large. Section [5](https://arxiv.org/html/2511.04784v1#S5 "5. Asymptotic Distribution of Numerator") presents the asymptotic normality of the numerator, and Section [6](https://arxiv.org/html/2511.04784v1#S6 "6. Asymptotic Distribution of Tail-Based Statistic") applies this result to characterize the asymptotic distribution of quantile contributions for a large number of variables. Finally, in Section [7](https://arxiv.org/html/2511.04784v1#S7 "7. Simulation and Callibration"), we present simulations of important cases and cumulative errors to illustrate the empirical performance and accuracy of our results.

## 2. Ordered and Tail-Based Statistics

To investigate the convergence and distribution of the Λn\Lambda\_{n} given in ([1.1](https://arxiv.org/html/2511.04784v1#S1.E1 "In 1. Introduction")), first we must consider its close relationship to the order statistics. For the random variables X1,X2,…,XnX\_{1},X\_{2},\ldots,X\_{n}, the associated order statistics are the random variables X(1)n,X(2)n,…,X(n)nX\_{(1)}^{n},X\_{(2)}^{n},\ldots,X\_{(n)}^{n} defined by ascending resorting of the X1,X2,…,XnX\_{1},X\_{2},\ldots,X\_{n}. Then we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λn​(p)=∑i=⌈n​p⌉nX(i)n∑i=1nXi=∑i=⌈n​p⌉nX(i)n∑i=1nX(i)n.\Lambda\_{n}(p)=\frac{\sum\_{i=\left\lceil np\right\rceil}^{n}X\_{(i)}^{n}}{\sum\_{i=1}^{n}X\_{i}}=\frac{\sum\_{i=\left\lceil np\right\rceil}^{n}X\_{(i)}^{n}}{\sum\_{i=1}^{n}X\_{(i)}^{n}}. |  | (2.1) |

In other word, to investigate the probability distribution of Λn\Lambda\_{n}, it is sufficient to know the joint distribution of the order statistics X(1)n,X(2)n,…,X(n)nX\_{(1)}^{n},X\_{(2)}^{n},\ldots,X\_{(n)}^{n}.
The following proposition for the distribution of each X(i)nX\_{(i)}^{n} is explained in [[17](https://arxiv.org/html/2511.04784v1#bib.bib17), [49](https://arxiv.org/html/2511.04784v1#bib.bib49), [3](https://arxiv.org/html/2511.04784v1#bib.bib3)]. Here I just rewrite the proof with a quantitative formulation of its combinatorics.

###### Proposition 2.1.

The probability distribution F(i)nF\_{(i)}^{n} and density function f(i)nf\_{(i)}^{n} of the order statistic X(i)nX\_{(i)}^{n} are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | F(i)n​(x)\displaystyle F\_{(i)}^{n}(x) | =I​(F​(x);i,n−i+1)=∑J=in(nJ)​(F​(x))J​(1−F​(x))n−J,\displaystyle=I\big(F(x);\,i,n-i+1\big)=\sum\_{J=i}^{n}\binom{n}{J}\Big(F(x)\Big)^{J}\Big(1-F(x)\Big)^{n-J}, |  | (2.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f(i)n​(x)\displaystyle f\_{(i)}^{n}(x) | =f​(x)B​(i,n−i+1)​(F​(x))i−1​(1−F​(x))n−i,\displaystyle=\frac{f(x)}{B(i,n-i+1)}\Big(F(x)\Big)^{i-1}\Big(1-F(x)\Big)^{n-i}, |  | (2.3) |

where FF and ff are respectively the probability distribution and density function of the variable X1X\_{1}, and B,IB,I are respectively the beta function and the regularized inclomplete beta function, i.e., for all ℜ​𝔢​(p),ℜ​𝔢​(q)>0\mathfrak{Re}(p),\mathfrak{Re}(q)>0

|  |  |  |
| --- | --- | --- |
|  | B​(p,q)=∫01tp−1​(1−t)q−1​𝑑t,\displaystyle B(p,q)=\int\_{0}^{1}t^{p-1}(1-t)^{q-1}\,dt, |  |
|  |  |  |
| --- | --- | --- |
|  | I​(x;p,q)=1B​(p,q)​∫0xtp−1​(1−t)q−1​𝑑t.\displaystyle I(x;\,p,q)=\frac{1}{B(p,q)}\int\_{0}^{x}t^{p-1}(1-t)^{q-1}\,dt. |  |

###### Proof.

As X(i)nX\_{(i)}^{n} is the (i/n)(i/n)-quantile variable of X1,…,XnX\_{1},\ldots,X\_{n}, for all x∈ℝx\in\mathbb{R}

|  |  |  |
| --- | --- | --- |
|  | X(i)n=Qn​(i/n)≤x⇔i≤∑j=1n𝟙(−∞,x]​(Xj).X\_{(i)}^{n}=Q\_{n}(i/n)\leq x\iff i\leq\sum\_{j=1}^{n}\mathds{1}\_{(-\infty,x]}(X\_{j}). |  |

So,

|  |  |  |  |
| --- | --- | --- | --- |
|  | F(j)n​(x)\displaystyle F\_{(j)}^{n}(x) | =ℙ​[X(i)n≤x]\displaystyle=\mathbb{P}[X\_{(i)}^{n}\leq x] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙ​[i≤∑j=1n𝟙(−∞,x]​(Xj)]\displaystyle=\mathbb{P}\left[i\leq\sum\_{j=1}^{n}\mathds{1}\_{(-\infty,x]}(X\_{j})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑J=inℙ​[J=∑j=1n𝟙(−∞,x]​(Xj)]\displaystyle=\sum\_{J=i}^{n}\mathbb{P}\left[J=\sum\_{j=1}^{n}\mathds{1}\_{(-\infty,x]}(X\_{j})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑J=in(nJ)​(ℙ​[X1≤x])J​(ℙ​[X1>x])n−J\displaystyle=\sum\_{J=i}^{n}\binom{n}{J}\Big(\mathbb{P}[X\_{1}\leq x]\Big)^{J}\Big(\mathbb{P}[X\_{1}>x]\Big)^{n-J} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑J=in(nJ)​(F​(x))J​(1−F​(x))n−J.\displaystyle=\sum\_{J=i}^{n}\binom{n}{J}\Big(F(x)\Big)^{J}\Big(1-F(x)\Big)^{n-J}. |  |

Now, we note

|  |  |  |
| --- | --- | --- |
|  | ∑J=in(nJ)​yJ​(1−y)n−J\displaystyle\sum\_{J=i}^{n}\binom{n}{J}y^{J}(1-y)^{n-J} |  |
|  |  |  |
| --- | --- | --- |
|  | =∫0yti​(1−t)n−i+1​𝑑tB​(i,n−i+1)\displaystyle=\frac{\displaystyle\int\_{0}^{y}t^{i}(1-t)^{n-i+1}\,dt}{B(i,n-i+1)} |  |
|  |  |  |
| --- | --- | --- |
|  | =I​(y;i,n−i+1),\displaystyle=I\big(y;\,i,n-i+1\big), |  |

and these prove ([2.2](https://arxiv.org/html/2511.04784v1#S2.E2 "In Proposition 2.1. ‣ 2. Ordered and Tail-Based Statistics")). The proof of ([2.3](https://arxiv.org/html/2511.04784v1#S2.E3 "In Proposition 2.1. ‣ 2. Ordered and Tail-Based Statistics")) is straight forward as follows.

|  |  |  |  |
| --- | --- | --- | --- |
|  | f(j)n​(x)\displaystyle f\_{(j)}^{n}(x) | =d​F(j)n​(x)d​x\displaystyle=\frac{dF\_{(j)}^{n}(x)}{dx} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =d​I​(F​(x);i,n−i+1)d​x\displaystyle=\frac{dI\big(F(x);\,i,n-i+1\big)}{dx} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =f​(x)​(F​(x))i−1​(1−F​(x))n−iB​(i,n−i+1).\displaystyle=\frac{f(x)\big(F(x)\big)^{i-1}\big(1-F(x)\big)^{n-i}}{B(i,n-i+1)}. |  |

∎

The joint density function of the order statistics X(1)n,X(2)n,…,X(n)nX\_{(1)}^{n},X\_{(2)}^{n},\ldots,X\_{(n)}^{n} is given by [[49](https://arxiv.org/html/2511.04784v1#bib.bib49), [2](https://arxiv.org/html/2511.04784v1#bib.bib2)] as following theorem and corollary.

###### Theorem 2.2.

Let 1≤k≤n1\leq k\leq n and 0=r0<r1<⋯<rk<rk+1=n+10=r\_{0}<r\_{1}<\cdots<r\_{k}<r\_{k+1}=n+1. If the random variables X1,X2,…,XnX\_{1},X\_{2},\ldots,X\_{n} are i.i.d with common absolutely continuous distribution FF and density function ff, then the joint density function of X(r1)n,X(r2)n,…,X(rk)nX\_{(r\_{1})}^{n},X\_{(r\_{2})}^{n},\ldots,X\_{(r\_{k})}^{n} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | f(r1,…,rk)n​(x1,…,xk)=n!​(∏i=1kf​(xi))​∏i=1k+1(F​(xi)−F​(xi−1))ri−ri−1−1(ri−ri−1−1)!,f\_{(r\_{1},\ldots,r\_{k})}^{n}(x\_{1},\ldots,x\_{k})=n!\left(\prod\_{i=1}^{k}f(x\_{i})\right)\prod\_{i=1}^{k+1}\frac{\big(F(x\_{i})-F(x\_{i-1})\big)^{r\_{i}-r\_{i-1}-1}}{(r\_{i}-r\_{i-1}-1)!}, |  | (2.4) |

if x1<x2<⋯<xkx\_{1}<x\_{2}<\cdots<x\_{k}, and it is 0 otherwise. Here F​(x0)=0F(x\_{0})=0 and F​(xk+1)=1F(x\_{k+1})=1.

###### Corollary 2.3.

If the random variables X1,X2,…,XnX\_{1},X\_{2},\ldots,X\_{n} are i.i.d with common absolutely continuous distribution FF and density function ff, then the joint density function of X(1)n,X(2)n,…,X(n)nX\_{(1)}^{n},X\_{(2)}^{n},\ldots,X\_{(n)}^{n} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | f(1,…,n)n​(x1,…,xn)=n!​∏i=1nf​(xi),f\_{(1,\ldots,n)}^{n}(x\_{1},\ldots,x\_{n})=n!\prod\_{i=1}^{n}f(x\_{i}), |  | (2.5) |

if x1<x2<⋯<xnx\_{1}<x\_{2}<\cdots<x\_{n}, and it is 0 otherwise.

Next, we evaluate the cumulative distribution function of the order statistics. However, this requires some insight into the relationship between the Binomial distribution and the regularized incomplete Beta function, as presented in the following lemma.

###### Lemma 2.4.

For all positive integers p,q≥1p,q\geq 1, and all a,b∈ℝa,b\in\mathbb{R}

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ia,b​(y;p,q)\displaystyle I\_{a,b}(y;\,p,q) | :=1B​(p,q)​∫ay(x−a)p−1​(b−x)q−1​𝑑x\displaystyle:=\frac{1}{B(p,q)}\int\_{a}^{y}(x-a)^{p-1}(b-x)^{q-1}\,dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑j=pp+q−1(p+q−1j)​(y−a)j​(b−y)p+q−1−j\displaystyle=\sum\_{j=p}^{p+q-1}\binom{p+q-1}{j}(y-a)^{j}(b-y)^{p+q-1-j} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑j=0q−1(p+q−1j)​(y−a)p+q−1−j​(b−y)j.\displaystyle=\sum\_{j=0}^{q-1}\binom{p+q-1}{j}(y-a)^{p+q-1-j}(b-y)^{j}. |  |

###### Proof.

By changing the variable t=x−ab−at=\frac{x-a}{b-a}, we have

|  |  |  |
| --- | --- | --- |
|  | Ia,b​(y;p,q)=(b−a)p+q−1​I​(y−ab−a;p,q),I\_{a,b}(y;p,q)=(b-a)^{p+q-1}I\left(\frac{y-a}{b-a};p,q\right), |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(u;p,q)\displaystyle I\left(u;p,q\right) | =ℙ​[J≥p]\displaystyle=\mathbb{P}[J\geq p] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑j=pp+q−1(p+q−1j)​uj​(1−u)p+q−1−j\displaystyle=\sum\_{j=p}^{p+q-1}\binom{p+q-1}{j}u^{j}(1-u)^{p+q-1-j} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑j=0q−1(p+q−1j)​up+q−1−j​(1−u)j,\displaystyle=\sum\_{j=0}^{q-1}\binom{p+q-1}{j}u^{p+q-1-j}(1-u)^{j}, |  |

where J∼ℬ​i​n​o​m​i​a​l​(u;p+q−1)J\sim\mathscr{B}inomial(u;p+q-1). Now, substituting u=y−ab−au=\frac{y-a}{b-a} proves the claim.
∎

###### Theorem 2.5.

Let 1≤k≤n1\leq k\leq n and 0<r1<⋯<rk<n+10<r\_{1}<\cdots<r\_{k}<n+1 are integers. If the random variables X1,X2,…,XnX\_{1},X\_{2},\ldots,X\_{n} are i.i.d with common absolutely continuous distribution FF and density function ff, then the cumulative distribution function of X(r1)n,X(r2)n,…,X(rk)nX\_{(r\_{1})}^{n},X\_{(r\_{2})}^{n},\ldots,X\_{(r\_{k})}^{n} is

|  |  |  |
| --- | --- | --- |
|  | F(r1,…,rk)n​(x1,…,xk)\displaystyle F\_{(r\_{1},\ldots,r\_{k})}^{n}(x\_{1},\ldots,x\_{k}) |  |
|  |  |  |
| --- | --- | --- |
|  | =∑Jk=0n−rk∑Jk−1=0n−rk−1−Jk∑Jk−2=0n−rk−2−Jk−Jk−1⋯​∑J1=0n−r1−∑i=2kJi\displaystyle=\sum\_{J\_{k}=0}^{n-r\_{k}}\quad\sum\_{J\_{k-1}=0}^{n-r\_{k-1}-J\_{k}}\quad\sum\_{J\_{k-2}=0}^{n-r\_{k-2}-J\_{k}-J\_{k-1}}\cdots\sum\_{J\_{1}=0}^{n-r\_{1}-\sum\_{i=2}^{k}J\_{i}} |  |
|  |  |  |
| --- | --- | --- |
|  | (nJ0,J1,…,Jk)​∏i=0k(F​(x(i+1)k)−F​(x(i)k))Ji,\displaystyle\quad\binom{n}{J\_{0},J\_{1},\ldots,J\_{k}}\prod\_{i=0}^{k}\Big(F\left(x\_{(i+1)}^{k}\right)-F\left(x\_{(i)}^{k}\right)\Big)^{J\_{i}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t.∑i=0kJi=n,\displaystyle s.t.\quad\sum\_{i=0}^{k}J\_{i}=n, |  | (2.6) |

if x1<x2<⋯<xkx\_{1}<x\_{2}<\cdots<x\_{k}, and it is 0 otherwise. Here F​(x0)=0F(x\_{0})=0, and F​(xk+1)=1F(x\_{k+1})=1. (Note: J0=n−∑i=1kJiJ\_{0}=n-\sum\_{i=1}^{k}J\_{i})

###### Proof 1: Calculus.

Applying the density function from Theorem [2.2](https://arxiv.org/html/2511.04784v1#S2.Thmdfn2 "Theorem 2.2. ‣ 2. Ordered and Tail-Based Statistics"), for y1≤⋯≤yky\_{1}\leq\cdots\leq y\_{k} we have

|  |  |  |
| --- | --- | --- |
|  | F(r1,…,rk)n​(y1,…,yk)\displaystyle F\_{(r\_{1},\ldots,r\_{k})}^{n}(y\_{1},\ldots,y\_{k}) |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​∫−∞y1∫x1y2⋯​∫xk−2yk−1∫xk−1yk𝑑xk​⋯​𝑑x1\displaystyle=n!\int\_{-\infty}^{y\_{1}}\int\_{x\_{1}}^{y\_{2}}\cdots\int\_{x\_{k-2}}^{y\_{k-1}}\int\_{x\_{k-1}}^{y\_{k}}dx\_{k}\cdots dx\_{1} |  |
|  |  |  |
| --- | --- | --- |
|  | ×(∏i=1kf​(xi))​∏i=1k+1(F​(xi)−F​(xi−1))ri−ri−1−1(ri−ri−1−1)!,\displaystyle\quad\times\left(\prod\_{i=1}^{k}f(x\_{i})\right)\prod\_{i=1}^{k+1}\frac{\big(F(x\_{i})-F(x\_{i-1})\big)^{r\_{i}-r\_{i-1}-1}}{(r\_{i}-r\_{i-1}-1)!}, |  |

where r0=0r\_{0}=0 and rk+1=n+1r\_{k+1}=n+1. By changing the variables ui=F​(xi),i=1,…​k+1u\_{i}=F(x\_{i}),\,i=1,\ldots k+1, we have

|  |  |  |
| --- | --- | --- |
|  | =n!​∫0F​(y1)∫u1F​(y2)⋯​∫uk−2F​(yk−1)∫uk−1F​(yk)∏i=1k+1(ui−ui−1)ri−ri−1−1(ri−ri−1−1)!​d​uk​⋯​d​u1\displaystyle=n!\int\_{0}^{F(y\_{1})}\int\_{u\_{1}}^{F(y\_{2})}\cdots\int\_{u\_{k-2}}^{F(y\_{k-1})}\int\_{u\_{k-1}}^{F(y\_{k})}\prod\_{i=1}^{k+1}\frac{(u\_{i}-u\_{i-1})^{r\_{i}-r\_{i-1}-1}}{(r\_{i}-r\_{i-1}-1)!}\,du\_{k}\cdots du\_{1} |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​∫0F​(y1)∫u1F​(y2)⋯​∫uk−2F​(yk−1)∏i=1k−1(ui−ui−1)ri−ri−1−1(ri−ri−1−1)!​d​uk−1​⋯​d​u1⏟πk−1\displaystyle=n!\underbrace{\int\_{0}^{F(y\_{1})}\int\_{u\_{1}}^{F(y\_{2})}\cdots\int\_{u\_{k-2}}^{F(y\_{k-1})}\prod\_{i=1}^{k-1}\frac{(u\_{i}-u\_{i-1})^{r\_{i}-r\_{i-1}-1}}{(r\_{i}-r\_{i-1}-1)!}\,du\_{k-1}\cdots du\_{1}}\_{\pi\_{k-1}} |  |
|  |  |  |
| --- | --- | --- |
|  | ×∫uk−1F​(yk)(uk+1−uk)rk+1−rk−1​(uk−uk−1)rk−rk−1−1(rk+1−rk−1)!​(rk−rk−1−1)!duk\displaystyle\quad\times\int\_{u\_{k-1}}^{F(y\_{k})}\frac{(u\_{k+1}-u\_{k})^{r\_{k+1}-r\_{k}-1}(u\_{k}-u\_{k-1})^{r\_{k}-r\_{k-1}-1}}{(r\_{k+1}-r\_{k}-1)!(r\_{k}-r\_{k-1}-1)!}\,du\_{k} |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​πk−1​∫uk−1F​(yk)(uk+1−uk)rk+1−rk−1​(uk−uk−1)rk−rk−1−1B​(rk+1−rk,rk−rk−1−1)​(rk+1−rk−1−1)!​𝑑uk.\displaystyle=n!\,\pi\_{k-1}\int\_{u\_{k-1}}^{F(y\_{k})}\frac{(u\_{k+1}-u\_{k})^{r\_{k+1}-r\_{k}-1}(u\_{k}-u\_{k-1})^{r\_{k}-r\_{k-1}-1}}{B(r\_{k+1}-r\_{k},r\_{k}-r\_{k-1}-1)(r\_{k+1}-r\_{k-1}-1)!}\,du\_{k}. |  |

Taking pk=rk−rk−1,qk=rk+1−rkp\_{k}=r\_{k}-r\_{k-1},q\_{k}=r\_{k+1}-r\_{k}, then by Lemma [2.4](https://arxiv.org/html/2511.04784v1#S2.Thmdfn4 "Lemma 2.4. ‣ 2. Ordered and Tail-Based Statistics")

|  |  |  |
| --- | --- | --- |
|  | =n!​πk−1(rk+1−rk−1−1)!​Iuk−1,uk+1​(F​(yk);rk−rk−1,rk+1−rk)\displaystyle=\frac{n!\,\pi\_{k-1}}{(r\_{k+1}-r\_{k-1}-1)!}\,I\_{u\_{k-1},u\_{k+1}}\Big(F(y\_{k});r\_{k}-r\_{k-1},r\_{k+1}-r\_{k}\Big) |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​πk−1(rk+1−rk−1−1)!​Iuk−1,uk+1​(F​(yk);pk,qk)\displaystyle=\frac{n!\,\pi\_{k-1}}{(r\_{k+1}-r\_{k-1}-1)!}\,I\_{u\_{k-1},u\_{k+1}}\big(F(y\_{k});p\_{k},q\_{k}\big) |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​πk−1(rk+1−rk−1−1)!\displaystyle=\frac{n!\,\pi\_{k-1}}{(r\_{k+1}-r\_{k-1}-1)!} |  |
|  |  |  |
| --- | --- | --- |
|  | ×∑Jk=0qk−1(pk+qk−1Jk)(F(yk)−uk−1)pk+qk−1−Jk(uk+1−F(yk))Jk\displaystyle\times\sum\_{J\_{k}=0}^{q\_{k}-1}\binom{p\_{k}+q\_{k}-1}{J\_{k}}\big(F(y\_{k})-u\_{k-1}\big)^{p\_{k}+q\_{k}-1-J\_{k}}\big(u\_{k+1}-F(y\_{k})\big)^{J\_{k}} |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​πk−1(rk+1−rk−1−1)!\displaystyle=\frac{n!\,\pi\_{k-1}}{(r\_{k+1}-r\_{k-1}-1)!} |  |
|  |  |  |
| --- | --- | --- |
|  | ×∑Jk=0rk+1−rk−1(rk+1−rk−1−1Jk)(F(yk)−uk−1)rk+1−rk−1−1−Jk(uk+1−F(yk))Jk\displaystyle\times\sum\_{J\_{k}=0}^{r\_{k+1}-r\_{k}-1}\binom{r\_{k+1}-r\_{k-1}-1}{J\_{k}}\big(F(y\_{k})-u\_{k-1}\big)^{r\_{k+1}-r\_{k-1}-1-J\_{k}}\big(u\_{k+1}-F(y\_{k})\big)^{J\_{k}} |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​πk−2​∑Jk=0rk+1−rk−1(uk+1−F​(yk))JkJk!⏟ΣJk\displaystyle=n!\,\pi\_{k-2}\underbrace{\sum\_{J\_{k}=0}^{r\_{k+1}-r\_{k}-1}\frac{\big(u\_{k+1}-F(y\_{k})\big)^{J\_{k}}}{J\_{k}!}}\_{\Sigma\_{J\_{k}}} |  |
|  |  |  |
| --- | --- | --- |
|  | ×∫uk−2F​(yk−1)(uk−1−uk−2)rk−1−rk−2−1(rk−1−rk−2−1)!⋅(F​(yk)−uk−1)rk+1−rk−1−1−Jk(rk+1−rk−1−1−Jk)!duk−1\displaystyle\times\int\_{u\_{k-2}}^{F(y\_{k-1})}\frac{(u\_{k-1}-u\_{k-2})^{r\_{k-1}-r\_{k-2}-1}}{(r\_{k-1}-r\_{k-2}-1)!}\cdot\frac{(F(y\_{k})-u\_{k-1})^{r\_{k+1}-r\_{k-1}-1-J\_{k}}}{(r\_{k+1}-r\_{k-1}-1-J\_{k})!}\,du\_{k-1} |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​πk−2​ΣJk\displaystyle=n!\,\pi\_{k-2}\Sigma\_{J\_{k}} |  |
|  |  |  |
| --- | --- | --- |
|  | ×∫uk−2F​(yk−1)(uk−1−uk−2)rk−1−rk−2−1⋅(F​(yk)−uk−1)rk+1−rk−1−1−JkB​(rk−1−rk−2,rk+1−rk−1−Jk)​Γ​(rk+1−rk−2−Jk)duk−1.\displaystyle\times\int\_{u\_{k-2}}^{F(y\_{k-1})}\frac{(u\_{k-1}-u\_{k-2})^{r\_{k-1}-r\_{k-2}-1}\cdot(F(y\_{k})-u\_{k-1})^{r\_{k+1}-r\_{k-1}-1-J\_{k}}}{B(r\_{k-1}-r\_{k-2},r\_{k+1}-r\_{k-1}-J\_{k})\Gamma(r\_{k+1}-r\_{k-2}-J\_{k})}\,du\_{k-1}. |  |

Again, by taking pk−1=rk−1−rk−2,qk−1=rk+1−rk−1−Jkp\_{k-1}=r\_{k-1}-r\_{k-2},\,q\_{k-1}=r\_{k+1}-r\_{k-1}-J\_{k}, then from Lemma [2.4](https://arxiv.org/html/2511.04784v1#S2.Thmdfn4 "Lemma 2.4. ‣ 2. Ordered and Tail-Based Statistics")

|  |  |  |
| --- | --- | --- |
|  | =n!​πk−2​ΣJk(rk+1−rk−2−Jk−1)!​Iuk−2,F​(yk)​(F​(yk−1);pk−1,qk−1)\displaystyle=\frac{n!\,\pi\_{k-2}\Sigma\_{J\_{k}}}{(r\_{k+1}-r\_{k-2}-J\_{k}-1)!}\,I\_{u\_{k-2},F(y\_{k})}\Big(F(y\_{k-1});p\_{k-1},q\_{k-1}\Big) |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​πk−2​ΣJk(rk+1−rk−2−Jk−1)!​∑Jk−1=0qk−1−1(pk−1+qk−1−1Jk−1)\displaystyle=\frac{n!\,\pi\_{k-2}\Sigma\_{J\_{k}}}{(r\_{k+1}-r\_{k-2}-J\_{k}-1)!}\sum\_{J\_{k-1}=0}^{q\_{k-1}-1}\binom{p\_{k-1}+q\_{k-1}-1}{J\_{k-1}} |  |
|  |  |  |
| --- | --- | --- |
|  | ×(F​(yk−1)−uk−2)pk−1+qk−1−1−Jk−1​(uk−F​(yk−1))Jk−1\displaystyle\times\big(F(y\_{k-1})-u\_{k-2}\big)^{p\_{k-1}+q\_{k-1}-1-J\_{k-1}}\big(u\_{k}-F(y\_{k-1})\big)^{J\_{k-1}} |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​πk−2​ΣJk(rk+1−rk−2−Jk−1)!​∑Jk−1=0rk+1−rk−1−Jk−1(rk+1−rk−2−Jk−1Jk−1)\displaystyle=\frac{n!\,\pi\_{k-2}\Sigma\_{J\_{k}}}{(r\_{k+1}-r\_{k-2}-J\_{k}-1)!}\sum\_{J\_{k-1}=0}^{r\_{k+1}-r\_{k-1}-J\_{k}-1}\binom{r\_{k+1}-r\_{k-2}-J\_{k}-1}{J\_{k-1}} |  |
|  |  |  |
| --- | --- | --- |
|  | ×(F​(yk−1)−uk−2)rk+1−rk−2−Jk−Jk−1−1​(uk−F​(yk−1))Jk−1\displaystyle\times\big(F(y\_{k-1})-u\_{k-2}\big)^{r\_{k+1}-r\_{k-2}-J\_{k}-J\_{k-1}-1}\big(u\_{k}-F(y\_{k-1})\big)^{J\_{k-1}} |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​πk−3​ΣJk​∑Jk−1=0rk+1−rk−1−Jk−1(F​(yk)−F​(yk−1))Jk−1Jk−1!⏟ΣJk−1\displaystyle=n!\,\pi\_{k-3}\Sigma\_{J\_{k}}\underbrace{\sum\_{J\_{k-1}=0}^{r\_{k+1}-r\_{k-1}-J\_{k}-1}\frac{\big(F(y\_{k})-F(y\_{k-1})\big)^{J\_{k-1}}}{J\_{k-1}!}}\_{\Sigma\_{J\_{k-1}}} |  |
|  |  |  |
| --- | --- | --- |
|  | ×∫uk−3F​(yk−2)(uk−2−uk−3)rk−2−rk−3−1(rk−2−rk−3−1)!\displaystyle\hskip 56.9055pt\times\int\_{u\_{k-3}}^{F(y\_{k-2})}\frac{(u\_{k-2}-u\_{k-3})^{r\_{k-2}-r\_{k-3}-1}}{(r\_{k-2}-r\_{k-3}-1)!} |  |
|  |  |  |
| --- | --- | --- |
|  | ⋅(F​(yk−1)−uk−2)rk+1−rk−2−Jk−Jk−1−1(rk+1−rk−2−Jk−Jk−1−1)!​d​uk−2\displaystyle\hskip 56.9055pt\cdot\frac{(F(y\_{k-1})-u\_{k-2})^{r\_{k+1}-r\_{k-2}-J\_{k}-J\_{k-1}-1}}{(r\_{k+1}-r\_{k-2}-J\_{k}-J\_{k-1}-1)!}\,du\_{k-2} |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​πk−3​ΣJk​ΣJk−1​∫uk−3F​(yk−2)(uk−2−uk−3)rk−2−rk−3−1Γ​(rk+1−rk−3−Jk−Jk−1)\displaystyle=n!\,\pi\_{k-3}\Sigma\_{J\_{k}}\Sigma\_{J\_{k-1}}\int\_{u\_{k-3}}^{F(y\_{k-2})}\frac{(u\_{k-2}-u\_{k-3})^{r\_{k-2}-r\_{k-3}-1}}{\Gamma(r\_{k+1}-r\_{k-3}-J\_{k}-J\_{k-1})} |  |
|  |  |  |
| --- | --- | --- |
|  | ×(F​(yk−1)−uk−2)rk+1−rk−2−Jk−Jk−1−1B​(rk−2−rk−3,rk+1−rk−2−Jk−Jk−1)​d​uk−2,\displaystyle\hskip 85.35826pt\times\frac{(F(y\_{k-1})-u\_{k-2})^{r\_{k+1}-r\_{k-2}-J\_{k}-J\_{k-1}-1}}{B(r\_{k-2}-r\_{k-3},r\_{k+1}-r\_{k-2}-J\_{k}-J\_{k-1})}\,du\_{k-2}, |  |

To identify the limits of the summations, we proceed one step further, and again by taking pk−2=rk−2−rk−3,qk−2=rk+1−rk−2−Jk−Jk−1p\_{k-2}=r\_{k-2}-r\_{k-3},\,q\_{k-2}=r\_{k+1}-r\_{k-2}-J\_{k}-J\_{k-1}, from Lemma [2.4](https://arxiv.org/html/2511.04784v1#S2.Thmdfn4 "Lemma 2.4. ‣ 2. Ordered and Tail-Based Statistics"), we have

|  |  |  |
| --- | --- | --- |
|  | =n!​πk−3​ΣJk​ΣJk−1(rk+1−rk−3−Jk−Jk+1−1)!​Iuk−3,F​(yk−1)​(F​(yk−2);pk−2,qk−2)\displaystyle=\frac{n!\,\pi\_{k-3}\Sigma\_{J\_{k}}\Sigma\_{J\_{k-1}}}{(r\_{k+1}-r\_{k-3}-J\_{k}-J\_{k+1}-1)!}\,I\_{u\_{k-3},F(y\_{k-1})}\Big(F(y\_{k-2});p\_{k-2},q\_{k-2}\Big) |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​πk−3​ΣJk​ΣJk−1(rk+1−rk−3−Jk−Jk−1−1)!​∑Jk−2=0qk−2−1(pk−2+qk−2−1Jk−2)\displaystyle=\frac{n!\,\pi\_{k-3}\Sigma\_{J\_{k}}\Sigma\_{J\_{k-1}}}{(r\_{k+1}-r\_{k-3}-J\_{k}-J\_{k-1}-1)!}\sum\_{J\_{k-2}=0}^{q\_{k-2}-1}\binom{p\_{k-2}+q\_{k-2}-1}{J\_{k-2}} |  |
|  |  |  |
| --- | --- | --- |
|  | ×(F​(yk−2)−uk−3)pk−2+qk−2−1−Jk−2​(uk−F​(yk−1))Jk−2\displaystyle\times\big(F(y\_{k-2})-u\_{k-3}\big)^{p\_{k-2}+q\_{k-2}-1-J\_{k-2}}\big(u\_{k}-F(y\_{k-1})\big)^{J\_{k-2}} |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​πk−3​ΣJk​ΣJk−1(rk+1−rk−3−Jk−Jk−1−1)!\displaystyle=\frac{n!\,\pi\_{k-3}\Sigma\_{J\_{k}}\Sigma\_{J\_{k-1}}}{(r\_{k+1}-r\_{k-3}-J\_{k}-J\_{k-1}-1)!} |  |
|  |  |  |
| --- | --- | --- |
|  | ×∑Jk−2=0rk+1−rk−2−Jk−Jk−1−1(rk+1−rk−3−Jk−Jk−1−1Jk−2)\displaystyle\times\sum\_{J\_{k-2}=0}^{r\_{k+1}-r\_{k-2}-J\_{k}-J\_{k-1}-1}\binom{r\_{k+1}-r\_{k-3}-J\_{k}-J\_{k-1}-1}{J\_{k-2}} |  |
|  |  |  |
| --- | --- | --- |
|  | ×(F(yk−2)−uk−3)rk+1−rk−3−Jk−Jk−1−Jk−2−1(F(yk−1−F(yk−1))Jk−2\displaystyle\times\big(F(y\_{k-2})-u\_{k-3}\big)^{r\_{k+1}-r\_{k-3}-J\_{k}-J\_{k-1}-J\_{k-2}-1}\big(F(y\_{k-1}-F(y\_{k-1})\big)^{J\_{k-2}} |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​πk−4​ΣJk​ΣJk−1​∑Jk−2=0rk+1−rk−2−Jk−Jk−1−1(F​(yk−1)−F​(yk−2))Jk−2Jk−2!⏟ΣJk−2\displaystyle=n!\,\pi\_{k-4}\Sigma\_{J\_{k}}\Sigma\_{J\_{k-1}}\underbrace{\sum\_{J\_{k-2}=0}^{r\_{k+1}-r\_{k-2}-J\_{k}-J\_{k-1}-1}\frac{\big(F(y\_{k-1})-F(y\_{k-2})\big)^{J\_{k-2}}}{J\_{k-2}!}}\_{\Sigma\_{J\_{k-2}}} |  |
|  |  |  |
| --- | --- | --- |
|  | ×∫uk−4F​(yk−3)(uk−3−uk−4)rk−3−rk−4−1(rk−3−rk−4−1)!\displaystyle\hskip 85.35826pt\times\int\_{u\_{k-4}}^{F(y\_{k-3})}\frac{(u\_{k-3}-u\_{k-4})^{r\_{k-3}-r\_{k-4}-1}}{(r\_{k-3}-r\_{k-4}-1)!} |  |
|  |  |  |
| --- | --- | --- |
|  | ⋅(F​(yk−2)−uk−3)rk+1−rk−3−Jk−Jk−1−Jk−2−1(rk+1−rk−3−Jk−Jk−1−Jk−2−1)!​d​uk−3.\displaystyle\hskip 85.35826pt\cdot\frac{(F(y\_{k-2})-u\_{k-3})^{r\_{k+1}-r\_{k-3}-J\_{k}-J\_{k-1}-J\_{k-2}-1}}{(r\_{k+1}-r\_{k-3}-J\_{k}-J\_{k-1}-J\_{k-2}-1)!}\,du\_{k-3}. |  |

Continuing this calculation recursively, we obtain

|  |  |  |
| --- | --- | --- |
|  | =n!​ΣJk​⋯​ΣJ2​∫u0F​(y1)(u1−u0)r1−r0−1(r1−r0−1)!⋅(F​(y2)−u1)rk+1−r1−1−∑i=2kJi(rk+1−r1−1−∑i=2kJi)!​𝑑u1\displaystyle=n!\Sigma\_{J\_{k}}\cdots\Sigma\_{J\_{2}}\int\_{u\_{0}}^{F(y\_{1})}\frac{(u\_{1}-u\_{0})^{r\_{1}-r\_{0}-1}}{(r\_{1}-r\_{0}-1)!}\cdot\frac{(F(y\_{2})-u\_{1})^{r\_{k+1}-r\_{1}-1-\sum\_{i=2}^{k}J\_{i}}}{(r\_{k+1}-r\_{1}-1-\sum\_{i=2}^{k}J\_{i})!}\,du\_{1} |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​ΣJk​⋯​ΣJ2​∫0F​(y1)u1r1−1​(F​(y2)−u1)rk+1−r1−1−∑i=2kJiB​(r1,rk+1−r1−∑j=2kJi)​(rk+1−1−∑i=2kJi)!​𝑑u1.\displaystyle=n!\Sigma\_{J\_{k}}\cdots\Sigma\_{J\_{2}}\int\_{0}^{F(y\_{1})}\frac{u\_{1}^{r\_{1}-1}(F(y\_{2})-u\_{1})^{r\_{k+1}-r\_{1}-1-\sum\_{i=2}^{k}J\_{i}}}{B(r\_{1},r\_{k+1}-r\_{1}-\sum\_{j=2}^{k}J\_{i})(r\_{k+1}-1-\sum\_{i=2}^{k}J\_{i})!}\,du\_{1}. |  |

By taking p1=r1,q1=rk+1−r1−∑i=2kJip\_{1}=r\_{1},q\_{1}=r\_{k+1}-r\_{1}-\sum\_{i=2}^{k}J\_{i}, we have

|  |  |  |
| --- | --- | --- |
|  | =n!​ΣJk​⋯​ΣJ2​I0,F​(y2)​(F​(y−1);p1,q1)(rk+1−1−∑i=2kJi)!\displaystyle=n!\Sigma\_{J\_{k}}\cdots\Sigma\_{J\_{2}}\frac{I\_{0,F(y\_{2})}\big(F(y-1);p\_{1},q\_{1}\big)}{(r\_{k+1}-1-\sum\_{i=2}^{k}J\_{i})!} |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​ΣJk​⋯​ΣJ2​1(rk+1−1−∑i=2kJi)!\displaystyle=n!\Sigma\_{J\_{k}}\cdots\Sigma\_{J\_{2}}\frac{1}{(r\_{k+1}-1-\sum\_{i=2}^{k}J\_{i})!} |  |
|  |  |  |
| --- | --- | --- |
|  | ×∑J1=0q1−1(p1+q1−1J1)(F(y1))p1+q1−1−J1(F(y2)−F(y1))J1\displaystyle\times\sum\_{J\_{1}=0}^{q\_{1}-1}\binom{p\_{1}+q\_{1}-1}{J\_{1}}\Big(F(y\_{1})\Big)^{p\_{1}+q\_{1}-1-J\_{1}}\Big(F(y\_{2})-F(y\_{1})\Big)^{J\_{1}} |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​ΣJk​⋯​ΣJ2​1(rk+1−1−∑i=2kJi)!​∑J1=0rk+1−r1−1−∑i=2kJi(rk+1−1−∑i=2kJiJ1)\displaystyle=n!\Sigma\_{J\_{k}}\cdots\Sigma\_{J\_{2}}\frac{1}{(r\_{k+1}-1-\sum\_{i=2}^{k}J\_{i})!}\sum\_{J\_{1}=0}^{r\_{k+1}-r\_{1}-1-\sum\_{i=2}^{k}J\_{i}}\binom{r\_{k+1}-1-\sum\_{i=2}^{k}J\_{i}}{J\_{1}} |  |
|  |  |  |
| --- | --- | --- |
|  | ×(F​(y1))rk+1−1−∑i=2kJi​(F​(y2)−F​(y1))J1\displaystyle\times\Big(F(y\_{1})\Big)^{r\_{k+1}-1-\sum\_{i=2}^{k}J\_{i}}\Big(F(y\_{2})-F(y\_{1})\Big)^{J\_{1}} |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​ΣJk​⋯​ΣJ2​∑J1=0rk+1−r1−1−∑i=2kJi(F​(y2)−F​(y1))J1J1!⋅(F​(y1))rk+1−1−∑i=1kJi(rk+1−1−∑i=1kJi)!\displaystyle=n!\Sigma\_{J\_{k}}\cdots\Sigma\_{J\_{2}}\sum\_{J\_{1}=0}^{r\_{k+1}-r\_{1}-1-\sum\_{i=2}^{k}J\_{i}}\frac{\big(F(y\_{2})-F(y\_{1})\big)^{J\_{1}}}{J\_{1}!}\cdot\frac{\big(F(y\_{1})\big)^{r\_{k+1}-1-\sum\_{i=1}^{k}J\_{i}}}{(r\_{k+1}-1-\sum\_{i=1}^{k}J\_{i})!} |  |
|  |  |  |
| --- | --- | --- |
|  | =∑Jk=0rk+1−rk−1∑Jk−1=0rk+2−rk−1−Jk−1∑Jk−2=0rk+1−rk−2−Jk−Jk−1−1⋯​∑J1=0rk+1−r1−1−∑i=2kJi\displaystyle=\sum\_{J\_{k}=0}^{r\_{k+1}-r\_{k}-1}\quad\sum\_{J\_{k-1}=0}^{r\_{k+2}-r\_{k-1}-J\_{k}-1}\quad\sum\_{J\_{k-2}=0}^{r\_{k+1}-r\_{k-2}-J\_{k}-J\_{k-1}-1}\cdots\sum\_{J\_{1}=0}^{r\_{k+1}-r\_{1}-1-\sum\_{i=2}^{k}J\_{i}} |  |
|  |  |  |
| --- | --- | --- |
|  | n!(rk+1−1−∑i=1kJi)!​J1!​⋯​Jk!\displaystyle\frac{n!}{(r\_{k+1}-1-\sum\_{i=1}^{k}J\_{i})!J\_{1}!\cdots J\_{k}!} |  |
|  |  |  |
| --- | --- | --- |
|  | ×(F​(yk+1)−F​(yk))Jk​(F​(yk)−F​(yk−1))Jk−1​⋯​(F​(y1)−F​(y0))rk+1−1−∑i=1kJi\displaystyle\times\big(F(y\_{k+1})-F(y\_{k})\big)^{J\_{k}}\big(F(y\_{k})-F(y\_{k-1})\big)^{J\_{k-1}}\cdots\big(F(y\_{1})-F(y\_{0})\big)^{r\_{k+1}-1-\sum\_{i=1}^{k}J\_{i}} |  |

where F​(y0)=0F(y\_{0})=0 and F​(yk+1)=1F(y\_{k+1})=1. Then, taking J0=rk+1−1−∑i=1kJi=n−∑i=1kJiJ\_{0}=r\_{k+1}-1-\sum\_{i=1}^{k}J\_{i}=n-\sum\_{i=1}^{k}J\_{i}, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∑Jk=0n−rk∑Jk−1=0n−rk−1−Jk∑Jk−2=0n−rk−2−Jk−Jk−1⋯​∑J1=0n−r1−∑i=2kJi\displaystyle=\sum\_{J\_{k}=0}^{n-r\_{k}}\quad\sum\_{J\_{k-1}=0}^{n-r\_{k-1}-J\_{k}}\quad\sum\_{J\_{k-2}=0}^{n-r\_{k-2}-J\_{k}-J\_{k-1}}\cdots\sum\_{J\_{1}=0}^{n-r\_{1}-\sum\_{i=2}^{k}J\_{i}} |  | (2.7) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (nJ0,J1,…,Jk)​∏i=0k(F​(yi+1)−F​(yi))Ji,\displaystyle\quad\binom{n}{J\_{0},J\_{1},\ldots,J\_{k}}\prod\_{i=0}^{k}\Big(F\left(y\_{i+1}\right)-F\left(y\_{i}\right)\Big)^{J\_{i}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | s.t.∑i=0kJi=n.\displaystyle s.t.\quad\sum\_{i=0}^{k}J\_{i}=n. |  |

Now, for arbitrary y1,…,yky\_{1},\ldots,y\_{k}, we have

|  |  |  |
| --- | --- | --- |
|  | F(r1,…,rk)n​(y1,…,yk)\displaystyle F\_{(r\_{1},\ldots,r\_{k})}^{n}(y\_{1},\ldots,y\_{k}) |  |
|  |  |  |
| --- | --- | --- |
|  | =ℙ​[X(1)n≤y1,…,X(k)n≤yk]\displaystyle=\mathbb{P}\left[X\_{(1)}^{n}\leq y\_{1},\ldots,X\_{(k)}^{n}\leq y\_{k}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | =ℙ​[X(1)n≤y(1)k,…,X(k)n≤y(k)k]\displaystyle=\mathbb{P}\left[X\_{(1)}^{n}\leq y\_{(1)}^{k},\ldots,X\_{(k)}^{n}\leq y\_{(k)}^{k}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =F(r1,…,rk)n​(y(1)k,…,y(k)k),\displaystyle=F\_{(r\_{1},\ldots,r\_{k})}^{n}\left(y\_{(1)}^{k},\ldots,y\_{(k)}^{k}\right), |  | (2.8) |

and as y(1)k≤⋯≤y(k)ky\_{(1)}^{k}\leq\cdots\leq y\_{(k)}^{k}, applying ([2.7](https://arxiv.org/html/2511.04784v1#S2.E7 "In 2. Ordered and Tail-Based Statistics")) to ([2.8](https://arxiv.org/html/2511.04784v1#S2.E8 "In 2. Ordered and Tail-Based Statistics")) returns

|  |  |  |
| --- | --- | --- |
|  | F(r1,…,rk)n​(y1,…,yk)\displaystyle F\_{(r\_{1},\ldots,r\_{k})}^{n}(y\_{1},\ldots,y\_{k}) |  |
|  |  |  |
| --- | --- | --- |
|  | =∑Jk=0n−rk∑Jk−1=0n−rk−1−Jk∑Jk−2=0n−rk−2−Jk−Jk−1⋯​∑J1=0n−r1−∑i=2kJi\displaystyle=\sum\_{J\_{k}=0}^{n-r\_{k}}\quad\sum\_{J\_{k-1}=0}^{n-r\_{k-1}-J\_{k}}\quad\sum\_{J\_{k-2}=0}^{n-r\_{k-2}-J\_{k}-J\_{k-1}}\cdots\sum\_{J\_{1}=0}^{n-r\_{1}-\sum\_{i=2}^{k}J\_{i}} |  |
|  |  |  |
| --- | --- | --- |
|  | (nJ0,J1,…,Jk)​∏i=0k(F​(y(i+1)k)−F​(y(i)k))Ji,\displaystyle\quad\binom{n}{J\_{0},J\_{1},\ldots,J\_{k}}\prod\_{i=0}^{k}\Big(F\left(y\_{(i+1)}^{k}\right)-F\left(y\_{(i)}^{k}\right)\Big)^{J\_{i}}, |  |
|  |  |  |
| --- | --- | --- |
|  | s.t.∑i=0kJi=n.\displaystyle s.t.\quad\sum\_{i=0}^{k}J\_{i}=n. |  |

∎

###### Proof 2: Combinatorics.

First, we note

|  |  |  |
| --- | --- | --- |
|  | X(r)n≤y⇔r≤∑i=1n𝟙(−∞,y]​(Xi),X\_{(r)}^{n}\leq y\iff r\leq\sum\_{i=1}^{n}\mathds{1}\_{(-\infty,y]}(X\_{i}), |  |

and so,

|  |  |  |
| --- | --- | --- |
|  | F(r1,…,rk)n​(y1,…,yk)\displaystyle F\_{(r\_{1},\ldots,r\_{k})}^{n}(y\_{1},\ldots,y\_{k}) |  |
|  |  |  |
| --- | --- | --- |
|  | =ℙ​[X(1)n≤y1,…,X(k)n≤yk]\displaystyle=\mathbb{P}\left[X\_{(1)}^{n}\leq y\_{1},\ldots,X\_{(k)}^{n}\leq y\_{k}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =ℙ​[r1≤∑i=1n𝟙(−∞,y1]​(Xi),⋯,rk≤∑i=1n𝟙(−∞,yk]​(Xi)].\displaystyle=\mathbb{P}\left[r\_{1}\leq\sum\_{i=1}^{n}\mathds{1}\_{(-\infty,y\_{1}]}(X\_{i})\,,\,\cdots\,,\,r\_{k}\leq\sum\_{i=1}^{n}\mathds{1}\_{(-\infty,y\_{k}]}(X\_{i})\right]. |  | (2.9) |

Here, we consider the following intervals

U0U1⋯Uk−1Uk\;U\_{0}\hskip 42.67912ptU\_{1}\hskip 39.83368pt\cdots\hskip 42.67912ptU\_{k-1}\hskip 45.52458ptU\_{k}

−∞=y0-\infty=y\_{0}]———[
y1y\_{1}]———[y2⋯yk−1y\_{2}\quad\cdots\quad y\_{k-1}]———[
yky\_{k}]———[yk+1=∞y\_{k+1}=\infty,

and denote

|  |  |  |
| --- | --- | --- |
|  | #k:=#​{i|Xi∈Uk}=∑i=1n𝟙]yk,yk+1[​(Xi),\#\_{k}\;:=\;\#\{i|X\_{i}\in U\_{k}\}\,=\,\sum\_{i=1}^{n}\mathds{1}\_{]y\_{k},y\_{k+1}[}(X\_{i}), |  |

where #\# denotes the cardinality of the set. Then, we have

|  |  |  |
| --- | --- | --- |
|  | rk≤∑i=1n𝟙(−∞,yk]​(Xi)⇔0≤#k≤n−rk.r\_{k}\leq\sum\_{i=1}^{n}\mathds{1}\_{(-\infty,y\_{k}]}(X\_{i})\iff 0\leq\#\_{k}\leq n-r\_{k}. |  |

Thus, equation ([2.9](https://arxiv.org/html/2511.04784v1#S2.E9 "In 2. Ordered and Tail-Based Statistics")) can be rewritten as follows.

|  |  |  |
| --- | --- | --- |
|  | =ℙ​[r1≤∑i=1n𝟙(−∞,y1]​(Xi),⋯,rk−1≤∑i=1n𝟙(−∞,yk−1]​(Xi), 0≤#k≤n−rk]\displaystyle=\mathbb{P}\left[r\_{1}\leq\sum\_{i=1}^{n}\mathds{1}\_{(-\infty,y\_{1}]}(X\_{i})\,,\,\cdots\,,\,r\_{k-1}\leq\sum\_{i=1}^{n}\mathds{1}\_{(-\infty,y\_{k-1}]}(X\_{i}),\,0\leq\#\_{k}\leq n-r\_{k}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | =∑Jk=0n−rkℙ​[r1≤∑i=1n𝟙(−∞,y1]​(Xi),⋯,rk−1≤∑i=1n𝟙(−∞,yk−1]​(Xi)|#k=Jk]\displaystyle=\sum\_{J\_{k}=0}^{n-r\_{k}}\mathbb{P}\left[r\_{1}\leq\sum\_{i=1}^{n}\mathds{1}\_{(-\infty,y\_{1}]}(X\_{i})\,,\,\cdots\,,\,r\_{k-1}\leq\sum\_{i=1}^{n}\mathds{1}\_{(-\infty,y\_{k-1}]}(X\_{i})\Big|\#\_{k}=J\_{k}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ×ℙ​[#k=Jk]\displaystyle\times\mathbb{P}[\#\_{k}=J\_{k}] |  |
|  |  |  |
| --- | --- | --- |
|  | =∑Jk=0n−rkℙ​[r1≤∑i=1n𝟙(−∞,y1]​(Xi),⋯,rk−1≤∑i=1n𝟙(−∞,yk−1]​(Xi)|#k=Jk]\displaystyle=\sum\_{J\_{k}=0}^{n-r\_{k}}\mathbb{P}\left[r\_{1}\leq\sum\_{i=1}^{n}\mathds{1}\_{(-\infty,y\_{1}]}(X\_{i})\,,\,\cdots\,,\,r\_{k-1}\leq\sum\_{i=1}^{n}\mathds{1}\_{(-\infty,y\_{k-1}]}(X\_{i})\Big|\#\_{k}=J\_{k}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ×(nJk)​(F​(yk+1)−F​(yk))Jk.\displaystyle\times\binom{n}{J\_{k}}\Big(F\left(y\_{k+1}\right)-F\left(y\_{k}\right)\Big)^{J\_{k}}. |  | (2.10) |

By denoting

|  |  |  |
| --- | --- | --- |
|  | #k−1:=#​{i|Xi∈Uk−1}=∑i=1n𝟙]yk−1,yk[​(Xi),\#\_{k-1}:=\#\{i|X\_{i}\in U\_{k-1}\}=\sum\_{i=1}^{n}\mathds{1}\_{]y\_{k-1},y\_{k}[}(X\_{i}), |  |

we can continue ([2.10](https://arxiv.org/html/2511.04784v1#S2.E10 "In 2. Ordered and Tail-Based Statistics")) as follows.

|  |  |  |
| --- | --- | --- |
|  | =∑Jk=0n−rk∑Jk−1=0n−Jk−rk−1\displaystyle=\sum\_{J\_{k}=0}^{n-r\_{k}}\quad\sum\_{J\_{k-1}=0}^{n-J\_{k}-r\_{k-1}} |  |
|  |  |  |
| --- | --- | --- |
|  | ℙ[r1≤∑i=1n𝟙(−∞,y1](Xi),⋯,rk−2≤∑i=1n𝟙(−∞,yk−2](Xi)|#k−1=Jk−1,#k=Jk]\displaystyle\mathbb{P}\left[r\_{1}\leq\sum\_{i=1}^{n}\mathds{1}\_{(-\infty,y\_{1}]}(X\_{i})\,,\,\cdots\,,\,r\_{k-2}\leq\sum\_{i=1}^{n}\mathds{1}\_{(-\infty,y\_{k-2}]}(X\_{i})\Big|\#\_{k-1}=J\_{k-1},\#\_{k}=J\_{k}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ×ℙ​[#k−1=Jk−1|#k=Jk]⋅ℙ​[#k=Jk]\displaystyle\times\mathbb{P}[\#\_{k-1}=J\_{k-1}\,|\,\#\_{k}=J\_{k}]\cdot\mathbb{P}[\#\_{k}=J\_{k}] |  |
|  |  |  |
| --- | --- | --- |
|  | =∑Jk=0n−rk∑Jk−1=0n−Jk−rk−1\displaystyle=\sum\_{J\_{k}=0}^{n-r\_{k}}\sum\_{J\_{k-1}=0}^{n-J\_{k}-r\_{k-1}} |  |
|  |  |  |
| --- | --- | --- |
|  | ℙ[r1≤∑i=1n𝟙(−∞,y1](Xi),⋯,rk−2≤∑i=1n𝟙(−∞,yk−2](Xi)|#k−1=Jk−1,#k=Jk]\displaystyle\mathbb{P}\left[r\_{1}\leq\sum\_{i=1}^{n}\mathds{1}\_{(-\infty,y\_{1}]}(X\_{i})\,,\,\cdots\,,\,r\_{k-2}\leq\sum\_{i=1}^{n}\mathds{1}\_{(-\infty,y\_{k-2}]}(X\_{i})\Big|\#\_{k-1}=J\_{k-1},\#\_{k}=J\_{k}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ×(nJk)​(n−JkJk−1)​(F​(yk+1)−F​(yk))Jk​(F​(yk)−F​(yk−1))Jk−1.\displaystyle\times\binom{n}{J\_{k}}\binom{n-J\_{k}}{J\_{k-1}}\Big(F\left(y\_{k+1}\right)-F\left(y\_{k}\right)\Big)^{J\_{k}}\Big(F\left(y\_{k}\right)-F\left(y\_{k-1}\right)\Big)^{J\_{k-1}}. |  |

By continuing this process, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑Jk=0n−rk∑Jk−1=0n−rk−1−Jk∑Jk−2=0n−rk−2−Jk−Jk−1⋯​∑J1=0n−r1−∑i=2kJi\displaystyle\sum\_{J\_{k}=0}^{n-r\_{k}}\quad\sum\_{J\_{k-1}=0}^{n-r\_{k-1}-J\_{k}}\quad\sum\_{J\_{k-2}=0}^{n-r\_{k-2}-J\_{k}-J\_{k-1}}\cdots\sum\_{J\_{1}=0}^{n-r\_{1}-\sum\_{i=2}^{k}J\_{i}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ℙ[#1=J1|#2=J2,…,#k=Jk]\displaystyle\mathbb{P}[\#\_{1}=J\_{1}\,|\,\#\_{2}=J\_{2},\ldots,\#\_{k}=J\_{k}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ℙ[#2=J2|#3=J3,…,#k=Jk]\displaystyle\mathbb{P}[\#\_{2}=J\_{2}\,|\,\#\_{3}=J\_{3},\ldots,\#\_{k}=J\_{k}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⋯\displaystyle\cdots |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ℙ​[#k−1=Jk−1|#k=Jk]\displaystyle\mathbb{P}[\#\_{k-1}=J\_{k-1}\,|\,\#\_{k}=J\_{k}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ℙ​[#k=Jk]\displaystyle\mathbb{P}[\#\_{k}=J\_{k}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑Jk=0n−rk∑Jk−1=0n−rk−1−Jk∑Jk−2=0n−rk−2−Jk−Jk−1⋯​∑J1=0n−r1−∑i=2kJi\displaystyle\sum\_{J\_{k}=0}^{n-r\_{k}}\quad\sum\_{J\_{k-1}=0}^{n-r\_{k-1}-J\_{k}}\quad\sum\_{J\_{k-2}=0}^{n-r\_{k-2}-J\_{k}-J\_{k-1}}\cdots\sum\_{J\_{1}=0}^{n-r\_{1}-\sum\_{i=2}^{k}J\_{i}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (nJk)​(n−JkJk−1)​⋯​(n−∑i=2kJiJ1)⋅(F​(y1)−F​(y0))n−∑i=1kJi\displaystyle\binom{n}{J\_{k}}\binom{n-J\_{k}}{J\_{k-1}}\cdots\binom{n-\sum\_{i=2}^{k}J\_{i}}{J\_{1}}\cdot\Big(F\left(y\_{1}\right)-F\left(y\_{0}\right)\Big)^{n-\sum\_{i=1}^{k}J\_{i}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×(F​(y2)−F​(y1))J1​⋯​(F​(yk+1)−F​(yk))Jk,\displaystyle\times\Big(F\left(y\_{2}\right)-F\left(y\_{1}\right)\Big)^{J\_{1}}\cdots\Big(F\left(y\_{k+1}\right)-F\left(y\_{k}\right)\Big)^{J\_{k}}, |  |

and by taking J0=n−∑i=1kJiJ\_{0}=n-\sum\_{i=1}^{k}J\_{i}, this returns ([2.6](https://arxiv.org/html/2511.04784v1#S2.E6 "In Theorem 2.5. ‣ 2. Ordered and Tail-Based Statistics")).
∎

###### Corollary 2.6.

Given the assumptions and notations in Theorem [2.5](https://arxiv.org/html/2511.04784v1#S2.Thmdfn5 "Theorem 2.5. ‣ 2. Ordered and Tail-Based Statistics"), if x1≤⋯≤xkx\_{1}\leq\cdots\leq x\_{k}, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | F(r1,…,rk)n​(x1,…,xk)\displaystyle F\_{(r\_{1},\ldots,r\_{k})}^{n}(x\_{1},\ldots,x\_{k}) |  | (2.11) |
|  |  |  |
| --- | --- | --- |
|  | =∑Jk=0n−rk∑Jk−1=0n−rk−1−Jk∑Jk−2=0n−rk−2−Jk−Jk−1⋯​∑J1=0n−r1−∑i=2kJi\displaystyle=\sum\_{J\_{k}=0}^{n-r\_{k}}\quad\sum\_{J\_{k-1}=0}^{n-r\_{k-1}-J\_{k}}\quad\sum\_{J\_{k-2}=0}^{n-r\_{k-2}-J\_{k}-J\_{k-1}}\cdots\sum\_{J\_{1}=0}^{n-r\_{1}-\sum\_{i=2}^{k}J\_{i}} |  |
|  |  |  |
| --- | --- | --- |
|  | (nJ0,J1,…,Jk)​∏i=0k(F​(xi+1)−F​(xi))Ji,\displaystyle\quad\binom{n}{J\_{0},J\_{1},\ldots,J\_{k}}\prod\_{i=0}^{k}\big(F\left(x\_{i+1}\right)-F\left(x\_{i}\right)\big)^{J\_{i}}, |  |
|  |  |  |
| --- | --- | --- |
|  | s.t.∑i=0kJi=n.\displaystyle s.t.\quad\sum\_{i=0}^{k}J\_{i}=n. |  |

## 3. Exact Distribution of Tail-Based Statistics

Here, we apply the Corollary [2.3](https://arxiv.org/html/2511.04784v1#S2.Thmdfn3 "Corollary 2.3. ‣ 2. Ordered and Tail-Based Statistics") to investigate the exact cumulative distribution of Λn​(p)\Lambda\_{n}(p). We use a.s. to denote almost sure convergence.

###### Proposition 3.1.

Let p∈(0,1)p\in(0,1) and 0<|λ|<10<|\lambda|<1. If the random variables X1,X2,…,XnX\_{1},X\_{2},\ldots,X\_{n} are i.i.d with common absolutely continuous distribution FF, and the almost everywhere positive density function ff, then for some N0≥1N\_{0}\geq 1, the cumulative distribution function of Λn​(p),n≥N0\Lambda\_{n}(p),n\geq N\_{0} is

* (i)

  If λ​𝔼​[X]>0\lambda\mathbb{E}[X]>0, then

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | FΛn​(p)​(λ)=1−n!​∫01∫0un⋯​∫0u3\displaystyle F\_{\Lambda\_{n}(p)}(\lambda)=1-n!\int\_{0}^{1}\int\_{0}^{u\_{n}}\cdots\int\_{0}^{u\_{3}} |  |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  |  | F​[(1−λλ)​∑i=⌈n​p⌉nF−1​(ui)−∑i=2⌈n​p⌉−1F−1​(ui)]​d​u2​⋯​d​un.\displaystyle F\left[\left(\frac{1-\lambda}{\lambda}\right)\sum\_{i=\left\lceil np\right\rceil}^{n}F^{-1}(u\_{i})-\sum\_{i=2}^{\left\lceil np\right\rceil-1}F^{-1}(u\_{i})\right]\,du\_{2}\cdots du\_{n}. |  | (3.1) |
* (ii)

  If λ​𝔼​[X]<0\lambda\mathbb{E}[X]<0, then

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | FΛn​(p)​(λ)=n!​∫01∫0un⋯​∫0u3\displaystyle F\_{\Lambda\_{n}(p)}(\lambda)=n!\int\_{0}^{1}\int\_{0}^{u\_{n}}\cdots\int\_{0}^{u\_{3}} |  |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  |  | F​[(1−λλ)​∑i=⌈n​p⌉nF−1​(ui)−∑i=2⌈n​p⌉−1F−1​(ui)]​d​u2​⋯​d​un.\displaystyle F\left[\left(\frac{1-\lambda}{\lambda}\right)\sum\_{i=\left\lceil np\right\rceil}^{n}F^{-1}(u\_{i})-\sum\_{i=2}^{\left\lceil np\right\rceil-1}F^{-1}(u\_{i})\right]\,du\_{2}\cdots du\_{n}. |  | (3.2) |

###### Proof.

For (i), let 0<λ,𝔼​[X]<10<\lambda,\mathbb{E}[X]<1. Then by the strong low of larg numbers (LLN) ∑i=1nXi/n​⟶a.s.​𝔼​[X]\sum\_{i=1}^{n}X\_{i}/n\overset{a.s.}{\longrightarrow}\mathbb{E}[X] and so, there are some N0≥1N\_{0}\geq 1 that for all n≥N0n\geq N\_{0} we have ∑i=1nXi>0\sum\_{i=1}^{n}X\_{i}>0. Next we have

|  |  |  |
| --- | --- | --- |
|  | Λn​(p)≤λ\displaystyle\Lambda\_{n}(p)\leq\lambda |  |
|  |  |  |
| --- | --- | --- |
|  | ⇔∑i=⌈n​p⌉nX(i)n∑i=1nXi≤λ\displaystyle\iff\frac{\sum\_{i=\left\lceil np\right\rceil}^{n}X\_{(i)}^{n}}{\sum\_{i=1}^{n}X\_{i}}\leq\lambda |  |
|  |  |  |
| --- | --- | --- |
|  | ⇔∑i=⌈n​p⌉nX(i)n≤λ​∑i=1nXi\displaystyle\iff\sum\_{i=\left\lceil np\right\rceil}^{n}X\_{(i)}^{n}\leq\lambda\sum\_{i=1}^{n}X\_{i} |  |
|  |  |  |
| --- | --- | --- |
|  | ⇔λ​∑i=1⌈n​p⌉−1X(i)n−(1−λ)​∑i=⌈n​p⌉nX(i)n≥ 0\displaystyle\iff\lambda\sum\_{i=1}^{\left\lceil np\right\rceil-1}X\_{(i)}^{n}\,-\,(1-\lambda)\sum\_{i=\left\lceil np\right\rceil}^{n}X\_{(i)}^{n}\,\geq\,0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⇔X(1)n≥(1−λλ)​∑i=⌈n​p⌉nX(i)n−∑i=2⌈n​p⌉−1X(i)n.\displaystyle\iff X\_{(1)}^{n}\geq\left(\frac{1-\lambda}{\lambda}\right)\sum\_{i=\left\lceil np\right\rceil}^{n}X\_{(i)}^{n}-\sum\_{i=2}^{\left\lceil np\right\rceil-1}X\_{(i)}^{n}. |  | (3.3) |

Now, by denoting

|  |  |  |
| --- | --- | --- |
|  | Dn​(λ,p):={𝒙=(x1,…,xn)|(1−λλ)​∑i=⌈n​p⌉nxi−∑i=2⌈n​p⌉−1xi≤x1,x1<x2<⋯<xn}⊂ℝn,D\_{n}(\lambda,p):=\left\{\bm{x}=(x\_{1},\ldots,x\_{n})\,\Bigg|\,\begin{matrix}\left(\frac{1-\lambda}{\lambda}\right)\sum\_{i=\left\lceil np\right\rceil}^{n}x\_{i}-\sum\_{i=2}^{\left\lceil np\right\rceil-1}x\_{i}\leq x\_{1},\\ x\_{1}<x\_{2}<\cdots<x\_{n}\end{matrix}\right\}\subset\mathbb{R}^{n}, |  |

from Corollary [2.3](https://arxiv.org/html/2511.04784v1#S2.Thmdfn3 "Corollary 2.3. ‣ 2. Ordered and Tail-Based Statistics"), one can write

|  |  |  |  |
| --- | --- | --- | --- |
|  | FΛn​(p)​(λ)\displaystyle F\_{\Lambda\_{n}(p)}(\lambda) | =ℙ​[Λn​(p)≤λ]\displaystyle=\mathbb{P}[\Lambda\_{n}(p)\leq\lambda] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙ​[λ​∑i=1⌈n​p⌉−1X(i)n−(1−λ)​∑i=⌈n​p⌉nX(i)n≥ 0]\displaystyle=\mathbb{P}\left[\lambda\sum\_{i=1}^{\left\lceil np\right\rceil-1}X\_{(i)}^{n}\,-\,(1-\lambda)\sum\_{i=\left\lceil np\right\rceil}^{n}X\_{(i)}^{n}\,\geq\,0\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫Dn​(λ,p)f(1,…,n)n​(𝒙)​𝑑𝒙\displaystyle=\int\_{D\_{n}(\lambda,p)}f^{n}\_{(1,\ldots,n)}(\bm{x})\,d\bm{x} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =n!​∫⋯∫Dn​(λ,p)​(∏i=1nf​(xi))​d​x1​⋯​d​xn\displaystyle=n!\underset{D\_{n}(\lambda,p)}{\idotsint}\left(\prod\_{i=1}^{n}f(x\_{i})\right)\,dx\_{1}\cdots dx\_{n} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =n!​∫−∞∞∫−∞xn⋯​∫−∞x3∫(1−λλ)​∑i=⌈n​p⌉nxi−∑i=2⌈n​p⌉−1xix2\displaystyle=n!\int\_{-\infty}^{\infty}\int\_{-\infty}^{x\_{n}}\cdots\int\_{-\infty}^{x\_{3}}\int\_{\left(\frac{1-\lambda}{\lambda}\right)\sum\_{i=\left\lceil np\right\rceil}^{n}x\_{i}-\sum\_{i=2}^{\left\lceil np\right\rceil-1}x\_{i}}^{x\_{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (∏i=1nf​(xi))​d​x1​⋯​d​xn.\displaystyle\qquad\left(\prod\_{i=1}^{n}f(x\_{i})\right)\,dx\_{1}\cdots dx\_{n}. |  |

Then, since FF is almost everywhere differentiable and invertible, by changing the variables ui=F​(xi)u\_{i}=F(x\_{i}) or xi=F−1​(ui)x\_{i}=F^{-1}(u\_{i}), for every i=1,…,ni=1,\ldots,n we have

|  |  |  |
| --- | --- | --- |
|  | =n!​∫01∫0un⋯​∫0u3∫F​[(1−λλ)​∑i=⌈n​p⌉nF−1​(ui)−∑i=2⌈n​p⌉−1F−1​(ui)]u2𝑑u1​⋯​𝑑un\displaystyle=n!\int\_{0}^{1}\int\_{0}^{u\_{n}}\cdots\int\_{0}^{u\_{3}}\int\_{F\left[\left(\frac{1-\lambda}{\lambda}\right)\sum\_{i=\left\lceil np\right\rceil}^{n}F^{-1}(u\_{i})-\sum\_{i=2}^{\left\lceil np\right\rceil-1}F^{-1}(u\_{i})\right]}^{u\_{2}}\,du\_{1}\cdots du\_{n} |  |
|  |  |  |
| --- | --- | --- |
|  | =n!​∫01∫0un⋯​∫0u3∫0u2𝑑u1​⋯​𝑑un\displaystyle=n!\int\_{0}^{1}\int\_{0}^{u\_{n}}\cdots\int\_{0}^{u\_{3}}\int\_{0}^{u\_{2}}\,du\_{1}\cdots du\_{n} |  |
|  |  |  |
| --- | --- | --- |
|  | −n!​∫01∫0un⋯​∫0u3∫0F​[(1−λλ)​∑i=⌈n​p⌉nF−1​(ui)−∑i=2⌈n​p⌉−1F−1​(ui)]𝑑u1​⋯​𝑑un,\displaystyle-n!\int\_{0}^{1}\int\_{0}^{u\_{n}}\cdots\int\_{0}^{u\_{3}}\int\_{0}^{F\left[\left(\frac{1-\lambda}{\lambda}\right)\sum\_{i=\left\lceil np\right\rceil}^{n}F^{-1}(u\_{i})-\sum\_{i=2}^{\left\lceil np\right\rceil-1}F^{-1}(u\_{i})\right]}\,du\_{1}\cdots du\_{n}, |  |

and this yields ([(i)](https://arxiv.org/html/2511.04784v1#S3.Ex1 "item (i) ‣ Proposition 3.1. ‣ 3. Exact Distribution of Tail-Based Statistics")). If −1<λ,𝔼​[X]<0-1<\lambda,\mathbb{E}[X]<0, then similarly ([3.3](https://arxiv.org/html/2511.04784v1#S3.E3 "In 3. Exact Distribution of Tail-Based Statistics")) is valid and so we have the same result.

For (ii), let λ>0,𝔼​[X]<0\lambda>0,\mathbb{E}[X]<0. Similar to the proof of (i), there are some N0≥1N\_{0}\geq 1 that for all n≥N0n\geq N\_{0} we have ∑i=1nXi<0\sum\_{i=1}^{n}X\_{i}<0. Next, for this case, one can see

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λn​(p)≥λ⇔X(1)n≥(1−λλ)​∑i=⌈n​p⌉nX(i)n−∑i=2⌈n​p⌉−1X(i)n,\Lambda\_{n}(p)\geq\lambda\iff X\_{(1)}^{n}\geq\left(\frac{1-\lambda}{\lambda}\right)\sum\_{i=\left\lceil np\right\rceil}^{n}X\_{(i)}^{n}-\sum\_{i=2}^{\left\lceil np\right\rceil-1}X\_{(i)}^{n}, |  | (3.4) |

and so, in this case we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | FΛn​(p)​(λ)\displaystyle F\_{\Lambda\_{n}(p)}(\lambda) | =ℙ​[Λn​(p)≤λ]\displaystyle=\mathbb{P}[\Lambda\_{n}(p)\leq\lambda] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1−ℙ​[Λn​(p)≥λ]\displaystyle=1-\mathbb{P}[\Lambda\_{n}(p)\geq\lambda] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1−ℙ​[X(1)n≥(1−λλ)​∑i=⌈n​p⌉nX(i)n−∑i=2⌈n​p⌉−1X(i)n]\displaystyle=1-\mathbb{P}\left[X\_{(1)}^{n}\geq\left(\frac{1-\lambda}{\lambda}\right)\sum\_{i=\left\lceil np\right\rceil}^{n}X\_{(i)}^{n}-\sum\_{i=2}^{\left\lceil np\right\rceil-1}X\_{(i)}^{n}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1−∫Dn​(λ,p)f(1,…,n)n​(𝒙)​𝑑𝒙.\displaystyle=1-\int\_{D\_{n}(\lambda,p)}f^{n}\_{(1,\ldots,n)}(\bm{x})\,d\bm{x}. |  |

Now, proceeding with similar calculation of part (i), from this final integral we have ([(ii)](https://arxiv.org/html/2511.04784v1#S3.Ex2 "item (ii) ‣ Proposition 3.1. ‣ 3. Exact Distribution of Tail-Based Statistics")). If λ<0,𝔼​[X]>0\lambda<0,\mathbb{E}[X]>0, then similarly ([3.4](https://arxiv.org/html/2511.04784v1#S3.E4 "In 3. Exact Distribution of Tail-Based Statistics")) is valid, and so, we have the same result.
∎

## 4. Convergence of Tail-Based Statistics

As the explicit form of the exact distribution functions ([(i)](https://arxiv.org/html/2511.04784v1#S3.Ex1 "item (i) ‣ Proposition 3.1. ‣ 3. Exact Distribution of Tail-Based Statistics")) and ([(ii)](https://arxiv.org/html/2511.04784v1#S3.Ex2 "item (ii) ‣ Proposition 3.1. ‣ 3. Exact Distribution of Tail-Based Statistics")) include multiple integrals, they are not computationally suitable for larg nambers of nn. So, we need to investigate further for the asymptotic behavior and distribution here.

###### Lemma 4.1.

Let X1,X2,…,XnX\_{1},X\_{2},\ldots,X\_{n} be i.i.d random variables with common absolutely continuous distribution FF. Then, for all p∈(0,1)p\in(0,1) that FF is continuous at its ppth quantile qpq\_{p}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1n​∑i=1nXi​𝟙{Xi≥Qn​(p)}​⟶a.s.​𝔼​[X1​𝟙{X1≥qp}],\frac{1}{n}\sum\_{i=1}^{n}X\_{i}\mathds{1}\_{\{X\_{i}\geq Q\_{n}(p)\}}\overset{a.s.}{\longrightarrow}\mathbb{E}\left[X\_{1}\mathds{1}\_{\{X\_{1}\geq q\_{p}\}}\right], |  | (4.1) |

where Qn​(p)Q\_{n}(p) is the ppth quantile of {Xi}i=1n\{X\_{i}\}\_{i=1}^{n}.

###### Proof.

Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | Un​(p)\displaystyle U\_{n}(p) | =1n​∑i=1nXi​𝟙{Xi≥Qn​(p)},\displaystyle=\frac{1}{n}\sum\_{i=1}^{n}X\_{i}\mathds{1}\_{\{X\_{i}\geq Q\_{n}(p)\}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Vn​(p)\displaystyle V\_{n}(p) | =1n​∑i=1nXi​𝟙{Xi≥qp}.\displaystyle=\frac{1}{n}\sum\_{i=1}^{n}X\_{i}\mathds{1}\_{\{X\_{i}\geq q\_{p}\}}. |  |

By the strong LLN we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vn​(p)​⟶a.s.​𝔼​[X1​𝟙{X1≥qp}].V\_{n}(p)\overset{a.s.}{\longrightarrow}\mathbb{E}\left[X\_{1}\mathds{1}\_{\{X\_{1}\geq q\_{p}\}}\right]. |  | (4.2) |

On the other hand, it is shown in [[25](https://arxiv.org/html/2511.04784v1#bib.bib25)] that, given the continuity of FF on qpq\_{p}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qn​(p)​⟶a.s.​qp.Q\_{n}(p)\overset{a.s.}{\longrightarrow}q\_{p}. |  | (4.3) |

Next, we can write

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Un​(p)−Vn​(p)|\displaystyle|U\_{n}(p)-V\_{n}(p)| | ≤1n​∑i=1n|Xi|⋅|𝟙{Xi≥Qn​(p)}−𝟙{Xi≥qp}|\displaystyle\leq\frac{1}{n}\sum\_{i=1}^{n}|X\_{i}|\cdot|\mathds{1}\_{\{X\_{i}\geq Q\_{n}(p)\}}-\mathds{1}\_{\{X\_{i}\geq q\_{p}\}}| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1n​∑i=1n|Xi|​ 1{Qn​(p)∧qp≤Xi<Qn​(p)∨qp}\displaystyle=\frac{1}{n}\sum\_{i=1}^{n}|X\_{i}|\,\mathds{1}\_{\{Q\_{n}(p)\wedge q\_{p}\leq X\_{i}<Q\_{n}(p)\vee q\_{p}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1n​∑i=1n|Xi|​ 1{an​(p)≤Xi<bn​(p)},\displaystyle=\frac{1}{n}\sum\_{i=1}^{n}|X\_{i}|\,\mathds{1}\_{\{a\_{n}(p)\leq X\_{i}<b\_{n}(p)\}}, |  |

where ∧\wedge and ∨\vee are respectively minimum and maximum. Here, from ([4.3](https://arxiv.org/html/2511.04784v1#S4.E3 "In 4. Convergence of Tail-Based Statistics")), for both an​(p)=Qn​(p)∧qpa\_{n}(p)=Q\_{n}(p)\wedge q\_{p} and bn​(p)=Qn​(p)∨qpb\_{n}(p)=Q\_{n}(p)\vee q\_{p} we have

|  |  |  |
| --- | --- | --- |
|  | an​(p),bn​(p)​⟶a.s.​qp.a\_{n}(p),b\_{n}(p)\overset{a.s.}{\longrightarrow}q\_{p}. |  |

So, almost surely, for all arbitrary ε>0\varepsilon>0, there are some N1ε​(p)>0N\_{1}^{\varepsilon}(p)>0 that for all n≥N1ε​(p)n\geq N\_{1}^{\varepsilon}(p), we have

|  |  |  |
| --- | --- | --- |
|  | 𝟙[an​(p),bn​(p))​(x)=0,∀x∈ℝ∖(qp−ε,qp+ε),\mathds{1}\_{[a\_{n}(p),b\_{n}(p))}(x)=0,\qquad\forall x\in\mathbb{R}\setminus(q\_{p}-\varepsilon,q\_{p}+\varepsilon), |  |

and so,

|  |  |  |
| --- | --- | --- |
|  | 𝟙[an​(p),bn​(p))​(x)≤𝟙(qp−ε,qp+ε)​(x).\mathds{1}\_{[a\_{n}(p),b\_{n}(p))}(x)\leq\mathds{1}\_{(q\_{p}-\varepsilon\,,\,q\_{p}+\varepsilon)}(x). |  |

Hence, for i≥1i\geq 1

|  |  |  |
| --- | --- | --- |
|  | 𝟙[an​(p),bn​(p))​(Xi)≤𝟙(qp−ε,qp+ε)​(Xi).\mathds{1}\_{[a\_{n}(p),b\_{n}(p))}(X\_{i})\leq\mathds{1}\_{(q\_{p}-\varepsilon\,,\,q\_{p}+\varepsilon)}(X\_{i}). |  |

So, for n≥N1ε​(p)n\geq N\_{1}^{\varepsilon}(p), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Un​(p)−Vn​(p)|\displaystyle|U\_{n}(p)-V\_{n}(p)| | ≤1n​∑i=1n|Xi|​ 1{[an​(p),bn​(p))}​(Xi)\displaystyle\leq\frac{1}{n}\sum\_{i=1}^{n}|X\_{i}|\,\mathds{1}\_{\{[a\_{n}(p),b\_{n}(p))\}}(X\_{i}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤1n​∑i=1n|Xi|​ 1(qp−ε,qp+ε)​(Xi).\displaystyle\leq\frac{1}{n}\sum\_{i=1}^{n}|X\_{i}|\,\mathds{1}\_{(q\_{p}-\varepsilon\,,\,q\_{p}+\varepsilon)}(X\_{i}). |  |

Again, by the strong LLN

|  |  |  |
| --- | --- | --- |
|  | 1n​∑i=1n|Xi|​ 1(qp−ε,qp+ε)​(Xi)​⟶a.s.​𝔼​[|X1|​ 1(qp−ε,qp+ε)​(X1)].\frac{1}{n}\sum\_{i=1}^{n}|X\_{i}|\,\mathds{1}\_{(q\_{p}-\varepsilon\,,\,q\_{p}+\varepsilon)}(X\_{i})\overset{a.s.}{\longrightarrow}\mathbb{E}\left[|X\_{1}|\,\mathds{1}\_{(q\_{p}-\varepsilon\,,\,q\_{p}+\varepsilon)}(X\_{1})\right]. |  |

That is, almost surely, for all ε>0\varepsilon>0, there are some N2ε​(p)>0N\_{2}^{\varepsilon}(p)>0 that for all n≥N2ε​(p)n\geq N\_{2}^{\varepsilon}(p), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Un​(p)−Vn​(p)|\displaystyle|U\_{n}(p)-V\_{n}(p)| | ≤𝔼​[|X1|​ 1(qp−ε,qp+ε)​(X1)]\displaystyle\leq\mathbb{E}\left[|X\_{1}|\,\mathds{1}\_{(q\_{p}-\varepsilon\,,\,q\_{p}+\varepsilon)}(X\_{1})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫−εε|qp−x|⋅f​(qp−x)​𝑑x\displaystyle=\int\_{-\varepsilon}^{\varepsilon}|q\_{p}-x|\cdot f(q\_{p}-x)\,dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​ε​max(−ε,ε)⁡|qp−x|⋅f​(qp−x)\displaystyle\leq 2\varepsilon\max\_{(-\varepsilon,\varepsilon)}|q\_{p}-x|\cdot f(q\_{p}-x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​ε​M,\displaystyle\leq 2\varepsilon M, |  |

where ff is the Radon-Nikodym derivative of FF, i.e., the probability density function of X1X\_{1}. We note, as ff is integrable in an interval (qp−ℓ,qp+ℓ)(q\_{p}-\ell,q\_{p}+\ell) around x=qpx=q\_{p}, we have M=max(−ℓ,ℓ)⁡|qp−x|⋅f​(qp−x)<∞M=\max\_{(-\ell,\ell)}|q\_{p}-x|\cdot f(q\_{p}-x)<\infty. So,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Un​(p)−Vn​(p)|​⟶a.s.​0.|U\_{n}(p)-V\_{n}(p)|\overset{a.s.}{\longrightarrow}0. |  | (4.4) |

Now, ([4.2](https://arxiv.org/html/2511.04784v1#S4.E2 "In 4. Convergence of Tail-Based Statistics")) and ([4.4](https://arxiv.org/html/2511.04784v1#S4.E4 "In 4. Convergence of Tail-Based Statistics")) prove the Theorem since the intersection of two events, each with probability 1, also has probability 1.
∎

###### Corollary 4.2.

By the assumptions and notations of the Lemma [4.1](https://arxiv.org/html/2511.04784v1#S4.Thmdfn1 "Lemma 4.1. ‣ 4. Convergence of Tail-Based Statistics") and its proof, for n→∞n\to\infty we have
Un​(p)=1n​∑i=1nXi​𝟙{Xi≥Qn​(p)}U\_{n}(p)=\frac{1}{n}\sum\_{i=1}^{n}X\_{i}\mathds{1}\_{\{X\_{i}\geq Q\_{n}(p)\}}
is almost surely (a.s.) close to the process
Vn​(p)=1n​∑i=1nXi​𝟙{Xi≥qp}V\_{n}(p)=\frac{1}{n}\sum\_{i=1}^{n}X\_{i}\mathds{1}\_{\{X\_{i}\geq q\_{p}\}}.

Next, we note

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λn​(p)=1n​∑i=1nXi​𝟙{Xi≥Qn​(p)}1n​∑i=1nXi,\Lambda\_{n}(p)=\frac{\frac{1}{n}\sum\_{i=1}^{n}X\_{i}\mathds{1}\_{\{X\_{i}\geq Q\_{n}(p)\}}}{\frac{1}{n}\sum\_{i=1}^{n}X\_{i}}, |  | (4.5) |

and so, we have the following theorem as a straightforward consequence of the Lemma [4.1](https://arxiv.org/html/2511.04784v1#S4.Thmdfn1 "Lemma 4.1. ‣ 4. Convergence of Tail-Based Statistics") and the strong LLN result that
1n​∑i=1nXi​⟶a.s.​μ\frac{1}{n}\sum\_{i=1}^{n}X\_{i}\overset{a.s.}{\longrightarrow}\mu
.

###### Theorem 4.3.

Let X1,X2,…,XnX\_{1},X\_{2},\ldots,X\_{n} be i.i.d random variables with common absolutely continuous distribution FF, and μ=𝔼​[X1]≠0\mu=\mathbb{E}[X\_{1}]\neq 0. Then, for all p∈(0,1)p\in(0,1) that FF is continuous at its ppth quantile qpq\_{p}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λn​(p)​⟶a.s.​aqpμ,\Lambda\_{n}(p)\overset{a.s.}{\longrightarrow}\frac{a\_{q\_{p}}}{\mu}, |  | (4.6) |

where aqp=𝔼​[X1​ 1{X1≥qp}]a\_{q\_{p}}=\mathbb{E}[X\_{1}\,\mathds{1}\_{\{X\_{1}\geq q\_{p}\}}].

## 5. Asymptotic Distribution of Numerator

Considering the explicit form of Λn​(p)\Lambda\_{n}(p) given by equation ([4.5](https://arxiv.org/html/2511.04784v1#S4.E5 "In 4. Convergence of Tail-Based Statistics")), it has a ratio distribution for large n→∞n\to\infty. If {Xi}i≥1\{X\_{i}\}\_{i\geq 1} are i.i.d with 𝔼​[Xi]=μ,𝕍​ar​[Xi]=σ2\mathbb{E}[X\_{i}]=\mu,\mathbb{V}\mathrm{ar}[X\_{i}]=\sigma^{2}, Then, by the central limit theorem (CLT), the denominator of the fraction converges to a normally distributed random variable. That is, for n→∞n\to\infty

|  |  |  |
| --- | --- | --- |
|  | Zn=1n​∑i=1nXi∼𝒩​(μ,σ2/n).Z\_{n}=\frac{1}{n}\sum\_{i=1}^{n}X\_{i}\sim\mathscr{N}(\mu,\sigma^{2}/n). |  |

On the other hand, as {Xi​ 1{Xi≥Qn​(p)}}i≥1\{X\_{i}\,\mathds{1}\_{\{X\_{i}\geq Q\_{n}(p)\}}\}\_{i\geq 1} are not independent random variables, the CLT is not applicable for the asymptotic distribution of the numerator of the fraction
Un​(p)U\_{n}(p),
even though it converges almost surely by the Lemma [4.1](https://arxiv.org/html/2511.04784v1#S4.Thmdfn1 "Lemma 4.1. ‣ 4. Convergence of Tail-Based Statistics"). Considering the literature on ratio distributions and the multiple integral involved in the explicit form of the exact distribution functions, ([(i)](https://arxiv.org/html/2511.04784v1#S3.Ex1 "item (i) ‣ Proposition 3.1. ‣ 3. Exact Distribution of Tail-Based Statistics")) and ([(ii)](https://arxiv.org/html/2511.04784v1#S3.Ex2 "item (ii) ‣ Proposition 3.1. ‣ 3. Exact Distribution of Tail-Based Statistics")), a close form of the Λn​(p)\Lambda\_{n}(p) distribution is so complicated (case-dependent) to characterize in general for large n→∞n\to\infty.

To overcome these difficulties, the asymptotic distribution of Un​(p)U\_{n}(p) is required. To this, we apply the asymptotic distribution of Qn​(p)Q\_{n}(p) and the law of total probability. The asymptotic normality of the distribution of Qn​(p)Q\_{n}(p) for n→∞n\to\infty was investigated by [[51](https://arxiv.org/html/2511.04784v1#bib.bib51), [6](https://arxiv.org/html/2511.04784v1#bib.bib6)]

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qn​(p)∼𝒩​(qp,p​(1−p)n​f2​(qp)),n→∞.Q\_{n}(p)\sim\mathscr{N}\left(q\_{p}\,,\,\frac{p(1-p)}{nf^{2}(q\_{p})}\right),\quad n\to\infty. |  | (5.1) |

So, applying this distribution, one can see

|  |  |  |
| --- | --- | --- |
|  | fQn​(p)​(q)=e−n​f2​(qp)2​p​(1−p)​(q−qp)22​π​p​(1−p)n​f2​(qp)​⟶n→∞​δqp​(q).f\_{Q\_{n}(p)}(q)\;=\;\frac{e^{-\frac{nf^{2}(q\_{p})}{2p(1-p)}(q-q\_{p})^{2}}}{\sqrt{\frac{2\pi p(1-p)}{nf^{2}(q\_{p})}}}\;\underset{n\to\infty}{\longrightarrow}\;\delta\_{q\_{p}}(q). |  |

While there are plenty studies for the ratio distributions of two Gaussian processes, the literatures for those ratios that numerator or denumerator are non-Gaussian are not that rich and also show sevear difficulties to have an explicit form of those ratio distribution. Then, a very straight forward question one may ask that is:

“Does UnU\_{n} have an asymptotic normality in distribution?”

The following theorem reveals a positive response, and the fact behind it.

###### Theorem 5.1.

Let X1,X2,…,XnX\_{1},X\_{2},\ldots,X\_{n} be i.i.d square integrable random variables, i.e., 𝔼​[X12]<∞\mathbb{E}[X\_{1}^{2}]<\infty, with common distribution FF continuous at qpq\_{p}. Then, for n→∞n\to\infty, the process UnU\_{n} admits the asymptotic normal distribution

|  |  |  |  |
| --- | --- | --- | --- |
|  | Un​(p)∼𝒩​(aqp,((bqp+)2+(bqp−)2+2​aqp+​aqp−)/n),U\_{n}(p)\,\sim\,\mathscr{N}\Big(a\_{q\_{p}}\,,\,\Big((b^{+}\_{q\_{p}})^{2}+(b^{-}\_{q\_{p}})^{2}+2a^{+}\_{q\_{p}}a^{-}\_{q\_{p}}\Big)\Big/n\Big), |  | (5.2) |

where aqp+,bqp+a^{+}\_{q\_{p}},b^{+}\_{q\_{p}} are the expectation and standard deviation of Xi+​𝟙{Xi≥qp}X\_{i}^{+}\mathds{1}\_{\{X\_{i}\geq q\_{p}\}}, and aqp−,bqp−a^{-}\_{q\_{p}},b^{-}\_{q\_{p}} are the expectation and standard deviation of Xi−​𝟙{Xi≥qp}X\_{i}^{-}\mathds{1}\_{\{X\_{i}\geq q\_{p}\}}.

###### Proof.

First, considering ([5.1](https://arxiv.org/html/2511.04784v1#S5.E1 "In 5. Asymptotic Distribution of Numerator")), for n→∞n\to\infty there are some rn>0r\_{n}>0 that rn→0r\_{n}\to 0 and

|  |  |  |
| --- | --- | --- |
|  | ℙ​[Qn∈Brn​(qp)]≈1.\mathbb{P}[Q\_{n}\in B\_{r\_{n}}(q\_{p})]\approx 1. |  |

So, for n→∞n\to\infty almost surely

|  |  |  |
| --- | --- | --- |
|  | qp−rn≤Qn≤qp+rn,q\_{p}-r\_{n}\leq Q\_{n}\leq q\_{p}+r\_{n}, |  |

and so,

|  |  |  |
| --- | --- | --- |
|  | 𝟙{Xi≥qp+rn}≤𝟙{Xi≥Qn}≤𝟙{Xi≥qp−rn}.\mathds{1}\_{\{X\_{i}\geq q\_{p}+r\_{n}\}}\leq\mathds{1}\_{\{X\_{i}\geq Q\_{n}\}}\leq\mathds{1}\_{\{X\_{i}\geq q\_{p}-r\_{n}\}}. |  |

Next, we have Xi=Xi+−Xi−X\_{i}=X\_{i}^{+}-X\_{i}^{-} where Xi+=max⁡{Xi,0}X\_{i}^{+}=\max\{X\_{i},0\} and Xi−=max⁡{−Xi,0}X\_{i}^{-}=\max\{-X\_{i},0\}, and also

|  |  |  |
| --- | --- | --- |
|  | Xi+​𝟙{Xi≥qp+rn}≤Xi+​𝟙{Xi≥Qn}≤Xi+​𝟙{Xi≥qp−rn},\displaystyle X\_{i}^{+}\mathds{1}\_{\{X\_{i}\geq q\_{p}+r\_{n}\}}\leq X\_{i}^{+}\mathds{1}\_{\{X\_{i}\geq Q\_{n}\}}\leq X\_{i}^{+}\mathds{1}\_{\{X\_{i}\geq q\_{p}-r\_{n}\}}, |  |
|  |  |  |
| --- | --- | --- |
|  | Xi−​𝟙{Xi≥qp+rn}≤Xi−​𝟙{Xi≥Qn}≤Xi−​𝟙{Xi≥qp−rn}.\displaystyle X\_{i}^{-}\mathds{1}\_{\{X\_{i}\geq q\_{p}+r\_{n}\}}\leq X\_{i}^{-}\mathds{1}\_{\{X\_{i}\geq Q\_{n}\}}\leq X\_{i}^{-}\mathds{1}\_{\{X\_{i}\geq q\_{p}-r\_{n}\}}. |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | Xi+​𝟙{Xi≥qp+rn}−Xi−​𝟙{Xi≥qp−rn}\displaystyle X\_{i}^{+}\mathds{1}\_{\{X\_{i}\geq q\_{p}+r\_{n}\}}-X\_{i}^{-}\mathds{1}\_{\{X\_{i}\geq q\_{p}-r\_{n}\}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Xi​𝟙{Xi≥Qn}=(Xi+−Xi−)​𝟙{Xi≥Qn}\displaystyle\leq X\_{i}\mathds{1}\_{\{X\_{i}\geq Q\_{n}\}}=(X\_{i}^{+}-X\_{i}^{-})\mathds{1}\_{\{X\_{i}\geq Q\_{n}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤Xi+​𝟙{Xi≥qp−rn}−Xi−​𝟙{Xi≥qp+rn},\displaystyle\leq X\_{i}^{+}\mathds{1}\_{\{X\_{i}\geq q\_{p}-r\_{n}\}}-X\_{i}^{-}\mathds{1}\_{\{X\_{i}\geq q\_{p}+r\_{n}\}}, |  | (5.3) |

and so,

|  |  |  |
| --- | --- | --- |
|  | W++​(n)−W−−​(n)≤Un≤W−+​(n)−W+−​(n),W^{+}\_{+}(n)-W^{-}\_{-}(n)\leq U\_{n}\leq W^{+}\_{-}(n)-W^{-}\_{+}(n), |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | W++​(n)\displaystyle W^{+}\_{+}(n) | =1n​∑i=1nXi+​𝟙{Xi≥qp+rn},\displaystyle=\frac{1}{n}\sum\_{i=1}^{n}X\_{i}^{+}\mathds{1}\_{\{X\_{i}\geq q\_{p}+r\_{n}\}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | W−+​(n)\displaystyle W^{+}\_{-}(n) | =1n​∑i=1nXi+​𝟙{Xi≥qp−rn},\displaystyle=\frac{1}{n}\sum\_{i=1}^{n}X\_{i}^{+}\mathds{1}\_{\{X\_{i}\geq q\_{p}-r\_{n}\}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | W+−​(n)\displaystyle W^{-}\_{+}(n) | =1n​∑i=1nXi−​𝟙{Xi≥qp+rn},\displaystyle=\frac{1}{n}\sum\_{i=1}^{n}X\_{i}^{-}\mathds{1}\_{\{X\_{i}\geq q\_{p}+r\_{n}\}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | W−−​(n)\displaystyle W^{-}\_{-}(n) | =1n​∑i=1nXi−​𝟙{Xi≥qp−rn},\displaystyle=\frac{1}{n}\sum\_{i=1}^{n}X\_{i}^{-}\mathds{1}\_{\{X\_{i}\geq q\_{p}-r\_{n}\}}, |  |

are all Gaussian processes. So, the processes Wn:=W++​(n)−W−−​(n)W\_{n}:=W^{+}\_{+}(n)-W^{-}\_{-}(n) and Vn:=W−+​(n)−W+−​(n)V\_{n}:=W^{+}\_{-}(n)-W^{-}\_{+}(n) are also Gaussian and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wn≤Un≤Vn.W\_{n}\leq U\_{n}\leq V\_{n}. |  | (5.4) |

Now,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Wn]\displaystyle\mathbb{E}[W\_{n}] | =𝔼[X1+𝟙{X1≥qp+rn}]−𝔼[X1−𝟙{X1≥qp−rn}]=:a++(n,qp)−a−−(n,qp),\displaystyle=\mathbb{E}[X\_{1}^{+}\mathds{1}\_{\{X\_{1}\geq q\_{p}+r\_{n}\}}]-\mathbb{E}[X\_{1}^{-}\mathds{1}\_{\{X\_{1}\geq q\_{p}-r\_{n}\}}]=:a^{+}\_{+}(n,q\_{p})-a^{-}\_{-}(n,q\_{p}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Vn]\displaystyle\mathbb{E}[V\_{n}] | =𝔼[X1+𝟙{X1≥qp−rn}]−𝔼[X1−𝟙{X1≥qp+rn}]=:a−+(n,qp)−a+−(n,qp),\displaystyle=\mathbb{E}[X\_{1}^{+}\mathds{1}\_{\{X\_{1}\geq q\_{p}-r\_{n}\}}]-\mathbb{E}[X\_{1}^{-}\mathds{1}\_{\{X\_{1}\geq q\_{p}+r\_{n}\}}]=:a^{+}\_{-}(n,q\_{p})-a^{-}\_{+}(n,q\_{p}), |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝕍​ar​[Wn]\displaystyle\mathbb{V}\mathrm{ar}[W\_{n}] | =1n(𝕍ar[X1+𝟙{X1≥qp+rn}]+𝕍ar[X1−𝟙{X1≥qp−rn}]\displaystyle=\frac{1}{n}\Big(\mathbb{V}\mathrm{ar}[X\_{1}^{+}\mathds{1}\_{\{X\_{1}\geq q\_{p}+r\_{n}\}}]+\mathbb{V}\mathrm{ar}[X\_{1}^{-}\mathds{1}\_{\{X\_{1}\geq q\_{p}-r\_{n}\}}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −2ℂov[X1+𝟙{X1≥qp+rn},X1−𝟙{X1≥qp−rn}])\displaystyle\qquad\quad-2\mathbb{C}\mathrm{ov}[X\_{1}^{+}\mathds{1}\_{\{X\_{1}\geq q\_{p}+r\_{n}\}},X\_{1}^{-}\mathds{1}\_{\{X\_{1}\geq q\_{p}-r\_{n}\}}]\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1n​((b++)2​(n,qp)+(b−−)2​(n,qp)+2​a++​(n,qp)​a−−​(n,qp)).\displaystyle=\frac{1}{n}\Big((b^{+}\_{+})^{2}(n,q\_{p})+(b^{-}\_{-})^{2}(n,q\_{p})+2a^{+}\_{+}(n,q\_{p})a^{-}\_{-}(n,q\_{p})\Big). |  |

Similarly,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝕍​ar​[Vn]\displaystyle\mathbb{V}\mathrm{ar}[V\_{n}] | =1n(𝕍ar[X1+𝟙{X1≥qp−rn}]+𝕍ar[X1−𝟙{X1≥qp+rn}]\displaystyle=\frac{1}{n}\Big(\mathbb{V}\mathrm{ar}[X\_{1}^{+}\mathds{1}\_{\{X\_{1}\geq q\_{p}-r\_{n}\}}]+\mathbb{V}\mathrm{ar}[X\_{1}^{-}\mathds{1}\_{\{X\_{1}\geq q\_{p}+r\_{n}\}}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −2ℂov[X1+𝟙{X1≥qp−rn},X1−𝟙{X1≥qp+rn}])\displaystyle\qquad\quad-2\mathbb{C}\mathrm{ov}[X\_{1}^{+}\mathds{1}\_{\{X\_{1}\geq q\_{p}-r\_{n}\}},X\_{1}^{-}\mathds{1}\_{\{X\_{1}\geq q\_{p}+r\_{n}\}}]\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1n​((b−+)2​(n,qp)+(b+−)2​(n,qp)+2​a−+​(n,qp)​a+−​(n,qp)).\displaystyle=\frac{1}{n}\Big((b^{+}\_{-})^{2}(n,q\_{p})+(b^{-}\_{+})^{2}(n,q\_{p})+2a^{+}\_{-}(n,q\_{p})a^{-}\_{+}(n,q\_{p})\Big). |  |

Then, for n→∞n\to\infty

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Wn],𝔼​[Vn]\displaystyle\mathbb{E}[W\_{n}],\mathbb{E}[V\_{n}] | ≈aqp,\displaystyle\approx a\_{q\_{p}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝕍​ar​[Wn],𝕍​ar​[Vn]\displaystyle\mathbb{V}\mathrm{ar}[W\_{n}],\mathbb{V}\mathrm{ar}[V\_{n}] | ≈1n​((bqp+)2+(bqp−)2+2​aqp+​aqp−).\displaystyle\approx\frac{1}{n}\Big((b^{+}\_{q\_{p}})^{2}+(b^{-}\_{q\_{p}})^{2}+2a^{+}\_{q\_{p}}a^{-}\_{q\_{p}}\Big). |  |

These and ([5.4](https://arxiv.org/html/2511.04784v1#S5.E4 "In 5. Asymptotic Distribution of Numerator")) proves this Theorem.
∎

## 6. Asymptotic Distribution of Tail-Based Statistic

The previous section discussed how UnU\_{n} is asymptotically a normal process 𝒩​(μn​(p),σn2​(p)/n)\mathscr{N}(\mu\_{n}(p),\sigma^{2}\_{n}(p)/n), that for known large-size sample distributions we have μn​(p)≈aqp\mu\_{n}(p)\approx a\_{q\_{p}} and σn2​(p)≈(bqp+)2+(bqp−)2+2​aqp+​aqp−\sigma^{2}\_{n}(p)\approx(b^{+}\_{q\_{p}})^{2}+(b^{-}\_{q\_{p}})^{2}+2a^{+}\_{q\_{p}}a^{-}\_{q\_{p}}. Thus, the process Λn\Lambda\_{n} has a ratio distribution of two correlated, noncentral, normally distributed processes, UnU\_{n} and ZnZ\_{n}. Here, we aim to identify this ratio distribution.
The method used in the following lemma was initiated by [[32](https://arxiv.org/html/2511.04784v1#bib.bib32)] and further developed by [[54](https://arxiv.org/html/2511.04784v1#bib.bib54)], who transformed the variables into a ratio of two uncorrelated normal processes with a constant offset. [[30](https://arxiv.org/html/2511.04784v1#bib.bib30)] showed that these ratios can be “almost Gaussian” under certain restrictions, [[27](https://arxiv.org/html/2511.04784v1#bib.bib27)] provided an exact analysis, and [[48](https://arxiv.org/html/2511.04784v1#bib.bib48)] examined them comprehensively. However, their computational combinations and associated complexities must be taken into account. [[32](https://arxiv.org/html/2511.04784v1#bib.bib32)] also developed exact results for the correlated case. By transforming the variables to be uncorrelated, however, one can simply apply Hinkley’s formula rather than resorting to more complicated expressions.

###### Lemma 6.1.

Let X1,X2,…,XnX\_{1},X\_{2},\ldots,X\_{n} be i.i.d square integrable random variables, i.e., 𝔼​[X12]<∞\mathbb{E}[X\_{1}^{2}]<\infty, with common absolutely continuous distribution FF. Then, for n→∞n\to\infty,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Cn​(p)\displaystyle C\_{n}(p) | =ℂ​ov​[Un,Zn]=cn​(p)/n,\displaystyle=\mathbb{C}\mathrm{ov}[U\_{n},Z\_{n}]=c\_{n}(p)/n, |  | (6.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ρn​(p)\displaystyle\rho\_{n}(p) | =ℂ​or​[Un,Zn]=cn​(p)σ⋅σn​(p),\displaystyle=\mathbb{C}\mathrm{or}[U\_{n},Z\_{n}]=\frac{c\_{n}(p)}{\sigma\cdot\sigma\_{n}(p)}, |  | (6.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | cn​(p)\displaystyle c\_{n}(p) | ≈aqp(2)−μ​aqp=bqp2−a~qp​aqp,\displaystyle\approx a^{(2)}\_{q\_{p}}-\mu a\_{q\_{p}}=b^{2}\_{q\_{p}}-\tilde{a}\_{q\_{p}}a\_{q\_{p}}, |  | (6.3) |

where aqp(2)=𝔼​[Xi2​𝟙{Xi≥qp}]a^{(2)}\_{q\_{p}}=\mathbb{E}[X\_{i}^{2}\mathds{1}\_{\{X\_{i}\geq q\_{p}\}}] and a~qp=μ−aqp=𝔼​[Xi​𝟙{Xi≤qp}]\tilde{a}\_{q\_{p}}=\mu-a\_{q\_{p}}=\mathbb{E}[X\_{i}\mathds{1}\_{\{X\_{i}\leq q\_{p}\}}].

###### Proof.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℂ​ov​[Un,Zn]\displaystyle\mathbb{C}\mathrm{ov}[U\_{n},Z\_{n}] | =1n2​ℂ​ov​[∑i=1nXi​𝟙{Xi≥Qn},∑j=1nXj]\displaystyle=\frac{1}{n^{2}}\mathbb{C}\mathrm{ov}\left[\sum\_{i=1}^{n}X\_{i}\mathds{1}\_{\{X\_{i}\geq Q\_{n}\}},\sum\_{j=1}^{n}X\_{j}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1n2​∑i,j=1nℂ​ov​[Xi​𝟙{Xi≥Qn},Xj].\displaystyle=\frac{1}{n^{2}}\sum\_{i,j=1}^{n}\mathbb{C}\mathrm{ov}[X\_{i}\mathds{1}\_{\{X\_{i}\geq Q\_{n}\}},X\_{j}]. |  |

From ([5.3](https://arxiv.org/html/2511.04784v1#S5.E3 "In 5. Asymptotic Distribution of Numerator")) we have

|  |  |  |
| --- | --- | --- |
|  | Xj+​Xi+​𝟙{Xi≥qp+rn}−Xj+​Xi−​𝟙{Xi≥qp−rn}\displaystyle X\_{j}^{+}X\_{i}^{+}\mathds{1}\_{\{X\_{i}\geq q\_{p}+r\_{n}\}}-X\_{j}^{+}X\_{i}^{-}\mathds{1}\_{\{X\_{i}\geq q\_{p}-r\_{n}\}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Xj+​Xi​𝟙{Xi≥Qn}\displaystyle\leq X\_{j}^{+}X\_{i}\mathds{1}\_{\{X\_{i}\geq Q\_{n}\}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Xj+​Xi+​𝟙{Xi≥qp−rn}−Xj+​Xi−​𝟙{Xi≥qp+rn},\displaystyle\leq X\_{j}^{+}X\_{i}^{+}\mathds{1}\_{\{X\_{i}\geq q\_{p}-r\_{n}\}}-X\_{j}^{+}X\_{i}^{-}\mathds{1}\_{\{X\_{i}\geq q\_{p}+r\_{n}\}}, |  |

and also,

|  |  |  |
| --- | --- | --- |
|  | Xj−​Xi+​𝟙{Xi≥qp+rn}−Xj−​Xi−​𝟙{Xi≥qp−rn}\displaystyle X\_{j}^{-}X\_{i}^{+}\mathds{1}\_{\{X\_{i}\geq q\_{p}+r\_{n}\}}-X\_{j}^{-}X\_{i}^{-}\mathds{1}\_{\{X\_{i}\geq q\_{p}-r\_{n}\}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Xj−​Xi​𝟙{Xi≥Qn}\displaystyle\leq X\_{j}^{-}X\_{i}\mathds{1}\_{\{X\_{i}\geq Q\_{n}\}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Xj−​Xi+​𝟙{Xi≥qp−rn}−Xj−​Xi−​𝟙{Xi≥qp+rn}.\displaystyle\leq X\_{j}^{-}X\_{i}^{+}\mathds{1}\_{\{X\_{i}\geq q\_{p}-r\_{n}\}}-X\_{j}^{-}X\_{i}^{-}\mathds{1}\_{\{X\_{i}\geq q\_{p}+r\_{n}\}}. |  |

So,

|  |  |  |
| --- | --- | --- |
|  | Xj+​Xi+​𝟙{Xi≥qp+rn}−Xj+​Xi−​𝟙{Xi≥qp−rn}\displaystyle X\_{j}^{+}X\_{i}^{+}\mathds{1}\_{\{X\_{i}\geq q\_{p}+r\_{n}\}}-X\_{j}^{+}X\_{i}^{-}\mathds{1}\_{\{X\_{i}\geq q\_{p}-r\_{n}\}} |  |
|  |  |  |
| --- | --- | --- |
|  | −Xj−​Xi+​𝟙{Xi≥qp−rn}+Xj−​Xi−​𝟙{Xi≥qp+rn}\displaystyle-X\_{j}^{-}X\_{i}^{+}\mathds{1}\_{\{X\_{i}\geq q\_{p}-r\_{n}\}}+X\_{j}^{-}X\_{i}^{-}\mathds{1}\_{\{X\_{i}\geq q\_{p}+r\_{n}\}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Xj​Xi​𝟙{Xi≥Qn}=(Xj+−Xj−)​Xi​𝟙{Xi≥Qn}\displaystyle\leq X\_{j}X\_{i}\mathds{1}\_{\{X\_{i}\geq Q\_{n}\}}=(X\_{j}^{+}-X\_{j}^{-})X\_{i}\mathds{1}\_{\{X\_{i}\geq Q\_{n}\}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Xj+​Xi+​𝟙{Xi≥qp−rn}−Xj+​Xi−​𝟙{Xi≥qp+rn}\displaystyle\leq X\_{j}^{+}X\_{i}^{+}\mathds{1}\_{\{X\_{i}\geq q\_{p}-r\_{n}\}}-X\_{j}^{+}X\_{i}^{-}\mathds{1}\_{\{X\_{i}\geq q\_{p}+r\_{n}\}} |  |
|  |  |  |
| --- | --- | --- |
|  | −Xj−​Xi+​𝟙{Xi≥qp+rn}+Xj−​Xi−​𝟙{Xi≥qp−rn},\displaystyle-X\_{j}^{-}X\_{i}^{+}\mathds{1}\_{\{X\_{i}\geq q\_{p}+r\_{n}\}}+X\_{j}^{-}X\_{i}^{-}\mathds{1}\_{\{X\_{i}\geq q\_{p}-r\_{n}\}}, |  |

and for n→∞n\to\infty we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Xj​Xi​𝟙{Xi≥Qn}]≈𝔼​[Xj​Xi​𝟙{Xi≥qp}]\displaystyle\mathbb{E}[X\_{j}X\_{i}\mathds{1}\_{\{X\_{i}\geq Q\_{n}\}}]\approx\mathbb{E}[X\_{j}X\_{i}\mathds{1}\_{\{X\_{i}\geq q\_{p}\}}] |  |
|  |  |  |
| --- | --- | --- |
|  | ={𝔼​[Xi2​𝟙{Xi≥qp}]=aqp(2)i=j𝔼​[Xj]​𝔼​[Xi​𝟙{Xi≥qp}]=μ​aqpi≤j.\displaystyle=\begin{cases}\mathbb{E}[X\_{i}^{2}\mathds{1}\_{\{X\_{i}\geq q\_{p}\}}]=a^{(2)}\_{q\_{p}}&i=j\\ \mathbb{E}[X\_{j}]\mathbb{E}[X\_{i}\mathds{1}\_{\{X\_{i}\geq q\_{p}\}}]=\mu a\_{q\_{p}}&i\leq j.\\ \end{cases} |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | ℂ​ov​[Xi​𝟙{Xi≥Qn},Xj]≈{aqp(2)−μ​aqpi=j0i≠j,\displaystyle\mathbb{C}\mathrm{ov}[X\_{i}\mathds{1}\_{\{X\_{i}\geq Q\_{n}\}},X\_{j}]\approx\begin{cases}a^{(2)}\_{q\_{p}}-\mu a\_{q\_{p}}&i=j\\ 0&i\neq j,\\ \end{cases} |  |

and so,

|  |  |  |
| --- | --- | --- |
|  | ℂ​ov​[Un,Zn]=(aqp(2)−μ​aqp)/n.\mathbb{C}\mathrm{ov}[U\_{n},Z\_{n}]=\left(a^{(2)}\_{q\_{p}}-\mu a\_{q\_{p}}\right)\Big/n. |  |

∎

###### Lemma 6.2.

For μ≠0\mu\neq 0, the process

|  |  |  |
| --- | --- | --- |
|  | Λ~n=Λn−cnσ2\widetilde{\Lambda}\_{n}=\Lambda\_{n}-\frac{c\_{n}}{\sigma^{2}} |  |

is a ratio of uncorrelated noncentral Gaussian processes, and has the probability density function

|  |  |  |  |
| --- | --- | --- | --- |
|  | fΛ~n​(t)=\displaystyle f\_{\widetilde{\Lambda}\_{n}}(t)= | n2​π​σ2​σ~n2⋅B~​(t)A~3​(t)⋅exp⁡[−n2⋅μ2σ2⋅(t−μ~n/μ)2t2+σ~n2/σ2]​erf​(B~​(t)A~​(t)​n2)\displaystyle\;\sqrt{\frac{n}{2\pi\sigma^{2}\tilde{\sigma}^{2}\_{n}}}\cdot\frac{\widetilde{B}(t)}{\widetilde{A}^{3}(t)}\cdot\exp\left[{-\frac{n}{2}\cdot\frac{\mu^{2}}{\sigma^{2}}\cdot\frac{\left(t-{\tilde{\mu}\_{n}}/{\mu}\right)^{2}}{t^{2}+{\tilde{\sigma}^{2}\_{n}}/{\sigma^{2}}}}\right]\mathrm{erf}\left(\frac{\widetilde{B}(t)}{\widetilde{A}(t)}\sqrt{\frac{n}{2}}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +e−n2​rn2π​σ​σ~n​A~2​(t),\displaystyle+\frac{e^{-\frac{n}{2}r^{2}\_{n}}}{{\pi\sigma\tilde{\sigma}\_{n}}\widetilde{A}^{2}(t)}, |  | (6.4) |

where

|  |  |  |
| --- | --- | --- |
|  | μ~n=μn−μ​cn/σ2,σ~n=σn2−cn2/σ2,rn2=μ~n2/σ~n2+μ2/σ2\displaystyle\tilde{\mu}\_{n}=\mu\_{n}-\mu c\_{n}/\sigma^{2},\quad\tilde{\sigma}\_{n}=\sqrt{\sigma^{2}\_{n}-c^{2}\_{n}/\sigma^{2}},\quad r^{2}\_{n}=\tilde{\mu}^{2}\_{n}/\tilde{\sigma}^{2}\_{n}+\mu^{2}/\sigma^{2} |  |
|  |  |  |
| --- | --- | --- |
|  | A~​(t)=t2σ~n2+1σ2,B~​(t)=μ~nσ~n2​t+μσ2.\displaystyle\widetilde{A}(t)=\sqrt{\frac{t^{2}}{\tilde{\sigma}^{2}\_{n}}+\frac{1}{\sigma^{2}}},\quad\widetilde{B}(t)=\frac{\tilde{\mu}\_{n}}{\tilde{\sigma}\_{n}^{2}}\,t+\frac{\mu}{\sigma^{2}}. |  |

###### Proof.

We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λn=μn+unμ+zn,\Lambda\_{n}=\frac{\mu\_{n}+u\_{n}}{\mu+z\_{n}}, |  | (6.5) |

where un​(p)u\_{n}(p) and znz\_{n} are corellated central Gaussian variables with variances σn2/n\sigma\_{n}^{2}/n and σ2/n\sigma^{2}/n respectively, and correlation ρn\rho\_{n}. Now, we apply the Geary-Hinkley transformation. Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | u~n\displaystyle\tilde{u}\_{n} | =un−ρu,z​σuσz​zn\displaystyle=u\_{n}-\rho\_{u,z}\frac{\sigma\_{u}}{\sigma\_{z}}z\_{n} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =un−ρn​σnσ​zn\displaystyle=u\_{n}-\rho\_{n}\frac{\sigma\_{n}}{\sigma}z\_{n} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =un−cnσ2​zn,\displaystyle=u\_{n}-\frac{c\_{n}}{\sigma^{2}}z\_{n}, |  |

then u~n\tilde{u}\_{n} and znz\_{n} are uncorrelated, and by

|  |  |  |
| --- | --- | --- |
|  | 𝔼[u~n]=μn−μ⋅cnσ2=:μ~n,\displaystyle\mathbb{E}[\tilde{u}\_{n}]=\mu\_{n}-\mu\cdot\frac{c\_{n}}{\sigma^{2}}=:\tilde{\mu}\_{n}, |  |
|  |  |  |
| --- | --- | --- |
|  | 𝕍ar[u~n]=(σn2−cn2/σ2)/n=:σ~n2/n,\displaystyle\mathbb{V}\mathrm{ar}[\tilde{u}\_{n}]=(\sigma^{2}\_{n}-c^{2}\_{n}/\sigma^{2})/n=:\tilde{\sigma}^{2}\_{n}/n, |  |

we have

|  |  |  |
| --- | --- | --- |
|  | Λn=μ~n+u~nμ+zn+cnσ2.\Lambda\_{n}=\frac{\tilde{\mu}\_{n}+\tilde{u}\_{n}}{\mu+z\_{n}}+\frac{c\_{n}}{\sigma^{2}}. |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | Λ~n=Λn−cnσ2=μ~n+u~nμ+zn,\widetilde{\Lambda}\_{n}=\Lambda\_{n}-\frac{c\_{n}}{\sigma^{2}}=\frac{\tilde{\mu}\_{n}+\tilde{u}\_{n}}{\mu+z\_{n}}, |  |

is a ratio of uncorrelated noncenteral Gaussian process, and so by [[32](https://arxiv.org/html/2511.04784v1#bib.bib32)] has the probability density function

|  |  |  |  |
| --- | --- | --- | --- |
|  | fΛ~n​(t)=n​exp⁡(−R2/2)2​π​σn​σ​a2​(t)​[2​π​b​(t)a​(t)​exp⁡(b2​(t)2​a2​(t))​erf​(b​(t)2​a​(t))+2],f\_{\widetilde{\Lambda}\_{n}}(t)\;=n\,\frac{\exp(-R^{2}/2)}{2\pi\sigma\_{n}\sigma\,a^{2}(t)}\,\left[\sqrt{2\pi}\,\frac{b(t)}{a(t)}\,\exp\left(\frac{b^{2}(t)}{2a^{2}(t)}\right)\mathrm{erf}\left(\frac{b(t)}{\sqrt{2}a(t)}\right)+2\,\right], |  | (6.6) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | R2\displaystyle R^{2} | =n​(μ~n2σ~n2+μ2σ2)=n​rn2,\displaystyle=n\left(\frac{\tilde{\mu}^{2}\_{n}}{\tilde{\sigma}^{2}\_{n}}+\frac{\mu^{2}}{\sigma^{2}}\right)=nr^{2}\_{n}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | a​(t)\displaystyle a(t) | =n​(t2σ~n2+1σ2)=n​A~​(t),\displaystyle=\sqrt{n\left(\frac{t^{2}}{\tilde{\sigma}^{2}\_{n}}+\frac{1}{\sigma^{2}}\right)}=\sqrt{n}\widetilde{A}(t), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | b​(t)\displaystyle b(t) | =n​(μ~nσ~n2​t+μσ2)=n​B~​(t).\displaystyle=n\left(\frac{\tilde{\mu}\_{n}}{\tilde{\sigma}^{2}\_{n}}\,t+\frac{\mu}{\sigma^{2}}\right)=n\widetilde{B}(t). |  |

Finally, since

|  |  |  |
| --- | --- | --- |
|  | 12​(R2−b2​(t)a2​(t))=n2​(R2−B2​(t)A2​(t))=n2⋅μ2σ2⋅(t−μ~n/μ)2t2+σ~n2/σ2,\frac{1}{2}\left(R^{2}-\frac{b^{2}(t)}{a^{2}(t)}\right)=\frac{n}{2}\left(R^{2}-\frac{B^{2}(t)}{A^{2}(t)}\right)=\frac{n}{2}\cdot\frac{\mu^{2}}{\sigma^{2}}\cdot\frac{\left(t-\tilde{\mu}\_{n}/{\mu}\right)^{2}}{t^{2}+{\tilde{\sigma}^{2}\_{n}}/{\sigma^{2}}}, |  |

([6.6](https://arxiv.org/html/2511.04784v1#S6.E6 "In 6. Asymptotic Distribution of Tail-Based Statistic")) results ([6.2](https://arxiv.org/html/2511.04784v1#S6.Ex19 "Lemma 6.2. ‣ 6. Asymptotic Distribution of Tail-Based Statistic")).
∎

Compensating the constant offset −cn/σ2-c\_{n}/\sigma^{2} of the Lemma [6.2](https://arxiv.org/html/2511.04784v1#S6.Thmdfn2 "Lemma 6.2. ‣ 6. Asymptotic Distribution of Tail-Based Statistic"), by changing variable t↦t−cn/σ2t\mapsto t-c\_{n}/\sigma^{2} we have the following theorem.

###### Theorem 6.3.

For μ≠0\mu\neq 0 and n→∞n\to\infty, the (asymptotic) probability density function of Λn\Lambda\_{n} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | fΛn​(t)=\displaystyle f\_{\Lambda\_{n}}(t)= | n2​π​(σ2​σn2−cn2)⋅B​(t)A3​(t)​erf​(B​(t)A​(t)​n2)\displaystyle\;\sqrt{\frac{n}{2\pi(\sigma^{2}\sigma^{2}\_{n}-c\_{n}^{2})}}\cdot\frac{B(t)}{A^{3}(t)}\;\mathrm{erf}\left(\frac{B(t)}{A(t)}\sqrt{\frac{n}{2}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp⁡[−n2⋅μ2σ2⋅(t−μn/μ)2(t−σn/σ)2+2​t​(1−ρn)​σn/σ]\displaystyle\times\exp\left[{-\frac{n}{2}\cdot\frac{\mu^{2}}{\sigma^{2}}\cdot\frac{(t-\mu\_{n}/\mu)^{2}}{(t-\sigma\_{n}/\sigma)^{2}+2t(1-\rho\_{n})\sigma\_{n}/\sigma}}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +e−n2​rn2π​A2​(t)​σ2​σn2−cn2,\displaystyle+\;\frac{e^{-\frac{n}{2}r^{2}\_{n}}}{\pi A^{2}(t)\sqrt{\sigma^{2}\sigma^{2}\_{n}-c^{2}\_{n}}}, |  | (6.7) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(t)\displaystyle A(t) | =(t−cn/σ2)2σn2−cn2/σ2+1σ2,\displaystyle=\sqrt{\frac{(t-c\_{n}/\sigma^{2})^{2}}{\sigma\_{n}^{2}-c\_{n}^{2}/\sigma^{2}}+\frac{1}{\sigma^{2}}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(t)\displaystyle B(t) | =(μn−cn​μ/σ2σn2−cn2/σ2)​(t−cn/σ2)+μσ2,\displaystyle=\left(\frac{\mu\_{n}-c\_{n}\mu/\sigma^{2}}{\sigma\_{n}^{2}-c\_{n}^{2}/\sigma^{2}}\right)(t-c\_{n}/\sigma^{2})\,+\,\frac{\mu}{\sigma^{2}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | rn2\displaystyle r^{2}\_{n} | =(μn−cn​μ/σ2)2σn2−cn2/σ2+μ2σ2.\displaystyle=\frac{(\mu\_{n}-c\_{n}\mu/\sigma^{2})^{2}}{\sigma\_{n}^{2}-c\_{n}^{2}/\sigma^{2}}+\frac{\mu^{2}}{\sigma^{2}}. |  |

###### Proof.

For all T∈ℝT\in\mathbb{R}

|  |  |  |  |
| --- | --- | --- | --- |
|  | FΛn​(T)\displaystyle F\_{\Lambda\_{n}}(T) | =ℙ​[Λn≤T]\displaystyle=\mathbb{P}[\Lambda\_{n}\leq T] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℙ​[Λ~n≤T−cn/σ2]\displaystyle=\mathbb{P}[\widetilde{\Lambda}\_{n}\leq T-c\_{n}/\sigma^{2}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫−∞T−cn/σ2fΛ~n​(u)​𝑑u\displaystyle=\int\_{-\infty}^{T-c\_{n}/\sigma^{2}}f\_{\widetilde{\Lambda}\_{n}}(u)\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫−∞TfΛ~n​(t−cn/σ2)​𝑑t,\displaystyle=\int\_{-\infty}^{T}f\_{\widetilde{\Lambda}\_{n}}(t-c\_{n}/\sigma^{2})\,dt, |  |

and so,

|  |  |  |
| --- | --- | --- |
|  | fΛn​(t)=fΛ~n​(t−cn/σ2),f\_{\Lambda\_{n}}(t)=f\_{\widetilde{\Lambda}\_{n}}(t-c\_{n}/\sigma^{2}), |  |

where fΛ~nf\_{\widetilde{\Lambda}\_{n}} is given by Lemma [6.2](https://arxiv.org/html/2511.04784v1#S6.Thmdfn2 "Lemma 6.2. ‣ 6. Asymptotic Distribution of Tail-Based Statistic"). Now, one may note

|  |  |  |
| --- | --- | --- |
|  | (t−cn/σ2−μ~n/μ)2(t−cn/σ2)2+σ~n2/σ2=(t−μn/μ)2(t−σn/σ)2+2​t​(1−ρn)​σn/σ.\frac{(t-c\_{n}/\sigma^{2}-\tilde{\mu}\_{n}/\mu)^{2}}{(t-c\_{n}/\sigma^{2})^{2}+\tilde{\sigma}^{2}\_{n}/\sigma^{2}}=\frac{(t-\mu\_{n}/\mu)^{2}}{(t-\sigma\_{n}/\sigma)^{2}+2t(1-\rho\_{n})\sigma\_{n}/\sigma}. |  |

∎

There is another approach to investigate the ratio distribution provided by Katz (1978) distribution approximation [[34](https://arxiv.org/html/2511.04784v1#bib.bib34)]. Here, we formulate it for Λn\Lambda\_{n} by the following proposition.

###### Proposition 6.4.

For μ≠0\mu\neq 0 and n→∞n\to\infty, the process Λn\Lambda\_{n} admits the approximatly logarithmic Gaussian distribution

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λn∼μnμ⋅ℒ​o​g​𝒩​o​r​m​a​l​(0,σ2μ2+σn2μn2−2​cnμn​μn).\Lambda\_{n}\sim\frac{\mu\_{n}}{\mu}\cdot\mathscr{L}\!{og}\mathscr{N}\!{ormal}\Bigg(0,\frac{\frac{\sigma^{2}}{\mu^{2}}+\frac{\sigma\_{n}^{2}}{\mu\_{n}^{2}}-\frac{2c\_{n}}{\mu\_{n}\mu}}{n}\Bigg). |  | (6.8) |

###### Proof.

From ([6.5](https://arxiv.org/html/2511.04784v1#S6.E5 "In 6. Asymptotic Distribution of Tail-Based Statistic")) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λn=μnμ⋅1+un/μn1+zn/μ,\Lambda\_{n}=\frac{\mu\_{n}}{\mu}\cdot\frac{1+u\_{n}/\mu\_{n}}{1+z\_{n}/\mu}, |  | (6.9) |

where un∼𝒩​(0,σn2/n)u\_{n}\sim\mathscr{N}(0,\sigma\_{n}^{2}/n) and zn∼𝒩​(0,σ2/n)z\_{n}\sim\mathscr{N}(0,\sigma^{2}/n). Taking the logarithm of ([6.9](https://arxiv.org/html/2511.04784v1#S6.E9 "In 6. Asymptotic Distribution of Tail-Based Statistic")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡Λn=log⁡(μnμ)+log⁡(1+unμn)−log⁡(1+znμ).\log\Lambda\_{n}=\log\left(\frac{\mu\_{n}}{\mu}\right)+\log\left(1+\frac{u\_{n}}{\mu\_{n}}\right)-\log\left(1+\frac{z\_{n}}{\mu}\right). |  | (6.10) |

Here, we apply the logarithmic power series, covergent on |x|<1|x|<1,

|  |  |  |
| --- | --- | --- |
|  | log⁡(1+x)=∑k=0∞(−1)k​xk+1k+1=x−x22+x33−⋯\log(1+x)=\sum\_{k=0}^{\infty}(-1)^{k}\frac{x^{k+1}}{k+1}=x-\frac{x^{2}}{2}+\frac{x^{3}}{3}-\cdots |  |

to approximate the two final part of the right hand side of ([6.10](https://arxiv.org/html/2511.04784v1#S6.E10 "In 6. Asymptotic Distribution of Tail-Based Statistic")). By the first power k=1k=1, for n→∞n\to\infty we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡Λn\displaystyle\log\Lambda\_{n} | ≈log⁡(μnμ)+unμn−znμ\displaystyle\approx\log\left(\frac{\mu\_{n}}{\mu}\right)+\frac{u\_{n}}{\mu\_{n}}-\frac{z\_{n}}{\mu} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∼log⁡(μnμ)+𝒩​(0,σ2μ2+σn2μn2−2​cnμn​μn),\displaystyle\sim\log\left(\frac{\mu\_{n}}{\mu}\right)+\mathscr{N}\Bigg(0,\frac{\frac{\sigma^{2}}{\mu^{2}}+\frac{\sigma\_{n}^{2}}{\mu\_{n}^{2}}-\frac{2c\_{n}}{\mu\_{n}\mu}}{n}\Bigg), |  | (6.11) |

or equivalently

|  |  |  |
| --- | --- | --- |
|  | Λn≈μnμ⋅exp⁡(unμn−znμ),\Lambda\_{n}\approx\frac{\mu\_{n}}{\mu}\cdot\exp\left(\frac{u\_{n}}{\mu\_{n}}-\frac{z\_{n}}{\mu}\right), |  |

and this proves ([6.8](https://arxiv.org/html/2511.04784v1#S6.E8 "In Proposition 6.4. ‣ 6. Asymptotic Distribution of Tail-Based Statistic")).
∎

###### Remark 6.5.

The asymptotic ratio distributions ([6.7](https://arxiv.org/html/2511.04784v1#S6.E7 "In Theorem 6.3. ‣ 6. Asymptotic Distribution of Tail-Based Statistic")) and ([6.8](https://arxiv.org/html/2511.04784v1#S6.E8 "In Proposition 6.4. ‣ 6. Asymptotic Distribution of Tail-Based Statistic")) are indeed usefull when the sample distribution is unknown. However, if the sample distribution is known, then by Theorem [4.3](https://arxiv.org/html/2511.04784v1#S4.Thmdfn3 "Theorem 4.3. ‣ 4. Convergence of Tail-Based Statistics"), Theorem [5.1](https://arxiv.org/html/2511.04784v1#S5.Thmdfn1 "Theorem 5.1. ‣ 5. Asymptotic Distribution of Numerator"), and Lemma [6.1](https://arxiv.org/html/2511.04784v1#S6.Thmdfn1 "Lemma 6.1. ‣ 6. Asymptotic Distribution of Tail-Based Statistic") for n→∞n\to\infty we can apply

|  |  |  |  |
| --- | --- | --- | --- |
|  | μn\displaystyle\mu\_{n} | ≈aqp,\displaystyle\approx a\_{q\_{p}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | σn2\displaystyle\sigma^{2}\_{n} | ≈(bqp+)2+(bqp−)2+2​aqp+​aqp−,\displaystyle\approx(b^{+}\_{q\_{p}})^{2}+(b^{-}\_{q\_{p}})^{2}+2a^{+}\_{q\_{p}}a^{-}\_{q\_{p}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | cn\displaystyle c\_{n} | ≈bqp2−a~qp​aqp,\displaystyle\approx b^{2}\_{q\_{p}}-\tilde{a}\_{q\_{p}}a\_{q\_{p}}, |  |

in ([6.7](https://arxiv.org/html/2511.04784v1#S6.E7 "In Theorem 6.3. ‣ 6. Asymptotic Distribution of Tail-Based Statistic")), and also ([6.8](https://arxiv.org/html/2511.04784v1#S6.E8 "In Proposition 6.4. ‣ 6. Asymptotic Distribution of Tail-Based Statistic")) returns

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λn∼aqpμ⋅ℒ​o​g​𝒩​o​r​m​a​l​(0,σ2μ2+(bqp+)2+(bqp−)2+2​aqp+​aqp−aqp2−2​bqp2−2​a~qp​aqpμ​aqpn).\displaystyle\Lambda\_{n}\sim\frac{a\_{q\_{p}}}{\mu}\cdot\mathscr{L}\!{og}\mathscr{N}\!{ormal}\left(0,\frac{\frac{\sigma^{2}}{\mu^{2}}+\frac{(b^{+}\_{q\_{p}})^{2}+(b^{-}\_{q\_{p}})^{2}+2a^{+}\_{q\_{p}}a^{-}\_{q\_{p}}}{a^{2}\_{q\_{p}}}-\frac{2b^{2}\_{q\_{p}}-2\tilde{a}\_{q\_{p}}a\_{q\_{p}}}{\mu a\_{q\_{p}}}}{n}\right). |  | (6.12) |

## 7. Simulation and Callibration

In this section, we conduct Monte Carlo simulations of the distribution ([6.8](https://arxiv.org/html/2511.04784v1#S6.E8 "In Proposition 6.4. ‣ 6. Asymptotic Distribution of Tail-Based Statistic")) with p=80%p=80\% for n=1000n=1000 i.i.d variables, and N=105N=10^{5} replications, with variables’ common (continuous) distributions

|  |  |  |
| --- | --- | --- |
|  | 𝙽𝚘𝚛𝚖𝚊𝚕​(μ,σ𝟸),𝙻𝚘𝚐𝚗𝚘𝚛𝚖𝚊𝚕​(μ,σ𝟸),𝙴𝚡𝚙𝚘𝚗𝚎𝚗𝚝𝚒𝚊𝚕​(μ),\displaystyle\mathtt{Normal(\mu,\sigma^{2}),Lognormal(\mu,\sigma^{2}),Exponential(\mu),} |  |
|  |  |  |
| --- | --- | --- |
|  | 𝚁𝚊𝚒𝚕𝚎𝚒𝚐𝚑​(𝚋),𝙶𝚎𝚗𝚎𝚛𝚊𝚕𝚒𝚣𝚎𝚍𝙿𝚊𝚛𝚎𝚝𝚘​(𝚔,𝚜,θ),𝙶𝚊𝚖𝚖𝚊​(α,θ),\displaystyle\mathtt{Raileigh(b),GeneralizedPareto(k,s,\theta),Gamma(\alpha,\theta),} |  |

where μ=θ=1,σ=k=b=s=0.25,α=3\mu=\theta=1,\sigma=k=b=s=0.25,\alpha=3, and their practical estimated distribution. To enable a clear comparison between the log-normal formulated density function and the empirically estimated density function, both are plotted on the histogram of the Λn\Lambda\_{n} statistics in Figure [1](https://arxiv.org/html/2511.04784v1#S7.F1 "Figure 1 ‣ 7. Simulation and Callibration"). One can easily observe how closely they approximate the actual density of this statistic, although, due to the sample size and the numbers nn and NN, there are always some differences between the formulated and estimated distributions. The accumulated area between the two curves (which represents the difference in cumulative probability) is reported in Table [1](https://arxiv.org/html/2511.04784v1#S7.T1 "Table 1 ‣ 7. Simulation and Callibration").

![Refer to caption](x1.png)


Figure 1. The histogram, analytical log-normal probability density function, and estimated probability density function of Λn\Lambda\_{n} for i.i.d variables from different continuous distributions.



| Distribution | Area between PDFs |
| --- | --- |
| Normal | 0.0713 |
| LogNormal | 0.0708 |
| Exponential | 0.0662 |
| Rayleigh | 0.0687 |
| Generalized Pareto | 0.0949 |
| Gamma | 0.0709 |

Table 1. Cumulative area between analytic and estimated PDFs for different variable distributions.

## Acknowledgement

The concept of quantile contributions was originally introduced to me by Tommi Sottinen and Klaus Grobys in the context of another study on applied statistics in economics, sincerely grateful to them for their valuable insights and inspiration. Nevertheless, the present work is an independent analytical study, and all parts of the research, analysis, and writing have been carried out solely by the author.

## References

* [1]

  10/90 gap, vol. from the original on January 21, 2021. Retrieved April
  16, 2015., Global Forum for Health Research (Organization), Archive of Global
  Forum for Health Research, 2011.
* [2]

  B. C. Arnold and N. Balakrishnan, Relations, bounds and
  approximations for order statistics, vol. 53, Springer Science & Business
  Media, 2012.
* [3]

  B. C. Arnold, N. Balakrishnan, and H. N. Nagaraja, A first course in
  order statistics, SIAM, 2008.
* [4]

  S. Asmussen, Steady-state properties of GI/G/1, Applied
  probability and Queues, (2003), pp. 266–301.
* [5]

  R. L. Axtell, Zipf distribution of us firm sizes, science, 293
  (2001), pp. 1818–1820.
* [6]

  R. R. Bahadur, A note on quantiles in large samples, The Annals of
  Mathematical Statistics, 37 (1966), pp. 577–580.
* [7]

  A.-L. Barabasi and Z. N. Oltvai, Network biology: understanding the
  cell’s functional organization, Nature reviews genetics, 5 (2004),
  pp. 101–113.
* [8]

  P. Barford, J. Kline, D. Plonka, and A. Ron, A signal analysis of
  network traffic anomalies, in Proceedings of the 2nd ACM SIGCOMM Workshop on
  Internet measurment, 2002, pp. 71–82.
* [9]

  Z. P. Bažant, Scaling theory for quasibrittle structural
  failure, Proceedings of the National Academy of Sciences, 101 (2004),
  pp. 13400–13407.
* [10]

  J. Bentley, Programmimg pearls, Communications of the ACM, 28
  (1985), pp. 896–901.
* [11]

  G. Buzsáki and K. Mizuseki, The log-dynamic brain: how skewed
  distributions affect network operations, Nature Reviews Neuroscience, 15
  (2014), pp. 264–278.
* [12]

  E. Castillo and A. Fernández-Canteli, A general regression model
  for lifetime evaluation and prediction, International Journal of Fracture,
  107 (2001), pp. 117–137.
* [13]

  A. Charles, What is the 1% rule?, The Guardian, July 2006.
* [14]

  V. Chistyakov, A theorem on sums of independent positive random
  variables and its applications to branching random processes, Theory of
  Probability & Its Applications, 9 (1964), pp. 640–648.
* [15]

  A. Clauset, C. R. Shalizi, and M. E. Newman, Power-law distributions
  in empirical data, SIAM review, 51 (2009), pp. 661–703.
* [16]

  R. Cont, Empirical properties of asset returns: stylized facts and
  statistical issues, Quantitative finance, 1 (2001), p. 223.
* [17]

  R. M. Cooke, D. Nieboer, and J. Misiewicz, Fat-Tailed Distributions:
  Data, Diagnostics and Dependence, Volume 1, vol. 1, John Wiley & Sons,
  2014.
* [18]

  M. E. Crovella and A. Bestavros, Self-similarity in world wide web
  traffic: Evidence and possible causes, IEEE/ACM Transactions on networking,
  5 (2002), pp. 835–846.
* [19]

  L. Currat, A. Francisco, S. Al-Tuwaijri, A. Ghaffar, and S. Jupp, 10/90 report on health research 2003-2004, vol. Archived 2015-04-16 at the
  Wayback Machine, WHO Drug Information, 2004.
* [20]

  S. Davey, The 10/90 report on health research 2003-2004., 2004.
* [21]

  A. B. Downey, The structural cause of file size distributions, in
  Proceedings of the 2001 ACM SIGMETRICS international conference on
  Measurement and modeling of computer systems, 2001, pp. 328–329.
* [22]

  L. Doyal, Gender and the 10/90 gap in health research, 2004.
* [23]

  P. Embrechts, C. Klüppelberg, and T. Mikosch, Modelling extremal
  events: for insurance and finance, vol. 33, Springer Science & Business
  Media, 2013.
* [24]

  A. Endo, S. Abbott, A. J. Kucharski, S. Funk, et al., Estimating the
  overdispersion in covid-19 transmission using outbreak sizes outside china,
  Wellcome open research, 5 (2020), p. 67.
* [25]

  V. Fabian and J. Hannan, Introduction to probability and
  mathematical statistics, John Wiley & Sons, 1985.
* [26]

  E. F. Fama, Mandelbrot and the stable paretian hypothesis, The
  journal of business, 36 (1963), pp. 420–429.
* [27]

  E. C. Fieller, The distribution of the index in a normal bivariate
  population, Biometrika, 24 (1932), pp. 428–440.
* [28]

  S. Foss, D. Korshunov, S. Zachary, et al., An introduction to
  heavy-tailed and subexponential distributions, vol. 6, Springer, 2011.
* [29]

  X. Gabaix, Power laws in economics and finance, Annu. Rev. Econ., 1
  (2009), pp. 255–294.
* [30]

  R. C. Geary, The frequency distribution of the quotient of two
  normal variates, Journal of the Royal Statistical Society, 93 (1930),
  pp. 442–446.
* [31]

  M. Harchol-Balter, B. Schroeder, N. Bansal, and M. Agrawal, Size-based scheduling to improve web performance, ACM Transactions on
  Computer Systems (TOCS), 21 (2003), pp. 207–233.
* [32]

  D. V. Hinkley, On the ratio of two correlated normal random
  variables, Biometrika, 56 (1969), pp. 635–639.
* [33]

  H. Jeong, S. P. Mason, A.-L. Barabási, and Z. N. Oltvai, Lethality and centrality in protein networks, Nature, 411 (2001),
  pp. 41–42.
* [34]

  D. Katz, J. Baptista, S. Azen, and M. Pike, Obtaining confidence
  intervals for the risk ratio in cohort studies, Biometrics, (1978),
  pp. 469–474.
* [35]

  W. E. Leland, M. S. Taqqu, W. Willinger, and D. V. Wilson, On the
  self-similar nature of ethernet traffic (extended version), IEEE/ACM
  Transactions on networking, 2 (2002), pp. 1–15.
* [36]

  M. Lin, B. Fan, J. C. Lui, and D.-M. Chiu, Stochastic analysis of
  file-swarming systems, Performance Evaluation, 64 (2007), pp. 856–875.
* [37]

  J. O. Lloyd-Smith, S. J. Schreiber, P. E. Kopp, and W. M. Getz, Superspreading and the effect of individual variation on disease emergence,
  Nature, 438 (2005), pp. 355–359.
* [38]

  T. Lux and M. Marchesi, Scaling and criticality in a stochastic
  multi-agent model of a financial market, Nature, 397 (1999), pp. 498–500.
* [39]

  B. Mandelbrot, The variation of certain speculative prices, The
  Journal of Business, 39 (1963), p. 394–419.
* [40]

  B. B. Mandelbrot and R. L. Hudson, The (mis) behaviour of markets: a
  fractal view of risk, ruin and reward, Profile books, 2010.
* [41]

  M. W. Mantle and R. Lichty, Managing the unmanageable: rules, tools,
  and insights for managing software people and teams, Addison-Wesley, 2012.
* [42]

  R. Metzler and J. Klafter, The random walk’s guide to anomalous
  diffusion: a fractional dynamics approach, Physics reports, 339 (2000),
  pp. 1–77.
* [43]

  D. Middleton, Non-gaussian noise models in signal processing for
  telecommunications: new methods an results for class a and class b noise
  models, IEEE Transactions on information theory, 45 (2002), pp. 1129–1149.
* [44]

  T. Mikosch, Regular variation, subexponentiality and their
  applications in probability theory, (1999).
* [45]

  C. L. Nikias and M. Shao, Signal processing with alpha-stable
  distributions and applications, Wiley-Interscience, 1995.
* [46]

  V. Pareto, Cours d’économie politique, vol. 1, Librairie Droz,
  1964.
* [47]

  V. Paxson and S. Floyd, Wide area traffic: the failure of poisson
  modeling, IEEE/ACM Transactions on networking, 3 (1995), pp. 226–244.
* [48]

  T. Pham-Gia, N. Turkkan, and E. Marchand, Density of the ratio of
  two normal random variables and applications, Communications in
  Statistics-Theory and Methods, 35 (2006), pp. 1569–1591.
* [49]

  R.-D. Reiss, Approximate distributions of order statistics: with
  applications to nonparametric statistics, Springer science & business
  media, 2012.
* [50]

  T. Rolski, H. Schmidli, V. Schmidt, and J. L. Teugels, Stochastic
  processes for insurance and finance, John Wiley & Sons, 2009.
* [51]

  R. J. Serfling, Approximation theorems of mathematical statistics,
  John Wiley & Sons, 2009.
* [52]

  M. F. Shlesinger, G. M. Zaslavsky, and J. Klafter, Strange
  kinetics, Nature, 363 (1993), pp. 31–37.
* [53]

  D. Sornette, Why stock markets crash: critical events in complex
  financial systems, in Why stock markets crash, Princeton university press,
  2009.
* [54]

  M. D. Springer, The algebra of random variables, (1979).
* [55]

  T. Sturgeon, The Claustrophile, Venture: Science fiction
  Magazine, (1956).
* [56]

   , On Hand: A
  book, Venture: Science fiction Magazine, 1 (1957).
* [57]

   , On
  Hand…Offhand: Books, Venture: Science fiction Magazine, 1 (1957).
* [58]

   , Sturgeon’s law,
  Venture Science Fiction, 66 (1958), pp. 2–8.
* [59]

  N. N. Taleb, The Black Swan: The Impact of the Highly Improbable,
  vol. 2, Random house trade paperbacks, 2010.
* [60]

  N. N. Taleb and R. Douady, On the super-additivity and estimation
  biases of quantile contributions, Physica A: Statistical Mechanics and its
  Applications, 429 (2015), pp. 252–260.
* [61]

  T. Van Mierlo et al., The 1% rule in four digital health social
  networks: an observational study, Journal of medical Internet research, 16
  (2014), p. e2966.
* [62]

  D. Vidyasagar, Global notes: the 10/90 gap disparities in global
  health research, Journal of Perinatology, 26 (2006), pp. 55–56.