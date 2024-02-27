---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
---
# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 15262 {#release-15262}

Summarized below are the continuous improvements for maintenance release 15262, which was publicly released on February 28, 2024. The previous maintenance release was release 14697.

2024.3.0 Feature Activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) for more information.

### Enhancements {#enhancements-15262}

* ASSETS-32101: Metadata for smart crop renditions should be updated in DB.
* ASSETS-31297: Improve checks to prevent deletion of copied assets from dynamic media.

### Fixed Issues {#fixed-issues-15262}

* ASSETS-15977: Remove deprecated v1 search events and pipeline producer.
* ASSETS-18088: Upgrade batik library dependencies to 1.17.
* ASSETS-21965: Metadata writeback workflow must only launch on asset metadata changes.
<!-- * ASSETS-23489: create repository-insights-agent as directCountsPrincipal. -->
<!-- * ASSETS-23815: add subject detection support. -->
<!-- * ASSETS-24739: Disable Frame.io Custom Action Endpoint on Publish. -->
* ASSETS-26368: Scheduled Bulk Import Jobs Not Removed if Job Config does not Exist.
<!-- * ASSETS-26413: XSS in collectionsettings.js * ASSETS-26413 - content model updates. -->
<!-- * ASSETS-26430: XSS in collection.js * ASSETS-26430 - content model exclusions. -->
<!-- * ASSETS-26431: XSS in columnpreview.js * ASSETS-26431 - content model updates. -->
<!-- * ASSETS-26489: Update to cq-dam-content 2.6.1606. Issues fixed: ASSETS-34088, ASSETS-33300, ASSETS-33296, ASSETS-31274, ASSETS-26489. -->
<!-- * ASSETS-26492: XSS in childasset.jsp * ASSETS-28963 [VULN-25903] & ASSETS-26492 SECURITY * Upgrading cq-dam-content version to fix ASSETS-28963 [VULN-25903] & ASSETS-26492. -->
<!-- * ASSETS-26541: Fix XSS issue in assetdetails.js. -->
* ASSETS-26549: Assets / Nodes with "jcr:lastModifiedBy": "workflow-process-service" show as "external user" in list view.
* ASSETS-26842: Update "Firefly" text to read "App Builder" in Processing Profile.
<!-- * ASSETS-27066: Update to cq-dam-content 2.6.1556, cq-dam-download 1.0.132. Issues fixed: ASSETS-27066, ASSETS-31280. -->
<!-- * ASSETS-27290: ASSETS-29453 update cq-dam-content version. -->
<!-- * ASSETS-27346: update com.adobe.granite.ui.content:zip:0.8.1398 * ASSETS-27346 updated artifacts from SITES-14801 due to required dependency versions * Update to cq-dam-content 2.6.1624. Issues fixed: ASSETS-27346, ASSETS-34571. -->
<!-- * ASSETS-27529: [VULN-25622] Stored XSS in /libs/dam/gui/coral/components/commons/assetselector/test/clientlibs/test/js/demo.js * ASSETS-27529 and ASSETS-31324 updated XSS securities in DAM content. -->
<!-- * ASSETS-28284: ASSETS-29037. -->
* ASSETS-28708: Very slow response for some IMS token requests.
* ASSETS-28767: Inconsistent publish state on assets if folder containing large no. of assets published.
<!-- * ASSETS-28894: XSS in reportlist.js * ASSETS-28894 - update granite.ui.content to 0.8.1376. -->
<!-- * ASSETS-28963: [VULN-25903] & ASSETS-26492 SECURITY * Upgrading cq-dam-content version to fix ASSETS-28963 [VULN-25903] & ASSETS-26492. -->
* ASSETS-29011: Smart crop is visible for read-only users.
<!-- * ASSETS-29037: ASSETS-28284 ASSETS-29037 * ASSETS-29037 isolate /var/dam/subjects cq:tags permission * ASSETS-29037 remove rep:write for content-authors on /var/dam/subjects/persons * ASSETS-29037 remove jcr:read for contributor on /var/dam/subjects/persons * ASSETS-29037 restore group perms on /var/dam/subjects * ASSETS-29037 upgrade it/platform serverside-security test-module to 6.6.136. -->
<!-- * ASSETS-29141: Update to cq-dam-api 6.1.170, cq-dam-core 5.15.68, cq-dam-processor-nui 1.1.808, cq-dam-processor-api 1.1.86, cq-dam-eventing 1.0.36. Issue fixed: ASSETS-29141. -->
* ASSETS-29348: AssetMoveEventHandler can consume too much memory.
<!-- * ASSETS-29453: ASSETS-27290 ASSETS-29453 update cq-dam-content version. -->
<!-- * ASSETS-29454: [VULN-26006] Update cq-dam-content version SECURITY * ASSETS-29454 Updated sidecar version. -->
* ASSETS-29738: Asset Upload Restriction fails with NullPointerException for woff files.
* ASSETS-30068: Bulk Import Asset Essentials to include status COMPLETED_WITH_ERROR for "job completed, but with error".
<!-- * ASSETS-30171: Updated dam-eventing version for ASSETS-30171. -->
* ASSETS-30261: Incorrect imsUserId sent to Pipeline for asset events.
<!-- * ASSETS-30354: XSS in publishwizard wizard.js. -->
<!-- * ASSETS-30405: XSS [VULN-26170]. -->
<!-- * ASSETS-30406: vulnerability fix for video preset editor. -->
<!-- * ASSETS-30410: Update sidecar version. -->
* ASSETS-30538: View Page option is Missing after Moving a PDF file.
<!-- * ASSETS-30591: add ide-support-open-any-class profile. -->
* ASSETS-30626: Failure to create delivery request reported for assets with empty assetId.
* ASSETS-30632: Added a separate Brand Portal publish status column in list view. Enhancement.
* ASSETS-30756: Move Asset Wizard action fails when folder name ends in 'html'.
* ASSETS-30810: Sanitize tags before rendering legacy youtube config.
* ASSETS-30934: Added support for `Iptc4xmpCore:AltTextAccessibility` and `Iptc4xmpCore:ExtDescrAccessibility` properties to Asset Metadata Editor. Enhancement.
<!-- * ASSETS-30987: Update eventing bundle for ASSETS-30987. -->
* ASSETS-31015: Unable to upload Assets with .msg filename extension.
* ASSETS-31038: Tasks events that are received by the notification service are not being processed.
* ASSETS-31097: Disable Async Copy for WCM Content to avoid traversal query warnings.
* ASSETS-31256: Assets / Nodes with "jcr:lastModifiedBy": "workflow-process-service" show as "external user" in list view.
* ASSETS-31260: Asset Metadata Form Dropdown field is not working correctly when the dropdown JSON has a big list.
<!-- * ASSETS-31274: Update to cq-dam-content 2.6.1606. Issues fixed: ASSETS-34088, ASSETS-33300, ASSETS-33296, ASSETS-31274, ASSETS-26489. -->
* ASSETS-31280: Make assets download in a flattened structure when added to a collection.
* ASSETS-31297: Prevent delete of copied asset from dynamic media.
* ASSETS-31301: `dynamicmedia_sly.js` cannot be correctly instantiated by the Use API.
<!-- * ASSETS-31324: ASSETS-27529 and ASSETS-31324 updated XSS securities in DAM content. -->
* ASSETS-31330: ko_KR: Unlocalized strings in Subtitles and Audio tracks.
* ASSETS-31405: InDesign server processing fails for large InDesign layouts.
* ASSETS-31570: Unified Shell - asset details "Save & Close", "Cancel" buttons need to be pressed more than once to work.
<!-- * ASSETS-31657: Support new Content Hub service code in granite.auth.ims bundle ASSETS-28708 Instrument exchangeTokenByIMSOrg with trace level timings Update to released granite.auth.ims bundle 1.4.42. -->
* ASSETS-31673: Bulk import failed for large Dropbox files.
<!-- * ASSETS-31715: Allow multiple cloud service integrations in AEM to work with multiple custom actions in Frame.io. -->
<!-- * ASSETS-31817: AEM-CS Work Required for Content Hub MVP. -->
<!-- * ASSETS-31945: [VULN-26683] Cloud Services XSS - /libs/dam/gui/components/admin/processingprofiles/clientlibs/processingprofiles/editprofile.js. -->
<!-- * ASSETS-31981: update granite async version dependency for Async job to batch commits for Asset delete operations when deleting large asset folders. -->
<!-- * ASSETS-31997: Updated addressbook version. -->
<!-- * ASSETS-32101: Metadata for smart crop renditions should be updated in DB. -->
<!-- * ASSETS-32105: cq-scene7-imaging: remove non-test usage of Guava 15 * ASSETS-32105 : updating guava dependency * ASSETS-32105 : updating guava dependency. -->
* ASSETS-32108: AEM Assets Not Saving User-Defined Card Size in View Settings.
<!-- * ASSETS-32147: Fix for ASSETS-30632 and ASSETS-32147: BP separate publish view and Guava removal. -->
* ASSETS-32230: Upgrade minimum runtime version of com.adobe.aem.repoapi bundle.
<!-- * ASSETS-32311: Asset Delivery opt-in for VIP program. -->
* ASSETS-32321: Post-Processing workflow and ImageProfile resolution fails if ancestor folder is missing 'jcr:content' subnode.
<!-- * ASSETS-32382: ASSETS-32455, ASSETS-32382: Changes in connected assets artifacts to remove non test usage of Guava 15. -->
<!-- * ASSETS-32455: ASSETS-32382: Changes in connected assets artifacts to remove non test usage of Guava 15. -->
<!-- * ASSETS-32509: Allowing the Content Hub Client ID. -->
* ASSETS-32544: Metadata export job fails intermittently.
* ASSETS-32679: Caching issues with asset (PDF) previews.
* ASSETS-32754: Tasks cannot be assigned to users who have not logged in previously.
* ASSETS-32755: Configure com/adobe/cq/dam/assetmove job topic to use an ordered queue.
<!-- * ASSETS-32782: Update to cq-dam-repository-insights-agent 1.0.10. Issue fixed: ASSETS-32782. -->
<!-- * ASSETS-32879: Update to cq-dam-api 6.1.172, cq-dam-core 5.15.74, cq-dam-processor-nui 1.1.818. Issue fixed: ASSETS-32879. -->
<!-- * ASSETS-32897: Update to cq-dam-content 2.6.1628, cq-dam-core 5.15.84. Issues fixed: ASSETS-32897, ASSETS-33538. -->
<!-- * ASSETS-32898:  -->
* ASSETS-32899: Searching inside Collections is extremely slow.
<!-- * ASSETS-32902: Adding a hydration endpoint. -->
<!-- * ASSETS-32989: Remove guava from similaritysearch bundle. -->
<!-- * ASSETS-32990: [VULN] Update stock integration package to remove security vulnerable Guava library * ASSETS-32990: Remove Guava from DAM Commons - SECURITY. -->
* ASSETS-33098: AEM Assets search facets "Tags predicate" does not work as expected.
<!-- * ASSETS-33193: ASSETS-33194 Updated cq-dam-content version. -->
<!-- * ASSETS-33194: ASSETS-33193 ASSETS-33194 Updated cq-dam-content version. -->
<!-- * ASSETS-33228: [VULN-26878] AMS XSS - /libs/dam/gui/coral/components/admin/folderschemaforms/formbuilder/v2/clientlibs/js/formdetails.js. -->
* ASSETS-33246: Release damAssetLucene-10. Enhancement.
<!-- * ASSETS-33296: Update to cq-dam-content 2.6.1606. Issues fixed: ASSETS-34088, ASSETS-33300, ASSETS-33296, ASSETS-31274, ASSETS-26489. -->
<!-- * ASSETS-33299: VULN-26916 Update unified-shell-integration-content to v 1.0.96. -->
<!-- * ASSETS-33300: Update to cq-dam-content 2.6.1606. Issues fixed: ASSETS-34088, ASSETS-33300, ASSETS-33296, ASSETS-31274, ASSETS-26489. -->
* ASSETS-33454: Review Task activity and comments not appearing in Timeline.
<!-- * ASSETS-33537: Add exclusion file for ASSETS-33537. -->
<!-- * ASSETS-33538: Update to cq-dam-content 2.6.1628, cq-dam-core 5.15.84. Issues fixed: ASSETS-32897, ASSETS-33538. -->
<!-- * ASSETS-33545: Fix XSS issues. -->
<!-- * ASSETS-33547: video profile vulnerability fix. -->
* ASSETS-33590: Add support for webm renditions for videos in processing profiles. Enhancement.
<!-- * ASSETS-33903: Custom Rendition serialization. -->
<!-- * ASSETS-33978: Add createdBy and modifiedBy to polaris metadata. -->
<!-- * ASSETS-34013: XSS in folder metadata schema handling SECURITY * ASSETS-34013: update content package in provisioning sidecar * ASSETS-34013: add cm exclusion. -->
* ASSETS-34088: PDF preview is not working on AEM Assets.
* ASSETS-34155: Dynamic Media - Updated AEM Viewers / 2024.1.0. 
<!-- * ASSETS-34571: Update to cq-dam-content 2.6.1624. Issues fixed: ASSETS-27346, ASSETS-34571. -->
* ASSETS-34684: Handle multivalue dc:title in content tree.
* ASSETS-34789: Fix normalization issues in filename conflict check.
<!-- * ASSETS-34938: Add genstudio-ojas-1 to allowed client ids. -->
<!-- * CQ-4354181: html injection in move and mergetag * CQ-4354181 html injection in move and mergetag. -->
<!-- * CQ-4354884: update assets-skyline-it artifact and repository * CQ-4354884: update test modules (#558) * CQ-4354884: update test modules (#559). -->
<!-- * CQ-4355555: latest AEM and Granite translations. -->
* DXML-13276: AEM Guides - integrate indexes in GraniteContent and remove them from the library.
<!-- * FORMS-11755: SKYOPS-66622,FORMS-11755,FORMS-12151,SKYOPS-69977 - Update to FACT tool version 0.5.180. -->
<!-- * FORMS-12151: SKYOPS-66622,FORMS-11755,FORMS-12151,SKYOPS-69977 - Update to FACT tool version 0.5.180. -->
* GRANITE-36205: Update oak version to 1.60-T20240131102219-0cde853. Enhancement.
<!-- * GRANITE-45379: override oak.fastQuerySize property for system principals * GRANITE-45379 keep oak.version in sync. -->
* GRANITE-47995: Deletion operations can fail due to conflicts with "cq:isDelivered" property.
* GRANITE-48079: Enable POST requests for OAuth online token validation.
<!-- * GRANITE-48110: upgrade quickstart-maven-plugin. -->
* GRANITE-48143: upgrade org.apache.sling.resourcemerger to 1.4.4 
<!-- * GRANITE-48199: remove com.adobe.granite.toggle.impl.dev from ethos feature. -->
<!-- * GRANITE-48813: GRANITE-48830 GRANITE-48834 GRANITE-48813 upgrade .auth.ims .auth.oauth. -->
<!-- * GRANITE-48830: GRANITE-48834 GRANITE-48813 upgrade .auth.ims .auth.oauth * GRANITE-48830 AEM to IMS integration in stage has become too unstable - update to granite.auth.ims bundle version 1.4.50 which has the max ttl fix in it * GRANITE-48830 AEM to IMS integration in stage has become too unstable - update to granite.auth.ims bundle version 1.4.52 which has the max ttl fix in it. -->
<!-- * GRANITE-48834: GRANITE-48830 GRANITE-48834 GRANITE-48813 upgrade .auth.ims .auth.oauth. -->
* GRANITE-49031: Update to Jackson 2.16.1.
<!-- * GRANITE-50157: safer redirects to inbox task URLs. -->
* SCRNS-3961: Screens - Sequence channel: Jquery animation used in Fade transition leads to black screen.
<!-- * SITES-14801: ASSETS-27346 updated artifacts from SITES-14801 due to required dependency versions. -->
<!-- * SITES-15030: SITES-16121, SITES-16207, SITES-15868, SITES-16118, SITES-16079. -->
* SITES-15868: Improve the performance for listing fragments.
* SITES-16079: `/fragments/{id}/references` started to return duplicates.
* SITES-16118: If a fragment is patched and a fragment field is missing from the model, an exception is thrown.
* SITES-16121: Retrieval of a model date field throws exception.
* SITES-16207: The POST /adobe/sites/cf/models operation returns two different OK status codes.
* SITES-17361: Re-embed Jsoup in the sites-headless bundle.
* SITES-17768: GraphQL to output Dynamic Media URL for assets referenced in Content Fragments.
<!-- * SITES-18021: Update cq-content-sync to 5.14.2. -->
* SITES-19326: Update links in Assets UI to open CF in new CF Editor. Enhancement.
* SKYOPS-66622: Author deployment crash looping after running a buildTransform enabled pipeline.
<!-- * SKYOPS-68495: dispatcher image version 2.0.199 (#530). -->
* SKYOPS-69977: Adaptive Image Servlet does not load image after latest update.
<!-- * VULN-25622: ASSETS-27529 [VULN-25622] Stored XSS in /libs/dam/gui/coral/components/commons/assetselector/test/clientlibs/test/js/demo.js. -->
<!-- * VULN-25903: ASSETS-28963 [VULN-25903] & ASSETS-26492 SECURITY * Upgrading cq-dam-content version to fix ASSETS-28963 [VULN-25903] & ASSETS-26492. -->
<!-- * VULN-26006: ASSETS-29454: [VULN-26006] Update cq-dam-content version SECURITY. -->
<!-- * VULN-26170: ASSETS-30405: XSS [VULN-26170]. -->
<!-- * VULN-26683: ASSETS-31945 [VULN-26683] Cloud Services XSS - /libs/dam/gui/components/admin/processingprofiles/clientlibs/processingprofiles/editprofile.js. -->
<!-- * VULN-26878: ASSETS-33228 [VULN-26878] AMS XSS - /libs/dam/gui/coral/components/admin/folderschemaforms/formbuilder/v2/clientlibs/js/formdetails.js. -->
<!-- * VULN-26916: ASSETS-33299 VULN-26916 Update unified-shell-integration-content to v 1.0.96. -->

### Known Issues {#known-issues-15262}

None.

### Change Notice {#change-notice-15262}

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

This change will be required after April 6, 2024.

Failing to update the dependency library will result in pipeline failures at the "Custom Functional Testing" step.

### Embedded Technologies {#embedded-tech-15262}

|Technology|Version|Link|
|---|---|---|
|AEM OAK |1.60-T20240131102219-0cde853|[Oak API 1.60.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.60.0/index.html)| 
|AEM SLING API |Version 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL|Version 1.4.20-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components|Version 2.23.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
