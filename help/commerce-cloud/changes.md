---
title: Notable changes to Commerce on AEM as a Cloud Service
description: Notable changes to Commerce on AEM as a Cloud Service as compared to Adobe Experience Manager 6.5.
---

# Notable changes to Commerce on AEM as a Cloud Service {#notable-changes}

Adobe Experience Manager as a Cloud Service brings many new features and possibilities to manage your AEM projects. This document highlights the important differences for Commerce capabilities between Commerce Integration Framework (CIF) for on-premise, Adobe Managed Service and Experience Manager as a Cloud Service. For other changes, see the generic [changes to Experience Manager as a Cloud Service](/help/release-notes/aem-cloud-changes.md).

The main differences as compared to Experience Manager 6.5 are in the following areas:
* [Support for CIF Classic](#cif-classic)
* [Deployment of CIF Authoring Tools](#cif-tools)
* [Moving from on-premise and Adobe Managed Service](#moving-cif-cs)

## Support for CIF Classic/Quickstart on Experience Manager as a Cloud Service {#cif-classic}

The Classic Commerce Integration Framework which included a Product Importer to import and store product catalogs in Experience Manager is no longer available in Experience Manager as a Cloud Service. The use of Classic CIF is not supported in Experience Manager as a Cloud Service and projects using Classic CIF will have to replace the Classic CIF implementation with the supported version as described in [CIF on Experience Manager as a Cloud Service](https://git.corp.adobe.com/AdobeDocs/experience-manager-cloud-service.en/blob/cif/help/commerce-cloud/architecture.md)


## Deployment of CIF {#cif-tools}

Shown below are the different deployment models for Commerce Integration Framework for the different AEM offerings:

|                  | AEM On-premise  |  AEM Managed Services         |  AEM Cloud Service         |
|-------------     |-----------|-----------|-----------|
|How to deploy CIF Authoring tools for Magento backend| [Refer to CIF Connector](https://github.com/adobe/commerce-cif-connector/blob/master/README.md) supported on AEM 6.5| [Refer to CIF Connector](https://github.com/adobe/commerce-cif-connector/blob/master/README.md) supported on AEM 6.5| AEM Cloud Service instance will need to be provisioned with CIF add-on. Contact your sales representative for more details|
|How to deploy [CIF Venia Project](https://github.com/adobe/aem-cif-guides-venia)|AEM package install|[Cloud Manager](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/deploying/overview.html) | 

Note: CIF Classic/Quickstart version of Commerce Integration Framework may be used on AEM On-premise offering for very limited use-cases. However, this is not the recommended solution.


## Moving to CIF on Experience Manager as a Cloud Service from on-premise and Managed Services {#moving-cif-cs}

