---
title: Configure and use asset microservices for asset processing
description: Learn how to configure and use the cloud-native asset microservices to process assets at scale.
contentOwner: AG
---

# Use asset microservices and processing profiles {#get-started-using-asset-microservices}

<!--
* Current capabilities of asset microservices offered. If workers have names then list the names and give a one-liner description. (The feature-set is limited for now and continues to grow. So will this article continue to be updated.)
* How to access the microservices. UI. API. Is extending possible right now?
* Detailed list of what file formats and what processing is supported by which workflows/workers process.
* How/where can admins check what's already configured and provisioned.
* How to create new config or request for new provisioning/purchase.

* [DO NOT COVER?] Exceptions or limitations or link back to lack of parity with AEM 6.5.
-->

Asset microservices provide for scalable and resilient processing of assets using cloud services. Adobe manages the services for optimal handling of different asset types and processing options.

Asset processing depends on the configuration in **[!UICONTROL Processing Profiles]**, which provide a default set up, and allow an administrator to add more specific asset processing configuration. Administrators can create and maintain the configurations of post-processing workflows, including optional customization. Customizing workflows allows for extensibility and full customization.

Asset microservices allows you can process a [broad range of file types](/help/assets/file-format-support.md) covering more formats out-of-the-box than what is possible with previous versions of Experience Manager. For example, thumbnail extraction of PSD and PSB formats is now possible that previously required third-party solutions like ImageMagick.

<!-- Proposed DRAFT diagram for asset microservices flow - see section "asset-microservices-flow.png (asset-microservices-configure-and-use.md)" in the PPTX deck

https://adobe-my.sharepoint.com/personal/gklebus_adobe_com/_layouts/15/guestaccess.aspx?guestaccesstoken=jexDC5ZnepXSt6dTPciH66TzckS1BPEfdaZuSgHugL8%3D&docid=2_1ec37f0bd4cc74354b4f481cd420e07fc&rev=1&e=CdgElS
-->

![A high-level view of asset processing](assets/asset-microservices-flow.png "A high-level view of asset processing")

>[!NOTE]
>
>The asset processing described here replaces the `DAM Update Asset` workflow model that exists in the previous versions of [!DNL Experience Manager]. Most of the standard rendition generation and metadata-related steps are replaced by the asset microservices processing, and remaining steps, if any, can be replaced by the post-processing workflow configuration.

## Understand asset processing options {#get-started}

Experience Manager allows for the following levels of processing.

