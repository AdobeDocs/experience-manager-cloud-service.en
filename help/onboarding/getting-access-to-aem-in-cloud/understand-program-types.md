---
title: Understanding Program and Program Types
description: Understanding Program and Program Types - Cloud Services
---

# Understanding Programs and Program Types {#understanding-programs} 

In Cloud Manager you have the Tenant entity at the very top which can have multiple Programs within it. Each Program can contain no more than one Production environment, and multiple non-production environments. 

The following diagram shows the hierarchy of entities in Cloud Manager.

   ![image](assets/program-types1.png)

## Program Types {#program-types}

A user can create a **Sandbox** or a **Regular** program. 

* A *Production Program* is created to enable live traffic at the appropriate time in the future.
   Refer to [Introduction to Production Programs](getting-access-to-aem-in-cloud/introduction-production-programs.md) for more details.


* A *Sandbox Program* is typically created to serve the purposes of training, running demo’s, enablement, POC’s, or documentation. It is not meant to carry live traffic and will have restrictions that a regular program will not. It will include Sites and Assets and will be delivered auto-populated with a Git branch that includes sample code, a Dev environment, and a non-production pipeline.
   Refer to [Introduction to Sandbox Programs](getting-access-to-aem-in-cloud/introduction-production-programs.md) for more details.

