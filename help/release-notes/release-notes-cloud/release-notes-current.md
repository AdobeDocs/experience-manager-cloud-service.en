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

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2024.2.0) is February 29, 2024. The next feature release (2024.3.0) is planned for March 28, 2024.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Release Video {#release-video}

Have a look at the February 2024 Release Overview video for a summary of the features added in the 2024.2.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3425864?quality=12)

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

* **[You can leverage the Real User Monitoring (RUM) Data Service](/help/implementing/cloud-manager/content-requests.md#real-user-monitoring-for-aem-as-a-cloud-service)** to enable client-side collection for AEM as a Cloud Service.
Real User Monitoring (RUM) Data Service offers a more precise reflection of user interactions, ensuring a reliable measure of website engagement. It is a great opportunity to gain advanced insights into your page performance. While this is beneficial for customers who use either Adobe-managed CDN or non-Adobe-managed CDN. Additionally, for customers using a non-Adobe managed CDN, automated traffic reporting can now be enabled for them, thus removing the need to share any traffic report with Adobe.

   If you are interested in testing this new feature and sharing your feedback, please send an email to `aemcs-rum-adopter@adobe.com`, along with your domain name for each of the environments that you would like to enable RUM for from your email address associated with your Adobe ID. Adobe's product team will then enable the Real User Monitoring (RUM) Data Service for you.
     
## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes/current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