|Configuration|Description|Use cases covered|
|---|---|---|
|[Default configuration](#default-config)|It is available as is and cannot be modified. This configuration provides very basic rendition generation capability.| Standard thumbnails used by [!DNL Assets] user interface (48, 140, and 319 px); Large preview (web rendition - 1280 px); Metadata and text extraction. |
|[Standard configuration](#standard-config) | Configured by administrators via user interface only. Provides more options for rendition generation than the above default configuration.| Change format and resolution of images; generate FPO renditions. |
|[Custom configuration](#custom-config) | Configured by administrators via user interface to invoke custom workers that support more complex requirements. Leverages a cloud-native [!DNL Asset Compute Service]. | See [allowed use cases](#custom-config). |

To create custom processing profiles specific to your custom requirements, say to integrate with other systems, see [post-processing workflows](#post-processing-workflows).

## Supported file formats {#supported-file-formats}

Asset microservices provide support for a wide variety of file formats in terms of the ability to generate renditions or extract metadata. See [supported file formats](file-format-support.md) for the full list.

## Default configuration {#default-config}

Some defaults are pre-configured to ensure that the default renditions required in Experience Manager are available. The default configuration also ensure that metadata extraction and text extraction operations are available. Users can start uploading or updating assets immediately and basic processing is available by default.

With the default configuration, only the most basic processing profile is configured. Such a processing profile is not visible on the user interface and you cannot modify it. It always executes to process uploaded assets. Such a default processing profile ensures that the basic processing required by [!DNL Experience Manager] is completed on all assets.

<!-- ![processing-profiles-standard](assets/processing-profiles-standard.png)
-->

## Standard profile {#standard-config}

[!DNL Experience Manager] provide capabilities to generate more specific renditions for common formats as per user's needs. An administrator can create additional [!UICONTROL Processing Profiles] to facilitate such rendition creation. Users then assign one or more of the available profiles to specific folders to get the additional processing done. Say for example, the additional processing can generate renditions for web, mobile, and tablet. The following video illustrates how to create and apply [!UICONTROL Processing Profiles] and how to access the created renditions.

* **Rendition width and height**: Rendition width and height specification provides maximum sizes of the generated output image. Asset microservices tries to produce the largest possible rendition, which width and height is not bigger than the specified width and height, respectively. The aspect ratio is preserved, that is the same as the original. An empty value means that asset processing assumes the pixel dimension of the original.

* **MIME type inclusion rules**: When an asset with a specific MIME type is processed, the MIME type is first checked against the excluded MIME types value for the rendition specification. If it matches that list, this specific rendition is not generated for the asset (blocked list). Otherwise, the MIME type is checked against the included MIME type, and if it matches the list, the rendition is generated (allowed list).

* **Special FPO rendition**: When placing large-sized assets from [!DNL Experience Manager] into [!DNL Adobe InDesign] documents, a creative professional waits for a substantial time after they [place an asset](https://helpx.adobe.com/indesign/using/placing-graphics.html). Meanwhile, the user is blocked from using [!DNL InDesign]. This interrupts creative flow and negatively impacts the user experience. Adobe enables temporarily placing small-sized renditions in [!DNL InDesign] documents to begin with, which can be replaced with full-resolution assets on-demand later. [!DNL Experience Manager] provides renditions that are used for placement only (FPO). These FPO renditions have a small file size but are of the same aspect ratio.

The processing profile can include a FPO (For Placement Only) rendition. See [!DNL Adobe Asset Link] [documentation](https://helpx.adobe.com/enterprise/using/manage-assets-using-adobe-asset-link.html) to understand if you need to turn it on for your processing profile. For more information, see [Adobe Asset Link complete documentation](https://helpx.adobe.com/enterprise/using/adobe-asset-link.html).

### Create standard profile {#create-standard-profile}

To create standard processing profile, follow these steps:

1. Administrators access **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Processing Profiles]**. Click **[!UICONTROL Create]**.
1. Provide a name that helps you uniquely identify the profile when applying to a folder.
1. To generate FPO renditions, on the **[!UICONTROL Standard]** tab, enable **[!UICONTROL Create FPO Rendition]**. Input a **[!UICONTROL Quality]** value between 1 and 100.
1. To generate other renditions, click **[!UICONTROL Add New]** and provide the following information:

   * File name of each rendition.
   * File format (PNG, JPEG, or GIF) of each rendition.
   * Width and height in pixels of each renditions. If the values are not specified, the full pixel size of the original image is used.
   * Quality in percent of each JPEG rendition.
   * Included and excluded MIME types to define the applicability of a profile.

![processing-profiles-adding](assets/processing-profiles-adding.png)

1. Click **[!UICONTROL Save]**.

The following video demonstrates the usefulness and usage of standard profile.

>[!VIDEO](https://video.tv.adobe.com/v/29832?quality=9)

<!-- Removed per cqdoc-15624 request by engineering.
 ![processing-profiles-list](assets/processing-profiles-list.png) 
 -->

## Custom profile and use cases {#custom-config}

**TBD items**:

* Overall cross-linking with the extensibility content.
* Mention how to get URL of worker. Worker URL for Dev, Stage, and Prod environments.
* Mention mapping of service parameters. Link to compute service article.
* Review from flow perspective shared in Jira ticket.

Some complex asset processing use cases cannot be accomplished using default configurations as the needs of the organizations are varied. Adobe offers [!DNL Asset Compute Service] for such use cases. It is a scalable and extensible service to process digital assets. It can transform image, video, document and other file formats into different renditions including thumbnails, extracted text & metadata and archives.

Developers can use the Asset Compute Service to create specialized custom workers that cater to pre-defined, complex use cases. [!DNL Experience Manager] can invoke these custom workers from the user interface by using custom profiles that administrators configure. [!DNL Asset Compute Service] supports the following use cases:

* Generate custom enhanced smart tags for digital assets using Adobe Sensei.
* Generate cropping mask of a subject using Adobe Sensei.
* Retrieve product metadata information from PIM system and make the metadata part of binary of asset during ingestion of asset.
* Change the background color of a transparent image using [!DNL Adobe Photoshop] API.
* Retouch an image using [!DNL Photoshop] API.
* Straighten an image using [!DNL Adobe Lightroom] API.

>[!NOTE]
>
>You cannot edit the standard metadata using the custom workers. You can only modify custom metadata.

### Create a custom profile {#create-custom-profile}

To create a custom profile, following these steps:

1. Administrators access **[!UICONTROL Tools > Assets > Processing Profiles]**. Click **[!UICONTROL Create]**.
1. Click on **[!UICONTROL Custom]** tab. Click **[!UICONTROL Add New]**. Provide the desired file name of the rendition.
1. Provide the following information and click **[!UICONTROL Save]**.

   * File name of each rendition and a supported file extension.
   * End-point URL of a Firefly custom app. The app must be from the same organization as the Experience Manager account is.
   * Add Service Parameters as required.
   * Included and excluded MIME types to define the applicability of a profile.

![custom-processing-profile](assets/custom-processing-profile.png)

>[!CAUTION]
>
>If the Firefly app and [!DNL Experience Manager] account are not from the same organization, the integration does not work.

## Use processing profiles to process assets {#use-profiles}

Create and apply the additional, custom processing profiles to specific folders for Experience Manager to process for assets uploaded to or updated in these folders. The default, in-built standard processing profile is always executed but is not visible on the user interface. If you add a custom profile, then both profiles are used to process the uploaded assets.

Apply processing profiles to folders using one of the following methods:

* Administrators can select a processing profile definition in **[!UICONTROL Tools > Assets > Processing Profiles]**, and use **[!UICONTROL Apply Profile to Folder(s)]** action. It opens a content browser that allow you to navigate to specific folders, select them and confirm the application of the profile.
* Users can select a folder in the Assets user interface, use **[!UICONTROL Properties]** action to open folder properties screen, click on the **[!UICONTROL Processing Profiles]** tab, and in the popup list, select the correct processing profile for that folder. To save the changes, click **[!UICONTROL Save & Close]**.

>[!NOTE]
>
>Only one processing profile can be applied to a specific folder. To generate more renditions, add more rendition definitions to the existing processing profile.

After a processing profile is applied to a folder, all the new assets uploaded (or updated) in this folder or any of it's sub-folders are processed using the additional processing profile configured. This processing is in addition to the standard, default profile. If you apply multiple profiles to a folder, the uploaded or updated assets are processed using each of these profiles.

>[!NOTE]
>
>A processing profile applied to a folder works for the entire tree, but can be over-ridden with another profile applied to a sub-folder. When assets are uploaded to a folder, Experience Manager checks the containing folder's properties for a processing profile. If none is applied, a parent folder in the hierarchy is checked for a processing profile to apply.

Users can check that the processing actually took place by opening a newly-uploaded asset for which processing has finished, opening asset preview, and clicking on the left-hand rail's **[!UICONTROL Renditions]** view. The specific renditions in the processing profile, for which the specific asset's type matches the MIME type inclusion rules, should be visible and accessible.

![additional-renditions](assets/renditions-additional-renditions.png)

*Figure: Example of two additional renditions generated by a processing profile applied to the parent folder.*

## Post-processing workflows {#post-processing-workflows}

For situation, where additional processing of assets is required that cannot be achieved using the processing profiles, additional post-processing workflows can be added to the configuration. This allows for adding fully customized processing on top of the configurable processing using asset microservices.

Post-processing workflows, if configured, are automatically executed by AEM after the microservices processing finishes. There is no need to add workflow launchers manually to trigger them. The examples include:

* Custom workflow steps to process assets.
* Integrations to add metadata or properties to assets from external systems, for example, product or process information.
* Additional processing done by external services.

Adding a post-processing workflow configuration to Experience Manager is comprised of the following steps:

* Create one or more workflow models. The documents mention it as *post-processing workflow models*, but those are regular Experience Manager workflow models.
* Add specific workflow steps to these models. The steps are executed on the assets based on a workflow model configuration.
* Add [!UICONTROL DAM Update Asset Workflow Completed Process] step at the end. Adding this step ensures that Experience Manager knows when the processing ends and the asset can be marked as processed, that is *New* is displayed on the asset.
* Create a configuration for the Custom Workflow Runner Service that allows to configure execution of a post-processing workflow model either by a path (folder location) or by a regular expression.

### Create post-processing workflow models {#create-post-processing-workflow-models}

Post-processing workflow models are regular AEM workflow models. Create different models if you need different processing for different repository locations or asset types.

Processing steps should be added based on needs. You can use any supported steps available, as well as any custom-implemented workflow steps.

Ensure that the last step of each post-processing workflows is `DAM Update Asset Workflow Completed Process`. The last step helps ensure that Experience Manager knows when asset processing is completed.

### Configure post-processing workflow execution {#configure-post-processing-workflow-execution}

To configure the post-processing workflow models to be executed for assets uploaded or updated in the system after the asset microservices processing finishes, the Custom Workflow Runner service needs to be configured.

The Custom Workflow Runner service (`com.adobe.cq.dam.processor.nui.impl.workflow.CustomDamWorkflowRunnerImpl`) is an OSGi service and provides two options for configuration:

* Post-processing workflows by path (`postProcWorkflowsByPath`): Multiple workflow models can be listed, based on different repository paths. Paths and models should be separated by a colon. Simple repository paths are supported and should be mapped to a workflow model in the `/var` path. For example: `/content/dam/my-brand:/var/workflow/models/my-workflow`.
* Post-processing workflows by expression (`postProcWorkflowsByExpression`): Multiple workflow models can be listed, based on different regular expressions. Expressions and models should be separated by a colon. The regular expression should point to the Asset node directly, and not one of the renditions or files. For example: `/content/dam(/.*/)(marketing/seasonal)(/.*):/var/workflow/models/my-workflow`.

>[!NOTE]
>
>Configuration of the Custom Workflow Runner is a configuration of an OSGi service. See [deploy to Experience Manager](/help/implementing/deploying/overview.md) for information on how to deploy an OSGi configuration.
>OSGi web console, unlike in on-premise and managed services deployments of AEM, is not directly available in the cloud service deployments.

For details about which standard workflow step can be used in the post-processing workflow, see [workflow steps in post-processing workflow](developer-reference-material-apis.md#post-processing-workflows-steps) in the developer reference.

## Best practices and limitations {#best-practices-limitations-tips}

* Consider your needs for all types of renditions when designing workflows. If you do not foresee the need of a rendition in the future, remove its creation step from the workflow. Renditions cannot be deleted in bulk afterwards. Undesired renditions may take up a lot of storage space after prolonged use of [!DNL Experience Manager]. For individual assets, you can remove renditions manually from the user interface. For multiple assets, you can either customize [!DNL Experience Manager] to delete specific renditions or delete the assets and upload those again.
