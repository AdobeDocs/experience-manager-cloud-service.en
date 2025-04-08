---
title: Understand Reference Demo Add-on Installation
description: Learn about Cloud Manager and how it is used to install the add-on.
exl-id: 9418aac6-a8c4-43f7-b329-b02149fe2d53
feature: Onboarding
role: Admin, User, Developer
---
# Understand Reference Demo Add-on Installation {#understand-installation}

Learn about Cloud Manager and how it is used to install the add-on.

>[!TIP]
>
>If you are experienced with Cloud Manager or want to jump directly to configuration and usage of the add-on, skip to [Create a Program and a Pipeline](create-program.md)
>
>If you want to learn how Cloud Manager and AEM work together to create your demo environments, and how to set up and use your own, continue reading the current document.

## Objective {#objective}

This document helps you understand how the installation process of the Reference Demos Add-on works, illustrating how the different pieces work together. After reading, you should:

* Have a basic understanding of Cloud Manager.
* Understand how pipelines deliver content and configuration to AEM.
* See how templates can create sites prepopulated with demo content with just a few clicks.

This document focuses on understanding these fundamental pieces of the AEM Reference Demo Add-on before moving on to the next step of the journey where you begin installation.

Although it is recommended to proceed through this journey, if you are experienced with Cloud Manager, or want to jump directly to configuration and usage of the add-on, skip to [Create a Program and a Pipeline](create-program.md).

## Responsible Role {#responsible-role}

This journey applies to a system administrator who is a member of the **Business Owner** role in Cloud Manager for your organization.

## Requirements and Prerequisites {#requirements-prerequisites}

There are minimal requirements to learn about and begin using the Reference Demos Add-on.

### Knowledge {#knowledge}

* Basic knowledge of Cloud Manager

### Tools {#tools}

* Be a member of **Business Owner** role in Cloud Manager for your organization

## Understanding Cloud Manager {#cloud-manager}

Cloud Manager is an essential component of AEM as a Cloud Service and serves as the single entry point for the platform.

Cloud Manager is used to administer the cloud resources supporting your AEM Projects including the environments and tools needed. For the purposes of this journey, a complete understanding of Cloud Manager is not necessary. However, you must be familiar with some basic concepts.

>[!TIP]
>
>If you want to learn about Cloud Manager in depth, see [Additional Resources](#additional-resources) section of this article for links to more information.

### Programs {#programs}

When you sign into Cloud Manager, you have access to one or more **programs**. A program can be defined in many different ways, but it is easiest to think about it as associated with the sites and experiences associated with one brand identity.

If you sign into Cloud Manager representing **WKND Travel and Adventure Enterprises**, you might create a **WKND Nightlife** program and a **WKND Backyard Projects** program. Both of these programs would have AEM environments for managing their associated sites.

### Sandboxes {#sandboxes}

Programs can be either production programs or sandbox programs.

* **A production program** is created to eventually allow live traffic when your program is ready to go live.
* **A sandbox program** is created for training, running demos, enablement, POCs, and so on, and is not meant for live traffic.

To install the AEM Reference Demos Add-on, create a sandbox program.

>[!NOTE]
>
>The AEM Reference Demos Add-on is only available in sandbox programs.

## Installation and Usage Flow {#installation-flow}

Now that you understand some fundamental concepts of Cloud Manager, the installation of the AEM Reference Demos Add-on is conceptually simple.

1. Log into Cloud Manager.
1. Create a sandbox AEM program, activating the AEM Reference Demos Add on as an option for the program.
1. The demo content and configuration is deployed to the program. The demo content contains:
   * Site templates used to create various AEM sites using features of AEM, prepopulated with best practices examples.
   * Configuration tools to manage your demo content.
1. Log into AEM in your new sandbox program and use the quick site creation tool and create demo sites based on the templates.
1. Use the configuration tools to manage those demo sites and template including deleting them when no longer needed.

## AEM Site Templates {#site-templates}

AEM Site Templates are packages that contain predefined content and structure for a site. Site templates can be customized to meet the needs of specific projects so when AEM administrators create sites, they can choose from templates that apply to their business cases.

The AEM Reference Demos Add-on includes multiple templates for various testing and demonstration needs. Once you have created your program and deployed the pipeline to install the add-on, you can log into AEM and create sites based on many demo templates

## What's Next {#what-is-next}

Now that you have completed this part of the AEM Reference Demos Add-on journey you should:

* Have a basic understanding of Cloud Manager.
* Understand how pipelines deliver content and configuration to AEM.
* See how templates can create sites prepopulated with demo content with just a few clicks.

Build on this knowledge and continue your AEM Quick Site Creation journey by reviewing [Create a Program and a Pipeline](create-program.md), where you learn how to set up a new program and pipeline to deploy the add-on.

## Additional Resources {#additional-resources}

While it is recommended that you move to the next part of the Quick Site Creation journey by reviewing [Create a Program and a Pipeline](create-program.md), the following are some additional, optional resources. These resources take a deeper dive into concepts mentioned in this document. However, they are not required to continue the journey.

* [Understanding Programs and Program Types](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/programs/program-types.html) - Start here to understanding the differences between live and sandbox programs.
* [Site Templates](/help/sites-cloud/administering/site-creation/site-templates.md) - If you would like to know more about the structure of site templates and how they are used to create sites, refer to this document.
* [Cloud Manager documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/onboarding-concepts/cloud-manager-introduction.html) - If you would like more details on Cloud Manager's features, you may want to directly consult the in-depth technical docs.
