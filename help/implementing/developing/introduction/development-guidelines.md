---
title: AEM as a Cloud Service Development Guidelines
description: To be completed 
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
* To change the log levels for Cloud environments, the Sling Logging OSGI configuration should be modified, followed by a full redeployment. Since this is not instantaneous, be cautious about enabling verbose logs on production environments which receive a lot of traffic. In the future, it's possible that there will be mechanisms to more quickly change the log level.

### Thread Dumps {#thread-dumps}

Thread dumps on Cloud environments are collected on an ongoing basis, but cannot be downloaded in a self-serve manner at this time. In the meanwhile, please contact AEM support if thread dumps are needed for debugging an issue, specifying the exact time window.

### CRX/DE Lite and System Console {#crxde-lite-and-system-console}

## Local Development {#local-development}

For local development, Developers have full access to CRXDE Lite (`/crx/de`)  and the AEM Web Console (`/system/console`).

Note that on local development (using the cloud-ready quickstart), `/apps` and `/libs` can be written to directly, which is different from Cloud environments where those top level folders are immutable.

## AEM as a Cloud Service Development tools {#aem-as-a-cloud-service-development-tools}

Customers can access CRXDE lite on the development environment but not stage or production. The immutable repository (`/libs`, `/apps`) cannot be written to at runtime so attempting to do so will result in errors.

A set of tools for debugging AEM as a Cloud Service developer environments are available in the Developer Console for dev, stage, and production environments. The url can be determined by adjusting the author or publish service urls as follows:

`https://dev-console>-<namespace>.<cluster>.dev.adobeaemcloud.com`

As a shortcut, the following Cloud Manager CLI command can be used to launch the developer console based on an environment parameter described below: 

`aio cloudmanager:open-developer-console <ENVIRONMENTID> --programId <PROGRAMID>`

See [this page](/help/release-notes/home.md) for more information.

Developers can generate status information, and resolve various resources.

As illustrated below, available statuses information include the state of bundles, components, OSGI configurations, oak indexes, OSGI services, and Sling jobs.

![Dev Console 1](/help/implementing/developing/introduction/assets/devconsole1.png)

As illustrated below, developers can resolve package dependencies and servlets:

![Dev Console 2](/help/implementing/developing/introduction/assets/devconsole2.png)

![Dev Console 3](/help/implementing/developing/introduction/assets/devconsole3.png)

Also useful for debugging, the Developer console has a link to the Explain Query tool:

![Dev Console 4](/help/implementing/developing/introduction/assets/devconsole4.png)

**AEM Staging and Production Service**

Customers will not have access to developer tooling for staging and production environments. 

### Diagnostics {#diagnostics}

System console is available for dev environments. However, diagnostic dumps for staging and production are not available.