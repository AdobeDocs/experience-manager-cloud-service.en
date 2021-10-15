---
title: Deploy Your Customized Theme
description: Learn how to deploy the theme using the pipeline.
index: no
hide: yes
hidefromtoc: yes
---

# Deploy Your Customized Theme {#deploy-your-customized-theme}

Learn how to deploy the theme using the pipeline.

>[!CAUTION]
>
>The Quick Site Creation tool is currently a tech preview. It is made available for testing and evaluation purposes and is not intended for production use unless agreed with Adobe Support.

## The Story So Far {#story-so-far}

In the previous document of the AEM Quick Site Creation journey, [Customize the Site Theme,](customize-theme.md) you learned how the theme is built, how to customize it, and how to test it using live AEM content, and you should now:

* Understand the basic structure of the site theme and how to edit it.
* See how to test your theme customizations using real AEM content via local proxy.
* Know how to commit your changes to the AEM git repository.

Now that your front end developer has committed the theme customizations to your AEM git repository, you an take the final step and use the pipeline to deploy them.

## Objective {#objective}

This document explains how to deploy the theme using the pipeline. After reading you should:

* Know how you can trigger a pipeline deployment.
* See how to check the deployment status.
* View the results of the deployment in your AEM environment.

## End of the Journey? {#end-of-journey}

Congratulations! You have completed the AEM Quick Site Creation journey! You should now:

* Understand how Cloud Manager and the front end pipeline work to manage and deploy front end customizations.
* Know how to create an AEM site based on a template and how to provide the theme and credentials to a front end developer.
* How to customize and test a theme using proxied AEM content and commit those changes to AEM git.
* How to deploy front end customization using the pipeline.

You are now ready to customize the themes of your own AEM site. However AEM is a powerful tool and there are many additional options available. Check out some of the additional resources available in the [Additional Resources section](#additional-resources) to learn more about the features you saw in this journey.

## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the Quick Site Creation journey by reviewing the document [Deploy Your Customized Theme,](deploy-theme.md) the following are some additional, optional resources that do a deeper dive on some concepts mentioned in this document, but they are not required to continue on the journey.

* [AEM as a Cloud Service technical documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service.html) - If you already have a firm understanding of AEM and headless technologies, you may want to directly consult our in-depth technical docs.
* [Cloud Manager documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/cloud-manager-introduction.html) - If you would like more details on Cloud Manager's features, you may want to directly consult our in-depth technical docs.
* [AEM Standard Site Template](https://github.com/adobe/aem-site-template-standard) - This is the GitHub repository of the AEM Standard Site template.
* [npm](https://www.npmjs.com) - AEM themes used to quickly build sites are based on npm.
* [webpack](https://webpack.js.org) - AEM themes used to quickly build sites rely on webpack.
* [Creating and Organizing Pages](/help/sites-cloud/authoring/fundamentals/organizing-pages.md) - This guide details how to manage pages of your AEM Site if you wish to customize it further after creating it from the template.
