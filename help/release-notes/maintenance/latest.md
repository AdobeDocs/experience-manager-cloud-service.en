---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 17569 {#release-17569}

Summarized below are the continuous improvements for maintenance release 17569, which was publicly released on August 27, 2024. The previous maintenance release was release 17465.

The 2024.9.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-17569}

* CQ-4353778 - Translation Process Events.
* CQ-4354583 - Send translation process events via Adobe Pipeline.
* CQ-4356479 - Allow only Adobe code to use the /adobe servlet context.
* CQ-4358133 - optimize Jenkins worker usage.
* CQ-4358226 - Save Translation keyword functionality doesn't work for particular String format.
* CQ-4358270 - AEM Translation Kit: August 08.
* CQ-4358310 - Add oak-compat-query-spi-1.2 to quickstart.
* GRANITE-36205 - Automated update for internal oak release in QS.
* GRANITE-49833 - Batching support for event sender and proxy.
* GRANITE-52053 - Remove usages of Commons Collections 3 - Platform others.
* GRANITE-52492 - Elastic async catchup in case of PIT restore.
* GRANITE-53086 - Update jacoco plugin version to 0.8.12 in AEMaaCS.
* GRANITE-53099 - Update to Apache Felix Http Jetty 5.1.24.
* GRANITE-53125 - Add classification to CloudEvent.
* GRANITE-53328 - Update Filevault to 3.8.0-T20240726111512-3cc11d50 containing stashing logging improvements.
* GRANITE-53340 - AEM660: Proper Versioning and branching for 660 CQ/Platform.
* GRANITE-53341 - Dont warn on usage of ACS Commons 6.
* GRANITE-53453 - update commons-lang to 3.15.0.
* GRANITE-53473 - Undeprecate Sling Settings.
* GRANITE-53478 - Update Filevault to version 3.8.0.
* GRANITE-53505 - Update QS to commons-collections-3.2.2-adobe-2.
* GRANITE-53528 - Update version of platform artifacts .
* GRANITE-53547 - Provide alternative API avoiding usage of Apache Commons Lang 2.
* GRANITE-53575 - Use BSAFE 6.2.5 in CS.
* GRANITE-53608 - Update Oak to latest public release (1.68.0).
* SITES-23583 - Sites Evergreen tests fail on Java 17.
* SKYOPS-79535 - Update to rum script v2.
* SKYOPS-79816 - Enable Sling Feature Analyzer Task for Service User Mappings in FACT Tool.
* SKYOPS-81179 - AEM builds testing for bundles toggling.
* SKYOPS-81866 - Report warnings for bundles known to be incompatible with Java 21.
* SKYOPS-82660 - Update Sling API to 2.27.6.
* SKYOPS-82961 - Update to Sling ResourceResolver 1.12.0-T20240723153354-a0270a0.
* SKYOPS-83356 - Create global dashboard for tracking JVM versions used in AEM deployments.
* SKYOPS-83436 - Java Runtime 21 rollout breaks creation of adaptive forms AEM Forms.
* SKYOPS-84272 - Log the java version used on aem launcher startup.

### Fixed Issues {#fixed-issues-17569}

* CMGR-60225 - Pipeline execution failure identified on AEM Sites CS customer while validating update to AEM release 17486
* GRANITE-45919 - Embargoed countries in Country/Region list in Edit User Settings
* GRANITE-51715 - Picker does sometimes not enter the selection into the text field
* GRANITE-53290 - Correctly check the protocol when parsing the URL in the XSS check
* GRANITE-53576 - Wrong definition of service ranking in OSGi configurations
* SKYOPS-82129 - Memoryleak in Sling Models

### Known Issues {#known-issues-17569}

None.

### Change Notice {#change-notice-17569}

* Starting in September 2024, AEM as a Cloud Service will disable the serialization of Resource Resolvers via the Sling Model Exporter framework. See [the documentation](/help/implementing/developing/hybrid/disallow-the-serialization-of-resourceresolvers-via-sling-model-exporter.md) for more details.

### Deprecated Features and APIs {#deprecated-17569}

Please note that we are in the proces of updating `com.day.cq.wcm.api` and with the current release, we have marked as `@Deprecated` a few of its methods and classes. These will be removed in future releases, so please consider switching to their suggested alternatives if you are using any of them.

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-17569}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 4 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-17569}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.68.0|[Oak API 1.68.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.68.0/index.html)| 
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.24-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.26.0|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
