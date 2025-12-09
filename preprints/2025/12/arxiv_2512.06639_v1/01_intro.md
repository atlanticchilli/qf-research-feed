---
authors:
- Zaniar Ahmadi
- Frédéric Godin
doc_id: arxiv:2512.06639v1
family_id: arxiv:2512.06639
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The
  authors report there are no competing interests to declare.
url_abs: http://arxiv.org/abs/2512.06639v1
url_html: https://arxiv.org/html/2512.06639v1
venue: arXiv q-fin
version: 1
year: 2025
---


Zaniar Ahmadi
Concordia University, Department of Mathematics and Statistics, Montréal, Canada

Frédéric Godin
Corresponding author.
  
  Email addresses:[zaniar.ahmadi@concordia.ca](mailto:zaniar.ahmadi@concordia.ca) (Zaniar Ahmadi), [frederic.godin@concordia.ca](mailto:frederic.godin@concordia.ca) (Frédéric Godin)
Concordia University, Department of Mathematics and Statistics, Montréal, Canada
Quantact Laboratory, Centre de Recherches Mathématiques, Montréal, Canada

(December 7, 2025)

###### Abstract

This paper investigates the deep hedging framework, based on reinforcement learning (RL), for the dynamic hedging of swaptions, contrasting its performance with traditional sensitivity-based rho-hedging. We design agents under three distinct objective functions—mean squared error, downside risk, and Conditional Value-at-Risk—to capture alternative risk preferences and evaluate how these objectives shape hedging styles.
Relying on a three-factor arbitrage-free dynamic Nelson-Siegel model for our simulation experiments,
our findings show that near-optimal hedging effectiveness is achieved when using two swaps as hedging instruments. Deep hedging strategies dynamically adapt the hedging portfolio’s exposure to risk factors across states of the market. In our experiments, their out-performance over rho-hedging strategies persists even in the presence some of model misspecification. These results highlight RL’s potential to deliver more efficient and resilient swaption hedging strategies.

JEL classification: E43, G12.

Keywords: Swaptions, Dynamic Hedging, Deep Reinforcement Learning, Term Structure Models, Risk Management.

## 1 Introduction

Interest rate derivatives play a central role in modern financial markets, with interest rate swaps and swaptions serving as foundational instruments for risk management and asset-liability transformation. Swaptions, which are options on interest rate swaps, are particularly vital for hedging interest rate volatility and convexity risk, offering flexibility in managing contingent liabilities and exposures. They are widely used by institutions such as insurance companies, pension funds and structured product issuers, and are integral to the pricing and risk management of callable bonds, mortgage-backed securities and other complex instruments. According to the Bank for International Settlements  (bis2024otc), the global notional value of outstanding interest rate derivatives exceeds $540 trillion, with swaptions comprising over $46 trillion of this total, reflecting their deep integration into the financial ecosystem.

Research on the hedging of swaptions has been ongoing for years. jamshidian1997libor demonstrates that a swaption can be replicated using a finite number of zero-coupon bonds, establishing a direct connection between swaptions and fundamental fixed-income contracts.
brace2001towards compute the Greeks of swaptions under the LIBOR market model (LMM) and show that the resulting hedging strategy aligns closely with that obtained with the Black swaption pricing formula.
The effectiveness of delta hedging strategies within LMM is extensively explored by tim\_dun\_simulated\_2001. They employ Monte Carlo simulations to show that while at-the-money swaptions can be hedged effectively, significant errors persist for in- and out-of-the-money contracts due to model limitations and sensitivity to volatility and payoff asymmetry. Research highlights the advantages of multi-factor frameworks for the representation of the term structure, which allow interest rates associated with different maturities to move independently and thus to capture the complex shifts, twists, and curvature observed in real markets. driessen2003performance find that multi-factor term structure models outperform single-factor models for hedging interest rate derivatives such as caps and swaptions because they capture yield curve movements more accurately. fan2003hedging demonstrate that higher-order multifactor Heath-Jarrow-Morton models significantly reduce hedging errors in the swaption market, while fan2007pricing further show that at least two factors are required to robustly capture the yield curve dynamics, which is necessary for effective swaption hedging. an2008compatibility compare one-factor LIBOR and swap market models, concluding that although they yield comparable results, significant biases and limitations underscore the need for more sophisticated or multi-factor methods. In addition, cresnikanalysis evaluates the hedging performance of the black1976pricing, hull1990pricing, and SABR (hagan2002managing)
models using both historical and synthetically generated scenarios, finding that stochastic volatility and multifactor models such as SABR provide superior risk reduction versus simpler one-factor alternatives. On a discordant note, pietersz2010comparison state that hedging performance on swaptions with single-factor models can be satisfactory, with smile effects having more material impacts than rates correlations. Recent research applies machine learning to address the complexity and high dimensionality of swaption hedging. wang2018deep introduce a deep learning-based BSDE solver within the LMM framework, utilizing a dedicated neural network architecture that efficiently prices and hedges Bermudan swaptions, computes Greeks, and handles high-dimensional problems.

Conventional hedging strategies, whether based on static hedges or dynamically updated sensitivities, remain fundamentally local in nature.
They typically optimize hedging positions one period at a time, without accounting for compounding risk premia or interaction between hedging errors of the future time periods. Deep reinforcement learning (DRL), as in  buehler2019deep, offers an alternative to conventional schemes and allow optimizing policies jointly over multiple periods. The use of DRL approaches for hedging optimization is referred to as deep hedging. The advantages of deep hedging lie in enabling multi-stage optimality, offering flexibility in targeting different objective functions, and providing the ability to account for physical distribution features such as risk premia. Such an approach can handle high-dimensional environments including multiple realistic characteristics such as transaction costs and market frictions, stochastic volatility (cao2021deep), and dynamic implied volaility surfaces (franccois2024enhancing; franccois2025deep). The deep hedging agent learns flexible, state-dependent hedging policies through interaction with simulated or historical market environments. For an overview of methodologies and trends in deep hedging, see the survey by pickard2023deep.

To the best of our knowledge, with the exception of oya2024deep, there are currently no other published works that employ deep hedging for swaptions.
This study aims to fill this gap by developing a deep hedging framework for hedging European swaptions when the spot rate dynamics follows a multi-factor short rate process. More specifically, we rely on the discrete-time arbitrage-free Nelson–Siegel model (DTAFNS) of eghbalzadeh2024discrete, which is a discrete-time version of the arbitrage-free Nelson–Siegel model of christensen2011affine.
This represents an important advancement in tackling the unique challenges posed by interest rate derivatives hedging and in broadening the scope of neural-network-based hedging strategies. A key difference between this paper and that of oya2024deep is that they rely on the Swap market Bergomi model, whereas we rely on a parsimonous three-factor model for dynamics of the term structure. The latter choice leads to better interpretability of trading strategies and clearer insight into the source of out-performance of the deep hedging model over benchmarks.

This study highlights multiple advantages of using deep hedging policies for hedging interest rate derivatives. First, we observe general superior performance over rho-hedging, including under some model misspecification. To achieve multi-stage optimality, the deep hedging agent leverages parametric yield-curve dynamics to better manage exposure to risk factors and associated risk premia. Deep hedging effectively captures higher-order risk exposure and pathwise dynamics (e.g. reflecting previous hedging errors) that traditional approaches fail to address. Moreover, we demonstrate how various risk preferences can be encoded through different choices for the objective functions. In particular, we train agents under mean squared error, downside risk, and Conditional Value-at-Risk (CVaR) objectives, showing how each criterion induces a distinct hedging style. This comparative analysis provides new insights into the trade-offs between hedge effectiveness in regular scenarios, tail-risk protection, and premium harvesting. Additionally, we evaluate the marginal value added of the multiple hedging swaps we consider for inclusion in the hedging portfolio. Our results show that the use of two swaps is sufficient to achieve near-optimal hedging effectiveness. All these aforementioned findings underscore the potential of deep hedging as a robust and economically meaningful framework for interest rate derivatives risk management.

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2512.06639v1#S2 "2 Market Environment and Financial Instruments ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.") describes the market environment, the DTAFNS model, and the associated pricing of interest rate instruments such as swaps and swaptions. Section [3](https://arxiv.org/html/2512.06639v1#S3 "3 Hedging Framework and Replicating Portfolio Construction ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.") introduces the proposed hedging framework, including the construction of the hedging portfolio, the deep hedging approach, and benchmark strategies based on factor sensitivities. Section [4](https://arxiv.org/html/2512.06639v1#S4 "4 Market and Model Setup ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.") details the experimental design, and neural network architectures employed for both pricing and hedging tasks. Section [5](https://arxiv.org/html/2512.06639v1#S5 "5 Numerical Experiments ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.") presents the empirical results, comparing the performance of deep hedging strategies against traditional benchmarks. Section [6](https://arxiv.org/html/2512.06639v1#S6 "6 Conclusion ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.") concludes.
The code used to produce numerical results of this paper is available on Github.111See <https://github.com/zaniara3/swaption_deep_hedging> and <https://github.com/zaniara3/swaption_pricing_KAN>.

## 2 Market Environment and Financial Instruments

We assume that the short-rate dynamics follow the DTAFNS model proposed by eghbalzadeh2024discrete. The DTAFNS model offers a tractable, arbitrage-free framework for yield curve modeling in discrete time. Its closed-form solutions and compatibility with financial applications make it a valuable tool for pricing, risk management, and forecasting in stochastic interest rate environments.

The market operates in discrete time with time steps t=0,1,…,Tt=0,1,\ldots,T, each separated by a fixed time increment Δ\Delta (in years). The financial market is modeled on a filtered probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}), where ℙ\mathbb{P} denotes the real-world (physical) probability measure and ℱ:={ℱt}t=0T\mathcal{F}:=\{\mathcal{F}\_{t}\}\_{t=0}^{T} represents the natural filtration encoding the information flow in the market. The time-tt term structure is driven by three factors, Xt(1)X\_{t}^{(1)}, Xt(2)X\_{t}^{(2)} and Xt(3)X\_{t}^{(3)}, each of which is ℱt\mathcal{F}\_{t}-measurable.
The short rate rtr\_{t} prevailing over the interval [t,t+1)[t,t+1) is specified as

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=Xt(1)+Xt(2).r\_{t}=X\_{t}^{(1)}+X\_{t}^{(2)}. |  | (1) |

The factors vector Xt=[Xt(1),Xt(2),Xt(3)]⊤X\_{t}=[X\_{t}^{(1)},X\_{t}^{(2)},X\_{t}^{(3)}]^{\top} is latent and evolves under measure ℙ\mathbb{P} according to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt+1=Xt+κℙ​(θℙ−Xt)+Σ​Zt+1ℙ.X\_{t+1}=X\_{t}+\kappa^{\mathbb{P}}(\theta^{\mathbb{P}}-X\_{t})+\Sigma Z\_{t+1}^{\mathbb{P}}. |  | (2) |

Here, κℙ=[κi,jℙ]∈ℝ3×3\kappa^{\mathbb{P}}=[\kappa^{\mathbb{P}}\_{i,j}]\in\mathbb{R}^{3\times 3} is the mean-reversion parameters matrix, θℙ=[θ1ℙ,θ2ℙ,θ3ℙ]⊤\theta^{\mathbb{P}}=[\theta^{\mathbb{P}}\_{1},\theta^{\mathbb{P}}\_{2},\theta^{\mathbb{P}}\_{3}]^{\top} is the long-term average level of the factors, and Σ=[Σi,j]∈ℝ3×3\Sigma=[\Sigma\_{i,j}]\in\mathbb{R}^{3\times 3} is a diagonal volatility matrix with strictly positive entries. The innovations {Ztℙ}t=1T\{Z\_{t}^{\mathbb{P}}\}\_{t=1}^{T} are i.i.d. standard multivariate Gaussian vectors under ℙ\mathbb{P} with contemporaneous correlations

|  |  |  |
| --- | --- | --- |
|  | ρi​j(Z):=corr​(Zt,iℙ,Zt,jℙ),for ​i,j=1,2,3.\rho\_{ij}^{(Z)}:=\mathrm{corr}(Z\_{t,i}^{\mathbb{P}},Z\_{t,j}^{\mathbb{P}}),\quad\text{for }i,j=1,2,3. |  |

The initial factor value X0=x0∈ℝ3X\_{0}=x\_{0}\in\mathbb{R}^{3} is fixed and is assumed to be known.

To enable arbitrage-free pricing of interest rate derivatives such as bonds, bond options, swaps, and swaptions, eghbalzadeh2024discrete specify risk-neutral dynamics under an equivalent martingale measure ℚ∼ℙ\mathbb{Q}\sim\mathbb{P}. The factor dynamics under ℚ\mathbb{Q} is assumed to be of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt+1=Xt+κℚ​(θℚ−Xt)+Σ​Zt+1ℚ,X\_{t+1}=X\_{t}+\kappa^{\mathbb{Q}}(\theta^{\mathbb{Q}}-X\_{t})+\Sigma Z\_{t+1}^{\mathbb{Q}}, |  | (3) |

where κℚ\kappa^{\mathbb{Q}} and θℚ\theta^{\mathbb{Q}} are obtained by solving the system of equations

