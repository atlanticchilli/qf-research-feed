---
authors:
- Eckhard Platen
doc_id: arxiv:2602.14575v1
family_id: arxiv:2602.14575
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2602.14575v1
url_html: https://arxiv.org/html/2602.14575v1
venue: arXiv q-fin
version: 1
year: 2026
---

Information-Theoretic Approach to
  
 Financial Market Modelling

Eckhard
Platen111University of Technology Sydney,
School of Mathematical and Physical Sciences, and 
  
Finance Discipline Group,

The paper treats the financial market as a communication system, using four information-theoretic assumptions to derive an idealized model with only one parameter. State variables are scalar stationary diffusions. The model minimizes the surprisal of the market and the Kullback-Leibler divergence between the benchmark-neutral pricing measure and the real-world probability measure. The state variables, their sums, and the growth optimal portfolio of the stocks evolve as squared radial Ornstein-Uhlenbeck processes in respective activity times.

JEL Classification: G10, G11

Mathematics Subject Classification: 62P05, 60G35, 62P20

Key words and phrases: growth optimal portfolio, communication system, surprisal, information minimization, squared radial Ornstein-Uhlenbeck process.

Acknowledgements: The author would like to express his gratitude for
receiving valuable suggestions on the paper by Yacine Ait-Sahalia, Mark Craddock, Kevin Fergusson, Len Garces, Martino Grasselli, Matheus Grasselli, Juri Hinz, Hardy Hulley, Sebastien Lleo, Erik Schloegl, Thorsten Schmidt, Michael Schmutz, Martin Schweizer, Stefan Tappe, and three referees.

## 1 Introduction

The Fundamental Theorem of Asset Pricing, derived by ?), forms the basis of modern financial mathematics, as presented, e.g., by ?). It states that the widely applied method of risk-neutral pricing is equivalent to the absence of free lunches with vanishing risk (FLVRs). ?) showed that the absence of FLVRs in real markets is not supported at a high significance level. This prompts reconsideration of financial market models to allow FLVRs and provide a sound, practical pricing method.

The benchmark approach provides a modelling framework where FLVRs can exist; see, e.g., ?) and ?). Benchmark-neutral pricing, introduced in ?), uses the stocks’ growth optimal portfolio (GOP) as numéraire and offers a practical, theory-based pricing approach. Developing related quantitative methods requires a financial market model that captures empirical facts and enables precise contingent claim hedging.

The following key stylized empirical facts should be incorporated into any model aiming to accurately reflect financial markets:

1. Stock market index volatilities tend to follow processes with stationary probability densities, as demonstrated in ?).

2. The log-return distributions of stock market indices closely approximate a Student-t distribution with four degrees of freedom across various statistical methodologies, as shown in ?), ?), ?), and ?).
  
  
3. Stock market indices display the leverage effect: declines in the index are associated with increased volatility, and vice versa; see ?), ?), and ?).
  
  
4. Volatility exhibits clustering and rough sample paths, including occasional spikes that differ from typical diffusion processes over calendar time, as discussed by ?), and ?).
  
  
5. Volatility comprises both rapidly and slowly changing components; see ?).
  
  
6. Log-returns of major indices exhibit scaling properties and self-similarity, as evidenced by ?) and ?).
  
  
7. Over extended periods, the logarithm of world stock market indices demonstrates approximately linear growth with mean-reverting characteristics, exemplified by the logarithm of the MSCI World total return stock index (MSCI) shown in Figure [4.1](https://arxiv.org/html/2602.14575v1#S4.F1 "Figure 4.1 ‣ 4.4 Ilustrations ‣ 4 Information-Minimized Market").
  
  
A ‘realistic’ financial market model, as referenced in this paper, should provide robust explanations for these observed empirical phenomena.

This paper explores a novel interpretation of the financial market, viewing it as a communication system. By integrating information-theoretical principles in the modelling, an idealized market model is developed based on four fundamental assumptions. These assumptions serve as the foundation for a rigorous and structured approach to understanding market dynamics. To ensure analytical tractability, the state variables within the market are represented as scalar stationary diffusions. This choice enables a manageable yet robust framework for analyzing the evolution and behaviour of these variables over time.

The existence of the growth optimal portfolio (GOP) is assumed, providing a benchmark for portfolio performance. The GOP of a market is interchangeably called the Kelly portfolio, expected logarithmic utility-maximizing portfolio, or numéraire portfolio;
see, e.g., ?), ?), ?), ?), ?), ?), ?), and ?). ?) identified the GOP in gambling using Shannon’s information theory, marking the discovery of the GOP.

The expected information content, specifically the surprisal of the stationary densities of the state variables, is minimized. This approach seeks the most efficient encoding of market information with the release of the minimal possible expected information content through traded prices.
  
The benchmark-neutral pricing measure is in ?) proposed to replace the putative risk-neutral pricing measure. The Kullback-Leibler divergence between the benchmark-neutral pricing measure and the real-world probability measure is also minimized. This ensures that the pricing density remains as close as possible to observed market probabilities, maintaining both realism and theoretical soundness when pricing contingent claims.

The framework that emerges from these information-minimization criteria yields a distinct idealized financial market model, which is called minimal market model (MMM). It extends the similarly named model proposed in ?) for the dynamics of a GOP. The paper will show, under the MMM, the state variables, their aggregated sums, and the GOP of the stocks all evolve according to squared radial Ornstein-Uhlenbeck (SROU) processes as studied in ?), each within their respective activity times. This result encapsulates the dynamic behaviour of both individual and collective market components within an information-theoretic modelling context.

The properties of the proposed model will be derived endogenously. The model will be parsimonious with only one parameter and a minimum number of driving Brownian motions. It will facilitate the design of extremely accurate hedging methods. The modelling of the complex stochastic dynamical system represented by the financial market is significantly simplified by modelling its state variables, the normalized factors, as independent scalar diffusion processes with stationary probability densities.
  
Since stocks are securities that are driven by several sources of randomness, it is not ideal to employ these as the stochastic basis of a financial market model. Instead, the paper models stocks as portfolios of independent auxiliary securities, the factors, which form the theoretical stochastic basis of the market. A factor is assumed to represent a portfolio of stocks. It is modelled as the product of an exponential function of time and an independent state variable, the normalized factor. By construction, the volatilities of the normalized factors are stationary processes and equal to those of the respective factors. All securities are denominated in units of the savings account, which is added as a security to the factors to form the extended market so that the interest rate does not need to be modelled.

The extended market is assumed to permit continuous trading, instantaneous investing and borrowing, short sales with full use of proceeds, infinitely divisible securities, and no transaction costs.
For the extended market, the modelling challenge is reduced to the question, which independent stationary scalar diffusions should model the normalized factors. To answer this question,
the paper optimizes
suitable Lagrangians that capture mathematically the principle driving the market’s dynamics, which is the minimization of expected information content, the, so called, surprisal.
To capture this principle, the
paper interprets the market as a communication system in the sense of ?), where the expected information content is minimized.
This identifies the optimal stationary probability densities of the normalized factors.

The fact that information-theoretical concepts are particularly pertinent to the field of finance can be explained as follows: The trades reveal with their prices information. The average speed of the information flow is measured by the average trading intensity, which the paper models by the market activity. The integrated market activity is called the market time. At certain periods, the market moves rather fast and at other periods more slowly. One notices that the market activity represents a fast moving process because particular information can trigger enormous trading activity in a very short time. Important is the fact that the market participants observe the market evolution in calendar time. When observing the volatility of a stock market index in calendar time during a period of high market activity, one observes volatility spikes, which a diffusion that is evolving in calendar time cannot generate. The paper assumes that the market is moving in a common market time that moves faster at major market movements. However, the state variables, which are the normalized factors, move in market time as scalar diffusions. This separates the modelling of the fast moving market activity from that of the in market time as diffusions evolving normalized factors. The market activity or speed of the information flow can be measured by the average trading intensity. The modelling of the market activity is beyond the scope of the current paper and suggested to be modelled similarly as proposed in ?). This leads to the first fundamental assumption of the paper:

A1:
The normalized factors evolve as independent, stationary scalar diffusions in market time, which is the integrated average trading intensity.

The existence of the GOP can be interpreted as a no-arbitrage condition because ?)
have shown that the existence of the GOP is equivalent to their No Unbounded Profit with Bounded Risk (NUPBR) condition. This no-arbitrage condition is weaker than the no Free Lunch with Vanishing Risk (FLVR) condition of ?). The assumption about the existence of the GOP is an extremely weak condition. When violated, the respective growth rate maximization would have no solution and the candidate for the GOP would reach infinite values in finite time, which is not a financial market that the current paper aims to model.
This leads to the second fundamental assumption of the paper:

A2:
The market’s GOP and a
unique, strong solution of the system of SDEs, characterizing the market’s normalized factor dynamics, exist.

By maximizing the instantaneous growth rate of portfolios of factors when forming the GOP of factors, which is called the benchmark, a first Lagrangian comes into play. The Assumption A2 requires the GOP of the entire market to exist, which is called numéraire portfolio (NP) and was named by ?). By maximizing the growth rate of all admissible portfolios in the market, a second Lagrangian emerges in the modelling.

The trades disclose price information. The stationary joint probability density of the normalized factors quantifies the probabilistic nature of the prices. When the surprisal, as defined in ?), is minimized, the probability densities are so that all price-relevant expected information content that could be removed by the buyer and seller in a trade has been removed under the given constraints. This leads to the third Lagrangian and the third fundamental assumption of the paper:

A3:
The surprisal, which is the expected information content of the stationary joint probability density of the normalized factors, is minimized.

The paper calls an extended market a surprisal-minimized market when the above three assumptions are satisfied. As an alternative and practicable pricing method to risk-neutral pricing, benchmark-neutral (BN) pricing has been proposed in ?), which employs as its numéraire the benchmark that equals the GOP of the factors. Buyers and sellers of contingent claims have an interest to minimize the increase of the expected information content caused by the pricing density they use.
The derivative of the Kullback-Leibler divergence, as defined in ?), of the BN pricing measure from the real-world probability measure quantifies the increase of expected information content as the result of BN pricing. Under the first three assumptions, the latter will be shown to be the only practicable pricing method that is applicable for all admissible contingent claims. This identifies the fourth Lagrangian and leads to the formulation of the fourth fundamental assumption of the paper:

A4:
The Kullback-Leibler divergence of the benchmark-neutral pricing measure from the real-world probability measure is minimized.

We call an extended market an information-minimized market when the four assumptions are satisfied by its dynamics.
The paper will show that the above four assumptions lead to an idealized financial market model that is ‘realistic’ in the sense that it generates the empirical facts previously listed. As indicated earlier, the derived idealized information-minimized financial market model is called minimal market model (MMM). The MMM has only one constant parameter when viewed in market time, which is the net risk-adjusted return. This parameter is not needed when applying benchmark-neutral pricing under the MMM. The observable market time is the only input that is required for the pricing and hedging of a wide range of contingent claims expressed in terms of the market time.
  
Under the BN pricing measure, the factors, sums of factors and the benchmark follow squared Bessel processes that evolve in respective observable activity times. Squared Bessel processes are special squared radial Ornstein-Uhlenbeck (SROU) processes, which are studied, e.g., in ?) and ?). They are generalizations of the CIR process, which was popularized in finance in ?). These processes are highly tractable with many explicit formulas for their functionals; see, e.g., ?).

The paper is organized as follows: Section 2 introduces the extended market of factors. Section 3 minimizes the surprisal of the stationary densities of the normalized factors. Section 4 minimizes the Kullback-Leibler divergence of the BN pricing measure from the real-world probability measure, which reveals the MMM.
Five appendices prove the theorems of the paper.

## 2 Market of Factors

### 2.1 Factors

Under Assumption A1, the nondecreasing market time τt\tau\_{t} evolves with respect to the calendar time t∈[t0,∞)t\in[t\_{0},\infty).
The modelling is performed on a filtered probability space (Ω,ℱ,ℱ¯,P)(\Omega,\mathcal{F},\underline{\cal{F}},P) in market time, satisfying the usual conditions; see, e.g.,
?). The filtration ℱ¯\underline{\cal{F}} =(ℱτ)τ∈[τt0,∞)=(\mathcal{F}\_{\tau})\_{\tau\in[\tau\_{t\_{0}},\infty)} models the evolution of all events relevant to the modelling.
  
The securities are denominated in units of the savings account Sτ0≡1S^{0}\_{\tau}\equiv 1 and specify n∈{1,2,…}n\in\{1,2,...\} stocks Aτ1,…,AτnA^{1}\_{\tau},...,A^{n}\_{\tau} as the risky primary security accounts. The stocks reinvest all dividends or other payments and expenses. The nn stocks are assumed to represent self-financing portfolios of the
nn independent factors Sτ1,…,SτnS^{1}\_{\tau},...,S^{n}\_{\tau} at the market time τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty). The kk-th factor SτkS^{k}\_{\tau}, k∈{1,…,n}k\in\{1,...,n\}, is assumed to be driven by the kk-th Brownian motion WτkW^{k}\_{\tau}. The nn independent driving Brownian motions Wτ1,…,WτnW^{1}\_{\tau},...,W^{n}\_{\tau} evolve in market time τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty) under the real-world probability measure PP, where the filtration generated by the Brownian motions is a subfiltration of the given filtration ℱ¯\underline{\cal{F}}.

The factors are independent, nonnegative auxiliary securities that form the stochastic basis of the market. We assume that each factor can be formed as a self-financing portfolio of the stocks, that is, we have the stochastic differential equation (SDE)

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​SτjSτj=∑k=1npτk,j​d​AτkAτk\frac{dS^{j}\_{\tau}}{S^{j}\_{\tau}}=\sum\_{k=1}^{n}p^{k,j}\_{\tau}\frac{dA^{k}\_{\tau}}{A^{k}\_{\tau}} |  | (2.1) |

with initial value Sτt0j>0S^{j}\_{\tau\_{t\_{0}}}>0, where the weights pτj,1,…,pτj,np^{j,1}\_{\tau},...,p^{j,n}\_{\tau} form predictable, square integrable processes for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty) and j∈{1,…,n}j\in\{1,...,n\}.

Under Assumption A2, the market formed by the nn factors has a growth optimal portfolio (GOP), which we call the benchmark and denote by Sτ∗S^{\*}\_{\tau} at the market time τ\tau. Since the set of portfolios that can be formed by the factors and those that can be formed by the stocks are assumed to be the same, it follows by Theorem 3.1 in ?) that the benchmark is also the GOP of the market formed by the stocks. The market formed by the factors has, by construction, no locally riskfree portfolio (LRP), which is a portfolio with zero volatility.
  
Theorem 3.1 in ?) reveals the general structure of a financial market with continuous securities that has a GOP and no LRP, which determines the structure of the market of factors.
The most striking structural property of this market is the existence of a unique net risk-adjusted return λ^τ\hat{\lambda}\_{\tau}, which emerges as the Lagrange multiplier of the growth rate maximization that identifies the benchmark Sτ∗S^{\*}\_{\tau}.
The net risk-adjusted return λ^τ\hat{\lambda}\_{\tau} is assumed to represent an adapted, square integrable process.
  
We assume for k∈{1,…,n}k\in\{1,...,n\} the kk-th factor process
Sk={Sτk,τ∈[τt0,∞)}S^{k}=\{S^{k}\_{\tau},\tau\in[\tau\_{t\_{0}},\infty)\} to satisfy the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​SτkSτk=λ^τ​d​τ+βτk​(βτk​ωk​d​τ+d​Wτk)\frac{dS^{k}\_{\tau}}{S^{k}\_{\tau}}=\hat{\lambda}\_{\tau}d\tau+\beta^{k}\_{\tau}(\beta^{k}\_{\tau}\omega^{k}d\tau+dW^{k}\_{\tau}) |  | (2.2) |

