---
title: Customize the Site Theme
description: Learn how the site theme is built, how to customize, and how to test using live AEM content.
index: no
hide: yes
hidefromtoc: yes
---

# Customize the Site Theme {#customize-the-site-theme}

Learn how the site theme is built, how to customize, and how to test using live AEM content.

>[!CAUTION]
>
>The Quick Site Creation tool is currently a tech preview. It is made available for testing and evaluation purposes and is not intended for production use unless agreed with Adobe Support.

## The Story So Far {#story-so-far}

If you are a front end developer only responsible for the customization of the site theme, you do not need any knowledge of how AEM was set up and can skip to the [Objective](#objective) section of this document.

If you also serve the role of administrator as well as front end developer, you learned in the previous document of the AEM Quick Site Creation journey, [Create Site from Template,](create-site.md) how to quickly create a new AEM site using a template, and you should now:

* Understand how to obtain AEM Site templates.
* Learn how to create a new site using a template.
* See how to download the template from your new site to provide to the front end developer.

Now that you have a site created based on a template and have all of the information that a front end developer needs, this article shifts perspective exclusively to the front end developer role and shows the developer how to customize the theme.

## Objective {#objective}

This document explains how the AEM site theme is built, how to customize it, and how to test it using live AEM content. After reading you should:

* Understand the basic structure of the site theme and how to edit it.
* See how to test your theme customizations using real AEM content via local proxy.
* Know how to commit your changes to the AEM git repository.

## Requirements {#requirements}

The Quick Site Creation tool allows front end developers to work completely independently without and knowledge of AEM or how it is set up. However, there is information that you must be provided by the AEM administrator.

* Theme source files to customize
* Path to an example page to use as a base of reference
* Git credentials to commit your customizations
* Proxy user credentials to test your customizations against live AEM content
* Front end design requirements

If you are missing any of these items, please contact your AEM administrator.

It is assumed that the front end developer has extensive experience with front end development workflows as well as common tools installed including:

* git
* npm
* webpack
* Preferred editor

## Understand the Theme Structure {#understand-theme}

Extract the theme provided by the AEM administrator to where you would like to edit the theme and open it in your preferred editor.

![Editing the theme](assets/edit-theme.png)

You will see that the theme is a typical front end project. The most important parts of the structure are:

* `src/main.ts`: This is the main entry point of your JS & CSS theme.
* `src/site`: These are files that are generic to the entire site.
* `src/components`: These are files that are specific to components.
* `src/resources`: These are associated files like icons, logos, and fonts.

>[!TIP]
>
>If you would like to know more about the standard AEM site theme, see the GitHub link in the [Additional Resources](#additional-resources) section at the end of this document.

Once you are comfortable with the structure of the theme project, we will start the local proxy so you can see any theme customizations in real time based on actual AEM content.

## Starting the Local Proxy {#starting-proxy}

1. From the command line navigate to the root of the theme on your local machine.
1. Execute `npm install` and npm retrieves dependencies and installs the project.

   ![npm install](assets/npm-install.png)

1. Execute `npm run live` and the proxy server starts.

   ![npm run live](assets/npm-run-live.png)

1. When the proxy server starts it automatically opens a browser to `http://localhost:7001/`. Tap or click **SIGN IN LOCALLY (ADMIN TASKS ONLY)** and sign on with the proxy user credentials provided to you by the administrator.

   ![Sign in locally](assets/sign-in-locally.png)

1. Once signed in, change the URL in the browser to point to the path to the sample content that the administrator provided to you.

   * For example if the path provided was `/content/<your-site>/en/home.html?wcmmode=disabled`
   * You would change the URL to `http://localhost:7001/content/<your-site>/en/home.html?wcmmode=disabled`

   ![Proxied sample content](assets/proxied-sample-content.png)

You can navigate the site to explore the content. The site is pulled live from the live AEM instance so you can make your theme customizations against real content.

## Customize the Theme {#customize-theme}

Now you can start customizing the theme. Here we will walk through a simple example to illustrate how you can see your changes live via the proxy.

1. In your editor, open the file `<your-theme-sources>/src/site/_variables.scss`

   ![Edit theme](assets/edit-theme.png)

1. Edit the variable `$color-background` and set it to a value other than white. In this example, we used `orange`.

   ![Edited theme](assets/edited-theme.png)

1. As soon as you save the file, you will see that the proxy server recognizes the change via the line `[Browsersync] File event [change]`.

   ![Proxy browsersync](assets/proxy-browsersync.png)

1. Switching back to your browser of the proxy server, the change is immediately visible.

   ![Orange theme](assets/orange-theme.png)

You can continue customizing the theme based on the requirements provided to you by the administrator.

## Committing the Changes {#committing-changes}

Once your customizations are complete, you can commit them to the AEM git repository. First you must clone the repository to your local machine.

1. From the command line, navigate to where you would like to clone the repo.
1. Execute the command provided to you from the administrator. It should be similar to `git clone https://git.cloudmanager.adobe.com/<my-org>/<my-program>/`. Use the git user name and password provided by the administrator.

   ![Clone repo](assets/clone-repo.png)

1. Move the theme project that you were editing into the cloned repo with a command similar to `mv <site-theme-sources> <cloned-repo>`
1. In the directory of the cloned repo, commit the theme files that you just moved into with the following commands.

   ```text
   git add .
   git commit -m "Adding theme sources"
   git push
   ```

1. The customizations are pushed to the AEM repository.

   ![Changes committed](assets/changes-committed.png)

Your customizations are now safely stored in the AEM repository. Now you simply need to inform the administrator the the customizations are ready to deploy.

## What's Next {#what-is-next}

Now that you have completed this part of the AEM Quick Site Creation journey you should:

* Understand the basic structure of the site theme and how to edit it.
* See how to test your theme customizations using real AEM content via local proxy.
* Know how to commit your changes to the AEM git repository.

If you are only responsible for front end development, congratulations! You are finished! Just remember to tell the administrator that your customizations are now ready to deploy.

If you are an administrator as well as a front end developer, build on this knowledge and continue your AEM Quick Site Creation journey by next reviewing the document [Deploy Your Customized Theme,](deploy-theme.md) where you will learn how to deploy the theme using the front end pipeline.

## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the Quick Site Creation journey by reviewing the document [Deploy Your Customized Theme,](deploy-theme.md) the following are some additional, optional resources that do a deeper dive on some concepts mentioned in this document, but they are not required to continue on the journey.

* [AEM Site Theme](https://github.com/adobe/aem-site-template-standard-theme-e2e) - This is the GitHub repository of the AEM Site Theme.
* [npm](https://www.npmjs.com) - AEM themes used to quickly build sites are based on npm.
* [webpack](https://webpack.js.org) - AEM themes used to quickly build sites rely on webpack.