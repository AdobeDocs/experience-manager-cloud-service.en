---
title: Functional Testing
description: Learn about the three different types of functional testing built into the AEM as a Cloud Service deployment process to ensure quality and reliability of your code.
exl-id: 7eb50225-e638-4c05-a755-4647a00d8357
---

# Introduction {#functional-testing-introduction}

> [!CONTEXTUALHELP]
> id="aemcloud_nonbpa_functionaltesting"
> title="Functional Testing"
> abstract="Learn about the three different types of functional testing built into the AEM as a Cloud Service deployment
> process to ensure quality and reliability of your code."

Learn about the quality gates available in
the [AEM as a Cloud Service deployment process](/help/implementing/cloud-manager/deploy-code.md),
the different types of functional testing built into, how you can contribute and how you can make best use of them in
the context of an overall testing strategy.

## Overview

The following diagram gives an overview of the quality gates available in
the [AEM as a Cloud Service deployment process](/help/implementing/cloud-manager/deploy-code.md).

![AEM Cloud Service deployment quality gates](assets/functional-testing/quality-gates-overview.svg)

## Purpose

The AEM Cloud Service deployment pipelines run at different stages in the customer development and AEM product release
lifecycle and provide various quality gates at different levels with the goal to ensure robust and safe deployments for
customer project and AEM product changes likewise.

Some quality gates are provided by Adobe out of the box, others need to be provided and configured by the customers.
The same quality gate can run at different stages in the lifecycle, some can even be used in the customers own
development setup and CI/CD.

The out of the box provided quality gates ensure proper functioning of the AEM product in the context of the customer
project. The customer provided quality gates focus on proper functioning of customer applications essential features and
the most important user interactions. Together they ensure robust and safe automatic deployments for customer changes
and AEM product changes.

The quality gates are not a general purpose testing framework intended to cover the complete testing strategy of the
customer. The AEM product undergoes extended testing before it reaches the AEM cloud service deployment process.
Likewise, the customer project is expected to have a good quality before it reaches the deployment process.

## Quality Gates

### Summary

|                           | Unit Tests                | Code Quality | Product Tests                | Custom<br/> Functional Tests              | Custom<br/> UI Tests                      | Experience Audit                 | Customer Validations | Manual Testing |
|---------------------------|---------------------------|--------------|------------------------------|-------------------------------------------|-------------------------------------------|----------------------------------|----------------------|----------------|
| Production Pipeline       | - Yes<br/>- Blocking<br/> | Yes          | - Yes<br/>- Blocking<br/>    | - Yes<br/>- Blocking<br/>- 60m Timeout    | - Yes<br/>- Blocking<br/>- 60m Timeout    | - Yes<br/>- Non-Blocking<br/>    | No                   | No             |
| Non-Production Pipeline   | - Yes<br/>- Blocking<br/> | Yes          | - Opt-In<br/>- Blocking<br/> | - Opt-In<br/>- Blocking<br/>- 60m Timeout | - Opt-In<br/>- Blocking<br/>- 60m Timeout | - Opt-In<br/>- Non-Blocking<br/> | No                   | No             |
| Adobe Internal Validation | - Yes<br/>- Blocking<br/> | Yes          | - Yes<br/>- Blocking<br/>    | - Yes<br/>- Blocking<br/>- 60m Timeout    | - Yes<br/>- Blocking<br/>- 60m Timeout    | - Yes<br/>- Non-Blocking<br/>    | No                   | No             |
| Customer CI/CD            | Yes                       | No           | No                           | Yes                                       | Yes                                       | No                               | Yes                  | Yes            |
| Customer Local Developer  | Yes                       | No           | No                           | Yes                                       | Yes                                       | No                               | Yes                  | Yes            |

### Unit Test

Unit tests are provided by the customer and build the foundation of every testing strategy. They are intended to run
fast and often and give early and fast feedback. They are tightly integrated into the developer workflows, customer
CI/CD and the AEM cloud service deployment pipelines.

