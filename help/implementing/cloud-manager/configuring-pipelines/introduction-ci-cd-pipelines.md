---
title: CI/CD Pipelines
description: Learn about Cloud Manager's CI/CD pipelines and how they can be used to efficiently deploy your code.
index: yes
exl-id: 40d6778f-65e0-4612-bbe3-ece02905709b
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Cloud Manager CI/CD Pipelines {#intro-cicd}

Learn about Cloud Manager's CI/CD pipelines and how they can be used to efficiently deploy your code.

## Introduction {#introduction}

A CI/CD pipeline in Cloud Manager is a mechanism to build code from a source repository and deploy it to an environment. A pipeline can be triggered by an event, such as a pull request from a source code repository (that is, a code change), or on a regular schedule to match a release cadence.

To configure a pipeline, you must:

* Define the trigger that will start the pipeline.
* Define the parameters controlling the production deployment.
* Configure the performance test parameters.

Cloud Manager offers two types of pipelines:

* [Production Pipelines](#prod-pipeline)
* [Non-Production Pipelines](#non-prod-pipeline)

![Types of pipelines](/help/implementing/cloud-manager/assets/configure-pipeline/ci-cd-config1.png)

## Production Pipelines {#prod-pipeline}

A production pipeline is a purpose-built pipeline that includes a series of orchestrated steps to deploy source code for production use. The steps include first building, packaging, testing, validating, and deploying into all staging environments. Therefore a production pipeline can only be added once a set of production and staging environments is created.

>[!TIP]
>
>See [Configuring a Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md) for more details.

## Non-Production Pipeline {#non-prod-pipeline}

A non-production pipeline mainly serves to run code quality scans or to deploy source code to a development environment.

>[!TIP]
>
>See [Configuring a Non-Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md) for more details.

## Code Sources {#code-sources}

In addition to production and non-production, pipelines can be differentiated by the type of code they deploy.

* **[Full Stack Pipelines](#full-stack-pipeline)** - Simultaneously deploy back-end and front-end code builds containing one or more AEM server applications along with HTTPD/Dispatcher configurations
* **[Config Pipelines](#config-deployment-pipeline)** - Quickly deploy configurations for features such as log forwarding, purge-related maintenance tasks, and various CDN configurations such as traffic filter rules (including WAF rules), request and response transformations, origin selectors, client-side redirects, error pages, customer-managed CDN keys, purge API keys, and basic auth.
  * Please see the document [Using Config Pipelines](help/operations/config-pipeline.md) for details.
* **[Front-End Pipelines](#front-end)** - Deploy front-end code builds containing one or more client-side UI applications 
* **[Web Tier Config Pipelines](#web-tier-config-pipelines)** - Deploys HTTPD/Dispatcher configurations

These are described in detail later in this document. 

### Understanding CI-CD Pipelines in Cloud Manager {#understand-pipelines}

The following table summarizes the pipelines available in Cloud Manager and their usages.

|Pipeline Type|Deployment or Code Quality|Source Code|Purpose|Notes|
|--- |--- |--- |---|---|
|Production or Non-Production|Deployment|Full-Stack|Simultaneously deploys back-end and front-end code builds along with HTTPD/Dispatcher configurations|When front-end code must be deployed simultaneously with AEM server code.<br>When front-end pipelines or web tier config pipelines have not yet been adopted.|
|Production or Non-Production|Deployment|Front-End|Deploys front-end code build containing one or more client-side UI application|Supports multiple, concurrent front-end pipelines<br>Much faster than full-stack deployments|
|Production or Non-Production|Deployment|Web Tier Config|Deploys HTTPD/Dispatcher configurations|Deploys in minutes|
|Production or Non-Production|Deployment|Config|Deploys [configuration for a number of features](/help/operations/config-pipeline.md) related to CDN, log forwarding, and purge maintenance tasks |Deploys in minutes|
|Non-Production|Code Quality|Full-Stack|Runs code quality scans on full-stack code without a deployment|Supports multiple pipelines|
|Non-Production|Code Quality|Front-End|Runs code quality scans on front-end code without a deployment|Supports multiple pipelines|
|Non-Production|Code Quality|Web Tier Config|Runs code quality scans on dispatcher configurations without a deployment|Supports multiple pipelines|

The following diagram illustrates Cloud Manager's pipeline configurations with traditional, single front-end repository, or independent front-end repository setups.

![Cloud Manager pipeline configurations](/help/implementing/cloud-manager/assets/configure-pipeline/cm-setup.png)

## Full-Stack Pipelines {#full-stack-pipeline}

Full-stack pipelines deploy back-end code, front-end code, and web tier configurations to AEM runtime all at the same time.

* Back-End Code - Immutable content such as Java code, OSGi configurations, repoinit, and mutable content
* Front-End Code - Application UI resources such as JavaScript, CSS, fonts
* Web Tier Config - HTTPD/Dispatcher configurations

The full-stack pipeline represents an 'uber' pipeline, doing everything at once, while giving users the options to exclusively deploy their front-end code or Dispatcher configurations via the front-end pipeline and the web tier config pipelines respectively.

Full-stack pipelines package front-end code (JavaScript/CSS) as [AEM client libraries](/help/implementing/developing/introduction/clientlibs.md).

Full-stack pipelines may deploy web tier configurations if a [web tier config pipeline](#web-tier-config-pipelines) is not configured.

The following restrictions apply.

* A user must be logged with the **Deployment Manager** role to configure or run pipelines.
* At any time, there can only be one full-stack pipeline per environment.

In addition, be aware of how the full-stack pipeline behaves if you choose to introduce a [web tier config pipeline.](#web-tier-config-pipelines)

* The full-stack pipeline for an environment will ignore the Dispatcher configuration if the corresponding web tier config pipeline exists.  
* If the corresponding web tier config pipeline for the environment does not exist, the user can configure the full-stack pipeline include or ignore the Dispatcher configuration.

Full-stack pipelines can be code quality pipelines or deployment.

### Configuring Full-Stack Pipelines {#configure-full-stack}

To learn how to configure full-stack pipelines, see the following documents:

* [Adding a Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md#full-stack-code)
* [Adding a Non-Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#full-stack-code)

## Config Pipelines {#config-deployment-pipeline}

With a config pipeline you can quickly deploy configurations for log forwarding, purge-related maintenance tasks, and various CDN configurations such as traffic filter rules (including WAF rules), request and response transformations, origin selectors, client-side redirects, error pages, customer-managed CDN keys, purge API keys, and basic auth.

Please see the document [Using Config Pipelines](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md) for a comprehensive list of supported features and to  learn how to manage the configurations in your repository so they are deployed properly.

### Configuring Config Pipelines {#configure-config-deployment}

To learn how to configure config pipelines, see the following documents:

* [Adding a Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md#targeted-deployment)
* [Adding a Non-Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#targeted-deployment)

## Front-End Pipelines {#front-end}

Front-end code is any code that is served as a static files. It is separate from UI code served by AEM and may include site themes, customer-defined SPAs, SPAs, and other solutions. 

Front-end pipelines help your teams streamline your design and development process by enabling accelerated deployment of front-end code asynchronous of back-end development. This dedicated pipeline deploys JavaScript and CSS to the AEM distribution layer as a theme, resulting in a new theme version which may be referenced from pages delivered by AEM.

>[!NOTE]
>
>A user with the **Deployment Manager** role can create and run multiple front-end pipelines concurrently.
>
>There is, however, a maximum limit of 300 pipelines per program (across all types).

Front-end pipelines can be code quality pipelines or deployment pipelines.

### Before you Configure Front-End Pipelines {#before-start}

Before you configure front-end pipelines, review the [AEM Quick Site Creation Journey](/help/journey-sites/quick-site/overview.md) for an end-to-end guide through the easy-to-use AEM Quick Site Creation tool. This journey will help you streamline your front-end development and allow you to quickly customize your site with no back-end AEM knowledge.

### Configure a Front-End Pipeline {#configure-front-end}

To learn how to configure front-end pipelines, see the following:

* [Adding a Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md#adding-production-pipeline)
* [Adding a Non-Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#adding-non-production-pipeline)

### Developing Sites with the Front-End Pipeline {#developing-with-front-end-pipeline}

With front-end pipelines, more independence is given to front-end developers and the development process can be accelerated.

See [Developing Sites with the Front-End Pipeline](/help/implementing/developing/introduction/developing-with-front-end-pipelines.md) for how this process works along with some considerations to be aware of to get the full potential out of this process.

## Web Tier Config Pipelines {#web-tier-config-pipelines}

Web tier config pipelines enable exclusive deployment of HTTPD/Dispatcher configuration to the AEM runtime by decoupling it from other code changes. It a streamlined pipeline that provides users who want to only deploy dispatcher configuration changes, an accelerated means to do so in only a few minutes.

>[!TIP]
>
>With web tier config pipelines, you can choose between storing your web config in the same source location as for the full stack pipeline or in a different location, depending which structure better suits your project.

The following restrictions apply.

* You must be on AEM version `2021.12.6151.20211217T120950Z` or newer to use web-tier config pipelines.
* You must [opt in to the flexible mode of the dispatcher tools](/help/implementing/dispatcher/disp-overview.md#validation-debug) to use web-tier config pipelines.
* A user must be logged with the **Deployment Manager** role to configure or run pipelines.
* At any time, there can only be one web tier config pipeline per environment.
* The user cannot configure a web tier config pipeline when its corresponding full-stack pipeline is running.
* The web tier structure must adhere to the flexible mode structure, as defined in the document [Dispatcher in the Cloud](/help/implementing/dispatcher/disp-overview.md#validation-debug).

In addition, be aware of how the [full stack pipeline](#full-stack-pipeline) behaves when introducing a web tier pipeline.

* If a web tier config pipeline has not been configured for an environment, the user can make a selection while configuring its corresponding full-stack pipeline to include or ignore the Dispatcher configuration during execution and deployment.
* Once a web tier config pipeline has been configured for an environment, its corresponding full-stack pipeline (if one exists) will ignore the dispatcher configuration during execution and deployment.
* After a web tier config pipeline is deleted, its corresponding full-stack pipeline is reset to deploy Dispatcher configurations during its execution.

Web tier config pipelines can be of the type code quality or deployment.

### Configuring Web Tier Pipelines {#configure-web-tier}

To learn how to configure web tier pipelines, see the following documents:

* [Adding a Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md#targeted-deployment)
* [Adding a Non-Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#targeted-deployment)

## Video Overview of Pipeline Types {#video}

For a quick overview of pipeline types, view this short video.

>[!VIDEO](https://video.tv.adobe.com/v/342363)
