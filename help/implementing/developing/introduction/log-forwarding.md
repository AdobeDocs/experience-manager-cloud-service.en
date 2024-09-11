---
title: Log Forwarding for AEM as a Cloud Service
description: Learn about forwarding logs to Splunk and other logging vendors in AEM as a Cloud Service
exl-id: 27cdf2e7-192d-4cb2-be7f-8991a72f606d
feature: Developing
role: Admin, Architect, Developer
---
# Log Forwarding {#log-forwarding}

>[!NOTE]
>
>This feature is not yet released, and some logging destinations may not be available at the time of release. In the meantime, you can open a support ticket to forward logs to **Splunk**, as described under [Logging for AEM as a Cloud Service](/help/implementing/developing/introduction/logging.md).

Customers who have a license for a logging vendor or host a logging product can have AEM logs (including Apache/Dispatcher) and CDN logs forwarded to the associated logging destinations. AEM as a Cloud Service supports the following logging destinations: 

* Azure Blob Storage
* DataDog
* Elasticsearch or OpenSearch
* HTTPS
* Splunk

Log forwarding is configured in a self-service manner by declaring a configuration in Git, and deploying it via the Cloud Manager Configuration Pipeline to dev, stage, and production environment types in production (non-sandbox) programs.

There is an option for the AEM and Apache/Dispatcher logs to be routed through AEM's advanced networking infrastructure, such as dedicated egress IP.

Note that the network bandwidth associated with logs sent to the logging destination are considered part of your organization's Network I/O usage.


## How This Article is Organized {#how-organized}

This article is organized in the following way:

* Setup - common for all logging destinations
* Logging destination configurations - each destination has a slightly different format
* Log Entry Formats - information about the log entry formats
* Advanced networking - sending AEM and Apache/Dispatcher logs through a dedicated egress or through a VPN


## Setup {#setup}

1. Create the following folder and file structure in the top-level folder in your project in Git:

   ```
   config/
        logForwarding.yaml
   ```

1. `logForwarding.yaml` should contain metadata and a configuration similar to the following format (we use Splunk as an example). 

   ```
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
   
   The **kind** parameter should be set to `LogForwarding` the version should be set to the schema version, which is 1.
   
   Tokens in the configuration (such as `${{SPLUNK_TOKEN}}`) represent secrets, which should not be stored in Git. Instead, declare them as Cloud Manager  [Environment Variables](/help/implementing/cloud-manager/environment-variables.md) of type **secret**. Make sure to select **All** as the dropdown value for the Service Applied field, so logs can be forwarded to author, publish, and preview tiers.
   
   It is possible to set different values between CDN logs and AEM logs (including Apache/Dispatcher), by including an additional **cdn** and/or **aem** block after the **default** block, where properties can override those defined in the **default** block; only the enabled property is required. A possible use case could be to use a different Splunk index for CDN logs, as the example below illustrates. 
   
   ```
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

   ```
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
   
1. For environment types other than RDE (which is not currently supported), create a targeted deployment config pipeline in Cloud Manager; note that Full Stack pipelines and Web Tier pipelines do not deploy the configuration file.

   * [See configuring production pipelines](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md).
   * [See configuring non-production pipelines](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md).

## Logging Destination Configuration {#logging-destinations}

Configurations for the supported logging destinations are listed below, along with any specific considerations.

### Azure Blob Storage {#azureblob}

   ```
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

#### Azure Blob Storage CDN logs {#azureblob-cdn}

Each of the globally distributed logging servers will produce a new file every few seconds, under the `aemcdn` folder. Once created, the file will no longer be appended to. The filename format is YYYY-MM-DDThh:mm:ss.sss-uniqueid.log. E.g., 2024-03-04T10:00:00.000-WnFWYN9BpOUs2aOVn4ee.log.

As an example, at some point in time:

```
aemcdn/
   2024-03-04T10:00:00.000-abc.log
   2024-03-04T10:00:00.000-def.log

```

And then 30 seconds later:

```
aemcdn/
   2024-03-04T10:00:00.000-abc.log
   2024-03-04T10:00:00.000-def.log
   2024-03-04T10:00:30.000-ghi.log
   2024-03-04T10:00:30.000-jkl.log
   2024-03-04T10:00:30.000-mno.log

```

