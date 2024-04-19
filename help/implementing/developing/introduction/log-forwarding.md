---
title: Log Forwarding for AEM as a Cloud Service
description: Learn about forwarding logs to Splunk and other logging vendors in AEM as a Cloud Service
hide: yes
hidefromtoc: yex
---

# Log Forwarding {#log-forwarding}

>[!NOTE]
>
>This feature is not release yet.

With AEM as a Cloud Service, logs can be forwarded to supported vendors. Currently, Splunk and Elasticsearch are supported, with more to follow soon.

Log forwarding is a self-service that can be configured by declaring the configuration in Git, and deploying it via the Configuration Pipeline. It includes AEM logs, Apache/Dispatcher logs, as well as CDN logs.

## Splunk Logs {#splunk-logs}

Customers who have Splunk accounts may request via customer support ticket that their AEM Cloud Service logs are forwarded to the appropriate index. The logging data is equivalent to what is available through the Cloud Manager log downloads, but customers may find it convenient to use the query features available in the Splunk product.

The network bandwidth associated with logs sent to Splunk are considered part of the customer's Network I/O usage.

CDN logs will be forwarded to Splunk for new support ticket requests; customers who already have Splunk forwarding enabled will be able to add CDN logs in the future.

### Enabling Splunk Forwarding {#enabling-splunk-forwarding}

In the support request, customers should indicate:

* Splunk HEC endpoint address. This endpoint must have a valid SSL certificate and be publicly accessible.
* The Splunk index
* The Splunk port 
* The Splunk HEC token. See [this page](https://docs.splunk.com/Documentation/Splunk/8.0.4/Data/HECExamples) for more information.

The properties above should be specified for each relevant program/environment type combination. For example, if a customer wanted dev, staging, and production environments, they should provide three sets of information, as indicated below. 

>[!NOTE]
>
>Splunk forwarding for sandbox program environments is not supported.

>[!NOTE]
>
>The Splunk forwarding capability is not possible from a dedicated egress IP address.

You should make sure that the initial request includes all dev environment that should be enabled, in addition to the stage/prod environments. Splunk must have an SSL certificate, and be public facing. 

If any new dev environments created after the initial request are intended to have Splunk forwarding, but do not have it enabled, an additional request should be made.

Also note that if dev environments have been requested, it is possible that other dev environments not in the request or even sandbox environments will have Splunk forwarding enabled and will share a Splunk index. Customers can use the `aem_env_id` field to distinguish between these environments.

Below you will find a sample customer support request:

Program 123, Production Env

* Splunk HEC endpoint address: `splunk-hec-ext.acme.com`
* Splunk index: acme_123prod (customer can choose whatever naming convention it wantes)
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