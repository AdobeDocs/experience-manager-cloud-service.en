---
title: Bulk Upload of Principals to IMS after using CTT
description: Overview of Bulk Upload files for groups and users, and how to use them on the Admin Console to create groups and users in IMS.
exl-id: 
---

# Bulk Upload of Principals to IMS after using CTT {#bulk-principal-uploading}

>[!CONTEXTUALHELP]
>id="bulk-principal-uploading"
>title="Bulk Upload of Principals"
>abstract="Overview of Bulk Upload files for groups and users, and how to use them on the Admin Console to create groups and users in IMS."
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/onboarding/journey/admin-console" text="AEM Admin Console documentation"
>additional-url="https://adminconsole.adobe.com/" text="AEM Admin Console"

## Introduction {#introduction}
Migrating content to the cloud using CTT and CAM creates groups on the AEM cloud instance, but it cannot do anything to put groups or users in IMS; but they need to exist in IMS to be properly managed by customers.  Fortunately there is functionality provided by Admin Console to create IMS groups and users in bulk.  The CAM ingestion aids this process by saving input files for this bulk creation, allowing customers to complete this Admin Console action as part of their overall migration process. Two kinds of bulk upload files are created: one for groups and one for users.

Also see [Manage users](https://helpx.adobe.com/ca/enterprise/using/users.html) for additional details about managing AEM as a Cloud Service users.

## General Rules for uploading files {#rules}
There are a few general guidelines for editing and using both kinds of upload files:
* Administrator access to the Admin Console must first be granted before these instructions can be followed.
* Note that there are a few different ways of creating users and group in IMS.  See [IMS Support for Adobe Experience Manager as a Cloud Service ](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/security/ims-support) to learn about all the options available.  Only the Admin Console bulk upload methods are described here.
* There are three Identity Types possible in IMS: Adobe ID, Enterprise ID, and Federated ID.  The instructions on this page are provided for **Adobe ID only**.  If you need to use Enterprise ID or Federated ID, please refer to the full [Admin Console documentation](https://helpx.adobe.com/ca/enterprise/using/admin-console.html) and also the specific documentation for [Admin Console Bulk Group upload](https://helpx.adobe.com/ca/enterprise/using/user-groups.html) and [Admin Console Bulk User upload](https://helpx.adobe.com/ca/enterprise/using/bulk-upload-users.html).  The specifications for the upload files are somewhat different for those two Identity Types.
* If a single CSV field allows multiple entries (such as multiple product profiles, multiple groups, or multiple admins) the entries must be contained withing double quotes and separated by a comma, i.e., "profile 1,profile 2".
  * Single quotes may be used for this case instead of double quotes, but editing the file in Microsoft Excel may result in parsing problems; if using Excel to edit these files, ensure you use double quotes instead of single quotes.

## Bulk Group Upload {#group-upload}
#### Use case: Groups have been migrated to AEM as a Cloud Service, but those groups are not present in IMS/Admin Console, so they need to be uploaded to IMS via the Admin Console.

To use the Admin Console's bulk group upload functionality after running a CTT/CAM migration, follow these steps:
1. Download the bulk group file from CAM
   * In CAM, go to Content Transfer and select Ingestion Jobs.
   * Click the ellipsis (...) on the line of the Ingestion in question, and choose "View principal summary".
   * On the dialog that appears, select select "Bulk Group File" from the dropdown list under "Download a file..." and click the Download button.
   * Save the resulting CSV file.
1. Edit the bulk group file
   * Each line represents a group to be uploaded, and has four fields (the fields' names make up the file's first line):
     * _User Group Name_ - The group name is required, and may contain a maximum of 255 characters.  This group name must be the same in IMS and AEM.
     * _Description_ - This field is optional, and may contain a maximum of 255 characters.
     * _User Group Admins_ - At least one group admin must be included in this field. Multiple admins can be assigned by separating each admin with a comma and enclosing the list within quotes. The entry for each admin must include the user's identity type, followed by a hyphen, and then the email address.  For example
       `"Adobe ID-myAdmin@example.com,Adobe ID-myOtherAdmin@example.com"`.  Do not include a space after the comma separating admins. You cannot include users (as admins) who are not currently part of the organization in the Admin Console.
     * _Assigned Product Profiles_ - This field is optional. You can assign multiple product profiles by separating each profile with a comma and enclosing the list within quotes. However, the product profiles that you include must already be set up for the organization. Ensure you specify the Product Profile name and not the product name.  Membership of Product Profiles assigned to a group will be inherited by all users placed in that group.  To find a product profile:
       * Go to Admin Console.
       * Find your Product (i.e., Adobe Experience Manager as a Cloud Service), and click on it.
       * Find your environment (instance), and click on it.
       * List the Product Profiles, and click on the one for your AEM env.  The product profile is at the top, i.e., "_AEM Users - author - Program 12345 - Environment 012345_".
   * When editing the CSV some applications may add additional quotes upon saving, which causes the processing to fail. It is good practice to inspect the raw CSV in a simple text editor to ensure that each field has only one opening and one closing quote (and they should not be "smart quotes"). 
1. Upload the bulk group file in the Admin Console
   * In the Admin Console, go to Users, then User Groups.
   * On the right side click the "..." button.  Choose **Add user groups by CSV** from the menu, and choose your CSV to upload; click Upload.
   * You'll get a response that the CSV is uploaded (to the Admin Console), but it is not imported to IMS yet.
   * Go to the same "..." menu and choose **Bulk operation results**.  It will show you a list of bulk upload attempts, and tell you (under Status) whether the bulk upload is processing, successful, or has failed.
      * At first it will show Processing, indicating it is not yet finished.
      * Once successfully completed, click on the Link **Add user groups** to see a simple status message for each line.
     * If instead it has failed, click on the small icon under File and it will give you a bit more information about why it failed.  The group line numbers are referenced starting at row 1.
1. Use Admin Console to verify your changes.
   
## Bulk User Upload and Edit {#bulk-user}
The Admin Console includes two separate actions for uploading and editing user details.  Instructions immediately below are for adding new users to IMS; instructions for editing existing IMS users are in the following section called Bulk User Edit.
### Bulk User Upload {#user-upload}
#### Use case: Groups have been migrated to AEM as a Cloud Service, and uploaded via Bulk upload or some other method.  Users might not be present in IMS/Admin Console, so they need to be uploaded and linked to their groups in IMS via the Admin Console.

To use the Admin Console's bulk user upload functionality, follow these steps:
1. Download the bulk user file from CAM
  * In CAM, go to Content Transfer and select Ingestion Jobs. 
  * Click the ellipsis (...) on the line of the Ingestion in question, and choose "View principal summary".
  * On the dialog that appears, select "Bulk User File" from the dropdown list under "Download a file..." and click the Download button.
  * Save the resulting CSV file.
  * NOTE: A user will appear in the Bulk User Upload file if it is in a group ingested during the same ingestion the file is created from.  It may also appear if the user is directly on an ACL or CUG of migrated content, or is a member of a built-in group or local group that is on an ACL or CUG of the migrated content. See [Group Migration](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/group-migration.md) for more information about these cases.
1. Edit the bulk user file
   * Each line represents a user to be uploaded, and has fifteen fields (the fields' names make up the file's first line).  Some fields are optional and are not described here; refer to [Bulk User CSV format](https://helpx.adobe.com/ca/enterprise/using/bulk-upload-users.html#csv-format).  The fields are:
     * _Identity Type_ - Optional.  If not specified, it will be created as an Adobe ID
     * _Username_ - Optional, and not used for Adobe ID uploads.
     * _Domain_ - Optional, and not used for Adobe ID uploads.
     * _Email_ - Required.  The email address will be used for verification the first time the user logs in.
     * _First Name_ - Optional.  Should be used because it appears, with Last Name, in several places.
     * _Last Name_ - Optional.  Should be used because it appears in several places.
     * _Country Code_ - Optional, and not used for Adobe ID uploads.
     * _ID_ - Optional, and not used for Adobe ID uploads.
     * _Product Configurations_ - Optional. This field will also be inherited from any groups the user is a member of.
     * _Admin Roles_ -  Optional. Use this field if the user is an Administrator. See [Bulk User CSV format](https://helpx.adobe.com/ca/enterprise/using/bulk-upload-users.html#csv-format) for details.
     * _Product Configurations Administered_ - Optional.  See [Bulk User CSV format](https://helpx.adobe.com/ca/enterprise/using/bulk-upload-users.html#csv-format) for details. This field will also be inherited from any groups the user is a member of.
     * _User Groups_ - Optional. A list of groups the user should be assigned to as a member.  Each group must be an already existing IMS group.  When the bulk user file is downloaded from CAM, this field is pre-populated with names of IMS-enabled group the user was a member of (directly or indirectly) before the migration.
     * _User Groups Administered_ - Optional.  See [Bulk User CSV format](https://helpx.adobe.com/ca/enterprise/using/bulk-upload-users.html#csv-format) for details. This field will also be inherited from any groups the user is a member of.
     * _Products Administered_ - Optional.  See [Bulk User CSV format](https://helpx.adobe.com/ca/enterprise/using/bulk-upload-users.html#csv-format) for details. This field will also be inherited from any groups the user is a member of.
     * _Contracts Administered_ - Optional.  See [Bulk User CSV format](https://helpx.adobe.com/ca/enterprise/using/bulk-upload-users.html#csv-format) for details.
     * _Developer Access_ - Optional.  See [Bulk User CSV format](https://helpx.adobe.com/ca/enterprise/using/bulk-upload-users.html#csv-format) for details.
     * _Auto Assigned Products_ - Optional.  See [Bulk User CSV format](https://helpx.adobe.com/ca/enterprise/using/bulk-upload-users.html#csv-format) for details.
   * When editing the CSV some applications may add additional quotes upon saving, which causes the processing to fail. It is good practice to inspect the raw CSV in a simple text editor to ensure that each field has only one opening and one closing quote (and they should not be "smart quotes").
1. Upload the bulk user file in the Admin Console
   * In the Admin Console, go to Users.
   * Click the **Add users by CSV** button.
   * Drag and Drop or Select a bulk user CSV file downloaded from CAM.
   * Click the Upload button.
   * You'll get a response that the CSV is uploaded (to the Admin Console), but it is not imported to IMS yet.
   * Go to the "..." menu on the right and choose **Bulk operation results**.  It will show you a list of bulk upload attempts, and tell you (under Status) whether the bulk upload is processing, successful, or has failed.
       * At first it will show Processing, indicating it is not yet finished.
       * Once successfully completed, click on the Link **Add users** to see a simple status message for each line.
       * If instead it has failed, click on the small icon under File and it will give you a bit more information about why it failed.  The user line numbers are referenced starting at row 1.
1. Use Admin Console to verify your changes.

>[!NOTE]
>After a non-wipe ingestion, it's possible that users that have been previously migrated and then created in IMS will appear in the Bulk User Upload file.  This could be for many reasons.  In this case, uploading the user again will fail.  Instead, try removing the user from the Bulk User Upload file and, if the user needs to be added to different groups, use the Bulk User Edit file as outlined below.

### Bulk User Edit {#user-edit}
#### Use case: Groups and users have been migrated to AEM as a Cloud Service, and uploaded via Bulk upload or some other method.  Now some changes need to be made to several users at once, such as adding them to an existing IMS group.

To use the Admin Console's bulk user edit functionality, follow these steps:
1. Download the bulk user file from Admin console
   * In the Admin Console, go to Users.
   * On the right side click the "..." button.  Choose **Edit user details by CSV** from the menu.
   * Click **Download CSV Template** and choose **Current Users**.  A CSV file should appear in your local Downloads folder.
1. Edit the bulk user file
   * In the Admin Console, go to Users.
   * Edit the CSV file using a text editor (recommended) or a spreadsheet application such as Excel.  Using an application may make unpredictable changes to the data, so it is recommended that after all edits are made, a text editor should be used to verify the formatting of the file.
   * Descriptions of the fields in this file are the same as above, under Bulk User Upload.
   * Remove all users that are not being edited.
   * If you change the User Groups field, leave current groups and add new ones as required. If you remove an existing group, the user will be taken out of that group in IMS.
   * When editing the CSV some applications may add additional quotes upon saving, which causes the processing to fail. It is good practice to inspect the raw CSV file in a simple text editor to ensure that each field has only one opening and one closing quote (and they should not be "smart quotes").
1. Upload the bulk user file in the Admin Console
   * In the Admin Console, go to Users.
   * On the right side click the "..." button.  Choose **Edit user details by CSV** from the menu.
   * Drag and Drop or Select the edited bulk user CSV file.
   * Click the Upload button.
   * You'll get a response that the CSV is uploaded (to the Admin Console), but it is not imported to IMS yet.
   * Go to the "..." menu on the right and choose **Bulk operation results**.  It will show you a list of bulk upload attempts, and tell you (under Status) whether the bulk upload is processing, successful, or has failed.
     * At first it will show Processing, indicating it is not yet finished.
     * Once successfully completed, click on the Link **Edit user details** to see a simple status message for each line.
     * If instead it has failed, click on the small icon under File and it will give you a bit more information about why it failed.  The user line numbers are referenced starting at row 1.
1. Use Admin Console to verify your changes.
