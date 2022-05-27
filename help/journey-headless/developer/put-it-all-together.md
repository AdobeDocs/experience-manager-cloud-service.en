---
title: How to Put It All Together - Your App and Your Content in AEM Headless
description: In this part of the AEM Headless Developer Journey, learn how to take your AEM Project including Content Fragments, your GraphQL calls, your REST API calls, and your application, and prepare it for going live.
exl-id: bece84ad-4c8c-410c-847e-9ef3f79970cb
---
# How to Put It All Together - Your App and Your Content in AEM Headless {#put-it-all-together}

In this part of the [AEM Headless Developer Journey](overview.md), you will get familiar with learn how to use the AEM development tooling as well as the Headless SDK to put your application together.

## The Story So Far {#story-so-far}

In the previous document of the AEM headless journey, [How to Update Your Content via AEM Assets APIs](update-your-content.md) you learned how to update your existing headless content in AEM via API and you should now:

* Understand the AEM Assets HTTP API.

## Objective {#objective}

This article aims to help you understand how to put your AEM headless application together by:

* Learning about the AEM Headless SDK and the development tooling required
* Setting up a local development runtime to simulate your content before going live
* Understanding AEM Content Replication Basics

## The AEM SDK {#the-aem-sdk}

The AEM SDK is used to build and deploy custom code. It is the main tool you need in order to develop and test your headless application before going live. It contains the following artifacts:

* The Quickstart jar - an executable jar file that can be used to set up both an author and a publish instance
* Dispatcher tools - the Dispatcher module and its dependencies for Windows and UNIX based systems
* Java API Jar - The Java Jar/Maven Dependency that exposes all allowed Java APIs that can be used to develop against AEM
* Javadoc jar - the javadocs for the Java API jar

## The AEM Headless SDK {#the-aem-headless-sdk}

Different from the AEM SDK, the AEM **Headless SDK** is set of libraries that can be used by clients to quickly and easily interact with AEM Headless APIs over HTTP.

For more information on the AEM Headless SDK, see the [documentation here](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/graphql/how-to/aem-headless-sdk.html?lang=en).

## Additional Development Tools {#additional-development-tools}

In addition to the AEM SDK, you will need additional tooling that facilitates developing and testing your code and content locally:

* Java
* Git
* Apache Maven
* The Node.js library
* The IDE of your choice

Because AEM is a Java application, you need to install Java and the Java SDK to support the development of AEM as a Cloud Service.

Git is what you will use to manage source control as well as to check in the changes to Cloud Manager and then deploy them to a production instance.

AEM uses Apache Maven to build projects projects generated from the AEM Maven Project archetype. All major IDEs provide integration support for Maven.

Node.js is a JavaScript runtime environment used to work with the front-end assets of an AEM project’s `ui.frontend` sub-project. Node.js is distributed with npm, is the de facto Node.js package manager, used to manage JavaScript dependencies.

## Components of an AEM System at a Glance {#components-of-an-aem-system-at-a-glance}

Next, let's take a look at the constituent parts of an AEM environment.

A full AEM environment is made up of an Author, Publish, and Dispatcher. These same components will be made available in the local development runtime in order to make it easier for you to preview your code and content before going live.

* **The Author service** is where internal users create, manage, and preview content.

* **The Publish service** is considered the “Live” environment and is typically what end users interact with. Content, after being edited and approved on the Author service, is distributed to the Publish service. The most common deployment pattern with AEM headless applications is to have the production version of the application connect to an AEM Publish service.

* **The Dispatcher** is a static web server augmented with the AEM dispatcher module. It caches web pages produced by the publish instance to improve performance.

## The Local Development Workflow {#the-local-development-workflow}

The local development project is built on Apache Maven and is using Git for source control. In order to update the project, developers can use their preferred integrated development environment, such as Eclipse, Visual Studio Code or or IntelliJ, amongst others.

To test code or content updates that will be ingested by your headless application, you need to deploy the updates to the local AEM runtime, which includes local instances of the AEM author and publish services.

Make sure to take note of the distinctions between each component in the local AEM runtime, as it is important to test your updates where they matter the most. For example, test content updates on author or test new code on the publish instance.

In a production system, a dispatcher and an http Apache server will always sit in front of an AEM publish instance. They provide caching and security services for the AEM system, so it is paramount to test code and content updates against the dispatcher as well.

## Previewing Your Code and Content Locally with The Local Development Environment {#previewing-your-code-and-content-locally-with-the-local-development-environment}

In order to prepare your AEM headless project for launch, you need to make sure all constituent parts of your project are functioning well.

To do that, you need to put everything together: code, content and configuration and test it in a local development environment for go live readiness.

The local development environment is comprised of three main areas:

1. The AEM Project - this will contain all the custom code, configuration and content the AEM developers are going to be working on
1. The Local AEM Runtime - local versions of the AEM author and publish services that will be used to deploy code from the AEM project
1. The Local Dispatcher Runtime - a local version of the Apache htttpd webserver that includes the Dispatcher module

Once the local development environment is set up, you can simulate content serving to the React app by deploying a static Node server locally.

In order to get a more in depth look at setting up a local development environment and all dependencies needed for content preview see [Production Deployment documentation](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/graphql/multi-step/production-deployment.html?lang=en#prerequisites).

## What's Next {#whats-next}

Now that you have completed this part of the AEM Headless Developer Journey, you should:

* Be familiar with the AEM Development Tools 
* Understand the local development workflow

You should continue your AEM headless journey by next reviewing the document [How to Go Live with Your Headless Application](/help/journey-headless/developer/go-live.md) where you actually take your AEM Headless project live!

## Additional Resources {#additional-resources}

* [The AEM as a Cloud Service SDK](/help/implementing/developing/introduction/aem-as-a-cloud-service-sdk.md)
* [Set Up A Local AEM Environment](https://experienceleague.adobe.com/docs/experience-manager-learn/foundation/development/set-up-a-local-aem-development-environment.html)
* [AEM Headless SDK for client-side browsers (JavaScript)](https://github.com/adobe/aem-headless-client-js)
* [AEM Headless SDK for server-side/Node.js (JavaScript)](https://github.com/adobe/aem-headless-client-nodejs)
* [AEM Headless SDK for Java™](https://github.com/adobe/aem-headless-client-java)

