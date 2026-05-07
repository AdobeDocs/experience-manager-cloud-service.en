---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 25892 {#release-25892}

Summarized below are the continuous improvements for maintenance release 25892, which was publicly released on May 5, 2026. The previous maintenance release was release 25520.

The 2026.5.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

>[!NOTE]
>
>Release 25821 has been made private. 

### Enhancements {#enhancements-25892}

* CQ-4362304: Create Guidelines frontend and update LLM config UI.
* GRANITE-39546: Upgrade Apache Tika to 3.x.
* GRANITE-53957: Upgrade Azure SDK V8 to V12 for oak-blob-azure.
* GRANITE-61245: Remove all usage of commons-lang (replace with commons-lang3).
* GRANITE-64748: Bump OIDC authentication handler.
* GRANITE-64764: Update Apache Commons Text to 1.15.0.
* GRANITE-64963: Update Filevault to 4.2.0.
* GRANITE-66197: Add Microsoft Graph API email support for M365 tenants.
* GRANITE-66449: Update Maven plugins for Java 17 API support.
* GRANITE-66473: Add Caffeine cache library to base-granite.
* GRANITE-66836: Update Quickstart to Oak 2.0.0.
* SKYOPS-129301: Set APIs jar Javadoc compliance level to Java 17.
* SKYOPS-129351: Update reactive-streams and reactor-core for MCP SDK compatibility.
* SKYOPS-131412: Update Apache Commons Exec to latest version.
* SKYOPS-131432: Update Felix SCR to 2.2.14.
* SKYOPS-131907: Update Sling API Regions to 1.1.10.
* SKYOPS-131938: Update GSON to latest version.
* SKYOPS-132173: Update Apache Commons Codec to latest version.
* SKYOPS-132182: Update Sling Tenant bundle.
* SKYOPS-132267: Update `org.osgi.service.component` annotation.
* SKYOPS-132272: Update Sling Feature Model bundle.
* SKYOPS-132525: Add Quickstart analyser to prevent new API removals.
* SKYOPS-134408: Update `com.adobe.granite.asset.core` to 2.2.82.
* SKYOPS-137750: Update `com.adobe.granite.comments` to 1.0.40.
* SKYOPS-137759: Update `com.adobe.granite.jobs.async.ui.commons` to 3.2.4.
* SKYOPS-138356: Update `com.adobe.granite.oauth.server` to 1.1.36.
* SKYOPS-138739: Update SnakeYAML to 2.6.

### Fixed Issues {#fixed-issues-25892}

* ASSETS-59546: Remove dependencies on deprecated commons-lang library.
* ASSETS-64831: AssetProcessorProcess resetting processing attempt count causes stuck assets.
* ASSETS-66683: Approval loop caused by uploadBlob failure.
* CNTBF-613: Fix Access Denied (JCR-101) when registering node types.
* GRANITE-44537: String in "Country/Region" not localized in AEM.
* GRANITE-61760: Fix failed activation of AdminUserInitializer.
* GRANITE-64543: Permission restrictions response does not follow API structure.
* GRANITE-66692: Internal classloader not sensitive to package refreshes.
* GRANITE-66732: Use activators instead of service components for start level 1 bundles.
* GRANITE-66846: AEM Permissions API does not show `rep:ntNames` restriction.
* SITES-39267: Restore pagePath in relationship chain entries.
* SITES-43715: Permission validation fails reading the resource status.

#### AEM Guides {#guides-25892}

* GUIDES-45110: When selecting an image in the Editor using the **Select file** dialog, only raster formats (such as JPG, PNG, and GIF) are displayed. Vector files (such as `.ai` and `.eps`) are not shown and cannot be selected.
* GUIDES-41938: Creating a topic in a folder with spaces in its name incorrectly creates a duplicate folder where spaces are replaced by hyphens, and the topic is saved there instead of the original folder.
* GUIDES-38377: When changes to an output preset in a Folder profile are applied to existing maps, the saved **Publish Context** for the AEM Sites preset is reset.
* GUIDES-43547: When large topics or maps are opened, the Author instance becomes unresponsive, requiring a restart in some cases.
* GUIDES-32520: When Backspace is used on elements, the Editor scrolls to the top of the topic regardless of the cursor position (Editor 2.0).

For more information about the new and enhanced features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap). 

### Known Issues {#known-issues-25892}

None.

### Deprecated Features and APIs {#deprecated-25892}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-25892}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 19 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-25892}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 2.0.0 | [Oak 2.0.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/2.0.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.65 | [Apache Httpd 2.4.65](https://apache.googlesource.com/httpd/+/refs/tags/2.4.65/CHANGES)|
|AEM Core Components| 2.30.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
