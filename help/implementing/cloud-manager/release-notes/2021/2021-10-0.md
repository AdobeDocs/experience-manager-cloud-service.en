---
title: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2021.10.0
description: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2021.10.0
feature: Release Information
exl-id: f8a87b00-52ce-42a6-a955-45cb14703b40
---
# Release Notes for Cloud Manager in Adobe Experience Manager as a Cloud Service 2021.10.0 {#release-notes}

This page outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.10.0.

>[!NOTE]
>To see the current Release Notes for Adobe Experience Manager as a Cloud Service, click [here](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/release-notes/release-notes/release-notes-current.html).

## Release Date {#release-date}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.10.0 is October 14, 2021.


### What's New {#what-is-new}

* In preparation for some upcoming changes, existing deployment pipelines will now be referenced and labelled in the user interface as **Full Stack** pipelines.

* Pipeline card has been refreshed to now display a single, integrated face that shows both production and non-production pipelines, and user can select Run/Pause/Resume directly from the action menu associated with each pipeline.

* A user in Deployment Manager role can now delete Production pipeline in a self-service manner via the UI.

* Add and edit pipeline experiences have been refreshed to now use familiar, modern modals.

* Users of Cloud Manager can now submit feedback directly from the user interface via the **Feedback** button on top right of the landing page.

* Yearly SLA Graphs can now be downloaded from the Cloud Manager's user interface. 

* Code quality and non-production pipeline executions will now use a more efficient shallow cloning process during the build step, leading to a faster build time for customers with especially large git repositories. 

* Add IP Allow List wizard will now inform the user if maximum allowed number of IP Allow Lists has been reached. 

* The Cloud Manager API documentation now includes an interactive playground that allows logged-in users to experiment with the API from their browser. See [Cloud Manager API Playground](https://www.adobe.io/experience-cloud/cloud-manager/reference/playground/) for more details.

* The tool tip on the Program card will be more descriptive if a selection option under 'Navigate To' is disabled. It now displays "A production environment does not exist." 

### Bug Fixes {#bug-fixes}

* In rare situations, when an Adobe staff would restore a customer's environment, the restore was considered complete before the environment was fully operational.

* Certain internal requests made during environment creation were not being retried.

* If deployment failed error occurs following domain name verification, the error message has been corrected to request the customer to contact their Adobe representative.
