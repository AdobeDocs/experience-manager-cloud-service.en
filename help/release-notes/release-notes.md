---
title: Release Notes for Adobe Experience Manager (AEM) as a Cloud Service.
seo-title: Release Notes for Adobe Experience Manager (AEM) as a Cloud Service.
description: Release Notes for Adobe Experience Manager (AEM) as a Cloud Service. 
seo-description: Release Notes for Adobe Experience Manager (AEM) as a Cloud Service. 
---

# Release Information {#release-information}

<!-- details need confirmation by PMs -->

| Product | Adobe Experience Manager as a Cloud Service |
|---|---|
| Version | 2019.12.0 |
| Type | Continuous Update |
| Availability date | Continuous Update |

## Experience Manager Assets as a Cloud Service {#assets-as-a-cloud-service-relnotes}

<!-- Need more details from gklebus 
For overall changes to AEM, link back to /help/release-notes/aem-cloud-changes.md when it is available in master.
-->

Adobe Experience Manager Assets as a Cloud Service offers a cloud-native, SaaS solution for businesses to not only perform their DAM operations with speed and impact, but also use next-generation smart capabilities, such as AI/ML, from within a system that is always current, always available, and always learning.

For detailed information about the new functionality in and the benefits of Assets as a Cloud Service, see [What's new in Assets as a Cloud Service](/help/assets/whats-new-assets.md).

The major new additions, deprecations, and removals are:

* Benefits of a cloud solution. <!-- Insert link to aem-cloud-changes.md  -->
* Online and scalable asset processing using asset microservices that replaces DAM Asset Update workflow. See [Overview of asset microservices](/help/assets/asset-microservices-overview.md).
* Some process steps are unsupported because those cannot be executed efficiently in the cloud environment. Some other process steps are unsupported as asset microservices replace these services and the configurations must be migrated to processing profiles. See [Add custom asset post-processing](/help/assets/asset-microservices-overview.md#add-custom-asset-post-processing).
* New methods to upload assets to AEM. See [add assets to Experience Manager](/help/assets/add-assets.md).
* Third-party software that are invoked by command line, such as ImageMagick and FFMPEG, are not supported.
* ZIP archive files can be uploaded into AEM but the in-repository extraction of ZIP archives is not supported yet.
* [Brand Portal](https://docs.adobe.com/content/help/en/experience-manager-brand-portal/using/introduction/brand-portal.html) support is not available yet.
* [InDesign Server Integration](https://helpx.adobe.com/experience-manager/6-5/assets/using/indesign.html) is not available yet. Asset templates and catalogs are also not available. INDD files are supported for rendition creation, metadata operations, and full-text extraction.
* [Scene7 Connect](https://helpx.adobe.com/experience-manager/6-5/sites/administering/using/scene7.html) and [DM Hybrid](https://helpx.adobe.com/experience-manager/6-5/assets/using/config-dynamic.html) are not available.
* [Connected Assets](https://helpx.adobe.com/experience-manager/6-5/assets/using/use-assets-across-connected-assets-instances.html) functionality is not available yet.
* [AEM Assets sharing with Experience Cloud](https://docs.adobe.com/content/help/en/experience-manager-65/administering/integration/configure-assets-cc-integration.html), that is, Marketing Cloud Assets Core Service, aka MAC, is not be available.
* Smart translation search is not available.
