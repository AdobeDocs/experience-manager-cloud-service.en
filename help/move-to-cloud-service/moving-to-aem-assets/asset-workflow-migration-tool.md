---
title: Asset Workflow Migration Tool
description: Asset Workflow Migration Tool
exl-id: 18490295-ead6-4691-8983-a6d4054e4264
---
# Asset Workflow Migration Tool {#asset-workflow-migration}

Asset Workflow Migration tool is used to automatically migrate asset processing workflows from on-premise or AMS deployments of AEM to processing profiles and OSGi Configurations for use in AEM Assets as a Cloud Service.

## Introduction {#introduction}

This section describes resources and implementation details on Asset Workflow Migration tool.

This utility allows the AEM developers to migrate existing AEM asset processing workflows to AEM as a Cloud Service.

## Supported workflows {#migration-support-for-workflows}

The workflows have varying level of migration support. See this [list of specific workflows](https://github.com/adobe/aem-cloud-migration/blob/master/src/main/resources/workflowSteps.properties). The workflows are categorized in the following categories based on the support provided. Adobe supports migration of the workflows that are listed in `SUPPORTED`, `REQUIRED`, or `OPTIONAL` categories. The workflow steps mentioned in the other categories are not supported.

* `SUPPORTED`: Supported functionality in [!DNL Experience Manager Assets] as a Cloud Service.
* `OPTIONAL`: Optional functionality in [!DNL Experience Manager Assets] as a Cloud Service.
* `REQUIRED`: A required step that is added to the workflow.
* `UNNECESSARY`: Functionality is not necessary in [!DNL Experience Manager Assets] as a Cloud Service.
* `NUI_OOTB`: Functionality provided by [Asset Compute Service](/help/assets/asset-microservices-configure-and-use.md).
* `DMS7_OOTB`: Functionality provided by default [!DNL Dynamic Media] connectors.
* `NUI_MIGRATED`: Migrated to a [processing profile for the Asset Compute Service](/help/assets/asset-microservices-configure-and-use.md).
* `UNSUPPORTED`: Currently not supported in [!DNL Experience Manager Assets] as a Cloud Service.

## Use Asset Workflow Migration tool {#use-workflow-migrator}

* **[!DNL Adobe I/O] CLI**: Adobe recommends using the Asset Workflow Migration tool via `aio-cli-plugin-aem-cloud-service-migration` ([!DNL Experience Manager] as a [!DNL Cloud Service] code refactoring plugin for the [!DNL Adobe I/O] CLI). To learn how to install and use the plugin, see [Git resource: aio-cli-plugin-aem-cloud-service-migration](https://github.com/adobe/aio-cli-plugin-aem-cloud-service-migration#introduction).

* **Standalone utility**: The Asset Workflow Migration Tool can also be executed as a standalone utility. To learn about installing and building code from the source, see **[Git resource: [!DNL Experience Manager Assets] as a [!DNL Cloud Service] - workflow migration](https://github.com/adobe/aem-cloud-migration)**.
