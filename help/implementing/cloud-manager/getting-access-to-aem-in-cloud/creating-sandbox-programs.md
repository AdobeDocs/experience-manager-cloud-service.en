---
title: Creating Sandbox Programs 
description: Learn how to use Cloud Manager to create your own sandbox program for training, demo, POC, or other non-production purposes.
exl-id: 10011392-3059-4bb0-88db-0af1d390742e
---
# Creating Sandbox Programs {#create-sandbox-program}

A sandbox program is typically created to serve the purposes of training, running demos, enablement, POCs, or documentation and is not meant to carry live traffic.

Learn more about program types in the document [Understanding Program and Program Types.](program-types.md)

## Create a Sandbox Program {#create}

1. Log on to Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.
 
1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, tap or click **Add Program** near the upper-right corner of the screen.

   ![Cloud Manager landing page](assets/log-in.png) 

1. From the create program wizard, select **Set up a sandbox**, and provide a program name.

   ![Program type creation](assets/create-sandbox.png)

1. Optionally, you can add an image to the program by dragging and dropping an image file to the **Add a program image** target or clicking it to select an image from a file browser. Select **Continue**.

   * The image serves only as the tile in the program overview window and helps to identify the program.

1. In the **Set up your sandbox** dialog box, choose which solutions you want to enable in your sandbox program by checking the options in the **Solutions &amp; Add-ons** table.
   
   * Use the chevrons next to the solution names so you can see additional, optional add-ons for the solutions.
   
   * The **Sites** and **Assets** solutions are always included in sandbox programs and cannot be de-selected.

   ![Select solutions and add-ons for a sandbox](assets/sandbox-solutions-add-ons.png)

1. Once you have selected the solutions and add-ons for your sandbox program, click **Create**.

You see a new sandbox program card on the landing page with a status indicator as the setup process progresses.

![Sandbox creation from overview page](assets/sandbox-setup.png)

## Sandbox Access {#access}

You can view the detail of your sandbox setup and access the environment (once available) by viewing the program overview page.

1. From the Cloud Manager landing page, click the ellipsis button on your created program.

   ![Accessing program overview](assets/program-overview-sandbox.png)

1. After the project creation step completes, you can access the **Access Repo Info** link to be able to use your git repo.

   ![Program configuration](assets/create-program4.png)
   
   >[!TIP]
   >
   >To learn more about accessing and managing your git repository, see [Accessing Git](/help/implementing/cloud-manager/managing-code/accessing-repos.md).

1. Once the development environment is created, you can use the **Access AEM** link to sign into AEM.

   ![Access AEM link](assets/create-program5.png)

1. Once the non-production pipeline deploying to development is complete, the wizard in the call-to-action guides you to either access the AEM development environment or to deploy code to development environment.

   ![Deploying sandbox](assets/create-program-setup-deploy.png)

>[!TIP]
>
>Please see the document [Navigating the Cloud Manager UI](/help/implementing/cloud-manager/navigation.md) for details on how to navigate Cloud Manager and understanding the **My Programs** console.
