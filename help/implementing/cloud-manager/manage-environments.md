---
title: Manage Environments - Cloud Service
description: Manage Environments - Cloud Service
---

# Managing Environments {#manage-environments} 

The following section describes the types of environment a  user can create and how the user can create an environment.

## Environment Types {#environment-types}

A user with the requisite permissions can create the following environment types (within the bounds of what is available to the specific tenant). 

* **Production and Stage Environment**: 
The Production and Stage is available as a duo and is used for testing and production purposes.  

* **Development**: A Development environment can be created for development and testing purposes and will be associated with non-production pipelines only.

  >[!NOTE]
  >A Development environment that is auto-created in a Sandbox program will be configured to include Sites and Assets solutions.
   
  The following table summarizes Environment types and their attributes:

   |Name|Author Tier|Publish Tier|User Can create| User can delete|Pipeline which can be associated with environment|
   |--- |--- |--- |--- |---|---|
   |Production |Yes |Yes if Sites included |Yes |No|Production pipeline|
   |Stage |Yes |Yes if Sites included |Yes |No|Production pipeline|
   |Development |Yes |Yes if Sites included |Yes |Yes|Non-production pipeline|

   >[!NOTE]
   >The Production and Stage is available as a duo and is used for testing and production purposes.  User will not be able to create only Stage or only Production environment.

## Adding Environment {#adding-environments}

1. Click on **Add Environment** to add an environment. This button will be accessible from the **Environments** screen. 
   ![](assets/environments-tab.png)

    The **Add Environment** option is also available on the **Environments** card when there are zero environments in the program.

    ![](assets/no-environments.png)

   >[!NOTE]
   >The **Add Environment** option will be disabled based on lack of permissions or what may be contracted.
   
1. The **Add environment** dialog box appears.The user needs to submit details such as **Environment type** and **Environment name** and **Environment description** (depending upon the user’s objective in creating the environment within the bounds of what is available to the specific tenant).

   ![](assets/add-environment2.png)

   >[!NOTE]
   >When creating an environment, one or more *integrations* are created in Adobe I/O. These are visible to customer users who have access to the Adobe I/O Console and must not be deleted. This is disclaimed in the description in the Adobe I/O Console.

   ![](assets/add-environment-image1.png)

1. Click **Save** to add an environment with the populated criteria.  Now the *Overview* screen  displays the card from where you can set up  your pipeline.

   >[!NOTE]
   >In case, you have not yet set up your non-production pipeline, the *Overview* screen  displays the card from where you can create your non-production pipeline.


## Viewing Environment {#viewing-environment}

The **Environments** card on the Overview page lists up to three environments. 

1. Select the **Show All** button to navigate to the **Environment** summary page to view a table with a complete list of environments.

   ![](assets/environment-view-1.png)

1. The **Environments** page displays the list of all the existing environments.

   ![](assets/environment-view-2.png)

1. Select any one of the environments from the list to view the environment details.

   ![](assets/environment-view-3.png)


## Updating Environment {#updating-dev-environment}

Updates of Stage and Production environments are automatically managed by Adobe. 

Updates to Development environments are managed by users of the program. When an environment is not running the latest publicly available AEM release, the status on Environments Card on the Home Screen will show **UPDATE AVAILABLE**.

![](assets/update-environ-1.png)


The **Update** option is available from the **Environments** Card. 
This option is also available, if you click on **Details** from the **Environments** card. The **Environments** page opens and once you select the Development environment, click on **...** and select **Update**, as shown in the figure below:

![](assets/environments-screen-update.png)

Selecting this option will allow a Deployment Manager to update the pipeline associated with this environment to the latest release and then execute the pipeline. 

If the pipeline has already been updated, the user is prompted to execute the pipeline.

## Deleting Environment {#deleting-environment}

User with the requisite permissions will be able to delete a Development environment. 

The **Delete** option is available from the dropdown menu in the **Environments** Card. Click on **...** for a Development environment you want to delete.

![](assets/environ-delete.png)

The delete option is also available, if you click on **Details** from the **Environments** card. The **Environments** page opens and once you select the Development environment, click on **...** and select **Delete**, as shown in the figure below:

![](assets/environ-delete-2.png)


>[!NOTE]
>
>This feature is not available for Production/Stage environment set in a regular program set up for production purposes. The feature is, however, available for Production/Stage environments in a Sandbox program.

## Managing Access {#managing-access}

Select **Manage Access** from the dropdown menu in the **Environments** Card. You can navigate to the author instance directly and manage access for your environment.

Refer to [Managing Access to Author Instance](/help/onboarding/getting-access-to-aem-in-cloud/navigation.md#manage-access-aem) to learn more.

![](assets/environ-manage-access.png)


## Accessing Developer Console {#accessing-developer-console}

Select **Developer Console** from the dropdown menu in the **Environments** Card. This will open a new tab in your browser with the login page to **Developer Console**. 

Only a user in the Developer role will have access to **Developer Console**. The exception being for Sandbox Programs, where any user with access to the Cloud Manager Sandbox Program will have access to **Developer Console**.

Refer to [Hibernating and De-hibernating Sandbox Environments](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/onboarding/getting-access/cloud-service-programs/sandbox-programs.html#hibernating-introduction) for more details.


![](assets/environ-dev-console.png)

This option is also available, if you click on **Details** from the **Environments** card. The **Environments** page opens and once you select an environment, click on **...** and select **Developer Console**.

## Login Locally {#login-locally}

Select **Local Login** from the dropdown menu in the **Environments** Card to login locally to Adobe Experience Manager 

![](assets/environ-login-locally.png)

Additionally, you can login locally from the **Environments** summary page.

![](assets/environ-login-locally-2.png)

