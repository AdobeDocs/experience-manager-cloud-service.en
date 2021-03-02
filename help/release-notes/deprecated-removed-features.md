---
title: Deprecated and removed features
description: Release notes specific to deprecated and removed features in Adobe Experience Manager as a Cloud Service.
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

| Capabilities | Deprecated feature | Replacement |
| ------------ | ------------------ | ----------- |
| Assets       | `DAM Asset Update` workflow to process ingested images. | Asset ingestion uses [asset microservices](/help/assets/asset-microservices-overview.md) now. |
| Assets       | Upload assets directly to AEM. See [deprecated asset upload APIs](/help/assets/developer-reference-material-apis.md#deprecated-asset-upload-api). | Use [Direct binary upload](/help/assets/add-assets.md). For technical details, see [direct upload APIs](/help/assets/developer-reference-material-apis.md#upload-binary). |
| Assets       | [Certain workflow steps](/help/assets/developer-reference-material-apis.md#post-processing-workflows-steps) in `DAM Asset Update` workflow are not supported, including calling command-line tools like ImageMagick. | [Asset microservices](/help/assets/asset-microservices-overview.md) provide a replacement for many workflows. For custom processing, use [post-processing workflows](/help/assets/asset-microservices-configure-and-use.md#post-processing-workflows). |
| Assets       | FFmpeg transcoding of videos. | For FFmpeg thumbnail generation, use [Asset microservices](/help/assets/asset-microservices-overview.md). For FFmpeg transcoding, use [Dynamic Media](/help/assets/manage-video-assets.md). |

## Removed features {#removed-features}

This section lists features and capabilities that have been removed from AEM with Experience Manager as a Cloud Service.

| Area         | Feature            | Replacement |
| ------------ | ------------------ | ----------- |
| UI        | While some Classic UI dialogs remain for the time being for a few select capabilities, such as Link Checker, Version Purge and some Cloud Service configurations, access to Classic UI in general has been removed in the AEM product UI. | Standard UI  |
| Dynamic Media | Previous integrations with [Dynamic Media Classic](https://experienceleague.adobe.com/docs/experience-manager-65/administering/integration/scene7.html#integration) and [Dynamic Media Hybrid mode](https://experienceleague.adobe.com/docs/experience-manager-65/assets/dynamic/config-dynamic.html#dynamic) are not available in AEM as a Cloud Service. | Use [Dynamic Media](/help/assets/dynamic-media/dynamic-media.md) provided with Experience Manager as a Cloud Service. |
| Sites | Portal Director and Portlet Component | These capabilities were deprecated in AEM 6.4 and have now been removed from AEM.|
| Sites | Design Importer | This capability has been removed as immutable sections of the AEM repository are not accessible at runtime. |
| Assets | [AEM Assets sharing with Marketing Cloud Assets Core Service and Creative Cloud services](https://docs.adobe.com/content/help/en/experience-manager-65/administering/integration/configure-assets-cc-integration.html) is not available. | For integration with Creative Cloud, use [Adobe Asset Link](https://helpx.adobe.com/enterprise/using/adobe-asset-link.html). |
