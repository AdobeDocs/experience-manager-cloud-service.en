---
title: Using User Mapping Tool
description: Using User Mapping Tool
exl-id: 88ce7ed3-46fe-4b3f-8e18-c7c8423faf24
---
# Using User Mapping Tool {#user-mapping-tool}

## Overview {#overview}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_usermapping"
>title="User Mapping Tool"
>abstract="The Content Transfer Tool helps you move users and groups from your existing AEM system to AEM as a Cloud Service. Existing users and groups need to be mapped to their IMS IDs to avoid duplicate users and groups on the Cloud Service author instance."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-user-mapping-tool.html?lang=en#important-considerations" text="Important Considerations for using User Mapping Tool"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-user-mapping-tool.html?lang=en#using-user-mapping-tool" text="Using User Mapping Tool"

As part of the transition journey to Adobe Experience Manager (AEM) as a Cloud Service, you need to move users and groups from your existing AEM system to AEM as a Cloud Service. This is done by the Content Transfer Tool. 

A major change to AEM as a Cloud Service is the fully integrated use of Adobe IDs for accessing the author tier.  This requires use of the [Adobe Admin Console](https://helpx.adobe.com/enterprise/using/admin-console.html) for managing users and user groups. The user-profile information is centralized in the Adobe Identity Management System (IMS) that provides single-sign-on across all Adobe cloud applications. For more details, refer to [Identity Management](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/overview/what-is-new-and-different.html?lang=en#identity-management). Because of this change, existing users and groups need to be mapped to their IMS IDs to avoid duplicate users and groups on the Cloud Service author instance.

### User Mapping Tool {#mapping-tool}

The Content Transfer Tool (without User Mapping) will migrate any users and groups associated with the content being migrated. The User Mapping Tool is a part of Content Transfer Tool, and its sole purpose is to modify the users and groups so that they can be recognized correctly by IMS, the single-sign-on functionality used by AEM as a Cloud Service. Once these modifications are done, the Content Transfer Tool migrates the specified content's users and groups as usual.

## Important Considerations {#important-considerations} 

### Exceptional cases {#exceptional-cases}

The following specific cases will be logged: 

1. If a user has no email address in the `profile/email` field of their *jcr* node the user or group in question will be migrated but not mapped.

1. If a given email is not found on the Adobe Identity Management System (IMS) system for the Organization ID used (or if the IMS ID cannot be retrieved for another reason) the user or group in question will be migrated but not mapped. 

1. If the user is currently disabled, it is treated the same as if it were not disabled. It will be mapped and migrated as normal, and will remain disabled on the cloud instance.

1. If a user exists on the target AEM Cloud Service instance with the same user name (rep:principalName) as one of the users on the source AEM instance the user or group in question will be not be migrated.

### Additional considerations {#additional-considerations}

* If the setting **Wipe existing content on Cloud instance before ingestion** is set, already transferred users on the Cloud Service instance will be deleted along with the entire existing repository and a new repository will be created to ingest content into. This also resets all settings including permissions on the target Cloud Service instance and is true for an admin user added to the **administrators** group. The admin user will need to be re-added to the **administrators** group to retrieve the access token for CTT.

* It is recommended to remove any existing user from the target Cloud Service AEM instance before running CTT with User Mapping. This is to prevent any conflict between migrating users from the source AEM instance to the target AEM instance. Conflicts will occur during ingestion if the same user exists on the source AEM instance and the target AEM instance. 

* When content top-ups are performed, if content is not transferred because it has not changed since the previous transfer, users and groups associated with that content will not be transferred either, even if the users and groups have changed in the meantime. This is because users and groups are migrated along with the content they are associated with.  

* If the target AEM Cloud Service instance has a user with a different user name but same email address as one of the users on the source AEM instance, and User Mapping is enabled, an error message will be written in the logs, and the source AEM user will not be transferred, as only one user with a given email address is allowed on the target system.

* If two users on the source AEM instance have the same email address, and User Mapping is enabled, an error message will be written in the logs and one of the source AEM users will not be transferred, as only one user with a given email address is allowed on the target system.


## Using the User Mapping Tool {#using-user-mapping-tool}

The User Mapping Tool uses an API that allows it to look up Adobe Identity Management System (IMS) users by email and return their IMS IDs. This API requires the user to create a Client ID for their organization, a Client Secret, and an Access or Bearer Token.  

Follow the steps below to set this up:

1. Navigate to [Adobe Developer Console](https://console.adobe.io) using your Adobe ID.
1. Create a new project or open an existing project.
1. Add an API - Click **Add to Project** and select **API**
1. Choose User Management API.  You might need to get permissions to have this option.
1. Create a JWT credential.
1. Generate a key pair, or Upload a public key (rsa is no good).  There is a button, **Generate a public/private keypair**, which will do this for you.  Make sure you save both the public and private keys.
1. Navigate to the User Management API.
1. Generate an access token (or or bearer token) by pasting your private key content into the text box and clicking **Generate Token**.
1. Save all this information such as **Client ID**, **Client Secret**, **Technical Account ID**, **Technical Account Email**, **Org ID**, and **Access Token** safely.

## User Interface {#user-interface}

The User Mapping Tool is integrated into the Content Transfer Tool. You can download the Content Transfer Tool from [Software Distribution Portal](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html). For more details on the latest version, refer to the [Current Release Notes](/help/release-notes/release-notes-cloud/release-notes-current.md).

1. Select the Adobe Experience Manager and navigate to tools -> **Operations** -> **User Mapping**.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets-user-mapping/user-mapping-landing1.png)

1. Click on **Create User Mapping Config**.

   >[!NOTE]
   >If you skip this step, users and groups mapping will be skipped during the Extraction phase.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets-user-mapping/user-mapping-landing2.png)

   Populate the fields in **User Management API Configuration**, as described below.

    ![image](/help/move-to-cloud-service/content-transfer-tool/assets-user-mapping/user-mapping-landing3.png)

   * **Org ID**:  Enter the Adobe Identity Management System (IMS) Org ID for the organization the users are being migrated.  

      >[!NOTE]
      >To get the Org ID, log into the [Admin Console](https://adminconsole.adobe.com/) and choose your organization (in the top right area) if you belong to more than one. The Org ID will be in the URL of that page, in the format like `xx@AdobeOrg`, where xx is the IMS Org ID.  Alternately, you can find the Org ID in the [Adobe Developer Console](https://console.adobe.io) page where you generate the Access Token.

   * **Client ID**: Enter the Client ID that you saved from the Setup step.

   * **Access Token**: Enter the Access Token that you saved from the Setup step.

      >[!NOTE]
      >The Access Token expires every 24 hours and a new one needs to be created. To create a new token, go back into [Adobe Developer Console](https://console.adobe.io), choose your project, click on **User Management API** and paste the same private key into the box.

1. After populating the fields, click on **Test Configuration** to test the connection to the User Management API service. If the connection is successful, you will be able to click on **Save** to save the configuration. 

1. After saving the configuration, select the configuration and click on **Start User Mapping**.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets-user-mapping/user-mapping-landing4.png)

1. Once User Mapping is complete, click on **Results** to view the summary.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets-user-mapping/user-mapping-landing5.png)

   >[!IMPORTANT]
   >Once User Mapping is complete, you can navigate back to Content Migration page using the breadcrumb. The User Mapping card displays the status and timestamp. Click on **Content Transfer** to create a migration Set to run extraction. Refer to [Running the Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html?lang=en#running-tool) for more details.
