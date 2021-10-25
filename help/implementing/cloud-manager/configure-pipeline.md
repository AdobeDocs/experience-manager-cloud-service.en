---
title: Configure CI/CD Pipeline - Cloud Services
description: Configure CI/CD Pipeline - Cloud Services
exl-id: d2024b42-9042-46a0-879e-110b214c7285
---
# Configuring your CI-CD Pipeline {#configure-ci-cd-pipeline} 

In Cloud Manager, there are two types of Pipeline:

* **Production Pipeline**:
  
  A Production Pipeline can only be added once a production and stage environment set is created. 
  
  Refer to [Setting up Production Pipeline](configure-pipeline.md#setting-up-the-pipeline) for more details.

* **Non-Production Pipeline**:

  A Non-Production Pipeline can be added from the **Overview** page from the Cloud Manager's user interface. 
  
  Refer to [Non-Production & Code Quality Only Pipelines](configure-pipeline.md#non-production-pipelines) for more details.

   >[!NOTE]
   >To configure your pipeline, you must:
   > * define the trigger that will start the pipeline.
   > * define the parameters controlling the production deployment.
   > * configure the performance test parameters.

## Setting up Production Pipeline {#setting-up-production-pipeline}

The Deployment Manager is responsible for setting up the Production Pipeline.

>[!NOTE]
>A Production Pipeline cannot be setup until a program creation is complete, Git repository has at least one branch, and a Production and Stage environment set is created.

Before you start to deploy your code, you must configure your pipeline settings from the [!UICONTROL Cloud Manager].

>[!NOTE]
>
>You can change the pipeline settings after initial set up.

### Adding a New Production Pipeline {#adding-production-pipeline}

Once you have setup your program and have at least one environment using [!UICONTROL Cloud Manager] UI, you are ready to add a production pipeline.

Follow these steps to configure the behavior and preferences for your production pipeline:

1. Navigate to the **Pipelines** card from the **Program Overview** page.
Click on **+Add** and select **Add Production Pipeline**. 

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/add-prod-1.png)

1. **Add Production Pipeline** dialog box displays. Enter the pipeline name.

   Additionally, you can also set up **Deployment Trigger** and **Important Metric Failures Behavior** from **Deployment Options**. Click on **Continue**.

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/prod-pipeline-add2.png)


   You can define the deployment triggers to start the pipeline.

    * **Manual** - using the UI manually start the pipeline.
    * **On Git Changes** - starts the CI/CD pipeline whenever there are commits added to the configured git branch. Even if you select this option, you can always start the pipeline manually.  

      During pipeline setup or edit, the Deployment Manager has the option of defining the behavior of the pipeline when an important failure is encountered in any of the quality gates.

       This is useful for customers who have the desire for more automated processes. The available options are:

    You can define the important failure metrics behavior to start the pipeline.

      * **Ask every time** - This is the default setting and requires manual intervention on any Important failure.
      * **Fail Immediately** - If selected, the pipeline will be cancelled whenever an Important failure occurs. This is essentially emulating a user manually rejecting each failure.
      * **Continue Immediately** - If selected, the pipeline will proceed automatically whenever an Important failure occurs. This is essentially emulating a user manually approving each failure.

1. The **Add Production Pipeline** dialog box includes a second tab labeled as **Source Code**. **Full Stack Code** is selected. You can choose the **Repository** and the **Git Branch**. Select the Production Deployment Options, as explained below. Click on **Continue**.

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/prod-fullstack1.png)

   Production Deployment Options:

   * **Pause before Deploying to Production**: This option allows the deployment tp pause before production.
   * **Scheduled**: This option allows the user to enable the scheduled production deployment.

1. The **Add Production Pipeline** dialog box includes a third tab labeled as **Experience Audit**. This option provides a table for the URL paths that should always be included in the Experience Audit. 

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/add-prod-audit.png)

   >[!IMPORTANT]
   >You must click on **Add Page** to define your own custom link. Page path must start with `/`.
   >![](/help/implementing/cloud-manager/assets/configure-pipeline/add-prod-audit2.png)
 

   Click **Add New Page** to provide a URL path to be included in the Experience Audit.

   For instance, if you would like to include `https://wknd.site/us/en/about-us.html` in the Experience Audit, enter the path `/us/en/about-us.html` in this field and click **Save**.

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/add-prod-audit3.png)

   The URL that appears in the table will be:
   
   `https://publish-p12361-e112003.adobeaemcloud.com/us/en/about-us.html`

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/add-prod-audit4.png)

   A maximum of 25 rows can be included. If there are no pages submitted by the user in this section, the homepage of the site will be included in the Experience Audit by default.
 
   Refer to [Understanding Experience Audit Results](/help/implementing/cloud-manager/experience-audit-testing.md) for more details.

    >[!NOTE]
    > The pages that are configured will be submitted to the service and evaluated according to the performance, accessibility, SEO (Search Engine Optimization), best practice, and PWA (Progressive Web App) tests. 
    
1. Click on **Save**. The newly created production pipeline now displays in the **Pipelines** card.

   The pipeline is shown on the card on the home screen with three actions, as shown below:
   
   * **Add** - allows adding of a new pipeline.
   * **Access Repo Info** - allows the user to get the information necessary to access Cloud Manager Git repository.
   * **Learn More** - navigates to understanding the CI/CD pipeline documentation resource. 
 
### Editing a Production Pipeline {#editing-prod-pipeline}

You can edit the pipeline configurations from the **Program Overview** page. 

Follow the steps below to edit the configured pipeline:

1. Navigate to **Pipelines** card from the **Program Overview** page.

1. Click on **...** from the **Pipelines** card and click on **Edit**, as shown in the figure below.

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/pipeline-edit1.png)

