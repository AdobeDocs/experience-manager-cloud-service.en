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

### AEM Java logging {#aem-java-logging}

AEM as a Cloud Service's provides access to Java log statements. Developers of applications for AEM should follow general Java logging best practices, logging pertinent statements about the execution of custom code, at the following log levels:

<table style="width: 100%;">
<tbody>
<tr style="height: 23px;">
<td style="height: 23px;">&nbsp;<b>AEM Environment</b></td>
<td style="height: 23px;">&nbsp;<b>Log Level</b></td>
<td style="height: 23px;">&nbsp;<b>Description</b></td>
<td style="height: 23px;">&nbsp;<b>Log Statement Availability</b></td>
</tr>
<tr style="height: 23px;">
<td style="height: 23px;">&nbsp;Development</td>
<td style="height: 23px;">&nbsp;DEBUG</td>
<td style="height: 23px;">&nbsp;Describes what is happening in the application.

When DEBUG logging is active, statements providing a clear picture of what activities occur as well as any key parameters that affect processing are logged.</td>
<td style="height: 23px;">&nbsp;<ul>
<li> Local Development</li>
<li>Development</li>
</ul></td>
</tr>
<tr style="height: 23px;">
<td style="height: 23px;">&nbsp;Stage</td>
<td style="height: 23px;">&nbsp;WARN</td>
<td style="height: 23px;">&nbsp;Describes conditions that have the potential to become errors.

When WARN logging is active, only statements indicating conditionals that are approaching sub-optimality are logged.</td>
<td style="height: 23px;">&nbsp;<ul>
<li> Local Development</li>
<li>Development</li>
<li>Stage</li>
</ul></td>
</tr>
<tr style="height: 23px;">
<td style="height: 23px;">&nbsp;Production</td>
<td style="height: 23px;">&nbsp;ERROR</td>
<td style="height: 23px;">&nbsp;Describes conditions that indicate a failure, and need to resolve.

When ERROR logging is active, only statements indicating failures are logged. ERROR log statements indicate a serious issue that should be resolved as soon as possible.</td>
<td style="height: 23px;">&nbsp;<ul>
<li> Local Development</li>
<li>Development</li>
<li>Stage</li>
<li>Production</li>
</ul></td>
</tr>
</tbody>
</table>
<!-- DivTable.com -->
<p>&nbsp;</p>