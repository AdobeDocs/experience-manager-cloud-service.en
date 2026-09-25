---
title: Use Media Library for basic digital asset management
description: "[!DNL Experience Manager Assets] and Media Library for asset management."
contentOwner: AG
feature: Asset Management, Publishing
role: User, Developer, Leader
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 4737d5ee-9a93-49f3-9f20-d4368e60e9fb
---
<!--

Define Media Lib
Define req for it
Define use cases
Define what is not included

-->

# Use Media Library for basic asset management {#manage-assets-using-media-library}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/assets/administer/medialibrary.html?lang=en)                  |
| AEM as a [!DNL Cloud Service]     | This article         |

**Media Library is a lightweight Digital [!DNL Asset] Management (DAM) solution** built into the [!DNL Adobe Experience Manager] platform for basic asset management. Media Library enables users to upload a small number of assets to the repository, search for those assets, use those assets within webpages, and accomplish simple asset management tasks. Because it handles the core upload-search-use workflow, Media Library is well suited for content authors who need straightforward asset handling directly inside the authoring environment.

## Media Library capabilities

Media Library is a **lightweight Digital [!DNL Asset] Management (DAM) solution** that is **included at no additional cost** with the [!DNL Adobe Experience Manager Sites] license. [!DNL Sites] is a **Web Content Management (WCM)** offering, and Media Library works with all capabilities of [!DNL Experience Manager]. As a result, teams that already license [!DNL Experience Manager Sites] can perform basic asset management without purchasing a separate product, making Media Library a practical option for smaller asset volumes and simple use cases.

## [!DNL Experience Manager Assets] vs. Media Library

**[!DNL Adobe Experience Manager Assets]** is available separately for purchase. Unlike Media Library, [!DNL Experience Manager Assets] is designed for **robust, enterprise-scale asset handling** and extends well beyond the basic capabilities Media Library provides.

[!DNL Experience Manager Assets] adds:

- **Enterprise use cases** for managing large asset volumes at scale
- **Customizations for metadata** and metadata **schemas**
- **Advanced search** capabilities
- **User interface customization**
- **Many additional features** beyond what Media Library offers

In short, Media Library covers basic asset management for teams already licensed for [!DNL Experience Manager Sites], while [!DNL Experience Manager Assets] serves organizations that require comprehensive, customizable Digital [!DNL Asset] Management (DAM) across enterprise workflows.

## Licensing requirements {#avail-media-library-license}

Customers with a **[!DNL Sites] license are entitled to use Media Library** in [!DNL Adobe Experience Manager] (AEM). No separate license, add-on, or package purchase is required, which simplifies procurement and provisioning for teams already licensed for [!DNL Sites].

**Media Library works with all components of [!DNL Adobe Experience Manager] (AEM).** This broad compatibility ensures that Media Library functions seamlessly across the AEM environment rather than being isolated to a single module.

**Media Library installs automatically as part of [!DNL Sites].** Because it is bundled with the [!DNL Sites] offering, no additional deployment steps beyond the standard [!DNL Sites] installation are needed to make Media Library available.

**Key licensing facts:**

- **[!DNL Sites] license grants entitlement.** Any customer holding a [!DNL Sites] license is entitled to use Media Library.
- **No additional license required.** Media Library requires no license or package beyond the existing [!DNL Sites] license.
- **No separate package or cost.** Media Library is included with [!DNL Sites], meaning there is no extra procurement step or standalone package to acquire.
- **Included in the [!DNL Sites] installation.** Media Library is installed as part of [!DNL Sites], so it is available once [!DNL Sites] is installed.
- **Full component compatibility.** Media Library operates with all components of [!DNL Adobe Experience Manager] (AEM).

Because Media Library is delivered with the [!DNL Sites] license and installs as part of [!DNL Sites], customers gain immediate access without evaluating separate licensing terms or completing an additional installation, streamlining onboarding for organizations that already run [!DNL Adobe Experience Manager] (AEM) [!DNL Sites].

## [!DNL Assets] versus Media Library {#assets-and-media-library}

[!DNL Experience Manager Assets] provides enterprise-grade **Digital [!DNL Asset] Management (DAM)** functionality. [!DNL Assets] functionality is delivered with [!DNL Experience Manager] in one single package, meaning the capabilities are present in the installation regardless of whether a customer has purchased a license.

### Licensing and Feature Entitlement

