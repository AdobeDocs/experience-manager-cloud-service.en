---
title: CDN Configuration Snippets for Common Scenarios
description: Copy-ready YAML patterns for the Adobe-managed CDN and customer-managed CDN setups, including edge authentication, redirects, cache variation, traffic shaping, and rate limits.
feature: Dispatcher
role: Admin
---

# CDN Configuration Snippets for Common Scenarios {#cdn-configuration-snippets}

This article collects practical `cdn.yaml` patterns for AEM as a Cloud Service. Use them together with the feature documentation for [CDN traffic rules](/help/implementing/dispatcher/cdn-configuring-traffic.md), [customer-managed CDN credentials](/help/implementing/dispatcher/cdn-credentials-authentication.md), and [traffic filter rules including WAF](/help/security/traffic-filter-rules-including-waf.md). Deploy snippets with a Cloud Manager [config pipeline](/help/operations/config-pipeline.md).

>[!NOTE]
>
>Replace host names, paths, IP ranges, keys, and thresholds with values that match your program. Test changes in a non-production environment before promoting them.

## Customer Managed CDN {#customer-managed-cdn}

### Setting Up Edge Key Authentication for Some Domains Only {#edge-auth-selected-hosts}

Problem: On a [customer-managed CDN](/help/implementing/dispatcher/cdn.md#point-to-point-cdn), you must enforce authentication for some customer hostnames while other hostnames that reach publish should stay available without that header (for example during rollout or when only one brand domain sits behind your CDN).

Solution: Require `X-AEM-Edge-Key` authentication only when the first hostname from `X-Forwarded-Host` equals your target hostname (for example `example.com`). The rule uses the `forwardedDomain` request property to perform that match and runs the `authenticate` action against your edge authenticator. Replace hostnames, authenticator names, and key placeholders for your program.

```yaml
kind: "CDN"
version: "1"
data:
  authentication:
    authenticators:
      - name: edge-key-auth
        type: edge
        edgeKey1: ${{CDN_EDGEKEY_1}}
        edgeKey2: ${{CDN_EDGEKEY_2}}
    rules:
      - name: edge-key-auth-rule
        when: { reqProperty: forwardedDomain, equals: "example.com" }
        action:
          type: authenticate
          authenticator: edge-key-auth
```

### Setting Up Edge Key Authentication for Requests Not Coming from VPN IPs {#edge-auth-trusted-ips}

Problem: Setup edge key authentication for BYOCDN but allow direct access to publish domain only for VPN IPs

Solution: Require X-AEM-Edge-Key authentication only when client IP is not in the list of VPN IPs

```yaml
kind: "CDN"
version: "1"
data:
  authentication:
    authenticators:
      - name: edge-auth
        type: edge
        edgeKey1: ${{CDN_EDGEKEY_1}}
        edgeKey2: ${{CDN_EDGEKEY_2}}
    rules:
      - name: edge-auth-rule
        when: { reqProperty: clientIp, notIn: ["10.0.0.1", "11.0.0.0/24", "<other VPN IPs>"] }
        action:
          type: authenticate
          authenticator: edge-auth
```

## Redirects {#redirects}

### Redirecting from APEX Domain to www {#apex-to-www}

```yaml
redirects:
  rules:
    - name: non-www-to-www-redirect
      when:
        reqProperty: domain
        doesNotMatch: '^www\.'
      action:
        type: redirect
        status: 301
        location:
          join:
            format: 'https://www.%s%s'
            args:
              - reqProperty: domain
              - reqProperty: url
```

### Modifying the Cache Key {#cache-key}

The CDN does not expose a separate “cache key” field. Because the URL participates in caching, you can split cache entries by changing the URL—for example by adding a query parameter through a [request transformation](/help/implementing/dispatcher/cdn-configuring-traffic.md#request-transformations).

```yaml
data:
  requestTransformations:
    rules:
      - name: set-request-different-cache-curl
        when:
          allOf:
            - reqProperty: tier
              equals: publish
            - reqHeader: user-agent
              matches: curl
        actions:
          - type: set
            queryParam: cache
            value: 'curl'
```

### Redirecting to a Normalised Path {#trailing-slash}

Send a permanent redirect when a browser requests a trailing slash on publish—for example from `https://www.example.com/path/` to `https://www.example.com/path`.

```yaml
kind: "CDN"
version: "1"
data:
  redirects:
    rules:
      - name: remove-trailing-slash
        when:
          allOf:
            - reqProperty: tier
              equals: publish
            - reqProperty: domain
              equals: www.example.com
            - reqProperty: originalPath
              matches: ^/(.+)/$
        action:
          type: redirect
          status: 301
          location:
            reqProperty: originalPath
            transform:
              - op: replace
                match: ^/(.+)/$
                replacement: https://www.example.com/\1
```

### Extracting Information from a JSON Cookie {#json-cookie}

```yaml
kind: "CDN"
version: "1"
data:
  requestTransformations:
    rules:
      - name: options-response
        when: { reqProperty: tier, equals: publish }
        actions:
        - type: set
          reqHeader: x-mycookie-info
          value:
            reqCookie: mycookie
            transform: 
            - 'base64decode'
            - { op: 'replace', match: '"info":\s*"([^"]*)"', replacement: '\1'} 
```

## Cross Origin Setup {#cross-origin}

### Serving OPTIONS Requests from the CDN {#options-from-cdn}

```yaml
kind: "CDN"
version: "1"
data:
  requestTransformations:
    rules:
      - name: options-response
        when:
          allOf: 
            - { reqProperty: path, like: /mypathi*  }
            - { reqProperty: method, equals: "OPTIONS" }
            - { reqHeader: Origin, equals: "https://example.com" }
        actions:
          - type: respond
            status: 200
            reason: "OK"
            headers:
              content-type: 'text/plain'
              access-control-allow-origin: { reqHeader: Origin }
              access-control-allow-methods: "*"
              access-control-allow-headers: "*"
```

## Traffic Filters {#traffic-filters}

### Rate Limiting ASN {#rate-limit-asn}

Problem: Per-IP rate limits can miss a distributed denial-of-service (DDoS) pattern: each address stays below the threshold, so legitimate and abusive traffic look alike at the IP layer.

Solution: Count requests by autonomous system name (`clientAsName`) so the limiter aggregates hosts that share the same network name. The snippet writes `clientAsName` to a log property on every request, then applies a rate limit on author and publish grouped by that value. Many users can share one ASN (for example a large ISP or a corporate VPN exit), so tune limits carefully and monitor CDN logs for false positives.

```yaml
kind: "CDN"
version: "1"
data:
  requestTransformations:
    rules:
      - name: log-on-request
        when: "*"
        actions:
          - type: set
            logProperty: client_as_name
            value:
              reqProperty: clientAsName
  trafficFilters:
    rules:
    - name: limit-requests-client-as-name
      when:
        reqProperty: tier
        matches: "author|publish"
      rateLimit:
        limit: 60
        window: 10
        penalty: 300
        count: all
        groupBy:
          - reqProperty: clientAsName
      action: block
```
