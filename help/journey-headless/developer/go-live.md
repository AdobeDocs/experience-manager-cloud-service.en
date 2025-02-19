---
title: How to Go Live with Your Headless Application
description: In this part of the AEM Headless Developer Journey, learn how to deploy a headless application live by taking your local code in Git and moving it to Cloud Manager Git for the CI/CD pipeline.
exl-id: 81616e31-764b-44b0-94a6-3ae24ce56bf6
solution: Experience Manager
feature: Headless, Content Fragments,GraphQL API
role: Admin, Architect, Developer
---
# How to Go Live with Your Headless Application {#go-live}

In this part of the [AEM Headless Developer Journey](overview.md), learn how to deploy a headless application live by taking your local code in Git and moving it to Cloud Manager Git for the CI/CD pipeline.

## The Story So Far {#story-so-far}

In the previous document of the AEM headless journey, [How to Put It All Together - Your App and Your Content in AEM Headless](put-it-all-together.md) you learned how to use the AEM development tools to put all the facets of your project together.

This article builds on those fundamentals so you understand how to prepare your own AEM headless project to go live.

## Objective {#objective}

This document helps you understand the AEM headless publication pipeline and the performance considerations you must be aware of before you go live with your application.

* Secure and Scale your application before Launch
* Monitor Performance and Debug Issues

<!-- Alexandru: this is a bit redundant, to review again later

## Prepare your AEM Headless Application for Go-Live {#prepare-your-aem-headless-application-for-golive}

-->
To get your AEM headless application ready for launch, follow the best practices outlined below.

## Secure and Scale your Headless Application Before Launch {#secure-and-scale-before-launch}

1. Configure [Token Based Authentication](/help/headless/security/authentication.md) with your GraphQL requests
1. Configure [Caching](/help/implementing/dispatcher/caching.md).

## Model Structure vs GraphQL Output {#structure-vs-output}

* Avoid creating queries that output more than 15kb of JSON (gzip compressed). Long JSON files are resource intensive for client application to parse.
* Avoid more than five nested levels of fragment hierarchies. Additional levels make it hard for content authors to consider the impact of their changes.
* Use multi-object queries instead of modeling queries with dependency hierarchies within the models. This allows more long-term flexibility to restructure JSON output without having to do many content changes.

## Maximize CDN Cache-Hit Ratio {#maximize-cdn}

* Do not use direct GraphQL queries, unless you are requesting live content from the surface.
  * Use persisted queries whenever possible.
  * Provide CDN TTL above 600 seconds in order for the CDN to cache them.
  * AEM can calculate the impact of a model change to existing queries.
* Split JSON files/GraphQL queries between low and high content change rate so you can reduce client traffic to CDN and assign higher TTL. This minimizes the CDN revalidating the JSON with the origin server.
* To actively invalidate content from the CDN use Soft Purge. This allows the CDN to redownload the content without causing a cache miss.

## Improve Time to Download Headless Content {#improve-download-time}

* Make sure HTTP clients use HTTP/2.
* Make sure HTTP clients Accept Headers request for gzip.
* Minimize the number of domains used to host JSON and referenced artifacts.
* Leverage `Last-modified-since` to refresh resources.
* Use `_reference` output in JSON file to start downloading assets without having to parse complete JSON files.

## Deploy to Production {#deploy-to-production}

Once you make sure that everything has been tested and is working properly, you are ready to push your code updates to a [centralized Git repository in Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/managing-code/setup-cloud-manager-git-integration.html).

After the updates have been uploaded to Cloud Manager, they can be deployed to AEM as a Cloud Service using [Cloud Manager's CI/CD pipeline](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/how-to-use/deploying-code.html).

You can start deploying your code by using the Cloud Manager CI/CD pipeline, which is covered extensively under [Deploying Content Packages by way of Cloud Manager and Package Manager ](/help/implementing/deploying/overview.md).

## Performance Monitoring {#performance-monitoring}

For users to have the best possible experience when using the AEM headless application, it is important that you monitor key performance metrics, as detailed below:

* Validate preview and production versions of the app
* Verify AEM status pages for current service availability status
* Access performance reports
  * Delivery Performance
    * CDN (Fastly) performance – check number of calls, cache rate, error rates and payload traffic
    * Origin servers - number of calls, error rates, CPU loads, payload traffic
  * Author Performance
    * Check number of users, requests and load
* Access App and space specific performance reports
  * Once the server is up, check whether the general metrics are green/orange/red, then identify specific app issues
  * Open same reports above filtered to app or space (for example, Photoshop desktop, paywall)
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

To efficiently log a bug with Support in case you need further assistance, do the following:

* Take screenshots of the problem, if necessary
* Document a way to reproduce the issue
* Document the content the issue reproduces with
* Log an issue through the AEM Support portal with the appropriate priority

## The Journey Ends - Or Does It? {#journey-ends}

Congratulations! You have completed the AEM Headless Developer Journey! You should now have an understanding of:

* The difference between headless and headful content delivery.
* AEM's headless features.
* How to organize and AEM Headless project.
* How to create headless content in AEM.
* How to retrieve and update headless content in AEM.
* How to go live with an AEM Headless project.
* What to do after the go-live.

You have either already launched your first AEM Headless project or now have all the knowledge you need to do so. Great job!

### Explore Single Page Applications {#explore-spa}

The headless stores in AEM does not need to stop here, though. You might remember in the [Getting Started part of the journey](getting-started.md#integration-levels) we discussed briefly how AEM not only supports headless delivery and traditional full-stack models, but can also support hybrid models that combine the advantages of both.

If this kind of flexibility is something you need for your project, continue on to the optional, additional part of the journey, [How to Create Single Page Applications (SPAs) with AEM](create-spa.md).

## Additional Resources {#additional-resources}

* [Introduction to AEM as a Headless CMS](/help/headless/introduction.md)
* [AEM Developer Portal](https://experienceleague.adobe.com/landing/experience-manager/headless/developer.html)
* [Tutorials for Headless in AEM](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/overview.html) 
* [An Overview of Deploying to AEM as a Cloud Service](/help/implementing/deploying/overview.md)
* [Use Cloud Manager to Deploy Your Code](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/how-to-use/deploying-code.html)
* [Integrate the Cloud Manager Git Repository with an External Git Repository and Deploy a Project to AEM as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/devops/deploy-code.html)
