---
authors:
- Xu Zhang
- Zhengang Huang
- Yunzhi Wu
- Xun Lu
- Erpeng Qi
- Yunkai Chen
- Zhongya Xue
- Qitong Wang
- Peng Wang
- Wei Wang
doc_id: arxiv:2511.08622v1
family_id: arxiv:2511.08622
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Multi-period Learning for Financial Time Series Forecasting
url_abs: http://arxiv.org/abs/2511.08622v1
url_html: https://arxiv.org/html/2511.08622v1
venue: arXiv q-fin
version: 1
year: 2025
---


Xu Zhang
School of Computer Science
  
Fudan UniversityShanghaiChina
[xuzhang22@m.fudan.edu.cn](mailto:xuzhang22@m.fudan.edu.cn)
, 
Zhengang Huang
Ant GroupShanghaiChina
[huangzhengang.hzg@antgroup.com](mailto:huangzhengang.hzg@antgroup.com)
, 
Yunzhi Wu
School of Computer Science
  
Fudan UniversityShanghaiChina
[yzwu22@m.fudan.edu.cn](mailto:yzwu22@m.fudan.edu.cn)
, 
Xun Lu
Ant GroupShanghaiChina
[hilber.lx@antgroup.com](mailto:hilber.lx@antgroup.com)
, 
Erpeng Qi
Ant GroupShanghaiChina
[erpeng.qep@antgroup.com](mailto:erpeng.qep@antgroup.com)
, 
Yunkai Chen
Ant GroupShanghaiChina
[chenyunkai.cyk@antgroup.com](mailto:chenyunkai.cyk@antgroup.com)
, 
Zhongya Xue
Ant GroupShanghaiChina
[zhongya.xzy@antgroup.com](mailto:zhongya.xzy@antgroup.com)
, 
Qitong Wang
Universite Paris CiteParisFrance
[qitong.wang@u-paris.fr](mailto:qitong.wang@u-paris.fr)
, 
Peng Wang
School of Computer Science
  
Fudan UniversityShanghaiChina
[pengwang5@fudan.edu.cn](mailto:pengwang5@fudan.edu.cn)
 and 
Wei Wang
School of Computer Science
  
Fudan UniversityShanghaiChina
[weiwang1@fudan.edu.cn](mailto:weiwang1@fudan.edu.cn)

(2025)

###### Abstract.

Time series forecasting is important in finance domain. Financial time series (TS) patterns are influenced by both short-term public opinions and medium-/long-term policy and market trends. Hence, processing multi-period inputs becomes crucial for accurate financial time series forecasting (TSF).
However, current TSF models either use only single-period input, or lack customized designs for addressing multi-period characteristics. In this paper, we propose a Multi-period Learning Framework (MLF) to enhance financial TSF performance.
MLF considers both TSF’s accuracy and efficiency requirements. Specifically, we design three new modules to better integrate the multi-period inputs for improving accuracy: (i) Inter-period Redundancy Filtering (IRF), that removes the information redundancy between periods for accurate self-attention modeling, (ii) Learnable Weighted-average Integration (LWI), that effectively integrates multi-period forecasts, (iii) Multi-period self-Adaptive Patching (MAP), that mitigates the bias towards certain periods by setting the same number of patches across all periods. Furthermore, we propose a Patch Squeeze module to reduce the number of patches
in self-attention modeling for maximized efficiency.
MLF incorporates multiple inputs with varying lengths (periods) to achieve better accuracy and reduces the costs of selecting input lengths during training.
The codes and datasets are available at <https://github.com/Meteor-Stars/MLF>.

time series forecasting; deep learning; financial sales; multi-periods; multi-scales; spatio-temporal data mining

††journalyear: 2025††copyright: acmlicensed††conference: Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.1; August 3–7, 2025; Toronto, ON, Canada††booktitle: Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.1 (KDD ’25), August 3–7, 2025, Toronto, ON, Canada††doi: 10.1145/3690624.3709422††isbn: 979-8-4007-1245-6/25/08††ccs: Information systems Spatial-temporal systems††ccs: Computing methodologies Artificial intelligence

## 1. Introduction

