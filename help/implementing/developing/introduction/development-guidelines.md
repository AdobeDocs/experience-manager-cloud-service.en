---
title: AEM as a Cloud Service Development Guidelines
seo-title: AEM as a Cloud Service Development Guidelines
description: To be completed 
seo-description: To be completed 
---

# AEM as a Cloud Service Development Guidelines {#aem-as-a-cloud-service-development-guidelines}

## Background Tasks and Long Running Jobs {#background-tasks-and-long-running-jobs}

Code executed as a background tasks must assume that the instance it is running in can be brought down at any time. Therefore the code must be resilient and most import resumable. That means that if the code gets re-executed it should not start from the beginning again but rather close to from where it left off. While this is not a new requirement for this kind of code, in AEM as a Cloud Service it is more likely that an instance take down is going to occur.

To minimize the trouble, long running jobs should be avoided if possible, and they should be resumable at a minimum. For executing such jobs, use Sling Jobs, which have an at-least-once guarantee and hence if they get interrupted will get re-executed as soon as possible. But they should probably not start from the beginning again. For scheduling such jobs, it is best to use the [Sling Jobs](https://sling.apache.org/documentation/bundles/apache-sling-eventing-and-job-handling.html#jobs-guarantee-of-processing) scheduler as this again the at-least-once execution.

The Sling Commons Scheduler should not be used for scheduling as execution cannot be guaranteed. It is just more likely that it will be scheduled.

Similarly, with everything that is asynchronously happening, like acting on observation events, (being it JCR events or Sling resource events), can't be guaranteed to be executed and therefore must be used with care. This is already true for AEM deployments in the present.

## Outgoing HTTP Connections {#outgoing-http-connections}

It is strongly recommended that any outgoing HTTP connections set reasonable connect and read timeouts. For code that does not apply these timeouts, AEM instances running on AEM as a Cloud Service will enforce a global timeouts. These timeout values are 10 seconds for connect calls and 60 seconds for read calls for connections used by the following popular Java libraries:

Adobe recommends the use of the provided [Apache HttpComponents Client 4.x library](https://hc.apache.org/httpcomponents-client-ga/) for making HTTP connections.

Alternatives that are known to work, but may require providing the dependency yourself are:

* [java.net.URL](https://docs.oracle.com/javase/7/docs/api/java/net/URL.html) and/or [java.net.URLConnection](https://docs.oracle.com/javase/7/docs/api/java/net/URLConnection.html) (Provided by AEM)
* [Apache Commons HttpClient 3.x](https://hc.apache.org/httpclient-3.x/) (not recommended as it is outdated and replaced by version 4.x)
* [OK Http](OK Http (Not provided by AEM)) (Not provided by AEM)

## Monitoring and Debugging {#monitoring-and-debugging}

### Logs {#logs}

* For local development, logs entries are written to local files
  * `./crx-quickstart/logs`
* On Cloud environments, developers can download logs through Cloud Manager or use a command line tool to tail the logs. <!-- See the [Cloud Manager documentation](https://docs.adobe.com/content/help/en/experience-manager-cloud-manager/using/introduction-to-cloud-manager.html) for more details. Note that custom logs are not supported and so all logs should be output to the error log. -->
* To change the log levels for Cloud environments, the Sling Logging OSGI configuration should be modified, followed by a full redeployment. In the future, it's possible that there will be mechanisms to more quickly change the log level.

### CRX/DE Lite and System Console {#crxde-lite-and-system-console}

**Local Development**

For local development, Developers have full access to CRXDE Lite (`/crx/de`)  and the AEM Web Console (`/system/console`).

Note that on local development (using the cloud-ready quickstart), `/apps` and `/libs` can be written to directly, which is different from Cloud environments where those top level folders are immutable.

**AEM Development Service**

Customers can access CRXDE lite on the development environment but not stage or production. The immutable repository (`/libs`, `/apps`) cannot be written to at runtime so attempting to do so will result in errors.

Developer Tools under `/system/console` will not be available in AEM as a Cloud Service. Instead, the following tools will be available at general availability, with additional developer tools made available based on need:

* Bundles state
* Components state
* Services state
* OSGI configuration state
* Index definitions
* Sling Jobs
* Recent requests
* Servlet resolver
* Resource resolver
* Package dependencies

**AEM Staging and Production Service**

Customers will not have access to developer tooling for staging and production environments. 

### Diagnostics {#diagnostics}

System console is available for dev environments. However, diagnostic dumps for staging and production are not available.