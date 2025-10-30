---
title: HIPAA readiness for Adobe Experience Manager as a Cloud Service
description: Learn about Experience Manager as a Cloud Service support for the HIPAA Regulations, and how to comply when implementing a new AEM as a Cloud Service project.
feature: Compliance
role: Admin, Architect, Developer, Leader
---
# HIPAA readiness for Adobe Experience Manager as a Cloud Service {#hipaa-readiness-for-adobe-experience-manager-as-a-cloud-service}

>[!WARNING]
>
>The contents of this document do not constitute legal advice and are not meant as a substitute for legal advice. 
>
>Consult your company's legal department for advice concerning HIPAA regulations. 

>[!NOTE]
>
>For more information about Adobe's response to privacy issues, and what this means for you as an Adobe customer, see:
>
>* [HIPAA and Adobe Products and Services](https://www.adobe.com/trust/compliance/hipaa-hds/hipaa-ready.html) in the Adobe Trust Center
>* [Adobe's Privacy Center](https://www.adobe.com/privacy.html)

For Adobe Experience Manager (AEM) as a Cloud Service, Adobe is providing documentation to help you understand HIPAA readiness. It can help you become compliant with these regulations. 

## Health Insurance Portability and Accountability Act (HIPAA) {#health-insurance-portability-and-accountability-act-hipaa}

The Health Insurance Portability and Accountability Act (HIPAA) is the key federal healthcare privacy law in the United States and is enforced by the U.S. Department of Health and Human Services (HHS). 

HIPAA applies to Covered Entities (such as healthcare providers, insurers, and clearinghouses) and Business Associates (such as those entities that provide services to covered entities). HIPAA requirements are set across three separate rules: Privacy Rule, Security Rule, and Breach Notification Rule. 

Adobe acts as a Business Associate for certain products, which Adobe classifies as “HIPAA-Ready Services.” Data regulated under HIPAA is referred to as Protected Health Information or PHI. PHI is a subset of health information that:

1. is created or received by a healthcare provider, health plan, or healthcare clearinghouse, 
1. relates to the past, present, or future physical or mental health or condition of an individual, the provision of healthcare to an individual, or the past, present, or future payment for the provision of healthcare to an individual, 
1. identifies the individual or with respect to which there is a reasonable basis to believe that the information can be used to identify the individual. 

The HIPAA Privacy and Security Rules require that a Covered Entity obtain written assurances from a Business Associate in the form of a Business Associate Agreement, or BAA, requiring the Business Associate to safeguard the privacy and security of the Covered Entityʼs PHI. 

For more information, see [HIPAA and Adobe Products and Services](https://www.adobe.com/trust/compliance/hipaa-hds/hipaa-ready.html) in the Adobe Trust Center.

## HIPAA assessment - terminology {#hipaa-assessment-terminology}

A service is labeled *HIPAA-ready* or *not HIPAA-ready* based on the outcome of its HIPAA assessment. Some services did not require a HIPAA assessment; for example, the Universal Editor. 

|HIPAA-ready? | Statements about HIPAA [1] | Why? | Can be integrated with HIPAA-ready services | Can be included in the SKU: Extended Security for Healthcare |
|--- |--- |--- |--- |--- |
|**Yes**, HIPAA-ready |A HIPAA-ready service |Handles consumer-level data, **and** processes, transmits, and/or stores ePHI. |Yes |Yes |
|**Not necessary** to conduct a HIPAA assessment |Included in our HIPAA-ready service [2] |Not a service that handles consumer-level data. Just customer-level data. |Yes |Yes |
|**No**, not HIPAA-ready |Not HIPAA-ready |Has not conducted a HIPAA assessment internally or externally to determine HIPAA scope. |No |No |

>[!NOTE]
>
>[1]: These are approved baseline statements. Marketing, contracts, Trust Center and other official customer-facing documents may contain different language.
>
>[2]: Applies only to decisions made at the time the Product Legal Assessment (PLA) and Privacy Impact Assessment (PIA) were completed for the documented use case.
>
>Only Product Legal and Privacy Legal make the decision to label a service either HIPAA-ready, not HIPAA-ready, or "Not necessary".

## Compliance of services in AEM as a Cloud Service {#compliance-of-services-in-aem-as-a-cloud-service}

Individual services within AEM as a Cloud have individual compliance ratings, based on the [assessment ratings](#hipaa-assessment-terminology). 

See the following table for compliance ratings, together with the [Additional Requirements](#additional-requirements).

|Product/Capability |Service |Statements |
|--- |--- |--- |
|AEM Sites |AEM Publish/Universal Editor |Included in our HIPAA-ready service |
|AEM Sites |Edge Delivery Services |A HIPAA-ready service |
|AEM Sites Optimizer |Sites Optimizer |Included in our HIPAA-ready service |
|AEM Assets |Content Hub |Included in our HIPAA-ready service |
|AEM Assets |Brand Portal | |
|AEM Assets |Dynamic Media Scene 7 |Not HIPAA-ready |
|AEM Forms |Authentication Facade Service |A HIPAA-ready service |
|AEM Forms |PDF Utility Service |A HIPAA-ready service |
|AEM CIF |Commerce Integration Framework | |
|AEM Cloud Manager |Cloud Manager |A HIPAA-ready service |
|AEM Cloud Foundation |Release Orchestrator |A HIPAA-ready service |
|AEM Cloud Foundation |Release Toggles |A HIPAA-ready service |
|AEM Cloud Foundation |Release Validator |A HIPAA-ready service |
|AEM Cloud Foundation |Software Distribution |Included in our HIPAA-ready service |
| | | |
|AEM Guides |Guides | |
| | | |
|LLM Optimizer |LLM Optimizer |Included in our HIPAA-ready service |

### Additional Requirements {#additional-requirements}

[Services listed](#compliance-of-services-in-aem-as-a-cloud-service) as HIPAA-ready (also referred to as a HIPAA-ready service) require the purchase of Extended Security for Healthcare. 

When Extended Security for Healthcare is purchased, there is the requirement that:

* the products selected for that program are HIPAA-ready (as listed in the table), 
* and Extended Security for Healthcare has been purchased for *each* product; this requires sufficient Cloud Manager Credits.

If the requirements are fulfilled, Extended Security for Healthcare can be applied upon AEM program creation; see [Setup](#setup) for details. 

>[!NOTE]
>
>For more details on provisioning, and pricing, reach out to your sales representative.

## Environments {#environments}

*HIPAA-ready* does not apply to RDE (Rapid Development Environment), Dev, or Stage environments, as these environments should not contain PHI. 

It is accepted best practice to:

* use dummy data for development and testing purposes
* only access PHI from production environments

The following table shows where the environment types are supported as HIPAA-ready.

|Product/Capability |RDE |Dev |Stage |Prod |
|--- |--- |--- |--- |--- |
|AEM Sites |No |No |No |Yes |
|AEM Assets |No |No |No |Yes |
|AEM Forms |No |No |No |Yes |
|Cloud Manager |No |No |No |Yes |
|Content Hub |No |No |No |Yes |
|Dynamic Media with OpenAPI |No |No |No |Yes |
|Dynamic Media (Scene7)/Brand Portal |No |No |No |No |
|Asset Share/Assets Essentials |No |No |No |No |
|Release Orchestrator |No |No |No |No |

## Setup {#setup}

When you [Create Production Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md), the [Security tab provides the options to activate HIPAA protection](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md#security).