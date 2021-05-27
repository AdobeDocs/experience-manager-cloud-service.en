---
title: Post Go-live Phase
description: Post Go-live Phase
exl-id: f9b0b2fa-e29c-4faa-a5e7-e5edd04b25ca
---
# Post Go-live {#post-go-live}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_troubleshooting"
>title="Troubleshooting AEM"
>abstract="Review best practices for continous development and manage logs along with tools like Developer console & CRXDE Lite to help with troubleshooting issues with AEM"
>additional-url="https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/using-cloud-manager/manage-logs.html" text="Accessing and Managing Logs"
>additional-url="https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/developing/development-guidelines.html#aem-as-a-cloud-service-development-tools" text="AEM as a Cloud Service Development tools"


In the Post Go-live phase, you should ensure clean-up of temporary files, review best practices for continuous development and manage logs.

The following tools are available to troubleshoot AEM as a Cloud Service environments:

* **Developer Console**
* **CRX/DE Lite**
* **Managing Logs**


## Developer Console {#developer-console}

Debugging AEM as a Cloud Service developer environments are available in the Developer Console for development, stage, and production environments.

Refer to [Implementing for AEM as a Cloud Service](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/developing/development-guidelines.html#aem-as-a-cloud-service-development-tools) to learn more about development tools.

## CRX/DE Lite {#crxde-lite}

As a user, you can access CRX/DE Lite on the development environment but not stage or production. 
  
>[!IMPORTANT]
>Writing to immutable repositories such as `/libs` and `/apps` at runtime will result in errors. Additionally, as a customer, you will not have access to developer tooling for staging and production environments.

Refer to [Developing with CRX/DE Lite](/help/implementing/developing/tools/crxde.md) to learn how to develop your AEM application using CRX/DE Lite.

## Managing Logs {#managing-logs}

Users can access a list of available log files for the selected environment.
  
Refer to [Accessing and Managing Logs](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/using-cloud-manager/manage-logs.html) to learn how to access and manage logs through UI or from API via Cloud Manager.

### Additional Support {#additional-support}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_support"
>title="Help & Support"
>abstract="Reach out to our AEM Support team to get clarifications or to address any concerns."
>additional-url="https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html" text="Support for Experience Cloud"

If you have questions about access to Cloud Service, contact your Adobe representative or [Support for Experience Cloud](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) for more details.
