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

   ![image](/help/move-to-cloud-service/cloud-readiness-analyzer/assets/cra-1.png)

1. Once you click on **Cloud Readiness Analyzer**, the tool starts generating the report and after few minutes the summary report is available on your AEM instance.

   >[!NOTE]
   >You will have to scroll down the page to view the complete report.

   ![image](/help/move-to-cloud-service/cloud-readiness-analyzer/assets/cra-2.png)

### Viewing the Results in the Summary Report {#viewing-the-results}

>[!IMPORTANT]
>The reports generated from Cloud Readiness Analyzer are based on Pattern Detectors. Refer to [Pattern Detectors](https://docs.adobe.com/content/help/en/experience-manager-65/deploying/upgrading/pattern-detector.html) for more details.

Once you scroll down the page to view the complete summary report, you can see the following information for each of the category highlighted in the report:

1. **Importance Level**

   The following table describes the meaning of the various Pattern Detector and Cloud Readiness Analyzer importance levels.

   |Importance Level|Description|
   |--- |--- |
   |INFO/0|This finding is provided for informational purposes.|
   |ADVISORY/1|This finding is potentially an upgrade issue. Further investigation is recommended.|
   |MAJOR/2|This finding is likely to be an upgrade issue that should be addressed.|
   |CRITICAL/3|This finding is very likely to be an upgrade issue that must be addressed to prevent loss of function or performance.|

1. **Description**
   The description provides an information on the reported category.

1. **Documentation URL**
   The documentation URL allows you to view the technical documentation for the associated type.

1. **Message**
   A description of the finding in a single message.

### Viewing the Results in a CSV Format {#viewing-the-results-csv}

The summary report is available in the AEM User Interface. You can download the full report in a comma-separated values (CSV) format that is helpful during the refactoring process.

Follow the steps below to generate a CSV format of your summary report:

1. 1. Select the Adobe Experience Manager and navigate to tools -> **Operations** -> **Cloud Readiness Analyzer**.

1. Once the report is available, click on **CSV** to download the full summary report in comma-separated values (CSV) format, as shown in the figure below.

![image](/help/move-to-cloud-service/cloud-readiness-analyzer/assets/cra-3.png)


#### Viewing the Report in AEM 6.1 Instances {#aem-instances-report}

Follow the steps below to download the CSV report for Adobe Experience Manager (AEM) 6.1:

1.Navigate to **Adobe Experience Manager Web Console
Configuration** using `https://serveraddress:serverport/system/console/configMgr`.

1. Select the **Status** tab and search for **Pattern Detector** from the drop-down list, as shown in the figure below.

   ![image](/help/move-to-cloud-service/cloud-readiness-analyzer/assets/cra-4.png)

1. You can download the summary report in a zip folder or in a JSON format.
 

