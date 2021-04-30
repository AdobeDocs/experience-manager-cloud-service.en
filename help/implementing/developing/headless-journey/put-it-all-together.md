---
title: How to Put It All Together - Your App and Your Content in AEM Headless
description: In this part of the AEM Headless Developer Journey, learn how to take your AEM Project including Content Fragments, your GraphQL calls, your REST API calls, and your application, and prepare it for going live.
hide: yes
hidefromtoc: yes
index: no
---

# How to Put It All Together - Your App and Your Content in AEM Headless {#put-it-all-together}

>[!CAUTION]
>
>WORK IN PROGRESS - The creation of this document is ongoing and it should not be understood as complete or definitive nor should it be used for production purposes.

In this part of the [AEM Headless Developer Journey,](#overview.md) learn how to take your AEM Project including Content Fragments, your GraphQL calls, your REST API calls, and your application, and prepare it for going live.

## The Story So Far {#story-so-far}

In the previous document of the AEM headless journey, [How to Update Your Content via AEM Assets APIs](update-your-content.md) you learned how to update your existing headless content in AEM via API and you should now:

* Understand the AEM Assets HTTP API.

This article builds on those fundamentals so you understand how to prepare your own AEM headless project to go live.

## Objective {#objective}

* Understand what is the local development workflow for AEM 
* Install the AEM SDK to get a local development runtime you can use to test your content on
* Learn about the development tools you need to have working beside the local development runtime

## The Local Development Workflow {#the-local-development-workflow}

The local development project is built on Apache Maven and is using Git for source control. In order to update the project, developers can use their preferred integrated development environment, such as Eclipse, Visual Studio Code or or IntelliJ, amongst others.

To test code or content updates that will be ingested by your headless application, you need to deploy the updates to a local AEM runtime, which includes local instances of the AEM author and publish instances.

Make sure to take note of the distinctions between each component in the local AEM runtime, as it is important to test your updates where they matter the most - for example, test content updates on author or test new code on the publish instance.

In a production system, a dispatcher and an http Apache server will always sit in front of an AEM publish instance. They provide caching and sercurity services for the AEM system, so it is paramount to test code and content updates against the dispatcher as well.

Once you make sure everything has been tested and is working properly, you are ready to push your code updates to a centralized Git repository in Cloud Manager.

After the updates have been uploaded to Cloud Manager, they can be deployed to AEM as a Cloud Service using Cloud Manager's CI/CD pipeline.


## The AEM SDK {#the-aem-sdk}

The AEM SDK is used to build and deploy custom code. It contains the following artifacts:

* The Quickstart jar - an executable jar file that can be used to set up both an author and a publish instance
* Dispatcher tools - the Dispatcher module and its dependencies for Windows and UNIX based systems
* Java API Jar - The Java Jar/Maven Dependency that exposes all allowed Java APIs that can be used to develop against AEM 
* Javadoc jar - the javadocs for the Java API jar

## Local Development Environment Setup {#local-development-environment}

In order to prepare your AEM headless project for launch, you need to make sure all constituent parts of your project are functioning well.

To do that, you need to put everything together - code, content and configuration and test it in a local development environment for go live readiness.

The local development environment is comprised of three main areas:

1. The AEM Project - this will contain all the custom code, configuration and content the AEM developers are going to be working on
1. The Local AEM Runtime - local versions of the AEM author and publish services that will be used to deploy code from the AEM project
1. The Local Dispatcher Runtime - a local version of the Apache htttpd webserver that includes the Dispatcher module

## Development Tools {#development-tools}

In addition to the AEM SDK, you will need additional tooling that facilitates developing and testing your code and content locally:

* Java
* Git
* Apache Maven
* The Node.js library
* The IDE of your choice

Because AEM is a Java application, you need to install Java and the Java SDK to support the development of AEM as a Cloud Service.

Git is the tool you will use to manage source control as well as to check in the changes to Cloud Manager and then deploy them to a production instance.

AEM uses Apache Maven to build projects projects generated from the AEM Maven Project archetype. All major IDEs provide integration support for Maven.

Node.js is a JavaScript runtime environment used to work with the front-end assets of an AEM project’s ui.frontend sub-project. Node.js is distributed with npm, is the de facto Node.js package manager, used to manage JavaScript dependencies.

## What's Next {#what-is-next}

You should continue your AEM headless journey by next reviewing the document [How to Go Live with Your Headless Application](go-live.md) where you actually take your AEM Headless project live!

## Additional Resources {#additional-resources}

* [Local Developmment Environment Setup](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/overview.html?lang=en#local-dispatcher-runtime) - learn how to install the tooling needed to start developing for AEM
* [AEM as a Cloud Service SDK](/help/implementing/developing/introduction/aem-as-a-cloud-service-sdk.md) - take an in depth look at the AEM SDK