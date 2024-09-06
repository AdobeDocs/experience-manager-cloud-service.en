---
title: Release Notes for Cloud Manager 2024.9.0 in Adobe Experience Manager as a Cloud Service
description: Learn about the release notes for Cloud Manager 2024.9.0 in AEM as a Cloud Service.
feature: Release Information
role: Admin

---
# Release notes for Cloud Manager 2024.9.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager release 2024.9.0 in AEM as a Cloud Service.

>[!NOTE]
>
>See the [current release notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md).

## Release date {#release-date}

The release date for Cloud Manager release 2024.9.0 in AEM as a Cloud Service is September 5, 2024. The next release is planned for October 3, 2024.

## What's new {#what-is-new}

* **Experience Audit dashboard:**

    Adobe Cloud Manager's [enhanced Experience Audit dashboard](/help/implementing/cloud-manager/experience-audit-dashboard.md), powered by Google Lighthouse, provides insights into the quality and performance of AEM Sites by evaluating core web vitals, SEO, and accessibility metrics. It helps users identify areas for improvement by offering actionable recommendations, enabling teams to enhance user experience, page load times, and site compliance. This dashboard simplifies the monitoring of critical site metrics and ensures that AEM applications meet high performance and accessibility standards.

* **Adobe generated and managed Domain Validation certificates:**

    With Cloud Manager, you are now able to [self-service Adobe generated and managed DV (Domain Validation) SSL certificates](/help/implementing/cloud-manager/managing-ssl-certifications/domain-validated-certificates.md). This capability gives you the fastest, easiest, and most cost-effective solution to create a secure website for your online organization or business. <!-- CMGR-52403 -->

* **Edge Delivery Services support in Cloud Manager:**

    If you have licensed Edge Delivery Services as part of AEM Sites, [you can now onboard your site with Edge Delivery Services directly through Cloud Manager](/help/implementing/cloud-manager/edge-delivery-services.md). This feature enables a guided, self-service Go Live experience. It also unifies essential workflows like domain name management, SSL certificates, and CDN mappings across all your AEM properties, ensuring consistency. <!-- CMGR-49859 -->

* KEEP IN? Starting this release, customers using GitHub repositories can now create and use Web Tier Config pipelines. ( CMGR-59046 and Slack https://cq-dev.slack.com/archives/C07LFP5BZ2L/p1725407057847379 )

* KEEP IN? SSL Certificates table in Cloud Manager now enables pagination in the user experience. ( https://jira.corp.adobe.com/browse/CMGR-61041 and Slack https://cq-dev.slack.com/archives/C07LFRE9QJU/p1725408553760009 )


<!--
## Early adoption program {#early-adoption}

For a chance to test some upcoming features, be a part of Adobe's early adoption program. -->


## Bug fixes

* Pagination for SSL certificates table view now works as expected. CMGR-60804 - [UI] Pagination doesn't work for ssl certificates



* When promoting an older source pipeline execution, the target used the most recent one. CMGR-59519

* KEEP IN? Fixed a UI bug that would cause the wrong artifact version to be promoted when using the "Promote Build" button from an execution ( https://jira.corp.adobe.com/browse/CMGR-59519 and Slack https://cq-dev.slack.com/archives/C07LFPN2R08/p1725408253474129 )