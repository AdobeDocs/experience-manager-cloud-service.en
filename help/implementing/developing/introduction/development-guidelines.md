---
title: AEM as a Cloud Service Development Guidelines
description: Learn guidelines for developing on AEM as a Cloud Service and about important ways in which it differs from AEM on premises and AEM in AMS.
exl-id: 94cfdafb-5795-4e6a-8fd6-f36517b27364
feature: Developing
role: Admin, Architect, Developer
---
# AEM as a Cloud Service Development Guidelines {#aem-as-a-cloud-service-development-guidelines}

>[!CONTEXTUALHELP]
>id="development_guidelines"
>title="AEM as a Cloud Service Development Guidelines"
>abstract="Learn guidelines for developing on AEM as a Cloud Service and about important ways in which it differs from AEM on premises and AEM in AMS."
>additional-url="https://video.tv.adobe.com/v/330555/" text="Demo of Package Structure"

This document presents guidelines for developing on AEM as a Cloud Service and about important ways in which it differs from AEM on premises and AEM in AMS.

## Code Must Be Cluster-Aware {#cluster-aware}

Code running in AEM as a Cloud Service must be aware of the fact that it is always running in a cluster. This means that there is always more than one instance running. The code must be resilient especially as an instance might be stopped at any point in time.

During the update of AEM as a Cloud Service, there are instances with old and new code running in parallel. Therefore, old code must not break with content created by new code and new code must be able to deal with old content.

If there is the need to identify the primary in the cluster, the Apache Sling Discovery API can be used to detect it.

## State in Memory {#state-in-memory}

State must not be kept in memory but persisted in the repository. Otherwise, this state might get lost if an instance is stopped.

## State on the Filesystem {#state-on-the-filesystem}

Do not use the instance's file system in AEM as a Cloud Service. The disk is ephemeral and is disposed when instances are recycled. Limited use of the filesystem for temporary storage relating to the processing of single requests is possible, but should not be abused for huge files. This is because it may have a negative impact on the resource usage quota and run into disk limitations.

As an example where file system usage is not supported, the Publish tier should ensure that any data that must be persisted is shipped off to an external service for longer term storage.

## Observation {#observation}

Similar, with everything that is asynchronously happening like acting on observation events, it cannot be guaranteed to be executed locally and therefore must be used with care. This is true for both JCR events and Sling resource events. At the time a change is happening, the instance may be taken down and be replaced by a different instance. Other instances in the topology that are active at that time are able to react to that event. In this case however, this will not be a local event and there might even be no active leader in case of an ongoing leader election when the event is issued.

## Background Tasks and Long Running Jobs {#background-tasks-and-long-running-jobs}

Code executed as a background tasks must assume that the instance it is running in can be brought down at any time. Therefore the code must be resilient, and most importantly resumable. That means that if the code gets re-executed it should not start from the beginning again but rather close to from where it left off. While this is not a new requirement for this kind of code, in AEM as a Cloud Service it is more likely that an instance take down is going to occur.

