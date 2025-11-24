---
title: Cache Management in Dynamic Media Open API
description: Cache Management in Dynamic Media Open API
role: User

---
# Cache Management in Dynamic Media Open API {#cache-management-dynamic-media-open-apis}

<<<<<<< Updated upstream
Asset delivery responses are cached at multiple layers to ensure optimal performance and fast content delivery. This document outlines the caching strategy and how you can manage cache behavior for your assets.

## 1. Adobe CDN Layer Caching

Asset delivery responses are cached at Adobe's CDN layer(s) for an extended period to optimize performance and reduce origin load. This caching is managed internally by Adobe to ensure the best experience for your users.

**Important Notes:**

- The cache duration is optimized for performance and is not user-configurable
- Adobe manages this layer to ensure reliability and optimal content delivery across all customers

## 2. Active Cache Invalidation

Adobe automatically invalidates cached content when assets are modified or updated. This event-driven invalidation ensures that your users always receive the most current version of your assets without manual intervention.

### Manual Cache Purging

If you need to manually purge cached content, you can do so using AEM's cache invalidation capabilities. For detailed instructions on how to purge specific cache URLs, please refer to the official AEM documentation:
W**Reference:** [AEM Dispatcher Cache Invalidation](https://experienceleague.adobe.com/docs/experience-manager-dispatcher/using/configuring/page-invalidate.html)

## 3. External Cache Control (BYOCDN & Browser Caching)

Asset delivery responses include a `Cache-Control` header with a default `max-age` of **10 minutes** for downstream caching layers. This applies to:

- Custom Bring-Your-Own-CDN (BYOCDN) configurations
- End-user browsers
- Any intermediate caching proxies

### Customizing Cache Control Headers

If you need to modify the cache control behavior for your specific use case, you can configure custom CDN rules to adjust response headers. This allows you to set different cache durations based on your requirements.
**Reference:** [AEM Custom CDN Rules for Response Headers](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/content-delivery/cdn-configuring-traffic.html#response-headers)

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

## Summary

| Layer | Cache Behavior | Customer Control |
|-------|---------------|------------------|
| Adobe CDN | Extended caching, internally managed | Not configurable |
| Active Invalidation | Event-driven, automatic on asset changes | Manual purge available via AEM |
| External Layers (BYOCDN/Browsers) | 10-minute default max-age | Configurable via CDN rules |
---
For additional assistance or questions about cache management, please contact Adobe Support.
=======

>>>>>>> Stashed changes

>[!MORELIKETHIS]
>
>* [Integrate Asset Selector with various applications](/help/assets/integrate-asset-selector.md)
