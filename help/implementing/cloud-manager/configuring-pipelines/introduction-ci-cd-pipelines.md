---
title: CI-CD Pipelines
description: Follow this page to learn about Cloud Manager CI-CD Pipelines
index: yes
---

# Cloud Manager CI-CD Pipelines {#intro-cicd}

## Introduction {#introduction}

A CI/CD pipeline in Cloud Manager can be triggered by some sort of event, such as a pull request from a source code repository, that is, a code change, or some sort of regular schedule to match a release cadence.

>[!NOTE]
>To configure your pipeline, you must:
>* define the trigger that will start the pipeline
>* define the parameters controlling the production deployment
>* configure the performance test parameters

In Cloud Manager, there are two types of Pipelines:

* [Production Pipeline](#prod-pipeline)
* [Non-Production Pipeline](#non-prod-pipeline)

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/ci-cd-config1.png)


## Production Pipeline {#prod-pipeline}

A Production pipelines is a purpose built pipeline that includes a series of orchestrated steps to take source code all the way into production. The steps include building, packaging, testing, validating, and deploying into all Stage environment first. Needless to say, a Production Pipeline can only be added once a production and stage environment set is created.

Refer to [Configuring a Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md) for more details.


## Non-Production Pipeline {#non-prod-pipeline}

A Non-Production Pipeline aims to run code-quality scans or to deploy source code into a development environment. 

Refer to [Configuring a Non-Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md) for more details.

## Understanding CI-CD Pipelines in Cloud Manager {#understand-pipelines}

The following table summarizes all the pipelines in Cloud Manager along with their usage.

|Pipeline Type|Deployment or Code Quality|Source Code|When to Use|When or Why Should I use?|
|--- |--- |--- |---|---|
|Production or Non-Production|Deployment|Front End|Fast deployment times.<br>Multiple front-end pipelines can be configured and run concurrently per environment.<br>The Front End pipeline build pushes out of the build to a storage. When an html page is served it may reference Frontend Code static files which will be served by the CDN using this storage as an origin.|To exclusively deploy front end code containing one or more clientside UI applications. Front end code is any code that is served as a static file. It is separate from UI code served by AEM. It includes Sites Themes, Customer defined SPAs, Firefly SPAs and any other solutions.<br>Must be on AEM version 2021.10.5933.20211012T154732Z|

The following diagram illustrates Cloud Manager pipeline configurations with traditional, single front-end repository or independent front-end repository setup:

![](/help/implementing/cloud-manager/assets/configure-pipeline/cm-setup.png)

## Cloud Manager Front End Pipelines {#front-end}

Front End  pipelines help your teams streamline your design and development process, by enabling accelerated front end  pipelines for deploying front end code. This differentiated pipeline deploys JavaScript and CSS to the AEM distribution layer as a theme, resulting in a new theme version which may be referenced from pages delivered from the AEM runtime. Front end code is any code that is served as a static file. It is separate from UI code served by AEM. It includes Sites Themes, Customer defined SPAs, Firefly SPAs and any other solutions. 

>[!IMPORTANT]
>You must be on AEM version `2021.10.5933.20211012T154732Z ` to leverage front end pipelines.

>[!NOTE]
>A user logged in as Deployment Manager role can create and run multiple front end pipelines concurrently. There is, however, a maximum limit of 300 pipelines per program (across all types).

These can be of the type Front End Code Quality or Front End Deployment pipelines.

### Before you Configure Front End Pipelines {#before-start}

Before you start configuring the Front End pipelines, see [AEM Quick Site Creation Journey](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/sites-journey/quick-site/overview.html) for an end to end workflow through the easy-to-use AEM Quick Site Creation tool. This documentation site will help you streamline the front-end development of your AEM Site and quickly customize your site with no AEM backend knowledge.

### Configure a Front End Pipeline {#configure-front-end}

To learn how to configure Front End Pipeline, refer to:

* [Adding a Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md#adding-production-pipeline)
* [Adding a Non-Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#adding-non-production-pipeline)

## Full Stack Pipelines {#full-stack-pipeline}

Full Stack pipeline gives the user the option to deploy back-end, front-end and HTTPD/dispatcher configuration all at the same time.  It deploys code and content to the AEM runtime including front end code (JavaScript/CSS) packaged as AEM Client Libraries. It may deploy web tier configuration if a Web Tier pipeline is not configured. This represents the 'uber' pipeline, while giving users the options to exclusively deploy their Front End code or dispatcher configuration via the Front End pipeline and the Web Tier Config pipeline respectively.

The following restrictions will apply:

1. A user must be logged in as Deployment Manager in order to configure or run pipelines.

1. At any time, there can only be one Full Stack pipeline per environment.

1. The user can configure the Full Stack pipeline for an environment to ignore or not to ignore the dispatcher configuration, If the corresponding Web Tier Config pipeline for the environment does not exist. 

1. The Full Stack pipeline for an environment will ignore the dispatcher configuration if the corresponding Web Tier Config pipeline for the environment exists.  

These can be of the type Full Stack - Code Quality or Full Stack - Deployment pipeline.

### Configure a Full Stack Pipeline {#configure-full-stack}

To learn how to configure Full Stack Pipeline, refer to:

* [Adding a Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md#adding-production-pipeline))
* [Adding a Non-Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#adding-non-production-pipeline)