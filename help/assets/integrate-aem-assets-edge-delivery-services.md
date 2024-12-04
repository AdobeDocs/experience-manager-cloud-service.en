---
title: Integrate AEM Assets while authoring content for Edge Delivery Services
description: Learn how to integrate the AEM Assets repository with Edge Delivery Services. This integration enables you to — integrate AEM Assets with Microsoft Word and Google Docs, integrate AEM Assets with Universal Editor, integrate Dynamic Media with OpenAPI capabilities with Universal Editor and integrate Dynamic Media with OpenAPI capabilities with Microsoft Word and Google Docs. After this integration, you can — use AEM assets within Microsoft Word and Google Docs, use AEM assets within Universal Editor, use Dynamic Media with OpenAPI capabilities assets within Universal Editor and use Dynamic Media with OpenAPI capabilities assets within Microsoft Word and Google Docs.
---
# Integrate AEM Assets while authoring content for Edge Delivery Services {#integrate-aem-assets-while-authoring-for-edge-delivery-services}

![EDS2](/help/assets/assets/EDS2.png)

Edge Delivery Services is a composable set of services that allows for a high degree of flexibility in how you author content on your website. You can use both [AEM content management](/help/sites-cloud/authoring/author-publish.md) and WYSIWYG authoring using the Universal Editor as well as document-based authoring.

You can edit content in:

* [Microsoft Word or Google docs](#integrate-aem-assets-document-based-authoring)

* [Universal Editor](#integrate-aem-assets-universal-editor)

After editing the content, you can publish it to Edge Delivery Services.

## Integrate AEM Assets with document-based authoring tools {#integrate-aem-assets-document-based-authoring-tools}

AEM Assets integration with the document-based authoring tools, such as Microsoft Word or Google Docs, provides an asset selector in your editor directly. Use this asset selector to access to the AEM Assets repository, and insert approved assets into your document.

### Prerequisites{#integrate-aem-assets-with-microsoft-word-and-google-docs}

Before you begin, ensure your document based authoring environment is ready:

* Integrate AEM with a document based authoring tool to set up the authoring environment for document based authoring. See [Getting Started – Developer Tutorial](https://www.aem.live/developer/tutorial) to set up the authoring environment.

### Integrate AEM Assets repository with the document-based authoring environment{#integrate-aem-assets-with-microsoft-word-or-google-docs-to-use-aem-assets-with-microsoft-word-or-google-docs}

Configure the AEM Assets Sidekick plugin, to use assets from your AEM Assets repository while authoring content in Microsoft Word or Google Docs.

* See [Configuring Adobe Experience Manager Assets Sidekick Plugin](https://www.aem.live/developer/configuring-aem-assets-sidekick-plugin) for configuration details.

* See [Adobe Experience Manager Assets Sidekick Plugin](https://www.aem.live/docs/aem-assets-sidekick-plugin#using-experience-manager-assets-for-website-authors) to learn how to access and use AEM assets in Microsoft Word or Google Docs.
![my-assets-sidebar](/help/assets/assets/my-assets-sidebar.png)

### Deliver assets using Dynamic Media with OpenAPI capabilities {#integrate-Dynamic-Media-with-OpenAPI-capabilities-with-Microsoft-Word-and-Google-Docs}

You can also use assets delivered using DM with OpenAPI Capabilities. It provides many benefits such as:

* Access to brand-approved assets only (images, videos, PDFs, and other Asset types) from AEM Assets Cloud Services.
* Governance (references vs. copies of the asset), which helps with auto-propagation of asset lifecycle events like expiration, deletion, and updates
* Dynamic image renditions and Smart Crop.
* Rich media optimization and delivery, such as adaptive video streaming out-of-the-box, and original asset delivery for PDFs.
* Asset-level impressions report (Coming Soon)

For more details on the capabilities, see [Dynamic Media with OpenAPI capabilities](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/dynamicmedia/dynamic-media-open-apis/dynamic-media-open-apis-overview) documentation.

#### Prerequisites {#prerequisites-for-dm-with-openapi-capabilities-to-use-aem-assets}  

To use asset reference, you must have:

* Entitlement to an Assets Cloud Service environment where Dynamic Media with Open API Capabilities is enabled.
* A Dynamic Media license.
* The AEM Assets sidekick plugin enabled with copy reference for image assets enabled. See [this](https://www.aem.live/developer/configuring-aem-assets-sidekick-plugin#copymode) for more information.
* Assets that are approved. Approved Assets have `dam:status=Approved` via the Assets Cloud Services backend or UI actions.

#### Use assets delivered using Dynamic Media with OpenAPI capabilities {#use-Dynamic-Media-with-OpenAPI-capabilities-assets-within-Microsoft-Word-and-Google-Docs}

To use assets delivered using Dynamic Media with OpenAPI Capabilities while authoring content, see:

* [Using image references](https://www.aem.live/docs/aem-assets-sidekick-plugin#using-image-references-when-authoring-content)
* [Using video references](https://www.aem.live/docs/aem-assets-sidekick-plugin#using-video-references-when-authoring-content)
* [Using asset references for non-image and video assets such as PDF, Zip files and more](https://www.aem.live/docs/aem-assets-sidekick-plugin#using-asset-references-for-pdf-zip-etc-when-authoring-content)

![delivery-prefix-repo](/help/assets/assets/delivery-prefix-repo.jpg)

## Integrate AEM Assets with Universal Editor {#integrate-aem-assets-with-universal-editor-to-use-aem-assets-within-universal-editor}

Set up the Universal Editor to integrate with the AEM Assets repository. This integration enables direct AEM asset insertion into Universal Editor content.

* See [Configuration in Edge Delivery Site](https://developer.adobe.com/uix/docs/extension-manager/extension-developed-by-adobe/configurable-asset-picker/#configuration-in-edge-delivery-site) to add a custom asset picker function in Universal Editor. The custom asset picker enables you to insert assets into your Universal Editor content directly. 
* See [Extension Overview](https://developer.adobe.com/uix/docs/extension-manager/extension-developed-by-adobe/configurable-asset-picker/#extension-overview) to learn how to access and insert AEM assets while authoring in Universal Editor. 

## Publish assets to Edge Delivery Services {#publish-assets-to-edge-delivery-services}

After authoring the content and inserting the appropriate assets within your authoring experience, you need to execute certain steps to publish and get those assets display on the website. For more information on the required steps, see [AEM Edge Delivery Services Assets Plugin](https://github.com/adobe-rnd/aem-assets-plugin/blob/main/README.md).
