---
title: Understanding Cloud Service Content Requests
description: If you have purchased content request licenses from Adobe, learn about the types of content requests that Adobe Experience Cloud as a Service measures and the variances with an organization's analytics reporting tools.
exl-id: 3666328a-79a7-4dd7-b952-38bb60f0967d
---
# Cloud Service Content Requests

## Introduction {#introduction}

Cloud Service content requests are measured via server-side collection of data. The collection is enabled via CDN log analysis.

>[!NOTE]
>We are excited to announce the GA rollout (Link to Release Notes) for client-side collection enabled via Real Use Monitoring service measurement. With the gA rollout, Adobe will start monitoring client-side traffic for it's customers automatically and there is no customer set up required. You can learn more by consulting the documentation in [this article](#real-user-monitoring-for-aem-as-a-cloud-service).

## Understanding Cloud Service Content Requests {#understaing-cloud-service-content-requests}

Content requests are automatically collected server-side at the edge of Adobe Experience Manager as a Cloud Service, via automated analysis of the log files originating from the AEM as a Cloud Service CDN. This is done by isolating the requests returning HTML `(text/html)` or JSON `(application /Json)` content from the CDN, and based on several inclusion and exclusion rules detailed below. A content request occurs independently from the returned content being served from the CDN caches or the content going back to the origin of the CDN (AEM's dispatchers).

The Real Use Monitoring service , the client-side collection, offers a more precise reflection of user interactions, ensuring a reliable measure of website engagement. This gives customers advanced insights into their page traffic and performance. While this is beneficial for both customers who use either the Adobe managed CDN or a non-Adobe managed CDN. In addition, automatic traffic reporting can now be enabled for customers using a non-Adobe managed CDN, thus removing the need to share any traffic reports with Adobe.

For customers that bring their own CDN on top of AEM as a Cloud Service, server-side reporting will result in numbers that cannot be used to compare with the licensed content requests. These numbers will have to be measured by the customer at the edge of the outer CDN. For these customers, client-side reporting and associated performance, the [Adobe RUM Data Service](#real-user-monitoring-for-aem-as-a-cloud-service) is the Adobe recommended option. See the [release notes](/help/release-notes/release-notes-cloud/release-notes-current.md#sites-early-adopter) for the information on how to opt-in.

## Server-side Collection {#serverside-collection}

There are rules in place to exclude well-known bots, including well-known services visiting the site regularly to refresh their search index or service.

### Variances of Cloud Service Content Requests {#content-requests-variances}

Content Requests can have variances with an organization's Analytics reporting tools as summarized in the following table. In general, *do not* use analytics tools that gather data by way of client-side instrumentation to report on the number of content requests for a given site, simply because they often depend on user consent to be triggered, therefore missing out on a significant fraction of the traffic. Analytics tools gathering data server-side in log files, or CDN reports for customers adding their own CDN on top of AEM as a Cloud Service, will provide better counts. For reporting on Page Views and their associated performance, the Adobe RUM Data Service is the Adobe recommended option. 

|Reason For Variance|Explanation|
|---|---|
|End user consent|Analytics tools relying on client-side instrumention often depend on user consent to be triggered. This could represent the majority of the traffic not being tracked. For customers who want to measure content requests on their own, it is recommended to rely on analytics tools gathering data server-side or CDN reports.|
|Tagging|All pages or API calls that are tracked as Adobe Experience Manager (AEM) content requests may not be tagged with Analytics tracking.|
|Tag Management Rules|Tag management rule settings may result in various data collection configurations on a page, resulting in some combination of discrepancies with content request tracking.|
|Bots|Unknown bots that have not been pre-identified and removed by AEM may cause tracking discrepancies.|
|Report Suites|Pages that are part of the same AEM instance and domain may send data to different Analytics report suites.|
|Third-Party Monitoring and Security Tools|Monitoring and security scanning tools may generate content requests for AEM that are not tracked in Analytics reports.|
|API Access|Programmatic access to pages or to Adobe Experience Manager APIs may generate content requests for AEM that are not tracked in Analytics reports.|
|Prefetch Requests|Using a prefetch service to pre-load pages to increase speed can cause significant content request traffic increases.|
|DDOS|While Adobe makes attempts to automatically detect and filter out traffic from DDOS attacks, there is no guarantee that all possible DDOS attacks are detected.|
|Traffic Blockers|Using a tracker blocker in a browser may opt out some requests from being tracked.|
|Firewalls|Firewalls may block Analytics tracking. This scenario is more frequent with corporate firewalls.|

See also [License Dashboard](/help/implementing/cloud-manager/license-dashboard.md).

### Types of included content requests {#included-content-requests}

| Request Type | Content Request | Description |
| --- | --- | --- |
| HTTP Code 100-299 | Included | These are regular requests that deliver all or partial content. |
| HTTP libraries for automation | Included | Examples:<br>&bull; Amazon CloudFront<br>&bull; Apache Http Client<br>&bull; Asynchronous Http Client<br>&bull; Axios<br>&bull; Azureus<br>&bull; Curl<br>&bull; GitHub Node Fetch<br>&bull; Guzzle<br>&bull; Go-http-client<br>&bull; Headless Chrome<br>&bull; Java&trade; Client<br>&bull; Jersey<br>&bull; Node Oembed<br>&bull; okhttp<br>&bull; Python Requests<br>&bull; Reactor Netty<br>&bull; Wget<br>&bull; WinHTTP|
| Monitoring and Health Check tools | Included | These are set up by the customer to monitor a certain aspect of the site. For example, availability or real-world user performance. Use `/system/probes/health` endpoint and not the actual HTML pages from the site.<br>Examples:<br>&bull; Amazon-Route53-Health-Check-Service<br>&bull; EyeMonIT_bot_version_0.1_[(https://www.eyemon.it/)](https://www.eyemon.it/)<br>&bull; Investis-Site24x7<br>&bull; Mozilla/5.0+(compatible; UptimeRobot/2.0; [https://uptimerobot.com/](https://uptimerobot.com/))<br>&bull; ThousandEyes-Dragonfly-x1<br>&bull; OmtrBot/1.0<br>&bull; WebMon/2.0.0|
| `<link rel="prefetch">` requests | Included | To increase the speed of loading the next page, customers can have the browser load a set of pages before the user clicks the link&mdash;so they are already in the cache. *Mind: This is increasing the traffic significantly*&mdash;depending on how many of these pages are prefetched.|
| Traffic that blocks Adobe Analytics or Google Analytics reporting | Included | It is more common that visitors of sites have privacy software installed (Ad-blockers, and so on) that impact the accuracy of Google Analytics or Adobe Analytics. AEM as a Cloud Service counts requests on the first entry-point into the Adobe operated infrastructure and not the client-side.|

See also [License Dashboard](/help/implementing/cloud-manager/license-dashboard.md).

### Types of excluded content requests {#excluded-content-request}

| Request Type | Content Request | Description |
| --- | --- | --- |
| HTTP Code 500+ | Excluded | Errors returned to the visitor when something goes wrong on AEM as a Cloud Service or the customer custom code.|
| HTTP Code 400-499 | Excluded | Errors returned to the visitor when the content does not exist (404) or there are other content or request-related issues.|
| HTTP Code 300-399 | Excluded | These are good requests that either check if something has changed on the server, or redirect the request to another resource. They do not contain content itself, therefore they are not billable.|
| Requests going to /libs/* | Excluded | AEM internal JSON requests, such as the CSRF token that is not billable.|
| Traffic from DDOS attacks | Excluded | DDOS protection. AEM does auto-detect some of the DDOS attacks and blocks them. DDOS attacks if detected are not billable. |
| AEM as a Cloud Service NewRelic Monitoring | Excluded | AEM as a Cloud Service global monitoring.|
| URL for customers to monitor their Cloud Service program | Excluded | Recommended URL to externally monitor the availability.<br><br>`/system/probes/health`|
| AEM as a Cloud Service Pod Warm-up Service | Excluded | 
Agent: skyline-service-warmup/1.*|
| Well-known search engines, social networks, and HTTP libraries (tagged by Fastly) | Excluded | Well-known services visiting the site regularly to refresh their search index or service:<br><br>Examples:<br>&bull; AddSearchBot<br>&bull; AhrefsBot<br>&bull; Applebot<br>&bull; Ask Jeeves Corporate Spider<br>&bull; Bingbot<br>&bull; BingPreview<br>&bull; BLEXBot<br>&bull; BuiltWith<br>&bull; Bytespider<br>&bull; CrawlerKengo<br>&bull; Facebookexternalhit<br>&bull; Google AdsBot<br>&bull; Google AdsBot Mobile<br>&bull; Googlebot<br>&bull; Googlebot Mobile<br>&bull; lmspider<br>&bull; LucidWorks<br>&bull; MJ12bot<br>&bull; Pingdom<br>&bull; Pinterest<br>&bull; SemrushBot<br>&bull; SiteImprove<br>&bull; StashBot<br>&bull; StatusCake<br>&bull; YandexBot|
| Exclude Commerce Integration Framework calls | Excluded | These are requests made to AEM that get forwarded to the Commerce Integration Framework&mdash;the URL starts with `/api/graphql`&mdash;to avoid double counting, they are not billable for Cloud Service.|
| Exclude `manifest.json` | Excluded | Manifest is not an API call, it is here to provide information on how to install web sites on desktop or mobile phone. Adobe should not count JSON request to `/etc.clientlibs/*/manifest.json`|
| Exclude `favicon.ico` | Excluded | While the returned content should not be HTML or JSON, we are observing that in some scenarios like SAML authentication flows, favicons can be returned as HTML therefore are explicitly excluded from the count.|

## Client-side Collection {#cliendside-collection}

### Real Use Monitoring Service for AEM as a Cloud Service {#real-use-monitoring-service-for-aem-as-a-cloud-service}

>[!INFO]
>
>This feature is only available to the early adopter program. 
>You need to be using AEM Cloud Service version **2023.11.14227** and above in order to enabled the RUM data service.

### Overview {#overview}

The Real Use Monitoring service is a type of performance monitoring technology that captures and analyzes the digital user experiences of a website or application in real-time. It provides visibility into the real-time performance of a web application and provides deeper insight into the end-user experience. 

With Real Use Monitoring , key performance metrics are tracked right from the initiation of the URL until the request is served back to the browser all of which helps the developers enhance the application to make it easy to use for the end users. 

### Who Can Benefit from Real Use Monitoring Service? {#who-can-benefit-from-rum-service}

RUM Data Service is beneficial for all customers whether utilising Adobe's, or their own CDN. It offers a representative reflection of user interactions, ensuring a reliable measure of website engagement by capturing the number of Page Views on the client-side. 

In particular, for Adobe CDN users,  this service provides valuable insights into user interactions, helping to identify if your CDN setup or implementation may be resulting in a higher number of content requests compared to server-side logs.

For customers employing their own CDN they can benefit from simplified traffic reporting, as Adobe now directly integrates these Page Views, eliminating the need for separate reports during renewal cycles. 

Would you like to unlock the full potential of your website , then ask us for providing you access to our Early Adopter version of RUM Explorer platform! This cutting-edge tool can provide unparalleled insights into your page performance, including detailed metrics on the number of clicks, Core Web Vitals (CWV), conversions, and comprehensive customer journey maps. Discover where your traffic is coming from—whether it's referrals, search engines, or direct visits—and understand your audience better with data on user agents, including bots, desktops, and mobile devices. By utilizing these powerful insights, you can fine-tune your digital experiences to meet your users' needs more effectively. Don't miss out on this opportunity to elevate your web performance. Interested in learning more? Reach out to us at email  "aemcs-rum-adopter@adobe.com" today and start optimizing your digital strategy!

### Understand how the Real Use Monitoring Service Works {#understand-how-the-rum-service-works}

Adobe Experience Manager uses Real Use Monitoring (RUM) to help customers and Adobe understand, how visitors are interacting with Adobe Experience Manager-powered sites, to diagnose performance issues, and to measure the effectiveness of experiments. RUM preserves the privacy of visitors through sampling - only a small portion of all page views will be monitored - and judicious exclusion of all personally identifiable information (PII). 

### Real Use Monitoring Service and Privacy {#rum-service-and-privacy}

The Real Use Monitoring service in Adobe Experience Manager is designed to preserve visitor privacy and minimize data collection. As a visitor, this means that no personal information will be collected by the site you are visiting or made available to Adobe. 

As a site operator, this means no additional opt-in is required to enable monitoring through this feature.So, there will be no additional pop up for the end users to accept for enabling RUM monitoring. 

### Real Use Monitoring Service Data Sampling {#rum-service-data-sampling}

Traditional web analytics solutions try to collect data on every single visitor. Adobe Experience Manager's Real Use Monitoring service only captures information from a small fraction of page views. The Real Use Monitoring service data is meant to be sampled and anonymized rather than a replacement for analytics. By default, pages will have a 1:100 sampling ratio. Site operators cannot configure this number to increase or decrease the sampling rate as of today. To estimate total traffic accurately,for every 100 page views, we gather detailed data from one, giving you a reliable approximation of overall traffic."

As the decision of whether the data will be collected is made on a page view by page view basis, it becomes virtually impossible to track interactions across multiple pages. RUM has no concept of visits, visitors, or sessions, only of page views. This is by design.

### What Data is Being Collected {#what-data-is-being-collected}

The Real Use Monitoring service is designed to prevent the collection of personally identifiable information. The full set of information that can be collected by Adobe Experience Manager's Real Use Monitoring service is listed below:

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

### How Real Use Monitoring Works for a customer

We are pleased to introduce Real Use Monitoring, a service that automatically monitors client-side traffic to provide you with valuable insights. As an Adobe customer, you don’t need to take any additional steps—this service is seamlessly integrated into your existing setup. With the General Availability (GA) rollout, you will automatically benefit from this new feature. If you wish to leverage more insights with this new feature to optimize your digital experiences effortlessly, please see here (link to Row 99).

### How Real Use Monitoring Service Data is Being Used {#how-rum-service-data-is-being-used}

RUM data is beneficial for the following purposes:

* To identify and fix performance bottlenecks for customer sites
* Streamlined, automatic traffic reporting that includes Page Views for customers using their own CDN, which means they do not have to share any traffic report with Adobe during their renewal cycles and we have got you covered.
* To understand how Adobe Experience Manager interacts with other scripts (such as analytics, targeting, or external libraries) on the same page, in order to increase compatibility.

### Limitations and Understanding Variance in Page Views and Performance Metrics {#limitations-and-understanding-variance-in-page-views-and-performance-metrics}

As you will analyze this data, there might or might not be variances in page views and other performance metrics reported by Real User Monitoring (RUM). These variances can be attributed to several factors inherent in real-time, client-side monitoring. Here are key considerations for customers to keep in mind when interpreting their RUM data:

1. **Tracker blockers**

   * End-users employing tracker blockers or privacy extensions can impede Real User Monitoring service's data collection, as these tools restrict the tracking scripts' execution. This restriction can lead to underreported page views and user interactions, creating a discrepancy between actual site activity and the data captured by RUM.

1. **Limitations in capturing API/JSON calls**

   * RUM data service focuses on the client-side experience and doesn't capture the backend API or JSON calls at this time. The exclusion of these calls from Real User Monitoring service data will create variances from the content requests measured by CDN Analytics.

### FAQ {#faq}

1. **How can I opt-out?**

We highly recommend using the Real Use Monitoring (RUM)  due to its significant benefits and that it can allow you to optimize your digital experiences. It can offers valuable insights that can help improve website performance and increase conversions. The service is designed to be seamless and has no impact on your website’s performance.

Opting out means missing out on these powerful insights. However, if you encounter any issues, our support team is here to help. 

1. **Would Adobe be able to track all the page views before the interaction reaches the customer managed CDN or at the point when the interaction reaches the customer managed CDN?**

   Yes.

1. **Will customers be able to integrate the RUM data service scripts with third-party systems like Dynatrace?**

   Yes.

1. **Are "Interaction to next paint", "Time to first byte" and "First contentful paint" Web vitals Metrics being collected?**

   Interaction to next paint (INP) and Time to first byte (TTFB) are collected.  First contentful paint is not collected at this time.
