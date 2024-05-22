---
title: Release Notes for 2023.10.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2023.10.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: 81a6cbd2-7101-429b-8572-2650c5bea963
---
# 2023.10.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2023.10.0 version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions such as 2021 or 2022.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2023.10.0) is October 26, 2023. The next feature release (2023.11.0) is planned for November 30, 2023.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Release Video {#release-video}

Have a look at the October 2023 Release Overview video for a summary of the features added in the 2023.10.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3425186/?quality=12)

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features {#assets-features}

**AEM Assets add-on for Adobe Express**: Experience Manager Assets now provides an add-on for Adobe Express. The add-on allows you to directly access the assets stored in Experience Manager Assets from within the Adobe Express user interface. You can place content managed in AEM Assets in the Express canvas and then save new or edited content in an AEM Assets repository. The add-on provides the following key benefits:

* Increased content reuse by editing and saving new assets in AEM

* Reduced overall time and effort  to create new assets or create new versions of existing assets

  ![Include assets from Assets add-on](/help/assets/assets/aem-assets-add-on-include-assets.png)

### New features in Assets view {#assets-view-features}

* **Bulk import assets from OneDrive data source**: Administrators now have the ability to [import large number of assets from OneDrive to AEM Assets](/help/assets/bulk-import-assets-view.md#onedrive-developer-application). The updated list for the supported data sources for bulk import include Azure, AWS, Google Cloud, Dropbox, and OneDrive. 

  ![assign metadata form to a folder](/help/assets/assets/bulk-import-source-details-onedrive.png)

* **Cross-Org Entitlement Support for Libraries**: Experience Manager Assets now enables you to configure access to Creative Cloud libraries in a different IMS Organization. It allows easier access to the latest cross-product workflows between Creative Cloud and Experience Manager and reduces time and effort for creatives.

### Pre-release features available in [!DNL Experience Manager Assets] {#prerelease-features-assets}

* **Dynamic Media**: [Multi-caption and multi-audio track support for videos in Dynamic Media](/help/assets/dynamic-media/video.md#about-msma)&mdash;You can now easily add multiple captions and multiple audio tracks to a primary video. This capability means that your videos are accessible across a global audience. You can customize a single, published primary video to a global audience in multiple languages and adhere with accessibility guidelines for different geographical regions. Authors can also manage the captions and audio tracks from a single tab in the user interface.

  ![Captions and Audio tracks tab on the Properties page of a selected video asset.](/help/release-notes/assets/msma-aem-cs.png)*Captions and Audio tracks tab on the Properties page of a selected video asset.*

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features in [!DNL Experience Manager Forms] {#forms-features}

* **[Custom properties for Adaptive Forms](/help/forms/template-editor-core-components.md#add-a-custom-group-name-in-the-policy-of-template-editor)**: You can associate custom attributes (key-value pairs) with a form template or adaptive forms component to allow forms developers to deliver dynamic form behaviors that adapts based on the values of these custom attributes. For example, developers can craft different renditions of a Headless Forms component on mobile, desktop, or web platforms, based on the values of custom attributes, thereby significantly enhancing the user experience across a wide array of devices.

* **Themes and templates**: Kickstart your form creation process with our new themes and templates, tailored to empower both seasoned professionals and new forms authors. Seamlessly built using Adaptive Forms Core Components, these meticulously curated themes and templates allow you to start creating forms swiftly for common use cases.

     ![Out of the box templates](/help/forms/assets/form-templates-ootb.png)


### Early adopter program {#forms-early-adopter}

* **[Protect your documents with DocAssurance APIs (Part of Communication APIs)](/help/forms/aem-forms-cloud-service-communications-introduction.md#document-assurance-doc-assurance)**: The DocAssurance APIs empower you to safeguard sensitive information by signing and encrypting the documents. Through encryption, the contents of a document are transformed into an unreadable format, ensuring that only authorized users can gain access. This fortified layer of protection not only shields valuable data from unauthorized eyes but also provides peace of mind. The Signature APIs let your organization protect the security and privacy of Adobe PDF documents that it distributes and receives. This service uses digital signatures and certification to ensure that only intended recipients can alter documents. 

     You can write to `aem-forms-ea@adobe.com` from your official email id to join the early adopter program and request access to the capability.
     
## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### Traffic Filter Rules, including WAF {#traffic-filter-rules-waf}

[Filter traffic at the Adobe Managed CDN](/help/security/traffic-filter-rules-including-waf.md) by declaring rules matching website traffic by properties including url, IP address, and user agent -- or set custom traffic rate limits to guard against DoS attacks. Customers may also license a set of advanced Web Application Firewall (WAF) rules for extra protection against sophisticated website threats. 

We encourage you to get familar with traffic filter rules by [trying out a tutorial](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/security/traffic-filter-and-waf-rules/overview.html)! It walks you through setting up a new Cloud Manager Configuration Pipeline, declaring rules in a configuration file, and analyzing CDN logs for malicious traffic.

Traffic filter rules are available now on dev environments, with a gradual rollout to stage and prod environments in November. You may request earlier access on stage and prod by emailing **aemcs-waf-adopter@adobe.com**. 

The advanced WAF traffic filter rules can be licensed later this year through the Enhanced Security or WAF-DDoS Protection offerings.

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes/current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
