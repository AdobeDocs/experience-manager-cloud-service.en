---
title: Release Notes for 2024.6.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2024.6.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 4033abf4-7094-4ce4-ba93-c936062667e3
---
# 2024.6.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2024.6.0 version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions such as 2022 or 2023.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>To receive a monthly email notification about updates to Experience Cloud release notes, subscribe to the [Adobe Priority Product Update](https://www.adobe.com/subscription/priority-product-update.html).

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2024.6.0) is June 27, 2024. The next feature release (2024.7.0) is planned for July 25, 2024.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Release Video {#release-video}

Have a look at the June 2024 Release Overview video for a summary of the features added in the 2024.6.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3430779?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New feature in Experience Manager Sites {#new-feature-sites}

**Real Use Monitoring (RUM) Data Service** {#real-use-monitoring}

The [Real Use Monitoring (RUM) Data Service](/help/sites-cloud/administering/real-use-monitoring-for-aem-as-a-cloud-service.md) is now generally available, enabling client-side data collection for AEM as a Cloud Service. This service provides a more accurate reflection of user interactions, ensuring a reliable measure of website engagement. It offers customers advanced insights into their page traffic and performance, presenting a valuable opportunity to understand and enhance page performance.

### Early Adopter Program {#sites-early-adopter}

**Generate Variations**

Leverage GenAI through AEM's new feature, [generate variations](/help/generative-ai/generate-variations.md), accessible now in Cloud Service. Generate variations helps you generate and scale content creation through the use of generative AI. Reach out to your Adobe account team for consideration in the program.

**Asset browsing in Content Fragment Console**

Content authors can now browse, view, and take actions on images, and other assets without having to leave the Content Fragment Console. 

 ![Asset Browsing](/help/sites-cloud/administering/content-fragments/assets/cf-console-assets-browse.png)

Interested in trying out the feature and sharing feedback? Send an email to aemcs-headless-adopter@adobe.com from your official email ID to learn more about the early adopter program.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in Experience Manager Assets {#new-features-assets}



**Content Hub**

Content Hub is available as part of Experience Manager Assets as a Cloud Service for democratizing access to on-brand content for organizations and their business partners. With Content Hub, you can easily find and distribute assets, reuse and create new on-brand variations, and accelerate activation at scale.

![Content Hub user interface](/help/release-notes/assets/content-hub-ui.png)

**Dynamic Media with OpenAPI Capabilities**

Dynamic Media with OpenAPI capabilities extends the DAM across Adobe and third-party applications, enabling access to on brand approved digital assets, in any channel, via Asset Selector or OpenAPI stack. Key tenets - no binary copies, assets are optimized and transformed at the edge for fast performance, deliver assets public or secure.

![New Dynamic Media data flow diagram](/help/assets/assets/dm-openapi-dfd.png)


### New features in Assets view {#assets-view-new-features}

**More options are available in the Assets Insights dashboard**

Asset Count by asset type and size are now available in the Assets Insights dashboard. These options deliver real-time data in your Assets view environment. They detail the count and percentage of assets by size range and asset type.

**Updates to embedded Adobe Express editor**

* Improved User Experience for saving as a new asset versus saving as a new version.

* Export of multipage Express documents (previously only single page was supported) in both multipage PDF and image formats. Selecting image formats saves each page as a distinct asset in the DAM for downstream distribution.

* Support for adding metadata in the Save dialog while saving an asset.

<!--


**Content Credentials**

Content Credentials feature in Assets view now provides detailed asset provenance data adhered to an asset. This helps to trace the enroute edits along the asset's lifecycle to prevent users from deception through deliberately tempered assets. This ensures content authenticity among users and fosters trust through transparency.

When looking at the asset details, any image with content credentials added, such as those created with GenAI, displays the manifest details in a dedicated panel. If the asset is downloaded, published, or shared, the credentials remain intact with the asset.

![check publish status1](/help/release-notes/assets/content-credentials.png)

-->

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

<!-- 

* **Configure a shard for Adobe Sign for AEM Forms**: Adobe distributes Acrobat Sign API around the globe in many deployment units called "shards." Each shard serves a customer's account, such as NA1, NA2, NA3, EU1, JP1, AU1, IN1, and others. The shard names correspond to geographic locations. You can now use more than one shard while using Adobe Sign integration with AEM Forms. 

--> 

### New features in AEM Forms {#forms-new-prerelease-features}

#### Enhanced Visual Rule Editor for Core Component Based Adaptive Forms

This release brings a significant upgrade to the Visual Rule Editor for adaptive forms based on core components. You can now: 

   * Create rules in the Visual Rule Editor to [override the default form submission success/failure messages](/help/forms/create-and-use-custom-functions.md#use-case-override-form-submission-success-and-error-handlers). 

   * In the Adaptive Forms Rule Editor, added the ability to [select different types of fields for the WHEN operation](/help/forms/rule-editor-core-components.md#allowed-multiple-fields-in-when).

   * A form author can now apply custom functions to [preprocess data before submission](/help/forms/create-and-use-custom-functions.md#use-case-submit-altered-data-to-the-server). 

   * Use the [**Save as Draft**](/help/forms/save-core-component-based-form-as-draft.md) functionality to save partially completed forms for later submission. This functionality is useful in scenarios where users need to interrupt filling out a form and come back to it later.
 
### Early Access features in AEM Forms {#forms-new-early-access-features}

The AEM Forms Early Access Program program offers a unique opportunity to you to get exclusive access to cutting-edge innovations before anyone else, and help shape their development. The program offers access to multiple innovations. 

This release notes lists the innovations delivered in the current release. For the complete list of innovations available under the Early Access Program, see [AEM Forms Early Access Program documentation](/help/forms/early-access-ea-features.md). 

#### Enhanced bot protection methods

AEM Forms has enhanced its security features by adding support for two popular CAPTCHA solutions: Cloudflare Turnstile and hCaptcha. This functionality complements the existing Google reCAPTCHA, offering users additional options. It enhances flexibility in safeguarding their forms from bots and spam submissions.

* **Cloudflare Turnstile**: This frictionless CAPTCHA verifies users through a simple challenge that does not require explicit interaction. It seamlessly integrates into your forms, improving the user experience.
* **hCaptcha**: This privacy-focused CAPTCHA offers a user-friendly alternative with a focus on data privacy. It aims to strike a balance between security and user experience.
* **Google reCAPTCHA**: AEM Forms continue to support both reCAPTCHA v2 and reCAPTCHA Enterprise, offering a reliable and well-established solution.

By offering multiple CAPTCHA options, AEM Forms have empowered you to select the solution that best aligns with your specific needs. 

Ready to integrate any of these CAPTCHA solutions with your Adaptive Forms? Adobe's documentation provides detailed instructions for each: [Cloudflare Turnstile](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-core-components/create-an-adaptive-form-on-forms-cs/integrate-adaptive-forms-turnstile-core-components), [hCaptcha](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-core-components/create-an-adaptive-form-on-forms-cs/integrate-adaptive-forms-hcaptcha-core-components), and [Google reCAPTCHA](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-core-components/create-an-adaptive-form-on-forms-cs/captcha-adaptive-forms-core-components).


### Forms Service

Forms service generates interactive PDF forms for data capture. It can also be used to import or export data to and from an existing interactive PDF form and validate submitted data. Here's a breakdown of its functionalities: 

* **Rendering Forms**: Generate an interactive PDF form from a template created using AEM Forms Designer and, optionally, XML data. This functionality produces a fillable PDF form optionally pre-filled with data.
* **Data Extraction and Import**: Import data into an existing PDF form as well as extract data from a filled PDF form. Both XDP and XML data formats are supported, and importing to non-XFA PDF forms (also known as AcroForms) additionally supports FDF and XFDF data.
* **Data Validation**: Validate submitted data, in XDP or XML format, against a template created using AEM Forms Designer.

>[!IMPORTANT] 
>
> If you are interested in joining Adobe's Early Access Program for any early access innovation, simply send an email from your official address to [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com) to request access. You can request access to all or any specific innovation.  

     
## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### Content Health-Related Actions Center Notifications Early Adopter Program {#actions-center-notifications}

[Actions Center](/help/operations/actions-center.md) sends email notifications when important incidents happen, or if something is noticed about your code or configuration where you should take proactive action. Adobe has now introduced several new types of notifications associated with your content health. This feature is available through an early adopter program. To participate, please reach out to Adobe Customer Care.

#### Pages Contain a Large Number of Nodes {#page-nodes}

A large number of nodes can degrade rendering performance and reduce page load times. Receive a proactive notification through Actions Center when a large number of nodes are detected on a page, allowing you to take the necessary steps to reduce the total number of nodes within a page.

#### Large Number of Running Workflow Instances {#running-workflows}

The workflow engine performance is impacted when there is a large number of running workflows in the author environment. You receive a proactive notification through Actions Center when a large number of running workflow instances are detected. This process lets you configure a purge job to terminate unnecessary running workflows.

#### Users Added Directly to Custom Groups {#users-customgroups}

You receive a proactive notification through Actions Center when users are added directly to custom groups. This process lets you follow IMS best practices by adding users to relevant IMS groups and then including those IMS groups as members of AEM groups.

#### Missing JCR Content {#jcr-content}

Actions Center proactively notifies you when missing JCR content is detected. This approach lets you add the missing content and prevent the failure of certain AEM Assets features.

#### Completed Workflows Not Purged {#workflows}

Actions Center proactively notifies you when completed workflows over 90 days old have not been purged. This approach helps improve the performance of your workflow engine by reducing the number of workflow instances.

#### Missing Sling Resource {#sling-resource}

Actions Center proactively notifies you when a missing Sling resource is detected. This approach lets you add the missing resource and prevent the failure of certain AEM Assets features.

### Content Delivery-related Early Adopter Programs {#foundation-early-adopter}

Email **<aemcs-cdn-config-adopter@adobe.com>**, indicating which of the early adopter programs below you are interested in.

#### Basic Authentication at the CDN (Early Adopter Program) {#basicauth-cdn}

Protect certain content resources by popping up a basic auth dialog requiring a username and password. This feature primarily targets light authentication use cases, like business stakeholders reviewing content, rather than serving as a comprehensive solution for end-user access rights. The list of username and passwords in managed through a configuration file in git that is deployed via Configuration Pipeline, with a reference to secret-type Cloud Manager environment variables. [Learn more](/help/implementing/dispatcher/cdn-credentials-authentication.md#basic-auth).

#### Purge Content at the CDN With a Self-Serve API Key (Early Adopter Program) {#purge-cdn}

Register a CDN purge API key in a self-service way, and use it to invalidate content at the CDN, either globally, or for one or more resources. [Learn more](/help/implementing/dispatcher/cdn-cache-purge.md).  

<!-- Email **<aemcs-cdn-config-adopter@adobe.com>** with a request to be an early adopter. -->

#### Self-Serve Creation of X-AEM-Edge-Key for Customer-Managed CDN (BYOCDN) (Early Adopter Program) {#byocdn-keys}

Previously, a support ticket was needed to generate the X-AEM-Edge-Key required for configuration of a customer-managed CDN. This outcome can now be accomplished in a self-serve way through a configuration file that is deployed using the Configuration Pipeline, removing any delay in onboarding a new environment. [Learn more](/help/implementing/dispatcher/cdn-credentials-authentication.md#CDN-HTTP-value).

<!-- Email **<aemcs-cdn-config-adopter@adobe.com>** with a request to be an early adopter. -->

#### Client-Side Redirects (Early Adopter Program) {#client-side-redirects-early-adopter}

Configure 301/302 client-side redirects in source control, and deploy to the CDN. [Learn more](/help/implementing/dispatcher/cdn-configuring-traffic.md#client-side-redirectors).<!-- and join the early adopter program by emailing **<aemcs-cdn-config-adopter@adobe.com>**. --> Note that there are several other features already available related to [CDN configuration](/help/implementing/dispatcher/cdn-configuring-traffic.md), including request and response transformations, and routing traffic to off-AEM sites.

#### Traffic Filter Rules Alerts (Early Adopter Program) {#traffic-filter-rules-alerts-early-adopter}

The recently released [Traffic Filter Rules](/help/security/traffic-filter-rules-including-waf.md), which include the optionally licensable Web Application Firewall (WAF) rules, lets you configure what traffic should be allowed or denied. 

Join the early adopter program so you can be alerted whenever your traffic filter rules are triggered. Actions Center email notifications keep you informed when certain traffic conditions occur so you can take appropriate measures. 

#### Business Users Can Declare Redirects Outside of Git (Early Adopter Program) {#apache-rewritemaps-early-adopter}

Similar to AEM 6.5, Apache/dispatcher ingest rewrite maps placed in a specific location in the publish repository, and load them, without requiring a web tier pipeline execution. This approach let business users declare redirects using a spreadsheet or a UI, like ACS Commons Redirect Map Manager or a custom application. <!-- Please reach out to **<aemcs-cdn-config-adopter@adobe.com>** for more information. -->

#### Edge Side Includes (ESI) for Loading Dynamic Content (Early Adopter Program) {#esi-early-adopter}

The Adobe Managed CDN now supports [Edge Side Includes (ESI)](/help/implementing/dispatcher/edge-side-includes.md), a markup language for edge level dynamic web content assembly. By including ESI snippets, you can cache the overall HTML page at the CDN with higher TTLs, while more frequently fetching from origin those smaller sections that require higher cadence updates (lower TTLs). <!--Please reach out to **<aemcs-cdn-config-adopter@adobe.com>** for more information.-->

## [!DNL Experience Manager] Guides {#guides}

You can find a complete list of new and enhanced features of the latest release of Adobe Experience Manager Guides [here](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/release-notes/cloud-release-notes/2024-releases/2406-release/whats-new-2024-06-0).

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes/current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).

## Universal Editor {#universal-editor}

You can find a complete list of Universal Editor releases [here](/help/release-notes/universal-editor/current.md).

## Generate Variations {#generate-variations}

You can find a complete list of Generate Variations releases [here](/help/generative-ai/release-notes-generate-variations.md).

## Experience Cloud Release Notes {#experience-cloud}

You can find information about releases of other Experience Cloud applications [here](https://experienceleague.adobe.com/en/docs/release-notes/experience-cloud/current).