1. The **Edit Production Pipeline** dialog box displays.

   1. The **Configuration** tab allows you to update the **Pipeline Name**, **Deployment Trigger**, and **Important Metrics Failure Behavior**.

      >[!NOTE]
      >See [Adding and Managing Repositories](/help/implementing/cloud-manager/managing-code/cloud-manager-repositories.md) to learn how to add and manage repositories in Cloud Manager.

      ![](/help/implementing/cloud-manager/assets/configure-pipeline/pipeline-edit2.png)


   1. The **Source** tab provides you an option to check or uncheck **Pause before deploying to Production** and **Scheduled** options from **Production Deployment Options**.

      ![](/help/implementing/cloud-manager/assets/configure-pipeline/prod-pipeline-editnotier.png)

   1. The **Experience Audit** option allows you to update or add new pages.

      ![](/help/implementing/cloud-manager/assets/configure-pipeline/pipeline-edit4.png)

1. Click on **Update** once you are done editing the pipeline.

### Additional Production Pipeline Actions {#additional-prod-actions}

#### Running a Production Pipeline {#run-prod}

You can run the production pipeline from the Pipelines card:

1. Navigate to **Pipelines** card from the **Program Overview** page.

1. Click on **...** from the **Pipelines** card and click on **Run**, as shown in the figure below.

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/prod-run.png)

#### Deleting a Production Pipeline {#delete-prod}

You can delete the production pipeline from the Pipelines card:

1. Navigate to **Pipelines** card from the **Program Overview** page.

1. Click on **...** from the **Pipelines** card and click on **Delete**, as shown in the figure below.

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/prod-delete.png)

   >[!NOTE]
   >A user in Deployment Manager role can now delete Production pipeline in a self-service manner via the **Delete** option from the Pipeline card.


## Non-Production & Code Quality Only Pipelines {#non-production-pipelines}

In addition to the main pipeline which deploys to stage and production, customers are able to set up additional pipelines, referred to as Non-Production Pipelines.
There are two types of non-production pipelines:

1. Code Quality: Runs code quality scans on the code in the a git branch. This pipeline executes the build and code quality steps.
1. Deployment: In addition to executing the build and code quality steps, this pipeline deploys the code to the selected non-production to AEM as a Cloud Service environment.

### Adding a New Non-Production Pipeline {#adding-non-production-pipeline}

On the home screen, these pipelines are listed in a new card:

1. Access the **Pipelines** card from the Cloud Manager home screen. Click on **+Add** and select **Add Non-Production Pipeline**. 

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/nonprod-pipeline-add1.png)

1. **Add Non-Production Pipeline**  dialog box displays. Select the type of pipeline you want to create, either **Code Quality Pipeline** or **Deployment Pipeline**.

   >[!NOTE]
   >For Deployment pipelines, you must select the deployment environment.

   Additionally, you can also set up **Deployment Trigger** and **Important Metric Failures Behavior** from **Deployment Options**. Click on **Continue**.

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/nonprod-pipeline-add2.png)

1. **Full Stack Code** is selected. You can choose the **Repository** and the **Git Branch**. Click on **Save**.

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/nonprod-pipeline-add3.png)

1. The newly created non-production pipeline now displays in the **Pipelines** card.

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/nonprod-pipeline-add4.png)


   The pipeline is shown on the card on the home screen with three actions, as shown below:
   
   * **Add** - allows adding of a new pipeline.
   * **Access Repo Info** - allows the user to get the information necessary to access Cloud Manager Git repository.
   * **Learn More** - navigates to understanding the CI/CD pipeline documentation resource. 

### Editing a Non-Production Pipeline {#editing-nonprod-pipeline}

You can edit the pipeline configurations from the **Pipelines card** from **Program Overview** page. 

Follow the steps below to edit the configured non-production pipeline:

1. Navigate to **Pipelines** card from the **Program Overview** page.

1. Select the non-production pipeline and click on **...**. Click on **Edit**, as shown in the figure below.

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/nonprod-pipeline-edit1.png)

1. The **Edit Production Pipeline** dialog box displays.

   1. The **Configuration** tab allows you to update the **Pipeline Name**, **Deployment Trigger**, and **Important Metric Failures Behavior**.

      >[!NOTE]
      >See [Adding and Managing Repositories](/help/implementing/cloud-manager/managing-code/cloud-manager-repositories.md) to learn how to add and manage repositories in Cloud Manager.

      ![](/help/implementing/cloud-manager/assets/configure-pipeline/nonprod-pipeline-edit2.png)


   1. The **Source Code** tab provides you update the **Repository** and the **Git Branch**.

      ![](/help/implementing/cloud-manager/assets/configure-pipeline/nonprod-pipeline-edit3.png)

1. Click on **Update** once you are done editing the non-production pipeline.

### Additional Non-Production Pipeline Actions {#additional-nonprod-actions}

#### Running a Non-Production Pipeline {#run-nonprod}

You can run the production pipeline from the Pipelines card:

1. Navigate to **Pipelines** card from the **Program Overview** page.

1. Click on **...** from the **Pipelines** card and click on **Run**, as shown in the figure below.

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/nonprod-run1.png)

#### Deleting a Non-Production Pipeline {#delete-nonprod}

You can delete the production pipeline from the Pipelines card:

1. Navigate to **Pipelines** card from the **Program Overview** page.

1. Click on **...** from the **Pipelines** card and click on **Delete**, as shown in the figure below.

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/nonprod-delete.png)


## The Next Steps {#the-next-steps}

Once you have configured the pipeline, you need to deploy your code.

Please see [Deploy your Code](deploy-code.md) for more details.
