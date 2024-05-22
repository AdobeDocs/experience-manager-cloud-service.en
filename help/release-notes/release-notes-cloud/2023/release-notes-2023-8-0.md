---
title: Release Notes for 2023.8.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2023.8.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: a0ffa6cf-64ae-468c-93f4-ac6805ef907e
---
# 2023.8.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2023.8.0 version of [!DNL Experience Manager] as a Cloud Service.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2023.8.0) is August 31, 2023. The next feature release (2023.9.0) is planned for September 28, 2023.

## Release Video {#release-video}

Have a look at the August 2023 Release Overview video for a summary of the features added in the 2023.8.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3423535/?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features in [!DNL Experience Manager Sites] {#sites-features}

* The [Content Fragment Console](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/content-fragments-console.html) now allows users to view tags and search by tags applied as metadata to Content Fragments. Users will no longer have to switch to the Assets UI for this capability, reducing context switching and improving efficiency. 

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

* **Bulk import assets from data sources**: Administrators now have the [ability to import large number of assets](/help/assets/bulk-import-assets-view.md) from a data source to AEM Assets. The administrators do not need to upload individual assets or folders to AEM Assets anymore. The supported data sources for bulk import include Azure, AWS, Google Cloud, and Dropbox.

  ![Bulk import assets from a data source](/help/release-notes/assets/bulk-import.png)

* **Image editing tools powered by Adobe Express**: Easy and intuitive [image editing tools powered by Adobe Express](/help/assets/edit-images-assets-view.md) available directly within AEM Assets to increase content re-use and accelerate content velocity.

  ![Image editing with Adobe Express](/help/release-notes/assets/edit-adobe-express.png)

* **Flexibility while pinning items for My Workspace Quick Access**: Ability to select and pin items for you, for your entire organization, or for a list of groups so that they display in the [Quick Access section of My Workspace](/help/assets/my-workspace-assets-view.md) based on your selection.

  ![Pin items for groups](/help/release-notes/assets/pin-items-for-groups.png)

### New features in Admin view {#admin-view-features}

**Search enhancements**

* Administrators can now [configure the batch size of assets](/help/assets/search-assets.md#configure-asset-batch-size) that display when you perform a search. The asset search results display in multiples of the configured batch size number when you further scroll down to load the results. You can select from the available batch sizes of 200, 500, and 1000 assets. Setting a lower batch size number results in faster search response times.

  ![Assets batch size configuration](/help/release-notes/assets/assets-batch-size-configuration.png)  

* Experience Manager Assets now includes a new version 9 of `damAssetLucene` index. `damAssetLucene-9` changes the behavior of Oak Query facet counting to [no longer evaluate access control on the facet counts](/help/assets/search-assets.md) returned by the underlying search index, which results in the faster search response times.

### Pre-release features available in [!DNL Experience Manager Assets] {#prerelease-features-assets}

* **Dynamic Media**: [Multi-caption and multi-audio track support for videos in Dynamic Media](/help/assets/dynamic-media/video.md#about-msma)&mdash;You can now easily add multiple captions and multiple audio tracks to a primary video. This capability means that your videos are accessible across a global audience. You can customize a single, published primary video to a global audience in multiple languages and adhere with accessibility guidelines for different geographical regions. Authors can also manage the captions and audio tracks from a single tab in the user interface.

  ![Captions and Audio tracks tab on the Properties page of a selected video asset.](/help/release-notes/assets/msma-aem-cs.png)*Captions and Audio tracks tab on the Properties page of a selected video asset.*

* **Assets**: Ability to select ZIP archives that are managed in Experience Manager and [extracting the files directly into Experience Manager](/help/assets/manage-digital-assets.md#extract-zip-archives) without downloading them.

  ![Pin items for groups](/help/release-notes/assets/extract-archive.png)


## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features available in [!DNL Forms] {#new-features-available-in-forms-channel}

* [**Google reCAPTCHA enterprise support**](/help/forms/captcha-adaptive-forms.md): Use Google reCAPTCHA Enterprise in an Adaptive Form to provide enhanced protection against fraudulent activity and spam, providing a safer user experience. With advanced risk analysis and seamless integration, genuine users can easily submit forms while bots are effectively blocked.


### Pre-release features available in [!DNL Forms] {#pre-release-features-available-in-forms-channel}

* **Adobe Analytics with Experience Cloud Setup Automation for Forms**: You can now enable Adobe Analytics with Experience Cloud Setup Automation with a flip of couple of buttons. It enables you to connect AEM Forms as a Cloud Service with Experience Platform tags and Adobe Analytics to capture and track performance metrics for your published forms. 

* **Adobe Analytics report template for Adaptive Forms**: Forms as a Cloud Service now provides an Adobe Analytics report OOTB. It helps you easily understand performance of your forms. The form-level metrics provide you an insight into how the form is performing on multiple key performance indicators (KPIs) like, renditions, visitors, submissions, Average fill time. By tracking user behavior and feedback, you can identify areas of the form that are causing confusion and guide improvements to the form's design and functionality. 

     ![Adaptive form user engagement adobe analytics report](/help/forms/assets/forms-analytics-report.png)

* **[Form Fragment in Adaptive Forms based on Core Components](/help/forms/adaptive-form-fragments-core-components.md)**: Say goodbye to duplication, optimize your digital inventory, and improve collaboration as you elevate your form-building experience with Form Fragments. These reusable components seamlessly integrate into multiple forms, streamlining the creation of consistent and professional-looking forms. Form Fragments ensure reusability, standardization, and brand consistency through 'change once and reflect everywhere' functionality. Experience greater maintainability and efficiency as updates made in one place are automatically propagated across all forms that utilize these fragments.

* **[Enhanced Adobe Sign Workflow step](/help/forms/aem-forms-workflow-step-reference.md#sign-document-step-sign-document-step)**: The Adobe Sign Workflow step is enhanced to include the following:
     * **Government ID-Based Authentication for Adobe Sign**: Adobe Acrobat Sign's Government ID-Based Authentication offers an additional layer of verification by enabling users to authenticate their identity using government-issued IDs (driver's license, national ID, passport). By using trusted identification documents, this enhancement adds an extra level of confidence to the signing process, making it ideal for scenarios that require heightened security, compliance, and user validation. 

     * **Audit Trail for Adobe Sign Documents**:  Use the Audit Trail feature for detailed insights into the lifecycle of your Adobe Sign documents. With the Audit Trail, you can now maintain a comprehensive record of all actions and interactions related to your documents. This includes details such as who viewed, edited, or signed the document, along with timestamps for each event. This enhancement is crucial for maintaining compliance, resolving disputes, and ensuring the integrity of your digital agreements. 
     
     * **New roles for Agreement recipients beyond just the Signer**: Adobe Acrobat Sign have the option to expand the roles for Agreement recipients beyond just the Signer to better match their workflow requirements. When enabled, each recipient in an Agreement have their role individually configurable, with Signer being the default. 

* **[Protect your documents with Document Assurance APIs (Part of Communication APIs)](/help/forms/aem-forms-cloud-service-communications-introduction.md#document-assurance-doc-assurance)**: The Document Assurance APIs  empowers you to safeguard sensitive information by signing and encrypting the documents. Through encryption, the contents of a document are transformed into an unreadable format, ensuring that only authorized users can gain access. This fortified layer of protection not only shields valuable data from unauthorized eyes but also provides peace of mind. The Signature APIs let your organization protect the security and privacy of Adobe PDF documents that it distributes and receives. This service uses digital signatures and certification to ensure that only intended recipients can alter documents.

* **Page Count Support in Communication APIs**: Now, along with retrieving your document through the Communication APIs, you can also receive the valuable information about the number of pages contained within the document. 

* **[Error handling with custom error handlers in rule editor](/help/forms/add-custom-error-handler-adaptive-forms-core-components.md)**: You can now invoke a custom function in response to an error returned by an external service and provide a tailored response to end users. For example, you can invoke a custom workflow in the backend for specific error codes or inform the customer that the service is down. 


### Headless Adaptive Forms early adopter program {#forms-early-adopter}

Use [Headless Adaptive Forms](https://experienceleague.adobe.com/docs/experience-manager-headless-adaptive-forms/using/overview.html) to enable your developers to create, publish, and manage interactive forms that can be accessed and interacted with through APIs, rather than through a traditional graphical user interface. Headless adaptive forms help you: 

* build high-quality multi-channel forms in the programming language of your choice 
* natively integrate forms to your desktop and mobile apps, websites, and chat applications 
* reuse your proprietary UI components with forms applications 
* use the power of Adobe Experience Manager Forms 

You can send an email to `aem-forms-headless@adobe.com` from your official email ID to join the early adopter program. 


## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### CDN Logs {#cdn-logs}

Download CDN logs from Cloud Manager, which is useful for cache-hit ratio optimization and greater visibility into the content delivery flow. [Learn about](/help/implementing/developing/introduction/logging.md#cdn-log) the CDN log format. This feature will gradually be rolled out to customers in early September.

### CDN and WAF Rules early adopter program {#waf-early-adopter}

Filter traffic at the CDN based on:

* request headers and properties (for example, IP address)
* traffic patterns known to be associated with malicious traffic

Interested in trying out the feature and sharing feedback? Send an email to **aemcs-waf-adopter@adobe.com** from your official email ID to learn more about the early adopter program. Space is limited.

Learn more about the feature in the article [here](/help/security/traffic-filter-rules-including-waf.md).


## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes/current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
