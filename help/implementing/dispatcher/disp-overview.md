---
title: Dispatcher in the Cloud
description: Dispatcher in the Cloud 
feature: Dispatcher
exl-id: 6d78026b-687e-434e-b59d-9d101349a707
---
# Dispatcher in the Cloud {#Dispatcher-in-the-cloud}

>[!CONTEXTUALHELP]
>id="aemcloud_nonbpa_dispoverview"
>title="Dispatcher in the Cloud"
>abstract="This section describes how to structure the AEM as a Cloud Service Apache and Dispatcher configurations, as well as how to validate  and run it locally before deploying to Cloud environments. It also describes debugging in Cloud environments."

## Introduction {#apache-and-dispatcher-configuration-and-testing}

**This section will need to be changed since we no longer detail the things below on this page**

This section describes how to structure the AEM as a Cloud Service Apache and Dispatcher configurations, as well as how to validate  and run it locally before deploying to Cloud environments. It also describes debugging in Cloud environments. For additional information about Dispatcher, see the [AEM Dispatcher documentation](https://experienceleague.adobe.com/docs/experience-manager-dispatcher/using/dispatcher.html).

>[!NOTE]
>Windows users need to use Windows 10 Professional or other distributions that support Docker. This is a pre-requisite for running and debugging Dispatcher on a local computer. The sections below include commands using the Mac or Linux versions of the SDK, but the Windows SDK can be used in a similar way.

## Dispatcher Tools {#dispatcher-sdk}

The Dispatcher Tools are part of the overall AEM as a Cloud Service SDK and provide:

* A vanilla file structure containing the configuration files to include in a maven project for Dispatcher.
* Tooling for customers to validate that the Dispatcher configuration includes only AEM as a Cloud Service supported directives.        Additionally, the tooling also validates that the syntax is correct so apache can start successfully.
* A Docker image that brings up the Dispatcher locally.

**To Brian: Anything else to add/change here?**

## Downloading and Extracting the Tools {#extracting-the-sdk}

The Dispatcher Tools, part of the [AEM as a Cloud Service SDK](/help/implementing/developing/introduction/aem-as-a-cloud-service-sdk.md), can be downloaded from a zip file at the [Software Distribution](https://downloads.experiencecloud.adobe.com/content/software-distribution/en/aemcloud.html) portal. Any new configuration available in that new Dispatcher Tools version can be used to deploy to Cloud environments running that version of AEM in the Cloud or higher.

Unzip the SDK, which bundles Dispatcher Tools for both macOS, Linux and Windows.

**For macOS/Linux**, make the Dispatcher tool artifact executable and run it. It will self-extract the Dispatcher Tools files underneath the directory you stored it to (where `version` is the version of the Dispatcher Tools).

```bash
$ chmod +x aem-sdk-dispatcher-tools-<version>-unix.sh
$ ./aem-sdk-dispatcher-tools-<version>-unix.sh
Verifying archive integrity...  100%   All good.
Uncompressing aem-sdk-dispatcher-tools-<version>-unix.sh 100%
```

**For Windows**, extract the Dispatcher Tooling zip archive.

To understand how to use the Dispatcher Tools see each mode's page **Link TBD (maybe we can add this as a note for visibility**.

## Supported Apache Modules {#supported-directives}

The table below shows the supported apache modules:

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

**To Brian: This is here just for added visibility. Functionally, each mode's page contains the list above and info about the allowlist, how to use etc. so I'm not sure if we need to add anything else on the chapter above (on this page)**

## Folder Structure {#folder-structure}

**To Brian: We need some info here about Achetype 28, so customers that land on this page have some context on the changes.**

With the CM 2021.7.0 release, there are two modes that will influence the structure and details of the validation:

1. **Flexible mode** - the recommended mode, and the default for AEM archetype 28, which is also used by Cloud Manager for new environments created after the CM 2021.7.0 release. Customers can activate this mode by adding the folder and file `opt-in/USE_SOURCES_DIRECTLY`. With this mode there are no limitations in the file structure under the rewrites folder, which in legacy mode required a single `rewrite.rules` file. Also, there is no limitation on the number of rules you can add. For details around folder structure and local validation using, see the "Flexible mode" page **link TBD**.

2. **Legacy mode** - for details around the folder structure and local validation for Legacy mode, see the "Legacy mode" page. **link TBD**

For details on how to migrate the Dispatcher configuration from AMS to AEM as a Cloud Service, see the Migrating the Dispatcher configuration from AMS to AEM as a Cloud Service page.**link TBD**

To understand how to use the Dispatcher Tools see each mode's page **Link TBD (maybe we can add this as a note for visibility**.
