---
title: Logging for AEM as a Cloud Service
description: Learn how to use Logging for AEM as a Cloud Service to configure global parameters for the central logging service, specific settings for the individual services or how to request data logging.
exl-id: 262939cc-05a5-41c9-86ef-68718d2cd6a9
feature: Log Files, Developing
role: Admin, Architect, Developer
---
# Logging for AEM as a Cloud Service {#logging-for-aem-as-a-cloud-service}

AEM as a Cloud Service is a platform for customers to include custom code to create unique experiences for their customer base. With this in mind, the logging service is a critical function to debug and understand code execution on local development, and cloud environments, particularly the AEM as a Cloud Service's Dev environments.

AEM as a Cloud Service logging settings and log levels are managed in configuration files that are stored as part of the AEM project in Git, and deployed as part of the AEM project via Cloud Manager. Logging in AEM as a Cloud Service can be broken into three logical sets:

* AEM logging, which performs logging at the AEM application level
* Apache HTTPD Web Server/Dispatcher logging, which performs logging of the web server and Dispatcher on the Publish tier.
* CDN logging, which as its name indicates, performs logging at the CDN. This feature is being gradually rolled out to customers in early September.

## AEM Logging {#aem-logging}

Logging at the AEM application level, is handled by three logs:

1. AEM Java logs, which render Java logging statements for the AEM application.
1. HTTP Request logs, which log information about HTTP requests and their responses served by AEM
1. HTTP Access logs, which log summarized information and HTTP requests served by AEM

>[!NOTE]
>
>HTTP requests that are served from Publish tier's Dispatcher cache or upstream CDN are not reflected in these logs.

## AEM Java Logging {#aem-java-logging}

AEM as a Cloud Service's provides access to Java log statements. Developers of applications for AEM should follow general Java logging best practices, logging pertinent statements about the execution of custom code, at the following log levels:

<table>
<tr>
<td>
<b>AEM Environment</b></td>
<td>
<b>Log Level</b></td>
<td>
<b>Description</b></td>
<td>
<b>Log Statement Availability</b></td>
</tr>
<tr>
<td>
Development</td>
<td>
DEBUG</td>
<td>
Describes what is happening in the application.<br>
When DEBUG logging is active, statements providing a clear picture of what activities occur and any key parameters that affect processing are logged.</td>
<td>
<ul>
<li> Local Development</li>
<li>Development</li>
</ul></td>
</tr>
<tr>
<td>
Stage</td>
<td>
WARN</td>
<td>
Describes conditions that have the potential to become errors.<br>
When WARN logging is active, only statements indicating conditionals that are approaching sub-optimality are logged.</td>
<td>
<ul>
<li> Local Development</li>
<li>Development</li>
<li>Stage</li>
</ul></td>
</tr>
<tr>
<td>
Production</td>
<td>
ERROR</td>
<td>
Describes conditions that indicate a failure, and need to resolve.<br>
When ERROR logging is active, only statements indicating failures are logged. ERROR log statements indicate a serious issue that should be resolved as soon as possible.</td>
<td>
<ul>
<li> Local Development</li>
<li>Development</li>
<li>Stage</li>
<li>Production</li>
</ul></td>
</tr>
</table>

While Java logging supports several other levels of logging granularity, AEM as a Cloud Service recommends using the three levels described above. 

AEM Log levels are set per environment type via OSGi configuration, which in turn are committed to Git, and deployed via Cloud Manager to AEM as a Cloud Service. Because of this, it is best to keep log statements consistent and well known for environment types to ensure the logs available via AEM as Cloud Service are available at the optimal log level without requiring redeployment of application with the updated log level configuration.

**Example Log Output**

