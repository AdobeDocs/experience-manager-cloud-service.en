---
title: What's new in Content Hub
description: Learn more on some of the recenly launched Content Hub capabilities
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 77a5c54c-bbc5-4dfb-9c3a-aa0620e836d0
---
# What's new in Content Hub {#whats-new-content-hub}

Content Hub is available as part of Experience Manager Assets as a Cloud Service for democratizing access to on-brand content for organizations and their business partners. It focuses on distributing assets for activation at scale and creation of on-brand content variants for improved marketing agility.

The following video demonstrates Content Hub key capabilities:

>[!VIDEO](https://video.tv.adobe.com/v/3463712)

>[!IMPORTANT]
>
>[Assets Ultimate](/help/assets/assets-ultimate-overview.md) and Assets as a Cloud Service include 250 Content Hub Limited users. [Assets Prime](/help/assets/assets-prime.md) includes 50 Content Hub Limited users.

## Release Date {#release-date}

The release date of Content Hub feature release (2026.05.0) is May 28, 2026 (same as that of AEM as a Cloud Service release). The next feature release (2026.06.0) is planned for June 25, 2026.

## May 2026 release features {#may-2026-release-features}

**AI Search**

AEM Assets Content Hub now includes AI Search, an advanced search capability that understands the meaning and intent behind user queries instead of relying only on exact keyword matches. AI Search delivers more accurate and context relevant results by recognizing relationships between words, concepts, and user intent. It supports multilingual queries, handles misspellings and typos, understands synonyms, and surfaces relevant assets even when users do not use exact metadata terms. 

For example, a search for `Woman drinking coffee` can also return assets tagged with related terms such as `Lady`, `Girl`, `Latte`, or `Cappuccino`. 

Administrators can enable or disable AI Search in Content Hub using the Configurations menu by selecting either AI Search or traditional keyword search.

[!BADGE Dive Deeper into this Feature]{type=Informative url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/content-hub/search-assets-content-hub#ai-search-aem-assets-content-hub"}


**Custom Sorting options**

Content Hub now allows administrators to enable custom metadata fields as sorting options on the Content Hub home page. In addition to the default sorting options, Size, Modified, Name, and Relevance, administrators can configure business-specific metadata fields such as Channel, Region, SKU, or Campaign to help users organize search results more effectively.

[!BADGE Dive Deeper into this Feature]{type=Informative url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/content-hub/search-assets-content-hub#configure-sorting-aem-assets-content-hub"}

**Asset Search and Download Event Support for Delivery APIs**

AEM Assets Delivery APIs now support asset search and asset download events, enabling organizations to track and respond to how assets are discovered and consumed across connected applications and experiences. These events help improve visibility into asset usage patterns, support analytics and reporting workflows, and simplify integrations with external systems and automation processes. 

With event-driven insights, teams can better understand content engagement and build more connected digital asset workflows. For more details, see the [API documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/asset_downloaded).

**Asset Delivery URL**

Content Hub now allows users to copy an asset's delivery URL directly from the asset properties. This enhancement makes it easier to share and embed approved assets across websites, applications, and external systems. By providing quick access to delivery-ready links, teams can streamline content distribution workflows and accelerate asset reuse across digital experiences.

>[!IMPORTANT]
>
>These features are available as Limited Availability features. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.


## February 2026 release features {#february-2026-release-features}

**Permission management in Content Hub using AEM Governance Agent**

In Content Hub, the AEM Governance Agent ensures that only the right people access the right assets at the right time. By applying granular, attribute-based controls and usage rights, it protects sensitive content while enabling secure collaboration. This means reduced compliance risk, stronger brand integrity, and faster workflows, teams can confidently share and reuse assets without worrying about unauthorized access or misuse. This balance of security and flexibility translates into higher operational efficiency and trust across the organization.

![Permission Management Overview](/help/ai-in-aem/agents/governance/assets/permission-management.png)

[!BADGE Dive Deeper into this Feature]{type=Informative url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/ai-in-aem/agents/governance/overview#permission-and-digital-rights-management"}


## October 2025 release features {#october-2025-release-features}

**Enhancements In Content Hub download experience**

Content Hub now supports downloading multiple asset renditions in a flat hierarchy, eliminating the need to navigate through multiple folders. User preferences for download behavior are now retained for a consistent experience across sessions. The new asset download experience streamlines asset management and improves efficiency by making downloaded files easier to locate and organize.

[!BADGE Dive Deeper into this Feature]{type=Informative url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/content-hub/download-assets-content-hub#download-asset-renditions"}

## September 2025 release features {#september-2025-release-features}

**Mark Collections as Favourites**

You can now mark collections as Favorites in Content Hub, making it easier to organize and retrieve them. Once added, your favourite collections are conveniently available from the **[!UICONTROL Favourites]** tab on the Content Hub home page.

**Pin collections for quick access**

Content Hub Administrators can now pin collections in Content Hub for quick access. Pinned collections are displayed in a dedicated **[!UICONTROL Pined]** section on the Collections home page, making it easier to keep important collections within reach.

[!BADGE Dive Deeper into this Feature]{type=Informative url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/content-hub/collections-content-hub#pin-unpin-collection"}

## August 2025 release features {#august-release-features}

**Bulk Search via Filter Properties**

Content Hub now makes it faster to discover the assets you need. With the new Bulk Search capability, you can enter multiple values for any filter property—separated by a delimiter (for example, multiple SKU IDs)—and instantly retrieve all matching assets using a single search.

[!BADGE Dive Deeper into this Feature]{type=Informative url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/content-hub/search-assets-content-hub#bulk-search"}

## July 2025 release features {#july-2025-release-features}

**Enhanced branding flexibility in Content Hub**

Building on existing personalization features, Content Hub now allows admins to further tailor their deployment by adding custom logo images. Support for the TIFF file format has also been added for both banner and logo images, enabling greater design flexibility.

[!BADGE Dive Deeper into this Feature]{type=Informative url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/content-hub/configure-content-hub-ui-options#configure-branding-content-hub"}

**Smarter sharing with titled links**

You can now add a title when generating a shared link—whether from the asset details view or after selecting one or more assets. This helps recipients easily identify the purpose of each link, especially when receiving multiple shared assets.

![private and public link](/help/assets/assets/shared-link-for-assets.png)

[!BADGE Dive Deeper into this Feature]{type=Informative url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/content-hub/share-assets-content-hub"}

**Improved filter navigation**

Content Hub now includes a **Show All** option within filters, allowing users to view all available facets along with asset counts from the current limitation of viewing only upto ten facets. Enhanced search and sort capabilities within each filter make it easier to discover and manage assets more efficiently.

## June 2025 release features {#june-2025-release-features}

### Collections governance {#collections-governance}

Content Hub now lets you control access to collections during creation, ensuring only authorized users can view or manage grouped assets. It ensures improved security, better collaboration, organized asset management, and simplified governance.

>[!VIDEO](https://video.tv.adobe.com/v/3463336)

[!BADGE Dive Deeper into this Feature]{type=Informative url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/content-hub/collections-content-hub#create-collections"}

## May 2025 release features {#may-2025-release-features}

Content Hub May release includes the following features:

* [Attribute-based Access Control](#attribute-based-access-control)

* [UI Branding](#ui-branding)

* [Public link sharing](#public-link-sharing)

* [Download multiple assets as a ZIP](#download-multiple-assets-as-zip)

* [Dynamic Media renditions in Content Hub](#dynamic-media-renditions)

### Attribute-based Access Control (ABAC) {#attribute-based-access-control}

Content Hub now allows you to apply rule-based restrictions to access assets. Asset permissions ensure governance and also make sure that only the relevant assets are accessible to users.

The asset restriction rules are based on metadata and if the conditions defined in the rule match the asset metadata, the asset gets displayed to the user groups.

Some of the key benefits of Attribute-based Access Control include:

* Eliminates the dependency on folder structure for permissions

* Allows administrators to upload assets and retroactively determine permission structures

* Reduces number of duplicates - improves asset integrity. Duplicates are needed in folder based permissions when same assets are shared with different groups.

[!BADGE Dive Deeper into this Feature]{type=Informative url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/content-hub/attribute-based-access-control"}

### UI Branding {#ui-branding}

Content Hub now allows administrators to customize the user interface with brand-specific elements, including banner images, banner titles and body text, as well as primary and secondary colors. These enhancements help ensure brand consistency, simplify user onboarding, and build trust.

![UI Branding](/help/assets/assets/content-hub-ui-branding.png)

[!BADGE Dive Deeper into this Feature]{type=Informative url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/content-hub/configure-content-hub-ui-options#configure-branding-content-hub"}

### Public link sharing {#public-link-sharing}

Content Hub now supports generating shareable links to allow external users, without application access, to view asset metadata or download assets.

![UI Branding](/help/assets/assets/public-and-private-link.png)

[!BADGE Dive Deeper into this Feature]{type=Informative url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/content-hub/share-assets-content-hub"}

### Download multiple assets as a ZIP {#download-multiple-assets-as-zip}

Content Hub now also allows you to download the selected assets and their renditions in a ZIP file and not as separate files simplifying file management for you.

[!BADGE Dive Deeper into this Feature]{type=Informative url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/content-hub/download-assets-content-hub#download-asset-renditions"}

### Dynamic Media renditions in Content Hub {#dynamic-media-renditions}

Access all your Dynamic Media preset renditions and smart-crops for download, directly from within the Content Hub User Interface.

​![Dynamic Media renditions](/help/assets/assets/dm-renditions-content-hub.png)

[!BADGE Dive Deeper into this Feature]{type=Informative url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/content-hub/download-assets-content-hub#download-asset-renditions"}


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

