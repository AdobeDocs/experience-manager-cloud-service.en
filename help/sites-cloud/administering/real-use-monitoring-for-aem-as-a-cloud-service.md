---
title: Real Use Monitoring for AEM as a Cloud Service
description: Learn how to use Real Use Monitoring (RUM) to capture and analyze the digital user experience of a website or application in real-time.
exl-id: 91fe9454-3dde-476a-843e-0e64f6f73aaf
---
# Real Use Monitoring Service for AEM as a Cloud Service {#real-use-monitoring-service-for-aem-as-a-cloud-service}

>[!NOTE]
>
>Adobe is excited to announce the [GA rollout](/help/release-notes/release-notes-cloud/release-notes-current.md#real-use-monitoring) for Real Use Monitoring service, the client-side collection of data. It is an automated service and there is no customer setup required.

>[!INFO]
>
>Client-side monitoring only works for customers with AEM Cloud Service version **2024.5.16461** and above.

## Overview {#overview}

The Real Use Monitoring (RUM) service is a performance monitoring technology that captures and analyzes the digital user experiences of a website or application in real-time. It provides visibility into the real-time performance of a web application and provides deeper insight into the end-user experience. "Real User Monitoring" has been rebranded to "Real Use Monitoring" because it better reflects the true essence of the service. The service focuses on optimizing performance by monitoring website engagements, rather than the users themselves.

With RUM, key performance metrics are tracked right from the initiation of the URL until the request is served back to the browser. It helps developers enhance the application to make it easy to use for the end users. 

## Who Can Benefit From a Real Use Monitoring Service? {#who-can-benefit-from-rum-service}

Real Use Monitoring service is beneficial for all customers. It offers a representative reflection of user interactions, ensuring a reliable measure of website engagement by capturing the number of client-side page views. 

For all Adobe customers, this service provides valuable insights into user interactions. Customers employing their own CDN can benefit from simplified traffic reporting, as Adobe now directly integrates the data collection, eliminating the need for separate reports during renewal cycles. 

Would you like to unlock the full potential of your website, using Adobe's Early Adopter RUM Explorer visualization tool to gain useful insights into your website engagement? This tool can provide insights into your page performance, including metrics on the number of clicks, Core Web Vitals (CWV), conversions, and customer journey maps. By using these powerful insights, you can fine-tune your digital experiences to meet your users' needs more effectively. If you wish to learn more and get access, email us at `rum-explorer@adobe.com`.

## Understand how the Real Use Monitoring Service Works {#understand-how-the-rum-service-works}

Adobe Experience Manager (AEM) uses Real Use Monitoring (RUM) to help customers and Adobe understand how visitors interact with AEM sites. It helps them diagnose performance issues, and measure the effectiveness of experiments. RUM preserves the privacy of visitors through sampling - only a small portion of all page views is monitored - and no personally identifiable information (PII) is collected. 

## Real Use Monitoring Service and Privacy {#rum-service-and-privacy}

The Real Use Monitoring service in AEM is designed to preserve visitor privacy and minimize data collection. As a visitor, it means that the site you are visiting or made available to Adobe, does not collect any personal information. 

As a site operator, no additional opt-in is required to enable monitoring through this feature. There is no additional pop-up or consent form for the end users to accept for enabling RUM. 

## Real Use Monitoring Service Data Sampling {#rum-service-data-sampling}

Traditional web analytics solutions try to collect data on every single visitor. AEM's RUM service only captures information from a small fraction of page views. The service is meant to be sampled and anonymized rather than a replacement for analytics. By default, pages have a 1:100 sampling ratio. Site operators cannot increase or decrease the sampling rate at this time. To estimate total traffic accurately, for every 100 page views, data is gathered from 1, giving you a reliable approximation of overall traffic.

As the decision of whether the data is collected, it is made on a page view by page view basis, and it becomes virtually impossible to track interactions across multiple pages. By design, RUM has no concept of visitors or sessions, only of page views.

## What Data is Being Collected {#what-data-is-being-collected}

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
* The Core Web Vitals (CWV) performance metrics, including the Largest Contentful Paint (LCP), First Input Delay (FID), Cumulative Layout Shift (CLS), and Time To First Byte (TTFB) that describe the visitor's quality of experience.

## How Real Use Monitoring Works for a customer {#how-rum-works-for-a-customer}

Real Use Monitoring automatically monitors client-side traffic to provide you with valuable insights. As an Adobe customer, you do not need to take any additional steps, as this service is seamlessly integrated into your existing setup. With the General Availability (GA) rollout, you automatically benefit from this new feature.

<!-- Alexandru: hiding temporarily, until we figure out where this needs to be linked to 

If you wish to leverage more insights with this new feature to optimize your digital experiences effortlessly, please see here (link to Row 99). -->

## How Real Use Monitoring Service Data is Being Used {#how-rum-service-data-is-being-used}

RUM data is beneficial for the following purposes:

* To identify and fix performance bottlenecks for customer sites
* To streamline automated traffic lookup that includes page views.
* To understand how AEM interacts with other scripts (such as analytics, targeting, or external libraries) on the same page, to increase compatibility.

## Limitations and Understanding Variance in Page Views and Performance Metrics {#limitations-and-understanding-variance-in-page-views-and-performance-metrics}

As you analyze RUM data, there may be variances in page views and other performance metrics. These variances can be attributed to several factors inherent in real-time, client-side monitoring. Here are key considerations for customers to keep in mind when interpreting their RUM data:

1. **Tracker Blockers**

   * End-users employing tracker blockers or privacy extensions can impede RUM data collection, as these tools restrict the tracking scripts' execution. This restriction may lead to underreported page views and user interactions, creating a discrepancy between actual site activity and the data captured by RUM.

1. **Limitations in capturing headless API/JSON calls**

   * RUM data service focuses on the client-side experience and doesn't capture the backend API or JSON calls made from a non-AEM headless app at this time. The exclusion of these calls from RUM service data creates variances from the content requests measured by CDN Analytics.

## FAQ {#faq}


1. **Can customers integrate the RUM service scripts with third-party systems like Dynatrace?**

   Yes.

1. **Are "Interaction to next paint," "Time to first byte," and "First contentful paint" Web vitals Metrics being collected?**

   Interaction to next paint (INP) and Time To First Byte (TTFB) are collected.  First contentful paint is not collected at this time.
   
1. **The `/.rum` path is blocked on my site, how should I fix?**

   The `/.rum` path is required for RUM collection to work. If you have a CDN in front of what Adobe provides as part of AEM as a Cloud Service, ensure that the `/.rum` path forwards to the same AEM origin as the rest of your AEM content. And, ensure that it is not adjusted in any way.
   
1. **Does RUM collection count toward content requests for contractual purposes?**

   The RUM library and the RUM collection do not count as content requests and do not increase the reported number of page views or API calls. Additionally, for customers who use out-of-the-box CDN with AEM as a Cloud Service, [server-side collection](#serverside-collection) is the basis for content requests.
   
1. **How can I opt out?**

   Adobe recommends using the Real Use Monitoring (RUM) due to its significant benefits and that it can allow you to optimize your digital experiences. It can offer valuable insights that can help improve website performance. The service is designed to be seamless and has no impact on your website's performance.

   Opting out means missing these insights. However, if you encounter any issues, contact Adobe Support.
