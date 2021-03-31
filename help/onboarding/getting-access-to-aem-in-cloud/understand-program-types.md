---
title: Understanding Program and Program Types
description: Understanding Program and Program Types - Cloud Services
---

# Understanding Programs and Program Types {#understanding-programs} 

In Cloud Manager you have the Tenant entity at the very top which can have multiple Programs within it. Each Program can contain no more than one Production environment, and multiple non-production environments. 

The following diagram shows the hierarchy of entities in Cloud Manager.

   ![image](assets/program-types1.png)

## Source Code Repository {#source-code-repository}

Cloud Manager program will come auto-provisioned with it’s own git repository.

For a user to access the Cloud Manager git repository, users will need to use a Git client with a command-line tool, a standalone visual Git client, or the user's IDE such as Eclipse, IntelliJ, NetBeans.

Once a Git client is set up, you can manage your git repository from the Cloud Manager UI. To learn about how to manage Git using Cloud Manager UI, refer to [Accessing Git](/help/implementing/cloud-manager/accessing-git.md).

To begin developing the AEM Cloud application, a local copy of the application code must be made by checking it out from the Cloud Manager repository to a location on their local computer where they wish to create their repository.

```java
$ git clone {URL}
```

>[!NOTE]
>A user can check out a copy of their code, and make changes in the local code repository. When ready, the user can commit their code changes back to the remote code repository in Cloud Manager.

## Program Types {#program-types}

A user can create a **Sandbox** or a **Production** program. 

* A *Production Program* is created to enable live traffic at the appropriate time in the future.
   Refer to [Introduction to Production Programs](/help/onboarding/getting-access-to-aem-in-cloud/introduction-production-programs.md) for more details.


* A *Sandbox Program* is typically created to serve the purposes of training, running demo’s, enablement, POC’s, or documentation. It is not meant to carry live traffic and will have restrictions that a Production program will not. It will include Sites and Assets and will be delivered auto-populated with a Git branch that includes sample code, a Dev environment, and a non-production pipeline.
   Refer to [Introduction to Sandbox Programs](/help/onboarding/getting-access-to-aem-in-cloud/introduction-sandbox-programs.md) for more details.

