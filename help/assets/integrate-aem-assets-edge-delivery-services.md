---
title: Integrate [!DNL AEM Assets] while authoring content for [!DNL Edge Delivery Services]
description: Learn how to integrate the [!DNL AEM Assets] with [!DNL Edge Delivery Services]. This integration enables you to integrate [!DNL AEM Assets] with [!DNL Microsoft Word] and [!DNL Google Docs], integrate [!DNL AEM Assets] with [!DNL Universal Editor], integrate [!DNL Dynamic Media with OpenAPI capabilities] with [!DNL Universal Editor] and integrate [!DNL Dynamic Media with OpenAPI capabilities] with [!DNL Microsoft Word] and [!DNL Google Docs].
exl-id: e58db2ce-a55a-49b3-ae8e-709b5ea8d095
---
# Integrate [!DNL AEM Assets] while authoring content for [!DNL Edge Delivery Services] {#integrate-aem-assets-while-authoring-for-edge-delivery-services}

![AEM assets with UE](/help/assets/assets/EDS2.png)

[[!DNL Edge Delivery Services]](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/overview) is a composable set of services that allows for a high degree of flexibility in how you author and deliver content on your website. You can use both [AEM content management](/help/sites-cloud/authoring/author-publish.md) and [WYSIWYG authoring using the [!DNL Universal Editor] as well as Document-Based Authoring](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/wysiwyg-authoring/authoring).

You can edit content in:

