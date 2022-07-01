---
title: Set Up Cloud Resources
description: Lean how to use Cloud Manager to set up and manage your own cloud resources like programs and environments.
role: Admin, User, Developer
exl-id: de3a33b7-b459-4e47-b232-a0f88e2ce22e
---
# Set Up Cloud Resources {#cloud-resources}

Lean how to use Cloud Manager to set up and manage your own cloud resources like programs and environments.

## Objective {#objective}

Since you completed the previous step in this journey, [Assigning Team Members to Cloud Manager Product Profiles,](assign-profiles-cloud-manager.md) your team can acess Cloud Manager. The next step is to create the resources within Cloud Manager necessary for your AEM as a Cloud Service project such as programs and environments.

After reading this document you should understand:

* A system administrator assigned to the **Business Owner** role must be the first in your organization to login and access Cloud Manager.
* How programs and environments are created in Cloud Manager.

## Introduction {#introduction}

Adding your cloud resources such as programs and environments is done via Cloud Manager. Typically a team member assigned to the **Business Owner** product profile is responsible for this task. This individual understands the business needs and who completes the initial Cloud Manager setup.

For the purposes of this onboarding journey, you, as the system administrator, already assigned yourself to the **Business Owner** product profile and will set up the cloud resources. Depending actual project requirements, the business owners may or may not be the same as the system administrator.

## Access Cloud Manager as System Administrator and Business Owner {#access-sysadmin-bo}

Before the team members that you assigned to the **Business Owner** role can access cloud manager and begin creating cloud resources, the system administrator must be assigned the **Business Owner** role and sign into Cloud Manager as you did in the previous step in this onboarding journey.

1. Ensure that you, as system administrator, have the **Business Owner** role assigned.

   * Return to the previous step in this journey, [Assign Team Members to Cloud Manager Product Profiles,](assign-profiles-cloud-manager.md) for more information about assigning the **Business Owner** role to the system administrator if you have not already done this.

1. Sign into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and be presented with the normal landing page.

By successfully signing in as system administrator with the **Business Owner** role, you initialize Cloud Manager for use by the other users with the **Business Owner** role. You will not receive a confirmation of this or any message. Simply signing in suffices.

Until you sign in to Cloud Manager as system administrator with the **Business Owner** role, other users with the **Business Owner** role will not be able to create programs in Cloud Manager even if they are assigned the correct roles.

## Navigate to Cloud Manager {#navigate-cloud-manager}

Users with the **Business Owner** role will receive a welcome email with a link to get started. Follow the steps below to navigate to Cloud Manager using this welcome email.

1. From your welcome email click on **Get started**, as shown in the figure below.
    ![Email example](/help/journey-onboarding/assets/get-started-email.png)

1. You will navigate to Cloud Manager's **Programs & Products** page.

   >[!TIP]
   >
   >You can also navigate directly to Cloud Manager's login page from `[my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/)`. Please bookmark this page for future reference.

1. You will be directed to Cloud Manager's landing page.

Alternatively, you can also navigate to Cloud Manager's **Programs and Products** page from Adobe Experience Cloud home page by following these steps