```
22.06.2020 18:33:30.120 [cm-p12345-e6789-aem-author-86657cbb55-xrnzq] *ERROR* [qtp501076283-1809] io.prometheus.client.dropwizard.DropwizardExports Failed to get value from Gauge
22.06.2020 18:33:30.229 [cm-p12345-e6789-aem-author-86657cbb55-xrnzq] *INFO* [qtp501076283-1805] org.apache.sling.auth.core.impl.SlingAuthenticator getAnonymousResolver: Anonymous access not allowed by configuration - requesting credentials
22.06.2020 18:33:30.370 [cm-p12345-e6789-aem-author-86657cbb55-xrnzq] *INFO* [73.91.59.34 [1592850810364] GET /libs/granite/core/content/login.html HTTP/1.1] org.apache.sling.i18n.impl.JcrResourceBundle Finished loading 0 entries for 'en_US' (basename: <none>) in 4ms
22.06.2020 18:33:30.372 [cm-p12345-e6789-aem-author-86657cbb55-xrnzq] *INFO* [FelixLogListener] org.apache.sling.i18n Service [5126, [java.util.ResourceBundle]] ServiceEvent REGISTERED
22.06.2020 18:33:30.372 [cm-p12345-e6789-aem-author-86657cbb55-xrnzq] *WARN* [73.91.59.34 [1592850810364] GET /libs/granite/core/content/login.html HTTP/1.1] libs.granite.core.components.login.login$jsp j_reason param value 'unknown' cannot be mapped to a valid reason message: ignoring
```

**Log Format**

<table>
<tbody>
<tr>
<td>Date and time</td>
<td>29.04.2020 21:50:13.398</td>
</tr>
<tr>
<td>AEM as a Cloud Service node ID</td>
<td>[cm-p1234-e5678-aem-author-59555cb5b8-q7l9s]</td>
</tr>
<tr>
<td>Log level</td>
<td>DEBUG</td>
</tr>
<tr>
<td>Thread</td>
<td>qtp2130572036-1472</td>
</tr>
<tr>
<td>Java class</td>
<td>com.example.approval.workflow.impl.CustomApprovalWorkflow</td>
</tr>
<tr>
<td>Log message</td>
<td>No specified approver, defaulting to [ Creative Approvers user group ]</td>
</tr>
</tbody>
</table>

### Configuration Loggers {#configuration-loggers}

AEM Java logs are defined as OSGi configuration, and thus target specific AEM as a Cloud Service environments using run mode folders.

Configure java logging for custom Java packages via OSGi configurations for the Sling LogManager factory. There are three supported configuration properties:

| OSGi Configuration property  | Description  |
|---|---|
| `org.apache.sling.commons.log.names` | The Java packages for which to collect log statements.  |
| `org.apache.sling.commons.log.level` | The log level at which to log the Java packages, specified by `org.apache.sling.commons.log.names`  |
| `org.apache.sling.commons.log.file`| Specify the target for the output: `logs/error.log`|

Changing other LogManager OSGi configuration properties may result in availability issues in AEM as a Cloud Service.

The following are examples of the recommended logging configurations (using the placeholder Java package of `com.example`) for the three AEM as a Cloud Service environment types.

### Development {#development}

/apps/my-app/config/org.apache.sling.commons.log.LogManager.factory.config-example.cfg.json

```
{
    "org.apache.sling.commons.log.names": ["com.example"],
    "org.apache.sling.commons.log.level": "debug"
    "org.apache.sling.commons.log.file": "logs/error.log"
}
```

### Stage {#stage}

/apps/my-app/config.stage/org.apache.sling.commons.log.LogManager.factory.config-example.cfg.json

```
{
    "org.apache.sling.commons.log.names": ["com.example"],
    "org.apache.sling.commons.log.level": "warn"
    "org.apache.sling.commons.log.file": "logs/error.log"
}
```

### Production {#productiomn}

/apps/my-app/config.prod/org.apache.sling.commons.log.LogManager.factory.config-example.cfg.json

```
{
    "org.apache.sling.commons.log.names": ["com.example"],
    "org.apache.sling.commons.log.level": "error"
    "org.apache.sling.commons.log.file": "logs/error.log"
}
```

## AEM HTTP Request Logging {#aem-http-request-logging}

AEM as a Cloud Service's HTTP request logging provides insight into the HTTP requests made to AEM and their HTTP responses in time order. This log is helpful to understand the HTTP Requests made to AEM and the order they are processed and responded to.

