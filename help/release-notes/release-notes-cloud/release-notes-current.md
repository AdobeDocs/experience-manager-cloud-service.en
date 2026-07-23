---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service
description: Current release notes for [!DNL Adobe Experience Manager] as a Cloud Service.
mini-toc-levels: 1
exl-id: a2d56721-502c-4f4e-9b72-5ca790df75c5
feature: Release Information
role: Admin
nudge: please
---
# Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the current (latest) version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions such as 2024 or 2025.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>To receive a monthly email notification about updates to Experience Cloud release notes, subscribe to the [Adobe Priority Product Update](https://www.adobe.com/subscription/priority-product-update.html).

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2026.6.0) is June 25, 2026. The next feature release (2026.7.0) is planned for July 30, 2026.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

<!-- 

## Release Video {#release-video}

Have a look at the May 2026 Release Overview video for a summary of the features added in the 2026.5.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3491490/?quality=12)

-->

## AEM Beta Programs {#aem-beta-programs}

Adobe Experience Manager (AEM) beta programs are a way for customers to get access to prerelease features and code, provide feedback, and guide the future of AEM. 

>[!IMPORTANT]
>
>Beta releases may contain defects and are provided "AS IS" without warranty of any kind. Adobe has no obligation to maintain, correct, update, change, modify or otherwise support (by way of Adobe Support Services or otherwise) the beta releases. Adobe advises customers to use caution and not rely on the correct functioning or performance of beta releases, or on any accompanying documentation or materials. Features and APIs in beta are subject to change without notice. Accordingly, any use of the beta releases is entirely at the customer's own risk.

**Benefits of participating**

Getting early access to features that Adobe is developing lets customers and partners provide feedback and shape product development. It also helps them prepare to adopt new capabilities before general availability.

**Current beta programs**

The following sections list active beta programs.

### Agents in AEM {#agents-in-aem}

If you would like to explore the powerful, new AEM agentic capabilities across production, governance, optimization, discovery, and development, [please learn about how you can access them here.](/help/ai-in-aem/agents/overview.md)

<!--
### Agents in AEM (Explorer program) {#agents-in-aem-beta-program}

Gain early access to powerful, new AEM agentic capabilities across production, governance, optimization, discovery, and development. Your feedback directly shapes Adobe's roadmap and final features. See [Overview of Agents in AEM](/help/ai-in-aem/agents/overview.md) to learn more.

This program typically lasts 4-6 weeks, but can be tailored to be flexible around your ability to actively participate. 

To opt in to participate in this program, email [aemagentsteam@adobe.com](mailto:aemagentsteam@adobe.com) and include the following details to the extent possible:

* Names and Adobe ID's of team members who will actively use agents.
* List Specific agents that you or your team will want to use. Or simply say "All Agents."

Customers selected for participation will be notified directly by Adobe. Participation is subject to eligibility considerations, including customer licensing and limited program capacity. While not all requests can be accommodated initially, additional customers may be considered in future beta waves.
-->

### AEM Foundation (Beta programs) {#aem-foundation-beta-programs}

