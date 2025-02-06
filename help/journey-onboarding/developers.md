---
title: Developer and Deployment Manager Tasks
description: Once they system administrator has set up the necessary cloud resources, learn how developers and deployment managers can access git to develop applications and use pipelines to deploy them.
feature: Onboarding
role: Admin, User, Developer
exl-id: f57a856b-0932-4e8f-be59-a19fe692e2ab
---

# Developer and Deployment Manager Tasks {#developer-deployment-manager}

In this optional part of the [onboarding journey](overview.md), you learn how developers and deployment managers can access git to develop applications and use pipelines to deploy them.

## The Story So Far {#story-so-far}

You have come a long way in your onboarding journey! Congratulations! The system administrator has completed the onboarding journey by setting up the necessary cloud resources and granting access in the document [Assigning AEM Product Profiles](assign-profiles-aem.md).

At this point your developers and deployment managers can begin creating your own applications while your AEM users can start creating content. In this sense, your onboarding is complete and now it is time to use your new AEM as a Cloud Service system, which this document will illustrate.

## Audience {#audience}

This document is therefore written from the perspective of the **developer** and **deployment manager**.

The system administrator can also perform these same tasks, but generally these roles are held by different users.

## Objective {#objective}

This document is a supplement to the onboarding journey to demonstrate the basic tasks of a developer and deployment manager once the system administrator has onboarded all the users and created the necessary cloud resources.

After reading this document, you should:

* As a developer, understand how to access and manage your Cloud Manager git repositories.
* As a deployment manager, be able set up pipelines and deploy your code in Cloud Manager.

## Developers and Deployment Managers {#roles}

Once the system administrator has completed the main onboarding tasks of creating users and setting up cloud resources, the users generally most anxious to access the system are the developers and deployment managers. This is because they are the users responsible for building your custom applications on top of AEM as a Cloud Service.

* **Developers** - These users access the Cloud Manager git repositories where they will manage the code for your AEM custom applications.
* **Deployment Managers** - These users use Cloud Manager to create and run pipelines that deploy the code from the git repositories to your running AEM environments.

Depending on your organizational needs, the same user(s) can have both roles.

## Prerequisites {#prerequisites}

Before you begin the tasks described in this document as a developer or deployment manager, ensure that your system administrator has completed all the steps in this onboarding journey. This means that:
 
* Your system administrator has assigned developers and deployment managers to their respective product profiles.
* Developers must additionally be assigned to **AEM Users** or **AEM Administrators** product profiles ito also use AEM.
* Cloud resources have been set up.

## Accessing git {#accessing-git}

You can access and manage your git repositories using self-service git account management from Cloud Manager.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to **Pipelines** card from your **Program Overview** page and find the **Access Repo Info** button to access and manage your git Repository.

   ![Access Repo Info button on Environments card](/help/implementing/cloud-manager/assets/repos/access-repo1.png)

1. Click the **View Repo Info** button to open a dialog to view:

   * The URL to the Cloud Manager git repository.
   * The git username.
   * The git password, the value of which is shown when the **Generate Password** button is clicked.

   ![Repository information](/help/implementing/cloud-manager/assets/repos/access-repo-create.png)

Using these credentials, the user can clone a local copy of the repository, and make changes in that local repository, and when ready can commit any code changes back to the remote code repository in Cloud Manager.

## Pipeline Setup {#setup-pipeline}

Once developers have added their custom code to your git repositories, the deployment manager can create and execute pipelines to deploy that code to your AEM environments.

Follow these steps to create your first non-production deployment pipeline.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Access the **Pipelines** card from the Cloud Manager home screen. Click **+Add** and select **Add Non-Production Pipeline**. 

   ![Add non-production pipeline](/help/implementing/cloud-manager/assets/configure-pipeline/nonprod-pipeline-add1.png)

1. On the **Configuration** tab of the **Add Non-Production Pipeline** dialog, select the type of non-production pipeline you with to add. For this example, select **Deployment Pipeline**.

   ![Add Non-Production pipeline dialog](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-pipeline-config.png)

1. Provide a **Non-Production Pipeline Name** to identify your pipeline along with the following additional information.

