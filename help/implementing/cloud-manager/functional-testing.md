---
title: Functional Testing
description: Learn about the three different types of functional testing built into the AEM as a Cloud Service deployment process to ensure quality and reliability of your code.
exl-id: 7eb50225-e638-4c05-a755-4647a00d8357
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Introduction {#functional-testing-introduction}

>[!CONTEXTUALHELP]
>id="aemcloud_nonbpa_functionaltesting"
>title="Functional Testing"
>abstract="Learn about the three different types of functional testing built into the AEM as a Cloud Service deployment process to ensure quality and reliability of your code."

Learn about the quality gates available in the [AEM as a Cloud Service deployment process](/help/implementing/cloud-manager/deploy-code.md), the different types of functional testing built in, how you can contribute and how you can make best use of them in the context of an overall testing strategy.

## Overview

The following diagram provides a high-level overview of the available pipelines in the context of an overall testing strategy and the [AEM as a Cloud Service deployment process](/help/implementing/cloud-manager/deploy-code.md).

![AEM Cloud Service deployment quality gates](assets/functional-testing/quality-gates-compact.svg)

## Purpose

The purpose of the AEM Cloud Service deployment pipelines is to facilitate robust and secure deployments at various stages of your development and AEM product release lifecycle. These pipelines incorporate multiple quality gates at different levels to ensure the integrity and safety of deployments for both your AEM application changes and AEM product updates.

Adobe provides several built-in quality gates, while others require your intervention for implementation and configuration. These quality gates are versatile, with some being applicable at various stages of the lifecycle and even integrable into your own development setup and CI/CD processes.

The built-in quality gates primarily validate the functionality of the AEM product within the context of your AEM application. In contrast, the custom quality gates you set up are designed to verify that your application's critical features and user interactions perform as intended. Collectively, these two sets of quality gates work together to ensure robust and secure automated deployments for both your code modifications and AEM product updates.

It is important to note that these quality gates are not intended to be a comprehensive testing framework for your entire testing strategy. The AEM product is subjected to extensive testing before entering the AEM cloud service deployment process. Similarly, your application should already be of high quality before it reaches the deployment phase. This approach ensures that the quality gates focus on their primary objective of safeguarding the deployment process, rather than being a substitute for a full testing regimen.

## Quality Gates

The following diagram provides a detailed view of available quality gates and their use in the overall testing strategy and the [AEM as a Cloud Service deployment process](/help/implementing/cloud-manager/deploy-code.md).

![AEM Cloud Service deployment quality gates](assets/functional-testing/quality-gates-overview.svg)

### Summary Customer Provided Quality Gates

|                               |      Unit Tests       |    Custom<br/> Functional Tests     |        Custom<br/> UI Tests         | Customer<br/> Validations | Manual<br/> Testing |
|:------------------------------|:---------------------:|:-----------------------------------:|:-----------------------------------:|:-------------------------:|:-------------------:|
| **Production Pipeline**       | Yes<br/>Blocking<br/> |  Yes<br/>Blocking<br/>60m Timeout   |  Yes<br/>Blocking<br/>30m Timeout   |            No             |         No          |
| **Non-Production Pipeline**   | Yes<br/>Blocking<br/> | Opt-In<br/>Blocking<br/>60m Timeout | Opt-In<br/>Blocking<br/>30m Timeout |            No             |         No          |
| **Adobe Internal Validation** | Yes<br/>Blocking<br/> |  Yes<br/>Blocking<br/>60m Timeout   |  Yes<br/>Blocking<br/>30m Timeout   |            No             |         No          |
| **Customer CI/CD**            |          Yes          |                 Yes                 |                 Yes                 |            Yes            |         Yes         |
| **Customer Local Developer**  |          Yes          |                 Yes                 |                 Yes                 |            Yes            |         Yes         |

### Unit Test

You are encouraged to provide the unit tests for your AEM application, which are the foundation of every testing strategy. They are intended to run fast and often and give early and fast feedback. They are tightly integrated into the developer workflows, your own CI/CD and the AEM cloud service deployment pipelines.

They are implemented using JUnit and are executed with Maven. See [core module of the AEM Project Archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/core.html#unit-tests) for an example unit test for AEM and getting started.

### Code quality

This quality gate is configured out-of-the-box and runs static code analysis on your AEM application code.

See [Code Quality Testing](/help/implementing/cloud-manager/code-quality-testing.md) and [Custom code quality rules](/help/implementing/cloud-manager/custom-code-quality-rules.md) for more information.

### Product tests

Product functional tests are a set of stable HTTP integration tests (ITs) of core functionality in AEM such as authoring and replication tasks. Adobe provides and maintains them out-of-the-box. They are intended to prevent changes to custom application code from being deployed if it breaks core functionality in the AEM product.

They are implemented using Junit, are run using Maven and use the official [AEM Testing Clients](https://github.com/adobe/aem-testing-clients). The product test suite is maintained as
an [open-source project](https://github.com/adobe/aem-test-samples/tree/aem-cloud/smoke), follows best-practices and can be considered a good starting point for the implementation of your tests.

### Custom functional tests

Like the product tests, customer functional tests are HTTP integration tests (ITs) and are as well implemented using Junit, are executed using Maven and built on top of the official [AEM Testing Clients](https://github.com/adobe/aem-testing-clients).

>[!NOTE]
>
>Custom functional tests are run in the production and non-production (opt-in) pipelines which are used by your AEM application changes deployments and AEM product push updates and are therefore a key contribution to help ensure proper functioning of your application and increase release safety. The customer functional tests are also executed in internal pre-release validation pipelines for each customer, which helps provide early feedback.

To keep pipeline runs efficient, we recommend focusing on key features and main user interaction flows. A run time of ~15 minutes or less for functional tests is recommended. Full functional test suites that do not fit in this quality gate are recommended to be ran as part of general customer validation pipelines during the customer's development flow.

See [open-sourced product tests](https://github.com/adobe/aem-test-samples/tree/aem-cloud/smoke) or the [it.tests module of the AEM Projects Archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/ittests.html) for examples.

See [Java Functional Tests](/help/implementing/cloud-manager/java-functional-testing.md) for more information.

### Custom UI tests

To maximize risk control for your customer-specific development, Adobe strongly encourages you to capture critical UI tests into AEMCS. They are intended to be kept rather limited in number, but with the highest impact on your customer experience.

The tests are packaged in a Docker image - designed to be as volatile as possible (with support for Cypress, Selenium, Java, and Javascript). They follow the same characteristics and purposes like the custom functional tests.

>[!NOTE]
>
>Custom UI tests are executed in the production and non-production (opt-in) pipelines which are used by your AEM application changes deployments and AEM product push updates and are therefore a key contribution to help ensure proper functioning of your application and increase release safety. The customer UI tests are also executed in internal pre-release validation pipelines for each customer, which helps provide early feedback.
>
>Non-Selenium containers should execute tests using an HTTP proxy based on the environment variables in the [UI Testing Section](/help/implementing/cloud-manager/ui-testing.md#custom-ui-testing).

In order to keep pipeline executions efficient, we recommend focusing on key features and main user interaction flows. Full UI test suites that do not fit in this quality gate are recommended to be executed as part of general customer validation pipelines during customer's development flow.

See [open-sourced example tests](https://github.com/adobe/aem-test-samples/tree/aem-cloud/) or the [ui.tests module of the AEM Projects Archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/uitests.html) for examples.

See [Custom UI Testing](/help/implementing/cloud-manager/ui-testing.md#custom-ui-testing) for more information.

### Experience audit

The experience audit quality gate is performing [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) audits against the customer's webpage.

This quality gate is provided by AEM out-of-the-box, but is not blocking the deployment pipelines. By default, an audit against the root page (`/`) of the publish instance is performed. You can contribute by configuring up to 25 custom paths that are considered for audits.

See [Experience Audit Testing](/help/implementing/cloud-manager/experience-audit-dashboard.md) for more information.

### Customer validations

The customer validations quality gate is a placeholder for the customer's own testing strategy and effort, executed before the customer's application changes reach the AEM cloud deployment pipelines.

Here you can choose the tools and frameworks you prefer. In contrast to customer function tests and custom UI tests, there are no AEM as a Cloud Service related limits, and we therefore recommend to perform long-running functional and UI testing here.

While you are free to choose any tool and framework, we recommend you align HTTP-based integration tests and UI tests with the tools and frameworks available in the custom functional tests and custom UI test quality gates. We recommend integrating [Rapid Development Environments (RDE)](/help/implementing/developing/introduction/rapid-development-environments.md) in your local testing strategy to test as close as possible to AEM cloud environments.

### Manual testing

The Manual testing quality gate is a placeholder for customers who do manual testing. AEM cloud pipelines do not support manual testing and therefore this needs to happen as part of your own local testing strategy.

For manual testing, it can be useful to integrate with an additional AEM Cloud Service development environment. 
