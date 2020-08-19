---
title: Overview to Test Results - Cloud Services
description: Overview to Test Results - Cloud Services
---

# Overview {#overview}

Cloud Manager for Cloud Services pipeline executions will support execution of tests that run against the stage environment. This is in contrast to tests run during the Build and Unit Testing step which are run offline, without access to any running AEM environment.

There are three broad categories of tests supported by Cloud Manager for Cloud Services Pipeline:

1. [Code Quality Testing](/help/implementing/cloud-manager/code-quality-testing.md)
1. [Functional Testing](/help/implementing/cloud-manager/functional-testing.md)
1. [Content Audit Testing](/help/implementing/cloud-manager/content-audit-testing.md)

These tests can be:

* Customer-written 
* Adobe-written
* Open source tool (powered by Lighthouse from Google) 

    >[!NOTE]
    > Both Customer-written tests and Adobe-written tests are run in a containerized infrastructure designed for running these types of tests.

