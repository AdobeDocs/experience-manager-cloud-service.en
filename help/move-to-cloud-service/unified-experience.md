---
title: Unified Experience for Code Refactoring Tools
description: Unified Experience for Code Refactoring Tools
---

# Unified Experience for Code Refactoring Tools {#unified-experience}

Multiple tools with different interaction points for customers creates a disjointed experience and increases the complexity of using tools, with each having different execution requirements in terms of installation, setup and execution.

## Benefits {#benefits}

The Unified Experience for Code Refactoring Tools invokes and executes all code refactoring tools that work on the source code from the same place.

The Unified Experience for Code Refactoring Tools along with the companion repositories allows to:

* Unify all the tools that work on source code migration into one `node.js` application exposed as `aio-cli plugin` to provide a consistent user experience to the user.

* Provision to perform the overall migration via a single command, while also providing flexibility to execute one particular tool as per requirement.

* Simplify future addition of new tools such as adding new tool to the plugin should simply require addition of a new command for developer, and a simple plugin update for user, so the experience remains consistent with more value addition.

### Understanding the Application Design

This tools unifies all the code refactoring tools into one node.js application exposed as `aio-cli plugin` to provide a consistent user experience to the user.

The plugin consists of two main parts:

* **User Interface** 

   `aio-cli` commands to execute one or more migration tools (via chaining the tools to be executed sequentially)`config.yaml` which takes in the required input parameters

* **Underlying Migration Tool Suite**

   The migration tools execute their functionalities by:

     * Scanning the respective section of customer's code and perform the migration (based on code implementation for best practices) to produce the output which can then be validated and deployed.

     * Recording the operations performed while migration, in a consistent order to produce a summary report.

## Using the Plugin {#using-plugin}

The `aio-cli-plugin-aem-cloud-service-migration` refactors customers code, repository structure or configurations on customer's local machine. This page captures the detailed requirements and design decisions for the unified experience.
It is available as an open source for community to extend for custom use cases.

## Availability {#availability}

You can install and use the `aio-cli-plugin-aem-cloud-service-migration` via `aio-cli` (currently only integrated with dispatcher converter).

Refer to [Git Resource: aio-cli-plugin-aem-cloud-service-migration](https://github.com/adobe/aio-cli-plugin-aem-cloud-service-migration) to learn about the usage and how you can contribute for this tool.

The plugin code has been open sourced in Github.

