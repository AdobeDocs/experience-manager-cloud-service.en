---
title: Developing Sites with the Front-End Pipeline
description: With the front-end pipeline, more independence is given to front-end developers and the development process can gain substantial velocity. This document describes some particular considerations of the front-end build process that should be given.
exl-id: 996fb39d-1bb1-4dda-a418-77cdf8b307c5
feature: Developing
role: Admin, Architect, Developer
---

# Developing Sites with the Front-End Pipeline {#developing-site-with-front-end-pipeline}

[With the front-end pipeline](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#front-end), more independence is given to the front-end developers and the development process can gain substantial velocity. This document describes how this process works along with some considerations to be aware of so you can get the full potential out of this process.

>[!TIP]
>
>If you are not yet familiar with how to use the front-end pipeline and the benefits it can bring, check out the [Quick Site Creation Journey](/help/journey-sites/quick-site/overview.md) for an example of how to quickly deploy a new site and customize its theme completely independent of back-end development.

## Front-End Build Contract {#front-end-build-contract}

Similar to the [full-stack build environment](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md), the front-end pipeline has its own environment. Developers have some flexibility using this pipeline so long as the following front-end build contract is observed.

The front-end pipeline requires the front-end Node.js project to use the `build` script directive to generate the build that it deploys. This is because Cloud Manager uses the command `npm run build` to generate the deployable project for the front-end build.

The resulting content of the `dist` folder is what is ultimately deployed by Cloud Manager, serving them as static files. These files are hosted externally to AEM, but are made available via a `/content/...` URL on the deployed environment.

## Node Versions {#node-versions}

The front-end build environment supports the following Node.js versions.

* 12
* 14 (default)
* 16
* 18

You can use the `NODE_VERSION` [environment variable](/help/implementing/cloud-manager/environment-variables.md) to set the desired version.

## Single Source of Truth {#single-source-of-truth}

A general good practice is to maintain a single source of truth for what's deployed to AEM. Cloud Manager's objective is to make that single source of truth obvious. However, as the front-end pipeline allows decoupling the location for parts of the code, some additional responsibility lies in the correct setup of the front-end pipelines. Some care must be taken to not create multiple front-end pipelines that deploy to the same site on the same environment.

For this reason, and especially when several front-end pipelines are created, it is recommended to maintain a systematic naming convention such as the following:

* The name of the front-end module, defined by the `name` property of the `package.json` file, should contain the name of the site it applies to. For example, for a site located at `/content/wknd`, the name of the front-end module would be something like `wknd-theme`.
* When a front-end module shares the same Git repository with other modules, the name of its folder should be equal to, or contain that same name of, the front-end module. For example, if the front-end module is named `wknd-theme`, the enclosing folder name would be something like `wknd-theme-sources`.
* The name of the Cloud Manager front-end pipeline should also contain the name of the front-end module and also add the environment to which it deploys (production or development). For example, for the front-end module named `wknd-theme`, the pipeline could be named something like `wknd-theme-prod`.

Such a convention should efficiently prevent the following deployment mistakes:

* Applying a front-end module to the wrong site
* Creating multiple front-end modules that apply the same site, which would overwrite each other
* Creating multiple front-end pipelines for the same sources, which could cause race conditions, not guaranteeing the order of deployments

## Separation of Concerns {#separation-of-concerns}

Another good practice that applies to any separation of concerns is to put special care in how the contract that separates the concerns is designed and managed. In the case of the front-end pipeline, the contract separating that code from the rest is the HTML and JSON rendered by the site. If that HTML and JSON remains stable, then the front-end pipeline delivers its maximal value by making the front-end team fully independent.

There's currently no specific capability to run the full-stack pipeline synchronously with the front-end pipeline(s). For this reason, when decoupling the front-end development from the full-stack pipeline, extra care must be put into the contract that separates these two areas of concerns. That contract generally is the HTML and/or JSON that Experience Manager renders. Changes to that contract must therefore be well-planned between the teams operating the different pipelines so that they agree on how to sequence the corresponding changes.

The following steps are generally recommended when it's necessary to perform changes to the HTML and/or JSON output that impact both areas of concerns.

1. The back-end team first sets up a development environment with the new HTML and/or JSON output.
   1. Via the full-stack pipeline, they deploy the code required to render the new HTML and/or JSON output that is desired.
   1. If that's to an environment that the front-end team did not previously have access to, then the following steps must be performed.
      1. URL: The front-end team must know the URL of that development environment.
      1. ACL: The front-end team must be given a local AEM user with something similar to "Contributors" rights.
      1. Git: The front-end team must have a separate Git location for the front-end module that specifically targets that development environment.
         * A usual practice is to create a `dev` branch, so that the changes done for the development environment can then easily be merged back into the `main` branch that is to be deployed to the production environment.
      1. Pipeline: The front-end team must have a front-end pipeline that deploys to the development environment. That pipeline would deploy the front-end module that is typically located in the `dev` branch, as described in the previous point.
1. The front-end team then makes the CSS and JS code work with both the old and the new output.
   1. As usual, to develop locally:
      1. The `npx aem-site-theme-builder proxy` command executed within the front-end module starts a proxy server that requests the content from an AEM environment, while replacing the CSS and JS files of the front-end module with the ones from the local `dist` folder.
      1. Configuring the `AEM_URL` variable in the hidden `.env` file allows to control from which AEM environment the local proxy server consumes the content. 
      1. Changing the value of this `AEM_URL` therefore lets you switch between the production and development environments to adjust the CSS and JS so that it fits to both environments.
      1. It must work with the development environment that renders the new output and with the production environment that renders the old output.
   1. The front-end work is completed when the updated front-end module works for both environments, and is deployed to both.
1. The back-end team can then update the production environment by deploying the code that renders the new HTML and/or JSON output via the full-stack pipeline.
1. The front-end team can then clean up their CSS and JS and remove what was only needed by the old output, deploying that last update to production via the front-end pipeline.

## Additional Resources {#additional-resources}

* [Site Themes](/help/sites-cloud/administering/site-creation/site-themes.md) - Learn how AEM site themes can be used to customize the style and design of your site.
* [AEM Site Theme Builder](https://github.com/adobe/aem-site-theme-builder) - Adobe provides an AEM Site Theme Builder as a set of scripts for creating new site themes.
