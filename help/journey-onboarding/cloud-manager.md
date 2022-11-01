---
title: Access Cloud Manager
description: Learn how to access Cloud Manager so that you can set up your project resources.
role: Admin, User, Developer
exl-id: c9476ac9-8318-493e-a48d-94ff5a6433a7
---
# Access Cloud Manager {#cloud-resources}

In this part of the [onboarding journey,](overview.md) you will learn how to access Cloud Manager so that you can set up your project resources.

## Objective {#objective}

In the previous article in this onboarding journey, [Assigning Team Members to Cloud Manager Product Profiles,](assign-profiles-cloud-manager.md) you granted your AEMaaCS team the proper roles. Now learn how to access Cloud Manager so that you can set up your project resources that your team will use.

Since you completed the previous step in this journey, your team can access Cloud Manager. Cloud Manager is used to create and manage your project resources such as programs and environments.

After reading this document you should understand:

* That a system administrator assigned to the **Business Owner** role must be the first in your organization to login and access Cloud Manager.
* How to sign into Cloud Manager.

## Cloud Manager {#cloud-manager}

Cloud Manager is an essential component of AEM as a Cloud Service and serves as the single entry point for your team. It supports customers with enterprise development setups with its purpose-built CI/CD pipelines, which are equipped to ensure thorough testing and highest code quality to deliver exceptional experiences. Cloud Manager provides everything required to get started in a self-service manner including the ability to create your cloud resources and environments.

Typically a team member assigned to the **Business Owner** product profile is responsible for adding your cloud resources such as programs and environments. This individual understands the business needs and who completes the initial Cloud Manager setup.

For the purposes of this onboarding journey, you, as the system administrator, already assigned yourself to the **Business Owner** product profile and will set up the cloud resources. Depending actual project requirements, the business owners may or may not be the same as the system administrator.

>[!NOTE]
>
>By default a user with access to an AEM environment will also have Cloud >Manager User role. This role in and of itself is insufficient to give the user access to program details view. Such a user with only Cloud Manager user role is able to navigate via the program menu options to the AEM environment author URL (if environments exist). Such users must contact their administrator if they wish to get program-level access.

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

## What’s Next {#whats-next}

Now that you can access Cloud Manager as a system administrator, you are ready to create your first program.

You should continue your onboarding journey by next reviewing the document [Create a Program](create-program.md) where you will learn how to do so.

## Additional Resources {#additional-resources}

Follow the additional resources to learn about:

* [Introduction to Cloud Manager](/help/onboarding/cloud-manager-introduction.md) - 
Learn about Cloud Manager, Cloud Manager programs, and environments.
