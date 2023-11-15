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
>From here, you can navigate to release notes of previous versions such as 2021 or 2022.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2023.11.0) is November 30, 2023. The next feature release (2023.12.0) is planned for December 14, 2023.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Release Video {#release-video}

Have a look at the November 2023 Release Overview video for a summary of the features added in the 2023.11.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3425186/?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### Early adopter program {#sites-early-adopter}

**[Find and Replace strings in Content Fragments](/help/sites-cloud/administering/content-fragments/managing.md#find-and-replace-find-and-replace)**: The Content Fragment Console provides users with an easy and intuitive way to replace a string appearing in multiple content fragments at once to help accelerate content velocity.

![Find and Replace](/help/sites-cloud/administering/content-fragments/assets/cf-managing-find-replace.png)

Interested in trying out the feature and sharing feedback? Send an email to **aemcs-headless-adopter@adobe.com** from your official email ID to learn more about the early adopter program. 

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features {#assets-features}

**AEM Assets add-on for Adobe Express**: Experience Manager Assets now provides an [add-on for Adobe Express](/help/assets/addon-adobe-express.md). The add-on allows you to directly access the assets stored in Experience Manager Assets from within the Adobe Express user interface. You can place content managed in AEM Assets in the Express canvas and then save new or edited content in an AEM Assets repository. The add-on provides the following key benefits:

* Increased content reuse by editing and saving new assets in AEM

* Reduced overall time and effort  to create new assets or create new versions of existing assets

  ![Include assets from Assets add-on](/help/assets/assets/aem-assets-add-on-include-assets.png)

### New features in Assets view {#assets-view-features}

* **Bulk import assets from OneDrive data source**: Administrators now have the ability to [import large number of assets from OneDrive to AEM Assets](/help/assets/bulk-import-assets-view.md#onedrive-developer-application). The updated list for the supported data sources for bulk import include Azure, AWS, Google Cloud, Dropbox, and OneDrive. 

  ![assign metadata form to a folder](/help/assets/assets/bulk-import-source-details-onedrive.png)

* **Cross-Org Entitlement Support for Libraries**: Experience Manager Assets now enables you to configure access to Creative Cloud libraries in a different IMS Organization. It allows easier access to the latest cross-product workflows between Creative Cloud and Experience Manager and reduces time and effort for creatives.

### Pre-release features available in [!DNL Experience Manager Assets] {#prerelease-features-assets}

* **Dynamic Media**: [Multi-subtitle and multi-audio track support for videos in Dynamic Media](/help/assets/dynamic-media/video.md#about-msma)&mdash;You can now easily add multiple subtitles and multiple audio tracks to a primary video. This capability means that your videos are accessible across a global audience. You can customize a single, published primary video to a global audience in multiple languages and adhere with accessibility guidelines for different geographical regions. Authors can also manage the subtitles and audio tracks from a single tab in the user interface.

  ![Subtitles and Audio tracks tab on the Properties page of a selected video asset.](/help/release-notes/assets/msma-aem-cs.png)*Subtitles and Audio tracks tab on the Properties page of a selected video asset.*

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features in [!DNL Experience Manager Forms] {#forms-features}

* **[Custom properties for Adaptive Forms](/help/forms/template-editor-core-components.md#add-a-custom-group-name-in-the-policy-of-template-editor)**: You can associate custom attributes (key-value pairs) with a form template or adaptive forms component to allow forms developers to deliver dynamic form behaviors that adapts based on the values of these custom attributes. For example, developers can craft different renditions of a Headless Forms component on mobile, desktop, or web platforms, based on the values of custom attributes, thereby significantly enhancing the user experience across a wide array of devices.

* **Themes and templates**: Kickstart your form creation process with our new themes and templates, tailored to empower both seasoned professionals and new forms authors. Seamlessly built using Adaptive Forms Core Components, these meticulously curated themes and templates allow you to start creating forms swiftly for common use cases.

     ![Out of the box templates](/help/forms/assets/form-templates-ootb.png)


### Early adopter program {#forms-early-adopter}

* **[Protect your documents with DocAssurance APIs (Part of Communication APIs)](/help/forms/aem-forms-cloud-service-communications-introduction.md#document-assurance-doc-assurance)**: The DocAssurance APIs empower you to safeguard sensitive information by signing and encrypting the documents. Through encryption, the contents of a document are transformed into an unreadable format, ensuring that only authorized users can gain access. This fortified layer of protection not only shields valuable data from unauthorized eyes but also provides peace of mind. The Signature APIs let your organization protect the security and privacy of Adobe PDF documents that it distributes and receives. This service uses digital signatures and certification to ensure that only intended recipients can alter documents. 

     You can write to `aem-forms-early-adopter-program@adobe.com` from your official email id to join the early adopter program and request access to the capability.
     
## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes/current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
