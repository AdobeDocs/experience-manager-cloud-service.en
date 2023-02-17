---
title: Release Notes for Cloud Manager 2022.4.0 in Adobe Experience Manager as a Cloud Service
description: These are the release notes for Cloud Manager 2022.4.0 in AEM as a Cloud Service.
feature: Release Information
exl-id: e7ff623b-aeca-40a6-bf48-98af270a4117
---
# Release Notes for Cloud Manager 2022.4.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager 2022.4.0 in AEM as a Cloud Service.

>[!NOTE]
>
>Refer to [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager release 2022.4.0 in AEM as a Cloud Service is April 7, 2022. The next release is planned for May 5, 2022.

## What's New {#what-is-new}

* Improvements to the duration and success rate of pipeline build steps have been implemented and will be incrementally rolled out to all customers through the month of April.
* You can now easily find a git branch by typing the first few characters of the name in the input field in the add and edit pipeline wizard and selecting from suggested matches for both [production](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md) and [non-production](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md) pipelines.
* Shortly after the April release, India will become available for selection when defining the cloud region during environment creation.
* The **Pipelines** page now has pagination to improve usability for programs with a large number of pipelines.
  * 50 rows per page will be displayed in the table.
* The version of the [AEM Project Archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/overview.html) used by Cloud Manager has been updated to version 36.
* Oracle JDK is now the default JDK for the development and operation of AEM applications. The Cloud Manager build process will automatically switch to using Oracle JDK, even if an alternative option is explicitly selected in the Maven toolchain.
  * To learn more about how to switch to Oracle JDK, please refer to [the Build Environment documentation.](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md#using-java-support)
  * Please refer to [the Java support policy for Adobe Experience Manager FAQ](https://experienceleague.adobe.com/docs/experience-manager-65/assets/Java_Policy_for_Adobe_Experience_Manager.pdf) to address common questions about this change.
* Pipeline execution will now fail faster by detecting older AEM versions during the validation step. Users will be presented with a message in the UI to guide them.

## Bug Fixes {#bug-fixes}

* The log created in the UI Test step is now available for download via the UI.
* Web tier config pipelines can now only reuse packages from web tier config executions.
* Greater clarity was added to the messages in the UI about how to update AEM on an outdated environment.
