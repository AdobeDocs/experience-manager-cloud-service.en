---
title: Edge Side Includes
description: The Adobe Managed CDN now supports Edge Side Includes (ESI), a markup language for edge level dynamic web content assembly.
feature: Dispatcher
exl-id: 35093477-2788-4f69-80a9-899f43567cae
role: Admin
---
# Edge Side Includes {#edge-side-includes}

Content delivery speed benefits from caching pages aggressively, achieved through setting cache headers with high time to live (TTL) values. This can be challenging when pages include dynamic content, which needs to be either frequently refreshed or potentially cannot be cached at all. Fortunately, there are strategies where the containing HTML page can be cached with a high TTL, deferring the fetch of the more dynamic content snippets to a later time, either through client-side Javascript or at the CDN. The latter approach is a standard called Edge Side Includes (ESI), which is supported for sites rendered with AEM publishing. The HTML includes ESI tags instructing the CDN to defer the serving of the page to the browser until it evaluates those tags, retrieving additional, more dynamic (lower TTL) content from the origin (or CDN cache if its TTL hasn't expired).

Some use cases where Edge Side Includes may be useful:

* Displaying an end user's name, or other information that is unique to an end user.
* Displaying a list of recent information, such as news articles or stock prices.

## ESI syntax {#esi-syntax}

The ESI syntax is as follows, if a parent page `/content/page.html` includes a snippet `content/snippets/mysnippet.html`.

```
<html>
  <head>
      <title>My Site</title>
  </head>
  <body>
    <div id="content">
      <esi:include src="/content/snippets/mysnippet.html" />
    </div>
  </body>
</html>

```

See the [ESI specification](https://www.w3.org/TR/esi-lang/) for details.

### Considerations {#esi-syntax-considerations}

* The following ESI tags are supported: include, comment, remove.
* ESI tags are processed at the CDN sequentially rather than concurrently, so many ESI tags on a page with low TTLs can add latency to the end user's experience.
* The maximum depth of ESI: include processing is 5.
* The maximum total ESI: include processing fragments is 256.


## Apache Configuration {#esi-apache}

If you have pages with ESI tags you should declare the following properties in the Apache configuration:

```
<LocationMatch "/parent-pages/*content/page.html">
   # disable dispatcher compression
   SetEnv no-gzip 1
   # enable esi processing 
   Header set x-aem-esi "on"
   # enable edgeCDN compression
   Header set x-aem-compress "on"

   # typically the main page is cached at the CDN
   Header always set Cache-Control "max-age=300"
 </LocationMatch>


<LocationMatch "/content/snippets/mysnippet.html">
  SetEnv no-gzip 1

  # typically the included page is either set to a lower TTL than the parent page, or not cached at all, as these 2 commented declarations show, respectively:
  #Header always set Cache-Control "no-cache"
  #Header always set Cache-Control "max-age=50"
 </LocationMatch> 

```

The configured properties have the following behavior:

| Property  | Behavior |
|-----------|--------------------------|
| **no-gzip** |If set to 1, the HTML page is transmitted from apache to the CDN uncompressed. This is necessary for ESI since content must be sent to CDN uncompressed so the CDN can see and evaluate the ESI tags.<br/><br/>Both the parent page and the included snippets should set no-gzip to 1.<br/><br/>This setting overrides whatever compression setting Apache might have otherwise used, based on the request's `Accept-Encoding` values.|
| **x-aem-esi** |If set to "on", the CDN will evaluate the parent HTML page's ESI tags.  By default, the header is not set.|
| **x-aem-compress** |If set to "on", the CDN will compress the content from the CDN to the browser. Since the transmission of the parent page from apache to CDN must be uncompressed for ESI to work (`no-gzip` set to 1), this can reduce latency.<br/><br/>If this header is not set, when the CDN retrieves content from the origin uncompressed, it would serve content to the client uncompressed, as well. Thus, it is necessary to set this header if `no-gzip` is set to 1 (required for ESI) and it is desired to serve content compressed from the CDN to the browser.|

## Sling Dynamic Include {#esi-sdi}

While not required, [Sling Dynamic Include](https://sling.apache.org/documentation/bundles/dynamic-includes.html) (SDI) can be used to generate ESI snippets that are interpreted at the CDN.
