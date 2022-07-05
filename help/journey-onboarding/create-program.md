---
title: Create a Program
description: Lean how to use Cloud Manager to create your first program.
role: Admin, User, Developer
---

# Create a Program {#create-program}

After reviewing the previous document in this onboarding journey, [Access Cloud Manager,](cloud-manager.md) you have ensured you have appropriate access to Cloud Manager. Now you can create your first program.

## Objective {#objective}

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

## Creating a Sandbox Program {#create-sandbox}

Follow these steps to create a sandbox program.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.
 
1. From Cloud Manager's landing page click on **Add Program** in the top-right corner of the screen.

   ![Cloud Manager landing page](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/first_timelogin1.png) 

1. From the create program wizard, select **Set up a sandbox**, provide a program name, and then click **Create**.

   ![Program type creation](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/create-sandbox.png)

You will see a new sandbox program card on the landing page with a status indicator as the setup process progresses.

![Sandbox creation from overview page](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/program-create-setupdemo2.png)

Once the program is complete, members of your organization assigned to the **Developer** product profile can login to Cloud Manager and manage Cloud Manager git repositories.

## What’s Next {#whats-next}

Now that your first program is created, you can create environments for it. You should continue your onboarding journey by next reviewing the document [Create Environments.](create-environments.md)

## Additional Resources {#additional-resources}

Follow the additional resources to learn about:

* [Program types and adding a program](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/programs.html)
* [Environment types and adding an environment](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/environments.html) 
* [Managing Cloud Manager Git](/help/implementing/cloud-manager/managing-code/accessing-repos.md)
* [Configuring access to AEM as a Cloud Service from Admin Console](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/accessing/overview.html#adobe-ims-users)