for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty) with strictly positive ℱτt0\mathcal{F}\_{\tau\_{t\_{0}}}-measurable, random initial kk-th factor value Sτt0k>0S^{k}\_{\tau\_{t\_{0}}}>0. The value of a factor may approach zero, at which instance it is assumed to be instantaneously reflected. For each independent driving Brownian motion WτkW^{k}\_{\tau}, k∈{1,…,n}k\in\{1,...,n\}, the respective kk-th factor volatility  is denoted by βτk\beta^{k}\_{\tau} and the respective risk premium parameter by ωk>0\omega^{k}>0. The volatility with respect to market time is assumed to represent a flexible, continuous, strictly positive, adapted, square integrable process in market time. The expected rate of return λ^τ+(βτk)2​ωk\hat{\lambda}\_{\tau}+(\beta^{k}\_{\tau})^{2}\omega^{k} is flexible because it is formed by the sum of the net risk-adjusted return and the product of the flexible kk-th risk premium parameter and the squared kk-th factor volatility.

### 2.2 Benchmark

Let us denote by βτ\beta\_{\tau} the diagonal matrix with the factor volatilities at its diagonal and zeros at all off-diagonal elements. Furthermore, we denote by ω=(ω1,…,ωn)⊤{\bf\omega}=(\omega^{1},...,\omega^{n})^{\top} the vector of the risk premium parameters. This allows us to write the SDE for the vector of factors 𝐒τ=(Sτ1,…,Sτn)⊤{\bf{S}}\_{\tau}=(S^{1}\_{\tau},...,S^{n}\_{\tau})^{\top} in the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​𝐒τ𝐒τ=λ^τ​𝟏​d​τ+βτ​(βτ​ω​d​τ+d​𝐖τ)\frac{d{\bf{S}}\_{\tau}}{{\bf{S}}\_{\tau}}=\hat{\lambda}\_{\tau}{\bf{1}}d\tau+\beta\_{\tau}(\beta\_{\tau}\omega d\tau+d{\bf{W}}\_{\tau}) |  | (2.3) |

with the vector of strictly positive initial values 𝐒τt0{\bf{S}}\_{\tau\_{t\_{0}}} and the vector process 𝐖={𝐖τ=(Wτ1,…,Wτn)⊤,τ∈[τt0,∞)}{\bf{W}}=\{{\bf{W}}\_{\tau}=(W^{1}\_{\tau},\dots,W^{n}\_{\tau})^{\top},\tau\in[\tau\_{t\_{0}},\infty)\} of the nn independent driving Brownian motions.
Here we write d​𝐒τ𝐒τ\frac{d{\bf{S}}\_{\tau}}{{\bf{S}}\_{\tau}} for the nn-vector of stochastic differentials (d​Sτ1Sτ1,…,d​SτnSτn)⊤(\frac{dS^{1}\_{\tau}}{S^{1}\_{\tau}},...,\frac{dS^{n}\_{\tau}}{S^{n}\_{\tau}})^{\top}.
By application of the Itô formula one obtains for a self-financing portfolio SτπS^{\pi}\_{\tau} of factors with weight vector πτ=(πτ1,…,πτn)⊤{\pi\_{\tau}}=(\pi^{1}\_{\tau},...,\pi^{n}\_{\tau})^{\top} the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​SτπSτπ=πτ⊤​d​𝐒τ𝐒τ\frac{dS^{\pi}\_{\tau}}{S^{\pi}\_{\tau}}=\pi\_{\tau}^{\top}\frac{d{\bf{S}}\_{\tau}}{{\bf{S}}\_{\tau}} |  | (2.4) |

and the instantaneous growth rate

|  |  |  |  |
| --- | --- | --- | --- |
|  | gτπ=λ^τ+(πτ)⊤​βτ​βτ​(ω−12​πτ)g^{\pi}\_{\tau}=\hat{\lambda}\_{\tau}+({\pi}\_{\tau})^{\top}\beta\_{\tau}\beta\_{\tau}\left(\omega-\frac{1}{2}\pi\_{\tau}\right) |  | (2.5) |

as the drift of the SDE of its logarithm for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty). The benchmark Sτ∗S^{\*}\_{\tau} is the portfolio that maximizes this growth rate, which involves the first Lagrangian and is defined as follows:

###### Definition 2.1

The benchmark Sτ∗S^{\*}\_{\tau} is the strictly positive portfolio of factors with maximum instantaneous growth rate gτπg^{\pi}\_{\tau} and initial value Sτt0∗>0S^{\*}\_{\tau\_{t\_{0}}}>0, where its weight vector πτ∗=(πτ∗,1,…,πτ∗,n)⊤{\pi^{\*}\_{\tau}}=(\pi^{\*,1}\_{\tau},...,\pi^{\*,n}\_{\tau})^{\top}
is a solution of the well-posed nn-dimensional constrained quadratic maximization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡{gτπ|πτ∈𝐑n,πτ⊤​𝟏=1},\max\left\{g^{\pi}\_{\tau}|\pi\_{\tau}\in{\bf R}^{n},\pi\_{\tau}^{\top}{\bf 1}=1\right\}, |  | (2.6) |

for all τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty).

Note that the above portfolios of factors do not invest in the LRP, which is the savings account. The following properties of the benchmark are derived in Appendix A:

###### Theorem 2.2

For a market of factors and τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty),
the sum of the risk premium parameters is conserved and equals the constant 11, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ω⊤​𝟏=1.\omega^{\top}{\bf{1}}=1. |  | (2.7) |

When constructing the benchmark, the vector of weights assigned to the factors corresponds to the vector of risk premium parameters

|  |  |  |  |
| --- | --- | --- | --- |
|  | πτ∗=ω\pi^{\*}\_{\tau}=\omega |  | (2.8) |

and the benchmark satisfies the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sτ∗Sτ∗=λ^τ​d​τ+(βτ​ω)⊤​(βτ​ω​d​τ+d​𝐖τ)\frac{dS^{\*}\_{\tau}}{S^{\*}\_{\tau}}=\hat{\lambda}\_{\tau}d\tau+(\beta\_{\tau}\omega)^{\top}(\beta\_{\tau}\omega d\tau+d{\bf{W}}\_{\tau}) |  | (2.9) |

for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty) with Sτt0∗>0S^{\*}\_{\tau\_{t\_{0}}}>0.

By Equation ([2.7](https://arxiv.org/html/2602.14575v1#S2.E7 "In Theorem 2.2 ‣ 2.2 Benchmark ‣ 2 Market of Factors")), the above theorem reveals the important property that the sum of the risk premium parameters is a conserved quantity and equals 11. For the case when the risk premium parameters would be predictable, square integrable processes, the respective proof of the above theorem does still work, the risk premium factors would still add up to one, and these would still represent the weights for the benchmark.

### 2.3 Numéraire Portfolio

The savings account denominated savings account Sτ0≡1S^{0}\_{\tau}\equiv 1 equals the constant 11
for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty).
Let us extend the market of factors by adding the savings account Sτ0≡1S^{0}\_{\tau}\equiv 1 to the factors 𝐒τ=(Sτ1,…,Sτn)⊤{\bf{S}}\_{\tau}=(S^{1}\_{\tau},...,S^{n}\_{\tau})^{\top}. In the extended market one can form self-financing portfolios by combining the n+1n+1 securities Sτ0,…,SτnS^{0}\_{\tau},...,S^{n}\_{\tau}. A positive self-financing portfolio SτπS^{\pi}\_{\tau} in the extended market is described by its initial value Sτt0π>0S^{\pi}\_{\tau\_{t\_{0}}}>0 and its risky security weights πτ=(πτ1,…,πτn)⊤\pi\_{\tau}=({\pi}^{1}\_{\tau},...,{\pi}^{n}\_{\tau})^{\top}, where the savings account weight equals

|  |  |  |  |
| --- | --- | --- | --- |
|  | πτ0=1−πτ⊤​𝟏\pi^{0}\_{\tau}=1-\pi^{\top}\_{\tau}{\bf{1}} |  | (2.10) |

for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty).
The portfolio SτπS^{\pi}\_{\tau} satisfies the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​SτπSτπ=πτ⊤​d​𝐒τ𝐒τ,\frac{dS^{\pi}\_{\tau}}{S^{\pi}\_{\tau}}=\pi\_{\tau}^{\top}\frac{d{\bf{S}}\_{\tau}}{{\bf{S}}\_{\tau}}, |  | (2.11) |

and its instantaneous growth rate, the drift of its logarithm, is of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | gτπ=πτ⊤​𝟏​λ^τ+(πτ)⊤​βτ​βτ​(ω−12​πτ)g^{\pi}\_{\tau}=\pi^{\top}\_{\tau}{\bf{1}}\hat{\lambda}\_{\tau}+({\pi}\_{\tau})^{\top}\beta\_{\tau}\beta\_{\tau}(\omega-\frac{1}{2}\pi\_{\tau}) |  | (2.12) |

for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty).

?) introduced the numéraire portfolio (NP) as a general market notion for the GOP of the extended market, showing that risk-neutral prices can be derived using the NP as numeraire and the real-world probability measure PP as pricing measure, which requires an equivalent risk-neutral measure.
The benchmark approach emphasizes that only the existence of the NP is needed to compute minimal prices for replicable contingent claims. ?) showed that the existence of the NP is equivalent to their NUPBR condition. In analogy to Definition [2.1](https://arxiv.org/html/2602.14575v1#S2.Thmtheorem1 "Definition 2.1 ‣ 2.2 Benchmark ‣ 2 Market of Factors"), and assuming A 2, the second Lagrangian is then relevant, leading to the following concept:

###### Definition 2.3

For the extended market, the NP Sτ∗∗S^{\*\*}\_{\tau} is the positive portfolio of the savings account and the factors with maximum instantaneous growth rate gτπ∗∗g^{\pi^{\*\*}}\_{\tau} and initial value Sτt0∗∗>0S^{\*\*}\_{\tau\_{t\_{0}}}>0, where its weight vector (πτ∗∗,0,πτ∗∗,1,…,πτ∗∗,n)⊤=(πτ∗∗,0,πτ∗∗⊤)(\pi^{\*\*,0}\_{\tau},\pi^{\*\*,1}\_{\tau},...,\\
\pi^{\*\*,n}\_{\tau})^{\top}=(\pi^{\*\*,0}\_{\tau},{\pi^{\*\*}\_{\tau}}^{\top})
is a solution of the well-posed (n+1)(n+1)-dimensional constrained quadratic maximization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡{gτπ|(πτ0,πτ⊤)⊤∈𝐑n+1,πτ0+πτ⊤​𝟏=1},\max\left\{g^{\pi}\_{\tau}|(\pi^{0}\_{\tau},\pi^{\top}\_{\tau})^{\top}\in{\bf R}^{n+1},\pi^{0}\_{\tau}+\pi\_{\tau}^{\top}{\bf 1}=1\right\}, |  | (2.13) |

for all τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty).

Under the Assumption A2, the existence of the NP is secured and the following result derived in Appendix B:

###### Theorem 2.4

For the given extended market, the NP Sτ∗∗S^{\*\*}\_{\tau} satisfies the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sτ∗∗Sτ∗∗=θτ∗∗⊤​(θτ∗∗​d​τ+d​𝐖τ)\frac{dS^{\*\*}\_{\tau}}{S^{\*\*}\_{\tau}}={\theta^{\*\*}\_{\tau}}^{\top}(\theta^{\*\*}\_{\tau}d\tau+d{\bf W}\_{\tau}) |  | (2.14) |

with initial value Sτt0∗∗>0S^{\*\*}\_{\tau\_{t\_{0}}}>0, market price of risk vector

|  |  |  |  |
| --- | --- | --- | --- |
|  | θτ∗∗=λ^τ​βτ−1​𝟏+βτ​ω,\theta^{\*\*}\_{\tau}=\hat{\lambda}\_{\tau}\beta\_{\tau}^{-1}{\bf{1}}+\beta\_{\tau}\omega, |  | (2.15) |

the NP
weights

|  |  |  |  |
| --- | --- | --- | --- |
|  | πτ∗∗=(πτ∗∗,1,…,πτ∗∗,n)⊤=λ^τ​βτ−2​𝟏+ω,\pi^{\*\*}\_{\tau}=(\pi^{\*\*,1}\_{\tau},...,\pi^{\*\*,n}\_{\tau})^{\top}=\hat{\lambda}\_{\tau}\beta\_{\tau}^{-2}{\bf{1}}+\omega, |  | (2.16) |

to be invested in the factors Sτ1,…,SτnS^{1}\_{\tau},...,S^{n}\_{\tau}, and the weight

|  |  |  |  |
| --- | --- | --- | --- |
|  | πτ∗∗,0=−λ^τ​𝟏⊤​βτ−2​𝟏\pi^{\*\*,0}\_{\tau}=-\hat{\lambda}\_{\tau}{\bf{1}}^{\top}\beta\_{\tau}^{-2}{\bf{1}} |  | (2.17) |

to be invested in the savings account Sτ0S^{0}\_{\tau}
for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty).

The flexibility of factor volatilities and risk premium parameters, along with Theorem 3.1 in ?), ensures a broad set of continuous market dynamics can be described using the extended market model, including stocks formed as portfolios of factors. The theorem remains valid when risk premium parameters are predictable, square-integrable processes.

## 3 Surprisal-Minimized Market

### 3.1 Normalized Factors

By applying the Assumption A2, we characterize below the state variables, the normalized factors, as independent, stationary, scalar diffusion processes that evolve in respective activity times.

We assume for k∈{1,…,n}k\in\{1,...,n\} the kk-th normalized factor YττkkY^{k}\_{\tau^{k}\_{\tau}} to be given as the ratio

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yττkk=SτkBτ​eττkY^{k}\_{\tau^{k}\_{\tau}}=\frac{S^{k}\_{\tau}}{B\_{\tau}e^{\tau^{k}\_{\tau}}} |  | (3.1) |

with basis exponential

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bτ=exp⁡{∫τt0τλ^s​𝑑s}B\_{\tau}=\exp\left\{\int\_{\tau\_{t\_{0}}}^{\tau}\hat{\lambda}\_{s}ds\right\} |  | (3.2) |

for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty), representing a scalar diffusion with stationary probability density p∞kp^{k}\_{\infty}. The stationary process YττkkY^{k}\_{\tau^{k}\_{\tau}} is assumed to evolve in the kk-th activity time

|  |  |  |  |
| --- | --- | --- | --- |
|  | ττk=τt0+(τ−ττt0)​ak\tau^{k}\_{\tau}=\tau\_{t\_{0}}+(\tau-\tau\_{\tau\_{t\_{0}}})a^{k} |  | (3.3) |

