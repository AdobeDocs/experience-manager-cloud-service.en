---
title: Release Notes for Release 2020.3.0
description: Release Notes for Release 2020.3.0
---

# Release Notes for AEM as a Cloud Service 2020.3.0 {#release-notes}

The following section outlines the general Release Notes for Experience Manager as a Cloud Service 2020.3.0.

## Cloud Manager {#cloud-manager}

The Release Date for Cloud Manager Release 2020.3.0 is March 05, 2020.

Follow this section to learn about what is new and the updates for Cloud Manager Release 2020.3.0.

### What's New {#what-is-new}

* The log for the build step is now available while the build step is running.
* Some of the messages on the pipeline execution details page have been edited for clarity.

### Bug Fixes  {#bug-fixes}

* Log files for the custom and product functional test steps could not be downloaded through the UI.
* When the git repository for a Cloud Service program failed to be created, users in the Deployment Manager role sometimes were unable to recover from this failure.
* Certain user activities during the creation of a sandbox program could cause the program creation to fail before the non-production pipeline was created.
* The ephemeral SonarQube instance used in the build step was occasionally failing to start within the configured timeout.
* Concurrent creation of dev environments in the same Cloud Service program could encounter a condition where only one was able to be created successfully.
* Experience Cloud notifications for Cloud Service programs were not consistently received.
* In specific projects, the *ResourceResolver objects should always be closed* would produce a Null Pointer Exception; this, however, did not impact pipeline execution.

