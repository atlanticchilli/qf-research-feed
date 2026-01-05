---
authors:
- Pengpeng Li
- Shi-Dong Liang
doc_id: arxiv:2601.00293v1
family_id: arxiv:2601.00293
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach'
url_abs: http://arxiv.org/abs/2601.00293v1
url_html: https://arxiv.org/html/2601.00293v1
venue: arXiv q-fin
version: 1
year: 2026
---


Pengpeng Li and Shi-Dong Liang
  
School of Physics, Sun Yat-Sen University
  
Guangzhou, China
stslsd@mail.sysu.edu.cn

(January 1, 2026)

###### Abstract

Based on the analog between the stochastic dynamics and quantum harmonic oscillator, we
propose a market force driving model to generalize the Black-Scholes model in finance market. We give new schemes of option pricing, in which we can take various unexpected
market behaviors into account to modify the option pricing. As examples, we present several market forces to analyze their effects on the option pricing. These results provide us two practical applications. One is to be used as a new scheme of option pricing when we can predict some hidden market forces or behaviors emerging. The other implies
the existence of some risk premium when some unexpected forces emerge.

## 1 Introduction

The option pricing is a crucial issue in finance.
The Black-Scholes model gives a guideline to price options by the risk-free scheme,
which assumes the portfolio satisfies the no-arbitrage condition, perfectly hedge,
invariant interests, no transaction cost and the continuous evolution of prices. [[1](https://arxiv.org/html/2601.00293v1#bib.bib1)] However, recently one discovers that above assumptions cannot hold in the practical finance markets, such as inconstant the risk-free interest rate, or non-continuously evolution, and fluctuate volatility,[[2](https://arxiv.org/html/2601.00293v1#bib.bib2)] which implies that the log return distribution (return is equal to the future price minus the original price) deviates normal (Guassian) distribution.
These phenomena induce a lot of interests to modify the Black-Scholes method.[[3](https://arxiv.org/html/2601.00293v1#bib.bib3), [4](https://arxiv.org/html/2601.00293v1#bib.bib4), [5](https://arxiv.org/html/2601.00293v1#bib.bib5), [6](https://arxiv.org/html/2601.00293v1#bib.bib6), [7](https://arxiv.org/html/2601.00293v1#bib.bib7)] Belal E. Baaquie proposed a path integral method to optimize the evaluation of path-dependent options.[[3](https://arxiv.org/html/2601.00293v1#bib.bib3)] By an elasticity variance model, Beni Lauterbach and Paul Schultz take the variant interest into account to give a new scheme of price.[[4](https://arxiv.org/html/2601.00293v1#bib.bib4)]
Moreover, Louis O. Scott proves that the accurate option prices can be computed via Monte Carlo simulations when the variance changes randomly.[[4](https://arxiv.org/html/2601.00293v1#bib.bib4), [5](https://arxiv.org/html/2601.00293v1#bib.bib5)] Interestingly,
H. Kleinert and J. Korbel claim that the prices of options can also be evaluated by the double-fractional differential equation and its solution provide a more reliable hedge comparing with Black-Scholes formula.[[6](https://arxiv.org/html/2601.00293v1#bib.bib6)]
Further, Lina Song and Weiguo Wang optimizes the fractional Black -Scholes Option pricing model by Finite Difference Method to give the solution of the difference equation.[[7](https://arxiv.org/html/2601.00293v1#bib.bib7)] More recently, Robert C. Merton generalized the stock return distribution to
give an option pricing formula for the discontinuous returns.[[8](https://arxiv.org/html/2601.00293v1#bib.bib8)]
Most importantly, considering the price distribution, R. N. Mantegna uses Levy Walk instead of original random walk and he gets a new price distribution deviating from normal distribution which can be applied into Black -Scholes Model. [[9](https://arxiv.org/html/2601.00293v1#bib.bib9)]
These studies on the generalized Black-Scholes model provide
many ways to improve the Black-Scholes model and to make the option price close the realistic finance market.

In fact, there exist some hidden market forces, such as shorting or buying an underlying asset in finance market, which drive the dynamics of finance market and make the stochastic process of the finance market deviate Guassian distribution.
This non-Guassian effect should modify the option pricing.
Therefore, in this paper, we will propose the market-force concepts to
describe the stochastic dynamics of finance market based on the quantum mechanics approach.
The stochastic dynamics of finance market is described by the wave function, which
follows the Schrödinger equation. The hidden market forces as
the market potential drive the stochastic dynamics of finance market, which
make the dynamics deviate the Guassian process and modify the Black-Scholes model which gives several schemes of option pricing.
In Sec. II, we present the market-force model of option pricing based on quantum mechanics.
In Sec. III, we propose several schemes of option pricing based on this model and discuss
their advantages and financial meanings. Finally we give the summary and conclusions
in Sec. IV.

## 2 Market force Model of Stochastic dynamics

### 2.1 Black-Scholes model

The dynamics of finance market is a stochastic process. The efficient market theory
assumes that there does not exist the arbitrage space, which implies that the
stochastic dynamics process is a Guassian process. The option pricing
of Black-Schole theory is based on the efficient market theory and the scheme
of option pricing is assumed to be risk free. The European call and put options are priced by

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | c\displaystyle c | =\displaystyle= | S0​N​(d+)−K​e−r​T​N​(d−)\displaystyle S\_{0}N(d\_{+})-Ke^{-rT}N(d\_{-}) |  | (1) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | p\displaystyle p | =\displaystyle= | K​e−r​T​N​(−d−)−S0​N​(−d+)\displaystyle Ke^{-rT}N(-d\_{-})-S\_{0}N(-d\_{+}) |  | (2) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | d±=l​n​(S0/K)+(r±σ2/2)​Tσ​Td\_{\pm}=\frac{ln(S\_{0}/K)+(r\pm\sigma^{2}/2)T}{\sigma\sqrt{T}} |  | (3) |

and d−=d+−σ​Td\_{-}=d\_{+}-\sigma\sqrt{T}.
S0S\_{0} is the current price of stock or asset and their corresponding delivery (strike) price KK if the option is exercised. rr is the risk-free rate and σ\sigma is the volatility of asset. TT is the time to maturity of the option.
N​(d±)N(d\_{\pm}) is the cumulative distribution function, which is expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | N​(d±)=12​π​∫−∞d±e−x22​𝑑xN(d\_{\pm})=\frac{1}{\sqrt{2\pi}}\int\_{-\infty}^{d\_{\pm}}e^{-\frac{x^{2}}{2}}dx |  | (4) |

where N​(d−)N(d\_{-}) is the probability for the call option exercised in a risk-free world.
The expression S0​N​(d+)​e−r​TS\_{0}N(d\_{+})e^{-rT} is the expected stock price at
time TT in a risk-free world when stock prices less than the strike price are counted as
zero.

It can be seen that the cumulative distribution function plays a role of
probability in the risk-free market. When we consider a finance market driven by
some market force, shorting or buying, the Guassian probability distribution
of N​(d±)N(d\_{\pm}) can be generalized to non-Guassian probability
distribution. We look for some hints from quantum mechanics how option pricing
work in a non-Guassian dynamics.

### 2.2 Analog between finance market and quantum harmonic oscillator

In general, the evolution of finance market is a stochastic dynamical process.
The Black-Scholes theory provides an option pricing scheme in a risk-free world,
which implies that the dynamical process of finance market is a Guassian process.
In quantum world the quantum state emerges also by a stochastic dynamics, in which
the probability density is expressed in terms of the norm of wave function.
The wave function evolution is driven by the Schrödinger equation. Therefore,
we can find an analog between the finance market and quantum mechanics.

(1) The finance market corresponds to the quantum bound systems.

(2) The stochastic dynamics of finance market corresponds to the dynamics of the quantum bound systems.

(3) The hidden shorting or buying in finance market corresponds to the intrinsic force or potential in quantum bound systems.

(4) The integrand function 12​π​e−x2/2≡PB​S​(x)\frac{1}{\sqrt{2\pi}}e^{-x^{2}/2}\equiv P\_{BS}(x) of N​(d±)N(d\_{\pm}) corresponds to the probability density P​(x)=|ψ​(x)|2P(x)=|\psi(x)|^{2} of the quantum bound systems. Further, the Black-Scholes model corresponds to the ground state of quantum harmonic oscillator, namely, PB​S​(x)=Pg,H​O​(x)P\_{BS}(x)=P\_{g,HO}(x). (See the following demonstration)

(5) The cumulative distribution function of the Black-Scholes model can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | N​(d±)=∫−∞d±PB​S​(x)​𝑑x=∫−∞d±Pg,H​O​(x)​𝑑xN(d\_{\pm})=\int\_{-\infty}^{d\_{\pm}}P\_{BS}(x)dx=\int\_{-\infty}^{d\_{\pm}}P\_{g,HO}(x)dx |  | (5) |

This analog between finance market and quantum mechanics provides a
way to modify the integrand function PB​S​(x)P\_{BS}(x) of the Black-Scholes model
and give some new schemes of option pricing. Notice that this integrand function has the same form of the ground state wave function of quantum harmonic oscillator,
we start from the one-dimensional quantum harmonic oscillator.
The potential of the harmonic oscillator is

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(x)=12​m​ω2​x2V(x)=\frac{1}{2}m\omega^{2}x^{2} |  | (6) |

and the stationary Schrödinger equation is written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℏ22​m​d2​ψd​x2+(E−m​ω22​x2)​ψ=0\frac{\hbar^{2}}{2m}\frac{d^{2}\psi}{dx^{2}}+\left(E-\frac{m\omega^{2}}{2}x^{2}\right)\psi=0 |  | (7) |

The wave function in the ground state can be solved

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψg​(x)=(απ)1/2​e−α2​x2/2\psi\_{g}(x)=\left(\frac{\alpha}{\sqrt{\pi}}\right)^{1/2}e^{-\alpha^{2}x^{2}/2} |  | (8) |

where α=m​ωℏ\alpha=\sqrt{\frac{m\omega}{\hbar}}.
For convenience we set α=12\alpha=\frac{1}{\sqrt{2}} such that the probability density in the ground state

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pg,H​O​(x)=12​π​e−x2/2=PB​S​(x)P\_{g,HO}(x)=\frac{1}{\sqrt{2\pi}}e^{-x^{2}/2}=P\_{BS}(x) |  | (9) |

Therefore, the ground state of quantum harmonic oscillator corresponds to Black-Schole model.
This correspondence between finance market and quantum harmonic oscillator provides a way
to generalize the Black-Scholes model based on quantum mechanics approach.
When we add some forces to generalize the quantum harmonic oscillator,
the ground state of wave function and its corresponding probability density deviates the Guassian form. This infers that some market forces emergence makes the finance market deviate the Guassian process and modify the Black-Scholes option pricing.

The finance market force is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | F=−d​V​(x)d​xF=-\frac{dV(x)}{dx} |  | (10) |

where V​(x)V(x) is the potential of the bound systems. General speaking,
force describes any local or individual behavior making finance market
deviate the equilibrium state, while potential describes the global effect
induced from these local or individual behaviors.
Thus, the finance market force describe the behaviors of shorting or buying the underlying asset or any economic news and psychological behaviors in finance market. F=−d​V​(x)d​x>0F=-\frac{dV(x)}{dx}>0 means any market force pushing the asset or stock price high. F=−d​V​(x)d​x<0F=-\frac{dV(x)}{dx}<0 means any market resistance bringing down the asset or stock price.

It should be pointed out that the finance market forces we introduce from quantum mechanics
will modify the option pricing from two ways. One is to modify Pg,H​OP\_{g,HO}, which means
to modify PB​SP\_{BS} and the cumulative distribution function, the other is to modify
the volatility σ\sigma because the force drives the probability distribution deviating
from the Guassian distribution. The effective volatility can be obtained by

|  |  |  |  |
| --- | --- | --- | --- |
|  | σeff=σ​σQ​M\sigma\_{\textrm{eff}}=\sigma\sigma\_{QM} |  | (11) |

where σQ​M=⟨x2⟩Q​M−⟨x⟩Q​M2\sigma\_{QM}=\sqrt{\left\langle x^{2}\right\rangle\_{QM}-\langle x\rangle\_{QM}^{2}} and ⟨f​(x)⟩Q​M=∫f​(x)​PQ​M​𝑑x\left\langle f(x)\right\rangle\_{QM}=\int f(x)P\_{QM}dx, where PQ​MP\_{QM} is the probability density from quantum mechanics. The volatility σQ​M\sigma\_{QM} in the Black-Scholes formula ([1](https://arxiv.org/html/2601.00293v1#S2.E1 "In 2.1 Black-Scholes model ‣ 2 Market force Model of Stochastic dynamics ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach"))(\ref{BSf1}) is 11 for the standard Guassian distribution.

In principle, we can design different forces to study or describe different market behaviors and modify the option pricing.
When the force vanishes F=0F=0, the quantum system reduces to the harmonic oscillator and our
model reduces to the Black-Scholes Model.
Thus, the standard harmonic oscillator potential 12​m​ω2​x2\frac{1}{2}m\omega^{2}x^{2} can be regarded as the natural boundary condition of finance market.

Based on this analog between the finance market and quantum harmonic oscillator, we can
take different forces into account for the harmonic oscillator to generalize
the Black-Scholes option pricing for understanding their financial meaning.

## 3 Market forces and option pricing

### 3.1 Constant forces

Let us consider the market force be a constant F=−kF=-k. It corresponds to the potential

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vk​(x)=k​xV\_{k}(x)=kx |  | (12) |

where kk is a small parameter describing the strength of the potential. Thus, the
Schrödinger equation of system can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℏ22​m​d2​ψd​x2+(E−m​ω22​x2+k​x)​ψ=0\frac{\hbar^{2}}{2m}\frac{d^{2}\psi}{dx^{2}}+\left(E-\frac{m\omega^{2}}{2}x^{2}+kx\right)\psi=0 |  | (13) |

By solving the Schrödinger equation, we obtain the solution of the wave function
in the ground state

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψg​(x)=(12​π)1/2​e−(x−xk)2/4\psi\_{g}(x)=\left(\frac{1}{\sqrt{2\pi}}\right)^{1/2}e^{-(x-x\_{k})^{2}/4} |  | (14) |

where xk=2​kℏ​ωx\_{k}=\frac{2k}{\hbar\omega}.
The peak of the probability density is shifted to xkx\_{k} shown in Fig.[1](https://arxiv.org/html/2601.00293v1#S3.F1 "Figure 1 ‣ 3.1 Constant forces ‣ 3 Market forces and option pricing ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")​(a)\ref{fig1}(a). Namely

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pk​(x)=12​π​e−(x+xk)2/2P\_{k}(x)=\frac{1}{2\pi}e^{-(x+x\_{k})^{2}/2} |  | (15) |

Using the corresponding relation in
Eq. ([5](https://arxiv.org/html/2601.00293v1#S2.E5 "In 2.2 Analog between finance market and quantum harmonic oscillator ‣ 2 Market force Model of Stochastic dynamics ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")) we plot numerically the call option price versus the shift xkx\_{k} in Fig. [1](https://arxiv.org/html/2601.00293v1#S3.F1 "Figure 1 ‣ 3.1 Constant forces ‣ 3 Market forces and option pricing ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")​(b)\ref{fig1}(b).

![Refer to caption](x1.png)


Figure 1: (Color online)(a) Comparison of the probability densities P​(x)P(x) between the normal and the force-driven probability densities. The solid line
of the probability density driven by a constant force and its shift depends on the
strength of force kk.
(b) The dashed line is the option price for F=0F=0 (Black-Scholes model)
The solid line is the option price modified by a constant force case F<0F<0.
The variance of call option price along with xkx\_{k}.
The parameters we use are r=10%r=10\%, S0=20S\_{0}=20, K=20K=20, T=1T=1year and σ=25%\sigma=25\%.

It can be seen from Fig. [1](https://arxiv.org/html/2601.00293v1#S3.F1 "Figure 1 ‣ 3.1 Constant forces ‣ 3 Market forces and option pricing ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")(a) that the shape of the probability density does not change and it moves to the left for the constant market force F<0F<0. Similarly, it will move to the right for F>0F>0. From the financial point of views, F<0F<0
means that there exists shorting the asset in finance market and F>0F>0 means buying behaviors in finance market. The option prices are shown in Fig. [1](https://arxiv.org/html/2601.00293v1#S3.F1 "Figure 1 ‣ 3.1 Constant forces ‣ 3 Market forces and option pricing ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")(b), in which the
the dashed line is the option price for F=0F=0 (Black-Scholes model) and
the solid line for the constant force case F<0F<0. When the force increases with kk
the call option price should decrease monotonically with kk for F<0F<0.
It matches the market behavior that sorting the underlying asset will reduce its call option price. Similarly it should increase with kk for F>0F>0.

### 3.2 Linear forces

When we consider the market force being proportional to xx, F=−2​λ​xF=-2\lambda x, which induces the potential in finance market

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vλ​(x)=λ​x2V\_{\lambda}(x)=\lambda x^{2} |  | (16) |

where λ>0\lambda>0. The Schrödinger equation of system can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℏ22​m​d2​ψd​x2+[E−(m​ω22+λ)​x2]​ψ=0\frac{\hbar^{2}}{2m}\frac{d^{2}\psi}{dx^{2}}+\left[E-\left(\frac{m\omega^{2}}{2}+\lambda\right)x^{2}\right]\psi=0 |  | (17) |

The wave function in the ground state can be solved by
ψg​(x)=(λω2​π)1/2​e−λω​x2/4\psi\_{g}(x)=\left(\frac{\lambda\_{\omega}}{\sqrt{2\pi}}\right)^{1/2}e^{-\lambda\_{\omega}x^{2}/4}
and the probability density is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pλ​(x)=λω2​π​e−λω​x2/2P\_{\lambda}(x)=\frac{\lambda\_{\omega}}{\sqrt{2\pi}}e^{-\lambda\_{\omega}x^{2}/2} |  | (18) |

where λω=1+λω\lambda\_{\omega}=\sqrt{1+\frac{\lambda}{\omega}}.

![Refer to caption](x2.png)


Figure 2: (Color online)(a)
Comparison of the probability densities P​(x)P(x) between the normal and the force-driven probability densities. The solid line of the probability density driven by a −2​λ​x-2\lambda x
force. The volatility vary with the strength of force λ\lambda.
(b) The dashed line is the option price for F=0F=0 (Black-Scholes model)
The solid line is the option price modified by the force.
The parameters we use are r=10%r=10\%, S0=20S\_{0}=20, K=20K=20, T=1​y​e​a​rT=1year and σ=25%\sigma=25\%.

Figure [2](https://arxiv.org/html/2601.00293v1#S3.F2 "Figure 2 ‣ 3.2 Linear forces ‣ 3 Market forces and option pricing ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")(a) shows the probability densities of the Black-Scholes model
and the generalized harmonic oscillator with the linear force.
It can be seen that the force modifies the peak height and the volatility of the probability density such that the option prices vary with the force strength seen in Fig. [2](https://arxiv.org/html/2601.00293v1#S3.F2 "Figure 2 ‣ 3.2 Linear forces ‣ 3 Market forces and option pricing ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")(b).

### 3.3 x2x^{2} forces

For the market force F=−3​β​x2F=-3\beta x^{2}, which induces the
potential in finance market

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vβ​(x)=β​x3V\_{\beta}(x)=\beta x^{3} |  | (19) |

The Hamiltonian for this case can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | H^=H^0+Vβ​(x)\widehat{H}=\widehat{H}\_{0}+V\_{\beta}(x) |  | (20) |

For small β\beta, we can use the perturbation method to turn out the approximate
solution of wave function in the ground state. The first-order approximation solution is zero. The second-order approximation solution of wave function
can be obtained by (see Appendix)

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψg​(x)=C(2​π)1/4​e−x2/4​[1−βℏ​ω​(13​x3+x2)]\psi\_{g}(x)=\frac{C}{(2\pi)^{1/4}}e^{-x^{2}/4}\left[1-\frac{\beta}{\hbar\omega}\left(\frac{1}{3}x^{3}+\frac{x}{2}\right)\right] |  | (21) |

The probability density is obtained

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pβ​(x)=C2​e−x2/22​π​[1−βℏ​ω​(13​x3+x2)]2P\_{\beta}(x)=C^{2}\frac{e^{-x^{2}/2}}{\sqrt{2\pi}}\left[1-\frac{\beta}{\hbar\omega}\left(\frac{1}{3}x^{3}+\frac{x}{2}\right)\right]^{2} |  | (22) |

where CC is the normalization constant.

We plot the probability density versus β\beta in Fig. [3](https://arxiv.org/html/2601.00293v1#S3.F3 "Figure 3 ‣ 3.3 𝑥² forces ‣ 3 Market forces and option pricing ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")(a) and the option price in Fig. [3](https://arxiv.org/html/2601.00293v1#S3.F3 "Figure 3 ‣ 3.3 𝑥² forces ‣ 3 Market forces and option pricing ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")(b).

![Refer to caption](x3.png)


Figure 3: (Color online)(a) The probability density versus β\beta
When β=0\beta=0 it reduces the normal distribution assumed in Black-Scholes Model.
(b) The call option price versus β\beta.
The parameters we use are r=10%r=10\%, S0=20S\_{0}=20, K=20K=20, T=1​y​e​a​rT=1year and σ=25%\sigma=25\%.

We can see from Fig. [3](https://arxiv.org/html/2601.00293v1#S3.F3 "Figure 3 ‣ 3.3 𝑥² forces ‣ 3 Market forces and option pricing ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")(a) that the main peak moves to right. As β\beta increase a sub-peak appears. This phenomena can be interpreted by the collective effect in finance market in the natural boundary condition.
Fig. [3](https://arxiv.org/html/2601.00293v1#S3.F3 "Figure 3 ‣ 3.3 𝑥² forces ‣ 3 Market forces and option pricing ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")(b) shows the option price with β\beta. As β\beta increases the option price goes down with shorting force, which matches our expectation.

### 3.4 x3x^{3} forces

Further we can consider the market force F=−4​γ​x3F=-4\gamma x^{3}, which induces the
potential in finance market

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vγ​(x)=γ​x4V\_{\gamma}(x)=\gamma x^{4} |  | (23) |

The Hamiltonian for this case can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | H^=H^0+Vγ​(x)\widehat{H}=\widehat{H}\_{0}+V\_{\gamma}(x) |  | (24) |

Similarly for small γ\gamma, by the perturbation method we can obtain the approximate
solution of wave function in the ground state. The solution of wave function in the first-order approximation can be given by (see Appendix)

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψg​(x)=C(2​π)1/4​e−x2/4​[1−γ4​2​ℏ​ω​(x4−9)]\psi\_{g}(x)=\frac{C}{(2\pi)^{1/4}}e^{-x^{2}/4}\left[1-\frac{\gamma}{4\sqrt{2}\hbar\omega}(x^{4}-9)\right] |  | (25) |

The probability density is obtained

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pβ​(x)=C2​e−x2/22​π​[1−γ4​2​ℏ​ω​(x4−9)]2P\_{\beta}(x)=C^{2}\frac{e^{-x^{2}/2}}{\sqrt{2\pi}}\left[1-\frac{\gamma}{4\sqrt{2}\hbar\omega}(x^{4}-9)\right]^{2} |  | (26) |

where CC is the normalization constant.
We plot the probability density versus γ\gamma in Fig. [4](https://arxiv.org/html/2601.00293v1#S3.F4 "Figure 4 ‣ 3.4 𝑥³ forces ‣ 3 Market forces and option pricing ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")(a) and the option price in Fig. [4](https://arxiv.org/html/2601.00293v1#S3.F4 "Figure 4 ‣ 3.4 𝑥³ forces ‣ 3 Market forces and option pricing ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")(b).

![Refer to caption](x4.png)


Figure 4: (Color online)(a)
The probability density versus γ\gamma
When γ=0\gamma=0 it reduces the normal distribution assumed in Black-Scholes Model.
(b) The call option price versus γ\gamma.
The plot we use r=10%r=10\%, S0=20S\_{0}=20, K=20K=20, T=1​y​e​a​rT=1year and σ=25%\sigma=25\%.

It should be noticed that the finance market depends on both γ\gamma and xx shown in Fig.[4](https://arxiv.org/html/2601.00293v1#S3.F4 "Figure 4 ‣ 3.4 𝑥³ forces ‣ 3 Market forces and option pricing ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")(a) .
For γ>0\gamma>0, F<0F<0 means that the force is resistant for x>0x>0 and the force is active for x<0x<0. For γ<0\gamma<0, F>0F>0 means that the force is active for x<0x<0 and the force is resistent for x>0x>0. As |λ||\lambda| increases, the original price could be unstable and there exist two symmetric attractors, which push the price either up or down.
Fig. [4](https://arxiv.org/html/2601.00293v1#S3.F4 "Figure 4 ‣ 3.4 𝑥³ forces ‣ 3 Market forces and option pricing ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")(b) shows the call option price versus γ\gamma. The call option price shows a minimum at γ≈0.063\gamma\approx 0.063 and a maximum at γ≈−0.14\gamma\approx-0.14.
When the price distribution becomes less homogeneous, the call option price will be lower. This perfectly matches the realistic situation that the less fluctuate price of underlying assets leads to a lower call option price.

Furthermore, we can also apply this method to solve any other polynomial boundary conditions. For an arbitrary condition, we can expand the function with Taylor series and we can analyze the change of the call option price to an arbitrary hidden market forces.

### 3.5 Quantum well

In finance market, if a company does not want its Underlying Asset price lower than SnS\_{n}, it is equivalent to exist a boundary condition that makes the dealing of its asset stop.
From quantum mechanics point of views we may set up a quantum well model
to simulate this behavior.
The potential of quantum well is

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(x)={0f​o​r|x|<a∞f​o​r|x|≥aV(x)=\left\{\begin{array}[]{c}0\quad for\quad|x|<a\\ \infty\quad for\quad|x|\geq a\end{array}\right. |  | (27) |

where a∝Δ​Sa\propto\Delta S. It implies when x≤Xnx\leq X\_{n} (Xn∝Sn−S0X\_{n}\propto S\_{n}-S\_{0})
the finance market is in the normal state and the market will stop if some unexpected forces make the Underlying Asset price going beyond the lower or upper bound, namely lower than S0−Δ​SS\_{0}-\Delta S or higher than S0+Δ​SS\_{0}+\Delta S. |a||a| can be regarded as a boundary of finance market.

The solution of wave function in ground state is obtained

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψg​(x)=1a​sin⁡[π2​a​(x+a)],x∈[−a,+a]\psi\_{g}(x)=\frac{1}{\sqrt{a}}\sin\left[{\frac{\pi}{2a}}(x+a)\right],\quad x\in[-a,+a] |  | (28) |

and the probability density is expressed as

|  |  |  |
| --- | --- | --- |
|  | PQ​W​(x)={1a​sin2⁡[π2​a​(x+a)],x∈[−a,+a]0,x∈(−∞,−a)​⋃(a,+∞)P\_{QW}(x)=\left\{\begin{array}[]{l}\frac{1}{a}\sin^{2}\left[{\frac{\pi}{2a}}(x+a)\right],\quad x\in[-a,+a]\\ 0,\qquad\qquad\qquad\qquad x\in(-\infty,-a)\bigcup(a,+\infty)\end{array}\right. |  |

![Refer to caption](x5.png)


Figure 5: (Color online)(a) Comparison of Probability Densities between the normal distribution and distribution in quantum well. 𝑷​(𝒙)\bm{P(x)}:
The half width of modified distribution is the half width between two barriers (infinity wells). Practical meaning of a is the width of price range for the underlying asset.
(b) The call option price change along with aa.
We use r=10%r=10\%, S0=20S\_{0}=20, K=20K=20, T=1​y​e​a​rT=1year and σ=25%\sigma=25\%.
If there is no arbitrary chance, call option price should be no less than S0−K​e−r​TS\_{0}-Ke^{-rT} which is regarded as the minimum price for call options.

Since the boundary of the well prevents neither the underlying price increasing too very high nor decreasing too very low, the whole distribution will be squeezed within −a<x<a-a<x<a. The probability of the future underlying price still near current price significantly increases, but when x→±ax\rightarrow\pm a, the probability decreased below the normal distribution seen in Fig. [5](https://arxiv.org/html/2601.00293v1#S3.F5 "Figure 5 ‣ 3.5 Quantum well ‣ 3 Market forces and option pricing ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")(a).
By plugging the distribution function in Eq. ([3.5](https://arxiv.org/html/2601.00293v1#S3.Ex1 "3.5 Quantum well ‣ 3 Market forces and option pricing ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")), we can plot the cc versus λ\lambda curve for the call option price with aa. The figure [5](https://arxiv.org/html/2601.00293v1#S3.F5 "Figure 5 ‣ 3.5 Quantum well ‣ 3 Market forces and option pricing ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")(b) shows that when a<0.3a<0.3, the original price does not change. The call option price is equal to S0−K​e−e​TS\_{0}-Ke^{-eT}. As aa increases the call option price will also increase. This result shows that as the price distribution becomes more homogeneous, the call option will be more expensive, which matches the realistic situation.

As illustrative examples here we present the call option pricing based on this framework. Similarly we can also give the modification of the put option pricing in the practical application.

## 4 Conclusion

The Black-Scholes model gives a scheme of option pricing based on the risk-free,
efficient market hypothesis and the standard Guassian stochastic dynamics of finance market.
In the realistic finance market there exist various unpredictable factors, such
as abnormal shorting or buying some assets, some rules or policy changes, some
unexpected news and some psychological features of investors, which could break
the efficient market hypothesis making the stochastic dynamics deviate
from the standard Guassian stochastic dynamics of finance market. How do we
take these factors into account to generalize the Black-Scholes model for the option pricing becomes a practical problem. We discover the analog between the Guassian stochastic dynamics
and the probability density of the ground state of quantum harmonic oscillator. We propose a market force model to simulate various unpredictable market behaviors to modifying
the Guassian dynamics based on quantum mechanics approach. Based on this model
we give a new scheme of option pricing for various unpredictable market behaviors.
The option pricing based on quantum mechanics provides a more systematic and explicit
way to generalize the Guassian probability distribution for the Black-Scholes model
than other approaches.[[9](https://arxiv.org/html/2601.00293v1#bib.bib9)]

As examples, we present several market forces to generalize the Black-Schole model
and turn out their corresponding option pricing. In principle, we can generalize further this method to more complicated forces driving the finance market because any form of forces
or potentials as a function of xx can be expanded by Taylor series. By the perturbation method we can calculate arbitrary-order approximation of wave function based on the quantum mechanics approach. On the other hand, we can also generalize the one-dimensional oscillator to the multi-dimensional oscillators, which covers various market forces
and their interactions which could modify the option pricing.

This study on the option pricing provides two practical hints. One is that as a new scheme
of option pricing we can modify the pure Black-Scholes model-based option pricing when we can predict some unexpected force emergence. The other is that when
one cannot predict these unexpected forces appearing. The prediction of the option pricing
based on this scheme provides some risk premium.

## 5 Appendices

### 5.1 The quantum harmonic oscillator

The Hamiltonian of 1D harmonic oscillator is written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | H=−ℏ22​m​d2d​x2+12​m​ω2​x2H=-\frac{\hbar^{2}}{2m}\frac{d^{2}}{dx^{2}}+\frac{1}{2}m\omega^{2}x^{2} |  | (29) |

The wave function can be obtained

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψn​(x)=(απ​2n​n!)1/2​e−α2​x2/2​Hn​(x)\psi\_{n}(x)=\left(\frac{\alpha}{\sqrt{\pi}2^{n}n!}\right)^{1/2}e^{-\alpha^{2}x^{2}/2}H\_{n}(x) |  | (30) |

where α=m​ωℏ≡12\alpha=\sqrt{\frac{m\omega}{\hbar}}\equiv\frac{1}{\sqrt{2}} for convenience.
The eigen energy is

|  |  |  |  |
| --- | --- | --- | --- |
|  | En=ℏ​ω​(n+12)E\_{n}=\hbar\omega\left(n+\frac{1}{2}\right) |  | (31) |

where n=0,1,2,⋯n=0,1,2,\cdots.

### 5.2 The perturbation method

The energy and wave function by the non-degenerate perturbation are

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | En\displaystyle E\_{n} | =\displaystyle= | En(0)+Hn​n′+∑m′|Hn​m′|2En(0)−Em(0)+…\displaystyle E\_{n}^{(0)}+H\_{nn}^{\prime}+\sum^{\prime}\_{m}\frac{|H\_{nm}^{\prime}|^{2}}{E\_{n}^{(0)}-E\_{m}^{(0)}}+... |  | (32) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ψn\displaystyle\psi\_{n} | =\displaystyle= | ψn(0)+∑m′Hn​m′En(0)−Em(0)​ψm(0)⁣′+…\displaystyle\psi\_{n}^{(0)}+\sum^{\prime}\_{m}\frac{H\_{nm}^{\prime}}{E\_{n}^{(0)}-E\_{m}^{(0)}}\psi\_{m}^{(0)\prime}+... |  | (33) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hn​m′=⟨ψn|H′|ψm⟩H\_{nm}^{\prime}=\langle\psi\_{n}|H^{\prime}|\psi\_{m}\rangle |  | (34) |

is the matrix element of the perturbation Hamiltonian.

### 5.3 The perturbation wave function in the ground state of harmonic oscillator

The ground state wave function of harmonic oscillator is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ0​(x)=(απ)1/2​e−α2​x2/2\psi\_{0}(x)=\left(\frac{\alpha}{\sqrt{\pi}}\right)^{1/2}e^{-\alpha^{2}x^{2}/2} |  | (35) |

For convenience, we introduce the occupation number representation

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | a^\displaystyle\widehat{a} | =\displaystyle= | α2​(x+iα2​p^x)\displaystyle\frac{\alpha}{\sqrt{2}}\left(x+\frac{i}{\alpha^{2}}\widehat{p}\_{x}\right) |  | (36) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | a^†\displaystyle\widehat{a}^{\dagger} | =\displaystyle= | α2​(x−iα2​p^x)\displaystyle\frac{\alpha}{\sqrt{2}}\left(x-\frac{i}{\alpha^{2}}\widehat{p}\_{x}\right) |  | (37) |

with

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | x\displaystyle x | =\displaystyle= | 12​α​(a^+a^†)\displaystyle\frac{1}{\sqrt{2}\alpha}\left(\widehat{a}+\widehat{a}^{\dagger}\right) |  | (38) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | p^x\displaystyle\widehat{p}\_{x} | =\displaystyle= | αi​2​(a^−a^†)\displaystyle\frac{\alpha}{i\sqrt{2}}\left(\widehat{a}-\widehat{a}^{\dagger}\right) |  | (39) |

The commutative relation is [a^,a^†]=1\left[\widehat{a},\widehat{a}^{\dagger}\right]=1 and

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | a^​|n⟩\displaystyle\widehat{a}|n\rangle | =\displaystyle= | n​|n−1⟩\displaystyle\sqrt{n}|n-1\rangle |  | (40) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | a^†​|n⟩\displaystyle\widehat{a}^{\dagger}|n\rangle | =\displaystyle= | n+1​|n+1⟩\displaystyle\sqrt{n+1}|n+1\rangle |  | (41) |

Case I: x2x^{2} forces

The perturbation Hamiltonian is

|  |  |  |  |
| --- | --- | --- | --- |
|  | H′=β​x3=β2​2​α3​(a^+a^†)3H^{\prime}=\beta x^{3}=\frac{\beta}{2\sqrt{2}\alpha^{3}}\left(\widehat{a}+\widehat{a}^{\dagger}\right)^{3} |  | (42) |

and the perturbation matrix element in the ground state is expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | H0​m′=⟨0|H′|m⟩=β2​2​α3​⟨0|(a+a†)3|m⟩H\_{0m}^{\prime}=\langle 0|H^{\prime}|m\rangle=\frac{\beta}{2\sqrt{2}\alpha^{3}}\langle 0|\left(a+a^{\dagger}\right)^{3}|m\rangle |  | (43) |

By using formula in Eq. ([33](https://arxiv.org/html/2601.00293v1#S5.E33 "In 5.2 The perturbation method ‣ 5 Appendices ‣ Option Pricing beyond Black-Scholes Model: Quantum Mechanics Approach")), we can obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ0=C​(12​π)1/2​e−x2/4​[1−βℏ​ω​(13​x3+x2)]\psi\_{0}=C\left(\frac{1}{\sqrt{2\pi}}\right)^{1/2}e^{-x^{2}/4}\left[1-\frac{\beta}{\hbar\omega}\left(\frac{1}{3}x^{3}+\frac{x}{2}\right)\right] |  | (44) |

The probability density can be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pβ​(x)=C2​e−x2/22​π​[1−βℏ​ω​(13​x3+x2)]2P\_{\beta}(x)=\frac{C^{2}e^{-x^{2}/2}}{\sqrt{2\pi}}\left[1-\frac{\beta}{\hbar\omega}\left(\frac{1}{3}x^{3}+\frac{x}{2}\right)\right]^{2} |  | (45) |

Case II: x3x^{3} forces

The perturbation Hamiltonian is

|  |  |  |  |
| --- | --- | --- | --- |
|  | H′=γ​x4=γ4​α4​(a+a†)4H^{\prime}=\gamma x^{4}=\frac{\gamma}{4\alpha^{4}}\left(a+a^{\dagger}\right)^{4} |  | (46) |

and the perturbation matrix element in the ground state is expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | H0​m′=⟨0|H′|m⟩=γ4​α4​⟨0|(a+a†)4|m⟩H\_{0m}^{\prime}=\langle 0|H^{\prime}|m\rangle=\frac{\gamma}{4\alpha^{4}}\langle 0|\left(a+a^{\dagger}\right)^{4}|m\rangle |  | (47) |

Similarly, we can obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ0=C​(12​π)1/2​e−x2/4​[1−γ4​2​ℏ​ω​(x4−9)]\psi\_{0}=C\left(\frac{1}{\sqrt{2\pi}}\right)^{1/2}e^{-x^{2}/4}\left[1-\frac{\gamma}{4\sqrt{2}\hbar\omega}\left(x^{4}-9\right)\right] |  | (48) |

The probability density is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pγ​(x)=C2​e−x2/22​π​[1−γ4​2​ℏ​ω​(x4−9)]2P\_{\gamma}(x)=\frac{C^{2}e^{-x^{2}/2}}{\sqrt{2\pi}}\left[1-\frac{\gamma}{4\sqrt{2}\hbar\omega}\left(x^{4}-9\right)\right]^{2} |  | (49) |

## References

* [1]
   F.Black and M.Scholes,The Pricing of Options and Corporate Liabilities,Journal of Political Economy,637-59,(May/June, 1973).
* [2]
   J. C.Hull,Options,futures, and other Derivatives the 10th Edition,
  320-323, Pearson, (2011).
* [3]
   B. E. Baaquie,Quantum Finance, 316, 78-115 (2004)
* [4]
   Lauterbach, Beni and Schultz, Paul, Journal of Finance,45, 1181-1209 (1990).
* [5]
   Scott, Louis O., Option Pricing when the Variance Changes Randomly: Theory, Estimation, and an Application, 22, 419-438 (1987).
* [6]
   Kleinert, H. and Korbel, J., Physica A Statistical Mechanics & Its Applications, 449, 200-214 (2016).
* [7]
   Song, Lina and Wang, Weiguo, Abstract & Applied Analysis, 2013, 1-16(2013).
* [8]
   Merton, Robert C.,J Financial Economics, 3, 125-144 (1976).
* [9]
   Mantegna, Rosario Nunzio,Physica A Statistical Mechanics & Its Applications ,179, 232 (1991).
* [10]
   B. E. Baaquie,Quantum Finance,316, 76-77 (2004).
* [11]
   B. E. Baaquie,Quantum Finance, 316, 73-76 (2004).