---
title: Logging
description: Learn how to configure global parameters for the central logging service, specific settings for the individual services or how to request data logging.
---

# Logging {#logging}

AEM as a Cloud Service is a platform for customers to include custom code to create unique experiences for their customer base. With this in mind, logging is a critical function in order to debug and understand code execution on local development, and cloud environments, particularly the AEM as a Cloud Service's Dev environments.

AEM logging and log levels are managed in configuration files that are stored as part of the AEM project in Git, and deployed as part of the AEM project via Cloud Manager. Logging in AEM as a Cloud Service can be broken into two logical sets:

* AEM logging, which performs logging at the AEM application level
* Apache HTTPD Web Server/Dispatcher logging, which performs logging of the web server and Dispatcher on the Publish tier.

## AEM Logging {#aem-loggin}

Logging at the AEM application level, is handled by three logs:

1. AEM Java logs, which render Java logging statements for the AEM application.
1. HTTP Request logs, which log information about HTTP requests and their responses served by AEM
1. HTTP Access logs, which log summarized information and HTTP requests served by AEM

Note that HTTP requests that are served from Publish tier's Dispatcher cache or upstream CDN are not reflected in these logs.

## AEM Java logging {#aem-java-logging}

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
When DEBUG logging is active, statements providing a clear picture of what activities occur as well as any key parameters that affect processing are logged.</td>
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

AEM Log levels are set per environment type via OSGi configuration, which in turn are committed to Git, and deployed via Cloud Manager to AEM as a Cloud Service. Because of this, it is best to keep log statements consistent and well known for environment types, in order to ensure the logs available via AEM as Cloud Service are available at the optimal log level without requiring redeployment of application with the updated log level configuration.

### Log Format {#log-format} 

| Date and Time  | AEM as a Cloud Service dode ID  | Log Level  | Thread  |  Java Class | Log message  |
|---|---|---|---|---|---|
| 29.04.2020 21:50:13.398  |  `[cm-p1234-e5678-aem-author-59555cb5b8-q7l9s]` | `*DEBUG*`  | qtp2130572036-1472  | com.example.approval.workflow.impl.CustomApprovalWorkflow  | `No specified approver, defaulting to [ Creative Approvers user group ]`  |

**Example log output**

```
22.06.2020 18:33:30.120 [cm-p12345-e6789-aem-author-86657cbb55-xrnzq] *ERROR* [qtp501076283-1809] io.prometheus.client.dropwizard.DropwizardExports Failed to get value from Gauge
22.06.2020 18:33:30.229 [cm-p12345-e6789-aem-author-86657cbb55-xrnzq] *INFO* [qtp501076283-1805] org.apache.sling.auth.core.impl.SlingAuthenticator getAnonymousResolver: Anonymous access not allowed by configuration - requesting credentials
22.06.2020 18:33:30.370 [cm-p12345-e6789-aem-author-86657cbb55-xrnzq] *INFO* [73.91.59.34 [1592850810364] GET /libs/granite/core/content/login.html HTTP/1.1] org.apache.sling.i18n.impl.JcrResourceBundle Finished loading 0 entries for 'en_US' (basename: <none>) in 4ms
22.06.2020 18:33:30.372 [cm-p12345-e6789-aem-author-86657cbb55-xrnzq] *INFO* [FelixLogListener] org.apache.sling.i18n Service [5126, [java.util.ResourceBundle]] ServiceEvent REGISTERED
22.06.2020 18:33:30.372 [cm-p12345-e6789-aem-author-86657cbb55-xrnzq] *WARN* [73.91.59.34 [1592850810364] GET /libs/granite/core/content/login.html HTTP/1.1] libs.granite.core.components.login.login$jsp j_reason param value 'unknown' cannot be mapped to a valid reason message: ignoring
```

### Configuration Loggers {#configuration-loggers}

AEM Java logs are defined as OSGi configuration, and thus target specific AEM as a Cloud Service environments using run mode folders.

