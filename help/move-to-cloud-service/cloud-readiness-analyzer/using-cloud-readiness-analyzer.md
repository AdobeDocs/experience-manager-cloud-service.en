---
title: Using Cloud Readiness Analyzer
description: Using Cloud Readiness Analyzer
---

# Using Cloud Readiness Analyzer {#using-cloud-readiness-analyzer}

## Important Considerations for Using Cloud Readiness Analyzer {#imp-considerations}

Follow the section below to understand the important considerations while running the Cloud Readiness Analyzer (CRA):

* CRA is supported on source AEM instances with version 6.1 and above.
* CRA can run on any environment. However, in order to increase the detection rate and avoid any slowdowns on business critical instances, it is recommended to run it on the source author staging environments that are as close as possible to production ones in the areas of customizations, configurations, content and user applications. Alternatively, it can also be run on a clone of the Publish environment.

## Availability {#availability}

The Cloud Readiness Analyzer (CRA) can be downloaded as a zip file from the the Software Distribution portal. You can install the package via Package Manager on your source Adobe Experience Manager (AEM) instance.

>[!NOTE]
>Download the Cloud Readiness Analyzer (CRA) from pending.

## Running the Cloud Readiness Analyzer {#running-tool}

Follow this section to learn how to run Cloud Readiness Analyzer:

1. Select the Adobe Experience Manager and navigate to tools -> **Operations** -> **Cloud Readiness Analyzer**.

### Viewing the Results {#viewing-the-results}

There are two ways to view the output of the CRA:

1. Using the organized report (available on AEM version 6.3 and above)
Refer to CRA Document Planning and Status to describe importance levels in the report

To view the output of the CRA (can be used with AEM version 6.1 and above):

1. Navigate to AEM Web Console by browsing to.

1. Select Status - Cloud Readiness Analyzer as shown in the image below.