---
title: Log Forwarding for AEM as a Cloud Service
description: Learn about forwarding logs to logging vendors in AEM as a Cloud Service
exl-id: 27cdf2e7-192d-4cb2-be7f-8991a72f606d
feature: Developing
role: Admin, Architect, Developer
---
# Log Forwarding {#log-forwarding}

>[!NOTE]
>
>Log Forwarding is now configured in self-serve way, different from the legacy method, which required submitting an Adobe Support ticket. See the [Migrating](#legacy-migration) section if your log forwarding was setup by Adobe.

Customers with a license with a logging vendor or who host a logging product can have AEM logs (including Apache/Dispatcher) and CDN logs forwarded to the associated logging destination. AEM as a Cloud Service supports the following logging destinations:

* Azure Blob Storage
* Datadog
* Elasticsearch or OpenSearch
* HTTPS
* Splunk

Log forwarding is configured in a self-service manner by declaring a configuration in Git, and deploying it via the Cloud Manager Config Pipeline to RDE, dev, stage, and production environment types in production (non-sandbox) programs.

There is an option for the AEM and Apache/Dispatcher logs to be routed through AEM's advanced networking infrastructure, such as dedicated egress IP.

Note that the network bandwidth associated with logs sent to the logging destination are considered part of your organization's Network I/O usage.

## How This Article is Organized {#how-organized}

This article is organized in the following way:

* Setup - common for all logging destinations
* Transport & Advanced Networking - consideration should be given to network setup before creating logging configuration
* Logging destination configurations - each destination has a slightly different format
* Log Entry Formats - information about the log entry formats
* Migrating from legacy log forwarding - how to move from log forwarding previously setup by Adobe to the self-serve approach

## Setup {#setup}

1. Create a file named `logForwarding.yaml`. It should contain metadata, as described in the [config pipeline article](/help/operations/config-pipeline.md#common-syntax) (**kind** should be set to `LogForwarding` and version set to "1"), with a configuration similar to the following (we use Splunk as an example).

   ```yaml
   kind: "LogForwarding"
   version: "1"
   metadata:
     envTypes: ["dev"]
   data:
     splunk:
       default:
         enabled: true
         host: "splunk-host.example.com"
         token: "${{SPLUNK_TOKEN}}"
         index: "AEMaaCS"
   
   ```

1. Place the file somewhere under a top level folder named *config* or similar, as described in [Using Config Pipelines](/help/operations/config-pipeline.md#folder-structure).

1. For environment types other than RDE (which uses command line tooling), create a targeted deployment config pipeline in Cloud Manager, as referenced by [this section](/help/operations/config-pipeline.md#creating-and-managing); note that Full Stack pipelines and Web Tier pipelines do not deploy the configuration file.

1. Deploy the configuration.

Tokens in the configuration (such as `${{SPLUNK_TOKEN}}`) represent secrets, which should not be stored in Git. Instead, declare them as Cloud Manager [Secret Environment Variables](/help/operations/config-pipeline.md#secret-env-vars). Make sure to select **All** as the dropdown value for the Service Applied field, so logs can be forwarded to author, publish, and preview tiers.

It is possible to set different values between CDN logs and AEM logs (including Apache/Dispatcher), by including an additional **cdn** and/or **aem** block after the **default** block, where properties can override those defined in the **default** block; only the enabled property is required. A possible use case could be to use a different Splunk index for CDN logs, as the example below illustrates.

   ```yaml
      kind: "LogForwarding"
      version: "1"
      metadata:
        envTypes: ["dev"]
      data:
        splunk:
          default:
            enabled: true
            host: "splunk-host.example.com"
            token: "${{SPLUNK_TOKEN}}"
            index: "AEMaaCS"
          cdn:
            enabled: true
            token: "${{SPLUNK_TOKEN_CDN}}"
            index: "AEMaaCS_CDN"   
   ```

   Another scenario is to disable either forwarding of the CDN logs or AEM logs (including Apache/Dispatcher). For example, to only forward the CDN logs, one can configure the following:

   ```yaml
      kind: "LogForwarding"
      version: "1"
      metadata:
        envTypes: ["dev"]
      data:
        splunk:
          default:
            enabled: true
            host: "splunk-host.example.com"
            token: "${{SPLUNK_TOKEN}}"
            index: "AEMaaCS"
          aem:
            enabled: false
   ```

## Transport & Advanced Networking {#transport-advancednetworking}

Some organizations choose to restrict which traffic can be received by the logging destinations, others may require to use ports other than HTTPS (443).  If so [Advanced Networking](/help/security/configuring-advanced-networking.md) will need to be configured before deploying log forwarding configuration.

|**Destination Port**|**Require Logs to appear from Fixed IP?**|**Require Advanced Networking?**|**LogForwarding.yaml Port Required?**|
|:-----:|:-----:|:-----:|:----:|
| HTTPS (443) | No | No | No |
| HTTPS (443) | Yes | Yes, [Dedicated Egress](/help/security/configuring-advanced-networking.md#dedicated-egress-ip-address-dedicated-egress-ip-address) | No |
| Non standard port (e.g 8088) | No | Yes | Yes |
| Non standrad port (e.g 8088) | Yes | Yes [Dedicated Egress](/help/security/configuring-advanced-networking.md#dedicated-egress-ip-address-dedicated-egress-ip-address) | Yes |

>[!NOTE]
>Whether your logs appear from a single IP address is determined by your choice of Advanced Networking configuration.  Dedicated Egress must be used to facilitate this.
>
> Advanced Networking configuration is a [two-step process](/help/security/configuring-advanced-networking.md#configuring-and-enabling-advanced-networking-configuring-enabling) requiring enablement at program and environment level.

For AEM logs (including Apache/Dispatcher), if you have configured [Advanced Networking](/help/security/configuring-advanced-networking.md), you can use the `aem.advancedNetworking` property to forward them from a Dedicated Egress IP address or over a VPN.

The example below shows how to configure logging on a standard HTTPS port with Advanced Networking.

   ```yaml
   kind: "LogForwarding"
   version: "1"
   metadata:
     envTypes: ["dev"]
   data:
     splunk:
       default:
         enabled: true
         host: "splunk-host.example.com"
         port: 443
         token: "${{SPLUNK_TOKEN}}"
         index: "aemaacs"
       aem:
         advancedNetworking: true
   ```

For CDN logs, you can allow-list the IP addresses, as described in [Fastly documentation - Public IP List](https://www.fastly.com/documentation/reference/api/utils/public-ip-list/). If that list of shared IP addresses is too large, consider sending traffic to an https server or (non-Adobe) Azure Blob Store where logic can be written to send the logs out of a known IP to their ultimate destination.

>[!NOTE]
>It is not possible for CDN logs to appear from the same IP address that your AEM logs appear from, this is because logs are sent directly from Fastly and not AEM Cloud Service.

## Logging Destination Configuration {#logging-destinations}

Configurations for the supported logging destinations are listed below, along with any specific considerations.

### Azure Blob Storage {#azureblob}

   ```yaml
   kind: "LogForwarding"
   version: "1"
   metadata:
     envTypes: ["dev"]
   data:
     azureBlob:
       default:
         enabled: true       
         storageAccountName: "example_acc"
         container: "aem_logs"
         sasToken: "${{AZURE_BLOB_SAS_TOKEN}}
         
   ```

A SAS token should be used for authentication. It should be created from the Shared access signature page, rather than on the Shared access token page, and should be configured with these settings:

* Allowed services: Blob must be selected.
* Allowed resources: Object must be selected.
* Allowed permissions: Write, Add, Create must be selected.
* A valid Start and Expiry date/time.

Here is a screenshot of a sample SAS token configuration:

![Azure Blob SAS token configuration](/help/implementing/developing/introduction/assets/azureblob-sas-token-config.png)

If logs have stopped being delivered after previously functioning correctly, check whether the SAS token you configured is still valid, as it may have expired.

#### Azure Blob Storage CDN logs {#azureblob-cdn}

Each of the globally distributed logging servers will produce a new file every few seconds, under the `aemcdn` folder. Once created, the file will no longer be appended to. The filename format is YYYY-MM-DDThh:mm:ss.sss-uniqueid.log. E.g., 2024-03-04T10:00:00.000-WnFWYN9BpOUs2aOVn4ee.log.

As an example, at some point in time:

```text
aemcdn/
   2024-03-04T10:00:00.000-abc.log
   2024-03-04T10:00:00.000-def.log

```

And then 30 seconds later:

```text
aemcdn/
   2024-03-04T10:00:00.000-abc.log
   2024-03-04T10:00:00.000-def.log
   2024-03-04T10:00:30.000-ghi.log
   2024-03-04T10:00:30.000-jkl.log
   2024-03-04T10:00:30.000-mno.log

```

Each file contains multiple json log entries, each on a separate line. The log entry formats are described under [Logging for AEM as a Cloud Service](/help/implementing/developing/introduction/logging.md), and each log entry also includes the additional properties mentioned in the [Log Entry Formats](#log-formats) section below.

#### Azure Blob Storage AEM logs {#azureblob-aem}

AEM logs (including Apache/Dispatcher) appear below a folder with the following naming convention:

* aemaccess
* aemerror
* aemrequest
* aemdispatcher
* aemhttpdaccess
* aemhttpderror

Under each folder, a single file will be created and appended to. Customers are responsible for processing and managing this file so it does not grow too large.

See the log entry formats under [Logging for AEM as a Cloud Service](/help/implementing/developing/introduction/logging.md). The log entries will also include the additional properties mentioned in the [Log Entry Formats](#log-formats) section below.

### Datadog {#datadog}

   ```yaml
   kind: "LogForwarding"
   version: "1"
   metadata:
     envTypes: ["dev"]
   data:
     datadog:
       default:
         enabled: true       
         host: "http-intake.logs.datadoghq.eu"
         token: "${{DATADOG_API_KEY}}"
         tags:
            tag1: value1
            tag2: value2
         
   ```

Considerations:

* Create an API Key, without any integration with a specific cloud provider.
* The tags property is optional
* For AEM logs, the Datadog source tag is set to one of `aemaccess`, `aemerror`, `aemrequest`, `aemdispatcher`, `aemhttpdaccess`, or `aemhttpderror`
* For CDN logs, the Datadog source tag is set to `aemcdn`
* The Datadog service tag is set to `adobeaemcloud`, but you can overwrite it in the tags section
* If your ingestion pipeline uses Datadog tags to determine the appropriate index for forwarding logs, verify that these tags are correctly configured in the Log Forwarding YAML file. Missing tags may prevent successful log ingestion if the pipeline depends on them.

### Elasticsearch and OpenSearch {#elastic}

   ```yaml
   kind: "LogForwarding"
   version: "1"
   metadata:
     envTypes: ["dev"]
   data:
     elasticsearch:
       default:
         enabled: true
         host: "example.com"
         user: "${{ELASTICSEARCH_USER}}"
         password: "${{ELASTICSEARCH_PASSWORD}}"
         pipeline: "ingest pipeline name"
   
   ```

Considerations:

* by default, the port is 443. It can optionally be overridden with a property named `port`
* For credentials, make sure to use use deployment credentials, rather than account credentials. These are the credentials that are generated in a screen that may resemble this image:

![Elastic deployment credentials](/help/implementing/developing/introduction/assets/ec-creds.png)

* For AEM logs, `index` is set to one of `aemaccess`, `aemerror`, `aemrequest`, `aemdispatcher`, `aemhttpdaccess`, or `aemhttpderror`
* The optional pipeline property should be set to the name of the Elasticsearch or OpenSearch ingest pipeline, which can be configured to route the log entry to the appropriate index. The pipeline's Processor type must be set to *script* and the script language should be set to *painless*. Here is a sample script snippet to route log entries into an index such as aemaccess_dev_26_06_2024:

```text
def envType = ctx.aem_env_type != null ? ctx.aem_env_type : 'unknown';
def sourceType = ctx._index;
def date = new SimpleDateFormat('dd_MM_yyyy').format(new Date());
ctx._index = sourceType + "_" + envType + "_" + date;

```

### HTTPS {#https}

   ```yaml
   kind: "LogForwarding"
   version: "1"
   metadata:
     envTypes: ["dev"]
   data:
     https:
       default:
         enabled: true
         url: "https://example.com/aem_logs/aem"
         authHeaderName: "X-AEMaaCS-Log-Forwarding-Token"
         authHeaderValue: "${{HTTPS_LOG_FORWARDING_TOKEN}}"
   
   ```

Considerations:

* The url string must include **https://** or validation will fail.
* The url may include a port. For example, `https://example.com:8443/aem_logs/aem`. If no port is included in the url string, port 443 (the default HTTPS port) is assumed.

#### HTTPS CDN logs {#https-cdn}

Web requests (POSTs) will be sent continuously, with a json payload that is an array of log entries, with the log entry format described under [Logging for AEM as a Cloud Service](/help/implementing/developing/introduction/logging.md#cdn-log). Additional properties are mentioned in the [Log Entry Formats](#log-formats) section below.

There is also be a property named `sourcetype`, which is set to the value `aemcdn`.

>[!NOTE]
>
> Before the first CDN log entry is sent, your HTTP server must successfully complete a one-time challenge: a request sent to the path ``/.well-known/fastly/logging/challenge`` must respond with an asterisk ``*`` in the body and 200 status code.

#### HTTPS AEM logs {#https-aem}

For AEM logs (including apache/dispacher), web requests (POSTs) will be sent continuously, with a json payload that is an array of log entries, with the various log entry formats as described under [Logging for AEM as a Cloud Service](/help/implementing/developing/introduction/logging.md). Additional properties are mentioned in the [Log Entry Formats](#log-formats) section below.

There is also be a property named `Source-Type`, which is set to one of these values:

* aemaccess
* aemerror
* aemrequest
* aemdispatcher
* aemhttpdaccess
* aemhttpderror

### Splunk {#splunk}

   ```yaml
   kind: "LogForwarding"
   version: "1"
   metadata:
     envTypes: ["dev"]
   data:
     splunk:
       default:
         enabled: true
         host: "splunk-host.example.com"
         token: "${{SPLUNK_TOKEN}}"
         index: "aemaacs"
   ```

Considerations:

* By default, the port is 443. It can optionally be overridden with a property named `port`.
* The sourcetype field will have one of the following values, depending on the specific log: *aemaccess*, *aemerror*,
*aemrequest*, *aemdispatcher*, *aemhttpdaccess*, *aemhttpderror*, *aemcdn*
* If the required IPs have been allowlisted and logs are still not being delivered, verify that there are no firewall rules enforcing Splunk token validation. Fastly performs an initial validation step where an invalid Splunk token is intentionally sent. If your firewall is set to terminate connections with invalid Splunk tokens, the validation process will fail, preventing Fastly from delivering logs to your Splunk instance.

>[!NOTE]
>
> [If migrating](#legacy-migration) from legacy Log Forwarding to this self-serve model, the `sourcetype` field's values sent to your Splunk index may have changed, so adjust accordingly.

<!--
### Sumo Logic {#sumologic}

   ```yaml
   kind: "LogForwarding"
   version: "1"
   metadata:
     envTypes: ["dev"]
   data:
     splunk:
       default:
         enabled: true
         host: "https://collectors.de.sumologic.com"
         uri: "/receiver/v1/http"
         privateKey: "${{SomeOtherToken}}"
   
   ```   
-->

## Log Entry Formats {#log-formats}

See [Logging for AEM as a Cloud Service](/help/implementing/developing/introduction/logging.md) for the format of each respective log type (CDN logs, and AEM logs including Apache/Dispatcher).

Since logs from multiple programs and environments may be forwarded to the same logging destination, in addition to the output described in the logging article, the following properties will be included in each log entry:

* aem_env_id
* aem_env_type
* aem_program_id
* aem_tier

As an example, the properties could have the following values:

```text
aem_env_id: 1242
aem_env_type: dev
aem_program_id: 12314
aem_tier: author

```

## Migrating from Legacy Log Forwarding {#legacy-migration}

Before Log Forwarding configuration was achieved through a self-serve model, customers were requested to open support tickets, where Adobe would initiate the integration.

Customers who had been setup in that manner by Adobe are welcome to adapt to the self-serve model at their convenience. There are several reason to make this transition:

* A new environment (e.g., a new dev env or RDE) has been provisioned.
* Changes to your existing Splunk endpoint or credentials.
* Adobe had setup your log forwarding before CDN logs were available and you would like to receive CDN logs.
* A conscious decision to proactively adapt to the self-serve model so your organization has the knowledge even before a time-sensitive change is necessary.

When ready to migrate, simply configure the YAML file as described in the preceding sections. Use the Cloud Manager config pipeline to deploy to each of the environments where the configuration should be applied.

It is recommended, but not required, that a configuration is deployed to all environments so they are all under self-serve control. If not, you may forget which environments have been configured by Adobe versus those configured in a self-serve way.

>[!NOTE]
>The `sourcetype` field's values sent to your Splunk index may have changed, so adjust accordingly.
>
>When Log Forwarding is deployed to an environment previously configured by Adobe support, you may receive duplicate logs for up to a few hours. This will eventually auto-resolve.
