---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 14813 {#release-14945}

Summarized below are the continuous improvements for maintenance release 14813, which was publicly released on January 11, 2023. The previous maintenance release was release 14697.

2024.1.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-14945}

* ASSETS-32101: Metadata for smart crop renditions should be updated in DB.
* ASSETS-31297: Improve checks to prevent deletion of copied assets from dynamic media.

### Fixed Issues {#fixed-issues-14945}

Note: generated from prod-14697..d412fc5c0f
* ASSETS-15977: Remove deprecated v1 search events and pipeline producer.
* ASSETS-18088: Upgrade batik library dependencies to 1.17.
* ASSETS-21965: Metadata writeback workflow must only launch on asset metadata changes.
* ASSETS-26368: Scheduled Bulk Import Jobs Not Removed if Job Config does not Exist.
* ASSETS-26549: Assets / Nodes with "jcr:lastModifiedBy": "workflow-process-service" show as "external user" in list view.
* ASSETS-26842: Update "Firefly" text to read "App Builder" in Processing Profile.
* ASSETS-28708: Very slow response for some IMS token requests.
* ASSETS-28767: Inconsistent publish state on assets if folder containing large no. of assets published.
* ASSETS-29011: Smart crop is visible for read-only users.
* ASSETS-29348: AssetMoveEventHandler can consume too much memory.
* ASSETS-29738: Asset Upload Restriction fails with NullPointerException for woff files.
* ASSETS-30068: Bulk Import Asset Essentials to include status COMPLETED_WITH_ERROR for "job completed, but with error".
* ASSETS-30261: Incorrect imsUserId sent to Pipeline for asset events.
* ASSETS-30538: View Page option is Missing after Moving a PDF file.
* ASSETS-30626: Failure to create delivery request reported for assets with empty assetId.
* ASSETS-30756: Move Asset Wizard action fails when folder name ends in 'html'.
* ASSETS-30987: Update eventing bundle for ASSETS-30987.
* ASSETS-31015: Unable to upload Assets with .msg filename extension.  
* ASSETS-31038: Tasks events that are received by the notification service are not being processed.
* --- RESUME EDITING HERE ---
* ASSETS-31097: added exclusions for ui-wcm-commons changes. * ASSETS-31097 update ui-wcm-commons artifact. * ASSETS-31097 updated exclusions. * ASSETS-31097 updated exclusions. * ASSETS-31097 updated exclusions.
* ASSETS-31256: Update to cq-dam-core 5.15.64, cq-dam-processor-dm 1.0.54. Issues fixed: ASSETS-31256, ASSETS-29348.
* ASSETS-31260: Resolve select issues with schema forms.
* ASSETS-31274: Update to cq-dam-content 2.6.1606. Issues fixed: ASSETS-34088, ASSETS-33300, ASSETS-33296, ASSETS-31274, ASSETS-26489.
* ASSETS-31280: Update to cq-dam-content 2.6.1556, cq-dam-download 1.0.132. Issues fixed: ASSETS-27066, ASSETS-31280.
* ASSETS-31301: Add exclusions.
* ASSETS-31324: ASSETS-27529 and ASSETS-31324 updated XSS securities in DAM content.
* ASSETS-31330: Update dynamic media packages.
* ASSETS-31405: handle long running IDS SOAP post.
* ASSETS-31570: Unified shell - asset details "Save & Close", "Cancel" buttons need to be pressed more than once to work * ASSETS-31570 upgrade cq-dam-content content-model-sidecar.
* ASSETS-31657: Update to released granite.auth.ims bundle 1.4.42.
* ASSETS-31673: Update to cq-dam-processor-nui 1.1.810 for ASSETS-31673.
* ASSETS-31715: Update to cq-dam-processor-nui 1.1.816. Issue fixed: ASSETS-31715.
* ASSETS-31817: Updating to latest R-API and Bundle Injection Adapters.
* ASSETS-31945: [VULN-26683] Cloud Services XSS - /libs/dam/gui/components/admin/processingprofiles/clientlibs/processingprofiles/editprofile.js.
* ASSETS-31981: update granite async version.
* ASSETS-32108: fix regressions in Assets View Settings.
* ASSETS-32230: Update RAPI bundle to 366.
* ASSETS-32311: Asset Delivery opt-in for VIP program.
* ASSETS-32382: ASSETS-32455, ASSETS-32382: Changes in connected assets artifacts to remove non test usage of Guava 15.
* ASSETS-32455: ASSETS-32382: Changes in connected assets artifacts to remove non test usage of Guava 15.
* ASSETS-32544: additional logging for metadata export.
* ASSETS-32679: Add cache-killer to rendition URLs when previewing content.
* ASSETS-32754: [Collab API] Tasks cannot be assigned to users who have not logged in previously in GenStudio and AEMCS.
* ASSETS-32755: configure ordered queue for asset move events.
* ASSETS-32782: Update to cq-dam-repository-insights-agent 1.0.10. Issue fixed: ASSETS-32782.
* ASSETS-32879: Update to cq-dam-api 6.1.172, cq-dam-core 5.15.74, cq-dam-processor-nui 1.1.818. Issue fixed: ASSETS-32879.
* ASSETS-32899: collection search optimisations.
* ASSETS-32902: Adding a hydration endpoint.
* ASSETS-33003: ASSETS-33003 - [QSBRM] Automated Release.
* ASSETS-33098: update foundation to fix behaviour of tags in omnisearch.
* ASSETS-33246: Roll out damAssetLucene-10.
* ASSETS-33296: Update to cq-dam-content 2.6.1606. Issues fixed: ASSETS-34088, ASSETS-33300, ASSETS-33296, ASSETS-31274, ASSETS-26489.
* ASSETS-33299: VULN-26916 Update unified-shell-integration-content to v 1.0.96.
* ASSETS-33300: Update to cq-dam-content 2.6.1606. Issues fixed: ASSETS-34088, ASSETS-33300, ASSETS-33296, ASSETS-31274, ASSETS-26489.
* ASSETS-33454: more robust handling of approval audit events.
* ASSETS-34088: Update to cq-dam-content 2.6.1606. Issues fixed: ASSETS-34088, ASSETS-33300, ASSETS-33296, ASSETS-31274, ASSETS-26489.
* CQ-4354181: html injection in move and mergetag * CQ-4354181 html injection in move and mergetag.
* CQ-4355555: latest AEM and Granite translations.
* DXML-13276: include com.adobe.granite.repository:1.8.108 for DXML index.
* FORMS-11755: SKYOPS-66622,FORMS-11755,FORMS-12151,SKYOPS-69977 - Update to FACT tool version 0.5.180.
* FORMS-12151: SKYOPS-66622,FORMS-11755,FORMS-12151,SKYOPS-69977 - Update to FACT tool version 0.5.180.
* GRANITE-36205: Update internal oak release version to latest.
* GRANITE-45379: override oak.fastQuerySize property for system principals * GRANITE-45379 keep oak.version in sync.
* GRANITE-48110: upgrade quickstart-maven-plugin.
* GRANITE-48143: 
* GRANITE-48199: remove com.adobe.granite.toggle.impl.dev from ethos feature.
* GRANITE-48813: GRANITE-48830 GRANITE-48834 GRANITE-48813 upgrade .auth.ims .auth.oauth.
* GRANITE-48830: GRANITE-48834 GRANITE-48813 upgrade .auth.ims .auth.oauth * GRANITE-48830 AEM to IMS integration in stage has become too unstable - update to granite.auth.ims bundle version 1.4.50 which has the max ttl fix in it * GRANITE-48830 AEM to IMS integration in stage has become too unstable - update to granite.auth.ims bundle version 1.4.52 which has the max ttl fix in it.
* GRANITE-48834: GRANITE-48830 GRANITE-48834 GRANITE-48813 upgrade .auth.ims .auth.oauth.
* GRANITE-49031: Regression resulting in `@JsonIgnore` annotation being ignored on transient fields.
* GRANITE-50157: safer redirects to inbox task URLs.
* SCRNS-3961: Jquery animation used in Fade transition leads to black screen.
* SITES-15030: SITES-16121, SITES-16207, SITES-15868, SITES-16118, SITES-16079.
* SITES-15868: SITES-15030 SITES-16121, SITES-16207, SITES-15868, SITES-16118, SITES-16079.
* SITES-16079: SITES-15030 SITES-16121, SITES-16207, SITES-15868, SITES-16118, SITES-16079.
* SITES-16118: SITES-15030 SITES-16121, SITES-16207, SITES-15868, SITES-16118, SITES-16079.
* SITES-16121: SITES-15030 SITES-16121, SITES-16207, SITES-15868, SITES-16118, SITES-16079.
* SITES-16207: SITES-15030 SITES-16121, SITES-16207, SITES-15868, SITES-16118, SITES-16079.
* SITES-17361: Re-embed Jsoup in the sites-headless bundle.
* SITES-17768: GraphQL to output Dynamic Media URL for assets referenced in Content Fragments.
* SITES-18021: update cq-content-sync to 5.14.2.
* SKYOPS-66622: FORMS-11755,FORMS-12151,SKYOPS-69977 - Update to FACT tool version 0.5.180.
* SKYOPS-68495: dispatcher image version 2.0.199 (#530).
* SKYOPS-69977: SKYOPS-66622,FORMS-11755,FORMS-12151,SKYOPS-69977 - Update to FACT tool version 0.5.180.


### Known Issues {#known-issues-14945}

None.

### Change Notice {#change-notice-14945}

**Action Required**

Upcoming changes will require the library [aem-cloud-testing-clients](https://github.com/adobe/aem-testing-clients) used in your custom functional tests to be updated to at least version **1.2.1**

Make sure that your dependency in `it.tests/pom.xml` has been updated.

```xml
<dependency>
   <groupId>com.adobe.cq</groupId>
   <artifactId>aem-cloud-testing-clients</artifactId>
   <version>1.2.1</version>
</dependency>
```

This change will be required after March 21, 2024.

Failing to update the dependency library will result in pipeline failures at the "Custom Functional Testing" step.

### Embedded Technologies {#embedded-tech-14813}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.60-T20240131102219-0cde853|[Oak API 1.60.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.60.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
