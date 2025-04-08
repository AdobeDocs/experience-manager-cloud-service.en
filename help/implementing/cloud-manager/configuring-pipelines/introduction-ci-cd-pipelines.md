---
title: Introduction to CI/CD Pipelines
description: Learn about Cloud Manager's CI/CD pipelines and how they can be used to deploy your code efficiently.
index: yes
exl-id: 40d6778f-65e0-4612-bbe3-ece02905709b
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Cloud Manager CI/CD Pipelines {#intro-cicd}

Learn about Cloud Manager's CI/CD (Continuous Integration/Continuous Delivery) pipelines and how they can be used to deploy your code efficiently.

## Introduction to CI/CD Pipelines {#introduction}

A CI/CD pipeline in Cloud Manager is a mechanism to build code from a source repository and deploy it to an environment. An event triggers a pipeline, such as a pull request from a source code repository such as Git (that is, a code change). Or, it can be triggered on a regular schedule to match a release cadence.

To configure a pipeline, you must do the following:

* Define the trigger that starts the pipeline.
* Define the parameters that control the production deployment.
* Configure the performance test parameters.

Cloud Manager offers two types of pipelines:

* [Production pipelines](#prod-pipeline)
* [Non-production pipelines](#non-prod-pipeline)

![Types of pipelines](/help/implementing/cloud-manager/assets/configure-pipeline/ci-cd-config1.png)

## Production pipelines {#prod-pipeline}

A production pipeline is a purpose-built pipeline that includes a series of orchestrated steps to deploy source code for production use. The steps include first building, packaging, testing, validating, and deploying into all staging environments. Therefore, a production pipeline can only be added once a set of production and staging environments is created.

>[!TIP]
>
>See [Configure a production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md).

## Non-production pipelines {#non-prod-pipeline}

A non-production pipeline mainly serves to run code quality scans or to deploy source code to a development environment.

>[!TIP]
>
>See [Configure a non-production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md).

## Code sources {#code-sources}

Pipelines can also differ by the type of code they deploy, in addition to production and non-production environments.

* **[Full stack pipelines](#full-stack-pipeline)** - Simultaneously deploy back-end and front-end code builds containing one or more AEM server applications along with HTTPD/Dispatcher configurations.
* **[Config pipelines](#config-deployment-pipeline)** - You can quickly deploy configurations for features like log forwarding and purge-related maintenance tasks. It also includes various CDN (Content Delivery Network) configurations, such as traffic filter rules, including Web Application Firewall (WAF) rules. Additionally, you can manage request and response transformations, origin selectors, client-side redirects, error pages, CDN keys, purge API keys, and basic authentication. See [Use Config pipelines](/help/operations/config-pipeline.md) for details.
* **[Front-end pipelines](#front-end)** - Deploy front-end code builds containing one or more client-side user interface applications.
* **[Web tier Config pipelines](#web-tier-config-pipelines)** - Deploys HTTPD/Dispatcher configurations.

These pipeline types are described in detail later in this document. 

### Understand CI-CD pipelines in Cloud Manager {#understand-pipelines}

The following table summarizes the pipelines available in Cloud Manager and their usages.

| Pipeline Type | Deployment or Code quality | Source code | Purpose | Notes |
| --- | --- | --- | --- | ---|
| Production or non-production | Deployment | Full-Stack | Simultaneously deploys back-end and front-end code builds along with HTTPD/Dispatcher configurations | Used when front-end code must be deployed simultaneously with AEM server code. Used when the front-end pipelines or web tier configuration pipelines have not yet been adopted. |
| Production or non-production | Deployment | Front-end | Deploys front-end code build containing one or more client-side UI application | Supports multiple, concurrent front-end pipelines<br>Much faster than full-stack deployments. |
| Production or non-production | Deployment | Web tier Config | Deploys HTTPD/Dispatcher configurations | Deploys in minutes |
| Production or non-production | Deployment | Config | Deploys [configuration for a number of features](/help/operations/config-pipeline.md) related to CDN, log forwarding, and purge maintenance tasks | Deploys in minutes |
| Non-production | Code quality | Full stack | Runs code quality scans on full-stack code without a deployment | Supports multiple pipelines |
| Non-Production | Code quality | Front-end | Runs code quality scans on front-end code without a deployment | Supports multiple pipelines |
| Non-Production | Code quality | Web tier Config | Runs code quality scans on Dispatcher configurations without a deployment | Supports multiple pipelines |

The following diagram illustrates Cloud Manager's pipeline configurations with traditional, single front-end repository, or independent front-end repository setups.

![Cloud Manager pipeline configurations](/help/implementing/cloud-manager/assets/configure-pipeline/cm-setup.png)

## Full-stack pipelines {#full-stack-pipeline}

Full-stack pipelines deploy back-end code, front-end code, and web tier configurations to the AEM runtime all at the same time.

* Back-End Code - Immutable content such as Java code, OSGi configurations, repoinit, and mutable content
* Front-End Code - Application UI resources such as JavaScript, CSS, fonts
* Web Tier Config - HTTPD/Dispatcher configurations

The full-stack pipeline represents an 'uber' pipeline. It handles everything simultaneously, while also allowing users to deploy their front-end code or Dispatcher configurations separately. This deployment is through the front-end pipeline and the web tier config pipelines, respectively.

Full-stack pipelines package front-end code (JavaScript/CSS) as [AEM client libraries](/help/implementing/developing/introduction/clientlibs.md).

Full-stack pipelines may deploy web tier configurations if a [web tier config pipeline](#web-tier-config-pipelines) is not configured.

The following restrictions apply.

* A user must be logged with the **Deployment Manager** role to configure or run pipelines.
* At any time, there can only be one full-stack pipeline per environment.

In addition, be aware of how the full-stack pipeline behaves if you choose to introduce a [web tier config pipeline](#web-tier-config-pipelines).

* The full-stack pipeline for an environment ignores the Dispatcher configuration if the corresponding web tier config pipeline exists.  
* If the corresponding web tier config pipeline for the environment does not exist, the user can configure the full-stack pipeline include or ignore the Dispatcher configuration.

Full-stack pipelines can be code quality pipelines or deployment.

### Configure full-stack pipelines {#configure-full-stack}

See [Add a production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md#full-stack-code).
See [Add a non-production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#full-stack-code).

## Config pipelines {#config-deployment-pipeline}

Using a config pipeline, you can deploy settings quickly for log forwarding, purge-related maintenance tasks, and various CDN configurations, including traffic filter rules (such as WAF (Web Application Firewall) rules). Additionally, you can manage request and response transformations, origin selectors, client-side redirects, error pages, customer-managed CDN keys, purge API keys, and basic authentication.

See [Use config pipelines](/help/operations/config-pipeline.md) for a comprehensive list of supported features and to learn how to manage the configurations in your repository so they are deployed properly.

### Configure config Pipelines {#configure-config-deployment}

See [Add a production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md#targeted-deployment).
See [Add a non-production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#targeted-deployment).

## Front-end pipelines {#front-end}

Front-end code is any code that is served as a static files. It is separate from UI code served by AEM and may include site themes, customer-defined SPAs, SPAs, and other solutions. 

Front-end pipelines help your teams streamline your design and development process by enabling accelerated deployment of front-end code, asynchronous of back-end development. This dedicated pipeline deploys JavaScript and CSS to the AEM distribution layer as a theme, resulting in a new theme version, which may be referenced from pages delivered by AEM.

>[!NOTE]
>
>A user with the **Deployment Manager** role can create and run multiple front-end pipelines concurrently.
>
>There is, however, a maximum limit of 300 pipelines per program (across all types).

Front-end pipelines can be code quality pipelines or deployment pipelines.

### Before you configure front-end pipelines {#before-start}

Before you configure front-end pipelines, review the [AEM Quick Site Creation Journey](/help/journey-sites/quick-site/overview.md) for an end-to-end guide through the easy-to-use AEM Quick Site Creation tool. This journey helps you streamline your front-end development and lets you customize your site quickly with no back-end AEM knowledge.

### Configure a front-end pipeline {#configure-front-end}

See [Add a production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md#adding-production-pipeline).
See [Add a non-production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#adding-non-production-pipeline).

### Develop Sites with the front-end pipeline {#developing-with-front-end-pipeline}

With front-end pipelines, more independence is given to front-end developers and the development process can be accelerated.

See [Develop Sites with the front-end pipeline](/help/implementing/developing/introduction/developing-with-front-end-pipelines.md) for how this process works along with some considerations to be aware of to get the full potential out of this process.

## Web tier config pipelines {#web-tier-config-pipelines}

Web tier config pipelines allow exclusive deployment of HTTPD/Dispatcher configuration to the AEM runtime, decoupling it from other code changes. It is a streamlined pipeline that provides users who want to deploy only Dispatcher configuration changes, an accelerated means to do so in only a few minutes.

>[!TIP]
>
>Web tier config pipelines let you store your web config in the same or a different source location as the full stack pipeline, depending on what best suits your project structure.

The following restrictions apply.

* Be on AEM version `2021.12.6151.20211217T120950Z` or newer to use web-tier config pipelines.
* [Opt in to the flexible mode of the Dispatcher tools](/help/implementing/dispatcher/disp-overview.md#validation-debug) to use web-tier config pipelines.
* A user must be logged with the **Deployment Manager** role to configure or run pipelines.
* At any time, there can only be one web tier config pipeline per environment.
* The user cannot configure a web tier config pipeline when its corresponding full-stack pipeline is running.
* The web tier structure must adhere to the flexible mode structure, as defined in the document [Dispatcher in the Cloud](/help/implementing/dispatcher/disp-overview.md#validation-debug).

In addition, be aware of how the [full stack pipeline](#full-stack-pipeline) behaves when introducing a web tier pipeline.

* If a web tier config pipeline is not set up for an environment, the user can choose to include or ignore the Dispatcher configuration while configuring the full-stack pipeline. This selection is made during execution and deployment.
* Once a web tier config pipeline is configured for an environment, its corresponding full-stack pipeline (if one exists) ignores the Dispatcher configuration during execution and deployment.
* After a web tier config pipeline is deleted, its corresponding full-stack pipeline is reset to deploy Dispatcher configurations during its execution.

Web tier config pipelines can be of the type `Code quality` or `Deployment`.

### Configure Web tier pipelines {#configure-web-tier}

See [Add a production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md#targeted-deployment).
See [Add a non-production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#targeted-deployment).

## Video overview of pipeline types {#video}

For a quick overview of pipeline types, view the following video (2 minutes, 26 seconds).

>[!VIDEO](https://video.tv.adobe.com/v/342363)
