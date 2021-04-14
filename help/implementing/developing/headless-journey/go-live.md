---
title: How to Go Live with Your Headless Application
description: In this part of the AEM Headless Developer Journey, learn how to deploy a headless application live by taking your local code in Git and moving it to Cloud Manager Git for the CI/CD pipeline.
---

# How to Go Live with Your Headless Application {#go-live}

In this part of the [AEM Headless Developer Journey,](#overview.md) learn how to deploy a headless application live by taking your local code in Git and moving it to Cloud Manager Git for the CI/CD pipeline.

## Content Replication and Caching Basics {#content-replication-and-caching}

A full AEM environment is made up of an Author, Publish, and Dispatcher. 

* **The Author service** is where internal users create, manage, and preview content. 

* **The Publish service** is considered the “Live” environment and is typically what end users interact with. Content, after being edited and approved on the Author service, is distributed to the Publish service.

* **The Dispatcher** is a static web server augmented with the AEM dispatcher module. It caches web pages produced by the publish instance to improve performance.

The most common deployment pattern with AEM headless applications is to have the production version of the application connect to an AEM Publish service.

## Requirements and Configuration {#requirements-and-configuration}

1. Install SDK in Publish Mode
2. Install sample content and GprahQL endpoints
3. Deploy and Configure a static Node Server.

## Secure and Scale your Headless Application Before Launch {#secure-and-scale-before-launch}

1. Configure [Token Based Authentication](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md)
2. Secure Webhooks
3. Configure Caching and Scalability

## Deploy to Production {#deploy-to-production}

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
    *  Fastly – check number of calls, cache rate, error rates, payload traffic 
    * Origin servers - number of calls, error rates, CPU loads, payload traffic 
  * Author Performance
    * Check number of users, requests and load
* Access App and Space specific performance reports
  * Once the server is up, check whether the general metrics are green/orange/red, then identify specific app issues
  * Open same reports above filtered to app/space (I.e. Photoshop desktop, paywall, etc.) 
  * Use Splunk log APIs to access service and application performance
  * Contact Customer Support in case there are other issues.

## Common Issues and Troubleshooting {#common-issues-and-troubleshooting}

## Additional Resources {#additional-resources}

