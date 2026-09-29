---
title: Cloud Manager Tests Overview
description: Get an overview of the three types of tests that Cloud Manager automatically runs to ensure the quality of your custom code.
exl-id: 5f5c97b1-4180-4f49-af8b-257d4744766e
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: a01bfd36-4ab8-4bf8-9dc0-5b45b890552e
    internal-label: APIs
subfeature_v2:
  - id: d9eb3b3e-9447-4ed4-bf4a-96c7b245cb27
    internal-label: Cloud Manager APIs
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---

# Cloud Manager Tests Overview {#overview}

There are three categories of tests supported by Cloud Manager for Cloud Services pipelines.

1. [Code Quality Testing](/help/implementing/cloud-manager/code-quality-testing.md)

   * Code quality testing evaluates the quality of your application code.
   * The code quality pipeline is executed immediately following the build step in all non-production and production pipelines.
   * The [custom code quality rules](/help/implementing/cloud-manager/custom-code-quality-rules.md) executed by Cloud Manager are created based on best practices from AEM Engineering.

1. [Functional Testing](/help/implementing/cloud-manager/functional-testing.md)

   * Functional testing runs during the stage testing phase of a [production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md). It can also run, optionally, during the testing phase of a [non-production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md).

1. [Experience Audit Testing](/help/implementing/cloud-manager/reports/report-experience-audit.md)

   * Experience audit testing is enabled in all Cloud Manager production pipelines and cannot be skipped.

These tests can be:

* Customer-written 
* Adobe-written
* Created with open source tools 

>[!NOTE]
>
> Both customer-written tests and Adobe-written tests are run in a containerized infrastructure designed for running such tests.
