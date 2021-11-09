---
title: Editing a Production Pipeline
description: Editing a Production Pipeline
index: yes
---

# Editing a Production Pipeline {#edit-prod-pipeline}

You can edit the pipeline configurations from the **Program Overview** page. 

>[!IMPORTANT]
>You cannot edit a pipeline that is running.

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

## Additional Production Pipeline Actions {#additional-prod-actions}

### Running a Production Pipeline {#run-prod}

You can run the production pipeline from the Pipelines card:

1. Navigate to **Pipelines** card from the **Program Overview** page.

1. Click on **...** from the **Pipelines** card and click on **Run**, as shown in the figure below.

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/prod-run.png)

### Deleting a Production Pipeline {#delete-prod}

You can delete the production pipeline from the Pipelines card:

1. Navigate to **Pipelines** card from the **Program Overview** page.

1. Click on **...** from the **Pipelines** card and click on **Delete**, as shown in the figure below.

   ![](/help/implementing/cloud-manager/assets/configure-pipeline/prod-delete.png)

   >[!NOTE]
   >A user in Deployment Manager role can now delete Production pipeline in a self-service manner via the **Delete** option from the Pipeline card.