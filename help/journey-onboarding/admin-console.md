---
title: Accessing the Admin Console
description: Once you understand the preparation necessary to onboarding and the basics of AEMaaCS structure, you are ready to log into the Admin Console for the first time.
---

# Accessing the Admin Console {#accessing-admin-console}

Now that you have read the article [AEM as a Cloud Service Terminology](terminology.md) and understand the basics of AEMaaCS structure, you are ready to log into the Admin Console for the first time!

## Objective {#objective}

As a system administrator you are responsible for managing users within your organization. You do this by using the Admin Console. After reading this section you should:

* Understand what and Adobe ID is.
* Be able to log in to Admin Console.
* Understand how to review your privileges as a system administrator via Admin Console.
* Know how to contact Adobe support for help.

## The Admin Console {#admin-console}

The Adobe Admin Console is a central place to administer and manage your Adobe product licenses and users. The Admin Console allows you to create and manage users in a single location instead of within your various individual solutions.

## Adobe ID {#adobe-id}

To sign into the Admin Console, you will need an Adobe ID. And Adobe ID is an account tied to a specific email address that is required to login and access AEM as a Cloud Service or any of your Adobe solutions. By using your Adobe ID you keep all your Adobe plans and products associated with a single account.

When you as the system administrator sets up your team in the Admin Console, you specify the email address that will be used as the Adobe ID.

There are three types of Adobe IDs:

* **Personal ID**: This is the default type of Adobe ID and is created at adobe.com. This account is managed by Adobe and anybody can create an account of this type.

* **Enterprise ID**: Organizations usually want to increase control of the users accounts. Only system administrators can create enterprise IDs and the organization owns these accounts with Adobe serving only as the host.

* **Federated ID**: With federated IDs the organization takes full ownership and control of the accounts. To do this your organization needs to integrate the Adobe Experience Cloud with your SAML2 single sign-on (SSO) system. This allows users to authenticate against their organization's SSO system rather than an account hosted by Adobe.

As system administrator, you may decide to onboard yourself and your team onto AEM as a Cloud Service using personal IDs before enterprise or federated IDs are set up. Once enterprise or federated IDs are set up, members can be transitioned to using those IDs.

## Logging in to Admin Console {#steps-admin-console}

Before you can use the Admin Console to administer users within your organization, you need to ensure that you yourself can access it properly and have the appropriate permissions.

1. As a System Administrator, you will receive multiple emails from Adobe as part of the onboarding process. Look for the welcome email that provides the information about the organization name to which you have been granted access.

1. Click on the **Get started** link in your welcome email to navigate to Admin Console. If you can not find the email, open a browser directly to Admin Console at [`https://adminconsole.adobe.com`](https://adminconsole.adobe.com).

   ![Welcome email](/help/journey-onboarding/assets/get-started-email.png)

1. Login using your Adobe ID. Upon successful login, you will see the **Overview** page of the Adobe Admin Console. 

   ![The Admin Console](/help/journey-onboarding/assets/get-started1.png)

1. If you have access to multiple organizations, please ensure that you have logged into correct Organization. To change your organization, click on the organization name from the top right corner and choose the required organization to which you need access.

   ![Change org](/help/journey-onboarding/assets/admin-console-orgswitch.png)

1. Select **Administrators** from the **Users** card to verify that you are a system administrator.

    ![Review administrators](/help/journey-onboarding/assets/get-started2.png)

1. Once you click on **Administrators** from the **Users** card, you can search by entering your Adobe ID email, username, first, or last name.

   ![Search users](/help/journey-onboarding/assets/get-started3.png)

1. If everything is working properly, the search will return your record. If the value in the **ADMIN ROLE** column shows **System**, you know that you (or the displayed user) are a system administrator.

   ![System status](/help/journey-onboarding/assets/get-started4.png)
   
Congratulations, system administrator!

## Adobe Identity Management System {#ims}

AEM as a Cloud Service comes pre-configured with Adobe Identity Management System (also known as IMS) for authentication. There is nothing you need to do as a system administrator to enable this.

By using IMS, AEM as a Cloud Service consolidates the login experience between AEM and the rest of the Adobe Experience Cloud. Organizations with multiple Adobe products especially benefit by creating role-based groups in the Admin Console and then assigning access to multiple products including AEM as a Cloud Service via IMS.

You will learn more about product profiles and assigning users in the next part of this onboarding journey.

## Contacting Adobe Support {#support}

If you have any issues, Adobe support can be accessed via the Admin Console. The **Support** tab lets you access various Adobe support functions through a simple and easy-to-use interface.

![Support tab](/help/onboarding/learn-concepts/assets/support-menu.png)

The tab allows you to create and manage cases, chat directly with Adobe customer support representatives, and schedule sessions with experts. System administrators and support administrators must sign in to access support cases and expert session options.

## What's Next {#whats-next}

Now that you have read this document, you should:

* Understand what and Adobe ID is.
* Be able to log in to Admin Console.
* Understand how to review your privileges as a system administrator via Admin Console.
* Know how to contact Adobe support for help.

You are ready to continue your onboarding journey by learning how to [assign team members to Cloud Manager Product Profiles](assign-profiles-cloud-manager.md) so that you colleagues can also access AEMaaCS.

## Additional Resources {#additional-resources}

* [Admin Console](/help/onboarding/learn-concepts/admin-console.md)
* [System Administrator](/help/onboarding/learn-concepts/system-administrator.md)