To minimize the trouble, long running jobs should be avoided if possible, and they should be resumable at a minimum. For executing such jobs, use Sling Jobs, which have an at-least-once guarantee and hence if they get interrupted will get re-executed as soon as possible. But they should probably not start from the beginning again. For scheduling such jobs, it is best to use the [Sling Jobs](https://sling.apache.org/documentation/bundles/apache-sling-eventing-and-job-handling.html#jobs-guarantee-of-processing) scheduler as this again ensures the at-least-once execution.

Do not use the Sling Commons Scheduler for scheduling as execution cannot be guaranteed. It is just more likely that it is scheduled.

Similarly, with everything that is asynchronously happening, like acting on observation events, (being it JCR events or Sling resource events), can't be guaranteed to be executed and therefore must be used with care. This is already true for AEM deployments in the present.

## Outgoing HTTP Connections {#outgoing-http-connections}

It is strongly recommended that any outgoing HTTP connections set reasonable connect and read timeouts; suggested values are 1 second for the connection timeout and 5 seconds for read timeout. The exact numbers must be determined based on the performance of the backend system handling these requests.

For code that does not apply these timeouts, AEM instances running on AEM as a Cloud Service will enforce a global timeouts. These timeout values are 10 seconds for connect calls and 60 seconds for read calls for connections.

Adobe recommends the use of the provided [Apache HttpComponents Client 4.x library](https://hc.apache.org/httpcomponents-client-ga/) for making HTTP connections.

Alternatives that are known to work, but may require providing the dependency yourself are:

* [java.net.URL](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/net/URL.html) and/or [java.net.URLConnection](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/net/URLConnection.html) (Provided by AEM)
* [Apache Commons HttpClient 3.x](https://hc.apache.org/httpclient-3.x/) (not recommended as it is outdated and replaced by version 4.x)
* [OK Http](https://square.github.io/okhttp/) (Not provided by AEM)

Next to providing timeouts also a proper handling of such timeouts and unexpected HTTP status codes should be implemented.

## Handling request rate limits {#rate-limit-handling}

When the rate of incoming requests to AEM exceeds healthy levels, AEM responds to new requests with HTTP error code 429. Applications making programmatic calls to AEM can consider coding defensively, retrying after a few seconds with an exponential backoff strategy. Before mid-August 2023, AEM responded to the same condition with HTTP error code 503.

## No Classic UI Customizations {#no-classic-ui-customizations}

AEM as a Cloud Service only supports the Touch UI for third-party customer code. Classic UI is not available for customization.

## No Native Binaries or Native Libraries {#avoid-native-binaries}

Native binaries and libraries must not be deployed to or installed in cloud environments.

In addition, code should not attempt to download native binaries or native java extensions (for example, JNI) at runtime.

## No Streaming Binaries through AEM as a Cloud Service {#no-streaming-binaries}

Binaries should be accessed through the CDN, which will serve binaries outside of the core AEM services.

For example, do not use `asset.getOriginal().getStream()`, which triggers downloading a binary onto the AEM service's ephemeral disk.

## No Reverse Replication Agents {#no-reverse-replication-agents}

Reverse replication from Publish to Author is not supported in AEM as a Cloud Service. If such a strategy is needed, you can use an external persistence store that is shared amongst the farm of Publish instances and potentially the Author cluster.

## Forward Replication Agents Might Need to be Ported {#forward-replication-agents}

Content is replicated from Author to Publish through a pub-sub mechanism. Custom replication agents are not supported.

## No Overloading Development Environments {#overloading-dev-envs}

Production environments are sized higher to ensure stable operation, while Stage environments are sized like Production environments to ensure realistic testing under production conditions.

Dev environments and Rapid Dev environments should be limited to development, error analysis, and functional tests, and are not designed to process high workloads, nor large amounts of content.

As an example, changing an index definition on a large content repository on a Dev environment can result in re-indexing resulting in too much processing. Tests that require substantial content should be run on Stage environments.

## Monitoring and Debugging {#monitoring-and-debugging}

### Logs {#logs}

For local development, logs entries are written to local files in the `/crx-quickstart/logs` folder.

On Cloud environments, developers can download logs through Cloud Manager or use a command line tool to tail the logs. <!-- See the [Cloud Manager documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/introduction-to-cloud-manager.html) for more details. Custom logs are not supported and so all logs should be output to the error log. -->

**Setting the Log Level**

To change the log levels for Cloud environments, the Sling Logging OSGI configuration should be modified, followed by a full redeployment. Because this is not instantaneous, be cautious about enabling verbose logs on production environments which receive lots of traffic. In the future, it is possible that there are mechanisms to more quickly change the log level.

>[!NOTE]
>
>To perform the configuration changes listed below, you create them on a local development environment and then push them to an AEM as a Cloud Service instance. For more information on how to do this, see [Deploying to AEM as a Cloud Service](/help/implementing/deploying/overview.md).

**Activating the DEBUG Log Level**

The default log level is INFO, that is, DEBUG messages are not logged. To activate DEBUG log level, update the following property to debug mode.

`/libs/sling/config/org.apache.sling.commons.log.LogManager/org.apache.sling.commons.log.level`

For example, set `/apps/<example>/config/org.apache.sling.commons.log.LogManager.factory.config~<example>.cfg.json` with the following value.

```json
{
   "org.apache.sling.commons.log.names": [
      "com.example"
   ],
   "org.apache.sling.commons.log.level": "DEBUG",
   "org.apache.sling.commons.log.file": "logs/error.log",
   "org.apache.sling.commons.log.additiv": "false"
}
```

Do not leave the log at the DEBUG log level longer than necessary, as this generates lots of entries.

Discrete log levels can be set for the different AEM environments using run mode-based OSGi configuration targeting if it's desirable to always log at `DEBUG` during development. For example:

| Environment | OSGi configuration location by run mode | `org.apache.sling.commons.log.level` property value |
| - | - | - |
|  Development | /apps/example/config/org.apache.sling.commons.log.LogManager.factory.config~example.cfg.json | DEBUG |
|  Stage | /apps/example/config.stage/org.apache.sling.commons.log.LogManager.factory.config~example.cfg.json | WARN |
|  Production | /apps/example/config.prod/org.apache.sling.commons.log.LogManager.factory.config~example.cfg.json | ERROR |

A line in the debug file usually starts with DEBUG, and then provides the log level, the installer action and the log message. For example:

```text
DEBUG 3 WebApp Panel: WebApp successfully deployed
```

The log levels are as follows:

| 0  | Fatal error   | The action has failed, and the installer cannot proceed.   |
|---|---|---|
| 1  | Error  | The action has failed. The installation proceeds, but a part of CRX was not installed correctly and will not work.   |
| 2  | Warning  | The action has succeeded but encountered problems. CRX may or may not work correctly. |
| 3  |  Information | The action has succeeded.   |

### Thread Dumps {#thread-dumps}

Thread dumps on Cloud environments are collected on an ongoing basis, but cannot be downloaded in a self-serve manner at this time. In the meanwhile, contact AEM support if thread dumps are needed for debugging an issue, specifying the exact time window.

## CRX/DE Lite and AEM as a Cloud Service Developer Console {#crxde-lite-and-developer-console}

### Local Development {#local-development}

For local development, Developers have full access to CRXDE Lite (`/crx/de`)  and the AEM Web Console (`/system/console`).

On local development (using the SDK), `/apps` and `/libs` can be written to directly, which is different from Cloud environments where those top level folders are immutable.

### AEM as a Cloud Service Development tools {#aem-as-a-cloud-service-development-tools}

>[!NOTE]
>The AEM as a Cloud Service Developer Console should not be confused with the similarly named [*Adobe Developer Console*](https://developer.adobe.com/developer-console/).
>

>[!NOTE]
>Some customers will have the option to try out a revamped experience for the AEM Cloud Service Developer Console. See [this article](/help/implementing/developing/introduction/aem-developer-console.md) for more information.

Customers can access CRXDE lite on the author tier's development environment but not stage or production. The immutable repository (`/libs`, `/apps`) cannot be written to at runtime so attempting to do so will result in errors.

Instead, the Repository Browser can be launched from the AEM as a Cloud Service Developer Console, providing a read-only view into the repository for all environments on author, publish, and preview tiers. For more information see the [Repository Browser](/help/implementing/developing/tools/repository-browser.md).

A set of tools for debugging AEM as a Cloud Service developer environments are available in the AEM as a Cloud Service Developer Console for RDE, dev, stage, and production environments. The url can be determined by adjusting the Author or Publish service urls as follows:

`https://dev-console-<namespace>.<cluster>.dev.adobeaemcloud.com`

As a shortcut, the following Cloud Manager CLI command can be used to launch the AEM as a Cloud Service Developer Console based on an environment parameter described below:

`aio cloudmanager:open-developer-console <ENVIRONMENTID> --programId <PROGRAMID>`

See [Release Information](/help/release-notes/home.md) for more information.

Developers can generate status information, and resolve various resources.

As illustrated below, available statuses information include the state of bundles, components, OSGI configurations, oak indexes, OSGI services, and Sling jobs.

![Dev Console 1](/help/implementing/developing/introduction/assets/devconsole1.png)

As illustrated below, developers can resolve package dependencies and servlets:

![Dev Console 2](/help/implementing/developing/introduction/assets/devconsole2.png)

![Dev Console 3](/help/implementing/developing/introduction/assets/devconsole3.png)

Also useful for debugging, the AEM as a Cloud Service Developer Console has a link to the Explain Query tool:

![Dev Console 4](/help/implementing/developing/introduction/assets/devconsole4.png)

For Production programs, access to the AEM as a Cloud Service Developer Console is defined by the "Cloud Manager - Developer Role" in the Adobe Admin Console, while for sandbox programs, the AEM as a Cloud Service Developer Console is available to any user with a product profile giving them access to AEM as a Cloud Service. For all programs, "Cloud Manager - Developer Role" is needed for status dumps and the repository browser and users must also be defined in the AEM Users or AEM Administrators Product Profile on both author and publish services to view data from both services. For more information about setting up user permissions, see [Cloud Manager Documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/requirements/setting-up-users-and-roles.html).

### Performance Monitoring {#performance-monitoring}

Adobe monitors application performance and takes measures to address if deterioration is observed. At this time, application metricscannot be obeserved.

## Sending Email {#sending-email}

The sections below describe how to request, configure, and send email.

>[!NOTE]
>
>The Mail Service can be configured with OAuth2 support. For more information, see [OAuth2 Support for the Mail Service](/help/security/oauth2-support-for-mail-service.md).

### Enabling Outbound Email {#enabling-outbound-email}

By default, ports used to send email are disabled. To activate a port, configure [advanced networking](/help/security/configuring-advanced-networking.md), making sure to set for each needed environment the `PUT /program/<program_id>/environment/<environment_id>/advancedNetworking` endpoint's port forwarding rules, which maps the intended port (for example, 465 or 587) to a proxy port.

It is recommended to configure advanced networking with a `kind` parameter set to `flexiblePortEgress` since Adobe can optimize performance of flexible port egress traffic. If a unique egress IP address is necessary, choose a `kind` parameter of `dedicatedEgressIp`. If you have already configured VPN for other reasons, you can use the unique IP address provided by that advanced networking variation as well.

You must send email through a mail server rather than directly to email clients. Otherwise, the emails may be blocked.

### Sending Emails {#sending-emails}

The [Day CQ Mail Service OSGI service](https://experienceleague.adobe.com/docs/experience-manager-65/administering/operations/notification.html#configuring-the-mail-service) should be used and emails must be sent to the mail server indicated in the support request rather than directly to recipients.

### Configuration {#email-configuration}

E-mails in AEM should be sent using the [Day CQ Mail Service OSGi service](https://experienceleague.adobe.com/docs/experience-manager-65/administering/operations/notification.html#configuring-the-mail-service).

See the [AEM 6.5 documentation](https://experienceleague.adobe.com/docs/experience-manager-65/administering/operations/notification.html) for details around configuring email settings. For AEM as a Cloud Service, note the following necessary adjustments to the `com.day.cq.mailer.DefaultMailService OSGI` service:

* The SMTP server host name should be set to $[env:AEM_PROXY_HOST;default=proxy.tunnel]
* The SMTP server port should be set to the value of the original proxy port set in the portForwards parameter used in the API call when configuring up advanced networking. For example, 30465 (rather than 465)

The SMTP server port should be set as the `portDest` value set in the portForwards parameter used in the API call when configuring advanced networking and the `portOrig` value should be a meaningful value that is within the required range of 30000 - 30999. For example, if the SMTP server port is 465, port 30465 should be used as the `portOrig` value.

In this case, and assuming SSL needs to be enabled, in the configuration of the **Day CQ Mail Service OSGI** service:

* Set `smtp.port` to `30465`
* Set `smtp.ssl` to `true`

Alternatively, if the destination port is 587, a `portOrig` value of 30587 should be used. And assuming that SSL should be disabled, the configuration of the Day CQ Mail Service OSGI service:

* Set `smtp.port` to `30587`
* Set `smtp.ssl` to `false`

The `smtp.starttls` property will automatically be set by AEM as a Cloud Service at runtime to an appropriate value. Thus, if `smtp.ssl` is set to true, `smtp.startls` is ignored. If `smtp.ssl` is set to false, `smtp.starttls` is set to true. This is regardless of the `smtp.starttls` values set in your OSGI configuration.


The Mail Service can optionally be configured with OAuth2 support. For more information, see [OAuth2 Support for the Mail Service](/help/security/oauth2-support-for-mail-service.md).

### Legacy email configuration {#legacy-email-configuration}

Prior to the 2021.9.0 release, email was configured through a customer support request. Note the following necessary adjustments to the `com.day.cq.mailer.DefaultMailService OSGI` service:

AEM as a Cloud Service requires mail to be sent through port 465. If a mail server does not support port 465, port 587 can be used, as long as the TLS option is enabled.

If port 465 has been requested:

* set `smtp.port` to `465`
* set `smtp.ssl` to `true`

and if port 587 has been requested:

* set `smtp.port` to `587`
* set `smtp.ssl` to `false`

The `smtp.starttls` property will automatically be set by AEM as a Cloud Service at runtime to an appropriate value. Thus, if `smtp.ssl` is set to true, `smtp.startls` is ignored. If `smtp.ssl` is set to false, `smtp.starttls` is set to true. This is regardless of the `smtp.starttls` values set in your OSGI configuration.

The SMTP server host should be set to that of your mail server.

## Avoid Large Multi-Value Properties {#avoid-large-mvps}

The Oak content repository that underlies AEM as a Cloud Service is not intended to be used with an excessive number of multi-value properties (MVPs). A rule-of-thumb is to keep MVPs below 1000. However actual performance depends on many factors.

Warnings are logged by default after exceeding 1000. They are similar to the following.

```text
org.apache.jackrabbit.oak.jcr.session.NodeImpl Large multi valued property [/path/to/property] detected (1029 values). 
```

Large MVPs can lead to errors due to the MongoDB document exceeding 16 MB, resulting in errors similar to the following.

```text
Caused by: com.mongodb.MongoWriteException: Resulting document after update is larger than 16777216
```

See the [Apache Oak documentation](https://jackrabbit.apache.org/oak/docs/dos_and_donts.html#Large_Multi_Value_Property) for more details.

## [!DNL Assets] development guidelines and use cases {#use-cases-assets}

To learn about the development use cases, recommendations, and reference materials for Assets as a Cloud Service, see [Developer references for Assets](/help/assets/developer-reference-material-apis.md#assets-cloud-service-apis).
