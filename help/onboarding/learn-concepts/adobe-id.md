---
title: Learn what is an Adobe ID
description: This page describes introductory information about Adobe ID.
---

## Understand Adobe ID {#adobe-id}

An Adobe ID is simply the email you will use to login and access AEM as a Cloud Service or any of your Adobe solutions. This is the email ID that your System Administrator uses while setting your team up. By using your Adobe ID you keep all your Adobe plans and products associated with a single account.

>[!IMPORTANT]
>An Adobe ID is essential for a secure and personalized experience with Adobe applications and services, and is required when you want to buy Adobe products. Refer to [Create or update your Adobe ID](https://helpx.adobe.com/ca/manage-account/using/create-update-adobe-id.html#HowtocreateorupdateyourAdobeID) to learn more.

## Identity Types available in Adobe Admin Console {#identity-types}

Adobe’s identity management system helps admins create and manage user's access to applications and services. Refer to [Identity overview](https://helpx.adobe.com/enterprise/admin-guide.html/enterprise/using/identity.ug.html) to learn more.

Adobe offers the following identity types or accounts to authenticate and authorize users:

* **Personal ID**

   This is the default type of account. Basically, the user needs to create an account at [adobe.com](https://www.adobe.com/). In other words, this account is managed by Adobe and anybody can create an account of this type. 

* **Enterprise ID** 

   Organizations usually want to increase the control of the users’ accounts. With Enterprise ID, only system administrators can create these type of accounts and the organization owns these accounts; Adobe only hosts them.

* **Federated ID**

   This is  where the organization takes full ownership and control of the accounts. In this case, you need to integrate the Adobe Experience Cloud with your Security Assertion Markup Language (SAML) 2.0 single sign-on system. The final result is that users authenticate against their company’s single sign-on (SSO) system and not against an account hosted at Adobe.

   >[!NOTE]
   >AEM ships with a SAML authentication handler. This handler provides support for the SAML 2.0 Authentication Request Protocol (Web-SSO profile) using the HTTP POST binding. Refer to [SAML 2.0 Authentication Handler](https://experienceleague.adobe.com/docs/experience-manager-65/administering/security/saml-2-0-authenticationhandler.html#security) to learn more.