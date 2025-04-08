---
title: Release Notes for 2024.9.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2024.9.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 75ecd154-112a-4468-9962-de50bb1f4cd0
---
# 2024.9.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2024.9.0 version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions such as 2022 or 2023.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>To receive a monthly email notification about updates to Experience Cloud release notes, subscribe to the [Adobe Priority Product Update](https://www.adobe.com/subscription/priority-product-update.html).

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2024.9.0) is September 26, 2024. The next feature release (2024.10.0) is planned for October 31, 2024.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Release Video {#release-video}

Have a look at the September 2024 Release Overview video for a summary of the features added in the 2024.9.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3434847?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New feature in Experience Manager Sites {#new-feature-sites}

#### Translation Management {#translation-management}

AEM translation workflows and API actions now trigger events to provide insight about translation job state changes. Users can subscribe to these events through the Adobe Developer Console. See [here](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/translation/) for more information on the AEM Translation Management API. 

### Early Adopter Program {#sites-early-adopter}

**Generate Variations**

Leverage GenAI through AEM's new feature, [generate variations](/help/generative-ai/generate-variations.md), accessible now in Cloud Service. Generate variations helps you generate and scale content creation through the use of generative AI. Reach out to your Adobe account team for consideration in the program.


## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### Early access feature in Dynamic Media {#dm-early-access}

**AI-generated video captions** 

AI-generated video captions in Adobe Dynamic Media use artificial intelligence to generate captions automatically for video content. This feature is designed to improve accessibility and enhance the user experience by providing accurate, real-time captions. The AI analyzes the video's audio track to transcribe speech and create captions, which can be edited for accuracy or customization. These captions help meet accessibility requirements and improve video engagement for audiences who rely on or prefer text-based video support. 

To get early access to AI-generated captions support on your Dynamic Media account, [create and submit an Adobe Customer Support case](/help/assets/dynamic-media/video.md##enable-dash).  

### New features in Asset Selector {#asset-selector-new-features}

Asset Selector now supports browsing Collections to find your desired asset.
![Asset selector collections](/help/assets/assets/collections-rail-modal-view.png)

### New features in Content Hub {#content-hub-new-features}

Administrators can now control if they need expired assets to be visible on Content Hub. If the expired assets are made visible, they can also define if users can download them.

![Expired assets on Content Hub](/help/assets/assets/view-download-expired-assets.png)

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New Pre-release features in AEM Forms {#forms-new-prerelease-features}

#### Auto-save a draft for Core Components based Adaptive Forms

Users can now benefit from an auto-save feature that saves a partially completed form as a draft automatically. They can return later to finish filling it out on the same or other device. This feature improves conversion rates for organizations by reducing form abandonment, as users do not need to start over form filling from the beginning.

 
### Early Access features in AEM Forms {#forms-new-early-access-features}

The AEM Forms Early Access Program program offers a unique opportunity to you to get exclusive access to cutting-edge innovations, and help shape their development.

This release notes lists the innovations delivered in the current release. For the complete list of innovations available under the Early Access Program, see [AEM Forms Early Access Program documentation](/help/forms/early-access-ea-features.md). 

#### AEM Forms AI Assistant

Generative AI for Adaptive Forms brings a whole new level of power and ease to your forms development processes. It allows you to build better forms faster than ever before. 

![Generative AI Assistant, Adaptive Forms](/help/forms/assets/generative-ai-assistant.png)

The Generative AI capabilities on offer are: 

* **AI Assistant for Product Queries**: Get instant answers to your AEM form-related questions. The AI assistant acts as your own personal knowledge base, providing insightful guidance and recommendations directly within the platform.

* **Adaptive Form Generation**: Effortlessly create full-fledged forms with generative AI prompts. Adobe's generative AI automatically generates user-friendly forms that reduce drop-offs and personalize the experience.

* **Panel Generation for Forms**: Generate form sections tailored to specific data collection needs. For example, generate sections for collecting payment information, customer preferences, or travel details.

* **Changing Form Layouts**: Experiment with different layouts and designs using generative AI prompts. Try out different layouts like wizard or tabbed views to find the perfect fit for your form. Use generative AI prompts to optimize your forms for mobile responsiveness and create visually engaging forms that users love.

* **Configure Submit Action**: Use generative AI prompts to configure a submit action effortlessly for your form. Choose from a library of pre-built submit actions or custom submit actions created and deployed by your development team.

>[!IMPORTANT] 
>
> Interested in joining the Early Access Program for any Forms innovation? Send an email from your official address to [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com) with the list of capabilities that you are interested in.

## CIF Add-on {#cloud-services-cif}

### Improvements {#improvements-fixes-cif}

* Make category limit customizable.

### Bug fixes {#bug-fixes-cif}

* Commerce fields are not properly integrated with the Assets Metadata Schema editor.
* Issue with Carousel Products Multifield for Drag & Drop.
* Issue with Carousel Category Multifield for Drag & Drop.
* On-click doesn't work for the menus in the Page information on the category & product editor page.
* Order Number is not visible in the Order Confirmation Page.

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### Edge Side Includes (ESI) for Loading Dynamic Content {#esi}

The Adobe Managed CDN now supports [Edge Side Includes (ESI)](/help/implementing/dispatcher/edge-side-includes.md), a markup language for edge level dynamic web content assembly. By including ESI snippets, you can cache the overall HTML page at the CDN with higher TTLs, while more frequently fetching from origin those smaller sections that require higher cadence updates (lower TTLs). This feature will be rolled out gradually.

### Basic Authentication at the CDN {#basicauth-cdn}

Protect certain content resources by popping up a basic auth dialog requiring a username and password. This feature primarily targets light authentication use cases, like business stakeholders reviewing content, rather than serving as a comprehensive solution for end-user access rights. The list of username and passwords is managed through a configuration file in Git that is deployed via Config Pipeline, with a reference to secret-type Cloud Manager environment variables. [Learn more](/help/implementing/dispatcher/cdn-credentials-authentication.md#basic-auth).

### Client-Side Redirects {#client-side-redirects}

Declare [browser redirects](/help/implementing/dispatcher/cdn-configuring-traffic.md#client-side-redirectors) in a configuration file Git that are deployed to and evaluated at the CDN. This can be useful for scenarios including deleting pages, changed site structure, and SEO optimization.

### New AEM Developer Console (Public Beta) {#aem-developer-console-beta}

Try out a revamped [AEM Developer Console](/help/implementing/developing/introduction/aem-developer-console.md), which offers a more interactive experience for debugging code in Cloud environments.

Anyone can access the public beta by clicking the *New Console Available* button in the current AEM Developer Console. Adobe welcomes feedback, which you can email to **<aemcs-new-devconsole-ui-beta@adobe.com>**.

![OSGi Bundles Screen in AEM Developer Console](/help/implementing/developing/introduction/assets/osgi-bundles.png)

### Business Users Can Declare Redirects Outside of Git (Early Adopter Program) {#apache-rewritemaps-early-adopter}

Similar to AEM 6.5, Apache/dispatcher ingests rewrite maps placed in a specific location in the publish repository, and loads them without requiring a web tier pipeline execution. This approach lets business users declare redirects using a spreadsheet or a UI, like ACS Commons Redirect Map Manager or a custom application. Join the early adopter program by emailing **<aemcs-cdn-config-adopter@adobe.com>**.

### Config Pipeline for RDEs (Early Adopter Program) {#config-pipeline-rdes-early-adopter}

The [Config Pipeline](/help/operations/config-pipeline.md) is used to deploy yaml file configurations, including CDN options (traffic filter rules, request/response transformations, and so on). Join the early adopter program by emailing **<aemcs-cdn-config-adopter@adobe.com>** to deploy these same configurations to RDEs (Rapid Development Environments), which use a CLI.

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
