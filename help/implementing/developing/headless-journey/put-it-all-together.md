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

* List
* of
* objectives

## Local Development Environment Setup {#local-development-environment}

In order to prepare your AEM headless project for launch, you will need to set up a local development environment.

The local development environment is composed of three main areas:

1. The AEM Project - this will contain all the custom code, configuration and content the AEM developers are going to be working on
1. The Local AEM Runtime - local versions of the AEM author and publish services that will be used to deploy code from the AEM project
1. The Local Dispatcher Runtime - a local version of the Apache htttpd webserver that includes the Dispatcher module

### Development Tools {#development-tools}

In order to develop for AEM, you will need the following development tools:

* Java and the Java SDK
* Git for source control
* Maven
* The Node.js library
* Docker for the Local Dispatcher Runtime
* The IDE of your choice

## The Local Development Workflow {#the-local-development-workflow}

The local development project is built on Apache Maven and is using Git for source control. In order to update the project, developers can use their preferred integrated development environment, such as Eclipse, Visual Studio Code or or IntelliJ, amongst others.

To test code updates or content that will be ingested by your headless application, you need to deploy the updates to a local AEM runtime, which includes local instances of the AEM author and publish services.

It is important that you test the author functionality in the author instance, as it is equally important to test code updates against a publish instance.

In a production system, a dispatcher and an http Apache server will always sit in front of an AEM publish instance. They provide caching and sercurity services for the AEM system, so it is imporant to test code and content updates against the dispatcher as well.

Once you make sure everything has been tested and is working properly, you are ready to push your code updates to a centralized Git repository in Cloud Manager.

Once the code updates are in Cloud Manager, they can be deployed to AEM as a Cloud Service using Cloud Manager's CI/CD pipeline.

## The AEM SDK {#the-aem-sdk}



## What's Next {#what-is-next}

Now that you have completed this part of the AEM Headless Developer Journey, you should:

* List
* of
* objectives

You should continue your AEM headless journey by next reviewing the document [How to Go Live with Your Headless Application](go-live.md) where you actually take your AEM Headless project live!

## Additional Resources {#additional-resources}
