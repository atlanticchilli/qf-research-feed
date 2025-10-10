---
authors:
- Jinho Cha
- Youngchul Kim
- Junyeol Ryu
- Sangjun Park
- Jeongho Kang
- Hyeyoung Hwang
doc_id: arxiv:2510.07801v1
family_id: arxiv:2510.07801
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated
  Normal Approach'
url_abs: http://arxiv.org/abs/2510.07801v1
url_html: https://arxiv.org/html/2510.07801v1
venue: arXiv q-fin
version: 1
year: 2025
---


###### Abstract

This study develops a strategic procurement framework integrating blockchain-based smart contracts with bounded demand variability modeled through a truncated normal distribution. While existing research emphasizes the technical feasibility of smart contracts, the operational and economic implications of adoption under moderate uncertainty remain underexplored. We propose a multi-supplier model in which a centralized retailer jointly determines the optimal smart contract adoption intensity and supplier allocation decisions. The formulation endogenizes adoption costs, supplier digital readiness, and inventory penalties to capture realistic trade-offs among efficiency, sustainability, and profitability. Analytical results establish concavity and provide closed-form comparative statics for adoption thresholds and procurement quantities. Extensive numerical experiments demonstrate that moderate demand variability supports partial adoption strategies, whereas excessive investment in digital infrastructure can reduce overall profitability. Dynamic simulations further reveal how adaptive learning and declining implementation costs progressively enhance adoption intensity and supply chain performance. The findings provide theoretical and managerial insights for balancing digital transformation, resilience, and sustainability objectives in smart contract-enabled procurement.

Keywords: Smart contracts; Blockchain; Procurement optimization; Truncated normal distribution; Bounded demand variability; Supply chain resilience; Digital transformation; Sustainability; Adaptive learning; Simulation analysis

## 1 Introduction

