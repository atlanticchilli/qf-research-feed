---
authors:
- Yuquan Li
- Yuexin Xiang
- Qin Wang
- Tsz Hon Yuen
- Andreas Deppeler
- Jiangshan Yu
doc_id: arxiv:2601.00196v1
family_id: arxiv:2601.00196
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'SoK: Stablecoins in Retail Payments *Yuexin Xiang is the corresponding author.'
url_abs: http://arxiv.org/abs/2601.00196v1
url_html: https://arxiv.org/html/2601.00196v1
venue: arXiv q-fin
version: 1
year: 2026
---


Yuquan Li1,
Yuexin Xiang2,∗,
Qin Wang3,
Tsz Hon Yuen2,
Andreas Deppeler4,
Jiangshan Yu5

###### Abstract

Stablecoins have emerged as a rapidly growing digital payment instrument, raising the question of whether blockchain-based settlement can function as a substitute for incumbent card networks in retail payments. This Systematization of Knowledge (SoK) provides a systematic comparison between stablecoin payment arrangements and card networks by situating both within a unified analytical framework. We first map their respective payment infrastructures, participant roles, and transaction lifecycles, highlighting fundamental differences in how authorization, settlement, and recourse are organized. Building on this mapping, we introduce the CLEAR framework, which evaluates retail payment systems across five dimensions: cost, legality, experience, architecture, and reach.

Our analysis shows that stablecoins deliver efficient, continuous, and programmable settlement, often compressing rail-level merchant fees and enabling 24/7 value transfer. However, these advantages are accompanied by an inversion of the traditional pricing and risk-allocation structure. Card networks internalize consumer-side frictions through subsidies, standardized liability rules, and post-transaction recourse, thereby supporting mass-market adoption. Stablecoin arrangements, by contrast, externalize transaction fees, error prevention, and dispute resolution to users, intermediaries, and courts, resulting in weaker consumer protection, higher cognitive burden at the point of interaction, and fragmented acceptance. Accordingly, stablecoins exhibit a conditional comparative advantage in closed-loop environments, cross-border corridors, and high-friction payment contexts, but remain structurally disadvantaged as open-loop retail payment instruments.

## I Introduction

