---
authors:
- Kaito Takano
- Masanori Hirano
- Kei Nakagawa
doc_id: arxiv:2511.02469v1
family_id: arxiv:2511.02469
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for
  Monetary Policy Decision Classification
url_abs: http://arxiv.org/abs/2511.02469v1
url_html: https://arxiv.org/html/2511.02469v1
venue: arXiv q-fin
version: 1
year: 2025
---


Kaito Takano
  
Masanori Hirano
  
Kei Nakagawa

###### Abstract

Accurately forecasting central bank policy decisions, particularly those of the Federal Open Market Committee (FOMC) has become increasingly important amid heightened economic uncertainty. While prior studies have used monetary policy texts to predict rate changes, most rely on static classification models that overlook the deliberative nature of policymaking. This study proposes a novel framework that structurally imitates the FOMC’s collective decision-making process by modeling multiple large language models (LLMs) as interacting agents. Each agent begins with a distinct initial belief and produces a prediction based on both qualitative policy texts and quantitative macroeconomic indicators. Through iterative rounds, agents revise their predictions by observing the outputs of others, simulating deliberation and consensus formation. To enhance interpretability, we introduce a latent variable representing each agent’s underlying belief (e.g., hawkish or dovish), and we theoretically demonstrate how this belief mediates the perception of input information and interaction dynamics. Empirical results show that this debate-based approach significantly outperforms standard LLMs-based baselines in prediction accuracy. Furthermore, the explicit modeling of beliefs provides insights into how individual perspectives and social influence shape collective policy forecasts.

††This paper does not reflect the view of the organizations the authors belong to. All errors in this paper are the responsibility of the authors.

## 1 Introduction

