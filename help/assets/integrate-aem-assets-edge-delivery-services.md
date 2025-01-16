---
title: Integrate AEM Assets while authoring content for Edge Delivery Services
description: Learn how to integrate the AEM Assets with Edge Delivery Services. This integration enables you to integrate AEM Assets with Microsoft Word and Google Docs, integrate AEM Assets with Universal Editor, integrate Dynamic Media with OpenAPI capabilities with Universal Editor and integrate Dynamic Media with OpenAPI capabilities with Microsoft Word and Google Docs.
exl-id: e58db2ce-a55a-49b3-ae8e-709b5ea8d095
---
# Integrate AEM Assets while authoring content for Edge Delivery Services {#integrate-aem-assets-while-authoring-for-edge-delivery-services}

![EDS2](/help/assets/assets/EDS2.png)

[Edge Delivery Services](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/overview) is a composable set of services that allows for a high degree of flexibility in how you author and deliver content on your website. You can use both [AEM content management](/help/sites-cloud/authoring/author-publish.md) and [WYSIWYG authoring using the Universal Editor as well as Document-Based Authoring](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/wysiwyg-authoring/authoring).

You can edit content in:

* [Microsoft Word or Google Docs](#integrate-aem-assets-with-document-based-authoring-tools)
* [Universal Editor](#integrate-aem-assets-with-universal-editor)

After editing the content, you can publish it to Edge Delivery Services.

## Integrating AEM Assets with Document-Based Authoring flows for Edge Delivery Services {#integrate-aem-assets-with-document-based-authoring-tools}

AEM Assets integration with the Document-Based Authoring tools, such as Microsoft Word or Google Docs, provides an asset selector in your editor directly. Use this asset selector to access to the AEM Assets, and insert approved assets into your document.

If you already have an Edge Delivery Services website, see [AEM Assets plugin](https://github.com/adobe-rnd/aem-assets-plugin/blob/main/README.md) to integrate AEM Assets with your existing AEM project. If you don't have an Edge Delivery Services website see, [Prerequisites](#integrate-aem-assets-with-microsoft-word-and-google-docs) and [Integrating AEM Assets with Document-Based Authoring environment](#integrate-aem-assets-with-microsoft-word-or-google-docs-to-use-aem-assets-with-microsoft-word-or-google-docs) sections below.

### Prerequisites{#integrate-aem-assets-with-microsoft-word-and-google-docs}

Before you begin, ensure that your Document-Based Authoring environment is ready:

* Integrate AEM with a Document-Based Authoring tool to set up the authoring environment. See [Getting Started - Developer Tutorial](https://www.aem.live/developer/tutorial) to set up the authoring environment.

### Integrating AEM Assets with Document-Based Authoring environment{#integrate-aem-assets-with-microsoft-word-or-google-docs-to-use-aem-assets-with-microsoft-word-or-google-docs}

Configure the AEM Assets Sidekick plugin to use assets while authoring content in Microsoft Word or Google Docs.

* See [Adobe Experience Manager Assets Sidekick Plugin](https://www.aem.live/docs/aem-assets-sidekick-plugin#using-experience-manager-assets-for-website-authors) to learn how to access and use AEM Assets in Microsoft Word or Google Docs.
* See [Configuring Adobe Experience Manager Assets Sidekick Plugin](https://www.aem.live/developer/configuring-aem-assets-sidekick-plugin) for configuration details.
![my-assets-sidebar](/help/assets/assets/my-assets-sidebar.png)

## Deliver assets using Dynamic Media with OpenAPI capabilities {#integrate-Dynamic-Media-with-OpenAPI-capabilities-with-Microsoft-Word-Google-Docs-and-universal-editor}

You can also use assets delivered using DM with OpenAPI capabilities. It provides many benefits such as:

* Access to brand-approved assets only (images, videos, PDFs, and other asset types) from AEM Assets Cloud Services.
* Governance (references vs. copies of the asset), which helps with auto-propagation of asset lifecycle events like expiration, deletion, and updates.
* Dynamic image renditions and Smart Crop.
* Rich media optimization and delivery, such as adaptive video streaming out-of-the-box, and original asset delivery for PDFs.
* Asset-level impressions report ([limited availability](/help/assets/manage-reports-assets-view.md#dynamic-media-delivery-reports)).

For more details on the capabilities, see [Dynamic Media with OpenAPI capabilities](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dynamic-media-open-apis/dynamic-media-open-apis-overview) documentation.

### Prerequisites {#prerequisites-for-dm-with-openapi-capabilities-to-use-aem-assets}  

To use asset reference, you must have:

* Entitlement to an Assets Cloud Service environment where Dynamic Media with Open API capabilities is enabled.
* A Dynamic Media license.
* The AEM Assets sidekick plugin enabled with copy reference for image assets enabled. For more details, see [this](https://www.aem.live/developer/configuring-aem-assets-sidekick-plugin#copymode) for Document-Based Authoring and see [this](https://developer.adobe.com/uix/docs/extension-manager/extension-developed-by-adobe/configurable-asset-picker/#extension-overview) for Universal Editor based authoring.
* Assets that are approved. Approved assets have `dam:status=Approved` via the Assets Cloud Services backend or UI actions.

### Use assets delivered using Dynamic Media with OpenAPI capabilities{#how-to-use-Dynamic-Media-with-OpenAPI-assets}

To use assets delivered using Dynamic Media with OpenAPI capabilities while authoring content, see:

* [Using image references](https://www.aem.live/docs/aem-assets-sidekick-plugin#using-image-references-when-authoring-content)
* [Using video references](https://www.aem.live/docs/aem-assets-sidekick-plugin#using-video-references-when-authoring-content)
* [Using asset references for non-image and video assets such as PDF, Zip files and more](https://www.aem.live/docs/aem-assets-sidekick-plugin#using-asset-references-for-pdf-zip-etc-when-authoring-content)

See this video to learn how to deliver assets using Dynamic Media with OpenAPI capabilities.

>[!VIDEO](https://video.tv.adobe.com/v/3441155)

## Sample Edge Delivery Services site{#example-of-an-Edge-Delivery-Services-site} 

See [WKND Travel](http://bit.ly/3DExLnf). This site is built using the Document-Based Authoring capabilities of Edge Delivery Services. The site's content is authored in [Google Docs](https://drive.google.com/drive/folders/1HCCHRWp4HJIXW_cUv5cRDQ5DzzqiZsXT), using Dynamic Media with OpenAPI capabilities for asset delivery. Once authored, the content is published directly from the document. For this Document-Based Authoring setup, all the essential files, folders, configurations, website's styling and functionality codes are stored in this [Git repository](https://github.com/hlxsites/franklin-assets-selector/tree/aem-dynamicmedia-demo/blocks).

## Integrating AEM Assets with Universal Editor based authoring flows for Edge Delivery Services {#integrate-aem-assets-with-universal-editor}

Set up the Universal Editor to integrate with AEM Assets. This integration enables you to use Dynamic Media with OpenAPI capabilities to deliver assets.

* See [Configuration in Edge Delivery Site](https://developer.adobe.com/uix/docs/extension-manager/extension-developed-by-adobe/configurable-asset-picker/#configuration-in-edge-delivery-site) to add a custom asset picker function in Universal Editor. The custom asset picker enables you to insert assets into your Universal Editor content directly.
* See [Extension overview](https://developer.adobe.com/uix/docs/extension-manager/extension-developed-by-adobe/configurable-asset-picker/#extension-overview) to learn how to access to AEM Assets and insert the assets while authoring in Universal Editor.
