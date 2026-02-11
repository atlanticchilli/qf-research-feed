---
authors:
- Runyao Yu
- Derek W. Bunn
- Julia Lin
- Jochen Stiasny
- Fabian Leimgruber
- Tara Esterl
- Yuchen Tao
- Lianlian Qi
- Yujie Chen
- Wentao Wang
- Jochen L. Cremer
doc_id: arxiv:2602.10071v1
family_id: arxiv:2602.10071
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday,
  and Balancing Electricity Markets'
url_abs: http://arxiv.org/abs/2602.10071v1
url_html: https://arxiv.org/html/2602.10071v1
venue: arXiv q-fin
version: 1
year: 2026
---


Runyao Yu1,2, Derek W. Bunn3, Julia Lin2, Jochen Stiasny1, Fabian Leimgruber2, Tara Esterl2,
  
Yuchen Tao4, Lianlian Qi2,5, Yujie Chen6, Wentao Wang7, Jochen L. Cremer1,2
  
1Delft University of Technology, 2Austrian Institute of Technology, 3London Business School, 4RWTH Aachen
  
5Technical University of Munich, 6Chinese University of Hongkong, 7University of Technology Sydney

###### Abstract

Electricity price forecasting (EPF) plays a critical role in power system operation and market decision making. While existing review studies have provided valuable insights into forecasting horizons, market mechanisms, and evaluation practices, the rapid adoption of deep learning has introduced increasingly diverse model architectures, output structures, and training objectives that remain insufficiently analyzed in depth.
This paper presents a structured review of deep learning methods for EPF in day-ahead, intraday, and balancing markets. Specifically, We introduce a unified taxonomy that decomposes deep learning models into backbone, head, and loss components, providing a consistent evaluation perspective across studies. Using this framework, we analyze recent trends in deep learning components across markets. Our study highlights the shift toward probabilistic, microstructure-centric, and market-aware designs. We further identify key gaps in the literature, including limited attention to intraday and balancing markets and the need for market-specific modeling strategies, thereby helping to consolidate and advance existing review studies.

## I Introduction

Europe has one of the world’s most active and tightly coupled wholesale electricity markets, where cross-border trading makes prices a central signal for system operation. In this setting, the day-ahead market provides the primary reference prices through a centralized auction clearing all delivery hours for the next day; however, forecast errors, renewable intermittency, and demand uncertainty leave substantial risk close to delivery. To manage these deviations, European markets rely on continuous intraday trading, which enables participants to adjust positions nearer to real time. Remaining mismatches between schedules and physical reality are finally resolved in the balancing market, where Transmission System Operators (TSOs) activate reserves and settle real-time imbalances.
Other regions (e.g., the US) operate real-time markets that are analogous to Europe’s near-real-time layers, but differ in design and are not considered here.
Accordingly, effective trading participation in each market stage relies on accurate Electricity Price Forecasting (EPF). EPF is therefore critical across the full market stack, supporting bidding strategies, congestion handling, and renewable integration.

![Refer to caption](x1.png)


Figure 1: 
Visualization of day-ahead, intraday, and imbalance prices from 1-15 October 2025 in Austria.
The imbalance price exhibits the highest volatility, the day-ahead price is the smoothest, and the intraday price lies in between.

