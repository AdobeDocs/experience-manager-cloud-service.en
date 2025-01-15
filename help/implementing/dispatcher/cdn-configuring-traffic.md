---
title: Configuring Traffic at the CDN
description: Learn how to configure CDN traffic by declaring rules and filters in a configuration file and deploying them to the CDN by using a Cloud Manager config pipeline.
feature: Dispatcher
exl-id: e0b3dc34-170a-47ec-8607-d3b351a8658e
role: Admin
---

# Configuring Traffic at the CDN {#cdn-configuring-cloud}

AEM as a Cloud Service offers a collection of features configurable at the [Adobe-managed CDN](/help/implementing/dispatcher/cdn.md#aem-managed-cdn) layer that modify the nature of either incoming requests or outgoing responses. The following rules, described in detail in this page, can be declared to achieve the following behavior:

* [Request transformations](#request-transformations) - modify aspects of incoming requests, including headers, paths and parameters.
* [Response transformations](#response-transformations) - modify headers that are on the way back to the client (for example, a web browser).
* [Client-side redirects](#client-side-redirectors) - trigger a browser redirect.
* [Origin selectors](#origin-selectors) - proxy to a different origin backend.

Also configurable at the CDN are Traffic Filter Rules (including WAF), which control what traffic is allowed or denied by the CDN. This feature is already released and you can learn more about it in the [Traffic Filter Rules including WAF rules](/help/security/traffic-filter-rules-including-waf.md) page.

Additionally, if the CDN cannot contact its origin, you can write a rule that references a self-hosted custom error page (which is then rendered). Learn more about this by reading the [Configuring CDN error pages](/help/implementing/dispatcher/cdn-error-pages.md) article.

All these rules, declared in a configuration file in source control, are deployed by using the Cloud Manager [config pipeline.](/help/operations/config-pipeline.md) Be aware that the cumulative size of the configuration file, including traffic filter rules, cannot exceed 100KB.

## Order of Evaluation {#order-of-evaluation}

Functionally, the various features mentioned previously are evaluated in the following sequence:

![Order of evaluation](/help/implementing/dispatcher/assets/order.png)

## Setup {#initial-setup}

Before you can configure traffic at the CDN you need to do the following:

1. Create a file named `cdn.yaml` or similar, referencing the various configuration snippets in the sections below.

    All snippets have these common properties, which are described under [Config Pipeline](/help/operations/config-pipeline.md#common-syntax). The `kind` property value should be *CDN* and the `version` property should be set to *1*.
    ```
    kind: "CDN"
    version: "1"
    metadata:
      envTypes: ["dev"]
    ```

1. Place the file somewhere under a top level folder named *config* or similar, as described under [Config Pipeline](/help/operations/config-pipeline.md#folder-structure).

1. Create a Config Pipeline in Cloud Manager, as described under [Config Pipeline](/help/operations/config-pipeline.md#managing-in-cloud-manager).

1. Deploy the configuration.

## Rules Syntax {#configuration-syntax}

The rule types in the sections below share a common syntax.

A rule is referenced by a name, a conditional "when clause", and actions.

The when clause determines whether a rule will be evaluated, based on properties including domain, path, query strings, headers, and cookies. The syntax is the same across rule types; for details, see the [Condition Structure section](/help/security/traffic-filter-rules-including-waf.md#condition-structure) in the Traffic Filter Rules article.

The details of the actions node differ per rule type, and are outlined in the individual sections below.

## Request Transformations {#request-transformations}

Request transformation rules allow you to modify incoming requests. The rules support setting, unsetting, and altering paths, query parameters, and headers (including cookies) based on various matching conditions, including regular expressions. You can also set variables, which can then be referenced later in the evaluation sequence.

Use cases are varied and include URL rewrites for application simplification or mapping legacy URLs.

As mentioned earlier, there is a size limit to the configuration file so organizations with larger requirements should define rules in the `apache/dispatcher` layer.

Configuration example:

```

kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev", "stage", "prod"]
data:
  requestTransformations:
    removeMarketingParams: true
    rules:
      - name: set-header-rule
        when:
          reqProperty: path
          like: /set-header
        actions:
          - type: set
            reqHeader: x-some-header
            value: some value
      - name: set-header-with-reqproperty-rule
        when:
          reqProperty: path
          like: /set-header
        actions:
          - type: set
            reqHeader: x-some-header
            value: {reqProperty: path}
      - name: unset-header-rule
        when:
          reqProperty: path
          like: /unset-header
        actions:
          - type: unset
            reqHeader: x-some-header

      - name: unset-matching-query-params-rule
        when:
          reqProperty: path
          equals: /unset-matching-query-params
        actions:
          - type: unset
            queryParamMatch: ^removeMe_.*$

      - name: unset-all-query-params-except-exact-two-rule
        when:
          reqProperty: path
          equals: /unset-all-query-params-except-exact-two
        actions:
          - type: unset
            queryParamMatch: ^(?!leaveMe$|leaveMeToo$).*$

      - name: multi-action
        when:
          reqProperty: path
          like: /multi-action
        actions:
          - type: set
            reqHeader: x-header1
            value: body set by transformation rule
          - type: set
            reqHeader: x-header2
            value: '201'

      - name: replace-html
        when:
          reqProperty: path
          like: /mypath
        actions:
          - type: transform
            reqProperty: path
            op: replace
            match: \.html$
            replacement: ""

```

**Actions**

Explained in the table below are the available actions.

| Name      | Properties               | Meaning     |
|-----------|--------------------------|-------------|
| **set** |(reqProperty or reqHeader or queryParam or reqCookie), value|Sets a specified request parameter (only "path" property supported), or request header, query parameter, or cookie, to a given value, which could be a string literal or request parameter. |
|     |var, value|Sets a specified request property to a given value.|
| **unset** |reqProperty|Removes a specified request parameter (only "path" property supported), or request header, query parameter, or cookie, to a given value, which could be a string literal or request parameter.|
|         |var|Removes a specified variable.|
|         |queryParamMatch|Removes all query parameters that match a specified regular expression.|
| **transform** |op:replace, (reqProperty or reqHeader or queryParam or reqCookie or var), match, replacement  | Replaces part of the request parameter (only "path" property supported), or request header, or query parameter, or cookie, or variable with a new value. |
|              |op:tolower, (reqProperty or reqHeader or queryParam or reqCookie or var) | Sets the request parameter (only "path" property supported), or request header, or query parameter, or cookie, or variable to its lowercase value. |

Replace actions support capture groups, as illustrated below:

```
      - name: extract-country-code-from-path
        when:
          reqProperty: path
          matches: ^/([a-zA-Z]{2})(/.*|$)
        actions:
          - type: set
            var: country-code
            value:
              reqProperty: path
          - type: transform
            var: country-code
            op: replace
            match: ^/([a-zA-Z]{2})(/.*|$)
            replacement: \1
      - name: replace-jpg-with-jpeg
        when:
          reqProperty: path
          like: /mypath
        actions:
          - type: transform
            reqProperty: path
            op: replace
            match: (.*)(\.jpg)$
            replacement: "\1\.jpeg"
```

Actions can be chained together. For example:

```
actions:
    - type: transform
      reqProperty: path
      op: replace
      match: \.html$
      replacement: ""
    - type: transform
      reqProperty: path
      op: tolower
```

### Variables {#variables}

You can set variables during the request transformation and then reference them later on in the evaluation sequence. See the [order of evaluation](#order-of-evaluation) diagram for further details.

Configuration example:

```

kind: "CDN"
version: "1"
metadata:
  envTypes: ["prod", "dev"]
data:
  requestTransformations:
    rules:
      - name: set-variable-rule
        when:
          reqProperty: path
          equals: /set-variable
        actions:
          - type: set
            var: some_var_name
            value: some_value

  responseTransformations:
    rules:
      - name: set-response-header-while-variable
        when:
          var: some_var_name
          equals: some_value
        actions:
          - type: set
            respHeader: x-some-header
            value: some header value

```

## Response Transformations {#response-transformations}

Response transformation rules allow you to set and unset headers of the CDN's outgoing responses. Also, see the example above for referencing a variable previously set in a request transformation rule. The response's status code can also be set.

Configuration example:

```

kind: "CDN"
version: "1"
metadata:
  envTypes: ["prod", "dev"]
data:
  responseTransformations:
    rules:
      - name: set-response-header-rule
        when:
          reqProperty: path
          like: /set-response-header
        actions:
          - type: set
            value: value-set-by-resp-rule
            respHeader: x-resp-header

      - name: unset-response-header-rule
        when:
          reqProperty: path
          like: /unset-response-header
        actions:
          - type: unset
            respHeader: x-header1

      # Example: Multi-action on response header
      - name: multi-action-response-header-rule
        when:
          reqProperty: path
          like: /multi-action-response-header
        actions:
          - type: set
            respHeader: x-resp-header-1
            value: value-set-by-resp-rule-1
          - type: set
            respHeader: x-resp-header-2
            value: value-set-by-resp-rule-2
      # Example: setting status code
      - name: status-code-rule
        when:
          reqProperty: path
          like: status-code
        actions:
          - type: set
            respProperty: status
            value: '410'        

```

**Actions**

Explained in the table below are the available actions.

| Name      | Properties               | Meaning     |
|-----------|--------------------------|-------------|
| **set** |reqHeader, value|Sets a specified header to a given value in the response.|
|          |respProperty, value|Sets a response property. Supports just the property "status" in order to set the status code.|
| **unset** |respHeader|Removes a specified header from the response.|

## Origin Selectors {#origin-selectors}

You can leverage the AEM CDN to route traffic to different backends, including non-Adobe applications (perhaps on a per-path or subdomain basis).

Configuration example:

```

kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  originSelectors:
    rules:
      - name: example-com
        when: { reqProperty: path, like: /proxy* }
        action:
          type: selectOrigin
          originName: example-com
          # skipCache: true
    origins:
      - name: example-com
        domain: www.example.com
        # ip: '1.1.1.1'
        # forwardHost: true
        # forwardCookie: true
        # forwardAuthorization: true
        # timeout: 20

```

**Actions**

Explained in the table below is the available action.

| Name      | Properties               | Meaning     |
|-----------|--------------------------|-------------|
|**selectOrigin** |originName|Name of one of the defined origins.|
|     |skipCache (optional, default is false)| Flag whether to use caching for requests matching this rule. By default, responses will be cached according to the response caching header (e.g., Cache-Control or Expires) |

**Origins**

Connections to origins are SSL only and use port 443.

| Property          | Meaning                    |
|------------------|--------------------------------------|
| **name** |Name which can be referenced by "action.originName".|
| **domain** |Domain name used to connect to the custom backend. It is also used for SSL SNI and validation.|
| **ip** (optional, supported iv4 and ipv6) |If provided, it is used to connect to the backend instead of "domain". Still "domain" is used for SSL SNI and validation.|
| **forwardHost** (optional, default is false) |If set to true, then "Host" header from the client request will be passed to the backend, otherwise the "domain" value will be passed in the "Host" header.|
| **forwardCookie** (optional, default is false) |If set to true then the "Cookie" header from the client request will be passed to backend, otherwise the Cookie header is removed.|
| **forwardAuthorization** (optional, default is false) |If set to true then the "Authorization" header from the client request will be passed to the backend, otherwise the Authorization header is removed.|
| **timeout** (optional, in seconds, default is 60) |Number of seconds the CDN should wait for a backend server to deliver the first byte of an HTTP response body. This value is also used as a between bytes timeout to the backend server.|

### Proxying to Edge Delivery Services {#proxying-to-edge-delivery}

There are scenarios where origin selectors should be used to route traffic through AEM Publish to AEM Edge Delivery Services:

* Some content is delivered by a domain managed by AEM Publish, while other content from the same domain is delivered by Edge Delivery Services
* Content delivered by Edge Delivery Services would benefit from rules deployed via config pipeline, including traffic filter rules or request/response transformations

Here is an example of an origin selector rule that can accomplish this:

```
kind: CDN
version: '1'
data:
  originSelectors:
    rules:
      - name: select-edge-delivery-services-origin
        when:
          allOf:
            - reqProperty: tier
              equals: publish
            - reqProperty: domain
              equals: <Production Host>
            - reqProperty: path
              matches: "^(/scripts/.*|/styles/.*|/fonts/.*|/blocks/.*|/icons/.*|.*/media_.*|/favicon.ico)"
        action:
          type: selectOrigin
          originName: aem-live
    origins:
      - name: aem-live
        domain: main--repo--owner.aem.live
```

>[!NOTE]
> Since the Adobe Managed CDN is used, make sure to configure push invalidation in **managed** mode, by following the Edge Delivery Services [Setup push invalidation documentation](https://www.aem.live/docs/byo-dns#setup-push-invalidation).


## Client-side Redirects {#client-side-redirectors}

You can use client side redirect rules for 301, 302 and similar client side redirects. If a rule matches, the CDN responds with a status line that includes the status code and message (for example, HTTP/1.1 301 Moved Permanently), as well as the location header set.

Both absolute and relative locations with fixed values are allowed.

Be aware that the cumulative size of the configuration file, including traffic filter rules, cannot exceed 100KB.

Configuration example:

```

kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  redirects:
    rules:
      - name: redirect-absolute
        when: { reqProperty: path, equals: "/page.html" }
        action:
          type: redirect
          status: 301
          location: https://example.com/page
      - name: redirect-relative
        when: { reqProperty: path, equals: "/anotherpage.html" }
        action:
          type: redirect
          location: /anotherpage

```

| Name      | Properties               | Meaning     |
|-----------|--------------------------|-------------|
|**redirect** |location|Value for the "Location" header.|
|     |status (optional, default is 301)|HTTP status to be used in the redirect message, 301 by default, the allowed values are: 301, 302, 303, 307, 308.|

The locations of a redirect can be either string literals (e.g., https://www.example.com/page) or the result of a property (e.g., path) that is optionally transformed, with the following syntax:

```
redirects:
  rules:
    - name: country-code-redirect
      when: { reqProperty: path, like: "/" }
      action:
        type: redirect
        location:
          reqProperty: clientCountry
          transform:
            - op: replace
              match: '^(.*)$'
              replacement: 'https://www.example.com/\1/home'
            - op: tolower
    - name: www-redirect
      when: { reqProperty: domain, equals: "example.com" }
      action:
        type: redirect
        location:
          reqProperty: url
          transform:
            - op: replace
              match: '^/(.*)$'
              replacement: 'https://www.example.com/\1'
```
