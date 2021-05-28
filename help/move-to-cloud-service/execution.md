---
title: Execution Phase
description: Execution Phase
exl-id: 176dd79d-0d72-443c-87db-dab24fb48b96
---
# Execution {#execution-phase}

Before you start the Execution phase, you should be on-boarded to Cloud Service. You also need to familiarize yourself with Cloud Manager since it is the sole mechanism for deploying code to AEM Cloud Service. 

Cloud Manager enables organizations to self-manage AEM in the Cloud. It includes a continuous integration and continuous delivery (CI/CD) framework that lets IT teams and implementation partners expedite the delivery of customizations or updates without compromising performance or security. 

Refer to the following resources below for more details:

* [Onboarding to Experience Manager as a Cloud Service](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/onboarding/home.html) to understand self-help resources about onboarding for Experience Manager as a Cloud Service.

* [Integrating Git with Adobe Cloud Manager](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/managing-code/integrating-with-git.html) to learn about using a Single Git repository to deploy code.

* [Adobe Experience as a Cloud Service Configuration](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/security/ims-support.html#aem-configuration) to learn about Managing Products and User Access in Admin Console.


## Introduction {#introduction}

The exact steps of your transition to Cloud Service depends on the systems you have purchased and the software development life-cycle practices you follow.

The following figure shows the main steps involved in the Execution phase:

![image](/help/move-to-cloud-service/assets/exec-image1.png)

## Content Transfer {#content-transfer}

To transfer content from your current AEM instance to your Cloud Service instance, you can use Adobe's Content Transfer Tool.

With this tool, you can specify the desired content subset that you want to transfer from your source AEM instance to your AEM Cloud Service instance. 

>[!NOTE]
>It is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service.

Refer to [Content Transfer Tool](/help/move-to-cloud-service/content-transfer-tool/overview-content-transfer-tool.md) for more details.

>[!IMPORTANT]
>Minimum system requirement for Content Transfer Tool is AEM 6.3 + and JAVA 8. If you are on a lower AEM version, you will need to upgrade your content repository to AEM 6.5 to use the Content Transfer Tool.

## Code Refactoring {#code-refactor}

Developing and running code in AEM as a Cloud Service requires a change in the mind-set. It should be noted that code must be resilient, especially as an instance might be stopped at any time. Code running in Cloud Service must be aware of the fact that it is always running in a cluster. This means that there is always more than one instance running.

Certain changes are required to AEM Maven projects to be compatible with AEM as a Cloud Service. AEM as a Cloud Service requires a separation of *content* and *code* into discrete packages for deployment into AEM.  

* `/apps` and `/libs` are considered immutable areas of AEM as they cannot be changed (create, update, delete) after AEM starts (i.e. at runtime). Any attempt to change an immutable area at runtime will fail.

* Everything else in the repository, `/content` , `/conf` , `/var` , `/home` , `/etc` , `/oak:index` , `/system` , `/tmp` , etc. are all mutable areas, meaning they can be changed at runtime.

Refer to [Recommended Package Structure](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/developing/aem-project-content-package-structure.html#recommended-package-structure) for more details. 

There are some additional development guidelines that you need to be aware of when developing on AEM as a Cloud Service. Refer to [AEM as a Cloud Service Development Guidelines](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/developing/development-guidelines.html) to learn more.

From your Planning phase, you should have a list of areas that need to be refactored to be compatible with Cloud Service. You should also review [Development Guidelines](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/developing/development-guidelines.html) for more details on how to refactor and optimize code to move to Cloud Service.  

To help accelerate some of your code refactoring tasks, you can use the following tools: 

* [Asset Workflow Migration](/help/move-to-cloud-service/moving-to-aem-assets/asset-workflow-migration-tool.md)
* [Dispatcher Converter](/help/move-to-cloud-service/refactoring-tools/dispatcher-transformation-utility-tools.md)
* [Modernization Tools](/help/move-to-cloud-service/refactoring-tools/aem-modernization-tools.md)

It is recommended to refactor and test the code locally before pushing it to a Cloud Service environment via Cloud Manager Git. 

Review [AEM SDK](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/deploying/overview.html#aem-as-a-cloud-service-sdk) documentation to learn more.

Some additional resources are listed below:

* Watch Install Dispatcher SDK to understand how to install Dispatcher SDK:

  >[!VIDEO](https://video.tv.adobe.com/v/30601)

* Watch Configure Dispatcher SDK to understand on how to configure Dispatcher SDK:

  >[!VIDEO](https://video.tv.adobe.com/v/30602)

* Review [Local Development Setup](https://docs.adobe.com/content/help/en/experience-manager-learn/cloud-service/local-development-environment-set-up/overview.html) documentation to set up a local development environment


To manage your on-going code development on your active AEM along with the code refactoring task as part of your transition journey, it is recommended to schedule a code freeze period until you have completed restructuring your Maven project to be compatible with AEM as a Cloud Service. 

Once, the project restructuring is done, you can resume new code development based on this new structure. This will reduce Cloud Manager pipeline failures during code deployment and testing.

>[!NOTE]
>The Content Transfer and Code Refactor tasks do not have be done sequentially. These tasks can be done independent of each other. However, the correct project structure is required to ensure that the content successfully renders in your Cloud Service environment.

## Best Practices for Code Deployment and Testing {#best-practices}

Cloud Manager for Cloud Services pipeline executions will support execution of tests that run against the stage environment. 

Refer to [Code Quality Testing](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/developing/understand-test-results.html#code-quality-testing) to learn about writing test scripts and recommended coverage of at least 50%.

Additionally, refer to [Understanding Custom Code Quality Rules](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/using-cloud-manager/custom-code-quality-rules.html) to learn more about custom code quality rules executed by Cloud Manager created based on best practices from AEM Engineering.

Cloud Manager usage is the sole mechanism for deploying code to Cloud Service environments.

Follow the resources below to learn how to use Cloud Manager to manage and deploy your code.

* [Managing Environments](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/using-cloud-manager/manage-environments.html)

* [Configuring your CI-CD Pipeline](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/using-cloud-manager/configure-pipeline.html)

* [Deploying your Code](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/using-cloud-manager/deploy-code.html)

## Best Practices for Go-Live Preparation {#go-live}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_prep"
>title="Go-Live Preparation"
>abstract="To ensure a smooth and successful go-live on AEM as a Cloud Service, you should plan for code and content freeze periods, testing iterations, content top-ups, performance tests, security tests and more."

To ensure a smooth and successful go-live on AEM as a Cloud Service, you should consider executing the following steps:

* Schedule code and content freeze period
* Perform final content top-up
* Complete testing iterations
* Run performance and security tests
* Cut-Over
