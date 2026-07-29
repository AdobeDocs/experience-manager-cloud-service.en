---
title: Detect duplicate assets for [!DNL Adobe Experience Manager] as a [!DNL Cloud Service]
description: Learn how to detect duplicate assets
contentOwner: KK
mini-toc-levels: 3
feature: Asset Management, Publishing,Collaboration, Asset Processing
role: User, Developer, Admin
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 40f63933-4f4e-4318-8d42-4b5c9b01f7cd
---

# Detect duplicate assets {#detect-duplicate-assets}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/assets/managing/duplicate-detection.html?lang=en)                  |
| AEM as a Cloud Service     | This article         |

If a DAM user uploads one or more assets that already exist in the repository, [!DNL Experience Manager] detects the duplication and notifies the user. Duplicate detection is disabled by default as it can have a performance impact depending on the size of the repository and the number of assets uploaded.

To enable the feature:

1. Navigate to **[!UICONTROL Tools > Assets > Assets Configurations]**.

1. Click **[!UICONTROL Asset Duplication Detector]**.

1. On the [!UICONTROL Asset Duplication Detector page], click **[!UICONTROL Enabled]**.

   `dam:sha1` value for the Detect Metadata field ensures that duplicate assets are detected even if the filenames are different.

1. Click **[!UICONTROL Save]**.

   ![Asset Duplication Detector](assets/asset-duplication-detector.png)

>[!NOTE]
>
>If you have configured Duplication Detector using `/apps/example/config.author/com.adobe.cq.assetcompute.impl.assetprocessor.AssetDuplicationDetector.cfg.json` configuration file (OSGi configuration), you can continue to use it. However, Adobe recommends using the new method.
 

Once enabled, Experience Manager sends notifications of duplicate assets to the Experience Manager Inbox. It is an aggregated result for multiple duplicates. Users can choose to remove the assets based on the results.

![Inbox notification for duplicate assets](assets/duplicate-detect-inbox-notification.png)

>[!NOTE]
>
>When you upload assets to the repository, Experience Manager detects duplication and notifies you about the first 100 duplicate assets.


**See also**

* [Translate Assets](/help/assets/translate-assets.md)
* [Assets HTTP API](/help/assets/mac-api-assets.md)
* [Assets supported file formats](/help/assets/file-format-support.md)
* [Search assets](/help/assets/search-assets.md)
* [Connected assets](/help/assets/use-assets-across-connected-assets-instances.md)
* [Asset reports](/help/assets/asset-reports.md)
* [Metadata schemas](/help/assets/metadata-schemas.md)
* [Download assets](/help/assets/download-assets-from-aem.md)
* [Manage metadata](/help/assets/manage-metadata.md)
* [Manage Dynamic Media templates](/help/assets/dynamic-media/manage-dynamic-media-templates.md)
* [Manage reports in Assets view](/help/assets/manage-reports-assets-view.md)
* [Search facets](/help/assets/search-facets.md)
* [Manage collections](/help/assets/manage-collections.md)
* [Bulk metadata import](/help/assets/metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)

