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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2024.1.0) is January 25, 2024. The next feature release (2024.2.0) is planned for February 29, 2024.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

<!-- 

## Release Video {#release-video}

Have a look at the December 2023 Release Overview video for a summary of the features added in the 2023.12.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3425864?quality=12)

-->

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### Extension Manager in AEM Sites {#sites-extension-manager}

**Explore the new [Extension Manager in AEM Sites](https://developer.adobe.com/uix/docs/extension-manager/)** to personalize your AEM setup by configuring UI extensions.

![Extension Manager in AEM Sites](/help/assets/sites/extension-manager/homepage.png)

The Extension Manager in AEM Sites enables developers and practitioners to access, manage, and customize UI extensions built to enhance the functionality of AEM Sites.
With the Extension Manager, you can:

* Enable or disable extensions on a per-instance basis;
* Configure extension parameters;
* Preview extensions and generate a shareable preview link;
* Discover UI extensibility features via interactive demos;
* Access Adobe's experimental features through first-party extensions.

We are actively seeking feedback and new use cases for UI extensions. If you would like to connect, please send an email to `uix@adobe.com`.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### Admin view prerelease features {#admin-view-prerelease}

**Preview renditions for all supported video types**

Experience Manager Assets now generates preview renditions of all supported video types by default without requiring a processing profile configuration

### Assets view {#assets-view-features}

**Smart tags blocklist** 

Assets Essentials now enables you to define blocklist that comprises words that should not be added as Smart Tags to assets when they are uploaded to the repository. This capability helps you to maintain brand compliance and reduces effort to moderate Smart Tags.

  ![Smart Tags blocklist](/help/assets/assets/block-tags.png)


## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

<!-- 

* **Configure a shard for Adobe Sign for AEM Forms**: Adobe distributes Acrobat Sign API around the globe in many deployment units called "shards." Each shard serves a customer's account, such as NA1, NA2, NA3, EU1, JP1, AU1, IN1, and others. The shard names correspond to geographic locations. You can now use more than one shard while using Adobe Sign integration with AEM Forms. 

--> 

### Early Adopter Program {#forms-early-adopter}

* **[Submit an Adaptive Form to Adobe Workfront Fusion Scenario](/help/forms/submit-adaptive-form-to-workfront-fusion.md)**: Forms as a Cloud Service offers an out-of-the-box options to effortlessly connect an Adaptive Form with Adobe Workfront. This simplifies the process of submitting an Adaptive Form to an Adobe Workfront scenario, allowing you trigger a Workfront Fusion scenario on submission of an Adaptive Form. 

* **[Right to left languages support](/help/forms/supporting-new-language-localization-core-components.md)**: Adaptive Forms built on Core Components can now be presented in a Right-to-Left (RTL) language like Arabic, Persian, and Urdu. The RTL languages are spoken by over 2 billion people globally. Using a form in RTL language allows you to extend the reach of your adaptive forms to cater to these diverse audiences and select into RTL markets. In certain regions, it's also a legal mandate to provide forms in the local language. By accommodating local languages, you not only open doors to a broader audience but also ensure compliance with relevant laws and regulations. 

  ![Right to left language support](/help/forms/assets/right-to-left-language-support.png)

* **[Protect your documents with DocAssurance APIs (Part of Communication APIs)](/help/forms/aem-forms-cloud-service-communications-introduction.md#document-assurance-doc-assurance)**: The DocAssurance APIs empower you to safeguard sensitive information by signing and encrypting the documents. Through encryption, the contents of a document are transformed into an unreadable format, ensuring that only authorized users can gain access. This fortified layer of protection not only shields valuable data from unauthorized eyes but also provides peace of mind. The Signature APIs let your organization protect the security and privacy of Adobe PDF documents that it distributes and receives. This service uses digital signatures and certification to ensure that only intended recipients can alter documents. 

     You can write to `aem-forms-early-adopter-program@adobe.com` from your official email id to join the early adopter program and request access to the capability.
     
## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### Support for Dynatrace {#dynatrace}

Dynatrace customers may monitor their AEM usage. [Read how](/help/implementing/cloud-manager/dynatrace.md) to request connectivity with your Dynatrace environment for application performance monitoring.

### RDE Support for Front-End Code using Site Themes and Site Templates: Early Adopter Program {#rde-frontend-early-adopter}

[Rapid Development Environments (RDEs)](/help/implementing/developing/introduction/rapid-development-environments.md) now support front-end code based on [site themes](/help/sites-cloud/administering/site-creation/site-themes.md) and [site templates](/help/sites-cloud/administering/site-creation/site-templates.md), for early adopters. With RDEs, this is done using a command line directive, rather than a [front-end pipeline](/help/sites-cloud/administering/site-creation/enable-front-end-pipeline.md). Please reach out to **aemcs-rde-support@adobe.com** to try it out and provide feedback.

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes/current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