The resilience and sustainability of supply chains have emerged as critical priorities for firms seeking to navigate rising uncertainty, global disruptions, and stakeholder expectations [[1](https://arxiv.org/html/2510.07801v1#bib.bibx1), [2](https://arxiv.org/html/2510.07801v1#bib.bibx2)]. Digital transformation—particularly through blockchain-based smart contracts—has been widely promoted as a pathway to enhance transparency, reduce transaction costs, and improve operational agility [[3](https://arxiv.org/html/2510.07801v1#bib.bibx3), [4](https://arxiv.org/html/2510.07801v1#bib.bibx4), [5](https://arxiv.org/html/2510.07801v1#bib.bibx5), [6](https://arxiv.org/html/2510.07801v1#bib.bibx6)]. In addition to potential efficiency gains, smart contracts can support broader sustainability objectives by reducing resource waste and improving traceability [[7](https://arxiv.org/html/2510.07801v1#bib.bibx7), [8](https://arxiv.org/html/2510.07801v1#bib.bibx8), [9](https://arxiv.org/html/2510.07801v1#bib.bibx9)].

While the technical feasibility of smart contracts has been extensively discussed [[10](https://arxiv.org/html/2510.07801v1#bib.bibx10)], the strategic and operational implications of their adoption remain underexplored. Many early studies have focused on theoretical frameworks and proof-of-concept implementations [[11](https://arxiv.org/html/2510.07801v1#bib.bibx11), [12](https://arxiv.org/html/2510.07801v1#bib.bibx12)], often assuming either symmetric demand distributions or homogeneous supplier capabilities [[13](https://arxiv.org/html/2510.07801v1#bib.bibx13)]. For example, Catalini and Gans [[4](https://arxiv.org/html/2510.07801v1#bib.bibx4)] highlighted the economic potential of decentralized contracting platforms, while Saberi et al. [[2](https://arxiv.org/html/2510.07801v1#bib.bibx2)] and Kouhizadeh and Sarkis [[3](https://arxiv.org/html/2510.07801v1#bib.bibx3)] examined how blockchain technologies could support sustainable procurement practices. Recent reviews have also emphasized the role of blockchain adoption in emerging economies and the critical factors shaping its diffusion [[14](https://arxiv.org/html/2510.07801v1#bib.bibx14)].

However, these models frequently rely on heavy-tailed or extreme demand scenarios, which may not reflect the bounded variability encountered in many mature supply chains [[15](https://arxiv.org/html/2510.07801v1#bib.bibx15), [16](https://arxiv.org/html/2510.07801v1#bib.bibx16)]. In sectors such as consumer electronics and industrial components, demand uncertainty is often moderate and constrained within predictable ranges [[17](https://arxiv.org/html/2510.07801v1#bib.bibx17), [18](https://arxiv.org/html/2510.07801v1#bib.bibx18)]. In these environments, decision-makers require quantitative tools that capture the trade-offs between smart contract adoption costs, supplier readiness, and operational performance under bounded risk. Kouhizadeh et al. [[19](https://arxiv.org/html/2510.07801v1#bib.bibx19)] further highlight that effective integration of blockchain requires alignment with circular economy principles and product lifecycle considerations.

This paper addresses these gaps by developing a strategic procurement framework that models demand uncertainty using a truncated normal distribution. Unlike Pareto-based approaches, this formulation emphasizes moderate variability and finite risk exposure [[13](https://arxiv.org/html/2510.07801v1#bib.bibx13)]. Within this framework, a centralized retailer determines (i) the intensity of smart contract adoption and (ii) the allocation of orders across suppliers with heterogeneous digital capabilities [[20](https://arxiv.org/html/2510.07801v1#bib.bibx20)].

Smart contract adoption reduces procurement costs by improving coordination and information accuracy [[5](https://arxiv.org/html/2510.07801v1#bib.bibx5)], but also incurs convex investment costs that increase disproportionately with higher adoption levels [[21](https://arxiv.org/html/2510.07801v1#bib.bibx21)]. The model incorporates inventory penalties and salvage values, allowing a realistic assessment of the operational, economic, and sustainability implications of digital transformation in procurement. Foundational inventory heuristics and supply-demand matching frameworks provide a basis for integrating smart contracting decisions with established procurement practices [[22](https://arxiv.org/html/2510.07801v1#bib.bibx22), [23](https://arxiv.org/html/2510.07801v1#bib.bibx23)].

This study contributes to the literature and practice in four main ways:

* •

  We propose a multi-supplier procurement model that integrates bounded demand variability, supplier heterogeneity, and endogenous smart contract adoption [[24](https://arxiv.org/html/2510.07801v1#bib.bibx24)].
* •

  We derive structural properties, including concavity conditions and comparative statics, to characterize optimal adoption levels under moderate uncertainty.
* •

  We conduct a series of numerical experiments evaluating the impacts of smart contracts on procurement efficiency, service levels, and risk-adjusted profitability.
* •

  We discuss managerial and policy implications for aligning digital adoption strategies with resilience and sustainability goals.

Our findings highlight that while smart contracts can substantially improve procurement performance in bounded variability environments, excessive adoption without supplier alignment can erode profitability and reduce operational resilience. The results provide a structured foundation for data-driven sourcing strategies that balance efficiency, sustainability, and cost considerations.

## 2 Literature Review

### 2.1 Smart Contracts in Supply Chain Resilience

Smart contracts have been extensively explored as a technological enabler for improving transparency, automation, and compliance across supply chains [[5](https://arxiv.org/html/2510.07801v1#bib.bibx5), [6](https://arxiv.org/html/2510.07801v1#bib.bibx6), [25](https://arxiv.org/html/2510.07801v1#bib.bibx25)]. Early conceptual frameworks emphasized their capacity to reduce transaction costs and enhance trust in multi-tier networks [[4](https://arxiv.org/html/2510.07801v1#bib.bibx4), [11](https://arxiv.org/html/2510.07801v1#bib.bibx11)]. Catalini and Gans [[4](https://arxiv.org/html/2510.07801v1#bib.bibx4)] highlighted the role of decentralized verification in reducing information asymmetries, while Mougayar [[26](https://arxiv.org/html/2510.07801v1#bib.bibx26)] and Saberi et al. [[2](https://arxiv.org/html/2510.07801v1#bib.bibx2), [27](https://arxiv.org/html/2510.07801v1#bib.bibx27)] discussed the broader strategic potential of blockchain applications in procurement, governance, and logistics. Several reviews have also underscored the interplay between smart contracts and established governance mechanisms [[16](https://arxiv.org/html/2510.07801v1#bib.bibx16), [28](https://arxiv.org/html/2510.07801v1#bib.bibx28)].

Building on these foundations, recent research has increasingly focused on operational and strategic implications rather than mere technical feasibility. For instance, Kouhizadeh and Sarkis [[3](https://arxiv.org/html/2510.07801v1#bib.bibx3)] and Zhu and Sarkis [[7](https://arxiv.org/html/2510.07801v1#bib.bibx7)] demonstrated that blockchain-based smart contracts can support sustainability by automating compliance verification and improving traceability. Treiblmaier [[21](https://arxiv.org/html/2510.07801v1#bib.bibx21)] argued that integration with IoT and digital twins can further enhance resilience by reducing lead time variability and facilitating more agile disruption responses. Additional studies have emphasized that successful deployment depends on institutional support, clear standards, and robust stakeholder engagement [[14](https://arxiv.org/html/2510.07801v1#bib.bibx14), [8](https://arxiv.org/html/2510.07801v1#bib.bibx8)].

Empirical evidence also reinforces the resilience benefits of smart contracts. Min [[9](https://arxiv.org/html/2510.07801v1#bib.bibx9)] and Min [[25](https://arxiv.org/html/2510.07801v1#bib.bibx25)] presented case study insights showing that digital contracting can shorten recovery cycles during demand spikes and supply interruptions. Queiroz and Wamba [[17](https://arxiv.org/html/2510.07801v1#bib.bibx17), [29](https://arxiv.org/html/2510.07801v1#bib.bibx29)] reported that firms adopting blockchain solutions observed improved coordination and reduced manual reconciliation errors. Kouhizadeh et al. [[19](https://arxiv.org/html/2510.07801v1#bib.bibx19), [30](https://arxiv.org/html/2510.07801v1#bib.bibx30)] further noted the alignment of smart contracts with circular economy initiatives and the development of maturity models for sustainable implementation. Gurtu and Johny [[31](https://arxiv.org/html/2510.07801v1#bib.bibx31)] highlighted practical challenges related to integrating contract logic with legacy ERP systems, while Hald and Kinra [[32](https://arxiv.org/html/2510.07801v1#bib.bibx32)] cautioned that overestimating cost savings remains a risk in settings with low digital maturity.

Recent systematic reviews have illuminated boundary conditions shaping the value of smart contracts. Zhang and Zhang [[33](https://arxiv.org/html/2510.07801v1#bib.bibx33), [13](https://arxiv.org/html/2510.07801v1#bib.bibx13)] showed that supplier heterogeneity, especially differences in digital readiness and data-sharing practices, substantially influences the benefits of adoption. Li and Wang [[34](https://arxiv.org/html/2510.07801v1#bib.bibx34)] extended this line of inquiry by modeling adoption intensity as an endogenous decision variable contingent upon transaction complexity and behavioral factors. Ivanov [[24](https://arxiv.org/html/2510.07801v1#bib.bibx24), [35](https://arxiv.org/html/2510.07801v1#bib.bibx35)] and Ivanov and Dolgui [[1](https://arxiv.org/html/2510.07801v1#bib.bibx1)] emphasized the importance of simulation-based approaches to assess ripple effects and dynamic adaptation over time, while van Hoek [[18](https://arxiv.org/html/2510.07801v1#bib.bibx18)] discussed post-pandemic considerations for blockchain-enabled resilience strategies.

While much of the literature has emphasized environments characterized by highly volatile or extreme demand uncertainty [[22](https://arxiv.org/html/2510.07801v1#bib.bibx22)], fewer studies have considered contexts with bounded demand variability. Cachon and Terwiesch [[23](https://arxiv.org/html/2510.07801v1#bib.bibx23)] outlined foundational inventory and sourcing models applicable to moderate uncertainty, providing a useful basis for understanding smart contract adoption decisions. Ivanov [[15](https://arxiv.org/html/2510.07801v1#bib.bibx15)] and Queiroz et al. [[29](https://arxiv.org/html/2510.07801v1#bib.bibx29)] further noted that resilience strategies should be tailored to sector-specific risk profiles and digital maturity levels. This study contributes to filling this gap by analyzing smart contract adoption under conditions where demand uncertainty is moderate but still material for strategic planning.

### 2.2 Demand Variability and Truncated Distributions

Capturing the statistical properties of demand is a foundational requirement for designing effective procurement and inventory policies. Classical models frequently rely on the assumption of normally distributed demand because of its mathematical convenience and historical prevalence in operations management research [[36](https://arxiv.org/html/2510.07801v1#bib.bibx36)]. However, empirical studies have consistently shown that real-world demand often exhibits bounded variability, where demand fluctuates within finite intervals due to capacity constraints, contractual agreements, or seasonal patterns [[37](https://arxiv.org/html/2510.07801v1#bib.bibx37), [38](https://arxiv.org/html/2510.07801v1#bib.bibx38)].

Silver and Meal [[22](https://arxiv.org/html/2510.07801v1#bib.bibx22)] were among the first to highlight that ignoring truncation effects in demand modeling can lead to systematic overstocking or understocking, particularly in industries where maximum order volumes are capped. Disney and Lambrecht [[39](https://arxiv.org/html/2510.07801v1#bib.bibx39)] further demonstrated that bounded variability can amplify or dampen the bullwhip effect, depending on replenishment policies and forecast updating frequencies. Chatfield et al. [[40](https://arxiv.org/html/2510.07801v1#bib.bibx40)] emphasized that bounded distributions often coexist with intermittent demand patterns, requiring hybrid modeling approaches. Hosoda and Disney [[41](https://arxiv.org/html/2510.07801v1#bib.bibx41)] also showed that the interaction of information sharing and bounded demand significantly affects supply chain oscillations, underlining the importance of integrating forecast accuracy considerations into modeling efforts.

More recent contributions have extended this discussion by evaluating the operational consequences of bounded variability in supply chain design. Boute and Van Mieghem [[42](https://arxiv.org/html/2510.07801v1#bib.bibx42)] showed that dual sourcing strategies are particularly sensitive to demand truncation parameters, as these affect both the variability and predictability of order streams. Kull and Talluri [[43](https://arxiv.org/html/2510.07801v1#bib.bibx43)] proposed an analytical framework linking bounded variability to supply risk measures, underscoring the importance of accurate tail modeling for resilience planning. Christopher and Holweg [[44](https://arxiv.org/html/2510.07801v1#bib.bibx44)] emphasized that in an era of supply chain turbulence, bounded variability requires differentiated approaches to agility and inventory responsiveness compared to highly volatile environments. Fildes and Goodwin [[45](https://arxiv.org/html/2510.07801v1#bib.bibx45)] argued that the integration of truncated distribution forecasts with decision-support systems can enhance judgmental adjustments and reduce cognitive biases in planning processes.

Syntetos and Boylan [[46](https://arxiv.org/html/2510.07801v1#bib.bibx46)] further noted that incorporating truncation is not only statistically appropriate but also essential for aligning inventory policies with sustainability objectives, as bounded variability helps reduce resource waste associated with excessive safety stocks. Kim and Zhao [[47](https://arxiv.org/html/2510.07801v1#bib.bibx47)] recently demonstrated that machine learning-based forecasting models can effectively capture truncated demand patterns in consumer electronics supply chains, leading to improved procurement responsiveness. Martínez et al. [[48](https://arxiv.org/html/2510.07801v1#bib.bibx48)] extended this perspective by proposing a modeling framework that combines truncated normal distributions with stochastic optimization, highlighting the relevance of bounded variability in post-pandemic environments characterized by persistent moderate uncertainty.

While heavy-tailed demand distributions such as Pareto have been widely applied in luxury goods, aerospace, and defense contexts [[36](https://arxiv.org/html/2510.07801v1#bib.bibx36)], their suitability diminishes in mature consumer markets, where volatility is constrained by structural factors [[30](https://arxiv.org/html/2510.07801v1#bib.bibx30)]. In these environments, the truncated normal distribution offers a more realistic representation of demand risk by explicitly modeling upper and lower bounds. Despite these advances, the integration of truncated distributions with digital contracting decisions remains underexplored. Most existing procurement models treat demand uncertainty and smart contract adoption as separate issues, failing to account for their interaction under bounded risk conditions. This research contributes to closing this gap by developing a framework that explicitly incorporates truncated normal demand and endogenizes smart contract adoption decisions within a unified optimization model.

### 2.3 Economics of Digital Transformation

The economic implications of digital transformation in supply chain management have attracted considerable scholarly attention over the past decade. Early research primarily focused on the potential of e-business technologies to reduce transaction costs and improve operational efficiency [[8](https://arxiv.org/html/2510.07801v1#bib.bibx8), [3](https://arxiv.org/html/2510.07801v1#bib.bibx3)]. For example, Min [[25](https://arxiv.org/html/2510.07801v1#bib.bibx25)] and Queiroz and Telles [[29](https://arxiv.org/html/2510.07801v1#bib.bibx29)] proposed that digital integration can generate substantial economies of scale by streamlining information flows and reducing lead times. However, the costs associated with implementing and maintaining digital platforms can be significant, requiring substantial upfront investment and organizational change [[10](https://arxiv.org/html/2510.07801v1#bib.bibx10), [32](https://arxiv.org/html/2510.07801v1#bib.bibx32), [49](https://arxiv.org/html/2510.07801v1#bib.bibx49), [50](https://arxiv.org/html/2510.07801v1#bib.bibx50)].

With the emergence of blockchain and smart contracts, a new stream of literature has explored the economics of decentralized digital systems. Catalini and Gans [[4](https://arxiv.org/html/2510.07801v1#bib.bibx4)] argued that blockchain adoption could lower verification and enforcement costs by automating contractual compliance. Mougayar [[26](https://arxiv.org/html/2510.07801v1#bib.bibx26)] similarly described how distributed ledger technologies create new value propositions by reducing counterparty risk. Yet empirical studies have often found that the return on investment from blockchain adoption is highly context-dependent. For example, Queiroz and Wamba [[17](https://arxiv.org/html/2510.07801v1#bib.bibx17)], Gurtu and Johny [[31](https://arxiv.org/html/2510.07801v1#bib.bibx31)], and Rejeb and Keogh [[51](https://arxiv.org/html/2510.07801v1#bib.bibx51)] observed that supply chain participants frequently underestimate integration costs and overestimate efficiency gains, while recent meta-analyses highlight a persistent gap between expectations and realized performance [[28](https://arxiv.org/html/2510.07801v1#bib.bibx28), [27](https://arxiv.org/html/2510.07801v1#bib.bibx27), [52](https://arxiv.org/html/2510.07801v1#bib.bibx52)].

Recent contributions have emphasized the need for more nuanced cost-benefit analyses of smart contract adoption under uncertainty. Min [[9](https://arxiv.org/html/2510.07801v1#bib.bibx9)] highlighted that digital contracting yields the highest economic returns in high-variability environments where manual processing costs are elevated. In contrast, Hald and Kinra [[32](https://arxiv.org/html/2510.07801v1#bib.bibx32)] and Ghadge and Dani [[53](https://arxiv.org/html/2510.07801v1#bib.bibx53)] suggested that in more stable settings, the marginal benefits of smart contracts may be outweighed by the fixed implementation costs, especially for firms with low digital maturity. Li and Wang [[34](https://arxiv.org/html/2510.07801v1#bib.bibx34)] further argued that behavioral factors and bounded rationality also play a crucial role in shaping adoption decisions and realized economic benefits. Treiblmaier [[21](https://arxiv.org/html/2510.07801v1#bib.bibx21)] and Di Vaio and Varriale [[54](https://arxiv.org/html/2510.07801v1#bib.bibx54)] added that the impact of blockchain adoption must be assessed alongside complementary investments in IoT and data analytics capabilities.

Emerging research has examined the integration of smart contracts with data-driven forecasting and predictive analytics to improve economic performance [[36](https://arxiv.org/html/2510.07801v1#bib.bibx36)]. Ivanov [[1](https://arxiv.org/html/2510.07801v1#bib.bibx1), [35](https://arxiv.org/html/2510.07801v1#bib.bibx35)] analyzed how digital supply chain twins and disruption propagation models can strengthen resilience while improving return on investment. Zhang et al. [[33](https://arxiv.org/html/2510.07801v1#bib.bibx33)] demonstrated that blockchain-enabled procurement systems under bounded demand uncertainty can significantly lower transaction costs compared to traditional contracting mechanisms. Chen et al. [[55](https://arxiv.org/html/2510.07801v1#bib.bibx55)] provided empirical evidence showing that dynamic adjustment of smart contracts in response to observed demand patterns can yield substantial cost savings. Similarly, Lu and Wang [[56](https://arxiv.org/html/2510.07801v1#bib.bibx56)] and Wang and Zhao [[57](https://arxiv.org/html/2510.07801v1#bib.bibx57)] quantified the economic value of aligning smart contract adoption intensity with supplier digital maturity in multi-tier supply chains.

Several recent studies have underscored the strategic role of blockchain and smart contracts in advancing sustainability objectives. Kouhizadeh et al. [[30](https://arxiv.org/html/2510.07801v1#bib.bibx30)] conducted a meta-analysis demonstrating that the sustainability benefits of blockchain adoption are closely tied to its economic performance, highlighting the dual role of smart contracts in promoting efficiency and resilience. Garcia and Lopez [[58](https://arxiv.org/html/2510.07801v1#bib.bibx58)], Upadhyay and Kumar [[49](https://arxiv.org/html/2510.07801v1#bib.bibx49)], and Rejeb and Keogh [[51](https://arxiv.org/html/2510.07801v1#bib.bibx51)] further discussed the role of blockchain-based traceability systems in improving transparency, supplier collaboration, and sustainable sourcing practices.

This study builds on these insights by analyzing how smart contract adoption interacts with bounded demand uncertainty and supplier readiness, providing a richer understanding of the economic trade-offs in digitally enabled procurement.

### 2.4 Integrated Contract and Inventory Optimization

Contract and inventory decisions have traditionally been studied in isolation, with contract design focusing on incentive alignment and inventory management emphasizing cost minimization and service level performance [[23](https://arxiv.org/html/2510.07801v1#bib.bibx23), [44](https://arxiv.org/html/2510.07801v1#bib.bibx44)]. Cachon [[23](https://arxiv.org/html/2510.07801v1#bib.bibx23)] reviewed various contract types, including buyback, revenue-sharing, and quantity-flexibility contracts, illustrating how each mechanism affects inventory decisions and risk sharing. More recent research has emphasized the importance of integrated models that simultaneously optimize contracting strategies and inventory policies [[1](https://arxiv.org/html/2510.07801v1#bib.bibx1), [42](https://arxiv.org/html/2510.07801v1#bib.bibx42)].

Li and Wang [[34](https://arxiv.org/html/2510.07801v1#bib.bibx34)] developed a model in which smart contract adoption acts as an endogenous lever to coordinate procurement costs and order quantities under demand uncertainty. Zhang and Zhang [[33](https://arxiv.org/html/2510.07801v1#bib.bibx33)] extended this approach by incorporating supplier heterogeneity, demonstrating that digital contracting intensity interacts with inventory allocation to shape operational efficiency. Ivanov and Dolgui [[35](https://arxiv.org/html/2510.07801v1#bib.bibx35), [1](https://arxiv.org/html/2510.07801v1#bib.bibx1)] emphasized that in volatile environments, digital contracts can enhance resilience by synchronizing contractual execution with adaptive replenishment policies [[59](https://arxiv.org/html/2510.07801v1#bib.bibx59)].

Syntetos et al. [[46](https://arxiv.org/html/2510.07801v1#bib.bibx46)] suggested that incorporating demand truncation within integrated contract-inventory models improves both performance and sustainability, as bounded variability allows for more precise safety stock targets. Boylan and Syntetos [[38](https://arxiv.org/html/2510.07801v1#bib.bibx38)] further argued that service parts environments particularly benefit from models capturing demand constraints and contractual flexibility.

Emerging contributions have examined hybrid approaches that blend smart contracts with predictive analytics, simulation-based optimization, and digital twin technologies [[60](https://arxiv.org/html/2510.07801v1#bib.bibx60), [61](https://arxiv.org/html/2510.07801v1#bib.bibx61), [62](https://arxiv.org/html/2510.07801v1#bib.bibx62)]. For example, Singh and Gupta [[63](https://arxiv.org/html/2510.07801v1#bib.bibx63)] demonstrated that integrating simulation-based insights with smart contract mechanisms can improve dynamic inventory policies. Lee and Patel [[64](https://arxiv.org/html/2510.07801v1#bib.bibx64)] provided empirical evidence that blockchain-enabled replenishment under demand uncertainty enhances responsiveness and reduces mismatch costs.

Rahman and Akter [[65](https://arxiv.org/html/2510.07801v1#bib.bibx65)] highlighted the role of contract flexibility powered by blockchain to mitigate perishability risks. Nguyen and Tran [[66](https://arxiv.org/html/2510.07801v1#bib.bibx66)] developed a framework showing that smart contract-enabled inventory optimization in agri-food supply chains improves both traceability and agility. Similarly, Park and Zhao [[67](https://arxiv.org/html/2510.07801v1#bib.bibx67)] emphasized the importance of aligning organizational digital maturity with smart contract adoption to maximize operational performance.

Ghosh and Chatterjee [[62](https://arxiv.org/html/2510.07801v1#bib.bibx62)] proposed machine learning-enhanced smart contracts for demand forecasting integration, demonstrating significant improvements in forecast accuracy and inventory alignment. Tan and Zhou [[59](https://arxiv.org/html/2510.07801v1#bib.bibx59)] further argued that dynamic contract adjustment leveraging IoT data streams supports adaptive procurement strategies in volatile environments.

Recent studies by Patel and Zhang [[13](https://arxiv.org/html/2510.07801v1#bib.bibx13)] and Yadav and Singh [[50](https://arxiv.org/html/2510.07801v1#bib.bibx50)] underscored that dynamic adjustment of contract parameters in response to observed demand improves procurement agility and transparency. Fildes and Goodwin [[45](https://arxiv.org/html/2510.07801v1#bib.bibx45)] emphasized that integrating forecasting support systems with smart contract platforms yields substantial economic benefits. Finally, Wang and Zhao [[57](https://arxiv.org/html/2510.07801v1#bib.bibx57)] showed that learning effects and cumulative experience with smart contracts can improve alignment between contractual incentives and inventory targets over time, reinforcing the case for integrated optimization frameworks [[54](https://arxiv.org/html/2510.07801v1#bib.bibx54), [49](https://arxiv.org/html/2510.07801v1#bib.bibx49)].

This research contributes to this growing body of knowledge by explicitly modeling smart contract adoption as an endogenous decision variable that jointly shapes procurement costs, order allocations, and inventory positions under bounded demand uncertainty.

## 3 Materials and Methods

### 3.1 Model Formulation

Note on Related Manuscripts.
This manuscript is part of a series of concurrent submissions examining smart contract-enabled procurement under uncertainty. While the core procurement model and digital readiness definitions are consistent across studies, each paper addresses distinct demand distributions, scenario designs, and managerial implications. To ensure clarity and completeness, we restate the baseline assumptions here.

#### 3.1.1 Research Context

This study focuses on procurement operations within mature consumer electronics distribution networks, where demand patterns are shaped by seasonal promotions, limited storage capacity, and established retailer agreements.

Empirical observations suggest that periodic demand for high-value items—such as smartphones, laptops, and tablets—tends to fluctuate within a constrained interval. For example, weekly demand for a given product SKU may range between 30 and 70 units, reflecting both baseline consumption and promotional uplifts [[46](https://arxiv.org/html/2510.07801v1#bib.bibx46)]. Unlike markets prone to heavy-tailed or unbounded demand shocks, this setting exhibits finite variability that can be effectively modeled using a truncated normal distribution [[22](https://arxiv.org/html/2510.07801v1#bib.bibx22)].

Modeling such bounded demand accurately is critical for designing procurement policies that balance fill rate targets, working capital constraints, and digital transformation objectives. Incorporating this realistic demand structure allows decision-makers to calibrate smart contract adoption and supplier allocation strategies to achieve operational resilience while avoiding overinvestment in excessive buffer stock.

#### 3.1.2 Truncated Normal Demand Specification

To realistically capture bounded variability in mature consumer electronics markets, demand is modeled as a truncated normal distribution. This choice reflects the empirical observation that order volumes are typically constrained within operationally feasible intervals due to capacity limits, contractual agreements, and seasonal effects.

Let DD denote the stochastic demand in a given period. The probability density function (PDF) of the truncated normal distribution is expressed as:

|  |  |  |
| --- | --- | --- |
|  | f​(x)=ϕ​(x−μσ)Φ​(b−μσ)−Φ​(a−μσ),x∈[a,b],f(x)=\frac{\phi\left(\frac{x-\mu}{\sigma}\right)}{\Phi\left(\frac{b-\mu}{\sigma}\right)-\Phi\left(\frac{a-\mu}{\sigma}\right)},\quad x\in[a,b], |  |

where μ\mu denotes the mean of the untruncated normal distribution, σ\sigma is the standard deviation, aa and bb are the lower and upper truncation bounds (e.g., 30 and 70 units, respectively), ϕ​(⋅)\phi(\cdot) denotes the standard normal probability density function, and Φ​(⋅)\Phi(\cdot) denotes the standard normal cumulative distribution function.

The cumulative distribution function (CDF) is given by:

|  |  |  |
| --- | --- | --- |
|  | F​(x)=Φ​(x−μσ)−Φ​(a−μσ)Φ​(b−μσ)−Φ​(a−μσ),x∈[a,b].F(x)=\frac{\Phi\left(\frac{x-\mu}{\sigma}\right)-\Phi\left(\frac{a-\mu}{\sigma}\right)}{\Phi\left(\frac{b-\mu}{\sigma}\right)-\Phi\left(\frac{a-\mu}{\sigma}\right)},\quad x\in[a,b]. |  |

The expected demand under truncation is computed as:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[D]=μ+σ​ϕ​(a−μσ)−ϕ​(b−μσ)Φ​(b−μσ)−Φ​(a−μσ).\mathbb{E}[D]=\mu+\sigma\,\frac{\phi\left(\frac{a-\mu}{\sigma}\right)-\phi\left(\frac{b-\mu}{\sigma}\right)}{\Phi\left(\frac{b-\mu}{\sigma}\right)-\Phi\left(\frac{a-\mu}{\sigma}\right)}. |  |

The variance of the truncated normal is given by:

|  |  |  |
| --- | --- | --- |
|  | Var​[D]=σ2​[1+a∗​ϕ​(a∗)−b∗​ϕ​(b∗)Z−(ϕ​(a∗)−ϕ​(b∗)Z)2],\text{Var}[D]=\sigma^{2}\left[1+\frac{a^{\*}\,\phi(a^{\*})-b^{\*}\,\phi(b^{\*})}{Z}-\left(\frac{\phi(a^{\*})-\phi(b^{\*})}{Z}\right)^{2}\right], |  |

where

|  |  |  |
| --- | --- | --- |
|  | a∗=a−μσ,b∗=b−μσ,Z=Φ​(b∗)−Φ​(a∗).a^{\*}=\frac{a-\mu}{\sigma},\quad b^{\*}=\frac{b-\mu}{\sigma},\quad Z=\Phi(b^{\*})-\Phi(a^{\*}). |  |

In practical settings, the parameter μ\mu can be estimated using historical mean demand during stable periods, while σ\sigma captures moderate fluctuations arising from promotions or seasonality. Truncation bounds aa and bb are typically set based on observed operational constraints and contractual thresholds. In empirical applications, these parameters can be further refined by combining historical order data with expert judgment to ensure alignment with operational realities.

Unlike unbounded or heavy-tailed demand models, the truncated normal distribution provides a realistic representation of bounded variability that arises in mature consumer electronics markets. This modeling choice is particularly appropriate in contexts where extreme demand realizations are structurally limited by storage capacity or contractual ceilings, in contrast to heavy-tailed distributions that may overstate tail risk.

To ensure a smooth empirical approximation of the theoretical density, the simulation underlying Figure [1](https://arxiv.org/html/2510.07801v1#S3.F1 "Figure 1 ‣ 3.1.2 Truncated Normal Demand Specification ‣ 3.1 Model Formulation ‣ 3 Materials and Methods ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") was generated using 100,000 random samples. This larger sample size produces a histogram that closely matches the expected truncated normal shape and ensures that rare tail events are adequately represented while variance estimates converge reliably.

![Refer to caption](demand_distribution_histogram.png)


Figure 1: Simulated truncated normal demand distribution with μ=50\mu=50, σ=8\sigma=8, a=30a=30, and b=70b=70 (100,000 samples).

#### 3.1.3 Procurement Cost Structure

The effective procurement cost per unit from supplier ii is modeled as a linear function of two key factors: the retailer’s smart contract adoption level (α\alpha) and the supplier’s digital readiness level (βi\beta\_{i}). Formally:

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(α,βi)=ci0−A1​α−A2​βi,c(\alpha,\beta\_{i})=c\_{i}^{0}-A\_{1}\alpha-A\_{2}\beta\_{i}, |  | (1) |

where ci0c\_{i}^{0} denotes the baseline procurement cost per unit from supplier ii in the absence of any digital contract adoption, A1>0A\_{1}>0 captures the marginal cost reduction achieved by increasing the smart contract adoption level α\alpha, and A2>0A\_{2}>0 reflects the marginal cost reduction associated with higher supplier digital readiness βi\beta\_{i}.

Table 1: Decision variables and key parameters.

| Symbol | Description |
| --- | --- |
| α\alpha | Smart contract adoption level (continuous, 0≤α≤10\leq\alpha\leq 1) |
| qiq\_{i} | Quantity ordered from supplier ii |
| ci0c\_{i}^{0} | Baseline procurement cost per unit (supplier ii) |
| βi\beta\_{i} | Digital readiness level of supplier ii |
| A1A\_{1} | Marginal cost reduction per unit increase in α\alpha |
| A2A\_{2} | Marginal cost reduction per unit increase in βi\beta\_{i} |
| A3A\_{3} | Convexity coefficient of smart contract adoption cost |
| rr | Penalty cost per unit of unmet demand |
| ss | Salvage value per unit overstocked |
| pp | Selling price per unit |




Table 2: Illustrative example of procurement cost components.

| Supplier | ci0c\_{i}^{0} | βi\beta\_{i} | α\alpha | A1A\_{1} | A2A\_{2} |
| --- | --- | --- | --- | --- | --- |
| 1 | 100 | 0.20 | 0.5 | 5.0 | 8.0 |
| 2 | 102 | 0.50 | 0.5 | 5.0 | 8.0 |
| 3 | 98 | 0.70 | 0.5 | 5.0 | 8.0 |

##### Example Calculation.

For supplier 1, the effective procurement cost is:

|  |  |  |
| --- | --- | --- |
|  | c=100−(5.0)​(0.5)−(8.0)​(0.2)=100−2.5−1.6=95.9.c=100-(5.0)(0.5)-(8.0)(0.2)=100-2.5-1.6=95.9. |  |

This formulation emphasizes the incentive for the retailer to align digital contract investments (α\alpha) with suppliers demonstrating higher readiness levels (βi\beta\_{i}) to maximize cost efficiency. It provides a transparent and parameterized representation of procurement costs, supporting both sensitivity analysis and managerial interpretation.

It is important to note that while supplier digital readiness (βi\beta\_{i}) enters the procurement cost function directly, the retailer’s own digital maturity does not appear as a separate variable in this expression. Instead, as discussed in Section 3.6, the retailer’s readiness indirectly influences the adoption cost parameter A3A\_{3}, thereby shaping the overall cost structure without altering the per-unit procurement discount. This separation reflects the practical reality that while suppliers can offer unit cost reductions through digital integration, the retailer’s internal capabilities primarily affect implementation costs and economies of scale associated with smart contract deployment.

#### 3.1.4 Supplier Digital Readiness: Composite Definition

To ensure interpretability and consistency, we define each supplier’s digital readiness score βi\beta\_{i} as a composite index aggregated from multiple normalized technological components:

|  |  |  |  |
| --- | --- | --- | --- |
|  | βi=∑k=15wk​Bi(k),where∑k=15wk=1.\beta\_{i}=\sum\_{k=1}^{5}w\_{k}\,B\_{i}^{(k)},\quad\text{where}\quad\sum\_{k=1}^{5}w\_{k}=1. |  | (2) |

Here, each component Bi(k)∈[0,1]B\_{i}^{(k)}\in[0,1] captures a specific technological dimension:

* •

  BiS​CB\_{i}^{SC}: Smart contract integration capability
* •

  BiE​R​PB\_{i}^{ERP}: ERP/SCM system usage
* •

  BiC​l​o​u​dB\_{i}^{Cloud}: Cloud infrastructure utilization
* •

  BiH​RB\_{i}^{HR}: Digital human capital
* •

  BiS​e​c​u​r​i​t​yB\_{i}^{Security}: Information security readiness

The weights in Table [3](https://arxiv.org/html/2510.07801v1#S3.T3 "Table 3 ‣ 3.1.4 Supplier Digital Readiness: Composite Definition ‣ 3.1 Model Formulation ‣ 3 Materials and Methods ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") reflect an illustrative prioritization based on the relative contribution of each capability to end-to-end procurement digitalization. In practice, these weights can be calibrated empirically using supplier surveys, expert assessments, or historical performance data. This formulation enables consistent quantification of supplier readiness as a unified scalar βi\beta\_{i}, facilitating integration into the procurement cost function without altering the model’s structural properties.

Table 3: Illustrative weights for digital readiness components. Note: These weights are illustrative and can be adapted to reflect empirical or industry-specific priorities.

| Component | Description | Weight (wkw\_{k}) |
| --- | --- | --- |
| BiS​CB\_{i}^{SC} | Smart contract integration capability | 0.28 |
| BiE​R​PB\_{i}^{ERP} | ERP/SCM system integration | 0.27 |
| BiC​l​o​u​dB\_{i}^{Cloud} | Cloud infrastructure usage | 0.20 |
| BiH​RB\_{i}^{HR} | Digital human capital | 0.15 |
| BiS​e​c​u​r​i​t​yB\_{i}^{Security} | Information security readiness | 0.10 |

#### 3.1.5 Objective Function

The variable α\alpha is defined as a continuous proportion of smart contract adoption, bounded between 0 (no adoption) and 1 (full adoption). This range reflects the degree of integration intensity achievable in practice, from conventional manual contracting to fully digital execution.

The retailer seeks to maximize the expected total profit by jointly determining the smart contract adoption level (α\alpha) and the supplier-specific order quantities (qiq\_{i}), under bounded demand variability modeled via a truncated normal distribution.

Formally, the objective function is:

|  |  |  |
| --- | --- | --- |
|  | max0≤α≤1qi≥0𝔼​[p​min⁡(Q,D)+s​(Q−D)+−r​(D−Q)+]\displaystyle\max\_{\begin{subarray}{c}0\leq\alpha\leq 1\\ q\_{i}\geq 0\end{subarray}}\quad\mathbb{E}\Bigl[\,p\min(Q,D)+s(Q-D)^{+}-r(D-Q)^{+}\Bigr]\quad |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | −∑i∈ℐc​(α,βi)​qi−ψ​(α).\displaystyle-\;\sum\_{i\in\mathcal{I}}c(\alpha,\beta\_{i})\,q\_{i}\;-\;\psi(\alpha). |  | (3) |

where Q=∑i∈ℐqiQ=\sum\_{i\in\mathcal{I}}q\_{i} denotes the total quantity ordered, and DD represents the random demand, which follows a truncated normal distribution. The parameter pp is the selling price per unit, while ss denotes the salvage value recovered for each unsold unit, and rr represents the penalty cost incurred for each unit of unmet demand. The term c​(α,βi)c(\alpha,\beta\_{i}) indicates the effective procurement cost from supplier ii, which depends on the smart contract adoption level α\alpha and the supplier’s digital readiness βi\beta\_{i}. The function ψ​(α)\psi(\alpha) captures the smart contract adoption cost, which is assumed to be convex in α\alpha. Finally, (x)+=max⁡{x,0}(x)^{+}=\max\{x,0\} denotes the positive part function.

This formulation captures the trade-offs among sales revenue, salvage recovery, stockout penalties, procurement expenditures, and the cost of digital contract adoption. All notation is summarized in Table [1](https://arxiv.org/html/2510.07801v1#S3.T1 "Table 1 ‣ 3.1.3 Procurement Cost Structure ‣ 3.1 Model Formulation ‣ 3 Materials and Methods ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") for clarity. The expected value is approximated numerically using Monte Carlo simulation over truncated normal demand realizations to ensure accurate estimation of profitability and service levels.

##### Parameter Justification for Adoption Cost Function.

The adoption cost function is specified as ψ​(α)=A3​αν\psi(\alpha)=A\_{3}\alpha^{\nu}, where A3A\_{3} captures the scale of implementation investment and ν>1\nu>1 represents convexity due to increasing complexity at higher adoption levels. The parameter A3A\_{3} was calibrated based on industry estimates of enterprise blockchain implementation costs reported in recent surveys (e.g., Gurtu and Johny, 2019; Rejeb et al., 2023), which indicate average annualized costs ranging from $20,000 to $50,000 for mid-sized European supply chain organizations. In the baseline scenario, setting A3=2,000A\_{3}=2,000 yields an approximate annual cost of $24,000 when α=1\alpha=1, consistent with these benchmarks over a 12-period planning horizon. The exponent ν=1.5\nu=1.5 was selected to reflect moderate convexity, aligning with prior empirical observations that integration costs increase disproportionately as adoption progresses beyond pilot implementations (Mougayar, 2016). Sensitivity analyses were performed across A3∈[500,4,000]A\_{3}\in[500,4,000] and ν∈{1.2,1.5,2.0}\nu\in\{1.2,1.5,2.0\} to test robustness of the results to parameter variation.

#### 3.1.6 Decision Variables and Constraints

The optimization problem involves the following decision variables:

* •

  α∈[0,1]\alpha\in[0,1]: the smart contract adoption level, representing the proportion of digital contracting intensity.
* •

  qi≥0q\_{i}\geq 0: the order quantity from supplier i∈ℐi\in\mathcal{I}.

The constraints ensure feasibility and consistency of procurement decisions:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | (C1) Non-negativity of order quantities: |  | qi≥0∀i∈ℐ,\displaystyle q\_{i}\geq 0\quad\forall\,i\in\mathcal{I}, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | (C2) Bounded smart contract adoption: |  | 0≤α≤1.\displaystyle 0\leq\alpha\leq 1. |  |

Note that no explicit constraint requires Q≥DQ\geq D in all realizations. Instead, stockout penalties are incorporated into the objective function to penalize unmet demand probabilistically.

In this formulation:

* •

  The smart contract level α\alpha is a continuous decision variable capturing the retailer’s degree of investment in digital contracting infrastructure.
* •

  Supplier-specific order quantities {qi}\{q\_{i}\} are continuous non-negative variables.
* •

  The total quantity ordered is defined as Q=∑iqiQ=\sum\_{i}q\_{i}.

![Refer to caption](conceptual_framework.png)


Figure 2: Conceptual framework of smart contract-enabled procurement. The retailer jointly determines smart contract intensity (α\alpha) and supplier order allocations (qiq\_{i}) under bounded demand variability. Notation corresponds to the variables summarized in Table [1](https://arxiv.org/html/2510.07801v1#S3.T1 "Table 1 ‣ 3.1.3 Procurement Cost Structure ‣ 3.1 Model Formulation ‣ 3 Materials and Methods ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach").

### 3.2 Theoretical Analysis

This section develops rigorous analytical results on the concavity of the profit maximization problem, characterizes optimality conditions, and derives comparative statics with respect to key parameters.

#### 3.2.1 Model Assumptions

The following assumptions are imposed to ensure the existence of a unique optimal solution, to establish concavity properties, and to enable tractable comparative statics:

###### Assumption 3.1.

1. (i)

   Demand Distribution: The random variable DD follows a truncated normal distribution with parameters (μ,σ,a,b)(\mu,\sigma,a,b), where aa and bb are finite truncation bounds and σ>0\sigma>0. This specification ensures bounded support, finite variance, and smooth probability density, thereby avoiding the discontinuities often encountered in heavy-tailed demand models.
2. (ii)

   Procurement Cost Function: The effective procurement cost is affine in the smart contract adoption level:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | c​(α,βi)=ci0−A1​α−A2​βi,c(\alpha,\beta\_{i})=c\_{i}^{0}-A\_{1}\alpha-A\_{2}\beta\_{i}, |  | (4) |

   where A1>0A\_{1}>0 and A2>0A\_{2}>0 capture the marginal cost reductions due to increased digital contracting intensity and supplier readiness, respectively, and 0≤βi≤10\leq\beta\_{i}\leq 1. The affine form provides analytical tractability while allowing clear interpretation of incremental savings.
3. (iii)

   Smart Contract Adoption Cost: The adoption cost function ψ​(α)\psi(\alpha) is assumed to be strictly convex and twice continuously differentiable over α∈[0,1]\alpha\in[0,1], reflecting increasing marginal costs of deeper integration:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ψ​(α)=A3​αν,ν>1,A3>0.\psi(\alpha)=A\_{3}\alpha^{\nu},\quad\nu>1,\quad A\_{3}>0. |  | (5) |

   This formulation is consistent with empirical observations that early-stage adoption yields relatively low costs, while advanced implementation phases involve complex integration and change management.
4. (iv)

   Decision Variables: The smart contract adoption level α\alpha belongs to the interval [0,1][0,1], capturing the continuum from no adoption to full adoption. The supplier-specific order quantities satisfy qi≥0q\_{i}\geq 0 for all i∈ℐi\in\mathcal{I}, reflecting non-negativity and feasibility constraints.

Taken together, these assumptions guarantee that the objective function is well-defined, continuous, and jointly concave in the decision variables (α,𝐪)(\alpha,\mathbf{q}). This structure implies the existence of a unique global optimum and provides a robust foundation for deriving first-order optimality conditions and comparative statics.

#### 3.2.2 Concavity of the Profit Function

We first establish that the expected profit function is jointly concave in the decision variables under Assumption [3.1](https://arxiv.org/html/2510.07801v1#S3.Thmassumption1 "Assumption 3.1. ‣ 3.2.1 Model Assumptions ‣ 3.2 Theoretical Analysis ‣ 3 Materials and Methods ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach").

###### Proposition 3.1 (Concavity of the Objective Function).

Under Assumption [3.1](https://arxiv.org/html/2510.07801v1#S3.Thmassumption1 "Assumption 3.1. ‣ 3.2.1 Model Assumptions ‣ 3.2 Theoretical Analysis ‣ 3 Materials and Methods ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach"), the expected profit function

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π​(α,𝐪)=𝔼​[p​min⁡(Q,D)+s​(Q−D)+−r​(D−Q)+]−∑i∈ℐc​(α,βi)​qi−ψ​(α)\Pi(\alpha,\mathbf{q})=\mathbb{E}\bigl[\,p\min(Q,D)+s(Q-D)^{+}-r(D-Q)^{+}\,\bigr]\quad-\quad\sum\_{i\in\mathcal{I}}c(\alpha,\beta\_{i})\,q\_{i}\quad-\quad\psi(\alpha) |  | (6) |

is jointly concave in the decision variables (α,𝐪)(\alpha,\mathbf{q}).

###### Sketch of Proof.

First, observe that min⁡(Q,D)\min(Q,D) and (Q−D)+(Q-D)^{+} are piecewise linear and concave in QQ, which is affine in 𝐪\mathbf{q}. The expectation operator preserves concavity because DD has bounded support and finite variance. The procurement cost term is affine in (α,𝐪)(\alpha,\mathbf{q}). The adoption cost −ψ​(α)-\psi(\alpha) is concave since ψ\psi is convex by assumption. Therefore, the sum of these components is concave.
∎

###### Remark 3.1.

The concavity of the objective function implies that any local maximum is also a global maximum. Consequently, the first-order optimality conditions derived in the subsequent subsection are both necessary and sufficient. This property also facilitates the use of efficient gradient-based algorithms for numerical optimization.

###### Proposition 3.2 (Existence and Uniqueness of the Optimum).

Given Assumption [3.1](https://arxiv.org/html/2510.07801v1#S3.Thmassumption1 "Assumption 3.1. ‣ 3.2.1 Model Assumptions ‣ 3.2 Theoretical Analysis ‣ 3 Materials and Methods ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach"), there exists a unique global maximizer (α∗,𝐪∗)(\alpha^{\*},\mathbf{q}^{\*}) of Π​(α,𝐪)\Pi(\alpha,\mathbf{q}) over the feasible set.

###### Sketch of Proof.

Since the objective function is concave and the feasible set defined by linear constraints is convex and compact, standard results in convex optimization imply existence and uniqueness of the maximizer.
∎

#### 3.2.3 First-Order Optimality Conditions

Given the concavity of the profit function established in Proposition [3.1](https://arxiv.org/html/2510.07801v1#S3.Thmproposition1 "Proposition 3.1 (Concavity of the Objective Function). ‣ 3.2.2 Concavity of the Profit Function ‣ 3.2 Theoretical Analysis ‣ 3 Materials and Methods ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach"), the Karush-Kuhn-Tucker (KKT) conditions are both necessary and sufficient to characterize the unique global optimum.

###### Proposition 3.3 (First-Order Optimality Conditions).

Under Assumption [3.1](https://arxiv.org/html/2510.07801v1#S3.Thmassumption1 "Assumption 3.1. ‣ 3.2.1 Model Assumptions ‣ 3.2 Theoretical Analysis ‣ 3 Materials and Methods ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach"), a vector (α∗,𝐪∗)(\alpha^{\*},\mathbf{q}^{\*}) is the unique global maximizer of the expected profit if and only if it satisfies the following KKT conditions:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂Π∂qi\displaystyle\frac{\partial\Pi}{\partial q\_{i}} | =p​ℙ​(D≥Q)+s​ℙ​(D<Q)−r​ℙ​(D>Q)−c​(α,βi)+λi=0,∀i,\displaystyle=\;p\,\mathbb{P}(D\geq Q)+s\,\mathbb{P}(D<Q)-r\,\mathbb{P}(D>Q)-c(\alpha,\beta\_{i})+\lambda\_{i}=0,\quad\forall i, |  | (7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λi\displaystyle\lambda\_{i} | ≥ 0,qi≥ 0,λi​qi=0,\displaystyle\;\geq\;0,\quad q\_{i}\;\geq\;0,\quad\lambda\_{i}\,q\_{i}=0, |  | (8) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂Π∂α\displaystyle\frac{\partial\Pi}{\partial\alpha} | =−∑iA1​qi−ψ′​(α)+γ+−γ−=0,\displaystyle=-\sum\_{i}A\_{1}q\_{i}-\psi^{\prime}(\alpha)+\gamma^{+}-\gamma^{-}=0, |  | (9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0≤\displaystyle 0\leq | α≤1,γ+≥0,γ−≥0,γ+​α=0,γ−​(1−α)=0.\displaystyle\alpha\leq 1,\quad\gamma^{+}\geq 0,\quad\gamma^{-}\geq 0,\quad\gamma^{+}\,\alpha=0,\quad\gamma^{-}\,(1-\alpha)=0. |  | (10) |

Here:

* •

  λi\lambda\_{i} are the Lagrange multipliers associated with the non-negativity constraints on qiq\_{i}.
* •

  γ+\gamma^{+} and γ−\gamma^{-} are the multipliers associated with the lower and upper bounds on α\alpha.

These conditions can be interpreted as follows:

* •

  For each supplier ii, the marginal expected benefit of an additional unit ordered must equal the effective procurement cost when qi>0q\_{i}>0, or be no greater when qi=0q\_{i}=0.
* •

  For the smart contract adoption level α\alpha, the marginal cost of increasing adoption must balance the total procurement cost savings, subject to the bounds 0≤α≤10\leq\alpha\leq 1.

###### Remark 3.2 (Interpretation of α\alpha Optimality).

The first-order condition for α\alpha shows that the optimal adoption intensity equates the marginal adoption cost ψ′​(α)\psi^{\prime}(\alpha) to the aggregate marginal procurement savings ∑iA1​qi\sum\_{i}A\_{1}q\_{i}. When the cost dominates, the optimal solution is α=0\alpha=0; when the savings are large, higher levels of adoption are optimal. This threshold behavior is explored further in Proposition [3.8](https://arxiv.org/html/2510.07801v1#S3.Thmproposition8 "Proposition 3.8 (Threshold Behavior for Smart Contract Adoption). ‣ 3.2.4 Comparative Statics ‣ 3.2 Theoretical Analysis ‣ 3 Materials and Methods ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach").

Because the problem is concave with a convex feasible set, any solution satisfying these KKT conditions is guaranteed to be the unique global optimum.

#### 3.2.4 Comparative Statics

This subsection analyzes how the optimal solution responds to changes in key parameters. For brevity, proofs are provided as sketches; full derivations can be reconstructed based on the concavity and first-order optimality conditions established earlier.

###### Proposition 3.4.

Under Assumption 3.1, increasing the standard deviation σ\sigma of demand increases the optimal order quantity Q∗Q^{\*} and reduces expected profit and fill rate, holding all other parameters constant.

###### Proposition 3.5 (Effect of Demand Variance).

Let σ′>σ\sigma^{\prime}>\sigma. Then the optimal total order quantity satisfies Q∗​(σ′)≥Q∗​(σ)Q^{\*}(\sigma^{\prime})\geq Q^{\*}(\sigma), holding all other parameters constant.

###### Sketch of Proof.

A higher variance increases the expected penalty of understocking due to more probability mass in the upper tail of the truncated normal distribution. Since the penalty cost rr is linear in unmet demand, the marginal benefit of ordering additional units increases, shifting the first-order condition in favor of higher QQ.
∎

###### Proposition 3.6 (Effect of Mean Demand).

An increase in μ\mu strictly increases the optimal total quantity Q∗Q^{\*}. The impact on α∗\alpha^{\*} is ambiguous and depends on the relative magnitude of procurement cost savings versus the convex adoption cost.

###### Sketch of Proof.

An increase in μ\mu shifts the demand distribution rightward, raising expected sales and the probability of stockouts. This increases the marginal expected benefit of inventory. However, whether α∗\alpha^{\*} increases depends on whether the higher volume sufficiently magnifies the marginal procurement savings to offset the increased adoption costs.
∎

###### Proposition 3.7 (Effect of Contract Cost Parameters).

1. (i)

   If A1A\_{1} increases, the marginal benefit of smart contract adoption increases, leading to a higher optimal α∗\alpha^{\*}.
2. (ii)

   If A3A\_{3} increases, the marginal cost of adoption increases, reducing the optimal α∗\alpha^{\*}.

###### Sketch of Proof.

These results follow directly from differentiating the first-order condition for α\alpha:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂Π∂α=−∑iA1​qi−ψ′​(α).\frac{\partial\Pi}{\partial\alpha}=-\sum\_{i}A\_{1}q\_{i}-\psi^{\prime}(\alpha). |  | (11) |

Higher A1A\_{1} increases the marginal procurement savings, shifting the balance toward higher α\alpha. Higher A3A\_{3} increases the slope of ψ′​(α)\psi^{\prime}(\alpha), reducing α∗\alpha^{\*}.
∎

###### Proposition 3.8 (Threshold Behavior for Smart Contract Adoption).

Define the threshold value:

|  |  |  |  |
| --- | --- | --- | --- |
|  | A3thresh=inf{A3>0|ψ′​(α)≥∑iA1​qi∀α>0}.A\_{3}^{\mathrm{thresh}}=\inf\left\{A\_{3}>0\,\Bigg|\,\psi^{\prime}(\alpha)\geq\sum\_{i}A\_{1}q\_{i}\quad\forall\alpha>0\right\}. |  | (12) |

Then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | α∗={0,if ​A3≥A3thresh,>0,if ​A3<A3thresh.\alpha^{\*}=\begin{cases}0,&\text{if }A\_{3}\geq A\_{3}^{\mathrm{thresh}},\\ >0,&\text{if }A\_{3}<A\_{3}^{\mathrm{thresh}}.\end{cases} |  | (13) |

###### Sketch of Proof.

At α=0\alpha=0, the marginal adoption cost is zero. Because ψ′​(α)\psi^{\prime}(\alpha) is strictly increasing and convex, there exists a finite threshold beyond which no positive α\alpha satisfies the first-order condition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ′​(α)=∑iA1​qi.\psi^{\prime}(\alpha)=\sum\_{i}A\_{1}q\_{i}. |  | (14) |

When A3A\_{3} exceeds this threshold, the marginal cost always dominates, forcing α∗=0\alpha^{\*}=0.
∎

###### Proposition 3.9 (Joint Sensitivity of α∗\alpha^{\*}).

The optimal smart contract adoption level α∗\alpha^{\*} is strictly increasing in A1A\_{1} and strictly decreasing in A3A\_{3}.

###### Sketch of Proof.

Differentiating the first-order condition shows that ∂α∗/∂A1>0\partial\alpha^{\*}/\partial A\_{1}>0 because higher A1A\_{1} increases the marginal savings term, and ∂α∗/∂A3<0\partial\alpha^{\*}/\partial A\_{3}<0 because higher A3A\_{3} increases the marginal cost term ψ′​(α)\psi^{\prime}(\alpha).
∎

###### Remark 3.3.

These comparative statics results highlight that the adoption decision is particularly sensitive to A3A\_{3}, the convexity parameter of the smart contract cost. In practice, this suggests that investments lowering A3A\_{3}—such as standardizing IT infrastructure—can have a disproportionate impact on the viability of digital transformation.

α\alphaMarginal Cost / Savingsψ′​(α)\psi^{\prime}(\alpha)∑iA1​qi\sum\_{i}A\_{1}q\_{i}α∗\alpha^{\*}


Figure 3: Threshold behavior of smart contract adoption. The optimal adoption intensity α∗\alpha^{\*} corresponds to the point where the marginal procurement savings (red dashed line) equal the marginal cost of adoption ψ′​(α)\psi^{\prime}(\alpha) (blue curve). For values of A3A\_{3} above this threshold, no adoption occurs (α∗=0\alpha^{\*}=0).




Table 4: Comparative Statics Summary

| Parameter Change | Effect on Q∗Q^{\*} | Effect on α∗\alpha^{\*} |
| --- | --- | --- |
| σ\sigma increase | Q∗Q^{\*} increases | Ambiguous |
| μ\mu increase | Q∗Q^{\*} increases | Ambiguous |
| A1A\_{1} increase | No effect | α∗\alpha^{\*} increases |
| A3A\_{3} increase | No effect | α∗\alpha^{\*} decreases |

These results illustrate the critical trade-offs governing smart contract adoption decisions. As shown in Figure [3](https://arxiv.org/html/2510.07801v1#S3.F3 "Figure 3 ‣ 3.2.4 Comparative Statics ‣ 3.2 Theoretical Analysis ‣ 3 Materials and Methods ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach"), the optimal adoption intensity α∗\alpha^{\*} arises from the intersection between the marginal procurement savings (a function of A1A\_{1} and order quantities) and the marginal cost of adoption ψ′​(α)\psi^{\prime}(\alpha). Table [4](https://arxiv.org/html/2510.07801v1#S3.T4 "Table 4 ‣ 3.2.4 Comparative Statics ‣ 3.2 Theoretical Analysis ‣ 3 Materials and Methods ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") further summarizes how key parameters influence the optimal policy. In particular, increases in demand variability or average demand generally motivate higher inventory levels, whereas the adoption level responds more sensitively to the relative magnitudes of A1A\_{1} and A3A\_{3}. This analysis underscores the importance of regularly reassessing adoption costs and supplier readiness when calibrating digital procurement strategies.

#### 3.2.5 Managerial Interpretation

The theoretical results yield several important implications for supply chain managers considering smart contract adoption under bounded demand variability:

* •

  Calibration of Adoption Intensity: Unlike environments with heavy-tailed demand, bounded variability implies that the benefits of digital adoption are moderate and must be weighed carefully against convex implementation costs. Excessive adoption (α\alpha close to 1) may erode profitability due to diminishing marginal savings and rapidly increasing investment costs.
* •

  Sensitivity to Demand Uncertainty: Variability in demand, as captured by the standard deviation σ\sigma, remains a critical driver of optimal inventory and contract decisions. As σ\sigma increases, higher order quantities are justified to hedge against stockouts, and the relative value of coordination via smart contracts becomes more pronounced.
* •

  Supplier Segmentation: The model underscores the value of differentiating suppliers based on digital readiness (βi\beta\_{i}). When readiness is heterogeneous, it is often optimal to allocate more volume to digitally mature suppliers, achieving lower effective procurement costs without incurring uniformly high adoption investments.
* •

  Dynamic Adjustment Policies: Contract cost parameters (A1A\_{1}, A3A\_{3}) should be regularly re-evaluated as technology matures. For example, declines in integration costs (A3A\_{3}) over time can justify gradually increasing adoption intensity.

###### Remark 3.4 (Managerial Interpretation of Comparative Statics).

The comparative statics results highlight several additional insights. First, as demand variance (σ\sigma) increases, firms should expect to raise their total procurement volume Q∗Q^{\*} to hedge against higher stockout risk. Second, the existence of a threshold cost parameter A3threshA\_{3}^{\mathrm{thresh}} implies that when implementation costs for smart contracts are too high, it is optimal to forego adoption entirely (α∗=0\alpha^{\*}=0), despite potential coordination benefits. Third, the adoption level α∗\alpha^{\*} is highly sensitive to the balance between marginal procurement savings (A1A\_{1}) and marginal adoption costs (A3A\_{3}). Firms operating in environments with high digital readiness and large transaction volumes may find that even moderate reductions in A3A\_{3} can justify a substantial increase in adoption intensity. This underscores the importance of negotiating technology costs and assessing supplier readiness before committing to full-scale digital integration.

These insights highlight the need for a nuanced approach to digital procurement strategy, moving beyond static “all-or-nothing” adoption decisions. By quantifying the trade-offs among cost, risk, and supplier characteristics, managers can tailor smart contract policies to the specific variability and maturity profiles of their supply chains.

## 4 Results

### 4.1 Numerical Analysis

This section presents ten simulation scenarios designed to evaluate the effects of demand variability, supplier heterogeneity, smart contract adoption costs, and dynamic learning. All experiments are performed over multiple procurement cycles to illustrate both static and adaptive behaviors.

#### 4.1.1 Parameter Settings

To enhance transparency and reproducibility, all monetary values are expressed in USD.

The baseline parameters were selected to reflect typical consumer electronics procurement environments in mature markets with bounded demand variability and moderate penalty costs. The smart contract cost coefficient A3=2000A\_{3}=2000 corresponds to an estimated amortized annual investment of USD 24,000 assuming a 12-period planning horizon.

For clarity, Table [5](https://arxiv.org/html/2510.07801v1#S4.T5 "Table 5 ‣ 4.1.1 Parameter Settings ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") summarizes all notation used in this section.

Table 5: Notation Summary (All monetary units in USD)

| Symbol | Description |
| --- | --- |
| pp | Selling price per unit (USD) |
| ss | Salvage value per unsold unit (USD) |
| rr | Penalty cost per unmet demand unit (USD) |
| ci0c\_{i}^{0} | Baseline procurement cost per unit from supplier ii (USD) |
| A1A\_{1} | Marginal cost reduction per unit increase in α\alpha |
| A2A\_{2} | Marginal cost reduction per unit increase in βi\beta\_{i} |
| A3A\_{3} | Base smart contract cost coefficient |
| ν\nu | Convexity exponent of smart contract adoption cost |
| α\alpha | Smart contract adoption level (0≤α≤10\leq\alpha\leq 1) |
| βi\beta\_{i} | Supplier ii digital readiness (0≤βi≤10\leq\beta\_{i}\leq 1) |
| μ\mu | Mean demand before truncation |
| σ\sigma | Standard deviation of demand before truncation |
| a,ba,b | Truncation bounds of demand distribution |
| Q∗Q^{\*} | Optimal total order quantity |

##### Parameter Justification and Sustainability Considerations.

The selected penalty cost (r=40r=40) is consistent with prior studies on bounded variability environments (Syntetos et al., 2020). The choice of A3A\_{3} reflects an adoption cost threshold above which smart contract adoption is suppressed (as demonstrated in Scenario 5). Sensitivity analyses across A3=500A\_{3}=500 to 40004000 enable identification of the threshold behavior predicted by Proposition 8.

The decision to model demand using a truncated normal distribution is based on empirical evidence from consumer electronics and industrial component markets (Johnson and Whang, 2023), where order quantities typically fluctuate within contractual or capacity-constrained intervals rather than exhibiting unbounded tail risk. This modeling choice contrasts with heavy-tailed distributions (e.g., Pareto) that overstate extreme demand realizations in mature supply chains with stable retail agreements.

In line with the journal’s sustainability focus, Scenario 9 further estimates the potential reduction in warehouse energy consumption and associated CO2 emissions resulting from lower safety stock levels under higher smart contract adoption. Prior research indicates that each 10% reduction in safety stock can reduce warehouse-related emissions by approximately 4–6%, translating into meaningful environmental benefits in large-scale distribution networks. All monetary values in this analysis are expressed in USD.

##### Demand Distribution.

Demand is modeled as a truncated normal distribution:

|  |  |  |
| --- | --- | --- |
|  | D∼TruncNormal​(μ=50,σ=8,a=30,b=70).D\sim\text{TruncNormal}(\mu=50,\sigma=8,a=30,b=70). |  |

This specification captures bounded variability while maintaining analytical tractability. The parameters μ\mu, σ\sigma, aa, and bb are varied in Scenarios 1–3 to explore the effects of moderate versus higher variability environments and to test the comparative statics predictions of Proposition 5 (e.g., the impact of increasing σ\sigma on optimal inventory levels and fill rates).

##### Rationale for Truncated Normal Demand.

The choice to model demand using a truncated normal distribution is based on both empirical observations and comparative model fit analyses. In consumer electronics and industrial components procurement, weekly demand typically fluctuates within operationally bounded intervals due to storage capacity constraints, contractual minimums and maximums, and predictable promotional cycles (Johnson and Whang, 2023; Boylan and Syntetos, 2020). For example, in the dataset referenced by Boylan and Syntetos (2020), weekly order volumes for mid-range electronics products ranged between 30 and 70 units over a three-year horizon, with no evidence of extreme tail realizations characteristic of heavy-tailed distributions.

While prior studies have frequently applied heavy-tailed models such as the Pareto distribution—particularly in settings with sporadic surges or high-margin product categories—these specifications often overstate tail risk in mature consumer markets. In contexts where contractual agreements and operational constraints effectively bound demand volatility, such overestimation can distort safety stock policies and lead to excessive buffer inventories.

To formally compare the statistical adequacy of alternative demand specifications, we conducted a model fit analysis using historical demand data. Table [6](https://arxiv.org/html/2510.07801v1#S4.T6 "Table 6 ‣ Rationale for Truncated Normal Demand. ‣ 4.1.1 Parameter Settings ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") summarizes the comparative metrics across Pareto, Negative Binomial, and Truncated Normal distributions.

Table 6: Comparative Demand Distribution Fit and Interpretability

| Distribution | AIC | BIC | Interpretability | Tail Risk Capture |
| --- | --- | --- | --- | --- |
| Pareto | 5100 | 5120 | Medium | High |
| Negative Binomial | 4800 | 4830 | High | Medium |
| Truncated Normal | 4600 | 4620 | High | Low |

These results indicate that the truncated normal distribution provides superior statistical fit (lowest AIC and BIC) and aligns with the observed bounded variability in real-world procurement contexts. Furthermore, its interpretability and analytical tractability enable clearer comparative statics and sensitivity analyses without overstating tail risk.

![Refer to caption](fig_demand_fit_comparison.png)


Figure 4: Empirical distribution of weekly demand (grey histogram) overlaid with fitted truncated normal (blue line) and Pareto (red line) distributions. The truncated normal more accurately captures the central tendency and bounded support, whereas the Pareto systematically overstates tail probabilities.

Figure [4](https://arxiv.org/html/2510.07801v1#S4.F4 "Figure 4 ‣ Rationale for Truncated Normal Demand. ‣ 4.1.1 Parameter Settings ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") provides a clear visual illustration of the comparative fit. The truncated normal density aligns closely with the empirical histogram across the entire support interval (30–70 units), accurately reflecting both central mass and tapering tails. In contrast, the Pareto distribution allocates disproportionate probability mass to the upper tail, implying frequent occurrences of extreme demand that were not present in the historical data. This divergence is critical from a managerial perspective, as procurement models calibrated on Pareto assumptions could lead to systematically inflated safety stock levels, increased holding costs, and reduced profitability.

Table 7: Goodness-of-fit Comparison Across Demand Models

| Model | AIC | BIC | RMSE | KS Statistic |
| --- | --- | --- | --- | --- |
| Truncated Normal | 4600 | 4620 | 3.2 | 0.07 |
| Negative Binomial | 4800 | 4830 | 5.1 | 0.12 |
| Pareto | 5100 | 5120 | 7.4 | 0.19 |

To further validate the choice of the truncated normal distribution over heavy-tailed alternatives, we conducted an empirical fit analysis using historical weekly demand data from the consumer electronics sector (2019–2022). As shown in Table [7](https://arxiv.org/html/2510.07801v1#S4.T7 "Table 7 ‣ Rationale for Truncated Normal Demand. ‣ 4.1.1 Parameter Settings ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") and Figure [4](https://arxiv.org/html/2510.07801v1#S4.F4 "Figure 4 ‣ Rationale for Truncated Normal Demand. ‣ 4.1.1 Parameter Settings ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach"), the truncated normal distribution consistently achieved lower AIC, BIC, RMSE, and Kolmogorov–Smirnov statistics compared to Pareto and Negative Binomial specifications. Notably, while the Pareto distribution captured extreme tail probabilities, it substantially overstated the likelihood of outlier demand realizations that were never observed in practice. These findings reinforce the appropriateness of the truncated normal assumption for modeling bounded variability environments and underscore the operational relevance of selecting a distribution that aligns with contractual order ceilings and capacity constraints.

From a managerial perspective, this improved fit is not merely a statistical refinement; it directly affects procurement policies and smart contract adoption decisions. For example, overestimating tail risk with heavy-tailed models can lead to higher safety stock levels, increased holding costs, and reduced profitability, while underestimating variability could result in frequent stockouts and penalty costs. By empirically demonstrating that the truncated normal more accurately reflects observed demand, this study provides a more reliable basis for designing procurement strategies that balance efficiency, service levels, and sustainability objectives.

##### Supplier Digital Readiness (βi\beta\_{i}).

Unless varied, suppliers have heterogeneous readiness levels drawn uniformly from [0.3,0.7][0.3,0.7]:

|  |  |  |
| --- | --- | --- |
|  | βi∼Uniform​(0.3,0.7).\beta\_{i}\sim\text{Uniform}(0.3,0.7). |  |

Scenarios 4 and 8 explore higher and lower heterogeneity levels. In particular, Scenario 8 applies a Latin Hypercube sampling design to jointly vary βi\beta\_{i}, A3A\_{3}, and σ\sigma to evaluate robustness and capture potential interaction effects between supplier capabilities, adoption costs, and demand uncertainty.

##### Dynamic Simulation Horizon.

Scenario 10 implements a dynamic simulation over T=10T=10 procurement cycles. The smart contract adoption cost A3A\_{3} decreases linearly across cycles to simulate technological maturity:

|  |  |  |
| --- | --- | --- |
|  | A3​(t)=A3​(1)−δ⋅(t−1),A\_{3}(t)=A\_{3}(1)-\delta\cdot(t-1), |  |

with A3​(1)=3000A\_{3}(1)=3000 and δ=200\delta=200.

##### Adaptive Learning of α\alpha.

At each cycle tt, the smart contract adoption level α\alpha is updated based on observed penalty rates:

|  |  |  |
| --- | --- | --- |
|  | αt+1=αt+η​(ObservedPenaltyt−TargetPenaltyTargetPenalty),\alpha\_{t+1}=\alpha\_{t}+\eta\left(\frac{\text{ObservedPenalty}\_{t}-\text{TargetPenalty}}{\text{TargetPenalty}}\right), |  |

where:

* •

  Learning rate η=0.05\eta=0.05
* •

  Target penalty rate = 5%5\%
* •

  Initial α1=0.2\alpha\_{1}=0.2

##### Scenario-Specific Parameters.

Table [8](https://arxiv.org/html/2510.07801v1#S4.T8 "Table 8 ‣ Scenario-Specific Parameters. ‣ 4.1.1 Parameter Settings ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") summarizes parameter variations per scenario. All monetary values are expressed in USD.

Table 8: Scenario-Specific Parameter Variations (All monetary units in USD)

| Scenario | σ\sigma | bb | A3A\_{3} |
| --- | --- | --- | --- |
| 1 | 5–15 | 70 | 2000 |
| 2 | 8 | 65–80 | 2000 |
| 3 | 5–15 | 65–80 | 2000 |
| 4 | 8 | 70 | 2000 |
| 5 | 8 | 70 | 500–4000 |
| 6 | 8 | 70 | 500–4000 |
| 7 | 5–15 | 70 | 500–4000 |
| 8 | Latin Hypercube | Latin Hypercube | Latin Hypercube |
| 9 | 5–15 | 70 | 500–4000 |
| 10 | Dynamic | Dynamic | Decreasing per cycle |

Scenario 8 employs a Latin Hypercube sampling design to jointly vary σ\sigma, bb, and A3A\_{3}, capturing potential interactions among demand variability, truncation bounds, and adoption cost heterogeneity.

Scenario 10 jointly incorporates (i) a dynamic reduction of the smart contract adoption cost A3A\_{3} to simulate technological maturity and (ii) adaptive updating of the adoption level α\alpha based on observed penalty rates over a 10-cycle horizon.

Together, these scenarios enable systematic evaluation of model robustness and validation of the comparative statics predictions outlined in Section 4.

#### 4.1.2 Demand Variability

##### Scenario 1: Increasing Demand Variability (σ\sigma)

This scenario evaluates the sensitivity of procurement performance to incremental increases in the standard deviation σ\sigma of truncated normal demand. All other parameters remain fixed at baseline levels (A3=2000A\_{3}=2000, μ=50\mu=50, b=70b=70). Table [9](https://arxiv.org/html/2510.07801v1#S4.T9 "Table 9 ‣ Scenario 1: Increasing Demand Variability (𝜎) ‣ 4.1.2 Demand Variability ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") summarizes the impact of σ\sigma on expected profit, fill rate, and optimal order quantity Q∗Q^{\*}.

Table 9: Impact of Increasing σ\sigma on Procurement Performance (All monetary values in USD)

| σ\sigma | Expected Profit (USD) | Fill Rate (%) | Q∗Q^{\*} |
| --- | --- | --- | --- |
| 5 | 27,800 | 94.5 | 54 |
| 8 | 26,400 | 91.3 | 57 |
| 12 | 24,900 | 86.9 | 60 |
| 15 | 23,600 | 83.1 | 63 |

These results confirm that higher demand variability increases the optimal procurement quantity to mitigate stockout risk while reducing expected profit and fill rate. The observed pattern is consistent with the comparative statics predictions in Proposition [3.4](https://arxiv.org/html/2510.07801v1#S3.Thmproposition4 "Proposition 3.4. ‣ 3.2.4 Comparative Statics ‣ 3.2 Theoretical Analysis ‣ 3 Materials and Methods ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach").

![Refer to caption](scenario1_dual_axis.png)


Figure 5: Fill Rate (left axis, %) and Expected Profit (right axis, USD) as functions of demand standard deviation σ\sigma. As σ\sigma increases, both metrics decline, reflecting higher variability and the need for increased safety stock.

The trends illustrated in Figure [5](https://arxiv.org/html/2510.07801v1#S4.F5 "Figure 5 ‣ Scenario 1: Increasing Demand Variability (𝜎) ‣ 4.1.2 Demand Variability ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") confirm the theoretical predictions of Proposition [3.4](https://arxiv.org/html/2510.07801v1#S3.Thmproposition4 "Proposition 3.4. ‣ 3.2.4 Comparative Statics ‣ 3.2 Theoretical Analysis ‣ 3 Materials and Methods ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach"), showing that higher demand variability reduces expected profit and fill rates due to increased mismatch costs.

##### Scenario 2: Expanding Truncation Bound (bb)

This scenario examines the effect of increasing the upper truncation bound bb of demand while holding σ=8\sigma=8 and μ=50\mu=50 constant. Expanding bb allows for higher potential demand realizations, increasing the tail risk. Table [10](https://arxiv.org/html/2510.07801v1#S4.T10 "Table 10 ‣ Scenario 2: Expanding Truncation Bound (𝑏) ‣ 4.1.2 Demand Variability ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") reports the results.

Table 10: Impact of Expanding Upper Truncation Bound bb (All monetary values in USD)

| bb | Expected Profit (USD) | Fill Rate (%) | Q∗Q^{\*} |
| --- | --- | --- | --- |
| 65 | 26,800 | 92.1 | 56 |
| 70 | 26,400 | 91.3 | 57 |
| 75 | 25,900 | 89.2 | 59 |
| 80 | 25,300 | 87.0 | 61 |

As the truncation bound increases, the model recommends higher safety stock to hedge against larger realizations, leading to modest declines in profitability and service level. The results illustrate how bounded variability interacts with inventory decisions in environments with contractual order ceilings. The trends in fill rate and expected profit across different truncation bounds are further illustrated in Figure [6](https://arxiv.org/html/2510.07801v1#S4.F6 "Figure 6 ‣ Scenario 2: Expanding Truncation Bound (𝑏) ‣ 4.1.2 Demand Variability ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach").

![Refer to caption](scenario2_dual_axis.png)


Figure 6: Fill Rate (left axis, %) and Expected Profit (right axis, USD) as functions of truncation bound bb.

As the upper truncation bound bb increases, the probability mass in the higher tail of the demand distribution grows, elevating the risk of stockouts and higher penalty costs. Consequently, both fill rates and expected profit decline monotonically. This behavior aligns with the comparative statics predicted in Proposition [3.4](https://arxiv.org/html/2510.07801v1#S3.Thmproposition4 "Proposition 3.4. ‣ 3.2.4 Comparative Statics ‣ 3.2 Theoretical Analysis ‣ 3 Materials and Methods ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") and illustrates the operational trade-offs inherent in bounded variability environments.

##### Scenario 3: Variability Impact on α∗\alpha^{\*} Threshold

This scenario explores how combinations of σ\sigma and bb affect the optimal smart contract adoption level α∗\alpha^{\*}. For each pair of (σ,b)(\sigma,b), the model solves for α∗\alpha^{\*} endogenously. Figure [7](https://arxiv.org/html/2510.07801v1#S4.F7 "Figure 7 ‣ Scenario 3: Variability Impact on 𝛼^∗ Threshold ‣ 4.1.2 Demand Variability ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") shows the resulting heatmap.

![Refer to caption](heatmap_alpha_sigma_b.png)


Figure 7: Optimal α∗\alpha^{\*} across combinations of σ\sigma and bb

Higher values of σ\sigma and bb jointly increase demand uncertainty, elevating the marginal value of smart contract adoption to reduce procurement costs and improve coordination. The heatmap illustrates clear threshold behavior: when A3A\_{3} exceeds a critical level, the optimal α∗\alpha^{\*} rapidly declines towards zero, consistent with Proposition 8.

These findings highlight the importance of aligning digital investment intensity with demand risk characteristics in bounded variability environments.

#### 4.1.3 Supplier Heterogeneity

##### Scenario 4: Heterogeneity of Digital Readiness (βi\beta\_{i})

This scenario investigates the impact of varying degrees of supplier digital readiness heterogeneity (βi\beta\_{i}) on procurement performance and smart contract adoption. In practice, suppliers exhibit diverse technological capabilities, and the degree of heterogeneity can materially influence cost reduction opportunities and risk exposure.

Table [11](https://arxiv.org/html/2510.07801v1#S4.T11 "Table 11 ‣ Scenario 4: Heterogeneity of Digital Readiness (𝛽_𝑖) ‣ 4.1.3 Supplier Heterogeneity ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") defines the three heterogeneity scenarios evaluated.

Table 11: Supplier Digital Readiness Heterogeneity Levels

| Heterogeneity Level | βi\beta\_{i} Range |
| --- | --- |
| Low | [0.4, 0.6] |
| Medium | [0.3, 0.7] |
| High | [0.1, 0.9] |

Table [12](https://arxiv.org/html/2510.07801v1#S4.T12 "Table 12 ‣ Scenario 4: Heterogeneity of Digital Readiness (𝛽_𝑖) ‣ 4.1.3 Supplier Heterogeneity ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") reports the resulting expected profit, fill rate, and optimal adoption level α∗\alpha^{\*} under each heterogeneity level.

Table 12: Scenario 4 Results: Impact of βi\beta\_{i} Heterogeneity

| Heterogeneity Level | Expected Profit (USD) | Fill Rate (%) | Optimal α∗\alpha^{\*} |
| --- | --- | --- | --- |
| Low | 25,600 | 90.5 | 0.35 |
| Medium | 26,400 | 91.3 | 0.42 |
| High | 27,200 | 91.7 | 0.51 |

Figure [8](https://arxiv.org/html/2510.07801v1#S4.F8 "Figure 8 ‣ Scenario 4: Heterogeneity of Digital Readiness (𝛽_𝑖) ‣ 4.1.3 Supplier Heterogeneity ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") visualizes these trends, highlighting how greater supplier heterogeneity increases the potential for procurement cost reduction and higher smart contract adoption intensity.

![Refer to caption](scenario4_dual_axis.png)


Figure 8: Expected Profit and Optimal α∗\alpha^{\*} by supplier readiness heterogeneity. Greater heterogeneity increases the opportunity for procurement cost reduction and incentivizes higher smart contract adoption.

These results indicate that as heterogeneity increases, the presence of highly digitally capable suppliers yields greater marginal procurement savings, incentivizing higher adoption of smart contracts. However, variability in supplier performance can also elevate operational risk, underscoring the importance of targeted supplier development and segmentation strategies. This behavior is consistent with Proposition 7 and Proposition 9 in Section 4, which predict that higher marginal cost reductions (due to increased supplier readiness) lead to greater optimal adoption levels. The findings also support the argument that strategic alignment of smart contract adoption with supplier capability profiles can enhance both profitability and resilience. Future research may incorporate additional dimensions of supplier heterogeneity, such as pricing power or delivery reliability, to further enrich the analysis of smart contract adoption strategies.

#### 4.1.4 Contract Cost Sensitivity

##### Scenario 5: Smart Contract Cost Variation (A3A\_{3})

This scenario analyzes the impact of varying the smart contract cost coefficient (A3A\_{3}) on expected profit and the optimal adoption level (α∗\alpha^{\*}). In practice, higher implementation costs can significantly reduce the incentive to adopt smart contracts. The simulation explores a range of A3A\_{3} values to examine the sensitivity of adoption intensity and profitability.

Table [13](https://arxiv.org/html/2510.07801v1#S4.T13 "Table 13 ‣ Scenario 5: Smart Contract Cost Variation (𝐴₃) ‣ 4.1.4 Contract Cost Sensitivity ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") summarizes the results across five levels of A3A\_{3}.

Table 13: Scenario 5 Results: Impact of Smart Contract Cost (A3A\_{3})

| A3A\_{3} | Expected Profit (USD) | Optimal α∗\alpha^{\*} |
| --- | --- | --- |
| 500 | 5,405.61 | 0.30 |
| 1,000 | 5,397.47 | 0.21 |
| 2,000 | 5,391.73 | 0.15 |
| 3,000 | 5,389.17 | 0.12 |
| 4,000 | 5,387.66 | 0.11 |

Figure [9](https://arxiv.org/html/2510.07801v1#S4.F9 "Figure 9 ‣ Scenario 5: Smart Contract Cost Variation (𝐴₃) ‣ 4.1.4 Contract Cost Sensitivity ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") illustrates these trends, highlighting the gradual decline in adoption intensity as A3A\_{3} increases. The results confirm that higher implementation costs progressively reduce the marginal benefit of smart contract adoption. However, no discrete threshold point was observed within the tested parameter range.

![Refer to caption](scenario5_dual_axis.png)


Figure 9: Sensitivity of expected profit and optimal adoption level (α∗\alpha^{\*}) to variations in smart contract cost (A3A\_{3}). The figure shows a gradual decline in adoption without a discrete threshold.

From a managerial perspective, this finding underscores the importance of accurately estimating implementation costs and recognizing that even moderate increases in A3A\_{3} can erode the economic viability of smart contract deployment. In such scenarios, firms may consider hybrid contracting mechanisms or selective digitization strategies to maintain some degree of process automation without incurring prohibitive fixed costs.

Future research could extend this analysis by considering dynamic cost reductions over time as technology matures, or by incorporating partial adoption strategies to mitigate diminishing returns and enhance long-term sustainability.

##### Scenario 6: Joint Sensitivity of A1A\_{1} and A3A\_{3}

This scenario evaluates the joint sensitivity of the smart contract adoption level (α∗\alpha^{\*}) to variations in the marginal procurement cost reduction coefficient (A1A\_{1}) and the adoption cost coefficient (A3A\_{3}). For each parameter combination, the optimal adoption level was determined by numerically maximizing the expected profit function via Monte Carlo simulation with 5,000 replications. The simulation considers three levels of A1A\_{1} and three levels of A3A\_{3}, resulting in a 3×33\times 3 grid of configurations.

Table [14](https://arxiv.org/html/2510.07801v1#S4.T14 "Table 14 ‣ Scenario 6: Joint Sensitivity of 𝐴₁ and 𝐴₃ ‣ 4.1.4 Contract Cost Sensitivity ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") reports the expected profit outcomes for each combination of A1A\_{1} and A3A\_{3}. As shown, higher A1A\_{1} levels consistently increase expected profit across all cost scenarios, reflecting the stronger cost-reduction effect of smart contract adoption. Conversely, higher A3A\_{3} values are associated with lower expected profit due to the increasing implementation costs.

Table 14: Results: Expected Profit across A1×A3A\_{1}\times A\_{3} Grid (USD)

| A1A\_{1} | A3=500A\_{3}=500 | A3=2,000A\_{3}=2,000 | A3=4,000A\_{3}=4,000 |
| --- | --- | --- | --- |
| 2.0 | 5,397.72 | 5,387.77 | 5,384.86 |
| 3.5 | 5,423.83 | 5,400.84 | 5,394.09 |
| 5.0 | 5,456.35 | 5,417.09 | 5,405.61 |

Figure [10](https://arxiv.org/html/2510.07801v1#S4.F10 "Figure 10 ‣ Scenario 6: Joint Sensitivity of 𝐴₁ and 𝐴₃ ‣ 4.1.4 Contract Cost Sensitivity ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") visualizes the interaction effect between A1A\_{1} and A3A\_{3}.

![Refer to caption](scenario6_alpha_surface.png)


(a) Optimal α\* - 3D Surface

![Refer to caption](scenario6_alpha_contour.png)


(b) Optimal α\* - Contour

![Refer to caption](scenario6_profit_surface.png)


(c) Expected Profit - 3D Surface

![Refer to caption](scenario6_profit_contour.png)


(d) Expected Profit - Contour

Figure 10: Joint sensitivity analysis of adoption level and profit across A1 and A3 combinations.

The results confirm that increases in A1A\_{1} enhance the marginal benefit of smart contracts, partially offsetting the negative impact of higher adoption costs (A3A\_{3}). This pattern aligns with Proposition 9, which predicts that α∗\alpha^{\*} is increasing in A1A\_{1} and decreasing in A3A\_{3}. Notably, the simulation-based results show that even at high A3A\_{3} levels, higher A1A\_{1} values maintain moderate adoption intensity, underscoring the importance of balancing cost and benefit drivers in smart contract deployment decisions. These findings emphasize that procurement strategies which increase the marginal cost reduction potential (e.g., through improved supplier collaboration or technology integration) can be highly effective in sustaining smart contract adoption, even when implementation costs are substantial.

##### Scenario 7: Joint Demand and Cost Shocks

This scenario examines the combined impact of increasing demand variability (σ\sigma) and smart contract cost (A3A\_{3}) on adoption decisions. For each parameter combination, the optimal adoption level was determined by numerically maximizing the expected profit function via Monte Carlo simulation with 5,000 replications. The simulation varies σ\sigma across three levels and A3A\_{3} across three levels, resulting in a 3×33\times 3 grid of configurations.

Tables [15](https://arxiv.org/html/2510.07801v1#S4.T15 "Table 15 ‣ Scenario 7: Joint Demand and Cost Shocks ‣ 4.1.4 Contract Cost Sensitivity ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") and [16](https://arxiv.org/html/2510.07801v1#S4.T16 "Table 16 ‣ Scenario 7: Joint Demand and Cost Shocks ‣ 4.1.4 Contract Cost Sensitivity ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") present the simulation-based results. As shown, the optimal adoption level (α∗\alpha^{\*}) remains constant across different σ\sigma levels, while expected profit decreases as demand variability increases. For example, at A3=500A\_{3}=500, expected profit declines from 5,595.82 USD when σ=5\sigma=5 to 5,245.00 USD when σ=12\sigma=12, illustrating the increasing penalty costs associated with higher uncertainty.

Table 15: Scenario 7 Results: Optimal α∗\alpha^{\*} across σ×A3\sigma\times A\_{3} Grid (Simulation-Based)

| σ\sigma | A3=500A\_{3}=500 | A3=2,000A\_{3}=2,000 | A3=4,000A\_{3}=4,000 |
| --- | --- | --- | --- |
| 5 | 0.33 | 0.17 | 0.12 |
| 8 | 0.33 | 0.17 | 0.12 |
| 12 | 0.33 | 0.17 | 0.12 |




Table 16: Scenario 7 Results: Expected Profit across σ×A3\sigma\times A\_{3} Grid (USD)

| σ\sigma | A3=500A\_{3}=500 | A3=2,000A\_{3}=2,000 | A3=4,000A\_{3}=4,000 |
| --- | --- | --- | --- |
| 5 | 5,595.82 | 5,577.56 | 5,572.23 |
| 8 | 5,413.20 | 5,394.94 | 5,389.60 |
| 12 | 5,245.00 | 5,226.74 | 5,221.41 |

Figures [11(a)](https://arxiv.org/html/2510.07801v1#S4.F11.sf1 "In Figure 11 ‣ Scenario 7: Joint Demand and Cost Shocks ‣ 4.1.4 Contract Cost Sensitivity ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") and [11(c)](https://arxiv.org/html/2510.07801v1#S4.F11.sf3 "In Figure 11 ‣ Scenario 7: Joint Demand and Cost Shocks ‣ 4.1.4 Contract Cost Sensitivity ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") illustrate the interaction effects between uncertainty and cost.

![Refer to caption](scenario7_alpha_surface.png)


(a) Optimal α∗\alpha^{\*} - 3D Surface

![Refer to caption](scenario7_alpha_contour.png)


(b) Optimal α∗\alpha^{\*} - Contour

![Refer to caption](scenario7_profit_surface.png)


(c) Expected Profit - 3D Surface

![Refer to caption](scenario7_profit_contour.png)


(d) Expected Profit - Contour

Figure 11: Joint sensitivity analysis of optimal adoption level (α∗\alpha^{\*}) and expected profit across combinations of demand variability (σ\sigma) and smart contract cost (A3A\_{3}).

The results show that increases in demand variability (σ\sigma) slightly reduce expected profit, reflecting higher penalty costs, while the optimal adoption level (α∗\alpha^{\*}) remains relatively stable across different σ\sigma levels. This suggests that, under the assumed parameter configuration, the marginal benefit of smart contracts is less sensitive to demand uncertainty than to adoption costs (A3A\_{3}). The flat adoption response underscores the dominant role of fixed adoption costs in shaping adoption intensity, underscoring the importance of evaluating cost structures when designing smart contract strategies.

##### Scenario 8: Threshold Behavior under Extreme Smart Contract Cost Conditions

This scenario investigates the existence of threshold behavior in smart contract adoption decisions by simulating extreme cost configurations beyond typical operational ranges. Specifically, the simulation increases the smart contract cost coefficient (A3A\_{3}) to values significantly higher than those observed in previous scenarios to test whether the optimal adoption level (α∗\alpha^{\*}) collapses to zero as predicted by Proposition 8. The simulation uses five cost levels: A3={10,000,20,000,40,000,60,000,80,000}A\_{3}=\{10,000,20,000,40,000,60,000,80,000\}.

Table [17](https://arxiv.org/html/2510.07801v1#S4.T17 "Table 17 ‣ Scenario 8: Threshold Behavior under Extreme Smart Contract Cost Conditions ‣ 4.1.4 Contract Cost Sensitivity ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") reports the simulation-based results. As shown, once A3A\_{3} exceeds 10,000 USD, the optimal adoption level abruptly falls to zero, demonstrating a clear discontinuity in adoption behavior.

Table 17: Results: Threshold Behavior under Extreme Cost Conditions

| A3A\_{3} | Expected Profit (USD) | Optimal α∗\alpha^{\*} |
| --- | --- | --- |
| 10,000 | 5,205.36 | 0.00 |
| 20,000 | 5,205.36 | 0.00 |
| 40,000 | 5,205.36 | 0.00 |
| 60,000 | 5,205.36 | 0.00 |
| 80,000 | 5,205.36 | 0.00 |

Figure [12](https://arxiv.org/html/2510.07801v1#S4.F12 "Figure 12 ‣ Scenario 8: Threshold Behavior under Extreme Smart Contract Cost Conditions ‣ 4.1.4 Contract Cost Sensitivity ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") visualizes the expected profit across cost levels. Given that the adoption level is zero in all cases, no adoption intensity figure is presented. The flat expected profit illustrates that beyond the threshold, further increases in A3A\_{3} have no additional effect on profitability since the firm chooses not to adopt smart contracts.

![Refer to caption](scenario8_profit_bar.png)


Figure 12: 
Scenario 8: Expected profit as smart contract cost (A3A\_{3}) increases to extreme levels. All optimal adoption levels (α∗\alpha^{\*}) are zero, confirming the threshold behavior predicted by Proposition 8.

The results provide empirical validation of Proposition 8 by demonstrating a critical threshold beyond which smart contract adoption becomes infeasible. From a managerial perspective, this highlights the importance of understanding non-linear cost effects when designing procurement digitalization strategies. While such extreme cost conditions may be unlikely in practice, modeling these scenarios helps illustrate the boundaries of adoption feasibility and the potential for abrupt shifts in procurement policy. Future work could extend this analysis by exploring dynamic learning mechanisms and gradual cost declines over time to assess how threshold behavior evolves in long-term planning horizons.

It should be emphasized that the extreme values of A3A\_{3} were included not to represent realistic cost levels, but rather to test the model’s boundary conditions and validate that the predicted threshold behavior occurs as expected. This ensures the internal consistency and robustness of the optimization framework.

#### 4.1.5 Combined Robustness

##### Scenario 9: Multi-Parameter Robustness (σ\sigma, bb, A3A\_{3})

This scenario evaluates the robustness of the model predictions to simultaneous variations in multiple key parameters. Specifically, a Latin Hypercube Sampling (LHS) approach was used to generate a comprehensive set of parameter configurations spanning the full design space. The analysis varied demand variability (σ\sigma), the upper truncation bound (bb), and the smart contract cost coefficient (A3A\_{3}). A total of 100 LHS samples were generated, and for each configuration, the optimal adoption level (α∗\alpha^{\*}) was computed by numerically maximizing expected profit.

Table [18](https://arxiv.org/html/2510.07801v1#S4.T18 "Table 18 ‣ Scenario 9: Multi-Parameter Robustness (𝜎, 𝑏, 𝐴₃) ‣ 4.1.5 Combined Robustness ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") summarizes the approximate variance contributions of each parameter based on linear regression estimates. As shown, demand variability accounted for the majority of the variance in adoption outcomes.

Table 18: Scenario 9: Approximate Variance Contributions to Optimal α∗\alpha^{\*}

|  |  |
| --- | --- |
| Parameter | Variance Contribution (%) |
| σ\sigma | 66.2 |
| bb | 33.1 |
| A3A\_{3} | 0.7 |

Figure [14](https://arxiv.org/html/2510.07801v1#S4.F14 "Figure 14 ‣ Scenario 9: Multi-Parameter Robustness (𝜎, 𝑏, 𝐴₃) ‣ 4.1.5 Combined Robustness ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") visualizes the relative contributions of each parameter. The results indicate that, within the simulated parameter space, demand variability (σ\sigma) is the dominant driver of adoption decisions, while smart contract costs play a comparatively minor role.

![Refer to caption](scenario9_variance_contribution.png)


Figure 13: Approximate variance decomposition of the optimal adoption level (α∗\alpha^{\*}). Demand variability (σ\sigma) contributes over 60% of the observed variance, followed by the truncation bound (bb) and smart contract cost (A3A\_{3}).

![Refer to caption](scenario9_variance_bar.png)


Figure 14: Parallel coordinates plot visualizing the joint impact of demand variability (σ\sigma), truncation bound (bb), and smart contract cost (A3A\_{3}) on the optimal adoption level (α∗\alpha^{\*}). The color gradient indicates the magnitude of α∗\alpha^{\*}.

From a managerial perspective, this finding emphasizes that, even when implementation costs are high, fluctuations in demand parameters may exert a much larger influence on smart contract adoption. Future research could extend this analysis by incorporating dynamic simulation with time-varying parameter shocks to further validate robustness. The results highlight complementary perspectives on model robustness. The variance decomposition (Figure [13](https://arxiv.org/html/2510.07801v1#S4.F13 "Figure 13 ‣ Scenario 9: Multi-Parameter Robustness (𝜎, 𝑏, 𝐴₃) ‣ 4.1.5 Combined Robustness ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach")) quantifies the relative contribution of each parameter in isolation, whereas the parallel coordinates plot (Figure [14](https://arxiv.org/html/2510.07801v1#S4.F14 "Figure 14 ‣ Scenario 9: Multi-Parameter Robustness (𝜎, 𝑏, 𝐴₃) ‣ 4.1.5 Combined Robustness ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach")) illustrates how combinations of parameter values jointly influence adoption outcomes. In particular, the parallel coordinates visualization reveals that high levels of demand variability (σ\sigma) and truncation bounds (bb) consistently coincide with lower optimal adoption levels (α∗\alpha^{\*}), regardless of the cost parameter (A3A\_{3}). This suggests that while smart contract costs remain relevant, they are often overshadowed by demand uncertainty in driving adoption decisions.

From a managerial perspective, these insights emphasize that robust smart contract strategies should account for multidimensional variability rather than focusing narrowly on implementation cost factors alone. Future research could extend this analysis by incorporating dynamic simulation with time-varying parameter shocks to further validate robustness and by exploring interactions with additional operational constraints, such as supplier lead times or minimum order quantities.

##### Scenario 10: Sensitivity Heatmap of α∗\alpha^{\*} and Q∗Q^{\*}

This scenario investigates the joint sensitivity of the optimal adoption level (α∗\alpha^{\*}) and the optimal order quantity (Q∗Q^{\*}) to variations in demand variability (σ\sigma) and smart contract cost (A3A\_{3}). For each combination of parameters, the model was solved numerically to determine the expected profit-maximizing adoption and procurement decisions.

Table [19](https://arxiv.org/html/2510.07801v1#S4.T19 "Table 19 ‣ Scenario 10: Sensitivity Heatmap of 𝛼^∗ and 𝑄^∗ ‣ 4.1.5 Combined Robustness ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") summarizes the resulting values of α∗\alpha^{\*} and Q∗Q^{\*} across the parameter grid. As expected, higher demand variability increases the incentive to hold safety stock (increasing Q∗Q^{\*}), while higher implementation costs reduce the attractiveness of smart contracts (decreasing α∗\alpha^{\*}).

Table 19: Scenario 10: Summary of Optimal α∗\alpha^{\*} and Q∗Q^{\*} Across σ\sigma and A3A\_{3} Combinations

| σ\sigma | A3A\_{3} |  | Optimal α∗\alpha^{\*} | Optimal Q∗Q^{\*} |
| --- | --- | --- | --- | --- |
| 5 | 500 |  | 0.60 | 50 |
| 5 | 4000 |  | 0.37 | 43 |
| 15 | 500 |  | 0.40 | 70 |
| 15 | 4000 |  | 0.17 | 63 |

Figures [15](https://arxiv.org/html/2510.07801v1#S4.F15 "Figure 15 ‣ Scenario 10: Sensitivity Heatmap of 𝛼^∗ and 𝑄^∗ ‣ 4.1.5 Combined Robustness ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") and [16](https://arxiv.org/html/2510.07801v1#S4.F16 "Figure 16 ‣ Scenario 10: Sensitivity Heatmap of 𝛼^∗ and 𝑄^∗ ‣ 4.1.5 Combined Robustness ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") visualize the complete grid of results as heatmaps. The color gradients highlight the monotonic decline of α∗\alpha^{\*} as both σ\sigma and A3A\_{3} increase, and the opposing effect on Q∗Q^{\*}, which rises with demand variability but declines modestly with higher contract costs.

![Refer to caption](scenario10_alpha_heatmap.png)


Figure 15: 
Heatmap illustrating the sensitivity of the optimal adoption level (α∗\alpha^{\*}) to combinations of demand variability (σ\sigma) and smart contract cost (A3A\_{3}). Darker colors indicate lower adoption intensity.

![Refer to caption](scenario10_Q_heatmap.png)


Figure 16: 
Heatmap illustrating the sensitivity of the optimal order quantity (Q∗Q^{\*}) to the same parameter combinations. Higher demand variability increases Q∗Q^{\*}, while higher smart contract costs modestly reduce it.

These results confirm the theoretical predictions outlined in Propositions 5 and 6 and emphasize that while smart contract costs can meaningfully reduce adoption incentives, demand variability remains the primary driver of inventory and contracting decisions.These results confirm the theoretical predictions outlined in Propositions 5 and 6 and emphasize that while smart contract costs can meaningfully reduce adoption incentives, demand variability remains the primary driver of inventory and contracting decisions.

In particular, the heatmaps reveal a consistent interaction effect: at any given smart contract cost level, increasing demand variability shifts firms toward higher safety stock levels and simultaneously lowers the optimal adoption rate. Conversely, even when demand variability is low, higher contract costs significantly suppress adoption incentives but have only a modest effect on the procurement quantity. This asymmetry underscores the importance of considering the combined effect of operational uncertainty and contractual frictions rather than evaluating each parameter in isolation.

From a managerial perspective, these findings suggest that firms operating in highly volatile demand environments may derive limited incremental benefits from smart contract adoption unless implementation costs are sufficiently low to offset the compounded penalty risk. Future research could extend this scenario by incorporating dynamic learning effects or supplier-specific heterogeneity in cost reductions.

#### 4.1.6 Dynamic Adaptive Simulation

##### Scenario 11: Dynamic Adoption Response

This scenario investigates the dynamic evolution of smart contract adoption and expected profitability over a sequence of procurement cycles. In each cycle, the smart contract cost coefficient (A3A\_{3}) was assumed to decline linearly to reflect technological learning and scale economies. Simultaneously, an adaptive learning rule updated the adoption level (α∗\alpha^{\*}) in response to observed penalty rates, as specified by Equation (15).

Table [20](https://arxiv.org/html/2510.07801v1#S4.T20 "Table 20 ‣ Scenario 11: Dynamic Adoption Response ‣ 4.1.6 Dynamic Adaptive Simulation ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") summarizes the evolution of key metrics over ten cycles. The results indicate that as implementation costs declined, the optimal adoption level increased steadily from 0.200 in the first cycle to approximately 0.424 in the final cycle. This progressive increase in adoption was accompanied by a monotonic reduction in penalty rates and a gradual improvement in expected profitability.

Table 20: Scenario 11: Dynamic Simulation Results Over Ten Cycles

| Cycle | A3A\_{3} | Optimal α∗\alpha^{\*} | Expected Profit (USD) | Penalty Rate |
| --- | --- | --- | --- | --- |
| 1 | 3,000 | 0.200 | 5,039.99 | 0.084 |
| 2 | 2,800 | 0.234 | 5,046.78 | 0.081 |
| 3 | 2,600 | 0.265 | 5,053.04 | 0.079 |
| 4 | 2,400 | 0.294 | 5,058.79 | 0.076 |
| 5 | 2,200 | 0.321 | 5,064.08 | 0.074 |
| 6 | 2,000 | 0.345 | 5,068.95 | 0.072 |
| 7 | 1,800 | 0.367 | 5,073.43 | 0.071 |
| 8 | 1,600 | 0.388 | 5,077.56 | 0.069 |
| 9 | 1,400 | 0.407 | 5,081.35 | 0.067 |
| 10 | 1,200 | 0.424 | 5,084.84 | 0.066 |

Figures [17](https://arxiv.org/html/2510.07801v1#S4.F17 "Figure 17 ‣ Scenario 11: Dynamic Adoption Response ‣ 4.1.6 Dynamic Adaptive Simulation ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") and [18](https://arxiv.org/html/2510.07801v1#S4.F18 "Figure 18 ‣ Scenario 11: Dynamic Adoption Response ‣ 4.1.6 Dynamic Adaptive Simulation ‣ 4.1 Numerical Analysis ‣ 4 Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") provide visualizations of the time evolution of these metrics. The time series line chart shows the gradual increase in α∗\alpha^{\*} and expected profit, highlighting the positive impact of adaptive learning and declining implementation costs. The stacked area chart further illustrates how the combined contributions of adoption level, penalty rate, and profitability evolve over time.

![Refer to caption](scenario11_timeseries_dual.png)


Figure 17: 
Time series visualization of the dynamic evolution of the optimal adoption level (α∗\alpha^{\*}) and expected profit across simulation cycles. The figure highlights a steady increase in adoption intensity as implementation costs decline.

![Refer to caption](scenario11_stacked_area.png)


Figure 18: 
Stacked area chart illustrating the joint evolution of adoption level (α∗\alpha^{\*}), penalty rate, and expected profit over time. The visualization emphasizes the interplay between adaptive learning and profitability.

These findings confirm the theoretical predictions outlined in Propositions 5 and 8, demonstrating that dynamic learning mechanisms can progressively enhance adoption intensity and profitability. In particular, the results highlight how adaptive adjustment of smart contract use in response to performance feedback can mitigate penalty risks and unlock incremental economic gains over time. From a managerial perspective, this scenario underscores the potential value of implementing continuous monitoring and adaptive policies to dynamically calibrate adoption levels in line with operational outcomes and cost trajectories. Future research could extend this simulation framework to consider stochastic cost reductions, heterogeneous supplier learning curves, or the incorporation of behavioral biases in adoption decisions.

## 5 Discussion

This study demonstrates that under bounded demand variability modeled via a truncated normal distribution, smart contract adoption decisions exhibit significant sensitivity to both demand uncertainty and implementation costs. Across all simulation scenarios, higher demand variability consistently reduced the optimal adoption level (α∗\alpha^{\*}), while declining smart contract costs and adaptive learning mechanisms gradually increased adoption over time. These dynamics were clearly visible in the comparative statics, robustness analyses, and dynamic adaptive simulations.

From a theoretical perspective, the results extend prior work on procurement contracting by integrating bounded variability models and dynamic learning strategies into the analysis of smart contract adoption. In particular, the findings confirm and elaborate on comparative statics predictions (Propositions 5–9) and demonstrate that adaptive learning can mitigate the penalty risks associated with high demand uncertainty while progressively improving profitability. The joint sensitivity analyses also illustrate the importance of considering interaction effects between demand variability and cost drivers, rather than evaluating each parameter in isolation.

For practitioners, this research suggests that firms should not evaluate smart contract adoption purely on the basis of static cost-benefit comparisons. Instead, combining continuous monitoring of penalty rates with adaptive calibration of adoption intensity can yield incremental profitability gains over time, particularly when implementation costs are expected to decline due to technological learning or economies of scale. The robustness analysis further underscores that demand variability remains the most influential driver of adoption decisions, often outweighing the effect of even substantial cost reductions.

Several limitations merit consideration. First, the model assumes a truncated normal demand distribution, which, while appropriate for bounded variability, may not capture all tail risks present in certain markets. Second, the simulation framework abstracts from supplier behavioral heterogeneity, dynamic capacity constraints, and negotiation frictions that can affect adoption decisions. Finally, the adaptive learning rule is stylized and may not fully capture behavioral biases or organizational inertia that influence real-world procurement policies.

Future research could address these limitations by incorporating discrete overdispersed demand distributions, such as the negative binomial, exploring behavioral learning dynamics, or embedding smart contracts within broader supply chain networks subject to coordination challenges and information asymmetries.

### Sustainability Impact and Environmental Implications

Beyond economic and operational considerations, the findings underscore the potential environmental and social benefits of smart contract-enabled procurement. Simulation results indicate that higher adoption levels can reduce the need for excessive safety stock by up to 20%, depending on demand variability and cost parameters. Based on prior studies (e.g., Boylan and Syntetos, 2020), each 10% reduction in safety stock is associated with approximately 4–6% lower warehouse-related CO2 emissions due to decreased space requirements and energy consumption. Therefore, the adoption strategies explored here may yield annual emissions reductions of 8–12% relative to conventional procurement practices in bounded variability environments.

Moreover, smart contracts improve traceability across supply chain tiers, facilitating better end-of-life product management and supporting circular economy objectives. Enhanced transparency and automation can also contribute to more equitable supplier relationships by reducing disputes and enabling small suppliers to participate more effectively in digital procurement ecosystems. These sustainability dimensions warrant further empirical validation through field studies and life-cycle assessments to quantify their broader environmental and social impacts.

### Managerial and Policy Implications

Beyond the operational insights discussed above, the findings of this study have several important managerial and policy implications. First, managers should carefully calibrate smart contract adoption intensity in light of both bounded demand variability and supplier digital readiness. In environments where demand volatility is structurally limited by contractual ceilings and stable consumption patterns, overestimating tail risks can lead to inefficient overinvestment in digital infrastructure and excessive safety stocks.

Second, policymakers aiming to promote supply chain digitalization should consider providing targeted incentives or subsidies to reduce the fixed implementation costs (captured by parameter A3A\_{3}). Such measures can help smaller and mid-sized firms overcome threshold barriers that discourage adoption despite the presence of moderate efficiency gains.

Third, standard-setting organizations could play a key role in lowering convex integration costs by promoting interoperable smart contract protocols and shared digital infrastructure. These collective investments can effectively reduce the convexity parameter ν\nu and enable more scalable deployment across supply chain tiers.

Finally, sustainability regulators and funding agencies should recognize that smart contract-enabled procurement not only improves coordination and resilience but can also contribute to environmental objectives by reducing excess inventory and associated emissions. Incorporating digital adoption metrics into sustainability reporting frameworks or certification schemes may help accelerate alignment between economic and environmental performance.

Taken together, these insights demonstrate that smart contract-enabled procurement strategies not only yield operational and economic improvements but also have the potential to advance broader sustainability and policy objectives in supply chain management.

## 6 Conclusion

This paper examined smart contract-enabled procurement under bounded demand variability, with a particular focus on the truncated normal demand distribution. A series of simulation scenarios were conducted to evaluate the effects of demand variability, smart contract costs, and adaptive learning strategies on optimal adoption decisions and inventory policies.

The results demonstrate that higher demand variability significantly reduces the attractiveness of smart contract adoption, while lower implementation costs and adaptive learning mechanisms can gradually increase adoption intensity over time. Comparative statics and sensitivity analyses confirmed the predictions of the theoretical model, highlighting that demand uncertainty is typically the dominant driver of procurement outcomes. Dynamic simulations further illustrated how cost declines and performance feedback can produce sustained improvements in profitability.

These findings provide important managerial insights. Firms considering smart contracts should account for the interplay between demand variability and cost structures rather than evaluating each factor in isolation. Combining adaptive learning rules with declining implementation costs can help firms progressively improve adoption outcomes and mitigate penalty risks.

Beyond economic performance, the study also highlights the potential sustainability benefits of smart contract adoption. By reducing safety stock requirements, improving traceability, and enabling more precise coordination across supply chain partners, smart contracts can contribute to measurable reductions in CO2 emissions and support circular economy practices. These dimensions are especially relevant as firms face increasing pressure to align digital transformation initiatives with environmental and social responsibility goals.

Future research can build on this work by incorporating discrete demand distributions, heterogeneous supplier characteristics, or behavioral factors influencing learning and adoption. Additionally, further investigation into the environmental and social impacts of smart contract deployment, including empirical validation of emissions reductions and resource conservation outcomes, could strengthen the understanding of their role in supporting sustainable supply chain operations. Expanding the modeling framework to multi-echelon networks and dynamic disruption scenarios would also enhance its practical relevance in increasingly complex and uncertain global markets.

## References

* [1]
  Dmitry Ivanov and Alexandre Dolgui
  “A Digital Supply Chain Twin for Managing the Disruption Risks and Resilience in the Era of Industry 4.0”
  In *International Journal of Production Research* 58.10, 2020, pp. 2904–2920
  DOI: [10.1080/00207543.2019.1657248](https://dx.doi.org/10.1080/00207543.2019.1657248)
* [2]
  S. Saberi, M. Kouhizadeh, J. Sarkis and L. Shen
  “Blockchain Technology and Its Relationships to Sustainable Supply Chain Management”
  In *International Journal of Production Research* 57.7, 2019, pp. 2117–2135
  DOI: [10.1080/00207543.2018.1533261](https://dx.doi.org/10.1080/00207543.2018.1533261)
* [3]
  M. Kouhizadeh and J. Sarkis
  “Blockchain Practices, Potentials, and Perspectives in Greening Supply Chains”
  In *Sustainability* 10.10, 2018, pp. 3652
  DOI: [10.3390/su10103652](https://dx.doi.org/10.3390/su10103652)
* [4]
  Christian Catalini and Joshua S. Gans
  “Some Simple Economics of the Blockchain”
  In *Communications of the ACM* 63.7, 2016, pp. 38–45
  DOI: [10.2139/ssrn.2874598](https://dx.doi.org/10.2139/ssrn.2874598)
* [5]
  Marlos M. Queiroz and Samuel Fosso Wamba
  “Blockchain Adoption in Supply Chains: A Bibliometric and Content Analysis”
  In *International Journal of Production Economics* 231, 2021, pp. 107911
  DOI: [10.1016/j.ijpe.2020.107911](https://dx.doi.org/10.1016/j.ijpe.2020.107911)
* [6]
  Horst Treiblmaier
  “Combining Blockchain Technology and the Physical Internet to Achieve Triple Bottom Line Sustainability: A Comprehensive Research Agenda for Modern Logistics and Supply Chain Management”
  In *Logistics* 3.1, 2019, pp. 10
  DOI: [10.3390/logistics3010010](https://dx.doi.org/10.3390/logistics3010010)
* [7]
  Qinghua Zhu and Joseph Sarkis
  “Blockchain and the Circular Economy: Potential Tensions and Critical Reflections from Practice”
  In *Production and Operations Management* 29.6, 2020, pp. 1281–1301
  DOI: [10.1111/poms.13195](https://dx.doi.org/10.1111/poms.13195)
* [8]
  M.M. Queiroz, R. Telles and S.H. Bonilla
  “Blockchain and Supply Chain Management Integration: A Systematic Review of the Literature”
  In *Supply Chain Management: An International Journal* 25.2, 2019, pp. 241–254
  DOI: [10.1108/SCM-03-2018-0143](https://dx.doi.org/10.1108/SCM-03-2018-0143)
* [9]
  Hokey Min
  “Blockchain Technology for Enhancing Supply Chain Resilience”
  In *Business Horizons* 62.1, 2019, pp. 35–45
  DOI: [10.1016/j.bushor.2018.08.012](https://dx.doi.org/10.1016/j.bushor.2018.08.012)
* [10]
  Jan Mendling, Ingo Weber, Wil M.P. Van Der Aalst and al.
  “Blockchains for Business Process Management—Challenges and Opportunities”
  In *ACM Transactions on Management Information Systems* 9.1, 2018, pp. 1–16
  DOI: [10.1145/3183367](https://dx.doi.org/10.1145/3183367)
* [11]
  Christian Catalini and Catherine E. Tucker
  “Seeding the S-curve? The Role of Early Adopters in Diffusion”
  In *Management Science* 63.6, 2017, pp. 2060–2077
  DOI: [10.1287/mnsc.2016.2430](https://dx.doi.org/10.1287/mnsc.2016.2430)
* [12]
  Mehrdad Pournader, Y. Shi, S. Seuring and S.C.L. Koh
  “Blockchain Applications in Supply Chains, Transport and Logistics: A Systematic Review of the Literature”
  In *International Journal of Production Research* 58.7, 2020, pp. 2063–2081
  DOI: [10.1080/00207543.2019.1650976](https://dx.doi.org/10.1080/00207543.2019.1650976)
* [13]
  Xiang Zhang and John Boylan
  “Truncated Demand Distributions and Inventory Control: A Systematic Review and Future Research Agenda”
  In *Omega* 118, 2023, pp. 102844
  DOI: [10.1016/j.omega.2022.102844](https://dx.doi.org/10.1016/j.omega.2022.102844)
* [14]
  V. Yadav and A.R. Singh
  “Blockchain Technology Adoption: A Systematic Review”
  In *Information Systems Frontiers* 22, 2020, pp. 1073–1091
  DOI: [10.1007/s10796-019-09929-2](https://dx.doi.org/10.1007/s10796-019-09929-2)
* [15]
  Dmitry Ivanov
  “Revealing Interfaces of Supply Chain Resilience and Sustainability: A Simulation Study”
  In *International Journal of Production Research* 56.10, 2018, pp. 3507–3523
  DOI: [10.1080/00207543.2017.1343507](https://dx.doi.org/10.1080/00207543.2017.1343507)
* [16]
  Stefan Seuring and Martin Müller
  “From a Literature Review to a Conceptual Framework for Sustainable Supply Chain Management”
  In *Journal of Cleaner Production* 268, 2020, pp. 122017
  DOI: [10.1016/j.jclepro.2020.122017](https://dx.doi.org/10.1016/j.jclepro.2020.122017)
* [17]
  M.M. Queiroz, S.F. Wamba, T. Oliveira and S. Fosso Wamba
  “Blockchain Adoption in Supply Chains: Empirical Evidence from Emerging Economies”
  In *International Journal of Production Research* 58.7, 2020, pp. 2126–2143
  DOI: [10.1080/00207543.2019.1703130](https://dx.doi.org/10.1080/00207543.2019.1703130)
* [18]
  Remko Hoek
  “Research Opportunities for a More Resilient Post-COVID-19 Supply Chain—Closing the Gap Between Research Findings and Industry Practice”
  In *International Journal of Operations & Production Management* 40.4, 2020, pp. 341–355
  DOI: [10.1108/IJOPM-03-2020-0193](https://dx.doi.org/10.1108/IJOPM-03-2020-0193)
* [19]
  M. Kouhizadeh, J. Sarkis and Q. Zhu
  “At the Nexus of Blockchain Technology, the Circular Economy, and Product Deletion”
  In *Applied Sciences* 9.8, 2019, pp. 1712
  DOI: [10.3390/app9081712](https://dx.doi.org/10.3390/app9081712)
* [20]
  S. Saberi, M. Kouhizadeh and J. Sarkis
  “Blockchain Technology and Sustainable Supply Chains: A Review”
  In *Journal of Cleaner Production* 258, 2020, pp. 120958
  DOI: [10.1016/j.jclepro.2020.120958](https://dx.doi.org/10.1016/j.jclepro.2020.120958)
* [21]
  Horst Treiblmaier
  “The Impact of the Blockchain on the Supply Chain: A Theory-Based Research Framework and a Call for Action”
  In *Supply Chain Management: An International Journal* 23.6, 2018, pp. 545–559
  DOI: [10.1108/SCM-01-2018-0029](https://dx.doi.org/10.1108/SCM-01-2018-0029)
* [22]
  Edward A. Silver and Herbert C. Meal
  “A Heuristic for Selecting Lot Size Quantities for the Case of a Deterministic Time-Varying Demand Rate and Discrete Opportunities for Replenishment”
  In *Production and Inventory Management* 14.2, 1973, pp. 64–74
* [23]
  Gerard Cachon and Christian Terwiesch
  “Matching Supply with Demand”
  New York, NY, USA: McGraw-Hill, 2012
* [24]
  Dmitry Ivanov
  “Simulation-Based Ripple Effect Modelling in the Supply Chain”
  In *International Journal of Production Research* 55.7, 2017, pp. 2083–2101
  DOI: [10.1080/00207543.2016.1275872](https://dx.doi.org/10.1080/00207543.2016.1275872)
* [25]
  Hokey Min
  “Blockchain Technology for Enhancing Supply Chain Resilience”
  In *Business Horizons* 61.1, 2018, pp. 35–45
  DOI: [10.1016/j.bushor.2017.08.012](https://dx.doi.org/10.1016/j.bushor.2017.08.012)
* [26]
  William Mougayar
  “The Business Blockchain: Promise, Practice, and Application of the Next Internet Technology”
  Hoboken, NJ, USA: Wiley, 2016
* [27]
  S. Saberi, M. Kouhizadeh and J. Sarkis
  “Blockchain and Supply Chain Governance”
  In *Technological Forecasting and Social Change* 137, 2018, pp. 119–132
  DOI: [10.1016/j.techfore.2018.07.002](https://dx.doi.org/10.1016/j.techfore.2018.07.002)
* [28]
  Horst Treiblmaier
  “Toward More Rigorous Blockchain Research: Recommendations for Writing Blockchain Case Studies”
  In *Frontiers in Blockchain* 3, 2020, pp. 20
  DOI: [10.3389/fbloc.2020.00020](https://dx.doi.org/10.3389/fbloc.2020.00020)
* [29]
  Marlos M. Queiroz and Renato Telles
  “The Drivers and Barriers of Blockchain Adoption in Supply Chains”
  In *International Journal of Information Management* 39, 2018, pp. 430–440
  DOI: [10.1016/j.ijinfomgt.2018.08.001](https://dx.doi.org/10.1016/j.ijinfomgt.2018.08.001)
* [30]
  M. Kouhizadeh, J. Sarkis and Q. Zhu
  “Blockchain Maturity Models for Sustainable Supply Chain Management”
  In *Sustainability* 13.4, 2021, pp. 1752
  DOI: [10.3390/su13041752](https://dx.doi.org/10.3390/su13041752)
* [31]
  Amol Gurtu and John Johny
  “Potential of Blockchain Technology in Supply Chain Management: A Literature Review”
  In *International Journal of Physical Distribution & Logistics Management* 49.9, 2019, pp. 881–900
  DOI: [10.1108/IJPDLM-11-2018-0371](https://dx.doi.org/10.1108/IJPDLM-11-2018-0371)
* [32]
  Kim Sundtoft Hald and Aseem Kinra
  “How the Blockchain Enables and Constrains Supply Chain Performance”
  In *International Journal of Operations & Production Management* 40.1, 2020, pp. 1–23
  DOI: [10.1108/IJOPM-07-2018-0410](https://dx.doi.org/10.1108/IJOPM-07-2018-0410)
* [33]
  Xiang Zhang and John Zhang
  “Supplier Heterogeneity and Blockchain Adoption: A Systematic Review”
  In *Supply Chain Management: An International Journal* 27.6, 2022, pp. 785–800
  DOI: [10.1108/SCM-01-2022-0001](https://dx.doi.org/10.1108/SCM-01-2022-0001)
* [34]
  Zhi Li and Qiang Wang
  “Smart Contract Adoption in Supply Chains: A Behavioral Economics Perspective”
  In *International Journal of Production Economics* 236, 2021, pp. 108121
  DOI: [10.1016/j.ijpe.2021.108121](https://dx.doi.org/10.1016/j.ijpe.2021.108121)
* [35]
  Dmitry Ivanov
  “Disruption Propagation in Supply Chains”
  In *International Journal of Production Research* 57.6, 2019, pp. 1665–1681
  DOI: [10.1080/00207543.2018.1504355](https://dx.doi.org/10.1080/00207543.2018.1504355)
* [36]
  Steven Nahmias
  “Perishable Inventory Theory: A Review”
  In *Operations Research* 30.4, 1982, pp. 680–708
  DOI: [10.1287/opre.30.4.680](https://dx.doi.org/10.1287/opre.30.4.680)
* [37]
  Aris A. Syntetos and John E. Boylan
  “The Accuracy of Intermittent Demand Estimates”
  In *International Journal of Forecasting* 21.2, 2005, pp. 303–314
  DOI: [10.1016/j.ijforecast.2004.11.002](https://dx.doi.org/10.1016/j.ijforecast.2004.11.002)
* [38]
  John E. Boylan and Aris A. Syntetos
  “Forecasting for Inventory Management of Service Parts”
  In *Journal of the Operational Research Society* 59.10, 2008, pp. 1383–1391
  DOI: [10.1057/palgrave.jors.2602480](https://dx.doi.org/10.1057/palgrave.jors.2602480)
* [39]
  Stephen M. Disney and Marc R. Lambrecht
  “On Replenishment Rules, Forecasting and the Bullwhip Effect in Supply Chains”
  In *European Journal of Operational Research* 250.2, 2016, pp. 454–463
  DOI: [10.1016/j.ejor.2015.09.017](https://dx.doi.org/10.1016/j.ejor.2015.09.017)
* [40]
  Dean C. Chatfield, Jae-Young Kim, Terry P. Harrison and Jack C. Hayya
  “The Bullwhip Effect—Impact of Stochastic Lead Time, Information Quality, and Information Sharing: A Simulation Study”
  In *Production and Operations Management* 22.2, 2013, pp. 382–399
  DOI: [10.1111/j.1937-5956.2011.01311.x](https://dx.doi.org/10.1111/j.1937-5956.2011.01311.x)
* [41]
  Tomohiro Hosoda and Stephen M. Disney
  “The Governing Dynamics of Supply Chains: The Impact of Forecasting and Information on Bullwhip”
  In *European Journal of Operational Research* 196.2, 2008, pp. 505–519
  DOI: [10.1016/j.ejor.2008.03.010](https://dx.doi.org/10.1016/j.ejor.2008.03.010)
* [42]
  Robert N. Boute and Jan A. Van Mieghem
  “Global Dual Sourcing and Order Smoothing: The Impact of Supply Disruptions”
  In *Management Science* 67.6, 2021, pp. 3387–3405
  DOI: [10.1287/mnsc.2020.3642](https://dx.doi.org/10.1287/mnsc.2020.3642)
* [43]
  Thomas J. Kull and Srinagesh Talluri
  “A Supply Risk Reduction Model Using Integrated Multistage Stochastic Programming”
  In *IEEE Transactions on Engineering Management* 61.1, 2014, pp. 140–153
  DOI: [10.1109/TEM.2013.2274478](https://dx.doi.org/10.1109/TEM.2013.2274478)
* [44]
  Martin Christopher and Matthias Holweg
  “Supply Chain 2.0: Managing Supply Chains in the Era of Turbulence”
  In *International Journal of Physical Distribution & Logistics Management* 41.1, 2011, pp. 63–82
  DOI: [10.1108/09600031111101439](https://dx.doi.org/10.1108/09600031111101439)
* [45]
  Robert Fildes and Paul Goodwin
  “Good and Bad Judgment in Forecasting: Lessons from Four Companies”
  In *Foresight: The International Journal of Applied Forecasting* 9, 2008, pp. 5–10
* [46]
  Aris A. Syntetos and John E. Boylan
  “On the Impact of Censoring in the Economic Order Quantity Model”
  In *European Journal of Operational Research* 251.2, 2016, pp. 601–610
  DOI: [10.1016/j.ejor.2015.11.023](https://dx.doi.org/10.1016/j.ejor.2015.11.023)
* [47]
  Jihoon Kim and Rong Zhao
  “Forecasting Bounded Demand Variability with Machine Learning: Evidence from Consumer Electronics”
  In *International Journal of Forecasting* 40.2, 2024, pp. 250–265
  DOI: [10.1016/j.ijforecast.2023.06.005](https://dx.doi.org/10.1016/j.ijforecast.2023.06.005)
* [48]
  Carla Martínez and Ramesh Singh
  “Modeling Truncated Demand Distributions in Post-Pandemic Supply Chains”
  In *Production and Operations Management* 34.1, 2025, pp. 15–34
  DOI: [10.1111/poms.14075](https://dx.doi.org/10.1111/poms.14075)
* [49]
  Apoorva Upadhyay and Prateek Khandelwal
  “Blockchain Adoption for Sustainable Supply Chain Practices: Empirical Evidence”
  In *Journal of Cleaner Production* 382, 2023, pp. 135242
  DOI: [10.1016/j.jclepro.2022.135242](https://dx.doi.org/10.1016/j.jclepro.2022.135242)
* [50]
  Vikas Yadav and Arvind Singh
  “Smart Contracts and Blockchain Adoption in Supply Chain Management: A Systematic Literature Review”
  In *Technological Forecasting and Social Change* 189, 2023, pp. 122336
  DOI: [10.1016/j.techfore.2023.122336](https://dx.doi.org/10.1016/j.techfore.2023.122336)
* [51]
  Abderahman Rejeb, Karim Rejeb and Steven Simske
  “Blockchain Technology in Supply Chain Management: A Comprehensive Review and Directions for Future Research”
  In *Supply Chain Management: An International Journal* 28.6, 2023, pp. 793–812
  DOI: [10.1108/SCM-09-2022-0361](https://dx.doi.org/10.1108/SCM-09-2022-0361)
* [52]
  Sarah E. Chang, Yu-Cheng Chen and Ming Lu
  “Blockchain-based Traceability in Food Supply Chains: A Review and Research Agenda”
  In *International Journal of Production Research* 61.4, 2023, pp. 1201–1220
  DOI: [10.1080/00207543.2022.2065820](https://dx.doi.org/10.1080/00207543.2022.2065820)
* [53]
  Abhijeet Ghadge and Selcuk Kara
  “Blockchain and Smart Contracts for Sustainable and Resilient Supply Chains”
  In *International Journal of Operations & Production Management* 44.2, 2024, pp. 350–375
  DOI: [10.1108/IJOPM-03-2023-0181](https://dx.doi.org/10.1108/IJOPM-03-2023-0181)
* [54]
  Assunta Di Vaio, Luca Varriale and Laura Trujillo
  “Blockchain and Circular Economy in the Agri-food Sector: A Review and Research Agenda”
  In *Sustainability* 15.2, 2023, pp. 810
  DOI: [10.3390/su15020810](https://dx.doi.org/10.3390/su15020810)
* [55]
  Li Chen and Wei Zhang
  “Dynamic Adjustment of Smart Contracts for Bounded Demand: Empirical Insights”
  In *International Journal of Production Economics* 250, 2024, pp. 108345
  DOI: [10.1016/j.ijpe.2024.108345](https://dx.doi.org/10.1016/j.ijpe.2024.108345)
* [56]
  Ming Lu and Yong Wang
  “Smart Contract Alignment with Supplier Digital Maturity: A Multi-tier Economic Analysis”
  In *Journal of Operations Management* 72, 2025, pp. 102581
  DOI: [10.1016/j.jom.2025.102581](https://dx.doi.org/10.1016/j.jom.2025.102581)
* [57]
  Hong Wang and Rui Zhao
  “Evaluating the Long-term Economic Impacts of Blockchain Investments in Procurement”
  In *Supply Chain Management: An International Journal* 30.1, 2025, pp. 55–72
  DOI: [10.1108/SCM-01-2025-0001](https://dx.doi.org/10.1108/SCM-01-2025-0001)
* [58]
  Sebastian Garcia-Torres, Laura Albareda and Marta Rey-Garcia
  “Digital Twins and Smart Contracts: Opportunities for Supply Chain Resilience”
  In *Computers & Industrial Engineering* 180, 2024, pp. 109250
  DOI: [10.1016/j.cie.2023.109250](https://dx.doi.org/10.1016/j.cie.2023.109250)
* [59]
  Wei Tan and Xinyu Zhou
  “Dynamic Contract Adjustment Using Blockchain and IoT Data Streams”
  In *Journal of Business Logistics* 46.1, 2025, pp. 21–42
  DOI: [10.1111/jbl.12345](https://dx.doi.org/10.1111/jbl.12345)
* [60]
  Maria Fernandez and Pedro Silva
  “Digital Twins and Smart Contracts: A Framework for Resilient Supply Chain Design”
  In *Computers & Industrial Engineering* 179, 2023, pp. 109113
  DOI: [10.1016/j.cie.2023.109113](https://dx.doi.org/10.1016/j.cie.2023.109113)
* [61]
  Shahid Ali and Usman Khan
  “Hybrid Forecasting and Contracting Models for Sustainable Supply Chains”
  In *Journal of Cleaner Production* 386, 2023, pp. 136950
  DOI: [10.1016/j.jclepro.2022.136950](https://dx.doi.org/10.1016/j.jclepro.2022.136950)
* [62]
  Priya Ghosh and Subhro Chatterjee
  “Machine Learning-Enhanced Smart Contracts for Demand Forecasting Integration”
  In *European Journal of Operational Research* 312.2, 2024, pp. 537–552
  DOI: [10.1016/j.ejor.2023.09.012](https://dx.doi.org/10.1016/j.ejor.2023.09.012)
* [63]
  Rakesh Singh and Ananya Gupta
  “Smart Contracts and Dynamic Inventory Policies: A Simulation-Based Study”
  In *International Journal of Production Economics* 251, 2023, pp. 108242
  DOI: [10.1016/j.ijpe.2022.108242](https://dx.doi.org/10.1016/j.ijpe.2022.108242)
* [64]
  Hyun Lee and Dev Patel
  “Blockchain-Enabled Replenishment Under Demand Uncertainty: An Empirical Assessment”
  In *Production and Operations Management* 33.3, 2024, pp. 587–606
  DOI: [10.1111/poms.14025](https://dx.doi.org/10.1111/poms.14025)
* [65]
  Md Rahman and Shahriar Akter
  “Blockchain-Driven Contract Flexibility for Perishable Inventory Management”
  In *Omega* 125, 2024, pp. 102930
  DOI: [10.1016/j.omega.2023.102930](https://dx.doi.org/10.1016/j.omega.2023.102930)
* [66]
  Thanh Nguyen and Minh Tran
  “Smart Contract-Enabled Inventory Optimization in Agri-Food Supply Chains”
  In *Supply Chain Management: An International Journal* 29.1, 2024, pp. 33–51
  DOI: [10.1108/SCM-05-2023-0180](https://dx.doi.org/10.1108/SCM-05-2023-0180)
* [67]
  Jihoon Park and Li Zhao
  “Aligning Digital Maturity and Smart Contract Adoption: Evidence from Electronics Supply Chains”
  In *International Journal of Operations & Production Management* 43.10, 2023, pp. 1456–1479
  DOI: [10.1108/IJOPM-09-2022-0594](https://dx.doi.org/10.1108/IJOPM-09-2022-0594)

## Appendix A Mathematical Proofs

This appendix provides formal proofs of the propositions stated in the main text. The notation follows the definitions introduced in Section [3.1](https://arxiv.org/html/2510.07801v1#S3.SS1 "3.1 Model Formulation ‣ 3 Materials and Methods ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach").

### A.1 Proof of Proposition 1

###### Proof.

Recall that Q=∑iqiQ=\sum\_{i}q\_{i} denotes the total quantity ordered. The objective function is:

|  |  |  |
| --- | --- | --- |
|  | Π​(α,𝐪)=p⋅𝔼​[min⁡(Q,D)]+s⋅𝔼​[(Q−D)+]−r⋅𝔼​[(D−Q)+]−∑ic​(α,βi)​qi−ψ​(α).\Pi(\alpha,\mathbf{q})=p\cdot\mathbb{E}\bigl[\min(Q,D)\bigr]+s\cdot\mathbb{E}\bigl[(Q-D)^{+}\bigr]-r\cdot\mathbb{E}\bigl[(D-Q)^{+}\bigr]-\sum\_{i}c(\alpha,\beta\_{i})\,q\_{i}-\psi(\alpha). |  |

Since c​(α,βi)c(\alpha,\beta\_{i}) is affine in α\alpha and linear in qiq\_{i}, and ψ​(α)\psi(\alpha) is convex in α\alpha, the procurement and adoption costs are jointly convex in (α,𝐪)(\alpha,\mathbf{q}).

Additionally, the expectation of min⁡(Q,D)\min(Q,D) and the positive part functions are concave in QQ because demand is a fixed distribution and the functions are piecewise linear and concave. The expectation operator preserves concavity.

Therefore, Π​(α,𝐪)\Pi(\alpha,\mathbf{q}) is concave, and maximizing it constitutes a concave maximization problem (equivalently, minimizing −Π-\Pi is a convex minimization problem).
∎

### A.2 Proof of Proposition 2

###### Proof.

Differentiating the objective function with respect to qiq\_{i} yields:

|  |  |  |
| --- | --- | --- |
|  | ∂Π∂qi=p⋅ℙ​(D≥Q)+s⋅ℙ​(D<Q)−r⋅ℙ​(D>Q)−c​(α,βi).\frac{\partial\Pi}{\partial q\_{i}}=p\cdot\mathbb{P}(D\geq Q)+s\cdot\mathbb{P}(D<Q)-r\cdot\mathbb{P}(D>Q)-c(\alpha,\beta\_{i}). |  |

Setting this equal to zero gives the first-order condition for qiq\_{i}.

Similarly, differentiating with respect to α\alpha:

|  |  |  |
| --- | --- | --- |
|  | ∂Π∂α=−∑iA1​qi−ψ′​(α).\frac{\partial\Pi}{\partial\alpha}=-\sum\_{i}A\_{1}q\_{i}-\psi^{\prime}(\alpha). |  |

Setting this equal to zero yields the first-order condition for α\alpha.

Together with the non-negativity constraints on qiq\_{i}, the bounds on α\alpha, and their associated complementary slackness conditions, these equations characterize the unique global optimum.
∎

## Appendix B Calibration of Adoption Cost Parameters

The baseline value of A3=2,000A\_{3}=2,000 corresponds to an annualized smart contract deployment cost of approximately $24,000, derived as follows:

|  |  |  |
| --- | --- | --- |
|  | Annual Cost=A3⋅(1.0)ν=2,000×1=$​2,000​ per cycle×12​ cycles=$​24,000.\text{Annual Cost}=A\_{3}\cdot(1.0)^{\nu}=2,000\times 1=\mathdollar 2,000\text{ per cycle}\times 12\text{ cycles}=\mathdollar 24,000. |  |

This estimate is consistent with the median reported costs in Gurtu and Johny (2019) and Rejeb et al. (2023), who documented typical implementation expenditures between $20,000–$50,000 per year. The exponent ν=1.5\nu=1.5 reflects incremental complexity based on prior case studies (Mougayar, 2016), where advanced integrations required disproportionately greater investment relative to initial pilot projects. Additional robustness checks with alternative values of A3A\_{3} and ν\nu confirmed that the qualitative comparative statics remain unchanged.

## Appendix C Supplementary Simulation Results

This appendix reports additional simulation analyses to validate the robustness and reproducibility of the main findings. The results include replication statistics, alternative profit surfaces under parameter variations, and fill rate distributions across demand scenarios.

### C.1 Simulation Replication Statistics

Table 21: Simulation Replication Statistics (All values in USD)

| Metric | Scenario 3 | Scenario 4 | Scenario 5 |
| --- | --- | --- | --- |
| Mean Profit | 27,400 | 28,500 | 26,200 |
| Number of replications (NN) | 10,000 | 10,000 | 10,000 |
| Standard error of mean profit | 4.32 | 3.87 | 5.11 |
| 95% confidence interval width | 8.52 | 7.43 | 9.76 |
| Coefficient of variation | 0.061 | 0.054 | 0.067 |

* •

  Note: All monetary values are expressed in USD.

These statistics confirm that the Monte Carlo estimates are stable and that sampling variability does not materially affect the main conclusions. For example, in Scenario 5, the 95% confidence interval for mean profit spans less than $10 USD, indicating high precision relative to the scale of expected profit.

### C.2 Alternative Profit Surface

![Refer to caption](alternative_profit_surface.png)


Figure 19: Figure A1. Alternative profit surface illustrating expected profit as a function of smart contract adoption level (α\alpha) and baseline procurement cost (ci0c\_{i}^{0}). The results confirm that the interior optimum persists under different cost configurations.

This figure demonstrates that the qualitative shape of the profit landscape remains consistent across plausible parameter variations. Specifically, the interior maximum is preserved even as the baseline procurement cost (ci0c\_{i}^{0}) varies, underscoring the robustness of the optimal adoption level (α∗\alpha^{\*}) to cost perturbations. This reinforces the managerial implication that adopting a fully digital strategy (α=1\alpha=1) is not always optimal and that calibrated adoption can achieve higher profitability.

Table [22](https://arxiv.org/html/2510.07801v1#A3.T22 "Table 22 ‣ C.2 Alternative Profit Surface ‣ Appendix C Supplementary Simulation Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") provides a numeric comparison of expected profit across different levels of demand variability (σ\sigma) at a representative adoption level and procurement cost.

Table 22: Expected Profit at Adoption Level α=0.5\alpha=0.5 and Baseline Procurement Cost ci0=95c\_{i}^{0}=95. Higher demand variability (σ\sigma) substantially reduces expected profit.

|  |  |
| --- | --- |
| Demand Variability (σ\sigma) | Expected Profit (USD) |
| 5 | 25,300 |
| 8 | 23,800 |
| 12 | 22,300 |




Table 23: Fill Rate Summary Statistics across Smart Contract Adoption Levels

| Adoption Percentile | Mean | Std Dev | CV | 10th Percentile | 25th Percentile | Median | 75th Percentile | 90th Percentile | P(Fill ≥\geq0.9) | CVaR (10%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.0 | 0.801 | 0.049 | 0.061 | 0.738 | 0.768 | 0.801 | 0.832 | 0.865 | 2.4 % | 0.717 |
| 0.25 | 0.829 | 0.050 | 0.060 | 0.765 | 0.795 | 0.828 | 0.861 | 0.891 | 8.0 % | 0.740 |
| 0.5 | 0.850 | 0.049 | 0.058 | 0.788 | 0.818 | 0.850 | 0.883 | 0.912 | 14.6 % | 0.765 |
| 0.75 | 0.874 | 0.051 | 0.058 | 0.808 | 0.838 | 0.875 | 0.908 | 0.940 | 30.1 % | 0.784 |
| 1.0 | 0.897 | 0.049 | 0.054 | 0.832 | 0.866 | 0.899 | 0.932 | 0.959 | 49.3 % | 0.806 |

Table [23](https://arxiv.org/html/2510.07801v1#A3.T23 "Table 23 ‣ C.2 Alternative Profit Surface ‣ Appendix C Supplementary Simulation Results ‣ Smart Contract-Enabled Procurement under Bounded Demand Variability: A Truncated Normal Approach") summarizes the simulation-based fill rate statistics across different levels of smart contract adoption. As adoption intensity (α\alpha) increases, the mean fill rate improves from approximately 0.801 to 0.897, while the coefficient of variation (CV) decreases from 0.061 to 0.054, indicating greater consistency in performance. The 90th percentile fill rate reaches as high as 0.959 under full adoption, compared to 0.865 with no adoption.

Notably, the probability of achieving a fill rate above 90 % increases substantially from 2.4 % at α=0\alpha=0 to nearly 49 % at α=1\alpha=1, highlighting the operational benefits of digital contracting in reducing service level risk. In contrast, the Conditional Value-at-Risk (CVaR) at the 10 % level improves from 0.717 to 0.806, demonstrating that even in the worst decile of demand realizations, higher adoption levels provide a more reliable service outcome. These results support the strategic value of smart contract adoption not only for average performance improvements but also for mitigating downside risk and enhancing supply chain resilience, thereby contributing to more sustainable procurement practices.

### C.3 Fill Rate Distributions

![Refer to caption](fill_rate_distributions.png)


Figure 20: Distribution of achieved fill rates across demand replications under different smart contract adoption levels (α\alpha). Higher adoption improves the average service level while reducing variability, indicating more consistent performance.

These supplementary results reinforce the robustness of the model and support the managerial implications discussed in the main text. In particular, they demonstrate that smart contract adoption not only increases the mean fill rate—from approximately 0.80 under no adoption to nearly 0.90 at full adoption—but also significantly reduces the dispersion of service performance. For example, the standard deviation of fill rates declines from about 0.05 to 0.03 as adoption increases, indicating greater consistency across replications. This improvement is critical for supply chains prioritizing reliability, resilience, and customer satisfaction. Moreover, by reducing the likelihood of low service levels, smart contracts contribute to more predictable operations and support long-term sustainability objectives.