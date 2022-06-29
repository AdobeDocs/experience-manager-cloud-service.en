---
title: AEM as a Cloud Service Terminology
description: This first part of the onboarding journey summarizes some basic terms you will need to know as you onboard into AEM as a Cloud Service.
---

# AEM as a Cloud Service Terminology {#terminology}

This first part of the onboarding journey summarizes some basic terms you will need to know as you onboard into AEM as a Cloud Service.

## Objective {#objective}

AEM as a Cloud Service is a powerful and flexible tool and to use any tool you should be familiar with the terminology and language used to describe it. This first step in your onboarding journey summarizes some key terms you need to understand before you begin using the system and how to contact support if you need help with any of these concepts.

After reading this document you will understand

* What a system administrator is.
* What the admin console is.
* What the Adobe Identity Management System is.
* What an Adobe ID is.
* How to contact Adobe support.

## System Administrator {#system-administrator}

The system administrator is the individual who is first contacted by Adobe after your AEM as a Cloud Service contract is signed, and is typically the first person to access and set up your AEM as a Cloud Service resources. This onboarding journey is written specifically for the role of the system administrator. If you are reading this, you are likely the system administrator.

The system administrator manages all aspects of their organizations AEMaaCS users, from access to permissions by using the Admin Console. To do this, a system administrator is an AEM as a Cloud Service user who has admin privileges in the [Admin Console,](#admin-console) which itself is described below.

## Admin Console {#admin-console}

The Adobe Admin Console is a central place to administer and manage your Adobe product licenses and users. The Admin Console allows you to create and manage users in a central location and not within your individual solutions.

## Adobe Identity Management System {#ims}

AEM as a Cloud Service comes pre-configured with Adobe Identity Management System (also known as IMS) for authentication.

AEM as a Cloud Service consolidates the login experience between AEM and the rest of the Adobe Experience Cloud. Organizations with multiple Adobe products especially benefit by creating role-based groups in the [Admin Console](#admin-console) and then assigning access to multiple products including AEM as a Cloud Service via IMS.

## Adobe ID {#adobe-id}

An Adobe ID is an account tied to a specific email address that is required to login and access AEM as a Cloud Service or any of your Adobe solutions. By using your Adobe ID you keep all your Adobe plans and products associated with a single account.

When you as the system administrator sets up your team in the Admin Console, you specify the email address that will be used as the Adobe ID.

There are three types of Adobe IDs:

* **Personal ID**: This is the default type of Adobe ID. Basically, the user needs to create an account at adobe.com. In other words, this account is managed by Adobe and anybody can create an account of this type.

* **Enterprise ID**: Organizations usually want to increase the control of the users’ accounts. With Enterprise ID, only system administrators can create these type of accounts and the organization owns these accounts; Adobe only hosts them.

* **Federated ID**: This is where the organization takes full ownership and control of the accounts. In this case, you need to integrate the Adobe Experience Cloud with your SAML2 SSO system. The final result is that users authenticate against their company’s SSO system and not against an account hosted at Adobe. See [SAML 2.0 Authentication Handler](https://experienceleague.adobe.com/docs/experience-manager-65/administering/security/saml-2-0-authenticationhandler.html?lang=en) to learn more.

>[!NOTE]
>If your Enterprise ID or Federated ID has not yet been setup, your system administrator may decide to onboard your team using Personal ID’s. Once the Enterprise or Federated ID is set up, members can be transitioned to using this ID.

# Contacting Adobe Support {#support}

Adobe Support can be accessed via Adobe Admin Console from where you can manage your support cases and schedule an expert session.

The **Support** tab in the [Admin Console](https://adminconsole.adobe.com/) lets you access various support functions through a simple and easy-to-use interface. 

![image](/help/onboarding/learn-concepts/assets/support-menu.png)

The interface allows you to create and manage cases, chat directly with Adobe Customer Support representatives, and schedule sessions with experts. [System Administrators and Support Administrators](https://helpx.adobe.com/enterprise/using/admin-roles.ug.html) must sign in to access the Support cases and Expert Session options.

>[!NOTE]
> Refer to [Experience Cloud | Support and Expert Sessions](https://helpx.adobe.com/enterprise/admin-guide.html/enterprise/using/support-for-experience-cloud.ug.html) for more details.

## What’s Next {#what-is-next}

Now that you have completed this part of the AEM Onboarding Journey you should:

* Understand the basic terms used when discussing AEM as a Cloud Service.
* Know how to contact Adobe support if you need assistance in your onboarding process.

Build on this knowledge and continue your AEM onboarding journey by next reviewing the document [Sign into the Admin Console](), where you will learn how access the console and verify your status as a system administrator.

## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the Onboarding Journey by reviewing the document [Sign into the Admin Console](), the following are some additional, optional resources that do a deeper dive on some concepts mentioned in this document, but they are not required to continue on the journey.

* [Admin Console Overview](https://helpx.adobe.com/enterprise/using/admin-console.html) - For more details on the Admin Console and how it works.
* [Admin Console again](/help/onboarding/learn-concepts/admin-console.md)
* [Create or update your Adobe ID](https://helpx.adobe.com/ca/manage-account/using/create-update-adobe-id.html#HowtocreateorupdateyourAdobeID) to learn more about Adobe IDs.