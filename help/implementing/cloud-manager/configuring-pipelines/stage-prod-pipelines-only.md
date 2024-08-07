---
title: Stage-Only and Production-Only Deployment Pipelines
description: Learn how you can split staging and production deployments using dedicated pipelines.

---
# Stage-Only and Production-Only Deployment Pipelines {#stage-prod-only}

You now have the option to split full-stack production deployment into two smaller, specialized deployments using two new CI/CD pipelines in Cloud Manager: one that deploys just to stage and one that deploys just to production.

>[!NOTE]
>
>This feature is only available to [the early adopter program.](/help/release-notes/current.md#early-adoption)

## Overview {#overview}

Currently, the Stage and Production environments are closely linked, with deployments managed through a single pipeline. While this setup has its advantages, it does have the following limitations:

* Deploying to Stage-only requires rejecting the **Promote to Prod** step, which results in the execution being marked as cancelled.
* To promote the latest code version from Stage to Production, you must redeploy the entire pipeline, including the Stage deployment, even if no code changes have occurred.
* During Stage+Prod deployments, environments cannot be updated. If you want to pause and test on Stage for several days before promoting to Production, you cannot update the Production environment (for example, changing [environment variables](/help/getting-started/build-environment.md#environment-variables)).

Stage-only and production-only deployment pipelines offer solutions to these use cases by providing dedicated deployment options.

* **Stage-Only Deployment Pipelines:**

    * Deploys to the Stage environment, with the execution completing after the deployment and tests are finished.
    * Behaves exactly like the current Full Stack Production Pipeline, but without the Production Deployment steps (approval, schedule, deploy).

* **Prod-Only Deployment Pipelines**:
    * Deploy only to a production environment with the option to select an execution successfully finished and validated on stage and deploy its artifacts on prod.  
    * Prod-only pipelines reuses the artifacts from the stage deployments, skipping the building phase.

Neither stage-only nor prod-only pipelines will be executed while a full-stack production pipeline is running and vice-versa.

These dedicated pipelines offer more flexibility. However, you should note the following details of operation and recommendations.

>[!NOTE]
>
>Prod-only pipelines always use the artifacts from the stage-only pipeline, regardless of what may have been deployed on stage by way of the standard coupled production pipeline in the meantime.
>
>* This scenario may lead to unwanted code rollbacks.
>* Adobe recommends that you stop using the standard coupled production pipeline once you start using the prod-only and stage-only pipelines.
>* If you still decide to run both the standard coupled pipelines and stage-only/prod-only pipelines, keep in mind the reuse of artifacts to avoid code rollbacks.

## Pipeline Creation {#pipeline-creation}

Prod-only and stage-only pipelines are created in a similar fashion to the standard coupled [production pipelines](/help/using/production-pipelines.md) and [non-production pipelines.](/help/using/non-production-pipelines.md).

**To create a pipeline:**

1. In Cloud Manager, on the **Pipelines** page , click **Add Pipeline**.

   ![Creating a stage-only or production-only pipeline](/help/implementing/cloud-manager/configuring-pipelines/assets/stage-prod-pipelines.png)

1. In the Add Pipeline drop-down list, choose one of the following:

   * **Add Production Only Pipeline** to create a prod-only deployment pipeline. Continue to [Prod-only pipeline creation](#prod-only).
   * **Add Non-Production Pipeline** to create a stage-only deployment pipeline. Continue to [Stage-only pipeline creation](#stage-only).


>[!NOTE]
>
>Some options may be dimmed (grayed out) if the corresponding pipelines already exist.
>
>* **Add Production Only Pipeline** is unavailable if a stage-only pipeline does not yet exist.
>* **Add Production Pipeline** is unavailable if a standard coupled pipeline already exists.
>* Only one prod-only and one stage-only pipelines are allowed per program.

### Stage-only pipeline creation {#stage-only}

1. After you select the **Add Non-Production Pipeline** option, the **Add Non-Production Pipeline** dialog box opens.
1. Select the stage environment in the **Eligible Deployment Environments** field for your pipeline. Complete the remaining fields and tap or click **Continue**.

   ![Creating a stage-only pipeline](/help/assets/configure-pipelines/stage-only.png)

1. On the **Stage Testing** tab, you can then define testing that should be performed on the staging environment. Tap or click **Save** to save your new pipeline.

   ![Test parameters for a stage-only pipeline](/help/assets/configure-pipelines/stage-only-test.png)

### Prod-Only pipeline creation {#prod-only}

1. Once you select the **Add Production Only Pipeline** option, the **Add Production Only Pipeline** dialog opens.
1. Provide a **Pipeline Name**. The remaining options and functionality of the dialog work the same as those in the standard coupled pipeline creation dialog. Tap or click **Save** to save the pipeline.

   ![Creating a production-only pipeline](/help/assets/configure-pipelines/prod-only-pipeline.png)

## Running Prod-Only and Stage-Only Pipelines {#running}

Prod-only and stage-only pipelines are run in the same way as [all other pipelines are run.](/help/using/managing-pipelines.md#running-pipelines) Please see that documentation for details.

In addition, a prod-only pipeline run can be triggered directly from the execution details of a stage-only pipeline.

### Stage-Only Pipelines {#stage-only-run}

A stage-only pipeline runs in nearly the same way as standard coupled pipelines. However at the end of the run, after the testing steps, a **Promote Build** button allows you to start a prod-only pipeline execution that uses the artifacts deployed on stage by this execution and deploys them on production.

![Stage-only pipeline run](/help/assets/configure-pipelines/stage-only-pipeline-run.png)

The **Promote Build** button only appears if you are on the latest successful stage-only pipeline execution. Once tapped or clicked, it will ask you to confirm the run of the prod-only pipeline or to create a prod-only pipeline if one does not already exist.

### Prod-Only Pipelines {#prod-only-run}

For prod-only pipelines it is important to identify the source artifacts that are to be deployed to production. These details can be found in the **Artifact Preparation** step. You can navigate to those executions for further details and logs.

![Artifact details](/help/assets/configure-pipelines/prod-only-pipeline-run.png)
