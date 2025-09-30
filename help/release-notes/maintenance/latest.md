---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 22758 {#22758}

Summarized below are the continuous improvements for maintenance release 22758, which was publicly released on October 1, 2025. The previous maintenance release was release 22450.

The 2025.10.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-22758}

* ASSETS-56227: Rename adobe-countdown-timer modifier
* CNTBF-493: Bump content-backflow bundle version to 2.0.28
* CQ-4361110:  Granite translations
* CQ-4361112:  Latest AEM translations
* GRANITE-56026: Improve permissions API status code responses
* GRANITE-56970: Upgrade crypto bundles
* GRANITE-61015: Added 'org.apache.commons.io.channels' package in public exported list
* GRANITE-61167: Felix log has been updated to latest OSGI spec
* GRANITE-61167: Update felix dependencies
* GRANITE-61169: Improve the check for protected strings
* GRANITE-61278: Update org.apache.commons:commons-email to version 1.6.0
* GRANITE-61278: Update org.apache.sling:org.apache.sling.commons.log.webconsole to version 1.0.2
* GRANITE-61278: Update org.apache.commons:commons-compress to version1.28.0
* GRANITE-61278: Update org.apache.commons:commons-exec to version 1.5.0
* GRANITE-61278: Update org.apache.sling.installer.provider.file to version 1.3.4
* GRANITE-61278: Update org.apache.sling:org.apache.sling.installer.provider.jcr to version 3.3.0
* GRANITE-61327: Adjust toggle name for Sling Resource Resolver fallback
* GRANITE-61622: Update sling dependencies
* GRANITE-61663: Add com.adobe.granite.repository.indexdefs-1.0.2 to quickstart
* GRANITE-61811: Add com.adobe.granite.repository-2.0.0 to quickstart
* GRANITE-62026: Update CS Quickstart: latest public release of Oak (1.86.0)
* SITES-32014: Listen for external events too to update service regs
* SITES-33206: KonMari 2025 tools allow for "soft deprecation" of AEM modules
* SITES-34277: Fix blocking error in translations workflows for pages
* SKYOPS-105553: Re-adding experimentation  it was missed the inclusion last time
* SKYOPS-108706: Upgraded release toggles bundle to latest version (etag caching)
* SKYOPS-114210: Updating to latest version of aem.pss.service bundle
* SKYOPS-115287: Update AEM-CS SDK clientlib compiler defaults to match transform job settings
* SKYOPS-115792: Update CS Quickstart: Sling ResourceResolver 1.12.11-T20250827104939-c451842
* SKYOPS-116171: Update to Sling ResourceResolver 1.12.12
* Released dispatcher-publish 2.0.258

### Fixed Issues {#fixed-issues-22758}

* GRANITE-61875: Fix triggers “invalid expression evaluation” – Authors cannot save Content Fragments & assets fail to download
* GRANITE-62115: Upgrade com.adobe.granite.crypto
* SITES-22059: Fixes JS error in PDF Viewer components  Unlocalized "File preview not available" string in Core Components site > PDF Viewer
* SKYOPS-118793: Reverting back vanity urls changes
* SITES-30879: AEM: Unlocalized strings in Sites > Page Editor > Search component
* GRANITE-59704: Fixed htmllibmanager.debug causes edit mode to fail
* GRANITE-61042: Integrate FELIX-6796 (ServiceTracker NPE fix) into AEM Felix Web Console bundle
* GRANITE-61165: Workspace.copy() throwing RepositoryException
* GRANITE-61875 : Updated ui.commons to 5.10.50
* SITES-34277: Fix blocking error in translations workflows for pages

### Known Issues {#known-issues-22758}

None.

### Deprecated Features and APIs {#deprecated-22758}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-22758}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 13 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-22758}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.86.0|[Oak API 1.86.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.86/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.65 | [Apache Httpd 2.4.65](https://apache.googlesource.com/httpd/+/refs/tags/2.4.65/CHANGES)|
|AEM Core Components| 2.30.1|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
