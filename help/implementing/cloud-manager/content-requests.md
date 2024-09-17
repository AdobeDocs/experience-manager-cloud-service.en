---
title: Understanding Cloud Service Content Requests
description: If you have purchased content request licenses from Adobe, learn about the types of content requests that Adobe Experience Cloud as a Service measures and the variances with an organization's analytics reporting tools.
exl-id: 3666328a-79a7-4dd7-b952-38bb60f0967d
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---
# Cloud Service Content Requests

## Introduction {#introduction}

Content requests are requests coming into AEM Sites (including in connection with Edge Delivery Services for AEM Sites) or any customer-provided caching system (like a Content Delivery Network) to deliver content or data in either HTML format via page views (for example, pages and experience fragments) or JSON format via API calls (in a headless manner). Content requests are counted either as a page view or 5 API Calls, and are measured at the ingress of the first caching system to receive a content request. Certain HTTP requests are included or excluded for purposes of counting content requests. The full list of such included and excluded HTTP requests, as well as their technical definitions, are available in the documentation.

## Understanding Cloud Service Content Requests {#understanding-cloud-service-content-requests}

For customers using the out-of-the-box CDN, Cloud Service content requests are measured via server-side collection of data. This collection is enabled via CDN log analysis. Content requests are automatically collected server-side at the edge of Adobe Experience Manager as a Cloud Service, via automated analysis of the log files originating from AEM as a Cloud Service CDN. This is done by isolating the requests returning HTML `(text/html)` or JSON `(application/json)` content from the CDN, and is based on several inclusion and exclusion rules detailed below. A content request occurs independently from the returned content being served from the CDN caches or the content going back to the origin of the CDN (AEM's dispatchers).

<!-- REMOVED AS PER EMAIL REQUEST FROM SHWETA DUA, JULY 30, 2024 TO RICK BROUGH AND ALEXANDRU SARCHIZ   For customers employing their own CDN, client-side collection offers a more precise reflection of interactions, ensuring a reliable measure of website engagement via the [Real Use Monitoring](/help/sites-cloud/administering/real-use-monitoring-for-aem-as-a-cloud-service.md) service. This gives customers advanced insights into their page traffic and performance. While it is beneficial for all customers, it offers a representative reflection of user interactions, ensuring a reliable measure of website engagement by capturing the number of page views from the client side. 

For customers that bring their own CDN on top of AEM as a Cloud Service, server-side reporting results in numbers that cannot be used to compare with the licensed content requests. With the [Real Use Monitoring](/help/sites-cloud/administering/real-use-monitoring-for-aem-as-a-cloud-service.md), Adobe can reflect a reliable measure of website engagement. --> 

### Variances of Cloud Service Content Requests {#content-requests-variances}

Content Requests can have variances within an organization's Analytics reporting tools as summarized in the following table. In general, *do not* use analytics tools that gather data by way of client-side instrumentation to report on the number of content requests for a given site, simply because they often depend on user consent to be triggered, therefore missing a significant fraction of the traffic. Analytics tools gathering data server-side in log files, or CDN reports for customers adding their own CDN on top of AEM as a Cloud Service, will provide better counts. 

|Reason For Variance|Explanation|
|---|---|
|End user consent|Analytics tools relying on client-side instrumentation often depend on user consent to be triggered. This could represent the majority of the traffic not being tracked. For customers who want to measure content requests on their own, it is recommended to rely on analytics tools gathering data server-side or CDN reports.|
|Tagging|All pages or API calls that are tracked as Adobe Experience Manager content requests may not be tagged with Analytics tracking.|
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

## Server-side Collection Rules {#serverside-collection}

There are rules in place to exclude well-known bots, including well-known services visiting the site regularly to refresh their search index or service.

### Types of included content requests {#included-content-requests}

| Request Type | Content Request | Description |
| --- | --- | --- |
| HTTP Code 100-299 | Included | These are regular requests that deliver all or partial content. |
| HTTP libraries for automation | Included | Examples:<br>&bull; Amazon CloudFront<br>&bull; Apache Http Client<br>&bull; Asynchronous Http Client<br>&bull; Axios<br>&bull; Azureus<br>&bull; Curl<br>&bull; GitHub Node Fetch<br>&bull; Guzzle<br>&bull; Go-http-client<br>&bull; Headless Chrome<br>&bull; Java&trade; Client<br>&bull; Jersey<br>&bull; Node Oembed<br>&bull; okhttp<br>&bull; Python Requests<br>&bull; Reactor Netty<br>&bull; Wget<br>&bull; WinHTTP<br>&bull; Fast HTTP<br>&bull; GitHub Node Fetch<br>&bull; Reactor Netty|
| Monitoring and Health Check tools | Included | These are set up by the customer to monitor a certain aspect of the site. For example, availability or real-world user performance.If these are targeting specific endpoints like /system/probes/health for health checks, we recommend that you use `/system/probes/health` endpoint and not the actual HTML pages from the site.[See below](#excluded-content-request)<br>Examples:<br>&bull; Amazon-Route53-Health-Check-Service<br>&bull; EyeMonIT_bot_version_0.1_[(https://www.eyemon.it/)](https://www.eyemon.it/)<br>&bull; Investis-Site24x7<br>&bull; Mozilla/5.0+(compatible; UptimeRobot/2.0; [https://uptimerobot.com/](https://uptimerobot.com/))<br>&bull; ThousandEyes-Dragonfly-x1<br>&bull; OmtrBot/1.0<br>&bull; WebMon/2.0.0|
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
| AEM as a Cloud Service New Relic Monitoring | Excluded | AEM as a Cloud Service global monitoring.|
| URL for customers to monitor their Cloud Service program | Excluded | We recommended to use URL to externally monitor the availability or health check.<br><br>`/system/probes/health`|
| AEM as a Cloud Service Pod Warm-up Service | Excluded | 
Agent: skyline-service-warmup/1.*|
| Well-known search engines, social networks, and HTTP libraries (tagged by Fastly) | Excluded | Well-known services visiting the site regularly to refresh their search index or service:<br><br>Examples:<br>&bull; AddSearchBot<br>&bull; AhrefsBot<br>&bull; Applebot<br>&bull; Ask Jeeves Corporate Spider<br>&bull; Bingbot<br>&bull; BingPreview<br>&bull; BLEXBot<br>&bull; BuiltWith<br>&bull; Bytespider<br>&bull; CrawlerKengo<br>&bull; Facebookexternalhit<br>&bull; Google AdsBot<br>&bull; Google AdsBot Mobile<br>&bull; Googlebot<br>&bull; Googlebot Mobile<br>&bull; lmspider<br>&bull; LucidWorks<br>&bull; MJ12bot<br>&bull; Pinterest<br>&bull; SemrushBot<br>&bull; SiteImprove<br>&bull; StashBot<br>&bull; StatusCake<br>&bull; YandexBot<br>&bull; Claudebot|
| Exclude Commerce Integration Framework calls | Excluded | These are requests made to AEM that get forwarded to the Commerce Integration Framework&mdash;the URL starts with `/api/graphql`&mdash;to avoid double counting, they are not billable for Cloud Service.|
| Exclude `manifest.json` | Excluded | Manifest is not an API call, it is here to provide information on how to install web sites on desktop or mobile phone. Adobe should not count JSON request to `/etc.clientlibs/*/manifest.json`|
| Exclude `favicon.ico` | Excluded | While the returned content should not be HTML or JSON, we are observing that in some scenarios like SAML authentication flows, favicons can be returned as HTML therefore are explicitly excluded from the count.|
| CDN proxy to a different backend | Excluded | Requests routed to different non-AEM backends using the CDN Origin Selectors(https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/cdn-configuring-traffic#origin-selectors) technique are excluded as they do not hit AEM.|
