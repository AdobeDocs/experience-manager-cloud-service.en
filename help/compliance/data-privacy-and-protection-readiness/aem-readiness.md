---
title: Data Protection and Data Privacy Regulations - Adobe Experience Manager as a Cloud Service Readiness
description: Learn about Adobe Experience Manager as a Cloud Service support for the various Data Protection and Data Privacy Regulations, and how to comply when implementing a new AEM as a Cloud Service project. These regulations include the EU General Data Protection Regulation (GDPR), the California Consumer Privacy Act.
exl-id: 5dfa353b-84c5-4b07-bfcd-b03c2d361553
feature: Compliance
role: "Admin, Architect, Developer, Leader"
---
# Adobe Experience Manager as a Cloud Service Readiness for Data Protection and Data Privacy Regulations {#aem-readiness-for-data-protection-and-data-privacy-regulations}

>[!WARNING]
>
>The contents of this document do not constitute legal advice and are not meant as a substitute for legal advice. 
>
>Consult your company's legal department for advice concerning Data Protection and Data Privacy regulations. 

>[!NOTE]
>
>For more information about Adobe's responses to privacy issues, and what these responses mean for you as an Adobe customer, see [Adobe's Privacy Center](https://www.adobe.com/privacy.html). 

To help Adobe customers be compliant with these regulations, Adobe is providing documentation and procedures (with APIs when available) for the customer privacy administrators and AEM administrators:

* The documentation helps administrators handle data protection, and data privacy requests. 
* The procedures documented let customers run the regulatory requests manually or make API calls, where available, from an external portal or service. 

>[!CAUTION]
>
>The details documented here are restricted to Adobe Experience Manager as a Cloud Service. 
>
>Data from another Adobe On-demand Service, together with any related privacy requests, require actions to be taken on that service.
>
>For more information, see [Adobe's Privacy Center](https://www.adobe.com/privacy.html).

## Introduction {#introduction}

Instances of Adobe Experience Manager as a Cloud Service, and the applications that run on them, are owned and operated by Adobe customers.

As a consequence, data protection regulations, such as GDPR, CCPA, and others, are largely the responsibility of the customers.

As a brief introduction, the regulations for data privacy and protection include new rules to be followed by the roles of:

* Business Entities (CCPA) and/or Data Controllers (GDPR) 

* Service Providers (CCPA) and/or Data Processors (GDPR) 

The main provisions in such regulations are:

1. Expanded definition of personal data to include all unique IDs; as in directly and indirectly identifiable data.

2. Strengthened consent requirements.

3. Increased focus on deletion rights (Data Erasure).

4. Opt-Out of Sale of Data.

For Adobe Experience Manager as a Cloud Service:

* The instances, and applications that run on them, are owned and operated by the customer. 

  * Ownership effectively means that the customer manages the regulatory roles, including Business Entities and Service Provider, Data Controller, and Data Processor, among others. 

  * The Adobe Experience Platform Privacy Service is not part of the workflow for AEM, as illustrated in the diagram below. 

* AEM includes documentation and procedures for the customer's privacy administrator and/or AEM administrator to execute the privacy regulation requests; either manually or through APIs, when available.

* No new service or UI has been added.

  * Instead procedures and APIs are documented for use by the customer UIs/portals that handle privacy regulation requests.

* AEM does not include any out-of-the-box tooling to support the privacy requests workflow. 

  * Adobe provides documentation and procedures for the customer's privacy administrator, AEM administrator, or both, enabling them to manually run requests related to the privacy regulations.

Adobe is providing procedures for handling privacy requests related to Access, Delete, and Opt-Out for Adobe Experience Manager as a Cloud Service. For some cases there are APIs available that can be called from a customer developed portal, or scripts to help with automation.

The following diagram illustrates what a privacy request workflow might look like (illustrated using Adobe Experience Manager 6.5):

![Data Protection and Privacy](assets/data-protection-and-privacy-01.png)

## Adobe Experience Manager as a Cloud Service and Regulatory Readiness {#aem-as-a-cloud-service-and-regulatory-readiness}

See the sections below for regulatory documentation for product areas of AEM as a Cloud Service.

## Adobe Experience Manager as a Cloud Service Foundation {#aem-foundation}

See [AEM Foundation Readiness for Data Protection and Data Privacy Regulations](/help/compliance/data-privacy-and-protection-readiness/foundation-readiness.md).

## Adobe Experience Manager as a Cloud Service Sites {#aem-sites}

See [AEM Sites Readiness for Data Protection and Data Privacy Regulations](/help/compliance/data-privacy-and-protection-readiness/sites-readiness.md)

## Adobe Experience Manager as a Cloud Service Integration with Adobe Target & Adobe Analytics {#aem-integration-with-adobe-target-adobe-analytics}

Integrations of Adobe Experience Manager as a Cloud Service with Adobe Target and Adobe Analytics are implemented with data protection and privacy (for example, GDPR) ready services. No personal data from Adobe Target or Adobe Analytics is stored in AEM in relation to the integrations.
For more information, see:

* [Adobe Target - Privacy Overview](https://experienceleague.adobe.com/docs/target-dev/developer/implementation/privacy/cmp-privacy-and-general-data-protection-regulation.html)  

* [Adobe Analytics Data Privacy Workflow](https://experienceleague.adobe.com/docs/analytics/admin/admin-tools/data-governance/an-gdpr-workflow.html)
