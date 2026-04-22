---
title: CDN Configuration Snippets for Common Scenarios
description: Copy-ready YAML patterns for the Adobe-managed CDN and customer-managed CDN setups, including edge authentication, redirects, cache variation, traffic shaping, and rate limits.
feature: Dispatcher
exl-id: 7c4e2a91-3d8f-41b2-9c0e-8f1a2b3c4d5e
role: Admin
---

# CDN Configuration Snippets for Common Scenarios {#cdn-configuration-snippets}

This article collects practical `cdn.yaml` patterns for AEM as a Cloud Service. Use them together with the feature documentation for [CDN traffic rules](/help/implementing/dispatcher/cdn-configuring-traffic.md), [customer-managed CDN credentials](/help/implementing/dispatcher/cdn-credentials-authentication.md), and [traffic filter rules including WAF](/help/security/traffic-filter-rules-including-waf.md). Deploy snippets with a Cloud Manager [config pipeline](/help/operations/config-pipeline.md).

>[!NOTE]
>
>Replace host names, paths, IP ranges, keys, and thresholds with values that match your program. Test changes in a non-production environment before promoting them.

## Customer Managed CDN {#customer-managed-cdn}

### Setting Up Edge Authentication for Some Domains Only {#edge-auth-selected-hosts}

Problem: Setup edge authentication for some domains (eg. example.com) but for others (like the default domain allow unrestricted access)

Solution: Require X-AEM-Edge-Key authentication only when first domain from X-Forwarded-Host is equal to "example.com".

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
        when: { reqProperty: forwardedDomain, equals: "example.com" }
        action:
          type: authenticate
          authenticator: edge-auth
```

### Setting Up Edge Authentication for Requests Not Coming from VPN IPs {#edge-auth-trusted-ips}

Problem: Setup edge authentication for BYOCDN but allow direct access to publish domain only for VPN IPs

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

There is no direct action to modify the cache but given that the url is part of the CDN cache key the url can be modified (for example by adding a query param).

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

Redirect www.example.com/path/ to www.example.com/path

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

Problem: Rate limiting by IPs can be inefficient in case of a DOS attack that is well distributed (volume per IP might be so low that it is impossible to distingue from legit traffic).

Solution: Rate limit per client as name which is the network name associated to the IP (google has many IPs but a unique ASN). It will help blocking the group of IPs behind the attack. You should also consider if customer is using a VPN as it might block VPN as well.

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
