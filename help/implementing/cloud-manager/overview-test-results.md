---
title: Overview to Test Results - Cloud Services
description: Overview to Test Results - Cloud Services
exl-id: 5f5c97b1-4180-4f49-af8b-257d4744766e
---
# Overview {#overview}

There are three broad categories of tests supported by Cloud Manager for Cloud Services Pipeline:

1. [Code Quality Testing](/help/implementing/cloud-manager/code-quality-testing.md)

   The Code Quality Testing evaluates the quality of your application code. The Code-Quality pipeline is executed immediately following the build step in all non-production and production pipelines.

   The [Custom Code Quality Rules](/help/implementing/cloud-manager/custom-code-quality-rules.md) executed by Cloud Manager are created based on best practices from AEM Engineering.

1. [Functional Testing](/help/implementing/cloud-manager/functional-testing.md)

   The Functional Testing is a part of  the Stage testing phase of a Production Pipeline.

1. [Experience Audit Testing](/help/implementing/cloud-manager/experience-audit-testing.md)

   The Experience Audit Testing is enabled in all Cloud Manager Production Pipelines and cannot be skipped.

These tests can be:

* Customer-written 
* Adobe-written
* Open source tool 

    >[!NOTE]
    > Both Customer-written tests and Adobe-written tests are run in a containerized infrastructure designed for running these types of tests.
