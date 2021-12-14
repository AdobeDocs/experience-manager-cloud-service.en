---
title: Implementation Phase
description: Making sure your code and content are ready for the migration to the cloud
exl-id: 176dd79d-0d72-443c-87db-dab24fb48b96
---
# Implementation Phase {#implementation-phase}

In the implementation phase of the journey, you will explore the tools through which you can make your code and content ready to be moved over to AEM as a Cloud Service.

## The Story So Far {#story-so-far}

In the previous parts of the journey you've went through [getting familiar with the changes in AEM as a Cloud Service](/help/journey-migration/getting-started.md), as well as determining if your deployment is ready to be moved to the cloud with the [readiness phase](/help/journey-migration/readiness.md).

This article continues on with advice on how to use Adobe provided tools to make sure your code and content are ready to be moved to the cloud.

## Objective {#objective}

This document aims to:

* Introduce you to Cloud Manager, AEM's continuous integration and delivery framework used to deploy code to AEM as a Cloud Service
* Get you up to speed with the content transfer tool
* Describe the code refactoring tools you will have to use in order to modernize your code for AEM as a Cloud Service

## Using Cloud Manager {#using-cloud-manager}

Before you start, you need to familiarize yourself with Cloud Manager since it is the sole mechanism for deploying code to AEM as a Cloud Service.

Cloud Manager enables organizations to self-manage AEM in the Cloud. It includes a continuous integration and continuous delivery (CI/CD) framework that lets IT teams and implementation partners expedite the delivery of customizations or updates without compromising performance or security.

You can get familiar with using Cloud Manager by consulting the resources below:

* [Onboarding to Experience Manager as a Cloud Service](/help/onboarding/home.md) to understand self-help resources about onboarding for Experience Manager as a Cloud Service.

* [Integrating Git with Adobe Cloud Manager](/help/implementing/cloud-manager/managing-code/integrating-with-git.md) to learn about using a Single Git repository to deploy code.

