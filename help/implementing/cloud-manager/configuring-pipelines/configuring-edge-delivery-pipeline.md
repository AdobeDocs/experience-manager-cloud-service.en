---
title: Add an Edge Delivery Pipeline
description: Learn how to add an Edge Delivery pipeline to build and deploy your code to production environments.
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Developer
hide: no
index: false
hidefromtoc: no
exl-id: 5ad342fa-dd71-4105-a9cb-2d999d402780
---
# Add an Edge Delivery pipeline {#configure-production-pipeline}

<!--badge: label="Beta" type="Positive" url="/help/implementing/cloud-manager/release-notes/current.md#gitlab-bitbucket" -->

Learn how to configure Edge Delivery pipelines to build and deploy your code to production environments. Edge Delivery pipelines let you configure features including log forwarding and the Adobe-Managed CDN.

For a list of supported configuration, see [Use config pipelines - supported configurations](/help/operations/config-pipeline.md#configurations).

A user must have the **[Deployment Manager](/help/onboarding/cloud-manager-introduction.md#role-based-permissions)** role to configure production pipelines.

>[!IMPORTANT]
>
>An Edge Delivery pipeline cannot be configured until the following has happened: 
>
>* A program is created that contains one Edge Delivery Services site and one mapped domain. Otherwise, the option called **Add Edge Delivery Pipeline** appears disabled in the user interface, and a tooltip explains missing requirements. See [Create an Edge Delivery site in Cloud Manager](/help/implementing/cloud-manager/edge-delivery/create-edge-delivery-site.md)
>* The Git repository has at least one branch. See [Manage Repositories in Cloud Manager](/help/implementing/cloud-manager/managing-code/managing-repositories.md).
>* The production and staging environments are created. See [Introduction to CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md).

<!-- CMGR‑69680 -->

Before you start to deploy your code, configure your pipeline settings from the [!UICONTROL Cloud Manager].

>[!NOTE]
>
>You can [edit pipeline settings](managing-pipelines.md) after the initial configuration.

**To add an Edge Delivery pipeline:**

1. Sign into Cloud Manager at [experience.adobe.com](https://experience.adobe.com).
1. In the **Quick access** section, click **Experience Manager**.
1. In the left side panel, click **Cloud Manager**.
1. Select an organization that you want.
1. On the **My Programs** console, click a program. 

   ![My programs page in Cloud Manager](/help/implementing/cloud-manager/configuring-pipelines/assets/my-programs.png)

1. Do one of the following:

   * **Add an Edge Delivery pipeline from the Pipelines card**

      1. In the left rail, under **Program**, click **![Overview icon](/help/implementing/cloud-manager/configuring-pipelines/assets/overview.svg) [Overview](/help/implementing/cloud-manager/navigation.md#my-programs)**. 
      1. On the **Program Overview** page, under the **Pipelines** card, click **![Plus sign](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Add_18_N.svg)Add**, then select **Add Edge Delivery Pipeline**. 

         ![The Pipelines card on the Program Overview page](/help/implementing/cloud-manager/configuring-pipelines/assets/pipelinescard-add-ed-pipeline.png)

         >[!TIP]
         >
         >Beside using the **Pipeline** card as seen in the screenshot above, you can also manage your pipeline from the **Pipelines** page.
         >
         >![Edge Delivery pipeline widget showing pipeline name, status, repository, and branch](/help/implementing/cloud-manager/release-notes/assets/edge-delivery-pipeline-widget.png)

   * **Add an Edge Delivery pipeline from the Pipelines page**

      1. In the left rail, under **Program**, click **![Workflow icon or Pipelines icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Workflow_18_N.svg) Pipelines**.
      1. On the Pipelines page, near the upper-right corner, click **Add Pipeline** > **Add Edge Delivery Pipeline**.

         ![The Pipelines page with the Add Pipeline button](/help/implementing/cloud-manager/configuring-pipelines/assets/pipelinespage-add-ed-pipeline.png)

         >[!TIP]
         >
         >Near the upper-left corner, click **Filters**, then under the **Delivery type** section, select the **Edge delivery** checkbox to filter the list to only Edge Delivery pipelines (that is, pipelines that use Edge Delivery Services). <!-- (CMGR-69682) -->
         >
         >![Filter panel showing new Delivery type of Edge delivery and Publish delivery](/help/implementing/cloud-manager/release-notes/assets/filter-delivery-type.png)

1. In the **Add Edge Delivery Pipeline** dialog box, in the **Pipeline Name** text field, type a descriptive pipeline label.

   ![Add Edge Delivery Pipeline dialog box](/help/implementing/cloud-manager/configuring-pipelines/assets/add-edge-delivery-pipeline-configuration.png)

1. Select the pipeline **Deployment Trigger** option that you want.

   * **Manual** - You start the deployment.
   * **On Git Changes** - Git commits start the deployment automatically. With this option, you can still start the pipeline manually, if necessary.
   
1. Click **Continue**.

1. Under **Source Code**, set the following options:

   * **Deployment Environment** - Displays the target environment field; remains read-only.

   * **Repository** - Use the drop-down list to point the pipeline at the exact Git repository that stores Edge Delivery configuration.

      See also [Add and Manage Repositories](/help/implementing/cloud-manager/managing-code/managing-repositories.md) to learn how to add and manage repositories in Cloud Manager.

   * **Git Branch** - Use the drop-down list to select a specific branch within the chosen repository. If necessary, click ![Recycle icon or Refresh icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Refresh_18_N.svg) to reload the Git branch drop-down list after recent pushes.
   * **Code Location** - Defines the folder path inside the repository where pipeline-ready code starts ( `/` equals the repository root). 
   
   ![Config pipeline](/help/implementing/cloud-manager/configuring-pipelines/assets/add-edge-delivery-pipeline-sourcecode.png)

1. Click **Save**.

You can now [manage your pipeline](managing-pipelines.md) from the **Pipelines** card on the **Program Overview** page, or from the **Pipelines** page.


   ![Edge Delivery pipeline widget showing pipeline name, status, repository, and branch](/help/implementing/cloud-manager/release-notes/assets/edge-delivery-pipeline-widget.png)



