---
title: Configuring CDN and Web Application Firewall Rules to Filter Traffic
description: Use the CDN and Web Application Firewall Rules to Filter Malitious Traffic
---

# Configuring CDN and Web Application Firewall Rules to Filter Traffic {#configuring-cdn-and-waf-rules-to-filter-traffic}

>[!NOTE]
>
>This feature is not yet generally available.

Adobe will try to mitigate attacks against customer websites, but itt may be useful to proactively filter requests matching certain patterns so malicious traffic does not reach your application. Possible approaches include:

* Apache layer modules such as `mod_security`
* Configuring rules that are deployed to the CDN using Cloud Manager's configuration pipeline. 

This article describes the latter approach, which offers two categories of rules:

1. **CDN rules**: block or allow requests based on request properties and request headers, including IP, paths, and user agent. These rules can be configured by all AEM as a Cloud Service customers
1. **WAF** (Web Application Firewall) rules: block requests that matches various patterns known to be associated with malicious traffic. These rules can be configured by customers who license the WAF add-on.

These rules can be deployed to all cloud environment types (RDE, dev, stage, prod) in production (non-sandbox) programs.

## Setup {#setup}

1. First, create the following folder and file structure the top level folder in git:

   ```
   config/
        cdn/
           cdn.yaml
           _config.yaml
   ```

1. `_config.yaml` describes the type of rules, the version, and the environment, as illustrated in the snippet below:

   ```
   kind: "CDN"
   version: "1"
   envType: "dev"
   ```

1. `cdn.yaml` should include a list of CDN rules and WAF rules, as described in sections below
1. In order to match WAF rules, WAF must be enabled in Cloud Manager, as described below for both the new and existing program scenarios. Note that a separate license must be purchased for WAF.

   1. In order to Configure WAF on a new Program, check the **WAF-DDOS Protection** check-box in the **Security** tab as shown below. Continue by following the steps described in [Add Production program](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md) to create your program

   1. In order to Configure WAF on an existing program, select the **Edit program** option by following the steps described in the [Editing Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/editing-programs.md) documentation. Then, in the **Security** tab of the wizard, you can un-check or check the WAF-DDOS option at any time

1. For environment types other than RDE, execute the Cloud Manager configuration pipeline, which can be configured as described below. 

   1. From the pipeline card in your Cloud Manager home page, select **Add Production Pipeline** or **Add Non-Production Pipeline** to launch the add pipeline wizard
   1. Select **Deployment Pipeline** in the configuration tab 

      ![Select the Deployment Pipeline option](/help/security/assets/deployment.png)

   1. Give your pipeline a name and select deployment triggers, then select **Continue** 
   1. In the **Source Code** tab, select **Targeted deployment**, then select **Config**

      ![Selet Targeted deployment](/help/security/assets/target-deployment.png)

   1. Select the repository and branch as needed. Note that if a Config pipeline already exists for the selected environment, this selection will be disabled.

      ![Overview of a Config Pipeline](/help/security/assets/config-pipeline.png)
      
      >[!NOTE]
      >
      >You can configure and run only one Config pipeline per environment.

   1. Select **Save**. Your new pipeline will appear in the pipeline card and can be run when you are ready. 
   1. For RDE, use the command line, as described in the section below.

## Rules Syntax {#rules-syntax}

The format of the rules is described below, followed by some examples in a subsequent section.

| **Property**   | **CND Rules**  | **WAF Rules**  | **Type**  | **Default**  | **Description**  |
|---|---|---|---|---|---|
| name  | X  | X  | `string`  | -  | Rule name (64 chars long, can only contains alphanumerics and - )  |
| when  | X  | X  | `Condition`  | -  | The basic structure is:<br><br>`{ <getter>: <value>, <predicate>: <value> }`<br><br>See Condition Structure syntax below, which describes the getters, predicates, and how to combine multiple conditions.  |
| action  | X  | X  | `Enum`  | log (CDN rules)  | For CDN rules: allow, block, log. Default is log.<br><br>For WAF rules: `enableWafRules`, `disableWafRules`, log. No default.  |
|  rateLimit | X  |   | `RateLimit`  | not defined  | Rate limiting configuration. Rate limiting is disabled if not defined.<br><br>There is a separate section further below describing the rateLimit syntax, along with examples.  |
| wafRules  |   |  X | `array[Enum]` | -  | List of WAF rules that should be enabled or disabled.<br><br>Examples include SQLI and XSS. See waf Rules list below for a full list.  |

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
|  **equals** | `string`  | true if getter result equals to provided value  |
|  **doesNotEqual** | `string`  | true if getter result not equal to provided value  |
| **like**  | `string`  | true if getter result matches provided pattern  |
| **notLike**  | `string`  | true if getter result does not match provided pattern  |
| **matches**  | `string`  | true if getter result matches provided regex  |
| **doesNotMatch**  | `string`  | true if getter result does not match provided regex  |
| **in**  | `array[string]`  | true if provided list contains getter result  |
|  **notIn** | `array[string]`  | true if provided list does not contain getter result  |

