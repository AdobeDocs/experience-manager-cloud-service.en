---
title: Purging the CDN cache
description: Learn how to remove cached objects from the Adobe CDN cache by configuring the purge API Token which can then be used in API calls.
feature: Dispatcher
---
# Purging the CDN cache {#cdn-purge-cache}

>[!NOTE]
>This feature is not yet generally available. To join the early-adopter program, email `aemcs-cdn-config-adopter@adobe.com`.

Purging removes an object from the Adobe CDN cache, prompting future requests that would otherwise hit that cached object to proceed to origin as a cache miss.
AEM as a Cloud Service allows you to configure a Purge API Token, which can then be used in API calls. See link TBD  to learn how to configure this token by using the Cloud Manager Configuration Pipeline Authentication directives.

There are three supported purging variations:

* [Single URL purge](#single-purge) - purge a single resource at a time.
* [Purge by surrogate key](#surrogate-key-purge) - purge multiple resources at one time.
* [Full purge](#full-purge) - purge all resources.

All purging variations share the following:

* The HTTP method must be set to `PURGE`.
* The URL can be any domain associated with the AEM service that the purge request is intended for.
* The `X-AEM-Purge-Key` must be provided in a HTTP header.

## Single URL purge {#single-purge}

You can purge a single resource at a time as follows:

```
curl
-X PURGE "https://publish-p1234-e5467.adobeaemcloud.com/resource-path" \
-H 'X-AEM-Purge-Key: <my_purge_key>' \
-H 'X-AEM-Purge: soft' #optional
```

As shown in the example above, you can **optionally** specify if the CDN should perform a hard purge (default) or a soft purge on the cached objects. The default is a hard purge, which makes the content immediately inaccessible to new requests until the content is retrieved from the origin. This can be configured to be a soft purge,which marks content as stale, but it is still served to clients so they do not need to wait until the content is retrieved from the origin.

## Surrogate key purge {#surrogate-key-purge}

Surrogate keys are unique identifiers that you use to purge a set of content. They are applied to content by adding a `Surrogate-Key` header to the response. One or more surrogate keys can be referenced in a purge API call.  

```
curl
-X PURGE "https://publish-p1234-e5467.adobeaemcloud.com" \
-H 'X-AEM-Purge-Key: <my_purge_key>' \
-H "Surrogate-Key: my-surrogate-key"
-H "X-AEM-Purge: soft" #optional
```

The `Surrogate-Key`(s) are separated by space. Similarly to the single URL purge, you can configure either a hard or a soft purge.

## Full purge {#full-purge}

You can perform a full purge of all cached resources as follows:

```
curl
-X PURGE "https://publish-p1234-e5467.adobeaemcloud.com" \
-H 'X-AEM-Purge-Key: <my_purge_key>' \
-H "X-AEM-Purge: all"
```

Be aware that the `X-AEM-Purge` header must include the 'all' value.
