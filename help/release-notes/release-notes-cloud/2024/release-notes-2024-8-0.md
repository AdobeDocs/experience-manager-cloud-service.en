---
title: Release Notes for 2024.8.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2024.8.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
feature: Release Information
role: Admin
exl-id: dd1d4b8f-8331-4e97-a754-37e720974db6
---
# 2024.8.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2024.8.0 version of [!DNL Experience Manager] as a Cloud Service.

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

>[!VIDEO](https://video.tv.adobe.com/v/3433381?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New feature in Experience Manager Sites {#new-feature-sites}

**AEM Authoring for Edge Delivery Services**

Existing Sites [inheritance](/help/sites-cloud/authoring/universal-editor/inheritance.md) functionality is now supported including:

* [AEM Launches](/help/sites-cloud/authoring/launches/overview.md)
* [MSM](/help/sites-cloud/administering/msm/overview.md) at the page level

In addition, the following page management features are now supported:

* [AEM Tags](/help/sites-cloud/authoring/sites-console/tags.md) can be exported as a [taxonomy](/help/edge/wysiwyg-authoring/taxonomy.md) to Edge Delivery Services.
* [Templates](/help/sites-cloud/authoring/universal-editor/templates.md) for Edge Delivery Services are coming soon!

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

### New Pre-release features in AEM Forms {#forms-new-prerelease-features}

#### Auto-save a draft for Core Components based Adaptive Forms

Users can now benefit from an auto-save feature that saves a partially completed form as a draft automatically. They can return later to finish filling it out on the same or other device. This feature improves conversion rates for organziations by reducing form abandonment, as users do not need to start over form filling from the beginning.

 
### Early Access features in AEM Forms {#forms-new-early-access-features}

The AEM Forms Early Access Program program offers a unique opportunity to you to get exclusive access to cutting-edge innovations, and help shape their development.

This release notes lists the innovations delivered in the current release. For the complete list of innovations available under the Early Access Program, see [AEM Forms Early Access Program documentation](/help/forms/early-access-ea-features.md). 

#### AEM Forms AI Assistant

Generative AI for Adaptive Forms brings a whole new level of power and ease to your forms development processes. It allows you to build better forms faster than ever before. 

![Generative AI Assistant, Adaptive Forms](/help/forms/assets/generative-ai-assistant.png)

The Generative AI capabilities on offer are: 

* **AI Assistant for Product Queries**: Get instant answers to your AEM form-related questions. The AI assistant acts as your own personal knowledge base, providing insightful guidance and recommendations directly within the platform.

* **Adaptive Form Generation**: Effortlessly create full-fledged forms with Generative AI Prompts. Our Generative AI automatically generates user-friendly forms that reduce drop-offs and personalize the experience.

* **Panel Generation for Forms**: Generate form sections tailored to specific data collection needs. For example, generate sections for collecting payment information, customer preferences, or travel details.

* **Changing Form Layouts**: Experiment with different layouts and designs using Generative AI Prompts. Try out different layouts like wizard or tabbed views to find the perfect fit for your form. Use Generative AI Prompts to optimize your forms for mobile responsiveness and create visually engaging forms that users love.

* **Configure Submit Action**: Use Generative AI prompts to effortlessly configure a submit action for your form. Choose from a library of pre-built submit actions or from a list of custom submit actions, created and deployed by your own development team.

>[!IMPORTANT] 
>
> If you are interested in joining the Early Access Program for any innovation, simply send an email from your official address to [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com) with the list of capabilities you are interested in.


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

You can find a complete list of new and enhanced features of the latest release of Adobe Experience Manager Guides [here](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap).

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
