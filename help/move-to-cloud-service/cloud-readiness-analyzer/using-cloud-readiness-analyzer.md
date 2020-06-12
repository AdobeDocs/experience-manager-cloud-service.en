---
title: Using Cloud Readiness Analyzer
description: Using Cloud Readiness Analyzer
---

# Using Cloud Readiness Analyzer {#using-cloud-readiness-analyzer}

## Important Considerations for Using Cloud Readiness Analyzer {#imp-considerations}

Follow the section below to understand the important considerations while running the Cloud Readiness Analyzer (CRA):
 
* The CRA report is built using the output of the Adobe Experience Manager (AEM) [Pattern Detector](https://docs.adobe.com/content/help/en/experience-manager-65/deploying/upgrading/pattern-detector.html). The version of Pattern Detector used by CRA is included in the CRA installation package.
 
* The CRA may only be run by the `admin` user or a user in the `Administrators` group.
 
* CRA is supported on AEM instances with version 6.1 and above.
 
* CRA can run on any environment, but it is preferred to have it run on a *Stage* environment.
 
   >[!NOTE]
   >In order to avoid an impact on business critical instances, it is recommended to run CRA on an *Author* staging environment that is as close as possible to the production environment in the areas of customizations, configurations, content and user applications. Alternatively, it can be run on a clone of the production *Author* environment.
 
* The CRA report generation can take a significant amount of time, from several minutes to a few hours. The amount of time required is highly dependent on the size and nature of the AEM repository content, the AEM version, and other factors.
 
* Because of the significant time required to generate the report, results are held in a cache and are available for subsequent viewing and downloading until the cache expires or the report is explicitly refreshed.

## Availability {#availability}

The Cloud Readiness Analyzer can be downloaded as a zip file from the Software Distribution Portal. You can install the package via Package Manager on your source Adobe Experience Manager (AEM) instance.

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

### AEM 6.3 and later {#aem-older-version}
 
For AEM 6.3 and above, the primary way to run Cloud Readiness Analyzer is to:
 
1. Use the Adobe Experience Manager user interface to navigate to Tools -> **Operations** -> **Cloud Readiness Analyzer**.
 
    >[!NOTE]
    >The CRA will begin a background process to generate the report as soon as the tool is opened. It displays an indication that the report generation is in process until the report is ready. You may close your browser tab and return at a later time to view the report when it is complete.
 
Once the CRA report has been generated and displayed, you have the option of downloading the report in a comma-separated values (CSV) format by clicking the **CSV** button in the upper right corner of the tool page.
 
You may force the CRA to clear its cache and regenerate the report by clicking the "Refresh Report" button in the upper left corner.
 
### AEM 6.2 and 6.1 {#aem-specific-versions}
 
The CRA user interface is limited in AEM 6.2 to a link that generates and downloads the CSV report. For AEM 6.1, the user interface is not functional and only the HTTP interface may be used.
 
In all versions, the included Pattern Detector may be run independently.
 
## CRA Summary Report {#cra-summary-report}
 
When the CRA is run in the AEM user interface, the report is displayed as results in the tool window. The format of the report is:
 
* Report Overview: Information about the report itself, including when it was generated.
* System Overview: Information about the AEM system on which the CRA was run.
* Finding Categories: Multiple sections that each address one or more findings of the same category. Each section includes the following: Category name, sub-types, finding count and importance, summary, link to category documentation, and individual finding information.
 
An importance level is assigned to each finding to indicate a rough priority for action. The importance levels used are as follows:
 
|Importance|Description|
|--- |--- |
|INFO|This finding is provided for informational purposes.|
|ADVISORY|This finding is potentially an upgrade issue. Further investigation is recommended.|
|MAJOR|This finding is likely to be an upgrade issue that should be addressed.|
|CRITICAL|This finding is very likely to be an upgrade issue that must be addressed to prevent loss of function or performance.|
 
## CRA CSV Report {#crs-csv-report}
 
When the "CSV" button is pressed, the CSV format of the CRA report is built from the results cache and returned to your browser. Depending on your browser settings, this report will be automatically downloaded as a file with a default name of `results.csv`. If the cache has expired then the report will be regenerated before the CSV file is built and downloaded.

Follow the steps below to generate a CSV format of the summary report from your AEM instance:

1. 1. Select the Adobe Experience Manager and navigate to tools -> **Operations** -> **Cloud Readiness Analyzer**.

1. Once the report is available, click on **CSV** to download the full summary report in comma-separated values (CSV) format, as shown in the figure below.

   ![image](/help/move-to-cloud-service/cloud-readiness-analyzer/assets/cra-3.png)
 
The CSV format of the report includes information that is generated from the Pattern Detector output, sorted and organized by category type, sub-type, and importance level. Its format is suitable for viewing and editing in an application such as Microsoft Excel. It is intended to provide all of the finding information in a repeatable format that can be helpful when comparing reports over time to measure progress.
 
The columns of the CSV format report are:

* **code**: the category code
* **type**: the category name
* **subtype**: the category sub-type
* **importance**: the importance level
* **identifier**: the primary identifier of the finding
* **other**: additional information about the finding
* **message**: the message provided for the finding
* **moreInfo**: a link which may be used to access online help about the category
* **context**: a JSON string of finding data
 
A value of "\N" in an column for an individual finding indicates that no data was provided.
 
## HTTP Interface {#http-interface}
 
The CRA provides an HTTP interface that may be used as an alternative to the AEM user interface. The interface supports both HEAD and GET commands. It may be used to generate the CRA report and return it in one of three formats: JSON, CSV, and tab-separated values (TSV).
 
The following URLs are available for HTTP access, where `<host>` is the hostname, and port if necessary, of the server on which the CRA is installed:
* `http://<host>/apps/readiness-analyzer/analysis/result.json` for JSON format
* `http://<host>/apps/readiness-analyzer/analysis/result.csv` for CSV format
* `http://<host>/apps/readiness-analyzer/analysis/result.tsv` for TSV format
 
### Executing an HTTP Request {#executing-http-request}
 
The HTTP interface may be used in a variety of methods.
 
One simple way is to open a browser tab in the same browser in which you have already signed in to AEM as an administrator. You can enter the URL in the browser tab and have the results displayed or downloaded by the browser.
 
You may also use a command-line tool such as `curl` or `wget` as well as any HTTP client application. When not using an browser tab with an authenticated session, you must supply an administrative user name and password as part of the comment. The following is an example of how this can be done:
`curl -u admin:admin 'http://localhost:4502/apps/readiness-analyzer/analysis/result.csv' > result.csv`
 
### Headers and Parameters {#http-headers-and-parameters}
 
The following HTTP headers are used by this interface:
 
* `Cache-Control: max-age=<seconds>`: Specify the cache freshness lifetime in seconds. (See [RFC 7234](https://tools.ietf.org/html/rfc7234#section-5.2.2.8).)
* `Prefer: respond-async`: Indicates that the server should respond asynchronously. (See [RFC 7240](https://tools.ietf.org/html/rfc7240#section-4.1).)
 
The following HTTP query parameters are available as a convenience for when HTTP headers might not be easily used:
 
* `max-age` (number, optional): Specify the cache freshness lifetime in seconds. This number must be 0 or greater. The default freshness lifetime is 86400 seconds, meaning that without this parameter or the corresponding header a fresh cache will be used to serve requests for 24 hours before the report must be regenerated. Using `max-age=0` will force the cache to be cleared and initiate a regeneration of the report. Immediately following this request the freshness lifetime will be reset to the previous non-zero value.
* `respond-async` (boolean, optional): Specify that the response should be provided asynchronously. Using `respond-async=true` when the cache is stale will cause the server to return a response of `202 Accepted, processing cache` without waiting for the report to be generated and the cache to be refreshed. If the cache is fresh then this parameter has no effect. The default value is `false`, meaning that without this parameter or the corresponding header, the server will respond synchronously, which may require a significant amount of time and require an adjustment to the maximum response time for the HTTP client.
 
When both an HTTP header and corresponding query parameter are present, the query parameter will take precedence.
 
A simply way to initiate the generation of the report via the HTTP interface is with the following command:
`curl -u admin:admin 'http://localhost:4502/apps/readiness-analyzer/analysis/result.json?max-age=0&respond-async=true'`
 
Once a request has been made, the client need not remain active for the report to be generated. The report generation could be initiated with one client using an HTTP GET request and, once the report has been generated, viewed from the cache in another client or the CSV tool in the AEM user interface.
 
### Responses (#http-responses)
 
The following response values are possible:
 
* `200 OK`: The response contains findings from the Pattern Detector which were generated within the freshness lifetime of the cache.
* `202 Accepted, processing cache`: Provided for asynchronous responses to indicate that the cache was stale and that a refresh is in process.
* `400 Bad Request`: Indicates that there was an error with the request. A message in Problem Details format (see [RFC 7807](https://tools.ietf.org/html/rfc7807)) provides more details.
* `401 Unauthorized`: The request was not authorized.
* `500 Internal Server Error`: Indicates that an internal server error occurred. A message in Problem Details format provides more details.
* `503 Service Unavailable`: Indicates that the server is busy with another response and cannot service this request in a timely manner. This is only like to occur when synchronous requests are made. A message in Problem Details format provides more details.
 
## Cache Lifetime Adjustment {#cache-adjustment}
 
The default CRA cache lifetime is 24 hours. With the option for refreshing a report, and regenerating the cache, in both the user interface and the HTTP interface, this default value is likely to be appropriate for most uses of the CRA. If the report generation time is particularly long for your AEM instance, you may wish to adjust the cache lifetime in order to minimize the regeneration of the report.
 
The cache lifetime value is stored as the `maxCacheAge` property on the following repository node:
`/apps/readiness-analyzer/content/CloudReadinessReport/jcr:content`
 
The value of this property is the cache lifetime in seconds. An administrator may adjust the cache lifetime using the CRX/DE Lite interface to AEM.

## Viewing the Report in AEM 6.1 Instances {#aem-instances-report}

Follow the steps below to download the CSV report for Adobe Experience Manager (AEM) 6.1:

1.Navigate to **Adobe Experience Manager Web Console
Configuration** using `https://serveraddress:serverport/system/console/configMgr`.

1. Select the **Status** tab and search for **Pattern Detector** from the drop-down list, as shown in the figure below.

   ![image](/help/move-to-cloud-service/cloud-readiness-analyzer/assets/cra-4.png)

1. You can download the summary report in a zip folder or in a JSON format.
 

