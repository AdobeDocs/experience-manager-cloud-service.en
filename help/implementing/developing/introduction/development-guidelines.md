---
title: AEM as a Cloud Service Development Guidelines
description: AEM as a Cloud Service Development Guidelines
exl-id: 94cfdafb-5795-4e6a-8fd6-f36517b27364
---
# AEM as a Cloud Service Development Guidelines {#aem-as-a-cloud-service-development-guidelines}

Code running in AEM as a Cloud Service must be aware of the fact that it is always running in a cluster. This means that there is always more than one instance running. The code must be resilient especially as an instance might be stopped at any point in time.

During the update of AEM as a Cloud Service, there will be instances with old and new code running in parallel. Therefore, old code must not break with content created by new code and new code must be able to deal with old content.
<!--

>[!NOTE]
> All of the best practices mentioned here hold true for on-premise deployments of AEM, if not stated otherwise. An instance can always stop due to various reasons. However, with Skyline it is more likely to happen therefore an instance stopping is the rule not an exception.

-->

If there is the need to identify the primary in the cluster, the Apache Sling Discovery API can be used to detect it.

## State in Memory {#state-in-memory}

State must not be kept in memory but persisted in the repository. Otherwise, this state might get lost if an instance is stopped.

## State on the Filesystem {#state-on-the-filesystem}

The instance's file system should not be used in AEM as a Cloud Service. The disk is ephemeral and will be disposed when instances are recycled. Limited use of the filesystem for temporary storage relating to the processing of single requests is possible, but should not be abused for huge files. This is because it may have a negative impact on the resource usage quota and run into disk limitations.

As an example where file system usage is not supported, the Publish tier should ensure that any data that needs to be persisted is shipped off to an external service for longer term storage.

## Observation {#observation}

