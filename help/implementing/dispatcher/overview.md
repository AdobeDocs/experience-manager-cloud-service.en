---
title: Content Delivery Flow Overview
description: Content Delivery Flow Overview
exl-id: fe42fb9e-cdf4-43e1-b688-7cecf4124fa5
---
# Content Delivery Flow {#content-delivery}

The current page details publish service content delivery in AEM as a Cloud Service. Publish service content delivery includes:

* CDN
* AEM dispatcher
* AEM publish

The data flow is as follows:

1. The URL is added in the browser
1. Request made to CDN mapped in DNS to that domain
1. If content is fully cached on CDN, CDN serves it to the browser
1. If content is not fully cached, the CDN calls out (reverse proxy) to the dispatcher
1. If content is fully cached on dispatcher, dispatcher serves it to the CDN
1. If content is not fully cached, the dispatcher calls out (reverse proxy) to the AEM publish
1. The content is rendered by the browser, which may also cache it, depending on the headers

By default, the content type HTML/text is set to expire after 300s (5 minutes) at the dispatcher layer, a threshold which both the dispatcher cache and CDN respect. During redeployments of the publish service, the dispatcher cache is cleared and subsequently warmed up before the new publish nodes accept traffic.

The sections below provide greater detail about content delivery, including CDN configuration and caching. 

Information about replication from the author service to the publish service is available [here](/help/operations/replication.md).
