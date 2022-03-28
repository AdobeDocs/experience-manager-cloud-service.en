---
title: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2021.6.0
description: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2021.5.0
feature: Release Information
exl-id: 9a0a53d3-31d4-493d-ba2e-b4bb22f60351
---
# Release Notes for Cloud Manager in Adobe Experience Manager as a Cloud Service 2021.6.0 {#release-notes}

This page outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.6.0.

>[!NOTE]
>To see the current Release Notes for Adobe Experience Manager as a Cloud Service, click [here](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/release-notes/release-notes/release-notes-current.html).

## Release Date {#release-date}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.6.0 is June 10, 2021.

### What's New {#what-is-new}

* Preview Service will be deployed on a rolling basis to all Programs. Customers will be notified in-product when their Program is enabled for Preview Service. Refer to [Accessing Preview Service](/help/implementing/cloud-manager/manage-environments.md#access-preview-service) for more details.

* Maven Dependencies downloaded during the build step will now be cached between pipeline executions. This feature will be enabled for customers over the next several weeks.

* The name of the program can now be edited through the edit program dialog.

* The default branch name used during both project creation and  in the default push command via manage git workflows has been changed to `main`.

* Edit program experience in the UI has been refreshed.

* The quality rule `ImmutableMutableMixCheck` has been updated to classify `/oak:index` nodes as being immutable. 

* The quality rules `CQBP-84` and `CQBP-84--dependencies` have been consolidated into a single rule. As part of this consolidation, the scanning of dependencies more accurately identifies issues in third party dependencies which are being deployed to the AEM runtime.

* To avoid confusion, the Publish AEM and Publish Dispatcher segment rows on the Environment Details page have been consolidated.

   ![](/help/implementing/cloud-manager/release-notes-cloud-manager/assets/aem-dispatcher.png)

* A new code quality rule has been added to validate the structure of `damAssetLucene` indexes. Refer to [Custom DAM Asset Lucene Oak Indexes](/help/implementing/cloud-manager/custom-code-quality-rules.md#oakpal-damAssetLucene-sanity-check) for more details.

* Environment details page will now display multiple domain names for Publish and Preview services (as applicable). Refer to [Environment Details](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/manage-environments.html?lang=en#viewing-environment) to more details.

### Bug Fixes {#bug-fixes}

* JCR node definitions containing a newline after the root element name were not correctly parsed.

* List repositories API would not filter deleted repositories.

* An incorrect error message was displayed when an invalid value was provided for the schedule step.

* On occasion, user may see a green *active* status next to an IP Allow List even when that configuration was not deployed.

* Some program editing sequences could result in the inability to create or edit the production pipeline.

* Some program editing sequences could result in the **Overview** page displaying a misleading message to re-execute program setup.
