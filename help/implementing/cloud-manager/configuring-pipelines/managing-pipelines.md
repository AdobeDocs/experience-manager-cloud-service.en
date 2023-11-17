---
title: Managing Pipelines
description: Learn how to manage your existing pipelines including editing, running, and deleting them.
index: yes
exl-id: 4aff5a84-134a-43fa-8de8-8d564f4edd16
---

# Managing Pipelines {#managing-pipelines}

Learn how to manage your existing pipelines including editing, running, and deleting them.

## Pipeline Card {#pipeline-card}

The **Pipelines** card on the **Program Overview** page in Cloud Manager gives you an overview of all of your pipelines and their current status.

![Pipelines card in Cloud Manager](/help/implementing/cloud-manager/assets/configure-pipeline/pipelines-card.png)

By clicking the ellipsis button next to each pipeline you can take the following actions.

* [Run the pipeline](#running-pipelines)
* [Edit the pipeline](#editing-pipelines)
* [Delete the pipeline](#deleting-pipelines)
* [View details](#view-details)

At the bottom of the list of pipelines, you have general options.

* **Add** - To [add a new production pipeline](configuring-production-pipelines.md) or [add new non-production pipeline](configuring-non-production-pipelines.md)
* **Show All** - Takes the user to the Pipelines screen to view all pipelines in a more detailed table.
* **Access Repo Info** - Displays the information necessary to access the Cloud Manager git repository
* **Learn More** - Navigates to CI/CD pipeline documentation resources.

## Pipelines Window {#pipelines}

The **Pipelines** window shows a complete list of all pipelines for the selected program. This is useful as it presents more comprehensive information than what is available in the [Pipeline Card.](#pipeline-card)

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. From the **Program Overview** page, tap or click the **Pipelines** tab to switch to the **Pipelines** window.

1. Here you can see a list of all pipelines for the program as well as start and stop pipeline execution as you would in the **Pipelines Card**.

If a pipeline is executing, hovering over its **Status** column will reveal details about the execution.

![Pipeline execution details](/help/implementing/cloud-manager/assets/configure-pipeline/pipeline-status.png)

Tapping or clicking **View details** will take you to the [details of the pipeline execution.](#view-details)

## Activity Window {#activity}

The **Activities** window shows a complete list of all pipelines executions for the selected program.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. From the **Program Overview** page, tap or click the **Activity** tab to switch to the **Activity** window.

1. Here you can see a list of all pipeline executions for the program including current and historical executions.

If a pipeline is executing, hovering over its **Status** column will reveal details about the execution.

![Pipeline execution details](/help/implementing/cloud-manager/assets/configure-pipeline/pipeline-activity.png)

Tapping or clicking **View details** will take you to the [details of the pipeline execution.](#view-details)

## Running Pipelines {#running-pipelines}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Pipelines** card from the **Program Overview** page and click the ellipsis button next to the pipeline you run select **Run** from the menu.

1. The pipeline run begins and is indicated by the **Status** column. 

You can see the details of the run by clicking the ellipsis button again and selecting **[View details.](#view-details)**

Depending on the type of pipeline, you may be able to cancel the run by clicking the ellipsis button again and selecting **Cancel**.

## Editing Pipelines {#editing-pipelines}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Pipelines** card from the **Program Overview** page and click the ellipsis button next to the pipeline you want to edit and then select **Edit** from the menu.

1. The **Edit Production Pipeline** or **Edit Non-Production Pipeline** dialog box displays, allowing you to edit the same details that you entered when creating the pipeline.

   * See the following pages for details on all of the fields and configuration options available for pipelines.
     * [Configuring Production Pipelines](configuring-production-pipelines.md)
     * [Configuring Non-Production Pipelines](configuring-non-production-pipelines.md)

1. Click **Update** once you are done editing the pipeline.

>[!NOTE]
>
>You cannot edit a running pipeline.

## Deleting Pipelines {#deleting-pipelines}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Pipelines** card from the **Program Overview** page and click the ellipsis button next to the pipeline you run select **Delete** from the menu.

>[!NOTE]
>
>You cannot delete a running pipeline.

## View Pipeline Details {#view-details}

You can view the details of a pipeline to see the status and logs of its last run.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Pipelines** card from the **Program Overview** page and click the ellipsis button next to the pipeline you run select **View details** from the menu.

1. You are taken to the details page of the running pipeline.

![Pipeline details](/help/implementing/cloud-manager/assets/configure-pipeline/pipeline-running-details.png)

From here you can see the status of the various steps of the pipeline and retrieve build logs for diagnostic purposes. See the document [Deploying Your Code](/help/implementing/cloud-manager/deploy-code.md) for more information on code deployment and tests run.

All the steps in a pipeline execution are displayed with the ones not yet started grayed out. Finished steps display their duration.

Once a pipeline step is complete, a summary is presented.

![Step summary](/help/implementing/cloud-manager/assets/configure-pipeline/pipeline-step.png)

Tap or click the **View details** link to reveal the **Duration** section. This includes the average duration for the pipeline based on the historical trend for that program.

![Duration](/help/implementing/cloud-manager/assets/configure-pipeline/duration.png)

>[!NOTE]
>
>You can only view details of a pipeline that is running or has been run at least once.

## Cancel Pipelines {#cancel}

If a pipeline is in the validation or build image phase you can safely cancel the pipeline run.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. From the program overview page, click the ellipsis button of the pipeline you wish to cancel on the **Pipelines** card.

   ![Cancelling a pipeline](/help/implementing/cloud-manager/assets/cancel-pipeline.png)

1. Tap or click **Cancel**.

Alternatively you can cancel a pipeline from the pipeline details page.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Pipelines** tab from the **Program Overview** page and tap or click the pipeline you wish to cancel.

1. You are taken to the details page of the running pipeline.

   ![Cancel Pipeline details](/help/implementing/cloud-manager/assets/cancel-pipeline-details.png)

1. Tap or click **Cancel**.