* [[!DNL Microsoft Word] or [!DNL Google Docs]](#integrate-aem-assets-with-document-based-authoring-tools)
* [[!DNL Universal Editor]](#integrate-aem-assets-with-UE-universal-editor)

After editing the content, you can publish it to Edge Delivery Services.

## Integrating [!DNL AEM Assets] with Document-Based Authoring flows for [!DNL Edge Delivery Services] {#integrate-aem-assets-with-document-based-authoring-tools}

When [!DNL AEM Assets] integrates with your Document-Based Authoring tools, such as [!DNL Microsoft Word] or [!DNL Google Docs], it provides an asset selector in your authoring tool. Use this asset selector to access [!DNL AEM Assets], and insert approved assets into your content.
If you already have an [!DNL Edge Delivery Services] website, see [[!DNL AEM Assets] plugin](https://github.com/adobe-rnd/aem-assets-plugin/blob/main/README.md) documentation to learn how to integrate [!DNL AEM Assets] with your existing [!DNL AEM] project. 
Follow the following [Prerequisites](#integrate-aem-assets-with-microsoft-word-and-google-docs) and [Integrating [!DNL AEM Assets] with Document-Based Authoring environment](#integrate-aem-assets-with-microsoft-word-or-google-docs-to-use-aem-assets-with-microsoft-word-or-google-docs) sections if you do not have an [!DNL Edge Delivery Services] website to publish your [!DNL AEM Assets] inclusive content authored in document based authoring tools.

### Prerequisites{#integrate-aem-assets-with-microsoft-word-and-google-docs}

Before you begin, ensure that your Document-Based Authoring environment is ready:

* Integrate [!DNL AEM] with a Document-Based Authoring tool to set up the authoring environment. See [Getting Started - Developer Tutorial](https://www.aem.live/developer/tutorial) to learn how to set up the authoring environment.

### Integrating [!DNL AEM Assets] with Document-Based Authoring environment{#integrate-aem-assets-with-microsoft-word-or-google-docs-to-use-aem-assets-with-microsoft-word-or-google-docs}

Configure the [!DNL AEM Assets] Sidekick plugin to use assets while authoring content in [!DNL Microsoft Word] or [!DNL Google Docs].

* See [[!DNL Adobe Experience Manager Assets Sidekick Plugin]](https://www.aem.live/docs/aem-assets-sidekick-plugin#using-experience-manager-assets-for-website-authors) to learn how to access and use AEM Assets in Microsoft Word or Google Docs.
* See [Configuring [!DNL Adobe Experience Manager Assets Sidekick Plugin]](https://www.aem.live/developer/configuring-aem-assets-sidekick-plugin) for configuration details.
![use dynamic media with openAPI capabilities in ms word and google docs](/help/assets/assets/my-assets-sidebar.png)

## Deliver assets using [!DNL Dynamic Media with OpenAPI capabilities] {#integrate-Dynamic-Media-with-OpenAPI-capabilities-with-Microsoft-Word-Google-Docs-and-universal-editor}

You can also use assets delivered using [!DNL Dynamic Media with OpenAPI capabilities]. It provides many benefits such as:

* Access to brand-approved assets only (images, videos, PDFs, and other asset types) from [!DNL AEM Assets Cloud Services].
* Governance (references vs. copies of the asset), which helps with auto-propagation of asset lifecycle events like expiration, deletion, and updates.
* Dynamic image renditions and Smart Crop.
* Rich media optimization and delivery, such as adaptive video streaming out-of-the-box, and original asset delivery for PDFs.
* Asset-level impressions report ([limited availability](/help/assets/manage-reports-assets-view.md#dynamic-media-delivery-reports)).

For more details on the capabilities, see [[!DNL Dynamic Media with OpenAPI capabilities]](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dynamic-media-open-apis/dynamic-media-open-apis-overview) documentation.

### Prerequisites {#prerequisites-for-dm-with-openapi-capabilities-to-use-aem-assets}  

To use asset reference, you must have:

* Entitlement to an Assets Cloud Service environment where [!DNL Dynamic Media with Open API capabilities] is enabled.
* A [!DNL Dynamic Media] license.
* The [!DNL AEM Assets sidekick plugin] enabled with copy reference for image assets enabled. For more details, see [this documentation](https://www.aem.live/developer/configuring-aem-assets-sidekick-plugin#copymode) for Document-Based Authoring and see [this documentation](https://developer.adobe.com/uix/docs/extension-manager/extension-developed-by-adobe/configurable-asset-picker/#extension-overview) for Universal Editor based authoring.
* Assets that are approved. Approved assets have `dam:status=Approved` via the Assets Cloud Services backend or UI actions.

### Use assets delivered using [!DNL Dynamic Media with OpenAPI capabilities]{#how-to-use-Dynamic-Media-with-OpenAPI-assets}

Select the following links to learn how to use [!DNL Dynamic Media with OpenAPI capabilities] to deliver images, videos and other asset types in your content:

* [Add images to your content](https://www.aem.live/docs/aem-assets-sidekick-plugin#using-image-references-when-authoring-content)
* [Add videos to your content](https://www.aem.live/docs/aem-assets-sidekick-plugin#using-video-references-when-authoring-content)
* [Add non-image and video assets such as PDF, Zip files and more to your content](https://www.aem.live/docs/aem-assets-sidekick-plugin#using-asset-references-for-pdf-zip-etc-when-authoring-content)

See this video to learn how to deliver assets in your content using Dynamic Media with OpenAPI capabilities.

>[!VIDEO](https://video.tv.adobe.com/v/3441155)

## Sample [!DNL Edge Delivery Services] site{#example-of-an-Edge-Delivery-Services-site} 

See [WKND Travel](http://bit.ly/3DExLnf), a site that is built using the Document-Based Authoring capabilities of [!DNL Edge Delivery Services]. The site's content is authored in [Google Docs](https://drive.google.com/drive/folders/1HCCHRWp4HJIXW_cUv5cRDQ5DzzqiZsXT) and [!DNL Dynamic Media with OpenAPI capabilities] is used to deliver assets in the content. After authoring, the content is published from the document directly. Explore this [Git repository](https://github.com/hlxsites/franklin-assets-selector/tree/aem-dynamicmedia-demo/blocks) to know about all the essential files, folders, configurations, website's styling and functionality codes that are used to create the Document-Based Authoring setup for this [!DNL Edge Delivery Services (EDS)] site.

## Integrating [!DNL AEM Assets] with [!DNL Universal Editor] based authoring flows for [!DNL Edge Delivery Services] {#integrate-aem-assets-with-UE-universal-editor}

Set up the [!DNL Universal Editor] to integrate with [!DNL AEM Assets]. This integration enables you to use [!DNL Dynamic Media with OpenAPI capabilities] to deliver assets.

* See [Configuration in [!DNL Edge Delivery] Site](https://developer.adobe.com/uix/docs/extension-manager/extension-developed-by-adobe/configurable-asset-picker/#configuration-in-edge-delivery-site) to learn how to add a custom asset picker function in [!DNL Universal Editor]. The custom asset picker enables you to insert assets into your [!DNL Universal Editor] content directly.
* See [Extension overview](https://developer.adobe.com/uix/docs/extension-manager/extension-developed-by-adobe/configurable-asset-picker/#extension-overview) to learn how to access to [!DNL AEM Assets] and insert the assets while authoring in [!DNL Universal Editor].