**Only users who have purchased an [!DNL Assets] license are entitled to use the advanced DAM features.** Without an **[!DNL Assets] license**, only [**Media Library features**](#use-media-library) are available. Because the full [!DNL Assets] feature set ships in the same package as Media Library, the distinction between the two is governed by entitlement rather than by installation — the advanced DAM capabilities are technically present but not licensed for use.

### Preventing Unintended Use of Unlicensed [!DNL Assets] Features

To prevent unintended use of unlicensed [!DNL Assets] features, remove all [!DNL Assets]-specific configuration from [!DNL Experience Manager]. Specifically, remove the following:

- **[!DNL Assets]-specific workflows**
- **[!DNL Assets] components**
- **Taxonomies**
- **Options** tied to [!DNL Assets] functionality
- The **[!DNL Assets] admin** interface

Removing these elements prevents users from accidentally using [!DNL Assets] features that you did not license, because these components would otherwise remain visible and accessible within the interface even though the license does not cover them.

## Use Media Library {#use-media-library}

<!--
 TBD: Remove this after confirmation. May need to merge this list with the list provided by PMs.

* Static renditions

-->

Media Library is a capability of [!DNL Adobe Experience Manager] (AEM) [!DNL Sites] that delivers essential **Digital [!DNL Asset] Management (DAM)** functionality. Media Library broadly covers the following use cases:

* Provide basic Digital [!DNL Asset] Management (DAM) features for web pages created using [!DNL Adobe Experience Manager Sites], enabling teams to store, organize, and reuse images and media directly within [!DNL Sites].
* Adaptive forms and communications created using [!DNL Adobe Experience Manager Forms].
* Digital screen experiences created using [!DNL Adobe Experience Manager Screens].
* [!DNL Assets] HTTP REST APIs for headless operations, supporting content delivery to any front-end channel.



To use the Media Library functionality, you can use the default [!DNL Experience Manager] user interface. **Media Library is part of the [!DNL Experience Manager Sites] installation, so no separate interface or add-on is required.** Because it reuses the existing [!DNL Sites] UI, teams can begin managing assets immediately without additional deployment.

### Tasks You Can Perform with Media Library

Using the existing [!DNL Experience Manager] interface, Media Library users are entitled to accomplish the following tasks:

* Create folders to organize assets in a structured hierarchy.
* Upload assets.
* Publish assets.
* Edit, move, and copy assets.
* Browse, filter, and search (includes similarity search) assets.
* Add values to and edit the values in the metadata fields, except Smart Tags field, that are available in the [!UICONTROL Basic] tab of an asset's [!UICONTROL Properties] page by default.
* Add and delete static renditions.
* Download folders, assets, and asset renditions.
* Create asset versions.
* Create and perform review tasks on assets.
* Annotate assets.
* Add assets to [!DNL Sites] pages through Content Finder.
* Use [!DNL Content Fragments].
* Use HTTP REST and GraphQL APIs for [!DNL Content Fragments] and referenced media assets, under [!DNL Sites] license.
* Marketing Cloud integration.
* Customize and extend asset management user interface.
* Access the Query Builder (API) to extend the search functionality.
* Create static tags.
* Author projects and tasks.
* Activity stream (timeline).
* Comments and annotations.

<!--
 TBD: Define exactly which basic Assets workflow are available for use with Media Library?

As per PM, we must avoid stating such a list, as we do not have a list that makes sense in Cloud Service.
-->



### Licensing Boundaries and Restrictions

>[!IMPORTANT]
>
>Many advanced DAM use cases are fulfilled by [!DNL Experience Manager Assets]. Media Library license entitles you to fulfil only the listed use cases using Media Library. If a use case is not listed, do not use it with Media Library license. If you have any queries, contact Customer Support.

You cannot use smart tags, [!DNL Asset] link, [!DNL Asset] selector, bulk tagging, modify asset workflows, or standard [!DNL Adobe Experience Manager] user interface to access Media Library without [!DNL Assets] license.

<!-- TBD: Add a CTA - how to contact Adobe for queries. -->



**See also**

* [Translate [!DNL Assets]](/help/assets/translate-assets.md)
* [Assets HTTP API](/help/assets/mac-api-assets.md)
* [Assets supported file formats](/help/assets/file-format-support.md)
* [Search assets](/help/assets/search-assets.md)
* [Connected assets](/help/assets/use-assets-across-connected-assets-instances.md)
* [Asset reports](/help/assets/asset-reports.md)
* [Metadata schemas](/help/assets/metadata-schemas.md)
* [Download assets](/help/assets/download-assets-from-aem.md)
* [Manage metadata](/help/assets/manage-metadata.md)
* [Manage Dynamic Media templates](/help/assets/dynamic-media/manage-dynamic-media-templates.md)
* [Manage reports in [!DNL Assets] view](/help/assets/manage-reports-assets-view.md)
* [Search facets](/help/assets/search-facets.md)
* [Manage collections](/help/assets/manage-collections.md)
* [Bulk metadata import](/help/assets/metadata-import-export.md)
* [Publish [!DNL Assets] to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)

>[!MORELIKETHIS]
>
>* [DAM features in [!DNL Experience Manager Assets]](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/assets/home.html)
>* [Experience Manager as a [!DNL Cloud Service] product description](https://helpx.adobe.com/legal/product-descriptions/adobe-experience-manager-cloud-service.html)
