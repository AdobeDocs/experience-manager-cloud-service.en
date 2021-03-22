---
title: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2020.11.0
description: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2020.11.0
feature: Release Information
---

# Release Notes for Cloud Manager in Adobe Experience Manager as a Cloud Service 2020.11.0 {#release-notes}

This page outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2020.11.0.

## Release Date {#release-date}

The Release Date for Cloud Manager in AEM as a Cloud Service 2020.11.0 is November 12, 2020.

## Cloud Manager {#cloud-manager}

### What's New {#what-is-new}

* A new menu option **Local Login** is now be available to users from the environment menu options on the Environment card and Environments Summary pages. 
   Refer to [Managing Environments](/help/implementing/cloud-manager/manage-environments.md#login-locally) for more details.

* The **Learn** tab in Cloud Manager has been refreshed with new images in the UI.

### Bug Fixes {#bug-fixes-cloud-manager}

* The loading of dependencies done prior to build execution required downloading a Maven plugin.
* The link from the Cloud Manager footer to select a language will now navigate to the correct location.
* Sometimes during the code scanning, the SonarQube process would not start. This will now be auto-detected and a restart attempted.
* All existing production pipelines will be automatically enabled with the Experience Audit step. 
