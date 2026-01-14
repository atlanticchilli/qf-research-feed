---
authors:
- Yichen Luo
- Yebo Feng
- Jiahua Xu
- Yang Liu
doc_id: arxiv:2601.08641v1
family_id: arxiv:2601.08641
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach
  with Chain-of-Thought Reasoning'
url_abs: http://arxiv.org/abs/2601.08641v1
url_html: https://arxiv.org/html/2601.08641v1
venue: arXiv q-fin
version: 1
year: 2026
---


Yichen Luo
University College LondonLondonUnited Kingdom
[yichen.luo.22@ucl.ac.uk](mailto:yichen.luo.22@ucl.ac.uk)
, 
Yebo Feng
Nanyang Technological UniversitySingapore
[yebo.feng@ntu.edu.sg](mailto:yebo.feng@ntu.edu.sg)
, 
Jiahua Xu
University College LondonExponential Science FoundationLondonUnited Kingdom
[jiahua.xu@ucl.ac.uk](mailto:jiahua.xu@ucl.ac.uk)
 and 
Yang Liu
Nanyang Technological UniversitySingapore
[yangliu@ntu.edu.sg](mailto:yangliu@ntu.edu.sg)

(2018)

###### Abstract.

The launch of $Trump coin ignited a wave in meme coin investment. Copy trading, as a strategy-agnostic approach that eliminates the need for deep trading knowledge, quickly gains widespread popularity in the meme coin market. However, copy trading is not a guarantee of profitability due to the prevalence of manipulative bots, the uncertainty of the followed wallets’ future performance, and the lag in trade execution. Recently, large language models have shown promise in financial applications by effectively understanding multi-modal data and producing explainable decisions. However, a single LLM struggles with complex, multi-faceted tasks such as asset allocation. These challenges are even more pronounced in cryptocurrency markets, where LLMs often lack sufficient domain-specific knowledge in their training data.

To address these challenges, we propose an explainable multi-agent system for meme coin copy trading. Inspired by the structure of an asset management team, our system decomposes the complex task into subtasks and coordinates specialized agents to solve them collaboratively. Employing few-shot chain-of-thought (CoT) prompting, each agent acquires professional meme coin trading knowledge, interprets multi-modal data, and generates explainable decisions. Using a dataset of 1,000 meme coin projects’ transaction data, our empirical evaluation shows that the proposed multi-agent system outperforms both traditional machine learning models and single LLMs, achieving 73% and 70% precision in identifying high-quality meme coin projects and key opinion leader (KOL) wallets, respectively. The selected KOLs collectively generated a total profit of $500,000 across these projects.

††copyright: acmlicensed††journalyear: 2018††doi: XXXXXXX.XXXXXXX††conference: Make sure to enter the correct
conference title from your rights confirmation email; June 03–05,
2018; Woodstock, NY††isbn: 978-1-4503-XXXX-X/2018/06

## 1. Introduction

While manipulative tactics such as rat trading are well-trodden ruses in traditional financial markets, these old-fashioned ploys have now become bot-driven and prey on naïve copy traders in a new hunting ground: the memecoin market.

The launch of $TRUMP memecoin by U.S. President Trump on January 17, 2025, ignited a surge of speculation in the memecoin market, drawing millions of traders to the memecoin market. However, many of these entrants lack prior trading experience. To lower the barrier to participation, memecoin-tracking platforms such as GMGN introduced copy trading, an automated, one-click feature that allows users to replicate other wallets. In practice, copiers attempt to identify so-called key opinion leader wallets—addresses perceived to possess insider knowledge, trading expertise, and consistent profitability—and replicate their trades. As a strategy-agnostic approach, copy trading eliminates the need for in-depth market knowledge and has rapidly become the most popular strategy among inexperienced memecoin traders.

However, copy trading is neither risk-free nor a guaranteed path to profit. Copiers face several challenges, most notably the prevalence of various manipulative bots that can conceal their positions, snipe trades, engage in wash trading, and falsify social media signals. Another major challenge lies in selecting the right key opinion leader wallet. Some key opinion leaders featured on tracking platforms may exploit their influence by buying meme coins early at low prices, prompting copiers to follow and inflate the price, then exiting at a profit—using copiers as exit liquidity. In such cases, copiers may end up buying high and selling low, resulting in losses. Another challenge is performance persistence: key opinion leaders who were successful in the past may underperform as market dynamics shift, particularly with the rise of new manipulative trading bots. Moreover, meme coin values are typically driven by hype and vulnerable to pump-and-dump schemes, meaning even skilled key opinion leaders can suffer loss. To maximize returns, copiers should be selective, targeting meme coins with higher upward potential and longer life expectancy.

