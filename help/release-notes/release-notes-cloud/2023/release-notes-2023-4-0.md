---
title: Release Notes for 2023.4.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2023.4.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: c34aedee-e45a-4e2a-ae7f-930bc0cc026f
feature: Release Information
role: Admin
---
# 2023.4.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2023.4.0 version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions such as 2021 or 2022.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2023.4.0) is June 7, 2023. The next feature release (2023.6.0) is planned for June 29, 2023.

## Release Video {#release-video}

Have a look at the April 2023 Release Overview video for a summary of the features added in the 2023.4.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3418681/?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features in [!DNL Experience Manager Sites] {#sites-features}

* Export Content Fragments from AEM as a Cloud Service to Adobe Target in JSON format and create corresponding JSON offers in Target.
* Support for GraphQL pagination and sorting, along with internal caching enhancements, now help improve the performance of decoupled client applications when fetching large content sets from AEM using complex GraphQL queries and filters. 

### New features in [!DNL Experience Manager Sites] prerelease {#prerelease-sites}

* Content Fragments and their references can now be published to the [AEM Preview Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-environments.html#access-preview-service) using the [Content Fragment Console](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/content-fragments-console.html), allowing users to preview the final experience on a decoupled preview application before going live.
* Images can now be dynamically optimized for web-delivery in headless scenarios using AEM GraphQL. [Query variables](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/how-to/images.html#query-variables) can be defined in GraphQL queries to allow decoupled client applications request accordingly optimized images from AEM. 
* Tags on [Content Fragment Variations](https://experienceleague.adobe.com/docs/experience-manager-65/assets/content-fragments/content-fragments-variations.html) can now be output to JSON using the AEM GraphQL conent delivery API. 

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#assets-features}

*   Added support for WebP images to automatically extract metadata, generate thumbnails and custom renditions. Smart Tags capability is also now supported for these files. Dynamic Media capabilities are not supported for WebP as an input format.

*   [Search experience enhancements](/help/assets/search-assets.md#aftersearch) - You can now quickly perform the following operations on the assets that display in the search results:

    * Create a workflow
    * Create a version
    * Relate or Unrelate assets

      You do not need to navigate to the asset location and view its properties to perform these operations.

*   Color Search facet usability improvements - Input field for color values is now editable and search results update only when you exit the color picker. 

*   New protocol support launched (DASH - Dynamic Adaptive Streaming over HTTP) for Adaptive streaming in Dynamic Media video delivery (with CMAF enabled):
    * Adaptive streaming (DASH/HLS) ensures better user viewing experience for videos
    * DASH is the international standard protocol for adaptive video streaming and is widely adopted in the industry
    * Available in all regions, to be enabled via support ticket

*  Dynamic Media _Snapshot_ - Experiment with test images or Dynamic Media URLs, to see the output of different image modifiers, and assess Smart Imaging optimizations for file size (with WebP and AVIF delivery), network bandwidth, and Device Pixel Ratio. See [Dynamic Media Snapshot](https://experienceleague.adobe.com/docs/experience-manager-learn/assets/dynamic-media/images/dynamic-media-snapshot.html).

### Feature in [!DNL Assets] prerelease {#prerelease-feature-assets}

* Dynamic Media - The user interface for some Smart Crop-related fields in an Image Profile are now updated to reflect the current guidelines for defining a Smart Crop. See [Crop options](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/assets/dynamicmedia/image-profiles.html#crop-options). 

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features available in [!DNL Forms] {#new-features-available-in-channel}

* **[Submit Adaptive Forms to Microsoft&reg; SharePoint and Microsoft&reg; OneDrive](/help/forms/configuring-submit-actions.md)**: Improve business user agility so you can launch new forms quickly and store submitted data in everyday tools they use like Microsoft&reg; SharePoint site or OneDrive folder.

### Features in [!DNL Forms] prerelease {#prerelease-features-forms}

* [Adaptive Forms within AEM Page Editor](/help/forms/create-or-add-an-adaptive-form-to-aem-sites-page.md): You can now use AEM Page Editor to quickly create and add multiple forms to your sites pages. This capability allows content authors to create seamless data capture experiences within Sites pages using the power of adaptive forms components including dynamic behavior, validations, data integration, generate document of record and business process automation. You can: 

    * Create an Adaptive Form by dragging and dropping form components to Adaptive Forms Container Component in AEM Sites editor or Experience Fragments.  
    * Use the Adaptive Forms Wizard within AEM Sites editor so you can create forms independent of any Sites page, providing you the freedom to reuse such forms across multiple pages.
    * Add multiple forms to a Sites page, streamlining the user experience and providing greater flexibility.
   
        >[!VIDEO](https://video.tv.adobe.com/v/3419284?quality=12&learn=on)

* [Adobe Acrobat Sign Solutions for Government](/help/forms/adobe-sign-integration-adaptive-forms.md): AEM Forms now integrate with Adobe Acrobat Sign Solutions for Government. This integration provides an advanced level of compliance and security for e-Signatures with Adaptive Form submissions for government associated accounts (Government departments and agencies).

    Integration with Adobe Acrobat Sign for Government enables Adobe's partners and government customers to use electronic signatures in Adaptive Forms for some of the most mission-critical and sensitive lines of business. This additional layer of security ensures that all e-signatures are fully compliant with FedRAMP Moderate compliance, providing Adobe's government customers with peace of mind.

* Enhanced error handling with custom error handlers in rule editor: You can now invoke a custom function (using Client Library) in response to an error returned by an external service and provide a tailored response to end users. Or, you can take specific actions for errors returned by a service. For example, you can invoke a custom workflow in the backend for specific error codes or inform the customer that the service is down.

    This functionality helps improve your overall error-handling capability by introducing standards-based error responses that are backward compatible with OOTB error handlers, with greater flexibility and control.

### Headless Adaptive Forms early adopter program {#forms-early-adopter}

Use Headless Adaptive Forms to enable your developers to create, publish, and manage interactive forms that can be accessed and interacted with through APIs, rather than through a traditional graphical user interface. Headless adaptive forms help you: 

* build high-quality multi-channel forms in the programming language of your choice 
* natively integrate forms to your desktop and mobile apps, websites, and chat applications 
* reuse your proprietary UI components with forms applications 
* use the power of Adobe Experience Manager Forms 

You can send an email to `aem-forms-headless@adobe.com` from your official email ID to join the early adopter program. 

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### What is New {#what-is-new-foundation}

* Additional Publish Regions: Sites Customers may license up to three publish regions, in addition to the primary region. Traffic is routed to additional publish farms, which results in lowered latency for certain requests, and increased resilience against regional outages. Contact your Adobe Account Manager for information about licensing [Additional Publish Regions](/help/operations/additional-publish-regions.md) for your programs.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes/current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
