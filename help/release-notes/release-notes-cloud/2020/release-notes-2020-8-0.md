---
title: Release Notes for 2020.8.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: "[!DNL Adobe Experience Manager] as a Cloud Service Release Notes for 2020.8.0."
exl-id: 83413130-ae90-4419-bcf7-42fdc740452b
feature: Release Information
role: Admin
---
# Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service 2020.8.0 {#release-notes}

The following section outlines the general Release Notes for Experience Manager as a Cloud Service 2020.8.0.


## [!DNL Adobe Experience Manager Sites] as a Cloud Service {#sites}

### What is new in [!DNL Sites] {#what-is-new-sites}

* Ability to [restore pages and sub-pages (page trees) to an earlier version](/help/sites-cloud/authoring/sites-console/page-versions.md#reinstating-versions).

* Ability to [create Launches](/help/sites-cloud/authoring/launches/overview.md) in AEM [SPA Editor](/help/implementing/developing/hybrid/introduction.md).


## [!DNL Adobe Experience Manager Assets] as a Cloud Service {#assets}

### What is new in [!DNL Assets] {#what-is-new-assets}

* Video transcoding is now supported with asset microservices. A new section in the [!UICONTROL Processing Profiles] configuration lets you set video bit rate and dimensions. The output format is MP4 with H.264 codec. For details, see [manage video assets](/help/assets/manage-video-assets.md#transcode-video). For more transcoding options and for video delivery, use [!DNL Dynamic Media] add-on.

* On new [!DNL Experience Manager Assets] deployments, the smart tagging functionality is now configured by default. No need to manually integrate with [!DNL Adobe Developer Console]. On existing deployments, administrators configure smart tags integration as before.

* A new [asset download experience](/help/assets/download-assets-from-aem.md) allows,

  * Asynchronous download for large downloads so that users do not have to wait.
  * A new modular API for developer extensibility.

* Metadata extraction for asset microservices has an improved performance. It increases the overall asset ingestion throughput.

* Use a processing profile to generate custom metadata using Compute Service. See [Custom metadata using processing profile](/help/assets/manage-metadata.md#metadata-compute-service).

* A simpler download experience for Brand Portal users that administrators can configure. See [download experience overview](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/introduction/whats-new.html#download-configurations).

* Native and high-fidelity PDF document previews are now available in Brand Portal. See [document viewer overview](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/introduction/whats-new.html#doc-viewer).

* You can now invalidate the CDN (Content Delivery Network) cache directly from [!DNL Dynamic Media] in AEM as a Cloud Service (as opposed to using [!DNL Dynamic Media Classic]). It ensures that the latest assets are served within minutes instead of hours. See [Invalidating the CDN cache by way of Dynamic Media](/help/assets/dynamic-media/invalidate-cdn-cache-dynamic-media.md).

* Enhanced accessibility support is added to user interface controls, navigation, browse, and search experience in [!DNL Assets].

  * If you press the Escape key after selecting [!UICONTROL Add Rendition] option, the focus returns to the toolbar. <!-- via CQ-4293594-->
  * Keyboard focus works as expected when using the Email combo box. <!-- via CQ-4286215 -->
  * The accordions elements in search filters section are interpreted as standard expandable accordions. <!-- via CQ-4273103 -->
  * When applying a tag to an asset, the dialog box displays tags as tree elements. ARIA attributes are appropriately applied to the tree elements to make them accessible now. <!-- via CQ-4272964 -->
  
* [!DNL AEM Desktop app] 2.0.3 release is now available. It improves compatibility with [!DNL Experience Manager] 6.5.5 service pack and has an updated client OS compatibility list. [!DNL Windows] 7 and [!DNL macOS] versions earlier than 10.14 are not supported.

### Bugs fixed in [!DNL Assets] {#bugs-fixed}

* Relate and unrelate option does not respond when clicked for the first time. (CQ-4299022)
* When downloading an asset, if you select the option to receive it via email, the email is not sent. (CQ-4299146)

## Adobe Experience Manager Commerce as a Cloud Service {#cloud-services-commerce}

### What's New {#what-is-new-commerce}

* Product Console feature is now available. This allows marketers/authors in AEM to view and navigate categories and products that are stored in the commerce backend. Support for properties for categories and products in the Product Console also provided.

* Product and Category Pickers improved to allow marketers to select product via SKU or select category via category ID.

## Cloud Manager {#cloud-manager}

### Release Date {#release-date-cm}

The Release Date for [!UICONTROL Cloud Manager] Version 2020.8.0 is August 06, 2020.

### What's New {#what-is-new-cloud-manager}

* Content Audit is a feature enabled on Cloud Manager Sites Production Pipelines. The Production Pipeline configuration for programs with Sites now includes a third tab named **Content Audit**. Whenever a production pipeline is run, a new Content Audit step is included in the pipeline after custom functional testing which evaluates the site against several dimensions including performance, SEO (Search Engine Optimization), accessibility, best practices and PWA (Progressive Web App).


  >[!NOTE]
  >Content Audit has since been renamed to Experience Audit.

   See [Experience Audit Testing](/help/implementing/cloud-manager/experience-audit-dashboard.md) for more details.

* Newlycreated environments in Assets programs will now be automatically configured with Smart Content Services.

* Hibernated environments can be de-hibernated from the Cloud Manager's **Overview** page.

* Ability to perform Experience Checks on pages, powered by Google Lighthouse. As part of Cloud Manager pipeline, up to 25 pages can be checked and validated against experience KPIs, and scores are displayed in Cloud Manager UI.

### Bug Fixes {#bug-fixes-cm}

* Some unnecessary and undesired SonarQube plugins were being executed as part of the Code Quality scanning.

* On the pipeline execution page, the branch name was incorrectly formatted.

* In some cases, completed pipeline executions were not successfully recorded as having been completed thereby preventing new executions of the pipeline.

* Pipeline executions would occasionally get *stuck* due to internal communication issues.

* Upon provisioning a new organization, some users with administrative roles other than system administrators were erroneously given access to Cloud Manager.

* Under certain conditions, the update indexes job was started multiple times in parallel resulting in a deployment failure.

* The tooltip on the program cards were not consistently correct.

* The user interface erroneously allowed for operations to be attempted on an environment while it was being deleted.

* There was a color mismatch on the Cloud Manager's **Overview** page.

### Known Issues {#known-issues-cm}

* Invalid pages are included bringing the Content Audit Average Score below what they should be.

* The Content Audit tab incorrectly displays the base URL using the author domain instead of the publish domain.

* To activate the Content Audit step, users must edit the pipeline and, optionally, add pages. If no pages are added, the homepage is audited.

## Content Transfer Tool {#content-transfer-tool}

Follow this section to learn about what is new and the updates for Content Transfer Tool Release v1.0.4.

### What's New {#what-is-new-ctt}

* Content Transfer Tool now supports Shared S3 DataStore.

### Bug Fixes {#ctt-bug-fixes}

* Additional timeouts added for the tool to complete actions.

* Earlier version UI sometimes displayed successful extraction even though log showed errors.

## Code Refactoring Tools {#code-refactoring-tools}

Follow this section to learn about what is new and the updates for Code Refactoring Tools.

### What's New {#what-is-new-refactoring}

* AIO-CLI plugin released to unify code refactoring tools to enable developers to invoke and execute code refactoring tools from one place. See [Git Resource: aio-cli-plugin-aem-cloud-service-migration](https://github.com/adobe/aio-cli-plugin-aem-cloud-service-migration) for more details.

* AEM Dispatcher Converter extended to support conversions of On-premise and Adobe Managed Services Dispatcher configurations into AEM as a Cloud Service compatible Dispatcher configurations. See [Git Resource: AEM Cloud Service Dispatcher Converter](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/dispatcher-converter) for more details.

* AEM Dispatcher Converter re-written in ` node.js ` and integrated with AIO-CLI plugin.