The emergence of large language models has transformed the financial sector, offering powerful tools for meme investment. Numerous studies have highlighted the strong capability of large language models to process and learn from multi-modal data (Yin et al., [2024](https://arxiv.org/html/2601.08641v1#bib.bib17)), including text (Yang et al., [2024](https://arxiv.org/html/2601.08641v1#bib.bib16); Li et al., [2023b](https://arxiv.org/html/2601.08641v1#bib.bib8)) and images (Zhang et al., [2024](https://arxiv.org/html/2601.08641v1#bib.bib18)), making them well-suited for analyzing meme coin markets and evaluating key opinion leader performance across various data types. In addition, their natural language generation capabilities (Wei et al., [2022](https://arxiv.org/html/2601.08641v1#bib.bib13); Liu et al., [2023a](https://arxiv.org/html/2601.08641v1#bib.bib9)) enable them to produce explainable investment decisions. However, the performance of standalone large language models in financial tasks remains limited, due to the complexity and reasoning demands of the domain (Xie et al., [2023](https://arxiv.org/html/2601.08641v1#bib.bib15); Li et al., [2023a](https://arxiv.org/html/2601.08641v1#bib.bib6)). These limitations are even more pronounced in meme coin markets, where domain-specific training data is scarce. To address this, recent research has proposed decomposing complex tasks into subtasks handled by multiple specialized large language model-based agents (Wu et al., [2023](https://arxiv.org/html/2601.08641v1#bib.bib14); Pan et al., [2024](https://arxiv.org/html/2601.08641v1#bib.bib12)). Inspired by human cognitive processes, this multi-agent approach enhances reasoning and problem-solving by enabling collaboration among agents, each focusing on a specific aspect of the task. While some studies have explored such agent-based systems in stock or high-cap cryptocurrency markets (Ding et al., [2024](https://arxiv.org/html/2601.08641v1#bib.bib2); Fatemi and Hu, [2024](https://arxiv.org/html/2601.08641v1#bib.bib3); Li et al., [2024](https://arxiv.org/html/2601.08641v1#bib.bib7)), no prior work has applied them to meme coin investment.

To address these challenges and fill the gap, we propose an explainable, multi-modal, multi-agent framework for meme coin copy trading. Inspired by task specialization in hedge funds, the framework decomposes the trading process into four subtasks—meme coin evaluation, trader assessment, wealth management, and order execution—each handled by a dedicated agent.

The meme evaluation agent identifies meme coins with strong growth potential and long-term viability. The trader evaluation agent selects key opinion leader wallets based on their historical trading performance. The trader evaluation agent selects key opinion leader wallets based on historical trading performance. The meme evaluation agent identifies high-potential, long-lived meme coins using candlestick patterns, trading metrics, and comment sentiment. The wealth management agent allocates capital across copy trading opportunities, while the order execution agent is responsible for submitting buy orders on Pumpfun. Finally, the order execution agent is responsible for submitting buy orders on PumpFun.

To demonstrate the effectiveness of our framework, we use the data of 4,000 meme coin projects to evaluate the performance of our multi-agent model. Our framework not only outperforms single large language model but also produce economically significant profits. The main contribution of this paper is summarized as:

* •

  We are the first to propose an algorithm for detecting manipulative bots. Using the signals generated by this algorithm, even the traditional machine learning models demonstrate predictive power in identifying key opinion leaders.
* •

  We are the first to propose a systematic framework for meme coin copy trading. Our framework outperforms not only traditional machine learning models but also single large language models in both key opinion leader and high-quality meme selection by integrating multimodal data, generating economically significant profits.
* •

  Inspired by the decision-making processes of professional meme coin traders, we implement chain-of-thought prompting for each agent to facilitate learning of expert-level strategies for evaluating meme coins and traders and ensure the explainability.
* •

  Our multi-agent model integrates multi-modal financial data—including text and visual information—into the decision-making process, enabling a more comprehensive understanding of market dynamics and enhancing overall performance.

## 2. Related Works

This section reviews prior work on using single large language models and multi-agent frameworks in investment tasks. Owing to their strong language understanding and reasoning abilities, large language models have been widely adopted for financial applications. Early efforts centered on employing single large language models to forecast asset prices and implement investment strategies. Some studies developed domain-specific financial large language models through fine-tuning (Xie et al., [2023](https://arxiv.org/html/2601.08641v1#bib.bib15); Liu et al., [2023b](https://arxiv.org/html/2601.08641v1#bib.bib10); Li et al., [2023a](https://arxiv.org/html/2601.08641v1#bib.bib6)), while others evaluated large language model performance in trading cryptocurrencies such as Bitcoin, Ethereum, and Solana (Li et al., [2024](https://arxiv.org/html/2601.08641v1#bib.bib7)). However, even fine-tuned single-agent models often yield limited predictive power and exhibit significant bias.

To address these shortcomings, recent research has turned to multi-agent systems. For example, the Summarize-Explain-Predict (SEP) framework uses a reflective agent that iteratively generates forecasts and explanations with support from auxiliary agents (Koa et al., [2024](https://arxiv.org/html/2601.08641v1#bib.bib4)). Other studies leverage multiple agents to handle data processing, summarization, reflection, and prediction tasks (Kou et al., [2024](https://arxiv.org/html/2601.08641v1#bib.bib5); Fatemi and Hu, [2024](https://arxiv.org/html/2601.08641v1#bib.bib3); Ding et al., [2024](https://arxiv.org/html/2601.08641v1#bib.bib2)). Luo et al. ([2025](https://arxiv.org/html/2601.08641v1#bib.bib11)) introduce a multi-agent large language model-based system for managing large-cap cryptocurrency portfolios. Despite these advancements, there is limited work on multi-agent, multi-modal models tailored to low-cap cryptocurrency investment. To bridge this gap, we propose a specialized multi-agent framework where distinct agents process different modalities and collaborate to invest in a universe of emerging cryptocurrencies.

## 3. Background

In this section, we introduce the concept of meme coin, Pumpfun’s business model, key players, and market manipulation dynamic on that platform.

### 3.1. Meme Coin and Pump.fun

![Refer to caption](x1.png)


Figure 1. Bonding curve mechanism. Red solid line describes the relationship between the total SOL deposited by traders and the total meme coins received. From this, the price of the meme coin in terms of SOL can also be derived (blue solid line). Blue and red dotted lines are the initial price and migration price. x′x^{\prime} and y′y^{\prime} are 30 and 1,073,000,191, respectively

A meme coin is a cryptocurrency that originates from internet memes, typically characterized by low liquidity and volatile price driven by community hype, social media trends, and celebrity endorsements. Pump.fun, the largest meme coin crowdfunding platform on Solana, lets users create meme coins for free.

First, users can upload an image and select a name and ticker, and Pumpfun will use this information to create a new token (so-called meme coin) via a standard smart contract on blockchain with a total supply of 1 billion. Immediately afterward, the creator can choose whether to purchase the token at the lowest available price. Of the total supply, 800 million tokens are made available for trading, while 200 million remain locked. This is similar to the Initial Public Offerings application stage in the stock market, but with no extremely simple prospectus and no regulatory approval.

Next, the meme coin enters the “launching stage”. It will be displayed on Pumpfun’s front page and open to subscription. At this stage, the creator and other traders could buy or sell 800 million meme coins at a designated price from or to the contract. The bonding curve mechanism, introduced in the next subsection, sets the price. This stage is similar to the primary market, where traders trade with the issuer. Two trivial differences between the meme coin launch stage and the stock Initial Public Offerings are:
(1) traders can withdraw the subscription at any point at this stage; and 
(2) the subscription price and withdrawal price are variable based on the bonding curve mechanism instead of being fixed.

After 800 meme coins are purchased (subscribed), the meme coin project automatically enters the next stage, which is called “migration”. Migration means the meme coin project receives sufficient subscription and will be listed on a decentralized exchange so that traders can trade with other traders (i.e., the secondary market). At this stage, the trading on decentralized exchange is nothing essentially different from the trading on a stock exchange.

Besides the financial market functions, Pumpfun provides social platform functions. Any user with a Solana wallet can comment on any coin, similar to StockTwit. Each trade bumps the coin’s name to the front page with a brief jiggle. The platform also flags potential bot activity and displays meme coin holding details.

### 3.2. Bonding Curve Mechanism

For the launch stage of a meme coin project, traders can subscribe to the meme coin using SOL, Solana’s native cryptocurrency, paying a 1% transaction fee and following the bonding curve mechanism. This mechanism defines the relationship between the total SOL deposited and the total meme coins received, given by:

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | y=y′−kx+x′,y=y^{\prime}-\frac{k}{x+x^{\prime}}, |  |

where xx is the amount of SOL deposited, and yy is the corresponding number of meme coins received. The parameters x′x^{\prime} and y′y^{\prime} represent the virtual reserves of SOL and meme coins, respectively, and are constants set by Pump.fun. Here, k=x′​y′k=x^{\prime}y^{\prime} is their constant product.
Based on Equation 1, we can derive the relationship between the price of meme coin and the SOL deposited as follows:

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | P=d​xd​y=−(x+x′)2k,P=\frac{dx}{dy}=-\frac{(x+x^{\prime})^{2}}{k}, |  |

where pp is the price of the meme coin in terms of SOL.
The bonding curve mechanism ensures prices rise with increased demand. In [Figure 10](https://arxiv.org/html/2601.08641v1#S8.F10 "Figure 10 ‣ 8.1. Meme evaluation agent ‣ 8. Framework Overview ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning"), we illustrate the relationship between the total SOL paid and the total meme coins received and the price of meme coins expressed in SOL. Once all 800 million meme coins are purchased, it will be listed on a decentralized exchange and the locked 200 million meme coins are migrated, a process known as “migration” or “graduation”.

### 3.3. Meme Coin Trading Actors

The meme coin ecosystem studied in this paper involves a diverse set of participants, each playing a distinct role in the lifecycle of a meme coin. We identify six key types of players:

#### 3.3.1. Pumpfun

Pumpfun is the most prominent meme coin launchpad at the time this paper is written. It allows anyone with a Solana wallet to create and trade meme coins in a standard way. Pumpfun’s business model involves charging a 1% fee on each buy or sell transaction, as well as a 0.015 SOL migration fee deducted from the liquidity pool.

#### 3.3.2. decentralized exchange

After a meme coin reaches its migration threshold on Pumpfun, it is migrated to a DEX, Raydium, for secondary market trading. The DEX relies on Automatic Market Maker for liquidity provision and meme coin pricing.

#### 3.3.3. Meme Coin Creator

The creator is the user who initiates a meme coin by uploading metadata and deploying the smart contract via Pumpfun. Creators can profit from early token purchases at low prices, and some employ bots to conceal their ownership, inflate trading volume, or manipulate sentiment. Thus, creators often act as both originators and strategic manipulators within the system.

#### 3.3.4. Traders

Traders are market participants who buy and sell meme coins either during the Pumpfun launch stage or on the DEX after migration. They can be affected by both transparent and hidden manipulative activity, and their profitability varies depending on timing and bot presence.

#### 3.3.5. Bot providers

Bot providers develop and rent or sell automated scripts to actors—typically creators or traders—who wish to manipulate market dynamics, as shown in [Figure 3](https://arxiv.org/html/2601.08641v1#S3.F3 "Figure 3 ‣ 3.4. Rug Pull and Manipulation Bots ‣ 3. Background ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning"). These bots include bundle bots (to hide ownership), volume bots (to simulate liquidity), and comment bots (to fabricate community sentiment). Bot providers commoditize manipulation and lower the cost of executing deceptive strategies, contributing to the industrialization of wash trading in meme coin markets.

### 3.4. Rug Pull and Manipulation Bots

![Refer to caption](x2.png)


(a) Naive Bundle.

![Refer to caption](x3.png)


(b) Bundle Bot.

![Refer to caption](x4.png)


(c) Sniper Bot.

![Refer to caption](x5.png)


(d) Gradual Bundle.

Figure 2. Heuristics for meme coin price impact from bots



![Refer to caption](Figures/bot.png)

Figure 3. Illustration of pump.fun bots.



![Refer to caption](x6.png)


(a) Launch bundle.

![Refer to caption](x7.png)


(b) Buy bundle.

![Refer to caption](x8.png)


(c) Creator-funded buy bundle.

![Refer to caption](x9.png)


(d) Sell bundle.

Figure 4. Heuristics for candlestick price impact.

While a meme coin migration generally indicates it has attracted sufficient trader attention and achieved higher trading volume and liquidity, this pattern does not always reflect genuine market confidence. In practice, malicious actors can exploit migration by orchestrating rug pulls or deploying wash trading bots to manufacture an illusion of interest and liquidity. Understanding these manipulative practices is essential to avoid being misled by inflated transaction data, as we explore next.

The speculative nature of meme coins makes them highly susceptible to rug pulls—sudden exit scams where the meme coin creator and early participants cash out and abandon the project. To make the scam appear organic, actors often deploy multiple fake wallets to simulate active trading and widespread interest while concealing their own positions, as illustrated in [Figure 3](https://arxiv.org/html/2601.08641v1#S3.F3 "Figure 3 ‣ 3.4. Rug Pull and Manipulation Bots ‣ 3. Background ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning"). This fabricated activity attracts new buyers, enabling early actors to profit. Typically, three types of automated scripts or bots are used: bundle bots, volume bots, and comment bots. These scripts control multiple wallets to execute coordinated transactions.

#### 3.4.1. Bundle Bot

A launch bundle bot is utilized when a creator launches a meme coin. During a launch on platforms like Pumpfun, the creator can purchase the meme coin at the lowest price based on a bonding curve mechanism, thereby driving up the price by subscribing to more tokens. However, these transactions, including the creator’s holdings, are publicly visible on the Pumpfun dashboard. If the creator engages in heavy purchasing to inflate the price, it may signal concentrated ownership to other traders, deterring them from investing due to fears of a rug pull.

To counteract this visibility, the launch bundle bot enables the creator to generate, fund, and control multiple wallets, which simultaneously buy the meme coin during the same creation block. This masks centralized ownership and creates an illusion of organic demand. This technique is analogous to *concealed ownership* strategies in stock markets, where traders may split their orders across multiple accounts or brokers to obscure their intentions. However, Pumpfun flags transactions occurring within the same block as potential bot activity, making this approach easily detectable. Moreover, only the coin creator can insert transactions into the creation block, further exposing such behavior as suspicious. We illustrate the heuristics of bundle bots in [Figure 4](https://arxiv.org/html/2601.08641v1#S3.F4 "Figure 4 ‣ 3.4. Rug Pull and Manipulation Bots ‣ 3. Background ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning").

#### 3.4.2. Bump Bot

![Refer to caption](x10.png)


Figure 5. Heuristic for the bump bot.

On Pumpfun, each transaction updates a token’s displayed attributes—such as its name, price, and recent trading activity—on the platform’s front page, thereby enhancing its visibility and attracting attention from potential traders. Token creators may exploit this mechanism by deploying bumpbots that repeatedly execute offsetting buy and sell orders. These artificial transactions do not alter actual holdings but instead create the illusion of heightened trading interest, inflating the token’s perceived popularity. We illustrate the heuristic of the bump bot in [Figure 5](https://arxiv.org/html/2601.08641v1#S3.F5 "Figure 5 ‣ 3.4.2. Bump Bot ‣ 3.4. Rug Pull and Manipulation Bots ‣ 3. Background ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning").

#### 3.4.3. Comment Bot

A Comment Bot is an automated script designed to fabricate user engagement by generating fake comments that simulate community interest and enthusiasm around a meme coin. Operating through multiple controlled wallets, the bot disseminates brief, context-free, and easily replicable positive messages. These comments typically lack substantive information yet are crafted to convey an impression of widespread support and social validation, using phrases such as “To the moon!”, “Don’t miss out!”, or “Huge potential here!”. The primary objective is to mislead genuine users into perceiving strong community backing, thereby encouraging investment under the false assumption of popular traction.

## 4. A Meme Coin Case Study

![Refer to caption](x11.png)


Figure 6. The impact of manipulative bots on the life cycle of a meme coin: a case study of MAO. A timeline highlights key events, which are mapped to the corresponding candlestick segments (framed by color boxes). These candlesticks are then linked to the underlying on-chain transaction and comment histories.

To investigate how manipulative bots influence the lifecycle of a meme coin, we present a case study in [Figure 6](https://arxiv.org/html/2601.08641v1#S4.F6 "Figure 6 ‣ 4. A Meme Coin Case Study ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning"). We select [MAO](https://pump.fun/coin/2F84uaBysP4sD7Qby33fAM9RrSzhcR9KWrUT1ixwpump) as a presentative example because it exhibits all four types of bots discussed in [subsection 3.4](https://arxiv.org/html/2601.08641v1#S3.SS4 "3.4. Rug Pull and Manipulation Bots ‣ 3. Background ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning"). While not all meme coins feature every type of bot, this case illustrates their mechanisms and clarifies how bots shape the lifecycle of a meme coin. For simplicity, wallet addresses are abbreviated to their first five characters.

### 4.1. Token Creation and Launch Bundle

At 15:06:24 on January 17, 2025, in block 314596960, token creator wallet 7xA7A created meme coin MAO, marked as stage 1 on the timeline in [Figure 6](https://arxiv.org/html/2601.08641v1#S4.F6 "Figure 6 ‣ 4. A Meme Coin Case Study ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning"). Within the same block, the creator employs an automated script to generate multiple fresh wallets (e.g., 712nX, 6fYzn, and 4hZpo) and purchase MAO, as shown by the red box in the left-hand transaction history panel in [Figure 6](https://arxiv.org/html/2601.08641v1#S4.F6 "Figure 6 ‣ 4. A Meme Coin Case Study ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning"). This behavior exemplifies the launch bundle described in [subsubsection 3.4.1](https://arxiv.org/html/2601.08641v1#S3.SS4.SSS1 "3.4.1. Bundle Bot ‣ 3.4. Rug Pull and Manipulation Bots ‣ 3. Background ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning"), whereby newly created wallets fabricate trading activity, artificially inflate the coin price, and conceal the creator’s true position.

### 4.2. Sniper Bot Front-Running

Only four blocks and one second after the launch, the sniper wallet EW6Dk front-ran all other retail traders and purchased the meme coin (orange box and stage 2). This automated sniper bot secured a relatively low entry price through its speed advantage while slightly inflating the coin’s price.

### 4.3. Comment and Bump Bot

From 15:10:17 to 16:26:42, comment bots disseminated fabricated positive messages (blue box and stage 3), such as “SENDOOR”, a term suggesting that the meme coin would accumulate sufficient market capitalization to migrate. This behavior created the illusion of active community communication and lured uninformed traders to participate. Between 15:37:36 and 16:40:45, the bump bot 4h7Lk.. repeatedly bought and sold the same amount of MAO (purple box and stage 4). Each transaction was bumped to the front page of Pumpfun, thereby attracting additional users.

### 4.4. Rug Pull

At 16:40:54, the creator and associated launch bundles began selling their holdings with a significant profit, causing the meme coin’s price to drop sharply within a minute (red box and stage 5). The sniper then detected this movement and exited its position with a moderate profit (orange box and stage 5). Ultimately, most retail traders closed their holdings with a loss.

We also visualize the two key performance metrics for meme coin projects:
(1) The vertical dashed gray line indicates the maximum return, defined as the return between the initial price and the peak price. 
(2) The horizontal dashed gray line denotes dump duration, measured as the time in seconds from the peak time to the point where the price falls to 10% of its peak price.

## 5. Analyzing Meme Coin Bot Activity

![Refer to caption](x12.png)


(a) Launch Bundle.

![Refer to caption](x13.png)


(b) Sniper Bot.

![Refer to caption](x14.png)


(c) Bump Bot.

![Refer to caption](x15.png)


(d) Comment Bot.

Figure 7. Distribution of performance metrics for meme coin projects with and without specific bots. The dashed line represents the mean of the distribution.

[Figure 7](https://arxiv.org/html/2601.08641v1#S5.F7 "Figure 7 ‣ 5. Analyzing Meme Coin Bot Activity ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning") presents the distribution of two performance metrics, maximum return and dump duration, for meme coin projects with and without specific bots. Projects with a launch bundle tend to exhibit slightly higher maximum returns but shorter dump duration on average. This can be attributed to the launch bundle concealing the creator’s holdings and fabricating demand, attracting more traders. However, given the malicious nature of launch bundles, creators often use them to dump the coin quickly to make profits, shortening the dump period. Most projects have sniper bots, and performance differences between those with and without sniper bots are negligible. Projects with comment bots and bump bots display significant increases in both performance metrics. This is intuitive, as bump bots push the coin to Pumpfun’s front page for greater trader exposure, while comment bots fabricate the appearance of an active community to attract traders.

![Refer to caption](x16.png)


Figure 8. Profit distributions for a KOL/bump bot/sniper bot ([CcS..1K3](https://solscan.io/account/CcSVw6PGY655z9ava7pQhSkckmBL7rtkrjPGRVK5z1K3)), a noise trader ([E9D..pWn](https://solscan.io/account/E9D2wrgjfhbaopWjgkiwX4o9eVFjLQhUiCr5SBiZMpWn)), and an underperforming trader/bump bot ([J8J..cd1](https://solscan.io/account/J8JSA7BGKmauruAD8A7fWwwz9UoPvbEKPksW1WDsqcd1)). The dashed line indicates the mean profit across all memecoin projects in which each trader participated. The light shading shows the Gaussian kernel density estimates of project-level trading profits, while the darker shading marks the 99% tt-confidence interval for the mean profit of each trader.

## 6. Methodology

![Refer to caption](x17.png)


Figure 9. The workflow of LLM-powered multi-agent system for meme coin copy trading.

In this section, we first decompose the meme coin copy trading process into a series of subtasks and formalize each component. We then introduce our proposed multi-agent meme coin copy trading framework, illustrated in [Figure 9](https://arxiv.org/html/2601.08641v1#S6.F9 "Figure 9 ‣ 6. Methodology ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning"). This framework allows multiple agents to learn from few-shot chain-of-thought prompting and make explainable decisions across wallet selection and meme coin selection.

## 7. Problem Formulation

### 7.1. Meme coin selection

We first evaluate meme coin project performance using transaction indicators, candlestick charts, and user comments. Given a vector of meme coin transaction indicators 𝜶t−1=[αi,t−1]m×1\bm{\alpha}\_{t-1}=[\alpha\_{i,t-1}]\_{m\times 1}, where mm is the total number of transaction indicators, and candlestick chart vt−1v\_{t-1}, and a vector of comments 𝐜t−1=[ci,t−1]n×1\mathbf{c}\_{t-1}=[c\_{i,t-1}]\_{n\times 1}, where nn is the total number of comments, our goal is to classify and select meme coin ii with above-average log return, which is defined as rt,t+j=log⁡(pt+jpt)r\_{t,t+j}=\log(\frac{p\_{t+j}}{p\_{t}}), where pt+jp\_{t+j} is the price when migration and pt+jp\_{t+j} is the price in jj minutes.

### 7.2. Wallet selection

We then identify trader wallets with consistent profitability and low-frequency trading behavior (referred to as key opinion leader). Given a vector of trader-specific transaction indicators 𝜷t−1=[βi,t−1]m×1\bm{\beta}\_{t-1}=[\beta\_{i,t-1}]\_{m\times 1}, where mm is the total number of trader-specific transaction indicators, we need to classify and select traders with the positive profit Πj\Pi\_{j} on a specific meme coin jj.

## 8. Framework Overview

In this paper, we propose an explainable multi-agent framework for meme coin copy trading, as illustrated in [Figure 9](https://arxiv.org/html/2601.08641v1#S6.F9 "Figure 9 ‣ 6. Methodology ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning"). The framework consists of four agents: the trader evaluation agent, wealth agent, meme evaluation agent, and DEX agent. The trader evaluation agent selects wallets with consistent profitability and low-frequency trading behavior. The wealth agent manages fund allocation to follow the selected key opinion leader wallets. The meme evaluation agent identifies high-potential, long-lived meme coins using multi-modal data such as transaction metrics, candlestick charts, and user comments. The decentralized exchange agent is responsible for the execution of the trading. Each agent is trained with meme coin trading knowledge and domain-specific reasoning via few-shot chain-of-thought prompting.

### 8.1. Meme evaluation agent

Algorithm 1  Bundle Bot Detection Algorithm

1: Input: Meme coin address AA and on-chain data DD

2: Output: Bundle bot dictionary RR

3: Extract the transaction list TT of meme coin AA from DD

4: Extract the launch block BlaunchB\_{\text{launch}} of meme coin AA

5: Initialize 𝐵𝑢𝑛𝑑𝑙𝑒𝑠←defaultdict​(list){\it Bundles}\leftarrow\text{defaultdict}(\text{list})

6: for all txn∈T\textit{txn}\in T do

7:  𝐵𝑢𝑛𝑑𝑙𝑒𝑠​[txn.block]←𝐵𝑢𝑛𝑑𝑙𝑒𝑠​[txn.block]+[txn]{\it Bundles}[\textit{txn.block}]\leftarrow{\it Bundles}[\textit{txn.block}]+[\textit{txn}]

8: end for

9: Initialize R←defaultdict​(int){\it R}\leftarrow\text{defaultdict}(\text{int})

10: for all (b,txns)∈𝐵𝑢𝑛𝑑𝑙𝑒𝑠(b,\textit{txns})\in{\it Bundles} do

11:  if b=Blaunchb=B\_{\text{launch}} and transfer exists between creator and txn makers then

12:   R​["Launch Bundle"]←1R[\texttt{"Launch Bundle"}]\leftarrow 1

13:  end if

14:  if b≠Blaunchb\neq B\_{\text{launch}} and all txns are buy orders then

15:   R​["Buy Bundle"]←1R[\texttt{"Buy Bundle"}]\leftarrow 1

16:   if transfer exists between creator and txn makers then

17:    R​["Creator-Funded Buy Bundle"]←1R[\texttt{"Creator-Funded Buy Bundle"}]\leftarrow 1

18:   end if

19:  end if

20:  if b≠Blaunchb\neq B\_{\text{launch}} and all txns are sell orders then

21:   R​["Sell Bundle"]←1R[\texttt{"Sell Bundle"}]\leftarrow 1

22:  end if

23: end for

24: return RR



![Refer to caption](Figures/candle_good.png)


(a) Meme coin project with good farming opportunity.

![Refer to caption](Figures/candle_poor.png)


(b) Meme coin project with poor farming opportunity.

Figure 10. Pre-migration candlestick chart.

To address the meme coin selection problem, we introduce the meme evaluation agent. Using few-shot chain-of-thought prompting, the agent learns expert knowledge to identify meme coins with strong farming potential—those likely to exhibit sustained upside in the future. We structure the agent’s reasoning along three key dimensions.

First, the agent evaluates transaction-level metrics to assess farming potential. Strong opportunities are typically characterized by the absence of creator-funded bundles, moderately sized buy and sell bundles, the existence of the bump bot, and high trading activity, as reflected in longer pre-migration durations, a greater number of unique traders, and higher transaction volumes.

Building on the bundle bot heuristics in [Figure 4](https://arxiv.org/html/2601.08641v1#S3.F4 "Figure 4 ‣ 3.4. Rug Pull and Manipulation Bots ‣ 3. Background ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning"), we propose an algorithm to detect their presence, as illustrated in Algorithm 1. The algorithm extracts the launch block and transaction history of a meme coin from on-chain data, aggregates transactions occurring in the same block into bundles, and classifies each bundle according to the following rules:
(1) bundles in the launch block involving transfers between the creator and transaction makers are identified as creator-funded bundles; 
(2) bundles outside the launch block containing only buy orders are labeled as buy bundles; 
(3) bundles outside the launch block with only buy orders and creator-to-trader transfers are classified as creator-funded buy bundles; and 
(4) bundles outside the launch block containing only sell orders are defined as sell bundles.

However, the algorithm does not capture all possible cases of creator-funded launch or buy bundles, as the creator may channel funds indirectly through intermediary wallets or centralized exchange. The agent then examines the meme coin’s candlestick chart to identify potential bundle bot activities. Projects with weak farming prospects often exhibit charts with a few large green candles, suggesting that early participants opened sizable positions to dump after migration (see [10(b)](https://arxiv.org/html/2601.08641v1#S8.F10.sf2 "10(b) ‣ Figure 10 ‣ 8.1. Meme evaluation agent ‣ 8. Framework Overview ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning")). In contrast, promising projects typically show a healthy pre-migration phase with multiple price fluctuations, reflecting active and organic trading (see [10(a)](https://arxiv.org/html/2601.08641v1#S8.F10.sf1 "10(a) ‣ Figure 10 ‣ 8.1. Meme evaluation agent ‣ 8. Framework Overview ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning")).

To detect the presence of a bump bot, we propose the algorithm described in Algorithm 2, building on the heuristic illustrated in [Figure 5](https://arxiv.org/html/2601.08641v1#S3.F5 "Figure 5 ‣ 3.4.2. Bump Bot ‣ 3.4. Rug Pull and Manipulation Bots ‣ 3. Background ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning"). We define a wash trading score for each meme coin trader, calculated as the ratio of the number of matched buy–sell transaction pairs of identical amounts to the trader’s net position. This metric captures the characteristic behavior of wash trading bots, which repeatedly execute offsetting trades without materially changing their overall holdings. A meme coin is classified as having a wash trading bot if at least one trader exhibits a wash trading score exceeding the predefined threshold cc (set to 50 in this study).

Algorithm 2  Bump Bot Detection Algorithm

1: Input: Meme coin address AA and on-chain data DD

2: Output: Boolean indicating presence of a bump bot

3: Extract the transaction list TT of meme coin AA from DD

4: Initialize 𝑇𝑟𝑎𝑑𝑒𝑟𝑠←defaultdict​(list){\it Traders}\leftarrow\text{defaultdict}(\text{list})

5: for all txn∈T\textit{txn}\in T do

6:  𝑇𝑟𝑎𝑑𝑒𝑟𝑠​[txn.trader]←𝑇𝑟𝑎𝑑𝑒𝑟𝑠​[txn.trader]+[txn]{\it Traders}[\textit{txn.trader}]\leftarrow{\it Traders}[\textit{txn.trader}]+[\textit{txn}]

7: end for

8: for all (𝑡𝑟𝑎𝑑𝑒𝑟,𝑡𝑥𝑛𝑠)∈𝑇𝑟𝑎𝑑𝑒𝑟𝑠({\it trader},{\it txns})\in{\it Traders} do

9:  Initialize 𝐹𝑙𝑖𝑝𝑠←0{\it Flips}\leftarrow 0

10:  Initialize 𝑃𝑜𝑠𝑖𝑡𝑖𝑜𝑛←1{\it Position}\leftarrow 1

11:  for i=1i=1 to |𝑡𝑥𝑛𝑠|−1|{\it txns}|-1 do

12:   𝑃𝑜𝑠𝑖𝑡𝑖𝑜𝑛←𝑃𝑜𝑠𝑖𝑡𝑖𝑜𝑛+𝑡𝑥𝑛𝑠​[i].amount{\it Position}\leftarrow{\it Position}+{\it txns}[i].\text{amount}

13:   if 𝑡𝑥𝑛𝑠​[i+1]{\it txns}[i+1] has the reverse transaction type and same amount as 𝑡𝑥𝑛𝑠​[i]{\it txns}[i] then

14:    𝐹𝑙𝑖𝑝𝑠←𝐹𝑙𝑖𝑝𝑠+1{\it Flips}\leftarrow{\it Flips}+1

15:   end if

16:  end for

17:  if 𝐹𝑙𝑖𝑝𝑠𝑃𝑜𝑠𝑖𝑡𝑖𝑜𝑛≥c\frac{{\it Flips}}{{\it Position}}\geq c then

18:   return True

19:  end if

20: end for

21: return False

Next, the agent assesses the sentiment of comments. Strong farming potential is often relevant to the participants of non-bot positive comments. Finally, the agent outputs a binary judgment, yes or no, on whether the project offers good farming potential. System instructions, prompts, and few-shot chain-of-thought examples are provided in the appendix.

### 8.2. Wallet evaluation agent

To address the wallet selection problem, we introduce a wallet evaluation agent. Employing few-shot chain-of-thought prompting, the agent learns to identify key opinion leader wallets—those with infrequent but consistently profitable trades. Its reasoning is based on three trader metrics: profitability (Total Profit, Total Profit Std), trading frequency (Total Average Transaction Number, Total Average Transaction Std), and trading experience (Total Average Transaction Number). The agent outputs a binary decision indicating whether a wallet qualifies as a key opinion leader. Details of system instructions, prompts, and few-shot chain-of-thought examples for the wallet evaluation agent are included in the appendix.

### 8.3. Wealth and DEX agent

The wealth agent is responsible for managing cash allocation in the copy-trading process. Based on the current wallet balance, it determines whether executing a copy trade is feasible and optimal. The decentralized exchange agent handles trade execution, interfacing directly with the decentralized exchange smart contract to perform transactions efficiently and reliably.

Table 1. Features included in the prediction model.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Feature | Notation | Description | Prediction Model Inclusion | | |
| Rule | ML | Agents |
| (Average) Return | R¯[x]\bar{R}\_{[x]}† | The average return across the previous [x][x] paricipated memecoins.† | ● | ● | ● |
| Number of Trades | #​T​r​a​d​e\#Trade | The total number of trades executed across all participated memecoins. | ● | ● | ● |
| Return Standard Deviation | s​t​dstd | The standard deviation of returns across all participated memecoins. | ○ | ● | ● |
| tt-stat | tt | The tt-statistic of the trader’s mean return across all participated memecoins. | ○ | ● | ● |
| Time Since Last Trade | T𝐿𝑎𝑠𝑡T\_{\it Last} | The seconds elapsed since the most recent trade before the current memecoin. | ○ | ● | ● |
| Time Since First Trade | T𝐹𝑖𝑟𝑠𝑡T\_{\it First} | The seconds elapsed since the trader’s very first trade. | ○ | ● | ● |
| Bot | [y][y] Bot‡ | A dummy variable equal to one if [y][y] bot is detected, and 0 otherwise.‡ | ○ | ● | ● |
| Candlestick | 𝐶𝑎𝑛𝑑𝑙𝑒𝑠𝑡𝑖𝑐𝑘\it Candlestick | The candlestick chart of the memecoin when the trader makes the first trade. | ○ | ○ | ● |
| Comments | 𝐶𝑜𝑚𝑚𝑒𝑛𝑡𝑠\it Comments | The comments of the memecoin when the trader makes the first trade. | ○ | ○ | ● |
| x†∈{all,1th,1th-5th,6th-10th,11th-15th}{}^{\dagger}x\in\{\text{all},\text{1th},\text{1th-5th},\text{6th-10th},\text{11th-15th}\}. | | | | | |
| y‡∈{Bundle, Sniper, Bump}{}^{\ddagger}y\in\{\text{Bundle, Sniper, Bump}\}. | | | | | |

## 9. Experiment

![Refer to caption](x18.png)


(a) Precision and F1 Scores.

![Refer to caption](x19.png)


(b) ROC Curves.

Figure 11. Model performance on the test set measured by Precision, F1F\_{1}, and ROC AUC at different threshold levels.

In this section, we discuss the experiment settings and evaluate the performance of our multi-agent system for meme coin copy trading.

### 9.1. Experiment Settings

We utilize transaction and transfer data sourced from Flipside, which maintains archive nodes with fully indexed access to Solana’s historical data. In particular, we gather the contract address, launch time and block, migration time and block, and the creator’s wallet address for the first 1,000 meme coins that migrated from Pump.fun to a DEX following the launch of $TRUMP on 2025-01-17 at 14:01:48. For each of these coins, we extract their transaction and transfer records from their initial launch up to 12 hours after migration. Transaction data includes the block number, timestamp, trader address, transaction type (buy/sell), meme token amount, SOL amount, and USD equivalent. Transfer data includes the block number, timestamp, sender, receiver, and the amount of tokens transferred.

### 9.2. Performance of Meme Evaluation Agent

Table 2. Performance of the meme evaluation agent using chain-of-thought prompting with data from different modalities across various post-migration intervals.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Agent | Interval | Accuracy | Precision | Recall | F1 Score |
| Transaction | 1 Min | 0.5358 | 0.5944 | 0.2253 | 0.3267 |
| 5 Mins | 0.5674 | 0.6778 | 0.2568 | 0.3725 |
| 10 Mins | 0.5821 | 0.7167 | 0.2716 | 0.3939 |
| 30 Mins | 0.5968 | 0.7556 | 0.2863 | 0.4153 |
| 1 Hour | 0.5926 | 0.7444 | 0.2821 | 0.4092 |
| 5 Hours | 0.5758 | 0.7000 | 0.2653 | 0.3847 |
| 10 Hours | 0.5653 | 0.6722 | 0.2547 | 0.3695 |
| Technical | 1 Min | 0.4870 | 0.4817 | 0.3420 | 0.4000 |
| 5 Mins | 0.5410 | 0.5577 | 0.3960 | 0.4632 |
| 10 Mins | 0.5630 | 0.5887 | 0.4180 | 0.4889 |
| 30 Mins | 0.5770 | 0.6085 | 0.4320 | 0.5053 |
| 1 Hour | 0.5790 | 0.6113 | 0.4340 | 0.5076 |
| 5 Hours | 0.5470 | 0.5662 | 0.4020 | 0.4702 |
| 10 Hours | 0.5330 | 0.5465 | 0.3880 | 0.4538 |
| Comment | 1 Min | 0.4900 | 0.4107 | 0.0460 | 0.0827 |
| 5 Mins | 0.5140 | 0.6250 | 0.0700 | 0.1259 |
| 10 Mins | 0.5180 | 0.6607 | 0.0740 | 0.1331 |
| 30 Mins | 0.5340 | 0.8036 | 0.0900 | 0.1619 |
| 1 Hour | 0.5300 | 0.7679 | 0.0860 | 0.1547 |
| 5 Hours | 0.5180 | 0.6607 | 0.0740 | 0.1331 |
| 10 Hours | 0.5200 | 0.6786 | 0.0760 | 0.1367 |
| All | 1 Min | 0.5800 | 0.6092 | 0.4463 | 0.5152 |
| 5 Mins | 0.6263 | 0.6724 | 0.4926 | 0.5687 |
| 10 Mins | 0.6347 | 0.6839 | 0.5011 | 0.5784 |
| 30 Mins | 0.6621 | 0.7213 | 0.5284 | 0.6100 |
| 1 Hour | 0.6705 | 0.7328 | 0.5368 | 0.6197 |
| 5 Hours | 0.6558 | 0.7126 | 0.5221 | 0.6027 |
| 10 Hours | 0.6389 | 0.6897 | 0.5053 | 0.5832 |

First, we assess the performance of the meme evaluation agent. Since some data sources may be noisy or less informative, we also report the performance of agents using each data modality individually. [Figure 5](https://arxiv.org/html/2601.08641v1#S3.F5 "Figure 5 ‣ 3.4.2. Bump Bot ‣ 3.4. Rug Pull and Manipulation Bots ‣ 3. Background ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning") shows the results of the meme evaluation agent with chain-of-thought prompting across different data types. The agent using transaction data achieves high precision and fair accuracy but low recall and F1 score, indicating a conservative approach that may overlook profitable farming opportunities. Precision rises from 1 to 30 minutes and then declines from 30 minutes to 10 hours, suggesting the strongest predictive power around the 30-minute mark. Agents relying on technical or comment data show similar patterns: high precision and fair accuracy but low recall and F1 score, again reflecting an overly conservative stance. In contrast, the agent combining all data sources achieves strong accuracy, precision, recall, and F1 score, effectively filtering out poor opportunities while capturing a wide range of promising ones. Its performance also remains stable across various post-migration intervals.

### 9.3. Performance of Wallet Evaluation Agent

Table 3. Performance of the wallet evaluation agent using chain-of-thought prompting. “TRUE” indicates that the wallet achieved a positive profit while trading a specific meme coin and qualified as a KOL, whereas “FALSE” indicates otherwise.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Predicted | |  |
| Actual | TRUE | FALSE | Total |
| TRUE | 4,773 | 238,169 | 242,942 |
| FALSE | 2,106 | 369,282 | 371,388 |
| Total | 6,879 | 607,451 | 614,330 |

Next, we evaluate the performance of the wallet evaluation agent. [Table 3](https://arxiv.org/html/2601.08641v1#S9.T3 "Table 3 ‣ 9.3. Performance of Wallet Evaluation Agent ‣ 9. Experiment ‣ Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning") presents its classification confusion matrix. Given the large number of traders involved in a single migrated meme coin, we place greater emphasis on precision over recall. The agent achieves a precision of approximately 70% (4773/6879) in identifying wallets worth copy trading, which is quite strong. This suggests that the wallet evaluation agent can effectively predict future wallet profitability based on historical trading features.

## 10. Conclusion

In this paper, we propose an explainable, multi-modal, multi-agent framework for meme coin copy trading that employs few-shot chain-of-thought prompting and algorithmic bot detection. By decomposing the complex trading process into four specialized agents—meme evaluation, trader evaluation, wealth management, and order execution—our system mimics the decision-making workflow of professional asset managers. Empirical evaluation on 1,000 meme coin projects demonstrates that our framework effectively identifies high-quality meme coins and consistently profitable KOL wallets, achieving 70–73% precision. The selected KOL wallets collectively generated over $500,000 in profit, validating the practical utility of our approach. Our work highlights the promise of LLM-powered multi-agent systems in navigating volatile, information-rich environments such as meme coin markets.

## References

* (1)
* Ding et al. (2024)

  Qianggang Ding, Haochen Shi, and Bang Liu. 2024.
  TradExpert: Revolutionizing Trading with Mixture of Expert LLMs.
  (10 2024).

  <https://arxiv.org/abs/2411.00782v1>
* Fatemi and Hu (2024)

  Sorouralsadat Fatemi and Yuheng Hu. 2024.
  FinVision: A Multi-Agent Framework for Stock Market Prediction.
  *Proceedings of the 5th ACM International Conference on AI in Finance* (10 2024), 582–590.

  <https://doi.org/10.1145/3677052.3698688>
* Koa et al. (2024)

  Kelvin J.L. Koa, Yunshan Ma, Ritchie Ng, and Tat Seng Chua. 2024.
  Learning to Generate Explainable Stock Predictions using Self-Reflective Large Language Models.
  *WWW 2024 - Proceedings of the ACM Web Conference* 12 (5 2024), 4304–4315.

  [https://doi.org/10.1145/3589334.3645611/SUPPL{\_}FILE/RFP1792.MP4](https://doi.org/10.1145/3589334.3645611/SUPPL%7B_%7DFILE/RFP1792.MP4)
* Kou et al. (2024)

  Zhizhuo Kou, Holam Yu, Jingshu Peng, Hong Kong, and China Lei Chen. 2024.
  Automate Strategy Finding with LLM in Quant investment.
  (9 2024).

  <https://arxiv.org/abs/2409.06289v1>
* Li et al. (2023a)

  Lezhi Li, Ting-Yu Chang, and Hai Wang. 2023a.
  Multimodal Gen-AI for Fundamental Investment Research.
  (12 2023).

  <https://arxiv.org/abs/2401.06164v1>
* Li et al. (2024)

  Yuan Li, Bingqiao Luo, Qian Wang, Nuo Chen, Xu Liu, and Bingsheng He. 2024.
  A Reflective LLM-based Agent to Guide Zero-shot Cryptocurrency Trading.
  (6 2024).

  <https://arxiv.org/abs/2407.09546v1>
* Li et al. (2023b)

  Yinheng Li, Shaofei Wang, Han Ding, and Hang Chen. 2023b.
  Large Language Models in Finance: A Survey.
  (2023).

  <https://doi.org/10.1145/3604237.3626869>
* Liu et al. (2023a)

  Hao Liu, Carmelo Sferrazza, and Pieter Abbeel. 2023a.
  Chain of Hindsight Aligns Language Models with Feedback.
  *12th International Conference on Learning Representations, ICLR 2024* (2 2023).

  <https://arxiv.org/abs/2302.02676v8>
* Liu et al. (2023b)

  Xiao-Yang Liu, Guoxuan Wang, Hongyang Yang, and Daochen Zha. 2023b.
  FinGPT: Democratizing Internet-scale Data for Financial Large Language Models.
  (7 2023).

  <https://arxiv.org/abs/2307.10485v2>
* Luo et al. (2025)

  Yichen Luo, Yebo Feng, Jiahua Xu, Paolo Tasca, and Yang Liu. 2025.
  LLM-Powered Multi-Agent System for Automated Crypto Portfolio Management.
  (1 2025).

  <https://arxiv.org/pdf/2501.00826>
* Pan et al. (2024)

  Bo Pan, Jiaying Lu, Ke Wang, Li Zheng, Zhen Wen, Yingchaojie Feng, Minfeng Zhu, and Wei Chen. 2024.
  AgentCoord: Visually Exploring Coordination Strategy for LLM-based Multi-Agent Collaboration.
  (4 2024).

  <https://arxiv.org/abs/2404.11943v1>
* Wei et al. (2022)

  Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, and Denny Zhou. 2022.
  Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.
  *Advances in Neural Information Processing Systems* 35 (1 2022).

  <https://arxiv.org/abs/2201.11903v6>
* Wu et al. (2023)

  Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun Zhang, Shaokun Zhang, Jiale Liu, Ahmed Hassan Awadallah, Ryen W White, Doug Burger, and Chi Wang. 2023.
  AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation.
  (8 2023).

  <https://arxiv.org/abs/2308.08155v2>
* Xie et al. (2023)

  Qianqian Xie, Xiao Zhang, Weiguang Han, Yanzhao Lai, Min Peng, Alejandro Lopez-Lira, and Jimin Huang. 2023.
  PIXIU: A Large Language Model, Instruction Data and Evaluation Benchmark for Finance.
  *Advances in Neural Information Processing Systems* 36 (6 2023).

  <https://arxiv.org/abs/2306.05443v1>
* Yang et al. (2024)

  Jingfeng Yang, Hongye Jin, Ruixiang Tang, Xiaotian Han, Qizhang Feng, Haoming Jiang, Shaochen Zhong, Bing Yin, and Xia Hu. 2024.
  Harnessing the Power of LLMs in Practice: A Survey on ChatGPT and Beyond.
  *ACM Transactions on Knowledge Discovery from Data* 18, 6 (4 2024).

  <https://doi.org/10.1145/3649506/ASSET/D2038F72-9808-4957-BF9D-FB4E05F82081/ASSETS/GRAPHIC/TKDD-2023-06-0236-F02.JPG>
* Yin et al. (2024)

  Shukang Yin, Chaoyou Fu, Sirui Zhao, Ke Li, Xing Sun, Tong Xu, and Enhong Chen. 2024.
  A Survey on Multimodal Large Language Models.
  *National Science Review* (11 2024).

  <https://doi.org/10.1093/NSR/NWAE403>
* Zhang et al. (2024)

  Jingyi Zhang, Jiaxing Huang, Sheng Jin, and Shijian Lu. 2024.
  Vision-Language Models for Vision Tasks: A Survey.
  *IEEE Transactions on Pattern Analysis and Machine Intelligence* 46, 8 (2024), 5625–5644.

  <https://doi.org/10.1109/TPAMI.2024.3369699>

## Appendix A System Instructions and Prompts

System Instruction of Meme Evaluation Agent

You are a professional meme coin analyst. You will be provided with the candlestick chart, transaction history, and comment history of a meme coin. Your task is to assess whether the meme coin demonstrates good farming potential. Good farming implies that the coin is likely to experience sustainable upside potential in the future. Your response should follow this format:
”reasoning”: (your reasoning), ”good\_farming”: (true/false)

Prompt of Meme Evaluation Agent

Launch Bundle: {Launch Bundle}
Creator-funded Buy Bundle: {Creator-funded Buy Bundle}
Buy Bundle: {Buy Bundle}
Sell Bundle: {Sell Bundle}
Bump Bot: {Bump Bot}
Pre-migration Duration: {Pre-migration Duration}
Number of Unique Traders: {Number of Unique Traders}
Number of Transactions: {Number of Transactions}
Holding Centralization: {Holding Centralization}
Comment History: {Comment History}
Does this meme coin have good farming potential?

System Instruction of Wallet Evaluation Agent

You are a professional meme coin wallet analyst. You will be provided with the indicators of a wallet from the past 50 migrated meme coins. Your task is to assess whether the wallet is appropriate for the copy trading. Your response should follow this format:
”reasoning”: (your reasoning), ”good\_wallet”: (true/false)

Prompt of Wallet Evaluation Agent

Total Profit: {Total Profit}
Total Profit Std: {Total Profit Std}
Total Average Transaction Number: {Total Average Transaction Number}
Total Transaction Number Std: {Total Transaction Number Std}
Total Token Participated: {Total Token Participated}
Does this wallet have good copy trading potential?

CoT 1 of Wallet Evaluation Agent

Q: Total Profit: 6359.5
Total Profit Std: 332.5
Total Average Transaction Number: 18.4
Total Transaction Number Std: 26.3
Total Token Participated: 34
Does this wallet have good copy trading potential?
A: {”reasoning”: ”First, the total profit is very high, indicating that the wallet has been successful in its trading activities. Second, the total profit standard deviation is also high, suggesting that the wallet has made many profitable trades. Third, the average transaction number is high, indicating a high level of trading activity. Fourth, the number of tokens participated is also high, suggesting a diversified portfolio. Taken together, these factors suggest that the wallet has good copy trading potential.”, ”good\_wallet”: true}

CoT 1 of Wallet Evaluation Agent

Q: Total Profit: 10.0
Total Profit Std: 0.0
Total Average Transaction Number: 2.0
Total Transaction Number Std: 0.0
Total Token Participated: 1
Does this wallet have good copy trading potential?
A: {”reasoning”: ”First, the total profit is very low, indicating that the wallet has not been successful in its trading activities. Second, the total profit standard deviation is zero, suggesting that the wallet has not made one profitable trade. Third, the average transaction number is low, indicating a lack of trading activity. Fourth, the number of tokens participated is also low, suggesting a lack of diversification. Taken together, these factors suggest that the wallet does not have good copy trading potential.”, ”good\_wallet”: false}

CoT 1 of Meme Evaluation Agent

Q: Transaction Indicators:
Creator-funded Bundle: No
Creator-funded Buy Bundle: No
Buy Bundle: Medium
Sell Bundle: Low
Bump Bot: No
Pre-migration Duration: Low
Number of Unique Traders: Low
Number of Transactions: Low
Holding Centralization: Medium
Comment History:
B249Gj: Makers missing in your strategy? Add them fast!
5mGU8X: Proceed with the send or hold off? Here’s my input.![[Uncaptioned image]](Figures/cot_1.png)
Does this meme coin have good farming potential?
A: {”reasoning”: ”First, the candlestick chart shows only a single green candle from launch to migration, suggesting that early participants may have opened large positions with the intention of dumping after migration. Regardless of the transaction indicators or comment history, this pattern indicates a high likelihood of a post-migration sell-off. Therefore, the meme coin does not exhibit good farming potential.”, ”good\_farming”: false}

CoT 2 of Meme Evaluation Agent

Q: Transaction Indicators:
Creator-funded Bundle: No
Creator-funded Buy Bundle: No
Buy Bundle: Medium
Sell Bundle: Medium
Bump Bot: No
Pre-migration Duration: High
Number of Unique Traders: High
Number of Transactions: High
Holding Centralization: Low
Comment History:
4isgWB: Makers missing in your workflow? Adjust fast!
GpTf6r: Everyone’s shipping - you’re idle? Time to act.
6B8Q9u: Banner![[Uncaptioned image]](Figures/cot_2.png)
Does this meme coin have good farming potential?”
A: {”reasoning”: ”First, the candlestick chart shows a healthy pre-migration duration with multiple price fluctuations, indicating active trading activity. Second, the meme coin lacks both a creator-funded bundle and a creator-funded buy bundle, suggesting that the creator is not manipulating the market. Third, the buy and sell bundles are both at a moderate level, pointing to medium bot activity. Fourth, the high pre-migration duration, high number of unique traders, and high transaction volume all indicate robust community engagement and activity. Fifth, the low holding centralization suggests a decentralized token distribution. Finally, the comment history is predominantly positive, reflecting strong community sentiment. Taken together, these factors indicate that the meme coin exhibits good farming potential.”, ”good\_farming”: true}

CoT 3 of Meme Evaluation Agent

Q: Transaction Indicators:
Creator-funded Bundle: Yes
Creator-funded Buy Bundle: No
Buy Bundle: Low
Sell Bundle: Low
Bump Bot: No
Pre-migration Duration: High
Number of Unique Traders: High
Number of Transactions: High
Holding Centralization: High
Comment History:
7tPtnG: 2X IS NOT ENOUGH?
8PKg9x: $TRUMPAI INVEST BEFORE IT GOES 100X![[Uncaptioned image]](Figures/cot_3.png)
Does this meme coin have good farming potential?”
A: {”reasoning”: ”First, the candlestick chart shows a medium pre-migration duration, indicating some level of community engagement. Second, this meme coin involves a creator-funded bundle, indicating the creator accumulated a significant share of tokens before migration. Such behavior often signals an intent to dump post-migration, which undermines the coin’s sustainability. Despite favorable candlestick chart, transaction indicators, and comment history, the presence of a creator-funded bundle strongly suggests poor farming potential.”, ”good\_farming”: false}

CoT 4 of Meme Evaluation Agent

Q: Transaction Indicators:
Creator-funded Bundle: No
Creator-funded Buy Bundle: No
Buy Bundle: High
Sell Bundle: Low
Bump Bot: Yes
Pre-migration Duration: High
Number of Unique Traders: High
Number of Transactions: High
Holding Centralization: Low
Comment History:![[Uncaptioned image]](Figures/cot_4.png)
Does this meme coin have good farming potential?”
A: {”reasoning”: ”First, the candlestick chart shows a healthy pre-migration duration with multiple price fluctuations, indicating active trading activity. Second, the meme coin lacks both a creator-funded bundle and a creator-funded buy bundle, suggesting that the creator is not manipulating the market. Third, this meme coin has a high buy bundle and the bump bot, indicating significant bot activity. While the pre-migration duration, number of unique traders, and number of transactions are all high, the presence of a high buy bundle suggests that the coin is likely to experience a price spike followed by a decline. These factors suggest that the meme coin exhibits poor farming potential.”, ”good\_farming”: false}

CoT 5 of Meme Evaluation Agent

Q: Transaction Indicators:
Creator-funded Bundle: No
Creator-funded Buy Bundle: No
Buy Bundle: Medium
Sell Bundle: Medium
Bump Bot: No
Pre-migration Duration: Low
Number of Unique Traders: Low
Number of Transactions: Low
Holding Centralization: Medium
Comment History:![[Uncaptioned image]](Figures/cot_5.png)
Does this meme coin have good farming potential?”
A: {”reasoning”: ”First, the candlestick chart shows a healthy pre-migration duration with multiple price fluctuations, indicating active trading activity. Second, the meme coin lacks both a creator-funded bundle and a creator-funded buy bundle, suggesting that the creator is not manipulating the market. Third, the buy bundle and sell bundle are both at a moderate level, and there is no evidence of bump bot activity, pointing to medium bot activity. Fourth, the low pre-migration duration, low number of unique traders, and low transaction number all indicate limited community engagement and activity. Fifth, the medium holding centralization suggests that a moderate number of holders control a significant portion of the tokens, which is often a sign of poor distribution. Finally, there is no comment history, indicating a lack of community interaction. Taken together, these factors strongly suggest that the meme coin does not exhibit good farming potential.”, ”good\_farming”: false}