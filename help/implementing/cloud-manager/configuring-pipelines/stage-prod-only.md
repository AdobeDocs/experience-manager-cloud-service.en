---
title: Split Stage-Only and Production-Only Pipelines
description: Learn how you can split staging and production deployments using dedicated pipelines.
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
badge: label="Beta" type="Positive" url="/help/implementing/cloud-manager/release-notes/current.md#staging-production-only-pipelines"
hide: yes
hidefromtoc: yes
index: no
exl-id: 7d76a87c-122c-4c4d-8071-957bef4c9cf1
---
# Split stage-only and production-only pipelines {#stage-prod-only}

You can split staging and production deployments using dedicated pipelines.

## Overview {#overview}

Staging and production environments are tightly coupled. By default, deployments to them are linked to a singular pipeline. That is, a deployment pipeline deploys to both the staging and production environments in that program. While this coupling is normally suitable, there are certain use cases where disadvantages are present:

* If you want to deploy to stage-only, you reject the **Promote to Prod** step in the pipeline. However, the execution becomes marked as canceled.
* If you want to deploy the latest code in a staging environment to production, you need to redeploy the entire pipeline including the staging deployment even though no code was changed there.
* Environments cannot be updated during deployments. If you pause to test in the staging environment for several days before promoting to production, the production environment remains locked and cannot be updated. This scenario makes non-dependent tasks such as updating [environment variables](/help/implementing/cloud-manager/environment-variables.md) impossible.

Stage-only and prod-only pipelines offer solutions to these use-cases by providing dedicated deployment options.

* **Stage-Only Deployment Pipelines:** Deploys only to a staging environment with the execution finishing once the deployment and tests are done. A stage-only pipeline behaves identically to the standard coupled full stack prod pipeline but without the production deployment steps (approval, schedule, deploy).
* **Prod-Only Deployment Pipelines:** Deploys only to production by selecting the most recent successful stage execution. Then deploying its artifacts to production. Prod-only pipelines reuse stage deployment artifacts, bypassing the build phase.

Stage-only and prod-only pipelines are not executed while a full-stack production pipeline is in progress, and vice versa. If both the stage-only and the full-stack production pipeline have the **On Git Changes** trigger configured and are pointing to the same branch and repository, only the stage-only pipeline is automatically started. Prod-only pipelines do not start **`On Git Changes`** because they are not directly linked to a repository.

Prod-only pipelines are triggered manually, as they are not directly linked to a repository for **On Git Changes**.

These dedicated pipelines offer more flexibility, but you should note the following details of operation and recommendations.

>[!NOTE]
>
>Prod-only pipelines always use artifacts from the stage-only pipeline. This process remains true even if the standard coupled production pipeline has deployed something else to stage in the meantime.
>
>* Such as scenario could lead to unwanted code rollbacks.
>* Adobe recommends to stop using the standard coupled production pipeline once you start using the prod-only and stage-only pipelines.
>* If you still decide to run both the standard coupled pipelines and stage/prod-only pipelines, keep in mind the reuse of artifacts to avoid code rollbacks.

## Pipeline creation {#pipeline-creation}

Prod-only and stage-only pipelines are created in a similar fashion to the standard coupled [production pipelines](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md) and [non-production pipelines](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md). See those documents for details.

