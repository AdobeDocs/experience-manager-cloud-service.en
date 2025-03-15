---
title: Release Notes for Cloud Manager 2025.3.0 in Adobe Experience Manager as a Cloud Service
description: Learn about the release of Cloud Manager 2025.3.0 in AEM as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 24d9fc6f-462d-417b-a728-c18157b23bbe
---
# Release notes for Cloud Manager 2025.3.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

<!-- https://wiki.corp.adobe.com/display/DMSArchitecture/Cloud+Manager+2025.03.0+Release -->

Learn about the release of Cloud Manager 2025.3.0 in AEM (Adobe Experience Manager) as a Cloud Service.


See also the [current release notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md).

## Release dates {#release-date}

The release date for Cloud Manager 2025.3.0 in AEM as a Cloud Service is Thursday, March 13, 2025. 

The next planned release is Thursday, April 10, 2025.
 
## What's new {#what-is-new}

* **Run multiple pipelines**

    The ability to run multiple pipelines simultaneously has been introduced on the Pipelines page. Users must select at least one pipeline but no more than ten. Near the upper-right corner on the Pipelines page, click **Run selected (x)**. A modal dialog box appears that lists any pipelines that cannot be started. Click **Run** to initiate all valid pipelines.

    ![Run selected pipelines dialog box](/help/implementing/cloud-manager/release-notes/assets/run-selected-pipelines.png)

* **Support extended to Node.js versions**

    The front-end build environment now supports the following `Node.js` versions:

    * 23
    * 22
    * 20

    See also [Develop Sites with the Front-End Pipeline](/help/implementing/developing/introduction/developing-with-front-end-pipelines.md#node-versions). <!-- CMGR-65307 -->

<!--
## Early adoption program {#early-adoption}

Be a part of Cloud Manager's early adoption program and have a chance to test upcoming features. -->


## Bug fixes

* **(UI) Fix for 'Advanced Network Configuration' updates in Cloud Manager**  

    A rare issue that prevented updates to the **Advanced Network Configuration** when an "Update available" notification was present has been resolved. Previously, Cloud Manager locked configuration modifications, including advanced networking settings, to prevent conflicts during an update. Customers can now manually trigger the pending update to apply the necessary changes without restrictions. <!-- CMGR-65913 and CMGR-65788 -->

* **(UI) Fix for IP allow list updates stuck in "Updating" state**  

    A rare issue where IP allow list updates in Cloud Manager remained stuck in the "Updating" state due to duplicate active domain configuration for an environment has been resolved. Previously, customers experienced indefinite processing delays when updating IP allow lists, preventing necessary network access adjustments. This fix ensures that IP allow list updates can now complete successfully without getting stuck. <!-- CMGR-65786 -->




<!-- ## Known issues {#known-issues} -->
