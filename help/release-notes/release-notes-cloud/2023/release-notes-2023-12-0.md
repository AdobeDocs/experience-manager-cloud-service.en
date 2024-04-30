---
title: Release Notes for 2023.12.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2023.12.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: b36add58-a2ba-4299-94be-e0026e9c553c
---
# 2023.12.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2023.12.0 version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions such as 2021 or 2022.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2023.12.0) is December 14, 2023. The next feature release (2024.1.0) is planned for January 25, 2023.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

<!-- 

## Release Video {#release-video}

Have a look at the December 2023 Release Overview video for a summary of the features added in the 2023.12.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3425864?quality=12)

-->

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### Early Adopter Program {#sites-early-adopter}

**You can leverage the [Real User Monitoring (RUM) Data Service](/help/implementing/cloud-manager/content-requests.md#real-user-monitoring-for-aem-as-a-cloud-service)** to enable client-side collection for AEM as a Cloud Service. 

Real User Monitoring (RUM) Data Service offers a more precise reflection of user interactions, ensuring a reliable measure of website engagement. It is a great opportunity to gain advanced insights into your page performance. While this is beneficial for customers who use either Adobe-managed CDN or non-Adobe-managed CDN. Additionally, for customers using a non-Adobe managed CDN, automated traffic reporting can now be enabled for them, thus removing the need to share any traffic report with Adobe.

If you are interested in testing this new feature and sharing your feedback, please send an email to `aemcs-rum-adopter@adobe.com`, along with your domain name for the production, stage and dev environment from your email address associated with your Adobe ID. Adobe's product team will then enable the Real User Monitoring (RUM) Data Service for you.


## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New Features in Assets View {#assets-view-features}

**Create GenAI images with Adobe Firefly**

Create new images based on search queries with an integration of Adobe Firefly text-to-image feature (requires Adobe Firefly license).

 ![Assets Firefly integration](/help/assets/assets/assets-firefly-integration.png)

**Find Similar Images**

You can now can easily find content by selecting an image and viewing similar images in the Experience Manager Assets repository.

<!--

* **Smart tags blocklist**: Experience Manager Assets now enables you to define a list of blocked tags. These tags are automatically removed from the auto-generated smart tags when you upload assets to the repository. This capability performs tags governance and saves a lot of time as you can add a tag to the block list and AEM Assets automatically excludes it from the list of tags for any of the assets that are added to the repository.

  ![storage usage insights](/help/assets/assets/block-tags.png)


**Video Preview**: AEM Assets now generates preview renditions of all supported video formats by default, without the need to configure a processing profile.

-->

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New Features in [!DNL Experience Manager Forms] {#forms-features}

* **[Connect an Adaptive Forms with Microsoft&reg; SharePoint List](/help/forms/configure-submit-actions-core-components.md#submit-to-sharepoint)**: AEM Forms provides an OOTB integration to submit forms data directly to SharePoint List, letting you use SharePoint's Lists capabilities. You can configure Microsoft SharePoint List as a datasource for a Form Data Model and use the **Submit using Form Data Model** submit action to connect an Adaptive Form with SharePoint List. 

<!-- 

* **Configure a shard for Adobe Sign for AEM Forms**: Adobe distributes Acrobat Sign API around the globe in many deployment units called "shards." Each shard serves a customer's account, such as NA1, NA2, NA3, EU1, JP1, AU1, IN1, and others. The shard names correspond to geographic locations. You can now use more than one shard while using Adobe Sign integration with AEM Forms. 

--> 

### Early Adopter Program {#forms-early-adopter}

* **[Submit an Adaptive Form to Adobe Workfront Fusion Scenario](/help/forms/submit-adaptive-form-to-workfront-fusion.md)**: Forms as a Cloud Service offers an out-of-the-box options to effortlessly connect an Adaptive Form with Adobe Workfront. This simplifies the process of submitting an Adaptive Form to an Adobe Workfront scenario, allowing you trigger a Workfront Fusion scenario on submission of an Adaptive Form. 

* **[Right to left languages support](/help/forms/supporting-new-language-localization-core-components.md)**: Adaptive Forms built on Core Components can now be presented in a Right-to-Left (RTL) language like Arabic, Persian, and Urdu. The RTL languages are spoken by over 2 billion people globally. Using a form in RTL language allows you to extend the reach of your adaptive forms to cater to these diverse audiences and select into RTL markets. In certain regions, it's also a legal mandate to provide forms in the local language. By accommodating local languages, you not only open doors to a broader audience but also ensure compliance with relevant laws and regulations. 

  ![Right to left language support](/help/forms/assets/right-to-left-language-support.png)

* **[Protect your documents with DocAssurance APIs (Part of Communication APIs)](/help/forms/aem-forms-cloud-service-communications-introduction.md#document-assurance-doc-assurance)**: The DocAssurance APIs empower you to safeguard sensitive information by signing and encrypting the documents. Through encryption, the contents of a document are transformed into an unreadable format, ensuring that only authorized users can gain access. This fortified layer of protection not only shields valuable data from unauthorized eyes but also provides peace of mind. The Signature APIs let your organization protect the security and privacy of Adobe PDF documents that it distributes and receives. This service uses digital signatures and certification to ensure that only intended recipients can alter documents. 

     You can write to `aem-forms-ea@adobe.com` from your official email id to join the early adopter program and request access to the capability.
     
## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### CDN Configuration Early Adopter Program {#cdn-config-early-adopter}

In addition to the recently released [Traffic Filter Rules](/help/security/traffic-filter-rules-including-waf.md), which includes the optionally licensable Web Application Firewall (WAF) rules, there's an opportunity to use the Configuration Pipeline to declare and deploy other types of CDN configuration. We'd love to hear about your use cases, including:
* 301/302 client-side redirects
* proxying requests at the edge to arbitrary origins
* URL transformations
* setting or modifying request or response headers
* custom error pages when the CDN can't reach AEM
* authentication by username/password
* any other useful CDN configurations

Send an email to **aemcs-cdn-config-adopter@adobe.com** from your official email ID with your feedback.

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes/current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
