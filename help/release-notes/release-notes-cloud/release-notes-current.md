---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
---

# Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the general Release Notes for [!DNL Experience Manager] as a Cloud Service.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2021.1.0 is February 3, 2021.
The following release (2021.2.0) will be on February 25, 2021.

## [!DNL Adobe Experience Manager Sites] as a Cloud Service {#sites}

### Headless Content Management {#headless}

* **[GraphQL API for Content Fragment Delivery](/help/assets/content-fragments/graphql-api-content-fragments.md)**: Ability to query Content Fragments using GraphQL syntax, and schemas based on Content Fragment models, for output in JSON format.

* **[Authentication Support for GraphQL API Requests](/help/assets/content-fragments/graphql-authentication-content-fragments.md)**: Ability to authenticate GraphQL API requests with access tokens for server-side APIs.

* **[The RemotePage Component](/help/implementing/developing/hybrid/remote-page.md)**: Added support for viewing and editing external SPAs within AEM using.

* **[Editing an External SPA within AEM](/help/implementing/developing/hybrid/editing-external-spa.md)**: Added ability to upload a standalone single-page application to an AEM instance, add editable sections of content, and enable authoring.

* Enhanced JSON output from GraphQL API, including ability to output rich text in JSON format and locales.

* Support for nesting Content Fragment models to allow creating nested Content Fragment structures, via dedicated Content Fragment Reference data types or Content Fragment references inline in multiline text fields.

* Additional validation rules available in Content Fragment model data types, including "unique", "required" and "translatable".

* Ability tag Content Fragment models, and to allow Content Fragment creation in a folder with policies by tags or paths.

* Usability enhancements in Content Fragment editor, including publish action and display of model a fragment is based on.

* Ability to preview JSON output directly in Content Fragment editor.

<!--
### Progressive Web Apps (PWAs) {#pwa}

* [A Progressive Web App (PWA) version of a site](/help/sites-cloud/authoring/features/enable-pwa.md)  can now be enabled at the project level via simple configuration.
-->

## [!DNL Adobe Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

* [!DNL Experience Manager] as a [!DNL Cloud Service] extends the Smart Tags functionality to support the identification of keywords and entities in text-based assets. The text is identified, indexed, and is made available as metadata to improve the search experience without the need for any configuration. See [Smart Tags](/help/assets/smart-tags.md).

* MXF file format is now supported. See [supported file formats](/help/assets/file-format-support.md#video-formats).

## Adobe Experience Manager Commerce as a Cloud Service {#cloud-services-commerce}

### What is New {#what-is-new-commerce}

* Product Experience Management: New 'Commerce' properties tab for Assets and Experience Fragments. This tab enables you to link products / categories to Assets and Experience Fragments. The tab also shows real-time data for linked products / categories, and a link to show details in the product console.

* Released CIF Venia Reference Site - 2021.02.02 that includes the latest CIF Core Components version v1.7.0. Refer to [CIF Venia Reference Site](https://github.com/adobe/aem-cif-guides-venia/releases/tag/venia-2021.02.02) for more details.

* Released CIF Core Components v1.7.0. Refer to [CIF Core Components](https://github.com/adobe/aem-core-cif-components/releases/tag/core-cif-components-reactor-1.7.0) for more details.

## Cloud Manager {#cloud-manager}

### Release Date {#release-date-cm}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.2.0 is February 11, 2021.

### What is New {#what-is-new-cloud-manager}

* Cloud Manager Production pipeline will now include Custom UI testing capability.

* Assets customers will now be able to choose when and where to deploy their Brand Portal instance in a self-service way via Cloud Manager UI. For a regular (non sandbox) program with Assets solution, Brand Portal can now be provisioned on the Production environment. The provisioning can be done only once on Production environment.

* The AEM Project Archetype used in Project and Sandbox Creation has been updated to version 25. 

* The list of deprecated APIs identified during code scanning has been refined to include additional classes and methods deprecated in the latest Cloud Service SDK releases.

* SonarQube profile for Cloud Manager updated to remove Sonar rule squid:S2142. This will no longer conflict with Thread Interruption checks.

* Cloud Manager UI will inform the user who may not temporarily not be able to add/update domain name because the associated environment either has a running pipeline attached to it or currently in the waiting for the approval step.

* Properties set in customer `pom.xml` files prefixed with sonar will now be dynamically removed in order to avoid build and quality scanning failures.

* Cloud Manager UI will inform the user who may not temporarily not be able to select an SSL certificate if it is in use by a Domain name that's currently being deployed.

* Additional Code Quality Rules have been added to cover Cloud Service Compatibility issues.

### Bug Fixes {#bug-fixes-cloud-manager}

* Matching SSL certificate against a domain name is no longer case sensitive.

* Cloud Manager UI will now inform a user if the certificate private keys does not meet the 2048 bit limit with an appropriate error message.

* Cloud Manager UI will inform the user who may not temporarily not be able to select an SSL certificate if it is in use by a Domain name that is currently being deployed.

* In some cases, an internal issue may cause environment deletion to be stuck.

* Some pipeline failures were incorrectly reported as pipeline errors.

## AEM as a Cloud Service Foundation {#aem-as-a-cloud-service-foundation}

### What is New {#what-is-new-foundation}

* Server-to-server authenticated API calls - Generate the appropriate access tokens to make authenticated server-to-server API calls between your external applications and AEM as a Cloud Service environments. Learn more by reading [the documentation](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md) or by consulting the [tutorial](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/overview.html?lang=en#authentication).

### SDK Build Analyzers {#sdk-build-analyzers}

The AEM as a Cloud Service SDK Build Analyzer Maven Plugin detects problems in a maven project, including missing dependencies. It gives developers an opportunity to discover issues during local development, well before deploying to Cloud environments with Cloud Manager.

Two new analyzers have been added for this release:

* repoinit analyzer
* bundle-nativecode

For more information, see the documentation [here](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/build-analyzer-maven-plugin.html?lang=en#developing).

## Cloud Transition Tools {#code-transition-tools}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v1.2.2 is February 01, 2021.

### What is new in [!DNL Content Transfer Tool] {#what-is-new-ctt}

* New capability and UI added to Content Transfer Tool – User Mapping Tool. This features automatically maps existing user and groups to their Adobe Identity Management System IDs as part of the content migration activity. Refer to [Using User Mapping Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-user-mapping-tool.html) for more details.
* Content Transfer Tool now migrates all groups and users referenced in the migration set including children.
* Users are allowed to select certain paths under `/etc` when creating migration sets.