The key to understanding this log is mapping the HTTP request and response pairs by their IDs, denoted by the numeric value in the brackets. Often requests and their corresponding responses have other HTTP requests and responses interjected between them in the log.

**Example Log**

```
29/Apr/2020:19:14:21 +0000 [137] > POST /conf/global/settings/dam/adminui-extension/metadataprofile/ HTTP/1.1 [cm-p1234-e5678-aem-author-59555cb5b8-q7l9s]
...
29/Apr/2020:19:14:22 +0000 [139] > GET /mnt/overlay/dam/gui/content/processingprofilepage/metadataprofiles/editor.html/conf/global/settings/dam/adminui-extension/metadataprofile/main HTTP/1.1 [cm-p1234-e5678-aem-author-59555cb5b8-q7l9s]
...
29/Apr/2020:19:14:21 +0000 [137] <- 201 text/html 111ms [cm-p1234-e5678-aem-author-59555cb5b8-q7l9s]
...
29/Apr/2020:19:14:22 +0000 [139] <- 200 text/html;charset=utf-8 637ms [cm-p1234-e5678-aem-author-59555cb5b8-q7l9s]
```

**Log Format**

<table>
<tbody>
<tr>
<td>Date and time</td>
<td>29/Apr/2020:19:14:21 +0000</td>
</tr>
<tr>
<td>Request/Response Pair ID</td>
<td><code>[137]</code></td>
</tr>
<tr>
<td>HTTP Method</td>
<td>POST</td>
</tr>
<tr>
<td>URL</td>
<td>/conf/global/settings/dam/adminui-extension/metadataprofile/</td>
</tr>
<tr>
<td>Protocol</td>
<td>HTTP/1.1
</td>
</tr>
<tr>
<td>AEM as a Cloud Service node ID</td>
<td>[cm-p1234-e5678-aem-author-59555cb5b8-q7l9s]</td>
</tr>
</tbody>
</table>

### Configuring the Log {#configuring-the-log}

The AEM HTTP Request log is not configurable in AEM as a Cloud Service.

## AEM HTTP Access Logging {#aem-http-access-logging}

AEM as Cloud Service HTTP access logging shows HTTP requests in time order. Each log entry represents the HTTP Request that accesses AEM.

This log is helpful to quickly understand what HTTP requests are being made to AEM, if they succeed by looking at the accompanying HTTP response status code, and how long the HTTP request took to complete. This log can also be helpful to debug a specific user's activity by filtering log entries by Users.

**Example Log Output**

```
cm-p1234-e26813-aem-author-59555cb5b8-8kgr2 - example@adobe.com 30/Apr/2020:17:37:14 +0000  "GET /libs/granite/ui/references/clientlibs/references.lc-5188e85840c529149e6cd29d94e74ad5-lc.min.css HTTP/1.1" 200 1141 "https://author-p10711-e26813.adobeaemcloud.com/mnt/overlay/dam/gui/content/assets/metadataeditor.external.html?item=/content/dam/en/images/example.jpeg&_charset_=utf8" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
cm-p1234-e26813-aem-author-59555cb5b8-8kgr2 - example@adobe.com 30/Apr/2020:17:37:14 +0000  "GET /libs/dam/gui/coral/components/admin/customthumb/clientlibs.lc-60e4443805c37afa0c74b674b141f1df-lc.min.css HTTP/1.1" 200 809 "https://author-p10711-e26813.adobeaemcloud.com/mnt/overlay/dam/gui/content/assets/metadataeditor.external.html?item=/content/dam/en/images/example.jpeg&_charset_=utf8" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
cm-p1234-e26813-aem-author-59555cb5b8-8kgr2 - example@adobe.com 30/Apr/2020:17:37:14 +0000  "GET /libs/dam/gui/coral/components/admin/metadataeditor/clientlibs/metadataeditor.lc-4a2226d8232f8b7ab27d24820b9ddd64-lc.min.js HTTP/1.1" 200 7965 "https://author-p10711-e26813.adobeaemcloud.com/mnt/overlay/dam/gui/content/assets/metadataeditor.external.html?item=/content/dam/en/images/example.jpeg&_charset_=utf8" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
```