for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty), where ak>0a^{k}>0 denotes the strictly positive kk-th activity and τt0∈(−∞,∞)\tau\_{t\_{0}}\in(-\infty,\infty) the initial market time. By Equation ([3.1](https://arxiv.org/html/2602.14575v1#S3.E1 "In 3.1 Normalized Factors ‣ 3 Surprisal-Minimized Market")) it follows the kk-th initial factor value

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sτt0k=Yτt0k​eτt0>0.S^{k}\_{\tau\_{t\_{0}}}=Y^{k}\_{{\tau\_{t\_{0}}}}e^{{\tau\_{t\_{0}}}}>0. |  | (3.4) |

By application of the Itô formula it is straightforward to see that a normalized factor has the same volatility as the respective factor.
For
the stationary kk-th normalized factor process Yk={Yτkk,τk∈[τt0,∞)}Y^{k}=\{Y^{k}\_{\tau^{k}},\tau^{k}\in[{\tau\_{t\_{0}}},\infty)\}, k∈{1,…,n}k\in\{1,...,n\}, we denote
by p∞kp^{k}\_{\infty} its stationary probability density,
where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐄p∞k​(f​(Yττkk))=∫0∞f​(y)​p∞k​(y)​𝑑y{\bf{E}}^{p^{k}\_{\infty}}\left(f(Y^{k}\_{\tau^{k}\_{\tau}})\right)=\int\_{0}^{\infty}f(y)p^{k}\_{\infty}(y)dy |  | (3.5) |

denotes the average with respect to this density.
  
Four constraints for the kk-th normalized factor dynamics emerge as follows:
  
First, the average level of a normalized factor is a crucial quantity because it determines the average level of the value of the factor at a given market time, which models an average price.
Since there would exist some ambiguity concerning the average level of the kk-th normalized factor, we parametrize the arithmetic average of YkY^{k}, with a view towards the proof of Theorem [3.4](https://arxiv.org/html/2602.14575v1#S3.Thmtheorem4 "Theorem 3.4 ‣ 3.2 Surprisal Minimization ‣ 3 Surprisal-Minimized Market"), so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 4​ωk=𝐄p∞k​(Yττkk)>04\omega^{k}={\bf{E}}^{p^{k}\_{\infty}}\left(Y^{k}\_{\tau^{k}\_{\tau}}\right)>0 |  | (3.6) |

for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty).
  
Second, under the benchmark approach, the logarithm of portfolios and, in particular, the logarithmic average of the portfolio with the largest instantaneous growth rate, the GOP, are of central importance. Therefore, we parametrize the logarithmic average of YkY^{k} by the flexible constant

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐄p∞k​(ln⁡(Yττkk))=ζk∈(−∞,∞){\bf{E}}^{p^{k}\_{\infty}}(\ln(Y^{k}\_{\tau^{k}\_{\tau}}))=\zeta^{k}\in(-\infty,\infty) |  | (3.7) |

for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty).

Third, by Theorem [2.2](https://arxiv.org/html/2602.14575v1#S2.Thmtheorem2 "Theorem 2.2 ‣ 2.2 Benchmark ‣ 2 Market of Factors") and ([2.7](https://arxiv.org/html/2602.14575v1#S2.E7 "In Theorem 2.2 ‣ 2.2 Benchmark ‣ 2 Market of Factors")), we have the constraint

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=1nωk=1.\sum\_{k=1}^{n}\omega^{k}=1. |  | (3.8) |

Fourth, with a view towards the proof of Theorem [4.4](https://arxiv.org/html/2602.14575v1#S4.Thmtheorem4 "Theorem 4.4 ‣ 4.2 Information Minimization ‣ 4 Information-Minimized Market"), we introduce for the activities the constraint

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=1nωk​1ak=1.\sum\_{k=1}^{n}\omega^{k}\sqrt{\frac{1}{a^{k}}}=1. |  | (3.9) |

It is our goal to specify the kk-th normalized factor as a flexible, stationary scalar diffusion under the above described constraints. We achieve this by setting the kk-th factor volatility equal to the function

|  |  |  |  |
| --- | --- | --- | --- |
|  | βτk=4​akϕk​(Yττkk),\beta^{k}\_{\tau}=\sqrt{\frac{4a^{k}}{\phi^{k}(Y^{k}\_{\tau^{k}\_{\tau}})}}, |  | (3.10) |

where the kk-th volatility function ϕk(.)\phi^{k}(.) is a flexible, infinitely often continuously differentiable, strictly positive function of the value of the kk-th normalized factor. According to Assumption A2, when assuming stationary normalized factors, it is required that the NP Sτ∗∗S^{\*\*}\_{\tau} exists and that the kk-th normalized factor in the kk-th activity time is modelled by a unique, independent scalar diffusion process; see, e.g., Section 7.7 in ?). By the equations ([3.1](https://arxiv.org/html/2602.14575v1#S3.E1 "In 3.1 Normalized Factors ‣ 3 Surprisal-Minimized Market")), ([2.2](https://arxiv.org/html/2602.14575v1#S2.E2 "In 2.1 Factors ‣ 2 Market of Factors")), ([3.3](https://arxiv.org/html/2602.14575v1#S3.E3 "In 3.1 Normalized Factors ‣ 3 Surprisal-Minimized Market")), and an application of the Itô formula, the kk-th normalized factor YττkkY^{k}\_{\tau^{k}\_{\tau}} satisfies the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yττkk=Yττkk​(4​ϕk​(Yττkk)−1​ωk−1)​ak​d​τ+Yττkk​ϕk​(Yττkk)−12​4​ak​d​WτkdY^{k}\_{\tau^{k}\_{\tau}}=Y^{k}\_{\tau^{k}\_{\tau}}\left(4\phi^{k}(Y^{k}\_{\tau^{k}\_{\tau}})^{-1}\omega^{k}-1\right)a^{k}d\tau+Y^{k}\_{\tau^{k}\_{\tau}}\phi^{k}(Y^{k}\_{\tau^{k}\_{\tau}})^{-\frac{1}{2}}\sqrt{4a^{k}}dW^{k}\_{\tau} |  | (3.11) |

of a scalar diffusion with instantaneous reflection at zero for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty). In the above SDE, the diffusion coefficient of the kk-th normalized factor is that of a flexible scalar diffusion process.
  
The drift coefficient is determined using the Itô formula. Consequently, this SDE encompasses a wide variety of scalar diffusion processes that evolve according to their activity times.
For instance, assigning ϕk​(y)=y¯\phi^{k}(y)=\bar{y} constant models factors with constant volatilities, as described by ?). If ϕk​(y)\phi^{k}(y) is set as a power function, such as ϕk​(y)=yx\phi^{k}(y)=y^{x}, the resulting dynamics exhibit constant elasticity of variance–type stochastic volatility, following the work of ?). Choosing ϕk​(y)=y\phi^{k}(y)=y (the identity function) produces 3/2-type stochastic volatility models, as noted by ?) and ?). If ϕk​(y)=y−1\phi^{k}(y)=y^{-1}, the model coincides with the ?) volatility specification, while ϕk​(y)=y−2\phi^{k}(y)=y^{-2} corresponds to the volatility of the Bachelier model (?)). By allowing ϕk(.)\phi^{k}(.) to be any suitable general function of the normalized factor, one obtains a broad family of local volatility function models; see, for example, ?), ?), and ?).
Considered in calendar time, the class of stochastic volatility models becomes even broader, since the market time remains highly adaptable and can be defined in numerous ways, with its derivative serving as a subordinator; see ?), ?), and ?). The Assumption A1 allows sufficient flexibility to choose the market time as a nondecreasing stochastic process, potentially extending beyond the semimartingale framework.

###### Definition 3.1

We call
the above described market, formed by the savings account Sτ0S^{0}\_{\tau} and the nn factors Sτ1,…,SτnS^{1}\_{\tau},...,S^{n}\_{\tau} as
primary security accounts, a stationary market, where the net risk-adjusted return λ^τ\hat{\lambda}\_{\tau} represents an adapted, square integrable process and the normalized factors stationary, independent, scalar diffusions in market time.

This does not mean that in a stationary market the factors or resulting stocks have to be stationary processes. Only the volatilities of the normalized factors are modelled in market time as processes with stationary probability densities. The kk-stationary probability density p∞k​(y)p^{k}\_{\infty}(y), y∈(0,∞)y\in(0,\infty), of the kk-th normalized factor is the solution of a respective ordinary differential equation, the Fokker-Planck equation, as shown, e.g., in Section 4.5 in ?).

### 3.2 Surprisal Minimization

The identification of stationary dynamics in normalized factors depends on the principle driving financial market behaviour. For a stationary market, this principle is formulated through a Lagrangian based on stationary probability densities, which must be minimized to find the optimal joint density. Shannon’s information theory, as described in ?), highlights information content as a key concept derived from event probabilities, with the surprisal representing the expected information content. This paper assumes in Assumption A3 that market prices minimize the surprisal of the joint probability density of normalized factors, suggesting prices embed maximum beneficial information on average. Information content for a continuous variable is measured by the negative logarithm of its probability density, as described in?), and surprisal is the expected information content. Thus, rather than focusing on expected utilities, returns, or monetary measures, fundamental financial market quantities are in this paper interpreted as information-theoretic quantities. Following Shannon and Kullback, this leads to the proposed notion below.

###### Definition 3.2

For a stationary market
with stationary joint density

|  |  |  |  |
| --- | --- | --- | --- |
|  | p∞=∏k=1np∞kp\_{\infty}=\prod\_{k=1}^{n}p^{k}\_{\infty} |  | (3.12) |

of the normalized factors, the surprisal ℐ​(p∞)\mathcal{I}(p\_{\infty}) of p∞p\_{\infty} is defined as its average information content, which is given by the sum of the integrals

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐ​(p∞)=−∑k=1n∫0∞p∞k​(y)​ln⁡(p∞k​(y))​𝑑y,\mathcal{I}(p\_{\infty})=-\sum\_{k=1}^{n}\int\_{0}^{\infty}p^{k}\_{\infty}(y)\ln(p^{k}\_{\infty}(y))dy, |  | (3.13) |

as long as, the above quantities exist.

The stationary market reaches its lowest surprisal when, within the given specific parametrization and set of constraints, the expected information content of the stationary joint density of normalized factors is minimized. This process yields the third Lagrangian in our pursuit of an idealized market model. We now present the following kind of market:

###### Definition 3.3

A stationary market
is said to be surprisal-minimized
if the surprisal
ℐ​(p∞)\mathcal{I}(p\_{\infty})
of the stationary joint density p∞p\_{\infty} of the normalized factors is minimized for the given parametrization and constraints.

The surprisal-minimized market can be seen as ’efficient,’ though this differs from efficiency as defined by ?) and ?). Negative surprisal, mathematically equal to entropy, is important in the derivation of natural laws across disciplines; see ?). The next theorem explains the results of minimizing the surprisal of p∞p\_{\infty}, as per Assumption A3; its proof is provided in Appendix C.

###### Theorem 3.4

For k∈{1,…,n}k\in\{1,...,n\} and τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty), the dynamics of the kk-th normalized factor YττkkY^{k}\_{\tau^{k}\_{\tau}} of a surprisal-minimized market is that of a CIR process of dimension 4n\frac{4}{n}, which evolves in the kk-th activity time ττk\tau^{k}\_{\tau} as the unique strong solution of
the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yττkk=(4n−Yττkk)​ak​d​τ+Yττkk​4​ak​d​Wτk,dY^{k}\_{\tau^{k}\_{\tau}}=\left(\frac{4}{n}-Y^{k}\_{\tau^{k}\_{\tau}}\right)a^{k}d\tau+\sqrt{Y^{k}\_{\tau^{k}\_{\tau}}4a^{k}}dW^{k}\_{\tau}, |  | (3.14) |

with its initial value Yτt0k=Sτt0k​e−ττt01Y^{k}\_{{\tau\_{t\_{0}}}}=S^{k}\_{\tau\_{t\_{0}}}e^{-\tau^{1}\_{\tau\_{t\_{0}}}}
distributed according to the surprisal-minimized stationary density p∞kp^{k}\_{\infty}. The latter is a gamma density with 4n\frac{4}{n} degrees of freedom and mean 4n\frac{4}{n}.

As requested by Assumption A3, the kk-th normalized factor is a stationary scalar diffusion. It generates a stationary volatility process in market time and has, by construction, the same volatility as the kk-th factor.
Therefore, the squared volatility

|  |  |  |  |
| --- | --- | --- | --- |
|  | (βτk)2=4​akYττkk(\beta^{k}\_{\tau})^{2}=\frac{4a^{k}}{Y^{k}\_{\tau^{k}\_{\tau}}} |  | (3.15) |

of the kk-th factor with respect to the market time τ\tau is generated by the squared volatility of the kk-th normalized factor. It follows by application of the Itô formula and using ([3.10](https://arxiv.org/html/2602.14575v1#S3.E10 "In 3.1 Normalized Factors ‣ 3 Surprisal-Minimized Market")) the 3/23/2 stochastic volatility dynamics that are characterized by the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​(βτk)2=(ak+(1−1n)​(βτk)2)​(βτk)2​d​τ−((βτk)2)32​d​Wτkd(\beta^{k}\_{\tau})^{2}=\left(a^{k}+\left(1-\frac{1}{n}\right)(\beta^{k}\_{\tau})^{2}\right)(\beta^{k}\_{\tau})^{2}d\tau-\left((\beta^{k}\_{\tau})^{2}\right)^{\frac{3}{2}}dW^{k}\_{\tau} |  | (3.16) |

for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty), as long as Yττkk>0Y^{k}\_{\tau^{k}\_{\tau}}>0. A 3/23/2 volatility model was proposed in ?) as the squared volatility model of a GOP. The latter model became in ?) named minimal market model (MMM); see ?). A 3/23/2-type volatility model was independently suggested in ?) for derivative pricing due to its excellent tractability. The current paper names the entire idealized financial market model MMM that results from applying all four assumptions.

By applying Equation ([3.1](https://arxiv.org/html/2602.14575v1#S3.E1 "In 3.1 Normalized Factors ‣ 3 Surprisal-Minimized Market")), ([2.2](https://arxiv.org/html/2602.14575v1#S2.E2 "In 2.1 Factors ‣ 2 Market of Factors")), and the Itô formula, one obtains the factor dynamics as follows:

###### Corollary 3.5

For a surprisal-minimized market and k∈{1,…,n}k\in\{1,...,n\}, the kk-th factor can be expressed as the product

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sτk=Yττkk​Bτ​eττk,S^{k}\_{\tau}=Y^{k}\_{\tau^{k}\_{\tau}}B\_{\tau}e^{\tau^{k}\_{\tau}}, |  | (3.17) |

which satisfies in the market time τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty) the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sτk=λ^τ​Sτk​d​τ+4n​Bτ​ak​eττk​d​τ+Sτk​4​Bτ​ak​eττk​d​WτkdS^{k}\_{\tau}=\hat{\lambda}\_{\tau}S^{k}\_{\tau}d\tau+\frac{4}{n}B\_{\tau}a^{k}e^{\tau^{k}\_{\tau}}d\tau+\sqrt{S^{k}\_{\tau}4B\_{\tau}a^{k}e^{\tau^{k}\_{\tau}}}dW^{k}\_{\tau} |  | (3.18) |

of a squared radial Ornstein-Uhlenbeck (SROU) process with dimension 4n\frac{4}{n} for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty).

### 3.3 Benchmark Dynamics

