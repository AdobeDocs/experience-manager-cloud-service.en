---
title: Creating a Program - Cloud Service
description: Creating a Program - Cloud Service
---

# Creating a Program {#create-a-program}

The cloud-native solution provides the user with requisite permissions and the ability to create a program on a self-service model.

A program creation wizard will ask the user to submit details, depending on the user’s objective in creating the program within the bounds of what is available to the specific customer or organization.

In the event of first-time access to Cloud Manager or if no programs exist in the tenant, the user will see **Create your first Program** screen. If user select *Esc* or clicks out of the dialog box, the following screen displays:

 ![](assets/create-program1.png)


## Using Create Program Wizard {#using-create-program-wizard}

Depending upon the user’s objective in creating the program within the bounds of what is available to the specific customer/organization, a program creation wizard will ask the user to submit one or more details.

  ![](assets/create-sandbox.png)


## Creating a Sandbox Program {#create-sandbox-program} 

Follow the steps below to create a sandbox program: 
 
1. From the create program wizard, select **Set up a sandbox**. User submits program name before selecting **Create**.

   ![](assets/create-sandbox.png)

1. User will see the new sandbox program card on the landing page, and can hover over it to select the Cloud Manager icon to navigate to the Cloud Manager overview page. The card will inform the user on the status of auto-setup of the newly created sandbox program. User will see progression.

    ![](assets/program-create-setupdemo2.png)

1. After the program set up and the project creation step completes, the user can access **Manage Git** link, as shown in the figure below:

   ![](assets/create-program4.png)
   
   >[!NOTE]
   >
   >To learn more about accessing and managing your Git Repository using Self-Service Git Account Management from Cloud Manager UI, refer to [Accessing Git](/help/implementing/cloud-manager/accessing-git.md).


1. Once the development environment is created, the user can **Access AEM** link, as shown in the figure below:

   ![](assets/create-program-5.png)

1. Once the Non-production pipeline deploying to development is complete, the wizard guides the user to either access AEM (on development) or to deploy code to development environment:

   ![](assets/create-program-setup-deploy.png)

   >[!NOTE]
   >You can also edit, switch or add a program from Cloud Manager Overview page, as shown below:

   ![](assets/create-program-a1.png)

## Deleting a Sandbox Program {#delete-sandbox-program}

A Sandbox Program user in *Business Owner* or *Deployment Manager* role in Cloud Manager can delete their Production and Stage environment set via the Cloud Manager UI. 

>[!NOTE]
>Selecting the delete option on either Production or Stage also deletes the other in the set.

The delete option is available from the landing page, as shown below:

   ![](assets/delete-sandbox1.png)

Or,

Select **Delete Program** from the **Program Overview** page to delete your Sandbox Program.

   ![](assets/delete-sandbox2.png)


## Creating a Regular Program {#create-regular-program}

A *Regular* program is intended for a user who is familiar with AEM and Cloud Manager and is ready to start writing, building and testing code with the objective of deploying it to Production.

Follow the steps below to create a regular program: 

1. Select **Set up for Production** in the Create Program wizard to create a regular program. User can accept the default program name or edit it before selecting **Continue**.

   ![](assets/create-prod1.png)

1. User will select solutions that are to be included in the program in the screen that will be presented following the screen above.

   

   >[!NOTE]
   >
   >The screen below is only displayed for the segment of customers who have purchased more than one solution. For customers who have purchased just one solution, the solution selection screen below will not be displayed.

   ![](assets/set-up-prod2.png)

1. Once you have selected the solutions, click **Create**.

   ![](assets/set-up-prod3.png)

1.  Once you see your program card on the landing page, hover over it to select the Cloud Manager icon to navigate to the Cloud Manager **Overview** page. 

    ![](assets/set-up-prod4.png)

1. The main call-to-action card will guide the user to create an environment, create a non-production pipeline, and finally a production pipeline.
   ![](assets/set-up-prod5.png)


    >[!NOTE]
    >
    >A regular program does not have **Auto-setup** feature.


    


