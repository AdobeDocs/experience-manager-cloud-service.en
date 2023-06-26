---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release X {#release-X}
 
Summarized below are the continuous improvements for maintenance release 12441, which was publicly released on June 28, 2023. This maintenance release is an update from previous maintenance release 12255.

2023.7.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information

### Enhancements {#enhancements-X}

- SITES-8316: Content Policies: Cache the ContentPolicyManager
- SITES-8769: [Styles] Improve StyleImpl calls in ResponsiveGrid
- SITES-13165: GraphQL - Ability to filter behavior for null values

### Known Issues {#known-issues-X}

None.

### Fixed Issues {#fixed-issues-X}

- Various vulnerability and accesibility fixes
- SITES-14073: CSV Report fails with 500 when selecting no property to export
- SITES-12577: Link checker transformer not rewriting links intermittently 
- SITES-12688: Logical operator OR not properly working in Asset Finder search
- SITES-4951: Tag-search in Page editor does not find sub-tags
- SITES-13559: 'Is not modifiable' exception thrown when rolling out component
- SITES-12715: Cloud service configs applied to Experience fragments folder do not persist
- SITES-11757: Inherit rollout configuration from Parent does not get reverted back for child pages
- SITES-12465: Arrow keys not working in Experience fragment component dialog
- SITES-12893: Apply circular reference validation for Experience Fragments
- SITES-13097: Not able to add experience fragments to a translation project

### Embedded Technologies {#embedded-tech-X}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.50-T20230405052634-f9df4aa|[Oak API 1.50.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.50.0/index.html)| 
|AEM SLING API |Version 2.27.0 |[Apache Sling API 2.27.0 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
