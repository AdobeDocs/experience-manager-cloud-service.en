---
title: Functional Testing
description: Learn about the three different types of functional testing built into the AEM as a Cloud Service deployment process to ensure quality and reliability of your code.
exl-id: 7eb50225-e638-4c05-a755-4647a00d8357
---

# Introduction {#functional-testing-introduction}

> [!CONTEXTUALHELP]
> id="aemcloud_nonbpa_functionaltesting"
> title="Functional Testing"
> abstract="Learn about the three different types of functional testing built into the AEM as a Cloud Service deployment process to ensure quality and reliability of your code."

Learn about the quality gates available in
the [AEM as a Cloud Service deployment process](/help/implementing/cloud-manager/deploy-code.md),
the different types of functional testing built in, how you can contribute and how you can make best use of them in
the context of an overall testing strategy.

## Overview

The following diagram gives an overview of the quality gates available in
the [AEM as a Cloud Service deployment process](/help/implementing/cloud-manager/deploy-code.md).

![AEM Cloud Service deployment quality gates](assets/functional-testing/quality-gates-overview.svg)

## Purpose

The AEM Cloud Service deployment pipelines run at different stages in your development and AEM product release
lifecycle and provide various quality gates at different levels with the goal to ensure robust and safe deployments for
your AEM application changes and AEM product changes likewise.

Adobe provides some quality gates out-of-the-box, while others need to be implemented and configured by you. The same
quality gate can run at different stages in the lifecycle, some can even be used in your own development setup and
CI/CD.

The out-of-the-box provided quality gates ensure the AEM product functionality works as expected in the context of your
AEM application. On the other hand, the custom quality gates you provide focus on validating that your application's
essential features and user interactions work as expected. The two types of quality gates together ensure robust and
safe automatic deployments for your code changes and AEM product changes.

The quality gates are not a general purpose testing framework intended to cover your complete testing strategy. The AEM
product undergoes extended testing before it reaches the AEM cloud service deployment process. Likewise, your
application is expected to have a good quality already before it reaches the deployment phase.

## Quality Gates

### Summary

|                           | Unit Tests            | Code Quality | Product Tests            | Custom<br/> Functional Tests        | Custom<br/> UI Tests                | Experience Audit             | Customer Validations | Manual Testing |
|---------------------------|-----------------------|--------------|--------------------------|-------------------------------------|-------------------------------------|------------------------------|----------------------|----------------|
| Production Pipeline       | Yes<br/>Blocking<br/> | Yes          | Yes<br/>Blocking<br/>    | Yes<br/>Blocking<br/>60m Timeout    | Yes<br/>Blocking<br/>60m Timeout    | Yes<br/>Non-Blocking<br/>    | No                   | No             |
| Non-Production Pipeline   | Yes<br/>Blocking<br/> | Yes          | Opt-In<br/>Blocking<br/> | Opt-In<br/>Blocking<br/>60m Timeout | Opt-In<br/>Blocking<br/>60m Timeout | Opt-In<br/>Non-Blocking<br/> | No                   | No             |
| Adobe Internal Validation | Yes<br/>Blocking<br/> | Yes          | Yes<br/>Blocking<br/>    | Yes<br/>Blocking<br/>60m Timeout    | Yes<br/>Blocking<br/>60m Timeout    | Yes<br/>Non-Blocking<br/>    | No                   | No             |
| Customer CI/CD            | Yes                   | No           | No                       | Yes                                 | Yes                                 | No                           | Yes                  | Yes            |
| Customer Local Developer  | Yes                   | No           | No                       | Yes                                 | Yes                                 | No                           | Yes                  | Yes            |

### Unit Test

You need to provide the unit tests for your AEM application, which are the foundation of every testing strategy. They
are intended to run fast and often and give early and fast feedback. They are tightly integrated into the developer
workflows, your own CI/CD and the AEM cloud service deployment pipelines.

