---
title: How to Go Live with Your Headless Application
description: In this part of the AEM Headless Developer Journey, learn how to deploy a headless application live by taking your local code in Git and moving it to Cloud Manager Git for the CI/CD pipeline.
hide: yes
hidefromtoc: yes
index: no
---

# How to Go Live with Your Headless Application {#go-live}

>[!CAUTION]
>
>WORK IN PROGRESS - The creation of this document is ongoing and it should not be understood as complete or definitive nor should it be used for production purposes.

In this part of the [AEM Headless Developer Journey,](#overview.md) learn how to deploy a headless application live by taking your local code in Git and moving it to Cloud Manager Git for the CI/CD pipeline.

## The Story So Far {#story-so-far}

In the previous document of the AEM headless journey, [How to Put It All Together - Your App and Your Content in AEM Headless](put-it-all-together.md) you learned how to prepare your own AEM headless project to go live and you should now:

* Understand the requirements to go live.

This article builds on those fundamentals so you understand how to actually take your AEM Headless project live.

## Objective {#objective}

This document helps you understand the AEM headless publication pipeline and the performance considerations you need to be aware of before you go live with your application.

* Understand AEM Content Replication and Caching Basics
* Configure the tooling required to simulate go live for your headless application
* Secure and Scale your application before Launch
* Monitor Performance and Debug Issues

## Content Replication and Caching Basics {#content-replication-and-caching}

A full AEM environment is made up of an Author, Publish, and Dispatcher.

* **The Author service** is where internal users create, manage, and preview content.

* **The Publish service** is considered the “Live” environment and is typically what end users interact with. Content, after being edited and approved on the Author service, is distributed to the Publish service.

* **The Dispatcher** is a static web server augmented with the AEM dispatcher module. It caches web pages produced by the publish instance to improve performance.

The most common deployment pattern with AEM headless applications is to have the production version of the application connect to an AEM Publish service.

## Requirements and Configuration {#requirements-and-configuration}

1. Set up a [Local Runtime](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/aem-runtime.html#install-java) using the [AEM as a Cloud service SDK](/help/implementing/developing/introduction/aem-as-a-cloud-service-sdk.md)
2. Install the [WKND sample content](/help/implementing/developing/introduction/develop-wknd-tutorial.md) and subsequent GraphQL endpoints
3. Deploy and Configure a [static Node Server](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/graphql/production-deployment.html?lang=en#static-server).

## Secure and Scale your Headless Application Before Launch {#secure-and-scale-before-launch}

1. Configure [Token Based Authentication](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md)
2. Secure Webhooks
3. Configure Caching and Scalability

## Deploy to Production {#deploy-to-production}

Once you have tested all your code and content locally, you are now ready to commence a production deployment with AEM.

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

## Monitoring {#monitoring}

### How to Check Overall Performance {#check-overall-performance}

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

In order to make sure that your application is properly functioning before launch, it is recommended you follow these steps as an general approach to debugging:

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
