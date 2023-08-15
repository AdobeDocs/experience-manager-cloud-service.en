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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2023.8.0) is August 31, 2023. The next feature release (2023.9.0) is planned for September 28, 2023.

## Release Video {#release-video}

Have a look at the August 2023 Release Overview video for a summary of the features added in the 2023.8.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3422016/?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features in [!DNL Experience Manager Sites] {#sites-features}

* The [Content Fragment Console](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/content-fragments-console.html?lang=en) now allows users to view tags and search by tags applied as metadata to Content Fragments. Users will no longer have to switch to the Assets UI for this capability, reducing context switching and improving efficiency. 

     ![Tagging in Content Fragment Console](/help/assets/content-fragments-console-tags.png)
* The new Content Fragment Editor is now available on AEM as a Cloud Service. It empowers content authors to be more productive by streamlining their authoring tasks and reducing the need to switch between different apps while editing content. 
     ![New Content Fragment Editor](/help/release-notes/assets/newCFEditor.png)

The new Content Fragment editor provides the following benefits that are not available in the original editor:
* Auto-saving for improved authoring efficiency and to prevent accidental loss of edits.
* Hierarchical view of a Content Fragment and its references using the Structure tree for quick navigation within a deeply structured fragment.
     ![Structure Tree in Content Fragment Editor](/help/release-notes/assets/newCFEditor_StructureTree.png)

* In-line uploading of assets as content references without having to upload it to the Asset DAM first
* Ad-hoc preview of the rendered experience delivered by the content fragment to help authors to visualize the look and feel of the content on the frontend app
* 1-click publishing and unpublishing of the content fragment from the editor
* Viewing and navigating to language copies while editing a content fragment
     ![Language Copies in Content Fragment Editor](/help/release-notes/assets/newCFEditor_LanguageCopies.PNG)

* Viewing versions to help keep track of the timeline of a content fragment

     ![Versions in Content Fragment Editor](/help/release-notes/assets/newCFEditor_Versionhistory.PNG)

* Viewing parent references to help authors understand the impact of their edits

     ![Parent References in Content Fragment Editor](/help/release-notes/assets/newCFEditor_Parentreferences.PNG)

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in Assets view {#assets-view-features}

<!--

**Assign metadata form to a folder**

You can now assign metadata form to a specific folder within your Assets Essentials deployment. All assets in the folder, including assets in the sub-folders, then display properties defined in the assigned metadata form.

![assign metadata form to a folder](/help/release-notes/assets/assign-to-folder.png)

-->

**Improved artificial intelligence framework for image Smart Tags**

Experience Manager Assets now uses an improved artificial intelligence framework for image Smart Tags. This content intelligence results in better relevancy and precision of Smart Tags available to all image assets on ingestion.

**Configure display of columns for Assets List view**

Assets Essentials now provides the ability to select the columns that display in the Assets List view, such as Status, Format, Dimensions, Size, and so on.

![Configure columns](/help/release-notes/assets/configure-columns.png)

**Sort search results based on relevance**

Assets Essentials now sorts the search results based on Relevance, by default. You can sort the searched assets in increasing or decreasing order of `Name`, `Relevance`, `Size`, `Modified`, and `Created`.


## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features available in [!DNL Forms] {#new-features-available-in-forms-channel}

* [**Out of the box themes**](/help/forms/using-themes-in-core-components.md) **and templates**: Kickstart your form creation process with our ready-to-use OOTB themes and templates, tailored to empower both seasoned professionals and new forms authors. Seamlessly built using Adaptive Forms Core Components, these meticulously curated themes and templates allow you to start creating forms swiftly for common use cases. 

     ![Out of the box templates](/help/forms/assets/form-templates-ootb.png)

* **React Components for Headless Forms**: You can now preview and customize   Headless Adaptive Form renditions with the React components provided out of the box. These components leverage BEM classes from Adaptive Forms Core Components for styling, making it effortless for you to customize their appearance according to your specific requirements.

* [**Create Adaptive Forms with repeatable sections**](/help/forms/create-forms-repeatable-sections.md): You can now make [Accordion](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/accordion.html), [Wizard](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/wizard.html), [Panel](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel-container.html), and [Horizontal Tabs](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/horizontal-tabs.html) components based Adaptive Form repeatable for multiple data record capture.  These repeatable sections allow you to provide multiple data entries easily. It is useful when the required instances of data are unknown in advance. A form filler can easily add or remove sections, making forms adaptable to different data entry scenarios and simplifying collection of multiple occurrences of the same data record.


### Pre-release features available in [!DNL Forms] {#pre-release-features-available-in-forms-channel}

* [**Google reCAPTCHA enterprise support**](/help/forms/captcha-adaptive-forms.md): Use Google reCAPTCHA Enterprise in an Adaptive Form to provide enhanced protection against fraudulent activity and spam, providing a safer user experience. With advanced risk analysis and seamless integration, genuine users can easily submit forms while bots are effectively blocked.

    >[!VIDEO](https://video.tv.adobe.com/v/3422097/adaptive-forms-recaptcha-core-components-captcha/?quality=12&learn=on)

### Headless Adaptive Forms early adopter program {#forms-early-adopter}

Use [Headless Adaptive Forms](https://experienceleague.adobe.com/docs/experience-manager-headless-adaptive-forms/using/overview.html) to enable your developers to create, publish, and manage interactive forms that can be accessed and interacted with through APIs, rather than through a traditional graphical user interface. Headless adaptive forms help you: 

* build high-quality multi-channel forms in the programming language of your choice 
* natively integrate forms to your desktop and mobile apps, websites, and chat applications 
* reuse your proprietary UI components with forms applications 
* use the power of Adobe Experience Manager Forms 

You can send an email to `aem-forms-headless@adobe.com` from your official email ID to join the early adopter program. 

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### Actions Center {#actions-center}

Subscribe to email notifications that alert you when critical incidents happen requiring immediate action, and also with personalized recommendations to optimize your site. [Actions Center](/help/operations/actions-center.md) serves as a hub where you can review these alerts, such as blocked replication queues or expiring credentials, and mark them as resolved.

![Actions Center screenshot](/help/assets/assets/actions-center.png)

### CDN and WAF Rules early adopter program {#waf-early-adopter}

Filter traffic at the CDN based on:
* request headers and properties (e.g., IP address)
* traffic patterns known to be associated with malicious traffic

Interested in trying out the feature and sharing feedback? Send an email to **aemcs-waf-adopter@adobe.com** from your official email ID to learn more about the early adopter program. Space is limited.

Learn more about the feature in the article [here](/help/security/cdn-and-waf-rules.md).

### Other Foundation changes {#other-foundation-changes}

* During the week of August 7th, AEM will return error code 429 instead of error code 503 when requests to AEM instances exceed a healthy level. [Learn more](/help/implementing/developing/introduction/development-guidelines.md).

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes/current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
