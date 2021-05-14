---
title: How to Go Live with Your Headless Application
description: In this part of the AEM Headless Developer Journey, learn how to deploy a headless application live by taking your local code in Git and moving it to Cloud Manager Git for the CI/CD pipeline.
hide: yes
hidefromtoc: yes
index: no
exl-id: f79b5ada-8f59-4706-9f90-bc63301b2b7d
---
# How to Go Live with Your Headless Application {#go-live}

>[!CAUTION]
>
>WORK IN PROGRESS - The creation of this document is ongoing and it should not be understood as complete or definitive nor should it be used for production purposes.

In this part of the [AEM Headless Developer Journey,](overview.md) learn how to deploy a headless application live by taking your local code in Git and moving it to Cloud Manager Git for the CI/CD pipeline.

## The Story So Far {#story-so-far}

In the previous document of the AEM headless journey, [How to Put It All Together - Your App and Your Content in AEM Headless](put-it-all-together.md) you learned how to prepare your own AEM headless project to go live and you should now:

* Understand the requirements to go live.

This article builds on those fundamentals so you understand how to actually take your AEM Headless project live.

## Objective {#objective}

This document helps you understand the AEM headless publication pipeline and the performance considerations you need to be aware of before you go live with your application.

* Learn about the AEM SDK and the development tooling required
* Set up a local development runtime to simulate your content before going live
* Understand AEM Content Replication and Caching Basics
* Secure and Scale your application before Launch
* Monitor Performance and Debug Issues

## The AEM SDK {#the-aem-sdk}

 It contains the following artifacts:

* The Quickstart jar - an executable jar file that can be used to set up both an author and a publish instance
* Dispatcher tools - the Dispatcher module and its dependencies for Windows and UNIX based systems
* Java API Jar - The Java Jar/Maven Dependency that exposes all allowed Java APIs that can be used to develop against AEM 
* Javadoc jar - the javadocs for the Java API jar

## Development Tools {#development-tools}

In addition to the AEM SDK, you will need additional tooling that facilitates developing and testing your code and content locally:

* Java
* The AEM SDK
* Git
* Apache Maven
* The Node.js library
* The IDE of your choice

Because AEM is a Java application, you need to install Java and the Java SDK to support the development of AEM as a Cloud Service.

The AEM SDK is used to build and deploy custom code. It is the main tool you need in order to test your headless application before going live.

Git is what you will use to manage source control as well as to check in the changes to Cloud Manager and then deploy them to a production instance.

AEM uses Apache Maven to build projects projects generated from the AEM Maven Project archetype. All major IDEs provide integration support for Maven.

Node.js is a JavaScript runtime environment used to work with the front-end assets of an AEM project’s ui.frontend sub-project. Node.js is distributed with npm, is the de facto Node.js package manager, used to manage JavaScript dependencies.

## Components of an AEM System at a Glance {#components-of-an-aem-system-at-a-glance}

A full AEM environment is made up of an Author, Publish, and Dispatcher. These same components will be made available in the local development runtime in order to make it easier for you to preview your code and content before going live.

* **The Author service** is where internal users create, manage, and preview content.

* **The Publish service** is considered the “Live” environment and is typically what end users interact with. Content, after being edited and approved on the Author service, is distributed to the Publish service. The most common deployment pattern with AEM headless applications is to have the production version of the application connect to an AEM Publish service.

* **The Dispatcher** is a static web server augmented with the AEM dispatcher module. It caches web pages produced by the publish instance to improve performance.

## The Local Development Workflow {#the-local-development-workflow}

The local development project is built on Apache Maven and is using Git for source control. In order to update the project, developers can use their preferred integrated development environment, such as Eclipse, Visual Studio Code or or IntelliJ, amongst others.

To test code or content updates that will be ingested by your headless application, you need to deploy the updates to the local AEM runtime, which includes local instances of the AEM author and publish services.

Make sure to take note of the distinctions between each component in the local AEM runtime, as it is important to test your updates where they matter the most. For example, test content updates on author or test new code on the publish instance.

In a production system, a dispatcher and an http Apache server will always sit in front of an AEM publish instance. They provide caching and sercurity services for the AEM system, so it is paramount to test code and content updates against the dispatcher as well.

Once you make sure everything has been tested and is working properly, you are ready to push your code updates to a centralized Git repository in Cloud Manager.

After the updates have been uploaded to Cloud Manager, they can be deployed to AEM as a Cloud Service using Cloud Manager's CI/CD pipeline.

## Previewing Your Code and Content Locally with The Local Development Environment {#previewing-your-code-and-content-locally-with-the-local-development-environment}

In order to prepare your AEM headless project for launch, you need to make sure all constituent parts of your project are functioning well.

To do that, you need to put everything together: code, content and configuration and test it in a local development environment for go live readiness.

The local development environment is comprised of three main areas:

1. The AEM Project - this will contain all the custom code, configuration and content the AEM developers are going to be working on
1. The Local AEM Runtime - local versions of the AEM author and publish services that will be used to deploy code from the AEM project
1. The Local Dispatcher Runtime - a local version of the Apache htttpd webserver that includes the Dispatcher module