See [AEM Foundation beta programs](#foundation-early-adopter).

### Cloud Manager (Beta programs) {#cloud-manager-beta-programs}

See [Cloud Manager beta programs](/help/implementing/cloud-manager/release-notes/current.md).

### AEM Assets (Beta programs) {#aem-assets-beta-programs}

See [AEM Assets beta programs](#assets-beta-program-features).

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### Visual Content Fragments {#visual-content-fragments}

AEM now supports [Visual Content Fragments](/help/sites-cloud/administering/content-fragments/visual-content-fragments.md), which render Content Fragment output as formatted HTML experiences using attached HTML templates. This enables content authors to preview and validate structured content in its final visual form before publication, and to deliver modular experiences consistently across channels — including web, email, and Edge Delivery Services. A built-in generic template is available for basic quality assurance without requiring a custom template.

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

**Open Photoshop assets in Adobe Express Embedded Editor**

You can now open Adobe Photoshop (.psd) files in addition to JPEG and PNG formats in Adobe Express embedded editor from Assets view and Content Hub. This enhancement enables creative and marketing teams to work with layered design files without leaving AEM Assets, streamlining content updates and reducing the need to switch between applications. PSD support helps accelerate content creation workflows while preserving the flexibility of source design assets. Users can save resulting remixed creations as channel-ready assets to AEM. 

**Import Adobe Illustrator and Adobe InDesign assets from AEM Assets into Adobe Express**

Adobe Express now supports importing Adobe Illustrator (.ai) and Adobe InDesign (.indd) files from AEM Assets using the Assets plugin. Adobe Illustrator files can be imported into the current document or imported into a new Express document. Adobe InDesign files can be imported into a new Express document. This capability allows creative and marketing teams to access and reuse approved design assets more easily, accelerating content creation and helping ensure consistent brand experiences across channels.

>[!IMPORTANT]
>
>This feature is available as Limited Availability feature. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.

**Maintain asset lineage between Adobe Express and AEM Assets**

AEM Assets now preserves lineage information for assets created in Adobe Express using assets sourced from AEM. This capability records relationships between source assets and the resulting content and stores it as asset metadata in AEM, enabling organizations to trace how approved assets are reused across creative workflows.

By maintaining asset lineage metadata, teams can improve governance, compliance, and content supply chain transparency. It also helps marketers and content administrators better understand asset reuse, support rights management initiatives, and track the origin of assets used in published content.

>[!IMPORTANT]
>
>This feature is available as Limited Availability feature. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.

**AEM integration with Workfront Planning and GenStudio for Performance Marketing for standard campaign metadata**

When AEM Assets is integrated with [Workfront Planning and GenStudio for Performance Marketing](https://experienceleague.adobe.com/en/docs/workfront/using/adobe-workfront-planning/planning-and-genstudio-integration/planning-and-genstudio-integration-article-index), campaign metadata fields, including Campaign Name, Region, Channel, Persona, and Product, are now available in Asset view properties rail under a dedicated read-only Campaign tab. When users in Workfront Planning connect assets from AEM to GenStudio the respective objects in Adobe GenStudio workspace, specific values (e.g., a specific campaign name) is automatically added to AEM asset's metadata. 

The integration enables users to quickly discover and search for assets based on campaign attributes. This enhancement improves asset findability, streamlines content management workflows, and helps teams locate the right assets for specific marketing initiatives more efficiently.

>[!IMPORTANT]
>
>This feature is available as Limited Availability feature and requires licenses for Workfront Planning and GenStudio for Performance Marketing. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.

**AI-powered content onboarding and content supply chain automation**

Use an AI-powered agent to configure and automate content migrations and recurring synchronization between supported content repositories. The agent guides you through connection setup, metadata mapping, and validation with dry runs before transferring content. By eliminating manual processes and custom integrations, this capability accelerates onboarding, simplifies ongoing synchronization, and helps keep assets and metadata consistent across systems.

>[!IMPORTANT]
>
>This feature is available as Limited Availability feature. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.


### New features in Dynamic Media with OpenAPI capabilities {#new-features-dynamic-media-openapi}

**AI-generated video captions** 

AI-generated video captions in Dynamic Media with OpenAPI capabilities use artificial intelligence to generate captions automatically for video content. This feature is designed to improve accessibility and enhance the user experience by providing accurate, real-time captions. The AI analyzes the video's audio track to transcribe speech and create captions, which can be edited for accuracy or customization. These captions help meet accessibility requirements and improve video engagement for audiences who rely on or prefer text-based video support.

>[!IMPORTANT]
>
>This feature is available as Limited Availability feature. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.

**Embedded video transcripts for improved accessibility and SEO**

The DynamicMedia Component now embeds transcripts for videos to improve accessibility for your customers. These are server side rendered (SSR) transcripts which directly increase the SEO and LLM visibility of videos. It also embeds a compliant VideoObject [ref https://schema.org/VideoObject] that helps search engine and LLM tools recognise videos in your page.

>[!IMPORTANT]
>
>This feature is available as Limited Availability feature. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.

**Custom thumbnails for videos**

Dynamic Media with OpenAPI capabilities now lets you upload custom thumbnails for video assets. By replacing automatically generated thumbnails with branded or purpose-built images, organizations can improve content presentation, enhance asset discoverability, and create a more engaging viewing experience.

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New Features in AEM Forms

#### Interactive Communication Editor 

[Interactive Communication (IC) Editor](/help/forms/interactive-communication/introduction.md) is now available in AEM Forms as a Cloud Service. It is a browser-based solution for creating, managing, and delivering data-driven interactive correspondences such as business correspondence, documents, statements, benefit notices, marketing mails, bills, and welcome kits.

![Interactive Communication Editor](/help/forms/assets/ic-editor.png)

* **Cloud-Based Editor**: Unlike AEM Forms Desktop Designer which can only be installed on Windows machines, the Interactive Communications editor runs in any modern browser with no installation required. This cloud-based approach eliminates installation hassles, provides cross-platform accessibility, and enables collaboration from any location with internet access. For more information, see [Getting Started with IC Editor](/help/forms/interactive-communication/getting-started.md).

* **Components and Properties**: Build communications using a drag-and-drop component library — text fields, tables, images, barcodes, subforms, and more. Configure layout, typography, margins, and appearance through the Properties panel. For more information, see [Introduction to Interactive Communication Editor](/help/forms/interactive-communication/introduction.md).

* **Data Binding**: Connect components to Form Data Models (FDM) using visual mapping to drive personalized, data-driven output. For more information, see [Data Binding in Interactive Communication Editor](/help/forms/interactive-communication/configure-data-binding.md).

* **Rule Editor**: Build dynamic, data-driven actions directly within your documents using an intuitive, point-and-click interface. Easily define conditional logic, automate workflows, and personalize content without writing code. For more information, see [Create Rules in Interactive Communication Editor](/help/forms/interactive-communication/use-the-rule-editor.md).

* **Templates and Document Fragments**: Create reusable templates and modular content blocks (headers, footers, disclaimers) for consistency and efficiency across multiple communications. For more information, see [Create a Template](/help/forms/interactive-communication/create-interactive-communication-template.md) and [Create a Fragment](/help/forms/interactive-communication/create-interactive-communication-fragment.md).

* **Template Locking**: Lock content and layout elements within templates to maintain brand integrity and prevent unauthorised modifications. For more information, see [Template Lock](/help/forms/interactive-communication/enable-template-lock.md).

* **PDF Preview**: Preview Interactive Communication with no data, local JSON files, or data models for flexible, data-driven testing. For more information, see [PDF Preview](/help/forms/interactive-communication/generate-pdf-preview.md).

* **Custom Fonts**: Embed custom or organization-approved fonts to ensure consistent, branded PDF rendering across devices. For more information, see [Add Custom Fonts](/help/forms/interactive-communication/add-custom-fonts.md).

* **Import and Export**: Seamlessly migrate and reuse Interactive Communication with their fragments and data models across environments. For more information, see [Import and Export](/help/forms/interactive-communication/import-and-export-the-interactive-communication.md).

* **Content Overflow**: "Allow page breaks within content" option for flowed layouts for smooth multi-page editing and better text management for complex documents. For more information, see [Content Overflow Handling](/help/forms/interactive-communication/handle-content-overflow.md).

* **XDP File Editing**: Edit XDP files in a browser instead of Forms Designer that runs only on Microsoft Windows desktop. For more information, see [Support XDP Editing](/help/forms/interactive-communication/support-xdp-editing.md).

* **Associate UI**: A simplified runtime interface for customer-facing associates to enter data and generate personalized communications in real time. Invoke the Associate UI directly on Publish instances to simplify integration and accelerate deployment across environments. For more information, see [Associate UI Overview](/help/forms/interactive-communication/associate-ui-in-interactive-communication-editor.md), [Enable and Configure Associate UI](/help/forms/interactive-communication/enable-configure-associate-ui.md), and [Integrate Associate UI](/help/forms/interactive-communication/invoke-associate-ui.md).

* **Dynamic Page Numbering**: Automatically display "Page # of ##" on master pages for clear, consistent pagination across multi-page documents. For more information, see [Dynamic Page Numbering](/help/forms/interactive-communication/implement-dynamic-page-numbering.md).

* **Versioning and Commenting in Interactive Communication Editor**: The Interactive Communication Editor now supports versioning and commenting so authors can save labeled versions, capture reviewer feedback, revert to earlier states, and maintain an audit trail across the content lifecycle. For more information, see [Versioning and Commenting in Interactive Communication Editor](/help/forms/interactive-communication/versioning-and-commenting-in-interactive-communication-editor.md).

* **Review and Annotate an Interactive Communication**: Reviewers can now annotate Interactive Communications in a dedicated read-only view, pin comments to specific components on the canvas, and share feedback in one place without editing the design. Authors can track and resolve annotations directly in the editor. For more information, see [Review and Annotate an Interactive Communication](/help/forms/interactive-communication/howto/review-and-annotate-interactive-communication.md).

* **Compare Interactive Communication Versions**: You can now compare any two saved versions of an Interactive Communication side by side as PDF previews to review layout and static content changes before publishing. For more information, see [Compare Interactive Communication Versions](/help/forms/interactive-communication/howto/compare-interactive-communication-versions.md).

* **Merge and Split Table Cells**: The Interactive Communication Editor now supports merging adjacent table cells and splitting merged cells back into individual columns, enabling spanning headers, summary rows, and more flexible table layouts. For more information, see [Merge and Split Table Cells](/help/forms/interactive-communication/howto/merge-and-split-table-cells.md).

* **Move a Component to the Master Page**: You can now move a component from a design page to the master page in one action so it appears consistently across every page of an Interactive Communication without recreating it. For more information, see [Move a Component to the Master Page](/help/forms/interactive-communication/howto/move-component-to-master-page.md).

* **Configure Dropdown Options for Associate UI**: Dropdown fields in the Associate UI now use an **Options Binding** model. Authors configure **Bind from Data** for dynamic option lists or manual static options so associates see the correct choices and pre-selected value. **Data Binding** is not supported for dropdown fields. For more information, see [Configure Dropdown Options for Associate UI](/help/forms/interactive-communication/associateui/configure-dropdown-options-binding.md).

* **Configure Bound and Unbound Variables for Associate UI**: Bound and unbound variables in **Text** components can now be configured for the Associate UI. Authors choose whether associates edit the entire text block inline in the document preview or enter values for individual variables in the data entry panel. Duplicate variable names propagate values across all matching occurrences in the preview. For more information, see [Configure Bound and Unbound Variables for Associate UI](/help/forms/interactive-communication/associateui/configure-bound-unbound-variables-associate-ui.md).

#### Additional CAPTCHA options for bot protection

AEM Forms now supports two additional CAPTCHA solutions for protecting Adaptive Forms from bots and spam submissions, in addition to the already available Google reCAPTCHA. This gives you more choice and flexibility in securing your forms.

* **Cloudflare Turnstile**: A frictionless CAPTCHA that verifies users through a simple challenge without requiring explicit interaction, improving the user experience. For more information, see [Use Turnstile in an Adaptive Form for Core Components](/help/forms/integrate-adaptive-forms-turnstile-core-components.md) and [Use Turnstile in an Adaptive Form for Foundation Components](/help/forms/integrate-adaptive-forms-turnstile.md).
* **hCaptcha**: A privacy-focused CAPTCHA that offers a user-friendly alternative with an emphasis on data privacy, balancing security and user experience. For more information, see [Use hCaptcha in an Adaptive Form for Core Components](/help/forms/integrate-adaptive-forms-hcaptcha-core-components.md) and [Use hCaptcha in an Adaptive Form for Foundation Components](/help/forms/integrate-adaptive-forms-hcaptcha.md).

### Early Adopter Features

#### Document of Record for forms embedded in AEM Sites

Authors can now configure and generate a Document of Record (Submission PDF) for Adaptive Forms Core Components embedded in AEM Sites pages. DoR settings—including auto-generation, custom XDP templates, and branding—are available directly from the **Adaptive Form Container** in the Sites page editor. [Learn more](/help/forms/generate-document-of-record-core-components.md#configure-document-of-record-for-forms-embedded-in-aem-sites).

#### Locale-specific custom XDP templates for Document of Record

When you associate a custom XDP template for DoR, you can provide locale-specific versions in the same folder using the `basename.<locale>.xdp` convention (for example, `a.xdp` and `a.fr.xdp`). AEM Forms automatically picks the template that matches the form locale when generating the Submission PDF, with fallback to the default template. [Learn more](/help/forms/generate-document-of-record-core-components.md#locale-specific-custom-xdp-templates-for-document-of-record).

#### Adobe Sign agreement expiration

You can set how long recipients have to complete signing by specifying **Document Expiration (Days)** in the **Electronic Signature** section of an Adaptive Form. The value is sent to Adobe Sign as `daysUntilSigningDeadline`. If left empty, the agreement does not expire. [Learn more](/help/forms/working-with-adobe-sign.md#set-document-expiration-for-an-adobe-sign-agreement).

## [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation {#foundation}

### [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation New Features {#foundation-new}

#### Conversational AI Interface for Cloud Manager Questions {#devagent-cloudmanager}

The Development Agent expands to handling questions related to Cloud Manager through the [Cloud Manager Job](/help/ai-in-aem/agents/brand-experience/development/development.md#cloud-manager-job). In AI Assistant, retrieve information about programs, environments, and pipelines (e.g., execution status). Quickly find links to error logs, access logs, and build logs. 

#### Enhancements to Pipeline Troubleshooting Agent Job {#devagent-pipeline-troubleshooting}

The Development Agent's [pipeline troubleshooting job](/help/ai-in-aem/agents/brand-experience/development/development.md#cloud-manager-pipeline-troubleshooting) helps developers diagnose and resolve issues in AEM as a Cloud Service deployments. New features include:

* Support for Web Tier Config Pipeline - In addition to supporting Full Stack pipelines (Deployment and Code Quality), the Development Agent now supports troubleshooting for the **Web Tier Config Pipeline**

* Experience Home Widget for failed pipelines - The Admin & IT role will see a [new widget](/help/ai-in-aem/agents/brand-experience/development/development.md#troubleshoot-from-experience-home) highlighting pipeline failures. A clickable button initiates the pipeline troubleshooting job in AI Assistant.

#### Manage Quiet Hours and Update Free Periods with AI Assistant {#quiet-hours-ai}

You can now view, create, and edit [Quiet Hours and Update Free Periods](/help/ai-in-aem/agents/brand-experience/development/development.md#control-updates-job) directly through the AEM AI Assistant.
The key benefit is fewer scheduling errors. As you make a request, the assistant guides you through what is possible and flags the limits that apply, such as the three-period cap, the mandatory one-week gap between periods, and the planned maintenance exclusion windows you cannot schedule over. So instead of discovering a constraint after a failed configuration, Business Owners and Deployment Managers are steered to a valid schedule in the same conversation. This protects critical business windows from automatic maintenance updates while reducing back-and-forth and misconfiguration.

### [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation Important Notices {#foundation-notices}

#### IMS Authentication Rich Errors {#ims-auth-rich-errors}

To help troubleshoot IMS integrations, `imsauth` has added support for *rich errors*.

Instead of returning only an HTTP status code, these errors provide additional context to help diagnose and resolve issues that can block authentication and access.

#### Java API Deprecations {#java-api-deprecation}

It is critical to remove usage of deprecated APIs. 

Since **April 14, 2026**, Cloud Manager pipelines that contain code using APIs targeting 2/26/2026 removal **fail during the Code Quality** step. Deployments will be blocked until the deprecated API usage is removed. *This may prevent you from releasing time-sensitive updates and could impact your business operations.* 

Starting **September 14, 2026**, environments still using these deprecated APIs **will not receive critical Adobe release updates** and will not be subject to Adobe's standard commitments around performance and availability. As a result, you will not receive new features or bug fixes, application stability and uptime may be negatively affected, and security risk exposure may increase further.

See the [deprecation article](/help/release-notes/deprecated-removed-features.md#aem-apis) for full details, but for convenience, these APIs are listed below:

+++ Expand to see the Java API deprecations

* `org.apache.sling.commons.auth`
* `org.apache.felix.webconsole`
* `org.eclipse.jetty`
* `com.mongodb`
* `org.apache.abdera`
* `org.apache.felix.http.whiteboard`
* `org.apache.cocoon.xml`
* `ch.qos.logback`
* `org.slf4j.spi`
* `org.slf4j.event`
* `org.apache.log4j`
* `com.google.common`
* `com.drew`
* `org.apache.jackrabbit.oak.plugins.memory`

+++

#### Dispatcher Local MCP server is part of AEM SDK {#local-dispatcher-mcp}

The Dispatcher local MCP server is now included in the **AEM SDK** in the [Software Distribution Portal](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html), packaged inside the AEM Dispatcher tools zip. Previously, the Dispatcher local MCP server was packaged in a separate beta listing of AEM Dispatcher tools.

The Dispatcher local MCP server enables AI tools to validate Dispatcher and Apache HTTPD configuration, trace request handling, and inspect cache behavior against a Dispatcher instance running locally in Docker.

#### Preparing for Java 25: AEM Cloud Service Runtime Upgrade Timeline

Java 25 is the next long-term support (LTS) release after Java 21, delivering improvements across performance, developer productivity, and security:

- **Performance** — Reduced memory footprint, more efficient garbage collection, and faster JVM warm-up benefit cloud-native deployments.
- **Developer productivity** — Cleaner object initialization, more expressive pattern matching, and simplified concurrent task management reduce boilerplate and improve code clarity.
- **Security** — Modernized cryptographic key derivation API to simplify common security workflows.

To help organizations plan testing and validation ahead of the necessary Java 25 runtime upgrade, Adobe is providing the following target dates. Any updates to this timeline will be communicated via release notes.

| Timeframe | Milestone |
|---|---|
| **Mid-October 2026** | AEM Cloud Service SDK supports Java 25 runtime. The Java 25 JDK is available for download from the Adobe Software Distribution portal. |
| **November 2026** | Customers are encouraged to optionally enable the Java 25 runtime in their Cloud environments to validate behavior. Early adoption maximizes time to surface and resolve issues. |
| **February – May 2027** | Adobe will gradually migrate lower environments (RDE, Dev) to the Java 25 runtime. Customers should validate behavior and report unexpected issues, and are encouraged to enable staging and production environments as well. A temporary rollback to Java 21 is available while resolving any problems. |
| **June 2027** | All environment runtimes (including staging and production) migrate to Java 25. Java 21 runtime is decommissioned. The AEM Cloud Service SDK will no longer support Java 21. |

AEM Cloud Service continues to support compiling customer code with Java 11, Java 17, and Java 21. However, Adobe recommends building with Java 25 (once available in AEM) to take full advantage of the latest language features and performance improvements.

### [!DNL Experience Manager] as a [!DNL Cloud Service] Foundation Early Adopter Features {#foundation-early-adopter}

#### AEM Edge Functions (*Public Beta* Program) {#edge-functions}

[AEM Edge Functions](/help/implementing/developing/introduction/edge-functions.md) is now in public beta so you can try it out in a self-serve way without contacting Adobe to enable.

This feature allows you to execute JavaScript at the CDN layer, bringing data processing closer to the end user. This reduces latency and enables responsive, dynamic experiences at the edge. It's available for both AEM Cloud Service Java Stack and Edge Delivery Services projects, for AEM Sites customers.

Common use cases include:

* Personalizing content based on geolocation, device type, or user attributes
* Acting as middleware between the CDN and your origin
* Reformatting responses from third-party APIs (and perhaps aggregating multiple API responses) before delivering them to the browser
* Composing and serving server-rendered HTML at the edge using content stitched from various backends

Follow [this tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/edge-functions/overview) for a concrete walk-through for both Edge Delivery Services and AEM as a Cloud Service Java-stack variations.

*By using the AEM Edge Functions Beta, you acknowledge that it is still in development and that you should not rely on the correct functioning of the technology or availability of data. This feature is provided as-is,
may change without notice, and is not covered by production SLAs.*

#### Snapshots for RDEs (*Public Beta* Program) {#rde-snapshot-program}

Snapshots for Rapid Development Environments (RDEs) is now in public beta so you can self-serve try it out without contacting Adobe to enable.

RDEs now support a feature [to take a snapshot](/help/implementing/developing/introduction/rapid-development-environments.md#snapshots) of the current state of code and content, which can be restored at a later time. This can be useful when syncing code that may need to be reverted, or when switching between development of different features. It's also possible to restore just the mutable content as a known starting point for testing.

*By using the RDE Snapshots Beta, you acknowledge that it is still in development and that you should not rely on the correct functioning of the technology or availability of data. While we have tested this feature extensively, there is a small possibility that your RDE could become unstable. If this occurs, a reset will restore it to a working state.*

#### Replication AI Troubleshooting (Beta Program) {#replication-ai-troubleshooting-beta}

Using the AI Assistant in AEM Author and other interfaces, you can troubleshoot replication-related issues such as blocked queues. To join the Beta Program, email [aem-devagent@adobe.com](mailto:aem-devagent@adobe.com), describing your interest.

#### Canary Production Deployments to Test Code Before Accepting Live Traffic (Beta Program) {#canary-beta}

Validate a production build with internal-only test traffic before exposing it to end users. Ship to production, route only canary traffic (using a special header), monitor behavior, then either promote to live traffic or roll back—without impacting customers.

Email [aemcs-canary-deployments-beta@adobe.com](mailto:aemcs-canary-deployments-beta@adobe.com) to request access and share feedback.

#### AEM Code Assessment and auto-fix via IDE AI agent (Beta Program) {#ide-ai-aemcode-issues}

AEM Cloud Service Java-stack teams using AI-assisted development in tools like Cursor, Claude Code, Visual Studio, and IntelliJ can now go further. A new [code assessment IDE agent skill](/help/ai-in-aem/local-development-with-ai-tools.md#use-the-code-assessment-skill) detects and auto-fixes issues directly in your AEM codebase, reducing review cycles and catching problems earlier in development. 

Supported checks include:
* replacing deprecated APIs
* modernizing Sling Model dependency injection
* updating outdated Maven dependencies
* adding missing timeouts to outbound HTTP calls
* bounding unbounded queries
* Sling schedulers
* resource change listeners the Replication
* JCR or OSGi event handling

This feature is in beta. Try it out and share feedback with the team at [aemcs-ai-ide-tools-feedback@adobe.com](mailto:aemcs-ai-ide-tools-feedback@adobe.com).

#### Edge Authentication for Edge Delivery Services (Beta Program) {#edge-authentication}

Edge Authentication lets you restrict access to Edge Delivery Services pages to only those who have authenticated with your identity provider (IdP). This is achieved by deploying an OpenID Connect (OIDC) configuration YAML file.

If interested, please email [aemcs-edgecompute-feedback@adobe.com](mailto:aemcs-edgecompute-feedback@adobe.com) with a brief description of your use case and any questions you may have.

#### OpenTelemetry for Application Performance Monitoring (APM) (Alpha Program) {#apm-alpha}

AEM as a Cloud Service now supports OpenTelemetry-based telemetry export, letting you monitor AEM alongside the rest of your systems in the APM tools your teams already use.

Use this integration to:

- Investigate slow or failing requests
- Track JVM health and resource usage over time
- Build dashboards and alerts for your AEM tiers
- Correlate AEM behavior with other services during incidents

To join the alpha, email [aemcs-apm-beta@adobe.com](mailto:aemcs-apm-beta@adobe.com), describing your use case.

### [!DNL Experience Manager] as a [!DNL Cloud Service] Assets Beta Features {#assets-beta-program-features}

#### UI Extensibility for Assets View {#ui-extensibility-assets-view-beta}

Assets View supports UI Extensibility, a developer-first capability that empowers customers to tailor the out-of-the-box experience to meet their specific business requirements.
Customers can leverage existing stable extension points by following Adobe's developer documentation to build and deploy extensions with minimal effort. For use cases where a required extension point is not yet available, Adobe works directly with customers to explore the requirements and assess the technical feasibility of delivering new extensibility APIs tailored to their needs, and may deliver such new APIs as **Beta Releases**.
Additionally, Adobe has developed a **GenAI-powered extension generation tool** currently available in an internal early adoption phase. This tool can significantly accelerate extension development time. Customers participating in this beta program will receive access to the tool and are encouraged to share feedback to help shape its evolution.
To participate or learn more, send an email to `GRP-ASSETSVIEWUIEXTENSIBILITY@adobe.com`.

#### Brand Aware Metadata (BAM) {#brand-aware-metadata-beta}

AEM Assets now supports Brand Aware Metadata, an AI-powered capability that automatically generates custom metadata for assets when uploaded or re-processed. This reduces the need for manual entry by orders of magnitude, helping teams find assets and deliver new experiences much faster. Customers maintain a library of prompts that define how AI should populate any given metadata field, tailored to their own brand vocabulary and taxonomy. This prompt library includes a playground to preview results and a prompt optimizer that automatically drafts suggested improvements.

Adobe is actively expanding BAM's capabilities through direct co-innovation with customers. Where a specific use case is not yet supported, Adobe works with participating customers to understand their needs and may deliver expanded capabilities as the beta progresses. Customers in this program gain early access to new features as they ship and are encouraged to share feedback that directly shapes the roadmap.

To participate or learn more, send an email to `GRP-AEM-ASSETS-BRANDAWAREMETADATA@adobe.com`.

#### Assets Onboarding Agent {#assets-onboarding-agent-beta}

If your organization is new to Experience Manager Assets, you can opt in to the **Assets Onboarding Agent Beta program**, which gives you access to the following AEM Brand Experience AI skills for onboarding:

* Guides users through DAM setup and migration planning by using a conversational workflow to capture business needs and recommend how an AEM Assets deployment should be structured.

* Creates core AEM Assets configuration artifacts such as folder hierarchies, tag taxonomies, metadata forms, and can help execute bulk import jobs to accelerate onboarding.

**Why participate?**

* Go live faster with a ready-to-use DAM environment by eliminating repetitive, manual steps with AI assistance.

* Lower operational overhead with automated configuration and preparation of folders, tags, metadata and asset imports.

* Improve consistency, governance, and ensure adherence to best practices through a curated setup experience with intelligent recommendations tailor-made for your business.

To participate or learn more, send an email to `GRP-AEM-ONBOARDING-AGENT@adobe.com`.

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