| AEM as a Cloud Service Node ID  | cm-p1235-e2644-aem-author-59555cb5b8-8kgr2  |
|---|---|
| IP address of the Client  | -  |
| User  |  myuser@adobe.com |
| Date and time  | 30/Apr/2020:17:37:14 +0000  |
|  HTTP method | GET  |
| URL  |  `/libs/granite/ui/references/clientlibs/references.lc-5188e85840c529149e6cd29d94e74ad5-lc.min.css` |
| Protocol  | HTTP/1.1  |
| HTTP response status  | 200  |
| Size of the response body in bytes  | 1141  |
| Referrer  | `"https://author-p1234-e4444.adobeaemcloud.com/mnt/overlay/dam/gui/content/assets/metadataeditor.external.html?item=/content/dam/wknd/en/adventures/surf-camp-in-costa-rica/adobestock_266405335.jpeg&_charset_=utf8"`  |
| User agent  | `"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"`  |

### Configuring the HTTP Access Log {#configuring-the-http-access-log}

The HTTP Access log is not configurable in AEM as a Cloud Service.

## Apache Web Server and Dispatcher Logging {#apache-web-server-and-dispatcher-logging}

AEM as a Cloud Service provides three logs for the Apache Web Servers and dispatcher layer on the Publish:

* Apache HTTPD Web Server Access log
* Apache HTTPD Web Server Error log
* Dispatcher log

These logs are only available for the Publish tier.

This set of logs provides insights into HTTP requests to the AEM as a Cloud Service Publish tier prior to those requests reaching the AEM application. This is important to understand as, ideally, most HTTP requests to the Publish tier servers are served by content that is cached by the Apache HTTPD Web Server and AEM Dispatcher, and never reach the AEM application itself. Thus there are no log statements for these requests in AEM's Java, Request or Access logs.

### Apache HTTPD Web Server Access Log {#apache-httpd-web-server-access-log}

The Apache HTTP Web Server access log provides statements for each HTTP request that reaches the Publish tier's Web server/Dispatcher. Requests that are served from an upstream CDN are not reflected in these logs.

