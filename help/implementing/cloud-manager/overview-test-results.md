---
title: Cloud Manager Tests Overview
description: Get an overview of the three types of tests that Cloud Manager automatically runs to ensure quality of your custom code.
exl-id: 5f5c97b1-4180-4f49-af8b-257d4744766e
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Cloud Manager Tests Overview {#overview}

There are three categories of tests supported by Cloud Manager for Cloud Services pipelines.

1. [Code Quality Testing](/help/implementing/cloud-manager/code-quality-testing.md)

   * Code quality testing evaluates the quality of your application code.
   * The code quality pipeline is executed immediately following the build step in all non-production and production pipelines.
   * The [custom code quality rules](/help/implementing/cloud-manager/custom-code-quality-rules.md) executed by Cloud Manager are created based on best practices from AEM Engineering.

1. [Functional Testing](/help/implementing/cloud-manager/functional-testing.md)

   * Functional testing is a part of the stage testing phase of a [production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md) and optionally part of testing phase of a [non-production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md).

1. [Experience Audit Testing](/help/implementing/cloud-manager/experience-audit-dashboard.md)

   * Experience audit testing is enabled in all Cloud Manager production pipelines andcannot be skipped.

These tests can be:

* Customer-written 
* Adobe-written
* Created with open source tools 

>[!NOTE]
>
> Both customer-written tests and Adobe-written tests are run in a containerized infrastructure designed for running such tests.
