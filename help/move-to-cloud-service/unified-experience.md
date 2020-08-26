---
title: Unified Experience for Code Refactoring Tools
description: Unified Experience for Code Refactoring Tools
---

# Unified Experience for Code Refactoring Tools {#unified-experience}

The Unified Experience for Code Refactoring tools unifies the experience for execution of AEM as a Cloud Service code refactoring tools which operate on dispatcher files, code, and repositories.

This tool reduces the complexity of using code refactoring tools, with each having different execution requirements in terms of installation, setup and execution.

![image](/help/move-to-cloud-service/assets/unified-1.png)

## Benefits {#benefits}

The Unified Experience for Code Refactoring tools invoke and execute all code refactoring tools that work on the source code from the same place.

These tools along with the companion repositories allows:

* Unifying all the tools that work on source code migration into one `node.js` application exposed as `aio-cli plugin` to provide a consistent user experience to the user.

* Provisioning to perform the overall migration via a single command, while also providing flexibility to execute one particular tool as per requirement.

* Simplifying future addition of new tools such as adding new tool to the plugin should simply require addition of a new command for developer, and a simple plugin update for user, so the experience remains consistent with more value addition.

## Understanding the Plugin {#understanding-plugin}

The `aio-cli-plugin-aem-cloud-service-migration` refactors customers code, repository structure or configurations on customer's local machine. This page captures the detailed requirements and design decisions for the unified experience.
It is available as an open source for community to extend for custom use cases.

This tools unifies all the code refactoring tools into one node.js application exposed as `aio-cli plugin` to provide a consistent user experience to the user. The plugin scans customer's local code base and produces AEM as a Cloud Service compatible code, configurations and packages which can then be deployed to Cloud Service environments.

The plugin consists of two main parts:

* **User Interface** 

   `aio-cli` commands to execute one or more migration tools (via chaining the tools to be executed sequentially)`config.yaml` which takes in the required input parameters

* **Underlying Migration Tool Suite**

   The migration tools execute their functionalities by:

     * Scanning the respective section of customer's code and perform the migration (based on code implementation for best practices) to produce the output which can then be validated and deployed.

     * Recording the operations performed while migration, in a consistent order to produce a summary report.

## Availability {#availability}

You can install and use the `aio-cli-plugin-aem-cloud-service-migration` via `aio-cli`.

>[!NOTE]
>Currently this tool is only integrated with the Dispatcher Converter.

Refer to [Git Resource: aio-cli-plugin-aem-cloud-service-migration](https://github.com/adobe/aio-cli-plugin-aem-cloud-service-migration) to learn about the usage and how you can contribute for this plugin code that is open sourced in GitHub.

