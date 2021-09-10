---
title: Setup Cloud Resources via Cloud Manager
description: Follow this page to learn how to setup Cloud Resources via Cloud Manager
role: Admin, User, Developer
exl-id: de3a33b7-b459-4e47-b232-a0f88e2ce22e
---
# Setup Cloud Resources via Cloud Manager {#setup-cloud-resources}

The System Administrator assigned to the Business Owner role should access and login to Cloud Manager. Following this, a team member assigned to the Business Owner product profile must login to Cloud Manager and create your cloud program and environments so that your team of experts can get started. 

## Objective {#objective}

This document helps you understand how your cloud resources are created and who can do it. 

After reading this section you should understand:

* A System Administrator assigned to the Business Owner role must be the first to access and login to Cloud Manager.
* How your cloud program and environments are created.

## Introduction {#introduction}

Adding your cloud resources is done via Cloud Manager by your team member assigned to Cloud Manager Business Owner product Profile. This individual is typically one who understand the business needs and who completes the initial Cloud Manager setup.

Follow the sections below to learn how to create your [cloud service programs](#create-cloud-service-program) and [environments](#create-cloud-environments).

### Pre-requisites {#prerequisites}

* The System Administrator assigned to the Business Owner role should access and login to Cloud Manager.

* Understand how to [navigate and login to Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/what-is-required/navigate-to-cloud-manager.html?lang=en).

* Be familiar with [Cloud Manager product profiles](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/aem-cs-team-product-profiles.html?lang=en#cloud-manager-product-profiles).

* Understand the concepts of Cloud Manager [programs](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/getting-access/understand-program-types.html?lang=en) and [environments](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/manage-environments.html?lang=en)

## Navigate to Cloud Manager {#navigate-cloud-manager}

The Business Owner user will receive a welcome email with a link to get started, or if they cannot find it, access [Cloud Manager](https://my.cloudmanager.adobe.com/) directly by logging in using your Adobe ID.

Follow the steps below to navigate to Cloud Manager:

1. From your welcome email click on **Get started**, as shown in the figure below.
    ![](/help/journey-onboarding/assets/get-started-email.png)

1. You will navigate to Cloud Manager's **Programs & Products** page.

   >[!IMPORTANT]
   >Alternatively, you can also navigate directly to Cloud Manager's login page from [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/). Please bookmark this page for future reference and to help you navigate directly to Cloud Manager's landing page.

1. You will be directed to Cloud Manager's landing page. See [Viewing Cloud Manager's Programs](#viewing-programs) section for more details. 

Additionally, you can navigate to Cloud Manager's **Programs and Products** page from Adobe Experience Cloud home page. Follow the steps below:

1. Navigate directly to [Adobe Experience Cloud](https://experience.adobe.com) and login using your Adobe ID.

1. From the Adobe Experience Cloud home page, Select **Experience Manager**.

   ![](/help/journey-onboarding/assets/setup-resources2.png)

1. This will take you to the AEM home page. From here, launch **Cloud Manager** .

   ![](/help/journey-onboarding/assets/setup-resources3.png)

1. Upon successful login, you will be directed to the landing page of Cloud Manager. See [Viewing Cloud Manager's Programs](#viewing-programs) section for more details.

   >[!NOTE]
   >Depending on the roles assigned in [!UICONTROL Cloud Manager] and the state of the application, you will see different screens while using [!UICONTROL Cloud Manager] UI.

### Viewing Programs in Cloud Manager's Landing page {#viewing-programs}

Upon successful login, you will be directed to the landing page of Cloud Manager. You will see one of the three options, described below:

#### When No Programs exist in Cloud Manager {#no-programs}

If no programs exist in your Organization, then your landing page directs you to create your first program, as shown in the figure below.

![](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/first_timelogin0.png)

#### When Programs already exist in Cloud Manager {#programs-exist}

If program(s) already exist in your Organization, then your landing page directs you to add another program and displays all your existing programs too, as shown in the figure below.

![](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/first_timelogin1.png)

#### When a Program exists and user is System Administrator {#programs-exist-sysadmin}

If program(s) already exist in your Organization, and you are a System Administrator, then your landing page displays **Manage Access** button along with **Add Program** option, as shown in the figure below.

![](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/admin-console-4.png)


## Verifying your User Roles {#verify-user-roles}

Once you have successfully logged into Cloud Manager, follow the steps below to verify that you have been assigned the Business Owner Product Profile:

1. Select your profile from the top right, as shown below.

   ![](/help/journey-onboarding/assets/setup-resources5.png)

1. Select **User Roles** and ensure you are assigned to Business Owner.

   ![](/help/journey-onboarding/assets/setup-resources6.png)

1. This confirms your user role as a Business Owner.

   ![](/help/journey-onboarding/assets/setup-resources7.png)

   Great job! You have successfully logged in to Cloud Manager as a Business Owner!

## Create Cloud Service Program {#create-cloud-service-program}

Follow the steps below to create your cloud service program from Cloud Manager:

1. Navigate to Cloud Manager landing page, as shown below.

   >[!NOTE]
   >You must be a team member assigned to Cloud Manager Business Owner product profile to successfully complete this step.

   From here, click on **Add Program** to launch the Add Program wizard. 

    ![](/help/journey-onboarding/assets/setup-resources4.png)
   
   >[!NOTE]
   >Watch the [video](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/programs.html?lang=en) to learn how to create your AEM as a Cloud program and learn about important considerations before creating your program.

   >[!IMPORTANT]
   >For step by step instruction on how to use the Add Program wizard, go [here](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/getting-access/production-programs/creating-production-program.html?lang=en).
   >
   >* Remember that the program name cannot be changed after creation. We recommend that you are certain about what name you wish to give your program.
   >* In the event that you have to change the name of your program, it will involve opening a case with Adobe Support or alternatively contacting your Adobe representative. They will assist with effectively deleting the program. You will have to start all over again with potential loss of work that your team has done.

1. Upon successful creation of your cloud program you can navigate to your program to see the **Overview** page of your program, as shown below.

   ![](/help/journey-onboarding/assets/setup-resources8.png)

   >[!NOTE]
   >If you have not already done so, now is a good time to add your Developer members to your Cloud Manager team. Refer to Add Users to Developer product profile and follow the steps outlined.

1. Members assigned to the Developer product profile can login to Cloud Manager and [Manage Cloud Manager Git](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/managing-code/accessing-git.html?lang=en).

   Great work! Now your program is successfully created, your Cloud Manager Git is available for your Developers to access! 


## Create your Cloud Environments {#create-cloud-environments}

Once you have successfully created your cloud program, create your cloud environments.

Follow the steps below to create your cloud environments from Cloud Manager:

1. Navigate to the Cloud Manager's **Overview** page and select **Add** from the environment card.

   ![](/help/journey-onboarding/assets/setup-resources9.png)

   >[!IMPORTANT]
   >A Cloud Manager user in the Business Owner or Deployment Manager role must be logged in to successfully complete this step.

   Additionally, watch the quick [video](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/environments.html?lang=en) tutorial to learn about Cloud Manager environments and how you can add them to your program.

1. This will launch the add environment wizard that will guide you through adding your environment. Add your development environment first to get familiar with the wizard. Refer to [Adding an Environment](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/manage-environments.html?lang=en#adding-environments) to learn more.

   >[!NOTE]
   >If you have not already done so, now is a good time to add your Developer members to your Cloud Manager team. Refer to Add Users to Developer product profile and follow the steps outlined.

1. Members assigned to the Developer product profile can login to Cloud Manager and [Manage Cloud Manager Git](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/managing-code/accessing-git.html?lang=en).

   Great work! Now your program is successfully created and your Cloud Manager Git is available for your Developers to access! 

   Congratulations! Now, your cloud program environments have been created and your Developers have been added to the team!

## What’s Next {#whats-next}

Your team members must be granted permissions to the instance, since permissions to administer Cloud Manager will not suffice. Now that your cloud resources have been created and are ready to be accessed by your team, the System Administrator must assign your team members to AEM as a Cloud Service product profiles from Adobe Admin Console.

>[!NOTE]
>To be granted access to AEM as a Cloud Service users must belong to one of two product profiles `AEM Users` or `AEM Administrators`. See [Managing Products and User Access in Admin Console](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/security/ims-support.html?lang=en#managing-products-and-user-access-in-admin-console) to learn more.

You should continue your onboarding journey by next reviewing the document [Assigning Team Members to AEM as a Cloud Service Product Profiles](/help/journey-onboarding/sysadmin/assign-team-members-aem-cloud-service.md).


## Additional Resources {#additional-resources}

Follow the additional resources to learn about:

* [Program types and adding a program](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/programs.html?lang=en)
* [Environment types and adding an environment](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/environments.html?lang=en) 
* [Managing Cloud Manager Git](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/managing-code/accessing-git.html?lang=en)
* [Configuring access to AEM as a Cloud Service from Admin Console](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/accessing/overview.html?lang=en#adobe-ims-users)