1. In the **Pipelines** window, click **Add Pipeline**.

   * Select **Add Non-Production Pipeline** to [create a stage-only pipeline](#stage-only).
   * Select **Add Production Only Pipeline** to [create a prod-only pipeline](#prod-only).

![Creating a prod/stage-only pipeline](/help/implementing/cloud-manager/configuring-pipelines/assets/prod-stage-pipeline.png)

>[!NOTE]
>
>Certain options may be grayed out if the corresponding pipelines already exist.
>
>* **Add Production Only Pipeline** is unavailable if a stage-only pipeline does not yet exist.
>* **Add Production Pipeline** is unavailable if a standard coupled pipeline already exists.
>* Only one prod-only and one stage-only pipelines are allowed per program.

### Create a stage-only pipeline {#stage-only}

1. In the **Add Non-Production Pipeline** dialog box, on the **Configuration** tab, select the **Deployment Pipeline** field for your pipeline.
1. In the Non-Productoin Pipeline Name field, enter a free-text name.
1. Select the desired deployment options, then click **Continue**.

   ![Configuration tab in the Add Non-Production Pipeline dialog box](/help/implementing/cloud-manager/configuring-pipelines/assets/add-non-prod-pipeline-1.png)

1. On the **Source Code** tab, select **Full Stack Code**. This option builds and deploys the entire AEM application (back-end, Dispatcher/web tier config, and any front-end modules in the repo).

1. In the **Eligible Deployment Environments** drop-down list, select the **stage** environment as the deployment environment for your pipeline. Selecting stage creates a pipeline dedicated to the stage environment (production promotion happens by way of a separate pipeline).

1. Select your **Repository** and **Git Branch** in the respective drop-down lists, then click **Continue**. 

   ![Source Code tab in the Add Non-Production Pipeline dialog box](/help/implementing/cloud-manager/configuring-pipelines/assets/add-non-prod-pipeline-2.png)

1. On the **Experience Audit** tab, the specified Site URL is the published URL that Cloud Manager audits for page quality. 

1. In the **Page Path** field, specify which pages you want to audit, then click **![Add icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Add_18_N.svg) Add Page**.

   The Experience Audit analyzes each path that you add for performance, accessibility, progressive web apps, best practices, SEO, and other quality checks. You can add multiple paths and remove any by clicking ![Cross size 400 icon](https://spectrum.adobe.com/static/icons/ui_18/CrossSize400.svg).

   ![Experience Audit tab in the Add Non-Production Pipeline dialog box](/help/implementing/cloud-manager/configuring-pipelines/assets/add-non-prod-pipeline-3.png)

1. Click **Save**.


### Create a prod-only pipeline {#prod-only}

1. In the dialog box **Add Production Only Pipeline**, in the **Pipeline Name** text field, enter the free-text name of the pipeline.
1. In the **Pipeline Name** field, type the name you want.
1. Under **Production Deployment Options**, select **Pause before deploying to Production**.

   This option inserts a manual approval gate right before the production step. The pipeline stops and waits for an approver (such as a Deployment Manager, or a Business Owner) to Approve or Cancel the production deploy. 
   
   Use for change control or last-minute checks.

1. Click **Save** to create the production-only pipeline with these options.

   ![Creating a production-only pipeline](/help/implementing/cloud-manager/configuring-pipelines/assets/add-production-only-pipeline.png)

## Run stage-only and prod-only pipelines {#running}

You can start the new pipelines [like any other pipeline](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md#running-pipelines). You can also trigger a production-only pipeline directly from a stage-only pipeline's execution details.

<!-- * Stage-only and prod-only pipelines offer a new [emergency mode](#emergency-mode) to skip testing.
Prod-only pipeline run can be triggered directly from the execution details of a [stage-only pipeline](#stage-only-run).


### Emergency Mode {#emergency-mode}

When starting production-only and staging-online pipelines, you are prompted to confirm the start and how it starts.

* **Normal Mode** is a standard run and includes stage testing steps.
* **Emergency Mode** skips stage testing steps.

![Emergency Mode](/help/assets/configure-pipelines/emergency-mode.png) -->

### Run stage-only pipelines {#stage-only-run}

In the execution details, a **Promote Build** button appears after the testing steps. Click it to trigger a production-only pipeline that deploys this run's stage artifacts to production. The button shows only on the latest successful stage-only run.

![Stage-only pipeline run](/help/implementing/cloud-manager/configuring-pipelines/assets/stage-only-pipelines-run.png)

When you click **Promote Build**, a dialog box opens for you to confirm the run of the related production-only pipeline. Click **Run** to start it. 

![Promote Build - Run Pipeline dialog box](/help/implementing/cloud-manager/configuring-pipelines/assets/promote-build-run.png)

If none exists, a setup dialog box prompts you to create one.

![Promote Build - No valid pipeline dialog box](/help/implementing/cloud-manager/configuring-pipelines/assets/promote-build-no-valid-pipeline.png)


### Run prod-only pipelines {#prod-only-run}

For a **production-only** pipeline, Cloud Manager displays the source artifacts that are deployed to production. Check the **Artifact Preparation** step for the source execution, then open it to view details and logs.


![Artifact details](/help/implementing/cloud-manager/configuring-pipelines/assets/prod-only-pipelines-run.png)