They are implemented using JUnit and are executed with Maven. Please refer to the
[core module of the AEM Project Archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/core.html#unit-tests)
for an example unit test for AEM and getting started.

### Code Quality

This quality gate is configured out-of-the-box and runs static code analysis on your AEM application code.

See [Code Quality Testing](/help/implementing/cloud-manager/code-quality-testing.md) and
[Custom code quality rules](/help/implementing/cloud-manager/custom-code-quality-rules.md) for more information.

### Product Tests

Product functional tests are a set of stable HTTP integration tests (ITs) of core functionality in AEM such as authoring
and replication tasks. Adobe provides and maintains them out-of-the box. They are intended to prevent changes to custom
application code from being deployed if it breaks core functionality in the AEM product.

They are implemented using Junit, are executed using Maven and make use of the
official [AEM Testing Clients](https://github.com/adobe/aem-testing-clients).
The product test suite is maintained as
an [open-source project](https://github.com/adobe/aem-test-samples/tree/aem-cloud/smoke),
follows best-practices and can be considered a good starting point for the implementation of your tests.

### Custom Functional Tests

After the unit tests, this is the second customer-provided quality gate. Like the product tests, customer functional
tests are HTTP integration tests (ITs) and are as well implemented using Junit, are executed using Maven and
built on top of the official [AEM Testing Clients](https://github.com/adobe/aem-testing-clients).

> [!NOTE]
>
> Custom functional tests are executed in the production and non-production (opt-in) pipelines which are used by
> your AEM application changes deployments and AEM product push updates and are therefore a key contribution
> to help ensure proper functioning of your application and increase release safety. The customer functional
> tests are also executed in internal pre-release validation pipelines for each customer, which helps provide early
> feedback.

In order to keep pipeline executions efficient, we recommend to focus on key features and main user interaction flows.
An execution time of ~15 minutes or less for functional tests is recommended. Full functional test suites that do not
fit in
this quality gate are recommended to be executed as part of general customer validation pipelines during the customer's
development flow.

Please refer to the [open-sourced product tests](https://github.com/adobe/aem-test-samples/tree/aem-cloud/smoke) or the
[it.tests module of the AEM Projects Archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/ittests.html)
for examples.

See [Java Functional Tests](/help/implementing/cloud-manager/java-functional-testing.md) for more information.

### Custom UI Tests

Custom UI testing enables you to create and automatically run UI tests for your AEM applications. Custom UI tests
follow the same characteristics and purpose like the custom functional tests but are focused on UI interactions.

UI tests support different UI-testing frameworks (e.g. Cypress) and tests are packaged in a Docker image to allow for a
wide choice of language and frameworks.

> [!NOTE]
>
> Custom UI tests are executed in the production and non-production (opt-in) pipelines which are used by your AEM
> application changes deployments and AEM product push updates and are therefore a key contribution to help
> ensure proper functioning of your application and increase release safety.The customer UI tests are also executed
> in internal pre-release validation pipelines for each customer, which helps provide early feedback.

In order to keep pipeline executions efficient, we recommend to focus on key features and main user interaction flows.
Full UI test suites that do not fit in this quality gate are recommended to be executed as part of general customer
validation pipelines during customer's development flow.

Please refer to the [open-sourced example tests](https://github.com/adobe/aem-test-samples/tree/aem-cloud/) or the
[ui.tests module of the AEM Projects Archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/uitests.html)
for examples.

See [Custom UI Testing](/help/implementing/cloud-manager/ui-testing.md#custom-ui-testing) for more information.

### Experience Audit

The experience audit quality gate is
performing [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
audits against the customer's webpage.

This quality gate is provided by AEM out-of-the box, but is currently not blocking the deployment pipelines. By default,
an audit against the root page (`/`) of the publish instance is performed. You can contribute by configuring up to 25
custom paths that are considered for audits.

See [Experience Audit Testing](/help/implementing/cloud-manager/experience-audit-testing.md)
for more information.

### Customer Validations

The customer validations quality gate is a placeholder for the customer's own testing strategy and effort, executed
before the customer's application changes reach the AEM cloud deployment pipelines.

Here you can, of course, choose the tools and frameworks you prefer. In contrast to customer function tests
and custom UI tests, there are no AEM cloud service related limits, and we therefore recommend to perform long-running
functional and UI testing here.

While you are free to choose any tool and framework, we recommend you align HTTP based integration tests
and UI tests with the tools and frameworks available in the custom functional tests and custom UI test quality gates.
We recommend integrating
[Rapid Development Environments (RDE)](/help/implementing/developing/introduction/rapid-development-environments.md)
in your local testing strategy to test as close as possible to AEM cloud environments.

### Manual testing

The Manual testing quality gate is a placeholder for customers who do manual testing. AEM cloud pipelines do not support
manual testing and therefore this needs to happen as part of your own local testing strategy.

For manual testing, it can be useful to integrate with an additional AEM Cloud Service development environment. 
