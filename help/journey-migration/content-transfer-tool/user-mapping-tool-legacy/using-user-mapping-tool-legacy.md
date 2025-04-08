---
title: Using User Mapping Tool (Legacy)
description: Using User Mapping Tool (Legacy)
exl-id: dcb750c4-0f81-4d11-ac6c-0592162b683d
hide: yes
hidefromtoc: yes
feature: Migration
role: Admin
---

# Using the User Mapping Tool (Legacy) {#using-user-mapping-tool}

>[!INFO]
>
>This documentation refers to a deprecated version of the tool. For more information on the latest version, see [Group Migration](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/group-migration.md).

The User Mapping Tool uses an API that allows it to look up Adobe Identity Management System (IMS) users by email and return their IMS IDs. This API requires the user to create a Client ID for their organization, a Client Secret, and an Access or Bearer Token.  

## Setting up the User Mapping Tool {#setting-up-user-mapping}

**Prerequisite:** User mapping requires that each user to be mapped to its IMS ID has an email address in its profile in AEM, and in IMS. Even if the user uses an email address as a user ID for logging in, mapping does not work for that user unless the email address is also in the profile, and also in IMS.

Follow the steps below to set this up:

1. Navigate to [Adobe Developer Console](https://developer.adobe.com/console/) using your Adobe ID.
1. Create a project or open an existing project.
1. Add an API - Click **Add to Project** and select **API**
1. Choose User Management API. You must have System Administrator permissions to have this option available.
1. Create a JWT credential.
1. Generate a key pair, or Upload a public key (rsa is no good). There is a button, **Generate a public/private keypair** that creates this keypair for you. Make sure you save both the public and private keys.
1. Navigate to the User Management API.
1. Generate an access token (or bearer token) by pasting your private key content into the text box and clicking **Generate Token**.
1. Save all this information such as **Client ID**, **Client Secret**, **Technical Account ID**, **Technical Account Email**, **Org ID**, and **Access Token** safely.

## Accessing the User Interface for User Mapping Tool {#user-interface}

The User Mapping Tool is integrated into the Content Transfer Tool. You can download the Content Transfer Tool from [Software Distribution Portal](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html). For more details on the latest version, see [Current Release Notes](/help/release-notes/release-notes-cloud/release-notes-current.md).

1. Select the Adobe Experience Manager and navigate to tools > **Operations** > **Content Migration**.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/user-mapping-access1.png)

1. Click the **User Mapping** card.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/user-mapping-access2.png)

1. Click **Create User Mapping Config**.

   >[!NOTE]
   >If you skip this step, users and groups mapping is skipped during the Extraction phase.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/user-mapping-access5.png)

   Populate the fields in **User Management API Configuration**, as described below.

    ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/user-mapping-access3.png)


   * **Org ID**:  Enter the Adobe Identity Management System (IMS) Org ID for the organization that the users are being migrated.  

      >[!NOTE]
      >To get the Org ID, log on to the [Admin Console](https://adminconsole.adobe.com/) and choose your organization (in the upper-right area) if you belong to more than one. The Org ID is in the URL of that page, in the format like `xx@AdobeOrg`, where xx is the IMS Org ID. Alternately, you can find the Org ID in the [Adobe Developer Console](https://developer.adobe.com/console/) page where you generate the Access Token.

   * **Client ID**: Enter the Client ID that you saved from the Setup step.

   * **Access Token**: Enter the Access Token that you saved from the Setup step.

      >[!NOTE]
      >The Access Token expires every 24 hours and a new one must be created. To create a token, go back into [Adobe Developer Console](https://developer.adobe.com/console/), choose your project, click **User Management API**, and paste the same private key into the box.

1. After populating the fields, click **Test Configuration** to test the connection to the User Management API service. If the connection is successful, you can click **Save** to save the configuration. 

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/user-mapping-access4.png)

1. After saving the configuration, select the configuration and click **Start User Mapping**.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/user-mapping-landing4.png)

1. Click **Start** from the dialog box so you start the User Mapping process.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/resume-user-mapping3.png)

   It displays the **Status** as **RUNNING**.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/user-mapping-start1.png)


1. After User Mapping is complete, click **Results** to view the summary.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/user-mapping-landing5.png)

   >[!IMPORTANT]
   >
   >* After User Mapping is complete, you can navigate back to Content Migration page using the breadcrumb. The User Mapping card displays the status and timestamp. Click **Content Transfer** so you can create a migration Set to run extraction. See [Running the Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/getting-started-content-transfer-tool.html#running-tool) for more details.

### Resuming the User Mapping Process {#resume-user-mapping-process}

If the User Mapping process is stopped due to any of the following reasons:

* The option **Stop User Mapping** was selected by the user.
* The access token expired during the process.
* Or, some other reason.

   >[!NOTE]
   >The progress is saved from where the process stopped. 
   
Follow the steps below to resume the User Mapping process:

1. Click **View Log** to review the User Mapping log so you can check the saved progress.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/resume-user-mapping1.png)

1. Click **Start User Mapping** button again to resume from where it left off. 

   >[!NOTE]
   >Ensure before restarting that the access token is still valid or has been refreshed.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/resume-user-mapping2.png)

1. Click **Start** from the dialog box so you resume the User Mapping process.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/resume-user-mapping3.png)

   After the User Mapping process completes, you can view the **Status** as **FINISHED** for that specific configuration.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/resume-user-mapping4.png)
