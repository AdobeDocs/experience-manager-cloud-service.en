---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: a2d56721-502c-4f4e-9b72-5ca790df75c5
---

# Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the general Release Notes for the current (latest) version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>From here, you can navigate to release notes of previous versions; for example, for those in 2020, 2021 and so on.

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2021.6.0 is June 24, 2021.
The following release (2021.7.0) will be on July 29, 2021.

## XML Documentation for AEM as a cloud Service {#xml-documentation}
 
### Release Date {#release-date-xml-documentation}
 
The Release Date for XML Documentation for AEM as a Cloud Service is June 24, 2021.
 
### What's New {#what-is-new-xml-documentation}
 
* XML Documentation for AEM as a Cloud Service is now GA.
* This will allow existing AEM Cloud Service customers to procure XML Documentation addon for importing, creating, managing and delivering technical content across multiple channels including AEM sites

## Release Video {#release-video}

Have a look at the [June 2021 Release Overview](https://video.tv.adobe.com/v/333602) video for a summary of the features added.

## Cloud Manager {#cloud-manager}

This section outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.6.0 and 2021.5.0.

## Release Date {#release-date-june-cm}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.6.0 is June 10, 2021.
The next release is planned for July 15, 2021.

### What's New {#what-is-new-junecm}

* Preview Service will be deployed on a rolling basis to all Programs. Customers will be notified in-product when their Program is enabled for Preview Service. Refer to [Accessing Preview Service](/help/implementing/cloud-manager/manage-environments.md#access-preview-service) for more details.

* Maven Dependencies downloaded during the build step will now be cached between pipeline executions. This feature will be enabled for customers over the next several weeks.

* The name of the program can now be edited through the edit program dialog.

* The default branch name used during both project creation and  in the default push command via manage git workflows has been changed to `main`.

* Edit program experience in the UI has been refreshed.

* The quality rule `ImmutableMutableMixCheck` has been updated to classify `/oak:index` nodes as being immutable. 

* The quality rules `CQBP-84` and `CQBP-84--dependencies` have been consolidated into a single rule. As part of this consolidation, the scanning of dependencies more accurately identifies issues in third party dependencies which are being deployed to the AEM runtime.

* To avoid confusion, the Publish AEM and Publish Dispatcher segment rows on the Environment Details page have been consolidated.

   ![](/help/onboarding/release-notes-cloud-manager/assets/aem-dispatcher.png)

* A new code quality rule has been added to validate the structure of `damAssetLucene` indexes. Refer to [Custom DAM Asset Lucene Oak Indexes](/help/implementing/cloud-manager/custom-code-quality-rules.md#oakpal-damAssetLucene-sanity-check) for more details.

* Environment details page will now display multiple domain names for Publish and Preview services (as applicable). Refer to [Environment Details](/help/implementing/cloud-manager/manage-environments.md#viewing-environment) to more details.

### Bug Fixes {#bug-fixes-junecm}

* JCR node definitions containing a newline after the root element name were not correctly parsed.

* List repositories API would not filter deleted repositories.

* An incorrect error message was displayed when an invalid value was provided for the schedule step.

* On occasion, user may see a green *active* status next to an IP Allow List even when that configuration was not deployed.

* Some program editing sequences could result in the inability to create or edit the production pipeline.

* Some program editing sequences could result in the **Overview** page displaying a misleading message to re-execute program setup.
