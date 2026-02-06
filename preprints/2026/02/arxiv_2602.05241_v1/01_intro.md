---
authors:
- Masaaki Fukasawa
doc_id: arxiv:2602.05241v1
family_id: arxiv:2602.05241
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: On the Skew Stickiness Ratio
url_abs: http://arxiv.org/abs/2602.05241v1
url_html: https://arxiv.org/html/2602.05241v1
venue: arXiv q-fin
version: 1
year: 2026
---


Masaaki Fukasawa
  
The University of Osaka
  
560-8531 Japan

###### Abstract

The skew stickiness ratio is a statistic that captures the joint dynamics of an asset price and its volatility. We derive a representation formula for this quantity using the Itô–Wentzell and Clark–Ocone formulae, and we apply it to analyze its asymptotics under Bergomi‑type stochastic volatility models.

## 1 Introduction

The Skew Stickiness Ratio (SSR), introduced by Bergomi [[2](https://arxiv.org/html/2602.05241v1#bib.bib2)], serves as a quantitative measure of how different models generate distinct implied volatility dynamics. Conventional stochastic volatility models yield SSR values that diverge from empirical observations. Since SSR captures the cross gamma risk associated with stochastic volatility, employing a model that aligns with market-consistent SSR values is crucial for effective derivative hedging.

Let S={St}S=\{S\_{t}\} be an asset price process satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt=Vt​d​Bt\frac{\mathrm{d}S\_{t}}{S\_{t}}=\sqrt{V\_{t}}\mathrm{d}B\_{t} |  | (1) |

for a positive continuous adapted process V={Vt}V=\{V\_{t}\},
where B={Bt}B=\{B\_{t}\} is a standard Brownian motion on a filtered probability space
(Ω,ℱ,𝖯,{ℱt})(\Omega,\mathscr{F},\mathsf{P},\{\mathscr{F}\_{t}\}).
For a fixed maturity T>0T>0, a strike price K>0K>0,
the put option price process P​(K)={Pt​(K)}P(K)=\{P\_{t}(K)\} and
the implied total variance process Σ​(K)={Σt​(K)}\Sigma(K)=\{\Sigma\_{t}(K)\} are defined through

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pt​(K)=𝖤​[(K−ST)+|ℱt]=pK​(St,Σt​(K)),P\_{t}(K)=\mathsf{E}[(K-S\_{T})\_{+}|\mathscr{F}\_{t}]=p\_{K}(S\_{t},\Sigma\_{t}(K)), |  | (2) |

where
pKp\_{K} is the Black-Scholes put option price given by

|  |  |  |
| --- | --- | --- |
|  | pK​(s,t)=K​Φ​(−d−)−s​Φ​(−d+),d±=d±​(s,t)=log⁡sK±12​tt.p\_{K}(s,t)=K\Phi(-d\_{-})-s\Phi(-d\_{+}),\ \ d\_{\pm}=d\_{\pm}(s,t)=\frac{\log\frac{s}{K}\pm\frac{1}{2}t}{\sqrt{t}}. |  |

We assume that P​(K)P(K) is a continuous martingale for each K>0K>0 and that
Pt​(K)P\_{t}(K) is twice continuously differentiable in KK for each t<Tt<T.
The implied volatility σ​(K)={σt​(K)}\sigma(K)=\{\sigma\_{t}(K)\},
the at-the-money volatility
σS={σtS}\sigma^{S}=\{\sigma^{S}\_{t}\},
the at-the-money skew
σ′={σt′}\sigma^{\prime}=\{\sigma^{\prime}\_{t}\}, and then the SSR process R={Rt}R=\{R\_{t}\} are defined through

|  |  |  |
| --- | --- | --- |
|  | σt​(K)=Σt​(K)T−t,σtS=σt​(St),σt′=dd​k|k=0​σt​(St​ek),Rt=1σt′​d​⟨σS,log⁡S⟩td​⟨log⁡S⟩t\sigma\_{t}(K)=\sqrt{\frac{\Sigma\_{t}(K)}{T-t}},\ \ \sigma^{S}\_{t}=\sigma\_{t}(S\_{t}),\ \ \sigma^{\prime}\_{t}=\frac{\mathrm{d}}{\mathrm{d}k}\Big|\_{k=0}\sigma\_{t}(S\_{t}e^{k}),\ \ R\_{t}=\frac{1}{\sigma^{\prime}\_{t}}\frac{\mathrm{d}\langle\sigma^{S},\log S\rangle\_{t}}{\mathrm{d}\langle\log S\rangle\_{t}} |  |

respectively. Here and hereafter,
we assume that σ′\sigma^{\prime} is nonzero.

The empirical version of SSR is computed as the regression coefficient of the increments of the market-implied at-the-money volatility with respect to the underlying log returns, normalized by the market-implied at-the-money skew.
According to Bergomi [[2](https://arxiv.org/html/2602.05241v1#bib.bib2)], the empirical SSR process takes values around 3/23/2 for time-to-maturities T−tT-t ranging from a month to a few years in index option markets.

While the at-the-money volatility is observable in markets and so the empirical SSR is a convenient statistic, the covariation ⟨σS,log⁡S⟩\langle\sigma^{S},\log S\rangle under a given model has not been rigorously computed in the literature.
In fact, Bergomi [[2](https://arxiv.org/html/2602.05241v1#bib.bib2)] and Bourgey et al. [[3](https://arxiv.org/html/2602.05241v1#bib.bib3)] have approximated RR by formally replacing σS\sigma^{S} by the square root of the averaged forward variance

|  |  |  |
| --- | --- | --- |
|  | σtV=1T−t​∫tTVt​(s)​ds,Vt​(s)=𝖤​[Vs|ℱt]\sigma^{V}\_{t}=\sqrt{\frac{1}{T-t}\int\_{t}^{T}V\_{t}(s)\mathrm{d}s},\ \ V\_{t}(s)=\mathsf{E}[V\_{s}|\mathscr{F}\_{t}] |  |

without any rigorous estimate of the approximation error.
Friz and Gatheral [[5](https://arxiv.org/html/2602.05241v1#bib.bib5)] and Bourgey et al. [[4](https://arxiv.org/html/2602.05241v1#bib.bib4)] have treated directly
⟨σS,log⁡S⟩\langle\sigma^{S},\log S\rangle while relying on a formal application of Itô’s formula with a functional derivative

|  |  |  |
| --- | --- | --- |
|  | d​⟨σS,log⁡S⟩td​⟨log⁡S⟩t=∫tTdu​δ​σSδ​Vt​(u)​d​⟨V​(u),log⁡S⟩td​⟨log⁡S⟩t\frac{\mathrm{d}\langle\sigma^{S},\log S\rangle\_{t}}{\mathrm{d}\langle\log S\rangle\_{t}}=\int\_{t}^{T}\mathrm{d}u\frac{\delta\sigma^{S}}{\delta V\_{t}(u)}\frac{\mathrm{d}\langle V(u),\log S\rangle\_{t}}{\mathrm{d}\langle\log S\rangle\_{t}} |  |

for which a verification seems not trivial.

This paper aims at a rigorous treatment of SSR based on the Itô–Wentzell and Clark–Ocone formulae, and applying it to analyze its asymptotics under Bergomi‑type models.
In Section 2, we derive a representation formula of SSR in terms of the Malliavin-Shigekawa derivative.
In Section 3, we apply the formula to derive the short-maturity limit of SSR under the Bergomi-type models.
In Section 4, we analyze the small volatility-of-volatility asymptotics.

## 2 SSR formulae

By a simple computation, we have an alternative representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt=1Σt′​(St)​d​⟨ΣS,S⟩td​⟨S⟩t,ΣtS=Σt​(St),R\_{t}=\frac{1}{\Sigma^{\prime}\_{t}(S\_{t})}\frac{\mathrm{d}\langle\Sigma^{S},S\rangle\_{t}}{\mathrm{d}\langle S\rangle\_{t}},\ \ \Sigma^{S}\_{t}=\Sigma\_{t}(S\_{t}), |  | (3) |

which is more convenient in the following.
As is well-known, differentiating ([2](https://arxiv.org/html/2602.05241v1#S1.E2 "In 1 Introduction ‣ On the Skew Stickiness Ratio")) in KK,

|  |  |  |
| --- | --- | --- |
|  | 𝖯​[K>ST|ℱt]=Φ​(−d−​(St,Σt​(K)))+∂pK∂t​(St,Σt​(K))​Σt′​(K),\mathsf{P}[K>S\_{T}|\mathscr{F}\_{t}]=\Phi(-d\_{-}(S\_{t},\Sigma\_{t}(K)))+\frac{\partial p\_{K}}{\partial t}(S\_{t},\Sigma\_{t}(K))\Sigma^{\prime}\_{t}(K), |  |

which implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σt′​(St)=2​ΣtSSt​ϕ​(ΣtS2)​(𝖯​[St>ST|ℱt]−Φ​(ΣtS2))\Sigma^{\prime}\_{t}(S\_{t})=\frac{2\sqrt{\Sigma^{S}\_{t}}}{S\_{t}\phi\left(\frac{\sqrt{\Sigma^{S}\_{t}}}{2}\right)}\left(\mathsf{P}[S\_{t}>S\_{T}|\mathscr{F}\_{t}]-\Phi\left(\frac{\sqrt{\Sigma^{S}\_{t}}}{2}\right)\right) |  | (4) |

by noting

|  |  |  |
| --- | --- | --- |
|  | ∂pK∂t​(s,t)=s2​t​ϕ​(−d+​(s,t))=K2​t​ϕ​(−d−​(s,t)).\frac{\partial p\_{K}}{\partial t}(s,t)=\frac{s}{2\sqrt{t}}\phi(-d\_{+}(s,t))=\frac{K}{2\sqrt{t}}\phi(-d\_{-}(s,t)). |  |

To compute ⟨ΣS,S⟩\langle\Sigma^{S},S\rangle, here we apply the Itô-Wentzell formula:

###### Lemma 1

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt=1+1Σ′​(St)​d​⟨Σ​(K),S⟩td​⟨S⟩t|K=St.R\_{t}=1+\frac{1}{\Sigma^{\prime}(S\_{t})}\frac{\mathrm{d}\langle\Sigma(K),S\rangle\_{t}}{\mathrm{d}\langle S\rangle\_{t}}\Bigg|\_{K=S\_{t}}. |  | (5) |

Proof:
By a generalized Itô formula (a.k.a. the Itô-Wentzell formula, see e.g., Kunita [[8](https://arxiv.org/html/2602.05241v1#bib.bib8)]),

|  |  |  |
| --- | --- | --- |
|  | ΣtS=Σt​(St)=Σ0​(S0)+∫0tΣu′​(Su)​dSu+12​∫0tΣu′′​(Su)​d​⟨S⟩u+∫0tΣ​(Su,d​u)+⟨∫0⋅Σ′​(Su,d​u),S⟩t,\begin{split}\Sigma^{S}\_{t}=\Sigma\_{t}(S\_{t})=\Sigma\_{0}(S\_{0})&+\int\_{0}^{t}\Sigma\_{u}^{\prime}(S\_{u})\mathrm{d}S\_{u}+\frac{1}{2}\int\_{0}^{t}\Sigma\_{u}^{\prime\prime}(S\_{u})\mathrm{d}\langle S\rangle\_{u}\\ &+\int\_{0}^{t}\Sigma(S\_{u},\mathrm{d}u)+\left\langle\int\_{0}^{\cdot}\Sigma^{\prime}(S\_{u},\mathrm{d}u),S\right\rangle\_{t},\end{split} |  |

where the fourth term of the right hand side is a nonlinear stochastic integral satisfying

|  |  |  |
| --- | --- | --- |
|  | ⟨∫0⋅Σ​(Su,d​u),S⟩=∫0⋅d​⟨Σ​(K),S⟩td​⟨S⟩t|K=St​d​⟨S⟩t.\left\langle\int\_{0}^{\cdot}\Sigma(S\_{u},\mathrm{d}u),S\right\rangle=\int\_{0}^{\cdot}\frac{\mathrm{d}\langle\Sigma(K),S\rangle\_{t}}{\mathrm{d}\langle S\rangle\_{t}}\Bigg|\_{K=S\_{t}}\mathrm{d}\langle S\rangle\_{t}. |  |

This implies

|  |  |  |
| --- | --- | --- |
|  | d​⟨ΣS,S⟩t=Σt′​(St)​d​⟨S⟩t+d​⟨Σ​(K),S⟩t|K=St\mathrm{d}\langle\Sigma^{S},S\rangle\_{t}=\Sigma^{\prime}\_{t}(S\_{t})\mathrm{d}\langle S\rangle\_{t}+\mathrm{d}\langle\Sigma(K),S\rangle\_{t}|\_{K=S\_{t}} |  |

and then, the claimed formula ([5](https://arxiv.org/html/2602.05241v1#S2.E5 "In Lemma 1 ‣ 2 SSR formulae ‣ On the Skew Stickiness Ratio")) together with ([3](https://arxiv.org/html/2602.05241v1#S2.E3 "In 2 SSR formulae ‣ On the Skew Stickiness Ratio")). □\square

###### Theorem 1

If the filtration {ℱt}\{\mathscr{F}\_{t}\} is generated by an nn-dimensional standard Brownian motion (B1,…,Bn)(B^{1},\dots,B^{n}) with B1=BB^{1}=B and
log⁡ST∈𝔻1,2\log S\_{T}\in\mathbb{D}^{1,2},
then R=X/YR=X/Y, where

|  |  |  |
| --- | --- | --- |
|  | Xt=𝖤​[1{St>ST}​STSt​(1−𝒟t1​log⁡STVt)|ℱt],Yt=𝖯​[St>ST|ℱt]−Φ​(ΣtS2),\begin{split}&X\_{t}=\mathsf{E}\left[1\_{\{S\_{t}>S\_{T}\}}\frac{S\_{T}}{S\_{t}}\left(1-\frac{\mathcal{D}^{1}\_{t}\log S\_{T}}{\sqrt{V\_{t}}}\right)\Bigg|\mathscr{F}\_{t}\right],\\ &Y\_{t}=\mathsf{P}[S\_{t}>S\_{T}|\mathscr{F}\_{t}]-\Phi\left(\frac{\sqrt{\Sigma^{S}\_{t}}}{2}\right),\end{split} |  |

(𝒟1,…,𝒟n)(\mathcal{D}^{1},\dots,\mathcal{D}^{n}) is the Malliavin-Shigekawa derivative operator with respect to (B1,…,Bn)(B^{1},\dots,B^{n}), and
𝔻1,2\mathbb{D}^{1,2} is the (1,2)(1,2)-Sobolev space with
respect to (𝒟1,…,𝒟n)(\mathcal{D}^{1},\dots,\mathcal{D}^{n}).

Proof:
Applying Itô’s formula to ([2](https://arxiv.org/html/2602.05241v1#S1.E2 "In 1 Introduction ‣ On the Skew Stickiness Ratio")),

|  |  |  |
| --- | --- | --- |
|  | d​⟨P​(K),S⟩t=∂pK∂s​(St,Σt​(K))​d​⟨S⟩t+∂pK∂t​(St,Σt​(K))​d​⟨Σt​(K),S⟩t,\mathrm{d}\langle P(K),S\rangle\_{t}=\frac{\partial p\_{K}}{\partial s}(S\_{t},\Sigma\_{t}(K))\mathrm{d}\langle S\rangle\_{t}+\frac{\partial p\_{K}}{\partial t}(S\_{t},\Sigma\_{t}(K))\mathrm{d}\langle\Sigma\_{t}(K),S\rangle\_{t}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | ∂pK∂s​(s,t)=−Φ​(−d+).\frac{\partial p\_{K}}{\partial s}(s,t)=-\Phi(-d\_{+}). |  |

This implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​⟨Σ​(K),S⟩td​⟨S⟩t|K=St=2​ΣtSSt​ϕ​(ΣtS2)​(d​⟨P​(K),S⟩td​⟨S⟩t|K=St+Φ​(−ΣtS2)).\frac{\mathrm{d}\langle\Sigma(K),S\rangle\_{t}}{\mathrm{d}\langle S\rangle\_{t}}\Bigg|\_{K=S\_{t}}=\frac{2\sqrt{\Sigma^{S}\_{t}}}{S\_{t}\phi\left(\frac{\sqrt{\Sigma^{S}\_{t}}}{2}\right)}\left(\frac{\mathrm{d}\langle P(K),S\rangle\_{t}}{\mathrm{d}\langle S\rangle\_{t}}\Bigg|\_{K=S\_{t}}+\Phi\left(-\frac{\sqrt{\Sigma^{S}\_{t}}}{2}\right)\right). |  | (6) |

Combining ([4](https://arxiv.org/html/2602.05241v1#S2.E4 "In 2 SSR formulae ‣ On the Skew Stickiness Ratio")), ([5](https://arxiv.org/html/2602.05241v1#S2.E5 "In Lemma 1 ‣ 2 SSR formulae ‣ On the Skew Stickiness Ratio")) and ([6](https://arxiv.org/html/2602.05241v1#S2.E6 "In 2 SSR formulae ‣ On the Skew Stickiness Ratio")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt=1+1Yt​(d​⟨P​(K),S⟩td​⟨S⟩t|K=St+Φ​(−ΣtS2)).R\_{t}=1+\frac{1}{Y\_{t}}\left(\frac{\mathrm{d}\langle P(K),S\rangle\_{t}}{\mathrm{d}\langle S\rangle\_{t}}|\_{K=S\_{t}}+\Phi\left(-\frac{\sqrt{\Sigma^{S}\_{t}}}{2}\right)\right). |  | (7) |

By the Clark-Ocone formula (see, e.g., [[9](https://arxiv.org/html/2602.05241v1#bib.bib9)]),

|  |  |  |
| --- | --- | --- |
|  | PT​(K)=(K−ST)+=𝖤​[(K−ST)+]+∫0T𝖤​[𝒟t1​(K−ST)+|ℱt]​dBt+MT⟂=𝖤​[(K−ST)+]−∫0T𝖤​[1{K>ST}​ST​𝒟t1​log⁡ST|ℱt]​dBt+MT⟂,\begin{split}P\_{T}(K)&=(K-S\_{T})\_{+}\\ &=\mathsf{E}[(K-S\_{T})\_{+}]+\int\_{0}^{T}\mathsf{E}[\mathcal{D}^{1}\_{t}(K-S\_{T})\_{+}|\mathscr{F}\_{t}]\mathrm{d}B\_{t}+M^{\perp}\_{T}\\ &=\mathsf{E}[(K-S\_{T})\_{+}]-\int\_{0}^{T}\mathsf{E}[1\_{\{K>S\_{T}\}}S\_{T}\mathcal{D}^{1}\_{t}\log S\_{T}|\mathscr{F}\_{t}]\mathrm{d}B\_{t}+M^{\perp}\_{T},\end{split} |  |

where
M⟂M^{\perp} is a martingale orthogonal to BB.
See Exercise 3.3 of [[9](https://arxiv.org/html/2602.05241v1#bib.bib9)] for a generalized chain rule used here.
Therefore,

|  |  |  |
| --- | --- | --- |
|  | d​⟨P​(K),S⟩t=−𝖤​[1{K>ST}​ST​𝒟t1​log⁡ST|ℱt]St​Vt​d​⟨S⟩t.\mathrm{d}\langle P(K),S\rangle\_{t}=-\frac{\mathsf{E}[1\_{\{K>S\_{T}\}}S\_{T}\mathcal{D}^{1}\_{t}\log S\_{T}|\mathscr{F}\_{t}]}{S\_{t}\sqrt{V\_{t}}}\mathrm{d}\langle S\rangle\_{t}. |  |

Notice that

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[1{K>ST}​ST|ℱt]=K​𝖯​[K>ST|ℱt]−𝖤​[(K−ST)+|ℱt]\mathsf{E}[1\_{\{K>S\_{T}\}}S\_{T}|\mathscr{F}\_{t}]=K\mathsf{P}[K>S\_{T}|\mathscr{F}\_{t}]-\mathsf{E}[(K-S\_{T})\_{+}|\mathscr{F}\_{t}] |  |

and so

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[1{St>ST}​ST|ℱt]St=𝖯​[St>ST|ℱt]−Pt​(St)St=𝖯​[St>ST|ℱt]−Φ​(ΣtS2)+Φ​(−ΣtS2).\begin{split}\frac{\mathsf{E}[1\_{\{S\_{t}>S\_{T}\}}S\_{T}|\mathscr{F}\_{t}]}{S\_{t}}&=\mathsf{P}[S\_{t}>S\_{T}|\mathscr{F}\_{t}]-\frac{P\_{t}(S\_{t})}{S\_{t}}\\ &=\mathsf{P}[S\_{t}>S\_{T}|\mathscr{F}\_{t}]-\Phi\left(\frac{\sqrt{\Sigma^{S}\_{t}}}{2}\right)+\Phi\left(-\frac{\sqrt{\Sigma^{S}\_{t}}}{2}\right).\end{split} |  |

Combining this with ([7](https://arxiv.org/html/2602.05241v1#S2.E7 "In 2 SSR formulae ‣ On the Skew Stickiness Ratio")), we obtain the claimed formula. □\square

###### Theorem 2

Assume a Bergomi-type model for Vt​(s)=𝖤​[Vs|ℱt]V\_{t}(s)=\mathsf{E}[V\_{s}|\mathscr{F}\_{t}]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vt​(s)=Vt​(s)​∑i=1dki​(s−t)​d​Wti,t<s,\mathrm{d}V\_{t}(s)=V\_{t}(s)\sum\_{i=1}^{d}k\_{i}(s-t)\mathrm{d}W^{i}\_{t},\ \ t<s, |  | (8) |

where
(W1,…,Wd)(W^{1},\dots,W^{d}) is a dd-dimensional standard Brownian motion correlated with BB in ([1](https://arxiv.org/html/2602.05241v1#S1.E1 "In 1 Introduction ‣ On the Skew Stickiness Ratio")) as

|  |  |  |
| --- | --- | --- |
|  | d​⟨B,Wi⟩t=ρi​d​t,ρ:=∑i=1dρi2∈(0,1),\mathrm{d}\langle B,W^{i}\rangle\_{t}=\rho\_{i}\mathrm{d}t,\ \ \rho:=\sqrt{\sum\_{i=1}^{d}\rho\_{i}^{2}}\in(0,1), |  |

kik\_{i}, i=1,…,di=1,\dots,d, are locally square integrable functions on [0,∞)[0,\infty), and
t↦V0​(t)t\mapsto V\_{0}(t) is a deterministic positive continuous function.
The conditions of Theorem [1](https://arxiv.org/html/2602.05241v1#Thmthm1 "Theorem 1 ‣ 2 SSR formulae ‣ On the Skew Stickiness Ratio") are satisfied and

|  |  |  |
| --- | --- | --- |
|  | Xt=−12​St​Vt​𝖤​[1{St>ST}​ST​∫tTVs​k​(s−t)​(d​Bs−Vs​d​s)|ℱt],X\_{t}=-\frac{1}{2S\_{t}\sqrt{V\_{t}}}\mathsf{E}\left[1\_{\{S\_{t}>S\_{T}\}}S\_{T}\int\_{t}^{T}\sqrt{V\_{s}}k(s-t)\left(\mathrm{d}B\_{s}-\sqrt{V\_{s}}\,\mathrm{d}s\right)\Bigg|\mathscr{F}\_{t}\right], |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | k=∑i=1dρi​ki.k=\sum\_{i=1}^{d}\rho\_{i}k\_{i}. |  | (9) |

Proof: First, we note that the system ([8](https://arxiv.org/html/2602.05241v1#S2.E8 "In Theorem 2 ‣ 2 SSR formulae ‣ On the Skew Stickiness Ratio")) is solved as

|  |  |  |
| --- | --- | --- |
|  | ST=St​exp⁡{∫tTVs​dBs−12​∫tTVs​ds},Vs=V0​(s)​exp⁡{∑i=1d∫0ski​(s−u)​dWui−12​∑i=1d∫0ski​(s−u)2​du}.\begin{split}S\_{T}&=S\_{t}\exp\left\{\int\_{t}^{T}\sqrt{V\_{s}}\mathrm{d}B\_{s}-\frac{1}{2}\int\_{t}^{T}V\_{s}\mathrm{d}s\right\},\\ V\_{s}&=V\_{0}(s)\exp\left\{\sum\_{i=1}^{d}\int\_{0}^{s}k\_{i}(s-u)\mathrm{d}W^{i}\_{u}-\frac{1}{2}\sum\_{i=1}^{d}\int\_{0}^{s}k\_{i}(s-u)^{2}\mathrm{d}u\right\}.\end{split} |  |

Second, Id−(ρ1,…,ρd)​(ρ1,…,ρd)⊤I\_{d}-(\rho\_{1},\dots,\rho\_{d})(\rho\_{1},\dots,\rho\_{d})^{\top} has the eigenvalues 11 and 1−ρ21-\rho^{2}, and so is regular, with
the symmetric Cholesky factor

|  |  |  |
| --- | --- | --- |
|  | Id−(ρ1,…,ρd)​(ρ1,…,ρd)⊤=L​L⊤,L=Id−β​(ρ1,…,ρd)​(ρ1,…,ρd)⊤,I\_{d}-(\rho\_{1},\dots,\rho\_{d})(\rho\_{1},\dots,\rho\_{d})^{\top}=LL^{\top},\ \ L=I\_{d}-\beta(\rho\_{1},\dots,\rho\_{d})(\rho\_{1},\dots,\rho\_{d})^{\top}, |  |

where β=(1−1−ρ2)/ρ2\beta=(1-\sqrt{1-\rho^{2}})/\rho^{2}. This implies that (B1,…,Bd+1)(B^{1},\dots,B^{d+1}) defined by
B1=BB^{1}=B and

|  |  |  |
| --- | --- | --- |
|  | [B2⋮Bd+1]=L−1​[W1−ρ1​B⋮Wd−ρd​B]\begin{bmatrix}B\_{2}\\ \vdots\\ B\_{d+1}\end{bmatrix}=L^{-1}\begin{bmatrix}W^{1}-\rho\_{1}B\\ \vdots\\ W^{d}-\rho\_{d}B\end{bmatrix} |  |

is a d+1d+1-dimensional standard Brownian motion such that

|  |  |  |
| --- | --- | --- |
|  | [W1⋮Wd]=[ρ1​B⋮ρd​B]+L​[B2⋮Bd+1].\begin{bmatrix}W^{1}\\ \vdots\\ W^{d}\end{bmatrix}=\begin{bmatrix}\rho\_{1}B\\ \vdots\\ \rho\_{d}B\end{bmatrix}+L\begin{bmatrix}B\_{2}\\ \vdots\\ B\_{d+1}\end{bmatrix}. |  |

Therefore, the model can be formulated in the framework of Theorem [1](https://arxiv.org/html/2602.05241v1#Thmthm1 "Theorem 1 ‣ 2 SSR formulae ‣ On the Skew Stickiness Ratio"), with

|  |  |  |
| --- | --- | --- |
|  | 𝒟t1​Vs=Vs2​∑i=1dρi​ki​(s−t),𝒟t1​Vs=Vs​∑i=1dρi​ki​(s−t)\mathcal{D}^{1}\_{t}\sqrt{V\_{s}}=\frac{\sqrt{V\_{s}}}{2}\sum\_{i=1}^{d}\rho\_{i}k\_{i}(s-t),\ \ \mathcal{D}^{1}\_{t}V\_{s}=V\_{s}\sum\_{i=1}^{d}\rho\_{i}k\_{i}(s-t) |  |

for s>ts>t. Since these are progressively measurable,

|  |  |  |
| --- | --- | --- |
|  | 𝒟t1​log⁡ST=Vt+∫tT𝒟t1​Vs​dBs−12​∫tT𝒟t1​Vs​ds=Vt+12​(∫tTVs​k​(s−t)​dBs−∫tTVs​k​(s−t)​ds)\begin{split}\mathcal{D}^{1}\_{t}\log S\_{T}&=\sqrt{V\_{t}}+\int\_{t}^{T}\mathcal{D}^{1}\_{t}\sqrt{V\_{s}}\mathrm{d}B\_{s}-\frac{1}{2}\int\_{t}^{T}\mathcal{D}^{1}\_{t}V\_{s}\mathrm{d}s\\ &=\sqrt{V\_{t}}+\frac{1}{2}\left(\int\_{t}^{T}\sqrt{V\_{s}}k(s-t)\mathrm{d}B\_{s}-\int\_{t}^{T}V\_{s}k(s-t)\mathrm{d}s\right)\end{split} |  |

by the standard computation. The rest would be clear.
□\square

###### Remark 1

The case d=2d=2 with kik\_{i} being exponential functions
ki​(t)=ai​e−bi​tk\_{i}(t)=a\_{i}e^{-b\_{i}t}, ai,bi>0a\_{i},b\_{i}>0 in ([8](https://arxiv.org/html/2602.05241v1#S2.E8 "In Theorem 2 ‣ 2 SSR formulae ‣ On the Skew Stickiness Ratio")),
describes the two factor Bergomi model (see Bergomi [[2](https://arxiv.org/html/2602.05241v1#bib.bib2)]).
The case d=1d=1 with k1​(t)=a​tH−1/2k\_{1}(t)=at^{H-1/2}, a>0a>0, H∈(0,1/2)H\in(0,1/2), describes the rough Bergomi model (see [[1](https://arxiv.org/html/2602.05241v1#bib.bib1)]).

## 3 Short-maturity asymptotics

In this section, we assume the Bergomi-type model ([8](https://arxiv.org/html/2602.05241v1#S2.E8 "In Theorem 2 ‣ 2 SSR formulae ‣ On the Skew Stickiness Ratio")) and the conditions for Theorem [2](https://arxiv.org/html/2602.05241v1#Thmthm2 "Theorem 2 ‣ 2 SSR formulae ‣ On the Skew Stickiness Ratio") to hold.
We derive the limit of RtR\_{t} as T→tT\to t.

Since the model is based on Brownian motions we can assume that the filtration {ℱt}\{\mathscr{F}\_{t}\} is generated by them.
Then, there exists a regular conditional probability measure 𝖯t\mathsf{P}\_{t} given ℱt\mathscr{F}\_{t}.
Let 𝖤t\mathsf{E}\_{t} denote the expectation under 𝖯t\mathsf{P}\_{t} and define

|  |  |  |
| --- | --- | --- |
|  | Xt​(T)=−12​St​Vt​𝖤t​[1{St>ST}​ST​∫tTVs​k​(s−t)​(d​Bs−Vs​d​s)],Yt​(T)=𝖯t​[St>ST]−Φ​(ΣtS​(T)2),\begin{split}X\_{t}(T)&=-\frac{1}{2S\_{t}\sqrt{V\_{t}}}\mathsf{E}\_{t}\left[1\_{\{S\_{t}>S\_{T}\}}S\_{T}\int\_{t}^{T}\sqrt{V\_{s}}k(s-t)\left(\mathrm{d}B\_{s}-\sqrt{V\_{s}}\,\mathrm{d}s\right)\right],\\ Y\_{t}(T)&=\mathsf{P}\_{t}[S\_{t}>S\_{T}]-\Phi\left(\frac{\sqrt{\Sigma^{S}\_{t}(T)}}{2}\right),\end{split} |  |

where ΣtS​(T)\Sigma\_{t}^{S}(T) is defined through

|  |  |  |
| --- | --- | --- |
|  | 𝖤t​[(St−ST)+]=pK​(St,ΣtS​(T)).\mathsf{E}\_{t}[(S\_{t}-S\_{T})\_{+}]=p\_{K}(S\_{t},\Sigma^{S}\_{t}(T)). |  |

By Theorem [2](https://arxiv.org/html/2602.05241v1#Thmthm2 "Theorem 2 ‣ 2 SSR formulae ‣ On the Skew Stickiness Ratio"), RR coincides with R​(T):=X​(T)/Y​(T)R(T):=X(T)/Y(T) almost everywhere with respect to d​𝖯⊗d​t\mathrm{d}\mathsf{P}\otimes\mathrm{d}t.

###### Theorem 3

Let kk defined by ([9](https://arxiv.org/html/2602.05241v1#S2.E9 "In Theorem 2 ‣ 2 SSR formulae ‣ On the Skew Stickiness Ratio")). If
there exists H∈(0,1/2]H\in(0,1/2] such that the map

|  |  |  |
| --- | --- | --- |
|  | u↦g​(u):=u1/2−H​k​(u)u\mapsto g(u):=u^{1/2-H}k(u) |  |

is continuous on (0,∞)(0,\infty) with finite limit g​(0+)>0g(0+)>0, then,

|  |  |  |
| --- | --- | --- |
|  | limT→tRt​(T)=H+32.\lim\_{T\to t}R\_{t}(T)=H+\frac{3}{2}. |  |

Proof:
The regular conditional distribution of

|  |  |  |
| --- | --- | --- |
|  | 1Vt​((T−t)−1/2​log⁡STSt,(T−t)−H​∫tTVs​k​(s−t)​(d​Bs−Vs​d​s))\frac{1}{\sqrt{V\_{t}}}\left((T-t)^{-1/2}\log\frac{S\_{T}}{S\_{t}},\,(T-t)^{-H}\int\_{t}^{T}\sqrt{V\_{s}}k(s-t)\left(\mathrm{d}B\_{s}-\sqrt{V\_{s}}\mathrm{d}s\right)\right) |  |

given ℱt\mathscr{F}\_{t} is uniformly integrable and by the martingale central limit theorem,
it converges in law
to a centered normal random variable (Z1,Z2)(Z\_{1},Z\_{2}) with covariance

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[Z12]=1,𝖤​[Z1​Z2]=2​g​(0+)2​H+1,𝖤​[Z22]=g​(0+)22​H.\mathsf{E}[Z\_{1}^{2}]=1,\ \ \mathsf{E}[Z\_{1}Z\_{2}]=\frac{2g(0+)}{2H+1},\ \ \mathsf{E}[Z\_{2}^{2}]=\frac{g(0+)^{2}}{2H}. |  |

Since 𝖤​[Z2|Z1=z]=𝖤​[Z1​Z2]​z\mathsf{E}[Z\_{2}|Z\_{1}=z]=\mathsf{E}[Z\_{1}Z\_{2}]z, we have then

|  |  |  |
| --- | --- | --- |
|  | (T−t)−H​Xt​(T)→−12​∫−∞0𝖤​[Z2|Z1=z]​ϕ​(z)​dz=g​(0+)2​H+1​ϕ​(0).(T-t)^{-H}X\_{t}(T)\to-\frac{1}{2}\int\_{-\infty}^{0}\mathsf{E}[Z\_{2}|Z\_{1}=z]\phi(z)\mathrm{d}z=\frac{g(0+)}{2H+1}\phi(0). |  |

On the other hand, by Theorem 2 of [[6](https://arxiv.org/html/2602.05241v1#bib.bib6)] (more precisely, by the proof of it), we know that

|  |  |  |
| --- | --- | --- |
|  | (T−t)−H​Yt​(T)→g​(0+)2​(H+1/2)​(H+3/2)​ϕ​(0),(T-t)^{-H}Y\_{t}(T)\to\frac{g(0+)}{2(H+1/2)(H+3/2)}\phi(0), |  |

which concludes the proof. □\square

## 4 Small volatility-of-volatility asymptotics

Here we introduce a small volatility-of-volatility parameter ϵ>0\epsilon>0
by replacing kik\_{i} by ϵ​ki\epsilon k\_{i} in ([8](https://arxiv.org/html/2602.05241v1#S2.E8 "In Theorem 2 ‣ 2 SSR formulae ‣ On the Skew Stickiness Ratio")).
We have then

|  |  |  |
| --- | --- | --- |
|  | St=Stϵ:=S0​exp⁡{∫0tVsϵ​dBs−12​∫0tVsϵ​ds},Vt=Vtϵ:=V0​(t)​exp⁡{ϵ​∑i=1d∫0tki​(t−s)​dWsi−ϵ22​∑i=1d∫0tki​(t−s)2​ds}.\begin{split}S\_{t}&=S^{\epsilon}\_{t}:=S\_{0}\exp\left\{\int\_{0}^{t}\sqrt{V^{\epsilon}\_{s}}\mathrm{d}B\_{s}-\frac{1}{2}\int\_{0}^{t}V^{\epsilon}\_{s}\mathrm{d}s\right\},\\ V\_{t}&=V^{\epsilon}\_{t}:=V\_{0}(t)\exp\left\{\epsilon\sum\_{i=1}^{d}\int\_{0}^{t}k\_{i}(t-s)\mathrm{d}W^{i}\_{s}-\frac{\epsilon^{2}}{2}\sum\_{i=1}^{d}\int\_{0}^{t}k\_{i}(t-s)^{2}\mathrm{d}s\right\}.\end{split} |  |

Here we consider the limit of RtR\_{t} as ϵ→0\epsilon\to 0.
For simplicity, we let t=0t=0, and
assume ℱ0\mathscr{F}\_{0} is the trivial σ\sigma-field.
Let kk be defined by ([9](https://arxiv.org/html/2602.05241v1#S2.E9 "In Theorem 2 ‣ 2 SSR formulae ‣ On the Skew Stickiness Ratio")) and define

|  |  |  |
| --- | --- | --- |
|  | X​(ϵ)=−ϵ2​S0​V0​(0)​𝖤​[1{S0>ST}​ST​∫0TVs​k​(s)​(d​Bs−Vs​d​s)],Y​(ϵ)=𝖯​[S0>ST]−Φ​(Σ0S2),\begin{split}X(\epsilon)&=-\frac{\epsilon}{2S\_{0}\sqrt{V\_{0}(0)}}\mathsf{E}\left[1\_{\{S\_{0}>S\_{T}\}}S\_{T}\int\_{0}^{T}\sqrt{V\_{s}}k(s)\left(\mathrm{d}B\_{s}-\sqrt{V\_{s}}\,\mathrm{d}s\right)\right],\\ Y(\epsilon)&=\mathsf{P}[S\_{0}>S\_{T}]-\Phi\left(\frac{\sqrt{\Sigma^{S}\_{0}}}{2}\right),\end{split} |  |

and R​(ϵ)=X​(ϵ)/Y​(ϵ)R(\epsilon)=X(\epsilon)/Y(\epsilon) in light of Theorem [2](https://arxiv.org/html/2602.05241v1#Thmthm2 "Theorem 2 ‣ 2 SSR formulae ‣ On the Skew Stickiness Ratio").

###### Theorem 4

If kk is not identically zero,
then for any t<Tt<T,

|  |  |  |
| --- | --- | --- |
|  | limϵ→0R​(ϵ)=∫0TV0​(s)​ds​∫0TV0​(u)​k​(u)​duV0​(0)​∫0TV0​(s)​∫sTV0​(u)​k​(u−s)​du​ds.\lim\_{\epsilon\to 0}R(\epsilon)=\frac{\int\_{0}^{T}V\_{0}(s)\mathrm{d}s\int\_{0}^{T}V\_{0}(u)k(u)\mathrm{d}u}{\sqrt{V\_{0}(0)}\int\_{0}^{T}\sqrt{V\_{0}(s)}\int\_{s}^{T}V\_{0}(u)k(u-s)\mathrm{d}u\mathrm{d}s}. |  |

Proof:
The 22-dimensional random vector

|  |  |  |
| --- | --- | --- |
|  | (log⁡STϵS0,∫0TVsϵ​k​(s)​(d​Bs−Vsϵ​d​s))\left(\log\frac{S^{\epsilon}\_{T}}{S\_{0}},\,\int\_{0}^{T}\sqrt{V^{\epsilon}\_{s}}k(s)\left(\mathrm{d}B\_{s}-\sqrt{V^{\epsilon}\_{s}}\mathrm{d}s\right)\right) |  |

is uniformly integrable and by the martingale central limit theorem,
it converges in law to a 22-dimensional normal random vector (Z1,Z2)(Z\_{1},Z\_{2}) with mean vector, covariance matrix,

|  |  |  |
| --- | --- | --- |
|  | (−A2,−B),(ABBC)\left(-\frac{A}{2},-B\right),\ \ \ \begin{pmatrix}A&B\\ B&C\end{pmatrix} |  |

respectively, where

|  |  |  |
| --- | --- | --- |
|  | A=∫0TV0​(s)​ds,B=∫0TV0​(s)​k​(s)​ds,C=∫0TV0​(s)​k​(s)2​ds.A=\int\_{0}^{T}V\_{0}(s)\mathrm{d}s,\ \ B=\int\_{0}^{T}V\_{0}(s)k(s)\mathrm{d}s,\ \ C=\int\_{0}^{T}V\_{0}(s)k(s)^{2}\mathrm{d}s. |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | X​(ϵ)ϵ→12​V0​(0)​𝖤​[1{Z1<0}​eZ1​Z2]=B2​V0​(0)​A​ϕ​(−A2).\begin{split}\frac{X(\epsilon)}{\epsilon}\to\frac{1}{2\sqrt{V\_{0}(0)}}\mathsf{E}\left[1\_{\{Z\_{1}<0\}}e^{Z\_{1}}Z\_{2}\right]=\frac{B}{2\sqrt{V\_{0}(0)A}}\phi\left(-\frac{A}{2}\right).\end{split} |  |

On the other hand, from Section 3 of [[7](https://arxiv.org/html/2602.05241v1#bib.bib7)], we know that

|  |  |  |
| --- | --- | --- |
|  | Y​(ϵ)ϵ→12​A3/2​ϕ​(−A2)​∫0TV0​(s)​∫sTV0​(u)​k​(u−s)​du​ds,\frac{Y(\epsilon)}{\epsilon}\to\frac{1}{2A^{3/2}}\phi\left(-\frac{A}{2}\right)\int\_{0}^{T}\sqrt{V\_{0}(s)}\int\_{s}^{T}V\_{0}(u)k(u-s)\mathrm{d}u\mathrm{d}s, |  |

which yields the claim.
□\square

###### Remark 2

When the initial forward variance curve V0​(t)V\_{0}(t) is flat and k=a​tH−1/2k=at^{H-1/2}, then
the right hand side is H+3/2H+3/2, close to the empirical estimate 3/23/2 when H≈0H\approx 0.

## References

* [1]

  C. Bayer, P. K. Friz, M. Fukasawa, J. Gatheral, A. Jacquier, and M. Rosenbaum, Rough Volatility, SIAM, 2024.
* [2]
   L. Bergomi, Stochastic Volatility Modeling, CRC Press, 2016.
* [3]

  F. Bourgey, S. De Marco, and J. Delemotte, Smile Dynamics and Rough Volatility (July 30, 2024). Available at SSRN: https://ssrn.com/abstract=4911186
* [4]

  Bourgey, Florian and Delemotte, Jules and De Marco, Stefano, Refined Expansions of the Skew-Stickiness Ratio in Stochastic Volatility Models (August 11, 2025). Available at SSRN: https://ssrn.com/abstract=5387754 or http://dx.doi.org/10.2139/ssrn.5387754
* [5]

  P. K. Friz and J. Gatheral, Computing the SSR. Quantitative Finance, 25:5, 701-710, 2025.
* [6]

  M. Fukasawa, Wiener Spiral for Volatility Modeling,
  Theory of Probability & Its Applications 68 (2023), 481-500.
* [7]

  M. Fukasawa, Martingale expansion for stochastic volatility (2026), Available at
  arXiv:2601.09324.
* [8]
   H. Kunita, Stochastic flows and stochastic differential equations,
  Cambridge University Press, 1990.
* [9]

  D. Nualart and E. Nualart,
  Introduction to Malliavin Calculus,
  Cambridge University Press, 2018.