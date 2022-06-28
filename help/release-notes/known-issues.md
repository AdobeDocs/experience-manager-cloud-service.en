---
title: Known issues
description: Known issues with Adobe Experience Manager as a Cloud Service
exl-id: 897b944a-d320-4d21-91f4-2cd3da6179b1
---
# Known issues {#known-issues}

This article lists the known issues of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] offering. The list is revised and updated with each continuous release of [!DNL Experience Manager].

[Contact support](https://experienceleague.adobe.com/?lang=en&support-solution=Experience+Manager#support) for more information about the known issues.

<!-- 
## Platform {#platform}
-->

## Sites {#sites}

Some known issues in [!DNL Sites] are:

* In the GraphQL IDE you can [manage the cache for your persisted queries](help/headless/graphql-api/graphiql-ide.md##managing-cache). 
  * On the first save the values saved for the headers are set to `0` - if the user has not changed those values in the dialog. 
  * On subsequent saves, the values set by the user are saved correctly. 
  * Therefore, the user has to save the headers two times. 

## [!DNL Assets] {#assets}

<!-- Jira label: assets-cloud-known-issues -->

Some known issues in [!DNL Assets] are:

* **Download**: If you download an empty folder, [!DNL Experience Manager] conveys a success message about creating a ZIP archive, but the archive is not created.

* **Metadata Schema**: Asset rating widget used to cause JSP compilation error. It was removed from the metadata schema. <!-- CQ-4282865, CQ-4284633 -->

Also, see [notable changes to [!DNL Experience Manager Assets]](/help/assets/assets-cloud-changes.md).

<!-- This content was added at GA. Not sure if we should continue to have this commitment about upcoming features/enh. in the docs. Commenting it for now.

### Upcoming Assets capabilities {#upcoming-assets-capabilities}

A few capabilities of Adobe Experience Manager Assets that depend on foundation capabilities, which are not yet available in the Experience Manager as a Cloud Service deployment architecture, are expected to be enabled at a later stage:

* Capabilities not enabled at this stage due to dependency on Commerce Integration Framework APIs:
  * Photoshoot workflow models.
  * Product information tab in the asset properties user interface is not populated.

* Capabilities not enabled at this stage due to dependency on InDesign Server integration:
  * Asset Templates and Asset Catalogs.
  * Multi-page preview of Adobe InDesign files.
-->

>[!MORELIKETHIS]
>
>* [Major changes in [!DNL Experience Manager]](aem-cloud-changes.md)
>* [Deprecated and removed features](deprecated-removed-features.md)
>* [Release notes](home.md)
