---
title: Index Converter
description: Index Converter
---

# Index Converter {#index-converter}

Index Converter is a utility developed to migrate a customer's index definition in preparation for the move to AEM as a Cloud Service.

## Introduction {#introduction}

Index Converter allows AEM developers to migrate existing Custom Oak Index Definitions to AEM as a Cloud Service compatible Custom Oak Index Definitions.

>[!NOTE]
>Index Converter only transforms *lucene* type Custom Oak Index Definitions which are present under `/apps` or `/oak:index`. It does not transform *lucene* type indexes which are created for `nt:base`.

There are two ways to create Custom Oak Index Definitions:

* `under /apps` (through any custom content package)
* directly under `/oak:index` path

>[!NOTE]
>Refer to [Ensure Oak Index](https://adobe-consulting-services.github.io/acs-aem-commons/features/ensure-oak-index/index.html) to learn how to define and create Oak Definitions

## Using the Index Converter {#using-index-converter}

>[!NOTE]
>While it is recommended to use Index Converter tool via [AIO CLI plugin for source migration](https://github.com/adobe/aio-cli-plugin-aem-cloud-service-migration), it can also be executed standalone.

Refer to **[Git Resource: aem-cs-source-migration-index-converter](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/index-converter)** to learn how to install and use the plugin.

