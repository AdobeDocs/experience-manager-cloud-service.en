---
title: CDN configuration snippets for common scenarios
description: Copy-ready YAML patterns for the Adobe-managed CDN and customer-managed CDN setups, including edge authentication, redirects, cache variation, traffic shaping, and rate limits.
feature: Dispatcher
exl-id: 7c4e2a91-3d8f-41b2-9c0e-8f1a2b3c4d5e
role: Admin
---

# CDN configuration snippets for common scenarios {#cdn-configuration-snippets}

This article collects practical `cdn.yaml` patterns for AEM as a Cloud Service. Use them together with the feature documentation for [CDN traffic rules](/help/implementing/dispatcher/cdn-configuring-traffic.md), [customer-managed CDN credentials](/help/implementing/dispatcher/cdn-credentials-authentication.md), and [traffic filter rules including WAF](/help/security/traffic-filter-rules-including-waf.md). Deploy snippets with a Cloud Manager [config pipeline](/help/operations/config-pipeline.md).

>[!NOTE]
>
>Replace host names, paths, IP ranges, keys, and thresholds with values that match your program. Test changes in a non-production environment before promoting them.

## Customer-managed CDN (BYOCDN) {#customer-managed-cdn}

These examples assume you already declared an `edge` authenticator (see [Customer-managed CDN HTTP header value](/help/implementing/dispatcher/cdn-credentials-authentication.md#CDN-HTTP-value)) and reference its name in each rule.

### Require `X-AEM-Edge-Key` only for selected hostnames {#edge-auth-selected-hosts}

**Goal:** Enforce edge authentication for traffic that presents a specific site hostname in `X-Forwarded-Host`, while leaving other hostnames on the publish tier unchanged (for example, during a gradual rollout or when a hostname bypasses the customer CDN).

**Approach:** Match the first hostname from `X-Forwarded-Host` using the `forwardedDomain` request property, and run the `authenticate` action only when it equals your target hostname.

```yaml
kind: "CDN"
version: "1"
data:
  authentication:
    authenticators:
      - name: edge-auth
        type: edge
        edgeKey1: ${{CDN_EDGEKEY_PRIMARY}}
        edgeKey2: ${{CDN_EDGEKEY_SECONDARY}}
    rules:
      - name: edge-auth-selected-host
        when:
          allOf:
            - { reqProperty: tier, equals: "publish" }
            - { reqProperty: forwardedDomain, equals: "www.example.com" }
        action:
          type: authenticate
          authenticator: edge-auth
```

For safer cutovers, you can temporarily add an extra header or path condition as described under [Migrating safely](/help/implementing/dispatcher/cdn-credentials-authentication.md#migrating-safely).

### Require `X-AEM-Edge-Key` except for trusted client IP ranges {#edge-auth-trusted-ips}

**Goal:** Allow designated networks (for example, monitoring tools or a corporate egress range) to reach the Adobe CDN publish hostname without presenting `X-AEM-Edge-Key`, while still requiring the header for the general internet.

**Approach:** Authenticate publish traffic only when the client IP is **not** in your allow list using the `notIn` predicate described in the [Traffic Filter Rules condition structure](/help/security/traffic-filter-rules-including-waf.md#condition-structure).

```yaml
kind: "CDN"
version: "1"
data:
  authentication:
    authenticators:
      - name: edge-auth
        type: edge
        edgeKey1: ${{CDN_EDGEKEY_PRIMARY}}
        edgeKey2: ${{CDN_EDGEKEY_SECONDARY}}
    rules:
      - name: edge-auth-outside-trusted-cidrs
        when:
          allOf:
            - { reqProperty: tier, equals: "publish" }
            - reqProperty: clientIp
              notIn:
                - "203.0.113.0/24"
                - "198.51.100.14/32"
        action:
          type: authenticate
          authenticator: edge-auth
```

Ensure the customer CDN forwards accurate `X-Forwarded-For` values so `clientIp` reflects the real end user, as described in [Customer CDN points to AEM managed CDN](/help/implementing/dispatcher/cdn.md#point-to-point-cdn).

## Redirects and URL normalization {#redirects}

Patterns use [server-side redirects](/help/implementing/dispatcher/cdn-configuring-traffic.md#server-side-redirectors).

### Apex domain to `www` {#apex-to-www}

Send visitors from `example.com` to `https://www.example.com`, preserving path and query string:

```yaml
kind: "CDN"
version: "1"
data:
  redirects:
    rules:
      - name: apex-to-www
        when: { reqProperty: domain, equals: "example.com" }
        action:
          type: redirect
          status: 301
          location:
            reqProperty: url
            transform:
              - op: replace
                match: '^https?://example\.com(.*)$'
                replacement: 'https://www.example.com\1'
```

### Remove a trailing slash from the path {#trailing-slash}

Normalize `https://www.example.com/path/` to `https://www.example.com/path`:

```yaml
kind: "CDN"
version: "1"
data:
  redirects:
    rules:
      - name: strip-trailing-slash
        when:
          reqProperty: path
          matches: '^/.+/$'
        action:
          type: redirect
          status: 301
          location:
            reqProperty: url
            transform:
              - op: replace
                match: '/$'
                replacement: ''
```

## Influence caching through the URL {#cache-key}

The CDN cache key includes the URL the edge receives. If you must segment cache entries without changing AEM content, add (or normalize) a query parameter with a [request transformation](/help/implementing/dispatcher/cdn-configuring-traffic.md#request-transformations):

```yaml
kind: "CDN"
version: "1"
data:
  requestTransformations:
    rules:
      - name: add-cache-variation-param
        when:
          reqProperty: path
          like: /content/experience-fragments/*
        actions:
          - type: set
            queryParam: af_segment
            value: mobile
```

Prefer tuning `Cache-Control` headers from AEM or Dispatcher when possible; use this pattern when a CDN-only variation is required.

## Read values from a structured cookie {#json-cookie}

When a cookie stores JSON, copy a field into a request header for logging or downstream use by chaining `set` and `transform` actions on `reqCookie`:

```yaml
kind: "CDN"
version: "1"
data:
  requestTransformations:
    rules:
      - name: extract-user-from-session-cookie
        when:
          reqProperty: path
          like: /api/*
        actions:
          - type: set
            var: session_json
            value:
              reqCookie: session
          - type: transform
            var: session_json
            op: replace
            match: '^.*"userId"\s*:\s*"([^"]+)".*$'
            replacement: '\1'
          - type: set
            reqHeader: x-user-id-from-cookie
            value:
              var: session_json
```

Validate the regular expression against real cookie values; escape characters as needed.

## Cross-origin (CORS) traffic {#cross-origin}

Browsers may issue `OPTIONS` preflight requests before cross-origin `POST` or custom-header calls. Typical steps:

1. Confirm traffic filter rules do not block `OPTIONS` for the affected paths.
2. Add [response transformations](/help/implementing/dispatcher/cdn-configuring-traffic.md#response-transformations) that set `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`, and related headers when `reqProperty: method` equals `OPTIONS` or when your API responses require CORS headers.

Because AEM often participates in the preflight response body, validate the full browser flow against stage before production rollout. Dispatcher-focused CORS samples are also available for self-hosted publish stacks in [Dispatcher caching and CORS](/help/headless/deployment/dispatcher-caching.md).

## Traffic filters and rate limits {#traffic-filters}

### Rate limit by autonomous system (ASN) {#rate-limit-asn}

Distributed attacks can generate low volumes per IP, which makes per-IP counters less effective. Aggregate instead by autonomous system name using `clientAsName` (see [request properties](/help/security/traffic-filter-rules-including-waf.md#condition-structure)) inside `groupBy`:

```yaml
kind: "CDN"
version: "1"
data:
  trafficFilters:
    rules:
      - name: rate-limit-by-asn
        when:
          reqProperty: tier
          equals: "publish"
        rateLimit:
          limit: 400
          window: 10
          penalty: 300
          count: all
          groupBy:
            - reqProperty: clientAsName
        action: block
```

>[!CAUTION]
>
>Many users can share the same autonomous system (for example, a large ISP or a shared corporate egress). Monitor CDN logs after enabling ASN-based limits to ensure legitimate audiences are not affected.

## See also {#see-also}

* [CDN in AEM as a Cloud Service](/help/implementing/dispatcher/cdn.md)
* [Configuring traffic at the CDN](/help/implementing/dispatcher/cdn-configuring-traffic.md)
* [CDN credentials and authentication](/help/implementing/dispatcher/cdn-credentials-authentication.md)
* [Traffic filter rules including WAF](/help/security/traffic-filter-rules-including-waf.md)
