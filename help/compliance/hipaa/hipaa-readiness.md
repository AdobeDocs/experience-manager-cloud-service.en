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

### The Health Insurance Portability and Accountability Act (HIPAA) {#the-health-insurance-portability-and-accountability-act-hipaa}

The HIPAA Privacy, Security, and Breach Notification Rules establish important protections for individually identifiable health information known as Protected Health Information (PHI).

Under HIPAA, a covered entity is a healthcare provider, health plan, or a healthcare clearinghouse. A business associate is an entity that provides services to a covered entity that involves access to PHI. The HIPAA Privacy and Security Rules require that a covered entity obtain written assurances from a business associate in the form of a Business Associate Agreement (BAA) requiring the business associate to safeguard the privacy and security of the Covered Entity’s PHI.

### Providing PHI to Adobe {#providing-phi-to-adobe}

Adobe acts as a Business Associate for its HIPAA-ready Services, listed under [HIPAA readiness of services in AEM as a Cloud Service](#hipaa-readiness-of-services-in-aem-as-a-cloud-service).

Customers that license any Adobe HIPAA-ready Service to process PHI **must** have the correct license and a signed BAA with Adobe. 

>[!IMPORTANT]
>
>Customers are not permitted to create, receive, maintain, or transmit PHI through Adobe products and services that are not designated as a HIPAA-ready Services or without the appropriate license to use a HIPAA-ready Service.

### HIPAA Shared Responsibilities {#hipaa-shared-responsibilities}

Adobe HIPAA-ready Services rely on a shared responsibility security model, requiring the customer and Adobe each to bear distinct responsibilities for maintaining the security of PHI. Under this shared security model, Adobe relies on the customer to use and configure the HIPAA-ready Services consistent with HIPAA.

For more information on executing an Adobe BAA for HIPAA-ready Services, please contact your Adobe sales representative or customer success manager.

>[!IMPORTANT]
>
>**Disclaimer**: 
>
>Customer is responsible for their use of Adobe HIPAA-ready Services and for ensuring that the Adobe HIPAA-ready Services meet their compliance requirements.

For more information, see [HIPAA and Adobe Products and Services](https://www.adobe.com/trust/compliance/hipaa-hds/hipaa-ready.html) in the Adobe Trust Center.

## HIPAA terminology {#hipaa-terminology}

The following table describes how AEM services are categorized for HIPAA usage. 

|HIPAA readiness | Description |
| --- | --- |
| HIPAA-ready | Designed to process PHI when configured appropriately and used with a BAA. |
| Not HIPAA-ready | Not designed to process PHI and must not be used in HIPAA-related use cases. |

>[!NOTE]
>
>HIPAA readiness classifications are based on the intended functionality of each service and may change over time. 
>
>Customers should refer to the most current documentation and applicable contractual terms when planning HIPAA-related deployments.

## HIPAA readiness of services in AEM as a Cloud Service {#hipaa-readiness-of-services-in-aem-as-a-cloud-service}

The following table describes which AEM services are HIPAA-ready and which services may be used alongside them. HIPAA-ready services require the purchase of Extended Security for Healthcare, as described under [Additional Requirements](#additional-requirements). 

| Product/Capability | Service(s) | HIPAA readiness |
| --- | --- | --- |
| AEM Sites | AEM Sites, AEM Publish, Edge Delivery Services | HIPAA-ready |
| AEM Sites | Universal Editor | Not HIPAA-ready<br>Can be added to an Extended Security Program when no PHI is introduced. |
| AEM Sites Optimizer |Sites Optimizer | Not HIPAA-ready<br>Can be added to an Extended Security Program when no PHI is introduced. |
| AEM Assets | AEM Assets | HIPAA-ready |
| AEM Assets | Content Hub | Not HIPAA-ready<br>Can be added to an Extended Security Program when no PHI is introduced. |
| AEM Assets | Brand Portal | Not HIPAA-ready |
| AEM Assets | Dynamic Media OpenAPI | Not HIPAA-ready<br>Can be added to an Extended Security Program when no PHI is introduced. |
| AEM Assets | Dynamic Media Scene 7 | Not HIPAA-ready |
| AEM Forms | AEM Forms, Authentication Facade Service, PDF Utility Service | HIPAA-ready |
| AEM CIF | Commerce Integration Framework | Not HIPAA-ready |
| AEM Cloud Manager | AEM Cloud Manager, Release Orchestrator, Release Toggles, Release Validator | HIPAA-ready |
| AEM Cloud Manager | Software Distribution | Not HIPAA-ready<br>Can be added to an Extended Security Program when no PHI is introduced. |
| | | |
| AEM Guides | AEM Guides | Not HIPAA-ready |
| | | |
| LLM Optimizer | LLM Optimizer | Not HIPAA-ready<br>Can be added to an Extended Security Program when no PHI is introduced. |

>[!NOTE]
>
>For not HIPAA-ready services that are indicated as can be added to an Extended Security program, customers must ensure that PHI is not routed to or stored in these services.
>
>Introducing PHI into a service that is not HIPAA-ready may result in non-compliance.

### Additional Requirements {#additional-requirements}

[Services listed](#hipaa-readiness-of-services-in-aem-as-a-cloud-service) as HIPAA-ready require the purchase of Extended Security for Healthcare. 

When Extended Security for Healthcare is purchased, there is the requirement that:

* the products selected for that program are HIPAA-ready (as listed in the table), 
* Extended Security for Healthcare has been purchased for *each* product; this ensures sufficient Cloud Manager Credits,
* Extended Security for Healthcare is applied at the time of program creation.

If the requirements are fulfilled, Extended Security for Healthcare can be applied upon AEM program creation; see [Setup](#setup) for details. 

>[!NOTE]
>
>For more details on provisioning, and pricing, reach out to your sales representative.

## Environments {#environments}

*HIPAA-ready* does not apply to RDE (Rapid Development Environment), Dev, or Stage environments, as PHI is not allowed on these environments. 

This means that you must:

* use dummy data for development and testing purposes
* only process PHI from production environments

The following table shows where the environment types can be supported as HIPAA-ready.

| | RDE | Dev | Stage | Prod |
| --- | --- | --- | --- | --- |
| Environment Type | No | No | No | Yes |

## Setup {#setup}

When you [Create Production Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md), the [Security tab provides the options to activate HIPAA protection](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md#security).