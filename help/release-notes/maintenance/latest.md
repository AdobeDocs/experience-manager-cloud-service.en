---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 14813 {#release-14813}

Summarized below are the continuous improvements for maintenance release 14813, which was publicly released on January 11, 2023. The previous maintenance release was release 14697.

2024.1.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-14813}

* ASSETS-32101: Metadata for smart crop renditions should be updated in DB.
* ASSETS-31297: Improve checks to prevent deletion of copied assets from dynamic media.

### Fixed Issues {#fixed-issues-14813}

* ASSETS-15977: Remove v1 search events * ASSETS-15977 Remove v1 events * ASSETS-15977 Remove pipeline producer.
* ASSETS-18088: batik library security updates.
* ASSETS-21965: Metadata writeback workflow must only launch on asset metadata changes.
* ASSETS-23489: create repository-insights-agent as directCountsPrincipal.
* ASSETS-23815: add subject detection support.
* ASSETS-24739: Disable Frame.io Custom Action Endpoint on Publish.
* ASSETS-26368: Update to cq-dam-processor-nui 1.1.814 for ASSETS-26368.
* ASSETS-26413: XSS in collectionsettings.js * ASSETS-26413 - content model updates.
* ASSETS-26430: XSS in collection.js * ASSETS-26430 - content model exclusions.
* ASSETS-26431: XSS in columnpreview.js * ASSETS-26431 - content model updates.
* ASSETS-26489: Update to cq-dam-content 2.6.1606. Issues fixed: ASSETS-34088, ASSETS-33300, ASSETS-33296, ASSETS-31274, ASSETS-26489.
* ASSETS-26492: XSS in childasset.jsp * ASSETS-28963 [VULN-25903] & ASSETS-26492 SECURITY * Upgrading cq-dam-content version to fix ASSETS-28963 [VULN-25903] & ASSETS-26492.
* ASSETS-26549: Assets / Nodes with "jcr:lastModifiedBy": "workflow-process-service" show as "external user" in list view.
* ASSETS-26842: Update to cq-dam-content 2.6.1572. Issue fixed: ASSETS-26842.
* ASSETS-27066: Update to cq-dam-content 2.6.1556, cq-dam-download 1.0.132. Issues fixed: ASSETS-27066, ASSETS-31280.
* ASSETS-27290: ASSETS-29453 update cq-dam-content version.
* ASSETS-27529: [VULN-25622] Stored XSS in /libs/dam/gui/coral/components/commons/assetselector/test/clientlibs/test/js/demo.js * ASSETS-27529 and ASSETS-31324 updated XSS securities in DAM content.
* ASSETS-28284: ASSETS-29037.
* ASSETS-28708: ASSETS-31657 Support new Content Hub service code in granite.auth.ims bundle ASSETS-28708 Instrument exchangeTokenByIMSOrg with trace level timings Update to released granite.auth.ims bundle 1.4.42.
* ASSETS-28767: Updated cq-dam-mac-sync version.
* ASSETS-28894: XSS in reportlist.js * ASSETS-28894 - update granite.ui.content to 0.8.1376.
* ASSETS-28963: [VULN-25903] & ASSETS-26492 SECURITY * Upgrading cq-dam-content version to fix ASSETS-28963 [VULN-25903] & ASSETS-26492.
* ASSETS-29011: Smart crop visible for read only users.
* ASSETS-29037: ASSETS-28284 ASSETS-29037 * ASSETS-29037 isolate /var/dam/subjects cq:tags permission * ASSETS-29037 remove rep:write for content-authors on /var/dam/subjects/persons * ASSETS-29037 remove jcr:read for contributor on /var/dam/subjects/persons * ASSETS-29037 restore group perms on /var/dam/subjects * ASSETS-29037 upgrade it/platform serverside-security test-module to 6.6.136.
* ASSETS-29141: Update to cq-dam-api 6.1.170, cq-dam-core 5.15.68, cq-dam-processor-nui 1.1.808, cq-dam-processor-api 1.1.86, cq-dam-eventing 1.0.36. Issue fixed: ASSETS-29141.
* ASSETS-29348: Update to cq-dam-core 5.15.64, cq-dam-processor-dm 1.0.54. Issues fixed: ASSETS-31256, ASSETS-29348.
* ASSETS-29453: ASSETS-27290 ASSETS-29453 update cq-dam-content version.
* ASSETS-29454: [VULN-26006] Update cq-dam-content version SECURITY * ASSETS-29454 Updated sidecar version.
* ASSETS-29738: Updating commons.mime for more up to date mime-type support.
* ASSETS-30068: New status COMPLETED_WITH_ERROR for bulk import AE.
* ASSETS-30171: Updated dam-eventing version for ASSETS-30171.
* ASSETS-30261: Update to cq-dam-eventing 1.0.32. Issue fixed: ASSETS-30261.
* ASSETS-30354: XSS in publishwizard wizard.js.
* ASSETS-30405: XSS [VULN-26170].
* ASSETS-30406: vulnerability fix for video preset editor.
* ASSETS-30410: Update sidecar version.
* ASSETS-30538: Updated dam-core version 5.15.72 for ASSETS-30538.
* ASSETS-30591: add ide-support-open-any-class profile.
* ASSETS-30626: Updated asset-delivery bundle version.
* ASSETS-30756: asset move fails when folder name ends in 'html'.
* ASSETS-30810: Sanitize tags before rendering legacy youtube config.
* ASSETS-30987: Update eventing bundle for ASSETS-30987.
* ASSETS-31015: 
* ASSETS-31038: Add user mapping for eventrecorderhelper.
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
* SCRNS-3961: 
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


### Known Issues {#known-issues-14813}

None.

### Change Notice {#change-notice-14813}

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