Yet EPF is challenging because electricity prices are shaped by non-storability, network constraints, and weather-driven uncertainty, leading to pronounced nonlinearity, regime changes, and heavy-tailed spikes. These difficulties manifest differently across markets: day-ahead prices reflect system-wide fundamentals and expectations at hourly (increasingly quarter-hourly) granularity; intraday prices are additionally driven by micro-orderbook dynamics and rapidly updating forecasts; and balancing prices are tightly linked to system imbalance, reserve scarcity, and activation rules, often yielding the highest volatility, as illustrated in Fig. [1](https://arxiv.org/html/2602.10071v1#S1.F1 "Figure 1 ‣ I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"). Consequently, the highly dynamic and spike-prone nature of electricity prices calls for forecasting models that can capture complex dependencies.

![Refer to caption](x2.png)


Figure 2: Backbone comparison of deep learning models.




TABLE I: Summary of electricity price forecasting studies.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Year | Paper | Market | Backbone | Head | Loss | Feature | Country |
| 2018 | [[28](https://arxiv.org/html/2602.10071v1#bib.bib25 "Forecasting spot electricity prices: deep learning approaches and empirical comparison of traditional algorithms")] | Day-ahead | LSTM-MLP / GRU-MLP | MMP | MAE | M | Belgium |
|  | [[64](https://arxiv.org/html/2602.10071v1#bib.bib27 "Electricity price forecasting using recurrent neural networks")] | Day-ahead | MLP / CNN / LSTM / GRU | SMP | MAE | M | Turkey |
|  | [[2](https://arxiv.org/html/2602.10071v1#bib.bib28 "Electricity price forecasting for nord pool data")] | Day-ahead | MLP | SMP | n.s. | U | Lithuania |
|  | [[7](https://arxiv.org/html/2602.10071v1#bib.bib29 "Deep neural networks (dnn) for day-ahead electricity price markets")] | Day-ahead | MLP | SMP | MSE | M | Spain / Portugal |
| 2019 | [[54](https://arxiv.org/html/2602.10071v1#bib.bib39 "Neural network based model comparison for intraday electricity price forecasting")] | \cellcolorM3lightgreenIntraday | \cellcolorM3lightgreenLSTM / GRU / MLP | \cellcolorM3lightgreenSMP | \cellcolorM3lightgreenMAE | \cellcolorM3lightgreenM | \cellcolorM3lightgreenTurkey |
|  | [[10](https://arxiv.org/html/2602.10071v1#bib.bib106 "Probabilistic forecasting of imbalance prices in the belgian context")] | \cellcolorM3midgreenBalancing | \cellcolorM3midgreenMLP | \cellcolorM3midgreenSMP | n.s. | \cellcolorM3midgreenM | \cellcolorM3midgreenBelgium |
|  | [[24](https://arxiv.org/html/2602.10071v1#bib.bib38 "Electricity price forecasting in the danish day-ahead market using the tbats, ann and arima methods")] | Day-ahead | MLP | SMP | MAE | M | Denmark |
|  | [[42](https://arxiv.org/html/2602.10071v1#bib.bib102 "On the importance of the long-term seasonal component in day-ahead electricity price forecasting with narx neural networks")] | Day-ahead | MLP | SMP | MSE | M | Norway / Sweden / Denmark / +2 |
|  | [[74](https://arxiv.org/html/2602.10071v1#bib.bib103 "Short term electricity spot price forecasting using catboost and bidirectional long short term memory neural network")] | Day-ahead | LSTM | SMP | n.s. | U | Sweden |
| 2020 | [[59](https://arxiv.org/html/2602.10071v1#bib.bib26 "Electricity price forecasting with neural networks on epex order books")] | Day-ahead | MLP | SMP | MSE | M | Germany / Austria |
|  | [[44](https://arxiv.org/html/2602.10071v1#bib.bib22 "Short-term electricity price forecasting with recurrent regimes and structural breaks")] | Day-ahead | MLP | SMP | MSE | M | Spain / Portugal |
|  | [[39](https://arxiv.org/html/2602.10071v1#bib.bib96 "Neural networks in day-ahead electricity price forecasting: single vs. multiple outputs")] | Day-ahead | MLP | SMP | n.s. | M | Belgium / France / Germany / + 4 |
|  | [[43](https://arxiv.org/html/2602.10071v1#bib.bib101 "Probabilistic electricity price forecasting with narx networks: combine point or probabilistic forecasts?")] | Day-ahead | MLP | SMM | Pinball | M | Norway / Sweden / Denmark / +2 |
| 2021 | [[34](https://arxiv.org/html/2602.10071v1#bib.bib41 "Day-ahead electricity price prediction applying hybrid models of lstm-based deep learning methods and feature selection algorithms under consideration of market coupling")] | Day-ahead | LSTM / CNN-LSTM | SMP | MSE | M | Norway / Sweden / Denmark / + 4 |
|  | [[29](https://arxiv.org/html/2602.10071v1#bib.bib42 "Forecasting day-ahead electricity prices: a review of state-of-the-art algorithms, best practices and an open-access benchmark")] | Day-ahead | MLP | SMP | MAE | M | Belgium / Norway / France / + 4 |
|  | [[20](https://arxiv.org/html/2602.10071v1#bib.bib114 "Forecasting electricity price in different time horizons: an application to the italian electricity market")] | Day-ahead | MLP | SMP | MSE | M | Italy |
| 2022 | [[5](https://arxiv.org/html/2602.10071v1#bib.bib91 "Interpretable transformer model for capturing regime switching effects of real-time electricity prices")] | \cellcolorM3midgreenBalancing | \cellcolorM3midgreenLSTM-Attention | \cellcolorM3midgreenSMM | \cellcolorM3midgreenPinball | \cellcolorM3midgreenM | \cellcolorM3midgreenBelgium |
|  | [[48](https://arxiv.org/html/2602.10071v1#bib.bib43 "Probabilistic forecasting of german electricity imbalance prices")] | \cellcolorM3midgreenBalancing | \cellcolorM3midgreenMLP | \cellcolorM3midgreenSSM | \cellcolorM3midgreenLogLik | \cellcolorM3midgreenM | \cellcolorM3midgreenGermany |
|  | [[63](https://arxiv.org/html/2602.10071v1#bib.bib44 "Electricity price forecasting on the day-ahead market using machine learning")] | Day-ahead | CNN / MLP | MMP | LogCosH | M | France / Germany / Belgium |
|  | [[73](https://arxiv.org/html/2602.10071v1#bib.bib45 "A hybrid model based on bidirectional long short-term memory neural network and catboost for short-term electricity spot price forecasting")] | Day-ahead | LSTM | SMP | n.s. | M | Sweden |
|  | [[45](https://arxiv.org/html/2602.10071v1#bib.bib46 "Electricity price forecasting with high penetration of renewable energy using attention-based lstm network trained by crisscross optimization")] | Day-ahead | Attention-LSTM | SMP | MAE | M | Denmark |
|  | [[3](https://arxiv.org/html/2602.10071v1#bib.bib49 "Framework for collaborative intelligence in forecasting day-ahead electricity price")] | Day-ahead | MLP | SMP | MAE | M | Spain |
|  | [[65](https://arxiv.org/html/2602.10071v1#bib.bib105 "Electricity price forecasting for norwegian day-ahead market using hybrid ai models")] | Day-ahead | MLP / LSTM | SMP | MSE | M | Norway |
| 2023 | [[41](https://arxiv.org/html/2602.10071v1#bib.bib97 "Trading on short-term path forecasts of intraday electricity prices. part ii–distributional deep neural networks")] | \cellcolorM3lightgreenIntraday | \cellcolorM3lightgreenMLP | \cellcolorM3lightgreenSMM | \cellcolorM3lightgreenNLL | \cellcolorM3lightgreenM | \cellcolorM3lightgreenGermany |
|  | [[12](https://arxiv.org/html/2602.10071v1#bib.bib89 "Forecasting imbalance price densities with statistical methods and neural networks")] | \cellcolorM3midgreenBalancing | \cellcolorM3midgreenMLP / LSTM / GRU / Transformer | \cellcolorM3midgreenSSM | \cellcolorM3midgreenPinball | \cellcolorM3midgreenM | \cellcolorM3midgreenUK |
|  | [[40](https://arxiv.org/html/2602.10071v1#bib.bib56 "Distributional neural networks for electricity price forecasting")] | Day-ahead | MLP | SMM | NLL | M | Germany |
|  | [[55](https://arxiv.org/html/2602.10071v1#bib.bib58 "Neural basis expansion analysis with exogenous variables: forecasting electricity prices with nbeatsx")] | Day-ahead | MLP | SMP | MAE | M | Belgium / France / Germany / + 5 |
|  | [[14](https://arxiv.org/html/2602.10071v1#bib.bib59 "Transfer learning for electricity price forecasting")] | Day-ahead | MLP | MMP | MAE | M | Belgium / France / Germany / + 5 |
|  | [[49](https://arxiv.org/html/2602.10071v1#bib.bib100 "Combining predictive distributions of electricity prices: does minimizing the crps lead to optimal decisions in day-ahead bidding?")] | Day-ahead | MLP | SMM | Pinball | M | Germany |
| 2024 | [[27](https://arxiv.org/html/2602.10071v1#bib.bib62 "Intraday electricity price forecasting via lstm and trading strategy for the power market: a case study of the west denmark dk1 grid region")] | \cellcolorM3lightgreenIntraday | \cellcolorM3lightgreenLSTM / CNN | \cellcolorM3lightgreenSMP | \cellcolorM3lightgreenn.s. | \cellcolorM3lightgreenM | \cellcolorM3lightgreenDenmark |
|  | [[52](https://arxiv.org/html/2602.10071v1#bib.bib70 "Electricity price forecasting in the irish balancing market")] | \cellcolorM3midgreenBalancing | \cellcolorM3midgreenMLP / LSTM-MLP | \cellcolorM3midgreenSMP | \cellcolorM3midgreenn.s. | \cellcolorM3midgreenM | \cellcolorM3midgreenIreland |
|  | [[9](https://arxiv.org/html/2602.10071v1#bib.bib73 "Seasonality in deep learning forecasts of electricity imbalance prices")] | \cellcolorM3midgreenBalancing | \cellcolorM3midgreenLSTM-Attention | \cellcolorM3midgreenSMP | \cellcolorM3midgreenMSE | \cellcolorM3midgreenM | \cellcolorM3midgreenUK |
|  | [[22](https://arxiv.org/html/2602.10071v1#bib.bib74 "Probabilistic electricity price forecasting based on penalized temporal fusion transformer")] | Day-ahead | Transformer | SMM | Pinball | M | Norway / Finland / Poland / +2 |
|  | [[69](https://arxiv.org/html/2602.10071v1#bib.bib61 "Forecasting day-ahead electricity prices with spatial dependence")] | Day-ahead | GNN | MMP | n.s. | M | Norway / Sweden / Denmark / + 4 |
|  | [[62](https://arxiv.org/html/2602.10071v1#bib.bib69 "A robust electricity price forecasting framework based on heteroscedastic temporal convolutional network")] | Day-ahead | MLP / CNN / Transformer / GRU | SMM | LogLik | M | Germany / France / Belgium / + 4 |
|  | [[46](https://arxiv.org/html/2602.10071v1#bib.bib72 "Day-ahead electricity price prediction in multi-price zones based on multi-view fusion spatio-temporal graph neural network")] | Day-ahead | GNN | MMP | MAE | M | Germany / Hungary / Italy / + 15 |
|  | [[31](https://arxiv.org/html/2602.10071v1#bib.bib78 "Data-driven techniques for short-term electricity price forecasting through novel deep learning approaches with attention mechanisms")] | Day-ahead | CNN-GRU / Transformer | SMP | MSE | M | Germany / Luxembourg |
|  | [[47](https://arxiv.org/html/2602.10071v1#bib.bib80 "Day-ahead electricity price forecasting using a cnn-bilstm model in conjunction with autoregressive modeling and hyperparameter optimization")] | Day-ahead | CNN-LSTM | SMP | MSE | U | UK / Germany |
| 2025 | [[6](https://arxiv.org/html/2602.10071v1#bib.bib99 "Probabilistic intraday electricity price forecasting using generative machine learning")] | \cellcolorM3lightgreenIntraday | \cellcolorM3lightgreenGM | \cellcolorM3lightgreenSMM | \cellcolorM3lightgreenCLF | \cellcolorM3lightgreenM | \cellcolorM3lightgreenGermany |
|  | [[56](https://arxiv.org/html/2602.10071v1#bib.bib90 "Prediction of imbalance prices through gradient boosting algorithms: an application to the greek balancing market")] | \cellcolorM3midgreenBalancing | \cellcolorM3midgreenLSTM | \cellcolorM3midgreenSMP | \cellcolorM3midgreenn.s. | \cellcolorM3midgreenM | \cellcolorM3midgreenGreece |
|  | [[53](https://arxiv.org/html/2602.10071v1#bib.bib85 "Optimising quantile-based trading strategies in electricity arbitrage")] | \cellcolorM3midgreenBalancing | \cellcolorM3midgreenMLP / LSTM-MLP | \cellcolorM3midgreenSMM | \cellcolorM3midgreenPinball | \cellcolorM3midgreenM | \cellcolorM3midgreenIreland |
|  | [[1](https://arxiv.org/html/2602.10071v1#bib.bib84 "Multivariate probabilistic forecasting of electricity prices with trading applications")] | Day-ahead | MLP / LSTM | SMM | NLL | M | Germany |
|  | [[68](https://arxiv.org/html/2602.10071v1#bib.bib87 "A novel mid-and long-term time-series forecasting framework for electricity price based on hierarchical recurrent neural networks")] | Day-ahead | RNN | SMP | MSE | M | France |
| 2026 | [[72](https://arxiv.org/html/2602.10071v1#bib.bib98 "Orderbook feature learning and asymmetric generalization in intraday electricity markets")] | \cellcolorM3lightgreenIntraday | \cellcolorM3lightgreenKAN / MLP | \cellcolorM3lightgreenSSM | \cellcolorM3lightgreenPinball | \cellcolorM3lightgreenM | \cellcolorM3lightgreenGermany / Austria |
|  | [[71](https://arxiv.org/html/2602.10071v1#bib.bib93 "OrderFusion: encoding orderbook for end-to-end probabilistic intraday electricity price forecasting")] | \cellcolorM3lightgreenIntraday | \cellcolorM3lightgreenCross-Attention (Transformer) | \cellcolorM3lightgreenSSM | \cellcolorM3lightgreenPinball | \cellcolorM3lightgreenM | \cellcolorM3lightgreenGermany / Austria |
|  | [[4](https://arxiv.org/html/2602.10071v1#bib.bib95 "Recurrent neural networks with linear structures for electricity price forecasting")] | Day-ahead | RNN | SMP | MSE | M | Germany |
|  | [[38](https://arxiv.org/html/2602.10071v1#bib.bib94 "Electricity price forecasting: bridging linear models, neural networks and online learning")] | Day-ahead | MLP | SMP | MAE | M | Germany / Spain |
|  | [[70](https://arxiv.org/html/2602.10071v1#bib.bib24 "PriceFM: foundation model for probabilistic electricity price forecasting")] | Day-ahead | MoE-GNN | MMM | Pinball | M | Germany / Austria / France / + 21 |

Against this backdrop, deep learning has emerged as a powerful tool for EPF due to its ability to learn complex nonlinear patterns from data. Early studies primarily applied neural networks for day-ahead price forecasting, using architectures such as MLPs, LSTMs, GRUs, and CNNs [[28](https://arxiv.org/html/2602.10071v1#bib.bib25 "Forecasting spot electricity prices: deep learning approaches and empirical comparison of traditional algorithms"), [64](https://arxiv.org/html/2602.10071v1#bib.bib27 "Electricity price forecasting using recurrent neural networks"), [2](https://arxiv.org/html/2602.10071v1#bib.bib28 "Electricity price forecasting for nord pool data"), [7](https://arxiv.org/html/2602.10071v1#bib.bib29 "Deep neural networks (dnn) for day-ahead electricity price markets")]. Subsequent work expanded the scope to multi-timestep forecasting, multi-market settings, and probabilistic outputs [[24](https://arxiv.org/html/2602.10071v1#bib.bib38 "Electricity price forecasting in the danish day-ahead market using the tbats, ann and arima methods"), [43](https://arxiv.org/html/2602.10071v1#bib.bib101 "Probabilistic electricity price forecasting with narx networks: combine point or probabilistic forecasts?"), [34](https://arxiv.org/html/2602.10071v1#bib.bib41 "Day-ahead electricity price prediction applying hybrid models of lstm-based deep learning methods and feature selection algorithms under consideration of market coupling"), [29](https://arxiv.org/html/2602.10071v1#bib.bib42 "Forecasting day-ahead electricity prices: a review of state-of-the-art algorithms, best practices and an open-access benchmark")]. More recently, advances in attention mechanisms, Transformers, graph-based models, and Mixture-of-Experts (MoEs) have further enriched the modeling landscape, enabling long-range dependency modeling, spatial coupling across bidding zones, and scalable multi-country forecasting [[45](https://arxiv.org/html/2602.10071v1#bib.bib46 "Electricity price forecasting with high penetration of renewable energy using attention-based lstm network trained by crisscross optimization"), [69](https://arxiv.org/html/2602.10071v1#bib.bib61 "Forecasting day-ahead electricity prices with spatial dependence"), [46](https://arxiv.org/html/2602.10071v1#bib.bib72 "Day-ahead electricity price prediction in multi-price zones based on multi-view fusion spatio-temporal graph neural network"), [22](https://arxiv.org/html/2602.10071v1#bib.bib74 "Probabilistic electricity price forecasting based on penalized temporal fusion transformer"), [70](https://arxiv.org/html/2602.10071v1#bib.bib24 "PriceFM: foundation model for probabilistic electricity price forecasting")].

Existing review papers have established a strong foundation for EPF by clarifying market mechanisms and forecasting horizons [[67](https://arxiv.org/html/2602.10071v1#bib.bib112 "Electricity price forecasting: a review of the state-of-the-art with a look into the future"), [21](https://arxiv.org/html/2602.10071v1#bib.bib107 "Electricity price forecasting: the dawn of machine learning"), [23](https://arxiv.org/html/2602.10071v1#bib.bib113 "A review on short-term electricity price forecasting techniques for energy markets")]. Other studies have emphasized the importance of rigorous and reproducible evaluation, advocating standardized datasets, error measures, and benchmarking toolkits [[30](https://arxiv.org/html/2602.10071v1#bib.bib110 "Forecasting day-ahead electricity prices: a review of state-of-the-art algorithms, best practices and an open-access benchmark"), [18](https://arxiv.org/html/2602.10071v1#bib.bib109 "Energy forecasting: a review and outlook")]. In parallel, probabilistic EPF has been systematically formalized through reliability-sharpness principles and statistically sound evaluation protocols [[50](https://arxiv.org/html/2602.10071v1#bib.bib111 "Recent advances in electricity price forecasting: a review of probabilistic forecasting")]. More recently, cross-market surveys have begun to jointly consider day-ahead, intraday, and balancing markets for general method analysis [[51](https://arxiv.org/html/2602.10071v1#bib.bib108 "A review of electricity price forecasting models in the day-ahead, intra-day, and balancing markets")].
Nevertheless, as deep learning plays an increasingly central role in EPF, most existing surveys provide limited in-depth analysis of deep learning. In particular, the interplay between representation learning, output formulation, and optimization objectives, and the way these design choices encode market characteristics, remains insufficiently structured. This gap motivates a unified deep learning taxonomy that can explain methodological shifts in the literature and enable consistent synthesis across markets.

To organize this rapidly growing and heterogeneous literature, this paper adopts a unified modeling perspective that decomposes deep learning approaches into three fundamental components: the *backbone*, which governs representation learning from inputs; the *head*, which defines the output structure across countries, timesteps, and uncertainty dimensions; and the *loss function*, which encodes the forecasting objective.
Using this framework, we review and conclude trends in deep learning-based EPF across day-ahead, intraday, and balancing markets. For day-ahead markets, the literature exhibits a clear evolution toward multi-country, multi-timestep, and multi-quantile models [[40](https://arxiv.org/html/2602.10071v1#bib.bib56 "Distributional neural networks for electricity price forecasting"), [55](https://arxiv.org/html/2602.10071v1#bib.bib58 "Neural basis expansion analysis with exogenous variables: forecasting electricity prices with nbeatsx"), [14](https://arxiv.org/html/2602.10071v1#bib.bib59 "Transfer learning for electricity price forecasting"), [62](https://arxiv.org/html/2602.10071v1#bib.bib69 "A robust electricity price forecasting framework based on heteroscedastic temporal convolutional network"), [22](https://arxiv.org/html/2602.10071v1#bib.bib74 "Probabilistic electricity price forecasting based on penalized temporal fusion transformer")]. Intraday studies, though fewer in number, increasingly emphasize orderbook-driven modeling and trajectory forecasting [[54](https://arxiv.org/html/2602.10071v1#bib.bib39 "Neural network based model comparison for intraday electricity price forecasting"), [27](https://arxiv.org/html/2602.10071v1#bib.bib62 "Intraday electricity price forecasting via lstm and trading strategy for the power market: a case study of the west denmark dk1 grid region"), [41](https://arxiv.org/html/2602.10071v1#bib.bib97 "Trading on short-term path forecasts of intraday electricity prices. part ii–distributional deep neural networks"), [72](https://arxiv.org/html/2602.10071v1#bib.bib98 "Orderbook feature learning and asymmetric generalization in intraday electricity markets"), [71](https://arxiv.org/html/2602.10071v1#bib.bib93 "OrderFusion: encoding orderbook for end-to-end probabilistic intraday electricity price forecasting")]. Balancing market research, by contrast, favors mechanism-aware pipelines and market-specific designs due to pronounced regime switching and heterogeneous settlement rules [[10](https://arxiv.org/html/2602.10071v1#bib.bib106 "Probabilistic forecasting of imbalance prices in the belgian context"), [48](https://arxiv.org/html/2602.10071v1#bib.bib43 "Probabilistic forecasting of german electricity imbalance prices"), [52](https://arxiv.org/html/2602.10071v1#bib.bib70 "Electricity price forecasting in the irish balancing market"), [53](https://arxiv.org/html/2602.10071v1#bib.bib85 "Optimising quantile-based trading strategies in electricity arbitrage"), [5](https://arxiv.org/html/2602.10071v1#bib.bib91 "Interpretable transformer model for capturing regime switching effects of real-time electricity prices"), [12](https://arxiv.org/html/2602.10071v1#bib.bib89 "Forecasting imbalance price densities with statistical methods and neural networks")]. The main contributions of this paper are as follows:

* •

  Unified deep learning evaluation taxonomy:
  We propose a unified evaluation framework that decomposes deep learning models into backbone, head, and loss components, and provides a consistent evaluation perspective for comparing architectures, output structures, and forecasting objectives across studies.
* •

  Cross-market trend synthesis: Using this taxonomy, we provide a comprehensive synthesis of deep learning trends in day-ahead, intraday, and balancing markets, clarifying how modeling choices evolve in response to distinct market characteristics.
* •

  Identification of gaps and future directions:
  We highlight key gaps and open challenges in the literature, including limited attention to intraday and balancing markets, the increasing importance of microstructure-aware and trajectory-based forecasting, and the need for market-specific design in deep learning models.

The remainder of this paper is organized as follows. Section [II](https://arxiv.org/html/2602.10071v1#S2 "II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets") presents the fundamental components of deep learning models, including the backbone, head, and loss function. Section [III](https://arxiv.org/html/2602.10071v1#S3 "III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets") analyzes trends and discusses future research directions in deep learning for EPF across markets. Section [IV](https://arxiv.org/html/2602.10071v1#S4 "IV Conclusion ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets") concludes the paper and summarizes key findings.

## II Deep Learning Components

A deep learning model typically consists of three components: a backbone, a head, and a loss function.
The *backbone* defines how a deep learning model processes the input sequence 𝐗∈ℝL×F\mathbf{X}\in\mathbb{R}^{L\times F}, where LL is the number of timesteps and FF the number of features (e.g., load, wind, price).
The *head* varies depending on whether the model is trained for single- or multi-output forecasting. The *loss* may be pointwise (e.g., MAE) or probabilistic (e.g., quantile loss).

### II-A Backbone

The choice of backbone reflects assumptions about temporal, spatial, and structural patterns in electricity markets.
The simplest backbone is the Multi-layer Perceptron (MLP) [[58](https://arxiv.org/html/2602.10071v1#bib.bib4 "Learning representations by back-propagating errors")], which flattens the input sequence into a vector of size L⋅FL\cdot F. While computationally efficient, MLPs ignore sequential or spatial dependencies.
To retain temporal structure, Convolutional Neural Networks (CNNs) [[32](https://arxiv.org/html/2602.10071v1#bib.bib5 "Gradient-based learning applied to document recognition")] operate directly on input sequences, applying local convolutional filters over time to capture short-range patterns.
Recurrent Neural Networks (RNNs) [[11](https://arxiv.org/html/2602.10071v1#bib.bib6 "Finding structure in time")] also take a sequential view, processing input sequence step-by-step to build memory over time. Variants like Long Short-Term Memory (LSTM) [[17](https://arxiv.org/html/2602.10071v1#bib.bib7 "Long short-term memory")] and Gated Recurrent Unit (GRU) [[8](https://arxiv.org/html/2602.10071v1#bib.bib8 "Learning phrase representations using rnn encoder-decoder for statistical machine translation")] mitigate vanishing gradients for long-sequence modeling, but are slow to train due to limited parallelism.
Replacing recurrence with an Attention mechanism, Transformer [[66](https://arxiv.org/html/2602.10071v1#bib.bib9 "Attention is all you need")] processes the entire sequence in parallel, learning dependencies between all time steps.
Extensions such as Cross-Attention further allow Transformers to condition price forecasts on contextual information.
As electricity markets are spatially interconnected through transmission lines, Graph Neural Networks (GNNs) [[26](https://arxiv.org/html/2602.10071v1#bib.bib10 "Semi-supervised classification with graph convolutional networks")] extend temporal backbones by explicitly incorporating graph structures of transmission topology, where the spatial dependencies are captured via message passing over the graph.
Generative Models (GMs) such as Variational Autoencoder (VAE) [[25](https://arxiv.org/html/2602.10071v1#bib.bib11 "Auto-encoding variational bayes")] and Generative Adversarial Network (GAN) [[13](https://arxiv.org/html/2602.10071v1#bib.bib12 "Generative adversarial nets")],
learn distributions over input sequence, offering calibrated probabilistic forecasts.
A recent addition is the Kolmogorov–Arnold Network (KAN) [[35](https://arxiv.org/html/2602.10071v1#bib.bib14 "Kan: kolmogorov-arnold networks")], which expresses functions over input sequences via sparse sums of univariate nonlinearities, yielding interpretable and structured representations.
In scenarios with high data heterogeneity, Mixture-of-Experts (MoE) [[61](https://arxiv.org/html/2602.10071v1#bib.bib15 "Outrageously large neural networks: the sparsely-gated mixture-of-experts layer")] improve flexibility by routing input sequences through multiple specialized subnetworks (e.g., MLP or CNN), with a learnable gating function selecting which experts to activate. This conditional computation enables the model to adapt to different regimes and load patterns.
When one backbone is not enough, Hybrid Models combine them: CNNs can extract local features before feeding into LSTMs [[57](https://arxiv.org/html/2602.10071v1#bib.bib16 "A dual-stage attention-based recurrent neural network for time series prediction")], or attention can replace MoE-style gating [[33](https://arxiv.org/html/2602.10071v1#bib.bib17 "Enhancing the locality and breaking the memory bottleneck of transformer on time series forecasting")], enabling dynamic expert selection.
The architectural choices reflect different assumptions about how electricity price signals evolve across time and space.

### II-B Head

The *head* determines the output structure of the model, reflecting how many countries, timesteps, and quantiles are forecasted simultaneously. Given the encoded representation of the input 𝐗∈ℝL×F\mathbf{X}\in\mathbb{R}^{L\times F}, the head maps it to a structured output depending on the forecasting objective.

The output types can be systematically categorized using the shorthand notation C-T-Q, where the first letter indicates the number of Countries (S: single, M: multiple), the second for Timesteps, and the third for Quantiles. Common head configurations are shown in Table [II](https://arxiv.org/html/2602.10071v1#S2.T2 "Table II ‣ II-B Head ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").

TABLE II: Output head configurations.

|  |  |  |  |
| --- | --- | --- | --- |
| Code | Description |  |  |
| SSP | Single-country | Single-timestep | Pointwise |
| SSS | Single-country | Single-timestep | Single-quantile |
| SSM | Single-country | Single-timestep | Multi-quantile |
| SMP | Single-country | Multi-timestep | Pointwise |
| SMS | Single-country | Multi-timestep | Single-quantile |
| SMM | Single-country | Multi-timestep | Multi-quantile |
| MSP | Multi-country | Single-timestep | Pointwise |
| MSS | Multi-country | Single-timestep | Single-quantile |
| MSM | Multi-country | Single-timestep | Multi-quantile |
| MMP | Multi-country | Multi-timestep | Pointwise |
| MMS | Multi-country | Multi-timestep | Single-quantile |
| MMM | Multi-country | Multi-timestep | Multi-quantile |

Beyond standard formulations, the flexibility of neural networks also enables more advanced multi-head designs with additional structural constraints. For instance, [[71](https://arxiv.org/html/2602.10071v1#bib.bib93 "OrderFusion: encoding orderbook for end-to-end probabilistic intraday electricity price forecasting"), [70](https://arxiv.org/html/2602.10071v1#bib.bib24 "PriceFM: foundation model for probabilistic electricity price forecasting")] proposed a *hierarchical quantile head* in which the median quantile is first predicted using a dense layer, and a non-negative residual is learned through another dense layer. Then, the upper quantile prediction is constructed by adding the non-negative residual to the median prediction, which guarantees monotonicity and effectively mitigates the quantile crossing issue, as also discussed in prior works [[37](https://arxiv.org/html/2602.10071v1#bib.bib18 "A hybrid model for gefcom2014 probabilistic electricity price forecasting"), [60](https://arxiv.org/html/2602.10071v1#bib.bib19 "Averaging predictive distributions across calibration windows for day-ahead electricity price forecasting"), [41](https://arxiv.org/html/2602.10071v1#bib.bib97 "Trading on short-term path forecasts of intraday electricity prices. part ii–distributional deep neural networks")].

### II-C Loss Function

The choice of loss function depends on the forecasting objective, which may be pointwise, probabilistic, or customized to reflect domain-specific considerations.

For pointwise forecasting, common loss functions include Mean Squared Error (MSE) and Mean Absolute Error (MAE), defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒMSE=1N​∑i=1N(yi−y^i)2,\mathcal{L}\_{\mathrm{MSE}}=\frac{1}{N}\sum\_{i=1}^{N}(y\_{i}-\hat{y}\_{i})^{2}, |  | (1) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒMAE=1N​∑i=1N|yi−y^i|,\mathcal{L}\_{\mathrm{MAE}}=\frac{1}{N}\sum\_{i=1}^{N}|y\_{i}-\hat{y}\_{i}|, |  | (2) |

where yiy\_{i} and y^i\hat{y}\_{i} denote the true and predicted values. MSE penalizes large errors more strongly due to its quadratic form, making it more sensitive to outliers compared to MAE.

For probabilistic forecasting, two major classes of loss functions are commonly used.

The first is the Pinball Loss, widely used for training quantile regressors. For a given quantile level τ∈(0,1)\tau\in(0,1), the pinball loss is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒpinball​(τ)=1N​∑i=1Nmax⁡(τ​(yi−y^i),(τ−1)​(yi−y^i)).\mathcal{L}\_{\mathrm{pinball}}(\tau)=\frac{1}{N}\sum\_{i=1}^{N}\max\left(\tau(y\_{i}-\hat{y}\_{i}),(\tau-1)(y\_{i}-\hat{y}\_{i})\right). |  | (3) |

This formulation encourages correct quantile calibration by penalizing overestimation and underestimation differently.

The second is the Log-Likelihood (LogLik). Assuming a parametric form (e.g., Gaussian), the LogLik is maximized, or Negative Log-Likelihood (NLL) is minimized, when the model assigns high probability density to the observed targets:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒLogLik=1N​∑i=1Nlog⁡p​(yi∣θi),\mathcal{L}\_{\mathrm{LogLik}}=\frac{1}{N}\sum\_{i=1}^{N}\log p(y\_{i}\mid\theta\_{i}), |  | (4) |

where p​(yi∣θi)p(y\_{i}\mid\theta\_{i}) is the predicted likelihood of the true value yiy\_{i} under distribution parameters θi\theta\_{i} (e.g., predicted mean and variance). LogLik-based losses are commonly used in generative models and parametric uncertainty quantification.

In addition to standard objectives, one may design Customized Loss Functions (CLFs) to guide the model toward desired behavior. For example, [[36](https://arxiv.org/html/2602.10071v1#bib.bib20 "Statistical and economic evaluation of forecasts in electricity markets: beyond rmse and mae")] proposes a Min-Max Price Deviation (MPD) loss, which reflects the profitability of battery systems. Such task-specific objectives are particularly relevant in market-driven applications where the value of a forecast depends on downstream decision impacts.

## III Trends in Electricity Price Forecasting

This section reviews empirical trends in deep learning-based EPF across day-ahead, intraday, and balancing markets. Despite differences in market design and forecasting objectives, several common patterns emerge. As shown in Table [I](https://arxiv.org/html/2602.10071v1#S1.T1 "Table I ‣ I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets") (n.s. denotes *not specified*; U and M under the *Feature* column indicate univariate and multivariate inputs; intraday studies are highlighted in green, and balancing-market studies are shaded in light gray), most studies favor multivariate input features, combining historical prices with exogenous variables such as load and renewable generation, reflecting the strong fundamental drivers of price dynamics. At the same time, a portion of the literature does not explicitly specify the training loss, complicating direct comparison across models. Beyond these shared characteristics, modeling choices diverge substantially by market, as discussed in the following subsections.

### III-A Day-Ahead Market

Day-ahead price forecasting has been the earliest and most extensively studied application of deep learning in power markets. As summarized in Table [I](https://arxiv.org/html/2602.10071v1#S1.T1 "Table I ‣ I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"), the literature from 2018 to 2026 reveals several clear methodological trends.

#### Evolution of model families

Early studies (2018-2020) predominantly relied on simple backbones such as MLP, LSTM, GRU, and CNN, either individually or in hybrid forms [[28](https://arxiv.org/html/2602.10071v1#bib.bib25 "Forecasting spot electricity prices: deep learning approaches and empirical comparison of traditional algorithms"), [64](https://arxiv.org/html/2602.10071v1#bib.bib27 "Electricity price forecasting using recurrent neural networks"), [2](https://arxiv.org/html/2602.10071v1#bib.bib28 "Electricity price forecasting for nord pool data"), [7](https://arxiv.org/html/2602.10071v1#bib.bib29 "Deep neural networks (dnn) for day-ahead electricity price markets"), [24](https://arxiv.org/html/2602.10071v1#bib.bib38 "Electricity price forecasting in the danish day-ahead market using the tbats, ann and arima methods")]. From 2021 onward, more expressive architectures began to emerge: attention-based models were increasingly adopted to capture temporal dependencies [[45](https://arxiv.org/html/2602.10071v1#bib.bib46 "Electricity price forecasting with high penetration of renewable energy using attention-based lstm network trained by crisscross optimization"), [22](https://arxiv.org/html/2602.10071v1#bib.bib74 "Probabilistic electricity price forecasting based on penalized temporal fusion transformer")], while GNNs were introduced to model spatial dependencies across interconnected bidding zones [[69](https://arxiv.org/html/2602.10071v1#bib.bib61 "Forecasting day-ahead electricity prices with spatial dependence"), [46](https://arxiv.org/html/2602.10071v1#bib.bib72 "Day-ahead electricity price prediction in multi-price zones based on multi-view fusion spatio-temporal graph neural network")].
Most recently, large-scale architectures combining MoE and graph structures have been proposed to jointly model multiple regions and market conditions [[70](https://arxiv.org/html/2602.10071v1#bib.bib24 "PriceFM: foundation model for probabilistic electricity price forecasting")], where graph priors encode physical and market connectivity across bidding zones, marking a shift toward foundation-style models for day-ahead forecasting.

#### Preference for multi-timestep heads

Because day-ahead markets require forecasts for all delivery times of the next day, most deep learning models adopt multi-head designs. As shown in Table [I](https://arxiv.org/html/2602.10071v1#S1.T1 "Table I ‣ I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"), the dominant head type is SMP (single-country, multi-timestep, point forecasting) [[64](https://arxiv.org/html/2602.10071v1#bib.bib27 "Electricity price forecasting using recurrent neural networks"), [2](https://arxiv.org/html/2602.10071v1#bib.bib28 "Electricity price forecasting for nord pool data"), [7](https://arxiv.org/html/2602.10071v1#bib.bib29 "Deep neural networks (dnn) for day-ahead electricity price markets"), [24](https://arxiv.org/html/2602.10071v1#bib.bib38 "Electricity price forecasting in the danish day-ahead market using the tbats, ann and arima methods"), [34](https://arxiv.org/html/2602.10071v1#bib.bib41 "Day-ahead electricity price prediction applying hybrid models of lstm-based deep learning methods and feature selection algorithms under consideration of market coupling")]. In more advanced settings, models extend this formulation to MMP, SMM, or MMM heads, enabling simultaneous forecasting across multiple countries and/or multiple quantiles [[63](https://arxiv.org/html/2602.10071v1#bib.bib44 "Electricity price forecasting on the day-ahead market using machine learning"), [55](https://arxiv.org/html/2602.10071v1#bib.bib58 "Neural basis expansion analysis with exogenous variables: forecasting electricity prices with nbeatsx"), [14](https://arxiv.org/html/2602.10071v1#bib.bib59 "Transfer learning for electricity price forecasting"), [70](https://arxiv.org/html/2602.10071v1#bib.bib24 "PriceFM: foundation model for probabilistic electricity price forecasting")].

#### Shift from pointwise to probabilistic setting

Another notable trend is the gradual transition from pointwise objectives toward probabilistic forecasting. Prior to 2022, most studies optimized pointwise losses such as MAE or MSE [[28](https://arxiv.org/html/2602.10071v1#bib.bib25 "Forecasting spot electricity prices: deep learning approaches and empirical comparison of traditional algorithms"), [64](https://arxiv.org/html/2602.10071v1#bib.bib27 "Electricity price forecasting using recurrent neural networks"), [24](https://arxiv.org/html/2602.10071v1#bib.bib38 "Electricity price forecasting in the danish day-ahead market using the tbats, ann and arima methods"), [34](https://arxiv.org/html/2602.10071v1#bib.bib41 "Day-ahead electricity price prediction applying hybrid models of lstm-based deep learning methods and feature selection algorithms under consideration of market coupling")]. After 2023, however, an increasing number of works adopted distributional or quantile-based losses to better capture uncertainty in day-ahead prices [[40](https://arxiv.org/html/2602.10071v1#bib.bib56 "Distributional neural networks for electricity price forecasting"), [22](https://arxiv.org/html/2602.10071v1#bib.bib74 "Probabilistic electricity price forecasting based on penalized temporal fusion transformer"), [62](https://arxiv.org/html/2602.10071v1#bib.bib69 "A robust electricity price forecasting framework based on heteroscedastic temporal convolutional network"), [43](https://arxiv.org/html/2602.10071v1#bib.bib101 "Probabilistic electricity price forecasting with narx networks: combine point or probabilistic forecasts?")]. This shift reflects growing recognition that point forecasts alone are insufficient for risk-aware decision making, especially under high renewable penetration and volatile market conditions.

### III-B Intraday Market

Compared to day-ahead forecasting, intraday price forecasting has received substantially less attention in the literature. Existing studies nevertheless reveal several emerging trends.

#### From macro-level features to microstructure

Early intraday studies typically adopt a macro-level perspective, using aggregated price indices or engineered features, such as Volume-Weighted Average Prices (VWAPs), together with exogenous variables like load and renewable generation. These features are then processed by relatively simple backbones such as MLPs or LSTMs [[54](https://arxiv.org/html/2602.10071v1#bib.bib39 "Neural network based model comparison for intraday electricity price forecasting"), [27](https://arxiv.org/html/2602.10071v1#bib.bib62 "Intraday electricity price forecasting via lstm and trading strategy for the power market: a case study of the west denmark dk1 grid region")]. More recently, the focus has shifted toward orderbook-centric modeling. Instead of relying on VWAPs,
[[72](https://arxiv.org/html/2602.10071v1#bib.bib98 "Orderbook feature learning and asymmetric generalization in intraday electricity markets")] extracts 384 orderbook features and demonstrates that price percentiles from both buy and sell sides carry strong predictive power.
Going one step further, [[71](https://arxiv.org/html/2602.10071v1#bib.bib93 "OrderFusion: encoding orderbook for end-to-end probabilistic intraday electricity price forecasting")] directly models the raw orderbook using a cross-attention mechanism that reflects market-specific priors on buy-sell interactions, explicitly capturing the dynamics between buy and sell orders and achieving state-of-the-art performance. These works suggest that the predictive potential of orderbook dynamics remains largely underexplored.

#### From single-index prediction to trajectory forecasting

While early studies focus on one-step-ahead single-index forecasting (e.g., ID3) [[54](https://arxiv.org/html/2602.10071v1#bib.bib39 "Neural network based model comparison for intraday electricity price forecasting"), [27](https://arxiv.org/html/2602.10071v1#bib.bib62 "Intraday electricity price forecasting via lstm and trading strategy for the power market: a case study of the west denmark dk1 grid region")], recent works increasingly emphasize trajectory forecasting [[41](https://arxiv.org/html/2602.10071v1#bib.bib97 "Trading on short-term path forecasts of intraday electricity prices. part ii–distributional deep neural networks"), [16](https://arxiv.org/html/2602.10071v1#bib.bib3 "Simulation-based forecasting for intraday power markets: modelling fundamental drivers for location, shape and scale of the price distribution")]. Predicting an entire price path provides richer information about the temporal evolution of intraday prices, enabling more informed trading decisions compared to isolated point forecasts. Generative and distributional models are particularly well suited for this setting, as they naturally capture temporal uncertainty and price path variability.

#### Limited accessibility and synthetic data

Overall, intraday deep learning research remains sparse, with most existing studies concentrating on Germany and Austria [[41](https://arxiv.org/html/2602.10071v1#bib.bib97 "Trading on short-term path forecasts of intraday electricity prices. part ii–distributional deep neural networks"), [72](https://arxiv.org/html/2602.10071v1#bib.bib98 "Orderbook feature learning and asymmetric generalization in intraday electricity markets"), [71](https://arxiv.org/html/2602.10071v1#bib.bib93 "OrderFusion: encoding orderbook for end-to-end probabilistic intraday electricity price forecasting")]. A key barrier is the limited accessibility of raw orderbook. Moreover, although not studied in a deep learning context, several works have shown that using information from neighboring delivery hours can further improve forecasting performance [[15](https://arxiv.org/html/2602.10071v1#bib.bib1 "Multivariate simulation-based forecasting for intraday power markets: modeling cross-product price effects"), [19](https://arxiv.org/html/2602.10071v1#bib.bib2 "Directional price forecasting in the continuous intraday market under consideration of neighboring products and limit order books")].
In this context, synthetic data generation may offer a promising future research direction, for example, by simulating realistic orderbook dynamics and neighboring trade interactions across delivery hours.

### III-C Balancing Market

Compared to day-ahead and intraday markets, imbalance prices exhibit stronger volatility, heavy-tailed distributions, and pronounced regime switching driven by market rules and system conditions. As a result, deep learning applications in balancing markets have developed along distinct methodological directions, as summarized below.

#### Two-stage modeling paradigms

As imbalance price formation is governed by explicit market mechanisms,
many studies adopt two-stage modeling paradigms, in which deep learning models are first used to predict intermediate variables (e.g., system imbalance), followed by a dedicated mapping to imbalance prices [[10](https://arxiv.org/html/2602.10071v1#bib.bib106 "Probabilistic forecasting of imbalance prices in the belgian context"), [48](https://arxiv.org/html/2602.10071v1#bib.bib43 "Probabilistic forecasting of german electricity imbalance prices"), [53](https://arxiv.org/html/2602.10071v1#bib.bib85 "Optimising quantile-based trading strategies in electricity arbitrage")].
This mechanism-aware modeling philosophy distinguishes balancing-market forecasting from more direct end-to-end approaches commonly used in day-ahead and intraday settings.

#### Preference for shallow backbones

In contrast to the increasing architectural complexity observed in day-ahead and intraday forecasting, balancing-market studies predominantly rely on shallow backbones with relatively few layers. These lightweight architectures are favored for their interpretability and computational efficiency, particularly when models are deployed in operational decision-making or trading contexts [[10](https://arxiv.org/html/2602.10071v1#bib.bib106 "Probabilistic forecasting of imbalance prices in the belgian context"), [52](https://arxiv.org/html/2602.10071v1#bib.bib70 "Electricity price forecasting in the irish balancing market"), [53](https://arxiv.org/html/2602.10071v1#bib.bib85 "Optimising quantile-based trading strategies in electricity arbitrage"), [56](https://arxiv.org/html/2602.10071v1#bib.bib90 "Prediction of imbalance prices through gradient boosting algorithms: an application to the greek balancing market")].

#### Single-country focus

Another prominent characteristic of the literature is its strong focus on single-country markets. Balancing mechanisms may vary across regions in terms of pricing rules, reserve products, and settlement procedures, which has led most studies to concentrate on individual national markets such as Germany [[5](https://arxiv.org/html/2602.10071v1#bib.bib91 "Interpretable transformer model for capturing regime switching effects of real-time electricity prices")], UK [[9](https://arxiv.org/html/2602.10071v1#bib.bib73 "Seasonality in deep learning forecasts of electricity imbalance prices"), [12](https://arxiv.org/html/2602.10071v1#bib.bib89 "Forecasting imbalance price densities with statistical methods and neural networks")], and Ireland [[52](https://arxiv.org/html/2602.10071v1#bib.bib70 "Electricity price forecasting in the irish balancing market"), [53](https://arxiv.org/html/2602.10071v1#bib.bib85 "Optimising quantile-based trading strategies in electricity arbitrage")]. While this market-specific focus enables close alignment with local price formation rules, it also limits cross-country generalization and highlights the challenges of developing unified balancing-market forecasting models.

## IV Conclusion

This review surveyed deep learning for electricity price forecasting across day-ahead, intraday, and balancing markets through a unified perspective of backbone, head, and loss design. While day-ahead forecasting has evolved toward probabilistic, multi-market, and foundation-style models, intraday research remains sparse and is shifting toward microstructure-aware and trajectory-based forecasting. Balancing markets, by contrast, favor price-formation-aware design due to strong regime switching rules.
Future research would benefit from greater attention to intraday and balancing markets, as well as from more advanced model structures that incorporate domain knowledge and market-specific mechanisms while retaining the flexibility of data-driven learning.

## References

* [1]
  I. Agakishiev, W. K. Härdle, M. Kopa, K. Kozmik, and A. Petukhina (2025)
  Multivariate probabilistic forecasting of electricity prices with trading applications.
  Energy Economics 141,  pp. 108008.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.43.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [2]
  R. Beigaite, T. Krilavičius, and K. L. Man (2018)
  Electricity price forecasting for nord pool data.
  In 2018 International conference on platform technology and service (PlatCon),
   pp. 1–6.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.4.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p3.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px1.p1.1 "Evolution of model families ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px2.p1.1 "Preference for multi-timestep heads ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [3]
  S. Beltran, A. Castro, I. Irizar, G. Naveran, and I. Yeregui (2022)
  Framework for collaborative intelligence in forecasting day-ahead electricity price.
  Applied Energy 306,  pp. 118049.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.23.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [4]
  S. Ben Amor and F. Ziel (2026)
  Recurrent neural networks with linear structures for electricity price forecasting.
  Renewable and Sustainable Energy Reviews 231,  pp. 116773.
  External Links: ISSN 1364-0321,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.rser.2026.116773),
  [Link](https://www.sciencedirect.com/science/article/pii/S1364032126000729)
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.47.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [5]
  J. Bottieau, Y. Wang, Z. De Greve, F. Vallee, and J. Toubeau (2022)
  Interpretable transformer model for capturing regime switching effects of real-time electricity prices.
  IEEE Transactions on Power Systems 38 (3),  pp. 2162–2176.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.18.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p5.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-C](https://arxiv.org/html/2602.10071v1#S3.SS3.SSS0.Px3.p1.1 "Single-country focus ‣ III-C Balancing Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [6]
  J. Chen, S. Lerch, M. Schienle, T. Serafin, and R. Weron (2025)
  Probabilistic intraday electricity price forecasting using generative machine learning.
  External Links: 2506.00044,
  [Link](https://arxiv.org/abs/2506.00044)
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.40.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [7]
  R. A. Chinnathambi, S. J. Plathottam, T. Hossen, A. S. Nair, and P. Ranganathan (2018)
  Deep neural networks (dnn) for day-ahead electricity price markets.
  In 2018 IEEE electrical power and energy conference (EPEC),
   pp. 1–6.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.5.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p3.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px1.p1.1 "Evolution of model families ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px2.p1.1 "Preference for multi-timestep heads ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [8]
  K. Cho, B. Van Merriënboer, C. Gulcehre, D. Bahdanau, F. Bougares, H. Schwenk, and Y. Bengio (2014)
  Learning phrase representations using rnn encoder-decoder for statistical machine translation.
  arXiv preprint arXiv:1406.1078.
  Cited by: [§II-A](https://arxiv.org/html/2602.10071v1#S2.SS1.p1.1 "II-A Backbone ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [9]
  S. Deng, J. Inekwe, V. Smirnov, A. Wait, and C. Wang (2024)
  Seasonality in deep learning forecasts of electricity imbalance prices.
  Energy Economics 137,  pp. 107770.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.33.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-C](https://arxiv.org/html/2602.10071v1#S3.SS3.SSS0.Px3.p1.1 "Single-country focus ‣ III-C Balancing Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [10]
  J. Dumas, I. Boukas, M. M. de Villena, S. Mathieu, and B. Cornélusse (2019)
  Probabilistic forecasting of imbalance prices in the belgian context.
  In 2019 16th International Conference on the European Energy Market (EEM),
   pp. 1–7.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.7.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p5.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-C](https://arxiv.org/html/2602.10071v1#S3.SS3.SSS0.Px1.p1.1 "Two-stage modeling paradigms ‣ III-C Balancing Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-C](https://arxiv.org/html/2602.10071v1#S3.SS3.SSS0.Px2.p1.1 "Preference for shallow backbones ‣ III-C Balancing Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [11]
  J. L. Elman (1990)
  Finding structure in time.
  Cognitive science 14 (2),  pp. 179–211.
  Cited by: [§II-A](https://arxiv.org/html/2602.10071v1#S2.SS1.p1.1 "II-A Backbone ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [12]
  V. N. Ganesh and D. Bunn (2023)
  Forecasting imbalance price densities with statistical methods and neural networks.
  IEEE Transactions on Energy Markets, Policy and Regulation 2 (1),  pp. 30–39.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.26.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p5.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-C](https://arxiv.org/html/2602.10071v1#S3.SS3.SSS0.Px3.p1.1 "Single-country focus ‣ III-C Balancing Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [13]
  I. J. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, and Y. Bengio (2014)
  Generative adversarial nets.
  Advances in neural information processing systems 27.
  Cited by: [§II-A](https://arxiv.org/html/2602.10071v1#S2.SS1.p1.1 "II-A Backbone ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [14]
  S. Gunduz, U. Ugurlu, and I. Oksuz (2023)
  Transfer learning for electricity price forecasting.
  Sustainable Energy, Grids and Networks 34,  pp. 100996.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.29.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p5.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px2.p1.1 "Preference for multi-timestep heads ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [15]
  S. Hirsch and F. Ziel (2024)
  Multivariate simulation-based forecasting for intraday power markets: modeling cross-product price effects.
  Applied Stochastic Models in Business and Industry 40 (6),  pp. 1571–1595.
  Cited by: [§III-B](https://arxiv.org/html/2602.10071v1#S3.SS2.SSS0.Px3.p1.1 "Limited accessibility and synthetic data ‣ III-B Intraday Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [16]
  S. Hirsch and F. Ziel (2024)
  Simulation-based forecasting for intraday power markets: modelling fundamental drivers for location, shape and scale of the price distribution.
  The Energy Journal 45 (3),  pp. 87–124.
  Cited by: [§III-B](https://arxiv.org/html/2602.10071v1#S3.SS2.SSS0.Px2.p1.1 "From single-index prediction to trajectory forecasting ‣ III-B Intraday Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [17]
  S. Hochreiter and J. Schmidhuber (1997)
  Long short-term memory.
  Neural computation 9 (8),  pp. 1735–1780.
  Cited by: [§II-A](https://arxiv.org/html/2602.10071v1#S2.SS1.p1.1 "II-A Backbone ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [18]
  T. Hong, P. Pinson, Y. Wang, R. Weron, D. Yang, and H. Zareipour (2020)
  Energy forecasting: a review and outlook.
  IEEE Open Access Journal of Power and Energy 7,  pp. 376–388.
  Cited by: [§I](https://arxiv.org/html/2602.10071v1#S1.p4.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [19]
  T. Hornek, S. P. Menci, and I. Pavić (2025)
  Directional price forecasting in the continuous intraday market under consideration of neighboring products and limit order books.
  ACM SIGENERGY Energy Informatics Review 5 (3),  pp. 77–92.
  Cited by: [§III-B](https://arxiv.org/html/2602.10071v1#S3.SS2.SSS0.Px3.p1.1 "Limited accessibility and synthetic data ‣ III-B Intraday Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [20]
  M. H. Imani, E. Bompard, P. Colella, and T. Huang (2021)
  Forecasting electricity price in different time horizons: an application to the italian electricity market.
  IEEE Transactions on Industry Applications 57 (6),  pp. 5726–5736.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.17.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [21]
  A. Jędrzejewski, J. Lago, G. Marcjasz, and R. Weron (2022)
  Electricity price forecasting: the dawn of machine learning.
  IEEE Power and Energy Magazine 20 (3),  pp. 24–31.
  Cited by: [§I](https://arxiv.org/html/2602.10071v1#S1.p4.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [22]
  H. Jiang, S. Pan, Y. Dong, and J. Wang (2024)
  Probabilistic electricity price forecasting based on penalized temporal fusion transformer.
  Journal of Forecasting 43 (5),  pp. 1465–1491.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.34.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p3.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p5.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px1.p1.1 "Evolution of model families ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px3.p1.1 "Shift from pointwise to probabilistic setting ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [23]
  L. Jiang and G. Hu (2018)
  A review on short-term electricity price forecasting techniques for energy markets.
  In 2018 15th International Conference on Control, Automation, Robotics and Vision (ICARCV),
   pp. 937–944.
  Cited by: [§I](https://arxiv.org/html/2602.10071v1#S1.p4.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [24]
  O. A. Karabiber and G. Xydis (2019)
  Electricity price forecasting in the danish day-ahead market using the tbats, ann and arima methods.
  Energies 12 (5),  pp. 928.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.8.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p3.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px1.p1.1 "Evolution of model families ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px2.p1.1 "Preference for multi-timestep heads ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px3.p1.1 "Shift from pointwise to probabilistic setting ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [25]
  D. P. Kingma and M. Welling (2013)
  Auto-encoding variational bayes.
  arXiv preprint arXiv:1312.6114.
  Cited by: [§II-A](https://arxiv.org/html/2602.10071v1#S2.SS1.p1.1 "II-A Backbone ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [26]
  T. Kipf (2016)
  Semi-supervised classification with graph convolutional networks.
  arXiv preprint arXiv:1609.02907.
  Cited by: [§II-A](https://arxiv.org/html/2602.10071v1#S2.SS1.p1.1 "II-A Backbone ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [27]
  D. K. Kılıç, P. Nielsen, and A. Thibbotuwawa (2024)
  Intraday electricity price forecasting via lstm and trading strategy for the power market: a case study of the west denmark dk1 grid region.
  Energies 17 (12),  pp. 2909.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.31.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p5.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-B](https://arxiv.org/html/2602.10071v1#S3.SS2.SSS0.Px1.p1.1 "From macro-level features to microstructure ‣ III-B Intraday Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-B](https://arxiv.org/html/2602.10071v1#S3.SS2.SSS0.Px2.p1.1 "From single-index prediction to trajectory forecasting ‣ III-B Intraday Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [28]
  J. Lago, F. De Ridder, and B. De Schutter (2018)
  Forecasting spot electricity prices: deep learning approaches and empirical comparison of traditional algorithms.
  Applied Energy 221,  pp. 386–405.
  External Links: ISSN 0306-2619,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.apenergy.2018.02.069),
  [Link](https://www.sciencedirect.com/science/article/pii/S030626191830196X)
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.2.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p3.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px1.p1.1 "Evolution of model families ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px3.p1.1 "Shift from pointwise to probabilistic setting ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [29]
  J. Lago, G. Marcjasz, B. De Schutter, and R. Weron (2021)
  Forecasting day-ahead electricity prices: a review of state-of-the-art algorithms, best practices and an open-access benchmark.
  Applied Energy 293,  pp. 116983.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.16.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p3.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [30]
  J. Lago, G. Marcjasz, B. De Schutter, and R. Weron (2021)
  Forecasting day-ahead electricity prices: a review of state-of-the-art algorithms, best practices and an open-access benchmark.
  Applied Energy 293,  pp. 116983.
  Cited by: [§I](https://arxiv.org/html/2602.10071v1#S1.p4.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [31]
  V. Laitsos, G. Vontzos, D. Bargiotas, A. Daskalopulu, and L. H. Tsoukalas (2024)
  Data-driven techniques for short-term electricity price forecasting through novel deep learning approaches with attention mechanisms.
  Energies 17 (7),  pp. 1625.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.38.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [32]
  Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner (2002)
  Gradient-based learning applied to document recognition.
  Proceedings of the IEEE 86 (11),  pp. 2278–2324.
  Cited by: [§II-A](https://arxiv.org/html/2602.10071v1#S2.SS1.p1.1 "II-A Backbone ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [33]
  S. Li, X. Jin, Y. Xuan, X. Zhou, W. Chen, Y. Wang, and X. Yan (2019)
  Enhancing the locality and breaking the memory bottleneck of transformer on time series forecasting.
  Advances in neural information processing systems 32.
  Cited by: [§II-A](https://arxiv.org/html/2602.10071v1#S2.SS1.p1.1 "II-A Backbone ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [34]
  W. Li and D. M. Becker (2021)
  Day-ahead electricity price prediction applying hybrid models of lstm-based deep learning methods and feature selection algorithms under consideration of market coupling.
  Energy 237,  pp. 121543.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.15.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p3.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px2.p1.1 "Preference for multi-timestep heads ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px3.p1.1 "Shift from pointwise to probabilistic setting ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [35]
  Z. Liu, Y. Wang, S. Vaidya, F. Ruehle, J. Halverson, M. Soljačić, T. Y. Hou, and M. Tegmark (2024)
  Kan: kolmogorov-arnold networks.
  arXiv preprint arXiv:2404.19756.
  Cited by: [§II-A](https://arxiv.org/html/2602.10071v1#S2.SS1.p1.1 "II-A Backbone ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [36]
  K. Maciejowska, A. Lipiecki, and B. Uniejewski (2025)
  Statistical and economic evaluation of forecasts in electricity markets: beyond rmse and mae.
  External Links: 2511.13616,
  [Link](https://arxiv.org/abs/2511.13616)
  Cited by: [§II-C](https://arxiv.org/html/2602.10071v1#S2.SS3.p6.1 "II-C Loss Function ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [37]
  K. Maciejowska and J. Nowotarski (2016)
  A hybrid model for gefcom2014 probabilistic electricity price forecasting.
  International Journal of Forecasting 32 (3),  pp. 1051–1056.
  External Links: ISSN 0169-2070,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.ijforecast.2015.11.008)
  Cited by: [§II-B](https://arxiv.org/html/2602.10071v1#S2.SS2.p3.1 "II-B Head ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [38]
  B. E. Mahtout and F. Ziel (2026)
  Electricity price forecasting: bridging linear models, neural networks and online learning.
  arXiv preprint arXiv:2601.02856.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.48.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [39]
  G. Marcjasz, J. Lago, and R. Weron (2020)
  Neural networks in day-ahead electricity price forecasting: single vs. multiple outputs.
  arXiv preprint arXiv:2008.08006.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.13.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [40]
  G. Marcjasz, M. Narajewski, R. Weron, and F. Ziel (2023)
  Distributional neural networks for electricity price forecasting.
  Energy Economics 125,  pp. 106843.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.27.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p5.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px3.p1.1 "Shift from pointwise to probabilistic setting ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [41]
  G. Marcjasz, T. Serafin, and R. Weron (2023)
  Trading on short-term path forecasts of intraday electricity prices. part ii–distributional deep neural networks.
  Technical report
   Department of Operations Research and Business Intelligence, Wroclaw ….
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.25.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p5.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§II-B](https://arxiv.org/html/2602.10071v1#S2.SS2.p3.1 "II-B Head ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-B](https://arxiv.org/html/2602.10071v1#S3.SS2.SSS0.Px2.p1.1 "From single-index prediction to trajectory forecasting ‣ III-B Intraday Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-B](https://arxiv.org/html/2602.10071v1#S3.SS2.SSS0.Px3.p1.1 "Limited accessibility and synthetic data ‣ III-B Intraday Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [42]
  G. Marcjasz, B. Uniejewski, and R. Weron (2019)
  On the importance of the long-term seasonal component in day-ahead electricity price forecasting with narx neural networks.
  International Journal of Forecasting 35 (4),  pp. 1520–1532.
  External Links: ISSN 0169-2070,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.ijforecast.2017.11.009),
  [Link](https://www.sciencedirect.com/science/article/pii/S0169207017301401)
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.9.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [43]
  G. Marcjasz, B. Uniejewski, and R. Weron (2020)
  Probabilistic electricity price forecasting with narx networks: combine point or probabilistic forecasts?.
  International Journal of Forecasting 36 (2),  pp. 466–479.
  External Links: ISSN 0169-2070,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.ijforecast.2019.07.002),
  [Link](https://www.sciencedirect.com/science/article/pii/S0169207019301979)
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.14.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p3.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px3.p1.1 "Shift from pointwise to probabilistic setting ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [44]
  R. A. d. Marcos, D. W. Bunn, A. Bello, and J. Reneses (2020)
  Short-term electricity price forecasting with recurrent regimes and structural breaks.
  Energies 13 (20),  pp. 5452.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.12.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [45]
  A. Meng, P. Wang, G. Zhai, C. Zeng, S. Chen, X. Yang, and H. Yin (2022)
  Electricity price forecasting with high penetration of renewable energy using attention-based lstm network trained by crisscross optimization.
  Energy 254,  pp. 124212.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.22.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p3.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px1.p1.1 "Evolution of model families ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [46]
  A. Meng, J. Zhu, B. Yan, and H. Yin (2024)
  Day-ahead electricity price prediction in multi-price zones based on multi-view fusion spatio-temporal graph neural network.
  Applied Energy 369,  pp. 123553.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.37.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p3.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px1.p1.1 "Evolution of model families ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [47]
  H. Mubarak, A. Abdellatif, S. Ahmad, M. Z. Islam, S. Muyeen, M. A. Mannan, and I. Kamwa (2024)
  Day-ahead electricity price forecasting using a cnn-bilstm model in conjunction with autoregressive modeling and hyperparameter optimization.
  International Journal of Electrical Power & Energy Systems 161,  pp. 110206.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.39.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [48]
  M. Narajewski (2022)
  Probabilistic forecasting of german electricity imbalance prices.
  Energies 15 (14),  pp. 4976.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.19.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p5.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-C](https://arxiv.org/html/2602.10071v1#S3.SS3.SSS0.Px1.p1.1 "Two-stage modeling paradigms ‣ III-C Balancing Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [49]
  W. Nitka and R. Weron (2023)
  Combining predictive distributions of electricity prices: does minimizing the crps lead to optimal decisions in day-ahead bidding?.
  arXiv preprint arXiv:2308.15443.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.30.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [50]
  J. Nowotarski and R. Weron (2018)
  Recent advances in electricity price forecasting: a review of probabilistic forecasting.
  Renewable and Sustainable Energy Reviews 81,  pp. 1548–1568.
  Cited by: [§I](https://arxiv.org/html/2602.10071v1#S1.p4.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [51]
  C. O’Connor, M. Bahloul, S. Prestwich, and A. Visentin (2025)
  A review of electricity price forecasting models in the day-ahead, intra-day, and balancing markets.
  Energies 18 (12),  pp. 3097.
  Cited by: [§I](https://arxiv.org/html/2602.10071v1#S1.p4.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [52]
  C. O’Connor, J. Collins, S. Prestwich, and A. Visentin (2024)
  Electricity price forecasting in the irish balancing market.
  Energy Strategy Reviews 54,  pp. 101436.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.32.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p5.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-C](https://arxiv.org/html/2602.10071v1#S3.SS3.SSS0.Px2.p1.1 "Preference for shallow backbones ‣ III-C Balancing Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-C](https://arxiv.org/html/2602.10071v1#S3.SS3.SSS0.Px3.p1.1 "Single-country focus ‣ III-C Balancing Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [53]
  C. O’Connor, J. Collins, S. Prestwich, and A. Visentin (2025)
  Optimising quantile-based trading strategies in electricity arbitrage.
  Energy and AI 20,  pp. 100476.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.42.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p5.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-C](https://arxiv.org/html/2602.10071v1#S3.SS3.SSS0.Px1.p1.1 "Two-stage modeling paradigms ‣ III-C Balancing Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-C](https://arxiv.org/html/2602.10071v1#S3.SS3.SSS0.Px2.p1.1 "Preference for shallow backbones ‣ III-C Balancing Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-C](https://arxiv.org/html/2602.10071v1#S3.SS3.SSS0.Px3.p1.1 "Single-country focus ‣ III-C Balancing Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [54]
  I. Oksuz and U. Ugurlu (2019)
  Neural network based model comparison for intraday electricity price forecasting.
  Energies 12 (23),  pp. 4557.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.6.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p5.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-B](https://arxiv.org/html/2602.10071v1#S3.SS2.SSS0.Px1.p1.1 "From macro-level features to microstructure ‣ III-B Intraday Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-B](https://arxiv.org/html/2602.10071v1#S3.SS2.SSS0.Px2.p1.1 "From single-index prediction to trajectory forecasting ‣ III-B Intraday Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [55]
  K. G. Olivares, C. Challu, G. Marcjasz, R. Weron, and A. Dubrawski (2023)
  Neural basis expansion analysis with exogenous variables: forecasting electricity prices with nbeatsx.
  International Journal of Forecasting 39 (2),  pp. 884–900.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.28.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p5.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px2.p1.1 "Preference for multi-timestep heads ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [56]
  K. Plakas, N. Andriopoulos, D. Papadaskalopoulos, A. Birbas, E. Housos, and I. Moraitis (2025)
  Prediction of imbalance prices through gradient boosting algorithms: an application to the greek balancing market.
  IEEE Access.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.41.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-C](https://arxiv.org/html/2602.10071v1#S3.SS3.SSS0.Px2.p1.1 "Preference for shallow backbones ‣ III-C Balancing Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [57]
  Y. Qin, D. Song, H. Chen, W. Cheng, G. Jiang, and G. Cottrell (2017)
  A dual-stage attention-based recurrent neural network for time series prediction.
  arXiv preprint arXiv:1704.02971.
  Cited by: [§II-A](https://arxiv.org/html/2602.10071v1#S2.SS1.p1.1 "II-A Backbone ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [58]
  D. E. Rumelhart, G. E. Hinton, and R. J. Williams (1986)
  Learning representations by back-propagating errors.
  nature 323 (6088),  pp. 533–536.
  Cited by: [§II-A](https://arxiv.org/html/2602.10071v1#S2.SS1.p1.1 "II-A Backbone ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [59]
  S. Schnürch and A. Wagner (2020-05)
  Electricity price forecasting with neural networks on epex order books.
  Applied Mathematical Finance 27 (3),  pp. 189–206.
  External Links: ISSN 1466-4313,
  [Link](http://dx.doi.org/10.1080/1350486X.2020.1805337),
  [Document](https://dx.doi.org/10.1080/1350486x.2020.1805337)
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.11.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [60]
  T. Serafin, B. Uniejewski, and R. Weron (2019)
  Averaging predictive distributions across calibration windows for day-ahead electricity price forecasting.
  Energies 12 (13).
  External Links: ISSN 1996-1073,
  [Document](https://dx.doi.org/10.3390/en12132561)
  Cited by: [§II-B](https://arxiv.org/html/2602.10071v1#S2.SS2.p3.1 "II-B Head ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [61]
  N. Shazeer, A. Mirhoseini, K. Maziarz, A. Davis, Q. Le, G. Hinton, and J. Dean (2017)
  Outrageously large neural networks: the sparsely-gated mixture-of-experts layer.
  arXiv preprint arXiv:1701.06538.
  Cited by: [§II-A](https://arxiv.org/html/2602.10071v1#S2.SS1.p1.1 "II-A Backbone ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [62]
  W. Shi and Y. F. Wang (2024)
  A robust electricity price forecasting framework based on heteroscedastic temporal convolutional network.
  International Journal of Electrical Power & Energy Systems 161,  pp. 110177.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.36.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p5.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px3.p1.1 "Shift from pointwise to probabilistic setting ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [63]
  L. Tschora, E. Pierre, M. Plantevit, and C. Robardet (2022)
  Electricity price forecasting on the day-ahead market using machine learning.
  Applied Energy 313,  pp. 118752.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.20.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px2.p1.1 "Preference for multi-timestep heads ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [64]
  U. Ugurlu, I. Oksuz, and O. Tas (2018)
  Electricity price forecasting using recurrent neural networks.
  Energies 11 (5).
  External Links: [Link](https://www.mdpi.com/1996-1073/11/5/1255),
  ISSN 1996-1073,
  [Document](https://dx.doi.org/10.3390/en11051255)
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.3.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p3.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px1.p1.1 "Evolution of model families ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px2.p1.1 "Preference for multi-timestep heads ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px3.p1.1 "Shift from pointwise to probabilistic setting ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [65]
  G. Vamathevan, M. F. Dynge, and Ü. Cali (2022)
  Electricity price forecasting for norwegian day-ahead market using hybrid ai models.
  In 2022 18th International Conference on the European Energy Market (EEM),
   pp. 1–6.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.24.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [66]
  A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin (2017)
  Attention is all you need.
  Advances in neural information processing systems 30.
  Cited by: [§II-A](https://arxiv.org/html/2602.10071v1#S2.SS1.p1.1 "II-A Backbone ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [67]
  R. Weron (2014)
  Electricity price forecasting: a review of the state-of-the-art with a look into the future.
  International journal of forecasting 30 (4),  pp. 1030–1081.
  Cited by: [§I](https://arxiv.org/html/2602.10071v1#S1.p4.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [68]
  W. Yan, P. Wang, R. Xu, R. Han, E. Chen, Y. Han, and X. Zhang (2025)
  A novel mid-and long-term time-series forecasting framework for electricity price based on hierarchical recurrent neural networks.
  Journal of the Franklin Institute 362 (6),  pp. 107590.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.44.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [69]
  Y. Yang, J. Guo, Y. Li, and J. Zhou (2024)
  Forecasting day-ahead electricity prices with spatial dependence.
  International Journal of Forecasting 40 (3),  pp. 1255–1270.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.35.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p3.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px1.p1.1 "Evolution of model families ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [70]
  R. Yu, C. Gu, J. Stiasny, Q. Wen, W. S. Dilov, L. Qi, and J. L. Cremer (2025)
  PriceFM: foundation model for probabilistic electricity price forecasting.
  External Links: 2508.04875,
  [Link](https://arxiv.org/abs/2508.04875)
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.49.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p3.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§II-B](https://arxiv.org/html/2602.10071v1#S2.SS2.p3.1 "II-B Head ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px1.p1.1 "Evolution of model families ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-A](https://arxiv.org/html/2602.10071v1#S3.SS1.SSS0.Px2.p1.1 "Preference for multi-timestep heads ‣ III-A Day-Ahead Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [71]
  R. Yu, Y. Tao, F. Leimgruber, T. Esterl, J. Stiasny, D. W. Bunn, Q. Wen, H. Guo, and J. L. Cremer (2026)
  OrderFusion: encoding orderbook for end-to-end probabilistic intraday electricity price forecasting.
  External Links: 2502.06830,
  [Link](https://arxiv.org/abs/2502.06830)
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.46.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p5.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§II-B](https://arxiv.org/html/2602.10071v1#S2.SS2.p3.1 "II-B Head ‣ II Deep Learning Components ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-B](https://arxiv.org/html/2602.10071v1#S3.SS2.SSS0.Px1.p1.1 "From macro-level features to microstructure ‣ III-B Intraday Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-B](https://arxiv.org/html/2602.10071v1#S3.SS2.SSS0.Px3.p1.1 "Limited accessibility and synthetic data ‣ III-B Intraday Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [72]
  R. Yu, R. Wu, Y. Han, and J. L. Cremer (2026)
  Orderbook feature learning and asymmetric generalization in intraday electricity markets.
  External Links: 2510.12685,
  [Link](https://arxiv.org/abs/2510.12685)
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.45.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§I](https://arxiv.org/html/2602.10071v1#S1.p5.1 "I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-B](https://arxiv.org/html/2602.10071v1#S3.SS2.SSS0.Px1.p1.1 "From macro-level features to microstructure ‣ III-B Intraday Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets"),
  [§III-B](https://arxiv.org/html/2602.10071v1#S3.SS2.SSS0.Px3.p1.1 "Limited accessibility and synthetic data ‣ III-B Intraday Market ‣ III Trends in Electricity Price Forecasting ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [73]
  F. Zhang, H. Fleyeh, and C. Bales (2022)
  A hybrid model based on bidirectional long short-term memory neural network and catboost for short-term electricity spot price forecasting.
  Journal of the Operational Research Society 73 (2),  pp. 301–325.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.21.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").
* [74]
  F. Zhang and H. Fleyeh (2019)
  Short term electricity spot price forecasting using catboost and bidirectional long short term memory neural network.
  In 2019 16th International Conference on the European Energy Market (EEM),
   pp. 1–6.
  Cited by: [TABLE I](https://arxiv.org/html/2602.10071v1#S1.T1.1.10.2.1.1 "In I Introduction ‣ Deep Learning for Electricity Price Forecasting: A Review of Day-Ahead, Intraday, and Balancing Electricity Markets").