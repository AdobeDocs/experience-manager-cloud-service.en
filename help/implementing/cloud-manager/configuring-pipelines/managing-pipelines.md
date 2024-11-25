---
title: Manage Pipelines
description: Learn how to manage your existing pipelines including editing, running, and deleting them.
index: yes
exl-id: 4aff5a84-134a-43fa-8de8-8d564f4edd16
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Manage pipelines {#managing-pipelines}

Learn how to manage your existing pipelines including editing, running, and deleting them.

## Pipeline card {#pipeline-card}

The **Pipelines** card on the **Program Overview** page in Cloud Manager gives you an overview of all of your pipelines and their current status.

![Pipelines card in Cloud Manager](/help/implementing/cloud-manager/assets/configure-pipeline/pipelines-card.png)

By clicking ![Ellipsis - More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) next to each pipeline, you can take the following actions:

* [Run a pipeline](#running-pipelines)
* [Cancel a pipeline](#cancel)
* [Edit a pipeline](#editing-pipelines)
* [Delete a pipeline](#deleting-pipelines)
* [View last run details of a pipeline](#view-details)

At the bottom of the list of pipelines, you have the following general options:

* **Add** - To [add a new production pipeline](configuring-production-pipelines.md) or [add a new non-production pipeline](configuring-non-production-pipelines.md)
* **Show All** - Takes the user to the Pipelines screen to view all pipelines in a more detailed table.
* **Access Repo Info** - Displays the information necessary to access the Cloud Manager git repository
* **Learn More** - Navigates to CI/CD pipeline documentation resources.

## Pipelines page {#pipelines}

The **Pipelines** page shows a complete list of all pipelines for the selected program. This information is useful because it presents more comprehensive information than what is available in the [Pipeline card](#pipeline-card).

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. From the **Program Overview** page, click ![Pipeline tab - Workflow icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Workflow_18_N.svg) **Pipelines** tab.

1. On the **Pipelines** page, you can see a list of all pipelines for the program and start and stop pipeline execution as you would in the **Pipelines Card**.

If a pipeline is executing, click ![Info - medium icon](https://spectrum.adobe.com/static/icons/ui_18/InfoMedium.svg) in the **Status** column to display a pop-up with details about the execution. Within the pop-up, click **View details** to see the [details of the pipeline execution](#view-details).

![Pipeline execution details](/help/implementing/cloud-manager/assets/configure-pipeline/pipeline-status.png)


You can also click ![Ellipsis - More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) next to the pipeline to take additional actions appropriate to the pipeline state such as [editing](#editing-pipelines) it or [canceling execution](#cancel).

![Pipeline actions](/help/implementing/cloud-manager/assets/configure-pipeline/pipeline-actions.png)

## Activity page {#activity}

The **Activity** page shows a complete list of all pipelines executions for the selected program and other important program events.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. From the **Program Overview** page, in the side menu, click ![Bell icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Bell_18_N.svg) **Activity**.

1. In the **Activity** page, you can see a list of all pipeline executions for the program, including current and historical executions.

If a pipeline is executing, you can click ![Info - medium icon](https://spectrum.adobe.com/static/icons/ui_18/InfoMedium.svg) in the **Status** column to display a pop-up showing you information about the execution.

![Pipeline execution details](/help/implementing/cloud-manager/assets/configure-pipeline/pipeline-activity.png)

Click the row representing the pipeline execution to view the [details of the pipeline execution](#view-details).

You can also click ![Ellipsis - More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) to take additional action on the pipeline execution, such as view its details or download the log, which takes you to the [pipeline details page](#view-details).

![Pipeline execution actions](/help/implementing/cloud-manager/assets/configure-pipeline/pipeline-execution-actions.png)

## Run a pipeline {#running-pipelines}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Pipelines** card from the **Program Overview** page.

1. Click ![Ellipsis - More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) next to the pipeline that you run.

1. From the drop-down menu, click ![Run - Play icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_PlayCircle_18_N.svg) **Run**.

   The pipeline run starts, and the **Status** column displays its progress.

You can see the details of the run by clicking ![Ellipsis - More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) again and clicking **[View details](#view-details)**.

Depending on the type of pipeline, you may be able to cancel the run by clicking ![Ellipsis - More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) again and clicking **Cancel**.

## Edit a pipeline {#editing-pipelines}

You can edit a pipeline if it is not running.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Pipelines** card from the **Program Overview** page.

1. Click ![Ellipsis - More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) next to the pipeline that you want to edit.

1. From the drop-down menu, click **Edit**.

1. In the **Edit Production Pipeline** or **Edit Non-Production Pipeline** dialog box, edit the same details that you entered when creating the pipeline.

   See the following pages for details on the fields and configuration options available for pipelines.
     * [Configure a Production Pipeline](configuring-production-pipelines.md)
     * [Configure a Non-Production Pipeline](configuring-non-production-pipelines.md)

1. When you are done, click **Update**.

>[!NOTE]
>
>Web tier and config pipelines are not supported with private repositories. See [Add a Private GitHub Repository in Cloud Manager](/help/implementing/cloud-manager/managing-code/private-repositories.md) for details and the full list of limitations.

## Delete a pipeline {#deleting-pipelines}

You can delete a pipeline if it is not running.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Pipelines** card from the **Program Overview** page.

1. Click ![Ellipsis - More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) next to the pipeline that you run.

1. From the drop-down menu, click **Delete**.


## View last run details of a pipeline {#view-details}

You can check the details of a pipeline to view the status and logs from its most recent run. However, you can only access the details if the pipeline is currently running or has been executed at least once.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Pipelines** card from the **Program Overview** page.

1. From the drop-down menu, click ![Ellipsis - More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) next to the pipeline that you run.

1. From the drop-down menu, click **View last execution**.

   You are taken to the details page of the running pipeline.

   ![Pipeline details](/help/implementing/cloud-manager/assets/configure-pipeline/pipeline-running-details.png)

   From here, you can see the status of the various steps of the pipeline and retrieve build logs for diagnostic purposes. See [Deploy Your Code](/help/implementing/cloud-manager/deploy-code.md) for more information on code deployment and tests run.

   All the steps in a pipeline execution are displayed with the ones not yet started grayed out. Finished steps display their duration.

   After a pipeline step is complete, a summary is presented.

   ![Step summary](/help/implementing/cloud-manager/assets/configure-pipeline/pipeline-step.png)

1. Click **View details** to expand the **Duration** section, where you can see the average duration of the pipeline based on the program's historical trends.

   ![Duration](/help/implementing/cloud-manager/assets/configure-pipeline/duration.png)

1. If your pipeline included a **Code Scanning** step that flagged issues, click **Download Details** to access a list of [code quality tests](/help/implementing/cloud-manager/code-quality-testing.md) that failed to pass.

   ![Code quality issues](assets/managing-pipelines-code-quality-issues.png)

   The CSV file includes a **Project File Location** column, showing the path to the problematic code relative to the project. In contrast, the **File Location** column reflects the Maven-generated path.

   ![Project code scan issue details](assets/managing-pipelines-code-quality-details.png)

## Cancel a pipeline {#cancel}

You can safely cancel the pipeline run if it is in the validation or build image phase.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. From the program overview page, click ![Ellipsis - More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) of the pipeline you want to cancel on the **Pipelines** card.

   ![Canceling a pipeline](/help/implementing/cloud-manager/assets/cancel-pipeline.png)

1. Click **Cancel**.

Alternatively, you can cancel a pipeline from the pipeline details page.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the ![Pipelines tab - Workflow icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Workflow_18_N.svg) **Pipelines** tab from the **Program Overview** page and select the pipeline you want to cancel.

   You are taken to the details page of the running pipeline.

   ![Cancel Pipeline details](/help/implementing/cloud-manager/assets/cancel-pipeline-details.png)

1. Click **Cancel**.
