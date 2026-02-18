---
title: Cache Management in Dynamic Media with Open APIs
description: Cache Management in Dynamic Media with Open APIs
role: User
exl-id: 203a5291-edb5-4900-8b0a-32e1ebae5395
---
# Cache Management in Dynamic Media with Open APIs {#cache-management-dynamic-media-open-apis}

Effective cache management is essential for delivering high-performance, scalable, and up-to-date digital assets. In Dynamic Media with Open APIs, cache management defines how content is stored, refreshed, and delivered across the various layers of the delivery pipeline. Asset delivery responses are cached at multiple layers to ensure optimal performance and fast content delivery.

Prolonged caching in Dynamic Media with Open APIs consists of [CDN Layer Caching](#cdn-layer-caching) and [External Cache Control (BYOCDN & Browser Caching)](#byocdn-browser-caching).

## CDN Layer Caching {#cdn-layer-caching}

Asset delivery responses are cached at [Adobe Managed CDN](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/cdn#aem-managed-cdn) for an extended period to maximize performance and minimize load on the origin. This caching is fully managed by Adobe to ensure a consistently high-quality experience for end users. The cache duration is intentionally optimized for performance and cannot be customized by users to maintain reliability and efficient content delivery across all customers.

All delivery URLs are cached at the edge (Fastly) for an extended duration to ensure optimal performance. The cached delivery objects include static renditions, videos, original image binaries, and dynamically transformed images such as resized or reformatted assets generated through URL parameters. <!--The CDN is designed to serve these assets directly from the cache without revalidating them, unless an explicit purge is performed.-->

## External Cache Control (BYOCDN & Browser Caching) {#byocdn-browser-caching}

Asset delivery responses include a `Cache-Control` header with a default `max-age` of **10 minutes** for downstream caching layers. This applies to custom *Bring-Your-Own-CDN (BYOCDN) configurations*, *end-user browsers*, and any *intermediate caching proxies*, ensuring consistent cache control across the entire delivery path.

### Customizing Cache Control Headers {#customizing-cache-control-headers}

Increasing cache time to live values beyond the default configuration increases the likelihood of serving stale content, which can delay the visibility of content updates in the end-user experience. If you need to modify the cache control behavior for your specific use case, you can configure custom CDN rules to adjust response headers. This allows you to set different cache durations based on your requirements. Refer to [AEM Custom CDN Rules for Response Headers](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/cdn-configuring-traffic).

```
responseTransformations:
    rules:
      - name: cache-asset-delivery
        when:
          allOf:
            - reqProperty: path
              like: '/adobe/assets/urn:aaid:aem:*'
            - reqProperty: tier
              equals: delivery
        actions:
          - type: set
            respHeader: Cache-Control
            value: max-age=300
```

For additional assistance or questions about cache management, contact [Adobe Support](https://helpx.adobe.com/in/contact.html).

## Active Cache Invalidation {#active-cache-invalidation}

Whenever an asset is updated, deleted, or modified (any metadata changes), Dynamic Media with Open APIs automatically invalidates every associated delivery URL on Adobe Managed CDN. This applies to URLs that use vanity IDs or aliases, along with any URLs that include transformation parameters, such as width, format, or quality. This event-driven invalidation ensures that your users always receive the most current version of your assets without manual intervention.

### Manual Cache Purging {#manual-cache-purging}

When there is a need to manually purge cached content, you can do so using AEM's cache invalidation capabilities. For detailed instructions on how to purge specific cache URLs, refer to [AEM CDN Cache Invalidation](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/cdn-cache-purge#single-purge).

## Frequently asked questions{#faq-cache-management}

+++**How does cache management affect existing integrations?**

Asset URLs remain unchanged, and the cache control header sent to browsers (and other downstream intermediaries) from Adobe Managed CDN continues to be 10-minutes with a [`stale-while-revalidate directive`](https://web.dev/articles/stale-while-revalidate#whats_it_mean), ensuring that downstream systems continue to leverage their caches optimally.

+++

+++**What triggers a cache purge?**

The cache purge triggers automatically when an asset is updated, modified, archived, or deleted.

<!--The cache purge triggers automatically in the following circumstances:
 
 - when an asset is updated, modified, or archived.
 - when an asset reaches `ready_for_delivery` state after approval.-->

+++

<!--
+++ **How long does it take for the cache to refresh after updating an asset?**

Any time the asset changes, the cache refreshes usually in *less than 60 seconds*.

+++

<!--
+++ **What happens if the cache purge system fails?**
The following mechanisms can be followed:
 
 - **Automatic retries:** 3 retry attempts with exponential backoff
 - **Monitoring:** Sev-2 alert fires if staleness exceeds 10 minutes
 - **Natural expiry:** Even without purge, cache expires after 10 hours maximum
 - **Manual override:** Engineers can manually purge via CLI tool

+++
-->

+++ **What all asset types are supported for long lived caching?**

The prolonged caching with event driven active cache invalidation is applicable to all types of assets in the Dynamic Media with Open APIs, regardless of the asset type or format.

+++

+++ **Can I opt-out of long-lived caching for my repository?**

To opt out of prolonged caching, contact [Adobe Support](https://helpx.adobe.com/in/contact.html) and provide the rationale for your request.

+++


>[!MORELIKETHIS]
>
>- [Integrate Asset Selector with various applications](/help/assets/integrate-asset-selector.md)
>- [Vanity URLs](/help/assets/vanity-urls.md)
