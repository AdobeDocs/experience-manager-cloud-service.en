---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 18099 {#release-18099}

Summarized below are the continuous improvements for maintenance release 18099, which was publicly released on October 9, 2024. The previous maintenance release was release 17964.

The 2024.10.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-18099}

* ASSETS-43015: Update to latest auth.ims bundle.
* ASSETS-41684: Update src/main/features/docker/ethos/base-ims-oauth.json.
* ASSETS-38322: Enabling http request event for AEM.
* ASSETS-41684: Add OOB OSGI configs to define FI to group mapping for Assets, Foundation, Sites, and Forms.
* ASSETS-41448: Update auth.ims bundle to support FI to group mappings.
* CQ-4356633: Add extra character in "Content Only" tooltip.
* SITES-23584: Foundation component tests fail on Java 17.
* GUIDES-19069: Add guidesPeerLinkIndex for aem guides add on.
* GRANITE-54300: Update Oak to latest public release (1.70.0).
* GRANITE-54274: Accept Firefly IMS client.
* GRANITE-36205: Update internal oak release version to latest.
* GRANITE-54266: Production SDK missing Search Suggestor service.
* GRANITE-50948 -Integrate repository service into AEM Add alternative repository service for local development.
* GRANITE-53966: Use separate thread pool for content-distribution.
* GRANITE-53514: Treeactivation 1.0.26.
* GRANITE-54054: Environment variable for com.adobe.granite.repository.impl.SystemUserValidation warnOnly.
* GRANITE-50948: Integrate repository service into AEM Support for repository service.
* GRANITE-52454: Adding support helper 0.1.2.
* GRANITE-53514: Treeactivation 1.0.26.
* GRANITE-54038: Add the Creative Cloud Enterprise IMS client to the AEM IMS client allowlist.
* GRANITE-36205: Update internal oak release version to latest.
* GRANITE-53485: Support Service Principal authentication for replication Azure Blob Storage.
* GRANITE-54006: update Jackson to 2.17.2.
* GRANITE-53287: Updating security-privileges integration test version.
* GRANITE-53914: Platform test failures with Java 17 Updated module version.
* GRANITE-53870: Create internal mechanism to skip max JVM version check for the quickstart.
* GRANITE-52454: Upgrading Support Helper GRANITE-52454 upgrading support helper to use latest release for AEMaaCS.
* SKYOPS-85335: Update org.apache.sling.jcr.repoinit to 1.1.52.
* SKYOPS-85336: Update Sling Commons Threads to 3.3.0.
* SKYOPS-76378: Improve thread-safety of ResourceBundle registration/deregistration in i18n.
* SKYOPS-84951: Mutable content checksum generation code is incorrect.
* SKYOPS-82383: Expose the 'helm-values' convert-merge-analyse result in the command execution descriptor.
* SKYOPS-86329: updating versions of platform test modules for java 21 sdk support.
* SKYOPS-69768: SlingModels do not deserialize ResourceResolvers.
* SKYOPS-84810: skip "40-initialize-publish.sh" execution on startup for RDE.
* SKYOPS-79285: Update Sling XSS to 2.4.2

### Fixed Issues {#fixed-issues-18099}

* CNTBF-298: Remove jcr:uuid from CC exported packages.
* SKYOPS-83910: Fix concurrency issues found in SKYOPS-82371. 
* GRANITE-52876: Update to com.adobe.granite.ui.content 0.8.1448.
* GRANITE-53088: Regression introduced by the fix of SITES-11992.
* GUIDES-14445: Native PDF generation fails with an error related to getting dependencies for Node.js.
* GUIDES-16961: The title with `<conref>` doesn't resolve in the Baseline and Translation dashboards of the Web Editor.
* GUIDES-17283: When selecting the **Use metadata added in the topicmeta** option, the metadata properties are not propagated in the document proprieties of the Native PDF output.
* GUIDES-17793: The referenced PDF isn’t activated from the **Bulk Publish Dashboard** during the Bulk Activation of published content.
  
For more information about the new and enhanced Guides features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap).

### Known Issues {#known-issues-18099}

* FORMS - 15818: Component descriptor entry `OSGI-INF/com.adobe.aemfd.docmanager.impl.*.xml` not found statements in server logs. These are harmless log statements.

### Deprecated Features and APIs {#deprecated-18099}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

The following is a summary of recently-deprecated features or those in the process of deprecation.

#### JavaScript Use API {#javascript-use-api}

[The JavaScript Use API](https://github.com/adobe/htl-spec/blob/master/SPECIFICATION.md#42-javascript-use-api) is officially deprecated due to challenges users have debugging and maintaining code that leverages the API, as well as performance limitations compared to the Java alternative.

You should should transition to [the Java Use API,](https://experienceleague.adobe.com/en/docs/experience-manager-htl/content/java-use-api) which offers better performance, easier debugging, and greater long-term support.

#### com.day.cq.wcm.api {#com-day-cq-wcm-api}

Please note that Adobe is in the process of updating `com.day.cq.wcm.api`. Some of its methods and classes have been marked as `@Deprecated` in the current release. These will be removed in future releases. Please consider switching to their suggested alternatives.

#### org.apache.jackrabbit.oak.plugins.blob {#org.apache.jackrabbit.oak.plugins.blob}

* GRANITE-54165: Deprecate org.apache.jackrabbit.oak.plugins.blob in public API.

### Security Fixes {#security-18099}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 2 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-18099}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.70.0|[Oak API 1.70.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.70.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.24-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.27.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
