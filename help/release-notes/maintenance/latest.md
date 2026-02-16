---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 24464 {#release-24464}

Summarized below are the continuous improvements for maintenance release 24464, which was publicly released on February 17, 2026. The previous maintenance release was release 24288.

The 2026.2.0 feature activation provides the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-24464}

* AEMARCH-264: Add support for validating conditional requests based on RequestEntity.
* AEMARCH-269: Expose JavaEE validation APIs for OpenAPI implementations.
* AEMARCH-276: Provide i18n support through RequestEntity.
* ASSETS-10995: Set limit on number of assets in download zip.
* ASSETS-50788: Update Search API to use Asset Metadata GET API.
* ASSETS-50946: Map request body using Metadata GET API to JCR metadata.
* ASSETS-55866: Avoid submitting new request for same asset until previous processing is complete.
* ASSETS-60300: Provide API to retrieve async job context and result.
* ASSETS-60574: Add support for latest version of Sling API bundle.
* ASSETS-61049: Continue metadata manager bundle development.
* ASSETS-61692: Perform semantic search by default in Search Open API.
* ASSETS-61696: BAM route and MFE wrapper on assets view.
* ASSETS-61854: Send GenStudio solution in activation/deactivation message.
* ASSETS-61973: Create API in AEM for managing prompts.
* ASSETS-62182: Asset Compute event handler for c2pa-manifest rendition.
* ASSETS-62413: Add support for customModifier field in every layer in JSON.
* ASSETS-62432: Merge folder delete API PR.
* ASSETS-62540: Increase ui-touch-optimized version in quickstart.
* ASSETS-62622: Handle search mode in MatchQuery.
* ASSETS-62780: Add feature toggle for folder API.
* ASSETS-62988: Hide c2pa manifest rendition from showing in renditions tab.
* ASSETS-63336: Template syncing from AEM to DM should only happen for dam namespaced metadata.
* ASSETS-63375: Put asset upload experimental OpenAPIs behind feature toggle.
* GRANITE-63744: Allow connecting async jobs to sling jobs.
* GRANITE-64567: Automatically disable semantic search for SKU searches.
* GUIDES-41187: Add headers for Guides usage.
* SITES-30452: Content API with ASO - title & description suggestions.
* SITES-34234: Page editor: preserve content tree state.

### Fixed Issues {#fixed-issues-24464}

* ASSETS-43198: Asset expiration notification emails do not respect user language preference.
* ASSETS-52061: Unable to navigate back after selecting saved search.
* ASSETS-53745: Dynamic Media download flow requires unselecting original asset before choosing web preset.
* ASSETS-59213: cq-dynamicmedia-core depends on deprecated commons-lang library.
* ASSETS-59214: cq-scene7-imaging depends on deprecated commons-lang library.
* ASSETS-59546: cq-remotedam-client-core depends on deprecated commons-lang library.
* ASSETS-59703: cq-dam-core depends on deprecated commons-lang library.
* ASSETS-59705: cq-dam-handler depends on deprecated commons-lang library.
* ASSETS-59707: cq-dam-indesign depends on deprecated commons-lang library.
* ASSETS-59709: cq-scene7-core depends on deprecated commons-lang library.
* ASSETS-59929: CSV from metadata export breaks when field has newline character.
* ASSETS-60241: Async move job fails when renaming folder.
* ASSETS-61134: Remove comparisonVersion tags from pom files.
* ASSETS-61309: Content Fragment move/copy no longer updates internal references.
* ASSETS-61730: Redirect to Direct Binary Access should respect asset encoding.
* ASSETS-62311: Search regression issues.
* ASSETS-62358: Assets report CSV shows corrupted values in content path.
* ASSETS-62610: Adobe Stock license button disabled in Assets UI.
* ASSETS-62613: NPE in `downloadasset`/`saveas`.
* ASSETS-62656: Omnisearch AI search indicator incorrectly shown for non-Assets searches.
* ASSETS-62671: Fix MatchQuery startsWith operator.
* ASSETS-62882: Info icon tooltip breaks when multiple invalid filenames uploaded.
* GRANITE-55387: Correcting word enclosed in quotes deletes entire word.
* GRANITE-64101: OOTB indexes converted to ES reverted back to Lucene on restart.
* GS-24323: Remove `/conf/genstudio` folder for JPMC.
* SITES-24530: Touch target of close/remove buttons in search modal not large enough.
* SITES-31425: Unlocalized error message in start workflow.

### Known Issues {#known-issues-24464}

None.

### Deprecated Features and APIs {#deprecated-24464}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-24464}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 14 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-24464}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.90.0|[Oak 1.90.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.90.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.65 | [Apache Httpd 2.4.65](https://apache.googlesource.com/httpd/+/refs/tags/2.4.65/CHANGES)|
|AEM Core Components| 2.30.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
