---
title: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2021.7.0
description: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2021.7.0
feature: Release Information
exl-id: 7ef738a5-4657-482d-848b-e95e4fb816f9
---
# Release Notes for Cloud Manager in Adobe Experience Manager as a Cloud Service 2021.7.0 {#release-notes}

This page outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.7.0.

>[!NOTE]
>To see the current Release Notes for Adobe Experience Manager as a Cloud Service, click [here](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/release-notes/release-notes/release-notes-current.html).

## Release Date {#release-date}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.7.0 is July 15, 2021.


### What's New {#what-is-new}

* Customers are now able to use Azul 8 and 11 JDKs for their Cloud Manager build processes and can either select to use one of these JDKs for toolchains-compatible Maven plugins *or* the entire Maven process execution.

* The outbound egress IP will now be logged in the build step log file. 

* Stage and Production environments running old versions of AEM will now report a status of **Update Available**. 

* The maximum SSL certificates supported has increased to 20 per program.

* The maximum number of domains that can be configured has increased to 500 per environment.

* The **Manage Git** buttons has been retitled to **Access Git Info** and the dialog has been visually refreshed.

* The version of the AEM Project Archetype used by Cloud Manager has been updated to version 28.

### Bug Fixes {#bug-fixes}

* In some situations, Preview was not an available option when binding an IP Allow List to an environment.

* Manually navigating to the execution details page for a non-existing execution did not show an error, just an endless loading screen.

* The error message shown when the maximum number of SSL certificates was reached was not helpful.

* In some circumstances, there could be a discrepancy in the release version shown in the pipeline card on the **Overview** page.

* Add program wizard incorrectly stated that name cannot be changed after creation. 

### Known Issues {#known-issues}

Customers switching to use the Azul JDKs should be aware that not all existing applications will compile without error on Azul JDK. It is highly recommended to test locally before switching.
