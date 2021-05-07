---
title: Index Converter
description: Index Converter
exl-id: e6a3ec6d-cc02-4f5b-8b1d-ea481d6884ca
---
# Index Converter {#index-converter}

Index Converter is a utility developed to migrate a customer's Index Definitions in preparation for the move to AEM as a Cloud Service.

## Introduction {#introduction}

The Index Converter allows AEM developers to migrate existing Custom Oak Index Definitions to AEM as a Cloud Service compatible Custom Oak Index Definitions.

>[!NOTE]
>Index Converter only transforms *lucene* type Custom Oak Index Definitions which are present under `/apps` or `/oak:index`. It does not transform *lucene* type indexes which are created for `nt:base`.

There are two ways to create Custom Oak Index Definitions:

* `under /apps` (through any custom content package)
* directly under `/oak:index` path

If [Ensure Oak Index](https://adobe-consulting-services.github.io/acs-aem-commons/features/ensure-oak-index/index.html) was used, please note that Ensure Definitions are not supported on AEM as a Cloud Service, and hence they need to be converted to Oak Index Definitions first and then need to be migrated to Custom Oak Index Definitions that are compatible with AEM as a Cloud Service as per below guidelines:

* If property ignore is set to `true`, ignore or skip the Ensure Definition
* Update the `jcr:primaryType` to `oak:QueryIndexDefinition`
* Remove any properties that are to be ignored as mentioned in OSGi configurations
* Remove subtree `/facets/jcr:content` from Ensure Definition

## Using the Index Converter {#using-index-converter}

* Via Adobe I/O CLI : It is recommended to use the Index Converter via `aio-cli-plugin-aem-cloud-service-migration` (AEM as a Cloud Service code refactoring plugin for the Adobe I/O CLI).

   Refer to **[Git Resource: aio-cli-plugin-aem-cloud-service-migration](https://github.com/adobe/aio-cli-plugin-aem-cloud-service-migration#introduction)** to learn how to install and use the plugin.

* As a standalone utility : The Index Converter can also be executed as a standalone utility.

   Refer to **[Git Resource: aem-cs-source-migration-index-converter](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/index-converter)** to learn how to use this tool.
