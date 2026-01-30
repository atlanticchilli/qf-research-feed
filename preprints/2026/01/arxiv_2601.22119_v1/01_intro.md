---
authors:
- Han Yang
- Dong Hao
- Zhuohan Wang
- Qi Shi
- Xingtong Li
doc_id: arxiv:2601.22119v1
family_id: arxiv:2601.22119
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Alpha Discovery via Grammar-Guided Learning and Search
url_abs: http://arxiv.org/abs/2601.22119v1
url_html: https://arxiv.org/html/2601.22119v1
venue: arXiv q-fin
version: 1
year: 2026
---


Han Yang
  
Dong Hao
  
Zhuohan Wang
  
Qi Shi
  
Xingtong Li

###### Abstract

Automatically discovering formulaic alpha factors is a central problem in quantitative finance. Existing methods often ignore syntactic and semantic constraints, relying on exhaustive search over unstructured and unbounded spaces. We present AlphaCFG, a grammar-based framework for defining and discovering alpha factors that are syntactically valid, financially interpretable, and computationally efficient. AlphaCFG uses an alpha-oriented context-free grammar to define a tree-structured, size-controlled search space, and formulates alpha discovery as a tree-structured linguistic Markov decision process, which is then solved using a grammar-aware Monte Carlo Tree Search guided by syntax-sensitive value and policy networks. Experiments on Chinese and U.S. stock market datasets show that AlphaCFG outperforms state-of-the-art baselines in both search efficiency and trading profitability. Beyond trading strategies, AlphaCFG serves as a general framework for symbolic factor discovery and refinement across quantitative finance, including asset pricing and portfolio construction.

Machine Learning, ICML

## 1 Introduction

### 1.1 Alpha discovery

In quantitative finance, alpha factors play a central role in asset management, quantitative trading, and investment decision-making. An alpha factor is an explicit function that maps historical market features, such as prices and volumes, to predictions of future returns. Alpha discovery refers to the systematic identification of such predictive functions from historical data and remains a core challenge due to the vast and complex space of possible functional forms. Beyond their practical importance, alpha discovery poses a fundamental machine-learning challenge: identifying symbolic functions that are both predictive and interpretable under severe combinatorial constraints.

