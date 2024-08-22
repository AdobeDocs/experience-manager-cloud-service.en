---
title: IMS Support for Adobe Experience Manager as a Cloud Service
description: Image Management System support for Adobe Experience Manager as a Cloud Service.
exl-id: fb563dbd-a761-4d83-9da1-58f8e462b383
feature: Security
role: Admin
---
# IMS Support for Adobe Experience Manager as a Cloud Service {#ims-support-for-aem-as-a-cloud-service}

## Introduction {#introduction}

* AEM as a Cloud Service includes Admin Console support for AEM instances and Adobe Identity Management System (IMS for short) based authentication.
* The Admin Console allows administrators to centrally manage all Experience Cloud users.
* Users and Groups can be assigned to product profiles associated with an AEM as a Cloud Service instance, allowing them to log on to that instance.

>[!TIP]
>
>See [Configure Access to AEM for Administrators](https://experienceleague.adobe.com/?recommended=ExperienceManager-A-1-2020.1.aem) for an introduction to how users authenticate using Adobe IMS to AEM as a Cloud Service. Also learn how Adobe IMS Users, User Groups, and Product Profiles are used to control access to AEM and its features and functionalities. Adobe ID required.

## Key Highlights {#key-highlights}

AEM as a Cloud Service offers IMS authentication support only for Author, Admin, and Dev users. It does not offer support for external end users of customer sites like site visitors.

* The Admin Console represents customers as IMS Organizations, Author, and Publish Instances in an environment as Product Context Instances. This representation allows System and Product administrators to manage access to instances.
* Product Profiles in the Admin Console determine which Instances that a user can access.
* Customers can use their own SAML 2 compliant Identity Providers (IDP for short) for Single Sign On.
* Only Enterprise or Federated IDs for customer Single Sign On are supported, no personal Adobe IDs.

## Architecture {#architecture}

IMS Authentication works using OAuth protocol between AEM and the Adobe IMS endpoint. Once a user has been added to IMS and has an Adobe Identity, they can log in to AEM author service using IMS credentials.

The user logon flow is shown below, the user is redirected to IMS and optionally to the customer IDP for SSO and then redirected back to AEM.

![IMS Architecture](/help/security/assets/ims1.png)

## How to Set Up {#how-to-set-up}

### Onboarding Organizations to Adobe Admin Console {#onboarding-orgs-to-adobe-admin-console}

The customer onboarding to Adobe Admin Console is a prerequisite to using Adobe IMS for AEM authentication.

As the first step, customers must have an Organization that is provisioned in Adobe IMS. Adobe Enterprise customers are represented as IMS Organizations in the [Adobe Admin Console](https://helpx.adobe.com/enterprise/using/admin-console.html). This area is the portal used by Adobe customers to manage their product entitlements for their users and groups.

AEM customers should already have an Organization that is provisioned, and as part of the IMS provisioning, the customer instances are made available in Admin Console for managing user entitlements and access.

After a customer exists as an IMS Organization, they have to configure their system as summarized in the following:

![IMS Onboarding](/help/security/assets/ims2.png)

1. The designated System Administrator receives an invitation to log in to Cloud Manager. After logging into Cloud manager, the System Administrators can choose to provision AEM programs, and environments, or navigate to Admin Console for Administrative tasks.
1. The System Administrator claims a domain to confirm the ownership of the respective domain (for example, acme.com)
1. The System Administrator sets up User Directories
1. The System Administrator does IDP configuration in Admin Console to set up Single Sign-On.
1. The AEM Administrator manages the local groups and permissions and privileges as usual.

The Adobe Identity Management basics including IDP configuration are covered under [Set up identity and Single Sign-On](https://helpx.adobe.com/enterprise/using/set-up-identity.html).

Enterprise Administration and Admin Console usage are covered under [Welcome to the enterprise and teams admin guide](https://helpx.adobe.com/enterprise/admin-guide.html).

### Onboarding Users in Admin Console {#onboarding-users-in-admin-console}

There are three ways to onboard users. Each method depends on the size of the customer and their preference. You can manually create users in Admin Console, upload a .csv file, or sync users from the customer's enterprise Active Directory.

**Manual Addition through Admin Console UI**

Users and Groups can be manually created in the Admin Console UI. This method can be used if you do not have many users to manage. For example, less than 50 AEM users, or if you are already using this method for administering other Adobe products like Analytics, Target or Creative Cloud applications.

![User Onboarding](/help/security/assets/ims3.png)

**File Upload in Admin Console UI**

For easy handling of user creation, a `.csv` file can be uploaded for adding users in bulk.

![File Upload](/help/security/assets/ims4.png)

**User Sync Tool**

User Sync Tool (UST in short) enables Adobe enterprise customers to create and manage Adobe users using Active Directory. This UST also works for other tested OpenLDAP directory services. The target users are IT Identity Administrators (Enterprise Directory or System Admins) who are able to install and configure the tool. The open-source tool is customizable so that customers that you modify it to suit your own particular requirements.

When User Sync runs, it fetches a list of users from the organization's Active Directory and compares it with the list of users within the Admin Console. It then calls the Adobe User Management API so that the Admin Console is synchronized with the organization's directory. The change flow is entirely one way. Any edits made in the Admin Console do not get pushed out to the directory.

The tool lets the system admin to map user groups in the customer's directory with product configuration and user groups in the Admin Console.

To set up User Sync, the organization must create a set of credentials in the same way they would use the [User Management API](https://developer.adobe.com/umapi/).

![User Sync Tool](/help/security/assets/ims5.png)

User Sync Tool is distributed through the Adobe GitHub repository [at this location](https://github.com/adobe-apiplatform/user-sync.py/releases/tag/v2.9.0rc2).

>[!NOTE]
>
>A prerelease version **2.4RC1** is available with dynamic group creation support under [User Sync Tool v2.4rc1 on GitHub](https://github.com/adobe-apiplatform/user-sync.py/releases/tag/v2.4rc1).

The major features for this release are the ability to dynamically map new LDAP groups for user membership in the Admin Console, and dynamic user group creation.

More information about the new group features can be found at [Adobe User Sync Tool - Additional Group Options](https://adobe-apiplatform.github.io/user-sync.py/en/user-manual/advanced_configuration.html#additional-group-options).

**User Sync Documentation**

See:

* [UST documentation](https://adobe-apiplatform.github.io/user-sync.py/en/) 

* the User Sync Tool must register as an Adobe Developer client UMAPI using the procedure from [Authentication for API Access](https://adobe-apiplatform.github.io/umapi-documentation/en/UM_Authentication.html)

* the [Adobe Developer Console Documentation](https://developer.adobe.com/developer-console/)

* the [User Management API that is used by the User Sync Tool](https://adobe-apiplatform.github.io/user-sync.py/en/)

## Adobe Experience as a Cloud Service Configuration {#aem-configuration}

>[!NOTE]
>
>The AEM IMS configuration required is automatically configured when the AEM environments and instances are provisioned. However, the administrator may modify it as per their requirements, see [Deploying to AEM as a Cloud Service](/help/implementing/deploying/overview.md).

The AEM IMS configuration required is auto-configured when the AEM environments and instances are provisioned. Customer administrators may modify part of the configuration as per their requirements

The overall approach is to configure Adobe IMS as an OAuth provider. The **Apache Jackrabbit Oak Default Sync Handler** can be modified just like for LDAP synchronization.

Below are the key OSGI configurations that must be modified to change properties like User Auto Membership or Groups Mappings.

<!-- Arun to provide list of osgi configs -->

## How to Use {#how-to-use}

### Managing Products and User Access in Admin Console {#managing-products-and-user-access-in-admin-console}

When the Product Administrator logs on to Admin Console, they see multiple instances of the AEM as a Cloud Service Product Context, as shown below. For example, select any of the products from the **Overview** page:

![Instances login](/help/security/assets/ims6.png)

You see a list of existing instances:

![Instances login2](/help/security/assets/ims7.png)

Under each Product Context instance, there are instances spanning Author or Publish services across Production, Stage, or Development environments. Each instance is associated to Product Profiles or Cloud Manager roles. These product profiles are used for assigning access to Users and Groups with the required privileges.

The **AEM Administrators_xxx** profile is used to grant Administrator privileges in the associated AEM instance while the **AEM Users_xxx** profile is used to add regular users.

Any users and groups added under this product profile are able to log on to that instance as shown in the example below:

![Product Profile](/help/security/assets/ims8.png)

>[!WARNING]
>
>Do not change the **AEM Administrators** product profile name. Changing the name of the **AEM Administrators** product profile removes administrator rights from all users assigned to that profile.

### Logging into Adobe Experience Manager as a Cloud Service {#logging-in-to-aem}

**Local Administrator Login**

AEM can continue to support local logins for Admin users. The logon screen lets you log on locally:

![Local Login](/help/security/assets/ims9.png)

<!-- the above image must be updated for skyline -->

**IMS-Based Login**

For other users, the IMS-based logon is used after IMS is configured on the instance. The user clicks the Sign-in with Adobe button as shown below:

![IMS Login](/help/security/assets/ims10.png)


>[!NOTE]
>
>Any user created in IMS can be created using Adobe ID or Federated ID. If a user is setup using Federated ID, they are authenticated using their Company's Identity Provider to log on.

They are redirected to the IMS logon screen and must enter their credentials:

![IMS Login2](/help/security/assets/ims11.png)

![IMS Login3](/help/security/assets/ims12.png)

If a federated IDP is configured during initial Admin Console setup, then the user is redirected to the customer IDP for SSO:

![IMS Login4](/help/security/assets/ims13.png)

After authentication is complete, the user is redirected back to AEM and logged in:

![IMS Login5](/help/security/assets/ims14.png)

### Managing Permissions and ACLs in Adobe Experience Manager as a Cloud Service {#managing-permissions-in-aem}

The ACLs and permissions continue to be managed in AEM. The User Groups that are synced from IMS can be assigned to local groups where ACLs and privileges are defined.

In the example below, synced groups are added to the local **Dam_Users** group as an example.

The user is part of the following Groups in IMS:

![ACL1](/help/security/assets/ims15.png)

When the user logs in, their Group Memberships are synced, as shown below:

![ACL2](/help/security/assets/ims16.png)

In AEM, the User Groups synced from IMS can be added as members to existing local groups, like **DAM Users**.

![ACL3](/help/security/assets/ims17.png)

As shown below, the group **AEM-GRP_008** inherits the permissions and privileges of **DAM Users**. This inheritance is an effective way of managing permissions for synced groups and is commonly used in the LDAP-based Authentication method.

![ACL3](/help/security/assets/ims18.png)


### Accessing Cloud Manager {#accessing-cloud-manager}

To be able to access Cloud Manager or to environments on AEM as a Cloud Service, you must be assigned to Profiles of the Cloud Manager Product.

See Role Definitions if you want to learn more about roles for users which govern the availability of specific features in Cloud Manager.

>[!NOTE]
>Cloud Manager has pre-configured roles with appropriate permissions. To learn about each of the roles with specific permissions, pre-configured tasks, or permissions, associated with each role, see [Role-Based Permissions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/requirements/role-based-permissions).

**Steps for Adding a User**

1. Add a user to a particular profile either from an existing user's screen or from a new user screen. 

1. Alternatively, you can also add a user from the **Overview** screen, as shown in the figure below.

   ![ACL3](/help/security/assets/ims23.png)

   >[!NOTE]
   >You can assign more than one profile to a user as shown in the figure below.

   ![ACL3](/help/security/assets/ims22.png)


1. Once you have been added to the appropriate profile, you should be able to access the respective tenants in Cloud Manager by way of [Adobe Experience Cloud](https://my.cloudmanager.adobe.com) using the upper-right corner from the user interface.


### Accessing an Instance in AEM as a Cloud Service {#accessing-instance-cloud-service}

>[!IMPORTANT]
>The steps mentioned in the preceding section must have already been completed before you are granted access to an instance in AEM as a Cloud Service.

To have access to an AEM instance within the **Admin Console**, you should see the Cloud Manager Program and the environments within the program in the product list on the **Admin Console**.

For example, in the screenshot below, you see two available environments namely *dev author* and a *publish*.

![ACL3](/help/security/assets/ims19.png)

To get access to AEM instances, the user must be added to a group of the appropriate Cloud Service Product.

Every author instance has an AEM Administrators and AEM Users Profile and every publish instance has an AEM Users Profile. You can add other profiles as needed. 

To get admin level access to the AEM instance, add the user to the AEM Administrators Profile for that particular Product.