Applying Theorem [2.2](https://arxiv.org/html/2602.14575v1#S2.Thmtheorem2 "Theorem 2.2 ‣ 2.2 Benchmark ‣ 2 Market of Factors"), we see that in a market that minimizes surprisal, the benchmark is created by assigning equal weights to all factors. Specifically, at any market time τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty), the weight of the kk-th factor is πτ∗,k=1n\pi^{\*,k}\_{\tau}=\frac{1}{n}. Since the volatility of a factor can become infinite if that factor reaches zero, we define 𝒯⊂[τt0,∞)\mathcal{T}\subset[\tau\_{t\_{0}},\infty) as the set of all market times when every one of the nn factors remains strictly positive. The SDEs governing the SROU processes for both the factors and their normalized counterparts have unique strong solutions, and these solutions are still well-defined even at points when a factor hits zero. To prevent complications from infinite volatility, we focus only on market times contained in 𝒯⊂[τt0,∞)\mathcal{T}\subset[\tau\_{t\_{0}},\infty). The dynamics for the benchmark under these conditions are detailed in Appendix D.

###### Theorem 3.6

Consider a surprisal-minimized market at a market time τ∈𝒯\tau\in\mathcal{T}. The benchmark Sτ∗S^{\*}\_{\tau} represents the equal-weighted factor portfolio and
satisfies the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sτ∗=λ^τ​Sτ∗​d​τ+Sτ∗​Zτ​d​τ+Sτ∗​Zτ​d​Wτ∗=λ^τ​Sτ∗​d​τ+4​eττ∗​aτ∗​d​τ+Sτ∗​4​eττ∗​aτ∗​d​Wτ∗,dS^{\*}\_{\tau}=\hat{\lambda}\_{\tau}S^{\*}\_{\tau}d\tau+S^{\*}\_{\tau}Z\_{\tau}d\tau+S^{\*}\_{\tau}\sqrt{Z\_{\tau}}dW^{\*}\_{\tau}=\hat{\lambda}\_{\tau}S^{\*}\_{\tau}d\tau+4e^{\tau^{\*}\_{\tau}}a^{\*}\_{\tau}d\tau+\sqrt{S^{\*}\_{\tau}}\sqrt{4e^{\tau^{\*}\_{\tau}}a^{\*}\_{\tau}}dW^{\*}\_{\tau}, |  | (3.19) |

with initial value Sτt0∗>0S^{\*}\_{\tau\_{t\_{0}}}>0
and squared benchmark volatility

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zτ=1n2​∑k=1n4​akYττkk,Z\_{\tau}=\frac{1}{n^{2}}\sum\_{k=1}^{n}\frac{4a^{k}}{Y^{k}\_{\tau^{k}\_{\tau}}}, |  | (3.20) |

where Wτ∗W^{\*}\_{\tau} is a Brownian motion with stochastic differential

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Wτ∗=Zτ−12​1n​∑k=1n4​akYττkk​d​WτkdW^{\*}\_{\tau}=Z\_{\tau}^{-\frac{1}{2}}\frac{1}{n}\sum\_{k=1}^{n}\sqrt{\frac{4a^{k}}{Y^{k}\_{\tau^{k}\_{\tau}}}}dW^{k}\_{\tau} |  | (3.21) |

and initial value Wτt0∗=0W^{\*}\_{\tau\_{t\_{0}}}=0.
The normalized benchmark

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yττ∗∗=Sτ∗eττ∗Y^{\*}\_{\tau^{\*}\_{\tau}}=\frac{S^{\*}\_{\tau}}{e^{\tau^{\*}\_{\tau}}} |  | (3.22) |

follows an SROU process of dimension four
that is evolving in the benchmark time

|  |  |  |  |
| --- | --- | --- | --- |
|  | ττ∗=ττt0∗+∫τt0τas∗​𝑑s\tau^{\*}\_{\tau}=\tau^{\*}\_{\tau\_{t\_{0}}}+\int\_{\tau\_{t\_{0}}}^{\tau}a^{\*}\_{s}ds |  | (3.23) |

and satisfies the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yττ∗∗=λ^τ​Yττ∗∗​d​τ+(4−Yττ∗∗)​aτ∗​d​τ+2​Yττ∗∗​aτ∗​d​Wτ∗dY^{\*}\_{\tau^{\*}\_{\tau}}=\hat{\lambda}\_{\tau}Y^{\*}\_{\tau^{\*}\_{\tau}}d\tau+\left(4-Y^{\*}\_{\tau^{\*}\_{\tau}}\right)a^{\*}\_{\tau}d\tau+2\sqrt{Y^{\*}\_{\tau^{\*}\_{\tau}}a^{\*}\_{\tau}}dW^{\*}\_{\tau} |  | (3.24) |

with initial value

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yττt0∗∗=Sτt0∗​e−ττt0∗Y^{\*}\_{\tau^{\*}\_{\tau\_{t\_{0}}}}=S^{\*}\_{\tau\_{t\_{0}}}e^{-\tau^{\*}\_{\tau\_{t\_{0}}}} |  | (3.25) |

and benchmark activity

|  |  |  |  |
| --- | --- | --- | --- |
|  | aτ∗=Zτ​Yττ∗∗4.a^{\*}\_{\tau}=\frac{Z\_{\tau}Y^{\*}\_{\tau^{\*}\_{\tau}}}{4}. |  | (3.26) |

The normalized benchmark is an SROU process with dimension four in benchmark time ττ∗\tau^{\*}\_{\tau}, always positive and uniquely solving the SDE ([3.24](https://arxiv.org/html/2602.14575v1#S3.E24 "In Theorem 3.6 ‣ 3.3 Benchmark Dynamics ‣ 3 Surprisal-Minimized Market")). Its squared volatility ZτZ\_{\tau} with respect to market time, as given in ([3.20](https://arxiv.org/html/2602.14575v1#S3.E20 "In Theorem 3.6 ‣ 3.3 Benchmark Dynamics ‣ 3 Surprisal-Minimized Market")), becomes infinite when any normalized factor reaches zero, causing an upward jump in benchmark time. This highlights that benchmark volatility may spike at certain moments; however, this does not imply that the diffusion coefficient itself becomes infinite. It also suggests the market time-integrated growth rate of the benchmark can have upward jumps when a factor hits zero.
  
The benchmark is built using a dynamic asset allocation approach. In actual trading, reallocations can only occur at specific intervals since trades are discrete, and the SDEs representing both the factors and the benchmark are theoretical models that assume continuous trading. The continuous-time framework approximates what typically occurs when factor values become extremely small.

Brownian motion and its Gaussian transition probability density effectively describe the limiting behavior in continuous time for a sum of independently moving particles. This principle underlies models such as Bachelier’s ?) approach for sums of independent capital units and the Black-Scholes model by ?), where it is applied to the logarithm of these sums. Empirical evidence, such as the Student-t log-return distribution observed in stock indices, indicates that these models do not sufficiently represent real market behavior. When analyzing the evolution of aggregated independent capital units, it becomes apparent that their trajectory is influenced by the exact count of units present. Within this framework, the SROU process and its noncentral chi-square transition probability density effectively model the limiting continuous-time dynamics of a system comprising independently moving particles that may generate new entities or cease to exist, as detailed in ?). This insight offers an intuitive perspective on the derived surprisal-minimized market dynamics, framing them as the aggregate activity of independent capital units that either proliferate or disappear autonomously.

## 4 Information-Minimized Market

### 4.1 Benchmark-Neutral Pricing

Hedging an inexpensive zero-coupon bond, which pays one unit of the savings account at maturity, necessitates trading both the numéraire and the savings account; for further details, refer to ?) and ?). This requirement implies that, in general, it is essential to be able to trade the numéraire used for pricing when hedging contingent claims. Subject to Assumption A2, real-world pricing may be employed with the NP Sτ∗∗S^{\*\*}\_{\tau} as the numéraire and the real-world probability measure PP as the pricing measure, as outlined in ?). Regarding the derived surprisal-minimized dynamics, risk-neutral pricing can result in prices that are considerably higher than necessary, as demonstrated by ?).
  
Within the current financial market, the NP represents a leveraged portfolio that takes a short position in the savings account. Since practical trading occurs at discrete intervals, a proxy for the NP, an extremely volatile portfolio, cannot be assured to remain strictly positive. Additionally, modelling the dynamics of the NP requires knowledge of the net risk-adjusted return λ^τ\hat{\lambda}\_{\tau}, a drift parameter process that is particularly challenging to estimate. To address these difficulties, ?) introduced the benchmark-neutral (BN) pricing method, which utilizes the benchmark Sτ∗S^{\*}\_{\tau} as the numéraire and the corresponding BN pricing measure QS∗Q\_{S^{\*}} as the pricing measure. The BN pricing measure QS∗Q\_{S^{\*}} is specified by
the Radon-Nikodym derivative

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΛQS∗​(τ)=d​QS∗d​P|ℱτ=Sτ∗Sτ∗∗Sτt0∗Sτt0∗∗\Lambda\_{Q\_{{{S^{\*}}}}}(\tau)=\frac{dQ\_{{S^{\*}}}}{dP}\Big|\_{\mathcal{F}\_{\tau}}=\frac{\frac{{S^{\*}\_{\tau}}}{S^{\*\*}\_{\tau}}}{\frac{{S^{\*}\_{\tau\_{t\_{0}}}}}{S^{\*\*}\_{\tau\_{t\_{0}}}}} |  | (4.1) |

for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty); see ?).

Let LQ1​(ℱτT){L}\_{Q}^{1}(\mathcal{F}\_{\tau\_{T}})
denote the set of QQ-integrable, ℱτT\mathcal{F}\_{\tau\_{T}}-measurable random variables in a filtered probability space (Ω,ℱ,ℱ¯,Q)(\Omega,\mathcal{F},\underline{\cal{F}},Q). It is shown in ?) for a more general financial market model than the above derived surprisal-minimized market model that the BN pricing measure QS∗Q\_{S^{\*}} is an equivalent probability measure and BN pricing determines the minimal possible prices for replicable contingent claims. More precisely, one can conclude directly from Theorem 3.4 in ?) the following facts:

###### Corollary 4.1

For a surprisal-minimized market with n>2n>2 and τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty), where the absolute value of the net risk-adjusted return λ^τ\hat{\lambda}\_{\tau} is constant and finite, the following statements hold:
  
(i) The BN pricing measure QS∗Q\_{S^{\*}} is an equivalent probability measure.
  
(ii) For a replicable contingent claim HτTH\_{\tau\_{T}}, with stopping time τT\tau\_{T} that is bounded as a market time, where HτTSτT∗∗∈LP1​(ℱτT)\frac{H\_{\tau\_{T}}}{S^{\*\*}\_{\tau\_{T}}}\in L^{1}\_{P}(\mathcal{F}\_{\tau\_{T}}), and HτTSτT∗∈LQS∗1​(ℱτT)\frac{H\_{\tau\_{T}}}{S^{\*}\_{\tau\_{T}}}\in L^{1}\_{Q\_{S^{\*}}}(\mathcal{F}\_{\tau\_{T}}),
its minimal possible price HτH\_{\tau} at the market time τ∈[τt0,τT]\tau\in[\tau\_{t\_{0}},\tau\_{T}] equals the BN price
provided by the benchmark-neutral pricing formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hτ=Sτ∗​𝐄QS∗​(HτTSτT∗|ℱτ).H\_{\tau}=S^{\*}\_{\tau}{\bf E}^{Q\_{S^{\*}}}\left(\frac{H\_{\tau\_{T}}}{S^{\*}\_{\tau\_{T}}}|\mathcal{F}\_{\tau}\right). |  | (4.2) |

(iii) For k∈{1,…,n}k\in\{1,...,n\}, the process W¯k={W¯τk,τ∈[τt0,∞)}\bar{W}^{k}=\{\bar{W}^{k}\_{\tau},\tau\in[\tau\_{t\_{0}},\infty)\},
satisfying the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​W¯τk=λ^τ​Sτk4​aτk​Bτ​eττk​d​τ+d​Wτkd\bar{W}^{k}\_{\tau}=\hat{\lambda}\_{\tau}\sqrt{\frac{S^{k}\_{\tau}}{4a^{k}\_{\tau}B\_{\tau}e^{\tau^{k}\_{\tau}}}}d\tau+dW^{k}\_{\tau} |  | (4.3) |

for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty) with W¯τt0k=0\bar{W}^{k}\_{\tau\_{t\_{0}}}=0, is under the BN pricing measure QS∗Q\_{S^{\*}} a Brownian motion in market time.
  
(iv) The benchmark satisfies the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sτ∗=Zτ​Sτ∗​d​τ+Zτ​Sτ∗​d​W¯τ∗=4​eττ∗​aτ∗​d​τ+Sτ∗​4​eττ∗​aτ∗​d​W¯τ∗dS^{\*}\_{\tau}=Z\_{\tau}S^{\*}\_{\tau}d\tau+\sqrt{Z\_{\tau}}S^{\*}\_{\tau}d\bar{W}^{\*}\_{\tau}=4e^{\tau^{\*}\_{\tau}}a^{\*}\_{\tau}d\tau+\sqrt{S^{\*}\_{\tau}4e^{\tau^{\*}\_{\tau}}a^{\*}\_{\tau}}d\bar{W}^{\*}\_{\tau} |  | (4.4) |

of a time-transformed squared Bessel process of dimension four, where W¯∗={W¯τ∗,τ∈[τt0,∞)}\bar{W}^{\*}=\{\bar{W}^{\*}\_{\tau},\tau\in[\tau\_{t\_{0}},\infty)\} is under the BN pricing measure QS∗Q\_{S^{\*}} a Brownian motion in market time,
satisfying the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​W¯τ∗=Zτ−12​λ^τ​d​τ+d​Wτ∗d\bar{W}^{\*}\_{\tau}=Z\_{\tau}^{-\frac{1}{2}}\hat{\lambda}\_{\tau}d\tau+dW^{\*}\_{\tau} |  | (4.5) |

for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty) with ZτZ\_{\tau} given in ([3.20](https://arxiv.org/html/2602.14575v1#S3.E20 "In Theorem 3.6 ‣ 3.3 Benchmark Dynamics ‣ 3 Surprisal-Minimized Market")) and W¯τt0∗=0\bar{W}^{\*}\_{\tau\_{t\_{0}}}=0.

The BN pricing measure QS∗Q\_{S^{\*}} substitutes in the SDEs of the factors under the real-world probability measure the net risk-adjusted return λ^τ\hat{\lambda}\_{\tau} by zero, and the processes Wτ1,…,WτnW^{1}\_{\tau},...,W^{n}\_{\tau} by respective processes W¯τ1,…,W¯τn\bar{W}^{1}\_{\tau},...,\bar{W}^{n}\_{\tau}, which are Brownian motions under the BN pricing measure. This means, the knowledge of the net risk-adjusted return λ^τ\hat{\lambda}\_{\tau} is not needed for BN pricing and hedging. The dimensions of the SROU processes that form the normalized factors, factors, and the benchmark remain under the BN pricing measure QS∗Q\_{S^{\*}} the same as under the real-world probability measure PP.

In a wide class of potential numéraires the benchmark has been shown in ?) to be the only portfolio that yields as numéraire an equivalent pricing measure. In ?) BN pricing has been generalized for not fully replicable contingent claims by introducing the concept of BN risk-minimization.

### 4.2 Information Minimization

We denote for the normalized factors the BN stationary joint density by the product

|  |  |  |  |
| --- | --- | --- | --- |
|  | q∞=∏k=1nq∞kq\_{\infty}=\prod\_{k=1}^{n}q^{k}\_{\infty} |  | (4.6) |

and the real-world stationary joint density by

|  |  |  |  |
| --- | --- | --- | --- |
|  | p∞=∏k=1np∞k.p\_{\infty}=\prod\_{k=1}^{n}p^{k}\_{\infty}. |  | (4.7) |

A trade at the market time τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty) reveals information through its price. Trades are discrete in time and the trading intensities, which quantify the speed of the flow of price information, are modelled by the market activities in the surprisal-minimized market.
By using ?), we employ the following notion:

###### Definition 4.2

For a surprisal-minimized market with BN stationary joint density q∞q\_{\infty} and real-world stationary joint density p∞p\_{\infty} of the normalized factors at the market time τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty), the Kullback-Leibler divergence I​(p∞,q∞)I(p\_{\infty},q\_{\infty}) of q∞q\_{\infty} from p∞p\_{\infty} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(p∞,q∞)=dd​τ​𝐄p∞​(−ln⁡(ΛQS∗​(τ))).I(p\_{\infty},q\_{\infty})=\frac{d}{d\tau}{\bf{E}}^{p\_{\infty}}\left(-\ln(\Lambda\_{Q\_{S^{\*}}}(\tau))\right). |  | (4.8) |

.

