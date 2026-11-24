---
title: Dispatcher in the Cloud
description: Learn about Dispatcher tools, the supported Apache modules and the legacy and flexible modes.
feature: Dispatcher
exl-id: 6d78026b-687e-434e-b59d-9d101349a707
role: Admin
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: 2741637d-a621-529a-b21b-bfe9be07a9c8
    internal-label: Dispatcher
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
---
# Dispatcher in the Cloud {#Dispatcher-in-the-cloud}

>[!CONTEXTUALHELP]
>id="aemcloud_nonbpa_dispoverview"
>title="Dispatcher in the Cloud"
>abstract="This page describes how to download and extract the Dispatcher tools, the supported Apache modules, and provides a high-level overview of the legacy and flexible modes."

## Introduction {#apache-and-dispatcher-configuration-and-testing}

This page describes the Dispatcher tools and how to download and extract them, lists the supported Apache modules, and provides a high-level overview of the legacy and flexible modes. Also, there are further references on validation, debugging, and migrating the Dispatcher configuration from AMS to AEM as a Cloud Service. <!-- ERROR: NOT FOUND (HTTP ERROR 404) Also, see [this video](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-5/cloud5-aem-dispatcher-cloud.html) for additional details about deploying dispatcher files in a cloud service environment. -->

## Dispatcher Tools {#dispatcher-sdk}

The Dispatcher Tools are part of the overall AEM as a Cloud Service SDK and provide:

* A standard file structure containing the configuration files to include in a maven project for Dispatcher.
* To validate that the Dispatcher configuration includes only AEM as a Cloud Service-supported directives, use this tooling. Also, the tooling validates that the syntax is correct so Apache can start successfully.
* A Docker image that starts the Dispatcher locally.

## Downloading and Extracting the Tools {#extracting-the-sdk}

