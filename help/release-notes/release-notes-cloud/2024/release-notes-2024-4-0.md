---
title: Release Notes for 2024.4.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2024.4.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: 153a3172-676f-4434-94d4-12fab8e17734
feature: Release Information
role: Admin
---
# 2024.4.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2024.4.0 version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions such as 2021 or 2022.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2024.4.0) is April 25, 2024. The next feature release (2024.5.0) is planned for May 30, 2024.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Release Video {#release-video}

Have a look at the April 2024 Release Overview video for a summary of the features added in the 2024.4.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3429111?quality=12)

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

![Link Share Configuration](/help/assets/assets/config-email-service.png)



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

* **[You can leverage the Real Use Monitoring (RUM) Data Service](/help/implementing/cloud-manager/content-requests.md#real-user-monitoring-for-aem-as-a-cloud-service)** to enable client-side collection for AEM as a Cloud Service.
Real Use Monitoring (RUM) Data Service offers a more precise reflection of user interactions, ensuring a reliable measure of website engagement. It is a great opportunity to gain advanced insights into your page performance. While this is beneficial for customers who use either Adobe-managed CDN or non-Adobe-managed CDN. Additionally, for customers using a non-Adobe managed CDN, automated traffic reporting can now be enabled for them, thus removing the need to share any traffic report with Adobe.

   If you are interested in testing this new feature and sharing your feedback, please send an email to `aemcs-rum-adopter@adobe.com`, along with your domain name for each of the environments that you would like to enable RUM for from your email address associated with your Adobe ID. Adobe's product team will then enable the Real Use Monitoring (RUM) Data Service for you.
     
## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### CDN Configuration {#cdn-config}

Configure traffic at the Adobe CDN in the following ways:

* [Request transformations](/help/implementing/dispatcher/cdn-configuring-traffic.md#request-transformations) - modify aspects of incoming requests, including paths, query parameters, and HTTP headers before they are routed to AEM.
* [Response transformations](/help/implementing/dispatcher/cdn-configuring-traffic.md#response-transformations) - change HTTP headers of the outgoing responses before they are served to the browser.
* [Origin selectors](/help/implementing/dispatcher/cdn-configuring-traffic.md#response-transformations#origin-selectors) - route traffic through the CDN to off-AEM sites and applications.

Once these rules are declared in source control (git), you can deploy them to the CDN using the Cloud Manager Configuration Pipeline. Also see the client-side redirects feature in the early adopter section below.

### Custom CDN error pages {#cdn-error-pages}

In the unlikely event that the CDN cannot route traffic to the AEM origin, a custom error page can be declared, replacing the generic version. [Learn more](/help/implementing/dispatcher/cdn-error-pages.md) about how to serve branded error pages.

### Early Adopter Programs {#foundation-early-adopter}

#### Client-side redirects (Early Adopter Program) {#client-side-redirects-early-adopter}

Configure 301/302 client-side redirects in source control, and deploy to the CDN. [Learn more](/help/implementing/dispatcher/cdn-configuring-traffic.md#client-side-redirectors) and join the early adopter program by emailing **<aemcs-cdn-config-adopter@adobe.com>**.

#### Traffic Filter Rules Alerts (Early Adopter Program) {#traffic-filter-rules-alerts-early-adopter}

The recently released [Traffic Filter Rules](/help/security/traffic-filter-rules-including-waf.md), which include the optionally licensable Web Application Firewall (WAF) rules, lets you configure what traffic should be allowed or denied. 

Now you can email **<aemcs-cdn-config-adopter@adobe.com>** to join the early adopter program so you can be alerted whenever your traffic filter rules are triggered. Actions Center email notifications will keep you informed when certain traffic conditions occur so you can take appropriate measures. 

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

## [!DNL Experience Manager] Guides {#guides}

### Ability to Translate Content into Multiple Languages Using Preconfigured Language Groups

Experience Manager Guides now allows you to create language groups and easily translate your content into multiple languages. This feature helps you organize and manage translations according to your organization's needs. 

For example, if you need to translate your content for some countries in Europe, you can create a language group for European languages like English (EN), French (FR), German (DE), Spanish (ES), and Italian (IT).

![translation panel](/help/release-notes/assets/guides/translation-languages-2404.png)

*Select the language groups or languages you want to translate your documents.* 

>[!NOTE]
>
>If a language's target folder is missing or the target language is the same as the source, it's grayed out and shows a warning sign.

As an administrator you can create language groups and configure them to multiple folder profiles. As an author, you can view the language groups that are configured on your folder profile.


Overall, creating language groups enhances the efficiency and productivity of translation projects, ultimately improving the localization process across multiple languages.


Learn how to [translate documents from the Web Editor](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/user-guide/author-content/create-preview-topics/author-content-aem-guides/work-with-web-editor/translate-documents-web-editor)

### Revamped Experience to Search and Filter Files in the Repository View

Now, you have an enhanced experience while filtering files. The revamped functionality to filter files provides an improved way to effortlessly search and navigate through files. 

![search files in repository view](/help/release-notes/assets/guides/repository-filter-search-2404.png)

*Search for the files containing the text `general purpose.`*

Enjoy benefits such as quicker access to relevant files and a more intuitive user interface, making your search experience smoother and more efficient. 

![quick search filter ](/help/release-notes/assets/guides/repository-filter-search-quick.png)

*Use the quick filters to search for DITA and Non-DITA files.*

Learn more about the **Filter Search** feature in the [Left Panel](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/user-guide/author-content/create-preview-topics/author-content-aem-guides/work-with-web-editor/web-editor-features#id2051EA0M0HS) section.

### Enhancements in the Data Source Connectors

The following enhancements have been made to the data source connectors for the 2024.4.0 release:

#### Connect to Salsify, Akeneo, and Microsoft Azure DevOps Boards (ADO) Data Sources

In addition to the existing out-of-the-box connectors, Experience Manager Guides also provides connectors for Salsify, Akeneo, and Microsoft Azure DevOps Boards (ADO) data sources. As an administrator, you can download and install these connectors. Then, configure the installed connectors.

#### Copy and Paste the Sample Query to Create a Content Snippet or Topic

You can easily copy and paste a sample data query in the generator to create a content snippet or topic. With this feature, you don't have to remember the syntax or create a  query manually. Instead of manually typing the query, you can copy and paste a sample query, edit it, and use it to fetch the data per your requirements. 

![insert content snippet dialog box](/help/release-notes/assets/guides/insert-content-snippet.png)

 *Copy and edit a sample query to create the content snippet.*

#### Connect to JSON Data Files Using a File Connector 


Now, as an administrator, you can configure a JSON file connector to use JSON data files as a data source. Use the connector to import the JSON files from your computer or the Adobe Experience Manager Assets. Then, as an author, you can create content snippets or topics using the generators.

This feature helps you use the data stored in your JSON files and reuse it across various snippets. The content is also updated dynamically whenever you update the JSON files.

#### Configure Multiple Resource URLs for a Connector to Create Content Snippets or Topics

As an administrator, you can configure multiple resource  URLs for some connectors like Generic REST Client, Salsify, Akeneo, and Microsoft Azure DevOps Boards (ADO). 
Then, as an author, connect with the data sources to create content snippets or topics using the generators. This feature is handy as you don't have to create a data source for each URL. It helps you to quickly fetch data from any of the resources for a particular data source in a single content snippet or topic. View more details about the data source connectors and how to [configure a data source connector from the user interface](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/install-guide/cs-ig/web-editor-configs-cs/conf-data-source-connector-tools). Learn how to [use data from your data source](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/user-guide/author-content/create-preview-topics/author-content-aem-guides/work-with-web-editor/web-editor-content-snippet).

For more information about the new features and enhancements, view [Experience Manager Guides releases information](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap).

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes/current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
