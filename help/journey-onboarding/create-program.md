---
title: Create a Program
description: Lean how to use Cloud Manager to create your first program.
role: Admin, User, Developer
exl-id: ade4bb43-5f48-4938-ac75-118009f0a73b
---
# Create a Program {#create-program}

In this part of the [onboarding journey,](overview.md) you will learn how to use Cloud Manager to create your first program.

## Objective {#objective}

After reviewing the previous document in this onboarding journey, [Access Cloud Manager,](cloud-manager.md) you have ensured you have appropriate access to Cloud Manager. Now you can create your first program.

After reading this document you will:

* Understand what a program is.
* Know the difference between production and sandbox programs.
* Be able to create your own program.

## What is a program? {#programs}

Programs are the highest level of organization in Cloud Manager. Depending on your license with Adobe, programs allow you to organize your solution and grant access to particular team members to those programs.

Cloud Manager programs represent sets of Cloud Manager environments. These programs support logical sets of business initiatives, typically corresponding to a licensed Service Level Agreement (SLA). For example, one program may represent the AEM resources to support a global public web site for an organization, while another program represents an internal, central DAM.

If you recall the example of the theoretical WKND Travel and Adventure Enterprises, who is a tenant that focuses on travel-related media, they might have two programs: one Sites program for its WKND Magazine division and one Assets program for WKND Media division. Different team members would then have access to the different programs because of their own division of labor requirements.

There are two different type of programs:

* A **production program** is created to enable live traffic for your site. This is your "real" environment.
* A **sandbox program** is typically created to serve the purposes of training, running demos, enablement, POCs, or documentation.

Since they serve different purposes, the different environments have different options. However the process of creating them is similar. For this onboarding journey we will create a sandbox environment.

>[!TIP]
>
>If you need to create a production program, see the [Additional Resources](#additional-resources) section for a link to documentation describing programs in detail.

## Creating a Sandbox Program {#create-sandbox}

Follow these steps to create a sandbox program.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.
 
1. From Cloud Manager's landing page click on **Add Program** in the top-right corner of the screen.

   ![Cloud Manager landing page](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/cloud-manager-my-programs.png) 

1. From the create program wizard, select **Set up a sandbox** and provide a program name and tap or click **Continue**.

   ![Program type creation](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/create-sandbox.png)

1. In the **Set up your sandbox** dialog, you can choose which solutions you wish to enable in your sandbox program. The **Sites** and **Assets** solutions are always included in sandbox programs and are automatically selected. This is sufficient for our onboarding example. Click **Create**.

   ![Solution selection](assets/set-up-sandbox-onboarding.png)
   
You will see a new sandbox program card on the landing page with a status indicator as the setup process progresses.

![Sandbox creation from overview page](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/program-create-setupdemo2.png)

Once the program is complete, members of your organization assigned to the **Developer** product profile can login to Cloud Manager and manage Cloud Manager git repositories.

## What’s Next {#whats-next}

Now that your first program is created, you can create environments for it. You should continue your onboarding journey by next reviewing the document [Create Environments.](create-environments.md)

## Additional Resources {#additional-resources}

The following are additional, optional resources if you would like to go beyond the content of the onboarding journey.

* [Programs and Program Types](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/program-types.md) - Learn about the hierarchy of Cloud Manager and how the different types of programs fit into its structure and how they differ.
* [Creating Sandbox Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-sandbox-programs.md) - Learn how to use Cloud Manager to create your own sandbox program for training, demo, POC, or other non-production purposes.
* [Creating Production Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md) - Learn how to use Cloud Manager to create your own production program to host live traffic.
* [Using Adobe Cloud Manager - Programs](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/programs.html) - Cloud Manager programs represent sets of AEM environments supporting logical sets of business initiatives, typically corresponding to a purchased Service Level Agreement (SLA).
* [AEM as a Cloud Service Team and Product Profiles](/help/onboarding/aem-cs-team-product-profiles.md) - Learn how AEM as a Cloud Service team and product profiles can grant and limit access to your licensed Adobe solutions.
