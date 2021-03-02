---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
---

# Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the general Release Notes for [!DNL Experience Manager] as a Cloud Service.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2021.2.0 is February 25, 2021.
The following release (2021.3.0) will be on March 25, 2021.

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

## What is new in [!DNL Assets] {#what-is-new-assets}

*  Businesses can now source assets using [!DNL Brand Portal]. Asset sourcing feature leverages [!DNL Brand Portal] to help customers engage with agency users to source assets for new marketing campaigns, photoshoots and projects. See [asset sourcing in [!DNL Brand Portal]](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/asset-sourcing-in-brand-portal/brand-portal-asset-sourcing.html).

* The [!DNL Brand Portal] usage report now displays only the active users. The inactive users are not displayed now. Active users are the ones whose account is assigned to a product profile in the [!DNL Admin Console]. See [[!DNL Brand Portal] reports](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/admin-tools/brand-portal-reports.html).

* In [!DNL Brand Portal], a new download setting is introduced, that lets you create separate folder for each asset when downloading folders, collection, and so on. See [download settings](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/download/brand-portal-download-assets.html).

<!-- TBD: refine this list of features and enh. for Feb release.

Customers using the Connected Assets feature can now easily view and track assets used on remote Sites instances. This affords customers a complete view of being used across all Sites powered pages, allowing for better tracking, management, and brand consistency.  -->

## Bug fixes in [!DNL Assets] {#bug-fixes-assets}

* When a new version of an existing asset is created after resolving the naming conflict, the metadata of original asset is overwritten. (CQ-4313594)
* When an asset with long annotation text is printed, the annotation text is trimmed, even if space is available. (CQ-4314101)
* When multiple assets are selected to update the properties, sometimes either an error occurs or properties of a deselected asset get updated. (CQ-4316532)
* When attempting to open [!UICONTROL Assets Admin Search Rail], the page remains blank and clicking on [!UICONTROL Edit] > [!UICONTROL Settings] generates an error. (CQ-4315079)

## Cloud Manager {#cloud-manager}

### Release Date {#release-date-cm}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.2.0 is February 11, 2021.

### What is New {#what-is-new-cloud-manager}


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

## Content Transfer Tool {#content-transfer-tool}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v1.2.4 is February 10, 2021.

### Bug Fixes {#bug-fixes-ctt}

* When mapping multiple users, some users’ IMS IDs were being mapped incorrectly. This has been fixed.

### Release Date {#release-date-ctt-feb}

The Release Date for Content Transfer Tool v1.2.2 is February 01, 2021.

### What is new in Content Transfer Tool {#what-is-new-ctt}

* New capability and UI added to Content Transfer Tool – User Mapping Tool. This features automatically maps existing user and groups to their Adobe Identity Management System IDs as part of the content migration activity. 
    Refer to [Using User Mapping Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-user-mapping-tool.html) for more details.
* Content Transfer Tool now migrates all groups and users referenced in the migration set including children.
* Users are allowed to select certain paths under `/etc` when creating migration sets.

## Best Practices Analyzer {#best-practices-analyzer}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.2 is February 18, 2021.

### What is new in Best Practices Analyzer {#what-is-new-bpa}

* Ability to detect the use of AEM Forms and AEM Forms implementation and indicate areas that are relevant to migrating to AEM Forms as a Cloud Service.
* Ability to detect and report on usage and count of custom components and templates.
* Ability to detect the type of node store and data store used.
* Ability to detect the usage of Dynamic Media.
* Ability to detect the Java version used.

## Code Refactoring Tools {#code-refactoring-tools}

### What is new in Code Refactoring Tools {#what-is-new-crt}

* New version of AIO-CLI plugin released. Latest version of this plugin includes several bug fixes for the Repository Modernizer. 
   Refer to [Unified Experience](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/refactoring-tools/unified-experience.html?lang=en#benefits) to learn more about this plugin.

### Bug Fixes {#bug-fixes-crt}

* Several bug fixes done on the Repository Modernizer. 
   Refer to [GitHub Resource: aem-cloud-service-source-migration](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/repository-modernizer) for more details.








