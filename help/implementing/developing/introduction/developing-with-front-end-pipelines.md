---
title: Develop Sites with the Front-End Pipeline
description: The front-end pipeline enhances developer independence and accelerates the development process. This article outlines key considerations for the front-end build process to ensure optimal performance and efficiency.
exl-id: 996fb39d-1bb1-4dda-a418-77cdf8b307c5
feature: Developing
role: Admin, Architect, Developer
---

# Develop Sites with the front-end pipeline {#developing-site-with-front-end-pipeline}

The [front-end pipeline](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#front-end) gives front-end developers greater independence and significantly accelerates development. This article explains how the process works and highlights key considerations to help you get the most out of it.

>[!TIP]
>
>If you are not yet familiar with how to use the front-end pipeline and its benefits, see the [Quick Site Creation Journey](/help/journey-sites/quick-site/overview.md) guide. It provides an example of how to deploy a new site quickly and customize its theme independently of back-end development.

## Understand the front-end pipeline setup and build process in AEM Cloud Manager {#front-end-build-contract}

Similar to the [full-stack build environment](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md), the front-end pipeline has its own environment. Developers have some flexibility with this pipeline, provided they follow the front-end build contract.

The front-end pipeline requires the front-end `Node.js` project to use the `build` script directive to generate the build that it deploys. This requirement exists because Cloud Manager uses the command `npm run build` to generate the deployable project for the front-end build.

The resulting content of the `dist` folder is what Cloud Manager ultimately deploys, serving them as static files. These files are hosted externally to AEM, but are made available by way of a `/content/...` URL on the deployed environment.

## Supported Node.js versions {#node-versions}

The front-end build environment supports the following `Node.js` versions:

* 23
* 22
* 20
* 18
* 16
* 14 (default)
* 12

You can use the `NODE_VERSION` [environment variable](/help/implementing/cloud-manager/environment-variables.md) to set the desired version.

## Best practices for naming and managing front-end pipelines in AEM {#single-source-of-truth}

A best practice for AEM deployments is to maintain a single, clear source of truth. Cloud Manager is designed to reinforce this principle. However, because the front-end pipeline allows parts of the code to be decoupled, proper setup is essential. To avoid conflicts, ensure that multiple front-end pipelines do not deploy to the same site within the same environment.

For this reason, and especially when several front-end pipelines are created, Adobe recommends that you maintain a systematic naming convention. You can use the following recommendations:

* The name of the front-end module, defined by the `name` property of the `package.json` file, should contain the name of the site it applies to. For example, for a site located at `/content/wknd`, the name of the front-end module would be something like `wknd-theme`.
* When a front-end module shares the same Git repository with other modules, the name of its folder should be equal to, or contain that same name of, the front-end module. For example, if the front-end module is named `wknd-theme`, the enclosing folder name would be something like `wknd-theme-sources`.
* The name of the Cloud Manager front-end pipeline should also contain the name of the front-end module and also add the environment to which it deploys (production or development). For example, for the front-end module named `wknd-theme`, the pipeline could be named something like `wknd-theme-prod`.

Such a convention prevents the following deployment mistakes:

* Applying a front-end module to the wrong site.
* Creating multiple front-end modules that apply the same site, which would overwrite each other.
* Creating multiple front-end pipelines for the same sources, which could cause race conditions, not guaranteeing the order of deployments.

## Coordinate front-end and back-end development for stability in AEM {#separation-of-concerns}

A key best practice for any separation of concerns is to design and manage the contract carefully that defines the boundaries between them. In the front-end pipeline, this contract is the HTML and JSON output rendered by the site. Maintaining the stability of this output ensures that the front-end pipeline delivers maximum value, allowing the front-end team to work independently.

There is currently no built-in capability to run the full-stack pipeline synchronously with the front-end pipelines. Therefore, when separating front-end development from the full-stack pipeline, it is crucial to manage the contract carefully that defines their boundaries. This contract typically consists of the HTML or JSON, or both, rendered by Experience Manager. Any changes to this contract should be carefully coordinated between teams managing different pipelines to ensure a smooth transition and proper sequencing of updates.

The following steps are generally recommended when making changes to the HTML or JSON output, especially when both areas are affected.

1. The back-end team first sets up a development environment with the new HTML or JSON output.
   1. By way of the full-stack pipeline, they deploy the code required to render the new HTML or JSON output, or both, that is desired.
   1. If that is to an environment that the front-end team did not previously have access to, then the following steps must be performed.
      1. URL: The front-end team must know the URL of that development environment.
      1. ACL: The front-end team must be given a local AEM user with something similar to "Contributors" rights.
      1. Git: The front-end team must have a separate Git location for the front-end module that specifically targets that development environment.
      
         A common practice is to create a `dev` branch to manage changes made in the development environment. This practice allows for an easier merge back into the `main` branch, which is used for deployment to the production environment.

      1. Pipeline: The front-end team must have a front-end pipeline that deploys to the development environment. That pipeline would deploy the front-end module that is typically located in the `dev` branch, as described in the previous point.
1. The front-end team then makes the CSS and JS code work with both the old and the new output.
   1. As usual, to develop locally, do the following:
      1. The `npx aem-site-theme-builder proxy` command starts a proxy server that retrieves content from an AEM environment. It replaces the front-end module's CSS and JS files with those files from the local `dist` folder.
      1. Configuring the `AEM_URL` variable in the hidden `.env` file lets you control from which AEM environment the local proxy server consumes the content. 
      1. Changing the value of `AEM_URL` therefore lets you switch between the production and development environments to adjust the CSS and JS so that it fits both environments.
      1. It must work with the development environment that renders the new output and with the production environment that renders the old output.
   1. The front-end work is completed when the updated front-end module works for both environments, and is deployed to both.
1. The back-end team can then update the production environment by deploying the code that renders the new HTML or JSON output, or both, by way of the full-stack pipeline.
1. The front-end team can clean up their CSS and JS, remove elements needed only for the old output, and deploy the final update to production using the front-end pipeline.

## Additional resources {#additional-resources}

* Learn how AEM site themes can be used to customize the style and design of your site.

   See [Site Themes](/help/sites-cloud/administering/site-creation/site-themes.md).

* Adobe provides an AEM Site Theme Builder as a set of scripts for creating new site themes.

   See [AEM Site Theme Builder](https://github.com/adobe/aem-site-theme-builder)



