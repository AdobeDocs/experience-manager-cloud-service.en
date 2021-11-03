---
title: Configuring a Non-Production Pipelines
description: Follow this page to learn about Configuring a Non-Production Pipeline in Cloud Manager
index: no
---

# Configuring a Non-Production Pipelines {#configure-non-production-pipeline}

In addition to the main pipeline which deploys to stage and production, customers are able to set up additional pipelines, referred to as Non-Production Pipelines.

There are two types of Non-Production pipelines:

1. Code Quality: Runs code quality scans on the code in the a git branch. This pipeline executes the build and code quality steps.
1. Deployment: In addition to executing the build and code quality steps, this pipeline deploys the code to the selected non-production to AEM as a Cloud Service environment.

## Adding a New Non-Production Pipeline {#adding-non-production-pipeline}

On the home screen, these pipelines are listed in a new card:

1. Access the **Pipelines** card from the Cloud Manager home screen. Click on **+Add** and select **Add Non-Production Pipeline**. 

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/nonprod-pipeline-add1.png)

1. **Add Non-Production Pipeline**  dialog box displays. Select the type of pipeline you want to create, either **Code Quality Pipeline** or **Deployment Pipeline**.

   >[!NOTE]
   >For Deployment pipelines, you must select the deployment environment.

   Additionally, you can also set up **Deployment Trigger** and **Important Metric Failures Behavior** from **Deployment Options**. Click on **Continue**.

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/nonprod-pipeline-add2.png)

1. Select **Full Stack Code** or **Front End Code**. You can choose the **Repository** and the **Git Branch**. Click on **Save**.

   >[!NOTE]
   >Before you start configuring the Front End pipelines, see AEM Quick Site Creation Journey for an end to end workflow through the easy-to-use AEM Quick Site Creation tool. This documentation site will help you streamline the front-end development of your AEM Site and quickly customize your site with no AEM backend knowledge.

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/nonprod-pipeline-add3.png)

1. The newly created non-production pipeline now displays in the **Pipelines** card.

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/nonprod-pipeline-add4.png)


   The pipeline is shown on the card on the home screen with three actions, as shown below:
   
   * **Add** - allows adding of a new pipeline.
   * **Access Repo Info** - allows the user to get the information necessary to access Cloud Manager Git repository.
   * **Learn More** - navigates to understanding the CI/CD pipeline documentation resource. 