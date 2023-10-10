---
title: Configuring Traffic Filter Rules with WAF Rules
description: Use Traffic Filter Rules with WAF Rules to Filter Traffic
exl-id: 6a0248ad-1dee-4a3c-91e4-ddbabb28645c
---
# Configuring Traffic Filter Rules with WAF Rules to Filter Traffic {#configuring-cdn-and-waf-rules-to-filter-traffic}

>[!NOTE]
>
>This feature is not yet generally available. To join the ongoing early adopter program, email **aemcs-waf-adopter@adobe.com**, including the name of your organization and context about your interest in the feature.

Adobe tries to mitigate attacks against customer websites, but it may be useful to proactively filter traffic matching certain patterns so malicious traffic does not reach your application. Possible approaches include:

* Apache layer modules such as `mod_security`
* Configuring traffic filter rules that are deployed to the CDN via Cloud Manager's configuration pipeline

This article describes the traffic filter rules approach. Most of these rules block or allow requests based on request properties and request headers, including IP, paths, and user agent. These rules can be configured by all AEM as a Cloud Service Sites and Forms customers.

Customers who license the WAF (Web Application Firewall) add-on can also configure an additional category of rules called "WAF traffic filter rules" (or WAF rules for short). These WAF rules block requests matching various patterns known to be associated with malicious traffic. Contact your Adobe account team for details about licensing this upcoming capability. Note that no additional license is required during the early adopter program.

Traffic filter rules can be deployed to all cloud environment types (RDE, dev, stage, prod) in production (non-sandbox) programs.

## Setup {#setup}

1. First, create the following folder and file structure the top-level folder in git:

   ```
   config/
        cdn.yaml
   ```

1. `cdn.yaml` should contain metadata as well as a list of traffic filters rules and WAF rules.

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

  The "kind" parameter should be set to "CDN" and the version should be set to the schema version, which is currently "1". See examples further below.


   <!-- Two properties -- `envType` and `envId` -- may be included to limit the scope of the rules. The envType property may have values "dev", "stage", or "prod", while the envId property is the environment (e.g., "53245"). This approach is useful if it is desired to have a single configuration pipeline, even if some environments have different rules. However, a different approach could be to have multiple configuration pipelines, each pointing to different repositories or git branches. -->

1. To configure WAF rules, WAF must be enabled in Cloud Manager, as described below for both the new and existing program scenarios. Note that a separate license must be purchased for WAF.

   1. To Configure WAF on a new Program, check the **WAF-DDOS Protection** check-box in the **Security** tab as shown below. Continue by following the steps described in [Add Production program](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md) to create your program

   1. To Configure WAF on an existing program, select the **Edit program** option by following the steps described in the [Editing Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/editing-programs.md) documentation. Then, in the **Security** tab of the wizard, you can uncheck or check the WAF-DDOS option at any time

1. For environment types other than RDE, execute the Cloud Manager configuration pipeline, which can be configured as described below.

   1. From the pipeline card in your Cloud Manager home page, select **Add Production Pipeline** or **Add Non-Production Pipeline** to launch the add pipeline wizard
   1. Select **Deployment Pipeline** in the configuration tab

      ![Select the Deployment Pipeline option](/help/security/assets/deployment.png)

   1. Give your pipeline a name and select deployment triggers, then select **Continue**
   1. In the **Source Code** tab, select **Targeted deployment**, then select **Config**

      ![Select Targeted deployment](/help/security/assets/target-deployment.png)

   1. Select the repository and branch as needed. If a Config pipeline exists for the selected environment, this selection is disabled.

      ![Overview of a Config Pipeline](/help/security/assets/config-pipeline.png)

      >[!NOTE]
      >
      > Users must be logged in as Deployment Manager in order to configure or run these pipelines.
      > Also, you can configure and run only one Config pipeline per environment.

   1. Set Code Location to where your root configuration is stored (eg. /config).
   1. Select **Save**. Your new pipeline will appear in the pipeline card and can be run when you are ready.
   1. For RDEs, the command line will be used, but RDE is not supported at this time.