The Dispatcher Tools, part of the [AEM as a Cloud Service SDK](/help/implementing/developing/introduction/aem-as-a-cloud-service-sdk.md), can be downloaded from a zip file at the [Software Distribution](https://downloads.experiencecloud.adobe.com/content/software-distribution/en/aemcloud.html) portal. Any new configuration available in that new Dispatcher Tools version can be used to deploy to Cloud environments running that version of AEM in the Cloud or higher.

Unzip the SDK, which bundles Dispatcher Tools for macOS, Linux&reg; and Windows.

**For macOS/Linux**, make the Dispatcher tool artifact executable and run it. It extracts the Dispatcher Tools files into the directory where you stored them (where `version` is the version of the Dispatcher Tools).

```bash
$ chmod +x aem-sdk-dispatcher-tools-<version>-unix.sh
$ ./aem-sdk-dispatcher-tools-<version>-unix.sh
Verifying archive integrity...  100%   All good.
Uncompressing aem-sdk-dispatcher-tools-<version>-unix.sh 100%

```

**For Windows**, extract the Dispatcher Tooling zip archive.

## Validation and Debugging using the Dispatcher Tools {#validation-debug}

The Dispatcher tools are used to validate and debug your project's Dispatcher configuration. Learn more about how to use those tools in the pages referenced below, based on whether your project's Dispatcher configuration is structured in flexible mode or legacy mode:

* **Flexible mode** - the recommended mode, and the default for AEM archetype 28 and higher, which Cloud Manager also uses for new environments created after the Cloud Manager 2021.7.0 release. Customers can activate this mode by adding the folder and file `opt-in/USE_SOURCES_DIRECTLY`. With this more flexible mode, there are no limitations in the file structure under the rewrites folder that required a single `rewrite.rules` file in legacy mode. Also, there is no limitation on the number of rules you can add. For details on folder structure and local validation, see [Validating and Debugging using Dispatcher Tools](/help/implementing/dispatcher/validation-debug.md).

* **Legacy mode** - For details on the folder structure and local validation for Dispatcher configuration legacy mode, see [Validating and Debugging using Dispatcher Tools (Legacy)](/help/implementing/dispatcher/validation-debug-legacy.md)

For more information on how to migrate from the legacy configuration model to the more flexible one, provided with AEM archetype 28 and onward, see [this documentation](/help/implementing/dispatcher/validation-debug.md#migrating).
  
## Content Disposition {#content-disposition}

For the publish tier, the default for serving blobs is as an attachment. Override this setting using the standard [content disposition header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition) in the Dispatcher.

The following is an example of how the configuration looks:

```
<LocationMatch "^\/content\/dam.*\.(pdf).*">
 Header unset Content-Disposition
 Header set Content-Disposition inline
</LocationMatch>
```

## Supported Apache Modules {#supported-directives}

The table below shows the supported Apache modules:

| Module Name | Reference Page |
|---|---|
| `core` | [https://httpd.apache.org/docs/2.4/mod/core.html](https://httpd.apache.org/docs/2.4/mod/core.html) |
| `mod_access_compat` | [https://httpd.apache.org/docs/2.4/mod/mod_access_compat.html](https://httpd.apache.org/docs/2.4/mod/mod_access_compat.html) |
| `mod_alias` | [https://httpd.apache.org/docs/2.4/mod/mod_alias.html](https://httpd.apache.org/docs/2.4/mod/mod_alias.html) |
| `mod_allowmethods` | [https://httpd.apache.org/docs/2.4/mod/mod_allowmethods.html](https://httpd.apache.org/docs/2.4/mod/mod_allowmethods.html) |
| `mod_authn_core` | [https://httpd.apache.org/docs/2.4/mod/mod_authn_core.html](https://httpd.apache.org/docs/2.4/mod/mod_authn_core.html) |
| `mod_authn_file` | [https://httpd.apache.org/docs/2.4/mod/core.html](https://httpd.apache.org/docs/2.4/mod/mod_authn_file.html) |
| `mod_authz_core` | [https://httpd.apache.org/docs/2.4/mod/core.html](https://httpd.apache.org/docs/2.4/mod/mod_authz_core.html) |
| `mod_authz_groupfile` | [https://httpd.apache.org/docs/2.4/mod/mod_authz_groupfile.html](https://httpd.apache.org/docs/2.4/mod/mod_authz_groupfile.html) |
| `mod_deflate` | [https://httpd.apache.org/docs/2.4/mod/mod_deflate.html](https://httpd.apache.org/docs/2.4/mod/mod_deflate.html) |
| `mod_dir` | [https://httpd.apache.org/docs/2.4/mod/mod_dir.html](https://httpd.apache.org/docs/2.4/mod/mod_dir.html) |
| `mod_env` | [https://httpd.apache.org/docs/2.4/mod/mod_env.html](https://httpd.apache.org/docs/2.4/mod/mod_env.html) |
| `mod_filter` | [https://httpd.apache.org/docs/2.4/mod/mod_filter.html](https://httpd.apache.org/docs/2.4/mod/mod_filter.html) |
| `mod_headers` | [https://httpd.apache.org/docs/2.4/mod/mod_headers.html](https://httpd.apache.org/docs/2.4/mod/mod_headers.html) |
| `mod_mime` | [https://httpd.apache.org/docs/2.4/mod/mod_mime.html](https://httpd.apache.org/docs/2.4/mod/mod_mime.html) |
| `mod_proxy` | [https://httpd.apache.org/docs/2.4/mod/mod_proxy.html](https://httpd.apache.org/docs/2.4/mod/mod_proxy.html) |
| `mod_proxy_http` | [https://httpd.apache.org/docs/2.4/mod/mod_proxy_http.html](https://httpd.apache.org/docs/2.4/mod/mod_proxy_http.html) |
| `mod_remoteip` | [https://httpd.apache.org/docs/2.4/mod/mod_remoteip.html](https://httpd.apache.org/docs/2.4/mod/mod_remoteip.html) |
| `mod_reqtimeout` | [https://httpd.apache.org/docs/2.4/mod/mod_reqtimeout.html](https://httpd.apache.org/docs/2.4/mod/mod_reqtimeout.html) |
| `mod_rewrite` | [https://httpd.apache.org/docs/2.4/mod/mod_rewrite.html](https://httpd.apache.org/docs/2.4/mod/mod_rewrite.html) |
| `mod_security` | [https://modsecurity.org/](https://modsecurity.org/) |
| `mod_setenvif` | [https://httpd.apache.org/docs/2.4/mod/mod_setenvif.html](https://httpd.apache.org/docs/2.4/mod/mod_setenvif.html) |
| `mod_ssl (only the SSLProxyEngine directive)` | [https://httpd.apache.org/docs/2.4/mod/mod_ssl.html#sslproxyengine](https://httpd.apache.org/docs/2.4/mod/mod_ssl.html#sslproxyengine) |
| `mod_substitute` | [https://httpd.apache.org/docs/2.4/mod/mod_substitute.html](https://httpd.apache.org/docs/2.4/mod/mod_substitute.html) |
| `mod_userdir` | [https://httpd.apache.org/docs/2.4/mod/mod_userdir.html](https://httpd.apache.org/docs/2.4/mod/mod_userdir.html) |
| `mod_macro` | [https://httpd.apache.org/docs/2.4/mod/mod_macro.html](https://httpd.apache.org/docs/2.4/mod/mod_macro.html) |
| `mod_include (no directives supported)` | [https://httpd.apache.org/docs/2.4/mod/mod_include.html](https://httpd.apache.org/docs/2.4/mod/mod_include.html) |


Customers cannot add arbitrary modules, however additional modules are considered for inclusion in the future. Customers can find the list of directives available for a given Dispatcher version by running the validator's allowlist command in the SDK.

The directives allowed in Apache configuration files can be listed by running the validator's allowlist command:

```

$ validator allowlist
Cloud manager validator 2.0.4
 
Allowlisted directives:
  <Directory>
  ...
  
```

## Folder Structure {#folder-structure}

The project's Apache and Dispatcher folder structure differs slightly based on which mode the project is using, as described in the [Validation and Debugging using the Dispatcher Tools](#validation-debug) section above.

## Deploy Dispatcher configurations {#deploy-dispatcher-configurations}

Cloud Manager deploys your Dispatcher configuration through a full stack pipeline or a Web Tier Config pipeline. A Web Tier Config pipeline deploys only the Dispatcher configuration.

When you configure a Web Tier Config pipeline, set **Code Location** to the folder that contains the `conf.d`, `conf.dispatcher.d`, and `opt-in` directories. For projects generated from the AEM Project Archetype with an unmodified structure, this folder is `/dispatcher/src`.

>[!IMPORTANT]
>
>If **Code Location** is `/` and your Dispatcher configuration is in a subfolder, the pipeline cannot find the `opt-in/USE_SOURCES_DIRECTLY` file and fails.

For the steps to configure these pipelines, see [Add a production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md#targeted-deployment) and [Add a non-production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#targeted-deployment). For more about Web Tier Config pipelines, see [CI/CD pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#web-tier-config-pipelines).

## Migrating the Dispatcher configuration from AMS {#ams-aem}

For details on how to migrate the Dispatcher configuration from AMS to AEM as a Cloud Service, see the [Migrating the Dispatcher configuration from AMS to AEM](/help/implementing/dispatcher/ams-aem.md) as a Cloud Service page.