Similar, with everything that is asynchronously happening like acting on observation events, it cannot be guaranteed to be executed locally and therefore must be used with care. This is true for both JCR events and Sling resource events. At the time a change is happening, the instance may be taken down and be replaced by a different instance. Other instances in the topology that are active at that time will be able to react to that event. In this case however, this will not be a local event and there might even be no active leader in case of an ongoing leader election when the event is issued.

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
* [OK Http](https://square.github.io/okhttp/) (Not provided by AEM)

## No Classic UI Customizations {#no-classic-ui-customizations}

AEM as a Cloud Service only supports the Touch UI for 3rd party customer code. Classic UI is not available for customization.

## Avoid Native Binaries {#avoid-native-binaries}

Code will not be able to download binaries at runtime nor modify them. For example, it will not be able to unpack `jar` or `tar` files.

## No Streaming Binaries through AEM as a Cloud Service {#no-streaming-binaries}

Binaries should be accessed through the CDN, which will serve binaries outside of the core AEM services.

For example, do not use `asset.getOriginal().getStream()`, which triggers downloading a binary onto the AEM service's ephemeral disk.

## No Reverse Replication Agents {#no-reverse-replication-agents}

Reverse replication from Publish to Author is not supported in AEM as a Cloud Service. If such a strategy is needed, you can use an external persistence store that is shared amongst the farm of Publish instances and potentially the Author cluster.

## Forward Replication Agents Might Need to be Ported {#forward-replication-agents}

Content is replicated from Author to Publish through a pub-sub mechanism. Custom replication agents are not supported.

## Monitoring and Debugging {#monitoring-and-debugging}

### Logs {#logs}

For local development, logs entries are written to local files in the `/crx-quickstart/logs` folder.

On Cloud environments, developers can download logs through Cloud Manager or use a command line tool to tail the logs. <!-- See the [Cloud Manager documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/introduction-to-cloud-manager.html) for more details. Note that custom logs are not supported and so all logs should be output to the error log. -->

**Setting the Log Level**

To change the log levels for Cloud environments, the Sling Logging OSGI configuration should be modified, followed by a full redeployment. Since this is not instantaneous, be cautious about enabling verbose logs on production environments which receive a lot of traffic. In the future, it's possible that there will be mechanisms to more quickly change the log level.

>[!NOTE]
>
>In order to perform the configuration changes listed below, you need to create them on a local development environment and then push them to an AEM as a Cloud Service instance. For more information on how to do this, see [Deploying to AEM as a Cloud Service](/help/implementing/deploying/overview.md).

**Activating the DEBUG Log Level**

The default log level is INFO, that is, DEBUG messages are not logged.
To activate DEBUG log level, set the

``` /libs/sling/config/org.apache.sling.commons.log.LogManager/org.apache.sling.commons.log.level ```

property to debug. Do not leave the log at the DEBUG log level longer than necessary, as it generates a lot of logs.
A line in the debug file usually starts with DEBUG, and then provides the log level, the installer action and the log message. For example:

``` DEBUG 3 WebApp Panel: WebApp successfully deployed ```

The log levels are as follows:

| 0  | Fatal error   | The action has failed, and the installer cannot proceed.   |
|---|---|---|
| 1  | Error  | The action has failed. The installation proceeds, but a part of CRX was not installed correctly and will not work.   |
| 2  | Warning  | The action has succeeded but encountered problems. CRX may or may not work correctly. |
| 3  |  Information | The action has succeeded.   |

### Thread Dumps {#thread-dumps}

Thread dumps on Cloud environments are collected on an ongoing basis, but cannot be downloaded in a self-serve manner at this time. In the meanwhile, please contact AEM support if thread dumps are needed for debugging an issue, specifying the exact time window.

## CRX/DE Lite and Developer Console {#crxde-lite-and-developer-console}

### Local Development {#local-development}

For local development, Developers have full access to CRXDE Lite (`/crx/de`)  and the AEM Web Console (`/system/console`).

Note that on local development (using the SDK), `/apps` and `/libs` can be written to directly, which is different from Cloud environments where those top level folders are immutable.

### AEM as a Cloud Service Development tools {#aem-as-a-cloud-service-development-tools}

Customers can access CRXDE lite on the author tier's development environment but not stage or production. The immutable repository (`/libs`, `/apps`) cannot be written to at runtime so attempting to do so will result in errors.

A set of tools for debugging AEM as a Cloud Service developer environments are available in the Developer Console for dev, stage, and production environments. The url can be determined by adjusting the Author or Publish service urls as follows:

`https://dev-console/-<namespace>.<cluster>.dev.adobeaemcloud.com`

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

For Production programs, access to the Developer Console is defined by the "Cloud Manager - Developer Role" in the Admin Console, while for sandbox programs, the Developer Console is available to any user with a product profile giving them access to AEM as a Cloud Service. For all programs, "Cloud Manager - Developer Role" is needed for status dumps and users must also be defined in the AEM Users or AEM Administrators Product Profile on both author and publish services in order to view status dump data from both services. For more information about setting up user permissions, see [Cloud Manager Documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/requirements/setting-up-users-and-roles.html).

### AEM Staging and Production Service {#aem-staging-and-production-service}

Customers will not have access to developer tooling for staging and production environments.

### Performance Monitoring {#performance-monitoring}

Adobe monitors application performance and takes measures to address if deterioration is observed. At this time, application metrics can not be obeserved.

## Dedicated Egress IP Address {#dedicated-egress-ip-address}

Upon request, AEM as a Cloud Service will provision a static, dedicated, IP address for HTTP (port 80) and HTTPS (port 443) outbound traffic programmed in Java code. 

### Benefits {#benefits}

This dedicated IP address can enhance security when integrating with SaaS vendors (like a CRM vendor) or other integrations outside of AEM as a Cloud Service that offer an allowlist of IP addresses. By adding the dedicated IP address to the allowlist, it ensures that only traffic from the customer's AEM Cloud Service will be permitted to flow into the external service. This is in addition to traffic from any other IPs allowed. 

Without the dedicated IP address feature enabled, traffic coming out of AEM as a Cloud Service flows through a set of IPs shared with other customers.

### Configuration {#configuration}

To enable a dedicated IP address, submit a request to Customer Support, who will provide the IP address information. The request should specify each environment and additional requests should be made if new environments need the feature after the initial request. Sandbox program environments are not supported.

### Feature Usage {#feature-usage}

The feature is compatible with Java code or libraries that result in outbound traffic, provided they use standard Java system properties for proxy configurations. In practice, this should include most common libraries. 

Below is a code sample:

```
public JSONObject getJsonObject(String relativePath, String queryString) throws IOException, JSONException {
  String relativeUri = queryString.isEmpty() ? relativePath : (relativePath + '?' + queryString);
  URL finalUrl = endpointUri.resolve(relativeUri).toURL();
  URLConnection connection = finalUrl.openConnection();
  connection.addRequestProperty("Accept", "application/json");
  connection.addRequestProperty("X-API-KEY", apiKey);

  try (InputStream responseStream = connection.getInputStream(); Reader responseReader = new BufferedReader(new InputStreamReader(responseStream, Charsets.UTF_8))) {
    return new JSONObject(new JSONTokener(responseReader));
  }
}
```

The same dedicated IP is applied to all of a customer's programs in their Adobe Organization and for all environments in each of their programs. It applies to both author and publish services.

Only HTTP and HTTPS ports are supported. This includes HTTP/1.1, as well as HTTP/2 when encrypted.

### Debugging Considerations {#debugging-considerations}

In order to validate that traffic is indeed outgoing on the expected dedicated IP address, check logs in the destination service, if available. Otherwise, it may be useful to call out to a debugging service such as [https://ifconfig.me/ip](https://ifconfig.me/ip), which will return the calling IP address.

## Sending Email {#sending-email}

AEM as a Cloud Service requires outbound mail to be encrypted. The sections below describe how to request, configure, and send email.

### Requesting Access {#requesting-access}

By default, outbound email is disabled. To activate it, submit a support ticket with:

1. The fully qualified domain name for the mail server (for example `smtp.sendgrid.net`)
1. The port to be used. It should be port 465 if supported by the mail server, otherwise port 587. Note that port 587 can only be used if the mail server requires and enforces TLS on that port
1. The program ID and environment ID for the environments they would like to mail out of
1. Whether SMTP access is needed on author, publish, or both.

### Sending Emails {#sending-emails}

The [Day CQ Mail Service OSGI service](https://experienceleague.adobe.com/docs/experience-manager-65/administering/operations/notification.html#configuring-the-mail-service) should be used and emails must be sent to the mail server indicated in the support request rather than directly to recipients.

AEM CS requires mail to be sent out through port 465. If a mail server does not support port 465, port 587 can be used, as long as the TLS option is enabled.

>[!NOTE]
>
>Note that Adobe does not support SMTP egressing over a unique dedicated IP address. 

### Configuration {#email-configuration}

E-mails in AEM should be sent using the [Day CQ Mail Service OSGi service](https://experienceleague.adobe.com/docs/experience-manager-65/administering/operations/notification.html#configuring-the-mail-service).

See [AEM 6.5 documentation](https://experienceleague.adobe.com/docs/experience-manager-65/administering/operations/notification.html) for details around configuring email settings. For AEM as a Cloud Service, the following adjustments must be made to the `com.day.cq.mailer.DefaultMailService OSGI` service:

If port 465 has been requested:

* set `smtp.port` to `465`
* set `smtp.ssl` to `true`

If port 587 has been requested (only allowed if the mail server does not support port 465):

* set `smtp.port` to `587`
* set `smtp.ssl` to `false`

The `smtp.starttls` property will automatically be set by AEM as a Cloud Service at runtime to an appropriate value. Thus, if `smtp.tls` is set to true, `smtp.startls` is ignored. If `smtp.ssl` is set to false, `smtp.starttls` is set to true. This is regardless of the `smtp.starttls` values set in your OSGI configuration.

## Recommendations and guidelines for [!DNL Assets] {#use-cases-assets}

To know about the development use cases, recommendations, and reference materials for Assets as a Cloud Service, see [Developer references for Assets](/help/assets/developer-reference-material-apis.md#assets-cloud-service-apis).
