---
title: Logging for AEM as a Cloud Service
description: Learn how to configure global parameters for the central logging service, specific settings for the individual services or how to request data logging in AEM as a Cloud Service.
exl-id: 262939cc-05a5-41c9-86ef-68718d2cd6a9
---
# Logging for AEM as a Cloud Service {#logging-for-aem-as-a-cloud-service}

AEM as a Cloud Service is a platform for customers to include custom code to create unique experiences for their customer base. With this in mind, logging is a critical function in order to debug and understand code execution on local development, and cloud environments, particularly the AEM as a Cloud Service's Dev environments.

AEM logging and log levels are managed in configuration files that are stored as part of the AEM project in Git, and deployed as part of the AEM project via Cloud Manager. Logging in AEM as a Cloud Service can be broken into two logical sets:

* AEM logging, which performs logging at the AEM application level
* Apache HTTPD Web Server/Dispatcher logging, which performs logging of the web server and Dispatcher on the Publish tier.

## AEM Logging {#aem-loggin}

Logging at the AEM application level, is handled by three logs:

1. AEM Java logs, which render Java logging statements for the AEM application.
1. HTTP Request logs, which log information about HTTP requests and their responses served by AEM
1. HTTP Access logs, which log summarized information and HTTP requests served by AEM

>[!NOTE]
>
>HTTP requests that are served from Publish tier's Dispatcher cache or upstream CDN are not reflected in these logs.

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

**Log Format**

<table>
<tbody>
<tr>
<td>AEM as a Cloud Service node ID</td>
<td>cm-p1235-e2644-aem-author-59555cb5b8-8kgr2</td>
</tr>
<tr>
<td>IP address of the Client</td>
<td>-</td>
</tr>
<tr>
<td>User</td>
<td>myuser@adobe.com</td>
</tr>
<tr>
<td>Date and time</td>
<td>30/Apr/2020:17:37:14 +0000</td>
</tr>
<tr>
<td>HTTP method</td>
<td>GET</td>
</tr>
<tr>
<td>URL</td>
<td>/libs/granite/ui/references/clientlibs/references.lc-5188e85840c529149e6cd29d94e74ad5-lc.min.css</td>
</tr>
<tr>
<td>Protocol</td>
<td>HTTP/1.1</td>
</tr>
<tr>
<td>HTTP response status</td>
<td>200</td>
</tr>
<tr>
<td>HTTP request time in milliseconds</td>
<td>1141</td>
</tr>
<tr>
<td>Referrer</td>
<td><code>"https://author-p1234-e4444.adobeaemcloud.com/mnt/overlay/dam/gui/content/assets/metadataeditor.external.html?item=/content/dam/wknd/en/adventures/surf-camp-in-costa-rica/adobestock_266405335.jpeg&_charset_=utf8"</code></td>
</tr>
<tr>
<td>User agent</td>
<td>"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"</td>
</tr>
</tbody>
</table>

### Configuring the HTTP Access Log {#configuring-the-http-access-log}

The HTTP Access log is not configurable in AEM as a Cloud Service.

## Apache Web Server and Dispatcher Logging {#apache-web-server-and-dispatcher-logging}

AEM as a Cloud Service provides three logs for the Apache Web Servers and dispatcher layer on the Publish:

* Apache HTTPD Web Server Access log
* Apache HTTPD Web Server Error log
* Dispatcher log

Note that these logs are only available for the Publish tier.

This set of logs provides insights into HTTP requests to the AEM as a Cloud Service Publish tier prior to those requests reaching the AEM application. This is important to understand as, ideally, most HTTP requests to the Publish tier servers are served by content that is cached by the Apache HTTPD Web Server and AEM Dispatcher, and never reach the AEM application itself. Thus there are no log statements for these requests in AEM's Java, Request or Access logs.

### Apache HTTPD Web Server Access Log {#apache-httpd-web-server-access-log}

The Apache HTTP Web Server access log provides statements for each HTTP request that reaches the Publish tier's Web server/Dispatcher. Note that requests that are served from an upstream CDN are not reflected in these logs.

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

It can be set to Error, Warn, Info, Debug and Trace1 - Trace8, with a default value of Warn. To debug your RewriteRules, it is recommended to raise the log level to Trace2.

