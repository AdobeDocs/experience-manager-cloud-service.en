---
title: Release Notes for 2024.10.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2024.10.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 7a63f04f-10f0-4879-bd06-4182bb288a9b
---
# 2024.10.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2024.10.0 version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions such as 2022 or 2023.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>To receive a monthly email notification about updates to Experience Cloud release notes, subscribe to the [Adobe Priority Product Update](https://www.adobe.com/subscription/priority-product-update.html).

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2024.10.0) is October 31, 2024. The next feature release (2024.11.0) is planned for November 21, 2024.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Release Video {#release-video}

Have a look at the October 2024 Release Overview video for a summary of the features added in the 2024.10.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3440501?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

**Modernized Page Events**

The following AEM Sites page events are now available as externally consumable events that are based on the AEM as a Cloud Service Eventing Platform. The events can be processed via Adobe I/O to interact with external processes. 
* Page published
* Page unpublished
* Page deleted

### Early Adopter Program {#sites-early-adopter}

**Generate Variations**

Leverage GenAI through AEM's new feature, [generate variations](/help/generative-ai/generate-variations.md), accessible now in Cloud Service. Generate variations helps you generate and scale content creation through the use of generative AI. Reach out to your Adobe account team for consideration in the program.

**AEM REST OpenAPI for Content Fragment Delivery**

The [AEM REST OpenAPI for Content Fragment Delivery](/help/headless/aem-rest-openapi-content-fragment-delivery.md), is available now for AEM as a Cloud Service. 

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### Early access feature in Dynamic Media {#dm-early-access}

**AI-generated video captions** 

AI-generated video captions in Adobe Dynamic Media use artificial intelligence to generate captions automatically for video content. This feature is designed to improve accessibility and enhance the user experience by providing accurate, real-time captions. The AI analyzes the video's audio track to transcribe speech and create captions, which can be edited for accuracy or customization. These captions help meet accessibility requirements and improve video engagement for audiences who rely on or prefer text-based video support. 

To get early access to AI-generated captions support on your Dynamic Media account, [create and submit an Adobe Customer Support case](/help/assets/dynamic-media/video.md##enable-dash).  

### New features in Assets view {#assets-view-new-features}

**Scheduled Reports**

Reports can now be automatically generated in the Assets View on a recurring schedule or at a future date, reducing the effort to uncover data-driven insights.

![Scheduled Reports-](/help/assets/assets/scheduled-reports-tab.png)

### New features in Content Hub {#content-hub-new-features}

**Digital Rights management for licensed assets**

Organizations can now increase license compliance and minimize risk of sharing assets with licensing terms by leveraging DRM for licensed assets for users of Content Hub, requiring users to review and accept license terms before they can start downloading licensed assets. For more information, see [Manage licensed assets on Content Hub](/help/assets/manage-licensed-assets-on-content-hub.md).

![download-multiple-license](/help/assets/assets/download-multiple-license.png)

**Asset card metadata configuration**

Content Hub now allows you to configure the key metadata fields that you need to display on the Asset Card upto a maximum of 6 fields. For more information, see the Asset Card section in [Configure Content Hub](/help/assets/configure-content-hub-ui-options.md#asset-card).

![key metadata on Asset Card](/help/assets/assets/asset-card-key-metadata.png)

**Configure the visibility and download of expired assets**

Administrators can now control if they need expired assets to be visible on Content Hub. If the expired assets are made visible, they can also define if users can download them. For more information, see the Expired Assets section in [Configure Content Hub](/help/assets/configure-content-hub-ui-options.md#expired-assets-content-hub).

![Expired assets on Content Hub](/help/assets/assets/expired-assets-content-hub.png)

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New feature in AEM Forms {#forms-new-features}

* [Enhance User Experience with Navigation Buttons in Panel Layouts](/help/forms/rule-editor-core-components-usecases.md#navigating-among-panels-using-button): You can now add navigation buttons to your panel layouts, such as Horizontal Tabs, Vertical Tabs, Accordions, or Wizard. These buttons enhance the user experience by simplifying transitions between panels, focusing on the selected panel.

<!--* **Specify Display Styles for Document of Record (DoR) Components**: In an XFA file, you can now specify the display styles for Document of Record components. These styles can later be applied to the corresponding components in Adaptive Forms Editor.-->

### New Pre-release features in AEM Forms {#forms-new-prerelease-features}

* [Auto-save a draft for Core Components based Adaptive Forms](/help/forms/save-core-component-based-form-as-draft.md): Users can now benefit from an auto-save feature that saves a partially completed form as a draft automatically. They can return later to finish filling it out on the same or other device. This feature improves conversion rates for organizations by reducing form abandonment, as users do not need to start over form filling from the beginning.

* [Update Adobe Sign scopes easily](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/forms/integrate/services/adobe-sign-integration-adaptive-forms): You can modify the scopes of an Adobe Sign configuration directly from the AEM Cloud Configurations page, making it quicker and easier to update existing configurations.

* [Asynchronous function support for Adaptive Forms](/help/forms/using-async-funct-in-rule-editor.md): When your Adaptive Form requires asynchronous operations, such as waiting for external processes or data retrieval, you can implement these operations with custom functions and configure them in the Rule Editor.
 
### Early Access features in AEM Forms {#forms-new-early-access-features}

The AEM Forms Early Access Program program offers a unique opportunity to you to get exclusive access to cutting-edge innovations, and help shape their development.

This release notes lists the innovations delivered in the current release. For the complete list of innovations available under the Early Access Program, see [AEM Forms Early Access Program documentation](/help/forms/early-access-ea-features.md). 

#### AEM Forms AI Assistant

[Generative AI for Adaptive Forms](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/forms/forms-overview/early-access-ea-features#aem-forms-ai-assistant-gen-ai) brings a whole new level of power and ease to your forms development processes. It allows you to build better forms faster than ever before. 

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

### Bug fixes {#bug-fixes-cif}

* Fixed UI tests to work properly with Core CIF components.
* Resolved issue with category URL format not functioning as expected in the cloud instance.

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### Configuration to Control Form Submissions {#configuration-submissions}

To control form submissions for Coral or Foundation forms at specific locations, AEM has introduced a new configuration: `com.adobe.granite.ui.components.FormRestrict`. This configuration consists of two fields:

1. **Add Allowed Paths**: Specifies the paths where form actions are permitted.
1. **Restrict Behavior**: Determines the behavior for restricted paths (paths not included in the allowed list). You can choose between two options:
   * **Popup** (default): Displays a popup notification.
   * **Prevent**:Blocks form submission.

>[!NOTE]
>
>This configuration is not supported for all Coral or Foundation forms located under `/apps`, `/libs`, `/mnt/overlay`, and `/mnt/override`.

### Self-Serve Log Forwarding with Advanced Networking Option {#log-forwarding}

While AEM (including Apache/Dispatcher) and CDN logs can be downloaded from Cloud Manager, many organizations find it beneficial to stream those logs to a preferred logging destination. AEM now supports [log forwarding](/help/implementing/developing/introduction/log-forwarding.md) to Azure Blob Storage, Datadog, HTTPS, Elasticsearch (and OpenSearch), and Splunk. AEM logs can be optionally forwarded over advanced networking configurations, such as using a dedicated IP address.

This feature is configured by users in a self-serve manner, and deployed using the [Config Pipeline](/help/operations/config-pipeline.md).

### Pipeline-free URL Redirects for Business Users {#pipeline-free-redirects}

Browser-side redirects are useful when a web page has been taken down or has moved, or other scenarios. With [Pipeline-free URL Redirects](/help/implementing/dispatcher/pipeline-free-url-redirects.md), you can place an Apache rewrite map file in an AEM publish location, where it is automatically loaded -- no need to commit the file to source control or initiate a Cloud Manager pipeline.

Options for publishing the rewrite file include uploading it as an asset, using the ACS Commons Rewrite Map Manager, or interacting with a custom user interface.

### Config Pipeline for RDEs {#config-pipeline-rdes}

Rapid Development Environments are a powerful tool for quickly deploying and testing code and configuration in a Cloud environment. RDEs now support [syncing of configuration YAML-files](/help/implementing/developing/introduction/rapid-development-environments.md#deploy-config-pipeline), including CDN settings such as traffic filter rules and request/response transformations, as well as log forwarding and other configuration options. [See the full list](/help/operations/config-pipeline.md) of supported configuration options for more details.

### New Product Profiles {#new-product-profiles}

When a new AEM environment is created, Product Profiles automatically appear in the Adobe Admin Console, enabling administrators to assign access to licensed solutions and features. 

New environments now include an updated set of Product Profiles, making them compatible with future features including generating API credentials in the Adobe Developer Console. Existing environments will be able to update their Product Profiles in a future release. [Learn more](/help/onboarding/aem-cs-team-product-profiles.md).

### New AEM Developer Console (Public Beta) {#aem-developer-console-beta}

Try out a revamped [AEM Developer Console](/help/implementing/developing/introduction/aem-developer-console.md), which offers a more interactive experience for debugging code in Cloud environments.

Anyone can access the public beta by clicking the *New Console Available* button in the current AEM Developer Console. Adobe welcomes feedback, which you can email to **<aemcs-new-devconsole-ui-beta@adobe.com>**.

![OSGi Bundles Screen in AEM Developer Console](/help/implementing/developing/introduction/assets/osgi-bundles.png)

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