They are implemented using Junit and are executed with Maven. Please refer to the
[core module of the AEM Project Archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/core.html?lang=en#unit-tests)
for an example unit test for AEM and getting started.

### Code Quality

This quality gate comes out of the box and runs code analysis against the customer's application code.

See [Code Quality Testing](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/test-results/code-quality-testing.html?lang=en)
and [Custom code quality rules](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/test-results/custom-code-quality-rules.html?lang=en)
for more information.

### Product Tests

Product functional tests are a set of stable HTTP integration tests (ITs) of core functionality in AEM such as authoring
and replication tasks. These tests are provided and maintained by Adobe out-of-the box and are intended to prevent
changes to custom application code from being deployed if it breaks core functionality.

They are implemented using Junit, are executed using Maven and make use of the
official [AEM Testing Clients](https://github.com/adobe/aem-testing-clients).
The product test suite is maintained as
an [open-source project](https://github.com/adobe/aem-test-samples/tree/aem-cloud/smoke),
follows best-practices and can be considered a good starting point for the implementation custom functional tests.

### Custom Functional Tests

After the unit tests, this is the second customer provided quality gate. Like the product tests, customer functional
tests are HTTP integration tests (ITs) and are as well implemented using Junit, are executed using Maven and as well
build on top of the official [AEM Testing Clients](https://github.com/adobe/aem-testing-clients).

> [!NOTE]
>
> Custom functional tests are executed in the production and non-production (opt-in) pipelines which are used by
> customer deployments and AEM product push updates likewise and are therefore a key contribution from the customer to
> help ensure proper functioning of the customer application and release safety. As well, the customer functional tests
> are executed in internal pre-release validation pipelines for each customer, which helps to provide early feedback.

In order to not delay pipeline executions, we recommend to focus on key features and main user interaction flows. Full
functional test suites that do not fit in this quality gate are recommended to be executed as part of general customer
validation pipelines during customer development flow.

Please refer to the [open-sourced product tests](https://github.com/adobe/aem-test-samples/tree/aem-cloud/smoke) or the
[it.tests module of the AEM Projects Archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/ittests.html?lang=en)
for examples.

See [Java Functional Tests](/help/implementing/cloud-manager/java-functional-testing.md) for more information.

### Custom UI Tests

Custom UI testing enables customers to create and automatically run UI tests for their AEM applications. Custom UI tests
follow the same characteristics and purpose like the custom functional tests.

UI tests are Selenium-based tests packaged in a Docker image to allow for a wide choice of language and frameworks such
as Java and Maven, Node and WebDriver.io, or any other framework and technology built upon Selenium.

> [!NOTE]
>
> Custom UI tests are executed in the production and non-production (opt-in) pipelines which are used by customer
> deployments and AEM product push updates likewise and are therefore a key contribution from the customer to help
> ensure proper functioning of the customer project and release safety. As well, the customer UI tests are executed
> in internal pre-release validation pipelines for each customer, which helps to provide early feedback.

In order to not delay pipeline executions, we recommend to focus on key features and main user interaction flows.
Full UI test suites that do not fit in this quality gate are recommended to be executed as part of general customer
validation pipelines during customer development flow.

Please refer to the [open-sourced example tests](https://github.com/adobe/aem-test-samples/tree/aem-cloud/) or the
[ui.tests module of the AEM Projects Archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/uitests.html?lang=en)
for examples.

See [Custom UI Testing](/help/implementing/cloud-manager/ui-testing.md#custom-ui-testing) for more information.

### Experience Audit

The experience audit quality gate is
performing [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
audits against the customer application.

This quality gate is provided by AEM out-of-the box, but is not blocking the deployment pipelines. By default, an audit
against the root page `/` of the publish instance is performed. Customers can contribute by configuring up to 25 custom
paths that are considered for audits.

See [Experience Audit Testing](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/test-results/experience-audit-testing.html?lang=en)
for more information.

### Customer Validations

The customer validations quality gate is a placeholder for the customers own testing strategy and effort, happening
before the customer's application changes reach the AEM cloud pipelines.

Here, customers can of course choose the tools and frameworks of their choice. In contrast to customer function tests
and custom UI tests, there are no AEM cloud service related limits, and we therefore recommend to perform most of the
functional and UI testing here.

While the customers are free to choose whatever tools and frameworks, we recommend to align HTTP based integration tests
and UI tests with the tools and frameworks available in the custom functional tests and custom UI test quality gates.
We recommend integrating
[RDE environments](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/rapid-development-environments.html?lang=en)
in customer's local testing strategy to test as close as possible to AEM cloud environments.

### Manual testing

The Manual testing quality gate is a placeholder for customers who do manual testing. AEM cloud pipelines do not support
manual testing and therefore this needs to happen as part of the customer's local testing strategy.
