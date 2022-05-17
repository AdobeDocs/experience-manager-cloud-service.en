---
title: Release Notes for Cloud Manager in AEM as a Cloud Service Release 2021.11.0
description: These are the release notes for Cloud Manager in AEM as a Cloud Service release 2021.11.0
feature: Release Information
exl-id: 98fd6d8a-ddc2-4f53-9dfc-d8e21af0c14d
---
# Release Notes for Cloud Manager in Adobe Experience Manager as a Cloud Service 2021.11.0 {#release-notes}

This page outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.11.0.

>[!NOTE]
>
>Refer to [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager in AEM as a Cloud Service 2021.11.0 is November 4, 2021.
The next release is planned for December 16, 2021.

## What's New {#what-is-new}

* Users can now leverage new Front End pipelines to exclusively deploy front end code in an accelerated manner. See [Cloud Manager Front End Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#front-end) to learn more.

   >[!IMPORTANT]
   >You must be on AEM version `2021.10.5933.20211012T154732Z` to leverage new Front End pipelines.

* Code Quality pipeline duration is significantly reduced by performing the code analysis in a more efficient way without the need of building a whole AEM image. This change will roll out progressively over the weeks following the release.

* The Git Commit ID will now be displayed in the pipeline execution details making it easier to track the code that was built.

* Program Creation is now available via publicly exposed API.

* Environment Creation is now available via publicly exposed API.

* The `x-request-id` response header is now visible in the API Playground on [www.adobe.io](https://www.adobe.io/). This header is useful when submitting customer care issues for troubleshooting.

* As a user, I see  Pipeline card with zero pipelines provide me with appropriate guidance. 

* A new Activity Page is now available where activities such as pipeline and code executions can be viewed along with their associated details. Over time, the activities listed in this page will expand in scope along with the details provided.

* A new Pipelines page with an on-hover, status popover for easy view of the summary of details is now available. Pipeline executions can be viewed along with their associated details.

* The Edit Pipeline API now supports changing the environment used in the deploy phases.

* An optimization in the OakPal scanning process has been introduced for large packages.

* The quality issue CSV file will now contain the timestamp for each quality issue. 

## Bug Fixes {#bug-fixes}

* Certain unorthodox build configurations resulted in unnecessary files being stored in the pipeline's Maven artifact cache which resulted in extraneous network I/O when starting and stopping the build container. 

* Pipeline PATCH API fails if deploy phase does not exist.

* The `ClientlibProxyResourceCheck` quality rule was producing false positive issues when there were client libraries with common base paths.

* Error message when max number of repositories has been reached did not specify the reason for the error.

* In rare cases, pipelines were failing due to inappropriate retry handling of certain response codes.
