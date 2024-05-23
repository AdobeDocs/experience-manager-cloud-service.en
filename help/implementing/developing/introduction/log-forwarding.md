---
title: Log Forwarding for AEM as a Cloud Service
description: Learn about forwarding logs to Splunk and other logging vendors in AEM as a Cloud Service
hide: yes
hidefromtoc: yes
---

# Log Forwarding {#log-forwarding}

>[!NOTE]
>
>This self-serve feature is not yet released and some logging destinations may not be available at the time of release. In the meanwhile, you can open a support ticket to forward logs to **Splunk**. Learn more in the [logging article](help/implementing/developing/introduction/logging.md).

Customers who have a license for a logging vendor or host a logging product can have AEM, Apache/Dispatcher, and CDN logs forwarded to the associated logging destinations. AEM as a Cloud Service supports the following logging destinations: 

* Azure Blob Storage
* DataDog
* Elasticsearch or OpenSearch
* HTTPS
* OpenSearch
* Splunk
* Sumo Logic

Log forwarding is configured in a self-service manner by declaring a configuration in Git, and deploying it via the Cloud Manager Configuration Pipeline to dev, stage, and production environment types in production (non-sandbox) programs.

Note that the network bandwidth associated with logs sent to the logging destination are considered part of your organization's Network I/O usage.


## How This Article is Organized {#how-organized}

This article is organized in the following way:

* Setup - common for all logging destinations
* Logging destination configurations - each destination has a slightly different format
* Advanced networking - sending AEM and Apache/Dispatcher logs through a dedicated egress or through a VPN


## Setup {#setup}

1. Create the following folder and file structure the top-level folder in your project in Git:

   ```
   config/
        logForwarding.yaml
   ```

1. logForwarding.yaml should contain metadata and a configuration similar to the following format (we use Splunk as an example). 

   ```
   kind: "LogForwarding"
   version: "1"
   metadata:
     envTypes: ["dev"]
   data:
     splunk:
       default:
         host: "example.com"
         port: 8888 # Optional
         index: "AEMaaCS"
         token: "${{SPLUNK_TOKEN}}"
   
   ```
   
   The default node must be included for future compatibility reasons. 

   The kind parameter should be set to LogForwarding the version should be set to the schema version, which is 1.
   
   Tokens in the configuration (such as "${{SPLUNK_TOKEN}}") represent secrets, which should not be stored in Git. Instead, declare them as Cloud Manager  [Environment Variables](/help/implementing/cloud-manager/environment-variables.md) of Type "secret".
   
1. For environment types other than RDE (which is not currently supported), create a targeted deployment config pipeline in Cloud Manager.

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
   
Considerations:

* Authenticate using the SAS token, which should have a minimum validaty period.
* The SAS Token should be created on the account page, not the container page.
   
### Datadog {#datadog}

   ```
   kind: "LogForwarding"
   version: "1"
   metadata:
     envTypes: ["dev"]
   data:
     dataDog:
       default:
         enabled: true       
         host: "http-intake.logs.datadoghq.eu"
         token: "${{DATADOG_API_KEY}}"
         
   ```
   
Considerations:

* Create an API Key, without any integration with a specific cloud provider.
   

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
         url: "https://example.com/aem_logs/aem"
         authHeaderName: "X-AEMaaCS-Log-Forwarding-Token"
         authHeaderValue: "${{HTTPS_LOG_FORWARDING_TOKEN}}"
   
   ```
   
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
         index: "AEMaaCS"
   
   ```
   
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

## Advanced Networking {#advanced-networking}

If you have organizational requirements to lock down traffic to your logging vendor, you can configure [advanced networking](/help/security/configuring-advanced-networking.md) and configure the yaml's host and port accordingly. 