## Traffic Filter Rules Syntax {#rules-syntax}

You can configure `traffic filter rules` to match on patterns such as IPs, user agent, request headers, hostname, geo, and url.

Customers who license the WAF offering can also configure a special category of traffic filter rules called `WAF traffic filter rules` (or WAF rules for short) that reference one or more WAF flags, which are listed in its own section below.

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

The format of the traffic filter rules in the cdn.yaml file is described below. See some examples in a later section.


| **Property**   | **Most traffic filter rules**  | **WAF traffic filter rules**  | **Type**  | **Default value**  | **Description**  |
|---|---|---|---|---|---|
| name  | X  | X  | `string`  | -  | Rule name (64 chars long, can only contain alphanumerics and - )  |
| when  | X  | X  | `Condition`  | -  | The basic structure is:<br><br>`{ <getter>: <value>, <predicate>: <value> }`<br><br>See Condition Structure syntax below, which describes the getters, predicates, and how to combine multiple conditions.  |
| action  | X  | X  | `Action` | log  | log, allow, block, log, or action object  Default is log |
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
| reqProperty  | `string`  | Request property.<br><br>One of: `path` , `queryString`, `method`, `tier`, `domain`, `clientIp`, `clientCountry`<br><br>The domain property is a lower-case transformation of the request's host header. It is useful for string comparisons so matches aren't missed due to case sensitivity.<br><br>The `clientCountry` uses two letter codes displayed at [https://en.wikipedia.org/wiki/Regional_indicator_symbol](https://en.wikipedia.org/wiki/Regional_indicator_symbol)  |
| reqHeader  | `string`  | Returns Request Header with specified name  |
| queryParam  | `string` | Returns Query Parameter with specified name  |
| cookie  | `string`  | Returns Cookie with specified name  |

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

### Action Structure {#action-structure}

Specified by `action` field which can be either a string specifying action type (allow, block, log) and assuming default values for all other options or an object where rule type is defined via `type` required field along with other options applicable to that type.

**Action Types**

Actions are prioritized according to their types in the following table, which is ordered to reflect the order actions are executed:

| **Name**  | **Allowed Properties**  | **Meaning**  |
|---|---|---|
|  **allow** | `wafFlags` (optional)  | if wafFlags is not present, stops further rule processing and proceeds to serving response. If wafFlags is present, it disables specified WAF protections and proceeds to further rule processing. |
|  **block** | `status, wafFlags` (optional and mutually exclusive)  | if wafFlags is not present, returns HTTP error bypassing all other properties, error code is defined by status property or defaults to 406. If wafFlags is present, it enables specified WAF protections and proceeds to further rule processing. |
| **log**  | `wafFlags` (optional)  | logs the fact that the rule was triggered, otherwise does not affect the processing. wafFlags has no effect |

### WAF Flags List {#waf-flags-list}

The `wafFlags` property may include the following:

| **Flag ID**  | **Flag Name** | **Description**  |
|---|---|---|
| SQLI  | SQL Injection  | SQL Injection is the attempt to gain access to an application or obtain privileged information by executing arbitrary database queries.  |
| BACKDOOR  |  Backdoor | A backdoor signal is a request which attempts to determine if a common backdoor file is present on the system.  |
| CMDEXE  | Command Execution  | Command Execution is the attempt to gain control or damage a target system through arbitrary system commands by means of user input.  |
| XSS  |  Cross Site Scripting | Cross-Site Scripting is the attempt to hijack a user's account or web-browsing session through malicious JavaScript code.  |
| TRAVERSAL  | Directory Traversal  | Directory Traversal is the attempt to navigate privileged folders throughout a system in hopes of obtaining sensitive information.  |
| USERAGENT  |  Attack tooling |  Attack Tooling is the use of automated software to identify security vulnerabilities or to attempt to exploit a discovered vulnerability. |
| LOG4J-JNDI  | Log4J JNDI  |  Log4J JNDI attacks attempt to exploit the [Log4Shell vulnerability](https://en.wikipedia.org/wiki/Log4Shell) present in Log4J versions earlier than 2.16.0 |
|  AWS SSRF | AWS-SSRF  | Server Side Request Forgery (SSRF) is a request which attempts to send requests made by the web application to target internal systems. AWS SSRF attacks use SSRF to obtain Amazon Web Services (AWS) keys and gain access to S3 buckets and their data.  |
| BHH  | Bad Hop Headers | Bad Hop Headers indicate an HTTP smuggling attempt through either a malformed Transfer-Encoding (TE) or Content-Length (CL) header, or a well-formed TE and CL header  |
| ABNORMALPATH  | Abnormal Path  | Abnormal Path indicates that the original path differs from the normalized path (for example, `/foo/./bar` is normalized to `/foo/bar`)  |
| COMPRESSED  | Compression Detected  | The POST request body is compressed and cannot be inspected. For example, if a "Content-Encoding: gzip" request header is specified and the POST body is not plain text.  |
| DOUBLEENCODING  | Double Encoding  |  Double Encoding checks for the evasion technique of double encoding html characters |
| FORCEFULBROWSING  | Forceful Browsing  | Forceful Browsing is the failed attempt to access admin pages  |
| NOTUTF8  | Invalid Encoding  | Invalid Encoding can cause the server to translate malicious characters from a request into a response, causing either a denial of service or XSS  |
| JSON-ERROR  | JSON Encoding Error  | A POST, PUT, or PATCH request body that is specified as containing JSON within the "Content-Type" request header but contains JSON parsing errors. This is often related to a programming error or an automated or malicious request.  |
| MALFORMED-DATA  | Malformed Data in the request body  | A POST, PUT, or PATCH request body that is malformed according to the "Content-Type" request header. For example, if a "Content-Type: application/x-www-form-urlencoded" request header is specified and contains a POST body that is json. This is often a programming error, automated or malicious request. Requires agent 3.2 or higher.  |
| SANS  | Malicious IP Traffic  | [SANS Internet Storm Center](https://isc.sans.edu/) list of IP addresses that have been reported to have engaged in malicious activity  |
| SIGSCI-IP  | Network Effect  | IP flagged by SignalSciences: Whenever an IP is flagged due to a malicious signal by the decision engine, that IP will be propagated to all customers. Subsequent requests from those IP addresses that contain any additional signal for the duration of the flag are then logged |
| NO-CONTENT-TYPE  | Missing "Content-Type" request header  | A POST, PUT, or PATCH request that does not have a "Content-Type" request header. By default application servers should assume "Content-Type: text/plain; charset=us-ascii" in this case. Many automated and malicious requests may be missing "Content Type".  |
| NOUA  | No User Agent  | Many automated and malicious requests use fake or missing User-Agents to make it difficult to identify the type of device making the requests.  |
| TORNODE  |  Tor Traffic | Tor is software that conceals a user's identity. A spike in Tor traffic can indicate an attacker trying to mask their location.  |
| DATACENTER  | Datacenter Traffic  | Datacenter Traffic is non-organic traffic originating from identified hosting providers. This type of traffic is not commonly associated with a real end user.  |
| NULLBYTE  | Null Byte | Null bytes do not normally appear in a request and indicate that the request is malformed and potentially malicious. |
| IMPOSTOR  |  SearchBot Impostor | Search bot impostor is someone pretending to be a Google or Bing search bot, but who is not legitimate. Note, does not depend on a response by itself, but must be resolved in the cloud first, so it should not be used in a pre rule.  |
| PRIVATEFILE  | Private files  | Private files are usually confidential in nature, such as an Apache `.htaccess` file, or a configuration file which could leak sensitive information  |
| SCANNER  |  Scanner | Identifies popular scanning services and tools  |
| RESPONSESPLIT  | HTTP Response Splitting  | Identifies when CRLF characters are submitted as input to the application to inject headers into the HTTP response  |
| XML-ERROR  | XML Encoding Error  | A POST, PUT, or PATCH request body that is specified as containing XML within the "Content-Type" request header but contains XML parsing errors. This is often related to a programming error or an automated or malicious request.  |

## Considerations {#considerations}

* When two conflicting rules are created, the allow rules will always take precedence over the block rules. For example, if you create a rule to block a specific path and a rule to allow one specific IP address, requests from that IP address on the blocked path will be allowed.

* If a rule is matched and blocked, the CDN responds with a `406` return code.

* The configuration files should not contain secrets since they would be readable by anyone who has access to the git repository.

## Rules Examples {#examples}

Some rule examples follow. See the [rate limit section](#rules-with-rate-limits) further down for examples of rate limiting.

**Example 1**

This rule blocks requests coming from IP 192.168.1.1:

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
         when: { reqProperty: clientIp, equals: "192.168.1.1" }
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

This rule blocks requests to path /block-me, and blocks every request that matches a SQLI or XSS pattern:

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

## Rules with Rate Limits {#rules-with-rate-limits}

Sometimes it is desirable to block traffic matching a rule only if the match exceeds a certain rate over time. Setting a value for the `rateLimit` property limits the rate of those requests that match the rule condition.

### rateLimit Structure {#ratelimit-structure}

| **Property**  | **Type**  | **Default**  | **MEANING**  |
|---|---|---|---|
|  limit |  integer from 10 to 10000     |  required |  Request rate in requests per second for which the rule is triggered. |
|  window | integer enum: 1, 10 or 60  | 10  | Sampling window in seconds for which request rate is calculated.  |
|  penalty | integer from 60 to 3600  | 300 (5 minutes) | A period in seconds for which matching requests are blocked (rounded to the nearest minute).  |
|  groupBy | array[Getter] | none | rate limiter counter will be aggregated by a set of request properties (for example clientIp).  |

### Examples {#ratelimiting-examples}

**Example 1**

This rule blocks a client for 5m when it exceeds 100 req/sec in the last 60 sec:

```
kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  trafficFilters:
    - name: limit-requests-client-ip
      when:
        - reqProperty: tier
        - matches: "author|publish"
      rateLimit:
        limit: 60
        window: 10
        penalty: 300
        groupBy:
          - reqProperty: clientIp
      action: block
```

**Example 2**

Block requests for 60s on path /critical/resource when it exceeds 100 req/sec in the last 60 sec:

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

## CDN Logs {#cdn-logs}

AEM as a Cloud Service provides access to CDN logs, which are useful for use cases including cache hit ratio optimization, and configuring CDN and WAF rules. CDN logs appear in the Cloud Manager **Download Logs** dialog, when selecting the Author or Publish service.

The "rules" property describes what traffic filter rules are matched, and has the following pattern:

```
"rules": "match=<matching-customer-named-rules-that-are-matched>,waf=<matching-WAF-rules>,action=<action_type>"
```

For example:

```
"rules": "match=Block-Traffic-under-private-folder,Enable-SQL-injection-everywhere,waf="SQLI,SANS",action=block"
```

The rules behave in the following manner:

* the customer-declared rule name of any matching rules will be listed in the matches attribute.
* the action attribute details whether the rules had the effect of blocking, allowing, or logging.
* if the WAF is licensed and enabled, the waf attribute will list any waf rules (e.g., SQLI; note that this is independent from the customer-declared name) that were detected, regardless of whether the waf rules were listed in the configuration.
* if no customer-declared rules match and no waf rules match, the rules attribute property will be blank.

In general, matching rules appear in the log entry for all requests to the CDN, regardless of whether it is a CDN hit, pass, or miss. However,  WAF rules appear in the log entry only for requests to the CDN that are considered CDN misses or passes, but not CDN hits.

The example below shows a sample cdn.yaml and two CDN log entries:


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
