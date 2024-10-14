---
title: Adobe's Digital Asset Management (DAM) using AEM 
description: Understand how to use and administer Adobe's Digital Asset Management (DAM) using Experience Manager Assets as a Cloud Service.
contentOwner: AK
feature: Asset Management
role: User, Leader, Architect
exl-id: 4437f214-d058-4975-8b8f-869a12c8103b
---

# Introducing Assets as a [!DNL Cloud Service] for Digital Asset Management in AEM {#assets-cloud-service-introduction}

<!-- Need review information from gklebus -->

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

Adobe Experience Manager Assets as a [!DNL Cloud Service] offers a cloud-native, PaaS solution for businesses to not only perform their Digital Asset Management and Dynamic Media operations with speed and impact, but also use next-generation smart capabilities, such as AI/ML, from within a system that is always current, always available, and always learning.

Concurrent ingestion of many assets or complex assets is resource-intensive task for an Experience Manager Author instance. The primary instance consumes considerable CPU, memory, and I/O resources when assets are added, processed, or even migrated. Such performance issues impact authoring and browsing experience of end users.

Businesses require support for a wide variety of file formats and content resolutions for multi-device, cross-geography, and multilingual use cases. Asset processing and storage requirements demand resources and capabilities that can overburden a traditional solution. At times, technical limitations of asset processing do not yield the desired results and at other times the cost of storage is an impediment for profit margins.

To begin with, understand the [benefits of a cloud-native offering](#solution-benefits) for Digital Asset Management. Check out the notable [changes to Experience Manager as a [!DNL Cloud Service]](/help/release-notes/aem-cloud-changes.md) that also impact Experience Manager Assets followed up the notable [changes to Assets](/help/assets/assets-cloud-changes.md).

Read on to know the [details of the new Assets capabilities](#whats-new-assets) and the [known issues](/help/release-notes/maintenance/latest.md). See a list of [deprecated or removed functionality](/help/release-notes/deprecated-removed-features.md) to know what is removed in this release. Finally, understand the Experience Manager terms with the help of this [glossary](/help/overview/terminology.md).

## Solution benefits {#solution-benefits}

The following are the key benefits of Assets as a [!DNL Cloud Service] for Digital Asset Management. To know more, see [overview of Experience Manager as a [!DNL Cloud Service]](/help/overview/introduction.md).

* **Modern cloud services for asset processing**: The new asset microservices is a cloud-based, scalable, reliable, and hassle-free asset processing service.
* **Highly scalable**: Elastic scalability across all types of deployments. Practically unlimited resources that are available on-demand, as and when needed. Saves the cost of over-design as compared to a traditional system.
* **Latest software**: Always current and always updated. All users have only the latest software with all patches, features, security, and bug fixes available to them. Developers and integrator work with the latest set of APIs without issues of multi-version support.
* **Always online**: Zero downtime (0dt), thanks to the instance deployed in a cluster with backups and redundancy. Upgrades are 0dt as well.
* **Constant monitoring**: The monitoring of the system is automated and built-in checks and triggers help maintain the performance, availability, and overall robustness.
* **Hassle-free deployments**: Experience Manager in the Cloud operations are completely automated that require no manual intervention. For automated deployments, the Cloud Manager (CM) component automates the build of deployable Docker images containing your custom code.

## Available persona-based experiences for Digital Asset Management {#persona-based-experiences}

Adobe offers robust Digital Asset Management (DAM) solutions for you to get the most out of your digital assets. Adobe Experience Manager Assets has two separate experiences that use the same Cloud Services repository:

* **Admin View**: The existing Assets as a Cloud Service user interface. Use the Admin View for all advanced Digital Asset Management capabilities including integrations, workflows, content automation, publishing and more. 

* **Assets View**: Adobe's lightweight asset management experience to store, manage, discover, and use digital assets. Streamlined user interface containing essential Digital Asset Management capabilities. Designed for the light-weight DAM users with a focus on upload, metadata management, search, download, and sharing.

Users with access to the Admin view can also access the Assets view. Assets View provides simplified user interface makes it easy to manage, discover, and distribute your digital assets. A broad set of users from across different functions, including creatives, marketing and line-of-business teams can collaborate on assets and access the right, approved assets when and where they need them. Many casual DAM users prefer the Assets view because it only contains a subset of features. The experience is targeted to creatives, read-only asset consumers, and lighter-weight DAM users.  

DAM librarians, developers, and super-users may continue to use the Admin view or switch between the user interfaces, as needed. You can select the experience that works best for your role. 

![add-tags](assets/newui-overview.svg)

For information on how to access the Assets view and some of the simplifications that it offers over Admin view, see [Introduction to Assets view](/help/assets/assets-view-introduction.md).

## Integration with Document-based Authoring  for Edge Delivery Services {#integrate-doc-authoring-edge-and-assets}

Edge Delivery enables you to create fast, engaging websites where authors can update and publish content quickly, and new sites can be launched rapidly. 

Integrate AEM Assets with Document-based Authoring  for Edge Delivery Services to enable website authors to use images available in AEM Assets repositories while authoring documents in Microsoft Word or Google Docs. For more information, see [Integrate AEM Assets with Document-based Authoring ](/help/edge/using.md#integrate-assets-edge).

## Integration with Adobe Journey Optimizer {#integration-with-ajo}

[Adobe Journey Optimizer](https://business.adobe.com/products/journey-optimizer/adobe-journey-optimizer.html) simplifies journey management for customers to provide omnichannel campaigns with intelligent decisioning and insights. When designing messages using Journey Optimizer, you can access Assets as a Cloud Service repository directly from within the Journey Optimizer interface. Users get access to assets, using the embedded user interface of Experience Manager Assets. For more information, see [Create and manage assets with Experience Manager Assets](https://experienceleague.adobe.com/docs/journey-optimizer/using/content-management/assets-images/assets.html).

## New Assets capabilities {#whats-new-assets}

The significant new capabilities are:

* [Asset microservices](/help/assets/asset-microservices-overview.md)
* [Asset upload methods](/help/assets/add-assets.md)

**See also**

* [Translate Assets](translate-assets.md)
* [Assets HTTP API](mac-api-assets.md)
* [Assets supported file formats](file-format-support.md)
* [Search assets](search-assets.md)
* [Connected assets](use-assets-across-connected-assets-instances.md)
* [Asset reports](asset-reports.md)
* [Metadata schemas](metadata-schemas.md)
* [Download assets](download-assets-from-aem.md)
* [Manage metadata](manage-metadata.md)
* [Search facets](search-facets.md)
* [Manage collections](manage-collections.md)
* [Bulk metadata import](metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)
