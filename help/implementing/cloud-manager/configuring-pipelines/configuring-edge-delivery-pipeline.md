---
title: Add an Edge Delivery Pipeline
description: Learn how to add an Edge Delivery pipeline to build and deploy your code to production environments.
index: no
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
badge: label="Beta" type="Positive" url="/help/implementing/cloud-manager/release-notes/current.md#gitlab-bitbucket" 
hide: yes
hidefromtoc: yes

---


# Add an Edge Delivery pipeline {#configure-production-pipeline}

Learn how to configure Edge Delivery pipelines to build and deploy your code to production environments. A production pipeline deploys code first to the stage environment. On approval, it deploys the same code to the production environment.

A user must have the **[Deployment Manager](/help/onboarding/cloud-manager-introduction.md#role-based-permissions)** role to configure production pipelines.

>[!NOTE]
>
>A production pipeline cannot be set up until the following has happened: 
>
>* The program is created.
>* The Git repository has at least one branch.
>* The production and staging environments are created.

Before you start to deploy your code, configure your pipeline settings from the [!UICONTROL Cloud Manager].

>[!NOTE]
>
>You can [edit pipeline settings](managing-pipelines.md) after the initial setup.

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

