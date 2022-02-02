---
title: CI-CD Pipelines
description: Learn about Cloud Manager's CI-CD pipelines and how they can be used to efficiently deploy your code.
index: yes
---

# Cloud Manager CI-CD Pipelines {#intro-cicd}

Learn about Cloud Manager's CI-CD pipelines and how they can be used to efficiently deploy your code.

## Introduction {#introduction}

A CI/CD pipeline in Cloud Manager can be triggered by an event, such as a pull request from a source code repository (i.e. a code change), or on a regular schedule to match a release cadence.

To configure your pipeline, you must:

* Define the trigger that will start the pipeline.
* Define the parameters controlling the production deployment.
* Configure the performance test parameters.

Cloud Manager offers two types of pipelines:

* [Production Pipelines](#prod-pipeline)
* [Non-Production Pipelines](#non-prod-pipeline)

![Types of pipelines](/help/implementing/cloud-manager/assets/configure-pipeline/ci-cd-config1.png)

## Production Pipelines {#prod-pipeline}

A production pipeline is a purpose-built pipeline that includes a series of orchestrated steps to bring source code to production. The steps include first building, packaging, testing, validating, and deploying into all staging environments. A production pipeline can only be added once a set of production and staging environments is created.

>[!TIP]
>
>Refer to the document [Configuring a Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md) for more details.

## Non-Production Pipeline {#non-prod-pipeline}

A non-production pipeline mainly serves to run code quality scans or to deploy source code to a development environment.

>[!TIP]
>
>Refer to the document [Configuring a Non-Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md) for more details.

## Understanding CI-CD Pipelines in Cloud Manager {#understand-pipelines}

The following table summarizes all the pipelines in Cloud Manager.

|Pipeline Type|Deployment or Code Quality|Source Code|What it Does|Usage|
|--- |--- |--- |---|---|
|Production or Non-Production|Deployment|Front-End|Pushes the build to a storage location. When a page is served it may reference front-end static files which will be served by the CDN using this location as an origin.<br>Multiple front-end pipelines can be configured and run concurrently per environment, offering fast deployment times.|To exclusively deploy front-end code containing one or more client-side UI applications.<br>Front-end code is any code that is served as a static file. It is separate from UI code served by AEM. It includes site themes, customer-defined SPAs, Firefly SPAs, and other solutions.|
|Production or Non-Production|Deployment|Full-Stack|Deploys AEM server code (immutable content, Java code, OSGi configurations, HTTPD/Dispatcher configuration, repoinit, mutable content, fonts) containing one or more AEM server applications simultaneously|For cases where front-end code must be deployed at exactly the same time as AEM server code.<br>For use when front-end pipelines have not yet been adopted.|
|Non-Production|Code Quality|Front-End|Evaluates your build success and code quality with support for multiple pipelines without doing a deployment.|To run code quality scans on front-end code.|
|Non-Production|Code Quality|Full-Stack|Evaluates your build success and code with support for multiple pipelines quality without doing a deployment.|To run code quality scan on full-stack code.|

The following diagram illustrates Cloud Manager's pipeline configurations with traditional, single front-end repository, or independent front-end repository setups.

![Cloud Manager pipeline configurations](/help/implementing/cloud-manager/assets/configure-pipeline/cm-setup.png)

## Cloud Manager Front-End Pipelines {#front-end}

Front-end pipelines help your teams streamline your design and development process by enabling accelerated pipelines for deploying front-end code. This dedicated pipeline deploys JavaScript and CSS to the AEM distribution layer as a theme, resulting in a new theme version which may be referenced from pages delivered by AEM.

Front-end code is any code that is served as a static file. It is separate from UI code served by AEM. It includes site themes, customer-defined SPAs, Firefly SPAs, and other solutions. 

>[!IMPORTANT]
>
>You must be on AEM version `2021.10.5933.20211012T154732Z ` or higher with Sites enabled to leverage front-end pipelines.

>[!NOTE]
>
>A user with the **Deployment Manager** role can create and run multiple front-end pipelines concurrently.
>
>There is, however, a maximum limit of 300 pipelines per program (across all types). These can be  front-end code quality or front-end deployment pipelines.

### Before you Configure Front-End Pipelines {#before-start}

Before you configure front-end pipelines, please review the [AEM Quick Site Creation Journey](/help/journey-sites/quick-site/overview.md) for an end-to-end guide through the easy-to-use AEM Quick Site Creation tool. This journey will help you streamline your front-end development and allow you to quickly customize your site with no back-end AEM knowledge.

### Configure a Front-End Pipeline {#configure-front-end}

To learn how to configure front-end pipelines, please refer to the following documents.

* [Adding a Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md#adding-production-pipeline)
* [Adding a Non-Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#adding-non-production-pipeline)

### Developing Sites with the Front-End Pipeline {#developing-with-front-end-pipeline}

With front-end pipelines, more independence is given to front-end developers and the development process can be accelerated.

Please refer to the document [Developing Sites with the Front-End Pipeline](/help/implementing/developing/introduction/developing-with-front-end-pipelines.md) for how this process works along with some considerations to be aware of in order to get the full potential out of this process.

## Full-Stack Pipelines {#full-stack-pipeline}

Full-stack pipelines give the user the option to deploy back-end code, front-end code, and HTTPD/Dispatcher configurations all at the same time. It deploys code and content to AEM runtime including front-end code (JavaScript/CSS) packaged as [AEM client libraries.](/help/implementing/developing/introduction/clientlibs.md)

Full-stack pipelines may deploy web tier configurations if a web tier pipeline is not configured. The full-stack pipeline represents an 'uber' pipeline, doing everything at once, while giving users the options to exclusively deploy their front-end code or Dispatcher configurations via the front-end pipeline and the web tier config pipelines respectively.

Full-stack pipelines can be code quality pipelines or deployment pipeline.

The following restrictions apply.

1. A user must be logged with the **Deployment Manager** role in order to configure or run pipelines.
1. At any time, there can only be one full-stack pipeline per environment.
1. The full-stack pipeline for an environment will ignore the Dispatcher configuration if the corresponding web tier config pipeline exists.  
1. If the corresponding web tier config pipeline for the environment does not exist, the user can configure the full-stack pipeline include or ignore the Dispatcher configuration.

### Configuring Full-Stack Pipelines {#configure-full-stack}

To learn how to configure full-stack pipelines, please refer to the following documents.

* [Adding a Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md#adding-production-pipeline)
* [Adding a Non-Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#adding-non-production-pipeline)
