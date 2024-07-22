---
title: Configuration Pipeline
description: Learn about how the configuration pipeline works in AEM as a Cloud Service and how to configure it.
exl-id: ???
feature: Operations
role: Admin
---
# Configuration Pipeline in AEM as a Cloud Service {#configuration-pipeline-in-aem-as-a-cloud-service}

The Cloud Manager Configuration Pipeline deploys one or more configuration (yaml) files to a target environment.

Configuration Pipeline supports configuration of the following features:

**Content delivery related**
* Traffic Filter Rules, including WAF rules - the rules are configuraed
* Other Traffic Configuration, such as request and response transformations, client-side redirects, and origin selectors - the rules are configured
* CDN error pages - the location of where the error pages are hosted
* Purging the CDN - the Purge API Key is declared
* Customer-Managed CDN - the X-AEM-Edge-Key is declared 
* Basic authentication at the CDN (for early adopters) - the username and passwords are declared

**Repository optimizations related**
* Version Purge and Audit Log Purge Maintenance Tasks - the rules around purging

**Developer experience related**
* Log forwarding (not yet released) - destinations (e.g., Splunk, Datadog, HTTPS) and related credentials

This article describes concepts shared across either all or a subset of the features supported by configutation pipelines.

It should be pointed out that each feature has its own dedicated article or section of an article detailing its unique syntax; when appropriate, this shared article is referenced. 

## Common syntax

kind - defines the type

version

envTypes

## Creating and managing the Configuration Pipeline in Cloud Manager

## scoping to specific environments


## Using secret environment variable

## CDN Rules Common syntax

