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


**Real User Monitoring (RUM) Data Service**

* **[You can leverage the Real User Monitoring (RUM) Data Service](/help/implementing/cloud-manager/content-requests.md#real-user-monitoring-for-aem-as-a-cloud-service)** to enable client-side collection for AEM as a Cloud Service.
Real User Monitoring (RUM) Data Service offers a more precise reflection of user interactions, ensuring a reliable measure of website engagement. It is a great opportunity to gain advanced insights into your page performance. While this is beneficial for customers who use either Adobe-managed CDN or non-Adobe-managed CDN. Additionally, for customers using a non-Adobe managed CDN, automated traffic reporting can now be enabled for them, thus removing the need to share any traffic report with Adobe.

   If you are interested in testing this new feature and sharing your feedback, please send an email to `aemcs-rum-adopter@adobe.com`, along with your domain name for each of the environments that you would like to enable RUM for from your email address associated with your Adobe ID. Adobe's product team will then enable the Real User Monitoring (RUM) Data Service for you.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

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

  * Create rules in Visual Rule editor to [override default form submission success/failure handlers](/help/forms/rule-editor-core-components.md). 
  
  * In the Adaptive Forms Rule Editor, added the ability to [select different types of fields for the WHEN operation](/help/forms/rule-editor-core-components.md).
  
  * A form author can now apply custom functions to [preprocess data before submission](/help/forms/rule-editor-core-components.md). 

  * Use the **Save as Draft** functionlaity to save partially completed forms for later submission. This is useful in scenarios where users need to interrupt filling out a form and come back to it later.

 

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

if you're interested in joining our Early Adopter program for any early adopter innovation, simply send an email from your official address to [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com) to request access. You can request access to all or any specific innovation.  


### Forms Service

Forms Service acts as an engine that takes form designs and data, and generates interactive PDF forms for users for data capture purposes. It can also extract the filled information and integrate it with other systems. Here's a breakdown of its functionalities:

* **Rendering Forms**: It can render PDF forms based on templates you design in AEM Forms Designer and data stored in XML format. This essentially creates an interactive fillable form from the static template.
* **Data Extraction and Import**: The Forms Service can both extract data filled out in a PDF form and import data into existing PDF forms. The data is typically formatted in XML for processing.
* **Fragment-Based Rendering**: It allows you to render forms partially, based on specific sections or fragments designed in AEM Forms Designer. This can be useful for building modular forms or dynamically showing sections based on user input.

     
## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### OAuth Server-to-Server credentials support for AEM integrations with other Adobe solutions {#S2S-OAuth-credentials}

Adobe Developer Console is used to generate credentials to access various APIs. One of those credential types, Service Account (JWT) credentials, has been deprecated in favor of OAuth Server-to-Server credentials, which AEM Cloud Service now supports for integrations with other Adobe solutions such as Adobe Analytics and Adobe Target.

[Read about the deprecation](/help/security/jwt-credentials-deprecation-in-adobe-developer-console.md) and [learn how to use the AEM author UI](/help/security/setting-up-ims-integrations-for-aem-as-a-cloud-service.md) to configure integrations with other Adobe solutions. 

### Traffic Spike at Origin Alerts {#traffic-spike-origin}

Receive proactive notifications when traffic patterns at the origin are indicative of a DDoS attack, allowing you to investigate and configure [traffic filter rules](/help/security/traffic-filter-rules-including-waf.md).

### RDE support for front-end code using Site Themes and Site Templates {#rde-frontend}

[Rapid Development Environments (RDEs)](/help/implementing/developing/introduction/rapid-development-environments.md) now support front-end code based on [site themes](/help/sites-cloud/administering/site-creation/site-themes.md) and [site templates](/help/sites-cloud/administering/site-creation/site-templates.md), for early adopters. With RDEs, this is done using a command line directive, rather than a [front-end pipeline](/help/sites-cloud/administering/site-creation/enable-front-end-pipeline.md).

### Enhanced logging for RDEs {#rde-logging}

While debugging code in a [Rapid Development Environment (RDE)](/help/implementing/developing/introduction/rapid-development-environments.md), developers can now configure and stream logs more efficiently, using the command line, and without modifying OSGI properties in version control. Features include:

* declare log levels on a per package or class level
* customize the log output format
* stream multiple logs in parallel 

### RDE CLI enhancements {#rde-cli-enhancements}

The [Rapid Development Environment (RDE)](/help/implementing/developing/introduction/rapid-development-environments.md) command line interface has some new features, which improve the developer experience:

* the setup command is interactive, making it easier to choose between organizations, programs and environments. It is also now possible to override these values at the command line 
* quiet mode
* json mode

### Early Adopter Programs {#foundation-early-adopter}

Email **<aemcs-cdn-config-adopter@adobe.com>**, indicating which of the early adopter programs below you are interested in.

#### Purge content at the CDN with a self-serve API key (Early Adopter Program) {#purge-cdn}

Register a CDN purge API key in a self-service way, and use it to invalidate content at the CDN, either globally, or for one or more resources.  

<!-- Email **<aemcs-cdn-config-adopter@adobe.com>** with a request to be an early adopter. -->

#### Self-serve creation of X-AEM-Edge-Key for BYOCDN (Early Adopter Program) {#purge-cdn-2}

Previously, a support ticket was needed to generate the X-AEM-Edge-Key required for configuration of a customer-managed CDN. This can now be accomplished in a self-serve way through a configuration file that is deployed using the Configuration Pipeline, removing any delay in onboarding a new environment.  

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

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes/current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
