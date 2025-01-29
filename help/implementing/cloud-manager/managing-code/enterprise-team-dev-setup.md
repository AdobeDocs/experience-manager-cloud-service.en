---
title: Enterprise Development Team Setup
description: Learn how to set up and scale your enterprise development team and see how AEM as a Cloud Service can support your development process.
exl-id: 85f8779b-12cb-441b-a34d-04641184497a
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---
# Enterprise development team setup for AEM as a Cloud Service {#enterprise-setup}

Learn how to set up and scale your enterprise development team and see how AEM (Adobe Experience Manager) as a Cloud Service can support your development process.

## Introduction {#introduction}

To support customers with enterprise development setups, AEM as a Cloud Service fully integrates with Cloud Manager and its purpose-built, [opinionated CI/CD pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md). These pipelines and services are built based on best practices, ensuring thorough [testing and the highest code quality](/help/implementing/cloud-manager/code-quality-testing.md).

## Cloud Manager's support in enterprise team development setup {#cloud-manager}

To ensure quick onboarding, Cloud Manager provides everything required to get started with developing digital experiences right away, including a Git repository to store customizations, which then get built, verified, and deployed by Cloud Manager.

Using Cloud Manager, development teams can work towards committing changes frequently without being dependent on Adobe personnel. 

Three types of environments are available in Cloud Manager.

* Development
* Stage
* Production 

Code can be deployed to development environments using a non-production pipeline. For staging and production environments, which always go together and thus ensure validation before production deployment as best practice, a production pipeline uses [quality gates](/help/implementing/cloud-manager/custom-code-quality-rules.md) to validate the application code and the configuration changes. 

The production pipeline deploys the code and the configuration to the staging environment first, tests the application, and finally deploys to production.

A Cloud Service SDK that is always updated with latest AEM as a Cloud Service improvements allows for local development directly using the developer's local hardware. This approach enables rapid development with very low turnaround times. Thus, developers can stay in their familiar local environment and choose from a wide variety of development tools, and push to development environments or production when they see fit. 

Cloud Manager supports flexible multi-team setups that can be adjusted to fit the needs of an enterprise. To ensure stable deployments across multiple teams, Cloud Manager's opinionated pipeline validates and tests the code from all teams together. This approach helps prevent situations where one team's changes impact production for all teams.

## Real world example {#real-world-example}

Each enterprise has different requirements including different team setup, processes, and development workflows. The setup described below is used by Adobe for several projects that deliver experiences on top of AEM as a Cloud Service.

For instance, the Adobe Creative Cloud applications, such as Adobe Photoshop or Adobe Illustrator, include content resources such as tutorials, samples, and guides available to their end users. Client applications consume content from AEM as a Cloud Service in a headless manner. They make API calls to the AEM Cloud publish tier to retrieve structured content as JSON streams. Additionally, the [Content Delivery Network (CDN) in AEM as a Cloud Service](/help/implementing/dispatcher/cdn.md#content-delivery) is used to serve both structured and unstructured content with optimal performance.

The teams contributing to this project adhere to the following process.

Each team uses its own development workflow and has a separate Git repository. An additional shared Git repository is used for onboarding projects. This Git repository contains the root structure of Cloud Manager's Git repository, including the shared Dispatcher configuration.

Onboarding a new project requires listing in the reactor Maven project file at the root of the shared Git repository. For Dispatcher configuration, a new configuration file is created inside the Dispatcher project. The main Dispatcher configuration then includes this file. Each team is responsible for its own Dispatcher configuration file. Changes to the shared Git repository are rare and are usually only required when a new project is onboarded. The main work is done by each project team within their own Git repository.
 
![Workflow diagram](/help/implementing/cloud-manager/assets/team-setup1.png)

The Git repository for each is set up using the [AEM Project Archetype](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/developing/archetype/overview) and thus follows the best practices for setting up AEM Projects. The only exception is the Dispatcher configuration, which is done in the shared Git repository as outlined above.

Each team uses a simplified Git workflow with two + N branches, following the Git flow model:

* A stable release branch contains the production code.

* A development branch contains the latest development.

* For each feature, a new branch is created.

Development is done in a feature branch. When the feature matures, it is merged into the development branch. Completed and validated features are picked from the development branch and merged into the stable branch.

All changes are done through PRs (Pull Requests). Quality gates automatically validate each PR. Sonar is used for quality checking the code and a set of test suites is run to ensure that the new code is not introducing any regression.

The setup in the Cloud Manager's Git repository has two branches.

* A stable release branch contains the production code from all teams.
* A development branch contains the development code from all teams.

Every push to a team's Git repository in either the development or the stable branch triggers a [GitHub action](/help/implementing/cloud-manager/managing-code/working-with-multiple-source-git-repositories.md#managing-code).

All projects follow the same setup for the stable branch. A push to the stable branch of a project is automatically pushed to the stable branch in Cloud Manager's Git repository. A push to the stable branch triggers the production pipeline in Cloud Manager. Each push by any team into a stable branch triggers the production pipeline. The production deployment is updated if all quality gates pass.

![Push diagram](/help/implementing/cloud-manager/assets/team-setup2.png)
 
Pushes to the development branch are handled differently. A push to a developer branch in a team's Git repository also triggers a GitHub action. This action automatically pushes the code into the development branch in Cloud Manager's Git repository. However, this code push does not automatically trigger the non-production pipeline. A call to Cloud Manager's API triggers it.

Running the production pipeline includes checking the code of all teams via the provided quality gates. After the code is deployed to stage, the tests and audits are run so everything is working as expected. When all gates are passed, the changes are rolled out to production without any interruption or downtime.

For local development, the [SDK for AEM as a Cloud Service](/help/implementing/developing/introduction/aem-as-a-cloud-service-sdk.md#developing) is used. The SDK allows a local author, publish, and Dispatcher to be set up. This workflow enables offline development and quick turnaround times. Sometimes only the author environment is used for development, but quickly setting up Dispatcher and publish environments allows testing everything locally before pushing into the Git repository.

Members of each team usually checkout the code from the shared Git for their own project code. There is no need to check out other projects because the projects are independent.

![Local checkout and SDK](/help/implementing/cloud-manager/assets/team-setup3.png)
 
This real-world setup can be used as a blueprint and then customized to the needs of an enterprise. The flexible branching and merging concept of Git allows for variations of the above workflows, customized to every team's needs. AEM as a Cloud Service supports all these variations without sacrificing the core value of the opinionated Cloud Manager pipeline.

>[!TIP]
>
>See [Work with Multiple Source Git Repositories](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/managing-code/multiple-git-repos#managing-code) to learn more about this setup.

### Considerations for a multi-team setup {#considerations}

With Cloud Manager's Git repository and the production pipeline, the full production code always passes through all quality gates, treating it as one deployment unit. This way the production system is always up without interruption or downtime.

In contrast, without such a system in place, because each team can deploy separately, there is a risk that an update from a single team can lead to production stability issues. In addition, it requires coordination and planned downtime to roll out updates. With an increasing number of teams, the coordination effort becomes much more complex and quickly unmanageable.

If a problem is detected in the quality gates, production is not affected, and the problem can be detected and fixed without Adobe personnel required to step in. Without Cloud Service and without always testing the whole deployment, partial deployments can cause outages requiring a request to roll back or even a full restore from a backup. Partial testing can also cause additional issues that must be resolved later, once again requiring coordination and support from Adobe personnel.

>[!TIP]
>
>For any multi-team setup, it is crucial to define a governance model and a set of standards all teams have to follow. The previous blueprint for a multi-team setup allows scaling across a larger number of teams, which you can use as a starting point.
