---
title: Add an Edge Delivery Pipeline
description: Learn how to add an Edge Delivery pipeline to build and deploy your code to production environments.
index: no
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
badge: label="Private beta" type="Positive" url="/help/implementing/cloud-manager/release-notes/current.md#gitlab-bitbucket" 
hide: yes
hidefromtoc: yes

---

# Add an Edge Delivery pipeline {#configure-production-pipeline}

Learn how to configure Edge Delivery pipelines to build and deploy your code to production environments. A production pipeline deploys code first to the stage environment. On approval, it deploys the same code to the production environment.

A user must have the **[Deployment Manager](/help/onboarding/cloud-manager-introduction.md#role-based-permissions)** role to configure production pipelines.

>[!NOTE]
>
>An Edge Delivery pipeline cannot be configured until the following has happened: 
>
>* A program is created that contains one Edge Delivery Services site and one mapped domain. Otherwise, the option **Add Edge Delivery Pipeline** appears disabled in the user interface, and a tooltip explains missing requirements. <!-- CMGR‑69680 -->
>* The Git repository has at least one branch.
>* The production and staging environments are created.

Before you start to deploy your code, configure your pipeline settings from the [!UICONTROL Cloud Manager].

>[!NOTE]
>
>You can [edit pipeline settings](managing-pipelines.md) after the initial configuration.

**To add an Edge Delivery pipeline:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the organization you want.

1. On the **My Programs** page, select the program you want.

   ![My programs page in Cloud Manager](/help/implementing/cloud-manager/configuring-pipelines/assets/my-programs.png)

1. Do one of the following:

   * **Add an Edge Delivery pipeline from the Pipelines card**

      1. In the left rail, under **Program**, click **![Overview icon](/help/implementing/cloud-manager/configuring-pipelines/assets/overview.svg) [Overview](/help/implementing/cloud-manager/navigation.md#my-programs)**. 
      1. On the **Program Overview** page, under the **Pipelines** card, click **![Plus sign](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Add_18_N.svg)Add**, then select **Add Edge Delivery Pipeline**. 

         ![The Pipelines card on the Program Overview page](/help/implementing/cloud-manager/configuring-pipelines/assets/pipelinescard-add-ed-pipeline.png)

   * **Add an Edge Delivery pipeline from the Pipelines page**

      1. In the left rail, under **Program**, click **![Workflow icon or Pipelines icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Workflow_18_N.svg) Pipelines**.
      1. On the Pipelines page, near the upper-right corner, click **Add Pipeline** > **Add Edge Delivery Pipeline**.

         ![The Pipelines page with the Add Pipeline button](/help/implementing/cloud-manager/configuring-pipelines/assets/pipelinespage-add-ed-pipeline.png)

1. In the **Add Edge Delivery Pipeline** dialog box, in the **Pipeline Name** text field, type a descriptive pipeline label.

   ![Add Edge Delivery Pipeline dialog box](/help/implementing/cloud-manager/configuring-pipelines/assets/add-edge-delivery-pipeline-configuration.png)

1. Select the pipeline **Deployment Trigger** option you want.

   * **Manual** - You start the deployment.
   * **On Git Changes** - Git commits start the deployment automatically. With this option, you can still start the pipeline manually, if necessary.
   
1. Click **Continue**.

1. Under **Source Code**, set the following options:

   * **Deployment Environment** - Displays the target environment field; remains read-only.

   * **Repository** - Use the drop-down list to point the pipeline at the exact Git repository that stores Edge Delivery configuration.

      See also [Add and Manage Repositories](/help/implementing/cloud-manager/managing-code/managing-repositories.md) to learn how to add and manage repositories in Cloud Manager.

   * **Git Branch** - Use the drop-down list to select a specific branch within the chosen repository. If necessary, click ![Recycle icon or Refresh icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Refresh_18_N.svg) to reload the Git branch drop-down list after recent pushes
   * **Code Location** - Defines the folder path inside the repository where pipeline-ready code starts ( `/` equals the repository root). 
   
   ![Config pipeline](/help/implementing/cloud-manager/configuring-pipelines/assets/add-edge-delivery-pipeline-sourcecode.png)

1. Click **Save**.

You can now [manage your pipeline](managing-pipelines.md) on the **Pipelines** card on the **Program Overview** page or from the **Pipelines** page.











<!--
## Add a new Edge Delivery pipeline {#adding-production-pipeline}

Once you have set up your program and have at least one environment using the [!UICONTROL Cloud Manager] UI, you are ready to add a production pipeline by following these steps.

>[!TIP]
>
>Before you configure a front-end pipeline, see the [AEM Quick Site Creation Journey](/help/journey-sites/quick-site/overview.md) for an end-to-end guide through the easy-to-use AEM Quick Site Creation tool. This journey can help you streamline the front-end development of your AEM Site, letting you customize your site quickly with no AEM back-end knowledge.

**To add a new Edge Delivery pipeline:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. Navigate to the **Pipelines** card from the **Program Overview** page and click **Add** to select **Add Production Pipeline**. 

   ![The Pipelines card on the Program Manager overview](/help/implementing/cloud-manager/assets/configure-pipeline/add-prod-1.png)

1. The **Add Production Pipeline** dialog box displays. Provide a **Pipeline Name** to identify your pipeline along with the following options. Click **Continue**.

   **Deployment Trigger** - You have the following options when defining the deployment triggers to start the pipeline.
      
      * **Manual** - Start the pipeline manually.
      * **On Git Changes** - Starts the CI/CD pipeline whenever commits are added to the configured Git branch. With this option, you can still start the pipeline manually as required.  

    **Important Metric Failures Behavior** - During pipeline setup or edit, the **Deployment Manager** has the option of defining the behavior of the pipeline when an important failure is encountered in any of the quality gates. The available options are:

    * **Ask every time** - Default setting. It requires manual intervention in any important failure.
    * **Fail Immediately** - If selected, the pipeline is canceled whenever an important failure occurs. This process is essentially emulating a user manually rejecting each failure.
    * **Continue Immediately** - If selected, the pipeline proceeds automatically whenever an important failure occurs. This process is essentially emulating a user manually approving each failure.

    ![Production pipeline configuration](/help/implementing/cloud-manager/assets/configure-pipeline/production-pipeline-configuration.png)

1. On the **Source Code** tab, select which type of code the pipeline should process.

   * **[Configure a full stack code pipeline](#full-stack-code)**
   * **[Configure a targeted deployment pipeline](#targeted-deployment)**

See [CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md) for more information about the types of pipelines.

The steps to complete the creation of your production pipeline vary depending on the type of source code you selected. Follow the links above to jump to the next section of this document so you can complete the configuration of your pipeline.
-->


