---
title: Unified Experience for Code Refactoring Tools
description: Unified Experience for Code Refactoring Tools
---

# Unified Experience for Code Refactoring Tools {#unified-experience}

We have developed tools to automate some of the code refactoring tasks required to be compatible with AEM as a Cloud Service. To reduce the complexity associated with installation and setup of different code refactoring tools, we have developed a plugin to unify tools that operate on code and repositories. 

## Benefits {#benefits}

The Unified Experience plugin provides the following benefits:

* Unifies tools that work on source code into one `node.js` application exposed as `aio-cli ` plugin to provide a consistent user experience to the user.

* Provides ability to execute all tools via a single command, while also providing the flexibility to execute specific tools as needed.

* Provides extensibility to simplify addition of new tools, while keeping the experience consistent.

## Understanding the Plugin {#understanding-plugin}

The `aio-cli-plugin-aem-cloud-service-migration` plugin consists of two main parts:

* **User Interface** 

  * `aio-cli` commands to execute one or more code refactoring tools (via chaining the tools to be executed sequentially).
  * `config.yaml` which takes in the required input parameters.

* **Underlying Code Refactoring Tool Suite**

   The code refactoring tools execute their functionalities by:

     * Scanning the respective section of customer's code and manipulating the code (based on code implementation for best practices) to produce the output which can then be validated and deployed.

     * Producing a summary report to record the operations performed during execution.

## Availability {#availability}

Refer to [Git Resource: aio-cli-plugin-aem-cloud-service-migration](https://github.com/adobe/aio-cli-plugin-aem-cloud-service-migration) to learn about the usage and how you can contribute to this plugin code that is open sourced in GitHub.

>[!NOTE]
>Currently the plugin is integrated with AEM Dispatcher Converter and Repository Modernizer.