The above Kullback-Leibler divergence measures the increase of expected information content when employing BN pricing. One notices by ([4.8](https://arxiv.org/html/2602.14575v1#S4.E8 "In Definition 4.2 ‣ 4.2 Information Minimization ‣ 4 Information-Minimized Market")) and ([4.1](https://arxiv.org/html/2602.14575v1#S4.E1 "In 4.1 Benchmark-Neutral Pricing ‣ 4 Information-Minimized Market")) that the Kullback-Leibler divergence equals
the average growth rate of the NP Sτ∗∗S^{\*\*}\_{\tau} denominated in units of the benchmark Sτ∗S^{\*}\_{\tau}.

The Assumption A4 postulates that the increase of expected information content from BN pricing is minimized in the market, which means that the Kullback-Leibler divergence I​(p∞,q∞)I(p\_{\infty},q\_{\infty}) is minimized. This minimization involves our fourth Lagrangian.

###### Definition 4.3

We call a surprisal-minimized market information-minimized when the above Kullback-Leibler divergence of q∞q\_{\infty} from p∞p\_{\infty} is minimized.

The results of the above minimization are described in the following theorem, where the proof is provided in Appendix E:

###### Theorem 4.4

For an information-minimized market, it follows for k∈{1,…,n}k\in\{1,...,n\} that the kk-th activity equals

|  |  |  |  |
| --- | --- | --- | --- |
|  | ak=1,a^{k}=1, |  | (4.9) |

and the net risk-adjusted return

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ^τ=λ^\hat{\lambda}\_{\tau}=\hat{\lambda} |  | (4.10) |

equals a constant, where the divergence of q∞q\_{\infty} from p∞p\_{\infty} amounts to

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(p∞,q∞)=λ^22I(p\_{\infty},q\_{\infty})=\frac{\hat{\lambda}^{2}}{2} |  | (4.11) |

for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty).

For an information-minimized market the activities equal 11 and the net risk-adjusted return λ^τ=λ^\hat{\lambda}\_{\tau}=\hat{\lambda} is a constant. As indicated earlier we name the resulting model as follows:

###### Definition 4.5

The idealized financial market model that results from the application of the four assumptions A1, A2, A3,and A4, yielding an information-minimized market, is called minimal market model (MMM).

Under the MMM and for k∈{1,…,n}k\in\{1,...,n\}, the kk-th factor

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sτk=Yτk​Bτ​eτ,S^{k}\_{\tau}=Y^{k}\_{\tau}B\_{\tau}e^{\tau}, |  | (4.12) |

has by ([2.2](https://arxiv.org/html/2602.14575v1#S2.E2 "In 2.1 Factors ‣ 2 Market of Factors")), ([3.1](https://arxiv.org/html/2602.14575v1#S3.E1 "In 3.1 Normalized Factors ‣ 3 Surprisal-Minimized Market")), and application of the Itô formula, the following properties:

###### Corollary 4.6

For
k∈{1,…,n}k\in\{1,...,n\}, the kk-th factor has under the MMM the dynamics of an SROU process with dimension dk=4nd\_{k}=\frac{4}{n}. It
satifies the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sτk=λ^​Sτk​d​τ+4n​Bτ​eτ​d​τ+Sτk​4​Bτ​eτ​d​WτkdS^{k}\_{\tau}=\hat{\lambda}S^{k}\_{\tau}d\tau+\frac{4}{n}B\_{\tau}e^{\tau}d\tau+\sqrt{S^{k}\_{\tau}}\sqrt{4B\_{\tau}e^{\tau}}dW^{k}\_{\tau} |  | (4.13) |

for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty), with random initial value Sτt0k=Yτt0k​eτt0S^{k}\_{\tau\_{t\_{0}}}=Y^{k}\_{\tau\_{t\_{0}}}e^{\tau\_{t\_{0}}}, where Yτt0kY^{k}\_{\tau\_{t\_{0}}} has the stationary probability density pτt0k=p∞kp^{k}\_{\tau\_{t\_{0}}}=p^{k}\_{\infty}
as its density.

?) analyze Lie group symmetries for PDEs governing diffusion dynamics with square-root state variable diffusion coefficients. For the normalized factors in ([4.13](https://arxiv.org/html/2602.14575v1#S4.E13 "In Corollary 4.6 ‣ 4.2 Information Minimization ‣ 4 Information-Minimized Market")), Theorem 4.4.3 in ?) identifies a specific Lie group symmetry aligning with these dynamics. This symmetry provides an explicit formula for the transition probability density, which is shown to be that of an SROU process; see Equation 5.1.2 in?). Therefore, the transition probability density for normalized factor dynamics relates directly to a corresponding Lie group symmetry of its governing PDE.
  
Noether’s Theorems in ?) predict that when a system of partial differential equations for state variables has a Lie group symmetry, a conservation law exists. In an information-minimized market, this conservation law appears as Equation ([4.10](https://arxiv.org/html/2602.14575v1#S4.E10 "In Theorem 4.4 ‣ 4.2 Information Minimization ‣ 4 Information-Minimized Market")), which means the net risk-adjusted return remains constant. This makes economic sense and enhances our understanding of how economies work: The parameter λ^\hat{\lambda}, a Lagrange multiplier, can be seen as the average extra net return a firm needs above the interest rate, assuming its business activity is risk-free. If firms earn less than λ^\hat{\lambda}, their operations would quickly become unprofitable. Conversely, if the average extra net return exceeds λ^\hat{\lambda}, new competitors would enter the market, driving down returns until they settle at the natural constant λ^\hat{\lambda}.

### 4.3 Additivity Property of Sums of Independent Factors

The sum of independent squared Bessel processes evolving in the same time forms another squared Bessel process, as shown by ?). This distinctive additivity arises from the specific partial differential equation governing the transition probability density of the squared Bessel process. These processes are particular types of SROU processes; see ?). By applying Corollary [4.6](https://arxiv.org/html/2602.14575v1#S4.Thmtheorem6 "Corollary 4.6 ‣ 4.2 Information Minimization ‣ 4 Information-Minimized Market"), the following result is derived:

###### Corollary 4.7

For
a set 𝒜⊆{1,…,n}\mathcal{A}\subseteq\{1,...,n\} of indexes of independent factors, the respective sum of independent factors

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sτ𝒜=∑k∈𝒜SτkS^{\mathcal{A}}\_{\tau}=\sum\_{k\in\mathcal{A}}S^{k}\_{\tau} |  | (4.14) |

satisfies under the MMM the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sτ𝒜=λ^​Sτ𝒜​d​τ+d𝒜​Bτ​eτ​d​τ+Sτ𝒜​4​Bτ​eτ​d​Wτ𝒜dS^{\mathcal{A}}\_{\tau}=\hat{\lambda}S^{\mathcal{A}}\_{\tau}d\tau+d\_{\mathcal{A}}B\_{\tau}e^{\tau}d\tau+\sqrt{S^{\mathcal{A}}\_{\tau}4B\_{\tau}e^{\tau}}dW^{\mathcal{A}}\_{\tau} |  | (4.15) |

of an SROU process
with net risk-adjusted return λ^\hat{\lambda}, dimension

|  |  |  |  |
| --- | --- | --- | --- |
|  | d𝒜=∑k∈𝒜4n,d\_{\mathcal{A}}=\sum\_{k\in\mathcal{A}}\frac{4}{n}, |  | (4.16) |

and initial value

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sτt0𝒜=∑k∈𝒜Sτt0k=∑k∈𝒜Yτt0k​eτt0,S^{\mathcal{A}}\_{\tau\_{t\_{0}}}=\sum\_{k\in\mathcal{A}}S^{k}\_{\tau\_{t\_{0}}}=\sum\_{k\in\mathcal{A}}Y^{k}\_{\tau\_{t\_{0}}}e^{\tau\_{t\_{0}}}, |  | (4.17) |

where Wτ𝒜W^{\mathcal{A}}\_{\tau} is a Brownian motion with stochastic differential

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Wτ𝒜=1Sτ𝒜​∑k∈𝒜Sτk​d​WτkdW^{\mathcal{A}}\_{\tau}=\frac{1}{\sqrt{S^{\mathcal{A}}\_{\tau}}}\sum\_{k\in\mathcal{A}}\sqrt{S^{k}\_{\tau}}dW^{k}\_{\tau} |  | (4.18) |

for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty) with initial value Wτt0𝒜=0W^{\mathcal{A}}\_{\tau\_{t\_{0}}}=0.
The respective normalized sum of factors

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yττ𝒜𝒜=Sτ𝒜Bτ​eτ=∑k∈𝒜YττkkY^{\mathcal{A}}\_{\tau^{\mathcal{A}}\_{\tau}}=\frac{S^{\mathcal{A}}\_{\tau}}{B\_{\tau}e^{\tau}}=\sum\_{k\in{\mathcal{A}}}Y^{k}\_{\tau^{k}\_{\tau}} |  | (4.19) |

satisfies the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yτ𝒜=(d𝒜−Yτ𝒜)​d​τ+4​Yτ𝒜​d​Wτ𝒜dY^{\mathcal{A}}\_{\tau}=\left(d\_{\mathcal{A}}-Y^{\mathcal{A}}\_{\tau}\right)d\tau+\sqrt{4Y^{\mathcal{A}}\_{\tau}}dW^{\mathcal{A}}\_{\tau} |  | (4.20) |

and evolves as a CIR process of dimension d𝒜d\_{\mathcal{A}} in the market time
τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty).

The result demonstrates that factor sums have a unique additive property under the MMM. The sum of all independent factors, called the factor portfolio (FP) SτF​PS^{FP}\_{\tau}, is particularly important. Using Corollary [4.7](https://arxiv.org/html/2602.14575v1#S4.Thmtheorem7 "Corollary 4.7 ‣ 4.3 Additivity Property of Sums of Independent Factors ‣ 4 Information-Minimized Market"), the Itô formula, and Equation ([2.7](https://arxiv.org/html/2602.14575v1#S2.E7 "In Theorem 2.2 ‣ 2.2 Benchmark ‣ 2 Market of Factors")), we conclude the following:

###### Corollary 4.8

The FP, which is the sum of the factors,

|  |  |  |  |
| --- | --- | --- | --- |
|  | SτF​P=∑k=1nSτk,S^{FP}\_{\tau}=\sum\_{k=1}^{n}S^{k}\_{\tau}, |  | (4.21) |

follows under the MMM a time-transformed squared Bessel process of dimension four. The normalized FP

|  |  |  |  |
| --- | --- | --- | --- |
|  | YττF​PF​P=∑k=1nYττkk=SτF​PBτ​eτY^{FP}\_{\tau^{FP}\_{\tau}}=\sum\_{k=1}^{n}Y^{k}\_{\tau^{k}\_{\tau}}=\frac{S^{FP}\_{\tau}}{B\_{\tau}e^{\tau}} |  | (4.22) |

represents a CIR process of dimension four in market time with average 44.

### 4.4 Ilustrations

For the SROU process SτF​PS^{FP}\_{\tau} evolving in the market time τt{\tau\_{t}} one obtains via application of the Itô formula its activity time via the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | τt=ln⁡([Sτ.F​P]t0,t+eτt0){\tau\_{t}}=\ln\left(\left[\sqrt{S^{FP}\_{\tau\_{.}}}\right]\_{t\_{0},t}+e^{{\tau\_{t\_{0}}}}\right) |  | (4.23) |

for t∈[t0,∞)t\in[t\_{0},\infty); see ?). The quadratic variation [Sτ.F​P]t0,t[\sqrt{S^{FP}\_{\tau\_{.}}}]\_{t\_{0},t} is observable. The only parameter needed to determine the activity time is the initial activity time τt0{\tau\_{t\_{0}}}. For stock market indices, the activity time typically evolves in an almost linear manner, making it easy to estimate the initial value through linear regression; see ?). This estimation only needs to be done once, after which the initial activity time becomes a known parameter. Once established, it remains unchanged, allowing for straightforward calculation of the current activity time when pricing contingent claims. By setting the maturity of a contingent claim as a fixed activity time value of the underlying security and finely discretizing calendar time, research by

![Refer to caption](x1.png)


Figure 4.1:  Logarithms of US savings account denominated MSCI (blue) and EWI114 (red).

?) and ?) has shown that hedge errors for inexpensive zero-coupon bonds are extremely small. Only noticeable discretization errors arise when activity time moves faster than expected in calendar time, resulting in larger activity time steps. The outstanding hedges achieved are due to the observed activity time capturing all features of the security trajectory not explained by diffusion dynamics modeled in activity time. Most of these features can be accounted for using Assumption A1, as shown in ?).

![Refer to caption](x2.png)


Figure 4.2:  Market time τt\tau\_{t} (blue) and benchmark time ττt∗\tau^{\*}\_{\tau\_{t}} (red).

For illustration, consider the MSCI World Total Return stock index (MSCI) in US savings account denomination as proxy for the factor portfolio SτF​PS^{FP}\_{\tau} and the EWI114 constructed in ?) as proxy for the benchmark Sτ∗S^{\*}\_{\tau}. The latter refers to an equally weighted portfolio of 114 global industry subsector indices, which can be considered as factors. Figure [4.1](https://arxiv.org/html/2602.14575v1#S4.F1 "Figure 4.1 ‣ 4.4 Ilustrations ‣ 4 Information-Minimized Market") shows the logarithms of both stock portfolios, revealing their roughly linear progression. Figure [4.2](https://arxiv.org/html/2602.14575v1#S4.F2 "Figure 4.2 ‣ 4.4 Ilustrations ‣ 4 Information-Minimized Market") displays the market time τt\tau\_{t} and the benchmark time ττt∗\tau^{\*}\_{\tau\_{t}}, both following nearly linear paths. As illustrated in ?) and ?), for a fixed maturity at the end of the dataset measured in benchmark time, an inexpensive zero-coupon bond, paying out one unit from the savings account, has been priced using BN pricing and hedging, with the EWI114 serving as a proxy. The resulting hedge error, shown in Figure [4.3](https://arxiv.org/html/2602.14575v1#S4.F3 "Figure 4.3 ‣ 4.4 Ilustrations ‣ 4 Information-Minimized Market"), is less than 0.00010.0001 units of the savings account at maturity, where one unit equals the payout. Notably, hedging inexpensive zero-coupon bonds with very long maturities turns out to be less costly than traditional risk-neutral pricing suggests, an insight highlighted by ?) and significant for pension and insurance industries.

![Refer to caption](x3.png)


Figure 4.3:  Hedge error for inexpensive zero-coupon bond.

### 4.5 Empirical Evidence

Let us compare predicted properties with empirical data from the real market, as outlined in the introduction: By design, stock market index volatilities are stationary processes; see ?). The Student-t density with four degrees of freedom emerges when estimating the log-return density of a security whose squared volatility follows an inverse gamma distribution with four degrees of freedom; see, e.g., ?) or ?). When the MSCI is viewed as the FP, the MMM predicts its log-return density as a Student-t density with four degrees of freedom, which ?) found to have high significance among numerous competing models. ?) demonstrated that, across many observation frequencies, the hypothesis that MSCI log-returns follow a Student-t distribution with approximately four degrees of freedom cannot be easily dismissed when valued in major currencies. Similar findings were obtained for the S&P500 in ?) and in ?) for stock indices of various countries.

Since for an SROU process the volatility is proportional to the inverse of its square root, the leverage effect, observed by ?), is endogeneously built into the MMM dynamics of stock indices and several other securities. The 3/23/2 stochastic volatility model for stock indices of the MMM explains the clustering and heteroscedasticity of observed volatilities. Moreover, the rough volatility paths observed, e.g., in ?), can be explained, as is shown in ?), due to the fact that the market activity evolves in market time but is viewed in calendar time, which generates volatility spikes. The paper ?) demonstrates that the market activity under the MMM is modelling the fast moving component of the stock market index volatility, whereas the inverse of the square root of the normalized stock market index represents its much slower moving component. This aligns with the findings in ?). The logarithm of a stock market index is under the MMM, by construction, approximately linearly evolving in a mean-reverting manner, as visible in Figure [4.1](https://arxiv.org/html/2602.14575v1#S4.F1 "Figure 4.1 ‣ 4.4 Ilustrations ‣ 4 Information-Minimized Market") for the MSCI. As shown in ?) and Figure [4.3](https://arxiv.org/html/2602.14575v1#S4.F3 "Figure 4.3 ‣ 4.4 Ilustrations ‣ 4 Information-Minimized Market"), the MMM delivered extremely accurate hedges for thousands of inexpensive extreme maturity bonds.
  
Under the MMM, benchmark dynamics follow an SROU process with dimension four in benchmark time. ?) constructed the EWI114 as a proxy for the world stock market benchmark, which shows strong average growth compared to the MSCI, as shown in Figure [4.1](https://arxiv.org/html/2602.14575v1#S4.F1 "Figure 4.1 ‣ 4.4 Ilustrations ‣ 4 Information-Minimized Market"). Similarly, ?) introduced the EWI104; its log-return density is shown to align with a Student-t distribution with four degrees of freedom, consistent with MMM predictions.
  
?) found that the 3/2-volatility model of the MMM outperforms other stochastic volatility models when applied to VIX derivatives. ?) observed self-similarity in stock indices, which the MMM also predicts through its modelling of sums of independent factors as squared Bessel processes; see ?). Thus, the MMM accounts for key empirical facts and can be considered to represent a ‘realistic’ financial market model.

