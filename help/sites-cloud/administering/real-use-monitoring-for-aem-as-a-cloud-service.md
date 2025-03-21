---
title: Real Use Monitoring for AEM as a Cloud Service
description: Learn about Real Use Monitoring (RUM) , an automated service that allows to monitor the client-side collection of data.
exl-id: 91fe9454-3dde-476a-843e-0e64f6f73aaf
feature: Administering
role: Admin
---
# Real Use Monitoring service for AEM as a Cloud Service {#real-use-monitoring-service-for-aem-as-a-cloud-service}

>[!NOTE]
>
>Real Use Monitoring service, the client-side collection of data, is an automated service. No customer setup is required.

>[!INFO]
>
>Client-side monitoring only works for customers with AEM (Adobe Experience Manager) Cloud Service version **2024.5.16461** and above.

## Overview {#overview}

The RUM (Real Use Monitoring) service is a performance monitoring technology that monitors the client-side traffic on a website or an application in real-time. This service focuses on collecting metrics and data that are key to optimize performance by monitoring website engagements, rather than the users themselves. With RUM, key performance metrics are tracked right from the initiation of the URL until the request is served back to the browser.

## Who can benefit from a Real Use Monitoring service? {#who-can-benefit-from-rum-service}

Real Use Monitoring helps customers and Adobe to understand how end-users interact with AEM sites. Real Use Monitoring diagnoses performance issues, and measure the effectiveness of experiments. Real Use Monitoring preserves the privacy of visitors through sampling - only a small portion of all page views is monitored - and no personally identifiable information (PII) is collected.

## Real Use Monitoring service and privacy {#rum-service-and-privacy}

The Real Use Monitoring service in AEM preserves visitor privacy and minimize data collection. As a visitor, it means that the site you are visiting or made available to Adobe, does not collect any personal information. 

As a site operator, no additional opt-in is required to enable monitoring through this feature. There is no additional pop-up or consent form for the end users to accept for enabling RUM. 

## Real Use Monitoring service data sampling {#rum-service-data-sampling}

Traditional web analytics solutions try to collect data on every single visitor. AEM's Real Use Monitoring (RUM) service only captures information from a small fraction of page views. The service is meant to be sampled and anonymized rather than a replacement for analytics. By default, pages have a 1:100 sampling ratio. Site operators cannot increase or decrease the sampling rate at this time. To estimate total traffic accurately, for every 100 page views, data is gathered from 1, giving you a reliable approximation of overall traffic.

As the decision of whether the data is collected, it is made on a page view by page view basis, and it becomes virtually impossible to track interactions across multiple pages. By design, RUM has no concept of visitors or sessions, only of page views.

## What data is collected? {#what-data-is-being-collected}

The Real Use Monitoring service is designed to prevent the collection of personally identifiable information. The full set of information collected by RUM is listed below:

* The host name of the site being visited, for example: `experienceleague.adobe.com`
* The broad user agent type and operating system that is used to display the page, such as: `desktop:windows` or `mobile:ios`
* The time of the data collection, such as: `2021-06-26 06:00:02.596000 UTC (in order to preserve privacy, we round all minutes to the previous hour, so that only seconds and milliseconds are tracked)`
* The URL of the page being visited, for instance: `https://experienceleague.adobe.com/docs`
* The Referrer URL (the URL of the page that linked to the current page, if the user followed a link)
* A randomly generated ID of the page view, in a format similar to: `2Ac6`
* The weight or inverse of the sampling rate, such as: `100`. It means only one in one hundred page views is recorded
* The checkpoint, or name, of a particular event in the sequence of loading the page. Or, interacting with it as a visitor
* The source, or identifier, of the DOM element that the user interacts with for the checkpoint mentioned above. For instance, it could be an image
* The target, or link to an external page or resource that the user interacts with for the checkpoint mentioned above. For example: `https://blog.adobe.com/jp/publish/2022/06/29/media_162fb947c7219d0537cce36adf22315d64fb86e94.png`
* The [Core Web Vitals (CWV)](https://web.dev/articles/lcp) performance metrics [Largest Contentful Paint (LCP)](https://web.dev/articles/lcp), [Interaction to Next Paint (INP)](https://web.dev/articles/inp) and [Cumulative Layout Shift (CLS)](https://web.dev/articles/cls) that describe the visitor's quality of experience.

## How Real Use Monitoring works for a customer {#how-rum-works-for-a-customer}

Real Use Monitoring automatically monitors client-side traffic. As an Adobe customer, you do not need to take any additional steps, as this service is seamlessly integrated into your existing setup. With Real Use Monitoring (RUM) service being generally available , you automatically benefit from this new feature. Real Use Monitoring service does not expose any customer facing metrics today to monitor. We are working to deliver this functionality to you as soon as possible.

<!-- Alexandru: hiding temporarily, until we figure out where this needs to be linked to 

If you wish to leverage more insights with this new feature to optimize your digital experiences effortlessly, please see here (link to Row 99). -->

## How Adobe uses Real Use Monitoring {#how-rum-data-is-being-used}

Real Use Monitoring data is used for the following purposes:

* To identify and fix performance bottlenecks for customer sites
* To understand how AEM interacts with other scripts (such as analytics, targeting, or external libraries) on the same page, to increase compatibility.
<!--
## Limitations and understanding variance in page views and performance metrics {#limitations-and-understanding-variance-in-page-views-and-performance-metrics}

Here are key considerations for customers to keep in mind when interpreting their RUM data:

1. **Tracker blockers**

   * End-users employing tracker blockers or privacy extensions can impede RUM data collection, as these tools restrict the tracking scripts' execution. This restriction may lead to underreported page views and user interactions, creating a discrepancy between actual site activity and the data captured by RUM.

1. **Limitations in capturing headless API/JSON calls**

   * RUM data service focuses on the client-side experience and doesn't capture the backend API or JSON calls made from a non-AEM headless app at this time. The exclusion of these calls from RUM service data creates variances from the content requests measured by CDN Analytics.
-->

## FAQ {#faq}

<!-- REMOVED THIS FAQ AS PER EMAIL REQUEST FROM SHWETA DUA, SEPTEMBER 4, 2024 TO THE DL-AEM-DOCS GROUP 
1. **Can customers integrate the RUM service scripts with third-party systems like Dynatrace?**

   Yes.
--> 

1. **Are "Interaction to next paint," "Time to first byte," and "First contentful paint" metrics being collected?**

   Interaction to next paint (INP) and Time To First Byte (TTFB) are collected.  First contentful paint is not collected at this time.
   
1. **The `/.rum` path is blocked on my site, how should I fix?**

   The `/.rum` path is required for RUM collection to work. If you use a CDN in front of Adobe's AEM as a Cloud Service, ensure that the `/.rum` path forwards to the same AEM origin as your other AEM content. And, ensure that it is not adjusted in any way.
   
1. **Does RUM collection count toward content requests for contractual purposes?**

   The RUM library and the RUM collection do not count as content requests and do not increase the reported number of page views or API calls. Additionally, for customers who use out-of-the-box CDN with AEM as a Cloud Service, [server-side collection](#serverside-collection) is the basis for content requests.
   
1. **How can I opt out?**

   Adobe recommends using the Real Use Monitoring (RUM) due to its significant benefits and that it will allow Adobe to help you optimize your digital experiences by improving website performance. The service is designed to be seamless and has no impact on your website's performance.

   Opting out may mean missing out a chance to improve traffic engagement on your website. However, if you encounter any issues, contact Adobe Support.