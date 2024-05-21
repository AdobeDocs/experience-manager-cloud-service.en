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
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2024.4.0) is May 30, 2024. The next feature release (2024.5.0) is planned for June 27, 2024.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

<!-- ## Release Video {#release-video}

Have a look at the May 2024 Release Overview video for a summary of the features added in the 2024.5.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3429111?quality=12)

-->

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### Early Adopter Program {#sites-early-adopter}

**Generate Variations**

Leverage GenAI through AEM's new feature, [generate variations](/help/generative-ai/generate-variations.md), accessible now in Cloud Service. Generate variations helps you generate and scale content creation through the use of generative AI. Reach out to your Adobe account team for consideration in the program.

**Asset browsing in Content Fragment Console**

Content authors can now browse, view, and take actions on images, and other assets without having to leave the Content Fragment Console. 

 ![Asset Browsing](/help/sites-cloud/administering/content-fragments/assets/cf-console-assets-browse.png)

Interested in trying out the feature and sharing feedback? Send an email to aemcs-headless-adopter@adobe.com from your official email ID to learn more about the early adopter program.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in Assets view {#assets-view-new-features}


**Contextual Search**

You can now also [search assets available in the repository by defining text prompts](/help/assets/search-assets-view.md#contextual-search). Experience Manager Assets automatically transforms those text prompts to search filters and displays the search results. You can view and modify automatic filters using the Filters Pane to further narrow down the search results.

![Contextual Search](/help/assets/assets/contextual-search-text-prompt1.png)

**Express video quick actions**

Experience Manager Assets now includes [easy and intuitive video editing tools powered by Adobe Express](/help/assets/edit-videos-assets-view.md) to increase content re-use and accelerate content velocity. The editing options include trimming, cropping, resizing a video, and also converting an MP4 to a GIF file.

![crop video with Adobe Express](/help/assets/assets/adobe-express-crop-video.png)

**Dynamic renditions**

You can now [view and download dynamic renditions (including smart crops)](/help/assets/renditions.md) in Experience Manager Assets. Dynamic renditions are customized versions of image assets created in real-time to meet specific needs, such as resizing images based on device resolution or cropping to fit different aspect ratios. These renditions enable organizations to deliver personalized and optimized experiences to diverse audience needs.

![Dynamic renditions](/help/assets/assets/preset_smart_crop.png)

**In-place rename for assets and folders**

Experience Manager Assets now offers a simplified user experience by providing [ability to rename an asset or a folder via single click](/help/assets/manage-organize-assets-view.md).

**Assign or remove metadata form to multiple folders**

You can now [assign or remove metadata form to multiple folders](/help/assets/metadata-assets-view.md#assign-metadata-form-to-a-folder).

### New features in Admin view {#admin-view-new-features}

**Link share configuration**

A new improved user experience for [creating link shares](/help/assets/share-assets.md) along with a brand new set of configurations that let administrators customize the default behavior of this capability for your users.

![Link share configuration](/help/assets/assets/config-email-service.png)


## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

<!-- 

* **Configure a shard for Adobe Sign for AEM Forms**: Adobe distributes Acrobat Sign API around the globe in many deployment units called "shards." Each shard serves a customer's account, such as NA1, NA2, NA3, EU1, JP1, AU1, IN1, and others. The shard names correspond to geographic locations. You can now use more than one shard while using Adobe Sign integration with AEM Forms. 

--> 

### New features in AEM Forms {#forms-new-features}

* **Enhanced Visual Rule Editor for Core Component Based Adaptive Forms**: This release brings a significant upgrade to the visual rule editor for adaptive forms based on core components. This release brings a significant upgrade to the visual rule editor for adaptive forms based on core components. This update focuses on streamlining interactions with custom functions, empowering you to build more robust and efficient forms. 

  You can now streamline custom function interactions by: 

  * [Leveraging new annotations to provide clearer function definitions](/help/forms/create-and-use-custom-functions.md#supported-javascript-annotations-for-custom-function). 
  * [Using caching mechanisms for custom functions, leading to faster form performance](/help/forms/create-and-use-custom-functions.md#caching-support-for-custom-function).
  * [Seamlessly working with global objects within custom functions](/help/forms/create-and-use-custom-functions.md#field-and-global-scope-objects-in-custom-functions).
  * [Defining and utilizing optional parameters within custom functions](/help/forms/create-and-use-custom-functions.md#parameter).

  This update also brings the following enhancements to rule editor functionality. You can: 

  * Implement powerful ["when-then-else"](/help/forms/rule-editor-core-components.md#when) logic for conditional execution.
  * Leverage modern JavaScript features like let and arrow functions (ES10 support).
  * Validate or reset not only fields, but also entire panels and forms, expanding control over user interactions.

  These advancements provide a more intuitive and powerful experience for crafting rules and custom functions within the visual rule editor.

* **[Create multiple versions of an Adaptive Form](/help/forms/add-comments-annotations-versioning-adaptive-form-core-components.md)**: You can now easily manage variations of existing forms. This simplifies version control and facilitates comparison for form optimization, all within a single, streamlined workflow.

* **[Compare Adaptive Form](/help/forms/compare-forms.md)**: You can now easily compare two forms to dentify differences between two forms. It facilitates smooth collaboration by enabling team members to compare revisions and discuss changes efficiently.

* **Accessibility Enhancements for Scribble Signature Component**: This update brings significant accessibility improvements to the Scribble Signature component:

  **Improved Keyboard Navigation:**
  * Pressing the Tab key allows users to navigate through all interactive elements within the signature dialog box.
  * Signing with a brush or keyboard and pressing Enter closes the dialog.
  * Focus remains on the signature control after signing and clicking "OK".
  
  **Clear Signature Functionality:**
  
  * A clear cross icon for erasing the signature is accessible via the Tab key.
  * The "Clear Signature Confirmation" dialog is also accessible through Tab navigation.

  **Enhanced Labels and Controls:**
  * The label for the keyboard signature button is now clearer, using "aria-label" to announce functionality (such as "aria-label='Sign using Keyboard'").
  * Improved contrast ensures all controls within the scribble signature are easily distinguishable.
  * The OK/check mark button now visually indicates when it's inactive.

  **Signature Feedback for Screen Readers:**
  * When a signature is typed, screen reader users can hear the text used to create the signature.

This update ensures a more inclusive experience for users with disabilities by improving navigation, clarity, and feedback for the Scribble Signature component.

### Early Adopter Program {#forms-early-adopter}

* **[Submit an Adaptive Form to Adobe Workfront Fusion Scenario](/help/forms/submit-adaptive-form-to-workfront-fusion.md)**: Forms as a Cloud Service offers an out-of-the-box option to effortlessly connect an Adaptive Form with Adobe Workfront. This simplifies the process of submitting an Adaptive Form to an Adobe Workfront scenario, allowing you trigger a Workfront Fusion scenario on submission of an Adaptive Form. 

    <br/> ![Adobe Workfront](/help/forms/assets/adobe-workfront.png) <br/> Using the Adobe Workfront Fusion Connector, you can design workflows that are triggered automatically upon submission of an Adaptive Form. For instance, envision a scenario where a workflow is initiated to assign a specific individual the task of reviewing submitted data, allowing approval or rejection of an application based on the information captured through the adaptive form. This streamlined integration enhances efficiency and brings a new level of automation to your workflow processes.| 

* **[Reader Extension Service](/help/forms/aem-forms-cloud-service-communications-introduction.md#reader-extension-service)**: AEM Forms Communication APIs has brought Reader Extension Service to allow you to add functionalities like form filling and commenting to regular PDFs, making them interactive for users with the free Adobe Reader. 

* [Right to left languages support](/help/forms/supporting-new-language-localization-core-components.md): Adaptive Forms built on Core Components can now be presented in a Right-to-Left (RTL) language like Arabic, Persian, and Urdu. The RTL languages are spoken by over 2 billion people globally. Using a form in RTL language allows you to extend the reach of your adaptive forms to cater to these diverse audiences and select into RTL markets. In certain regions, it's also a legal mandate to provide forms in the local language. By accommodating local languages, you not only open doors to a broader audience but also ensure compliance with relevant laws and regulations.

* **[Protect your documents with DocAssurance APIs (Part of Communication APIs)](/help/forms/aem-forms-cloud-service-communications-introduction.md#document-assurance-doc-assurance)**: The DocAssurance APIs empower you to safeguard sensitive information by signing and encrypting the documents. Through encryption, the contents of a document are transformed into an unreadable format, ensuring that only authorized users can gain access. This fortified layer of protection not only shields valuable data from unauthorized eyes but also provides peace of mind. The Signature APIs let your organization protect the security and privacy of Adobe PDF documents that it distributes and receives. This service uses digital signatures and certification to ensure that only intended recipients can alter documents. 

     You can write to `aem-forms-ea@adobe.com` from your official email id to join the early adopter program and request access to the capability.

* **[You can leverage the Real User Monitoring (RUM) Data Service](/help/implementing/cloud-manager/content-requests.md#real-user-monitoring-for-aem-as-a-cloud-service)** to enable client-side collection for AEM as a Cloud Service.
Real User Monitoring (RUM) Data Service offers a more precise reflection of user interactions, ensuring a reliable measure of website engagement. It is a great opportunity to gain advanced insights into your page performance. While this is beneficial for customers who use either Adobe-managed CDN or non-Adobe-managed CDN. Additionally, for customers using a non-Adobe managed CDN, automated traffic reporting can now be enabled for them, thus removing the need to share any traffic report with Adobe.

   If you are interested in testing this new feature and sharing your feedback, please send an email to `aemcs-rum-adopter@adobe.com`, along with your domain name for each of the environments that you would like to enable RUM for from your email address associated with your Adobe ID. Adobe's product team will then enable the Real User Monitoring (RUM) Data Service for you.
     
## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### Traffic Spike at Origin Alerts {#traffic-spike-origin}

Receive proactive notifications when traffic patterns at the origin are indicative of a DDoS attack, allowing you to investigate and configure [traffic filter rules](/help/security/traffic-filter-rules-including-waf.md).

### RDE Support for Front-End Code using Site Themes and Site Templates (Early Adopter Program) {#rde-frontend}

[Rapid Development Environments (RDEs)](/help/implementing/developing/introduction/rapid-development-environments.md) now support front-end code based on [site themes](/help/sites-cloud/administering/site-creation/site-themes.md) and [site templates](/help/sites-cloud/administering/site-creation/site-templates.md), for early adopters. With RDEs, this is done using a command line directive, rather than a [front-end pipeline](/help/sites-cloud/administering/site-creation/enable-front-end-pipeline.md).


### Early Adopter Programs {#foundation-early-adopter}

#### Client-side redirects (Early Adopter Program) {#client-side-redirects-early-adopter}

Configure 301/302 client-side redirects in source control, and deploy to the CDN. [Learn more](/help/implementing/dispatcher/cdn-configuring-traffic.md#client-side-redirectors) and join the early adopter program by emailing **<aemcs-cdn-config-adopter@adobe.com>**. Note that there are several other features already available related to [CDN configuration](/help/implementing/dispatcher/cdn-configuring-traffic), including request and response transformations, and routing traffic to off-AEM sites.

#### Traffic Filter Rules Alerts (Early Adopter Program) {#traffic-filter-rules-alerts-early-adopter}

The recently released [Traffic Filter Rules](/help/security/traffic-filter-rules-including-waf.md), which include the optionally licensable Web Application Firewall (WAF) rules, lets you configure what traffic should be allowed or denied. 

Now you can email **<aemcs-cdn-config-adopter@adobe.com>** to join the early adopter program so you can be alerted whenever your traffic filter rules are triggered. Actions Center email notifications will keep you informed when certain traffic conditions occur so you can take appropriate measures. 

#### Apache/Dispatcher Runtime Ingestion of Rewrite Maps (Early Adopter Program) {#apache-rewritemaps-early-adopter}

Similar to AEM 6.5, Apache/dispatcher will ingest rewrite maps placed in a specific location in the publish repository, and load them, without requiring a web tier pipeline execution. This opens up opportunities for a business user to declare redirects using a UI, such as that offered by ACS Commons Redirect Map Manager. Please reach out to **<aemcs-cdn-config-adopter@adobe.com>** for more information.

#### Edge Side Includes (ESI) for Loading Dynamic Content (Early Adopter Program) {#esi-early-adopter}

The Adobe Managed CDN now supports Edge Side Includes (ESI), a markup language for edge level dynamic web content assembly. By including ESI snippets, you can cache the overall HTML page at the CDN with higher TTLs, while more frequently fetching from origin those smaller sections that require higher cadence updates (lower TTLs). Please reach out to **<aemcs-cdn-config-adopter@adobe.com>** for more information.

#### Enhanced logging for RDEs (Early Adopter Program) {#rde-logging-early-adopter}

While debugging code in a [Rapid Development Environment (RDE)](/help/implementing/developing/introduction/rapid-development-environments.md), developers can now configure and stream logs more efficiently, using the command line, and without modifying OSGI properties in version control. Features include:

* declare log levels on a per package or class level
* customize the log output format
* stream multiple logs in parallel 

Please reach out to **<aemcs-rde-support@adobe.com>** to try it out and provide feedback.

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes/current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