|  |  |  |  |
| --- | --- | --- | --- |
|  | {κℚ=κℙ−Σ​γ,κℚ​θℚ=κℙ​θℙ,\left\{\begin{aligned} \kappa^{\mathbb{Q}}&=\kappa^{\mathbb{P}}-\Sigma\gamma,\\ \kappa^{\mathbb{Q}}\theta^{\mathbb{Q}}&=\kappa^{\mathbb{P}}\theta^{\mathbb{P}},\end{aligned}\right. |  | (4) |

for some constant vector γ\gamma, with {Ztℚ}\{Z^{\mathbb{Q}}\_{t}\} being independent standard Gaussian vectors with correlation matrix [ρi​j(Z)]i,j=13[\rho\_{ij}^{(Z)}]^{3}\_{i,j=1} under ℚ\mathbb{Q}.
This dynamics retains the same autoregressive structure as under the physical measure. This consistency is desirable because it preserves analytical tractability and facilitates simulation under both real-world and risk-neutral measures.
Furthermore, it is assumed that matrix κℚ\kappa^{\mathbb{Q}} is of the form

|  |  |  |
| --- | --- | --- |
|  | κℚ=[0000λ−λ00λ],with ​λ∈(0,1).\kappa^{\mathbb{Q}}=\begin{bmatrix}0&0&0\\ 0&\lambda&-\lambda\\ 0&0&\lambda\end{bmatrix},\quad\text{with }\lambda\in(0,1). |  |

The null first row of κℚ\kappa^{\mathbb{Q}} entails that the first factor is non-stationary under ℚ\mathbb{Q} despite being stationary under ℙ\mathbb{P}.

#### Zero Coupon Pricing.

The DTAFNS model admits an exponential-affine solution for zero-coupon bond prices. Specifically, for a bond maturing at time TT, the arbitrage-free price at time t<Tt<T is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | P(t,T)=𝔼ℚ[exp(−Δ∑j=tT−1rj)|ℱt]=Aτexp[−ΔBτ⊤Xt],P(t,T)=\mathbb{E}^{\mathbb{Q}}\left[\exp\left(-\Delta\sum\_{j=t}^{T-1}r\_{j}\right)\middle|\mathcal{F}\_{t}\right]=A\_{\tau}\exp\left[-\Delta B\_{\tau}^{\top}X\_{t}\right], |  | (5) |

where τ=T−t\tau=T-t denotes the number of time steps remaining before maturity, and Bτ=[Bτ(1),Bτ(2),Bτ(3)]⊤B\_{\tau}=[B\_{\tau}^{(1)},B\_{\tau}^{(2)},B\_{\tau}^{(3)}]^{\top} is a vector of loadings associated with each factor. The mapping AτA\_{\tau} reflects the yield curve shape when term structure factors are null. Closed-form formulas for (Aτ,Bτ)(A\_{\tau},B\_{\tau}) are provided in Appendix [A](https://arxiv.org/html/2512.06639v1#A1 "Appendix A Zero-Coupon price ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.").

#### Interest Rate Swaps Pricing.

According to brigo2001interest, a Payer Forward-Starting Interest Rate Swap (PFS) is a contract with a future effective date TαT\_{\alpha},
where one party agrees to pay a fixed interest rate KK on a nominal amount NN and receive a floating rate over a sequence of dates {Tα+1,…,Tβ}\{T\_{\alpha+1},\ldots,T\_{\beta}\}, where Ti+1=Ti+1T\_{i+1}=T\_{i}+1 for all ii (with an elapse of Δ\Delta years occurring between TiT\_{i} and Ti+1T\_{i+1}).
At each payment date TiT\_{i} in this schedule, the fixed leg pays

|  |  |  |
| --- | --- | --- |
|  | N​K​Δ,NK\Delta, |  |

while the floating leg pays

|  |  |  |
| --- | --- | --- |
|  | N​L​(Ti−1,Ti)​Δ,NL(T\_{i-1},T\_{i})\Delta, |  |

where L​(Ti−1,Ti)L(T\_{i-1},T\_{i}) denotes the simply-compounded spot rate set at Ti−1T\_{i-1} for the period [Ti−1,Ti][T\_{i-1},T\_{i}]:

|  |  |  |
| --- | --- | --- |
|  | L​(Ti−1,Ti)=1−P​(Ti−1,Ti)P​(Ti−1,Ti)​Δ.L(T\_{i-1},T\_{i})=\frac{1-P(T\_{i-1},T\_{i})}{P(T\_{i-1},T\_{i})\Delta}. |  |

The floating leg resets at dates Tα,Tα+1,…,Tβ−1T\_{\alpha},T\_{\alpha+1},\ldots,T\_{\beta-1} and pays at dates Tα+1,…,TβT\_{\alpha+1},\ldots,T\_{\beta}. Let 𝒯:={Tα,…,Tβ}\mathcal{T}:=\{T\_{\alpha},\ldots,T\_{\beta}\} denote the full tenor schedule of the swap.

The discounted value of the PFS cash flows at a time t<Tαt<T\_{\alpha} is given by

|  |  |  |
| --- | --- | --- |
|  | ∑i=α+1βD​(t,Ti)​N​Δ​(L​(Ti−1,Ti)−K),\sum\_{i=\alpha+1}^{\beta}D(t,T\_{i})N\Delta\left(L(T\_{i-1},T\_{i})-K\right), |  |

where D​(t,Ti)=exp⁡(−Δ​∑s=tTi−1rs)D(t,T\_{i})=\exp\left(-\Delta\sum\_{s=t}^{T\_{i}-1}r\_{s}\right) is the stochastic discount factor between time tt and the payment date TiT\_{i}.
Using no-arbitrage arguments and risk-neutral pricing, the forward-start swap value can be expressed in terms of observable market instrument prices as

|  |  |  |  |
| --- | --- | --- | --- |
|  | PFS​(t,𝒯,N,K)=N​Δ​∑i=α+1βP​(t,Ti)​(F​(t;Ti−1,Ti)−K)=N​(P​(t,Tα)−P​(t,Tβ))−N​K​Δ​∑i=α+1βP​(t,Ti),\begin{split}\text{PFS}(t,\mathcal{T},N,K)&=N\Delta\sum\_{i=\alpha+1}^{\beta}P(t,T\_{i})\left(F(t;T\_{i-1},T\_{i})-K\right)\\ &=N\left(P(t,T\_{\alpha})-P(t,T\_{\beta})\right)-NK\Delta\sum\_{i=\alpha+1}^{\beta}P(t,T\_{i}),\end{split} |  | (6) |

where F​(t;Ti−1,Ti)F(t;T\_{i-1},T\_{i}) denotes the simply-compounded forward rate for the period [Ti−1,Ti][T\_{i-1},T\_{i}]

|  |  |  |
| --- | --- | --- |
|  | F​(t;Ti−1,Ti)=1Δ​(P​(t,Ti−1)P​(t,Ti)−1).F(t;T\_{i-1},T\_{i})=\frac{1}{\Delta}\Big(\frac{P(t,T\_{i-1})}{P(t,T\_{i})}-1\Big). |  |

The forward swap rate, denoted Sα,β​(t)S\_{\alpha,\beta}(t), is the fixed rate that equates the value of the PFS to zero (i.e., the par rate). Solving for this value yields

|  |  |  |
| --- | --- | --- |
|  | Sα,β​(t)=P​(t,Tα)−P​(t,Tβ)Δ​∑i=α+1βP​(t,Ti).S\_{\alpha,\beta}(t)=\frac{P(t,T\_{\alpha})-P(t,T\_{\beta})}{\Delta\sum\_{i=\alpha+1}^{\beta}P(t,T\_{i})}. |  |

This rate is commonly used as a benchmark in swaption pricing and hedging applications.

#### Swaption Pricing.

A European payer swaption is a financial derivative that grants its holder the right, but not the obligation, to enter into a payer interest rate swap (IRS) at a predetermined future time, typically coinciding with the first reset date of the underlying swap, denoted TαT\_{\alpha}. The length of the underlying swap, given by Tβ−TαT\_{\beta}-T\_{\alpha}, is referred to as the tenor of the swaption.

From ([6](https://arxiv.org/html/2512.06639v1#S2.E6 "In Interest Rate Swaps Pricing. ‣ 2 Market Environment and Financial Instruments ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.")), the value of the underlying payer IRS at the swaption maturity TαT\_{\alpha} is

|  |  |  |
| --- | --- | --- |
|  | N​Δ​∑i=α+1βP​(Tα,Ti)​(F​(Tα;Ti−1,Ti)−K).N\Delta\sum\_{i=\alpha+1}^{\beta}P(T\_{\alpha},T\_{i})\left(F(T\_{\alpha};T\_{i-1},T\_{i})-K\right). |  |

The swaption is exercised only if this value is positive. Thus, the discounted payoff of the payer swaption at a time t<Tαt<T\_{\alpha} is

|  |  |  |
| --- | --- | --- |
|  | N​D​(t,Tα)​Δ​(∑i=α+1βP​(Tα,Ti)​(F​(Tα;Ti−1,Ti)−K))+.ND(t,T\_{\alpha})\Delta\left(\sum\_{i=\alpha+1}^{\beta}P(T\_{\alpha},T\_{i})\left(F(T\_{\alpha};T\_{i-1},T\_{i})-K\right)\right)^{+}. |  |

The swaption is said to be at-the-money (ATM) if the strike equals the forward swap rate, i.e.

|  |  |  |
| --- | --- | --- |
|  | K=KATM:=Sα,β​(0)=P​(0,Tα)−P​(0,Tβ)Δ​∑i=α+1βP​(0,Ti).K=K\_{\text{ATM}}:=S\_{\alpha,\beta}(0)=\frac{P(0,T\_{\alpha})-P(0,T\_{\beta})}{\Delta\sum\_{i=\alpha+1}^{\beta}P(0,T\_{i})}. |  |

It is in-the-money (ITM) for the payer swaption if K<KATMK<K\_{\text{ATM}} and out-of-the-money (OTM) if K>KATMK>K\_{\text{ATM}}.

Because the holder of the swaption can, when exercising at maturity TαT\_{\alpha}, enter—at zero cost—an ATM payer swap whose fixed rate is the swap rate, the risk-neutral measure can be used to represent the time-tt price of a European payer swaption with notional NN, strike KK, and tenor structure 𝒯\mathcal{T} through

|  |  |  |
| --- | --- | --- |
|  | PS​[t,𝒯,K,N]=𝔼ℚ​[D​(t,Tα)​(N​(Sα,β​(Tα)−K)+​Δ​∑i=α+1βP​(Tα,Ti))|ℱt]=𝔼ℚ​[D​(t,Tα)​𝒫Tα|ℱt]\begin{split}\mathrm{PS}\left[t,\mathcal{T},K,N\right]&=\mathbb{E}^{\mathbb{Q}}\left[\left.D(t,T\_{\alpha})\left(N\left(S\_{\alpha,\beta}(T\_{\alpha})-K\right)^{+}\Delta\sum\_{i=\alpha+1}^{\beta}P(T\_{\alpha},T\_{i})\right)\right|\mathcal{F}\_{t}\right]=\mathbb{E}^{\mathbb{Q}}\left[D(t,T\_{\alpha})\mathcal{P}\_{T\_{\alpha}}|\mathcal{F}\_{t}\right]\end{split} |  |

where 𝒫Tα\mathcal{P}\_{T\_{\alpha}} is the swaption payoff at maturity

|  |  |  |
| --- | --- | --- |
|  | 𝒫Tα=N​(1−P​(Tα,Tβ)−K​Δ​∑i=α+1βP​(Tα,Ti))+.\mathcal{P}\_{T\_{\alpha}}=N\left(1-P(T\_{\alpha},T\_{\beta})-K\Delta\sum\_{i=\alpha+1}^{\beta}P(T\_{\alpha},T\_{i})\right)^{+}.\ |  |

As explained in godin2023pricing, the price can also be expressed by using the TαT\_{\alpha}-forward measure ℚTα\mathbb{Q}^{T\_{\alpha}}, which uses P​(t,Tα)P(t,T\_{\alpha}) as the numéraire to simplify the pricing formula

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | PS​[t,𝒯,K,N]\displaystyle\mathrm{PS}\left[t,\mathcal{T},K,N\right] | =P​(t,Tα)​𝔼ℚTα​[𝒫Tα|ℱt].\displaystyle=P(t,T\_{\alpha})\mathbb{E}^{\mathbb{Q}^{T\_{\alpha}}}\left[\mathcal{P}\_{T\_{\alpha}}|\mathcal{F}\_{t}\right]. |  | (7) |

This formulation reduces the pricing problem to computing the conditional expectation of a function of future bond prices. Since zero-coupon bond prices under the DTAFNS model are exponential-affine in the factors, the time-TαT\_{\alpha} bond prices involved in ([7](https://arxiv.org/html/2512.06639v1#S2.E7 "In Swaption Pricing. ‣ 2 Market Environment and Financial Instruments ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.")) can be fully characterized by the term structure factors XTαX\_{T\_{\alpha}}. For the dynamics of the factors under the TT-forward measure, refer to Appendix [B](https://arxiv.org/html/2512.06639v1#A2 "Appendix B Factor Dynamics under the 𝑇-forward Measure ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.").

## 3 Hedging Framework and Replicating Portfolio Construction

We consider a discrete-time hedging framework where hedging portfolio rebalancing dates are {0,1,…,Tα}\{0,1,\dots,T\_{\alpha}\}.
The objective is to construct a hedging portfolio to hedge a short position on a European swaption. Without loss of generality, a payer swaption is considered.

To hedge a short position in this option, an agent constructs a dynamic self-financing portfolio comprising MM forward-starting payer swaps (which may include the underlying swap) and a money market account that accrues interest at the prevailing short rate. The value of the hedging portfolio at time t≤Tαt\leq T\_{\alpha} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt=ϕt⊤​PFSt+ψt​ert−1​Δ,V\_{t}=\phi\_{t}^{\top}\mathrm{PFS}\_{t}+\psi\_{t}e^{r\_{t-1}\Delta}, |  | (8) |

where PFSt=[PFSt(1),…,PFSt(M)]⊤\mathrm{PFS}\_{t}=[\mathrm{PFS}\_{t}^{(1)},\dots,\mathrm{PFS}\_{t}^{(M)}]^{\top} is the time-tt value of the hedging forward-starting payer swaps, ψt\psi\_{t} is the cash amount held at time t−1t-1, which earns interest compounded at rate rt−1r\_{t-1}, and the hedging strategy is represented by the predictable process {(ϕt,ψt)}t=1Tα\{(\phi\_{t},\psi\_{t})\}\_{t=1}^{T\_{\alpha}}, where ϕt=[ϕt(1),…,ϕt(M)]⊤\phi\_{t}=[\phi\_{t}^{(1)},\dots,\phi\_{t}^{(M)}]^{\top} is the vector of hedge ratios (i.e., multiplier of the notional value) of the swap positions held at time t−1t-1.222In the case N=1N=1 considered in this work, ϕt\phi\_{t} represents notional values.
Under the self-financing condition, the cash holding is determined endogenously as333In unreported experiments, we have tested the inclusion of transaction costs, which impact the portfolio value. However, the impact of such costs under realistic cost levels reflective of market conditions was very minor, and thus we chose not to include them in the paper.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψt+1=Vt−ϕt+1⊤​PFSt.\psi\_{t+1}=V\_{t}-\phi\_{t+1}^{\top}\mathrm{PFS}\_{t}. |  | (9) |

The agent aims to determine an optimal dynamic hedging strategy {ϕt}t=1Tα\{\phi\_{t}\}^{T\_{\alpha}}\_{t=1}, with the goal of minimizing the hedging error risk at the swaption maturity TαT\_{\alpha}.

We refer to the set 𝒳={Xt,t=0,…,Tα}\mathcal{X}=\{X\_{t},\,t=0,\dots,T\_{\alpha}\} as the path of yield curve factors up to time TαT\_{\alpha}. At each time tt, the hedger observes the vector YtY\_{t}, which represents the information taken into account to determine their hedging positions.
The composition of YtY\_{t} in our setting is detailed subsequently. Based on this input, the hedge ratios are determined by a policy function πθ:Yt↦ϕt+1\pi\_{\theta}:Y\_{t}\mapsto\phi\_{t+1}, parameterized by a neural network with weights θ\theta:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕt+1=πθ​(Yt).\phi\_{t+1}=\pi\_{\theta}(Y\_{t}). |  | (10) |

This approximation allows representing the sequence of hedging decisions as a parameterized control policy that is learned from simulated market scenarios.

The terminal hedging error is defined as the difference between the swaption payoff and the final hedging portfolio value:

|  |  |  |
| --- | --- | --- |
|  | hTα​(πθ)=𝒫Tα−VTα​(πθ),h\_{T\_{\alpha}}(\pi\_{\theta})=\mathcal{P}\_{T\_{\alpha}}-V\_{T\_{\alpha}}(\pi\_{\theta}), |  |

where the dependence of the terminal hedging portfolio value VTαV\_{T\_{\alpha}} on policy parameters θ\theta is made explicit.
A positive value of hTαh\_{T\_{\alpha}} indicates a hedging shortfall, i.e., the hedging strategy failed to fully offset the liability. The hedger’s objective is to find a policy πθ\pi\_{\theta} that minimizes a risk measure applied to the hedging error:

|  |  |  |  |
| --- | --- | --- | --- |
|  | arg⁡minθ⁡𝒥​(θ),𝒥​(θ)≡ζ​(hTα​(πθ))\arg\min\_{\theta}\;\mathcal{J}(\theta),\quad\mathcal{J}(\theta)\equiv\zeta\left(h\_{T\_{\alpha}}(\pi\_{\theta})\right) |  | (11) |

for a given risk measure ζ\zeta.
This formulation is closely related to the deep hedging framework introduced in buehler2019deep, where trading strategies are optimized end-to-end using neural networks and Monte Carlo simulations.

### 3.1 Deep Hedging Using Reinforcement Learning

To assess the performance of a given policy, we use Monte Carlo simulation. We generate nn independent paths 𝒳(i)\mathcal{X}^{(i)}, i=1,…,ni=1,\dots,n, where each path is a realization of the factor process {Xt}t=1,…,Tα\{X\_{t}\}\_{t=1,\dots,T\_{\alpha}}. For each path and for a fixed parameter vector θ\theta,
we compute the replicating portfolio values using ([8](https://arxiv.org/html/2512.06639v1#S3.E8 "In 3 Hedging Framework and Replicating Portfolio Construction ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.")), with hedge ratios at each time step being given by ([10](https://arxiv.org/html/2512.06639v1#S3.E10 "In 3 Hedging Framework and Replicating Portfolio Construction ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.")).

Accordingly, we define the terminal hedging error hTαh\_{T\_{\alpha}} as a function of both the market path 𝒳(i)\mathcal{X}^{(i)} and the hedging strategy generated by the policy πθ\pi\_{\theta}, which we denote by

|  |  |  |
| --- | --- | --- |
|  | hTα(i):=hTα​(πθ;𝒳(i)).h\_{T\_{\alpha}}^{(i)}:=h\_{T\_{\alpha}}(\pi\_{\theta};\mathcal{X}^{(i)}). |  |

Estimates of the objective function ([11](https://arxiv.org/html/2512.06639v1#S3.E11 "In 3 Hedging Framework and Replicating Portfolio Construction ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.")) are obtained from the empirical distribution of hedging errors. Denote by nbn\_{b} the batch size used in training.
The mean squared error (MSE) objective is estimated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥^MSE​(θ)=1nb​∑i=1nb[hTα(i)]2.\hat{\mathcal{J}}\_{\text{MSE}}(\theta)=\frac{1}{n\_{b}}\sum\_{i=1}^{n\_{b}}\left[h\_{T\_{\alpha}}^{(i)}\right]^{2}. |  | (12) |

The downside risk (DR) objective penalizes only under-hedging scenarios, and its estimate is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥^DR​(θ)=1nb​∑i=1nb[max⁡(hTα(i),0)]2.\hat{\mathcal{J}}\_{\text{DR}}(\theta)=\frac{1}{n\_{b}}\sum\_{i=1}^{n\_{b}}\left[\max(h\_{T\_{\alpha}}^{(i)},0)\right]^{2}. |  | (13) |

When the objective is to control tail risk, we consider the CVaR as the performance criterion. Following rockafellar2000optimization, we define the empirical 𝔞\mathfrak{a}-value-at-risk of the hedging error distribution as

|  |  |  |  |
| --- | --- | --- | --- |
|  | v^𝔞nb:=inf{z∈ℝ|1nb​∑k=1nb𝟏{hTα(i)≤z}≥𝔞}.\hat{v}\_{\mathfrak{a}}^{\,n\_{b}}:=\inf\left\{z\in\mathbb{R}\;\middle|\;\frac{1}{n\_{b}}\sum\_{k=1}^{n\_{b}}\mathbf{1}\_{\{h\_{T\_{\alpha}}^{(i)}\leq z\}}\geq\mathfrak{a}\right\}. |  | (14) |

The corresponding CVaRa is estimated via:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥^CVaR​(θ)=v^𝔞nb+1nb​(1−𝔞)​∑i=1nb[hTα(i)−v^αnb]+,\hat{\mathcal{J}}\_{\text{CVaR}}(\theta)=\hat{v}\_{\mathfrak{a}}^{\,n\_{b}}+\frac{1}{n\_{b}(1-\mathfrak{a})}\sum\_{i=1}^{n\_{b}}\left[h\_{T\_{\alpha}}^{(i)}-\hat{v}\_{\alpha}^{\,n\_{b}}\right]^{+}, |  | (15) |

This loss encourages the agent to minimize the average excess of large hedging errors over the value-at-risk, aiming to mitigate the severity of highly adverse scenarios.

The optimization problem ([11](https://arxiv.org/html/2512.06639v1#S3.E11 "In 3 Hedging Framework and Replicating Portfolio Construction ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.")) is tackled using mini-batch stochastic gradient descent (SGD). The parameter vector θ\theta is iteratively updated using:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ(j+1)=θ(j)−𝔫j​∇θ𝒥^​(θ(j)),\theta^{(j+1)}=\theta^{(j)}-\mathfrak{n}\_{j}\nabla\_{\theta}\hat{\mathcal{J}}(\theta^{(j)}), |  | (16) |

where 𝔫j\mathfrak{n}\_{j} is the learning rate for iteration jj, and the gradient ∇θ𝒥^​(θ(j))\nabla\_{\theta}\hat{\mathcal{J}}(\theta^{(j)}) is computed using automatic differentiation in PyTorch.
Here, the superscript jj denotes the iteration index of the SGD procedure. At each iteration, a new batch of Monte Carlo paths 𝒳\mathcal{X} is generated under the current policy θ(j)\theta^{(j)}, and the risk-based objective 𝒥^​(θ(j))\hat{\mathcal{J}}(\theta^{(j)}) is estimated from this batch. This procedure ensures that parameter updates are always based on fresh simulations reflecting the evolving policy.

### 3.2 The Rho-Hedging Benchmark

In this section, we introduce the rho-hedging strategy that serves as a benchmark for the learning-based methods developed in this paper.

To hedge the swaption position against market risk, the common rho-hedging procedure neutralizes its sensitivity to the key term structure factors Xt(1)X\_{t}^{(1)}, Xt(2)X\_{t}^{(2)}, or Xt(3)X\_{t}^{(3)} that drive the evolution of interest rates under the DTAFNS model. This is achieved by equating the factor-wise sensitivities (i.e., the rhos) of the swaption and these of the replicating portfolio.

When using a single forward-start swap (M=1M=1) in the replicating portfolio, to neutralize the sensitivity to a single factor k∈{1,2,3}k\in\{1,2,3\}; the hedge ratio must be set to

|  |  |  |
| --- | --- | --- |
|  | ϕt+1(1)=∂PSt∂Xt(k)/∂PFSt(1)∂Xt(k).\phi\_{t+1}^{(1)}=\frac{\partial\mathrm{PS}\_{t}}{\partial X\_{t}^{(k)}}\bigg/\frac{\partial\mathrm{PFS}^{(1)}\_{t}}{\partial X\_{t}^{(k)}}. |  |

where PSt\mathrm{PS}\_{t} denotes the time-tt value of the payer swaption.

The choice of the risk factor that is neutralized depends on which risk dimension (e.g., level, slope, or curvature) is deemed most significant for the swaption exposure. As the factor Xt−1(k)X\_{t-1}^{(k)} evolves over time, ϕt(1)\phi\_{t}^{(1)} is dynamically updated, resulting in a rho-hedging strategy that rebalances the portfolio to attempt tracking the swaption’s value.

In the case where two swaps are used (M=2M=2), the hedge ratios that neutralize the sensitivity of two of the factors k≠j∈{1,2,3}k\neq j\in\{1,2,3\} to be chosen are determined by solving the linear system

|  |  |  |
| --- | --- | --- |
|  | [∂PFSt(1)∂Xt(j)∂PFSt(2)∂Xt(j)∂PFSt(1)∂Xt(k)∂PFSt(2)∂Xt(k)]⏟=⁣:Qt​[ϕt+1(1)ϕt+1(2)]=[∂PSt∂Xt(j)∂PSt∂Xt(k)]⏟=⁣:bt.\underbrace{\begin{bmatrix}\frac{\partial\mathrm{PFS}^{(1)}\_{t}}{\partial X\_{t}^{(j)}}&\frac{\partial\mathrm{PFS}^{(2)}\_{t}}{\partial X\_{t}^{(j)}}\\ \frac{\partial\mathrm{PFS}^{(1)}\_{t}}{\partial X\_{t}^{(k)}}&\frac{\partial\mathrm{PFS}^{(2)}\_{t}}{\partial X\_{t}^{(k)}}\end{bmatrix}}\_{=:Q\_{t}}\begin{bmatrix}\phi\_{t+1}^{(1)}\\ \phi\_{t+1}^{(2)}\end{bmatrix}=\underbrace{\begin{bmatrix}\frac{\partial\mathrm{PS}\_{t}}{\partial X\_{t}^{(j)}}\\ \frac{\partial\mathrm{PS}\_{t}}{\partial X\_{t}^{(k)}}\end{bmatrix}}\_{=:b\_{t}}. |  |

This ensures that the portfolio has a null local sensititivy with respect to both factors jj and kk. This system of linear equations can be generalized for neutralizing three factors using three swaps.

However, instead of applying above formulas providing exact solutions, we instead apply a regularized least-squares approach to minimize net sensitivites of the portfolio. This enhances numerical stability and incorporates additional sensitivity control.
Specifically, the hedge ratios are obtained from

|  |  |  |
| --- | --- | --- |
|  | ϕt+1=arg⁡minϕ​‖Qt​ϕ−bt‖2+l1​‖ϕ‖2+l2​‖ϕ−ϕt‖2,\phi\_{t+1}=\underset{\phi}{\arg\min}\,\|Q\_{t}\phi-b\_{t}\|^{2}+l\_{1}\|\phi\|^{2}+l\_{2}\|\phi-\phi\_{t}\|^{2}, |  |

where l1l\_{1} and l2l\_{2} are regularization parameters and QtQ\_{t} and btb\_{t} are respectively the matrix and the vector containing sensitivities of all hedging swaps and of the swaption to the various factors. This approach removes abrupt fluctuations in hedging positions that were otherwise (very rarely) observed in our simulations, leading to instability and poor performance. In the vast majority of cases the impact of the regularization on hedging positions is almost null for the mild values parameters l1l\_{1} and l2l\_{2} considered in our work.444In this study we set l1=l2=0.01l\_{1}=l\_{2}=0.01.

Once the hedge ratios are determined, we impose two additional leverage constraints on the outputs which are detailed in Section [4.2](https://arxiv.org/html/2512.06639v1#S4.SS2 "4.2 Leverage Bounds ‣ 4 Market and Model Setup ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.").

The price of a PFS is given by ([6](https://arxiv.org/html/2512.06639v1#S2.E6 "In Interest Rate Swaps Pricing. ‣ 2 Market Environment and Financial Instruments ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.")), and its gradient with respect to factor k=1,2,3k=1,2,3 is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂PFSt∂Xt(k)=−N​Δ​(BTα−t(k)​P​(t,Tα)−BTβ−t(k)​P​(t,Tβ)−K​Δ​∑i=α+1βBTi−t(k)​P​(t,Ti)).\begin{split}\frac{\partial\mathrm{PFS}\_{t}}{\partial X\_{t}^{(k)}}&=-N\Delta\Big(B\_{T\_{\alpha}-t}^{(k)}P(t,T\_{\alpha})-B\_{T\_{\beta}-t}^{(k)}P(t,T\_{\beta})-K\Delta\sum\_{i=\alpha+1}^{\beta}B\_{T\_{i}-t}^{(k)}P(t,T\_{i})\Big).\end{split} |  | (17) |

## 4 Market and Model Setup

We use the calibrated DTAFNS model proposed by eghbalzadeh2024discrete on end-of-month Canadian spot rate curves from January 1986 to January 2022 (434 months) to simulate the yield curve term structure factors. The calibrated parameters are given in Appendix [C](https://arxiv.org/html/2512.06639v1#A3 "Appendix C Model Parameter Setup ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.").

Based on this model, we investigate the dynamic hedging of a European payer swaption written on a plain-vanilla forward-starting interest rate swap. Specifically, we consider an ATM swaption with a maturity of Tα=60T\_{\alpha}=60 months (5 years with Δ=1/12\Delta=1/12), giving the holder the right to enter into a 5y×\times10y payer swap, i.e. a swap that starts in five years and runs for ten years (a five-years-forward, ten-year-tenor swap), with a fixed rate of K=2.5083K=2.5083% and unit notional (N=1N=1). The hedging portfolio is rebalanced monthly, using forward-starting payer swaps as hedging instruments. Hedging swaps include the underlying swap and possibly other swaps with different tenors or maturities. The swaption price at time t=0t=0 serves as the initial value V0V\_{0} of the replicating portfolio.

### 4.1 Hedging Network Architecture

For the hedging agent, we employ a four-layer fully connected neural network (FCNN) to approximate the mapping from observed market features to hedge ratios. The width of the respective FCNN hidden layers is [8,32,32,8][8,32,32,8], followed by a final output layer of size MM, where MM is the number of forward-starting swaps used in the replicating portfolio. For some input YtY\_{t}, the network output is a vector ϕt+1=πθ​(Yt)\phi\_{t+1}=\pi\_{\theta}(Y\_{t}) representing the hedge ratios for the MM swaps at time tt before any constraint is imposed. Once the unconstrained hedge ratios have been determined, we impose two constraints on the outputs to reflect risk limits analogous to these applied in practice. The details about the constraints are provided in Section [4.2](https://arxiv.org/html/2512.06639v1#S4.SS2 "4.2 Leverage Bounds ‣ 4 Market and Model Setup ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.").

The input vector YtY\_{t} which includes the current values of the term structure factors XtX\_{t}, the time-to-maturity (Tα−t)​Δ(T\_{\alpha}-t)\Delta, and the current portfolio value VtV\_{t}.
All inputs except time-to-maturity are first normalized for each batch. The processed input then passes through a sequence of fully connected layers, each followed by a Mish activation function (misra2019mish)

|  |  |  |
| --- | --- | --- |
|  | x↦x⋅tanh⁡(ln⁡(1+ex)),x\mapsto x\cdot\tanh(\ln(1+e^{x})), |  |

which provides smooth and non-monotonic transformations.
No dropout is applied, and the network is kept relatively shallow to avoid overfitting given the structured nature of the inputs. We employ a linear activation function for the final layer to determine the positions in the hedging swaps.

The neural network parameters are initialized using the Kaiming uniform method (he2015delving), which defines the initial parameter vector θ(0)\theta^{(0)}. It is designed for networks with nonlinear activations and helps maintain stable gradients during training.

Training is performed using the Adam optimizer from kingma2014adam with an initial learning rate of 5×10−35\times 10^{-3}.
The model is trained for a maximum of 800 epochs. The learning rate is reduced using a plateau-based scheduler, and early stopping is applied with a patience threshold of 200 epochs to avoid overfitting. Each epoch consists of multiple mini-batches of size nb=2048n\_{b}=2048, drawn from a simulated dataset of n=100,000n=100{,}000 Monte Carlo paths. The training objective is to minimize a user-specified risk measure, such as MSE, DR, or CVaR as defined in Section [3.1](https://arxiv.org/html/2512.06639v1#S3.SS1 "3.1 Deep Hedging Using Reinforcement Learning ‣ 3 Hedging Framework and Replicating Portfolio Construction ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare."), applied to the terminal hedging error.

### 4.2 Leverage Bounds

The hedging positions outputted by the neural network and rho-hedging positions are unconstrained. In practice, trading desks face binding limits: treasury funding and credit lines limits, clearing margin and liquidity haircut constraints, counterparty/concentration limits, and book-level risk controls such as gross notional and DV01/PV01 caps.555DV01 (Dollar Value of a Basis Point) measures first-order price sensitivity to a 1 bp parallel shift in the yield curve.
PV01 (Present Value of 1 bp) is the present value change from a 1 bp change in the fixed rate of a swap.
To reflect these operational realities and to avoid pro-cyclical “lever up on gains, delever on losses” behavior,666A constraint scaled by the current hedging portfolio value |Vt||V\_{t}| expands risk capacity after gains and contracts it after losses, inducing buy-high/sell-low rebalancing and elevated turnover. We mitigate this by using a stabilized basis (|Vt|+B)(|V\_{t}|+B) in our limits.
we impose two complementary constraints on our notional positions

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (per-leg exposure) | |ϕi,t|​|PFSi,t|≤Lper​(|Vt|+B),∀i,\displaystyle|\phi\_{i,t}|\,|\mathrm{PFS}\_{i,t}|\;\leq\;L\_{\text{per}}\,(|V\_{t}|+B),\quad\forall i, |  | (18) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (gross exposure) | ∑i=1K|ϕi,t|​|PFSi,t|≤Lgt​(|Vt|+B).\displaystyle\sum\_{i=1}^{K}|\phi\_{i,t}|\,|\mathrm{PFS}\_{i,t}|\;\leq\;L\_{\text{gt}}\,(|V\_{t}|+B). |  | (19) |

The absolute value of the ϕi,t\phi\_{i,t}, the hedging notional position for leg ii, and that of the forward-starting swap price PFSi,t\mathrm{PFS}\_{i,t}, serve as the exposure factor in dollars, consistent with desk practices for notional caps. The first constraint prevents any single leg from dominating the book (mitigating ill-conditioning and concentration risk), while the second controls overall leverage, in line with standard gross exposure or DV01 guardrails at the portfolio level. The scaling term (|Vt|+B)(|V\_{t}|+B) provides a stabilized risk budget: VtV\_{t} denotes the current portfolio value (taken in absolute value in implementation), and B≥0B\!\geq\!0 is a fixed liquidity/capital buffer that (i) avoids vanishing limits when |Vt||V\_{t}| is small, and (ii) curbs pro-cyclical upsizing when |Vt||V\_{t}| spikes. The leverage multipliers LperL\_{\text{per}} and LgtL\_{\text{gt}} are policy parameters reflecting the desk’s risk appetite and external constraints (funding, margin, and capital).777By setting Vt=V0V\_{t}=V\_{0}, one can change the dynamic leverage to a static leverage constraint.
These bounds keep the hedge implementable across liquidity regimes,
align with real-world risk controls, and improve numerical stability during learning and backtesting.

Let the (unconstrained) per-leg dollar exposures be

|  |  |  |
| --- | --- | --- |
|  | ei,t=|φi,t|​|PFSi,t|,i=1,…,M,e\_{i,t}\;=\;\lvert\varphi\_{i,t}\rvert\,\lvert\mathrm{PFS}\_{i,t}\rvert,\qquad i=1,\dots,M, |  |

where φi,t\varphi\_{i,t} is the unconstrained position on swap ii at time tt obtained either from the neural network for deep hedging, or from regularized least-squares for rho-hedging.
Limits scale with a stabilized basis

|  |  |  |
| --- | --- | --- |
|  | Bt=|Vt|+B,B\_{t}\;=\;\lvert V\_{t}\rvert+B, |  |

We enforce a per-leg exposure cap and a gross (portfolio-level) exposure cap

|  |  |  |
| --- | --- | --- |
|  | 0≤xi,t≤Lper​Bt,∑i=1Mxi,t≤Lgt​Bt,0\leq x\_{i,t}\leq L\_{\mathrm{per}}\,B\_{t},\qquad\sum\_{i=1}^{M}x\_{i,t}\leq L\_{\mathrm{gt}}\,B\_{t}, |  |

where xi,t=|ϕi,t|​|PFSi,t|x\_{i,t}=|\phi\_{i,t}||\mathrm{PFS}\_{i,t}|.
At each tt, we project et=[e1,t,…,eM,t]e\_{t}=[e\_{1,t},\dots,e\_{M,t}] onto the feasible set by

|  |  |  |
| --- | --- | --- |
|  | xt⋆=arg⁡minx∈ℝM⁡‖x−et‖22s.t.0≤xi≤Lper​Bt​(i=1,…,M),∑i=1Mxi≤Lgt​Bt.x\_{t}^{\star}=\arg\min\_{x\in\mathbb{R}^{M}}\;\big\|x-e\_{t}\big\|\_{2}^{2}\quad\text{s.t.}\quad 0\leq x\_{i}\leq L\_{\mathrm{per}}\,B\_{t}\ (i=1,\dots,M),\;\sum\_{i=1}^{M}x\_{i}\leq L\_{\mathrm{gt}}\,B\_{t}. |  |

Feasible hedge notionals are then recovered, preserving direction,

|  |  |  |
| --- | --- | --- |
|  | ϕi,t=sign⁡(φi,t)​xi,t⋆|PFSi,t|.\phi\_{i,t}\;=\;\operatorname{sign}\!\big(\varphi\_{i,t}\big)\;\frac{x\_{i,t}^{\star}}{\lvert\mathrm{PFS}\_{i,t}\rvert}\,. |  |

We employ this projection on both benchmark and RL weights to obtain a fair comparison888We use Lp​e​r=2L\_{per}=2, Lg​t=3L\_{gt}=3 and B=1B=1.. Furthermore, such constraints are imposed post-hoc instead of being integrated during the training of the policy since these constraints reduce the smoothness of the objective function and lead to less stable training.

### 4.3 Swaption prices and their derivatives

Swaption prices provided by ([7](https://arxiv.org/html/2512.06639v1#S2.E7 "In Swaption Pricing. ‣ 2 Market Environment and Financial Instruments ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.")) are not available in closed-form. To avoid recomputing estimates of such prices through Monte Carlo simulation every time a price is needed, we pre-compute prices of swaptions offline with a Kolmogorov-Arnold neural network. The methodology is explained in Appendix [D](https://arxiv.org/html/2512.06639v1#A4 "Appendix D Swaption Pricing Network ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare."). This approach is also used to compute the first-order sensitivity of swaption prices with respect to term structure risk factors, as also detailed in that section.

## 5 Numerical Experiments

In this section, we evaluate the performance of the deep hedging strategy and compare it to that of conventional rho-hedging approaches. The evaluation is performed on N(O​O​S)=100,000N^{(OOS)}=100,\!000 out-of-sample paths generated with the same parameters that are used to generate training set paths.

### 5.1 Hedging Performance Metrics

We assess the distribution of terminal hedging errors using a comprehensive set of risk and performance metrics that are hereby provided.

#### Mean.

The *mean* of the hedging errors hTα(i),i=1,…,N(O​O​S)h\_{T\_{\alpha}}^{(i)},i=1,\ldots,N^{(OOS)} captures the average hedging bias, indicating whether a strategy systematically *overhedges* (negative mean) or *underhedges* (positive mean).

#### Root Mean Squared Error (RMSE).

The RMSE, which is calculated as the square root of the MSE obtained by applying formula ([12](https://arxiv.org/html/2512.06639v1#S3.E12 "In 3.1 Deep Hedging Using Reinforcement Learning ‣ 3 Hedging Framework and Replicating Portfolio Construction ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.")) to out-of-sample paths, penalizes both over- and underhedging symmetrically.

#### Root Downside Risk (RDR).

Computed through the square root of ([13](https://arxiv.org/html/2512.06639v1#S3.E13 "In 3.1 Deep Hedging Using Reinforcement Learning ‣ 3 Hedging Framework and Replicating Portfolio Construction ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.")) applied on out-of-sample paths, the root downside risk metric quantifies the impact of positive hedging errors, assessing the severity of underhedging losses.

#### Tail Risk.

Tail risk is measured with CVaR99%, which gives the average value of the worst 1% hedging losses hTα(i)h\_{T\_{\alpha}}^{(i)}.

#### Probability of underhedging.

We also compute the *probability of underhedging*

|  |  |  |
| --- | --- | --- |
|  | P​(H​E>0)=1N(O​O​S)​∑i=1N(O​O​S)𝟙{hTα(i)>0},P(HE>0)=\frac{1}{N^{(OOS)}}\sum\_{i=1}^{N^{(OOS)}}\mathds{1}\_{\{h\_{T\_{\alpha}}^{(i)}>0\}}, |  |

which reflects the frequency at which the hedging strategy fails to fully replicate the swaption payoff.

#### Hedging Risk Reduction (HRR).

To evaluate the effectiveness of the hedging strategy relative to an unhedged position, we compute the *hedging risk reduction*, defined as

|  |  |  |
| --- | --- | --- |
|  | HRR=1−Std​(hTα)Std​(hTαunhedged),\text{HRR}=1-\frac{\text{Std}(h\_{T\_{\alpha}})}{\text{Std}(h^{\text{unhedged}}\_{T\_{\alpha}})}, |  |

where hTαunhedgedh^{\text{unhedged}}\_{T\_{\alpha}} denotes the hedging error in absence of hedging, i.e. when ϕ≡𝟎\phi\equiv\mathbf{0}. When no hedging is applied, the swaption premium received at time 0 is deposited in a bank account and accrues risk-free interest until the swaption maturity.
The HRR metric represents the percentage reduction in hedging error volatility achieved by hedging.

#### Trading Intensity (TI).

TI measures the extent of replicating portfolio position fluctuations between consecutive time steps, across all hedging instruments.

|  |  |  |
| --- | --- | --- |
|  | TI=1N(O​O​S)​∑i=1N(O​O​S)∑t=1Tα∑k=1M|ϕt(k)−ϕt−1(k)|.\text{TI}=\frac{1}{N^{(OOS)}}\sum\_{i=1}^{N^{(OOS)}}\sum\_{t=1}^{T\_{\alpha}}\sum\_{k=1}^{M}\left|\phi\_{t}^{(k)}-\phi\_{t-1}^{(k)}\right|. |  |

#### Dynamic Tracking Error (DTE).

Dynamic Tracking Error measures the pathwise deviation between the hedged portfolio value and the swaption price across the hedging horizon. For each path ii, it is defined as

|  |  |  |
| --- | --- | --- |
|  | DTEi=1Tα​∑t=1Tα(Vi,t−PSi,t)2,\text{DTE}\_{i}=\sqrt{\frac{1}{T\_{\alpha}}\sum\_{t=1}^{T\_{\alpha}}\big(V\_{i,t}-\mathrm{PS}\_{i,t}\big)^{2}}, |  |

where PSi,t\mathrm{PS}\_{i,t} is the swaption price at time tt for path ii.
The average DTE across all paths is

|  |  |  |
| --- | --- | --- |
|  | DTE=1N(O​O​S)​∑i=1N(O​O​S)DTEi.\text{DTE}=\frac{1}{N^{(OOS)}}\sum\_{i=1}^{N^{(OOS)}}\text{DTE}\_{i}. |  |

### 5.2 Hedging Performance

This section presents an assessment of the performance of our proposed RL method through Monte Carlo simulation. The RL method is compared to conventional dynamic rho-hedging approaches. The impact of the number of hedging instruments on hedging performance is assessed, with either one, two or three swaps being included in the hedging portfolio.
The single hedging swap case employs the underlying forward-starting swap, which has a start date on the swaption’s maturity and whose tenor is the same as that of the swaption. For the two-swap scenario, we augment the hedging portfolio by including an additional 10y×\times2y swap, i.e. two-year-tenor swap starting in ten years. This second swap is chosen to load primarily on the long end of the curve, capturing movements in long-term rates and in the level and slope components that the underlying hedging instrument alone may not span. Extending further, the three-swap case introduces in addition a 2y×\times2y swap, which concentrates exposure at the front end of the curve, targeting short-term rate dynamics and improving control of near-dated shocks.
Using short tenors and maturities that are far from these of the underlying for the additional hedging swaps allows
reducing correlation among hedging legs and protecting against a broader span of risks,
yielding a more effective dynamic hedge.

We use the following notation for rho-hedging. ρ−X(i)\rho-X^{(i)} utilizes a single-swap hedge and neutralizes exposure to the rate of factor ii at each rebalancing date. ρ−(X(i),X(k))\rho-(X^{(i)},X^{(k)}) hedges rely instead on two swaps and neutralize the exposure to the two factors (i,k)(i,k). Lastly, ρ\rho hedging neutralizes exposure to all three factors using three hedging swaps.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Strategy | Mean | RMSE | RDR | CVaR99% | P(HE >> 0) | HRR | TI | DTE |
| Hedging with One Swap | | | | | | | | |
| RL MSE | -0.0033 | 0.0086 | 0.0042 | 0.0228 | 0.3220 | 0.8798 | 2.7623 | 0.0049 |
| RL DR | -0.0052 | 0.0109 | 0.0032 | 0.0179 | 0.3092 | 0.8551 | 2.3316 | 0.0057 |
| RL CVaR | -0.0055 | 0.0128 | 0.0039 | 0.0157 | 0.3910 | 0.8251 | 2.2039 | 0.0066 |
| ρ−X(1)\rho\!-\!X^{(1)} | -0.0046 | 0.0106 | 0.0038 | 0.0185 | 0.3380 | 0.8556 | 2.4602 | 0.0053 |
| ρ−X(2)\rho\!-\!X^{(2)} | -0.0031 | 0.0147 | 0.0091 | 0.0394 | 0.3933 | 0.7838 | 2.4153 | 0.0109 |
| ρ−X(3)\rho\!-\!X^{(3)} | -0.0038 | 0.0089 | 0.0039 | 0.0218 | 0.2965 | 0.8790 | 2.5955 | 0.0049 |
| Hedging with Two Swaps | | | | | | | | |
| RL MSE | -0.0025 | 0.0080 | 0.0042 | 0.0230 | 0.3413 | 0.8860 | 9.8791 | 0.0043 |
| RL DR | -0.0087 | 0.0135 | 0.0022 | 0.0147 | 0.1729 | 0.8441 | 6.9082 | 0.0074 |
| RL CVaR | -0.0081 | 0.0151 | 0.0030 | 0.0131 | 0.3353 | 0.8088 | 4.4295 | 0.0076 |
| ρ−(X(1),X(2))\rho\!-\!(X^{(1)},X^{(2)}) | -0.0068 | 0.0120 | 0.0031 | 0.0175 | 0.2396 | 0.8508 | 7.6409 | 0.0063 |
| ρ−(X(1),X(3))\rho\!-\!(X^{(1)},X^{(3)}) | -0.0037 | 0.0122 | 0.0059 | 0.0276 | 0.3933 | 0.8247 | 7.6791 | 0.0057 |
| ρ−(X(2),X(3))\rho\!-\!(X^{(2)},X^{(3)}) | -0.0076 | 0.0132 | 0.0044 | 0.0238 | 0.2377 | 0.8380 | 6.6959 | 0.0083 |
| Hedging with Three Swaps | | | | | | | | |
| RL MSE | -0.0014 | 0.0076 | 0.0045 | 0.0236 | 0.3981 | 0.8868 | 20.2907 | 0.0040 |
| RL DR | -0.0089 | 0.0137 | 0.0022 | 0.0145 | 0.1629 | 0.8438 | 10.6775 | 0.0076 |
| RL CVaR | -0.0080 | 0.0143 | 0.0029 | 0.0131 | 0.3028 | 0.8209 | 4.1674 | 0.0075 |
| ρ\rho Hedging | -0.0051 | 0.0106 | 0.0034 | 0.0182 | 0.2988 | 0.8603 | 6.7003 | 0.0051 |

Table 1: Performance metrics across reinforcement learning and rho-hedging strategies using one, two, and three swaps.

Table [1](https://arxiv.org/html/2512.06639v1#S5.T1 "Table 1 ‣ 5.2 Hedging Performance ‣ 5 Numerical Experiments ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.") reports performance metrics for RL-based and rho-hedging strategies using one, two, and three swaps on an out-of-sample dataset.

In the single-swap setting, RL methods consistently outperform traditional rho-hedging when the performance metric matches the objective function of the RL agent. The RL-MSE strategy achieves the lowest RMSE (0.0086), highlighting its precision in tracking the target payoff. The RL-DR specification provides the strongest downside protection, with the smallest root downside risk (0.0032). The RL-CVaR approach offers the greatest reduction in tail exposure, recording the lowest CVaR99% (0.0157). Furthermore, RL-CVaR strategies systematically have the lowest trading intensity, which would reduce trading costs in practice.
Among rho-hedging strategies, hedging the first factor provides the most risk protection, at least in terms of RDR and CVaR99%.

Adding a second swap substantially improves hedging performance for all strategies. RL strategies still retain a clear advantage. The RL-MSE model again produces the highest risk reduction as measured by HRR (0.8860) and the lowest RMSE (0.0080), confirming better replication accuracy.
The RL-DR objective minimizes root downside risk (0.0022) and yields the lowest probability of underhedging (0.1729), while RL-CVaR delivers superior tail performance with a CVaR99% of 0.0131.

Adding a third swap to the hedging portfolio only provides marginal additional benefits (if any) in terms of performance, both for RL methods and rho-hedging. For instance, the ρ\rho-hedging strategy with three swaps underperforms the ρ​(X(1),X(2))\rho(X^{(1)},X^{(2)}) in terms of DR and CVaR99%. This indicates that hedging effectiveness approaches a near-optimal level with two instruments. This can be explained by the high negative correlations between the level factor and the two others as seen in matrix ρ\rho from Appendix [C](https://arxiv.org/html/2512.06639v1#A3 "Appendix C Model Parameter Setup ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare."), which are respectively −0.63-0.63 and −0.41-0.41. While adding a new swap does not result in a significant improvement in performance, it notably increases trading intensity, especially for the RL-MSE and RL-DR strategies. There is thus insufficient de-correlation between factors to justify the use of a third hedging instrument. The inability of the third hedging swap to materially improve hedging performance is consistent with previous studies suggesting that increasing the number of hedging instruments beyond a certain point yields little incremental benefit and may raise instability (fan2003hedging; driessen2003performance; fan2007pricing).

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |

![Refer to caption](x1.png)

![Refer to caption](x2.png)

![Refer to caption](x3.png)

![Refer to caption](x4.png)

![Refer to caption](x5.png)

![Refer to caption](x6.png)

![Refer to caption](x7.png)


(a) MSE

![Refer to caption](x8.png)


(b) DR

![Refer to caption](x9.png)


(c) CVaR99%

Figure 1: Comparison of kernel density estimates of in-sample (IS) and out-of-sample (OOS) hedging error distributions for RL-based strategies, and out-of-sample distributions for dynamic rho-hedge strategies, across different hedging portfolio compositions. The vertical lines indicate the mean of each distribution, while the black line indicates a null hedging error. The first row corresponds to hedging portfolios with one swap, the second row to two swaps, and the third row to three swaps.

Figure [1](https://arxiv.org/html/2512.06639v1#S5.F1 "Figure 1 ‣ 5.2 Hedging Performance ‣ 5 Numerical Experiments ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.") shows kernel density plots comparing the hedging error distributions of RL and rho-hedging strategies under the three objective risk measures for RL agents: MSE, DR, and CVaR99%. Strategies displayed use either one, two, or three swaps as hedging instruments. The RL strategies consistently produce tighter, well-centered error distributions, with very little difference between in-sample and out-of-sample results. This pattern indicates that the RL methods do not overfit the training data.
For the MSE objective especially, the RL error curves are symmetric, and they sharply peak near their mean,
indicating accurate and stable hedging. In contrast, the rho-hedging strategies often have wider distributions with heavier tails, and distribution modes are in several instances far from the mean.
This implies more frequent large errors and some bias in replication. Under the DR and CVaR objectives, RL methods exhibit thinner right tails, confirming that they manage risks related to extreme losses and downside fluctuations better.

Overall, RL-based hedging consistently outperforms rho-hedging by delivering superior risk mitigation performance.

### 5.3 Residual Sensitivity Analysis

This section analyzes whether the outperformance of RL hedging strategies is partially due to
systematic exposure to some of the risk factors in order to harvest associated risk premia.
We conduct a residual exposure sensitivity analysis. Define, for any time step tt, the residual vector, ξt=[ξt(1),ξt(2),ξt(3)]⊤\xi\_{t}=[\xi\_{t}^{(1)},\xi\_{t}^{(2)},\xi\_{t}^{(3)}]^{\top}:

|  |  |  |
| --- | --- | --- |
|  | ξt=At​ϕt+1−νt,\xi\_{t}=A\_{t}\phi\_{t+1}-\nu\_{t}, |  |

where νt\nu\_{t} is the vector of the swaptions’ sensitivities to the underlying risk factors,
and AtA\_{t} is a 3×M3\times M matrix of sensitivities of the available swaps in the replicating portfolio, where MM is the number of swaps in the replicating portfolio:

|  |  |  |
| --- | --- | --- |
|  | (νt)i=∂PSt∂Xt(i),and(At)i,j=∂PFSt(j)∂Xt(i),fori=1,2,3,j=1,…,M.\Big(\nu\_{t}\Big)\_{i}=\frac{\partial\mathrm{PS\_{t}}}{\partial X\_{t}^{(i)}},\quad\text{and}\quad\Big(A\_{t}\Big)\_{i,j}=\frac{\partial\mathrm{PFS\_{t}^{(j)}}}{\partial X\_{t}^{(i)}},\quad\text{for}\quad i=1,2,3,\quad j=1,\dots,M. |  |

By plotting the time series of the mean value across all paths of each component ξt(k)\xi\_{t}^{(k)}, we can identify whether there is a systematic bias in any direction. If ξt(k)\xi\_{t}^{(k)} fluctuates around zero with low variance, the RL agent behaves similarly to a traditional rho-hedger.
Conversely, if ξt(k)\xi\_{t}^{(k)} consistently remains above (below) zero, it indicates that the RL agent systematically positions itself to benefit from an increase (decrease)
in the value of factor X(k)X^{(k)}. This analysis helps to assess whether the observed outperformance of RL hedging strategies arises at least partially from directional exposure.

We examine the agent’s behavior along two sets of paths: those that ultimately result in either (i) a positive payoff or (ii) a zero payoff. Focusing on these sets of scenarios separately provides insight into how the agent adjusts its actions based on the option moneyness as the portfolio approaches maturity. Paths associated with a high (low) payoff are associated with an increase (a decrease) in interest rates, specifically in the level factor. The value of payer swaps also increases when interest rates increase.

The three factors, corresponding respectively to the level (X(1)X^{(1)}), slope (X(2)X^{(2)}), and curvature (X(3)X^{(3)}) of the yield curve, are associated with distinct risk premia. The level (factor X(1)X^{(1)}) is associated with long-term interest rates and inflation expectations. This factor is linked to the term premium: investors typically require compensation for holding long-duration bonds. The slope (factor X(2)X^{(2)}) is associated with steepening/flattening of the yield curve and reflects the difference between short- and long-term rates. It is linked to carry/roll-down trade premium. The curvature (factor X(3)X^{(3)}) represents medium-term deviations, often tied to intermediate-term economic uncertainty or changing term premia. It is associated with convexity and volatility-of-volatility risk, where investors often demand compensation for bearing curvature exposure (duffee2002term; diebold2006forecasting).

In our model, we can measure risk premia by comparing the difference in the long-run averages of factors under the physical and risk-neutral measures, namely θℙ−θℚ\theta^{\mathbb{P}}-\theta^{\mathbb{Q}}. For the slope and curvature factors, this difference points to premia of about −3.3%-3.3\% and −2.6%-2.6\%, respectively. However, since the level factor process has a unit root under ℚ\mathbb{Q}, the long-term mean is not θ1ℙ−θ1ℚ\theta^{\mathbb{P}}\_{1}-\theta^{\mathbb{Q}}\_{1} and the latter quantity cannot be used to evaluate the risk premium.
Instead, the risk-neutral conditional expected value of Xt(1)X^{(1)}\_{t} given information at time zero stays fixed at X0(1)=−0.0312X\_{0}^{(1)}=-0.0312. Conversely, the long-run mean for X(1)X^{(1)} is θ1ℙ=0\theta^{\mathbb{P}}\_{1}=0 under the physical measure ℙ\mathbb{P}; we can thus conclude that there is a positive level risk premium at time t=0t=0 given by θ1ℙ−X0(1)=0.0312\theta^{\mathbb{P}}\_{1}-X\_{0}^{(1)}=0.0312.
Therefore, systematic long exposure to the slope or curvature factors entails effectively paying a risk premium, which is equivalent to buying insurance against unfavourable states.
Cutting back on those exposures, or even holding negative exposure, in turn, reflects efforts to save on costs. On the other hand, holding long level exposure leads to collecting its positive premium. Conversely, reducing the exposure to the level factor reflects a desire to manage risk despite reducing prospective profits.

In Figure [2](https://arxiv.org/html/2512.06639v1#S5.F2 "Figure 2 ‣ 5.3 Residual Sensitivity Analysis ‣ 5 Numerical Experiments ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare."), we track the residual exposure to the three term structure factors when a short swaption position is hedged with two swaps. Results are presented for the RL agents using the MSE, DR, and CVaR99% risk measures as objectives, and for rho-hedging.

We observe that patterns in exposure to the slope and curvature are similar; for each RL objective function or scenario set considered, both tend to increase or decrease simultaneously. This can be explained by these two factors having similary dynamics under our setting, with both being associated with negative risk premium, having a strong negative correlation with the level factor and being positively correlated together (0.2993). Contrarily, the level factor exhibits distictive dynamics; it is associated with a positive premium at t=0t=0, it has a unit root under the risk-neutral measure and it is negatively correlated to the two other factors. This explains why, in several instances, exposure to the level factor displays different patterns than these associated with the curvature and slope factors.

The MSE agent responds symmetrically to hedging errors, aiming to minimize any deviation rather than guard only against downside or tail risk. When the payoff is likely to turn positive, it tends to hold a long position in the level factor, collecting the associated risk premium to help cover for such payoff and getting profits from hedging swaps. In contrast, when the trade is unlikely to finish in-the-money, as maturity approaches, the agent reduces its level exposure and tends to even go short, giving up potential upside in order to avoid hedging profits.
The average exposure to the other factors is modest; while the average curvature exposure is almost nil throughout the hedging horizon, the slope exposure moves towards zero as maturity approaches. Overall, the MSE agent strategy is simple and focused: it actively manages level risk to steer the hedging portfolio value and avoid non-zero hedging profits or shortfalls, while treating slope and curvature as secondary.

Risk exposures associated with the hedging strategy of the DR-RL agent depart from these of the MSE-RL agent;
whereas the curvature exposure (green line) was almost null for the latter, large short (negative) exposures are observed for the former at earlier stages. This is reflective of asymmetric preferences of the RL agent who does not fear being penalized for large hedging profits potentially stemming from harvesting the (negative) risk premium on third factor through short exposure. Such harvested premium can help creating a buffer in early stages of the hedge to offset potential future losses.

While CVaR-RL and DR-RL agents both have predominantly negative exposures within paths leading to a positive payoff, the exposure to the level factor in paths with a zero payoff is vastly different. For instance, the very large positive level and slope exposures observed in later stages for the CVaR-RL agent reflect the fact that, when the swaption is out-of-the-money (recall that the short rate is the sum of level and slope factors), the only way a tail-risk event can occur is through a very large spike in interest rates; positive exposure on the slope and level factors helps guarding against hikes in these two factors.

![Refer to caption](x10.png)

![Refer to caption](x11.png)

![Refer to caption](x12.png)

Figure 2: Residuals for 2-Swap Portfolio – Multiple Objectives. Shaded areas represent scaled standard deviation bands (0.5×\timesstd) for visual clarity

### 5.4 Feature Importance

To understand what drives RL hedging strategies, it is important to evaluate how much influence each model input has on the rebalacing decisions being applied. Analyzing feature importance allows us to see which of the state variables play a bigger role in hedging position adjustments, improving both transparency and interpretability. We assess the contribution of the term structure factors, namely the level, slope, and curvature of the yield curve, the hedging portfolio value, and the time-to-maturity, and examine how they shape the model’s hedging policy.

In our setting, we apply SHapley Additive exPlanations (SHAP) to the hedging portfolio positions generated by the RL policy. This framework follows the approach of vstrumbelj2014explaining, later formalized by lundberg2017unified. SHAP values decompose each hedging decision into contributions from the various state variables (i.e. features) by measuring each feature’s marginal contribution. To implement Shapley decompositions, we use the shap package in Python. Under this implementation, Shapley decomposition values are obtained without retraining the model on reduced sets of features. Instead, when computing predictions that rely on a subset of features, the model with the full set of features is applied with white noise values being used to substitute for values of features that are dropped. A sample of 3000 randomly chosen observations is used to report results.

The resulting beeswarm plots shown in Figure [3](https://arxiv.org/html/2512.06639v1#S5.F3 "Figure 3 ‣ 5.4 Feature Importance ‣ 5 Numerical Experiments ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.") provide an intuitive way to interpret these attributions. Please note that the x axis has a different scale for the various subpanels to enhance visibility. Each row represents one of the three hedging agents associated with the three considered objective functions. Results are displayed for the two-hedging-swap case, with left (right) columns depicting positions on the first (second) hedging swap.
The horizontal axis represents the SHAP value, i.e., the impact of a feature on the hedging position: positive values push the position upward, while negative values push it downward. Each dot corresponds to one observation. The color encodes the magnitude of the feature value, with red indicating high values and blue indicating low values; the combination of points color and of their horizontal axis value reveals the directional impact of the features. Features exhibiting a wider spread for SHAP values exert stronger influence on the RL model’s hedging decisions.
Taken together, these elements reveal not only which features matter most, but also how their realizations drive hedging position adjustments.

![Refer to caption](x13.png)

![Refer to caption](x14.png)

![Refer to caption](x15.png)

![Refer to caption](x16.png)

![Refer to caption](x17.png)

![Refer to caption](x18.png)

Figure 3: Shapley feature importance of hedge swap weights for two hedging strategies (MSE, DR, CVaR).

Figure [3](https://arxiv.org/html/2512.06639v1#S5.F3 "Figure 3 ‣ 5.4 Feature Importance ‣ 5 Numerical Experiments ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.") reveals several important insights. First, the SHAP value ranges differ across the three RL objectives, indicating that each agent adjusts its swap positions with a distinct level of sensitivity depending on the optimization criterion. Additionally, within each agent, the SHAP values for the first swap (the swap underlying the swaption) exhibit a much narrower range than those of the second swap.
This is because the tenor of the underlying swap is 10 years, whereas it is only 2 years for the second hedging swap; the price of the first swap exhibits much more variability and thus positions on the second swap must be on a higher scale to provide the same hedging effect.
Furthermore, the CVaR-RL agent displays a markedly narrower SHAP range compared with the MSE-RL and DR-RL agents, indicating far smaller adjustments in its hedge positions. This aligns with Table [1](https://arxiv.org/html/2512.06639v1#S5.T1 "Table 1 ‣ 5.2 Hedging Performance ‣ 5 Numerical Experiments ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare."), where the CVaR-RL strategy exhibits the lowest trading intensity (TI).
Comparing the MSE-RL and DR-RL agents, the SHAP distributions for MSE-RL are wider and more asymmetric, explaining why the MSE-RL strategy has substantially higher trading intensity than the DR-RL strategy. Nevertheless, for all variables and for both swaps, the overall direction of the impact of any given feature on hedging positions is the same for MSE-RL and DR-RL. Interestingly, a finding that is not reported numerically in this paper is that the DR-RL agent has on average a long position on the second payer hedging swap, whereas the average position on the second swap is negative (short) for the MSE-RL. Despite this gap, positions are impacted in the same direction by standalone changes in features.
Furtheremore, regardless of the agent and the feature, the impact on the first and on the second hedging swap positions are always in opposite directions, which means that the position on the second swap is used to partially offset some exposure generated by positions in the first swap. This reflects that the underlying hedging swap is the primary instrument replicating the swaption payoff. In contrast, the second swap serves mainly to absorb residual risks that the first swap cannot hedge, or to mitigate unwarranted risk exposure created by positions on the first swap.

The level feature has very high variable importance for all three agents and both hedging swaps. The term structure level is the main driver of risk in our model. The portfolio value also is very important for the MSE-RL and DR-RL agents, whereas such variable is less impactful for the CVaR-RL agent. Interestingly, for the DR-RL agent, the impact of portfolio value is very asymmetric; when the hedger is ahead (i.e. large portfolio value) it can be aggressive in holding a larger underlying swap position to protect against potential hikes in interest rates. This is different for the MSE-RL agent who would be penalized for holding large positions on the first swap and collecting the level premium, since this would exacerbate large gains.
The inclusion of the portfolio value within state variables informing hedging decisions contributes to the out-performance of RL strategies over rho-hedging benchmarks, since the latter do not factor-in such information when making hedging decisions.
The time-to-maturity plays a more important role for the CVaR-RL agent; as maturity approaches the CVaR-RL hedger is better informed about whether the realized scenario is a tail risk event and must act more swiftly accordingly. The slope and curvature factors have more a modest impact that varies according to the agent’s objective function.

### 5.5 Market Sensitivity Analysis

In this section, we examine the robustness of the hedging strategies to model misspecification. Specifically, we consider separately perturbations on two key sets of parameters of the yield curve factor process ([2](https://arxiv.org/html/2512.06639v1#S2.E2 "In 2 Market Environment and Financial Instruments ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.")): the mean-reversion speed parameters κℙ\kappa^{\mathbb{P}} and the long-run means θℙ\theta^{\mathbb{P}}. We then evaluate out-of-sample hedging performance of agents trained on original parameters when hedging on paths generated with perturbed parameters. Benchmarks also rely on hedging positions calculated with original parameters. We define perturbed parameter as

|  |  |  |
| --- | --- | --- |
|  | κ′=cκ​κℙ,θ′=cθ​θℙ,\kappa^{\prime}=c\_{\kappa}\kappa^{\mathbb{P}},\qquad\theta^{\prime}=c\_{\theta}\theta^{\mathbb{P}}, |  |

with scaling constants set to cκ=cθ=1.20c\_{\kappa}=c\_{\theta}=1.20.

Table [2](https://arxiv.org/html/2512.06639v1#S5.T2 "Table 2 ‣ 5.5 Market Sensitivity Analysis ‣ 5 Numerical Experiments ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.") and Table [3](https://arxiv.org/html/2512.06639v1#S5.T3 "Table 3 ‣ 5.5 Market Sensitivity Analysis ‣ 5 Numerical Experiments ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.") report the performance of hedging strategies under perturbations respectively to the mean-reversion speed parameters κℙ\kappa^{\mathbb{P}}, and to the long-run mean parameters θℙ\theta^{\mathbb{P}}.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Strategy | Mean | RMSE | RDR | CVaR99% | P(HE >> 0) | HRR | TI | DTE |
| Hedging with One Swap | | | | | | | | |
| RL MSE | -0.0031 | 0.0095 | 0.0053 | 0.0277 | 0.3392 | 0.8639 | 2.8249 | 0.0061 |
| RL DR | -0.0052 | 0.0115 | 0.0041 | 0.0228 | 0.3126 | 0.8462 | 2.4137 | 0.0072 |
| RL CVaR | -0.0055 | 0.0128 | 0.0043 | 0.0191 | 0.3626 | 0.8257 | 2.2844 | 0.0080 |
| ρ−X(1)\rho\!-\!X^{(1)} | -0.0045 | 0.0113 | 0.0048 | 0.0241 | 0.3309 | 0.8444 | 2.4602 | 0.0067 |
| ρ−X(2)\rho\!-\!X^{(2)} | -0.0023 | 0.0156 | 0.0100 | 0.0404 | 0.4342 | 0.7683 | 2.4153 | 0.0117 |
| ρ−X(3)\rho\!-\!X^{(3)} | -0.0037 | 0.0098 | 0.0050 | 0.0268 | 0.3114 | 0.8630 | 2.5955 | 0.0062 |
| Hedging with Two Swaps | | | | | | | | |
| RL MSE | -0.0024 | 0.0090 | 0.0054 | 0.0282 | 0.3528 | 0.8702 | 9.1072 | 0.0056 |
| RL DR | -0.0091 | 0.0140 | 0.0025 | 0.0168 | 0.1740 | 0.8412 | 7.2776 | 0.0098 |
| RL CVaR | -0.0084 | 0.0152 | 0.0031 | 0.0156 | 0.3003 | 0.8110 | 4.5699 | 0.0097 |
| ρ−(X(1),X(2))\rho\!-\!(X^{(1)},X^{(2)}) | -0.0070 | 0.0127 | 0.0037 | 0.0205 | 0.2551 | 0.8414 | 7.6409 | 0.0086 |
| ρ−(X(1),X(3))\rho\!-\!(X^{(1)},X^{(3)}) | -0.0036 | 0.0128 | 0.0067 | 0.0307 | 0.3826 | 0.8173 | 7.6791 | 0.0068 |
| ρ−(X(2),X(3))\rho\!-\!(X^{(2)},X^{(3)}) | -0.0081 | 0.0137 | 0.0045 | 0.0260 | 0.2182 | 0.8349 | 6.6959 | 0.0102 |
| Hedging with Three Swaps | | | | | | | | |
| RL MSE | -0.0012 | 0.0084 | 0.0056 | 0.0283 | 0.4084 | 0.8755 | 19.0079 | 0.0050 |
| RL DR | -0.0095 | 0.0141 | 0.0024 | 0.0163 | 0.1484 | 0.8442 | 11.2466 | 0.0101 |
| RL CVaR | -0.0083 | 0.0144 | 0.0031 | 0.0156 | 0.2782 | 0.8238 | 4.2854 | 0.0096 |
| ρ\rho Hedging | -0.0051 | 0.0113 | 0.0044 | 0.0227 | 0.3071 | 0.8494 | 6.7003 | 0.0069 |

Table 2: Performance metrics under κℙ\kappa^{\mathbb{P}}-shocks for RL and ρ\rho-hedging strategies using one, two, and three swaps.

The impact of parameter misspecification differs between the two perturbation scenarios. When κℙ\kappa^{\mathbb{P}} is perturbed, the deterioration in hedging performance is more important for rho-hedging strategies than for deep hedges. For instance, in the case of hedging with three swaps, the absolute difference between the RDR of the RL-DR trading strategy with shocks on κ\kappa (displayed in Table [2](https://arxiv.org/html/2512.06639v1#S5.T2 "Table 2 ‣ 5.5 Market Sensitivity Analysis ‣ 5 Numerical Experiments ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.")) and that without such shocks (see Table [1](https://arxiv.org/html/2512.06639v1#S5.T1 "Table 1 ‣ 5.2 Hedging Performance ‣ 5 Numerical Experiments ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.")) is only 0.00020.0002. Similarly, the absolute change in C​V​a​R99%CVaR\_{99\%} for the RL-CVaR agent is 0.00250.0025. Conversely the rho-hedges show higher sensitivity to parameter perturbation, with corresponding RDR and C​V​a​R99%CVaR\_{99\%} differences being 0.00100.0010 and 0.00450.0045, respectively.
Errors in the speed of mean-reversion mainly affect the persistence of market shocks, which RL policies are better able to absorb.

Perturbations to θℙ\theta^{\mathbb{P}} lead to more pronounced degradation of performance across all metrics. Shifting the long-run mean introduces a structural drift in the factor dynamics, which results in larger MSE, downside risk and CVaR99%\mathrm{CVaR}\_{99\%}. Both RL and ρ\rho-hedges deteriorate under these conditions, but the RL agents still have higher performance than the traditional first-order sensitivity-based strategies, e.g. 0.00570.0057 versus 0.00700.0070 for RDR and 0.02820.0282 versus 0.02940.0294 for CVaR99%\mathrm{CVaR}\_{99\%} in the three-hedging-swaps case.

RL strategies consistently deliver lower tail risk, and better hedging risk reduction than rho-hedges under perturbed parameters.
The main reason why the hedging models are less sensitive to changes in κℙ\kappa^{\mathbb{P}} is that altering the speed of mean reversion does not drastically modify the average shape of the factor paths; they still revert toward the same long‐run mean. In contrast, changing the long‐run mean θℙ\theta^{\mathbb{P}} shifts the entire yield curve factor long-term levels; the effect of altered risk factor premia to which hedging portfolios are exposed compounds over time, which then leads to a substantial drop in performance.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Strategy | Mean | RMSE | RDR | CVaR99% | P(HE >> 0) | HRR | TI | DTE |
| Hedging with One Swap | | | | | | | | |
| RL MSE | -0.0028 | 0.0134 | 0.0080 | 0.0352 | 0.4346 | 0.8021 | 2.7291 | 0.0114 |
| RL DR | -0.0044 | 0.0148 | 0.0072 | 0.0313 | 0.4347 | 0.7864 | 2.3318 | 0.0124 |
| RL CVaR | -0.0047 | 0.0153 | 0.0071 | 0.0263 | 0.4135 | 0.7800 | 2.2091 | 0.0127 |
| ρ−X(1)\rho\!-\!X^{(1)} | -0.0039 | 0.0142 | 0.0073 | 0.0295 | 0.4267 | 0.7939 | 2.4602 | 0.0120 |
| ρ−X(2)\rho\!-\!X^{(2)} | -0.0007 | 0.0187 | 0.0129 | 0.0445 | 0.5066 | 0.7181 | 2.4153 | 0.0132 |
| ρ−X(3)\rho\!-\!X^{(3)} | -0.0032 | 0.0133 | 0.0073 | 0.0321 | 0.4299 | 0.8064 | 2.5955 | 0.0117 |
| Hedging with Two Swaps | | | | | | | | |
| RL MSE | -0.0021 | 0.0134 | 0.0084 | 0.0362 | 0.4602 | 0.8216 | 9.5996 | 0.0110 |
| RL DR | -0.0073 | 0.0162 | 0.0059 | 0.0286 | 0.3713 | 0.8055 | 6.9664 | 0.0145 |
| RL CVaR | -0.0068 | 0.0169 | 0.0064 | 0.0246 | 0.3720 | 0.7922 | 4.4346 | 0.0141 |
| ρ−(X(1),X(2))\rho\!-\!(X^{(1)},X^{(2)}) | -0.0055 | 0.0151 | 0.0068 | 0.0290 | 0.3931 | 0.8109 | 7.6409 | 0.0133 |
| ρ−(X(1),X(3))\rho\!-\!(X^{(1)},X^{(3)}) | -0.0028 | 0.0154 | 0.0092 | 0.0359 | 0.4353 | 0.7960 | 7.6791 | 0.0117 |
| ρ−(X(2),X(3))\rho\!-\!(X^{(2)},X^{(3)}) | -0.0072 | 0.0155 | 0.0066 | 0.0344 | 0.2756 | 0.8157 | 6.6959 | 0.0151 |
| Hedging with Three Swaps | | | | | | | | |
| RL MSE | -0.0016 | 0.0130 | 0.0083 | 0.0351 | 0.4791 | 0.8273 | 19.9834 | 0.0107 |
| RL DR | -0.0075 | 0.0160 | 0.0057 | 0.0282 | 0.3544 | 0.8101 | 10.7588 | 0.0147 |
| RL CVaR | -0.0067 | 0.0162 | 0.0062 | 0.0246 | 0.3667 | 0.8026 | 4.1602 | 0.0140 |
| ρ\rho Hedging | -0.0045 | 0.0144 | 0.0070 | 0.0294 | 0.4141 | 0.8169 | 6.7003 | 0.0124 |

Table 3: Performance metrics under θℙ\theta^{\mathbb{P}}-shocks for RL and ρ\rho-hedging strategies using one, two, and three swaps.

## 6 Conclusion

In this paper, we set out to investigate whether RL can provide a more effective and robust framework to produce dynamic hedges of swaption positions compared to traditional sensitivity-based rho-hedging.
The analysis yields several key insights. First, based on our three-factor arbitrage-free dynamic Nelson-Siegel model setting, we find that the incremental benefit of adding a second swap into the hedging portfolio is substantial, while further improvements from the inclusion of a third instrument are modest. While the underlying asset swap is the primary instrument that is relied upon for replication, the second swap allows adjusting residual exposures, e.g. mitigating unwarranted exposure created by positions on the first swap.
Our approach incorporates multiple possible objective functions, namely mean squared error, downside risk, and CVaR. We highlight that different risk preferences translate into distinct hedging styles, with dynamically-adjusted risk exposure to the various term structure factors exhibiting different patterns across the various RL objective functions. A variable importance assessment highlights that the level risk factor is the most impactful out of the three term structure factors in terms of hedging decisions. The hedging portfolio value, which is not used by benchmark strategies, also influences hedging decisions considerably, at least for RL agents using MSE or downside risk as their objective. Model misspecification tests, in which hedging performance is assessed on interest rate paths generated with perturbed parameters, highlight the resilience of the RL strategies which still out-perform benchmarks. Taken together, these findings suggest that reinforcement learning offers a compelling framework for the dynamic hedging of swaptions.

## Appendix A Zero-Coupon price

As shown in eghbalzadeh2024discrete, the time-tt price of a risk-free zero-coupon bond paying one dollar on maturity T>tT>t is, under the such model,

|  |  |  |
| --- | --- | --- |
|  | P​(t,T)=Aτ​exp⁡[−Δ​Bτ⊤​Xt],P(t,T)=A\_{\tau}\exp\left[-\Delta B\_{\tau}^{\top}X\_{t}\right], |  |

where τ=T−t\tau=T-t, Bτ=[Bτ(1),Bτ(2),Bτ(3)]⊤B\_{\tau}=\left[B^{(1)}\_{\tau},B^{(2)}\_{\tau},B^{(3)}\_{\tau}\right]^{\top} and

|  |  |  |
| --- | --- | --- |
|  | Bτ(1)=τ,Bτ(2)=1−(1−λ)τλ,Bτ(3)=1−(1−λ)τ−1λ−(τ−1)​(1−λ)τ−1,B^{(1)}\_{\tau}=\tau,\quad B^{(2)}\_{\tau}=\frac{1-(1-\lambda)^{\tau}}{\lambda},\quad B^{(3)}\_{\tau}=\frac{1-(1-\lambda)^{\tau-1}}{\lambda}-(\tau-1)(1-\lambda)^{\tau-1}, |  |

|  |  |  |
| --- | --- | --- |
|  | log⁡Aτ=−Δ​θ2ℚ​(Bτ(1)−Bτ(2))+Δ​θ3ℚ​Bτ(3)+12​Δ2​vτ,\log A\_{\tau}=-\Delta\theta\_{2}^{\mathbb{Q}}(B\_{\tau}^{(1)}-B\_{\tau}^{(2)})+\Delta\theta\_{3}^{\mathbb{Q}}B\_{\tau}^{(3)}+\frac{1}{2}\Delta^{2}v\_{\tau}, |  |

with

vτ=(∑i=13∑j=13vτ(i,j)),\displaystyle v\_{\tau}=\left(\sum\_{i=1}^{3}\sum\_{j=1}^{3}v\_{\tau}^{(i,j)}\right),

vτ(1,1)=Σ1,12​τ​(τ−1)​(2​τ−1)6,\displaystyle v\_{\tau}^{(1,1)}=\Sigma\_{1,1}^{2}\frac{\tau(\tau-1)(2\tau-1)}{6},
vτ(2,2)=Σ2,22λ2​(τ−2​[1−(1−λ)τλ]+1−(1−λ)2​τ1−(1−λ)2),\displaystyle v\_{\tau}^{(2,2)}=\frac{\Sigma\_{2,2}^{2}}{\lambda^{2}}\left(\tau-2\left[\frac{1-(1-\lambda)^{\tau}}{\lambda}\right]+\frac{1-(1-\lambda)^{2\tau}}{1-(1-\lambda)^{2}}\right),
vτ(3,3)=𝟙{τ>1}Σ3,32λ2[τ−2+ζ0((1−λ)2,τ−1)+λ2ζ2((1−λ)2,τ−1)\displaystyle v\_{\tau}^{(3,3)}=\mathds{1}\_{\{\tau>1\}}\frac{\Sigma\_{3,3}^{2}}{\lambda^{2}}\left[\tau-2+\zeta\_{0}((1-\lambda)^{2},\tau-1)+\lambda^{2}\zeta\_{2}((1-\lambda)^{2},\tau-1)\right.

|  |  |  |
| --- | --- | --- |
|  | −2ζ0((1−λ),τ−1)−2λζ1((1−λ),τ−1)+2λζ1((1−λ)2,τ−1)],\left.-2\zeta\_{0}((1-\lambda),\tau-1)-2\lambda\zeta\_{1}((1-\lambda),\tau-1)+2\lambda\zeta\_{1}((1-\lambda)^{2},\tau-1)\right], |  |

vτ(1,2)=vτ(2,1)=ρ1,2​Σ1,1​Σ2,2​1λ​(τ​(τ−1)2−ζ1​((1−λ),τ)),\displaystyle v\_{\tau}^{(1,2)}=v\_{\tau}^{(2,1)}=\rho\_{1,2}\Sigma\_{1,1}\Sigma\_{2,2}\frac{1}{\lambda}\left(\frac{\tau(\tau-1)}{2}-\zeta\_{1}((1-\lambda),\tau)\right),

vτ(1,3)=vτ(3,1)=𝟙{τ>1}ρ1,3Σ1,1Σ3,31λ[τ​(τ−1)2−1−ζ0((1−λ),τ−1)\displaystyle v\_{\tau}^{(1,3)}=v\_{\tau}^{(3,1)}=\mathds{1}\_{\{\tau>1\}}\rho\_{1,3}\Sigma\_{1,1}\Sigma\_{3,3}\frac{1}{\lambda}\Big[\frac{\tau(\tau-1)}{2}-1-\zeta\_{0}((1-\lambda),\tau-1)

|  |  |  |
| --- | --- | --- |
|  | −(λ+1)ζ1((1−λ),τ−1)−λζ2((1−λ),τ−1)],-(\lambda+1)\zeta\_{1}((1-\lambda),\tau-1)-\lambda\zeta\_{2}((1-\lambda),\tau-1)\Big], |  |

vτ(2,3)=vτ(3,2)=𝟙{τ>1}ρ2,3Σ2,2Σ3,3(τ−2−(2−λ)​ζ0​((1−λ),τ−1)+(1−λ)​ζ0​((1−λ)2,τ−1)λ2\displaystyle v\_{\tau}^{(2,3)}=v\_{\tau}^{(3,2)}=\mathds{1}\_{\{\tau>1\}}\rho\_{2,3}\Sigma\_{2,2}\Sigma\_{3,3}\left(\frac{\tau-2-(2-\lambda)\zeta\_{0}((1-\lambda),\tau-1)+(1-\lambda)\zeta\_{0}((1-\lambda)^{2},\tau-1)}{\lambda^{2}}\right.

|  |  |  |
| --- | --- | --- |
|  | +−ζ1​((1−λ),τ−1)+(1−λ)​ζ1​((1−λ)2,τ−1)λ),\left.+\frac{-\zeta\_{1}((1-\lambda),\tau-1)+(1-\lambda)\zeta\_{1}((1-\lambda)^{2},\tau-1)}{\lambda}\right), |  |

ζ0​(r,τ)≡∑u=1τ−1ru=r−rτ1−r,\displaystyle\zeta\_{0}(r,\tau)\equiv\sum\_{u=1}^{\tau-1}r^{u}=\frac{r-r^{\tau}}{1-r},

ζ1​(r,τ)≡∑u=1τ−1u​ru=r−τ​rτ+(τ−1)​rτ+1(1−r)2,\displaystyle\zeta\_{1}(r,\tau)\equiv\sum\_{u=1}^{\tau-1}ur^{u}=\frac{r-\tau r^{\tau}+(\tau-1)r^{\tau+1}}{(1-r)^{2}},

ζ2​(r,τ)≡∑u=1τ−1u2​ru=−(τ−1)2​rτ+2+(2​τ2−2​τ−1)​rτ+1−τ2​rτ+r2+r(1−r)3.\displaystyle\zeta\_{2}(r,\tau)\equiv\sum\_{u=1}^{\tau-1}u^{2}r^{u}=\frac{-(\tau-1)^{2}r^{\tau+2}+(2\tau^{2}-2\tau-1)r^{\tau+1}-\tau^{2}r^{\tau}+r^{2}+r}{(1-r)^{3}}.

## Appendix B Factor Dynamics under the TT-forward Measure

Results from this appendix are drawn from godin2023pricing. The TT-forward measure, denoted by ℚT\mathbb{Q}^{T}, is defined using the price of a zero-coupon bond maturing at time TT as the numéraire. The Radon–Nikodym derivative for changing from the risk-neutral measure ℚ\mathbb{Q} to ℚT\mathbb{Q}^{T} is given by

|  |  |  |
| --- | --- | --- |
|  | d​ℚTd​ℚ=D​(0,T)P​(0,T).\frac{d\mathbb{Q}^{T}}{d\mathbb{Q}}=\frac{D(0,T)}{P(0,T)}. |  |

Let τ=T−t\tau=T-t. Under the TT-forward measure, the innovation process satisfies

|  |  |  |
| --- | --- | --- |
|  | Zt+1T=Zt+1ℚ+Δ​Σ​Bτ−1,Z\_{t+1}^{T}=Z\_{t+1}^{\mathbb{Q}}+\Delta\Sigma B\_{\tau-1}, |  |

and the conditional distribution of Zt+1TZ\_{t+1}^{T} given ℱt\mathcal{F}\_{t} is Gaussian with zero mean and covariance matrix ρ\rho. As shown in Proposition 2.1 and Corollary 2.1 of godin2023pricing, the sequence {ZjT}j=1T\{Z\_{j}^{T}\}\_{j=1}^{T} is conditionally independent under ℚT\mathbb{Q}^{T}.

Using this, the dynamics of the term structure factors under the TT-forward measure can be written in the affine form

|  |  |  |
| --- | --- | --- |
|  | Xt+1=Xt−ηtT+κT​(θT−Xt)+Σ​Zt+1T,X\_{t+1}=X\_{t}-\eta\_{t}^{T}+\kappa^{T}(\theta^{T}-X\_{t})+\Sigma Z\_{t+1}^{T}, |  |

where the parameters are defined as

|  |  |  |
| --- | --- | --- |
|  | θT=θℚ,κT=κℚ,ηtT=Δ​Σ​ρ​Σ​Bτ−1.\theta^{T}=\theta^{\mathbb{Q}},\quad\kappa^{T}=\kappa^{\mathbb{Q}},\quad\eta\_{t}^{T}=\Delta\Sigma\rho\Sigma B\_{\tau-1}. |  |

Finally, Proposition 2.2 in the same paper states that for any t+n≤Tt+n\leq T, the future factor values Xt+nX\_{t+n}, conditionally on ℱt\mathcal{F}\_{t}, follow a multivariate Gaussian distribution under ℚT\mathbb{Q}^{T} with explicitly computable mean vector and covariance matrix whose formulas are given in godin2023pricing. This tractability plays a crucial role in pricing and hedging derivatives such as swaptions under the DTAFNS model.

## Appendix C Model Parameter Setup

We use the calibrated DTAFNS model parameters proposed in eghbalzadeh2024discrete. They perform a joint estimation of parameters from measures ℙ\mathbb{P} and ℚ\mathbb{Q}, which gives the following estimates:

* •

  Shape parameter: λ=0.0233\lambda=0.0233.

* •

  Long-term means:

  |  |  |  |
  | --- | --- | --- |
  |  | θℙ=[0.00000.03010.0505],θℚ=[0.00000.06330.0766].\theta^{\mathbb{P}}=\begin{bmatrix}0.0000\\ 0.0301\\ 0.0505\end{bmatrix},\quad\theta^{\mathbb{Q}}=\begin{bmatrix}0.0000\\ 0.0633\\ 0.0766\end{bmatrix}. |  |
* •

  Correlation matrix of innovations:

  |  |  |  |
  | --- | --- | --- |
  |  | ρ=[1.0000−0.6303−0.4097−0.63031.00000.2993−0.40970.29931.0000].\rho=\begin{bmatrix}1.0000&-0.6303&-0.4097\\ -0.6303&1.0000&0.2993\\ -0.4097&0.2993&1.0000\end{bmatrix}. |  |
* •

  Volatilities (diagonal of Σ\Sigma):

  |  |  |  |
  | --- | --- | --- |
  |  | diag​(Σ)=[0.00270.00450.0070].\text{diag}(\Sigma)=\begin{bmatrix}0.0027\\ 0.0045\\ 0.0070\end{bmatrix}. |  |
* •

  Speed of mean-reversion (under ℙ\mathbb{P}):

  |  |  |  |
  | --- | --- | --- |
  |  | κℙ=[0.00750.00000.00000.00000.0288−0.02330.00000.00000.0354].\kappa^{\mathbb{P}}=\begin{bmatrix}0.0075&0.0000&0.0000\\ 0.0000&0.0288&-0.0233\\ 0.0000&0.0000&0.0354\end{bmatrix}. |  |
* •

  Speed of mean-reversion (under ℚ\mathbb{Q}):

  |  |  |  |
  | --- | --- | --- |
  |  | κℚ=[0.00000.00000.00000.00000.0233−0.02330.00000.00000.0233].\kappa^{\mathbb{Q}}=\begin{bmatrix}0.0000&0.0000&0.0000\\ 0.0000&0.0233&-0.0233\\ 0.0000&0.0000&0.0233\end{bmatrix}. |  |
* •

  Market price of risk vector:

  |  |  |  |
  | --- | --- | --- |
  |  | γ=[2.79231.20161.7167].\gamma=\begin{bmatrix}2.7923\\ 1.2016\\ 1.7167\end{bmatrix}. |  |
* •

  Initial Factor Values:999Starting values X0X\_{0} correspond to filtered values of the factors process on January 31, 2022, which is the last of day of the sample that is used to estimate parameters. See Appendix B.2 of eghbalzadeh2024evaluation for such values.

  |  |  |  |
  | --- | --- | --- |
  |  | X0=[−0.03120.03840.0688].X\_{0}=\begin{bmatrix}-0.0312\\ 0.0384\\ 0.0688\end{bmatrix}. |  |

These values are used as the initial condition for simulating the evolution of the yield curve factors over time.

## Appendix D Swaption Pricing Network

There is no closed-form solution for the swaption price provided by Equation ([7](https://arxiv.org/html/2512.06639v1#S2.E7 "In Swaption Pricing. ‣ 2 Market Environment and Financial Instruments ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.")), and thus the swaption sensitivity ∂PSt−1∂Xt−1(k)\frac{\partial\mathrm{PS}\_{t-1}}{\partial X\_{t-1}^{(k)}} is not available in closed-form either. To calculate such quantity we adopt a hybrid method that combines Monte Carlo simulation with neural network approximation.

Our goal is to approximate the mapping from the factor values and time to maturity to the corresponding swaption price.
The approach proceeds as follows

1. 1.

   Simulate factor paths under the physical measure.
   We simulate NkN\_{k} sample paths of the factor process (Xt)t=0,1,…,Tβ(X\_{t})\_{t=0,1,\dots,T\_{\beta}} under the real-world (physical) measure ℙ\mathbb{P}. This results in an array of Nk×(Tβ+1)N\_{k}\times(T\_{\beta}+1) samples.
2. 2.

   Select NkN\_{k} samples for X0X\_{0}.
   From the simulated paths obtained in Step 1, we sample the NkN\_{k} initial values {(i)X0}i=1Nk\{\_{(i)}X\_{0}\}\_{i=1}^{N\_{k}} randomly.101010Any value with the paths, including non-initial values, can be selected. These represent diverse and realistic starting conditions for the term structure factors.
3. 3.

   Randomize swaption maturities.
   For each of the NkN\_{k} samples obtained from step 2, we generate an integer Tα(i)T\_{\alpha}^{(i)} uniformly at random from the set {1,2,…,Tα}\{1,2,\dots,T\_{\alpha}\}. This assigns a random maturity to each sample of the previous step, reflecting a distribution of swaptions across different maturities.
4. 4.

   Compute swaption prices using the forward measure.
   For each pair ((i)X0,Tα(i))(\_{(i)}X\_{0},T\_{\alpha}^{(i)}), we use the forward-measure swaption pricing formula from godin2023pricing:

   |  |  |  |
   | --- | --- | --- |
   |  | PS[0,𝒯(i),K,N]=𝔼ℚTα(i)[𝒫Tα(i)|ℱ0],PS\left[0,\mathcal{T}^{(i)},K,N\right]=\mathbb{E}^{\mathbb{Q}^{T\_{\alpha}^{(i)}}}\left[\mathcal{P}\_{T\_{\alpha}^{(i)}}\,\middle|\,\mathcal{F}\_{0}\right], |  |

   where 𝒫Tα(i)\mathcal{P}\_{T\_{\alpha}^{(i)}} denotes the discounted swap payoff at maturity Tα(i)T\_{\alpha}^{(i)}, and 𝒯(i)\mathcal{T}^{(i)} is the associated tenor structure. The expectation is evaluated using Monte Carlo simulation under the corresponding Tα(i)T\_{\alpha}^{(i)}-forward measure.

This process yields a training dataset consisting of input-output pairs {((i)X0,Tα(i)),PS(i)}\{(\_{(i)}X\_{0},T\_{\alpha}^{(i)}),PS^{(i)}\}, which is then used to train a neural network that approximates the pricing function, as described in Section [D.1](https://arxiv.org/html/2512.06639v1#A4.SS1 "D.1 Kolmogorov–Arnold Networks ‣ Appendix D Swaption Pricing Network ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare."), and its sensitivities for out-of-sample prediction. For the sensitivities, a finite difference approach is considered.

In summary, the objective is to learn a smooth approximation of the pricing function, thereby enabling fast and accurate generalization for out-of-sample factor inputs during hedging and simulation. This model is then used to evaluate swaption prices and sensitivities in real-time, significantly reducing computational overhead while preserving accuracy.

The type of neural network considered is a fully connected Kolmogorov–Arnold neural network (KAN). The structure of such network is discussed next.

### D.1 Kolmogorov–Arnold Networks

Kolmogorov–Arnold Networks (KANs) are a recent neural architecture first introduced in liu2024kan and inspired by the Kolmogorov–Arnold representation theorem, which asserts that any multivariate continuous function can be written as a finite sum of compositions of univariate continuous functions.

KANs provide a more interpretable alternative to standard FCNNs.
While traditional FCNNs apply fixed linear transformations followed by nonlinear activation functions (such as ReLU or Sigmoid), KANs take a different approach: they apply learnable univariate functions directly to each input coordinate and then combine the results linearly. This design allows KANs to adaptively learn nonlinear transformations on a per-dimension basis, making them highly expressive and naturally suited for capturing structured dependencies.

In this work, we use a KAN to approximate the swaption pricing function. Each univariate function is parameterized as a linear combination of Radial Basis Functions (RBFs), following the FastKAN framework proposed in li2024kolmogorovarnold. These Gaussian RBFs are centered along the input axis, allowing the network to capture local patterns in the data with smooth transitions.
This architecture enhances both flexibility and interpretability.

The structure of the KAN model used in this study is summarized as follows:

* •

  Each input pair (Xτ,τ)(X\_{\tau},\tau), consisting of the yield curve factors at time τ∈{0,1,…,Tα}\tau\in\{0,1,\dots,T\_{\alpha}\} and the time-to-maturity, passes through a learnable univariate function composed of RBF kernels.
* •

  The outputs of these functions are then linearly combined to produce the network output, which represents the swaption price under predefined parameters.
* •

  Several such layers are stacked to form a deep KAN model, optionally including residual connections or normalization layers to improve training dynamics.

This structure provides the agent with a faster, more accurate, and interpretable approximation of swaption prices, which is particularly advantageous in settings where no closed-form pricing formula is available. For a detailed comparison highlighting why KAN are preferable to standard FCNN architectures in our setting, see Section [D.2](https://arxiv.org/html/2512.06639v1#A4.SS2 "D.2 KAN vs. FCNN Performance Comparison ‣ Appendix D Swaption Pricing Network ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.").

#### Pricing Network Architecture.

To approximate the swaption pricing function, we employ a three-layer Kolmogorov–Arnold Network (KAN) with layer widths of 8, 16, and 8, respectively. The model takes as input four features: the three term structure factors generated by the DTAFNS model and the time-to-maturity, expressed in years. The network outputs a single scalar corresponding to the price of a payer swaption.

Training data is generated using Monte Carlo simulations, with data for each swaption of maturity Tα(i)T^{(i)}\_{\alpha} being generated under the Tα(i)T^{(i)}\_{\alpha}-forward risk-neutral measure, using Nk=20,000N\_{k}=20{,}000 sample paths.
However, each swaption in the dataset has the same tenor and strike, each corresponding to these of the swaption we want to price in subsequent simulation experiments. The network is trained for up to 5,000 epochs using the Adam optimizer with a learning rate of 0.001, minimizing the smooth L1 loss (Huber loss) between predicted and simulated swaption prices.

Once trained, the pricing network is used to evaluate swaption prices and compute their gradients with respect to the input factors. We employ the central difference method to compute the gradient, as it exhibits greater stability and accuracy compared to the neural network’s gradient obtained through automatic differentiation. The computed sensitivities are then used to determine the hedge ratios in the benchmark rho-hedging strategies.

### D.2 KAN vs. FCNN Performance Comparison

This section presents a comparative analysis of the Kolmogorov–Arnold Network (KAN) and a standard FCNN for approximating swaption prices. While the KAN architecture consists of 3 layers with widths [8,16,8][8,16,8], the FCNN model employs a deeper and wider architecture with 4 layers of respective widths [512,1024,1024,512][512,1024,1024,512]. Despite its significantly smaller size, the KAN demonstrates superior performance. Indeed, Figure [4](https://arxiv.org/html/2512.06639v1#A4.F4 "Figure 4 ‣ D.2 KAN vs. FCNN Performance Comparison ‣ Appendix D Swaption Pricing Network ‣ Learning to Hedge SwaptionsGodin is funded by NSERC (RGPIN-2024-04593). The authors report there are no competing interests to declare.") illustrates the in-sample (IS) and out-of-sample (OOS) performance trajectories of both models over 1000 training epochs.

![Refer to caption](x19.png)


Figure 4: In-sample (left) and out-of-sample (right) performance of KAN and FCNN across 1000 training epochs.

The KAN consistently outperforms the FCNN across multiple quantitative metrics. In the in-sample setting, the KAN exhibits a smooth and stable convergence trajectory with minimal variance. In contrast, the FCNN displays several sharp fluctuations, notably around epochs 150 and 500, indicating optimization instability and sensitivity to local minima.
Out-of-sample performance further highlights the KAN’s superiority in terms of generalization. The mean OOS error over the 1000 epochs for the KAN is 1.73×10−61.73\times 10^{-6}.
It is substantially lower than that of the FCNN, which is 4.71×10−64.71\times 10^{-6}. Additionally, the KAN achieves a significantly smaller generalization gap and reaches stable performance approximately 250 epochs earlier than FCNN (309 vs. 562 epochs). The final OOS error for the KAN remains in the order of 10−910^{-9}, an order of magnitude lower than that of the FCNN.
Overall, the KAN achieves:

* •

  Lower mean and final IS and OOS errors,
* •

  Smaller standard deviations, indicating greater robustness,
* •

  Faster convergence to a stable solution,
* •

  A tighter generalization gap, confirming enhanced predictive performance.

These findings support the conclusion that the KAN offers a faster, more stable, accurate, and generalizable architecture for swaption price approximation compared to conventional feedforward networks, even when using significantly fewer parameters.