**wafRules List**

The `waRules` property may include the following rules:

| **Rule ID**  | **Rule Name** | **Description**  |
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
| ABNORMALPATH  | Abnormal Path  | Abnormal Path indicates the original path differs from the normalized path (e.g., `/foo/./bar` is normalized to `/foo/bar`)  |
| COMPRESSED  | Compression Detected  | The POST request body is compressed and cannot be inspected. For example, if a "Content-Encoding: gzip" request header is specified and the POST body is not plain text.  |
| DOUBLEENCODING  | Double Encoding  |  Double Encoding checks for the evasion technique of double encoding html characters |
| FORCEFULBROWSING  | Forceful Browsing  | Forceful Browsing is the failed attempt to access admin pages  |
| NOTUTF8  | Invalid Encoding  | Invalid Encoding can cause the server to translate malicious characters from a request into a response, causing either a denial of service or XSS  |
| JSON-ERROR  | JSON Encoding Error  | A POST, PUT, or PATCH request body that is specified as containing JSON within the "Content-Type" request header but contains JSON parsing errors. This is often related to a programming error or an automated or malicious request.  |
| MALFORMED-DATA  | Malformed Data in the request body  | A POST, PUT or PATCH request body that is malformed according to the "Content-Type" request header. For example, if a "Content-Type: application/x-www-form-urlencoded" request header is specified and contains a POST body that is json. This is often a programming error, automated or malicious request. Requires agent 3.2 or higher.  |
| SANS  | Malicious IP Traffic  | [SANS Internet Storm Center](https://isc.sans.edu/) list of IP addresses that have been reported to have engaged in malicious activity  |
| SIGSCI-IP  | Network Effect  | IP flagged by SignalSciences: Whenever an IP is flagged due to a malicious signal by our decision engine, that IP will be propagated to all customers. We then log subsequent requests from those IP addresses that contain any additional signal for the duration of the flag.  |
| NO-CONTENT-TYPE  | Missing "Content-Type" request header  | A POST, PUT or PATCH request that does not have a "Content-Type" request header. By default application servers should assume "Content-Type: text/plain; charset=us-ascii" in this case. Many automated and malicious requests may be missing "Content Type".  |
| NOUA  | No User Agent  | Many automated and malicious requests use fake or missing User-Agents to make it difficult to identify the type of device making the requests.  |
| TORNODE  |  Tor Traffic | Tor is software that conceals a user's identity. A spike in Tor traffic can indicate an attacker trying to mask their location.  |
| DATACENTER  | Datacenter Traffic  | Datacenter Traffic is non-organic traffic originating from identified hosting providers. This type of traffic is not commonly associated with a real end user.  |
| NULLBYTE  | Null Byte | Null bytes do not normally appear in a request and indicate the request is malformed and potentially malicious. |
| IMPOSTOR  |  SearchBot Impostor | Search bot impostor is someone pretending to be a Google or Bing search bot, but who is not legitimate. Note, doesn not depend on a response per se, but needs to be resolved in the cloud first, so it should not be used in a pre rule.  |
| PRIVATEFILE  | Private files  | Private files are usually confidential in nature, such as an Apache `.htaccess` file, or a configuration file which could leak sensitive information  |
| SCANNER  |  Scanner | Identifies popular scanning services and tools  |
| RESPONSESPLIT  | HTTP Response Splitting  | Identifies when CRLF characters are submitted as input to the application to inject headers into the HTTP response  |
| XML-ERROR  | XML Encoding Error  | A POST, PUT, or PATCH request body that is specified as containing XML within the "Content-Type" request header but contains XML parsing errors. This is often related to a programming error or an automated or malicious request.  |