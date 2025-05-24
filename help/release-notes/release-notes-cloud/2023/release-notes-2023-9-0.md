---
title: Release Notes for 2023.9.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2023.9.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: d747f58b-8d6c-418d-9d2b-ec3ae4b6dc03
feature: Release Information
role: Admin
---

# 2023.9.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2023.9.0 version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions such as 2021 or 2022.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2023.9.0) is September 28, 2023. The next feature release (2023.10.0) is planned for October 26, 2023.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Release Video {#release-video}

Have a look at the September 2023 Release Overview video for a summary of the features added in the 2023.9.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3424826/?quality=12)

## AEM Edge Delivery Services {#edge-delivery}

Edge Delivery is a new set of composable services focused on maximizing the impact of content to drive measurable business outcomes at the point of customer interaction.

Learn more about Edge Delivery Services in the article [here](/help/edge/overview.md).

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in Assets view {#assets-view-features}

**Assign metadata form to a folder**

You can now assign metadata form to a specific folder within your deployment. All assets in the folder, including assets in the sub-folders, then display properties defined in the assigned metadata form.

![assign metadata form to a folder](/help/release-notes/assets/assign-to-folder.png)

### New features in Admin view {#admin-view-features}

* **Integrate AEM Assets as a Cloud Service with Document-based Authoring  for Edge Delivery Services**: Integrate AEM Assets with Document-based Authoring  for Edge Delivery Services to enable website authors to [use images available in AEM Assets repositories while authoring documents in Microsoft Word or Google Docs](/help/edge/using.md#integrate-assets-edge).

* **Extract ZIP archives**: Ability to select ZIP archives that are managed in Experience Manager and [extracting the files directly into Experience Manager](/help/assets/manage-digital-assets.md#extract-zip-archives) without downloading them.

  ![Pin items for groups](/help/release-notes/assets/extract-archive.png)

### Pre-release features available in [!DNL Experience Manager Assets] {#prerelease-features-assets}

* **Dynamic Media**: [Multi-caption and multi-audio track support for videos in Dynamic Media](/help/assets/dynamic-media/video.md#about-msma)&mdash;You can now easily add multiple captions and multiple audio tracks to a primary video. This capability means that your videos are accessible across a global audience. You can customize a single, published primary video to a global audience in multiple languages and adhere with accessibility guidelines for different geographical regions. Authors can also manage the captions and audio tracks from a single tab in the user interface.

  ![Captions and Audio tracks tab on the Properties page of a selected video asset.](/help/release-notes/assets/msma-aem-cs.png)*Captions and Audio tracks tab on the Properties page of a selected video asset.*

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features in [!DNL Experience Manager Forms] {#forms-features}

* [**Google reCAPTCHA enterprise support**](/help/forms/captcha-adaptive-forms-core-components.md): Use Google reCAPTCHA Enterprise in an Adaptive Form to provide enhanced protection against fraudulent activity and spam, providing a safer user experience. With advanced risk analysis and seamless integration, genuine users can easily submit forms while bots are effectively blocked.

* [**Adobe Analytics with Experience Cloud Setup Automation for Forms**](/help/forms/enable-adobe-analytics-adaptive-form-using-experience-cloud-setup-automation.md): You can now enable Adobe Analytics with Experience Cloud Setup Automation with a flip of couple of buttons. It enables you to connect AEM Forms as a Cloud Service with Experience Platform tags and Adobe Analytics to capture and track performance metrics for your published forms.

     >[!VIDEO](https://video.tv.adobe.com/v/3424577/enable-adobe-analytics/?quality=12&learn=on)

* [**Adobe Analytics report template for Adaptive Forms**](/help/forms/view-understand-aem-forms-analytics-reports.md): Forms as a Cloud Service now provides an Adobe Analytics report OOTB. It helps you easily understand performance of your forms. The form-level metrics provide you an insight into how the form is performing on multiple key performance indicators (KPIs) like, renditions, visitors, submissions, Average fill time. By tracking user behavior and feedback, you can identify areas of the form that are causing confusion and guide improvements to the form's design and functionality.

     ![Adaptive form user engagement adobe analytics report](/help/forms/assets/forms-analytics-report.png)

* **[Form Fragment in Adaptive Forms based on Core Components](/help/forms/adaptive-form-fragments-core-components.md)**: Say goodbye to duplication, optimize your digital inventory, and improve collaboration as you elevate your form-building experience with Form Fragments. These reusable components seamlessly integrate into multiple forms, streamlining the creation of consistent and professional-looking forms. Form Fragments ensure reusability, standardization, and brand consistency through 'change once and reflect everywhere' functionality. Experience greater maintainability and efficiency as updates made in one place are automatically propagated across all forms that utilize these fragments.

* **[Enhanced Adobe Sign Workflow step](/help/forms/aem-forms-workflow-step-reference.md#sign-document-step-sign-document-step)**: The Adobe Sign Workflow step is enhanced to include the following:
     * **Government ID-Based Authentication for Adobe Sign**: Adobe Acrobat Sign's Government ID-Based Authentication offers an additional layer of verification by enabling users to authenticate their identity using government-issued IDs (driver's license, national ID, passport). By using trusted identification documents, this enhancement adds an extra level of confidence to the signing process, making it ideal for scenarios that require heightened security, compliance, and user validation. 

     * **Audit Trail for Adobe Sign Documents**:  Use the Audit Trail feature for detailed insights into the lifecycle of your Adobe Sign documents. With the Audit Trail, you can now maintain a comprehensive record of all actions and interactions related to your documents. This includes details such as who viewed, edited, or signed the document, along with timestamps for each event. This enhancement is crucial for maintaining compliance, resolving disputes, and ensuring the integrity of your digital agreements. 
     
     * **New roles for Agreement recipients beyond just the Signer**: Adobe Acrobat Sign have the option to expand the roles for Agreement recipients beyond just the Signer to better match their workflow requirements. When enabled, each recipient in an Agreement have their role individually configurable, with Signer being the default. 

* **Page Count Support in Communication APIs**: Now, along with retrieving your document through the Communication APIs, you can also receive the valuable information about the number of pages contained within the document. 

* **[Error handling with custom error handlers in rule editor](/help/forms/add-custom-error-handler-adaptive-forms-core-components.md)**: You can now invoke a custom function in response to an error returned by an external service and provide a tailored response to end users. For example, you can invoke a custom workflow in the backend for specific error codes or inform the customer that the service is down. 

* **[64-bit Version of AEM Forms Designer](/help/forms/installing-configuring-designer.md)**: The 64-bit version of AEM Forms Designer brings enhanced performance, scalability, and memory management to empower your form creation experience. With the 64-bit architecture, you can tackle even larger and more complex projects with ease, ensuring seamless design workflows and optimized efficiency. Elevate your form design capabilities and embrace the future of AEM Forms Designer with this cutting-edge release.

### Early adopter program {#forms-early-adopter}

* **[Protect your documents with DocAssurance APIs (Part of Communication APIs)](/help/forms/aem-forms-cloud-service-communications-introduction.md#document-assurance-doc-assurance)**: The DocAssurance APIs empower you to safeguard sensitive information by signing and encrypting the documents. Through encryption, the contents of a document are transformed into an unreadable format, ensuring that only authorized users can gain access. This fortified layer of protection not only shields valuable data from unauthorized eyes but also provides peace of mind. The Signature APIs let your organization protect the security and privacy of Adobe PDF documents that it distributes and receives. This service uses digital signatures and certification to ensure that only intended recipients can alter documents. 

     You can write to `aem-forms-ea@adobe.com` from your official email id to join the early adopter program and request access to the capability.

* **[Headless Adaptive Forms](https://experienceleague.adobe.com/docs/experience-manager-headless-adaptive-forms/using/overview.html)**: Use Headless Adaptive Forms to enable your developers to create, publish, and manage interactive forms that can be accessed and interacted with through APIs, rather than through a traditional graphical user interface. Headless adaptive forms help you: 

     * build high-quality multi-channel forms in the programming language of your choice 
     * natively integrate forms to your desktop and mobile apps, websites, and chat applications 
     * reuse your proprietary UI components with forms applications 
     * use the power of Adobe Experience Manager Forms 

     You can send an email to `aem-forms-headless@adobe.com` from your official email ID to join the early adopter program. 
     
## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### New CDN caching behavior for campaign-related URL parameters {#cache-url-params}

For new environments, the CDN will remove marketing related query parameters by default to increase marketing campaign performance and cache hit ratios. Existing environments are unaffected. [Learn more](/help/implementing/dispatcher/caching.md#marketing-parameters).

### Traffic Filter Rules (including WAF Rules) early adopter program {#waf-early-adopter}

Filter traffic at the CDN based on:

* request headers and properties (for example, IP address)
* traffic patterns known to be associated with malicious traffic

Interested in trying out the feature and sharing feedback? Send an email to **aemcs-waf-adopter@adobe.com** from your official email ID to learn more about the early adopter program. Space is limited.

Learn more about the feature in the article [here](/help/security/traffic-filter-rules-including-waf.md).

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes/current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
