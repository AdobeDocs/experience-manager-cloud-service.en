---
title: HIPAA readiness for Adobe Experience Manager as a Cloud Service
description: Learn about Experience Manager as a Cloud Service Sites support for the HIPAA Regulations, and how to comply when implementing a new AEM as a Cloud Service project.
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

For Adobe Experience Manager (AEM) as a Cloud Service, Adobe is providing documentation to help you understand HIPPA readiness. It can help you become compliant with these regulations. 

## Health Insurance Portability and Accountability Act (HIPAA) {#health-insurance-portability-and-accountability-act-hipaa}

The Health Insurance Portability and Accountability Act (HIPAA) is the key federal healthcare privacy law in the United States and is enforced by the U.S. Department of Health and Human Services (HHS). 

HIPAA applies to Covered Entities (such as healthcare providers, insurers, and clearinghouses) and Business Associates (such as those entities that provide services to covered entities). HIPAA requirements are set across three separate rules: Privacy Rule, Security Rule, and Breach Notification Rule. 

Adobe acts as a Business Associate for certain products, which Adobe classifies as “HIPAA-Ready Services.” Data regulated under HIPAA is referred to as Protected Health Information or PHI. PHI is a subset of health information that:

1. is created or received by a healthcare provider, health plan, or healthcare clearinghouse, 
1. relates to the past, present, or future physical or mental health or condition of an individual, the provision of healthcare to an individual, or the past, present, or future payment for the provision of healthcare to an individual, 
1. identifies the individual or with respect to which there is a reasonable basis to believe that the information can be used to identify the individual. 

The HIPAA Privacy and Security Rules require that a Covered Entity obtain written assurances from a Business Associate in the form of a Business Associate Agreement, or BAA, requiring the Business Associate to safeguard the privacy and security of the Covered Entityʼs PHI. 

For more information, see [HIPAA and Adobe Products and Services](https://www.adobe.com/trust/compliance/hipaa-hds/hipaa-ready.html) in the Adobe Trust Center.

## HIPAA terminology {#hipaa-terminology}

A service is labeled *HIPAA-ready* or *not HIPAA-ready* based on the outcome of its HIPAA assessment. However, some services did not require a HIPAA assessment; for example, the Universal Editor. 


|HIPAA-ready? | Can be integrated with HIPAA-ready services | Can be included in the SKU: Extended Security for Healthcare | Statements about HIPAA [2] | Why? |
|--- |--- |--- |--- |--- |
|**Yes**, HIPAA-ready |Yes |Yes |"A HIPAA-ready service" |Handles consumer-level data, **and** processes, transmits, and/or stores ePHI. |
|**Not necessary** to conduct a HIPAA assessment |Yes |Yes |"Included in our HIPAA-ready service" [1] |Not a service that handles consumer-level data. Just customer-level data. |
|**No**, not HIPAA-ready |No |No |"Not HIPAA-ready" |Has not conducted a HIPAA assessment internally or externally to determine HIPAA scope. |

>[!NOTE]
>
>[1]: Applies only to decisions made at the time the PLA/PIA was completed for the documented use case.
>[2]: These are approved baseline statements. Marketing, contracts, Trust Center and other official customer-facing documents may contain different language.
>
>Only Product Legal and Privacy Legal make the decision to label a service either HIPAA-ready, not HIPAA-ready, or "Not necessary".

## AEM as a Cloud Service Compliance Listings {#aem-as-a-cloud-service-compliance-listings}

Individual services within AEM as a Cloud have differing compliance ratings. See the following table.

|Product/Capability |Service |HIPAA-ready? |Statements |
|--- |--- |--- |--- |
|AEM Sites |Universal Editor |Not necessary |"Included in our HIPAA-ready service" |
|AEM Sites |Edge Delivery Services |Yes |"A HIPAA-ready service" |
|AEM Sites Optimizer |Sites Optimizer |Not necessary |"Included in our HIPAA-ready service" |
|AEM Assets |Content Hub |Not necessary |"Included in our HIPAA-ready service" |
|AEM Assets |Brand Portal | | |
|AEM Assets |Dynamic Media Scene 7 |No |"Not HIPAA-ready" |
|AEM Forms |Authentication Facade Service |Yes |"A HIPAA-ready service" |
|AEM Forms |PDF Utility Service |Yes |"A HIPAA-ready service" |
|LLM Optimizer |LLM Optimizer |Not necessary |"Included in our HIPAA-ready service" |
|AEM CIF |Commerce Integration Framework | | |
|AEM Cloud Manager |Cloud Manager |Yes |"A HIPAA-ready service" |
|AEM Cloud Foundation |Release Orchestrator |Yes |"A HIPAA-ready service" |
|AEM Cloud Foundation |Release Toggles |Yes |"A HIPAA-ready service" |
|AEM Cloud Foundation |Release Validator |Yes |"A HIPAA-ready service" |
|AEM Cloud Foundation |Software Distribution |Not necessary |"Included in our HIPAA-ready service" |