Once the local development environment is set up, you can simulate content serving to the React app by deploying a static Node server locally.

In order to get a more in depth look at setting up a local development environemnt and all dependencies needed for content preview see [Production Deployment with an AEM Publish Service](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/graphql/multi-step/production-deployment.html?lang=en#prerequisites).

## Deploy to Production {#deploy-to-production}

Once you have tested all your code and content locally, you are ready to commence a production deployment with AEM.

You can start deploying your code by leveraging the Cloud Manager CI/CD pipeline, which is covered extensively [here](/help/implementing/deploying/overview.md).

## Prepare your AEM Headless Application for Go-Live {#prepare-your-aem-headless-application-for-golive}

Now it's time to get your AEM headless application ready for launch, by followiing the best practices outlined below.

### Secure and Scale your Headless Application Before Launch {#secure-and-scale-before-launch}

1. Configure [Token Based Authentication](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md)
1. Secure Webhooks
1. Configure Caching and Scalability

### Model Structure vs GraphQL Output {#structure-vs-output}

* Avoid creating queries that output more than 15kb of JSON (gzip compressed). Long JSON files are resource intensive for client application to parse.
* Avoid more than five nested levels of fragment hierarchies. Additional levels make it hard for content authors to consider the impact of their changes.
* Use multi-object queries instead of modeling queries with dependency hierarchies within the models. This allows more long-term flexibility to restructure JSON output without having to do a lot of content changes.

### Maximize CDN Cache-Hit Ratio {#maximize-cdn}

* Do not use direct GraphQL queries, unless you are requesting live content from the surface.
  * Instead, use persisted queries.
  * Provide CDN TTL above 600 seconds so the CDN can cache them.
  * AEM can calculate the impact of a model change to existing queries.
* Split JSON files/GraphQL queries between low and high content change rate in order to reduce client traffic to CDN and assign higher TTL. This minimizes the CDN revalidating the JSON with the origin server.
* To actively invalidate content from the CDN use Soft Purge. This allows the CDN to re-download the content without causing a cache miss.

### Improve Time to Download Headless Content {#improve-download-time}

* Make sure HTTP clients use HTTP/2.
* Make sure HTTP clients Accept Headers request for gzip.
* Minimize the number of domains used to host JSON and referenced artifacts.
* Leverage `Last-modified-since` to refresh resources.
* Use `_reference` output in JSON file to start downloading assets without having to parse complete JSON files.

## Performance Monitoring {#performance-monitoring}

In order for users to have the best possible experience when using the AEM headless application, it is important that you monitor key performance metrics, as detailed below:

* Validate preview and production versions of the app
* Verify AEM status pages for current service availability status
* Access performance reports
  * Delivery Performance
    * Fastly (CDN) – check number of calls, cache rate, error rates, payload traffic
    * Origin servers - number of calls, error rates, CPU loads, payload traffic
  * Author Performance
    * Check number of users, requests and load
* Access App and Space specific performance reports
  * Once the server is up, check whether the general metrics are green/orange/red, then identify specific app issues
  * Open same reports above filtered to app/space (I.e. Photoshop desktop, paywall, etc.)
  * Use Splunk log APIs to access service and application performance
  * Contact Customer Support in case there are other issues.

## Troubleshooting {#troubleshooting}

### Debugging {#debugging}

Follow these best practices as a general approach to debugging:

* Validate functionality and performance with the preview version of the application
* Validate functionality and performance with the production version of the application
* Validate with the JSON preview of the Content Fragment Editor
* Inspect the JSON in the client application to check for the presence of client application or delivery issues
* Inspect the JSON using GraphQL to check for the presence of issues related to cached content or AEM

### Logging a Bug with Support {#logging-a-bug-with-support}

In order to efficiently log a bug with Support in case you need further assistance, follow the below steps:

* Take screenshots of the problem, if necessary
* Document a way to reproduce the issue
* Document the content the issue reproduces with
* Log an issue through the AEM Support portal with the appropriate priority

## What's Next {#what-is-next}

Now that you have completed this part of the AEM Headless Developer Journey, you should:

* Understand AEM Content Replication and Caching Basics.
* Know how to configure the tooling required to simulate go live for your headless application.
* Know how to secure and Scale your application before Launch.
* Understand how to monitor Performance and Debug Issues.

You should continue your AEM headless journey by next reviewing the document [Post Launch](post-launch.md) where you learn how to maintain your headless experience.

## Additional Resources {#additional-resources}

* [Set Up A Local AEM Environment](https://experienceleague.adobe.com/docs/experience-manager-learn/foundation/development/set-up-a-local-aem-development-environment.html)
* [The AEM as a Cloud Service SDK](/help/implementing/developing/introduction/aem-as-a-cloud-service-sdk.md)
* [An Overview of Deploying to AEM as a Cloud Service](/help/implementing/deploying/overview.md)
* [Use Cloud Manager to Deploy Your Code](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/how-to-use/deploying-code.html)
* [Integrate the Cloud Manager Git Repository with an External Git Repository and Deploy a Project to AEM as a Cloud Service](https://git.corp.adobe.com/AdobeDocs/experience-manager-cloud-service.en/blob/master/help/implementing/developing/headless-journey/access-your-content.md)