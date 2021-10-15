---
title: Customize the Site Theme
description: Learn how the theme is built, how to customize, and how to test using live AEM content.
index: no
hide: yes
hidefromtoc: yes
---

# Customize the Site Theme {#customize-the-site-theme}

Learn how the theme is built, how to customize, and how to test using live AEM content.

>[!CAUTION]
>
>The Quick Site Creation tool is currently a tech preview. It is made available for testing and evaluation purposes and is not intended for production use unless agreed with Adobe Support.

## The Story So Far {#story-so-far}

In the previous document of the AEM Quick Site Creation journey, [Create Site from Template,](create-site.md) you learned how to quickly create a new AEM site using a template, and you should now:

* Understand how to obtain AEM Site templates.
* Learn how to create a new site using a template.
* See how to download the template from your new site to provide to the front end developer.

Now that you have a site created based on a template and provided the theme to your front end developer, this article shifts perspective exclusively to the front end developer role and shows the developer how to customize the theme.

## Objective {#objective}

This document explains how the theme is built, how to customize it, and how to test it using live AEM content. After reading you should:

* Understand the basic structure of the site theme and how to edit it.
* See how to test your theme customizations using real AEM content via local proxy.
* Know how to commit your changes to the AEM git repository.

## What's Next {#what-is-next}

Now that you have completed this part of the AEM Quick Site Creation journey you should:

* Understand the basic structure of the site theme and how to edit it.
* See how to test your theme customizations using real AEM content via local proxy.
* Know how to commit your changes to the AEM git repository.

Build on this knowledge and continue your AEM Quick Site Creation journey by next reviewing the document [Deploy Your Customized Theme,](deploy-theme.md) where you will learn how to deploy the theme using the front end pipeline.
## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the Quick Site Creation journey by reviewing the document [Deploy Your Customized Theme,](deploy-theme.md) the following are some additional, optional resources that do a deeper dive on some concepts mentioned in this document, but they are not required to continue on the journey.

* [AEM Standard Site Template](https://github.com/adobe/aem-site-template-standard) - This is the GitHub repository of the AEM Standard Site template.
* [npm](https://www.npmjs.com) - AEM themes used to quickly build sites are based on npm.
* [webpack](https://webpack.js.org) - AEM themes used to quickly build sites rely on webpack.