## Conclusion

Based on four assumption, a parsimonious, idealized information-minimized financial market model has been derived. The stock market index and the growth optimal portfolio of the stocks are under this model and under the benchmark-neutral pricing measure squared Bessel processes that evolve in respective activity times. No parameters are required for the accurate benchmark-neutral pricing and hedging of a wide range of contingent claims. Only the observable market time and the observable benchmark value enter the respective formulas for prices and hedges concerning the benchmark.
The findings indicate that the financial market can be viewed as a communication system, and concepts from information theory are particularly pertinent to the field of finance. Further research could revisit long standing questions in finance from the perspective of this paper and may lead to interesting answers.

## Appendix A: Proof of Theorem [2.2](https://arxiv.org/html/2602.14575v1#S2.Thmtheorem2 "Theorem 2.2 ‣ 2.2 Benchmark ‣ 2 Market of Factors")

Proof:
By applying Theorem 3.1 in ?) for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty), we obtain from ([2.2](https://arxiv.org/html/2602.14575v1#S2.E2 "In 2.1 Factors ‣ 2 Market of Factors")) with the SDE 3.10 in Theorem 3.1 in ?)
for the portfolio SτπS^{\pi}\_{\tau} with weight vector πτ=(πτ1,…,πτn)⊤\pi\_{\tau}=(\pi^{1}\_{\tau},...,\pi^{n}\_{\tau})^{\top} for the holdings in the factors 𝐒τ{\bf{S}}\_{\tau} the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​SτπSτπ=πτ⊤​d​𝐒τ𝐒τ=λ^τ​d​τ+∑k=1nπτk​βτk​(βτk​ωk​d​τ+d​Wτk).\frac{dS^{\pi}\_{\tau}}{S^{\pi}\_{\tau}}=\pi\_{\tau}^{\top}\frac{d{\bf{S}}\_{\tau}}{{\bf{S}}\_{\tau}}=\hat{\lambda}\_{\tau}d\tau+\sum\_{k=1}^{n}\pi^{k}\_{\tau}\beta^{k}\_{\tau}(\beta^{k}\_{\tau}\omega^{k}d\tau+d{W}^{k}\_{\tau}). |  | (A.1) |

By the matrix equation (3.5) in Theorem 3.1 in ?) it follows for the kk-th factor-GOP weight

|  |  |  |  |
| --- | --- | --- | --- |
|  | (βτk)2​πτ∗,k+λ^τ=λ^τ+(βτk)2​ωk,(\beta^{k}\_{\tau})^{2}\pi^{\*,k}\_{\tau}+\hat{\lambda}\_{\tau}=\hat{\lambda}\_{\tau}+(\beta^{k}\_{\tau})^{2}\omega^{k}, |  | (A.2) |

which yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | πτ∗,k=ωk\pi^{\*,k}\_{\tau}=\omega^{k} |  | (A.3) |

for k∈{1,…,n}k\in\{1,...,n\} and τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty). By
applying Equation (3.8) in ?) we obtain the kk-th benchmark volatility

|  |  |  |  |
| --- | --- | --- | --- |
|  | πτ∗,k​βτk=ωk​βτk\pi^{\*,k}\_{\tau}\beta^{k}\_{\tau}=\omega^{k}\beta^{k}\_{\tau} |  | (A.4) |