Retail payments are end-user initiated transfers for routine commercial and personal purposes and are widely regarded as essential infrastructure for contemporary economic activity [[1](https://arxiv.org/html/2601.00196v1#bib.bib1), [2](https://arxiv.org/html/2601.00196v1#bib.bib2)]. They encompass the arrangements, instruments, and technical infrastructures that enable households and firms to initiate, authorize, and settle low-value transactions at scale. By reliably linking consumers, merchants, and financial intermediaries, these systems reduce checkout frictions and transaction costs while sustaining confidence in everyday exchange [[3](https://arxiv.org/html/2601.00196v1#bib.bib3), [1](https://arxiv.org/html/2601.00196v1#bib.bib1)]. Continued improvements in retail payment systems have further supported economic performance. Empirical evidence suggests a strong correlation between the adoption of efficient electronic instruments and higher economic output, consumption, and trade, particularly in markets where harmonization enhances system performance [[4](https://arxiv.org/html/2601.00196v1#bib.bib4)].

Retail payments in mature payment markets are dominated by card network payments, including card-present transactions and transactions initiated via mobile wallets [[5](https://arxiv.org/html/2601.00196v1#bib.bib5)]. Traditional card schemes, such as Visa and Mastercard, offer sub-second authorization, high reliability, and predictable settlement through standardized messaging and interbank clearing in central bank money [[6](https://arxiv.org/html/2601.00196v1#bib.bib6), [7](https://arxiv.org/html/2601.00196v1#bib.bib7)]. These systems have matured into a highly coordinated ecosystem of issuers, acquirers, and processors, bolstered by regulatory frameworks such as the Revised Payment Services Directive (PSD2) [[8](https://arxiv.org/html/2601.00196v1#bib.bib8)], which ensures competition, security, and consumer recourse.

However, a challenger ecosystem has emerged. Instead of the high-volatility assets that defined the early cryptocurrency market, stablecoin, a digital asset intended to maintain a stable value relative to a reference fiat currency through reserve or algorithmic models, has scaled rapidly as a potential alternative payment rail. By October 2025, the stablecoin supply exceeded $300 billion [[9](https://arxiv.org/html/2601.00196v1#bib.bib9)] as shown in Fig. [1](https://arxiv.org/html/2601.00196v1#S1.F1 "Figure 1 ‣ I Introduction ‣ SoK: Stablecoins in Retail Payments *Yuexin Xiang is the corresponding author."), with on-chain settlement volumes reaching approximately $8.9 trillion in the first half of the year [[10](https://arxiv.org/html/2601.00196v1#bib.bib10)]. At the application layer, the convergence of Web3 [[11](https://arxiv.org/html/2601.00196v1#bib.bib11)] and retail is accelerating. For example, the integration of OKX Pay’s stablecoin with GrabPay in Singapore demonstrates that stablecoin rails are increasingly being integrated into familiar Near Field Communication (NFC) and QR-based checkout flows [[12](https://arxiv.org/html/2601.00196v1#bib.bib12), [13](https://arxiv.org/html/2601.00196v1#bib.bib13), [14](https://arxiv.org/html/2601.00196v1#bib.bib14)].

![Refer to caption](stablecoin-mktcap.png)


Figure 1: Global stablecoin market capitalization with major depeg, regulatory, and infrastructure events highlighted

Stablecoins differ from other crypto-assets in that they are explicitly designed to maintain a stable value against a reference fiat currency, making them suitable for transactional use in retail payments. Their widespread adoption as settlement assets across exchanges and Decentralized Finance (DeFi) platforms [[15](https://arxiv.org/html/2601.00196v1#bib.bib15), [16](https://arxiv.org/html/2601.00196v1#bib.bib16), [17](https://arxiv.org/html/2601.00196v1#bib.bib17), [18](https://arxiv.org/html/2601.00196v1#bib.bib18)] demonstrates operational scalability, even though these contexts differ from point-of-sale commerce. Recent regulatory initiatives, including the Markets in Crypto-assets Regulation (MiCA) [[19](https://arxiv.org/html/2601.00196v1#bib.bib19)] and the GENIUS Act [[20](https://arxiv.org/html/2601.00196v1#bib.bib20)], further clarify issuance and conduct requirements, strengthening their relevance as regulated payment instruments. These features make stablecoins the most appropriate blockchain-based basis for comparison with card- and account-based payment networks.

Despite rapid growth in cross-border and institutional applications, the extent to which stablecoins can achieve functional parity with card networks at the retail Point of Sale (POS) remains uncertain. Prior studies highlight several dimensions along which decentralized payment rails differ structurally from centralized card networks. First, blockchain settlement does not always confer the same legal finality as card-scheme payments, and transaction reversibility is not natively supported at the protocol layer [[21](https://arxiv.org/html/2601.00196v1#bib.bib21), [22](https://arxiv.org/html/2601.00196v1#bib.bib22)]. Second, operational complexity continues to constrain merchant adoption, as access to crypto-fiat conversion, refund handling, and reconciliation remains less standardized than the workflows provided by traditional acquirers [[23](https://arxiv.org/html/2601.00196v1#bib.bib23), [24](https://arxiv.org/html/2601.00196v1#bib.bib24)]. Third, responsibility within stablecoin arrangements is distributed across different entities, including issuers, wallet providers, and infrastructure operators, while the underlying blockchains themselves do not bear contractual liability [[25](https://arxiv.org/html/2601.00196v1#bib.bib25), [26](https://arxiv.org/html/2601.00196v1#bib.bib26)]. Finally, systematic comparison is challenged by the absence of harmonized performance statistics, requiring analytical frameworks that can organize heterogeneous evidence and metrics across payment architectures [[27](https://arxiv.org/html/2601.00196v1#bib.bib27), [7](https://arxiv.org/html/2601.00196v1#bib.bib7), [28](https://arxiv.org/html/2601.00196v1#bib.bib28)].

While prior research has extensively analyzed stablecoins, existing Systematization of Knowledge (SoK) studies primarily examine them through design, economic, or security lenses, rather than as retail payment infrastructures. Early taxonomies such as Moin et al. [[29](https://arxiv.org/html/2601.00196v1#bib.bib29)] classify stablecoins by stabilization and collateral mechanisms, while broader surveys [[30](https://arxiv.org/html/2601.00196v1#bib.bib30)] integrate economic, regulatory, and technical perspectives without evaluating transaction-level payment performance. More recent security-focused frameworks [[31](https://arxiv.org/html/2601.00196v1#bib.bib31)] further concentrate on smart-contract and composability risks in DeFi. Consequently, the suitability and performance of stablecoins as retail payment rails remain insufficiently examined in prior SoK studies.

To address these gaps, this study compares stablecoin arrangements with card networks through a unified analytical perspective. It anchors this comparison in the CLEAR framework, which systematizes the evaluation of Cost, Legality, Experience, Architecture, and Reach.

The analysis focuses specifically on *asset-backed* stablecoins, which dominate current retail-oriented designs and provide the most direct counterpart to incumbent payment systems; algorithmic stablecoins are excluded because their historical instability makes them unsuitable as a basis for retail payment infrastructure (as the UST collapse noted in Fig. [1](https://arxiv.org/html/2601.00196v1#S1.F1 "Figure 1 ‣ I Introduction ‣ SoK: Stablecoins in Retail Payments *Yuexin Xiang is the corresponding author.")). Based on this framework, we address the following research questions (RQs):

* •

  RQ1: What are the core instruments, technical rails, and participant roles that differentiate stablecoin payment systems from card networks?
* •

  RQ2: How do stablecoin payment systems perform relative to card systems when assessed through the CLEAR framework?
* •

  RQ3:
  What institutional, governance, and interoperability conditions are required for stablecoins to match the levels of transaction assurance provided by card networks and enable large-scale retail adoption?

Contributions. Having established the analytical focus, this study advances three primary contributions:

* •

  We establish a common basis for comparison by aligning the transaction lifecycles of stablecoin-based payments and card networks.
* •

  We develop and apply the CLEAR framework to synthesize evidence on the strengths and limitations of both payment architectures.
* •

  We propose a measurement framework for assessing the conditions that would allow stablecoins to attain parity with card systems in retail payment.

Throughout this paper, the term *card networks/systems* refers to the underlying open-loop payment rails such as Visa that govern authorization, clearing, and settlement. Mobile wallets such as Apple Pay, as well as open-loop transportation payments that route transactions over these networks, are treated as user-facing interfaces within this architecture rather than as independent payment infrastructures.

The remainder of this paper is organized as follows. Section [II](https://arxiv.org/html/2601.00196v1#S2 "II Mapping Payment System Landscape ‣ SoK: Stablecoins in Retail Payments *Yuexin Xiang is the corresponding author.") outlines the retail payment landscape and establishes the basis for comparing stablecoin and card network models. Section [III](https://arxiv.org/html/2601.00196v1#S3 "III CLEAR: A Comparison Framework ‣ SoK: Stablecoins in Retail Payments *Yuexin Xiang is the corresponding author.") applies the CLEAR framework to evaluate their performance across five dimensions. Section [IV](https://arxiv.org/html/2601.00196v1#S4 "IV Discussion and Implications ‣ SoK: Stablecoins in Retail Payments *Yuexin Xiang is the corresponding author.") synthesizes these findings and sets out implications for stablecoin progress toward retail parity. Section [V](https://arxiv.org/html/2601.00196v1#S5 "V Conclusion ‣ SoK: Stablecoins in Retail Payments *Yuexin Xiang is the corresponding author.") summarizes our work.

## II Mapping Payment System Landscape

Comparison between stablecoin-based payments and card networks requires clarification of the payment infrastructures on which they operate. Differences in settlement architecture, governance, and transaction lifecycles shape core performance outcomes. Accordingly, we begin by mapping the evolution of retail payment infrastructures and situating both systems within a common analytical framework.

### II-A Payment Infrastructure

Retail payment systems have evolved from physical token exchange to account-based arrangements and, more recently, toward programmable value transfer. Economic research characterizes this evolution as a shift from token-based to account-based systems, reflecting persistent trade-offs among finality, scalability, and geographic reach [[32](https://arxiv.org/html/2601.00196v1#bib.bib32)]. Next, we present their evolution over time.

Cash and Paper Payments.
Early retail payment systems relied on physical tokens such as specie and cash and paper-based instruments such as cheques and giros. Cash offered immediate settlement finality in face-to-face settings but was constrained by physical materiality. Paper instruments allowed for remote payment but were operationally intensive: manual clearing processes produced settlement lags of several days and higher error rates [[1](https://arxiv.org/html/2601.00196v1#bib.bib1)]. Consequently, payment processing in this era was slow, locally fragmented, and costly for both banks and merchants.

Electronic Card Payments.
Since the 1970s, retail payments have increasingly migrated toward electronic, account-based infrastructures through card networks. Magnetic-stripe and later EMV cards established the four-party model with real-time authorization at the POS and deferred interbank settlement under standardized messaging (e.g., ISO 8583) [[33](https://arxiv.org/html/2601.00196v1#bib.bib33), [34](https://arxiv.org/html/2601.00196v1#bib.bib34), [35](https://arxiv.org/html/2601.00196v1#bib.bib35), [36](https://arxiv.org/html/2601.00196v1#bib.bib36), [6](https://arxiv.org/html/2601.00196v1#bib.bib6)]. Subsequent digital and mobile innovations in the 2010s, including tokenization and biometric authentication in wallets such as Apple Pay, improved security and user experience but largely preserved existing rails: authorization is near-instant, while merchant settlement remains batch-based, typically occurring one or two business days later [[7](https://arxiv.org/html/2601.00196v1#bib.bib7), [37](https://arxiv.org/html/2601.00196v1#bib.bib37), [38](https://arxiv.org/html/2601.00196v1#bib.bib38)].

Real-Time and Blockchain Payments.
In response to the latency of legacy cards and ACH rails, the payment landscape has bifurcated into two modernizing paths: central bank-coordinated real-time systems and decentralized blockchain infrastructures.

* •

  Real-Time Payment Systems. Many jurisdictions have introduced Real-Time Payment (RTP) systems (e.g., SEPA Instant [[39](https://arxiv.org/html/2601.00196v1#bib.bib39)], PIX [[40](https://arxiv.org/html/2601.00196v1#bib.bib40)], FedNow [[41](https://arxiv.org/html/2601.00196v1#bib.bib41)]) that enable 24/7 interbank settlement in central-bank money, substantially reducing settlement delays [[42](https://arxiv.org/html/2601.00196v1#bib.bib42), [43](https://arxiv.org/html/2601.00196v1#bib.bib43)]. While RTP improves the speed of legacy bank-based payment systems, integration into merchant checkout flows and card-like governance remains uneven.
* •

  Blockchain Settlement. In parallel, blockchain technology introduced a distinct settlement architecture. Bitcoin demonstrated peer-to-peer value transfer without a central clearinghouse using cryptographic consensus to prevent double spending [[44](https://arxiv.org/html/2601.00196v1#bib.bib44)]. Ethereum later extended this model by embedding smart contracts, enabling programmable and conditional transfers at the settlement layer [[45](https://arxiv.org/html/2601.00196v1#bib.bib45), [46](https://arxiv.org/html/2601.00196v1#bib.bib46), [47](https://arxiv.org/html/2601.00196v1#bib.bib47)].
* •

  Stablecoin Payments. Cryptocurrency volatility limited early blockchain assets as retail payment instruments [[48](https://arxiv.org/html/2601.00196v1#bib.bib48)], motivating the development of stablecoins. Stablecoins combine blockchain-based programmability with a price peg to fiat currencies, supported by heterogeneous backing assets [[30](https://arxiv.org/html/2601.00196v1#bib.bib30), [49](https://arxiv.org/html/2601.00196v1#bib.bib49), [50](https://arxiv.org/html/2601.00196v1#bib.bib50)], aiming to deliver monetary stability alongside global, continuous settlement [[28](https://arxiv.org/html/2601.00196v1#bib.bib28)].

This convergence makes the stablecoin model a natural point of comparison with the card network model. The two models are presented in sequence below.

### II-B Card Network Model (Fig. [2](https://arxiv.org/html/2601.00196v1#S2.F2 "Figure 2 ‣ II-B Card Network Model (Fig. 2) ‣ II Mapping Payment System Landscape ‣ SoK: Stablecoins in Retail Payments *Yuexin Xiang is the corresponding author."))

Card payments can be characterized as a rule-based and multi-sided payment arrangement linking the cardholder, merchant, issuer, and acquirer, coordinated through a card scheme that standardizes messaging, risk management, and settlement procedures [[51](https://arxiv.org/html/2601.00196v1#bib.bib51)]. The arrangement operates within an account-based ledger structure in which transaction authorization verifies credentials and funds availability, while the transfer of monetary value is completed through subsequent clearing and interbank settlement rather than at the moment of authorization [[52](https://arxiv.org/html/2601.00196v1#bib.bib52)].

Instruments.
In retail payments, mainstream instruments can be grouped into four categories that are commonly used in official payment statistics and monitoring frameworks of central banks and standard-setting bodies: card payments, credit transfers, direct debits, and prepaid balances [[53](https://arxiv.org/html/2601.00196v1#bib.bib53), [54](https://arxiv.org/html/2601.00196v1#bib.bib54)].

* •

  Card Payments [[55](https://arxiv.org/html/2601.00196v1#bib.bib55)]. Payments initiated using a physical or virtual card and routed through an open-loop card scheme. The underlying funds may be held in a bank deposit account or in an e-money account; however, the transaction is classified as a card payment because the card scheme rail is used at the POS. Under the four-party model, the issuer returns an authorization in seconds, while clearing and settlement occur subsequently under scheme rules and chargeback frameworks [[27](https://arxiv.org/html/2601.00196v1#bib.bib27)]. Examples include Visa, Mastercard, and UnionPay [[56](https://arxiv.org/html/2601.00196v1#bib.bib56)].
* •

  Credit Transfers [[57](https://arxiv.org/html/2601.00196v1#bib.bib57)]. Payments in which the payer instructs a Payment Service Provider (PSP) to push funds directly to the payee’s account over batch or instant rails. These instruments are widely used for bill payments and payroll, and, where instant rails and request-to-pay overlays exist, they can also support POS and e-commerce transactions. Examples include SEPA credit transfer [[39](https://arxiv.org/html/2601.00196v1#bib.bib39)], ACH, faster payments [[58](https://arxiv.org/html/2601.00196v1#bib.bib58)], and RTP.
* •

  Direct Debits [[59](https://arxiv.org/html/2601.00196v1#bib.bib59)]. Payments initiated by the payee, based on a prior mandate, to pull funds from the payer’s account on agreed dates. Scheme rulebooks govern mandate management, notifications, and dispute and refund rights, making direct debits the standard instrument for recurring payments such as utilities and subscriptions. Examples include SEPA direct debit [[60](https://arxiv.org/html/2601.00196v1#bib.bib60)] and Bacs direct debit [[61](https://arxiv.org/html/2601.00196v1#bib.bib61)].
* •

  Prepaid Payments [[62](https://arxiv.org/html/2601.00196v1#bib.bib62)]. Payments executed using prepaid value stored with an issuer and transferred within the issuer’s proprietary closed-loop infrastructure, rather than over open-loop card schemes or interbank transfer rails. The stored value represents a claim on the issuer and is accessed within the system’s own payment environment. Examples include transit cards and retailer gift cards [[63](https://arxiv.org/html/2601.00196v1#bib.bib63)].

Participants.
Card networks are commonly described using a four-party model [[64](https://arxiv.org/html/2601.00196v1#bib.bib64)], consisting of the consumer, the merchant, the issuer, and the acquirer. In practice, these bilateral relationships are coordinated through a card scheme that provides the rulebook and network infrastructure linking issuers and acquirers. Fig. [2](https://arxiv.org/html/2601.00196v1#S2.F2 "Figure 2 ‣ II-B Card Network Model (Fig. 2) ‣ II Mapping Payment System Landscape ‣ SoK: Stablecoins in Retail Payments *Yuexin Xiang is the corresponding author.") summarizes these roles and the associated transaction and fee flows. The arrangement therefore involves the following participants [[65](https://arxiv.org/html/2601.00196v1#bib.bib65), [66](https://arxiv.org/html/2601.00196v1#bib.bib66)]:

* •

  Consumer.
  The transaction is initiated by the consumer, who presents a payment card at the merchant’s POS or checkout interface. This action signals consent to transact and triggers the creation of a payment request addressed to the merchant. Upon receiving the authorization outcome relayed back through the network, the consumer receives confirmation of approval or decline. Economically, authorization commits the issuer to honor the payment, with actual monetary settlement deferred beyond the point of interaction.
* •

  Merchant.
  The merchant is the retailer selling goods or services [[67](https://arxiv.org/html/2601.00196v1#bib.bib67)]. Upon receiving the consumer’s payment initiation, the merchant submits the transaction details to its acquirer. This submission represents a pull request for funds, whereby the merchant asks the acquirer to obtain authorization and, ultimately, settlement from the issuer. After authorization is completed and the response is returned, the merchant proceeds with the delivery of goods or services. Depending on scheme rules, subsequent disputes may lead to reversal after authorization.
* •

  Acquirer. The acquirer (e.g., Worldpay [[68](https://arxiv.org/html/2601.00196v1#bib.bib68)], Stripe [[69](https://arxiv.org/html/2601.00196v1#bib.bib69)], and Adyen [[70](https://arxiv.org/html/2601.00196v1#bib.bib70)]) is the merchant-facing financial institution or processor that receives transaction submissions from merchants and forwards authorization requests into the card scheme network. Acting as the gateway to the scheme, it formats, validates, and routes transaction data, relays the authorization response back to the merchant, and subsequently participates in the settlement process under scheme rules. In exchange for these services, the acquirer charges the Merchant Discount Rate (MDR). [[71](https://arxiv.org/html/2601.00196v1#bib.bib71)].
* •

  Issuer.
  The issuer is the consumer’s bank and the ultimate decision-maker in the authorization process. After receiving the authorization request from the scheme, the issuer evaluates the transaction using account balance checks and fraud detection algorithms, then returns an approval or decline message formatted according to ISO 8583 [[35](https://arxiv.org/html/2601.00196v1#bib.bib35)]. The issuer maintains the ledger of the consumer’s deposit balance or credit line and assumes both credit risk, when cardholders fail to repay, and fraud risk, when unauthorized transactions occur. These services are compensated through interchange fees received from the acquirer.
* •

  Scheme.
  The scheme (e.g., Visa, Mastercard, and UnionPay [[72](https://arxiv.org/html/2601.00196v1#bib.bib72)]) operates the central routing and clearing infrastructure that connects acquirers and issuers. It forwards authorization requests from acquirers to issuers and relays issuer decisions back along the same path, while defining technical and operating standards and ensuring interoperability across participants. These functions are funded through scheme fees charged to participating institutions [[73](https://arxiv.org/html/2601.00196v1#bib.bib73)].

![Refer to caption](traditional-participants.png)


Figure 2: Card network model

Transaction Lifecycle.
The card network lifecycle can be decomposed into five sequential phases as shown in Fig. [3](https://arxiv.org/html/2601.00196v1#S2.F3 "Figure 3 ‣ II-B Card Network Model (Fig. 2) ‣ II Mapping Payment System Landscape ‣ SoK: Stablecoins in Retail Payments *Yuexin Xiang is the corresponding author."), highlighting the temporal separation between information processing and liquidity transfer [[27](https://arxiv.org/html/2601.00196v1#bib.bib27)].

![Refer to caption](lifecycle-card.png)


Figure 3: Lifecycle of card network model

1. 1.

   Initialization. A transaction is initiated at the Point of Interaction (POI) [[74](https://arxiv.org/html/2601.00196v1#bib.bib74)], where payment credentials are captured and transaction data are prepared for network processing [[75](https://arxiv.org/html/2601.00196v1#bib.bib75)]. At this stage, the system establishes the parameters required for subsequent authorization, but no account validation or value transfer occurs.
2. 2.

   Authorization. The authorization stage involves real-time account validation by the issuer. Upon receiving an authorization request routed through the acquirer and card network using standardized messaging formats such as ISO 8583 [[35](https://arxiv.org/html/2601.00196v1#bib.bib35)]. The issuer verifies card validity, available funds or credit, account status, and fraud controls, and returns an approval or decline decision within seconds [[76](https://arxiv.org/html/2601.00196v1#bib.bib76), [77](https://arxiv.org/html/2601.00196v1#bib.bib77)]. An approved authorization results in a temporary hold on the cardholder’s account, creating a conditional payment obligation under scheme rules [[76](https://arxiv.org/html/2601.00196v1#bib.bib76)]. At this stage, no interbank transfer of liquidity occurs; authorization is informational and contractual in nature, distinct from clearing and settlement, which occur subsequently [[27](https://arxiv.org/html/2601.00196v1#bib.bib27), [52](https://arxiv.org/html/2601.00196v1#bib.bib52)].
3. 3.

   Clearing. Clearing is the post-authorization process in which approved transactions are aggregated and reconciled by the card network, and net obligations between issuers and acquirers are calculated under scheme rules to form settlement positions, without yet transferring funds [[52](https://arxiv.org/html/2601.00196v1#bib.bib52), [27](https://arxiv.org/html/2601.00196v1#bib.bib27)].
4. 4.

   Settlement. Settlement is the stage at which payment obligations are discharged through the transfer of funds between parties [[52](https://arxiv.org/html/2601.00196v1#bib.bib52)]. In card payment systems, settlement typically occurs after clearing with a delay (often T+1 or T+2) [[78](https://arxiv.org/html/2601.00196v1#bib.bib78)], reflecting deferred net settlement arrangements and liquidity management practices rather than real-time value transfer [[78](https://arxiv.org/html/2601.00196v1#bib.bib78)]. At this stage, net positions between issuers and acquirers are settled using interbank money, most often through central bank settlement infrastructures such as Real-Time Gross Settlement systems (RTGS), completing the monetary leg of the transaction [[1](https://arxiv.org/html/2601.00196v1#bib.bib1)].
5. 5.

   Recourse. Distinctively, the card payment lifecycle remains open after settlement. Card scheme rules provide post-settlement dispute and chargeback mechanisms that allow issuers to reclaim funds from acquirers and merchants in cases such as fraud or non-delivery [[76](https://arxiv.org/html/2601.00196v1#bib.bib76)]. While interbank settlement is final at the infrastructure level, these contractual mechanisms permit subsequent reallocation of funds, rendering settlement economically final but legally conditional for end users [[79](https://arxiv.org/html/2601.00196v1#bib.bib79)].

### II-C Stablecoin Model (Fig. [4](https://arxiv.org/html/2601.00196v1#S2.F4 "Figure 4 ‣ II-C Stablecoin Model (Fig. 4) ‣ II Mapping Payment System Landscape ‣ SoK: Stablecoins in Retail Payments *Yuexin Xiang is the corresponding author."))

Instruments.
Stablecoins constitute the primary cryptocurrency payment asset for retail and on-chain settlement due to their price stability relative to fiat units of account [[80](https://arxiv.org/html/2601.00196v1#bib.bib80)]. However, stablecoin transactions do not operate in isolation: their issuance, transfer, and programmability are intrinsically dependent on other classes of crypto assets that support execution and protocol-level functionality [[17](https://arxiv.org/html/2601.00196v1#bib.bib17)].

* •

  Payment Layer: Stablecoins.
  Stablecoins are digital tokens designed to maintain a stable value relative to a reference asset [[20](https://arxiv.org/html/2601.00196v1#bib.bib20)], typically a fiat currency. Their price stability makes them suitable as a medium of exchange and unit of account for retail payments and on-chain settlement.
* •

  Execution Layer: Native Chains. Stablecoin issuance, transfer, and settlement are typically executed on public blockchains [[81](https://arxiv.org/html/2601.00196v1#bib.bib81)] (e.g., Ethereum and Solana [[82](https://arxiv.org/html/2601.00196v1#bib.bib82)]). These native chains provide consensus, transaction ordering, and finality [[83](https://arxiv.org/html/2601.00196v1#bib.bib83), [84](https://arxiv.org/html/2601.00196v1#bib.bib84)], while their associated native tokens are used to pay transaction fees and incentivize validators. As a result, the cost, latency, and reliability of stablecoin payments are directly shaped by the performance characteristics and congestion dynamics of the underlying chain.
* •

  Functionality Layer: Protocols. Within DeFi environments, stablecoins interact with smart contracts deployed on application protocols such as decentralized exchanges (DEXs) [[85](https://arxiv.org/html/2601.00196v1#bib.bib85)], lending platforms [[86](https://arxiv.org/html/2601.00196v1#bib.bib86)], and bridges [[87](https://arxiv.org/html/2601.00196v1#bib.bib87)]. These protocols are commonly associated with utility tokens that confer governance rights, access to protocol services, or eligibility for liquidity incentives. While such tokens are not used as means of payment at the POS, they support the circulation, composability, and programmability of stablecoins across applications.

Participants.
Stablecoin-based payment arrangements diverge from the structure of card networks. Rather than relying on a centralized issuer-acquirer-scheme hierarchy with contractual clearing and settlement obligations, stablecoin payments operate through a modular architecture composed of customers, issuers, blockchain networks, merchants, and intermediaries as shown in Fig. [4](https://arxiv.org/html/2601.00196v1#S2.F4 "Figure 4 ‣ II-C Stablecoin Model (Fig. 4) ‣ II Mapping Payment System Landscape ‣ SoK: Stablecoins in Retail Payments *Yuexin Xiang is the corresponding author.").

Each participant substitutes for a layer of the card payment stack, while reallocating authorization, settlement, and risk management functions from institutions to software and market-based intermediaries. This functional reallocation creates a responsibility vacuum: unlike the hierarchical card model in which the scheme acts as the ultimate contractual arbiter, the modular structure of stablecoin payments lacks a single entity that is accountable for end-to-end transaction success.

* •

  Customer.
  The customer initiates stablecoin payments using a wallet [[88](https://arxiv.org/html/2601.00196v1#bib.bib88)], which constructs and signs transfer instructions and submits them to the blockchain network for execution [[89](https://arxiv.org/html/2601.00196v1#bib.bib89)]. Payment is authorized by the user’s signature, and settlement occurs directly on the ledger as part of transaction execution. Custodial wallets operated by intermediaries perform compliance checks, transaction monitoring, and internal ledgering [[90](https://arxiv.org/html/2601.00196v1#bib.bib90), [91](https://arxiv.org/html/2601.00196v1#bib.bib91), [92](https://arxiv.org/html/2601.00196v1#bib.bib92)], whereas self-custodial wallets provide direct network access while placing operational responsibility on the user [[93](https://arxiv.org/html/2601.00196v1#bib.bib93), [94](https://arxiv.org/html/2601.00196v1#bib.bib94)].
* •

  Issuer.
  Stablecoin issuers such as Circle [[95](https://arxiv.org/html/2601.00196v1#bib.bib95)] and Tether [[96](https://arxiv.org/html/2601.00196v1#bib.bib96)], which issue USDC and USDT respectively [[97](https://arxiv.org/html/2601.00196v1#bib.bib97)], are responsible for minting and burning tokens in response to fiat deposits and redemptions [[98](https://arxiv.org/html/2601.00196v1#bib.bib98)]. Supply changes are effected on-chain through mint and burn transactions, while fiat settlement and custody occur off-chain via intermediaries. Unlike card issuers, stablecoin issuers do not authorize retail transactions or extend credit at the POS; their role is limited to maintaining reserve backing and ensuring redemption at par.
* •

  Blockchain Network.
  The blockchain network serves as the shared execution and settlement infrastructure of stablecoin payments, maintaining the canonical ledger, validating transactions, enforcing consensus rules, and producing settlement finality [[99](https://arxiv.org/html/2601.00196v1#bib.bib99), [100](https://arxiv.org/html/2601.00196v1#bib.bib100)]. Signed transactions are submitted, ordered, executed, and finalized on-chain, resulting in balance updates whose latency and finality depend on the underlying consensus design [[101](https://arxiv.org/html/2601.00196v1#bib.bib101), [102](https://arxiv.org/html/2601.00196v1#bib.bib102)]. Unlike card schemes, the blockchain network provides no contractual guarantees, chargeback mechanisms, or dispute resolution; settlement is technical rather than legal.
* •

  Merchant.
  Merchants accept stablecoin payments by receiving on-chain transfers and monitoring network confirmations. Merchant-facing software providers may assist with transaction detection, pricing, and reconciliation, but they do not assume the risk-sharing role of acquirers. Once a transaction is finalized on the blockchain, it becomes effectively irreversible, and merchants do not benefit from scheme-level fraud protection or chargeback rights [[103](https://arxiv.org/html/2601.00196v1#bib.bib103), [84](https://arxiv.org/html/2601.00196v1#bib.bib84), [104](https://arxiv.org/html/2601.00196v1#bib.bib104)]. Thus, fraud and operational risk are borne more directly by merchants and customers than in card systems.
* •

  Intermediary.
  Intermediaries, most prominently crypto exchanges [[105](https://arxiv.org/html/2601.00196v1#bib.bib105), [106](https://arxiv.org/html/2601.00196v1#bib.bib106)], serve as the primary interface between the fiat monetary system and the stablecoin ecosystem. They aggregate issuance and redemption demand on behalf of users and merchants and provide fiat-stablecoin conversion, interacting with issuers off-chain and submitting mint and burn instructions to the blockchain network [[107](https://arxiv.org/html/2601.00196v1#bib.bib107), [108](https://arxiv.org/html/2601.00196v1#bib.bib108)]. Functionally, intermediaries combine elements of acquirers and settlement banks in card networks, but operate without centralized scheme rules or mandated liability frameworks, making them critical for liquidity and the practical usability of stablecoins in retail payments.

![Refer to caption](stablecoin-participants.png)


Figure 4: Stablecoin model

Transaction Lifecycle.
The stablecoin payment lifecycle can be organized into five phases as shown in Fig. [5](https://arxiv.org/html/2601.00196v1#S2.F5 "Figure 5 ‣ II-C Stablecoin Model (Fig. 4) ‣ II Mapping Payment System Landscape ‣ SoK: Stablecoins in Retail Payments *Yuexin Xiang is the corresponding author."), reflecting how transaction creation, admissibility, ordering, and state transition are executed within a unified blockchain ledger. Unlike card systems, these functions are integrated at the protocol level, while the effective acceptance of payment depends on the underlying consensus design and confirmation policy.

![Refer to caption](lifecycle-coin.png)


Figure 5: Lifecycle of stablecoin model

1. 1.

   Initialization. A retail stablecoin payment begins when the consumer’s wallet retrieves the merchant’s receiving address, and constructs a transfer instruction. The user authorizes this instruction through a cryptographic signature [[109](https://arxiv.org/html/2601.00196v1#bib.bib109)]. In custodial settings, authorization may occur as an internal approval, with the provider signing and submitting the transaction on the user’s behalf.
2. 2.

   Validation. The transaction is propagated to the network, where nodes verify protocol-level admissibility, including signature correctness, nonce sequencing, and balance sufficiency [[110](https://arxiv.org/html/2601.00196v1#bib.bib110), [111](https://arxiv.org/html/2601.00196v1#bib.bib111)]. In parallel, custodial intermediaries may apply additional risk or compliance screening prior to submission. This stage determines whether a transaction is eligible for execution, rather than whether payment is economically accepted.
3. 3.

   Ordering. Admissible transactions are ordered into blocks or execution batches [[112](https://arxiv.org/html/2601.00196v1#bib.bib112), [113](https://arxiv.org/html/2601.00196v1#bib.bib113)]. In contrast to deferred, end-of-day clearing in card schemes, ordering in blockchain networks occurs continuously, establishing a canonical transaction sequence that directly determines ledger state transitions.
4. 4.

   Settlement. Upon acceptance of a block under the consensus mechanism, the ledger state is updated and balances are reassigned [[114](https://arxiv.org/html/2601.00196v1#bib.bib114), [115](https://arxiv.org/html/2601.00196v1#bib.bib115)]. In this sense, clearing and settlement are collapsed into a single atomic state transition. However, the strength of finality depends on the consensus model and confirmation depth, particularly under probabilistic-finality designs. Merchants therefore typically treat payment as complete only after a predefined confirmation policy is satisfied.
5. 5.

   Recourse. Because base-layer transfers rely on immutable ledgers and lack a network-wide adjudication authority, stablecoin payments do not support native chargebacks or scheme-mandated reversals [[103](https://arxiv.org/html/2601.00196v1#bib.bib103), [116](https://arxiv.org/html/2601.00196v1#bib.bib116)]. Corrective action generally requires a new transaction initiated by the recipient. While smart contracts or custodial platforms may implement escrow, dispute resolution, or rollback-like controls [[117](https://arxiv.org/html/2601.00196v1#bib.bib117), [118](https://arxiv.org/html/2601.00196v1#bib.bib118)], these mechanisms remain application-specific rather than properties of the settlement layer itself, creating a structural asymmetry relative to card systems.

### II-D Structural Comparison of Card and Stablecoin Systems

This section compares card networks and stablecoin payment systems at the model and lifecycle levels, clarifying how payment functions are organized and executed across participants.

Model Level Comparison. At the model level, card networks and stablecoin systems differ fundamentally in how coordination, authority, and responsibility are organized among participants. Card networks implement a hierarchical, institutionally coordinated architecture in which issuers, acquirers, and schemes perform clearly delineated roles under contractual rulebooks. Authorization authority, risk management, and settlement obligations are centralized within regulated intermediaries, while schemes provide standardized governance, messaging, and interoperability across the network.

Stablecoin payment systems adopt a modular, protocol-coordinated architecture. Core payment functions are distributed across token issuers, blockchain networks, wallets, and intermediaries, with execution and settlement embedded in software rather than enforced through bilateral contractual arrangements. Stablecoin issuers are responsible for minting, burning, and reserve management but do not authorize individual retail transactions. Blockchain networks execute and finalize transfers according to consensus rules while remaining operational infrastructure rather than contractual counterparties. Intermediaries such as custodial platforms and exchanges aggregate liquidity, compliance, and access to fiat systems on a discretionary, market-driven basis rather than under scheme-mandated obligations.

Therefore, card networks concentrate governance and responsibility within a small number of institutional actors, whereas stablecoin systems unbundle these functions across multiple technical and organizational layers. This difference does not imply superiority of one model over the other, but it produces distinct patterns of authority, accountability, and risk allocation that shape how each system operates in practice.

Lifecycle Level Comparison.
At the lifecycle level, the two systems diverge in how informational processing and value transfer are sequenced and finalized, as summarized in Table [I](https://arxiv.org/html/2601.00196v1#S2.T1 "TABLE I ‣ II-D Structural Comparison of Card and Stablecoin Systems ‣ II Mapping Payment System Landscape ‣ SoK: Stablecoins in Retail Payments *Yuexin Xiang is the corresponding author."). In card networks, authorization, clearing, and settlement are temporally separated. Issuer authorization provides an immediate but conditional payment signal, while clearing and net settlement occur subsequently through scheme-defined processes and interbank settlement arrangements. Even after settlement, transactions remain subject to post-settlement recourse under scheme rules, preserving the possibility of reversal through standardized dispute mechanisms.

In stablecoin systems, transaction validation, ordering, and settlement are integrated within a unified ledger execution process. Once a transaction satisfies protocol-level admissibility and is confirmed under the network’s consensus mechanism, balances are reassigned directly on-chain. Clearing and settlement are therefore collapsed into a single state transition, and finality is determined by technical confirmation rather than institutional agreement. Native mechanisms for chargeback or reversal are absent at the base layer; any corrective action must be implemented through subsequent transactions or application-specific controls outside the settlement layer itself.

These lifecycle differences reflect alternative design choices rather than differences in transaction stages per se. Card systems preserve legal and economic conditionality beyond settlement, whereas stablecoin systems emphasize atomic execution and ledger finality. Assessing whether these design choices support substitutability in retail payments therefore requires an explicit, function-oriented evaluation framework.

TABLE I: Alignment of Transaction Lifecycle Stages Across Card and Stablecoin Payment Systems

|  |  |  |
| --- | --- | --- |
| Stage | Card Network Model | Stablecoin Model |
| Initialization | •  Capture payment credentials at the POI. •  Construct an authorization request under scheme messaging standards such as ISO 8583. •  Populate transaction parameters for subsequent network processing. | •  Retrieve the merchant receiving address and construct a transfer instruction. •  Authorize the instruction through a cryptographic signature. •  Broadcast the signed transaction, or submit it via a custodial intermediary. |
| Authorization/Validation | •  Validate the payer account and assess available funds or credit. •  Apply issuer fraud screening and risk controls. •  Approve or decline and place an authorization hold without moving interbank liquidity. | •  Verify protocol admissibility, including signature correctness. •  Enforce transaction sequencing rules to prevent replay and preserve ordering. •  Confirm balance sufficiency and other protocol constraints prior to execution. |
| Clearing/Ordering | •  Aggregate authorized transactions into clearing batches. •  Compute obligations across issuers and acquirers, often on a net basis. •  Translate transaction records into settlement positions under scheme rules. | •  Continuously sequence admissible transactions under the network consensus mechanism. •  Commit the canonical execution order in blocks or execution batches. •  Determine state transitions directly from the committed transaction order. |
| Settlement | •  Transfer net obligations after clearing, typically T+1 to T+2. •  Settle in interbank money, commonly via central bank infrastructures such as RTGS. •  Treat settlement finality as legally conditional under scheme rules and dispute frameworks. | •  Update ledger state when a block is accepted under consensus. •  Reassign balances at the protocol level as an atomic state transition. •  Rely on the network finality model and merchant confirmation policy for effective acceptance. |
| Recourse | •  Provide dispute handling under scheme rulebooks. •  Allow chargebacks and adjustments that can reverse prior outcomes. •  Reallocate liability contractually after the original transaction. | •  Provide no native chargeback mechanism at the base ledger. •  Require corrective action through a subsequent transfer initiated by the recipient. •  Support escrow or dispute logic only through application-specific mechanisms. |

## III CLEAR: A Comparison Framework

As illustrated previously, a fundamental structural divergence separates incumbent card systems from emerging stablecoin arrangements, spanning both the organization of authority at the model level and the sequencing of validation, settlement, and recourse at the lifecycle level. While these differences clarify how transactions are executed and governed, they are insufficient on their own to determine whether stablecoins can effectively substitute for cards in retail payments.

The substitutability question is inherently functional rather than architectural. Retail payment adoption is widely understood as a coordination problem involving multiple stakeholder groups, in which improving performance along a single dimension is insufficient if frictions persist elsewhere in the payment chain [[119](https://arxiv.org/html/2601.00196v1#bib.bib119)]. Regardless of how coordination and settlement are implemented, a retail payment instrument must therefore satisfy a common set of performance requirements across key economic, legal, operational, and adoption dimensions. To evaluate whether stablecoin-based payments meet these requirements relative to card networks, we introduce the CLEAR framework:

* •

  C – Cost. Evaluates economic incentives for adoption. It compares the merchant-facing fee structures of card payment systems with the transaction cost dynamics of stablecoin-based payments, including protocol fees and network congestion effects.
* •

  L – Legality. Evaluates the strength of the legal and regulatory safety net. It examines the trade-off between the ex post consumer protections embedded in card networks, such as chargebacks and dispute resolution, and the settlement finality characteristic of blockchain-based payments.
* •

  E – Experience. Evaluates user-facing friction at the POI. It compares the speed, predictability, and usability of card-based interactions with the wallet-based transaction approval processes required in stablecoin payments.
* •

  A – Architecture. Evaluates systemic and operational risk. It contrasts the centrally governed security and liability structures of card schemes with the distributed execution environments of stablecoin systems, where risk is fragmented across custodial, protocol, and infrastructure layers.
* •

  R – Reach. Evaluates network effects and adoption constraints. It assesses the difficulty of coordinating merchants and users in a fragmented stablecoin ecosystem relative to the near-universal acceptance achieved by established card networks.

### III-A Cost: The Inversion of the Pricing Structure

The divergence between card and stablecoin payment models is most economically visible in how transaction costs are allocated across market sides. Drawing on the theory of two-sided markets [[120](https://arxiv.org/html/2601.00196v1#bib.bib120), [119](https://arxiv.org/html/2601.00196v1#bib.bib119)], we argue that the key distinction lies in an inversion of the pricing structure: card networks subsidize the payer side while recovering costs from merchants, whereas stablecoin-based payments reduce certain merchant-facing charges at the rail level but introduce payer-facing marginal costs and operational frictions that weaken the subsidy mechanism underpinning modern retail payment habits. These differences generate contrasting patterns of cost incidence, pricing structure, and user-facing frictions.

Merchant Acceptance Cost. This dimension captures the marginal fee burden imposed on the merchant at the point of settlement. In card-based payment systems, the dominant merchant-facing charge is the MDR, expressed as a percentage of the transaction value deducted during settlement. MDR aggregates multiple underlying components, including interchange paid to the issuing bank, network or scheme fees, and acquirer or processor markups.

Card – Merchant Discount Rate. In the United States (US), the MDR, which comprises interchange, scheme, and processor fees [[121](https://arxiv.org/html/2601.00196v1#bib.bib121)], typically ranges from about 1% to 3% of the transaction value in 2025 [[122](https://arxiv.org/html/2601.00196v1#bib.bib122)].
By contrast, under the European Union’s Interchange Fee Regulation (IFR), the interchange component of the MDR, which is the single largest fee element in card schemes, is capped at 0.2% for consumer debit cards and 0.3% for consumer credit cards [[123](https://arxiv.org/html/2601.00196v1#bib.bib123)].
The regulation substantially compresses average merchant acceptance costs relative to the US, although total MDR remains heterogeneous across merchant categories, card types, and acquirer contracts [[3](https://arxiv.org/html/2601.00196v1#bib.bib3), [124](https://arxiv.org/html/2601.00196v1#bib.bib124)].
Importantly, MDR is not merely a toll: it finances cross-subsidization within the two-sided platform. As formalized by Rochet and Tirole [[120](https://arxiv.org/html/2601.00196v1#bib.bib120)], interchange allows issuers to subsidize consumer participation through rewards, grace periods, and fraud and liability services, helping the platform overcome the initial coordination problem of adoption. Merchants therefore pay a premium to access a broad base of consumers and the liquidity provided by issuer credit lines.

Stablecoin – Disintermediated Transfer with Re-intermediation. Stablecoin transfers remove interchange and scheme fee layers at the rail level by settling on a public ledger. In a direct transfer, the recipient-side fee is typically zero, while marginal on-chain costs are borne by the sender via gas fees. In practice, however, most retail merchants require custodial processors for compliance, key management, accounting, and often automated conversion to fiat. These services typically charge a percentage fee that functions as a de facto floor for crypto acceptance costs [[125](https://arxiv.org/html/2601.00196v1#bib.bib125)]. The resulting model resembles fee-for-service payment processing rather than fee-for-credit intermediation.

While stablecoins can therefore reduce certain acceptance fees in principle, they also weaken a key element of the card value proposition: the integration of consumer credit and its associated subsidy. In their baseline transfer form, stablecoins behave closer to digital cash than to digital credit, which may limit their ability to stimulate credit-fueled consumption absent an additional credit layer.

Consumer Transaction Cost.
This dimension evaluates the marginal cost and operational burden imposed on the payer at the point of transaction.

Card – Near-zero Marginal Cost at POI. In the card model, consumers typically face zero marginal fees at the point of interaction, while issuer competition for top-of-wallet status often takes the form of rewards and float (e.g., an interest-free grace period). In two-sided market terms, these features constitute a subsidy or negative price on the payer side, facilitating network take-up [[120](https://arxiv.org/html/2601.00196v1#bib.bib120)]. Consumer costs may still arise indirectly (e.g., through interest on revolving credit or price pass-through by merchants), but they are not typically levied as a per-transaction charge at POI.

Stablecoin – Resource Metering and Asset Mismatch. In blockchain-based payments, users (or their service providers) must fund state changes via network transaction fees (e.g., gas), which reflect the computational resources required to execute and record transfers [[45](https://arxiv.org/html/2601.00196v1#bib.bib45)]. Unlike fixed banking fees, gas prices are determined in a market for block space and can vary with network conditions [[126](https://arxiv.org/html/2601.00196v1#bib.bib126)]. Layer-2 (L2) scaling solutions can compress average fees materially by batching transactions on a Layer-1 chain [[127](https://arxiv.org/html/2601.00196v1#bib.bib127), [128](https://arxiv.org/html/2601.00196v1#bib.bib128)], though fee levels remain contingent on network design and congestion [[129](https://arxiv.org/html/2601.00196v1#bib.bib129)]. A structural friction nonetheless remains in many settings: fees must often be paid in the network’s native asset (e.g., ETH), even when the transfer amount is denominated in a stablecoin. This fee-payment asset mismatch forces users to maintain balances in volatile native tokens to enable stablecoin payments, increasing operational complexity relative to single-asset card interactions [[130](https://arxiv.org/html/2601.00196v1#bib.bib130)].

Thus, the cost dimension highlights an adoption-relevant reallocation: card networks externalize marginal frictions away from the payer at POI, whereas stablecoin payments tend to reintroduce payer-facing costs and wallet-management burdens unless fees are abstracted or subsidized by intermediaries.

Liquidity and Boundary Cost.
This dimension evaluates the cost of converting the settlement asset into working capital usable for routine fiat-denominated expenses.

Card – Integrated Liquidity. Card settlement ultimately delivers commercial bank money in the merchant’s domestic unit of account, enabling immediate use for taxes, wages, rent, and suppliers. For domestic transactions, conversion is typically not required; cross-border transactions can incur additional premia, often attributed to cross-region interchange schedules, network assessment fees, and processor currency conversion markups [[131](https://arxiv.org/html/2601.00196v1#bib.bib131), [132](https://arxiv.org/html/2601.00196v1#bib.bib132), [133](https://arxiv.org/html/2601.00196v1#bib.bib133)].

Stablecoin – Segregated Liquidity. Stablecoin settlement delivers a tokenized asset distinct from the merchant’s fiat working-capital needs, creating a boundary that must be crossed unless the merchant operates within a crypto-native value chain. Off-ramping introduces renewed intermediation and typically involves (i) exchange or processor spreads/fees and (ii) banking frictions such as wire fees and settlement delays [[134](https://arxiv.org/html/2601.00196v1#bib.bib134)].

This comparison suggests a total cost of ownership (TCO) [[135](https://arxiv.org/html/2601.00196v1#bib.bib135)] perspective: lower rail-level acceptance costs may be offset by conversion and reconciliation costs when merchants ultimately require fiat liquidity. Consequently, stablecoins realize their clearest cost advantage in a closed-loop environment where incoming stablecoins can be redeployed to pay suppliers without repeatedly crossing the crypto-fiat boundary [[125](https://arxiv.org/html/2601.00196v1#bib.bib125)].

Cost Level Finding
*The important cost distinction is not settlement efficiency but cost incidence.*
Card networks subsidize consumers and recover costs from merchants, with interchange financing credit provision, fraud protection, and consumer guarantees. Stablecoin systems remove interchange and some merchant-side fees, but also remove the mechanism that funds these subsidies, shifting costs to users through transaction fees, liquidity fragmentation, and off-ramping. Consequently, stablecoins currently resemble digital cash rather than a retail credit instrument, performing well in closed loops but remaining disadvantaged in open-loop retail settings.

### III-B Legality: The Protection-Finality Trade-off

This dimension evaluates how payment systems allocate liability and define the moment at which obligations are discharged. In line with the payments-economics literature [[79](https://arxiv.org/html/2601.00196v1#bib.bib79), [32](https://arxiv.org/html/2601.00196v1#bib.bib32)], these issues reflect a fundamental design tension: systems must balance reversibility, which protects users from fraud and error, with settlement finality that protects the wider system from credit and insolvency risk. Card networks and stablecoin arrangements resolve this trade-off through radically different institutional mechanisms. These differences result in contrasting allocations of liability, protection, and settlement finality.

Consumer Protection and Recourse.
This part analyzes the allocation of liability when a transaction is unauthorized, fraudulent, or disputed.

Card – Statutory Protection. In card systems, strong consumer protection is embedded in law and scheme rules. Under PSD2 in Europe and regulation in US, consumer liability for unauthorized transactions is strictly capped, and issuers are mandated to reimburse cardholders promptly. Chargebacks operationalize this protection. When a dispute is filed, the issuer must provisionally credit the payer and recover the amount from the merchant. In economic terms, the network mutualizes fraud risk by shifting the burden toward merchants, a mechanism consistent with platform theories of optimal liability allocation [[120](https://arxiv.org/html/2601.00196v1#bib.bib120), [21](https://arxiv.org/html/2601.00196v1#bib.bib21)].

Stablecoin – Asset Safeguards and Transfer Risk. The regulatory approach for stablecoins, exemplified by the EU’s MiCA regulation, focuses on the issuer rather than the transaction, protects the asset but not the transfer.

* •

  *Asset Protection:* MiCA imposes strict requirements on issuers of EMTs and ARTs. It mandates that issuers maintain 1:1 reserves and grants holders a permanent right of redemption at par [[19](https://arxiv.org/html/2601.00196v1#bib.bib19)]. This protects the user from issuer insolvency or de-pegging.
* •

  *Transfer Risk:* However, regulations generally do not mandate reimbursement for user errors or “Authorized Push Payment” fraud. Because the user controls the private key and signs the instruction, the protocol treats the transaction as valid. There is no protocol-level administrator with a general statutory obligation or native technical capability to reverse an individual transfer once confirmed on the ledger. [[136](https://arxiv.org/html/2601.00196v1#bib.bib136)].

Beyond the EU’s MiCA framework, the US, Singapore, and Hong Kong have each introduced stablecoin-specific regulatory regimes, reflecting a coordinated shift toward treating stablecoins as regulated payment instruments rather than speculative crypto-assets. Across these jurisdictions, regulation converges on full reserve backing, issuer licensing, and enforceable redemption rights. In the US, initiatives under the GENIUS Act emphasize reserve composition and supervisory oversight without introducing card-scheme-style dispute resolution mechanisms [[20](https://arxiv.org/html/2601.00196v1#bib.bib20)]. Monetary Authority of Singapore (MAS) similarly prioritizes reserve backing and redemption rights for single-currency stablecoins while preserving on-chain transfer finality [[137](https://arxiv.org/html/2601.00196v1#bib.bib137)], and Hong Kong’s proposed regime focuses on issuer authorization and governance rather than post-settlement consumer recourse [[138](https://arxiv.org/html/2601.00196v1#bib.bib138)].

However, this convergence is largely issuer- and asset-centric rather than transaction-centric. While prevailing regimes ensure that stablecoins are prudently managed and redeemable at par, they provide limited safeguards once a payment has been executed. Transfers authorized at the wallet or protocol level are typically treated as final, even when induced by error or fraud, with no statutory obligation or native system mechanism for reversal. Unlike card networks, which mutualize fraud and dispute risk through issuer guarantees and scheme-level rules, stablecoin systems largely externalize transfer risk to end users, particularly in non-custodial settings, shifting the burden of security and error prevention from the payment system to the individual consumer. This structural distinction underpins the persistent legal and assurance gap between stablecoin-based payments and mature card-based retail payment systems.

Settlement Finality and Enforceability.
This dimension evaluates the legal moment when a payment obligation is irrevocably discharged.

Card – Designated Finality. Under frameworks such as the EU Settlement Finality Directive (SFD) [[139](https://arxiv.org/html/2601.00196v1#bib.bib139)], payment systems designate a precise moment, usually the posting of entries at the central bank, after which transfers are legally irrevocable and protected from clawback, even in insolvency. This deterministic finality is foundational to modern clearing and settlement [[52](https://arxiv.org/html/2601.00196v1#bib.bib52)].

Stablecoin – Probabilistic Finality. Stablecoins rely on blockchain consensus mechanisms that provide technical finality, including probabilistic finality in Proof-of-Work (PoW) [[140](https://arxiv.org/html/2601.00196v1#bib.bib140)] systems and economic finality in Proof-of-Stake (PoS) [[141](https://arxiv.org/html/2601.00196v1#bib.bib141)] systems, among others. While blocks become effectively irreversible after sufficient confirmations, this technical finality is not equivalent to legal finality. As noted by Nabilou [[25](https://arxiv.org/html/2601.00196v1#bib.bib25)], courts may recognize a payer’s claim even when the protocol cannot reverse the transfer, creating a mismatch between on-chain reality and off-chain legal obligations.

This dichotomy creates a strategic trade-off for merchants. Card network rails provide high legal certainty within established banking and legal frameworks, but expose merchants to post-settlement reversibility through consumer-initiated chargebacks. Stablecoin rails invert this balance: settlement is immediate and technically irreversible, offering strong operational certainty, yet the legal finality of payment remains ambiguous, particularly regarding whether the underlying obligation is definitively discharged under existing insolvency and commercial law.

Data Privacy and Compliance. A third legal friction exists regarding the compatibility of ledger architectures with data protection laws.

Card – Private Ledgers. Card network systems rely on private, centrally administered bank and network ledgers rather than publicly replicated state. Transaction data are held in controlled databases operated by issuers, acquirers, and card networks under contractual and regulatory governance. This centralized architecture is inherently compatible with the General Data Protection Regulation (GDPR), including the “Right to be Forgotten” [[142](https://arxiv.org/html/2601.00196v1#bib.bib142)], as intermediaries can selectively delete or anonymize records upon valid erasure requests without affecting system operation, ensuring compliance through institutional governance rather than protocol-level design.

Stablecoin – Public Verification. Public permissionless blockchains [[143](https://arxiv.org/html/2601.00196v1#bib.bib143)] function by broadcasting transaction details to a globally distributed network of nodes. Once data is written to the blockchain, it is technically impossible to erase. Even if the user’s identity is pseudonymous, represented only by a wallet address, metadata analysis can often re-identify individuals [[144](https://arxiv.org/html/2601.00196v1#bib.bib144), [145](https://arxiv.org/html/2601.00196v1#bib.bib145)]. This immutability creates a direct tension with GDPR requirements for data erasure and rectification [[146](https://arxiv.org/html/2601.00196v1#bib.bib146)].

According to the above analysis, stablecoins face a compliance paradox. To be useful for retail payments, they require the transparency of a public ledger to ensure trust without an intermediary. Yet, this very transparency renders them potentially non-compliant with strict privacy regimes. Thus, widespread retail adoption may ultimately depend on the successful integration of privacy-preserving compliance mechanisms, including privacy-enhancing technologies such as Zero-Knowledge Proofs (ZKPs) [[147](https://arxiv.org/html/2601.00196v1#bib.bib147), [148](https://arxiv.org/html/2601.00196v1#bib.bib148)], Secure Multiparty Computation (SMPC) [[149](https://arxiv.org/html/2601.00196v1#bib.bib149), [150](https://arxiv.org/html/2601.00196v1#bib.bib150)], and Trusted Execution Environments (TEEs) [[151](https://arxiv.org/html/2601.00196v1#bib.bib151), [152](https://arxiv.org/html/2601.00196v1#bib.bib152)], rather than on the base ledger design alone.

Legality Level Finding
*The decisive legal distinction in retail payments lies in whether protection is applied at the transaction level or confined to the asset level.*
Card networks embed consumer protection directly into transaction processing through chargebacks, issuer guarantees, and scheme-level rulebooks that mutualize dispute risk across the system. Stablecoin regimes, by contrast, prioritize issuer solvency and redemption while preserving on-chain transfer finality. Without a network-wide rulebook or designated authority to adjudicate disputes, stablecoin payment systems remain institutionally incomplete, externalizing transfer risk to users and turning technical finality into a material business risk in open-loop retail payments.

### III-C Experience: The Perception-Performance Gap

The experience dimension synthesizes subjective perceptions such as trust, usability, and perceived security with objective system performance such as latency and reliability. Literature rooted in the Technology Acceptance Model (TAM) [[153](https://arxiv.org/html/2601.00196v1#bib.bib153)] and the Unified Theory of Acceptance and Use of Technology (UTAUT) [[154](https://arxiv.org/html/2601.00196v1#bib.bib154)] consistently finds that adoption hinges less on technical capability and more on perceived usefulness, perceived security, and ease of use, which are constructs that shape both intention and actual usage [[155](https://arxiv.org/html/2601.00196v1#bib.bib155)]. These perceptual factors serve as economic complements to institutional assurances such as liability protection and settlement finality. These differences give rise to contrasting perceptions of security, usability, and reliability.

Consumer Perception and the Demand Side.
This part evaluates the psychological and structural barriers facing the payer.

Card – Structural Assurance. Consumers favor payment methods perceived as secure, simple, and useful. In mature markets, card networks benefit from what Sangari and Mashatan [[156](https://arxiv.org/html/2601.00196v1#bib.bib156)] define as tradition-related barriers regarding challengers: the user’s preference for familiar methods is reinforced by deep structural assurances such as clear governance, defined recourse, and reliable intermediation. These assurances lower the threshold for trust, allowing intention to translate directly into use without significant cognitive resistance.

Stablecoin – Consumer Resistance. Barriers to adoption remain substantial. Although awareness of stablecoins is high, uptake is constrained by consumer resistance.
A multi-analytical study by Sangari and Mashatan [[156](https://arxiv.org/html/2601.00196v1#bib.bib156)] shows that price volatility is not the sole impediment; rather, it intensifies underlying concerns related to the absence of structural assurances, including unclear protections and opaque governance.
User-centered security studies further clarify the experiential mechanisms behind this resistance: while users associate stablecoins with price stability and perceived regulatory alignment, they remain uncertain about reserve transparency, governance, and failure modes across different stablecoin designs, and must actively perform risk assessment and mitigation in the absence of institutional guarantees [[157](https://arxiv.org/html/2601.00196v1#bib.bib157), [158](https://arxiv.org/html/2601.00196v1#bib.bib158)].
In the absence of such assurances, security and privacy concerns increase, reinforcing consumers’ reliance on established payment methods.

This resistance is reflected in a persistent gap between awareness and use. Survey evidence shows that awareness can be widespread, yet ownership and transactional use remain limited. For example, Canadian survey evidence reports that roughly 64% of respondents were aware of Bitcoin in 2017, while only about 2.9% reported owning it[[159](https://arxiv.org/html/2601.00196v1#bib.bib159)], and often motivated by investment rather than payment needs [[160](https://arxiv.org/html/2601.00196v1#bib.bib160), [161](https://arxiv.org/html/2601.00196v1#bib.bib161)].

Evidence from the hospitality sector further underscores this pattern. Quan and coauthors [[155](https://arxiv.org/html/2601.00196v1#bib.bib155)] find that perceived security and ease of use are the dominant determinants of trust. The operational complexity of managing private keys in self-custodial stablecoin systems fails to meet the ease-of-use threshold required to displace mobile wallets in high-frequency retail environments.

The broader literature consistently shows that trust mediates the relationship between technology and user intention. Stablecoins currently exhibit a trust deficit: although they provide functional advantages such as speed and global reach, they lack the institutional safety wrap that consumers depend on to mitigate risk.

Merchant Perception and the Supply Side.
This section evaluates the willingness of retailers to integrate new payment rails.

Card – Network Externalities. Merchant acceptance is driven by expected net transactional benefits and observable customer demand [[24](https://arxiv.org/html/2601.00196v1#bib.bib24)]. Card networks benefit from strong positive network externalities: because nearly all consumers carry cards, merchants are compelled to accept them to avoid losing sales.

Stablecoin – The Niche Trap. Survey evidence indicates that crypto acceptance is not random but highly conditional. Polasik et al. [[162](https://arxiv.org/html/2601.00196v1#bib.bib162)] find that adoption is most visible among start-ups, smaller retailers, and firms operating in developing economies or informal sectors, where weak formal infrastructure makes crypto a rational substitute for legacy bank and card payment rails. For mainstream retailers, by contrast, the primary barrier is the absence of customer demand [[24](https://arxiv.org/html/2601.00196v1#bib.bib24)]. This creates a feedback loop in which consumers do not pay with crypto because merchants do not accept it, and merchants do not accept it because consumers do not request it. Silinskyte [[163](https://arxiv.org/html/2601.00196v1#bib.bib163)] further notes that facilitating conditions, particularly the ease of integrating through payment service providers, are essential for translating merchant intention into actual implementation.

This evidence points to a classic two-sided market coordination failure. Unlike the card network, which utilized interchange fees to subsidize the chicken-and-egg problem, the stablecoin ecosystem lacks a centralized mechanism to simultaneously incentivize merchants and consumers. Consequently, uptake remains modest and fragmented outside of specific niches.

Operational Performance.
This section remains focused on the objective metrics about latency reliability we discussed previously: approved and confirmation. Consequently, even where technical performance converges at the user interface level, differences in predictability, failure handling, and institutional backstops sustain a perceptual gap between card-based and stablecoin-based payments.

Card – Instant Operational Approval.
Card authorization is commonly described as completing within a few seconds, which merchants interpret as a near real-time operational signal that settlement will follow [[77](https://arxiv.org/html/2601.00196v1#bib.bib77)].

Stablecoin – Routing and Liquidity. While some blockchain networks and scaling solutions can deliver near real-time user-facing payment acknowledgments, performance remains sensitive to network conditions, routing pathways, and available liquidity. Providers typically display a paid or pending status within seconds, yet final confirmation may take longer, particularly on base-layer networks where settlement depends on block production times [[164](https://arxiv.org/html/2601.00196v1#bib.bib164), [165](https://arxiv.org/html/2601.00196v1#bib.bib165)]. A further limitation is the lack of audited, cross-rail performance statistics; existing comparisons rely largely on heterogeneous vendor reports rather than harmonized measurement frameworks.

Experience Level Finding
*The critical determinant of user experience in retail payments is not raw technical performance but perceived security, predictability, and ease of use.*
Card networks align system behavior with user expectations by embedding institutional guarantees and familiar interaction patterns that abstract risk away from users. Stablecoin payments, by contrast, shift security and error management to consumers and merchants, increasing cognitive and operational burden even when underlying performance is comparable. Thus, user experience reflects how effectively a payment system minimizes uncertainty at the point of interaction.

### III-D Architecture: System Integrity and Security

The architectural dimension concerns how payment systems validate transactions, maintain ledger integrity, and withstand operational failures or attacks. In payments economics, these choices are shaped by the underlying instrument type. Account-based systems require a trusted authority to verify identity and update balances, whereas token-based systems require distributed consensus to validate transfers of bearer-like assets [[32](https://arxiv.org/html/2601.00196v1#bib.bib32)]. These differences shape contrasting patterns of operational resilience and security risk allocation.

Network Topology and Operational Resilience. This section focuses on how structural layout affects system resilience and the pattern of failures observed in practice.

Card – Centralized Intermediation.
Traditional card networks follow a hub-and-spoke topology in which a central intermediary coordinates messaging, risk scoring, and routing between issuers and acquirers. This structure optimizes throughput and operational control, enabling near-instant authorization and globally interoperable acceptance. However, literature in financial market infrastructures notes that centralization introduces correlated-failure risks: outages at a major processor, scheme switch, or cloud provider can halt retail transactions at scale [[166](https://arxiv.org/html/2601.00196v1#bib.bib166), [52](https://arxiv.org/html/2601.00196v1#bib.bib52)]. Empirically, card outages in Europe and the US illustrate this fragility, yet systematic academic quantification of such events remains limited.

Stablecoin – Distributed Consensus with Centralized Bottlenecks.
Stablecoin arrangements inherit the security and fault-tolerance properties of the blockchains [[167](https://arxiv.org/html/2601.00196v1#bib.bib167)] on which they are issued. These networks implement forms of Byzantine Fault Tolerant (BFT) [[168](https://arxiv.org/html/2601.00196v1#bib.bib168), [169](https://arxiv.org/html/2601.00196v1#bib.bib169)] consensus that allow decentralized validators to maintain ledger integrity under adversarial conditions. In blockchain-based payment environments, this produces a settlement layer that is resilient to validator outages and capable of maintaining continuity of the ledger [[44](https://arxiv.org/html/2601.00196v1#bib.bib44), [170](https://arxiv.org/html/2601.00196v1#bib.bib170)].

At the user-facing level, however, operational fragilities arise from reliance on intermediated transaction processing. Even when settlement is decentralized, many practical implementations depend on a single operator or service to coordinate transaction flow before it reaches the underlying blockchain [[171](https://arxiv.org/html/2601.00196v1#bib.bib171)]. This creates a structural asymmetry: the base ledger exhibits strong theoretical resilience, yet the execution environment can stall if the coordinating service experiences downtime, congestion, or restrictive behavior. Although users may retain the ability to move their balances directly on the base chain, they cannot access the continuous, low-latency transfers expected in retail commerce when such interruptions occur. Empirical research highlights this gap between settlement robustness and operational fragility as a key bottleneck for stablecoin use in payments [[172](https://arxiv.org/html/2601.00196v1#bib.bib172), [173](https://arxiv.org/html/2601.00196v1#bib.bib173)].

Security Model Shift. This section analyzes how architectures allocate security risk, contrasting institution-managed credential protection with user-managed cryptographic control.

Card – Credential-sharing and Perimeter Security.
Account-based networks rely on credential sharing, including Primary Account Number (PAN) and other personal identifiers, which must be processed across many intermediaries. This places concentrated volumes of sensitive information in large custodial databases. Security economists describe these repositories as honeypots that attract attackers and cause repeated large-scale breaches [[174](https://arxiv.org/html/2601.00196v1#bib.bib174)]. Although tokenization and Payment Card Industry Data Security Standards (PCI DSS) [[175](https://arxiv.org/html/2601.00196v1#bib.bib175)] reduce some exposure, the overall perimeter-defense model still depends on institutional controls rather than mathematical certainty.

Stablecoin – Cryptographic Guarantees and User Vulnerability.
In token-based architectures, security is achieved via cryptography rather than identity verification [[44](https://arxiv.org/html/2601.00196v1#bib.bib44)]. The private key acts as the authorization root and is never shared with the merchant, so the system structurally eliminates the institutional honeypot risk inherent in card networks (where centralized databases of PANs attract mass breaches). However, this architecture creates a security inversion, shifting the locus of risk from the network perimeter to the user endpoint.

Empirical studies emphasize that while the network is resilient, the user is fragile. Karantias et al. [[176](https://arxiv.org/html/2601.00196v1#bib.bib176)] document the high frequency of wallet compromise, phishing, and key loss-failures for which blockchain protocols offer no formal remediation mechanism. Unlike the card model, where the issuer absorbs the risk of fraud, the stablecoin model imposes strict liability on the user. Furthermore, the reliance on programmable settlement introduces smart contract risk, where software exploits create a vector for systemic loss absent in traditional banking ledgers [[177](https://arxiv.org/html/2601.00196v1#bib.bib177), [178](https://arxiv.org/html/2601.00196v1#bib.bib178), [179](https://arxiv.org/html/2601.00196v1#bib.bib179)]. Recent research highlights these technical risks but frequently overlooks the economic implication: that stablecoins effectively demonetize the insurance function of payments, trading consumer protection for settlement finality.

Architecture Level Finding
*The fundamental architectural trade-off in retail payments lies between centralized risk absorption and decentralized technical resilience.*
Card networks centralize validation and security within intermediaries, enabling strong institutional control but exposing the system to correlated operational failures. Stablecoin systems, by contrast, secure ledger integrity through distributed consensus and cryptographic verification, reducing settlement risk while shifting execution and security risk to users and smart contracts. Therefore, architecture determines not only system resilience but also where operational and security risks ultimately reside within the payment ecosystem.

### III-E Reach: The Fragmentation Barrier

The reach dimension concerns the scale of merchant acceptance and the interoperability standards that enable it. Payment systems are classic network goods: their value rises with the size of their user base, and incumbents benefit from strong positive feedback loops, switching costs, and path dependence [[180](https://arxiv.org/html/2601.00196v1#bib.bib180), [181](https://arxiv.org/html/2601.00196v1#bib.bib181)]. These dynamics shape adoption more powerfully than technical performance alone. In this sense, differences in reach reflect not only technical design choices but also the presence or absence of mechanisms that coordinate expectations across market participants. These architectural differences manifest along two closely related dimensions: network topology and operational resilience, and the underlying security model governing transaction authorization and risk allocation. These differences translate into contrasting degrees of interoperability, coordination, and network scale.

Network Scale and Standardization. This section compares how card networks and stablecoin systems achieve reach, highlighting the contrasting roles of standardization and fragmentation in shaping their global scalability and reliability.

Card – Global Interoperability.
Traditional card networks achieve near-universal reach through decades of enforced standardization. Interoperability is secured through ISO 8583 [[35](https://arxiv.org/html/2601.00196v1#bib.bib35)] messaging, EMV hardware specifications and scheme rulebooks that ensure functional equivalence across issuers, acquirers and geographies. With an acceptance footprint now exceeding 150 million merchant locations in more than 200 countries and territories [[182](https://arxiv.org/html/2601.00196v1#bib.bib182)], cards exhibit the characteristics of a mature network good: a ubiquitous installed base and stable expectations that reinforce adoption on both sides of the market. The two-sided platform literature emphasizes that such standardization is essential for global scale [[36](https://arxiv.org/html/2601.00196v1#bib.bib36)]. Taken together, these features give card networks a highly predictable operational profile and make them difficult to fully displace even when alternative technologies emerge.

Stablecoins – Fragmented Infrastructures.
Stablecoin networks operate across heterogeneous blockchains, such as Ethereum, Solana, and Tron [[183](https://arxiv.org/html/2601.00196v1#bib.bib183)], each with distinct execution environments and token standards. This creates structural fragmentation, since identical stablecoins issued across chains are not mutually substitutable and no shared messaging layer exists to coordinate them. This fragmentation is not merely technical but reflects a coordination failure, as no governing entity exists to mandate standards or align expectations across issuers, wallets, and merchants. Interoperability depends on cross-chain bridges [[184](https://arxiv.org/html/2601.00196v1#bib.bib184), [185](https://arxiv.org/html/2601.00196v1#bib.bib185)] that lock assets on one chain and mint representations on another. Empirical data shows that cross-chain bridges were a particularly vulnerable component of the blockchain ecosystem, with an estimated $2 billion stolen across 13 separate bridge hacks—accounting for a majority of total value lost in crypto hacks in 2022  [[186](https://arxiv.org/html/2601.00196v1#bib.bib186)]. Although technical proposals aim to improve portability and cross-chain execution, most remain early-stage and are unevenly implemented. As a result, stablecoin circulation remains dispersed across isolated execution environments, and operational behavior varies widely depending on chain-level design choices.

Coordination Problem. This section examines how coordination dynamics shape adoption, contrasting the strong network effects that reinforce card dominance with the more fragile and localized patterns seen in stablecoin use.

Card – Lock-in via Network Effects.
Large installed bases generate substantial switching costs. A merchant who drops cards risks losing nearly all customers, and a consumer who abandons cards faces limited acceptance for everyday purchases. This dynamic reflects the start-up problem in network economics, that is, even if a challenger technology is technically superior, it cannot displace an incumbent without overcoming entrenched expectations and coordination equilibria [[180](https://arxiv.org/html/2601.00196v1#bib.bib180)]. Empirical work on payment-system competition shows that merchants adopt new methods only when expected demand is sufficiently large or when intermediaries provide financial incentives to offset the risk of early adoption. These reinforcing expectations help maintain the stability of card-based retail payments across diverse markets.

Stablecoin – Limited to Closed Loops.
Stablecoin payments, by contrast, tend to flourish in closed-loop environments such as crypto exchanges, remittance corridors and merchant niches in economies with weak banking infrastructure. In advanced economies, the lack of unified standards and the absence of broad consumer demand limit the emergence of mutually reinforcing network effects. As stablecoin activity remains distributed across isolated platforms and user communities, adoption patterns are driven more by localized incentives and specific operational contexts than by broad two-sided market forces. This leads to a payment landscape where stablecoins function within domain-specific ecosystems but exhibit limited capacity to generalize into mass retail environments.

Card networks operate as a unified system because interoperability is mandated and consistently enforced across all participants. Stablecoins, by contrast, function across a set of incompatible ledgers that lack a common settlement or messaging layer, which keeps circulation dispersed and coordination limited. Without convergence on shared technical and operational standards similar to ISO 8583 or EMV, stablecoin arrangements are unlikely to achieve the broad, retail-facing reach characteristic of card networks. In brief, these structural differences explain why cards scale as a global payment utility while stablecoin usage remains concentrated within specific, self-contained environments.

Reach Level Finding
*The primary determinant of reach in retail payments is not technological openness but coordinated standardization and expectation alignment.*
Card networks achieve global scale by enforcing interoperable standards that consolidate participants into a single, predictable system and enable strong network effects across merchants and consumers. Stablecoin payments, by contrast, fragment activity across heterogeneous ledgers and interoperability layers, dispersing liquidity and usage norms. As a result, stablecoins struggle to generate self-reinforcing network effects and remain largely confined to closed or domain-specific loops in the absence of system-wide coordination.

## IV Discussion and Implications

The preceding sections evaluated stablecoin-based payments relative to incumbent card networks along the CLEAR dimensions. This discussion interprets those results in a broader economic framework, focusing on the conditions under which stablecoins outperform incumbent rails, the constraints on convergence in retail payments, and the implications for competition and coexistence with central bank digital currencies (CBDCs).

### IV-A Contextual Domains of Stablecoin Advantage

Stablecoin-based payment arrangements demonstrate strong technical capabilities at the settlement layer, yet remain institutionally incomplete as general-purpose retail payment instruments. Whether convergence with incumbent card networks is feasible depends not on eliminating all frictions, but on selectively mitigating those that directly constrain adoption. This subsection interprets the preceding analysis by identifying the conditions under which stablecoins may partially converge with card-based systems, while remaining structurally distinct.

High-friction Cross-border Corridors.
Stablecoins deliver their most pronounced efficiency gains in cross border remittances and Business-to-Business (B2B) treasury flows, where legacy correspondent banking chains remain both costly and slow. Empirical evidence shows that the global average cost of sending the benchmark remittance amount of $200 reached 6.35% in Q1 2024, while banks charged an average of 12.66%, substantially exceeding the fees of money transfer operators and digital providers [[187](https://arxiv.org/html/2601.00196v1#bib.bib187), [188](https://arxiv.org/html/2601.00196v1#bib.bib188)]. These costs reflect the layered structure of correspondent banking, which relies on sequential intermediaries, manual reconciliation, and limited operating hours.

In this context, stablecoin based settlement compresses both time and cost by bypassing multiple correspondent layers and enabling near continuous ledger based finality. High throughput networks support rapid cross border value transfer with fewer intermediaries, making efficiency gains particularly salient where traditional cross-border payment infrastructure performs poorly. Industry estimates indicate that in 2024, approximately 5-10 % of stablecoin transaction volume, equivalent to around 1.3 trillion US dollars, reflected genuine real economy payment activity, including cross border remittances, corporate treasury operations, and retail payments, with comparative advantages concentrated in cross border use cases [[189](https://arxiv.org/html/2601.00196v1#bib.bib189)].

High-Inflation and Financially Constrained Economies.
A second domain of stablecoin advantage arises in jurisdictions experiencing sustained inflation, currency depreciation, or limited access to reliable banking services. In these settings, the primary appeal of stablecoins lies less in payment efficiency than in access to a relatively stable unit of account and store of value. USD denominated stablecoins in particular function as de facto instruments of value preservation in markets such as Turkey and Nigeria, where domestic currencies exhibit pronounced volatility [[189](https://arxiv.org/html/2601.00196v1#bib.bib189)].

Here, features that are often viewed as constraints in advanced retail payment systems, most notably the immutability of blockchain ledgers, take on a different functional role. Ledger immutability provides users with a form of monetary autonomy that allows savings to be insulated from domestic banking instability, capital controls, or inflationary erosion. As a consequence, stablecoin usage in these economies reflects a demand for monetary stability rather than a substitution for mature retail payment instruments. In this sense, stablecoins operate as an alternative monetary infrastructure rather than as a competing retail payment rail.

### IV-B Pathways to Partial Convergence

Stablecoin arrangements demonstrate strong technological performance in settlement through atomic execution, yet remain institutionally incomplete as general-purpose retail instruments because they lack a scheme-level governance rulebook. The shift from hierarchical, institution-managed networks to modular, protocol-governed architectures creates a responsibility vacuum: dispute handling, liability allocation, and operating standards are pushed to wallets, intermediaries, and courts, which weakens consumer recourse and inhibits the self-reinforcing network effects seen in card schemes.

Accordingly, convergence depends less on raw throughput and more on developing governed intervention mechanisms and shared operational standards that can replicate the trust and stability of incumbent systems. This subsection synthesizes the prior evidence into practical pathways toward partial convergence.

Reconstructing Consumer Side Subsidies.
Convergence in retail payments is shaped by whether stablecoin arrangements can recreate the consumer-side subsidies that historically enabled card network adoption. While stablecoin settlement compresses merchant-facing acceptance costs, widespread retail use requires that transaction-related frictions be abstracted away from consumers. In their current form, gas fees and portfolio management requirements impose operational burdens on users, which conflicts with the pricing structure that underpins habitual card usage.

Progress toward convergence therefore depends on reallocating these burdens to intermediaries that benefit from stablecoin-based settlement. Account abstraction under ERC 4337 enables paymasters to sponsor transaction fees and allows payment service providers to internalize costs within their treasury operations [[190](https://arxiv.org/html/2601.00196v1#bib.bib190)]. Early pilots by firms such as Worldpay and Nuvei illustrate this direction, as stablecoin-related costs are absorbed at the infrastructure level rather than exposed at the POI [[191](https://arxiv.org/html/2601.00196v1#bib.bib191), [192](https://arxiv.org/html/2601.00196v1#bib.bib192)]. Such fee internalization mirrors card economics, where operational complexity is deliberately hidden from end users in order to facilitate scale.

Reconciling Finality with Legal Recourse.
Legal convergence is constrained by the tension between technical irreversibility and the demand for transaction-level protection. Stablecoin arrangements provide asset-level safeguards through reserve backing and redemption rights, yet generally lack mechanisms for consumer reimbursement in cases of fraud or mistaken transfers. Card-based systems, by contrast, embed chargebacks, liability allocation, and statutory reimbursement obligations that establish predictable outcomes when transactions fail and anchor consumer trust.

Movement toward convergence is emerging through hybrid regulatory and institutional designs. Frameworks such as MiCA introduce issuance controls and allow issuer- or authority-initiated freezes that permit limited intervention without replicating full card-style reversibility [[19](https://arxiv.org/html/2601.00196v1#bib.bib19)]. At the same time, institutional actors such as Visa and PayPal demonstrate how compliance screening, fraud controls, and controlled intervention can be layered onto stablecoin-enabled payment environments. Over time, convergence requires legal doctrines that align technical finality with legally recognized discharge of obligations, producing predictability comparable to regimes such as PSD2 [[32](https://arxiv.org/html/2601.00196v1#bib.bib32)]. These developments point toward partially governed architectures rather than a return to fully immutable instruments.

Abstracting Risk and Interaction Frictions.
Experiential convergence depends on narrowing the gap between system performance and user expectations at the POI. In mature retail markets, consumers expect payment experiences that are fast, predictable, and supported by strong structural assurances. Direct self-custodial use of stablecoins exposes users to key management, fee selection, and routing uncertainty, which increases perceived risk and suppresses willingness to transact. Empirical evidence consistently shows that trust and ease of use dominate payment choice, and stablecoin-based interactions remain disadvantaged on both dimensions [[156](https://arxiv.org/html/2601.00196v1#bib.bib156), [155](https://arxiv.org/html/2601.00196v1#bib.bib155)].

Mitigation therefore hinges on abstraction at the interface level. Account abstraction under ERC 4337 [[190](https://arxiv.org/html/2601.00196v1#bib.bib190)] allows wallets to conceal gas fees, streamline authorization flows, and introduce familiar authentication mechanisms such as biometric verification or social recovery. Large platforms increasingly embed stablecoins within closed-loop environments, as illustrated by PayPal’s PYUSD, where identity verification and fraud controls remain intact [[193](https://arxiv.org/html/2601.00196v1#bib.bib193)]. In these configurations, users experience stablecoin payments as simple transactional actions rather than cryptographic procedures, bringing interaction patterns closer to those of card-based systems.

Consolidating Operational Reliability.
Operational convergence requires aligning resilient settlement with dependable end-to-end execution. Blockchain consensus mechanisms provide strong guarantees of ledger integrity, yet retail payment performance depends on the reliability of surrounding layers, including wallets, routing services, bridges, and liquidity providers. While stablecoin settlement is relatively robust by design, user experience can degrade when these ancillary components encounter congestion, downtime, or coordination failures [[172](https://arxiv.org/html/2601.00196v1#bib.bib172), [173](https://arxiv.org/html/2601.00196v1#bib.bib173)].

Progress toward convergence therefore depends on architectural consolidation and institutional standardization. Industry pilots illustrate early movement in this direction. Visa’s USDC-based settlement integrates stablecoins directly into acquirer treasury flows, reducing reliance on legacy correspondent banking infrastructure [[194](https://arxiv.org/html/2601.00196v1#bib.bib194)]. Cross-chain interoperability initiatives such as the Cross-Chain Interoperability Protocol (CCIP) seek to standardize messaging and settlement across heterogeneous chains [[195](https://arxiv.org/html/2601.00196v1#bib.bib195)], although most remain at an early stage and often rely on trusted components [[196](https://arxiv.org/html/2601.00196v1#bib.bib196)]. Achieving card-level reliability requires clearly defined operational rules, recovery procedures, and governance structures that ensure predictable behavior under stress.

Coordinating Standards and Expectations.
Scalable convergence ultimately depends on coordinating expectations across market participants through shared standards. Card networks achieve global reach by enforcing interoperability through ISO 8583 messaging, EMV authentication, and scheme rulebooks, which ensure consistent behavior across merchants, issuers, and geographies [[35](https://arxiv.org/html/2601.00196v1#bib.bib35)]. This uniformity underpins strong network effects and stabilizes adoption on both market sides.

Stablecoin ecosystems, by contrast, remain distributed across incompatible execution environments, with interoperability often mediated by bridges that introduce operational and security risks. Meaningful convergence therefore requires both technical and institutional coordination. Technically, stablecoins require shared settlement and messaging standards that deliver consistent functionality across chains. Institutionally, they require governance frameworks that define acceptable behavior for issuers, payment service providers, and intermediaries, allowing merchants to treat stablecoin payments as predictable and uniform. Until such coordination emerges, stablecoins are likely to remain highly effective within specialized domains, yet constrained in their ability to scale as a universal retail payment utility.

### IV-C Stablecoins and CBDCs in Systemic Competition

Private stablecoins face inherent limitations in supplying the legal finality, supervisory oversight, and systemic safeguards required for large-scale retail deployment [[197](https://arxiv.org/html/2601.00196v1#bib.bib197), [198](https://arxiv.org/html/2601.00196v1#bib.bib198)]. These constraints have prompted central banks to explore central bank digital currencies (CBDCs) not merely as technological upgrades to existing payment infrastructures, but as strategic instruments for preserving monetary sovereignty and anchoring trust in an increasingly tokenized financial system [[199](https://arxiv.org/html/2601.00196v1#bib.bib199), [200](https://arxiv.org/html/2601.00196v1#bib.bib200), [201](https://arxiv.org/html/2601.00196v1#bib.bib201)]. Recent policy blueprints converge on a layered architecture in which CBDCs operate as a foundational settlement asset, while private digital instruments provide higher-layer functionality and application-specific innovation.

Within this emerging architecture, competition between stablecoins and CBDCs operates at the level of system design rather than direct substitution. CBDCs are structurally advantaged in providing legally recognized finality, uniform compliance with consumer protection regimes, and native integration with anti-money laundering and supervisory frameworks [[202](https://arxiv.org/html/2601.00196v1#bib.bib202)]. They can also be embedded within domestic instant payment infrastructures and designed with negligible marginal transaction costs, reducing the scope for private instruments to compete on cost or baseline accessibility alone. From an architectural perspective, state-issued systems can enforce common interoperability standards across intermediaries, avoiding the fragmentation and bridge-related vulnerabilities that characterize multi-chain stablecoin ecosystems [[198](https://arxiv.org/html/2601.00196v1#bib.bib198)]. These features do not ensure superior adoption outcomes, but they do confer a level of institutional credibility that private issuers cannot replicate independently.

The more plausible trajectory is therefore one of functional differentiation rather than wholesale displacement. Stablecoins retain comparative advantages in environments where programmability, composability, and cross-border portability are central, including platform-based economies, decentralized financial applications, and selected international payment corridors where sovereign systems may lack interoperability. CBDCs, by contrast, are positioned to serve as settlement anchors, supplying legal certainty, operational uniformity, and state-backed assurances suited to large-scale retail and institutional use. As sovereign digital instruments begin to replicate many of the technical features associated with stablecoins while closing institutional gaps around governance and recourse, competitive dynamics shift away from direct rivalry toward complementary roles.

## V Conclusion

Stablecoins and card networks embody fundamentally different institutional and technical logics. Stablecoins deliver continuous, programmable settlement on shared ledgers but externalize core elements of the retail payment safety wrapper, including consumer recourse, liability allocation, and interoperability, into wallets, intermediaries, and courts. Card networks, while slower at final settlement, function more effectively as mass-market instruments by bundling authorization, risk management, and post-transaction protections into enforceable rulebooks. Consequently, stablecoins perform well in closed-loop or high-friction environments but remain structurally disadvantaged in open-loop POS settings where trust, simplicity, and near-universal acceptance dominate adoption.

Across our research questions, card networks emerge as pull-based, intermediary-governed account systems with separated authorization and settlement, whereas stablecoins operate as push-based token transfers that collapse validation and settlement into irreversible ledger updates (RQ1). Under the CLEAR framework (RQ2), stablecoins display a conditional cost advantage through 24/7 settlement and reduced rail-level fees, but underperform on legality, experience, and reach. Closing this gap (RQ3) requires selective re-intermediation, such as fee abstraction, governed intervention mechanisms, and shared standards, rather than full disintermediation. Absent such convergence, stablecoins are likely to complement card networks as efficient settlement assets and niche payment instruments, rather than replace them in general-purpose retail payments.

## References

* [1]

  Bank for International Settlements, “The role of central bank money in payment systems,” Tech. Rep., 2003. [Online]. Available: https://www.bis.org/cpmi/publ/d55.pdf
* [2]

  I. Hasan, T. De Renzis, and H. Schmiedel, *Retail payments and economic growth*. Bank of Finland Research Discussion Papers, 2012, no. 19/2012.
* [3]

  European Central Bank, “The payment system: Payments, securities and derivatives, and the role of the eurosystem,” 2010, accessed: Oct. 10, 2025. [Online]. Available: https://www.ecb.europa.eu/pub/pdf/other/paymentsystem201009en.pdf
* [4]

  I. Hasan, T. De Renzis, and H. Schmiedel, “Retail payments and the real economy,” 2013.
* [5]

  A. Lagator, “Global development trends in payment card industry,” National Bank of Serbia, Tech. Rep., 2021.
* [6]

  Bank for International Settlements, “Fast payments - enhancing the speed and availability of retail payments,” 2016, accessed: Oct. 10, 2025. [Online]. Available: https://www.bis.org/cpmi/publ/d154.pdf
* [7]

  European Central Bank, “Report on a digital euro,” 2020, accessed: Oct. 10, 2025. [Online]. Available: https://www.ecb.europa.eu/pub/pdf/other/Report\_on\_a\_digital\_euro~4d7268b458.en.pdf
* [8]

  U. B. L. Yawe and U. I. Mukisa, “The impact of the revised payment services directive on the market for payment initiation services.” *Journal of Payments Strategy & Systems*, vol. 14, no. 1, 2020.
* [9]

  DefiLlama, “Total stablecoin market capitalization,” 2025, accessed: Nov. 23, 2025. [Online]. Available: https://defillama.com/stablecoins
* [10]

  Rise, “25 stablecoin statistics from 2025 (so far),” 2025, accessed: Nov. 19, 2025. [Online]. Available: https://www.riseworks.io/blog/stablecoin-statistics-from-2025
* [11]

  Q. Wang, R. Li, Q. Wang, S. Chen, M. Ryan, and T. Hardjono, “Exploring web3 from the view of blockchain,” *arXiv preprint arXiv:2206.08821*, 2022.
* [12]

  OKX, “Okx pay singapore: Scan-to-pay with stablecoins at grabpay merchants,” accessed: Nov. 27, 2025. [Online]. Available: https://www.okx.com/en-au/learn/okx-pay-singapore
* [13]

  The Business Times (Singapore), “Okx singapore launches stablecoin payments at grabpay merchants,” accessed: Nov. 27, 2025. [Online]. Available: https://www.businesstimes.com.sg/wealth/crypto-alternative-assets/okx-singapore-launches-stablecoin-payments-grabpay-merchants
* [14]

  Channel NewsAsia, “Xsgd launches on coinbase,” accessed: Oct. 10, 2025. [Online]. Available: https://www.channelnewsasia.com/business/stablecoin-xsgd-singapore-launch-coinbase-crypto-okx-pay-5379656
* [15]

  H. Tian, K. Xue, X. Luo, S. Li, J. Xu, J. Liu, J. Zhao, and D. S. Wei, “Enabling cross-chain transactions: A decentralized cryptocurrency exchange protocol,” *IEEE Transactions on Information Forensics and Security*, vol. 16, pp. 3928–3941, 2021.
* [16]

  A. Brechlin, J. Schäfer, and F. Armknecht, “Buy crypto, sell privacy: Investigating the cryptocurrency exchange evonax,” in *2024 IEEE International Conference on Blockchain and Cryptocurrency*. IEEE, 2024, pp. 1–7.
* [17]

  S. Werner, D. Perez, L. Gudgeon, A. Klages-Mundt, D. Harz, and W. Knottenbelt, “Sok: Decentralized finance (defi),” in *Proceedings of the 4th ACM Conference on Advances in Financial Technologies*, 2022, pp. 30–46.
* [18]

  L. Zhou, X. Xiong, J. Ernstberger, S. Chaliasos, Z. Wang, Y. Wang, K. Qin, R. Wattenhofer, D. Song, and A. Gervais, “Sok: Decentralized finance (defi) attacks,” in *2023 IEEE Symposium on Security and Privacy*. IEEE, 2023, pp. 2444–2461.
* [19]

  European Union, “Regulation (eu) 2023/1114 on markets in crypto-assets (mica),” 2023, accessed Oct. 11, 2025. [Online]. Available: https://eur-lex.europa.eu/eli/reg/2023/1114/oj
* [20]

  “Guiding and establishing national innovation for u.s. stablecoins act (genius act),” 2025, accessed: Nov. 19, 2025. [Online]. Available: https://www.congress.gov/bill/119th-congress/senate-bill/1582/text
* [21]

  G. Neyer and B. Geva, “Blockchain and payment systems: What are the benefits and costs?” *Journal of Payments Strategy & Systems*, vol. 11, no. 3, pp. 215–225, 2017.
* [22]

  E. Koutrouli and P. Manousopoulos, “Exploring the use of crypto-assets for payments,” *FinTech*, vol. 4, no. 2, p. 15, 2025.
* [23]

  E. Erdin, S. Mercan, and K. Akkaya, “An evaluation of cryptocurrency payment channel networks and their privacy implications,” *arXiv preprint arXiv:2102.02659*, 2021.
* [24]

  N. Jonker, “What drives the adoption of crypto-payments by online retailers?” *Electronic Commerce Research and Applications*, vol. 35, p. 100848, 2019.
* [25]

  H. Nabilou, “The dark side of licensing cryptocurrency exchanges as payment institutions,” *Law and Financial Markets Review*, vol. 14, no. 1, pp. 39–47, 2020.
* [26]

  T. Puschmann and M. Huang-Sui, “A taxonomy for decentralized finance,” *International Review of Financial Analysis*, vol. 92, p. 103083, 2024.
* [27]

  World Bank, “Payment systems worldwide: A snapshot—summary outcomes of the fourth global payment systems survey,” World Bank, Tech. Rep., 2018. [Online]. Available: https://documents1.worldbank.org/curated/en/099011624132054588/pdf/P1787031cca90801019d011a41f21efe348.pdf
* [28]

  D. Arner, R. Auer, and J. Frost, “Stablecoins: Risks, potential and regulation,” 2020, accessed: Nov. 19, 2025. [Online]. Available: https://www.bis.org/publ/work905.htm
* [29]

  A. Moin, K. Sekniqi, and E. G. Sirer, “Sok: A classification framework for stablecoin designs,” in *Financial Cryptography and Data Security*. Springer, 2020, pp. 174–197.
* [30]

  A. Mahrous, M. Caprolu, and R. Di Pietro, “Sok: A structured analysis of economic and technical stablecoin-related research,” in *2025 IEEE International Conference on Blockchain and Cryptocurrency*. IEEE, 2025, pp. 1–17.
* [31]

  S. Ling, Y. Du, Y. Zhou, L. Wu, C. Wang, X. Jia, and H. Yan, “Sok: Stablecoin designs, risks, and the stablecoin lego,” *arXiv preprint arXiv:2506.17622*, 2025.
* [32]

  C. M. Kahn and W. Roberds, “Why pay? an introduction to payments economics,” *Journal of Financial Intermediation*, vol. 18, no. 1, pp. 1–23, 2009.
* [33]

  M. Ward, “Emv card payments–an update,” *Information Security Technical Report*, vol. 11, no. 2, pp. 89–92, 2006.
* [34]

  D. L. Stearns, *Electronic value exchange: Origins of the VISA electronic payment system*. Springer, 2011.
* [35]

  International Organization for Standardization, “Iso 8583:2023 — financial-transaction-card-originated messages: Interchange message specifications,” 2023, accessed: Nov. 27, 2025. [Online]. Available: https://www.iso.org/standard/79451.html
* [36]

  D. S. Evans and R. Schmalensee, *Paying with plastic: the digital revolution in buying and borrowing*. Mit Press, 2004.
* [37]

  A. Thomadakis, “Shortening the settlement cycle: Why europe should not wait too long to introduce t+1,” *Journal of Securities Operations & Custody*, vol. 14, no. 4, pp. 350–354, 2022.
* [38]

  J. Benito, “Navigating settlement efficiency in a world of csdr and t+1.” *Journal of Securities Operations & Custody*, vol. 17, no. 3, 2025.
* [39]

  European Payments Council. SEPA Instant Credit Transfer. Accessed: 18 Dec 2025. [Online]. Available: https://www.europeanpaymentscouncil.eu/what-we-do/sepa-instant-credit-transfer
* [40]

  Banco Central do Brasil. Pix. Accessed: 18 Dec 2025. [Online]. Available: https://www.bcb.gov.br/en/financialstability/pix\_en
* [41]

  Federal Reserve Financial Services. FedNow Service. Accessed: 18 Dec 2025. [Online]. Available: https://www.frbservices.org/financial-services/fednow
* [42]

  Bank for International Settlements, “Central bank digital currency: Key features and implications,” 2021, accessed: Nov. 19, 2025. [Online]. Available: https://www.bis.org/cpmi/publ/d201.pdf
* [43]

  World Bank Group, “Innovations in electronic payment acceptance: Enabling better access for micro and small merchants,” The World Bank, Washington, DC, Tech. Rep., 2022.
* [44]

  S. Nakamoto and A. Bitcoin, “A peer-to-peer electronic cash system,” *Bitcoin.–URL: https://bitcoin. org/bitcoin. pdf*, vol. 4, no. 2, p. 15, 2008.
* [45]

  V. Buterin, “A next-generation smart contract and decentralized application platform,” 2014, accessed: Oct. 11, 2025. [Online]. Available: https://ethereum.org/en/whitepaper
* [46]

  Z. Zheng, S. Xie, H.-N. Dai, W. Chen, X. Chen, J. Weng, and M. Imran, “An overview on smart contracts: Challenges, advances and platforms,” *Future Generation Computer Systems*, vol. 105, pp. 475–491, 2020.
* [47]

  R. Garg, “Ethereum based smart contracts for trade and finance,” *International Journal of Economics and Management Engineering*, vol. 16, no. 11, pp. 619–629, 2022.
* [48]

  J. Mattke, C. Maier, and L. Reis, “Is cryptocurrency money? three empirical studies analyzing medium of exchange, store of value and unit of account,” in *Proceedings of the 2020 Computers and People Research Conference*, 2020, pp. 26–35.
* [49]

  Tether, “Tether transparency: Usdt reserves,” 2025, accessed: Dec. 4, 2025. [Online]. Available: https://tether.to/en/transparency/?tab=usdt
* [50]

  Circle, “Circle transparency and reserves reporting,” 2025, accessed: Dec. 4, 2025. [Online]. Available: https://www.circle.com/transparency
* [51]

  B. Alexandrova-Kabadjova, “Impact of interchange fees on a nonsaturated multi-agent payment card market,” *Intelligent Systems in Accounting, Finance and Management: International Journal*, vol. 16, no. 1-2, pp. 33–48, 2009.
* [52]

  Bank for International Settlements, “A glossary of terms used in payments and settlement systems,” 2016, accessed: Nov. 19, 2025. [Online]. Available: https://www.bis.org/cpmi/publ/d00b.htm
* [53]

  S. J. Hughes and S. T. Middlebrook, “Developments in the laws governing electronic payments made through gift cards, debit and prepaid cards, credit cards, and direct deposits of federal benefits,” *Bus. Law.*, vol. 66, p. 159, 2010.
* [54]

  D. HUMPHREY, “10.1 payments overview,” *The Oxford Handbook of Banking*, p. 285, 2019.
* [55]

  M. Rysman, “An empirical analysis of payment card usage,” *The Journal of Industrial Economics*, vol. 55, no. 1, pp. 1–36, 2007.
* [56]

  A. F. Aysan, O. Ozturk, and N. H. Selim, “Local power, global reach: The rise and impact of domestic payment networks in the financial landscape,” *Journal of Science and Technology Policy Management*, vol. 16, no. 1, pp. 143–162, 2025.
* [57]

  European Central Bank. Payments and markets glossary. Accessed: 19 Dec, 2025. [Online]. Available: https://www.ecb.europa.eu/services/glossary/html/act7c.en.html
* [58]

  Pay.UK. Faster Payment System. Accessed: 18 Dec 2025. [Online]. Available: https://www.wearepay.uk/what-we-do/payment-systems/faster-payment-system/
* [59]

  Australian Securities and Investments Commission. Direct debits. MoneySmart (Australian Government). Accessed: 19 Dec, 2025. [Online]. Available: https://moneysmart.gov.au/banking/direct-debits
* [60]

  European Payments Council. SEPA Direct Debit. Accessed: 18 Dec 2025. [Online]. Available: https://www.europeanpaymentscouncil.eu/what-we-do/sepa-direct-debit
* [61]

  Bacs. Direct Debit. Accessed: 18 Dec 2025. [Online]. Available: https://www.bacs.co.uk/bacs-schemes/direct-debit
* [62]

  M. Lilge, “Evolution of prepaid service towards a real-time payment system,” in *IEEE Intelligent Network 2001 Workshop. IN 2001 Conference Record (Cat. No. 01TH8566)*. IEEE, 2001, pp. 195–198.
* [63]

  D. Horne and N. Bendle, “Gift cards: a review and research agenda,” *The international review of retail, distribution and consumer research*, vol. 26, no. 2, pp. 154–170, 2016.
* [64]

  R. A. Prager, M. D. Manuszak, E. K. Kiser, and R. Borzekowski, “Interchange fees and payment card networks: Economics, industry developments, and policy issues,” 2009.
* [65]

  S. Chakravorti, “Theory of credit card networks: A survey of the literature,” *Review of network Economics*, vol. 2, no. 2, 2003.
* [66]

  C. Scardovi, “Digital transformation in payments,” in *Digital Transformation in Financial Services*. Springer, 2017, pp. 65–84.
* [67]

  A. Giardina, “The merchant,” *The Romans*, pp. 245–271, 1993.
* [68]

  Worldpay. Worldpay. Accessed: 18 Dec 2025. [Online]. Available: https://www.worldpay.com/en-GB
* [69]

  Stripe. Stripe Australia. Accessed: 18 Dec 2025. [Online]. Available: https://stripe.com/au
* [70]

  Adyen. Adyen Australia. Accessed: 18 Dec 2025. [Online]. Available: https://www.adyen.com/en\_AU
* [71]

  H. Guo, M. Leng, and Y. Wang, “Interchange fee rate, merchant discount rate, and retail price in a credit card network: A game-theoretic analysis,” *Naval Research Logistics (NRL)*, vol. 59, no. 7, pp. 525–551, 2012.
* [72]

  UnionPay International. UnionPay International. Accessed: 18 Dec 2025. [Online]. Available: https://www.unionpayintl.com/en/
* [73]

  Reserve Bank of Australia. Backgrounder on Interchange and Scheme Fees. Accessed: 18 Dec 2025. [Online]. Available: https://www.rba.gov.au/payments-and-infrastructure/review-of-retail-payments-regulation/backgrounders/backgrounder-on-interchange-and-scheme-fees.html
* [74]

  Verifone. Points of Interaction — Verifone Central. Accessed: 18 Dec 2025. [Online]. Available: https://verifone.cloud/docs/verifone-central/verifone-central/manage-your-account/administration/points-interaction
* [75]

  I. Stripe, “How payment transaction processing works,” 2023, accessed: 21 Dec, 2025. [Online]. Available: https://stripe.com/au/resources/more/how-payment-transaction-processing-works
* [76]

  Visa Inc., “Visa core rules and visa product and service rules,” 2025, effective May 20, 2025; Accessed Oct. 11, 2025. [Online]. Available: https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf
* [77]

  Checkout.com, “Card authorization explained: How does it work?” 2024, accessed: Nov. 27, 2025. [Online]. Available: https://www.checkout.com/blog/card-authorization-explained
* [78]

  Thrivent, “T+1 settlement: Definitions, pros, cons & why it’s important for investors,” 2025, accessed: 21 Dec, 2025. [Online]. Available: https://www.thrivent.com/insights/investing/t-1-settlement-definitions-pros-cons-why-its-important-for-investors
* [79]

  C. M. Kahn and W. Roberds, “The economics of payment finality,” *Economic Review-Federal Reserve Bank of Atlanta*, vol. 87, no. 2, pp. 1–12, 2002.
* [80]

  C. Dark, E. Rogerson, N. Rowbotham, and P. Wallis, “Stablecoins: Market developments, risks and regulation,” *Bulletin*, Dec 2022. [Online]. Available: https://www.rba.gov.au/publications/bulletin/2022/dec/pdf/stablecoins-market-developments-risks-and-regulation.pdf
* [81]

  M. S. Ferdous, M. J. M. Chowdhury, and M. A. Hoque, “A survey of consensus algorithms in public blockchain systems for crypto-currencies,” *Journal of Network and Computer Applications*, vol. 182, p. 103035, 2021.
* [82]

  A. Yakovenko, “Solana: A new architecture for a high performance blockchain v0. 8.13,” 2018.
* [83]

  A. Asayag, G. Cohen, I. Grayevsky, M. Leshkowitz, O. Rottenstreich, R. Tamari, and D. Yakira, “A fair consensus protocol for transaction ordering,” in *2018 IEEE 26th International Conference on Network Protocols*. IEEE, 2018, pp. 55–65.
* [84]

  R. A. Das, M. M. S. Pahalovi, and M. N. Yanhaona, “Transaction finality through ledger checkpoints,” in *2019 IEEE 25th International Conference on Parallel and Distributed Systems*. IEEE, 2019, pp. 183–192.
* [85]

  S. Malamud and M. Rostek, “Decentralized exchange,” *American Economic Review*, vol. 107, no. 11, pp. 3320–3362, 2017.
* [86]

  B. Kaplan, V. F. Benli, and E. A. Alp, “Decentralized finance and new lending protocols,” *PressAcademia Procedia*, vol. 16, no. 1, pp. 192–195, 2023.
* [87]

  N. Li, M. Qi, Z. Xu, X. Zhu, W. Zhou, S. Wen, and Y. Xiang, “Blockchain cross-chain bridge security: Challenges, solutions, and future outlook,” *Distributed Ledger Technologies: Research and Practice*, vol. 4, no. 1, pp. 1–34, 2025.
* [88]

  S. Suratkar, M. Shirole, and S. Bhirud, “Cryptocurrency wallet: A review,” in *2020 4th international conference on computer, communication and signal processing*. IEEE, 2020, pp. 1–7.
* [89]

  M. Dotan, Y.-A. Pignolet, S. Schmid, S. Tochner, and A. Zohar, “Survey on blockchain networking: Context, state-of-the-art, challenges,” *ACM Computing Surveys*, vol. 54, no. 5, pp. 1–34, 2021.
* [90]

  A. Kazerani, D. Rosati, and B. Lesser, “Determining the usability of bitcoin for beginners using change tip and coinbase,” in *Proceedings of the 35th ACM International Conference on the Design of Communication*, 2017, pp. 1–5.
* [91]

  L. J. Trautman, “E-commerce, cyber, and electronic payment system risks: lessons from paypal,” *UC Davis Bus. LJ*, vol. 16, p. 261, 2015.
* [92]

  T.-H. Chen, “Do you know your customer? bank risk assessment based on machine learning,” *Applied Soft Computing*, vol. 86, p. 105779, 2020.
* [93]

  W.-M. Lee, “Using the metamask crypto-wallet,” in *Beginning Ethereum Smart Contracts Programming: With Examples in Python, Solidity, and JavaScript*. Springer, 2023, pp. 111–144.
* [94]

  Phantom. (2025) Phantom — the crypto wallet for everyone. Accessed: Dec. 4, 2025. [Online]. Available: https://phantom.com
* [95]

  Circle Internet Group, Inc., “Circle — open infrastructure for faster, smarter payments,” 2025, accessed: 20 Dec, 2025. [Online]. Available: https://www.circle.com
* [96]

  Tether Limited, “Tether — official home of tether,” 2025, accessed: 20 Dec, 2025. [Online]. Available: https://tether.to/en
* [97]

  K. Qin, L. Zhou, Y. Afonin, L. Lazzaretti, and A. Gervais, “Cefi vs. defi–comparing centralized to decentralized finance,” *arXiv preprint arXiv:2106.08157*, 2021.
* [98]

  H. Arslanian, “Stablecoins,” in *The Book of Crypto: The Complete Guide to Understanding Bitcoin, Cryptocurrencies and Digital Assets*. Springer, 2022, pp. 149–170.
* [99]

  J. Xu, C. Wang, and X. Jia, “A survey of blockchain consensus protocols,” *ACM Computing Surveys*, vol. 55, no. 13s, pp. 1–35, 2023.
* [100]

  H. Nabilou, “Probabilistic settlement finality in proof-of-work blockchains: Legal considerations,” *Bus. & Fin. L. Rev.*, vol. 7, p. 139, 2024.
* [101]

  V. Gramoli, “From blockchain consensus back to byzantine consensus,” *Future Generation Computer Systems*, vol. 107, pp. 760–769, 2020.
* [102]

  Y. Xiao, N. Zhang, W. Lou, and Y. T. Hou, “A survey of distributed consensus protocols for blockchain networks,” *IEEE communications surveys & tutorials*, vol. 22, no. 2, pp. 1432–1465, 2020.
* [103]

  E. Politou, F. Casino, E. Alepis, and C. Patsakis, “Blockchain mutability: Challenges and proposed solutions,” *IEEE Transactions on Emerging Topics in Computing*, vol. 9, no. 4, pp. 1972–1986, 2019.
* [104]

  T. Ye, M. Luo, Y. Yang, K.-K. R. Choo, and D. He, “A survey on redactable blockchain: Challenges and opportunities,” *IEEE Transactions on Network Science and Engineering*, vol. 10, no. 3, pp. 1669–1683, 2023.
* [105]

  K. N. Johnson, “Decentralized finance: Regulating cryptocurrency exchanges,” *Wm. & Mary L. Rev.*, vol. 62, p. 1911, 2020.
* [106]

  K. Okasová and K. Košt’ál, “Using machine learning for predicting arbitrage occurrences in cryptocurrency exchanges,” in *2024 IEEE International Conference on Blockchain and Cryptocurrency*. IEEE, 2024, pp. 1–7.
* [107]

  Circle Internet Group, Inc., “Usdc redemption structure,” 2025, accessed: 20 Dec, 2025. [Online]. Available: https://help.circle.com/s/article/USDC-redemption-structure?language=en\_US&category=Fees\_and\_Billing
* [108]

  Tether Operations, S.A. de C.V., “Redeem tether tokens to fiat currency,” 2025, accessed: 20 Dec, 2025. [Online]. Available: https://tether.to/ru/redeem-tethers-to-fiat-currency
* [109]

  S. Houy, P. Schmid, and A. Bartel, “Security aspects of cryptocurrency wallets—a systematic literature review,” *ACM Computing Surveys*, vol. 56, no. 1, pp. 1–31, 2023.
* [110]

  D. Puthal, N. Malik, S. P. Mohanty, E. Kougianos, and G. Das, “Everything you wanted to know about the blockchain: Its promise, components, processes, and problems,” *IEEE Consumer Electronics Magazine*, vol. 7, no. 4, pp. 6–14, 2018.
* [111]

  B. Lashkari and P. Musilek, “A comprehensive review of blockchain consensus mechanisms,” *IEEE access*, vol. 9, pp. 43 620–43 652, 2021.
* [112]

  P. Ruan, D. Loghin, Q.-T. Ta, M. Zhang, G. Chen, and B. C. Ooi, “A transactional perspective on execute-order-validate blockchains,” in *Proceedings of the 2020 ACM SIGMOD International Conference on Management of Data*, 2020, pp. 543–557.
* [113]

  A. Salau, R. Dantu, K. Morozov, S. Badruddoja, and K. Upadhyay, “Making blockchain validators honest,” in *2022 Fourth International Conference on Blockchain Computing and Applications (BCCA)*. IEEE, 2022, pp. 267–273.
* [114]

  C. Zhang, C. Wu, and X. Wang, “Overview of blockchain consensus mechanism,” in *Proceedings of the 2020 2nd International Conference on Big Data Engineering*, 2020, pp. 7–12.
* [115]

  L. Zhang, R. Zhou, Q. Liu, J. Xu, and C. Liu, “Transaction confirmation time estimation in the bitcoin blockchain,” in *International Conference on Web Information Systems Engineering*. Springer, 2021, pp. 30–45.
* [116]

  M. Asante, G. Epiphaniou, C. Maple, H. Al-Khateeb, M. Bottarelli, and K. Z. Ghafoor, “Distributed ledger technologies in supply chain security management: A comprehensive survey,” *IEEE Transactions on Engineering Management*, vol. 70, no. 2, pp. 713–739, 2021.
* [117]

  L. Liu, L. Wei, W. Zhang, M. Wen, Y. Liu, and S.-C. Cheung, “Characterizing transaction-reverting statements in ethereum smart contracts,” in *2021 36th IEEE/ACM International Conference on Automated Software Engineering (ASE)*. IEEE, 2021, pp. 630–641.
* [118]

  Z. Liao, S. Hao, Y. Nan, and Z. Zheng, “Smartstate: Detecting state-reverting vulnerabilities in smart contracts via fine-grained state-dependency analysis,” in *Proceedings of the 32nd ACM SIGSOFT International Symposium on Software Testing and Analysis*, 2023, pp. 980–991.
* [119]

  M. Rysman, “The economics of two-sided markets,” *Journal of economic perspectives*, vol. 23, no. 3, pp. 125–143, 2009.
* [120]

  J.-C. Rochet and J. Tirole, “Cooperation among competitors: Some economics of payment card associations,” *Rand Journal of economics*, pp. 549–570, 2002.
* [121]

  Helcim, “Merchant discount rate: How to calculate,” 2024, accessed: 23 Dec, 2025. [Online]. Available: https://www.helcim.com/guides/merchant-discount-rate/
* [122]

  Investopedia, “Understanding merchant discount rate: Definition & key fees explained,” 2025, accessed: 23 Dec, 2025. [Online]. Available: https://www.investopedia.com/terms/m/merchant-discount-rate.asp
* [123]

  E. Commission, “Regulation (eu) 2015/751 of the european parliament and of the council of 29 april 2015 on interchange fees for card-based payment transactions,” 2015, accessed: Nov. 19, 2025. [Online]. Available: https://eur-lex.europa.eu/eli/reg/2015/751/oj/eng
* [124]

  F. Reserve, “Regulation ii - average debit card interchange fee by payment card network,” 2024, accessed: Nov. 19, 2025. [Online]. Available: https://www.federalreserve.gov/paymentsystems/regii-average-interchange-fee.htm
* [125]

  A. Ho, S. Darbha, Y. Gorelkina, and A. García, “The relative benefits and risks of stablecoins as a means of payment: A case study perspective,” December 2022, accessed: Nov. 19, 2025. [Online]. Available: https://www.bankofcanada.ca/2022/12/staff-discussion-paper-2022-21
* [126]

  A. Donmez and A. Karaivanov, “Transaction fee economics in the ethereum blockchain,” *Economic Inquiry*, vol. 60, no. 1, pp. 265–292, 2022.
* [127]

  L. Gudgeon, P. Moreno-Sanchez, S. Roos, P. McCorry, and A. Gervais, “Sok: Layer-two blockchain protocols,” in *International Conference on Financial Cryptography and Data Security*. Springer, 2020, pp. 201–226.
* [128]

  C. Sguanci, R. Spatafora, and A. M. Vergani, “Layer 2 blockchain scaling: A survey,” *arXiv preprint arXiv:2107.10881*, 2021.
* [129]

  CoinLaw.io, “Gas fee markets on layer-2 statistics 2025: Key insights,” 2025. [Online]. Available: https://coinlaw.io/gas-fee-markets-on-layer-2-statistics
* [130]

  M. Li, B. Gao, K. Toyoda, Y. Yang, J. Samsudin, H. Zhang, S. Lu, T. H. Tng, K. Choo, and Q. Wei, “Mstablechain: Towards multi-native stablecoins in evm-compatible blockchain for stable fee and mass adoption,” *arXiv preprint arXiv:2410.22100*, 2024.
* [131]

  European Commission, “Report on the application of regulation (eu) 2015/751 on interchange fees for card-based payment transactions,” European Commission, Commission Staff Working Document SWD(2020) 118 final, June 2020.
* [132]

  Tidal Commerce, “Isa fee explained: Visa international service assessment,” 2023, accessed: Dec. 5, 2025. [Online]. Available: https://www.tidalcommerce.com/learn/isa-fee
* [133]

  Stripe, “Pricing and fees: International card costs,” 2025, accessed: Dec. 5, 2025. [Online]. Available: https://stripe.com/pricing
* [134]

  Circle Internet Financial, “Ushering in the next chapter for usdc,” 2023, centre governance brought in-house; Accessed Oct. 11, 2025. [Online]. Available: https://www.circle.com/blog/ushering-in-the-next-chapter-for-usdc
* [135]

  B. G. Ferrin and R. E. Plank, “Total cost of ownership models: An exploratory study,” *Journal of Supply chain management*, vol. 38, no. 2, pp. 18–29, 2002.
* [136]

  D. A. Zetzsche, F. Annunziata, D. W. Arner, and R. P. Buckley, “The markets in crypto-assets regulation (mica) and the eu digital finance strategy,” *Capital Markets Law Journal*, vol. 16, no. 2, pp. 203–225, 2021.
* [137]

  Monetary Authority of Singapore, “Mas finalises stablecoin regulatory framework,” August 2023, mandates 100% liquid asset backing and redemption within 5 business days. [Online]. Available: https://www.mas.gov.sg/news/media-releases/2023/mas-finalises-stablecoin-regulatory-framework
* [138]

  Hong Kong Monetary Authority, “Conclusion of discussion paper on crypto-assets and stablecoins,” HKMA, Tech. Rep., 2023, establishes the mandatory licensing regime for FRS issuers.
* [139]

  European Parliament and Council of the European Union, “Directive 98/26/ec of the european parliament and of the council of 19 may 1998 on settlement finality in payment and securities settlement systems,” 2024, accessed: Nov. 19, 2025. [Online]. Available: https://eur-lex.europa.eu/eli/dir/1998/26/oj/eng
* [140]

  A. Gervais, G. O. Karame, K. Wüst, V. Glykantzis, H. Ritzdorf, and S. Capkun, “On the security and performance of proof of work blockchains,” in *Proceedings of the 2016 ACM SIGSAC conference on computer and communications security*, 2016, pp. 3–16.
* [141]

  C. T. Nguyen, D. T. Hoang, D. N. Nguyen, D. Niyato, H. T. Nguyen, and E. Dutkiewicz, “Proof-of-stake consensus mechanisms for future blockchain networks: fundamentals, applications and opportunities,” *IEEE access*, vol. 7, pp. 85 727–85 745, 2019.
* [142]

  “General data protection regulation, article 17: Right to erasure,” 2016. [Online]. Available: https://gdpr-info.eu/art-17-gdpr
* [143]

  W. Liang, Y. Liu, C. Yang, S. Xie, K. Li, and W. Susilo, “On identity, transaction, and smart contract privacy on permissioned and permissionless blockchain: a comprehensive survey,” *ACM Computing Surveys*, vol. 56, no. 12, pp. 1–35, 2024.
* [144]

  A. Biryukov and S. Tikhomirov, “Deanonymization and linkability of cryptocurrency transactions based on network analysis,” in *2019 IEEE European symposium on security and privacy*. IEEE, 2019, pp. 172–184.
* [145]

  Y. Xiang, Y. Lei, D. Bao, T. Li, Q. Yang, W. Liu, W. Ren, and K.-K. R. Choo, “Babd: A bitcoin address behavior dataset for pattern analysis,” *IEEE Transactions on Information Forensics and Security*, vol. 19, pp. 2171–2185, 2023.
* [146]

  M. Finck, “Blockchains and data protection in the european union,” *Eur. Data Prot. L. Rev.*, vol. 4, p. 17, 2018.
* [147]

  U. Fiege, A. Fiat, and A. Shamir, “Zero knowledge proofs of identity,” in *Proceedings of the nineteenth annual ACM symposium on Theory of computing*, 1987, pp. 210–217.
* [148]

  X. Sun, F. R. Yu, P. Zhang, Z. Sun, W. Xie, and X. Peng, “A survey on zero-knowledge proof in blockchain,” *IEEE Network*, vol. 35, no. 4, pp. 198–205, 2021.
* [149]

  Y. Lindell, “Secure multiparty computation,” *Communications of the ACM*, vol. 64, no. 1, pp. 86–96, 2020.
* [150]

  H. Zhong, Y. Sang, Y. Zhang, and Z. Xi, “Secure multi-party computation on blockchain: An overview,” in *International symposium on parallel architectures, algorithms and programming*. Springer, 2019, pp. 452–460.
* [151]

  P. Jauernig, A.-R. Sadeghi, and E. Stapf, “Trusted execution environments: properties, applications, and challenges,” *IEEE Security & Privacy*, vol. 18, no. 2, pp. 56–60, 2020.
* [152]

  J. Lind, I. Eyal, F. Kelbert, O. Naor, P. Pietzuch, and E. G. Sirer, “Teechain: Scalable blockchain payments using trusted execution environments,” *arXiv preprint arXiv:1707.05454*, 2017.
* [153]

  N. Marangunić and A. Granić, “Technology acceptance model: a literature review from 1986 to 2013,” *Universal access in the information society*, vol. 14, no. 1, pp. 81–95, 2015.
* [154]

  V. Venkatesh and J. Thong, “Unified theory of acceptance and use of technology: A synthesis and the road ahead,” *Journal of the association for Information Systems*, 2016.
* [155]

  W. Quan, H. Moon, S. S. Kim, and H. Han, “Mobile, traditional, and cryptocurrency payments influence consumer trust, attitude, and destination choice: Chinese versus koreans,” *International Journal of Hospitality Management*, vol. 108, p. 103363, 2023.
* [156]

  M. S. Sangari and A. Mashatan, “What is driving consumer resistance to crypto-payment? a multianalytical investigation,” *Psychology & Marketing*, vol. 41, no. 3, pp. 575–591, 2024.
* [157]

  J. J. Si, T. Sharma, and K. Y. Wang, “Understanding user-perceived security risks and mitigation strategies in the web3 ecosystem,” in *Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems*, 2024, pp. 1–22.
* [158]

  M. Y. Guan, Y. Yu, T. Sharma, M. Z. Huang, K. Qin, Y. Wang, and K. Y. Wang, “Security perceptions of users in stablecoins: Advantages and risks within the cryptocurrency ecosystem,” in *2025 IEEE Symposium on Security and Privacy (SP)*. IEEE, 2025, pp. 2753–2771.
* [159]

  C. S. Henry, K. P. Huynh, and G. Nicholls, “Bitcoin awareness and usage in canada,” *Journal of Digital Banking*, vol. 2, no. 4, pp. 311–337, 2018.
* [160]

  S. Schuh and O. Shy, “Us consumers’ adoption and use of bitcoin and other virtual currencies,” in *DeNederlandsche bank, Conference entitled “Retail payments: mapping out the road ahead*, 2016.
* [161]

  F. Shahzad, G. Xiu, J. Wang, and M. Shahbaz, “An empirical investigation on the adoption of cryptocurrencies among the people of mainland china,” *Technology in Society*, vol. 55, pp. 33–40, 2018.
* [162]

  M. Polasik, A. I. Piotrowska, T. P. Wisniewski, R. Kotkowski, and G. Lightfoot, “Price fluctuations and the use of bitcoin: An empirical inquiry,” *International journal of electronic commerce*, vol. 20, no. 1, pp. 9–49, 2015.
* [163]

  J. Silinskyte, “Understanding bitcoin adoption: Unified theory of acceptance and use of technology (utaut) application (master’s thesis),” *University Leiden*, 2014.
* [164]

  I. Malakhov, A. Marin, and S. Rossi, “Analysis of the confirmation time in proof-of-work blockchains,” *Future Generation Computer Systems*, vol. 147, pp. 275–291, 2023.
* [165]

  Y. Kawase and S. Kasahara, “Priority queueing analysis of transaction-confirmation time for bitcoin.” *Journal of Industrial & Management Optimization*, vol. 16, no. 3, 2020.
* [166]

  T. Moore, “The economics of cybersecurity: Principles and policy options,” *International Journal of Critical Infrastructure Protection*, vol. 3, no. 3-4, pp. 103–117, 2010.
* [167]

  V. Gramoli, R. Guerraoui, A. Lebedev, and G. Voron, “Stabl: Blockchain fault tolerance,” *arXiv preprint arXiv:2409.13142*, 2024.
* [168]

  M. Castro, B. Liskov *et al.*, “Practical byzantine fault tolerance,” in *USENIX Symposium on Operating Systems Design and Implementation*, vol. 99, no. 1999, 1999, pp. 173–186.
* [169]

  J. Sousa, A. Bessani, and M. Vukolic, “A byzantine fault-tolerant ordering service for the hyperledger fabric blockchain platform,” in *2018 48th annual IEEE/IFIP international conference on dependable systems and networks*. IEEE, 2018, pp. 51–58.
* [170]

  R. Böhme, N. Christin, B. Edelman, and T. Moore, “Bitcoin: Economics, technology, and governance,” *Journal of economic Perspectives*, vol. 29, no. 2, pp. 213–238, 2015.
* [171]

  S. Motepalli, L. Freitas, and B. Livshits, “Sok: Decentralized sequencers for rollups,” *arXiv preprint arXiv:2310.03616*, 2023.
* [172]

  L. T. Thibault, T. Sarry, and A. S. Hafid, “Blockchain scaling using rollups: A comprehensive survey,” *IEEE Access*, vol. 10, pp. 93 039–93 054, 2022.
* [173]

  P. McCorry, C. Buckland, B. Yee, and D. Song, “Sok: Validating bridges as a scaling solution for blockchains,” *Cryptology ePrint Archive*, 2021.
* [174]

  R. Anderson, *Security engineering: a guide to building dependable distributed systems*. John Wiley & Sons, 2010.
* [175]

  E. A. Morse and V. Raval, “Pci dss: Payment card industry data security standards in context,” *Computer Law & Security Review*, vol. 24, no. 6, pp. 540–554, 2008.
* [176]

  K. Karantias, “Sok: A taxonomy of cryptocurrency wallets,” *Cryptology ePrint Archive*, 2020.
* [177]

  D. He, Z. Deng, Y. Zhang, S. Chan, Y. Cheng, and N. Guizani, “Smart contract vulnerability analysis and security audit,” *IEEE Network*, vol. 34, no. 5, pp. 276–282, 2020.
* [178]

  Y. Zhuang, Z. Liu, P. Qian, Q. Liu, X. Wang, and Q. He, “Smart contract vulnerability detection using graph neural networks,” in *Proceedings of the twenty-ninth international conference on international joint conferences on artificial intelligence*, 2021, pp. 3283–3290.
* [179]

  C. Chen, J. Su, J. Chen, Y. Wang, T. Bi, J. Yu, Y. Wang, X. Lin, T. Chen, and Z. Zheng, “When chatgpt meets smart contract vulnerability detection: How far are we?” *ACM Transactions on Software Engineering and Methodology*, vol. 34, no. 4, pp. 1–30, 2025.
* [180]

  M. L. Katz and C. Shapiro, “Network externalities, competition, and compatibility,” *The American economic review*, vol. 75, no. 3, pp. 424–440, 1985.
* [181]

  J. Farrell and G. Saloner, “Installed base and compatibility: Innovation, product preannouncements, and predation,” *The American economic review*, pp. 940–955, 1986.
* [182]

  Nilson, “Worldwide card acceptance locations for global brands midyear 2024,” 2024, accessed: Nov. 27, 2025. [Online]. Available: https://nilsonreport.com/articles/worldwide-card-acceptance-locations-for-global-brands-midyear-2024
* [183]

  C. Li, R. Xu, B. Palanisamy, L. Duan, M. Shen, J. Liu, and W. Wang, “Blockchain takeovers in web 3.0: An empirical study on the tron-steem incident,” *ACM Transactions on the Web*, vol. 19, no. 2, pp. 1–23, 2025.
* [184]

  T. Xie, J. Zhang, Z. Cheng, F. Zhang, Y. Zhang, Y. Jia, D. Boneh, and D. Song, “zkbridge: Trustless cross-chain bridges made practical,” in *Proceedings of the 2022 ACM SIGSAC Conference on Computer and Communications Security*, 2022, pp. 3003–3017.
* [185]

  S.-S. Lee, A. Murashkin, M. Derka, and J. Gorzny, “Sok: Not quite water under the bridge: Review of cross-chain bridge hacks,” in *2023 IEEE International Conference on Blockchain and Cryptocurrency*. IEEE, 2023, pp. 1–14.
* [186]

  Chainalysis, “The 2023 crypto crime report,” 2023, accessed: Nov. 19, 2025. [Online]. Available: https://www.chainalysis.com/blog/2023-crypto-crime-report-introduction
* [187]

  World Bank, “Remittance prices worldwide quarterly report (issue 49),” The World Bank Group, Tech. Rep., March 2024. [Online]. Available: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099053025155726868
* [188]

  F. News, “Dlocal partners with moneygram to expand leading international payment services in high growth markets,” 2024, accessed: 24 Dec, 2025. [Online]. Available: https://ffnews.com/newsarticle/paytech/dlocal-partners-with-moneygram-to-expand-leading-international-payment-services-in-high-growth-markets
* [189]

  K. Jhanji, K. Burchardi, Y. H. Zhang, C. Bravo, T. Hung, B. Kronfellner, and H. Samad, “Stablecoins: Five killer tests to gauge their potential,” Boston Consulting Group, White Paper, May 2025. [Online]. Available: https://media-publications.bcg.com/Stablecoins-five-killer-tests-to-gauge-their-potential.pdf
* [190]

  V. Buterin, Y. Weiss, D. Tirosh *et al.*, “Erc-4337: Account abstraction using alt mempool,” 2021. [Online]. Available: https://eips.ethereum.org/EIPS/eip-4337
* [191]

  Worldpay, “Usdc role in payment landscape grows,” 2022, accessed: Nov. 27, 2025. [Online]. Available: https://www.worldpay.com/en/insights/articles/usdc-stablecoin-circle
* [192]

  Nuvei, “Nuvei launches comprehensive blockchain payment solution for cross-border b2b payments,” December 2024, accessed: Nov. 27, 2025. [Online]. Available: https://www.nuvei.com/posts/nuvei-launches-comprehensive-blockchain-payment-solution
* [193]

  PayPal, “Paypal launches u.s. dollar stablecoin,” August 2023, accessed: Nov. 27, 2025. [Online]. Available: https://newsroom.paypal-corp.com/2023-08-07-PayPal-Launches-U-S-Dollar-Stablecoin
* [194]

  Visa, “Visa expands stablecoin settlement capabilities to merchant acquirers,” September 2023, accessed: Nov. 27, 2025. [Online]. Available: https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.19881.html
* [195]

  L. Breidenbach *et al.*, “Chainlink 2.0: Next steps in the evolution of decentralized oracle networks,” Chainlink Labs, Tech. Rep., 2021. [Online]. Available: https://research.chain.link/whitepaper-v2.pdf
* [196]

  R. Belchior, A. Vasconcelos, S. Guerreiro, and M. Correia, “A survey on blockchain interoperability: Past, present, and future trends,” *ACM Computing Surveys*, vol. 54, no. 8, pp. 1–41, 2021.
* [197]

  Bank for International Settlements, “Annual economic report 2023. chapter iii: Blueprint for the future monetary system: improving the old, enabling the new,” Tech. Rep., 2023. [Online]. Available: https://www.bis.org/publ/arpdf/ar2023e3.htm
* [198]

  ——, “Application of the pfmi to stablecoin arrangements: Final report and accompanying report,” accessed: Oct. 10, 2025. [Online]. Available: https://www.bis.org/cpmi/publ/d207.htm
* [199]

  R. Auer, J. Frost, L. Gambacorta, C. Monnet, T. Rice, and H. S. Shin, “Central bank digital currencies: motives, economic implications, and the research frontier,” *Annual review of economics*, vol. 14, no. 1, pp. 697–721, 2022.
* [200]

  S. Prodan, P. Konhäusner, D.-C. Dabija, G. Lazaroiu, and L. Marincean, “The rise in popularity of central bank digital currencies. a systematic review,” *Heliyon*, vol. 10, no. 9, 2024.
* [201]

  Bank for International Settlements, “Tokenisation in the context of money and other assets,” 2024. [Online]. Available: https://www.bis.org/cpmi/publ/d225.pdf
* [202]

  T. N. Al-Tawil, “Anti-money laundering regulation of cryptocurrency: Uae and global approaches,” *Journal of Money Laundering Control*, vol. 26, no. 6, pp. 1150–1164, 2023.