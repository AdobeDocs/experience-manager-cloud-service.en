---
title: Release Notes for 2024.5.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2024.5.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
---
# 2024.5.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2024.5.0 version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions such as 2022 or 2023.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2024.5.0) is May 30, 2024. The next feature release (2024.6.0) is planned for June 27, 2024.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Release Video {#release-video}

Have a look at the May 2024 Release Overview video for a summary of the features added in the 2024.5.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3429503?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features in Sites {#sites-new-features}

**AEM Authoring for Edge Delivery Services**

Enhanced stability and various improvements for a better authoring experience.

### Early Adopter Program {#sites-early-adopter}

**Generate Variations**

Leverage GenAI through AEM's new feature, [generate variations](/help/generative-ai/generate-variations.md), accessible now in Cloud Service. Generate variations helps you generate and scale content creation through the use of generative AI. Reach out to your Adobe account team for consideration in the program.

**Asset browsing in Content Fragment Console**

Content authors can now browse, view, and take actions on images, and other assets without having to leave the Content Fragment Console. 

 ![Asset Browsing](/help/sites-cloud/administering/content-fragments/assets/cf-console-assets-browse.png)

Interested in trying out the feature and sharing feedback? Send an email to aemcs-headless-adopter@adobe.com from your official email ID to learn more about the early adopter program.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in Admin view {#admin-view-new-features}

* WebM is now a supported output file in processing profile for video.
* MP4 is now supported in the native integration of AEM in Express (import and export).

### New features in Assets view {#assets-view-new-features}

**Publish assets to AEM and Dynamic Media**

Experience Manager Assets now enables you to quickly [publish assets to Experience Manager and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md) using the Assets view without switching to the Admin view. You can publish assets while uploading, browsing, and searching assets.

![check publish status1](/help/assets/assets/check-publish-status1.png)

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

<!-- 

* **Configure a shard for Adobe Sign for AEM Forms**: Adobe distributes Acrobat Sign API around the globe in many deployment units called "shards." Each shard serves a customer's account, such as NA1, NA2, NA3, EU1, JP1, AU1, IN1, and others. The shard names correspond to geographic locations. You can now use more than one shard while using Adobe Sign integration with AEM Forms. 

--> 

### New pre-release features in AEM Forms {#forms-new-prerelease-features}

#### Enhanced Visual Rule Editor for Core Component Based Adaptive Forms

This release brings a significant upgrade to the visual rule editor for adaptive forms based on core components. You can now: 

  * Create rules in Visual Rule editor to [override default form submission success/failure handlers](/help/forms/create-and-use-custom-functions.md#field-and-global-scope-objects-in-custom-functions). 
  
  * In the Adaptive Forms Rule Editor, added the ability to [select different types of fields for the WHEN operation](/help/forms/rule-editor-core-components.md#allowed-multiple-fields-in-when).
  
  * A form author can now apply custom functions to [preprocess data before submission](/help/forms/create-and-use-custom-functions.md#field-and-global-scope-objects-in-custom-functions). 

  * Use the [**Save as Draft**](/help/forms/save-core-component-based-form-as-draft.md) functionality to save partially completed forms for later submission. This is useful in scenarios where users need to interrupt filling out a form and come back to it later.

 

### Early Adopter features in AEM Forms {#forms-new-early-adopter-features} 

The AEM Forms Early Adopter Program program offers a unique opportunity to you to get exclusive access to cutting-edge innovations before anyone else, and help shape their development. 
The program offers access to multiple innovations. 

This release notes lists the innovations delivered in current release. For the complete list of innovations available under the Early Adopter Program, see [AEM Forms Early Adopter Program documentation](/help/forms/early-adopter-ea-features.md). 

#### Enhanced bot protection methods

AEM Forms has enhanced its security features by adding support for two popular CAPTCHA solutions: Cloudflare Turnstile and hCaptcha. This adds to the already available Google reCAPTCHA, providing users with more choice and flexibility in protecting their forms from bots and spam submissions.

* **Cloudflare Turnstile**: This frictionless CAPTCHA verifies users through a simple challenge that doesn't require explicit interaction. It seamlessly integrates into your forms, improving the user experience.
* **hCaptcha**: This privacy-focused CAPTCHA offers a user-friendly alternative with a focus on data privacy. It aims to strike a balance between security and user experience.
* **Google reCAPTCHA**: AEM Forms continue to support both reCAPTCHA v2 and reCAPTCHA Enterprise, offering a reliable and well-established solution.

By offering multiple CAPTCHA options, AEM Forms have empowered you to select the solution that best aligns with your specific needs. 

Ready to integrate any of these CAPTCHA solution with your Adaptive Forms? Our documentation provides detailed instructions for each: [Cloudflare Turnstile](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-core-components/create-an-adaptive-form-on-forms-cs/integrate-adaptive-forms-turnstile-core-components), [hCaptcha](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-core-components/create-an-adaptive-form-on-forms-cs/integrate-adaptive-forms-hcaptcha-core-components), and [Google reCAPTCHA](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-core-components/create-an-adaptive-form-on-forms-cs/captcha-adaptive-forms-core-components).


### Forms Service

Forms service generates interactive PDF forms for data capture. It can also be used to importor  export data to and from an existing interactive PDF form and validate submitted data. Here's a breakdown of its functionalities: 

* **Rendering Forms**: Generate an interactive PDF form from a template created using AEM Forms Designer and, optionally, XML data. This essentially produces a fillable PDF form optionally pre-filled with data.
* **Data Extraction and Import**: Import data into an existing PDF form as well as extract data from a filled PDF form. Both XDP and XML data formats are supported, and importing to non-XFA PDF forms (also known as AcroForms) additionally supports FDF and XFDF data.
* **Data Validation**: : Validate submitted data, in XDP or XML format, against a template created using AEM Forms Designer.

>[!IMPORTANT] 
>
> If you're interested in joining our Early Adopter program for any early adopter innovation, simply send an email from your official address to [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com) to request access. You can request access to all or any specific innovation.  

     
## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### OAuth Server-to-Server credentials support for AEM integrations with other Adobe solutions {#S2S-OAuth-credentials}

Adobe Developer Console is used to generate credentials to access various APIs. One of those credential types, Service Account (JWT) credentials, has been deprecated in favor of OAuth Server-to-Server credentials, which AEM Cloud Service now supports for integrations with other Adobe solutions such as Adobe Analytics and Adobe Target.

[Read about the deprecation](/help/security/jwt-credentials-deprecation-in-adobe-developer-console.md) and [learn how to use the AEM author UI](/help/security/setting-up-ims-integrations-for-aem-as-a-cloud-service.md) to configure integrations with other Adobe solutions. 

### Traffic Spike at Origin Alerts {#traffic-spike-origin}

[Receive proactive notifications](/help/security/traffic-filter-rules-including-waf.md#traffic-spike-at-origin-alert) through Actions Center when traffic patterns at the origin are indicative of a DDoS attack, allowing you to investigate and configure traffic filter rules.

### New Features for RDEs {#RDE-new-features}

[Rapid Development Environments (RDEs)](/help/implementing/developing/introduction/rapid-development-environments.md) let developers swiftly deploy, review, and test changes in the Cloud. Several new features will be rolled out during the month of June. We also invite you to engage directly with Adobe engineering at the [RDE Discord channel](https://discord.com/channels/1131492224371277874/1245304281184079872).


#### RDE support for front-end code using Site Themes and Site Templates {#rde-frontend}

[RDEs now support front-end code](/help/implementing/developing/introduction/rapid-development-environments.md#deploying-themes-to-rde) based on [site themes](/help/sites-cloud/administering/site-creation/site-themes.md) and [site templates](/help/sites-cloud/administering/site-creation/site-templates.md), for early adopters. With RDEs, this is done using a command line directive, rather than a [front-end pipeline](/help/sites-cloud/administering/site-creation/enable-front-end-pipeline.md).

#### Enhanced logging for RDEs {#rde-logging}

While debugging code in an RDE, developers can now [configure and stream logs more productively](/help/implementing/developing/introduction/rapid-development-environments.md#rde-logging), using the command line, and without modifying OSGI properties in version control. Features include:

* declaring log levels on a per package or class level
* customizing the log output format
* streaming multiple logs in parallel 

#### RDE CLI enhancements {#rde-cli-enhancements}

The RDE command line interface has some new features, which improve the developer experience:

* [the setup command is interactive](/help/implementing/developing/introduction/rapid-development-environments.md#installing-the-rde-command-line-tools-interactive), making it easier to choose between organizations, programs and environments. It is also now possible to override these values at the command line.
* [quiet mode](/help/implementing/developing/introduction/rapid-development-environments.md#global-flags) for a less verbose output.
* [json mode](/help/implementing/developing/introduction/rapid-development-environments.md#global-flags) for useful output when invoked programatically. 

### New Actions Center notifications {#actions-center-notifications}

[Actions Center](/help/operations/actions-center.md) sends email notifications when important incidents happen, or if we notice something about your code or configuration where you should take proactive action. There are three new types of notification:

* too many outgoing connections through advanced networking infrastructure
* usage of a deprecated Service User Mapping format
* a potential DDoS attack is underway

### Early Adopter Programs {#foundation-early-adopter}

Email **<aemcs-cdn-config-adopter@adobe.com>**, indicating which of the early adopter programs below you are interested in.

#### Purge content at the CDN with a self-serve API key (Early Adopter Program) {#purge-cdn}

Register a CDN purge API key in a self-service way, and use it to invalidate content at the CDN, either globally, or for one or more resources. [Learn more](/help/implementing/dispatcher/cdn-cache-purge.md).  

<!-- Email **<aemcs-cdn-config-adopter@adobe.com>** with a request to be an early adopter. -->

#### Self-serve creation of X-AEM-Edge-Key for customer-managed CDN (BYOCDN) (Early Adopter Program) {#byocdn-keys}

Previously, a support ticket was needed to generate the X-AEM-Edge-Key required for configuration of a customer-managed CDN. This can now be accomplished in a self-serve way through a configuration file that is deployed using the Configuration Pipeline, removing any delay in onboarding a new environment. [Learn more](/help/implementing/dispatcher/cdn-credentials-authentication.md#CDN-HTTP-value).

<!-- Email **<aemcs-cdn-config-adopter@adobe.com>** with a request to be an early adopter. -->

#### Client-side redirects (Early Adopter Program) {#client-side-redirects-early-adopter}

Configure 301/302 client-side redirects in source control, and deploy to the CDN. [Learn more](/help/implementing/dispatcher/cdn-configuring-traffic.md#client-side-redirectors).<!-- and join the early adopter program by emailing **<aemcs-cdn-config-adopter@adobe.com>**. --> Note that there are several other features already available related to [CDN configuration](/help/implementing/dispatcher/cdn-configuring-traffic.md), including request and response transformations, and routing traffic to off-AEM sites.

#### Traffic Filter Rules Alerts (Early Adopter Program) {#traffic-filter-rules-alerts-early-adopter}

The recently released [Traffic Filter Rules](/help/security/traffic-filter-rules-including-waf.md), which include the optionally licensable Web Application Firewall (WAF) rules, lets you configure what traffic should be allowed or denied. 

Join the early adopter program so you can be alerted whenever your traffic filter rules are triggered. Actions Center email notifications will keep you informed when certain traffic conditions occur so you can take appropriate measures. 

#### Business users can declare redirects outside of Git (Early Adopter Program) {#apache-rewritemaps-early-adopter}

Similar to AEM 6.5, Apache/dispatcher will ingest rewrite maps placed in a specific location in the publish repository, and load them, without requiring a web tier pipeline execution. This opens up opportunities for a business user to declare redirects using either a spreadsheet or a UI, such as that offered by ACS Commons Redirect Map Manager or created as part of a customer application. <!-- Please reach out to **<aemcs-cdn-config-adopter@adobe.com>** for more information. -->

#### Edge Side Includes (ESI) for Loading Dynamic Content (Early Adopter Program) {#esi-early-adopter}

The Adobe Managed CDN now supports [Edge Side Includes (ESI)](/help/implementing/dispatcher/edge-side-includes.md), a markup language for edge level dynamic web content assembly. By including ESI snippets, you can cache the overall HTML page at the CDN with higher TTLs, while more frequently fetching from origin those smaller sections that require higher cadence updates (lower TTLs). <!--Please reach out to **<aemcs-cdn-config-adopter@adobe.com>** for more information.-->

#### Real User Monitoring (RUM) Data Service (Early Adopter Program)

* **[Real Use Monitoring (RUM) Data Service is now GA](/help/implementing/cloud-manager/content-requests.md#real-user-monitoring-for-aem-as-a-cloud-service)** enabling client-side collection of data for AEM as a Cloud Service.
The Real Use Monitoring service , the client-side collection, offers a more precise reflection of interactions, ensuring a reliable measure of website engagement. It enables customers with advanced insights into their page traffic and performance. It is a great opportunity to learn more about your page performance and gain insights to improve it.

## [!DNL Experience Manager] Guides {#guides}

You can find a complete list of new and enhanced features of the latest release of Adobe Experience Manager Guides [here](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/release-notes/cloud-release-notes/2024-releases/2404-release/whats-new-2024-04-0).

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes/current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).

## Experience Cloud Release Notes {#experience-cloud}

You can find information about releases of other Experience Cloud applications [here](https://experienceleague.adobe.com/en/docs/release-notes/experience-cloud/current).
To receive a monthly email notification about updates to Experience Cloud release notes, subscribe to the [Adobe Priority Product Update](https://www.adobe.com/subscription/priority-product-update.html). 
