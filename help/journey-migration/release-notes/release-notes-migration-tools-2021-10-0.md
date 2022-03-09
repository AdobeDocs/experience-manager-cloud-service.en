---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2021.10.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2021.11.0
feature: Release Information
exl-id: 6b1caa63-dcb0-4c48-ab2c-fd72617abf13
---
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2021.10.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2021.10.0.

>[!NOTE]
>To see the current Release Notes for Adobe Experience Manager as a Cloud Service, click [here](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/release-notes/release-notes/release-notes-current.html).

## Cloud Acceleration Manager {#cam-release}

### Release Date {#release-date-cam}

The Release Date for Cloud Acceleration Manager is October 25, 2021.

### What's New {#what-is-new-cam}

Cloud Acceleration Manager now provides users with the ability to view historical BPA reports in a Trendline Report. With this Report, users can view the progress they are making in an easy to consume graphical representation. Refer to [Using View Trendline](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-acceleration-manager/using-cam/cam-readiness-phase.html?lang=en#trendline-view-cam) for more details.

### Release Date {#release-date-october-cam}

The Release Date for Cloud Acceleration Manager is October 04, 2021.
 
### What is New {#what-is-new-cam-oct}

Cloud Acceleration Manager now provides users with the ability to view the BPA reports in a printable preview, allowing simple printing or printing to PDF for easy shareability. Refer to Step 6 and 7 in [Using Best Practices Analysis Card](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-acceleration-manager/using-cam/cam-readiness-phase.html?lang=en#best-practices-analysis).


## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt-latest}

The Release Date for Content Transfer Tool v1.6.0 is October 04, 2021.

### What's New {#what-is-new-ctt-oct}

* Improved User Mapping Tool with a simplified User Experience, including the following features listed below. For more details, refer to [Using User Mapping Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/user-mapping-tool/using-user-mapping-tool.html).
  * Test connection to the User Management API before running the User Mapping
  * Gracefully skip errors and continue with the User Mapping activity
  * User Mapping no longer fails if **Access Token** expires after 24 hours. User Mapping can be re-run from where it last stopped.

* To increase the Content Transfer Tool robustness, content can be ingested to either Author instance or Publish instance at a time. See [Getting Started with Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/getting-started-content-transfer-tool.html?lang=en) for more details.

* When versions are included, the path `/var/audit` is automatically included to migrate audit events.

## Best Practices Analyzer {#best-practices-analyzer}

### Release Date {#release-date-bpa-latest}

The Release Date for Best Practices Analyzer v2.1.20 is October 05, 2021.

### What's New {#what-is-new-bpa-oct}

* Ability to detect and report on node name length.

* Ability to detect and report on the total Index size.

* Ability to detect and report on assets that are missing their original rendition.
