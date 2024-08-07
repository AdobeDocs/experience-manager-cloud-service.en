---
title: Stage-Only and Prod-Only Pipelines
description: Learn how you can split staging and production only deployments using dedicated pipelines.
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer

---
# Stage-Only and Production-Only Deployment Pipelines {#stage-prod-only}

You now have the option to split Full Stack production deployment into two smaller, specialized CI/CD pipelines in Cloud Manager: one for staging and one for production.

>[!NOTE]
>
>This feature is only available to [the early adopter program](/help/implementing/cloud-manager/release-notes/current.md#early-adoption).

## Overview {#overview}

Currently, the Stage and Production environments are closely linked, with deployments managed through a single pipeline. While this setup has its advantages, it does have the following limitations:

* Deploying to Stage-only requires rejecting the **Promote to Prod** step, which results in the execution being marked as canceled.
* To promote the latest code version from Stage to Production, you must redeploy the entire pipeline, including the Stage deployment, even if no code changes have occurred.
* During Stage+Prod deployments, environments cannot be updated. If you want to pause and test on Stage for several days before promoting to Production, you cannot update the Production environment (for example, changing [environment variables](/help/implementing/cloud-manager/environment-variables.md)).

Stage-only and production-only deployment pipelines offer solutions to these use cases by providing dedicated deployment options.

* **Stage-only pipelines:**

    * Deploys to the Stage environment, with the execution completing after the deployment and tests are finished.
    * It behaves exactly like the current Full Stack Production Pipeline, but without the Production deployment steps (approval, schedule, deploy).

* **Prod-only pipelines:**

    * Deploy only to a production environment with the option to select an execution successfully finished and validated on stage and deploy its artifacts on prod.  
    * Prod-only pipelines reuse the artifacts from the stage deployments, skipping the building phase.

Stage-only and prod-only pipelines do not run while a full-stack production pipeline is in progress, and vice versa.

These dedicated pipelines offer more flexibility. However, you should note the following details of the operation and recommendations.

>[!NOTE]
>
>Prod-only pipelines consistently use artifacts from the stage-only pipeline. This workflow remains true regardless of any deployments made to stage by way of the standard coupled production pipeline in the interim.
>
>* This scenario may lead to unwanted code rollbacks.
>* Adobe recommends that you stop using the standard coupled production pipeline once you start using the prod-only and stage-only pipelines.
>* If you still decide to run both the standard coupled pipelines and stage-only/prod-only pipelines, keep in mind the reuse of artifacts to avoid code rollbacks.

## Create a pipeline {#pipeline-creation}

Prod-only and stage-only pipelines are created in a similar fashion to the standard coupled [production pipelines](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md) and [non-production pipelines](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md).

**To create a pipeline:**

1. In Cloud Manager, on the **Pipelines** page, click **Add Pipeline**.

   ![Creating a stage-only or production-only pipeline](/help/implementing/cloud-manager/configuring-pipelines/assets/stage-prod-pipelines.png)

1. In the **Add Pipeline** drop-down list, choose one of the following:

   * **Add a Non-Production Pipeline** to create a stage-only deployment pipeline. Continue to [Stage-only pipeline creation](#stage-only).
   * **Add Production Only Pipeline** to create a prod-only deployment pipeline. Continue to [Prod-only pipeline creation](#prod-only).

>[!NOTE]
>
>Some options may be dimmed (grayed out) if the corresponding pipelines already exist.
>
>* **Add Production Only Pipeline** is unavailable if a stage-only pipeline does not yet exist.
>* **Add Production Pipeline** is unavailable if a standard coupled pipeline already exists.
>* Only one prod-only and one stage-only pipelines are allowed per program.

### Stage-only pipeline creation {#stage-only}

1. After you select **Add Non-Production Pipeline**, the **Add Non-Production Pipeline** dialog box opens.
1. Under the **Pipeline Configuration** heading in the dialog box, in the **Eligible Deployment Environment** drop-down list, select the stage environment for your pipeline.

   ![Creating a stage-only pipeline](/help/implementing/cloud-manager/configuring-pipelines/assets/stage-only.png)

1. Complete the remaining fields, then in the lower-right corner, click **Continue**.

1. On the **Stage Testing** tab, define any testing that you want performed in the staging environment.

   ![Test parameters for a stage-only pipeline](/help/implementing/cloud-manager/configuring-pipelines/assets/stage-only-test.png)

1. In the lower-right corner, click **Save** to save the stage-only pipeline.

### Prod-only pipeline creation {#prod-only}

1. After you select **Add Production Only Pipeline**, the **Add Production Only Pipeline** dialog box opens.
1. In the **Pipeline Name** text field, enter the name you want.

   The remaining options and functionality in the dialog box work the same as those options and functionality found in the standard coupled pipeline creation dialog box. 

   ![Creating a production-only pipeline](/help/implementing/cloud-manager/configuring-pipelines/assets/prod-only-pipeline.png)

1. Click **Save** to save the prod-only pipeline.

## Running stage-only and prod-only pipelines {#running}

Stage-only and prod-only pipelines are run in the same way as all other pipeline are run. See [Running pipelines](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md#running-pipelines).

Additionally, you can initiate a production-only pipeline run directly from the execution details of a stage-only pipeline.

### Stage-Only Pipelines {#stage-only-run}

A stage-only pipeline operates similarly to standard coupled pipelines. However, at the end of the run, after the testing steps, a **Promote Build** button becomes available. This button lets you initiate a production-only pipeline execution using the artifacts deployed on stage by the run and deploy them to production. The button only appears if you are on the latest successful stage-only pipeline execution.

![Stage-only pipeline run](/help/implementing/cloud-manager/configuring-pipelines/assets/stage-only-pipeline-run.png)

Clicking **Promote Build** prompts you to confirm the run of the production-only pipeline or to create one if it does not already exist.

### Prod-Only Pipelines {#prod-only-run}

For prod-only pipeline, it is important to identify the source artifacts that are to be deployed to production. These details can be found in the **Artifact Preparation** step. You can navigate to those executions for further details and logs.

For the production-only pipeline, it is crucial to highlight the source artifacts that are deployed to production. You can find details about the source execution in the **Artifact Preparation** step. Navigate to those executions for more information and logs.

![Artifact details](/help/implementing/cloud-manager/configuring-pipelines/assets/prod-only-pipeline-run.png)
