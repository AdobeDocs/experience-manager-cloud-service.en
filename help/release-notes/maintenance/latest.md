---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

>[!NOTE]
>
>Release 23122 has been made private on November 3rd.

## Release 22943 {#22943}

Summarized below are the continuous improvements for maintenance release 22943, which was publicly released on October 14, 2025. The previous maintenance release was release 22758.

The 2025.10.0 feature activation provides the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-22943}

* ASSETS-57809: Index definition update for damAssetLucene-13.
* ASSETS-36521: Improved DM Reupload Workflow to Ensure Consistent Post-Processing.
* ASSETS-56400: Added new OOTB Zoom PNG rendition for assets with transparency.
* ASSETS-55326: Enabled AI metadata folder config view through HTTP events.
* ASSETS-56905: Support connection to Indesign via proxy.
* ASSETS-48286: Add CAI properties to Algolia for GenStudio.
* ASSETS-48653: Apply the invisible watermark in the preprocessing phase.
* ASSETS-55874: Migrating image preset from scene7 to DMWithOpenapi.
* SITES-30452: Content API improvements for ASO on the /content/definition endpoint.
  
### Fixed Issues {#fixed-issues-22943}

* ASSETS-56301: Fixed selective metadata export to include PredictedTags in CSV.
* ASSETS-55543: Refactored async processing logic into a reusable bundle.
* ASSETS-54789: Fixed NPE in ACLPermissionsValidator when DM ACL is enabled.
* ASSETS-55888: Fixed malware rendition appearing in the UI renditions panel.
* GRANITE-62236: Fixed keyword localization issue in saved searches for smart collections.
* GRANITE-61875: Fixed “invalid expression evaluation” hotfix issue preventing saving Content Fragments and asset downloads.
* SITES-24074: Fixed hidden mobile navigation receiving focus during keyboard tab navigation.
* SITES-33611: Fixed Live Copy Overview issue for high-volume markets.

#### AEM Guides {#guides-22943}

* GUIDES-31421: When multiple DITA maps or topics are open and one of the topics is closed, the **>>** button which showcases all the open tabs gets overlapped with the remaining open tabs on the Tab bar.
* GUIDES-33229: When generating PDFs, the filtering rules in a DITAVAL file are ignored if any property name contains a period.
* GUIDES-33720: When zooming in the screen of Translation UI, the Send for Translation button moves under the ellipsis and becomes enabled even without any asset being selected.
* GUIDES-33590: When a reviewer completes a review task or initiator updates review task without entering comments, the notification email sent displays the most recent previous comment.

For more information about the new and enhanced features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap). 

### Deprecated Features and APIs {#deprecated-22943}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-22943}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 14 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Change Notice

* This release contains the following new product index versions:
* **damAssetLucene-13**

### Embedded Technologies {#embedded-tech-22943}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.86.0|[Oak 1.86.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.86/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.65 | [Apache Httpd 2.4.65](https://apache.googlesource.com/httpd/+/refs/tags/2.4.65/CHANGES)|
|AEM Core Components| 2.30.2|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
