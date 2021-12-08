---
title: Post Go-Live
description: Learn how to monitor for issues and improve performance
---

# Post Go-Live {#post-go-live}

This is the last part of the journey so you will learn to how to monitor for issues and improve performance once the migration is complete. You should ensure the clean-up of temporary files, review best practices for continuous development and manage logs.

## The Story So Far {#story-so-far}

In the previous step of the journey, you learned how to perform the migration and [Go-live](/help/journey-migration/go-live.md) once the code and the content were ready to be moved over to AEM as a Cloud Service.

## Objective {#objective}

This document describes the tools that are available to troubleshoot AEM as a Cloud Service environments:

* **Developer Console**
* **CRX/DE Lite**
* **Managing Logs**

## Developer Console {#developer-console}

Debugging AEM as a Cloud Service developer environments are available in the Developer Console for development, stage, and production environments.

Refer to [Implementing for AEM as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/development-guidelines.html#aem-as-a-cloud-service-development-tools) to learn more about development tools.

## CRX/DE Lite {#crxde-lite}

As a user, you can access CRX/DE Lite on the development environment but not stage or production. 
  
>[!IMPORTANT]
>Writing to immutable repositories such as `/libs` and `/apps` at runtime will result in errors. Additionally, as a customer, you will not have access to developer tooling for staging and production environments.

Refer to [Developing with CRX/DE Lite](/help/implementing/developing/tools/crxde.md) to learn how to develop your AEM application using CRX/DE Lite.

## Managing Logs {#managing-logs}

Users can access a list of available log files for the selected environment.
  
Refer to [Accessing and Managing Logs](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/manage-logs.html) to learn how to access and manage logs through UI or from API via Cloud Manager.

## Contacting Support {#contacting-support}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_support"
>title="Help & Support"
>abstract="Reach out to our AEM Support team to get clarifications or to address any concerns."
>additional-url="https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html" text="Support for Experience Cloud"

If you have questions about access to Cloud Service, contact your Adobe representative or [Support for Experience Cloud](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) for more details.

## The Journey Ends - Or Does It? {#journey-ends}

Congratulations! You have completed the AEM as a Cloud Service Migration Journey! You should have an understanding of how to:

* Get started with moving to AEM as a Cloud Service
* Determine if your deployment is ready to be moved to AEM as a Cloud Service
* Make your code and content cloud ready
* Perform the migration
* Monitor for issues and improve performance

You are now ready to migrate to AEM as a Cloud Service! Check out some of the additional resources available in the Additional Resources section to learn more about the tools and features used in this journey.

## Additional Resources {#additional-resources}

**TBD**

<!--#>[!CONTEXTUALHELP]
>id="aemcloud_golive_troubleshooting"
>exl-id: f9b0b2fa-e29c-4faa-a5e7-e5edd04b25ca
>title="Troubleshooting AEM"
>abstract="Review best practices for continous development and manage logs along with tools like Developer console & CRXDE Lite to help with troubleshooting issues with AEM"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/manage-logs.html" text="Accessing and Managing Logs"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/development-guidelines.html#aem-as-a-cloud-service-development-tools" text="AEM as a Cloud Service Development tools"-->
