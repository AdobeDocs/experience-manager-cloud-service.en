---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current release notes for [!DNL Adobe Experience Manager] as a Cloud Service.
mini-toc-levels: 1
exl-id: a2d56721-502c-4f4e-9b72-5ca790df75c5
feature: Release Information
role: Admin
---
# Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the current (latest) version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions such as 2022 or 2023.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>To receive a monthly email notification about updates to Experience Cloud release notes, subscribe to the [Adobe Priority Product Update](https://www.adobe.com/subscription/priority-product-update.html).

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2024.8.0) is August 29, 2024. The next feature release (2024.9.0) is planned for September 26, 2024.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Release Video {#release-video}

Have a look at the August 2024 Release Overview video for a summary of the features added in the 2024.8.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3431707?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New feature in Experience Manager Sites {#new-feature-sites}

**AEM Authoring for Edge Delivery Services**

Existing Sites [inheritance](/help/sites-cloud/authoring/universal-editor/inheritance.md) functionality is now supported including:

* [AEM Launches](/help/sites-cloud/authoring/launches/overview.md)
* [MSM](/help/sites-cloud/administering/msm/overview.md) at the page level

In addition, the following page management features are now supported:

* [AEM Tags](/help/sites-cloud/authoring/sites-console/tags.md) can be exported as a [taxonomy](/help/edge/wysiwyg-authoring/taxonomy.md) to Edge Delivery Services.
* [Templates](/help/edge/wysiwyg-authoring/templates.md) for Edge Delivery Services are coming soon!

### Early Adopter Program {#sites-early-adopter}

**Generate Variations**

Leverage GenAI through AEM's new feature, [generate variations](/help/generative-ai/generate-variations.md), accessible now in Cloud Service. Generate variations helps you generate and scale content creation through the use of generative AI. Reach out to your Adobe account team for consideration in the program.


## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in Assets view {#assets-view-new-features}

**Updated Adobe Firefly Image Generation**

Assets as a Cloud Service now uses the latest widget from Firefly that allows you to generate images in different styles using Adobe Firefly. By defining its style, composition, dimensions, and more, using the in-built Firefly editor, you can quickly create & save the assets you need directly within the AEM Assets repository for immediate use.

![Adobe Firefly image generation](/help/assets/assets/bugatti-type-57.png)

**PSB file support**

Assets as a Cloud Service now supports Photoshop large documents (PSB files) in addition to the existing PSD file support.

### New enhancements in Content Hub {#content-hub-new-enhancements}

* Better handling of long filenames, easy expansion of complete name via tooltip.
* Improved thumbnails to better fit content aspect ratio and cover larger area of content.
* Custom thumbnail experience from AEM supported with content hub.
* Improvements in colour search.
* Improvements in configurations save experience.
* Improved info page of collections to reflect creator name.


## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features in AEM Forms {#forms-new-prerelease-features}

#### Enhanced Visual Rule Editor for Core Component Based Adaptive Forms

Adaptive form authors can use repeatable form fields in out of the box functions available in visual rule editor for core components to build complex business logic in the forms, without requiring customization or development team's assistance.
 
### Early Access features in AEM Forms {#forms-new-early-access-features}

The AEM Forms Early Access Program program offers a unique opportunity to you to get exclusive access to cutting-edge innovations before anyone else, and help shape their development. The program offers access to multiple innovations. 

This release notes lists the innovations delivered in the current release. For the complete list of innovations available under the Early Access Program, see [AEM Forms Early Access Program documentation](/help/forms/early-access-ea-features.md). 

#### Author adaptive forms using Universal Editor

Leverage the Adobe Experience Manager [Universal Editor](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/introduction) to create adaptive forms using WYSIWYG drag-drop authoring, for both headless and headful enrollment experiences, delivered via Edge Delivery Service. Adaptive form authors can easily create and launch experiments for variations of the forms in the web pages and determine the best performing experiences for end users.

>[!IMPORTANT] 
>
> If you are interested in joining Adobe's Early Access Program for any early access innovation, simply send an email from your official address to [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com) to request access. You can request access to all or any specific innovation.  

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### Content Delivery-related Early Adopter Programs {#foundation-early-adopter}

Email **<aemcs-cdn-config-adopter@adobe.com>**, indicating which of the early adopter programs below you are interested in.

#### Basic Authentication at the CDN (Early Adopter Program) {#basicauth-cdn}

Protect certain content resources by popping up a basic auth dialog requiring a username and password. This feature primarily targets light authentication use cases, like business stakeholders reviewing content, rather than serving as a comprehensive solution for end-user access rights. The list of username and passwords in managed through a configuration file in git that is deployed via Configuration Pipeline, with a reference to secret-type Cloud Manager environment variables. [Learn more](/help/implementing/dispatcher/cdn-credentials-authentication.md#basic-auth).

#### Client-Side Redirects (Early Adopter Program) {#client-side-redirects-early-adopter}

Configure 301/302 client-side redirects in source control, and deploy to the CDN. [Learn more](/help/implementing/dispatcher/cdn-configuring-traffic.md#client-side-redirectors).<!-- and join the early adopter program by emailing **<aemcs-cdn-config-adopter@adobe.com>**. --> Note that there are several other features already available related to [CDN configuration](/help/implementing/dispatcher/cdn-configuring-traffic.md), including request and response transformations, and routing traffic to off-AEM sites.

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
