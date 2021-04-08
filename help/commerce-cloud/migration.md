---
title: Migration to the AEM Commerce Integration Framework (CIF) add-on
description: How to migrate to the AEM Commerce Integration Framework (CIF) add-on from an old version
exl-id: c136763f-56aa-450e-8796-bc84bf6c205d
---
# Migration to the AEM Commerce Integration Framework (CIF) add-on {#cif-migration}

Customers moving from an AEM on-premise or Managed Services installation to AEM as a Cloud Service need to do a few minor adjustments on the AEM project.

The first adjustment, as described above, is needed for the CIF Connector. The CIF Connector is replaced by the CIF add-on which is deployed by Adobe. Therefore do not install the CIF Connector on AEM as a Cloud Service. Also, the use with the local AEM Cloud SDK is not supported, Adobe provides the CIF add-on also for [local development](develop.md).

Second, understand the [AEM Project Structure](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/developing/aem-project-content-package-structure.html) and the characteristics of AEM as a Cloud Service. Adapt your project setup to the AEM as a Cloud Service layout.
The main differences here are:

* The GraphQL client OSGI bundle **must not** be included into the AEM project anymore, it is deployed via the CIF add-on
* OSGI configs for GraphQL client and Graphql Data Service **must not** be included into the AEM project anymore

>[!TIP]
>
>Check out the [AEM Venia Reference Store](https://github.com/adobe/aem-cif-guides-venia) project on GitHub. This project provides Maven profiles for AEM as a Cloud Service and on-premise deployments which take into account the different framework conditions.
