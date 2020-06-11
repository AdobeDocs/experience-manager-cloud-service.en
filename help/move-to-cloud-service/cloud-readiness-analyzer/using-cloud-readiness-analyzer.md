---
title: Using Cloud Readiness Analyzer
description: Using Cloud Readiness Analyzer
---

# Using Cloud Readiness Analyzer {#using-cloud-readiness-analyzer}

## Important Considerations for Using Cloud Readiness Analyzer {#imp-considerations}

Follow the section below to understand the important considerations while running the Cloud Readiness Analyzer (CRA):

* CRA is supported on source AEM instances with version 6.1 and above
* CRA can run on any environment (preferably *Stage* environment)

   >[!NOTE]
   >In order to increase the detection rate and avoid any slowdowns on business critical instances, it is recommended to run CRA on the source author staging environments that are as close as possible to production ones in the areas of customizations, configurations, content and user applications. Alternatively, it can also run on a clone of the *Publish* environment.

## Availability {#availability}

The Cloud Readiness Analyzer can be downloaded as a zip file from the the Software Distribution portal. You can install the package via Package Manager on your source Adobe Experience Manager (AEM) instance.

>[!NOTE]
>Download the Cloud Readiness Analyzer from the Software Distribution Portal *pending*.

## Running the Cloud Readiness Analyzer {#running-tool}

Follow this section to learn how to run Cloud Readiness Analyzer:

1. Select the Adobe Experience Manager and navigate to tools -> **Operations** -> **Cloud Readiness Analyzer**.

### Viewing the Results {#viewing-the-results}

>[!IMPORTANT]
>The reports generated from Cloud Readiness Analyzer are based on Pattern Detectors. Refer to [Pattern Detectors](https://docs.adobe.com/content/help/en/experience-manager-65/deploying/upgrading/pattern-detector.html) for more details.

There are two ways to view the output from the Cloud Readiness Analyzer:

1. **Using the Organized Report**

   >[!NOTE]
   >The organized report is available on AEM version 6.3 and above.

   Or,

1. **Viewing the output of the CRA**

   Follow the steps below to view the output from the Cloud Readiness Analyzer:

   >[!NOTE]
   >The steps below are applicable to AEM version 6.1 and above.

   1. Navigate to **AEM Web Console** using `https://serveraddress:serverport/system/console/configMgr`.

   1. Select **Status - Pattern Detector** as shown in the figure below.

#### Viewing the Report in AEM 6.1 Instances {#aem-instances-report}

You can download the csv report for AEM 6.1.This is pending. 

#### Understanding Importance Levels in the Report {#importance-levels}

The following table describes the meaning of the various Pattern Detector and Cloud Readiness Analyzer importance levels.

|Importance Level|Description|
|--- |--- |
|INFO/0|This finding is provided for informational purposes.|
|ADVISORY/1|This finding is potentially an upgrade issue. Further investigation is recommended.|
|MAJOR/2|This finding is likely to be an upgrade issue that should be addressed.|
|CRITICAL/3|This finding is very likely to be an upgrade issue that must be addressed to prevent loss of function or performance.|