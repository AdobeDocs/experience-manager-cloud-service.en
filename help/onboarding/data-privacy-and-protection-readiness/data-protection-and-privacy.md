---
title: Data Protection and Data Privacy Regulations - AEM Readiness
seo-title: AEM Readiness for Data Protection and Data Privacy Regulations; such as GDPR, CCPA, etc
description: Learn about Adobe Experience Manager as a Cloud Service support for the various Data Protection and Data Privacy Regulations; including the EU General Data Protection Regulation (GDPR), the California Consumer Privacy Act and how to comply when implementing a new AEM as a Cloud Service project. 
seo-description: Learn about Adobe Experience Manager as a Cloud Service support for the various Data Protection and Data Privacy Regulations; including the EU General Data Protection Regulation (GDPR), the California Consumer Privacy Act and how to comply when implementing a new AEM as a Cloud Service project. 
---

# AEM Readiness for Data Protection and Data Privacy Regulations {#aem-readiness-for-data-protection-and-data-privacy-regulations}

>[!WARNING]
>THIS PAGE IS FOR INTERNAL DOCUMENTATION ONLY.
>THE CONTENT OF THIS PAGE IS CURRENTLY SUBJECT TO THE LEGAL REVIEW, AND IS ALSO WAITING FOR CONFIRMATION ON CERTAIN TECHNICAL DETAILS.

>[!WARNING]
>
>The contents of this document do not constitute legal advice and are not meant as a substitute for legal advice. 
>
>Please consult your company's legal department for advice concerning Data Protection and Data Privacy regulations. 

>[!NOTE]
>
>For more information about Adobe's response to privacy issues, and what this means for you as an Adobe customer, see [Adobe's Privacy Center](https://www.adobe.com/privacy.html). 

Adobe is providing documentation and procedures (with APIs when available), for the customer privacy administrator or AEM administrator to handle data protection and data privacy requests and help our customers be compliant with these regulations. The procedures documented will allow customers to execute the regulatory requests manually or by calling into APIs, where available, from an external portal or service. 

>[!CAUTION]
>
>The details documented here are restricted to Adobe Experience Manager as a Cloud Service. 
>
>Data from another Adobe Service, together with any related privacy requests, will require actions to be taken on that service.
>
>For further information see [Adobe's Privacy Center](https://www.adobe.com/privacy.html).

## Introduction {#introduction}

Instances of Adobe Experience Manager as a Cloud Service, and the applications that run on them, are owned and operated by our customers.

As a consequence, data protection regulations, such as GDPR, CCPA, and others, are largely the responsibility of the customers.

As a very brief introduction, the regulations for data privacy and protection include new rules to be followed by the roles of:

* Business Entities (CCPA) and/or Data Controllers (GDPR) 

* Service Providers (CCPA) and/or Data Processors (GDPR) 

The main provisions in such regulations are:

1. Expanded definition of personal data to include all unique IDs; as in directly and indirectly identifiable data.

2. Strengthened consent requirements.

3. Increased focus on deletion rights (Data Erasure).

4. Opt-Out of Sale of Data.

For Adobe Experience Manager as a Cloud Service:

* The instances, and applications that run on them, are owned and operated by the customer. 

  * This effectively means that the customer manages the regulatory roles, including Business and Service Provider, Data Controller, and Data Processor, amongst others. 

  * The Adobe privacy service will not be part of the workflow for AEM, as illustrated in the diagram below. 

* AEM provides documentation and procedures for the customer's Privacy Administrator and/or AEM Administrator to execute the Privacy regulation requests; either manually or through APIs, when available.

* No new service or UI has been added.

  * Instead procedures and APIs are documented for use by the customer UIs/portals that handle privacy regulation requests.

* AEM will not include any out-of-the-box tooling to support the privacy requests workflow. 

  * Adobe will provide documentation and procedures for the customer's Privacy Administrator and/or AEM Administrator, enabling them to manually execute requests related to the privacy regulations.

Adobe is providing procedures for handling privacy requests related to Access, Delete and Opt-Out for Adobe Experience Manager as a Cloud Service. In some cases, there are APIs available that can be called from a customer developed portal or scripts to help with automation.

![Data Protection and Privacy](assets/data-protection-and-privacy-01.png)

## AEM as a Cloud Service and Regulatory Readiness {#aem-as-a-cloud-service-and-regulatory-readiness}

Please see the sections below for regulatory documentation for product areas of AEM as a Cloud Service.

## AEM Foundation {#aem-foundation}

See [AEM Foundation Readiness for Data Protection and Data Privacy Regulations](/help/onboarding/data-privacy-and-protection-readiness/data-protection-and-privacy-foundation.md).

## AEM Sites {#aem-sites}

See [AEM Sites Readiness for Data Protection and Data Privacy Regulations.](/help/onboarding/data-privacy-and-protection-readiness/data-protection-and-privacy-sites.md)

### AEM Integration with Adobe Target & Adobe Analytics {#aem-integration-with-adobe-target-adobe-analytics}

These AEM integrations are with GDPR ready services. No personal data from Adobe Target or Adobe Analytics is stored in AEM in relation to the integrations.

For further information see:

* [Adobe Target - Privacy Overview](https://docs.adobe.com/content/help/en/target/using/implement-target/before-implement/privacy/privacy.html)  

* [Adobe Analytics Data Privacy Workflow](https://docs.adobe.com/content/help/en/analytics/admin/data-governance/an-gdpr-workflow.html)
