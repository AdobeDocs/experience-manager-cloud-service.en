---
title: Set Up Your Pipeline
description: Create a front-end pipeline to manage the customization of your site's theme.
---

# Set up Your Pipeline {#set-up-your-pipeline}

Create a front-end pipeline to manage the customization of your site's theme.

>[!CAUTION]
>
>The Quick Site Creation tool is currently a tech preview. It is made available for testing and evaluation purposes and is not intended for production use unless agreed with Adobe Support.

## The Story So Far {#story-so-far}

In the previous document of the AEM Quick Site Creation journey, [Create Site from Template,](create-site.md) you learned how to use a site template to quickly create an AEM site that can be further customized using front-end tools and now you should now:

* Understand how to obtain AEM Site templates.
* Learn how to create a new site using a template.
* See how to download the template from your new site to provide to the front-end developer.

This article builds on those fundamentals so you can set up a front-end pipeline, which the front-end developer will use later in the journey to deploy front-end customizations.

## Objective {#objective}

This document helps you understand front-end pipelines and how to create one to manage the deployment of your site's customized theme. After reading you should:

* Understand what a front-end pipeline is.
* Know how to set up a front-end pipeline in Cloud Manager.

## Responsible Role {#responsible-role}

This part of the journey applies to the Cloud Manager administrator.

## Requirements {#requirements}

* You need to have access to Cloud Manager.
* You need to be a member of the **Deployment Manager** role in Cloud Manager.

## What is a Front-End Pipeline {#front-end-pipeline}

Front-end development involves the customization of JavaScript, CSS, and static resources that define the styling of your AEM site. The front-end developer will work in their own local environments to make these customizations. Once they are ready, the changes are committed to the AEM git repository. But they are only committed to the source code. They are not yet live.

The front-end pipeline takes these committed customizations and deploys them to an AEM environment, generally production or non-production environments.

In this way, front-end development can work separately from and parallel to any full-stack back-end development on AEM, which has its own deployment pipelines.

>[!NOTE]
>
>The front-end pipelines can only deploy JavaScript, CSS, and static resources to style your AEM site. Site content such as pages or assets can not be deployed in a pipeline.

## Access Cloud Manager {#login}

1. Log into Adobe Experience Cloud at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/).

1. Once logged in ensure that you are in the correct organization by checking it in the top-right corner of the screen. If you are only member of one org, this step is not necessary. Then tap or click **Experience Manager**.

   ![Experience Cloud Overview](assets/experience-cloud-overview.png)

1. On the next page, tap or click the **Launch** to start the **Cloud Manager** app.

   ![Experience Manager apps](assets/experience-manager-apps.png)

1. The next page lists the various programs available. Tap or click the one you wish to manage. If you are just starting with AEM as a Cloud Service, you likely only have one program available.

   ![Selecting a program in Cloud Manager](assets/cloud-manager-select-program.png)

You now see an overview of your Cloud Manager. Your page will look different but similar to this example.

![Cloud Manager overview](assets/cloud-manager-overview.png)

Note the name of the program that you have accessed or copy the URL. You will need to provide this to the front-end developer later.

## Create a Front-End Pipeline {#create-front-end-pipeline}

Now that you have accessed Cloud Manager, you can create a pipeline for front-end deployment.

1. In the **Pipelines** section of the Cloud Manager page, tap or click the **Add** button.

   ![Pipelines](assets/pipelines-add.png)

1. In the pop-up menu that appears beneath the **Add** button select **Add Non-Production Pipeline** for the purposes of this journey.

1. On the **Configuration** tab of the **Add Non-Production Pipeline** dialog that opens:
   * Select **Deployment Pipeline**.
   * Provide the pipeline with a name in the **Non-Production Pipeline Name** field.

   ![Add pipeline configuration](assets/add-pipeline-configuration.png)

1. Tap or click **Continue**.

1. On the **Source Code** tab:
   * Select **Front End Code** as the type of code to deploy.
   * Make sure that the correct environment is selected under **Eligible Deployment Environments**.
   * Select the correct **Repository**.
   * Define which **Git Branch** the pipeline should be associated with.
   * Define the **Code Location** if the front-end development is located under a particular path in the selected repository. The default value is the root of the repository, but often front-end development and back end will be under different paths.

   ![Source code info for adding pipeline](assets/add-pipeline-source-code.png)

1. Tap or click **Save**.

The new pipeline is created and visible in the **Pipelines** section of the Cloud Manager window. Tapping of clicking the ellipsis after the pipeline name reveals options to further edit or view details as necessary.

![Pipeline options](assets/new-pipeline.png)

## What's Next {#what-is-next}

Now that you have completed this part of the AEM Quick Site Creation journey you should:

* Understand what a front-end pipeline is.
* Know how to set up a front-end pipeline in Cloud Manager.

Build on this knowledge and continue your AEM Quick Site Creation journey by next reviewing the document [Grant Access to the Front-End Developer,](grant-access.md) where you will onboard the front-end developers into Cloud Manager so they have access to your AEM site git repository and pipeline.

## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the Quick Site Creation journey by reviewing the document [Customize the Site Theme,](customize-theme.md) the following are some additional, optional resources that do a deeper dive on some concepts mentioned in this document, but they are not required to continue on the journey.

* [Cloud Manager documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/cloud-manager-introduction.html) - If you would like more details on Cloud Manager's features, you may want to directly consult the in-depth technical docs.