Configure java logging for custom Java packages via OSGi configurations for the Sling LogManager factory. There are two supported configuration properties:

| OSGi Configuration property  | Description  |
|---|---|
| org.apache.sling.commons.log.names | The Java packages for which to collect log statements.  |
| org.apache.sling.commons.log.level | The log level at which to log the Java packages, specified by org.apache.sling.commons.log.names  |

Changing other LogManager OSGi configuration properties may result in availability issues in AEM as a Cloud Service.

The following are examples of the recommended logging configurations (using the placeholder Java package of `com.example`) for the three AEM as a Cloud Service environment types.

### Development {#development}

/apps/my-app/config/org.apache.sling.commons.log.LogManager.factory.config-example.cfg.json

```
{
    "org.apache.sling.commons.log.names": ["com.example"],
    "org.apache.sling.commons.log.level": "debug"
}
```

### Stage {#stage}

/apps/my-app/config.stage/org.apache.sling.commons.log.LogManager.factory.config-example.cfg.json

```
{
    "org.apache.sling.commons.log.names": ["com.example"],
    "org.apache.sling.commons.log.level": "warn"
}
```

### Production {#productiomn}

/apps/my-app/config.prod/org.apache.sling.commons.log.LogManager.factory.config-example.cfg.json

```
{
    "org.apache.sling.commons.log.names": ["com.example"],
    "org.apache.sling.commons.log.level": "error"
}
```

## AEM HTTP Request Logging {#aem-http-request-logging}

AEM as a Cloud Service's HTTP request logging provides insight into the HTTP requests made to AEM and their HTTP responses in time order. This log is helpful to understand the HTTP Requests made to AEM and the order they are processed and responded to.

The key to understanding this log is mapping the HTTP request and response pairs by their IDs, denoted by the numeric value in the brackets. Note that often requests and their corresponding responses have other HTTP requests and responses interjected between them in the log.

### Log Format {#http-request-logging-format}

| Date and Time  | Request/Response Pair ID  |   | HTTP Method  | URL  | Protocol  | AEM as a Cloud Service node ID  |
|---|---|---|---|---|---|---|
| 29/Apr/2020:19:14:21 +0000  | `[137]`  | ->  |  POST |  /conf/global/settings/dam/adminui-extension/metadataprofile/ |  HTTP/1.1 | `[cm-p1234-e5678-aem-author-59555cb5b8-q7l9s]`  |

**Example Log**

```
29/Apr/2020:19:14:21 +0000 [137] -> POST /conf/global/settings/dam/adminui-extension/metadataprofile/ HTTP/1.1 [cm-p1234-e5678-aem-author-59555cb5b8-q7l9s]
...
29/Apr/2020:19:14:22 +0000 [139] -> GET /mnt/overlay/dam/gui/content/processingprofilepage/metadataprofiles/editor.html/conf/global/settings/dam/adminui-extension/metadataprofile/main HTTP/1.1 [cm-p1234-e5678-aem-author-59555cb5b8-q7l9s]
...
29/Apr/2020:19:14:21 +0000 [137] <- 201 text/html 111ms [cm-p1234-e5678-aem-author-59555cb5b8-q7l9s]
...
29/Apr/2020:19:14:22 +0000 [139] <- 200 text/html;charset=utf-8 637ms [cm-p1234-e5678-aem-author-59555cb5b8-q7l9s]
```

### Configuring the Log {#configuring-the-log}

The AEM HTTP Request log is not configurable in AEM as a Cloud Service.

## AEM HTTP Access Logging {#aem-http-access-logging}

AEM as Cloud Service HTTP access logging shows HTTP requests in time order. Each log entry represents the HTTP Request that accesses AEM.

This log is helpful to quickly understand what HTTP requests are being made to AEM, if they succeed by looking at the accompanying HTTP response status code, and how long the HTTP request took to complete. This log can also be helpful to debug a specific user's activity by filtering log entries by Users.

### Log Format {#access-log-format}

