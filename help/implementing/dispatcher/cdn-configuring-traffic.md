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
* [Server-side redirects](#server-side-redirectors) - trigger a browser redirect.
* [Origin selectors](#origin-selectors) - proxy to a different origin backend.

Also configurable at the CDN are Traffic Filter Rules (including WAF), which control what traffic is allowed or denied by the CDN. This feature is already released and you can learn more about it in the [Traffic Filter Rules including WAF rules](/help/security/traffic-filter-rules-including-waf.md) page.

Additionally, if the CDN cannot contact its origin, you can write a rule that references a self-hosted custom error page (which is then rendered). Learn more about this by reading the [Configuring CDN error pages](/help/implementing/dispatcher/cdn-error-pages.md) article.

All these rules, declared in a configuration file in source control, are deployed by using the Cloud Manager [config pipeline](/help/operations/config-pipeline.md). Be aware that the cumulative size of the configuration file, including traffic filter rules, cannot exceed 100KB.

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
    ```

1. Place the file somewhere under a top level folder named *config* or similar, as described under [Config Pipeline](/help/operations/config-pipeline.md#folder-structure).

1. Create a Config Pipeline in Cloud Manager, as described under [Config Pipeline](/help/operations/config-pipeline.md#managing-in-cloud-manager).

1. Deploy the configuration.

## Rules Syntax {#configuration-syntax}

The rule types in the sections below share a common syntax.

A rule is referenced by a name, a conditional "when clause", and actions.

The "when" clause determines whether a rule will be evaluated, based on properties including domain, path, query strings, headers, and cookies. The syntax is the same across rule types; for details, see the [Condition Structure section](/help/security/traffic-filter-rules-including-waf.md#condition-structure) in the Traffic Filter Rules article.

The details of the actions node differ per rule type, and are outlined in the individual sections below.

In the configuration rules, you can reference secrets defined as environment variables (see [Configuration Secrets](/help/implementing/dispatcher/cdn-credentials-authentication.md)).

## Request Transformations {#request-transformations}

Request transformation rules allow you to modify incoming requests. The rules support setting, unsetting, and altering paths, query parameters, and headers (including cookies) based on various matching conditions, including regular expressions. You can also set variables, which can then be referenced later in the evaluation sequence.

Use cases are varied and include URL rewrites for application simplification or mapping legacy URLs.

As mentioned earlier, there is a size limit to the configuration file so organizations with larger requirements should define rules in the `apache/dispatcher` layer.

Configuration example:

```

kind: "CDN"
version: "1"
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
      - name: log-on-request
        when: "*"
        actions:
          - type: set
            logProperty: forwarded_host
            value:
              reqHeader: x-forwarded-host
```

**Actions**

Explained in the table below are the available actions.

| Name      | Properties               | Meaning     |
|-----------|--------------------------|-------------|
| **set** |reqProperty, value|Sets a specified request parameter (only "path" property supported) |
|     |reqHeader, value|Sets a specified request header to a given value.|
|     |queryParam, value|Sets a specified query parameter to a given value.|
|     |reqCookie, value|Sets a specified request cookie to a given value.|
|     |logProperty, value|Sets a specified CDN log property to a given value.|
|     |var, value|Sets a specified variable to a given value.|
| **unset** |reqProperty|Removes a specified request parameter (only "path" property supported)|
|     |reqHeader, value|Removes a specified request header.|
|     |queryParam, value|Removes a specified query parameter.|
|     |reqCookie, value|Removes a specified cookie.|
|     |logProperty, value|Removes a specified CDN log property.|
|     |var|Removes a specified variable.|
|     |queryParamMatch|Removes all query parameters that match a specified regular expression.|
|     |queryParamDoesNotMatch|Removes all query parameters that do not match a specified regular expression.|
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

### Log property {#logproperty}

You can add your own log properties in your CDN logs using request and response transformations.

Configuration example:

```
requestTransformations:
  rules:
    - name: log-on-request
      when: "*"
      actions:
        - type: set
          logProperty: forwarded_host
          value:
            reqHeader: x-forwarded-host
responseTransformations:
  rules:
    - name: log-on-response
      when: '*'
      actions:
        - type: set
          logProperty: cache_control
          value:
            respHeader: cache-control
```

Log example:

```
{
"timestamp": "2025-03-26T09:20:01+0000",
"ttfb": 19,
"cli_ip": "147.160.230.112",
"cli_country": "CH",
"rid": "974e67f6",
"req_ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
"host": "example.com",
"url": "/content/hello.png",
"method": "GET",
"res_ctype": "image/png",
"cache": "PASS",
"status": 200,
"res_age": 0,
"pop": "PAR",
"rules": "",
"forwarded_host": "example.com",
"cache_control": "max-age=300"
}
```

## Response Transformations {#response-transformations}

Response transformation rules allow you to set and unset headers, cookies and status of the CDN's outgoing responses. Also, see the example above for referencing a variable previously set in a request transformation rule.

Configuration example:

```
kind: "CDN"
version: "1"
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
      - name: status-code-rule
        when:
          reqProperty: path
          like: status-code
        actions:
          - type: set
            respProperty: status
            value: '410'
      - name: set-response-cookie-with-attributes-as-object
        when: '*'
        actions:
          - type: set
            respCookie: first-name
            value: first-value
            attributes:
              expires: '2025-08-29T10:00:00'
              domain: example.com
              path: /some-path
              secure: true
              httpOnly: true
              extension: ANYTHING
      - name: unset-response-cookie
        when: '*'
        actions:
          - type: unset
            respCookie: third-name
```

**Actions**

Explained in the table below are the available actions.

| Name      | Properties               | Meaning     |
|-----------|--------------------------|-------------|
| **set** |respProperty, value|Sets a response property. Supports just the property "status" in order to set the status code.|
|     |respHeader, value|Sets a specified response header to a given value.|
|     |respCookie, attributes (expires, domain, path, secure, httpOnly, extension), value|Sets a specified request cookie with specific attributes to a given value.|
|     |logProperty, value|Sets a specified CDN log property to a given value.|
|     |var, value|Sets a specified variable to a given value.|
| **unset** |respHeader|Removes a specified header from the response.|
|     |respCookie, value|Removes a specified cookie.|
|     |logProperty, value|Removes a specified CDN log property.|
|     |var|Removes a specified variable.|

## Origin Selectors {#origin-selectors}

You can leverage the AEM CDN to route traffic to different backends, including non-Adobe applications (perhaps on a per-path or subdomain basis).

The request properties `originalPath` and `originalUrl` are the immutable original path (without query parameters) and full URL (including query parameters), respectively—each taken before any CDN [request transformations](#request-transformations). Use them in `when` conditions when you need to anchor rules on what the client initially sent, rather than values that may have been rewritten earlier in the evaluation sequence. Use `originalPath` for path-only matching; use `originalUrl` when the query string must be part of the condition (for example, routing or filtering on a specific initial request URL).

Configuration example:

```
kind: "CDN"
version: "1"
data:
  originSelectors:
    rules:
      - name: example-com
        when: { reqProperty: originalPath, like: /proxy* }
        action:
          type: selectOrigin
          originName: example-com
          # skipCache: true
          # headers:
          #   Authorization: ${{AUTH_TOKEN}}
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

| Name                | Properties                                 | Meaning                                                                                                                                                                                             |
|---------------------|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **selectOrigin**    | originName                             | Name of one of the defined origins.                                                                                                                                                                 |
|                     | skipCache (optional, default is false) | Flag whether to use caching for requests matching this rule. By default, responses will be cached according to the response caching header (e.g., Cache-Control or Expires)                         |
|                     | headers (optional, default is `{}`)    | Key-value pairs containing additional HTTP headers to be sent to the selected backend when the rule is triggered. With keys corresponding to header names and values corresponding to header values |
| **selectAemOrigin** | originName                             | Name of one of the predefined AEM origins (supported value: `static`).                                                                                                                              |
|                     | skipCache (optional, default is false) | Flag whether to use caching for requests matching this rule. By default, responses will be cached according to the response caching header (e.g., Cache-Control or Expires)                         |
|                     | headers (optional, default is `{}`)    | Key-value pairs containing additional HTTP headers to be sent to the selected backend when the rule is triggered. With keys corresponding to header names and values corresponding to header values |

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

>[!IMPORTANT]
>
>The **domain** value must not contain `.adobeaemcloud.com`. You cannot proxy directly to an adobeaemcloud.com domain. This restriction protects against unwanted request loops. To proxy traffic to your AEM as a Cloud Service environment, use a [custom domain](#proxying-to-aemaacs) installed in your AEMaaCS environment as the origin backend instead.

### Proxying custom domain to AEM static tier {#proxy-custom-domain-static}

Origin selectors can be used to route AEM publish traffic to AEM static content deployed using the [front end pipeline](/help/implementing/developing/introduction/developing-with-front-end-pipelines.md). Use cases include serving static resources on the same domain as the page (e.g., example.com/static) or on an explicitly different domain (e.g., static.example.com).

Here is an example of an origin selector rule that can accomplish this:

```
kind: CDN
version: '1'
data:
  originSelectors:
    rules:
      - name: select-aem-static-origin
        when:
          reqProperty: domain
          equals: static.example.com
        action:
          type: selectAemOrigin
          originName: static
```

### Proxying to Edge Delivery Services {#proxying-to-edge-delivery}

There are scenarios where origin selectors should be used to route traffic through AEM Publish to AEM Edge Delivery Services:

* Some content is delivered by a domain managed by AEM Publish, while other content from the same domain is delivered by Edge Delivery Services.
* Content delivered by Edge Delivery Services would benefit from rules deployed via config pipeline, including traffic filter rules or request/response transformations.
* The Edge Delivery configuration pipeline lets you configure Adobe-managed CDN settings by defining rules such as `trafficFilters`, `originSelectors`, and `redirects`. <!-- https://wiki.corp.adobe.com/pages/editpage.action?pageId=3610084282 -->

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
>
>Because the Adobe Managed CDN is used, make sure to configure push invalidation in **managed** mode, by following the Edge Delivery Services [Setup push invalidation documentation](https://www.aem.live/docs/byo-dns#setup-push-invalidation).


### Proxying to AEMaaCS environment {#proxying-to-aemaacs}

You cannot use an `adobeaemcloud.com` domain directly as an origin in your CDN configuration. Doing so is rejected (domain must not contain `.adobeaemcloud.com`) to protect against unwanted request loops. This also applies when routing from a domain installed for an Edge Delivery Site.

If your custom domain (`www.example.com`) is already installed to an AEMaaCS environment, the default routing will route to AEM backend without any CDN rule. Use origin selectors when you need to route cross-environment (for example, from `pXXXX-eYYYY` to `pXXXX-eZZZZ`) or from an Edge Delivery Site to an AEMaaCS environment.

To proxy traffic to your AEM as a Cloud Service environment in those cases (for example, to route specific paths such as `/graphql` to a backend), install a custom domain in your AEMaaCS environment and use that custom domain as the origin in your CDN configuration.

**Example:** If your AEM publish tier is reachable at `publish-pXXXXX-eYYYYY.adobeaemcloud.com`, do not use that domain in `originSelectors`. Instead:

1. Install a custom domain in your AEMaaCS environment (for example, `aem-publish-origin.example.com`) that points to your publish service.
2. In your CDN config, define an origin with that custom domain and route the desired paths (for example, `/graphql`) to it.

```
kind: CDN
version: '1'
data:
  originSelectors:
    rules:
      - name: graphql-to-aem-publish
        when:
          allOf:
            - reqProperty: domain
              equals: www.example.com
            - reqProperty: originalPath
              like: /graphql*
        action:
          type: selectOrigin
          originName: aem-publish-origin
    origins:
      - name: aem-publish-origin
        domain: aem-publish-origin.example.com
```


## Server-side Redirects {#server-side-redirectors}

You can use client side redirect rules for 301, 302 and similar client side redirects. If a rule matches, the CDN responds with a status line that includes the status code and message (for example, HTTP/1.1 301 Moved Permanently), as well as the location header set.

Both absolute and relative locations with fixed values are allowed.

Be aware that the cumulative size of the configuration file, including traffic filter rules, cannot exceed 100KB.

Configuration example:

```

kind: "CDN"
version: "1"
data:
  redirects:
    rules:
      - name: redirect-absolute
        when: { reqProperty: originalPath, equals: "/page.html" }
        action:
          type: redirect
          status: 301
          location: https://example.com/page
      - name: redirect-relative
        when: { reqProperty: originalPath, equals: "/anotherpage.html" }
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
