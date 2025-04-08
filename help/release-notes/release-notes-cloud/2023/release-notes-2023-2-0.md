---
title: Release Notes for 2023.2.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2023.2.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: 671056e6-84cc-4c2c-bca3-fde68d5cc835
feature: Release Information
role: Admin
---
# 2023.2.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2023.2.0 version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions; for example, for those in 2021, 2022, and so on.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2023.2.0) is April 12, 2023. The next feature release (2023.4.0) is planned for June 7, 2023.

## Release Video {#release-video}

Have a look at the February 2023 Release Overview video for a summary of the features added in the 2023.2.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3416885/?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features in [!DNL Experience Manager Sites] prelease {#prerelease-sites}

* Export content fragments from AEM as a cloud service to Adobe target as JSON offers.
* Support for GraphQL pagination and sorting, along with internal caching enhancements, now help improve the performance of decoupled client applications when fetching large content sets from AEM using complex GraphQL queries and filters.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#assets-features}

* New protocol (DASH - Dynamic Adaptive Streaming over HTTP) support launched for Adaptive streaming in Dynamic Media video delivery (with CMAF enabled):
   * Adaptive streaming (DASH/HLS) ensures better user viewing experience for videos
   * DASH is the international standard protocol for adaptive video streaming and is widely adopted in the industry

* Added support for WebP images to automatically extract metadata, generate thumbnails and custom renditions. Smart Tag and Smart Crop capabilities are also now supported for these files.

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features available in [!DNL Forms] {#new-features-available-in-channel}

* **[Use data capture core components to build Adaptive Forms](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html)**: [Use Adaptive Forms editor](/help/forms/creating-adaptive-form-core-components.md) to create forms based on standardized data capture components (Core Components). These components provide customization capabilities, reduced development time, and lower maintenance costs for your digital enrolment experiences.

*   **[Frontend pipeline support for styling core component based Adaptive Forms](/help/forms/using-themes-in-core-components.md)**: Utilize standardized BEM-based themes for Core Components-based Adaptive Forms by deploying them with Frontend Deployment pipeline to enhance the look and feel of your forms and align with your organization's brand approved design guidelines.

*   **[Generate Document of Record for core component based Adaptive Forms](/help/forms/generate-document-of-record-core-components.md)**: Create a document of record containing submitted data for Adaptive Forms built using core components for archival or reference to end users, in print or in the document format. 

![https://www.aemcomponents.dev/](/help/forms/assets/sample-core-components-based-adaptive-form.png)

*   **[Efficient form-building with the Save an Adaptive Form as a template feature](/help/forms/template-editor.md#save-an-adaptive-form-as-template-saving-adaptive-form-as-template)**: Expedite and standardize form development by saving existing brand approved forms as form templates for quick reuse.

*   **[Connect AEM Forms to JDBC-Supported databases](/help/forms/configure-data-sources.md#configure-relational-database-configure-relational-database)**: Connect to enterprise databases directly from AEM Cloud service using JDBC protocol, without the need to expose them over REST API.

*   **[Integrate with REST Endpoints Using Open API 3.0](/help/forms/configure-data-sources.md#configure-restful-services-open-api-specification-version-20-configure-restful-services-swagger-version30)**: Seamlessly integrate into systems of record which support Open API 3.0 to store and fetch data using form data models.

*   **[Share an Adaptive Form for review](/help/forms/create-reviews-forms.md)**: Use the Adaptive Forms review mechanism to allow one or more reviewers to review the form.


### Features in [!DNL Forms] prerelease {#prerelease-features-forms}

* **[Submit Adaptive Forms to Microsoft SharePoint and Microsoft OneDrive](/help/forms/configuring-submit-actions.md)**: Improve business user agility to launch new forms quickly and store submitted data in everyday tools they use like Microsoft SharePoint site or OneDrive folder.

![Submit Adaptive Forms to Microsoft SharePoint and Microsoft OneDrive](/help/forms/assets/onedrive-and-sharepoint.jpg)


## Headless Adaptive Forms early adopter program {#forms-early-adopter}

Use Headless Adaptive Forms to enable your developers to create, publish, and manage interactive forms that can be accessed and interacted with through APIs, rather than through a traditional graphical user interface. Headless adaptive forms help you: 

* build high-quality multi-channel forms in the programming language of your choice 
* natively integrate forms to your desktop and mobile apps, websites, and chat applications 
* reuse your proprietary UI components with forms applications 
* use the power of Adobe Experience Manager Forms 

You can send an email to aem-forms-headless@adobe.com from your official email ID to join the early adopter program. 

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes/current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
