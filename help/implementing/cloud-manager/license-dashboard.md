---
title: License Dashboard
description: Cloud Manager provides a dashboard for easy viewing of AEMaaCS product entitlements available to your organization or tenant.
exl-id: bf0f54a9-fe86-4bfb-9fa6-03cf0fd5f404
---
# License Dashboard {#license-dashboard}

Cloud Manager provides a dashboard for easy viewing of AEMaaCS product entitlements available to your organization or tenant.

## Overview {#overview}

The Cloud Manager License Dashboard provides easy access to the following information:

1. Solution entitlements are available to you across all of your programs, including what's used and what's available
1. Content Request consumption metrics trended by month for the Sites solution

## Using the License Dashboard {#using-dashboard}

To access your license dashboard, follow these steps.

>[!NOTE]
>
>A user in the **Business Owner** role must be logged in to view the License Dashboard.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, switch to the **License** tab.

![License Dashboard](assets/license-dashboard.png)

The dashboard is divided into three sections showing you:

* **Solutions** - This section summarizes which solutions that you have licensed such as Sites or Assets.
* **Add-ons** - This section summarizes which add-ons to your licensed solutions that you have available.
* **Sandbox &amp; Development Environments** - This section summarizes what environments that you have available.

Each section summarizes what is available and how it is used, if at all. Currently only Sites solutions are displayed even if other solutions exist in the tenant.

* The **Status** column displays the number of entitlements unused versus the total available for the tenant.
* The **Configured on** column indicates the programs on which the solution entitlement has been applied.
  * An entitlement is considered as used only when a production environment has been created or if one exists, if an update pipeline has been run on it. 
* The **Usage** column displays the content requests consumed in the past 12 months as a graph when clicked.

>[!TIP]
>
>To learn how to manage your Adobe entitlements across your entire organization from Admin Console, see the [Admin Console overview](https://helpx.adobe.com/enterprise/using/admin-console.html).

## Frequently Asked Questions {#faq}

### What is a content request? {#what-is-a-content-request}

A content request is a request coming into AEM Sites or any customer-provided caching system such as a content delivery network to deliver content or data in either HTML format as a page view or in JSON format as an API call.

One content request is counted for each page view or for every five API calls, measured at the ingress of the first caching system to receive a content request. Content requests are counted against production environments only.

Content Requests exclude requests or activities initiated by or on behalf of Adobe for the sole purpose of providing products and services. Adobe-identified user agent traffic from bots, crawlers, and spiders related to common search engines and social media services are also excluded.

See also [Understanding Cloud Service Content Requests](/help/implementing/cloud-manager/content-requests.md).

### How does Adobe Experience Manager measure content requests? {#how-are-content-requests-measured}

Content requests are tracked on AEM as a Cloud Service's edge servers. Origin traffic does not count towards content requests. The CDN built into AEM as a Cloud Service tracks valid HTML and JSON requests.

AEM also has rules in place to exclude well-known bots, including well-known services visiting the site regularly to refresh their search index or service.

See also [Understanding Cloud Service Content Requests](/help/implementing/cloud-manager/content-requests.md).

### Why does my Analytics report show different results than the AEM Content Requests? {#why-are-reports-different}

Content Requests can have variances with an organization's Analytics reporting tools. For more information, see [Understanding Cloud Service Content Requests](/help/implementing/cloud-manager/content-requests.md).

### What if I would like to learn more about my content request volume? {#current-request-volumes}

If you would like additional insights into the content request volume shown in the License Dashboard, your Adobe team can provide a report that shows the top volume drivers of content requests. Reach out to your Adobe team or to Adobe Customer Support to request a top usage report.

### What if I am using my own CDN? {#using-own-cdn}

The License Dashboard only shows data tracked by the Cloud Service CDN. If you choose to bring your own CDN (BYOCDN), you report your content request volume back to Adobe on an annual basis, as stated in your contract.  
