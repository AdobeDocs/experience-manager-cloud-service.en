---
title: Deprecated and Removed Features
seo-title: Deprecated and Removed Features
description: Release notes specific to deprecated and removed features in Adobe Experience Manager as a Cloud Service
seo-description: Release notes specific to deprecated and removed features in Adobe Experience Manager as a Cloud Service
topic-tags: release-notes

---

# Deprecated and Removed Features {#deprecated-and-removed-features}

Adobe constantly evaluates product capabilities, to over time reinvent or replace older features with more modern alternatives to improve overall customer value, always under careful consideration of backward compatibility. Additionaly, as Adobe Experience Manager as a Cloud Service provides a cloud-native deployment model, certain capabilities and features were replaced by cloud-native counterparts.

To communicate the impending removal/replacement of AEM capabilities, the following rules apply:

1. Announcement of deprecation comes first. While deprecated, capabiiities are still available, but they will not be further enhanced.
1. Removal of deprecated capabilities will occur in the following major release at the earliest. Actual target date for removal will be announced.

This process gives customers at least one release cycle to adapt their implementation to a new version or successor of a deprecated capability, before actual removal.

## Deprecated Features {#deprecated-features}

This section lists features and capabilities that have been marked as deprecated in Experience Manager as a Cloud Service. Generally, features that are planned to be removed in a future release are set to deprecated first, with an alternative provided.

Customers are advised to review if they make use of the feature/capability in their current deployment, and make plans to change their implementation to use the alternative provided.

| Area         | Feature            | Replacement |
| ------------ | ------------------ | ----------- |
| Assets       | Asset ingestion and processing no longer uses DAM Asset Update Workflow | Asset ingestion uses [Asset microservices](/help/assets/asset-microservices-overview.md) now |
| Assets       | Uploading assets directly to AEM - see [deprecated asset upload APIs](help/assets/developer-reference-material-apis.md#deprecated-asset-upload-api) | [Direct binary uplaod](help/assets/add-assets.md) is used in Experience Manager as a Cloud Service. See technical details of the [direct upload APIs](help/assets/developer-reference-material-apis.md#details-binary-upload) |
| Assets       | [Certain workflow steps](help/assets/developer-reference-material-apis.md#post-processing-workflows-steps) in DAM Asset Update Workflow are not supported, including calling commandline tools like ImageMagick | [Asset microservices](/help/assets/asset-microservices-overview.md) provide a replacement for a number of tehm. Custom processing can be done using [post-processing workflows](help/assets/asset-microservices-configure-and-use.md#post-processing-workflows) |


## Removed Features {#removed-features}

This section lists features and capabilities that have been removed from AEM with Experience Manager as a Cloud Service. 

| Area         | Feature            | Replacement |
| ------------ | ------------------ | ----------- |
| Dynamic Media | Older integartions with Dynamic Media Classic (Scene7)](https://helpx.adobe.com/experience-manager/6-5/sites/administering/using/scene7.html) and [Dynamic Media Hybrid Mode](https://helpx.adobe.com/experience-manager/6-5/assets/using/config-dynamic.html) are not available in AEM as a Cloud Service | Use [Dynamic Media](help/assets/dynamic-media/dynamic-media-assets.md) provided with Experience Manager as a Cloud Service |
| Assets | [AEM Assets sharing with Marketing Cloud Assets Core Service and Creative Cloud services](https://docs.adobe.com/content/help/en/experience-manager-65/administering/integration/configure-assets-cc-integration.html) is be available | For integration with Creative Cloud, [Adobe Asset Link](https://helpx.adobe.com/enterprise/using/adobe-asset-link.html) is recommended |