1. For the **Deployment Trigger** select **Manual** so that the pipeline runs only when you start it.

1. Click **Continue**.

1. On the **Source Code** tab of the **Add Non-Production Pipeline** dialog, you must select which type of code the pipeline should process. For this example, select **Full Stack Code**.

1. On the **Source Code** tab, you must define the following options.

   * **Eligible Deployment Environments** - You must choose which environment to which the pipeline should deploy.
   * **Repository** - This options defines from which git repo the pipeline should retrieve the code.
   * **Git Branch** - This option defines from which branch in the selected the pipeline should retrieve the code.
     * Enter the first few characters of the branch name and the auto-complete feature of this field will find the matching branches to help you select.

   ![Full-stack pipeline](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-pipeline-full-stack.png)

1. Click **Save**.

You have now created your first pipeline! Users with the deployment manager role can now start the pipeline from the Cloud Manager UI.

## Deploy {#deploy}

Now that developers have added their custom code to the git repositories and you have a pipeline created to deploy that code, it is time to execute the pipeline to actually move that code from git to your environment.

![Pipelines card in Cloud Manager](/help/implementing/cloud-manager/assets/configure-pipeline/pipelines-card.png)

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Pipelines** card from the **Program Overview** page and click the ellipsis button next to the pipeline you created in the previous section and select **Run** from the menu.

1. The pipeline run begins and is indicated by the **Status** column. 

You can see the details of the run by clicking the ellipsis button again and selecting **View details**.

Congratulations! You have now deployed code from your git repository to a non-production environment!

## What's Next {#whats-next}

Now that you have read this document you should:

* As a developer, understand how to access and manage your Cloud Manager git repositories.
* As a deployment manager, be able set up pipelines and deploy your code in Cloud Manager.

You have hit the ground running as a developer or deployment manager with not only working knowledge of Cloud Manager but also working environments, repositories, and pipelines! But there is more to learn about AEM as a Cloud Service's powerful CI/CD tools. Check out the [Additional Resources](#additional-resources) section for more details.

If you are interested in how content authors access and use AEM as a Cloud service, continue on to the final part of the onboarding journey, [AEM User Tasks](aem-users.md).

>[!TIP]
>
>Now that you are onboarded, you can [learn how to easily add the AEM Reference Demos Add-On](/help/journey-sites/demos-add-on/overview.md) to a sandbox environment with minimal AEM configuration and be able to test the powerful features of AEM with rich examples based on best-practices.

## Additional Resources {#additional-resources}

The following are additional, optional resources if you would like to go beyond the content of the onboarding journey.

* [Accessing Repositories](/help/implementing/cloud-manager/managing-code/accessing-repos.md) - Learn how to access and manage your git repository using the self-service git account management from Cloud Manager.
* [Using git with Cloud Manager](/help/implementing/cloud-manager/managing-code/integrating-with-git.md) - Learn how to use Cloud Manager's git repositories and how to integrate your own on-premise customer-managed git repository with Cloud Manager.
* [Local Development Environment Set up](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/overview.html) - This tutorial walks you through setting up a local development environment for Adobe Experience Manager (AEM) using the AEM as a Cloud Service SDK. 
* [Getting Started with AEM Sites - WKND Tutorial](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-wknd-tutorial-develop/overview.html) - This multi-part tutorial is designed for developers new to Adobe Experience Manager (AEM). This tutorial walks through the implementation of an AEM site for a fictitious lifestyle brand the WKND. The tutorial covers fundamental topics like project setup, Core Components, Editable Templates, Client-side libraries, and component development with Adobe Experience Manager Sites.
* [Getting Started with SPAs in AEM Using React](/help/implementing/developing/hybrid/getting-started-react.md) - This article presents a sample SPA application, explains how it is put together, and lets you get up-and-running with your own SPA quickly using the React framework.
* [Getting Started with SPAs in AEM Using Angular](/help/implementing/developing/hybrid/getting-started-angular.md) - This article presents a sample SPA application, explains how it is put together, and lets you get up-and-running with your own SPA quickly using the Angular framework.
* [Headless Developer Journey](/help/journey-headless/developer/overview.md) - Start here for a guided course for developing headless applications with AEM.