Each file contains multiple json log entries, each on a separate line. The log entry formats are described under [Logging for AEM as a Cloud Service](/help/implementing/developing/introduction/logging.md), and each log entry also includes the additional properties mentioned in the [Log Entry Formats](#log-format) section below.

#### Azure Blob Storage AEM logs {#azureblob-aem}

AEM logs (including Apache/Dispatcher) appear below a folder with the following naming convention:

* aemaccess
* aemerror
* aemdispatcher 
* httpdaccess
* httpderror

Under each folder, a single file will be created and appended to. Customers are responsible for processing and managing this file so it does not grow too large.

See the log entry formats under [Logging for AEM as a Cloud Service](/help/implementing/developing/introduction/logging.md). The log entries will also include the additional properties mentioned in the [Log Entry Formats](#log-formats) section below.

   
### Datadog {#datadog}

   ```
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
* the tags property is optional
* For AEM logs, the Datadog source tag is set to one of `aemaccess`, `aemerror`, `aemdispatcher`, `httpdaccess`, or `httpderror`
* For CDN logs, the Datadog source tag is set to `aemcdn`
* the Datadog service tag is set to `adobeaemcloud`, but you can overwrite it in the tags section
   

### Elasticsearch and OpenSearch {#elastic}

   ```
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

* The optional pipeline property should be set to the name of the Elasticsearch or OpenSearch ingest pipeline, which can be configured to route the log entry to the appropriate index. The pipeline's Processor type must be set to *script* and the script language should be set to *painless*. Here is a sample script snippet to route log entries into an index such as aemaccess_dev_26_06_2024:

```
def envType = ctx.aem_env_type != null ? ctx.aem_env_type : 'unknown';
def sourceType = ctx._index;
def date = new SimpleDateFormat('dd_MM_yyyy').format(new Date());
ctx._index = sourceType + "_" + envType + "_" + date;

```

### HTTPS {#https}

   ```
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

* The url string must include **https://** or validation will fail. If no port is included in the url string (e.g., `https://example.com:8443/aem_logs/aem`), port 443 (the default HTTPS port) is assumed.
* If you would like to use a port different than 443, please provide it as part of the URL.

#### HTTPS CDN logs {#https-cdn}

Web requests (POSTs) will be sent continuously, with a json payload that is an array of log entries, with the log entry format described under [Logging for AEM as a Cloud Service](/help/implementing/developing/introduction/logging.md#cdn-log). Additional properties are mentioned in the [Log Entry Formats](#log-formats) section below.

There is also be a property named `sourcetype`, which is set to the value `aemcdn`.

>[!NOTE]
>
> Before the first CDN log entry is sent, your HTTP server must successfully complete a one-time challenge: a request sent to the path ``/.well-known/fastly/logging/challenge`` must respond with an asterisk ``*`` in the body and 200 status code.

#### HTTPS AEM logs {#https-aem}

For AEM logs (including apache/dispacher), web requests (POSTs) will be sent continuously, with a json payload that is an array of log entries, with the various log entry formats as described under [Logging for AEM as a Cloud Service](/help/implementing/developing/introduction/logging.md). Additional properties are mentioned in the [Log Entry Formats](#log-format) section below.

There is also be a property named `sourcetype`, which is set to one of these values:

* aemaccess
* aemerror
* aemdispatcher 
* httpdaccess
* httpderror

### Splunk {#splunk}

   ```
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

* by default, the port is 443. It can optionally be overridden with a property named `port`


<!--
### Sumo Logic {#sumologic}

   ```
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

```
aem_env_id: 1242
aem_env_type: dev
aem_program_id: 12314
aem_tier: author

```

## Advanced Networking {#advanced-networking}

Some organizations choose to restrict which traffic can be received by the logging destinations.

For the CDN log, you can allow-list the IP addresses, as described in [fastly documentation - Public IP List](https://www.fastly.com/documentation/reference/api/utils/public-ip-list/). If that list of shared IP addresses is too large, consider sending traffic to an https server or (non-Adobe) Azure Blob Store where logic can be written to send the logs out of a dedicated IP to their ultimate destination. 

For AEM logs (including Apache/Dispatcher), if you have configured [advanced networking](/help/security/configuring-advanced-networking.md), you can use the advancedNetworking property to forward them from a dedicated egress IP address or over a VPN.

   ```
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
       aem:
         advancedNetworking: true
   ```