<table>
<tbody>
<tr>
<td><b>AEM as a Cloud Service node ID</b></td>
<td><b>IP address of the client</b></td>
<td><b>User</b></td>
<td><b>Date and time</b></td>
<td><b>Blank</b></td>
<td><b>HTTP method</b></td>
<td><b>URL</b></td>
<td><b>Protocol</b></td>
<td><b>Blank</b></td>
<td><b>HTTP response status</b></td>
<td><b>HTTP response time in milliseconds</b></td>
<td><b>Referrer</b></td>
<td><b>User agent</b></td>
</tr>
<tr>
<td>cm-p1235-e2644-aem-author-59555cb5b8-8kgr2</td>
<td>-</td>
<td>myuser@adobe.com</td>
<td>30/Apr/2020:17:37:14 +0000</td>
<td>"</td>
<td>GET</td>
<td>/libs/granite/ui/references/clientlibs/references.lc-5188e85840c529149e6cd29d94e74ad5-lc.min.css</td>
<td>HTTP/1.1</td>
<td>"</td>
<td>200</td>
<td>1141</td>
<td><code>"https://author-p1234-e4444.adobeaemcloud.com/mnt/overlay/dam/gui/content/assets/metadataeditor.external.html?item=/content/dam/wknd/en/adventures/surf-camp-in-costa-rica/adobestock_266405335.jpeg&_charset_=utf8"</code></td>
<td>"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"</td>
</tr>
</tbody>
</table>


**Example**

```
cm-p1234-e26813-aem-author-59555cb5b8-8kgr2 - example@adobe.com 30/Apr/2020:17:37:14 +0000  "GET /libs/granite/ui/references/clientlibs/references.lc-5188e85840c529149e6cd29d94e74ad5-lc.min.css HTTP/1.1" 200 1141 "https://author-p10711-e26813.adobeaemcloud.com/mnt/overlay/dam/gui/content/assets/metadataeditor.external.html?item=/content/dam/en/images/example.jpeg&_charset_=utf8" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
cm-p1234-e26813-aem-author-59555cb5b8-8kgr2 - example@adobe.com 30/Apr/2020:17:37:14 +0000  "GET /libs/dam/gui/coral/components/admin/customthumb/clientlibs.lc-60e4443805c37afa0c74b674b141f1df-lc.min.css HTTP/1.1" 200 809 "https://author-p10711-e26813.adobeaemcloud.com/mnt/overlay/dam/gui/content/assets/metadataeditor.external.html?item=/content/dam/en/images/example.jpeg&_charset_=utf8" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
cm-p1234-e26813-aem-author-59555cb5b8-8kgr2 - example@adobe.com 30/Apr/2020:17:37:14 +0000  "GET /libs/dam/gui/coral/components/admin/metadataeditor/clientlibs/metadataeditor.lc-4a2226d8232f8b7ab27d24820b9ddd64-lc.min.js HTTP/1.1" 200 7965 "https://author-p10711-e26813.adobeaemcloud.com/mnt/overlay/dam/gui/content/assets/metadataeditor.external.html?item=/content/dam/en/images/example.jpeg&_charset_=utf8" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
```

### Configuring the HTTP Access Log {#configuring-the-http-access-log}

The HTTP Access log is not configurable in AEM as a Cloud Service.

## Apache Web Server / Dispatcher Logging {#dispatcher-logging}

AEM as a Cloud Service provides three logs for the Apache Web Servers and dispatcher layer on the Publish:

* Apache HTTPD Web Server Access log
* Apache HTTPD Web Server Error log
* Dispatcher log

Note that these logs are only available for the Publish tier.

This set of logs provides insights into HTTP requests to the AEM as a Cloud Service Publish tier prior to those requests reaching the AEM application. This is important to understand as, ideally, most HTTP requests to the Publish tier servers are served by cached content by the Apache HTTPD Web Server and AEM Dispatcher, and never reach the AEM application itself, thus there are no log statements for these requests in AEM's Java, Request or Access logs.