---
title: Access the Admin Console
description: Once you understand the preparation necessary to onboarding and the basics of AEM as a Cloud Service structure, you are ready to log into the Admin Console for the first time.
exl-id: 0ccce328-a356-4ba9-b7fe-f67abc25b924
feature: Onboarding
role: Admin, User, Developer
---
# Access the Admin Console {#accessing-admin-console}

In this part of the [onboarding journey](overview.md), you learn about the preparation necessary before you can log into the system for the first time.

## Objective {#objective}

Now that you have read the article [AEM as a Cloud Service Terminology](terminology.md) and understand the basics of AEMaaCS structure, you are ready to log into the Admin Console for the first time!

As a system administrator you are responsible for managing users within your organization using the Admin Console. After reading this section you should be able to do the following,

* Understand what an Adobe ID is.
* Be able to log in to the Admin Console.
* Understand how to review your privileges as a system administrator by way of the Admin Console.
* Know how to contact Adobe support for help.

## About the Admin Console {#admin-console}

The Adobe Admin Console is a central place to administer and manage your Adobe product licenses and users. The Admin Console lets you create and manage users in a single location instead of within your various individual solutions.

### Adobe ID {#adobe-id}

To sign into the Admin Console, you need an Adobe ID. An Adobe ID is an account tied to a specific email address that is required to log in and access AEM as a Cloud Service or any of your Adobe solutions. By using your Adobe ID, you keep all your Adobe plans and products associated with a single account.

When you, as system administrator, set up your team in the Admin Console, you specify the email address that is used as the Adobe ID.

There are three types of Adobe IDs:

* **Personal ID**: The default type of Adobe ID and is created at adobe.com. Managed by Adobe and anybody can create an account of this type.

* **Enterprise ID**: Organizations usually want to increase control of the users' accounts. Only system administrators can create enterprise IDs and the organization owns these accounts with Adobe serving only as the host.

* **Federated ID**: With federated IDs, the organization takes full ownership and control of the accounts. Your organization must integrate the Adobe Experience Cloud with your SAML2 single sign-on (SSO) system. Doing so lets users authenticate against their organization's SSO system rather than an account hosted by Adobe.

As a system administrator, you may onboard yourself and your team to AEM as a Cloud Service with personal IDs. Do this task before enterprise or federated IDs are in place. Once enterprise or federated IDs are set up, members can be transitioned to using those IDs.

### Log in directly to Admin Console {#steps-admin-console}

Before you can use the Admin Console to administer users within your team, you need to ensure that you yourself can access it properly and have the appropriate permissions.

1. As a system administrator, you receive multiple emails from Adobe as part of the onboarding process. Look for the welcome email that provides the information about the organization name to which you have been granted access.

1. Click the **Get started** link in your welcome email to navigate to the Admin Console. If you cannot find the email, open a browser directly to Admin Console at [`https://adminconsole.adobe.com`](https://adminconsole.adobe.com).

   ![Welcome email](/help/journey-onboarding/assets/get-started-email.png)

1. Login using your Adobe ID. Upon successful login, you see the **Overview** page of the Adobe Admin Console. 

   ![The Admin Console](/help/journey-onboarding/assets/get-started1.png)

1. If you have access to multiple organizations, ensure that you have logged into the correct organization. To change your organization, click the organization name from the top right corner and choose the required organization to which you need access.

   ![Change org](/help/journey-onboarding/assets/admin-console-orgswitch.png)

1. Select **Administrators** from the **Users** card to verify that you are a system administrator.

    ![Review administrators](/help/journey-onboarding/assets/get-started2.png)

1. After you click **Administrators** from the **Users** card, you can search by entering your Adobe ID email, username, first, or last name.

   ![Search users](/help/journey-onboarding/assets/get-started3.png)

1. If everything works properly, the search returns your record. If the value in the **ADMIN ROLE** column shows **System**, you know that you (or the displayed user) are a system administrator.

   ![System status](/help/journey-onboarding/assets/get-started4.png)
   
Congratulations, system administrator!

## Access the Admin Console through Experience Hub  {#access-admin-console-via-experience-hub}

[Experience Hub](/help/experience-hub.md) is the unified, personalized home for AEM. It brings AEM Tools and the Admin Console together in one place.

   ![Admin Console option as it appears on the Experience Hub home page](/help/journey-onboarding/assets/experiencehub-adminconsole1.png)

**To access the Admin Console through Experience Hub:**

1. Click [Adobe Experience Cloud](https://experience.adobe.com/#/@foundationinternal/home) to open Experience Hub's home page.

1. In the **Quick access** grouping, click [**Admin Console**](https://experience.adobe.com).

## Adobe Identity Management System {#ims}

AEM as a Cloud Service comes pre-configured with Adobe Identity Management System (also known as IMS) for authentication. There is nothing that you need to do as a system administrator to enable this functionality.

By using IMS, AEM as a Cloud Service consolidates the login experience between AEM and the rest of the Adobe Experience Cloud. Organizations with many Adobe products gain the most. Create role-based groups in the Admin Console and grant product access through IMS, such as AEM as a Cloud Service.

You learn more about product profiles and assigning users in the next part of this onboarding journey.

## Contact Adobe Support {#support}

If you have any issues, Adobe support can be accessed via the Admin Console. The **Support** tab lets you access various Adobe support functions through a simple and easy-to-use interface.

![Support tab](/help/journey-onboarding/assets/support-menu.png)

The tab lets you create and manage cases, chat directly with Adobe customer support representatives, and schedule sessions with experts. System administrators and support administrators must sign in to access support cases and expert session options.

## What's next {#whats-next}

Now that you have read this document, you should:

* Understand what an Adobe ID is.
* Be able to log in to the Admin Console.
* Understand how to review your privileges as a system administrator using the Admin Console.
* Know how to contact Adobe support for help.

You are ready to continue your onboarding journey by learning how to [assign team members to Cloud Manager Product Profiles](assign-profiles-cloud-manager.md) so that your colleagues can also access AEMaaCS.

## Additional resources {#additional-resources}

The following are additional, optional resources if you would like to go beyond the content of the onboarding journey.

* [Admin Console Overview](https://helpx.adobe.com/enterprise/using/admin-console.html) - A comprehensive overview of the Admin Console
* [Create or Update Your Adobe ID](https://helpx.adobe.com/ca/manage-account/using/create-update-adobe-id.html#HowtocreateorupdateyourAdobeID) - Learn how to create an Adobe ID, change it, and manage multiple Adobe IDs.
* [SAML 2.0 Authentication Handler](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/security/saml-2-0-authenticationhandler#) - AEM ships with a SAML authentication handler. This handler provides support for the SAML 2.0 Authentication Request Protocol (Web-SSO profile) using the HTTP POST binding.
* [Administrative Roles](https://helpx.adobe.com/enterprise/using/admin-roles.html) - Using the Adobe Admin Console, organizations can define a flexible administrative hierarchy that enables fine-grained management of Adobe product access and usage.
* [Support and Expert Sessions](https://helpx.adobe.com/enterprise/admin-guide.html/enterprise/using/support-for-experience-cloud.html) - Learn how to access the support options on the Admin Console, manage your support cases, schedule an expert session, and more.
