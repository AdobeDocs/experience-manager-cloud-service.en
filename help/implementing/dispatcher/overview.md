---
title: Content Delivery Flow Overview
description: Learn more about the content delivery data flow and how to publish your content
exl-id: fe42fb9e-cdf4-43e1-b688-7cecf4124fa5
feature: Dispatcher
role: Admin
---
# Content Delivery Flow {#content-delivery}

The current page details publish service content delivery in AEM as a Cloud Service. Publish service content delivery includes:

* CDN
* AEM Dispatcher
* AEM publisher

The data flow is as follows:

1. The URL is added in the browser
1. Request made to CDN mapped in DNS to that domain
1. If content is fully cached on CDN, CDN serves it to the browser
1. If content is not fully cached, the CDN calls out (reverse proxy) to the Dispatcher
1. If content is fully cached on Dispatcher, Dispatcher serves it to the CDN
1. If content is not fully cached, the Dispatcher calls out (reverse proxy) to the AEM publish
1. The content is rendered by the browser, which may also cache it, depending on the headers

By default, the content type HTML/text is set to expire after 300 seconds (5 minutes) at the Dispatcher layer, a threshold which both the Dispatcher cache and CDN respect. During redeployments of the publish service, the Dispatcher cache is cleared and then warmed up before the new publish nodes accept traffic.

The following sections provide greater detail about content delivery:
* [CDN configuration](/help/implementing/dispatcher/cdn.md)
* [Caching](/help/implementing/dispatcher/caching.md)

For information about replication from the author service to the publish service see [Replication](/help/operations/replication.md).