See information about the error log format in the [official apache documentation](https://httpd.apache.org/docs/2.4/logs.html#accesslog).

**Example Log Output**

```
cm-p1234-e5678-aem-publish-b86c6b466-qpfvp - - 17/Jul/2020:09:14:41 +0000  "GET /etc.clientlibs/wknd/clientlibs/clientlib-site/resources/images/favicons/favicon-32.png HTTP/1.1" 200 715 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0"
cm-p1234-e5678-aem-publish-b86c6b466-qpfvp - - 17/Jul/2020:09:14:41 +0000  "GET /etc.clientlibs/wknd/clientlibs/clientlib-site/resources/images/favicons/favicon-512.png HTTP/1.1" 200 9631 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0"
cm-p1234-e5678-aem-publish-b86c6b466-qpfvp - - 17/Jul/2020:09:14:42 +0000  "GET /etc.clientlibs/wknd/clientlibs/clientlib-site/resources/images/country-flags/US.svg HTTP/1.1" 200 810 "https://publish-p6902-e30226.adobeaemcloud.com/content/wknd/us/en.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0"
```

**Log Format**

<table>
<tbody>
<tr>
<td>AEM as a Cloud Servide node ID</td>
<td>cm-p1234-e26813-aem-publish-5c787687c-lqlxr</td>
</tr>
<tr>
<td>IP Address of the client</td>
<td>-</td>
</tr>
<tr>
<td>User</td>
<td>-</td>
</tr>
<tr>
<td>Date and time</td>
<td>01/May/2020:00:09:46 +0000</td>
</tr>
<tr>
<td>HTTP Method</td>
<td>GET</td>
</tr>
<tr>
<td>URL</td>
<td>/content/example.html</td>
</tr>
<tr>
<td>Protocol</td>
<td>HTTP/1.1</td>
</tr>
<tr>
<td>HTTP Response status</td>
<td>200</td>
</tr>
<tr>
<td>Size</td>
<td>310</td>
</tr>
<tr>
<td>Referer</td>
<td>-</td>
</tr>
<tr>
<td>User agent</td>
<td>"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"</td>
</tr>
</tbody>
</table>

### Configuring the Apache HTTPD Web Server Access Log {#configuring-the-apache-httpd-webs-server-access-log}

This log is not configurable in AEM as a Cloud Service.

## Apache HTTPD Web Server Error Log {#apache-httpd-web-server-error-log}

The Apache HTTP Web Server error log provides statements for each error in the Publish tier's Web server/Dispatcher.

See information about the error log format in the [official apache documentation](https://httpd.apache.org/docs/2.4/logs.html#errorlog).

**Example Log Output**

```
Fri Jul 17 02:19:48.093820 2020 [mpm_worker:notice] [pid 1:tid 140272153361288] [cm-p1234-e30226-aem-publish-b86c6b466-b9427] AH00292: Apache/2.4.43 (Unix) Communique/4.3.4-20200424 mod_qos/11.63 configured -- resuming normal operations
Fri Jul 17 02:19:48.093874 2020 [core:notice] [pid 1:tid 140272153361288] [cm-p1234-e30226-aem-publish-b86c6b466-b9427] AH00094: Command line: 'httpd -d /etc/httpd -f /etc/httpd/conf/httpd.conf -D FOREGROUND -D ENVIRONMENT_PROD'
Fri Jul 17 02:29:34.517189 2020 [mpm_worker:notice] [pid 1:tid 140293638175624] [cm-p1234-e30226-aem-publish-b496f64bf-5vckp] AH00295: caught SIGTERM, shutting down
```

**Log Format**

<table>
<tbody>
<tr>
<td>Date and time</td>
<td>Fri Jul 17 02:16:42.608913 2020</td>
</tr>
<tr>
<td>Event Level</td>
<td>[mpm_worker:notice]</td>
</tr>
<tr>
<td>Process ID</td>
<td>[pid 1:tid 140715149343624]</td>
</tr>
<tr>
<td>Pod name</td>
<td>[cm-p1234-e56789-aem-publish-b86c6b466-qpfvp]</td>
</tr>
<tr>
<td>Message</td>
<td>AH00094: Command line: 'httpd -d /etc/httpd -f /etc/httpd/conf/httpd.conf -D FOREGROUND -D </td>
</tr>
</tbody>
</table>

### Configuring the Apache HTTPD Web Server Error Log {#configuring-the-apache-httpd-web-server-error-log}

The mod_rewrite log levels are defined by the variable REWRITE_LOG_LEVEL in the file `conf.d/variables/global.var`.

It can be set to error, warn, info, debug and trace1 - trace8, with a default value of warn. To debug your RewriteRules, it is recommended to raise the log level to trace2. It's recommended to debug rewrite rules using the [Dispatcher SDK](../../dispatcher/validation-debug.md). The maximal log level for AEM as a Cloud Service is `debug`. Thus it is currently not effectively possible to debug rewrite rules in the cloud.

See the [mod_rewrite module documentation](https://httpd.apache.org/docs/current/mod/mod_rewrite.html#logging) for more information.

To set the log level per environment, use the appropriate conditional branch in the global.var file, as described below:

```
Define REWRITE_LOG_LEVEL debug
  
<IfDefine ENVIRONMENT_STAGE>
  ...
  Define REWRITE_LOG_LEVEL warn
  ...
</IfDefine>
<IfDefine ENVIRONMENT_PROD>
  ...
  Define REWRITE_LOG_LEVEL error
  ...
</IfDefine>
```

## Dispatcher Log {#dispatcher-log}

**Example**

```
[17/Jul/2020:23:48:06 +0000] [I] [cm-p12904-e25628-aem-publish-6c5f7c9dbd-mzcvr] "GET /content/wknd/us/en/adventures.html" - 475ms [publishfarm/0] [action miss] "publish-p12904-e25628.adobeaemcloud.com"
[17/Jul/2020:23:48:07 +0000] [I] [cm-p12904-e25628-aem-publish-6c5f7c9dbd-mzcvr] "GET /content/wknd/us/en/adventures/climbing-new-zealand/_jcr_content/root/responsivegrid/carousel/item_1571266094599.coreimg.jpeg/1473680817282/sport-climbing.jpeg" 302 10ms [publishfarm/0] [action none] "publish-p12904-e25628.adobeaemcloud.com"
[17/Jul/2020:23:48:07 +0000] [I] [cm-p12904-e25628-aem-publish-6c5f7c9dbd-mzcvr] "GET /content/wknd/us/en/adventures/ski-touring-mont-blanc/_jcr_content/root/responsivegrid/carousel/item_1571168419252.coreimg.jpeg/1572047288089/adobestock-238230356.jpeg" 302 11ms [publishfarm/0] [action none] "publish-p12904-e25628.adobeaemcloud.com"
```

**Log Format**

<table>
<tbody>
<tr>
<td>Date and time</td>
<td>[17/Jul/2020:23:48:16 +0000]</td>
</tr>
<tr>
<td>Pod Name</td>
<td>[cm-p12904-e25628-aem-publish-6c5f7c9dbd-mzcvr]</td>
</tr>
<tr>
<td>Protocol</td>
<td>GET</td>
</tr>
<tr>
<td>URL</td>
<td>/content/experience-fragments/wknd/language-masters/en/contributors/sofia-sjoeberg/master/_jcr_content/root/responsivegrid/image.coreimg.100.500.jpeg/1572236359031/ayo-ogunseinde-237739.jpeg</td>
</tr>
<tr>
<td>Dispatcher response status code</td>
<td>/content/experience-fragments/wknd/language-masters/en/contributors/sofia-sjoeberg/master/_jcr_content/root/responsivegrid/image.coreimg.100.500.jpeg/1572236359031/ayo-ogunseinde-237739.jpeg</td>
</tr>
<tr>
<td>Duration</td>
<td>1949ms</td>
</tr>
<tr>
<td>Farm</td>
<td>[publishfarm/0]</td>
</tr>
<tr>
<td>Cache status</td>
<td>[action miss]</td>
</tr>
<tr>
<td>Host</td>
<td>"publish-p12904-e25628.adobeaemcloud.com"</td>
</tr>
</tbody>
</table>

### Configuring the Dispatcher Error Log {#configuring-the-dispatcher-error-log}

The dispatcher log levels is defined by the variable DISP_LOG_LEVEL in the file `conf.d/variables/global.var`.

It can be set to error, warn, info, debug and trace1, with a default value of warn.

While Dispatcher logging supports several other levels of logging granularity, the AEM as a Cloud Service recommends using the levels described below.

To set the log level per environment, use the appropriate conditional branch in the `global.var` file, as described below:

```
Define DISP_LOG_LEVEL debug
  
<IfDefine ENVIRONMENT_STAGE>
  ...
  Define DISP_LOG_LEVEL warn
  ...
</IfDefine>
<IfDefine ENVIRONMENT_PROD>
  ...
  Define DISP_LOG_LEVEL error
  ...
</IfDefine>
```

>[!NOTE]
>
>For AEM as a Cloud Service environments, debug is the maximal verbosity level. The trace log level is not supported so you should avoid setting it when working in cloud environments.

## CDN Log {#cdn-log}

AEM as a Cloud Service provides access to CDN logs, which are useful for use cases including cache hit ratio optimization. The CDN log format cannot be customized and there is no concept of setting it to different modes such as info, warn, or error.

 **Example**

 ```
 {
 "timestamp": "2023-05-26T09:20:01+0000",
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
 "rules": "match=Enable-SQL-Injection-and-XSS-waf-rules-globally,waf=SQLI,action=blocked"
 }
 ```

 **Log Format**

 The CDN logs are distinct from the other logs in that it adheres to a json format.

 | **Field Name**  | **Description**  |
 |---|---|
 | *timestamp*  | The time the request started, after TLS termination  |
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
 | *rules*  | The names of any matching [traffic filter rules](/help/security/traffic-filter-rules-including-waf.md) and WAF flags, also indicating if the match resulted in a block. Empty if no rules matched.  |
 

## How to Access Logs {#how-to-access-logs}

### Cloud Environments {#cloud-environments}

AEM as a Cloud Service logs for cloud services can be accessed either by downloading through the Cloud Manager interface or by tailing logs at the command line using the using the Adobe I/O command line interface. For more information, see the [Cloud Manager logging documentation](/help/implementing/cloud-manager/manage-logs.md).

### Logs for Additional Publish Regions {#logs-for-additional-publish-regions}

If additional publish regions are enabled for a particular environment, logs for each region will be available to download from Cloud Manager, as mentioned above.

The AEM logs and the dispatcher logs for the additional publish regions will specify the region in the first 3 letters after the environment id, as exemplified by **nld2** in the sample below, which refers to an additional AEM publish instance located in the Netherlands:

```
cm-p7613-e12700-nld2-aem-publish-bcbb77549-5qmmt 127.0.0.1 - 07/Nov/2023:23:57:11 +0000 "HEAD /libs/granite/security/currentuser.json HTTP/1.1" 200 - "-" "Java/11.0.19"

```

### Local SDK {#local-sdk}

AEM as a Cloud Service SDK provides logs files to support local development.

AEM logs are located in the folder `crx-quickstart/logs`, where the following logs can be viewed:

* AEM Java log: `error.log`
* AEM HTTP Request log: `request.log`
* AEM HTTP Access log: `access.log`

Apache layer logs, including dispatcher, are in the Docker container which holds the Dispatcher. See the [Dispatcher documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/content-delivery/disp-overview.html) for information on how to start the Dispatcher. 

To retrieve the logs:

1. At the command line, type `docker ps` to list your containers
1. To log into the container, type "`docker exec -it <container> /bin/sh`", where `<container>` is the dispatcher container id from the previous step
1. Navigate to the cache root under `/mnt/var/www/html`
1. The logs are under `/etc/httpd/logs`
1. Inspect the logs: they can be accessed under the folder XYZ, where the following logs can be viewed:
   * Apache HTTPD Web server access log - `httpd_access.log`
   * Apache HTTPD Web server error logs - `httpd_error.log`
   * Dispatcher logs - `dispatcher.log`

Logs are also directly printed to the terminal output. Most of the time, these logs should be DEBUG, which can be accomplished by passing in the Debug level as a parameter when running Docker. For example:

`DISP_LOG_LEVEL=Debug ./bin/docker_run.sh out docker.for.mac.localhost:4503 8080`

## Debugging Production and Stage {#debugging-production-and-stage}

In exceptional circumstances, log levels need to be changed to log at a finer granularity in Stage or Production environments. 

While this is possible, it requires changes to the log levels in the configuration files in Git from Warn and Error to Debug, and performing a deployment to AEM as a Cloud Service to register these configuration changes with the environments. 

Depending on the traffic and the amount of log statement written by Debug, this may result in an adverse performance impact on the environment, therefore, it's recommended that changes to Stage and Production debug levels are:

* Done judiciously, and only when absolutely necessary
* Reverted to the appropriate levels and re-deployed as soon as possible

## Log Forwarding {#log-forwarding}

While logs can be downloaded from Cloud Manager, some organizations find it benficial to forward those logs to a preferred logging destination. AEM supports streaming logs to the following destinations:

* Azure Blob Storage
* Datadog
* HTTPD
* Elasticsearch (and OpenSearch)
* Splunk

Refer to the [Log Forwarding article](/help/implementing/developing/introduction/log-forwarding.md) for details on how to configure this feature.

>[!NOTE]
>
>Log forwarding for sandbox program environments is not supported.
