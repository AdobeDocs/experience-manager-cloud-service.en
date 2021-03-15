---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
---

# Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the general Release Notes for the current (latest) version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>From here you can navigate to release notes of previous versions; for example, for those in 2020, 2021 and so on.

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2021.3.0 is March 25, 2021.
The following release (2021.4.0) will be on April 29, 2021.

## [!DNL Adobe Experience Manager Sites] as a Cloud Service {#sites}

<!--
### Progressive Web Apps (PWAs) {#pwa}

* [A Progressive Web App (PWA) version of a site](/help/sites-cloud/authoring/features/enable-pwa.md)  can now be enabled at the project level via simple configuration.
-->

## Cloud Manager {#cloud-manager}

This section outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.3.0.

## Release Date {#release-date-cm-march}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.3.0 is March 11, 2021.

### What's New {#what-is-new-march}

* Customers with environments with pre-existing CDN configurations for IP Allowlists, SSL certificates and custom domain names will see a message about their previously existing configurations and will be able to self-serve via the UI. Users can now:
   * Add Sites solution to an existing program with Assets (or vice-versa).
   * Remove Sites (or Assets) from an existing program with both Sites and Assets.
   * Add second, unused solution entitlement either to an existing program or as a new Program.

* Users with requisite permission can now Edit Program, allowing them to do the following in a self-service manner. 

* AEM Push Update" label will now be displayed for both Pipeline Execution and Activity screens.

*  If an environment is hibernated but there is also an AEM update available, the “Hibernated” status will take precedence over “Update available”.

* Users can now see their Cloud Manager role(s) by selecting the 'View Cloud Manager Role(s)' option after navigating to the User Profile icon (top right) of Unified Shell. 

* The label "Application for Approval" has been relabeled to "Production Approval" for greater clarity.

* The "Version" label has been relabeled to "Git Tag" in the Production pipeline execution screen.

* The labels which define the behavior when important metrics do not meet the defined threshold have been relabeled to reflect their true behavior – Cancel Immediately and Approve Immediately.

* The class and method deprecation lists have been updated based on version `2021.3.4997.20210303T022849Z-210225` of the AEM Cloud Service SDK.

* Cloud Manager Production pipeline will now include Custom UI testing capability.

### Bug Fixes {#bug-fixes-cm-march}

* Package versioning was skipped in some cases during AEM push upgrade.

* Some quality issues were not properly discovered when packages were embedded in other packages.

* In obscure situations, the default program name generated upon opening the Add Program dialog could be a duplicate of an existing program name. 

* On occasion, if user navigates away from pipeline execution page immediately after starting a pipeline, an error message is displayed stating that the action failed, although the execution actually starts.

* The build step was unnecessarily restarted when customer builds resulted in invalid packages.

* On occasion, user may see a green "active" status next to an IP Allowlist even when that configuration was not deployed.

* All existing production pipelines will be automatically enabled with the Experience Audit step.


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

### Release Date {#release-date-ctt-march}

The Release Date for Content Transfer Tool v1.3.0 is March 04, 2021.

### What is new in Content Transfer Tool {#what-is-new-ctt-march}

* CTT now installs to `/apps` instead of `/libs` Browser bookmarks to certain pages may no longer be valid.
* When CTT is installed, user will have to navigate an additional level to get to the Content Transfer page. See [Using Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html) for more details.

### Bug Fixes {#bug-fixes-ctt-march}

* When migrating content from a specific path, CTT was pulling in unrelated resources. This has been fixed

## Code Refactoring Tools {#code-refactoring-tools}

### What is new in Code Refactoring Tools {#what-is-new-crt}

* New features and enhancements for Repository Modernizer. Refer to [GitHub Resource: Repository Modernizer](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/repository-modernizer) for the latest version.
  * Normalize OSGi configs (except RepoInit configs) to the preferred .cfg.json format.
  * Rename OSGi config folders to the specified format.
  * Generate the ui.apps.structure project.
  * Create the analyze module.
  
* New features and enhancements for Dispatcher Converter. Refer to [GitHub Resource: Dispatcher Converter](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/dispatcher-converter)
  * Creation of separate files for different inclusions instead of in lining the content.
  * Ability to handle both folder path of vhosts and path to vhost files.
  * Generation of farm files with large customer configurations in range of 600 and more.