See the [mod_rewrite module documentation](https://httpd.apache.org/docs/current/mod/mod_rewrite.html#logging) for more information.

To set the log level per environment, use the appropriate conditional branch in the global.var file, as described below:

```
Define REWRITE_LOG_LEVEL Debug
  
<IfDefine ENVIRONMENT_STAGE>
  ...
  Define REWRITE_LOG_LEVEL Warn
  ...
</IfDefine>
<IfDefine ENVIRONMENT_PROD>
  ...
  Define REWRITE_LOG_LEVEL Error
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

It can be set to Error, Warn, Info, Debug and Trace1, with a default value of Warn.

While Dispatcher logging supports several other levels of logging granularity, the AEM as a Cloud Service recommends using the levels described below.

To set the log level per environment, use the appropriate conditional branch in the `global.var` file, as described below:

```
Define DISP_LOG_LEVEL Debug
  
<IfDefine ENVIRONMENT_STAGE>
  ...
  Define DISP_LOG_LEVEL Warn
  ...
</IfDefine>
<IfDefine ENVIRONMENT_PROD>
  ...
  Define DISP_LOG_LEVEL Error
  ...
</IfDefine>
```

## How to Access Logs {#how-to-access-logs}

### Cloud Environments {#cloud-environments}

AEM as a Cloud Service logs for cloud services can be accessed either by downloading through the Cloud Manager interface or by tailing logs at the command line using the using the Adobe I/O command line interface. For more information, see the [Cloud Manager logging documentation](/help/implementing/cloud-manager/manage-logs.md).

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

## Splunk Logs {#splunk-logs}

Customers who have Splunk accounts may request via customer support ticket that their AEM Cloud Service logs are forwarded to the appropriate index. The logging data is equivalent to what is available through the Cloud Manager log downloads, but customers may find it convenient to leverage the query features available in the Splunk product.

The network bandwidth associated with logs sent to Splunk are considered part of the customer's Network I/O usage.

### Enabling Splunk Forwarding {#enabling-splunk-forwarding}

In the support request, customers should indicate:

* Splunk HEC endpoint address
* The Splunk index
* The Splunk port 
* The Splunk HEC token. See [this page](https://docs.splunk.com/Documentation/Splunk/8.0.4/Data/HECExamples) for more information.

The properties above should be specified for each relevant program/environment type combination.  For example, if a customer wanted dev, staging, and production environments, they should provide three sets of information, as indicated below. 

>[!NOTE]
>
>Splunk forwarding for sandbox program environments is not supported.

You should make sure that the initial request includes all dev environment that should be enabled, in addition to the stage/prod environments.

If any new dev environments created after the initial request are intended to have Splunk forwarding, but don't have it enabled, an additional request should be made.

Also note that if dev environments have been requested, it is possible that other dev environments not in the request or even sandbox environments will have Splunk forwarding enabled and will share a Splunk index. Customers can use the `aem_env_id` field to distinguish between these environments.

Below you will find a sample customer support request:

Program 123, Production Env

* Splunk HEC endpoint address: `splunk-hec-ext.acme.com`
* Splunk index: acme_123prod (customer can choose whatever naming convention it wishes)
* Splunk port: 443
* Splunk HEC token: ABC123

Program 123, Stage Env

* Splunk HEC endpoint address: `splunk-hec-ext.acme.com`
* Splunk index: acme_123stage
* Splunk port: 443
* Splunk HEC token: ABC123

Program 123, Dev Envs

* Splunk HEC endpoint address: `splunk-hec-ext.acme.com`
* Splunk index: acme_123dev
* Splunk port: 443
* Splunk HEC token: ABC123

It may be sufficient for the same Splunk index to be used for each environment, in which case either the `aem_env_type` field can be used to differentiate based on the values dev, stage, and prod. If there are multiple dev environments, the `aem_env_id` field can also be used. Some organizations may choose a separate index for the production environment's logs if the associated index limits access to a reduced set of Splunk users. 

Here is an example log entry:

```
aem_env_id: 1242
aem_env_type: dev
aem_program_id: 12314
aem_tier: author
file_path: /var/log/aem/error.log
host: 172.34.200.12 
level: INFO
msg: [FelixLogListener] com.adobe.granite.repository Service [5091, [org.apache.jackrabbit.oak.api.jmx.SessionMBean]] ServiceEvent REGISTERED
orig_time: 16.07.2020 08:35:32.346
pod_name: aemloggingall-aem-author-77797d55d4-74zvt
splunk_customer: true
```
