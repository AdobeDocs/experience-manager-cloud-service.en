---
title: Traffic Filter Rules including WAF Rules
description: Configuring Traffic Filter Rules including Web Application Firewall (WAF) Rules
exl-id: 6a0248ad-1dee-4a3c-91e4-ddbabb28645c
---

# Traffic Filter Rules Including WAF Rules {#traffic-filter-rules-including-waf-rules}

Traffic filter rules can be used to block or allow requests at the CDN layer, which may be useful in scenarios such as:

* Restricting access to specific domains to internal company traffic, before a new site goes live
* Establishing rate limits so as to be less susceptible to volumetric DoS attacks
* Preventing IP addresses known to be malicious from targeting your pages

Most of these traffic filter rules are available to all AEM as a Cloud Service Sites and Forms customers. They mainly operate on request properties and request headers, including IP, hostname, path, and user agent.

A subcategory of traffic filter rules require either an Enhanced Security license or WAF-DDoS Protection license. These powerful rules are known as WAF (Web Application Firewall) traffic filter rules (or WAF rules for short) and have access to the [WAF Flags](#waf-flags-list) described later in this article.

Traffic filter rules can be deployed via Cloud Manager configuration pipelines to dev, stage, and production environment types in production (non-sandbox) programs. Support for RDEs will come in the future.

[Follow through a tutorial](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/security/traffic-filter-and-waf-rules/overview.html) to quickly build concrete expertise on this feature.

## How This Article is Organized {#how-organized}

This article is organized into the following sections:

* **Traffic protection overview:** Learn how you are protected from malicious traffic.
* **Suggested process for configuring rules:** Read about a high level methodology for protecting your website.
* **Setup:** Discover how to setup, configure, and deploy traffic filter rules, including the advanced WAF rules.
* **Rules syntax:** Read about how to declare traffic filter rules in the `cdn.yaml` configuration file. This includes both the traffic filter rules available to all Sites and Forms customers, and the subcategory of WAF rules for those who license that capability.
* **Rules examples:** See examples of declared rules to get you on your way.
* **Rate limit rules:** Learn how to use rate limiting rules to protect your site from high volume attacks.
* **CDN logs:** See what declared rules and WAF Flags match your traffic.
* **Dashboard Tooling:** Analyze your CDN logs to come up with new traffic filter rules.
* **Recommended Starter Rules:** A set of rules to get started with.
* **Tutorial:** Practical knowledge about the feature, including how to use dashboard tooling to declare the right rules.

We invite you to give feedback or ask questions about traffic filter rules by emailing **aemcs-waf-adopter@adobe.com**.

## Traffic Protection Overview {#traffic-protection-overview}

In the current digital landscape, malicious traffic is an ever-present threat. We recognize the gravity of the risk and offer several approaches to protect customer applications and mitigate attacks when they occur.

At the edge, the Adobe Managed CDN absorbs DoS attacks at the network
layer (layers 3 and 4), including flood and reflection/amplification attacks.

By default, Adobe takes measures to prevent performance degradation due to bursts of unexpectedly high traffic beyond a certain threshold. In the event of a DoS attack impacting site availability, Adobe's operations teams are alerted and take steps to mitigate.

Customers may take proactive measures to mitigate application layer attacks (layer 7) by configuring rules at various layers of the content delivery flow.

For example, at the Apache layer, customers may configure either the [dispatcher module](https://experienceleague.adobe.com/docs/experience-manager-dispatcher/using/configuring/dispatcher-configuration.html#configuring-access-to-content-filter) or [ModSecurity](https://experienceleague.adobe.com/docs/experience-manager-learn/foundation/security/modsecurity-crs-dos-attack-protection.html) to limit access to certain content.

And as this article describes, traffic filter rules rules may be deployed to the Adobe Managed CDN, using Cloud Manager's configuration pipeline. In addition to traffic filter rules based on properties like IP address, path, and headers, or rules based on setting rate limits, customers may also license a powerful subcategory of traffic filter rules called WAF rules.

## Suggested Process {#suggested-process}

The following is a high-level recommended end-to-end process for coming up with the right traffic filter rules:

1. Configure non-production and production configuration pipelines, as described in the [Setup](#setup) section.
1. Customers who have licensed the subcategory of WAF traffic filter rules should enable them in Cloud Manager.
1. Read and try out the tutorial to concretely understand how to use traffic filter rules, including WAF rules if they've been licensed. The tutorial walks you through deploying rules to a dev environment, simulating malicious traffic, downloading the [CDN logs](#cdn-logs), and analyzing them in [dashboard tooling](#dashboard-tooling).
1. Copy the recommended starter rules to `cdn.yaml` and deploy the configuration to the production environment in log mode.
1. After collecting some traffic, analyze the results using [dashboard tooling](#dashboard-tooling) to see if there were any matches. Lookout for false positives, and make any necessary adjustments, ultimately enabling the starter rules in block mode.
1. Add custom rules based on analysis of the CDN logs, first testing with simulated traffic on dev environments before deploying to stage and production environments in log mode, then block mode.
1. Monitor traffic on an ongoing basis, making changes to the rules as the threat landscape evolves.

## Setup {#setup}

1. First, create the following folder and file structure the top-level folder in your project in Git:

   ```
   config/
        cdn.yaml
   ```

1. `cdn.yaml` should contain metadata and a list of traffic filters rules and WAF rules.

   ```
   kind: "CDN"
   version: "1"
   metadata:
     envTypes: ["dev"]
   data:
     trafficFilters:
       rules:
       # Block simple path
       - name: block-path
         when:
           allOf:
             - reqProperty: tier
               matches: "author|publish"
             - reqProperty: path
               equals: '/block/me'
         action: block
   ```

  The `kind` parameter should be set to `CDN` and the version should be set to the schema version, which is currently `1`. See examples further below.


   <!-- Two properties -- `envType` and `envId` -- may be included to limit the scope of the rules. The envType property may have values "dev", "stage", or "prod", while the envId property is the environment (for example, "53245"). This approach is useful if it is desired to have a single configuration pipeline, even if some environments have different rules. However, a different approach could be to have multiple configuration pipelines, each pointing to different repositories or git branches. -->

1. If WAF rules are licensed, you should enable the feature in Cloud Manager, as described below for both the new and existing program scenarios.

   1. To configure WAF on a new program, check the **WAF-DDOS Protection** check-box on the **Security** tab when you [add a production program.](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md)

   1. To configure WAF on an existing program, [editing your program](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/editing-programs.md) and on the **Security** tab uncheck or check the **WAF-DDOS** option at any time.

1. For environment types other than RDE, create a targeted deployment config pipeline in Cloud Manager.

   * [See configuring production pipelines](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md).
   * [See configuring non-production pipelines](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md).

For RDEs, the command line will be used, but RDE is not supported at this time.

**Notes**

* You can use `yq` to validate locally the YAML formatting of your configuration file (for example, `yq cdn.yaml`).

## Traffic Filter Rules Syntax {#rules-syntax}

You can configure `traffic filter rules` to match on patterns such as IPs, user agent, request headers, hostname, geo, and url.

Customers who license the Enhanced Security or WAF-DDoS Protection Security offering can also configure a special category of traffic filter rules called `WAF traffic filter rules` (or WAF rules for short) that reference one or more [WAF flags](#waf-flags-list).

Here's an example of a set of traffic filter rules, which also includes a WAF rule.

```
kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  trafficFilters:
    rules:
      - name: "path-rule"
        when: { reqProperty: path, equals: /block-me }
        action:
          type: block
      - name: "Enable-SQL-Injection-and-XSS-waf-rules-globally"
        when: { reqProperty: path, like: "*" }
        action:
          type: block
          wafFlags: [ SQLI, XSS]
```

The format of the traffic filter rules in the `cdn.yaml` file is described below. See some [other examples](#examples) in a later section, and a separate section on [Rate Limit Rules](#rate-limit-rules).


| **Property**   | **Most traffic filter rules**  | **WAF traffic filter rules**  | **Type**  | **Default value**  | **Description**  |
|---|---|---|---|---|---|
| name  | X  | X  | `string`  | -  | Rule name (64 chars long, can only contain alphanumerics and - )  |
| when  | X  | X  | `Condition`  | -  | The basic structure is:<br><br>`{ <getter>: <value>, <predicate>: <value> }`<br><br>[See Condition Structure syntax](#condition-structure) below, which describes the getters, predicates, and how to combine multiple conditions.  |
| action  | X  | X  | `Action` | log  | log, allow, block, or Action object. Default is log |
|  rateLimit | X  |   | `RateLimit`  | not defined  | Rate limiting configuration. Rate limiting is disabled if not defined.<br><br>There is a separate section further below describing the rateLimit syntax, along with examples.  |

### Condition Structure {#condition-structure}

A Condition can be either a simple Condition or a group of Conditions.

**Simple Condition**

A Simple Condition is composed of a getter and a predicate.

```
{ <getter>: <value>, <predicate>: <value> }
```

**Group Conditions**

A Group of Conditions is composed of multiple Simple and/or Group Conditions.

```
<allOf|anyOf>:
  - { <getter>: <value>, <predicate>: <value> }
  - { <getter>: <value>, <predicate>: <value> }
  - <allOf|anyOf>:
    - { <getter>: <value>, <predicate>: <value> }
```

|  **Property** | **Type**  | **Meaning**  |
|---|---|---|
| **allOf**  | `array[Condition]` | **and** operation. true if all listed conditions return true  |
|  **anyOf** |  `array[Condition]` | **or** operation. true if any of listed conditions return true  |

**Getter**

| **Property**   | **Type**  | **Description**  |
|---|---|---|
| reqProperty  | `string`  | Request property.<br><br>One of:<br><ul><li>`path`: Returns the full path of a URL without the query parameters.</li><li>`queryString`: Returns the query part of a URL</li><li>`method`: Returns the HTTP method used in the request.</li><li>`tier`: Returns one of `author`, `preview` or `publish`.</li><li>`domain`: Returns the domain property (as defined in the `Host` header) in lower-case</li><li>`clientIp`: Returns the client IP.</li><li>`clientCountry`: Returns a two letter code ([https://en.wikipedia.org/wiki/Regional_indicator_symbol](https://en.wikipedia.org/wiki/Regional_indicator_symbol) that identify in which country the client is located.</li></ul> |
| reqHeader  | `string`  | Returns Request Header with specified name  |
| queryParam  | `string` | Returns Query Parameter with specified name  |
| reqCookie  | `string`  | Returns Cookie with specified name  |
| postParam  | `string`  | Returns Post Parameter with specified name from Request body. Only works when body is of content type `application/x-www-form-urlencoded` |

**Predicate**

| **Property**  | **Type**  | **Meaning**  |
|---|---|---|
|  **equals** | `string`  | true if the getter result equals to provided value  |
|  **doesNotEqual** | `string`  | true if the getter result is not equal to provided value  |
| **like**  | `string`  | true if getter result matches provided pattern  |
| **notLike**  | `string`  | true if getter result does not match provided pattern  |
| **matches**  | `string`  | true if getter result matches provided regex  |
| **doesNotMatch**  | `string`  | true if getter result does not match provided regex  |
| **in**  | `array[string]`  | true if provided list contains getter result  |
|  **notIn** | `array[string]`  | true if provided list does not contain getter result  |
|  **exists** | `boolean`  | true when set to true and property exists or when set to false and property does not exist  |

**Notes**

* The request property `clientIp` can only be used with the following predicates: `equals`, `doesNotEqual`, `in`, `notIn`. `clientIp` can also be compared against IP ranges when using `in` and `notIn` predicates. The following example implements a condition to evaluate if a client IP is in the IP range of 192.168.0.0/24 (so from 192.168.0.0 to 192.168.0.255):

```
when:
  reqProperty: clientIp
  in: [ "192.168.0.0/24" ]
```

* We recommend the use of [regex101](https://regex101.com/) and [Fastly Fiddle](https://fiddle.fastly.dev/) when working with regex. You can also learn more about how Fastly handles regex in this [article](https://developer.fastly.com/reference/vcl/regex/#best-practices-and-common-mistakes).


### Action Structure {#action-structure}

An `action` can either be a string specifying the action (allow, block or log), or an object composed of both the action type (allow, block or log) and options like wafFlags and/or status.

**Action Types**

Actions are prioritized according to their types in the following table, which is ordered to reflect the order actions are executed:

| **Name**  | **Allowed Properties**  | **Meaning**  |
|---|---|---|
|  **allow** | `wafFlags` (optional), `alert` (optional, not yet released)  | if wafFlags is not present, stops further rule processing and proceeds to serving response. If wafFlags is present, it disables specified WAF protections and proceeds to further rule processing. <br>If alert is specified, an Actions Center notification is sent if the rule is triggered 10 times in a 5 minute window. This feature is not yet released; see the [Traffic Filter Rules Alerts](#traffic-filter-rules-alerts) section for information on how to join the early adopter program. |
|  **block** | `status, wafFlags` (optional and mutually exclusive), `alert` (optional, not yet released)  | if wafFlags is not present, returns HTTP error bypassing all other properties, error code is defined by status property or defaults to 406. If wafFlags is present, it enables specified WAF protections and proceeds to further rule processing. <br>If alert is specified, an Actions Center notification is sent if the rule is triggered 10 times in a 5 minute window. This feature is not yet released; see the [Traffic Filter Rules Alerts](#traffic-filter-rules-alerts) section for information on how to join the early adopter program. |
| **log**  | `wafFlags` (optional), `alert` (optional, not yet released)  | logs the fact that the rule was triggered, otherwise does not affect the processing. wafFlags has no effect. <br>If alert is specified, an Actions Center notification is sent if the rule is triggered 10 times in a 5 minute window. This feature is not yet released; see the [Traffic Filter Rules Alerts](#traffic-filter-rules-alerts) section for information on how to join the early adopter program. |

### WAF Flags List {#waf-flags-list}

The `wafFlags` property, which can be used in the licensable WAF traffic filter rules, may reference the following:

| **Flag ID**  | **Flag Name** | **Description**  |
|---|---|---|
| SQLI  | SQL Injection  | SQL Injection is the attempt to gain access to an application or obtain privileged information by executing arbitrary database queries.  |
| BACKDOOR  |  Backdoor | A backdoor signal is a request which attempts to determine if a common backdoor file is present on the system.  |
| CMDEXE  | Command Execution  | Command Execution is the attempt to gain control or damage a target system through arbitrary system commands by means of user input.  |
| XSS  |  Cross Site Scripting | Cross-Site Scripting is the attempt to hijack a user's account or web-browsing session through malicious JavaScript code.  |
| TRAVERSAL  | Directory Traversal  | Directory Traversal is the attempt to navigate privileged folders throughout a system in hopes of obtaining sensitive information.  |
| USERAGENT  |  Attack tooling |  Attack Tooling is the use of automated software to identify security vulnerabilities or to attempt to exploit a discovered vulnerability. |
| LOG4J-JNDI  | Log4J JNDI  |  Log4J JNDI attacks attempt to exploit the [Log4Shell vulnerability](https://en.wikipedia.org/wiki/Log4Shell) present in Log4J versions earlier than 2.16.0 |
| BHH  | Bad Hop Headers | Bad Hop Headers indicate an HTTP smuggling attempt through either a malformed Transfer-Encoding (TE) or Content-Length (CL) header, or a well-formed TE and CL header  |
| CODEINJECTION | Code Injection | Code Injection is the attempt to gain control or damage a target system through arbitrary application code commands by means of user input. |
| ABNORMALPATH  | Abnormal Path  | Abnormal Path indicates that the original path differs from the normalized path (for example, `/foo/./bar` is normalized to `/foo/bar`)  |
| DOUBLEENCODING  | Double Encoding  |  Double Encoding checks for the evasion technique of double encoding html characters |
| NOTUTF8  | Invalid Encoding  | Invalid Encoding can cause the server to translate malicious characters from a request into a response, causing either a denial of service or XSS  |
| JSON-ERROR  | JSON Encoding Error  | A POST, PUT, or PATCH request body that is specified as containing JSON within the "Content-Type" request header but contains JSON parsing errors. This is often related to a programming error or an automated or malicious request.  |
| MALFORMED-DATA  | Malformed Data in the request body  | A POST, PUT, or PATCH request body that is malformed according to the "Content-Type" request header. For example, if a "Content-Type: application/x-www-form-urlencoded" request header is specified and contains a POST body that is json. This is often a programming error, automated or malicious request. Requires agent 3.2 or higher.  |
| SANS  | Malicious IP Traffic  | [SANS Internet Storm Center](https://isc.sans.edu/) list of IP addresses that have been reported to have engaged in malicious activity  |
| NO-CONTENT-TYPE  | Missing "Content-Type" request header  | A POST, PUT, or PATCH request that does not have a "Content-Type" request header. By default application servers should assume "Content-Type: text/plain; charset=us-ascii" in this case. Many automated and malicious requests may be missing "Content Type".  |
| NOUA  | No User Agent  | Many automated and malicious requests use fake or missing User-Agents to make it difficult to identify the type of device making the requests.  |
| TORNODE  |  Tor Traffic | Tor is software that conceals a user's identity. A spike in Tor traffic can indicate an attacker trying to mask their location.  |
| NULLBYTE  | Null Byte | Null bytes do not normally appear in a request and indicate that the request is malformed and potentially malicious. |
| PRIVATEFILE  | Private files  | Private files are usually confidential in nature, such as an Apache `.htaccess` file, or a configuration file which could leak sensitive information  |
| SCANNER  |  Scanner | Identifies popular scanning services and tools  |
| RESPONSESPLIT  | HTTP Response Splitting  | Identifies when CRLF characters are submitted as input to the application to inject headers into the HTTP response  |
| XML-ERROR  | XML Encoding Error  | A POST, PUT, or PATCH request body that is specified as containing XML within the "Content-Type" request header but contains XML parsing errors. This is often related to a programming error or an automated or malicious request.  |

## Considerations {#considerations}

* When two conflicting rules are created, the allow rules will always take precedence over the block rules. For example, if you create a rule to block a specific path and a rule to allow one specific IP address, requests from that IP address on the blocked path will be allowed.

* If a rule is matched and blocked, the CDN responds with a `406` return code.

* The configuration files should not contain secrets since they would be readable by anyone who has access to the git repository.

* IP Allow lists defined in Cloud Manager take precedence over Traffic Filters Rules.

* WAF rule matches only appear in CDN logs for CDN misses and passes, not hits.

## Rules Examples {#examples}

Some rule examples follow. See the [rate limit section](#rules-with-rate-limits) further down for examples of rate limit rules.

**Example 1**

This rule blocks requests coming from **IP 192.168.1.1**:

```
kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  trafficFilters:
     rules:
       - name: "block-request-from-ip"
         when: { reqProperty: clientIp, equals: "192.168.1.1" }
         action:
           type: block
```

**Example 2**

This rule blocks requests on path `/helloworld` on publish with a User-Agent that contains Chrome:

```
kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  trafficFilters:
    rules:
      - name: "block-request-from-chrome-on-path-helloworld-for-publish-tier"
        when:
          allOf:
          - { reqProperty: path, equals: /helloworld }
          - { reqProperty: tier, equals: publish }
          - { reqHeader: user-agent, matches: '.*Chrome.*'  }
        action:
          type: block
```

**Example 3**

This rule blocks requests that contain the query parameter `foo`, but allows every request coming from IP 192.168.1.1:

```
kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  trafficFilters:
    rules:
      - name: "block-request-that-contains-query-parameter-foo"
        when: { queryParam: url-param, equals: foo }
        action:
          type: block
      - name: "allow-all-requests-from-ip"
        when: { reqProperty: clientIp, equals: 192.168.1.1 }
        action:
          type: allow
```

**Example 4**

This rule blocks requests to path `/block-me`, and blocks every request that matches a `SQLI` or `XSS` pattern. This example includes a WAF traffic filter rules, which references the `SQLI` and `XSS` [WAF Flags](#waf-flags-list), and thus requires a separate license.

```
kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  trafficFilters:
    rules:
      - name: "path-rule"
        when: { reqProperty: path, equals: /block-me }
        action:
          type: block
      - name: "Enable-SQL-Injection-and-XSS-waf-rules-globally"
        when: { reqProperty: path, like: "*" }
        action:
          type: block
          wafFlags: [ SQLI, XSS]
```

**Example 5**

This rule blocks access to OFAC countries:

```
kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  trafficFilters:
    rules:
      - name: block-ofac-countries
        when:
          allOf:
            - reqProperty: tier
              matches: "author|publish"
            - reqProperty: clientCountry
              in:
                - SY
                - BY
                - MM
                - KP
                - IQ
                - CD
                - SD
                - IR
                - LR
                - ZW
                - CU
                - CI
        action: block
```

## Rate Limit Rules {#rate-limits-rules}

Sometimes it is desirable to block traffic if it exceeds a certain rate of incoming requests, perhaps based on a specific condition. Setting a value for the `rateLimit` property limits the rate of those requests that match the rule condition.

Rate limit rules cannot reference WAF flags. They are available to all Sites and Forms customers.

Rate limits are calculated per CDN POP. As an example, assume that POPs in Montreal, Miami, and Dublin experience traffic rates of 80, 90, and 120 request per second respectively, and that the rate limit rule is set to a limit of 100. In that case, only the traffic to Dublin would be rate limited.

### rateLimit Structure {#ratelimit-structure}

| **Property**  | **Type**  | **Default**  | **MEANING**  |
|---|---|---|---|
|  limit |  integer from 10 to 10000     |  required |  Request rate (per CDN POP) in requests per second for which the rule is triggered. |
|  window | integer enum: 1, 10 or 60  | 10  | Sampling window in seconds for which request rate is calculated. The accuracy of counters will depend on the size of the window (bigger window bigger accuracy). For example, one can expect 50% accuracy for the 1 second window and 90% accuracy for the 60 second window. |
|  penalty | integer from 60 to 3600  | 300 (5 minutes) | A period in seconds for which matching requests are blocked (rounded to the nearest minute).  |
|  groupBy | array[Getter] | none | rate limiter counter will be aggregated by a set of request properties (for example, clientIp).  |


### Examples {#ratelimiting-examples}

**Example 1**

This rule blocks a client for 5m when it exceeds an average of 60 req/sec (per CDN POP) in the last 10 sec:

```
kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  trafficFilters:
    rules:
    - name: limit-requests-client-ip
      when:
        reqProperty: tier
        matches: "author|publish"
      rateLimit:
        limit: 60
        window: 10
        penalty: 300
        groupBy:
          - reqProperty: clientIp
      action: block
```

**Example 2**

Block requests on path /critical/resource for 60s when it exceeds an average of 100 req/sec (per CDN POP) in the last 60 sec:

```
kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  trafficFilters:
    rules:
      - name: rate-limit-example
        when: { reqProperty: path, equals: /critical/resource }
        action:
          type: block
        rateLimit: { limit: 100, window: 60, penalty: 60 }
```

## Traffic Filter Rules Alerts {#traffic-filter-rules-alerts}

>[!Note]
>
> This feature is not yet released. To gain access through the early adopter program, email **aemcs-waf-adopter@adobe.com**.

A rule can be configured to send an Actions Center notification if it is triggered 10 times within a 5 minute window, thereby alerting you when certain traffic patterns are occuring so you can take any necessary measures. Learn more about [Actions Center](/help/operations/actions-center.md), including how to setup the required Notification Profiles to receive emails.

![Actions Center Notification](/help/operations/assets/traffic-filter-rules-actions-center-alert.png)


The alert property (currently prefixed with *experimental* since the feature is not yet released) can be applied to the action node for all action types (allow, block, log).

```
kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  trafficFilters:
    rules:
      - name: "path-rule"
        when: { reqProperty: path, equals: /block-me }
        action:
          type: block
          experimental_alert: true
```

## CDN Logs {#cdn-logs}

AEM as a Cloud Service provides access to CDN logs, which are useful for use cases including cache hit ratio optimization, and configuring traffic filter rules. CDN logs appear in the Cloud Manager **Download Logs** dialog, when selecting the Author or Publish service.

CDN logs may be delayed up to five minutes.

The `rules` property describes what traffic filter rules are matched, and has the following pattern:

```
"rules": "match=<matching-customer-named-rules-that-are-matched>,waf=<matching-WAF-rules>,action=<action_type>"
```

For example:

```
"rules": "match=Block-Traffic-under-private-folder,Enable-SQL-injection-everywhere,waf="SQLI,SANS",action=block"
```

The rules behave in the following manner:

* The customer-declared rule name of any matching rules will be listed in the `match` attribute.
* The `action` attribute determines whether the rules had the effect of blocking, allowing, or logging.
* If the WAF is licensed and enabled, the `waf` attribute will list any WAF flags (for example, SQLI) that were detected, regardless of whether the WAF flags were listed in any rules. This is to provide insight into potential new rules to declare.
* If no customer-declared rules match and no waf rules match, the `rules` property will be blank.

As noted earlier, WAF rule matches only appear in CDN logs for CDN misses and passes, not hits.

The example below shows a sample `cdn.yaml` and two CDN log entries:


```
kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  trafficFilters:
    rules:
      - name: "path-rule"
        when: { reqProperty: path, equals: /block-me }
        action: block
      - name: "Enable-SQL-Injection-and-XSS-waf-rules-globally"
        when: { reqProperty: path, like: "*" }
        action:
          type: block
          wafFlags: [ SQLI, XSS ]
```

```
{
"timestamp": "2023-05-26T09:20:01+0000",
"ttfb": 19,
"cli_ip": "147.160.230.112",
"cli_country": "CH",
"rid": "974e67f6",
"req_ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
"host": "example.com",
"url": "/block-me",
"method": "GET",
"res_ctype": "",
"cache": "PASS",
"status": 406,
"res_age": 0,
"pop": "PAR",
"rules": "match=path-rule,action=blocked"
}
```

```

{
"timestamp": "2023-05-26T09:20:01+0000",
"ttfb": 19,
"cli_ip": "147.160.230.112",
"cli_country": "CH",
"req_ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
"rid": "974e67f6",
"host": "example.com",
"url": "/?sqli=%27%29%20UNION%20ALL%20SELECT%20NULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL--%20fAPK",
"method": "GET",
"res_ctype": "image/png",
"cache": "PASS",
"status": 406,
"res_age": 0,
"pop": "PAR",
"rules": "match=Enable-SQL-Injection-and-XSS-waf-rules-globally,waf=SQLI,action=blocked"
}
```

### Log Format {#cdn-log-format}

Below is a list of the field names used in CDN logs, along with a brief description.

 | **Field Name**  | **Description**  |
 |---|---|
 | *timestamp*  | The time the request started, after TLS termination.  |
 | *ttfb*  | Abbreviation for *Time To First Byte*. The time interval between the request started up to the point before the response body started being streamed. |
 | *cli_ip*  |  The client IP address. |
 | *cli_country* | Two-letter [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) alpha-2 country code for the client country. |
 | *rid* |  The value of the request header used to uniquely identify the request. |
 | *req_ua* |  The user agent responsible for making a given HTTP request. |
 | *host*  | The authority that the request is intended for.   |
 | *url*  | The full path, including query parameters.  |
 | *method*  |  HTTP method sent by the client, such as "GET" or "POST". |
 | *res_ctype*  | The Content-Type used to indicate the original media type of the resource.  |
 | *cache*  |  State of the cache. Possible values are HIT, MISS, or PASS |
 | *status*  | The HTTP status code as an integer value.  |
 | *res_age*  | The amount of time (in seconds) a response has been cached (in all nodes).  |
 | *pop*  | Datacenter of the CDN cache server.  |
 | *rules*  | The name of any matching rules.<br><br>Also indicates if the match resulted in a block. <br><br>For example, "`match=Enable-SQL-Injection-and-XSS-waf-rules-globally,waf=SQLI,action=blocked`"<br><br>Empty if no rules matched.  |

## Dashboard Tooling {#dashboard-tooling}

Adobe provides a mechanism to download dashboard tooling onto your computer to ingest CDN logs downloaded via Cloud Manager. With this tooling, you can analyze your traffic to help come up with the appropriate traffic filter rules to declare, including WAF rules.

Dashboard tooling can be cloned directly from the [AEMCS-CDN-Log-Analysis-ELK-Tool](https://github.com/adobe/AEMCS-CDN-Log-Analysis-ELK-Tool) Github repository.

[See the tutorial](#tutorial) for concrete instructions on how to use the dashboard tooling.

## Recommended starter rules {#recommended-starter-rules}

You can copy the recommended rules below into your `cdn.yaml` to get started. Start in log mode, analyze your traffic, and when satisfied, change to block mode. You may want to modify the rules based on the unique characteristics of your website's live traffic.

```
kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev", "stage", "prod"]
data:
  trafficFilters:
    rules:
    #  Block client for 5m when it exceeds 100 req/sec on a time window of 1sec
    - name: limit-requests-client-ip
      when:
        reqProperty: path
        like: '*'
      rateLimit:
        limit: 100
        window: 1
        penalty: 300
        groupBy:
          - reqProperty: clientIp
      action: log
    # Block requests coming from OFAC countries
    - name: block-ofac-countries
      when:
        allOf:
          - { reqProperty: tier, equals: publish }
          - reqProperty: clientCountry
            in:
              - SY
              - BY
              - MM
              - KP
              - IQ
              - CD
              - SD
              - IR
              - LR
              - ZW
              - CU
              - CI
      action: log
    # Enable recommended WAF protections (only works if WAF is licensed enabled for your environment)
    - name: block-waf-flags-globally
      when:
        reqProperty: tier
        matches: "author|publish"
      action:
        type: log
        wafFlags:
          - SANS
          - TORNODE
          - NOUA
          - SCANNER
          - USERAGENT
          - PRIVATEFILE
          - ABNORMALPATH
          - TRAVERSAL
          - NULLBYTE
          - BACKDOOR
          - LOG4J-JNDI
          - SQLI
          - XSS
          - CODEINJECTION
          - CMDEXE
          - NO-CONTENT-TYPE
          - UTF8
    # Disable protection against CMDEXE on /bin (only works if WAF is licensed enabled for your environment)
    - name: allow-cdmexe-on-root-bin
      when:
        allOf:
          - reqProperty: tier
            matches: "author|publish"
          - reqProperty: path
            matches: "^/bin/.*"
      action:
        type: log
        wafFlags:
          - CMDEXE
```

## Tutorial {#tutorial}

[Work through a tutorial](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/security/traffic-filter-and-waf-rules/overview.html) to gain practical knowledge and experience around traffic filter rules.

The tutorial walks you through:

* Setting up the Cloud Manager configuration pipeline
* Using tools to simulate malicious traffic
* Declaring traffic filter rules, including WAF rules
* Analyzing results with dashboard tooling
* Best practices
