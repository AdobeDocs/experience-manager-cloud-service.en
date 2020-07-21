---
title: Introduction to Commerce on AEM as a Cloud Service
description: What's new in Commerce on AEM as a Cloud Service.
---

# Introducing Commerce Integration Framework on AEM as a Cloud Service {#commerce-intro}

Commerce Integration Framework (CIF) on Experience Manager as a Cloud Service is Adobe's recommended pattern to integrate and extend commerce services from Magento and other third party commerce solutions with the Experience Cloud. This enables Adobe Customers to deliver extraordinary and personalized omnichannel shopping experience based on state-of-the-art technology.

The Commerce Integration Framework is an add-on module for Experience Manager as a Cloud Service and provides a set of authoring tools, components, and a reference storefront to accelerate development of integrations between Experience Manager as a Cloud Service and commerce solutions.


Adobe provides two versions of the Commerce Integration Framework:

|                         | CIF on-prem                                                                                                                                                                                            | CIF Cloud                                                                                                              |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Supported AEM versions  | AEM on-prem or AMS 6.x                                                                                                                                                                                 | AEM AMS 6.4 and 6.5                                                                                                    |
| Back-end                | - AEM, Java <br> - Monolithic integration, pre-build mapping (template)<br> - JCR repository                                                                                                                    | - Magento <br>- Java and Javascript <br>- No Commerce data stored in JCR repository                                            |
| Front-end               | AEM server-side rendered pages                                                                                                                                                                         | Mixed page application (hybrid rendering)                                                                              |
| Product catalog         | - Product importer, editor, caching in AEM <br>- Regular catalogs with AEM or proxy pages                                                                                                                  | - No product import <br>- Generic templates <br>- On-demand data via connector                                                 |
| Scalability             | - Can support up to a few million products (depends on the use-case) <br> - Caching on Dispatcher                                                                                                           | - No volume limitation <br>- Caching on Dispatcher or CDN                                                                  |
| Standardized data model | No                                                                                                                                                                                                     | Yes, Magento GraphQL schema                                                                                            |
| Availability            | Yes:<br> - SAP Commerce Cloud (Extension updated to support AEM 6.4 and Hybris 5 (default) and maintains compatibility with Hybris 4 <br>- Salesforce Commerce Cloud (Connector open-sourced to support AEM 6.4) | Yes via open source via GitHub. <br> Magento Commerce (Supports Magento 2.3.2 (default) and compatible with Magento 2.3.1). |
| When to use             | Limited use-cases: For scenarios where small, static catalogs may need to be imported                                                                                                                  | Preferred solution in most use-cases    
