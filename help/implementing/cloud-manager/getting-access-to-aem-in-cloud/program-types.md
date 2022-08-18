---
title: Programs and Program Types
description: Learn about the hierarchy of Cloud Manager and how the different types of programs fit into its structure and how they differ.
exl-id: 507df619-a5b5-419a-9e38-db77541425a2
---

# Programs and Program Types {#understanding-programs} 

Cloud Manager is built around a hierarchy of entities. The details of this is not critical to your everyday work in Cloud Manager, but an overview of it will help you as you understand programs and set up your very own.

![Cloud Manager hierarchy](assets/program-types1.png)

* **TENANT** - This is the top of the hierarchy. Every customer is provisioned with a tenant.
* **PROGRAMS** - Each tenant has one or more programs, [which often reflect the customer's licensed solutions.](introduction-production-programs.md)
* **ENVIRONMENTS** - Each program has multiple environments such as production for live content, one for staging, and one for development purposes.
  * Each program can have only one production environment, but multiple non-production environments.
* **REPOSITORY** - Programs have git repositories where application and front-end code is maintained for the environments.
* **TOOLS &amp; WORKFLOWS** - Pipelines manage the deployment of code from the repositories to the environments while other tools allow for access to logs, monitoring, and environment management.

An example is often helpful in contextualizing this hierarchy.

* WKND Travel and Adventure Enterprises might be a **tenant** that focuses on travel-related media.
* The WKND Travel and Adventure Enterprises tenant might have two **programs**: one Sites program for WKND Magazine and one Assets program for WKND Media.
* The WKND Magazine and WKND Media programs would both have dev, stage, and production **environments**.

## Source Code Repository {#source-code-repository}

A Cloud Manager program will come auto-provisioned with its own git repository.

To access the Cloud Manager git repository, users will need to use a git client with a command-line tool, a standalone visual git client, or the user's IDE of choice such as Eclipse, IntelliJ, or NetBeans.

Once a git client is set up, you can manage your git repository from the Cloud Manager UI. To learn about how to manage git using Cloud Manager UI, please refer to the document [Accessing Git.](/help/implementing/cloud-manager/managing-code/accessing-repos.md)

To begin developing the AEM Cloud application, a local copy of the application code must be made by checking it out from the Cloud Manager repository to a location on your local computer.

```java
$ git clone {URL}
```

The workflow is thus a standard git workflow.

1. A user clones a local copy of the git repository.
1. The user makes changes in the local code repository.
1. When ready, the user commits the changes back to the remote git repository.

The only difference is that the remote git repository is part of Cloud Manager, which is transparent to the developer.

## Program Types {#program-types}

A user can create a a **production** program or a **sandbox** program.

* A **production program** is created to enable live traffic for your site.
  * Please refer to the document [Introduction to Production Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/introduction-production-programs.md) for more details.
* A **sandbox program** is typically created to serve the purposes of training, running demos, enablement, POCs, or documentation.
  * A sandbox environment is not meant to carry live traffic and will have restrictions that a production program will not.
  * It will include Sites and Assets and will be delivered auto-populated with a git branch that includes sample code, a development environment, and a non-production pipeline.
  * Please refer to the document [Introduction to Sandbox Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/introduction-sandbox-programs.md) for more details.
