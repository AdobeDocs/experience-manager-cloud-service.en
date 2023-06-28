---
title: Functional Testing
description: Learn about the three different types of functional testing built into the AEM as a Cloud Service deployment process to ensure quality and reliability of your code.
exl-id: 7eb50225-e638-4c05-a755-4647a00d8357
---

# Functional Testing {#functional-testing}

>[!CONTEXTUALHELP]
>id="aemcloud_nonbpa_functionaltesting"
>title="Functional Testing"
>abstract="Learn about the three different types of functional testing built into the AEM as a Cloud Service deployment process to ensure quality and reliability of your code."

Learn about the three different types of functional testing built into the [AEM as a Cloud Service deployment process](/help/implementing/cloud-manager/deploy-code.md) to ensure quality and reliability of your code.

## Scope

The purpose of the functional testing steps in the Cloud Manager pipeline is to ensure that the essential functionality of your application is working as expected.

This testing phase is the last level of automated testing before deploying your code to production.

Functional testing should not replace, but rather complement and extend other testing strategies such as unit testing,
integration testing, or functional testing performed outside the pipeline execution in Cloud Manager.

## Overview {#overview}

There are three different types of functional testing in AEM as a Cloud Service.

* [Product Functional Testing](#product-functional-testing)
* [Custom Functional Testing](#custom-functional-testing)
* [Custom UI Testing](#custom-ui-testing)

For all functional tests, the detailed results of the tests can be downloaded as a `.zip` file by using the **Download build log** button in the build overview screen as part of the [deployment process.](/help/implementing/cloud-manager/deploy-code.md)

These logs do not include the logs of the actual AEM runtime process. To access those logs, please refer to the document [Accessing and Managing Logs](/help/implementing/cloud-manager/manage-logs.md) for more details.

Both the product functional tests and sample custom functional tests are based on the [AEM Testing Clients.](https://github.com/adobe/aem-testing-clients)

### Product Functional Testing {#product-functional-testing}

Product functional tests are a set of stable HTTP integration tests (ITs) of core functionality in AEM such as authoring and replication tasks. These tests are maintained by Adobe and are intended to prevent  changes to custom application code from being deployed if it breaks core functionality.

* [Production Pipelines](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md): Product functional tests run automatically whenever you deploy new code to Cloud Manager and cannot be skipped.
* [Non-Production Pipelines](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md): Product functional tests can be optionally selected to run whenever you execute your non-production pipeline.

Product functional tests are maintained as an open-source project. See [product functional tests](https://github.com/adobe/aem-test-samples/tree/aem-cloud/smoke) in GitHub for details.

### Custom Functional Testing {#custom-functional-testing}

While product functional testing is defined by Adobe, you can write your own quality testing for your own application. This is run as custom functional testing as part of the [production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md) or optionally [non-production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md) to ensure the quality of your application.

Custom functional testing is executed both for custom code deployments as well as push upgrades, which makes it especially important to write good functional tests which prevent AEM code changes from breaking your application code. The custom functional testing step is always present and cannot be skipped.

See [Java Functional Tests](/help/implementing/cloud-manager/java-functional-testing.md) for more information.


### Custom UI Testing {#custom-ui-testing}

Custom UI testing is an optional feature that enables you to create and automatically run UI tests for your applications. UI tests are Selenium-based tests packaged in a Docker image to allow for a wide choice of language and frameworks such as Java and Maven, Node and WebDriver.io, or any other framework and technology built upon Selenium.

See [Custom UI Testing](/help/implementing/cloud-manager/ui-testing.md#custom-ui-testing) for more information.

