---
title: IMS Support for AEM as a Cloud Service
seo-title: IMS Support for AEM as a Cloud Service
description: IMS Support for AEM as a Cloud Service 
seo-description: IMS Support for AEM as a Cloud Service 
---

# IMS Support for AEM as a Cloud Service {#ims-support-for-aem-as-a-cloud-service}

## Introduction {#introduction}

* AEM as a Cloud Service includes Admin Console support for AEM  instances and Adobe IMS(Identity Management System) based authentication.
* Admin Console  allows customer admins to centrally manage all Experience Cloud users.
* Users and Groups can be assigned to product profiles associated with AEM instances, allowing them to log in to that instance.

## Key Highlights {#key-highlights}

AEM IMS authentication support is only for Author, Admin, Dev users etc. not external end users of customer site like site visitors etc.

* The Admin Console will represent customers as IMS Orgs and Author and Publish Instances in an environment as Product Context Instances; this will allow customer System and Product Admins to  manage access to instances.
* Product Profiles in Admin Console will determine which Instances a user can access.
* Customers will be able to use their own SAML 2 compliant IDPs for SSO.
* Only Enterprise or Federated IDs(for customer SSO) will be supported, no personal Adobe IDs.

## Architecture {#architecture}

IMS Authentication works using OAuth protocol between AEM and the Adobe IMS endpoint. Once a user has been added to IMS and has an Adobe Identity, they can log in to AEM Managed Services instances using IMS credentials.

The user login flow is shown below, the user will be redirected to IMS and optionally to the customer IDP for SSO and then redirected back to AEM.

![IMS Architecture](/help/assets/assets/ims1.png)

## How to Set Up {#how-to-set-up}

### Onboarding Organizations to Adobe Admin Console {#onboarding-orgs-to-adobe-admin-console}

The customer onboarding to Adobe Admin Console is a pre-requisite to using Adobe IMS for AEM authentication. 

