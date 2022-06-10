---
title: License Dashboard
description: Cloud Manager provides a dashboard for easy viewing of AEMaaCS product entitlements available to your organization or tenant.
exl-id: bf0f54a9-fe86-4bfb-9fa6-03cf0fd5f404
---
# License Dashboard {#license-dashboard}

Cloud Manager provides a dashboard for easy viewing of AEMaaCS product entitlements available to your organization or tenant.

## Overview {#overview}

The Cloud Manager License Dashboard provides easy access to the following information:

1. Solution entitlements available to you across all of your programs, including what's used and what's available
1. Content Request consumption metrics trended by month for the Sites solution

## Using the License Dashboard {#using-dashboard}

To access your license dashboard, follow these steps.

>[!NOTE]
>
>A user in **Business Owner** role must be logged in to view the License Dashboard.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the products overview page, switch to the **License** tab.

![License Dashboard](assets/license-dashboard.png)

The dashboard is divided into three sections showing you:

* **Solutions** - This section summarizes which solutions that you have licensed such as Sites or Assets.
* **Add-ons** - This section summarizes which add-ons to your licensed solutions that you have available.
* **Sandbox &amp; Development Environments** - This section summarizes what environments that you have available.

Each section summarizes what is available and how it is currently used, if at all. Currently only Sites solutions are displayed even if other solutions exist in the tenant.

* The **Status** column displays the number of entitlements unused vs. total available for the tenant.
* The **Configured on** column indicates the programs on which the solution entitlement has been applied.
  * An entitlement is considered as used only when a production environment has been created or if one already exists, if an update pipeline has been run on it. 
* The **Usage** column displays the content requests consumed in the past 12 months as a graph when clicked.

>[!TIP]
>
>Refer to [Admin Console overview](https://helpx.adobe.com/enterprise/using/admin-console.html) to learn how to manage your Adobe entitlements across your entire organization from Admin Console.

## Frequently Asked Questions {#faq}

### What is a content request? {#what-is-a-content-request}

A content request is a request coming into AEM Sites or any customer-provided caching system  such as a content delivery network to deliver content or data in either HTML format as a page view or in JSON format as an API call.

One content request is counted for each page view or for every five API calls, measured at the ingress of the first caching system to receive a content request.

Content Requests exclude requests or activity initiated by or on behalf of Adobe for the sole purpose of providing products and services. Adobe-identified user agent traffic from bots, crawlers, and spiders related to common search engines and social media services are also excluded.

### How does Adobe Experience Manager measure content requests? {#how-are-content-requests-measured}

Content requests are tracked server-side within Cloud Service. The CDN built into AEM as a Cloud Service tracks valid HTML and JSON requests. AEM also has rules in place to exclude well-known bots, including well-known services visiting the site regularly to refresh their search index or service.

The following is a non-exhaustive list of examples of excluded well-known services.

* AddSearchBot 
* AhrefsBot 
* Applebot 
* Ask Jeeves Corporate Spider 
* Bingbot 
* BingPreview 
* BLEXBot 
* BuiltWith 
* Bytespider 
* CrawlerKengo 
* Facebookexternalhit 
* Google AdsBot 
* Google AdsBot Mobile 

### Why does my Analytics report show different results than the AEM Content Requests? {#why-are-reports-different}

Content Requests will have variances with an organization’s Analytics reporting tools as summarized in this table.

|Reason For Variance|Explanation|
|---|---|
|Tagging|All pages that are tracked as AEM content requests may or may not be tagged with Analytics tracking.<br>All API calls that are tracked as AEM content requests will not be tagged by an organization’s Analytics tool.<br>Pages or API calls may be tagged to track actions instead of views.|
|Tag Management Rules|Tag management rule settings may result in a variety of data collection configurations on a page, resulting in some combination of discrepancies with content request tracking.|
|Bots|Unknown bots that have not been pre-identified and removed by AEM may cause tracking discrepancies.|
|Report Suites|Pages that are part of the same AEM instance and domain may send data to different Analytics report suites.|
|Third-Party Monitoring and Security Tools|Monitoring and security scanning tools may generate content requests for AEM that are not tracked in Analytics reports.|
|Prefetch Requests|Using a prefetch service to pre-load pages to increase speed can cause significant content request traffic increases.|
|DDOS|While Adobe makes every effort to automatically detect and filter out traffic from DDOS attacks, there is no guarantee that all possible DDOS attacks will be detected.|

### What if I am using my own CDN? {#using-own-cdn}

The Content Request Dashboard in Cloud Manager will not show tracking for your own CDN.
