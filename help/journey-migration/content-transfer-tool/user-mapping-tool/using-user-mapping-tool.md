---
title: Using User Mapping Tool
description: Using User Mapping Tool
exl-id: dcb750c4-0f81-4d11-ac6c-0592162b683d
---
# Using the User Mapping Tool {#using-user-mapping-tool}

The User Mapping Tool uses an API that allows it to look up Adobe Identity Management System (IMS) users by email and return their IMS IDs. This API requires the user to create a Client ID for their organization, a Client Secret, and an Access or Bearer Token.  

## Setting up the User Mapping Tool {#setting-up-user-mapping}

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

## Accessing the User Interface for User Mapping Tool {#user-interface}

The User Mapping Tool is integrated into the Content Transfer Tool. You can download the Content Transfer Tool from [Software Distribution Portal](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html). For more details on the latest version, refer to the [Current Release Notes](/help/release-notes/release-notes-cloud/release-notes-current.md).

1. Select the Adobe Experience Manager and navigate to tools -> **Operations** -> **Content Migration**.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/user-mapping-access1.png)

1. Click on **User Mapping** card.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/user-mapping-access2.png)

1. Click on **Create User Mapping Config**.

   >[!NOTE]
   >If you skip this step, users and groups mapping will be skipped during the Extraction phase.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/user-mapping-access5.png)

   Populate the fields in **User Management API Configuration**, as described below.

    ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/user-mapping-access3.png)


   * **Org ID**:  Enter the Adobe Identity Management System (IMS) Org ID for the organization the users are being migrated.  

      >[!NOTE]
      >To get the Org ID, log into the [Admin Console](https://adminconsole.adobe.com/) and choose your organization (in the top right area) if you belong to more than one. The Org ID will be in the URL of that page, in the format like `xx@AdobeOrg`, where xx is the IMS Org ID.  Alternately, you can find the Org ID in the [Adobe Developer Console](https://console.adobe.io) page where you generate the Access Token.

   * **Client ID**: Enter the Client ID that you saved from the Setup step.

   * **Access Token**: Enter the Access Token that you saved from the Setup step.

      >[!NOTE]
      >The Access Token expires every 24 hours and a new one needs to be created. To create a new token, go back into [Adobe Developer Console](https://console.adobe.io), choose your project, click on **User Management API** and paste the same private key into the box.

1. After populating the fields, click on **Test Configuration** to test the connection to the User Management API service. If the connection is successful, you will be able to click on **Save** to save the configuration. 

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/user-mapping-access4.png)

1. After saving the configuration, select the configuration and click on **Start User Mapping**.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/user-mapping-landing4.png)

1. Click on **Start** from the the dialog box to start the User Mapping process.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/resume-user-mapping3.png)

   It displays the **Status** as **RUNNING**.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/user-mapping-start1.png)


1. Once User Mapping is complete, click on **Results** to view the summary.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/user-mapping-landing5.png)

   >[!IMPORTANT]
   >* Once User Mapping is complete, you can navigate back to Content Migration page using the breadcrumb. The User Mapping card displays the status and timestamp. Click on **Content Transfer** to create a migration Set to run extraction. Refer to [Running the Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html?lang=en#running-tool) for more details.

### Resuming the User Mapping Process {#resume-user-mapping-process}

If the User Mapping process is stopped due to any of the following reasons:

* The user selected **Stop User Mapping**
* the access token expired during the process or,
* some other reason

   >[!NOTE]
   >The progress is saved from where the process stopped. 
   
Follow the steps below to resume the User Mapping process:

1. Click on **View Log** to review the User Mapping log to check the saved progress.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/resume-user-mapping1.png)

1. Click on the **Start User Mapping** button again to resume from where it left off. 

   >[!NOTE]
   >Ensure before restarting that the access token is still valid or has been refreshed.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/resume-user-mapping2.png)

1. Click on **Start** from the the dialog box to resume the User Mapping process.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/resume-user-mapping3.png)

   Once the User Mapping process completes, you will view the **Status** as **FINISHED** for that specific configuration.

   ![image](/help/journey-migration/content-transfer-tool/assets-user-mapping/resume-user-mapping4.png)