for k∈{1,…,n}k\in\{1,...,n\} and τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty). Furthermore, we obtain by Equation (3.4) in Theorem 3.1 in ?) and ([A.3](https://arxiv.org/html/2602.14575v1#Ax1.E3 "In Appendix A: Proof of Theorem 2.2")) the sum

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=1nωk=∑k=1nπτ∗,k=1,\sum\_{k=1}^{n}\omega^{k}=\sum\_{k=1}^{n}\pi^{\*,k}\_{\tau}=1, |  | (A.5) |

which proves Equation ([2.7](https://arxiv.org/html/2602.14575v1#S2.E7 "In Theorem 2.2 ‣ 2.2 Benchmark ‣ 2 Market of Factors")). By ([A.3](https://arxiv.org/html/2602.14575v1#Ax1.E3 "In Appendix A: Proof of Theorem 2.2")) one obtains the Equation ([2.8](https://arxiv.org/html/2602.14575v1#S2.E8 "In Theorem 2.2 ‣ 2.2 Benchmark ‣ 2 Market of Factors")) and the SDE ([2.9](https://arxiv.org/html/2602.14575v1#S2.E9 "In Theorem 2.2 ‣ 2.2 Benchmark ‣ 2 Market of Factors")), which completes the proof of Theorem [2.2](https://arxiv.org/html/2602.14575v1#S2.Thmtheorem2 "Theorem 2.2 ‣ 2.2 Benchmark ‣ 2 Market of Factors").

## Appendix B: Proof of Theorem [2.4](https://arxiv.org/html/2602.14575v1#S2.Thmtheorem4 "Theorem 2.4 ‣ 2.3 Numéraire Portfolio ‣ 2 Market of Factors")

Proof:
Since the savings account Sτ0≡1S^{0}\_{\tau}\equiv 1 is a traded security in the extended market, it follows from Theorem 3.1 in ?) that the risk-adjusted return of this market is zero. For a savings account denominated portfolio SτπS^{\pi}\_{\tau}, which invests with the weight πτ0\pi^{0}\_{\tau} in the savings account Sτ0S^{0}\_{\tau} and with the weight πτk\pi^{k}\_{\tau} in the kk-th factor SτkS^{k}\_{\tau}, k∈{1,…,n}k\in\{1,...,n\}, it follows by Equation (3.8) and Equation (3.11) in Theorem 3.1 in ?) that this portfolio equals the NP Sτ∗∗S^{\*\*}\_{\tau} when it satisfies the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sτ∗∗Sτ∗∗=∑k=1nθτ∗∗,k​(θτ∗∗,k​d​τ+d​Wτk)\frac{dS^{\*\*}\_{\tau}}{S^{\*\*}\_{\tau}}=\sum\_{k=1}^{n}\theta^{\*\*,k}\_{\tau}\left(\theta^{\*\*,k}\_{\tau}d\tau+dW^{k}\_{\tau}\right) |  | (B.1) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | θτ∗∗,k=πτ∗∗,k​βτk,\theta^{\*\*,k}\_{\tau}=\pi^{\*\*,k}\_{\tau}\beta^{k}\_{\tau}, |  | (B.2) |

which proves Equation ([2.14](https://arxiv.org/html/2602.14575v1#S2.E14 "In Theorem 2.4 ‣ 2.3 Numéraire Portfolio ‣ 2 Market of Factors")). By Equation (3.8) in Theorem 3.1 in ?) we have the kk-th market price of risk
and by the matrix equation (3.5) in Theorem 3.1 in ?) the equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | (βτk)2​πτ∗∗,k=λ^t+(βτk)2​ωk,(\beta^{k}\_{\tau})^{2}\pi^{\*\*,k}\_{\tau}=\hat{\lambda}\_{t}+(\beta^{k}\_{\tau})^{2}\omega^{k}, |  | (B.3) |

which is solved by the optimal kk-th NP weight

|  |  |  |  |
| --- | --- | --- | --- |
|  | πτ∗∗,k=λ^τ(βτk)2+ωk\pi^{\*\*,k}\_{\tau}=\frac{\hat{\lambda}\_{\tau}}{(\beta^{k}\_{\tau})^{2}}+\omega^{k} |  | (B.4) |

and yields the kk-th market price of risk

|  |  |  |  |
| --- | --- | --- | --- |
|  | θτ∗∗,k=λ^τβτk+ωk​βτk\theta^{\*\*,k}\_{\tau}=\frac{\hat{\lambda}\_{\tau}}{\beta^{k}\_{\tau}}+\omega^{k}\beta^{k}\_{\tau} |  | (B.5) |

for k∈{1,…,n}k\in\{1,...,n\} and τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty). We obtain by ([B.4](https://arxiv.org/html/2602.14575v1#Ax2.E4 "In Appendix B: Proof of Theorem 2.4")) and ([2.7](https://arxiv.org/html/2602.14575v1#S2.E7 "In Theorem 2.2 ‣ 2.2 Benchmark ‣ 2 Market of Factors")) the NP weight

|  |  |  |  |
| --- | --- | --- | --- |
|  | πτ∗∗,0=1−∑k=1nπτ∗∗,k=1−λ^τ​∑k=1n(βτk)−2−1=−λ^τ​∑k=1n(βτk)−2\pi^{\*\*,0}\_{\tau}=1-\sum\_{k=1}^{n}\pi^{\*\*,k}\_{\tau}=1-\hat{\lambda}\_{\tau}\sum\_{k=1}^{n}(\beta^{k}\_{\tau})^{-2}-1=-\hat{\lambda}\_{\tau}\sum\_{k=1}^{n}(\beta^{k}\_{\tau})^{-2} |  | (B.6) |

to be invested in the savings account Sτ0S^{0}\_{\tau}.
This completes the proof of Theorem [2.4](https://arxiv.org/html/2602.14575v1#S2.Thmtheorem4 "Theorem 2.4 ‣ 2.3 Numéraire Portfolio ‣ 2 Market of Factors").

## Appendix C: Proof of Theorem [3.4](https://arxiv.org/html/2602.14575v1#S3.Thmtheorem4 "Theorem 3.4 ‣ 3.2 Surprisal Minimization ‣ 3 Surprisal-Minimized Market")

Proof:
We perform the minimization of the surprisal

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐ​(p∞)=∑k=1nℐ​(p∞k),\mathcal{I}(p\_{\infty})=\sum\_{k=1}^{n}\mathcal{I}(p^{k}\_{\infty}), |  | (C.1) |

of the stationary joint density p∞p\_{\infty} in several steps.

1. At first, we derive the stationary densities of the normalized factors. For k∈{1,…,n}k\in\{1,...,n\}, the stationary density p∞kp^{k}\_{\infty} of the kk-th normalized factor, when it is evolving in the market time τ\tau,
is by the SDE ([3.11](https://arxiv.org/html/2602.14575v1#S3.E11 "In 3.1 Normalized Factors ‣ 3 Surprisal-Minimized Market")) the solution of the stationary Fokker-Planck equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​y​(p∞k​(y)​y​((ϕk​(y))−1​4​ωk−1)​ak)−12​d2d​y2​(p∞k​(y)​y2​4​akϕk​(y))=0,\frac{d}{dy}\left(p^{k}\_{\infty}(y)y((\phi^{k}(y))^{-1}4\omega^{k}-1)a^{k}\right)-\frac{1}{2}\frac{d^{2}}{dy^{2}}\left(p^{k}\_{\infty}(y)y^{2}\frac{4a^{k}}{\phi^{k}(y)}\right)=0, |  | (C.2) |

as described, e.g.,in Chapter 4 in ?), which is a second-order ODE. Its solution is given by the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | p∞k​(y)=Ck​ϕk​(y)4​y2​exp⁡{2​∫1yωk−ϕk​(u)4u​𝑑u}p^{k}\_{\infty}(y)=\frac{C\_{k}\phi^{k}(y)}{4y^{2}}\exp\left\{2\int\_{1}^{y}\frac{\omega^{k}-\frac{\phi^{k}(u)}{4}}{u}du\right\} |  | (C.3) |

for y∈(0,∞)y\in(0,\infty) and some constant Ck>0C\_{k}>0. The latter ensures that p∞kp^{k}\_{\infty} is a probability density.

2. Under the constraints ([3.6](https://arxiv.org/html/2602.14575v1#S3.E6 "In 3.1 Normalized Factors ‣ 3 Surprisal-Minimized Market")) and ([3.7](https://arxiv.org/html/2602.14575v1#S3.E7 "In 3.1 Normalized Factors ‣ 3 Surprisal-Minimized Market")), we minimize according to ([3.13](https://arxiv.org/html/2602.14575v1#S3.E13 "In Definition 3.2 ‣ 3.2 Surprisal Minimization ‣ 3 Surprisal-Minimized Market")) the surprisal

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐ​(p∞k)=−∫0∞ln⁡(p∞k​(y))​p∞k​(y)​𝑑y\mathcal{I}(p^{k}\_{\infty})=-\int\_{0}^{\infty}\ln(p^{k}\_{\infty}(y))p^{k}\_{\infty}(y)dy |  | (C.4) |

of the stationary probability density p∞kp^{k}\_{\infty} of the kk-th independent normalized factor Yτ.kkY^{k}\_{\tau^{k}\_{.}}, k∈{1,…,n}k\in\{1,...,n\}. According to the formula ([3.13](https://arxiv.org/html/2602.14575v1#S3.E13 "In Definition 3.2 ‣ 3.2 Surprisal Minimization ‣ 3 Surprisal-Minimized Market")), we minimize the Lagrangian

|  |  |  |
| --- | --- | --- |
|  | ℒ​(p∞k,λ0,λ1,λ2)=−∫0∞ln⁡(p∞k​(y))​p∞k​(y)​𝑑y+λ0​(∫0∞p∞k​(y)​𝑑y−1){\cal{L}}(p^{k}\_{\infty},\lambda\_{0},\lambda\_{1},\lambda\_{2})=-\int\_{0}^{\infty}\ln(p^{k}\_{\infty}(y))p^{k}\_{\infty}(y)dy+\lambda\_{0}\left(\int\_{0}^{\infty}p^{k}\_{\infty}(y)dy-1\right) |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | +λ1​(∫0∞y​p∞k​(y)​𝑑y−4​ωk)+λ2​(∫0∞ln⁡(y)​p∞k​(y)​𝑑y−ζk),+\lambda\_{1}\left(\int\_{0}^{\infty}yp^{k}\_{\infty}(y)dy-4\omega^{k}\right)+\lambda\_{2}\left(\int\_{0}^{\infty}\ln(y)p^{k}\_{\infty}(y)dy-\zeta^{k}\right), |  | (C.5) |

where λ0,λ1,λ2\lambda\_{0},\lambda\_{1},\lambda\_{2} are Lagrange multipliers. ℒ​(p∞k,λ0,λ1,λ2){\cal{L}}(p^{k}\_{\infty},\lambda\_{0},\lambda\_{1},\lambda\_{2}) is minimized when its Fréchet derivative δ​ℒ​(p∞k,λ0,λ1,λ2)\delta{\cal{L}}(p^{k}\_{\infty},\lambda\_{0},\lambda\_{1},\lambda\_{2}), i.e., the first variation of ℒ​(p∞k,λ0,λ1,λ2){\cal{L}}(p^{k}\_{\infty},\lambda\_{0},\lambda\_{1},\lambda\_{2}) with respect to admissible variations of p∞kp^{k}\_{\infty}, becomes zero. This implies for the surprisal-minimized stationary density p∞kp^{k}\_{\infty} the equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​ℒ​(p∞k,λ0,λ1,λ2)=∫0∞(−ln⁡(p∞k​(y))+λ0+λ1​y+λ2​ln⁡(y))​δ​p∞k​(y)​𝑑y=0.\delta{\cal{L}}(p^{k}\_{\infty},\lambda\_{0},\lambda\_{1},\lambda\_{2})=\int\_{0}^{\infty}\left(-\ln(p^{k}\_{\infty}(y))+\lambda\_{0}+\lambda\_{1}y+\lambda\_{2}\ln(y)\right)\delta p^{k}\_{\infty}(y)dy=0. |  | (C.6) |

The solution of the above first-order condition is the gamma density

|  |  |  |  |
| --- | --- | --- | --- |
|  | p∞k​(y)=exp⁡{λ0+λ1​y+λ2​ln⁡(y)}p^{k}\_{\infty}(y)=\exp\{\lambda\_{0}+\lambda\_{1}y+\lambda\_{2}\ln(y)\} |  | (C.7) |

for y∈(0,∞)y\in(0,\infty) with the constraint

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0∞exp⁡{λ0+λ1​y+λ2​ln⁡(y)}​𝑑y=1,\int\_{0}^{\infty}\exp\{\lambda\_{0}+\lambda\_{1}y+\lambda\_{2}\ln(y)\}dy=1, |  | (C.8) |

and the Lagrange multipliers λ0,λ1,λ2\lambda\_{0},\lambda\_{1},\lambda\_{2}. It
has 2​(λ2+1)2(\lambda\_{2}+1) degrees of freedom and as parameters and constraints the averages

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐄p∞k​(Y.k)=λ2+1−λ1=4​ωk{\bf{E}}^{p^{k}\_{\infty}}(Y^{k}\_{.})=\frac{\lambda\_{2}+1}{-\lambda\_{1}}=4\omega^{k} |  | (C.9) |

and

|  |  |  |
| --- | --- | --- |
|  | 𝐄p∞k​(ln⁡(Y.k))=ζk.{\bf{E}}^{p^{k}\_{\infty}}(\ln(Y^{k}\_{.}))=\zeta^{k}. |  |

3. The SDE for the kk-th normalized factor is given by ([3.11](https://arxiv.org/html/2602.14575v1#S3.E11 "In 3.1 Normalized Factors ‣ 3 Surprisal-Minimized Market")).
Consequently, the stationary density p∞k​(y)p^{k}\_{\infty}(y) of the kk-th normalized factor satisfies the Fokker-Planck equation with the drift and diffusion coefficient functions of the SDE ([3.11](https://arxiv.org/html/2602.14575v1#S3.E11 "In 3.1 Normalized Factors ‣ 3 Surprisal-Minimized Market")). This yields the stationary density p∞k​(y)p^{k}\_{\infty}(y) in the form ([C.3](https://arxiv.org/html/2602.14575v1#Ax3.E3 "In Appendix C: Proof of Theorem 3.4")). The latter must equal the above-identified gamma density. By setting both expressions for the stationary density equal, respective conditions for the function ϕk​(y)\phi^{k}(y) emerge.
  
The Weierstrass Approximation Theorem states that a continuous function can be approximated on a bounded interval by a polynomial. When using a polynomial for characterizing ϕk​(y)\phi^{k}(y) and searching for a match of the stationary density ([C.3](https://arxiv.org/html/2602.14575v1#Ax3.E3 "In Appendix C: Proof of Theorem 3.4")) with the gamma density ([C.7](https://arxiv.org/html/2602.14575v1#Ax3.E7 "In Appendix C: Proof of Theorem 3.4")), then one finds by comparing the coefficients of the possible polynomials that only the polynomial

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕk​(y)=y\phi^{k}(y)=y |  | (C.10) |

provides such a match.
This yields for the kk-th normalized factor process Y.kY^{k}\_{.} the
stationary density

|  |  |  |  |
| --- | --- | --- | --- |
|  | p∞k​(y)=Ck​y4​y2​exp⁡{2​∫1yωk−u4u​𝑑u}=y2​ωk−122​ωk​Γ​(2​ωk)​exp⁡{−y2}p^{k}\_{\infty}(y)=\frac{C\_{k}y}{4y^{2}}\exp\left\{2\int\_{1}^{y}\frac{\omega^{k}-\frac{u}{4}}{u}du\right\}=\frac{y^{2\omega^{k}-1}}{2^{2\omega^{k}}\Gamma(2\omega^{k})}\exp\left\{-\frac{y}{2}\right\} |  | (C.11) |

for y>0y>0. The above density is the gamma density with dk=4​ωkd\_{k}=4\omega^{k} degrees of freedom and mean 4​ωk4\omega^{k}. We assumed
the logarithmic average of the stationary density to equal a constant ζk\zeta^{k}, which emerges as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζk=𝐄p∞k​(ln⁡(Y.k))=ln⁡(2)+ψ​(2​ωk),\zeta^{k}={\bf{E}}^{p^{k}\_{\infty}}(\ln(Y^{k}\_{.}))=\ln\left(2\right)+\psi(2\omega^{k}), |  | (C.12) |

where the function ψ​(x)\psi(x)
is the diagamma function; see, e.g., ?) or ?).
  
4. The resulting CIR process is a stationary process where its initial value Yτt0k=Sτt0kY^{k}\_{\tau\_{t\_{0}}}=S^{k}\_{\tau\_{t\_{0}}} is distributed according to its stationary density.
This yields with

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐ=∑k=1n1n​ℐ​(p∞k)\sqrt{\mathcal{I}}=\sum\_{k=1}^{n}\frac{1}{n}\sqrt{\mathcal{I}(p^{k}\_{\infty})} |  | (C.13) |

the surprisal of the stationary joint density

|  |  |  |
| --- | --- | --- |
|  | ℐ​(p∞)=n​∑k=1n1n​ℐ​(p∞k)=n​∑k=1n1n​(ℐ​(p∞k))2\mathcal{I}(p\_{\infty})=n\sum\_{k=1}^{n}\frac{1}{n}\mathcal{I}(p^{k}\_{\infty})=n\sum\_{k=1}^{n}\frac{1}{n}\left(\sqrt{\mathcal{I}(p^{k}\_{\infty})}\right)^{2} |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | =n​((ℐ)2+∑k=1n1n​(ℐ​(p∞k)−ℐ)2).=n\left((\sqrt{\mathcal{I}})^{2}+\sum\_{k=1}^{n}\frac{1}{n}\left(\sqrt{\mathcal{I}(p^{k}\_{\infty})}-\sqrt{\mathcal{I}}\right)^{2}\right). |  | (C.14) |

The latter is minimized for

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐ​(p∞k)=ℐ,\sqrt{\mathcal{I}(p^{k}\_{\infty})}=\sqrt{\mathcal{I}}, |  | (C.15) |

which means by ([2.7](https://arxiv.org/html/2602.14575v1#S2.E7 "In Theorem 2.2 ‣ 2.2 Benchmark ‣ 2 Market of Factors")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ωk=1n.\omega^{k}=\frac{1}{n}. |  | (C.16) |

According to ?), the kk-th normalized factor is a CIR process and, more generally, an SROU process that represents a unique strong solution of the SDE ([3.14](https://arxiv.org/html/2602.14575v1#S3.E14 "In Theorem 3.4 ‣ 3.2 Surprisal Minimization ‣ 3 Surprisal-Minimized Market")), which completes the proof of Theorem [3.4](https://arxiv.org/html/2602.14575v1#S3.Thmtheorem4 "Theorem 3.4 ‣ 3.2 Surprisal Minimization ‣ 3 Surprisal-Minimized Market").

## Appendix D: Proof of Theorem [3.6](https://arxiv.org/html/2602.14575v1#S3.Thmtheorem6 "Theorem 3.6 ‣ 3.3 Benchmark Dynamics ‣ 3 Surprisal-Minimized Market")

Proof:
  
1. Let us consider a market time τ∈𝒯\tau\in\mathcal{T} when no normalized factor equals zero. By employing Theorem [2.2](https://arxiv.org/html/2602.14575v1#S2.Thmtheorem2 "Theorem 2.2 ‣ 2.2 Benchmark ‣ 2 Market of Factors") with ([2.9](https://arxiv.org/html/2602.14575v1#S2.E9 "In Theorem 2.2 ‣ 2.2 Benchmark ‣ 2 Market of Factors")) and ([3.10](https://arxiv.org/html/2602.14575v1#S3.E10 "In 3.1 Normalized Factors ‣ 3 Surprisal-Minimized Market")),
it follows for the benchmark the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sτ∗Sτ∗=λ^τ​d​τ+∑k=1n1n​4​akYττkk​(1n​4​akYττkk​d​τ+d​Wτk).\frac{dS^{\*}\_{\tau}}{S^{\*}\_{\tau}}=\hat{\lambda}\_{\tau}d\tau+\sum\_{k=1}^{n}\frac{1}{n}\sqrt{\frac{4a^{k}}{Y^{k}\_{\tau^{k}\_{\tau}}}}\left(\frac{1}{n}\sqrt{\frac{4a^{k}}{Y^{k}\_{\tau^{k}\_{\tau}}}}d\tau+d{W}^{k}\_{\tau}\right). |  | (D.1) |

By using ([3.20](https://arxiv.org/html/2602.14575v1#S3.E20 "In Theorem 3.6 ‣ 3.3 Benchmark Dynamics ‣ 3 Surprisal-Minimized Market")), one can rewrite this SDE in the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sτ∗=λ^τ​Sτ∗​d​τ+Zτ​Sτ∗​d​τ+Zτ​Sτ∗​d​Wτ∗,dS^{\*}\_{\tau}=\hat{\lambda}\_{\tau}S^{\*}\_{\tau}d\tau+Z\_{\tau}S^{\*}\_{\tau}d\tau+\sqrt{Z\_{\tau}}S^{\*}\_{\tau}d{W}^{\*}\_{\tau}, |  | (D.2) |

where the Brownian motion Wτ∗W^{\*}\_{\tau} has the stochastic differential given in ([3.21](https://arxiv.org/html/2602.14575v1#S3.E21 "In Theorem 3.6 ‣ 3.3 Benchmark Dynamics ‣ 3 Surprisal-Minimized Market"))
with initial value Wτt0∗=0W^{\*}\_{\tau\_{t\_{0}}}=0. This proves the SDE ([3.19](https://arxiv.org/html/2602.14575v1#S3.E19 "In Theorem 3.6 ‣ 3.3 Benchmark Dynamics ‣ 3 Surprisal-Minimized Market")) together with ([3.20](https://arxiv.org/html/2602.14575v1#S3.E20 "In Theorem 3.6 ‣ 3.3 Benchmark Dynamics ‣ 3 Surprisal-Minimized Market")) and
([3.21](https://arxiv.org/html/2602.14575v1#S3.E21 "In Theorem 3.6 ‣ 3.3 Benchmark Dynamics ‣ 3 Surprisal-Minimized Market")).
  
2. Similarly as in ([3.1](https://arxiv.org/html/2602.14575v1#S3.E1 "In 3.1 Normalized Factors ‣ 3 Surprisal-Minimized Market")), one can introduce the normalized benchmark Yττ∗∗Y^{\*}\_{\tau^{\*}\_{\tau}} via the formula ([3.22](https://arxiv.org/html/2602.14575v1#S3.E22 "In Theorem 3.6 ‣ 3.3 Benchmark Dynamics ‣ 3 Surprisal-Minimized Market")).
By application of the Itô formula, Equation ([3.22](https://arxiv.org/html/2602.14575v1#S3.E22 "In Theorem 3.6 ‣ 3.3 Benchmark Dynamics ‣ 3 Surprisal-Minimized Market")), and ([3.20](https://arxiv.org/html/2602.14575v1#S3.E20 "In Theorem 3.6 ‣ 3.3 Benchmark Dynamics ‣ 3 Surprisal-Minimized Market")) it follows that Yττ∗∗Y^{\*}\_{\tau^{\*}\_{\tau}} satisfies the SDE

|  |  |  |
| --- | --- | --- |
|  | d​Yττ∗∗Yττ∗∗=λ^τ​d​τ+(Zτ−aτ∗)​d​τ+Zτ​d​Wτ∗\frac{dY^{\*}\_{\tau^{\*}\_{\tau}}}{Y^{\*}\_{\tau^{\*}\_{\tau}}}=\hat{\lambda}\_{\tau}d\tau+\left(Z\_{\tau}-a^{\*}\_{\tau}\right)d\tau+\sqrt{Z\_{\tau}}dW^{\*}\_{\tau} |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | =λ^τ​d​τ+(4Yττ∗∗−1)​aτ∗​d​τ+4​aτ∗Yττ∗∗​d​Wτ∗=\hat{\lambda}\_{\tau}d\tau+\left(\frac{4}{Y^{\*}\_{\tau^{\*}\_{\tau}}}-1\right)a^{\*}\_{\tau}d\tau+\sqrt{\frac{4a^{\*}\_{\tau}}{Y^{\*}\_{\tau^{\*}\_{\tau}}}}dW^{\*}\_{\tau} |  | (D.3) |

and is forming an SROU process of dimension four satisfying the SDE ([3.24](https://arxiv.org/html/2602.14575v1#S3.E24 "In Theorem 3.6 ‣ 3.3 Benchmark Dynamics ‣ 3 Surprisal-Minimized Market")) that
evolves in the benchmark time

|  |  |  |  |
| --- | --- | --- | --- |
|  | ττ∗=ττt0∗+∫τt0τas∗​𝑑s\tau^{\*}\_{\tau}=\tau^{\*}\_{\tau\_{t\_{0}}}+\int\_{\tau\_{t\_{0}}}^{\tau}a^{\*}\_{s}ds |  | (D.4) |

with the benchmark activity

|  |  |  |  |
| --- | --- | --- | --- |
|  | aτ∗=14​Zτ​Yττ∗∗.a^{\*}\_{\tau}=\frac{1}{4}Z\_{\tau}Y^{\*}\_{\tau^{\*}\_{\tau}}. |  | (D.5) |

This proves the remaining statements of Theorem [3.6](https://arxiv.org/html/2602.14575v1#S3.Thmtheorem6 "Theorem 3.6 ‣ 3.3 Benchmark Dynamics ‣ 3 Surprisal-Minimized Market").

## Appendix E: Proof of Theorem [4.4](https://arxiv.org/html/2602.14575v1#S4.Thmtheorem4 "Theorem 4.4 ‣ 4.2 Information Minimization ‣ 4 Information-Minimized Market")

Proof:
For a surprisal-minimized market one can write the Radon-Nikodym derivative ΛQS∗​(τ)\Lambda\_{Q\_{S^{\*}}}(\tau), given in ([4.1](https://arxiv.org/html/2602.14575v1#S4.E1 "In 4.1 Benchmark-Neutral Pricing ‣ 4 Information-Minimized Market")), of the BN pricing measure QS∗Q\_{S^{\*}} as the product

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΛQS∗​(τ)=∏k=1nΛQS∗k​(τ),\Lambda\_{Q\_{S^{\*}}}(\tau)=\prod\_{k=1}^{n}\Lambda\_{Q\_{S^{\*}}}^{k}(\tau), |  | (E.1) |

of the independent martingales

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΛQS∗k​(τ)=exp⁡{−12​∫τt0τλ^2​Yτskk4​ak​𝑑s−∫τt0τλ^2​Yτskk4​ak​𝑑Wsk}\Lambda\_{Q\_{S^{\*}}}^{k}(\tau)=\exp\left\{-\frac{1}{2}\int\_{\tau\_{t\_{0}}}^{\tau}\frac{\hat{\lambda}^{2}Y^{k}\_{\tau^{k}\_{s}}}{4a^{k}}ds-\int\_{\tau\_{t\_{0}}}^{\tau}\sqrt{\frac{\hat{\lambda}^{2}Y^{k}\_{\tau^{k}\_{s}}}{4a^{k}}}dW^{k}\_{s}\right\} |  | (E.2) |

for k∈{1,…,n}k\in\{1,...,n\} and τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty). According to Equation ([4.8](https://arxiv.org/html/2602.14575v1#S4.E8 "In Definition 4.2 ‣ 4.2 Information Minimization ‣ 4 Information-Minimized Market")), ([E.2](https://arxiv.org/html/2602.14575v1#Ax5.E2 "In Appendix E: Proof of Theorem 4.4")), and ([3.6](https://arxiv.org/html/2602.14575v1#S3.E6 "In 3.1 Normalized Factors ‣ 3 Surprisal-Minimized Market")) we have to minimize the Kullback-Leibler divergence

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(p∞,q∞)=12​∑k=1n𝐄p∞​(λ^τ2​Yττkk4​ak)=12​n​∑k=1nλ^τ2ak→minI(p\_{\infty},q\_{\infty})=\frac{1}{2}\sum\_{k=1}^{n}{\bf{E}}^{p\_{\infty}}\left(\frac{\hat{\lambda}\_{\tau}^{2}Y^{k}\_{\tau^{k}\_{\tau}}}{4a^{k}}\right)=\frac{1}{2n}\sum\_{k=1}^{n}\frac{\hat{\lambda}\_{\tau}^{2}}{a^{k}}\rightarrow\min |  | (E.3) |

of q∞q\_{\infty} from p∞p\_{\infty}. In ([3.9](https://arxiv.org/html/2602.14575v1#S3.E9 "In 3.1 Normalized Factors ‣ 3 Surprisal-Minimized Market")), the average of the inverse of the square root of the activity in market time is set to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=1n1n​1ak=1.\sum\_{k=1}^{n}\frac{1}{n}\sqrt{\frac{1}{a^{k}}}=1. |  | (E.4) |

This allows us to write the Kullback-Leibler divergence in the form

|  |  |  |
| --- | --- | --- |
|  | I​(p∞,q∞)=λ^τ22​n​∑k=1n1ak=λ^τ22​((∑k=1n1n​1ak)2+∑k=1n1n​(1ak−1)2)I(p\_{\infty},q\_{\infty})=\frac{\hat{\lambda}\_{\tau}^{2}}{2n}\sum\_{k=1}^{n}\frac{1}{a^{k}}=\frac{\hat{\lambda}\_{\tau}^{2}}{2}\left(\left(\sum\_{k=1}^{n}\frac{1}{n}\sqrt{\frac{1}{a^{k}}}\right)^{2}+\sum\_{k=1}^{n}\frac{1}{n}\left(\sqrt{\frac{1}{a^{k}}}-1\right)^{2}\right) |  |

|  |  |  |
| --- | --- | --- |
|  | =λ^τ22​(1+∑k=1n1n​(1ak−1)2).=\frac{\hat{\lambda}\_{\tau}^{2}}{2}\left(1+\sum\_{k=1}^{n}\frac{1}{n}\left(\sqrt{\frac{1}{a^{k}}}-1\right)^{2}\right). |  |

This expression is minimized with respect to the activities if all activities are equal with value

|  |  |  |  |
| --- | --- | --- | --- |
|  | ak=1,a^{k}=1, |  | (E.5) |

which proves ([4.9](https://arxiv.org/html/2602.14575v1#S4.E9 "In Theorem 4.4 ‣ 4.2 Information Minimization ‣ 4 Information-Minimized Market")) and yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(p∞,q∞)=λ^τ22I(p\_{\infty},q\_{\infty})=\frac{\hat{\lambda}\_{\tau}^{2}}{2} |  | (E.6) |

for τ∈[τt0,∞)\tau\in[\tau\_{t\_{0}},\infty).
  
Since the stationary probability densities p∞p\_{\infty} and q∞q\_{\infty} do not change over market time,
we obtain the net risk-adjusted return

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ^τ=2​I​(p∞,q∞)=λ^\hat{\lambda}\_{\tau}=\sqrt{2I(p\_{\infty},q\_{\infty})}=\hat{\lambda} |  | (E.7) |

as a constant.
This proves ([4.11](https://arxiv.org/html/2602.14575v1#S4.E11 "In Theorem 4.4 ‣ 4.2 Information Minimization ‣ 4 Information-Minimized Market")) and, therefore, Theorem [4.4](https://arxiv.org/html/2602.14575v1#S4.Thmtheorem4 "Theorem 4.4 ‣ 4.2 Information Minimization ‣ 4 Information-Minimized Market").

## References

* Abramowitz & Stegun (1972

  Abramowitz, M. & I. A. Stegun (Eds.) (1972).
  Handbook of Mathematical Functions with Formulas, Graphs, and
  Mathematical Tables.
  Dover, New York.
* Ait-Sahalia, Fan & Li (2013

  Ait-Sahalia, Y., J. Fan, & Y. Li (2013).
  The leverage effect puzzle: Disentangling sources of bias at high
  frequency.
  Journal Financial Economics 109(1), 224–249.
* Bachelier (1900

  Bachelier, L. (1900).
  Théorie de la spéculation.
  Annales de l’Ecole Normale Supérieure, Series 3 17,
  21–86.
* Baldeaux & Platen (2013

  Baldeaux, J. & E. Platen (2013).
  Functionals of Multidimensional Diffusions with Applications to
  Finance.
  Springer.
* Barone-Adesi, Platen & Sala (2024

  Barone-Adesi, G., E. Platen, & C. Sala (2024).
  Managing the shortfall risk of target date funds by overfunding.
  Journal of Pension Economics and Finance, 1–25.
* Bayer, Friz & Gatheral (2016

  Bayer, C., P. Friz, & J. Gatheral (2016).
  Pricing under rough volatility.
  Quant. Finance. 16(6), 887–904.
* Becherer (2001

  Becherer, D. (2001).
  The numeraire portfolio for unbounded semimartingales.
  Finance and Stochastics 5(3), 327–341.
* Black (1976a

  Black, F. (1976a).
  The pricing of commodity contracts.
  J. Financial Economics 3, 167–179.
* Black (1976b

  Black, F. (1976b).
  Studies in stock price volatility changes.
  In Proceedings of the 1976 Business Meeting of the Business and
  Economic Statistics Section, American Statistical Association, pp. 177–181.
* Black & Scholes (1973

  Black, F. & M. Scholes (1973).
  The pricing of options and corporate liabilities.
  J. Political Economy 81, 637–654.
* Bochner (1955

  Bochner, S. (1955).
  Harmonic Analysis and the Theory of Probability.
  University of California Press, Berkeley, CA.
* Breeden & Litzenberger (1978

  Breeden, D. T. & R. Litzenberger (1978).
  Prices of state-contingent claims implicit in option prices.
  J. Business 51, 621–651.
* Breymann, Lüthi & Platen (2009

  Breymann, W., D. Lüthi, & E. Platen (2009).
  Empirical behavior of a world stock index from intra-day to monthly
  time scales.
  The European Physical Journal B 71, 511–522.
* Clark (1973

  Clark, P. K. (1973).
  A subordinated stochastic process model with finite variance for
  speculative prices.
  Econometrica 41, 135–159.
* Cox (1975

  Cox, J. C. (1975).
  Notes on option pricing I: constant elasticity of variance
  diffusions.
  Stanford University, (working paper, unpublished).
* Cox, Ingersoll & Ross (1985

  Cox, J. C., J. E. Ingersoll, & S. A. Ross (1985).
  A theory of the term structure of interest rates.
  Econometrica 53, 385–407.
* Craddock & Platen (2004

  Craddock, M. & E. Platen (2004).
  Symmetry group methods for fundamental solutions.
  J. of Differential Equations 207(2), 285–302.
* Delbaen & Schachermayer (1998

  Delbaen, F. & W. Schachermayer (1998).
  The fundamental theorem of asset pricing for unbounded stochastic
  processes.
  Math. Ann. 312, 215–250.
* Derman & Kani (1994

  Derman, E. & I. Kani (1994).
  The volatility smile and its implied tree.
  Goldman Sachs Quantitative Strategies Research Notes.
* Dupire (1994

  Dupire, B. (1994).
  Pricing with a smile.
  Risk 7, 18–20.
* El Euch, Fukasawa & Rosenbaum (2018

  El Euch, O., M. Fukasawa, & M. Rosenbaum (2018).
  The microstructural foundations of leverage effect and rough
  volatility.
  Finance and Stochastics 22(1), 241–280.
* Engle (1982

  Engle, R. F. (1982).
  Autoregressive conditional heteroskedasticity with estimates of the
  variance of U.K. inflation.
  Econometrica 50(4), 987–1007.
* Fama (1970

  Fama, E. F. (1970).
  Efficient capital markets: a review of theory and empirical work.
  The Journal of Finance 25(2), 383–417.
* Feller (1971

  Feller, W. (1971).
  An Introduction to Probability Theory and Its Applications
  (2nd ed.), Volume 2.
  Wiley, New York.
* Fergusson & Platen (2006

  Fergusson, K. & E. Platen (2006).
  On the distributional characterization of log-returns of a world
  stock index.
  Applied Mathematical Finance 13(1), 19–38.
* Fergusson & Platen (2023

  Fergusson, K. & E. Platen (2023).
  Less-expensive valuation of long-term annuities linked to mortality,
  cash and equity.
  Annals of Actuarial Science 17(1), 170–207.
* Filipović & Platen (2009

  Filipović, D. & E. Platen (2009).
  Consistent market extensions under the benchmark approach.
  Mathematical Finance 19(1), 41–52.
* Fouque, Papanicolau & Sircar (1999

  Fouque, J. P., G. Papanicolau, & K. R. Sircar (1999).
  Financial modelling in a fast mean-reverting stochastic volatility
  environment.
  Asia-Pacific Financial Markets 6, 37–48.
* Geman, El Karoui & Rochet (1995

  Geman, S., N. El Karoui, & J. C. Rochet (1995).
  Changes of numeraire, changes of probability measures and pricing of
  options.
  Journal Applied Probability 32, 443–458.
* Goard & Mazur (2013

  Goard, J. & M. Mazur (2013).
  Stochastic volatility models and the pricing of vix options.
  Math. Finance 23(3), 439–458.
* Göing-Jaeschke & Yor (2003

  Göing-Jaeschke, A. & M. Yor (2003).
  A survey and some generalizations of Bessel processes.
  Bernoulli 9(2), 313–349.
* Grossman & Stiglitz (1980

  Grossman, S. & J. Stiglitz (1980).
  Impossibility of informationally efficient markets.
  The American Economic Review 70(3), 393–408.
* Hagan, Kumar, Lesniewski & Woodward (2002

  Hagan, P. S., D. Kumar, A. S. Lesniewski, & D. Woodward (2002).
  Managing smile risk.
  Willmot, 84–108.
* Heston (1993

  Heston, S. L. (1993).
  A closed-form solution for options with stochastic volatility with
  applications to bond and currency options.
  Review of Financial Studies 6(2), 327–343.
* Heston (1997

  Heston, S. L. (1997).
  A simple new formula for options with stochastic volatility.
  Technical report, Washington University of St. Louis.
* Hulley & Schweizer (2010

  Hulley, H. & M. Schweizer (2010).
  M6 - On minimal market models and minimal martingale measures.
  In C. Chiarella and A. Novikov (Eds.), Contemporary Quantitative
  Finance - Essays in Honour of Eckhard Platen. Springer.
* Hurst & Platen (1997

  Hurst, S. R. & E. Platen (1997).
  The marginal distributions of returns and volatility.
  In Y. Dodge (Ed.), L1L\_{1}-Statistical Procedures and Related
  Topics, Volume 31 of IMS Lecture Notes - Monograph Series, pp. 301–314. Institute of Mathematical Statistics Hayward, California.
* Jarrow (2022

  Jarrow, R. (2022).
  Continuous-Time Asset Pricing Theory.
  Springer-Finance, Second Edition.
* Johnson, Kotz & Balakrishnan (1995

  Johnson, N. L., S. Kotz, & N. Balakrishnan (1995).
  Continuous Univariate Distributions (2nd ed.), Volume 2 of
  Wiley Series in Probability and Mathematical Statistics.
  John Wiley & Sons.
* Karatzas & Kardaras (2007

  Karatzas, I. & C. Kardaras (2007).
  The numeraire portfolio in semimartingale financial models.
  Finance and Stochastics 11(4), 447–493.
* Karatzas & Shreve (1998

  Karatzas, I. & S. E. Shreve (1998).
  Methods of Mathematical Finance.
  Springer.
* Kelly (1956

  Kelly, J. R. (1956).
  A new interpretation of information rate.
  Bell Systems Technology Journal 35, 917–926.
* Kosmann-Schwarzbach (2018

  Kosmann-Schwarzbach, Y. (2018).
  The Noether Theorems.
  Springer.
* Kullback (1959

  Kullback, S. (1959).
  Information Theory and Statistics.
  New York, Wiley.
* Long (1990

  Long, J. B. (1990).
  The numeraire portfolio.
  J. Financial Economics 26, 29–69.
* MacLean, Thorp & Ziemba (2011

  MacLean, L., E. Thorp, & W. Ziemba (2011).
  The Kelly Capital Growth Investment Criterion.
  World Scientific.
* Mandelbrot (2001

  Mandelbrot, B. (2001).
  Scaling in financial prices: I. Tails and dependence.
  Quant. Finance. 1, 113–123.
* Markowitz & Usmen (1996a

  Markowitz, H. & N. Usmen (1996a).
  The likelihood of various stock market return distributions, Part
  1: Principles of inference.
  J. Risk &\& Uncertainty 13(3), 207–219.
* Markowitz & Usmen (1996b

  Markowitz, H. & N. Usmen (1996b).
  The likelihood of various stock market return distributions, Part
  2: Empirical results.
  J. Risk &\& Uncertainty 13(3), 221–247.
* Merton (1971

  Merton, R. C. (1971).
  Optimum consumption and portfolio rules in a continuous-time model.
  J. Economic Theory 3(4), 373–413.
* Noether (1918

  Noether, E. (1918).
  Invariante variationsprobleme.
  Goettinger Nachrichten, 235–247.
* Platen (1997

  Platen, E. (1997).
  A non-linear stochastic volatility model.
  Technical report, Australian National University.
  FMRR 005-97.
* Platen (2001

  Platen, E. (2001).
  A minimal financial market model.
  In Trends in Mathematics, pp. 293–301. Birkhäuser.
* Platen (2006

  Platen, E. (2006).
  A benchmark approach to finance.
  Mathematical Finance 16(1), 131–151.
* Platen (2025

  Platen, E. (2025).
  Benchmark-neutral pricing.
  Quantitative Finance 25(12), 1907–1919.
  open access, https://doi.org/10.1080/14697688.2025.2577115.
* Platen (2026

  Platen, E. (2026).
  Generalized minimal market model.
  Technical report.
  https://ssrn.com/abstract=.
* Platen & Fergusson (2025

  Platen, E. & K. Fergusson (2025).
  Free lunches with vanishing risks most likely exist.
  Technical report.
  arXiv preprint arXiv:2508.07108.
* Platen & Heath (2006

  Platen, E. & D. Heath (2006).
  A Benchmark Approach to Quantitative Finance.
  Springer Finance. Springer.
* Platen & Rendek (2008

  Platen, E. & R. Rendek (2008).
  Empirical evidence on Student-tt log-returns of diversified world
  stock indices.
  Journal of Statistical Theory and Practice 2(2),
  233–251.
* Platen & Rendek (2012

  Platen, E. & R. Rendek (2012).
  Approximating the numéraire portfolio by naive diversification.
  Journal of Asset Management 13(1), 34–50.
* Platen & Rendek (2019

  Platen, E. & R. Rendek (2019).
  Dynamics of a well-diversified equity index.
  Technical report, University of Technology Sydney, QFRC Research
  Paper 398, SSRN 3317320.
* Revuz & Yor (1999

  Revuz, D. & M. Yor (1999).
  Continuous Martingales and Brownian Motion (3rd ed.).
  Springer.
* Schmutz, Platen & Schmidt (2025

  Schmutz, M., E. Platen, & T. Schmidt (2025).
  Benchmark-neutral risk-minimization for insurance products and
  nonreplicable claims.
  ArXiv:2506.19494,.
* Shannon (1948

  Shannon, C. (1948).
  A mathematical theory of communication.
  Bell System Technical Journal 27(3).
* Shiga & Watanabe (1973

  Shiga, T. & S. Watanabe (1973).
  Bessel diffusion as a one parameter family of diffusion processes.
  Zeitschrift fuer Wahrscheinlichkeitstheorie und Verwandte
  Gebiete 27, 37–46.