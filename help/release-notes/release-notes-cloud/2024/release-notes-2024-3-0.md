---
title: Release Notes for 2024.3.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2024.3.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: b3816929-2c0a-4d6a-b583-c928d2182ecd
feature: Release Information
role: Admin
---
# 2024.3.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2024.3.0 version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions such as 2021 or 2022.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2024.3.0) is April 11, 2024. The next feature release (2024.4.0) is planned for April 25, 2024.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Release Video {#release-video}

Have a look at the March 2024 Release Overview video for a summary of the features added in the 2024.3.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3428342?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features in [!DNL Experience Manager Sites] {#sites-features}

**AEM Authoring for Edge Delivery Services**

AEM Sites can now be used as a content source for Edge Delivery Services. Authors manage their websites in AEM using the new Universal Editor with in-context wysiwyg authoring. This enables companies to build fast high performance webpages with Edge Delivery Services while leveraging AEM's powerful capabilites for content management.

  ![AEM Authoring](/help/edge/assets/universal_editor_edge_delivery_services.png)
  
For more information, see the [documentation](/help/edge/overview.md) and watch the [AEM Gems - Getting started with AEM Authoring and Edge Delivery Services](https://experienceleaguecommunities.adobe.com/t5/adobe-experience-manager/aem-gems-getting-started-with-aem-authoring-and-edge-delivery/m-p/652694#M43905)

**Universal Editor for Headless Implementations**

The Universal Editor enables also decoupled web applications to harness the same intuitive in-context WYSIWYG authoring previously exclusive to traditional sites. Content creators can now visually compose layouts using Content Fragments with the same ease as components within pages.

What sets the Universal Editor apart is its adaptability to diverse web architectures, accommodating both server- and client-side rendering, remaining framework-agnostic, and eliminating the necessity for AEM hosting. Integrating existing web applications with the Universal Editor for content editing is straightforward, primarily requiring developers to incorporate specific data attributes into their markup.

With that, the Universal Editor ensures a consistent editing experience, regardless of content structure or underlying technology stack. For more information, see the [Universal Editor Introduction](/help/implementing/universal-editor/introduction.md).

**Content Management OpenAPIs for Content Fragments and Models**

Developers can now programmatically interact with Content Fragments and Content Fragment models and perform CruD operations on them using Content Management OpenAPIs. For more information, see [API documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/sites/)

**Multisite Management support for Experience Fragments**

Multisite Management support has been extended for folder structures that store experience fragments, allowing users to rollout a complete content structure with experience fragments.

**Compare Content Fragment Versions**

The new Content Fragment Editor now allows content authors to compare and view differences between the current version of a content fragment and a previous version. 

### Early Adopter Program {#sites-early-adopter}

**Generate Variations**

Leverage GenAI through AEM's new feature, [generate variations](/help/generative-ai/generate-variations.md), accessible now in Cloud Service. Generate variations helps you generate and scale content creation through the use of generative AI. Reach out to your Adobe account team for consideration in the program.

**Asset browsing in Content Fragment Console**

Content authors can now browse, view, and take actions on images, and other assets without having to leave the Content Fragment Console. 

 ![Asset Browsing](/help/sites-cloud/administering/content-fragments/assets/cf-console-assets-browse.png)

Interested in trying out the feature and sharing feedback? Send an email to aemcs-headless-adopter@adobe.com from your official email ID to learn more about the early adopter program.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in Admin view {#admin-view}

**Native integration with Adobe Express**

AEM Assets integrates natively with Adobe Express, which allows you to directly access the assets stored in AEM Assets from within the Adobe Express user interface. You can place content managed in AEM Assets in the Express canvas and then save new or edited content in an AEM Assets repository.

![Include assets from Assets add-on](/help/assets/assets/adobe-express-native-integration.png)

**Preview renditions for all supported video types**

Experience Manager Assets now generates preview renditions of all supported video types by default without requiring a processing profile configuration.

### New features in Assets view {#assets-view}

**Manage permissions for collections** 

Assets Essentials allows the administrators to manage access levels for private collections available in the repository. As an administrator, you can create user groups and assign permissions to those groups to manage access levels. You can also delegate the permission management privileges to user groups.


## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

<!-- 

* **Configure a shard for Adobe Sign for AEM Forms**: Adobe distributes Acrobat Sign API around the globe in many deployment units called "shards." Each shard serves a customer's account, such as NA1, NA2, NA3, EU1, JP1, AU1, IN1, and others. The shard names correspond to geographic locations. You can now use more than one shard while using Adobe Sign integration with AEM Forms. 

--> 

### New features for AEM Forms {#forms-new-features}

* **[Adobe Experience Manager Forms Edge Delivery Services](/help/edge/docs/forms/overview.md)**: Edge Delivery Services for AEM Forms is a composable set of services that enables a rapid development environment where authors can update, publish, and launch new forms rapidly. These services deliver exceptional and high impact forms experiences that drive engagement and conversions. These forms experiences are easy to author and develop. 

  ![EDS Forms Features](/help/edge/assets/eds-forms-features.png)

These services enable you to:

  * Work with multiple content sources on the same forms site and use your preferred authoring tools, such as Microsoft Excel, Google Sheets, or Adaptive Forms Editor.
  * Deliver Digital Enrollment experiences that load and render quickly and continuously monitor your forms performance through real use monitoring (RUM).
  * Use plain HTML, modern CSS, and vanilla JavaScript to create exceptional experiences, avoiding the steep learning curve of a specific framework.


### New features in Prerelease for AEM Forms {#forms-pre-release}

* **Enhanced Visual Rule Editor for Core Component Based Adaptive Forms**: This release brings a significant upgrade to the visual rule editor for adaptive forms based on core components. This release brings a significant upgrade to the visual rule editor for adaptive forms based on core components. This update focuses on streamlining interactions with custom functions, empowering you to build more robust and efficient forms. 

  You can now streamline custom function interactions by: 

  * Leveraging new annotations to provide clearer function definitions. 
  * Using caching mechanisms for custom functions, leading to faster form performance.
  * Seamlessly working with global objects within custom functions.
  * Defining and utilizing optional parameters within custom functions.

  This update also brings the following enhancements to rule editor functionality. You can: 

  * Implement powerful "when-then-else" logic for conditional execution.
  * Leverage modern JavaScript features like let and arrow functions (ES10 support).
  * Validate or reset not only fields, but also entire panels and forms, expanding control over user interactions.

  These advancements provide a more intuitive and powerful experience for crafting rules and custom functions within the visual rule editor.

* **Create multiple versions of an Adaptive Form**: You can now easily manage variations of existing forms. This simplifies version control and facilitates comparison for form optimization, all within a single, streamlined workflow.

* **Compare Adaptive Form**: You can now easily compare two forms to dentify differences between two forms. It facilitates smooth collaboration by enabling team members to compare revisions and discuss changes efficiently.

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

* **Reader Extension Service**: AEM Forms Communication APIs has brought Reader Extension Service to allow you to add functionalities like form filling and commenting to regular PDFs, making them interactive for users with the free Adobe Reader. 

* [Right to left languages support](/help/forms/supporting-new-language-localization-core-components.md): Adaptive Forms built on Core Components can now be presented in a Right-to-Left (RTL) language like Arabic, Persian, and Urdu. The RTL languages are spoken by over 2 billion people globally. Using a form in RTL language allows you to extend the reach of your adaptive forms to cater to these diverse audiences and select into RTL markets. In certain regions, it's also a legal mandate to provide forms in the local language. By accommodating local languages, you not only open doors to a broader audience but also ensure compliance with relevant laws and regulations.

* **[Protect your documents with DocAssurance APIs (Part of Communication APIs)](/help/forms/aem-forms-cloud-service-communications-introduction.md#document-assurance-doc-assurance)**: The DocAssurance APIs empower you to safeguard sensitive information by signing and encrypting the documents. Through encryption, the contents of a document are transformed into an unreadable format, ensuring that only authorized users can gain access. This fortified layer of protection not only shields valuable data from unauthorized eyes but also provides peace of mind. The Signature APIs let your organization protect the security and privacy of Adobe PDF documents that it distributes and receives. This service uses digital signatures and certification to ensure that only intended recipients can alter documents. 

     You can write to `aem-forms-ea@adobe.com` from your official email id to join the early adopter program and request access to the capability.

* **[You can leverage the Real Use Monitoring (RUM) Data Service](/help/implementing/cloud-manager/content-requests.md#real-user-monitoring-for-aem-as-a-cloud-service)** to enable client-side collection for AEM as a Cloud Service.
Real Use Monitoring (RUM) Data Service offers a more precise reflection of user interactions, ensuring a reliable measure of website engagement. It is a great opportunity to gain advanced insights into your page performance. While this is beneficial for customers who use either Adobe-managed CDN or non-Adobe-managed CDN. Additionally, for customers using a non-Adobe managed CDN, automated traffic reporting can now be enabled for them, thus removing the need to share any traffic report with Adobe.

   If you are interested in testing this new feature and sharing your feedback, please send an email to `aemcs-rum-adopter@adobe.com`, along with your domain name for each of the environments that you would like to enable RUM for from your email address associated with your Adobe ID. Adobe's product team will then enable the Real Use Monitoring (RUM) Data Service for you.
     
## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### Early Adopter Programs {#foundation-early-adopter}

#### Traffic Filter Rules Alerts (Early Adopter Program) {#traffic-filter-rules-alerts-early-adopter}

The recently released [Traffic Filter Rules](/help/security/traffic-filter-rules-including-waf.md), which include the optionally licensable Web Application Firewall (WAF) rules, lets you configure what traffic should be allowed or denied. 

Now you can email **<aemcs-cdn-config-adopter@adobe.com>** to join the early adopter program so you can be alerted whenever your traffic filter rules are triggered. Actions Center email notifications will keep you informed when certain traffic conditions occur so you can take appropriate measures. 

#### CDN Configuration (Early Adopter Program) {#cdn-config-early-adopter}

In addition to the recently released [Traffic Filter Rules](/help/security/traffic-filter-rules-including-waf.md), which include the optionally licensable Web Application Firewall (WAF) rules, there's an opportunity to use the Configuration Pipeline to declare and deploy other types of CDN configuration. [Learn more](/help/implementing/dispatcher/cdn-configuring-traffic.md) and join the early adopter program by emailing **<aemcs-cdn-config-adopter@adobe.com>** to gain access to:

* 301/302 client-side redirects
* proxying requests at the edge to arbitrary origins (such as non-AEM applications)
* URL transformations
* setting or modifying request or response headers
* custom error pages when the CDN can't reach AEM

#### Apache/Dispatcher Runtime Ingestion of Rewrite Maps (Early Adopter Program) {#apache-rewritemaps-early-adopter}

Similar to AEM 6.5, Apache/dispatcher will ingest rewrite maps placed in a specific location in the publish repository, and load them, without requiring a web tier pipeline execution. This opens up opportunities for a business user to declare redirects using a UI, such as that offered by ACS Commons Redirect Map Manager. Please reach out to **<aemcs-cdn-config-adopter@adobe.com>** for more information.

#### Edge Side Includes (ESI) for Loading Dynamic Content (Early Adopter Program) {#esi-early-adopter}

The Adobe Managed CDN now supports Edge Side Includes (ESI), a markup language for edge level dynamic web content assembly. By including ESI snippets, you can cache the overall HTML page at the CDN with higher TTLs, while more frequently fetching from origin those smaller sections that require higher cadence updates (lower TTLs). Please reach out to **<aemcs-cdn-config-adopter@adobe.com>** for more information.

#### RDE Support for Front-End Code using Site Themes and Site Templates (Early Adopter Program) {#rde-frontend-early-adopter}

[Rapid Development Environments (RDEs)](/help/implementing/developing/introduction/rapid-development-environments.md) now support front-end code based on [site themes](/help/sites-cloud/administering/site-creation/site-themes.md) and [site templates](/help/sites-cloud/administering/site-creation/site-templates.md), for early adopters. With RDEs, this is done using a command line directive, rather than a [front-end pipeline](/help/sites-cloud/administering/site-creation/enable-front-end-pipeline.md). Please reach out to **<aemcs-rde-support@adobe.com>** to try it out and provide feedback.

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
