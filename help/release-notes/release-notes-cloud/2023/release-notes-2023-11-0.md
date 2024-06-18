---
title: Release Notes for 2023.11.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2023.11.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: 19cff082-80aa-445c-9462-5e319b7fe0e9
feature: Release Information
role: Admin
---
# 2023.11.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2023.11.0 version of [!DNL Experience Manager] as a Cloud Service.

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

>[!VIDEO](https://video.tv.adobe.com/v/3425864?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### Early Adopter Program {#sites-early-adopter}

**[Find and Replace strings in Content Fragments](/help/sites-cloud/administering/content-fragments/managing.md#find-and-replace-find-and-replace)**: The Content Fragment Console provides users with an easy and intuitive way to replace a string appearing in multiple content fragments at once to help accelerate content velocity.

![Find and Replace](/help/sites-cloud/administering/content-fragments/assets/cf-managing-find-replace.png)

Interested in trying out the feature and sharing feedback? Send an email to **aemcs-headless-adopter@adobe.com** from your official email ID to learn more about the early adopter program. 

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New Features in Assets View {#assets-view-features}

* **Embedded Adobe Express editor in AEM Assets**: Users with access to Express now have integrated image editing and creation tools from Adobe Express and Adobe Firefly available directly within AEM Assets to improve content reuse and accelerate content velocity.

  ![assign metadata form to a folder](/help/assets/assets/adobe-express-aem-assets.png)

<!--

* **Smart tags blocklist**: Experience Manager Assets now enables you to define a list of blocked tags. These tags are automatically removed from the auto-generated smart tags when you upload assets to the repository. This capability performs tags governance and saves a lot of time as you can add a tag to the block list and AEM Assets automatically excludes it from the list of tags for any of the assets that are added to the repository.

  ![storage usage insights](/help/assets/assets/block-tags.png)

-->


* **Storage usage reports in Insights**: Administrators now have the ability to view the storage usage reports available as part of Insights.

  ![storage usage insights](/help/assets/assets/storage-usage-insights.png)

* **Search first homepage configuration**: Experience Manager Assets now enables you to configure the homepage experience for your organization. If you select search first as the homepage, you can configure the search bar alignment, background image, and logo for your organization.

  ![search first configuration](/help/assets/assets/search-first-configuration.png)

### New Features in  Prerelease for Admin View {#admin-view-features-prerelease}

**Video Preview**: AEM Assets now generates preview renditions of all supported video formats by default, without the need to configure a processing profile.

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New Features in [!DNL Experience Manager Forms] {#forms-features}

* **[Checkbox component](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/checkbox.html)**: Adaptive Forms based on Core Components can now include a checkbox component. It allows users to make binary choices, selecting or deselecting a particular option. It typically appears as a small box that can be clicked or tapped to toggle between two states: checked and unchecked. The checkbox is a common form element used to present a yes/no or true/false choice. 

* **[Terms and Conditions component](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/terms-and-conditions.html)**: Adaptive Forms based on Core Components can now include a Terms and Conditions component. It allows forms authors to introduce a specific section within the form where users are presented with the terms, conditions, or legal agreements associated with the use of a service, product, or platform. This component is designed to inform users about the rules, regulations, and obligations they are agreeing to by submitting the form. 

  ![Checkbox, Terms and Conditions, and Vertical tab components](/help/forms/assets/forms-components.png)

* **[Vertical tabs component](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/vertical-tabs.html)**: Adaptive Forms based on Core Components can now organize form content into a vertical list of tabs, providing a structured and navigable layout. The use of vertical tabs in a form can enhance the overall user experience by simplifying navigation and improving the organization of form content, especially in situations where a form contains multiple sections or complex information. 



### New Features in [!DNL Forms] Prerelease {#prerelease-features-forms}

* **[Connect an Adaptive Forms with Microsoft&reg; SharePoint List](/help/forms/configure-submit-actions-core-components.md#submit-to-sharepoint)**: AEM Forms provides an OOTB integration to submit forms data directly to SharePoint List, enabling you to leverage SharePoint's Lists capabilities. You can configure Microsoft SharePoint List as a datasource for a Form Data Model and use the **Submit using Form Data Model** submit action to connect an Adaptive Form with SharePoint List. 

<!-- 

* **Configure a shard for Adobe Sign for AEM Forms**: Adobe distributes Acrobat Sign API around the globe in many deployment units called "shards." Each shard serves a customer's account, such as NA1, NA2, NA3, EU1, JP1, AU1, IN1, and others. The shard names correspond to geographic locations. You can now use more than one shard while using Adobe Sign integration with AEM Forms. 

--> 

### Early Adopter Program {#forms-early-adopter}

* **Submit an Adaptive Form to Adobe Workfront Fusion Scenario**: Forms as a Cloud Service offers an out-of-the-box options to effortlessly connect an Adaptive Form with Adobe Workfront. This simplifies the process of submitting an Adaptive Form to an Adobe Workfront scenario, allowing you trigger a Workfront Fusion scenario on submission of an Adaptive Form. 

* **Right to left languages support**: Adaptive Forms built on Core Components can now be presented in a Right-to-Left (RTL) language like Arabic, Persian, and Urdu. The RTL languages are spoken by over 2 billion people globally. Using a form in RTL language allows you to extend the reach of your adaptive forms to cater to these diverse audiences and tap into RTL markets. In certain regions, it's also a legal mandate to provide forms in the local language. By accommodating local languages, you not only open doors to a broader audience but also ensure compliance with relevant laws and regulations. 

  ![Right to left language support](/help/forms/assets/right-to-left-language-support.png)

* **[Protect your documents with DocAssurance APIs (Part of Communication APIs)](/help/forms/aem-forms-cloud-service-communications-introduction.md#document-assurance-doc-assurance)**: The DocAssurance APIs empower you to safeguard sensitive information by signing and encrypting the documents. Through encryption, the contents of a document are transformed into an unreadable format, ensuring that only authorized users can gain access. This fortified layer of protection not only shields valuable data from unauthorized eyes but also provides peace of mind. The Signature APIs let your organization protect the security and privacy of Adobe PDF documents that it distributes and receives. This service uses digital signatures and certification to ensure that only intended recipients can alter documents. 

     You can write to `aem-forms-ea@adobe.com` from your official email id to join the early adopter program and request access to the capability.
     
## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### WAF Traffic Filter Rules Can Now Be Licensed {#cdn-waf-license}

Traffic Filter Rules were released in October, and included a note that the special category of Web Application Firewall (WAF) rules would be available later this year to supplement the rules already available to Sites and Forms customers. As an update, the WAF-DDoS Protection offering can now be licensed.

Once licensed, these advanced WAF rules can be deployed to the CDN using the Cloud Manager Configuration Pipeline to add an extra layer of protection against web attacks. 
 
Read about [Traffic Filter Rules](/help/security/traffic-filter-rules-including-waf.md), including WAF. Speak to your AEM account team about licensing WAF-DDoS Protection or Enhanced Security.

### CDN Configuration Early Adopter Program {#cdn-config-early-adopter}

In addition to the recently released [Traffic Filter Rules (including WAF)](/help/security/traffic-filter-rules-including-waf.md), there's an opportunity to use the Configuration Pipeline to declare and deploy other types of CDN configuration. We'd love to hear about your use cases, including:
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

## Known Issues {#known-issues}

* Unable to submit Adaptive Forms based on Core Components. The issue occurs for Adaptive Forms built using Core Components versions 2.0.38 – 2.0.60. 

  To resolve the issue. you can move to Adaptive Form Core Components version 2.0.62 or later. To set a version of Adaptive Forms Core Components for your environment, [set versions of the core.forms.components.version, core.forms.components.af.version, and core.wcm.components.version component](/help/forms/enable-adaptive-forms-core-components.md#2-add-adaptive-forms-core-components-dependencies-to-your-git-repository) dependencies in your Forms as a Cloud Service repository or AEM Archetype based project and [deploy the changes to your Forms as a Cloud Service environment](/help/forms/enable-adaptive-forms-core-components.md#build-and-deploy-updated-code-on-an-aem-forms-as-a-cloud-service-environment). You can find the latest version of Adaptive Forms Core Components dependencies at [Adaptive Forms Core Components Git repository](https://github.com/adobe/aem-core-forms-components#system-requirements).
