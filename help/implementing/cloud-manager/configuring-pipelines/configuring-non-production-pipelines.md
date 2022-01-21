---
title: Configuring a Non-Production Pipelines
description: Follow this page to learn about Configuring a Non-Production Pipeline in Cloud Manager
index: yes
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

   You can define the following deployment triggers to start the pipeline.

    * **Manual** - using the UI manually start the pipeline.
    * **On Git Changes** - starts the CI/CD pipeline whenever there are commits added to the configured git branch. Even if you select this option, you can always start the pipeline manually.  

      During pipeline setup or edit, the Deployment Manager has the option of defining the behavior of the pipeline when an important failure is encountered in any of the quality gates.

       This is useful for customers who have the desire for more automated processes. The available options are:

    You can define the important failure metrics behavior to start the pipeline.

      * **Ask every time** - This is the default setting and requires manual intervention on any Important failure.
      * **Fail Immediately** - If selected, the pipeline will be cancelled whenever an Important failure occurs. This is essentially emulating a user manually rejecting each failure.
      * **Continue Immediately** - If selected, the pipeline will proceed automatically whenever an Important failure occurs. This is essentially emulating a user manually approving each failure.

1. Select **[Full Stack Code](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#full-stack-pipeline)** or **[Front End Code](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#front-end)**.

   If you selected **Front End Code**, you must select the **Repository**, **Git Branch** and **Code Location**, as shown in the figure below:

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-confignew1.png)

   If you selected **Full Stack Code**, you must select the **Repository** and **Git Branch**, as shown in the figure:
   ![](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-fullstack1.png)

   >[!IMPORTANT]
   >If a Full Stack Code pipeline already exists for the selected environment, this selection will be disabled.

   >[!NOTE]
   >Before you start configuring the Front End pipelines, see [AEM Quick Site Creation Journey](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/sites-journey/quick-site/overview.html) for an end to end workflow through the easy-to-use AEM Quick Site Creation tool. This documentation site will help you streamline the front-end development of your AEM Site and quickly customize your site with no AEM backend knowledge.

1. The newly created non-production pipeline now displays in the **Pipelines** card.

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/non-prod-fullstack2.png)


   The pipeline is shown on the card on the home screen with four actions, as shown below:
   
   * **Add** - allows adding of a new pipeline.
   * **Show All** - allows the user to view all the pipelines.
   * **Access Repo Info** - allows the user to get the information necessary to access Cloud Manager Git repository.
   * **Learn More** - navigates to understanding the CI/CD pipeline documentation resource. 