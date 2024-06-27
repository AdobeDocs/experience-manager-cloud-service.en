---
title: Release Notes for 2023.7.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2023.7.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: 7866d94c-e54c-4bb2-aaa6-66c019e46336
feature: Release Information
role: Admin
---
# 2023.7.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2023.7.0 version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions such as 2021 or 2022.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2023.7.0) is July 27, 2023. The next feature release (2023.8.0) is planned for August 31, 2023.

## Release Video {#release-video}

Have a look at the July 2023 Release Overview video for a summary of the features added in the 2023.7.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3422016/?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features in [!DNL Experience Manager Sites] {#sites-features}

* MSM for Content Fragments. AEM Multisite Manager is now available for Content Fragments, allowing to create Content Fragment Live Copies for bulk content distribution. Granular inheritance controls are available down to Content Fragment Element and Variation level. 

### New features in [!DNL Experience Manager Sites] prerelease {#prerelease-sites}

* The [Content Fragment Console](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/content-fragments-console.html) now allows users to view tags and search by tags applied as metadata to Content Fragments. Users will no longer have to switch to the Assets UI for this capability, reducing context switching and improving efficiency. 

![Tagging in Content Fragment Console](/help/assets/content-fragments-console-tags.png)

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

* **[React Components for Headless Forms](https://github.com/adobe/aem-forms-headless-components/tree/main/packages/react-vanilla-components)**: You can now preview and customize   Headless Adaptive Form renditions with the React components provided out of the box. These components use BEM classes from Adaptive Forms Core Components for styling, making it effortless for you to customize their appearance according to your specific requirements.

* [**Create Adaptive Forms with repeatable sections**](/help/forms/create-forms-repeatable-sections.md): You can now make [Accordion](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/accordion.html), [Wizard](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/wizard.html), [Panel](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel), and [Horizontal Tabs](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/horizontal-tabs.html) components based Adaptive Form repeatable for multiple data record capture.  These repeatable sections allow you to provide multiple data entries easily. It is useful when the required instances of data are unknown in advance. A form filler can easily add or remove sections, making forms adaptable to different data entry scenarios and simplifying collection of multiple occurrences of the same data record.


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
* request headers and properties (for example, IP address)
* traffic patterns known to be associated with malicious traffic

Interested in trying out the feature and sharing feedback? Send an email to **aemcs-waf-adopter@adobe.com** from your official email ID to learn more about the early adopter program. Space is limited.

Learn more about the feature in the article [here](/help/security/traffic-filter-rules-including-waf.md).

### Other Foundation changes {#other-foundation-changes}

* During the week of August 7th, AEM will return error code 429 instead of error code 503 when requests to AEM instances exceed a healthy level. [Learn more](/help/implementing/developing/introduction/development-guidelines.md).

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes/current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
