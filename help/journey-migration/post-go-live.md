---
title: Post Go-Live
description: Learn how to monitor for issues and improve performance.
exl-id: 487f0b51-501b-48fc-a796-3cb8a6d64462
feature: Migration
role: Admin
---
# Post Go-Live {#post-go-live}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_troubleshooting"
>title="Troubleshooting AEM"
>abstract="Review best practices for continuous development and management of logs. Learn about tools like Developer Console and CRXDE Lite to help with troubleshooting issues with AEM."
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-logs" text="Accessing and Managing Logs"
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines#aem-as-a-cloud-service-development-tools" text="AEM as a Cloud Service Development tools"

This journey is the last part, so you learn how to monitor for issues and improve performance after the migration is complete. Ensure the clean-up of temporary files, review best practices for continuous development, and manage logs.

## The Story So Far {#story-so-far}

In the previous step of the journey, you learned how to perform the migration and [Go-live](/help/journey-migration/go-live.md) once the code and the content were ready to be moved over to AEM as a Cloud Service.

## Objective {#objective}

This document describes the tools that are available to troubleshoot AEM as a Cloud Service environments:

* **Developer Console**
* **CRXDE Lite**
* **Managing Logs**

## Developer Console {#developer-console}

Debugging AEM as a Cloud Service developer environments is available in the Developer Console for development, stage, and production environments.

See [Implementing for AEM as a Cloud Service](/help/implementing/developing/introduction/development-guidelines.md#aem-as-a-cloud-service-development-tools) to learn more about development tools.

## CRXDE Lite {#crxde-lite}

As a user, you can access CRXDE Lite in the development environment but not stage or production. 
  
>[!IMPORTANT]
>Writing to immutable repositories, such as `/libs` and `/apps` at runtime, results in errors. Also, you do not have access to developer tooling for staging and production environments.

See [Developing with CRXDE Lite](/help/implementing/developing/tools/crxde.md) for more information about how to develop your AEM application using CRXDE Lite.

## Managing Logs {#managing-logs}

Users can access a list of available log files for the selected environment.
  
See [Accessing and Managing Logs](/help/implementing/cloud-manager/manage-logs.md) to learn how to access and manage logs through the user interface or from the API by way of the Cloud Manager.

## Contacting Support {#contacting-support}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_support"
>title="Help & Support"
>abstract="Contact Adobe's AEM Support team to get clarifications or to address any concerns."
>additional-url="https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html" text="Support for Experience Cloud"

If you have questions about access to Cloud Service, contact your Adobe representative or [Support for Experience Cloud](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) for more details.

## Document learnings {#document-learnings}

Once the migration is complete, document the knowledge gained during this process. Some questions that might help the documentation process are:

* What worked well and what did not?
* What were the major pain points?
* Recommendations if there is a future migration.

Share these post-migration learnings with stakeholders and teams inside your organization.

## The Journey Ends - Or Does It? {#journey-ends}

Congratulations! You have completed the AEM as a Cloud Service Migration Journey! You should have an understanding of how to:

* Get started with moving to AEM as a Cloud Service
* Determine if your deployment is ready to be moved to AEM as a Cloud Service
* Make your code and content cloud ready
* Perform the migration
* Monitor for issues and improve performance