1. Navigate directly to [Adobe Experience Cloud](https://experience.adobe.com) and login using your Adobe ID.

1. From the Adobe Experience Cloud home page, Select **Experience Manager**.

   ![Experience Cloud homepage](/help/journey-onboarding/assets/setup-resources2.png)

1. This will take you to the AEM home page. From here, click **Launch** on the **Cloud Manager** tile.

   ![AEM home page](/help/journey-onboarding/assets/setup-resources3.png)

1. Upon successful login, you will be directed to the landing page of Cloud Manager. See [Viewing Cloud Manager's Programs](#viewing-programs) section for more details.

How you access your programs and products via Cloud Manager is up to you and has no effect on how you use Cloud Manager or how you manage your programs.

>[!NOTE]
>
>Depending on the roles assigned in Cloud Manager and the state of the application, you will see different screens while using the Cloud Manager UI.

## Viewing Programs {#viewing-programs}

Once you successfully access Cloud Manager, what you see will depend on the state of your programs as detailed in the following sections.

### When No Programs Exist {#no-programs}

If no programs exist in your organization, then your landing page directs you to create your first program.

![No programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/first_timelogin0.png)

### When Programs Already Exist {#programs-exist}

If programs already exist in your organization, then your landing page displays your existing programs and also offers a button to add additional programs.

![Programs exist](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/first_timelogin1.png)

### When a Program Exists and You are a System Administrator {#programs-exist-sysadmin}

If programs already exist in your organization and you are a system administrator, then your landing page displays **Manage Access** button along with **Add Program** option.

![System administrator view](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/admin-console-4.png)

## Verifying Your User Roles {#verify-user-roles}

Once you have successfully logged into Cloud Manager, you can verify that you have been assigned the **Business Owner** product profile.

1. Select your profile from the top right of the window.

   ![User profile](/help/journey-onboarding/assets/setup-resources5.png)

1. Select **User Roles** to display the roles assigned to your user.

   ![User roles](/help/journey-onboarding/assets/setup-resources6.png)

1. The dialog should confirm that your user has the **Business Owner** role.

   ![List of user roles](/help/journey-onboarding/assets/setup-resources7.png)

You have successfully logged in to Cloud Manager as a Business Owner! If you are not assigned the **Business Owner** role, contact your system administrator.

## Create a Cloud Service Program {#create-cloud-service-program}

Now that you have ensured you have appropriate access, you can create your first program.

1. Navigate to the Cloud Manager landing page at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and sign in.

1. On the Cloud Manager landing page, click on **Add Program** to launch the Add Program wizard. 

   ![Landing page](/help/journey-onboarding/assets/setup-resources4.png)
   
   >[!TIP]
   >
   >For step by step instruction on how to use the Add Program wizard, go refer to the document [Creating Production Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md) or watch this [video](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/programs.html) to learn how to create your AEM as a Cloud program and learn about important considerations before creating your program.

   
1. Upon successful creation of your cloud program you can navigate to your program from the Cloud Manager landing page to see the **Overview** page of your program.

   ![Program overview](/help/journey-onboarding/assets/setup-resources8.png)

1. Members assigned to the Developer product profile can login to Cloud Manager and manage Cloud Manager git repositories.

   * If you have not already done so, now is a good time to assign members to the **Developer** role in your Cloud Manager team. Return to the [Assign Team Members to Cloud Manager Product Profiles](/help/journey-onboarding/sysadmin/assign-team-members-cloud-manager.md) document of this journey for more information.

Now your program is successfully created and your Cloud Manager git repository is available for your developers to access! 

## Create your Cloud Environments {#create-cloud-environments}

Once you have successfully created your cloud program, create your cloud environments.

1. Navigate to the Cloud Manager landing page at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select **Add** from the environment card.

   ![Add Environment button](/help/journey-onboarding/assets/setup-resources9.png)

1. The add environment wizard launches and guides you through adding your environment. Add your development environment first to get familiar with the wizard.
 
   >[!TIP]
   >
   >Refer to the document [Adding an Environment](/help/implementing/cloud-manager/manage-environments.md#adding-environments) to learn more or watch [this quick video tutorial](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/environments.html) to learn about Cloud Manager environments and how you can add them to your program.

1. Members assigned to the **Developer** product profile can login to Cloud Manager and manage Cloud Manager git repositories.

Now your program is successfully created and your Cloud Manager git is available for your developers to access!

## What’s Next {#whats-next}

Now that your cloud resources have been created and are ready to be accessed by your team, the System Administrator must assign your team members to AEM as a Cloud Service product profiles from Adobe Admin Console in order to access those resources.

You should continue your onboarding journey by next reviewing the document [Assigning Team Members to AEM as a Cloud Service Product Profiles](/help/journey-onboarding/sysadmin/assign-team-members-aem-cloud-service.md) where you will learn how to grant your team members the rights they need to access your new environments.

## Additional Resources {#additional-resources}

Follow the additional resources to learn about:

* [Program types and adding a program](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/programs.html)
* [Environment types and adding an environment](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/environments.html) 
* [Managing Cloud Manager Git](/help/implementing/cloud-manager/managing-code/accessing-repos.md)
* [Configuring access to AEM as a Cloud Service from Admin Console](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/accessing/overview.html#adobe-ims-users)
