---
title: Understanding Content Requests
description: If you have purchased content request licenses from Adobe, learn about the types of content requests that Adobe Experience Cloud as a Service measures.

---
# Understanding Content Requests {#about-content-request}

Content requests are tracked on Adobe Experience Manager (AEM) as a Cloud Service's Edge servers. Origin traffic does not count towards content requests. The CDN built into AEM as a Cloud Service tracks valid HTML and JSON requests.

AEM also has rules in place to exclude well-known bots, including well-known services visiting the site regularly to refresh their search index or service.

See also [License Dashboard](/help/implementing/cloud-manager/license-dashboard.md). 

## Types of excluded content requests{#excluded-content-request}

| Request Type | Content Request | Description |
| --- | --- | --- |
| HTTP Code 500+ | Excluded | Errors returned to the visitor when something goes wrong on AEM as a Cloud Service or the customer custom code.|
| HTTP Code 400-499 | Excluded | Errors returned to the visitor when the content does not exist (404) or there are other content or request-related issues.|
| HTTP Code 300-399 | Excluded | These are good requests that either check if something has changed on the server, or redirect the request to another resource. They do not contain content itself, therefore they are not billable.|
| Requests going to /libs/* | Excluded | AEM internal JSON requests, such as the CSRF token that is not billable.|
| Traffic from DDOS attacks | Excluded | DDOS protection. AEM does auto-detect some of the DDOS attacks and blocks them. DDOS attacks if detected are not billable.<br><br>Auto-detected DDOS types:<br>&bull; DDOSBlockedCiphersSHA<br>&bull; DDOSBlockedPattern<br>&bull; DDOSSuspiciousRequest |
| AEM as a Cloud Service NewRelic Monitoring | Excluded | AEM as a Cloud Service global monitoring.<br><br>User Agent: Mozilla/5.0 (X11; Linux&reg; x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/*|
| URL for customers to monitor their Cloud Service program | Excluded | Recommended URL to externally monitor the availability.<br><br>`/system/probes/health`|
| AEM as a Cloud Service Pod Warm-up Service | Excluded | User Agent: skyline-service-warmup/1.4|
| Well-known search engines, social networks, and HTTP libraries (tagged by Fastly) | Excluded | Well-known services visiting the site regularly to refresh their search index or service:<br><br>Examples:<br>&bull; AddSearchBot<br>&bull; AhrefsBot<br>&bull; Applebot<br>&bull; Ask Jeeves Corporate Spider<br>&bull; Bingbot<br>&bull; BingPreview<br>&bull; BLEXBot<br>&bull; BuiltWith<br>&bull; Bytespider<br>&bull; CrawlerKengo<br>&bull; Facebookexternalhit<br>&bull; Google AdsBot<br>&bull; Google AdsBot Mobile<br>&bull; Googlebot<br>&bull; Googlebot Mobile<br>&bull; lmspider<br>&bull; LucidWorks<br>&bull; MJ12bot<br>&bull; Pingdom<br>&bull; Pinterest<br>&bull; SemrushBot<br>&bull; SiteImprove<br>&bull; StashBot<br>&bull; StatusCake<br>&bull; YandexBot|
| Exclude Commerce Integration Framework calls | Excluded | These are requests made to AEM that get forwarded to the Commerce Integration Framework&mdash;the URL starts with `/api/graphql`&mdash;to avoid double counting, they are not billable for Cloud Service.|
| Exclude `manifest.json` | Excluded | Manifest is not an API call, it is here to provide information on how to install web sites on desktop or mobile phone. Adobe should not count JSON request to `/etc.clientlibs/*/manifest.json`|
| Exclude `favicon.ico` | Excluded | For customers with SAML auth, the favicon request made by browsers is delivered as HTML and counted as a content request. Filtering out `favicon.ico` is recommended.|

## Types of included content requests{#included-content-requests}

| Request Type | Content Request | Description |
| --- | --- | --- |
| Exclude HTML done by way of fetch or XHR | Included | This is under consideration and is still being evaluated if it should be included. |
| HTTP Code 100-299 | Included | These are regular requests that deliver all or partial content |
| HTTP libraries for automation | Included | Examples:<br>&bull; Amazon CloudFront<br>&bull; Apache Http Client<br>&bull; Asynchronous Http Client<br>&bull; Axios<br>&bull; Azureus<br>&bull; Curl<br>&bull; GitHub Node Fetch<br>&bull; Guzzle<br>&bull; Go-http-client<br>&bull; Headless Chrome<br>&bull; Java&trade; Client<br>&bull; Jersey<br>&bull; Node Oembed<br>&bull; okhttp<br>&bull; Python Requests<br>&bull; Reactor Netty<br>&bull; Wget<br>&bull; WinHTTP|
| Monitoring and Health Check tools | Included | These are set up by the customer to monitor a certain aspect of the site. For example, availability or real-world user performance. Use `/system/probes/health` endpoint and not the actual HTML pages from the site.<br>Examples:<br>&bull; Amazon-Route53-Health-Check-Service<br>&bull; EyeMonIT_bot_version_0.1_[(https://www.eyemon.it/)](https://www.eyemon.it/)<br>&bull; Investis-Site24x7<br>&bull; Mozilla/5.0+(compatible; UptimeRobot/2.0; [https://uptimerobot.com/](https://uptimerobot.com/))<br>&bull; ThousandEyes-Dragonfly-x1<br>&bull; OmtrBot/1.0<br>&bull; WebMon/2.0.0|
| `<link rel="prefetch">` requests | Included | To increase the speed of loading the next page, customers can have the browser load a set of pages before the user clicks the link&mdash;so they are already in the cache. *Mind: This is increasing the traffic significantly*&mdash;depending on how many of these pages are prefetched.|
| Traffic that blocks Adobe Analytics or Google Analytics reporting | Included | It is more common that visitors of sites have privacy software installed (Ad-blockers, and so on) that impact the accuracy of Google Analytics or Adobe Analytics. AEM as a Cloud Service counts requests on the first entry-point into the Adobe operated infrastructure and not the client-side.|