Time series forecasting (TSF) is a critical task in the finance industry (Sezer et al., [2020](https://arxiv.org/html/2511.08622v1#bib.bib24); Krollner et al., [2010](https://arxiv.org/html/2511.08622v1#bib.bib17); Zhang et al., [2024b](https://arxiv.org/html/2511.08622v1#bib.bib39); Tang et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib28)).
For example, Alipay is a well-known App
that offers convenient digital payment and investment services  (Zhang et al., [2024a](https://arxiv.org/html/2511.08622v1#bib.bib40), [2018](https://arxiv.org/html/2511.08622v1#bib.bib41); Zang et al., [2023](https://arxiv.org/html/2511.08622v1#bib.bib36); Chen et al., [2019](https://arxiv.org/html/2511.08622v1#bib.bib4)).
Fund sales forecasting is used in financial services of Alipay App to manage the inventory of different fund products.
Accurate inventory management is not only crucial for ensuring sufficient availability of various fund products on the Alipay App, but also for aiding fund institutions in investment preparation and risk management.
Moreover, TSF models need to be daily retrained and inferred to accommodate new data for the most accurate fund sales forecasting.
Therefore, not only accuracy, but also the efficiency of the TSF model are crucial for real-world financial applications.

One of the key characteristics of financial TS is that their temporal patterns are influenced by different information from multiple periods of historical data (i.e., TS with multiple lengths)  (Chen et al., [2016](https://arxiv.org/html/2511.08622v1#bib.bib5); Zeng, [2008](https://arxiv.org/html/2511.08622v1#bib.bib38); Gu and Xu, [2021](https://arxiv.org/html/2511.08622v1#bib.bib12); Tran et al., [2019](https://arxiv.org/html/2511.08622v1#bib.bib30)).
For instance, the sales of fund products
are affected not only by short-term public opinions and the company’s operational conditions, but also by medium-/long-term policies and market trends.
We also found this phenomenon in our experiments.
In the scenario of fund sales forecasting, Table [1](https://arxiv.org/html/2511.08622v1#S1.T1 "Table 1 ‣ 1. Introduction ‣ Multi-period Learning for Financial Time Series Forecasting") indicates that there is no single period input that can provide the best predictions.
Specifically, 33.53% samples are best forecasted using the short-period input (PTST5), 27.35% using medium-period input (PTST10) and 39.12% using long-period input (PTST30), respectively.
These uniform ratios suggest that choosing a single fixed period will result in suboptimal forecasting accuracy.
For this situation, a simple solution might be to select appropriate input lengths for different forecasting legnths during training, but this leads to high overhead and may not be accurate enough.

Table 1. MSE (Mean Squared Error; lower is better) of a single-step TSF under various input lengths nn (representing different periods) on the Alipay Fund dataset.
PTST5 refers to a PatchTST (Nie et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib21)) model trained on inputs of length n=5n=5.
κ=m​e​a​n​((Xh−Xf)2)\kappa=mean((X\_{h}-X\_{f})^{2}) quantifies the consistency between historical windows XhX^{h} (30 time steps) and the forecasted value XfX^{f}.
A higher κ\kappa indicates sharper pattern fluctuations.

| Data Subset Ratios | MSE | | | Distribution |
| --- | --- | --- | --- | --- |
| PTST5 | PTST10 | PTST30 | Consistency κ\kappa |
| 33.53%, best by PTST5 | 49.28 | 54.85 | 63.31 | 60.64 |
| 27.35%, best by PTST10 | 12.34 | 8.92 | 13.57 | 22.46 |
| 39.12%, best by PTST30 | 14.56 | 12.23 | 7.34 | 14.82 |

Further analyzing the temporal pattern, we found 33.53% samples, best predicted by short-period input, tend to have sharply fluctuating future values.
This is evidenced by the highest κ\kappa=60.64.
In contrast, the remaining 27.35% and 39.12% samples, best predicted by medium- and long-period inputs, have relatively smooth future values as they show lower κ\kappa=22.46 and 14.82, respectively.
This can be interpreted in the financial domain that short-term hot public topics lead to urgent fund transactions, while medium-/long-term global policies and market trends have a bigger impact on the steady trend of fund sales.
Hence, short-period inputs are tightly correlated with future fluctuations, while medium- and long-period inputs are more associated with future steady trends.
This explains why different periods work best at predicting different samples in Table [1](https://arxiv.org/html/2511.08622v1#S1.T1 "Table 1 ‣ 1. Introduction ‣ Multi-period Learning for Financial Time Series Forecasting").
In fact, future values
can consist of both sharp fluctuations and smooth trends.
In this case, even selecting appropriate input lengths in advance for different prediction lengths cannot address the issue.
Hence, considering the multi-period inputs simultaneously is crucial for accurate financial TSF.

Recently, several architectures have been proposed for TSF task, including transformer-based Scaleformer (Shabani et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib25)), PatchTST (Nie et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib21)) and Pathformer (Chen et al., [2024](https://arxiv.org/html/2511.08622v1#bib.bib6)), as well as linear model-based NHits (Challu et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib3)), TSmixer (Chen et al., [2023](https://arxiv.org/html/2511.08622v1#bib.bib7)) and TiDE (Das et al., [2023](https://arxiv.org/html/2511.08622v1#bib.bib10)).
These models show promising accuracy in the TSF task, but their designs only consider the single-period input (TS with a fixed length), as shown in Figure [1](https://arxiv.org/html/2511.08622v1#S1.F1 "Figure 1 ‣ 1. Introduction ‣ Multi-period Learning for Financial Time Series Forecasting")(a).
On one hand, this leads to the need to select appropriate input lengths for different prediction lengths, resulting in high training overhead. On the other hand, as analyzed above, future values may contain both sharp fluctuations and stable trends, which requires joint predictions using inputs of different lengths.
Although FiLM (Zhou et al., [2022a](https://arxiv.org/html/2511.08622v1#bib.bib42)) considers the multi-period inputs, it just linearly integrates multi-period outputs
without any specific architecture designs for multi-period characteristics.
We discuss one multi-period property in the right of Figure [1](https://arxiv.org/html/2511.08622v1#S1.F1 "Figure 1 ‣ 1. Introduction ‣ Multi-period Learning for Financial Time Series Forecasting")(b).
As longer-period inputs inherently contain shorter-period inputs, there is information redundancy among different periods.
If not well processed, this inter-period redundancy may have adverse effects on model training.
For example, it can cause self-attention to overfocus on the information of repetitive parts among different periods, leaving the other parts underutilized.
Hence, in our TSF scheme,
TSF model not only takes multi-period inputs, but also embrace customized designs to address the multi-period characteristics, as shown in the left of Figure [1](https://arxiv.org/html/2511.08622v1#S1.F1 "Figure 1 ‣ 1. Introduction ‣ Multi-period Learning for Financial Time Series Forecasting")(b).
To our knowledge, such multi-period based TSF model is rarely explored.

![Refer to caption](figure/multi_scale_inputs_0701v2.jpg)

Figure 1. Current TSF scheme (a) and ours (b). The blue rectangle highlights the characteristics of the multi-period inputs.

In this paper, we introduce MLF (Multi-period Learning Framework) for accurate financial TSF.
MLF is designed to effectively utilize the diverse information across
multi-period inputs.
However, it is nontrivial to integrate multi-period inputs, which
presents challenges in accuracy and efficiency.
First, how to address the characteristics of multi-period inputs to effectively integrate multi-period information for forecasting is a key challenge (integration challenge).
Second, compared to single-period inputs in Figure [1](https://arxiv.org/html/2511.08622v1#S1.F1 "Figure 1 ‣ 1. Introduction ‣ Multi-period Learning for Financial Time Series Forecasting")(a),
multi-period inputs in Figure [1](https://arxiv.org/html/2511.08622v1#S1.F1 "Figure 1 ‣ 1. Introduction ‣ Multi-period Learning for Financial Time Series Forecasting")(b)
will significantly increase the computational and memory usage of the model.
Therefore,
how to enhance the efficiency of multi-period based models while maintaining improved accuracy is another challenge (efficiency challenge).
To address the integration challenge, we introduce three new designs into the transformer architecture: (i) Inter-period Redundancy Filtering (IRF) block to eliminate the inter-period information redundancy,
(ii) Learnable Weighted-average Integration (LWI) module to effectively integrate the final multi-period forecasts,
(iii) Multi-period self-Adaptive Patching (MAP) module to set the same number of patches for all periods.
To tackle the efficiency challenge, we propose a Patch-Squeeze module to reduce input length by removing redundancy within each single period (i.e., intra-period redundancy).
Specifically, the motivation of integration design (i) is that redundancy naturally exists between different periods.
Due to similar segments having higher correlations, this redundancy may cause the self-attention to excessively focus on repetitive segments and can’t effectively utilize information in non-repetitive segments among periods for more accurate multi-period integration.
We propose an Inter-period Redundancy Filtering (IRF) block to address this issue.
For integration design (ii),
before reaching the Learnable Weighted-average Integration (LWI) module, the model’s output is still multi-period forecasts, so we need to make the final integration of them.
Considering different future positions are best forecasted by different periods,
simply averaging may lead to inaccurate integration.
Hence, we propose LWI to adaptively assign weights to different period forecasts, giving higher weights to more accurate predictions and vice versa.
Accordingly, LWI can improve the integration accuracy of multi-period forecasts.
The design intuition for integration design (iii) is that the model may have a bias towards certain periods due to they have varying numbers of patches.
This may prevent the model from fully utilizing information of all periods, thereby reducing integration accuracy.
Hence, we propose Multi-period self-Adaptive Patching (MAP) to set the same number of patches for all periods to address this issue.

Finally, employing multi-period inputs will significantly increase time and memory costs, posing challenges for scaling to large datasets and deploying in a production system.
To address the efficiency challenge, we design a Patch-Squeeze module to reduce the number of patches within each period.
Patch-Squeeze is based on a key observation, originally from the TS self-supervised learning tasks, that a few numbers of patches are sufficient in reconstructing a much larger set of masked patches (Shao et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib26)).
This can be interpreted as there exists intra-period information redundancy.
Hence, reducing intra-period redundancy, i.e., reducing the number of patches within each period, can improve model efficiency without compromising accuracy.

In summary, compared to existing methods, MLF processes multiple inputs of different lengths to enhance prediction accuracy, considering both accuracy and efficiency. Our contributions are as follows:

1. (1)

   We introduce MLF, a new Multi-period Learning Framework for financial TSF. MLF incorporates multiple inputs with varying lengths (periods) to achieve better accuracy, and one benefit is reducing the costs of selecting input lengths for different prediction lengths during training.
2. (2)

   We propose three new architecture designs to better integrate the multi-period inputs, namely, Multi-period self-Adaptive Patching (MAP) modules, Inter-period Redundancy Filtering (IRF) block, and Learnable Weighted-average Integration (LWI).
3. (3)

   We further propose a simple but effective Patch-Squeeze module for time dimensionality reduction, which provides high efficiency and maintain expected TSF accuracy while addressing multi-period inputs with varying lengths.
4. (4)

   We introduce a new financial dataset of fund sales collected from Ant Fortune and the Alipay App, expanding the public dataset repository and enabling a more comprehensive evaluation of TSF models.
5. (5)

   Our experimental results indicate that MLF outperforms advanced TSF baselines in terms of accuracy and efficiency on both collected fund and public datasets.
   The deployment results on the Alipay App further confirms MLF’s effectiveness.

## 2. Related Work and Preliminary

### 2.1. Time Series Forecasting (TSF)

#### 2.1.1. Single-period based TSF

Numerous deep learning models have been proposed by using single-period.
RNNs (Jordan, [1997](https://arxiv.org/html/2511.08622v1#bib.bib16); Elman, [1990](https://arxiv.org/html/2511.08622v1#bib.bib11); Hochreiter and Schmidhuber, [1997](https://arxiv.org/html/2511.08622v1#bib.bib13); Cho et al., [2014](https://arxiv.org/html/2511.08622v1#bib.bib9)) use recurrent structures to capture short-term temporal dependency.
Meanwhile, temporal convolutional networks (TCN) (Sen et al., [2019](https://arxiv.org/html/2511.08622v1#bib.bib23); Wu et al., [2019](https://arxiv.org/html/2511.08622v1#bib.bib35), [2020](https://arxiv.org/html/2511.08622v1#bib.bib34); Li et al., [2018](https://arxiv.org/html/2511.08622v1#bib.bib19)) employ causal and dilated convolutions for parallel computation, effectively capturing temporal dependencies in the TSF task.

The transformer (Vaswani et al., [2017](https://arxiv.org/html/2511.08622v1#bib.bib31)) has been extensively adapted for long-term TSF task (Wu et al., [2021](https://arxiv.org/html/2511.08622v1#bib.bib33); Zhou et al., [2022b](https://arxiv.org/html/2511.08622v1#bib.bib43)).
Pyraformer (Liu et al., [2021](https://arxiv.org/html/2511.08622v1#bib.bib20)) employs a multi-pass downsampling operation to capture temporal dependencies at various granularities. Scaleformer (Shabani et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib25)) further enhances Pyraformer by iteratively refining forecasts at finer scales.
Instead of using multi-pass downsampling, Pathformer (Chen et al., [2024](https://arxiv.org/html/2511.08622v1#bib.bib6)) utilizes different patch sizes to construct multiple time series and designs an adaptive pathway for improving the performance of TSF.
However, linear models like DLinear (Zeng et al., [2023](https://arxiv.org/html/2511.08622v1#bib.bib37)), TSMixer (Chen et al., [2023](https://arxiv.org/html/2511.08622v1#bib.bib7)), N-BEATS (Oreshkin et al., [2019](https://arxiv.org/html/2511.08622v1#bib.bib22)) and NHits (Challu et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib3)) have emerged to challenge the effectiveness of transformer-based methods. PatchTST (Nie et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib21)) addresses this by splitting input series into patches and learning self-attention at the patch level, achieving advanced performance in long-term TSF tasks.
This illustrates that transformers retain significant potential for TSF when appropriately tailored to the task.

Recently, Large Language Models (LLMs) have shown effectiveness in TSF tasks, particularly in scenarios requiring few training examples (few-shot learning) (Jin et al., [2023](https://arxiv.org/html/2511.08622v1#bib.bib15); Zhou et al., [2023](https://arxiv.org/html/2511.08622v1#bib.bib44)). Nonetheless, researchers also express worry about using LLMs for TSF (Tan et al., [2024](https://arxiv.org/html/2511.08622v1#bib.bib27)).

#### 2.1.2. Multi-period based TSF

To our knowledge, few TSF models are proposed to utilize multi-period inputs simultaneously to obtain more accurate TSF.
FiLM (Zhou et al., [2022a](https://arxiv.org/html/2511.08622v1#bib.bib42)) is a multi-period based method, but it just linearly integrates multi-period outputs for TSF.
Although it shows accuracy improvement for using multi-period inputs, it lacks customized designs to effectively handle their characteristics such as redundancy between periods, varying prediction effectiveness, and varying sequence lengths among periods, which suggests an opportunity for further research.

![Refer to caption](figure/multi_scale_inputs_0110.jpg)

Figure 2. Comparison between multi-period inputs in subfigure (c) and multi-scale inputs in subfigure (b).



![Refer to caption](figure/0701multi_scale_frame_work.jpg)

Figure 3. MLF and corresponding components.

#### 2.1.3. Difference between multi-period inputs and multi-scale inputs

In this paper, multi-period inputs refer to multiple original time series windows with varying input lengths, as shown in Figure [2](https://arxiv.org/html/2511.08622v1#S2.F2 "Figure 2 ‣ 2.1.2. Multi-period based TSF ‣ 2.1. Time Series Forecasting (TSF) ‣ 2. Related Work and Preliminary ‣ Multi-period Learning for Financial Time Series Forecasting")(c).
This is different from the multi-scale inputs in Pyraformer (Liu et al., [2021](https://arxiv.org/html/2511.08622v1#bib.bib20)) and Scaleformer (Shabani et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib25)), which are obtained by downsampling from the same fixed input length (Figure [2](https://arxiv.org/html/2511.08622v1#S2.F2 "Figure 2 ‣ 2.1.2. Multi-period based TSF ‣ 2.1. Time Series Forecasting (TSF) ‣ 2. Related Work and Preliminary ‣ Multi-period Learning for Financial Time Series Forecasting")(b)).
In extensive experiments, we observe that different input lengths have a significant impact on prediction accuracy. However, selecting appropriate input lengths is a crucial challenge affecting time series forecasting.

To address this, we propose MLF to extract the semantic information of short-medium-long-term individually using sequences with varying lengths, to avoid models failing to learn the different semantics under only long-term inputs, e.g., the prediction error of Pathformer and Scaleformer using long-term sequence inputs is higher than that of short-term ones.
In contrast, by directly inputting multiple windows with varying lengths, MLF can achieve good prediction accuracy, reducing the costs of selecting input windows during training.

### 2.2. Problem Definition

Given a historical multivariate TS instance 𝒳h=[x1,x2,…,xn]∈ℝn×c\mathcal{X}\_{h}=[x\_{1},x\_{2},\ldots,x\_{n}]\in\mathbb{R}^{n\times c} with length nn, the TSF task aims to predict the future mm steps 𝒳f=[xn+1,xn+2,…,xn+m]∈ℝm×c\mathcal{X}\_{f}=[x\_{n+1},x\_{n+2},...,x\_{n+m}]\in\mathbb{R}^{m\times c} for all cc variables (for simplicity, we will omit cc in the following sections).

In this paper, we focus on designing a Multi-period Learning Framework for TSF.
The multi-period inputs 𝒳h∗\mathcal{X}\_{h}^{\*} are defined as [𝒳h1,𝒳h2,…,𝒳hS][\mathcal{X}\_{h}^{1},\mathcal{X}\_{h}^{2},\ldots,\mathcal{X}\_{h}^{S}] where ss (1≤s≤S1\leq s\leq S) denotes the period index.
The multi-period input consists of multiple time series with different lengths nsn\_{s}.
A larger ss indicates a longer period, and nSn\_{S} represents the length of the longest period.

## 3. Multi-period Learning Framework (MLF)

We illustrate MLF in Figure [3](https://arxiv.org/html/2511.08622v1#S2.F3 "Figure 3 ‣ 2.1.2. Multi-period based TSF ‣ 2.1. Time Series Forecasting (TSF) ‣ 2. Related Work and Preliminary ‣ Multi-period Learning for Financial Time Series Forecasting").
First, the multi-period input passes through the Multi-period self-Adaptive Patching (MAP) module.
The input of each period is converted into the same number of patches and then linearly embedded.
Second, each period’s patch embeddings are sent to the Patch Squeeze module.
It reduces the number of patches by reducing the information redundancy within each period.
Third, the squeezed period patch embeddings are fed into the Multi-period self-Attention (MA) and Inter-period Redundancy Filtering (IRF) blocks.
IRF removes information redundancy between periods for more accurate MA modeling.
MA and IRF blocks form a MLF block.
By stacking MLF blocks, MLF progressively removes inter-period redundancy and achieves better modeling of multi-period input.
Finally, the Learnable Weighted-average Integration (LWI) module integrates multi-period forecasts from all blocks to generate the final prediction.
We will detail each design.

### 3.1. Multi-period self-Adaptive Patching (MAP)

Following the convention (Nie et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib21)), we split the multi-period input 𝒳h∗\mathcal{X}\_{h}^{\*} into patches instead of individual points as input units.

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | 𝒳ps=P​a​t​c​h​(𝒳hs,L,K),\mathcal{X}\_{p}^{s}=Patch(\mathcal{X}\_{h}^{s},L,K),\vskip-2.84544pt |  |

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | Ns=⌊(ns−L)/K⌋+2,N^{s}=\lfloor(n^{s}-L)/K\rfloor+2, |  |

where P​a​t​c​h​(⋅)Patch(\cdot) represents the patching function.
LL and KK denote the patch length and stride of the P​a​t​c​h​(⋅)Patch(\cdot) function, respectively.
The parameter KK determines the non-overlapping region between consecutive patches. Following (Nie et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib21)), we pad KK repeated numbers of the last value to the end of the original sequence before patching.
In Eq. [2](https://arxiv.org/html/2511.08622v1#S3.E2 "In 3.1. Multi-period self-Adaptive Patching (MAP) ‣ 3. Multi-period Learning Framework (MLF) ‣ Multi-period Learning for Financial Time Series Forecasting"), ⌊⋅⌋\lfloor\cdot\rfloor denotes rounding down.
P​a​t​c​h​(⋅)Patch(\cdot) transforms a time series into multiple subsequences (patches).
𝒳ps\mathcal{X}\_{p}^{s} denotes the patched period 𝒳hs\mathcal{X}\_{h}^{s}.
Each 𝒳ps∈ℝL×Ns\mathcal{X}\_{p}^{s}\in\mathbb{R}^{L\times N^{s}}, where NsN^{s} represents the number of patches in 𝒳hs\mathcal{X}\_{h}^{s}.

Eq. [1](https://arxiv.org/html/2511.08622v1#S3.E1 "In 3.1. Multi-period self-Adaptive Patching (MAP) ‣ 3. Multi-period Learning Framework (MLF) ‣ Multi-period Learning for Financial Time Series Forecasting") to Eq. [2](https://arxiv.org/html/2511.08622v1#S3.E2 "In 3.1. Multi-period self-Adaptive Patching (MAP) ‣ 3. Multi-period Learning Framework (MLF) ‣ Multi-period Learning for Financial Time Series Forecasting") depict standard multi-period patching, where different periods 𝒳hs\mathcal{X}\_{h}^{s} are patched based on fixed values of LL and KK.
As illustrated in Figure [4](https://arxiv.org/html/2511.08622v1#S3.F4 "Figure 4 ‣ 3.1. Multi-period self-Adaptive Patching (MAP) ‣ 3. Multi-period Learning Framework (MLF) ‣ Multi-period Learning for Financial Time Series Forecasting")(a), this approach results in an increase in the number of patches from short-term to long-term periods.
This disparity can lead to unequal treatment of different periods by the model, as shorter-term period inputs
may not receive adequate utilization during optimization due to fewer patches.

To address this issue of unequal treatment, we introduce Multi-period self-Adaptive Patching (MAP) module.
Illustrated in Figure [4](https://arxiv.org/html/2511.08622v1#S3.F4 "Figure 4 ‣ 3.1. Multi-period self-Adaptive Patching (MAP) ‣ 3. Multi-period Learning Framework (MLF) ‣ Multi-period Learning for Financial Time Series Forecasting")(b), MAP ensures each period 𝒳hs\mathcal{X}\_{h}^{s} contains an equal number of patches by self-adaptively adjusting patch lengths and strides.
Specifically, we set Ls=α⋅KsL^{s}=\alpha\cdot K^{s} (where α\alpha is fixed at 2 in this paper) and maintain a fixed number of patches N~\widetilde{N} across all periods.
Substituting this into Eq. [2](https://arxiv.org/html/2511.08622v1#S3.E2 "In 3.1. Multi-period self-Adaptive Patching (MAP) ‣ 3. Multi-period Learning Framework (MLF) ‣ Multi-period Learning for Financial Time Series Forecasting") and expanding, we obtain:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3) |  | N~\displaystyle\widetilde{N} | =(ns−L)/K+2\displaystyle=(n^{s}-L)/K+2 |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4) |  |  | =(ns−α⋅K)/K+2\displaystyle=(n^{s}-\alpha\cdot K)/K+2 |  |

After further expanding the formula, we can derive the self-adaptive LsL^{s} and KsK^{s} for different periods:

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | N~⋅K−α⋅K=ns−α⋅K\vskip-2.84544pt\begin{split}\widetilde{N}\cdot K-\alpha\cdot K&=n^{s}-\alpha\cdot K\\ \end{split} |  |

|  |  |  |  |
| --- | --- | --- | --- |
| (6) |  | Ks=⌊ns/N~⌋,Ls=α⋅KsK^{s}=\lfloor n^{s}/\widetilde{N}\rfloor,\ \ \ L^{s}=\alpha\cdot K^{s} |  |

Self-adaptive LsL^{s} and KsK^{s} ensure each period 𝒳hs\mathcal{X}\_{h}^{s} contains an equal number of patches, allowing the model to evenly consider the temporal information across different periods.
Substituting LsL^{s} and KsK^{s} into Eq. [1](https://arxiv.org/html/2511.08622v1#S3.E1 "In 3.1. Multi-period self-Adaptive Patching (MAP) ‣ 3. Multi-period Learning Framework (MLF) ‣ Multi-period Learning for Financial Time Series Forecasting") yields the self-adaptive patched 𝒳ps\mathcal{X}\_{p}^{s}.

Before feeding the patches of each period into the transformer encoder, they are projected into a DD-dimensional embedding space with a learnable additive position encoding (Vaswani et al., [2017](https://arxiv.org/html/2511.08622v1#bib.bib31); Nie et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib21)).
The embedded representation of 𝒳ps\mathcal{X}\_{p}^{s} is denoted as 𝒳ds\mathcal{X}\_{d}^{s} and can be formulated as:

|  |  |  |  |
| --- | --- | --- | --- |
| (7) |  | 𝒳ds=W​𝒳psps+Wp​o​ss\mathcal{X}\_{d}^{s}=W{{}\_{p}^{s}}\mathcal{X}\_{p}^{s}+W\_{pos}^{s} |  |

where each Wps∈ℝD×LsW\_{p}^{s}\in\mathbb{R}^{D\times L^{s}} and Wp​o​ss∈ℝD×NsW\_{pos}^{s}\in\mathbb{R}^{D\times N^{s}}.

![Refer to caption](figure/0613multi_scale_adaptive_patchingv2.jpg)

Figure 4. 
Illustration of the standard multi-period patching (using fixed patch lengths) and self-adaptive multi-period patching (using self-adaptively varied patch lengths).

### 3.2. Patch Squeeze

Studies of self-supervised learning for time series  (Shao et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib26)) suggest that there is information redundancy within periods.
That is, a small subset of patches can effectively capture the global temporal patterns of the entire period.
Motivated by this insight, we propose a patch squeeze module to distill essential information from the original time series data into a reduced number of patches.
This module not only substantially reduces both time complexity and memory usage, but also shows an insignificant impact on accuracy (empirically verified in Section [4.3](https://arxiv.org/html/2511.08622v1#S4.SS3 "4.3. Time Series Forecasting Efficiency ‣ 4. Experiments and Results ‣ Multi-period Learning for Financial Time Series Forecasting") and Section [4.5.3](https://arxiv.org/html/2511.08622v1#S4.SS5.SSS3 "4.5.3. Effectiveness of patch squeeze module ‣ 4.5. Ablation Study ‣ 4. Experiments and Results ‣ Multi-period Learning for Financial Time Series Forecasting")).

The patch squeeze module, illustrated in Figure [5](https://arxiv.org/html/2511.08622v1#S3.F5 "Figure 5 ‣ 3.2. Patch Squeeze ‣ 3. Multi-period Learning Framework (MLF) ‣ Multi-period Learning for Financial Time Series Forecasting"), consists of a lightweight encoder (P​a​t​c​h​E​n​cPatchEnc, implemented with one linear layer) and decoder (composed of M​L​PLsMLP\_{L}^{s} and M​L​PNsMLP\_{N}^{s}).
The outputs of the patch squeeze module, denoted as 𝒳^ps\mathcal{\hat{X}}\_{p}^{s} (used for reconstruction loss) and 𝒳^d\mathcal{\hat{X}}\_{d} (sent to the transformer encoder), are formulated as follows:

|  |  |  |  |
| --- | --- | --- | --- |
| (8) |  | 𝒳^ds=P​a​t​c​h​E​n​c​(𝒳ds,r)\mathcal{\hat{X}}\_{d}^{s}=PatchEnc(\mathcal{X}\_{d}^{s},r) |  |

|  |  |  |  |
| --- | --- | --- | --- |
| (9) |  | 𝒳^d=[𝒳^d0,⋯,𝒳^ds]\mathcal{\hat{X}}\_{d}=[\mathcal{\hat{X}}\_{d}^{0},\cdots,\mathcal{\hat{X}}\_{d}^{s}] |  |

|  |  |  |  |
| --- | --- | --- | --- |
| (10) |  | 𝒳^ps=M​L​PLs​(M​L​PNs​(𝒳^ds))\mathcal{\hat{X}}\_{p}^{s}=MLP\_{L}^{s}(MLP\_{N}^{s}(\mathcal{\hat{X}}\_{d}^{s})) |  |

where rr represents the squeeze factor, which reduces the original patch number NsN^{s} to Nsr\frac{N^{s}}{r}. M​L​PNsMLP\_{N}^{s} and M​L​PLsMLP\_{L}^{s} are used to align the dimensions of patch number and patch length accordingly.
𝒳^ps\mathcal{\hat{X}}\_{p}^{s} represents the reconstructed original time series.
This reconstruction is used to calculate the reconstruction loss, helping the reduced number of patches effectively capture the essential information from the original patches.
𝒳^d\mathcal{\hat{X}}\_{d} denotes the concatenation of the squeezed multi-period patch embeddings, which are
fed into the transformer encoder.

![Refer to caption](figure/Rec_0701.jpg)

Figure 5. Illustration of patch squeeze module.

### 3.3. Vanilla Multi-period Attention

By directly feeding 𝒳^d\mathcal{\hat{X}}\_{d} into the transformer encoder, we implement the vanilla multi-period self-attention. Specifically, each head h=1,2,…,Hh=1,2,...,H in the multi-head attention processes 𝒳^d\mathcal{\hat{X}}\_{d} to generate HH distinct query matrices Qh=(𝒳^d)T​WhQQ\_{h}=(\mathcal{\hat{X}}\_{d})^{T}W\_{h}^{Q}, key matrices Kh=(𝒳^d)T​WhKK\_{h}=(\mathcal{\hat{X}}\_{d})^{T}W\_{h}^{K}, and value matrices Vh=(𝒳^d)T​WhVV\_{h}=(\mathcal{\hat{X}}\_{d})^{T}W\_{h}^{V}. TT denotes matrix transposition.
A scaled dot-product operation is then applied to compute the attention output Oh∈ℝD×NO\_{h}\in\mathbb{R}^{D\times N}:

|  |  |  |  |
| --- | --- | --- | --- |
| (11) |  | Oh=A​t​t​e​n​t​i​o​n​(Qh,Kh,Vh)=σ​(Qh​(Kh)Tdk)​Vh\vskip-2.84544ptO\_{h}=Attention(Q\_{h},K\_{h},V\_{h})=\sigma(\frac{Q\_{h}(K\_{h})^{T}}{\sqrt{d\_{k}}})V\_{h} |  |

here, σ\sigma denotes the Softmax function.
The
output ze∈ℝD×Nz\_{e}\in\mathbb{R}^{D\times N} at the ee-th encoder layer is computed using BatchNorm and a feed-forward network with residual connections (Vaswani et al., [2017](https://arxiv.org/html/2511.08622v1#bib.bib31); Nie et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib21)).

### 3.4. Inter-period Redundancy Filtering-based Multi-period Self-attention

The information redundancy between different periods can cause self-attention to excessively focus on repetitive segments due to higher correlations between similar parts.
This can prevent self-attention from capturing all patterns distributed across short and medium-/long-term periods, thereby impairing TSF performance.

To mitigate this issue, we propose an Inter-period Redundancy Filtering (IRF) block, illustrated in Figure [3](https://arxiv.org/html/2511.08622v1#S2.F3 "Figure 3 ‣ 2.1.2. Multi-period based TSF ‣ 2.1. Time Series Forecasting (TSF) ‣ 2. Related Work and Preliminary ‣ Multi-period Learning for Financial Time Series Forecasting")(b).
IRF identifies redundant information in longer periods based on shorter ones, and then removes it in the embedding space.
Consequently, IRF helps better self-attention modeling, allowing important information from all periods to be effectively utilized, thereby improving prediction accuracy.
For implementation, IRF starts by splitting the concatenated period representations from zez\_{e}:

|  |  |  |  |
| --- | --- | --- | --- |
| (12) |  | ze1,ze2,⋯,zes,⋯,zeS=s​p​l​i​t​(ze)z^{1}\_{e},z^{2}\_{e},\cdots,z^{s}\_{e},\cdots,z^{S}\_{e}=split(z\_{e}) |  |

Each zes∈ℝD×Nsz^{s}\_{e}\in\mathbb{R}^{D\times N^{s}} denotes the representation of the ss-th period.
Then, we devise a Single Period Processing (SPP, as shown in Figure [3](https://arxiv.org/html/2511.08622v1#S2.F3 "Figure 3 ‣ 2.1.2. Multi-period based TSF ‣ 2.1. Time Series Forecasting (TSF) ‣ 2. Related Work and Preliminary ‣ Multi-period Learning for Financial Time Series Forecasting")(b)) module for each period representation zesz^{s}\_{e}.
SPP has two branches of linear layers.
The forecast branch generates prediction of the current period, while the redundancy estimation branch estimates the redundancy to be removed from the longer period representation zes′z^{s^{\prime}}\_{e} (s<s′≤Ss<s^{\prime}\leq S).
SPP outputs the forecasts 𝒳^fes\mathcal{\hat{X}}^{s}\_{f\_{e}} and the estimated redundancy ϵes\epsilon^{s}\_{e} for the ss-th period at ee-th block.

|  |  |  |  |
| --- | --- | --- | --- |
| (13) |  | 𝒳^fes,ϵes=S​P​P​(zes)\mathcal{\hat{X}}^{s}\_{f\_{e}},\epsilon^{s}\_{e}=SPP(z^{s}\_{e}) |  |

To reduce redundancy, we subtract the estimated redundancy of all shorter periods from the current period embedding zesz^{s}\_{e}.
The period representation after redundancy filtering is denoted as z^es\hat{z}^{s}\_{e}:

|  |  |  |  |
| --- | --- | --- | --- |
| (14) |  | z^es=zes−∑j=0s−1ϵejdk\hat{z}^{s}\_{e}=z^{s}\_{e}-\sum\_{j=0}^{s-1}\frac{\epsilon^{j}\_{e}}{\sqrt{d\_{k}}} |  |

dk\sqrt{d\_{k}} serves as a scaling factor designed to prevent numerical overflow and stabilize gradients.
z^es\hat{z}^{s}\_{e} are then output to the subsequent encoder layer.

Lastly, as illustrated in Figure [3](https://arxiv.org/html/2511.08622v1#S2.F3 "Figure 3 ‣ 2.1.2. Multi-period based TSF ‣ 2.1. Time Series Forecasting (TSF) ‣ 2. Related Work and Preliminary ‣ Multi-period Learning for Financial Time Series Forecasting")(a), stacking the MLF block (one transformer block and one IRF block)
enables progressive redundancy filtering, thereby improving the accuracy of redundancy estimates and self-attention modeling.
Each MLF block has a forecast head (Lee et al., [2015](https://arxiv.org/html/2511.08622v1#bib.bib18); Huang et al., [2017](https://arxiv.org/html/2511.08622v1#bib.bib14)).
We aggregate the forecasts from all blocks by:

|  |  |  |  |
| --- | --- | --- | --- |
| (15) |  | 𝒳¯fs=1E​∑e=1E𝒳fes\mathcal{\overline{X}}\_{f}^{s}=\frac{1}{E}\sum\_{e=1}^{E}\mathcal{X}^{s}\_{f\_{e}} |  |

where 𝒳¯fs\mathcal{\overline{X}}\_{f}^{s} is the average forecast at the block level for period ss.

### 3.5. Learnable Weighted-average Integration (LWI)

After obtaining forecasts 𝒳¯fs\mathcal{\overline{X}}\_{f}^{s} for each
period,
we now integrate multiple period forecasts to obtain the final prediction by learned weighted averaging.
As different future positions are best forecasted by different periods, simply adding or averaging these predictions may lead to inaccurate forecasting.
Hence, we propose a Learnable Weighted-average Integration (LWI) module to effectively integrate multi-period forecasts.
LWI adaptively assigns the weights for different period forecasts, which increases the contribution of accurate predictions while reducing the impact of inaccurate ones.

To implement LWI, we start by extracting temporal features ν\nu from the longest-period TS 𝒳hS\mathcal{X}\_{h}^{S} using a lightweight Convolutional Neural Network (CNN), which consists of a convolutional layer (C​o​n​v​(⋅)Conv(\cdot)), padding function (P​a​d​(⋅)Pad(\cdot)), BatchNorm (B​N​(⋅)BN(\cdot)) and Maxpooling (M​a​x​P​o​o​l​(⋅)MaxPool(\cdot)) layer.
Then we employ two MLPs to derive query and key values, enabling a dot product operation to compute attention scores that indicate the model’s effective focus on different periods.
These attention scores are then passed through a sigmoid activation function ς​(⋅)\varsigma(\cdot) to generate weights A​t​tAtt for each period.
Finally, we average the multi-period forecasts based on the learned weights as the final prediction (Eq. [18](https://arxiv.org/html/2511.08622v1#S3.E18 "In 3.5. Learnable Weighted-average Integration (LWI) ‣ 3. Multi-period Learning Framework (MLF) ‣ Multi-period Learning for Financial Time Series Forecasting")).
The entire process that depicted in right of Figure [3](https://arxiv.org/html/2511.08622v1#S2.F3 "Figure 3 ‣ 2.1.2. Multi-period based TSF ‣ 2.1. Time Series Forecasting (TSF) ‣ 2. Related Work and Preliminary ‣ Multi-period Learning for Financial Time Series Forecasting")(a) can be formulated as follows:

|  |  |  |  |
| --- | --- | --- | --- |
| (16) |  | ν=M​a​x​P​o​o​l​(B​N​(C​o​n​v​(P​a​d​(𝒳h))))\nu=MaxPool(BN(Conv(Pad(\mathcal{X}\_{h}))))\vskip-2.84544pt |  |

|  |  |  |  |
| --- | --- | --- | --- |
| (17) |  | A​t​t=ς​(tanh⁡(Θ1​ν+b1)⊙tanh⁡(Θ2​ν+b2))Att=\varsigma\left(\tanh{(\Theta\_{1}\nu+\textbf{b}\_{1})}\odot\tanh{(\Theta\_{2}\nu+\textbf{b}\_{2})}\right)\vskip-2.84544pt |  |

|  |  |  |  |
| --- | --- | --- | --- |
| (18) |  | 𝒳¯f=1S​∑e=1S𝒳fs⊙A​t​ts\mathcal{\overline{X}}\_{f}=\frac{1}{S}\sum\_{e=1}^{S}\mathcal{X}^{s}\_{f}\odot Att^{s} |  |

where Θ\Theta and b are learnable parameters.

### 3.6. System Deployment

We illustrate the online system architecture in Figure [6](https://arxiv.org/html/2511.08622v1#S3.F6 "Figure 6 ‣ 3.6. System Deployment ‣ 3. Multi-period Learning Framework (MLF) ‣ Multi-period Learning for Financial Time Series Forecasting").
It consists of three sub-systems: the Fund Inventory Management System (FIMS), Alipay APP Market Shelf, and the MaxCompute database.
FIMS incorporates modules for Sales Forecasting (SF, with MLF in it), Inventory Planning (IP), and Data Monitoring (DM).
SF predicts fund sales for the upcoming 5 days based on historical sales data.
IP uses an inventory planning algorithm to determine product inventory according to the forecasted sales.
DM monitors the reasonableness of forecasted sales and inventory plans.

The system operates as follows.
The shelf subsystem continuously sends trading data to the FIMS subsystem, which updates the sales records of fund products in the MaxCompute database.
At the end of each day, FIMS performs three sequential daily batch tasks: 1) retraining the MLF model; 2) using the updated MLF to forecast fund sales for the next 5 days; and 3) planning product inventory with the IP module.
Subsequently, the inventory of all fund products on the shelf is adjusted accordingly.
Additionally, both forecasted fund sales and planned inventory are persistently stored in the MaxCompute database for retrospective analysis.

Training.
The final loss function for MLF is:

|  |  |  |  |
| --- | --- | --- | --- |
| (19) |  | ℒMLF=ℒMSE​(𝒳¯f,𝒳f)+1S​∑j=1SℒMSE​(𝒳^pj,𝒳pj)\mathcal{L\_{\text{MLF}}}=\mathcal{L\_{\text{MSE}}}(\mathcal{\overline{X}}\_{f},\mathcal{X}\_{f})+\frac{1}{S}\sum\_{j=1}^{S}\mathcal{L\_{\text{MSE}}}(\mathcal{\hat{X}}^{j}\_{p},\mathcal{X}^{j}\_{p}) |  |

here, the first term refers to the forecasting loss, while the second term represents the reconstruction loss.

![Refer to caption](figure/deployment_system_0701.jpg)

Figure 6. Alipay’s fund management system architecture.
MLF has been deployed in this production environment.

## 4. Experiments and Results

### 4.1. Experimental Settings

#### 4.1.1. Datasets

Fund sales dataset.
We collected sales data for different fund products from Ant Fortune, an online wealth management platform on the Alipay APP, consisting of daily user transactions for applying and redeeming funds.
The dataset spans from January 2015 to January 2023 and is split into training, validation, and testing sets in a 7:1:2 ratio.
For model training and evaluation, we merged the training, validation, and test sets across all fund datasets.

Public datasets. These datasets, as shown in Table [2](https://arxiv.org/html/2511.08622v1#S4.T2 "Table 2 ‣ 4.1.1. Datasets ‣ 4.1. Experimental Settings ‣ 4. Experiments and Results ‣ Multi-period Learning for Financial Time Series Forecasting"), cover a range of time steps and variables and have been widely employed in the literature for multivariate forecasting tasks (Nie et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib21); Wu et al., [2021](https://arxiv.org/html/2511.08622v1#bib.bib33); Zhou et al., [2022b](https://arxiv.org/html/2511.08622v1#bib.bib43)).

Table 2. Statistics of used popular public datasets.

| Datasets | ETTh1/h2 | ETTm1/m2 | Weather | Exchange | Illness | Electricity |
| --- | --- | --- | --- | --- | --- | --- |
| Features | 7 | 7 | 21 | 8 | 7 | 321 |
| Timesteps | 17420 | 69680 | 52696 | 7588 | 966 | 26304 |




Table 3. Comparing MLF with popular benchmarks in short-term multivariate forecasting. “-” denotes that the prediction length is too short to use Scaleformer. The best results are in bold and the second best are underlined.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | MLF | | PatchTST | | Patch-Ensemble | | Patch-Concat | | NHits | | FiLM | | Scaleformer | | Pathformer | |
|  | MSE | WMA. | MSE | WMA. | MSE | WMA. | MSE | WMA. | MSE | WMA. | MSE | WMA. | MSE | WMA. | MSE | WMA. |
| Fund | 1 | 33.85 | 75.84 | 36.68 | 81.05 | 40.30 | 86.68 | 39.68 | 85.87 | 36.53 | 80.29 | 46.12 | 96.10 | - | - | 35.54 | 80.75 |
|  | ±\pm0.033 | ±\pm0.093 | ±\pm0.068 | ±\pm0.288 | ±\pm0.235 | ±\pm0.431 | ±\pm0.328 | ±\pm0.266 | ±\pm0.057 | ±\pm0.108 | ±\pm0.009 | ±\pm0.009 | - | - | ±\pm0.08 | ±\pm0.06 |
| 5 | 38.28 | 80.37 | 40.28 | 83.09 | 39.95 | 83.24 | 41.60 | 87.14 | 40.91 | 83.93 | 42.86 | 85.35 | 40.43 | 83.74 | 39.90 | 82.58 |
|  | ±\pm0.029 | ±\pm0.071 | ±\pm0.055 | ±\pm0.143 | ±\pm0.068 | ±\pm0.087 | ±\pm0.357 | ±\pm0.643 | ±\pm0.024 | ±\pm0.090 | ±\pm0.009 | ±\pm0.001 | ±\pm0.088 | ±\pm2.47 | ±\pm0.02 | ±\pm0.06 |
| 8 | 41.94 | 86.06 | 44.71 | 88.81 | 44.06 | 88.77 | 43.49 | 88.08 | 44.81 | 89.23 | 44.57 | 89.12 | 43.97 | 87.62 | 44.17 | 88.67 |
|  | ±\pm0.031 | ±\pm0.123 | ±\pm0.085 | ±\pm0.164 | ±\pm0.052 | ±\pm0.094 | ±\pm0.289 | ±\pm0.552 | ±\pm0.020 | ±\pm0.062 | ±\pm0.009 | ±\pm0.001 | ±\pm0.062 | ±\pm2.22 | ±\pm0.04 | ±\pm0.11 |
| 10 | 44.42 | 88.66 | 46.18 | 90.63 | 46.09 | 91.36 | 45.59 | 90.46 | 46.73 | 91.12 | 46.62 | 92.67 | 45.75 | 89.63 | 45.56 | 89.82 |
|  | ±\pm0.057 | ±\pm0.041 | ±\pm0.063 | ±\pm0.160 | ±\pm0.049 | ±\pm0.070 | ±\pm0.054 | ±\pm0.101 | ±\pm0.087 | ±\pm0.097 | ±\pm0.004 | ±\pm0.009 | ±\pm0.088 | ±\pm2.23 | ±\pm0.06 | ±\pm0.13 |
|  |  | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE |
| Electricity | 1 | 0.0472 | 0.1340 | 0.0510 | 0.1410 | 0.053 | 0.144 | 0.0492 | 0.1382 | 0.0517 | 0.1430 | 0.0729 | 0.1750 | - | - | 0.0613 | 0.1590 |
| ETTh1 | 1 | 0.0873 | 0.1899 | 0.0979 | 0.2033 | 0.115 | 0.2202 | 0.0958 | 0.1983 | 0.113 | 0.2268 | 0.1327 | 0.2395 | - | - | 0.1067 | 0.213 |
| ETTm1 | 1 | 0.0412 | 0.1245 | 0.0461 | 0.13 | 0.0524 | 0.1457 | 0.0450 | 0.1298 | 0.0475 | 0.139 | 0.0998 | 0.1918 | - | - | 0.0470 | 0.1346 |
| Illness | 1 | 0.1493 | 0.2188 | 0.1782 | 0.2340 | 0.2918 | 0.2934 | 0.2476 | 0.2409 | 0.2515 | 0.2833 | 0.3104 | 0.3306 | - | - | 0.269 | 0.279 |
| Exchange | 1 | 0.0029 | 0.0267 | 0.0042 | 0.0363 | 0.0037 | 0.030 | 0.0047 | 0.0325 | 0.008 | 0.0559 | 0.0055 | 0.0445 | - | - | 0.0035 | 0.0293 |



![Refer to caption](figure/speed_memory_0701v2.jpg)

Figure 7. 
Efficiency analysis for best-performing TSF models was conducted on Ettm1, Weather, and Fund datasets.

#### 4.1.2. Evaluation Metrics

We evaluate multivariate TSF tasks using three metrics: Mean Squared Error (MSE), Mean Absolute Error (MAE), and Weighted Mean Absolute Percentage Error (WMAPE or WMA. for short).
WMAPE is particularly relevant for the fund dataset on the Alipay APP, as it assesses the accuracy of predictions on larger values.
This metric aligns with the business goal of accurately forecasting larger transactions in fund products.
We present the sum of WMAPE for the two variables in the fund dataset.

Table 4. Comparing MLF with popular benchmarks in long-term multivariate forecasting. The best results are indicated in bold, and the second-best results are underlined.

|  |  | MLF | | PatchTST | | Patch-Ensemble | | Patch-Concat | | NHits | | FiLM | | Scaleformer | | Pathformer | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE |
| ETTh1 | 96 | 0.363 | 0.392 | 0.370 | 0.400 | 0.370 | 0.401 | 0.369 | 0.400 | 0.427 | 0.439 | 0.371 | 0.394 | 0.379 | 0.409 | 0.393 | 0.406 |
| 192 | 0.399 | 0.416 | 0.413 | 0.429 | 0.402 | 0.422 | 0.406 | 0.427 | 0.472 | 0.473 | 0.414 | 0.423 | 0.411 | 0.43 | 0.421 | 0.436 |
| 336 | 0.416 | 0.423 | 0.422 | 0.440 | 0.424 | 0.432 | 0.427 | 0.433 | 0.525 | 0.498 | 0.442 | 0.445 | 0.43 | 0.443 | 0.451 | 0.451 |
| 720 | 0.438 | 0.454 | 0.447 | 0.468 | 0.445 | 0.463 | 0.445 | 0.463 | 0.608 | 0.565 | 0.465 | 0.472 | 0.446 | 0.465 | 0.483 | 0.470 |
| ETTh2 | 96 | 0.267 | 0.334 | 0.274 | 0.337 | 0.276 | 0.341 | 0.277 | 0.341 | 0.314 | 0.379 | 0.284 | 0.348 | 0.275 | 0.343 | 0.285 | 0.349 |
| 192 | 0.327 | 0.374 | 0.341 | 0.382 | 0.337 | 0.379 | 0.336 | 0.379 | 0.401 | 0.434 | 0.357 | 0.4 | 0.337 | 0.384 | 0.331 | 0.385 |
| 336 | 0.350 | 0.396 | 0.359 | 0.405 | 0.357 | 0.403 | 0.358 | 0.403 | 0.452 | 0.469 | 0.377 | 0.417 | 0.364 | 0.414 | 0.368 | 0.409 |
| 720 | 0.383 | 0.423 | 0.388 | 0.427 | 0.387 | 0.429 | 0.388 | 0.430 | 0.545 | 0.527 | 0.439 | 0.456 | 0.397 | 0.438 | 0.389 | 0.427 |
| ETTm1 | 96 | 0.285 | 0.344 | 0.293 | 0.346 | 0.296 | 0.347 | 0.290 | 0.345 | 0.32 | 0.367 | 0.302 | 0.345 | 0.293 | 0.347 | 0.301 | 0.352 |
| 192 | 0.324 | 0.366 | 0.333 | 0.370 | 0.332 | 0.373 | 0.331 | 0.372 | 0.357 | 0.392 | 0.338 | 0.368 | 0.333 | 0.371 | 0.356 | 0.383 |
| 336 | 0.355 | 0.384 | 0.360 | 0.392 | 0.366 | 0.395 | 0.365 | 0.396 | 0.392 | 0.417 | 0.365 | 0.385 | 0.364 | 0.391 | 0.387 | 0.405 |
| 720 | 0.401 | 0.410 | 0.404 | 0.417 | 0.415 | 0.427 | 0.417 | 0.427 | 0.442 | 0.441 | 0.42 | 0.42 | 0.42 | 0.425 | 0.416 | 0.420 |
| ETTm2 | 96 | 0.164 | 0.253 | 0.166 | 0.256 | 0.163 | 0.257 | 0.169 | 0.263 | 0.176 | 0.255 | 0.165 | 0.256 | 0.172 | 0.255 | 0.168 | 0.258 |
| 192 | 0.218 | 0.295 | 0.223 | 0.296 | 0.226 | 0.304 | 0.227 | 0.306 | 0.245 | 0.305 | 0.222 | 0.296 | 0.231 | 0.298 | 0.227 | 0.296 |
| 336 | 0.270 | 0.330 | 0.277 | 0.336 | 0.278 | 0.336 | 0.285 | 0.340 | 0.295 | 0.346 | 0.277 | 0.333 | 0.278 | 0.328 | 0.273 | 0.331 |
| 720 | 0.344 | 0.379 | 0.357 | 0.381 | 0.360 | 0.393 | 0.360 | 0.393 | 0.401 | 0.413 | 0.371 | 0.389 | 0.361 | 0.383 | 0.366 | 0.392 |
| Weather | 96 | 0.145 | 0.195 | 0.148 | 0.200 | 0.149 | 0.201 | 0.147 | 0.199 | 0.158 | 0.212 | 0.199 | 0.262 | 0.152 | 0.208 | 0.155 | 0.208 |
| 192 | 0.191 | 0.238 | 0.194 | 0.241 | 0.196 | 0.244 | 0.194 | 0.240 | 0.202 | 0.247 | 0.228 | 0.288 | 0.197 | 0.251 | 0.196 | 0.246 |
| 336 | 0.241 | 0.280 | 0.245 | 0.282 | 0.247 | 0.284 | 0.248 | 0.284 | 0.257 | 0.3 | 0.267 | 0.323 | 0.253 | 0.296 | 0.25 | 0.286 |
| 720 | 0.296 | 0.328 | 0.309 | 0.330 | 0.318 | 0.337 | 0.316 | 0.335 | 0.327 | 0.356 | 0.319 | 0.361 | 0.311 | 0.343 | 0.324 | 0.337 |

#### 4.1.3. Baselines

We compare our Multi-period Learning Framework (MLF) against three types of baselines.
(i) single-period based models: This category includes PtachTST (Nie et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib21)), NHits (Challu et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib3)), Scaleformer (Shabani et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib25)) and PathFormer (Chen et al., [2024](https://arxiv.org/html/2511.08622v1#bib.bib6)).
Since Scaleformer serves as a general architecture, we combine it with Autoformer (Wu et al., [2021](https://arxiv.org/html/2511.08622v1#bib.bib33)), NHits (Challu et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib3)), and PatchTST (Nie et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib21)) to create strong baseline.

(ii) Multi-period based models: This category includes FiLM (Zhou et al., [2022a](https://arxiv.org/html/2511.08622v1#bib.bib42)) and two multi-period variants based on PatchTST, called Patch-Concat and Patch-Ensemble. Specifically, for Patch-Concat, we concatenate multi-period data for training PatchTST.
For Patch-Ensemble, we train multiple instances of PatchTST using multiple periods with different TS lengths for ensemble learning.
We compare these three baselines to demonstrate the necessity of the structure designed for multi-period forecasting in MLF.

#### 4.1.4. Implementation Details

For short-term time series forecasting (TSF) tasks, the short-term to long-term multi-period lengths for MLF are 5, 10, 30, 60, 120, and 150 time steps.
Prediction lengths vary across m∈1,5,8,10m\in{1,5,8,10}.
For long-term TSF tasks, the used short-term to long-term multi-period lengths are 128,256,512,768, 1024 and 2048 time steps.
Prediction lengths vary across m∈96,192,336,720m\in{96,192,336,720}.
Each period within MLF employs a fixed number of 64 patches, with a squeeze factor r∈r\in 2,4,8 to squeeze the long-sequence input.
Both Patch-Concat and Patch-Ensemble models utilize the same multi-period configuration as MLF.
The learning rate and batch size are set to 0.0001 and 128 respectively.
All methods follow the same data loading parameters (e.g., train/val/test split ratio) as in (Nie et al., [2022](https://arxiv.org/html/2511.08622v1#bib.bib21)).
Each method is trained for 30 epochs.
All experiments in this paper are conducted using PyTorch on an NVIDIA GeForce RTX 3090 GPU.

### 4.2. Time Series Forecasting Accuracy

#### 4.2.1. Comparison with single-period baselines

Extensive results show that MLF outperforms advanced single-period baselines, including PatchTST, NHits, Scaleformer, and PathFormer on both short-term (Table [3](https://arxiv.org/html/2511.08622v1#S4.T3 "Table 3 ‣ 4.1.1. Datasets ‣ 4.1. Experimental Settings ‣ 4. Experiments and Results ‣ Multi-period Learning for Financial Time Series Forecasting")) and long-term tasks (Table [4](https://arxiv.org/html/2511.08622v1#S4.T4 "Table 4 ‣ 4.1.2. Evaluation Metrics ‣ 4.1. Experimental Settings ‣ 4. Experiments and Results ‣ Multi-period Learning for Financial Time Series Forecasting")).
These baselines are well-designed for single-period time series and doesn’t utilize multi-period information.
However, we have observed that inputs of different lengths have a significant impact on prediction accuracy. However, these single-period-based methods can only process one input at a time, which prevents them from achieving better prediction accuracy.
In contrast, MLF not only utilizes multi-period inputs, but also incorporates new designs to maximize its TSF potential, achieving better accuracy.

#### 4.2.2. Comparison with multi-period methods

Extensive results also show that MLF outperforms advanced multi-period methods FiLM, Patch-Concat and Patch-Ensemble, as shown Table [3](https://arxiv.org/html/2511.08622v1#S4.T3 "Table 3 ‣ 4.1.1. Datasets ‣ 4.1. Experimental Settings ‣ 4. Experiments and Results ‣ Multi-period Learning for Financial Time Series Forecasting") and Table [4](https://arxiv.org/html/2511.08622v1#S4.T4 "Table 4 ‣ 4.1.2. Evaluation Metrics ‣ 4.1. Experimental Settings ‣ 4. Experiments and Results ‣ Multi-period Learning for Financial Time Series Forecasting").
This highlights that merely linearly integrating multi-period outputs (FiLM), concatenating multi-period inputs for training PatchTST (Patch-Concat) and using multiple instances of PatchTST for ensemble learning (Patch-Ensemble) fails to fulfill the forecasting potential of multi-period data.
In contrast, MLF is customized to address the characteristics of multi-period data, such as inter-period redundancy and varying sequence lengths.
New designs in MLF enable it to effectively utilize information across all periods, thereby achieving superior accuracy in TSF tasks.

### 4.3. Time Series Forecasting Efficiency

In MLF, we use squeeze factors of 8 (MLF-8) and 4 (MLF-4).
For a fair comparison, we maintained consistency in shared hyper-parameters (such as hidden size and attention heads in the transformer) and settings (like batch size).

We select the best-performing models for an efficiency comparison.
Results are depicted in Figure [7](https://arxiv.org/html/2511.08622v1#S4.F7 "Figure 7 ‣ 4.1.1. Datasets ‣ 4.1. Experimental Settings ‣ 4. Experiments and Results ‣ Multi-period Learning for Financial Time Series Forecasting").
Due to GPU memory constraints (24GB), baselines like Pathformer can handle a maximum sequence length of 576 across all datasets, while Scaleformer manages 576 for Weather datasets and 1024 for ETTm1 or Fund datasets.
Despite MLF’s significantly longer actual input sequence length (2816 compared to 576 or 1024 for PathFormer and Scaleformer), it achieves better efficiency.
For instance, on the Fund dataset (Figure [7](https://arxiv.org/html/2511.08622v1#S4.F7 "Figure 7 ‣ 4.1.1. Datasets ‣ 4.1. Experimental Settings ‣ 4. Experiments and Results ‣ Multi-period Learning for Financial Time Series Forecasting")(a)), MLF is 3.6 times faster than Scaleformer and 11.8 times faster than PathFormer in terms of inference time.
MLF’s efficiency advantage is even bigger with larger datasets, as shown in the results of the Weather dataset (Figure [7](https://arxiv.org/html/2511.08622v1#S4.F7 "Figure 7 ‣ 4.1.1. Datasets ‣ 4.1. Experimental Settings ‣ 4. Experiments and Results ‣ Multi-period Learning for Financial Time Series Forecasting")(b)), while maintaining satisfactory accuracy (Table [7](https://arxiv.org/html/2511.08622v1#S4.T7 "Table 7 ‣ 4.5.3. Effectiveness of patch squeeze module ‣ 4.5. Ablation Study ‣ 4. Experiments and Results ‣ Multi-period Learning for Financial Time Series Forecasting")).

### 4.4. Deployment Results

MLF has been deployed in the FIMS of Alipay since late February 2024.
We compared the WMAPE and Gross Merchandise Volume (GMV) of all fund products between MLF and the previously deployed model PatchTST.
Table [5](https://arxiv.org/html/2511.08622v1#S4.T5 "Table 5 ‣ 4.4. Deployment Results ‣ 4. Experiments and Results ‣ Multi-period Learning for Financial Time Series Forecasting") shows the improvement ratio of WMAPE (I​RW​M​A​P​E=P​a​t​c​h​T​S​TW​M​A​P​E−M​L​FW​M​A​P​EP​a​t​c​h​T​S​TW​M​A​P​EIR\_{WMAPE}=\frac{PatchTST\_{WMAPE}-MLF\_{WMAPE}}{PatchTST\_{WMAPE}}) and the improvement ratio of GMV (I​RG​M​V=M​L​FG​M​V−P​a​t​c​h​T​S​TG​M​VP​a​t​c​h​T​S​TG​M​VIR\_{GMV}=\frac{MLF\_{GMV}-PatchTST\_{GMV}}{PatchTST\_{GMV}}) over five consecutive weeks.
The improvement ratios of WMAPE and GMV over advanced PatchTST demonstrate that multi-period based MLF is effective in the fund sales forecasting scenario.

Table 5. Deployment results over consecutive five weeks.

| Year (2024) | Week 1 | Week 2 | Week 3 | Week 4 | Week 5 | Mean |
| --- | --- | --- | --- | --- | --- | --- |
| I​RW​M​A​P​EIR\_{WMAPE} (%) | 6.84 | 4.25 | 5.21 | 4.92 | 4.62 | 5.16 |
| I​RG​M​VIR\_{GMV} (%) | 1.14 | 0. 58 | 0.72 | 0.85 | 0.95 | 0.84 |

### 4.5. Ablation Study

#### 4.5.1. Ablation of each component (Table [6](https://arxiv.org/html/2511.08622v1#S4.T6 "Table 6 ‣ 4.5.1. Ablation of each component (Table 6) ‣ 4.5. Ablation Study ‣ 4. Experiments and Results ‣ Multi-period Learning for Financial Time Series Forecasting"))

(1) Effectiveness of Inter-period Redundancy Filtering (IRF). “w/o IRF” denotes we remove redundancy subtract operation (without using Eq. [14](https://arxiv.org/html/2511.08622v1#S3.E14 "In 3.4. Inter-period Redundancy Filtering-based Multi-period Self-attention ‣ 3. Multi-period Learning Framework (MLF) ‣ Multi-period Learning for Financial Time Series Forecasting")) in IRF block.
When removing IRF, we observe raised MSE.
Moreover, compared to ”w/o MA”, ”w/o (MA+IRF)” also shows further raised MSE.
The raised MSE demonstrates that filtering redundancy between periods allows self-attention to avoid overly focusing on repetitive parts.
This enables the utilization of information from all periods, resulting in better TSF accuracy.

Figures [8](https://arxiv.org/html/2511.08622v1#S4.F8 "Figure 8 ‣ 4.5.3. Effectiveness of patch squeeze module ‣ 4.5. Ablation Study ‣ 4. Experiments and Results ‣ Multi-period Learning for Financial Time Series Forecasting")(a)-(d) further illustrate this.
Specifically, we obtained self-attention heatmaps by averaging the attention score matrices of all test samples on the Fund dataset.
Each index on the horizontal axis represents a patch, with every consecutive three patches representing a period.
The heatmap without the IRF operation shows an overemphasis on the overlapping parts among the multi-period inputs (vertical highlight areas in Figures [8](https://arxiv.org/html/2511.08622v1#S4.F8 "Figure 8 ‣ 4.5.3. Effectiveness of patch squeeze module ‣ 4.5. Ablation Study ‣ 4. Experiments and Results ‣ Multi-period Learning for Financial Time Series Forecasting")(b) and (d)), while the heatmap with the IRF operation demonstrates that most regions (non-repetitive parts among periods) receive effective attention.

Table 6. Ablation study on various datasets.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Methods/ Datasets | Illness | Electricity | ETTh1 | Exchange | Fund |
| MSE | MSE | MSE | MSE | WMA. |
| MLF | 0.149 | 0.0472 | 0.087 | 0.0030 | 75.84 |
| w/o IRF | 0.163 | 0.0500 | 0.091 | 0.0033 | 78.56 |
| w/o (LWI) | 0.155 | 0.0491 | 0.088 | 0.0032 | 77.32 |
| w/o MA | 0.236 | 0.0539 | 0.114 | 0.004 | 78.23 |
| w/o (MA+IRF) | 0.261 | 0.0559 | 0.130 | 0.004 | 79.85 |

(2) Effectiveness of MA and LWI.
The raised MSE observed in the ”w/o LWI” and ”w/o MA” highlights the importance of the Learnable Weighted-average Integration (LWI) and Multi-period self-Attention (MA) modules.
Based on the learned adaptive period weights, LWI increases the contribution of accurate predictions while reducing the impact of inaccurate ones, thereby improving overall forecasting accuracy.
MA effectively captures multi-period dependencies.
Together, these modules are crucial for realizing the full potential of multi-period based time series forecasting.

#### 4.5.2. Effectiveness of Multi-period self-Adaptive Patching (MAP)

In the standard multi-period patching, the shorter periods have fewer patches while the longer one is the opposite.
The results in Figure [9](https://arxiv.org/html/2511.08622v1#S4.F9 "Figure 9 ‣ 4.5.3. Effectiveness of patch squeeze module ‣ 4.5. Ablation Study ‣ 4. Experiments and Results ‣ Multi-period Learning for Financial Time Series Forecasting") show the raised MSE when MAP is removed (w/o MAP), indicating that shorter periods may be unfairly treated in standard multi-period patching due to the insufficient number of patches.
MAP ensures each period 𝒳hs\mathcal{X}\_{h}^{s} has an equal number of patches, allowing the model to equally pay attention to the time semantics of all periods and improving TSF performance.

#### 4.5.3. Effectiveness of patch squeeze module

As shown in Table [7](https://arxiv.org/html/2511.08622v1#S4.T7 "Table 7 ‣ 4.5.3. Effectiveness of patch squeeze module ‣ 4.5. Ablation Study ‣ 4. Experiments and Results ‣ Multi-period Learning for Financial Time Series Forecasting"), MLF achieves satisfactory performance with squeeze factors of 2, 4, and 8.
This demonstrates that the patch squeeze module in MLF can significantly reduce time complexity while maintaining good accuracy.
Additionally, the reconstruction loss in the patch squeeze module is effective, as Figure [8](https://arxiv.org/html/2511.08622v1#S4.F8 "Figure 8 ‣ 4.5.3. Effectiveness of patch squeeze module ‣ 4.5. Ablation Study ‣ 4. Experiments and Results ‣ Multi-period Learning for Financial Time Series Forecasting")(d) shows raised MSE when this term is removed (”w/o reconstruction loss”).

Table 7. Effectiveness of the patch squeeze module: MLF’s accuracy with squeeze factors 2 (MLF-2), 4 (MLF-4), and 8 (MLF-8). ’-’ indicates out of memory.

|  |  | PatchTST | | MLF-2 | | MLF-4 | | MLF-8 | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE |
| ETTm1 | 96 | 0.293 | 0.346 | 0.283 | 0.342 | 0.285 | 0.344 | 0.287 | 0.345 |
| 192 | 0.333 | 0.370 | 0.322 | 0.366 | 0.324 | 0.366 | 0.326 | 0.366 |
| 336 | 0.360 | 0.392 | 0.357 | 0.387 | 0.356 | 0.384 | 0.355 | 0.384 |
| 720 | 0.404 | 0.417 | 0.406 | 0.413 | 0.400 | 0.410 | 0.401 | 0.410 |
| Weather | 96 | 0.148 | 0.200 | - | - | 0.146 | 0.196 | 0.145 | 0.195 |
| 192 | 0.194 | 0.241 | - | - | 0.191 | 0.238 | 0.191 | 0.239 |
| 336 | 0.245 | 0.282 | - | - | 0.244 | 0.283 | 0.241 | 0.280 |
| 720 | 0.309 | 0.330 | - | - | 0.304 | 0.333 | 0.296 | 0.328 |



![Refer to caption](figure/attn_rec0701.jpg)

  


Figure 8. Extra ablation study: (a)-(d) Self-attention visualization with and without IRF. (e) Ablation of the reconstruction loss in the patch squeeze module on the ETTm1 dataset.



![Refer to caption](figure/wo_map0701v2.jpg)

Figure 9. 
Ablation study of Multi-period self-Adaptive Patching (MAP) module. We report the average MSE values for predicting future 96, 192, 336, and 720 time steps.

## 5. Conclusion

This paper introduces Multi-period Learning Framework MLF, which incorporates multiple inputs with varying lengths to achieve better accuracy and reduces the costs of selecting input windows during training. MLF also demonstrates that using a simple encoder to squeeze the input time series (dimensionality reduction) can significantly improve model efficiency, reduce memory overhead, and achieve comparable or even better forecasting accuracy.
MLF’s other designs, including MAP, IRF, and LWI also help better address multi-period characteristics and enhance TSF performance.
Nevertheless, there is still considerable room for exploration in model architectures that use historical inputs of different lengths simultaneously for prediction.
Future research could explore novel designs aimed at better addressing the challenges caused by multi-period characteristics for multi-period forecasting, thereby further releasing the predictive potential of multi-period inputs. To facilitate research, we have open-sourced the code.

## 6. Acknowledgements

This work is supported by the Ministry of Science and Technology of China, National Key Research and Development Program (No. 2021YFB3300503).

## References

* (1)
* Box et al. (2015)

  George EP Box, Gwilym M Jenkins, Gregory C Reinsel, and Greta M Ljung. 2015.
  *Time series analysis: forecasting and control*.
  John Wiley & Sons.
* Challu et al. (2022)

  C Challu, KG Olivares, BN Oreshkin, F Garza, M Mergenthaler, and A Dubrawski. 2022.
  N-hits: Neural hierarchical interpolation for time series forecasting. arXiv.
  *arXiv preprint arXiv:2201.12886* (2022).
* Chen et al. (2019)

  Cen Chen, Xiaolu Zhang, Sheng Ju, Chilin Fu, Caizhi Tang, Jun Zhou, and Xiaolong Li. 2019.
  AntProphet: an Intention Mining System behind Alipay’s Intelligent Customer Service Bot.. In *IJCAI*, Vol. 8. 6497–6499.
* Chen et al. (2016)

  Jou-Fan Chen, Wei-Lun Chen, Chun-Ping Huang, Szu-Hao Huang, and An-Pin Chen. 2016.
  Financial Time-Series Data Analysis Using Deep Convolutional Neural Networks. In *7th International Conference on Cloud Computing and Big Data, CCBD 2016, Macau, China, November 16-18, 2016*. IEEE Computer Society, 87–92.

  <https://doi.org/10.1109/CCBD.2016.027>
* Chen et al. (2024)

  Peng Chen, Yingying Zhang, Yunyao Cheng, Yang Shu, Yihang Wang, Qingsong Wen, Bin Yang, and Chenjuan Guo. 2024.
  Pathformer: Multi-scale transformers with Adaptive Pathways for Time Series Forecasting.
  *arXiv preprint arXiv:2402.05956* (2024).
* Chen et al. (2023)

  Si-An Chen, Chun-Liang Li, Nate Yoder, Sercan O Arik, and Tomas Pfister. 2023.
  Tsmixer: An all-mlp architecture for time series forecasting.
  *arXiv preprint arXiv:2303.06053* (2023).
* Chen et al. (2015)

  Tianqi Chen, Tong He, Michael Benesty, Vadim Khotilovich, Yuan Tang, Hyunsu Cho, Kailong Chen, Rory Mitchell, Ignacio Cano, Tianyi Zhou, et al. 2015.
  Xgboost: extreme gradient boosting.
  *R package version 0.4-2* 1, 4 (2015), 1–4.
* Cho et al. (2014)

  Kyunghyun Cho, Bart Van Merriënboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, and Yoshua Bengio. 2014.
  Learning phrase representations using RNN encoder-decoder for statistical machine translation.
  *arXiv preprint arXiv:1406.1078* (2014).
* Das et al. (2023)

  Abhimanyu Das, Weihao Kong, Andrew Leach, Shaan K Mathur, Rajat Sen, and Rose Yu. 2023.
  Long-term Forecasting with TiDE: Time-series Dense Encoder.
  *Transactions on Machine Learning Research* (2023).
* Elman (1990)

  Jeffrey L Elman. 1990.
  Finding structure in time.
  *Cognitive science* 14, 2 (1990), 179–211.
* Gu and Xu (2021)

  Zheng Gu and Yuhua Xu. 2021.
  Chaotic Dynamics Analysis Based on Financial Time Series.
  *Complex.* 2021 (2021), 2373423:1–2373423:6.

  <https://doi.org/10.1155/2021/2373423>
* Hochreiter and Schmidhuber (1997)

  Sepp Hochreiter and Jürgen Schmidhuber. 1997.
  Long short-term memory.
  *Neural computation* 9, 8 (1997), 1735–1780.
* Huang et al. (2017)

  Gao Huang, Zhuang Liu, Laurens Van Der Maaten, and Kilian Q Weinberger. 2017.
  Densely connected convolutional networks. In *Proceedings of the IEEE conference on computer vision and pattern recognition*. 4700–4708.
* Jin et al. (2023)

  Ming Jin, Shiyu Wang, Lintao Ma, Zhixuan Chu, James Y Zhang, Xiaoming Shi, Pin-Yu Chen, Yuxuan Liang, Yuan-Fang Li, Shirui Pan, et al. 2023.
  Time-LLM: Time Series Forecasting by Reprogramming Large Language Models. In *The Twelfth International Conference on Learning Representations*.
* Jordan (1997)

  Michael I Jordan. 1997.
  Serial order: A parallel distributed processing approach.
  In *Advances in psychology*. Vol. 121. Elsevier, 471–495.
* Krollner et al. (2010)

  Bjoern Krollner, Bruce J. Vanstone, and Gavin R. Finnie. 2010.
  Financial time series forecasting with machine learning techniques: a survey. In *18th European Symposium on Artificial Neural Networks, ESANN 2010, Bruges, Belgium, April 28-30, 2010, Proceedings*.

  <https://www.esann.org/sites/default/files/proceedings/legacy/es2010-50.pdf>
* Lee et al. (2015)

  Chen-Yu Lee, Saining Xie, Patrick W. Gallagher, Zhengyou Zhang, and Zhuowen Tu. 2015.
  Deeply-Supervised Nets. In *Proceedings of the Eighteenth International Conference on Artificial Intelligence and Statistics, AISTATS 2015, San Diego, California, USA, May 9-12, 2015* *(JMLR Workshop and Conference Proceedings, Vol. 38)*, Guy Lebanon and S. V. N. Vishwanathan (Eds.). JMLR.org.

  <http://proceedings.mlr.press/v38/lee15a.html>
* Li et al. (2018)

  Yaguang Li, Rose Yu, Cyrus Shahabi, and Yan Liu. 2018.
  Diffusion Convolutional Recurrent Neural Network: Data-Driven Traffic Forecasting. In *6th International Conference on Learning Representations, ICLR 2018, Vancouver, BC, Canada, April 30 - May 3, 2018, Conference Track Proceedings*. OpenReview.net.

  <https://openreview.net/forum?id=SJiHXGWAZ>
* Liu et al. (2021)

  Shizhan Liu, Hang Yu, Cong Liao, Jianguo Li, Weiyao Lin, Alex X Liu, and Schahram Dustdar. 2021.
  Pyraformer: Low-complexity pyramidal attention for long-range time series modeling and forecasting. In *International conference on learning representations*.
* Nie et al. (2022)

  Yuqi Nie, Nam H Nguyen, Phanwadee Sinthong, and Jayant Kalagnanam. 2022.
  A time series is worth 64 words: Long-term forecasting with transformers.
  *arXiv preprint arXiv:2211.14730* (2022).
* Oreshkin et al. (2019)

  Boris N Oreshkin, Dmitri Carpov, Nicolas Chapados, and Yoshua Bengio. 2019.
  N-BEATS: Neural basis expansion analysis for interpretable time series forecasting.
  *arXiv preprint arXiv:1905.10437* (2019).
* Sen et al. (2019)

  Rajat Sen, Hsiang-Fu Yu, and Inderjit S Dhillon. 2019.
  Think globally, act locally: A deep neural network approach to high-dimensional time series forecasting.
  *Advances in neural information processing systems* 32 (2019).
* Sezer et al. (2020)

  Omer Berat Sezer, Mehmet Ugur Gudelek, and Ahmet Murat Ozbayoglu. 2020.
  Financial time series forecasting with deep learning: A systematic literature review: 2005–2019.
  *Applied soft computing* 90 (2020), 106181.
* Shabani et al. (2022)

  Mohammad Amin Shabani, Amir H Abdi, Lili Meng, and Tristan Sylvain. 2022.
  Scaleformer: Iterative Multi-scale Refining Transformers for Time Series Forecasting. In *The Eleventh International Conference on Learning Representations*.
* Shao et al. (2022)

  Zezhi Shao, Zhao Zhang, Fei Wang, and Yongjun Xu. 2022.
  Pre-training enhanced spatial-temporal graph neural network for multivariate time series forecasting. In *Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining*. 1567–1577.
* Tan et al. (2024)

  Mingtian Tan, Mike A Merrill, Vinayak Gupta, Tim Althoff, and Thomas Hartvigsen. 2024.
  Are Language Models Actually Useful for Time Series Forecasting?
  *arXiv preprint arXiv:2406.16964* (2024).
* Tang et al. (2022)

  Yajiao Tang, Zhenyu Song, Yulin Zhu, Huaiyu Yuan, Maozhang Hou, Junkai Ji, Cheng Tang, and Jianqiang Li. 2022.
  A survey on machine learning models for financial time series forecasting.
  *Neurocomputing* 512 (2022), 363–380.

  <https://doi.org/10.1016/J.NEUCOM.2022.09.003>
* Taylor and Letham (2018)

  Sean J Taylor and Benjamin Letham. 2018.
  Forecasting at scale.
  *The American Statistician* 72, 1 (2018), 37–45.
* Tran et al. (2019)

  Dat Thanh Tran, Alexandros Iosifidis, Juho Kanniainen, and Moncef Gabbouj. 2019.
  Temporal Attention-Augmented Bilinear Network for Financial Time-Series Data Analysis.
  *IEEE Trans. Neural Networks Learn. Syst.* 30, 5 (2019), 1407–1418.

  <https://doi.org/10.1109/TNNLS.2018.2869225>
* Vaswani et al. (2017)

  Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. 2017.
  Attention is all you need.
  *Advances in neural information processing systems* 30 (2017).
* Wang et al. (2006)

  Xiaozhe Wang, Kate Smith, and Rob Hyndman. 2006.
  Characteristic-based clustering for time series data.
  *Data mining and knowledge Discovery* 13 (2006), 335–364.
* Wu et al. (2021)

  Haixu Wu, Jiehui Xu, Jianmin Wang, and Mingsheng Long. 2021.
  Autoformer: Decomposition transformers with auto-correlation for long-term series forecasting.
  *Advances in Neural Information Processing Systems* 34 (2021), 22419–22430.
* Wu et al. (2020)

  Zonghan Wu, Shirui Pan, Guodong Long, Jing Jiang, Xiaojun Chang, and Chengqi Zhang. 2020.
  Connecting the Dots: Multivariate Time Series Forecasting with Graph Neural Networks. In *KDD ’20: The 26th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, Virtual Event, CA, USA, August 23-27, 2020*, Rajesh Gupta, Yan Liu, Jiliang Tang, and B. Aditya Prakash (Eds.). ACM, 753–763.

  <https://doi.org/10.1145/3394486.3403118>
* Wu et al. (2019)

  Zonghan Wu, Shirui Pan, Guodong Long, Jing Jiang, and Chengqi Zhang. 2019.
  Graph WaveNet for Deep Spatial-Temporal Graph Modeling. In *Proceedings of the Twenty-Eighth International Joint Conference on Artificial Intelligence, IJCAI 2019, Macao, China, August 10-16, 2019*, Sarit Kraus (Ed.). ijcai.org, 1907–1913.

  <https://doi.org/10.24963/IJCAI.2019/264>
* Zang et al. (2023)

  Xiaoling Zang, Binbin Hu, Jun Chu, Zhiqiang Zhang, Guannan Zhang, Jun Zhou, and Wenliang Zhong. 2023.
  Commonsense Knowledge Graph towards Super APP and Its Applications in Alipay. In *Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining*. 5509–5519.
* Zeng et al. (2023)

  Ailing Zeng, Muxi Chen, Lei Zhang, and Qiang Xu. 2023.
  Are transformers effective for time series forecasting?. In *Proceedings of the AAAI conference on artificial intelligence*, Vol. 37. 11121–11128.
* Zeng (2008)

  Zhanggui Zeng. 2008.
  *Financial Time Series Analysis using Pattern Recognition Methods*.
  Ph. D. Dissertation. University of Sydney, Australia.

  <https://hdl.handle.net/2123/3558>
* Zhang et al. (2024b)

  Cheng Zhang, Nilam Nur Amir Sjarif, and Roslina Binti Ibrahim. 2024b.
  Deep learning models for price forecasting of financial time series: A review of recent advancements: 2020-2022.
  *WIREs Data. Mining. Knowl. Discov.* 14, 1 (2024).

  <https://doi.org/10.1002/WIDM.1519>
* Zhang et al. (2024a)

  Xu Zhang, Zhengang Huang, Yunzhi Wu, Xun Lu, Erpeng Qi, Yunkai Chen, Zhongya Xue, Peng Wang, and Wei Wang. 2024a.
  Self-Adaptive Scale Handling for Forecasting Time Series with Scale Heterogeneity. In *ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*. IEEE, 7485–7489.
* Zhang et al. (2018)

  Zhiqiang Zhang, Chaochao Chen, Jun Zhou, and Xiaolong Li. 2018.
  An Industrial-Scale System for Heterogeneous Information Card Ranking in Alipay. In *Database Systems for Advanced Applications - 23rd International Conference, DASFAA 2018, Gold Coast, QLD, Australia, May 21-24, 2018, Proceedings, Part II* *(Lecture Notes in Computer Science, Vol. 10828)*, Jian Pei, Yannis Manolopoulos, Shazia W. Sadiq, and Jianxin Li (Eds.). Springer, 713–724.

  <https://doi.org/10.1007/978-3-319-91458-9_44>
* Zhou et al. (2022a)

  Tian Zhou, Ziqing Ma, Qingsong Wen, Liang Sun, Tao Yao, Wotao Yin, Rong Jin, et al. 2022a.
  Film: Frequency improved legendre memory model for long-term time series forecasting.
  *Advances in Neural Information Processing Systems* 35 (2022), 12677–12690.
* Zhou et al. (2022b)

  Tian Zhou, Ziqing Ma, Qingsong Wen, Xue Wang, Liang Sun, and Rong Jin. 2022b.
  Fedformer: Frequency enhanced decomposed transformer for long-term series forecasting. In *International Conference on Machine Learning*. PMLR, 27268–27286.
* Zhou et al. (2023)

  Tian Zhou, Peisong Niu, Liang Sun, Rong Jin, et al. 2023.
  One fits all: Power general time series analysis by pretrained lm.
  *Advances in neural information processing systems* 36 (2023), 43322–43355.

## Appendix A Appendix

### A.1. More details about fund datasets

On the one hand, from the time series visualization in Figure [10](https://arxiv.org/html/2511.08622v1#A1.F10 "Figure 10 ‣ A.1. More details about fund datasets ‣ Appendix A Appendix ‣ Multi-period Learning for Financial Time Series Forecasting"), we can intuitively observe pattern differences between the Fund dataset and the public datasets. Influenced by long-term market conditions, short-term policy, and public opinion, the time series of fund sales exhibit steeper ascending and descending trends as well as more frequent fluctuations, containing complex semantics.

On the other hand, inspired by (Wang et al., [2006](https://arxiv.org/html/2511.08622v1#bib.bib32)), in Table [8](https://arxiv.org/html/2511.08622v1#A1.T8 "Table 8 ‣ A.1. More details about fund datasets ‣ Appendix A Appendix ‣ Multi-period Learning for Financial Time Series Forecasting"), we quantify the trend, periodicity, and kurtosis of the Fund dataset and other popular TSF public datasets. Fund dataset exhibits lower trend and periodicity along with higher kurtosis, indicating more complex TS (Wang et al., [2006](https://arxiv.org/html/2511.08622v1#bib.bib32)) and bringing more challenges for TSF tasks.

By introducing the Fund datasets, we intend to expand the public dataset repository for more comprehensive evaluations of TSF algorithms. The features of each fund product are as follows:

1. (1)

   “product\_pid” denotes the fund ID of the different fund products.
2. (2)

   “is\_summarydate” denotes whether the transaction date of the fund product is a summary date (fund products do not trade on holidays and weekends, and the trading volume during these periods is aggregated to the next non-holiday or non-weekend, called summary date).
3. (3)

   “apply\_amt” represents the applying transaction amount of the current fund product.
4. (4)

   “redeem\_amt” represents the redemption transaction amount of the current fund product.
5. (5)

   “during\_days” indicates the holding period of the current fund product (the number of days to hold the fund product before it can be traded).
6. (6)

   “is\_trad” indicates whether the current day is a trading day.
7. (7)

   “is\_weekend\_delay” indicates whether it is a weekend before a trading day.
8. (8)

   “holiday\_num” indicates how many statutory holidays occur before the trading day.

![Refer to caption](appendix_figure/series_comp_0120.png)

  


Figure 10. Time series visualization of Fund dataset (first two lines) and other public datasets.




Table 8. Average trends, periodicity, and kurtosis comparison.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Datasets | Fund | Electricity | ETTh1 | ETTm1 | Exchange | Illness |
| Trend | 0.74 | 0.84 | 0.86 | 0.86 | 1.0 | 0.71 |
| Periodicity | 0.62 | 0.92 | 0.72 | 0.74 | 0.31 | 0.81 |
| Kurtosis | 29.21 | 0.39 | 1.37 | 1.37 | -0.53 | 5.56 |

### A.2. More details about public datasets

The following public datasets are extensively used for TSF algorithm evaluation, covering four practical applications: energy, economics, weather, and disease:

1. (1)

   The Electricity dataset collects the electricity consumption (kWh) every 15 minutes of 321 clients from 2012 to 2014.
2. (2)

   The ETT dataset comprises two sub-datasets, ETT1 and ETT2, collected from two separate counties. Each sub-dataset offers two versions with varying sampling resolutions (15 minutes and 1 hour). ETT dataset includes multiple time series of electrical loads and a single time sequence of oil temperature.
3. (3)

   The Weather dataset contains 21 meteorological indicators, such as air temperature, humidity, etc, recorded every 10 minutes for the entirety of 2020.
4. (4)

   Exchange dataset contains real-time exchange rates for eight different countries.
5. (5)

   The Illness dataset contains data on patients with influenza-like illnesses in the United States.

We have made the Fund and public datasets available at the link111<https://drive.google.com/drive/folders/1IecxNQqH6hYEgaZT70t273BFHV-WeIw1?usp=sharing>. Our code link222<https://github.com/Meteor-Stars/MLF> provides the all data processing scripts.

Table 9. More comparison results of short-term TSF task on the collected Fund dataset.

|  |  | MLF | | Autoformer | | FEDformer | | LSTM | | RNN | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | MSE | WMA. | MSE | WMA. | MSE | WMA. | MSE | WMA. | MSE | WMA. |
| Fund | 1 | 33.85 | 75.84 | 36.5 | 82.17 | 36.85 | 80.31 | 51.41 | 85.91 | 36.2 | 79.82 |
|  | ±\pm0.033 | ±\pm0.093 | ±\pm0.027 | ±\pm0.007 | ±\pm0.002 | ±\pm0.003 | ±\pm0.18 | ±\pm0.18 | ±\pm0.08 | ±\pm0.06 |
| 5 | 38.28 | 80.37 | 45.45 | 93.79 | 47.92 | 97.4 | 62.98 | 101.88 | 40.42 | 83.52 |
|  | ±\pm0.029 | ±\pm0.071 | ±\pm0.038 | ±\pm0.004 | ±\pm0.038 | ±\pm0.003 | ±\pm0.18 | ±\pm0.17 | ±\pm0.02 | ±\pm0.06 |
| 8 | 41.94 | 86.06 | 51.05 | 99.9 | 45.2 | 90.3 | 69.94 | 109.04 | 44.69 | 89.74 |
|  | ±\pm0.031 | ±\pm0.123 | ±\pm0.144 | ±\pm0.007 | ±\pm0.001 | ±\pm0.001 | ±\pm0.1 | ±\pm0.03 | ±\pm0.04 | ±\pm0.11 |
| 10 | 44.42 | 88.66 | 52.72 | 100.35 | 47.1 | 91.92 | 71.68 | 109.78 | 46.67 | 91.55 |
|  | ±\pm0.057 | ±\pm0.041 | ±\pm0.104 | ±\pm0.003 | ±\pm0.037 | ±\pm0.001 | ±\pm0.11 | ±\pm0.08 | ±\pm0.06 | ±\pm0.13 |
|  |  | DLinear | | GRU | | XGBoost | | Prophet | | ARIMA | |
|  | MSE | WMA. | MSE | WMA. | MSE | WMA. | MSE | WMA. | MSE | WMA. |
| Fund | 1 | 97.23 | 158.72 | 51.57 | 85.35 | 49.29 | 93.07 | 66.5 | 128.18 | 46.64 | 103.71 |
|  | ±\pm0.009 | ±\pm0.002 | ±\pm0.03 | ±\pm0.01 | - | - | - | - | - | - |
| 5 | 99.50 | 159.95 | 59.21 | 93.95 | 53.55 | 95.86 | 93.75 | 154.62 | 49.56 | 105.51 |
|  | ±\pm0.004 | ±\pm0.003 | ±\pm0.15 | ±\pm0.23 | - | - | - | - | - | - |
| 8 | 95.37 | 148.25 | 66.54 | 102.56 | 57.23 | 101.97 | 136.97 | 180.16 | 53.11 | 108.6 |
|  | ±\pm0.005 | ±\pm0.004 | ±\pm0.08 | ±\pm0.11 | - | - | - | - | - | - |
| 10 | 90.70 | 142.89 | 69.0 | 104.86 | 58.53 | 101.7 | 171.59 | 194.13 | 54.35 | 108.91 |
|  | ±\pm0.005 | ±\pm0.004 | ±\pm0.07 | ±\pm0.11 | - | - | - | - | - | - |




Table 10. Extra result of short-term TSF task on the public datasets.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | MLF | | Autoformer | | FEDformer | | LSTM | | DLinear | | RNN | | GRU | |
| MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE |
| ETTh1 | 0.0873 | 0.1899 | 0.2213 | 0.3429 | 0.2318 | 0.3495 | 0.1318 | 0.2389 | 0.2320 | 0.3345 | 0.1139 | 0.2224 | 0.1074 | 0.2146 |
| ETTm1 | 0.0412 | 0.1245 | 0.0496 | 0.1382 | 0.0489 | 0.136 | 0.0458 | 0.1366 | 0.0659 | 0.1682 | 0.045 | 0.1357 | 0.0453 | 0.1349 |
| Illness | 0.1493 | 0.2188 | 0.3006 | 0.3367 | 0.3081 | 0.3409 | 0.852 | 0.5899 | 0.7842 | 0.6832 | 0.4092 | 0.3739 | 0.3688 | 0.3363 |
| Excha. | 0.0029 | 0.0267 | 0.0186 | 0.0959 | 0.0101 | 0.0685 | 0.015 | 0.0835 | 0.0080 | 0.0576 | 0.0094 | 0.0634 | 0.0079 | 0.0601 |



![Refer to caption](appendix_figure/case_vis_fund_merge_allv2.jpg)

Figure 11. Visualizations of forecasting future 5 and 10 time steps on MLF and two strong baselines (Scaleformer and PtachTST) on Fund dataset.

### A.3. Extra results for short-term TSF task

Here we compare MLF with more TSF baselines:

1. (1)

   Popular transformer models Autoformer (Wu et al., [2021](https://arxiv.org/html/2511.08622v1#bib.bib33)) and FEDformer (Zhou et al., [2022b](https://arxiv.org/html/2511.08622v1#bib.bib43)).
2. (2)

   Popular neural networks LSTM (Hochreiter and Schmidhuber, [1997](https://arxiv.org/html/2511.08622v1#bib.bib13)), RNN (Jordan, [1997](https://arxiv.org/html/2511.08622v1#bib.bib16); Elman, [1990](https://arxiv.org/html/2511.08622v1#bib.bib11)), GRU (Cho et al., [2014](https://arxiv.org/html/2511.08622v1#bib.bib9)) and DLinear (Zeng et al., [2023](https://arxiv.org/html/2511.08622v1#bib.bib37)).
3. (3)

   Popular machine learning models XGBoost (Chen et al., [2015](https://arxiv.org/html/2511.08622v1#bib.bib8)), Prophet (Taylor and Letham, [2018](https://arxiv.org/html/2511.08622v1#bib.bib29)) and ARIMA (Box et al., [2015](https://arxiv.org/html/2511.08622v1#bib.bib2)).

For ARIMA, the auto-regressive order, differencing order, and moving average order are all set as 1 for better performance. For Prophet, the growth, changepoint range, and changepoint prior scale are set as “linear”, 0.8 and 0.1 respectively. The seasonality prior scale and holidays prior scale are set as 10 for better performance. For XGBoost, the learning rate, max depth, and the number of estimators are set as 0.3, 12, and 1000 respectively. We use time and variable lag information to construct features for better performance. For LSTM, RNN, and GRU, the number of hidden layers is 3. The hidden size is set as 1024.
For Autoformer and FEDformer, as with the baseline approach in the main experiments, we use the recommended hyperparameters in baseline codes.

The comparison results on Fund dataset and public datasets are shown in Table [9](https://arxiv.org/html/2511.08622v1#A1.T9 "Table 9 ‣ A.2. More details about public datasets ‣ Appendix A Appendix ‣ Multi-period Learning for Financial Time Series Forecasting") and Table [10](https://arxiv.org/html/2511.08622v1#A1.T10 "Table 10 ‣ A.2. More details about public datasets ‣ Appendix A Appendix ‣ Multi-period Learning for Financial Time Series Forecasting") respectively.
Results show that the overall accuracy of MLF is the best and second is RNN.
The traditional machine learning models have not gained an advantage in predicting fund sales.
Moreover, we observed that models that perform well in long-term TSF task (e.g., DLinear, Autoformer, and FEDformer) do not perform as well in short-term TSF task, while MLF achieves desirable results in both short-term and long-term TSF tasks.
This indicates the superiority of MLF.

### A.4. Extra results for patch squeeze module

Table [11](https://arxiv.org/html/2511.08622v1#A1.T11 "Table 11 ‣ A.5. Visualizations of forecasting on Fund dataset ‣ Appendix A Appendix ‣ Multi-period Learning for Financial Time Series Forecasting") shows the effectiveness of the patch squeeze module on the ETTm1 dataset.
We also have applied Patch Squeeze to PatchTST with fixed input length 1536. Specifically, on weather dataset, the average error of original PatchTST is 0.2554, with training epoch time 248.87s. while setting squeeze factor as 2 or 4, corresponding results are 0.2550 or 0.260 and 83.50s or 44.26s, indicating remarkable improvements in efficiency. The same conclusion is reached on the ETTm datasets. This further demonstrates that the simple but effective Patch Squeeze module significantly improves efficiency while maintaining good accuracy.

### A.5. Visualizations of forecasting on Fund dataset

As shown in Figure [11](https://arxiv.org/html/2511.08622v1#A1.F11 "Figure 11 ‣ A.2. More details about public datasets ‣ Appendix A Appendix ‣ Multi-period Learning for Financial Time Series Forecasting"), we visualize the forecasting of MLF and two strong baselines (Scaleformer and PatchTST) on the Fund dataset. The visualization shows that MLF can better forecast the steeper ascending and descending trends, indicating the superiority of MLF, which utilizes customized designs for addressing and using multi-period inputs for better TSF effect.

Table 11. Extra results about the effectiveness of patch squeeze module: MLF’s accuracy with squeeze factors 2 (MLF-2), 4 (MLF-4), and 8 (MLF-8).

|  |  | PatchTST | | MLF-2 | | MLF-4 | | MLF-8 | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | MSE | MAE | MSE | MAE | MSE | MAE | MSE | MAE |
| ETTm2 | 96 | 0.166 | 0.256 | 0.164 | 0.254 | 0.163 | 0.253 | 0.164 | 0.252 |
| 192 | 0.223 | 0.296 | 0.220 | 0.295 | 0.218 | 0.295 | 0.223 | 0.297 |
| 336 | 0.277 | 0.336 | 0.275 | 0.330 | 0.269 | 0.329 | 0.270 | 0.330 |
| 720 | 0.357 | 0.381 | 0.343 | 0.380 | 0.346 | 0.378 | 0.344 | 0.379 |