* [Adobe Experience as a Cloud Service Configuration](/help/security/ims-support.md#aem-configuration) to learn about Managing Products and User Access in Admin Console.

## Use the Adobe Provided Tools to Make Your Content and Code Cloud Ready {#use-tools-to-make-code-and-content-cloud-ready}


The exact steps of your transition to Cloud Service depends on the systems you have purchased and the software development life-cycle practices you follow.

The following figure shows the main steps involved in the phase that involves converting your code and content for use with AEM as a Cloud Service:

![image](/help/move-to-cloud-service/assets/exec-image1.png)

We will start detailing the tools you need to leverage in order to achieve this in the chapters below.

## Content Migration {#content-migration}

To migrate content from your current AEM instance to your Cloud Service instance, you can use Adobe's Content Transfer Tool.

With this tool, you can specify the desired content subset that you want to transfer from your source AEM instance to your AEM Cloud Service instance.

Content Migration is a multi-step aprocess that requires planning, tracking and collaboration between different teams. 

<!--- The following diagram lays out the ideal path to be followed for a successful content migration. 

![](/help/journey-migration/assets/contenttransferoverview.png) -->

<!-- Alexandru: looks to be redundant, given that it's already covered in the CTT docs.

>[!NOTE]
>It is recommended to do frequent differential content top-ups to shorten the content freeze period for the final differential content transfer before going live on Cloud Service. -->

For a complete detail on how the tool works and how we recommend you use it, see the [Content Transfer Tool documentation](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/overview-content-transfer-tool.md).

<!-- Alexandru: looks to be redundant, given that it's already covered in the CTT docs. 

>[!IMPORTANT]
>Minimum system requirement for Content Transfer Tool is AEM 6.3 + and JAVA 8. If you are on a lower AEM version, you will need to upgrade your content repository to AEM 6.5 to use the Content Transfer Tool. -->

## Code Refactoring {#code-refactor}

### Set Up for Development {#set-up-for-development}

It is time to start refactoring the existing features to be compatible with Cloud Services.

In order to do this, you need to take a look at the documentation detailing the basic tooling you'll need to start refactoring your code:


* During planning, it is a good idea to have a list of areas that need to be refactored in order to be compatible with AEM as a Cloud Service. You can review [Development Guidelines](/help/implementing/developing/introduction/development-guidelines.md) for more details on how to refactor and optimize code for Cloud Service.  
* Read up on how to [Manage Configurations](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/configurations.html?lang=en#what-is-a-configuration) in AEM as a Cloud Service.
* Learn how to set up a Local Development Environment by downloading the [AEM as a Cloud Service SDK](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/aem-as-a-cloud-service-sdk.html?lang=en)
* Finally, familiarize yourself with the [AEM as a Cloud Service Java API](https://www.adobe.io/experience-manager/reference-materials/cloud-service/javadoc/index.html).

Additionally, you can also:

* Watch this video to understand how to install the Dispatcher SDK locally:

  >[!VIDEO](https://video.tv.adobe.com/v/30601)

* Watch this video to understand how to configure Dispatcher SDK:

  >[!VIDEO](https://video.tv.adobe.com/v/30602)

### A Change in Mindset {#a-change-in-mindset}

Developing and running code in AEM as a Cloud Service requires a change in the mindset. It should be noted that code must be resilient, especially as an instance might be stopped at any time. Code running in Cloud Service must be aware of the fact that it is always running in a cluster. This means that there is always more than one instance running.

Certain changes are required in order for AEM Maven projects to be cloud compatible. AEM as a Cloud Service requires a separation of *content* and *code* into distinct packages for deployment into AEM:  

* `/apps` and `/libs` are considered immutable areas of AEM as they cannot be changed after AEM starts (that is to say at runtime). This includes create, update or delete operations. Any attempt to change an immutable area at runtime will fail.

* Everything else in the repository, (for example, `/content` , `/conf` , `/var` , `/home` , `/etc` , `/oak:index` , `/system` , `/tmp`) are all mutable areas, meaning they can be changed at runtime.

You can learn more by consulting the [Recommended Package Structure](/help/implementing/developing/introduction/aem-project-content-package-structure.md#recommended-package-structure) documentation. 


### Cloud Migration Tools {#cloud-migration-tools}

Adobe provides several tools to help accelerate some of your code refactoring tasks. Understanding these tools and the problems they solve will reduce migration complexity and time.

* [Asset Workflow Migration](/help/move-to-cloud-service/moving-to-aem-assets/asset-workflow-migration-tool.md), a tool that is use to automatically migrate asset processing workflows
* [Dispatcher Converter](/help/move-to-cloud-service/refactoring-tools/dispatcher-transformation-utility-tools.md), a tool that converts your existing Dispatcher configurations into a format that is ready for AEM as a Cloud Service.
* [Repository Modernizer](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/moving/refactoring-tools/repo-modernizer.html?lang=en), a tool that takes an AEM Multimode project as input and converts it into an AEM as a Cloud Service one
* [Index Converter](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/moving/refactoring-tools/index-converter.html?lang=en), a tool that converts indexes into a form compatible with AEM as a Cloud Service
* [Modernization Tools](/help/move-to-cloud-service/refactoring-tools/aem-modernization-tools.md), a suite of utilities which can be used to convert legacy AEM features to the modern and supported capabilities of AEM as a Cloud Service.

<!-- ### Test and Refactor Your Code Locally {#refactor-your-code-locally}

It is recommended to refactor and test the code locally before pushing it to a Cloud Service environment via Git with Cloud Manager. 

You can start by learning how to [set up a local development environment](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/overview.html). -->

Once you have set up the local development environment, get familiar with the AEM as a Cloud Service SDK by consulting the [documentation](/help/implementing/developing/introduction/aem-as-a-cloud-service-sdk.md).


### Schedule a Content Freeze {#schedule-a-content-freeze}  

To manage your on-going code development on your active AEM along with the code refactoring tasks as part of your transition journey, we recommended you schedule a code freeze period until you have completed restructuring your Maven project to be compatible with AEM as a Cloud Service.

Once the project restructuring is done, you can resume new code development based on this new structure. This will reduce Cloud Manager pipeline failures during code deployment and testing.

>[!NOTE]
>The Content Transfer and Code Refactor tasks do not have be done sequentially. These tasks can be done independent of each other. However, the correct project structure is required to ensure that the content successfully renders in your Cloud Service environment.

## Best Practices for Code Deployment and Testing {#best-practices}

The Cloud Manager pipeline will support execution of tests that run against the stage environment.

Follow the best practices in the documents below regarding code quality testing:

* [Code Quality Testing](/help/implementing/cloud-manager/code-quality-testing.md), a document that describes the process of writing test scripts and explains the concept of recommended coverage of at least 50%.
* [Understanding Custom Code Quality Rules](/help/implementing/cloud-manager/custom-code-quality-rules.md) which aims to describe the custom code quality rules executed by Cloud Manager created based on best practices from AEM Engineering.

## What's Next {#what-is-next}

Once you've fully understood how to asses if your AEM installation is ready to be moved to the cloud, as we as learn how to use the tools needed to make it ready, it's time to move on to the [go-live phase](help/journey-migration/go-live.md).

## Additional Resources {#additional-resources}

