---
title: Deprecated and removed features
description: Release notes specific to deprecated and removed features in Adobe Experience Manager as a Cloud Service.
topic-tags: release-notes

---

# Deprecated and removed features {#deprecated-and-removed-features}

Adobe constantly evaluates product capabilities, to over time reinvent or replace older features with more modern alternatives to improve overall customer value, always under careful consideration of backward compatibility. Additionally, as Adobe Experience Manager as a Cloud Service provides a cloud-native deployment model, certain capabilities and features were replaced by cloud-native counterparts.

To communicate the impending removal/replacement of AEM capabilities, the following rules apply:

1. Announcement of deprecation comes first. Deprecated capabilities continue to remain available but are not enhanced further.
1. Capabilities announced to be deprecated are removed in the subsequent major release, at the earliest. The actual target date for removal is announced.

This process gives customers at least one release cycle to adapt their implementation to a new version or successor of a deprecated capability, before actual removal.

## Deprecated features {#deprecated-features}

This section lists features and capabilities that have been marked as deprecated in Experience Manager as a Cloud Service. Typically, features that are planned to be removed in a future release are set to deprecated first, with an alternative provided.

Customers are advised to review if they make use of the feature/capability in their current deployment, and make plans to change their implementation to use the alternative provided.

| Area         | Feature            | Replacement |
| ------------ | ------------------ | ----------- |
| Assets       | Asset ingestion and processing no longer uses `DAM Asset Update` workflow | Asset ingestion uses [asset microservices](/help/assets/asset-microservices-overview.md) now. |
| Assets       | Upload assets directly to AEM - see [deprecated asset upload APIs](/help/assets/developer-reference-material-apis.md#deprecated-asset-upload-api) | [Direct binary upload](/help/assets/add-assets.md) is used in Experience Manager as a Cloud Service. For technical details, see [direct upload APIs](/help/assets/developer-reference-material-apis.md#overview-binary-upload). |
| Assets       | [Certain workflow steps](/help/assets/developer-reference-material-apis.md#post-processing-workflows-steps) in DAM Asset Update Workflow are not supported, including calling command-line tools like ImageMagick | [Asset microservices](/help/assets/asset-microservices-overview.md) provide a replacement for many workflows. For custom processing, use [post-processing workflows](/help/assets/asset-microservices-configure-and-use.md#post-processing-workflows). |

## Removed features {#removed-features}

This section lists features and capabilities that have been removed from AEM with Experience Manager as a Cloud Service. 

| Area         | Feature            | Replacement |
| ------------ | ------------------ | ----------- |
| Dynamic Media | Previous integrations with [Dynamic Media Classic (Scene7)](https://helpx.adobe.com/experience-manager/6-5/sites/administering/using/scene7.html) and [Dynamic Media Hybrid mode](https://helpx.adobe.com/experience-manager/6-5/assets/using/config-dynamic.html) are not available in AEM as a Cloud Service. | Use [Dynamic Media](/help/assets/dynamic-media/dynamic-media-assets.md) provided with Experience Manager as a Cloud Service. |
| Assets | [AEM Assets sharing with Marketing Cloud Assets Core Service and Creative Cloud services](https://docs.adobe.com/content/help/en/experience-manager-65/administering/integration/configure-assets-cc-integration.html) is not available. | For integration with Creative Cloud, use [Adobe Asset Link](https://helpx.adobe.com/enterprise/using/adobe-asset-link.html). |
