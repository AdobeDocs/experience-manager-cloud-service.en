---
title: Edge Side Includes
description: The Adobe Managed CDN now supports Edge Side Includes (ESI), a markup language for edge level dynamic web content assembly.
feature: Dispatcher
---
# Edge Side Includes {#edge-side-includes}

>[!NOTE]
>This feature is not yet generally available. To join the early-adopter program, email `aemcs-cdn-config-adopter@adobe.com` and describe your use case.

Content delivery speed benefits from caching pages aggressively, achieved through setting cache headers with high time to live (TTL) values. This can be challenging when pages include dynamic content, which needs to be either frequently refreshed or potentially cannot be cached at all. Fortunately, there are strategies where the containing HTML page can be cached with a high TTL, deferring the fetch of the more dynamic content snippets to a later time, either through client-side Javascript or at the CDN. The latter approach is a standard called Edge Side Includes (ESI). The HTML includes ESI tags instructing the CDN to defer the serving of the page to the browser until it evaluates those tags, retrieving additional, more dynamic (lower TTL) content from the origin (or CDN cache if its TTL hasn't expired).

## ESI syntax {#esi-syntax}

The ESI syntax is as follows: if a parent page `/parent-pages/page.html` includes `parent-pages-containing-esi-tags/page.html`.

## Apache Configuration {#esi-apache}

Pages with ESI tags should declare the following properties in the apache configuration:

```
<LocationMatch "/parent-pages/*">
   # disable dispatcher compression
   SetEnv no-gzip 1
   # enable esi processing
   Header set x-aem-esi "on"
   # enable edge compression
   Header set x-aem-compress "on"
</LocationMatch>

```

The configured properties have the following behavior:

| Property  | Behavior |
|-----------|--------------------------|
| **no-gzip** |If set to 1, the parent HTML page is transmitted from apache to the CDN uncompressed. Content must be sent to the CDN uncompressed since the CDN must be able to see and evaluate the ESI tags. This setting overrides whatever compression setting apache might have otherwise used, based on the request's Accept-Encoding values.|
| **x-aem-esi** |If set to "on", the CDN will evaluate the parent HTML page's ESI tags.|
| **x-aem-compress** |If set to "on", Fastly will compress the content sent to the browser. Since the transmission of the parent page from apache to CDN must be uncompressed for ESI to work (no-gzip set to 1), this can reduce latency.|
