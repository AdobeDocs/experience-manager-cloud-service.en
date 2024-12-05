---
title: Purging the CDN cache
description: Learn how to remove cached objects from the Adobe CDN cache by configuring the purge API Token which can then be used in API calls.
feature: CDN Cache
exl-id: 4d091677-b817-4aeb-b131-7a5407ace3e0
role: Admin
---
# Purging the CDN cache {#cdn-purge-cache}

Purging removes an object from the Adobe CDN cache, resulting in future requests proceeding to the origin as a cache miss, rather than being served from cache.
AEM as a Cloud Service allows you to configure a Purge API Token, which can then be used in Purge API calls. Read [Configuring CDN Credentials and Authentication](/help/implementing/dispatcher/cdn-credentials-authentication.md#purge-API-token) to learn how to configure this token using the Cloud Manager Config Pipeline Authentication directives.

There are three supported purging variations:

* [Single URL purge](#single-purge) - purge a single resource at a time.
* [Purge by surrogate key](#surrogate-key-purge) - purge multiple resources at one time.
* [Full purge](#full-purge) - purge all resources.

All purge variations share the following:

* The HTTP method must be set to `PURGE`.
* The URL can be any domain associated with the AEM service that the purge request is intended for.
* The `X-AEM-Purge-Key` must be provided in a HTTP header.

>[!CAUTION]
>Purging the CDN cache, especially with the hard flag, will increase traffic at the origin and could lead to an outage when not executed properly.

You may reference [a tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/caching/how-to/purge-cache) focused on configuring purge keys and performing the CDN cache purge.

## Single URL purge {#single-purge}

You can purge a single resource at a time as follows:

```
curl
-X PURGE "https://publish-p1234-e5467.adobeaemcloud.com/resource-path" \
-H 'X-AEM-Purge-Key: <my_purge_key>' \
-H 'X-AEM-Purge: soft'
```

As shown in the example above, you can **optionally** specify if the CDN should perform a **hard** purge (default) or a **soft** purge on the cached objects.

The default hard purge makes the content immediately inaccessible to new requests until the content is retrieved from the origin. Soft purge marks content as stale, but still serves it to clients so they do not need to wait until the content is retrieved from the origin.

## Surrogate key purge {#surrogate-key-purge}

Surrogate keys are unique identifiers that you use to purge a set of content. They are applied to content by adding a `Surrogate-Key` header to the response. One or more surrogate keys can be referenced in a purge API call.  

```
curl
-X PURGE "https://publish-p1234-e5467.adobeaemcloud.com" \
-H 'X-AEM-Purge-Key: <my_purge_key>' \
-H "Surrogate-Key: my-surrogate-key"
-H "X-AEM-Purge: soft" #optional
```

The `Surrogate-Key`(s) are separated by spaces. Similarly to the single URL purge, you can configure either a hard or a soft purge.

## Full purge {#full-purge}

You can perform a full purge of all cached resources as follows:

```
curl
-X PURGE "https://publish-p1234-e5467.adobeaemcloud.com" \
-H 'X-AEM-Purge-Key: <my_purge_key>' \
-H "X-AEM-Purge: all"
```

Be aware that the `X-AEM-Purge` header must include the 'all' value.

## Interaction with Customer Managed CDN

In case of a [Customer Managed CDN](/help/implementing/dispatcher/cdn.md#point-to-point-CDN) also the `X-Forwarded-Host` and `X-AEM-Edge-Key` need to be provided:

```
curl
-X PURGE "https://publish-p1234-e5467.adobeaemcloud.com/resource-path" \
-H 'X-AEM-Purge-Key: <my_purge_key>' \
-H 'X-AEM-Edge-Key: <my_edge_key>' \
-H 'X-Forwarded-Host: <my_forwarded_domain>'
```


## Interactions with Apache/Dispatcher layer {#apache-layer}

As described under [Content Delivery Flow](/help/implementing/dispatcher/overview.md), the CDN retrieves content from the Apache/Dispatcher layer, if the cache has expired. This implies that before purging a resource at the CDN, you should ensure that a fresh version of the content is also available at the Dispatcher. For further details also see [Dispatcher Cache Invalidation](/help/implementing/dispatcher/caching.md#disp).
