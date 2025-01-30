---
title: Using Config Pipelines
description: Learn how you can use config pipelines to deploy different configurations AEM as a Cloud Service such as log forwarding settings, purge-related maintenance tasks, and various CDN configurations.
feature: Operations
role: Admin
exl-id: bd121d31-811f-400b-b3b8-04cdee5fe8fa
---
# Using Config Pipelines {#config-pipelines}

Learn how you can use config pipelines to deploy different configurations AEM as a Cloud Service such as log forwarding settings, purge-related maintenance tasks, and various CDN configurations.

## Overview {#overview}

A Cloud Manager config pipeline deploys configurations files (created in YAML format) to a target environment. A number of features in AEM as a Cloud Service can be configured in this way, including log forwarding, purge-related maintenance tasks, and several CDN features.

Config pipelines can be deployed via Cloud Manager to dev, stage, and production environment types. The configuration files can be deployed to Rapid Development Environments (RDEs) using [command line tooling](/help/implementing/developing/introduction/rapid-development-environments.md#deploy-config-pipeline).

This following sections of this document give an overview of important information regarding how config pipelines can be used and how configurations for them should be structured. It describes general concepts shared across either all or a subset of the features supported by config pipelines.

* [Supported Configurations](#configurations) - A list of configurations that can be deployed with config pipelines
* [Creating and Managing Config Pipelines](#creating-and-managing) - How to create a config pipeline.
* [Common Syntax](#common-syntax) - Syntax shared across configurations
* [Folder Structure](#folder-structure) - Describes the structure config pipelines expect for the configurations
* [Secret environment variables](#secret-env-vars) - Examples of using environment variables to not disclose secrets in your configurations

## Supported Configurations {#configurations}

The following table offers a comprehensive list of such configurations with links to dedicated documentation describing its distinct configuration syntax and other information.

| Type   | YAML `kind` Value | Description  |
|---|---|---|
| [Traffic Filter Rules, including WAF](/help/security/traffic-filter-rules-including-waf.md) | `CDN` | Declare rules to block malicious traffic |
| [Request Transformations](/help/implementing/dispatcher/cdn-configuring-traffic.md#request-transformations)  | `CDN` | Declare rules to transform the shape of the traffic request |
| [Response Transformations](/help/implementing/dispatcher/cdn-configuring-traffic.md#response-transformations)  | `CDN` | Declare rules to transform the shape of the response for a given request |
| [Client-side Redirects](/help/implementing/dispatcher/cdn-configuring-traffic.md#client-side-redirectors)  | `CDN` | Declare 301/302-style client-side redirects |
| [Origin Selectors](/help/implementing/dispatcher/cdn-configuring-traffic.md#origin-selectors)  | `CDN` | Declare rules to route traffic to different backends, including non-Adobe applications |
| [CDN error pages](/help/implementing/dispatcher/cdn-error-pages.md) | `CDN` | Override the default error page if AEM origin cannot be reached, referencing the location of self-hosted static content in the configuration file  |
| [CDN Purge](/help/implementing/dispatcher/cdn-credentials-authentication.md#purge-API-token) | `CDN` | Declare the Purge API keys used to purge the CDN |
| [Customer-managed CDN HTTP token](/help/implementing/dispatcher/cdn-credentials-authentication.md#purge-API-token#CDN-HTTP-value) | `CDN` | Declare the value of the X-AEM-Edge-Key needed to call the Adobe CDN from a Customer CDN |
| [Basic authentication](/help/implementing/dispatcher/cdn-credentials-authentication.md#purge-API-token#basic-auth) | `CDN` | Declare the usernames and passwords for a basic auth dialog protecting certain URLs. |
| [Version Purge Maintenance Task](/help/operations/maintenance.md#purge-tasks) | `MaintenanceTasks` | Optimize the AEM repository by declaring rules around when content versions should be purged |
| [Audit log Purge Maintenance Task](/help/operations/maintenance.md#purge-tasks) | `MaintenanceTasks` | Optimize the AEM audit log for increased performance by declaring rules around when logs should be purged |
| [Log forwarding](/help/implementing/developing/introduction/log-forwarding.md) | `LogForwarding` | Configure the endpoints and credentials for forwarding logs to various destinations, including Azure Blob Storage, Datadog, HTTPS, Elasticsearch, Splunk) |

## Creating and Managing Config Pipelines {#creating-and-managing}

For information on how to create and configure pipelines, please see the document [CI/CD Pipelines.](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#config-deployment-pipeline)

When creating a config pipeline in Cloud Manager, be sure to select a **Targeted Deployment** rather than **Full Stack Code** when configuring the pipeline.

As noted earlier, configuration for RDEs is deployed using [command line tooling](/help/implementing/developing/introduction/rapid-development-environments.md#deploy-config-pipeline) rather than a pipeline.


## Common Syntax {#common-syntax}

Each configuration file begins with properties resembling the following example snippet:

 ```yaml
   kind: "LogForwarding"
   version: "1"
   metadata:
     envTypes: ["dev"]
```

| Property  | Description  | Default  |
|---|---|---|
|  `kind` | A string that determines which type of configuration, such as log forwarding, traffic filter rules, or request transformations | Required, no default |
|  `version` | A string representing the schema version | Required, no default |
|  `envTypes` | This array of strings is a child property of the `metadata` node. Possible values are dev, stage, prod, or any combination, and it determines for which environment types the configuration will be processed. For example, if the array only includes `dev`, the configuration will not be loaded on stage or prod environments, even if the configuration is deployed there. | All environment types (dev, stage, prod)|

You can use the `yq` utility to validate locally the YAML formatting of your configuration file (for example, `yq cdn.yaml`).

## Folder Structure {#folder-structure}

A folder named `/config` or similar should be at the top of the tree, with one more YAML files somewhere in a tree below it.

For example:

```text
/config
  cdn.yaml
```

or

```text
/config
  /dev
    cdn.yaml
```

The folder names and filenames below `/config` are arbitrary. The YAML file, however, must include a valid [`kind` property value.](#configurations)

Typically, configurations are deployed to all environments. If all the property values are identical for each environment, a single YAML file will suffice. However, it is common for property values to differ between environments, for example while testing a lower environment.

The following sections illustrate some strategies for structuring your files.

### A Single Config File for All Environments {#single-file}

The file structure will resemble the following:

```text
/config
  cdn.yaml
  logForwarding.yaml
```

Use this structure when the same configuration is sufficient for all environments and for all types of configuration (CDN, log forwarding, and so on). In this scenario, the `envTypes` array property would include all environment types.

```yaml
   kind: "cdn"
   version: "1"
   metadata:
     envTypes: ["dev", "stage", "prod"]
```

Using secret-type environment variables, it is possible for [secret properties](#secret-env-vars) to vary per environment, as illustrated by the `${{SPLUNK_TOKEN}}` reference

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

### A Separate File Per Environment Type {#file-per-env}

The file structure will resemble the following:

```text
/config
  cdn-dev.yaml
  cdn-stage.yaml
  cdn-prod.yaml
  logForwarding-dev.yaml
  logForwarding-stage.yaml
  logForwarding-prod.yaml
```

Use this structure when there may be differences in property values. In the files, one would expect the `envTypes` array value to correspond with the suffix, for example 
`cdn-dev.yaml` and `logForwarding-dev.yaml` with a value of `["dev"]`, `cdn-stage.yaml` and `logForwarding-stage.yaml` with a value of `["stage"]`, and so on.

### A Folder Per Environment {#folder-per-env}

In this strategy, there is a separate `config` folder per environment, with a separate pipeline declared in Cloud Manager for each.

This approach is particularly useful if you have multiple dev environments, where each has unique property values.

The file structure will resemble the following:

```text
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

## Secret Environment Variables {#secret-env-vars}

So that sensitive information need not be stored in source control, configuration files support Cloud Manager environment variables of type **secret**. For some configurations, including log forwarding, secret environment variables are mandatory for certain properties.

The snippet below is an example of how the secret environment variable `${{SPLUNK_TOKEN}}` is used in the configuration.

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

Please see the document [Cloud Manager Environment Variables](/help/implementing/cloud-manager/environment-variables.md) for details on how to use environment variables.
