---
title: Config Pipeline
description: Learn about how the Config Pipeline works in AEM as a Cloud Service and how to configure it.
feature: Operations
role: Admin
---
# Config Pipeline in AEM as a Cloud Service {#config-pipeline-in-aem-as-a-cloud-service}

The Cloud Manager Config Pipeline deploys one or more configuration (yaml) files to a target environment.

Config Pipeline supports configuration of the following features:

| **Type**   | **"kind" value in yaml** | **Description**  |
|---|---|---|
| [Traffic Filter Rules, including WAF](/help/security/traffic-filter-rules-including-waf.md) | CDN | Declare rules to block malicious traffic. |
| [Request Transformations](/help/implementing/dispatcher/cdn-configuring-traffic.md#request-transformations)  | CDN | Declare rules to transform the shape of the traffic request. |
| [Response Transformations](/help/implementing/dispatcher/cdn-configuring-traffic.md#response-transformations)  | CDN | Declare rules to transform the shape of the  response for a given request. |
| [Client-side Redirects](/help/implementing/dispatcher/cdn-configuring-traffic.md#client-side-redirectors)  | CDN | Declare 301/302-style client-side redirects. Sign up as an early adopter. |
| [Origin Selectors](/help/implementing/dispatcher/cdn-configuring-traffic.md#origin-selectors)  | CDN | Declare rules to route traffic to different backends, including non-Adobe applications. |
| [CDN error pages](/help/implementing/dispatcher/cdn-error-pages.md) | CDN | Override the default error page if AEM origin cannot be reached, referencing the location of self-hosted static content in the configuration file.  |
| [CDN Purge](/help/implementing/dispatcher/cdn-credentials-authentication.md#purge-API-token) | CDN | Declare the Purge API keys used to purge the CDN. |
| [Customer-managed CDN HTTP token](/help/implementing/dispatcher/cdn-credentials-authentication.md#purge-API-token#CDN-HTTP-value) | CDN | Declare the value of the X-AEM-Edge-Key needed to call the Adobe CDN from a Customer CDN. |
| [Basic authentication](/help/implementing/dispatcher/cdn-credentials-authentication.md#purge-API-token#basic-auth) | CDN | Declare the usernames and passwords for a basic auth dialog protecting certain URLs. Sign up as an early adopter. |
| [Version Purge Maintenance Task](/help/operations/maintenance.md#purge-tasks) | MaintenanceTasks | Optimize the AEM repository by declaring rules around when content versions should be purged. |
| [Audit log Purge Maintenance Task](/help/operations/maintenance.md#purge-tasks) | MaintenanceTasks | Optimize the AEM audit log for increased performance by declaring rules around when logs should be purged. |
| [Log forwarding](/help/implementing/developing/introduction/log-forwarding.md) | LogForwarding | Configure the endpoints and credentials for forwarding logs to various destinations (e.g., Splunk, Datadog, HTTPS). This feature is not yet available. |


This article describes concepts shared across either all or a subset of the features supported by Config Pipelines.

It should be pointed out that each feature has its own dedicated article or section of an article detailing its unique syntax; when appropriate, this shared article is referenced. 

Configuration Pipleines can be deployed via Cloud Manager to dev, stage, and production environment types in production (non-sandbox) programs. RDEs are not currently supported.

## Common syntax {#common-syntax}

All configuration files begin with properties resembling the following example snippet:

 ```
   kind: "LogForwarding"
   version: "1"
   metadata:
     envTypes: ["dev"]
```

| **Property**  | **Description**  | **Default**  |
|---|---|---|
|  **kind** | A string that determines which type of configuration. For example, log forwarding, traffic filter rules, or request transformations. | Required, no default |
|  **version** | A string representing the schema version. | Required, no default |
|  **envTypes** | This array of strings is a child property of the **metadata** node. Possible values are dev, stage, prod, and it determines for which environment types the configuration will be processed. For example, if the array only includes "dev", the configuration will not be loaded on stage or prod environments, even if the configuration is deployed to there. | All environment types, no default |

You can use `yq` to validate locally the YAML formatting of your configuration file (for example, `yq cdn.yaml`).

## Creating and managing the Config Pipeline in Cloud Manager{#managing-in-cloud-manager}

Review the Cloud Manager article for instructions around creating a [production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md) or [non-production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md). When creating a Config Pipeline, make sure to select a Targeted Deployment rather than Full Stack Code, and choose **Config**.

A folder `/config` should be at the top of the tree, with one more yaml files somewhere in a tree below it.

For example:

```
/config
  cdn.yaml
```

or

```
/config
  /dev
    cdn.yaml
```

Below `/config`, the folder names and filenames are arbitrary; the yaml file, however, must include a known `kind` property value.

Typically, you will want to deploy configurations to all environments. If all the property values are identical for each environment, a single yaml file will suffice. However, it is common for property values to differ between environments; for example, while testing a lower environment.

Here are some strategies, with the example file structures that include two configuration types.

### A single config file for all environments {#single-file}

The file structure will resemble:

```
/config
  cdn.yaml
  logForwarding.yaml
```

Use when the same configuration is sufficient for all environments, for all types of configuration (CDN, log forwarding, etc)
```
   kind: "cdn"
   version: "1"
   metadata:
     envTypes: ["dev", "stage", "prod"]
```

Using secret-type environment variables, it is possible for secret properties to vary per environment:

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

### A separate file per environment type {#file-per-env}

The file structure will resemble:

```
/config
  cdn-dev.yaml
  cdn-stage.yaml
  cdn-prod.yaml
  logForwarding-dev.yaml
  logForwarding-stage.yaml
  logForwarding-prod.yaml
```

Use this structure when there may be differences in property values. One would expect `cdn-dev.yaml` to have an envTypes array of ``dev``, `cdn-stage.yaml` to have an array of ``stage``, etc.

### A folder per environment {#folder-per-env}

In this strategy, there is a separate `config` folder per environment, and an independent pipeline is declared for each.

This approach is particularly useful if you have multiple dev envs, where each has unique property values.

The file structure will resemble:

```
/config/dev1
  cdn.yaml
  logForwarding.yaml
/config/dev2
  cdn.yaml
  logForwarding.yaml
/config/prod  
  cdn.yaml
  logForwarding.yaml
```

A variation of this approach is to maintain a separate branch per environment.

## Secret environment variables {#secret-env-vars}

So that sensitive information need not be stored in source control, configuration files support Cloud Manager *Environment Variables* of type *secret*. In fact, for some configurations, including log forwarding, secret environment variables are mandatory for certain properties.

See Cloud Manager Environment Variables article for how to [define these secrets](/help/implementing/cloud-manager/environment-variables.md).

See the snippet below for an example of how the secret  `${{SPLUNK_TOKEN}}` is used as a token in the configuration.

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