Existing approaches to alpha discovery can be broadly classified into three categories. Heuristic or expert-driven methods rely on financial intuition, such as value factors (e.g., price-to-earnings ratios (Fama and French, [1992](https://arxiv.org/html/2601.22119v1#bib.bib15 "The cross-section of expected stock returns"))) and momentum factors (e.g., past 12-month returns (Carhart, [1997](https://arxiv.org/html/2601.22119v1#bib.bib14 "On persistence in mutual fund performance"))), but lack scalability and are quickly arbitraged once widely adopted, reducing predictive accuracy over time. Data-driven learning methods, including regression (Bhandari et al., [2022](https://arxiv.org/html/2601.22119v1#bib.bib43 "Predicting stock market index using lstm"); Qin et al., [2017](https://arxiv.org/html/2601.22119v1#bib.bib44 "A dual-stage attention-based recurrent neural network for time series prediction"); Dai et al., [2022](https://arxiv.org/html/2601.22119v1#bib.bib45 "Price change prediction of ultra high frequency financial data based on temporal convolutional network"); Mozaffari and Zhang, [2024](https://arxiv.org/html/2601.22119v1#bib.bib46 "Predictive modeling of stock prices using transformer model")), tree-based ensembles (Wang et al., [2023](https://arxiv.org/html/2601.22119v1#bib.bib42 "An xgboost-based multivariate deep learning framework for stock index futures price forecasting"); Bisdoulis, [2024](https://arxiv.org/html/2601.22119v1#bib.bib41 "Assets forecasting with feature engineering and transformation methods for lightgbm")), unsupervised learning (Xu, [2025](https://arxiv.org/html/2601.22119v1#bib.bib47 "Unsupervised temporal encoding for stock price prediction through dual-phase learning")), and reinforcement learning (Lee, [2001](https://arxiv.org/html/2601.22119v1#bib.bib35 "Stock price prediction using reinforcement learning")), can capture complex nonlinear patterns, yet often suffer from limited interpretability and overfitting due to their black-box nature. Formulaic alpha methods (Zhang et al., [2020](https://arxiv.org/html/2601.22119v1#bib.bib3 "Autoalpha: an efficient hierarchical evolutionary algorithm for mining alpha factors in quantitative investment")) emphasize human-readable mathematical expressions composed of predefined operators, offering transparency and interpretability, and have therefore regained recent attention.

Table 1: Comparison of Alpha Discovery Methods

| Category | Pros | Cons |
| --- | --- | --- |
| Heuristic / Expert | Intuitive, easy to use | Limited, quickly arbitraged |
| Data-driven Learning | Captures complex patterns | Black-box, less interpretable |
| Formulaic Alpha | Interpretable, transparent | Computationally expensive |

Our work lies at the intersection of data-driven learning and formulaic alpha methods, aiming at the automatic discovery of explainable alpha factors. This problem can be viewed as symbolic regression (Makke and Chawla, [2024](https://arxiv.org/html/2601.22119v1#bib.bib17 "Interpretable scientific discovery with symbolic regression: a review")), which seeks explicit mathematical expressions that fit data while remaining interpretable, but is difficult due to its combinatorial search space and semantic equivalence among expressions. Early approaches such as genetic programming (GP) (Zhang et al., [2020](https://arxiv.org/html/2601.22119v1#bib.bib3 "Autoalpha: an efficient hierarchical evolutionary algorithm for mining alpha factors in quantitative investment")) evolve expression trees to optimize information coefficients. More recent methods, including AlphaGen (Yu et al., [2023](https://arxiv.org/html/2601.22119v1#bib.bib30 "Generating synergistic formulaic alpha collections via reinforcement learning")) and AlphaQCM (Zhu and Zhu, [2025](https://arxiv.org/html/2601.22119v1#bib.bib29 "AlphaQCM: alpha discovery in finance with distributional reinforcement learning")), adopt reinforcement learning to improve scalability.
Existing methods face the following fundamental challenges.

(1) Lack of linguistic characterization leads to inefficient search in an unbounded space.
Automated discovery of formulaic alphas is fundamentally a problem of searching over mathematical languages, yet existing methods lack an explicit linguistic framework to organize and constrain this search. In the absence of formal grammatical structure, current approaches must explore vast, and often effectively infinite, combinatorial spaces of expressions, relying on ad hoc syntactic checks to ensure validity. This unstructured exploration severely limits sample efficiency, degrades model performance, and incurs substantial computational cost.

(2) Semantic redundancy causes systematic waste in learning and search.
Many syntactically distinct mathematical sequences correspond to the same underlying semantics, but existing methods mostly encode expressions as linear sequences and treat the variants as independent. As a result, semantically equivalent expressions are repeatedly explored and evaluated, leading to significant redundancy in representation learning and search, and greatly reducing efficiency.

### 1.2 Our Work

We propose AlphaCFG,111Our source code is available at <https://github.com/HanYang544/AlphaCFG> a general linguistic–learning framework for the automatic discovery of interpretable alpha factors. The central idea is to treat alpha discovery as a structured language generation and learning problem, rather than an unstructured search over mathematical expressions. By combining formal grammar with learning and search, AlphaCFG provides a principled way to generate, validate, and optimize human-readable alpha factors. In this way, grammar serves as an explicit inductive bias that shapes both the search space and the learning dynamics.

(1) Grammar-Constrained Alpha Factors.
From a language-theoretic perspective, we first formalize the space of alpha factors as a structured mathematical language.
We propose two formal languages, α\alpha-Syn and α\alpha-Sem, that integrate context-free grammar (CFG) with finance domain–specific knowledge of alpha factors. α\alpha-Syn enforces grammatical correctness, while α\alpha-Sem further ensures financial semantic validity. These languages generate alpha expressions recursively in a tree-structured form, making tree-structure–based learning and optimization possible. To control complexity and reduce redundancy, we further enforce (i) length constraints to bound the search space, and (ii) expression-tree pruning to remove syntactically distinct but semantically equivalent factors.

(2) Structure Characterization of Alpha Space.
Building on this grammar-based language, we cast alpha discovery as a large Tree-Structured Linguistic Markov Decision Process (TSL-MDP), where each state is a partial expression, terminal states represent complete alpha factors, and rewards are given by the information coefficient (IC) on real market data. This formulation transforms alpha discovery from unstructured trial-and-error into a principled sequential decision process over the space of formulaic alpha factors.

(3) Reinforcing MCTS with Syntax-Aware Learning.
Finally, we design a learning and search algorithm that exploits the grammar-induced structure of the TSL-MDP. We employ a grammar-aware Monte Carlo Tree Search (MCTS), in which action selection is guided by a syntax-aware Upper Confidence Bound (UCB) rule. To generalize across the large state space, each partial expression tree is encoded using a Tree-LSTM, yielding structure-aware representations shared by a value network, which estimates expected performance from historical market data, and a policy network, which predicts promising alpha expansions. Through reinforced interaction between MCTS and these learned models, AlphaCFG progressively refines its search strategy and discovers high-quality alpha factors efficiently.

AlphaCFG is not limited to trading strategies and naturally extends to other quantitative finance tasks, by allowing flexible customization of operators, grammatical structures, and objective functions. We use trading as a representative testbed to demonstrate the effectiveness of AlphaCFG.
We evaluate AlphaCFG on CSI 300 and S&P 500 stocks, where it consistently outperforms strong baselines across multiple metrics, including returns, information coefficient (IC), Sharpe ratio, and maximum drawdown. Our results show that improved grammar design yields faster convergence and higher-quality factors. Moreover, AlphaCFG effectively refines existing factors and improves their predictive performance, highlighting its utility as a general tool for factor refinement and augmentation. Ablation studies further confirm the critical roles of grammar design and syntax-based representation learning in effective factor discovery.

## 2 Problem Formulation

Consider a market with nn stocks over TT trading days.
On each day t∈{1,2,…,T}t\in\{1,2,\dots,T\}, stock ii is associated with a feature matrix
𝐱t,i∈ℝm×τ′\mathbf{x}\_{t,i}\in\mathbb{R}^{m\times\tau^{\prime}}, which records mm raw market features
(e.g., opening and closing prices, volumes) over τ′\tau^{\prime} days.
We denote by
𝐗t=(𝐱t,1,𝐱t,2,…,𝐱t,n)\mathbf{X}\_{t}=(\mathbf{x}\_{t,1},\mathbf{x}\_{t,2},\dots,\mathbf{x}\_{t,n})
the collection of features for all stocks on day tt.

An *alpha factor* is a function
f:ℝm×τ′→ℝf:\mathbb{R}^{m\times\tau^{\prime}}\rightarrow\mathbb{R}
that maps the historical features of a single stock to a scalar score.
Applying ff cross-sectionally to all stocks on day tt yields a factor vector
𝐲t=(yt,1,…,yt,n)∈ℝn\mathbf{y}\_{t}=(y\_{t,1},\dots,y\_{t,n})\in\mathbb{R}^{n},
where yt,i=f​(𝐱t,i)y\_{t,i}=f(\mathbf{x}\_{t,i}) (illustrated in [Figure 6(a)](https://arxiv.org/html/2601.22119v1#A3.F6.sf1 "In Figure 6 ‣ Appendix C Supplement to Problem Formulation ‣ Alpha Discovery via Grammar-Guided Learning and Search")).
These scores are subsequently used to rank stocks or construct portfolios.

We focus on *formulaic* alpha factors, which are explicit mathematical expressions constructed from a predefined set of input features ([Table 4](https://arxiv.org/html/2601.22119v1#A1.T4 "In Appendix A Tables ‣ Alpha Discovery via Grammar-Guided Learning and Search")), constants ([Table 5](https://arxiv.org/html/2601.22119v1#A1.T5 "In Appendix A Tables ‣ Alpha Discovery via Grammar-Guided Learning and Search")), and operators ([Table 6](https://arxiv.org/html/2601.22119v1#A1.T6 "In Appendix A Tables ‣ Alpha Discovery via Grammar-Guided Learning and Search")).
These operators and operands are commonly used in quantitative finance (Yang et al., [2020](https://arxiv.org/html/2601.22119v1#bib.bib23 "Qlib: an ai-oriented quantitative investment platform")).
Representative examples are shown in [Figure 6(b)](https://arxiv.org/html/2601.22119v1#A3.F6.sf2 "In Figure 6 ‣ Appendix C Supplement to Problem Formulation ‣ Alpha Discovery via Grammar-Guided Learning and Search").

#### Evaluation via Information Coefficient.

The predictive quality of an alpha factor is evaluated using the *Information Coefficient* (IC), a standard metric in asset management (Grinold and Kahn, [2000](https://arxiv.org/html/2601.22119v1#bib.bib32 "Active portfolio management")).
For a given prediction horizon τ\tau, the realized τ\tau-day return of stock ii observed at day tt is

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt,i(τ)=Closet+τ,iCloset,i−1,r\_{t,i}^{(\tau)}=\frac{\mathrm{Close}\_{t+\tau,i}}{\mathrm{Close}\_{t,i}}-1, |  | (1) |

where Closet,i\mathrm{Close}\_{t,i} is the closing price of stock ii on day tt.
Let 𝐫t(τ)=(rt,1(τ),…,rt,n(τ))\mathbf{r}\_{t}^{(\tau)}=(r\_{t,1}^{(\tau)},\dots,r\_{t,n}^{(\tau)}) denote the cross-sectional return vector.
The daily IC at day tt is defined as the Pearson correlation between factor scores and subsequent returns:

|  |  |  |
| --- | --- | --- |
|  | ICt​(𝐲t,𝐫t(τ))=∑i=1n(yt,i−y¯t)​(rt,i(τ)−r¯t(τ))∑i=1n(yt,i−y¯t)2​∑i=1n(rt,i(τ)−r¯t(τ))2,\mathrm{IC}\_{t}(\mathbf{y}\_{t},\mathbf{r}\_{t}^{(\tau)})=\frac{\sum\_{i=1}^{n}(y\_{t,i}-\bar{y}\_{t})(r\_{t,i}^{(\tau)}-\overline{r}\_{t}^{(\tau)})}{\sqrt{\sum\_{i=1}^{n}(y\_{t,i}-\bar{y}\_{t})^{2}}\sqrt{\sum\_{i=1}^{n}(r\_{t,i}^{(\tau)}-\overline{r}\_{t}^{(\tau)})^{2}}}, |  |

where
y¯t=1n​∑i=1nyt,i\bar{y}\_{t}=\frac{1}{n}\sum\_{i=1}^{n}y\_{t,i} and
r¯t(τ)=1n​∑i=1nrt,i(τ)\overline{r}\_{t}^{(\tau)}=\frac{1}{n}\sum\_{i=1}^{n}r\_{t,i}^{(\tau)}.

To assess factor performance over the entire period, we use average daily IC of alpha factor ff:

|  |  |  |  |
| --- | --- | --- | --- |
|  | IC​(f)=1T​∑t=1TICt​(𝐲t,𝐫t(τ)).\mathrm{IC}(f)=\frac{1}{T}\sum\_{t=1}^{T}\mathrm{IC}\_{t}\bigl(\mathbf{y}\_{t},\mathbf{r}\_{t}^{(\tau)}\bigr). |  | (2) |

A higher IC​(f)\mathrm{IC}(f) indicates stronger predictive power.
Accordingly, the goal of *alpha discovery* is to identify formulaic factors that maximize IC​(f)\mathrm{IC}(f).

In practice, a common and effective strategy is to linearly combine multiple factors.
Following AlphaGen (Yu et al., [2023](https://arxiv.org/html/2601.22119v1#bib.bib30 "Generating synergistic formulaic alpha collections via reinforcement learning")), we optimize the IC of such linear combinations (referred to as a *factor pool*).
The detailed combination procedure is provided in [Algorithm 1](https://arxiv.org/html/2601.22119v1#alg1 "In B.1 Linear combination alpha factor algorithm ‣ Appendix B Algorithms ‣ Alpha Discovery via Grammar-Guided Learning and Search") in Appendix [B.1](https://arxiv.org/html/2601.22119v1#A2.SS1 "B.1 Linear combination alpha factor algorithm ‣ Appendix B Algorithms ‣ Alpha Discovery via Grammar-Guided Learning and Search").

## 3 Design Language of Interpretable Alphas

The space of formulaic alpha factors grows combinatorially with expression length, rendering brute-force search inefficient.
Moreover, a large fraction of candidate expressions are either *syntactically invalid* (i.e., ill-formed operator compositions) or *semantically nonsensical* (i.e., violating financial or temporal constraints), which severely hampers both efficiency and interpretability.

From a machine learning perspective, automated alpha discovery is therefore not merely an optimization problem, but fundamentally a *language design problem*: one must define a hypothesis space that is expressive enough to capture meaningful financial signals, while being sufficiently structured to admit efficient search and learning.
In the absence of such structure, existing methods are forced to explore an effectively unbounded symbolic space, leading to severe combinatorial explosion and redundant evaluations.

To address these challenges, we introduce a formal *linguistic characterization* of alpha factors based on Context-Free Grammar (CFG) (Chomsky and Schützenberger, [1959](https://arxiv.org/html/2601.22119v1#bib.bib1 "The algebraic theory of context-free languages"); Hopcroft and Ullman, [1979](https://arxiv.org/html/2601.22119v1#bib.bib22 "Automata theory, languages, and computation")).
By explicitly specifying the syntactic rules that govern valid alpha expressions, we restrict the search space to well-formed expressions, enforce operator-operand consistency, and enable tree-based search and learning.
This linguistic view allows us to systematically decompose the alpha search space into nested levels of validity, as illustrated in [Figure 1](https://arxiv.org/html/2601.22119v1#S3.F1 "In 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search").

Σ∗\Sigma^{\*}ℒs​y​n\mathcal{L}\_{syn}ℒs​e​m\mathcal{L}\_{sem}ℒsem≤k\mathcal{L}\_{\mathrm{sem}}^{\leq k}


Figure 1: 
Nested spaces of alpha expressions:
Σ∗\Sigma^{\*} (all symbol sequences),
ℒsyn\mathcal{L}\_{\mathrm{syn}} (syntactically valid),
ℒsem\mathcal{L}\_{\mathrm{sem}} (semantically valid),
and ℒsem≤K\mathcal{L}\_{\mathrm{sem}}^{\leq K} (length-bounded semantic alphas).

### 3.1 Syntactically-Valid Alpha Language

We begin by defining a grammar that ensures *syntactic validity*, which serves as the foundation for the following sections of semantic constraints and learning algorithms.

Syntactic validity requires that every generated alpha expression be a well-formed and evaluable symbolic program.
It entails two conditions:
(i) a well-defined hierarchical structure enforced by prefix notation and recursive nonterminal expansion; and
(ii) strictly follow operator arity, so that each operator receives the correct number of operands.
These are captured by the following generation rule:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤𝗑𝗉𝗋→𝖮𝗉​(𝖤𝗑𝗉𝗋,…)∣𝖳𝖾𝗋𝗆𝖲𝗒𝖻,\mathsf{Expr}\;\to\;\mathsf{Op}(\mathsf{Expr},\dots)\;\mid\;\mathsf{TermSyb}, |  | (3) |

where 𝖤𝗑𝗉𝗋∈𝒩\mathsf{Expr}\in\mathcal{N} denotes a recursively expandable nonterminal symbol,
𝖮𝗉∈𝒯\mathsf{Op}\in\mathcal{T} denotes prefix-notation operators,
and 𝖳𝖾𝗋𝗆𝖲𝗒𝖻∈𝒯\mathsf{TermSyb}\in\mathcal{T} denotes terminal symbols which are features and constants.

#### Structural Well-Formedness.

Formula ([3](https://arxiv.org/html/2601.22119v1#S3.E3 "Equation 3 ‣ 3.1 Syntactically-Valid Alpha Language ‣ 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search")) enforces a prefix-notation structure in which each operator 𝖮𝗉\mathsf{Op} precedes its operands, eliminating ambiguity in operator precedence and evaluation order.
Recursive expansion of 𝖤𝗑𝗉𝗋\mathsf{Expr} enables the construction of complex expressions, while termination is ensured by substituting terminal symbols.
Therefore, each valid derivation admits a unique hierarchical representation which we call *Abstract Syntax Representation (ASR)*. 222In formal language (Hopcroft and Ullman, [1979](https://arxiv.org/html/2601.22119v1#bib.bib22 "Automata theory, languages, and computation")), an expression corresponds to an abstract syntax tree (AST); we use the term ASR to distinguish it from the large search tree introduced later.

###### Definition 1.

An Abstract Syntax Representation (ASR) is a rooted, ordered tree encoding a single alpha expression, whose internal nodes are operators with arity-matched children and whose leaves are features, constants, or (in partial derivations) nonterminal symbols.

#### Operator Arity Constraints.

Syntactic validity also requires that all operators be applied with the correct number of operands.
We instantiate 𝖮𝗉\mathsf{Op} using operator families with fixed arity, reflecting common primitives in quantitative finance.
These include unary operators (𝖴𝗇𝖺𝗋𝗒𝖮𝗉\mathsf{UnaryOp}), binary operators (𝖡𝗂𝗇𝖺𝗋𝗒𝖮𝗉\mathsf{BinaryOp}),
rolling operators (𝖱𝗈𝗅𝗅𝗂𝗇𝗀𝖮𝗉\mathsf{RollingOp}),
paired rolling operators (𝖯𝖺𝗂𝗋𝖾𝖽𝖱𝗈𝗅𝗅𝗂𝗇𝗀𝖮𝗉\mathsf{PairedRollingOp}),
and nullary terminal symbols (𝖳𝖾𝗋𝗆𝖲𝗒𝖻\mathsf{TermSyb}) representing constants and raw features.
The resulting production rules are given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤𝗑𝗉𝗋→𝖴𝗇𝖺𝗋𝗒𝖮𝗉​(𝖤𝗑𝗉𝗋)∣𝖡𝗂𝗇𝖺𝗋𝗒𝖮𝗉​(𝖤𝗑𝗉𝗋,𝖤𝗑𝗉𝗋)∣𝖱𝗈𝗅𝗅𝗂𝗇𝗀𝖮𝗉(𝖤𝗑𝗉𝗋,𝖤𝗑𝗉𝗋)∣𝖯𝖺𝗂𝗋𝖾𝖽𝖱𝗈𝗅𝗅𝗂𝗇𝗀𝖮𝗉(𝖤𝗑𝗉𝗋,𝖤𝗑𝗉𝗋,𝖤𝗑𝗉𝗋)∣𝖳𝖾𝗋𝗆𝖲𝗒𝖻.\begin{aligned} \mathsf{Expr}\;\to\;&\mathsf{UnaryOp}(\mathsf{Expr})\;\mid\;\mathsf{BinaryOp}(\mathsf{Expr},\mathsf{Expr})\\ &\mid\;\mathsf{RollingOp}(\mathsf{Expr},\mathsf{Expr})\\ &\mid\;\mathsf{PairedRollingOp}(\mathsf{Expr},\mathsf{Expr},\mathsf{Expr})\\ &\mid\;\mathsf{TermSyb}.\end{aligned} |  | (4) |

All feature symbols and constants are listed in [Table 4](https://arxiv.org/html/2601.22119v1#A1.T4 "In Appendix A Tables ‣ Alpha Discovery via Grammar-Guided Learning and Search") and [Table 5](https://arxiv.org/html/2601.22119v1#A1.T5 "In Appendix A Tables ‣ Alpha Discovery via Grammar-Guided Learning and Search"), respectively,
while [Table 6](https://arxiv.org/html/2601.22119v1#A1.T6 "In Appendix A Tables ‣ Alpha Discovery via Grammar-Guided Learning and Search") lists all operators together with their arity categories.
These rules fully specify the admissible syntactic forms of alpha expressions.

We now formally define the context-free grammar that characterizes syntactically valid alpha expressions.

###### Definition 2 (α\alpha-Syn).

The context-free grammar for a syntactically valid alpha language α\alpha-Syn is defined as G=(𝒩,𝒯,𝒫,𝒮)G=(\mathcal{N},\mathcal{T},\mathcal{P},\mathcal{S}) where
𝒩\mathcal{N} is the recursively expandable nonterminal symbols,
𝒯\mathcal{T} is the terminal symbols including stock features ([Table 4](https://arxiv.org/html/2601.22119v1#A1.T4 "In Appendix A Tables ‣ Alpha Discovery via Grammar-Guided Learning and Search")),
numerical constants ([Table 5](https://arxiv.org/html/2601.22119v1#A1.T5 "In Appendix A Tables ‣ Alpha Discovery via Grammar-Guided Learning and Search")), and operators with fixed arity ([Table 6](https://arxiv.org/html/2601.22119v1#A1.T6 "In Appendix A Tables ‣ Alpha Discovery via Grammar-Guided Learning and Search")),
𝒫\mathcal{P} is the production rules given in Formula [4](https://arxiv.org/html/2601.22119v1#S3.E4 "Equation 4 ‣ Operator Arity Constraints. ‣ 3.1 Syntactically-Valid Alpha Language ‣ 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search"),
which enforce prefix-notation and strict operator-arity consistency, and 𝒮\mathcal{S} is the start symbol.

[Definition 2](https://arxiv.org/html/2601.22119v1#Thmdefinition2 "Definition 2 (𝛼-Syn). ‣ Operator Arity Constraints. ‣ 3.1 Syntactically-Valid Alpha Language ‣ 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search") generates the language ℒsyn\mathcal{L}\_{\mathrm{syn}} of syntactically valid alpha expressions, as illustrated in [Figure 1](https://arxiv.org/html/2601.22119v1#S3.F1 "In 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search").

### 3.2 Semantically-Interpretable Alpha Language

While α\alpha-Syn guarantees syntactic validity, it does not ensure semantic soundness in quantitative trading, as syntax alone cannot capture domain-specific financial constraints such as temporal coherence, numerical admissibility, or economically meaningful operator interactions.
Now we refine α\alpha-Syn in [Definition 2](https://arxiv.org/html/2601.22119v1#Thmdefinition2 "Definition 2 (𝛼-Syn). ‣ Operator Arity Constraints. ‣ 3.1 Syntactically-Valid Alpha Language ‣ 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search") by embedding domain-informed semantic constraints directly into the grammar, thereby defining a semantically interpretable alpha language.

#### Semantic Constraints.

We enforce a set of minimal and widely accepted financial semantic constraints:
(i) Rolling window constraint: the window-size operand of 𝖱𝗈𝗅𝗅𝗂𝗇𝗀𝖮𝗉\mathsf{RollingOp} and 𝖯𝖺𝗂𝗋𝖾𝖽𝖱𝗈𝗅𝗅𝗂𝗇𝗀𝖮𝗉\mathsf{PairedRollingOp} is integer constant;
(ii) Non-triviality: expressions cannot consist solely of constants and operators;
(iii) Numerical validity: operands must lie within domains consistent with their operators;
(iv) Time-series consistency: 𝖯𝖺𝗂𝗋𝖾𝖽𝖱𝗈𝗅𝗅𝗂𝗇𝗀𝖮𝗉\mathsf{PairedRollingOp} must operate on two time-varying features; constant operands are disallowed.

###### Definition 3 (α\alpha-Sem).

A semantic refinement of α\alpha-Syn is a context-free grammar
G=(𝒩′,𝒯′,𝒫′,𝒮)G=(\mathcal{N}^{\prime},\mathcal{T}^{\prime},\mathcal{P}^{\prime},\mathcal{S}) that shares the same start symbol 𝒮\mathcal{S} as α\alpha-Syn. The nonterminal symbols 𝒯′\mathcal{T}^{\prime} add Num and Constant.
The Terminal symbols 𝒯\mathcal{T} is refined to containing features in [Table 4](https://arxiv.org/html/2601.22119v1#A1.T4 "In Appendix A Tables ‣ Alpha Discovery via Grammar-Guided Learning and Search"), constant in [Table 5](https://arxiv.org/html/2601.22119v1#A1.T5 "In Appendix A Tables ‣ Alpha Discovery via Grammar-Guided Learning and Search") and operators in [Table 6](https://arxiv.org/html/2601.22119v1#A1.T6 "In Appendix A Tables ‣ Alpha Discovery via Grammar-Guided Learning and Search").
The production rules 𝒫′\mathcal{P}^{\prime} distinguishes the type of operands by:

|  |  |  |
| --- | --- | --- |
|  | 𝖤𝗑𝗉𝗋→𝖥𝖾𝖺𝗍𝗎𝗋𝖾∣𝖴𝗇𝖺𝗋𝗒𝖮𝗉​(𝖤𝗑𝗉𝗋)∣𝖡𝗂𝗇𝖺𝗋𝗒𝖮𝗉​(𝖤𝗑𝗉𝗋,𝖤𝗑𝗉𝗋)∣​𝖡𝗂𝗇𝖺𝗋𝗒𝖮𝗉​(𝖤𝗑𝗉𝗋,𝖢𝗈𝗇𝗌𝗍𝖺𝗇𝗍)∣𝖡𝗂𝗇𝖺𝗋𝗒𝖮𝗉\_𝖠𝗌𝗒𝗆(𝖢𝗈𝗇𝗌𝗍𝖺𝗇𝗍,𝖤𝗑𝗉𝗋)∣𝖱𝗈𝗅𝗅𝗂𝗇𝗀𝖮𝗉(𝖤𝗑𝗉𝗋,𝖭𝗎𝗆)∣𝖯𝖺𝗂𝗋𝖾𝖽𝖱𝗈𝗅𝗅𝗂𝗇𝗀𝖮𝗉(𝖤𝗑𝗉𝗋,𝖤𝗑𝗉𝗋,𝖭𝗎𝗆),𝖭𝗎𝗆→ 20∣…,𝖢𝗈𝗇𝗌𝗍𝖺𝗇𝗍→−0.01∣…\begin{aligned} \mathsf{Expr}\;\to\;&\;\mathsf{Feature}\;\mid\;\mathsf{UnaryOp}(\mathsf{Expr})\\ &\mid\;\mathsf{BinaryOp}(\mathsf{Expr},\mathsf{Expr})\mid\mathsf{BinaryOp}(\mathsf{Expr},\mathsf{Constant})\\ &\mid\;\mathsf{BinaryOp\\_Asym}(\mathsf{Constant},\mathsf{Expr})\\ &\mid\;\mathsf{RollingOp}(\mathsf{Expr},\mathsf{Num})\\ &\mid\;\mathsf{PairedRollingOp}(\mathsf{Expr},\mathsf{Expr},\mathsf{Num}),\\ \mathsf{Num}\;\to\;&\;20\mid\dots,\qquad\mathsf{Constant}\;\to\;-0.01\mid\dots\end{aligned} |  |

The terminal symbols and operators of α\alpha-Sem can be revised or extended beyond [Table 4](https://arxiv.org/html/2601.22119v1#A1.T4 "In Appendix A Tables ‣ Alpha Discovery via Grammar-Guided Learning and Search"), [Table 5](https://arxiv.org/html/2601.22119v1#A1.T5 "In Appendix A Tables ‣ Alpha Discovery via Grammar-Guided Learning and Search"), and [Table 6](https://arxiv.org/html/2601.22119v1#A1.T6 "In Appendix A Tables ‣ Alpha Discovery via Grammar-Guided Learning and Search") to support other domains or tasks in quantitative finance.

#### Length Bounded Grammar α\alpha-Sem-kk.

Although α\alpha-Sem enforces both syntactic and semantic validity, its recursive production rules can still generate expressions of unbounded depth, leading to an intractable search space.
We apply *kk-bounded constraint*, which assign each alpha expression with a length counter kk capped at KK. Each production rule incurs an incremental cost Δ​k\Delta k ([Table 7](https://arxiv.org/html/2601.22119v1#A1.T7 "In Appendix A Tables ‣ Alpha Discovery via Grammar-Guided Learning and Search")), and a rule may be applied only if k+Δ​k≤Kk+\Delta k\leq K.
This constraint yields a bounded semantic grammar α\alpha-Sem-kk ([Algorithm 2](https://arxiv.org/html/2601.22119v1#alg2 "In B.2 Length control of semantic interpretable alpha factor generator ‣ Appendix B Algorithms ‣ Alpha Discovery via Grammar-Guided Learning and Search")).

### 3.3 Alpha Space Structure

Each grammar above (α\alpha-Syn, α\alpha-Sem, and α\alpha-Sem-kk) generates a space of many alpha expressions, corresponding to a *formal alpha language*, denoted by
ℒsyn\mathcal{L}\_{\mathrm{syn}}, ℒsem\mathcal{L}\_{\mathrm{sem}}, and ℒsem≤K\mathcal{L}\_{\mathrm{sem}}^{\leq K}, respectively.
These languages are naturally nested, as illustrated in [Figure 1](https://arxiv.org/html/2601.22119v1#S3.F1 "In 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search"), with each successive layer imposing additional constraints and yielding a progressively smaller and more structured hypothesis space for alpha discovery.

Among them, the kk-bounded semantic grammar α\alpha-Sem-kk plays a central role in this work.
Bounding the derivation depth while enforcing both syntactic and semantic validity yields a finite yet expressive language ℒsem≤K\mathcal{L}\_{\mathrm{sem}}^{\leq K}, enabling systematic search.
A detailed analysis of the space complexity of ℒsem≤K\mathcal{L}\_{\mathrm{sem}}^{\leq K} is provided in Appendix [E](https://arxiv.org/html/2601.22119v1#A5 "Appendix E Search Space Complexity ‣ Alpha Discovery via Grammar-Guided Learning and Search").

###### Definition 4 (Search Space Structure).

Given a grammar α\alpha-Syn, α\alpha-Sem, or α\alpha-Sem-kk, the corresponding alpha language can be represented as a rooted tree.
The root node corresponds to the start symbol, each edge corresponds to the application of a production rule,
intermediate nodes represent partially derived expressions, and leaf nodes correspond to fully derived alpha factors.

This formulation of [Definition 4](https://arxiv.org/html/2601.22119v1#Thmdefinition4 "Definition 4 (Search Space Structure). ‣ 3.3 Alpha Space Structure ‣ 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search") fundamentally changes the nature of alpha discovery.
Rather than exhaustive searching over the unstructured and infinite symbol space Σ∗\Sigma^{\*}, alpha discovery can now be viewed as exploring a tree-structured language space
ℒsem≤K\mathcal{L}\_{\mathrm{sem}}^{\leq K} induced by α\alpha-Sem-kk.
In this view, our alpha discovery reduces to identifying high-quality leaf nodes within a large but well-organized derivation tree.

![Refer to caption](Search-Tree-0.png)


Figure 2: The tree-structured search space.

[Figure 2](https://arxiv.org/html/2601.22119v1#S3.F2 "In 3.3 Alpha Space Structure ‣ 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search") illustrates the structure of the space
of all alpha expressions under α\alpha-Sem-kk. In this tree, each rounded-box node corresponds to an alpha expression, which is equivalent to an Abstract Syntax Representation (ASR) shown in the middle of the figure. Within each ASR, grey nodes denote nonterminal symbols, colored nodes denote terminal symbols, and edges represent grammar-driven expansion steps. This tree-structured perspective naturally supports tree-based search and learning algorithms.

## 4 Reinforced Alpha Language Tree Search

In the previous section, α\alpha-Sem-kk induces a large yet well-structured tree of candidate alpha factors, where each leaf corresponds to a complete, evaluable expression.
Unlike conventional tree search problems, this space combines (i) explosive early branching, (ii) sharp contraction near a depth bound, and (iii) grammar-driven and formula-dependent actions, resulting in highly non-uniform search dynamics.
Moreover, the predictive performance of an alpha is revealed only at terminal nodes, which yields long-horizon dependencies and sparse rewards.

These challenges make unguided search ineffective and motivate a language-principled decision-making formulation.
Accordingly, we cast alpha discovery as a Tree-Structured Linguistic Markov Decision Process (TSL-MDP) and develop a reinforcement learning–guided, grammar-aware MCTS framework, supported by syntax-aware representation learning for efficient policy and value estimation.

### 4.1 Decision-Making on Large Tree

With [Definition 4](https://arxiv.org/html/2601.22119v1#Thmdefinition4 "Definition 4 (Search Space Structure). ‣ 3.3 Alpha Space Structure ‣ 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search"), alpha discovery can be viewed as a sequential decision process over a large derivation tree. Equivalently, the task reduces to: (i) selecting a high-quality root-to-leaf path that yields a strong alpha, or (ii) expanding an intermediate node (e.g., a partially specified or masked factor) into a more predictive expression.

In this search tree, each complete alpha factor (leaf node) is evaluated by the average IC in [Equation 2](https://arxiv.org/html/2601.22119v1#S2.E2 "In Evaluation via Information Coefficient. ‣ 2 Problem Formulation ‣ Alpha Discovery via Grammar-Guided Learning and Search"), computed from historical market data ([Figure 2](https://arxiv.org/html/2601.22119v1#S3.F2 "In 3.3 Alpha Space Structure ‣ 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search"), [Algorithm 1](https://arxiv.org/html/2601.22119v1#alg1 "In B.1 Linear combination alpha factor algorithm ‣ Appendix B Algorithms ‣ Alpha Discovery via Grammar-Guided Learning and Search")).
This IC serves as the reward signal and can be propagated backward along the derivation path, assigning value estimates to intermediate nodes.
Consequently, partial expressions naturally correspond to states, grammar production rules to actions, and derivation steps to state transitions.

This perspective leads to a principled formulation of grammar-guided alpha discovery as a Markov Decision Process, which we term the *Tree-Structured Linguistic Markov Decision Process (TSL-MDP)*.

###### Definition 5 (TSL-MDP).

Alpha discovery under α\alpha-Sem-kk is a Tree-Structured Linguistic Markov Decision Process
TSL-MDP=⟨S,A,P,R,γ⟩\text{TSL-MDP}=\langle S,A,P,R,\gamma\rangle, where
SS is the set of partial or complete alpha expressions;
AA is the set of grammar production rules in [Definition 3](https://arxiv.org/html/2601.22119v1#Thmdefinition3 "Definition 3 (𝛼-Sem). ‣ Semantic Constraints. ‣ 3.2 Semantically-Interpretable Alpha Language ‣ 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search");
P​(s′∣s,a)P(s^{\prime}\mid s,a) deterministically applies rule aa to expand the leftmost nonterminal in ss, yielding a longer alpha expression s′s^{\prime};
and reward R​(s,a)R(s,a) is nonzero only when s′s^{\prime} is a complete alpha expression, equal to its IC evaluated on market data.

![Refer to caption](new-rl2.png)


Figure 3: Grammar-aware reinforcement learning and MCTS, based on alpha representation and value and policy networks.

### 4.2 Reinforcement Learning Guided MCTS

While the tree structure of TSL-MDP makes it amenable to search, classical MCTS becomes ineffective at this scale due to long-horizon dependencies, highly irregular branching, and the absence of intermediate rewards.
We embed MCTS into a reinforcement learning framework that is explicitly tailored to grammar-based alpha generation.

Specifically, two neural networks are introduced: a policy network that predicts promising grammar production rules conditioned on a partial expression, and a value network that estimates the expected predictive quality of an incomplete alpha.
Both networks are driven by a Tree-LSTM encoder (Tai et al., [2015](https://arxiv.org/html/2601.22119v1#bib.bib7 "Improved semantic representations from tree-structured long short-term memory networks")) that consumes the Abstract Syntax Representation ([Definition 1](https://arxiv.org/html/2601.22119v1#Thmdefinition1 "Definition 1. ‣ Structural Well-Formedness. ‣ 3.1 Syntactically-Valid Alpha Language ‣ 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search")) of the current alpha expression, enabling structure-aware generalization across the vast TSL-MDP state space. Our framework is illustrated in [Figure 7](https://arxiv.org/html/2601.22119v1#A4.F7 "In Appendix D Reinforcement Learning Framework ‣ Alpha Discovery via Grammar-Guided Learning and Search").

#### Overall Interaction Between RL and MCTS.

Starting from the start symbol of α\alpha-Sem, alpha generation proceeds iteratively.
At each iteration jj, we perform II rounds of grammar-aware MCTS guided by the current policy and value networks.
The resulting search statistics induce a distribution over different production rules at the root, from which an action is sampled to expand to a node in the next layer of the search tree, which increases the current alpha expression.
The expanded node in this new layer then becomes the new root, and the process repeats until a complete alpha expression is generated.
Each completed alpha yields an IC reward, forming a trajectory of grammar decisions.
By collecting such trajectories, we iteratively update the policy and value networks via reinforcement learning, resulting in an effective *search–learn–search* loop.
An overview of this interaction is illustrated in [Figure 7](https://arxiv.org/html/2601.22119v1#A4.F7 "In Appendix D Reinforcement Learning Framework ‣ Alpha Discovery via Grammar-Guided Learning and Search"), with the corresponding pseudocode provided in [Algorithm 4](https://arxiv.org/html/2601.22119v1#alg4 "In Appendix D Reinforcement Learning Framework ‣ Alpha Discovery via Grammar-Guided Learning and Search").

#### MCTS Components.

At a given root state jj, the MCTS agent incrementally explores a subtree of the TSL-MDP through repeated simulations. Then it executes the following components (see [Figure 3](https://arxiv.org/html/2601.22119v1#S4.F3 "In 4.1 Decision-Making on Large Tree ‣ 4 Reinforced Alpha Language Tree Search ‣ Alpha Discovery via Grammar-Guided Learning and Search") (a) and Appendix [B.3](https://arxiv.org/html/2601.22119v1#A2.SS3 "B.3 Algorithm of Four Stages of MCTS ‣ Appendix B Algorithms ‣ Alpha Discovery via Grammar-Guided Learning and Search") for details).

Selection. From the root, the MCTS agent repeatedly applies an α\alpha-CFG production rule to the leftmost nonterminal symbol until reaching a frontier node which has not yet been expanded.
The TSL-MDP exhibits highly irregular branching, with depth-dependent numbers of applicable production rules.
We therefore introduce an adaptive branching factor in the PUCT formulation, where bb denotes the number of valid actions at the current state and brefb\_{\text{ref}} is a normalization constant given by the maximum branching factor.
The ratio bbref\sqrt{\frac{b}{b\_{\text{ref}}}} modulates the exploration term, emphasizing exploitation for small branching factors and promoting broader exploration for larger ones. Accordingly, we use the adapted PUCT-style selection rule (Silver et al., [2017](https://arxiv.org/html/2601.22119v1#bib.bib5 "Mastering the game of go without human knowledge")):

|  |  |  |
| --- | --- | --- |
|  | a∗=arg⁡maxa⁡(Q​(s,a)+cpuct​bbref​P​(s,a)​∑bN​(s,b)1+N​(s,a))a^{\*}=\arg\max\_{a}\left(Q(s,a)+c\_{\text{puct}}\sqrt{\tfrac{b}{b\_{\text{ref}}}}\,P(s,a)\tfrac{\sqrt{\sum\_{b}N(s,b)}}{1+N(s,a)}\right) |  |

Expansion and Evaluation.
Upon reaching a frontier node, all valid α\alpha-CFG production rules are applied to generate its child states. The resulting node is evaluated using a Tree-LSTM–based value network V​(s)V(s), which estimates the expected terminal reward of the corresponding partial expression. Meanwhile, a policy network produces a distribution P​(s,a)P(s,a) over valid production rules, providing prior guidance for future selections.

Backpropagation. The evaluation result V​(s)V(s) is backpropagated along the selection path, updating Q​(s,a)Q(s,a) and visit counts N​(s,a)N(s,a). Iterating these steps allow MCTS agent progressively expands its explored subtree and refines the search statistics over the TSL-MDP ([Algorithm 3](https://arxiv.org/html/2601.22119v1#alg3 "In B.3 Algorithm of Four Stages of MCTS ‣ Appendix B Algorithms ‣ Alpha Discovery via Grammar-Guided Learning and Search")).

Table 2: Evaluation metrics comparison of different methods (5 random seeds).

| CSI300 | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Method | Rank IC | IC | Rank ICIR | ICIR | Sharpe | Max Drawdown |
| XGBoost | 0.0288 (0.0000) | 0.0326 (0.0000) | 0.2895 (0.0000) | 0.2818 (0.0000) | 0.2853 (0.0000) | -0.2777 (0.0000) |
| LightGBM | 0.0539 (0.0029) | 0.0296 (0.0014) | 0.3963 (0.0247) | 0.2649 (0.0395) | 0.2680 (0.0666) | -0.3271 (0.0177) |
| LSTM | 0.0128 (0.0260) | 0.0127 (0.0136) | 0.0896 (0.2064) | 0.1041 (0.1060) | 0.1268 (0.0425) | -0.3542 (0.0240) |
| TCN | 0.0303 (0.0236) | 0.0085 (0.0133) | 0.2726 (0.1855) | 0.0871 (0.1557) | 0.0908 (0.0754) | -0.2988 (0.0191) |
| ALSTM | 0.0138 (0.0076) | 0.0105 (0.0067) | 0.1194 (0.0540) | 0.0950 (0.0550) | 0.1372 (0.1113) | -0.3475 (0.0501) |
| Transformer | 0.0423 (0.0133) | 0.0248 (0.0132) | 0.3759 (0.0697) | 0.2457 (0.0971) | 0.1699 (0.1105) | -0.3365 (0.0377) |
| gplearn | 0.0706 (0.0119) | 0.0440 (0.0139) | 0.4695 (0.1164) | 0.3478 (0.1397) | 0.2062 (0.2346) | -0.3854 (0.0324) |
| AlphaQCM | 0.0811 (0.0046) | 0.0525 (0.0048) | 0.5334 (0.0296) | 0.3874 (0.0121) | 0.4363 (0.0610) | -0.3605 (0.0339) |
| RPN+PPO(AlphaGen) | 0.0837 (0.0070) | 0.0477 (0.0086) | 0.5724 (0.0343) | 0.3531 (0.0574) | 0.4978 (0.1478) | -0.3497 (0.0423) |
| Ablation Studies | | | | | | |
| RPN+MCTS | 0.0710 (0.0031) | 0.0500 (0.0026) | 0.5577 (0.0292) | 0.4285 (0.0293) | 0.5639 (0.1050) | -0.3201 (0.0613) |
| α\alpha-Syn+MCTS | 0.0745 (0.0052) | 0.0487 (0.0036) | 0.5125 (0.0467) | 0.3974 (0.0367) | 0.4852 (0.1320) | -0.3475 (0.0414) |
| α\alpha-Sem+MCTS | 0.0770 (0.0044) | 0.0512 (0.0015) | 0.5593 (0.0340) | 0.4369 (0.0301) | 0.5801 (0.1169) | -0.3039 (0.0206) |
| α\alpha-Sem-kk+MCTS(AlphaCFG) | 0.0865 (0.0060) | 0.0577 (0.0029) | 0.6036 (0.0537) | 0.4505 (0.0249) | 0.6459 (0.0612) | -0.2963 (0.0289) |
| S&P500 | | | | | | |
| Method | Rank IC | IC | Rank ICIR | ICIR | Sharpe | Max Drawdown |
| XGBoost | 0.0140 (0.0000) | 0.0104 (0.0000) | 0.1535 (0.0000) | 0.1456 (0.0000) | 0.5883 (0.0000) | -0.2543 (0.0000) |
| LightGBM | 0.0078 (0.0021) | 0.0220 (0.0032) | 0.0860 (0.0269) | 0.2072 (0.0229) | 0.5852 (0.0547) | -0.2047 (0.0128) |
| LSTM | 0.0131 (0.0077) | 0.0219 (0.0040) | 0.1157 (0.0786) | 0.1847 (0.0419) | 0.5601 (0.0546) | -0.2345 (0.0142) |
| TCN | 0.0198 (0.0040) | 0.0166 (0.0020) | 0.1358 (0.0190) | 0.1340 (0.0133) | 0.4973 (0.0271) | -0.2396 (0.0175) |
| ALSTM | 0.0202 (0.0028) | 0.0268 (0.0039) | 0.1569 (0.0344) | 0.1993 (0.0391) | 0.4441 (0.0397) | -0.2418 (0.0109) |
| Transformer | 0.0106 (0.0049) | 0.0185 (0.0036) | 0.0828 (0.0433) | 0.1806 (0.0361) | 0.5979 (0.1163) | -0.2512 (0.0070) |
| gplearn | 0.0130 (0.0122) | 0.0322 (0.0110) | 0.0812 (0.0643) | 0.1877 (0.0437) | 0.8241 (0.1814) | -0.2456 (0.0434) |
| AlphaQCM | 0.0178 (0.0055) | 0.0384 (0.0056) | 0.1149 (0.0381) | 0.2527 (0.0336) | 1.0566 (0.0756) | -0.2105 (0.0273) |
| RPN+PPO(AlphaGen) | 0.0149 (0.0055) | 0.0342 (0.0050) | 0.1045 (0.0364) | 0.2420 (0.0296) | 0.8271 (0.1421) | -0.2559 (0.0242) |
| Ablation Studies | | | | | | |
| RPN+MCTS | 0.0309 (0.0054) | 0.0385 (0.0031) | 0.2447 (0.0234) | 0.3308 (0.0344) | 0.7992 (0.0854) | -0.1957 (0.0140) |
| α\alpha-Syn+MCTS | 0.0111 (0.0017) | 0.0272 (0.0047) | 0.0913 (0.0087) | 0.2335 (0.0356) | 0.8046 (0.0322) | -0.2286 (0.0186) |
| α\alpha-Sem+MCTS | 0.0265 (0.0011) | 0.0413 (0.0030) | 0.2075 (0.0108) | 0.3360 (0.0162) | 0.8315 (0.0855) | -0.2243 (0.0225) |
| α\alpha-Sem-kk+MCTS(AlphaCFG) | 0.0354 (0.0026) | 0.04573 (0.0034) | 0.2958(0.0154) | 0.4099 (0.0230) | 0.8473 (0.0483) | -0.1942 (0.0126) |

### 4.3 Syntax Representation Learning

Network Design.
The main challenge in TSL-MDP is its vast state space, which requires evaluating both partial and complete alpha expressions as well as policies for expanding them.
Since each state is naturally represented by an ASR ([Definition 1](https://arxiv.org/html/2601.22119v1#Thmdefinition1 "Definition 1. ‣ Structural Well-Formedness. ‣ 3.1 Syntactically-Valid Alpha Language ‣ 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search")), we employ syntax-aware representation learning that directly encodes structure and semantics, which avoids costly rollout-based evaluations in classical MCTS.
Moreover, due to the symmetry of some operators (e.g., commutative operands), there are a large number of isomorphic factor expressions (defined in [Definition 6](https://arxiv.org/html/2601.22119v1#Thmdefinition6 "Definition 6 (Isomorphism of ASR(Tree)). ‣ Appendix G Calculation of Tree Similarity ‣ Alpha Discovery via Grammar-Guided Learning and Search")) in TSL-MDP. Syntax-aware representation learning is suitable for addressing these redundancies as it operates directly on ASRs rather than linear sequence.

Accordingly, we use a Tree-LSTM encoder (Tai et al., [2015](https://arxiv.org/html/2601.22119v1#bib.bib7 "Improved semantic representations from tree-structured long short-term memory networks")) with two heads: a policy head for predicting production-rule distributions and a value head for estimating terminal rewards (details are provided in Appendix [F](https://arxiv.org/html/2601.22119v1#A6 "Appendix F Details of Tree-LSTM ‣ Alpha Discovery via Grammar-Guided Learning and Search")).
As shown in [Figure 3](https://arxiv.org/html/2601.22119v1#S4.F3 "In 4.1 Decision-Making on Large Tree ‣ 4 Reinforced Alpha Language Tree Search ‣ Alpha Discovery via Grammar-Guided Learning and Search") (b), the Tree-LSTM recursively aggregates information, producing a fixed-dimensional state embedding for each ASR. This embedding is shared by both policy network for production-rule prediction and value network for state-value estimation in MCTS.

Train and Sampling Procedure. The policy and value networks are trained jointly using Tree-LSTM representations of TSL-MDP states.
Initially, both networks are randomly initialized and used to guide MCTS expansion and evaluation.
The resulting search statistics define an initial policy for alpha generation, which is then used to: (i) supervise the policy network via imitation of the MCTS-derived action distribution, and (ii) sample complete alpha expressions whose IC values (from market data) provide supervision for the value network.
In subsequent iterations, the updated networks guide new MCTS constructions, and the process repeats until enough alphas have been sampled.

Diversity-Aware Value Target.
Since the ultimate objective is to construct a composite factor ICℱ\mathrm{IC}\_{\mathcal{F}} (See [Algorithm 1](https://arxiv.org/html/2601.22119v1#alg1 "In B.1 Linear combination alpha factor algorithm ‣ Appendix B Algorithms ‣ Alpha Discovery via Grammar-Guided Learning and Search")), generating expressions that are structurally similar to existing factors can reduce pool diversity and degrade overall performance. To mitigate this, we incorporate a diversity-aware adjustment into the value target.
Specifically, we define a normalized structural similarity measure sim​(⋅,⋅)\mathrm{sim}(\cdot,\cdot), based on maximum common subtree matching (Sager et al., [2006](https://arxiv.org/html/2601.22119v1#bib.bib11 "Detecting similar java classes using tree algorithms")) between the newly generated ASR fjf\_{j} corresponding to state sjs\_{j} and any existing ft∈ℱf\_{t}\in\mathcal{F}. This similarity penalizes states whose grammatical structures overlap with ℱ\mathcal{F}. The resulting value target is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | z​(sj)=(1−max⁡(0,maxft∈ℱ⁡sim​(ft,fj)))⋅ICℱ.z(s\_{j})=\bigl(1-\max(0,\max\_{f\_{t}\in\mathcal{F}}\mathrm{sim}(f\_{t},f\_{j}))\bigr)\cdot\mathrm{IC}\_{\mathcal{F}}. |  | (5) |

More details about tree similarity can be seen in [Appendix G](https://arxiv.org/html/2601.22119v1#A7 "Appendix G Calculation of Tree Similarity ‣ Alpha Discovery via Grammar-Guided Learning and Search").

## 5 Experiments

Detailed experimental settings, including datasets, comparison methods, evaluation metrics, and hyperparameters, are provided in the Appendix
([Section I.1](https://arxiv.org/html/2601.22119v1#A9.SS1 "I.1 Data ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search"), [Section I.2](https://arxiv.org/html/2601.22119v1#A9.SS2 "I.2 Comparison Methods ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search"), [Section I.3](https://arxiv.org/html/2601.22119v1#A9.SS3 "I.3 Evaluation Metrics ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search"), and [Appendix H](https://arxiv.org/html/2601.22119v1#A8 "Appendix H AlphaCFG Framework Parameter Setting for Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search")).
Analysis on network architectures and mined factor examples with interpretability discussions are presented in
[Section I.4](https://arxiv.org/html/2601.22119v1#A9.SS4 "I.4 Comparison of Different Network Architectures ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search") and [Section I.6](https://arxiv.org/html/2601.22119v1#A9.SS6 "I.6 Case Study of the interpretability of formulaic factors ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search"), respectively.

Comparison of Generation Spaces. We first compare different factor generation spaces ([Figure 1](https://arxiv.org/html/2601.22119v1#S3.F1 "In 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search")) to evaluate the impact of language constraints on factor discovery. Specifically, we compare three CFG levels with Reverse Polish Notation (RPN) (Krtolica and Stanimirović, [2004](https://arxiv.org/html/2601.22119v1#bib.bib33 "Reverse polish notation method")), a computation and verification formalism with a non-recursive structure, on the CSI 300 and S&P 500 training datasets.
With a pool size of 10 and max length 5, [Figure 4](https://arxiv.org/html/2601.22119v1#S5.F4 "In 5 Experiments ‣ Alpha Discovery via Grammar-Guided Learning and Search") shows the training IC across epochs.
Results confirm our analysis in [Section 3.3](https://arxiv.org/html/2601.22119v1#S3.SS3 "3.3 Alpha Space Structure ‣ 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search"), where more constrained, grammar-defined spaces yield faster convergence and higher-quality factors.
Although RPN converges to a performance level close to α\alpha-Sem, its convergence is noticeably slower.
This behavior reflects the limited semantic and length constraints of RPN, whose non-recursive structure restricts its effectiveness for structured factor generation compared to α\alpha-Sem.

![Refer to caption](x1.png)


Figure 4: Comparison of training curves of generation methods.

Comparison with Existing Alpha Mining Methods. To create a fair comparison environment, we use the optimized hyperparameters from the validation dataset experiments (see details in Appendix [I.5](https://arxiv.org/html/2601.22119v1#A9.SS5 "I.5 Optimization of Combined Factor Parameters on the Validation Set ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search")) for each method, including our MCTS-based methods (α\alpha-Syn, α\alpha-Sem, α\alpha-Sem-kk and RPN) against existing factor mining methods or prediction models (formulaic: Alphagen, AlphaQCM, GPlearn; ML-based: XGBoost, LightGBM, LSTM, ALSTM, TCN, Transformer). The experiments were conducted separately on the CSI 300 index and the S&P 500 constituents testing data, evaluating both correlation-based metrics and backtesting performance. The backtesting results are obtained using a single top-kk/drop-nn strategy to conduct simulated trading based on real stock data (detailed in Appendix [I.3](https://arxiv.org/html/2601.22119v1#A9.SS3 "I.3 Evaluation Metrics ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search")).
Quantitative results are summarized in [Table 2](https://arxiv.org/html/2601.22119v1#S4.T2 "In MCTS Components. ‣ 4.2 Reinforcement Learning Guided MCTS ‣ 4 Reinforced Alpha Language Tree Search ‣ Alpha Discovery via Grammar-Guided Learning and Search"), and cumulative return curves are shown in [Figure 5](https://arxiv.org/html/2601.22119v1#S5.F5 "In 5 Experiments ‣ Alpha Discovery via Grammar-Guided Learning and Search").

![Refer to caption](x2.png)


(a) CSI 300

![Refer to caption](x3.png)


(b) S&P 500

Figure 5: Cumulative return comparison in simulated trading

Overall, our method achieves the best performance across all correlation metrics directly related to the optimization target IC.
Ablation studies further demonstrate the indispensable roles of syntactic constraints, semantic constraints, and length control.
While formulaic factor mining methods generally outperform machine-learning models that directly predict returns in correlation metrics, our approach also achieves strong backtesting performance.
Despite not directly optimizing for backtesting objectives, our method consistently attains superior Sharpe ratios and lower maximum drawdowns, and achieves the highest overall profitability among all compared methods.

Improving Traditional Alpha Factors.
Beyond directly mining composite factors, our α\alpha-Sem-kk+MCTS framework can be used to refine existing interpretable alpha factors.
We select a set of classic but recently ineffective factors from the GTJA 191 Factor Library and the Alpha101 Factor Library (Kakushadze, [2016](https://arxiv.org/html/2601.22119v1#bib.bib12 "101 formulaic alphas")).
Factors from the GTJA 191 library are refined using the CSI 300 dataset, while Alpha101 factors are refined using the S&P 500 dataset.
By partially masking operators and operands while preserving the left-side structure within half of the original expression length, we optimize these factors using a single-factor reward objective (illustrated by the blue path in [Figure 2](https://arxiv.org/html/2601.22119v1#S3.F2 "In 3.3 Alpha Space Structure ‣ 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search")).
As shown in [Table 3](https://arxiv.org/html/2601.22119v1#S5.T3 "In 5 Experiments ‣ Alpha Discovery via Grammar-Guided Learning and Search"), our framework consistently improves the absolute IC values of many classic factors on the test datasets, demonstrating its effectiveness in strengthening existing alpha signals.

Table 3: Refinement Results: Test Set IC Before and After Applying α\alpha-Sem-kk+MCTS framework.

|  |  |
| --- | --- |
| GTJA191 | |
| Original: open/Ref(close,1)-1 | 0.00185 |
| Improved: open/0.1-Cov(volume,high,20) | 0.04279 |
| Original: Mean(close,6)-close | 0.00482 |
| Improved: Mean(Cov(vwap,volume,20)/(-0.01),20)/0.05 | 0.04262 |
| Original: close-Ref(close,5) | 0.00495 |
| Improved: close-Greater(-0.1,Cov(volume,|vwap|,30)) | 0.03872 |
| Alpha101 | |
| Original: -Corr(open,volume,10) | 0.00271 |
| Improved: Corr(open,Log(|open|),40)·CSRank(high) | 0.02934 |
| Original: -Rank(CSRank(low),9) | 0.01031 |
| Improved: Rank(CSRank(CSRank(Sign(vwap))),30)·CSRank(high) | 0.02944 |
| Original: Pow(high· low,0.5)-vwap) | 0.00112 |
| Improved: Pow(CSRank(|open|)·open,CSRank(close))-vwap | 0.03126 |

## 6 Conclusion

AlphaCFG formulates alpha factor discovery as a grammar-guided, syntax-tree–structured search problem that enforces interpretability while enabling efficient integration of reinforcement learning with neural Monte Carlo Tree Search.
Beyond trading, the framework naturally extends to other factor-based quantitative finance tasks.
More broadly, AlphaCFG exemplifies grammar-guided symbolic regression, where domain knowledge is encoded directly in the search space rather than learned implicitly from data.
A promising direction for future work is to integrate AlphaCFG with large-scale learned priors, such as foundation models over programs or syntax trees, to further accelerate search and improve generalization in structured reasoning problems.

## References

* H. N. Bhandari, B. Rimal, N. R. Pokhrel, R. Rimal, K. R. Dahal, and R. K. Khatri (2022)
  Predicting stock market index using lstm.
  Machine Learning with Applications 9,  pp. 100320.
  Cited by: [§I.2](https://arxiv.org/html/2601.22119v1#A9.SS2.p3.1 "I.2 Comparison Methods ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search"),
  [§1.1](https://arxiv.org/html/2601.22119v1#S1.SS1.p2.1 "1.1 Alpha discovery ‣ 1 Introduction ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* K. Bisdoulis (2024)
  Assets forecasting with feature engineering and transformation methods for lightgbm.
  arXiv preprint arXiv:2501.07580.
  Cited by: [§I.2](https://arxiv.org/html/2601.22119v1#A9.SS2.p3.1 "I.2 Comparison Methods ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search"),
  [§1.1](https://arxiv.org/html/2601.22119v1#S1.SS1.p2.1 "1.1 Alpha discovery ‣ 1 Introduction ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* M. M. Carhart (1997)
  On persistence in mutual fund performance.
  The Journal of Finance 52 (1),  pp. 57–82.
  Cited by: [§1.1](https://arxiv.org/html/2601.22119v1#S1.SS1.p2.1 "1.1 Alpha discovery ‣ 1 Introduction ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* N. Chomsky and M. P. Schützenberger (1959)
  The algebraic theory of context-free languages.
  In Studies in Logic and the Foundations of Mathematics,
  Vol. 26,  pp. 118–161.
  Cited by: [§3](https://arxiv.org/html/2601.22119v1#S3.p3.1 "3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* W. Dai, Y. An, and W. Long (2022)
  Price change prediction of ultra high frequency financial data based on temporal convolutional network.
  Procedia Computer Science 199,  pp. 1177–1183.
  Cited by: [§I.2](https://arxiv.org/html/2601.22119v1#A9.SS2.p3.1 "I.2 Comparison Methods ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search"),
  [§1.1](https://arxiv.org/html/2601.22119v1#S1.SS1.p2.1 "1.1 Alpha discovery ‣ 1 Introduction ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* E. F. Fama and K. R. French (1992)
  The cross-section of expected stock returns.
  The Journal of Finance 47 (2),  pp. 427–465.
  Cited by: [§1.1](https://arxiv.org/html/2601.22119v1#S1.SS1.p2.1 "1.1 Alpha discovery ‣ 1 Introduction ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* R. C. Grinold and R. N. Kahn (2000)
  Active portfolio management.
  Cited by: [§2](https://arxiv.org/html/2601.22119v1#S2.SS0.SSS0.Px1.p1.4 "Evaluation via Information Coefficient. ‣ 2 Problem Formulation ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* J. E. Hopcroft and J. D. Ullman (1979)
  Automata theory, languages, and computation.
   Addison-Wesley.
  Cited by: [§3](https://arxiv.org/html/2601.22119v1#S3.p3.1 "3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search"),
  [footnote 2](https://arxiv.org/html/2601.22119v1#footnote2 "In Structural Well-Formedness. ‣ 3.1 Syntactically-Valid Alpha Language ‣ 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* L. Jin, F. Doshi-Velez, T. Miller, W. Schuler, and L. Schwartz (2018)
  Unsupervised grammar induction with depth-bounded pcfg.
  Transactions of the Association for Computational Linguistics 6,  pp. 211–224.
  Cited by: [§B.2](https://arxiv.org/html/2601.22119v1#A2.SS2.p1.7 "B.2 Length control of semantic interpretable alpha factor generator ‣ Appendix B Algorithms ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* Z. Kakushadze (2016)
  101 formulaic alphas.
  Wilmott (84),  pp. 72–81.
  Cited by: [§5](https://arxiv.org/html/2601.22119v1#S5.p5.2 "5 Experiments ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* P. V. Krtolica and P. S. Stanimirović (2004)
  Reverse polish notation method.
  International Journal of Computer Mathematics 81 (3),  pp. 273–284.
  Cited by: [§5](https://arxiv.org/html/2601.22119v1#S5.p2.2 "5 Experiments ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* J. W. Lee (2001)
  Stock price prediction using reinforcement learning.
  In ISIE 2001. 2001 IEEE International Symposium on Industrial Electronics Proceedings (Cat. No. 01TH8570),
  Vol. 1,  pp. 690–695.
  Cited by: [§1.1](https://arxiv.org/html/2601.22119v1#S1.SS1.p2.1 "1.1 Alpha discovery ‣ 1 Introduction ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* N. Makke and S. Chawla (2024)
  Interpretable scientific discovery with symbolic regression: a review.
  Artificial Intelligence Review 57 (1),  pp. 2.
  Cited by: [§1.1](https://arxiv.org/html/2601.22119v1#S1.SS1.p3.1 "1.1 Alpha discovery ‣ 1 Introduction ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* L. Mozaffari and J. Zhang (2024)
  Predictive modeling of stock prices using transformer model.
  In Proceedings of the 2024 9th International Conference on Machine Learning Technologies,
   pp. 41–48.
  Cited by: [§I.2](https://arxiv.org/html/2601.22119v1#A9.SS2.p3.1 "I.2 Comparison Methods ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search"),
  [§1.1](https://arxiv.org/html/2601.22119v1#S1.SS1.p2.1 "1.1 Alpha discovery ‣ 1 Introduction ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* Y. Qin, D. Song, H. Chen, W. Cheng, G. Jiang, and G. Cottrell (2017)
  A dual-stage attention-based recurrent neural network for time series prediction.
  arXiv preprint arXiv:1704.02971.
  Cited by: [§I.2](https://arxiv.org/html/2601.22119v1#A9.SS2.p3.1 "I.2 Comparison Methods ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search"),
  [§1.1](https://arxiv.org/html/2601.22119v1#S1.SS1.p2.1 "1.1 Alpha discovery ‣ 1 Introduction ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* T. Sager, H. C. Gall, M. Pinzger, and A. Bernstein (2006)
  Detecting similar java classes using tree algorithms.
  In Proceedings of the 2006 ACM Symposium on Applied Computing,
   pp. 654–661.
  Cited by: [§4.3](https://arxiv.org/html/2601.22119v1#S4.SS3.p4.6 "4.3 Syntax Representation Learning ‣ 4 Reinforced Alpha Language Tree Search ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* D. Silver, J. Schrittwieser, K. Simonyan, I. Antonoglou, A. Huang, A. Guez, T. Hubert, L. Baker, M. Lai, A. Bolton, et al. (2017)
  Mastering the game of go without human knowledge.
  nature 550 (7676),  pp. 354–359.
  Cited by: [§B.3](https://arxiv.org/html/2601.22119v1#A2.SS3.p3.10 "B.3 Algorithm of Four Stages of MCTS ‣ Appendix B Algorithms ‣ Alpha Discovery via Grammar-Guided Learning and Search"),
  [§4.2](https://arxiv.org/html/2601.22119v1#S4.SS2.SSS0.Px2.p2.4 "MCTS Components. ‣ 4.2 Reinforcement Learning Guided MCTS ‣ 4 Reinforced Alpha Language Tree Search ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* K. S. Tai, R. Socher, and C. D. Manning (2015)
  Improved semantic representations from tree-structured long short-term memory networks.
  arXiv preprint arXiv:1503.00075.
  Cited by: [§4.2](https://arxiv.org/html/2601.22119v1#S4.SS2.p2.1 "4.2 Reinforcement Learning Guided MCTS ‣ 4 Reinforced Alpha Language Tree Search ‣ Alpha Discovery via Grammar-Guided Learning and Search"),
  [§4.3](https://arxiv.org/html/2601.22119v1#S4.SS3.p2.1 "4.3 Syntax Representation Learning ‣ 4 Reinforced Alpha Language Tree Search ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* J. Wang, Q. Cheng, and Y. Dong (2023)
  An xgboost-based multivariate deep learning framework for stock index futures price forecasting.
  Kybernetes 52 (10),  pp. 4158–4177.
  Cited by: [§I.2](https://arxiv.org/html/2601.22119v1#A9.SS2.p3.1 "I.2 Comparison Methods ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search"),
  [§1.1](https://arxiv.org/html/2601.22119v1#S1.SS1.p2.1 "1.1 Alpha discovery ‣ 1 Introduction ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* Q. Xu (2025)
  Unsupervised temporal encoding for stock price prediction through dual-phase learning.
  In Proceedings of the 2025 International Conference on Economic Management and Big Data Application,
   pp. 778–784.
  Cited by: [§1.1](https://arxiv.org/html/2601.22119v1#S1.SS1.p2.1 "1.1 Alpha discovery ‣ 1 Introduction ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* X. Yang, W. Liu, D. Zhou, J. Bian, and T. Liu (2020)
  Qlib: an ai-oriented quantitative investment platform.
  arXiv preprint arXiv:2009.11189.
  Cited by: [§I.2](https://arxiv.org/html/2601.22119v1#A9.SS2.p3.1 "I.2 Comparison Methods ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search"),
  [§2](https://arxiv.org/html/2601.22119v1#S2.p3.1 "2 Problem Formulation ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* S. Yu, H. Xue, X. Ao, F. Pan, J. He, D. Tu, and Q. He (2023)
  Generating synergistic formulaic alpha collections via reinforcement learning.
  In Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining,
   pp. 5476–5486.
  Cited by: [§I.2](https://arxiv.org/html/2601.22119v1#A9.SS2.p2.1 "I.2 Comparison Methods ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search"),
  [§1.1](https://arxiv.org/html/2601.22119v1#S1.SS1.p3.1 "1.1 Alpha discovery ‣ 1 Introduction ‣ Alpha Discovery via Grammar-Guided Learning and Search"),
  [§2](https://arxiv.org/html/2601.22119v1#S2.SS0.SSS0.Px1.p3.1 "Evaluation via Information Coefficient. ‣ 2 Problem Formulation ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* T. Zhang, Y. Li, Y. Jin, and J. Li (2020)
  Autoalpha: an efficient hierarchical evolutionary algorithm for mining alpha factors in quantitative investment.
  arXiv preprint arXiv:2002.08245.
  Cited by: [§I.2](https://arxiv.org/html/2601.22119v1#A9.SS2.p2.1 "I.2 Comparison Methods ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search"),
  [§1.1](https://arxiv.org/html/2601.22119v1#S1.SS1.p2.1 "1.1 Alpha discovery ‣ 1 Introduction ‣ Alpha Discovery via Grammar-Guided Learning and Search"),
  [§1.1](https://arxiv.org/html/2601.22119v1#S1.SS1.p3.1 "1.1 Alpha discovery ‣ 1 Introduction ‣ Alpha Discovery via Grammar-Guided Learning and Search").
* Z. Zhu and K. Zhu (2025)
  AlphaQCM: alpha discovery in finance with distributional reinforcement learning.
  In Forty-second International Conference on Machine Learning,
  Cited by: [§I.2](https://arxiv.org/html/2601.22119v1#A9.SS2.p2.1 "I.2 Comparison Methods ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search"),
  [§1.1](https://arxiv.org/html/2601.22119v1#S1.SS1.p3.1 "1.1 Alpha discovery ‣ 1 Introduction ‣ Alpha Discovery via Grammar-Guided Learning and Search").

## Appendix A Tables

Table 4: Stock Feature Variables

| Feature | Description |
| --- | --- |
| open | Opening price |
| high | Highest price |
| low | Lowest price |
| close | Closing price |
| volume | Trading volume |
| vwap | Volume Weighted Average Price (VWAP) |




Table 5: Constant Parameters

| Nonterminal | Values |
| --- | --- |
| Constant | −0.1,−0.05,−0.01, 0.01, 0.05, 0.1-0.1,\,-0.05,\,-0.01,\,0.01,\,0.05,\,0.1 |
| Num | 20, 30, 4020,\,30,\,40 |




Table 6: Formulaic Alpha Factor Operators in Our Framework (the BinaryOp in Formula ([4](https://arxiv.org/html/2601.22119v1#S3.E4 "Equation 4 ‣ Operator Arity Constraints. ‣ 3.1 Syntactically-Valid Alpha Language ‣ 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search")) does not distinguish whether it is symmetric)

| Operator | Type | Description |
| --- | --- | --- |
| Abs​(x)\text{Abs}(x) | Unary | Absolute value, |x|\lvert x\rvert. |
| Sign​(x)\text{Sign}(x) | Unary | Returns the sign of xx: 1 for positive, -1 for negative, 0 for zero. |
| Log​(x)\text{Log}(x) | Unary | Natural logarithm, log⁡(x)\log(x). |
| Add​(x,y)\text{Add}(x,y) | Binary | Addition, x+yx+y. |
| Mul​(x,y)\text{Mul}(x,y) | Binary | Multiplication, x⋅yx\cdot y. |
| Greater​(x,y)\text{Greater}(x,y) | Binary | Returns the larger of two values: max⁡(x,y)\max(x,y). |
| Less​(x,y)\text{Less}(x,y) | Binary | Returns the smaller of two values: min⁡(x,y)\min(x,y). |
| Div​(x,y)\text{Div}(x,y) | Binary-Asym | Division, x/yx/y. |
| Pow​(x,y)\text{Pow}(x,y) | Binary-Asym | Exponentiation, xyx^{y}. |
| Sub​(x,y)\text{Sub}(x,y) | Binary-Asym | Subtraction, x−yx-y. |
| CSRank​(x)\text{CSRank}(x) | Rolling | Cross-sectional ranking (normalizes the rank of xx across all stocks on the same day). |
| Rank​(x,t)\text{Rank}(x,t) | Rolling | Time-series ranking of xx over the past tt days. |
| WMA​(x,t)\text{WMA}(x,t) | Rolling | Weighted moving average with weights decaying over time. |
| EMA​(x,t)\text{EMA}(x,t) | Rolling | Exponential moving average with recursive smoothing. |
| Ref​(x,t)\text{Ref}(x,t) | Rolling | Value of xx from tt days ago. |
| Mean​(x,t)\text{Mean}(x,t) | Rolling | Mean of xx over the past tt days, 1t​∑i=0t−1x−i\frac{1}{t}\sum\_{i=0}^{t-1}x\_{-i}. |
| Sum​(x,t)\text{Sum}(x,t) | Rolling | Sum of xx over the past tt days, ∑i=0t−1x−i\sum\_{i=0}^{t-1}x\_{-i}. |
| Std​(x,t)\text{Std}(x,t) | Rolling | Standard deviation of xx over the past tt days. |
| Var​(x,t)\text{Var}(x,t) | Rolling | Variance of xx over the past tt days. |
| Skew​(x,t)\text{Skew}(x,t) | Rolling | Skewness (measure of asymmetry) of xx over the past tt days. |
| Kurt​(x,t)\text{Kurt}(x,t) | Rolling | Kurtosis (measure of tail thickness) of xx over the past tt days. |
| Max​(x,t)\text{Max}(x,t) | Rolling | Maximum value of xx over the past tt days. |
| Min​(x,t)\text{Min}(x,t) | Rolling | Minimum value of xx over the past tt days. |
| Med​(x,t)\text{Med}(x,t) | Rolling | Median of xx over the past tt days. |
| Mad​(x,t)\text{Mad}(x,t) | Rolling | Mean absolute deviation, 1t​∑i=0t−1|x−i−x¯|\frac{1}{t}\sum\_{i=0}^{t-1}\lvert x\_{-i}-\bar{x}\rvert. |
| Delta​(x,t)\text{Delta}(x,t) | Rolling | Difference, x−Ref​(x,t)x-\text{Ref}(x,t). |
| Cov​(x,y,t)\text{Cov}(x,y,t) | PairedRolling | Covariance between xx and yy over the past tt days. |
| Corr​(x,y,t)\text{Corr}(x,y,t) | PairedRolling | Pearson correlation coefficient between xx and yy over the past tt days. |




Table 7: 
Length increments Δ​k\Delta k for each production rule.

| Production Rules | Δ​k\Delta k |
| --- | --- |
| 𝖤𝗑𝗉𝗋→𝖥𝖾𝖺𝗍𝗎𝗋𝖾\mathsf{Expr}\to\mathsf{Feature} | 0 |
| 𝖭𝗎𝗆→20​…\mathsf{Num}\to 20\dots | 0 |
| 𝖢𝗈𝗇𝗌𝗍𝖺𝗇𝗍→−0.01​…\mathsf{Constant}\to-0.01\dots | 0 |
| 𝖤𝗑𝗉𝗋→𝖴𝗇𝖺𝗋𝗒𝖮𝗉​(𝖤𝗑𝗉𝗋)\mathsf{Expr}\to\mathsf{UnaryOp}(\mathsf{Expr}) | 1 |
| 𝖤𝗑𝗉𝗋→𝖡𝗂𝗇𝖺𝗋𝗒𝖮𝗉​(𝖤𝗑𝗉𝗋,𝖤𝗑𝗉𝗋)\mathsf{Expr}\to\mathsf{BinaryOp}(\mathsf{Expr},\mathsf{Expr}) | 2 |
| 𝖤𝗑𝗉𝗋→𝖡𝗂𝗇𝖺𝗋𝗒𝖮𝗉​(𝖤𝗑𝗉𝗋,𝖢𝗈𝗇𝗌𝗍𝖺𝗇𝗍)\mathsf{Expr}\to\mathsf{BinaryOp}(\mathsf{Expr},\mathsf{Constant}) | 2 |
| 𝖤𝗑𝗉𝗋→𝖡𝗂𝗇𝖺𝗋𝗒𝖮𝗉​\_​𝖠𝗌𝗒𝗆​(𝖢𝗈𝗇𝗌𝗍𝖺𝗇𝗍,𝖤𝗑𝗉𝗋)\mathsf{Expr}\to\mathsf{BinaryOp\\_Asym}(\mathsf{Constant},\mathsf{Expr}) | 2 |
| 𝖤𝗑𝗉𝗋→𝖱𝗈𝗅𝗅𝗂𝗇𝗀𝖮𝗉​(𝖤𝗑𝗉𝗋,𝖭𝗎𝗆)\mathsf{Expr}\to\mathsf{RollingOp}(\mathsf{Expr},\mathsf{Num}) | 2 |
| 𝖤𝗑𝗉𝗋→𝖯𝖺𝗂𝗋𝖾𝖽𝖱𝗈𝗅𝗅𝗂𝗇𝗀𝖮𝗉​(𝖤𝗑𝗉𝗋,𝖤𝗑𝗉𝗋,𝖭𝗎𝗆)\mathsf{Expr}\to\mathsf{PairedRollingOp}(\mathsf{Expr},\mathsf{Expr},\mathsf{Num}) | 3 |

## Appendix B Algorithms

### B.1 Linear combination alpha factor algorithm

The linear combination factor model is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(X;F,w)=∑j=1nwj​fj​(X)=y,c(X;F,w)=\sum\_{j=1}^{n}w\_{j}f\_{j}(X)=y, |  | (6) |

where F={f1,…,fn}F=\{f\_{1},\dots,f\_{n}\} denotes the set of factors, w={w1,…,wn}w=\{w\_{1},\dots,w\_{n}\} are the weights of factors in linear combination , XX represents the input stock feature data, and yy is the combined output. The optimization is conducted by minimizing the loss function

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(w)=1T​∑t=1T‖yt−rt‖2L(w)=\frac{1}{T}\sum\_{t=1}^{T}\|y\_{t}-r\_{t}\|^{2} |  | (7) |

where rtr\_{t} is the actual stock return, and yty\_{t} is the alpha value of linear combination factor.

Algorithm 1  Incremental Combination Model Optimization

Input: alpha set F={f1,…,fn}F=\{f\_{1},\ldots,f\_{n}\}, weights w={w1,…,wn}w=\{w\_{1},\ldots,w\_{n}\}, new alpha fnewf\_{\text{new}}

Output: optimal alpha subset F∗F^{\*}, optimal weights w∗w^{\*}, combination IC ICℱ\mathrm{IC}\_{\mathcal{F}}

F←F∪{fnew}F\leftarrow F\cup\{f\_{\text{new}}\}

w←w∥rand()w\leftarrow w\,\|\,\text{rand()}

for i=1i=1 to num\_gradient\_steps do

Compute loss L​(w)L(w) according to Eq. ([7](https://arxiv.org/html/2601.22119v1#A2.E7 "Equation 7 ‣ B.1 Linear combination alpha factor algorithm ‣ Appendix B Algorithms ‣ Alpha Discovery via Grammar-Guided Learning and Search"))

w←GradientDescent​(L​(w))w\leftarrow\text{GradientDescent}(L(w))

end for

p←arg⁡mini⁡|wi|p\leftarrow\arg\min\_{i}|w\_{i}|

F←F∖{fp}F\leftarrow F\setminus\{f\_{p}\};  w←w∖{wp}w\leftarrow w\setminus\{w\_{p}\}

Compute the combination IC: ICℱ←IC​(F,w)\mathrm{IC}\_{\mathcal{F}}\leftarrow\text{IC}(F,w)

Return F,w,ICℱF,w,\mathrm{IC}\_{\mathcal{F}}

### B.2 Length control of semantic interpretable alpha factor generator

Following the intuition of grammar-constrained generation (Jin et al., [2018](https://arxiv.org/html/2601.22119v1#bib.bib20 "Unsupervised grammar induction with depth-bounded pcfg")), we introduce a kk-bounded constraint to explicitly limit expression length.
The mechanism maintains a counter k\mathit{k} for the partial length of the expression and enforces a maximum threshold KK. Each production rule has a predefined increment Δ​k\Delta k, representing its contribution to the expression length(see [Table 7](https://arxiv.org/html/2601.22119v1#A1.T7 "In Appendix A Tables ‣ Alpha Discovery via Grammar-Guided Learning and Search") for details). A rule is applied only if
k+Δ​k≤K,\mathit{k}+\Delta k\leq K,
thereby guaranteeing that each expansion step remains within the feasible bound.
By integrating this length-aware constraint into the derivation procedure, we obtain a bounded variant of α\alpha-Sem, denoted as α\alpha-Sem-k.
The procedure is described in [Algorithm 2](https://arxiv.org/html/2601.22119v1#alg2 "In B.2 Length control of semantic interpretable alpha factor generator ‣ Appendix B Algorithms ‣ Alpha Discovery via Grammar-Guided Learning and Search").

Algorithm 2  α\alpha-Sem-kk

Input: Grammar G=(𝒩,𝒯,𝒫,𝒮)G=(\mathcal{N},\mathcal{T},\mathcal{P},\mathcal{S}), maximum length KK, rule increments Δ​k:Γ→β\Delta k:\Gamma\to\beta

Output: Prefix expression tree TT

Initialize TT as a single-node tree with root SS

Set: k←0k\leftarrow 0

while TT contains a nonterminal node do

Let uu be the first nonterminal node in a pre-order traversal of TT

Compute the set of applicable rules:

|  |  |  |
| --- | --- | --- |
|  | 𝒜←{l∈𝒫∣l​ is applicable to ​u​ and ​k+Δ​k​(l)≤K}\mathcal{A}\leftarrow\{l\in\mathcal{P}\mid l\text{ is applicable to }u\text{ and }k+\Delta k(l)\leq K\} |  |

Choose rule l:Γ→βl:\Gamma\to\beta from 𝒜\mathcal{A}

Replace node uu with children corresponding to β\beta

Update: k←k+Δ​k​(l)k\leftarrow k+\Delta k(l)

end while

Return TT

### B.3 Algorithm of Four Stages of MCTS

Algorithm 3  Grammar-aware MCTS with Branch-adapted PUCT

Input: root state sroots\_{\mathrm{root}}, policy-value network fθf\_{\theta}, iteration count II

Output: improved policy π​(a∣sroot)\pi(a\mid s\_{\mathrm{root}})

for i=1i=1 to II do

s←sroots\leftarrow s\_{\mathrm{root}}

Initialize empty list of traversed edges E←[]E\leftarrow[\;]

while ss is not fully expanded do

b←b\leftarrow number of valid actions from ss

a∗←arg⁡maxa⁡[Q​(s,a)+cpuct⋅bbref⋅P​(s,a)⋅∑bN​(s,b)1+N​(s,a)]a^{\*}\leftarrow\arg\max\_{a}\Bigg[Q(s,a)+c\_{\text{puct}}\cdot\sqrt{\tfrac{b}{b\_{\mathrm{ref}}}}\cdot P(s,a)\cdot\tfrac{\sqrt{\sum\_{b}N(s,b)}}{1+N(s,a)}\Bigg]

Append (s,a∗)(s,a^{\*}) to EE

s←apply​(s,a∗)s\leftarrow\text{apply}(s,a^{\*})

end while

sL←ss\_{L}\leftarrow s

(P​(sL,⋅),V​(sL))←fθ​(sL)(P(s\_{L},\cdot),V(s\_{L}))\leftarrow f\_{\theta}(s\_{L})

Expand sLs\_{L} using P​(sL,⋅)P(s\_{L},\cdot)

for all (s,a)∈E(s,a)\in E do

N​(s,a)←N​(s,a)+1N(s,a)\leftarrow N(s,a)+1

Q​(s,a)←1N​(s,a)​∑s′∣s,a→s′V​(s′)Q(s,a)\leftarrow\frac{1}{N(s,a)}\sum\_{s^{\prime}\mid s,a\rightarrow s^{\prime}}V(s^{\prime})

end for

end for

π​(a∣sroot)=N​(sroot,a)1/T∑b∈A​(sroot)N​(sroot,b)1/T\pi(a\mid s\_{\mathrm{root}})=\frac{N(s\_{\mathrm{root}},a)^{1/T}}{\sum\_{b\in A(s\_{\mathrm{root}})}N(s\_{\mathrm{root}},b)^{1/T}}

Return π​(a∣sroot)\pi(a\mid s\_{\mathrm{root}})

Assume that at a certain iteration ii, our MCTS has already explored a portion of the TSL-MDP, denoted by an agent MiM\_{i}. This agent corresponds to a subtree of the large TSL-MDP, sharing the same root, and MiM\_{i} has obtained policy for this partial subtree. For example, at simulation MiM\_{i}, the subtree agent MiM\_{i} shown on the left in [Figure 3](https://arxiv.org/html/2601.22119v1#S4.F3 "In 4.1 Decision-Making on Large Tree ‣ 4 Reinforced Alpha Language Tree Search ‣ Alpha Discovery via Grammar-Guided Learning and Search") has already been explored. This subtree starts as only a root when i=0i=0, and is intended to expand toward the full TSL-MDP tree as ii increases, eventually reaching iteration i=Ii=I.

Selection. First, within MiM\_{i}, starting from root of the subtree, the MCTS agent repeatedly selects an α\alpha-CFG production rule at each incomplete alpha expression (each round-box node), and replaces its leftmost nonterminal symbol (the dark black arrows in [Figure 3](https://arxiv.org/html/2601.22119v1#S4.F3 "In 4.1 Decision-Making on Large Tree ‣ 4 Reinforced Alpha Language Tree Search ‣ Alpha Discovery via Grammar-Guided Learning and Search")), which goes to a new incomplete alpha expression (a child round-box node). This repeats until it reaches a “frontier” alpha expression that has a child not yet included in MiM\_{i} (e.g., node (1) in [Figure 3](https://arxiv.org/html/2601.22119v1#S4.F3 "In 4.1 Decision-Making on Large Tree ‣ 4 Reinforced Alpha Language Tree Search ‣ Alpha Discovery via Grammar-Guided Learning and Search")).

The TSL-MDP has two key features: (1) different nonterminal symbols have different numbers of production rules, and (2) the number of valid production rules decreases sharply near the bottom of the search tree due to the length control in [B.2](https://arxiv.org/html/2601.22119v1#A2.SS2 "B.2 Length control of semantic interpretable alpha factor generator ‣ Appendix B Algorithms ‣ Alpha Discovery via Grammar-Guided Learning and Search"). To address this, we adopt a production rule selection function analogous to PUCT (Silver et al., [2017](https://arxiv.org/html/2601.22119v1#bib.bib5 "Mastering the game of go without human knowledge")).

|  |  |  |  |
| --- | --- | --- | --- |
|  | a∗=arg⁡maxa⁡(Q​(s,a)+cpuct⋅bbref⋅P​(s,a)⋅∑bN​(s,b)1+N​(s,a)),a^{\*}=\arg\max\_{a}\left(Q(s,a)+c\_{\text{puct}}\cdot\sqrt{\tfrac{b}{b\_{\text{ref}}}}\cdot P(s,a)\cdot\frac{\sqrt{\sum\_{b}N(s,b)}}{1+N(s,a)}\right), |  | (8) |

Here, Q​(s,a)Q(s,a) is the value of selecting production rule aa for formula ss, and P​(s,a)P(s,a) is the probability of selecting aa under ss.
bb is the number of branches at the current depth, and brefb\_{\text{ref}} is the branch balance constant (defined by the maximum number of branches)
Eq. ([8](https://arxiv.org/html/2601.22119v1#A2.E8 "Equation 8 ‣ B.3 Algorithm of Four Stages of MCTS ‣ Appendix B Algorithms ‣ Alpha Discovery via Grammar-Guided Learning and Search")) balances irregular branching through the adaptive term b/bref\sqrt{b/b\_{\text{ref}}}: smaller branching factors emphasize exploitation, while larger ones promote broader exploration.

Expansion. After finding such a frontier alpha expression node, the MCTS agent will execute a certain production rule on it, generating a new alpha expression which has not yet been covered by MiM\_{i} (e.g., round-box node (2) in [Figure 3](https://arxiv.org/html/2601.22119v1#S4.F3 "In 4.1 Decision-Making on Large Tree ‣ 4 Reinforced Alpha Language Tree Search ‣ Alpha Discovery via Grammar-Guided Learning and Search")), and also attaching all the corresponding possible production rules to this new alpha expression (e.g., the two arrows attached to node (2)).
The probabilities for executing available production rules for expression ss follow the distribution P​(s)P(s).

Evaluation. Since the newly expanded alpha expression is at the head of the current agent MtM\_{t} and remains incomplete, the existing policy cannot assess its quality. Thus, MCTS requires a method to evaluate it. Given the vastness of the TSL-MDP, traditional simulation-based evaluation is infeasible. Moreover, as shown in [Definition 1](https://arxiv.org/html/2601.22119v1#Thmdefinition1 "Definition 1. ‣ Structural Well-Formedness. ‣ 3.1 Syntactically-Valid Alpha Language ‣ 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search"), the expressions at any state in TSL-MDP are small tree structures (i.e., the small trees inside each round-box in [Figure 3](https://arxiv.org/html/2601.22119v1#S4.F3 "In 4.1 Decision-Making on Large Tree ‣ 4 Reinforced Alpha Language Tree Search ‣ Alpha Discovery via Grammar-Guided Learning and Search")). Therefore, in the next section, we design a Tree-LSTM–based representation learning method to construct a value network for V​(s)V(s), as well as a policy network P​(s,a)P(s,a) over any expression.

Backpropagation. The result V​(s)V(s) of evaluation is backpropagated from the path of selection (the path directed by black arrow in the third tree of [Figure 3](https://arxiv.org/html/2601.22119v1#S4.F3 "In 4.1 Decision-Making on Large Tree ‣ 4 Reinforced Alpha Language Tree Search ‣ Alpha Discovery via Grammar-Guided Learning and Search")). Mean value of each edge in the path is updated by V​(s)V(s) and visit count N​(s,a)N(s,a) of each edge in the path increases by one.

The MCTS agent MiM\_{i} executes the above procedures at each iteration ii ([Algorithm 3](https://arxiv.org/html/2601.22119v1#alg3 "In B.3 Algorithm of Four Stages of MCTS ‣ Appendix B Algorithms ‣ Alpha Discovery via Grammar-Guided Learning and Search") shows the procedure of MCTS search.). Since one node is expanded at each step, the MCTS agent MiM\_{i} will eventually cover enough nodes and edges of the TSL-MDP. The resulting search assigns a basic value to every node and obtain a basic policy for the TSL-MDP, which two can be used to further optimize the policy.

## Appendix C Supplement to Problem Formulation

[Figure 6(a)](https://arxiv.org/html/2601.22119v1#A3.F6.sf1 "In Figure 6 ‣ Appendix C Supplement to Problem Formulation ‣ Alpha Discovery via Grammar-Guided Learning and Search") illustrates the calculation process of an alpha factor. For a period of TT trading days, we compute the alpha factor for each stock using an alpha factor function

|  |  |  |
| --- | --- | --- |
|  | 𝐲t=(yt,1,…,yt,n)∈ℝn,\mathbf{y}\_{t}=(y\_{t,1},\dots,y\_{t,n})\in\mathbb{R}^{n}, |  |

which takes as input the feature data of nn stocks over the current day tt and the previous τ′−1\tau^{\prime}-1 days. The resulting values represent the score of each stock for the current day, i.e., the alpha factor. These alpha values are subsequently used for stock selection and the formulation of trading strategies.

[Figure 6(b)](https://arxiv.org/html/2601.22119v1#A3.F6.sf2 "In Figure 6 ‣ Appendix C Supplement to Problem Formulation ‣ Alpha Discovery via Grammar-Guided Learning and Search") shows an example of formulaic factor: The factor Sum​(Sub​(v​w​a​p,1),2​d)\mathrm{Sum}(\mathrm{Sub}(vwap,1),2d) computes the sum of the most recent two days of VWAP values after subtracting 11 from each.
To obtain the factor value on Wednesday, the operator first evaluates Sub​(v​w​a​p,1)\mathrm{Sub}(vwap,1) for Tuesday and Wednesday and then aggregates them:
(2−1)+(3−1)=3(2-1)+(3-1)=3.
This output serves as the alpha signal, the predicted return for Wednesday which is subsequently used in downstream stock-selection or portfolio-construction procedures.

![Refer to caption](factor-new.png)


(a) Illustration of an alpha factor.

![Refer to caption](cal.png)


(b) An example of a formulaic factor.

Figure 6: Alpha example.

## Appendix D Reinforcement Learning Framework

We present pseudo-code of MCTS combined with reinforcement learning method ([Algorithm 4](https://arxiv.org/html/2601.22119v1#alg4 "In Appendix D Reinforcement Learning Framework ‣ Alpha Discovery via Grammar-Guided Learning and Search")). This is a reinforcement learning-based factor mining method designed to automatically discover a combination of factors from stock market data that can effectively predict stock returns. Specifically, the algorithm initializes a set of factors, their corresponding weights, and a policy-value network. In the process of obtaining data through reinforcement learning, it employs a MCTS policy to generate actions for each state, thereby constructing a multi-step factor generation path. The final state of the path is parsed into a computable alpha expression, evaluated using the I​CℱIC\_{\mathcal{F}} as the reward signal. The reward is given along with the optimization of the factor combination ℱ\mathcal{F}. The actual value for each step along the path, denoted as ztz\_{t} is computed based on I​CℱIC\_{\mathcal{F}} and the similarity between the newly generated factor and existing ones, following the formulation in [Equation 5](https://arxiv.org/html/2601.22119v1#S4.E5 "In 4.3 Syntax Representation Learning ‣ 4 Reinforced Alpha Language Tree Search ‣ Alpha Discovery via Grammar-Guided Learning and Search") in [Section 4.3](https://arxiv.org/html/2601.22119v1#S4.SS3 "4.3 Syntax Representation Learning ‣ 4 Reinforced Alpha Language Tree Search ‣ Alpha Discovery via Grammar-Guided Learning and Search").

After generating multi-step factor paths in each iteration, the policy and value networks are trained using the collected path data (sj,π​(a|sj),zj)(s\_{j},\pi(a|s\_{j}),z\_{j}) stored in a replay buffer, where sjs\_{j} is the state vector encoded by TreeLSTM, π​(a|sj)\pi(a|s\_{j}) is the policy from MCTS, and ztz\_{t} is shown above. After training, the networks are redeployed to guide a new round of search. Through iterative training and exploration, the IC of the learned factor combination is progressively improved. The algorithm outputs the final optimized factor combination set along with its corresponding weights when the IC shows no more significant improvement.

The overall workflow of this algorithm is illustrated in [Figure 7](https://arxiv.org/html/2601.22119v1#A4.F7 "In Appendix D Reinforcement Learning Framework ‣ Alpha Discovery via Grammar-Guided Learning and Search") in the following page, while a specific illustration of its MCTS component [Algorithm 3](https://arxiv.org/html/2601.22119v1#alg3 "In B.3 Algorithm of Four Stages of MCTS ‣ Appendix B Algorithms ‣ Alpha Discovery via Grammar-Guided Learning and Search") is in [Figure 3](https://arxiv.org/html/2601.22119v1#S4.F3 "In 4.1 Decision-Making on Large Tree ‣ 4 Reinforced Alpha Language Tree Search ‣ Alpha Discovery via Grammar-Guided Learning and Search"), and the illustration of its neural network part is in [Figure 3](https://arxiv.org/html/2601.22119v1#S4.F3 "In 4.1 Decision-Making on Large Tree ‣ 4 Reinforced Alpha Language Tree Search ‣ Alpha Discovery via Grammar-Guided Learning and Search") (b).

![Refer to caption](AlphaCFG-4.png)


Figure 7: The overall framework of AlphaCFG.




Algorithm 4  Alpha Mining via Reinforcement Learning

Input: stock trend dataset Y={yt}Y=\{y\_{t}\}

Output: optimal alpha subset F∗F^{\*}, optimal weights w∗w^{\*}

Initialize alpha set FF and weights ww

Initialize policy-value network fθf\_{\theta} and replay buffer DD

for each epoch do

for each factor path search do

Initialize empty trajectory E←[]E\leftarrow[\;]

for j=0j=0 to JJ do

Append state sjs\_{j} to EE

sroot←sjs\_{\mathrm{root}}\leftarrow s\_{j}

π​(a∣sj)←π​(a∣sroot)\pi(a\mid s\_{j})\leftarrow\pi(a\mid s\_{\mathrm{root}})

Sample action aj∼π​(a∣sj)a\_{j}\sim\pi(a\mid s\_{j})

sj+1←apply​(sj,aj)s\_{j+1}\leftarrow\text{apply}(s\_{j},a\_{j})

end for

fj←parse​(sJ)f\_{j}\leftarrow\text{parse}(s\_{J})

Obtain reward ICℱ\mathrm{IC}\_{\mathcal{F}} using [Algorithm 1](https://arxiv.org/html/2601.22119v1#alg1 "In B.1 Linear combination alpha factor algorithm ‣ Appendix B Algorithms ‣ Alpha Discovery via Grammar-Guided Learning and Search")

Reward Assignment

for j=0j=0 to JJ do

z​(sj)←(1−max⁡(0,maxft∈F⁡sim​(ft,fj)))⋅ICℱz(s\_{j})\leftarrow\Bigl(1-\max\bigl(0,\max\_{f\_{t}\in F}\mathrm{sim}(f\_{t},f\_{j})\bigr)\Bigr)\cdot\mathrm{IC}\_{\mathcal{F}}

D←D∪{(sj,π​(a∣sj),z​(sj))}D\leftarrow D\cup\{(s\_{j},\pi(a\mid s\_{j}),z(s\_{j}))\}

end for

end for

Network Update

for each gradient step do

Sample minibatch B⊂DB\subset D

Lθ=(z​(st)−Vθ​(st))2−∑aπ​(a∣st)​log⁡Pθ​(a∣st)+c​‖θ‖2L\_{\theta}=\left(z(s\_{t})-V\_{\theta}(s\_{t})\right)^{2}-\sum\_{a}\pi(a\mid s\_{t})\log P\_{\theta}(a\mid s\_{t})+c\|\theta\|^{2}

θ←θ−η​∇θLθ\theta\leftarrow\theta-\eta\nabla\_{\theta}L\_{\theta}

end for

end for

Return F∗,w∗F^{\*},w^{\*}

## Appendix E Search Space Complexity

To compare the sizes of expression search spaces under different generation methods, we study three methods from a combinatorial perspective:
(i) a purely exponential baseline (arbitrary combination of all symbols corresponding to Σ∗\Sigma^{\*});
(ii) α\alpha-Syn (corresponding to ℒsyn\mathcal{L}\_{\mathrm{syn}});
(iii) α\alpha-Sem (corresponding to ℒsyn\mathcal{L}\_{\mathrm{syn}}).
All three methods share the same parameter sets (operator types, number of features, constants, etc.), but progressively impose stricter constraints, resulting in smaller search spaces.

We set the following notation: the size of the unary operator set is |U||U|, the size of the binary operator set is |B||B|, the size of the asymmetric binary operator set is |Basym||B\_{\text{asym}}|, the size of the rolling operator set is |R||R|, the size of the paired rolling operator set is |Rpair||R\_{\text{pair}}|, the number of features is |ℱ||\mathcal{F}|, the number of constant parameters is |𝒞||\mathcal{C}|, and the number of rolling-window parameters is |𝒩||\mathcal{N}|.

### E.1 Unstructured Space Σ∗\Sigma^{\*}

The method of arbitrary symbol combination (referred to ) takes one symbol equally at each step from all available symbols.
Let the total number of symbols be:

|  |  |  |
| --- | --- | --- |
|  | r=|ℱ|+|𝒞|+|𝒩|+|U|+|B|+|Basym|+|R|+|Rpair|.r=|\mathcal{F}|+|\mathcal{C}|+|\mathcal{N}|+|U|+|B|+|B\_{\text{asym}}|+|R|+|R\_{\text{pair}}|. |  |

Then the number of sequences of length nn is
rn=rn,r\_{n}=r^{n},
and the cumulative size is
∑i≤nri=Θ​(rn).\sum\_{i\leq n}r\_{i}=\Theta(r^{n}).

### E.2 Syntactically Legal Space ℒsyn\mathcal{L}\_{\mathrm{syn}}

We introduce syntax constraints to ensure that generated expressions are all syntactically valid.
We consider the grammar α\alpha-Syn:

|  |  |  |
| --- | --- | --- |
|  | 𝖤𝗑𝗉𝗋→𝖴𝗇𝖺𝗋𝗒𝖮𝗉​(E)​∣𝖡𝗂𝗇𝖺𝗋𝗒𝖮𝗉​(E,E)∣​𝖱𝗈𝗅𝗅𝗂𝗇𝗀𝖮𝗉​(E,E)​∣𝖯𝖺𝗂𝗋𝖾𝖽𝖱𝗈𝗅𝗅𝗂𝗇𝗀𝖮𝗉​(E,E,E)∣​𝖳𝖾𝗋𝗆𝖲𝗒𝖻.\mathsf{Expr}\rightarrow\mathsf{UnaryOp}(E)\mid\mathsf{BinaryOp}(E,E)\mid\mathsf{RollingOp}(E,E)\mid\mathsf{PairedRollingOp}(E,E,E)\mid\mathsf{TermSyb}. |  |

Let hnh\_{n} be the number of valid expressions of length nn.
The terminal set size is:
T=|ℱ|+|𝒞|+|𝒩|.T=|\mathcal{F}|+|\mathcal{C}|+|\mathcal{N}|.

Define operator cardinalities:
U=|U|,Q=|B|+|Basym|,R=|R|,P=|Rpair|U=|U|,Q=|B|+|B\_{\text{asym}}|,R=|R|,P=|R\_{\text{pair}}|, respectively(The meanings of the notations are as shown in D).

The recurrence formula is:
h1=T,h\_{1}=T,
and for n≥2n\geq 2:

|  |  |  |
| --- | --- | --- |
|  | hn=U​hn−1+(Q+R)​∑i=1n−2hi​hn−1−i+P​∑i+j+k=n−1i,j,k≥1hi​hj​hk.h\_{n}=Uh\_{n-1}+(Q+R)\sum\_{i=1}^{n-2}h\_{i}\,h\_{n-1-i}+P\!\!\!\sum\_{\begin{subarray}{c}i+j+k=n-1\\ i,j,k\geq 1\end{subarray}}h\_{i}h\_{j}h\_{k}. |  |

The subsequent derivation of an explicit form from this recurrence becomes rather cumbersome. Since the technical steps mirror the usual treatment of general cubic functional equations, we omit the full derivation here.

### E.3 Semantically Legal Space ℒsem\mathcal{L}\_{\mathrm{sem}}

α\alpha-Sem introduces more constraints on constants, argument types, and rolling windows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤𝗑𝗉𝗋→\displaystyle\mathsf{Expr}\to | 𝖥𝖾𝖺𝗍𝗎𝗋𝖾∣𝖴𝗇𝖺𝗋𝗒𝖮𝗉​(𝖤𝗑𝗉𝗋)\displaystyle\ \mathsf{Feature}\mid\mathsf{UnaryOp}(\mathsf{Expr}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∣𝖡𝗂𝗇𝖺𝗋𝗒𝖮𝗉​(𝖤𝗑𝗉𝗋,𝖤𝗑𝗉𝗋)∣​𝖡𝗂𝗇𝖺𝗋𝗒𝖮𝗉​(𝖤𝗑𝗉𝗋,𝖢𝗈𝗇𝗌𝗍𝖺𝗇𝗍)\displaystyle\mid\mathsf{BinaryOp}(\mathsf{Expr},\mathsf{Expr})\mid\mathsf{BinaryOp}(\mathsf{Expr},\mathsf{Constant}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∣𝖡𝗂𝗇𝖺𝗋𝗒𝖮𝗉​\_​𝖠𝗌𝗒𝗆​(𝖢𝗈𝗇𝗌𝗍𝖺𝗇𝗍,𝖤𝗑𝗉𝗋)∣​𝖱𝗈𝗅𝗅𝗂𝗇𝗀𝖮𝗉​(𝖤𝗑𝗉𝗋,𝖭𝗎𝗆)\displaystyle\mid\mathsf{BinaryOp\\_Asym}(\mathsf{Constant},\mathsf{Expr})\mid\mathsf{RollingOp}(\mathsf{Expr},\mathsf{Num}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∣𝖯𝖺𝗂𝗋𝖾𝖽𝖱𝗈𝗅𝗅𝗂𝗇𝗀𝖮𝗉(𝖤𝗑𝗉𝗋,𝖤𝗑𝗉𝗋,𝖭𝗎𝗆),\displaystyle\mid\mathsf{PairedRollingOp}(\mathsf{Expr},\mathsf{Expr},\mathsf{Num}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖭𝗎𝗆→\displaystyle\mathsf{Num}\to | 20∣⋯,𝖢𝗈𝗇𝗌𝗍𝖺𝗇𝗍→−0.01∣⋯\displaystyle 20\mid\cdots,\qquad\mathsf{Constant}\to-01\mid\cdots |  |

Let fnf\_{n} denotes the number of valid expressions of length nn.

The recurrence formula becomes

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | fn=\displaystyle f\_{n}= | |U|​fn−1\displaystyle|U|\,f\_{n-1} |  | (unary) |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | +|B|​∑i=1n−2fi​fn−1−i\displaystyle+|B|\sum\_{i=1}^{n-2}f\_{i}f\_{n-1-i} |  | (binary) |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | +|B|​|𝒞|​fn−2\displaystyle+|B|\,|\mathcal{C}|\,f\_{n-2} |  | (binary + right constant) |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | +|Basym|​|𝒞|​fn−2\displaystyle+|B\_{\text{asym}}|\,|\mathcal{C}|\,f\_{n-2} |  | (asymmetric binary + left constant) |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | +|R|​|𝒩|​fn−2\displaystyle+|R|\,|\mathcal{N}|\,f\_{n-2} |  | (rolling) |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | +|Rpair|​|𝒩|​∑i=1n−3fi​fn−2−i\displaystyle+|R\_{\text{pair}}|\,|\mathcal{N}|\sum\_{i=1}^{n-3}f\_{i}f\_{n-2-i} |  | (paired rolling).\displaystyle\text{(paired rolling)}. |  |

The recurrence formula is similar, and compared with α\alpha-Syn, recurrence of α\alpha-Sem includes more convolution terms and more realistic constraints, providing a more accurate operator usage. In the following, we present the overall analysis.

Because the expression length is unbounded, the search spaces of all three generation methods are infinite.
Therefore, the comparison does not concern the total size of each space, but rather the size of the finite subspace consisting of expressions whose length is at most nn.

For each grammar, the production rules yield a recurrence for the number of expressions of exact length nn ) ( rn,hn,fnr\_{n},h\_{n},f\_{n}), and accumulating these values from 11 to nn gives the size of the corresponding truncated subspace. By computing these cumulative counts and plotting their growth as functions of nn, we can directly compare how quickly the reachable portions of the three search spaces expand.

### E.4 Empirical Verification

Based on the recurrence formulas, We compute the cumulative counts of {rn}\{r\_{n}\}, {hn}\{h\_{n}\}, and {fn}\{f\_{n}\} for n=1∼n=1\sim NN, and plot their growth curves to visualize differences between the three methods (shown in [Figure 8](https://arxiv.org/html/2601.22119v1#A5.F8 "In E.4 Empirical Verification ‣ Appendix E Search Space Complexity ‣ Alpha Discovery via Grammar-Guided Learning and Search")). Since all three methods yield inherently infinite search spaces, we further design α\alpha-Sem-k based on [Algorithm 2](https://arxiv.org/html/2601.22119v1#alg2 "In B.2 Length control of semantic interpretable alpha factor generator ‣ Appendix B Algorithms ‣ Alpha Discovery via Grammar-Guided Learning and Search"), which can be seen as the red dotted line in [Figure 8](https://arxiv.org/html/2601.22119v1#A5.F8 "In E.4 Empirical Verification ‣ Appendix E Search Space Complexity ‣ Alpha Discovery via Grammar-Guided Learning and Search"). The results are consistent with the analysis in [Figure 1](https://arxiv.org/html/2601.22119v1#S3.F1 "In 3 Design Language of Interpretable Alphas ‣ Alpha Discovery via Grammar-Guided Learning and Search"), which further strengthens the superiority of our approach in theory.

[Figure 8](https://arxiv.org/html/2601.22119v1#A5.F8 "In E.4 Empirical Verification ‣ Appendix E Search Space Complexity ‣ Alpha Discovery via Grammar-Guided Learning and Search") explains the core of the superiority of our method: By introducing constraints of syntax and semantics, We get an infinite set containing only valid factors. In actual factor search tasks, we cannot exhaust this space that exploring a finite subset is realistic. Therefore, We utilize the recursive feature of CFG and further designed α\alpha-Sem-k capable of generating factors of only a finite length. Ultimately, we reduced the complexity of the search space from an exponential level to a constant level, making this task solvable.

![Refer to caption](x4.png)


Figure 8: Comparison of cumulative search space sizes of different grammar levels.

## Appendix F Details of Tree-LSTM

Starting from ASR leaf nodes, the Tree-LSTM recursively aggregates child hidden and cell states through gating (input, forget, output), combining them with the node’s input embedding. This bottom-up process continues until the root, yielding a fixed-dimensional state vector that encodes both the syntax and operator-specific dependencies of the entire expression. Thus, the Tree-LSTM transforms variable-sized trees into single vectors while preserving structural and semantic information.

In our α\alpha-CFG, operators are different: (i) symmetric operators, where order is irrelevant, and (ii)asymmetrical (order-sensitive) operators, where order must be preserved.
Tree-LSTM naturally supports both cases through two variants: the N-ary Tree-LSTM, which uses position-sensitive parameters to encode child order, and the Child-Sum Tree-LSTM, which aggregates child states by their mean to provide order-invariant representations.
Based on these, we tailor aggregation strategies: for symmetric binary operators (𝖤𝗑𝗉𝗋→𝖡𝗂𝗇𝖺𝗋𝗒𝖮𝗉​(𝖤𝗑𝗉𝗋,𝖤𝗑𝗉𝗋)\mathsf{Expr}\to\mathsf{BinaryOp}(\mathsf{Expr},\mathsf{Expr})) we adopt Child-Sum to avoid redundant encodings; for paired rolling operators (𝖤𝗑𝗉𝗋→𝖯𝖺𝗂𝗋𝖾𝖽𝖱𝗈𝗅𝗅𝗂𝗇𝗀𝖮𝗉​(𝖤𝗑𝗉𝗋,𝖤𝗑𝗉𝗋,𝖭𝗎𝗆)\mathsf{Expr}\to\mathsf{PairedRollingOp}(\mathsf{Expr},\mathsf{Expr},\mathsf{Num})) we first apply unordered aggregation to operands and then use N-ary encoding to incorporate the time-window parameter; and for all other operators we employ standard N-ary encoding. Such operation can address the problem of isomorphic redundancy of alpha factors defined in [Definition 6](https://arxiv.org/html/2601.22119v1#Thmdefinition6 "Definition 6 (Isomorphism of ASR(Tree)). ‣ Appendix G Calculation of Tree Similarity ‣ Alpha Discovery via Grammar-Guided Learning and Search").The resulting tree embeddings are treated as input to be given into the policy and value heads to predict next-rule probabilities and estimated state value.

### F.1 N-ary Tree-LSTM (Position-Sensitive)

Let node jj have NN children with hidden states 𝐡1,…,𝐡N\mathbf{h}\_{1},\dots,\mathbf{h}\_{N}, input 𝐱j\mathbf{x}\_{j}, output hidden state 𝐡j\mathbf{h}\_{j} and cell state 𝐜j\mathbf{c}\_{j}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐢j\displaystyle\mathbf{i}\_{j} | =σ​(W(i)​𝐱j+∑k=1NUk(i)​𝐡k+𝐛(i))\displaystyle=\sigma\left(W^{(i)}\mathbf{x}\_{j}+\sum\_{k=1}^{N}U\_{k}^{(i)}\mathbf{h}\_{k}+\mathbf{b}^{(i)}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐟j​k\displaystyle\mathbf{f}\_{jk} | =σ​(W(f)​𝐱j+Uk(f)​𝐡k+𝐛(f)),k=1,…,N\displaystyle=\sigma\left(W^{(f)}\mathbf{x}\_{j}+U\_{k}^{(f)}\mathbf{h}\_{k}+\mathbf{b}^{(f)}\right),\qquad k=1,\dots,N |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐨j\displaystyle\mathbf{o}\_{j} | =σ​(W(o)​𝐱j+∑k=1NUk(o)​𝐡k+𝐛(o))\displaystyle=\sigma\left(W^{(o)}\mathbf{x}\_{j}+\sum\_{k=1}^{N}U\_{k}^{(o)}\mathbf{h}\_{k}+\mathbf{b}^{(o)}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐮j\displaystyle\mathbf{u}\_{j} | =tanh⁡(W(u)​𝐱j+∑k=1NUk(u)​𝐡k+𝐛(u))\displaystyle=\tanh\left(W^{(u)}\mathbf{x}\_{j}+\sum\_{k=1}^{N}U\_{k}^{(u)}\mathbf{h}\_{k}+\mathbf{b}^{(u)}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐜j\displaystyle\mathbf{c}\_{j} | =𝐢j⊙𝐮j+∑k=1N𝐟j​k⊙𝐜k\displaystyle=\mathbf{i}\_{j}\odot\mathbf{u}\_{j}+\sum\_{k=1}^{N}\mathbf{f}\_{jk}\odot\mathbf{c}\_{k} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐡j\displaystyle\mathbf{h}\_{j} | =𝐨j⊙tanh⁡(𝐜j)\displaystyle=\mathbf{o}\_{j}\odot\tanh(\mathbf{c}\_{j}) |  |

### F.2 Child-Sum Tree-LSTM

Let node jj have a set of children C​(j)C(j) with hidden states 𝐡k\mathbf{h}\_{k}, k∈C​(j)k\in C(j):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐡~j\displaystyle\tilde{\mathbf{h}}\_{j} | =1|C​(j)|​∑k∈C​(j)𝐡k\displaystyle=\frac{1}{|C(j)|}\sum\_{k\in C(j)}\mathbf{h}\_{k} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐢j\displaystyle\mathbf{i}\_{j} | =σ​(W(i)​𝐱j+U(i)​𝐡~j+𝐛(i))\displaystyle=\sigma\left(W^{(i)}\mathbf{x}\_{j}+U^{(i)}\tilde{\mathbf{h}}\_{j}+\mathbf{b}^{(i)}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐟j​k\displaystyle\mathbf{f}\_{jk} | =σ​(W(f)​𝐱j+U(f)​𝐡k+𝐛(f)),k∈C​(j)\displaystyle=\sigma\left(W^{(f)}\mathbf{x}\_{j}+U^{(f)}\mathbf{h}\_{k}+\mathbf{b}^{(f)}\right),\quad k\in C(j) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐨j\displaystyle\mathbf{o}\_{j} | =σ​(W(o)​𝐱j+U(o)​𝐡~j+𝐛(o))\displaystyle=\sigma\left(W^{(o)}\mathbf{x}\_{j}+U^{(o)}\tilde{\mathbf{h}}\_{j}+\mathbf{b}^{(o)}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐮j\displaystyle\mathbf{u}\_{j} | =tanh⁡(W(u)​𝐱j+U(u)​𝐡~j+𝐛(u))\displaystyle=\tanh\left(W^{(u)}\mathbf{x}\_{j}+U^{(u)}\tilde{\mathbf{h}}\_{j}+\mathbf{b}^{(u)}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐜j\displaystyle\mathbf{c}\_{j} | =𝐢j⊙𝐮j+∑k∈C​(j)𝐟j​k⊙𝐜k\displaystyle=\mathbf{i}\_{j}\odot\mathbf{u}\_{j}+\sum\_{k\in C(j)}\mathbf{f}\_{jk}\odot\mathbf{c}\_{k} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐡j\displaystyle\mathbf{h}\_{j} | =𝐨j⊙tanh⁡(𝐜j)\displaystyle=\mathbf{o}\_{j}\odot\tanh(\mathbf{c}\_{j}) |  |

## Appendix G Calculation of Tree Similarity

###### Definition 6 (Isomorphism of ASR(Tree)).

ASR T1T\_{1} and T2T\_{2} are isomorphic only if:

1. 1.

   The label of root nodes must be the same;
2. 2.

   Recursively check each child node, the labels of the child nodes are equivalent: for asymmetrical operations, the order of the subtrees must be preserved; for symmetrical operations (Binary type operators in [Table 6](https://arxiv.org/html/2601.22119v1#A1.T6 "In Appendix A Tables ‣ Alpha Discovery via Grammar-Guided Learning and Search")) or partially symmetrical operations (Corr, Cov, where the order of the first two operands’ child nodes doesn’t matter), the order of the subtrees doesn’t matter as long as the operands match;
3. 3.

   Recursively check that all child nodes and their structures are isomorphic.

Given two alpha factor expresions(partial or completed), they correspond to two ASRs T1T\_{1} and T2T\_{2} which are also two trees. Let Sub​(T)\text{Sub}(T) denote the set of all subtrees of TT, where each subtree is induced by a child of node in TT along with all its descendant nodes (including the child node itself). Let N​(T)N(T) denote the total number of subtrees in TT, recursively defined as:

|  |  |  |
| --- | --- | --- |
|  | N​(T)=1+∑c∈Children​(T)N​(c).N(T)=1+\sum\_{c\in\text{Children}(T)}N(c). |  |

The normalized similarity between the two ASR is defined as:

|  |  |  |
| --- | --- | --- |
|  | sim​(T1,T2)=maxt1∈Sub​(T1)t2∈Sub​(T2)⁡css​(t1,t2)max⁡(N​(T1),N​(T2)),\mathrm{sim}(T\_{1},T\_{2})=\frac{\max\_{\begin{subarray}{c}t\_{1}\in\text{Sub}(T\_{1})\\ t\_{2}\in\text{Sub}(T\_{2})\end{subarray}}\mathrm{css}(t\_{1},t\_{2})}{\max\left(N(T\_{1}),\;N(T\_{2})\right)}, |  |

where the numerator represents the size of the largest isomorphic subtree shared by T1T\_{1} and T2T\_{2}, i.e., the number of matching nodes in the largest common subtree. Tree isomorphism is defined formally in  [Definition 6](https://arxiv.org/html/2601.22119v1#Thmdefinition6 "Definition 6 (Isomorphism of ASR(Tree)). ‣ Appendix G Calculation of Tree Similarity ‣ Alpha Discovery via Grammar-Guided Learning and Search"). If no such isomorphic subtree exists, then css​(t1,t2)=0\mathrm{css}(t\_{1},t\_{2})=0.

The denominator max⁡(N​(T1),N​(T2))\max(N(T\_{1}),N(T\_{2})) corresponds to the number of nodes in the larger of the two trees, serving as an upper bound for the size of any common subtree. Intuitively, it reflects the maximum number of matching nodes that could be achieved if one tree were a subtree of the other, or if the two trees were structurally identical. As such, the denominator defines the *maximum potential scale* of a common subtree, and serves to normalize the matching node count in the numerator. This ensures that the resulting similarity score lies within the standardized range [0,1][0,1], thereby facilitating both quantitative analysis and intuitive comparison of structural similarity between expression trees.

## Appendix H AlphaCFG Framework Parameter Setting for Experiment

### H.1 MCTS Parameters

* •

  Exploration Parameter : The exploration-exploitation trade-off parameter in the UCT formula is set to c=1c=1.
* •

  MCTS Simulations : 64 simulations are performed per state.
* •

  MCTS Parallelism: 8 parallel simulations are used to speed up the exploration.
* •

  Eval Batch Size: 2 evaluations using network are carried out simultaneously each time.
* •

  Branch balance coefficient: 40

### H.2 Network Architecture

Feature Extractor (Tree-LSTM):

* •

  Embedding Dimension: 128.
* •

  Hidden Size: 128.
* •

  Dropout Rate: 0.1.

Policy Network:

* •

  Input: Features extracted by the feature extractor (Tree-LSTM).
* •

  Hidden Layers:

  + –

    Layer 1: Fully connected layer with 128 input features and 64 output features.
  + –

    Layer 2: Fully connected layer with 64 input features and 128 output features (embedding dimension).
* •

  Activation Function: Softmax

Value Network:

* •

  Input: Features extracted by the feature extractor (Tree-LSTM).
* •

  Hidden Layers:

  + –

    Layer 1: Fully connected layer with the embedding dimension (128) as input and 64 output features.
  + –

    Layer 2: Fully connected layer with 64 input features and 64 output features.
* •

  Activation Functions: ReLU activation functions applied to the hidden layers.
* •

  Output: A fully connected layer with a single output value without activation function.

### H.3 Optimizer and Training Parameters

* •

  Optimizer: Adam optimizer with default settings
* •

  Learning Rate: A learning rate of 10−410^{-4}.
* •

  Batch Size: 64.
* •

  Number of factor trajectories in an iteration: 100(2\*50).
* •

  Training Iterations: 100 iterations.
* •

  Batch Size for Training: 64.
* •

  Replay Buffer Size: 20,000.
* •

  Early Stopping Criteria: Early stopping based on validation performance, with a threshold of 20% iterations without improvement.

## Appendix I More Results of Experiment

We evaluate the proposed framework on both the China A-share and U.S. equity markets. Our experiments are designed to: (1) demonstrate that the proposed context-free grammar provides practical advantages over linear generation methods (e.g., Reverse Polish Notation) for representing and generating alpha factors; (2) validate that the syntax representation learning method using Tree-LSTM to encode state outperforms linear network architectures; (3) evaluate the performance of the grammar-aware discovery framework across multiple metrics in comparison with existing factor-mining methods; (4) assess whether the alpha factors discovered by our model deliver superior trading performance in realistic backtesting scenarios; and (5) examine how our model enhances the performance of existing classical factors.

### I.1 Data

For the A-share market, we adopt the constituent stocks of the CSI 300 index, and for the U.S. market, we use the constituent stocks of the S&P 500 index. The dataset is temporally partitioned into three subsets: the training set (2010-01-01 to 2017-12-31), the validation set (2018-01-01 to 2019-12-31), and the testing set (2021-01-01 to 2024-12-31). To avoid distortions caused by abnormal market volatility and structural irregularities during the COVID-19 pandemic, data from calendar year 2020 are excluded by design. Six raw stock-level features are used as model inputs: {open,close,high,low,volume,vwap}\{\mathrm{open},\;\mathrm{close},\;\mathrm{high},\;\mathrm{low},\;\mathrm{volume},\;\mathrm{vwap}\}. Formulaic alpha factors are constructed by applying arithmetic operators to these base features under the grammar constraints described earlier. The prediction target for factors is the 20-day forward return, computed using closing prices for both buying and selling, i.e., Rt(20)=Ref​(close,−20)close−1R\_{t}^{(20)}=\frac{\mathrm{Ref}(\mathrm{close},\,-20)}{\mathrm{close}}-1.

### I.2 Comparison Methods

We evaluate three variants of grammar-constrained factor discovery method: (i) α\alpha-Syn (generation constrained solely by syntactic rules) (ii) α\alpha-Sem (generation constrained by both syntactic and semantic rules) (iii) α\alpha-Sem-kk (generation further restricted by a length-bounding mechanism in [Algorithm 2](https://arxiv.org/html/2601.22119v1#alg2 "In B.2 Length control of semantic interpretable alpha factor generator ‣ Appendix B Algorithms ‣ Alpha Discovery via Grammar-Guided Learning and Search")). To further validate the grammar effectiveness, we also incorporate Reverse Polish Notation (RPN).
(Specifically for α\alpha-Syn, we constrain the rolling window size to be an integer constant in α\alpha-Syn to facilitate smooth training.)

For a broader performance assessment of the entire framework, we compare our method against two state-of-the-art factor mining baselines: AlphaGen (Yu et al., [2023](https://arxiv.org/html/2601.22119v1#bib.bib30 "Generating synergistic formulaic alpha collections via reinforcement learning")) and AlphaQCM (Zhu and Zhu, [2025](https://arxiv.org/html/2601.22119v1#bib.bib29 "AlphaQCM: alpha discovery in finance with distributional reinforcement learning")). Both employ RPN, with AlphaGen using Proximal Policy Optimization (PPO) and AlphaQCM using distributed reinforcement learning. Additionally, GPlearn (Zhang et al., [2020](https://arxiv.org/html/2601.22119v1#bib.bib3 "Autoalpha: an efficient hierarchical evolutionary algorithm for mining alpha factors in quantitative investment")) is included as a symbolic-regression baseline, which generates formula trees through genetic programming. All of the above factor generation methods optimize the Information Coefficient (IC) of the linear combination of factors.

To further validate our approach, we include several widely used machine learning models as additional baselines: XGBoost (Wang et al., [2023](https://arxiv.org/html/2601.22119v1#bib.bib42 "An xgboost-based multivariate deep learning framework for stock index futures price forecasting")), LightGBM (Bisdoulis, [2024](https://arxiv.org/html/2601.22119v1#bib.bib41 "Assets forecasting with feature engineering and transformation methods for lightgbm")), LSTM (Bhandari et al., [2022](https://arxiv.org/html/2601.22119v1#bib.bib43 "Predicting stock market index using lstm")), ALSTM (Qin et al., [2017](https://arxiv.org/html/2601.22119v1#bib.bib44 "A dual-stage attention-based recurrent neural network for time series prediction")), TCN (Dai et al., [2022](https://arxiv.org/html/2601.22119v1#bib.bib45 "Price change prediction of ultra high frequency financial data based on temporal convolutional network")), and Transformer (Mozaffari and Zhang, [2024](https://arxiv.org/html/2601.22119v1#bib.bib46 "Predictive modeling of stock prices using transformer model")).The hyperparameters of these models are set according to the benchmark configurations provided by Qlib (Yang et al., [2020](https://arxiv.org/html/2601.22119v1#bib.bib23 "Qlib: an ai-oriented quantitative investment platform")). To mitigate the impact of randomness, all models are trained and evaluated 5 times with different fixed random seeds.

### I.3 Evaluation Metrics

We evaluate factor effectiveness from two complementary perspectives: correlation metrics, including IC, RankIC, ICIR, and RankICIR, capture the statistical relationship between factors and future returns.
Backtesting metrics, which are obtained by investment simulation using a top-k/drop-n strategy (see the next paragraph for details ), including MaxDD and Sharpe, assess the profitability and risk characteristics of factors in simulated trading (see [Table 8](https://arxiv.org/html/2601.22119v1#A9.T8 "In I.3 Evaluation Metrics ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search") for details).

Top-kk/drop-nn strategy is applied to simulate actual trading operations: for each trading day, we first ranked stocks based on their factor prediction scores, then selected the top kk stocks from the sorted list.
To balance return potential and trading costs, we adopted an equal-weight allocation approach while limiting daily portfolio adjustments to a maximum of n stocks.
In our experiment, we set k=60k=60 and n=5n=5, ensuring sufficient portfolio diversification while controlling transaction costs.

[Table 8](https://arxiv.org/html/2601.22119v1#A9.T8 "In I.3 Evaluation Metrics ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search") provides the specific calculation methods for all evaluation metrics.

Table 8: Summary of Evaluation Metrics

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Category | Metric Name | Abbrev. | Formula | Description |
| Correlation Metrics | Information Coefficient | IC | IC=ρ​(αi,Ri)\mathrm{IC}=\rho(\alpha\_{i},R\_{i}) | Pearson correlation between factor values αi\alpha\_{i} and future returns RiR\_{i}. |
|  | Rank Information Coefficient | RankIC | RankIC=ρ​(r​(αi),r​(Ri))\mathrm{RankIC}=\rho(r(\alpha\_{i}),r(R\_{i})) | Spearman correlation after ranking; r​(⋅)r(\cdot) is the rank function. |
|  | Information Ratio | ICIR | ICIR=IC¯σIC\mathrm{ICIR}=\dfrac{\overline{\mathrm{IC}}}{\sigma\_{\mathrm{IC}}} | Ratio of mean IC to its volatility, measuring prediction stability. |
|  | Rank Information Ratio | RankICIR | RankICIR=RankIC¯σRankIC\mathrm{RankICIR}=\dfrac{\overline{\mathrm{RankIC}}}{\sigma\_{\mathrm{RankIC}}} | Ratio of mean RankIC to its volatility, evaluating rank correlation stability. |
| Backtesting Metrics | Maximum Drawdown | MaxDD | MaxDD=maxt⁡Pmax​(0,t)−PtPmax​(0,t)\mathrm{MaxDD}=\max\_{t}\dfrac{P\_{\max}(0,t)-P\_{t}}{P\_{\max}(0,t)} | Largest peak-to-trough decline in backtest; PtP\_{t} is NAV, Pmax​(0,t)=maxs≤t⁡PsP\_{\max}(0,t)=\max\_{s\leq t}P\_{s}. |
|  | Sharpe Ratio | Sharpe | Sharpe=𝔼​[rp−rf]σrp×N\mathrm{Sharpe}=\dfrac{\mathbb{E}[r\_{p}-r\_{f}]}{\sigma\_{r\_{p}}}\times\sqrt{N} | Annualized excess return per unit risk; rpr\_{p}: daily return, rfr\_{f}: risk-free rate, NN: 252 (trading days). |

### I.4 Comparison of Different Network Architectures

We conducted comparative experiments under different network architectures (Transformer, LSTM, CNN) while keeping other conditions constant. With a pool size of 10 and max length 5, [Figure 9](https://arxiv.org/html/2601.22119v1#A9.F9 "In I.4 Comparison of Different Network Architectures ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search") shows training IC across epochs. Results demonstrate the effectiveness and superiority of syntax representation learning. Tree-LSTM not only extracts the structural and semantic information of expressions but also reduces redundancy caused by isomorphic forms ([Definition 6](https://arxiv.org/html/2601.22119v1#Thmdefinition6 "Definition 6 (Isomorphism of ASR(Tree)). ‣ Appendix G Calculation of Tree Similarity ‣ Alpha Discovery via Grammar-Guided Learning and Search")).

![Refer to caption](x5.png)


Figure 9: Comparison of training curves of different network architectures.

### I.5 Optimization of Combined Factor Parameters on the Validation Set

To obtain the optimized combined factor parameters, we conducted experiments on the validation set for two dimensions: Maximum Length of Individual Factors (Max Length) and Factor Pool Size (Pool Size) (results shown in [Figure 10](https://arxiv.org/html/2601.22119v1#A9.F10 "In I.5 Optimization of Combined Factor Parameters on the Validation Set ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search")). Specifically, we first fix the maximum length of individual factors and then evaluate the valid IC for different pool sizes {1, 5, 10, 20, 30} to select the optimal pool size. After selecting the optimal pool size under α\alpha-Sem-kk, we fix it and then explore different values of the maximum length of individual factors {5, 10, 15, 20, 25} to identify the best configuration.

![Refer to caption](x6.png)


Figure 10:  Valid IC of various generation approaches.

Finally, we obtain the best combined factor parameters:

CSI 300:

* •

  RPN+MCTS: Max Length: 10; Pool Size: 20
* •

  α\alpha-Syn: Max Length: 10; Pool Size: 20
* •

  α\alpha-Sem: Max Length: 10; Pool Size: 10
* •

  α\alpha-Sem-kk: Max Length: 10; Pool Size: 10
* •

  RPN+PPO: Max Length: 20; Pool Size: 20

S&P 500:

* •

  RPN+MCTS: Max Length: 20; Pool Size: 20
* •

  α\alpha-Syn: Max Length: 10; Pool Size: 20
* •

  α\alpha-Sem: Max Length: 10; Pool Size: 20
* •

  α\alpha-Sem-kk: Max Length: 10; Pool Size: 20
* •

  RPN+PPO: Max Length: 20; Pool Size: 20

The optimization objective of the GP method using a combined model has little effect (the generated combined factors are highly similar), so only the single-factor IC is used as its optimization objective.

### I.6 Case Study of the interpretability of formulaic factors

[Table 9](https://arxiv.org/html/2601.22119v1#A9.T9 "In I.6 Case Study of the interpretability of formulaic factors ‣ Appendix I More Results of Experiment ‣ Alpha Discovery via Grammar-Guided Learning and Search") shows an example of alpha factors generated by our framework, tested on the CSI 300 index constituents.
The mined factors exhibit strong interpretability grounded in market microstructure theory. For example, the factor Log(|Std((0.05-volume),40)|) measures the volatility of inverse trading volume over a 40-day window. This factor gauges the temporal variability of illiquidity, which may signal market stress or substantial price impact. Another example, Cov(volume,vwap,40), captures the co-movement between trading volume and the volume-weighted average price in past 40 days. A high covariance indicates strong directional consensus, potentially reflecting persistent momentum or, conversely, price reversals.

Table 9: Top 10 Ranked Alphas and Their Weights

#
Alpha Expression
Weight


1
Mean(Corr(Sum(open,40),(high-volume),20),20)
-0.00889

2
volume
-0.01278

3
Std(close,40)
0.01778

4
Pow(Med(Cov(high,low,30),30),0.1)
0.01411

5
Delta(Log(|Min(high,30)/0.01|),30)
-0.01649

6
Cov((-0.1-Sum(close,40)),volume,20)+low
-0.01649

7
0.01Greater(-0.1/Corr(high,close,30),volume)
-0.00823

8
Log(|Std((0.05-volume),40)|)
0.01224

9
Greater(-0.01,Log(|Log(|low|)|))
-0.04616

10
Cov(volume,vwap,40)
-0.01412