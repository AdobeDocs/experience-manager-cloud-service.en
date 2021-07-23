---
title: Setup Cloud Resources via Cloud Manager
description: Follow this page to learn how to setup Cloud Resources via Cloud Manager
hide: yes
hidefromtoc: yes
index: no
---
# Setup Cloud Resources via Cloud Manager {#setup-cloud-resources}

The System Administrator assigned to the *Business Owner* role should access and login to Cloud Manager. Following this, a team member assigned to the *Business Owner* product profile must login to Cloud Manager and create your cloud program and environments so that your team of experts can get started. 

## Objective {#objective}

This document helps you understand how your cloud resources are created and who can do it. 

After reading this section you should understand:

* A System Administrator assigned to the *Business Owner* role must be the first to access and login to Cloud Manager.
* How your cloud program and environments are created.

## Introduction {#introduction}

Adding your cloud resources is done via Cloud Manager by your team member assigned to Cloud Manager Business Owner product Profile. This individual is typically one who understand the business needs and who completes the initial Cloud Manager setup.

Follow the sections below to learn how to create your [cloud service programs](#create-cloud-service-program) and [environments](#create-cloud-environments).

### Pre-requisites {#prerequisites}

* The System Administrator assigned to the *Business Owner* role should access and login to Cloud Manager.

* Understand how to [navigate and login to Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/what-is-required/navigate-to-cloud-manager.html?lang=en).

* Be familiar with [Cloud Manager product profiles](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/aem-cs-team-product-profiles.html?lang=en#cloud-manager-product-profiles).

* Understand the considerations for creating your program. Watch this video to learn more.

* Understand the concepts of Cloud Manager [programs](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/getting-access/understand-program-types.html?lang=en) and [environments](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/manage-environments.html?lang=en)

## Navigate to Cloud Manager {#navigate-cloud-manager}

1. The *Business Owner* user will receive a welcome email from where they can get started, or if they cannot find it, go directly to [Adobe Experience Cloud](https://experience.adobe.com/#/@ccs/home) and login using your Adobe ID. 

   ![](/help/onboarding/onboarding-journey/assets/setup-resources1.png)

1. From the Adobe Experience Cloud home page, Select **Experience Manager**.

   ![](/help/onboarding/onboarding-journey/assets/setup-resources2.png)

1. This will take you to the AEM home page. From here, launch **Cloud Manager** .

   ![](/help/onboarding/onboarding-journey/assets/setup-resources3.png)

1. Cloud Manager landing page displays, as shown in the figure below.

   ![](/help/onboarding/onboarding-journey/assets/setup-resources4.png)

1. Verify that you have been assigned Business Owner Product Profile. To do so, select your profile from the top right, as shown below.

   ![](/help/onboarding/onboarding-journey/assets/setup-resources5.png)

1. Select **User Roles** and ensure you are assigned to Business Owner.

   ![](/help/onboarding/onboarding-journey/assets/setup-resources6.png)

1. This confirms your user role as a Business Owner.

   ![](/help/onboarding/onboarding-journey/assets/setup-resources7.png)

   Great job! You have successfully logged in to Cloud Manager as a Business Owner!

## Create Cloud Service Program {#create-cloud-service-program}

Follow the steps below to create your cloud service program from Cloud Manager:

1. Navigate to Cloud Manager landing page as shown below.

   >[!NOTE]
   >You must be a team member assigned to Cloud Manager Business Owner product profile to successfully complete this step.

   From here, click on **Add Program** to launch the Add Program wizard. 

    ![](/help/onboarding/onboarding-journey/assets/setup-resources4.png)
   
   >[!NOTE]
   >Watch the [video](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/programs.html?lang=en) to learn how to create your AEM as a Cloud program and learn about important considerations before creating your program.

   >[!IMPORTANT]
   >For step by step instruction on how to use the Add Program wizard, go [here](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/getting-access/production-programs/creating-production-program.html?lang=en).
   >
   >* Remember that the program name cannot be changed after creation. We recommend that you are certain about what name you wish to give your program.
   >* In the event that you have to change the name of your program, it will involve opening a case with Adobe Support or alternatively contacting your Adobe representative. They will assist with effectively deleting the program. You will have to start all over again with potential loss of work that your team has done.

1. Upon successful creation of your cloud program you can navigate to your program to see the **Overview** page of your program, as shown below.

   ![](/help/onboarding/onboarding-journey/assets/setup-resources8.png)

   >[!NOTE]
   >If you have not already done so, now is a good time to add your Developer members to your Cloud Manager team. Refer to Add Users to Developer product profile and follow the steps outlined.

1. Members assigned to the Developer product profile can login to Cloud Manager and [Manage Cloud Manager Git](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/managing-code/accessing-git.html?lang=en).

   Great work! Now your program is successfully created, your Cloud Manager Git is available for your Developers to access! 


## Create your Cloud Environments {#create-cloud-environments}

Once you have successfully created your cloud program, create your cloud environments.

Follow the steps below to create your cloud environments from Cloud Manager:

1. Navigate to Cloud Manager's **Overview** page and select **Add** from the environment card.

   ![](/help/onboarding/onboarding-journey/assets/setup-resources9.png)

   >[!IMPORTANT]
   >A Cloud Manager user in the Business Owner or Deployment Manager role must be logged in to successfully complete this step.

   Additionally, watch the quick [video](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/environments.html?lang=en) tutorial to learn about Cloud Manager environments and how you can add them to your program.

1. This will launch the add environment wizard that will guide your with adding your environment. Add your development environment first to get familiar. Refer to [Adding an Environment](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/manage-environments.html?lang=en#adding-environments) to learn more.

   >[!NOTE]
   >If you have not already done so, now is a good time to add your Developer members to your Cloud Manager team. Refer to Add Users to Developer product profile and follow the steps outlined.

1. Members assigned to the Developer product profile can login to Cloud Manager and [Manage Cloud Manager Git](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/managing-code/accessing-git.html?lang=en).

   Great work! Now your program is successfully created, your Cloud Manager Git is available for your Developers to access! 

   Congratulations! Now, your cloud program environments have been created, and your Developers have been added to the team!

## What’s Next {#whats-next}

Your team members must be granted permissions to the instance, since permissions to administer Cloud Manager will not suffice. Now that your cloud resources have been created and are ready to be accessed by your team, the System Administrator must assign your team members to AEM as a Cloud Service product profiles from Admin Console.

You should continue your onboarding journey by next reviewing the document Assigning Team Members to AEM as a Cloud Service Product Profiles.

>[!NOTE]
>To be granted access to AEM as a Cloud Service users must belong to one of two product profiles 'AEM Users' or 'AEM Administrators'. Learn more.

## Additional Resources {#additional-resources}

Follow the additional resources to learn about:

* [Program types and adding a program](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/programs.html?lang=en)
* [Environment types and adding an environment](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/environments.html?lang=en) 
* [Managing Cloud Manager Git](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/managing-code/accessing-git.html?lang=en)
* [Configuring access to AEM as a Cloud Service from Admin Console](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/accessing/overview.html?lang=en#adobe-ims-users)