As the first step, customers should have an Org provisioned in Adobe IMS. Adobe Enterprise customers are represented as IMS Orgs in [Adobe Admin Console](https://helpx.adobe.com/enterprise/using/admin-console.html) (the portal used by Adobe customers to manage their product entitlements for their users and groups.)

AEM customers should already have an Org provisioned, and as part of the IMS provisioning, the customer instances will be made available in Admin Console for managing user entitlements and access.

Once a customer exists as an IMS Org, this is the summary of the configuration workflows: 

![IMS Onboarding](/help/assets/assets/ims2.png)

1. The designated System Admin  receives an invite to log in to Cloud Manager, after logging into the Cloud manager, they System Admins can choose to provision AEM programs and environments or navigate to Admin Console for Administrative tasks.
1. The System Admin Claims Domain to confirm the ownership of the domain( e.g acme.com etc.)
1. The System Admin sets up User Directories
1. The System Admin does IDP configuration in Admin Console for SSO setup.
The AEM Admin manages the local groups and permissions and privileges as usual.

The Adobe Identity Management Basics including IDP configuration are covered [here](https://helpx.adobe.com/enterprise/using/set-up-identity.html).

Enterprise Administration and Admin Console usage is covered [here](https://helpx.adobe.com/enterprise/managing/user-guide.html).

### Onboarding Users in Admin Console {#onboarding-users-in-admin-console}

There are three ways to onboard users depending on the size of the customer and their preference: manually create users in Admin Console, upload a .csv file or sync users from the customer's enterprise Active Directory.

**Manual Addition through Admin Console UI**

Users and Groups can be manually created in the Admin Console UI, this method can be used if they do not have a large number of users to manage, e.g. less than 50 AEM users or if the customer is already using this method for administering other Adobe products e.g. Analytics, Target or Creative Cloud applications.

![User Onboarding](/help/assets/assets/ims3.png)

**File Upload in Admin Console UI**

For easy handling of user creation, a .csv file can be uploaded for adding users in bulk.

![File Upload](/help/assets/assets/ims4.png)

**User Sync Tool**

User Sync Tool(UST) enables our enterprise customers to create/manage Adobe users utilizing Active Directory (or other tested OpenLDAP directory services).  The target users are IT Identity Administrators (Enterprise Directory / System Admins) who will be able to install and configure the tool.  The open-source tool is customizable so that customers can have a developer modify it to suit their own particular requirements. 

When User Sync runs, it fetches a list of users from the organization’s Active Directory (or other data source) and compares it with the list of users within the Admin Console.  It then calls the Adobe User Management API so that the Admin Console is synchronized with the organization’s directory.  The change flow is entirely one-way; any edits made in the Admin Console do not get pushed out to the directory.

The tool allows the system admin to map user groups in the customer’s directory with product configuration and user groups in the Admin Console.

To set up User Sync, the organization needs to create a set of credentials in the same way they would use the [User Management API](https://www.adobe.io/apis/experienceplatform/umapi-new.html).

![User Sync Tool](/help/assets/assets/ims5.png)

User Sync Tool is distributed through the Adobe Github repo [at this location](https://github.com/adobe-apiplatform/user-sync.py/releases/latest).

>[!NOTE]
>
> A pre-release version 2.4RC1 is available with dynamic group creation support and can be found [here](https://github.com/adobe-apiplatform/user-sync.py/releases/tag/v2.4rc1).

The major features for this release are the ability to dynamically map new LDAP groups for user membership in the Admin Console, as well as dynamic user group creation. 

More information about the new group features can be found [at this location](https://github.com/adobe-apiplatform/user-sync.py/blob/v2/docs/en/user-manual/advanced_configuration.md#additional-group-options).

**User Sync Documentation**

Refer to the [UST documentation](https://adobe-apiplatform.github.io/user-sync.py/en/) for more details.

The User Sync Tool needs to register as an Adobe I/O client UMAPI using the procedure [here](https://adobe-apiplatform.github.io/umapi-documentation/en/UM_Authentication.html).

Adobe I/O Console Documentation can be found [here](https://www.adobe.io/apis/cloudplatform/console.html).

The User Management API that is used by the User Sync Tool is covered [here](https://www.adobe.io/apis/cloudplatform/umapi-new.html).

## Adobe Experience as a Cloud Service Configuration {#aem-configuration}

> [!NOTE]
>
>The AEM IMS configuration required will be auto-configured when the AEM environments and instances are provisioned, however, the customer admin may modify it as per their requirements( e.g Auto Group Membership, Group Mapping etc.) using method described [here](/help/implementing/deploying/deploying.md).

The overall approach is to configure Adobe IMS as an OAuth provider, the **Apache Jackrabbit Oak Default Sync Handler** can be modified just like for LDAP sync.

Here are the key OSGI configurations that can be modified to change properties like User Auto-Membership, Groups Mappings etc.

<!-- Arun to provide list of osgi configs -->

## How to Use {#how-to-use}

### Managing Products and User Access in Admin Console {#managing-products-and-user-access-in-admin-console}

When the customer Product Admin logs in to Admin Console, they will see multiple instances of the AEM Managed Services Product Context as shown below:

![Instances login](/help/assets/assets/ims6.png)

In this example, the org AEM-MS-Onboard has 32 instances spanning different topologies and environments like Stage, Prod etc. 

![Instances login2](/help/assets/assets/ims7.png)

Under each Product Context instance, there will be associated Product Profiles, these product profiles are used for assigning access to users and groups with the required privilege.

The **Administrator_xxx** profile will be used to grant Administrator privileges in the associated AEM instance while the **User_xxx** profile is used to add regular users.

Any users and groups added under this product profile will be able to login to that instance as shown in the example below:

![Product Profile](/help/assets/assets/ims8.png)

### Logging into Adobe Experience Manager as a Cloud Service (#logging-in-to-aem)

**Local Admin Login**

AEM can continue to support local logins for Admin users, the login screen has an option to log in locally:

![Local Login](/help/assets/assets/ims9.png)

<!-- the above image needs to be updated for skyline -->

**IMS Based Login**

For other users, the IMS based login can be used once IMS is configured on the instance, the user will first click on the Sign in with Adobe button as shown below:

![IMS Login](/help/assets/assets/ims10.png)

They will then be redirected to the IMS login screen and enter their credentials:

![IMS Login2](/help/assets/assets/ims11.png)

![IMS Login3](/help/assets/assets/ims12.png)

If a federated IDP is configured during initial Admin Console setup, then the user will be redirected to the customer IDP for SSO:

![IMS Login4](/help/assets/assets/ims13.png)

After authentication is complete, the user will be redirected back to AEM and logged in:

![IMS Login5](/help/assets/assets/ims14.png)

### Managing Permissions and ACLs in Adobe Experience Manager as a Cloud Service {#managing-permissions-in-aem}

The ACLs and permissions will continue to be managed in AEM, the user groups that are synced from IMS can be assigned to local groups where ACLs and Privileges are defined.

In the example below, we are adding synced groups to the local Dam_Users group as an example. 

The user is part of the following Groups in IMS:

![ACL1](/help/assets/assets/ims15.png)

When the user logs in, their Group Memberships are synced, as shown below:

![ACL2](/help/assets/assets/ims16.png)

In AEM, the user groups synced from IMS can be added as members to existing local groups, e.g. DAM Users. 

![ACL3](/help/assets/assets/ims17.png)

As shown below the group AEM-GRP_008 inherits the Permissions and Privileges of DAM Users, this is an effective way of managing Permissions for synced groups and is commonly used in LDAP based Authentication method as well.

![ACL3](/help/assets/assets/ims18.png)