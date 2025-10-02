---
title: Use Config Pipelines
description: Learn how you can use config pipelines to deploy different configurations in AEM as a Cloud Service such as log forwarding settings, purge-related maintenance tasks, and various CDN configurations.
feature: Operations
role: Admin
exl-id: bd121d31-811f-400b-b3b8-04cdee5fe8fa
---
# Use config pipelines {#config-pipelines}

Learn how you can use config pipelines to deploy different configurations in AEM as a Cloud Service such as log forwarding settings, purge-related maintenance tasks, and various CDN configurations.

## Overview {#overview}

A Cloud Manager config pipeline deploys configurations files (created in YAML format) to a target environment. A number of features in AEM as a Cloud Service can be configured in this way, including log forwarding, purge-related maintenance tasks, and several CDN features.

For **Publish Delivery** Projects, config pipelines can be deployed via Cloud Manager to dev, stage, and production environment types. The configuration files can be deployed to Rapid Development Environments (RDEs) using [command line tooling](/help/implementing/developing/introduction/rapid-development-environments.md#deploy-config-pipeline).

Config pipelines can also be deployed through Cloud Manager for **Edge Delivery** Projects.

This following sections of this document give an overview of important information regarding how config pipelines can be used and how configurations for them should be structured. It describes general concepts shared across either all or a subset of the features supported by config pipelines.

* [Supported Configurations](#configurations) - A list of configurations that can be deployed with config pipelines
* [Creating and Managing Config Pipelines](#creating-and-managing) - How to create a config pipeline
* [Common Syntax](#common-syntax) - Syntax shared across configurations
* [Folder Structure](#folder-structure) - Describes the structure config pipelines expect for the configurations
* [Secret environment variables](#secret-env-vars) - Examples of using environment variables to not disclose secrets in your configurations
* [Secret pipeline variables](#secret-pipeline-vars) - Examples of using environment variables to not disclose secrets in your configurations fore Edge Delivery Services projects

## Supported configurations {#configurations}

The following table offers a comprehensive list of such configurations with links to dedicated documentation describing its distinct configuration syntax and other information.

| Type   | YAML `kind` Value | Description  | Publish Delivery | Edge Delivery |
|---|---|---|---|---|
| [Traffic Filter Rules, including WAF](/help/security/traffic-filter-rules-including-waf.md) | `CDN` | Declare rules to block malicious traffic | X | X |
| [Request Transformations](/help/implementing/dispatcher/cdn-configuring-traffic.md#request-transformations)  | `CDN` | Declare rules to transform the shape of the traffic request | X | X |
| [Response Transformations](/help/implementing/dispatcher/cdn-configuring-traffic.md#response-transformations)  | `CDN` | Declare rules to transform the shape of the response for a given request | X | X |
| [Server-side Redirects](/help/implementing/dispatcher/cdn-configuring-traffic.md#server-side-redirectors)  | `CDN` | Declare 301/302-style server-side redirects | X | X |
| [Origin Selectors](/help/implementing/dispatcher/cdn-configuring-traffic.md#origin-selectors)  | `CDN` | Declare rules to route traffic to different backends, including non-Adobe applications | X | X |
| [CDN error pages](/help/implementing/dispatcher/cdn-error-pages.md) | `CDN` | Override the default error page if AEM origin cannot be reached, referencing the location of self-hosted static content in the configuration file  | X |  |
| [CDN Purge](/help/implementing/dispatcher/cdn-credentials-authentication.md#purge-API-token) | `CDN` | Declare the Purge API keys used to purge the CDN | X |  |
| [Customer-managed CDN HTTP token](/help/implementing/dispatcher/cdn-credentials-authentication.md#purge-API-token#CDN-HTTP-value) | `CDN` | Declare the value of the X-AEM-Edge-Key needed to call the Adobe CDN from a Customer CDN | X |  |
| [Basic authentication](/help/implementing/dispatcher/cdn-credentials-authentication.md#purge-API-token#basic-auth) | `CDN` | Declare the usernames and passwords for a basic auth dialog protecting certain URLs. | X | X |
| [Version Purge Maintenance Task](/help/operations/maintenance.md#purge-tasks) | `MaintenanceTasks` | Optimize the AEM repository by declaring rules around when content versions should be purged | X |  |
| [Audit log Purge Maintenance Task](/help/operations/maintenance.md#purge-tasks) | `MaintenanceTasks` | Optimize the AEM audit log for increased performance by declaring rules around when logs should be purged | X |  |
| [Log forwarding](/help/implementing/developing/introduction/log-forwarding.md) | `LogForwarding` | Configure the endpoints and credentials for forwarding logs to various destinations, including Azure Blob Storage, Datadog, HTTPS, Elasticsearch, Splunk | X | X |
| [Registering a Client ID](/help/implementing/developing/open-api-based-apis.md) | `API` | Scope Adobe Developer Console API projects to a specific AEM environments by registering the client ID. This is needed for usage of OpenAPI-based APIs that require authentication | X |  |

## Create and manage config pipelines {#creating-and-managing}

For information on how to create and configure **Publish Delivery** config pipelines, see [CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#config-deployment-pipeline). When creating a config pipeline in Cloud Manager, be sure to select a **Targeted Deployment** rather than **Full Stack Code** when configuring the pipeline. As noted earlier, configuration for RDEs is deployed using [command line tooling](/help/implementing/developing/introduction/rapid-development-environments.md#deploy-config-pipeline) rather than a pipeline.

For information on how to create and configure **Edge Delivery** config pipelines, see the [Add an Edge Delivery pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-edge-delivery-pipeline.md) article.

## Common syntax {#common-syntax}

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
| `envTypes` | This array of strings is a child property of the `metadata` node. For **Publish Delivery**, possible values are dev, stage, prod, or any combination, and it determines for which environment types the configuration will be processed. For example, if the array only includes `dev`, the configuration will not be loaded on stage or prod environments, even if the configuration is deployed there. For **Edge Delivery**, only a value of `prod` should be used | All environment types, which is (dev, stage, prod) for Publish Delivery or just prod for Edge Delivery |

You can use the `yq` utility to validate locally the YAML formatting of your configuration file (for example, `yq cdn.yaml`).

## Folder structure {#folder-structure}

A folder named `/config` or similar should be at the top of the tree, with one more YAML files somewhere in a tree below it.

For example:

```text
/config
  cdn.yaml
```

Or

```text
/config
  /dev
    cdn.yaml
```

The folder names and filenames below `/config` are arbitrary. The YAML file, however, must include a valid [`kind` property value](#configurations).

Typically, configurations are deployed to all environments. If all the property values are identical for each environment, a single YAML file is sufficient. However, it is common for property values to differ between environments, for example while testing a lower environment.

The following sections illustrate some strategies for structuring your files.

### A single config file for all environments {#single-file}

The file structure resembles the following:

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

Using secret-type environment (or pipeline) variables, it is possible for [secret properties](#secret-env-vars) to vary per environment, as illustrated by the following `${{SPLUNK_TOKEN}}` reference.

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

### A separate file per environment type {#file-per-env}

The file structure resembles the following:

```text
/config
  cdn-dev.yaml
  cdn-stage.yaml
  cdn-prod.yaml
  logForwarding-dev.yaml
  logForwarding-stage.yaml
  logForwarding-prod.yaml
```

Use this structure when there may be differences in property values. In the files, one would expect the `envTypes` array value to correspond with the suffix. For example,`cdn-dev.yaml` and `logForwarding-dev.yaml` with a value of `["dev"]`, `cdn-stage.yaml` and `logForwarding-stage.yaml` with a value of `["stage"]`, and so on.

### A folder per environment {#folder-per-env}

In this strategy, there is a separate `config` folder per environment, with a separate pipeline declared in Cloud Manager for each.

This approach is particularly useful if you have multiple dev environments, where each has unique property values.

The file structure resembles the following:

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

### Edge Delivery Services {#yamls-for-eds}

Edge Delivery config pipelines do not have separate development, staging, and production environments. Unlike Publish Delivery environments, where changes progress through dev, stage, and prod tiers, the configuration deployed through an Edge Delivery config pipeline is applied directly to all domain mappings registered in Cloud Manager with an Edge Delivery Site.

Thus, deploy a simple file structure like:

```text
/config
  cdn.yaml
  logForwarding.yaml
```

If a rule needs to differ per Edge Delivery Site, use the *when* syntax to distinguish the rules from each other. For example, notice that the domain matches dev.example.com in the snippet below, which can be distinguished from the domain www.example.com.

```
kind: "CDN"
version: "1"
data:
  trafficFilters:
    rules:
    # Block simple path
    - name: block-path
      when:
        allOf:
          - reqProperty: domain
            equals: "dev.example.com"
          - reqProperty: path
            equals: '/block/me'
      action: block
```

If including the *envTypes* metadata field, only the value **prod** should be used (omitting the envTypes metadata field is also fine). For the *tier* reqProperty, only the value **publish** should be used.  

## Secret environment variables {#secret-env-vars}

So that sensitive information need not be stored in source control, configuration files support Cloud Manager environment variables of type **secret**. For some configurations, including log forwarding, secret environment variables are mandatory for certain properties.

Note that secret environment variables are used for Publish Delivery projects; see the Secret Pipeline Variables section for Edge Delivery Services projects.

The following snippet is an example of how the secret environment variable `${{SPLUNK_TOKEN}}` is used in the configuration.

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

## Secret Pipeline Variables {#secret-pipeline-vars}

For Edge Delivery Services Projects, use Cloud Manager pipeline variables of type **secret** so sensitive information need not be stored in source control. The *Step Applied* select box should use the **deploy** option. 

The syntax is identical to the snippet shown in the previous section.

Please see the document [Pipeline Variables in Cloud Manager](/help/implementing/cloud-manager/configuring-pipelines/pipeline-variables.md) for details on how to use pipeline variables.
