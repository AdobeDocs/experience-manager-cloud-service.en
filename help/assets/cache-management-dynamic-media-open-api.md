---
title: Cache Management in Dynamic Media Open API
description: Cache Management in Dynamic Media Open API
role: User

---
# Cache Management in Dynamic Media Open API {#cache-management-dynamic-media-open-apis}

Effective cache management is essential for delivering high-performance, scalable, and up-to-date digital assets. In Dynamic Media Open APIs, cache management defines how content is stored, refreshed, and delivered across the various layers of the delivery pipeline. Asset delivery responses are cached at multiple layers to ensure optimal performance and fast content delivery.

## 1. CDN Layer Caching {#cdn-layer-caching}

Asset delivery responses are cached at Adobe's CDN layers for an extended period to maximize performance and minimize load on the origin. This caching is fully managed by Adobe to ensure a consistently high-quality experience for end users. The cache duration is intentionally optimized for performance and cannot be customized by users to maintain reliability and efficient content delivery across all customers.

All delivery URLs are cached at the edge (Fastly) for an extended duration to ensure optimal performance. The cached delivery objects include static renditions, videos, original image binaries, and dynamically transformed images such as resized or reformatted assets generated through URL parameters. The CDN is designed to serve these assets directly from the cache without revalidating them, unless an explicit purge is performed.

## 2. Active Cache Invalidation {#active-cache}

Whenever an asset is updated, deleted, or modified (any metadata changes), the CDN automatically invalidates every associated delivery URL. This applies to URLs that use vanity IDs or aliases, along with any URLs that include transformation parameters, such as width, format, or quality. This event-driven invalidation ensures that your users always receive the most current version of your assets without manual intervention.

### Manual Cache Purging {#manual-cache-purging}

When there is a need to manually purge cached content, you can do so using AEM's cache invalidation capabilities. For detailed instructions on how to purge specific cache URLs, refer to [AEM Dispatcher Cache Invalidation](https://experienceleague.adobe.com/en/docs/experience-manager-dispatcher/using/configuring/page-invalidate).

## 3. External Cache Control (BYOCDN & Browser Caching) {#bycdn-browser-caching}

Asset delivery responses include a `Cache-Control` header with a default `max-age` of **10 minutes** for downstream caching layers. This applies to custom *Bring-Your-Own-CDN (BYOCDN) configurations*, *end-user browsers*, and any *intermediate caching proxies*, ensuring consistent cache control across the entire delivery path.

### Customizing Cache Control Headers

If you need to modify the cache control behavior for your specific use case, you can configure custom CDN rules to adjust response headers. This allows you to set different cache durations based on your requirements. Refer to [AEM Custom CDN Rules for Response Headers](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/cdn-configuring-traffic).

```
responseTransformations:
    rules:
      - name: cache-asset-delivery
        when:
          allOf:
            - reqProperty: path
              like: '/adobe/assets/urn:aaid:aem:*'
        actions:
          - type: set
            respHeader: Cache-Control
            value: max-age=300
```

For additional assistance or questions about cache management, please contact [Adobe Support](https://helpx.adobe.com/in/contact.html).

## Frequently asked questions{#faq-cache-management}

+++**How does cache management affect existing integrations?**

Asset URLs remain unchanged, and the Cache-Control header sent to browsers and AEMCS Fastly continues to use a 10-minute duration, ensuring that downstream systems and behaviors remain unaffected.

+++

+++**What triggers a cache purge?**
  
The cache purge triggers automatically in the following circumstances:
 
 - when an asset is updated, modified, or archived.
 - when an asset reaches `ready_for_delivery` state after approval.

+++

+++ **How long does it take for the cache to refresh after updating an asset?**

The overall time is *<60 seconds*.

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

The long lived caching is applicable to all types of assets in the Dynamic Media Open API, regardless of the asset type or format.

+++

+++ **Can I opt-out of long-lived caching for my repository?**

You can contact [Adobe Support](https://helpx.adobe.com/in/contact.html) to add your repository in the denylist.

+++



>[!MORELIKETHIS]
>
>- [Integrate Asset Selector with various applications](/help/assets/integrate-asset-selector.md)
