---
title: Caching in AEM Edge Functions
description: Learn how the CDN cache and Edge Function fetch cache interact, how to configure caching behavior, and how to purge cached content across both layers.
feature: Developing, Edge Delivery Services
role: Developer
---
# Caching in AEM Edge Functions {#edge-functions-caching}

>[!IMPORTANT]
>
>AEM Edge Functions is a **beta** feature. Features and documentation may change without notice. To join the early access program and provide feedback, email [aemcs-edgecompute-feedback@adobe.com](mailto:aemcs-edgecompute-feedback@adobe.com).

This page provides detailed technical guidance on how caching works within AEM Edge Functions, including the two-cache architecture, how to control caching behavior in your code, and how to purge cache entries when content changes.

For general background on how AEM as a Cloud Service caching works, see [Caching in AEM as a Cloud Service](/help/implementing/dispatcher/caching.md) and [The CDN in AEM as a Cloud Service](/help/implementing/dispatcher/cdn.md). For code examples, refer to the [AEM Edge Functions Boilerplate — Caching](https://github.com/adobe/aem-edge-functions-boilerplate/blob/main/README.md#caching).

## Caching Architecture {#architecture}

AEM Edge Functions sit between the CDN and the backend services that the function fetches from. These backends can be AEM publish instances, third-party APIs, external databases, or any HTTP endpoint your code calls. There are **two distinct caches** in the request flow, each operating independently:

```
Browser → AEM CDN (CDN Cache) → AEM Edge Functions (Fetch Cache) → Backend (AEM, APIs, etc.)
```

| Cache | What it caches | Influenced by | How to purge |
|---|---|---|---|
| **CDN Cache** | The Edge Function's response to the browser | Response headers set by the Edge Function (`Cache-Control`, `Surrogate-Control`, `Surrogate-Key`) | [CDN Cache Purge API](/help/implementing/dispatcher/cdn-cache-purge.md) |
| **Edge Function Fetch Cache** | Backend responses to `fetch()` calls within the Edge Function, and data stored via the Core Cache API | Backend response headers, `CacheOverride` on fetch calls, or programmatic surrogate keys via Core Cache API | `aio aem edge-functions purge-cache` CLI command or `purgeSurrogateKey()` |

Understanding this two-layer architecture is essential because each cache has a different scope, different controls, and a different purge mechanism. Effective caching requires deliberate configuration at both levels.

## CDN Cache (Outer) {#cdn-cache}

The CDN cache sits between the browser and the Edge Function. It caches the Edge Function's **response**. You control its behavior by setting standard HTTP cache headers on your Edge Function responses:

```js
return new Response(body, {
  headers: {
    'Surrogate-Key': 'page-home product-123',
    'Cache-Control': 'public, max-age=3600'
  }
});
```

Multiple surrogate keys are separated by spaces. These surrogate keys can be used to purge the CDN cache using the [CDN Cache Purge API](/help/implementing/dispatcher/cdn-cache-purge.md). The concept of surrogate key purging is the same as described in [Purge the cache for a group of resources](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/caching/how-to/purge-cache#purge-the-cache-for-a-group-of-resources) — the key difference is that the CDN surrogate keys here are set by your Edge Function code rather than by the backend.

## Edge Function Fetch Cache (Inner) {#fetch-cache}

The Edge Function fetch cache sits between the Edge Function and the backends it calls. It caches the **backend's response** to `fetch()` calls made within your Edge Function code. It also holds any data your code stores via the [**Core Cache API**](https://js-compute-reference-docs.edgecompute.app/docs/fastly:cache/CoreCache/insert) or [**Simple Cache API**](https://js-compute-reference-docs.edgecompute.app/docs/fastly:cache/SimpleCache) — programmatic caching interfaces that give you fine-grained control over what gets cached, for how long, and under which surrogate keys.

It is **not** influenced by headers you set on the Edge Function's outgoing response — only by the backend's response headers, by [`CacheOverride`](https://js-compute-reference-docs.edgecompute.app/docs/fastly:cache-override/CacheOverride/) options on your fetch calls, or by surrogate keys you assign programmatically when writing to the Core Cache API.

>[!NOTE]
>
>The `Surrogate-Key` header you set on your Edge Function's *outgoing response* to the browser controls the **outer CDN cache**, not this inner cache. Surrogate keys for the inner cache come from the backend's `Surrogate-Key` response header or from keys you assign when writing to the Core Cache API.

### Caching Backend Responses {#cache-override}

To cache backend responses for a specific duration:

```js
import { CacheOverride } from "fastly:cache-override";

const response = await fetch(request, {
  backend: "my-origin",
  cacheOverride: new CacheOverride({ ttl: 300 })
});
```

### Bypassing the Cache {#cache-pass}

To bypass the fetch cache entirely and always fetch from the backend, use `pass` mode:

```js
import { CacheOverride } from "fastly:cache-override";

const response = await fetch(request, {
  backend: "my-origin",
  cacheOverride: new CacheOverride({ mode: "pass" })
});
```

## Cache Purging {#cache-purging}

When cached content becomes stale, you need to explicitly purge it. Because the two caches operate independently, it is important to understand which layer you're invalidating and how they interact.

### Coordinating Purges Across Both Layers {#coordinating-purges}

Because the Edge Function sits behind the CDN as a backend (reachable through [origin selectors](/help/implementing/dispatcher/cdn-configuring-traffic.md#origin-selectors)), purging one cache layer without the other can produce unexpected results:

1. **Purging only the CDN cache** causes the next request to invoke the Edge Function. If the Edge Function's fetch cache still holds stale data, it returns old content — which the CDN then caches again.
2. **Purging only the Edge Function cache** clears internal state, but the CDN continues serving its previously cached copy until it expires or is separately purged.

**Best practice:** When underlying data changes, purge **both** caches — use the CDN Cache Purge API for the outer layer and `purge-cache` (or `purgeSurrogateKey()`) for the inner Edge Function layer. Using consistent surrogate keys across both layers simplifies coordinated invalidation. For a complete example of this pattern, see the [AEM Edge Functions Boilerplate — Purging](https://github.com/adobe/aem-edge-functions-boilerplate/blob/main/README.md#purging-the-edge-function-fetch-cache).

### Purging the CDN Cache {#purge-cdn-cache}

To purge the outer CDN cache (the Edge Function's response cached at the CDN layer), use the [CDN Cache Purge API](/help/implementing/dispatcher/cdn-cache-purge.md). This is the same purge mechanism used for all AEM as a Cloud Service content cached at the CDN — see [How to purge the CDN cache](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/caching/how-to/purge-cache) for step-by-step guidance.

In the AEM as a Cloud Service architecture, Edge Functions receive traffic from the CDN via [origin selectors](/help/implementing/dispatcher/cdn-configuring-traffic.md#origin-selectors) (see also [CDN Routing](/help/implementing/developing/introduction/edge-functions.md#cdn-routing)). The complete request flow is:

```
Client → AEM CDN (VCL) → Origin Selector → Edge Function → Backend
```

The CDN caches the final response returned by the Edge Function. A CDN purge clears **only** that outer cached response — it has no effect on the Edge Function's internal caches.

### Purging the Edge Function Fetch Cache {#purge-fetch-cache}

The `purge-cache` CLI command purges the **Edge Function fetch cache** (the backend responses cached within the Edge Function). It does **not** purge the outer CDN cache. For full CLI options and flags, see the [`purge-cache` command reference](https://github.com/adobe/aio-cli-plugin-aem-edge-functions/blob/main/README.md#purge-cache).

#### Where Surrogate Keys Come From {#surrogate-key-origin}

Surrogate keys used in purge commands must match the keys that were **tagged on the cached content at the time it was stored**. This is the same concept as [surrogate key–based purging](/help/implementing/dispatcher/cdn-cache-purge.md#surrogate-key-purge) used in the AEM CDN, but applied to the Edge Function's internal cache. These keys come from:

- The `Surrogate-Key` response header that the backend returns when the Edge Function fetches from it.
- Keys you assign programmatically when writing to the [Core Cache API](https://js-compute-reference-docs.edgecompute.app/docs/fastly:cache/CoreCache/insert) (e.g., via the `surrogateKeys` option when inserting a cache entry).

For example, if your backend responds with:

```
HTTP/1.1 200 OK
Content-Type: text/html
Surrogate-Key: page-about product-456 category-shoes
Cache-Control: public, max-age=3600
```

Then the cached response is tagged with three surrogate keys: `page-about`, `product-456`, and `category-shoes`. You can later purge it using any of those keys:

```bash
# Purge all cached content tagged with "product-456"
aio aem edge-functions purge-cache <function-name> --surrogateKey product-456

# Purge multiple keys at once
aio aem edge-functions purge-cache <function-name> -k page-about -k category-shoes
```

>[!TIP]
>
>Choose surrogate key naming conventions that map to your content model — for example, by page path (`page-about`), content ID (`product-456`), or content type (`category-shoes`). This makes targeted cache invalidation intuitive when content changes.

#### Purge All {#purge-all}

```bash
# Purge all cached content (use with caution)
aio aem edge-functions purge-cache <function-name> --all
```

#### Soft Purge {#soft-purge}

Use the `--soft` flag to perform a soft purge, which retains stale entries in the cache and reduces backend load while enabling stale revalidation:

```bash
aio aem edge-functions purge-cache <function-name> --surrogateKey product-456 --soft
```

#### Programmatic Purge {#programmatic-purge}

You can also purge surrogate keys programmatically from within your Edge Function code using [`purgeSurrogateKey`](https://js-compute-reference-docs.edgecompute.app/docs/fastly:compute/purgeSurrogateKey):

```js
import { purgeSurrogateKey } from "fastly:compute";

// Hard purge (immediate removal)
purgeSurrogateKey("product-456");

// Soft purge (retain stale entries for revalidation)
purgeSurrogateKey("product-456", true);
```

>[!CAUTION]
>
>Purging all cached content increases traffic to backends. Use the `--all` flag carefully and prefer targeted surrogate key purges where possible.