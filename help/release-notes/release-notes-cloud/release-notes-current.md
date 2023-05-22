---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
mini-toc-levels: 1
exl-id: a2d56721-502c-4f4e-9b72-5ca790df75c5
---
# Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the current (latest) version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions; for example, for those in 2021, 2022, and so on.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2023.4.0) is May 25, 2023. The next feature release (2023.6.0) is planned for June 29, 2023.

## Release Video {#release-video}

Have a look at the April 2023 Release Overview video for a summary of the features added in the 2023.4.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3418681/?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features in [!DNL Experience Manager Sites] {#sites-features}

* Export content fragments from AEM as a cloud service to Adobe target as JSON offers.
* Support for GraphQL pagination and sorting, along with internal caching enhancements, now help improve the performance of decoupled client applications when fetching large content sets from AEM using complex GraphQL queries and filters.

### New features in [!DNL Experience Manager Sites] prelease {#prerelease-sites}

* Content Fragments and their references can now be published to the [AEM Preview Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-environments.html?lang=en#access-preview-service) using the [Content Fragment Console](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/content-fragments-console.html?lang=en), allowing users to preview the final experience on a decoupled preview application before going live.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#assets-features}

* Added support for WebP images to automatically extract metadata, generate thumbnails and custom renditions. Smart Tags capability is also now supported for these files. Dynamic Media capabilities are not supported for WebP as an input format.

* [Search experience enhancements](/help/assets/search-assets.md#aftersearch) - You can now quickly perform the following operations on the assets that display in the search results:

   * Create a workflow
   * Create a new version
   * Relate or Unrelate assets

     You do not need to navigate to the asset location and view its properties to perform these operations.

* Color Search facet usability improvements - Input field for color values is now editable and search results update only when you exit the color picker. 

* New protocol (DASH - Dynamic Adaptive Streaming over HTTP) support launched for Adaptive streaming in Dynamic Media video delivery (with CMAF enabled):
   * Adaptive streaming (DASH/HLS) ensures better end user viewing experience for videos
   * DASH is the international standard protocol for adaptive video streaming and is widely adopted in the industry
   * Available in all regions, to be enabled via support ticket


* Dynamic Media _Snapshot_ - Experiment with test images or Dynamic Media URLs, to see the output of different image modifiers, and Smart Imaging optimizations for file size (with WebP and AVIF delivery), network bandwidth, and Device Pixel Ratio. See [Dynamic Media Snapshot](https://experienceleague.adobe.com/docs/experience-manager-learn/assets/dynamic-media/images/dynamic-media-snapshot.html).

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features available in [!DNL Forms] {#new-features-available-in-channel}

* **[Submit Adaptive Forms to Microsoft SharePoint and Microsoft OneDrive](/help/forms/configuring-submit-actions.md)**: Improve business user agility to launch new forms quickly and store submitted data in everyday tools they use like Microsoft SharePoint site or OneDrive folder.

![Submit Adaptive Forms to Microsoft SharePoint and Microsoft OneDrive](/help/forms/assets/onedrive-and-sharepoint.jpg)


### Features in [!DNL Forms] prerelease {#prerelease-features-forms}

*   Enhanced Adobe Acrobat Sign integration and compliance: AEM Forms now integrate with Adobe Acrobat Sign for Government, providing an advanced level of compliance and security for e-Signatures with Adaptive Form submissions for government associated accounts (Government departments and agencies).

   Integration with Adobe Acrobat Sign for Government enables our partners and government customers to use electronic signatures in Adaptive Forms for some of the most mission-critical and sensitive lines of business. This additional layer of security ensures that all e-signatures are fully compliant with FedRAMP moderated compliances, providing our government customers with peace of mind.

*   Adaptive Forms within AEM Sites editor: You can now use AEM Sites editor to quickly create and add multiple forms to your sites pages. This capability allows content authors to create seamless data capture experiences within Sites pages using the power of adaptive forms components including dynamic behavior, validations, data integration, generate document of record and business process automation. You can: 

      * Create an Adaptive Form by dragging and dropping form components to Adaptive Forms Container Component in AEM Sites editor.  
      *   Use the Adaptive Forms Wizard within AEM Sites editor to create forms independent of any Sites page, providing you the freedom to reuse such forms across multiple pages.
      *   Add multiple forms to a Sites page, streamlining the user experience and providing greater flexibility.

      >[!VIDEO](https://video.tv.adobe.com/v/3419284?quality=12&learn=on)
  
*   Enhance error handling with custom error handlers in rule editor: You can now invoke a custom function (using Client Library) in response to an error returned by an external service and provide a tailored response to end users or take specific actions for errors returned by a service. For instance, you can invoke a custom workflow in the backend for specific error codes or inform the customer that the service is down.

   This helps improve your overall error-handling capability by introducing standards-based error responses, that are backward compatible with OOTB error handlers, with greater flexibility and control.

## Headless Adaptive Forms early adopter program {#forms-early-adopter}

Use Headless Adaptive Forms to enable your developers to create, publish, and manage interactive forms that can be accessed and interacted with through APIs, rather than through a traditional graphical user interface. Headless adaptive forms help you: 

* build high-quality multi-channel forms in the programming language of your choice 
* natively integrate forms to your desktop and mobile apps, websites, and chat applications 
* reuse your proprietary UI components with forms applications 
* leverage the power of Adobe Experience Manager Forms 

You can send an email to aem-forms-headless@adobe.com from your official email ID to join the early adopter program. 

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here.](/help/implementing/cloud-manager/release-notes/current.md)

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