Monetary policy decision makings by central banks, especially changes in policy interest rates, have direct effects on financial markets and the cost of capital in the real economy [[29](https://arxiv.org/html/2511.02469v1#bib.bib29), [22](https://arxiv.org/html/2511.02469v1#bib.bib22), [15](https://arxiv.org/html/2511.02469v1#bib.bib15)].
Among central banks, the Federal Open Market Committee (FOMC) of the U.S. is one of the most closely watched decision-making bodies in the world. Its policy rate decisions have significant influence not only on the U.S. economy but also on global financial markets. When the FOMC raises interest rates, U.S. dollar–denominated assets become more attractive, encouraging capital inflows into the United States. As a result, other countries—particularly emerging markets—often experience capital outflows, currency depreciation, and tighter financial conditions [[16](https://arxiv.org/html/2511.02469v1#bib.bib16), [4](https://arxiv.org/html/2511.02469v1#bib.bib4), [6](https://arxiv.org/html/2511.02469v1#bib.bib6)].

The FOMC consists of 12 voting members: 7 governors from the Federal Reserve Board and 5 presidents of regional Federal Reserve Banks.
The committee meets eight times per year to determine the target range for the federal funds rate by majority vote.
Each member has a unique background, shaped by their region and area of expertise, and thus brings a different beliefs to monetary policy.
These beliefs are often categorized as either “dovish” (favoring more accommodative policy) or “hawkish” (favoring tighter policy).
The FOMC’s decision-making process is designed to reflect these diverse views.
During each meeting, members present their policy beliefs, engage in debates, and ultimately reach a consensus.
On the final day of the meeting, the committee releases a policy statement that announces the interest rate decision and outlines the economic reasoning behind it.111<https://www.federalreserve.gov/monetarypolicy/fomc.htm>
To inform these decisions, the FOMC uses various types of information, including macroeconomic indicators such as the inflation rate.
In addition, it consults the Beige Book, a qualitative report that reflects regional economic conditions.
The Beige Book is published two weeks before each FOMC meeting and is compiled by the twelve regional Federal Reserve Banks. It summarizes findings from interviews with local businesses and stakeholders. Unlike typical economic data, the Beige Book is released in textual form and contains unstructured qualitative information.222<https://www.federalreserve.gov/monetarypolicy/publications/beige-book-default.htm>
With the increasing complexity of economic conditions and the acceleration of inflation, accurately predicting both the timing and direction of monetary policy decisions has become a critical challenge for macroprudential policy design and investment strategy development like [[12](https://arxiv.org/html/2511.02469v1#bib.bib12), [21](https://arxiv.org/html/2511.02469v1#bib.bib21), [3](https://arxiv.org/html/2511.02469v1#bib.bib3)].
In parallel, central banks themselves are increasingly adopting AI technologies.
As monetary policy communication becomes more sophisticated and real-time analytics are further developed, external market participants are also expected to adopt more advanced analytical tools [[10](https://arxiv.org/html/2511.02469v1#bib.bib10), [2](https://arxiv.org/html/2511.02469v1#bib.bib2)].
With this background, this study addresses the problem of predicting policy rate decisions made by the FOMC.

Many literature has attempted to forecast monetary policy decisions and market responses by analyzing the content of central bank communications, particularly unstructured policy texts such as the Beige Book and FOMC statements [[14](https://arxiv.org/html/2511.02469v1#bib.bib14), [30](https://arxiv.org/html/2511.02469v1#bib.bib30), [11](https://arxiv.org/html/2511.02469v1#bib.bib11)]. These studies typically focus on extracting features from the text such as tone, sentiment, or keyword frequencies and apply regression-based approaches to link them with policy outcomes or market variables.

However, existing approaches face two main limitations.
First, they fail to account for the deliberative decision-making process that is intrinsic to the institutional structure of the FOMC [[32](https://arxiv.org/html/2511.02469v1#bib.bib32), [19](https://arxiv.org/html/2511.02469v1#bib.bib19)].
As described earlier, FOMC members express divergent policy beliefs informed by differing economic perspectives, and these views are gradually reconciled through discussion and debate to form a final consensus.
Yet, many prior studies treat the FOMC as a single unified decision-making entity, neglecting the internal dynamics and diversity of beliefs within the committee.

Second, most existing methods rely on static text analysis based on dictionaries or single-model predictions [[14](https://arxiv.org/html/2511.02469v1#bib.bib14), [30](https://arxiv.org/html/2511.02469v1#bib.bib30), [11](https://arxiv.org/html/2511.02469v1#bib.bib11)].
As a result, they struggle to integrate macroeconomic indicators with textual information in a cohesive manner, and they lack the capacity to model how individual beliefs emerge and evolve among committee members during the policy formation process.

To address the aforementioned challenges, this study proposes a novel descriptive framework for policy rate determination that structurally simulates the deliberative decision-making process of the FOMC.
The proposed framework models the process using multiple pre-trained LLMs, each acting as an autonomous agent.
Each LLM-based agent represents an FOMC member with a distinct policy beliefs—such as dovish or hawkish—and operates independently.
Each agent receives as input a combination of qualitative information and quantitative macroeconomic indicators.
Based on this input, the agent generates an initial policy decision.
Then, in successive rounds, each agent sequentially observes the decisions made by other agents and updates its own output accordingly.
In each round, agents revise their decisions by incorporating the judgments of others as part of an ongoing debate.
This iterative, interdependent process is designed to structurally mimic the institutional dynamics of actual FOMC meetings, namely, the expression of beliefs, debate, beliefs adjustment, and eventual consensus formation.

Furthermore, following [[9](https://arxiv.org/html/2511.02469v1#bib.bib9)], we explicitly model each agent’s internal policy beliefs as a discrete latent variable. We assume that the policy label is generated probabilistically based on this latent stance, and we formalize the decision process as a Bayesian generative model.
Theoretically, the output of each agent is generated as a function of (i) the input data (text and macroeconomic indicators), (ii) the observed decisions of other agents, and (iii) the agent’s own latent belief, serving as a mediating variable. This structure can capture the interaction between external evidence, peer influence, and individual predispositions.

The goal of this study is to answer two research questions using the proposed structural framework.
Although debate-based multi-agent LLMs have proven effective in enhancing reasoning, accuracy, and consensus-building [[8](https://arxiv.org/html/2511.02469v1#bib.bib8), [5](https://arxiv.org/html/2511.02469v1#bib.bib5), [18](https://arxiv.org/html/2511.02469v1#bib.bib18)], there is no existing research that applies structured debate-based LLM frameworks specifically to the financial domain.

First, we empirically evaluate whether the proposed model can replicate actual FOMC policy decisions. Specifically, we test whether the model, given the Beige Book and macroeconomic indicators available before each FOMC meeting, can produce the same decision outcome as the actual FOMC. This serves as an empirical validation of whether our model, which incorporates the institutional features of the FOMC, also possesses practical predictive power.

Second, we aim to identify which components of the proposed framework are most critical for decision-making. To this end, we conduct an ablation study to quantitatively assess the contribution of various components—including textual information, macroeconomic variables, peer agent outputs, and latent beliefs variables. This analysis reveals the key informational and structural factors that drive interest rate decisions in our framework.

## 2 Related Work

Recent advances in LLMs have been remarkable. Notably, cutting-edge models such as ChatGPT [[23](https://arxiv.org/html/2511.02469v1#bib.bib23)], GPT-4 [[24](https://arxiv.org/html/2511.02469v1#bib.bib24)], Claude, and Gemini have demonstrated performance and generalizability far beyond previous models, finding applications across diverse fields. These models trace their origins to the Transformer architecture [[35](https://arxiv.org/html/2511.02469v1#bib.bib35)], evolving through subsequent developments including BERT [[7](https://arxiv.org/html/2511.02469v1#bib.bib7)] and the GPT series [[27](https://arxiv.org/html/2511.02469v1#bib.bib27), [28](https://arxiv.org/html/2511.02469v1#bib.bib28), [17](https://arxiv.org/html/2511.02469v1#bib.bib17)], ultimately leading to the emergence of LLMs.

Since LLMs are trained on diverse texts, they acquire thought patterns that people have.
This capability has been leveraged in research applications such as opinion research, which can generate responses specific to demographic characteristics or individual preferences [[26](https://arxiv.org/html/2511.02469v1#bib.bib26), [13](https://arxiv.org/html/2511.02469v1#bib.bib13)].

Furthermore, Park et al. [[25](https://arxiv.org/html/2511.02469v1#bib.bib25)] constructed an RPG-style social simulation featuring LLM-based agents with various roles to investigate how new social structures form. Additionally, ResearchTown [[36](https://arxiv.org/html/2511.02469v1#bib.bib36)] - an LLM-based research community simulation environment - was developed to model and analyze the emergence of new academic papers through collaborative research among scholars. Takata et al. [[34](https://arxiv.org/html/2511.02469v1#bib.bib34)] developed an LLM-based multi-agent environment to examine the mechanisms underlying the manifestation of individual characteristics.

Building upon these studies, this study investigates whether LLMs can reproduce the process of collective decision-making in the financial domain.

It is well established that when multiple decision-making entities interact, complex behaviors emerge rather than linear patterns.
Notable studies include those by Schelling [[31](https://arxiv.org/html/2511.02469v1#bib.bib31), [31](https://arxiv.org/html/2511.02469v1#bib.bib31)] and Axelrod [[1](https://arxiv.org/html/2511.02469v1#bib.bib1)], which demonstrate that when numerous agents with extremely simple decision-making behaviors interact, phenomena such as segregation and cultural diversity can emerge.
Similarly, in financial markets, Lux et al. [[20](https://arxiv.org/html/2511.02469v1#bib.bib20)] demonstrated that agent interactions are crucial for reproducing stylized facts in financial market simulations.

Given those backgrounds, this study aims to reproduce the decision-making process by simulating interactions among members of the FOMC using LLMs, with the goal of reproducing the complex collective decision-making behavior of the members.

## 3 Problem Formulation

In this study, we consider a three-class classification problem to predict the central bank’s next policy rate decision (Raise, Hold, or Lower) based on financial texts and associated numerical macroeconomic data.

Unlike conventional supervised learning approaches that optimize model parameters using labeled training data, our approach relies on LLMs that have already been pre-trained. These LLMs are used directly for prediction without additional parameter tuning.

Let xx denote a financial text, and let v∈ℝdv\in\mathbb{R}^{d} denote a vector of relevant numerical indicators. Here, xx is a natural language document, whose length and structure can vary. The vector vv summarizes dd-dimensional quantitative macroeconomic indicators relevant to policy decisions, such as recent inflation or unemployment rates.

The corresponding label yy is an element of the discrete set 𝒴\mathcal{Y} representing the policy rate decision:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒴={Raise,Hold,Lower}\displaystyle\mathcal{Y}=\{\text{Raise},\,\text{Hold},\,\text{Lower}\} |  | (1) |

Our dataset consists of tuples of past published texts, the numerical indicators available at the time, and the actual policy decision made by the central bank. However, we do not fine-tune the model using these data.

Instead, each LLM receives the input pair (x,v)(x,v) as a prompt and generates a prediction z∈𝒴z\in\mathcal{Y} based on its fixed, pre-trained parameters ϕ\phi:

|  |  |  |  |
| --- | --- | --- | --- |
|  | z∼PLLM​(z∣x,v,ϕ)\displaystyle z\sim P\_{\mathrm{LLM}}\bigl(z\mid x,\,v,\,\phi\bigr) |  | (2) |

This formulation treats the LLM as a probabilistic predictor over the set of possible policy actions, conditioned on both textual and numerical inputs.

## 4 Proposed Method

In this study, we propose a framework in which a total of nn LLMs act as agents and conduct a multi-round debate over TT iterations to reach a collective decision for classification.

Each agent ii has pre-trained parameters ϕi\phi\_{i} and receives as input a financial text xx and numerical vector vv. At the initial round t=0t=0, agent ii independently generates a policy label based on its own model as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | zi(0)∼PLLM​(z∣x,v,ϕi),zi(0)∈𝒴.\displaystyle z\_{i}^{(0)}\sim P\_{\mathrm{LLM}}\bigl(z\mid x,\,v,\,\phi\_{i}\bigr),\qquad z\_{i}^{(0)}\in\mathcal{Y}. |  | (3) |

Here, zi(0)z\_{i}^{(0)} represents the initial label proposed by agent ii. The distribution PLLM(⋅∣x,v,ϕi)P\_{\mathrm{LLM}}(\cdot\mid x,v,\phi\_{i}) is fully determined by the fixed pre-trained parameters ϕi\phi\_{i} of agent ii.

From round t≥1t\geq 1 onward, each agent observes the set of predictions made by all agents in the previous round:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z(t−1)={z1(t−1),z2(t−1),…,zn(t−1)},\displaystyle Z^{(t-1)}=\bigl\{\,z\_{1}^{(t-1)},\,z\_{2}^{(t-1)},\,\dots,\,z\_{n}^{(t-1)}\bigr\}, |  | (4) |

and updates its prediction accordingly:

|  |  |  |  |
| --- | --- | --- | --- |
|  | zi(t)∼PLLM​(z∣x,v,Z(t−1),ϕi),zi(t)∈𝒴.\displaystyle z\_{i}^{(t)}\sim P\_{\mathrm{LLM}}\bigl(z\mid x,\,v,\,Z^{(t-1)},\,\phi\_{i}\bigr),\qquad z\_{i}^{(t)}\in\mathcal{Y}. |  | (5) |

The conditional distribution PLLM(⋅∣x,v,Z(t−1),ϕi)P\_{\mathrm{LLM}}(\cdot\mid x,\,v,\,Z^{(t-1)},\,\phi\_{i}) represents the agent’s output distribution given not only the original inputs (x,v)(x,v), but also the collective output of all agents in the previous round Z(t−1)Z^{(t-1)} as additional context.

For instance, agent ii may incorporate the opinions of others along with updated macroeconomic indicators such as inflation and unemployment into its prompt. This allows the agent to refine its judgment by comparing its beliefs with others and the latest data.

This iterative process forms a debate-based decision-making framework, where each agent updates its output in each round by considering both the opinions of others and the economic data.

At the final round TT, let a​(⋅)a(\cdot) denote a label extraction function that maps each agent’s response to a canonical decision. If all agents agree on the same label, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | a​(z1(T))=a​(z2(T))=⋯=a​(zn(T)),\displaystyle a\bigl(z\_{1}^{(T)}\bigr)=a\bigl(z\_{2}^{(T)}\bigr)=\cdots=a\bigl(z\_{n}^{(T)}\bigr), |  | (6) |

then the shared label z=a​(zi(T))z=a(z\_{i}^{(T)}) is adopted as the final prediction, and the debate terminates. If consensus is not achieved after the maximum number of rounds TT, the label with the highest number of supporting agents is selected as the final output.

### 4.1 Latent Policy Beliefs

While the debate-based framework described above enables iterative opinion exchange among agents, it lacks transparency in explaining why each agent selects a particular label, that is, the internal policy beliefs remains a black box.
To address this, we introduce an explicit latent variable representing the agent’s underlying policy beliefs, following the framework proposed by [[9](https://arxiv.org/html/2511.02469v1#bib.bib9)].
This latent variable, referred to as a hawk-dove stance, governs how each agent interprets the input text xx and numerical data vv.

We define a discrete latent space of policy stances as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Θ={θ1,θ2,…,θK},\displaystyle\Theta=\{\theta\_{1},\,\theta\_{2},\,\dots,\,\theta\_{K}\}, |  | (7) |

where each element θk\theta\_{k} represents a cluster of policy beliefs, such as strongly hawkish (favoring aggressive rate hikes), moderately hawkish, or dovish (favoring monetary easing).
The cardinality K=|Θ|K=|\Theta| denotes the number of distinct stance categories.

Suppose agent ii is given the input text xx, numerical data vv, and the set of labels from the previous round,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z(t)={z1(t),z2(t),…,zn(t)},\displaystyle Z^{(t)}=\{z\_{1}^{(t)},\,z\_{2}^{(t)},\,\dots,\,z\_{n}^{(t)}\}, |  | (8) |

and outputs a label in round t+1t+1. The probability of its response is modeled as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | PLLM​(zi(t+1)∣x,v,Z(t),ϕi),\displaystyle P\_{\mathrm{LLM}}\bigl(z\_{i}^{(t+1)}\mid x,\,v,\,Z^{(t)},\,\phi\_{i}\bigr), |  | (9) |

which can be expanded via marginalization over the latent beliefs variable θ∈Θ\theta\in\Theta as follows.

###### Lemma 1(Latent Beliefs Decomposition)

|  |  |  |
| --- | --- | --- |
|  | PLLM​(zi(t+1)∣x,v,Z(t),ϕi)\displaystyle P\_{\mathrm{LLM}}\bigl(z\_{i}^{(t+1)}\mid x,\,v,\,Z^{(t)},\,\phi\_{i}\bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =∑θ∈ΘP​(zi(t+1)∣θ,x,v,Z(t),ϕi)​P​(θ∣x,v,Z(t),ϕi).\displaystyle~~=\sum\_{\theta\in\Theta}P\bigl(z\_{i}^{(t+1)}\mid\theta,\,x,\,v,\,Z^{(t)},\,\phi\_{i}\bigr)\,P\bigl(\theta\mid x,\,v,\,Z^{(t)},\,\phi\_{i}\bigr). |  | (10) |

Here, P​(zi(t+1)∣θ,x,v,Z(t),ϕi)P(z\_{i}^{(t+1)}\mid\theta,\,x,\,v,\,Z^{(t)},\,\phi\_{i}) represents the conditional probability that agent ii outputs label zi(t+1)z\_{i}^{(t+1)} given a known stance θ\theta, observed inputs xx, vv, and previous agent responses Z(t)Z^{(t)}. The posterior distribution P​(θ∣x,v,Z(t),ϕi)P(\theta\mid x,\,v,\,Z^{(t)},\,\phi\_{i}) captures the probability that agent ii adopts belief θ\theta after observing xx, vv, and Z(t)Z^{(t)}.

###### Assumption 1 (Conditional Independence Given Latent Belief)

For any round tt and any belief θ∈Θ\theta\in\Theta, the output zi(t+1)z\_{i}^{(t+1)} by agent ii is conditionally independent of xx, vv, and Z(t)Z^{(t)} once θ\theta is known:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(zi(t+1)∣θ,x,v,Z(t),ϕi)=P​(zi(t+1)∣θ,ϕi)(∀θ∈Θ,t≥0).\displaystyle P\bigl(z\_{i}^{(t+1)}\mid\theta,\,x,\,v,\,Z^{(t)},\,\phi\_{i}\bigr)=P\bigl(z\_{i}^{(t+1)}\mid\theta,\,\phi\_{i}\bigr)\quad(\forall\,\theta\in\Theta,\;t\geq 0). |  | (11) |

This assumption implies that once the belief θ\theta is fixed, the final label output becomes independent of the input text xx, numerical data vv, and others’ responses.

Under this assumption, the output probability can be simplified as follows.

###### Lemma 2(Posterior Decomposition)

Given Assumption [11](https://arxiv.org/html/2511.02469v1#S4.E11 "In Assumption 1 (Conditional Independence Given Latent Belief) ‣ 4.1 Latent Policy Beliefs ‣ 4 Proposed Method ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification"), the output probability in Equation ([9](https://arxiv.org/html/2511.02469v1#S4.E9 "In 4.1 Latent Policy Beliefs ‣ 4 Proposed Method ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification")) reduces to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | PLLM​(zi(t+1)∣x,v,Z(t),ϕi)=∑θ∈ΘP​(zi(t+1)∣θ,ϕi)​P​(θ∣x,v,Z(t),ϕi).\displaystyle P\_{\mathrm{LLM}}\bigl(z\_{i}^{(t+1)}\mid x,\,v,\,Z^{(t)},\,\phi\_{i}\bigr)=\sum\_{\theta\in\Theta}P\bigl(z\_{i}^{(t+1)}\mid\theta,\,\phi\_{i}\bigr)\,P\bigl(\theta\mid x,\,v,\,Z^{(t)},\,\phi\_{i}\bigr). |  | (12) |

Moreover, the posterior distribution over stances is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(θ∣x,v,Z(t),ϕi)∝P​(x,v∣θ,ϕi)​P​(θ∣ϕi)​∏j=1nP​(zj(t)∣θ,ϕi).\displaystyle P\bigl(\theta\mid x,\,v,\,Z^{(t)},\,\phi\_{i}\bigr)\;\propto\;P\bigl(x,\,v\mid\theta,\,\phi\_{i}\bigr)\,P\bigl(\theta\mid\phi\_{i}\bigr)\,\prod\_{j=1}^{n}P\bigl(z\_{j}^{(t)}\mid\theta,\,\phi\_{i}\bigr). |  | (13) |

Here, P​(zj(t)∣θ,ϕi)P(z\_{j}^{(t)}\mid\theta,\,\phi\_{i}) is the probability that agent jj produces label zj(t)z\_{j}^{(t)} given stance θ\theta. The term P​(x,v∣θ,ϕi)P(x,v\mid\theta,\phi\_{i}) is the likelihood of observing (x,v)(x,v) under belief θ\theta, and P​(θ∣ϕi)P(\theta\mid\phi\_{i}) represents the prior belief distribution of agent ii.
The product term reflects how well the previous responses of other agents support belief θ\theta.

Using this framework, each agent determines its own belief θ\theta by jointly considering the input text xx, numerical indicators vv, and the previous outputs from other agents. Once a belief θ\theta is selected, the agent generates its final label conditioned on that belief.
These lemmas provide a formal foundation for modeling the internal reasoning process of each agent. Specifically, they describe how an agent interprets input signals, selects a monetary policy belief, and generates a final decision in a mathematically consistent manner.

## 5 Experiment

In this section, we conduct two experiments to evaluate the effectiveness of our framework.
First, we test whether our model can reproduce actual FOMC policy decisions (Raise, Hold, or Lower) using the Beige Book and macroeconomic indicators available before each meeting.
Second, we perform an ablation study to analyze the contribution of each component in our model such as textual information, numerical indicators, peer predictions, and belief variables to overall prediction performance.

### 5.1 Dataset

Our empirical analysis spans all scheduled FOMC meetings from January 2000 to December 2025.
The next subsections describe three sources of information that match the inputs used by our agents.

#### 5.1.1 Policy Rate:

As our target variable, we use the actual federal funds policy rate decision made by the FOMC at each meeting.
We classify each decision into one of three categories: Raise, Hold, or Lower, based on changes in the target range of the policy rate compared to the previous meeting.
We also use as an input to the LLM, since information on the current level and trend of the policy rate may be important in decision the policy rate.
We obtain this data from the Bloomberg terminal333<https://www.bloomberg.com/professional/products/bloomberg-terminal/>.

#### 5.1.2 Macroeconomic Indicators:

To construct the input data for our model, we use both macroeconomic indicators and qualitative policy texts.
In accordance with the Federal Reserve’s dual mandate: maximum employment and price stability, we use the unemployment rate and the inflation rate as macroeconomic indicators.
We obtain these data from the Federal Reserve Economic Data (FRED) database444<https://fred.stlouisfed.org/>.

#### 5.1.3 Beige Book:

The Beige Book compiles economic conditions of the jurisdictions of each regional Federal Reserve Bank, and is published two weeks prior to the FOMC meetings.
Its topics span a wide range, including GDP, inflation, employment, manufacturing, agriculture, tourism, real estate, and more. Given its role as material for debate at FOMC meetings, the Beige Book also serves as one of the resources for speculating on the outcomes of the next FOMC meeting[[11](https://arxiv.org/html/2511.02469v1#bib.bib11)].

In our research, we work with the Beige Book corpus created by [[33](https://arxiv.org/html/2511.02469v1#bib.bib33)].
This dataset is structured to be user-friendly for a range of analytical purposes, reflecting insights from existing studies.
Its design promotes widespread use, allowing for consistent comparisons in various experiments.
Each sentence in this dataset is assigned a topic, and we use ’overall economic activity’ or ’summary’ topic sentences.

### 5.2 Experimental Settings

Given the FOMC’s eight meetings per year, our study’s experimental period encompasses approximately 200 distinct time slices.
We randomly select these slices such that 15 instances correspond to "Raise", 30 to "Hold", and 15 to "Lower" decisions.
However, periods with minimal policy rate changes (e.g., between 2009-2015) or consecutive rate hikes are considered too trivial as prediction tasks, so we exclude any slices where the true policy decision matches either the preceding or following decision.

We consider the task of predicting the FOMC’s policy rate decision (Raise, Hold, or Lower) at the time of the Beige Book release, with policy decisions to be made two weeks later.
The input prompt includes: Beige Book textual data, economic indicators from the past three months, and the last two policy rate decisions.

We set the number of agents nn to 7 to facilitate majority voting.
Each agent is assigned a specific belief profile, consisting of: one each of "Strong Hawkish", "Moderately Hawkish", "Moderately Dovish", "Strong Dovish", and three "Neutral" agents.
Detailed definitions of these beliefs are presented in Table [1](https://arxiv.org/html/2511.02469v1#S5.T1 "Table 1 ‣ 5.2 Experimental Settings ‣ 5 Experiment ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification").

Table 1: Belief Description

| Belief | Description |
| --- | --- |
| Strong Hawkish | Prioritizes controlling inflation and supports aggressive interest rate hikes |
| Moderately Hawkish | Proposes tightening of inflation but is mindful of economic downturns |
| Neutral | Makes careful decisions while monitoring the balance between prices and the economy |
| Moderately Dovish | Emphasizes supporting the economy while also paying a certain amount of attention to prices |
| Strong Dovish | Prioritizes economic recovery and actively supports interest rate cuts |

For our LLM implementation, we will use GPT-4o-mini555gpt-4o-mini-2024-07-18, with API access provided by OpenAI666<https://openai.com/>.
The temperature hyperparameter, which controls the randomness in generation, is set to 1 to enable diverse debate patterns, while all other hyperparameters are configured to their default values.
To ensure consistent output format, we will employ Structured Outputs777<https://platform.openai.com/docs/guides/structured-outputs?api-mode=responses>. This configuration specifies that the output should include both a ’label’ and its supporting ’justification’.

The maximum number of rounds is set to 10 to allow sufficient debate time. However, debate will terminate immediately when all LLMs reach complete agreement on their outputs.

The actual prompt used is as follows:

Round t=0t=0
  
 


Today is {Month}.
  
You will be given beige book text data, associated macroeconomic numerical data, historical policy rate, and a prior belief of central bank policy.
  
Based on these inputs, predict whether the central bank will Raise, Hold, or Lower the policy rate after two weeks. You should provide a brief justification for your answer, and you must output one of the three labels: Raise, Hold, or Lower.
  
Please also note that policy rate changes should be implemented with appropriate speed, and that taking Hold is not necessarily always the best approach.
  
Belief: {Beliefk\mathrm{Belief}\_{k}}
  
Beige Book Text Data: {Text}
  
Macroeconomic Numerical Data: {Indicators}
  
Historical Policy Rate: {Rates}

Round t>0t>0
  
 


Today is {Month}.
  
Several other models have already given their predictions and current beliefs:
  
Model1\mathrm{Model}\_{1}: Label is {Prediction1(t−1)\mathrm{Prediction}\_{1}^{(t-1)}}. {Justification1(t−1)\mathrm{Justification}\_{1}^{(t-1)}} ({Belief1\mathrm{Belief}\_{1}})
  
Model2\mathrm{Model}\_{2}: Label is {Prediction2(t−1)\mathrm{Prediction}\_{2}^{(t-1)}}. {Justification2(t−1)\mathrm{Justification}\_{2}^{(t-1)}} ({Belief2\mathrm{Belief}\_{2}})
  
⋯\cdot\cdot\cdot
  
Modeln\mathrm{Model}\_{n}: Label is {Predictionn(t−1)\mathrm{Prediction}\_{n}^{(t-1)}}. {Justificationn(t−1)\mathrm{Justification}\_{n}^{(t-1)}} ({Beliefn\mathrm{Belief}\_{n}})
  
  
Now you should consider these responses and beliefs.
  
You are again given beige book text data, associated macroeconomic numerical data, historical policy rate, your current prediction, and your current belief.
  
Use all of these to predict whether the central bank will Raise, Hold, or Lower the policy rate after two weeks. You should provide a brief justification for your answer, and you must output one of the three labels: Raise, Hold, or Lower.
  
Please also note that policy rate changes should be implemented with appropriate speed, and that taking Hold is not necessarily always the best approach.
  
Belief: {Beliefk\mathrm{Belief}\_{k}}
  
Current Prediction: {Predictionk(t−1)\mathrm{Prediction}\_{k}^{(t-1)}}
  
Beige Book Text Data: {Text}
  
Macroeconomic Numerical Data: {Indicators}
  
Historical Policy Rate: {Rates}

Here, underline represents a variable containing information embedded in the prompt.
The correspondence with Equation [5](https://arxiv.org/html/2511.02469v1#S4.E5 "In 4 Proposed Method ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification") is as follows:

zi(t)=(Predictioni(t),Justificationi(t))z\_{i}^{(t)}=(\mathrm{Prediction}\_{i}^{(t)},\mathrm{Justification}\_{i}^{(t)}) :
:   Predicted Label and Its Justification

ϕi=Beliefi\phi\_{i}=\mathrm{Belief}\_{i} :
:   Belief

x=Textx=\mathrm{Text} :
:   Beige Book Text Data

v=Indicators,Ratesv=\mathrm{Indicators},\mathrm{Rates} :
:   Macroeconomic Numerical Data

The above experiments will be referred to as experiment (1) in the following.

### 5.3 Ablation Study

As part of our ablation study, we will investigate the impact of: (2) textual information, (3) macroeconomic indicators, and (4) the current policy rate level on prediction accuracy.
The prompt structure remains largely unchanged from Experiment (1), with only the following single sentence varying: ’You will be given beige book text data, associated macroeconomic numerical data, historical policy rate, and a prior belief of central bank policy.’ We will modify this information content to assess its influence.
For example, the prompt without textual information would appear as follows:

Round t=0t=0 (Remove Text)
  
 


Today is {Month}.
  
You will be given beige associated macroeconomic numerical data, historical policy rate, and a prior belief of central bank policy.
  
Based on these inputs, predict whether the central bank will Raise, Hold, or Lower the policy rate after two weeks. You should provide a brief justification for your answer, and you must output one of the three labels: Raise, Hold, or Lower.
  
Please also note that policy rate changes should be implemented with appropriate speed, and that taking Hold is not necessarily always the best approach.
  
Belief: {Beliefk\mathrm{Belief}\_{k}}
  
Macroeconomic Numerical Data: {Indicators}
  
Historical Policy Rate: {Rates}

Round t>0t>0 (Remove Text)
  
 


Today is {Month}.
  
Several other models have already given their predictions and current beliefs:
  
Model1\mathrm{Model}\_{1}: Label is {Prediction1(t−1)\mathrm{Prediction}\_{1}^{(t-1)}}. {Justification1(t−1)\mathrm{Justification}\_{1}^{(t-1)}} ({Belief1\mathrm{Belief}\_{1}})
  
Model2\mathrm{Model}\_{2}: Label is {Prediction2(t−1)\mathrm{Prediction}\_{2}^{(t-1)}}. {Justification2(t−1)\mathrm{Justification}\_{2}^{(t-1)}} ({Belief2\mathrm{Belief}\_{2}})
  
⋯\cdot\cdot\cdot
  
Modeln\mathrm{Model}\_{n}: Label is {Predictionn(t−1)\mathrm{Prediction}\_{n}^{(t-1)}}. {Justificationn(t−1)\mathrm{Justification}\_{n}^{(t-1)}} ({Beliefn\mathrm{Belief}\_{n}})
  
  
Now you should consider these responses and beliefs.
  
You are again given associated macroeconomic numerical data, historical policy rate, your current prediction, and your current belief.
  
Use all of these to predict whether the central bank will Raise, Hold, or Lower the policy rate after two weeks. You should provide a brief justification for your answer, and you must output one of the three labels: Raise, Hold, or Lower.
  
Please also note that policy rate changes should be implemented with appropriate speed, and that taking Hold is not necessarily always the best approach.
  
Belief: {Beliefk\mathrm{Belief}\_{k}}
  
Current Prediction: {Predictionk(t−1)\mathrm{Prediction}\_{k}^{(t-1)}}
  
Macroeconomic Numerical Data: {Indicators}
  
Historical Policy Rate: {Rates}

Furthermore, to examine the predictive capability of a simple approach without beliefs (5), we will investigate accuracy using the following prompt.
To maintain consistent conditions, we will perform seven predictions and determine policy decisions through majority voting.

Round t=0t=0 (Remove Belief)
  
 


Today is {Month}.
  
You will be given beige book text data, associated macroeconomic numerical data and historical policy rate.
  
Based on these inputs, predict whether the central bank will Raise, Hold, or Lower the policy rate after two weeks. You should provide a brief justification for your answer, and you must output one of the three labels: Raise, Hold, or Lower.
  
Please also note that policy rate changes should be implemented with appropriate speed, and that taking Hold is not necessarily always the best approach.
  
Beige Book Text Data: {Text}
  
Macroeconomic Numerical Data: {Indicators}
  
Historical Policy Rate: {Rates}

Finally, to demonstrate the utility of multi-round agent debate in reaching consensus, we define Experiment (6) as the majority vote result from round 0 of the main experiment (1).

### 5.4 Results & Discussion

We conducted experiments (1) through (6), calculating three evaluation metrics—Precision, Recall, and F1-Score using macro averaging. The results are presented in Table [2](https://arxiv.org/html/2511.02469v1#S5.T2 "Table 2 ‣ 5.4 Results & Discussion ‣ 5 Experiment ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification").

Table 2: All results (Precision, Recall, F1-Score)

| Experimental Settings | Precision | Recall | F1-Score |
| --- | --- | --- | --- |
| (1) Proposed Method | 0.549 | 0.467 | 0.476 |
| (2) Remove Beige Book | 0.399 | 0.422 | 0.385 |
| (4) Remove Historical Policy Rate | 0.535 | 0.456 | 0.464 |
| (5) Remove Belief | 0.514 | 0.411 | 0.399 |
| (6) No Debate | 0.543 | 0.422 | 0.415 |

Experimental results showed that (1) yielded the best performance.
The confusion matrix for (1) is presented in Table [3](https://arxiv.org/html/2511.02469v1#S5.T3 "Table 3 ‣ 5.4 Results & Discussion ‣ 5 Experiment ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification").

Table 3: Confusion Matrix

|  |  |  | Predicted |  |
| --- | --- | --- | --- | --- |
|  |  | Raise | Hold | Lower |
|  | Raise | 7 | 8 | 0 |
| Actual | Hold | 8 | 20 | 2 |
|  | Lower | 0 | 11 | 4 |

As shown in Table [3](https://arxiv.org/html/2511.02469v1#S5.T3 "Table 3 ‣ 5.4 Results & Discussion ‣ 5 Experiment ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification"), no significant directional errors were observed—for instance, raising rates when lowering was the actual decision or vice versa.
The information sources used in this research demonstrate that policy direction can be reasonably constrained.

Results from Experiment (2) indicate that Beige Book information proves valuable for policy rate determination.
The Beige Book contains descriptions of overall U.S. price and employment conditions, which align with the Fed’s Dual Mandate.
Furthermore, results from Experiment (3) confirm that both quantitative and textual macroeconomic indicators are crucial for policy rate decision-making.
However, the presence of recent policy rate trends (Experiment (4)) showed no significant impact on prediction accuracy.
This finding may be partially explained by our intentional selection of policy rate transition points.
When policy rate trends are present, it could potentially be useful for predicting rate changes, but excessive reliance on current trend biases may pose risks and requires caution.

Experiments (5) and (6) represent majority voting results without inter-agent debate.
These results demonstrate that the iterative decision-making approach—where each agent refines its judgment based on others’ opinions over multiple rounds—is an effective methodology.

Based on the empirical results from Experiments (1) and (6), we present in Table [4](https://arxiv.org/html/2511.02469v1#S5.T4 "Table 4 ‣ 5.4 Results & Discussion ‣ 5 Experiment ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification"): (1) aggregated policy decisions for each belief category after the final round, and (6) aggregated policy decisions for each belief category before any debate.

Table 4: Aggregate policy decisions by belief category

|  |  | (1)After debate |  |  | (6)Before debate |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Raise | Hold | Lower | Raise | Hold | Lower |
| Strong Hawkish | 30 | 29 | 1 | 33 | 22 | 5 |
| Moderately Hawkish | 28 | 32 | 0 | 27 | 27 | 6 |
| Neutral | 31 | 136 | 13 | 45 | 117 | 18 |
| Moderately Dovish | 3 | 53 | 4 | 15 | 36 | 9 |
| Strong Dovish | 4 | 46 | 10 | 15 | 32 | 13 |
| Total | 96 | 296 | 28 | 135 | 234 | 51 |

Furthermore, the aggregated policy decision counts for "Raise", "Hold", and "Lower" in Experiment (5) without belief information are 111, 280, and 29 respectively.
From Experiment (5) results, we observe that regardless of belief type, there is a consistent predictive bias toward "Hold", followed by "Raise" and then "Lower".
This bias persists even after incorporating belief information.
Comparing Experiment (5) with (6), we note that providing belief information somewhat mitigates the tendency toward "Hold" dominance, resulting in more diverse policy decision outcomes.
By allowing each agent to generate diverse opinions based on initial beliefs in Experiment (1) and then facilitating their mutual exchange, we achieve the optimal results shown in [2](https://arxiv.org/html/2511.02469v1#S5.T2 "Table 2 ‣ 5.4 Results & Discussion ‣ 5 Experiment ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification").
Figure [5](https://arxiv.org/html/2511.02469v1#S5.T5 "Table 5 ‣ 5.4 Results & Discussion ‣ 5 Experiment ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification") illustrates the policy decision changes resulting from the debate process.

Table 5: Transition Matrix

|  |  |  | (6)Before debate |  |
| --- | --- | --- | --- | --- |
|  |  | Raise | Hold | Lower |
|  | Raise | 80 | 55 | 0 |
| (1)After debate | Hold | 16 | 217 | 1 |
|  | Lower | 0 | 24 | 27 |

## 6 Conclusion

In this study, we proposed a structured modeling approach that simulates the FOMC’s collective decision-making process using multiple large language models.
Each agent integrates policy texts and macroeconomic indicators, updates its belief through debate, and makes a final prediction.
We also introduced a latent belief variable and theoretically showed that it mediates the relationship between input information and the agent’s decision, thereby enhancing the interpretability of agent behavior.
We evaluated the method on 60 meetings held between 2000 and 2025. The full model that includes both debate and beliefs reached an F1 score of 0.48, outperforming versions that remove the debate, the beliefs, the Beige Book, or the macroeconomic indicators. The ablation study showed that the Beige Book is especially important for accuracy, and that the debate rounds lessen the strong Hold bias seen when the agents do not interact.
Several limitations remain in this study: The belief space is small and discrete, the framework relies on a single language model family, and the experiments cover only the FOMC. For further study, we will test continuous belief spaces, introduce safeguards against hallucination, and apply the framework to other central bank policy committees such as the European Central Bank and the Bank of Japan.

## Appendix 0.A Proof of Lemma

### 0.A.1 Proof of Lemma [1](https://arxiv.org/html/2511.02469v1#Thmlemma1 "Lemma 1(Latent Beliefs Decomposition) ‣ 4.1 Latent Policy Beliefs ‣ 4 Proposed Method ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification")

###### Proof

Using the law of total probability, we can marginalize over the latent policy belief θ\theta to express the label generation probability at round t+1t+1 as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | PLLM​(zi(t+1)∣x,v,Z(t),ϕi)\displaystyle P\_{\mathrm{LLM}}\bigl(z\_{i}^{(t+1)}\mid x,\,v,\,Z^{(t)},\,\phi\_{i}\bigr) | =∑θ∈ΘP​(zi(t+1),θ∣x,v,Z(t),ϕi)\displaystyle=\sum\_{\theta\in\Theta}P\bigl(z\_{i}^{(t+1)},\,\theta\mid x,\,v,\,Z^{(t)},\,\phi\_{i}\bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑θ∈ΘP​(zi(t+1)∣θ,x,v,Z(t),ϕi)​P​(θ∣x,v,Z(t),ϕi).\displaystyle=\sum\_{\theta\in\Theta}P\bigl(z\_{i}^{(t+1)}\mid\theta,\,x,\,v,\,Z^{(t)},\,\phi\_{i}\bigr)\,P\bigl(\theta\mid x,\,v,\,Z^{(t)},\,\phi\_{i}\bigr). |  |

Here, P​(zi(t+1)∣θ,x,v,Z(t),ϕi)P(z\_{i}^{(t+1)}\mid\theta,\,x,\,v,\,Z^{(t)},\,\phi\_{i}) denotes the conditional probability that agent ii generates label zi(t+1)z\_{i}^{(t+1)} given a known latent belief θ\theta and observations xx, vv, and Z(t)Z^{(t)}.
The term P​(θ∣x,v,Z(t),ϕi)P(\theta\mid x,\,v,\,Z^{(t)},\,\phi\_{i}) represents the posterior distribution over stances after observing xx, vv, and Z(t)Z^{(t)}. This completes the proof of Lemma [1](https://arxiv.org/html/2511.02469v1#Thmlemma1 "Lemma 1(Latent Beliefs Decomposition) ‣ 4.1 Latent Policy Beliefs ‣ 4 Proposed Method ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification").

### 0.A.2 Proof of Lemma [2](https://arxiv.org/html/2511.02469v1#Thmlemma2 "Lemma 2(Posterior Decomposition) ‣ 4.1 Latent Policy Beliefs ‣ 4 Proposed Method ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification")

###### Proof

According to Assumption [11](https://arxiv.org/html/2511.02469v1#S4.E11 "In Assumption 1 (Conditional Independence Given Latent Belief) ‣ 4.1 Latent Policy Beliefs ‣ 4 Proposed Method ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification"), we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(zi(t+1)∣θ,x,v,Z(t),ϕi)=P​(zi(t+1)∣θ,ϕi)(∀θ∈Θ,t≥0).\displaystyle P\bigl(z\_{i}^{(t+1)}\mid\theta,\,x,\,v,\,Z^{(t)},\,\phi\_{i}\bigr)=P\bigl(z\_{i}^{(t+1)}\mid\theta,\,\phi\_{i}\bigr)\quad(\forall\,\theta\in\Theta,\;t\geq 0). |  | (14) |

Substituting this into the decomposition from Lemma [1](https://arxiv.org/html/2511.02469v1#Thmlemma1 "Lemma 1(Latent Beliefs Decomposition) ‣ 4.1 Latent Policy Beliefs ‣ 4 Proposed Method ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification"), we obtain:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | PLLM​(zi(t+1)∣x,v,Z(t),ϕi)\displaystyle P\_{\mathrm{LLM}}\bigl(z\_{i}^{(t+1)}\mid x,\,v,\,Z^{(t)},\,\phi\_{i}\bigr) | =∑θ∈ΘP​(zi(t+1)∣θ,ϕi)​P​(θ∣x,v,Z(t),ϕi),\displaystyle=\sum\_{\theta\in\Theta}P\bigl(z\_{i}^{(t+1)}\mid\theta,\,\phi\_{i}\bigr)\,P\bigl(\theta\mid x,\,v,\,Z^{(t)},\,\phi\_{i}\bigr), |  | (15) |

which corresponds to the first part of Lemma [2](https://arxiv.org/html/2511.02469v1#Thmlemma2 "Lemma 2(Posterior Decomposition) ‣ 4.1 Latent Policy Beliefs ‣ 4 Proposed Method ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification").

Next, we derive the posterior distribution P​(θ∣x,v,Z(t),ϕi)P\bigl(\theta\mid x,\,v,\,Z^{(t)},\,\phi\_{i}\bigr) using Bayes’ theorem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(θ∣x,v,Z(t),ϕi)=P​(x,v,Z(t)∣θ,ϕi)​P​(θ∣ϕi)P​(x,v,Z(t)∣ϕi).P\bigl(\theta\mid x,\,v,\,Z^{(t)},\,\phi\_{i}\bigr)=\frac{P\bigl(x,\,v,\,Z^{(t)}\mid\theta,\,\phi\_{i}\bigr)\,P\bigl(\theta\mid\phi\_{i}\bigr)}{P\bigl(x,\,v,\,Z^{(t)}\mid\phi\_{i}\bigr)}. |  | (16) |

Since the denominator P​(x,v,Z(t)∣ϕi)P(x,\,v,\,Z^{(t)}\mid\phi\_{i}) does not depend on θ\theta, we consider the proportional relationship instead.

We now assume conditional independence of the text xx, numerical data vv, and previous responses Z(t)Z^{(t)} given the stance θ\theta:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(x,v,Z(t)∣θ,ϕi)=P​(x,v∣θ,ϕi)​P​(Z(t)∣θ,ϕi).P\bigl(x,\,v,\,Z^{(t)}\mid\theta,\,\phi\_{i}\bigr)=P\bigl(x,\,v\mid\theta,\,\phi\_{i}\bigr)\,P\bigl(Z^{(t)}\mid\theta,\,\phi\_{i}\bigr). |  | (17) |

Substituting this into the numerator of Equation ([16](https://arxiv.org/html/2511.02469v1#Pt0.A1.E16 "In Proof ‣ 0.A.2 Proof of Lemma 2 ‣ Appendix 0.A Proof of Lemma ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification")), we get:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(x,v∣θ,ϕi)​P​(Z(t)∣θ,ϕi)​P​(θ∣ϕi).\displaystyle P\bigl(x,\,v\mid\theta,\,\phi\_{i}\bigr)\,P\bigl(Z^{(t)}\mid\theta,\,\phi\_{i}\bigr)\,P\bigl(\theta\mid\phi\_{i}\bigr). |  | (18) |

Furthermore, we assume that each element zj(t)z\_{j}^{(t)} in Z(t)={zj(t)}j=1nZ^{(t)}=\{z\_{j}^{(t)}\}\_{j=1}^{n} is conditionally independent given the same belief θ\theta:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(Z(t)∣θ,ϕi)=∏j=1nP​(zj(t)∣θ,ϕi).P\bigl(Z^{(t)}\mid\theta,\,\phi\_{i}\bigr)=\prod\_{j=1}^{n}P\bigl(z\_{j}^{(t)}\mid\theta,\,\phi\_{i}\bigr). |  | (19) |

Substituting into Equation ([16](https://arxiv.org/html/2511.02469v1#Pt0.A1.E16 "In Proof ‣ 0.A.2 Proof of Lemma 2 ‣ Appendix 0.A Proof of Lemma ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification")), we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(θ∣x,v,Z(t),ϕi)\displaystyle P\bigl(\theta\mid x,\,v,\,Z^{(t)},\,\phi\_{i}\bigr) | ∝P​(x,v,Z(t)∣θ,ϕi)​P​(θ∣ϕi)\displaystyle\propto P\bigl(x,\,v,\,Z^{(t)}\mid\theta,\,\phi\_{i}\bigr)\,P\bigl(\theta\mid\phi\_{i}\bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =[P​(x,v∣θ,ϕi)​P​(Z(t)∣θ,ϕi)]​P​(θ∣ϕi)\displaystyle=\left[P\bigl(x,\,v\mid\theta,\,\phi\_{i}\bigr)\,P\bigl(Z^{(t)}\mid\theta,\,\phi\_{i}\bigr)\right]\,P\bigl(\theta\mid\phi\_{i}\bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =P​(x,v∣θ,ϕi)​P​(θ∣ϕi)​∏j=1nP​(zj(t)∣θ,ϕi).\displaystyle=P\bigl(x,\,v\mid\theta,\,\phi\_{i}\bigr)\,P\bigl(\theta\mid\phi\_{i}\bigr)\,\prod\_{j=1}^{n}P\bigl(z\_{j}^{(t)}\mid\theta,\,\phi\_{i}\bigr). |  |

This corresponds to the posterior decomposition in Equation ([13](https://arxiv.org/html/2511.02469v1#S4.E13 "In Lemma 2(Posterior Decomposition) ‣ 4.1 Latent Policy Beliefs ‣ 4 Proposed Method ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification")) of Lemma [2](https://arxiv.org/html/2511.02469v1#Thmlemma2 "Lemma 2(Posterior Decomposition) ‣ 4.1 Latent Policy Beliefs ‣ 4 Proposed Method ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification").

Therefore, under Assumption [11](https://arxiv.org/html/2511.02469v1#S4.E11 "In Assumption 1 (Conditional Independence Given Latent Belief) ‣ 4.1 Latent Policy Beliefs ‣ 4 Proposed Method ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification"), both Lemma [1](https://arxiv.org/html/2511.02469v1#Thmlemma1 "Lemma 1(Latent Beliefs Decomposition) ‣ 4.1 Latent Policy Beliefs ‣ 4 Proposed Method ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification") and Lemma [2](https://arxiv.org/html/2511.02469v1#Thmlemma2 "Lemma 2(Posterior Decomposition) ‣ 4.1 Latent Policy Beliefs ‣ 4 Proposed Method ‣ Modeling Hawkish-Dovish Latent Beliefs in Multi-Agent Debate-Based LLMs for Monetary Policy Decision Classification") hold.

## References

* [1]

  Axelrod, R.: The dissemination of culture: A model with local convergence and global polarization. Journal of conflict resolution 41(2), 203–226 (1997)
* [2]

  Balsategui, I., Gorjón, S., Marqués, J.M.: Artificial intelligence in the financial system: implications and progress from a central bank perspective. Financial Stability Review (Autumn) (2024)
* [3]

  Brandão-Marques, M.L., Meeks, M.R., Nguyen, V.: Monetary Policy with Uncertain Inflation Persistence. International Monetary Fund (2024)
* [4]

  Bruno, V., Shin, H.S.: Capital flows and the risk-taking channel of monetary policy. Journal of monetary economics 71, 119–132 (2015)
* [5]

  Chan, C.M., Chen, W., Su, Y., Yu, J., Xue, W., Zhang, S., Fu, J., Liu, Z.: Chateval: Towards better LLM-based evaluators through multi-agent debate. In: The Twelfth International Conference on Learning Representations (2024)
* [6]

  Couture, C.: Financial market effects of fomc projections. Journal of Macroeconomics 67, 103279 (2021)
* [7]

  Devlin, J., Chang, M.W., Lee, K., Toutanova, K.: BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. In: Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics. pp. 4171–4186. Association for Computational Linguistics (2019)
* [8]

  Du, Y., Li, S., Torralba, A., Tenenbaum, J.B., Mordatch, I.: Improving factuality and reasoning in language models through multiagent debate. In: Forty-first International Conference on Machine Learning (2023)
* [9]

  Estornell, A., Liu, Y.: Multi-llm debate: Framework, principals, and interventions. Advances in Neural Information Processing Systems 37, 28938–28964 (2024)
* [10]

  Fanta, N., Horvath, R.: Artificial intelligence and central bank communication: the case of the ecb. Applied Economics Letters pp. 1–8 (2024)
* [11]

  Fujiwara, M., Suimon, Y., Nakagawa, K.: Treasury yield spread prediction with sentiments of beige book and macroeconomic data. In: 2023 14th IIAI International Congress on Advanced Applied Informatics (IIAI-AAI). pp. 337–342. IEEE (2023)
* [12]

  Fulton, C., Hubrich, K.: Forecasting us inflation in real time. Econometrics 9(4),  36 (2021)
* [13]

  Gatto, J., Basak, M., Srivastava, Y., Bohlman, P., Preum, S.M.: Scope of large language models for mining emerging opinions in online health discourse. arXiv (2024), <https://arxiv.org/abs/2403.03336>
* [14]

  Hansen, S., McMahon, M., Prat, A.: Transparency and deliberation within the fomc: A computational linguistics approach. The Quarterly Journal of Economics 133(2), 801–870 (2018)
* [15]

  Jarociński, M., Karadi, P.: The macroeconomic impact of news about policy and news about the economy in ecb announcements. Research Bulletin 50 (2018)
* [16]

  Kim, S.: International transmission of us monetary policy shocks: Evidence from var’s. Journal of monetary Economics 48(2), 339–372 (2001)
* [17]

  Larochelle, H., Ranzato, M., Hadsell, R., Balcan, M., Lin, H. (eds.): Language Models are Few-Shot Learners, vol. 33. Curran Associates, Inc. (2020)
* [18]

  Liang, T., He, Z., Jiao, W., Wang, X., Wang, Y., Wang, R., Yang, Y., Shi, S., Tu, Z.: Encouraging divergent thinking in large language models through multi-agent debate. In: Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing. pp. 17889–17904 (2024)
* [19]

  López-Moctezuma, G.: Sequential deliberation in collective decision-making: The case of the fomc (2016)
* [20]

  Lux, T., Marchesi, M.: Scaling and Criticality in a Stochastic Multi-agent Model of a Financial Market. Nature 397(6719), 498–500 (1999)
* [21]

  Nakagawa, K., Suimon, Y.: Inflation rate tracking portfolio optimization method: Evidence from japan. Finance Research Letters 49, 103130 (2022)
* [22]

  Nakamura, E., Steinsson, J.: High-frequency identification of monetary non-neutrality: the information effect. The Quarterly Journal of Economics 133(3), 1283–1330 (2018)
* [23]

  OpenAI: ChatGPT (2023), https://openai.com/blog/chatgpt/
* [24]

  OpenAI: GPT-4 Technical Report (2023), <https://arxiv.org/abs/2303.08774>
* [25]

  Park, J.S., O’Brien, J., Cai, C.J., Morris, M.R., Liang, P., Bernstein, M.S.: Generative agents: Interactive simulacra of human behavior. In: Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology. UIST ’23, Association for Computing Machinery, New York, NY, USA (2023)
* [26]

  Qu, Y., Wang, J.: Performance and biases of large language models in public opinion simulation. Humanities and Social Sciences Communications 11(1), 1–13 (2024)
* [27]

  Radford, A., Narasimhan, K., Salimans, T., Sutskever, I.: Improving Language Understanding by Generative Pre-Training (2018), https://cdn.openai.com/research-covers/language-unsupervised/language\_understanding\_paper.pdf
* [28]

  Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., Sutskever, I.: Language Models are Unsupervised Multitask Learners (2019), https://cdn.openai.com/better-language-models/language\_models\_are\_unsupervised\_multitask\_learners.pdf
* [29]

  Romer, C.D., Romer, D.H.: Federal reserve information and the behavior of interest rates. American economic review 90(3), 429–457 (2000)
* [30]

  Routledge, B.R.: Machine learning and asset allocation. Financial Management 48(4), 1069–1094 (2019)
* [31]

  Schelling, T.C.: Models of Segregation. The American Economic Review 59(2), 488–493 (1969)
* [32]

  Schonhardt-Bailey, C.: Deliberating American monetary policy: A textual analysis. MIT press (2013)
* [33]

  Takano, K., Hasegawa, N., Naito, A., Nakagawa, K.: Construction of the frb beige book corpus and analysis (japanese). Proceedings of The 37th Annual Conference of the Japanese Society for Artificial Intelligence pp. 3Xin4–33 (2023)
* [34]

  Takata, R., Masumori, A., Ikegami, T.: Spontaneous emergence of agent individuality through social interactions in large language model-based communities. Entropy 26(12),  1092 (2024)
* [35]

  Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, L.u., Polosukhin, I.: Attention is all you need. In: Advances in Neural Information Processing Systems. vol. 30. Curran Associates, Inc.
* [36]

  Yu, H., Hong, Z., Cheng, Z., Zhu, K., Xuan, K., Yao, J., Feng, T., You, J.: Researchtown: Simulator of human research community. arXiv (2024)