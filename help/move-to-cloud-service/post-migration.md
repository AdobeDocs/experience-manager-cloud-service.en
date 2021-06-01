---
title: Post Migration Phase
description: Post Migration Phase
---

# Post-migration {#post-migration}

In the Post-migration phase, you should ensure clean-up of temporary files, review best practices for continuous development and manage logs.

The following tools are available to troubleshoot AEM as a Cloud Service environments:

* **Developer Console**
* **CRXDE Lite**
* **Managing Logs**


## Developer Console {#developer-console}

Debugging AEM as a Cloud Service developer environments are available in the Developer Console for development, stage, and production environments.

Refer to [Implementing for AEM as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/development-guidelines.html#aem-as-a-cloud-service-development-tools) to learn more about development tools.

## CRXDE Lite {#crxde-lite}

As a user, you can access **CRXDE Lite** on the development environment but not stage or production. 
  
>[!IMPORTANT]
>Writing to immutable repositories such as `/libs` and `/apps` at runtime will result in errors. Additionally, as a customer, you will not have access to developer tooling for staging and production environments.

Refer to [Developing with CRXDE Lite](/help/implementing/developing/tools/crxde.md) to learn how to develop your AEM application using CRXDE Lite.

## Managing Logs {#managing-logs}

Users can access a list of available log files for the selected environment.
  
Refer to [Accessing and Managing Logs](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/manage-logs.html) to learn how to access and manage logs through UI or from API via Cloud Manager.

### Additional Support {#additional-support}

If you have questions about access to Cloud Service, contact your Adobe representative or Adobe AEM CQ Support Portal.
