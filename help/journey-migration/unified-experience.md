---
title: Unified Experience for Code Refactoring Tools
description: Learn about Unified Experience for Code Refactoring Tools.
exl-id: daee0e2d-1e2b-41a3-acab-fc59142d0e05
feature: Migration
role: Admin
---
# Unified Experience for Code Refactoring Tools {#unified-experience}

Adobe has developed tools to automate some of the code refactoring tasks required to be compatible with Adobe Experience Manager (AEM) as a Cloud Service. To reduce the complexity associated with the installation and setup of different code refactoring tools, Adobe has developed a plug-in to unify tools that operate on code and repositories.

## Benefits {#benefits}

The Unified Experience plugin provides the following benefits:

* Unifies tools that work on source code into one `node.js` application exposed as `aio-cli ` plugin to provide a consistent user experience to the user.

* Runs all tools by way of a single command, while also providing the flexibility to run specific tools as needed.

* Simplifies the addition of new tools, while keeping the experience consistent.

## Understanding the Plugin {#understanding-plugin}

The `aio-cli-plugin-aem-cloud-service-migration` plugin consists of two main parts:

* **User Interface** 

  * `aio-cli` commands to execute one or more code refactoring tools (by way of chaining the tools to be run sequentially).
  * `config.yaml` which takes in the required input parameters.

* **Underlying Code Refactoring Tool Suite**

   The code refactoring tools execute their functionalities by:

     * Scanning the respective section of the customer's code and manipulating the code (based on code implementation for best practices) to produce the output which can then be validated and deployed.

     * Producing a summary report to record the operations performed during execution.

## Availability {#availability}

See [Git Resource: aio-cli-plugin-aem-cloud-service-migration](https://github.com/adobe/aio-cli-plugin-aem-cloud-service-migration) where you can learn about usage and how you can contribute to this plug-in code that is open-sourced in GitHub.

>[!NOTE]
>Currently the plugin is integrated with AEM Dispatcher Converter and Repository Modernizer.
