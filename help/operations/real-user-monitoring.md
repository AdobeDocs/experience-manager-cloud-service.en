---
title: Real User Monitoring (RUM) for AEM as a Cloud Service
description: Leverage Real User Monitoring (RUM) in order to keep track of all the actual user interactions of a website or an application in real-time
---

# Real User Monitoring (RUM) for AEM as a Cloud Service {#real-user-monitoring-for-aem-as-a-cloud-service}

>[!INFO]
>
>This feature is only available to the early adopter program. 
>Customers need to be on AEM Cloud Service version 2023.11.14227 and above for enabling RUM data service.
>

## Overview {#overview}

Real User Monitoring (RUM) is a type of performance monitoring technology that captures and analyzes the digital user experiences of a website or application in real-time. It gives complete visibility into the real-time performance of a web application and provides accurate insight into the end-user experience. 

RUM provides deep insight into key performance metrics right from the initiation of the URL until the request is served back to the browser all of which helps the developers enhance the application to make it easy to use for the end users. 

## Understand how the RUM Data Service Works {#understand-how-the-rum-data-service-works}

Adobe Experience Manager uses Real User Monitoring (RUM) to understand how visitors are interacting with Adobe Experience Manager-powered sites, to diagnose performance issues, and to measure the effectiveness of experiments. RUM preserves the privacy of visitors through sampling - only a small portion of all page views will be monitored - and judicious exclusion of all personally identifiable information (PII). 

## RUM and Privacy {#rum-and-privacy}

Real User Monitoring in Adobe Experience Manager is designed to preserve visitor privacy and minimize data collection. As a visitor, this means that no personal information will be collected by the site you are visiting or made available to Adobe. 

As a site operator, this means no additional opt-in is required to enable monitoring through this feature.So, there will be no additional pop up for the end users to accept for enabling RUM monitoring. 

## RUM Data is Sampled {#rum-data-is-sampled}

Traditional web analytics solutions try to collect data on every single visitor. Adobe Experience Manager's Real User Monitoring only captures information from a small fraction of page views.RUM is meant to be sampled and anonymized rather than a replacement for analytics. By default, pages will have a 1:100 sampling ratio. Site operators cannot configure this number to increase or decrease the sampling rate as of today.

As the decision of whether the data will be collected is made on a page view by page view basis, it becomes virtually impossible to track interactions across multiple pages. RUM has no concept of visits, visitors, or sessions, only of page views. This is by design.

## What Data is Being Collected {#what-data-is-being-collected}

RUM is designed to prevent the collection of personally identifiable information. The full set of information that can be collected by Adobe Experience Manager's Real User Monitoring is listed below:

* The host name of the site being visited, for example: `experienceleague.adobe.com`
* The broad user agent type that is used to display the page, such as: desktop or mobile
* The time of the data collection, such as: `2021-06-26 06:00:02.596000 UTC (in order to preserve privacy, we round all minutes to the previous hour, so that only seconds and milliseconds are tracked)`
* The URL of the page being visited, for instance: `https://experienceleague.adobe.com/docs`
* The Referrer URL (the URL of the page that linked to the current page, if the user followed a link)
* A randomly generated ID of the page view, in a format similar to: `2Ac6`
* The weight or inverse of the sampling rate, such as: `100`. This means only one in one hundred page views will be recorded
* The checkpoint, or name of a particular event in the sequence of loading the page or interacting with it as a visitor
* The source, or identifier of the DOM element that the user interacts with for the checkpoint mentioned above. For instance, this could be an image
* The target, or link to an external page or resource that the user interacts with for the checkpoint mentioned above. For example: `https://blog.adobe.com/jp/publish/2022/06/29/media_162fb947c7219d0537cce36adf22315d64fb86e94.png`
* The Core Web Vitals (CWV) performance metrics, the Largest Contentful Paint (LCP), First Input Delay (FID), and Cumulative Layout Shift (CLS) that describe the visitor's quality of experience.

## How to Set Up the RUM Data Service {#how-to-set-up-them-rum-data-service}

If you have requested to be a part of our Early Adopter program, Adobe's product team will enable RUM Data monitoring for you. Once this is completed, Adobe's product team will reach out to you to provide you with the domain key and data dashboard URL for you to view the Page View and [The Core Web Vitals(CWB)](https://web.dev/vitals/) metrics through the support collaboration channel created by Adobe's Product team. 

## Viewing the Traffic and Performance Metrics for Your Website {#viewing-the-traffic-and-performance-metrics-for-your-website}

A Slack channel would be created for Early Adopter customers to provide them with the initial support for sharing the data desk dashboard url to access the Page Views and Core Web Vital metrics. 

To access the data desk dashboard url, customers will need a domain key which will be created by Adobe and it will be provided to them in the Slack collaboration channel. 

You will then be guided on how to use the domain key to access the data dashboard link and view the metrics.

## How RUM Data is Being Used {#how-rum-data-is-being-used}

Adobe uses RUM data for the following purposes:

* To identify and fix performance bottlenecks for customer sites
* To estimate the number of page views for customer sites
* To understand how Adobe Experience Manager interacts with other scripts (such as analytics, targeting, or external libraries) on the same page, in order to increase compatibility.

## Limitations and Understanding Variance in Page Views and Performance Metrics {#limitations-and-understanding-variance-in-page-views-and-performance-metrics}

As you will analyze this data, there might or might not be variances in page views and other performance metrics reported by Real User Monitoring (RUM). These variances can be attributed to several factors inherent in real-time, client-side monitoring. Here are key considerations for customers to keep in mind when interpreting their RUM data:

1. **Tracker blockers**

   * End-users employing tracker blockers or privacy extensions can impede RUM's data collection, as these tools restrict the tracking scripts' execution. This restriction can lead to underreported page views and user interactions, creating a discrepancy between actual site activity and the data captured by RUM.

1. **Limitations in capturing API/JSON calls**

   * RUM data service focuses on the client-side experience and doesn't capture the backend API or JSON calls at this time. The exclusion of these calls from RUM data will create variances from the content requests measured by CDN Analytics.

## FAQ {#faq}

1. **How can I opt-out?**

   Customers who want to opt-out of the RUM monitoring bundle can reach out to Adobe Support.

1. **How can I configure paths to include or exclude in monitoring?**

   Customers will be able to configure paths to include or exclude the URLs for monitoring by setting the Environment variables within the configuration in Cloud Manager by using these variables: `AEM_WEBVITALS_EXCLUDE` and `AEM_WEBVITALS_INCLUDE_PATHS`
   
   Please note that by default, the 'include' setting is configured to target '/content'. It's important to remember that the paths you need to configure here are content paths within the system, not the URL paths you see in your browser. This distinction is key for accurately setting up and customizing your configuration to meet your specific needs.

1. **Would Adobe be able to track all the page views prior to them reaching the customer managed CDN?**

   Yes.

1. **Will customers be able to integrat the RUM data service scripts with third-party systems like Dynatrace?**

   Yes.
1. **Are “Interaction to next paint”, “Time to first byte” and “First contentful paint” Web vitals Metrics being collected?**

   Interaction to next paint (INP) and Time to first byte (TTFB) are collected.  First contentful paint is not collected at this time.
