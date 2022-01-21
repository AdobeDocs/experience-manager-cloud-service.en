---
title: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2020.6.0
description: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2020.6.0
feature: Release Information
exl-id: 879a5025-f94f-4549-bf6e-e1cc6b6a7b58
---
# Release Notes for Cloud Manager in Adobe Experience Manager as a Cloud Service 2020.6.0 {#release-notes}

This page outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2020.6.0.

## Release Date {#release-date}

The Release Date for Cloud Manager in AEM as a Cloud Service 2020.6.0 is June 04, 2020.

## What's New {#whats-new-cloud-manager}

* A user in the *Business Owner* role in Cloud Manager is now able to delete a Sandbox Program from the landing page (via quick action button on Program card) or from within the program.

  Refer to [Deleting a Sandbox Program](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/getting-access/cloud-service-programs/creating-a-program.html) for more details.

* A Sandbox Program user in *Business Owner* or *Deployment Manager* role in Cloud Manager is now able to delete their Production and Stage environment set via the Cloud Manager UI. The delete option is now available from both the Environment card on the **Programs Overview** page as well as the **Environments** page. Selecting the delete option on either Production or Stage also deletes the other in the set.

  Refer to [Deleting a Sandbox Program](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/getting-access/cloud-service-programs/creating-a-program.html) for more details.

* Coach marks on the landing page to inform and instruct the user about basic navigation.

* Coach marks on the **Program Overview** page to inform and instruct the user about basic navigation inside Cloud Manager to get them started.

* A **LEARN** page is now available in Cloud Manager, accessible via the top navigation. This page includes resources to help users learn about the most frequently used work-flows as relevant to their roles assigned in Cloud Manager.

* Sandbox Programs are now identified by means of a **Sandbox** badge that will be displayed on the program card on the landing page as well as next to the program name in the **Program Overview** page.

* A user in the SysAdmin role now has one-click access to the location in Admin Console from where user roles or permissions to Cloud Manager can be managed. A **Manage Access** button is now available on the landing page next to the **Add Program** button.
  
  Refer to [SysAdmin Tasks](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/getting-access/navigation.html#sysadmin-tasks) for more details.

* A user in the SysAdmin role now has one-click access to author instance directly from Cloud Manager. 

  Refer to [Managing Access to Author Instance](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/getting-access/navigation.html#manage-access-aem) for more details.

* The Build log now includes the list of discovered artifacts, including skipped content packages.

* The Build step now validates that all of the generated content packages include all mandatory properties – name, group and version.

* The Build step now validates that the build produced at least one content package.

### Bug Fixes {#bug-fixes-cm}

* In certain situations, the icons in the **Create Program** dialog were misaligned.

* The AEM release identifier was not consistently displayed on the **Programs Overview** page.

* When configuring the production pipeline, the **Scheduled Deployment** option was not visible for some customers.

### Known Issues {#known-issues-cm}

* Environments within a Sandbox program will be hibernated when no activity is detected for a certain duration. This status will not be observed in Cloud Manager. The status can however be observed via Developer Console. This will be addressed in an upcoming release.

* The link to the Developer Console directly from Cloud Manager will not display the option to de-hibernate/hibernate a Sandbox Program's environment. To address this, once at the Developer Console, add the pattern `#release-cm-p1234-e5678` to the end of the url, where *1234* is the Program ID and *5678* is the Environment ID. This will be addressed in an upcoming release.
